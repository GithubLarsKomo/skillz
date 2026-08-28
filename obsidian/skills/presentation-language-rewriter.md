---
type: skill
generated: true
name: "presentation-language-rewriter"
category: "workflow"
userFacing: true
evaluationPassed: true
evaluationMode: "compatibility"
caseCount: 3
recordedResultCount: 3
sourcePath: "skills/presentation-language-rewriter/SKILL.md"
tags:
  - skill
  - skill-category/workflow
---

# presentation-language-rewriter

Überarbeitet deutsche und englische Präsentationstexte elementbezogen für Slide-Titel, Key Messages, Bullets, Chart-Labels, Tabellen, Annotationen und Speaker Notes. Verwenden, wenn Präsentationssprache prägnant, idiomatisch, management-, wissenschafts- oder fachgerecht verbessert werden soll; nicht als Ersatz für Report- oder Memo-Redaktion.

> Generated from canonical repository metadata. Do not edit this note manually.

## Category

[[categories/workflow|workflow]]

## Requires

- [[skills/rewrite-fidelity-verifier|rewrite-fidelity-verifier]]

## Required by

- [[skills/template-presentation-workflow|template-presentation-workflow]]

## Outputs

- `presentation-language-report.json`
- `presentation-revised-text`

## Output consumers

### `presentation-language-report.json`

- [[skills/template-presentation-workflow|template-presentation-workflow]]

### `presentation-revised-text`

- [[skills/template-presentation-workflow|template-presentation-workflow]]

## Evaluation

- Mode: `compatibility`
- Passed: `True`
- Cases: `3`
- Recorded results: `3`

## Canonical source

`skills/presentation-language-rewriter/SKILL.md`
