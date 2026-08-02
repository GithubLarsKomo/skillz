#!/usr/bin/env python3
from __future__ import annotations

import json
import os
import urllib.error
import urllib.request
from pathlib import Path

from adapt_model_interpretation import adapt
from build_model_interpretation_request import canonical_json, validate_index
from qualify_model_provider import fingerprint
from run_model_interpretation import validate_request
from score_capability_interpretations import load_json

CONFIG_SCHEMA_VERSION = 1
QUALIFICATION_SCHEMA_VERSION = 1


def validate_config(config: object) -> dict:
    required = {"schemaVersion", "providerId", "endpoint", "modelId", "apiKeyEnv", "timeoutSeconds"}
    if not isinstance(config, dict) or set(config) != required:
        raise ValueError("provider config has invalid fields")
    if config.get("schemaVersion") != CONFIG_SCHEMA_VERSION:
        raise ValueError(f"unsupported provider config schemaVersion {config.get('schemaVersion')!r}")
    for field in ("providerId", "endpoint", "modelId"):
        if not isinstance(config.get(field), str) or not config[field].strip():
            raise ValueError(f"provider config {field} must be non-empty")
    if config["apiKeyEnv"] is not None and (not isinstance(config["apiKeyEnv"], str) or not config["apiKeyEnv"].strip()):
        raise ValueError("provider config apiKeyEnv must be null or a non-empty string")
    if not isinstance(config["timeoutSeconds"], int) or isinstance(config["timeoutSeconds"], bool) or config["timeoutSeconds"] < 1:
        raise ValueError("provider config timeoutSeconds must be a positive integer")
    if not config["endpoint"].startswith(("http://", "https://")):
        raise ValueError("provider config endpoint must use http or https")
    return config


def verify_qualification(config: dict, qualification: object, benchmark: object, capability_index: object) -> dict:
    config = validate_config(config)
    capability_index = validate_index(capability_index)
    if not isinstance(qualification, dict):
        raise ValueError("qualification root must be an object")
    if qualification.get("schemaVersion") != QUALIFICATION_SCHEMA_VERSION:
        raise ValueError("unsupported qualification schemaVersion")
    if qualification.get("qualified") is not True:
        raise ValueError("provider/model is not qualified")
    if qualification.get("providerId") != config["providerId"]:
        raise ValueError("qualification providerId does not match provider config")
    if qualification.get("modelId") != config["modelId"]:
        raise ValueError("qualification modelId does not match provider config")
    if qualification.get("benchmarkSha256") != fingerprint(benchmark):
        raise ValueError("qualification benchmark fingerprint is stale or mismatched")
    if qualification.get("capabilityIndexSha256") != fingerprint(capability_index):
        raise ValueError("qualification capability-index fingerprint is stale or mismatched")
    return qualification


def render_request_body(request: dict, config: dict) -> dict:
    request = validate_request(request)
    config = validate_config(config)
    return {
        "model": config["modelId"],
        "temperature": 0,
        "messages": [
            {
                "role": "system",
                "content": "Return exactly one JSON object matching capability-model-interpretation-v1. Do not add prose or provenance/admission controls.",
            },
            {"role": "user", "content": canonical_json(request)},
        ],
    }


def build_headers(config: dict, environ: dict[str, str] | None = None) -> dict[str, str]:
    config = validate_config(config)
    env = os.environ if environ is None else environ
    headers = {"Content-Type": "application/json", "Accept": "application/json"}
    if config["apiKeyEnv"] is not None:
        token = env.get(config["apiKeyEnv"])
        if not token:
            raise ValueError(f"missing API key environment variable: {config['apiKeyEnv']}")
        headers["Authorization"] = f"Bearer {token}"
    return headers


def default_transport(endpoint: str, body: bytes, headers: dict[str, str], timeout_seconds: int) -> bytes:
    req = urllib.request.Request(endpoint, data=body, headers=headers, method="POST")
    try:
        with urllib.request.urlopen(req, timeout=timeout_seconds) as response:
            return response.read()
    except urllib.error.HTTPError as exc:
        raise ValueError(f"provider HTTP error: {exc.code}") from exc
    except urllib.error.URLError as exc:
        raise ValueError(f"provider transport error: {exc.reason}") from exc
    except TimeoutError as exc:
        raise ValueError("provider transport timeout") from exc


def parse_provider_response(raw: bytes | str) -> dict:
    try:
        data = json.loads(raw.decode("utf-8") if isinstance(raw, bytes) else raw)
    except (UnicodeDecodeError, json.JSONDecodeError) as exc:
        raise ValueError(f"provider response is not valid JSON: {exc}") from exc
    try:
        content = data["choices"][0]["message"]["content"]
    except (TypeError, KeyError, IndexError) as exc:
        raise ValueError("provider response does not contain choices[0].message.content") from exc
    if isinstance(content, dict):
        proposal = content
    elif isinstance(content, str):
        try:
            proposal = json.loads(content)
        except json.JSONDecodeError as exc:
            raise ValueError(f"provider message content is not valid JSON: {exc}") from exc
    else:
        raise ValueError("provider message content must be a JSON object or JSON string")
    if not isinstance(proposal, dict):
        raise ValueError("provider proposal root must be an object")
    adapt(proposal)
    return proposal


def invoke(request: dict, config: dict, qualification: dict, benchmark: dict, capability_index: dict, *, transport=default_transport, environ: dict[str, str] | None = None) -> dict:
    verify_qualification(config, qualification, benchmark, capability_index)
    body = canonical_json(render_request_body(request, config)).encode("utf-8")
    headers = build_headers(config, environ)
    raw = transport(config["endpoint"], body, headers, config["timeoutSeconds"])
    return parse_provider_response(raw)


def load(path: Path) -> dict:
    return load_json(path)
