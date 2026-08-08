---
type: skill
generated: true
name: "medical-device-field-action-communication"
category: "regulated-engineering"
userFacing: true
evaluationPassed: true
evaluationMode: "compatibility"
caseCount: 4
recordedResultCount: 4
sourcePath: "skills/medical-device-field-action-communication/SKILL.md"
tags:
  - skill
  - skill-category/regulated-engineering
---

# medical-device-field-action-communication

Plant, kontrolliert und evidenziert Medical-Device-/IVD-Field-Action-, FSN- und Recall-Kommunikation über Kunden, Distributoren und Downstream-Empfänger, ohne Versand, Zustellung, Acknowledgement oder Maßnahmenabschluss zu simulieren.

> Generated from canonical repository metadata. Do not edit this note manually.

## Category

[[categories/regulated-engineering|regulated-engineering]]

## Requires

- [[skills/controlled-quality-documentation|controlled-quality-documentation]]
- [[skills/quality-record-integrity|quality-record-integrity]]
- [[skills/regulated-product-context|regulated-product-context]]

## Required by

- [[skills/medical-device-field-action-effectiveness|medical-device-field-action-effectiveness]]
- [[skills/medical-device-field-action-physical-execution|medical-device-field-action-physical-execution]]

## Outputs

- `field-action-communication-state.json`
- `field-action-notice-package.json`
- `field-action-recipient-scope.json`

## Output consumers

### `field-action-communication-state.json`

- [[skills/medical-device-field-action-effectiveness|medical-device-field-action-effectiveness]]
- [[skills/medical-device-field-action-physical-execution|medical-device-field-action-physical-execution]]

### `field-action-notice-package.json`

- [[skills/medical-device-field-action-effectiveness|medical-device-field-action-effectiveness]]
- [[skills/medical-device-field-action-physical-execution|medical-device-field-action-physical-execution]]

### `field-action-recipient-scope.json`

- [[skills/medical-device-field-action-effectiveness|medical-device-field-action-effectiveness]]
- [[skills/medical-device-field-action-physical-execution|medical-device-field-action-physical-execution]]

## Evaluation

- Mode: `compatibility`
- Passed: `True`
- Cases: `4`
- Recorded results: `4`

## Canonical source

`skills/medical-device-field-action-communication/SKILL.md`
