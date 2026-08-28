---
type: skill
generated: true
name: "sport-training-plan-workflow"
category: "workflow"
userFacing: true
evaluationPassed: true
evaluationMode: "compatibility"
caseCount: 3
recordedResultCount: 3
sourcePath: "skills/sport-training-plan-workflow/SKILL.md"
tags:
  - skill
  - skill-category/workflow
---

# sport-training-plan-workflow

Orchestriert einen einmaligen ausführbaren Trainingsplan aus Athletenprofil, Ziel-/Performance-Modell, Saison-/Meso-/Mikroplanung und den spezialisierten Kraft-/Power- und Ausdauer-Prescriptions. Verwenden für konkrete Wochen-/Blockpläne ohne longitudinalen Athlete-Management-State; Fachlogik bleibt in den spezialisierten Sport-Skills.

> Generated from canonical repository metadata. Do not edit this note manually.

## Category

[[categories/workflow|workflow]]

## Requires

- [[skills/sport-athlete-profile|sport-athlete-profile]]
- [[skills/sport-endurance-programming|sport-endurance-programming]]
- [[skills/sport-goal-performance-model|sport-goal-performance-model]]
- [[skills/sport-mesocycle-planning|sport-mesocycle-planning]]
- [[skills/sport-microcycle-planning|sport-microcycle-planning]]
- [[skills/sport-performance-diagnostics|sport-performance-diagnostics]]
- [[skills/sport-season-periodization|sport-season-periodization]]
- [[skills/sport-strength-power-programming|sport-strength-power-programming]]

## Required by

- [[skills/sport-diagnostics-training-report-workflow|sport-diagnostics-training-report-workflow]]
- [[skills/sport-training-programming|sport-training-programming]]

## Outputs

- `sport-training-plan.json`

## Output consumers

### `sport-training-plan.json`

- [[skills/sport-diagnostics-training-report-workflow|sport-diagnostics-training-report-workflow]]
- [[skills/sport-training-programming|sport-training-programming]]

## Evaluation

- Mode: `compatibility`
- Passed: `True`
- Cases: `3`
- Recorded results: `3`

## Canonical source

`skills/sport-training-plan-workflow/SKILL.md`
