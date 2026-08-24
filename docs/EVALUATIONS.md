# Evaluations

Skill evaluations are validated and scored with one offline runner:

```bash
python scripts/evaluate_skills.py
python scripts/evaluate_skills.py --json
```

Each executable suite lives at `skills/<skill>/tests/evaluation.json` and must contain the three case classes `happy-path`, `edge-case`, and `failure-case`. Recorded baselines live under `skills/<skill>/tests/results/`.

When a new evaluation case has no recorded result yet, the normal validation run fails with the exact expected result path and points to the scaffold command:

```bash
python scripts/evaluate_skills.py --init-missing-baselines
```

This command creates only missing `tests/results/<case-id>.json` files and never overwrites an existing baseline. Generated files are deliberately non-passing drafts: required behaviors start with `passed: false`, forbidden behaviors with `observed: true`, evidence fields contain `TODO` markers, and `overall` is `draft`. A maintainer must verify each behavior, replace TODO text with concrete evidence, set the assessments to their verified values, and only then set `overall` to `pass`. This prevents baseline scaffolding from silently approving a new evaluation.

The scaffold command is idempotent. Running it again after all result files exist reports no missing baselines and leaves existing evidence untouched. `--json` may be combined with `--init-missing-baselines` for machine-readable created paths and initialization errors.

A suite may add `skills/<skill>/tests/rubric.json` using `schemas/evaluation-rubric.schema.json`. Rubric schema version 1 defines weighted dimensions, a pass threshold between 0 and 1, and explicit blocking criteria. Existing suites without `rubric.json` remain supported through a deterministic compatibility rubric; the runner reports `compatibilityMode: true` and does not invent skill-specific scoring criteria.

Normal evaluation mode is read-only. Malformed JSON, duplicate case IDs, unsupported schema versions, invalid thresholds, missing required case classes, stale or missing recorded results, failed required behaviors, observed forbidden behaviors, or missing evidence all cause a non-zero exit with file-level diagnostics. The only write mode is the explicit `--init-missing-baselines` scaffold operation described above.

CI runs the unit tests for the runner and then executes `python scripts/evaluate_skills.py`. Evaluation remains offline and does not use production data, network services, or LLM-as-judge behavior.
