---
type: skill
generated: true
name: "fda-de-novo-strategy"
category: "regulated-engineering"
userFacing: true
evaluationPassed: true
evaluationMode: "compatibility"
caseCount: 3
recordedResultCount: 3
sourcePath: "skills/fda-de-novo-strategy/SKILL.md"
tags:
  - skill
  - skill-category/regulated-engineering
---

# fda-de-novo-strategy

Entwickelt eine evidenzgebundene FDA-De-Novo-Strategie für neuartige Low-/Moderate-Risk-Devices ohne tragfähigen Predicate und verbindet Risiko, Controls, Evidenz und offene FDA-Fragen.

> Generated from canonical repository metadata. Do not edit this note manually.

## Category

[[categories/regulated-engineering|regulated-engineering]]

## Requires

- [[skills/fda-device-classification-product-code|fda-device-classification-product-code]]
- [[skills/medical-device-risk-management-iso14971|medical-device-risk-management-iso14971]]
- [[skills/regulated-product-context|regulated-product-context]]
- [[skills/regulatory-evidence-traceability|regulatory-evidence-traceability]]

## Required by

- [[skills/fda-de-novo-special-controls|fda-de-novo-special-controls]]

## Outputs

- `de-novo-evidence-gaps.json`
- `de-novo-strategy.json`

## Output consumers

### `de-novo-evidence-gaps.json`

- [[skills/fda-de-novo-special-controls|fda-de-novo-special-controls]]

### `de-novo-strategy.json`

- [[skills/fda-de-novo-special-controls|fda-de-novo-special-controls]]

## Evaluation

- Mode: `compatibility`
- Passed: `True`
- Cases: `3`
- Recorded results: `3`

## Canonical source

`skills/fda-de-novo-strategy/SKILL.md`
