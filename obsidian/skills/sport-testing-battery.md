---
type: skill
generated: true
name: "sport-testing-battery"
category: "workflow"
userFacing: true
evaluationPassed: true
evaluationMode: "compatibility"
caseCount: 3
recordedResultCount: 3
sourcePath: "skills/sport-testing-battery/SKILL.md"
tags:
  - skill
  - skill-category/workflow
---

# sport-testing-battery

Wählt eine minimale, sport- und zielbezogene Leistungsdiagnostik-Batterie aus und legt Protokoll, Zeitpunkt, Wiederholbarkeit und Entscheidungsnutzen fest. Verwenden zur Testplanung über Saisonphasen; nicht für unnötige Maximaltests kurz vor Wettkämpfen oder medizinische Diagnostik.

> Generated from canonical repository metadata. Do not edit this note manually.

## Category

[[categories/workflow|workflow]]

## Requires

- [[skills/sport-athlete-profile|sport-athlete-profile]]
- [[skills/sport-goal-performance-model|sport-goal-performance-model]]
- [[skills/sport-season-periodization|sport-season-periodization]]

## Required by

- [[skills/sport-athlete-management|sport-athlete-management]]

## Outputs

- `sport-testing-plan.json`

## Output consumers

### `sport-testing-plan.json`

- [[skills/sport-athlete-management|sport-athlete-management]]

## Evaluation

- Mode: `compatibility`
- Passed: `True`
- Cases: `3`
- Recorded results: `3`

## Canonical source

`skills/sport-testing-battery/SKILL.md`
