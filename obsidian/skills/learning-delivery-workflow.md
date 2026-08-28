---
type: skill
generated: true
name: "learning-delivery-workflow"
category: "internal"
userFacing: false
evaluationPassed: true
evaluationMode: "compatibility"
caseCount: 3
recordedResultCount: 3
sourcePath: "skills/learning-delivery-workflow/SKILL.md"
tags:
  - skill
  - skill-category/internal
---

# learning-delivery-workflow

Orchestriert die formatübergreifende Auslieferung eines bereits kanonischen Learning-Content-, Multi-Source- oder Course-Modells über DESIGN.md, Visualplanung, SVG/Bild-Assets, Landingpage, Präsentation, DOCX/PDF und finales Cross-Format-QA, ohne fachliche Learning-Semantik neu zu autorieren. Verwenden als interne gemeinsame Delivery-Schicht für Learning-Orchestratoren.

> Generated from canonical repository metadata. Do not edit this note manually.

## Category

[[categories/internal|internal]]

## Requires

- [[skills/learning-artifact-qa|learning-artifact-qa]]
- [[skills/learning-content-design-system|learning-content-design-system]]
- [[skills/learning-document-delivery|learning-document-delivery]]
- [[skills/learning-image-generator|learning-image-generator]]
- [[skills/learning-landingpage-renderer|learning-landingpage-renderer]]
- [[skills/learning-svg-generator|learning-svg-generator]]
- [[skills/learning-visual-planner|learning-visual-planner]]
- [[skills/template-presentation-workflow|template-presentation-workflow]]

## Required by

- [[skills/youtube-course-builder-workflow|youtube-course-builder-workflow]]
- [[skills/youtube-learning-workflow|youtube-learning-workflow]]
- [[skills/youtube-playlist-learning-workflow|youtube-playlist-learning-workflow]]

## Outputs

- `learning-delivery-bundle.json`
- `learning-delivery-run.json`

## Output consumers

### `learning-delivery-bundle.json`

- [[skills/youtube-course-builder-workflow|youtube-course-builder-workflow]]
- [[skills/youtube-learning-workflow|youtube-learning-workflow]]
- [[skills/youtube-playlist-learning-workflow|youtube-playlist-learning-workflow]]

### `learning-delivery-run.json`

- [[skills/youtube-course-builder-workflow|youtube-course-builder-workflow]]
- [[skills/youtube-learning-workflow|youtube-learning-workflow]]
- [[skills/youtube-playlist-learning-workflow|youtube-playlist-learning-workflow]]

## Evaluation

- Mode: `compatibility`
- Passed: `True`
- Cases: `3`
- Recorded results: `3`

## Canonical source

`skills/learning-delivery-workflow/SKILL.md`
