#!/usr/bin/env python3
"""Independently audit the post-Step-09A Step 11 source preflight.

This validator does not import the preflight builder and creates no production
blueprint, Blender data, geometry, render, export, or Unreal artifact.
"""

from __future__ import annotations

from collections import defaultdict
import gzip
import hashlib
import json
from pathlib import Path
from typing import Any


ROOT = Path(__file__).resolve().parents[2]
ASSET = "SM_DRW_SiegeBreaker_Hammer_A01"
ASSET_ROOT = ROOT / "docs/assets/blueprints" / ASSET
PARENT = ASSET_ROOT / "proof_runs/SB-CR-STEPS01-16-R8-PIXEL-EXACT-A01"
RUN = ASSET_ROOT / "proof_runs/SB-CR-STEPS10-16-R8-ZERO-EXTRUSION-A02"
OWNERSHIP = (
    ASSET_ROOT
    / "proof_runs/SB-CR-R8-STEP09A-COMPONENT-PIXEL-OWNERSHIP-A01"
)
PREFLIGHT = RUN / "manifests/STEP_11_SOURCE_AUTHORITY_PREFLIGHT_A02.json"
VALIDATION = RUN / "manifests/STEP_11_VALIDATION_A02.json"

AUTHORITY_LOCK = OWNERSHIP / "manifests/STEP_09A_AUTHORITY_LOCK.json"
APPROVAL = (
    OWNERSHIP / "steps/STEP_09A_OWNERSHIP_DECISION_APPROVAL_RECORD.md"
)
INTERPRETATION = (
    OWNERSHIP / "manifests/STEP_09A_INTERPRETATION_INPUT.json"
)
SCANLINES = OWNERSHIP / "evidence/STEP_09A_COMPONENT_SCANLINES.json.gz"
BOUNDARIES = (
    OWNERSHIP / "manifests/STEP_09A_BOUNDARY_AND_CORRESPONDENCE_INDEX.json"
)
OWNERSHIP_VALIDATION = OWNERSHIP / "manifests/STEP_09A_VALIDATION.json"
REVIEW_BOARD = (
    OWNERSHIP / "review/STEP_09A_COMPONENT_PIXEL_OWNERSHIP_REVIEW.png"
)
FRONT_MARKS = (
    OWNERSHIP
    / "evidence/STEP_09A_EXACT_MARKS/STEP_09A_FRONT_EXACT_MARKS.png"
)
RIGHT_MARKS = (
    OWNERSHIP
    / "evidence/STEP_09A_EXACT_MARKS/STEP_09A_RIGHT_EXACT_MARKS.png"
)
TOP_MARKS = (
    OWNERSHIP
    / "evidence/STEP_09A_EXACT_MARKS/STEP_09A_TOP_EXACT_MARKS.png"
)
BOTTOM_MARKS = (
    OWNERSHIP
    / "evidence/STEP_09A_EXACT_MARKS/STEP_09A_BOTTOM_EXACT_MARKS.png"
)
OWNERSHIP_OUTPUT = OWNERSHIP / "steps/STEP_09A_OUTPUT_RECORD.md"
OWNERSHIP_HANDOFF = (
    OWNERSHIP / "handoffs/STEP_09A_TO_STEP_11_HANDOFF.md"
)
STEP09 = PARENT / "manifests/STEP_09_INTEGRATED_EXACT_MEASUREMENT_INDEX.json"
STEP10 = RUN / "manifests/STEP_10_INTERPRETATION_DECISIONS.json"
NUMERIC = RUN / "manifests/STEP_10_NUMERIC_SUBSTITUTION_CLARIFICATION.json"


def sha256(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest()


def load(path: Path) -> dict[str, Any]:
    value = json.loads(path.read_text(encoding="utf-8"))
    if not isinstance(value, dict):
        raise RuntimeError(f"Expected JSON object: {path}")
    return value


def add(
    checks: list[dict[str, Any]],
    check_id: str,
    observed: Any,
    expected: Any,
) -> None:
    checks.append(
        {
            "id": check_id,
            "result": "PASS" if observed == expected else "FAIL",
            "observed": observed,
            "expected": expected,
        }
    )


def validate_component_record(
    record: dict[str, Any],
    rectangle: list[int],
) -> tuple[bool, dict[int, list[tuple[int, int]]], dict[str, int]]:
    x0, y0, x1, y1 = rectangle
    rows = record.get("rows")
    if not isinstance(rows, list):
        return False, {}, {}
    valid = True
    intervals: dict[int, list[tuple[int, int]]] = defaultdict(list)
    owner_total = 0
    selected_total = 0
    enclosed_total = 0
    previous_y = y0 - 1
    for row in rows:
        y = row.get("y")
        if not isinstance(y, int) or not y0 <= y < y1 or y <= previous_y:
            valid = False
            continue
        previous_y = y
        owner_runs = row.get("owner_runs_half_open")
        selected_runs = row.get("selected_runs_half_open")
        enclosed_runs = row.get("enclosed_source_runs_half_open")
        if not all(
            isinstance(value, list)
            for value in (owner_runs, selected_runs, enclosed_runs)
        ):
            valid = False
            continue
        previous_end = x0
        row_owner = 0
        for run in owner_runs:
            if (
                not isinstance(run, list)
                or len(run) != 2
                or not all(isinstance(value, int) for value in run)
            ):
                valid = False
                continue
            start, end = run
            if not (x0 <= start < end <= x1 and start >= previous_end):
                valid = False
            previous_end = end
            row_owner += end - start
            intervals[y].append((start, end))
        row_selected = sum(end - start for start, end in selected_runs)
        row_enclosed = sum(end - start for start, end in enclosed_runs)
        if (
            row.get("owner_pixel_count") != row_owner
            or row_selected + row_enclosed != row_owner
        ):
            valid = False
        owner_total += row_owner
        selected_total += row_selected
        enclosed_total += row_enclosed
    totals = {
        "owner": owner_total,
        "selected": selected_total,
        "enclosed": enclosed_total,
    }
    if (
        record.get("owner_pixel_count") != owner_total
        or record.get("selected_capture_pixel_count") != selected_total
        or record.get("enclosed_source_pixel_count") != enclosed_total
        or owner_total != selected_total + enclosed_total
    ):
        valid = False
    return valid, intervals, totals


def validate_view_overlap(
    interval_sets: dict[str, dict[int, list[tuple[int, int]]]]
) -> tuple[bool, int]:
    overlap_count = 0
    all_rows = {
        y
        for component_rows in interval_sets.values()
        for y in component_rows
    }
    for y in all_rows:
        intervals: list[tuple[int, int, str]] = []
        for component, component_rows in interval_sets.items():
            intervals.extend(
                (start, end, component)
                for start, end in component_rows.get(y, [])
            )
        intervals.sort()
        for index, (start, end, component) in enumerate(intervals):
            for next_start, next_end, next_component in intervals[index + 1 :]:
                if next_start >= end:
                    break
                if next_component != component:
                    overlap_count += max(
                        0, min(end, next_end) - max(start, next_start)
                    )
    return overlap_count == 0, overlap_count


def validate_boundary(
    boundary: dict[str, Any], rectangle: list[int]
) -> bool:
    x0, y0, x1, y1 = rectangle
    valid = True
    samples = boundary.get("samples")
    if samples is not None:
        if not isinstance(samples, list):
            return False
        prior_y = y0 - 1
        for sample in samples:
            y = sample.get("y")
            if not isinstance(y, int) or not y0 <= y < y1 or y <= prior_y:
                valid = False
                continue
            prior_y = y
            for key, value in sample.items():
                if key.endswith("_edge_x"):
                    if not isinstance(value, int) or not x0 <= value <= x1:
                        valid = False
                elif key.endswith("_runs_half_open"):
                    if not validate_runs(value, x0, x1):
                        valid = False
    for key, value in boundary.items():
        if key.endswith("_runs_half_open"):
            if not validate_runs(value, x0, x1):
                valid = False
        elif key.endswith("_source_row"):
            if not isinstance(value, int) or not y0 <= value < y1:
                valid = False
        elif key.endswith("_source_edge_y"):
            if not isinstance(value, int) or not y0 <= value <= y1:
                valid = False
    return valid


def validate_runs(value: Any, x0: int, x1: int) -> bool:
    if not isinstance(value, list):
        return False
    previous_end = x0
    for run in value:
        if (
            not isinstance(run, list)
            or len(run) != 2
            or not all(isinstance(item, int) for item in run)
        ):
            return False
        start, end = run
        if not (x0 <= start < end <= x1 and start >= previous_end):
            return False
        previous_end = end
    return True


def main() -> int:
    checks: list[dict[str, Any]] = []
    preflight = load(PREFLIGHT)
    authority = load(AUTHORITY_LOCK)
    interpretation = load(INTERPRETATION)
    boundary_index = load(BOUNDARIES)
    ownership_validation = load(OWNERSHIP_VALIDATION)
    step09 = load(STEP09)
    with gzip.open(SCANLINES, "rt", encoding="utf-8") as stream:
        scanlines = json.load(stream)

    add(
        checks,
        "preflight_schema",
        preflight.get("schema"),
        "AERATHEA_R8_ZERO_EXTRUSION_STEP11_SOURCE_PREFLIGHT_A02_V1",
    )
    add(checks, "preflight_asset", preflight.get("asset"), ASSET)
    add(checks, "preflight_decision", preflight.get("decision"), "PASS")
    add(checks, "preflight_missing_authority", preflight.get("missing_authority"), [])
    add(
        checks,
        "production_blueprint_not_created",
        preflight.get("production_blueprint_created"),
        False,
    )
    add(
        checks,
        "step11_blueprint_not_authorized",
        preflight.get("step_11_production_blueprint_authorized"),
        False,
    )
    add(
        checks,
        "step12_not_unlocked",
        preflight.get("step_12_unlocked"),
        False,
    )
    add(
        checks,
        "no_geometry_or_blender",
        preflight.get("geometry_or_blender_created"),
        False,
    )
    add(
        checks,
        "no_render_export_or_unreal",
        preflight.get("render_export_or_unreal_created"),
        False,
    )

    approval_text = APPROVAL.read_text(encoding="utf-8")
    add(checks, "approval_response_exact", "> approved" in approval_text, True)
    add(
        checks,
        "approval_scope_excludes_blueprint_geometry_step12",
        all(
            text in approval_text
            for text in (
                "does not authorize:",
                "Step 11 production blueprint",
                "Blender or geometry",
                "Step 12",
            )
        ),
        True,
    )
    add(
        checks,
        "authority_lock_schema",
        authority.get("schema"),
        "AERATHEA_R8_STEP09A_OWNERSHIP_AUTHORITY_LOCK_V1",
    )
    add(checks, "authority_lock_decision", authority.get("decision"), "approved")
    add(
        checks,
        "authority_lock_decision_authority",
        authority.get("decision_authority"),
        "Flamestrike",
    )
    add(
        checks,
        "authority_lock_preflight_authorized",
        authority.get("step_11_source_authority_preflight_authorized"),
        True,
    )
    add(
        checks,
        "authority_lock_blueprint_not_authorized",
        authority.get("step_11_production_blueprint_authorized"),
        False,
    )
    add(
        checks,
        "authority_lock_geometry_not_authorized",
        authority.get("geometry_authority"),
        False,
    )

    approved_paths = {
        "interpretation_input": INTERPRETATION,
        "component_scanlines": SCANLINES,
        "boundary_and_correspondence_index": BOUNDARIES,
        "independent_validation": OWNERSHIP_VALIDATION,
        "review_board": REVIEW_BOARD,
        "front_exact_marks": FRONT_MARKS,
        "right_exact_marks": RIGHT_MARKS,
        "top_exact_marks": TOP_MARKS,
        "bottom_exact_marks": BOTTOM_MARKS,
        "output_record": OWNERSHIP_OUTPUT,
        "candidate_handoff": OWNERSHIP_HANDOFF,
    }
    for name, path in approved_paths.items():
        observed = sha256(path)
        expected = authority["approved_file_sha256"][name]
        add(checks, f"approved_hash_{name}", observed, expected)
        add(
            checks,
            f"preflight_hash_result_{name}",
            preflight["authority_lock"]["approved_file_hash_results"][name],
            {"expected": expected, "observed": observed, "match": True},
        )
    add(
        checks,
        "preflight_authority_lock_hash",
        preflight["authority_lock"]["sha256"],
        sha256(AUTHORITY_LOCK),
    )
    add(
        checks,
        "preflight_approval_record_hash",
        preflight["authority_lock"]["approval_record_sha256"],
        sha256(APPROVAL),
    )
    add(
        checks,
        "preflight_authority_lock_valid",
        preflight["authority_lock"]["valid"],
        True,
    )

    add(
        checks,
        "step09a_validation_result",
        ownership_validation.get("result"),
        "PASS",
    )
    add(
        checks,
        "step09a_validation_count",
        [
            ownership_validation.get("summary", {}).get("passed"),
            ownership_validation.get("summary", {}).get("total"),
            ownership_validation.get("summary", {}).get("failed_check_ids"),
        ],
        [79, 79, []],
    )
    add(
        checks,
        "step09a_validation_all_checks_pass",
        all(
            item.get("result") == "PASS"
            for item in ownership_validation.get("checks", [])
        ),
        True,
    )
    add(
        checks,
        "step09a_validation_no_geometry",
        ownership_validation.get("geometry_or_blender_created"),
        False,
    )
    add(
        checks,
        "step09a_validation_no_filled_review",
        ownership_validation.get("candidate_fill_review_created"),
        False,
    )

    add(
        checks,
        "scanline_schema",
        scanlines.get("schema"),
        "AERATHEA_R8_STEP09A_COMPONENT_SCANLINES_V1",
    )
    required_components = {
        "front": {
            "C01_CENTER_CORE",
            "C02_STONE_LEFT",
            "C03_STONE_RIGHT",
            "C06_UPPER_HAFT_CAP",
            "C12_RESERVED_EXISTING_OWNER",
        },
        "right": {
            "C01_SIDE_RESERVED_IN_METAL_HALF",
            "C04_METAL_CENTER_PIECE_SIDE",
            "C04_RUNE_SIDE",
        },
        "top": {
            "C02_STONE_LEFT",
            "C03_STONE_RIGHT",
            "CENTRAL_NON_STONE_RESERVED",
        },
        "bottom": {
            "C02_STONE_LEFT",
            "C03_STONE_RIGHT",
            "CENTRAL_NON_STONE_RESERVED",
        },
    }
    all_interval_sets: dict[
        str, dict[str, dict[int, list[tuple[int, int]]]]
    ] = {}
    calculated_counts: dict[str, dict[str, int]] = {}
    for view, expected_components in required_components.items():
        view_record = scanlines["views"][view]
        rectangle = view_record["rectangle_half_open"]
        observed_components = set(view_record["component_owners"])
        add(
            checks,
            f"{view}_component_set",
            sorted(observed_components),
            sorted(expected_components),
        )
        all_interval_sets[view] = {}
        calculated_counts[view] = {}
        for component in sorted(expected_components):
            valid, intervals, totals = validate_component_record(
                view_record["component_owners"][component], rectangle
            )
            add(checks, f"{view}_{component}_record_valid", valid, True)
            add(
                checks,
                f"{view}_{component}_owner_nonempty",
                totals.get("owner", 0) > 0,
                True,
            )
            all_interval_sets[view][component] = intervals
            calculated_counts[view][component] = totals["owner"]
        overlap_ok, overlap_count = validate_view_overlap(
            all_interval_sets[view]
        )
        add(
            checks,
            f"{view}_component_overlap_pixels",
            overlap_count,
            0,
        )
        add(checks, f"{view}_component_overlap_gate", overlap_ok, True)
        protected = view_record.get("protected_negative_spaces")
        protected_valid = isinstance(protected, list)
        if protected_valid:
            x0, y0, x1, y1 = rectangle
            for item in protected:
                y = item.get("y")
                if not isinstance(y, int) or not y0 <= y < y1:
                    protected_valid = False
                    break
                if not validate_runs(item.get("runs_half_open"), x0, x1):
                    protected_valid = False
                    break
        add(
            checks,
            f"{view}_protected_records_coordinate_valid",
            protected_valid,
            True,
        )
    add(
        checks,
        "preflight_component_counts_match_direct_replay",
        preflight["available_exact_authority"]["component_owner_pixel_counts"],
        calculated_counts,
    )

    required_boundary_ids = [
        "FRONT_C02_INNER_OWNER_EDGE",
        "FRONT_C03_INNER_OWNER_EDGE",
        "FRONT_C01_C06_CONTACT",
        "FRONT_C06_C07_CONTACT",
        "FRONT_C12_RESERVED_C01_CONTACT",
        "RIGHT_C04_CANDIDATE_HALF_BOUNDARIES",
        "RIGHT_C04_TOP_BOTTOM_EDGES",
        "TOP_C02_INNER_OWNER_EDGE",
        "TOP_C03_INNER_OWNER_EDGE",
        "TOP_STONE_SEPARATION_WITHOUT_CENTRAL_OWNER",
        "BOTTOM_C02_INNER_OWNER_EDGE",
        "BOTTOM_C03_INNER_OWNER_EDGE",
        "BOTTOM_STONE_SEPARATION_WITHOUT_CENTRAL_OWNER",
    ]
    add(
        checks,
        "preflight_required_boundary_ids",
        preflight.get("required_boundary_ids"),
        required_boundary_ids,
    )
    add(
        checks,
        "boundary_id_set",
        sorted(boundary_index["boundaries"]),
        sorted(required_boundary_ids),
    )
    rectangles = {
        view: scanlines["views"][view]["rectangle_half_open"]
        for view in ("front", "right", "top", "bottom")
    }
    for boundary_id in required_boundary_ids:
        boundary = boundary_index["boundaries"][boundary_id]
        add(
            checks,
            f"{boundary_id}_coordinate_valid",
            validate_boundary(boundary, rectangles[boundary["view"]]),
            True,
        )
    required_group_ids = [
        "CORR_C02_FRONT_TOP_BOTTOM_INNER_OWNER_EDGES",
        "CORR_C03_FRONT_TOP_BOTTOM_INNER_OWNER_EDGES",
        "CORR_C04_RIGHT_CANDIDATE_FACE_EDGES",
        "CORR_C01_C06_C07_FRONT_CONTACTS",
    ]
    add(
        checks,
        "preflight_required_group_ids",
        preflight.get("required_correspondence_group_ids"),
        required_group_ids,
    )
    groups = boundary_index["correspondence_groups"]
    add(
        checks,
        "correspondence_group_ids",
        [group["id"] for group in groups],
        required_group_ids,
    )
    add(
        checks,
        "correspondence_group_boundary_references",
        all(
            boundary_id in boundary_index["boundaries"]
            for group in groups
            for boundary_id in group["ordered_boundary_ids"]
        ),
        True,
    )
    required_groups = [
        {
            "id": "CORR_C02_FRONT_TOP_BOTTOM_INNER_OWNER_EDGES",
            "component": "C02_STONE_LEFT",
            "ordered_boundary_ids": [
                "FRONT_C02_INNER_OWNER_EDGE",
                "TOP_C02_INNER_OWNER_EDGE",
                "BOTTOM_C02_INNER_OWNER_EDGE",
            ],
            "scope": "ordered exact source-edge sets only; no point pairing or surface created",
        },
        {
            "id": "CORR_C03_FRONT_TOP_BOTTOM_INNER_OWNER_EDGES",
            "component": "C03_STONE_RIGHT",
            "ordered_boundary_ids": [
                "FRONT_C03_INNER_OWNER_EDGE",
                "TOP_C03_INNER_OWNER_EDGE",
                "BOTTOM_C03_INNER_OWNER_EDGE",
            ],
            "scope": "ordered exact source-edge sets only; no point pairing or surface created",
        },
        {
            "id": "CORR_C04_RIGHT_CANDIDATE_FACE_EDGES",
            "component": "C04_STRIKE_FACE_POSITIVE_X",
            "ordered_boundary_ids": [
                "RIGHT_C04_CANDIDATE_HALF_BOUNDARIES",
                "RIGHT_C04_TOP_BOTTOM_EDGES",
            ],
            "scope": "two candidate-specific ordered source-edge sets about x=557",
        },
        {
            "id": "CORR_C01_C06_C07_FRONT_CONTACTS",
            "component": "C06_UPPER_HAFT_CAP",
            "ordered_boundary_ids": [
                "FRONT_C01_C06_CONTACT",
                "FRONT_C06_C07_CONTACT",
            ],
            "scope": "exact adjacent source-row edge sets only",
        },
    ]
    add(
        checks,
        "correspondence_groups_exact_order_only_records",
        groups,
        required_groups,
    )

    add(
        checks,
        "all_seven_required_owners_found",
        [
            item["component"]
            for item in preflight["required_coordinate_bearing_owners"]
            if item.get("found") is True
        ],
        [
            "C01_CENTER_CORE",
            "C02_STONE_LEFT",
            "C03_STONE_RIGHT",
            "C04_STRIKE_FACE_POSITIVE_X",
            "C06_UPPER_HAFT_CAP",
            "PROTECTED_NEGATIVE_SPACES",
            "CROSS_VIEW_COMMON_BOUNDARIES",
        ],
    )
    add(
        checks,
        "whole_pixel_total_matches_parent",
        preflight["available_exact_authority"]["whole_hammer_selected_pixels"],
        step09["total_exact_selected_pixels"],
    )
    add(
        checks,
        "front_width_matches_parent",
        preflight["available_exact_authority"]["front_owned_width_cm"],
        step09["derived_dimensions_cm"]["width_front_owned"][
            "display_decimal"
        ],
    )
    add(
        checks,
        "rune_depth_matches_parent",
        preflight["available_exact_authority"]["rune_final_depth_cm"],
        step09["right_candidate_halves"]["rune_side"][
            "completed_depth_cm"
        ]["display_decimal"],
    )
    add(
        checks,
        "metal_depth_matches_parent",
        preflight["available_exact_authority"]["metal_final_depth_cm"],
        step09["right_candidate_halves"]["metal_center_piece_side"][
            "completed_depth_cm"
        ]["display_decimal"],
    )
    expected_input_hashes = {
        "parent_step09_index": sha256(STEP09),
        "step10_decisions": sha256(STEP10),
        "step10_numeric_precedence": sha256(NUMERIC),
        "step09a_authority_lock": sha256(AUTHORITY_LOCK),
        "step09a_approval_record": sha256(APPROVAL),
        "step09a_component_scanlines": sha256(SCANLINES),
        "step09a_boundary_index": sha256(BOUNDARIES),
        "step09a_validation": sha256(OWNERSHIP_VALIDATION),
    }
    add(
        checks,
        "preflight_input_hashes",
        preflight.get("input_sha256"),
        expected_input_hashes,
    )
    add(
        checks,
        "production_blueprint_file_absent",
        (
            RUN / "manifests/STEP_11_PRODUCTION_GEOMETRY_BLUEPRINT.json"
        ).exists(),
        False,
    )

    failures = [
        item["id"] for item in checks if item["result"] != "PASS"
    ]
    result = "PASS" if not failures else "FAIL"
    report = {
        "schema": "AERATHEA_R8_ZERO_EXTRUSION_STEP11_VALIDATION_A02_V1",
        "asset": ASSET,
        "run_id": "SB-CR-STEPS10-16-R8-ZERO-EXTRUSION-A02",
        "step": "11 source-authority preflight rerun only",
        "artifact_status": "proof only",
        "independent_validator": str(Path(__file__).relative_to(ROOT)),
        "input_sha256": {
            "preflight_a02": sha256(PREFLIGHT),
            **expected_input_hashes,
        },
        "checks": checks,
        "pass_count": sum(
            item["result"] == "PASS" for item in checks
        ),
        "check_count": len(checks),
        "failed_check_ids": failures,
        "result": result,
        "source_authority_preflight_decision": (
            "PASS" if result == "PASS" else "FAIL"
        ),
        "missing_authority": (
            [] if result == "PASS" else preflight.get("missing_authority")
        ),
        "production_blueprint_created": False,
        "step_11_production_blueprint_authorized": False,
        "step_12_unlocked": False,
        "geometry_authority": False,
        "unreal_authority": False,
        "next_gate": (
            "Flamestrike decision on a separately stated Step 11 "
            "production-blueprint contract"
            if result == "PASS"
            else "stop and correct the failed evidence checks"
        ),
    }
    VALIDATION.write_text(
        json.dumps(report, indent=2, sort_keys=True) + "\n",
        encoding="utf-8",
    )
    print(
        f"AERATHEA_STEP11_SOURCE_AUTHORITY_A02_{result} "
        f"{report['pass_count']}/{report['check_count']} "
        f"validation={VALIDATION.relative_to(ROOT)}"
    )
    return 0 if result == "PASS" else 1


if __name__ == "__main__":
    raise SystemExit(main())
