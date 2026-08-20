---
type: skill
generated: true
name: "teach"
category: "productivity"
userFacing: true
evaluationPassed: true
evaluationMode: "compatibility"
caseCount: 3
recordedResultCount: 3
sourcePath: "skills/teach/SKILL.md"
tags:
  - skill
  - skill-category/productivity
---

# teach

Orchestriert auf ausdrücklichen Wunsch einen zustandsbehafteten Lernprozess mit Lernmission, evidenzbasiertem Stoff, nachgewiesener Kompetenz, adaptivem nächsten Schritt und Übergaben an die Exam-Trainer-Lernruntime. Verwenden bei `/teach`, beim gezielten Erlernen eines Themas oder mit `/teach skill <skill-name>`; nicht für gewöhnliche Einzelerklärungen ohne Lernworkspace.

> Generated from canonical repository metadata. Do not edit this note manually.

## Category

[[categories/productivity|productivity]]

## Requires

- [[skills/learning-assessment|learning-assessment]]
- [[skills/learning-assessment-spec|learning-assessment-spec]]
- [[skills/learning-mission|learning-mission]]
- [[skills/learning-next-step|learning-next-step]]
- [[skills/learning-state|learning-state]]
- [[skills/research-to-evidence-note|research-to-evidence-note]]

## Required by

- —

## Outputs

- `learning-mission.json`
- `learning-next-step.json`
- `learning-practice-request.json`
- `learning-state.json`

## Output consumers

### `learning-mission.json`

- Ambiguous producer contract; no inferred consumer edge.

### `learning-next-step.json`

- Ambiguous producer contract; no inferred consumer edge.

### `learning-practice-request.json`

- Terminal or currently unconsumed output.

### `learning-state.json`

- Ambiguous producer contract; no inferred consumer edge.

## Evaluation

- Mode: `compatibility`
- Passed: `True`
- Cases: `3`
- Recorded results: `3`

## Canonical source

`skills/teach/SKILL.md`
