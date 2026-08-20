---
type: skill
generated: true
name: "precision-language-rewriter"
category: "workflow"
userFacing: true
evaluationPassed: true
evaluationMode: "compatibility"
caseCount: 3
recordedResultCount: 3
sourcePath: "skills/precision-language-rewriter/SKILL.md"
tags:
  - skill
  - skill-category/workflow
---

# precision-language-rewriter

Überarbeitet deutsche und englische Reports, Memos und Sachtexte in den Modi light, author oder editorial auf Präzision, idiomatische Sprache, Genrepassung und optional bestätigte Author Voice, ohne neue Sachinformation zu erzeugen oder fachliche Terminologie zugunsten künstlicher Variation zu verwässern.

> Generated from canonical repository metadata. Do not edit this note manually.

## Category

[[categories/workflow|workflow]]

## Requires

- —

## Required by

- [[skills/precision-writing-revision|precision-writing-revision]]

## Outputs

- `revised-text`
- `rewrite-change-map.json`

## Output consumers

### `revised-text`

- [[skills/precision-writing-revision|precision-writing-revision]]

### `rewrite-change-map.json`

- [[skills/precision-writing-revision|precision-writing-revision]]

## Evaluation

- Mode: `compatibility`
- Passed: `True`
- Cases: `3`
- Recorded results: `3`

## Canonical source

`skills/precision-language-rewriter/SKILL.md`
