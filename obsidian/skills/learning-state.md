---
type: skill
generated: true
name: "learning-state"
category: "internal"
userFacing: false
evaluationPassed: true
evaluationMode: "compatibility"
caseCount: 3
recordedResultCount: 3
sourcePath: "skills/learning-state/SKILL.md"
tags:
  - skill
  - skill-category/internal
---

# learning-state

Pflegt einen portablen semantischen Lernzustand aus nachgewiesenen Kompetenzen, relevantem Vorwissen, Fehlvorstellungen, Lücken und kurzen Learning Records. Verwenden, wenn Lern- oder Prüfungsevidenz in dauerhaften Kompetenzzustand überführt oder ein bestehender Zustand nachvollziehbar revidiert werden soll; nicht als Roh-Eventlog oder Scheduler.

> Generated from canonical repository metadata. Do not edit this note manually.

## Category

[[categories/internal|internal]]

## Requires

- —

## Required by

- [[skills/learning-assessment-spec|learning-assessment-spec]]
- [[skills/learning-next-step|learning-next-step]]
- [[skills/teach|teach]]

## Outputs

- `learning-record.md`
- `learning-state.json`

## Output consumers

### `learning-record.md`

- [[skills/learning-assessment-spec|learning-assessment-spec]]
- [[skills/learning-next-step|learning-next-step]]
- [[skills/teach|teach]]

### `learning-state.json`

- [[skills/learning-assessment-spec|learning-assessment-spec]]
- [[skills/learning-next-step|learning-next-step]]
- [[skills/teach|teach]]

## Evaluation

- Mode: `compatibility`
- Passed: `True`
- Cases: `3`
- Recorded results: `3`

## Canonical source

`skills/learning-state/SKILL.md`
