---
type: skill-workflow
generated: true
workflowId: "service-and-coding-to-vigilance"
scenarioId: "service-and-coding-to-vigilance"
sourceBenchmark: "benchmarks/regulated-engineering-e2e-v1.json"
tags:
  - skill-workflow
---

# service-and-coding-to-vigilance

> Generated from an executable repository benchmark. Do not edit manually.

## Sequence

1. [[skills/medical-device-customer-contact-intake|medical-device-customer-contact-intake]]
2. [[skills/medical-device-service-report-quality-routing|medical-device-service-report-quality-routing]]
3. [[skills/medical-device-complaint-handling|medical-device-complaint-handling]]
4. [[skills/medical-device-complaint-customer-followup|medical-device-complaint-customer-followup]]
5. [[skills/medical-device-adverse-event-coding|medical-device-adverse-event-coding]]
6. [[skills/medical-device-complaint-regulatory-routing|medical-device-complaint-regulatory-routing]]
7. [[skills/fda-complaint-mdr-reportability|fda-complaint-mdr-reportability]]
8. [[skills/ivdr-pms-vigilance|ivdr-pms-vigilance]]
9. [[skills/medical-device-pms-system|medical-device-pms-system]]

## Must preserve

- service-state-not-quality-closure
- pre-service-evidence-preservation
- existing-customer-followup-owner-preserved
- narrative-remains-coding-source-of-truth
- coding-release-versioning
- coding-not-causality-or-reportability
- time-critical-regulatory-bypass

## Source

`benchmarks/regulated-engineering-e2e-v1.json`
