# Evaluations

Skill evaluations are validated and scored with one offline runner:

```bash
python scripts/evaluate_skills.py
python scripts/evaluate_skills.py --json
```

Each executable suite lives at `skills/<skill>/tests/evaluation.json` and must contain the three case classes `happy-path`, `edge-case`, and `failure-case`. Recorded baselines live under `skills/<skill>/tests/results/`.

A suite may add `skills/<skill>/tests/rubric.json` using `schemas/evaluation-rubric.schema.json`. Rubric schema version 1 defines weighted dimensions, a pass threshold between 0 and 1, and explicit blocking criteria. Existing suites without `rubric.json` remain supported through a deterministic compatibility rubric; the runner reports `compatibilityMode: true` and does not invent skill-specific scoring criteria.

The JSON form is stable for unchanged repository inputs and is intended for CI and later maturity scoring. The runner is read-only: malformed JSON, duplicate case IDs, unsupported schema versions, invalid thresholds, missing required case classes, stale recorded results, failed required behaviors, observed forbidden behaviors, or missing evidence all cause a non-zero exit with file-level diagnostics.

CI runs the unit tests for the runner and then executes `python scripts/evaluate_skills.py`. Evaluation remains offline and does not use production data, network services, or LLM-as-judge behavior.
