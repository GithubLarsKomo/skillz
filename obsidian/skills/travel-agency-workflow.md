---
type: skill
generated: true
name: "travel-agency-workflow"
category: "workflow"
userFacing: true
evaluationPassed: true
evaluationMode: "compatibility"
caseCount: 3
recordedResultCount: 3
sourcePath: "skills/travel-agency-workflow/SKILL.md"
tags:
  - skill
  - skill-category/workflow
---

# travel-agency-workflow

Orchestriert private Reisen von geklärten Anforderungen über Ziel-, Transport- und Unterkunftsrecherche sowie aktuelle Verfügbarkeit bis zu Ranking und zeitlich-räumlich geprüftem Reiseplan.

> Generated from canonical repository metadata. Do not edit this note manually.

## Category

[[categories/workflow|workflow]]

## Requires

- [[skills/travel-availability-snapshot|travel-availability-snapshot]]
- [[skills/travel-context-builder|travel-context-builder]]
- [[skills/travel-destination-research|travel-destination-research]]
- [[skills/travel-itinerary-planner|travel-itinerary-planner]]
- [[skills/travel-option-ranking|travel-option-ranking]]
- [[skills/travel-stay-research|travel-stay-research]]
- [[skills/travel-transport-research|travel-transport-research]]

## Required by

- —

## Outputs

- `travel-plan.json`
- `travel-plan.md`
- `travel-shortlist.json`

## Output consumers

### `travel-plan.json`

- Terminal or currently unconsumed output.

### `travel-plan.md`

- Terminal or currently unconsumed output.

### `travel-shortlist.json`

- Terminal or currently unconsumed output.

## Evaluation

- Mode: `compatibility`
- Passed: `True`
- Cases: `3`
- Recorded results: `3`

## Canonical source

`skills/travel-agency-workflow/SKILL.md`
