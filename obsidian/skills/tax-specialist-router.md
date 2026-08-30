---
type: skill
generated: true
name: "tax-specialist-router"
category: "workflow"
userFacing: true
evaluationPassed: true
evaluationMode: "compatibility"
caseCount: 3
recordedResultCount: 3
sourcePath: "skills/tax-specialist-router/SKILL.md"
tags:
  - skill
  - skill-category/workflow
---

# tax-specialist-router

Zerlegt Tax Matters in fachlich kohärente Work Orders für passende Tax Specialists und integriert deren Ergebnisse, ohne deren Fachlogik zu duplizieren; Legal, Accounting, Valuation und Counsel bleiben eigene Ownership-Layer.

> Generated from canonical repository metadata. Do not edit this note manually.

## Category

[[categories/workflow|workflow]]

## Requires

- [[skills/current-tax-context|current-tax-context]]

## Required by

- [[skills/tax-advisory-office|tax-advisory-office]]

## Outputs

- `tax-specialist-integration-status.json`
- `tax-specialist-route-map.json`
- `tax-specialist-work-orders.json`

## Output consumers

### `tax-specialist-integration-status.json`

- [[skills/tax-advisory-office|tax-advisory-office]]

### `tax-specialist-route-map.json`

- [[skills/tax-advisory-office|tax-advisory-office]]

### `tax-specialist-work-orders.json`

- [[skills/tax-advisory-office|tax-advisory-office]]

## Evaluation

- Mode: `compatibility`
- Passed: `True`
- Cases: `3`
- Recorded results: `3`

## Canonical source

`skills/tax-specialist-router/SKILL.md`
