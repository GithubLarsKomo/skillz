---
type: skill-workflow
generated: true
workflowId: "ivdr-field-action-through-authority-finalization"
scenarioId: "ivdr-field-action-through-authority-finalization"
sourceBenchmark: "benchmarks/regulated-engineering-field-action-authority-finalization-v1.json"
tags:
  - skill-workflow
---

# ivdr-field-action-through-authority-finalization

> Generated from an executable repository benchmark. Do not edit manually.

## Sequence

1. [[skills/ivdr-pms-vigilance|ivdr-pms-vigilance]]
2. [[skills/ivdr-field-safety-corrective-action|ivdr-field-safety-corrective-action]]
3. [[skills/medical-device-field-action-communication|medical-device-field-action-communication]]
4. [[skills/medical-device-field-action-physical-execution|medical-device-field-action-physical-execution]]
5. [[skills/medical-device-field-action-effectiveness|medical-device-field-action-effectiveness]]
6. [[skills/ivdr-fsca-status-final-reporting|ivdr-fsca-status-final-reporting]]
7. [[skills/medical-device-pms-system|medical-device-pms-system]]

## Must preserve

- current form and authority context are verified before manufacturer final reporting
- manufacturer final report submission is distinct from competent-authority receipt review assessment and closure
- unresolved causal evidence cannot be hidden by a Final Non-reportable shortcut
- new safety facts or scope drift supersede finalization readiness and immediately reopen vigilance FSCA risk and CAPA paths
- notified-body state remains distinct from competent-authority state
- authority silence never becomes acceptance

## Source

`benchmarks/regulated-engineering-field-action-authority-finalization-v1.json`
