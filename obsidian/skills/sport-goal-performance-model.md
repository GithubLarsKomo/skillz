---
type: skill
generated: true
name: "sport-goal-performance-model"
category: "workflow"
userFacing: true
evaluationPassed: true
evaluationMode: "compatibility"
caseCount: 3
recordedResultCount: 3
sourcePath: "skills/sport-goal-performance-model/SKILL.md"
tags:
  - skill
  - skill-category/workflow
---

# sport-goal-performance-model

Übersetzt ein sportliches Ziel in Outcome-, Performance- und Prozessziele sowie eine priorisierte KPI- und Limiter-Struktur. Verwenden vor Saison- oder Blockplanung, wenn Zieltermin, Wettkampfpriorität und messbare Leistungsanforderungen geklärt werden müssen; nicht für die konkrete Wochenprogrammierung.

> Generated from canonical repository metadata. Do not edit this note manually.

## Category

[[categories/workflow|workflow]]

## Requires

- [[skills/sport-athlete-profile|sport-athlete-profile]]

## Required by

- [[skills/sport-athlete-management|sport-athlete-management]]
- [[skills/sport-season-periodization|sport-season-periodization]]

## Outputs

- `sport-performance-model.json`

## Output consumers

### `sport-performance-model.json`

- [[skills/sport-athlete-management|sport-athlete-management]]
- [[skills/sport-season-periodization|sport-season-periodization]]

## Evaluation

- Mode: `compatibility`
- Passed: `True`
- Cases: `3`
- Recorded results: `3`

## Canonical source

`skills/sport-goal-performance-model/SKILL.md`
