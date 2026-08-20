---
type: skill
generated: true
name: "spec-to-vertical-issues"
category: "engineering"
userFacing: true
evaluationPassed: true
evaluationMode: "compatibility"
caseCount: 3
recordedResultCount: 3
sourcePath: "skills/spec-to-vertical-issues/SKILL.md"
tags:
  - skill
  - skill-category/engineering
---

# spec-to-vertical-issues

Zerlegt eine freigegebene, konsistente Spezifikation in kleine, unabhängig abnehmbare vertikale Implementierungs-Issues mit vollständiger Rückverfolgbarkeit, Abnahmeevidenz, Abhängigkeiten und expliziten Nicht-Zielen. Verwenden, wenn aus SPEC.md und Entscheidungsregister eine geordnete Engineering-Backlog-Übergabe entstehen soll, ohne irreversible Architekturentscheidungen stillschweigend zu treffen.

> Generated from canonical repository metadata. Do not edit this note manually.

## Category

[[categories/engineering|engineering]]

## Requires

- [[skills/conversation-to-spec|conversation-to-spec]]

## Required by

- [[skills/test-driven-vertical-slice|test-driven-vertical-slice]]
- [[skills/throwaway-prototype|throwaway-prototype]]

## Outputs

- `dependency-order.json`
- `vertical-issues.json`
- `vertical-issues.md`

## Output consumers

### `dependency-order.json`

- [[skills/test-driven-vertical-slice|test-driven-vertical-slice]]
- [[skills/throwaway-prototype|throwaway-prototype]]

### `vertical-issues.json`

- [[skills/test-driven-vertical-slice|test-driven-vertical-slice]]
- [[skills/throwaway-prototype|throwaway-prototype]]

### `vertical-issues.md`

- [[skills/test-driven-vertical-slice|test-driven-vertical-slice]]
- [[skills/throwaway-prototype|throwaway-prototype]]

## Evaluation

- Mode: `compatibility`
- Passed: `True`
- Cases: `3`
- Recorded results: `3`

## Canonical source

`skills/spec-to-vertical-issues/SKILL.md`
