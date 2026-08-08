---
type: skill-workflow
generated: true
workflowId: "ivdr-vigilance-to-fsca-closure"
scenarioId: "ivdr-vigilance-to-fsca-closure"
sourceBenchmark: "benchmarks/regulated-engineering-e2e-v1.json"
tags:
  - skill-workflow
---

# ivdr-vigilance-to-fsca-closure

> Generated from an executable repository benchmark. Do not edit manually.

## Sequence

1. [[skills/ivdr-pms-vigilance|ivdr-pms-vigilance]]
2. [[skills/ivdr-field-safety-corrective-action|ivdr-field-safety-corrective-action]]
3. [[skills/medical-device-field-action-communication|medical-device-field-action-communication]]
4. [[skills/medical-device-field-action-effectiveness|medical-device-field-action-effectiveness]]
5. [[skills/medical-device-pms-system|medical-device-pms-system]]

## Must preserve

- incident-reportability-separate-from-fsca
- urgent-safety-action-nonblocking
- fsca-scope-versioning
- fsn-risk-meaning-preserved
- recipient-scope-from-distribution-evidence
- sent-delivered-acknowledged-action-separated
- downstream-distribution-reconciled
- effectiveness-has-versioned-denominator
- capa-effectiveness-separate
- authority-closure-not-simulated
- new-safety-facts-reopen

## Source

`benchmarks/regulated-engineering-e2e-v1.json`
