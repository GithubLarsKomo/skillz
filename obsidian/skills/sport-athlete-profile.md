---
type: skill
generated: true
name: "sport-athlete-profile"
category: "workflow"
userFacing: true
evaluationPassed: true
evaluationMode: "compatibility"
caseCount: 3
recordedResultCount: 3
sourcePath: "skills/sport-athlete-profile/SKILL.md"
tags:
  - skill
  - skill-category/workflow
---

# sport-athlete-profile

Erfasst und versioniert den trainingsrelevanten Athletenkontext als belastbaren Ausgangszustand für Planung, Monitoring und Adaptation. Verwenden bei Neuaufnahme, Profiländerungen oder wenn Alter, Trainingsalter, Sportart, Verfügbarkeit, Präferenzen oder dokumentierte Einschränkungen für spätere Sport-Skills strukturiert bereitgestellt werden müssen; nicht für medizinische Diagnosen.

> Generated from canonical repository metadata. Do not edit this note manually.

## Category

[[categories/workflow|workflow]]

## Requires

- —

## Required by

- [[skills/sport-athlete-management|sport-athlete-management]]
- [[skills/sport-daily-athlete-monitoring|sport-daily-athlete-monitoring]]
- [[skills/sport-goal-performance-model|sport-goal-performance-model]]
- [[skills/sport-training-adaptation-engine|sport-training-adaptation-engine]]

## Outputs

- `athlete-profile.json`

## Output consumers

### `athlete-profile.json`

- [[skills/sport-athlete-management|sport-athlete-management]]
- [[skills/sport-daily-athlete-monitoring|sport-daily-athlete-monitoring]]
- [[skills/sport-goal-performance-model|sport-goal-performance-model]]
- [[skills/sport-training-adaptation-engine|sport-training-adaptation-engine]]

## Evaluation

- Mode: `compatibility`
- Passed: `True`
- Cases: `3`
- Recorded results: `3`

## Canonical source

`skills/sport-athlete-profile/SKILL.md`
