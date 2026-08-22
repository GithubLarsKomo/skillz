#!/usr/bin/env python3
from __future__ import annotations

import json
import os
from datetime import datetime, timezone
from pathlib import Path
from typing import Callable

import openai_compatible_provider as provider
import validate_sport_p1_contracts as p1_validator
import validate_sport_p2_contracts as p2_validator

ROOT = Path(__file__).resolve().parents[1]
RUNTIME_ID = "skillz-sport-specialist-runtime/1"

REGISTRY = {
    "strength_power_plan": {"layer": "p1", "definition": "strengthPowerPlan", "kind": "strength-power-plan", "skill": "sport-strength-power-programming"},
    "endurance_plan": {"layer": "p1", "definition": "endurancePlan", "kind": "endurance-plan", "skill": "sport-endurance-programming"},
    "recovery_state": {"layer": "p1", "definition": "recoveryState", "kind": "recovery-state", "skill": "sport-recovery-sleep"},
    "fueling_plan": {"layer": "p1", "definition": "fuelingPlan", "kind": "fueling-plan", "skill": "sport-nutrition-fueling"},
    "energy_availability_risk": {"layer": "p1", "definition": "energyAvailabilityRisk", "kind": "energy-availability-risk", "skill": "sport-nutrition-fueling"},
    "rehab_progression": {"layer": "p1", "definition": "rehabProgression", "kind": "rehab-progression", "skill": "sport-injury-rehabilitation"},
    "return_after_illness_plan": {"layer": "p1", "definition": "returnAfterIllnessPlan", "kind": "return-after-illness-plan", "skill": "sport-return-after-illness"},
    "testing_plan": {"layer": "p1", "definition": "testingPlan", "kind": "testing-plan", "skill": "sport-testing-battery"},
    "adaptation_analysis": {"layer": "p1", "definition": "adaptationAnalysis", "kind": "adaptation-analysis", "skill": "sport-adaptation-analysis"},
    "performance_psychology_plan": {"layer": "p2", "definition": "performancePsychologyPlan", "kind": "performance-psychology-plan", "skill": "sport-performance-psychology"},
    "mental_health_routing": {"layer": "p2", "definition": "mentalHealthRouting", "kind": "mental-health-routing", "skill": "sport-mental-health-routing"},
    "training_music_profile": {"layer": "p2", "definition": "trainingMusicProfile", "kind": "training-music-profile", "skill": "sport-training-music"},
    "environment_adjustment": {"layer": "p2", "definition": "environmentAdjustment", "kind": "environment-adjustment", "skill": "sport-environment-travel"},
}

REQUEST_FIELDS = {"athlete_id", "trigger", "artifact_type", "skill", "contract", "snapshot"}
CONTRACT_FIELDS = {"layer", "version", "definition"}


def canonical_json(value: object) -> str:
    return json.dumps(value, ensure_ascii=False, sort_keys=True, separators=(",", ":"))


def validate_runtime_request(value: object) -> dict:
    if not isinstance(value, dict):
        raise ValueError("runtime request root must be an object")
    if set(value) != REQUEST_FIELDS:
        raise ValueError("runtime request has invalid fields")
    athlete_id = value.get("athlete_id")
    trigger = value.get("trigger")
    artifact_type = value.get("artifact_type")
    skill = value.get("skill")
    contract = value.get("contract")
    snapshot = value.get("snapshot")
    if not isinstance(athlete_id, str) or not athlete_id.strip():
        raise ValueError("athlete_id must be a non-empty string")
    if not isinstance(trigger, str) or not trigger.strip():
        raise ValueError("trigger must be a non-empty string")
    if not isinstance(artifact_type, str) or artifact_type not in REGISTRY:
        raise ValueError("unsupported artifact_type")
    if not isinstance(snapshot, dict):
        raise ValueError("snapshot must be an object")
    descriptor = REGISTRY[artifact_type]
    if skill != descriptor["skill"]:
        raise ValueError("skill does not match artifact_type registry")
    if not isinstance(contract, dict) or set(contract) != CONTRACT_FIELDS:
        raise ValueError("contract has invalid fields")
    if contract.get("layer") != descriptor["layer"] or contract.get("version") != 1 or contract.get("definition") != descriptor["definition"]:
        raise ValueError("contract does not match artifact_type registry")
    return value


def load_provider_config(environ: dict[str, str] | None = None) -> dict:
    env = os.environ if environ is None else environ
    config_path = env.get("SPORT_RUNTIME_PROVIDER_CONFIG", "").strip()
    if config_path:
        try:
            value = json.loads(Path(config_path).read_text(encoding="utf-8"))
        except (OSError, json.JSONDecodeError) as exc:
            raise ValueError(f"cannot read SPORT_RUNTIME_PROVIDER_CONFIG: {exc}") from exc
        return provider.validate_config(value)

    timeout_raw = env.get("SPORT_PROVIDER_TIMEOUT_SECONDS", "60").strip()
    try:
        timeout = int(timeout_raw)
    except ValueError as exc:
        raise ValueError("SPORT_PROVIDER_TIMEOUT_SECONDS must be an integer") from exc
    api_key_env = env.get("SPORT_PROVIDER_API_KEY_ENV", "").strip() or None
    value = {
        "schemaVersion": 1,
        "providerId": env.get("SPORT_PROVIDER_ID", "").strip(),
        "endpoint": env.get("SPORT_PROVIDER_ENDPOINT", "").strip(),
        "modelId": env.get("SPORT_MODEL_ID", "").strip(),
        "apiKeyEnv": api_key_env,
        "timeoutSeconds": timeout,
    }
    return provider.validate_config(value)


def load_contract_excerpt(descriptor: dict) -> dict:
    schema_path = ROOT / "schemas" / f"sport-athlete-management-{descriptor['layer']}-v1.schema.json"
    try:
        schema = json.loads(schema_path.read_text(encoding="utf-8"))
    except (OSError, json.JSONDecodeError) as exc:
        raise ValueError(f"cannot read canonical sport contract: {exc}") from exc
    defs = schema.get("$defs")
    if not isinstance(defs, dict) or descriptor["definition"] not in defs or "commonEnvelope" not in defs:
        raise ValueError("canonical sport contract is missing required definitions")
    return {
        "commonEnvelope": defs["commonEnvelope"],
        descriptor["definition"]: defs[descriptor["definition"]],
    }


def load_skill_text(descriptor: dict) -> str:
    path = ROOT / "skills" / descriptor["skill"] / "SKILL.md"
    try:
        text = path.read_text(encoding="utf-8")
    except OSError as exc:
        raise ValueError(f"cannot read registered skill: {exc}") from exc
    if not text.strip():
        raise ValueError("registered skill is empty")
    return text


def build_provider_body(request: dict, provider_config: dict) -> dict:
    request = validate_runtime_request(request)
    provider_config = provider.validate_config(provider_config)
    descriptor = REGISTRY[request["artifact_type"]]
    skill_text = load_skill_text(descriptor)
    contract_excerpt = load_contract_excerpt(descriptor)
    system = (
        f"Execute exactly the registered Skillz sport skill {descriptor['skill']} for one canonical artifact. "
        "Return exactly one JSON object representing the artifact and nothing else: no Markdown, no commentary, no chain-of-thought. "
        "Follow SKILL.md and the supplied canonical contract. Never invent missing measurements; put uncertainty into uncertainties. "
        "Preserve safety/medical/mental-health routing boundaries. Do not add plan mutations outside the requested artifact contract.\n\n"
        f"--- SKILL.md ---\n{skill_text}\n--- END SKILL.md ---"
    )
    user = {
        "artifact_type": request["artifact_type"],
        "trigger": request["trigger"],
        "athlete_id": request["athlete_id"],
        "contract": request["contract"],
        "contract_schema": contract_excerpt,
        "snapshot": request["snapshot"],
    }
    return {
        "model": provider_config["modelId"],
        "temperature": 0,
        "messages": [
            {"role": "system", "content": system},
            {"role": "user", "content": canonical_json(user)},
        ],
    }


def parse_provider_artifact(raw: bytes | str) -> dict:
    try:
        data = json.loads(raw.decode("utf-8") if isinstance(raw, bytes) else raw)
    except (UnicodeDecodeError, json.JSONDecodeError) as exc:
        raise ValueError(f"provider response is not valid JSON: {exc}") from exc
    try:
        content = data["choices"][0]["message"]["content"]
    except (TypeError, KeyError, IndexError) as exc:
        raise ValueError("provider response does not contain choices[0].message.content") from exc
    if isinstance(content, dict):
        artifact = content
    elif isinstance(content, str):
        try:
            artifact = json.loads(content)
        except json.JSONDecodeError as exc:
            raise ValueError(f"provider message content is not valid JSON: {exc}") from exc
    else:
        raise ValueError("provider message content must be a JSON object or JSON string")
    if not isinstance(artifact, dict):
        raise ValueError("provider artifact root must be an object")
    return artifact


def validate_artifact(artifact_type: str, artifact: dict) -> None:
    descriptor = REGISTRY[artifact_type]
    errors = p1_validator.validate(descriptor["kind"], artifact) if descriptor["layer"] == "p1" else p2_validator.validate(descriptor["kind"], artifact)
    if errors:
        raise ValueError("artifact contract validation failed: " + "; ".join(errors))


def normalize_artifact(request: dict, artifact: dict, *, now: datetime | None = None) -> dict:
    normalized = dict(artifact)
    normalized["schema_version"] = 1
    normalized["athlete_id"] = request["athlete_id"]
    moment = datetime.now(timezone.utc) if now is None else now.astimezone(timezone.utc)
    normalized["generated_at"] = moment.isoformat().replace("+00:00", "Z")
    validate_artifact(request["artifact_type"], normalized)
    return normalized


def invoke(
    request: dict,
    provider_config: dict,
    *,
    transport: Callable[[str, bytes, dict[str, str], int], bytes] = provider.default_transport,
    environ: dict[str, str] | None = None,
    revision: str | None = None,
    now: datetime | None = None,
) -> dict:
    request = validate_runtime_request(request)
    provider_config = provider.validate_config(provider_config)
    body = canonical_json(build_provider_body(request, provider_config)).encode("utf-8")
    headers = provider.build_headers(provider_config, environ)
    raw = transport(provider_config["endpoint"], body, headers, provider_config["timeoutSeconds"])
    artifact = normalize_artifact(request, parse_provider_artifact(raw), now=now)
    env = os.environ if environ is None else environ
    effective_revision = (revision or env.get("SKILLZ_REVISION", "").strip() or "unknown")
    return {
        "artifact": artifact,
        "provenance": {
            "skillz_revision": effective_revision,
            "runtime": RUNTIME_ID,
            "model": provider_config["modelId"],
            "provider": provider_config["providerId"],
        },
    }
