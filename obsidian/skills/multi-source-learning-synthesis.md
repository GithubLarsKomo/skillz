---
type: skill
generated: true
name: "multi-source-learning-synthesis"
category: "internal"
userFacing: false
evaluationPassed: true
evaluationMode: "compatibility"
caseCount: 3
recordedResultCount: 3
sourcePath: "skills/multi-source-learning-synthesis/SKILL.md"
tags:
  - skill
  - skill-category/internal
---

# multi-source-learning-synthesis

Konsolidiert mehrere evidenzgebundene Learning-Modelle zu einem deduplizierten gemeinsamen Wissensmodell mit Claim-Clustern, Konflikten, Quellenabdeckung, Konsensstärke und offenen Lücken. Verwenden für Playlist-, Kurs- oder Multi-Video-Learning vor gemeinsamer HTML/PPTX/DOCX/PDF-Ausgabe.

> Generated from canonical repository metadata. Do not edit this note manually.

## Category

[[categories/internal|internal]]

## Requires

- [[skills/learning-source-arbitration|learning-source-arbitration]]

## Required by

- [[skills/course-concept-graph|course-concept-graph]]
- [[skills/youtube-playlist-learning-workflow|youtube-playlist-learning-workflow]]

## Outputs

- `multi-source-conflict-map.json`
- `multi-source-learning-model.json`

## Output consumers

### `multi-source-conflict-map.json`

- [[skills/course-concept-graph|course-concept-graph]]
- [[skills/youtube-playlist-learning-workflow|youtube-playlist-learning-workflow]]

### `multi-source-learning-model.json`

- [[skills/course-concept-graph|course-concept-graph]]
- [[skills/learning-delivery-workflow|learning-delivery-workflow]]
- [[skills/youtube-playlist-learning-workflow|youtube-playlist-learning-workflow]]

## Evaluation

- Mode: `compatibility`
- Passed: `True`
- Cases: `3`
- Recorded results: `3`

## Canonical source

`skills/multi-source-learning-synthesis/SKILL.md`
