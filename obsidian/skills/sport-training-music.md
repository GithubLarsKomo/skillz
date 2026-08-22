---
type: skill
generated: true
name: "sport-training-music"
category: "workflow"
userFacing: true
evaluationPassed: true
evaluationMode: "compatibility"
caseCount: 3
recordedResultCount: 3
sourcePath: "skills/sport-training-music/SKILL.md"
tags:
  - skill
  - skill-category/workflow
---

# sport-training-music

Erstellt präferenzbasierte Musikprofile und Session-Empfehlungen für Aktivierung, Motivation, Affekt, Warm-up, Training und Recovery. Verwenden für Trainingsmusik nach Athletenpräferenzen; BPM und Genre nicht als starre Leistungs- oder Intensitätsformel behandeln.

> Generated from canonical repository metadata. Do not edit this note manually.

## Category

[[categories/workflow|workflow]]

## Requires

- [[skills/sport-athlete-profile|sport-athlete-profile]]
- [[skills/sport-microcycle-planning|sport-microcycle-planning]]

## Required by

- [[skills/sport-athlete-management|sport-athlete-management]]

## Outputs

- `training-music-profile.json`

## Output consumers

### `training-music-profile.json`

- [[skills/sport-athlete-management|sport-athlete-management]]

## Evaluation

- Mode: `compatibility`
- Passed: `True`
- Cases: `3`
- Recorded results: `3`

## Canonical source

`skills/sport-training-music/SKILL.md`
