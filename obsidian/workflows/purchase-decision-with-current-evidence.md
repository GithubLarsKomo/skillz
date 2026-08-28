---
type: skill-workflow
generated: true
workflowId: "purchase-decision-with-current-evidence"
scenarioId: "purchase-decision-with-current-evidence"
sourceBenchmark: "benchmarks/cross-domain-workflows-e2e-v1.json"
tags:
  - skill-workflow
---

# purchase-decision-with-current-evidence

> Generated from an executable repository benchmark. Do not edit manually.

## Sequence

1. [[skills/product-evidence-research|product-evidence-research]]
2. [[skills/price-availability-snapshot|price-availability-snapshot]]
3. [[skills/product-comparison-ranking|product-comparison-ranking]]

## Must preserve

- decision requirements and hard constraints
- separation of product evidence from current commercial availability
- transparent ranking criteria and trade-offs
- fresh price and availability snapshot when relevant

## Source

`benchmarks/cross-domain-workflows-e2e-v1.json`
