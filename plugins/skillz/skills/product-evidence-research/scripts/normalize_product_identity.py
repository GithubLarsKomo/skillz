#!/usr/bin/env python3
from __future__ import annotations
import argparse, json, re, sys

FIELDS = ("manufacturer","productFamily","model","generation","revision","variant","region","sku","mpn","status")

def clean(value):
    if value is None:
        return None
    if not isinstance(value, str):
        raise ValueError("identity fields must be strings or null")
    value = re.sub(r"\s+", " ", value).strip()
    return value or None

def normalize(data):
    if not isinstance(data, dict):
        raise ValueError("input must be a JSON object")
    out = {key: clean(data.get(key)) for key in FIELDS}
    if not out["manufacturer"] or not out["model"]:
        raise ValueError("manufacturer and model are required")
    out["identityConfidence"] = data.get("identityConfidence", "unknown")
    if out["identityConfidence"] not in {"high","medium","low","unknown"}:
        raise ValueError("invalid identityConfidence")
    return out

def main():
    parser = argparse.ArgumentParser(description="Normalize a product identity JSON object.")
    parser.add_argument("input", nargs="?", help="JSON object; stdin is used when omitted")
    args = parser.parse_args()
    raw = args.input if args.input is not None else sys.stdin.read()
    try:
        data = json.loads(raw)
        print(json.dumps(normalize(data), ensure_ascii=False, sort_keys=True, separators=(",",":")))
        return 0
    except (ValueError, json.JSONDecodeError) as exc:
        print(f"ERROR: {exc}", file=sys.stderr)
        return 2

if __name__ == "__main__":
    raise SystemExit(main())
