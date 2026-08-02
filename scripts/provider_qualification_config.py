from __future__ import annotations

import hashlib

from model_interpretation_request_contract import canonical_json


def projection(provider_id: str, model_id: str, provider_config: dict | None = None) -> dict:
    if not isinstance(provider_id, str) or not provider_id.strip():
        raise ValueError("provider id must be non-empty")
    if not isinstance(model_id, str) or not model_id.strip():
        raise ValueError("model id must be non-empty")
    if provider_config is None:
        return {"kind": "fixture", "providerId": provider_id, "modelId": model_id}
    required = {"schemaVersion", "providerId", "endpoint", "modelId", "apiKeyEnv", "timeoutSeconds"}
    if not isinstance(provider_config, dict) or set(provider_config) != required:
        raise ValueError("provider config has invalid fields")
    if provider_config.get("schemaVersion") != 1:
        raise ValueError("unsupported provider config schemaVersion")
    if provider_config.get("providerId") != provider_id:
        raise ValueError("provider config providerId does not match qualification identity")
    if provider_config.get("modelId") != model_id:
        raise ValueError("provider config modelId does not match qualification identity")
    endpoint = provider_config.get("endpoint")
    if not isinstance(endpoint, str) or not endpoint.strip():
        raise ValueError("provider config endpoint must be non-empty")
    timeout = provider_config.get("timeoutSeconds")
    if not isinstance(timeout, int) or isinstance(timeout, bool) or timeout < 1:
        raise ValueError("provider config timeoutSeconds must be a positive integer")
    api_key_env = provider_config.get("apiKeyEnv")
    if api_key_env is not None and (not isinstance(api_key_env, str) or not api_key_env.strip()):
        raise ValueError("provider config apiKeyEnv must be null or a non-empty string")
    return {
        "kind": "openai-compatible",
        "providerId": provider_id,
        "modelId": model_id,
        "endpoint": endpoint,
        "timeoutSeconds": timeout,
        "auth": {"kind": "bearer-env" if api_key_env else "none", "environmentVariable": api_key_env},
    }


def fingerprint(provider_id: str, model_id: str, provider_config: dict | None = None) -> str:
    value = projection(provider_id, model_id, provider_config)
    return hashlib.sha256(canonical_json(value).encode("utf-8")).hexdigest()
