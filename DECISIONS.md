# Decisions

## 2026-09-06: establish a Markdown feasibility project

The user authorized proceeding with the feasibility study and creating a local
directory with Git version tracking. GitHub access was offered as a possible
later step; no account connection, remote creation, or publication was requested.

The user specifically endorsed concept pages containing different senses and
links to their proposals. This is an organizing principle of the pilot.

The earlier proposed study size was 30–50 passages. The first editorial sample
uses the lower end, 30. This is a deliberately selected sample for preparing the study, not a statistical
sample of world philosophy.

Human reader testing is part of the study design. It has not been conducted.
Any analysis produced by the authoring assistant must be labeled editorial
and provisional, even if internal structural checks pass.

## 2026-09-06: initial editorial implementation

The initial sample contains 30 cases. The record convention uses stable IDs,
relative Markdown links, and concept-sense anchors. It currently distinguishes
49 senses on 25 concept pages. These boundaries are editorial choices awaiting
review, not additional user-approved philosophical commitments.

All source interpretations and draft answer guides were prepared by the same
assistant. No external reviewers were contacted. Expected context needs are
editorial expectations for the reader study. The record format, link integrity, and authored
word counts can be checked independently of their philosophical quality.

At this initial stage, the repository contained no browser preview. The pilot provides complete links to
sources and senses, with one grouped argument as a structural example. Fuller
argument, narrative, and historical materials were left for the next study phase.

## 2026-09-06: revise the language for a broader readership

The user authorized a thorough language revision. The revision uses the same
terms for the same editorial roles, separates interpretations from adaptations
and generalizations, and replaces technical sense headings with readable ones.
That revision retained stable sense IDs and used explicit HTML anchors to keep
existing links while headings changed. The browser preview and structural
checker were updated for those conventions.

The revision preserves words that limit philosophical claims and brings key
scope restrictions into short versions. Expected context needs concern the
primary reader question and are revised when that question no longer requires
additional context. They remain editorial expectations, not reader findings.

Selected passages were rechecked where revisions required source clarification,
including [Aristotle](people/aristotle.md)'s standard for the mean, [Kant](people/kant.md)'s restriction on maxims,
[Mill](people/mill.md)'s historical scope, [Hume](people/hume.md)'s use of knowledge, and Buddhist terminology.
These checks were performed by assistants, not independent source reviewers.
No reader study has been conducted. Publication remains future work.

## 2026-09-06: remove HTML from Markdown

The user reported visible HTML anchors in the concept pages. Sense sections
now use ordinary Markdown headings, with all internal links and relation targets
updated to their heading fragments. Stable local sense IDs remain in front
matter, mapped to those fragments. The previous anchor URLs are not preserved.
Future heading changes must update the mappings and incoming links together.

The concept template and record conventions describe this format. The checker
validates the sense mappings and links in both directions. The preview generates
heading anchors itself and displays all source HTML as text.
