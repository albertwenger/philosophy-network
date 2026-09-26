# Philosophy network

This project connects philosophical concepts and their different meanings to
contributors, cited passages, and short interpretations.

The current focus is expanding concepts and contributors while keeping each
interpretation traceable to its source. Entries use concise language and
retain the context needed to understand their claims.

## Start here

- [Network index](INDEX.md): browse concepts, contributors, and proposals.
- [Next work](NEXT.md): priorities for expanding and reviewing the network.

## How to read the network

A **proposal** is a draft interpretation of a cited passage. Each proposal has
a **short version** and **context and limits**. Read both parts: the short version
may need the context to preserve the meaning of the passage.

An optional **reasoning** section sets out the steps behind an interpretation.

A **source excerpt**, where available, quotes the cited edition so you can
compare the interpretation with the passage itself. Quotations preserve the
source's wording; `[…]` marks an omission. Each proposal links to a **Source**
page with the edition, passage references, and access to the full work.
Any limits on that access are identified there.

Excerpts currently use editions verified as public domain in the United States.
Source pages record the basis and any exceptions; older works can have modern
translations with different reuse terms. Public-domain status can vary by country.

A **sense** is a particular meaning of a term in a passage. Each concept page
introduces the meanings explored in its linked passages and groups its related
senses for comparison. These descriptions are draft interpretations; they do
not imply that the contributor supplied a definition or accepted every meaning
discussed. Grouping does not establish equivalence or historical influence.
Links work in both directions, so readers can follow a proposal to a sense
and back.

Three starting points:

- [Virtue](concepts/virtue.md): character and moral standards.
- [Self](concepts/self.md): thinking, identification, and social experience.
- [Freedom](concepts/freedom.md): limits on coercion and what is up to us.

## Editorial principles

- Use ordinary, contemporary language where it preserves meaning.
- Repeat a term when its meaning stays the same; change it when the distinction matters.
- Keep interpretations of a source distinct from adaptations that change its claims.
- Preserve competing interpretations when the difference changes an important answer.
- Preserve accuracy and useful context when shortening a passage.
- Track revisions in Git. The Markdown files are the authoritative version.

## Project status

The network contains 30 proposals, 27 concept pages, 13 contributor pages,
and 19 source records. All interpretations remain drafts and have not received
independent source review. Reader testing is deferred while the network grows.

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
philosophy. See [its report](STRUCTURAL-CHECK.md).

To check the preview's rendering, corpus links, and file-change detection:

```bash
python3 -m unittest discover -s tools -p 'test_preview.py'
```

## Version control

The project is versioned in Git and available in the
[GitHub repository](https://github.com/albertwenger/philosophy-network).
