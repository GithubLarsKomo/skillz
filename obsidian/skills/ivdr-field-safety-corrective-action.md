---
type: skill
generated: true
name: "ivdr-field-safety-corrective-action"
category: "regulated-engineering"
userFacing: true
evaluationPassed: true
evaluationMode: "compatibility"
caseCount: 4
recordedResultCount: 4
sourcePath: "skills/ivdr-field-safety-corrective-action/SKILL.md"
tags:
  - skill
  - skill-category/regulated-engineering
---

# ivdr-field-safety-corrective-action

Überführt eine IVDR-Vigilance-/Field-Action-Frage in eine evidenzgebundene FSCA-Entscheidung, behördliche Sequenz, Field-Safety-Notice-Anforderungen und kontrollierte Execution-Handoffs, ohne Authority- oder Customer-Aktionen zu simulieren.

> Generated from canonical repository metadata. Do not edit this note manually.

## Category

[[categories/regulated-engineering|regulated-engineering]]

## Requires

- [[skills/controlled-quality-documentation|controlled-quality-documentation]]
- [[skills/ivdr-pms-vigilance|ivdr-pms-vigilance]]
- [[skills/mdcg-guidance-navigator|mdcg-guidance-navigator]]
- [[skills/medical-device-capa|medical-device-capa]]
- [[skills/medical-device-risk-management-iso14971|medical-device-risk-management-iso14971]]
- [[skills/regulatory-evidence-traceability|regulatory-evidence-traceability]]

## Required by

- [[skills/ivdr-fsca-status-final-reporting|ivdr-fsca-status-final-reporting]]

## Outputs

- `field-safety-notice-content.json`
- `ivdr-fsca-assessment.json`
- `ivdr-fsca-regulatory-plan.json`

## Output consumers

### `field-safety-notice-content.json`

- [[skills/ivdr-fsca-status-final-reporting|ivdr-fsca-status-final-reporting]]

### `ivdr-fsca-assessment.json`

- [[skills/ivdr-fsca-status-final-reporting|ivdr-fsca-status-final-reporting]]

### `ivdr-fsca-regulatory-plan.json`

- [[skills/ivdr-fsca-status-final-reporting|ivdr-fsca-status-final-reporting]]

## Evaluation

- Mode: `compatibility`
- Passed: `True`
- Cases: `4`
- Recorded results: `4`

## Canonical source

`skills/ivdr-field-safety-corrective-action/SKILL.md`
