---
type: skill
generated: true
name: "medical-device-service-report-quality-routing"
category: "regulated-engineering"
userFacing: true
evaluationPassed: true
evaluationMode: "compatibility"
caseCount: 3
recordedResultCount: 3
sourcePath: "skills/medical-device-service-report-quality-routing/SKILL.md"
tags:
  - skill
  - skill-category/regulated-engineering
---

# medical-device-service-report-quality-routing

Überführt Medical-Device-/IVD-Service-, Repair- und Troubleshooting-Ereignisse evidenztreu in Quality-/Complaint-/Safety-Routing, ohne Serviceabschluss mit Qualitäts- oder regulatorischer Closure zu verwechseln.

> Generated from canonical repository metadata. Do not edit this note manually.

## Category

[[categories/regulated-engineering|regulated-engineering]]

## Requires

- [[skills/medical-device-customer-contact-intake|medical-device-customer-contact-intake]]
- [[skills/quality-record-integrity|quality-record-integrity]]

## Required by

- —

## Outputs

- `service-complaint-handoff.json`
- `service-event-quality-record.json`
- `service-quality-routing.json`

## Output consumers

### `service-complaint-handoff.json`

- Terminal or currently unconsumed output.

### `service-event-quality-record.json`

- Terminal or currently unconsumed output.

### `service-quality-routing.json`

- Terminal or currently unconsumed output.

## Evaluation

- Mode: `compatibility`
- Passed: `True`
- Cases: `3`
- Recorded results: `3`

## Canonical source

`skills/medical-device-service-report-quality-routing/SKILL.md`
