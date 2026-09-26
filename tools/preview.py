#!/usr/bin/env python3
"""Dependency-free, read-only browser preview for this Markdown corpus."""
import argparse
from hashlib import sha256
from html import escape
from http.server import BaseHTTPRequestHandler, ThreadingHTTPServer
import json
from pathlib import Path
import re
from urllib.parse import quote, unquote, urlsplit
import webbrowser

from check_network import ROOT, LINK, metadata, heading_anchor, markdown_headings, visible_text, expected_type

ASSETS = Path(__file__).with_name('preview')


def resolve_link(path, ref):
    url = urlsplit(ref)
    if url.scheme or url.netloc:
        return None
    target = (ROOT / path).parent / unquote(url.path) if url.path else ROOT / path
    target = target.resolve()
    if not target.is_relative_to(ROOT) or target.suffix != '.md':
        return None
    return target.relative_to(ROOT).as_posix(), unquote(url.fragment)


def href(path, ref):
    local = resolve_link(path, ref)
    if local:
        target, fragment = local
        return '#/' + quote(target, safe='/') + ('#' + quote(fragment) if fragment else '')
    if urlsplit(ref).scheme in ('https', 'http', 'mailto'):
        return ref
    return '#'


def inline(text, path):
    # Escape source HTML; only this renderer emits markup.
    tokens = []
    def hold(value):
        tokens.append(value)
        return '\x00' + str(len(tokens) - 1) + '\x00'
    text = re.sub(r'`([^`]+)`', lambda m: hold('<code>' + escape(m[1]) + '</code>'), text)
    text = LINK.sub(lambda m: hold('<a href="' + escape(href(path, m[1]), quote=True) + '">' + escape(m[0][1:m[0].index('](')]) + '</a>'), text)
    text = escape(text)
    text = re.sub(r'\*\*(.+?)\*\*', r'<strong>\1</strong>', text)
    text = re.sub(r'(?<!\w)\*([^*]+)\*', r'<em>\1</em>', text)
    return re.sub(r'\x00(\d+)\x00', lambda m: tokens[int(m[1])], text)


def render(body, path):
    """Render the corpus's headings, paragraphs, lists, tables, quotes and code."""
    lines = body.splitlines()
    out, seen = [], set()
    i = 0
    def special(line):
        return re.match(r'^(#{1,6}\s|```|\s*[-*+]\s|\s*\d+[.)]\s|>|\|)', line)
    while i < len(lines):
        line = lines[i]
        if not line.strip():
            i += 1
            continue
        if line.startswith('```'):
            code = []
            i += 1
            while i < len(lines) and not lines[i].startswith('```'):
                code.append(lines[i]); i += 1
            out.append('<pre><code>' + escape('\n'.join(code)) + '</code></pre>')
        elif m := re.match(r'^(#{1,6})\s+(.+?)\s*$', line):
            level, title = len(m[1]), m[2]
            anchor = heading_anchor(title, seen)
            out.append(f'<h{level} id="{escape(anchor)}">{inline(title, path)}</h{level}>')
        elif line.startswith('|') and i + 1 < len(lines) and re.match(r'^\|[\s:|\-]+\|\s*$', lines[i + 1]):
            cells = lambda row: row.strip().strip('|').split('|')
            out.append('<div class="table-wrap"><table><thead><tr>' + ''.join('<th>' + inline(c.strip(), path) + '</th>' for c in cells(line)) + '</tr></thead><tbody>')
            i += 2
            while i < len(lines) and lines[i].startswith('|'):
                out.append('<tr>' + ''.join('<td>' + inline(c.strip(), path) + '</td>' for c in cells(lines[i])) + '</tr>')
                i += 1
            out.append('</tbody></table></div>')
            continue
        elif m := re.match(r'^\s*([-*+]|\d+[.)])\s+(.*)', line):
            ordered = m[1][0].isdigit()
            tag = 'ol' if ordered else 'ul'
            pattern = r'^\s*\d+[.)]\s+(.*)' if ordered else r'^\s*[-*+]\s+(.*)'
            out.append('<' + tag + '>')
            while i < len(lines) and (m := re.match(pattern, lines[i])):
                item = m[1]; i += 1
                while i < len(lines) and lines[i].strip() and not special(lines[i]):
                    item += ' ' + lines[i].strip(); i += 1
                out.append('<li>' + inline(item, path) + '</li>')
            out.append('</' + tag + '>')
            continue
        elif line.startswith('>'):
            paragraphs, paragraph = [], []
            while i < len(lines) and lines[i].startswith('>'):
                quoted = lines[i][1:].removeprefix(' ')
                if quoted.strip():
                    paragraph.append(quoted)
                elif paragraph:
                    paragraphs.append(' '.join(paragraph))
                    paragraph = []
                i += 1
            if paragraph:
                paragraphs.append(' '.join(paragraph))
            out.append('<blockquote>' + ''.join('<p>' + inline(p, path) + '</p>' for p in paragraphs) + '</blockquote>')
            continue
        else:
            paragraph = [line]
            i += 1
            while i < len(lines) and lines[i].strip() and not special(lines[i]):
                paragraph.append(lines[i]); i += 1
            out.append('<p>' + inline(' '.join(paragraph), path) + '</p>')
            continue
        i += 1
    return '\n'.join(out)


def snapshot():
    docs, edges, digest = [], [], sha256()
    paths = sorted(p for p in ROOT.rglob('*.md') if not any(part.startswith('.') for part in p.relative_to(ROOT).parts) and not p.is_symlink())
    for file in paths:
        path, source = file.relative_to(ROOT).as_posix(), file.read_text(encoding='utf-8')
        digest.update((path + '\0' + source).encode())
        error = ''
        expected = expected_type(file, ROOT)
        try:
            parsed = metadata(source)
            meta = parsed or {}
            if expected and parsed is None:
                error = f'Missing front matter for {expected} record'
            elif expected and meta.get('type') != expected:
                error = f'Expected record type: {expected}'
            elif expected:
                missing = [key for key in ('id', 'status') if not isinstance(meta.get(key), str) or not meta[key]]
                if missing:
                    error = 'Missing or invalid ' + ', '.join(missing)
        except ValueError as exc:
            meta, error = {}, str(exc)
        body = source.split('\n---\n', 1)[1] if source.startswith('---\n') and '\n---\n' in source else source
        title = re.search(r'^# (.+)$', body, re.M)
        labels = {anchor: visible_text(heading) for _, heading, anchor, _, _ in markdown_headings(body)}
        status = meta.get('status', '')
        docs.append(dict(path=path, title=visible_text(title[1]) if title else file.stem, type=expected or meta.get('type', 'guide'), status=status if isinstance(status, str) else '', html=render(body, path), text=visible_text(body), anchors=labels, error=error))
        typed = {}
        for rel in meta.get('relations', []):
            if isinstance(rel, dict) and isinstance(rel.get('target'), str):
                target = resolve_link(path, rel['target'])
                if target:
                    typed[target] = rel
        targets = {target for ref in LINK.findall(body) if (target := resolve_link(path, ref))}
        for target in sorted(targets | typed.keys()):
            rel = typed.get(target, {})
            edges.append(dict(source=path, target=target[0], fragment=target[1], type=rel.get('type', 'link'), status=rel.get('status', '')))
    return dict(version=digest.hexdigest(), docs=docs, edges=edges)


class Handler(BaseHTTPRequestHandler):
    def do_GET(self):
        route = urlsplit(self.path).path
        if route == '/api/network':
            try:
                content = json.dumps(snapshot()).encode()
            except (OSError, ValueError, TypeError) as exc:
                self.send_error(500, str(exc)); return
            kind = 'application/json; charset=utf-8'
        elif route in ('/', '/app.js', '/style.css'):
            file = ASSETS / {'/': 'index.html', '/app.js': 'app.js', '/style.css': 'style.css'}[route]
            content = file.read_bytes()
            kind = {'/': 'text/html', '/app.js': 'text/javascript', '/style.css': 'text/css'}[route] + '; charset=utf-8'
        else:
            self.send_error(404); return
        self.send_response(200)
        self.send_header('Content-Type', kind)
        self.send_header('Cache-Control', 'no-store')
        self.send_header('X-Content-Type-Options', 'nosniff')
        self.end_headers()
        self.wfile.write(content)

    def log_message(self, *args):
        pass


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--port', type=int, default=8000)
    parser.add_argument('--no-browser', action='store_true')
    args = parser.parse_args()
    try:
        server = ThreadingHTTPServer(('127.0.0.1', args.port), Handler)
    except OSError as exc:
        parser.exit(1, f'Cannot start preview: {exc}. Try --port 8001.\n')
    url = f'http://localhost:{server.server_port}'
    print(f'Agora: {url}\nPress Ctrl+C to stop.', flush=True)
    if not args.no_browser:
        webbrowser.open(url)
    try:
        server.serve_forever()
    except KeyboardInterrupt:
        pass
    finally:
        server.server_close()


if __name__ == '__main__':
    main()
