---
type: skill
generated: true
name: "regulatory-change-monitoring"
category: "regulated-engineering"
userFacing: true
evaluationPassed: true
evaluationMode: "compatibility"
caseCount: 3
recordedResultCount: 3
sourcePath: "skills/regulatory-change-monitoring/SKILL.md"
tags:
  - skill
  - skill-category/regulated-engineering
---

# regulatory-change-monitoring

Erkennt belastbare Änderungen an offiziellen Regulatory-Quellen über versionierte Snapshots, Status-/Inhalts-Deltas und Freshness und übergibt normalisierte Change Events an bestehende Regulatory-Impact-Owner.

> Generated from canonical repository metadata. Do not edit this note manually.

## Category

[[categories/regulated-engineering|regulated-engineering]]

## Requires

- [[skills/regulatory-evidence-traceability|regulatory-evidence-traceability]]
- [[skills/research-to-evidence-note|research-to-evidence-note]]

## Required by

- —

## Outputs

- `regulatory-change-events.json`
- `regulatory-change-watch-status.json`
- `regulatory-source-register.json`

## Output consumers

### `regulatory-change-events.json`

- Terminal or currently unconsumed output.

### `regulatory-change-watch-status.json`

- Terminal or currently unconsumed output.

### `regulatory-source-register.json`

- Terminal or currently unconsumed output.

## Evaluation

- Mode: `compatibility`
- Passed: `True`
- Cases: `3`
- Recorded results: `3`

## Canonical source

`skills/regulatory-change-monitoring/SKILL.md`
