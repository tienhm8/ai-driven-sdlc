#!/usr/bin/env python3
"""Serve the framework guide and read-only project progress on localhost."""

from http import HTTPStatus
from http.server import BaseHTTPRequestHandler, ThreadingHTTPServer
from pathlib import Path
import argparse
import json
import re
import sys
from urllib.parse import unquote, urlsplit

sys.path.insert(0, str(Path(__file__).resolve().parents[1] / "src"))
from ai_sdlc_platform.config import PROJECT_ID_PATTERN, load_project_manifest
from ai_sdlc_platform.progress import DEFAULT_STATE_DIR, collect_progress

ROOT = Path(__file__).resolve().parents[2]
STATUS_ROUTE = re.compile(r"/api/projects/([^/]+)/status")


def list_projects(root: Path) -> list[dict]:
    found = []
    base = root / "projects"
    for path in sorted(base.iterdir()) if base.is_dir() else []:
        if not path.is_dir() or not re.fullmatch(PROJECT_ID_PATTERN, path.name):
            continue
        try:
            name = load_project_manifest(path)["project"]["name"]
        except (OSError, ValueError, KeyError):
            continue  # not an initialized project instance
        found.append({"id": path.name, "name": name})
    return found


def make_handler(root: Path, state_dir: Path):
    page = root / "framework" / "guide" / "index.html"

    class Handler(BaseHTTPRequestHandler):
        server_version = "GuideServer"

        def _send(self, status, body: bytes, content_type: str):
            self.send_response(status)
            self.send_header("Content-Type", content_type)
            self.send_header("Content-Length", str(len(body)))
            self.send_header("Cache-Control", "no-store")
            self.send_header("X-Content-Type-Options", "nosniff")
            self.end_headers()
            self.wfile.write(body)

        def _json(self, status, payload):
            self._send(status, json.dumps(payload, ensure_ascii=False).encode(), "application/json; charset=utf-8")

        def do_GET(self):
            path = unquote(urlsplit(self.path).path)
            if path in ("/", "/index.html"):
                self._send(HTTPStatus.OK, page.read_bytes(), "text/html; charset=utf-8")
            elif path == "/api/projects":
                self._json(HTTPStatus.OK, {"projects": list_projects(root)})
            elif match := STATUS_ROUTE.fullmatch(path):
                ids = {p["id"] for p in list_projects(root)}
                if match.group(1) not in ids:
                    self._json(HTTPStatus.NOT_FOUND, {"error": "Unknown project"})
                    return
                try:
                    result = collect_progress(root / "projects" / match.group(1), root / "framework", state_dir)
                except Exception as error:  # surface a readable message, keep the server alive
                    self._json(HTTPStatus.INTERNAL_SERVER_ERROR, {"error": f"{type(error).__name__}: {error}"})
                    return
                self._json(HTTPStatus.OK, result)
            else:
                self._json(HTTPStatus.NOT_FOUND, {"error": "Not found"})

        def _reject(self):
            self._json(HTTPStatus.METHOD_NOT_ALLOWED, {"error": "Read-only server"})

        do_POST = do_PUT = do_DELETE = do_PATCH = _reject

        def log_message(self, fmt, *args):
            sys.stderr.write("%s - %s\n" % (self.address_string(), fmt % args))

    return Handler


def main():
    parser = argparse.ArgumentParser(description="Serve the AI-Driven SDLC guide (read-only, localhost only)")
    parser.add_argument("--port", type=int, default=8765)
    parser.add_argument("--state-dir", type=Path, default=DEFAULT_STATE_DIR,
                        help=f"Governance state directory (default: {DEFAULT_STATE_DIR})")
    args = parser.parse_args()
    server = ThreadingHTTPServer(("127.0.0.1", args.port), make_handler(ROOT, args.state_dir.expanduser()))
    print(f"Guide: http://127.0.0.1:{server.server_port}/  (Ctrl+C to stop)")
    try:
        server.serve_forever()
    except KeyboardInterrupt:
        pass


if __name__ == "__main__":
    main()
