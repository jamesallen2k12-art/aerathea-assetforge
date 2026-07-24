#!/usr/bin/env python3
"""Build the document-only Step 11 A02 Siege Breaker geometry blueprint.

This script reads approved measurement and ownership records and writes one
JSON construction specification. It does not import bpy, open Blender, create
geometry, render, export, or unlock Step 12.
"""

from __future__ import annotations

import gzip
import hashlib
import json
from fractions import Fraction
from pathlib import Path
from typing import Any


ROOT = Path(__file__).resolve().parents[2]
ASSET = "SM_DRW_SiegeBreaker_Hammer_A01"
ASSET_ROOT = ROOT / "docs/assets/blueprints" / ASSET
PARENT_RUN = (
    ASSET_ROOT / "proof_runs/SB-CR-STEPS01-16-R8-PIXEL-EXACT-A01"
)
OWNERSHIP_RUN = (
    ASSET_ROOT / "proof_runs/SB-CR-R8-STEP09A-COMPONENT-PIXEL-OWNERSHIP-A01"
)
RUN = (
    ASSET_ROOT / "proof_runs/SB-CR-STEPS10-16-R8-ZERO-EXTRUSION-A02"
)
OUTPUT = RUN / "manifests/STEP_11_PRODUCTION_GEOMETRY_BLUEPRINT.json"


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
        PARENT_RUN / "manifests/STEP_04_COMPONENT_AND_SOURCE_OWNERSHIP_INVENTORY.json"
    ),
    "step05_registration": (
        PARENT_RUN / "manifests/STEP_05_PIXEL_WORLD_REGISTRATION_LOCK.json"
    ),
    "step06_front": (
        PARENT_RUN / "manifests/STEP_06_FRONT_MEASUREMENT_CONTRACT.json"
    ),
    "step06_back": (
        PARENT_RUN / "manifests/STEP_06_BACK_MEASUREMENT_CONTRACT.json"
    ),
    "step07_left": (
        PARENT_RUN / "manifests/STEP_07_LEFT_MEASUREMENT_CONTRACT.json"
    ),
    "step07_right": (
        PARENT_RUN / "manifests/STEP_07_RIGHT_MEASUREMENT_CONTRACT.json"
    ),
    "step08_top": (
        PARENT_RUN / "manifests/STEP_08_TOP_MEASUREMENT_CONTRACT.json"
    ),
    "step08_bottom": (
        PARENT_RUN / "manifests/STEP_08_BOTTOM_MEASUREMENT_CONTRACT.json"
    ),
    "step09_index": (
        PARENT_RUN / "manifests/STEP_09_INTEGRATED_EXACT_MEASUREMENT_INDEX.json"
    ),
    "step09_pre_geometry": (
        PARENT_RUN / "manifests/STEP_09_PRE_GEOMETRY_EXACT_DATA_AUDIT.json"
    ),
    "step10_decisions": RUN / "manifests/STEP_10_INTERPRETATION_DECISIONS.json",
    "step10_numeric": (
        RUN / "manifests/STEP_10_NUMERIC_SUBSTITUTION_CLARIFICATION.json"
    ),
    "step09a_authority_lock": (
        OWNERSHIP_RUN / "manifests/STEP_09A_AUTHORITY_LOCK.json"
    ),
    "step09a_scanlines": (
        OWNERSHIP_RUN / "evidence/STEP_09A_COMPONENT_SCANLINES.json.gz"
    ),
    "step09a_boundaries": (
        OWNERSHIP_RUN / "manifests/STEP_09A_BOUNDARY_AND_CORRESPONDENCE_INDEX.json"
    ),
    "step09a_validation": (
        OWNERSHIP_RUN / "manifests/STEP_09A_VALIDATION.json"
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


def load_json(path: Path) -> Any:
    return json.loads(path.read_text(encoding="utf-8"))


def load_gzip_json(path: Path) -> Any:
    return json.loads(gzip.decompress(path.read_bytes()))


def fraction_record(value: Fraction) -> dict[str, Any]:
    return {
        "numerator": value.numerator,
        "denominator": value.denominator,
        "display_decimal": f"{float(value):.12f}",
    }


def sum_runs(rows: list[dict[str, Any]], key: str) -> int:
    return sum(
        int(x1) - int(x0)
        for row in rows
        for x0, x1 in row.get(key, [])
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


def front_interval_record(
    owner_id: str,
    component: str,
    start: int,
    stop: int,
    front: dict[str, Any],
) -> dict[str, Any]:
    rows = [
        row
        for row in front["row_profiles"]
        if start <= int(row["source_y"]) < stop
    ]
    if [int(row["source_y"]) for row in rows] != list(range(start, stop)):
        raise RuntimeError(f"Incomplete exact front row interval: {component}")
    return {
        "id": owner_id,
        "source_file_key": "step06_front",
        "json_pointer": (
            f"/row_profiles filtered by {start}<=source_y<{stop}"
        ),
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


def c12_owner_record(
    front: dict[str, Any],
    reserved_owner: dict[str, Any],
) -> dict[str, Any]:
    upper_rows = [
        row
        for row in front["row_profiles"]
        if 208 <= int(row["source_y"]) < 221
    ]
    if [int(row["source_y"]) for row in upper_rows] != list(range(208, 221)):
        raise RuntimeError("Incomplete exact C12 upper selected-row interval")
    reserved_rows = reserved_owner["rows"]
    if [int(row["y"]) for row in reserved_rows] != list(range(221, 295)):
        raise RuntimeError("Incomplete exact C12 reserved-owner interval")
    canonical_rows = [
        {
            "source_y": int(row["source_y"]),
            "owner_runs_half_open": row["runs_half_open"],
            "ownership_source": "step06_front exact selected runs",
        }
        for row in upper_rows
    ] + [
        {
            "source_y": int(row["y"]),
            "owner_runs_half_open": row["owner_runs_half_open"],
            "ownership_source": "step09a_scanlines approved reserved C12 owner",
        }
        for row in reserved_rows
    ]
    return {
        "id": "OWN_FRONT_C12_FULL",
        "source_file_keys": ["step06_front", "step09a_scanlines"],
        "json_pointers": [
            "/row_profiles filtered by 208<=source_y<221",
            (
                "/views/front/component_owners/"
                "C12_RESERVED_EXISTING_OWNER/rows"
            ),
        ],
        "view": "front",
        "component": "C12_UPPER_HEAD_CAP_SPIRE",
        "source_rows_half_open": [208, 295],
        "row_count": len(canonical_rows),
        "owner_pixel_count": sum_runs(
            upper_rows, "runs_half_open"
        ) + sum_runs(reserved_rows, "owner_runs_half_open"),
        "rows_canonical_sha256": canonical_sha256(canonical_rows),
        "ownership_rule": (
            "rows 208..220 use only exact Step 06 selected runs; rows "
            "221..294 use only the approved Step 09A reserved C12 owner"
        ),
        "stone_pixels_borrowed": False,
        "source_edge_domain": "integer half-open source pixel edges",
    }


def source_row(front: dict[str, Any], y: int) -> dict[str, Any]:
    rows = [
        row for row in front["row_profiles"] if int(row["source_y"]) == y
    ]
    if len(rows) != 1:
        raise RuntimeError(f"Expected one front row {y}, found {len(rows)}")
    return rows[0]


def positive_radius_from_runs(
    y: int,
    runs: list[list[int]],
    ownership_ref: str,
) -> dict[str, Any]:
    if not runs:
        raise RuntimeError(f"No exact owner runs at front source row {y}")
    x_edge = max(int(run[1]) for run in runs)
    axis = 562
    value = Fraction(abs(x_edge - axis) * 170, 1063)
    return {
        "source_y": y,
        "positive_envelope_edge_x": x_edge,
        "axis_source_edge_x": axis,
        "radius_cm": fraction_record(value),
        "source_ownership_ref": ownership_ref,
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


def surface(
    surface_id: str,
    component: str,
    variants: list[str],
    method: str,
    ownership_refs: list[str],
    equation_refs: list[str],
    measurement_refs: list[str],
    instruction: str,
    visible_occurrence_rule: str,
) -> dict[str, Any]:
    return {
        "id": surface_id,
        "component": component,
        "candidate_variants": variants,
        "method": method,
        "source_ownership_refs": ownership_refs,
        "equation_refs": equation_refs,
        "measurement_refs": measurement_refs,
        "instruction": instruction,
        "visible_occurrence_rule": visible_occurrence_rule,
        "hidden_surface": False,
        "backing_surface_created": False,
        "extrusion_used": False,
    }


def closure(
    closure_id: str,
    components: list[str],
    variants: list[str],
    method: str,
    ownership_refs: list[str],
    equation_refs: list[str],
    measurement_refs: list[str],
    instruction: str,
) -> dict[str, Any]:
    return {
        "id": closure_id,
        "components": components,
        "candidate_variants": variants,
        "method": method,
        "source_ownership_refs": ownership_refs,
        "equation_refs": equation_refs,
        "measurement_refs": measurement_refs,
        "instruction": instruction,
        "creates_new_exterior_silhouette": False,
        "fills_protected_negative_space": False,
        "duplicate_wall_created": False,
        "extrusion_used": False,
    }


def main() -> None:
    for key, path in FILES.items():
        if not path.is_file():
            raise RuntimeError(f"Required authority file is missing: {key}")
    for key, expected in EXPECTED_SHA256.items():
        observed = sha256(FILES[key])
        if observed != expected:
            raise RuntimeError(
                f"Authority hash mismatch for {key}: {observed} != {expected}"
            )

    registration = load_json(FILES["step05_registration"])
    front = load_json(FILES["step06_front"])
    right = load_json(FILES["step07_right"])
    top = load_json(FILES["step08_top"])
    bottom = load_json(FILES["step08_bottom"])
    step09 = load_json(FILES["step09_index"])
    step10 = load_json(FILES["step10_decisions"])
    numeric = load_json(FILES["step10_numeric"])
    authority_lock = load_json(FILES["step09a_authority_lock"])
    scanlines = load_gzip_json(FILES["step09a_scanlines"])
    boundaries = load_json(FILES["step09a_boundaries"])
    preflight = load_json(FILES["step11_preflight"])
    preflight_validation = load_json(FILES["step11_preflight_validation"])

    if authority_lock["decision"] != "approved":
        raise RuntimeError("Step 09A ownership is not approved")
    if preflight["decision"] != "PASS" or preflight["missing_authority"]:
        raise RuntimeError("Step 11 source preflight is not an exact pass")
    if preflight_validation["result"] != "PASS":
        raise RuntimeError("Step 11 preflight independent validation failed")
    if step10["unresolved_geometry_affecting_items"]:
        raise RuntimeError("Step 10 still contains geometry-affecting unknowns")

    expected_owner_counts = {
        "front": {
            "C01_CENTER_CORE": 46183,
            "C02_STONE_LEFT": 71788,
            "C03_STONE_RIGHT": 71689,
            "C06_UPPER_HAFT_CAP": 6068,
            "C12_RESERVED_EXISTING_OWNER": 6463,
        },
        "right": {
            "C01_SIDE_RESERVED_IN_METAL_HALF": 9832,
            "C04_METAL_CENTER_PIECE_SIDE": 37508,
            "C04_RUNE_SIDE": 42029,
        },
        "top": {
            "C02_STONE_LEFT": 141087,
            "C03_STONE_RIGHT": 140054,
            "CENTRAL_NON_STONE_RESERVED": 103446,
        },
        "bottom": {
            "C02_STONE_LEFT": 132685,
            "C03_STONE_RIGHT": 133227,
            "CENTRAL_NON_STONE_RESERVED": 109361,
        },
    }
    if (
        preflight["available_exact_authority"]["component_owner_pixel_counts"]
        != expected_owner_counts
    ):
        raise RuntimeError("Preflight owner totals changed")

    evidence_catalog: dict[str, dict[str, Any]] = {}
    owner_ids = {
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
    for (view, component), owner_id in owner_ids.items():
        record = exact_owner_record(
            owner_id,
            view,
            component,
            scanlines["views"][view]["component_owners"][component],
        )
        if record["owner_pixel_count"] != expected_owner_counts[view][component]:
            raise RuntimeError(f"Owner total changed: {owner_id}")
        evidence_catalog[owner_id] = record

    lower_intervals = {
        "OWN_FRONT_C07": ("C07_HAFT", 670, 870),
        "OWN_FRONT_C07B": ("C07B_HAFT_TO_HANDLE_FERRULE", 870, 955),
        "OWN_FRONT_C08": ("C08_GRIP", 955, 1110),
        "OWN_FRONT_C09": ("C09_LOWER_COLLAR", 1110, 1150),
        "OWN_FRONT_C10": ("C10_POMMEL_BODY", 1150, 1220),
        "OWN_FRONT_C11": ("C11_POMMEL_TERMINAL_CAP", 1220, 1271),
    }
    for owner_id, (component, start, stop) in lower_intervals.items():
        evidence_catalog[owner_id] = front_interval_record(
            owner_id, component, start, stop, front
        )
    evidence_catalog["OWN_FRONT_C12_FULL"] = c12_owner_record(
        front,
        scanlines["views"]["front"]["component_owners"][
            "C12_RESERVED_EXISTING_OWNER"
        ],
    )
    component_to_owner_id = {
        value[0]: owner_id for owner_id, value in lower_intervals.items()
    }
    component_to_owner_id.update(
        {
            "C12_UPPER_HEAD_CAP_SPIRE": "OWN_FRONT_C12_FULL",
            "C01_CENTER_CORE": "OWN_FRONT_C01",
            "C06_UPPER_HAFT_CAP": "OWN_FRONT_C06",
        }
    )

    def owner_runs(owner_id: str, source_y: int) -> list[list[int]]:
        if owner_id == "OWN_FRONT_C12_FULL":
            if source_y < 221:
                return source_row(front, source_y)["runs_half_open"]
            owner = scanlines["views"]["front"]["component_owners"][
                "C12_RESERVED_EXISTING_OWNER"
            ]
            rows = [row for row in owner["rows"] if int(row["y"]) == source_y]
            if len(rows) != 1:
                raise RuntimeError(
                    f"Expected one reserved C12 row {source_y}"
                )
            return rows[0]["owner_runs_half_open"]
        step09a_components = {
            "OWN_FRONT_C01": "C01_CENTER_CORE",
            "OWN_FRONT_C06": "C06_UPPER_HAFT_CAP",
        }
        if owner_id in step09a_components:
            owner = scanlines["views"]["front"]["component_owners"][
                step09a_components[owner_id]
            ]
            rows = [row for row in owner["rows"] if int(row["y"]) == source_y]
            if len(rows) != 1:
                raise RuntimeError(
                    f"Expected one {owner_id} row {source_y}"
                )
            return rows[0]["owner_runs_half_open"]
        return source_row(front, source_y)["runs_half_open"]

    for view in ("front", "right", "top", "bottom"):
        records = scanlines["views"][view]["protected_negative_spaces"]
        evidence_catalog[f"PROTECTED_{view.upper()}"] = {
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
        evidence_catalog[boundary_id] = {
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
        evidence_catalog[record["id"]] = {
            "id": record["id"],
            "source_file_key": "step09a_boundaries",
            "json_pointer": (
                "/correspondence_groups by exact id " + record["id"]
            ),
            "view": "cross_view",
            "component": record["component"],
            "ordered_boundary_ids": record["ordered_boundary_ids"],
            "scope": record["scope"],
            "record_canonical_sha256": canonical_sha256(record),
        }

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
    measurement_catalog = {
        key: component_measurement(key, *values)
        for key, values in component_ranges.items()
    }
    measurement_catalog.update(
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
                "value": registration["view_uniform_scales_cm_per_pixel"][
                    "front"
                ],
            },
            "MEAS_RIGHT_SCALE": {
                "id": "MEAS_RIGHT_SCALE",
                "source_file_key": "step05_registration",
                "json_pointer": "/view_uniform_scales_cm_per_pixel/right",
                "value": registration["view_uniform_scales_cm_per_pixel"][
                    "right"
                ],
            },
            "MEAS_AXIAL_SCALE": {
                "id": "MEAS_AXIAL_SCALE",
                "source_file_key": "step05_registration",
                "json_pointer": "/view_uniform_scales_cm_per_pixel/top",
                "value": registration["view_uniform_scales_cm_per_pixel"][
                    "top"
                ],
            },
            "MEAS_FRONT_WIDTH": {
                "id": "MEAS_FRONT_WIDTH",
                "source_file_key": "step09_index",
                "json_pointer": "/derived_dimensions_cm/width_front_owned",
                "value": step09["derived_dimensions_cm"][
                    "width_front_owned"
                ],
                "half_value_cm": fraction_record(Fraction(52020, 1063)),
            },
            "MEAS_RUNE_DEPTH": {
                "id": "MEAS_RUNE_DEPTH",
                "source_file_key": "step09_index",
                "json_pointer": (
                    "/right_candidate_halves/rune_side/completed_depth_cm"
                ),
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
    transition_catalog = {}
    for transition_id, (upper, lower, upper_row, lower_row) in (
        transition_rows.items()
    ):
        upper_owner_id = component_to_owner_id[upper]
        lower_owner_id = component_to_owner_id[lower]
        upper_radius = positive_radius_from_runs(
            upper_row,
            owner_runs(upper_owner_id, upper_row),
            upper_owner_id,
        )
        lower_radius = positive_radius_from_runs(
            lower_row,
            owner_runs(lower_owner_id, lower_row),
            lower_owner_id,
        )
        same_radius = (
            upper_radius["radius_cm"]["numerator"]
            * lower_radius["radius_cm"]["denominator"]
            == lower_radius["radius_cm"]["numerator"]
            * upper_radius["radius_cm"]["denominator"]
        )
        transition_catalog[transition_id] = {
            "id": transition_id,
            "upper_component": upper,
            "lower_component": lower,
            "upper_source_ownership_ref": upper_owner_id,
            "lower_source_ownership_ref": lower_owner_id,
            "source_rows": [upper_row, lower_row],
            "shared_source_edge_y": lower_row,
            "shared_world_z_cm": front_z(lower_row),
            "upper_positive_radius": upper_radius,
            "lower_positive_radius": lower_radius,
            "closure": (
                "one coordinate-equal common half-ring"
                if same_radius
                else "one exact planar positive-X half-annular shoulder"
            ),
            "same_radius": same_radius,
        }

    equation_catalog = {
        "EQ_FRONT_XZ": {
            "id": "EQ_FRONT_XZ",
            "formula": "X=(x-562)*170/1063; Z=(1271-y)*170/1063",
            "authority": ["step05_registration", "step06_front"],
            "role": "exact front source-edge to world X/Z mapping",
        },
        "EQ_RIGHT_YZ": {
            "id": "EQ_RIGHT_YZ",
            "formula": "Y=(x-557)*85/548; Z=(1262-y)*85/548",
            "authority": ["step05_registration", "step07_right"],
            "role": "exact right source-edge to world Y/Z mapping",
        },
        "EQ_TOP_XY": {
            "id": "EQ_TOP_XY",
            "formula": (
                "X=(x-1533/2)*52020/517681; "
                "Y=(y-1093/2)*52020/517681"
            ),
            "authority": ["step05_registration", "step08_top"],
            "role": "exact top source-edge to world X/Y mapping",
        },
        "EQ_BOTTOM_XY": {
            "id": "EQ_BOTTOM_XY",
            "formula": (
                "X=(1529/2-x)*52020/517681; "
                "Y=(539-y)*52020/517681"
            ),
            "authority": ["step05_registration", "step08_bottom"],
            "role": "exact bottom source-edge to world X/Y mapping",
        },
        "EQ_FRONT_OWNER_PLANE": {
            "id": "EQ_FRONT_OWNER_PLANE",
            "formula": (
                "P_front(x,y,candidate)=("
                "(x-562)*170/1063,-D_candidate/2,"
                "(1271-y)*170/1063)"
            ),
            "authority": [
                "component_equations",
                "step10_decisions",
                "step10_numeric",
            ],
            "role": (
                "place an exact front-owned visible domain once on the "
                "candidate front envelope; no copied depth face"
            ),
        },
        "EQ_TOP_OWNER_PLANE": {
            "id": "EQ_TOP_OWNER_PLANE",
            "formula": (
                "P_top(x,y,Z_component_top)=("
                "(x-1533/2)*52020/517681,"
                "(y-1093/2)*52020/517681,Z_component_top)"
            ),
            "source_half_selector": (
                "retain only pixel cells whose exact sample has Y<=0; "
                "the one Rz180 completion supplies the complement"
            ),
            "authority": [
                "component_equations",
                "closure_amendment",
                "step10_decisions",
            ],
            "role": "exact top-owner cap domain for the measured source half",
        },
        "EQ_BOTTOM_OWNER_PLANE": {
            "id": "EQ_BOTTOM_OWNER_PLANE",
            "formula": (
                "P_bottom(x,y,Z_component_bottom)=("
                "(1529/2-x)*52020/517681,"
                "(539-y)*52020/517681,Z_component_bottom)"
            ),
            "source_half_selector": (
                "retain only pixel cells whose exact sample has Y<=0; "
                "the one Rz180 completion supplies the complement"
            ),
            "authority": [
                "component_equations",
                "closure_amendment",
                "step10_decisions",
            ],
            "role": (
                "exact bottom-owner underside domain for the measured source "
                "half"
            ),
        },
        "EQ_CANDIDATE_AXIAL_INTERSECTION": {
            "id": "EQ_CANDIDATE_AXIAL_INTERSECTION",
            "formula": (
                "S_compatible=S_exact_owner_cell intersect "
                "{(X,Y): -D_candidate/2<=Y<=0}; retain only nonzero-area "
                "intersections and do not move an original cell edge"
            ),
            "outside_classification": (
                "exact axial source evidence outside the selected candidate "
                "depth remains comparison/color evidence and creates no "
                "geometry"
            ),
            "authority": [
                "view_scale_contract",
                "step10_decisions",
                "step10_numeric",
            ],
            "role": (
                "enforce the approved candidate-specific final depth without "
                "stretching, normalizing, or moving an axial source pixel"
            ),
        },
        "EQ_C04_RUNE_SOURCE_HALF": {
            "id": "EQ_C04_RUNE_SOURCE_HALF",
            "formula": (
                "P=(+52020/1063,-(x-557)*85/548,"
                "(1262-y)*85/548), x in [557,668)"
            ),
            "authority": [
                "r8_execution_contract",
                "component_equations",
                "step10_decisions",
            ],
            "role": "map the rune-side right owner into the negative-Y face half",
        },
        "EQ_C04_METAL_SOURCE_HALF": {
            "id": "EQ_C04_METAL_SOURCE_HALF",
            "formula": (
                "P=(+52020/1063,(x-557)*85/548,"
                "(1262-y)*85/548), x in [418,557)"
            ),
            "authority": [
                "r8_execution_contract",
                "component_equations",
                "step10_decisions",
            ],
            "role": (
                "map the metal-center-piece right owner into the negative-Y "
                "face half"
            ),
        },
        "EQ_FACE_LOCAL_MIRROR": {
            "id": "EQ_FACE_LOCAL_MIRROR",
            "formula": "(X,Y,Z)->(X,-Y,Z) exactly once about Y=0",
            "authority": ["component_equations", "step10_decisions"],
            "role": (
                "complete one positive-X strike face from one measured face "
                "half; weld only coordinate-equal Y=0 vertices"
            ),
        },
        "EQ_EXACT_OWNER_BOUNDARY": {
            "id": "EQ_EXACT_OWNER_BOUNDARY",
            "formula": (
                "boundary edges are integer half-open cell edges incident to "
                "exactly one owner cell and one non-owner cell"
            ),
            "authority": ["closure_amendment", "step09a_boundaries"],
            "role": "derive no new contour beyond the exact owner membership",
        },
        "EQ_ORDERED_RULED_FACE": {
            "id": "EQ_ORDERED_RULED_FACE",
            "formula": "R(s,t)=(1-t)*A(s)+t*B(s), 0<=t<=1",
            "pairing_rule": (
                "Parameterize each approved ordered pixel-edge polyline by "
                "exact cumulative source-edge length. Use the sorted union of "
                "their exact rational breakpoints; evaluate only along the "
                "existing straight source edges at each shared parameter, "
                "then join corresponding values. Never smooth, search a "
                "nearby row, or move an owner boundary."
            ),
            "authority": ["component_equations", "closure_amendment"],
            "role": (
                "straight hidden connection inside the owning component "
                "domain; never a new exterior silhouette"
            ),
        },
        "EQ_RADIUS_FROM_FRONT": {
            "id": "EQ_RADIUS_FROM_FRONT",
            "formula": (
                "r(y,owner)=abs(x_positive_exact_owner_edge(y)-562)"
                "*170/1063"
            ),
            "owner_selection_rule": (
                "read the positive edge only from the surface instruction's "
                "exact source_ownership_ref; never from the whole-row outer "
                "interval when another component is present"
            ),
            "authority": [
                "component_equations",
                "step10_numeric",
                "step06_front",
            ],
            "role": (
                "new R8 front pixel consequence; old fixed 5/42/18/11 cm "
                "component values are not used"
            ),
        },
        "EQ_ROTATIONAL_SURFACE": {
            "id": "EQ_ROTATIONAL_SURFACE",
            "formula": (
                "P(z,theta)=(r(z)*cos(theta),r(z)*sin(theta),z), "
                "-pi/2<=theta<=pi/2 for the source half"
            ),
            "authority": ["component_equations", "step10_decisions"],
            "role": "exact source-derived positive-X half rotational surface",
        },
        "EQ_COLUMN_WRAP": {
            "id": "EQ_COLUMN_WRAP",
            "formula": (
                "U=(x_edge-x_left(y))/(x_right(y)-x_left(y)); "
                "theta(U)=-pi/2+pi*U"
            ),
            "factor": "flat-diameter-to-half-circumference=pi/2 exactly",
            "authority": ["r8_execution_contract", "component_equations"],
            "role": (
                "each retained exact source column owns its proportional U "
                "interval; no source column is skipped or repeated"
            ),
        },
        "EQ_HALF_ANNULAR_SHOULDER": {
            "id": "EQ_HALF_ANNULAR_SHOULDER",
            "formula": (
                "P(t,theta)=((1-t)*r_upper+t*r_lower)*"
                "(cos(theta),sin(theta),0)+(0,0,Z_station), "
                "0<=t<=1, -pi/2<=theta<=pi/2"
            ),
            "authority": ["closure_amendment", "step10_numeric"],
            "role": (
                "one planar station closure between exact adjacent R8 radii; "
                "omit when the radii are coordinate-equal"
            ),
        },
        "EQ_PLANAR_HALF_CAP": {
            "id": "EQ_PLANAR_HALF_CAP",
            "formula": (
                "P(t,theta)=(t*r_terminal*cos(theta),"
                "t*r_terminal*sin(theta),Z_terminal), "
                "0<=t<=1, -pi/2<=theta<=pi/2"
            ),
            "authority": ["closure_amendment", "step10_numeric"],
            "role": "close only the exact C11 bottom or C12 top terminal ring",
        },
        "EQ_RZ180_COMPLETION": {
            "id": "EQ_RZ180_COMPLETION",
            "formula": "(X,Y,Z)->(-X,-Y,Z) exactly once",
            "authority": [
                "r8_execution_contract",
                "zero_extrusion_handoff",
                "step10_decisions",
            ],
            "role": "whole-asset completion after the source set is validated",
        },
        "EQ_EQUAL_COORDINATE_WELD": {
            "id": "EQ_EQUAL_COORDINATE_WELD",
            "formula": (
                "merge only vertices with exactly equal canonical rational "
                "coordinates; no tolerance search or nearest-point weld"
            ),
            "authority": ["source_half_contract", "step10_decisions"],
            "role": "prevent position change during completion",
        },
    }

    both = ["rune_side", "metal_center_piece_side"]
    surface_instructions = [
        surface(
            "SURF_C01_FRONT",
            "C01_CENTER_CORE",
            both,
            "exact_visible_owner_domain",
            ["OWN_FRONT_C01"],
            ["EQ_FRONT_XZ", "EQ_FRONT_OWNER_PLANE"],
            ["MEAS_C01", "MEAS_FRONT_SCALE", "MEAS_RUNE_DEPTH", "MEAS_METAL_DEPTH"],
            (
                "Triangulate only the exact C01 front owner domain on the "
                "candidate front envelope. Interior pixels remain UV/color "
                "owners; only exact owner boundaries may create geometry."
            ),
            "one front occurrence; the back occurrence comes only from Rz180",
        ),
        surface(
            "SURF_C02_FRONT",
            "C02_STONE_LEFT",
            both,
            "exact_visible_owner_domain",
            ["OWN_FRONT_C02"],
            ["EQ_FRONT_XZ", "EQ_FRONT_OWNER_PLANE"],
            ["MEAS_C02", "MEAS_FRONT_SCALE", "MEAS_RUNE_DEPTH", "MEAS_METAL_DEPTH"],
            "Build the exact front-owned C02 visible domain once.",
            "one front occurrence; no backing wall",
        ),
        surface(
            "SURF_C02_TOP_HALF",
            "C02_STONE_LEFT",
            both,
            "exact_visible_owner_domain",
            ["OWN_TOP_C02"],
            [
                "EQ_TOP_XY",
                "EQ_TOP_OWNER_PLANE",
                "EQ_CANDIDATE_AXIAL_INTERSECTION",
            ],
            [
                "MEAS_C02",
                "MEAS_AXIAL_SCALE",
                "MEAS_RUNE_DEPTH",
                "MEAS_METAL_DEPTH",
            ],
            (
                "Build only the exact negative-Y source-half cells from the "
                "approved top C02 owner at MEAS_C02.world_z_top_cm. Intersect "
                "each exact cell with the selected candidate depth; never "
                "stretch it. Preserve every protected gap."
            ),
            "one source-half occurrence; Rz180 supplies the complement",
        ),
        surface(
            "SURF_C02_BOTTOM_HALF",
            "C02_STONE_LEFT",
            both,
            "exact_visible_owner_domain",
            ["OWN_BOTTOM_C02"],
            [
                "EQ_BOTTOM_XY",
                "EQ_BOTTOM_OWNER_PLANE",
                "EQ_CANDIDATE_AXIAL_INTERSECTION",
            ],
            [
                "MEAS_C02",
                "MEAS_AXIAL_SCALE",
                "MEAS_RUNE_DEPTH",
                "MEAS_METAL_DEPTH",
            ],
            (
                "Build only the exact negative-Y source-half cells from the "
                "approved bottom C02 owner at "
                "MEAS_C02.world_z_bottom_cm. Intersect each exact cell with "
                "the selected candidate depth; never stretch it. Preserve "
                "every protected gap."
            ),
            "one source-half occurrence; Rz180 supplies the complement",
        ),
        surface(
            "SURF_C03_FRONT",
            "C03_STONE_RIGHT",
            both,
            "exact_visible_owner_domain",
            ["OWN_FRONT_C03"],
            ["EQ_FRONT_XZ", "EQ_FRONT_OWNER_PLANE"],
            ["MEAS_C03", "MEAS_FRONT_SCALE", "MEAS_RUNE_DEPTH", "MEAS_METAL_DEPTH"],
            "Build the exact front-owned C03 visible domain once.",
            "one front occurrence; no backing wall",
        ),
        surface(
            "SURF_C03_TOP_HALF",
            "C03_STONE_RIGHT",
            both,
            "exact_visible_owner_domain",
            ["OWN_TOP_C03"],
            [
                "EQ_TOP_XY",
                "EQ_TOP_OWNER_PLANE",
                "EQ_CANDIDATE_AXIAL_INTERSECTION",
            ],
            [
                "MEAS_C03",
                "MEAS_AXIAL_SCALE",
                "MEAS_RUNE_DEPTH",
                "MEAS_METAL_DEPTH",
            ],
            (
                "Build only the exact negative-Y source-half cells from the "
                "approved top C03 owner at MEAS_C03.world_z_top_cm. Intersect "
                "each exact cell with the selected candidate depth; never "
                "stretch it. Preserve every protected gap."
            ),
            "one source-half occurrence; Rz180 supplies the complement",
        ),
        surface(
            "SURF_C03_BOTTOM_HALF",
            "C03_STONE_RIGHT",
            both,
            "exact_visible_owner_domain",
            ["OWN_BOTTOM_C03"],
            [
                "EQ_BOTTOM_XY",
                "EQ_BOTTOM_OWNER_PLANE",
                "EQ_CANDIDATE_AXIAL_INTERSECTION",
            ],
            [
                "MEAS_C03",
                "MEAS_AXIAL_SCALE",
                "MEAS_RUNE_DEPTH",
                "MEAS_METAL_DEPTH",
            ],
            (
                "Build only the exact negative-Y source-half cells from the "
                "approved bottom C03 owner at "
                "MEAS_C03.world_z_bottom_cm. Intersect each exact cell with "
                "the selected candidate depth; never stretch it. Preserve "
                "every protected gap."
            ),
            "one source-half occurrence; Rz180 supplies the complement",
        ),
        surface(
            "SURF_C04_RUNE_FACE_HALF",
            "C04_STRIKE_FACE_POSITIVE_X",
            ["rune_side"],
            "exact_face_half_then_local_mirror",
            ["OWN_RIGHT_C04_RUNE", "RIGHT_C04_CANDIDATE_HALF_BOUNDARIES"],
            ["EQ_RIGHT_YZ", "EQ_C04_RUNE_SOURCE_HALF", "EQ_FACE_LOCAL_MIRROR"],
            ["MEAS_C04", "MEAS_FRONT_WIDTH", "MEAS_RUNE_DEPTH"],
            (
                "Build the rune-side owner half at +X, locally mirror it once "
                "about Y=0, and weld only the exact center edge. Do not build "
                "a plate thickness or backing face."
            ),
            "one completed positive-X strike face before whole Rz180",
        ),
        surface(
            "SURF_C04_METAL_FACE_HALF",
            "C04_STRIKE_FACE_POSITIVE_X",
            ["metal_center_piece_side"],
            "exact_face_half_then_local_mirror",
            ["OWN_RIGHT_C04_METAL", "RIGHT_C04_CANDIDATE_HALF_BOUNDARIES"],
            ["EQ_RIGHT_YZ", "EQ_C04_METAL_SOURCE_HALF", "EQ_FACE_LOCAL_MIRROR"],
            ["MEAS_C04", "MEAS_FRONT_WIDTH", "MEAS_METAL_DEPTH"],
            (
                "Build the metal-center-piece owner half at +X, locally "
                "mirror it once about Y=0, and weld only the exact center "
                "edge. Pixels reserved to C01 remain excluded."
            ),
            "one completed positive-X strike face before whole Rz180",
        ),
        surface(
            "SURF_C06_ROTATIONAL_HALF",
            "C06_UPPER_HAFT_CAP",
            both,
            "source_radius_rotational_half",
            ["OWN_FRONT_C06"],
            ["EQ_RADIUS_FROM_FRONT", "EQ_ROTATIONAL_SURFACE", "EQ_COLUMN_WRAP"],
            ["MEAS_C06", "MEAS_FRONT_SCALE"],
            (
                "Use every approved C06 row and its positive exact owner edge "
                "as r(z); retain source-column U ownership without fixed old "
                "dimensions."
            ),
            "one positive-X rotational half; Rz180 supplies the complement",
        ),
        surface(
            "SURF_C07_ROTATIONAL_HALF",
            "C07_HAFT",
            both,
            "source_radius_rotational_half",
            ["OWN_FRONT_C07"],
            ["EQ_RADIUS_FROM_FRONT", "EQ_ROTATIONAL_SURFACE", "EQ_COLUMN_WRAP"],
            ["MEAS_C07", "MEAS_FRONT_SCALE"],
            (
                "Use the exact R8 front rows 670..869 and their new "
                "radius-by-Z consequence. The old fixed 5 cm shaft diameter "
                "is not carried into this run."
            ),
            "one positive-X rotational half; Rz180 supplies the complement",
        ),
        surface(
            "SURF_C07B_ROTATIONAL_HALF",
            "C07B_HAFT_TO_HANDLE_FERRULE",
            both,
            "source_radius_rotational_half",
            ["OWN_FRONT_C07B"],
            ["EQ_RADIUS_FROM_FRONT", "EQ_ROTATIONAL_SURFACE", "EQ_COLUMN_WRAP"],
            ["MEAS_C07B", "MEAS_FRONT_SCALE"],
            "Use only the exact R8 ferrule rows and their radius profile.",
            "one positive-X rotational half; Rz180 supplies the complement",
        ),
        surface(
            "SURF_C08_ROTATIONAL_HALF",
            "C08_GRIP",
            both,
            "source_radius_rotational_half",
            ["OWN_FRONT_C08"],
            ["EQ_RADIUS_FROM_FRONT", "EQ_ROTATIONAL_SURFACE", "EQ_COLUMN_WRAP"],
            ["MEAS_C08", "MEAS_FRONT_SCALE"],
            (
                "Use only exact R8 grip rows and proportional source-column "
                "wrap. Leather phase is material evidence and may not deform "
                "the geometry."
            ),
            "one positive-X rotational half; Rz180 supplies the complement",
        ),
        surface(
            "SURF_C09_ROTATIONAL_HALF",
            "C09_LOWER_COLLAR",
            both,
            "source_radius_rotational_half",
            ["OWN_FRONT_C09"],
            ["EQ_RADIUS_FROM_FRONT", "EQ_ROTATIONAL_SURFACE", "EQ_COLUMN_WRAP"],
            ["MEAS_C09", "MEAS_FRONT_SCALE"],
            "Use only exact R8 collar rows and their radius profile.",
            "one positive-X rotational half; Rz180 supplies the complement",
        ),
        surface(
            "SURF_C10_ROTATIONAL_HALF",
            "C10_POMMEL_BODY",
            both,
            "source_radius_rotational_half",
            ["OWN_FRONT_C10"],
            ["EQ_RADIUS_FROM_FRONT", "EQ_ROTATIONAL_SURFACE", "EQ_COLUMN_WRAP"],
            ["MEAS_C10", "MEAS_FRONT_SCALE"],
            (
                "Use only exact R8 pommel rows and their radius profile. The "
                "old fixed 18 cm length and 11 cm width are not carried into "
                "this run."
            ),
            "one positive-X rotational half; Rz180 supplies the complement",
        ),
        surface(
            "SURF_C11_ROTATIONAL_HALF",
            "C11_POMMEL_TERMINAL_CAP",
            both,
            "source_radius_rotational_half",
            ["OWN_FRONT_C11"],
            ["EQ_RADIUS_FROM_FRONT", "EQ_ROTATIONAL_SURFACE", "EQ_COLUMN_WRAP"],
            ["MEAS_C11", "MEAS_FRONT_SCALE"],
            "Use only exact R8 terminal-cap rows and their radius profile.",
            "one positive-X rotational half; Rz180 supplies the complement",
        ),
        surface(
            "SURF_C12_ROTATIONAL_HALF",
            "C12_UPPER_HEAD_CAP_SPIRE",
            both,
            "source_radius_rotational_half",
            ["OWN_FRONT_C12_FULL"],
            ["EQ_RADIUS_FROM_FRONT", "EQ_ROTATIONAL_SURFACE", "EQ_COLUMN_WRAP"],
            ["MEAS_C12", "MEAS_FRONT_SCALE"],
            (
                "Rows 208..220 use the exact front selected runs; rows "
                "221..294 use only the reserved existing C12 owner. No C12 "
                "shape is inferred from stone pixels."
            ),
            "one positive-X rotational half; Rz180 supplies the complement",
        ),
    ]

    closure_instructions = [
        closure(
            "CLOSURE_C02_INNER",
            ["C02_STONE_LEFT", "C01_C12_SHARED_CENTRAL_STRUCTURE"],
            both,
            "ordered_straight_ruled_faces",
            [
                "CORR_C02_FRONT_TOP_BOTTOM_INNER_OWNER_EDGES",
                "FRONT_C02_INNER_OWNER_EDGE",
                "TOP_C02_INNER_OWNER_EDGE",
                "BOTTOM_C02_INNER_OWNER_EDGE",
            ],
            ["EQ_EXACT_OWNER_BOUNDARY", "EQ_ORDERED_RULED_FACE"],
            ["MEAS_C02", "MEAS_FRONT_SCALE", "MEAS_AXIAL_SCALE"],
            (
                "Join only the approved ordered C02 inner boundary sets. "
                "Every protected run stays open; unmatched coordinates stop "
                "the later build."
            ),
        ),
        closure(
            "CLOSURE_C03_INNER",
            ["C03_STONE_RIGHT", "C01_C12_SHARED_CENTRAL_STRUCTURE"],
            both,
            "ordered_straight_ruled_faces",
            [
                "CORR_C03_FRONT_TOP_BOTTOM_INNER_OWNER_EDGES",
                "FRONT_C03_INNER_OWNER_EDGE",
                "TOP_C03_INNER_OWNER_EDGE",
                "BOTTOM_C03_INNER_OWNER_EDGE",
            ],
            ["EQ_EXACT_OWNER_BOUNDARY", "EQ_ORDERED_RULED_FACE"],
            ["MEAS_C03", "MEAS_FRONT_SCALE", "MEAS_AXIAL_SCALE"],
            (
                "Join only the approved ordered C03 inner boundary sets. "
                "Every protected run stays open; unmatched coordinates stop "
                "the later build."
            ),
        ),
        closure(
            "CLOSURE_C03_TO_C04_RUNE",
            ["C03_STONE_RIGHT", "C04_STRIKE_FACE_POSITIVE_X"],
            ["rune_side"],
            "one_common_exterior_boundary",
            [
                "OWN_FRONT_C03",
                "OWN_TOP_C03",
                "OWN_BOTTOM_C03",
                "OWN_RIGHT_C04_RUNE",
                "CORR_C04_RIGHT_CANDIDATE_FACE_EDGES",
            ],
            ["EQ_EXACT_OWNER_BOUNDARY", "EQ_ORDERED_RULED_FACE"],
            ["MEAS_C03", "MEAS_C04", "MEAS_FRONT_WIDTH", "MEAS_RUNE_DEPTH"],
            (
                "C04 replaces the outward C03 exterior occurrence at +X. "
                "Use one shared boundary and no strike-face backing plate."
            ),
        ),
        closure(
            "CLOSURE_C03_TO_C04_METAL",
            ["C03_STONE_RIGHT", "C04_STRIKE_FACE_POSITIVE_X"],
            ["metal_center_piece_side"],
            "one_common_exterior_boundary",
            [
                "OWN_FRONT_C03",
                "OWN_TOP_C03",
                "OWN_BOTTOM_C03",
                "OWN_RIGHT_C04_METAL",
                "CORR_C04_RIGHT_CANDIDATE_FACE_EDGES",
            ],
            ["EQ_EXACT_OWNER_BOUNDARY", "EQ_ORDERED_RULED_FACE"],
            ["MEAS_C03", "MEAS_C04", "MEAS_FRONT_WIDTH", "MEAS_METAL_DEPTH"],
            (
                "C04 replaces the outward C03 exterior occurrence at +X. "
                "Exclude the exact C01-reserved right pixels and create no "
                "strike-face backing plate."
            ),
        ),
        closure(
            "CONTACT_C12_C01",
            ["C12_UPPER_HEAD_CAP_SPIRE", "C01_CENTER_CORE"],
            both,
            "shared_boundary_no_duplicate_wall",
            ["FRONT_C12_RESERVED_C01_CONTACT"],
            ["EQ_EXACT_OWNER_BOUNDARY", "EQ_ORDERED_RULED_FACE"],
            ["MEAS_C12", "MEAS_C01"],
            (
                "Use the exact y=295 front contact once. C12 and C01 may "
                "share that boundary but may not carry coincident walls."
            ),
        ),
        closure(
            "CONTACT_C01_C06",
            ["C01_CENTER_CORE", "C06_UPPER_HAFT_CAP"],
            both,
            "shared_boundary_no_duplicate_wall",
            ["FRONT_C01_C06_CONTACT", "CORR_C01_C06_C07_FRONT_CONTACTS"],
            ["EQ_EXACT_OWNER_BOUNDARY", "EQ_ORDERED_RULED_FACE"],
            ["MEAS_C01", "MEAS_C06"],
            (
                "Use the exact y=600 adjacent owner runs once. The one-pixel "
                "run difference remains source evidence and is joined only by "
                "the approved straight boundary rule."
            ),
        ),
        closure(
            "CONTACT_C06_C07",
            ["C06_UPPER_HAFT_CAP", "C07_HAFT"],
            both,
            "shared_ring_or_exact_ruled_connection",
            ["FRONT_C06_C07_CONTACT", "CORR_C01_C06_C07_FRONT_CONTACTS"],
            ["EQ_EXACT_OWNER_BOUNDARY", "EQ_ORDERED_RULED_FACE"],
            ["MEAS_C06", "MEAS_C07"],
            (
                "Join at exact front edge y=670 and its source-derived ring. "
                "Do not add a receiver volume."
            ),
        ),
    ]
    transition_to_measurements = {
        "TR_C12_C01": ["MEAS_C12", "MEAS_C01"],
        "TR_C01_C06": ["MEAS_C01", "MEAS_C06"],
        "TR_C06_C07": ["MEAS_C06", "MEAS_C07"],
        "TR_C07_C07B": ["MEAS_C07", "MEAS_C07B"],
        "TR_C07B_C08": ["MEAS_C07B", "MEAS_C08"],
        "TR_C08_C09": ["MEAS_C08", "MEAS_C09"],
        "TR_C09_C10": ["MEAS_C09", "MEAS_C10"],
        "TR_C10_C11": ["MEAS_C10", "MEAS_C11"],
    }
    for transition_id in (
        "TR_C07_C07B",
        "TR_C07B_C08",
        "TR_C08_C09",
        "TR_C09_C10",
        "TR_C10_C11",
    ):
        transition = transition_catalog[transition_id]
        closure_instructions.append(
            closure(
                "CONTACT_" + transition_id.removeprefix("TR_"),
                [
                    transition["upper_component"],
                    transition["lower_component"],
                ],
                both,
                (
                    "coordinate_equal_common_half_ring"
                    if transition["same_radius"]
                    else "exact_planar_half_annular_shoulder"
                ),
                [
                    component_to_owner_id[transition["upper_component"]],
                    component_to_owner_id[transition["lower_component"]],
                ],
                ["EQ_RADIUS_FROM_FRONT", "EQ_HALF_ANNULAR_SHOULDER"],
                transition_to_measurements[transition_id],
                (
                    f"At source edge y={transition['shared_source_edge_y']}, "
                    f"use {transition['closure']} from the two exact adjacent "
                    "R8 radius records. Add no coincident wall."
                ),
            )
        )
    closure_instructions.extend(
        [
            closure(
                "CAP_C11_BOTTOM",
                ["C11_POMMEL_TERMINAL_CAP"],
                both,
                "exact_planar_positive_x_half_cap",
                ["OWN_FRONT_C11"],
                ["EQ_RADIUS_FROM_FRONT", "EQ_PLANAR_HALF_CAP"],
                ["MEAS_C11", "MEAS_OVERALL_LENGTH"],
                (
                    "Close only the exact terminal ring from front row 1270 "
                    "at world Z=0; do not extend the radius or Z range."
                ),
            ),
            closure(
                "CAP_C12_TOP",
                ["C12_UPPER_HEAD_CAP_SPIRE"],
                both,
                "exact_planar_positive_x_half_cap",
                ["OWN_FRONT_C12_FULL"],
                ["EQ_RADIUS_FROM_FRONT", "EQ_PLANAR_HALF_CAP"],
                ["MEAS_C12", "MEAS_OVERALL_LENGTH"],
                (
                    "Close only the exact terminal ring from front row 208 at "
                    "world Z=170; do not extend the radius or Z range."
                ),
            ),
            closure(
                "GUARD_PROTECTED_NEGATIVE_SPACES",
                [
                    "C01_CENTER_CORE",
                    "C02_STONE_LEFT",
                    "C03_STONE_RIGHT",
                    "C04_STRIKE_FACE_POSITIVE_X",
                    "C06_UPPER_HAFT_CAP",
                ],
                both,
                "no_surface_no_fill_guard",
                [
                    "PROTECTED_FRONT",
                    "PROTECTED_RIGHT",
                    "PROTECTED_TOP",
                    "PROTECTED_BOTTOM",
                ],
                ["EQ_EXACT_OWNER_BOUNDARY"],
                ["MEAS_FRONT_SCALE", "MEAS_RIGHT_SCALE", "MEAS_AXIAL_SCALE"],
                (
                    "Every approved exterior-connected protected pixel remains "
                    "unoccupied in every projection. A later conflict stops "
                    "before geometry is saved."
                ),
            ),
            closure(
                "WHOLE_ASSET_RZ180",
                [
                    "C01",
                    "C02",
                    "C03",
                    "C04",
                    "C06",
                    "C07",
                    "C07B",
                    "C08",
                    "C09",
                    "C10",
                    "C11",
                    "C12",
                ],
                both,
                "exact_single_whole_completion",
                [
                    "OWN_FRONT_C01",
                    "OWN_FRONT_C02",
                    "OWN_FRONT_C03",
                    "OWN_FRONT_C06",
                    "OWN_FRONT_C07",
                    "OWN_FRONT_C07B",
                    "OWN_FRONT_C08",
                    "OWN_FRONT_C09",
                    "OWN_FRONT_C10",
                    "OWN_FRONT_C11",
                    "OWN_FRONT_C12_FULL",
                ],
                ["EQ_RZ180_COMPLETION", "EQ_EQUAL_COORDINATE_WELD"],
                [
                    "MEAS_WORLD_FRAME",
                    "MEAS_FRONT_WIDTH",
                    "MEAS_RUNE_DEPTH",
                    "MEAS_METAL_DEPTH",
                    "MEAS_OVERALL_LENGTH",
                ],
                (
                    "After every source-half gate passes, apply exactly one "
                    "Rz180 completion to the whole source set. Merge only "
                    "coordinate-equal seam vertices."
                ),
            ),
        ]
    )

    reserved_evidence = [
        {
            "id": "RESERVED_TOP_CENTRAL_NON_STONE",
            "source_ownership_ref": "OWN_TOP_CENTRAL_RESERVED",
            "candidate_variants": both,
            "rule": (
                "These exact pixels remain shared C01/C12 top-view color and "
                "orientation evidence. Step 09A explicitly did not decide "
                "their C01-versus-C12 split, so they create no independent "
                "plane, plate, fill, or geometry surface. Later material "
                "registration may use them only on geometry already created "
                "by a separately cited exact component instruction."
            ),
        },
        {
            "id": "RESERVED_BOTTOM_CENTRAL_NON_STONE",
            "source_ownership_ref": "OWN_BOTTOM_CENTRAL_RESERVED",
            "candidate_variants": both,
            "rule": (
                "These exact pixels remain shared central underside color and "
                "orientation evidence. Their component and Z assignment is "
                "not approved, so they create no independent plane, plate, "
                "fill, or geometry surface. Protected surroundings remain "
                "empty."
            ),
        },
        {
            "id": "RESERVED_RIGHT_C01_METAL_VARIANT",
            "source_ownership_ref": "OWN_RIGHT_C01_RESERVED",
            "candidate_variants": ["metal_center_piece_side"],
            "rule": (
                "These exact pixels remain C01 visibility/color evidence and "
                "are excluded from C04. They do not create an independent "
                "plate, receiver, backing surface, or new geometry plane."
            ),
        },
        {
            "id": "LOCKED_BACK_NONOWNING",
            "source_file_key": "step06_back",
            "rule": (
                "Back remains color/comparison evidence only; it may not "
                "replace front-owned geometry or create a copied depth face."
            ),
        },
        {
            "id": "LOCKED_LEFT_NONOWNING",
            "source_file_key": "step07_left",
            "rule": (
                "Left remains comparison evidence and the final negative-X "
                "strike face comes only from the approved Rz180 completion."
            ),
        },
    ]

    candidate_variants = {
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

    blueprint = {
        "schema": "AERATHEA_R8_ZERO_EXTRUSION_STEP11_PRODUCTION_BLUEPRINT_A02_V1",
        "asset": ASSET,
        "run_id": "SB-CR-STEPS10-16-R8-ZERO-EXTRUSION-A02",
        "step": "11 production blueprint only",
        "date": "2026-07-23",
        "artifact_status": "candidate pending independent audit and Flamestrike decision",
        "decision": "candidate_pending_independent_audit",
        "plain_english_goal": (
            "Tell a later approved build exactly which measured source owns "
            "each surface and exactly which approved equation may connect it, "
            "without building anything now."
        ),
        "approval": {
            "decision": "approved",
            "decision_authority": "Flamestrike",
            "proposed_contract_sha256": EXPECTED_SHA256["proposed_contract"],
            "approval_record_path": str(
                FILES["approval_record"].relative_to(ROOT)
            ),
            "approval_record_sha256": sha256(FILES["approval_record"]),
            "authorized_work": "document and independent audit only",
        },
        "authority_files": {
            key: {
                "path": str(path.relative_to(ROOT)),
                "sha256": sha256(path),
                "hash_locked": key in EXPECTED_SHA256,
            }
            for key, path in FILES.items()
        },
        "algorithmic_reference_boundary": {
            "reference_files": [
                "proven_process_output",
                "proven_process_builder",
                "proven_process_audit",
            ],
            "permitted_use": (
                "algorithmic sequence, direct-surface ownership, ruled "
                "closure, completion, and independent-audit structure only"
            ),
            "forbidden_use": (
                "old mesh, old coordinates, old masks, old UVs, old "
                "materials, old textures, old dimensions, or old renders"
            ),
            "fresh_r8_measurements_required": True,
        },
        "input_gate": {
            "step09a_authority": authority_lock["decision"],
            "step09a_validation": "PASS 79/79",
            "step10_validation": "PASS 50/50",
            "step11_source_preflight": preflight["decision"],
            "step11_source_preflight_validation": (
                f"{preflight_validation['result']} "
                f"{preflight_validation['pass_count']}/"
                f"{preflight_validation['check_count']}"
            ),
            "missing_authority": preflight["missing_authority"],
        },
        "pixel_and_world_frame": {
            "pixel_convention": registration["pixel_convention"],
            "world_frame": registration["world_frame"],
            "coordinate_equations": registration["coordinate_equations"],
            "one_uniform_scale_per_view": True,
            "source_resampling": False,
            "component_specific_scaling": False,
        },
        "numeric_precedence": {
            "only_fixed_external_anchor": numeric[
                "fixed_external_numeric_anchor"
            ],
            "new_pixel_consequences": numeric["new_pixel_consequences"],
            "older_fixed_component_values_not_carried": numeric[
                "older_numeric_locks_not_carried_into_r8"
            ],
            "final_depth_precedence": numeric["final_depth_precedence"],
        },
        "candidate_variants": candidate_variants,
        "evidence_catalog": evidence_catalog,
        "measurement_catalog": measurement_catalog,
        "transition_catalog": transition_catalog,
        "equation_catalog": equation_catalog,
        "surface_instructions": surface_instructions,
        "closure_and_contact_instructions": closure_instructions,
        "reserved_evidence": reserved_evidence,
        "construction_order": [
            "verify every authority hash and exact preflight gate",
            "materialize exact evidence catalogs without changing coordinates",
            "build one selected C04 face half and perform its one local mirror",
            (
                "build C01/C02/C03 visible owner surfaces; keep unresolved "
                "central axial evidence reserved and non-geometric"
            ),
            "build C06/C07/C07B/C08/C09/C10/C11/C12 rotational source halves",
            "create only declared shared contacts, ruled faces, shoulders, and terminal caps",
            "prove protected spaces empty and every visible owner occurs once",
            "apply exactly one whole-asset Rz180 and coordinate-equal weld",
            "audit the saved candidate directly before any review render",
        ],
        "topology_and_performance_plan": {
            "lod0_target_triangles": 8000,
            "lod0_hard_cap_triangles": 10000,
            "required_lods": ["LOD0", "LOD1", "LOD2", "LOD3"],
            "lod_targets_as_lod0_fraction": {
                "LOD0": "1",
                "LOD1": "3/5",
                "LOD2": "3/10",
                "LOD3": "3/25",
            },
            "fidelity_precedence": (
                "Exact source boundaries, protected gaps, contacts, and the "
                "primary silhouette may not be reduced to meet a budget."
            ),
            "over_cap_action": (
                "Stop before saving geometry and report Blueprint block: rule "
                "missing; request a separate performance amendment."
            ),
            "pixel_to_topology_rule": (
                "Owner pixels control exact surface membership and UV/color "
                "ownership. Geometry is required at every exact boundary "
                "change and approved radius change; planar interiors may be "
                "triangulated without moving or deleting an owner boundary."
            ),
        },
        "uv_material_texture_plan": {
            "geometry_change_in_step14_or_step15": False,
            "material_families": [
                "dark faceted stone",
                "aged bronze",
                "dark steel",
                "dark brown leather",
                "cold blue rune/crystal emissive",
            ],
            "material_slot_count": 2,
            "material_slots": [
                {
                    "slot": 0,
                    "name": "MI_DRW_SiegeBreaker_Opaque",
                    "families": [
                        "dark faceted stone",
                        "aged bronze",
                        "dark steel",
                        "dark brown leather",
                    ],
                },
                {
                    "slot": 1,
                    "name": "MI_DRW_SiegeBreaker_Emissive",
                    "families": ["cold blue rune/crystal emissive"],
                },
            ],
            "texture_resolution": "2048x2048",
            "texture_set": [
                "T_DRW_SiegeBreaker_A01_BC",
                "T_DRW_SiegeBreaker_A01_N",
                "T_DRW_SiegeBreaker_A01_ORM",
                "T_DRW_SiegeBreaker_A01_E",
            ],
            "source_visible_color_rule": (
                "Exact owner-view pixels remain view-local color evidence. "
                "Back, left, ornament phase, and dark-value evidence may not "
                "change geometry."
            ),
            "uv_rule": (
                "UV ownership is component-specific. Rotational rows use the "
                "exact source-column U intervals from EQ_COLUMN_WRAP. No UV "
                "is created in Step 11."
            ),
        },
        "collision_pivot_export_plan": {
            "asset_type": "Static Mesh Weapon Prop",
            "asset_name": ASSET,
            "pivot": "bottom-center terminal/pommel at world (0,0,0)",
            "collision_proxy_count": 3,
            "collision_proxies": [
                "UCX_SM_DRW_SiegeBreaker_Hammer_A01_Head_00",
                "UCX_SM_DRW_SiegeBreaker_Hammer_A01_HaftGrip_00",
                "UCX_SM_DRW_SiegeBreaker_Hammer_A01_Pommel_00",
            ],
            "export_names": {
                "fbx": f"{ASSET}.fbx",
                "glb": f"{ASSET}.glb",
            },
            "execution_now": False,
            "unreal_path_future": (
                "/Game/Aerathea/Weapons/Dwarven/SiegeBreaker/"
            ),
        },
        "artistic_soul_review_rubric": [
            "monumental top-heavy Dwarven great-hammer silhouette",
            "two faceted stone strike masses remain readable",
            "central layered diamond remains the focal point",
            "narrow shaft remains contrasted against the massive head",
            "grip and weighted pommel remain distinct",
            "cold blue rune light stays restrained",
            "no blank back, facade, carrier, copied depth face, or projection shell",
            "protected stone/core gaps remain visibly open",
        ],
        "future_execution_contract": {
            "step12_authorized_now": False,
            "future_entry_point": (
                "python3 Tools/DCC/build_siegebreaker_r8_step12_"
                "source_geometry_a01.py --blueprint "
                "docs/assets/blueprints/SM_DRW_SiegeBreaker_Hammer_A01/"
                "proof_runs/SB-CR-STEPS10-16-R8-ZERO-EXTRUSION-A02/"
                "manifests/STEP_11_PRODUCTION_GEOMETRY_BLUEPRINT.json "
                "--candidate {rune_side|metal_center_piece_side} "
                "--output-root <fresh-isolated-root>"
            ),
            "entry_point_exists_now": False,
            "required_environment_lock_fields": [
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
            "missing_environment_field_action": (
                "fail before Blender starts; do not infer a default"
            ),
            "state_path": [
                "STEP_11_BLUEPRINT_APPROVED",
                "STEP_12_AUTHORITY_VERIFIED",
                "STEP_12_SOURCE_HALF_BUILT",
                "STEP_12_SOURCE_HALF_AUDITED",
                "STEP_12_RZ180_COMPLETED",
                "STEP_12_SAVED_CANDIDATE_AUDITED",
                "STEP_12_REVIEW_READY",
            ],
            "illegal_transition_action": "fail closed and preserve the last verified state",
            "event_trace_fields": [
                "monotonic event index",
                "UTC timestamp",
                "state before and after",
                "candidate variant",
                "command and parameters",
                "input hashes",
                "output hashes",
                "tool versions",
                "check result",
                "failure or retry reason",
            ],
            "resume_rule": (
                "Resume only from the last output whose canonical hash and "
                "state-transition record independently verify."
            ),
        },
        "clean_replay_plan": {
            "run_a_root": "<fresh-isolated-root>/run_a/{candidate}",
            "run_b_root": "<fresh-isolated-root>/run_b/{candidate}",
            "no_cross_run_output_reads": True,
            "network_access": False,
            "canonical_geometry_record": [
                "component ID",
                "exact rational vertex position before float serialization",
                "face index order",
                "normal",
                "UV",
                "material assignment",
                "transform",
                "pivot",
                "bounds",
            ],
            "required_equalities": [
                "state path",
                "canonical geometry hash",
                "component and contact records",
                "protected-space projection results",
                "LOD triangle counts",
                "collision canonical hashes",
                "review-board composition",
                "validation verdicts",
            ],
            "forced_interruption_test": (
                "interrupt after source-half audit, resume from the verified "
                "checkpoint, and require the same final canonical result"
            ),
            "negative_tests": [
                "corrupted source hash",
                "corrupted owner row",
                "corrupted scale",
                "corrupted rotation axis",
                "protected-gap fill attempt",
                "second Rz180 attempt",
                "forbidden extrusion method",
                "output hash mismatch",
            ],
        },
        "mandatory_step12_gates": [
            "all authority hashes match",
            "every constructed surface resolves to one blueprint surface instruction",
            "every hidden face resolves to one closure instruction",
            "no protected source pixel is occupied",
            "no owner pixel is claimed by two visible surfaces in one view",
            "no independent backing wall or copied depth face exists",
            "no extrusion, slab, primitive replacement, or generalized cross-section exists",
            "every rotational radius replays from the exact front row",
            "each C04 variant retains its own exact completed depth",
            "one C04 local mirror and one whole Rz180 occur, no more",
            "only coordinate-equal seam vertices weld",
            "pivot is world (0,0,0) and height is exactly 170 cm",
            "LOD0 does not exceed the hard cap or the build stops for an amendment",
        ],
        "forbidden_methods": [
            "Blender Extrude",
            "Solidify",
            "bmesh extrude operations",
            "cube or primitive replacement",
            "slab",
            "copied depth face",
            "silhouette push through depth",
            "generalized cross-section",
            "per-component backing wall",
            "source resampling",
            "nearby-row search",
            "smoothing",
            "averaging",
            "per-component scale",
            "protected-gap fill",
            "old mesh import",
            "repair-forward",
        ],
        "output_ceiling": {
            "production_blueprint_created": True,
            "blender_opened": False,
            "geometry_created": False,
            "render_created": False,
            "export_created": False,
            "unreal_created": False,
            "step12_unlocked": False,
        },
        "next_gate": (
            "independent document audit, visible review, then a separate "
            "Flamestrike approve/revise/reject/blocked decision"
        ),
    }

    OUTPUT.parent.mkdir(parents=True, exist_ok=True)
    OUTPUT.write_text(
        json.dumps(blueprint, indent=2, sort_keys=True) + "\n",
        encoding="utf-8",
    )
    print("AERATHEA_STEP11_PRODUCTION_BLUEPRINT_A02_WRITTEN")
    print(
        json.dumps(
            {
                "output": str(OUTPUT),
                "sha256": sha256(OUTPUT),
                "surface_instructions": len(surface_instructions),
                "closure_instructions": len(closure_instructions),
                "blender_opened": False,
                "geometry_created": False,
            },
            indent=2,
        )
    )


if __name__ == "__main__":
    main()
