---
name: structured-knowledge-artifact
description: Verpackt bereits fachlich bestimmte Informationen in ein provider-neutrales, adressierbares Wissensartefakt mit stabiler Identität, Metadaten, typisierten Links und Provenance. Verwenden, wenn Ergebnisse aus Decision Records, Memory Governance, Research, Domain Models oder anderen Skills dauerhaft referenzierbar und zwischen Markdown-, JSON-, Graph- oder Obsidian-Adaptern austauschbar werden sollen; bestimmt selbst weder Memory-Persistenz noch fachliche Wahrheit.
version: 0.1.0
status: candidate
owners:
  - GithubLarsKomo
outputs:
  - knowledge-artifact.json
  - knowledge-artifact.md
lastEvaluated: 2026-08-02
---

# Structured Knowledge Artifact

## Zweck

Dieser Skill erzeugt einen stabilen Envelope um bereits bestimmte Inhalte. Er trennt Semantik von Darstellung und Storage.

## Nicht-Ziele

Der Skill:
- entscheidet nicht, ob Gesprächsinhalte dauerhaftes Memory werden dürfen (`communication-memory-governance`),
- löst keine Memory-Konflikte (`memory-sync-reconciliation`),
- erfindet keine Entscheidungen oder Domain-Relationen,
- schreibt nicht direkt in Obsidian, Neo4j oder andere Backends.

## Minimaler Vertrag

```json
{
  "schemaVersion": 1,
  "id": "stable-id",
  "artifactType": "decision|memory|preference|domain-entity|research-note|handoff|status|other",
  "title": "human-readable title",
  "content": "canonical textual representation",
  "metadata": {},
  "links": [
    {"type": "supports|contradicts|supersedes|superseded-by|relates-to|derived-from|part-of|references", "targetId": "..."}
  ],
  "provenance": [{"sourceRef": "...", "observedAt": "ISO-8601"}],
  "lifecycle": {"state": "active|superseded|expired|rejected|transient"}
}
```

Domain producers may add fields under `metadata`; adapters must not silently reinterpret them.

## Workflow

1. Identify the upstream semantic owner and accept only its already-determined result.
2. Reuse an existing stable ID when the artifact represents the same logical object; do not generate duplicate identities for format conversions.
3. Preserve source references and lifecycle semantics from the producer.
4. Add only explicit, evidence-backed typed links.
5. Produce canonical JSON and, when requested, a Markdown mirror.
6. Verify round-trip preservation of ID, type, links, provenance and lifecycle before handing the artifact to an adapter.

## Markdown mirror

A Markdown representation may use YAML properties and wikilink-compatible text, but the portable contract is semantic rather than Obsidian-specific. At minimum preserve `id`, `artifactType`, lifecycle state and source references in machine-readable frontmatter.

## Quality gate

Pass only if:
- no new domain claim was invented while packaging,
- identity is stable across representations,
- provenance is not lost,
- lifecycle/supersession semantics survive conversion,
- transient artifacts are not promoted to durable memory by this skill,
- an adapter can consume the output without hidden conversational context.
