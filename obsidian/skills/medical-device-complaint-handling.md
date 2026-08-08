---
type: skill
generated: true
name: "medical-device-complaint-handling"
category: "regulated-engineering"
userFacing: true
evaluationPassed: true
evaluationMode: "compatibility"
caseCount: 4
recordedResultCount: 4
sourcePath: "skills/medical-device-complaint-handling/SKILL.md"
tags:
  - skill
  - skill-category/regulated-engineering
---

# medical-device-complaint-handling

Führt Medical-Device-/IVD-Complaints als kontrollierten QMS-Prozess von Intake über Evaluation und Investigation bis zu evidenzbasierter Closure, ohne MDR-/Vigilance-Reportability, CAPA oder Risk Management zu duplizieren.

> Generated from canonical repository metadata. Do not edit this note manually.

## Category

[[categories/regulated-engineering|regulated-engineering]]

## Requires

- [[skills/medical-device-customer-contact-intake|medical-device-customer-contact-intake]]
- [[skills/quality-record-integrity|quality-record-integrity]]
- [[skills/regulated-product-context|regulated-product-context]]

## Required by

- [[skills/medical-device-adverse-event-coding|medical-device-adverse-event-coding]]
- [[skills/medical-device-complaint-customer-followup|medical-device-complaint-customer-followup]]
- [[skills/medical-device-complaint-regulatory-routing|medical-device-complaint-regulatory-routing]]

## Outputs

- `complaint-closure-readiness.json`
- `complaint-investigation-plan.json`
- `complaint-record.json`
- `complaint-regulatory-handoff.json`

## Output consumers

### `complaint-closure-readiness.json`

- [[skills/medical-device-adverse-event-coding|medical-device-adverse-event-coding]]
- [[skills/medical-device-complaint-customer-followup|medical-device-complaint-customer-followup]]
- [[skills/medical-device-complaint-regulatory-routing|medical-device-complaint-regulatory-routing]]

### `complaint-investigation-plan.json`

- [[skills/medical-device-adverse-event-coding|medical-device-adverse-event-coding]]
- [[skills/medical-device-complaint-customer-followup|medical-device-complaint-customer-followup]]
- [[skills/medical-device-complaint-regulatory-routing|medical-device-complaint-regulatory-routing]]

### `complaint-record.json`

- [[skills/medical-device-adverse-event-coding|medical-device-adverse-event-coding]]
- [[skills/medical-device-complaint-customer-followup|medical-device-complaint-customer-followup]]
- [[skills/medical-device-complaint-regulatory-routing|medical-device-complaint-regulatory-routing]]

### `complaint-regulatory-handoff.json`

- [[skills/medical-device-adverse-event-coding|medical-device-adverse-event-coding]]
- [[skills/medical-device-complaint-customer-followup|medical-device-complaint-customer-followup]]
- [[skills/medical-device-complaint-regulatory-routing|medical-device-complaint-regulatory-routing]]

## Evaluation

- Mode: `compatibility`
- Passed: `True`
- Cases: `4`
- Recorded results: `4`

## Canonical source

`skills/medical-device-complaint-handling/SKILL.md`
