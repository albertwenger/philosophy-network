# Reader study protocol

Status: proposed study. Draft materials exist; no reader responses have been collected.

## Research question

For a specified task, how briefly can a philosophical passage be expressed
while preserving the distinctions readers need to understand, apply, and
question it?

The study measures accuracy and reader effort separately. It also examines
whether interpretations preserve the source's meaning and whether readers
can find the context they need.

## Current materials

The [study passages](CORPUS.md) comprise 30 deliberately selected passages,
with one proposal and one study case for each. The assistant prepared both
the interpretations and the draft answer guides. Their agreement is not
independent evidence of accuracy.

The source records identify the editions and passages consulted. Before
reader testing, independent source reviewers should confirm the interpretations,
review the answer guides, and fix the exact boundaries of each source excerpt.
The present references locate passages; they do not yet define standardized
excerpts for comparison.

## Reading versions

These are the four versions proposed for comparison on the same reader task.
They describe what readers would see, not a ranking of philosophical value.

| Reading version | Material shown |
| --- | --- |
| Short version | The text under Short version in a proposal |
| With context and limits | The short version plus Context and limits |
| Network | The short version with context and limits, plus linked senses, source references, arguments, open questions, and other prepared context |
| Source passage | A fixed excerpt from the specified edition with essential surrounding context |

Give all readers the same neutral question sheet, including any comparison
statement the question refers to. Keep expected context needs, comparison
classifications, and draft answer guides out of the participant materials:
they can reveal the expected answer. The study cases are authoring worksheets,
not participant handouts. The network version must also exclude links to these
worksheets during testing.

Record all material readers consult, including the question sheet. For the
network version, also record which links they follow. An entry may be short
while requiring substantial additional reading.

The network currently supplies concept links and source references for every
proposal, one grouped argument, and two open questions. Many cases still need
fuller argument, historical, or narrative material prepared before comparison.
A link to the source alone does not show that the network saves reading effort.

## Expected context needs

Each case records the context expected to be needed for its primary reader question.
This expectation guides preparation of the reading versions; it is not a
finding about the smallest adequate version. The categories describe a main
need and can overlap.

| Expected context | Reason for the expectation |
| --- | --- |
| None for this question | The short version may preserve the particular distinction the question asks about. |
| Context and limits | The proposal's explanation may prevent an important misreading. |
| Argument | The reader may need the premises, inference, or commitments made in a dialogue. |
| Historical context | The social setting or the source's limits on scope may be part of the idea. |
| Form or sequence | An exercise, narrative, or sequence of examples may be needed to understand the contribution. |

A **possible misreading** states a mistake to distinguish from the proposal.
An **adaptation for comparison** deliberately changes a source claim and may
be defensible in its own right. A **competing interpretation** offers another
reading of the same passage. Keep these roles distinct when revising the
cases. A draft answer guide can be revised when source review identifies
another defensible answer.

## Reader study

1. Have source reviewers examine the excerpt boundaries, sense distinctions,
   interpretations, and draft answer guides. Preserve substantial competing
   interpretations.
2. Prepare the missing context and record the exact study materials in a Git
   commit. Use that version for the comparison.
3. Try the instructions with a few readers to identify confusing questions.
   Revise them before collecting the main results.
4. Assign different readers to different reading versions of each passage.
   Rotate versions across passages. Avoid showing a reader the fuller version
   before asking about the short version of the same passage.
5. Record familiarity with each work. Include unfamiliar material in a later
   sample so that recognition of famous sayings cannot conceal missing content.
6. Ask the case's reader question and further question about an assumption,
   limit, or choice of interpretation. Ask readers to identify what remains
   uncertain.
7. Have reviewers assess responses without seeing the reader's identity or
   assigned version. Allow more than one defensible interpretation. Record
   disagreements and the reasons for them; a majority vote does not establish
   philosophical truth.
8. Compare accuracy and effort by case and reading version. Report participant
   numbers, missing responses, familiarity, uncertainty, and results that
   challenge the editorial expectations.

Recruitment and collection of participant data remain future work. This
repository contains no participant information.

## Proposed scoring

Score each dimension separately: 0 = materially mistaken, 1 = partly adequate,
2 = adequate for the agreed task. Mark an unresolved interpretation unscorable
when assigning a number would conceal the disagreement.

- Understanding: distinguishes the proposal from a possible misreading, adaptation, or competing interpretation.
- Application: handles the selected example or counterexample.
- Critical assessment: identifies relevant reasons, assumptions, or an objection.
- Source fidelity: preserves the source's scope and distinguishes interpretation from quotation or adaptation.
- Uncertainty: recognizes where the reading version leaves a question open.

Also record time spent, words consulted, links followed, and reader confidence.
Report these alongside accuracy. Do not combine the measures into one score
without a reason for the weighting. Fast, confident misunderstanding is a
failure.

Before the main study, specify the acceptable loss on each task and the
smallest useful reduction in effort. Use variation in the preliminary reader
responses to plan the main study's participant numbers. The current editorial
assessment supplies neither acceptance thresholds nor a justified sample size.

## Interpretation and comparison rules

- A word that limits scope must remain wherever removing it changes an important answer.
- A claimed equivalence must allow substitution in the stated context without changing the claim.
- An analogy supports comparison without establishing equivalence or an inference.
- Premises that support a conclusion together must not be shown as each supporting it independently.
- An adaptation that changes a source claim needs its own proposal and a link to its source of inspiration. A generalization extends the scope of a claim and must state that extension.
- A sense may remain provisional, partly explained by examples, or dependent on other senses.

## Results and stopping rule

For each case, identify the shortest tested reading version that preserves
the agreed distinctions within the agreed tolerances. Record what context had
to be restored and why. Stop shortening when it changes an important answer
or makes a necessary distinction inaccessible.

Compare lengths only after measuring the source excerpts and all material
readers consult. Report any savings from sharing definitions across the
network separately from the effort required of an individual reader.

The [construction findings](FINDINGS.md) describe the draft materials and
editorial concerns. They do not establish that this stopping rule has been
reached.
