---
type: skill
generated: true
name: "medical-device-adverse-event-coding"
category: "regulated-engineering"
userFacing: true
evaluationPassed: true
evaluationMode: "compatibility"
caseCount: 3
recordedResultCount: 3
sourcePath: "skills/medical-device-adverse-event-coding/SKILL.md"
tags:
  - skill
  - skill-category/regulated-engineering
---

# medical-device-adverse-event-coding

Normalisiert Medical-Device-/IVD-Complaint- und Adverse-Event-Fakten in versionierte IMDRF-/marktbezogene Code-Kandidaten mit Quellenbindung, ohne Codierung mit Kausalität oder Reportability zu verwechseln.

> Generated from canonical repository metadata. Do not edit this note manually.

## Category

[[categories/regulated-engineering|regulated-engineering]]

## Requires

- [[skills/medical-device-complaint-handling|medical-device-complaint-handling]]
- [[skills/regulatory-evidence-traceability|regulatory-evidence-traceability]]

## Required by

- —

## Outputs

- `adverse-event-code-set.json`
- `adverse-event-coding-delta.json`
- `adverse-event-coding-rationale.json`

## Output consumers

### `adverse-event-code-set.json`

- Terminal or currently unconsumed output.

### `adverse-event-coding-delta.json`

- Terminal or currently unconsumed output.

### `adverse-event-coding-rationale.json`

- Terminal or currently unconsumed output.

## Evaluation

- Mode: `compatibility`
- Passed: `True`
- Cases: `3`
- Recorded results: `3`

## Canonical source

`skills/medical-device-adverse-event-coding/SKILL.md`
