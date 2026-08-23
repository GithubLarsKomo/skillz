---
type: skill
generated: true
name: "contract-review"
category: "workflow"
userFacing: true
evaluationPassed: true
evaluationMode: "compatibility"
caseCount: 3
recordedResultCount: 3
sourcePath: "skills/contract-review/SKILL.md"
tags:
  - skill
  - skill-category/workflow
---

# contract-review

Bewertet einen hochgeladenen oder als Text bereitgestellten privaten oder beruflichen Vertrag einschließlich Anlagen und AGB gegen bestätigte Requirements, Rechtsgrundlagen und wirtschaftlich-operative Risiken und erzeugt eine priorisierte Issue-Liste mit Verhandlungspositionen. Verwenden für Vertragsprüfung, Risikoanalyse und Redline-Vorbereitung, nicht für die initiale Vertragserzeugung.

> Generated from canonical repository metadata. Do not edit this note manually.

## Category

[[categories/workflow|workflow]]

## Requires

- [[skills/contract-legal-context|contract-legal-context]]

## Required by

- [[skills/contract-workflow|contract-workflow]]

## Outputs

- `contract-issue-list.json`
- `contract-review.json`
- `contract-review.md`

## Output consumers

### `contract-issue-list.json`

- [[skills/contract-workflow|contract-workflow]]

### `contract-review.json`

- [[skills/contract-workflow|contract-workflow]]

### `contract-review.md`

- [[skills/contract-workflow|contract-workflow]]

## Evaluation

- Mode: `compatibility`
- Passed: `True`
- Cases: `3`
- Recorded results: `3`

## Canonical source

`skills/contract-review/SKILL.md`
