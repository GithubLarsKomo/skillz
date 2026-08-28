---
type: skill
generated: true
name: "course-concept-graph"
category: "internal"
userFacing: false
evaluationPassed: true
evaluationMode: "compatibility"
caseCount: 3
recordedResultCount: 3
sourcePath: "skills/course-concept-graph/SKILL.md"
tags:
  - skill
  - skill-category/internal
---

# course-concept-graph

Baut aus einem evidenzgebundenen Multi-Source-Learning-Modell einen gerichteten Begriffs- und Voraussetzungsgrafen für Kursaufbau, Modulgrenzen und Lernreihenfolge. Verwenden vor automatischer Learning-Path-Planung; nicht zur inhaltlichen Erfindung fehlender Voraussetzungen.

> Generated from canonical repository metadata. Do not edit this note manually.

## Category

[[categories/internal|internal]]

## Requires

- [[skills/multi-source-learning-synthesis|multi-source-learning-synthesis]]

## Required by

- [[skills/learning-path-planner|learning-path-planner]]
- [[skills/youtube-course-builder-workflow|youtube-course-builder-workflow]]

## Outputs

- `course-concept-graph.json`

## Output consumers

### `course-concept-graph.json`

- [[skills/learning-path-planner|learning-path-planner]]
- [[skills/youtube-course-builder-workflow|youtube-course-builder-workflow]]

## Evaluation

- Mode: `compatibility`
- Passed: `True`
- Cases: `3`
- Recorded results: `3`

## Canonical source

`skills/course-concept-graph/SKILL.md`
