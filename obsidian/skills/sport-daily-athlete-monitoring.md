---
type: skill
generated: true
name: "sport-daily-athlete-monitoring"
category: "workflow"
userFacing: true
evaluationPassed: true
evaluationMode: "compatibility"
caseCount: 3
recordedResultCount: 3
sourcePath: "skills/sport-daily-athlete-monitoring/SKILL.md"
tags:
  - skill
  - skill-category/workflow
---

# sport-daily-athlete-monitoring

Erfasst einen kurzen Morning-Check, passive Wearable-/Biometrie-Kontexte und die tatsächliche Post-Session-Reaktion einschließlich sRPE, Schlaf, Müdigkeit, Muskelkater, Stress, Motivation, Schmerz und Krankheitssymptomen. Verwenden für tägliches longitudinales Monitoring; Wearable- oder Vendor-Scores nie als alleinigen Readiness-Regler oder medizinische Diagnose verwenden.

> Generated from canonical repository metadata. Do not edit this note manually.

## Category

[[categories/workflow|workflow]]

## Requires

- [[skills/sport-athlete-profile|sport-athlete-profile]]

## Required by

- [[skills/sport-adaptation-analysis|sport-adaptation-analysis]]
- [[skills/sport-athlete-management|sport-athlete-management]]
- [[skills/sport-injury-rehabilitation|sport-injury-rehabilitation]]
- [[skills/sport-mental-health-routing|sport-mental-health-routing]]
- [[skills/sport-nutrition-fueling|sport-nutrition-fueling]]
- [[skills/sport-recovery-sleep|sport-recovery-sleep]]
- [[skills/sport-return-after-illness|sport-return-after-illness]]
- [[skills/sport-training-adaptation-engine|sport-training-adaptation-engine]]

## Outputs

- `completed-session.json`
- `daily-checkin.json`

## Output consumers

### `completed-session.json`

- [[skills/sport-adaptation-analysis|sport-adaptation-analysis]]
- [[skills/sport-athlete-management|sport-athlete-management]]
- [[skills/sport-injury-rehabilitation|sport-injury-rehabilitation]]
- [[skills/sport-mental-health-routing|sport-mental-health-routing]]
- [[skills/sport-nutrition-fueling|sport-nutrition-fueling]]
- [[skills/sport-recovery-sleep|sport-recovery-sleep]]
- [[skills/sport-return-after-illness|sport-return-after-illness]]
- [[skills/sport-training-adaptation-engine|sport-training-adaptation-engine]]

### `daily-checkin.json`

- [[skills/sport-adaptation-analysis|sport-adaptation-analysis]]
- [[skills/sport-athlete-management|sport-athlete-management]]
- [[skills/sport-injury-rehabilitation|sport-injury-rehabilitation]]
- [[skills/sport-mental-health-routing|sport-mental-health-routing]]
- [[skills/sport-nutrition-fueling|sport-nutrition-fueling]]
- [[skills/sport-recovery-sleep|sport-recovery-sleep]]
- [[skills/sport-return-after-illness|sport-return-after-illness]]
- [[skills/sport-training-adaptation-engine|sport-training-adaptation-engine]]

## Evaluation

- Mode: `compatibility`
- Passed: `True`
- Cases: `3`
- Recorded results: `3`

## Canonical source

`skills/sport-daily-athlete-monitoring/SKILL.md`
