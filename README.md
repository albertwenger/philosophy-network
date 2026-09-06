# Philosophy network: feasibility study

This project investigates how far philosophical ideas can be reduced to clear,
compact expressions while preserving the distinctions needed to understand,
compare, and criticize them.

The source of truth is a set of Markdown files. The first deliverable is a
feasibility study and a navigable pilot corpus. The project name is provisional.

## Agreed starting points

- Use ordinary, contemporary language where it preserves meaning.
- Give concepts multiple distinguishable senses, with links to the proposals
  that articulate or use those senses.
- Make philosophers, sources, proposals, concepts, and study cases navigable
  in both directions.
- Preserve the difference between a source, an interpretation, an added
  assumption, and a new generalization.
- Evaluate reductions by their usefulness and fidelity, including examples,
  objections, and the closest competing interpretation.
- Track revisions in Git.

## Start here

- [Preliminary findings](study/FINDINGS.md): evidence and remaining questions.
- [Network index](INDEX.md): browse concepts, contributors, and proposals.
- [Corpus](study/CORPUS.md): 30 passages and their proposed reduction tests.
- [Study protocol](study/PROTOCOL.md): evaluate fidelity and usefulness.
- [Next work](study/NEXT.md): independent review and reader testing.

## Three useful entry points

- [Virtue](concepts/virtue.md): three related senses and their proposals.
- [Self](concepts/self.md): four senses with distinct commitments and contexts.
- [Freedom](concepts/freedom.md): noninterference and Stoic agency.

Each sense links to proposals that articulate or use it. Each proposal links
back to its senses, contributor, source edition, and study case. Grouping
senses is a proposal for comparison, not a declaration of equivalence.

## Project status

The first editorial pass contains 30 cases, 30 candidate proposals, 25 concept
pages with 49 senses, 13 contributor pages, and 19 source records. All proposals
remain drafts. No reader study has been conducted.

[Decision record](DECISIONS.md) · [Record conventions](SCHEMA.md)

## Working locally

Read the files directly in a Markdown editor or on GitHub. No server or package
installation is required. Python 3 is used only for the structural checker:

```bash
python3 tools/check_network.py
```

To update the report of links, metadata, and counts:

```bash
python3 tools/check_network.py --report
```

The checker establishes structural consistency. It does not validate the
philosophy. See [its report](study/STRUCTURAL-CHECK.md).

## Version control

Initialized 2026-09-06, on branch main. No remote is configured. Existing history
can be pushed to a GitHub repository when the user connects an account and
chooses or authorizes that destination.

The downloadable project snapshot includes the working tree and local Git
history. After extracting it, enter the philosophy-network directory and use
Git normally. Git tracks conceptual revisions as well as file changes.
