---
type: skill
generated: true
name: "fda-510k-substantial-equivalence"
category: "regulated-engineering"
userFacing: true
evaluationPassed: true
evaluationMode: "compatibility"
caseCount: 3
recordedResultCount: 3
sourcePath: "skills/fda-510k-substantial-equivalence/SKILL.md"
tags:
  - skill
  - skill-category/regulated-engineering
---

# fda-510k-substantial-equivalence

Baut eine evidenzgebundene 510(k)-Substantial-Equivalence-Bewertung aus Intended Use, technologischen Merkmalen, Safety/Effectiveness-Fragen und Performance-Daten.

> Generated from canonical repository metadata. Do not edit this note manually.

## Category

[[categories/regulated-engineering|regulated-engineering]]

## Requires

- [[skills/fda-510k-predicate-strategy|fda-510k-predicate-strategy]]
- [[skills/medical-device-risk-management-iso14971|medical-device-risk-management-iso14971]]
- [[skills/regulatory-evidence-traceability|regulatory-evidence-traceability]]

## Required by

- [[skills/fda-dual-510k-clia-waiver|fda-dual-510k-clia-waiver]]

## Outputs

- `se-evidence-gaps.json`
- `substantial-equivalence-assessment.json`
- `substantial-equivalence-matrix.md`

## Output consumers

### `se-evidence-gaps.json`

- [[skills/fda-dual-510k-clia-waiver|fda-dual-510k-clia-waiver]]

### `substantial-equivalence-assessment.json`

- [[skills/fda-dual-510k-clia-waiver|fda-dual-510k-clia-waiver]]

### `substantial-equivalence-matrix.md`

- [[skills/fda-dual-510k-clia-waiver|fda-dual-510k-clia-waiver]]

## Evaluation

- Mode: `compatibility`
- Passed: `True`
- Cases: `3`
- Recorded results: `3`

## Canonical source

`skills/fda-510k-substantial-equivalence/SKILL.md`
