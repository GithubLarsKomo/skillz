---
type: skill
generated: true
name: "medical-device-complaint-customer-followup"
category: "regulated-engineering"
userFacing: true
evaluationPassed: true
evaluationMode: "compatibility"
caseCount: 4
recordedResultCount: 4
sourcePath: "skills/medical-device-complaint-customer-followup/SKILL.md"
tags:
  - skill
  - skill-category/regulated-engineering
---

# medical-device-complaint-customer-followup

Plant und dokumentiert Medical-Device-/IVD-Customer-Follow-up für offene oder wieder zu öffnende Complaints evidenzbasiert, konsistent und datensparsam und führt neue Fakten kontrolliert in Complaint- und Regulatory-Reassessment zurück, ohne Investigation oder Reportability zu übernehmen.

> Generated from canonical repository metadata. Do not edit this note manually.

## Category

[[categories/regulated-engineering|regulated-engineering]]

## Requires

- [[skills/medical-device-complaint-handling|medical-device-complaint-handling]]
- [[skills/quality-record-integrity|quality-record-integrity]]
- [[skills/regulated-product-context|regulated-product-context]]

## Required by

- [[skills/medical-device-complaint-regulatory-routing|medical-device-complaint-regulatory-routing]]

## Outputs

- `customer-communication-record.json`
- `customer-followup-evidence.json`
- `customer-followup-plan.json`

## Output consumers

### `customer-communication-record.json`

- [[skills/medical-device-complaint-regulatory-routing|medical-device-complaint-regulatory-routing]]

### `customer-followup-evidence.json`

- [[skills/medical-device-complaint-regulatory-routing|medical-device-complaint-regulatory-routing]]

### `customer-followup-plan.json`

- [[skills/medical-device-complaint-regulatory-routing|medical-device-complaint-regulatory-routing]]

## Evaluation

- Mode: `compatibility`
- Passed: `True`
- Cases: `4`
- Recorded results: `4`

## Canonical source

`skills/medical-device-complaint-customer-followup/SKILL.md`
