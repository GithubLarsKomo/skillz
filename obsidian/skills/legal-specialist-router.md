---
type: skill
generated: true
name: "legal-specialist-router"
category: "workflow"
userFacing: true
evaluationPassed: true
evaluationMode: "compatibility"
caseCount: 3
recordedResultCount: 3
sourcePath: "skills/legal-specialist-router/SKILL.md"
tags:
  - skill
  - skill-category/workflow
---

# legal-specialist-router

Routet präzise Legal-Work-Orders an passende Rechtsgebiets-, Compliance-, Regulatory-, IP- oder Sports-Law-Specialists und integriert deren Ergebnisse, ohne deren Fachlogik zu duplizieren. Verwenden, wenn ein Matter mehrere Rechts- oder Regelwerksschichten berührt.

> Generated from canonical repository metadata. Do not edit this note manually.

## Category

[[categories/workflow|workflow]]

## Requires

- [[skills/current-law-context|current-law-context]]
- [[skills/legal-client-strategy|legal-client-strategy]]

## Required by

- [[skills/legal-compliance-office|legal-compliance-office]]

## Outputs

- `legal-specialist-integration-status.json`
- `legal-specialist-route-map.json`
- `legal-specialist-work-orders.json`

## Output consumers

### `legal-specialist-integration-status.json`

- [[skills/legal-compliance-office|legal-compliance-office]]

### `legal-specialist-route-map.json`

- [[skills/legal-compliance-office|legal-compliance-office]]

### `legal-specialist-work-orders.json`

- [[skills/legal-compliance-office|legal-compliance-office]]

## Evaluation

- Mode: `compatibility`
- Passed: `True`
- Cases: `3`
- Recorded results: `3`

## Canonical source

`skills/legal-specialist-router/SKILL.md`
