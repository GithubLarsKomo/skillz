---
type: skill
generated: true
name: "thought-capture-journal"
category: "productivity"
userFacing: true
evaluationPassed: true
evaluationMode: "compatibility"
caseCount: 3
recordedResultCount: 3
sourcePath: "skills/thought-capture-journal/SKILL.md"
tags:
  - skill
  - skill-category/productivity
---

# thought-capture-journal

Normalisiert fortlaufend aufgezeichnete, unstrukturierte Gedanken aus einer einzelnen datierten Markdown- oder Textdatei zu einem nachvollziehbaren Thought Journal. Verwenden, wenn Ideen per Smartphone, Diktat oder Quick-Note gesammelt und anschließend für Graphanalyse vorbereitet werden sollen; der Skill interpretiert noch keine Beziehungen zwischen Gedanken.

> Generated from canonical repository metadata. Do not edit this note manually.

## Category

[[categories/productivity|productivity]]

## Requires

- —

## Required by

- [[skills/thought-graph-extractor|thought-graph-extractor]]
- [[skills/thought-to-concept-flow|thought-to-concept-flow]]

## Outputs

- `thought-journal.json`
- `thought-journal.md`

## Output consumers

### `thought-journal.json`

- [[skills/thought-graph-extractor|thought-graph-extractor]]
- [[skills/thought-to-concept-flow|thought-to-concept-flow]]

### `thought-journal.md`

- [[skills/thought-graph-extractor|thought-graph-extractor]]
- [[skills/thought-to-concept-flow|thought-to-concept-flow]]

## Evaluation

- Mode: `compatibility`
- Passed: `True`
- Cases: `3`
- Recorded results: `3`

## Canonical source

`skills/thought-capture-journal/SKILL.md`
