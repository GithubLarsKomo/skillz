---
type: skill
generated: true
name: "fda-pccp-change-control"
category: "regulated-engineering"
userFacing: true
evaluationPassed: true
evaluationMode: "compatibility"
caseCount: 3
recordedResultCount: 3
sourcePath: "skills/fda-pccp-change-control/SKILL.md"
tags:
  - skill
  - skill-category/regulated-engineering
---

# fda-pccp-change-control

Bewertet bestätigte Medical-Device-Änderungen gegen einen tatsächlich autorisierten oder cleared FDA-PCCP-Scope, trennt PCCP-konforme Umsetzung von neuer Submission und routet Abweichungen in bestehende Change-/Submission-Pfade.

> Generated from canonical repository metadata. Do not edit this note manually.

## Category

[[categories/regulated-engineering|regulated-engineering]]

## Requires

- [[skills/decision-record|decision-record]]
- [[skills/design-change-regulatory-impact|design-change-regulatory-impact]]
- [[skills/medical-device-risk-management-iso14971|medical-device-risk-management-iso14971]]
- [[skills/regulatory-evidence-traceability|regulatory-evidence-traceability]]

## Required by

- —

## Outputs

- `pccp-applicability.json`
- `pccp-change-evidence.json`
- `pccp-deviation-routing.json`

## Output consumers

### `pccp-applicability.json`

- Terminal or currently unconsumed output.

### `pccp-change-evidence.json`

- Terminal or currently unconsumed output.

### `pccp-deviation-routing.json`

- Terminal or currently unconsumed output.

## Evaluation

- Mode: `compatibility`
- Passed: `True`
- Cases: `3`
- Recorded results: `3`

## Canonical source

`skills/fda-pccp-change-control/SKILL.md`
