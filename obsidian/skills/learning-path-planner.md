---
type: skill
generated: true
name: "learning-path-planner"
category: "internal"
userFacing: false
evaluationPassed: true
evaluationMode: "compatibility"
caseCount: 3
recordedResultCount: 3
sourcePath: "skills/learning-path-planner/SKILL.md"
tags:
  - skill
  - skill-category/internal
---

# learning-path-planner

Plant aus einem Course-Concept-Graph eine didaktisch begründete Modul- und Lektionenreihenfolge mit Voraussetzungen, Einstiegspunkten, optionalen Abkürzungen und Abschlusskompetenzen. Verwenden für Course Builder und Learning Paths nach Multi-Source-Synthese.

> Generated from canonical repository metadata. Do not edit this note manually.

## Category

[[categories/internal|internal]]

## Requires

- [[skills/course-concept-graph|course-concept-graph]]

## Required by

- [[skills/learning-activity-generator|learning-activity-generator]]
- [[skills/youtube-course-builder-workflow|youtube-course-builder-workflow]]

## Outputs

- `learning-path.json`

## Output consumers

### `learning-path.json`

- [[skills/learning-activity-generator|learning-activity-generator]]
- [[skills/youtube-course-builder-workflow|youtube-course-builder-workflow]]

## Evaluation

- Mode: `compatibility`
- Passed: `True`
- Cases: `3`
- Recorded results: `3`

## Canonical source

`skills/learning-path-planner/SKILL.md`
