---
type: skill
generated: true
name: "merge-conflict-resolution"
category: "internal"
userFacing: false
evaluationPassed: true
evaluationMode: "compatibility"
caseCount: 3
recordedResultCount: 3
sourcePath: "skills/merge-conflict-resolution/SKILL.md"
tags:
  - skill
  - skill-category/internal
---

# merge-conflict-resolution

Löst Git-Merge-Konflikte semantisch, rekonstruiert die Änderungsabsichten beider Seiten, bewahrt akzeptiertes Verhalten und Repository-Invarianten und erzeugt einen überprüfbaren Auflösungsstand mit Tests, Rollback und Restrisiken. Verwenden, wenn Konfliktmarker allein nicht zeigen, welche fachliche oder technische Kombination korrekt ist.

> Generated from canonical repository metadata. Do not edit this note manually.

## Category

[[categories/internal|internal]]

## Requires

- [[skills/agent-handoff|agent-handoff]]
- [[skills/deferred-external-action-verification|deferred-external-action-verification]]
- [[skills/disciplined-diagnosis|disciplined-diagnosis]]
- [[skills/test-driven-vertical-slice|test-driven-vertical-slice]]
- [[skills/two-axis-code-review|two-axis-code-review]]

## Required by

- —

## Outputs

- `conflict-residual-risk-handoff.json`
- `conflict-resolution-evidence.json`
- `resolved-change-brief.md`

## Output consumers

### `conflict-residual-risk-handoff.json`

- Terminal or currently unconsumed output.

### `conflict-resolution-evidence.json`

- Terminal or currently unconsumed output.

### `resolved-change-brief.md`

- Terminal or currently unconsumed output.

## Evaluation

- Mode: `compatibility`
- Passed: `True`
- Cases: `3`
- Recorded results: `3`

## Canonical source

`skills/merge-conflict-resolution/SKILL.md`
