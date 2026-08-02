# Provider qualification registry

The `qualifications/` directory is the reviewed persistence layer for provider/model qualification evidence. It starts empty by design. A live provider is not considered registered merely because a manual qualification run passed.

## Promotion flow

1. Run the manual live provider validation in `qualify` mode or invoke `scripts/run_live_provider_validation.py --mode qualify` locally.
2. Inspect the resulting qualification JSON. It must contain no credentials, endpoint, provider responses, or proposal bodies.
3. Add the qualification JSON under `qualifications/` with a stable file name.
4. Add exactly one matching entry to `qualifications/index.json` containing `providerId`, `modelId`, and the qualification artifact path.
5. Open a normal pull request.
6. `python scripts/qualification_registry.py verify` runs in normal offline CI and rejects stale or malformed evidence.
7. Only after review and merge is the qualification considered registered.

Any change to the committed interpretation benchmark or capability index changes its fingerprint and therefore invalidates previously registered evidence until the provider/model is requalified.

## Registry format

```json
{
  "schemaVersion": 1,
  "entries": [
    {
      "providerId": "example-provider",
      "modelId": "example-model",
      "path": "qualifications/example-provider--example-model.json"
    }
  ]
}
```

Paths must remain under `qualifications/`. Provider/model identity must be unique. The artifact itself must be a successful `capability-model-provider-qualification-v1` result whose provider/model identity and benchmark/index fingerprints exactly match the registry and current repository state.

## Verification and lookup

```bash
python scripts/qualification_registry.py verify
```

Exact lookup:

```bash
python scripts/qualification_registry.py lookup example-provider example-model
```

Lookup is exact only. There are no aliases, ranking, provider fallback, or model fallback.

## Data intentionally excluded

The registry never requires or stores API keys, endpoint URLs, provider response bodies, prompt transcripts, or proposal sets. It stores only qualification evidence needed to prove that a specific provider/model pair passed the pinned benchmark against the pinned capability index.
