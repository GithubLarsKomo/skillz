---
type: skill-workflow
generated: true
workflowId: "fda-recall-through-termination"
scenarioId: "fda-recall-through-termination"
sourceBenchmark: "benchmarks/regulated-engineering-field-action-authority-finalization-v1.json"
tags:
  - skill-workflow
---

# fda-recall-through-termination

> Generated from an executable repository benchmark. Do not edit manually.

## Sequence

1. [[skills/fda-corrections-removals|fda-corrections-removals]]
2. [[skills/medical-device-field-action-communication|medical-device-field-action-communication]]
3. [[skills/medical-device-field-action-physical-execution|medical-device-field-action-physical-execution]]
4. [[skills/medical-device-field-action-effectiveness|medical-device-field-action-effectiveness]]
5. [[skills/fda-recall-status-termination|fda-recall-status-termination]]
6. [[skills/medical-device-pms-system|medical-device-pms-system]]

## Must preserve

- recall-specific FDA reporting cadence overrides generic planning intervals
- status reports preserve nonresponders unknown products effectiveness results and versioned scope
- firm completed termination requested and FDA terminated are distinct states
- FDA termination requires verified FDA evidence
- scope extensions can trigger Part 806 amendment reassessment instead of being buried in status reporting
- new safety facts bypass termination readiness

## Source

`benchmarks/regulated-engineering-field-action-authority-finalization-v1.json`
