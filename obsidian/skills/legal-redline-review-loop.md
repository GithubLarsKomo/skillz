---
type: skill
generated: true
name: "legal-redline-review-loop"
category: "workflow"
userFacing: true
evaluationPassed: true
evaluationMode: "compatibility"
caseCount: 3
recordedResultCount: 3
sourcePath: "skills/legal-redline-review-loop/SKILL.md"
tags:
  - skill
  - skill-category/workflow
---

# legal-redline-review-loop

Vergleicht neue Vertrags- oder Legal-Redline-Versionen mit dem letzten bewerteten Stand, hält Issue-Lineage und Verhandlungszustand stabil und klassifiziert Änderungen als improved, accepted, neutral, deteriorated, new-risk, resolved oder regression. Verwenden in iterativen Vertragsverhandlungen nach initialem Review und Negotiation Strategy.

> Generated from canonical repository metadata. Do not edit this note manually.

## Category

[[categories/workflow|workflow]]

## Requires

- [[skills/contract-review|contract-review]]
- [[skills/legal-negotiation-strategy|legal-negotiation-strategy]]

## Required by

- [[skills/contract-matter-workflow|contract-matter-workflow]]

## Outputs

- `negotiation-state.json`
- `redline-delta.json`
- `redline-review.md`

## Output consumers

### `negotiation-state.json`

- [[skills/contract-matter-workflow|contract-matter-workflow]]

### `redline-delta.json`

- [[skills/contract-matter-workflow|contract-matter-workflow]]

### `redline-review.md`

- [[skills/contract-matter-workflow|contract-matter-workflow]]

## Evaluation

- Mode: `compatibility`
- Passed: `True`
- Cases: `3`
- Recorded results: `3`

## Canonical source

`skills/legal-redline-review-loop/SKILL.md`
