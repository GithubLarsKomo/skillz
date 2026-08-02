#!/usr/bin/env python3
from __future__ import annotations

import argparse
import hashlib
import json


def canonical_json(value: object) -> str:
    return json.dumps(value, ensure_ascii=False, sort_keys=True, separators=(",", ":"))


def identity_key(provider_id: str, model_id: str) -> str:
    if not isinstance(provider_id, str) or not provider_id.strip():
        raise ValueError("provider id must be non-empty")
    if not isinstance(model_id, str) or not model_id.strip():
        raise ValueError("model id must be non-empty")
    payload = {"providerId": provider_id, "modelId": model_id}
    return hashlib.sha256(canonical_json(payload).encode("utf-8")).hexdigest()[:24]


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(description="Build a filesystem-safe deterministic key from exact provider/model identity.")
    parser.add_argument("provider_id")
    parser.add_argument("model_id")
    args = parser.parse_args(argv)
    try:
        print(identity_key(args.provider_id, args.model_id))
    except ValueError as exc:
        parser.error(str(exc))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
