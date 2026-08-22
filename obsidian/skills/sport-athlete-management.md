---
type: skill
generated: true
name: "sport-athlete-management"
category: "workflow"
userFacing: true
evaluationPassed: true
evaluationMode: "compatibility"
caseCount: 3
recordedResultCount: 3
sourcePath: "skills/sport-athlete-management/SKILL.md"
tags:
  - skill
  - skill-category/workflow
---

# sport-athlete-management

Orchestriert den geschlossenen Sport-Trainingsregelkreis von Athletenprofil und Zielmodell über Saison-, Meso- und Mikroplanung zu Daily Monitoring, Session-Completion und auditierbarer Adaptation. Verwenden für longitudinale Trainingssteuerung über mehrere Ebenen; Fachlogik der Spezialskills nicht duplizieren.

> Generated from canonical repository metadata. Do not edit this note manually.

## Category

[[categories/workflow|workflow]]

## Requires

- [[skills/sport-athlete-profile|sport-athlete-profile]]
- [[skills/sport-daily-athlete-monitoring|sport-daily-athlete-monitoring]]
- [[skills/sport-goal-performance-model|sport-goal-performance-model]]
- [[skills/sport-mesocycle-planning|sport-mesocycle-planning]]
- [[skills/sport-microcycle-planning|sport-microcycle-planning]]
- [[skills/sport-season-periodization|sport-season-periodization]]
- [[skills/sport-training-adaptation-engine|sport-training-adaptation-engine]]

## Required by

- —

## Outputs

- `athlete-management-state.json`
- `next-training-decision.json`
- `plan-revision.json`

## Output consumers

### `athlete-management-state.json`

- Terminal or currently unconsumed output.

### `next-training-decision.json`

- Terminal or currently unconsumed output.

### `plan-revision.json`

- Terminal or currently unconsumed output.

## Evaluation

- Mode: `compatibility`
- Passed: `True`
- Cases: `3`
- Recorded results: `3`

## Canonical source

`skills/sport-athlete-management/SKILL.md`
