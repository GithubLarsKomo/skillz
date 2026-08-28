---
type: skill
generated: true
name: "contract-drafting"
category: "workflow"
userFacing: true
evaluationPassed: true
evaluationMode: "compatibility"
caseCount: 3
recordedResultCount: 3
sourcePath: "skills/contract-drafting/SKILL.md"
tags:
  - skill
  - skill-category/workflow
---

# contract-drafting

Erzeugt aus bestätigten Requirements, Client Strategy, aktuellem Rechtskontext und funktionalem Deal Model einen privaten oder beruflichen Vertragsentwurf, wahlweise auf Basis einer hochgeladenen Vorlage, und dokumentiert Platzhalter, Abweichungen, Specialist Inputs, Rechtsannahmen und offene Punkte. Verwenden für neue Vertragsentwürfe oder template-basiertes Drafting, nicht für primäre Fremdvertragsbewertung.

> Generated from canonical repository metadata. Do not edit this note manually.

## Category

[[categories/workflow|workflow]]

## Requires

- [[skills/agreement-type-analysis|agreement-type-analysis]]
- [[skills/current-law-context|current-law-context]]

## Required by

- [[skills/contract-matter-workflow|contract-matter-workflow]]

## Outputs

- `contract-draft.md`
- `contract-drafting-report.json`
- `contract-open-points.md`

## Output consumers

### `contract-draft.md`

- [[skills/contract-matter-workflow|contract-matter-workflow]]

### `contract-drafting-report.json`

- [[skills/contract-matter-workflow|contract-matter-workflow]]

### `contract-open-points.md`

- [[skills/contract-matter-workflow|contract-matter-workflow]]

## Evaluation

- Mode: `compatibility`
- Passed: `True`
- Cases: `3`
- Recorded results: `3`

## Canonical source

`skills/contract-drafting/SKILL.md`
