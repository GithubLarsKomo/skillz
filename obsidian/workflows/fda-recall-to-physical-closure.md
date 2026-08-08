---
type: skill-workflow
generated: true
workflowId: "fda-recall-to-physical-closure"
scenarioId: "fda-recall-to-physical-closure"
sourceBenchmark: "benchmarks/regulated-engineering-field-action-physical-v1.json"
tags:
  - skill-workflow
---

# fda-recall-to-physical-closure

> Generated from an executable repository benchmark. Do not edit manually.

## Sequence

1. [[skills/fda-corrections-removals|fda-corrections-removals]]
2. [[skills/medical-device-field-action-communication|medical-device-field-action-communication]]
3. [[skills/medical-device-field-action-physical-execution|medical-device-field-action-physical-execution]]
4. [[skills/medical-device-field-action-effectiveness|medical-device-field-action-effectiveness]]
5. [[skills/medical-device-pms-system|medical-device-pms-system]]

## Must preserve

- 806-clock-not-blocked-by-execution
- recipient-action-separate-from-unit-state
- rma-not-return
- third-party-custody-evidence
- verified-correction-before-release
- product-reconciliation
- fda-termination-external

## Source

`benchmarks/regulated-engineering-field-action-physical-v1.json`
