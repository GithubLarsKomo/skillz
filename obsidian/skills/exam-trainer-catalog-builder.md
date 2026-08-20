---
type: skill
generated: true
name: "exam-trainer-catalog-builder"
category: "internal"
userFacing: false
evaluationPassed: true
evaluationMode: "compatibility"
caseCount: 3
recordedResultCount: 3
sourcePath: "skills/exam-trainer-catalog-builder/SKILL.md"
tags:
  - skill
  - skill-category/internal
---

# exam-trainer-catalog-builder

Übersetzt eine explizite Teach-Lernübergabe mit Lernmission, Kompetenzbezug, Assessment-Spec und belegten Inhalten in den portablen ETF-Vertrag `etf-teach-catalog` mit stabilen KnowledgeItems und QuestionVariants. Verwenden, wenn Skillz Lernmaterial an exam-trainer-framework übergeben soll; recherchiert keine Fachwahrheit, schedult nichts und erzeugt keine formale Trainingsfreigabe.

> Generated from canonical repository metadata. Do not edit this note manually.

## Category

[[categories/internal|internal]]

## Requires

- [[skills/learning-assessment-spec|learning-assessment-spec]]
- [[skills/learning-mission|learning-mission]]

## Required by

- [[skills/teach|teach]]

## Outputs

- `etf-teach-catalog.json`

## Output consumers

### `etf-teach-catalog.json`

- [[skills/teach|teach]]

## Evaluation

- Mode: `compatibility`
- Passed: `True`
- Cases: `3`
- Recorded results: `3`

## Canonical source

`skills/exam-trainer-catalog-builder/SKILL.md`
