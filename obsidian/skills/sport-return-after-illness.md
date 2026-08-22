---
type: skill
generated: true
name: "sport-return-after-illness"
category: "workflow"
userFacing: true
evaluationPassed: true
evaluationMode: "compatibility"
caseCount: 3
recordedResultCount: 3
sourcePath: "skills/sport-return-after-illness/SKILL.md"
tags:
  - skill
  - skill-category/workflow
---

# sport-return-after-illness

Steuert die graduelle Rückkehr ins Training nach akuter Erkrankung oder krankheitsbedingter Pause anhand aktueller Symptome, Unterbrechungsdauer, Vorbelastung und Reaktion auf Wiedereinstieg. Verwenden nach Krankheit; kardiopulmonale/systemische Red Flags an medizinische Abklärung routen.

> Generated from canonical repository metadata. Do not edit this note manually.

## Category

[[categories/workflow|workflow]]

## Requires

- [[skills/sport-athlete-profile|sport-athlete-profile]]
- [[skills/sport-daily-athlete-monitoring|sport-daily-athlete-monitoring]]

## Required by

- [[skills/sport-athlete-management|sport-athlete-management]]

## Outputs

- `return-after-illness-plan.json`

## Output consumers

### `return-after-illness-plan.json`

- [[skills/sport-athlete-management|sport-athlete-management]]

## Evaluation

- Mode: `compatibility`
- Passed: `True`
- Cases: `3`
- Recorded results: `3`

## Canonical source

`skills/sport-return-after-illness/SKILL.md`
