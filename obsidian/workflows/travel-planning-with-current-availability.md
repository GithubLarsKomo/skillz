---
type: skill-workflow
generated: true
workflowId: "travel-planning-with-current-availability"
scenarioId: "travel-planning-with-current-availability"
sourceBenchmark: "benchmarks/cross-domain-workflows-e2e-v1.json"
tags:
  - skill-workflow
---

# travel-planning-with-current-availability

> Generated from an executable repository benchmark. Do not edit manually.

## Sequence

1. [[skills/travel-context-builder|travel-context-builder]]
2. [[skills/travel-destination-research|travel-destination-research]]
3. [[skills/travel-transport-research|travel-transport-research]]
4. [[skills/travel-stay-research|travel-stay-research]]
5. [[skills/travel-availability-snapshot|travel-availability-snapshot]]
6. [[skills/travel-option-ranking|travel-option-ranking]]
7. [[skills/travel-itinerary-planner|travel-itinerary-planner]]

## Must preserve

- confirmed travel requirements and hard constraints across all downstream workers
- separation of relatively stable travel evidence from time-stamped current availability and prices
- hard feasibility gates before weighted option ranking
- spatial and temporal feasibility including transfers and required buffers before itinerary completion

## Source

`benchmarks/cross-domain-workflows-e2e-v1.json`
