---
type: skill
generated: true
name: "medical-device-pms-system"
category: "regulated-engineering"
userFacing: true
evaluationPassed: true
evaluationMode: "compatibility"
caseCount: 3
recordedResultCount: 3
sourcePath: "skills/medical-device-pms-system/SKILL.md"
tags:
  - skill
  - skill-category/regulated-engineering
---

# medical-device-pms-system

Steuert ein marktübergreifendes Medical-Device-PMS-System aus Plan, Datenquellen, Review-Zyklen, Signalrouting, Management-Review-Handoff und Lifecycle-Rückkopplung, ohne Vigilance, Complaint, CAPA oder PMPF zu duplizieren.

> Generated from canonical repository metadata. Do not edit this note manually.

## Category

[[categories/regulated-engineering|regulated-engineering]]

## Requires

- [[skills/decision-record|decision-record]]
- [[skills/medical-device-risk-management-iso14971|medical-device-risk-management-iso14971]]
- [[skills/regulated-product-context|regulated-product-context]]
- [[skills/regulatory-evidence-traceability|regulatory-evidence-traceability]]

## Required by

- [[skills/ivdr-pms-vigilance|ivdr-pms-vigilance]]
- [[skills/medical-device-field-action-effectiveness|medical-device-field-action-effectiveness]]
- [[skills/qms-management-review-governance|qms-management-review-governance]]

## Outputs

- `pms-management-review-input.json`
- `pms-review-status.json`
- `pms-source-register.json`
- `pms-system-plan.json`

## Output consumers

### `pms-management-review-input.json`

- [[skills/ivdr-pms-vigilance|ivdr-pms-vigilance]]
- [[skills/medical-device-field-action-effectiveness|medical-device-field-action-effectiveness]]
- [[skills/qms-management-review-governance|qms-management-review-governance]]

### `pms-review-status.json`

- [[skills/ivdr-pms-vigilance|ivdr-pms-vigilance]]
- [[skills/medical-device-field-action-effectiveness|medical-device-field-action-effectiveness]]
- [[skills/qms-management-review-governance|qms-management-review-governance]]

### `pms-source-register.json`

- [[skills/ivdr-pms-vigilance|ivdr-pms-vigilance]]
- [[skills/medical-device-field-action-effectiveness|medical-device-field-action-effectiveness]]
- [[skills/qms-management-review-governance|qms-management-review-governance]]

### `pms-system-plan.json`

- [[skills/ivdr-pms-vigilance|ivdr-pms-vigilance]]
- [[skills/medical-device-field-action-effectiveness|medical-device-field-action-effectiveness]]
- [[skills/qms-management-review-governance|qms-management-review-governance]]

## Evaluation

- Mode: `compatibility`
- Passed: `True`
- Cases: `3`
- Recorded results: `3`

## Canonical source

`skills/medical-device-pms-system/SKILL.md`
