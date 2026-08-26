---
type: skill
generated: true
name: "presentation-render-verifier"
category: "workflow"
userFacing: true
evaluationPassed: null
evaluationMode: "none"
caseCount: 0
recordedResultCount: 0
sourcePath: "skills/presentation-render-verifier/SKILL.md"
tags:
  - skill
  - skill-category/workflow
---

# presentation-render-verifier

Rendert ein Präsentationsdeck in visuell prüfbare Folienbilder und eine Druck-/PDF-Version und bewertet das Ergebnis auf Clipping, Font-Substitution, unerwartete Umbrüche, Kontrast, visuelle Hierarchie, Dichte und Deck-Konsistenz. Verwenden als finales visuelles QA-Gate nach struktureller Layoutprüfung; nicht als Ersatz für objektbasierte PPTX-Prüfung.

> Generated from canonical repository metadata. Do not edit this note manually.

## Category

[[categories/workflow|workflow]]

## Requires

- [[skills/presentation-layout-qa|presentation-layout-qa]]

## Required by

- [[skills/template-presentation-workflow|template-presentation-workflow]]

## Outputs

- `presentation-preview.pdf`
- `presentation-render-qa.json`
- `presentation-render-qa.md`

## Output consumers

### `presentation-preview.pdf`

- [[skills/template-presentation-workflow|template-presentation-workflow]]

### `presentation-render-qa.json`

- [[skills/template-presentation-workflow|template-presentation-workflow]]

### `presentation-render-qa.md`

- [[skills/template-presentation-workflow|template-presentation-workflow]]

## Evaluation

- Mode: `none`
- Passed: `None`
- Cases: `0`
- Recorded results: `0`

## Canonical source

`skills/presentation-render-verifier/SKILL.md`
