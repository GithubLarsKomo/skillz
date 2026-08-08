---
type: skill
generated: true
name: "knowledge-map-generator"
category: "internal"
userFacing: false
evaluationPassed: true
evaluationMode: "compatibility"
caseCount: 3
recordedResultCount: 3
sourcePath: "skills/knowledge-map-generator/SKILL.md"
tags:
  - skill
  - skill-category/internal
---

# knowledge-map-generator

Projiziert vorhandene strukturierte Wissensartefakte und explizite Relationen in einen provider-neutralen Graphen aus Nodes, Edges und optionalen Groups. Verwenden, wenn Projekt-, Architektur-, Decision-, Domain- oder Memory-Zusammenhänge visualisiert oder an JSON Canvas, Mermaid, Graphviz, Neo4j oder andere Renderer übergeben werden sollen; der Skill erfindet keine fehlenden Beziehungen.

> Generated from canonical repository metadata. Do not edit this note manually.

## Category

[[categories/internal|internal]]

## Requires

- [[skills/structured-knowledge-artifact|structured-knowledge-artifact]]

## Required by

- [[skills/obsidian-adapter|obsidian-adapter]]

## Outputs

- `knowledge-map.json`

## Output consumers

### `knowledge-map.json`

- [[skills/obsidian-adapter|obsidian-adapter]]

## Evaluation

- Mode: `compatibility`
- Passed: `True`
- Cases: `3`
- Recorded results: `3`

## Canonical source

`skills/knowledge-map-generator/SKILL.md`
