from __future__ import annotations

import json

REQUEST_SCHEMA_VERSION = 1
REQUEST_RESPONSE_SCHEMA = "capability-model-interpretation-v1"


def canonical_json(value: object) -> str:
    return json.dumps(value, ensure_ascii=False, sort_keys=True, separators=(",", ":"))


def validate_request(request: object) -> dict:
    required = {
        "schemaVersion", "requestId", "sourceText", "capabilityIndex",
        "availableCapabilities", "availableOutputs", "responseSchema", "controlRules",
    }
    if not isinstance(request, dict) or set(request) != required:
        raise ValueError("interpretation request has invalid fields")
    if request.get("schemaVersion") != REQUEST_SCHEMA_VERSION:
        raise ValueError(f"unsupported interpretation request schemaVersion {request.get('schemaVersion')!r}")
    if not isinstance(request.get("requestId"), str) or not request["requestId"]:
        raise ValueError("requestId must be a non-empty string")
    if request.get("responseSchema") != REQUEST_RESPONSE_SCHEMA:
        raise ValueError(f"responseSchema must be {REQUEST_RESPONSE_SCHEMA!r}")
    return request
