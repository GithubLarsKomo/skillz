---
type: skill
generated: true
name: "tax-professional-routing"
category: "workflow"
userFacing: true
evaluationPassed: true
evaluationMode: "compatibility"
caseCount: 3
recordedResultCount: 3
sourcePath: "skills/tax-professional-routing/SKILL.md"
tags:
  - skill
  - skill-category/workflow
---

# tax-professional-routing

Prüft für Tax Matters, Positionen, Erklärungen, Einsprüche und Vertretung, ob und an welcher Stelle eine nach Berufsrecht befugte Tax Professional Validation oder externe Authority erforderlich ist, erzeugt dafür ein eng umrissenes Work Package und verhindert die Simulation einer Steuerberaterzulassung.

> Generated from canonical repository metadata. Do not edit this note manually.

## Category

[[categories/workflow|workflow]]

## Requires

- [[skills/current-tax-context|current-tax-context]]

## Required by

- [[skills/tax-advisory-office|tax-advisory-office]]
- [[skills/tax-matter-final-gate|tax-matter-final-gate]]
- [[skills/tax-procedure-matter-workflow|tax-procedure-matter-workflow]]

## Outputs

- `tax-authority-boundaries.json`
- `tax-professional-gate.json`
- `tax-professional-work-order.json`

## Output consumers

### `tax-authority-boundaries.json`

- [[skills/tax-advisory-office|tax-advisory-office]]
- [[skills/tax-matter-final-gate|tax-matter-final-gate]]
- [[skills/tax-procedure-matter-workflow|tax-procedure-matter-workflow]]

### `tax-professional-gate.json`

- [[skills/tax-advisory-office|tax-advisory-office]]
- [[skills/tax-matter-final-gate|tax-matter-final-gate]]
- [[skills/tax-procedure-matter-workflow|tax-procedure-matter-workflow]]

### `tax-professional-work-order.json`

- [[skills/tax-advisory-office|tax-advisory-office]]
- [[skills/tax-matter-final-gate|tax-matter-final-gate]]
- [[skills/tax-procedure-matter-workflow|tax-procedure-matter-workflow]]

## Evaluation

- Mode: `compatibility`
- Passed: `True`
- Cases: `3`
- Recorded results: `3`

## Canonical source

`skills/tax-professional-routing/SKILL.md`
