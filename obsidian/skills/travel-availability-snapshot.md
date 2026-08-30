---
type: skill
generated: true
name: "travel-availability-snapshot"
category: "internal"
userFacing: false
evaluationPassed: true
evaluationMode: "compatibility"
caseCount: 3
recordedResultCount: 3
sourcePath: "skills/travel-availability-snapshot/SKILL.md"
tags:
  - skill
  - skill-category/internal
---

# travel-availability-snapshot

Erfasst zeitgestempelte aktuelle Transport-, Unterkunfts-, Mietwagen- und Aktivitätsangebote für bekannte Travel-Kandidaten einschließlich Preis, Verfügbarkeit und buchungsrelevanter Konditionen.

> Generated from canonical repository metadata. Do not edit this note manually.

## Category

[[categories/internal|internal]]

## Requires

- —

## Required by

- [[skills/travel-agency-workflow|travel-agency-workflow]]

## Outputs

- `travel-availability-snapshot.json`
- `travel-availability-snapshot.md`

## Output consumers

### `travel-availability-snapshot.json`

- [[skills/travel-agency-workflow|travel-agency-workflow]]
- [[skills/travel-itinerary-planner|travel-itinerary-planner]]
- [[skills/travel-option-ranking|travel-option-ranking]]

### `travel-availability-snapshot.md`

- [[skills/travel-agency-workflow|travel-agency-workflow]]

## Evaluation

- Mode: `compatibility`
- Passed: `True`
- Cases: `3`
- Recorded results: `3`

## Canonical source

`skills/travel-availability-snapshot/SKILL.md`
