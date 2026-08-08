---
type: skill
generated: true
name: "obsidian-adapter"
category: "internal"
userFacing: false
evaluationPassed: true
evaluationMode: "compatibility"
caseCount: 3
recordedResultCount: 3
sourcePath: "skills/obsidian-adapter/SKILL.md"
tags:
  - skill
  - skill-category/internal
---

# obsidian-adapter

Rendert provider-neutrale Knowledge Artifacts, Views und Maps in Obsidian-kompatible Markdown-, Bases- und JSON-Canvas-Artefakte und liest optional editierte Obsidian-Artefakte ausschließlich als nicht-kanonische Kandidaten zurück. Verwenden, wenn der bestehende Knowledge-Layer in einen Obsidian Vault projiziert oder aus Obsidian sicher zur vorgelagerten Governance/Reconciliation zurückgeführt werden soll; Obsidian bleibt Adapter, nicht semantische Quelle.

> Generated from canonical repository metadata. Do not edit this note manually.

## Category

[[categories/internal|internal]]

## Requires

- [[skills/knowledge-map-generator|knowledge-map-generator]]
- [[skills/knowledge-view|knowledge-view]]
- [[skills/structured-knowledge-artifact|structured-knowledge-artifact]]

## Required by

- —

## Outputs

- `obsidian-candidate.json`
- `obsidian-map.canvas`
- `obsidian-note.md`
- `obsidian-view.base`

## Output consumers

### `obsidian-candidate.json`

- Terminal or currently unconsumed output.

### `obsidian-map.canvas`

- Terminal or currently unconsumed output.

### `obsidian-note.md`

- Terminal or currently unconsumed output.

### `obsidian-view.base`

- Terminal or currently unconsumed output.

## Evaluation

- Mode: `compatibility`
- Passed: `True`
- Cases: `3`
- Recorded results: `3`

## Canonical source

`skills/obsidian-adapter/SKILL.md`
