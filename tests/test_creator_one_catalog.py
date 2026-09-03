import importlib.util
from pathlib import Path

SCRIPT = Path(__file__).parents[1] / "tools" / "build_creator_one_catalog.py"
CATALOG = Path(__file__).parents[1] / "research" / "creator-one-endpoint-catalog.json"
SPEC = importlib.util.spec_from_file_location("build_creator_one_catalog", SCRIPT)
MODULE = importlib.util.module_from_spec(SPEC)
assert SPEC.loader is not None
SPEC.loader.exec_module(MODULE)


def test_catalog_annotations_cover_safety_and_plain_english():
    get_route = MODULE.annotate(
        {
            "method": "GET",
            "path": "/CreativeOne/OrderQuery/CreatorGetOrderDetail",
            "payload": "params",
            "fields": ["orderID"],
            "read_only": True,
            "observed_wrapper": True,
        }
    )
    assert get_route["service"] == "OrderQuery"
    assert get_route["classification"] == "read-only"
    assert "creator get order detail" in get_route["plain_english"].lower()
    assert get_route["live_validation"]["status"] == "validated"


def test_catalog_marks_post_and_unknown_as_unsafe_to_probe():
    base = {
        "path": "/CreativeOne/OrderCommand/CreatorQuitOrder",
        "payload": "data",
        "fields": ["orderID"],
        "read_only": False,
        "observed_wrapper": True,
    }
    post = MODULE.annotate({**base, "method": "POST"})
    unknown = MODULE.annotate({**base, "method": None, "payload": None, "observed_wrapper": False})
    assert post["classification"] == "action-or-mutation"
    assert "Do not call" in post["safe_usage"]
    assert unknown["classification"] == "unknown"
    assert "Do not call" in unknown["safe_usage"]


def test_builder_deduplicates_routes_through_extractor():
    source = b'''genBaseURL("/CreativeOne/Creator/GetProfile"),request({method:"GET"})\n"/CreativeOne/Creator/GetProfile"'''
    catalog = MODULE.build(source)
    assert catalog["route_count"] == 1
    assert catalog["method_counts"] == {"GET": 1}


def test_checked_in_catalog_is_complete_and_internally_consistent():
    import json

    catalog = json.loads(CATALOG.read_text())
    paths = [route["path"] for route in catalog["routes"]]
    methods = [route["method"] or "UNKNOWN" for route in catalog["routes"]]
    assert catalog["scope"] == "TikTok One /CreativeOne endpoints only"
    assert catalog["route_count"] == len(paths) == len(set(paths)) == 564
    assert (
        catalog["method_counts"]
        == {
            "UNKNOWN": methods.count("UNKNOWN"),
            "GET": methods.count("GET"),
            "POST": methods.count("POST"),
        }
        == {"UNKNOWN": 427, "GET": 87, "POST": 50}
    )
    assert sum(catalog["service_counts"].values()) == 564
    assert catalog["live_validated_count"] == 8
    assert all(route["plain_english"] and route["safe_usage"] for route in catalog["routes"])
