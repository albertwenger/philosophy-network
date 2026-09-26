# Next work

## The 64-concept expansion

The next milestone expands the baseline of 27 concepts, 30 proposals, 13
contributors, and 18 sources to 64 concepts. Every concept should connect to
at least two distinct proposals, preferably three. A proposal can serve more
than one concept when the cited passage actually uses the relevant senses.
Multiple sense links from one proposal count only once for concept coverage.

The four core record types remain concept, contributor, proposal, and source.
The groupings below organize this expansion; they are not new page types or
an exhaustive classification of philosophy.

## Planned waves

| Wave | New concepts | Total concepts | Editorial emphasis |
| --- | --- | ---: | --- |
| 1 | Habit, Human nature, Experience, Care, Compassion, Justice, Democracy, Power, Rights, Responsibility, Community, Personhood, Dignity | 40 | Cultivation, relationships, and social life; deepen existing ethical concepts |
| 2 | Reality, Being, Substance, Change, Time, Perception, Consciousness, Embodiment, Reason, Truth, Belief, Doubt | 52 | Knowledge, mind, and reality; broaden philosophical and textual traditions |
| 3 | Beauty, Art, Interpretation, Emotion, Desire, Happiness, Nature, Technology, Labor, Alienation, Progress, Sustainability | 64 | Art, work, and the environment; connect historical and contemporary perspectives |

Each wave also deepens its related existing concepts. Concept boundaries and
candidate passages can change when close reading warrants it; preserve the
64-concept milestone and explain any substitution.

## Progress

| Checkpoint | Concepts | Proposals | Contributors | Sources |
| --- | ---: | ---: | ---: | ---: |
| Baseline | 27 | 30 | 13 | 18 |
| Wave 1 | 40 | 57 | 17 | 22 |

Wave 1 adds Mencius, Dewey, Gyekye, and Tronto. All 23 concepts developed in
that wave have at least two distinct proposals, and 19 have at least three.
New connections to Habit, Experience, and Human nature also reuse existing
Aristotle and Wollstonecraft proposals. Baseline interpretations and excerpts
are unchanged. Source inspection and structural validation are complete;
the interpretations remain drafts.

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
- Validate and commit each complete wave. At 64 concepts, review coverage,
  concept boundaries, source fidelity, navigation, and the practical limits of
  the current structure before choosing the next expansion.

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
