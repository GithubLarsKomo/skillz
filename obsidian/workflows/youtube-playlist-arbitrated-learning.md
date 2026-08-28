---
type: skill-workflow
generated: true
workflowId: "youtube-playlist-arbitrated-learning"
scenarioId: "youtube-playlist-arbitrated-learning"
sourceBenchmark: "benchmarks/cross-domain-workflows-e2e-v1.json"
tags:
  - skill-workflow
---

# youtube-playlist-arbitrated-learning

> Generated from an executable repository benchmark. Do not edit manually.

## Sequence

1. [[skills/youtube-learning-workflow|youtube-learning-workflow]]
2. [[skills/learning-source-arbitration|learning-source-arbitration]]
3. [[skills/multi-source-learning-synthesis|multi-source-learning-synthesis]]
4. [[skills/learning-delivery-workflow|learning-delivery-workflow]]

## Must preserve

- individual source analysis before synthesis
- source independence and authority rather than majority vote
- explicit unresolved material conflicts
- single multi-source model for all delivered formats

## Source

`benchmarks/cross-domain-workflows-e2e-v1.json`
