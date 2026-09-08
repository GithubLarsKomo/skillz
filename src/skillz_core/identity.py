from __future__ import annotations

import hashlib
import json
from pathlib import Path
from typing import Any

from .status import normalize_commit, provenance

DEFAULT_REPOSITORY = "GithubLarsKomo/skillz"


def _canonical_json(value: Any) -> bytes:
    return (json.dumps(value, ensure_ascii=False, sort_keys=True, separators=(",", ":")) + "\n").encode("utf-8")


def catalog_hash(index: dict[str, Any], graph: dict[str, Any]) -> str:
    digest = hashlib.sha256()
    for label, value in (("capability-index-v1", index), ("dependency-graph-v1", graph)):
        digest.update(label.encode("utf-8"))
        digest.update(b"\0")
        digest.update(_canonical_json(value))
        digest.update(b"\0")
    return digest.hexdigest()


def freshness(
    *,
    catalog_commit: str | None,
    runtime_commit: str | None,
    catalog_version: str | None,
    runtime_version: str | None,
) -> str:
    catalog = normalize_commit(catalog_commit, field="catalog commit")
    runtime = normalize_commit(runtime_commit, field="runtime commit")
    if catalog is not None and runtime is not None:
        return "current" if catalog == runtime else "stale"
    if catalog_version and runtime_version and catalog_version.strip() != runtime_version.strip():
        return "stale"
    if any(value is not None for value in (catalog_commit, runtime_commit, catalog_version, runtime_version)):
        return "unknown"
    return "not-compared"


def catalog_identity(
    index: dict[str, Any],
    graph: dict[str, Any],
    *,
    version_path: Path,
    runtime_commit: str | None = None,
    runtime_version: str | None = None,
) -> dict[str, Any]:
    meta = provenance(index)
    repository = str(meta.get("repository") or DEFAULT_REPOSITORY)
    ref = meta.get("ref")
    commit_value = meta.get("commitSha")
    commit = normalize_commit(str(commit_value) if commit_value is not None else None, field="catalog commit")
    version_value = meta.get("version")
    if version_value is not None and str(version_value).strip():
        version = str(version_value).strip()
    else:
        try:
            version = version_path.read_text(encoding="utf-8").strip() or None
        except OSError:
            version = None

    return {
        "repository": repository,
        "ref": str(ref) if ref is not None else None,
        "version": version,
        "commitSha": commit,
        "indexSchemaVersion": index.get("schemaVersion"),
        "graphSchemaVersion": graph.get("schemaVersion"),
        "skillCount": int(index.get("skillCount", len(index.get("skills", [])))),
        "entrypointCount": int(index.get("entrypointCount", 0)),
        "evaluationSuiteCount": int(index.get("evaluationSuiteCount", 0)),
        "evaluationPassed": index.get("evaluationPassed"),
        "evaluationErrorCount": int(index.get("evaluationErrorCount", 0)),
        "catalogHash": catalog_hash(index, graph),
        "freshness": freshness(
            catalog_commit=commit,
            runtime_commit=runtime_commit,
            catalog_version=version,
            runtime_version=runtime_version,
        ),
    }
