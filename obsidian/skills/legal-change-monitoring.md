---
type: skill
generated: true
name: "legal-change-monitoring"
category: "workflow"
userFacing: true
evaluationPassed: true
evaluationMode: "compatibility"
caseCount: 3
recordedResultCount: 3
sourcePath: "skills/legal-change-monitoring/SKILL.md"
tags:
  - skill
  - skill-category/workflow
---

# legal-change-monitoring

Überwacht Rechtsänderungen außerhalb des spezialisierten Medical-Device-Regulatory-Monitorings über versionierte Primärquellen-Snapshots, trennt echte normative Änderungen von Metadaten-/Guidance-Änderungen und erzeugt belastbare Legal-Change-Events mit asOf, Effective Date und betroffenen Rechtsgebieten.

> Generated from canonical repository metadata. Do not edit this note manually.

## Category

[[categories/workflow|workflow]]

## Requires

- [[skills/current-law-context|current-law-context]]
- [[skills/research-to-evidence-note|research-to-evidence-note]]

## Required by

- [[skills/legal-change-impact-orchestrator|legal-change-impact-orchestrator]]

## Outputs

- `legal-change-events.json`
- `legal-change-watch-status.json`
- `legal-source-watch-register.json`

## Output consumers

### `legal-change-events.json`

- [[skills/legal-change-impact-orchestrator|legal-change-impact-orchestrator]]

### `legal-change-watch-status.json`

- [[skills/legal-change-impact-orchestrator|legal-change-impact-orchestrator]]

### `legal-source-watch-register.json`

- [[skills/legal-change-impact-orchestrator|legal-change-impact-orchestrator]]

## Evaluation

- Mode: `compatibility`
- Passed: `True`
- Cases: `3`
- Recorded results: `3`

## Canonical source

`skills/legal-change-monitoring/SKILL.md`
