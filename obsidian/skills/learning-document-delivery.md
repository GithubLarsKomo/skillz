---
type: skill
generated: true
name: "learning-document-delivery"
category: "workflow"
userFacing: true
evaluationPassed: true
evaluationMode: "compatibility"
caseCount: 3
recordedResultCount: 3
sourcePath: "skills/learning-document-delivery/SKILL.md"
tags:
  - skill
  - skill-category/workflow
---

# learning-document-delivery

Überführt ein kanonisches Learning-Content-Modell und seine Visuals DESIGN.md-konform in ein editierbares Lern-DOCX und daraus in ein geprüftes PDF, mit Corporate-Renderer-Routing wenn ein verbindlicher Firmenkontext vorliegt. Verwenden für Lernhandouts, SOP-Drafts und Video-Study-Guides; nicht zum inhaltlichen Re-Authoring beim Rendering.

> Generated from canonical repository metadata. Do not edit this note manually.

## Category

[[categories/workflow|workflow]]

## Requires

- [[skills/learning-content-design-system|learning-content-design-system]]

## Required by

- [[skills/learning-delivery-workflow|learning-delivery-workflow]]

## Outputs

- `learning-document-qa.json`
- `learning-handout.docx`
- `learning-handout.pdf`

## Output consumers

### `learning-document-qa.json`

- [[skills/learning-delivery-workflow|learning-delivery-workflow]]

### `learning-handout.docx`

- [[skills/learning-delivery-workflow|learning-delivery-workflow]]

### `learning-handout.pdf`

- [[skills/learning-delivery-workflow|learning-delivery-workflow]]

## Evaluation

- Mode: `compatibility`
- Passed: `True`
- Cases: `3`
- Recorded results: `3`

## Canonical source

`skills/learning-document-delivery/SKILL.md`
