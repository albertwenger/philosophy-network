# Decisions

## 2026-09-26: add source excerpts to proposals

Proposals now include a clearly labeled quotation where the cited edition is
verified as public domain in the United States. The first pass adds excerpts to
24 proposals, preserving qualifications and marking internal omissions. The
interpretation notice now refers specifically to the short version and commentary.
The guide explains the distinction once; no new record category is introduced.

Source pages identify the edition, its reuse basis, and access to the full work.
The three Buddhist proposals retain links to the complete discourses: the cited
modern translations are freely available under reuse terms, rather than presented
as public domain. The three Wittgenstein proposals also remain linked without
excerpts because U.S. public-domain status was not established. Their Source page
labels the online German text as Part I and links to a complete publisher edition.

The Epictetus source now uses Carter's historical 1759 edition, rather than the
modernized wording previously linked. Both interpretations were rechecked against
it. These editorial checks do not replace independent source review.

## 2026-09-26: focus on four core record types

The open-question category and its two pages have been removed, along with
their links, authoring instructions, and question-specific relation types.
The network now has four record types: concepts, contributors, proposals,
and sources. This keeps expansion focused on breadth and source-grounded
interpretations. Earlier question pages remain available in Git history.

## 2026-09-26: keep reasoning within proposals

The separate argument record was a prototype for showing premises and their
joint inference to a conclusion. Its content now lives in an optional
Reasoning section of the [Hume proposal](proposals/p007-hume-induction.md#reasoning),
with its scope limits retained and its open question linked to that section.

Argument is no longer a separate record type, directory, or navigation category.
Proposals can include reasoning when useful; their `form` may still describe
the cited passage as an argument. Separate argument records can be reconsidered
if comparison or reuse later makes them useful.

## 2026-09-26: prioritize expanding the network

The current focus is adding concepts, contributors, and cited interpretations.
The 30 study cases were authoring worksheets for a proposed comparison of
reader understanding and effort across short versions, added context, the
network, and source passages. No reader responses were collected.

The case worksheets and study setup have been removed from the working project,
along with their navigation, authoring requirements, and checker rules.
Earlier study materials remain available in Git history. Proposals, concept
senses, contributor biographies, sources, arguments, and open questions remain
the core of the network. Source review can proceed as it grows; reader testing
can be designed later when it becomes useful.

The entries below record earlier stages of the project.

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

The initial sample contained 30 cases. The record convention used stable IDs,
relative Markdown links, and concept-sense anchors. It distinguished
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

## 2026-09-06: give each concept its own page and title

Piety and moral rightness now have separate pages, as do reciprocity and
universalization. These pairings joined distinct concepts. The remaining
combined titles were simplified to Opinion, Humanity, Education, End, and
Middle, retaining related senses under one concept. The pilot now has 27
concept pages and the same 49 senses.

Concept titles use a single word when accurate. Established multiword names
such as Moral rightness are retained when they name one concept. The record
conventions and template now state this rule.
