#!/usr/bin/env python3
"""Build a complete, operator-friendly TikTok One endpoint catalog."""

from __future__ import annotations

import argparse
import hashlib
import importlib.util
import json
import re
from collections import Counter
from pathlib import Path
from typing import Any

EXTRACTOR_PATH = Path(__file__).with_name("extract_creator_one_api.py")
SPEC = importlib.util.spec_from_file_location("extract_creator_one_api", EXTRACTOR_PATH)
EXTRACTOR = importlib.util.module_from_spec(SPEC)
assert SPEC.loader is not None
SPEC.loader.exec_module(EXTRACTOR)

LIVE_VALIDATED = {
    "/CreativeOne/OrderQuery/CreatorCampaignManagementHomepage",
    "/CreativeOne/OrderQuery/CreatorCollabList",
    "/CreativeOne/OrderQuery/CreatorGetCollabDetailV2",
    "/CreativeOne/OrderQuery/CreatorGetOrderDetail",
    "/CreativeOne/OrderQuery/CreatorGetFolderTree",
    "/CreativeOne/OrderQuery/CreatorGetFileList",
    "/CreativeOne/OrderQuery/CreatorGetPostItemList",
    "/CreativeOne/OrderQuery/CreatorGetOrderTrackingInfo",
}
VALIDATION_DATE = "2026-09-03"
WORD_RE = re.compile(r"[A-Z]+(?=[A-Z][a-z]|\d|$)|[A-Z]?[a-z]+|\d+(?:K|V\d+)?|[A-Z]+")
ACRONYMS = (
    "OpenAPI",
    "SparkAds",
    "TikTok",
    "IDs",
    "URL",
    "TTO",
    "MCN",
    "GMV",
    "CRM",
    "API",
    "SOW",
    "PDF",
    "CSV",
    "VAT",
    "ID",
)


def humanize(value: str) -> str:
    placeholders = {f"ACRONYM{i}": acronym for i, acronym in enumerate(ACRONYMS)}
    for placeholder, acronym in placeholders.items():
        value = value.replace(acronym, f" {placeholder} ")
    value = re.sub(r"(V\d+)", r" \1 ", value)
    words = []
    for chunk in value.replace("_", " ").split():
        if chunk in placeholders:
            words.append(placeholders[chunk])
        elif re.fullmatch(r"V\d+", chunk):
            words.append(chunk)
        else:
            words.extend(WORD_RE.findall(chunk))
    return " ".join(
        word if word in ACRONYMS or word.isupper() or re.fullmatch(r"V\d+", word) else word.lower()
        for word in words
    )


def annotate(route: dict[str, Any]) -> dict[str, Any]:
    _, _, service, action = route["path"].split("/", 3)
    method = route["method"]
    if method == "GET":
        classification = "read-only"
        safe_usage = "Allowlist required; safe for authenticated read validation."
    elif method == "POST":
        classification = "action-or-mutation"
        safe_usage = "Do not call automatically; review semantics and obtain authorization."
    else:
        classification = "unknown"
        safe_usage = "Do not call until method, inputs, and side effects are proven."
    return {
        **route,
        "service": service,
        "action": action,
        "plain_english": f"{humanize(action).capitalize()} in the {humanize(service)} service.",
        "classification": classification,
        "safe_usage": safe_usage,
        "live_validation": (
            {"status": "validated", "date": VALIDATION_DATE}
            if route["path"] in LIVE_VALIDATED
            else {"status": "not-tested"}
        ),
    }


def build(source: bytes, source_url: str = "") -> dict[str, Any]:
    routes = [annotate(route) for route in EXTRACTOR.extract(source.decode(), True)]
    return {
        "scope": "TikTok One /CreativeOne endpoints only",
        "source": {
            "url": source_url,
            "sha256": hashlib.sha256(source).hexdigest(),
        },
        "route_count": len(routes),
        "method_counts": dict(Counter(route["method"] or "UNKNOWN" for route in routes)),
        "service_counts": dict(Counter(route["service"] for route in routes)),
        "live_validated_count": sum(
            route["live_validation"]["status"] == "validated" for route in routes
        ),
        "routes": routes,
    }


def markdown(catalog: dict[str, Any]) -> str:
    lines = [
        "# Complete TikTok One endpoint catalog",
        "",
        f"Source SHA-256: `{catalog['source']['sha256']}`  ",
        f"Total: **{catalog['route_count']}** routes — "
        + ", ".join(f"**{count} {method}**" for method, count in catalog["method_counts"].items()),
        "",
        "Safety: GET routes are read-only candidates and still require an explicit allowlist. "
        "POST and UNKNOWN routes are never called automatically.",
        "",
    ]
    if catalog["source"]["url"]:
        lines.insert(3, f"Official bundle: `{catalog['source']['url']}`  ")
    services: dict[str, list[dict[str, Any]]] = {}
    for route in catalog["routes"]:
        services.setdefault(route["service"], []).append(route)
    for service, routes in services.items():
        lines += [
            f"## {service} ({len(routes)})",
            "",
            "| Action | Method | Classification | Endpoint | Input | Parameters | Live |",
            "| --- | --- | --- | --- | --- | --- | --- |",
        ]
        for route in routes:
            fields = ", ".join(f"`{field}`" for field in route["fields"]) or "—"
            live = (
                f"Validated {route['live_validation']['date']}"
                if route["live_validation"]["status"] == "validated"
                else "Not tested"
            )
            lines.append(
                f"| {route['plain_english']} | {route['method'] or 'UNKNOWN'} | "
                f"{route['classification']} | `{route['path']}` | "
                f"{route['payload'] or ('none' if route['observed_wrapper'] else 'unwrapped')} | "
                f"{fields} | {live} |"
            )
        lines.append("")
    return "\n".join(lines)


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("bundle", type=Path)
    parser.add_argument("--source-url", default="")
    parser.add_argument("--json-output", type=Path, required=True)
    parser.add_argument("--markdown-output", type=Path, required=True)
    args = parser.parse_args()
    catalog = build(args.bundle.read_bytes(), args.source_url)
    args.json_output.write_text(json.dumps(catalog, indent=2) + "\n", encoding="utf-8")
    args.markdown_output.write_text(markdown(catalog), encoding="utf-8")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
