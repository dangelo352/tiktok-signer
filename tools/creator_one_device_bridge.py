#!/usr/bin/env python3
"""Read TikTok One creator APIs through the logged-in Android app.

The app opens a first-party, read-only CreatorOne URL in its own WebView. Its
native request stack supplies the current creator session. Android text
selection and scrcpy's local clipboard synchronization return the JSON to the
Mac; no token, cookie, or signed header is extracted or printed.
"""

from __future__ import annotations

import argparse
import json
import shutil
import subprocess
import sys
import time
import urllib.parse
from pathlib import Path
from typing import Any


ORIGIN = "https://inapp.tiktokv.com"
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
    "analytics": ("/CreativeOne/OrderQuery/CreatorAnalyticOrderInfo", ("itemID", "videoID")),
    "tracking": ("/CreativeOne/OrderQuery/CreatorGetOrderTrackingInfo", ("orderID",)),
    "generated-content": (
        "/CreativeOne/OrderQuery/CreatorGetGeneratedContent",
        ("campaignID", "generateAction", "taskID"),
    ),
}
STAGES = {"todo": 1, "pending": 2, "in-progress": 3, "done": 4}


def run(command: list[str], *, input_bytes: bytes | None = None) -> bytes:
    return subprocess.run(
        command,
        input=input_bytes,
        stdout=subprocess.PIPE,
        stderr=subprocess.PIPE,
        check=True,
    ).stdout


def parse_params(items: list[str], allowed: tuple[str, ...]) -> dict[str, str]:
    values: dict[str, str] = {}
    for item in items:
        if "=" not in item:
            raise ValueError(f"invalid parameter {item!r}; expected KEY=VALUE")
        key, value = item.split("=", 1)
        if key not in allowed:
            raise ValueError(f"unsupported parameter {key!r}")
        values[key] = value
    return values


def parse_stages(value: str) -> list[str]:
    stages = list(dict.fromkeys(item.strip() for item in value.split(",") if item.strip()))
    unknown = sorted(set(stages) - set(STAGES))
    if unknown:
        raise ValueError(f"unsupported stage(s): {', '.join(unknown)}")
    return stages


class DeviceBridge:
    def __init__(self, serial: str, wait_seconds: float) -> None:
        self.serial = serial
        self.wait_seconds = wait_seconds
        self.scrcpy: subprocess.Popen[bytes] | None = None
        self.previous_clipboard = run(["pbpaste"])

    def __enter__(self) -> "DeviceBridge":
        if subprocess.run(["pgrep", "-x", "scrcpy"], stdout=subprocess.DEVNULL).returncode != 0:
            self.scrcpy = subprocess.Popen(
                ["scrcpy", "--serial", self.serial, "--no-video", "--no-audio"],
                stdout=subprocess.DEVNULL,
                stderr=subprocess.DEVNULL,
            )
            time.sleep(1.5)
        return self

    def __exit__(self, *_args: object) -> None:
        run(["pbcopy"], input_bytes=self.previous_clipboard)
        if self.scrcpy is not None:
            self.scrcpy.terminate()
            try:
                self.scrcpy.wait(timeout=3)
            except subprocess.TimeoutExpired:
                self.scrcpy.kill()

    def adb(self, *args: str) -> bytes:
        return run(["adb", "-s", self.serial, *args])

    def copy_button_coordinates(self) -> tuple[int, int]:
        screenshot = self.adb("exec-out", "screencap", "-p")
        tsv = run(
            ["tesseract", "stdin", "stdout", "--psm", "6", "tsv"],
            input_bytes=screenshot,
        ).decode("utf-8", errors="replace")
        for line in tsv.splitlines():
            columns = line.split("\t")
            if len(columns) == 12 and columns[11].strip() == "Copy":
                left, top, width, height = map(int, columns[6:10])
                return left + width // 2, top + height // 2
        raise RuntimeError("Android text-selection Copy button was not found")

    def fetch(self, route: str, params: dict[str, str]) -> Any:
        path, allowed = ROUTES[route]
        unexpected = sorted(set(params) - set(allowed))
        if unexpected:
            raise ValueError(f"unsupported parameter(s): {', '.join(unexpected)}")
        url = ORIGIN + path
        if params:
            url += "?" + urllib.parse.urlencode(params)
        deep_link = "snssdk1233://webview?url=" + urllib.parse.quote(url, safe="")
        # TikTok's CrossPlatformActivity may retain the first deep-link URL
        # when reused. A force-stop clears that activity only; account/session
        # storage remains intact and the next URL is fetched fresh.
        self.adb("shell", "am", "force-stop", "com.zhiliaoapp.musically")
        self.adb(
            "shell", "am", "start", "-W", "-a", "android.intent.action.VIEW", "-d", deep_link
        )
        time.sleep(self.wait_seconds)

        for attempt in range(3):
            sentinel = f"tiktok-one-waiting-{time.time_ns()}".encode()
            run(["pbcopy"], input_bytes=sentinel)
            self.adb("shell", "input", "swipe", "350", "200", "350", "200", "1200")
            time.sleep(0.7)
            self.adb("shell", "input", "tap", "325", "139")
            time.sleep(0.7)
            if route != "homepage":
                # Selecting a long response hides the toolbar. A second long
                # press reveals it without following any URL under the text.
                self.adb("shell", "input", "swipe", "500", "205", "500", "205", "600")
                time.sleep(0.7)
            copy_x, copy_y = self.copy_button_coordinates()
            self.adb("shell", "input", "tap", str(copy_x), str(copy_y))
            time.sleep(1.2)
            raw = run(["pbpaste"])
            if raw != sentinel:
                try:
                    payload = json.loads(raw)
                except json.JSONDecodeError:
                    pass
                else:
                    base = payload.get("BaseResp", {}) if isinstance(payload, dict) else {}
                    if base.get("StatusCode", 0) != 0:
                        raise RuntimeError("TikTok One returned a nonzero status")
                    return payload
            time.sleep(0.8 + attempt)
        raise RuntimeError("could not copy a JSON response from the TikTok WebView")


def crawl_campaigns(
    bridge: DeviceBridge, stages: list[str], limit: int, max_pages: int
) -> dict[str, Any]:
    result = {"homepage": bridge.fetch("homepage", {}), "stages": {}}
    for stage in stages:
        pages = []
        page = 1
        while page <= max_pages:
            payload = bridge.fetch(
                "collabs",
                {"collabStage": str(STAGES[stage]), "limit": str(limit), "page": str(page)},
            )
            pages.append(payload)
            pagination = payload.get("pagination", {})
            print(
                f"{stage}: page {page}/{pagination.get('pageCount', '?')} "
                f"({len(payload.get('orderList', []))} rows)",
                file=sys.stderr,
            )
            if not pagination.get("hasMore", False):
                break
            page += 1
        result["stages"][stage] = pages
    return result


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("route", choices=[*ROUTES, "campaigns"])
    parser.add_argument("--serial", default="ZY22KV9SVC")
    parser.add_argument("--param", action="append", default=[], metavar="KEY=VALUE")
    parser.add_argument("--stages", default="todo,pending,in-progress,done")
    parser.add_argument("--limit", type=int, default=20)
    parser.add_argument("--max-pages", type=int, default=100)
    parser.add_argument("--wait-seconds", type=float, default=3.0)
    parser.add_argument("--output", type=Path)
    args = parser.parse_args()

    for executable in ("adb", "scrcpy", "pbcopy", "pbpaste", "tesseract"):
        if not shutil.which(executable):
            parser.error(f"missing required executable: {executable}")
    if not 1 <= args.limit <= 100:
        parser.error("--limit must be between 1 and 100")

    try:
        with DeviceBridge(args.serial, args.wait_seconds) as bridge:
            if args.route == "campaigns":
                stages = parse_stages(args.stages)
                payload = crawl_campaigns(bridge, stages, args.limit, args.max_pages)
            else:
                payload = bridge.fetch(
                    args.route, parse_params(args.param, ROUTES[args.route][1])
                )
    except (OSError, subprocess.CalledProcessError, RuntimeError, ValueError) as exc:
        print(f"error: {exc}", file=sys.stderr)
        return 1

    rendered = json.dumps(payload, ensure_ascii=False, indent=2) + "\n"
    if args.output:
        args.output.parent.mkdir(parents=True, exist_ok=True)
        args.output.write_text(rendered, encoding="utf-8")
        print(f"wrote {args.output}", file=sys.stderr)
    else:
        print(rendered, end="")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
