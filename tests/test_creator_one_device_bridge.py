import importlib.util
from pathlib import Path

import pytest


SCRIPT = Path(__file__).parents[1] / "tools" / "creator_one_device_bridge.py"
SPEC = importlib.util.spec_from_file_location("creator_one_device_bridge", SCRIPT)
MODULE = importlib.util.module_from_spec(SPEC)
assert SPEC.loader is not None
SPEC.loader.exec_module(MODULE)


def test_device_bridge_is_get_only_and_first_party():
    assert MODULE.ORIGIN == "https://inapp.tiktokv.com"
    assert set(MODULE.ROUTES) == {
        "homepage",
        "collabs",
        "collab-detail",
        "order-detail",
        "folder-tree",
        "files",
        "posts",
        "analytics",
        "tracking",
        "generated-content",
    }


def test_parse_params_rejects_fields_outside_route_allowlist():
    assert MODULE.parse_params(["page=2", "limit=20"], ("page", "limit")) == {
        "page": "2",
        "limit": "20",
    }
    with pytest.raises(ValueError, match="unsupported parameter"):
        MODULE.parse_params(["apply=true"], ("page", "limit"))


def test_all_campaign_stages_are_available_and_deduplicated():
    stages = MODULE.parse_stages("todo,pending,in-progress,done,todo")
    assert stages == ["todo", "pending", "in-progress", "done"]
    assert [MODULE.STAGES[stage] for stage in stages] == [1, 2, 3, 4]


def test_unknown_campaign_stage_is_rejected():
    with pytest.raises(ValueError, match="unsupported stage"):
        MODULE.parse_stages("todo,explore")
