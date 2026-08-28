---
type: skill
generated: true
name: "learning-visual-planner"
category: "internal"
userFacing: false
evaluationPassed: true
evaluationMode: "compatibility"
caseCount: 3
recordedResultCount: 3
sourcePath: "skills/learning-visual-planner/SKILL.md"
tags:
  - skill
  - skill-category/internal
---

# learning-visual-planner

Plant für evidenzgebundene Lerninhalte die jeweils informationsstärkste Visualisierung und entscheidet zwischen Quellframe, Diagramm/SVG, Chart, annotiertem Screenshot oder generierter Illustration. Verwenden vor Grafik- oder Bilderzeugung; nicht zum Erzeugen dekorativer Assets oder zum Verändern fachlicher Claims.

> Generated from canonical repository metadata. Do not edit this note manually.

## Category

[[categories/internal|internal]]

## Requires

- [[skills/multimodal-learning-analysis|multimodal-learning-analysis]]

## Required by

- [[skills/learning-delivery-workflow|learning-delivery-workflow]]
- [[skills/learning-image-generator|learning-image-generator]]
- [[skills/learning-svg-generator|learning-svg-generator]]

## Outputs

- `learning-visual-plan.json`

## Output consumers

### `learning-visual-plan.json`

- [[skills/learning-delivery-workflow|learning-delivery-workflow]]
- [[skills/learning-image-generator|learning-image-generator]]
- [[skills/learning-svg-generator|learning-svg-generator]]

## Evaluation

- Mode: `compatibility`
- Passed: `True`
- Cases: `3`
- Recorded results: `3`

## Canonical source

`skills/learning-visual-planner/SKILL.md`
