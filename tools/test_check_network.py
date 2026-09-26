"""Integrity checks against a small corpus, independent of the published entries."""
from contextlib import redirect_stdout
import io
import json
from pathlib import Path
import tempfile
import unittest
from unittest.mock import patch

import check_network


class NetworkChecks(unittest.TestCase):
    def setUp(self):
        directory = tempfile.TemporaryDirectory()
        self.addCleanup(directory.cleanup)
        self.root = Path(directory.name)
        root_patch = patch.object(check_network, 'ROOT', self.root)
        root_patch.start()
        self.addCleanup(root_patch.stop)
        self.write('people/author.md', {
            'id': 'person.author', 'type': 'person', 'status': 'navigation-entry',
        }, '# Author\n\n## Proposals\n\n- [Second](../proposals/second.md)\n\n'
           '## Sources\n\n- [Work](../sources/work.md)\n')
        self.write('people/speaker.md', {
            'id': 'person.speaker', 'type': 'person', 'status': 'navigation-entry',
        }, '# Speaker\n\n## Proposals\n\n- [First](../proposals/first.md)\n')
        self.write('sources/work.md', {
            'id': 'source.work', 'type': 'source', 'status': 'passages-inspected',
            'contributor': 'person.author', 'url': 'https://example.com/work',
        }, '# Work\n\nContributor: [Author](../people/author.md).\n\n'
           '## Selected passages\n\n- [First](../proposals/first.md)\n'
           '- [Second](../proposals/second.md)\n')
        self.write('concepts/example.md', {
            'id': 'concept.example', 'type': 'concept', 'status': 'provisional',
            'senses': {'first': 'first-meaning', 'second': 'second-meaning'},
        }, '# Example\n\n## First meaning\n\n[First](../proposals/first.md)\n\n'
           '## Second meaning\n\n[First](../proposals/first.md)\n\n[Second](../proposals/second.md)\n')
        for name, contributor, meanings in (
                ('first', 'speaker', ['first-meaning', 'second-meaning']),
                ('second', 'author', ['second-meaning'])):
            links = [f'../concepts/example.md#{meaning}' for meaning in meanings]
            self.write(f'proposals/{name}.md', {
                'id': f'proposal.{name}', 'type': 'proposal', 'status': 'draft',
                'attribution': 'editorial-reconstruction',
                'contributor': f'person.{contributor}', 'source': 'source.work',
                'relations': [{'type': 'uses-sense', 'target': link, 'status': 'editorial-mapping'} for link in links],
            }, f'# {name.title()}\n\n## Short version\n\nA short interpretation.\n\n'
               '## Context and limits\n\nThe relevant context.\n\n'
               f'## Source and attribution\n\n[Contributor](../people/{contributor}.md); [Work](../sources/work.md).\n\n'
               '## Concept senses\n\n' + '\n'.join(f'- [Meaning]({link})' for link in links) + '\n')

    def write(self, path, meta, body):
        file = self.root / path
        file.parent.mkdir(parents=True, exist_ok=True)
        front = '---\n' + '\n'.join(f'{key}: {json.dumps(value)}' for key, value in meta.items()) + '\n---\n\n'
        file.write_text(front + body, encoding='utf-8')

    def change_meta(self, path, **changes):
        text = (self.root / path).read_text(encoding='utf-8')
        meta = check_network.metadata(text)
        meta.update(changes)
        self.write(path, meta, text.split('\n---\n', 1)[1].lstrip('\n'))

    def replace(self, path, old, new):
        file = self.root / path
        text = file.read_text(encoding='utf-8')
        self.assertIn(old, text)
        file.write_text(text.replace(old, new), encoding='utf-8')

    def check(self, *errors):
        output = io.StringIO()
        with redirect_stdout(output):
            result = check_network.run()
        self.assertEqual(result, 1 if errors else 0, output.getvalue())
        for error in errors:
            self.assertIn(error, output.getvalue())

    def remove_first_relation(self):
        meta = check_network.metadata((self.root / 'proposals/first.md').read_text())
        self.change_meta('proposals/first.md', relations=meta['relations'][1:])

    def test_valid_corpus_allows_a_textual_speaker_distinct_from_source_author(self):
        self.check()

    def test_coverage_counts_distinct_proposals_across_senses(self):
        output = io.StringIO()
        with redirect_stdout(output):
            result = check_network.run(report=True, min_proposals_per_concept=2)
        self.assertEqual(result, 0, output.getvalue())
        summary = json.loads(output.getvalue())
        self.assertEqual(summary['proposals_per_concept'],
                         {'min': 2, 'median': 2, 'max': 2, 'at_least_two': 1, 'at_least_three': 0})
        self.assertIn('| Example | 2 | 2 |', (self.root / 'STRUCTURAL-CHECK.md').read_text())

    def test_multiple_sense_links_cannot_satisfy_a_higher_coverage_target(self):
        output = io.StringIO()
        with redirect_stdout(output):
            result = check_network.run(min_proposals_per_concept=3)
        self.assertEqual(result, 1)
        self.assertIn('Needs at least 3 distinct proposals; found 2', output.getvalue())

    def test_sense_backlink_requires_reciprocal_relation_to_that_exact_sense(self):
        self.remove_first_relation()
        self.check('Sense first proposal link lacks a reciprocal uses-sense relation')

    def test_visible_concept_link_requires_relation_even_without_its_backlink(self):
        self.remove_first_relation()
        self.replace('concepts/example.md', '## First meaning\n\n[First](../proposals/first.md)',
                     '## First meaning\n\nA description without a proposal.')
        self.check('Concept senses link lacks a uses-sense relation: concepts/example.md#first-meaning')

    def test_concept_sense_requires_visible_reciprocal_link(self):
        self.replace('proposals/first.md', '- [Meaning](../concepts/example.md#first-meaning)\n', '')
        self.check('Machine-readable relation lacks visible link',
                   'Sense first proposal lacks a visible link to this sense')

    def test_mapped_sense_must_be_listed_in_concept_senses_not_elsewhere(self):
        link = '[Meaning](../concepts/example.md#first-meaning)'
        self.replace('proposals/first.md', '- ' + link + '\n', '')
        with (self.root / 'proposals/first.md').open('a') as file:
            file.write('\n## Other links\n\n' + link + '\n')
        self.check('Concept senses section is missing mapped sense: concepts/example.md#first-meaning')

    def test_relation_requires_declared_sense_not_just_existing_heading(self):
        meta = check_network.metadata((self.root / 'proposals/first.md').read_text())
        relations = meta['relations']
        relations[0]['target'] = '../concepts/example.md#example'
        self.change_meta('proposals/first.md', relations=relations)
        self.replace('proposals/first.md', '[Meaning](../concepts/example.md#first-meaning)',
                     '[Meaning](../concepts/example.md#example)')
        self.check('Sense mapping has no declared target')

    def test_proposal_attribution_matches_declared_source_and_contributor(self):
        self.change_meta('proposals/first.md', contributor='person.author')
        self.replace('proposals/first.md', '[Work](../sources/work.md)', '[Other](../concepts/example.md)')
        # Incidental links elsewhere do not satisfy Source and attribution.
        with (self.root / 'proposals/first.md').open('a') as file:
            file.write('\n## Other links\n\n[Author](../people/author.md) [Work](../sources/work.md)\n')
        self.check('Source and attribution must link to declared contributor: people/author.md',
                   'Source and attribution must link to declared source: sources/work.md')

    def test_source_visibly_identifies_its_declared_contributor(self):
        self.replace('sources/work.md', '[Author](../people/author.md)', '[Speaker](../people/speaker.md)')
        self.check('Source must link to declared contributor: people/author.md')

    def test_contributor_lists_match_assignments_within_the_named_sections(self):
        self.replace('people/author.md', '## Proposals', '## Other links')
        self.replace('people/speaker.md', '[First](../proposals/first.md)', '[Second](../proposals/second.md)')
        self.replace('people/author.md', '## Sources', '## Further reading')
        self.check('people/author.md: Proposals list is missing assigned record: proposals/second.md',
                   'people/author.md: Sources list is missing assigned record: sources/work.md',
                   'people/speaker.md: Proposals list is missing assigned record: proposals/first.md',
                   'people/speaker.md: Proposals list contains unassigned record: proposals/second.md')

    def test_selected_passages_matches_source_assignments(self):
        self.replace('sources/work.md', '- [First](../proposals/first.md)', '- [Speaker](../people/speaker.md)')
        with (self.root / 'sources/work.md').open('a') as file:
            file.write('\n## Other links\n\n[First](../proposals/first.md)\n')
        self.check('Selected passages list is missing assigned record: proposals/first.md',
                   'Selected passages list contains unassigned record: people/speaker.md')

    def test_core_folder_requires_front_matter_and_its_matching_type(self):
        (self.root / 'concepts/new.md').write_text('# New concept\n')
        self.change_meta('sources/work.md', type='person')
        self.check('concepts/new.md: Missing front matter for concept record',
                   'sources/work.md: Folder requires type source')

    def test_meta_pages_do_not_require_record_metadata(self):
        (self.root / 'README.md').write_text('# Reading guide\n\n[Example](concepts/example.md)\n')
        (self.root / 'templates').mkdir()
        (self.root / 'templates/PROPOSAL.md').write_text('# Proposal template\n')
        self.assertEqual(check_network.expected_type('concepts/example.md'), 'concept')
        self.assertEqual(check_network.expected_type(self.root / 'sources/work.md', self.root), 'source')
        self.assertIsNone(check_network.expected_type('templates/PROPOSAL.md'))
        self.check()

    def test_malformed_metadata_produces_errors_instead_of_crashing(self):
        self.change_meta('proposals/first.md', id=['wrong'], contributor={}, relations={})
        self.change_meta('sources/work.md', url=None)
        self.check('Missing or invalid id', 'contributor must reference an existing person ID',
                   'Relations must be a list', 'Source needs an HTTPS URL')

    def test_malformed_relation_fields_produce_errors_instead_of_crashing(self):
        self.change_meta('proposals/first.md', relations=[{'type': 'uses-sense', 'target': [], 'status': None}])
        self.check('Invalid relation: type, target, and status must be nonempty strings')


if __name__ == '__main__':
    unittest.main()
