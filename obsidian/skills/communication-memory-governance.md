---
type: skill
generated: true
name: "communication-memory-governance"
category: "communication-memory"
userFacing: true
evaluationPassed: true
evaluationMode: "compatibility"
caseCount: 3
recordedResultCount: 3
sourcePath: "skills/communication-memory-governance/SKILL.md"
tags:
  - skill
  - skill-category/communication-memory
---

# communication-memory-governance

Verwaltet stabile Kommunikationspräferenzen und bestätigte Langzeit-Memory-Einträge getrennt von transientem Gesprächs-, Projekt- und Agentenzustand. Verwenden, wenn wiederkehrende User-Präferenzen, dauerhafte Fakten oder Korrekturen nachvollziehbar, scope-begrenzt und datenschutzsicher über Sitzungen hinweg verfügbar bleiben sollen, ohne Agent-Handoff, Decision Records oder Projektstatus zu duplizieren.

> Generated from canonical repository metadata. Do not edit this note manually.

## Category

[[categories/communication-memory|communication-memory]]

## Requires

- —

## Required by

- [[skills/memory-sync-reconciliation|memory-sync-reconciliation]]

## Outputs

- `communication-profile.json`
- `memory-ledger.json`

## Output consumers

### `communication-profile.json`

- [[skills/memory-sync-reconciliation|memory-sync-reconciliation]]

### `memory-ledger.json`

- [[skills/memory-sync-reconciliation|memory-sync-reconciliation]]

## Evaluation

- Mode: `compatibility`
- Passed: `True`
- Cases: `3`
- Recorded results: `3`

## Canonical source

`skills/communication-memory-governance/SKILL.md`
