---
type: skill-workflow
generated: true
workflowId: "customer-contact-to-dual-market-vigilance"
scenarioId: "customer-contact-to-dual-market-vigilance"
sourceBenchmark: "benchmarks/regulated-engineering-e2e-v1.json"
tags:
  - skill-workflow
---

# customer-contact-to-dual-market-vigilance

> Generated from an executable repository benchmark. Do not edit manually.

## Sequence

1. [[skills/medical-device-customer-contact-intake|medical-device-customer-contact-intake]]
2. [[skills/medical-device-complaint-handling|medical-device-complaint-handling]]
3. [[skills/medical-device-complaint-regulatory-routing|medical-device-complaint-regulatory-routing]]
4. [[skills/fda-complaint-mdr-reportability|fda-complaint-mdr-reportability]]
5. [[skills/ivdr-pms-vigilance|ivdr-pms-vigilance]]
6. [[skills/medical-device-pms-system|medical-device-pms-system]]

## Must preserve

- original-contact-voice
- immutable-receipt-chronology
- individual-complaint-record
- investigation-decision-evidence
- evidence-preservation
- awareness-provenance
- separate-jurisdiction-decisions
- time-critical-escalation
- complaint-closure-not-regulatory-closure

## Source

`benchmarks/regulated-engineering-e2e-v1.json`
