---
type: skill
generated: true
name: "learning-activity-generator"
category: "internal"
userFacing: false
evaluationPassed: true
evaluationMode: "compatibility"
caseCount: 3
recordedResultCount: 3
sourcePath: "skills/learning-activity-generator/SKILL.md"
tags:
  - skill
  - skill-category/internal
---

# learning-activity-generator

Erzeugt evidenzgebundene Lernaktivitäten, Übungen und Wissenchecks aus Lernzielen und Course-Concept-Graph, mit Antwortbegründung, Distraktorlogik und klarer Trennung zwischen Recall, Verständnis und Anwendung. Verwenden innerhalb des Course Builders; nicht zur psychometrischen Kalibrierung oder Zertifizierungsprüfung.

> Generated from canonical repository metadata. Do not edit this note manually.

## Category

[[categories/internal|internal]]

## Requires

- [[skills/learning-path-planner|learning-path-planner]]

## Required by

- [[skills/youtube-course-builder-workflow|youtube-course-builder-workflow]]

## Outputs

- `course-activities.json`
- `course-knowledge-checks.json`

## Output consumers

### `course-activities.json`

- [[skills/youtube-course-builder-workflow|youtube-course-builder-workflow]]

### `course-knowledge-checks.json`

- [[skills/youtube-course-builder-workflow|youtube-course-builder-workflow]]

## Evaluation

- Mode: `compatibility`
- Passed: `True`
- Cases: `3`
- Recorded results: `3`

## Canonical source

`skills/learning-activity-generator/SKILL.md`
