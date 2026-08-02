# Obsidian Skills – Redundancy / Gap Analysis

Source inspiration: `kepano/obsidian-skills` (MIT), evaluated as concepts rather than copied implementation.

## Design rule

Obsidian is an adapter and interchange target, not the canonical knowledge model. Core capabilities remain provider-neutral and use stable Markdown/JSON contracts.

## Matrix

| Upstream capability | Existing skillz capability | Gap | Decision |
|---|---|---|---|
| Obsidian Markdown: properties, links, embeds, addressable blocks | `decision-record`, `agent-handoff`, `project-status-brief`, `communication-memory-governance` already create semantic artifacts | no shared contract for identity, metadata, typed links and provenance across artifacts | add `structured-knowledge-artifact` |
| Obsidian Bases: filters, formulas, views, summaries | capability index/query tooling and several status skills provide domain-specific projections | no generic, side-effect-free projection over governed knowledge artifacts | add `knowledge-view` |
| JSON Canvas: nodes, edges, groups | `large-work-wayfinder`, `architecture-deepening-review`, `domain-model-maintenance` reason about structures | no provider-neutral graph/map interchange contract | add `knowledge-map-generator` |
| Obsidian CLI | repository/tool adapters already remain outside core semantics | Obsidian execution may be useful but is product-specific | defer to optional `obsidian-adapter`; do not make it core |
| Defuddle: clean web-to-Markdown extraction | research workflows consume sources but extraction/normalization is not a shared contract | provenance-preserving source normalization is reusable | future `source-to-context`; keep outside this first slice |

## Redundancy boundaries

### `communication-memory-governance`
Owns persistability, sensitivity, lifecycle, confidence and memory activation. It must not be replaced by a linked-note model.

### `memory-sync-reconciliation`
Owns reconciliation of divergent governance-conformant memory states. Knowledge views/maps are read models and must not resolve conflicts.

### `decision-record`
Owns decision semantics. `structured-knowledge-artifact` only provides an envelope and links.

### `agent-handoff` / `project-status-brief`
Own transient work/project state. They may emit or reference knowledge artifacts but do not become durable memory automatically.

### `domain-model-maintenance`
Owns domain-model changes. `knowledge-map-generator` only projects existing entities/relations; it does not invent domain semantics.

### `composable-skill-factory`
Owns creation/evaluation of skills. The new capabilities follow its small-skill, stable-handoff and adapter-separation rules.

## Minimal architecture

```text
semantic producers
(decision-record, governance, handoff, domain model, research)
        |
        v
structured-knowledge-artifact
        |
        +-------------------+
        |                   |
        v                   v
 knowledge-view       knowledge-map-generator
        |                   |
        +---------+---------+
                  v
          provider adapters
      Obsidian / files / Neo4j / ...
```

`chatgpt-communication` remains the governed persistence/exchange channel for communication memory. It should consume the artifact envelope for Markdown mirrors and later expose linked-memory projections, while JSON remains the canonical machine state until a separately reviewed migration changes that contract.

## Recommended slices

1. Introduce `structured-knowledge-artifact` as the common envelope.
2. Introduce `knowledge-view` as a pure projection contract.
3. Introduce `knowledge-map-generator` as a pure graph projection contract.
4. Extend `chatgpt-communication` with an Obsidian-compatible Markdown mirror contract built on the envelope.
5. Later evaluate `source-to-context` and an `obsidian-adapter` independently; neither is required for the core model.

## License / provenance

The architecture is inspired by the open-format separation visible in `kepano/obsidian-skills`. No upstream skill text is copied. Any future direct code reuse must retain the applicable MIT attribution and be reviewed separately.