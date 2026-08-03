# Obsidian Skills – Redundancy / Gap Analysis

Source inspiration: `kepano/obsidian-skills` (MIT), evaluated as concepts rather than copied implementation.

## Design rule

Obsidian is an adapter and interchange target, not the canonical knowledge model. Core capabilities remain provider-neutral and use stable Markdown/JSON contracts.

## Matrix

| Upstream capability | Existing skillz capability | Gap | Decision |
|---|---|---|---|
| Obsidian Markdown: properties, links, embeds, addressable blocks | `decision-record`, `agent-handoff`, `project-status-brief`, `communication-memory-governance` already create semantic artifacts | no shared contract for identity, metadata, typed links and provenance across artifacts | implemented as `structured-knowledge-artifact` |
| Obsidian Bases: filters, formulas, views, summaries | capability index/query tooling and several status skills provide domain-specific projections | no generic, side-effect-free projection over governed knowledge artifacts | implemented as `knowledge-view` |
| JSON Canvas: nodes, edges, groups | `large-work-wayfinder`, `architecture-deepening-review`, `domain-model-maintenance` reason about structures | no provider-neutral graph/map interchange contract | implemented as `knowledge-map-generator` |
| Obsidian CLI / execution | repository/tool adapters remain outside core semantics | product-specific export/import boundary needed | implemented as optional `obsidian-adapter`; CLI remains replaceable execution backend |
| Defuddle: clean web-to-Markdown extraction | research workflows consume sources but extraction/normalization was not a shared contract | provenance-preserving source normalization is reusable | implemented independently as `source-to-context` |

## Redundancy boundaries

### `communication-memory-governance`
Owns persistability, sensitivity, lifecycle, confidence and memory activation. It is not replaced by a linked-note model.

### `memory-sync-reconciliation`
Owns reconciliation of divergent governance-conformant memory states. Knowledge views/maps and the Obsidian adapter are projections/candidate transport and must not resolve conflicts.

### `decision-record`
Owns decision semantics. `structured-knowledge-artifact` only provides an envelope and links.

### `agent-handoff` / `project-status-brief`
Own transient work/project state. They may emit or reference knowledge artifacts but do not become durable memory automatically.

### `domain-model-maintenance`
Owns domain-model changes. `knowledge-map-generator` only projects existing entities/relations; it does not invent domain semantics.

### `research-to-evidence-note`
Owns Claim-Synthese, Quellenqualität, Widersprüche und Confidence. `source-to-context` normalisiert nur bereits zugängliche Quelleninhalte.

### `composable-skill-factory`
Owns creation/evaluation of skills. The new capabilities follow its small-skill, stable-handoff and adapter-separation rules.

## Resulting architecture

```text
retrieval / parser / OCR / connectors
              |
              v
       source-to-context
              |
              v
   research / semantic producers
(decision, governance, domain, handoff)
              |
              v
 structured-knowledge-artifact
              |
        +-----+------+
        |            |
        v            v
 knowledge-view  knowledge-map-generator
        |            |
        +-----+------+
              v
       obsidian-adapter
       /      |       \
 Markdown   Bases   JSON Canvas
              |
              v
      candidate import only
              |
              v
 governance / reconciliation / apply
```

`chatgpt-communication` remains the governed persistence/exchange channel for communication memory. Its linked-memory Obsidian contract keeps canonical JSON authoritative and treats Markdown/Bases/Canvas as read projections. Any reverse flow stops first at a candidate artifact and must re-enter governance/reconciliation.

## Status of recommended slices

1. `structured-knowledge-artifact` — implemented and merged.
2. `knowledge-view` — implemented and merged.
3. `knowledge-map-generator` — implemented and merged.
4. `chatgpt-communication` Obsidian-compatible interchange contract — implemented and merged.
5. `source-to-context` — implemented independently on `main`.
6. `obsidian-adapter` — current follow-up slice; provider-specific and optional by design.

## Remaining deliberate non-goals

- no Obsidian dependency in provider-neutral core skills,
- no automatic bidirectional canonical sync,
- no Last-write-wins from filesystem timestamps,
- no promotion of manual wikilinks or Canvas edges to canonical domain relations,
- no duplication of research, governance or reconciliation semantics inside the adapter.

## License / provenance

The architecture is inspired by the open-format separation visible in `kepano/obsidian-skills`. No upstream skill text is copied. Any future direct code reuse must retain the applicable MIT attribution and be reviewed separately.
