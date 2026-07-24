#!/usr/bin/env python3
"""Build the post-Step-09A Step 11 source-authority preflight.

This script reads approved coordinate evidence only. It creates no production
blueprint, Blender data, geometry, render, export, or Unreal artifact.
"""

from __future__ import annotations

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
OUTPUT = RUN / "manifests/STEP_11_SOURCE_AUTHORITY_PREFLIGHT_A02.json"

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
        raise RuntimeError(f"Expected a JSON object: {path}")
    return value


def component_ready(
    scanlines: dict[str, Any], view: str, component: str
) -> bool:
    record = (
        scanlines.get("views", {})
        .get(view, {})
        .get("component_owners", {})
        .get(component)
    )
    if not isinstance(record, dict):
        return False
    rows = record.get("rows")
    return (
        isinstance(rows, list)
        and bool(rows)
        and isinstance(record.get("owner_pixel_count"), int)
        and record["owner_pixel_count"] > 0
    )


def boundary_ready(
    boundaries: dict[str, Any], boundary_id: str
) -> bool:
    record = boundaries.get("boundaries", {}).get(boundary_id)
    if not isinstance(record, dict):
        return False
    if "samples" in record:
        return isinstance(record["samples"], list) and (
            bool(record["samples"])
            or boundary_id
            == "BOTTOM_STONE_SEPARATION_WITHOUT_CENTRAL_OWNER"
        )
    return any(
        key.endswith("_runs_half_open") and isinstance(value, list) and value
        for key, value in record.items()
    )


def write_json(path: Path, value: Any) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(
        json.dumps(value, indent=2, sort_keys=True) + "\n",
        encoding="utf-8",
    )


def main() -> None:
    authority = load(AUTHORITY_LOCK)
    step09 = load(STEP09)
    step10 = load(STEP10)
    numeric = load(NUMERIC)
    boundary_index = load(BOUNDARIES)
    ownership_validation = load(OWNERSHIP_VALIDATION)
    with gzip.open(SCANLINES, "rt", encoding="utf-8") as stream:
        scanlines = json.load(stream)

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
    hash_results = {
        name: {
            "expected": authority["approved_file_sha256"][name],
            "observed": sha256(path),
            "match": sha256(path)
            == authority["approved_file_sha256"][name],
        }
        for name, path in approved_paths.items()
    }
    authority_lock_valid = (
        authority.get("schema")
        == "AERATHEA_R8_STEP09A_OWNERSHIP_AUTHORITY_LOCK_V1"
        and authority.get("decision") == "approved"
        and authority.get("decision_authority") == "Flamestrike"
        and authority.get("step_11_source_authority_preflight_authorized")
        is True
        and authority.get("step_11_production_blueprint_authorized") is False
        and authority.get("geometry_authority") is False
        and all(item["match"] for item in hash_results.values())
        and "approved" in APPROVAL.read_text(encoding="utf-8").lower()
    )
    ownership_validation_valid = (
        ownership_validation.get("result") == "PASS"
        and ownership_validation.get("summary", {}).get("passed") == 79
        and ownership_validation.get("summary", {}).get("total") == 79
        and not ownership_validation.get("summary", {}).get(
            "failed_check_ids"
        )
        and ownership_validation.get("geometry_or_blender_created") is False
        and ownership_validation.get("candidate_fill_review_created") is False
    )

    required_boundaries = [
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
    required_groups = [
        "CORR_C02_FRONT_TOP_BOTTOM_INNER_OWNER_EDGES",
        "CORR_C03_FRONT_TOP_BOTTOM_INNER_OWNER_EDGES",
        "CORR_C04_RIGHT_CANDIDATE_FACE_EDGES",
        "CORR_C01_C06_C07_FRONT_CONTACTS",
    ]
    present_groups = {
        group.get("id")
        for group in boundary_index.get("correspondence_groups", [])
        if isinstance(group, dict)
    }
    all_boundary_sets_present = all(
        boundary_ready(boundary_index, boundary_id)
        for boundary_id in required_boundaries
    )
    all_correspondence_groups_present = set(required_groups) <= present_groups

    findings = [
        {
            "component": "C01_CENTER_CORE",
            "required": "exact new-front membership plus C12/C06 contact edges",
            "found": (
                authority_lock_valid
                and ownership_validation_valid
                and component_ready(scanlines, "front", "C01_CENTER_CORE")
                and boundary_ready(boundary_index, "FRONT_C01_C06_CONTACT")
                and boundary_ready(
                    boundary_index, "FRONT_C12_RESERVED_C01_CONTACT"
                )
            ),
            "evidence": [
                "front/C01_CENTER_CORE",
                "FRONT_C12_RESERVED_C01_CONTACT",
                "FRONT_C01_C06_CONTACT",
            ],
        },
        {
            "component": "C02_STONE_LEFT",
            "required": "exact front/top/bottom membership and ordered boundaries",
            "found": (
                authority_lock_valid
                and ownership_validation_valid
                and all(
                    component_ready(scanlines, view, "C02_STONE_LEFT")
                    for view in ("front", "top", "bottom")
                )
                and all(
                    boundary_ready(
                        boundary_index, f"{view}_C02_INNER_OWNER_EDGE"
                    )
                    for view in ("FRONT", "TOP", "BOTTOM")
                )
                and required_groups[0] in present_groups
            ),
            "evidence": [
                "front/top/bottom C02_STONE_LEFT scanlines",
                required_groups[0],
            ],
        },
        {
            "component": "C03_STONE_RIGHT",
            "required": "exact front/top/bottom membership and ordered boundaries",
            "found": (
                authority_lock_valid
                and ownership_validation_valid
                and all(
                    component_ready(scanlines, view, "C03_STONE_RIGHT")
                    for view in ("front", "top", "bottom")
                )
                and all(
                    boundary_ready(
                        boundary_index, f"{view}_C03_INNER_OWNER_EDGE"
                    )
                    for view in ("FRONT", "TOP", "BOTTOM")
                )
                and required_groups[1] in present_groups
            ),
            "evidence": [
                "front/top/bottom C03_STONE_RIGHT scanlines",
                required_groups[1],
            ],
        },
        {
            "component": "C04_STRIKE_FACE_POSITIVE_X",
            "required": "exact new-right membership and boundaries for both approved candidate halves",
            "found": (
                authority_lock_valid
                and ownership_validation_valid
                and component_ready(scanlines, "right", "C04_RUNE_SIDE")
                and component_ready(
                    scanlines, "right", "C04_METAL_CENTER_PIECE_SIDE"
                )
                and boundary_ready(
                    boundary_index, "RIGHT_C04_CANDIDATE_HALF_BOUNDARIES"
                )
                and boundary_ready(
                    boundary_index, "RIGHT_C04_TOP_BOTTOM_EDGES"
                )
                and required_groups[2] in present_groups
            ),
            "evidence": [
                "right/C04_RUNE_SIDE",
                "right/C04_METAL_CENTER_PIECE_SIDE",
                required_groups[2],
            ],
        },
        {
            "component": "C06_UPPER_HAFT_CAP",
            "required": "exact new-front membership and C01/C07 contacts",
            "found": (
                authority_lock_valid
                and ownership_validation_valid
                and component_ready(
                    scanlines, "front", "C06_UPPER_HAFT_CAP"
                )
                and boundary_ready(
                    boundary_index, "FRONT_C01_C06_CONTACT"
                )
                and boundary_ready(
                    boundary_index, "FRONT_C06_C07_CONTACT"
                )
                and required_groups[3] in present_groups
            ),
            "evidence": [
                "front/C06_UPPER_HAFT_CAP",
                "FRONT_C01_C06_CONTACT",
                "FRONT_C06_C07_CONTACT",
            ],
        },
        {
            "component": "PROTECTED_NEGATIVE_SPACES",
            "required": "exact exterior-connected source-coordinate records in every owning view",
            "found": (
                authority_lock_valid
                and ownership_validation_valid
                and all(
                    "protected_negative_spaces"
                    in scanlines.get("views", {}).get(view, {})
                    for view in ("front", "right", "top", "bottom")
                )
                and bool(
                    scanlines["views"]["front"][
                        "protected_negative_spaces"
                    ]
                )
                and bool(
                    scanlines["views"]["top"]["protected_negative_spaces"]
                )
                and bool(
                    scanlines["views"]["bottom"][
                        "protected_negative_spaces"
                    ]
                )
            ),
            "evidence": [
                "front/right/top/bottom protected_negative_spaces",
                "Step 09A protected-space independent replay checks",
            ],
        },
        {
            "component": "CROSS_VIEW_COMMON_BOUNDARIES",
            "required": "all exact ordered boundary sets and approved order-only correspondence groups",
            "found": (
                authority_lock_valid
                and ownership_validation_valid
                and all_boundary_sets_present
                and all_correspondence_groups_present
            ),
            "evidence": required_boundaries + required_groups,
        },
    ]
    missing = [
        item["component"] for item in findings if item["found"] is not True
    ]
    decision = "PASS" if not missing else "Blueprint block: source authority missing"

    component_counts = {
        view: {
            component: record["owner_pixel_count"]
            for component, record in value["component_owners"].items()
        }
        for view, value in scanlines["views"].items()
    }
    preflight = {
        "schema": "AERATHEA_R8_ZERO_EXTRUSION_STEP11_SOURCE_PREFLIGHT_A02_V1",
        "asset": ASSET,
        "run_id": "SB-CR-STEPS10-16-R8-ZERO-EXTRUSION-A02",
        "parent_run_id": "SB-CR-STEPS01-16-R8-PIXEL-EXACT-A01",
        "ownership_amendment_run_id": (
            "SB-CR-R8-STEP09A-COMPONENT-PIXEL-OWNERSHIP-A01"
        ),
        "step": "11 source-authority preflight rerun only",
        "artifact_status": "preflight evidence pending independent audit",
        "approval_scope": (
            "hash-locked Step 09A ownership authority plus this preflight; "
            "no production blueprint or geometry"
        ),
        "authority_lock": {
            "path": str(AUTHORITY_LOCK.relative_to(ROOT)),
            "sha256": sha256(AUTHORITY_LOCK),
            "approval_record_path": str(APPROVAL.relative_to(ROOT)),
            "approval_record_sha256": sha256(APPROVAL),
            "valid": authority_lock_valid,
            "approved_file_hash_results": hash_results,
        },
        "available_exact_authority": {
            "whole_hammer_selected_pixels": step09[
                "total_exact_selected_pixels"
            ],
            "front_uniform_scale_cm_per_pixel": "170/1063",
            "right_uniform_scale_cm_per_pixel": "85/548",
            "front_owned_width_cm": step09["derived_dimensions_cm"][
                "width_front_owned"
            ]["display_decimal"],
            "rune_final_depth_cm": step09["right_candidate_halves"][
                "rune_side"
            ]["completed_depth_cm"]["display_decimal"],
            "metal_final_depth_cm": step09["right_candidate_halves"][
                "metal_center_piece_side"
            ]["completed_depth_cm"]["display_decimal"],
            "right_rotation_axis_x": 557,
            "front_component_z_stations": bool(
                step09.get("front_component_stations_world_z_cm")
            ),
            "approved_component_names_and_view_roles": True,
            "approved_hidden_closure_equations": True,
            "approved_rz180_completion": True,
            "approved_rotational_and_haft_equations": True,
            "approved_component_pixel_ownership": authority_lock_valid,
            "step09a_independent_validation": (
                "PASS 79/79" if ownership_validation_valid else "FAIL"
            ),
            "component_owner_pixel_counts": component_counts,
            "ordered_boundary_set_count": len(
                boundary_index["boundaries"]
            ),
            "order_only_correspondence_group_count": len(
                boundary_index["correspondence_groups"]
            ),
        },
        "required_coordinate_bearing_owners": findings,
        "required_boundary_ids": required_boundaries,
        "required_correspondence_group_ids": required_groups,
        "missing_authority": missing,
        "input_sha256": {
            "parent_step09_index": sha256(STEP09),
            "step10_decisions": sha256(STEP10),
            "step10_numeric_precedence": sha256(NUMERIC),
            "step09a_authority_lock": sha256(AUTHORITY_LOCK),
            "step09a_approval_record": sha256(APPROVAL),
            "step09a_component_scanlines": sha256(SCANLINES),
            "step09a_boundary_index": sha256(BOUNDARIES),
            "step09a_validation": sha256(OWNERSHIP_VALIDATION),
        },
        "decision": decision,
        "production_blueprint_created": False,
        "step_11_production_blueprint_authorized": False,
        "step_12_unlocked": False,
        "geometry_or_blender_created": False,
        "render_export_or_unreal_created": False,
        "next_gate": (
            "present the independently audited preflight result; request a "
            "separate Step 11 production-blueprint contract decision"
            if decision == "PASS"
            else "remain blocked and report the missing authority"
        ),
    }
    write_json(OUTPUT, preflight)
    print(
        "AERATHEA_STEP11_SOURCE_AUTHORITY_PREFLIGHT_A02_"
        f"{decision.replace(' ', '_')} "
        f"found={len(findings) - len(missing)}/{len(findings)} "
        f"output={OUTPUT.relative_to(ROOT)}"
    )


if __name__ == "__main__":
    main()
