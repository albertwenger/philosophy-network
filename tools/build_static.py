#!/usr/bin/env python3
"""Export the viewer for static hosting. Run: python3 tools/build_static.py.

Preview: python3 -m http.server 8001 --bind 127.0.0.1 --directory dist
Then open http://localhost:8001/. Rebuild after changing Markdown or assets.
"""
import argparse
import json
from pathlib import Path
import shutil

from preview import ASSETS, ROOT, snapshot


def build(output):
    data = snapshot()
    output.mkdir(parents=True, exist_ok=True)
    html = (ASSETS / 'index.html').read_text(encoding='utf-8')
    html = html.replace('data-network="./api/network" data-live="true"',
                        'data-network="./network.json" data-live="false"')
    (output / 'index.html').write_text(html, encoding='utf-8')
    for name in ('app.js', 'style.css'):
        shutil.copyfile(ASSETS / name, output / name)
    (output / 'network.json').write_text(
        json.dumps(data, ensure_ascii=False, separators=(',', ':')) + '\n',
        encoding='utf-8')
    (output / '.nojekyll').touch()
    return data


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--output', type=Path, default=ROOT / 'dist',
                        help='Output directory (default: dist in the repository)')
    args = parser.parse_args()
    data = build(args.output)
    print(f"Exported {len(data['docs'])} pages to {args.output.resolve()}")


if __name__ == '__main__':
    main()
