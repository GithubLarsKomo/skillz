---
type: skill
generated: true
name: "template-presentation-workflow"
category: "workflow"
userFacing: true
evaluationPassed: null
evaluationMode: "none"
caseCount: 0
recordedResultCount: 0
sourcePath: "skills/template-presentation-workflow/SKILL.md"
tags:
  - skill
  - skill-category/workflow
---

# template-presentation-workflow

Orchestriert die Erstellung oder Überarbeitung editierbarer Präsentationen auf Basis eines vorhandenen PowerPoint-Templates oder einer Referenzpräsentation. Übernimmt Look & Feel, kuratiert Storyline und Slide-Architektur, optimiert Deutsch/Englisch präsentationsspezifisch und erzwingt strukturelle sowie Render-/PDF-QA. Verwenden für template-basierte Management-, wissenschaftliche, technische, Sales- oder Educational-Decks; Corporate-Spezialregeln bleiben in dünnen Wrapper-Skills.

> Generated from canonical repository metadata. Do not edit this note manually.

## Category

[[categories/workflow|workflow]]

## Requires

- [[skills/presentation-language-rewriter|presentation-language-rewriter]]
- [[skills/presentation-layout-qa|presentation-layout-qa]]
- [[skills/presentation-render-verifier|presentation-render-verifier]]
- [[skills/presentation-template-profiler|presentation-template-profiler]]

## Required by

- [[skills/euroimmun-presentation-workflow|euroimmun-presentation-workflow]]
- [[skills/youtube-course-builder-workflow|youtube-course-builder-workflow]]
- [[skills/youtube-learning-workflow|youtube-learning-workflow]]
- [[skills/youtube-playlist-learning-workflow|youtube-playlist-learning-workflow]]

## Outputs

- `presentation-qa.md`
- `presentation-template-profile.json`
- `presentation.pdf`
- `presentation.pptx`

## Output consumers

### `presentation-qa.md`

- Ambiguous producer contract; no inferred consumer edge.

### `presentation-template-profile.json`

- Ambiguous producer contract; no inferred consumer edge.

### `presentation.pdf`

- [[skills/euroimmun-presentation-workflow|euroimmun-presentation-workflow]]
- [[skills/youtube-course-builder-workflow|youtube-course-builder-workflow]]
- [[skills/youtube-learning-workflow|youtube-learning-workflow]]
- [[skills/youtube-playlist-learning-workflow|youtube-playlist-learning-workflow]]

### `presentation.pptx`

- [[skills/euroimmun-presentation-workflow|euroimmun-presentation-workflow]]
- [[skills/youtube-course-builder-workflow|youtube-course-builder-workflow]]
- [[skills/youtube-learning-workflow|youtube-learning-workflow]]
- [[skills/youtube-playlist-learning-workflow|youtube-playlist-learning-workflow]]

## Evaluation

- Mode: `none`
- Passed: `None`
- Cases: `0`
- Recorded results: `0`

## Canonical source

`skills/template-presentation-workflow/SKILL.md`
