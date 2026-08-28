---
type: skill-workflow
generated: true
workflowId: "youtube-course-builder"
scenarioId: "youtube-course-builder"
sourceBenchmark: "benchmarks/cross-domain-workflows-e2e-v1.json"
tags:
  - skill-workflow
---

# youtube-course-builder

> Generated from an executable repository benchmark. Do not edit manually.

## Sequence

1. [[skills/youtube-playlist-learning-workflow|youtube-playlist-learning-workflow]]
2. [[skills/course-concept-graph|course-concept-graph]]
3. [[skills/learning-path-planner|learning-path-planner]]
4. [[skills/learning-activity-generator|learning-activity-generator]]
5. [[skills/learning-delivery-workflow|learning-delivery-workflow]]

## Must preserve

- acyclic prerequisite graph based on learning dependency rather than playlist order
- observable objectives and exit criteria
- evidence-linked formative activities
- same course fingerprint across requested formats

## Source

`benchmarks/cross-domain-workflows-e2e-v1.json`
