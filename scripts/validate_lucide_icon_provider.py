#!/usr/bin/env python3
"""Validate the Skillz Lucide provider against its pinned upstream snapshot.

Offline checks are deterministic and run without network access. With
``--check-upstream`` the validator fetches the immutable ``icons`` Git subtree
pinned in ``docs/icons/lucide/upstream-snapshot.json`` and proves that every
icon name referenced by the semantic overlay exists in that exact Lucide
revision.
"""

from __future__ import annotations

import argparse
import json
import os
import sys
import urllib.error
import urllib.request
from pathlib import Path
from typing import Any

ROOT = Path(__file__).resolve().parents[1]
CATALOG_PATH = ROOT / "docs/icons/lucide/icon-semantic-catalog.json"
SNAPSHOT_PATH = ROOT / "docs/icons/lucide/upstream-snapshot.json"
REGISTRY_PATH = ROOT / "skills/icon-selector/references/provider-registry.json"
PROVIDER_ID = "lucide-generic"


class ValidationError(RuntimeError):
    pass


def _load_json(path: Path) -> dict[str, Any]:
    try:
        return json.loads(path.read_text(encoding="utf-8"))
    except (OSError, json.JSONDecodeError) as exc:
        raise ValidationError(f"Cannot read valid JSON from {path.relative_to(ROOT)}: {exc}") from exc


def collect_referenced_icons(catalog: dict[str, Any]) -> list[str]:
    refs: set[str] = set()

    for domain_name, domain in catalog.get("semanticDomains", {}).items():
        icons = domain.get("preferredIcons", [])
        if not isinstance(icons, list):
            raise ValidationError(f"semanticDomains.{domain_name}.preferredIcons must be a list")
        refs.update(str(icon) for icon in icons)

    for route_name, route in catalog.get("preferredRouting", {}).items():
        icon = route.get("icon")
        if not isinstance(icon, str) or not icon:
            raise ValidationError(f"preferredRouting.{route_name}.icon must be a non-empty string")
        refs.add(icon)

    for index, rule in enumerate(catalog.get("ambiguityRules", [])):
        concepts = rule.get("concepts", [])
        if not isinstance(concepts, list):
            raise ValidationError(f"ambiguityRules[{index}].concepts must be a list")
        refs.update(str(icon) for icon in concepts)

    fallback_icons = catalog.get("fallbackPolicy", {}).get("fallbackIcons", [])
    if not isinstance(fallback_icons, list):
        raise ValidationError("fallbackPolicy.fallbackIcons must be a list")
    refs.update(str(icon) for icon in fallback_icons)

    invalid = sorted(icon for icon in refs if not icon or icon != icon.strip() or " " in icon)
    if invalid:
        raise ValidationError(f"Invalid canonical Lucide icon names: {invalid}")

    return sorted(refs)


def validate_offline() -> tuple[dict[str, Any], list[str]]:
    catalog = _load_json(CATALOG_PATH)
    snapshot = _load_json(SNAPSHOT_PATH)
    registry = _load_json(REGISTRY_PATH)

    if catalog.get("provider") != PROVIDER_ID:
        raise ValidationError(f"Catalog provider must be {PROVIDER_ID!r}")
    if snapshot.get("provider") != PROVIDER_ID:
        raise ValidationError(f"Snapshot provider must be {PROVIDER_ID!r}")

    providers = registry.get("providers", {})
    if PROVIDER_ID not in providers:
        raise ValidationError(f"Provider registry is missing {PROVIDER_ID!r}")
    lucide = providers[PROVIDER_ID]

    profile = catalog.get("profile", {})
    release = snapshot.get("release")
    commit = snapshot.get("commit")
    source_tree = snapshot.get("sourceTree")
    inventory_tree = snapshot.get("inventoryTree")
    repository = snapshot.get("sourceRepository")

    pinned_values = (release, commit, source_tree, inventory_tree, repository)
    if not all(isinstance(value, str) and value for value in pinned_values):
        raise ValidationError(
            "Snapshot must pin non-empty repository, release, commit, sourceTree and inventoryTree values"
        )
    if any(len(value) != 40 for value in (commit, source_tree, inventory_tree)):
        raise ValidationError("Snapshot commit/sourceTree/inventoryTree must use full 40-character Git SHAs")

    if profile.get("sourceRepository") != repository:
        raise ValidationError("Catalog sourceRepository differs from pinned snapshot")
    if profile.get("profiledRelease") != release:
        raise ValidationError("Catalog profiledRelease differs from pinned snapshot")
    catalog_commit = profile.get("profiledCommit")
    if not isinstance(catalog_commit, str) or not commit.startswith(catalog_commit):
        raise ValidationError("Catalog profiledCommit does not identify the pinned snapshot commit")

    if lucide.get("upstreamRepository") != repository:
        raise ValidationError("Provider registry upstreamRepository differs from pinned snapshot")
    if lucide.get("profiledRelease") != release:
        raise ValidationError("Provider registry profiledRelease differs from pinned snapshot")
    registry_commit = lucide.get("profiledCommit")
    if not isinstance(registry_commit, str) or not commit.startswith(registry_commit):
        raise ValidationError("Provider registry profiledCommit does not identify the pinned snapshot commit")

    if lucide.get("providerPriority") != "generic-fallback":
        raise ValidationError("Lucide must remain a generic-fallback provider")
    if lucide.get("assetPersistence") not in {"dependency-or-runtime", "runtime-only"}:
        raise ValidationError("Lucide assetPersistence must not imply vendoring the full upstream library")

    corporate = providers.get("euroimmun-corporate")
    if not isinstance(corporate, dict) or corporate.get("providerPriority") != "corporate":
        raise ValidationError("Corporate provider priority contract is missing or weakened")

    status_safety = catalog.get("statusSafety", {})
    required_safety = (
        "criticalMeaningRequiresTextLabel",
        "positiveStatusRequiresEvidence",
        "regulatoryApprovalMayNotBeInferredFromIcon",
        "medicalIconMayNotImplyDiagnosisOrPerformance",
    )
    missing_safety = [key for key in required_safety if status_safety.get(key) is not True]
    if missing_safety:
        raise ValidationError(f"Required claim/status safety gates are not enabled: {missing_safety}")

    refs = collect_referenced_icons(catalog)
    snapshot_refs = snapshot.get("referencedIcons")
    if not isinstance(snapshot_refs, list):
        raise ValidationError("Snapshot referencedIcons must be a list")
    if snapshot_refs != sorted(set(snapshot_refs)):
        raise ValidationError("Snapshot referencedIcons must be sorted and unique")
    if refs != snapshot_refs:
        missing = sorted(set(refs) - set(snapshot_refs))
        stale = sorted(set(snapshot_refs) - set(refs))
        raise ValidationError(
            "Semantic catalog and pinned reference snapshot differ; "
            f"missing_from_snapshot={missing}, stale_in_snapshot={stale}"
        )
    if snapshot.get("referencedIconCount") != len(refs):
        raise ValidationError(
            f"Snapshot referencedIconCount must be {len(refs)}, got {snapshot.get('referencedIconCount')}"
        )

    return snapshot, refs


def fetch_upstream_paths(snapshot: dict[str, Any]) -> set[str]:
    repository = snapshot["sourceRepository"]
    inventory_tree = snapshot["inventoryTree"]
    url = f"https://api.github.com/repos/{repository}/git/trees/{inventory_tree}?recursive=1"
    headers = {
        "Accept": "application/vnd.github+json",
        "User-Agent": "skillz-lucide-integrity-validator",
        "X-GitHub-Api-Version": "2022-11-28",
    }
    token = os.environ.get("GITHUB_TOKEN")
    if token:
        headers["Authorization"] = f"Bearer {token}"

    request = urllib.request.Request(url, headers=headers)
    try:
        with urllib.request.urlopen(request, timeout=30) as response:
            payload = json.load(response)
    except (urllib.error.URLError, TimeoutError, json.JSONDecodeError) as exc:
        raise ValidationError(f"Cannot fetch pinned Lucide icon tree {inventory_tree}: {exc}") from exc

    if payload.get("sha") != inventory_tree:
        raise ValidationError(
            f"GitHub returned icon tree {payload.get('sha')!r}, expected {inventory_tree!r}"
        )
    if payload.get("truncated") is True:
        raise ValidationError("Pinned Lucide icons subtree response is truncated")

    entries = payload.get("tree")
    if not isinstance(entries, list):
        raise ValidationError("Pinned Lucide icon tree response has no tree entries")
    return {
        entry.get("path")
        for entry in entries
        if isinstance(entry, dict) and isinstance(entry.get("path"), str)
    }


def validate_upstream(snapshot: dict[str, Any], refs: list[str]) -> None:
    paths = fetch_upstream_paths(snapshot)
    pattern = snapshot.get("inventoryPathPattern", "{name}.json")
    missing = [name for name in refs if pattern.format(name=name) not in paths]
    if missing:
        raise ValidationError(
            "Semantic catalog references Lucide icons absent from the pinned upstream icon tree: "
            + ", ".join(missing)
        )


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument(
        "--check-upstream",
        action="store_true",
        help="Also fetch the immutable pinned Lucide icons Git subtree and verify every referenced icon name.",
    )
    args = parser.parse_args(argv)

    try:
        snapshot, refs = validate_offline()
        if args.check_upstream:
            validate_upstream(snapshot, refs)
    except ValidationError as exc:
        print(f"Lucide provider validation FAILED: {exc}", file=sys.stderr)
        return 1

    mode = "offline + pinned upstream" if args.check_upstream else "offline"
    print(
        "Lucide provider validation PASS "
        f"({mode}; release={snapshot['release']}; icons={len(refs)}; inventoryTree={snapshot['inventoryTree']})"
    )
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
