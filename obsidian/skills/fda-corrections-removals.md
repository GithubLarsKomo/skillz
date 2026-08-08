---
type: skill
generated: true
name: "fda-corrections-removals"
category: "regulated-engineering"
userFacing: true
evaluationPassed: true
evaluationMode: "compatibility"
caseCount: 4
recordedResultCount: 4
sourcePath: "skills/fda-corrections-removals/SKILL.md"
tags:
  - skill
  - skill-category/regulated-engineering
---

# fda-corrections-removals

Bewertet Medical-Device-Korrekturen und -Entfernungen nach 21 CFR 806/Part 7 auf Reportability, 10-Arbeitstage-Frist, Recall-/Recordkeeping-Pfad und verknüpft Risk, MDR, CAPA und externe FDA-Aktionen ohne diese zu duplizieren.

> Generated from canonical repository metadata. Do not edit this note manually.

## Category

[[categories/regulated-engineering|regulated-engineering]]

## Requires

- [[skills/decision-record|decision-record]]
- [[skills/fda-complaint-mdr-reportability|fda-complaint-mdr-reportability]]
- [[skills/medical-device-capa|medical-device-capa]]
- [[skills/medical-device-risk-management-iso14971|medical-device-risk-management-iso14971]]

## Required by

- [[skills/fda-recall-status-termination|fda-recall-status-termination]]

## Outputs

- `correction-removal-action-plan.json`
- `correction-removal-assessment.json`
- `correction-removal-reporting-state.json`

## Output consumers

### `correction-removal-action-plan.json`

- [[skills/fda-recall-status-termination|fda-recall-status-termination]]

### `correction-removal-assessment.json`

- [[skills/fda-recall-status-termination|fda-recall-status-termination]]

### `correction-removal-reporting-state.json`

- [[skills/fda-recall-status-termination|fda-recall-status-termination]]

## Evaluation

- Mode: `compatibility`
- Passed: `True`
- Cases: `4`
- Recorded results: `4`

## Canonical source

`skills/fda-corrections-removals/SKILL.md`
