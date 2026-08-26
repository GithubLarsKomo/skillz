---
type: skill
generated: true
name: "implement-from-issue"
category: "engineering"
userFacing: true
evaluationPassed: true
evaluationMode: "compatibility"
caseCount: 3
recordedResultCount: 3
sourcePath: "skills/implement-from-issue/SKILL.md"
tags:
  - skill
  - skill-category/engineering
---

# implement-from-issue

Implementiert ein klar abgegrenztes Repository-Issue vom verifizierten Ausgangszustand bis zu einem überprüfbaren Commit- oder Pull-Request-Stand mit vollständiger Rückverfolgbarkeit, Testevidenz, Sicherheits- und Migrationsbewertung sowie expliziter externer Nachverifikation. Verwenden, wenn ein umsetzungsreifes Issue sicher und ohne Scope-Ausweitung ausgeführt werden soll.

> Generated from canonical repository metadata. Do not edit this note manually.

## Category

[[categories/engineering|engineering]]

## Requires

- [[skills/agent-handoff|agent-handoff]]
- [[skills/deferred-external-action-verification|deferred-external-action-verification]]
- [[skills/disciplined-diagnosis|disciplined-diagnosis]]
- [[skills/test-driven-vertical-slice|test-driven-vertical-slice]]

## Required by

- [[skills/optimize-software-performance|optimize-software-performance]]
- [[skills/two-axis-code-review|two-axis-code-review]]

## Outputs

- `implementation-evidence.json`
- `implementation-residual-risk-handoff.json`
- `reviewable-change-brief.md`

## Output consumers

### `implementation-evidence.json`

- [[skills/optimize-software-performance|optimize-software-performance]]
- [[skills/two-axis-code-review|two-axis-code-review]]

### `implementation-residual-risk-handoff.json`

- [[skills/optimize-software-performance|optimize-software-performance]]
- [[skills/two-axis-code-review|two-axis-code-review]]

### `reviewable-change-brief.md`

- [[skills/optimize-software-performance|optimize-software-performance]]
- [[skills/two-axis-code-review|two-axis-code-review]]

## Evaluation

- Mode: `compatibility`
- Passed: `True`
- Cases: `3`
- Recorded results: `3`

## Canonical source

`skills/implement-from-issue/SKILL.md`
