---
type: skill
generated: true
name: "sport-nutrition-fueling"
category: "workflow"
userFacing: true
evaluationPassed: true
evaluationMode: "compatibility"
caseCount: 3
recordedResultCount: 3
sourcePath: "skills/sport-nutrition-fueling/SKILL.md"
tags:
  - skill
  - skill-category/workflow
---

# sport-nutrition-fueling

Plant leistungsorientiertes Fueling, Proteinverteilung, Flüssigkeit und Wettkampfernährung und erkennt Hinweise auf niedrige Energieverfügbarkeit/RED-S. Verwenden für Trainings- und Wettkampfernährung; nicht als klinische Diätetik oder autonome Diagnose von RED-S.

> Generated from canonical repository metadata. Do not edit this note manually.

## Category

[[categories/workflow|workflow]]

## Requires

- [[skills/sport-athlete-profile|sport-athlete-profile]]
- [[skills/sport-daily-athlete-monitoring|sport-daily-athlete-monitoring]]
- [[skills/sport-mesocycle-planning|sport-mesocycle-planning]]
- [[skills/sport-microcycle-planning|sport-microcycle-planning]]

## Required by

- [[skills/sport-athlete-management|sport-athlete-management]]

## Outputs

- `energy-availability-risk.json`
- `sport-fueling-plan.json`

## Output consumers

### `energy-availability-risk.json`

- [[skills/sport-athlete-management|sport-athlete-management]]

### `sport-fueling-plan.json`

- [[skills/sport-athlete-management|sport-athlete-management]]

## Evaluation

- Mode: `compatibility`
- Passed: `True`
- Cases: `3`
- Recorded results: `3`

## Canonical source

`skills/sport-nutrition-fueling/SKILL.md`
