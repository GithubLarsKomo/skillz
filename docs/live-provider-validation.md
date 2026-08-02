# Live provider validation

This repository keeps all normal pull-request and push validation offline. Real provider calls are isolated in `.github/workflows/live-provider-validation.yml`, which is triggered only with `workflow_dispatch`.

## GitHub Actions

The manual workflow accepts:

- `mode`: `smoke-only` or `qualify`
- `provider_id`: stable provider identifier used by qualification artifacts
- `endpoint`: OpenAI-compatible chat-completions endpoint
- `model_id`: exact model identifier
- `case_id`: benchmark case used only in `smoke-only` mode
- `use_api_key`: whether bearer authentication is required
- `timeout_seconds`: per-request timeout

When `use_api_key` is enabled, configure the repository or environment secret `CAPABILITY_PROVIDER_API_KEY`. The workflow never writes the secret value into a file, summary, artifact, qualification record, or log intentionally. Provider configuration contains only the fixed environment-variable name.

The workflow has only `contents: read` permission. It does not commit files, open pull requests, upload provider responses, schedule itself, or run on `push`/`pull_request`.

## Validation modes

### smoke-only

Runs exactly one committed benchmark case through the live provider. The provider response must parse as a single `capability-model-interpretation-v1` object and pass the existing model adapter. No provider qualification is produced.

### qualify

Runs every case in `benchmarks/capability-interpretation-v1.json`. Validated responses are held only in process memory as a temporary proposal set and scored by the existing qualification implementation. Qualification is tied to the exact provider id, model id, benchmark fingerprint, proposal-set fingerprint, and committed capability-index fingerprint.

The workflow may write the resulting qualification JSON under `$RUNNER_TEMP` for the duration of the job, but it does not upload or commit it. The visible summary contains only redacted status and fingerprints; it never contains proposal bodies.

## Local invocation

Authenticated endpoint:

```bash
export CAPABILITY_PROVIDER_API_KEY='...'
python scripts/run_live_provider_validation.py \
  --mode smoke-only \
  --provider-id local-openai-compatible \
  --endpoint http://127.0.0.1:11434/v1/chat/completions \
  --model-id example-model \
  --case-id exact-review-output \
  --api-key-env CAPABILITY_PROVIDER_API_KEY
```

Unauthenticated local endpoint:

```bash
NO_PROXY=localhost,127.0.0.1 no_proxy=localhost,127.0.0.1 \
python scripts/run_live_provider_validation.py \
  --mode qualify \
  --provider-id local-openai-compatible \
  --endpoint http://127.0.0.1:11434/v1/chat/completions \
  --model-id example-model \
  --no-auth \
  --qualification-out /tmp/provider-qualification.json
```

The qualification file is optional. If written, it should be treated as evidence for exactly the benchmark and capability-index fingerprints contained in that file; any relevant change requires requalification.

## Security boundary

The regular `openai-compatible` provider path still requires a matching qualification artifact before network invocation. Only this explicit manual qualification collector is permitted to call a provider before qualification exists, because creating the first qualification otherwise would be circular. This exception is isolated from the normal model runner and deterministic resolver pipeline.
