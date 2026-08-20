---
type: skill
generated: true
name: "exam-trainer-result-import"
category: "internal"
userFacing: false
evaluationPassed: true
evaluationMode: "compatibility"
caseCount: 3
recordedResultCount: 3
sourcePath: "skills/exam-trainer-result-import/SKILL.md"
tags:
  - skill
  - skill-category/internal
---

# exam-trainer-result-import

Übersetzt den von exam-trainer-framework exportierten Vertrag `etf-teach-review-evidence` in provider-neutrale, referenzierbare Laufzeitevidenz für `learning-assessment`. Verwenden nach ETF-Lern- oder Prüfungssitzungen; bewahrt ReviewEvent-Herkunft und IDs, importiert keine Scheduler-Interna und vergibt selbst keine Kompetenzstufe.

> Generated from canonical repository metadata. Do not edit this note manually.

## Category

[[categories/internal|internal]]

## Requires

- —

## Required by

- [[skills/teach|teach]]

## Outputs

- `learning-runtime-evidence.json`

## Output consumers

### `learning-runtime-evidence.json`

- [[skills/teach|teach]]

## Evaluation

- Mode: `compatibility`
- Passed: `True`
- Cases: `3`
- Recorded results: `3`

## Canonical source

`skills/exam-trainer-result-import/SKILL.md`
