---
type: skill
generated: true
name: "tax-matter-intake"
category: "analysis"
userFacing: true
evaluationPassed: true
evaluationMode: "compatibility"
caseCount: 3
recordedResultCount: 3
sourcePath: "skills/tax-matter-intake/SKILL.md"
tags:
  - skill
  - skill-category/analysis
---

# tax-matter-intake

Strukturiert steuerliche Matters auf Steuerpflichtigen-/Entity-, Zeitraum-, Jurisdiktions-, Steuerarten-, Fristen-, Facts- und Dokumentebene und trennt bestätigte Tatsachen, Annahmen, fehlende Belege und Legal-/Accounting-/Valuation-Abhängigkeiten vor materieller Tax-Analyse.

> Generated from canonical repository metadata. Do not edit this note manually.

## Category

[[categories/analysis|analysis]]

## Requires

- —

## Required by

- [[skills/tax-advisory-office|tax-advisory-office]]

## Outputs

- `tax-dependency-map.json`
- `tax-fact-gaps.json`
- `tax-matter.json`

## Output consumers

### `tax-dependency-map.json`

- [[skills/tax-advisory-office|tax-advisory-office]]

### `tax-fact-gaps.json`

- [[skills/tax-advisory-office|tax-advisory-office]]

### `tax-matter.json`

- [[skills/tax-advisory-office|tax-advisory-office]]

## Evaluation

- Mode: `compatibility`
- Passed: `True`
- Cases: `3`
- Recorded results: `3`

## Canonical source

`skills/tax-matter-intake/SKILL.md`
