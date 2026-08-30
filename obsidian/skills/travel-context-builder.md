---
type: skill
generated: true
name: "travel-context-builder"
category: "internal"
userFacing: false
evaluationPassed: false
evaluationMode: "compatibility"
caseCount: 3
recordedResultCount: 0
sourcePath: "skills/travel-context-builder/SKILL.md"
tags:
  - skill
  - skill-category/internal
---

# travel-context-builder

Normalisiert bestätigte Reiseanforderungen, Präferenzen, Zeitfenster, Reisende, Budget und harte Constraints in einen kanonischen Travel Context ohne fehlende Entscheidungen zu erfinden.

> Generated from canonical repository metadata. Do not edit this note manually.

## Category

[[categories/internal|internal]]

## Requires

- —

## Required by

- [[skills/travel-agency-workflow|travel-agency-workflow]]

## Outputs

- `travel-context.json`

## Output consumers

### `travel-context.json`

- [[skills/travel-agency-workflow|travel-agency-workflow]]
- [[skills/travel-availability-snapshot|travel-availability-snapshot]]
- [[skills/travel-destination-research|travel-destination-research]]
- [[skills/travel-itinerary-planner|travel-itinerary-planner]]
- [[skills/travel-option-ranking|travel-option-ranking]]
- [[skills/travel-stay-research|travel-stay-research]]
- [[skills/travel-transport-research|travel-transport-research]]

## Evaluation

- Mode: `compatibility`
- Passed: `False`
- Cases: `3`
- Recorded results: `0`

## Canonical source

`skills/travel-context-builder/SKILL.md`
