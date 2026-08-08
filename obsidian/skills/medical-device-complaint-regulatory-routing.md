---
type: skill
generated: true
name: "medical-device-complaint-regulatory-routing"
category: "regulated-engineering"
userFacing: true
evaluationPassed: true
evaluationMode: "compatibility"
caseCount: 5
recordedResultCount: 5
sourcePath: "skills/medical-device-complaint-regulatory-routing/SKILL.md"
tags:
  - skill
  - skill-category/regulated-engineering
---

# medical-device-complaint-regulatory-routing

Überführt Medical-Device-/IVD-Complaint-Fakten, Customer-Follow-up und Awareness-Evidence frühzeitig in jurisdiction-spezifische Reportability-/Vigilance-Assessments, ohne selbst FDA-MDR-, EU-Vigilance- oder andere Behördenentscheidungen zu treffen.

> Generated from canonical repository metadata. Do not edit this note manually.

## Category

[[categories/regulated-engineering|regulated-engineering]]

## Requires

- [[skills/fda-complaint-mdr-reportability|fda-complaint-mdr-reportability]]
- [[skills/ivdr-pms-vigilance|ivdr-pms-vigilance]]
- [[skills/medical-device-complaint-customer-followup|medical-device-complaint-customer-followup]]
- [[skills/medical-device-complaint-handling|medical-device-complaint-handling]]
- [[skills/regulated-product-context|regulated-product-context]]
- [[skills/regulatory-evidence-traceability|regulatory-evidence-traceability]]

## Required by

- —

## Outputs

- `complaint-regulatory-routing.json`
- `regulatory-awareness-timeline.json`
- `vigilance-entry-handoff.json`

## Output consumers

### `complaint-regulatory-routing.json`

- Terminal or currently unconsumed output.

### `regulatory-awareness-timeline.json`

- Terminal or currently unconsumed output.

### `vigilance-entry-handoff.json`

- Terminal or currently unconsumed output.

## Evaluation

- Mode: `compatibility`
- Passed: `True`
- Cases: `5`
- Recorded results: `5`

## Canonical source

`skills/medical-device-complaint-regulatory-routing/SKILL.md`
