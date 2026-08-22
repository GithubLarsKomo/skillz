---
type: skill
generated: true
name: "sport-training-adaptation-engine"
category: "workflow"
userFacing: true
evaluationPassed: true
evaluationMode: "compatibility"
caseCount: 3
recordedResultCount: 3
sourcePath: "skills/sport-training-adaptation-engine/SKILL.md"
tags:
  - skill
  - skill-category/workflow
---

# sport-training-adaptation-engine

Vergleicht geplante Belastung, tatsächlich absolvierte Einheit, subjektive und objektive Reaktion, Trends und Health Constraints und erzeugt eine erklärbare akute, taktische oder strategische Trainingsanpassung. Verwenden für Proceed/Modify/Recover/Review-Entscheidungen; nicht als autonomes medizinisches Clearance- oder Verletzungsvorhersagesystem.

> Generated from canonical repository metadata. Do not edit this note manually.

## Category

[[categories/workflow|workflow]]

## Requires

- [[skills/sport-athlete-profile|sport-athlete-profile]]
- [[skills/sport-daily-athlete-monitoring|sport-daily-athlete-monitoring]]
- [[skills/sport-microcycle-planning|sport-microcycle-planning]]

## Required by

- [[skills/sport-athlete-management|sport-athlete-management]]

## Outputs

- `training-adaptation-decision.json`

## Output consumers

### `training-adaptation-decision.json`

- [[skills/sport-athlete-management|sport-athlete-management]]

## Evaluation

- Mode: `compatibility`
- Passed: `True`
- Cases: `3`
- Recorded results: `3`

## Canonical source

`skills/sport-training-adaptation-engine/SKILL.md`
