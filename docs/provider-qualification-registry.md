# Provider qualification registry

The `qualifications/` directory is the reviewed persistence layer for provider/model qualification evidence. It starts empty by design. A live provider is not considered registered merely because a manual qualification run passed.

## Promotion flow

1. Run the manual **Live provider validation** workflow in `qualify` mode, or invoke `scripts/run_live_provider_validation.py --mode qualify` locally with both `--qualification-out` and `--provider-config-out`.
2. A successful GitHub workflow uploads a short-lived `provider-promotion-<provider>-<model>` artifact. It contains exactly `provider-config.json`, `qualification.json`, and `manifest.json`.
3. Download and inspect the artifact. It contains the secrets-free provider configuration and qualification-v2 evidence only; it must contain no credential value, Authorization header, provider response, proposal body, or source prompt transcript.
4. Copy the provider config to `providers/` and add its exact `providerId` + `modelId` entry to `providers/index.json`.
5. Copy the qualification to `qualifications/` and add its matching entry to `qualifications/index.json`.
6. Open a normal pull request. Do not automate registry mutation from the live workflow.
7. Normal offline CI verifies both registries and the `providerConfigSha256` binding. Only after review and merge is the provider/model pair considered registered.

Any change to the committed interpretation benchmark or capability index invalidates previously registered evidence. Changing the bound secrets-free provider configuration (including endpoint, timeout, auth mode/environment-variable name, provider id, or model id) also invalidates the qualification. Credential values themselves are never part of the fingerprint.

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

Paths must remain under `qualifications/`. Provider/model identity must be unique. The artifact itself must be a successful qualification schema v2 result whose provider/model identity, provider-config fingerprint, benchmark fingerprint, and capability-index fingerprint match the reviewed repository state.

## Verification and lookup

```bash
python scripts/qualification_registry.py verify
```

Exact lookup:

```bash
python scripts/qualification_registry.py lookup example-provider example-model
```

Lookup is exact only. There are no aliases, ranking, provider fallback, or model fallback.

## Promotion bundle builder

For a local successful qualification:

```bash
python scripts/build_provider_promotion_bundle.py \
  provider-config.json qualification.json provider-promotion-bundle
```

The builder rejects unqualified evidence, identity mismatch, or provider-config fingerprint drift before writing files.

## Data intentionally excluded

The qualification registry never stores API keys, provider response bodies, prompt transcripts, or proposal sets. Endpoint and other secrets-free runtime configuration live separately in the reviewed `providers/` registry and are bound cryptographically to qualification-v2 evidence through `providerConfigSha256`.
