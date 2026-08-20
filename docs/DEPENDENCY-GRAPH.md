# Dependency graph semantics

The repository derives skill composition data from canonical `requires`, `consumes`, and `outputs` frontmatter.

Run `python scripts/generate_repository_metadata.py` to regenerate the README catalog, sync manifest, and dependency graph artifacts. Run the same command with `--check` for read-only validation.

## Hard skill dependencies

Hard dependency edges come only from `requires`. Every required skill must exist, self-dependencies are invalid, duplicate requirements are invalid, and dependency cycles are rejected with an explicit cycle path.

`requires` means that another skill is a mandatory execution dependency. It must not be used merely to express that an artifact is a useful or preferred input.

## Artifact consumption

`consumes` declares concrete artifacts that a skill accepts as inputs without creating a hard skill dependency. Every explicitly consumed artifact must have exactly one declared producer in the repository; unknown, ambiguous, duplicate, or self-produced consumption contracts are invalid.

A skill may therefore have `requires: []` while consuming an artifact produced by another skill. This supports workflows where the artifact can also arrive from an equivalent pre-existing source while preserving explicit producer/consumer traceability for the normal path.

For backward compatibility, outputs of a hard-required skill are still inferred as consumed when the consumer has no explicit `consumes` list. Once a skill declares one or more explicit consumed artifacts, those declarations take precedence over broad legacy inference for that consumer.

## Outputs

`outputs` are declarations of handoff contracts. The graph records all producers. A uniquely named output has one known producer; if several skills declare the same output, the contract is marked ambiguous and no producer-consumer relationship is guessed. Unconsumed outputs are informational and are not automatically errors because terminal user-facing artifacts are valid outputs.

Generated artifacts are `docs/skill-dependency-graph.json` for machine consumption and `docs/SKILL-DEPENDENCIES.md` for human review. Both are deterministic and must not be edited manually.
