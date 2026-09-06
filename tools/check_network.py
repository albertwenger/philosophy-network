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
PACKAGES = {'core', 'qualification', 'argument', 'historical', 'form'}
TYPES = {'proposal', 'concept', 'person', 'source', 'argument', 'question', 'case'}
RELATIONS = {'uses-sense', 'questions-standard', 'challenges-inference'}
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


def words(text):
    return len(re.findall(r"\b[^\W_]+(?:[’'-][^\W_]+)*\b", text))


def anchors(text):
    result, seen = set(), Counter()
    for heading in re.findall(r'^#{1,6}\s+(.+?)\s*$', text, re.M):
        base = re.sub(r'[^\w\- ]', '', heading.lower()).replace(' ', '-')
        result.add(base + (f'-{seen[base]}' if seen[base] else ''))
        seen[base] += 1
    return result


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
        for ref in LINK.findall(text):
            if not urlsplit(ref).scheme:
                link_count += 1
            target(p, ref)

    def require_id(p, meta, key, expected):
        q = by_id.get(meta.get(key))
        if q is None or records[q].get('type') != expected:
            error(p, f'{key} must reference an existing {expected} ID')

    counts, packages = Counter(), Counter()
    core_counts, qualified_counts = [], []
    sense_count = 0
    for p, meta in records.items():
        kind = meta.get('type')
        counts[kind] += 1
        if kind == 'proposal':
            require_id(p, meta, 'contributor', 'person')
            require_id(p, meta, 'source', 'source')
            if meta.get('attribution') != 'editorial-reconstruction':
                error(p, 'Pilot attribution must be explicit')
            core, qual = section(files[p], 'Core'), section(files[p], 'Qualification')
            if not core or not qual:
                error(p, 'Missing Core or Qualification')
            core_counts.append(words(core))
            qualified_counts.append(words(core) + words(qual))
            if not meta.get('relations'):
                error(p, 'Proposal has no concept mappings')
        elif kind == 'case':
            require_id(p, meta, 'proposal', 'proposal')
            package = meta.get('hypothesized_package')
            if package not in PACKAGES:
                error(p, 'Unknown package hypothesis')
            packages[package] += 1
            if meta.get('human_responses') != 0 or meta.get('status') != 'editorial-only':
                error(p, 'Initial pilot must not claim human observations')
            for heading in ('Editorial hypothesis', 'Constructed rival', 'Reader probe', 'Provisional reviewer key', 'Observation record'):
                if not section(files[p], heading):
                    error(p, f'Missing {heading}')
        elif kind == 'concept':
            senses = meta.get('senses', [])
            if not senses or len(senses) != len(set(senses)):
                error(p, 'Missing or duplicate senses')
            sense_count += len(senses)
            for sense in senses:
                title = 'sense-' + sense
                if title not in anchors(files[p]):
                    error(p, f'Missing sense heading {title}')
                refs = LINK.findall(section(files[p], title))
                if not any(records.get(target(p, ref), {}).get('type') == 'proposal' for ref in refs):
                    error(p, f'Sense {sense} has no proposal link')
        elif kind == 'source':
            require_id(p, meta, 'contributor', 'person')
            if urlsplit(meta.get('url', '')).scheme != 'https':
                error(p, 'Source needs an HTTPS URL')
        elif kind == 'argument':
            require_id(p, meta, 'source', 'source')
            if meta.get('joint_support') is not True:
                error(p, 'Joint premise support must be explicit')
            if len(meta.get('premises', [])) < 2:
                error(p, 'Grouped argument needs at least two premises')
            for ref in meta.get('premises', []):
                target(p, ref)
            q = target(p, meta.get('conclusion', ''))
            if records.get(q, {}).get('type') != 'proposal':
                error(p, 'Conclusion needs a proposal target')
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
                sense = urlsplit(relation['target']).fragment.removeprefix('sense-')
                if records.get(q, {}).get('type') != 'concept' or sense not in records.get(q, {}).get('senses', []):
                    error(p, 'Sense mapping has no declared target')
                refs = LINK.findall(section(files[q], 'sense-' + sense))
                if not any(target(q, ref) == p for ref in refs):
                    error(p, 'Concept sense lacks a backlink to proposal')

    if counts['proposal'] != counts['case']:
        errors.append('Every pilot proposal needs a case')
    linked = [m.get('proposal') for m in records.values() if m.get('type') == 'case']
    if len(linked) != len(set(linked)):
        errors.append('Duplicate case assignment to a proposal')
    if errors:
        print('\n'.join(errors))
        return 1

    def stats(values):
        return {'min': min(values), 'median': statistics.median(values), 'max': max(values)}
    summary = {'records': dict(sorted(counts.items())), 'senses': sense_count, 'local_links': link_count,
               'packages': dict(sorted(packages.items())), 'core_words': stats(core_counts), 'qualified_words': stats(qualified_counts)}
    if report:
        out = '# Structural check\n\nStatus: passed. Generated by `python3 tools/check_network.py --report`.\n\n'
        out += 'Checks cover metadata, IDs, local links and anchors, senses and proposal backlinks, and argument targets. External URLs are not checked by this script.\n\n'
        out += '| Record type | Count |\n| --- | ---: |\n'
        for kind, count in sorted(counts.items()):
            out += f'| {kind} | {count} |\n'
        out += f'\nDeclared senses: {sense_count}.\n\n'
        out += '| Text package | Minimum words | Median words | Maximum words |\n| --- | ---: | ---: | ---: |\n'
        for title, values in [('Core', core_counts), ('Core plus qualification', qualified_counts)]:
            out += f'| {title} | {min(values)} | {statistics.median(values):g} | {max(values)} |\n'
        out += '\nCounts cover only the named sections, excluding metadata, sources, concepts, and argument context. They do not measure semantic compression or reader performance.\n\n'
        out += 'Structural success is not philosophical validation. No human observations are asserted by the pilot case records.\n'
        (ROOT / 'study/STRUCTURAL-CHECK.md').write_text(out, encoding='utf-8')
    print(json.dumps(summary, indent=2))
    return 0


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--report', action='store_true')
    sys.exit(run(parser.parse_args().report))
