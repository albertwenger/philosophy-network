#!/usr/bin/env python3
"""Check Markdown network structure; this does not validate the philosophy."""
from pathlib import Path
from collections import Counter
from urllib.parse import unquote, urlsplit
import argparse
import json
import re
import statistics
import sys

ROOT = Path(__file__).resolve().parents[1]
TYPES = {'proposal', 'concept', 'person', 'source'}
RELATIONS = {'uses-sense'}
LINK = re.compile(r'(?<!!)\[[^\]\n]+\]\(([^\s)]+)\)')


def metadata(text):
    if not text.startswith('---\n'):
        return None
    end = text.find('\n---\n', 4)
    if end < 0:
        raise ValueError('Unclosed front matter')
    result = {}
    for line in text[4:end].splitlines():
        key, sep, value = line.partition(':')
        if not sep or key in result:
            raise ValueError('Invalid or duplicate front-matter key')
        result[key] = json.loads(value.strip())
    return result


def section(text, title):
    m = re.search(r'^## ' + re.escape(title) + r'\n\n(.*?)(?=\n## |\Z)', text, re.M | re.S)
    return m.group(1).strip() if m else ''


def visible_text(text):
    """Read Markdown link labels without treating destinations as prose."""
    return LINK.sub(lambda m: m[0][1:m[0].index('](')], text)


def heading_anchor(title, seen):
    """Create the same ordinary heading fragment in the checker and preview."""
    base = re.sub(r'[^\w\- ]', '', visible_text(title).lower()).replace(' ', '-')
    anchor, suffix = base, 0
    while anchor in seen:
        suffix += 1
        anchor = f'{base}-{suffix}'
    seen.add(anchor)
    return anchor


def markdown_headings(text):
    scanned = without_fenced_code(text)
    seen = set()
    for match in re.finditer(r'^(#{1,6})[ \t]+(.+?)[ \t]*$', scanned, re.M):
        yield len(match[1]), match[2], heading_anchor(match[2], seen), match.start(), match.end()


def heading_sections(text, level=2):
    """Find sections by their actual heading positions, including repeated titles."""
    headings = list(markdown_headings(text))
    result = {}
    for i, (depth, title, anchor, _, start) in enumerate(headings):
        if depth != level:
            continue
        end = next((item[3] for item in headings[i + 1:] if item[0] <= level), len(text))
        result[anchor] = (title, text[start:end].strip())
    return result


def words(text):
    return len(re.findall(r"\b[^\W_]+(?:[’'-][^\W_]+)*\b", visible_text(text)))


def without_fenced_code(text):
    """Mask fenced examples while preserving offsets into the source text."""
    return re.sub(r'^```[^\n]*\n.*?(?:^```[^\n]*(?:\n|$)|\Z)',
                  lambda m: re.sub(r'[^\n]', ' ', m[0]), text, flags=re.M | re.S)


def anchor_counts(text):
    return Counter(heading[2] for heading in markdown_headings(text))


def anchors(text):
    return set(anchor_counts(text))


def run(report=False):
    errors = []
    files = {p.resolve(): p.read_text(encoding='utf-8') for p in ROOT.rglob('*.md') if '.git' not in p.parts}
    records, by_id = {}, {}

    def error(p, msg):
        errors.append(f'{p.relative_to(ROOT)}: {msg}')

    for p, text in files.items():
        try:
            meta = metadata(text)
        except ValueError as exc:
            error(p, str(exc))
            continue
        if meta is None:
            continue
        records[p] = meta
        for key in ('id', 'type', 'status'):
            if not isinstance(meta.get(key), str) or not meta[key]:
                error(p, f'Missing or invalid {key}')
        if meta.get('type') not in TYPES:
            error(p, 'Unknown record type')
        ident = meta.get('id')
        if ident in by_id:
            error(p, f'Duplicate ID {ident}')
        else:
            by_id[ident] = p

    def target(p, ref):
        parsed = urlsplit(ref)
        if parsed.scheme or parsed.netloc:
            return None
        q = (p.parent / unquote(parsed.path)).resolve() if parsed.path else p
        if not q.is_relative_to(ROOT):
            error(p, f'Link escapes repository: {ref}')
            return None
        if not q.is_file():
            error(p, f'Missing link target: {ref}')
            return None
        if parsed.fragment and (q not in files or unquote(parsed.fragment) not in anchors(files[q])):
            error(p, f'Missing anchor: {ref}')
        return q

    link_count = 0
    for p, text in files.items():
        if re.search(r'</?[A-Za-z][^>]*>', without_fenced_code(text)):
            error(p, 'Raw HTML is not allowed in Markdown; use ordinary headings and links')
        for anchor, count in anchor_counts(text).items():
            if count > 1:
                error(p, f'Duplicate anchor: {anchor}')
        for ref in LINK.findall(text):
            if not urlsplit(ref).scheme:
                link_count += 1
            target(p, ref)

    def require_id(p, meta, key, expected):
        q = by_id.get(meta.get(key))
        if q is None or records[q].get('type') != expected:
            error(p, f'{key} must reference an existing {expected} ID')

    counts = Counter()
    short_counts, with_context_counts = [], []
    sense_count = 0
    for p, meta in records.items():
        kind = meta.get('type')
        counts[kind] += 1
        if kind == 'proposal':
            require_id(p, meta, 'contributor', 'person')
            require_id(p, meta, 'source', 'source')
            if meta.get('attribution') != 'editorial-reconstruction':
                error(p, 'Proposal attribution must be explicit')
            short = section(files[p], 'Short version')
            context = section(files[p], 'Context and limits')
            if not short or not context:
                error(p, 'Missing Short version or Context and limits')
            short_counts.append(words(short))
            with_context_counts.append(words(short) + words(context))
            if not meta.get('relations'):
                error(p, 'Proposal has no concept mappings')
        elif kind == 'concept':
            senses = meta.get('senses')
            if (not isinstance(senses, dict) or not senses
                    or any(not isinstance(s, str) or not s or not isinstance(a, str) or not a for s, a in senses.items())):
                error(p, 'Senses must map stable IDs to Markdown heading fragments')
                continue
            if len(senses.values()) != len(set(senses.values())):
                error(p, 'Different senses must link to distinct headings')
            sense_count += len(senses)
            declared_sections = heading_sections(files[p])
            if set(declared_sections) != set(senses.values()):
                error(p, 'Sense mappings and Markdown headings differ')
            for sense, anchor in senses.items():
                heading, content = declared_sections.get(anchor, ('', ''))
                if not heading or heading.startswith('sense-'):
                    error(p, f'Missing readable sense heading for {anchor}')
                refs = LINK.findall(content)
                if not any(records.get(target(p, ref), {}).get('type') == 'proposal' for ref in refs):
                    error(p, f'Sense {sense} has no proposal link')
        elif kind == 'source':
            require_id(p, meta, 'contributor', 'person')
            if urlsplit(meta.get('url', '')).scheme != 'https':
                error(p, 'Source needs an HTTPS URL')
        for relation in meta.get('relations', []):
            if not isinstance(relation, dict) or not all(k in relation for k in ('type', 'target', 'status')):
                error(p, 'Invalid relation')
                continue
            if relation['type'] not in RELATIONS:
                error(p, 'Unknown relation type')
            q = target(p, relation['target'])
            if relation['target'] not in LINK.findall(files[p]):
                error(p, 'Machine-readable relation lacks visible link')
            if relation['type'] == 'uses-sense' and q is not None:
                fragment = unquote(urlsplit(relation['target']).fragment)
                senses = records.get(q, {}).get('senses', {})
                if (records.get(q, {}).get('type') != 'concept' or not isinstance(senses, dict)
                        or fragment not in senses.values()):
                    error(p, 'Sense mapping has no declared target')
                refs = LINK.findall(heading_sections(files[q]).get(fragment, ('', ''))[1])
                if not any(target(q, ref) == p for ref in refs):
                    error(p, 'Concept sense lacks a backlink to proposal')

    if errors:
        print('\n'.join(errors))
        return 1

    def stats(values):
        return {'min': min(values), 'median': statistics.median(values), 'max': max(values)}
    summary = {'records': dict(sorted(counts.items())), 'senses': sense_count, 'local_links': link_count,
               'short_version_words': stats(short_counts), 'with_context_words': stats(with_context_counts)}
    if report:
        out = '# Structural check\n\nStatus: passed. Generated by `python3 tools/check_network.py --report`.\n\n'
        out += 'Checks cover metadata, IDs, local links and anchors, senses and proposal backlinks, and relation targets. External URLs are not checked by this script.\n\n'
        out += '| Record type | Count |\n| --- | ---: |\n'
        for kind, count in sorted(counts.items()):
            out += f'| {kind} | {count} |\n'
        out += f'\nDeclared senses: {sense_count}.\n\n'
        out += '| Text counted | Minimum words | Median words | Maximum words |\n| --- | ---: | ---: | ---: |\n'
        for title, values in [('Short version', short_counts), ('Short version with context and limits', with_context_counts)]:
            out += f'| {title} | {min(values)} | {statistics.median(values):g} | {max(values)} |\n'
        out += '\nCounts cover only the named sections, excluding metadata, source excerpts, reasoning, concept pages, and other linked context. They do not measure reader effort or show that meaning has been preserved.\n\n'
        out += 'Structural checks do not assess philosophical accuracy.\n'
        (ROOT / 'STRUCTURAL-CHECK.md').write_text(out, encoding='utf-8')
    print(json.dumps(summary, indent=2))
    return 0


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--report', action='store_true')
    sys.exit(run(parser.parse_args().report))
