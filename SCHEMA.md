# Record conventions, version 0.8

The Markdown files are the authoritative version. Records use relative links
and stable identifiers. Links to headings must be updated when those headings
change.
These conventions describe the network's structure, not a complete classification
of philosophy.

Link philosopher names to their contributor pages with ordinary Markdown,
including names in headings. Keep existing links to works and sources, and
do not link a contributor's name to the page the reader is already on.

## Records and language

| Type | Folder | Role |
| --- | --- | --- |
| concept | concepts | Senses of one concept, kept distinct for comparison |
| proposal | proposals | A draft interpretation with a short version, context and limits, and attribution |
| person | people | A philosopher, textual speaker, or attributed contributor |
| source | sources | One work in a specified edition, with references to inspected passages |

Reuse a Source when adding passages from the same work and edition. Keep chapter
and section references within that Source and its proposals, rather than creating
a Source for each chapter. Separately complete dialogues or discourses can have
their own Sources. A different translation or edition needs a distinct Source
when it is cited; a multi-volume edition of one work can share one Source.

Use **interpretation** for a reading of a source. A **reconstruction** is an
attempt to express the source's meaning or reasoning faithfully; it remains
an interpretation. An **adaptation** deliberately changes a source claim.
A **generalization** extends its scope. A substantive competing interpretation
or adaptation needs a separate proposal with its difference made explicit.

Use the same term for the same meaning across a proposal and its linked senses.
Preserve different terms when they carry a philosophical distinction.
**Short version** names the brief text; **Context and limits**
names the explanation needed to read it. Neither section is a substitute for
the source.

An identifier is stable across wording revisions and must not be reassigned
to unrelated content. Filenames can change if links are updated.
Some identifiers retain earlier titles: Opinion uses `concept.belief`, Humanity
uses `concept.person`, and the newer Belief page uses `concept.belief-assent`.

## Front matter

Records start with YAML front matter. Each top-level value is written as a
JSON value on one line so the checker can read it without dependencies.
Multiline YAML values are not supported.

Every record requires `id`, `type`, and `status`. Files in the four record folders
must have front matter with the type matching their folder. Project documentation
and templates outside these folders can omit front matter and appear as Meta in
the preview. Incomplete core records are flagged rather than classified as Meta.
The checker also requires fields specific to each type. Proposals contain the
sections `Short version` and `Context and limits`, with the text stored once. Word counts are computed
from these sections.

Proposals may include an optional `Reasoning` section for premises and the
inference connecting them to a conclusion. Make clear when premises work
together. This explanation belongs within the proposal and uses ordinary
Markdown headings.

## Senses and headings

Give each concept its own page and title. Use a single word when it names the
concept accurately; an established multiword name such as Moral rightness is
also valid. Separate distinct concepts instead of combining them in a title.
Keep multiple senses together when they belong to the same concept.

Open with a short orientation to the meanings or questions explored on the
page, grounded in its senses. The [reading guide](README.md#how-to-read-the-network)
explains draft status and the limits of grouping; do not repeat that notice
in each concept's introduction.

A sense describes what a term means in the selected passage. It may be a
meaning used, proposed, or challenged there; its presence does not imply that
the contributor accepts it. Give each sense a descriptive heading and use
ordinary language drawn from its linked proposal where possible.

Several proposals can share a sense when the meaning stays stable. Different
examples, practices, or consequences do not by themselves require separate
senses. Add a new sense when a distinction in meaning matters to reading the
passages, and define that distinction clearly.

End each sense heading and repeated sense label with only the philosopher's
name in parentheses, linked to the contributor page with Markdown. Put source
details in the linked proposals.

Each concept's `senses` field maps stable local sense IDs to the link fragments
generated from its descriptive headings. For example:

```yaml
senses: {"aristotle": "character-directed-toward-good-choice-aristotle"}
```

The body uses ordinary Markdown headings, without HTML. Proposals link to the
heading fragment, and each sense links back to the proposals that use it.
Heading fragments come from the visible heading text, including link labels
but excluding link destinations.
When a heading changes, keep its local sense ID and update the mapping, all
Markdown links, and all relation targets that refer to it. The checker verifies
the mapping and links in both directions.

## Relationships

Each relation contains `type`, `target`, and `status`. Targets are relative
paths, optionally with a heading fragment. Every relation also has a visible Markdown
link. The preview displays readable labels while preserving the stored types.

| Stored type | Reader label | Meaning |
| --- | --- | --- |
| uses-sense | Uses sense | A proposal is linked to a particular sense; this can include examining or challenging that sense. |

Links record the interpretation; they do not establish logical validity or
soundness. Add a relation type only with a precise use and an example.

## Citation and navigation consistency

A proposal's `Source and attribution` section must visibly link to its declared
source and contributor. Its `Concept senses` section must link to each declared
sense relationship, and every sense link in that section must have a matching
`uses-sense` relation. Each concept sense's proposal links must reciprocate those
relations to that exact sense. A broader thematic connection alone does not
establish that a proposal uses the sense.

A contributor's `Proposals` and `Sources` sections list the records that name
that contributor in their metadata. A Source visibly links to its declared
contributor, and its `Selected passages` section lists the proposals that cite
it. Keep broader associations outside these assignment lists. The checker
compares these sections with the metadata in both directions to catch missing
entries and mistaken assignments.

## Attribution and status

Open each contributor page with a biographical sketch of about two sentences:
birth and death years (where known), historical or geographical context, and
a central contribution. Mark approximate or disputed dates explicitly. Follow
the sketch with a link to the contributor's Wikipedia biography for further
reading, and retain any specific note about attribution of the linked texts.

All current proposals have `attribution: "editorial-reconstruction"` and
`status: "draft"`. Their visible notice is: "The short version and commentary
are draft interpretations, not quotations." This applies to the interpretation;
the separately labeled source excerpt quotes the cited edition. Attribution
does not claim that the contributor used the modern wording or endorsed another
speaker's position. Future
adaptations need a distinct attribution value and corresponding checker support.

Source records use `status: "passages-inspected"`. This means the cited passages
were consulted, not that the translation or whole work received independent
scholarly review.

## Source excerpts and editions

Where the cited edition is verified as public domain in the United States,
add a `Source excerpt` section after the commentary (including any `Reasoning`)
and before `Source and attribution`. Use Markdown blockquotes and identify the
translator, if any, and exact passage. Preserve wording, meaningful emphasis,
and enough context to retain qualifications, speakers, and scope. Mark internal
omissions with `[…]` and disclose any editorial additions in square brackets.
Do not silently modernize a quotation. Excerpts do not enter the word counts
for the short version and context.

On each Source page, provide a clearly labeled link to the complete work in the
cited edition, retaining useful links to individual books or chapters. If only
part of the work is freely available, state that limit and link to a complete
edition through a publisher or library where possible. A full-work link does not
mean the whole work has been inspected.

A `Text and reuse` section records the specific edition's public-domain basis,
supporting link, jurisdiction, and date checked. Availability online alone does
not establish public-domain status, and an ancient work's modern translation
has its own terms. Leave the proposal linked without an excerpt when the edition
is not public domain or its status is unverified, and explain this on the Source
page. If an edition changes, recheck the interpretation, terminology, and locators
against that edition. No new record type or required metadata field is needed.

## Checks

Run `python3 tools/check_network.py` from the repository root. Add `--report`
to update the [structural report](STRUCTURAL-CHECK.md).

Use `--min-proposals-per-concept 2` when checking the completed 64-concept
milestone. Coverage counts distinct proposals across all senses of a concept;
several mappings from one proposal count once. The default minimum remains one
so a new concept can be developed incrementally. The report also counts the
contributors behind those proposals. Counts do not establish independent
perspectives or justify a relationship that the cited passage does not support.

The checker verifies record-folder metadata, identifiers, references, local links
and heading fragments, sense mappings and links in both directions, visible
citations, contributor/source navigation lists, required sections, and relation
targets. It reports record and word counts. It does not assess philosophical
truth, source fidelity, external link availability, or reader understanding.
