---
type: skill
generated: true
name: "medical-device-field-action-physical-execution"
category: "regulated-engineering"
userFacing: true
evaluationPassed: true
evaluationMode: "compatibility"
caseCount: 4
recordedResultCount: 4
sourcePath: "skills/medical-device-field-action-physical-execution/SKILL.md"
tags:
  - skill
  - skill-category/regulated-engineering
---

# medical-device-field-action-physical-execution

Steuert und evidenziert die physische Ausführung autorisierter Medical-Device-/IVD-Feldmaßnahmen von RMA, Transport und Chain-of-Custody über Quarantine und Correction bis Verification, Destruction oder anderer Disposition, ohne MRB, Effectiveness oder Authority Closure zu duplizieren.

> Generated from canonical repository metadata. Do not edit this note manually.

## Category

[[categories/regulated-engineering|regulated-engineering]]

## Requires

- [[skills/controlled-quality-documentation|controlled-quality-documentation]]
- [[skills/medical-device-field-action-communication|medical-device-field-action-communication]]
- [[skills/quality-record-integrity|quality-record-integrity]]

## Required by

- [[skills/medical-device-field-action-effectiveness|medical-device-field-action-effectiveness]]

## Outputs

- `field-action-disposition-evidence.json`
- `field-action-physical-execution-plan.json`
- `field-action-unit-custody-ledger.json`

## Output consumers

### `field-action-disposition-evidence.json`

- [[skills/medical-device-field-action-effectiveness|medical-device-field-action-effectiveness]]

### `field-action-physical-execution-plan.json`

- [[skills/medical-device-field-action-effectiveness|medical-device-field-action-effectiveness]]

### `field-action-unit-custody-ledger.json`

- [[skills/medical-device-field-action-effectiveness|medical-device-field-action-effectiveness]]

## Evaluation

- Mode: `compatibility`
- Passed: `True`
- Cases: `4`
- Recorded results: `4`

## Canonical source

`skills/medical-device-field-action-physical-execution/SKILL.md`
