---
type: skill
generated: true
name: "knowledge-view"
category: "internal"
userFacing: false
evaluationPassed: true
evaluationMode: "compatibility"
caseCount: 3
recordedResultCount: 3
sourcePath: "skills/knowledge-view/SKILL.md"
tags:
  - skill
  - skill-category/internal
---

# knowledge-view

Erzeugt deterministische, schreibgeschützte Sichten auf strukturierte Wissensartefakte anhand expliziter Filter, Sortierungen, Gruppierungen und abgeleiteter Felder. Verwenden, wenn aktive Entscheidungen, offene Fragen, Memory-Einträge, Projektartefakte oder andere Knowledge Artifacts selektiv als Kontext oder Übersicht projiziert werden sollen; verändert weder Quellen noch löst der Skill Konflikte.

> Generated from canonical repository metadata. Do not edit this note manually.

## Category

[[categories/internal|internal]]

## Requires

- [[skills/structured-knowledge-artifact|structured-knowledge-artifact]]

## Required by

- [[skills/obsidian-adapter|obsidian-adapter]]

## Outputs

- `knowledge-view.json`

## Output consumers

### `knowledge-view.json`

- [[skills/obsidian-adapter|obsidian-adapter]]

## Evaluation

- Mode: `compatibility`
- Passed: `True`
- Cases: `3`
- Recorded results: `3`

## Canonical source

`skills/knowledge-view/SKILL.md`
