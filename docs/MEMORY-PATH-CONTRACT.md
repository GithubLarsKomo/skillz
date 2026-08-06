# Memory Path Contract

Every skill has a memory path. The memory path is a governed handoff, not an additional durable output owned by the skill.

## Principle

A skill may discover information worth reusing, but it must not persist that information directly as durable memory. At completion, the skill may emit an ephemeral `memory-candidate-handoff-v1` payload and pass it to `communication-memory-governance`, which alone decides whether a candidate becomes active memory, remains a candidate, is rejected, expires, or supersedes an older entry.

This prevents three failure modes:

- transient run state being mistaken for durable memory;
- volatile regulatory facts being stored as timeless truth;
- every skill inventing a separate persistence mechanism or memory file.

## Candidate classes

Use the handoff only for reusable, non-sensitive learnings in one of these classes:

- `durable-fact`: a stable fact that remains useful beyond the current run;
- `durable-constraint`: a stable constraint that should shape later work;
- `validated-pattern`: a reusable workflow, interpretation pattern, failure mode, or decision heuristic validated by evidence;
- `communication-preference`: a stable user interaction preference.

Do not use the memory path for current task status, open follow-ups, current repository state, temporary tool results, speculative hypotheses, secrets, sensitive personal data, or raw connector payloads.

## Regulatory memory rules

Regulatory and standards-related candidates require stronger provenance:

- distinguish law/regulation, standard, guidance, organizational policy, interpretation, and project decision;
- include authoritative `sourceRefs` whenever the candidate depends on external authority;
- include `asOf` for time-dependent claims;
- include `reviewAfter` or `expiresAt` when guidance, implementation status, database content, transition rules, fees, review targets, recognized standards, or similar facts can change;
- store reusable interpretation/process learnings preferentially over snapshots of volatile facts;
- never promote a classification, clearance, approval, certification, notified-body position, or legal conclusion to durable fact unless the required authority is actually evidenced.

## Ephemeral handoff

The handoff conforms to `schemas/memory-candidate-handoff-v1.schema.json` and is run-scoped. Example:

```json
{
  "schemaVersion": 1,
  "sourceSkill": "ivdr-device-classification",
  "asOf": "2026-08-06T20:00:00Z",
  "candidates": [
    {
      "kind": "validated-pattern",
      "statement": "For this product family, specimen type is a classification-relevant discriminator that must be fixed before applying the rule tree.",
      "scope": "project-family:example-ivd",
      "sourceRefs": ["classification-assessment:sha256:..."],
      "confidence": "high",
      "reviewAfter": null
    }
  ],
  "rejectedRunOnly": []
}
```

`communication-memory-governance` receives the payload and applies sensitivity, durability, confirmation, provenance, conflict, supersession, expiry, and forget rules. The producing skill must never claim persistence succeeded unless the memory system actually confirms it.

## Skill-authoring requirement

Every new or materially revised skill must include a `## Memory Path` section that states:

1. what type of learning is eligible;
2. what is explicitly run-only;
3. which provenance/freshness fields are mandatory;
4. that the candidate handoff goes to `communication-memory-governance`;
5. that persistence is not owned or assumed by the producing skill.

For skills whose work should normally produce no durable learning, the section still exists and says that the default handoff is empty unless a validated reusable learning emerges.
