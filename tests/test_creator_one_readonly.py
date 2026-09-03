import importlib.util
from pathlib import Path


SCRIPT = Path(__file__).parents[1] / "tools" / "creator_one_readonly.py"
SPEC = importlib.util.spec_from_file_location("creator_one_readonly", SCRIPT)
MODULE = importlib.util.module_from_spec(SPEC)
assert SPEC.loader is not None
SPEC.loader.exec_module(MODULE)


def test_default_operational_stage_mapping():
    stages = MODULE.parse_stages("todo,pending,done,todo")
    assert stages == ["todo", "pending", "done"]
    assert [MODULE.STAGES[stage] for stage in stages] == ["1", "2", "4"]


def test_campaign_crawl_excludes_in_progress_and_stops_pagination(monkeypatch):
    calls = []

    def fake_request(route, values, *_args):
        calls.append((route, values.copy()))
        if route == "homepage":
            return {"data": {"todoCnt": 3}}
        page = int(values["page"])
        rows = [{"id": 1}, {"id": 2}] if page == 1 else [{"id": 3}]
        return {"data": {"orderList": rows}}

    monkeypatch.setattr(MODULE, "request", fake_request)
    payload = MODULE.crawl_campaigns(
        ["todo", "pending", "done"], 2, 10, "", "token", "inapp-us", True, None
    )

    collab_calls = [values for route, values in calls if route == "collabs"]
    assert [values["collabStage"] for values in collab_calls] == [
        "1", "1", "2", "2", "4", "4"
    ]
    assert set(payload["stages"]) == {"todo", "pending", "done"}

