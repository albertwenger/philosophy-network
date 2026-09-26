# Review of the 64-concept expansion

Date: 2026-09-26. This is an editorial review by the authoring assistants,
including separate read-only passes over selected passages and concept mappings.
It is not independent scholarly review or a reader study. All proposals remain
drafts.

## Milestone

| Checkpoint | Concepts | Proposals | Contributors | Sources |
| --- | ---: | ---: | ---: | ---: |
| Baseline | 27 | 30 | 13 | 18 |
| Wave 1 | 40 | 57 | 17 | 22 |
| Wave 2 | 52 | 88 | 22 | 31 |
| Wave 3 | 64 | 116 | 29 | 41 |

All 64 concepts have at least two distinct proposals; 52 have three or more.
There are 180 senses. Several links from one proposal count once toward a
concept's coverage. The [structural report](STRUCTURAL-CHECK.md) records the
per-concept counts.

The expansion adds 37 concepts, 86 proposals, 16 contributors, and 23 sources.
The original 30 proposals retain their short versions, context, reasoning, and
source excerpts. Three gain mappings to new concepts where the existing passage
supports the connection.

## What the structure supports

The four record types still suffice. Concepts organize meanings; proposals carry
the interpretations and their limits; contributors supply context and navigation;
sources identify the work, edition, passages, and access. No additional category
was needed for this expansion.

A single meaning can have several supporting passages. The three proposals under
[Sustainability](concepts/sustainability.md) share one sense: restraint, care, and
resource cycling are related practices, not automatically three meanings of the
term. New passages should prompt a new sense only when the meaning changes.

Related concepts remain useful when their questions are distinct. [Being](concepts/being.md)
concerns existence, [Reality](concepts/reality.md) distinguishes appearance and
dependence, and [Substance](concepts/substance.md) examines the relation between a
thing and its qualities. The [Opinion](concepts/opinion.md) and [Belief](concepts/belief.md)
pages explicitly acknowledge overlap. These are working boundaries grounded in
the selected passages, not a universal classification.

A proposal can connect to several concepts without requiring a duplicate
interpretation. New bridges connect [Hume](people/hume.md)’s account of custom to
[Habit](concepts/habit.md) and [Kimmerer](people/kimmerer.md)’s account of returning care to
[Reciprocity](concepts/reciprocity.md), each through a meaning grounded in its
passage. Conversely, a shared topic does not establish a uses-sense
relationship. The selected [Marx](people/marx.md) passages support two aspects of
[Alienation](concepts/alienation.md); a broader criticism of modernity was not
added merely to increase that count.

## Breadth and remaining gaps

The new material includes [Mencius](people/mencius.md) and [Dewey](people/dewey.md) on cultivation and education,
[Gyekye](people/gyekye.md) and [Tronto](people/tronto.md) on social life, [Avicenna](people/avicenna.md) and [Maimonides](people/maimonides.md) on understanding,
[Nāgārjuna](people/nagarjuna.md) and [Dōgen](people/dogen.md) on dependence and time, [Fricker](people/fricker.md) on epistemic injustice,
and [Kimmerer](people/kimmerer.md), [Dussel](people/dussel.md), and [Haraway](people/haraway.md) on ecological, historical, and technological
questions. Historical and contemporary writings now connect across more parts
of the network.

Coverage remains uneven. Several regions and traditions still appear through a
single contributor, and European and North American texts remain prominent.
Neither birthplaces nor a tally of contributors establishes representative
coverage of a tradition. Future selection should deepen African, Indigenous,
Latin American, Islamic, and South Asian perspectives, including disagreements
within those traditions. Women are more visible, but remain a minority of
contributors.

Ten concepts currently draw on only one contributor: Inference, Recognition,
Piety, Humanity, Philosophy, Universalization, Compassion, Opinion, Alienation,
and Sustainability. Their multiple proposals are substantive passages,
but they do not supply multiple contributors' perspectives. These are useful
candidates for broadening before adding another large set of concepts.

## Sources and interpretation

New contributors have concise biographies with dates and Wikipedia links. Source
records identify the edition and exact consulted passages. Public-domain excerpts
retain their wording and attribution. Modern translations and contemporary works
use concise interpretations and links when public-domain status is not established.

Access limits are explicit: the [Dōgen](people/dogen.md) PDF is Book 1 of a four-book edition,
[Fricker](people/fricker.md)'s author-hosted PDF is the Introduction, and [Kimmerer](people/kimmerer.md)'s Serviceberry source
is the essay rather than the later expanded book. Full-work access is linked
where available without claiming that the entire work was inspected.

Passage checks considered speakers, qualifications, translation choices, and
whether a sense is used or challenged. These checks found no unresolved blocking
issues in the reviewed material. Independent review should begin with the
cross-tradition comparisons and passages whose interpretation depends heavily
on translation.

## Navigation and validation

The coverage checker passes with a two-proposal minimum. All 28 automated tests
pass, covering structural rules, preview rendering, corpus links, and file-change
detection. All contributor pages have Wikipedia links. The original proposal
text and excerpt comparison reports no changes.

Browser checks confirmed the 64-concept filter, navigation through new proposals
and source records, exact sense links, and the Show Meta toggle. At a 390-pixel
mobile viewport the sidebar starts collapsed, search finds the new material,
selecting a result closes the sidebar, and reopening it retains the search and
filter. The tested pages remained readable without horizontal overflow.

Three local Python snapshot builds took 465–467 ms for 260 Markdown pages,
compared with 217–228 ms for the 97-page baseline. This is a small local check,
not a general performance benchmark; it found no immediate need to change the
preview architecture. Long concept and contributor lists remain a practical
area to observe during use.

## Next decisions

Use this milestone for sustained reading before setting the next numerical
target. Prioritize a second contributor for selected single-contributor concepts,
independent passage review, and feedback on finding and comparing interpretations.
Keep the current four-type model until a concrete reading or authoring difficulty
justifies a structural change.

[Next work](NEXT.md) · [Network index](INDEX.md) · [Record conventions](SCHEMA.md)
