---
type: skill
generated: true
name: "medical-device-customer-contact-intake"
category: "regulated-engineering"
userFacing: true
evaluationPassed: true
evaluationMode: "compatibility"
caseCount: 4
recordedResultCount: 4
sourcePath: "skills/medical-device-customer-contact-intake/SKILL.md"
tags:
  - skill
  - skill-category/regulated-engineering
---

# medical-device-customer-contact-intake

Normalisiert Medical-Device-/IVD-Kundenkontakte kanalunabhängig in einen belastbaren Quality-Intake und trennt Service, Feedback, mögliche Complaint und potenzielles Safety-Signal, ohne Beschwerden durch Wortwahl, Kulanz oder Frontline-Lösung wegzuklassifizieren.

> Generated from canonical repository metadata. Do not edit this note manually.

## Category

[[categories/regulated-engineering|regulated-engineering]]

## Requires

- [[skills/quality-record-integrity|quality-record-integrity]]

## Required by

- [[skills/medical-device-complaint-handling|medical-device-complaint-handling]]
- [[skills/medical-device-service-report-quality-routing|medical-device-service-report-quality-routing]]

## Outputs

- `complaint-intake-handoff.json`
- `customer-contact-record.json`
- `customer-contact-triage.json`

## Output consumers

### `complaint-intake-handoff.json`

- [[skills/medical-device-complaint-handling|medical-device-complaint-handling]]
- [[skills/medical-device-service-report-quality-routing|medical-device-service-report-quality-routing]]

### `customer-contact-record.json`

- [[skills/medical-device-complaint-handling|medical-device-complaint-handling]]
- [[skills/medical-device-service-report-quality-routing|medical-device-service-report-quality-routing]]

### `customer-contact-triage.json`

- [[skills/medical-device-complaint-handling|medical-device-complaint-handling]]
- [[skills/medical-device-service-report-quality-routing|medical-device-service-report-quality-routing]]

## Evaluation

- Mode: `compatibility`
- Passed: `True`
- Cases: `4`
- Recorded results: `4`

## Canonical source

`skills/medical-device-customer-contact-intake/SKILL.md`
