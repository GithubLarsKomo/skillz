---
type: skill
generated: true
name: "fda-qmsr-iso13485-gap"
category: "regulated-engineering"
userFacing: true
evaluationPassed: true
evaluationMode: "compatibility"
caseCount: 3
recordedResultCount: 3
sourcePath: "skills/fda-qmsr-iso13485-gap/SKILL.md"
tags:
  - skill
  - skill-category/regulated-engineering
---

# fda-qmsr-iso13485-gap

Trennt ISO-13485-QMS-Evidenz von aktuellen FDA-QMSR-spezifischen Pflichten, Inspection-Impacts und Gaps, ohne ein zweites QMS-Prozessmodell zu erzeugen.

> Generated from canonical repository metadata. Do not edit this note manually.

## Category

[[categories/regulated-engineering|regulated-engineering]]

## Requires

- [[skills/medical-device-qms-iso13485|medical-device-qms-iso13485]]
- [[skills/regulatory-evidence-traceability|regulatory-evidence-traceability]]
- [[skills/two-axis-compliance-review|two-axis-compliance-review]]

## Required by

- [[skills/fda-qmsr-inspection-readiness|fda-qmsr-inspection-readiness]]

## Outputs

- `qmsr-gap-assessment.md`
- `qmsr-iso13485-delta.json`

## Output consumers

### `qmsr-gap-assessment.md`

- [[skills/fda-qmsr-inspection-readiness|fda-qmsr-inspection-readiness]]

### `qmsr-iso13485-delta.json`

- [[skills/fda-qmsr-inspection-readiness|fda-qmsr-inspection-readiness]]

## Evaluation

- Mode: `compatibility`
- Passed: `True`
- Cases: `3`
- Recorded results: `3`

## Canonical source

`skills/fda-qmsr-iso13485-gap/SKILL.md`
