from __future__ import annotations

import json
import logging
import time
from collections.abc import Mapping
from typing import Any

LOGGER_NAME = "skillz_mcp.operations"
logger = logging.getLogger(LOGGER_NAME)


def _emit(level: int, payload: dict[str, Any]) -> None:
    logger.log(level, json.dumps(payload, sort_keys=True, separators=(",", ":"), ensure_ascii=False))


def request_identifier(method: str, params: object) -> str | None:
    """Extract only the operation identifier; never serialize tool arguments or request bodies."""
    if isinstance(params, Mapping):
        if method == "tools/call":
            value = params.get("name")
        elif method == "resources/read":
            value = params.get("uri")
        else:
            value = None
    else:
        if method == "tools/call":
            value = getattr(params, "name", None)
        elif method == "resources/read":
            value = getattr(params, "uri", None)
        else:
            value = None
    return str(value) if value is not None else None


async def operational_logging(ctx: Any, call_next: Any) -> Any:
    """Observe one MCP message without logging arguments, bodies, credentials, or response content."""
    started = time.perf_counter()
    method = str(ctx.method)
    identifier = request_identifier(method, ctx.params)
    base: dict[str, Any] = {
        "event": "mcp_request",
        "method": method,
        "request": ctx.request_id is not None,
    }
    if identifier is not None:
        base["identifier"] = identifier

    try:
        result = await call_next(ctx)
    except Exception as exc:
        elapsed_ms = round((time.perf_counter() - started) * 1000, 3)
        _emit(
            logging.WARNING,
            {
                **base,
                "outcome": "error",
                "latencyMs": elapsed_ms,
                "errorCategory": type(exc).__name__,
            },
        )
        raise

    elapsed_ms = round((time.perf_counter() - started) * 1000, 3)
    _emit(logging.INFO, {**base, "outcome": "success", "latencyMs": elapsed_ms})
    return result


def log_catalog_loaded(identity: Mapping[str, Any]) -> None:
    """Log only compact startup identity/provenance, never catalog or skill content."""
    _emit(
        logging.INFO,
        {
            "event": "catalog_loaded",
            "repository": identity.get("repository"),
            "ref": identity.get("ref"),
            "version": identity.get("version"),
            "commitSha": identity.get("commitSha"),
            "indexSchemaVersion": identity.get("indexSchemaVersion"),
            "graphSchemaVersion": identity.get("graphSchemaVersion"),
            "skillCount": identity.get("skillCount"),
            "entrypointCount": identity.get("entrypointCount"),
            "catalogHash": identity.get("catalogHash"),
            "freshness": identity.get("freshness"),
        },
    )
