---
type: skill
generated: true
name: "person-research-dossier"
category: "research-knowledge"
userFacing: true
evaluationPassed: true
evaluationMode: "compatibility"
caseCount: 3
recordedResultCount: 3
sourcePath: "skills/person-research-dossier/SKILL.md"
tags:
  - skill
  - skill-category/research-knowledge
---

# person-research-dossier

Recherchiert eine konkrete Person aus belastbaren öffentlichen und bereitgestellten Quellen und strukturiert Biographie, Lebenslauf, Veröffentlichungen, IP, Arbeitgeber, Karriere sowie freiwillig öffentlich gemachte Hobbies und Sport in ein quellengebundenes Dossier. Verwenden, wenn eine Person systematisch verstanden werden soll, bevor ein Profilbericht, Meeting-Briefing oder rollenbezogenes Assessment entsteht.

> Generated from canonical repository metadata. Do not edit this note manually.

## Category

[[categories/research-knowledge|research-knowledge]]

## Requires

- [[skills/research-to-evidence-note|research-to-evidence-note]]

## Required by

- [[skills/person-profile-report|person-profile-report]]
- [[skills/person-research-report-workflow|person-research-report-workflow]]

## Outputs

- `person-ip-map.json`
- `person-publications.json`
- `person-research-dossier.md`
- `person-research-evidence.json`
- `person-timeline.json`

## Output consumers

### `person-ip-map.json`

- [[skills/person-profile-report|person-profile-report]]
- [[skills/person-research-report-workflow|person-research-report-workflow]]

### `person-publications.json`

- [[skills/person-profile-report|person-profile-report]]
- [[skills/person-research-report-workflow|person-research-report-workflow]]

### `person-research-dossier.md`

- [[skills/person-research-report-workflow|person-research-report-workflow]]

### `person-research-evidence.json`

- [[skills/person-profile-report|person-profile-report]]
- [[skills/person-research-report-workflow|person-research-report-workflow]]

### `person-timeline.json`

- [[skills/person-profile-report|person-profile-report]]
- [[skills/person-research-report-workflow|person-research-report-workflow]]

## Evaluation

- Mode: `compatibility`
- Passed: `True`
- Cases: `3`
- Recorded results: `3`

## Canonical source

`skills/person-research-dossier/SKILL.md`
