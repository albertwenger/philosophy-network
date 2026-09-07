# Philosophy network: feasibility pilot

This project asks how briefly a philosophical passage can be expressed while
preserving the distinctions readers need to understand, apply, and question it.

The pilot contains 30 draft interpretations linked to sources and concept
senses. It shows how the proposed network can be populated and identifies
places where shortening may change meaning. Whether readers understand these
versions accurately, and with less effort, remains untested.

## Start here

- [Construction findings](study/FINDINGS.md): what was built and what remains untested.
- [Network index](INDEX.md): browse concepts, contributors, and proposals.
- [Study passages](study/CORPUS.md): the 30 passages and their study cases.
- [Reader study protocol](study/PROTOCOL.md): how understanding and effort would be compared.
- [Next work](study/NEXT.md): source review and reader testing.

## How to read the network

A **proposal** is a draft interpretation of a cited passage. Each proposal has
a **short version** and **context and limits**, followed by its source and links
to concept senses. Read both parts: the short version may need the context to
preserve the meaning of the passage.

A **sense** is a particular meaning of a term in a passage. Concept pages group
related senses for comparison. Grouping does not establish equivalence or
historical influence. Links work in both directions, so readers can follow a
proposal to a sense and back.

Three starting points:

- [Virtue](concepts/virtue.md): character and moral standards.
- [Self](concepts/self.md): thinking, identification, and social experience.
- [Freedom](concepts/freedom.md): limits on coercion and what is up to us.

## Editorial principles

- Use ordinary, contemporary language where it preserves meaning.
- Repeat a term when its meaning stays the same; change it when the distinction matters.
- Keep interpretations of a source distinct from adaptations that change its claims.
- Preserve competing interpretations when the difference changes an important answer.
- Evaluate accuracy and reader effort separately. Brevity alone is not success.
- Track revisions in Git. The Markdown files are the authoritative version.

## Project status

The pilot contains 30 study cases, 30 proposals, 25 concept pages, 13 contributor
pages, and 19 source records. All interpretations remain drafts. Source review
by independent reviewers and reader testing are still needed.

[Decision record](DECISIONS.md) · [Record conventions](SCHEMA.md)

## Working locally

Launch the local browser preview with Python 3.10 or later (no packages needed):

```bash
python3 tools/preview.py
```

This opens [the local viewer](http://localhost:8000). Search titles and passages,
filter by page type, and follow links or the graph of connected pages.
Each page lists links from and to it. Relations have readable labels and
statuses; ordinary links are labeled as navigation. Sense links jump
to their headings. Saved Markdown edits, additions, and deletions appear within
about two seconds, preserving the current page and search.

The viewer is read-only, works offline, and is available only on your computer.
The Markdown files remain the authoritative version. The preview supports
headings, paragraphs, links, emphasis, lists, tables, quotes, and fenced code.
It generates link targets from headings and displays any source HTML as text.
It is not a full CommonMark renderer.

Stop it with Ctrl+C. Use `--port 8001` if port 8000 is occupied, or
`--no-browser` to print the address without opening a browser. You can also
continue reading the files directly in a Markdown editor or on GitHub.

Run the structural checker:

```bash
python3 tools/check_network.py
```

To update the report of links, metadata, and counts:

```bash
python3 tools/check_network.py --report
```

The checker establishes structural consistency. It does not validate the
philosophy. See [its report](study/STRUCTURAL-CHECK.md).

To check the preview's rendering, corpus links, and file-change detection:

```bash
python3 -m unittest discover -s tools -p 'test_preview.py'
```

## Version control

The project uses local Git history. No remote repository is configured.
A publication destination remains to be arranged.
