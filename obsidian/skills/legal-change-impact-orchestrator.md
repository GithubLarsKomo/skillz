---
type: skill
generated: true
name: "legal-change-impact-orchestrator"
category: "workflow"
userFacing: true
evaluationPassed: true
evaluationMode: "compatibility"
caseCount: 3
recordedResultCount: 3
sourcePath: "skills/legal-change-impact-orchestrator/SKILL.md"
tags:
  - skill
  - skill-category/workflow
---

# legal-change-impact-orchestrator

Übersetzt verifizierte Legal-Change-Events in strukturierte Impact-Work-Orders für betroffene Rechtsträger, Prozesse, Verträge, Policies, Controls und Specialist Domains, ohne die fachliche Rechtsbewertung selbst zu übernehmen. Verbindet Legal Change Monitoring mit Obligation Register, Specialist Router und Executive Governance.

> Generated from canonical repository metadata. Do not edit this note manually.

## Category

[[categories/workflow|workflow]]

## Requires

- [[skills/compliance-obligation-register|compliance-obligation-register]]
- [[skills/legal-change-monitoring|legal-change-monitoring]]
- [[skills/legal-compliance-risk-assessment|legal-compliance-risk-assessment]]
- [[skills/legal-specialist-router|legal-specialist-router]]

## Required by

- [[skills/executive-legal-compliance-governance|executive-legal-compliance-governance]]

## Outputs

- `legal-change-decision-queue.json`
- `legal-change-impact-map.json`
- `legal-change-work-orders.json`

## Output consumers

### `legal-change-decision-queue.json`

- [[skills/executive-legal-compliance-governance|executive-legal-compliance-governance]]

### `legal-change-impact-map.json`

- [[skills/executive-legal-compliance-governance|executive-legal-compliance-governance]]

### `legal-change-work-orders.json`

- [[skills/executive-legal-compliance-governance|executive-legal-compliance-governance]]

## Evaluation

- Mode: `compatibility`
- Passed: `True`
- Cases: `3`
- Recorded results: `3`

## Canonical source

`skills/legal-change-impact-orchestrator/SKILL.md`
