#!/usr/bin/env python3
"""Independent Step 11 source-authority preflight for Siege Breaker R8."""

from __future__ import annotations

import gzip
import hashlib
import json
from pathlib import Path
from typing import Any, Iterable


ROOT = Path(__file__).resolve().parents[2]
ASSET = "SM_DRW_SiegeBreaker_Hammer_A01"
ASSET_ROOT = ROOT / "docs/assets/blueprints" / ASSET
PARENT = (
    ASSET_ROOT
    / "proof_runs/SB-CR-STEPS01-16-R8-PIXEL-EXACT-A01"
)
RUN = (
    ASSET_ROOT
    / "proof_runs/SB-CR-STEPS10-16-R8-ZERO-EXTRUSION-A02"
)
PREFLIGHT = RUN / "manifests/STEP_11_SOURCE_AUTHORITY_PREFLIGHT.json"
VALIDATION = RUN / "manifests/STEP_11_VALIDATION.json"
STEP04 = PARENT / "manifests/STEP_04_COMPONENT_AND_SOURCE_OWNERSHIP_INVENTORY.json"
STEP09 = PARENT / "manifests/STEP_09_INTEGRATED_EXACT_MEASUREMENT_INDEX.json"
STEP10 = RUN / "manifests/STEP_10_INTERPRETATION_DECISIONS.json"
NUMERIC = RUN / "manifests/STEP_10_NUMERIC_SUBSTITUTION_CLARIFICATION.json"
MEASUREMENTS = [
    PARENT / "manifests/STEP_06_FRONT_MEASUREMENT_CONTRACT.json",
    PARENT / "manifests/STEP_06_BACK_MEASUREMENT_CONTRACT.json",
    PARENT / "manifests/STEP_07_LEFT_MEASUREMENT_CONTRACT.json",
    PARENT / "manifests/STEP_07_RIGHT_MEASUREMENT_CONTRACT.json",
    PARENT / "manifests/STEP_08_TOP_MEASUREMENT_CONTRACT.json",
    PARENT / "manifests/STEP_08_BOTTOM_MEASUREMENT_CONTRACT.json",
]
CAPTURES = [
    PARENT
    / f"evidence/STEP_03_COMPLETE_HAMMER_SCANLINES/{view}_complete_hammer_scanlines.json.gz"
    for view in ("front", "back", "left", "right", "top", "bottom")
]


def sha256(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest()


def load(path: Path) -> dict[str, Any]:
    value = json.loads(path.read_text(encoding="utf-8"))
    if not isinstance(value, dict):
        raise RuntimeError(f"Expected JSON object: {path}")
    return value


def nested_keys(value: Any) -> Iterable[str]:
    if isinstance(value, dict):
        for key, child in value.items():
            yield str(key)
            yield from nested_keys(child)
    elif isinstance(value, list):
        for child in value:
            yield from nested_keys(child)


def add(
    checks: list[dict[str, Any]],
    name: str,
    observed: Any,
    expected: Any,
) -> None:
    checks.append(
        {
            "name": name,
            "pass": observed == expected,
            "observed": observed,
            "expected": expected,
        }
    )


def main() -> None:
    preflight = load(PREFLIGHT)
    step04 = load(STEP04)
    step09 = load(STEP09)
    step10 = load(STEP10)
    numeric = load(NUMERIC)
    measurements = [load(path) for path in MEASUREMENTS]
    checks: list[dict[str, Any]] = []

    add(
        checks,
        "preflight_schema",
        preflight.get("schema"),
        "AERATHEA_R8_ZERO_EXTRUSION_STEP11_SOURCE_PREFLIGHT_V1",
    )
    add(
        checks,
        "whole_pixel_total_matches_step09",
        preflight["available_exact_authority"]["whole_hammer_selected_pixels"],
        step09["total_exact_selected_pixels"],
    )
    add(
        checks,
        "front_width_matches_step09",
        preflight["available_exact_authority"]["front_owned_width_cm"],
        step09["derived_dimensions_cm"]["width_front_owned"]["display_decimal"],
    )
    add(
        checks,
        "rune_depth_matches_step09",
        preflight["available_exact_authority"]["rune_final_depth_cm"],
        step09["right_candidate_halves"]["rune_side"]["completed_depth_cm"][
            "display_decimal"
        ],
    )
    add(
        checks,
        "metal_depth_matches_step09",
        preflight["available_exact_authority"]["metal_final_depth_cm"],
        step09["right_candidate_halves"]["metal_center_piece_side"][
            "completed_depth_cm"
        ]["display_decimal"],
    )
    add(
        checks,
        "step04_coordinates_not_recorded",
        step04.get("pixel_coordinates_recorded"),
        False,
    )
    add(
        checks,
        "step04_correspondence_not_resolved",
        step04.get("cross_view_correspondence_resolved"),
        False,
    )
    add(
        checks,
        "step04_hidden_surface_not_resolved",
        step04.get("hidden_surface_resolved"),
        False,
    )
    add(
        checks,
        "all_required_coordinate_owners_absent",
        all(
            item.get("found") is False
            for item in preflight["required_coordinate_bearing_owners"]
        ),
        True,
    )
    add(
        checks,
        "required_owner_count",
        len(preflight["required_coordinate_bearing_owners"]),
        7,
    )

    forbidden_exact_owner_keys = {
        "component_pixel_ownership",
        "component_owner_mask",
        "component_boundary_coordinates",
        "negative_space_pixel_membership",
        "cross_view_boundary_correspondence",
    }
    measurement_keys = {
        key.lower()
        for record in measurements
        for key in nested_keys(record)
    }
    add(
        checks,
        "measurement_records_have_no_component_owner_coordinates",
        sorted(forbidden_exact_owner_keys & measurement_keys),
        [],
    )
    add(
        checks,
        "measurement_records_are_whole_view_profiles",
        all(
            "row_profiles" in record
            and "column_profiles" in record
            and "source_rectangle_half_open" in record
            for record in measurements
        ),
        True,
    )

    capture_schemas = []
    capture_views = []
    for path in CAPTURES:
        value = json.loads(gzip.decompress(path.read_bytes()))
        capture_schemas.append(value.get("schema"))
        capture_views.append(value.get("view"))
        add(
            checks,
            f"{value.get('view')}_capture_has_only_complete_hammer_selection",
            "component_pixel_ownership" not in value
            and "component_owner_masks" not in value
            and "rows_with_exact_rgba" in value,
            True,
        )
    add(
        checks,
        "all_six_capture_views_present",
        sorted(capture_views),
        ["back", "bottom", "front", "left", "right", "top"],
    )
    add(
        checks,
        "capture_schema_is_complete_hammer_scanline",
        all(
            schema == "AERATHEA_COMPLETE_HAMMER_RGBA_SCANLINES_V1"
            for schema in capture_schemas
        ),
        True,
    )

    step10_text = json.dumps(step10, sort_keys=True)
    add(
        checks,
        "step10_adds_no_component_coordinates",
        "component_boundary_coordinates" not in step10_text
        and "component_pixel_ownership" not in step10_text,
        True,
    )
    add(
        checks,
        "numeric_record_adds_no_component_coordinates",
        "component_boundary_coordinates"
        not in json.dumps(numeric, sort_keys=True),
        True,
    )
    add(
        checks,
        "production_blueprint_absent",
        (
            RUN / "manifests/STEP_11_PRODUCTION_GEOMETRY_BLUEPRINT.json"
        ).exists(),
        False,
    )
    add(
        checks,
        "preflight_decision_exact",
        preflight.get("decision"),
        "Blueprint block: source authority missing",
    )
    add(
        checks,
        "proposed_amendment_has_no_geometry_authority",
        preflight["proposed_recovery_amendment"]["geometry_authority"],
        False,
    )
    add(
        checks,
        "proposed_amendment_requires_flamestrike",
        preflight["proposed_recovery_amendment"][
            "requires_flamestrike_approval_before_execution"
        ],
        True,
    )

    evidence_checks_pass = all(item["pass"] for item in checks)
    missing = preflight["missing_authority"]
    result = "BLOCKED" if evidence_checks_pass and missing else "FAIL"
    report = {
        "schema": "AERATHEA_R8_ZERO_EXTRUSION_STEP11_VALIDATION_V1",
        "asset": ASSET,
        "run_id": "SB-CR-STEPS10-16-R8-ZERO-EXTRUSION-A02",
        "step": "11",
        "independent_validator": str(Path(__file__).relative_to(ROOT)),
        "input_sha256": {
            "preflight": sha256(PREFLIGHT),
            "step04_inventory": sha256(STEP04),
            "step09_index": sha256(STEP09),
            "step10_decisions": sha256(STEP10),
            "step10_numeric_precedence": sha256(NUMERIC),
            "measurements": {
                path.name: sha256(path) for path in MEASUREMENTS
            },
            "complete_hammer_captures": {
                path.name: sha256(path) for path in CAPTURES
            },
        },
        "checks": checks,
        "pass_count": sum(1 for item in checks if item["pass"]),
        "check_count": len(checks),
        "result": result,
        "block_code": (
            "Blueprint block: source authority missing"
            if result == "BLOCKED"
            else None
        ),
        "missing_authority": missing,
        "artifact_status": "proof only",
        "next_step_unlocked": None,
        "geometry_authority": False,
    }
    VALIDATION.write_text(
        json.dumps(report, indent=2, sort_keys=True) + "\n",
        encoding="utf-8",
    )
    print(
        f"AERATHEA_STEP_11_SOURCE_AUTHORITY_{result} "
        f"{report['pass_count']}/{report['check_count']}"
    )
    if result == "FAIL":
        raise SystemExit(1)


if __name__ == "__main__":
    main()
