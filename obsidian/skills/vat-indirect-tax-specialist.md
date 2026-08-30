---
type: skill
generated: true
name: "vat-indirect-tax-specialist"
category: "tax-specialist"
userFacing: true
evaluationPassed: true
evaluationMode: "compatibility"
caseCount: 3
recordedResultCount: 3
sourcePath: "skills/vat-indirect-tax-specialist/SKILL.md"
tags:
  - skill
  - skill-category/tax-specialist
---

# vat-indirect-tax-specialist

Analysiert Umsatzsteuer-/VAT-Matters entlang Steuerbarkeit, Leistungsart, Leistungsort, Steuerbefreiung, Steuersatz, Bemessungsgrundlage, Reverse Charge, Rechnung, Vorsteuer und grenzüberschreitender Behandlung und hält Contract-, Customs- und International-Tax-Abhängigkeiten getrennt.

> Generated from canonical repository metadata. Do not edit this note manually.

## Category

[[categories/tax-specialist|tax-specialist]]

## Requires

- [[skills/current-tax-context|current-tax-context]]
- [[skills/tax-position-register|tax-position-register]]

## Required by

- —

## Outputs

- `vat-assessment.json`
- `vat-open-issues.json`
- `vat-transaction-map.json`

## Output consumers

### `vat-assessment.json`

- Terminal or currently unconsumed output.

### `vat-open-issues.json`

- Terminal or currently unconsumed output.

### `vat-transaction-map.json`

- Terminal or currently unconsumed output.

## Evaluation

- Mode: `compatibility`
- Passed: `True`
- Cases: `3`
- Recorded results: `3`

## Canonical source

`skills/vat-indirect-tax-specialist/SKILL.md`
