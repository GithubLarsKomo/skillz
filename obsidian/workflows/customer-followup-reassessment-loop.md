---
type: skill-workflow
generated: true
workflowId: "customer-followup-reassessment-loop"
scenarioId: "customer-followup-reassessment-loop"
sourceBenchmark: "benchmarks/regulated-engineering-e2e-v1.json"
tags:
  - skill-workflow
---

# customer-followup-reassessment-loop

> Generated from an executable repository benchmark. Do not edit manually.

## Sequence

1. [[skills/medical-device-customer-contact-intake|medical-device-customer-contact-intake]]
2. [[skills/medical-device-complaint-handling|medical-device-complaint-handling]]
3. [[skills/medical-device-complaint-regulatory-routing|medical-device-complaint-regulatory-routing]]
4. [[skills/fda-complaint-mdr-reportability|fda-complaint-mdr-reportability]]
5. [[skills/ivdr-pms-vigilance|ivdr-pms-vigilance]]
6. [[skills/medical-device-pms-system|medical-device-pms-system]]

## Must preserve

- followup-as-new-evidence-event
- historical-contact-and-closure-state
- complaint-reopen-state
- prior-assessment-versioning
- independent-jurisdiction-reassessment
- new-evidence-not-immunity
- time-critical-reassessment
- updated-pms-feedback

## Source

`benchmarks/regulated-engineering-e2e-v1.json`
