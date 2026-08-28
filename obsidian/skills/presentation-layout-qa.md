---
type: skill
generated: true
name: "presentation-layout-qa"
category: "workflow"
userFacing: true
evaluationPassed: null
evaluationMode: "none"
caseCount: 0
recordedResultCount: 0
sourcePath: "skills/presentation-layout-qa/SKILL.md"
tags:
  - skill
  - skill-category/workflow
---

# presentation-layout-qa

Prüft PowerPoint-Folien strukturell und kompositorisch auf Text-/Box-Overflow, Objektüberlagerungen, Slide-Grenzen, Footer-/Quellenkollisionen, Font-Ausreißer, Bild-/Chart-/Tabellenfehler sowie objektivierbare visuelle Qualitätsmängel wie überdimensionierte Container, schlechte Information-to-Space-Ratio, schwache Leserichtung und untergewichtete Schlussfolgerungen. Verwenden als Layout-QA vor finalem Rendering; ergänzt, aber ersetzt nicht den vollständigen visuellen Render-Review.

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

- Mode: `none`
- Passed: `None`
- Cases: `0`
- Recorded results: `0`

## Canonical source

`skills/presentation-layout-qa/SKILL.md`
