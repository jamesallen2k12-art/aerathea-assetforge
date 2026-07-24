#!/usr/bin/env python3
"""Build the twin-hammer measurement-only authority-resolution candidate.

This tool reads only hash-locked source and measurement records. It writes one
JSON table package and creates no image, Blender data, geometry, or production
artifact.
"""

from __future__ import annotations

import argparse
from fractions import Fraction
import gzip
import hashlib
import json
from pathlib import Path
from typing import Any

from PIL import Image


ROOT = Path(__file__).resolve().parents[2]
ASSET = "SM_DRW_SiegeBreaker_Hammer_A01"
RUN_ID = "SB-CR-STEPS10-16-R8-ZERO-EXTRUSION-A02"
RUN_ROOT = (
    ROOT
    / "docs/assets/blueprints"
    / ASSET
    / "proof_runs"
    / RUN_ID
)
CONTRACT_PATH = (
    RUN_ROOT
    / "steps"
    / "TWIN_HAMMER_HEAD_CORRESPONDENCE_CONTACT_AND_ROTATIONAL_STATION_AUTHORITY_RESOLUTION_A01_CONTRACT.md"
)
OUTPUT_PATH = (
    RUN_ROOT
    / "manifests"
    / "TWIN_HAMMER_HEAD_CORRESPONDENCE_CONTACT_ROTATIONAL_STATION_AUTHORITY_A01.json"
)
APPROVED_CONTRACT_SHA256 = (
    "1352b2c008c30bda6e2755fc568126e62fc65e049b8a79c13808f4ea7e1a4548"
)

PARENT_ROOT = (
    ROOT
    / "docs/assets/blueprints"
    / ASSET
    / "proof_runs"
    / "SB-CR-STEPS01-16-R8-PIXEL-EXACT-A01"
)
STEP09A_ROOT = (
    ROOT
    / "docs/assets/blueprints"
    / ASSET
    / "proof_runs"
    / "SB-CR-R8-STEP09A-COMPONENT-PIXEL-OWNERSHIP-A01"
)
FRONT_PATH = PARENT_ROOT / "manifests/STEP_06_FRONT_MEASUREMENT_CONTRACT.json"
TOP_PATH = PARENT_ROOT / "manifests/STEP_08_TOP_MEASUREMENT_CONTRACT.json"
BOTTOM_PATH = PARENT_ROOT / "manifests/STEP_08_BOTTOM_MEASUREMENT_CONTRACT.json"
STEP09_PATH = (
    PARENT_ROOT / "manifests/STEP_09_INTEGRATED_EXACT_MEASUREMENT_INDEX.json"
)
BOUNDARY_PATH = (
    STEP09A_ROOT / "manifests/STEP_09A_BOUNDARY_AND_CORRESPONDENCE_INDEX.json"
)
SCANLINE_PATH = STEP09A_ROOT / "evidence/STEP_09A_COMPONENT_SCANLINES.json.gz"
AUTHORITY_LOCK_PATH = STEP09A_ROOT / "manifests/STEP_09A_AUTHORITY_LOCK.json"

NEW_R8_ROOT = (
    ROOT
    / "Saved/AssetForgeResearch/SiegeBreaker/A12_R8_SixViewGeneration"
    / "VisualReference_A01"
)

AUTHORITY_HASHES: dict[str, str] = {
    "AGENTS.md": "5d2d2637a58113f0a6f5ec92e40d8bb2bda9e03fb58b4868a0d9dfbb3b57ad55",
    (
        "docs/assets/blueprints/SM_DRW_SiegeBreaker_Hammer_A01/proof_runs/"
        "SB-CR-STEPS10-16-R8-ZERO-EXTRUSION-A02/manifests/STEP_STATE.json"
    ): "da38d30770c297b9f5ee74affe8dad9a2c0ff2ab4f5591891f5da1e37327cac0",
    (
        "docs/assets/blueprints/SM_DRW_SiegeBreaker_Hammer_A01/proof_runs/"
        "SB-CR-STEPS10-16-R8-ZERO-EXTRUSION-A02/steps/"
        "TWIN_HAMMER_CENTER_POST_AND_HANDLE_FRESH_BUILD_CORRECTION_A01_CONTRACT.md"
    ): "1e424dfdbb12b7e12c67e3a6c4cae29c1eb80309c5fe0d3717f6e0fd772e8b37",
    (
        "docs/assets/blueprints/SM_DRW_SiegeBreaker_Hammer_A01/proof_runs/"
        "SB-CR-STEPS10-16-R8-ZERO-EXTRUSION-A02/manifests/"
        "TWIN_HAMMER_CENTER_POST_HANDLE_FRESH_BUILD_CORRECTION_A01_AUTHORITY_PREFLIGHT.json"
    ): "b2546925d0be580fc002b88dbffb9284e5a028b3eed55f372ad5b752de7d7eee",
    (
        "docs/assets/blueprints/SM_DRW_SiegeBreaker_Hammer_A01/steps/"
        "A12_R10_R8_PIXEL_EXACT_STEPS01_16_A01_CONTRACT.md"
    ): "77b0339126388be01f59532cd6b79228450b61e739ebc10c2f849833fd337bd4",
    (
        "docs/assets/blueprints/SM_DRW_SiegeBreaker_Hammer_A01/proof_runs/"
        "SB-CR-STEPS01-16-R8-PIXEL-EXACT-A01/manifests/"
        "STEP_06_FRONT_MEASUREMENT_CONTRACT.json"
    ): "85f09fc89c8b73df8e6fdf47924e2251da9dda6decabe44fa3f3b2577b7708eb",
    (
        "docs/assets/blueprints/SM_DRW_SiegeBreaker_Hammer_A01/proof_runs/"
        "SB-CR-STEPS01-16-R8-PIXEL-EXACT-A01/manifests/"
        "STEP_08_TOP_MEASUREMENT_CONTRACT.json"
    ): "5925dee1ab39a0535150804a4353157b17d51fec648791774808c9c832dd8b36",
    (
        "docs/assets/blueprints/SM_DRW_SiegeBreaker_Hammer_A01/proof_runs/"
        "SB-CR-STEPS01-16-R8-PIXEL-EXACT-A01/manifests/"
        "STEP_08_BOTTOM_MEASUREMENT_CONTRACT.json"
    ): "aea70d998dabe9f28d3ec5fb44a2d2206f8874096a3d33ee9b836074b2ede9a2",
    (
        "docs/assets/blueprints/SM_DRW_SiegeBreaker_Hammer_A01/proof_runs/"
        "SB-CR-STEPS01-16-R8-PIXEL-EXACT-A01/manifests/"
        "STEP_09_INTEGRATED_EXACT_MEASUREMENT_INDEX.json"
    ): "5a0a3eea8f877d55216f9efabe15b0ee1cf938e4c15a825a0e218f72ba76839a",
    (
        "docs/assets/blueprints/SM_DRW_SiegeBreaker_Hammer_A01/proof_runs/"
        "SB-CR-R8-STEP09A-COMPONENT-PIXEL-OWNERSHIP-A01/steps/"
        "STEP_09A_CONTRACT.md"
    ): "be1fd161263dca733ce3ca84c0648871f98383b162652f4a6fdac0ba199a528b",
    (
        "docs/assets/blueprints/SM_DRW_SiegeBreaker_Hammer_A01/proof_runs/"
        "SB-CR-R8-STEP09A-COMPONENT-PIXEL-OWNERSHIP-A01/manifests/"
        "STEP_09A_AUTHORITY_LOCK.json"
    ): "a7e07ad68e9b2737c7c70e71e9df714766a285695693e741197900e17c3a06a5",
    (
        "docs/assets/blueprints/SM_DRW_SiegeBreaker_Hammer_A01/proof_runs/"
        "SB-CR-R8-STEP09A-COMPONENT-PIXEL-OWNERSHIP-A01/manifests/"
        "STEP_09A_BOUNDARY_AND_CORRESPONDENCE_INDEX.json"
    ): "e190ed266753c797d4f9ec812154ff3b29f5d5d780e53e235e780c43492d0bd8",
    (
        "docs/assets/blueprints/SM_DRW_SiegeBreaker_Hammer_A01/proof_runs/"
        "SB-CR-R8-STEP09A-COMPONENT-PIXEL-OWNERSHIP-A01/evidence/"
        "STEP_09A_COMPONENT_SCANLINES.json.gz"
    ): "396adfbaaefc8a8ea35104e5e96dfde322510fb4ce88530fbb32f7f3073b3562",
    (
        "docs/assets/blueprints/SM_DRW_SiegeBreaker_Hammer_A01/steps/"
        "A12_R10_R8_CORRECT_AXIS_TWO_HAMMER_A01_CONTRACT.md"
    ): "c76ba4e02336ed609e7c747d200e3e63bc247b8bf43b44541bea9392aa006517",
    (
        "docs/assets/blueprints/SM_DRW_SiegeBreaker_Hammer_A01/proof_runs/"
        "SB-CR-STEPS10-16-R8-ZERO-EXTRUSION-A02/manifests/"
        "SHARED_DEPTH_RECOVERY_BLUEPRINT_A01.json"
    ): "efdbd8795dff2031fcde9e734868ff4c617dc37ad1e7b3743c3727daea981d58",
    (
        "docs/assets/blueprints/SM_DRW_SiegeBreaker_Hammer_A01/proof_runs/"
        "SB-CR-STEPS10-16-R8-ZERO-EXTRUSION-A02/manifests/"
        "SHARED_DEPTH_RECOVERY_BLUEPRINT_A01_AUTHORITY_LOCK.json"
    ): "6889b826481e5e11dd10775f2b81467b1014687b7fda9ebbff62d519bfff09bc",
    (
        "docs/assets/blueprints/SM_DRW_SiegeBreaker_Hammer_A01/steps/"
        "A12_R10_STEP02_COMPONENT_EQUATION_CONTRACT_DRAFT.md"
    ): "a40d0b67d802687ac3c9ec9ad8e00a915cc1dc730ce31f3fab00b18a1837a21c",
    (
        "SourceAssets/Concepts/SiegeBreaker/siege_breaker_front_view.png"
    ): "d00bf9ffcfd4862884626fa961c5f6b4fd6cedfdff7936b2210ca2a905e57e95",
    (
        "SourceAssets/Concepts/SiegeBreaker/siege_breaker_back_view.png"
    ): "15b4633f2df4ee06115ef4a7e238f287ebece1bae514ad4005c1036a57359799",
    (
        "SourceAssets/Concepts/SiegeBreaker/siege_breaker_left_view.png"
    ): "1a23e0c24f7be4b12df93e2509b9d300acc9161a21a32b336f7cf63c1288d91b",
    (
        "SourceAssets/Concepts/SiegeBreaker/siege_breaker_right_view.png"
    ): "04a1e9359d518b1dec35fe161020bd23ab9e2f8d5934f24e4184aecaa91d8330",
    (
        "SourceAssets/Concepts/SiegeBreaker/siege_breaker_top_view.png"
    ): "06d9cc7f78a4fe459a1f620e4787b53bf63399f7215bb9106a4e264749147d1c",
    (
        "SourceAssets/Concepts/SiegeBreaker/siege_breaker_bottom_view.png"
    ): "634dcf706a95a7f967b0c73d3c28fff318e3f91b2866e790369a57fa3b6e8d91",
}

NEW_R8_IMAGES: dict[str, tuple[str, str]] = {
    "front": (
        "SM_DRW_SiegeBreaker_Hammer_A01_A12_R8_FRONT_A01.png",
        "9a34588afd4fef32001cd9cb2115699e7506ef1e90331c19f4d32483c60aab8c",
    ),
    "back": (
        "SM_DRW_SiegeBreaker_Hammer_A01_A12_R8_BACK_A01.png",
        "f09dd1ad3978f39e10ecee8ea7efa84336520f0cea4921fe3c410dfd04019694",
    ),
    "left": (
        "SM_DRW_SiegeBreaker_Hammer_A01_A12_R8_LEFT_A01.png",
        "7215495802065bb1907ec67f46e6f7c622b9beaf768eb710a5fc12880a6b1cc5",
    ),
    "right": (
        "SM_DRW_SiegeBreaker_Hammer_A01_A12_R8_RIGHT_A01.png",
        "58f3199babbcf9323751d04f0ffafa4316048243cf2f39992cdb6b04176306e8",
    ),
    "top": (
        "SM_DRW_SiegeBreaker_Hammer_A01_A12_R8_TOP_A01.png",
        "be3e0b70de7a6e4fad025315f22feb21dc948ea9c3e7efb0adb63a983f190f9c",
    ),
    "bottom": (
        "SM_DRW_SiegeBreaker_Hammer_A01_A12_R8_BOTTOM_A01.png",
        "d2a32732fd480a0556e882e304bcfbff1dd82d0a913ad4c36117109406de988e",
    ),
}

HEAD_BOUNDARY_IDS = [
    "FRONT_C02_INNER_OWNER_EDGE",
    "TOP_C02_INNER_OWNER_EDGE",
    "BOTTOM_C02_INNER_OWNER_EDGE",
    "FRONT_C03_INNER_OWNER_EDGE",
    "TOP_C03_INNER_OWNER_EDGE",
    "BOTTOM_C03_INNER_OWNER_EDGE",
]

COMPONENT_INTERVALS = [
    ("C06_UPPER_HAFT_CAP", "upper coupler", 600, 670),
    ("C07_HAFT", "true straight haft", 670, 870),
    ("C07B_HAFT_TO_HANDLE_FERRULE", "ferrule", 870, 955),
    ("C08_GRIP", "grip", 955, 1110),
    ("C09_LOWER_COLLAR", "lower collar", 1110, 1150),
    ("C10_POMMEL_BODY", "pommel body", 1150, 1220),
    ("C11_POMMEL_TERMINAL_CAP", "terminal cap", 1220, 1271),
]


def sha256(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest()


def canonical_json_bytes(value: Any) -> bytes:
    return (
        json.dumps(value, ensure_ascii=True, indent=2, sort_keys=True) + "\n"
    ).encode("utf-8")


def rational(value: Fraction | int) -> dict[str, Any]:
    q = value if isinstance(value, Fraction) else Fraction(value)
    return {
        "numerator": q.numerator,
        "denominator": q.denominator,
        "fraction": f"{q.numerator}/{q.denominator}",
        "display_decimal": f"{float(q):.12f}",
    }


def fraction_text(value: Fraction | int) -> str:
    q = value if isinstance(value, Fraction) else Fraction(value)
    return f"{q.numerator}/{q.denominator}"


def z_edge(source_y: int) -> Fraction:
    if 600 <= source_y <= 955:
        return Fraction(132) - Fraction(source_y - 600) * Fraction(7992, 42955)
    if 955 <= source_y <= 1110:
        return Fraction(7980, 121) - Fraction(source_y - 955) * Fraction(42, 155)
    if 1110 <= source_y <= 1271:
        return Fraction(1271 - source_y) * Fraction(18, 121)
    raise ValueError(f"source edge outside C06-C11 domain: {source_y}")


def intersect_runs(
    left: list[list[int]], right: list[list[int]]
) -> list[list[int]]:
    result: list[list[int]] = []
    for left_start, left_end in left:
        for right_start, right_end in right:
            start = max(left_start, right_start)
            end = min(left_end, right_end)
            if start < end:
                result.append([start, end])
    return result


def unit_edges(runs: list[list[int]]) -> list[list[int]]:
    return [
        [x, x + 1]
        for start, end in runs
        for x in range(start, end)
    ]


def observed_hash_replay() -> list[dict[str, Any]]:
    result: list[dict[str, Any]] = []
    checks = dict(AUTHORITY_HASHES)
    checks[str(CONTRACT_PATH.relative_to(ROOT))] = APPROVED_CONTRACT_SHA256
    for view, (filename, expected) in NEW_R8_IMAGES.items():
        checks[str((NEW_R8_ROOT / filename).relative_to(ROOT))] = expected
    for relative_path, expected in sorted(checks.items()):
        path = ROOT / relative_path
        observed = sha256(path)
        if observed != expected:
            raise RuntimeError(
                f"authority hash mismatch: {relative_path}: {observed} != {expected}"
            )
        result.append(
            {
                "path": relative_path,
                "expected_sha256": expected,
                "observed_sha256": observed,
                "result": "PASS",
            }
        )
    return result


def decode_sources() -> dict[str, Any]:
    result: dict[str, Any] = {}
    for view, (filename, expected) in NEW_R8_IMAGES.items():
        path = NEW_R8_ROOT / filename
        if sha256(path) != expected:
            raise RuntimeError(f"new-R8 source hash mismatch: {view}")
        with Image.open(path) as image:
            image.load()
            result[view] = {
                "path": str(path.relative_to(ROOT)),
                "sha256": expected,
                "mode": image.mode,
                "size_pixels": [image.width, image.height],
                "decoded_without_resampling": True,
            }
    return result


def boundary_inventory(boundaries: dict[str, Any]) -> list[dict[str, Any]]:
    result: list[dict[str, Any]] = []
    for boundary_id, record in sorted(boundaries.items()):
        samples = record.get("samples", [])
        metadata = {key: value for key, value in record.items() if key != "samples"}
        result.append(
            {
                "boundary_id": boundary_id,
                "view": record["view"],
                "sample_count": len(samples),
                "first_sample": samples[0] if samples else None,
                "last_sample": samples[-1] if samples else None,
                "metadata": metadata,
                "classification": "authoritative projected boundary evidence",
            }
        )
    return result


def projected_contacts(boundaries: dict[str, Any]) -> dict[str, Any]:
    specs = [
        (
            "FRONT_C01_C06_CONTACT",
            "c01_owner_runs_half_open",
            "c06_owner_runs_half_open",
        ),
        (
            "FRONT_C06_C07_CONTACT",
            "c06_owner_runs_half_open",
            "c07_source_domain_runs_half_open",
        ),
        (
            "FRONT_C12_RESERVED_C01_CONTACT",
            "c12_reserved_runs_half_open",
            "c01_owner_runs_half_open",
        ),
    ]
    contacts: list[dict[str, Any]] = []
    for boundary_id, left_key, right_key in specs:
        record = boundaries[boundary_id]
        runs = intersect_runs(record[left_key], record[right_key])
        edges = unit_edges(runs)
        contacts.append(
            {
                "contact_id": boundary_id,
                "view": record["view"],
                "shared_source_edge_y": record["shared_source_edge_y"],
                "left_runs_half_open": record[left_key],
                "right_runs_half_open": record[right_key],
                "intersection_runs_half_open": runs,
                "unit_source_edges": edges,
                "unit_edge_count": len(edges),
                "classification": "exact two-dimensional projected contact",
                "creates_3d_contact": False,
            }
        )

    c04 = boundaries["RIGHT_C04_TOP_BOTTOM_EDGES"]
    c04_boundaries: list[dict[str, Any]] = []
    for candidate in ("metal", "rune"):
        for position in ("top", "bottom"):
            key = f"{position}_{candidate}_owner_runs_half_open"
            runs = c04[key]
            edges = unit_edges(runs)
            c04_boundaries.append(
                {
                    "candidate": (
                        "metal_center_piece_side"
                        if candidate == "metal"
                        else "rune_side"
                    ),
                    "position": position,
                    "source_edge_y": c04[f"{position}_source_edge_y"],
                    "owner_runs_half_open": runs,
                    "unit_source_edges": edges,
                    "unit_edge_count": len(edges),
                    "classification": "exact projected owner boundary only",
                    "common_contact_status": (
                        "blocked: adjacent physical owner and incidence absent"
                    ),
                }
            )
    return {
        "front_projected_contacts": contacts,
        "right_c04_owner_boundaries": c04_boundaries,
        "bottom_center_separation": {
            "boundary_id": "BOTTOM_STONE_SEPARATION_WITHOUT_CENTRAL_OWNER",
            "sample_count": len(
                boundaries["BOTTOM_STONE_SEPARATION_WITHOUT_CENTRAL_OWNER"][
                    "samples"
                ]
            ),
            "classification": "recorded absence of bottom-specific samples",
            "fill_or_no_gap_authority": False,
        },
    }


def owner_edge_key(component: str) -> str:
    if component == "C02_STONE_LEFT":
        return "c02_owner_edge_x"
    if component == "C03_STONE_RIGHT":
        return "c03_owner_edge_x"
    raise ValueError(component)


def head_embedding_matrix(
    boundaries: dict[str, Any],
    front: dict[str, Any],
    top: dict[str, Any],
    bottom: dict[str, Any],
) -> list[dict[str, Any]]:
    front_scale = Fraction(
        front["uniform_scale_cm_per_pixel"]["numerator"],
        front["uniform_scale_cm_per_pixel"]["denominator"],
    )
    front_axis = Fraction(front["center_x_source_edge"]["numerator"])
    front_bottom = front["source_rectangle_half_open"][3]
    axial_records = {"top": top, "bottom": bottom}
    result: list[dict[str, Any]] = []
    for boundary_id in HEAD_BOUNDARY_IDS:
        boundary = boundaries[boundary_id]
        component = boundary["owner"]
        view = boundary["view"]
        edge_key = owner_edge_key(component)
        samples: list[dict[str, Any]] = []
        for index, sample in enumerate(boundary["samples"]):
            edge_x = sample[edge_key]
            source_y = sample["y"]
            if view == "front":
                observable = {
                    "X": rational((Fraction(edge_x) - front_axis) * front_scale),
                    "Z_new_r8_global_view": rational(
                        Fraction(front_bottom - source_y) * front_scale
                    ),
                }
                missing = "Y"
                registration = (
                    "new-R8 global front-view registration is observable "
                    "measurement history; complete physical Z embedding is "
                    "blocked because its A edge maps to 114070/1063 cm while "
                    "the later physical lock sets Z_A=132 cm"
                )
            else:
                record = axial_records[view]
                scale = Fraction(
                    record["uniform_scale_cm_per_pixel"]["numerator"],
                    record["uniform_scale_cm_per_pixel"]["denominator"],
                )
                x0, y0, x1, y1 = record["source_rectangle_half_open"]
                center_x = Fraction(x0 + x1, 2)
                center_y = Fraction(y0 + y1, 2)
                observable = {
                    "X_view_local": rational(
                        (Fraction(edge_x) - center_x) * scale
                    ),
                    "Y_view_local_source_down": rational(
                        (Fraction(source_y) - center_y) * scale
                    ),
                }
                missing = "Z"
                registration = (
                    "exact centered view-local metric coordinates; world-Y "
                    "sign/incidence and hidden Z are not approved"
                )
            samples.append(
                {
                    "source_order_index": index,
                    "source_edge": {"x": edge_x, "y": source_y},
                    "raw_step09a_sample": sample,
                    "view_observable_coordinates_cm": observable,
                    "unobservable_world_coordinate": missing,
                    "complete_world_xyz": False,
                    "coordinate_registration": registration,
                    "proposed_physical_edge_id": None,
                    "start_corner_id": None,
                    "end_corner_id": None,
                    "classification": {
                        "source_edge": "authoritative evidence",
                        "view_metric_coordinates": "authoritative view-local evidence",
                        "world_embedding": "blocked unknown",
                    },
                }
            )
        result.append(
            {
                "boundary_id": boundary_id,
                "component": component,
                "view": view,
                "source_order": boundary["order"],
                "sample_count": len(samples),
                "complete_world_embedding": False,
                "samples": samples,
            }
        )
    return result


def head_closure_tables(boundaries: dict[str, Any]) -> tuple[list[Any], list[Any]]:
    closures: list[dict[str, Any]] = []
    triangulation: list[dict[str, Any]] = []
    for component in ("C02_STONE_LEFT", "C03_STONE_RIGHT"):
        prefix = "C02" if component.startswith("C02") else "C03"
        rail_ids = [
            f"FRONT_{prefix}_INNER_OWNER_EDGE",
            f"TOP_{prefix}_INNER_OWNER_EDGE",
            f"BOTTOM_{prefix}_INNER_OWNER_EDGE",
        ]
        counts = [len(boundaries[rail]["samples"]) for rail in rail_ids]
        closures.append(
            {
                "patch_owner": component,
                "projected_boundary_ids": rail_ids,
                "projected_counts": counts,
                "cyclic_physical_order": None,
                "shared_corner_ids": [],
                "complete_xyz_embedding": False,
                "visible_source_owned_rails": rail_ids,
                "equation_owned_hidden_rail": None,
                "approved_closure_equation": None,
                "protected_space_ids": [
                    "TOP_STONE_SEPARATION_WITHOUT_CENTRAL_OWNER",
                    "BOTTOM_STONE_SEPARATION_WITHOUT_CENTRAL_OWNER",
                ],
                "outward_orientation": None,
                "status": "BLOCKED",
                "blocks": [
                    (
                        "Blueprint block: source authority missing — complete "
                        "3D embedding or hidden-boundary owner missing"
                    ),
                    (
                        "Blueprint block: rule missing — physical boundary "
                        "incidence or closure equation missing"
                    ),
                ],
            }
        )
        triangulation.append(
            {
                "component": component,
                "projected_boundary_ids": rail_ids,
                "projected_counts": counts,
                "zipper_rule_available": True,
                "zipper_prerequisites": {
                    "approved_two_rail_correspondence": False,
                    "shared_start_corner": False,
                    "shared_end_corner": False,
                    "complete_xyz": False,
                    "approved_closure_equation": False,
                    "approved_winding": False,
                },
                "triangle_index_triplets": [],
                "triangle_count": 0,
                "result": "BLOCKED_ZERO_TRIPLETS_EMITTED",
            }
        )
    return closures, triangulation


def station_table() -> list[dict[str, Any]]:
    result: list[dict[str, Any]] = []
    for component, semantic, start, end in COMPONENT_INTERVALS:
        z_top = z_edge(start)
        z_bottom = z_edge(end)
        result.append(
            {
                "component": component,
                "semantic_owner": semantic,
                "source_row_cells_half_open": [start, end],
                "source_row_count": end - start,
                "upper_source_edge": start,
                "lower_source_edge": end,
                "upper_world_z_cm": rational(z_top),
                "lower_world_z_cm": rational(z_bottom),
                "physical_length_cm": rational(z_top - z_bottom),
                "classification": "candidate assembled exact station authority",
            }
        )
    return result


def decorative_radius(
    rows: dict[int, dict[str, Any]], source_y: int
) -> tuple[int, Fraction]:
    positive_edge = rows[source_y]["outer_interval_half_open"][1]
    distance = positive_edge - 562
    return distance, Fraction(distance) * Fraction(11, 136)


def transition_contact_table(
    rows: dict[int, dict[str, Any]]
) -> list[dict[str, Any]]:
    transitions: list[dict[str, Any]] = []

    def add(
        edge: int,
        upper_component: str,
        lower_component: str | None,
        upper_radius: Fraction | None,
        lower_radius: Fraction | None,
        upper_owner: str,
        lower_owner: str,
        special_status: str | None = None,
    ) -> None:
        equal = (
            upper_radius is not None
            and lower_radius is not None
            and upper_radius == lower_radius
        )
        if special_status is not None:
            status = special_status
        elif equal:
            status = "candidate coordinate-equal common ring"
        else:
            status = (
                "BLOCKED: Blueprint block: rule missing — rotational "
                "transition shoulder/contact"
            )
        transitions.append(
            {
                "source_edge": edge,
                "world_z_cm": rational(z_edge(edge)),
                "upper_component": upper_component,
                "lower_component": lower_component,
                "upper_radius_owner": upper_owner,
                "lower_radius_owner": lower_owner,
                "upper_radius_cm": (
                    rational(upper_radius) if upper_radius is not None else None
                ),
                "lower_radius_cm": (
                    rational(lower_radius) if lower_radius is not None else None
                ),
                "coordinate_equal_radius": equal,
                "approved_planar_shoulder_equation": None,
                "status": status,
            }
        )

    _, c06_first = decorative_radius(rows, 600)
    _, c06_last = decorative_radius(rows, 669)
    _, c07b_first = decorative_radius(rows, 870)
    _, c07b_last = decorative_radius(rows, 954)
    _, c08_first = decorative_radius(rows, 955)
    _, c08_last = decorative_radius(rows, 1109)
    _, c09_first = decorative_radius(rows, 1110)
    _, c09_last = decorative_radius(rows, 1149)
    _, c10_first = decorative_radius(rows, 1150)
    _, c10_last = decorative_radius(rows, 1219)
    _, c11_first = decorative_radius(rows, 1220)
    _, c11_last = decorative_radius(rows, 1270)

    add(
        600,
        "C01_CENTER_CORE",
        "C06_UPPER_HAFT_CAP",
        None,
        c06_first,
        "head contact has projected evidence only",
        "new-R8 positive edge under candidate decorative factor",
        "BLOCKED: complete C01/C06 3D contact owner absent",
    )
    add(
        670,
        "C06_UPPER_HAFT_CAP",
        "C07_HAFT",
        c06_last,
        Fraction(5, 2),
        "new-R8 positive edge under candidate decorative factor",
        "approved true-haft radius",
    )
    add(
        870,
        "C07_HAFT",
        "C07B_HAFT_TO_HANDLE_FERRULE",
        Fraction(5, 2),
        c07b_first,
        "approved true-haft radius",
        "new-R8 positive edge under candidate decorative factor",
    )
    add(
        955,
        "C07B_HAFT_TO_HANDLE_FERRULE",
        "C08_GRIP",
        c07b_last,
        c08_first,
        "new-R8 positive edge under candidate decorative factor",
        "proposed C08 radius owner",
    )
    add(
        1110,
        "C08_GRIP",
        "C09_LOWER_COLLAR",
        c08_last,
        c09_first,
        "proposed C08 radius owner",
        "new-R8 positive edge under candidate decorative factor",
    )
    add(
        1150,
        "C09_LOWER_COLLAR",
        "C10_POMMEL_BODY",
        c09_last,
        c10_first,
        "new-R8 positive edge under candidate decorative factor",
        "new-R8 positive edge under candidate decorative factor",
    )
    add(
        1220,
        "C10_POMMEL_BODY",
        "C11_POMMEL_TERMINAL_CAP",
        c10_last,
        c11_first,
        "new-R8 positive edge under candidate decorative factor",
        "new-R8 positive edge under candidate decorative factor",
    )
    add(
        1271,
        "C11_POMMEL_TERMINAL_CAP",
        None,
        c11_last,
        None,
        "last new-R8 terminal row under candidate decorative factor",
        "no lower component",
        "BLOCKED: current-lineage terminal-cap closure equation absent",
    )
    return transitions


def c08_radius_table(
    rows: dict[int, dict[str, Any]]
) -> dict[str, Any]:
    lower_distances = {
        source_y: rows[source_y]["outer_interval_half_open"][1] - 562
        for source_y in range(955, 1271)
    }
    lower_max = max(lower_distances.values())
    scale = Fraction(11, 2) / lower_max
    if lower_max != 68 or scale != Fraction(11, 136):
        raise RuntimeError("lower decorative radial registration did not replay")

    row_table: list[dict[str, Any]] = []
    for source_y in range(955, 1110):
        row = rows[source_y]
        positive_edge = row["outer_interval_half_open"][1]
        distance = positive_edge - 562
        radius = Fraction(distance) * scale
        column_intervals = []
        for source_x in range(562, positive_edge):
            column_intervals.append(
                {
                    "source_column_cell_half_open": [source_x, source_x + 1],
                    "u_interval_exact": [
                        fraction_text(Fraction(source_x - 562, distance)),
                        fraction_text(Fraction(source_x + 1 - 562, distance)),
                    ],
                }
            )
        row_table.append(
            {
                "source_row": source_y,
                "source_row_cell_half_open": [source_y, source_y + 1],
                "outer_interval_half_open": row["outer_interval_half_open"],
                "positive_x_owner_edge": positive_edge,
                "raw_positive_half_radius_pixels": distance,
                "radial_scale_cm_per_pixel": rational(scale),
                "radius_cm": rational(radius),
                "world_z_cell_cm": {
                    "upper": rational(z_edge(source_y)),
                    "lower": rational(z_edge(source_y + 1)),
                },
                "source_column_parameter_ownership": column_intervals,
                "creates_ring_or_surface": False,
            }
        )
    distances = [
        item["raw_positive_half_radius_pixels"] for item in row_table
    ]
    return {
        "source_record": str(FRONT_PATH.relative_to(ROOT)),
        "source_axis_edge_x": 562,
        "source_rows_half_open": [955, 1110],
        "lower_registration_domain_half_open": [955, 1271],
        "lower_max_distance_pixels": lower_max,
        "lower_max_rows": [
            source_y
            for source_y, distance in lower_distances.items()
            if distance == lower_max
        ],
        "radial_scale_cm_per_pixel": rational(scale),
        "row_count": len(row_table),
        "minimum_distance_pixels": min(distances),
        "maximum_distance_pixels": max(distances),
        "minimum_radius_cm": rational(Fraction(min(distances)) * scale),
        "maximum_radius_cm": rational(Fraction(max(distances)) * scale),
        "rows": row_table,
        "classification": "candidate C08 radius-by-Z interpretation",
        "creates_geometry": False,
    }


def hidden_closure_table(
    transitions: list[dict[str, Any]],
) -> list[dict[str, Any]]:
    rows: list[dict[str, Any]] = [
        {
            "closure_contact_id": "C02_C01_INNER_HEAD_BOUNDARY",
            "adjacent_components": ["C02_STONE_LEFT", "C01_CENTER_CORE"],
            "visible_boundary_owners": [
                "FRONT_C02_INNER_OWNER_EDGE",
                "TOP_C02_INNER_OWNER_EDGE",
                "BOTTOM_C02_INNER_OWNER_EDGE",
            ],
            "complete_xyz_embedding": False,
            "physical_incidence": False,
            "closure_equation": None,
            "classification": "blocked unknown",
            "triangulation_permitted": False,
            "later_geometry_permitted": False,
            "reason": "missing hidden rail, corner incidence, and complete XYZ",
        },
        {
            "closure_contact_id": "C03_C01_INNER_HEAD_BOUNDARY",
            "adjacent_components": ["C03_STONE_RIGHT", "C01_CENTER_CORE"],
            "visible_boundary_owners": [
                "FRONT_C03_INNER_OWNER_EDGE",
                "TOP_C03_INNER_OWNER_EDGE",
                "BOTTOM_C03_INNER_OWNER_EDGE",
            ],
            "complete_xyz_embedding": False,
            "physical_incidence": False,
            "closure_equation": None,
            "classification": "blocked unknown",
            "triangulation_permitted": False,
            "later_geometry_permitted": False,
            "reason": "missing hidden rail, corner incidence, and complete XYZ",
        },
        {
            "closure_contact_id": "C04_HEAD_PERIMETER",
            "adjacent_components": [
                "C04_STRIKE_FACE_POSITIVE_X",
                "C02_OR_C03_STONE_OWNER_UNRESOLVED",
            ],
            "visible_boundary_owners": ["RIGHT_C04_TOP_BOTTOM_EDGES"],
            "complete_xyz_embedding": False,
            "physical_incidence": False,
            "closure_equation": None,
            "classification": "blocked unknown",
            "triangulation_permitted": False,
            "later_geometry_permitted": False,
            "reason": "adjacent component owner and complete perimeter incidence absent",
        },
        {
            "closure_contact_id": "C12_C01_HEAD_CONTACT",
            "adjacent_components": [
                "C12_UPPER_HEAD_CAP_SPIRE",
                "C01_CENTER_CORE",
            ],
            "visible_boundary_owners": ["FRONT_C12_RESERVED_C01_CONTACT"],
            "complete_xyz_embedding": False,
            "physical_incidence": False,
            "closure_equation": None,
            "classification": "projected contact evidence; 3D contact blocked",
            "triangulation_permitted": False,
            "later_geometry_permitted": False,
            "reason": "projected contact does not own a complete 3D common boundary",
        },
    ]
    for transition in transitions:
        rows.append(
            {
                "closure_contact_id": (
                    f"ROTATIONAL_TRANSITION_{transition['source_edge']}"
                ),
                "adjacent_components": [
                    transition["upper_component"],
                    transition["lower_component"],
                ],
                "visible_boundary_owners": [
                    transition["upper_radius_owner"],
                    transition["lower_radius_owner"],
                ],
                "complete_xyz_embedding": (
                    transition["coordinate_equal_radius"]
                    and transition["source_edge"] != 600
                ),
                "physical_incidence": transition["coordinate_equal_radius"],
                "closure_equation": (
                    "coordinate-equal common ring"
                    if transition["coordinate_equal_radius"]
                    else None
                ),
                "classification": (
                    "candidate interpretation"
                    if transition["coordinate_equal_radius"]
                    else "blocked unknown"
                ),
                "triangulation_permitted": False,
                "later_geometry_permitted": False,
                "reason": transition["status"],
            }
        )
    return rows


def build_candidate() -> dict[str, Any]:
    if sha256(CONTRACT_PATH) != APPROVED_CONTRACT_SHA256:
        raise RuntimeError("approved authority-resolution contract hash mismatch")

    authority_replay = observed_hash_replay()
    decoded_sources = decode_sources()
    front = json.loads(FRONT_PATH.read_text(encoding="utf-8"))
    top = json.loads(TOP_PATH.read_text(encoding="utf-8"))
    bottom = json.loads(BOTTOM_PATH.read_text(encoding="utf-8"))
    step09 = json.loads(STEP09_PATH.read_text(encoding="utf-8"))
    boundary_index = json.loads(BOUNDARY_PATH.read_text(encoding="utf-8"))
    authority_lock = json.loads(AUTHORITY_LOCK_PATH.read_text(encoding="utf-8"))
    with gzip.open(SCANLINE_PATH, "rt", encoding="utf-8") as stream:
        scanlines = json.load(stream)

    scope = authority_lock["approved_scope"]
    if not (
        scope["hidden_surfaces"] is False
        and scope["ordered_boundary_edge_sets"] is True
        and authority_lock["artifact_status"]["ordered_correspondence_groups"]
        == "authoritative"
    ):
        raise RuntimeError("Step 09A scope changed")

    expected_stations = {
        "A_begin_haft_including_coupler": 600,
        "C_coupler_meets_true_haft": 670,
        "H1_haft_meets_handle_ferrule": 870,
        "H8_ferrule_meets_grip": 955,
        "U1_grip_meets_collar": 1110,
        "U3_collar_meets_pommel": 1150,
        "L4_pommel_meets_terminal_cap": 1220,
        "terminal_bottom": 1271,
    }
    if front["component_stations_source_edges"] != expected_stations:
        raise RuntimeError("new-R8 station source edges changed")

    boundaries = boundary_index["boundaries"]
    inventory = boundary_inventory(boundaries)
    contacts = projected_contacts(boundaries)
    embeddings = head_embedding_matrix(boundaries, front, top, bottom)
    closures, triangulation = head_closure_tables(boundaries)
    stations = station_table()
    rows = {item["source_y"]: item for item in front["row_profiles"]}
    transitions = transition_contact_table(rows)
    c08 = c08_radius_table(rows)
    hidden = hidden_closure_table(transitions)

    top_gap = boundaries["TOP_STONE_SEPARATION_WITHOUT_CENTRAL_OWNER"][
        "samples"
    ]
    bottom_gap = boundaries["BOTTOM_STONE_SEPARATION_WITHOUT_CENTRAL_OWNER"][
        "samples"
    ]

    source_role = {
        "decision_status": "candidate interpretation pending Flamestrike output decision",
        "new_r8_lineage": {
            "role": (
                "current source pixels, view-local contours, component station "
                "observations, color observations, and view-local measurements"
            ),
            "decoded_sources": decoded_sources,
        },
        "step09a": {
            "role": (
                "authoritative component memberships, protected negative "
                "spaces, projected boundaries, and source order"
            ),
            "hidden_surfaces": False,
            "point_pairing": False,
            "triangulation": False,
        },
        "correct_axis_contract": {
            "role": (
                "explicit new-R8 station semantics and later physical "
                "longitudinal/radial locks"
            )
        },
        "shared_depth_blueprint": {
            "role": "validation bounds and twin identity only",
            "creates_surface": False,
        },
        "original_six_view_lineage": {
            "role": "reference only",
            "current_numeric_input": False,
            "exact_cross_lineage_mapping": None,
        },
        "component_equation_contract": {
            "role": (
                "equation-form and fail-closed precedent only; old image "
                "coordinates, scale, and stations excluded"
            )
        },
    }

    protected_disposition = {
        "top_center_separation": {
            "boundary_id": "TOP_STONE_SEPARATION_WITHOUT_CENTRAL_OWNER",
            "sample_count": len(top_gap),
            "samples": top_gap,
            "classification": "authoritative exclusion evidence",
            "fill_authority": False,
        },
        "bottom_center_separation": {
            "boundary_id": "BOTTOM_STONE_SEPARATION_WITHOUT_CENTRAL_OWNER",
            "sample_count": len(bottom_gap),
            "samples": bottom_gap,
            "classification": "recorded absence; bottom disposition unknown",
            "fill_authority": False,
        },
        "step09a_protected_negative_space_record_counts": {
            view: len(record["protected_negative_spaces"])
            for view, record in sorted(scanlines["views"].items())
        },
        "all_protected_spaces_are_exclusions": True,
        "geometry_or_fill_created": False,
    }

    front_a_global = Fraction(1271 - 600) * Fraction(170, 1063)
    front_a_lock = Fraction(132)
    result: dict[str, Any] = {
        "schema": (
            "AERATHEA_TWIN_HAMMER_HEAD_CONTACT_ROTATIONAL_AUTHORITY_A01_V1"
        ),
        "date": "2026-07-24",
        "asset": ASSET,
        "paired_asset": "SM_DRW_FoeHammer_Hammer_A01",
        "run_id": RUN_ID,
        "contract": {
            "path": str(CONTRACT_PATH.relative_to(ROOT)),
            "approved_sha256": APPROVED_CONTRACT_SHA256,
            "observed_sha256": sha256(CONTRACT_PATH),
            "flamestrike_execution_decision": "approved",
        },
        "artifact_status": (
            "candidate partial authority resolution; production remains blocked"
        ),
        "result": "PASS_MEASUREMENT_PROCESS_WITH_PARTIAL_AUTHORITY_RESOLUTION",
        "geometry_created": False,
        "imagery_created": False,
        "blender_opened": False,
        "production_authority": False,
        "authority_hash_replay": {
            "checked": len(authority_replay),
            "failures": 0,
            "result": "PASS",
            "records": authority_replay,
        },
        "source_role_and_lineage_matrix": source_role,
        "projected_boundary_inventory": inventory,
        "projected_contact_expansion": contacts,
        "head_corner_anchor_and_embedding_matrix": {
            "boundary_count": len(embeddings),
            "sample_count": sum(item["sample_count"] for item in embeddings),
            "complete_world_xyz_sample_count": 0,
            "boundaries": embeddings,
            "front_longitudinal_registration_conflict": {
                "new_r8_global_view_A_cm": rational(front_a_global),
                "later_physical_Z_A_cm": rational(front_a_lock),
                "difference_cm": rational(front_a_lock - front_a_global),
                "status": (
                    "blocked: no approved current head-Z mapping reconciles "
                    "the two registrations"
                ),
            },
        },
        "head_closure_incidence_table": closures,
        "candidate_correspondence_and_index_triangulation": {
            "rule": (
                "integer cross-multiplication zipper; executable only after "
                "complete two-rail XYZ/corner/incidence/equation authority"
            ),
            "groups": triangulation,
            "total_triangle_index_triplets": 0,
            "geometry_created": False,
        },
        "hidden_closure_and_common_contact_table": hidden,
        "c06_c11_half_open_station_table": {
            "source_station_edges": expected_stations,
            "piecewise_z_formulas": {
                "600_to_955": "132-(y-600)*(7992/42955)",
                "955_to_1110": "7980/121-(y-955)*(42/155)",
                "1110_to_1271": "(1271-y)*(18/121)",
            },
            "continuous_at_edges": [955, 1110],
            "components": stations,
        },
        "rotational_transition_contact_table": transitions,
        "c08_radius_by_z_table": c08,
        "protected_space_disposition": protected_disposition,
        "resolved_items": [
            "candidate new-R8 versus original-lineage role split",
            "exact projected C01/C06, C06/C07, and C12/C01 run intersections",
            "exact C04 top and bottom projected owner-boundary expansion",
            "complete C06-C11 half-open source station table",
            "continuous later-approved piecewise physical Z registration",
            "candidate C08 radius-by-Z ownership for all 155 source rows",
            "exact coordinate-equal C08/C09 transition-radius observation",
        ],
        "remaining_blocks": [
            {
                "label": "Blueprint block: source authority missing",
                "detail": (
                    "complete head XYZ embedding, physical corner incidence, "
                    "hidden-boundary owner, and bottom center-gap disposition"
                ),
            },
            {
                "label": "Blueprint block: rule missing",
                "detail": (
                    "complete cyclic head boundary incidence and approved "
                    "hidden-closure equation"
                ),
            },
            {
                "label": "Blueprint block: source authority conflict",
                "detail": (
                    "front global-view head Z registration maps A to "
                    "114070/1063 cm while the later physical lock sets A to "
                    "132 cm; no approved current head-Z reconciliation exists"
                ),
            },
            {
                "label": "Blueprint block: source authority missing",
                "detail": (
                    "C04 top/bottom boundaries lack an exact adjacent stone "
                    "owner and full physical perimeter incidence"
                ),
            },
            {
                "label": "Blueprint block: rule missing",
                "detail": (
                    "unequal-radius rotational contacts require current-lineage "
                    "shoulder equations; terminal cap closure also remains "
                    "unreconciled"
                ),
            },
        ],
        "prohibited_output_scan": {
            "geometry_objects": 0,
            "vertices": 0,
            "faces": 0,
            "meshes": 0,
            "blender_files": 0,
            "images": 0,
            "renders": 0,
            "exports": 0,
            "unreal_assets": 0,
            "component_fills": 0,
            "solution_overlays": 0,
            "hidden_surface_previews": 0,
            "quarantined_geometry_reads": 0,
            "result": "PASS",
        },
        "next_authority_decision": {
            "requested_from": "Flamestrike",
            "choices": ["approve", "revise", "reject", "blocked"],
            "automatic_authority_promotion": False,
            "production_contract_unlocked": False,
            "production_remains_stopped": True,
        },
        "input_cross_checks": {
            "step09_front_input_sha256": step09["inputs"]["step06_front"],
            "step09_top_input_sha256": step09["inputs"]["step08_top"],
            "step09_bottom_input_sha256": step09["inputs"]["step08_bottom"],
            "step09a_scanline_geometry_created": scanlines["geometry_created"],
            "step09a_candidate_fill_review_created": scanlines[
                "candidate_fill_review_created"
            ],
        },
        "resolver": {
            "path": str(Path(__file__).resolve().relative_to(ROOT)),
            "sha256": sha256(Path(__file__).resolve()),
            "imports_production_builder": False,
        },
    }
    return result


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument(
        "--check-only",
        action="store_true",
        help="Build and validate canonical bytes without writing the manifest.",
    )
    args = parser.parse_args()

    candidate = build_candidate()
    payload = canonical_json_bytes(candidate)
    payload_sha = hashlib.sha256(payload).hexdigest()
    if args.check_only:
        print("measurement_candidate_check=PASS")
        print(f"candidate_bytes={len(payload)}")
        print(f"candidate_sha256={payload_sha}")
        print("artifact_status=candidate partial authority resolution")
        return
    if OUTPUT_PATH.exists():
        raise RuntimeError(f"refusing to overwrite fresh output: {OUTPUT_PATH}")
    OUTPUT_PATH.write_bytes(payload)
    print(f"wrote={OUTPUT_PATH}")
    print(f"sha256={payload_sha}")
    print("result=PASS_MEASUREMENT_PROCESS_WITH_PARTIAL_AUTHORITY_RESOLUTION")


if __name__ == "__main__":
    main()
