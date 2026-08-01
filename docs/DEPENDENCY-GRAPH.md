# Dependency graph semantics

The repository derives skill composition data from canonical `requires` and `outputs` frontmatter.

Run `python scripts/generate_repository_metadata.py` to regenerate the README catalog, sync manifest, and dependency graph artifacts. Run the same command with `--check` for read-only validation.

Hard dependency edges come only from `requires`. Every required skill must exist, self-dependencies are invalid, duplicate requirements are invalid, and dependency cycles are rejected with an explicit cycle path.

`outputs` are declarations of handoff contracts. The graph records all producers. A uniquely named output has one known producer; if several skills declare the same output, the contract is marked ambiguous and no producer-consumer relationship is guessed. Orphan outputs are informational and are not automatically errors.

Generated artifacts are `docs/skill-dependency-graph.json` for machine consumption and `docs/SKILL-DEPENDENCIES.md` for human review. Both are deterministic and must not be edited manually.
