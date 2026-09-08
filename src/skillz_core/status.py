from __future__ import annotations

import json
import re
from pathlib import Path
from typing import Any

SHA_RE = re.compile(r"^[0-9a-fA-F]{40}$")
VALID_STATES = {"current", "stale", "unknown"}


def normalize_commit(value: str | None, *, field: str) -> str | None:
    if value is None or not value.strip():
        return None
    normalized = value.strip().lower()
    if not SHA_RE.fullmatch(normalized):
        raise ValueError(f"{field} must be a full 40-character Git commit SHA")
    return normalized


def load_distribution_manifest(path: Path) -> dict[str, Any]:
    try:
        value = json.loads(path.read_text(encoding="utf-8"))
    except (OSError, json.JSONDecodeError) as exc:
        raise ValueError(f"cannot read installed distribution manifest: {exc}") from exc
    if not isinstance(value, dict):
        raise ValueError("installed distribution manifest root must be an object")
    return value


def installed_identity(manifest: dict[str, Any]) -> tuple[str | None, str | None]:
    version = manifest.get("pluginVersion")
    commit = manifest.get("sourceCommit")
    normalized_version = str(version).strip() if version is not None and str(version).strip() else None
    normalized_commit = normalize_commit(str(commit) if commit is not None else None, field="installed sourceCommit")
    return normalized_version, normalized_commit


def resolve_status(
    *,
    repository_head: str | None,
    repository_version: str | None,
    installed_commit: str | None,
    installed_version: str | None,
) -> dict[str, Any]:
    head = normalize_commit(repository_head, field="repository HEAD")
    installed = normalize_commit(installed_commit, field="installed commit")
    repo_version = repository_version.strip() if repository_version and repository_version.strip() else None
    runtime_version = installed_version.strip() if installed_version and installed_version.strip() else None

    commit_match = None if head is None or installed is None else head == installed
    version_match = None if repo_version is None or runtime_version is None else repo_version == runtime_version

    if commit_match is True:
        state = "current"
        reason = "installed source commit matches repository HEAD"
    elif commit_match is False:
        state = "stale"
        reason = "installed source commit differs from repository HEAD"
    elif version_match is False:
        state = "stale"
        reason = "installed plugin version differs from repository version"
    else:
        state = "unknown"
        reason = "exact freshness cannot be proven without both repository HEAD and installed source commit"

    return {
        "schemaVersion": 1,
        "status": state,
        "reason": reason,
        "repository": {"head": head, "version": repo_version},
        "installed": {"commit": installed, "version": runtime_version},
        "comparisons": {"commitMatch": commit_match, "versionMatch": version_match},
    }


def render_status_human(status: dict[str, Any]) -> str:
    if status.get("status") not in VALID_STATES:
        raise ValueError("invalid skill status payload")
    repository = status["repository"]
    installed = status["installed"]
    comparisons = status["comparisons"]

    def shown(value: object) -> str:
        return "—" if value is None else str(value)

    return "\n".join(
        [
            f"status: {status['status']}",
            f"reason: {status['reason']}",
            f"repository HEAD: {shown(repository.get('head'))}",
            f"repository version: {shown(repository.get('version'))}",
            f"installed commit: {shown(installed.get('commit'))}",
            f"installed version: {shown(installed.get('version'))}",
            f"commit match: {shown(comparisons.get('commitMatch'))}",
            f"version match: {shown(comparisons.get('versionMatch'))}",
        ]
    )


def provenance(index: dict) -> dict:
    value = index.get("provenance", {})
    return value if isinstance(value, dict) else {}


def repository_version(index: dict, version_path: Path, override: str | None = None) -> str | None:
    if override and override.strip():
        return override.strip()
    value = provenance(index).get("version")
    if value is not None and str(value).strip():
        return str(value).strip()
    try:
        return version_path.read_text(encoding="utf-8").strip() or None
    except OSError:
        return None


def build_status_payload(
    index: dict,
    *,
    version_path: Path,
    repository_head: str | None,
    repository_version_override: str | None,
    installed_manifest: Path | None,
    installed_commit: str | None,
    installed_version: str | None,
) -> dict:
    meta = provenance(index)
    head = repository_head or (str(meta.get("commitSha")) if meta.get("commitSha") is not None else None)
    runtime_version = installed_version
    runtime_commit = installed_commit
    if installed_manifest is not None:
        manifest_version, manifest_commit = installed_identity(load_distribution_manifest(installed_manifest))
        runtime_version = runtime_version or manifest_version
        runtime_commit = runtime_commit or manifest_commit
    return resolve_status(
        repository_head=head,
        repository_version=repository_version(index, version_path, repository_version_override),
        installed_commit=runtime_commit,
        installed_version=runtime_version,
    )
