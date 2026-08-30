---
type: skill
generated: true
name: "tax-matter-final-gate"
category: "workflow"
userFacing: true
evaluationPassed: true
evaluationMode: "compatibility"
caseCount: 3
recordedResultCount: 3
sourcePath: "skills/tax-matter-final-gate/SKILL.md"
tags:
  - skill
  - skill-category/workflow
---

# tax-matter-final-gate

Prüft vor Abschluss, Filing, Änderung, Einspruch, Umsetzung oder Übergabe eines Tax Matters, ob Facts, aktuelle Rechtsgrundlage, Berechnung, Positionen, Professional Review, Legal-/Accounting-/Valuation-Dependencies, Fristen und Autorität konsistent geschlossen oder ausdrücklich offen dokumentiert sind.

> Generated from canonical repository metadata. Do not edit this note manually.

## Category

[[categories/workflow|workflow]]

## Requires

- [[skills/tax-position-register|tax-position-register]]
- [[skills/tax-professional-routing|tax-professional-routing]]

## Required by

- [[skills/tax-advisory-office|tax-advisory-office]]

## Outputs

- `tax-final-gate-status.json`
- `tax-next-safe-action.json`
- `tax-open-items.json`

## Output consumers

### `tax-final-gate-status.json`

- [[skills/tax-advisory-office|tax-advisory-office]]

### `tax-next-safe-action.json`

- [[skills/tax-advisory-office|tax-advisory-office]]

### `tax-open-items.json`

- [[skills/tax-advisory-office|tax-advisory-office]]

## Evaluation

- Mode: `compatibility`
- Passed: `True`
- Cases: `3`
- Recorded results: `3`

## Canonical source

`skills/tax-matter-final-gate/SKILL.md`
