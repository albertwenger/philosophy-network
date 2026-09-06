# Markdown conventions, version 0.1

The Markdown files are canonical. This is a small provisional convention for
the study, with ordinary relative links usable in GitHub or any Markdown
reader. It is not a complete philosophical ontology.

## Records

| Type | Folder | Role |
| --- | --- | --- |
| concept | concepts | A navigational family of explicitly separate senses |
| proposal | proposals | A compact candidate formulation with qualifications and attribution |
| person | people | A philosopher, textual speaker, or attributed contributor |
| source | sources | A specified edition and inspected passage locators |
| argument | arguments | Grouped premises, a conclusion, and an inference under examination |
| question | questions | An open issue or objection with an explicit target |
| case | study/cases | A reduction hypothesis, proposed probes, and observation status |

An identifier is stable across wording revisions. Filenames can change if
links are updated; identifiers should not be reassigned to unrelated content.
Substantive competing interpretations should receive separate proposal IDs.

## Front matter

Records start with YAML front matter. For ease of parsing without dependencies,
each top-level value in this version is written as a JSON value on one line.
This is a restricted subset of YAML; multiline YAML values are not supported
by the included checker.

Required fields are id, type, and status. Type-specific fields are checked by
the validation script. Core and Qualification are Markdown sections, each
containing the actual text once. Counts are computed from these sections.

## Senses

Each concept declares its local sense IDs in the senses array. A heading such
as `## sense-aristotle` creates an ordinary Markdown anchor. Proposals point to
the relevant anchor, and the sense lists its associated proposals.

These are provisional sense distinctions and editorial glosses, not assertions
that each philosopher supplied an explicit dictionary definition. A proposal
may articulate, use, or challenge a sense. Placement in one concept family is
not an assertion of equivalence or historical influence.

## Relationships

Relations contain type, target, and status. Targets are relative paths,
optionally with a fragment. Every machine-readable relation has a visible
Markdown link as well.

Currently used types:

- uses-sense: a proposal is mapped to a particular concept sense.
- questions-standard: a question asks what supplies a proposal’s criterion.
- challenges-inference: an objection concerns an inference, without asserting
  that the conclusion is false.

For an argument, the premises array groups its inputs, conclusion identifies
its target, and joint_support makes the conjunctive interpretation explicit.
The present argument uses internal premise anchors and an external proposal
as its conclusion target. Argument mapping records a proposed reconstruction;
the checker does not establish logical validity or soundness.

Later types might include defines, presupposes, distinguishes, generalizes,
contradicts-under-scope, and analogous-in-respect. Each should be added only
with a precise use and an example. Loose similarity must never become an
entailment through an undocumented default.

## Attribution and status

All pilot proposals have attribution editorial-reconstruction and status
draft. That does not claim the historical contributor used the modern wording,
originated the concept, or endorses a position expressed by another speaker.

Source files are marked passages-inspected. This describes the source-checking
action, not scholarly verification of the translation or work as a whole.

Cases have status editorial-only and human_responses 0. Editorial hypotheses
must not be relabeled as measured accuracy. Verified human observations belong
in separate records with a frozen study version and a documented procedure.

## Checks

Run `python3 tools/check_network.py` from the repository root. To also write
the structural report, run `python3 tools/check_network.py --report`.

The checker verifies identifiers, metadata references, relative file links,
anchors, sense mappings and backlinks, required sections, and argument targets.
It reports corpus counts and word counts. It does not assess philosophical
truth, author fidelity, live external links, or reader understanding.
