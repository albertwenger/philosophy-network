# Initial feasibility findings

Date: 2026-09-06. Status: provisional editorial analysis.

## Assessment

The proposed Markdown network is practical, and separating concept senses
produces a useful first representation. Constructing the corpus exposes
specific ways that a short, clear expression can change its philosophical
content.

This pass supports proceeding to independent source review and a reader
comparison. It does not establish that the reductions preserve understanding,
that the chosen senses are optimal, or that philosophy as a whole admits a
similar representation.

## Work completed

Thirty passages were selected across 13 contributors or textual attributions,
using 19 primary-source records. They cover nine overlapping forms of writing.
Each case contains a core, qualification, source locator, concept mappings,
constructed rival, proposed probe, provisional reviewer key, and a hypothesis
about the context needed.

The network contains 25 concept pages with 49 senses, one grouped argument,
and two questions with explicit targets. The same assistant authored the
formulations and their editorial assessments. No independent reviewers or
human participants have evaluated them.

## Length of the candidates

| Text package | Minimum words | Median words | Maximum words |
| --- | ---: | ---: | ---: |
| Core | 8 | 10 | 15 |
| Core plus qualification | 26 | 33.5 | 38 |

These are descriptive counts from the [checker](../tools/check_network.py),
not measured minima or evidence of semantic fidelity. The cores were
deliberately written to be short. The counts exclude sources, concept pages,
metadata, and argument context. They therefore do not measure the reader’s
total burden or source-to-summary compression.

## Editorial package hypotheses

| Package expected to be needed | Cases |
| --- | ---: |
| Core | 5 |
| Qualification | 11 |
| Argument context | 5 |
| Historical context | 5 |
| Form or sequence | 4 |

These are single-editor hypotheses about a purposive sample, not success
rates or estimates of the share of philosophy reducible to each level.
[Individual cases](CORPUS.md) expose the reasons for each assignment. The
categories identify a dominant issue and can overlap in substance.

## Lessons from the construction

1. **Sense separation is implementable.** The [self](../concepts/self.md) and
   [freedom](../concepts/freedom.md) pages demonstrate how comparison can coexist
   with explicit differences. The usefulness and correctness of the sense
   boundaries still require review.
2. **A few words can carry decisive content.** [Case 16](cases/c016-wittgenstein-meaning.md)
   retains scope in the core. [Case 11](cases/c011-kant-humanity.md) tests a
   small restriction with large consequences. Cutting words should follow
   analysis of which inferences they change.
3. **A link can defer an explanation.** [Case 1](cases/c001-aristotle-mean.md)
   and its [question](../questions/q001-appropriateness.md) expose a standard
   needing clarification. Making that dependency visible does not resolve it.
4. **Modernization can change strength or scope.** Cases
   [14](cases/c014-mill-harm.md), [19](cases/c019-epictetus-judgment.md), and
   [27](cases/c027-wollstonecraft-virtue.md) distinguish a historical claim
   from an improvement or weaker adaptation. Both can be retained as separate
   proposals. Git history alone cannot replace simultaneous competing records.
5. **Context can constitute an idea.** [Case 29](cases/c029-du-bois-double-consciousness.md)
   tests whether removing social context changes the explanatory target. A
   short core can include context, but independent review must determine how
   much more a reader needs.
6. **Some contributions are activities.** The comparative, methodological,
   and narrative cases offer useful entry points. A summary has not thereby
   taught the reader to carry out the activity. Compact procedures and ordered
   examples should be prepared and tested as additional forms of reduction.
7. **Relations need explicit targets.** The [induction argument](../arguments/a001-induction.md)
   groups premises. Its [question](../questions/q002-circularity.md) targets
   the reach of an inference. This demonstrates a representational distinction,
   not machine verification of the argument.

## Remaining uncertainty

Reader understanding, reviewer agreement, sense granularity, translation
sensitivity, and authoring/review cost have not been measured. Most complete
argument, historical, and narrative packages still need preparation. Linking
the original is not itself evidence of effective compression.

The sample favors accessible and familiar passages and has substantial
regional, historical, and genre gaps, described in the [corpus note](CORPUS.md).
Prior familiarity can conceal missing content. A subsequent sample should
include less recognizable material and rival translations.

## Recommended next experiment

Review the sense model and several contrasting cases with the user. Obtain
independent source review, freeze exact excerpt boundaries and comparison
materials in Git, and compare core, qualified, network, and source conditions.
Measure error patterns and effort separately using the [protocol](PROTOCOL.md).

The target is the shortest representation that preserves distinctions needed
for a defined task. This repository makes that target concrete enough to
investigate; it does not yet demonstrate that the target has been reached.

[Overview](../README.md) · [Index](../INDEX.md) · [Next work](NEXT.md)
