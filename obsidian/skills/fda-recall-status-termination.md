---
type: skill
generated: true
name: "fda-recall-status-termination"
category: "regulated-engineering"
userFacing: true
evaluationPassed: true
evaluationMode: "compatibility"
caseCount: 4
recordedResultCount: 4
sourcePath: "skills/fda-recall-status-termination/SKILL.md"
tags:
  - skill
  - skill-category/regulated-engineering
---

# fda-recall-status-termination

Erstellt und verfolgt FDA-Recall-Statusberichte, Termination-Request-Pakete und verifizierte FDA-Authority-States aus kontrollierter Field-Action-Evidence, ohne interne Completion als FDA Termination zu simulieren.

> Generated from canonical repository metadata. Do not edit this note manually.

## Category

[[categories/regulated-engineering|regulated-engineering]]

## Requires

- [[skills/fda-corrections-removals|fda-corrections-removals]]
- [[skills/medical-device-field-action-effectiveness|medical-device-field-action-effectiveness]]
- [[skills/quality-record-integrity|quality-record-integrity]]
- [[skills/regulatory-evidence-traceability|regulatory-evidence-traceability]]

## Required by

- —

## Outputs

- `fda-recall-authority-state.json`
- `fda-recall-status-report.json`
- `fda-recall-termination-request.json`

## Output consumers

### `fda-recall-authority-state.json`

- Terminal or currently unconsumed output.

### `fda-recall-status-report.json`

- Terminal or currently unconsumed output.

### `fda-recall-termination-request.json`

- Terminal or currently unconsumed output.

## Evaluation

- Mode: `compatibility`
- Passed: `True`
- Cases: `4`
- Recorded results: `4`

## Canonical source

`skills/fda-recall-status-termination/SKILL.md`
