#!/usr/bin/env python3
"""Extract TikTok One API wrappers from a downloaded creator-center bundle.

The creator-center JavaScript is minified, but its generated API wrappers have a
stable shape: genBaseURL("/CreativeOne/...") followed by request({method, ...}).
This tool inventories those wrappers without needing an authenticated session.
It never reads or emits cookies or request headers.
"""

from __future__ import annotations

import argparse
import json
import re
from pathlib import Path
from typing import Any


ENDPOINT_RE = re.compile(
    r"genBaseURL\((?P<quote>['\"])(?P<path>/CreativeOne/[^'\"]+)(?P=quote)\)"
)
RAW_ENDPOINT_RE = re.compile(
    r"(?P<quote>['\"])(?P<path>/CreativeOne/[^'\"]+)(?P=quote)"
)
METHOD_RE = re.compile(r"method\s*:\s*['\"](?P<method>[A-Z]+)['\"]")
PAYLOAD_RE = re.compile(
    r"method\s*:\s*['\"][A-Z]+['\"]\s*,\s*"
    r"(?P<kind>params|data)\s*:\s*(?P<variable>[A-Za-z_$][\w$]*)"
)
FIELD_RE = re.compile(r"(?:^|,)\s*(?P<field>[A-Za-z_$][\w$]*)\s*:")


def enclosing_wrapper(source: str, position: int) -> str:
    """Return the minified function containing an endpoint occurrence."""
    start = source.rfind("function ", 0, position)
    if start < 0:
        start = max(0, source.rfind("=>", 0, position) - 500)
    end = source.find("}function ", position)
    if end < 0:
        end = min(len(source), position + 2_500)
    else:
        end += 1
    return source[start:end]


def object_fields(wrapper: str, variable: str) -> list[str]:
    escaped = re.escape(variable)
    assignment = re.search(
        rf"(?:let|const|var|,)\s*{escaped}\s*=\s*\{{(?P<body>[^}}]*)\}}",
        wrapper,
    )
    if not assignment:
        return []
    return [match.group("field") for match in FIELD_RE.finditer(assignment.group("body"))]


def extract(source: str, include_unwrapped: bool = False) -> list[dict[str, Any]]:
    routes: dict[str, dict[str, Any]] = {}
    if include_unwrapped:
        for endpoint in RAW_ENDPOINT_RE.finditer(source):
            path = endpoint.group("path")
            routes[path] = {
                "method": None,
                "path": path,
                "payload": None,
                "fields": [],
                "read_only": None,
                "observed_wrapper": False,
            }
    for endpoint in ENDPOINT_RE.finditer(source):
        wrapper = enclosing_wrapper(source, endpoint.start())
        method_match = METHOD_RE.search(wrapper)
        if not method_match:
            continue
        payload_match = PAYLOAD_RE.search(wrapper)
        payload_kind = payload_match.group("kind") if payload_match else None
        fields = (
            object_fields(wrapper, payload_match.group("variable"))
            if payload_match
            else []
        )
        path = endpoint.group("path")
        routes[path] = {
            "method": method_match.group("method"),
            "path": path,
            "payload": payload_kind,
            "fields": fields,
            "read_only": method_match.group("method") == "GET",
            "observed_wrapper": True,
        }
    return sorted(routes.values(), key=lambda route: route["path"])


def markdown(routes: list[dict[str, Any]]) -> str:
    lines = [
        "| Method | Endpoint | Input | Fields |",
        "| --- | --- | --- | --- |",
    ]
    for route in routes:
        fields = ", ".join(f"`{field}`" for field in route["fields"]) or "—"
        lines.append(
            f"| {route['method'] or 'UNKNOWN'} | `{route['path']}` | "
            f"{route['payload'] or ('none' if route['observed_wrapper'] else 'unwrapped')} "
            f"| {fields} |"
        )
    return "\n".join(lines) + "\n"


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("bundle", type=Path, help="Downloaded creator-center JS bundle")
    parser.add_argument("--format", choices=("json", "markdown"), default="json")
    parser.add_argument("--output", type=Path)
    parser.add_argument(
        "--include-unwrapped",
        action="store_true",
        help="Include every quoted /CreativeOne route, marking unknown methods",
    )
    args = parser.parse_args()

    routes = extract(
        args.bundle.read_text(encoding="utf-8"),
        include_unwrapped=args.include_unwrapped,
    )
    rendered = (
        json.dumps({"route_count": len(routes), "routes": routes}, indent=2) + "\n"
        if args.format == "json"
        else markdown(routes)
    )
    if args.output:
        args.output.parent.mkdir(parents=True, exist_ok=True)
        args.output.write_text(rendered, encoding="utf-8")
    else:
        print(rendered, end="")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
