---
type: skill
generated: true
name: "fda-ivd-clia-waiver"
category: "regulated-engineering"
userFacing: true
evaluationPassed: true
evaluationMode: "compatibility"
caseCount: 3
recordedResultCount: 3
sourcePath: "skills/fda-ivd-clia-waiver/SKILL.md"
tags:
  - skill
  - skill-category/regulated-engineering
---

# fda-ivd-clia-waiver

Bewertet IVDs auf FDA-CLIA-Waiver-Eignung und erzeugt Flex-/User-Study- sowie Evidence-Gaps ohne Submission zu simulieren.

> Generated from canonical repository metadata. Do not edit this note manually.

## Category

[[categories/regulated-engineering|regulated-engineering]]

## Requires

- [[skills/fda-device-classification-product-code|fda-device-classification-product-code]]
- [[skills/medical-device-risk-management-iso14971|medical-device-risk-management-iso14971]]
- [[skills/regulated-product-context|regulated-product-context]]
- [[skills/regulatory-evidence-traceability|regulatory-evidence-traceability]]

## Required by

- [[skills/fda-dual-510k-clia-waiver|fda-dual-510k-clia-waiver]]

## Outputs

- `clia-evidence-gaps.json`
- `clia-waiver-strategy.json`
- `flex-study-needs.json`

## Output consumers

### `clia-evidence-gaps.json`

- [[skills/fda-dual-510k-clia-waiver|fda-dual-510k-clia-waiver]]

### `clia-waiver-strategy.json`

- [[skills/fda-dual-510k-clia-waiver|fda-dual-510k-clia-waiver]]

### `flex-study-needs.json`

- [[skills/fda-dual-510k-clia-waiver|fda-dual-510k-clia-waiver]]

## Evaluation

- Mode: `compatibility`
- Passed: `True`
- Cases: `3`
- Recorded results: `3`

## Canonical source

`skills/fda-ivd-clia-waiver/SKILL.md`
