---
type: skill-workflow
generated: true
workflowId: "fda-correction-removal-to-recall-closure"
scenarioId: "fda-correction-removal-to-recall-closure"
sourceBenchmark: "benchmarks/regulated-engineering-e2e-v1.json"
tags:
  - skill-workflow
---

# fda-correction-removal-to-recall-closure

> Generated from an executable repository benchmark. Do not edit manually.

## Sequence

1. [[skills/fda-corrections-removals|fda-corrections-removals]]
2. [[skills/medical-device-field-action-communication|medical-device-field-action-communication]]
3. [[skills/medical-device-field-action-effectiveness|medical-device-field-action-effectiveness]]
4. [[skills/medical-device-pms-system|medical-device-pms-system]]

## Must preserve

- 806-reportability-separate-from-recall-classification
- 806-clock-not-blocked-by-execution
- recipient-scope-from-distribution-evidence
- communication-evidence-state-separation
- strategy-governs-effectiveness-check
- nonresponders-remain-in-scope
- product-reconciliation
- internal-completion-not-fda-termination
- new-safety-facts-reopen

## Source

`benchmarks/regulated-engineering-e2e-v1.json`
