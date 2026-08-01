# Structured capability resolver

`python scripts/resolve_capabilities.py` is a read-only inspection primitive over `docs/skill-capability-index.json`.

It accepts only explicit exact constraints and combines them by intersection. It does not perform natural-language interpretation, synonym expansion, semantic similarity, ranking, fallback selection, orchestration, or skill execution.

Examples:

```bash
python scripts/resolve_capabilities.py --output agent-handoff.json
python scripts/resolve_capabilities.py --requires iterate-software-projects --evaluation-mode compatibility
python scripts/resolve_capabilities.py --portable-files required --json
```

The JSON form is versioned by `schemas/capability-resolver-output-v1.schema.json`. Candidates are alphabetically ordered and include the exact constraints they satisfy. Excluded skills are returned separately with the exact constraints they fail. Ambiguous output contracts remain ambiguous; the resolver never chooses a preferred producer.

An empty candidate list is a valid result. Unknown output names, dependency skill names, unsupported evaluation modes, and unsupported capability-index schema versions are explicit errors rather than triggers for broader matching.
