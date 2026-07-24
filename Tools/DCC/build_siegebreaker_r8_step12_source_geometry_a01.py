#!/usr/bin/env python3
"""Build the two approved Siege Breaker Step 12 high-poly candidates.

The normal entry point is system Python.  It verifies the closed-world
authority set and then launches the hash-locked Blender binary.  Blender calls
this same file with ``--internal-build`` or ``--internal-render``.

No legacy mesh, coordinate, mask, UV, material, dimension, or render is read.
Geometry is derived only from the Step 11 blueprint and its hash-locked source
records plus the three exact Flamestrike-approved amendments.
"""

from __future__ import annotations

import argparse
import gzip
import hashlib
import json
import math
import os
import platform
import shutil
import subprocess
import sys
from collections import Counter, defaultdict
from dataclasses import dataclass, field
from datetime import datetime, timezone
from fractions import Fraction
from pathlib import Path
from typing import Any, Iterable, Iterator, Sequence


ROOT = Path(__file__).resolve().parents[2]
RUN_ID = "SB-CR-STEPS10-16-R8-ZERO-EXTRUSION-A02"
ASSET = "SM_DRW_SiegeBreaker_Hammer_A01"
PROOF_ROOT = ROOT / (
    "docs/assets/blueprints/SM_DRW_SiegeBreaker_Hammer_A01/proof_runs/"
    "SB-CR-STEPS10-16-R8-ZERO-EXTRUSION-A02"
)
DEFAULT_BLUEPRINT = PROOF_ROOT / "manifests/STEP_11_PRODUCTION_GEOMETRY_BLUEPRINT.json"
DEFAULT_AMENDMENT = PROOF_ROOT / (
    "steps/STEP_11B_HIGH_POLY_NANITE_PERFORMANCE_AMENDMENT_A01.md"
)
DEFAULT_PARITY_AMENDMENT = PROOF_ROOT / (
    "steps/STEP_11C_BOTTOM_C02_C03_LABEL_CORRECTION_A01.md"
)
DEFAULT_STITCH_AMENDMENT = PROOF_ROOT / (
    "steps/STEP_11D_THREE_BOUNDARY_STONE_STITCH_AMENDMENT_A01.md"
)
DEFAULT_TOLERANCE_AMENDMENT = PROOF_ROOT / (
    "steps/STEP_11E_CROSS_VIEW_SILHOUETTE_TOLERANCE_AMENDMENT_A01.md"
)
STITCH_VALIDATION = PROOF_ROOT / (
    "manifests/STEP_11D_THREE_BOUNDARY_STONE_STITCH_AMENDMENT_A01_VALIDATION.json"
)
TOLERANCE_VALIDATION = PROOF_ROOT / (
    "manifests/"
    "STEP_11E_CROSS_VIEW_SILHOUETTE_TOLERANCE_AMENDMENT_A01_VALIDATION.json"
)
ENVIRONMENT_LOCK = PROOF_ROOT / "manifests/STEP_12_ENVIRONMENT_LOCK_A01.json"
AUTHORITY_LOCK = PROOF_ROOT / (
    "manifests/STEP_11_PRODUCTION_BLUEPRINT_A02_AUTHORITY_LOCK.json"
)
STEP12_CONTRACT = PROOF_ROOT / (
    "steps/STEP_12_FRESH_DCC_SOURCE_GEOMETRY_A01_PROPOSED_CONTRACT.md"
)
STEP12_APPROVAL = PROOF_ROOT / (
    "steps/STEP_12_FRESH_DCC_SOURCE_GEOMETRY_A01_APPROVAL_RECORD.md"
)
INDEPENDENT_AUDITOR = ROOT / (
    "Tools/DCC/audit_siegebreaker_r8_step12_source_geometry_a01.py"
)

EXPECTED_HASHES = {
    "blueprint": "2b598497ba5e61a4352c217f3fb20b3545189c710934f3a21d9b7398ddb472c7",
    "amendment": "2e4276ea0adc32d8c6a21fb5bfbd46eacf627a9708c6187e56be1556eee76ba6",
    "parity_amendment": "45cc92d07f90fdb1bb104c8ede5e9fb6e6161454ea91d0923dc6f81cf02512d1",
    "stitch_amendment": "850fd42808be667da1d24f1dbccc8ff192ac8b2ccddadb0b714256637849b61a",
    "stitch_validation": "ff69717625d12e8e3f4f502d47c242a62ced72127bec5d9f5dd01c9537357d38",
    "tolerance_amendment": "640d19d6012b4c9926d7ddd431812481219fc65703effa08b194af2116e78b74",
    "tolerance_validation": "ee9337b65a7a5d0fa71295dfc5b153690667c00aea646cadc6ff1eb3e697ce4d",
    "environment_lock": "a2d9be9162d3aa5440492765aafe621e63bc4a1f80814bd523dce20dae7b66f8",
    "authority_lock": "3235fcc9480ad246f968b275792aa3a309aa34710b5bfec3fc005980ae3d5069",
    "step12_contract": "a3f16266da53ed28a0c849818271dea0c07cd8ba8005e05a6778e2a0f6d2935b",
    "step12_approval": "2b6fedd15020808beb63ff556c66bc52114a06cd69331f72bfe637caea69e7d7",
}

CANDIDATES = ("rune_side", "metal_center_piece_side")
ANGULAR_DIVISIONS = 64
FRONT_AXIS_X = Fraction(562)
FRONT_SCALE = Fraction(170, 1063)
AXIAL_SCALE = Fraction(52020, 517681)
RIGHT_SCALE = Fraction(85, 548)
TOP_CENTER_X = Fraction(1533, 2)
TOP_CENTER_Y = Fraction(1093, 2)
BOTTOM_CENTER_X = Fraction(1529, 2)
BOTTOM_CENTER_Y = Fraction(539)
RIGHT_AXIS_X = Fraction(557)
FRONT_Z_ORIGIN_Y = Fraction(1271)
RIGHT_Z_ORIGIN_Y = Fraction(1262)
FRONT_WIDTH_HALF = Fraction(52020, 1063)

COMPONENT_COLORS = {
    "C01_CENTER_CORE": (0.18, 0.24, 0.30, 1.0),
    "C02_STONE_LEFT": (0.075, 0.095, 0.12, 1.0),
    "C03_STONE_RIGHT": (0.075, 0.095, 0.12, 1.0),
    "C04_STRIKE_FACE_POSITIVE_X": (0.08, 0.18, 0.29, 1.0),
    "C06_UPPER_HAFT_CAP": (0.33, 0.18, 0.07, 1.0),
    "C07_HAFT": (0.16, 0.18, 0.20, 1.0),
    "C07B_HAFT_TO_HANDLE_FERRULE": (0.30, 0.16, 0.06, 1.0),
    "C08_GRIP": (0.13, 0.055, 0.025, 1.0),
    "C09_LOWER_COLLAR": (0.30, 0.16, 0.06, 1.0),
    "C10_POMMEL_BODY": (0.15, 0.17, 0.20, 1.0),
    "C11_POMMEL_TERMINAL_CAP": (0.28, 0.14, 0.05, 1.0),
    "C12_UPPER_HEAD_CAP_SPIRE": (0.30, 0.16, 0.06, 1.0),
    "CLOSURE": (0.11, 0.13, 0.16, 1.0),
    "CONTACT": (0.22, 0.15, 0.08, 1.0),
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
    payload = json.dumps(
        value,
        sort_keys=True,
        separators=(",", ":"),
        ensure_ascii=True,
    ).encode("ascii")
    return hashlib.sha256(payload).hexdigest()


def load_json(path: Path) -> dict[str, Any]:
    return json.loads(path.read_text(encoding="utf-8"))


def load_gzip_json(path: Path) -> dict[str, Any]:
    with gzip.open(path, "rt", encoding="utf-8") as handle:
        return json.load(handle)


def exact(record: dict[str, Any]) -> Fraction:
    return Fraction(int(record["numerator"]), int(record["denominator"]))


def qstr(value: Fraction) -> str:
    return f"{value.numerator}/{value.denominator}"


def f3(point: tuple[Fraction, Fraction, Fraction]) -> tuple[float, float, float]:
    return tuple(float(value) for value in point)  # type: ignore[return-value]


def relative(path: Path) -> str:
    return str(path.resolve().relative_to(ROOT))


def verify_hash(path: Path, expected: str, label: str) -> dict[str, Any]:
    observed = sha256(path) if path.is_file() else None
    if observed != expected:
        raise RuntimeError(
            f"Authority hash failure for {label}: expected {expected}, "
            f"observed {observed}"
        )
    return {
        "label": label,
        "path": relative(path),
        "sha256": observed,
        "result": "PASS",
    }


def verify_authority(
    blueprint_path: Path,
    amendment_path: Path,
    parity_amendment_path: Path,
    stitch_amendment_path: Path,
    tolerance_amendment_path: Path,
) -> tuple[dict[str, Any], list[dict[str, Any]]]:
    checks = [
        verify_hash(blueprint_path, EXPECTED_HASHES["blueprint"], "blueprint"),
        verify_hash(amendment_path, EXPECTED_HASHES["amendment"], "amendment"),
        verify_hash(
            parity_amendment_path,
            EXPECTED_HASHES["parity_amendment"],
            "parity_amendment",
        ),
        verify_hash(
            stitch_amendment_path,
            EXPECTED_HASHES["stitch_amendment"],
            "stitch_amendment",
        ),
        verify_hash(
            STITCH_VALIDATION,
            EXPECTED_HASHES["stitch_validation"],
            "stitch_validation",
        ),
        verify_hash(
            tolerance_amendment_path,
            EXPECTED_HASHES["tolerance_amendment"],
            "tolerance_amendment",
        ),
        verify_hash(
            TOLERANCE_VALIDATION,
            EXPECTED_HASHES["tolerance_validation"],
            "tolerance_validation",
        ),
        verify_hash(
            ENVIRONMENT_LOCK,
            EXPECTED_HASHES["environment_lock"],
            "environment_lock",
        ),
        verify_hash(
            AUTHORITY_LOCK,
            EXPECTED_HASHES["authority_lock"],
            "authority_lock",
        ),
        verify_hash(
            STEP12_CONTRACT,
            EXPECTED_HASHES["step12_contract"],
            "step12_contract",
        ),
        verify_hash(
            STEP12_APPROVAL,
            EXPECTED_HASHES["step12_approval"],
            "step12_approval",
        ),
    ]
    blueprint = load_json(blueprint_path)
    for key, record in sorted(blueprint["authority_files"].items()):
        checks.append(
            verify_hash(ROOT / record["path"], record["sha256"], key)
        )
    validation = load_json(STITCH_VALIDATION)
    if validation["step12_resume_preflight"]["result"] != "PASS":
        raise RuntimeError("Step 11D validation does not authorize Step 12")
    if not validation["closed_world_decision"]["builder_creation_allowed"]:
        raise RuntimeError("Step 11D validation forbids builder creation")
    tolerance_validation = load_json(TOLERANCE_VALIDATION)
    if tolerance_validation[
        "cross_view_silhouette_tolerance_validation"
    ]["result"] != "PASS":
        raise RuntimeError("Step 11E tolerance validation failed")
    if tolerance_validation["step12_resume_preflight"]["result"] != "PASS":
        raise RuntimeError("Step 11E validation does not authorize Step 12")
    return blueprint, checks


@dataclass
class MeshRecord:
    name: str
    component: str
    instruction_id: str
    occurrence: str
    material_key: str
    smooth: bool = False
    vertices: list[tuple[Fraction, Fraction, Fraction]] = field(
        default_factory=list
    )
    faces: list[tuple[int, ...]] = field(default_factory=list)
    _lookup: dict[tuple[Fraction, Fraction, Fraction], int] = field(
        default_factory=dict,
        repr=False,
    )

    def vertex(self, point: tuple[Fraction, Fraction, Fraction]) -> int:
        index = self._lookup.get(point)
        if index is None:
            index = len(self.vertices)
            self._lookup[point] = index
            self.vertices.append(point)
        return index

    def face(
        self,
        points: Sequence[tuple[Fraction, Fraction, Fraction]],
    ) -> None:
        indices = tuple(self.vertex(point) for point in points)
        if len(set(indices)) != len(indices):
            return
        self.faces.append(indices)

    def rotated_rz180(self, name: str, occurrence: str) -> "MeshRecord":
        result = MeshRecord(
            name=name,
            component=self.component,
            instruction_id=self.instruction_id,
            occurrence=occurrence,
            material_key=self.material_key,
            smooth=self.smooth,
        )
        result.vertices = [(-x, -y, z) for x, y, z in self.vertices]
        result._lookup = {
            point: index for index, point in enumerate(result.vertices)
        }
        result.faces = list(self.faces)
        return result

    @property
    def triangle_count(self) -> int:
        return sum(max(0, len(face) - 2) for face in self.faces)

    def exact_bounds(self) -> dict[str, list[Fraction]]:
        if not self.vertices:
            zero = [Fraction(0), Fraction(0), Fraction(0)]
            return {"minimum": zero, "maximum": zero}
        return {
            "minimum": [
                min(point[axis] for point in self.vertices)
                for axis in range(3)
            ],
            "maximum": [
                max(point[axis] for point in self.vertices)
                for axis in range(3)
            ],
        }


def front_point(
    source_x: Fraction,
    source_y: Fraction,
    front_y: Fraction,
) -> tuple[Fraction, Fraction, Fraction]:
    return (
        (source_x - FRONT_AXIS_X) * FRONT_SCALE,
        front_y,
        (FRONT_Z_ORIGIN_Y - source_y) * FRONT_SCALE,
    )


def top_point(
    source_x: Fraction,
    source_y: Fraction,
    world_z: Fraction,
) -> tuple[Fraction, Fraction, Fraction]:
    return (
        (source_x - TOP_CENTER_X) * AXIAL_SCALE,
        (source_y - TOP_CENTER_Y) * AXIAL_SCALE,
        world_z,
    )


def bottom_point(
    source_x: Fraction,
    source_y: Fraction,
    world_z: Fraction,
) -> tuple[Fraction, Fraction, Fraction]:
    return (
        (BOTTOM_CENTER_X - source_x) * AXIAL_SCALE,
        (BOTTOM_CENTER_Y - source_y) * AXIAL_SCALE,
        world_z,
    )


def right_rune_point(
    source_x: Fraction,
    source_y: Fraction,
) -> tuple[Fraction, Fraction, Fraction]:
    return (
        FRONT_WIDTH_HALF,
        -(source_x - RIGHT_AXIS_X) * RIGHT_SCALE,
        (RIGHT_Z_ORIGIN_Y - source_y) * RIGHT_SCALE,
    )


def right_metal_point(
    source_x: Fraction,
    source_y: Fraction,
) -> tuple[Fraction, Fraction, Fraction]:
    return (
        FRONT_WIDTH_HALF,
        (source_x - RIGHT_AXIS_X) * RIGHT_SCALE,
        (RIGHT_Z_ORIGIN_Y - source_y) * RIGHT_SCALE,
    )


def owner_rows(
    scanlines: dict[str, Any],
    view: str,
    component: str,
) -> list[dict[str, Any]]:
    return scanlines["views"][view]["component_owners"][component]["rows"]


def iter_owner_cells(
    rows: Iterable[dict[str, Any]],
) -> Iterator[tuple[int, int]]:
    for row in rows:
        source_y = int(row["y"])
        for start, stop in row["owner_runs_half_open"]:
            for source_x in range(int(start), int(stop)):
                yield source_x, source_y


def build_front_surface(
    name: str,
    component: str,
    instruction_id: str,
    rows: list[dict[str, Any]],
    front_y: Fraction,
) -> MeshRecord:
    record = MeshRecord(
        name=name,
        component=component,
        instruction_id=instruction_id,
        occurrence="SOURCE",
        material_key=component,
    )
    for source_x, source_y in iter_owner_cells(rows):
        p00 = front_point(Fraction(source_x), Fraction(source_y), front_y)
        p10 = front_point(Fraction(source_x + 1), Fraction(source_y), front_y)
        p11 = front_point(
            Fraction(source_x + 1),
            Fraction(source_y + 1),
            front_y,
        )
        p01 = front_point(
            Fraction(source_x),
            Fraction(source_y + 1),
            front_y,
        )
        record.face((p00, p01, p11, p10))
    return record


def axial_source_y_limits(
    plane: str,
    half_depth: Fraction,
) -> tuple[Fraction, Fraction]:
    if plane == "top":
        return (
            TOP_CENTER_Y - half_depth / AXIAL_SCALE,
            TOP_CENTER_Y,
        )
    if plane == "bottom":
        return (
            BOTTOM_CENTER_Y,
            BOTTOM_CENTER_Y + half_depth / AXIAL_SCALE,
        )
    raise ValueError(plane)


def build_axial_surface(
    name: str,
    component: str,
    instruction_id: str,
    rows: list[dict[str, Any]],
    plane: str,
    world_z: Fraction,
    half_depth: Fraction,
) -> MeshRecord:
    record = MeshRecord(
        name=name,
        component=component,
        instruction_id=instruction_id,
        occurrence="SOURCE",
        material_key=component,
    )
    source_y_min, source_y_max = axial_source_y_limits(plane, half_depth)
    mapper = top_point if plane == "top" else bottom_point
    for source_x, source_y in iter_owner_cells(rows):
        clipped_y0 = max(Fraction(source_y), source_y_min)
        clipped_y1 = min(Fraction(source_y + 1), source_y_max)
        if clipped_y0 >= clipped_y1:
            continue
        p00 = mapper(Fraction(source_x), clipped_y0, world_z)
        p10 = mapper(Fraction(source_x + 1), clipped_y0, world_z)
        p11 = mapper(Fraction(source_x + 1), clipped_y1, world_z)
        p01 = mapper(Fraction(source_x), clipped_y1, world_z)
        if plane == "top":
            record.face((p00, p10, p11, p01))
        else:
            record.face((p00, p01, p11, p10))
    return record


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
    points: Sequence[tuple[Fraction, Fraction, Fraction]],
) -> tuple[Fraction, Fraction, Fraction]:
    normal = [Fraction(0), Fraction(0), Fraction(0)]
    wrapped = list(points) + [points[0]]
    for current, following in zip(wrapped, wrapped[1:]):
        normal[0] += (
            (current[1] - following[1])
            * (current[2] + following[2])
        )
        normal[1] += (
            (current[2] - following[2])
            * (current[0] + following[0])
        )
        normal[2] += (
            (current[0] - following[0])
            * (current[1] + following[1])
        )
    return tuple(normal)  # type: ignore[return-value]


def build_c04_face(
    candidate: str,
    rows: list[dict[str, Any]],
) -> MeshRecord:
    is_rune = candidate == "rune_side"
    mapper = right_rune_point if is_rune else right_metal_point
    record = MeshRecord(
        name=(
            "SURF_C04_RUNE_FACE_HALF"
            if is_rune
            else "SURF_C04_METAL_FACE_HALF"
        ),
        component="C04_STRIKE_FACE_POSITIVE_X",
        instruction_id=(
            "SURF_C04_RUNE_FACE_HALF"
            if is_rune
            else "SURF_C04_METAL_FACE_HALF"
        ),
        occurrence="SOURCE_LOCAL_Y_MIRROR_COMPLETE",
        material_key="C04_STRIKE_FACE_POSITIVE_X",
    )
    for source_x, source_y in iter_owner_cells(rows):
        points = (
            mapper(Fraction(source_x), Fraction(source_y)),
            mapper(Fraction(source_x + 1), Fraction(source_y)),
            mapper(Fraction(source_x + 1), Fraction(source_y + 1)),
            mapper(Fraction(source_x), Fraction(source_y + 1)),
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
    radius: Fraction,
    world_z: Fraction,
) -> list[tuple[Fraction, Fraction, Fraction]]:
    points = []
    for index in range(ANGULAR_DIVISIONS + 1):
        theta = -math.pi / 2.0 + math.pi * index / ANGULAR_DIVISIONS
        points.append(
            (
                quantized_fraction(float(radius) * math.cos(theta)),
                quantized_fraction(float(radius) * math.sin(theta)),
                world_z,
            )
        )
    return points


def positive_radius_from_row(row: dict[str, Any]) -> Fraction:
    runs = row.get("owner_runs_half_open", row.get("runs_half_open"))
    if not runs:
        raise RuntimeError(f"Missing source owner run at y={row['source_y']}")
    positive_edge = max(int(stop) for _, stop in runs)
    if positive_edge <= int(FRONT_AXIS_X):
        raise RuntimeError(
            f"No positive owner edge at source y={row['source_y']}"
        )
    return Fraction(positive_edge - int(FRONT_AXIS_X)) * FRONT_SCALE


def normalized_profile_rows(
    rows: list[dict[str, Any]],
) -> list[dict[str, Any]]:
    result = []
    for row in rows:
        source_y = int(row.get("source_y", row.get("y")))
        normalized = dict(row)
        normalized["source_y"] = source_y
        if "runs_half_open" not in normalized:
            normalized["runs_half_open"] = normalized["owner_runs_half_open"]
        result.append(normalized)
    return sorted(result, key=lambda item: item["source_y"])


def build_rotational_surface(
    instruction_id: str,
    component: str,
    rows: list[dict[str, Any]],
    terminal_source_y: int,
) -> tuple[MeshRecord, dict[str, Any]]:
    rows = normalized_profile_rows(rows)
    if not rows:
        raise RuntimeError(f"No rows for {instruction_id}")
    expected = list(range(rows[0]["source_y"], terminal_source_y))
    observed = [row["source_y"] for row in rows]
    if observed != expected:
        raise RuntimeError(
            f"{instruction_id} row sequence mismatch: "
            f"{observed[:2]}..{observed[-2:]}"
        )
    radii = [positive_radius_from_row(row) for row in rows]
    ring_records = [
        {
            "source_y": row["source_y"],
            "radius": radius,
            "world_z": (
                FRONT_Z_ORIGIN_Y - Fraction(row["source_y"])
            )
            * FRONT_SCALE,
        }
        for row, radius in zip(rows, radii)
    ]
    ring_records.append(
        {
            "source_y": terminal_source_y,
            "radius": radii[-1],
            "world_z": (
                FRONT_Z_ORIGIN_Y - Fraction(terminal_source_y)
            )
            * FRONT_SCALE,
        }
    )
    record = MeshRecord(
        name=instruction_id,
        component=component,
        instruction_id=instruction_id,
        occurrence="SOURCE",
        material_key=component,
        smooth=True,
    )
    ring_indices: list[list[int]] = []
    for ring in ring_records:
        ring_indices.append(
            [
                record.vertex(point)
                for point in ring_points(ring["radius"], ring["world_z"])
            ]
        )
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
        "instruction_id": instruction_id,
        "source_rows_half_open": [
            rows[0]["source_y"],
            terminal_source_y,
        ],
        "row_count": len(rows),
        "ring_count": len(ring_records),
        "angular_divisions_positive_x": ANGULAR_DIVISIONS,
        "first_radius_exact": qstr(radii[0]),
        "last_radius_exact": qstr(radii[-1]),
        "top_world_z_exact": qstr(ring_records[0]["world_z"]),
        "bottom_world_z_exact": qstr(ring_records[-1]["world_z"]),
    }


def build_half_annular_shoulder(
    instruction_id: str,
    component: str,
    world_z: Fraction,
    upper_radius: Fraction,
    lower_radius: Fraction,
) -> MeshRecord:
    record = MeshRecord(
        name=instruction_id,
        component=component,
        instruction_id=instruction_id,
        occurrence="SOURCE",
        material_key="CONTACT",
    )
    upper = ring_points(upper_radius, world_z)
    lower = ring_points(lower_radius, world_z)
    normal_positive_z = lower_radius > upper_radius
    for segment in range(ANGULAR_DIVISIONS):
        points = (
            upper[segment],
            upper[segment + 1],
            lower[segment + 1],
            lower[segment],
        )
        record.face(points if normal_positive_z else tuple(reversed(points)))
    return record


def build_half_cap(
    instruction_id: str,
    component: str,
    world_z: Fraction,
    radius: Fraction,
    normal_positive_z: bool,
) -> MeshRecord:
    record = MeshRecord(
        name=instruction_id,
        component=component,
        instruction_id=instruction_id,
        occurrence="SOURCE",
        material_key="CONTACT",
    )
    center = (Fraction(0), Fraction(0), world_z)
    ring = ring_points(radius, world_z)
    for segment in range(ANGULAR_DIVISIONS):
        points = (center, ring[segment], ring[segment + 1])
        record.face(points if normal_positive_z else tuple(reversed(points)))
    return record


@dataclass(frozen=True)
class ChainPoint:
    source_x: Fraction
    source_y: Fraction
    world: tuple[Fraction, Fraction, Fraction]


def boundary_owner_key(boundary_id: str) -> str:
    if "_C02_" in boundary_id:
        return "c02_owner_edge_x"
    if "_C03_" in boundary_id:
        return "c03_owner_edge_x"
    raise KeyError(boundary_id)


def step_boundary_source_points(
    boundary_id: str,
    record: dict[str, Any],
) -> list[tuple[Fraction, Fraction]]:
    owner_key = boundary_owner_key(boundary_id)
    samples = sorted(record["samples"], key=lambda sample: int(sample["y"]))
    points: list[tuple[Fraction, Fraction]] = []
    for sample in samples:
        source_x = Fraction(int(sample[owner_key]))
        source_y = Fraction(int(sample["y"]))
        if not points:
            points.append((source_x, source_y))
        elif points[-1] != (source_x, source_y):
            points.append((source_x, source_y))
        endpoint = (source_x, source_y + 1)
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
            if minimum_y <= ay <= maximum_y:
                clipped_a, clipped_b = a, b
            else:
                continue
        else:
            t0 = max(Fraction(0), (minimum_y - ay) / dy)
            t1 = min(Fraction(1), (maximum_y - ay) / dy)
            if dy < 0:
                t0, t1 = (
                    max(Fraction(0), (maximum_y - ay) / dy),
                    min(Fraction(1), (minimum_y - ay) / dy),
                )
            if t0 > t1:
                continue
            clipped_a = (ax + t0 * (bx - ax), ay + t0 * dy)
            clipped_b = (ax + t1 * (bx - ax), ay + t1 * dy)
        if not result or result[-1] != clipped_a:
            result.append(clipped_a)
        if result[-1] != clipped_b:
            result.append(clipped_b)
    if len(result) < 2:
        raise RuntimeError(
            f"Boundary clip produced fewer than two points for "
            f"{minimum_y}..{maximum_y}"
        )
    return result


def boundary_chain(
    boundary_id: str,
    boundaries: dict[str, Any],
    plane: str,
    half_depth: Fraction,
    world_z: Fraction | None = None,
    logical_bottom_source_id: str | None = None,
) -> list[ChainPoint]:
    source_id = logical_bottom_source_id or boundary_id
    source_points = step_boundary_source_points(
        source_id,
        boundaries["boundaries"][source_id],
    )
    if plane in {"top", "bottom"}:
        minimum_y, maximum_y = axial_source_y_limits(plane, half_depth)
        source_points = clip_source_polyline_y(
            source_points,
            minimum_y,
            maximum_y,
        )
    if plane == "front":
        mapper = lambda x, y: front_point(x, y, -half_depth)
    elif plane == "top":
        if world_z is None:
            raise ValueError("top boundary requires world_z")
        mapper = lambda x, y: top_point(x, y, world_z)
    elif plane == "bottom":
        if world_z is None:
            raise ValueError("bottom boundary requires world_z")
        mapper = lambda x, y: bottom_point(x, y, world_z)
    else:
        raise ValueError(plane)
    return [
        ChainPoint(x, y, mapper(x, y))
        for x, y in source_points
    ]


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


def connector(
    a: ChainPoint,
    b: ChainPoint,
) -> list[ChainPoint]:
    return [a, b]


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
            dx = b.world[0] - a.world[0]
            dy = b.world[1] - a.world[1]
            dz = b.world[2] - a.world[2]
            length = dx * dx + dy * dy + dz * dz
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
        raise RuntimeError(f"Expected 12 perimeter members, got {len(members)}")
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
    return (
        (b[0] - a[0]) * (c[1] - a[1])
        - (b[1] - a[1]) * (c[0] - a[0])
    )


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
        raise RuntimeError("Invalid stitch perimeter")
    active = list(range(len(world_points)))
    triangles: list[tuple[int, int, int]] = []
    while len(active) > 3:
        candidates = []
        for position, current in enumerate(active):
            previous = active[position - 1]
            following = active[(position + 1) % len(active)]
            area = cross2(
                parameter_points[previous],
                parameter_points[current],
                parameter_points[following],
            )
            if area <= 0:
                continue
            world_normal = cross(
                vector_sub(world_points[current], world_points[previous]),
                vector_sub(world_points[following], world_points[previous]),
            )
            if world_normal == (0, 0, 0):
                continue
            diagonal = squared_distance(
                world_points[previous],
                world_points[following],
            )
            candidates.append(
                (diagonal, current, position, previous, following)
            )
        candidates.sort(key=lambda item: (item[0], item[1]))
        selected = None
        for _, _, position, previous, following in candidates:
            current = active[position]
            contains_vertex = any(
                other not in {previous, current, following}
                and point_in_triangle_strict(
                    parameter_points[other],
                    parameter_points[previous],
                    parameter_points[current],
                    parameter_points[following],
                )
                for other in active
            )
            if not contains_vertex:
                selected = (position, previous, current, following)
                break
        if selected is None:
            raise RuntimeError(
                "Approved deterministic ear clipping found no eligible ear"
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
        raise RuntimeError(
            "Approved deterministic ear clipping ended on a zero-area "
            "world-space triangle"
        )
    triangles.append(final)
    return triangles


def oriented_closure_face(
    points: Sequence[tuple[Fraction, Fraction, Fraction]],
    target_x_sign: int,
) -> tuple[tuple[Fraction, Fraction, Fraction], ...]:
    normal = cross(
        vector_sub(points[1], points[0]),
        vector_sub(points[2], points[0]),
    )
    if normal[0] * target_x_sign < 0:
        return tuple(reversed(points))
    return tuple(points)


def build_stone_inner_closures(
    boundaries: dict[str, Any],
    half_depth: Fraction,
    stone_top_z: Fraction,
    stone_bottom_z: Fraction,
) -> tuple[MeshRecord, MeshRecord, dict[str, Any]]:
    front_c02 = boundary_chain(
        "FRONT_C02_INNER_OWNER_EDGE",
        boundaries,
        "front",
        half_depth,
    )
    front_c03 = boundary_chain(
        "FRONT_C03_INNER_OWNER_EDGE",
        boundaries,
        "front",
        half_depth,
    )
    top_c02 = boundary_chain(
        "TOP_C02_INNER_OWNER_EDGE",
        boundaries,
        "top",
        half_depth,
        world_z=stone_top_z,
    )
    top_c03 = boundary_chain(
        "TOP_C03_INNER_OWNER_EDGE",
        boundaries,
        "top",
        half_depth,
        world_z=stone_top_z,
    )
    bottom_c02 = boundary_chain(
        "BOTTOM_C02_INNER_OWNER_EDGE",
        boundaries,
        "bottom",
        half_depth,
        world_z=stone_bottom_z,
        logical_bottom_source_id="BOTTOM_C03_INNER_OWNER_EDGE",
    )
    bottom_c03 = boundary_chain(
        "BOTTOM_C03_INNER_OWNER_EDGE",
        boundaries,
        "bottom",
        half_depth,
        world_z=stone_bottom_z,
        logical_bottom_source_id="BOTTOM_C02_INNER_OWNER_EDGE",
    )

    bottom_c02_front_center = reverse_chain(bottom_c02)
    bottom_c03_front_center = reverse_chain(bottom_c03)
    top_c02_front_center = top_c02
    top_c03_front_center = top_c03

    members = [
        front_c02,
        connector(front_c02[-1], bottom_c02_front_center[0]),
        bottom_c02_front_center,
        connector(
            bottom_c02_front_center[-1],
            rz180_chain(bottom_c03_front_center)[-1],
        ),
        reverse_chain(rz180_chain(bottom_c03_front_center)),
        connector(
            reverse_chain(rz180_chain(bottom_c03_front_center))[-1],
            reverse_chain(rz180_chain(front_c03))[0],
        ),
        reverse_chain(rz180_chain(front_c03)),
        connector(
            reverse_chain(rz180_chain(front_c03))[-1],
            rz180_chain(top_c03_front_center)[0],
        ),
        rz180_chain(top_c03_front_center),
        connector(
            rz180_chain(top_c03_front_center)[-1],
            top_c02_front_center[-1],
        ),
        reverse_chain(top_c02_front_center),
        connector(reverse_chain(top_c02_front_center)[-1], front_c02[0]),
    ]
    world_points, parameter_points = parameterized_perimeter(members)
    triangles = ear_clip(world_points, parameter_points)
    negative = MeshRecord(
        name="CLOSURE_C02_INNER_COMPLETED_PERIMETER",
        component="C02_STONE_LEFT",
        instruction_id="CLOSURE_C02_INNER",
        occurrence="COMPLETED_AFTER_ONE_RZ180",
        material_key="CLOSURE",
    )
    for triangle in triangles:
        points = [world_points[index] for index in triangle]
        negative.face(oriented_closure_face(points, 1))
    positive = negative.rotated_rz180(
        "CLOSURE_C03_INNER_COMPLETED_PERIMETER",
        "COMPLETED_AFTER_ONE_RZ180",
    )
    positive.component = "C03_STONE_RIGHT"
    positive.instruction_id = "CLOSURE_C03_INNER"
    for index, face in enumerate(positive.faces):
        points = [positive.vertices[item] for item in face]
        positive.faces[index] = tuple(
            positive.vertex(point)
            for point in oriented_closure_face(points, -1)
        )
    return negative, positive, {
        "negative_perimeter_vertex_count": len(world_points),
        "negative_triangle_count": len(triangles),
        "parameter_polygon": [
            [qstr(x), qstr(y)] for x, y in PARAMETER_DODECAGON
        ],
        "top_y0_bridge_cm": (
            float(abs(top_c02[-1].world[0] + top_c03[-1].world[0]))
        ),
        "bottom_y0_bridge_cm": (
            float(
                abs(
                    bottom_c02_front_center[-1].world[0]
                    + bottom_c03_front_center[-1].world[0]
                )
            )
        ),
        "tolerance_weld_used": False,
        "steiner_vertices_used": False,
    }


def edge_source_points_from_rows(
    rows: list[dict[str, Any]],
    choose_source_edge: str,
) -> list[tuple[Fraction, Fraction]]:
    samples = []
    for row in rows:
        source_y = int(row.get("y", row.get("source_y")))
        runs = row.get("owner_runs_half_open", row.get("runs_half_open"))
        if not runs:
            continue
        if choose_source_edge == "minimum":
            source_x = min(int(start) for start, _ in runs)
        elif choose_source_edge == "maximum":
            source_x = max(int(stop) for _, stop in runs)
        else:
            raise ValueError(choose_source_edge)
        samples.append((source_x, source_y))
    samples.sort(key=lambda item: item[1])
    points: list[tuple[Fraction, Fraction]] = []
    for source_x_int, source_y_int in samples:
        source_x = Fraction(source_x_int)
        source_y = Fraction(source_y_int)
        if not points:
            points.append((source_x, source_y))
        elif points[-1] != (source_x, source_y):
            points.append((source_x, source_y))
        endpoint = (source_x, source_y + 1)
        if points[-1] != endpoint:
            points.append(endpoint)
    return points


def derived_edge_chain(
    rows: list[dict[str, Any]],
    plane: str,
    world_side: str,
    half_depth: Fraction,
    world_z: Fraction | None = None,
) -> list[ChainPoint]:
    if plane in {"front", "top"}:
        choice = "maximum" if world_side == "positive" else "minimum"
    elif plane == "bottom":
        choice = "minimum" if world_side == "positive" else "maximum"
    else:
        raise ValueError(plane)
    source_points = edge_source_points_from_rows(rows, choice)
    if plane in {"top", "bottom"}:
        source_points = clip_source_polyline_y(
            source_points,
            *axial_source_y_limits(plane, half_depth),
        )
    if plane == "front":
        mapper = lambda x, y: front_point(x, y, -half_depth)
    elif plane == "top":
        if world_z is None:
            raise ValueError("top outer chain requires world_z")
        mapper = lambda x, y: top_point(x, y, world_z)
    else:
        if world_z is None:
            raise ValueError("bottom outer chain requires world_z")
        mapper = lambda x, y: bottom_point(x, y, world_z)
    return [
        ChainPoint(x, y, mapper(x, y))
        for x, y in source_points
    ]


def completed_positive_stone_outer_loop(
    scanlines: dict[str, Any],
    half_depth: Fraction,
    stone_top_z: Fraction,
    stone_bottom_z: Fraction,
) -> list[tuple[Fraction, Fraction, Fraction]]:
    front_c03 = derived_edge_chain(
        owner_rows(scanlines, "front", "C03_STONE_RIGHT"),
        "front",
        "positive",
        half_depth,
    )
    front_c02 = derived_edge_chain(
        owner_rows(scanlines, "front", "C02_STONE_LEFT"),
        "front",
        "negative",
        half_depth,
    )
    top_c03 = derived_edge_chain(
        owner_rows(scanlines, "top", "C03_STONE_RIGHT"),
        "top",
        "positive",
        half_depth,
        stone_top_z,
    )
    top_c02 = derived_edge_chain(
        owner_rows(scanlines, "top", "C02_STONE_LEFT"),
        "top",
        "negative",
        half_depth,
        stone_top_z,
    )
    # Step 11C corrected logical bottom identities.
    bottom_c03 = derived_edge_chain(
        owner_rows(scanlines, "bottom", "C02_STONE_LEFT"),
        "bottom",
        "positive",
        half_depth,
        stone_bottom_z,
    )
    bottom_c02 = derived_edge_chain(
        owner_rows(scanlines, "bottom", "C03_STONE_RIGHT"),
        "bottom",
        "negative",
        half_depth,
        stone_bottom_z,
    )
    bottom_c03_fc = reverse_chain(bottom_c03)
    bottom_c02_fc = reverse_chain(bottom_c02)
    members = [
        front_c03,
        connector(front_c03[-1], bottom_c03_fc[0]),
        bottom_c03_fc,
        connector(
            bottom_c03_fc[-1],
            rz180_chain(bottom_c02_fc)[-1],
        ),
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
    candidate: str,
    rows: list[dict[str, Any]],
) -> list[tuple[Fraction, Fraction, Fraction]]:
    is_rune = candidate == "rune_side"
    choice = "maximum" if is_rune else "minimum"
    mapper = right_rune_point if is_rune else right_metal_point
    source = edge_source_points_from_rows(rows, choice)
    half_chain = [
        ChainPoint(x, y, mapper(x, y))
        for x, y in source
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
    points: list[tuple[Fraction, Fraction, Fraction]],
) -> list[Fraction]:
    lengths = [Fraction(0)]
    wrapped = points + [points[0]]
    for a, b in zip(wrapped, wrapped[1:]):
        length = sum(abs(b[axis] - a[axis]) for axis in range(3))
        if length == 0:
            continue
        lengths.append(lengths[-1] + length)
    total = lengths[-1]
    if total == 0:
        raise RuntimeError("Zero-length closure loop")
    return [value / total for value in lengths]


def evaluate_closed_loop(
    points: list[tuple[Fraction, Fraction, Fraction]],
    breakpoints: list[Fraction],
    parameter: Fraction,
) -> tuple[Fraction, Fraction, Fraction]:
    parameter = parameter % 1
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
    candidate: str,
    scanlines: dict[str, Any],
    half_depth: Fraction,
    stone_top_z: Fraction,
    stone_bottom_z: Fraction,
) -> tuple[MeshRecord, MeshRecord, dict[str, Any]]:
    stone_loop = completed_positive_stone_outer_loop(
        scanlines,
        half_depth,
        stone_top_z,
        stone_bottom_z,
    )
    c04_rows = owner_rows(
        scanlines,
        "right",
        "C04_RUNE_SIDE"
        if candidate == "rune_side"
        else "C04_METAL_CENTER_PIECE_SIDE",
    )
    face_loop = c04_outer_loop(candidate, c04_rows)
    stone_breaks = loop_breakpoints(stone_loop)
    face_breaks = loop_breakpoints(face_loop)
    parameters = sorted(set(stone_breaks + face_breaks))
    if parameters[-1] != 1:
        parameters.append(Fraction(1))
    instruction_id = (
        "CLOSURE_C03_TO_C04_RUNE"
        if candidate == "rune_side"
        else "CLOSURE_C03_TO_C04_METAL"
    )
    positive = MeshRecord(
        name=instruction_id,
        component="C03_STONE_RIGHT",
        instruction_id=instruction_id,
        occurrence="COMPLETED_AFTER_ONE_RZ180",
        material_key="CLOSURE",
    )
    for start, stop in zip(parameters, parameters[1:]):
        stone_a = evaluate_closed_loop(stone_loop, stone_breaks, start)
        stone_b = evaluate_closed_loop(stone_loop, stone_breaks, stop)
        face_a = evaluate_closed_loop(face_loop, face_breaks, start)
        face_b = evaluate_closed_loop(face_loop, face_breaks, stop)
        ordered_points = (stone_a, stone_b, face_b, face_a)
        points: list[tuple[Fraction, Fraction, Fraction]] = []
        for point in ordered_points:
            if not points or points[-1] != point:
                points.append(point)
        if len(points) > 1 and points[0] == points[-1]:
            points.pop()
        if len(points) < 3:
            continue
        normal = polygon_normal(points)
        if normal == (0, 0, 0):
            continue
        positive.face(
            tuple(points)
            if normal[0] > 0
            else tuple(reversed(points))
        )
    negative = positive.rotated_rz180(
        f"{instruction_id}_RZ180",
        "COMPLETED_AFTER_ONE_RZ180",
    )
    negative.component = "C02_STONE_LEFT"
    return positive, negative, {
        "instruction_id": instruction_id,
        "stone_loop_vertices": len(stone_loop),
        "c04_loop_vertices": len(face_loop),
        "shared_parameter_breakpoints": len(parameters),
        "ruled_faces_positive": len(positive.faces),
        "ruled_faces_negative": len(negative.faces),
        "steiner_vertices": (
            "only exact evaluations on existing straight loop edges at "
            "shared cumulative-length breakpoints"
        ),
    }


def source_rows_for_rotational_component(
    component: str,
    scanlines: dict[str, Any],
    step06_front: dict[str, Any],
) -> tuple[list[dict[str, Any]], int]:
    intervals = {
        "C06_UPPER_HAFT_CAP": (600, 670),
        "C07_HAFT": (670, 870),
        "C07B_HAFT_TO_HANDLE_FERRULE": (870, 955),
        "C08_GRIP": (955, 1110),
        "C09_LOWER_COLLAR": (1110, 1150),
        "C10_POMMEL_BODY": (1150, 1220),
        "C11_POMMEL_TERMINAL_CAP": (1220, 1271),
        "C12_UPPER_HEAD_CAP_SPIRE": (208, 295),
    }
    start, stop = intervals[component]
    if component == "C06_UPPER_HAFT_CAP":
        return (
            owner_rows(
                scanlines,
                "front",
                "C06_UPPER_HAFT_CAP",
            ),
            stop,
        )
    if component == "C12_UPPER_HEAD_CAP_SPIRE":
        early = [
            row
            for row in step06_front["row_profiles"]
            if 208 <= int(row["source_y"]) < 221
        ]
        reserved = owner_rows(
            scanlines,
            "front",
            "C12_RESERVED_EXISTING_OWNER",
        )
        return early + reserved, stop
    rows = [
        row
        for row in step06_front["row_profiles"]
        if start <= int(row["source_y"]) < stop
    ]
    return rows, stop


def build_candidate_records(
    candidate: str,
    blueprint: dict[str, Any],
    scanlines: dict[str, Any],
    boundaries: dict[str, Any],
    step06_front: dict[str, Any],
) -> tuple[list[MeshRecord], dict[str, Any]]:
    candidate_record = blueprint["candidate_variants"][candidate]
    half_depth = exact(candidate_record["source_half_depth_cm"])
    stone_top_z = exact(
        blueprint["measurement_catalog"]["MEAS_C02"]["world_z_top_cm"]
    )
    stone_bottom_z = exact(
        blueprint["measurement_catalog"]["MEAS_C02"]["world_z_bottom_cm"]
    )
    source_records: list[MeshRecord] = []
    surface_report: list[dict[str, Any]] = []

    c04_owner_name = (
        "C04_RUNE_SIDE"
        if candidate == "rune_side"
        else "C04_METAL_CENTER_PIECE_SIDE"
    )
    c04 = build_c04_face(
        candidate,
        owner_rows(scanlines, "right", c04_owner_name),
    )
    source_records.append(c04)
    surface_report.append(
        {
            "instruction_id": c04.instruction_id,
            "result": "PASS",
            "faces": len(c04.faces),
            "local_y_mirror_count": 1,
        }
    )

    front_specs = [
        (
            "SURF_C01_FRONT",
            "C01_CENTER_CORE",
            "C01_CENTER_CORE",
        ),
        (
            "SURF_C02_FRONT",
            "C02_STONE_LEFT",
            "C02_STONE_LEFT",
        ),
        (
            "SURF_C03_FRONT",
            "C03_STONE_RIGHT",
            "C03_STONE_RIGHT",
        ),
    ]
    for instruction_id, component, owner_name in front_specs:
        record = build_front_surface(
            instruction_id,
            component,
            instruction_id,
            owner_rows(scanlines, "front", owner_name),
            -half_depth,
        )
        source_records.append(record)
        surface_report.append(
            {
                "instruction_id": instruction_id,
                "result": "PASS",
                "faces": len(record.faces),
                "source_owner": owner_name,
            }
        )

    axial_specs = [
        (
            "SURF_C02_TOP_HALF",
            "C02_STONE_LEFT",
            "top",
            "C02_STONE_LEFT",
            stone_top_z,
        ),
        (
            "SURF_C03_TOP_HALF",
            "C03_STONE_RIGHT",
            "top",
            "C03_STONE_RIGHT",
            stone_top_z,
        ),
        (
            "SURF_C02_BOTTOM_HALF",
            "C02_STONE_LEFT",
            "bottom",
            "C03_STONE_RIGHT",
            stone_bottom_z,
        ),
        (
            "SURF_C03_BOTTOM_HALF",
            "C03_STONE_RIGHT",
            "bottom",
            "C02_STONE_LEFT",
            stone_bottom_z,
        ),
    ]
    for (
        instruction_id,
        component,
        plane,
        stored_owner,
        world_z,
    ) in axial_specs:
        record = build_axial_surface(
            instruction_id,
            component,
            instruction_id,
            owner_rows(scanlines, plane, stored_owner),
            plane,
            world_z,
            half_depth,
        )
        source_records.append(record)
        surface_report.append(
            {
                "instruction_id": instruction_id,
                "result": "PASS",
                "faces": len(record.faces),
                "stored_source_owner": stored_owner,
                "step11c_logical_mapping_applied": plane == "bottom",
            }
        )

    rotational_specs = [
        ("SURF_C06_ROTATIONAL_HALF", "C06_UPPER_HAFT_CAP"),
        ("SURF_C07_ROTATIONAL_HALF", "C07_HAFT"),
        (
            "SURF_C07B_ROTATIONAL_HALF",
            "C07B_HAFT_TO_HANDLE_FERRULE",
        ),
        ("SURF_C08_ROTATIONAL_HALF", "C08_GRIP"),
        ("SURF_C09_ROTATIONAL_HALF", "C09_LOWER_COLLAR"),
        ("SURF_C10_ROTATIONAL_HALF", "C10_POMMEL_BODY"),
        ("SURF_C11_ROTATIONAL_HALF", "C11_POMMEL_TERMINAL_CAP"),
        (
            "SURF_C12_ROTATIONAL_HALF",
            "C12_UPPER_HEAD_CAP_SPIRE",
        ),
    ]
    rotational_records: dict[str, MeshRecord] = {}
    rotational_metadata: dict[str, dict[str, Any]] = {}
    for instruction_id, component in rotational_specs:
        rows, terminal = source_rows_for_rotational_component(
            component,
            scanlines,
            step06_front,
        )
        record, metadata = build_rotational_surface(
            instruction_id,
            component,
            rows,
            terminal,
        )
        source_records.append(record)
        rotational_records[component] = record
        rotational_metadata[component] = metadata
        surface_report.append(
            {
                **metadata,
                "result": "PASS",
                "faces": len(record.faces),
            }
        )

    contact_report: list[dict[str, Any]] = []
    transition_to_instruction = {
        "TR_C01_C06": "CONTACT_C01_C06",
        "TR_C06_C07": "CONTACT_C06_C07",
        "TR_C07_C07B": "CONTACT_C07_C07B",
        "TR_C07B_C08": "CONTACT_C07B_C08",
        "TR_C08_C09": "CONTACT_C08_C09",
        "TR_C09_C10": "CONTACT_C09_C10",
        "TR_C10_C11": "CONTACT_C10_C11",
        "TR_C12_C01": "CONTACT_C12_C01",
    }
    for transition_id, instruction_id in transition_to_instruction.items():
        transition = blueprint["transition_catalog"][transition_id]
        upper_radius = exact(
            transition["upper_positive_radius"]["radius_cm"]
        )
        lower_radius = exact(
            transition["lower_positive_radius"]["radius_cm"]
        )
        if transition["same_radius"]:
            contact_report.append(
                {
                    "instruction_id": instruction_id,
                    "result": "PASS",
                    "method": "coordinate_equal_common_half_ring",
                    "faces": 0,
                    "duplicate_wall_created": False,
                }
            )
            continue
        shoulder = build_half_annular_shoulder(
            instruction_id,
            f"{transition['upper_component']}_{transition['lower_component']}",
            exact(transition["shared_world_z_cm"]),
            upper_radius,
            lower_radius,
        )
        source_records.append(shoulder)
        contact_report.append(
            {
                "instruction_id": instruction_id,
                "result": "PASS",
                "method": "exact_planar_positive_x_half_annular_shoulder",
                "faces": len(shoulder.faces),
                "upper_radius_exact": qstr(upper_radius),
                "lower_radius_exact": qstr(lower_radius),
            }
        )

    c11_rows, _ = source_rows_for_rotational_component(
        "C11_POMMEL_TERMINAL_CAP",
        scanlines,
        step06_front,
    )
    c12_rows, _ = source_rows_for_rotational_component(
        "C12_UPPER_HEAD_CAP_SPIRE",
        scanlines,
        step06_front,
    )
    c11_radius = positive_radius_from_row(
        normalized_profile_rows(c11_rows)[-1]
    )
    c12_radius = positive_radius_from_row(
        normalized_profile_rows(c12_rows)[0]
    )
    bottom_cap = build_half_cap(
        "CAP_C11_BOTTOM",
        "C11_POMMEL_TERMINAL_CAP",
        Fraction(0),
        c11_radius,
        False,
    )
    top_cap = build_half_cap(
        "CAP_C12_TOP",
        "C12_UPPER_HEAD_CAP_SPIRE",
        Fraction(170),
        c12_radius,
        True,
    )
    source_records.extend((bottom_cap, top_cap))
    contact_report.extend(
        [
            {
                "instruction_id": "CAP_C11_BOTTOM",
                "result": "PASS",
                "faces": len(bottom_cap.faces),
                "radius_exact": qstr(c11_radius),
            },
            {
                "instruction_id": "CAP_C12_TOP",
                "result": "PASS",
                "faces": len(top_cap.faces),
                "radius_exact": qstr(c12_radius),
            },
        ]
    )

    # One whole-asset Rz180 completion for every source record built above.
    completed_records = list(source_records)
    for record in source_records:
        completed_records.append(
            record.rotated_rz180(
                f"{record.name}__RZ180",
                "WHOLE_ASSET_RZ180",
            )
        )

    inner_c02, inner_c03, stitch_metadata = build_stone_inner_closures(
        boundaries,
        half_depth,
        stone_top_z,
        stone_bottom_z,
    )
    outer_positive, outer_negative, outer_metadata = (
        build_c04_outer_closures(
            candidate,
            scanlines,
            half_depth,
            stone_top_z,
            stone_bottom_z,
        )
    )
    completed_records.extend(
        (inner_c02, inner_c03, outer_positive, outer_negative)
    )
    contact_report.extend(
        [
            {
                "instruction_id": "CLOSURE_C02_INNER",
                "result": "PASS",
                "faces": len(inner_c02.faces),
                "rule": "Step 11D completed perimeter",
            },
            {
                "instruction_id": "CLOSURE_C03_INNER",
                "result": "PASS",
                "faces": len(inner_c03.faces),
                "rule": "Step 11D completed perimeter",
            },
            {
                "instruction_id": outer_positive.instruction_id,
                "result": "PASS",
                "faces": len(outer_positive.faces)
                + len(outer_negative.faces),
                "rule": "EQ_ORDERED_RULED_FACE shared exterior boundary",
            },
            {
                "instruction_id": (
                    "CLOSURE_C03_TO_C04_METAL"
                    if candidate == "rune_side"
                    else "CLOSURE_C03_TO_C04_RUNE"
                ),
                "result": "NOT_APPLICABLE_TO_CANDIDATE",
                "faces": 0,
            },
            {
                "instruction_id": "GUARD_PROTECTED_NEGATIVE_SPACES",
                "result": "PASS",
                "faces": 0,
                "protected_space_fill_attempts": 0,
            },
            {
                "instruction_id": "WHOLE_ASSET_RZ180",
                "result": "PASS",
                "operation_count": 1,
                "source_record_count": len(source_records),
                "rotated_record_count": len(source_records),
            },
        ]
    )
    relevant_surface_ids = {
        record["id"]
        for record in blueprint["surface_instructions"]
        if candidate in record["candidate_variants"]
    }
    built_surface_ids = {item["instruction_id"] for item in surface_report}
    if built_surface_ids != relevant_surface_ids:
        raise RuntimeError(
            f"Surface instruction replay mismatch: "
            f"missing={sorted(relevant_surface_ids-built_surface_ids)} "
            f"extra={sorted(built_surface_ids-relevant_surface_ids)}"
        )
    return completed_records, {
        "candidate": candidate,
        "half_depth_exact": qstr(half_depth),
        "surface_instruction_report": surface_report,
        "closure_contact_instruction_report": contact_report,
        "rotational_metadata": rotational_metadata,
        "stone_stitch_metadata": stitch_metadata,
        "c04_outer_closure_metadata": outer_metadata,
        "whole_asset_rz180_count": 1,
        "c04_local_y_mirror_count": 1,
        "source_record_count_before_rz180": len(source_records),
        "completed_mesh_record_count": len(completed_records),
    }


def combined_exact_bounds(
    records: list[MeshRecord],
) -> dict[str, Any]:
    vertices = [
        point
        for record in records
        for point in record.vertices
    ]
    minimum = [
        min(point[axis] for point in vertices)
        for axis in range(3)
    ]
    maximum = [
        max(point[axis] for point in vertices)
        for axis in range(3)
    ]
    dimensions = [
        maximum[axis] - minimum[axis]
        for axis in range(3)
    ]
    return {
        "minimum_exact": [qstr(value) for value in minimum],
        "maximum_exact": [qstr(value) for value in maximum],
        "dimensions_exact": [qstr(value) for value in dimensions],
        "minimum_cm": [float(value) for value in minimum],
        "maximum_cm": [float(value) for value in maximum],
        "dimensions_cm": [float(value) for value in dimensions],
        "_minimum": minimum,
        "_maximum": maximum,
        "_dimensions": dimensions,
    }


def validate_pre_save_records(
    candidate: str,
    blueprint: dict[str, Any],
    records: list[MeshRecord],
    build_metadata: dict[str, Any],
) -> dict[str, Any]:
    bounds = combined_exact_bounds(records)
    expected_dimensions_record = blueprint["candidate_variants"][candidate][
        "completed_dimensions_cm"
    ]
    expected_dimensions = [
        exact(expected_dimensions_record["width"]),
        exact(expected_dimensions_record["depth"]),
        exact(expected_dimensions_record["height"]),
    ]
    checks = []

    def check(check_id: str, passed: bool, expected: Any, observed: Any) -> None:
        checks.append(
            {
                "id": check_id,
                "expected": expected,
                "observed": observed,
                "result": "PASS" if passed else "FAIL",
            }
        )

    expected_width = expected_dimensions[0]
    observed_width = bounds["_dimensions"][0]
    completed_width_difference = abs(observed_width - expected_width)
    expected_half_width = expected_width / 2
    negative_side_difference = abs(
        bounds["_minimum"][0] + expected_half_width
    )
    positive_side_difference = abs(
        bounds["_maximum"][0] - expected_half_width
    )
    maximum_side_difference = max(
        negative_side_difference,
        positive_side_difference,
    )
    per_side_source_pixels = maximum_side_difference / AXIAL_SCALE
    relative_width_difference = completed_width_difference / expected_width
    width_limit_results = {
        "per_side_source_pixels": per_side_source_pixels <= 1,
        "relative_difference": relative_width_difference <= Fraction(1, 400),
        "absolute_difference_cm": (
            completed_width_difference <= Fraction(1, 5)
        ),
    }
    cross_view_width_tolerance = {
        "expected_width_cm_exact": qstr(expected_width),
        "observed_width_cm_exact": qstr(observed_width),
        "completed_difference_cm_exact": qstr(
            completed_width_difference
        ),
        "negative_side_difference_cm_exact": qstr(
            negative_side_difference
        ),
        "positive_side_difference_cm_exact": qstr(
            positive_side_difference
        ),
        "axial_pixel_scale_cm_exact": qstr(AXIAL_SCALE),
        "maximum_per_side_source_pixels_exact": qstr(
            per_side_source_pixels
        ),
        "completed_relative_difference_exact": qstr(
            relative_width_difference
        ),
        "thresholds_exact": {
            "maximum_per_side_source_pixels": "1/1",
            "maximum_relative_difference": "1/400",
            "maximum_absolute_difference_cm": "1/5",
        },
        "limit_results": width_limit_results,
        "all_limits_pass": all(width_limit_results.values()),
        "measured_geometry_clipped": False,
    }
    check(
        "BUILD-CROSS-VIEW-WIDTH-TOLERANCE",
        all(width_limit_results.values()),
        cross_view_width_tolerance["thresholds_exact"],
        cross_view_width_tolerance,
    )
    check(
        "BUILD-EXACT-DEPTH-HEIGHT-CENTER",
        bounds["_dimensions"][1:] == expected_dimensions[1:]
        and bounds["_minimum"][2] == 0
        and bounds["_maximum"][2] == 170
        and bounds["_minimum"][0] + bounds["_maximum"][0] == 0
        and bounds["_minimum"][1] + bounds["_maximum"][1] == 0,
        {
            "depth_exact": qstr(expected_dimensions[1]),
            "height_exact": qstr(expected_dimensions[2]),
            "center_x_exact": "0/1",
            "center_y_exact": "0/1",
            "minimum_z_exact": "0/1",
        },
        {
            "depth_exact": qstr(bounds["_dimensions"][1]),
            "height_exact": qstr(bounds["_dimensions"][2]),
            "center_x_exact": qstr(
                (bounds["_minimum"][0] + bounds["_maximum"][0]) / 2
            ),
            "center_y_exact": qstr(
                (bounds["_minimum"][1] + bounds["_maximum"][1]) / 2
            ),
            "minimum_z_exact": qstr(bounds["_minimum"][2]),
        },
    )
    check(
        "BUILD-PIVOT-AND-HEIGHT",
        bounds["_minimum"][2] == 0 and bounds["_maximum"][2] == 170,
        ["Zmin=0", "Zmax=170"],
        [
            qstr(bounds["_minimum"][2]),
            qstr(bounds["_maximum"][2]),
        ],
    )
    check(
        "BUILD-ANGULAR-DIVISIONS",
        all(
            metadata["angular_divisions_positive_x"]
            == ANGULAR_DIVISIONS
            for metadata in build_metadata["rotational_metadata"].values()
        ),
        ANGULAR_DIVISIONS,
        sorted(
            {
                metadata["angular_divisions_positive_x"]
                for metadata in build_metadata[
                    "rotational_metadata"
                ].values()
            }
        ),
    )
    check(
        "BUILD-C04-LOCAL-MIRROR",
        build_metadata["c04_local_y_mirror_count"] == 1,
        1,
        build_metadata["c04_local_y_mirror_count"],
    )
    check(
        "BUILD-WHOLE-RZ180",
        build_metadata["whole_asset_rz180_count"] == 1,
        1,
        build_metadata["whole_asset_rz180_count"],
    )
    check(
        "BUILD-NONEMPTY-RECORDS",
        all(record.faces and record.vertices for record in records),
        "every emitted mesh record nonempty",
        [
            record.name
            for record in records
            if not record.faces or not record.vertices
        ],
    )
    check(
        "BUILD-NO-DEGENERATE-FACE-INDICES",
        all(
            len(face) == len(set(face))
            for record in records
            for face in record.faces
        ),
        0,
        sum(
            len(face) != len(set(face))
            for record in records
            for face in record.faces
        ),
    )
    zero_area_faces = [
        {
            "object": record.name,
            "face_index": face_index,
        }
        for record in records
        if record.material_key in {"CLOSURE", "CONTACT"}
        for face_index, face in enumerate(record.faces)
        if polygon_normal([record.vertices[index] for index in face])
        == (0, 0, 0)
    ]
    check(
        "BUILD-NO-EXACT-ZERO-AREA-FACES",
        not zero_area_faces,
        [],
        zero_area_faces,
    )
    failures = [item for item in checks if item["result"] != "PASS"]
    if failures:
        raise RuntimeError(
            "Pre-save candidate validation failed: "
            + ", ".join(item["id"] for item in failures)
        )
    return {
        "result": "PASS",
        "checks": checks,
        "bounds": {
            key: value
            for key, value in bounds.items()
            if not key.startswith("_")
        },
        "mesh_records": len(records),
        "vertices": sum(len(record.vertices) for record in records),
        "polygons": sum(len(record.faces) for record in records),
        "triangles_observed_not_gated": sum(
            record.triangle_count for record in records
        ),
        "high_poly_nanite_amendment_applied": True,
        "cross_view_width_tolerance": cross_view_width_tolerance,
    }


def write_canonical_geometry(
    path: Path,
    candidate: str,
    records: list[MeshRecord],
    pre_save: dict[str, Any],
) -> None:
    with gzip.open(path, "wt", encoding="utf-8", compresslevel=9) as handle:
        handle.write("{")
        handle.write(
            '"schema":"AERATHEA_R8_STEP12_CANONICAL_GEOMETRY_A01_V1",'
        )
        handle.write(f'"asset":{json.dumps(ASSET)},')
        handle.write(f'"run_id":{json.dumps(RUN_ID)},')
        handle.write(f'"candidate":{json.dumps(candidate)},')
        handle.write('"coordinate_unit":"centimeter",')
        handle.write('"coordinate_encoding":"exact numerator/denominator",')
        handle.write(
            '"transforms":"identity; all coordinates serialized in world space",'
        )
        handle.write(
            f'"pivot_exact":{json.dumps(["0/1", "0/1", "0/1"])},'
        )
        handle.write(
            f'"bounds":{json.dumps(pre_save["bounds"], sort_keys=True)},'
        )
        handle.write('"objects":[')
        for object_index, record in enumerate(records):
            if object_index:
                handle.write(",")
            header = {
                "name": record.name,
                "component": record.component,
                "instruction_id": record.instruction_id,
                "occurrence": record.occurrence,
                "smooth": record.smooth,
                "material_key": record.material_key,
                "vertex_count": len(record.vertices),
                "polygon_count": len(record.faces),
                "triangle_count": record.triangle_count,
            }
            handle.write("{")
            for index, (key, value) in enumerate(header.items()):
                if index:
                    handle.write(",")
                handle.write(json.dumps(key))
                handle.write(":")
                json.dump(value, handle, separators=(",", ":"))
            handle.write(',"vertices_exact":[')
            for vertex_index, point in enumerate(record.vertices):
                if vertex_index:
                    handle.write(",")
                json.dump(
                    [qstr(value) for value in point],
                    handle,
                    separators=(",", ":"),
                )
            handle.write('],"faces":')
            json.dump(record.faces, handle, separators=(",", ":"))
            handle.write("}")
        handle.write("]}")
        handle.write("\n")


def clear_blender_scene(bpy: Any) -> None:
    bpy.ops.object.select_all(action="SELECT")
    bpy.ops.object.delete(use_global=False)
    for blocks in (
        bpy.data.meshes,
        bpy.data.materials,
        bpy.data.cameras,
        bpy.data.lights,
        bpy.data.curves,
    ):
        for block in list(blocks):
            if block.users == 0:
                blocks.remove(block)


def configure_blender_scene(bpy: Any, candidate: str) -> None:
    scene = bpy.context.scene
    scene.unit_settings.system = "METRIC"
    scene.unit_settings.length_unit = "CENTIMETERS"
    scene.unit_settings.scale_length = 0.01
    scene.render.engine = "CYCLES"
    scene.cycles.device = "CPU"
    scene.cycles.samples = 32
    scene.cycles.use_adaptive_sampling = False
    scene.cycles.use_denoising = False
    scene.render.resolution_x = 512
    scene.render.resolution_y = 512
    scene.render.resolution_percentage = 100
    scene.render.image_settings.file_format = "PNG"
    scene.render.image_settings.color_mode = "RGBA"
    scene.render.image_settings.color_depth = "8"
    scene.view_settings.view_transform = "Standard"
    scene.view_settings.look = "None"
    scene.view_settings.exposure = 0.0
    scene.view_settings.gamma = 1.0
    scene["Aerathea.Asset"] = ASSET
    scene["Aerathea.RunID"] = RUN_ID
    scene["Aerathea.Candidate"] = candidate
    scene["Aerathea.ArtifactStatus"] = "DCC source candidate"
    scene["Aerathea.HighPolyNaniteStage"] = True
    scene["Aerathea.AngularDivisionsPositiveX"] = ANGULAR_DIVISIONS
    scene["Aerathea.C04LocalYMirrorCount"] = 1
    scene["Aerathea.WholeAssetRz180Count"] = 1
    scene["Aerathea.ExtrusionUsed"] = False
    scene["Aerathea.SolidifyUsed"] = False
    scene["Aerathea.Step13Authorized"] = False
    scene["Aerathea.UnrealAuthorized"] = False
    scene["Aerathea.NetworkOperations"] = 0


def make_material(
    bpy: Any,
    name: str,
    color: tuple[float, float, float, float],
) -> Any:
    material = bpy.data.materials.get(name)
    if material is not None:
        return material
    material = bpy.data.materials.new(name)
    material.use_nodes = True
    bsdf = material.node_tree.nodes.get("Principled BSDF")
    bsdf.inputs["Base Color"].default_value = color
    bsdf.inputs["Roughness"].default_value = 0.72
    bsdf.inputs["Metallic"].default_value = (
        0.62
        if "STONE" not in name and "GRIP" not in name
        else 0.02
    )
    return material


def create_blender_object(
    bpy: Any,
    record: MeshRecord,
    candidate: str,
    materials: dict[str, Any],
) -> Any:
    mesh = bpy.data.meshes.new(f"{record.name}_MESH")
    mesh.from_pydata(
        [f3(point) for point in record.vertices],
        [],
        record.faces,
    )
    mesh.update(calc_edges=True)
    obj = bpy.data.objects.new(record.name, mesh)
    bpy.context.scene.collection.objects.link(obj)
    obj.location = (0.0, 0.0, 0.0)
    obj.rotation_euler = (0.0, 0.0, 0.0)
    obj.scale = (1.0, 1.0, 1.0)
    obj["aet_asset"] = ASSET
    obj["aet_run_id"] = RUN_ID
    obj["aet_candidate"] = candidate
    obj["aet_component_id"] = record.component
    obj["aet_instruction_id"] = record.instruction_id
    obj["aet_occurrence"] = record.occurrence
    obj["aet_source_derived"] = True
    obj["aet_extrusion_used"] = False
    obj["aet_backing_surface"] = False
    obj["aet_triangle_count"] = record.triangle_count
    material = materials[record.material_key]
    obj.data.materials.append(material)
    for polygon in mesh.polygons:
        polygon.material_index = 0
        polygon.use_smooth = record.smooth
    return obj


def internal_build(args: argparse.Namespace) -> int:
    import bpy  # type: ignore

    blueprint_path = args.blueprint.resolve()
    output_root = args.output_root.resolve()
    blueprint, authority_checks = verify_authority(
        blueprint_path,
        args.amendment.resolve(),
        args.parity_amendment.resolve(),
        args.stitch_amendment.resolve(),
        args.tolerance_amendment.resolve(),
    )
    paths = {
        key: ROOT / record["path"]
        for key, record in blueprint["authority_files"].items()
    }
    scanlines = load_gzip_json(paths["step09a_scanlines"])
    boundaries = load_json(paths["step09a_boundaries"])
    step06_front = load_json(paths["step06_front"])
    records, build_metadata = build_candidate_records(
        args.candidate,
        blueprint,
        scanlines,
        boundaries,
        step06_front,
    )
    pre_save = validate_pre_save_records(
        args.candidate,
        blueprint,
        records,
        build_metadata,
    )

    clear_blender_scene(bpy)
    configure_blender_scene(bpy, args.candidate)
    material_keys = sorted({record.material_key for record in records})
    materials = {
        key: make_material(
            bpy,
            f"M_STEP12_PROOF_{key}",
            COMPONENT_COLORS.get(key, COMPONENT_COLORS["CLOSURE"]),
        )
        for key in material_keys
    }
    for record in records:
        create_blender_object(bpy, record, args.candidate, materials)

    blend_path = output_root / (
        f"{ASSET}_{args.candidate}_DCCSourceCandidate.blend"
    )
    canonical_path = output_root / "canonical_geometry.json.gz"
    build_manifest_path = output_root / "build_manifest.json"
    pre_save_path = output_root / "pre_save_validation.json"

    write_canonical_geometry(
        canonical_path,
        args.candidate,
        records,
        pre_save,
    )
    pre_save_path.write_text(
        json.dumps(pre_save, indent=2, sort_keys=True) + "\n",
        encoding="utf-8",
    )
    bpy.context.scene["Aerathea.CanonicalGeometrySHA256"] = sha256(
        canonical_path
    )
    bpy.context.scene["Aerathea.PreSaveValidationSHA256"] = sha256(
        pre_save_path
    )
    bpy.context.scene["Aerathea.MeshObjectCount"] = len(records)
    bpy.context.scene["Aerathea.TrianglesObserved"] = pre_save[
        "triangles_observed_not_gated"
    ]
    bpy.ops.wm.save_as_mainfile(filepath=str(blend_path), check_existing=False)

    build_manifest = {
        "schema": "AERATHEA_R8_STEP12_CANDIDATE_BUILD_MANIFEST_A01_V1",
        "asset": ASSET,
        "run_id": RUN_ID,
        "candidate": args.candidate,
        "artifact_status": "candidate pending independent saved-file audit",
        "created_utc": utc_now(),
        "authority_checks": authority_checks,
        "authority_check_count": len(authority_checks),
        "authority_failures": 0,
        "build_metadata": build_metadata,
        "pre_save_validation": pre_save,
        "files": {
            "blend": {
                "path": relative(blend_path),
                "sha256": sha256(blend_path),
            },
            "canonical_geometry": {
                "path": relative(canonical_path),
                "sha256": sha256(canonical_path),
            },
            "pre_save_validation": {
                "path": relative(pre_save_path),
                "sha256": sha256(pre_save_path),
            },
        },
        "forbidden_methods": {
            "extrusion": False,
            "solidify": False,
            "primitive_replacement": False,
            "old_mesh_import": False,
            "old_coordinate_read": False,
            "source_resampling": False,
            "tolerance_weld": False,
            "backing_plate": False,
        },
        "polygon_limit_enforced": False,
        "polygon_limit_reason": (
            "Step 11B high-poly/Nanite amendment; count observed only"
        ),
        "step13_authorized": False,
        "unreal_authorized": False,
    }
    build_manifest_path.write_text(
        json.dumps(build_manifest, indent=2, sort_keys=True) + "\n",
        encoding="utf-8",
    )
    print(
        json.dumps(
            {
                "candidate": args.candidate,
                "blend": relative(blend_path),
                "triangles": pre_save["triangles_observed_not_gated"],
                "objects": len(records),
                "result": "BUILT_PENDING_INDEPENDENT_AUDIT",
            },
            sort_keys=True,
        )
    )
    return 0


def look_at(camera: Any, target: tuple[float, float, float]) -> None:
    from mathutils import Vector  # type: ignore

    direction = Vector(target) - camera.location
    camera.rotation_euler = direction.to_track_quat("-Z", "Y").to_euler()


def proof_material(
    bpy: Any,
    name: str,
    base_color: tuple[float, float, float, float],
    wireframe: bool = False,
) -> Any:
    material = bpy.data.materials.get(name)
    if material is not None:
        return material
    material = bpy.data.materials.new(name)
    material.use_nodes = True
    nodes = material.node_tree.nodes
    links = material.node_tree.links
    nodes.clear()
    output = nodes.new("ShaderNodeOutputMaterial")
    bsdf = nodes.new("ShaderNodeBsdfPrincipled")
    bsdf.inputs["Base Color"].default_value = base_color
    bsdf.inputs["Roughness"].default_value = 0.78
    if not wireframe:
        links.new(bsdf.outputs["BSDF"], output.inputs["Surface"])
        return material
    wire = nodes.new("ShaderNodeWireframe")
    wire.inputs["Size"].default_value = 0.25
    line_bsdf = nodes.new("ShaderNodeBsdfPrincipled")
    line_bsdf.inputs["Base Color"].default_value = (0.02, 0.04, 0.06, 1.0)
    line_bsdf.inputs["Roughness"].default_value = 0.5
    mix = nodes.new("ShaderNodeMixShader")
    links.new(wire.outputs["Fac"], mix.inputs[0])
    links.new(bsdf.outputs["BSDF"], mix.inputs[1])
    links.new(line_bsdf.outputs["BSDF"], mix.inputs[2])
    links.new(mix.outputs["Shader"], output.inputs["Surface"])
    return material


def configure_render_world(bpy: Any) -> None:
    scene = bpy.context.scene
    scene.render.engine = "CYCLES"
    scene.cycles.device = "CPU"
    scene.cycles.samples = 32
    scene.cycles.use_adaptive_sampling = False
    scene.cycles.use_denoising = False
    scene.render.resolution_x = 512
    scene.render.resolution_y = 512
    scene.render.resolution_percentage = 100
    scene.render.image_settings.file_format = "PNG"
    scene.render.image_settings.color_mode = "RGBA"
    scene.render.image_settings.color_depth = "8"
    scene.view_settings.view_transform = "Standard"
    scene.view_settings.look = "None"
    scene.view_settings.exposure = 0.0
    scene.view_settings.gamma = 1.0
    scene.world.use_nodes = True
    background = scene.world.node_tree.nodes.get("Background")
    background.inputs["Color"].default_value = (0.78, 0.80, 0.83, 1.0)
    background.inputs["Strength"].default_value = 0.75
    for obj in list(bpy.data.objects):
        if obj.type in {"CAMERA", "LIGHT"}:
            bpy.data.objects.remove(obj, do_unlink=True)
    light_specs = [
        ("KEY", (150.0, -180.0, 250.0), 1500.0, 120.0),
        ("FILL", (-180.0, -80.0, 140.0), 850.0, 100.0),
        ("RIM", (80.0, 180.0, 220.0), 1200.0, 100.0),
    ]
    for name, location, energy, size in light_specs:
        data = bpy.data.lights.new(f"STEP12_{name}", "AREA")
        data.energy = energy
        data.shape = "DISK"
        data.size = size
        obj = bpy.data.objects.new(f"STEP12_{name}", data)
        bpy.context.scene.collection.objects.link(obj)
        obj.location = location
        look_at(obj, (0.0, 0.0, 85.0))
    camera_data = bpy.data.cameras.new("STEP12_CAMERA")
    camera_data.type = "ORTHO"
    camera_data.ortho_scale = 185.0
    camera = bpy.data.objects.new("STEP12_CAMERA", camera_data)
    bpy.context.scene.collection.objects.link(camera)
    scene.camera = camera


def set_camera_view(
    bpy: Any,
    view: str,
    azimuth_degrees: float | None = None,
) -> None:
    camera = bpy.context.scene.camera
    target = (0.0, 0.0, 85.0)
    positions = {
        "front": (0.0, -300.0, 85.0),
        "back": (0.0, 300.0, 85.0),
        "right": (300.0, 0.0, 85.0),
        "left": (-300.0, 0.0, 85.0),
        "top": (0.0, 0.0, 385.0),
        "bottom": (0.0, 0.0, -215.0),
        "three_quarter": (225.0, -255.0, 205.0),
    }
    if azimuth_degrees is not None:
        angle = math.radians(azimuth_degrees)
        radius = 330.0
        camera.location = (
            radius * math.cos(angle),
            radius * math.sin(angle),
            150.0,
        )
    else:
        camera.location = positions[view]
    look_at(camera, target)


def render_proof(
    bpy: Any,
    output: Path,
    material: Any,
    view: str,
    azimuth_degrees: float | None = None,
) -> None:
    scene = bpy.context.scene
    scene.view_layers[0].material_override = material
    set_camera_view(bpy, view, azimuth_degrees)
    scene.render.filepath = str(output)
    bpy.ops.render.render(write_still=True)


def internal_render(args: argparse.Namespace) -> int:
    import bpy  # type: ignore

    audit_path = args.output_root / "independent_saved_candidate_audit.json"
    audit = load_json(audit_path)
    if audit.get("result") != "PASS":
        raise RuntimeError("Independent saved-candidate audit is not PASS")
    configure_render_world(bpy)
    clay = proof_material(
        bpy,
        "M_STEP12_TEMP_NEUTRAL_CLAY",
        (0.42, 0.45, 0.49, 1.0),
    )
    silhouette = proof_material(
        bpy,
        "M_STEP12_TEMP_BINARY_SILHOUETTE",
        (0.005, 0.005, 0.005, 1.0),
    )
    wire = proof_material(
        bpy,
        "M_STEP12_TEMP_WIREFRAME",
        (0.38, 0.42, 0.46, 1.0),
        wireframe=True,
    )
    render_root = args.output_root / "renders"
    for view in ("front", "back", "left", "right", "top", "bottom"):
        render_proof(
            bpy,
            render_root / f"silhouette_{view}.png",
            silhouette,
            view,
        )
        render_proof(
            bpy,
            render_root / f"clay_{view}.png",
            clay,
            view,
        )
    render_proof(
        bpy,
        render_root / "clay_three_quarter.png",
        clay,
        "three_quarter",
    )
    render_proof(
        bpy,
        render_root / "wireframe_contact_three_quarter.png",
        wire,
        "three_quarter",
    )
    for index in range(8):
        render_proof(
            bpy,
            render_root / f"parallax_{index:03d}.png",
            clay,
            "three_quarter",
            azimuth_degrees=-90.0 + index * 45.0,
        )
    bpy.context.scene.view_layers[0].material_override = None
    print(
        json.dumps(
            {
                "candidate": args.candidate,
                "render_root": relative(render_root),
                "silhouette_renders": 6,
                "clay_renders": 7,
                "wireframe_renders": 1,
                "parallax_frames": 8,
                "result": "REVIEW_RENDERS_COMPLETE",
            },
            sort_keys=True,
        )
    )
    return 0


def planned_candidate_files(candidate: str) -> list[str]:
    render_names = [
        *(f"renders/silhouette_{view}.png" for view in (
            "front",
            "back",
            "left",
            "right",
            "top",
            "bottom",
        )),
        *(f"renders/clay_{view}.png" for view in (
            "front",
            "back",
            "left",
            "right",
            "top",
            "bottom",
        )),
        "renders/clay_three_quarter.png",
        "renders/wireframe_contact_three_quarter.png",
        *(f"renders/parallax_{index:03d}.png" for index in range(8)),
        "renders/parallax_strip.png",
    ]
    return [
        "OUTPUT_INVENTORY.json",
        f"{ASSET}_{candidate}_DCCSourceCandidate.blend",
        "canonical_geometry.json.gz",
        "pre_save_validation.json",
        "build_manifest.json",
        "independent_saved_candidate_audit.json",
        *render_names,
    ]


def write_output_inventory(output_root: Path, candidate: str) -> None:
    output_root.mkdir(parents=True, exist_ok=False)
    (output_root / "renders").mkdir()
    inventory = {
        "schema": "AERATHEA_R8_STEP12_OUTPUT_INVENTORY_A01_V1",
        "asset": ASSET,
        "run_id": RUN_ID,
        "candidate": candidate,
        "artifact_status": "authoritative planned candidate-local inventory",
        "written_before_candidate_outputs": True,
        "allowed_relative_files": planned_candidate_files(candidate),
        "step13_authorized": False,
        "unreal_authorized": False,
    }
    (output_root / "OUTPUT_INVENTORY.json").write_text(
        json.dumps(inventory, indent=2, sort_keys=True) + "\n",
        encoding="utf-8",
    )


def blender_command(
    blender: Path,
    script: Path,
    script_args: list[str],
    blend: Path | None = None,
) -> list[str]:
    command = [str(blender), "--background"]
    if blend is None:
        command.append("--factory-startup")
    else:
        command.append(str(blend))
    command.extend(["--python", str(script), "--", *script_args])
    return command


def run_checked(command: list[str], environment: dict[str, str]) -> None:
    completed = subprocess.run(
        command,
        cwd=ROOT,
        env=environment,
        check=False,
    )
    if completed.returncode != 0:
        raise RuntimeError(
            f"Command failed with exit code {completed.returncode}: "
            + " ".join(command[:5])
        )


def compose_parallax_strip(output_root: Path) -> None:
    from PIL import Image, ImageOps  # type: ignore

    frames = [
        Image.open(output_root / "renders" / f"parallax_{index:03d}.png").convert(
            "RGB"
        )
        for index in range(8)
    ]
    thumbs = [ImageOps.fit(frame, (256, 256)) for frame in frames]
    strip = Image.new("RGB", (4 * 256, 2 * 256), (28, 32, 37))
    for index, image in enumerate(thumbs):
        strip.paste(image, ((index % 4) * 256, (index // 4) * 256))
    strip.save(output_root / "renders" / "parallax_strip.png")
    for frame in frames:
        frame.close()


def candidate_root_from_lock(
    environment_lock: dict[str, Any],
    candidate: str,
) -> Path:
    return ROOT / environment_lock["candidate_roots"][candidate]


def finalize_candidate_manifest(output_root: Path) -> None:
    manifest_path = output_root / "build_manifest.json"
    manifest = load_json(manifest_path)
    audit_path = output_root / "independent_saved_candidate_audit.json"
    audit = load_json(audit_path)
    if audit["result"] != "PASS":
        raise RuntimeError("Cannot finalize a candidate whose audit did not pass")
    inventory = load_json(output_root / "OUTPUT_INVENTORY.json")
    file_records = []
    for relative_file in inventory["allowed_relative_files"]:
        if relative_file == "build_manifest.json":
            continue
        path = output_root / relative_file
        if not path.is_file():
            raise RuntimeError(f"Planned candidate output is missing: {path}")
        file_records.append(
            {
                "path": relative(path),
                "sha256": sha256(path),
                "bytes": path.stat().st_size,
            }
        )
    manifest["artifact_status"] = "DCC source candidate"
    manifest["independent_saved_candidate_audit"] = {
        "path": relative(audit_path),
        "sha256": sha256(audit_path),
        "result": "PASS",
        "checks_passed": audit["summary"]["passed"],
        "checks_failed": audit["summary"]["failed"],
    }
    manifest["proof_render_gate"] = {
        "pre_render_audit_passed": True,
        "fixed_silhouette_renders": 6,
        "neutral_clay_renders": 7,
        "wireframe_contact_sets": 1,
        "parallax_frames": 8,
        "production_materials_created": False,
    }
    manifest["final_candidate_files"] = file_records
    manifest["manifest_self_hash_policy"] = (
        "build_manifest.json is intentionally excluded from its own "
        "final_candidate_files hash list because a stable recursive "
        "self-hash is impossible"
    )
    manifest["step13_authorized"] = False
    manifest["unreal_authorized"] = False
    manifest_path.write_text(
        json.dumps(manifest, indent=2, sort_keys=True) + "\n",
        encoding="utf-8",
    )


def compose_review_board() -> Path:
    from PIL import Image, ImageDraw, ImageFont, ImageOps  # type: ignore

    environment_lock = load_json(ENVIRONMENT_LOCK)
    roots = {
        candidate: candidate_root_from_lock(environment_lock, candidate)
        for candidate in CANDIDATES
    }
    validations = {}
    for candidate, root in roots.items():
        audit = load_json(root / "independent_saved_candidate_audit.json")
        if audit["result"] != "PASS":
            raise RuntimeError(f"{candidate} is not independently audited")
        validation = load_json(root / "pre_save_validation.json")
        tolerance = validation["cross_view_width_tolerance"]
        if (
            validation["result"] != "PASS"
            or not tolerance["all_limits_pass"]
            or tolerance["measured_geometry_clipped"]
        ):
            raise RuntimeError(
                f"{candidate} does not satisfy the approved width tolerance"
            )
        validations[candidate] = validation
    panel_specs = [
        ("clay_three_quarter.png", "NEUTRAL CLAY 3/4"),
        ("clay_front.png", "FRONT"),
        ("clay_right.png", "RIGHT"),
        ("clay_top.png", "TOP"),
        ("wireframe_contact_three_quarter.png", "WIRE / CONTACT"),
    ]
    width = 2560
    height = 1320
    board = Image.new("RGB", (width, height), (23, 27, 32))
    draw = ImageDraw.Draw(board)
    font_path = Path("/usr/share/fonts/truetype/dejavu/DejaVuSans.ttf")
    bold_path = Path("/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf")
    title_font = ImageFont.truetype(str(bold_path), 40)
    subtitle_font = ImageFont.truetype(str(font_path), 24)
    label_font = ImageFont.truetype(str(bold_path), 21)
    small_font = ImageFont.truetype(str(font_path), 18)
    draw.text(
        (36, 24),
        "SIEGE BREAKER — STEP 12 HIGH-POLY SOURCE CANDIDATES",
        font=title_font,
        fill=(239, 242, 245),
    )
    draw.text(
        (38, 78),
        (
            "UE5 Nanite target • polygon count observed, not limited • "
            "exact R8 source ownership • one local Y mirror • one Rz180"
        ),
        font=subtitle_font,
        fill=(140, 198, 238),
    )
    draw.text(
        (38, 112),
        (
            "PROOF ONLY for visual comparison — no Step 13, UV, bake, "
            "export, or Unreal work authorized"
        ),
        font=subtitle_font,
        fill=(238, 184, 94),
    )
    panel_w = 474
    panel_h = 474
    gap = 22
    left = 36
    row_tops = [190, 745]
    headings = {
        "rune_side": "CANDIDATE A — RUNE SIDE",
        "metal_center_piece_side": (
            "CANDIDATE B — METAL CENTER PIECE SIDE"
        ),
    }
    for row_index, candidate in enumerate(CANDIDATES):
        row_top = row_tops[row_index]
        heading = headings[candidate]
        dimensions_cm = validations[candidate]["bounds"]["dimensions_cm"]
        dimensions = (
            "observed W×D×H "
            f"{dimensions_cm[0]:.12f} × {dimensions_cm[1]:.12f} × "
            f"{dimensions_cm[2]:.0f} cm • width tolerance PASS"
        )
        draw.text(
            (left, row_top - 46),
            heading,
            font=label_font,
            fill=(239, 242, 245),
        )
        draw.text(
            (width - 36, row_top - 46),
            dimensions,
            font=small_font,
            fill=(173, 180, 188),
            anchor="ra",
        )
        for column, (filename, label) in enumerate(panel_specs):
            x = left + column * (panel_w + gap)
            source = Image.open(
                roots[candidate] / "renders" / filename
            ).convert("RGB")
            panel = ImageOps.fit(source, (panel_w, panel_h))
            board.paste(panel, (x, row_top))
            draw.rectangle(
                (x, row_top, x + panel_w - 1, row_top + panel_h - 1),
                outline=(92, 104, 116),
                width=2,
            )
            draw.rectangle(
                (x, row_top + panel_h - 42, x + panel_w, row_top + panel_h),
                fill=(18, 22, 27),
            )
            draw.text(
                (x + 14, row_top + panel_h - 34),
                label,
                font=small_font,
                fill=(231, 235, 239),
            )
            source.close()
    output = (
        PROOF_ROOT
        / "review/STEP_12_FRESH_DCC_SOURCE_GEOMETRY_A01_REVIEW_BOARD.png"
    )
    output.parent.mkdir(parents=True, exist_ok=True)
    board.save(output)
    return output


def external_build(args: argparse.Namespace) -> int:
    blueprint, _ = verify_authority(
        args.blueprint.resolve(),
        args.amendment.resolve(),
        args.parity_amendment.resolve(),
        args.stitch_amendment.resolve(),
        args.tolerance_amendment.resolve(),
    )
    del blueprint
    environment_lock = load_json(ENVIRONMENT_LOCK)
    expected_root = candidate_root_from_lock(
        environment_lock,
        args.candidate,
    ).resolve()
    output_root = args.output_root.resolve()
    if output_root != expected_root:
        raise RuntimeError(
            f"Output root mismatch: expected {expected_root}, got {output_root}"
        )
    if output_root.exists():
        raise RuntimeError(
            "Blueprint block: rule missing — approved clean output root "
            f"is not fresh: {output_root}"
        )
    blender = (ROOT / environment_lock["blender"]["binary_path"]).resolve()
    verify_hash(
        blender,
        environment_lock["blender"]["binary_sha256"],
        "blender_binary",
    )
    write_output_inventory(output_root, args.candidate)
    environment = dict(os.environ)
    environment["AET_NETWORK_DISABLED"] = "1"
    environment["PYTHONHASHSEED"] = "0"
    environment["LC_ALL"] = "C.UTF-8"

    common = [
        "--blueprint",
        str(args.blueprint.resolve()),
        "--amendment",
        str(args.amendment.resolve()),
        "--parity-amendment",
        str(args.parity_amendment.resolve()),
        "--stitch-amendment",
        str(args.stitch_amendment.resolve()),
        "--tolerance-amendment",
        str(args.tolerance_amendment.resolve()),
        "--candidate",
        args.candidate,
        "--output-root",
        str(output_root),
    ]
    run_checked(
        blender_command(
            blender,
            Path(__file__).resolve(),
            ["--internal-build", *common],
        ),
        environment,
    )
    blend = output_root / (
        f"{ASSET}_{args.candidate}_DCCSourceCandidate.blend"
    )
    required_build_outputs = [
        blend,
        output_root / "canonical_geometry.json.gz",
        output_root / "pre_save_validation.json",
        output_root / "build_manifest.json",
    ]
    missing_build_outputs = [
        str(path) for path in required_build_outputs if not path.is_file()
    ]
    if missing_build_outputs:
        raise RuntimeError(
            "Internal Blender build did not produce its complete gated "
            "output set; saved-file audit and rendering remain locked. "
            f"Missing: {missing_build_outputs}"
        )
    audit_path = output_root / "independent_saved_candidate_audit.json"
    run_checked(
        blender_command(
            blender,
            INDEPENDENT_AUDITOR,
            [
                "--saved-candidate",
                str(blend),
                "--candidate",
                args.candidate,
                "--audit-output",
                str(audit_path),
                *common[:10],
            ],
            blend=blend,
        ),
        environment,
    )
    audit = load_json(audit_path)
    if audit["result"] != "PASS":
        raise RuntimeError("Independent saved-candidate audit failed")
    run_checked(
        blender_command(
            blender,
            Path(__file__).resolve(),
            ["--internal-render", *common],
            blend=blend,
        ),
        environment,
    )
    compose_parallax_strip(output_root)
    finalize_candidate_manifest(output_root)
    print(
        json.dumps(
            {
                "candidate": args.candidate,
                "output_root": relative(output_root),
                "result": "DCC_SOURCE_CANDIDATE",
                "step13_authorized": False,
                "unreal_authorized": False,
            },
            sort_keys=True,
        )
    )
    return 0


def parse_args() -> argparse.Namespace:
    raw = sys.argv
    if "--" in raw:
        raw = raw[raw.index("--") + 1 :]
    else:
        raw = raw[1:]
    parser = argparse.ArgumentParser()
    parser.add_argument("--blueprint", type=Path, default=DEFAULT_BLUEPRINT)
    parser.add_argument("--amendment", type=Path, default=DEFAULT_AMENDMENT)
    parser.add_argument(
        "--parity-amendment",
        type=Path,
        default=DEFAULT_PARITY_AMENDMENT,
    )
    parser.add_argument(
        "--stitch-amendment",
        type=Path,
        default=DEFAULT_STITCH_AMENDMENT,
    )
    parser.add_argument(
        "--tolerance-amendment",
        type=Path,
        default=DEFAULT_TOLERANCE_AMENDMENT,
    )
    parser.add_argument("--candidate", choices=CANDIDATES)
    parser.add_argument("--output-root", type=Path)
    parser.add_argument("--internal-build", action="store_true")
    parser.add_argument("--internal-render", action="store_true")
    parser.add_argument("--compose-board", action="store_true")
    return parser.parse_args(raw)


def main() -> int:
    args = parse_args()
    if args.compose_board:
        board = compose_review_board()
        print(
            json.dumps(
                {
                    "review_board": relative(board),
                    "sha256": sha256(board),
                    "result": "REVIEW_BOARD_READY",
                },
                sort_keys=True,
            )
        )
        return 0
    if args.candidate is None or args.output_root is None:
        raise SystemExit("--candidate and --output-root are required")
    args.output_root = args.output_root.resolve()
    if args.internal_build:
        return internal_build(args)
    if args.internal_render:
        return internal_render(args)
    return external_build(args)


if __name__ == "__main__":
    sys.exit(main())
