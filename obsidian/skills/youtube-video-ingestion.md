---
type: skill
generated: true
name: "youtube-video-ingestion"
category: "internal"
userFacing: false
evaluationPassed: null
evaluationMode: "none"
caseCount: 0
recordedResultCount: 0
sourcePath: "skills/youtube-video-ingestion/SKILL.md"
tags:
  - skill
  - skill-category/internal
---

# youtube-video-ingestion

Normalisiert ein zugängliches YouTube-Video zu einem nachvollziehbaren Quellenpaket aus Metadaten, zeitcodiertem Transcript, Kapitel-/Segmentstruktur und selektierten visuellen Evidenzankern. Verwenden als Ingestion-Schritt für Lern-, SOP- oder Analyseworkflows; nicht zum Umgehen von Zugriffsschutz, DRM oder Plattformbeschränkungen und nicht zur inhaltlichen Synthese.

> Generated from canonical repository metadata. Do not edit this note manually.

## Category

[[categories/internal|internal]]

## Requires

- —

## Required by

- [[skills/youtube-learning-workflow|youtube-learning-workflow]]

## Outputs

- `youtube-frame-index.json`
- `youtube-transcript-index.json`
- `youtube-video-source.json`

## Output consumers

### `youtube-frame-index.json`

- [[skills/youtube-learning-workflow|youtube-learning-workflow]]

### `youtube-transcript-index.json`

- [[skills/youtube-learning-workflow|youtube-learning-workflow]]

### `youtube-video-source.json`

- [[skills/youtube-learning-workflow|youtube-learning-workflow]]

## Evaluation

- Mode: `none`
- Passed: `None`
- Cases: `0`
- Recorded results: `0`

## Canonical source

`skills/youtube-video-ingestion/SKILL.md`
