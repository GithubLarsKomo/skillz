---
type: skill
generated: true
name: "fda-device-classification-product-code"
category: "regulated-engineering"
userFacing: true
evaluationPassed: true
evaluationMode: "compatibility"
caseCount: 3
recordedResultCount: 3
sourcePath: "skills/fda-device-classification-product-code/SKILL.md"
tags:
  - skill
  - skill-category/regulated-engineering
---

# fda-device-classification-product-code

Ermittelt FDA-Geräteklasse, Regulation Number, Product Code und Premarket-Kontext evidenzgebunden aus aktuellen offiziellen Quellen, ohne eine FDA-Entscheidung zu simulieren.

> Generated from canonical repository metadata. Do not edit this note manually.

## Category

[[categories/regulated-engineering|regulated-engineering]]

## Requires

- [[skills/regulated-product-context|regulated-product-context]]
- [[skills/regulatory-evidence-traceability|regulatory-evidence-traceability]]
- [[skills/research-to-evidence-note|research-to-evidence-note]]

## Required by

- [[skills/fda-510k-predicate-strategy|fda-510k-predicate-strategy]]
- [[skills/fda-de-novo-strategy|fda-de-novo-strategy]]
- [[skills/fda-ivd-clia-waiver|fda-ivd-clia-waiver]]

## Outputs

- `fda-device-classification.json`
- `fda-product-code-evidence.json`

## Output consumers

### `fda-device-classification.json`

- [[skills/fda-510k-predicate-strategy|fda-510k-predicate-strategy]]
- [[skills/fda-de-novo-strategy|fda-de-novo-strategy]]
- [[skills/fda-ivd-clia-waiver|fda-ivd-clia-waiver]]

### `fda-product-code-evidence.json`

- [[skills/fda-510k-predicate-strategy|fda-510k-predicate-strategy]]
- [[skills/fda-de-novo-strategy|fda-de-novo-strategy]]
- [[skills/fda-ivd-clia-waiver|fda-ivd-clia-waiver]]

## Evaluation

- Mode: `compatibility`
- Passed: `True`
- Cases: `3`
- Recorded results: `3`

## Canonical source

`skills/fda-device-classification-product-code/SKILL.md`
