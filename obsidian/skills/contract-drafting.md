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

Erzeugt aus bestätigten Requirements und einem geprüften Legal Context einen privaten oder beruflichen Vertragsentwurf, wahlweise auf Basis einer hochgeladenen Vorlage, und dokumentiert Platzhalter, Abweichungen, Rechtsannahmen und offene Punkte. Verwenden für neue Vertragsentwürfe oder template-basiertes Drafting, nicht für die primäre Bewertung eines fremden Vertrags.

> Generated from canonical repository metadata. Do not edit this note manually.

## Category

[[categories/workflow|workflow]]

## Requires

- [[skills/contract-legal-context|contract-legal-context]]

## Required by

- [[skills/contract-workflow|contract-workflow]]

## Outputs

- `contract-draft.md`
- `contract-drafting-report.json`
- `contract-open-points.md`

## Output consumers

### `contract-draft.md`

- [[skills/contract-workflow|contract-workflow]]

### `contract-drafting-report.json`

- [[skills/contract-workflow|contract-workflow]]

### `contract-open-points.md`

- [[skills/contract-workflow|contract-workflow]]

## Evaluation

- Mode: `compatibility`
- Passed: `True`
- Cases: `3`
- Recorded results: `3`

## Canonical source

`skills/contract-drafting/SKILL.md`
