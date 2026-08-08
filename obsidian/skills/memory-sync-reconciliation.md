---
type: skill
generated: true
name: "memory-sync-reconciliation"
category: "internal"
userFacing: false
evaluationPassed: true
evaluationMode: "compatibility"
caseCount: 3
recordedResultCount: 3
sourcePath: "skills/memory-sync-reconciliation/SKILL.md"
tags:
  - skill
  - skill-category/internal
---

# memory-sync-reconciliation

Gleicht mehrere bereits governance-konforme Kommunikationsprofile und Memory-Ledger deterministisch ab, propagiert Forget/Supersession/Expiry sicher und legt echte Konflikte zur Auflösung vor. Verwenden, wenn Memory-Stände aus unterschiedlichen Sitzungen, Clients oder Persistenzkanälen konvergieren sollen, ohne neue Memories zu erfinden.

> Generated from canonical repository metadata. Do not edit this note manually.

## Category

[[categories/internal|internal]]

## Requires

- [[skills/communication-memory-governance|communication-memory-governance]]

## Required by

- —

## Outputs

- `communication-profile.merged.json`
- `memory-ledger.merged.json`
- `memory-reconciliation-plan.json`

## Output consumers

### `communication-profile.merged.json`

- Terminal or currently unconsumed output.

### `memory-ledger.merged.json`

- Terminal or currently unconsumed output.

### `memory-reconciliation-plan.json`

- Terminal or currently unconsumed output.

## Evaluation

- Mode: `compatibility`
- Passed: `True`
- Cases: `3`
- Recorded results: `3`

## Canonical source

`skills/memory-sync-reconciliation/SKILL.md`
