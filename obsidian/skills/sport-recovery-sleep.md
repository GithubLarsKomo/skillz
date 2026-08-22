---
type: skill
generated: true
name: "sport-recovery-sleep"
category: "analysis"
userFacing: true
evaluationPassed: true
evaluationMode: "compatibility"
caseCount: 3
recordedResultCount: 3
sourcePath: "skills/sport-recovery-sleep/SKILL.md"
tags:
  - skill
  - skill-category/analysis
---

# sport-recovery-sleep

Interpretiert Schlaf, Ermüdung und Erholung longitudinal gegen die individuelle Baseline und leitet konkrete Recovery-Optionen ab. Verwenden bei kumulierter Müdigkeit, Schlafproblemen, Reise oder Wettkampfbelastung; keinen opaken Readiness-Score und keine HRV-Alleinsteuerung erzeugen.

> Generated from canonical repository metadata. Do not edit this note manually.

## Category

[[categories/analysis|analysis]]

## Requires

- [[skills/sport-athlete-profile|sport-athlete-profile]]
- [[skills/sport-daily-athlete-monitoring|sport-daily-athlete-monitoring]]

## Required by

- [[skills/sport-athlete-management|sport-athlete-management]]
- [[skills/sport-environment-travel|sport-environment-travel]]

## Outputs

- `recovery-state.json`

## Output consumers

### `recovery-state.json`

- [[skills/sport-athlete-management|sport-athlete-management]]
- [[skills/sport-environment-travel|sport-environment-travel]]

## Evaluation

- Mode: `compatibility`
- Passed: `True`
- Cases: `3`
- Recorded results: `3`

## Canonical source

`skills/sport-recovery-sleep/SKILL.md`
