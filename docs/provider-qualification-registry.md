# Provider qualification registry

The `qualifications/` directory is the reviewed persistence layer for provider/model qualification evidence. It starts empty by design. A live provider is not considered registered merely because a manual qualification run passed.

## Promotion flow

1. Run the manual **Live provider validation** workflow in `qualify` mode, or invoke `scripts/run_live_provider_validation.py --mode qualify` locally with both `--qualification-out` and `--provider-config-out`.
2. A successful GitHub workflow uploads a short-lived `provider-promotion-<identity-key>` artifact. The opaque 24-hex-character identity key is derived deterministically from the exact `providerId` + `modelId` pair; the exact identities themselves remain unchanged inside the bundle. The artifact contains exactly `provider-config.json`, `qualification.json`, and `manifest.json`.
3. Download and inspect the artifact. It contains the secrets-free provider configuration and qualification-v2 evidence only; it must contain no credential value, Authorization header, provider response, proposal body, or source prompt transcript.
4. From the repository root, dry-run the local promotion preparer:

```bash
python scripts/prepare_registry_promotion.py /path/to/extracted/provider-promotion-bundle
```

The dry run validates the bundle manifest, exact provider/model identity, provider-config fingerprint, current benchmark fingerprint, current capability-index fingerprint, target paths, and duplicate registry identities. It prints the four files that would change without modifying the repository.

5. After inspection, apply the prepared change explicitly:

```bash
python scripts/prepare_registry_promotion.py /path/to/extracted/provider-promotion-bundle --apply
```

`--apply` writes the provider config and qualification artifact under opaque identity-key filenames, plus `providers/index.json` and `qualifications/index.json`. It then verifies both complete registries and resolves the exact provider/model pair. If post-write verification fails, all four files are restored to their pre-apply state.

6. Inspect the resulting local diff and open a normal pull request. The preparer never commits, pushes, opens a PR, calls a provider, or accesses credentials.
7. Normal offline CI verifies both registries and the `providerConfigSha256` binding. Only after review and merge is the provider/model pair considered registered.

Any change to the committed interpretation benchmark or capability index invalidates previously registered evidence. Changing the bound secrets-free provider configuration (including endpoint, timeout, auth mode/environment-variable name, provider id, or model id) also invalidates the qualification. Credential values themselves are never part of the fingerprint.

## Identity keys and filenames

Provider and model identifiers are canonical data, not filenames. They may contain characters such as `:`, `/`, dots, or provider-specific model tags. `scripts/provider_identity_key.py` derives a deterministic 24-hex-character key from the exact identity pair. Promotion artifact names and provider/qualification filenames use only that key; registry entries and runtime lookup continue to use the exact original `providerId` and `modelId`.

The key is never used as an alias or lookup fallback. Changing either exact identity changes the key and the qualification binding.

## Secrets-free endpoint constraint

The shared OpenAI-compatible provider config validator only accepts `http` or `https` endpoints with a hostname and optional port/path. Endpoint URLs may not contain URL userinfo, query parameters, or fragments. This keeps credential-bearing strings such as `https://user:password@host/...` or `...?api_key=...` out of live requests, qualification fingerprints, promotion bundles, and reviewed registries.

Providers that genuinely require query parameters are not represented by embedding those parameters in `endpoint`; they need an explicit future adapter/config extension with its own secrets-free contract and tests.

## Registry format

```json
{
  "schemaVersion": 1,
  "entries": [
    {
      "providerId": "example-provider",
      "modelId": "org/example-model:tag",
      "path": "qualifications/<identity-key>.json"
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
python scripts/qualification_registry.py lookup example-provider 'org/example-model:tag'
```

Lookup is exact only. There are no aliases, ranking, provider fallback, model fallback, or identity-key lookup.

## Promotion bundle builder

For a local successful qualification:

```bash
python scripts/build_provider_promotion_bundle.py \
  provider-config.json qualification.json provider-promotion-bundle
```

The builder rejects unqualified evidence, identity mismatch, or provider-config fingerprint drift before writing files.

## Data intentionally excluded

The qualification registry never stores API keys, provider response bodies, prompt transcripts, or proposal sets. Endpoint and other secrets-free runtime configuration live separately in the reviewed `providers/` registry and are bound cryptographically to qualification-v2 evidence through `providerConfigSha256`.
