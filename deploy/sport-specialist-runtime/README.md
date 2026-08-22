# Sport Specialist Runtime

This service executes the registered Sport Athlete Management P1/P2 skills for `sport-athlete-management-app`. Skillz remains the owner of reasoning; the product remains the owner of athlete identity, persistence, audit and final plan application.

## Interface

- `GET /healthz`
- `POST /reason`

`/reason` accepts only a registered `artifact_type` together with its exact owning skill and canonical contract definition. Arbitrary skill names or paths are rejected before any model call.

## Coolify / Hetzner

Create a Dockerfile-based service from this repository and set the Dockerfile location to:

```text
deploy/sport-specialist-runtime/Dockerfile
```

Use port `8080`. Prefer an internal service network; the runtime does not need a public hostname when the athlete app can resolve it by internal service name.

Recommended application environment:

```text
SKILLZ_SPECIALIST_URL=http://<internal-runtime-service>:8080/reason
SKILLZ_SPECIALIST_TOKEN=<same value as SPORT_RUNTIME_BEARER_TOKEN>
SKILLZ_SOURCE_REVISION=<deployed Skillz SHA>
```

Runtime environment is documented in `.env.example`.

## Provider examples

For an internal Ollama/vLLM/OpenAI-compatible endpoint, configure its chat-completions URL, model ID and timeout through `SPORT_PROVIDER_*`. No API-key variable is needed when that internal endpoint does not require authentication.

For a provider that requires a token, set `SPORT_PROVIDER_API_KEY_ENV` to the **name** of a secret environment variable and define that variable in Coolify. The provider token is read only by the runtime container and never returned to the athlete application.

## Request contract

The athlete app sends one selected specialist per request:

```json
{
  "athlete_id": "athlete-123",
  "trigger": "key_session_completed",
  "artifact_type": "recovery_state",
  "skill": "sport-recovery-sleep",
  "contract": {
    "layer": "p1",
    "version": 1,
    "definition": "recoveryState"
  },
  "snapshot": {}
}
```

The runtime loads `skills/<registered-skill>/SKILL.md` and the corresponding canonical schema definition from `schemas/`. The model receives no capability to choose another skill or contract.

## Output gate

The model must return exactly one JSON object for the requested artifact. The runtime then:

1. binds `schema_version=1`;
2. binds the authoritative request `athlete_id`;
3. assigns the runtime UTC `generated_at` timestamp;
4. runs the existing deterministic P1/P2 validator;
5. rejects unsafe or structurally invalid output;
6. wraps the artifact with provider/model/runtime/Skillz-revision provenance.

Missing substantive data are not filled by code. The model must express uncertainty and safety flags through the canonical artifact fields; otherwise validation fails.

## Safety boundaries

The deterministic validators remain the final gate after model generation. Examples of rejected output include:

- opaque `readiness_score` in `recovery_state`;
- ACWR encoded as injury probability;
- illness red flags without required medical routing;
- P2 direct plan mutation fields;
- an urgent mental-health route that does not pause performance optimization and require immediate support routing;
- BPM used as a mandatory physiological training zone.

The service returns HTTP 502 for provider/model/contract failures. It does not invent a fallback artifact.

## Logging and privacy

The HTTP server logs request path/status via the standard request line but does not serialize request bodies, headers, snapshots or provider content. Do not add body-level logging in production because snapshots can contain health-adjacent athlete data.

## Deployment verification

1. Build the Docker image from the runtime Dockerfile.
2. Confirm `/healthz` returns the configured provider/model and the intended `SKILLZ_REVISION`.
3. Verify a request without the bearer token fails when `SPORT_RUNTIME_BEARER_TOKEN` is enabled.
4. From the athlete app private network, generate one low-risk explicit artifact such as `training_music_profile`.
5. Confirm the product stores artifact v1 plus runtime/model/provider/Skillz provenance.
6. Generate it again and confirm v2 exists while v1 remains.
7. Break the provider endpoint temporarily and verify the product records a failed reasoning run without a new artifact.
