#!/usr/bin/env python3
"""Read-only client for TikTok One creator campaign endpoints.

Authentication is supplied as an existing H5 session cookie and/or a creator
account X-Tt-Token captured from the user's own device. Secrets are never
logged or written into output. This client intentionally has no generic URL
option and no POST support, so discovering a route cannot accidentally turn
into a campaign mutation.
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

from tiktok_signer import DeviceProfile, TikTokSigner


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

STAGES = {
    "todo": "1",
    "pending": "2",
    "in-progress": "3",
    "done": "4",
}


def load_cookie(cookie_file: Path | None, session_json: Path | None) -> str:
    cookie = cookie_file.read_text(encoding="utf-8").strip() if cookie_file else ""
    if not cookie and session_json:
        session = json.loads(session_json.read_text(encoding="utf-8"))
        cookie = str(session.get("cookie", "")).strip()
    cookie = cookie or os.environ.get("TIKTOK_ONE_COOKIE", "").strip()
    if "\n" in cookie or "\r" in cookie:
        raise ValueError("Cookie input must be one line.")
    return cookie


def load_secret(path: Path | None, env_name: str) -> str:
    value = path.read_text(encoding="utf-8").strip() if path else ""
    value = value or os.environ.get(env_name, "").strip()
    if "\n" in value or "\r" in value:
        raise ValueError(f"{env_name} input must be one line.")
    return value


def parse_stages(value: str) -> list[str]:
    stages = [part.strip().lower() for part in value.split(",") if part.strip()]
    unknown = sorted(set(stages) - set(STAGES))
    if unknown:
        raise ValueError(f"unsupported stage(s): {', '.join(unknown)}")
    return list(dict.fromkeys(stages))


def request(
    route_name: str,
    values: dict[str, str],
    cookie: str,
    tt_token: str,
    origin: str,
    signed: bool,
    device_profile: Path | None,
) -> Any:
    path, allowed_fields = ROUTES[route_name]
    query = {key: values[key] for key in allowed_fields if values.get(key) is not None}
    if tt_token:
        query["request_tag_from"] = "h5"
    base_url = ORIGINS[origin]
    url = base_url + path
    query_string = urllib.parse.urlencode(query)
    if query:
        url += "?" + query_string
    headers = {
        "Accept": "application/json, text/plain, */*",
        "Origin": base_url,
        "Referer": base_url + "/creative/creatormarketplace/home",
        "User-Agent": "com.zhiliaoapp.musically/2024603030 "
        "(Linux; U; Android 15; en_US; moto g 5G - 2024)",
    }
    if cookie:
        headers["Cookie"] = cookie
    if tt_token:
        headers["X-Tt-Token"] = tt_token
        headers["x-tt-dataflow-id"] = "671088913"
    if signed:
        if device_profile:
            TikTokSigner.set_device(DeviceProfile.load(device_profile.read_text()))
        headers.update(
            TikTokSigner.generate_headers(
                params=query_string,
                version_name="46.3.3",
                version_code=2024603030,
                cookie=cookie or None,
            )
        )
    req = urllib.request.Request(
        url,
        method="GET",
        headers=headers,
    )
    try:
        with urllib.request.urlopen(req, timeout=30) as response:
            return json.load(response)
    except urllib.error.HTTPError as exc:
        # Do not echo response bodies: gateways sometimes reflect session data.
        raise RuntimeError(f"TikTok One returned HTTP {exc.code} for {route_name}") from exc


def crawl_campaigns(
    stages: list[str],
    limit: int,
    max_pages: int,
    cookie: str,
    tt_token: str,
    origin: str,
    signed: bool,
    device_profile: Path | None,
) -> dict[str, Any]:
    result: dict[str, Any] = {
        "homepage": request(
            "homepage", {}, cookie, tt_token, origin, signed, device_profile
        ),
        "stages": {},
    }
    for stage in stages:
        pages: list[Any] = []
        for page in range(1, max_pages + 1):
            payload = request(
                "collabs",
                {"collabStage": STAGES[stage], "limit": str(limit), "page": str(page)},
                cookie,
                tt_token,
                origin,
                signed,
                device_profile,
            )
            pages.append(payload)
            data = payload.get("data", payload) if isinstance(payload, dict) else {}
            rows = data.get("orderList", []) if isinstance(data, dict) else []
            if not isinstance(rows, list) or len(rows) < limit:
                break
        result["stages"][stage] = pages
    return result


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("route", choices=[*sorted(ROUTES), "campaigns"])
    parser.add_argument("--cookie-file", type=Path)
    parser.add_argument("--session-json", type=Path)
    parser.add_argument("--tt-token-file", type=Path)
    parser.add_argument("--signed", action="store_true")
    parser.add_argument("--device-profile", type=Path)
    parser.add_argument("--origin", choices=sorted(ORIGINS), default="ads-us")
    parser.add_argument("--output", type=Path)
    parser.add_argument("--param", action="append", default=[], metavar="KEY=VALUE")
    parser.add_argument("--stages", default="todo,pending,done")
    parser.add_argument("--limit", type=int, default=20)
    parser.add_argument("--max-pages", type=int, default=100)
    args = parser.parse_args()

    values: dict[str, str] = {}
    for item in args.param:
        if "=" not in item:
            parser.error(f"invalid --param {item!r}; expected KEY=VALUE")
        key, value = item.split("=", 1)
        values[key] = value
    allowed = set(ROUTES[args.route][1]) if args.route != "campaigns" else set()
    unexpected = sorted(set(values) - allowed)
    if unexpected:
        parser.error(f"unsupported parameter(s) for {args.route}: {', '.join(unexpected)}")

    try:
        cookie = load_cookie(args.cookie_file, args.session_json)
        tt_token = load_secret(args.tt_token_file, "TIKTOK_ONE_TT_TOKEN")
        if not cookie and not tt_token:
            raise ValueError(
                "Provide --cookie-file, --session-json, --tt-token-file, or the matching environment variable."
            )
        if args.limit < 1 or args.limit > 100:
            raise ValueError("--limit must be between 1 and 100")
        if args.max_pages < 1 or args.max_pages > 1000:
            raise ValueError("--max-pages must be between 1 and 1000")
        if args.route == "campaigns":
            payload = crawl_campaigns(
                parse_stages(args.stages),
                args.limit,
                args.max_pages,
                cookie,
                tt_token,
                args.origin,
                args.signed,
                args.device_profile,
            )
        else:
            payload = request(
                args.route,
                values,
                cookie,
                tt_token,
                args.origin,
                args.signed,
                args.device_profile,
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
