---
type: skill
generated: true
name: "creative-revision-regression"
category: "workflow"
userFacing: true
evaluationPassed: true
evaluationMode: "compatibility"
caseCount: 3
recordedResultCount: 3
sourcePath: "skills/creative-revision-regression/SKILL.md"
tags:
  - skill
  - skill-category/workflow
---

# creative-revision-regression

Klassifiziert die Auswirkung materieller Creative-Writing-Revisionen, entscheidet welche früheren Gates dadurch ungültig werden und prüft gezielte Fixes gegen Protect-Constraints und Kollateralschäden. Verwenden nach strukturellen, Reader-, Voice- oder Award-getriebenen Revisionen; kleine Line-Fixes sollen keine unnötigen Voll-Reruns auslösen.

> Generated from canonical repository metadata. Do not edit this note manually.

## Category

[[categories/workflow|workflow]]

## Requires

- [[skills/creative-prose-revision|creative-prose-revision]]

## Required by

- [[skills/fiction-award-jury-review|fiction-award-jury-review]]
- [[skills/fiction-series-writing-workflow|fiction-series-writing-workflow]]
- [[skills/song-album-release-workflow|song-album-release-workflow]]

## Outputs

- `creative-revision-regression.json`
- `gate-invalidation-map.json`
- `revision-impact-classification.json`

## Output consumers

### `creative-revision-regression.json`

- [[skills/fiction-award-jury-review|fiction-award-jury-review]]
- [[skills/fiction-series-writing-workflow|fiction-series-writing-workflow]]
- [[skills/song-album-release-workflow|song-album-release-workflow]]

### `gate-invalidation-map.json`

- [[skills/fiction-series-writing-workflow|fiction-series-writing-workflow]]
- [[skills/song-album-release-workflow|song-album-release-workflow]]

### `revision-impact-classification.json`

- [[skills/song-album-release-workflow|song-album-release-workflow]]

## Evaluation

- Mode: `compatibility`
- Passed: `True`
- Cases: `3`
- Recorded results: `3`

## Canonical source

`skills/creative-revision-regression/SKILL.md`
