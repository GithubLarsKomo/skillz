---
type: skill
generated: true
name: "travel-itinerary-planner"
category: "internal"
userFacing: false
evaluationPassed: true
evaluationMode: "compatibility"
caseCount: 3
recordedResultCount: 3
sourcePath: "skills/travel-itinerary-planner/SKILL.md"
tags:
  - skill
  - skill-category/internal
---

# travel-itinerary-planner

Verwandelt ausgewählte oder gerankte Reiseoptionen in einen zeitlich und räumlich konsistenten Reiseplan mit Transfers, Öffnungszeiten, Reservierungsfenstern, Puffern und expliziten Unsicherheiten.

> Generated from canonical repository metadata. Do not edit this note manually.

## Category

[[categories/internal|internal]]

## Requires

- [[skills/travel-option-ranking|travel-option-ranking]]

## Required by

- [[skills/travel-agency-workflow|travel-agency-workflow]]

## Outputs

- `travel-itinerary.json`
- `travel-itinerary.md`

## Output consumers

### `travel-itinerary.json`

- [[skills/travel-agency-workflow|travel-agency-workflow]]

### `travel-itinerary.md`

- [[skills/travel-agency-workflow|travel-agency-workflow]]

## Evaluation

- Mode: `compatibility`
- Passed: `True`
- Cases: `3`
- Recorded results: `3`

## Canonical source

`skills/travel-itinerary-planner/SKILL.md`
