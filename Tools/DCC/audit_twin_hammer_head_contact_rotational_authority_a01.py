#!/usr/bin/env python3
"""Independently audit the twin-hammer authority-resolution candidate.

This validator does not import the resolver. It independently reads the
hash-locked evidence and replays projected contacts, head embedding blocks,
station arithmetic, transition radii, and every C08 row/column interval.
"""

from __future__ import annotations

import argparse
import ast
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
MANIFEST_PATH = (
    RUN_ROOT
    / "manifests"
    / "TWIN_HAMMER_HEAD_CORRESPONDENCE_CONTACT_ROTATIONAL_STATION_AUTHORITY_A01.json"
)
AUDIT_PATH = (
    RUN_ROOT
    / "manifests"
    / "TWIN_HAMMER_HEAD_CORRESPONDENCE_CONTACT_ROTATIONAL_STATION_AUTHORITY_A01_INDEPENDENT_AUDIT.json"
)
RESOLVER_PATH = (
    ROOT
    / "Tools/DCC/measure_twin_hammer_head_contact_rotational_authority_a01.py"
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

EXPECTED_HASHES: dict[str, str] = {
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
    str(CONTRACT_PATH.relative_to(ROOT)): APPROVED_CONTRACT_SHA256,
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
for _view, (_filename, _hash) in NEW_R8_IMAGES.items():
    EXPECTED_HASHES[
        str((NEW_R8_ROOT / _filename).relative_to(ROOT))
    ] = _hash

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


class Audit:
    def __init__(self) -> None:
        self.checks: list[dict[str, Any]] = []

    def check(
        self,
        check_id: str,
        condition: bool,
        expected: Any | None = None,
        observed: Any | None = None,
    ) -> None:
        record: dict[str, Any] = {
            "id": check_id,
            "result": "PASS" if condition else "FAIL",
        }
        if expected is not None:
            record["expected"] = expected
        if observed is not None:
            record["observed"] = observed
        self.checks.append(record)

    @property
    def failed(self) -> list[str]:
        return [
            item["id"] for item in self.checks if item["result"] == "FAIL"
        ]

    @property
    def passed(self) -> int:
        return sum(item["result"] == "PASS" for item in self.checks)


def sha256(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest()


def canonical_json_bytes(value: Any) -> bytes:
    return (
        json.dumps(value, ensure_ascii=True, indent=2, sort_keys=True) + "\n"
    ).encode("utf-8")


def as_fraction(record: dict[str, Any]) -> Fraction:
    result = Fraction(record["numerator"], record["denominator"])
    if record["fraction"] != f"{result.numerator}/{result.denominator}":
        raise ValueError("fraction text mismatch")
    if record["display_decimal"] != f"{float(result):.12f}":
        raise ValueError("fraction decimal mismatch")
    return result


def z_edge(source_y: int) -> Fraction:
    if 600 <= source_y <= 955:
        return Fraction(132) - Fraction(source_y - 600) * Fraction(7992, 42955)
    if 955 <= source_y <= 1110:
        return Fraction(7980, 121) - Fraction(source_y - 955) * Fraction(42, 155)
    if 1110 <= source_y <= 1271:
        return Fraction(1271 - source_y) * Fraction(18, 121)
    raise ValueError(source_y)


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


def owner_edge_key(component: str) -> str:
    return (
        "c02_owner_edge_x"
        if component == "C02_STONE_LEFT"
        else "c03_owner_edge_x"
    )


def audit_authority_hashes(
    manifest: dict[str, Any], audit: Audit
) -> None:
    records = {
        item["path"]: item
        for item in manifest["authority_hash_replay"]["records"]
    }
    audit.check(
        "authority_replay_path_set",
        set(records) == set(EXPECTED_HASHES),
        sorted(EXPECTED_HASHES),
        sorted(records),
    )
    for relative_path, expected in sorted(EXPECTED_HASHES.items()):
        path = ROOT / relative_path
        observed = sha256(path) if path.is_file() else None
        audit.check(
            f"authority_hash::{relative_path}",
            observed == expected
            and relative_path in records
            and records[relative_path]["expected_sha256"] == expected
            and records[relative_path]["observed_sha256"] == expected
            and records[relative_path]["result"] == "PASS",
            expected,
            observed,
        )
    audit.check(
        "authority_replay_summary",
        manifest["authority_hash_replay"]["checked"] == len(EXPECTED_HASHES)
        and manifest["authority_hash_replay"]["failures"] == 0
        and manifest["authority_hash_replay"]["result"] == "PASS",
    )


def audit_source_decode(manifest: dict[str, Any], audit: Audit) -> None:
    decoded = manifest["source_role_and_lineage_matrix"]["new_r8_lineage"][
        "decoded_sources"
    ]
    for view, (filename, expected_hash) in NEW_R8_IMAGES.items():
        path = NEW_R8_ROOT / filename
        with Image.open(path) as image:
            image.load()
            observed = {
                "mode": image.mode,
                "size_pixels": [image.width, image.height],
            }
        item = decoded[view]
        audit.check(
            f"new_r8_decode::{view}",
            item["sha256"] == expected_hash
            and item["mode"] == observed["mode"]
            and item["size_pixels"] == observed["size_pixels"]
            and item["decoded_without_resampling"] is True,
            observed,
            {
                "mode": item["mode"],
                "size_pixels": item["size_pixels"],
            },
        )


def audit_boundaries_and_contacts(
    manifest: dict[str, Any],
    boundaries: dict[str, Any],
    audit: Audit,
) -> None:
    inventory = {
        item["boundary_id"]: item
        for item in manifest["projected_boundary_inventory"]
    }
    audit.check(
        "boundary_inventory_id_set",
        set(inventory) == set(boundaries),
    )
    for boundary_id, source in sorted(boundaries.items()):
        samples = source.get("samples", [])
        item = inventory[boundary_id]
        metadata = {key: value for key, value in source.items() if key != "samples"}
        audit.check(
            f"boundary_inventory::{boundary_id}",
            item["sample_count"] == len(samples)
            and item["first_sample"] == (samples[0] if samples else None)
            and item["last_sample"] == (samples[-1] if samples else None)
            and item["metadata"] == metadata
            and item["classification"]
            == "authoritative projected boundary evidence",
        )

    contact_specs = [
        (
            "FRONT_C01_C06_CONTACT",
            "c01_owner_runs_half_open",
            "c06_owner_runs_half_open",
            115,
        ),
        (
            "FRONT_C06_C07_CONTACT",
            "c06_owner_runs_half_open",
            "c07_source_domain_runs_half_open",
            69,
        ),
        (
            "FRONT_C12_RESERVED_C01_CONTACT",
            "c12_reserved_runs_half_open",
            "c01_owner_runs_half_open",
            149,
        ),
    ]
    projected = manifest["projected_contact_expansion"]
    contact_items = {
        item["contact_id"]: item
        for item in projected["front_projected_contacts"]
    }
    for boundary_id, left_key, right_key, expected_count in contact_specs:
        source = boundaries[boundary_id]
        runs = intersect_runs(source[left_key], source[right_key])
        edges = unit_edges(runs)
        item = contact_items[boundary_id]
        audit.check(
            f"projected_contact::{boundary_id}",
            item["shared_source_edge_y"] == source["shared_source_edge_y"]
            and item["intersection_runs_half_open"] == runs
            and item["unit_source_edges"] == edges
            and item["unit_edge_count"] == expected_count == len(edges)
            and item["creates_3d_contact"] is False,
        )

    c04_source = boundaries["RIGHT_C04_TOP_BOTTOM_EDGES"]
    c04_items = {
        (item["candidate"], item["position"]): item
        for item in projected["right_c04_owner_boundaries"]
    }
    for candidate, token in (
        ("metal_center_piece_side", "metal"),
        ("rune_side", "rune"),
    ):
        for position in ("top", "bottom"):
            runs = c04_source[f"{position}_{token}_owner_runs_half_open"]
            edges = unit_edges(runs)
            item = c04_items[(candidate, position)]
            audit.check(
                f"c04_projected_boundary::{candidate}::{position}",
                item["source_edge_y"]
                == c04_source[f"{position}_source_edge_y"]
                and item["owner_runs_half_open"] == runs
                and item["unit_source_edges"] == edges
                and item["unit_edge_count"] == len(edges)
                and item["classification"]
                == "exact projected owner boundary only",
            )
    bottom = projected["bottom_center_separation"]
    audit.check(
        "bottom_center_separation_recorded_absence",
        bottom["sample_count"] == 0
        and bottom["fill_or_no_gap_authority"] is False,
    )


def audit_head_embedding(
    manifest: dict[str, Any],
    boundaries: dict[str, Any],
    front: dict[str, Any],
    top: dict[str, Any],
    bottom: dict[str, Any],
    audit: Audit,
) -> None:
    matrix = manifest["head_corner_anchor_and_embedding_matrix"]
    items = {item["boundary_id"]: item for item in matrix["boundaries"]}
    front_scale = Fraction(
        front["uniform_scale_cm_per_pixel"]["numerator"],
        front["uniform_scale_cm_per_pixel"]["denominator"],
    )
    front_axis = Fraction(front["center_x_source_edge"]["numerator"])
    front_bottom = front["source_rectangle_half_open"][3]
    axial = {"top": top, "bottom": bottom}
    total = 0
    for boundary_id in HEAD_BOUNDARY_IDS:
        source = boundaries[boundary_id]
        item = items[boundary_id]
        component = source["owner"]
        edge_key = owner_edge_key(component)
        valid = (
            item["sample_count"] == len(source["samples"])
            and item["complete_world_embedding"] is False
        )
        for index, (sample, observed) in enumerate(
            zip(source["samples"], item["samples"], strict=True)
        ):
            edge_x = sample[edge_key]
            source_y = sample["y"]
            valid = (
                valid
                and observed["source_order_index"] == index
                and observed["source_edge"] == {"x": edge_x, "y": source_y}
                and observed["raw_step09a_sample"] == sample
                and observed["complete_world_xyz"] is False
                and observed["proposed_physical_edge_id"] is None
                and observed["start_corner_id"] is None
                and observed["end_corner_id"] is None
            )
            coordinates = observed["view_observable_coordinates_cm"]
            if source["view"] == "front":
                valid = (
                    valid
                    and observed["unobservable_world_coordinate"] == "Y"
                    and as_fraction(coordinates["X"])
                    == (Fraction(edge_x) - front_axis) * front_scale
                    and as_fraction(coordinates["Z_new_r8_global_view"])
                    == Fraction(front_bottom - source_y) * front_scale
                )
            else:
                record = axial[source["view"]]
                scale = Fraction(
                    record["uniform_scale_cm_per_pixel"]["numerator"],
                    record["uniform_scale_cm_per_pixel"]["denominator"],
                )
                x0, y0, x1, y1 = record["source_rectangle_half_open"]
                valid = (
                    valid
                    and observed["unobservable_world_coordinate"] == "Z"
                    and as_fraction(coordinates["X_view_local"])
                    == (Fraction(edge_x) - Fraction(x0 + x1, 2)) * scale
                    and as_fraction(coordinates["Y_view_local_source_down"])
                    == (Fraction(source_y) - Fraction(y0 + y1, 2)) * scale
                )
        audit.check(f"head_embedding_block::{boundary_id}", valid)
        total += len(source["samples"])
    audit.check(
        "head_embedding_summary",
        matrix["boundary_count"] == 6
        and matrix["sample_count"] == total
        and matrix["complete_world_xyz_sample_count"] == 0,
        {"boundary_count": 6, "sample_count": total},
        {
            "boundary_count": matrix["boundary_count"],
            "sample_count": matrix["sample_count"],
        },
    )
    conflict = matrix["front_longitudinal_registration_conflict"]
    expected_global = Fraction(114070, 1063)
    audit.check(
        "front_head_z_registration_conflict",
        as_fraction(conflict["new_r8_global_view_A_cm"]) == expected_global
        and as_fraction(conflict["later_physical_Z_A_cm"]) == Fraction(132)
        and as_fraction(conflict["difference_cm"])
        == Fraction(132) - expected_global
        and conflict["status"].startswith("blocked:"),
    )


def audit_head_closure_and_triangulation(
    manifest: dict[str, Any], audit: Audit
) -> None:
    closures = manifest["head_closure_incidence_table"]
    triangulation = manifest[
        "candidate_correspondence_and_index_triangulation"
    ]
    audit.check(
        "head_closure_count_and_blocks",
        len(closures) == 2
        and all(item["status"] == "BLOCKED" for item in closures)
        and all(item["complete_xyz_embedding"] is False for item in closures)
        and all(item["approved_closure_equation"] is None for item in closures)
        and all(len(item["blocks"]) == 2 for item in closures),
    )
    groups = triangulation["groups"]
    audit.check(
        "head_zero_triangulation",
        len(groups) == 2
        and triangulation["total_triangle_index_triplets"] == 0
        and triangulation["geometry_created"] is False
        and all(item["triangle_index_triplets"] == [] for item in groups)
        and all(item["triangle_count"] == 0 for item in groups)
        and all(
            item["result"] == "BLOCKED_ZERO_TRIPLETS_EMITTED"
            for item in groups
        ),
    )


def audit_stations_and_transitions(
    manifest: dict[str, Any],
    front_rows: dict[int, dict[str, Any]],
    audit: Audit,
) -> None:
    section = manifest["c06_c11_half_open_station_table"]
    components = section["components"]
    audit.check(
        "station_component_count",
        len(components) == len(COMPONENT_INTERVALS) == 7,
    )
    by_component = {item["component"]: item for item in components}
    for component, semantic, start, end in COMPONENT_INTERVALS:
        item = by_component[component]
        expected_top = z_edge(start)
        expected_bottom = z_edge(end)
        audit.check(
            f"station::{component}",
            item["semantic_owner"] == semantic
            and item["source_row_cells_half_open"] == [start, end]
            and item["source_row_count"] == end - start
            and as_fraction(item["upper_world_z_cm"]) == expected_top
            and as_fraction(item["lower_world_z_cm"]) == expected_bottom
            and as_fraction(item["physical_length_cm"])
            == expected_top - expected_bottom,
        )
    audit.check(
        "longitudinal_continuity",
        z_edge(955) == Fraction(7980, 121)
        and z_edge(1110) == Fraction(2898, 121)
        and section["continuous_at_edges"] == [955, 1110],
    )

    def decorative(source_y: int) -> Fraction:
        edge = front_rows[source_y]["outer_interval_half_open"][1]
        return Fraction(edge - 562) * Fraction(11, 136)

    expected = {
        600: (None, decorative(600), False),
        670: (decorative(669), Fraction(5, 2), False),
        870: (Fraction(5, 2), decorative(870), False),
        955: (decorative(954), decorative(955), False),
        1110: (decorative(1109), decorative(1110), True),
        1150: (decorative(1149), decorative(1150), False),
        1220: (decorative(1219), decorative(1220), False),
        1271: (decorative(1270), None, False),
    }
    transitions = {
        item["source_edge"]: item
        for item in manifest["rotational_transition_contact_table"]
    }
    audit.check(
        "transition_edge_set",
        set(transitions) == set(expected),
    )
    for edge, (upper, lower, equal) in expected.items():
        item = transitions[edge]
        observed_upper = (
            as_fraction(item["upper_radius_cm"])
            if item["upper_radius_cm"] is not None
            else None
        )
        observed_lower = (
            as_fraction(item["lower_radius_cm"])
            if item["lower_radius_cm"] is not None
            else None
        )
        audit.check(
            f"transition::{edge}",
            as_fraction(item["world_z_cm"]) == z_edge(edge)
            and observed_upper == upper
            and observed_lower == lower
            and item["coordinate_equal_radius"] is equal
            and item["approved_planar_shoulder_equation"] is None,
        )
    audit.check(
        "only_c08_c09_coordinate_equal_transition",
        [
            edge
            for edge, item in transitions.items()
            if item["coordinate_equal_radius"]
        ]
        == [1110],
    )


def audit_c08(
    manifest: dict[str, Any],
    front_rows: dict[int, dict[str, Any]],
    audit: Audit,
) -> None:
    table = manifest["c08_radius_by_z_table"]
    lower = {
        source_y: front_rows[source_y]["outer_interval_half_open"][1] - 562
        for source_y in range(955, 1271)
    }
    lower_max = max(lower.values())
    lower_max_rows = [
        source_y for source_y, value in lower.items() if value == lower_max
    ]
    scale = Fraction(11, 2) / lower_max
    audit.check(
        "c08_registration",
        lower_max == 68
        and scale == Fraction(11, 136)
        and table["lower_max_distance_pixels"] == lower_max
        and table["lower_max_rows"] == lower_max_rows
        and as_fraction(table["radial_scale_cm_per_pixel"]) == scale,
    )
    rows = table["rows"]
    audit.check(
        "c08_row_count",
        table["row_count"] == len(rows) == 155,
    )
    observed_distances: list[int] = []
    for source_y, item in zip(range(955, 1110), rows, strict=True):
        source = front_rows[source_y]
        edge = source["outer_interval_half_open"][1]
        distance = edge - 562
        observed_distances.append(distance)
        columns = item["source_column_parameter_ownership"]
        columns_valid = len(columns) == distance
        for source_x, column in zip(
            range(562, edge), columns, strict=True
        ):
            columns_valid = (
                columns_valid
                and column["source_column_cell_half_open"]
                == [source_x, source_x + 1]
                and column["u_interval_exact"]
                == [
                    f"{Fraction(source_x - 562, distance).numerator}/"
                    f"{Fraction(source_x - 562, distance).denominator}",
                    f"{Fraction(source_x + 1 - 562, distance).numerator}/"
                    f"{Fraction(source_x + 1 - 562, distance).denominator}",
                ]
            )
        audit.check(
            f"c08_row::{source_y}",
            item["source_row"] == source_y
            and item["source_row_cell_half_open"] == [source_y, source_y + 1]
            and item["outer_interval_half_open"]
            == source["outer_interval_half_open"]
            and item["positive_x_owner_edge"] == edge
            and item["raw_positive_half_radius_pixels"] == distance
            and as_fraction(item["radial_scale_cm_per_pixel"]) == scale
            and as_fraction(item["radius_cm"]) == Fraction(distance) * scale
            and as_fraction(item["world_z_cell_cm"]["upper"])
            == z_edge(source_y)
            and as_fraction(item["world_z_cell_cm"]["lower"])
            == z_edge(source_y + 1)
            and columns_valid
            and item["creates_ring_or_surface"] is False,
        )
    audit.check(
        "c08_range",
        min(observed_distances) == table["minimum_distance_pixels"] == 33
        and max(observed_distances) == table["maximum_distance_pixels"] == 38
        and as_fraction(table["minimum_radius_cm"]) == Fraction(363, 136)
        and as_fraction(table["maximum_radius_cm"]) == Fraction(209, 68),
    )


def audit_protected_and_forbidden(
    manifest: dict[str, Any],
    boundaries: dict[str, Any],
    scanlines: dict[str, Any],
    audit: Audit,
) -> None:
    disposition = manifest["protected_space_disposition"]
    top = disposition["top_center_separation"]
    bottom = disposition["bottom_center_separation"]
    top_source = boundaries["TOP_STONE_SEPARATION_WITHOUT_CENTRAL_OWNER"][
        "samples"
    ]
    bottom_source = boundaries[
        "BOTTOM_STONE_SEPARATION_WITHOUT_CENTRAL_OWNER"
    ]["samples"]
    audit.check(
        "top_protected_separation",
        top["sample_count"] == len(top_source) == 37
        and top["samples"] == top_source
        and top["fill_authority"] is False,
    )
    audit.check(
        "bottom_protected_separation",
        bottom["sample_count"] == len(bottom_source) == 0
        and bottom["samples"] == []
        and bottom["fill_authority"] is False,
    )
    expected_counts = {
        view: len(record["protected_negative_spaces"])
        for view, record in sorted(scanlines["views"].items())
    }
    audit.check(
        "protected_negative_space_counts",
        disposition["step09a_protected_negative_space_record_counts"]
        == expected_counts
        and disposition["all_protected_spaces_are_exclusions"] is True
        and disposition["geometry_or_fill_created"] is False,
    )

    prohibited = manifest["prohibited_output_scan"]
    zero_keys = [
        "geometry_objects",
        "vertices",
        "faces",
        "meshes",
        "blender_files",
        "images",
        "renders",
        "exports",
        "unreal_assets",
        "component_fills",
        "solution_overlays",
        "hidden_surface_previews",
        "quarantined_geometry_reads",
    ]
    audit.check(
        "manifest_prohibited_output_counts",
        all(prohibited[key] == 0 for key in zero_keys)
        and prohibited["result"] == "PASS"
        and manifest["geometry_created"] is False
        and manifest["imagery_created"] is False
        and manifest["blender_opened"] is False,
    )

    forbidden_suffixes = {
        ".blend",
        ".blend1",
        ".fbx",
        ".glb",
        ".gltf",
        ".png",
        ".jpg",
        ".jpeg",
        ".svg",
        ".uasset",
        ".umap",
    }
    prefix = "TWIN_HAMMER_HEAD_CORRESPONDENCE_CONTACT_ROTATIONAL_STATION_AUTHORITY_A01"
    matching_files = [
        path
        for path in RUN_ROOT.rglob(f"{prefix}*")
        if path.is_file()
    ]
    forbidden_matches = [
        str(path.relative_to(ROOT))
        for path in matching_files
        if path.suffix.lower() in forbidden_suffixes
    ]
    audit.check(
        "filesystem_no_forbidden_prefixed_outputs",
        forbidden_matches == [],
        [],
        forbidden_matches,
    )
    resolver_text = RESOLVER_PATH.read_text(encoding="utf-8")
    auditor_text = Path(__file__).read_text(encoding="utf-8")

    def imported_modules(source: str) -> set[str]:
        result: set[str] = set()
        for node in ast.walk(ast.parse(source)):
            if isinstance(node, ast.Import):
                result.update(alias.name for alias in node.names)
            elif isinstance(node, ast.ImportFrom) and node.module:
                result.add(node.module)
        return result

    resolver_imports = imported_modules(resolver_text)
    auditor_imports = imported_modules(auditor_text)
    audit.check(
        "tools_do_not_import_blender_or_each_other",
        not ({"bpy", "bmesh"} & resolver_imports)
        and not ({"bpy", "bmesh"} & auditor_imports)
        and "measure_twin_hammer_head_contact_rotational_authority_a01"
        not in auditor_imports,
    )


def build_audit() -> dict[str, Any]:
    if not MANIFEST_PATH.is_file():
        raise RuntimeError(f"candidate manifest missing: {MANIFEST_PATH}")
    manifest = json.loads(MANIFEST_PATH.read_text(encoding="utf-8"))
    audit = Audit()

    audit.check(
        "schema",
        manifest["schema"]
        == "AERATHEA_TWIN_HAMMER_HEAD_CONTACT_ROTATIONAL_AUTHORITY_A01_V1",
    )
    audit.check(
        "contract_hash_and_approval",
        sha256(CONTRACT_PATH) == APPROVED_CONTRACT_SHA256
        and manifest["contract"]["approved_sha256"]
        == APPROVED_CONTRACT_SHA256
        and manifest["contract"]["observed_sha256"]
        == APPROVED_CONTRACT_SHA256
        and manifest["contract"]["flamestrike_execution_decision"]
        == "approved",
    )
    audit.check(
        "candidate_status_and_ceiling",
        manifest["artifact_status"]
        == "candidate partial authority resolution; production remains blocked"
        and manifest["result"]
        == "PASS_MEASUREMENT_PROCESS_WITH_PARTIAL_AUTHORITY_RESOLUTION"
        and manifest["production_authority"] is False,
    )

    audit_authority_hashes(manifest, audit)
    audit_source_decode(manifest, audit)

    front = json.loads(FRONT_PATH.read_text(encoding="utf-8"))
    top = json.loads(TOP_PATH.read_text(encoding="utf-8"))
    bottom = json.loads(BOTTOM_PATH.read_text(encoding="utf-8"))
    step09 = json.loads(STEP09_PATH.read_text(encoding="utf-8"))
    boundary_index = json.loads(BOUNDARY_PATH.read_text(encoding="utf-8"))
    authority_lock = json.loads(AUTHORITY_LOCK_PATH.read_text(encoding="utf-8"))
    with gzip.open(SCANLINE_PATH, "rt", encoding="utf-8") as stream:
        scanlines = json.load(stream)

    audit.check(
        "step09_input_hash_chain",
        step09["inputs"]["step06_front"] == sha256(FRONT_PATH)
        and step09["inputs"]["step08_top"] == sha256(TOP_PATH)
        and step09["inputs"]["step08_bottom"] == sha256(BOTTOM_PATH)
        and manifest["input_cross_checks"]["step09_front_input_sha256"]
        == step09["inputs"]["step06_front"]
        and manifest["input_cross_checks"]["step09_top_input_sha256"]
        == step09["inputs"]["step08_top"]
        and manifest["input_cross_checks"]["step09_bottom_input_sha256"]
        == step09["inputs"]["step08_bottom"],
    )
    scope = authority_lock["approved_scope"]
    audit.check(
        "step09a_scope",
        scope["hidden_surfaces"] is False
        and scope["ordered_boundary_edge_sets"] is True
        and authority_lock["artifact_status"]["ordered_correspondence_groups"]
        == "authoritative",
    )
    audit.check(
        "source_role_split",
        manifest["source_role_and_lineage_matrix"]["original_six_view_lineage"][
            "role"
        ]
        == "reference only"
        and manifest["source_role_and_lineage_matrix"]["original_six_view_lineage"][
            "current_numeric_input"
        ]
        is False
        and manifest["source_role_and_lineage_matrix"]["step09a"][
            "hidden_surfaces"
        ]
        is False
        and manifest["source_role_and_lineage_matrix"]["shared_depth_blueprint"][
            "creates_surface"
        ]
        is False,
    )

    boundaries = boundary_index["boundaries"]
    audit_boundaries_and_contacts(manifest, boundaries, audit)
    audit_head_embedding(manifest, boundaries, front, top, bottom, audit)
    audit_head_closure_and_triangulation(manifest, audit)
    front_rows = {item["source_y"]: item for item in front["row_profiles"]}
    audit_stations_and_transitions(manifest, front_rows, audit)
    audit_c08(manifest, front_rows, audit)
    audit_protected_and_forbidden(manifest, boundaries, scanlines, audit)

    labels = {item["label"] for item in manifest["remaining_blocks"]}
    audit.check(
        "remaining_block_labels",
        labels
        == {
            "Blueprint block: source authority missing",
            "Blueprint block: rule missing",
            "Blueprint block: source authority conflict",
        },
    )
    audit.check(
        "next_gate_stays_manual",
        manifest["next_authority_decision"]["automatic_authority_promotion"]
        is False
        and manifest["next_authority_decision"]["production_contract_unlocked"]
        is False
        and manifest["next_authority_decision"]["production_remains_stopped"]
        is True,
    )

    failed = audit.failed
    return {
        "schema": (
            "AERATHEA_TWIN_HAMMER_HEAD_CONTACT_ROTATIONAL_AUTHORITY_A01_"
            "INDEPENDENT_AUDIT_V1"
        ),
        "date": "2026-07-24",
        "asset": ASSET,
        "paired_asset": "SM_DRW_FoeHammer_Hammer_A01",
        "run_id": RUN_ID,
        "artifact_status": "proof only",
        "result": "PASS" if not failed else "FAIL",
        "checks_total": len(audit.checks),
        "checks_passed": audit.passed,
        "checks_failed": len(failed),
        "failed_check_ids": failed,
        "checks": audit.checks,
        "candidate_manifest": {
            "path": str(MANIFEST_PATH.relative_to(ROOT)),
            "sha256": sha256(MANIFEST_PATH),
            "artifact_status": manifest["artifact_status"],
            "production_authority": False,
        },
        "contract": {
            "path": str(CONTRACT_PATH.relative_to(ROOT)),
            "approved_sha256": APPROVED_CONTRACT_SHA256,
            "observed_sha256": sha256(CONTRACT_PATH),
        },
        "tools": {
            "resolver": {
                "path": str(RESOLVER_PATH.relative_to(ROOT)),
                "sha256": sha256(RESOLVER_PATH),
            },
            "independent_auditor": {
                "path": str(Path(__file__).resolve().relative_to(ROOT)),
                "sha256": sha256(Path(__file__).resolve()),
                "imports_resolver": False,
            },
        },
        "replayed_observation_totals": {
            "authority_hashes": len(EXPECTED_HASHES),
            "new_r8_images_decoded": 6,
            "head_boundary_sequences": 6,
            "head_boundary_samples": sum(
                len(boundaries[boundary_id]["samples"])
                for boundary_id in HEAD_BOUNDARY_IDS
            ),
            "projected_contact_unit_edges": 115 + 69 + 149,
            "head_triangle_index_triplets": 0,
            "component_intervals": 7,
            "station_edges": 8,
            "rotational_transitions": 8,
            "c08_rows": 155,
            "geometry_outputs": 0,
            "image_outputs": 0,
            "blender_outputs": 0,
        },
        "candidate_disposition": (
            "candidate partial authority resolution; production remains blocked"
        ),
        "remaining_authority_need": (
            "Flamestrike approve/revise/reject/blocked decision on the "
            "candidate tables; complete head embedding/closure and unequal-"
            "radius transition rules remain blocked"
        ),
        "geometry_created": False,
        "imagery_created": False,
        "blender_opened": False,
        "production_authority": False,
    }


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument(
        "--check-only",
        action="store_true",
        help="Run the independent replay without writing the audit manifest.",
    )
    args = parser.parse_args()
    result = build_audit()
    payload = canonical_json_bytes(result)
    payload_sha = hashlib.sha256(payload).hexdigest()
    if args.check_only:
        print(f"independent_audit={result['result']}")
        print(
            f"checks={result['checks_passed']}/{result['checks_total']} "
            f"failed={result['checks_failed']}"
        )
        print(f"audit_candidate_sha256={payload_sha}")
        if result["result"] != "PASS":
            raise SystemExit(1)
        return
    if AUDIT_PATH.exists():
        raise RuntimeError(f"refusing to overwrite fresh output: {AUDIT_PATH}")
    AUDIT_PATH.write_bytes(payload)
    print(f"wrote={AUDIT_PATH}")
    print(f"sha256={payload_sha}")
    print(f"result={result['result']}")
    print(
        f"checks={result['checks_passed']}/{result['checks_total']} "
        f"failed={result['checks_failed']}"
    )
    if result["result"] != "PASS":
        raise SystemExit(1)


if __name__ == "__main__":
    main()
