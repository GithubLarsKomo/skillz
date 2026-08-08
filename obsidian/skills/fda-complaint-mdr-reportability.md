---
type: skill
generated: true
name: "fda-complaint-mdr-reportability"
category: "regulated-engineering"
userFacing: true
evaluationPassed: true
evaluationMode: "compatibility"
caseCount: 5
recordedResultCount: 5
sourcePath: "skills/fda-complaint-mdr-reportability/SKILL.md"
tags:
  - skill
  - skill-category/regulated-engineering
---

# fda-complaint-mdr-reportability

Bewertet Medical-Device-Complaints auf FDA-MDR-Reportability, Timing und Folgeaktionen ohne Complaint- oder CAPA-System zu duplizieren.

> Generated from canonical repository metadata. Do not edit this note manually.

## Category

[[categories/regulated-engineering|regulated-engineering]]

## Requires

- [[skills/medical-device-risk-management-iso14971|medical-device-risk-management-iso14971]]
- [[skills/quality-record-integrity|quality-record-integrity]]
- [[skills/regulated-product-context|regulated-product-context]]
- [[skills/regulatory-evidence-traceability|regulatory-evidence-traceability]]

## Required by

- [[skills/fda-corrections-removals|fda-corrections-removals]]
- [[skills/medical-device-complaint-regulatory-routing|medical-device-complaint-regulatory-routing]]

## Outputs

- `complaint-regulatory-actions.json`
- `mdr-reportability-assessment.json`

## Output consumers

### `complaint-regulatory-actions.json`

- [[skills/fda-corrections-removals|fda-corrections-removals]]
- [[skills/medical-device-complaint-regulatory-routing|medical-device-complaint-regulatory-routing]]

### `mdr-reportability-assessment.json`

- [[skills/fda-corrections-removals|fda-corrections-removals]]
- [[skills/medical-device-complaint-regulatory-routing|medical-device-complaint-regulatory-routing]]

## Evaluation

- Mode: `compatibility`
- Passed: `True`
- Cases: `5`
- Recorded results: `5`

## Canonical source

`skills/fda-complaint-mdr-reportability/SKILL.md`
