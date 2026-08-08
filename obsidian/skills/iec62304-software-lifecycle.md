---
type: skill
generated: true
name: "iec62304-software-lifecycle"
category: "regulated-engineering"
userFacing: true
evaluationPassed: true
evaluationMode: "compatibility"
caseCount: 3
recordedResultCount: 3
sourcePath: "skills/iec62304-software-lifecycle/SKILL.md"
tags:
  - skill
  - skill-category/regulated-engineering
---

# iec62304-software-lifecycle

Bewertet Medical-Device-Software-Lifecycle, Safety Class und Evidence Gaps entlang IEC 62304 ohne QMS oder Risk zu duplizieren.

> Generated from canonical repository metadata. Do not edit this note manually.

## Category

[[categories/regulated-engineering|regulated-engineering]]

## Requires

- [[skills/design-control-traceability|design-control-traceability]]
- [[skills/medical-device-qms-iso13485|medical-device-qms-iso13485]]
- [[skills/medical-device-risk-management-iso14971|medical-device-risk-management-iso14971]]
- [[skills/regulated-product-context|regulated-product-context]]

## Required by

- [[skills/medical-device-cybersecurity-lifecycle|medical-device-cybersecurity-lifecycle]]

## Outputs

- `software-evidence-gaps.json`
- `software-lifecycle-assessment.json`
- `software-safety-classification.json`

## Output consumers

### `software-evidence-gaps.json`

- [[skills/medical-device-cybersecurity-lifecycle|medical-device-cybersecurity-lifecycle]]

### `software-lifecycle-assessment.json`

- [[skills/medical-device-cybersecurity-lifecycle|medical-device-cybersecurity-lifecycle]]

### `software-safety-classification.json`

- [[skills/medical-device-cybersecurity-lifecycle|medical-device-cybersecurity-lifecycle]]

## Evaluation

- Mode: `compatibility`
- Passed: `True`
- Cases: `3`
- Recorded results: `3`

## Canonical source

`skills/iec62304-software-lifecycle/SKILL.md`
