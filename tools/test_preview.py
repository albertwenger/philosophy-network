"""Preview checks: corpus links, safe rendering, and live snapshot updates."""
import re
import tempfile
import unittest
from pathlib import Path
from unittest.mock import patch

import preview
from check_network import anchors, heading_sections, metadata, visible_text, words


class PreviewTests(unittest.TestCase):
    def test_corpus_links_and_sense_anchors(self):
        data = preview.snapshot()
        docs = {d['path']: d for d in data['docs']}
        self.assertGreater(len(docs), 120)
        for edge in data['edges']:
            self.assertIn(edge['target'], docs)
            if edge['fragment']:
                self.assertIn('id="' + edge['fragment'] + '"', docs[edge['target']]['html'])
        relations = [e for e in data['edges'] if e['source'] == 'proposals/p018-epictetus-control.md' and e['type'] == 'uses-sense']
        self.assertEqual(len(relations), 2)
        self.assertTrue(all(e['status'] == 'editorial-mapping' for e in relations))

    def test_safe_rendering_and_links(self):
        result = preview.render('# Heading\n\n<script>alert(1)</script>\n\n[unsafe](javascript:alert)\n\n[Freedom](../concepts/freedom.md#freedom-in-what-is-up-to-us-epictetus)\n\n```\n<a>\n```', 'proposals/example.md')
        self.assertNotIn('<script>', result)
        self.assertNotIn('href="javascript:', result)
        self.assertIn('#/concepts/freedom.md#freedom-in-what-is-up-to-us-epictetus', result)
        self.assertIn('<pre><code>&lt;a&gt;</code></pre>', result)
        self.assertIsNone(preview.resolve_link('INDEX.md', '../outside.md'))

    def test_snapshot_tracks_edits_additions_and_deletions(self):
        with tempfile.TemporaryDirectory() as directory, patch.object(preview, 'ROOT', Path(directory)):
            page = Path(directory) / 'one.md'
            page.write_text('# One\n\nOriginal')
            original = preview.snapshot()
            page.write_text('# One\n\nUpdated')
            updated = preview.snapshot()
            self.assertNotEqual(original['version'], updated['version'])
            self.assertIn('Updated', updated['docs'][0]['html'])
            second = Path(directory) / 'two.md'
            second.write_text('# Two')
            self.assertEqual(len(preview.snapshot()['docs']), 2)
            page.unlink()
            self.assertEqual(len(preview.snapshot()['docs']), 1)

    def test_tables_lists_and_duplicate_headings(self):
        result = preview.render('# Same\n\n# Same\n\n| A | B |\n| --- | --- |\n| X | Y |\n\n- item\n  continued\n', 'INDEX.md')
        self.assertIn('id="same-1"', result)
        self.assertIn('<th>A</th>', result)
        self.assertIn('<td>Y</td>', result)
        self.assertIn('<li>item continued</li>', result)

    def test_plain_heading_links_and_sections(self):
        body = '# Self\n\n## The thinking subject (Descartes)\n\nA subject.\n\n[Proposal](../proposals/example.md)\n\n## Changing identity\n\nAnother sense.\n'
        rendered = preview.render(body, 'concepts/self.md')
        self.assertIn('<h2 id="the-thinking-subject-descartes">The thinking subject (Descartes)</h2>', rendered)
        self.assertNotIn('<a id=', rendered)
        self.assertEqual(anchors(body), {'self', 'the-thinking-subject-descartes', 'changing-identity'})
        senses = heading_sections(body)
        self.assertEqual(senses['the-thinking-subject-descartes'][0], 'The thinking subject (Descartes)')
        self.assertIn('[Proposal]', senses['the-thinking-subject-descartes'][1])
        self.assertNotIn('Another sense.', senses['the-thinking-subject-descartes'][1])

    def test_linked_names_preserve_heading_targets_and_word_counts(self):
        plain = 'Character directed toward good choice (Aristotle)'
        linked = 'Character directed toward good choice ([Aristotle](../people/aristotle.md))'
        body = '# Virtue\n\n## ' + linked + '\n\nA description.\n'
        rendered = preview.render(body, 'concepts/virtue.md')
        anchor = 'character-directed-toward-good-choice-aristotle'
        self.assertIn('<h2 id="' + anchor + '">', rendered)
        self.assertIn('<a href="#/people/aristotle.md">Aristotle</a>', rendered)
        self.assertEqual(anchors(body), anchors('# Virtue\n\n## ' + plain + '\n'))
        self.assertEqual(visible_text(linked), plain)
        self.assertEqual(words(linked), words(plain))
        possessive = 'Knowledge ([Plato](../people/plato.md)’s Meno)'
        self.assertIn('knowledge-platos-meno', anchors('## ' + possessive + '\n'))

    def test_snapshot_labels_do_not_expose_markdown_link_destinations(self):
        with tempfile.TemporaryDirectory() as directory, patch.object(preview, 'ROOT', Path(directory)):
            page = Path(directory) / 'one.md'
            page.write_text('# [Aristotle](people/aristotle.md)\n\n## A sense ([Aristotle](people/aristotle.md))\n\nDescription.')
            doc = preview.snapshot()['docs'][0]
            self.assertEqual(doc['title'], 'Aristotle')
            self.assertEqual(doc['anchors']['a-sense-aristotle'], 'A sense (Aristotle)')
            self.assertNotIn('people/aristotle.md', doc['text'])

    def test_all_source_html_is_escaped_including_empty_anchors(self):
        body = '<a id="sense-one"></a><a id="sense-one"></a>\n\n<a id="sense-bad" onclick="alert(1)"></a>\n\n<a href="javascript:alert(1)">bad</a>\n\n```\n<a id="sense-example"></a>\n## Example heading\n```'
        rendered = preview.render(body, 'concepts/example.md')
        self.assertNotIn('<a id=', rendered)
        self.assertNotIn('<a href=', rendered)
        self.assertIn('&lt;a id=', rendered)
        self.assertEqual(anchors(body), set())

    def test_repeated_headings_keep_distinct_section_content(self):
        body = '# Shared name\n\n## Shared name\n\n[First](first.md)\n\n## Shared name\n\n[Second](second.md)\n\n### Details\n\nNested text.\n\n```\n## Example\n```\n'
        senses = heading_sections(body)
        self.assertEqual(set(senses), {'shared-name-1', 'shared-name-2'})
        self.assertIn('[First]', senses['shared-name-1'][1])
        self.assertNotIn('[Second]', senses['shared-name-1'][1])
        self.assertIn('[Second]', senses['shared-name-2'][1])
        self.assertNotIn('[First]', senses['shared-name-2'][1])
        self.assertIn('Nested text.', senses['shared-name-2'][1])
        rendered = preview.render(body, 'concepts/example.md')
        for anchor in anchors(body):
            self.assertEqual(rendered.count('id="' + anchor + '"'), 1)

    def test_markdown_corpus_has_no_html_and_uses_heading_fragments(self):
        for path in preview.ROOT.rglob('*.md'):
            if '.git' in path.parts:
                continue
            text = path.read_text(encoding='utf-8')
            with self.subTest(path=path):
                self.assertIsNone(re.search(r'</?[A-Za-z][^>]*>', text))
                self.assertNotIn('#sense-', text)
                meta = metadata(text)
                if meta and meta['type'] == 'concept':
                    self.assertIsInstance(meta['senses'], dict)
                    self.assertEqual(set(meta['senses'].values()), set(heading_sections(text)))


if __name__ == '__main__':
    unittest.main()
