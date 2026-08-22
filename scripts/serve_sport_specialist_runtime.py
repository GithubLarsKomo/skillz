#!/usr/bin/env python3
from __future__ import annotations

import hmac
import json
import os
import sys
from http.server import BaseHTTPRequestHandler, ThreadingHTTPServer
from typing import Callable

import sport_specialist_runtime as runtime

DEFAULT_MAX_BODY = 512 * 1024


def parse_int_env(name: str, default: int, low: int, high: int, environ: dict[str, str] | None = None) -> int:
    env = os.environ if environ is None else environ
    raw = env.get(name, str(default)).strip()
    try:
        value = int(raw)
    except ValueError as exc:
        raise ValueError(f"{name} must be an integer") from exc
    if value < low or value > high:
        raise ValueError(f"{name} must be within {low}..{high}")
    return value


def bearer_authorized(header_value: str | None, expected_token: str) -> bool:
    if not expected_token:
        return True
    if not isinstance(header_value, str) or not header_value.startswith("Bearer "):
        return False
    supplied = header_value[7:]
    return bool(supplied) and hmac.compare_digest(supplied.encode("utf-8"), expected_token.encode("utf-8"))


def make_server(
    host: str,
    port: int,
    provider_config: dict,
    *,
    bearer_token: str = "",
    revision: str = "unknown",
    max_body: int = DEFAULT_MAX_BODY,
    transport: Callable = runtime.provider.default_transport,
    environ: dict[str, str] | None = None,
) -> ThreadingHTTPServer:
    provider_config = runtime.provider.validate_config(provider_config)
    if not isinstance(host, str) or not host.strip():
        raise ValueError("host must be non-empty")
    if not isinstance(port, int) or isinstance(port, bool) or port < 0 or port > 65535:
        raise ValueError("port must be within 0..65535")
    if not isinstance(max_body, int) or isinstance(max_body, bool) or max_body < 1024 or max_body > 2 * 1024 * 1024:
        raise ValueError("max_body must be within 1024..2097152")
    if bearer_token and len(bearer_token) < 32:
        raise ValueError("SPORT_RUNTIME_BEARER_TOKEN must contain at least 32 characters when enabled")

    class Handler(BaseHTTPRequestHandler):
        server_version = "SkillzSportRuntime/1"
        sys_version = ""

        def log_message(self, fmt: str, *args) -> None:
            # BaseHTTPRequestHandler logs request line/status only; never serialize headers or request bodies here.
            sys.stderr.write("sport-runtime %s - %s\n" % (self.address_string(), fmt % args))

        def send_json(self, status: int, value: object) -> None:
            body = json.dumps(value, ensure_ascii=False, separators=(",", ":")).encode("utf-8")
            self.send_response(status)
            self.send_header("Content-Type", "application/json; charset=utf-8")
            self.send_header("Content-Length", str(len(body)))
            self.send_header("Cache-Control", "no-store")
            self.send_header("X-Content-Type-Options", "nosniff")
            self.end_headers()
            self.wfile.write(body)

        def do_GET(self) -> None:
            if self.path != "/healthz":
                self.send_json(404, {"error": "not_found"})
                return
            self.send_json(200, {
                "ok": True,
                "runtime": runtime.RUNTIME_ID,
                "provider": provider_config["providerId"],
                "model": provider_config["modelId"],
                "skillz_revision": revision or "unknown",
            })

        def do_POST(self) -> None:
            if self.path != "/reason":
                self.send_json(404, {"error": "not_found"})
                return
            if not bearer_authorized(self.headers.get("Authorization"), bearer_token):
                self.send_json(401, {"error": "unauthorized"})
                return
            if self.headers.get_content_type() != "application/json":
                self.send_json(415, {"error": "content_type_must_be_application_json"})
                return
            length_raw = self.headers.get("Content-Length")
            if length_raw is None:
                self.send_json(411, {"error": "content_length_required"})
                return
            try:
                length = int(length_raw)
            except ValueError:
                self.send_json(400, {"error": "invalid_content_length"})
                return
            if length < 0 or length > max_body:
                self.send_json(413, {"error": "request_body_too_large"})
                return
            raw = self.rfile.read(length)
            try:
                payload = json.loads(raw.decode("utf-8"))
                runtime.validate_runtime_request(payload)
            except (UnicodeDecodeError, json.JSONDecodeError, ValueError) as exc:
                self.send_json(400, {"error": "invalid_runtime_request", "detail": str(exc)})
                return
            try:
                result = runtime.invoke(
                    payload,
                    provider_config,
                    transport=transport,
                    environ=environ,
                    revision=revision,
                )
            except ValueError as exc:
                self.send_json(502, {"error": "specialist_reasoning_failed", "detail": str(exc)})
                return
            except Exception:
                self.send_json(500, {"error": "internal_error"})
                return
            self.send_json(200, result)

    return ThreadingHTTPServer((host, port), Handler)


def main() -> int:
    try:
        provider_config = runtime.load_provider_config()
        host = os.environ.get("SPORT_RUNTIME_HOST", "0.0.0.0").strip() or "0.0.0.0"
        port = parse_int_env("SPORT_RUNTIME_PORT", 8080, 1, 65535)
        max_body = parse_int_env("SPORT_RUNTIME_MAX_BODY_BYTES", DEFAULT_MAX_BODY, 1024, 2 * 1024 * 1024)
        bearer_token = os.environ.get("SPORT_RUNTIME_BEARER_TOKEN", "")
        revision = os.environ.get("SKILLZ_REVISION", "").strip() or "unknown"
        server = make_server(host, port, provider_config, bearer_token=bearer_token, revision=revision, max_body=max_body)
    except ValueError as exc:
        print(f"ERROR: {exc}", file=sys.stderr)
        return 2

    print(f"{runtime.RUNTIME_ID} listening on {host}:{port}", file=sys.stderr)
    try:
        server.serve_forever()
    except KeyboardInterrupt:
        pass
    finally:
        server.server_close()
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
