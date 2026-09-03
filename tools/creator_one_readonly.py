#!/usr/bin/env python3
"""Read-only client for TikTok One creator campaign endpoints.

Authentication is supplied as an existing H5 session cookie. The cookie is
never logged or written into output. This client intentionally has no generic
URL option and no POST support, so discovering a route cannot accidentally
turn into a campaign mutation.
"""

from __future__ import annotations

import argparse
import json
import os
import sys
import urllib.error
import urllib.parse
import urllib.request
from pathlib import Path
from typing import Any


ORIGINS = {
    "ads-us": "https://ads.us.tiktok.com",
    "inapp-us": "https://inapp-ttp2.tiktokv.us",
}
ROUTES = {
    "homepage": ("/CreativeOne/OrderQuery/CreatorCampaignManagementHomepage", ()),
    "collabs": (
        "/CreativeOne/OrderQuery/CreatorCollabList",
        ("collabStage", "limit", "page", "campaignID"),
    ),
    "collab-detail": (
        "/CreativeOne/OrderQuery/CreatorGetCollabDetailV2",
        (
            "campaignID",
            "opportunityID",
            "orderID",
            "creatorAgencyID",
            "joinSource",
            "partnerCampaignID",
        ),
    ),
    "order-detail": ("/CreativeOne/OrderQuery/CreatorGetOrderDetail", ("orderID",)),
    "folder-tree": ("/CreativeOne/OrderQuery/CreatorGetFolderTree", ("campaignID",)),
    "files": (
        "/CreativeOne/OrderQuery/CreatorGetFileList",
        ("campaignID", "folderID", "orderType", "limit", "page"),
    ),
    "posts": (
        "/CreativeOne/OrderQuery/CreatorGetPostItemList",
        ("page", "limit", "scene", "orderID", "brandLinkID"),
    ),
    "analytics": (
        "/CreativeOne/OrderQuery/CreatorAnalyticOrderInfo",
        ("itemID", "videoID"),
    ),
    "tracking": (
        "/CreativeOne/OrderQuery/CreatorGetOrderTrackingInfo",
        ("orderID",),
    ),
    "generated-content": (
        "/CreativeOne/OrderQuery/CreatorGetGeneratedContent",
        ("campaignID", "generateAction", "taskID"),
    ),
}


def load_cookie(cookie_file: Path | None, session_json: Path | None) -> str:
    cookie = cookie_file.read_text(encoding="utf-8").strip() if cookie_file else ""
    if not cookie and session_json:
        session = json.loads(session_json.read_text(encoding="utf-8"))
        cookie = str(session.get("cookie", "")).strip()
    cookie = cookie or os.environ.get("TIKTOK_ONE_COOKIE", "").strip()
    if not cookie:
        raise ValueError(
            "Provide an H5 session through --cookie-file or TIKTOK_ONE_COOKIE."
        )
    if "\n" in cookie or "\r" in cookie:
        raise ValueError("Cookie input must be one line.")
    return cookie


def request(route_name: str, values: dict[str, str], cookie: str, origin: str) -> Any:
    path, allowed_fields = ROUTES[route_name]
    query = {key: values[key] for key in allowed_fields if values.get(key) is not None}
    base_url = ORIGINS[origin]
    url = base_url + path
    if query:
        url += "?" + urllib.parse.urlencode(query)
    req = urllib.request.Request(
        url,
        method="GET",
        headers={
            "Accept": "application/json, text/plain, */*",
            "Cookie": cookie,
            "Origin": base_url,
            "Referer": base_url + "/creative/creatormarketplace/home",
            "User-Agent": "Mozilla/5.0 (Linux; Android 9) AppleWebKit/537.36 "
            "(KHTML, like Gecko) Version/4.0 Chrome/120 Mobile Safari/537.36",
        },
    )
    try:
        with urllib.request.urlopen(req, timeout=30) as response:
            return json.load(response)
    except urllib.error.HTTPError as exc:
        # Do not echo response bodies: gateways sometimes reflect session data.
        raise RuntimeError(f"TikTok One returned HTTP {exc.code} for {route_name}") from exc


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("route", choices=sorted(ROUTES))
    parser.add_argument("--cookie-file", type=Path)
    parser.add_argument("--session-json", type=Path)
    parser.add_argument("--origin", choices=sorted(ORIGINS), default="ads-us")
    parser.add_argument("--output", type=Path)
    parser.add_argument("--param", action="append", default=[], metavar="KEY=VALUE")
    args = parser.parse_args()

    values: dict[str, str] = {}
    for item in args.param:
        if "=" not in item:
            parser.error(f"invalid --param {item!r}; expected KEY=VALUE")
        key, value = item.split("=", 1)
        values[key] = value
    allowed = set(ROUTES[args.route][1])
    unexpected = sorted(set(values) - allowed)
    if unexpected:
        parser.error(f"unsupported parameter(s) for {args.route}: {', '.join(unexpected)}")

    try:
        payload = request(
            args.route,
            values,
            load_cookie(args.cookie_file, args.session_json),
            args.origin,
        )
    except (OSError, ValueError, RuntimeError, json.JSONDecodeError) as exc:
        print(f"error: {exc}", file=sys.stderr)
        return 1

    rendered = json.dumps(payload, ensure_ascii=False, indent=2) + "\n"
    if args.output:
        args.output.parent.mkdir(parents=True, exist_ok=True)
        args.output.write_text(rendered, encoding="utf-8")
    else:
        print(rendered, end="")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
