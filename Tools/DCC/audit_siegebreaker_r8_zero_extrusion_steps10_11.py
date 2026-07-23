#!/usr/bin/env python3
"""Independent pre-DCC audit for Siege Breaker R8 zero-extrusion recovery.

This validator reads authority and production records directly. It does not
import the production builder and does not accept builder-authored pass flags.
"""

from __future__ import annotations

import argparse
import hashlib
import json
from pathlib import Path
from typing import Any


ROOT = Path(__file__).resolve().parents[2]
ASSET = "SM_DRW_SiegeBreaker_Hammer_A01"
ASSET_ROOT = ROOT / "docs/assets/blueprints" / ASSET
RUN_ROOT = (
    ASSET_ROOT
    / "proof_runs/SB-CR-STEPS10-16-R8-ZERO-EXTRUSION-A02"
)
PARENT_ROOT = (
    ASSET_ROOT
    / "proof_runs/SB-CR-STEPS01-16-R8-PIXEL-EXACT-A01"
)

DECISIONS = RUN_ROOT / "manifests/STEP_10_INTERPRETATION_DECISIONS.json"
NUMERIC_SUBSTITUTION = (
    RUN_ROOT / "manifests/STEP_10_NUMERIC_SUBSTITUTION_CLARIFICATION.json"
)
STEP10_VALIDATION = RUN_ROOT / "manifests/STEP_10_VALIDATION.json"
BLUEPRINT = RUN_ROOT / "manifests/STEP_11_PRODUCTION_GEOMETRY_BLUEPRINT.json"
STEP11_VALIDATION = RUN_ROOT / "manifests/STEP_11_VALIDATION.json"

AUTHORITY_FILES = {
    "execution_contract": (
        ASSET_ROOT / "steps/A12_R10_R8_PIXEL_EXACT_STEPS01_16_A01_CONTRACT.md",
        "77b0339126388be01f59532cd6b79228450b61e739ebc10c2f849833fd337bd4",
    ),
    "component_equations": (
        ASSET_ROOT / "steps/A12_R10_STEP02_COMPONENT_EQUATION_CONTRACT_DRAFT.md",
        "a40d0b67d802687ac3c9ec9ad8e00a915cc1dc730ce31f3fab00b18a1837a21c",
    ),
    "view_owned_scale_contract": (
        ASSET_ROOT
        / "steps/A12_R10_STEP02A_R8_VIEW_OWNED_SCALE_RECONCILIATION_A01_CONTRACT.md",
        "84da92d2bec200a646bee4297965e9cd3bcd9aac090381b4108d931d7c1f4cd7",
    ),
    "source_half_contract": (
        ASSET_ROOT
        / "steps/A12_R10_STEP06_ONE_RZ180_SOURCE_HALF_ASSEMBLY_A01_CONTRACT.md",
        "eba4884b6b52178846854b59c88594fc3aa896067d868f6748d4aadd3bc4106a",
    ),
    "closure_amendment": (
        ASSET_ROOT / "steps/A12_R10_STEP06A_DETERMINISTIC_CLOSURE_AMENDMENT_A01.md",
        "8ee99d2b5c510a540623aa4a69154b3bc0da9c7a9e846a42194a0dabe716d1b4",
    ),
    "step09_index": (
        PARENT_ROOT / "manifests/STEP_09_INTEGRATED_EXACT_MEASUREMENT_INDEX.json",
        "5a0a3eea8f877d55216f9efabe15b0ee1cf938e4c15a825a0e218f72ba76839a",
    ),
    "step09_pre_geometry_audit": (
        PARENT_ROOT / "manifests/STEP_09_PRE_GEOMETRY_EXACT_DATA_AUDIT.json",
        "260c79857fe059517b4076bcc65b538aef807a7be33a58a4a46edc32c2150fdb",
    ),
}


def sha256(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest()


def load_json(path: Path) -> dict[str, Any]:
    value = json.loads(path.read_text(encoding="utf-8"))
    if not isinstance(value, dict):
        raise RuntimeError(f"Expected JSON object: {path}")
    return value


def check(
    checks: list[dict[str, Any]],
    name: str,
    observed: Any,
    expected: Any = True,
) -> None:
    passed = observed == expected
    if isinstance(observed, set):
        observed = sorted(observed)
    if isinstance(expected, set):
        expected = sorted(expected)
    checks.append(
        {
            "name": name,
            "pass": passed,
            "observed": observed,
            "expected": expected,
        }
    )


def authority_checks(checks: list[dict[str, Any]]) -> None:
    for name, (path, expected_hash) in AUTHORITY_FILES.items():
        check(checks, f"{name}_exists", path.is_file())
        observed = sha256(path) if path.is_file() else None
        check(checks, f"{name}_sha256", observed, expected_hash)


def audit_step10() -> dict[str, Any]:
    checks: list[dict[str, Any]] = []
    authority_checks(checks)
    record = load_json(DECISIONS)
    numeric = load_json(NUMERIC_SUBSTITUTION)
    matrix = load_json(
        PARENT_ROOT / "manifests/STEP_09_DISAGREEMENT_UNKNOWN_MATRIX.json"
    )
    inventory = load_json(
        PARENT_ROOT
        / "manifests/STEP_04_COMPONENT_AND_SOURCE_OWNERSHIP_INVENTORY.json"
    )
    cross_view = load_json(
        PARENT_ROOT / "manifests/STEP_09_CROSS_VIEW_CORRESPONDENCE.json"
    )
    step09_index = load_json(
        PARENT_ROOT / "manifests/STEP_09_INTEGRATED_EXACT_MEASUREMENT_INDEX.json"
    )
    execution_contract_text = AUTHORITY_FILES["execution_contract"][0].read_text(
        encoding="utf-8"
    )

    expected_dx = {f"DX{index:03d}" for index in range(1, 6)}
    expected_uk = {f"UK{index:03d}" for index in range(1, 13)}
    source_dx = {item["id"] for item in matrix["items"]}
    source_uk = {item["id"] for item in inventory["unresolved_unknowns"]}
    resolved_dx = {item["id"] for item in record["disagreement_resolutions"]}
    resolved_uk = {item["id"] for item in record["unknown_resolutions"]}

    check(checks, "record_schema", record.get("schema"),
          "AERATHEA_R8_ZERO_EXTRUSION_STEP10_DECISIONS_V1")
    check(checks, "record_step", record.get("step"), "10")
    check(checks, "geometry_created_false", record.get("geometry_created"), False)
    check(
        checks,
        "new_interpretation_created_false",
        record.get("new_interpretation_created"),
        False,
    )
    check(checks, "source_disagreement_ids_exact", source_dx, expected_dx)
    check(checks, "source_unknown_ids_exact", source_uk, expected_uk)
    check(checks, "resolved_disagreement_ids_exact", resolved_dx, expected_dx)
    check(checks, "resolved_unknown_ids_exact", resolved_uk, expected_uk)
    check(
        checks,
        "all_disagreements_use_existing_rules",
        all(
            item.get("status") == "resolved_by_existing_approved_rule"
            and bool(item.get("authority"))
            for item in record["disagreement_resolutions"]
        ),
    )
    check(
        checks,
        "all_unknowns_use_existing_rules",
        all(
            item.get("status") == "resolved_by_existing_approved_rule"
            and bool(item.get("authority"))
            for item in record["unknown_resolutions"]
        ),
    )
    check(
        checks,
        "no_unresolved_geometry_affecting_items",
        record.get("unresolved_geometry_affecting_items"),
        [],
    )
    check(
        checks,
        "parent_cross_view_waited_for_step10",
        cross_view.get("hidden_surface_correspondence"),
        "unresolved until Step 10",
    )

    rules = record["construction_rules_carried_forward"]
    check(
        checks,
        "whole_completion_exact",
        rules.get("whole_completion"),
        "exactly one Rz(180 degrees): (X,Y,Z)->(-X,-Y,Z)",
    )
    check(
        checks,
        "haft_formula_exact",
        rules.get("haft"),
        "theta(U)=-pi/2+pi*U with exact pi/2 flat-diameter-to-half-circumference factor",
    )
    check(
        checks,
        "combined_boundary_rule_present",
        "combined exterior boundary" in rules.get("head", ""),
    )
    check(
        checks,
        "negative_space_rule_present",
        rules.get("negative_spaces"),
        "source-connected negative spaces remain unoccupied",
    )
    check(
        checks,
        "rune_depth_preserved",
        record["disagreement_resolutions"][2]["candidate_results_cm"]["rune_side"],
        "34.434306569343",
    )
    check(
        checks,
        "metal_depth_preserved",
        record["disagreement_resolutions"][2]["candidate_results_cm"][
            "metal_center_piece_side"
        ],
        "43.120437956204",
    )
    check(
        checks,
        "axial_mean_not_final_candidate_depth",
        record["disagreement_resolutions"][1].get("final_geometry_role"),
        "comparison_and_orientation_only",
    )
    check(
        checks,
        "candidate_depths_own_final_geometry",
        record["disagreement_resolutions"][2].get("final_geometry_role"),
        "authoritative_candidate_depth",
    )
    check(
        checks,
        "decision_record_does_not_name_invalid_parent_step_artifact",
        not any(
            token in DECISIONS.read_text(encoding="utf-8")
            for token in (
                "STEP_10_INTERPRETATION_DECISIONS.json:invalid",
                "STEP_11_PRODUCTION_GEOMETRY_BLUEPRINT.json:invalid",
                "build_siegebreaker_r8_pixel_exact_steps10_11.py",
                "build_siegebreaker_r8_pixel_exact_steps12_16.py",
            )
        ),
    )
    check(
        checks,
        "numeric_substitution_schema",
        numeric.get("schema"),
        "AERATHEA_R8_STEP10_NUMERIC_SUBSTITUTION_V1",
    )
    check(
        checks,
        "only_fixed_external_anchor_is_length",
        numeric.get("fixed_external_numeric_anchor"),
        {"name": "overall_length_cm", "value": "170.000000000000"},
    )
    check(
        checks,
        "front_width_matches_step09",
        numeric["new_pixel_consequences"]["front_owned_width_cm"],
        step09_index["derived_dimensions_cm"]["width_front_owned"][
            "display_decimal"
        ],
    )
    check(
        checks,
        "rune_depth_matches_step09",
        numeric["new_pixel_consequences"]["rune_side_completed_depth_cm"],
        step09_index["right_candidate_halves"]["rune_side"][
            "completed_depth_cm"
        ]["display_decimal"],
    )
    check(
        checks,
        "metal_depth_matches_step09",
        numeric["new_pixel_consequences"][
            "metal_center_piece_completed_depth_cm"
        ],
        step09_index["right_candidate_halves"]["metal_center_piece_side"][
            "completed_depth_cm"
        ]["display_decimal"],
    )
    check(
        checks,
        "centered_axial_mean_matches_step09",
        numeric["new_pixel_consequences"]["centered_top_bottom_depth_cm"],
        {
            "value": step09_index["derived_dimensions_cm"][
                "depth_centered_top_bottom_owned"
            ]["display_decimal"],
            "final_geometry_role": "comparison_and_orientation_only",
        },
    )
    check(
        checks,
        "final_candidate_dimensions_exact",
        numeric.get("final_candidate_dimensions_cm"),
        {
            "rune_side": [
                "97.873941674506",
                "34.434306569343",
                "170.000000000000",
            ],
            "metal_center_piece_side": [
                "97.873941674506",
                "43.120437956204",
                "170.000000000000",
            ],
        },
    )
    check(
        checks,
        "final_depth_precedence_explicit",
        numeric.get("final_depth_precedence"),
        "candidate-specific right-view completed depth controls final geometry; centered top/bottom mean is comparison and orientation evidence only",
    )
    check(
        checks,
        "front_stations_match_step09",
        numeric["new_pixel_consequences"][
            "front_component_stations_world_z_cm"
        ],
        {
            name: value["display_decimal"]
            for name, value in step09_index[
                "front_component_stations_world_z_cm"
            ].items()
        },
    )
    check(
        checks,
        "older_conflicting_numeric_locks_explicit",
        {
            key: value
            for key, value in numeric[
                "older_numeric_locks_not_carried_into_r8"
            ].items()
            if key != "reason"
        },
        {
            "shaft_diameter_cm": "5",
            "grip_length_cm": "42",
            "pommel_length_cm": "18",
            "pommel_width_cm": "11",
        },
    )
    check(
        checks,
        "separate_component_scale_forbidden",
        numeric.get("separate_component_scale_permitted"),
        False,
    )
    check(
        checks,
        "source_resampling_forbidden",
        numeric.get("source_resampling_permitted"),
        False,
    )
    check(
        checks,
        "numeric_rule_creates_no_interpretation",
        numeric.get("new_interpretation_created"),
        False,
    )
    check(
        checks,
        "active_contract_declares_only_length_fixed",
        "Overall length `170 cm` is the approved external scale anchor."
        in execution_contract_text
        and "Every other overall or component dimension is an observed consequence"
        in execution_contract_text,
    )
    check(
        checks,
        "active_contract_forbids_component_scaling",
        "separate scale factors for head, coupler, shaft, ferrule, grip, collar,"
        in execution_contract_text,
    )

    passed = all(item["pass"] for item in checks)
    report = {
        "schema": "AERATHEA_R8_ZERO_EXTRUSION_STEP10_VALIDATION_V1",
        "asset": ASSET,
        "run_id": "SB-CR-STEPS10-16-R8-ZERO-EXTRUSION-A02",
        "step": "10",
        "independent_validator": str(Path(__file__).relative_to(ROOT)),
        "input_sha256": {
            "decision_record": sha256(DECISIONS),
            "numeric_substitution": sha256(NUMERIC_SUBSTITUTION),
            **{
                name: sha256(path)
                for name, (path, _expected) in AUTHORITY_FILES.items()
            },
        },
        "checks": checks,
        "pass_count": sum(1 for item in checks if item["pass"]),
        "check_count": len(checks),
        "result": "PASS" if passed else "FAIL",
        "artifact_status": "proof only",
        "next_step_unlocked": "11" if passed else None,
    }
    STEP10_VALIDATION.parent.mkdir(parents=True, exist_ok=True)
    STEP10_VALIDATION.write_text(
        json.dumps(report, indent=2, sort_keys=True) + "\n",
        encoding="utf-8",
    )
    return report


def audit_step11() -> dict[str, Any]:
    checks: list[dict[str, Any]] = []
    authority_checks(checks)
    step10 = load_json(STEP10_VALIDATION)
    blueprint = load_json(BLUEPRINT)

    check(checks, "step10_passed", step10.get("result"), "PASS")
    check(
        checks,
        "blueprint_schema",
        blueprint.get("schema"),
        "AERATHEA_R8_ZERO_EXTRUSION_STEP11_BLUEPRINT_V1",
    )
    check(checks, "blueprint_step", blueprint.get("step"), "11")
    check(checks, "geometry_created_false", blueprint.get("geometry_created"), False)
    check(
        checks,
        "source_half_count",
        blueprint["construction"]["whole_asset"]["measured_source_half_count"],
        1,
    )
    check(
        checks,
        "whole_completion_count",
        blueprint["construction"]["whole_asset"]["rz180_completion_count"],
        1,
    )
    check(
        checks,
        "whole_completion_formula",
        blueprint["construction"]["whole_asset"]["transform"],
        "Rz(180 degrees): (X,Y,Z)->(-X,-Y,Z)",
    )
    check(
        checks,
        "forbidden_operation_count_zero",
        len(blueprint["zero_extrusion_audit"]["forbidden_operations"]),
        0,
    )
    check(
        checks,
        "required_component_ids_exact",
        set(blueprint["construction"]["required_components"]),
        {
            "C01_CENTER_CORE",
            "C02_STONE_LEFT",
            "C03_STONE_RIGHT",
            "C04_STRIKE_FACE_POSITIVE_X",
            "C06_UPPER_HAFT_CAP",
            "C07A_HAFT_CYLINDER",
            "C07B_HAFT_TO_HANDLE_FERRULE",
            "C08_GRIP",
            "C09_LOWER_COLLAR",
            "C10_POMMEL_BODY",
            "C11_POMMEL_TERMINAL_CAP",
            "C12_UPPER_HEAD_CAP_SPIRE",
        },
    )
    check(
        checks,
        "candidate_depths_exact",
        blueprint["candidates"],
        [
            {
                "id": "rune_side",
                "right_interval_half_open": [557, 668],
                "completed_depth_cm": "34.434306569343",
            },
            {
                "id": "metal_center_piece_side",
                "right_interval_half_open": [418, 557],
                "completed_depth_cm": "43.120437956204",
            },
        ],
    )
    check(
        checks,
        "front_width_exact",
        blueprint["dimensions_cm"]["front_owned_width"],
        "97.873941674506",
    )
    check(
        checks,
        "length_exact",
        blueprint["dimensions_cm"]["length"],
        "170.000000000000",
    )
    check(
        checks,
        "haft_mapping_exact",
        blueprint["construction"]["haft"]["theta"],
        "theta(U)=-pi/2+pi*U",
    )
    check(
        checks,
        "rotational_equation_exact",
        blueprint["construction"]["rotational_components"]["equation"],
        "P(z,theta)=(r(z)cos(theta),r(z)sin(theta),z)",
    )
    check(
        checks,
        "combined_boundary_only",
        blueprint["construction"]["head"]["per_component_backing_walls"],
        0,
    )
    check(
        checks,
        "invalid_parent_geometry_reuse_false",
        blueprint["input_firewall"]["invalid_parent_steps_10_16_reused"],
        False,
    )
    check(
        checks,
        "old_mesh_import_false",
        blueprint["input_firewall"]["old_blend_or_mesh_imported"],
        False,
    )
    check(
        checks,
        "no_manual_dcc",
        blueprint["execution"]["manual_dcc_editing"],
        False,
    )
    check(
        checks,
        "run_a_run_b_distinct",
        blueprint["reproducibility"]["run_a_root"]
        != blueprint["reproducibility"]["run_b_root"],
    )
    check(
        checks,
        "lod0_cap",
        blueprint["performance"]["lod0_hard_cap_triangles"],
        10000,
    )
    check(
        checks,
        "unreal_authority_false",
        blueprint["authority_ceiling"]["unreal"],
        False,
    )

    blueprint_text = BLUEPRINT.read_text(encoding="utf-8").lower()
    forbidden_positive_claims = (
        '"method": "extrusion"',
        '"method": "solidify"',
        '"method": "cube"',
        '"method": "slab"',
        '"method": "generalized cross-section"',
        '"old_blend_or_mesh_imported": true',
    )
    check(
        checks,
        "no_forbidden_positive_method_claim",
        not any(token in blueprint_text for token in forbidden_positive_claims),
    )

    passed = all(item["pass"] for item in checks)
    report = {
        "schema": "AERATHEA_R8_ZERO_EXTRUSION_STEP11_VALIDATION_V1",
        "asset": ASSET,
        "run_id": "SB-CR-STEPS10-16-R8-ZERO-EXTRUSION-A02",
        "step": "11",
        "independent_validator": str(Path(__file__).relative_to(ROOT)),
        "input_sha256": {
            "blueprint": sha256(BLUEPRINT),
            "step10_validation": sha256(STEP10_VALIDATION),
            **{
                name: sha256(path)
                for name, (path, _expected) in AUTHORITY_FILES.items()
            },
        },
        "checks": checks,
        "pass_count": sum(1 for item in checks if item["pass"]),
        "check_count": len(checks),
        "result": "PASS" if passed else "FAIL",
        "artifact_status": "proof only",
        "next_step_unlocked": "12" if passed else None,
    }
    STEP11_VALIDATION.write_text(
        json.dumps(report, indent=2, sort_keys=True) + "\n",
        encoding="utf-8",
    )
    return report


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--step", choices=("10", "11"), required=True)
    args = parser.parse_args()
    report = audit_step10() if args.step == "10" else audit_step11()
    print(
        f"AERATHEA_STEP_{args.step}_INDEPENDENT_AUDIT_{report['result']} "
        f"{report['pass_count']}/{report['check_count']}"
    )
    if report["result"] != "PASS":
        raise SystemExit(1)


if __name__ == "__main__":
    main()
