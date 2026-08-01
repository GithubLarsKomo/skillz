# Machine-readable metadata schemas

The repository exposes explicit versioned contracts for machine-readable capability data.

## Contracts

- `schemas/skill-capability-index-v1.schema.json` validates `docs/skill-capability-index.json`.
- `schemas/capability-query-output-v1.schema.json` validates both stable JSON output shapes emitted by `scripts/query_capabilities.py --json`:
  - a single full skill record;
  - a list result object with `matches` and `count`.

Validation is offline and read-only:

```bash
python scripts/validate_metadata_schemas.py
```

The implementation intentionally supports only the JSON Schema subset used by these repository contracts. It is not a general-purpose JSON Schema engine.

## Compatibility policy

Schema version 1 describes the current public machine-readable boundary.

- Adding an optional field is compatible when existing consumers can ignore it.
- Removing a field, changing a required field, changing a field type, narrowing accepted values, or changing meaning requires a new schema version.
- Generated artifacts must keep their declared `schemaVersion` aligned with the corresponding contract.
- Consumers must fail explicitly on unsupported versions rather than guessing or coercing.
- Query output remains an inspection interface only. These schemas do not authorize ranking, natural-language matching, routing, orchestration, tool execution, or skill execution.

## CI

CI separately tests the validator implementation and validates the committed capability index plus representative single-skill and list query outputs. This keeps validator bugs distinct from data-contract regressions.
