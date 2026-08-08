---
type: skill
generated: true
name: "fda-510k-predicate-strategy"
category: "regulated-engineering"
userFacing: true
evaluationPassed: true
evaluationMode: "compatibility"
caseCount: 3
recordedResultCount: 3
sourcePath: "skills/fda-510k-predicate-strategy/SKILL.md"
tags:
  - skill
  - skill-category/regulated-engineering
---

# fda-510k-predicate-strategy

Findet und bewertet 510(k)-Predicate-Kandidaten evidenzgebunden auf rechtliche Vermarktbarkeit, Intended Use, Technologie, Safety/Performance und aktuelle FDA-Quellen.

> Generated from canonical repository metadata. Do not edit this note manually.

## Category

[[categories/regulated-engineering|regulated-engineering]]

## Requires

- [[skills/fda-device-classification-product-code|fda-device-classification-product-code]]
- [[skills/regulated-product-context|regulated-product-context]]
- [[skills/regulatory-evidence-traceability|regulatory-evidence-traceability]]
- [[skills/research-to-evidence-note|research-to-evidence-note]]

## Required by

- [[skills/fda-510k-substantial-equivalence|fda-510k-substantial-equivalence]]

## Outputs

- `predicate-candidate-set.json`
- `predicate-strategy.md`

## Output consumers

### `predicate-candidate-set.json`

- [[skills/fda-510k-substantial-equivalence|fda-510k-substantial-equivalence]]

### `predicate-strategy.md`

- [[skills/fda-510k-substantial-equivalence|fda-510k-substantial-equivalence]]

## Evaluation

- Mode: `compatibility`
- Passed: `True`
- Cases: `3`
- Recorded results: `3`

## Canonical source

`skills/fda-510k-predicate-strategy/SKILL.md`
