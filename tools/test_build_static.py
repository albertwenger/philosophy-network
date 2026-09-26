"""Check the export is complete and can be hosted under a repository path."""
from html.parser import HTMLParser
import json
from pathlib import Path
import tempfile
import unittest
from urllib.parse import urljoin

from build_static import build


class AssetParser(HTMLParser):
    def __init__(self):
        super().__init__()
        self.urls = []
        self.settings = {}

    def handle_starttag(self, tag, attrs):
        attrs = dict(attrs)
        if tag == 'html':
            self.settings = attrs
            self.urls.append(attrs['data-network'])
        if tag in ('script', 'link'):
            self.urls.append(attrs.get('src') or attrs['href'])


class StaticBuildTests(unittest.TestCase):
    def test_export_is_self_contained_and_supports_subpaths(self):
        with tempfile.TemporaryDirectory() as directory:
            output = Path(directory) / 'philosophy-network'
            data = build(output)
            self.assertEqual(json.loads((output / 'network.json').read_text()), data)
            self.assertGreater(len(data['docs']), 200)
            parser = AssetParser()
            parser.feed((output / 'index.html').read_text())
            self.assertEqual(parser.settings['data-live'], 'false')
            for url in parser.urls:
                resolved = urljoin('/philosophy-network/', url)
                self.assertTrue(resolved.startswith('/philosophy-network/'))
                self.assertTrue((Path(directory) / resolved.lstrip('/')).is_file())
            self.assertTrue((output / '.nojekyll').is_file())
            self.assertFalse(list(output.glob('*.py')))


if __name__ == '__main__':
    unittest.main()
