#!/usr/bin/env python3
"""Independently audit the document-only Step 11 A02 blueprint.

This validator does not import the blueprint builder. It replays the approved
measurements and ownership records directly, checks every planned surface and
connection, and writes one proof-only JSON report. It does not import bpy,
open Blender, create geometry, render, export, or unlock Step 12.
"""

from __future__ import annotations

import ast
from fractions import Fraction
import gzip
import hashlib
import json
from pathlib import Path
from typing import Any


ROOT = Path(__file__).resolve().parents[2]
ASSET = "SM_DRW_SiegeBreaker_Hammer_A01"
ASSET_ROOT = ROOT / "docs/assets/blueprints" / ASSET
PARENT = ASSET_ROOT / "proof_runs/SB-CR-STEPS01-16-R8-PIXEL-EXACT-A01"
OWNERSHIP = (
    ASSET_ROOT
    / "proof_runs/SB-CR-R8-STEP09A-COMPONENT-PIXEL-OWNERSHIP-A01"
)
RUN = ASSET_ROOT / "proof_runs/SB-CR-STEPS10-16-R8-ZERO-EXTRUSION-A02"
BLUEPRINT = RUN / "manifests/STEP_11_PRODUCTION_GEOMETRY_BLUEPRINT.json"
VALIDATION = RUN / "manifests/STEP_11_BLUEPRINT_VALIDATION_A02.json"
BUILDER = ROOT / "Tools/DCC/build_siegebreaker_r8_step11_production_blueprint_a02.py"


FILES = {
    "agents": ROOT / "AGENTS.md",
    "project_charter": ASSET_ROOT / f"{ASSET}_PROJECT_CHARTER.md",
    "pipeline_plan": (
        ASSET_ROOT / f"{ASSET}_STEPS_01_16_PROOF_OF_CONCEPT_PIPELINE_PLAN.md"
    ),
    "r7_component_plan": (
        ASSET_ROOT / f"{ASSET}_A12_R7_COMPONENT_GEOMETRY_RECOVERY_PLAN.md"
    ),
    "r8_execution_contract": (
        ASSET_ROOT / "steps/A12_R10_R8_PIXEL_EXACT_STEPS01_16_A01_CONTRACT.md"
    ),
    "component_equations": (
        ASSET_ROOT / "steps/A12_R10_STEP02_COMPONENT_EQUATION_CONTRACT_DRAFT.md"
    ),
    "component_equations_approval": (
        ASSET_ROOT
        / "steps/A12_R10_STEP02_COMPONENT_EQUATION_CONTRACT_A01_APPROVAL_RECORD.md"
    ),
    "view_scale_contract": (
        ASSET_ROOT
        / "steps/A12_R10_STEP02A_R8_VIEW_OWNED_SCALE_RECONCILIATION_A01_CONTRACT.md"
    ),
    "source_half_contract": (
        ASSET_ROOT
        / "steps/A12_R10_STEP06_ONE_RZ180_SOURCE_HALF_ASSEMBLY_A01_CONTRACT.md"
    ),
    "closure_amendment": (
        ASSET_ROOT
        / "steps/A12_R10_STEP06A_DETERMINISTIC_CLOSURE_AMENDMENT_A01.md"
    ),
    "zero_extrusion_handoff": (
        ASSET_ROOT / "handoffs/A12_R10_R8_ZERO_EXTRUSION_RESET_HANDOFF.md"
    ),
    "proven_process_output": (
        ASSET_ROOT
        / "steps/A12_R10_A09_PROCESS_COMPLETE_RZ180_A02_OUTPUT_RECORD.md"
    ),
    "proven_process_builder": (
        ROOT
        / "Tools/DCC/build_siegebreaker_a12_r10_a09_process_complete_rz180.py"
    ),
    "proven_process_audit": (
        ROOT
        / "Tools/DCC/audit_siegebreaker_a12_r10_a09_process_complete_rz180.py"
    ),
    "step04_inventory": (
        PARENT / "manifests/STEP_04_COMPONENT_AND_SOURCE_OWNERSHIP_INVENTORY.json"
    ),
    "step05_registration": (
        PARENT / "manifests/STEP_05_PIXEL_WORLD_REGISTRATION_LOCK.json"
    ),
    "step06_front": (
        PARENT / "manifests/STEP_06_FRONT_MEASUREMENT_CONTRACT.json"
    ),
    "step06_back": (
        PARENT / "manifests/STEP_06_BACK_MEASUREMENT_CONTRACT.json"
    ),
    "step07_left": (
        PARENT / "manifests/STEP_07_LEFT_MEASUREMENT_CONTRACT.json"
    ),
    "step07_right": (
        PARENT / "manifests/STEP_07_RIGHT_MEASUREMENT_CONTRACT.json"
    ),
    "step08_top": (
        PARENT / "manifests/STEP_08_TOP_MEASUREMENT_CONTRACT.json"
    ),
    "step08_bottom": (
        PARENT / "manifests/STEP_08_BOTTOM_MEASUREMENT_CONTRACT.json"
    ),
    "step09_index": (
        PARENT / "manifests/STEP_09_INTEGRATED_EXACT_MEASUREMENT_INDEX.json"
    ),
    "step09_pre_geometry": (
        PARENT / "manifests/STEP_09_PRE_GEOMETRY_EXACT_DATA_AUDIT.json"
    ),
    "step10_decisions": RUN / "manifests/STEP_10_INTERPRETATION_DECISIONS.json",
    "step10_numeric": (
        RUN / "manifests/STEP_10_NUMERIC_SUBSTITUTION_CLARIFICATION.json"
    ),
    "step09a_authority_lock": (
        OWNERSHIP / "manifests/STEP_09A_AUTHORITY_LOCK.json"
    ),
    "step09a_scanlines": (
        OWNERSHIP / "evidence/STEP_09A_COMPONENT_SCANLINES.json.gz"
    ),
    "step09a_boundaries": (
        OWNERSHIP / "manifests/STEP_09A_BOUNDARY_AND_CORRESPONDENCE_INDEX.json"
    ),
    "step09a_validation": (
        OWNERSHIP / "manifests/STEP_09A_VALIDATION.json"
    ),
    "step11_preflight": (
        RUN / "manifests/STEP_11_SOURCE_AUTHORITY_PREFLIGHT_A02.json"
    ),
    "step11_preflight_validation": (
        RUN / "manifests/STEP_11_VALIDATION_A02.json"
    ),
    "proposed_contract": (
        RUN / "steps/STEP_11_PRODUCTION_BLUEPRINT_A02_PROPOSED_CONTRACT.md"
    ),
    "approval_record": (
        RUN / "steps/STEP_11_PRODUCTION_BLUEPRINT_A02_APPROVAL_RECORD.md"
    ),
}


EXPECTED_SHA256 = {
    "agents": "5d2d2637a58113f0a6f5ec92e40d8bb2bda9e03fb58b4868a0d9dfbb3b57ad55",
    "project_charter": "41c543aebf9bca5e5e8b970851843b6485fa17fc3473325d46a3960a9ba46f1b",
    "pipeline_plan": "53046eb839b94d9548dfc2e49471b3605a2fc882228ca5e4291db7390e584a2a",
    "r7_component_plan": "b0b077c8d39a07e5d1ab12309e77560afa1c407fe3bb3e6272a0c4e6d568b22e",
    "r8_execution_contract": "77b0339126388be01f59532cd6b79228450b61e739ebc10c2f849833fd337bd4",
    "component_equations": "a40d0b67d802687ac3c9ec9ad8e00a915cc1dc730ce31f3fab00b18a1837a21c",
    "component_equations_approval": "8296f530d48f43b99c6de26271e3be4da0a9fd512e389c90f55b9d5208185b29",
    "view_scale_contract": "84da92d2bec200a646bee4297965e9cd3bcd9aac090381b4108d931d7c1f4cd7",
    "source_half_contract": "eba4884b6b52178846854b59c88594fc3aa896067d868f6748d4aadd3bc4106a",
    "closure_amendment": "8ee99d2b5c510a540623aa4a69154b3bc0da9c7a9e846a42194a0dabe716d1b4",
    "zero_extrusion_handoff": "405d93b079c0fe52bdc443cadd085010fb64acf4cf9d078bf6e78d7e915e3ba0",
    "proven_process_output": "639db9d0c565aae7b974dab6fce9fb888f1b8412c77bbb2f6046413a7dbdff52",
    "proven_process_builder": "088ec22595437611e4f0e136db13b49d32ce3caaf8224c60f145f1c15153f235",
    "proven_process_audit": "6db37706e87021cf1ea978091c1e7b9f30c21163a5d5bd64bb6b32919ee352e0",
    "step04_inventory": "1bf54f9400dc2a4d0bb972ad56a3a913b586254f09b4867542e1c9899daf8a60",
    "step05_registration": "aed4b8d87a4a5b442c0465c9db59fa524f63797153d662e1a5e7cf90423a2446",
    "step06_front": "85f09fc89c8b73df8e6fdf47924e2251da9dda6decabe44fa3f3b2577b7708eb",
    "step06_back": "817af18192b3cf3b26ac47fb460e18b82266c30ce61f993b463a36175c014fcb",
    "step07_left": "7d099a11fb5566059bf0caaeaa353c479a531acff78fac6a9bedbeea739eb3f1",
    "step07_right": "977831e86b02148125a7e1a04024d2d114721590ebf63937bdd314d02cc427c9",
    "step08_top": "5925dee1ab39a0535150804a4353157b17d51fec648791774808c9c832dd8b36",
    "step08_bottom": "aea70d998dabe9f28d3ec5fb44a2d2206f8874096a3d33ee9b836074b2ede9a2",
    "step09_index": "5a0a3eea8f877d55216f9efabe15b0ee1cf938e4c15a825a0e218f72ba76839a",
    "step09_pre_geometry": "260c79857fe059517b4076bcc65b538aef807a7be33a58a4a46edc32c2150fdb",
    "step10_decisions": "0559b801ed3f544af82057d45f918599f07524588ff49c5ca92aefa744e467e9",
    "step10_numeric": "ff2f7cb37284dc7d1416044913375f67924ec4141c22a5385b3a29541e7446b9",
    "step09a_authority_lock": "a7e07ad68e9b2737c7c70e71e9df714766a285695693e741197900e17c3a06a5",
    "step09a_scanlines": "396adfbaaefc8a8ea35104e5e96dfde322510fb4ce88530fbb32f7f3073b3562",
    "step09a_boundaries": "e190ed266753c797d4f9ec812154ff3b29f5d5d780e53e235e780c43492d0bd8",
    "step09a_validation": "1e02aecf558145d4e440b1cdda90513fb28a0075149b1bf24f7ed3c00f7c3e60",
    "step11_preflight": "d243832e443779ae99e658e401a1985b94fa243a1a803849a50d1f31bd97eba0",
    "step11_preflight_validation": "e2bf62f65612945bdd9e295295b2b970098e88d75edd21d2e8c4896d5fbcf32b",
    "proposed_contract": "b563abfcda868f0345c65c729acee0d7d0dd9123e65544405d0139de06d64800",
    "approval_record": "6e2786e5d283f0176f90f83a80493c04581a6680aab32b3214c52403382e522f",
}


def sha256(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest()


def canonical_sha256(value: Any) -> str:
    payload = json.dumps(
        value, sort_keys=True, separators=(",", ":"), ensure_ascii=True
    ).encode("ascii")
    return hashlib.sha256(payload).hexdigest()


def load_json(path: Path) -> dict[str, Any]:
    value = json.loads(path.read_text(encoding="utf-8"))
    if not isinstance(value, dict):
        raise RuntimeError(f"Expected JSON object: {path}")
    return value


def load_gzip_json(path: Path) -> dict[str, Any]:
    value = json.loads(gzip.decompress(path.read_bytes()))
    if not isinstance(value, dict):
        raise RuntimeError(f"Expected gzip JSON object: {path}")
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


def fraction_record(value: Fraction) -> dict[str, Any]:
    return {
        "numerator": value.numerator,
        "denominator": value.denominator,
        "display_decimal": f"{float(value):.12f}",
    }


def sum_runs(rows: list[dict[str, Any]], key: str) -> int:
    return sum(
        int(end) - int(start)
        for row in rows
        for start, end in row.get(key, [])
    )


def exact_owner_record(
    owner_id: str,
    view: str,
    component: str,
    owner: dict[str, Any],
) -> dict[str, Any]:
    rows = owner["rows"]
    return {
        "id": owner_id,
        "source_file_key": "step09a_scanlines",
        "json_pointer": f"/views/{view}/component_owners/{component}",
        "view": view,
        "component": component,
        "row_count": len(rows),
        "owner_pixel_count": int(owner["owner_pixel_count"]),
        "selected_capture_pixel_count": int(
            owner["selected_capture_pixel_count"]
        ),
        "enclosed_source_pixel_count": int(
            owner["enclosed_source_pixel_count"]
        ),
        "rows_canonical_sha256": canonical_sha256(rows),
        "source_edge_domain": "integer half-open source pixel edges",
    }


def front_rows(
    front: dict[str, Any], start: int, stop: int
) -> list[dict[str, Any]]:
    rows = [
        row
        for row in front["row_profiles"]
        if start <= int(row["source_y"]) < stop
    ]
    if [int(row["source_y"]) for row in rows] != list(range(start, stop)):
        raise RuntimeError(f"Incomplete front interval {start}..{stop}")
    return rows


def front_interval_record(
    owner_id: str,
    component: str,
    start: int,
    stop: int,
    front: dict[str, Any],
) -> dict[str, Any]:
    rows = front_rows(front, start, stop)
    return {
        "id": owner_id,
        "source_file_key": "step06_front",
        "json_pointer": f"/row_profiles filtered by {start}<=source_y<{stop}",
        "view": "front",
        "component": component,
        "source_rows_half_open": [start, stop],
        "row_count": len(rows),
        "selected_pixel_count": sum_runs(rows, "runs_half_open"),
        "rows_canonical_sha256": canonical_sha256(rows),
        "ownership_rule": (
            "all exact selected front-source runs inside the approved "
            "component station interval"
        ),
        "source_edge_domain": "integer half-open source pixel edges",
    }


def c12_record(
    front: dict[str, Any], reserved_owner: dict[str, Any]
) -> dict[str, Any]:
    upper = front_rows(front, 208, 221)
    reserved = reserved_owner["rows"]
    if [int(row["y"]) for row in reserved] != list(range(221, 295)):
        raise RuntimeError("Incomplete C12 reserved rows")
    canonical_rows = [
        {
            "source_y": int(row["source_y"]),
            "owner_runs_half_open": row["runs_half_open"],
            "ownership_source": "step06_front exact selected runs",
        }
        for row in upper
    ] + [
        {
            "source_y": int(row["y"]),
            "owner_runs_half_open": row["owner_runs_half_open"],
            "ownership_source": "step09a_scanlines approved reserved C12 owner",
        }
        for row in reserved
    ]
    return {
        "id": "OWN_FRONT_C12_FULL",
        "source_file_keys": ["step06_front", "step09a_scanlines"],
        "json_pointers": [
            "/row_profiles filtered by 208<=source_y<221",
            "/views/front/component_owners/C12_RESERVED_EXISTING_OWNER/rows",
        ],
        "view": "front",
        "component": "C12_UPPER_HEAD_CAP_SPIRE",
        "source_rows_half_open": [208, 295],
        "row_count": 87,
        "owner_pixel_count": (
            sum_runs(upper, "runs_half_open")
            + sum_runs(reserved, "owner_runs_half_open")
        ),
        "rows_canonical_sha256": canonical_sha256(canonical_rows),
        "ownership_rule": (
            "rows 208..220 use only exact Step 06 selected runs; rows "
            "221..294 use only the approved Step 09A reserved C12 owner"
        ),
        "stone_pixels_borrowed": False,
        "source_edge_domain": "integer half-open source pixel edges",
    }


def front_z(edge_y: int) -> dict[str, Any]:
    return fraction_record(Fraction((1271 - edge_y) * 170, 1063))


def right_z(edge_y: int) -> dict[str, Any]:
    return fraction_record(Fraction((1262 - edge_y) * 85, 548))


def component_measurement(
    measurement_id: str,
    component: str,
    view: str,
    source_rows: tuple[int, int],
    top_z: dict[str, Any],
    bottom_z: dict[str, Any],
    owner_id: str,
) -> dict[str, Any]:
    top = Fraction(top_z["numerator"], top_z["denominator"])
    bottom = Fraction(bottom_z["numerator"], bottom_z["denominator"])
    return {
        "id": measurement_id,
        "component": component,
        "view": view,
        "source_rows_half_open": list(source_rows),
        "world_z_top_cm": top_z,
        "world_z_bottom_cm": bottom_z,
        "world_length_cm": fraction_record(top - bottom),
        "owner_id": owner_id,
    }


def semantic_record(record: dict[str, Any], component_key: str) -> dict[str, Any]:
    return {
        "id": record["id"],
        component_key: record[component_key],
        "candidate_variants": record["candidate_variants"],
        "method": record["method"],
        "source_ownership_refs": record["source_ownership_refs"],
        "equation_refs": record["equation_refs"],
        "measurement_refs": record["measurement_refs"],
    }


def main() -> int:
    checks: list[dict[str, Any]] = []
    for key, path in FILES.items():
        add(checks, f"authority_file_exists_{key}", path.is_file(), True)
        add(checks, f"authority_hash_{key}", sha256(path), EXPECTED_SHA256[key])
    add(checks, "blueprint_exists", BLUEPRINT.is_file(), True)
    add(checks, "builder_exists", BUILDER.is_file(), True)

    blueprint = load_json(BLUEPRINT)
    registration = load_json(FILES["step05_registration"])
    front = load_json(FILES["step06_front"])
    step09 = load_json(FILES["step09_index"])
    step10 = load_json(FILES["step10_decisions"])
    numeric = load_json(FILES["step10_numeric"])
    authority_lock = load_json(FILES["step09a_authority_lock"])
    scanlines = load_gzip_json(FILES["step09a_scanlines"])
    boundaries = load_json(FILES["step09a_boundaries"])
    preflight = load_json(FILES["step11_preflight"])
    preflight_validation = load_json(FILES["step11_preflight_validation"])

    add(
        checks,
        "blueprint_schema",
        blueprint.get("schema"),
        "AERATHEA_R8_ZERO_EXTRUSION_STEP11_PRODUCTION_BLUEPRINT_A02_V1",
    )
    add(checks, "blueprint_asset", blueprint.get("asset"), ASSET)
    add(
        checks,
        "blueprint_run",
        blueprint.get("run_id"),
        "SB-CR-STEPS10-16-R8-ZERO-EXTRUSION-A02",
    )
    add(
        checks,
        "blueprint_status",
        blueprint.get("artifact_status"),
        "candidate pending independent audit and Flamestrike decision",
    )
    add(
        checks,
        "blueprint_decision",
        blueprint.get("decision"),
        "candidate_pending_independent_audit",
    )
    add(checks, "step09a_authority_approved", authority_lock["decision"], "approved")
    add(checks, "step10_no_unknowns", step10["unresolved_geometry_affecting_items"], [])
    add(checks, "preflight_pass", preflight["decision"], "PASS")
    add(checks, "preflight_missing_authority", preflight["missing_authority"], [])
    add(checks, "preflight_validation_pass", preflight_validation["result"], "PASS")
    add(
        checks,
        "preflight_validation_count",
        [
            preflight_validation["pass_count"],
            preflight_validation["check_count"],
        ],
        [119, 119],
    )

    approval_text = FILES["approval_record"].read_text(encoding="utf-8")
    add(checks, "approval_exact_response", "> approved" in approval_text, True)
    add(
        checks,
        "approval_exact_question",
        (
            "write the exact 3D construction" in approval_text
            and "without opening Blender or creating geometry?" in approval_text
        ),
        True,
    )
    add(
        checks,
        "approval_hash_bound",
        blueprint["approval"]["approval_record_sha256"],
        EXPECTED_SHA256["approval_record"],
    )
    add(
        checks,
        "proposed_contract_hash_bound",
        blueprint["approval"]["proposed_contract_sha256"],
        EXPECTED_SHA256["proposed_contract"],
    )
    add(
        checks,
        "approval_scope_document_only",
        blueprint["approval"]["authorized_work"],
        "document and independent audit only",
    )

    expected_authority_files = {
        key: {
            "path": str(path.relative_to(ROOT)),
            "sha256": EXPECTED_SHA256[key],
            "hash_locked": True,
        }
        for key, path in FILES.items()
    }
    add(
        checks,
        "blueprint_authority_catalog_exact",
        blueprint["authority_files"],
        expected_authority_files,
    )
    add(
        checks,
        "algorithmic_reference_files",
        blueprint["algorithmic_reference_boundary"]["reference_files"],
        [
            "proven_process_output",
            "proven_process_builder",
            "proven_process_audit",
        ],
    )
    add(
        checks,
        "algorithmic_reference_requires_fresh_r8",
        blueprint["algorithmic_reference_boundary"][
            "fresh_r8_measurements_required"
        ],
        True,
    )
    add(
        checks,
        "algorithmic_reference_forbids_old_data",
        all(
            phrase in blueprint["algorithmic_reference_boundary"]["forbidden_use"]
            for phrase in ("old mesh", "old coordinates", "old dimensions")
        ),
        True,
    )

    builder_tree = ast.parse(BUILDER.read_text(encoding="utf-8"))
    imported_roots = {
        alias.name.split(".")[0]
        for node in ast.walk(builder_tree)
        if isinstance(node, ast.Import)
        for alias in node.names
    }
    imported_roots.update(
        node.module.split(".")[0]
        for node in ast.walk(builder_tree)
        if isinstance(node, ast.ImportFrom) and node.module
    )
    called_names = {
        node.func.id
        for node in ast.walk(builder_tree)
        if isinstance(node, ast.Call) and isinstance(node.func, ast.Name)
    }
    add(checks, "builder_does_not_import_bpy", "bpy" in imported_roots, False)
    add(checks, "builder_does_not_import_bmesh", "bmesh" in imported_roots, False)
    add(
        checks,
        "builder_does_not_import_subprocess",
        "subprocess" in imported_roots,
        False,
    )
    add(checks, "builder_does_not_call_exec", "exec" in called_names, False)
    add(checks, "builder_does_not_call_eval", "eval" in called_names, False)

    owner_names = {
        ("front", "C01_CENTER_CORE"): "OWN_FRONT_C01",
        ("front", "C02_STONE_LEFT"): "OWN_FRONT_C02",
        ("front", "C03_STONE_RIGHT"): "OWN_FRONT_C03",
        ("front", "C06_UPPER_HAFT_CAP"): "OWN_FRONT_C06",
        ("front", "C12_RESERVED_EXISTING_OWNER"): "OWN_FRONT_C12_RESERVED",
        ("right", "C01_SIDE_RESERVED_IN_METAL_HALF"): "OWN_RIGHT_C01_RESERVED",
        ("right", "C04_METAL_CENTER_PIECE_SIDE"): "OWN_RIGHT_C04_METAL",
        ("right", "C04_RUNE_SIDE"): "OWN_RIGHT_C04_RUNE",
        ("top", "C02_STONE_LEFT"): "OWN_TOP_C02",
        ("top", "C03_STONE_RIGHT"): "OWN_TOP_C03",
        ("top", "CENTRAL_NON_STONE_RESERVED"): "OWN_TOP_CENTRAL_RESERVED",
        ("bottom", "C02_STONE_LEFT"): "OWN_BOTTOM_C02",
        ("bottom", "C03_STONE_RIGHT"): "OWN_BOTTOM_C03",
        ("bottom", "CENTRAL_NON_STONE_RESERVED"): "OWN_BOTTOM_CENTRAL_RESERVED",
    }
    expected_evidence: dict[str, dict[str, Any]] = {}
    for (view, component), owner_id in owner_names.items():
        expected_evidence[owner_id] = exact_owner_record(
            owner_id,
            view,
            component,
            scanlines["views"][view]["component_owners"][component],
        )
    lower_intervals = {
        "OWN_FRONT_C07": ("C07_HAFT", 670, 870),
        "OWN_FRONT_C07B": ("C07B_HAFT_TO_HANDLE_FERRULE", 870, 955),
        "OWN_FRONT_C08": ("C08_GRIP", 955, 1110),
        "OWN_FRONT_C09": ("C09_LOWER_COLLAR", 1110, 1150),
        "OWN_FRONT_C10": ("C10_POMMEL_BODY", 1150, 1220),
        "OWN_FRONT_C11": ("C11_POMMEL_TERMINAL_CAP", 1220, 1271),
    }
    for owner_id, (component, start, stop) in lower_intervals.items():
        expected_evidence[owner_id] = front_interval_record(
            owner_id, component, start, stop, front
        )
    expected_evidence["OWN_FRONT_C12_FULL"] = c12_record(
        front,
        scanlines["views"]["front"]["component_owners"][
            "C12_RESERVED_EXISTING_OWNER"
        ],
    )
    for view in ("front", "right", "top", "bottom"):
        records = scanlines["views"][view]["protected_negative_spaces"]
        expected_evidence[f"PROTECTED_{view.upper()}"] = {
            "id": f"PROTECTED_{view.upper()}",
            "source_file_key": "step09a_scanlines",
            "json_pointer": f"/views/{view}/protected_negative_spaces",
            "view": view,
            "component": "PROTECTED_NEGATIVE_SPACE",
            "record_count": len(records),
            "protected_pixel_count": sum_runs(records, "runs_half_open"),
            "records_canonical_sha256": canonical_sha256(records),
            "ownership_rule": "exterior-connected and permanently unoccupied",
        }
    for boundary_id, record in boundaries["boundaries"].items():
        expected_evidence[boundary_id] = {
            "id": boundary_id,
            "source_file_key": "step09a_boundaries",
            "json_pointer": f"/boundaries/{boundary_id}",
            "view": record["view"],
            "component": record.get("owner", "SHARED_OR_ORDERED_BOUNDARY"),
            "order": record["order"],
            "sample_count": len(record.get("samples", [])),
            "record_canonical_sha256": canonical_sha256(record),
        }
    for record in boundaries["correspondence_groups"]:
        expected_evidence[record["id"]] = {
            "id": record["id"],
            "source_file_key": "step09a_boundaries",
            "json_pointer": "/correspondence_groups by exact id " + record["id"],
            "view": "cross_view",
            "component": record["component"],
            "ordered_boundary_ids": record["ordered_boundary_ids"],
            "scope": record["scope"],
            "record_canonical_sha256": canonical_sha256(record),
        }
    add(
        checks,
        "evidence_id_set_exact",
        sorted(blueprint["evidence_catalog"]),
        sorted(expected_evidence),
    )
    for evidence_id, expected in expected_evidence.items():
        add(
            checks,
            f"evidence_replay_{evidence_id}",
            blueprint["evidence_catalog"].get(evidence_id),
            expected,
        )
    add(
        checks,
        "c12_stone_pixels_not_borrowed",
        blueprint["evidence_catalog"]["OWN_FRONT_C12_FULL"][
            "stone_pixels_borrowed"
        ],
        False,
    )

    component_ranges = {
        "MEAS_C12": (
            "C12_UPPER_HEAD_CAP_SPIRE",
            "front",
            (208, 295),
            front_z(208),
            front_z(295),
            "OWN_FRONT_C12_FULL",
        ),
        "MEAS_C02": (
            "C02_STONE_LEFT",
            "front",
            (221, 600),
            front_z(221),
            front_z(600),
            "OWN_FRONT_C02",
        ),
        "MEAS_C03": (
            "C03_STONE_RIGHT",
            "front",
            (221, 600),
            front_z(221),
            front_z(600),
            "OWN_FRONT_C03",
        ),
        "MEAS_C01": (
            "C01_CENTER_CORE",
            "front",
            (295, 600),
            front_z(295),
            front_z(600),
            "OWN_FRONT_C01",
        ),
        "MEAS_C04": (
            "C04_STRIKE_FACE_POSITIVE_X",
            "right",
            (241, 651),
            right_z(241),
            right_z(651),
            "OWN_RIGHT_C04_RUNE/OWN_RIGHT_C04_METAL",
        ),
        "MEAS_C06": (
            "C06_UPPER_HAFT_CAP",
            "front",
            (600, 670),
            front_z(600),
            front_z(670),
            "OWN_FRONT_C06",
        ),
        "MEAS_C07": (
            "C07_HAFT",
            "front",
            (670, 870),
            front_z(670),
            front_z(870),
            "OWN_FRONT_C07",
        ),
        "MEAS_C07B": (
            "C07B_HAFT_TO_HANDLE_FERRULE",
            "front",
            (870, 955),
            front_z(870),
            front_z(955),
            "OWN_FRONT_C07B",
        ),
        "MEAS_C08": (
            "C08_GRIP",
            "front",
            (955, 1110),
            front_z(955),
            front_z(1110),
            "OWN_FRONT_C08",
        ),
        "MEAS_C09": (
            "C09_LOWER_COLLAR",
            "front",
            (1110, 1150),
            front_z(1110),
            front_z(1150),
            "OWN_FRONT_C09",
        ),
        "MEAS_C10": (
            "C10_POMMEL_BODY",
            "front",
            (1150, 1220),
            front_z(1150),
            front_z(1220),
            "OWN_FRONT_C10",
        ),
        "MEAS_C11": (
            "C11_POMMEL_TERMINAL_CAP",
            "front",
            (1220, 1271),
            front_z(1220),
            front_z(1271),
            "OWN_FRONT_C11",
        ),
    }
    expected_measurements = {
        key: component_measurement(key, *values)
        for key, values in component_ranges.items()
    }
    expected_measurements.update(
        {
            "MEAS_WORLD_FRAME": {
                "id": "MEAS_WORLD_FRAME",
                "source_file_key": "step05_registration",
                "json_pointer": "/world_frame",
                "value": registration["world_frame"],
            },
            "MEAS_FRONT_SCALE": {
                "id": "MEAS_FRONT_SCALE",
                "source_file_key": "step05_registration",
                "json_pointer": "/view_uniform_scales_cm_per_pixel/front",
                "value": registration["view_uniform_scales_cm_per_pixel"]["front"],
            },
            "MEAS_RIGHT_SCALE": {
                "id": "MEAS_RIGHT_SCALE",
                "source_file_key": "step05_registration",
                "json_pointer": "/view_uniform_scales_cm_per_pixel/right",
                "value": registration["view_uniform_scales_cm_per_pixel"]["right"],
            },
            "MEAS_AXIAL_SCALE": {
                "id": "MEAS_AXIAL_SCALE",
                "source_file_key": "step05_registration",
                "json_pointer": "/view_uniform_scales_cm_per_pixel/top",
                "value": registration["view_uniform_scales_cm_per_pixel"]["top"],
            },
            "MEAS_FRONT_WIDTH": {
                "id": "MEAS_FRONT_WIDTH",
                "source_file_key": "step09_index",
                "json_pointer": "/derived_dimensions_cm/width_front_owned",
                "value": step09["derived_dimensions_cm"]["width_front_owned"],
                "half_value_cm": fraction_record(Fraction(52020, 1063)),
            },
            "MEAS_RUNE_DEPTH": {
                "id": "MEAS_RUNE_DEPTH",
                "source_file_key": "step09_index",
                "json_pointer": "/right_candidate_halves/rune_side/completed_depth_cm",
                "value": step09["right_candidate_halves"]["rune_side"][
                    "completed_depth_cm"
                ],
                "half_value_cm": fraction_record(Fraction(9435, 548)),
            },
            "MEAS_METAL_DEPTH": {
                "id": "MEAS_METAL_DEPTH",
                "source_file_key": "step09_index",
                "json_pointer": (
                    "/right_candidate_halves/metal_center_piece_side/"
                    "completed_depth_cm"
                ),
                "value": step09["right_candidate_halves"][
                    "metal_center_piece_side"
                ]["completed_depth_cm"],
                "half_value_cm": fraction_record(Fraction(11815, 548)),
            },
            "MEAS_OVERALL_LENGTH": {
                "id": "MEAS_OVERALL_LENGTH",
                "source_file_key": "step09_index",
                "json_pointer": "/derived_dimensions_cm/length_anchor",
                "value": step09["derived_dimensions_cm"]["length_anchor"],
            },
        }
    )
    add(
        checks,
        "measurement_id_set_exact",
        sorted(blueprint["measurement_catalog"]),
        sorted(expected_measurements),
    )
    for measurement_id, expected in expected_measurements.items():
        add(
            checks,
            f"measurement_replay_{measurement_id}",
            blueprint["measurement_catalog"].get(measurement_id),
            expected,
        )

    component_to_owner = {
        value[0]: owner_id for owner_id, value in lower_intervals.items()
    }
    component_to_owner.update(
        {
            "C12_UPPER_HEAD_CAP_SPIRE": "OWN_FRONT_C12_FULL",
            "C01_CENTER_CORE": "OWN_FRONT_C01",
            "C06_UPPER_HAFT_CAP": "OWN_FRONT_C06",
        }
    )

    def source_row(source_y: int) -> dict[str, Any]:
        rows = [
            row
            for row in front["row_profiles"]
            if int(row["source_y"]) == source_y
        ]
        if len(rows) != 1:
            raise RuntimeError(f"Expected one front row {source_y}")
        return rows[0]

    def owner_runs(owner_id: str, source_y: int) -> list[list[int]]:
        if owner_id == "OWN_FRONT_C12_FULL":
            if source_y < 221:
                return source_row(source_y)["runs_half_open"]
            component = "C12_RESERVED_EXISTING_OWNER"
        elif owner_id == "OWN_FRONT_C01":
            component = "C01_CENTER_CORE"
        elif owner_id == "OWN_FRONT_C06":
            component = "C06_UPPER_HAFT_CAP"
        else:
            return source_row(source_y)["runs_half_open"]
        rows = [
            row
            for row in scanlines["views"]["front"]["component_owners"][
                component
            ]["rows"]
            if int(row["y"]) == source_y
        ]
        if len(rows) != 1:
            raise RuntimeError(f"Expected one {owner_id} row {source_y}")
        return rows[0]["owner_runs_half_open"]

    transition_rows = {
        "TR_C12_C01": ("C12_UPPER_HEAD_CAP_SPIRE", "C01_CENTER_CORE", 294, 295),
        "TR_C01_C06": ("C01_CENTER_CORE", "C06_UPPER_HAFT_CAP", 599, 600),
        "TR_C06_C07": ("C06_UPPER_HAFT_CAP", "C07_HAFT", 669, 670),
        "TR_C07_C07B": (
            "C07_HAFT",
            "C07B_HAFT_TO_HANDLE_FERRULE",
            869,
            870,
        ),
        "TR_C07B_C08": (
            "C07B_HAFT_TO_HANDLE_FERRULE",
            "C08_GRIP",
            954,
            955,
        ),
        "TR_C08_C09": ("C08_GRIP", "C09_LOWER_COLLAR", 1109, 1110),
        "TR_C09_C10": (
            "C09_LOWER_COLLAR",
            "C10_POMMEL_BODY",
            1149,
            1150,
        ),
        "TR_C10_C11": (
            "C10_POMMEL_BODY",
            "C11_POMMEL_TERMINAL_CAP",
            1219,
            1220,
        ),
    }
    expected_transitions: dict[str, dict[str, Any]] = {}
    for transition_id, (upper, lower, upper_y, lower_y) in transition_rows.items():
        upper_owner = component_to_owner[upper]
        lower_owner = component_to_owner[lower]

        def radius_record(y: int, owner_id: str) -> dict[str, Any]:
            edge = max(int(run[1]) for run in owner_runs(owner_id, y))
            return {
                "source_y": y,
                "positive_envelope_edge_x": edge,
                "axis_source_edge_x": 562,
                "radius_cm": fraction_record(
                    Fraction(abs(edge - 562) * 170, 1063)
                ),
                "source_ownership_ref": owner_id,
            }

        upper_radius = radius_record(upper_y, upper_owner)
        lower_radius = radius_record(lower_y, lower_owner)
        same = upper_radius["radius_cm"] == lower_radius["radius_cm"]
        expected_transitions[transition_id] = {
            "id": transition_id,
            "upper_component": upper,
            "lower_component": lower,
            "upper_source_ownership_ref": upper_owner,
            "lower_source_ownership_ref": lower_owner,
            "source_rows": [upper_y, lower_y],
            "shared_source_edge_y": lower_y,
            "shared_world_z_cm": front_z(lower_y),
            "upper_positive_radius": upper_radius,
            "lower_positive_radius": lower_radius,
            "closure": (
                "one coordinate-equal common half-ring"
                if same
                else "one exact planar positive-X half-annular shoulder"
            ),
            "same_radius": same,
        }
    add(
        checks,
        "transition_catalog_direct_replay",
        blueprint["transition_catalog"],
        expected_transitions,
    )
    add(
        checks,
        "c12_c01_uses_central_owner_edge",
        [
            blueprint["transition_catalog"]["TR_C12_C01"][
                "upper_positive_radius"
            ]["positive_envelope_edge_x"],
            blueprint["transition_catalog"]["TR_C12_C01"][
                "lower_positive_radius"
            ]["positive_envelope_edge_x"],
        ],
        [636, 636],
    )
    add(
        checks,
        "c01_c06_does_not_use_stone_edge",
        [
            blueprint["transition_catalog"]["TR_C01_C06"][
                "upper_positive_radius"
            ]["positive_envelope_edge_x"],
            blueprint["transition_catalog"]["TR_C01_C06"][
                "lower_positive_radius"
            ]["positive_envelope_edge_x"],
        ],
        [619, 620],
    )

    expected_equation_formulas = {
        "EQ_FRONT_XZ": "X=(x-562)*170/1063; Z=(1271-y)*170/1063",
        "EQ_RIGHT_YZ": "Y=(x-557)*85/548; Z=(1262-y)*85/548",
        "EQ_TOP_XY": (
            "X=(x-1533/2)*52020/517681; "
            "Y=(y-1093/2)*52020/517681"
        ),
        "EQ_BOTTOM_XY": (
            "X=(1529/2-x)*52020/517681; "
            "Y=(539-y)*52020/517681"
        ),
        "EQ_FRONT_OWNER_PLANE": (
            "P_front(x,y,candidate)=((x-562)*170/1063,-D_candidate/2,"
            "(1271-y)*170/1063)"
        ),
        "EQ_TOP_OWNER_PLANE": (
            "P_top(x,y,Z_component_top)=((x-1533/2)*52020/517681,"
            "(y-1093/2)*52020/517681,Z_component_top)"
        ),
        "EQ_BOTTOM_OWNER_PLANE": (
            "P_bottom(x,y,Z_component_bottom)=((1529/2-x)*52020/517681,"
            "(539-y)*52020/517681,Z_component_bottom)"
        ),
        "EQ_CANDIDATE_AXIAL_INTERSECTION": (
            "S_compatible=S_exact_owner_cell intersect "
            "{(X,Y): -D_candidate/2<=Y<=0}; retain only nonzero-area "
            "intersections and do not move an original cell edge"
        ),
        "EQ_C04_RUNE_SOURCE_HALF": (
            "P=(+52020/1063,-(x-557)*85/548,(1262-y)*85/548), "
            "x in [557,668)"
        ),
        "EQ_C04_METAL_SOURCE_HALF": (
            "P=(+52020/1063,(x-557)*85/548,(1262-y)*85/548), "
            "x in [418,557)"
        ),
        "EQ_FACE_LOCAL_MIRROR": "(X,Y,Z)->(X,-Y,Z) exactly once about Y=0",
        "EQ_EXACT_OWNER_BOUNDARY": (
            "boundary edges are integer half-open cell edges incident to "
            "exactly one owner cell and one non-owner cell"
        ),
        "EQ_ORDERED_RULED_FACE": "R(s,t)=(1-t)*A(s)+t*B(s), 0<=t<=1",
        "EQ_RADIUS_FROM_FRONT": (
            "r(y,owner)=abs(x_positive_exact_owner_edge(y)-562)*170/1063"
        ),
        "EQ_ROTATIONAL_SURFACE": (
            "P(z,theta)=(r(z)*cos(theta),r(z)*sin(theta),z), "
            "-pi/2<=theta<=pi/2 for the source half"
        ),
        "EQ_COLUMN_WRAP": (
            "U=(x_edge-x_left(y))/(x_right(y)-x_left(y)); "
            "theta(U)=-pi/2+pi*U"
        ),
        "EQ_HALF_ANNULAR_SHOULDER": (
            "P(t,theta)=((1-t)*r_upper+t*r_lower)*"
            "(cos(theta),sin(theta),0)+(0,0,Z_station), "
            "0<=t<=1, -pi/2<=theta<=pi/2"
        ),
        "EQ_PLANAR_HALF_CAP": (
            "P(t,theta)=(t*r_terminal*cos(theta),"
            "t*r_terminal*sin(theta),Z_terminal), "
            "0<=t<=1, -pi/2<=theta<=pi/2"
        ),
        "EQ_RZ180_COMPLETION": "(X,Y,Z)->(-X,-Y,Z) exactly once",
        "EQ_EQUAL_COORDINATE_WELD": (
            "merge only vertices with exactly equal canonical rational "
            "coordinates; no tolerance search or nearest-point weld"
        ),
    }
    add(
        checks,
        "equation_id_set_exact",
        sorted(blueprint["equation_catalog"]),
        sorted(expected_equation_formulas),
    )
    for equation_id, formula in expected_equation_formulas.items():
        add(
            checks,
            f"equation_formula_{equation_id}",
            blueprint["equation_catalog"][equation_id]["formula"],
            formula,
        )
    allowed_equation_authority = set(FILES)
    add(
        checks,
        "all_equation_authority_refs_resolve",
        all(
            bool(record.get("authority"))
            and set(record["authority"]).issubset(allowed_equation_authority)
            for record in blueprint["equation_catalog"].values()
        ),
        True,
    )
    add(
        checks,
        "radius_equation_owner_specific",
        "surface instruction's exact source_ownership_ref"
        in blueprint["equation_catalog"]["EQ_RADIUS_FROM_FRONT"][
            "owner_selection_rule"
        ],
        True,
    )
    add(
        checks,
        "ordered_ruled_face_is_exact_and_non_smoothing",
        all(
            phrase
            in blueprint["equation_catalog"]["EQ_ORDERED_RULED_FACE"][
                "pairing_rule"
            ]
            for phrase in (
                "exact cumulative source-edge length",
                "exact rational breakpoints",
                "Never smooth",
            )
        ),
        True,
    )
    add(
        checks,
        "axial_outside_evidence_non_geometric",
        "creates no geometry"
        in blueprint["equation_catalog"]["EQ_CANDIDATE_AXIAL_INTERSECTION"][
            "outside_classification"
        ],
        True,
    )

    both = ["rune_side", "metal_center_piece_side"]
    expected_surfaces = [
        {
            "id": "SURF_C01_FRONT",
            "component": "C01_CENTER_CORE",
            "candidate_variants": both,
            "method": "exact_visible_owner_domain",
            "source_ownership_refs": ["OWN_FRONT_C01"],
            "equation_refs": ["EQ_FRONT_XZ", "EQ_FRONT_OWNER_PLANE"],
            "measurement_refs": [
                "MEAS_C01",
                "MEAS_FRONT_SCALE",
                "MEAS_RUNE_DEPTH",
                "MEAS_METAL_DEPTH",
            ],
        },
        {
            "id": "SURF_C02_FRONT",
            "component": "C02_STONE_LEFT",
            "candidate_variants": both,
            "method": "exact_visible_owner_domain",
            "source_ownership_refs": ["OWN_FRONT_C02"],
            "equation_refs": ["EQ_FRONT_XZ", "EQ_FRONT_OWNER_PLANE"],
            "measurement_refs": [
                "MEAS_C02",
                "MEAS_FRONT_SCALE",
                "MEAS_RUNE_DEPTH",
                "MEAS_METAL_DEPTH",
            ],
        },
        {
            "id": "SURF_C02_TOP_HALF",
            "component": "C02_STONE_LEFT",
            "candidate_variants": both,
            "method": "exact_visible_owner_domain",
            "source_ownership_refs": ["OWN_TOP_C02"],
            "equation_refs": [
                "EQ_TOP_XY",
                "EQ_TOP_OWNER_PLANE",
                "EQ_CANDIDATE_AXIAL_INTERSECTION",
            ],
            "measurement_refs": [
                "MEAS_C02",
                "MEAS_AXIAL_SCALE",
                "MEAS_RUNE_DEPTH",
                "MEAS_METAL_DEPTH",
            ],
        },
        {
            "id": "SURF_C02_BOTTOM_HALF",
            "component": "C02_STONE_LEFT",
            "candidate_variants": both,
            "method": "exact_visible_owner_domain",
            "source_ownership_refs": ["OWN_BOTTOM_C02"],
            "equation_refs": [
                "EQ_BOTTOM_XY",
                "EQ_BOTTOM_OWNER_PLANE",
                "EQ_CANDIDATE_AXIAL_INTERSECTION",
            ],
            "measurement_refs": [
                "MEAS_C02",
                "MEAS_AXIAL_SCALE",
                "MEAS_RUNE_DEPTH",
                "MEAS_METAL_DEPTH",
            ],
        },
        {
            "id": "SURF_C03_FRONT",
            "component": "C03_STONE_RIGHT",
            "candidate_variants": both,
            "method": "exact_visible_owner_domain",
            "source_ownership_refs": ["OWN_FRONT_C03"],
            "equation_refs": ["EQ_FRONT_XZ", "EQ_FRONT_OWNER_PLANE"],
            "measurement_refs": [
                "MEAS_C03",
                "MEAS_FRONT_SCALE",
                "MEAS_RUNE_DEPTH",
                "MEAS_METAL_DEPTH",
            ],
        },
        {
            "id": "SURF_C03_TOP_HALF",
            "component": "C03_STONE_RIGHT",
            "candidate_variants": both,
            "method": "exact_visible_owner_domain",
            "source_ownership_refs": ["OWN_TOP_C03"],
            "equation_refs": [
                "EQ_TOP_XY",
                "EQ_TOP_OWNER_PLANE",
                "EQ_CANDIDATE_AXIAL_INTERSECTION",
            ],
            "measurement_refs": [
                "MEAS_C03",
                "MEAS_AXIAL_SCALE",
                "MEAS_RUNE_DEPTH",
                "MEAS_METAL_DEPTH",
            ],
        },
        {
            "id": "SURF_C03_BOTTOM_HALF",
            "component": "C03_STONE_RIGHT",
            "candidate_variants": both,
            "method": "exact_visible_owner_domain",
            "source_ownership_refs": ["OWN_BOTTOM_C03"],
            "equation_refs": [
                "EQ_BOTTOM_XY",
                "EQ_BOTTOM_OWNER_PLANE",
                "EQ_CANDIDATE_AXIAL_INTERSECTION",
            ],
            "measurement_refs": [
                "MEAS_C03",
                "MEAS_AXIAL_SCALE",
                "MEAS_RUNE_DEPTH",
                "MEAS_METAL_DEPTH",
            ],
        },
        {
            "id": "SURF_C04_RUNE_FACE_HALF",
            "component": "C04_STRIKE_FACE_POSITIVE_X",
            "candidate_variants": ["rune_side"],
            "method": "exact_face_half_then_local_mirror",
            "source_ownership_refs": [
                "OWN_RIGHT_C04_RUNE",
                "RIGHT_C04_CANDIDATE_HALF_BOUNDARIES",
            ],
            "equation_refs": [
                "EQ_RIGHT_YZ",
                "EQ_C04_RUNE_SOURCE_HALF",
                "EQ_FACE_LOCAL_MIRROR",
            ],
            "measurement_refs": [
                "MEAS_C04",
                "MEAS_FRONT_WIDTH",
                "MEAS_RUNE_DEPTH",
            ],
        },
        {
            "id": "SURF_C04_METAL_FACE_HALF",
            "component": "C04_STRIKE_FACE_POSITIVE_X",
            "candidate_variants": ["metal_center_piece_side"],
            "method": "exact_face_half_then_local_mirror",
            "source_ownership_refs": [
                "OWN_RIGHT_C04_METAL",
                "RIGHT_C04_CANDIDATE_HALF_BOUNDARIES",
            ],
            "equation_refs": [
                "EQ_RIGHT_YZ",
                "EQ_C04_METAL_SOURCE_HALF",
                "EQ_FACE_LOCAL_MIRROR",
            ],
            "measurement_refs": [
                "MEAS_C04",
                "MEAS_FRONT_WIDTH",
                "MEAS_METAL_DEPTH",
            ],
        },
    ]
    rotational = [
        ("C06", "C06_UPPER_HAFT_CAP"),
        ("C07", "C07_HAFT"),
        ("C07B", "C07B_HAFT_TO_HANDLE_FERRULE"),
        ("C08", "C08_GRIP"),
        ("C09", "C09_LOWER_COLLAR"),
        ("C10", "C10_POMMEL_BODY"),
        ("C11", "C11_POMMEL_TERMINAL_CAP"),
        ("C12", "C12_UPPER_HEAD_CAP_SPIRE"),
    ]
    for short, component in rotational:
        expected_surfaces.append(
            {
                "id": f"SURF_{short}_ROTATIONAL_HALF",
                "component": component,
                "candidate_variants": both,
                "method": "source_radius_rotational_half",
                "source_ownership_refs": [f"OWN_FRONT_{short}_FULL"]
                if short == "C12"
                else [f"OWN_FRONT_{short}"],
                "equation_refs": [
                    "EQ_RADIUS_FROM_FRONT",
                    "EQ_ROTATIONAL_SURFACE",
                    "EQ_COLUMN_WRAP",
                ],
                "measurement_refs": [f"MEAS_{short}", "MEAS_FRONT_SCALE"],
            }
        )
    observed_surfaces = [
        semantic_record(record, "component")
        for record in blueprint["surface_instructions"]
    ]
    add(checks, "surface_semantics_exact", observed_surfaces, expected_surfaces)
    add(
        checks,
        "surface_ids_unique",
        len({record["id"] for record in observed_surfaces}),
        len(observed_surfaces),
    )

    evidence_ids = set(blueprint["evidence_catalog"])
    equation_ids = set(blueprint["equation_catalog"])
    measurement_ids = set(blueprint["measurement_catalog"])
    all_instructions = (
        blueprint["surface_instructions"]
        + blueprint["closure_and_contact_instructions"]
    )
    for record in all_instructions:
        add(
            checks,
            f"{record['id']}_has_source_ownership",
            bool(record["source_ownership_refs"]),
            True,
        )
        add(
            checks,
            f"{record['id']}_ownership_refs_resolve",
            set(record["source_ownership_refs"]).issubset(evidence_ids),
            True,
        )
        add(
            checks,
            f"{record['id']}_has_equation",
            bool(record["equation_refs"]),
            True,
        )
        add(
            checks,
            f"{record['id']}_equation_refs_resolve",
            set(record["equation_refs"]).issubset(equation_ids),
            True,
        )
        add(
            checks,
            f"{record['id']}_has_measurement",
            bool(record["measurement_refs"]),
            True,
        )
        add(
            checks,
            f"{record['id']}_measurement_refs_resolve",
            set(record["measurement_refs"]).issubset(measurement_ids),
            True,
        )
        add(
            checks,
            f"{record['id']}_no_extrusion",
            record["extrusion_used"],
            False,
        )

    add(
        checks,
        "surface_flags_no_backing",
        all(
            not record["hidden_surface"]
            and not record["backing_surface_created"]
            for record in blueprint["surface_instructions"]
        ),
        True,
    )
    add(
        checks,
        "central_reserved_not_surface",
        not any(
            "CENTRAL_RESERVED" in record["id"]
            for record in blueprint["surface_instructions"]
        ),
        True,
    )
    add(
        checks,
        "all_axial_stone_surfaces_candidate_clipped",
        all(
            "EQ_CANDIDATE_AXIAL_INTERSECTION" in record["equation_refs"]
            and "MEAS_RUNE_DEPTH" in record["measurement_refs"]
            and "MEAS_METAL_DEPTH" in record["measurement_refs"]
            for record in blueprint["surface_instructions"]
            if record["id"]
            in {
                "SURF_C02_TOP_HALF",
                "SURF_C02_BOTTOM_HALF",
                "SURF_C03_TOP_HALF",
                "SURF_C03_BOTTOM_HALF",
            }
        ),
        True,
    )

    expected_closure_ids = [
        "CLOSURE_C02_INNER",
        "CLOSURE_C03_INNER",
        "CLOSURE_C03_TO_C04_RUNE",
        "CLOSURE_C03_TO_C04_METAL",
        "CONTACT_C12_C01",
        "CONTACT_C01_C06",
        "CONTACT_C06_C07",
        "CONTACT_C07_C07B",
        "CONTACT_C07B_C08",
        "CONTACT_C08_C09",
        "CONTACT_C09_C10",
        "CONTACT_C10_C11",
        "CAP_C11_BOTTOM",
        "CAP_C12_TOP",
        "GUARD_PROTECTED_NEGATIVE_SPACES",
        "WHOLE_ASSET_RZ180",
    ]
    observed_closures = blueprint["closure_and_contact_instructions"]
    add(
        checks,
        "closure_id_order_exact",
        [record["id"] for record in observed_closures],
        expected_closure_ids,
    )
    add(
        checks,
        "closure_ids_unique",
        len({record["id"] for record in observed_closures}),
        len(observed_closures),
    )
    expected_transition_methods = {
        "CONTACT_C07_C07B": "exact_planar_half_annular_shoulder",
        "CONTACT_C07B_C08": "exact_planar_half_annular_shoulder",
        "CONTACT_C08_C09": "coordinate_equal_common_half_ring",
        "CONTACT_C09_C10": "exact_planar_half_annular_shoulder",
        "CONTACT_C10_C11": "exact_planar_half_annular_shoulder",
    }
    observed_by_id = {record["id"]: record for record in observed_closures}
    for closure_id, method in expected_transition_methods.items():
        add(
            checks,
            f"{closure_id}_method_replays_transition",
            observed_by_id[closure_id]["method"],
            method,
        )
    add(
        checks,
        "closure_flags_no_new_silhouette_gap_or_duplicate",
        all(
            not record["creates_new_exterior_silhouette"]
            and not record["fills_protected_negative_space"]
            and not record["duplicate_wall_created"]
            for record in observed_closures
        ),
        True,
    )
    add(
        checks,
        "protected_guard_has_all_views",
        observed_by_id["GUARD_PROTECTED_NEGATIVE_SPACES"][
            "source_ownership_refs"
        ],
        [
            "PROTECTED_FRONT",
            "PROTECTED_RIGHT",
            "PROTECTED_TOP",
            "PROTECTED_BOTTOM",
        ],
    )
    add(
        checks,
        "whole_completion_exact",
        [
            observed_by_id["WHOLE_ASSET_RZ180"]["method"],
            observed_by_id["WHOLE_ASSET_RZ180"]["equation_refs"],
        ],
        [
            "exact_single_whole_completion",
            ["EQ_RZ180_COMPLETION", "EQ_EQUAL_COORDINATE_WELD"],
        ],
    )
    add(
        checks,
        "local_mirror_only_on_two_c04_variants",
        sorted(
            record["id"]
            for record in blueprint["surface_instructions"]
            if "EQ_FACE_LOCAL_MIRROR" in record["equation_refs"]
        ),
        ["SURF_C04_METAL_FACE_HALF", "SURF_C04_RUNE_FACE_HALF"],
    )
    add(
        checks,
        "whole_rz180_only_one_instruction",
        sum(
            "EQ_RZ180_COMPLETION" in record["equation_refs"]
            for record in all_instructions
        ),
        1,
    )

    expected_candidates = {
        "rune_side": {
            "source_owner": "OWN_RIGHT_C04_RUNE",
            "source_interval_half_open": [557, 668],
            "source_half_depth_cm": fraction_record(Fraction(9435, 548)),
            "completed_dimensions_cm": {
                "width": fraction_record(Fraction(104040, 1063)),
                "depth": fraction_record(Fraction(9435, 274)),
                "height": fraction_record(Fraction(170, 1)),
            },
            "front_envelope_y_cm": fraction_record(Fraction(-9435, 548)),
            "strike_face_equation": "EQ_C04_RUNE_SOURCE_HALF",
        },
        "metal_center_piece_side": {
            "source_owner": "OWN_RIGHT_C04_METAL",
            "source_interval_half_open": [418, 557],
            "source_half_depth_cm": fraction_record(Fraction(11815, 548)),
            "completed_dimensions_cm": {
                "width": fraction_record(Fraction(104040, 1063)),
                "depth": fraction_record(Fraction(11815, 274)),
                "height": fraction_record(Fraction(170, 1)),
            },
            "front_envelope_y_cm": fraction_record(Fraction(-11815, 548)),
            "strike_face_equation": "EQ_C04_METAL_SOURCE_HALF",
        },
    }
    add(
        checks,
        "candidate_dimensions_direct_replay",
        blueprint["candidate_variants"],
        expected_candidates,
    )
    add(
        checks,
        "candidate_depths_remain_distinct",
        blueprint["candidate_variants"]["rune_side"]["completed_dimensions_cm"][
            "depth"
        ]
        != blueprint["candidate_variants"]["metal_center_piece_side"][
            "completed_dimensions_cm"
        ]["depth"],
        True,
    )
    add(
        checks,
        "numeric_precedence_direct",
        blueprint["numeric_precedence"],
        {
            "only_fixed_external_anchor": numeric[
                "fixed_external_numeric_anchor"
            ],
            "new_pixel_consequences": numeric["new_pixel_consequences"],
            "older_fixed_component_values_not_carried": numeric[
                "older_numeric_locks_not_carried_into_r8"
            ],
            "final_depth_precedence": numeric["final_depth_precedence"],
        },
    )

    reserved = {record["id"]: record for record in blueprint["reserved_evidence"]}
    add(
        checks,
        "reserved_evidence_id_set",
        sorted(reserved),
        [
            "LOCKED_BACK_NONOWNING",
            "LOCKED_LEFT_NONOWNING",
            "RESERVED_BOTTOM_CENTRAL_NON_STONE",
            "RESERVED_RIGHT_C01_METAL_VARIANT",
            "RESERVED_TOP_CENTRAL_NON_STONE",
        ],
    )
    add(
        checks,
        "top_central_reserved_non_geometric",
        all(
            phrase in reserved["RESERVED_TOP_CENTRAL_NON_STONE"]["rule"]
            for phrase in ("did not decide", "no independent", "geometry")
        ),
        True,
    )
    add(
        checks,
        "bottom_central_reserved_non_geometric",
        all(
            phrase in reserved["RESERVED_BOTTOM_CENTRAL_NON_STONE"]["rule"]
            for phrase in ("not approved", "no independent", "geometry")
        ),
        True,
    )
    add(
        checks,
        "right_c01_reserved_excluded_from_c04",
        all(
            phrase in reserved["RESERVED_RIGHT_C01_METAL_VARIANT"]["rule"]
            for phrase in ("excluded from C04", "no", "geometry plane")
        ),
        True,
    )

    topology = blueprint["topology_and_performance_plan"]
    add(checks, "lod0_target", topology["lod0_target_triangles"], 8000)
    add(checks, "lod0_hard_cap", topology["lod0_hard_cap_triangles"], 10000)
    add(
        checks,
        "four_lods_required",
        topology["required_lods"],
        ["LOD0", "LOD1", "LOD2", "LOD3"],
    )
    add(
        checks,
        "over_cap_stops_for_amendment",
        "Stop before saving geometry" in topology["over_cap_action"],
        True,
    )
    material = blueprint["uv_material_texture_plan"]
    add(checks, "material_slot_count", material["material_slot_count"], 2)
    add(checks, "texture_resolution", material["texture_resolution"], "2048x2048")
    add(
        checks,
        "texture_set_exact",
        material["texture_set"],
        [
            "T_DRW_SiegeBreaker_A01_BC",
            "T_DRW_SiegeBreaker_A01_N",
            "T_DRW_SiegeBreaker_A01_ORM",
            "T_DRW_SiegeBreaker_A01_E",
        ],
    )
    collision = blueprint["collision_pivot_export_plan"]
    add(checks, "collision_proxy_count", collision["collision_proxy_count"], 3)
    add(
        checks,
        "pivot_exact",
        collision["pivot"],
        "bottom-center terminal/pommel at world (0,0,0)",
    )
    add(checks, "no_export_execution", collision["execution_now"], False)

    future = blueprint["future_execution_contract"]
    add(checks, "step12_not_authorized", future["step12_authorized_now"], False)
    add(checks, "step12_entry_absent", future["entry_point_exists_now"], False)
    add(
        checks,
        "future_environment_lock_complete",
        future["required_environment_lock_fields"],
        [
            "Blender binary path and SHA-256",
            "Blender version",
            "Python version",
            "OS and architecture",
            "locale and unit system",
            "color-management settings",
            "render backend and device class",
            "dependency versions and hashes",
            "fixed seeds",
            "network disabled",
        ],
    )
    add(
        checks,
        "future_state_begins_after_blueprint_approval",
        future["state_path"][0],
        "STEP_11_BLUEPRINT_APPROVED",
    )
    add(
        checks,
        "clean_replay_isolated",
        [
            blueprint["clean_replay_plan"]["no_cross_run_output_reads"],
            blueprint["clean_replay_plan"]["network_access"],
        ],
        [True, False],
    )
    add(
        checks,
        "mandatory_gates_include_zero_extrusion_and_exact_completion",
        all(
            any(phrase in gate for gate in blueprint["mandatory_step12_gates"])
            for phrase in (
                "no extrusion",
                "one C04 local mirror and one whole Rz180",
                "protected source pixel",
            )
        ),
        True,
    )
    add(
        checks,
        "forbidden_method_set_contains_required_blocks",
        {
            "Blender Extrude",
            "Solidify",
            "bmesh extrude operations",
            "cube or primitive replacement",
            "slab",
            "copied depth face",
            "generalized cross-section",
            "source resampling",
            "protected-gap fill",
            "old mesh import",
            "repair-forward",
        }.issubset(set(blueprint["forbidden_methods"])),
        True,
    )
    add(
        checks,
        "output_ceiling_exact",
        blueprint["output_ceiling"],
        {
            "production_blueprint_created": True,
            "blender_opened": False,
            "geometry_created": False,
            "render_created": False,
            "export_created": False,
            "unreal_created": False,
            "step12_unlocked": False,
        },
    )
    add(
        checks,
        "next_gate_requires_flamestrike",
        "Flamestrike" in blueprint["next_gate"],
        True,
    )

    failures = [check["id"] for check in checks if check["result"] != "PASS"]
    result = "PASS" if not failures else "FAIL"
    report = {
        "schema": "AERATHEA_R8_ZERO_EXTRUSION_STEP11_BLUEPRINT_VALIDATION_A02_V1",
        "asset": ASSET,
        "run_id": "SB-CR-STEPS10-16-R8-ZERO-EXTRUSION-A02",
        "step": "11 production blueprint independent document audit",
        "artifact_status": "proof only",
        "independent_validator": str(Path(__file__).relative_to(ROOT)),
        "independent_validator_sha256": sha256(Path(__file__)),
        "builder_imported": False,
        "input_sha256": {
            "blueprint": sha256(BLUEPRINT),
            "blueprint_builder": sha256(BUILDER),
            **{key: sha256(path) for key, path in FILES.items()},
        },
        "checks": checks,
        "pass_count": sum(check["result"] == "PASS" for check in checks),
        "check_count": len(checks),
        "failed_check_ids": failures,
        "result": result,
        "decision": (
            "blueprint_document_pass_pending_flamestrike_decision"
            if result == "PASS"
            else "Blueprint block: source authority missing"
        ),
        "blueprint_artifact_status": "candidate",
        "production_asset_created": False,
        "blender_opened": False,
        "geometry_created": False,
        "render_created": False,
        "export_created": False,
        "unreal_created": False,
        "step12_unlocked": False,
        "next_gate": (
            "visible plain-English review and Flamestrike approve/revise/"
            "reject/blocked decision on this exact Step 11 blueprint"
            if result == "PASS"
            else "stop and correct the failed blueprint evidence checks"
        ),
    }
    VALIDATION.write_text(
        json.dumps(report, indent=2, sort_keys=True) + "\n",
        encoding="utf-8",
    )
    print(
        f"AERATHEA_STEP11_BLUEPRINT_A02_{result} "
        f"{report['pass_count']}/{report['check_count']} "
        f"validation={VALIDATION.relative_to(ROOT)}"
    )
    return 0 if result == "PASS" else 1


if __name__ == "__main__":
    raise SystemExit(main())
