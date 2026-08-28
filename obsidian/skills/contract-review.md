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

Bewertet einen hochgeladenen oder als Text bereitgestellten privaten oder beruflichen Vertrag einschließlich Anlagen und AGB gegen bestätigte Requirements, aktuelle Rechtsgrundlagen, funktionales Deal Model, Mandantenstrategie und wirtschaftlich-operative Risiken und erzeugt eine priorisierte Issue-Liste mit Risk- und Negotiation-Handoffs. Verwenden für Vertragsprüfung und Redline-Vorbereitung, nicht für initiales Drafting.

> Generated from canonical repository metadata. Do not edit this note manually.

## Category

[[categories/workflow|workflow]]

## Requires

- [[skills/agreement-type-analysis|agreement-type-analysis]]
- [[skills/current-law-context|current-law-context]]

## Required by

- [[skills/contract-matter-workflow|contract-matter-workflow]]
- [[skills/legal-redline-review-loop|legal-redline-review-loop]]

## Outputs

- `contract-issue-list.json`
- `contract-review.json`
- `contract-review.md`
- `contract-risk-input.json`

## Output consumers

### `contract-issue-list.json`

- [[skills/contract-matter-workflow|contract-matter-workflow]]
- [[skills/legal-redline-review-loop|legal-redline-review-loop]]

### `contract-review.json`

- [[skills/contract-matter-workflow|contract-matter-workflow]]
- [[skills/legal-redline-review-loop|legal-redline-review-loop]]

### `contract-review.md`

- [[skills/contract-matter-workflow|contract-matter-workflow]]
- [[skills/legal-redline-review-loop|legal-redline-review-loop]]

### `contract-risk-input.json`

- [[skills/contract-matter-workflow|contract-matter-workflow]]
- [[skills/legal-redline-review-loop|legal-redline-review-loop]]

## Evaluation

- Mode: `compatibility`
- Passed: `True`
- Cases: `3`
- Recorded results: `3`

## Canonical source

`skills/contract-review/SKILL.md`
