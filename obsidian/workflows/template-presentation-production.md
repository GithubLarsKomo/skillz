---
type: skill-workflow
generated: true
workflowId: "template-presentation-production"
scenarioId: "template-presentation-production"
sourceBenchmark: "benchmarks/cross-domain-workflows-e2e-v1.json"
tags:
  - skill-workflow
---

# template-presentation-production

> Generated from an executable repository benchmark. Do not edit manually.

## Sequence

1. [[skills/presentation-template-profiler|presentation-template-profiler]]
2. [[skills/presentation-language-rewriter|presentation-language-rewriter]]
3. [[skills/presentation-layout-qa|presentation-layout-qa]]
4. [[skills/presentation-render-verifier|presentation-render-verifier]]

## Must preserve

- template or reference authority
- semantic fidelity during language rewriting
- structural layout checks separated from visual render checks
- editable PPTX and derived PDF parity

## Source

`benchmarks/cross-domain-workflows-e2e-v1.json`
