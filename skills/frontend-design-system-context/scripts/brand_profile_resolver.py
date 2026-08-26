#!/usr/bin/env python3
from __future__ import annotations

import argparse
import json
import re
from pathlib import Path

PROFILE_DIR = Path(__file__).resolve().parents[1] / "references" / "brand-profiles"
PROFILE_FILES = {
    "euroimmun-corporate": PROFILE_DIR / "euroimmun.json",
    "sport-performance": PROFILE_DIR / "sport-performance.json",
}


def _norm(value: str | None) -> str:
    return " ".join((value or "").casefold().split())


def _load(profile_id: str) -> dict:
    path = PROFILE_FILES[profile_id]
    data = json.loads(path.read_text(encoding="utf-8"))
    data["_profile_path"] = str(path)
    return data


def _explicit_builtin_brand(explicit_brand: str) -> str | None:
    normalized = _norm(explicit_brand)
    if not normalized:
        return None
    for profile_id in ("euroimmun-corporate", "sport-performance"):
        profile = _load(profile_id)
        aliases = {_norm(alias) for alias in profile["matching"].get("explicit_brand_aliases", [])}
        if normalized in aliases:
            return profile_id
    return None


def _is_sport_context(*, context: str, skill_slug: str) -> bool:
    normalized_context = _norm(context)
    normalized_slug = _norm(skill_slug)
    sport = _load("sport-performance")
    if any(normalized_slug.startswith(_norm(prefix)) for prefix in sport["matching"]["skill_slug_prefixes"]):
        return True
    return any(
        re.search(rf"(?<!\w){re.escape(_norm(term))}(?!\w)", normalized_context)
        for term in sport["matching"]["context_terms"]
    )


def resolve_profile_id(*, context: str = "", skill_slug: str = "", explicit_brand: str | None = None) -> str | None:
    """Resolve a built-in profile using binding domain standards.

    Precedence:
    1. Explicit built-in brand alias.
    2. EUROIMMUN corporate context.
    3. Sport skill/domain context -> binding sport-performance profile.
    4. Explicit unrelated brand outside built-in domains -> no built-in profile.
    5. No built-in profile.

    An unrelated explicit brand name must not suppress the binding Sport Performance
    palette for a Sport application. A higher-priority corporate profile such as
    EUROIMMUN still wins when its context is present.
    """
    explicit_builtin = _explicit_builtin_brand(explicit_brand or "")
    if explicit_builtin:
        return explicit_builtin

    normalized_context = _norm(context)
    if "euroimmun" in normalized_context:
        return "euroimmun-corporate"

    if _is_sport_context(context=context, skill_slug=skill_slug):
        return "sport-performance"

    if _norm(explicit_brand):
        return None

    return None


def resolve_profile(*, context: str = "", skill_slug: str = "", explicit_brand: str | None = None) -> dict | None:
    profile_id = resolve_profile_id(context=context, skill_slug=skill_slug, explicit_brand=explicit_brand)
    return _load(profile_id) if profile_id else None


def main() -> int:
    parser = argparse.ArgumentParser(description="Resolve built-in Skillz brand profiles for Impeccable design work.")
    parser.add_argument("--context", default="")
    parser.add_argument("--skill-slug", default="")
    parser.add_argument("--explicit-brand")
    args = parser.parse_args()
    profile = resolve_profile(context=args.context, skill_slug=args.skill_slug, explicit_brand=args.explicit_brand)
    print(json.dumps(profile, indent=2, ensure_ascii=False) if profile else "null")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
