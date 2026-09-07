# Concept template

Copy an existing concept record and assign a new stable ID. For each sense:

- Give the sense a readable Markdown heading and map its stable local ID to
  the heading fragment in `senses`.
- End each sense heading and repeated sense label with only the philosopher's
  name in parentheses, linked to the contributor page with Markdown. Put source
  details in the linked proposals.
- Use the visible heading text to form the fragment; omit link destinations.
- Explain what the term means in the linked passage, including when that meaning is challenged there.
- Reuse the linked proposal's vocabulary where the meaning is the same.
- Link to the proposals that use, propose, or challenge this meaning.
- State any important uncertainty or distinction that the description leaves unresolved.

Introduce the page as draft interpretations of the term's use in the linked
passages. Grouping invites comparison; it establishes neither equivalence nor
historical influence. Each linked proposal must link back to the exact sense.
When a heading changes, preserve the local ID and update its mapping, Markdown
links, and relation targets. Do not add HTML anchors.

[Record conventions](../SCHEMA.md) · [Example concept](../concepts/virtue.md)
