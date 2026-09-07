# Record conventions, version 0.3

The Markdown files are the authoritative version. Records use relative links
and stable identifiers. Links to headings must be updated when those headings
change.
These conventions describe the pilot's structure, not a complete classification
of philosophy.

Link philosopher names to their contributor pages with ordinary Markdown,
including names in headings. Keep existing links to works and sources, and
do not link a contributor's name to the page the reader is already on.

## Records and language

| Type | Folder | Role |
| --- | --- | --- |
| concept | concepts | Related senses of a term, kept distinct for comparison |
| proposal | proposals | A draft interpretation with a short version, context and limits, and attribution |
| person | people | A philosopher, textual speaker, or attributed contributor |
| source | sources | A specified edition and references to inspected passages |
| argument | arguments | Premises, a conclusion, and an inference under examination |
| question | questions | An open question or objection with an explicit target |
| case | study/cases | A proposed reader question, draft answer guide, and expected context need |

Use **interpretation** for a reading of a source. A **reconstruction** is an
attempt to express the source's meaning or reasoning faithfully; it remains
an interpretation. An **adaptation** deliberately changes a source claim.
A **generalization** extends its scope. A substantive competing interpretation
or adaptation needs a separate proposal with its difference made explicit.

Use the same term for the same meaning across a proposal, its linked sense,
and its study case. Preserve different terms when they carry a philosophical
distinction. **Short version** names the brief text; **Context and limits**
names the explanation needed to read it. Neither section is a substitute for
the source.

An identifier is stable across wording revisions and must not be reassigned
to unrelated content. Filenames can change if links are updated.

## Front matter

Records start with YAML front matter. Each top-level value is written as a
JSON value on one line so the checker can read it without dependencies.
Multiline YAML values are not supported.

Every record requires `id`, `type`, and `status`. The checker also requires
fields specific to each type. Proposals contain the sections `Short version`
and `Context and limits`, with the text stored once. Word counts are computed
from these sections.

## Senses and headings

A sense describes what a term means in the selected passage. It may be a
meaning used, proposed, or challenged there; its presence does not imply that
the contributor accepts it. Give each sense a descriptive heading and use
ordinary language drawn from its linked proposal where possible.

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

Sense distinctions are draft interpretations. They do not assert that a
contributor supplied a dictionary definition. Grouping senses establishes
neither equivalence nor historical influence.

## Relationships

Each relation contains `type`, `target`, and `status`. Targets are relative
paths, optionally with a heading fragment. Every relation also has a visible Markdown
link. The preview displays readable labels while preserving the stored types.

| Stored type | Reader label | Meaning |
| --- | --- | --- |
| uses-sense | Uses sense | A proposal is linked to a particular sense; this can include examining or challenging that sense. |
| questions-standard | Questions standard | An open question asks how a proposal's standard is specified or applied. |
| challenges-inference | Questions inference | An open question concerns an inference without asserting that its conclusion is false. |

For an argument, `premises` groups the inputs, `conclusion` identifies the
claim under examination, and `joint_support` states that the premises work
together. The current argument links to premise headings and a proposal
as its conclusion. Links record the interpretation; they do not establish
logical validity or soundness. Add a relation type only with a precise use
and an example.

## Attribution and status

All current proposals have `attribution: "editorial-reconstruction"` and
`status: "draft"`. Their visible notice is: "Draft interpretation of the cited
passage; not a quotation." Neither attribution claims that the contributor
used the modern wording or endorsed another speaker's position. Future
adaptations need a distinct attribution value and corresponding checker support.

Source records use `status: "passages-inspected"`. This means the cited passages
were consulted, not that the translation or whole work received independent
scholarly review.

Cases use `status: "editorial-only"` and `human_responses: 0`. The field
`expected_context` records an expectation for the particular reader question:

| Stored value | Reader label |
| --- | --- |
| none | None for this question |
| context-and-limits | Context and limits |
| argument | Argument |
| historical | Historical context |
| form | Form or sequence |

These categories are distinct from the four **reading versions** in the
[reader study protocol](study/PROTOCOL.md#reading-versions). They do not record
a measured minimum. Reader results require separate records tied to the exact
study version and a documented procedure.

Cases use the headings `Expected context need`, `Reader question`,
`Draft answer guide`, `Further question`, and `Reader results`. A comparison
is labeled `Possible misreading`, `Adaptation for comparison`, or
`Competing interpretation` according to its role.

## Checks

Run `python3 tools/check_network.py` from the repository root. Add `--report`
to update the [structural report](study/STRUCTURAL-CHECK.md).

The checker verifies identifiers, references, local links and heading fragments,
sense mappings and links in both directions, required sections, and argument
targets. It reports record and word counts. It does not assess philosophical
truth, source fidelity, external link availability, or reader understanding.
