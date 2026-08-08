---
type: skill
generated: true
name: "deferred-external-action-verification"
category: "internal"
userFacing: false
evaluationPassed: true
evaluationMode: "compatibility"
caseCount: 3
recordedResultCount: 3
sourcePath: "skills/deferred-external-action-verification/SKILL.md"
tags:
  - skill
  - skill-category/internal
---

# deferred-external-action-verification

Richtet für asynchron arbeitende externe Programme, APIs und CI/CD-Systeme eine zeitversetzte, wiederholbare Ergebnisprüfung per Cronjob oder gleichwertigem Scheduler ein. Nimmt jeden vom Agenten selbst ausgelösten CI-Lauf automatisch in eine Beobachtungsliste auf und setzt den gespeicherten Arbeitsablauf nach verifiziertem Erfolg fort. Der Skill definiert Wartefenster, Statusabfrage, Idempotenz, Sperren, Retry- und Abbruchregeln, Protokollierung sowie die sichere Aufräumlogik nach Erfolg oder endgültigem Fehler.

> Generated from canonical repository metadata. Do not edit this note manually.

## Category

[[categories/internal|internal]]

## Requires

- —

## Required by

- [[skills/engineering-delivery-followup|engineering-delivery-followup]]
- [[skills/implement-from-issue|implement-from-issue]]
- [[skills/merge-conflict-resolution|merge-conflict-resolution]]
- [[skills/qms-management-review-action-followup|qms-management-review-action-followup]]

## Outputs

- `continuation result`
- `verified terminal status`
- `watch record`

## Output consumers

### `continuation result`

- [[skills/engineering-delivery-followup|engineering-delivery-followup]]
- [[skills/implement-from-issue|implement-from-issue]]
- [[skills/merge-conflict-resolution|merge-conflict-resolution]]
- [[skills/qms-management-review-action-followup|qms-management-review-action-followup]]

### `verified terminal status`

- [[skills/engineering-delivery-followup|engineering-delivery-followup]]
- [[skills/implement-from-issue|implement-from-issue]]
- [[skills/merge-conflict-resolution|merge-conflict-resolution]]
- [[skills/qms-management-review-action-followup|qms-management-review-action-followup]]

### `watch record`

- [[skills/engineering-delivery-followup|engineering-delivery-followup]]
- [[skills/implement-from-issue|implement-from-issue]]
- [[skills/merge-conflict-resolution|merge-conflict-resolution]]
- [[skills/qms-management-review-action-followup|qms-management-review-action-followup]]

## Evaluation

- Mode: `compatibility`
- Passed: `True`
- Cases: `3`
- Recorded results: `3`

## Canonical source

`skills/deferred-external-action-verification/SKILL.md`
