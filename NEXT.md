# Next work

## The 64-concept expansion

The milestone is complete: 64 concepts, 116 proposals, 29 contributors, and
41 sources. Every concept has at least two distinct proposals, and 52 have
three or more. The baseline contained 27 concepts, 30 proposals, 13 contributors,
and 18 sources. See the [expansion review](EXPANSION-REVIEW.md) for findings and
remaining gaps.

A proposal can serve more than one concept when the cited passage actually uses
the relevant senses. Multiple sense links from one proposal count only once for
concept coverage.

The four core record types remain concept, contributor, proposal, and source.
The groupings below organize this expansion; they are not new page types or
an exhaustive classification of philosophy.

## Completed waves

| Wave | New concepts | Total concepts | Editorial emphasis |
| --- | --- | ---: | --- |
| 1 | Habit, Human nature, Experience, Care, Compassion, Justice, Democracy, Power, Rights, Responsibility, Community, Personhood, Dignity | 40 | Cultivation, relationships, and social life; deepen existing ethical concepts |
| 2 | Reality, Being, Substance, Change, Time, Perception, Consciousness, Embodiment, Reason, Truth, Belief, Doubt | 52 | Knowledge, mind, and reality; broaden philosophical and textual traditions |
| 3 | Beauty, Art, Interpretation, Emotion, Desire, Happiness, Nature, Technology, Labor, Alienation, Progress, Sustainability | 64 | Art, work, and the environment; connect historical and contemporary perspectives |

Each wave also deepened its related existing concepts. All 37 planned new
concepts were retained; meanings and passage selections were refined during
review.

## Progress

| Checkpoint | Concepts | Proposals | Contributors | Sources |
| --- | ---: | ---: | ---: | ---: |
| Baseline | 27 | 30 | 13 | 18 |
| Wave 1 | 40 | 57 | 17 | 22 |
| Wave 2 | 52 | 88 | 22 | 31 |
| Wave 3 | 64 | 116 | 29 | 41 |

Wave 1 adds [Mencius](people/mencius.md), [Dewey](people/dewey.md),
[Gyekye](people/gyekye.md), and [Tronto](people/tronto.md). All 23 concepts developed in
that wave have at least two distinct proposals, and 19 have at least three.
New connections to Habit, Experience, and Human nature also reuse existing
[Aristotle](people/aristotle.md) and [Wollstonecraft](people/wollstonecraft.md) proposals. Baseline interpretations and excerpts
are unchanged. Source inspection and structural validation are complete;
the interpretations remain drafts.

Wave 2 adds [Avicenna](people/avicenna.md), [Maimonides](people/maimonides.md),
[Nāgārjuna](people/nagarjuna.md), [Dōgen](people/dogen.md), and
[Miranda Fricker](people/fricker.md). All concepts developed in this wave have
at least two distinct proposals. It also connects [Hume](people/hume.md)'s
account of custom to [Habit](concepts/habit.md). Source and concept reviews found
no blocking issues; the interpretations remain drafts.

Wave 3 adds [Spinoza](people/spinoza.md), [Schiller](people/schiller.md),
[Marx](people/marx.md), [William Morris](people/morris.md),
[Robin Wall Kimmerer](people/kimmerer.md), [Enrique Dussel](people/dussel.md),
and [Donna Haraway](people/haraway.md). It reaches the coverage target across all
64 concepts and connects ecological care with [Reciprocity](concepts/reciprocity.md).
The final review retained one shared Sustainability sense across three passages
and two substantive proposals each for Alienation and Progress.

## Next priorities

- Read and use the expanded network before choosing another numerical target.
  Record concrete difficulties finding, comparing, or following passages.
- Add another contributor to selected concepts that currently draw on only one,
  especially Compassion, Recognition, Alienation, and Sustainability. The
  [review](EXPANSION-REVIEW.md#breadth-and-remaining-gaps) lists all ten.
- Deepen underrepresented traditions through multiple contributors and internal
  disagreements, rather than treating any single author as representative.
- Arrange independent review of selected interpretations, beginning with
  translation-sensitive and cross-tradition comparisons. Use the existing
  [source review template](templates/REVIEW.md).
- Keep the four record types. Revisit the structure when actual reading or
  authoring reveals a problem that ordinary links and clearer senses cannot solve.

## Selection and review

- Build contributor, source, proposal, and sense records together around
  inspected passages. Give new contributors multiple proposals where practical.
- Deliberately broaden periods and geographies, including contemporary work,
  women, African, Asian, Latin American, and Indigenous perspectives. Individual
  contributors cannot stand for entire traditions; record remaining gaps.
- Reuse a sense only when the meaning remains stable. Keep distinctions visible
  and avoid forcing different terms into the same English concept.
- Select sources for their philosophical relevance and the reliability of the
  cited edition. Excerpt verified public-domain editions; use precise references
  and access links for modern or uncertain editions without reproducing them.
- Review exact passage locators, attribution, scope, translation limits, and
  reciprocal links. Source inspection and editorial review do not constitute
  independent scholarly review; proposals remain drafts.
- Validate and commit each complete wave. Review coverage, concept boundaries,
  source fidelity, navigation, and the practical limits of the structure at
  each substantial milestone before choosing the next expansion.

## Coverage verification

The [structural report](STRUCTURAL-CHECK.md) lists distinct proposals and
contributors for each concept. For the completed milestone, run:

```bash
python3 tools/check_network.py --min-proposals-per-concept 2 --report
python3 -m unittest discover -s tools -p 'test_*.py'
```

These checks establish structural consistency and coverage counts. They do
not establish that an interpretation is correct or that comparisons are
philosophically justified. Use the [source review template](templates/REVIEW.md)
when arranging independent review.

[Network index](INDEX.md) · [Project overview](README.md)
