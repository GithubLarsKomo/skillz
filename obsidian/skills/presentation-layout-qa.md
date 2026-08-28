---
type: skill
generated: true
name: "presentation-layout-qa"
category: "workflow"
userFacing: true
evaluationPassed: true
evaluationMode: "compatibility"
caseCount: 3
recordedResultCount: 3
sourcePath: "skills/presentation-layout-qa/SKILL.md"
tags:
  - skill
  - skill-category/workflow
---

# presentation-layout-qa

Prüft PowerPoint-Folien strukturell auf Text- und Box-Overflow, Objektüberlagerungen, Slide-Grenzen, Font-Ausreißer, inkonsistente Ausrichtung, Platzhaltermissbrauch, Bildverzerrung, Chart-/Tabellen-Clipping und Footer-Kollisionen. Verwenden als technische QA vor finalem Rendering; nicht als visuelle Geschmacksprüfung.

> Generated from canonical repository metadata. Do not edit this note manually.

## Category

[[categories/workflow|workflow]]

## Requires

- [[skills/presentation-template-profiler|presentation-template-profiler]]

## Required by

- [[skills/presentation-render-verifier|presentation-render-verifier]]
- [[skills/template-presentation-workflow|template-presentation-workflow]]

## Outputs

- `presentation-layout-qa.json`
- `presentation-layout-qa.md`

## Output consumers

### `presentation-layout-qa.json`

- [[skills/presentation-render-verifier|presentation-render-verifier]]
- [[skills/template-presentation-workflow|template-presentation-workflow]]

### `presentation-layout-qa.md`

- [[skills/presentation-render-verifier|presentation-render-verifier]]
- [[skills/template-presentation-workflow|template-presentation-workflow]]

## Evaluation

- Mode: `compatibility`
- Passed: `True`
- Cases: `3`
- Recorded results: `3`

## Canonical source

`skills/presentation-layout-qa/SKILL.md`
