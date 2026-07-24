#!/usr/bin/env python3
"""Build the approved shared-depth Siege Breaker and Foe Hammer twins.

This is a clean recovery builder.  It reads only hash-locked source
measurements, approved component ownership scanlines, the approved recovery
blueprint, and its fresh-builder approval record.  It never reads either
quarantined Step 12 builder output, canonical-geometry output, or blend file.

System Python is the public entry point.  The exact project-local Blender
binary re-enters this file with ``--internal-build-all`` or
``--internal-render``.
"""

from __future__ import annotations

import argparse
import gzip
import hashlib
import json
import math
import os
import shutil
import subprocess
import sys
from dataclasses import dataclass, field
from datetime import datetime, timezone
from fractions import Fraction
from pathlib import Path
from typing import Any, Iterable, Iterator, Sequence


ROOT = Path(__file__).resolve().parents[2]
RUN_ID = "SB-CR-STEPS10-16-R8-ZERO-EXTRUSION-A02"
BUILD_ID = "FRESH_TWIN_DCC_SOURCE_BUILDER_A01"
PROOF_ROOT = ROOT / (
    "docs/assets/blueprints/SM_DRW_SiegeBreaker_Hammer_A01/proof_runs/"
    "SB-CR-STEPS10-16-R8-ZERO-EXTRUSION-A02"
)
MEASUREMENT_ROOT = ROOT / (
    "docs/assets/blueprints/SM_DRW_SiegeBreaker_Hammer_A01/proof_runs/"
    "SB-CR-STEPS01-16-R8-PIXEL-EXACT-A01/manifests"
)
OWNERSHIP_ROOT = ROOT / (
    "docs/assets/blueprints/SM_DRW_SiegeBreaker_Hammer_A01/proof_runs/"
    "SB-CR-R8-STEP09A-COMPONENT-PIXEL-OWNERSHIP-A01"
)

BLUEPRINT = PROOF_ROOT / "manifests/SHARED_DEPTH_RECOVERY_BLUEPRINT_A01.json"
BLUEPRINT_LOCK = (
    PROOF_ROOT
    / "manifests/SHARED_DEPTH_RECOVERY_BLUEPRINT_A01_AUTHORITY_LOCK.json"
)
BLUEPRINT_VALIDATION = (
    PROOF_ROOT
    / "manifests/SHARED_DEPTH_RECOVERY_BLUEPRINT_A01_VALIDATION.json"
)
BUILD_APPROVAL = (
    PROOF_ROOT / "steps/FRESH_TWIN_DCC_SOURCE_BUILDER_A01_APPROVAL_RECORD.md"
)
A11_DEPTH = ROOT / (
    "docs/assets/blueprints/SM_DRW_SiegeBreaker_Hammer_A01/manifests/"
    "A11_TRUE_AXIAL_TOP_BOTTOM_PIXEL_MEASUREMENT.json"
)
STEP05 = MEASUREMENT_ROOT / "STEP_05_PIXEL_WORLD_REGISTRATION_LOCK.json"
STEP06_FRONT = MEASUREMENT_ROOT / "STEP_06_FRONT_MEASUREMENT_CONTRACT.json"
STEP07_RIGHT = MEASUREMENT_ROOT / "STEP_07_RIGHT_MEASUREMENT_CONTRACT.json"
STEP08_TOP = MEASUREMENT_ROOT / "STEP_08_TOP_MEASUREMENT_CONTRACT.json"
STEP08_BOTTOM = MEASUREMENT_ROOT / "STEP_08_BOTTOM_MEASUREMENT_CONTRACT.json"
STEP09_INDEX = MEASUREMENT_ROOT / "STEP_09_INTEGRATED_EXACT_MEASUREMENT_INDEX.json"
STEP09A_LOCK = OWNERSHIP_ROOT / "manifests/STEP_09A_AUTHORITY_LOCK.json"
STEP09A_BOUNDARIES = (
    OWNERSHIP_ROOT / "manifests/STEP_09A_BOUNDARY_AND_CORRESPONDENCE_INDEX.json"
)
STEP09A_SCANLINES = (
    OWNERSHIP_ROOT / "evidence/STEP_09A_COMPONENT_SCANLINES.json.gz"
)
ENVIRONMENT_LOCK = PROOF_ROOT / "manifests/STEP_12_ENVIRONMENT_LOCK_A01.json"

BLENDER = ROOT / "Tools/External/Blender/blender-4.5.11-linux-x64/blender"
AUDITOR = ROOT / "Tools/DCC/audit_siegebreaker_foehammer_shared_depth_a01.py"

ASSETS = {
    "siege_breaker": {
        "asset_id": "SM_DRW_SiegeBreaker_Hammer_A01",
        "display_name": "Siege Breaker",
        "variant": "rune_side",
        "output_root": ROOT
        / (
            "SourceAssets/Blender/Weapons/Dwarven/"
            "SM_DRW_SiegeBreaker_Hammer_A01/"
            "A12_R10_R8_SharedDepth_DCCSource_A01"
        ),
    },
    "foe_hammer": {
        "asset_id": "SM_DRW_FoeHammer_Hammer_A01",
        "display_name": "Foe Hammer",
        "variant": "metal_center_piece_side",
        "output_root": ROOT
        / (
            "SourceAssets/Blender/Weapons/Dwarven/"
            "SM_DRW_FoeHammer_Hammer_A01/"
            "A12_R10_R8_SharedDepth_DCCSource_A01"
        ),
    },
}

COMBINED_MANIFEST = (
    PROOF_ROOT / "manifests/FRESH_TWIN_DCC_SOURCE_BUILDER_A01_MANIFEST.json"
)
REVIEW_BOARD = (
    PROOF_ROOT / "review/FRESH_TWIN_DCC_SOURCE_BUILDER_A01_REVIEW.png"
)

EXPECTED_HASHES = {
    BLUEPRINT: "efdbd8795dff2031fcde9e734868ff4c617dc37ad1e7b3743c3727daea981d58",
    BLUEPRINT_LOCK: "6889b826481e5e11dd10775f2b81467b1014687b7fda9ebbff62d519bfff09bc",
    BLUEPRINT_VALIDATION: "48e53e3ddfff94319927aebaec47fcbe9c40ea7369c20a4b73cdc0c38fa47ff5",
    BUILD_APPROVAL: "8b59685cf27656805ecf73385ab980c1d96dec2686ac1928f6f547f4dad787ef",
    A11_DEPTH: "46877ab4b0142d8141deb4feab234f461a31e61e118d3ce7b41e0b3679786096",
    STEP05: "aed4b8d87a4a5b442c0465c9db59fa524f63797153d662e1a5e7cf90423a2446",
    STEP06_FRONT: "85f09fc89c8b73df8e6fdf47924e2251da9dda6decabe44fa3f3b2577b7708eb",
    STEP07_RIGHT: "977831e86b02148125a7e1a04024d2d114721590ebf63937bdd314d02cc427c9",
    STEP08_TOP: "5925dee1ab39a0535150804a4353157b17d51fec648791774808c9c832dd8b36",
    STEP08_BOTTOM: "aea70d998dabe9f28d3ec5fb44a2d2206f8874096a3d33ee9b836074b2ede9a2",
    STEP09_INDEX: "5a0a3eea8f877d55216f9efabe15b0ee1cf938e4c15a825a0e218f72ba76839a",
    STEP09A_LOCK: "a7e07ad68e9b2737c7c70e71e9df714766a285695693e741197900e17c3a06a5",
    STEP09A_BOUNDARIES: "e190ed266753c797d4f9ec812154ff3b29f5d5d780e53e235e780c43492d0bd8",
    STEP09A_SCANLINES: "396adfbaaefc8a8ea35104e5e96dfde322510fb4ce88530fbb32f7f3073b3562",
    ENVIRONMENT_LOCK: "a2d9be9162d3aa5440492765aafe621e63bc4a1f80814bd523dce20dae7b66f8",
    BLENDER: "dc72290ee8651c93c4a946c012c5f2a034946fd320e6c3ab214fa23181427428",
}

FRONT_SCALE = Fraction(170, 1063)
AXIAL_SCALE = Fraction(52020, 517681)
RIGHT_SCALE = Fraction(85, 548)
FRONT_AXIS_X = Fraction(562)
FRONT_Z_ORIGIN_Y = Fraction(1271)
TOP_CENTER_X = Fraction(1533, 2)
TOP_CENTER_Y = Fraction(1093, 2)
BOTTOM_CENTER_X = Fraction(1529, 2)
BOTTOM_CENTER_Y = Fraction(539)
RIGHT_AXIS_X = Fraction(557)
RIGHT_Z_ORIGIN_Y = Fraction(1262)
STRIKE_PLANE_X = Fraction(52020, 1063)
COMMON_HALF_DEPTH = Fraction(3322106, 149985)
EXPECTED_BOUNDS = (
    Fraction(50719500, 517681),
    Fraction(6644212, 149985),
    Fraction(170),
)
ANGULAR_DIVISIONS = 64

COMPONENT_COLORS = {
    "C01_CENTER_CORE": (0.18, 0.24, 0.30, 1.0),
    "C02_STONE_LEFT": (0.075, 0.095, 0.12, 1.0),
    "C03_STONE_RIGHT": (0.075, 0.095, 0.12, 1.0),
    "C04_LOCAL_TREATMENT": (0.055, 0.18, 0.34, 1.0),
    "C06_UPPER_HAFT_CAP": (0.34, 0.18, 0.055, 1.0),
    "C07_HAFT": (0.16, 0.18, 0.20, 1.0),
    "C07B_HAFT_TO_HANDLE_FERRULE": (0.32, 0.16, 0.045, 1.0),
    "C08_GRIP": (0.12, 0.045, 0.018, 1.0),
    "C09_LOWER_COLLAR": (0.32, 0.16, 0.045, 1.0),
    "C10_POMMEL_BODY": (0.15, 0.17, 0.20, 1.0),
    "C11_POMMEL_TERMINAL_CAP": (0.30, 0.14, 0.035, 1.0),
    "C12_UPPER_HEAD_CAP_SPIRE": (0.32, 0.16, 0.045, 1.0),
    "CLOSURE": (0.105, 0.125, 0.15, 1.0),
    "CONTACT": (0.22, 0.14, 0.055, 1.0),
}


def utc_now() -> str:
    return datetime.now(timezone.utc).isoformat()


def sha256(path: Path) -> str:
    digest = hashlib.sha256()
    with path.open("rb") as handle:
        for block in iter(lambda: handle.read(1024 * 1024), b""):
            digest.update(block)
    return digest.hexdigest()


def canonical_sha256(value: Any) -> str:
    return hashlib.sha256(
        json.dumps(
            value, sort_keys=True, separators=(",", ":"), ensure_ascii=True
        ).encode("ascii")
    ).hexdigest()


def relative(path: Path) -> str:
    return str(path.resolve().relative_to(ROOT))


def qstr(value: Fraction) -> str:
    return f"{value.numerator}/{value.denominator}"


def exact(record: dict[str, Any]) -> Fraction:
    return Fraction(int(record["numerator"]), int(record["denominator"]))


def load_json(path: Path) -> dict[str, Any]:
    return json.loads(path.read_text(encoding="utf-8"))


def load_gzip_json(path: Path) -> dict[str, Any]:
    with gzip.open(path, "rt", encoding="utf-8") as handle:
        return json.load(handle)


def verify_authority() -> tuple[dict[str, Any], list[dict[str, Any]]]:
    checks = []
    for path, expected in EXPECTED_HASHES.items():
        observed = sha256(path) if path.is_file() else None
        if observed != expected:
            raise RuntimeError(
                f"Authority hash mismatch for {relative(path)}: "
                f"expected {expected}, observed {observed}"
            )
        checks.append(
            {
                "path": relative(path),
                "sha256": observed,
                "result": "PASS",
            }
        )
    blueprint = load_json(BLUEPRINT)
    lock = load_json(BLUEPRINT_LOCK)
    ownership_lock = load_json(STEP09A_LOCK)
    if lock["artifact_status"] != "authoritative":
        raise RuntimeError("Shared-depth authority lock is not authoritative")
    if lock["blueprint"]["effective_status"] != (
        "authoritative shared-depth recovery blueprint"
    ):
        raise RuntimeError("Shared-depth blueprint effective status failed")
    if ownership_lock["decision"] != "approved":
        raise RuntimeError("Step 09A ownership set is not approved")
    if blueprint["evidence_interpretation_guards"][
        "source_owner_required_for_every_surface"
    ] is not True:
        raise RuntimeError("Blueprint surface provenance guard is absent")
    expected = blueprint["shared_output_bounds_cm_exact"]
    blueprint_bounds = (
        Fraction(
            expected["width_x"]["numerator"],
            expected["width_x"]["denominator"],
        ),
        Fraction(
            expected["depth_y"]["numerator"],
            expected["depth_y"]["denominator"],
        ),
        Fraction(
            expected["height_z"]["numerator"],
            expected["height_z"]["denominator"],
        ),
    )
    if blueprint_bounds != EXPECTED_BOUNDS:
        raise RuntimeError("Shared XYZ authority does not match builder lock")
    if blueprint["global_depth_ownership"][
        "candidate_specific_global_depth_allowed"
    ]:
        raise RuntimeError("Candidate-specific global depth is forbidden")
    return blueprint, checks


@dataclass
class MeshRecord:
    name: str
    component: str
    source_owner: str
    equation_id: str
    occurrence: str
    material_key: str
    variant_local_c04: bool = False
    local_extent_audit_owner: bool = False
    smooth: bool = False
    vertices: list[tuple[Fraction, Fraction, Fraction]] = field(
        default_factory=list
    )
    faces: list[tuple[int, ...]] = field(default_factory=list)
    _lookup: dict[tuple[Fraction, Fraction, Fraction], int] = field(
        default_factory=dict, repr=False
    )

    def vertex(self, point: tuple[Fraction, Fraction, Fraction]) -> int:
        index = self._lookup.get(point)
        if index is None:
            index = len(self.vertices)
            self._lookup[point] = index
            self.vertices.append(point)
        return index

    def face(
        self, points: Sequence[tuple[Fraction, Fraction, Fraction]]
    ) -> None:
        indices = tuple(self.vertex(point) for point in points)
        if len(indices) >= 3 and len(set(indices)) == len(indices):
            self.faces.append(indices)

    def rz180(self, suffix: str = "__RZ180") -> "MeshRecord":
        result = MeshRecord(
            name=f"{self.name}{suffix}",
            component=self.component,
            source_owner=self.source_owner,
            equation_id=self.equation_id,
            occurrence="WHOLE_ASSET_RZ180",
            material_key=self.material_key,
            variant_local_c04=self.variant_local_c04,
            local_extent_audit_owner=self.local_extent_audit_owner,
            smooth=self.smooth,
        )
        result.vertices = [(-x, -y, z) for x, y, z in self.vertices]
        result._lookup = {
            point: index for index, point in enumerate(result.vertices)
        }
        result.faces = list(self.faces)
        return result

    @property
    def triangles(self) -> int:
        return sum(max(0, len(face) - 2) for face in self.faces)


def record_hash(records: Sequence[MeshRecord]) -> str:
    digest = hashlib.sha256()
    for record in sorted(records, key=lambda item: item.name):
        header = (
            record.name,
            record.component,
            record.source_owner,
            record.equation_id,
            record.occurrence,
            record.material_key,
            record.variant_local_c04,
            record.local_extent_audit_owner,
            record.smooth,
        )
        digest.update(repr(header).encode("utf-8"))
        for point in record.vertices:
            digest.update(
                ("v:" + ",".join(qstr(value) for value in point) + "\n").encode(
                    "ascii"
                )
            )
        for face in record.faces:
            digest.update(
                ("f:" + ",".join(str(index) for index in face) + "\n").encode(
                    "ascii"
                )
            )
    return digest.hexdigest()


def combined_bounds(records: Sequence[MeshRecord]) -> dict[str, Any]:
    vertices = [
        point for record in records for point in record.vertices
    ]
    minimum = [
        min(point[axis] for point in vertices) for axis in range(3)
    ]
    maximum = [
        max(point[axis] for point in vertices) for axis in range(3)
    ]
    dimensions = [
        maximum[axis] - minimum[axis] for axis in range(3)
    ]
    return {
        "minimum_exact": [qstr(value) for value in minimum],
        "maximum_exact": [qstr(value) for value in maximum],
        "dimensions_exact": [qstr(value) for value in dimensions],
        "minimum_decimal": [float(value) for value in minimum],
        "maximum_decimal": [float(value) for value in maximum],
        "dimensions_decimal": [float(value) for value in dimensions],
        "_dimensions": dimensions,
    }


def owner_rows(
    scanlines: dict[str, Any], view: str, component: str
) -> list[dict[str, Any]]:
    return scanlines["views"][view]["component_owners"][component]["rows"]


def iter_owner_cells(
    rows: Iterable[dict[str, Any]],
) -> Iterator[tuple[int, int]]:
    for row in rows:
        source_y = int(row.get("y", row.get("source_y")))
        runs = row.get("owner_runs_half_open", row.get("runs_half_open"))
        for start, stop in runs:
            for source_x in range(int(start), int(stop)):
                yield source_x, source_y


def front_point(
    source_x: Fraction, source_y: Fraction, world_y: Fraction
) -> tuple[Fraction, Fraction, Fraction]:
    return (
        (source_x - FRONT_AXIS_X) * FRONT_SCALE,
        world_y,
        (FRONT_Z_ORIGIN_Y - source_y) * FRONT_SCALE,
    )


def top_point(
    source_x: Fraction, source_y: Fraction, world_z: Fraction
) -> tuple[Fraction, Fraction, Fraction]:
    return (
        (source_x - TOP_CENTER_X) * AXIAL_SCALE,
        (source_y - TOP_CENTER_Y) * AXIAL_SCALE,
        world_z,
    )


def bottom_point(
    source_x: Fraction, source_y: Fraction, world_z: Fraction
) -> tuple[Fraction, Fraction, Fraction]:
    return (
        (BOTTOM_CENTER_X - source_x) * AXIAL_SCALE,
        (BOTTOM_CENTER_Y - source_y) * AXIAL_SCALE,
        world_z,
    )


def c04_point(
    variant: str, source_x: Fraction, source_y: Fraction
) -> tuple[Fraction, Fraction, Fraction]:
    if variant == "rune_side":
        world_y = -(source_x - RIGHT_AXIS_X) * RIGHT_SCALE
    elif variant == "metal_center_piece_side":
        world_y = (source_x - RIGHT_AXIS_X) * RIGHT_SCALE
    else:
        raise ValueError(variant)
    return (
        STRIKE_PLANE_X,
        world_y,
        (RIGHT_Z_ORIGIN_Y - source_y) * RIGHT_SCALE,
    )


def axial_source_y_limits(plane: str) -> tuple[Fraction, Fraction]:
    if plane == "top":
        return (
            TOP_CENTER_Y - COMMON_HALF_DEPTH / AXIAL_SCALE,
            TOP_CENTER_Y,
        )
    if plane == "bottom":
        return (
            BOTTOM_CENTER_Y,
            BOTTOM_CENTER_Y + COMMON_HALF_DEPTH / AXIAL_SCALE,
        )
    raise ValueError(plane)


def vector_sub(
    a: tuple[Fraction, Fraction, Fraction],
    b: tuple[Fraction, Fraction, Fraction],
) -> tuple[Fraction, Fraction, Fraction]:
    return (a[0] - b[0], a[1] - b[1], a[2] - b[2])


def cross(
    a: tuple[Fraction, Fraction, Fraction],
    b: tuple[Fraction, Fraction, Fraction],
) -> tuple[Fraction, Fraction, Fraction]:
    return (
        a[1] * b[2] - a[2] * b[1],
        a[2] * b[0] - a[0] * b[2],
        a[0] * b[1] - a[1] * b[0],
    )


def polygon_normal(
    points: Sequence[tuple[Fraction, Fraction, Fraction]]
) -> tuple[Fraction, Fraction, Fraction]:
    normal = [Fraction(0), Fraction(0), Fraction(0)]
    wrapped = list(points) + [points[0]]
    for current, following in zip(wrapped, wrapped[1:]):
        normal[0] += (current[1] - following[1]) * (
            current[2] + following[2]
        )
        normal[1] += (current[2] - following[2]) * (
            current[0] + following[0]
        )
        normal[2] += (current[0] - following[0]) * (
            current[1] + following[1]
        )
    return tuple(normal)  # type: ignore[return-value]


def build_front_surface(
    name: str,
    component: str,
    source_owner: str,
    rows: list[dict[str, Any]],
) -> MeshRecord:
    record = MeshRecord(
        name=name,
        component=component,
        source_owner=source_owner,
        equation_id="EQ_FRONT_OWNER_CELL_AT_SHARED_FRONT_PLANE",
        occurrence="SOURCE",
        material_key=component,
    )
    for source_x, source_y in iter_owner_cells(rows):
        points = (
            front_point(
                Fraction(source_x),
                Fraction(source_y),
                -COMMON_HALF_DEPTH,
            ),
            front_point(
                Fraction(source_x),
                Fraction(source_y + 1),
                -COMMON_HALF_DEPTH,
            ),
            front_point(
                Fraction(source_x + 1),
                Fraction(source_y + 1),
                -COMMON_HALF_DEPTH,
            ),
            front_point(
                Fraction(source_x + 1),
                Fraction(source_y),
                -COMMON_HALF_DEPTH,
            ),
        )
        record.face(points)
    return record


def build_axial_surface(
    name: str,
    component: str,
    source_owner: str,
    rows: list[dict[str, Any]],
    plane: str,
    world_z: Fraction,
) -> MeshRecord:
    record = MeshRecord(
        name=name,
        component=component,
        source_owner=source_owner,
        equation_id="EQ_AXIAL_OWNER_CELL_COMMON_BODY_LIMIT",
        occurrence="SOURCE",
        material_key=component,
    )
    source_y_min, source_y_max = axial_source_y_limits(plane)
    mapper = top_point if plane == "top" else bottom_point
    for source_x, source_y in iter_owner_cells(rows):
        clipped_y0 = max(Fraction(source_y), source_y_min)
        clipped_y1 = min(Fraction(source_y + 1), source_y_max)
        if clipped_y0 >= clipped_y1:
            continue
        points = (
            mapper(Fraction(source_x), clipped_y0, world_z),
            mapper(Fraction(source_x + 1), clipped_y0, world_z),
            mapper(Fraction(source_x + 1), clipped_y1, world_z),
            mapper(Fraction(source_x), clipped_y1, world_z),
        )
        record.face(points if plane == "top" else tuple(reversed(points)))
    return record


def build_c04_face(
    variant: str, rows: list[dict[str, Any]]
) -> MeshRecord:
    treatment = "RUNE" if variant == "rune_side" else "METAL_CENTER_PIECE"
    source_owner = (
        "OWN_RIGHT_C04_RUNE"
        if variant == "rune_side"
        else "OWN_RIGHT_C04_METAL"
    )
    equation_id = (
        "EQ_C04_RUNE_LOCAL_HALF"
        if variant == "rune_side"
        else "EQ_C04_METAL_LOCAL_HALF"
    )
    record = MeshRecord(
        name=f"SURF_C04_{treatment}_LOCAL_HALF",
        component="C04_LOCAL_TREATMENT",
        source_owner=source_owner,
        equation_id=equation_id,
        occurrence="SOURCE_LOCAL_Y_MIRROR_COMPLETE",
        material_key="C04_LOCAL_TREATMENT",
        variant_local_c04=True,
        local_extent_audit_owner=True,
    )
    for source_x, source_y in iter_owner_cells(rows):
        points = (
            c04_point(
                variant, Fraction(source_x), Fraction(source_y)
            ),
            c04_point(
                variant, Fraction(source_x + 1), Fraction(source_y)
            ),
            c04_point(
                variant, Fraction(source_x + 1), Fraction(source_y + 1)
            ),
            c04_point(
                variant, Fraction(source_x), Fraction(source_y + 1)
            ),
        )
        normal = cross(
            vector_sub(points[1], points[0]),
            vector_sub(points[2], points[0]),
        )
        ordered = points if normal[0] > 0 else tuple(reversed(points))
        record.face(ordered)
        mirrored = tuple((x, -y, z) for x, y, z in ordered)
        record.face(tuple(reversed(mirrored)))
    return record


def quantized_fraction(value: float) -> Fraction:
    return Fraction(f"{value:.12f}")


def ring_points(
    radius: Fraction, world_z: Fraction
) -> list[tuple[Fraction, Fraction, Fraction]]:
    points = []
    for index in range(ANGULAR_DIVISIONS + 1):
        theta = -math.pi / 2 + math.pi * index / ANGULAR_DIVISIONS
        points.append(
            (
                quantized_fraction(float(radius) * math.cos(theta)),
                quantized_fraction(float(radius) * math.sin(theta)),
                world_z,
            )
        )
    return points


def normalized_profile_rows(
    rows: list[dict[str, Any]]
) -> list[dict[str, Any]]:
    result = []
    for row in rows:
        normalized = dict(row)
        normalized["source_y"] = int(row.get("source_y", row.get("y")))
        if "runs_half_open" not in normalized:
            normalized["runs_half_open"] = normalized["owner_runs_half_open"]
        result.append(normalized)
    return sorted(result, key=lambda item: item["source_y"])


def positive_radius_from_row(row: dict[str, Any]) -> Fraction:
    runs = row.get("owner_runs_half_open", row.get("runs_half_open"))
    if not runs:
        raise RuntimeError(f"Missing profile runs at row {row['source_y']}")
    edge = max(int(stop) for _, stop in runs)
    if edge <= int(FRONT_AXIS_X):
        raise RuntimeError(
            f"Profile has no positive-X owner edge at {row['source_y']}"
        )
    return Fraction(edge - int(FRONT_AXIS_X)) * FRONT_SCALE


def build_rotational_surface(
    name: str,
    component: str,
    source_owner: str,
    rows: list[dict[str, Any]],
    terminal_source_y: int,
) -> tuple[MeshRecord, dict[str, Any]]:
    rows = normalized_profile_rows(rows)
    expected_rows = list(range(rows[0]["source_y"], terminal_source_y))
    observed_rows = [row["source_y"] for row in rows]
    if observed_rows != expected_rows:
        raise RuntimeError(
            f"{component} source row sequence is not contiguous: "
            f"{observed_rows[:2]}..{observed_rows[-2:]}"
        )
    radii = [positive_radius_from_row(row) for row in rows]
    rings = [
        (
            row["source_y"],
            radius,
            (FRONT_Z_ORIGIN_Y - Fraction(row["source_y"]))
            * FRONT_SCALE,
        )
        for row, radius in zip(rows, radii)
    ]
    rings.append(
        (
            terminal_source_y,
            radii[-1],
            (FRONT_Z_ORIGIN_Y - Fraction(terminal_source_y))
            * FRONT_SCALE,
        )
    )
    record = MeshRecord(
        name=name,
        component=component,
        source_owner=source_owner,
        equation_id="EQ_FRONT_OWNER_EDGE_ROTATION_ABOUT_Z",
        occurrence="SOURCE",
        material_key=component,
        smooth=True,
    )
    ring_indices = [
        [record.vertex(point) for point in ring_points(radius, world_z)]
        for _, radius, world_z in rings
    ]
    for upper, lower in zip(ring_indices, ring_indices[1:]):
        for segment in range(ANGULAR_DIVISIONS):
            record.faces.append(
                (
                    upper[segment],
                    lower[segment],
                    lower[segment + 1],
                    upper[segment + 1],
                )
            )
    return record, {
        "component": component,
        "source_owner": source_owner,
        "source_rows_half_open": [rows[0]["source_y"], terminal_source_y],
        "row_count": len(rows),
        "ring_count": len(rings),
        "angular_divisions_positive_x": ANGULAR_DIVISIONS,
        "first_radius_exact": qstr(radii[0]),
        "last_radius_exact": qstr(radii[-1]),
        "top_world_z_exact": qstr(rings[0][2]),
        "bottom_world_z_exact": qstr(rings[-1][2]),
    }


def build_half_annular_shoulder(
    name: str,
    component: str,
    source_owner: str,
    world_z: Fraction,
    upper_radius: Fraction,
    lower_radius: Fraction,
) -> MeshRecord:
    record = MeshRecord(
        name=name,
        component=component,
        source_owner=source_owner,
        equation_id="EQ_EXACT_PLANAR_HALF_ANNULAR_SHOULDER",
        occurrence="SOURCE",
        material_key="CONTACT",
    )
    upper = ring_points(upper_radius, world_z)
    lower = ring_points(lower_radius, world_z)
    for segment in range(ANGULAR_DIVISIONS):
        points = (
            upper[segment],
            upper[segment + 1],
            lower[segment + 1],
            lower[segment],
        )
        record.face(
            points if lower_radius > upper_radius else tuple(reversed(points))
        )
    return record


def build_half_cap(
    name: str,
    component: str,
    source_owner: str,
    world_z: Fraction,
    radius: Fraction,
    positive_z: bool,
) -> MeshRecord:
    record = MeshRecord(
        name=name,
        component=component,
        source_owner=source_owner,
        equation_id="EQ_EXACT_SOURCE_RADIUS_TERMINAL_HALF_CAP",
        occurrence="SOURCE",
        material_key="CONTACT",
    )
    center = (Fraction(0), Fraction(0), world_z)
    ring = ring_points(radius, world_z)
    for segment in range(ANGULAR_DIVISIONS):
        points = (center, ring[segment], ring[segment + 1])
        record.face(points if positive_z else tuple(reversed(points)))
    return record


@dataclass(frozen=True)
class ChainPoint:
    source_x: Fraction
    source_y: Fraction
    world: tuple[Fraction, Fraction, Fraction]


def reverse_chain(chain: list[ChainPoint]) -> list[ChainPoint]:
    return list(reversed(chain))


def rz180_chain(chain: list[ChainPoint]) -> list[ChainPoint]:
    return [
        ChainPoint(
            point.source_x,
            point.source_y,
            (-point.world[0], -point.world[1], point.world[2]),
        )
        for point in chain
    ]


def connector(a: ChainPoint, b: ChainPoint) -> list[ChainPoint]:
    return [a, b]


def boundary_owner_key(boundary_id: str) -> str:
    if "_C02_" in boundary_id:
        return "c02_owner_edge_x"
    if "_C03_" in boundary_id:
        return "c03_owner_edge_x"
    raise KeyError(boundary_id)


def step_boundary_source_points(
    boundary_id: str, record: dict[str, Any]
) -> list[tuple[Fraction, Fraction]]:
    owner_key = boundary_owner_key(boundary_id)
    samples = sorted(record["samples"], key=lambda sample: int(sample["y"]))
    points: list[tuple[Fraction, Fraction]] = []
    for sample in samples:
        point = (
            Fraction(int(sample[owner_key])),
            Fraction(int(sample["y"])),
        )
        if not points or points[-1] != point:
            points.append(point)
        endpoint = (point[0], point[1] + 1)
        if points[-1] != endpoint:
            points.append(endpoint)
    return points


def clip_source_polyline_y(
    points: list[tuple[Fraction, Fraction]],
    minimum_y: Fraction,
    maximum_y: Fraction,
) -> list[tuple[Fraction, Fraction]]:
    result: list[tuple[Fraction, Fraction]] = []
    for a, b in zip(points, points[1:]):
        ax, ay = a
        bx, by = b
        dy = by - ay
        if dy == 0:
            if not minimum_y <= ay <= maximum_y:
                continue
            clipped_a, clipped_b = a, b
        else:
            if max(ay, by) < minimum_y or min(ay, by) > maximum_y:
                continue
            crossings = sorted(
                (
                    (minimum_y - ay) / dy,
                    (maximum_y - ay) / dy,
                )
            )
            t0 = max(Fraction(0), crossings[0])
            t1 = min(Fraction(1), crossings[1])
            if t0 > t1:
                continue
            clipped_a = (ax + t0 * (bx - ax), ay + t0 * dy)
            clipped_b = (ax + t1 * (bx - ax), ay + t1 * dy)
        if not result or result[-1] != clipped_a:
            result.append(clipped_a)
        if result[-1] != clipped_b:
            result.append(clipped_b)
    if len(result) < 2:
        raise RuntimeError("Source boundary clip produced fewer than two points")
    return result


def boundary_chain(
    boundary_id: str,
    boundaries: dict[str, Any],
    plane: str,
    world_z: Fraction | None = None,
    logical_source_id: str | None = None,
) -> list[ChainPoint]:
    source_id = logical_source_id or boundary_id
    source_points = step_boundary_source_points(
        source_id, boundaries["boundaries"][source_id]
    )
    if plane in {"top", "bottom"}:
        source_points = clip_source_polyline_y(
            source_points, *axial_source_y_limits(plane)
        )
    if plane == "front":
        mapper = lambda x, y: front_point(x, y, -COMMON_HALF_DEPTH)
    elif plane == "top":
        if world_z is None:
            raise ValueError("Top boundary requires world Z")
        mapper = lambda x, y: top_point(x, y, world_z)
    elif plane == "bottom":
        if world_z is None:
            raise ValueError("Bottom boundary requires world Z")
        mapper = lambda x, y: bottom_point(x, y, world_z)
    else:
        raise ValueError(plane)
    return [ChainPoint(x, y, mapper(x, y)) for x, y in source_points]


PARAMETER_DODECAGON = [
    (Fraction(0), Fraction(6)),
    (Fraction(0), Fraction(3)),
    (Fraction(1), Fraction(1)),
    (Fraction(3), Fraction(0)),
    (Fraction(6), Fraction(0)),
    (Fraction(8), Fraction(1)),
    (Fraction(9), Fraction(3)),
    (Fraction(9), Fraction(6)),
    (Fraction(8), Fraction(8)),
    (Fraction(6), Fraction(9)),
    (Fraction(3), Fraction(9)),
    (Fraction(1), Fraction(8)),
]


def chain_parameters(chain: list[ChainPoint]) -> list[Fraction]:
    cumulative = [Fraction(0)]
    for a, b in zip(chain, chain[1:]):
        length = abs(b.source_x - a.source_x) + abs(
            b.source_y - a.source_y
        )
        if length == 0:
            length = sum(
                (b.world[axis] - a.world[axis]) ** 2 for axis in range(3)
            )
        cumulative.append(cumulative[-1] + length)
    total = cumulative[-1]
    if total == 0:
        return [
            Fraction(index, max(1, len(chain) - 1))
            for index in range(len(chain))
        ]
    return [value / total for value in cumulative]


def parameterized_perimeter(
    members: list[list[ChainPoint]],
) -> tuple[
    list[tuple[Fraction, Fraction, Fraction]],
    list[tuple[Fraction, Fraction]],
]:
    if len(members) != 12:
        raise RuntimeError(
            f"Expected 12 exact boundary members, got {len(members)}"
        )
    world_points: list[tuple[Fraction, Fraction, Fraction]] = []
    parameter_points: list[tuple[Fraction, Fraction]] = []
    for index, member in enumerate(members):
        start = PARAMETER_DODECAGON[index]
        stop = PARAMETER_DODECAGON[(index + 1) % 12]
        for point, t in zip(member, chain_parameters(member)):
            parameter = (
                start[0] + t * (stop[0] - start[0]),
                start[1] + t * (stop[1] - start[1]),
            )
            if (
                world_points
                and world_points[-1] == point.world
                and parameter_points[-1] == parameter
            ):
                continue
            world_points.append(point.world)
            parameter_points.append(parameter)
    if (
        world_points[0] == world_points[-1]
        and parameter_points[0] == parameter_points[-1]
    ):
        world_points.pop()
        parameter_points.pop()
    return world_points, parameter_points


def cross2(
    a: tuple[Fraction, Fraction],
    b: tuple[Fraction, Fraction],
    c: tuple[Fraction, Fraction],
) -> Fraction:
    return (b[0] - a[0]) * (c[1] - a[1]) - (
        b[1] - a[1]
    ) * (c[0] - a[0])


def point_in_triangle_strict(
    point: tuple[Fraction, Fraction],
    a: tuple[Fraction, Fraction],
    b: tuple[Fraction, Fraction],
    c: tuple[Fraction, Fraction],
) -> bool:
    return (
        cross2(a, b, point) > 0
        and cross2(b, c, point) > 0
        and cross2(c, a, point) > 0
    )


def squared_distance(
    a: tuple[Fraction, Fraction, Fraction],
    b: tuple[Fraction, Fraction, Fraction],
) -> Fraction:
    return sum((a[axis] - b[axis]) ** 2 for axis in range(3))


def ear_clip(
    world_points: list[tuple[Fraction, Fraction, Fraction]],
    parameter_points: list[tuple[Fraction, Fraction]],
) -> list[tuple[int, int, int]]:
    if len(world_points) != len(parameter_points) or len(world_points) < 3:
        raise RuntimeError("Invalid exact boundary-stitch perimeter")
    active = list(range(len(world_points)))
    triangles: list[tuple[int, int, int]] = []
    while len(active) > 3:
        candidates = []
        for position, current in enumerate(active):
            previous = active[position - 1]
            following = active[(position + 1) % len(active)]
            if (
                cross2(
                    parameter_points[previous],
                    parameter_points[current],
                    parameter_points[following],
                )
                <= 0
            ):
                continue
            world_normal = cross(
                vector_sub(world_points[current], world_points[previous]),
                vector_sub(world_points[following], world_points[previous]),
            )
            if world_normal == (0, 0, 0):
                continue
            candidates.append(
                (
                    squared_distance(
                        world_points[previous], world_points[following]
                    ),
                    current,
                    position,
                    previous,
                    following,
                )
            )
        candidates.sort(key=lambda item: (item[0], item[1]))
        selected = None
        for _, _, position, previous, following in candidates:
            current = active[position]
            contains = any(
                other not in {previous, current, following}
                and point_in_triangle_strict(
                    parameter_points[other],
                    parameter_points[previous],
                    parameter_points[current],
                    parameter_points[following],
                )
                for other in active
            )
            if not contains:
                selected = (position, previous, current, following)
                break
        if selected is None:
            raise RuntimeError(
                "Deterministic exact boundary stitch found no eligible ear"
            )
        position, previous, current, following = selected
        triangles.append((previous, current, following))
        active.pop(position)
    final = tuple(active)
    final_normal = cross(
        vector_sub(world_points[final[1]], world_points[final[0]]),
        vector_sub(world_points[final[2]], world_points[final[0]]),
    )
    if final_normal == (0, 0, 0):
        raise RuntimeError("Boundary stitch ended on a zero-area triangle")
    triangles.append(final)
    return triangles


def oriented_x_face(
    points: Sequence[tuple[Fraction, Fraction, Fraction]],
    target_sign: int,
) -> tuple[tuple[Fraction, Fraction, Fraction], ...]:
    normal = cross(
        vector_sub(points[1], points[0]),
        vector_sub(points[2], points[0]),
    )
    return (
        tuple(reversed(points))
        if normal[0] * target_sign < 0
        else tuple(points)
    )


def build_stone_inner_closures(
    boundaries: dict[str, Any],
    stone_top_z: Fraction,
    stone_bottom_z: Fraction,
) -> tuple[list[MeshRecord], dict[str, Any]]:
    front_c02 = boundary_chain(
        "FRONT_C02_INNER_OWNER_EDGE", boundaries, "front"
    )
    front_c03 = boundary_chain(
        "FRONT_C03_INNER_OWNER_EDGE", boundaries, "front"
    )
    top_c02 = boundary_chain(
        "TOP_C02_INNER_OWNER_EDGE",
        boundaries,
        "top",
        world_z=stone_top_z,
    )
    top_c03 = boundary_chain(
        "TOP_C03_INNER_OWNER_EDGE",
        boundaries,
        "top",
        world_z=stone_top_z,
    )
    bottom_c02 = boundary_chain(
        "BOTTOM_C02_INNER_OWNER_EDGE",
        boundaries,
        "bottom",
        world_z=stone_bottom_z,
        logical_source_id="BOTTOM_C03_INNER_OWNER_EDGE",
    )
    bottom_c03 = boundary_chain(
        "BOTTOM_C03_INNER_OWNER_EDGE",
        boundaries,
        "bottom",
        world_z=stone_bottom_z,
        logical_source_id="BOTTOM_C02_INNER_OWNER_EDGE",
    )
    bottom_c02_fc = reverse_chain(bottom_c02)
    bottom_c03_fc = reverse_chain(bottom_c03)
    members = [
        front_c02,
        connector(front_c02[-1], bottom_c02_fc[0]),
        bottom_c02_fc,
        connector(bottom_c02_fc[-1], rz180_chain(bottom_c03_fc)[-1]),
        reverse_chain(rz180_chain(bottom_c03_fc)),
        connector(
            reverse_chain(rz180_chain(bottom_c03_fc))[-1],
            reverse_chain(rz180_chain(front_c03))[0],
        ),
        reverse_chain(rz180_chain(front_c03)),
        connector(
            reverse_chain(rz180_chain(front_c03))[-1],
            rz180_chain(top_c03)[0],
        ),
        rz180_chain(top_c03),
        connector(rz180_chain(top_c03)[-1], top_c02[-1]),
        reverse_chain(top_c02),
        connector(reverse_chain(top_c02)[-1], front_c02[0]),
    ]
    world_points, parameter_points = parameterized_perimeter(members)
    triangles = ear_clip(world_points, parameter_points)
    c02 = MeshRecord(
        name="CLOSURE_C02_INNER_EXACT_BOUNDARIES",
        component="C02_STONE_LEFT",
        source_owner=(
            "FRONT/TOP/BOTTOM_C02_C03_INNER_OWNER_EDGE_SETS"
        ),
        equation_id="EQ_RULED_EXACT_BOUNDARY_CLOSURE",
        occurrence="COMPLETED_AFTER_ONE_RZ180",
        material_key="CLOSURE",
    )
    for triangle in triangles:
        points = [world_points[index] for index in triangle]
        c02.face(oriented_x_face(points, 1))
    c03 = c02.rz180("__COMPLETED_PAIR")
    c03.name = "CLOSURE_C03_INNER_EXACT_BOUNDARIES"
    c03.component = "C03_STONE_RIGHT"
    c03.occurrence = "COMPLETED_AFTER_ONE_RZ180"
    c03.faces = [
        tuple(reversed(face)) for face in c03.faces
    ]
    return [c02, c03], {
        "equation_id": "EQ_RULED_EXACT_BOUNDARY_CLOSURE",
        "perimeter_vertices": len(world_points),
        "triangles_per_side": len(triangles),
        "tolerance_weld_used": False,
        "steiner_vertices_used": False,
    }


def edge_source_points_from_rows(
    rows: list[dict[str, Any]], choose: str
) -> list[tuple[Fraction, Fraction]]:
    samples = []
    for row in rows:
        source_y = int(row.get("y", row.get("source_y")))
        runs = row.get("owner_runs_half_open", row.get("runs_half_open"))
        if not runs:
            continue
        if choose == "minimum":
            source_x = min(int(start) for start, _ in runs)
        elif choose == "maximum":
            source_x = max(int(stop) for _, stop in runs)
        else:
            raise ValueError(choose)
        samples.append((source_x, source_y))
    samples.sort(key=lambda item: item[1])
    points: list[tuple[Fraction, Fraction]] = []
    for source_x_int, source_y_int in samples:
        point = (Fraction(source_x_int), Fraction(source_y_int))
        if not points or points[-1] != point:
            points.append(point)
        endpoint = (point[0], point[1] + 1)
        if points[-1] != endpoint:
            points.append(endpoint)
    return points


def derived_edge_chain(
    rows: list[dict[str, Any]],
    plane: str,
    world_side: str,
    world_z: Fraction | None = None,
) -> list[ChainPoint]:
    if plane in {"front", "top"}:
        choose = "maximum" if world_side == "positive" else "minimum"
    elif plane == "bottom":
        choose = "minimum" if world_side == "positive" else "maximum"
    else:
        raise ValueError(plane)
    source_points = edge_source_points_from_rows(rows, choose)
    if plane in {"top", "bottom"}:
        source_points = clip_source_polyline_y(
            source_points, *axial_source_y_limits(plane)
        )
    if plane == "front":
        mapper = lambda x, y: front_point(x, y, -COMMON_HALF_DEPTH)
    elif plane == "top":
        if world_z is None:
            raise ValueError("Top edge chain requires world Z")
        mapper = lambda x, y: top_point(x, y, world_z)
    else:
        if world_z is None:
            raise ValueError("Bottom edge chain requires world Z")
        mapper = lambda x, y: bottom_point(x, y, world_z)
    return [ChainPoint(x, y, mapper(x, y)) for x, y in source_points]


def completed_positive_stone_outer_loop(
    scanlines: dict[str, Any],
    stone_top_z: Fraction,
    stone_bottom_z: Fraction,
) -> list[tuple[Fraction, Fraction, Fraction]]:
    front_c03 = derived_edge_chain(
        owner_rows(scanlines, "front", "C03_STONE_RIGHT"),
        "front",
        "positive",
    )
    front_c02 = derived_edge_chain(
        owner_rows(scanlines, "front", "C02_STONE_LEFT"),
        "front",
        "negative",
    )
    top_c03 = derived_edge_chain(
        owner_rows(scanlines, "top", "C03_STONE_RIGHT"),
        "top",
        "positive",
        stone_top_z,
    )
    top_c02 = derived_edge_chain(
        owner_rows(scanlines, "top", "C02_STONE_LEFT"),
        "top",
        "negative",
        stone_top_z,
    )
    bottom_c03 = derived_edge_chain(
        owner_rows(scanlines, "bottom", "C02_STONE_LEFT"),
        "bottom",
        "positive",
        stone_bottom_z,
    )
    bottom_c02 = derived_edge_chain(
        owner_rows(scanlines, "bottom", "C03_STONE_RIGHT"),
        "bottom",
        "negative",
        stone_bottom_z,
    )
    bottom_c03_fc = reverse_chain(bottom_c03)
    bottom_c02_fc = reverse_chain(bottom_c02)
    members = [
        front_c03,
        connector(front_c03[-1], bottom_c03_fc[0]),
        bottom_c03_fc,
        connector(bottom_c03_fc[-1], rz180_chain(bottom_c02_fc)[-1]),
        reverse_chain(rz180_chain(bottom_c02_fc)),
        connector(
            reverse_chain(rz180_chain(bottom_c02_fc))[-1],
            reverse_chain(rz180_chain(front_c02))[0],
        ),
        reverse_chain(rz180_chain(front_c02)),
        connector(
            reverse_chain(rz180_chain(front_c02))[-1],
            rz180_chain(top_c02)[0],
        ),
        rz180_chain(top_c02),
        connector(rz180_chain(top_c02)[-1], top_c03[-1]),
        reverse_chain(top_c03),
        connector(reverse_chain(top_c03)[-1], front_c03[0]),
    ]
    world, _ = parameterized_perimeter(members)
    return world


def c04_outer_loop(
    variant: str, rows: list[dict[str, Any]]
) -> list[tuple[Fraction, Fraction, Fraction]]:
    choose = "maximum" if variant == "rune_side" else "minimum"
    source = edge_source_points_from_rows(rows, choose)
    half_chain = [
        ChainPoint(x, y, c04_point(variant, x, y)) for x, y in source
    ]
    mirrored = [
        ChainPoint(
            point.source_x,
            point.source_y,
            (point.world[0], -point.world[1], point.world[2]),
        )
        for point in half_chain
    ]
    members = [
        half_chain,
        connector(half_chain[-1], mirrored[-1]),
        reverse_chain(mirrored),
        connector(mirrored[0], half_chain[0]),
    ]
    result = []
    for member in members:
        for point in member:
            if not result or result[-1] != point.world:
                result.append(point.world)
    if result[0] == result[-1]:
        result.pop()
    return result


def loop_breakpoints(
    points: list[tuple[Fraction, Fraction, Fraction]]
) -> list[Fraction]:
    lengths = [Fraction(0)]
    wrapped = points + [points[0]]
    for a, b in zip(wrapped, wrapped[1:]):
        length = sum(abs(b[axis] - a[axis]) for axis in range(3))
        if length:
            lengths.append(lengths[-1] + length)
    if lengths[-1] == 0:
        raise RuntimeError("Zero-length exact closure loop")
    return [value / lengths[-1] for value in lengths]


def evaluate_closed_loop(
    points: list[tuple[Fraction, Fraction, Fraction]],
    breakpoints: list[Fraction],
    parameter: Fraction,
) -> tuple[Fraction, Fraction, Fraction]:
    parameter %= 1
    wrapped = points + [points[0]]
    for index, (start, stop) in enumerate(
        zip(breakpoints, breakpoints[1:])
    ):
        if start <= parameter <= stop:
            if stop == start:
                return wrapped[index]
            t = (parameter - start) / (stop - start)
            return tuple(
                wrapped[index][axis]
                + t * (wrapped[index + 1][axis] - wrapped[index][axis])
                for axis in range(3)
            )  # type: ignore[return-value]
    return points[0]


def build_c04_outer_closures(
    variant: str,
    scanlines: dict[str, Any],
    stone_top_z: Fraction,
    stone_bottom_z: Fraction,
) -> tuple[list[MeshRecord], dict[str, Any]]:
    stone_loop = completed_positive_stone_outer_loop(
        scanlines, stone_top_z, stone_bottom_z
    )
    owner_name = (
        "C04_RUNE_SIDE"
        if variant == "rune_side"
        else "C04_METAL_CENTER_PIECE_SIDE"
    )
    face_loop = c04_outer_loop(
        variant, owner_rows(scanlines, "right", owner_name)
    )
    stone_breaks = loop_breakpoints(stone_loop)
    face_breaks = loop_breakpoints(face_loop)
    parameters = sorted(set(stone_breaks + face_breaks))
    if parameters[-1] != 1:
        parameters.append(Fraction(1))
    label = "RUNE" if variant == "rune_side" else "METAL"
    positive = MeshRecord(
        name=f"CLOSURE_C04_{label}_TO_SHARED_STONE_POSITIVE_X",
        component="C04_LOCAL_TREATMENT",
        source_owner=(
            f"{owner_name}+FRONT/TOP/BOTTOM_C02_C03_OUTER_OWNER_EDGES"
        ),
        equation_id="EQ_RULED_C04_TO_SHARED_BODY_BOUNDARIES",
        occurrence="COMPLETED_AFTER_ONE_RZ180",
        material_key="CLOSURE",
        variant_local_c04=True,
    )
    for start, stop in zip(parameters, parameters[1:]):
        points = [
            evaluate_closed_loop(stone_loop, stone_breaks, start),
            evaluate_closed_loop(stone_loop, stone_breaks, stop),
            evaluate_closed_loop(face_loop, face_breaks, stop),
            evaluate_closed_loop(face_loop, face_breaks, start),
        ]
        deduped: list[tuple[Fraction, Fraction, Fraction]] = []
        for point in points:
            if not deduped or deduped[-1] != point:
                deduped.append(point)
        if len(deduped) > 1 and deduped[0] == deduped[-1]:
            deduped.pop()
        if len(deduped) < 3 or polygon_normal(deduped) == (0, 0, 0):
            continue
        positive.face(
            deduped
            if polygon_normal(deduped)[0] > 0
            else tuple(reversed(deduped))
        )
    negative = positive.rz180("__RZ180")
    return [positive, negative], {
        "equation_id": "EQ_RULED_C04_TO_SHARED_BODY_BOUNDARIES",
        "stone_loop_vertices": len(stone_loop),
        "c04_loop_vertices": len(face_loop),
        "shared_parameter_breakpoints": len(parameters),
        "ruled_faces_per_side": len(positive.faces),
        "variant_local_c04": True,
    }


ROTATIONAL_INTERVALS = {
    "C06_UPPER_HAFT_CAP": (600, 670),
    "C07_HAFT": (670, 870),
    "C07B_HAFT_TO_HANDLE_FERRULE": (870, 955),
    "C08_GRIP": (955, 1110),
    "C09_LOWER_COLLAR": (1110, 1150),
    "C10_POMMEL_BODY": (1150, 1220),
    "C11_POMMEL_TERMINAL_CAP": (1220, 1271),
    "C12_UPPER_HEAD_CAP_SPIRE": (208, 295),
}


def source_rows_for_rotational_component(
    component: str,
    scanlines: dict[str, Any],
    step06_front: dict[str, Any],
) -> tuple[list[dict[str, Any]], int, str]:
    start, stop = ROTATIONAL_INTERVALS[component]
    if component == "C06_UPPER_HAFT_CAP":
        return (
            owner_rows(scanlines, "front", component),
            stop,
            "OWN_FRONT_C06",
        )
    if component == "C12_UPPER_HEAD_CAP_SPIRE":
        early = [
            row
            for row in step06_front["row_profiles"]
            if start <= int(row["source_y"]) < 221
        ]
        reserved = owner_rows(
            scanlines, "front", "C12_RESERVED_EXISTING_OWNER"
        )
        return early + reserved, stop, "OWN_FRONT_C12_FULL"
    rows = [
        row
        for row in step06_front["row_profiles"]
        if start <= int(row["source_y"]) < stop
    ]
    owner = {
        "C07_HAFT": "OWN_FRONT_C07",
        "C07B_HAFT_TO_HANDLE_FERRULE": "OWN_FRONT_C07B",
        "C08_GRIP": "OWN_FRONT_C08",
        "C09_LOWER_COLLAR": "OWN_FRONT_C09",
        "C10_POMMEL_BODY": "OWN_FRONT_C10",
        "C11_POMMEL_TERMINAL_CAP": "OWN_FRONT_C11",
    }[component]
    return rows, stop, owner


def build_shared_base_records(
    scanlines: dict[str, Any],
    boundaries: dict[str, Any],
    step06_front: dict[str, Any],
) -> tuple[list[MeshRecord], dict[str, Any]]:
    stone_top_z = (FRONT_Z_ORIGIN_Y - Fraction(221)) * FRONT_SCALE
    stone_bottom_z = (FRONT_Z_ORIGIN_Y - Fraction(600)) * FRONT_SCALE
    source_records: list[MeshRecord] = []
    provenance: list[dict[str, Any]] = []

    for name, component, owner in (
        ("SURF_C01_FRONT", "C01_CENTER_CORE", "C01_CENTER_CORE"),
        ("SURF_C02_FRONT", "C02_STONE_LEFT", "C02_STONE_LEFT"),
        ("SURF_C03_FRONT", "C03_STONE_RIGHT", "C03_STONE_RIGHT"),
    ):
        record = build_front_surface(
            name,
            component,
            f"OWN_FRONT_{component.split('_')[0]}",
            owner_rows(scanlines, "front", owner),
        )
        source_records.append(record)
        provenance.append(
            {
                "record": record.name,
                "source_owner": record.source_owner,
                "equation_id": record.equation_id,
                "faces": len(record.faces),
            }
        )

    axial_specs = (
        (
            "SURF_C02_TOP_HALF",
            "C02_STONE_LEFT",
            "OWN_TOP_C02",
            "top",
            "C02_STONE_LEFT",
            stone_top_z,
        ),
        (
            "SURF_C03_TOP_HALF",
            "C03_STONE_RIGHT",
            "OWN_TOP_C03",
            "top",
            "C03_STONE_RIGHT",
            stone_top_z,
        ),
        (
            "SURF_C02_BOTTOM_HALF",
            "C02_STONE_LEFT",
            "OWN_BOTTOM_C02_LOGICAL",
            "bottom",
            "C03_STONE_RIGHT",
            stone_bottom_z,
        ),
        (
            "SURF_C03_BOTTOM_HALF",
            "C03_STONE_RIGHT",
            "OWN_BOTTOM_C03_LOGICAL",
            "bottom",
            "C02_STONE_LEFT",
            stone_bottom_z,
        ),
    )
    for name, component, owner, plane, stored_owner, world_z in axial_specs:
        record = build_axial_surface(
            name,
            component,
            owner,
            owner_rows(scanlines, plane, stored_owner),
            plane,
            world_z,
        )
        source_records.append(record)
        provenance.append(
            {
                "record": record.name,
                "source_owner": record.source_owner,
                "stored_owner": stored_owner,
                "equation_id": record.equation_id,
                "faces": len(record.faces),
            }
        )

    profile_records: dict[str, MeshRecord] = {}
    profile_rows: dict[str, list[dict[str, Any]]] = {}
    profile_metadata: dict[str, Any] = {}
    for component in ROTATIONAL_INTERVALS:
        rows, terminal, source_owner = source_rows_for_rotational_component(
            component, scanlines, step06_front
        )
        record, metadata = build_rotational_surface(
            f"SURF_{component}_ROTATIONAL_HALF",
            component,
            source_owner,
            rows,
            terminal,
        )
        source_records.append(record)
        profile_records[component] = record
        profile_rows[component] = normalized_profile_rows(rows)
        profile_metadata[component] = metadata
        provenance.append(
            {
                "record": record.name,
                "source_owner": source_owner,
                "equation_id": record.equation_id,
                "faces": len(record.faces),
            }
        )

    component_contact_rows = {
        "C01_CENTER_CORE": normalized_profile_rows(
            owner_rows(scanlines, "front", "C01_CENTER_CORE")
        ),
        **profile_rows,
    }
    transitions = (
        ("C12_UPPER_HEAD_CAP_SPIRE", "C01_CENTER_CORE", 295),
        ("C01_CENTER_CORE", "C06_UPPER_HAFT_CAP", 600),
        ("C06_UPPER_HAFT_CAP", "C07_HAFT", 670),
        ("C07_HAFT", "C07B_HAFT_TO_HANDLE_FERRULE", 870),
        ("C07B_HAFT_TO_HANDLE_FERRULE", "C08_GRIP", 955),
        ("C08_GRIP", "C09_LOWER_COLLAR", 1110),
        ("C09_LOWER_COLLAR", "C10_POMMEL_BODY", 1150),
        ("C10_POMMEL_BODY", "C11_POMMEL_TERMINAL_CAP", 1220),
    )
    transition_report = []
    for upper_component, lower_component, source_edge_y in transitions:
        upper_row = component_contact_rows[upper_component][-1]
        lower_row = component_contact_rows[lower_component][0]
        if upper_row["source_y"] != source_edge_y - 1:
            raise RuntimeError(
                f"Upper contact row mismatch for {upper_component}"
            )
        if lower_row["source_y"] != source_edge_y:
            raise RuntimeError(
                f"Lower contact row mismatch for {lower_component}"
            )
        upper_radius = positive_radius_from_row(upper_row)
        lower_radius = positive_radius_from_row(lower_row)
        world_z = (FRONT_Z_ORIGIN_Y - source_edge_y) * FRONT_SCALE
        report = {
            "upper_component": upper_component,
            "lower_component": lower_component,
            "source_edge_y": source_edge_y,
            "world_z_exact": qstr(world_z),
            "upper_radius_exact": qstr(upper_radius),
            "lower_radius_exact": qstr(lower_radius),
        }
        if upper_radius == lower_radius:
            report.update(
                {
                    "method": "coordinate_equal_common_half_ring",
                    "faces": 0,
                }
            )
        else:
            name = f"CONTACT_{upper_component}_TO_{lower_component}"
            shoulder = build_half_annular_shoulder(
                name,
                f"{upper_component}_{lower_component}",
                f"{upper_component}:row={source_edge_y-1};"
                f"{lower_component}:row={source_edge_y}",
                world_z,
                upper_radius,
                lower_radius,
            )
            source_records.append(shoulder)
            provenance.append(
                {
                    "record": shoulder.name,
                    "source_owner": shoulder.source_owner,
                    "equation_id": shoulder.equation_id,
                    "faces": len(shoulder.faces),
                }
            )
            report.update(
                {
                    "method": "exact_source_radii_half_annular_shoulder",
                    "faces": len(shoulder.faces),
                }
            )
        transition_report.append(report)

    c11_rows = profile_rows["C11_POMMEL_TERMINAL_CAP"]
    c12_rows = profile_rows["C12_UPPER_HEAD_CAP_SPIRE"]
    bottom_cap = build_half_cap(
        "CAP_C11_BOTTOM",
        "C11_POMMEL_TERMINAL_CAP",
        "OWN_FRONT_C11:row=1270",
        Fraction(0),
        positive_radius_from_row(c11_rows[-1]),
        False,
    )
    top_cap = build_half_cap(
        "CAP_C12_TOP",
        "C12_UPPER_HEAD_CAP_SPIRE",
        "OWN_FRONT_C12_FULL:row=208",
        Fraction(170),
        positive_radius_from_row(c12_rows[0]),
        True,
    )
    source_records.extend((bottom_cap, top_cap))
    for record in (bottom_cap, top_cap):
        provenance.append(
            {
                "record": record.name,
                "source_owner": record.source_owner,
                "equation_id": record.equation_id,
                "faces": len(record.faces),
            }
        )

    completed = list(source_records)
    completed.extend(record.rz180() for record in source_records)
    inner_closures, inner_metadata = build_stone_inner_closures(
        boundaries, stone_top_z, stone_bottom_z
    )
    completed.extend(inner_closures)
    provenance.extend(
        {
            "record": record.name,
            "source_owner": record.source_owner,
            "equation_id": record.equation_id,
            "faces": len(record.faces),
        }
        for record in inner_closures
    )
    return completed, {
        "stone_top_z_exact": qstr(stone_top_z),
        "stone_bottom_z_exact": qstr(stone_bottom_z),
        "source_records_before_whole_asset_rz180": len(source_records),
        "whole_asset_rz180_count": 1,
        "completed_shared_record_count": len(completed),
        "profile_metadata": profile_metadata,
        "transition_report": transition_report,
        "inner_closure_metadata": inner_metadata,
        "surface_provenance": provenance,
    }


def build_variant_records(
    variant: str,
    scanlines: dict[str, Any],
    stone_top_z: Fraction,
    stone_bottom_z: Fraction,
) -> tuple[list[MeshRecord], dict[str, Any]]:
    owner_name = (
        "C04_RUNE_SIDE"
        if variant == "rune_side"
        else "C04_METAL_CENTER_PIECE_SIDE"
    )
    face = build_c04_face(
        variant, owner_rows(scanlines, "right", owner_name)
    )
    records = [face, face.rz180()]
    closures, closure_metadata = build_c04_outer_closures(
        variant, scanlines, stone_top_z, stone_bottom_z
    )
    records.extend(closures)
    expected_half = (
        Fraction(9435, 548)
        if variant == "rune_side"
        else Fraction(11815, 548)
    )
    interval = (
        (557, 668)
        if variant == "rune_side"
        else (418, 557)
    )
    domain_half = max(
        abs(Fraction(interval[0]) - RIGHT_AXIS_X),
        abs(Fraction(interval[1]) - RIGHT_AXIS_X),
    ) * RIGHT_SCALE
    if domain_half != expected_half:
        raise RuntimeError(
            f"{variant} approved local domain mismatch: "
            f"{domain_half} != {expected_half}"
        )
    extent_vertices = [
        point
        for record in records
        if record.local_extent_audit_owner
        for point in record.vertices
    ]
    visible_face_half = max(abs(point[1]) for point in extent_vertices)
    if visible_face_half > domain_half:
        raise RuntimeError(
            f"{variant} visible face exceeds its approved local domain: "
            f"{visible_face_half} > {domain_half}"
        )
    if any(
        abs(point[1]) > COMMON_HALF_DEPTH
        for record in records
        for point in record.vertices
    ):
        raise RuntimeError(f"{variant} exceeds the common depth envelope")
    return records, {
        "variant": variant,
        "owner_name": owner_name,
        "source_interval_half_open": list(interval),
        "local_domain_half_extent_expected_exact": qstr(expected_half),
        "local_domain_half_extent_observed_exact": qstr(domain_half),
        "visible_face_half_extent_observed_exact": qstr(visible_face_half),
        "visible_face_fills_entire_domain": visible_face_half == domain_half,
        "domain_is_registration_not_fill": True,
        "local_y_mirror_count": 1,
        "whole_asset_rz180_count": 1,
        "record_count": len(records),
        "closure_metadata": closure_metadata,
        "surface_provenance": [
            {
                "record": record.name,
                "source_owner": record.source_owner,
                "equation_id": record.equation_id,
                "faces": len(record.faces),
            }
            for record in records
        ],
    }


def validate_records(
    asset: dict[str, Any],
    shared_records: list[MeshRecord],
    variant_records: list[MeshRecord],
    shared_hash: str,
) -> dict[str, Any]:
    records = shared_records + variant_records
    bounds = combined_bounds(records)
    if tuple(bounds["_dimensions"]) != EXPECTED_BOUNDS:
        raise RuntimeError(
            f"{asset['asset_id']} exact bounds mismatch: "
            f"{bounds['dimensions_exact']}"
        )
    if any(
        not record.source_owner or not record.equation_id
        for record in records
    ):
        raise RuntimeError("Every surface must cite a source owner and equation")
    forbidden = "EQ_CANDIDATE_AXIAL_INTERSECTION"
    if any(
        forbidden in (
            record.name
            + record.source_owner
            + record.equation_id
            + record.occurrence
        )
        for record in records
    ):
        raise RuntimeError("Forbidden candidate axial intersection was found")
    if any(record.variant_local_c04 for record in shared_records):
        raise RuntimeError("Shared base contains local C04 geometry")
    return {
        "result": "PASS",
        "artifact_status": "candidate pending independent saved-file audit",
        "asset_id": asset["asset_id"],
        "variant": asset["variant"],
        "expected_dimensions_cm_exact": [
            qstr(value) for value in EXPECTED_BOUNDS
        ],
        "observed_bounds": {
            key: value for key, value in bounds.items() if not key.startswith("_")
        },
        "shared_base_canonical_sha256": shared_hash,
        "shared_record_count": len(shared_records),
        "variant_record_count": len(variant_records),
        "mesh_record_count": len(records),
        "vertices": sum(len(record.vertices) for record in records),
        "faces": sum(len(record.faces) for record in records),
        "triangles": sum(record.triangles for record in records),
        "surface_provenance_count": len(records),
        "surface_provenance_complete": True,
        "forbidden_equation_absent": True,
        "quarantined_geometry_read_count": 0,
        "whole_asset_rz180_count": 1,
        "local_y_mirror_count": 1,
    }


def clear_blender_scene(bpy: Any) -> None:
    bpy.ops.object.select_all(action="SELECT")
    bpy.ops.object.delete(use_global=False)
    for collection in (
        bpy.data.meshes,
        bpy.data.materials,
        bpy.data.cameras,
        bpy.data.lights,
    ):
        for datablock in list(collection):
            if datablock.users == 0:
                collection.remove(datablock)


def create_material(bpy: Any, key: str) -> Any:
    name = f"MAT_PROOF_{key}"
    material = bpy.data.materials.get(name)
    if material is None:
        material = bpy.data.materials.new(name)
        color = COMPONENT_COLORS.get(key, COMPONENT_COLORS["CLOSURE"])
        material.diffuse_color = color
        material["Aerathea.ProofOnly"] = True
        material["Aerathea.MaterialStatus"] = "proof only"
    return material


def create_blender_object(bpy: Any, record: MeshRecord) -> Any:
    mesh = bpy.data.meshes.new(f"{record.name}_MESH")
    mesh.from_pydata(
        [
            (float(point[0]), float(point[1]), float(point[2]))
            for point in record.vertices
        ],
        [],
        record.faces,
    )
    mesh.update(calc_edges=True)
    if record.smooth:
        for polygon in mesh.polygons:
            polygon.use_smooth = True
    obj = bpy.data.objects.new(record.name, mesh)
    bpy.context.scene.collection.objects.link(obj)
    obj.data.materials.append(create_material(bpy, record.material_key))
    obj["Aerathea.Component"] = record.component
    obj["Aerathea.SourceOwner"] = record.source_owner
    obj["Aerathea.EquationId"] = record.equation_id
    obj["Aerathea.Occurrence"] = record.occurrence
    obj["Aerathea.VariantLocalC04"] = record.variant_local_c04
    obj["Aerathea.LocalExtentAuditOwner"] = (
        record.local_extent_audit_owner
    )
    obj["Aerathea.ArtifactStatus"] = (
        "candidate pending independent saved-file audit"
    )
    return obj


def configure_scene(
    bpy: Any,
    asset: dict[str, Any],
    shared_hash: str,
    validation: dict[str, Any],
) -> None:
    scene = bpy.context.scene
    scene.unit_settings.system = "METRIC"
    scene.unit_settings.length_unit = "CENTIMETERS"
    scene.unit_settings.scale_length = 0.01
    scene["Aerathea.AssetId"] = asset["asset_id"]
    scene["Aerathea.DisplayName"] = asset["display_name"]
    scene["Aerathea.BuildId"] = BUILD_ID
    scene["Aerathea.RunId"] = RUN_ID
    scene["Aerathea.ArtifactStatus"] = (
        "candidate pending independent saved-file audit"
    )
    scene["Aerathea.LocalC04Treatment"] = asset["variant"]
    scene["Aerathea.CompletedFaceRule"] = (
        "double rune sided"
        if asset["variant"] == "rune_side"
        else "double metal-center-piece sided"
    )
    scene["Aerathea.SharedBaseCanonicalSha256"] = shared_hash
    scene["Aerathea.ExpectedWidthCmExact"] = qstr(EXPECTED_BOUNDS[0])
    scene["Aerathea.ExpectedDepthCmExact"] = qstr(EXPECTED_BOUNDS[1])
    scene["Aerathea.ExpectedHeightCmExact"] = qstr(EXPECTED_BOUNDS[2])
    scene["Aerathea.CommonHalfDepthCmExact"] = qstr(COMMON_HALF_DEPTH)
    if asset["variant"] == "rune_side":
        local_interval = (557, 668)
        local_domain_half = Fraction(9435, 548)
    else:
        local_interval = (418, 557)
        local_domain_half = Fraction(11815, 548)
    scene["Aerathea.LocalC04SourceIntervalHalfOpen"] = (
        f"[{local_interval[0]},{local_interval[1]})"
    )
    scene["Aerathea.LocalC04DomainHalfCmExact"] = qstr(local_domain_half)
    scene["Aerathea.LocalC04DomainIsRegistrationNotFill"] = True
    scene["Aerathea.WholeAssetRz180Count"] = 1
    scene["Aerathea.C04LocalYMirrorCount"] = 1
    scene["Aerathea.QuarantinedGeometryReadCount"] = 0
    scene["Aerathea.ForbiddenEquationAbsent"] = True
    scene["Aerathea.TrianglesObserved"] = validation["triangles"]


def write_json(path: Path, value: Any) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(
        json.dumps(value, indent=2, sort_keys=True) + "\n",
        encoding="utf-8",
    )


def internal_build_all() -> int:
    import bpy

    blueprint, authority_checks = verify_authority()
    scanlines = load_gzip_json(STEP09A_SCANLINES)
    boundaries = load_json(STEP09A_BOUNDARIES)
    step06_front = load_json(STEP06_FRONT)
    shared_records, shared_report = build_shared_base_records(
        scanlines, boundaries, step06_front
    )
    shared_hash = record_hash(shared_records)
    shared_bounds = combined_bounds(shared_records)
    if tuple(shared_bounds["_dimensions"]) != EXPECTED_BOUNDS:
        raise RuntimeError(
            "Canonical shared base does not own the exact common XYZ bounds: "
            f"{shared_bounds['dimensions_exact']}"
        )

    asset_results: dict[str, Any] = {}
    observed_exact_dimensions: dict[str, list[str]] = {}
    for asset_key, asset in ASSETS.items():
        output_root: Path = asset["output_root"]
        output_root.mkdir(parents=True, exist_ok=False)
        variant_records, variant_report = build_variant_records(
            asset["variant"],
            scanlines,
            Fraction(shared_report["stone_top_z_exact"]),
            Fraction(shared_report["stone_bottom_z_exact"]),
        )
        validation = validate_records(
            asset, shared_records, variant_records, shared_hash
        )
        clear_blender_scene(bpy)
        configure_scene(bpy, asset, shared_hash, validation)
        for record in shared_records:
            create_blender_object(bpy, record)
        for record in variant_records:
            create_blender_object(bpy, record)

        blend_path = (
            output_root
            / f"{asset['asset_id']}_DCCSource_SharedDepth_A01.blend"
        )
        bpy.ops.wm.save_as_mainfile(
            filepath=str(blend_path), check_existing=False
        )
        pre_save_path = output_root / "pre_save_validation.json"
        write_json(pre_save_path, validation)
        manifest = {
            "schema": "AERATHEA_FRESH_TWIN_DCC_SOURCE_A01_ASSET_V1",
            "date_utc": utc_now(),
            "run_id": RUN_ID,
            "build_id": BUILD_ID,
            "artifact_status": (
                "candidate pending independent saved-file audit"
            ),
            "asset_id": asset["asset_id"],
            "display_name": asset["display_name"],
            "local_c04_treatment": asset["variant"],
            "governing_blueprint": {
                "path": relative(BLUEPRINT),
                "sha256": EXPECTED_HASHES[BLUEPRINT],
                "effective_status": "authoritative",
            },
            "fresh_builder_approval": {
                "path": relative(BUILD_APPROVAL),
                "sha256": EXPECTED_HASHES[BUILD_APPROVAL],
                "status": "authoritative approval record",
            },
            "source_authority_checks": authority_checks,
            "input_geometry_files": [],
            "quarantined_geometry_read_count": 0,
            "shared_base": {
                "canonical_sha256": shared_hash,
                "record_count": len(shared_records),
                "bounds": {
                    key: value
                    for key, value in shared_bounds.items()
                    if not key.startswith("_")
                },
                "report": shared_report,
            },
            "variant_report": variant_report,
            "pre_save_validation": validation,
            "outputs": {
                "blend": {
                    "path": relative(blend_path),
                    "sha256": sha256(blend_path),
                },
                "pre_save_validation": {
                    "path": relative(pre_save_path),
                    "sha256": sha256(pre_save_path),
                },
            },
            "authority_boundary": {
                "dcc_source_candidate_after_independent_audit": True,
                "step_13": False,
                "retopology_uv_bake_export": False,
                "unreal": False,
            },
        }
        manifest_path = output_root / "build_manifest.json"
        write_json(manifest_path, manifest)
        asset_results[asset_key] = {
            "asset_id": asset["asset_id"],
            "variant": asset["variant"],
            "output_root": relative(output_root),
            "blend": {
                "path": relative(blend_path),
                "sha256": sha256(blend_path),
            },
            "manifest": {
                "path": relative(manifest_path),
                "sha256": sha256(manifest_path),
            },
            "pre_save_result": validation["result"],
            "shared_base_canonical_sha256": shared_hash,
            "observed_dimensions_cm_exact": validation[
                "observed_bounds"
            ]["dimensions_exact"],
        }
        observed_exact_dimensions[asset_key] = validation[
            "observed_bounds"
        ]["dimensions_exact"]

    if len(set(shared_hash for _ in asset_results)) != 1:
        raise RuntimeError("Shared-base canonical hash equality failed")
    if len(
        {
            tuple(dimensions)
            for dimensions in observed_exact_dimensions.values()
        }
    ) != 1:
        raise RuntimeError("Cross-asset exact dimensions differ")

    combined = {
        "schema": "AERATHEA_FRESH_TWIN_DCC_SOURCE_BUILDER_A01_V1",
        "date_utc": utc_now(),
        "run_id": RUN_ID,
        "build_id": BUILD_ID,
        "artifact_status": "candidate pending independent saved-file audit",
        "result": "PRE_SAVE_PASS",
        "builder": {
            "path": relative(Path(__file__)),
            "sha256": sha256(Path(__file__)),
        },
        "governing_blueprint": {
            "path": relative(BLUEPRINT),
            "sha256": EXPECTED_HASHES[BLUEPRINT],
        },
        "fresh_builder_approval": {
            "path": relative(BUILD_APPROVAL),
            "sha256": EXPECTED_HASHES[BUILD_APPROVAL],
        },
        "canonical_shared_base_sha256": shared_hash,
        "exact_shared_dimensions_cm": [
            qstr(value) for value in EXPECTED_BOUNDS
        ],
        "cross_asset_exact_bound_difference_cm": ["0/1", "0/1", "0/1"],
        "source_authority_checks": authority_checks,
        "input_geometry_files": [],
        "quarantined_geometry_read_count": 0,
        "assets": asset_results,
        "next_gate": "independent saved-file and cross-asset audit",
        "step_13_authority": False,
        "unreal_authority": False,
    }
    write_json(COMBINED_MANIFEST, combined)
    print(json.dumps(combined, indent=2, sort_keys=True))
    return 0


def look_at(camera: Any, target: tuple[float, float, float]) -> None:
    from mathutils import Vector

    direction = Vector(target) - camera.location
    camera.rotation_euler = direction.to_track_quat("-Z", "Y").to_euler()


def configure_render_scene(bpy: Any) -> None:
    scene = bpy.context.scene
    try:
        scene.render.engine = "BLENDER_WORKBENCH_NEXT"
    except TypeError:
        scene.render.engine = "BLENDER_WORKBENCH"
    scene.render.resolution_x = 640
    scene.render.resolution_y = 640
    scene.render.resolution_percentage = 100
    scene.render.image_settings.file_format = "PNG"
    scene.render.image_settings.color_mode = "RGBA"
    scene.render.film_transparent = False
    scene.display.shading.light = "STUDIO"
    scene.display.shading.studio_light = "paint.sl"
    scene.display.shading.color_type = "MATERIAL"
    scene.display.shading.show_shadows = True
    scene.display.shading.show_cavity = True
    scene.display.shading.cavity_type = "WORLD"
    scene.display.shading.curvature_ridge_factor = 1.5
    scene.display.shading.curvature_valley_factor = 1.2
    scene.world.color = (0.018, 0.024, 0.032)


def render_view(
    bpy: Any,
    output: Path,
    direction: tuple[float, float, float],
    target: tuple[float, float, float],
    ortho_scale: float,
) -> None:
    camera_data = bpy.data.cameras.new(f"CAM_{output.stem}")
    camera_data.type = "ORTHO"
    camera_data.ortho_scale = ortho_scale
    camera = bpy.data.objects.new(f"CAM_{output.stem}", camera_data)
    bpy.context.scene.collection.objects.link(camera)
    length = math.sqrt(sum(value * value for value in direction))
    unit = tuple(value / length for value in direction)
    camera.location = tuple(
        target[index] + unit[index] * 420.0 for index in range(3)
    )
    look_at(camera, target)
    bpy.context.scene.camera = camera
    bpy.context.scene.render.filepath = str(output)
    bpy.ops.render.render(write_still=True)
    bpy.data.objects.remove(camera, do_unlink=True)
    bpy.data.cameras.remove(camera_data)


def internal_render(asset_key: str) -> int:
    import bpy

    asset = ASSETS[asset_key]
    output_root: Path = asset["output_root"]
    audit_path = output_root / "independent_saved_file_audit.json"
    audit = load_json(audit_path)
    if audit.get("result") != "PASS":
        raise RuntimeError(
            f"{asset['asset_id']} independent audit has not passed"
        )
    render_root = output_root / "renders"
    render_root.mkdir(exist_ok=False)
    configure_render_scene(bpy)
    target = (0.0, 0.0, 85.0)
    views = {
        "front": ((0.0, -1.0, 0.0), 190.0),
        "right": ((1.0, 0.0, 0.0), 190.0),
        "top": ((0.0, 0.0, 1.0), 116.0),
        "three_quarter": ((1.0, -1.35, 0.68), 205.0),
    }
    for name, (direction, scale) in views.items():
        render_view(
            bpy,
            render_root / f"{name}.png",
            direction,
            target,
            scale,
        )
    manifest = {
        "schema": "AERATHEA_FRESH_TWIN_DCC_SOURCE_RENDER_A01_V1",
        "asset_id": asset["asset_id"],
        "artifact_status": "candidate review evidence",
        "independent_audit_sha256": sha256(audit_path),
        "views": {
            name: {
                "path": relative(render_root / f"{name}.png"),
                "sha256": sha256(render_root / f"{name}.png"),
            }
            for name in views
        },
        "step_13_authority": False,
        "unreal_authority": False,
    }
    write_json(output_root / "render_manifest.json", manifest)
    return 0


def blender_command(*arguments: str, blend: Path | None = None) -> list[str]:
    command = [
        str(BLENDER),
        "--background",
        "--factory-startup",
    ]
    if blend is not None:
        command.append(str(blend))
    command.extend(["--python", str(Path(__file__).resolve()), "--"])
    command.extend(arguments)
    return command


def run_checked(command: list[str]) -> None:
    environment = dict(os.environ)
    environment["PYTHONHASHSEED"] = "0"
    subprocess.run(
        command,
        cwd=ROOT,
        env=environment,
        check=True,
    )


def external_build_all() -> int:
    verify_authority()
    if COMBINED_MANIFEST.exists():
        raise RuntimeError(
            f"Fresh-build manifest already exists: {relative(COMBINED_MANIFEST)}"
        )
    for asset in ASSETS.values():
        if asset["output_root"].exists():
            raise RuntimeError(
                "Fresh output root already exists: "
                f"{relative(asset['output_root'])}"
            )
    run_checked(blender_command("--internal-build-all"))
    if not COMBINED_MANIFEST.is_file():
        raise RuntimeError("Blender did not produce the combined manifest")
    return 0


def compose_review_board() -> Path:
    from PIL import Image, ImageDraw, ImageFont

    font_path = Path("/usr/share/fonts/truetype/dejavu/DejaVuSans.ttf")
    bold_path = Path(
        "/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf"
    )
    title_font = ImageFont.truetype(str(bold_path), 32)
    asset_font = ImageFont.truetype(str(bold_path), 25)
    label_font = ImageFont.truetype(str(font_path), 18)
    small_font = ImageFont.truetype(str(font_path), 15)
    thumb = 350
    margin = 28
    header = 105
    row_header = 62
    footer = 70
    width = margin * 2 + thumb * 4
    height = header + (row_header + thumb) * 2 + footer
    board = Image.new("RGB", (width, height), (12, 17, 24))
    draw = ImageDraw.Draw(board)
    draw.text(
        (margin, 18),
        "AERATHEA — SHARED-DEPTH TWIN HAMMERS",
        font=title_font,
        fill=(230, 237, 245),
    )
    draw.text(
        (margin, 63),
        "97.974428267601 × 44.299176584 × 170 cm  •  independent audit PASS",
        font=label_font,
        fill=(145, 184, 222),
    )
    view_names = ("front", "right", "top", "three_quarter")
    cursor_y = header
    for asset_key in ("siege_breaker", "foe_hammer"):
        asset = ASSETS[asset_key]
        audit = load_json(
            asset["output_root"] / "independent_saved_file_audit.json"
        )
        treatment = (
            "DOUBLE RUNE SIDED"
            if asset["variant"] == "rune_side"
            else "DOUBLE METAL-CENTER-PIECE SIDED"
        )
        draw.text(
            (margin, cursor_y + 8),
            f"{asset['display_name']}  —  {treatment}",
            font=asset_font,
            fill=(230, 237, 245),
        )
        draw.text(
            (width - 285, cursor_y + 13),
            f"AUDIT {audit['result']}  |  DCC SOURCE CANDIDATE",
            font=small_font,
            fill=(125, 214, 166),
        )
        cursor_y += row_header
        for index, view in enumerate(view_names):
            image = Image.open(
                asset["output_root"] / "renders" / f"{view}.png"
            ).convert("RGB")
            image.thumbnail((thumb, thumb), Image.Resampling.LANCZOS)
            tile = Image.new("RGB", (thumb, thumb), (21, 28, 37))
            tile.paste(
                image,
                ((thumb - image.width) // 2, (thumb - image.height) // 2),
            )
            x = margin + index * thumb
            board.paste(tile, (x, cursor_y))
            draw.rectangle(
                (x, cursor_y, x + thumb - 1, cursor_y + thumb - 1),
                outline=(62, 79, 97),
                width=1,
            )
            draw.text(
                (x + 10, cursor_y + 10),
                view.replace("_", " ").upper(),
                font=small_font,
                fill=(198, 211, 224),
            )
        cursor_y += thumb
    draw.text(
        (margin, height - 48),
        (
            "Candidate review evidence only • shared base hash equal • "
            "zero cross-asset XYZ difference • Step 13 / export / Unreal locked"
        ),
        font=small_font,
        fill=(142, 154, 168),
    )
    REVIEW_BOARD.parent.mkdir(parents=True, exist_ok=True)
    board.save(REVIEW_BOARD)
    return REVIEW_BOARD


def external_render_all() -> int:
    verify_authority()
    for asset_key, asset in ASSETS.items():
        blend = (
            asset["output_root"]
            / f"{asset['asset_id']}_DCCSource_SharedDepth_A01.blend"
        )
        if not blend.is_file():
            raise RuntimeError(f"Missing audited blend: {relative(blend)}")
        run_checked(
            blender_command("--internal-render", "--asset-key", asset_key, blend=blend)
        )
    board = compose_review_board()
    print(f"Review board: {relative(board)}")
    return 0


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser()
    parser.add_argument("--build-all", action="store_true")
    parser.add_argument("--render-all", action="store_true")
    parser.add_argument("--internal-build-all", action="store_true")
    parser.add_argument("--internal-render", action="store_true")
    parser.add_argument("--asset-key", choices=tuple(ASSETS))
    return parser.parse_args(sys.argv[sys.argv.index("--") + 1 :] if "--" in sys.argv else None)


def main() -> int:
    args = parse_args()
    if args.internal_build_all:
        return internal_build_all()
    if args.internal_render:
        if not args.asset_key:
            raise RuntimeError("--internal-render requires --asset-key")
        return internal_render(args.asset_key)
    if args.build_all:
        return external_build_all()
    if args.render_all:
        return external_render_all()
    raise RuntimeError(
        "Choose --build-all, --render-all, --internal-build-all, "
        "or --internal-render"
    )


if __name__ == "__main__":
    raise SystemExit(main())
