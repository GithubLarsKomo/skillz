---
type: skill
generated: true
name: "youtube-learning-workflow"
category: "workflow"
userFacing: true
evaluationPassed: null
evaluationMode: "none"
caseCount: 0
recordedResultCount: 0
sourcePath: "skills/youtube-learning-workflow/SKILL.md"
tags:
  - skill
  - skill-category/workflow
---

# youtube-learning-workflow

Orchestriert die tiefgehende Analyse eines YouTube-Videos zu evidenzgebundenen Key Take-Home Messages und optionalen derived SOPs, plant passende Diagramme/SVGs/Bilder, bindet alles an DESIGN.md und erzeugt wahlweise Landingpage-HTML, Präsentation und DOCX/PDF mit Cross-Format-QA. Verwenden für YouTube-Learner, Video-to-SOP, Video-to-Study-Guide oder Video-to-Presentation; nicht zum Umgehen von YouTube-Zugriffsschutz oder zur ungeprüften Freigabe regulierter SOPs.

> Generated from canonical repository metadata. Do not edit this note manually.

## Category

[[categories/workflow|workflow]]

## Requires

- [[skills/learning-delivery-workflow|learning-delivery-workflow]]
- [[skills/learning-summary-synthesis|learning-summary-synthesis]]
- [[skills/multimodal-learning-analysis|multimodal-learning-analysis]]
- [[skills/procedure-sop-extractor|procedure-sop-extractor]]
- [[skills/youtube-video-ingestion|youtube-video-ingestion]]

## Required by

- [[skills/youtube-playlist-learning-workflow|youtube-playlist-learning-workflow]]

## Outputs

- `learning-content-model.json`
- `youtube-learning-run.json`

## Output consumers

### `learning-content-model.json`

- [[skills/learning-delivery-workflow|learning-delivery-workflow]]
- [[skills/youtube-playlist-learning-workflow|youtube-playlist-learning-workflow]]

### `youtube-learning-run.json`

- [[skills/youtube-playlist-learning-workflow|youtube-playlist-learning-workflow]]

## Evaluation

- Mode: `none`
- Passed: `None`
- Cases: `0`
- Recorded results: `0`

## Canonical source

`skills/youtube-learning-workflow/SKILL.md`
