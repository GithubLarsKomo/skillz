---
type: skill
generated: true
name: "medical-device-field-action-effectiveness"
category: "regulated-engineering"
userFacing: true
evaluationPassed: true
evaluationMode: "compatibility"
caseCount: 4
recordedResultCount: 4
sourcePath: "skills/medical-device-field-action-effectiveness/SKILL.md"
tags:
  - skill
  - skill-category/regulated-engineering
---

# medical-device-field-action-effectiveness

Bewertet die tatsächliche Wirksamkeit und Closure-Readiness von Medical-Device-/IVD-Feldmaßnahmen anhand von Recipient-, Communication-, Action-, Product-Reconciliation- und Follow-up-Evidence, ohne CAPA-Effektivität oder Authority-Termination zu simulieren.

> Generated from canonical repository metadata. Do not edit this note manually.

## Category

[[categories/regulated-engineering|regulated-engineering]]

## Requires

- [[skills/medical-device-capa|medical-device-capa]]
- [[skills/medical-device-field-action-communication|medical-device-field-action-communication]]
- [[skills/medical-device-field-action-physical-execution|medical-device-field-action-physical-execution]]
- [[skills/medical-device-pms-system|medical-device-pms-system]]
- [[skills/medical-device-risk-management-iso14971|medical-device-risk-management-iso14971]]
- [[skills/quality-record-integrity|quality-record-integrity]]

## Required by

- [[skills/fda-recall-status-termination|fda-recall-status-termination]]
- [[skills/ivdr-fsca-status-final-reporting|ivdr-fsca-status-final-reporting]]

## Outputs

- `field-action-closure-readiness.json`
- `field-action-effectiveness-assessment.json`
- `field-action-product-reconciliation.json`

## Output consumers

### `field-action-closure-readiness.json`

- [[skills/fda-recall-status-termination|fda-recall-status-termination]]
- [[skills/ivdr-fsca-status-final-reporting|ivdr-fsca-status-final-reporting]]

### `field-action-effectiveness-assessment.json`

- [[skills/fda-recall-status-termination|fda-recall-status-termination]]
- [[skills/ivdr-fsca-status-final-reporting|ivdr-fsca-status-final-reporting]]

### `field-action-product-reconciliation.json`

- [[skills/fda-recall-status-termination|fda-recall-status-termination]]
- [[skills/ivdr-fsca-status-final-reporting|ivdr-fsca-status-final-reporting]]

## Evaluation

- Mode: `compatibility`
- Passed: `True`
- Cases: `4`
- Recorded results: `4`

## Canonical source

`skills/medical-device-field-action-effectiveness/SKILL.md`
