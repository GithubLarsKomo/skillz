from __future__ import annotations

from pathlib import Path, PurePosixPath, PureWindowsPath
from urllib.parse import unquote

DEFAULT_MAX_TEXT_BYTES = 1_000_000


def decoded_path(value: str) -> str:
    """Decode URL escaping twice so encoded and double-encoded traversal is visible."""
    first = unquote(value)
    return unquote(first)


def safe_relative_path(root: Path, relative_path: str) -> Path:
    """Resolve a repository-relative path while preventing traversal and symlink escape."""
    if not isinstance(relative_path, str) or not relative_path:
        raise ValueError("relative path must be a non-empty string")

    decoded = decoded_path(relative_path)
    if "\x00" in decoded:
        raise ValueError("relative path must not contain NUL bytes")
    if "\\" in decoded:
        raise ValueError("relative path must use forward slashes")

    posix = PurePosixPath(decoded)
    windows = PureWindowsPath(decoded)
    if posix.is_absolute() or windows.is_absolute() or windows.drive:
        raise ValueError("absolute paths are not allowed")
    if any(part in {".", ".."} for part in posix.parts):
        raise ValueError("path traversal segments are not allowed")

    allowed_root = root.resolve()
    candidate = (allowed_root / Path(*posix.parts)).resolve(strict=False)
    try:
        candidate.relative_to(allowed_root)
    except ValueError as exc:
        raise ValueError("resolved path escapes the allowed root") from exc
    return candidate


def read_utf8_text(root: Path, relative_path: str, *, max_bytes: int = DEFAULT_MAX_TEXT_BYTES) -> str:
    """Read bounded UTF-8 text from an allowlisted root using the safe path policy."""
    if max_bytes < 1:
        raise ValueError("max_bytes must be positive")
    path = safe_relative_path(root, relative_path)
    try:
        size = path.stat().st_size
    except OSError as exc:
        raise LookupError(f"resource does not exist: {relative_path}") from exc
    if not path.is_file():
        raise LookupError(f"resource is not a file: {relative_path}")
    if size > max_bytes:
        raise ValueError(f"resource exceeds text size limit of {max_bytes} bytes")
    try:
        return path.read_text(encoding="utf-8")
    except UnicodeDecodeError as exc:
        raise ValueError("resource is not valid UTF-8 text") from exc
    except OSError as exc:
        raise LookupError(f"cannot read resource: {relative_path}") from exc


def describe_path(root: Path, relative_path: str) -> dict:
    """Return safe metadata for a file or one-level directory listing without serving bytes."""
    path = safe_relative_path(root, relative_path)
    if not path.exists():
        raise LookupError(f"resource does not exist: {relative_path}")
    if path.is_file():
        return {
            "path": decoded_path(relative_path),
            "type": "file",
            "size": path.stat().st_size,
        }
    if not path.is_dir():
        raise LookupError(f"unsupported resource type: {relative_path}")

    entries: list[dict] = []
    for child in sorted(path.iterdir(), key=lambda item: item.name):
        rel = child.relative_to(root.resolve()).as_posix()
        safe_child = safe_relative_path(root, rel)
        entries.append(
            {
                "name": child.name,
                "path": rel,
                "type": "directory" if safe_child.is_dir() else "file",
                "size": safe_child.stat().st_size if safe_child.is_file() else None,
            }
        )
    return {
        "path": decoded_path(relative_path),
        "type": "directory",
        "entries": entries,
    }
