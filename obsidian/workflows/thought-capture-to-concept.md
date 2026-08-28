---
type: skill-workflow
generated: true
workflowId: "thought-capture-to-concept"
scenarioId: "thought-capture-to-concept"
sourceBenchmark: "benchmarks/cross-domain-workflows-e2e-v1.json"
tags:
  - skill-workflow
---

# thought-capture-to-concept

> Generated from an executable repository benchmark. Do not edit manually.

## Sequence

1. [[skills/round-based-requirements-grilling|round-based-requirements-grilling]]
2. [[skills/thought-capture-journal|thought-capture-journal]]
3. [[skills/thought-graph-extractor|thought-graph-extractor]]
4. [[skills/knowledge-map-generator|knowledge-map-generator]]

## Must preserve

- confirmed goal frame before final concept structure
- raw thought capture before premature categorization
- semantic links between goals ideas risks questions and actions
- traceability from concept structure back to captured thoughts

## Source

`benchmarks/cross-domain-workflows-e2e-v1.json`
