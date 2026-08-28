---
type: skill
generated: true
name: "multimodal-learning-analysis"
category: "internal"
userFacing: false
evaluationPassed: null
evaluationMode: "none"
caseCount: 0
recordedResultCount: 0
sourcePath: "skills/multimodal-learning-analysis/SKILL.md"
tags:
  - skill
  - skill-category/internal
---

# multimodal-learning-analysis

Analysiert ein zeitcodiertes Videoquellenpaket gemeinsam aus Sprache, visuellen Beobachtungen und Metadaten und erzeugt evidenzgebundene Lernclaims, Konzepte, Demonstrationen, Warnungen und Beziehungen. Verwenden nach Video-Ingestion; nicht zum Rendern finaler Lernartefakte oder zum Erfinden nicht sichtbarer Prozessdetails.

> Generated from canonical repository metadata. Do not edit this note manually.

## Category

[[categories/internal|internal]]

## Requires

- —

## Required by

- [[skills/learning-summary-synthesis|learning-summary-synthesis]]
- [[skills/learning-visual-planner|learning-visual-planner]]
- [[skills/procedure-sop-extractor|procedure-sop-extractor]]
- [[skills/youtube-learning-workflow|youtube-learning-workflow]]

## Outputs

- `learning-concept-map.json`
- `learning-evidence.json`

## Output consumers

### `learning-concept-map.json`

- [[skills/learning-summary-synthesis|learning-summary-synthesis]]
- [[skills/learning-visual-planner|learning-visual-planner]]
- [[skills/procedure-sop-extractor|procedure-sop-extractor]]
- [[skills/youtube-learning-workflow|youtube-learning-workflow]]

### `learning-evidence.json`

- [[skills/learning-summary-synthesis|learning-summary-synthesis]]
- [[skills/learning-visual-planner|learning-visual-planner]]
- [[skills/procedure-sop-extractor|procedure-sop-extractor]]
- [[skills/youtube-learning-workflow|youtube-learning-workflow]]

## Evaluation

- Mode: `none`
- Passed: `None`
- Cases: `0`
- Recorded results: `0`

## Canonical source

`skills/multimodal-learning-analysis/SKILL.md`
