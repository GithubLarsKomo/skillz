---
type: skill
generated: true
name: "travel-option-ranking"
category: "internal"
userFacing: false
evaluationPassed: true
evaluationMode: "compatibility"
caseCount: 3
recordedResultCount: 3
sourcePath: "skills/travel-option-ranking/SKILL.md"
tags:
  - skill
  - skill-category/internal
---

# travel-option-ranking

Bewertet Reiseoptionen deterministisch gegen bestätigte harte Constraints und Entscheidungskriterien und trennt Reisefit, Kosten, Evidenzabdeckung und Ranking-Confidence.

> Generated from canonical repository metadata. Do not edit this note manually.

## Category

[[categories/internal|internal]]

## Requires

- —

## Required by

- [[skills/travel-agency-workflow|travel-agency-workflow]]
- [[skills/travel-itinerary-planner|travel-itinerary-planner]]

## Outputs

- `travel-ranking.json`
- `travel-ranking.md`

## Output consumers

### `travel-ranking.json`

- [[skills/travel-agency-workflow|travel-agency-workflow]]
- [[skills/travel-itinerary-planner|travel-itinerary-planner]]

### `travel-ranking.md`

- [[skills/travel-agency-workflow|travel-agency-workflow]]

## Evaluation

- Mode: `compatibility`
- Passed: `True`
- Cases: `3`
- Recorded results: `3`

## Canonical source

`skills/travel-option-ranking/SKILL.md`
