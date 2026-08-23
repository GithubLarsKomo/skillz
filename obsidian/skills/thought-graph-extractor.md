---
type: skill
generated: true
name: "thought-graph-extractor"
category: "research-knowledge"
userFacing: true
evaluationPassed: true
evaluationMode: "compatibility"
caseCount: 3
recordedResultCount: 3
sourcePath: "skills/thought-graph-extractor/SKILL.md"
tags:
  - skill
  - skill-category/research-knowledge
---

# thought-graph-extractor

Analysiert ein normalisiertes Thought Journal, extrahiert Themen, Aussagen, Ziele, Fragen, Widersprüche und belastbar begründete Beziehungen und erzeugt daraus einen nachvollziehbaren semantischen Graphen mit Confidence und Provenance. Verwenden, wenn unstrukturierte Gedanken zu einem Obsidian-, Mermaid- oder Mindmap-fähigen Wissensgraphen verdichtet werden sollen; finale Zielkonzepte gehören nachgelagert in thought-to-concept-flow.

> Generated from canonical repository metadata. Do not edit this note manually.

## Category

[[categories/research-knowledge|research-knowledge]]

## Requires

- [[skills/structured-knowledge-artifact|structured-knowledge-artifact]]
- [[skills/thought-capture-journal|thought-capture-journal]]

## Required by

- [[skills/thought-to-concept-flow|thought-to-concept-flow]]

## Outputs

- `structured thought artifacts`
- `thought-graph-summary.md`
- `thought-graph.json`

## Output consumers

### `structured thought artifacts`

- [[skills/thought-to-concept-flow|thought-to-concept-flow]]

### `thought-graph-summary.md`

- [[skills/thought-to-concept-flow|thought-to-concept-flow]]

### `thought-graph.json`

- [[skills/thought-to-concept-flow|thought-to-concept-flow]]

## Evaluation

- Mode: `compatibility`
- Passed: `True`
- Cases: `3`
- Recorded results: `3`

## Canonical source

`skills/thought-graph-extractor/SKILL.md`
