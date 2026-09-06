# Feasibility study protocol

Status: proposed reader protocol, with an initial editorial pass completed.
No participants have been recruited and no human results have been collected.

## Research question

For a specified task, how much can a philosophical passage be reduced while
preserving the distinctions necessary to identify, apply, and criticize its
central contribution?

The study distinguishes textual brevity, clarity, historical fidelity,
argumentative adequacy, and navigability. None is a proxy for all the others.

## Scope of this first pass

The [corpus](CORPUS.md) contains 30 purposively selected passages, with 30
candidate proposals and case worksheets. These are calibration materials.
They were written and evaluated provisionally by the same assistant, so their
agreement is not independent validation.

The source passages were consulted using the editions recorded in the source
files. Before reader testing, an independent source reviewer should freeze
the exact excerpt boundaries, confirm the paraphrase, and revise the proposed
reviewer keys. The current locators are sufficient for finding each passage;
the experiment has not yet established standardized source extracts.

## What each level supplies

| Level | Material shown | Intended purpose |
| --- | --- | --- |
| Core | The sentence under Core in a proposal | Recognize and compare the isolated insight |
| Qualified | Core plus Qualification | Preserve decisive scope and distinctions |
| Network | Qualified entry plus linked senses, source, argument, questions, and context | Examine dependencies and applications |
| Source | A fixed excerpt from the specified edition with essential surrounding context | Comparison condition for the same task |

The network condition must record which links were followed and the total
material consulted. A short entry is not economical if readers must repeatedly
reconstruct a large hidden context.

The present pilot does not yet supply a complete network treatment for every
case. It supplies all concept links and source locators, one explicit grouped
argument, and two questions. Cases hypothesized to require additional argument,
form, or historical context still need that context prepared as standardized
reader material. A link to the original does not itself prove successful
compression.

## Editorial package hypotheses

Each case has one primary package hypothesis for the selected task. The
categories identify the dominant issue and are not a scale of philosophical
value or exhaustive descriptions of a work.

| Code | Hypothesis to test |
| --- | --- |
| core | The core may preserve the narrow distinction tested by the probe. |
| qualification | The short qualifier is expected to prevent an important error. |
| argument | Inspecting premises, inference, or dialogue commitments is expected to be necessary. |
| form | The sequence, exercise, or narrative is expected to do indispensable work. |
| historical | Social context or historical scope is expected to constitute part of the idea. |

The case records contain proposed probes and provisional reviewer keys. They
do not contain observations. A category must be revised if independent review
shows that a smaller or different package is adequate.

## Reader study

1. Have source specialists review the passage boundaries, candidate senses,
   paraphrases, and answer criteria. Preserve substantial competing readings.
2. Prepare the missing context packages and freeze a Git commit for the study.
3. Pilot instructions with a few readers to identify confusing questions.
   Revise before collecting the main comparison data.
4. Allocate different readers to different representations of each passage.
   Rotate conditions across passages; avoid showing one reader the fuller
   version before testing that reader on the short version of the same idea.
5. Record familiarity with each work. Include unfamiliar material in a later
   sample so that recognition of famous slogans cannot conceal missing content.
6. Ask the case-specific probe and an open question about an objection,
   assumption, or scope limit. Ask readers to identify what remains uncertain.
7. Have reviewers score de-identified responses without seeing the assigned
   condition. Allow more than one defensible interpretation. Record and discuss
   reviewer disagreements rather than treating a majority vote as philosophical
   truth.
8. Compare error patterns and effort by case and condition. Report sample size,
   missing responses, familiarity, uncertainty, and counterexamples to the
   editorial hypotheses.

Recruitment and collection of personal data are separate future actions. This
repository contains only templates and no participant information.

## Proposed scoring

Score each dimension independently: 0 = materially mistaken, 1 = partly
adequate, 2 = adequate for the agreed task. An unresolved reading can be marked
unscorable instead of forcing a number.

- Discrimination: distinguishes the proposal from a nearby rival.
- Application: handles the selected example or counterexample.
- Argument: identifies relevant grounds, assumptions, or an objection.
- Fidelity: preserves source scope and distinguishes reconstruction from text.
- Uncertainty: recognizes where the representation leaves a question open.

Separately record time spent, words consulted, links followed, and the reader’s
confidence. Do not combine these into a single quality score until there is a
reason for a specific weighting. Low time with confident misunderstanding is
not a success.

Before the main study, specify the allowable loss on each task, the smallest
useful gain in effort, and sample size using the pilot’s variability. No
acceptance threshold or statistically justified sample size has been claimed
in this editorial pass.

## Reduction and comparison rules

- A scope restriction that changes the answer to a probe must survive in the
  relevant package.
- A claimed equivalence must survive substitution in the stated context.
- An analogy permits comparison without licensing substitution or inference.
- Shared premises may jointly support a conclusion; separate support links
  must not turn conjunction into independent support.
- A new generalization or improvement receives its own proposal and links back
  to what inspired it.
- A concept can remain provisional, plural, partly example-based, or mutually
  dependent on other concepts.

## Outputs and stopping rule

For each case, identify the smallest tested package that preserves the agreed
distinctions within the agreed tolerances. Record what had to be restored and
why. Further shortening stops when it changes an important answer or makes a
necessary distinction inaccessible.

Report source-to-representation ratios only after source extracts and all
consulted dependencies have been measured. Corpus-wide sharing of definitions
should be reported separately from the burden on an individual reader.

The [initial findings](FINDINGS.md) concern the constructed corpus and editorial
risks. They make no claim that this stopping rule has been empirically reached.
