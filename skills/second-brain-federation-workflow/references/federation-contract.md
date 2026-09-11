# Second Brain Federation Contract

## Purpose

This contract defines the boundary between autonomous Project Second Brains and a private Super Second Brain.

The Super Second Brain is a registry and routing layer. It MUST NOT become a second source of truth for project content.

## Canonical ownership

Child Project Second Brains own project memory, decisions, events, state, evidence references and asset manifests. Producer skills continue to own their canonical artifacts.

The Super Second Brain owns only federation metadata:

- stable brain identity,
- repository reference and observed visibility,
- project-memory entrypoint,
- scope and workflow-family routing metadata,
- availability and freshness,
- non-sensitive relations between brains,
- federation lifecycle events.

## Privacy boundary

A real federation registry can itself reveal sensitive information because repository names and domain labels expose the existence of projects or matters.

Therefore:

- the real Super Second Brain SHOULD be private by default;
- private repository names MUST NOT be committed to a public framework repository merely to configure routing;
- content from a private Child Brain MUST NOT be copied into a less-protected Super Brain;
- the portable `skillz` repository may contain only generic schemas, workflow rules and neutral examples.

## Availability model

Repository availability and Project-Memory availability are distinct.

| Status | Meaning |
|---|---|
| `available` | Repository and declared memory entrypoint were verified. |
| `bootstrap-needed` | Repository exists and is reachable, but no usable Project-Memory root is present yet. |
| `pending` | Expected registry target cannot yet be completely verified. |
| `unavailable` | A previously known target cannot currently be reached. |
| `archived` | Target is intentionally historical and not an active routing destination. |

Do not infer `available` solely from repository existence.

## Stable identity

Each Child Brain has a stable `brainId`. Repository rename, transfer or restructuring updates location metadata without minting a new `brainId` unless the knowledge domain itself is intentionally split into a new brain.

## Recommended Super-Brain layout

```text
README.md
docs/super-memory/
├── INDEX.md
├── REGISTRY.md
├── registry.json
├── state.json
├── brains/
├── domains/
└── events/
```

## Registry minimum fields

```json
{
  "brainId": "stable-brain-id",
  "label": "Human-readable label",
  "mode": "project|collection",
  "scope": "routing scope",
  "repository": "owner/repository",
  "repositoryVisibility": "private|public|internal",
  "projectMemoryRoot": "docs/project-memory/INDEX.md",
  "status": "available|bootstrap-needed|pending|unavailable|archived",
  "workflowFamilies": [],
  "tags": [],
  "lastVerifiedAt": "ISO-8601 timestamp",
  "latestEventRef": null
}
```

## Mutable federation state: single-source rule

Availability, freshness and current repository/memory reachability are **mutable federation state**. They MUST have one canonical source in the Super Brain, normally `registry.json`.

- Human tables such as `REGISTRY.md` MAY be derived projections.
- Stable per-brain routing notes SHOULD point to the canonical registry instead of duplicating `status`, `lastVerifiedAt` or reachability fields.
- If a consumer generates cached projections, they MUST be refreshed from the canonical registry during the same federation transition.
- Scope, workflow-family routing and stable `brainId` may live in durable routing notes, but a stale routing note MUST NOT override the canonical registry.

This rule prevents contradictory states such as `available` in the registry and `bootstrap-needed` in a routing note.

## Collection repositories

A collection repository groups multiple cases, matters or projects in one domain. The repository SHOULD maintain a domain-level Project Memory at the declared federation root while individual persistent children live under:

```text
projects/<id>/docs/project-memory/
```

Collection mode is preferred over creating one repository per case when the children share the same domain governance, access boundary, retention model and workflow family.

Create a child Project Memory only when the work is genuinely longitudinal, for example a persistent coaching programme, legal matter, investigation, tax case, course, dossier, trip or athlete/season programme. One-off answers, lookups or transient tasks do not require a child memory.

Create a separate repository for a child only when it has a materially independent lifecycle, access/retention boundary, source-control/runtime need or canonical artifact set that cannot be safely governed by the collection.

The Super Brain registers the collection itself and MAY index active child roots as pointers. It MUST NOT flatten their content into the global registry.

## Consolidation policy

Topic overlap alone is not a reason to merge Second Brains. Prefer **logical consolidation** through domain maps, relations and routing before physical repository consolidation.

A physical merge is appropriate only when candidate brains substantially converge on all of the following:

- lifecycle and closure semantics,
- access, privacy and retention boundary,
- canonical artifact ownership,
- workflow families and transition gates,
- repository/runtime needs.

If any of these boundaries differ materially, keep the Child Brains separate and connect them through federation domain maps or explicit relations.

## Synchronization policy

Federation sync is event-driven rather than write-through on every local Project-Memory update.

Sync is required when:

- a brain is created or first registered;
- a repository is renamed, transferred or archived;
- scope or routing metadata materially changes;
- availability changes state;
- an explicit global refresh is requested;
- a milestone or handoff deliberately publishes a refreshed routing summary.

Ordinary local events do not require a cross-repository write.

## Read-before-route

The Super Brain is a routing map, not a substitute for reading the Child Brain. When a Child Brain is available, any substantive task MUST follow the registry pointer and read the canonical Child entrypoint before relying on local project context.

## Failure semantics

- Missing Super Brain does not block Child Brains.
- Missing Child Project Memory yields `bootstrap-needed`.
- Connectivity or authorization failure yields `unavailable` or `pending` depending on prior state.
- No identifier, visibility, path, freshness timestamp or state may be fabricated.
- Historical federation events are append-oriented; corrections use a later event rather than silent history rewrite.
