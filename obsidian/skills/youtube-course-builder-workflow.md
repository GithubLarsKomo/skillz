---
type: skill
generated: true
name: "youtube-course-builder-workflow"
category: "workflow"
userFacing: true
evaluationPassed: true
evaluationMode: "compatibility"
caseCount: 3
recordedResultCount: 3
sourcePath: "skills/youtube-course-builder-workflow/SKILL.md"
tags:
  - skill
  - skill-category/workflow
---

# youtube-course-builder-workflow

Baut aus mehreren YouTube-Videos oder einem Multi-Source-Learning-Modell einen modularen Learning Path mit Voraussetzungen, Lernzielen, Übungen, Wissenchecks und konsistenten Kursartefakten in HTML/PPTX/DOCX/PDF. Verwenden für Course Builder, Curriculum aus Videoquellen oder strukturierte Learning Paths; nicht als psychometrisch validierte Prüfung oder automatische Zertifizierung.

> Generated from canonical repository metadata. Do not edit this note manually.

## Category

[[categories/workflow|workflow]]

## Requires

- [[skills/course-concept-graph|course-concept-graph]]
- [[skills/learning-activity-generator|learning-activity-generator]]
- [[skills/learning-delivery-workflow|learning-delivery-workflow]]
- [[skills/learning-path-planner|learning-path-planner]]
- [[skills/youtube-playlist-learning-workflow|youtube-playlist-learning-workflow]]

## Required by

- —

## Outputs

- `course-learning-model.json`
- `youtube-course-builder-run.json`

## Output consumers

### `course-learning-model.json`

- [[skills/learning-delivery-workflow|learning-delivery-workflow]]

### `youtube-course-builder-run.json`

- Terminal or currently unconsumed output.

## Evaluation

- Mode: `compatibility`
- Passed: `True`
- Cases: `3`
- Recorded results: `3`

## Canonical source

`skills/youtube-course-builder-workflow/SKILL.md`
