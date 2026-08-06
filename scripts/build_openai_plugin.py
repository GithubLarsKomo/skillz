#!/usr/bin/env python3
from __future__ import annotations

import argparse
import hashlib
import io
import json
import shutil
import tarfile
from pathlib import Path
from typing import Any

ROOT = Path(__file__).resolve().parents[1]
SYNC = ROOT / ".skill-sync.json"
VERSION = ROOT / "VERSION"
TEMPLATE = ROOT / "distribution" / "openai-plugin" / ".codex-plugin" / "plugin.json"


def normalized_bytes(path: Path) -> bytes:
    text = path.read_text(encoding="utf-8").replace("\r\n", "\n").replace("\r", "\n").rstrip("\n") + "\n"
    return text.encode("utf-8")


def sha256_bytes(data: bytes) -> str:
    return hashlib.sha256(data).hexdigest()


def source_sha(path: Path) -> str:
    return sha256_bytes(normalized_bytes(path))


def load_json(path: Path) -> dict[str, Any]:
    value = json.loads(path.read_text(encoding="utf-8"))
    if not isinstance(value, dict):
        raise ValueError(f"{path}: expected JSON object")
    return value


def parse_skill_document(source: Path) -> tuple[dict[str, str], str]:
    text = normalized_bytes(source).decode("utf-8")
    lines = text.splitlines()
    if not lines or lines[0] != "---":
        raise ValueError(f"{source}: missing YAML frontmatter")
    try:
        end = lines.index("---", 1)
    except ValueError as exc:
        raise ValueError(f"{source}: unterminated YAML frontmatter") from exc
    metadata: dict[str, str] = {}
    for line in lines[1:end]:
        if ":" in line and not line.startswith((" ", "\t", "-")):
            key, value = line.split(":", 1)
            metadata[key] = value.strip()
    body = "\n".join(lines[end + 1 :]).lstrip("\n").rstrip("\n")
    return metadata, body


def render_openai_skill(source: Path) -> bytes:
    metadata, body = parse_skill_document(source)
    if not metadata.get("name") or not metadata.get("description"):
        raise ValueError(f"{source}: name and description are required")
    rendered = f"---\nname: {metadata['name']}\ndescription: {metadata['description']}\n---\n\n{body}\n"
    return rendered.encode("utf-8")


def _yaml_quote(value: str) -> str:
    return json.dumps(value, ensure_ascii=False)


def render_openai_agent_metadata(source: Path) -> bytes:
    metadata, _ = parse_skill_document(source)
    name = metadata.get("name")
    description = metadata.get("description")
    if not name or not description:
        raise ValueError(f"{source}: name and description are required")
    display_name = " ".join(part.capitalize() for part in name.split("-") if part)
    short_description = description if len(description) <= 120 else description[:117].rstrip() + "..."
    implicit = metadata.get("implicitInvocation", "true")
    normalized = implicit.casefold()
    if normalized not in {"true", "false"}:
        raise ValueError(f"{source}: implicitInvocation must be true or false")
    lines = [
        "interface:",
        f"  display_name: {_yaml_quote(display_name)}",
        f"  short_description: {_yaml_quote(short_description)}",
        "policy:",
        f"  allow_implicit_invocation: {normalized}",
    ]
    return ("\n".join(lines) + "\n").encode("utf-8")


def validate_plugin_manifest(value: dict[str, Any], expected_version: str) -> None:
    required = ["name", "version", "description", "author", "skills", "interface"]
    for key in required:
        if key not in value:
            raise ValueError(f"plugin manifest missing {key}")
    if value["name"] != "skillz":
        raise ValueError("plugin manifest name must be skillz")
    if value["version"] != expected_version:
        raise ValueError(f"plugin version {value['version']} != VERSION {expected_version}")
    if value["skills"] != "./skills/":
        raise ValueError("plugin skills path must be ./skills/")
    if "apps" in value or "mcpServers" in value:
        raise ValueError("apps/mcpServers require companion files and are out of scope")
    author = value.get("author")
    interface = value.get("interface")
    if not isinstance(author, dict) or not author.get("name"):
        raise ValueError("plugin author.name required")
    if not isinstance(interface, dict):
        raise ValueError("plugin interface object required")
    for key in ("displayName", "shortDescription", "longDescription", "developerName", "category"):
        if not interface.get(key):
            raise ValueError(f"plugin interface.{key} required")


def build(output: Path) -> dict[str, Any]:
    version = VERSION.read_text(encoding="utf-8").strip()
    sync = load_json(SYNC)
    if sync.get("schemaVersion") != 2 or not isinstance(sync.get("skills"), dict):
        raise ValueError("unsupported .skill-sync.json")
    plugin = load_json(TEMPLATE)
    validate_plugin_manifest(plugin, version)

    if output.exists():
        shutil.rmtree(output)
    (output / ".codex-plugin").mkdir(parents=True)
    (output / "skills").mkdir()
    plugin_bytes = (json.dumps(plugin, ensure_ascii=False, sort_keys=True, indent=2) + "\n").encode("utf-8")
    (output / ".codex-plugin" / "plugin.json").write_bytes(plugin_bytes)

    skills_manifest: dict[str, Any] = {}
    for name, spec in sorted(sync["skills"].items()):
        files = spec.get("files")
        if not isinstance(files, dict) or not files:
            raise ValueError(f"skill {name}: no portable files")
        bundle_files: dict[str, Any] = {}
        skill_source = ROOT / "skills" / name / "SKILL.md"
        agent_source = ROOT / "skills" / name / "agents" / "openai.yaml"
        if "SKILL.md" not in files:
            raise ValueError(f"skill {name}: SKILL.md is required")
        if "agents/openai.yaml" not in files:
            raise ValueError(f"skill {name}: canonical agents/openai.yaml is required")
        expected_agent_metadata = render_openai_agent_metadata(skill_source)
        if not agent_source.is_file():
            raise ValueError(f"missing canonical OpenAI metadata: {agent_source}")
        if normalized_bytes(agent_source) != expected_agent_metadata:
            raise ValueError(f"canonical OpenAI metadata drift: skills/{name}/agents/openai.yaml")
        for rel, expected in sorted(files.items()):
            source = ROOT / "skills" / name / rel
            if not source.is_file():
                raise ValueError(f"missing portable file: {source}")
            actual = source_sha(source)
            if actual != expected:
                raise ValueError(f"source hash drift: skills/{name}/{rel}")
            data = render_openai_skill(source) if rel == "SKILL.md" else normalized_bytes(source)
            dest = output / "skills" / name / rel
            dest.parent.mkdir(parents=True, exist_ok=True)
            dest.write_bytes(data)
            bundle_files[rel] = {"sourceSha256": actual, "bundleSha256": sha256_bytes(data)}
        skills_manifest[name] = {"files": bundle_files}

    manifest = {
        "schemaVersion": 1,
        "distribution": "openai-plugin",
        "pluginName": "skillz",
        "pluginVersion": version,
        "sourceRepository": sync.get("repository", "GithubLarsKomo/skillz"),
        "pluginManifestSha256": sha256_bytes(plugin_bytes),
        "skills": skills_manifest,
    }
    manifest_bytes = (json.dumps(manifest, ensure_ascii=False, sort_keys=True, separators=(",", ":")) + "\n").encode("utf-8")
    (output / "skillz-distribution-manifest.json").write_bytes(manifest_bytes)
    validate_bundle(output, manifest)
    return manifest


def validate_bundle(output: Path, manifest: dict[str, Any] | None = None) -> None:
    plugin = load_json(output / ".codex-plugin" / "plugin.json")
    validate_plugin_manifest(plugin, VERSION.read_text(encoding="utf-8").strip())
    manifest = manifest or load_json(output / "skillz-distribution-manifest.json")
    for name, spec in sorted(manifest["skills"].items()):
        skill_md = output / "skills" / name / "SKILL.md"
        if not skill_md.is_file():
            raise ValueError(f"bundle missing skills/{name}/SKILL.md")
        lines = skill_md.read_text(encoding="utf-8").splitlines()
        if len(lines) < 4 or lines[0] != "---":
            raise ValueError(f"invalid packaged frontmatter: {name}")
        end = lines.index("---", 1)
        keys = [line.split(":", 1)[0] for line in lines[1:end] if ":" in line]
        if keys != ["name", "description"]:
            raise ValueError(f"packaged SKILL.md frontmatter must contain only name+description: {name}")
        agent_metadata = output / "skills" / name / "agents" / "openai.yaml"
        if not agent_metadata.is_file():
            raise ValueError(f"bundle missing skills/{name}/agents/openai.yaml")
        for rel, hashes in spec["files"].items():
            path = output / "skills" / name / rel
            if sha256_bytes(path.read_bytes()) != hashes["bundleSha256"]:
                raise ValueError(f"bundle hash mismatch: skills/{name}/{rel}")


def write_deterministic_tar(source_dir: Path, archive: Path) -> None:
    archive.parent.mkdir(parents=True, exist_ok=True)
    with tarfile.open(archive, "w", format=tarfile.PAX_FORMAT) as tf:
        for path in sorted(source_dir.rglob("*")):
            if not path.is_file():
                continue
            rel = Path(source_dir.name) / path.relative_to(source_dir)
            data = path.read_bytes()
            info = tarfile.TarInfo(str(rel))
            info.size = len(data)
            info.mode = 0o644
            info.mtime = 0
            info.uid = info.gid = 0
            info.uname = info.gname = ""
            tf.addfile(info, io.BytesIO(data))


def main() -> int:
    parser = argparse.ArgumentParser(description="Build a deterministic OpenAI/Codex plugin bundle from canonical Skillz sources.")
    parser.add_argument("--output", type=Path, required=True)
    parser.add_argument("--archive", type=Path)
    args = parser.parse_args()
    try:
        manifest = build(args.output.resolve())
        if args.archive:
            write_deterministic_tar(args.output.resolve(), args.archive.resolve())
    except (OSError, ValueError, json.JSONDecodeError) as exc:
        print(f"ERROR: {exc}")
        return 2
    print(json.dumps({"ok": True, "pluginVersion": manifest["pluginVersion"], "skillCount": len(manifest["skills"]), "output": str(args.output.resolve())}, sort_keys=True))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
