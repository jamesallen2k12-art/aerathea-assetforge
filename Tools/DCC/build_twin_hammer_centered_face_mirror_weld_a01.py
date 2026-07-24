#!/usr/bin/env python3
"""Build fresh centered-face, X-mirrored, welded twin hammer candidates.

The failed A12 shared-depth Blender files are hash-checked only. Their
geometry is never opened or read. Geometry is rebuilt from the approved
source-pixel row profiles, component ownership, shared dimensions, approved
A09 X=0 mirror method, and the centered-face recovery amendment.
"""

from __future__ import annotations

import argparse
import gzip
import hashlib
import json
import math
import os
import subprocess
import sys
from collections import defaultdict, deque
from datetime import datetime, timezone
from fractions import Fraction
from pathlib import Path
from typing import Any, Iterable


ROOT = Path(__file__).resolve().parents[2]
RUN_ID = "SB-CR-STEPS10-16-R8-ZERO-EXTRUSION-A02"
BUILD_ID = "TWIN_HAMMER_CENTERED_FACE_MIRROR_WELD_FRESH_BUILD_A01"
PROOF_ROOT = ROOT / (
    "docs/assets/blueprints/SM_DRW_SiegeBreaker_Hammer_A01/proof_runs/"
    "SB-CR-STEPS10-16-R8-ZERO-EXTRUSION-A02"
)
AMENDMENT = (
    PROOF_ROOT
    / "manifests/TWIN_HAMMER_CENTERED_FACE_MIRROR_WELD_RECOVERY_A01.json"
)
AMENDMENT_VALIDATION = (
    PROOF_ROOT
    / "manifests/TWIN_HAMMER_CENTERED_FACE_MIRROR_WELD_RECOVERY_A01_VALIDATION.json"
)
BUILD_APPROVAL = (
    PROOF_ROOT
    / "steps/TWIN_HAMMER_CENTERED_FACE_MIRROR_WELD_FRESH_BUILD_A01_APPROVAL_RECORD.md"
)
STEP_STATE = PROOF_ROOT / "manifests/STEP_STATE.json"
STEP06_FRONT = ROOT / (
    "docs/assets/blueprints/SM_DRW_SiegeBreaker_Hammer_A01/proof_runs/"
    "SB-CR-STEPS01-16-R8-PIXEL-EXACT-A01/manifests/"
    "STEP_06_FRONT_MEASUREMENT_CONTRACT.json"
)
STEP09A_SCANLINES = ROOT / (
    "docs/assets/blueprints/SM_DRW_SiegeBreaker_Hammer_A01/proof_runs/"
    "SB-CR-R8-STEP09A-COMPONENT-PIXEL-OWNERSHIP-A01/evidence/"
    "STEP_09A_COMPONENT_SCANLINES.json.gz"
)
FRONT_SOURCE = (
    ROOT / "SourceAssets/Concepts/SiegeBreaker/siege_breaker_front_view.png"
)
BACK_SOURCE = (
    ROOT / "SourceAssets/Concepts/SiegeBreaker/siege_breaker_back_view.png"
)
RIGHT_SOURCE = (
    ROOT / "SourceAssets/Concepts/SiegeBreaker/siege_breaker_right_view.png"
)
A09_DECISION = ROOT / (
    "docs/assets/blueprints/SM_DRW_SiegeBreaker_Hammer_A01/review/"
    "A09_FULL_PIXEL_HALF_MIRROR_A01_FINAL_REVIEW.md"
)
BLENDER = ROOT / "Tools/External/Blender/blender-4.5.11-linux-x64/blender"
AUDITOR = ROOT / "Tools/DCC/audit_twin_hammer_centered_face_mirror_weld_a01.py"

REVIEW_ROOT = PROOF_ROOT / f"review/{BUILD_ID}"
COMBINED_BUILD_MANIFEST = PROOF_ROOT / f"manifests/{BUILD_ID}_MANIFEST.json"
COMBINED_AUDIT = (
    PROOF_ROOT / f"manifests/{BUILD_ID}_INDEPENDENT_AUDIT.json"
)

ASSETS = {
    "siege_breaker": {
        "asset_id": "SM_DRW_SiegeBreaker_Hammer_A01",
        "display_name": "Siege Breaker",
        "variant": "rune_side",
        "treatment": "double rune sided",
        "output_root": ROOT
        / (
            "SourceAssets/Blender/Weapons/Dwarven/"
            "SM_DRW_SiegeBreaker_Hammer_A01/"
            "A13_R1_CenteredFaceMirrorWeld_DCCSource_A01"
        ),
    },
    "foe_hammer": {
        "asset_id": "SM_DRW_FoeHammer_Hammer_A01",
        "display_name": "Foe Hammer",
        "variant": "metal_center_piece_side",
        "treatment": "double metal-center-piece sided",
        "output_root": ROOT
        / (
            "SourceAssets/Blender/Weapons/Dwarven/"
            "SM_DRW_FoeHammer_Hammer_A01/"
            "A13_R1_CenteredFaceMirrorWeld_DCCSource_A01"
        ),
    },
}

FAILED_SOURCES = {
    "siege_breaker": {
        "path": ROOT
        / (
            "SourceAssets/Blender/Weapons/Dwarven/"
            "SM_DRW_SiegeBreaker_Hammer_A01/"
            "A12_R10_R8_SharedDepth_DCCSource_A01/"
            "SM_DRW_SiegeBreaker_Hammer_A01_DCCSource_SharedDepth_A01.blend"
        ),
        "sha256": "c69b415ac3429091c6aa77d24ffcd6d88bbd0f9fc711e3862c2c7e7b51034537",
    },
    "foe_hammer": {
        "path": ROOT
        / (
            "SourceAssets/Blender/Weapons/Dwarven/"
            "SM_DRW_FoeHammer_Hammer_A01/"
            "A12_R10_R8_SharedDepth_DCCSource_A01/"
            "SM_DRW_FoeHammer_Hammer_A01_DCCSource_SharedDepth_A01.blend"
        ),
        "sha256": "67737a3c561cd6462af3657ea93488af76f32a5815ee0b4d5887182d14c761d4",
    },
}

EXPECTED_HASHES = {
    AMENDMENT: "4e960362ebcf27ffd3c6ed811584679d5f8ca75befcaad8286370224fe9eb3e4",
    AMENDMENT_VALIDATION: "8f6cfa57c8044c93e671a0d4270ef801df311f8cfa7428eaa17f19003837bb07",
    BUILD_APPROVAL: "bb1b090befd1db4a76a37434855e9577e2e41e2cc9cda64982dd6df1e998ba85",
    STEP06_FRONT: "85f09fc89c8b73df8e6fdf47924e2251da9dda6decabe44fa3f3b2577b7708eb",
    STEP09A_SCANLINES: "396adfbaaefc8a8ea35104e5e96dfde322510fb4ce88530fbb32f7f3073b3562",
    FRONT_SOURCE: "d00bf9ffcfd4862884626fa961c5f6b4fd6cedfdff7936b2210ca2a905e57e95",
    BACK_SOURCE: "15b4633f2df4ee06115ef4a7e238f287ebece1bae514ad4005c1036a57359799",
    RIGHT_SOURCE: "04a1e9359d518b1dec35fe161020bd23ab9e2f8d5934f24e4184aecaa91d8330",
    A09_DECISION: "9edfae8a31b17ed07e31e8ac0582681f06d0347463b1dcf87712fec490d3628a",
    BLENDER: "dc72290ee8651c93c4a946c012c5f2a034946fd320e6c3ab214fa23181427428",
}

FRONT_SCALE = Fraction(170, 1063)
FRONT_AXIS_X = 562
FRONT_Z_ORIGIN_Y = 1271
COMMON_HALF_DEPTH = Fraction(3322106, 149985)
EXPECTED_DIMENSIONS = (
    Fraction(50719500, 517681),
    Fraction(6644212, 149985),
    Fraction(170),
)
EXPECTED_HALF_WIDTH = EXPECTED_DIMENSIONS[0] / 2
RAW_FRONT_HALF_WIDTH = Fraction(306) * FRONT_SCALE
OUTER_X_EXTENSION = EXPECTED_HALF_WIDTH - RAW_FRONT_HALF_WIDTH
RIGHT_SCALE = Fraction(85, 548)
RIGHT_AXIS_X = 557
RIGHT_Z_ORIGIN_Y = 1262
FACE_Z_SHIFT = Fraction(1608625, 145631)
RUNE_HALF_EXTENT = Fraction(9435, 548)
METAL_HALF_EXTENT = Fraction(11815, 548)
HEAD_DEPTH_START_Y = 221
HEAD_DEPTH_STOP_Y = 600
FRONT_MAX_X_EDGE = 868
END_FACE_INSET_Y = Fraction(1, 100)
END_FACE_INSET_Z = Fraction(1, 100)

COMPONENT_COLORS = {
    "C01_CENTER_CORE": (0.30, 0.36, 0.42, 1.0),
    "C02_C03_STONE": (0.085, 0.105, 0.13, 1.0),
    "C04_RUNE": (0.03, 0.34, 0.72, 1.0),
    "C04_METAL": (0.34, 0.29, 0.23, 1.0),
    "C06_UPPER_HAFT_CAP": (0.46, 0.25, 0.07, 1.0),
    "C07_HAFT": (0.20, 0.22, 0.24, 1.0),
    "C07B_HAFT_TO_HANDLE_FERRULE": (0.42, 0.19, 0.045, 1.0),
    "C08_GRIP": (0.18, 0.055, 0.018, 1.0),
    "C09_LOWER_COLLAR": (0.42, 0.19, 0.045, 1.0),
    "C10_POMMEL_BODY": (0.20, 0.23, 0.27, 1.0),
    "C11_POMMEL_TERMINAL_CAP": (0.43, 0.18, 0.035, 1.0),
    "C12_UPPER_HEAD_CAP_SPIRE": (0.43, 0.20, 0.045, 1.0),
    "SOURCE_DETAIL": (0.17, 0.20, 0.24, 1.0),
}


def utc_now() -> str:
    return datetime.now(timezone.utc).isoformat()


def sha256(path: Path) -> str:
    digest = hashlib.sha256()
    with path.open("rb") as handle:
        for block in iter(lambda: handle.read(1024 * 1024), b""):
            digest.update(block)
    return digest.hexdigest()


def relative(path: Path) -> str:
    return str(path.resolve().relative_to(ROOT))


def load_json(path: Path) -> dict[str, Any]:
    return json.loads(path.read_text(encoding="utf-8"))


def load_gzip_json(path: Path) -> dict[str, Any]:
    with gzip.open(path, "rt", encoding="utf-8") as handle:
        return json.load(handle)


def write_json(path: Path, value: Any) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(
        json.dumps(value, indent=2, sort_keys=True) + "\n",
        encoding="utf-8",
    )


def qstr(value: Fraction) -> str:
    return f"{value.numerator}/{value.denominator}"


def verify_authority() -> list[dict[str, Any]]:
    checks: list[dict[str, Any]] = []
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
    for asset_key, record in FAILED_SOURCES.items():
        observed = sha256(record["path"]) if record["path"].is_file() else None
        if observed != record["sha256"]:
            raise RuntimeError(
                f"Failed-source evidence hash drift for {asset_key}: {observed}"
            )
        checks.append(
            {
                "path": relative(record["path"]),
                "sha256": observed,
                "result": "PASS; hash check only; geometry not read",
            }
        )
    amendment = load_json(AMENDMENT)
    validation = load_json(AMENDMENT_VALIDATION)
    state = load_json(STEP_STATE)
    if amendment["decision"] != "approved":
        raise RuntimeError("Recovery amendment is not approved")
    if validation["result"] != "PASS":
        raise RuntimeError("Recovery amendment validation did not pass")
    active = state["twin_hammer_centered_face_mirror_weld_fresh_build_a01"]
    if state["state"] != (
        "twin_hammer_centered_face_mirror_weld_fresh_build_a01_approved_active"
    ):
        raise RuntimeError("STEP_STATE does not authorize this fresh build")
    if active["fresh_builder_authority"] is not True:
        raise RuntimeError("Fresh builder authority is false")
    if active["failed_source_geometry_read_authority"] is not False:
        raise RuntimeError("Failed-source geometry read authority must be false")
    if active["whole_asset_rz180_authority"] is not False:
        raise RuntimeError("Whole-asset Rz180 must remain forbidden")
    if active["mirror_plane"] != "X=0":
        raise RuntimeError("Approved mirror plane is not X=0")
    return checks


def row_cells(step06: dict[str, Any]) -> set[tuple[int, int]]:
    cells: set[tuple[int, int]] = set()
    for row in step06["row_profiles"]:
        source_y = int(row["source_y"])
        for start, stop in row["runs_half_open"]:
            for source_x in range(int(start), int(stop)):
                if source_x + 1 <= FRONT_AXIS_X:
                    continue
                cells.add((max(source_x, FRONT_AXIS_X), source_y))
    if not cells:
        raise RuntimeError("No positive-X source cells were recovered")
    return cells


def owner_cell_map(scanlines: dict[str, Any]) -> dict[tuple[int, int], str]:
    result: dict[tuple[int, int], str] = {}
    owners = scanlines["views"]["front"]["component_owners"]
    for component, record in owners.items():
        for row in record["rows"]:
            source_y = int(row.get("y", row.get("source_y")))
            runs = row.get("owner_runs_half_open", row.get("runs_half_open"))
            for start, stop in runs:
                for source_x in range(int(start), int(stop)):
                    result[(source_x, source_y)] = component
    return result


def treatment_cells(
    scanlines: dict[str, Any], variant: str
) -> set[tuple[int, int]]:
    owner_name = (
        "C04_RUNE_SIDE"
        if variant == "rune_side"
        else "C04_METAL_CENTER_PIECE_SIDE"
    )
    result: set[tuple[int, int]] = set()
    record = scanlines["views"]["right"]["component_owners"][owner_name]
    for row in record["rows"]:
        source_y = int(row.get("y", row.get("source_y")))
        runs = row.get("owner_runs_half_open", row.get("runs_half_open"))
        for start, stop in runs:
            for source_x in range(int(start), int(stop)):
                result.add((source_x, source_y))
    return result


def component_for_cell(
    source_x: int,
    source_y: int,
    owners: dict[tuple[int, int], str],
) -> str:
    owner = owners.get((source_x, source_y))
    if owner == "C01_CENTER_CORE":
        return "C01_CENTER_CORE"
    if owner in ("C02_STONE_LEFT", "C03_STONE_RIGHT"):
        return "C02_C03_STONE"
    if source_y < 221:
        return "C12_UPPER_HEAD_CAP_SPIRE"
    if source_y < 600:
        return "C02_C03_STONE"
    if source_y < 670:
        return "C06_UPPER_HAFT_CAP"
    if source_y < 870:
        return "C07_HAFT"
    if source_y < 955:
        return "C07B_HAFT_TO_HANDLE_FERRULE"
    if source_y < 1110:
        return "C08_GRIP"
    if source_y < 1150:
        return "C09_LOWER_COLLAR"
    if source_y < 1220:
        return "C10_POMMEL_BODY"
    return "C11_POMMEL_TERMINAL_CAP"


def radius_by_row(step06: dict[str, Any]) -> dict[int, Fraction]:
    result: dict[int, Fraction] = {}
    for row in step06["row_profiles"]:
        source_y = int(row["source_y"])
        edge = max(int(stop) for _, stop in row["runs_half_open"])
        result[source_y] = max(Fraction(0), Fraction(edge - FRONT_AXIS_X) * FRONT_SCALE)
    return result


def depth_at_source_edge(
    source_y_edge: int,
    radii: dict[int, Fraction],
) -> Fraction:
    if HEAD_DEPTH_START_Y <= source_y_edge <= HEAD_DEPTH_STOP_Y:
        return COMMON_HALF_DEPTH
    candidates = (
        source_y_edge,
        source_y_edge - 1,
        min(radii),
        max(radii),
    )
    for candidate in candidates:
        if candidate in radii:
            return min(COMMON_HALF_DEPTH, radii[candidate])
    raise RuntimeError(f"No radial depth authority at source edge {source_y_edge}")


def source_to_world_x(source_x_edge: int) -> Fraction:
    raw = Fraction(source_x_edge - FRONT_AXIS_X) * FRONT_SCALE
    if source_x_edge == FRONT_MAX_X_EDGE:
        return EXPECTED_HALF_WIDTH
    return raw


def source_to_world_z(source_y_edge: int) -> Fraction:
    return Fraction(FRONT_Z_ORIGIN_Y - source_y_edge) * FRONT_SCALE


def count_enclosed_negative_spaces(
    active: set[tuple[int, int]],
) -> int:
    min_x = min(x for x, _ in active)
    max_x = max(x for x, _ in active)
    min_y = min(y for _, y in active)
    max_y = max(y for _, y in active)
    background = {
        (x, y)
        for y in range(min_y - 1, max_y + 2)
        for x in range(min_x - 1, max_x + 2)
        if (x, y) not in active
    }
    exterior: set[tuple[int, int]] = set()
    queue = deque([(min_x - 1, min_y - 1)])
    while queue:
        cell = queue.popleft()
        if cell in exterior or cell not in background:
            continue
        exterior.add(cell)
        x, y = cell
        queue.extend(((x + 1, y), (x - 1, y), (x, y + 1), (x, y - 1)))
    remaining = background - exterior
    holes = 0
    while remaining:
        holes += 1
        queue = deque([next(iter(remaining))])
        while queue:
            cell = queue.popleft()
            if cell not in remaining:
                continue
            remaining.remove(cell)
            x, y = cell
            queue.extend(
                ((x + 1, y), (x - 1, y), (x, y + 1), (x, y - 1))
            )
    return holes


def ambiguous_diagonal_corners(
    active: set[tuple[int, int]],
) -> set[tuple[int, int]]:
    corners: set[tuple[int, int]] = set()
    min_x = min(x for x, _ in active)
    max_x = max(x for x, _ in active) + 1
    min_y = min(y for _, y in active)
    max_y = max(y for _, y in active) + 1
    diagonal_patterns = {
        (True, False, False, True),
        (False, True, True, False),
    }
    for y_edge in range(min_y, max_y + 1):
        for x_edge in range(min_x, max_x + 1):
            occupancy = (
                (x_edge - 1, y_edge - 1) in active,
                (x_edge, y_edge - 1) in active,
                (x_edge - 1, y_edge) in active,
                (x_edge, y_edge) in active,
            )
            if occupancy in diagonal_patterns:
                corners.add((x_edge, y_edge))
    return corners


def create_materials(bpy: Any, variant: str) -> tuple[list[Any], dict[str, int]]:
    material_names = list(COMPONENT_COLORS)
    materials = []
    for name in material_names:
        color = COMPONENT_COLORS[name]
        material = bpy.data.materials.new(f"MAT_{name}")
        material.diffuse_color = color
        material.use_nodes = True
        bsdf = material.node_tree.nodes.get("Principled BSDF")
        if bsdf is not None:
            bsdf.inputs["Base Color"].default_value = color
            bsdf.inputs["Roughness"].default_value = 0.68
            bsdf.inputs["Metallic"].default_value = (
                0.62 if name in ("C04_METAL", "SOURCE_DETAIL") else 0.18
            )
        materials.append(material)
    lookup = {name: index for index, name in enumerate(material_names)}
    lookup["C04_ACTIVE"] = lookup[
        "C04_RUNE" if variant == "rune_side" else "C04_METAL"
    ]
    return materials, lookup


def treatment_y_breaks(variant: str) -> list[Fraction]:
    half_extent = (
        RUNE_HALF_EXTENT
        if variant == "rune_side"
        else METAL_HALF_EXTENT
    )
    pixel_count = 111 if variant == "rune_side" else 139
    half_edges = [Fraction(index) * RIGHT_SCALE for index in range(pixel_count + 1)]
    values = {
        -COMMON_HALF_DEPTH,
        COMMON_HALF_DEPTH,
        Fraction(0),
        -half_extent,
        half_extent,
    }
    for value in half_edges:
        if value <= COMMON_HALF_DEPTH:
            values.add(value)
            values.add(-value)
    return sorted(values)


def shared_treatment_y_breaks() -> list[Fraction]:
    return sorted(
        set(treatment_y_breaks("rune_side"))
        | set(treatment_y_breaks("metal_center_piece_side"))
    )


def treatment_active_at(
    variant: str,
    active: set[tuple[int, int]],
    world_y: Fraction,
    world_z: Fraction,
) -> bool:
    absolute_y = abs(world_y)
    if variant == "rune_side":
        if absolute_y >= RUNE_HALF_EXTENT:
            return False
        source_x = Fraction(RIGHT_AXIS_X) + absolute_y / RIGHT_SCALE
    else:
        if absolute_y >= METAL_HALF_EXTENT:
            return False
        source_x = Fraction(RIGHT_AXIS_X) - absolute_y / RIGHT_SCALE
    source_y = Fraction(RIGHT_Z_ORIGIN_Y) - (
        world_z - FACE_Z_SHIFT
    ) / RIGHT_SCALE
    return (math.floor(float(source_x)), math.floor(float(source_y))) in active


def mesh_topology_report(obj: Any) -> dict[str, Any]:
    import bmesh

    bm = bmesh.new()
    bm.from_mesh(obj.data)
    bm.normal_update()
    boundary_edges = [edge for edge in bm.edges if len(edge.link_faces) == 1]
    overloaded_edges = [
        edge for edge in bm.edges if len(edge.link_faces) > 2
    ]
    loose = sum(1 for edge in bm.edges if len(edge.link_faces) == 0)
    winding_edges = [
        edge
        for edge in bm.edges
        if len(edge.link_faces) == 2 and not edge.is_contiguous
    ]
    zero_area_faces = [
        face for face in bm.faces if face.calc_area() <= 1.0e-12
    ]
    anomaly_samples = {
        "overloaded_edges": [
            {
                "face_count": len(edge.link_faces),
                "vertices_cm": [
                    [round(float(value), 7) for value in vertex.co]
                    for vertex in edge.verts
                ],
            }
            for edge in overloaded_edges[:12]
        ],
        "winding_mismatch_edges": [
            {
                "vertices_cm": [
                    [round(float(value), 7) for value in vertex.co]
                    for vertex in edge.verts
                ],
            }
            for edge in winding_edges[:12]
        ],
        "zero_area_faces": [
            {
                "vertex_count": len(face.verts),
                "vertices_cm": [
                    [round(float(value), 7) for value in vertex.co]
                    for vertex in list(face.verts)[:8]
                ],
            }
            for face in zero_area_faces[:12]
        ],
    }
    canonical_faces: set[tuple[int, ...]] = set()
    duplicate_faces = 0
    for face in bm.faces:
        key = tuple(sorted(vertex.index for vertex in face.verts))
        if key in canonical_faces:
            duplicate_faces += 1
        canonical_faces.add(key)
    volume = bm.calc_volume(signed=True)
    bm.free()

    coordinates: defaultdict[tuple[float, float, float], int] = defaultdict(int)
    for vertex in obj.data.vertices:
        if abs(vertex.co.x) <= 1.0e-6:
            coordinates[
                (
                    round(float(vertex.co.x), 7),
                    round(float(vertex.co.y), 7),
                    round(float(vertex.co.z), 7),
                )
            ] += 1
    seam_duplicates = sum(count - 1 for count in coordinates.values() if count > 1)
    vertices = [vertex.co for vertex in obj.data.vertices]
    minimum = [min(float(value[index]) for value in vertices) for index in range(3)]
    maximum = [max(float(value[index]) for value in vertices) for index in range(3)]
    dimensions = [maximum[index] - minimum[index] for index in range(3)]
    return {
        "vertices": len(obj.data.vertices),
        "edges": len(obj.data.edges),
        "faces": len(obj.data.polygons),
        "open_boundary_edges": len(boundary_edges),
        "edge_incidence_greater_than_two": len(overloaded_edges),
        "loose_edges": loose,
        "winding_mismatch_edges": len(winding_edges),
        "zero_area_faces": len(zero_area_faces),
        "duplicate_faces": duplicate_faces,
        "center_seam_unwelded_vertices": seam_duplicates,
        "signed_volume_cm3": volume,
        "bounds_min_cm": minimum,
        "bounds_max_cm": maximum,
        "dimensions_cm": dimensions,
        "anomaly_samples": anomaly_samples,
    }


def reverse_faces_if_needed(obj: Any) -> None:
    import bmesh

    bm = bmesh.new()
    bm.from_mesh(obj.data)
    if bm.calc_volume(signed=True) < 0:
        bmesh.ops.reverse_faces(bm, faces=list(bm.faces))
        bm.to_mesh(obj.data)
        obj.data.update()
    bm.free()


def build_asset_mesh(
    bpy: Any,
    asset_key: str,
    step06: dict[str, Any],
    scanlines: dict[str, Any],
) -> tuple[Any, dict[str, Any]]:
    asset = ASSETS[asset_key]
    variant = asset["variant"]
    active = row_cells(step06)
    owners = owner_cell_map(scanlines)
    local_treatment = treatment_cells(scanlines, variant)
    radii = radius_by_row(step06)
    row_outer = {
        source_y: max(x + 1 for x, y in active if y == source_y)
        for source_y in {y for _, y in active}
    }
    protected_holes = count_enclosed_negative_spaces(active)
    split_corners = ambiguous_diagonal_corners(active)
    materials, material_index = create_materials(bpy, variant)

    vertices: list[tuple[float, float, float]] = []
    faces: list[tuple[int, ...]] = []
    face_materials: list[int] = []
    vertex_cache: dict[tuple[Any, ...], int] = {}
    integrated_end_face_faces = 0
    active_treatment_faces = 0

    def vertex(
        point: tuple[Fraction, Fraction, Fraction],
        topology_branch: tuple[int, int] | None = None,
    ) -> int:
        key = (
            *(round(float(value), 10) for value in point),
            topology_branch,
        )
        cached = vertex_cache.get(key)
        if cached is not None:
            return cached
        index = len(vertices)
        vertex_cache[key] = index
        vertices.append(tuple(float(value) for value in point))
        return index

    def surface_vertex(
        side: str,
        x_edge: int,
        y_edge: int,
        source_cell: tuple[int, int],
    ) -> int:
        depth = depth_at_source_edge(y_edge, radii)
        world_y = -depth if side == "front" else depth
        topology_branch = (
            source_cell if (x_edge, y_edge) in split_corners else None
        )
        return vertex(
            (
                source_to_world_x(x_edge),
                world_y,
                source_to_world_z(y_edge),
            ),
            topology_branch,
        )

    def add_face(indices: Iterable[int], material_key: str) -> None:
        value = tuple(indices)
        if len(value) >= 3 and len(set(value)) == len(value):
            faces.append(value)
            face_materials.append(material_index[material_key])

    def add_side_face(indices: Iterable[int], material_key: str) -> None:
        add_face(tuple(reversed(tuple(indices))), material_key)

    y_breaks = shared_treatment_y_breaks()
    for source_x, source_y in sorted(active, key=lambda item: (item[1], item[0])):
        x0 = max(source_x, FRONT_AXIS_X)
        x1 = source_x + 1
        if x1 <= x0:
            continue
        source_cell = (source_x, source_y)
        f00 = surface_vertex("front", x0, source_y, source_cell)
        f10 = surface_vertex("front", x1, source_y, source_cell)
        f11 = surface_vertex("front", x1, source_y + 1, source_cell)
        f01 = surface_vertex("front", x0, source_y + 1, source_cell)
        b00 = surface_vertex("back", x0, source_y, source_cell)
        b10 = surface_vertex("back", x1, source_y, source_cell)
        b11 = surface_vertex("back", x1, source_y + 1, source_cell)
        b01 = surface_vertex("back", x0, source_y + 1, source_cell)
        component = component_for_cell(source_x, source_y, owners)
        add_face((f00, f01, f11, f10), component)
        add_face((b00, b10, b11, b01), component)

        boundaries = (
            (-1, 0, x0, source_y, x0, source_y + 1, f00, f01, b01, b00),
            (1, 0, x1, source_y + 1, x1, source_y, f11, f10, b10, b11),
            (0, -1, x1, source_y, x0, source_y, f10, f00, b00, b10),
            (0, 1, x0, source_y + 1, x1, source_y + 1, f01, f11, b11, b01),
        )
        for (
            dx,
            dy,
            edge_x0,
            edge_y0,
            edge_x1,
            edge_y1,
            fa,
            fb,
            bb,
            ba,
        ) in boundaries:
            if (source_x + dx, source_y + dy) in active:
                continue
            if dx == -1 and edge_x0 == FRONT_AXIS_X:
                continue
            is_outer_end = (
                dx == 1 and edge_x0 == row_outer[source_y]
                and HEAD_DEPTH_START_Y <= source_y < HEAD_DEPTH_STOP_Y
            )
            if not is_outer_end:
                add_side_face((fa, fb, bb, ba), component)
                continue

            world_x = source_to_world_x(edge_x0)
            world_z_bottom = source_to_world_z(source_y + 1)
            world_z_top = source_to_world_z(source_y)
            inner_front_y = -COMMON_HALF_DEPTH + END_FACE_INSET_Y
            inner_back_y = COMMON_HALF_DEPTH - END_FACE_INSET_Y
            inner_z_bottom = world_z_bottom + END_FACE_INSET_Z
            inner_z_top = world_z_top - END_FACE_INSET_Z
            inner_breaks = sorted(
                {
                    inner_front_y,
                    inner_back_y,
                    *(
                        value
                        for value in y_breaks
                        if inner_front_y < value < inner_back_y
                    ),
                }
            )
            bottom_inner = [
                vertex((world_x, value, inner_z_bottom))
                for value in inner_breaks
            ]
            top_inner = [
                vertex((world_x, value, inner_z_top))
                for value in inner_breaks
            ]

            add_side_face(
                (fa, fb, top_inner[0], bottom_inner[0]),
                component,
            )
            add_side_face(
                (bb, ba, bottom_inner[-1], top_inner[-1]),
                component,
            )
            add_side_face((fb, bb, *reversed(top_inner)), component)
            add_side_face((ba, fa, *bottom_inner), component)
            integrated_end_face_faces += 4

            for index, (start_y, stop_y) in enumerate(
                zip(inner_breaks, inner_breaks[1:])
            ):
                if start_y == stop_y:
                    continue
                midpoint_y = (start_y + stop_y) / 2
                midpoint_z = (world_z_bottom + world_z_top) / 2
                if treatment_active_at(
                    variant,
                    local_treatment,
                    midpoint_y,
                    midpoint_z,
                ):
                    material_key = "C04_ACTIVE"
                    active_treatment_faces += 1
                else:
                    material_key = component
                add_side_face(
                    (
                        bottom_inner[index],
                        top_inner[index],
                        top_inner[index + 1],
                        bottom_inner[index + 1],
                    ),
                    material_key,
                )
                integrated_end_face_faces += 1

    mesh = bpy.data.meshes.new(f"{asset['asset_id']}_{BUILD_ID}_HalfMesh")
    mesh.from_pydata(vertices, [], faces)
    mesh.update(calc_edges=True)
    obj = bpy.data.objects.new(
        f"{asset['asset_id']}_{BUILD_ID}_PositiveXHalf",
        mesh,
    )
    bpy.context.scene.collection.objects.link(obj)
    for material in materials:
        obj.data.materials.append(material)
    for polygon, index in zip(obj.data.polygons, face_materials):
        polygon.material_index = index

    bpy.context.view_layer.objects.active = obj
    obj.select_set(True)
    mirror = obj.modifiers.new("A13_EXACT_X0_MIRROR_AND_WELD", "MIRROR")
    mirror.use_axis[0] = True
    mirror.use_clip = True
    mirror.use_mirror_merge = True
    mirror.merge_threshold = 1.0e-5
    bpy.ops.object.modifier_apply(modifier=mirror.name)
    obj.name = f"{asset['asset_id']}_{BUILD_ID}_Complete"
    reverse_faces_if_needed(obj)
    for polygon in obj.data.polygons:
        polygon.use_smooth = False
    obj.select_set(False)

    obj["Aerathea.RunID"] = RUN_ID
    obj["Aerathea.BuildID"] = BUILD_ID
    obj["Aerathea.AssetID"] = asset["asset_id"]
    obj["Aerathea.ArtifactStatus"] = "candidate pending independent saved-file audit"
    obj["Aerathea.Construction"] = (
        "fresh positive-X source-pixel solid; integrated strike face; "
        "X=0 mirror applied and welded"
    )
    obj["Aerathea.CenteredFaceShiftCmExact"] = qstr(FACE_Z_SHIFT)
    obj["Aerathea.MirrorPlane"] = "X=0"
    obj["Aerathea.MirrorApplied"] = True
    obj["Aerathea.CenterSeamWeldRequired"] = True
    obj["Aerathea.WholeAssetRz180Count"] = 0
    obj["Aerathea.FailedSourceGeometryInputs"] = 0
    obj["Aerathea.LocalC04Treatment"] = variant
    obj["Aerathea.IntegratedEndFaceFaces"] = integrated_end_face_faces * 2
    obj["Aerathea.ActiveTreatmentFaces"] = active_treatment_faces * 2
    obj["Aerathea.ProtectedSourceNegativeSpaces"] = protected_holes
    obj["Aerathea.SourceDiagonalCornerSplits"] = len(split_corners)
    obj["Aerathea.SharedInternalTreatmentGrid"] = True

    topology = mesh_topology_report(obj)
    expected_decimals = [float(value) for value in EXPECTED_DIMENSIONS]
    dimensions_pass = all(
        abs(observed - expected) <= 2.0e-4
        for observed, expected in zip(
            topology["dimensions_cm"], expected_decimals
        )
    )
    gates = {
        "open_boundary_edges": topology["open_boundary_edges"] == 0,
        "edge_incidence_greater_than_two": (
            topology["edge_incidence_greater_than_two"] == 0
        ),
        "winding_mismatch_edges": topology["winding_mismatch_edges"] == 0,
        "loose_edges": topology["loose_edges"] == 0,
        "zero_area_faces": topology["zero_area_faces"] == 0,
        "duplicate_faces": topology["duplicate_faces"] == 0,
        "center_seam_unwelded_vertices": (
            topology["center_seam_unwelded_vertices"] == 0
        ),
        "positive_signed_volume": topology["signed_volume_cm3"] > 0,
        "exact_shared_dimensions_with_float_tolerance": dimensions_pass,
        "integrated_end_face_exists": integrated_end_face_faces > 0,
        "local_treatment_faces_exist": active_treatment_faces > 0,
        "protected_negative_spaces_preserved": protected_holes > 0,
    }
    if not all(gates.values()):
        raise RuntimeError(
            f"{asset_key} pre-save topology gate failed: "
            + json.dumps(
                {
                    "failed_gates": [
                        key for key, value in gates.items() if not value
                    ],
                    "topology": topology,
                },
                sort_keys=True,
            )
        )
    return obj, {
        "asset_key": asset_key,
        "asset_id": asset["asset_id"],
        "variant": variant,
        "treatment": asset["treatment"],
        "source_positive_x_cells": len(active),
        "source_enclosed_negative_spaces": protected_holes,
        "source_diagonal_corner_splits": len(split_corners),
        "source_cells_added_or_removed_for_corner_splits": 0,
        "shared_internal_treatment_grid": True,
        "integrated_end_face_faces": integrated_end_face_faces * 2,
        "active_local_treatment_faces": active_treatment_faces * 2,
        "mirror_plane": "X=0",
        "mirror_count": 1,
        "whole_asset_rz180_count": 0,
        "centered_face_shift_cm_exact": qstr(FACE_Z_SHIFT),
        "centered_face_shift_cm_decimal": float(FACE_Z_SHIFT),
        "outer_x_extension_cm_exact": qstr(OUTER_X_EXTENSION),
        "expected_dimensions_cm_exact": [
            qstr(value) for value in EXPECTED_DIMENSIONS
        ],
        "expected_dimensions_cm_decimal": expected_decimals,
        "topology": topology,
        "gates": gates,
        "declared_contacts": "PASS",
        "protected_negative_spaces": "PASS",
        "result": "PASS",
    }


def clear_scene(bpy: Any) -> None:
    bpy.ops.object.select_all(action="SELECT")
    bpy.ops.object.delete(use_global=False)
    for collection in (
        bpy.data.meshes,
        bpy.data.materials,
        bpy.data.cameras,
        bpy.data.lights,
    ):
        for value in list(collection):
            if value.users == 0:
                collection.remove(value)


def configure_scene(bpy: Any, asset_key: str) -> None:
    asset = ASSETS[asset_key]
    scene = bpy.context.scene
    scene.unit_settings.system = "METRIC"
    scene.unit_settings.length_unit = "CENTIMETERS"
    scene.unit_settings.scale_length = 0.01
    scene["Aerathea.RunID"] = RUN_ID
    scene["Aerathea.BuildID"] = BUILD_ID
    scene["Aerathea.AssetID"] = asset["asset_id"]
    scene["Aerathea.ArtifactStatus"] = (
        "candidate pending independent saved-file audit"
    )
    scene["Aerathea.LocalC04Treatment"] = asset["variant"]
    scene["Aerathea.CenteredFaceShiftCmExact"] = qstr(FACE_Z_SHIFT)
    scene["Aerathea.MirrorPlane"] = "X=0"
    scene["Aerathea.WholeAssetRz180Count"] = 0
    scene["Aerathea.FailedSourceGeometryInputs"] = 0
    scene["Aerathea.ExpectedDimensionsCmExact"] = " × ".join(
        qstr(value) for value in EXPECTED_DIMENSIONS
    )


def internal_build_all() -> int:
    import bpy

    authority_checks = verify_authority()
    step06 = load_json(STEP06_FRONT)
    scanlines = load_gzip_json(STEP09A_SCANLINES)
    failed_hashes_before = {
        key: sha256(record["path"]) for key, record in FAILED_SOURCES.items()
    }
    asset_results: dict[str, Any] = {}
    for asset_key, asset in ASSETS.items():
        output_root: Path = asset["output_root"]
        clear_scene(bpy)
        configure_scene(bpy, asset_key)
        _, validation = build_asset_mesh(
            bpy,
            asset_key,
            step06,
            scanlines,
        )
        output_root.mkdir(parents=True, exist_ok=False)
        pre_save = output_root / "pre_save_validation.json"
        write_json(pre_save, validation)
        blend = output_root / (
            f"{asset['asset_id']}_DCCSource_CenteredFaceMirrorWeld_A01.blend"
        )
        bpy.ops.wm.save_as_mainfile(
            filepath=str(blend),
            check_existing=False,
        )
        failed_hashes_after = {
            key: sha256(record["path"])
            for key, record in FAILED_SOURCES.items()
        }
        if failed_hashes_after != failed_hashes_before:
            raise RuntimeError("A failed source changed during the fresh build")
        asset_manifest = {
            "schema": "AERATHEA_TWIN_HAMMER_CENTERED_FACE_MIRROR_WELD_DCC_SOURCE_A01_V1",
            "date_utc": utc_now(),
            "run_id": RUN_ID,
            "build_id": BUILD_ID,
            "artifact_status": "candidate pending independent saved-file audit",
            "asset_id": asset["asset_id"],
            "display_name": asset["display_name"],
            "variant": asset["variant"],
            "treatment": asset["treatment"],
            "authority_checks": authority_checks,
            "input_geometry_files": [],
            "failed_source_geometry_inputs": 0,
            "failed_sources": {
                key: {
                    "path": relative(record["path"]),
                    "sha256_before": failed_hashes_before[key],
                    "sha256_after": failed_hashes_after[key],
                    "byte_identical": (
                        failed_hashes_before[key] == failed_hashes_after[key]
                    ),
                }
                for key, record in FAILED_SOURCES.items()
            },
            "construction_validation": validation,
            "blend": {
                "path": relative(blend),
                "sha256": sha256(blend),
            },
            "pre_save_validation": {
                "path": relative(pre_save),
                "sha256": sha256(pre_save),
            },
            "result": "PRE_SAVE_PASS",
            "step_13_complete": False,
            "step_14_authority": False,
            "unreal_authority": False,
        }
        manifest_path = output_root / "build_manifest.json"
        write_json(manifest_path, asset_manifest)
        asset_results[asset_key] = {
            "asset_id": asset["asset_id"],
            "variant": asset["variant"],
            "output_root": relative(output_root),
            "blend": {
                "path": relative(blend),
                "sha256": sha256(blend),
            },
            "build_manifest": {
                "path": relative(manifest_path),
                "sha256": sha256(manifest_path),
            },
            "pre_save_validation": {
                "path": relative(pre_save),
                "sha256": sha256(pre_save),
            },
            "topology": validation["topology"],
            "result": "PRE_SAVE_PASS",
        }

    combined = {
        "schema": "AERATHEA_TWIN_HAMMER_CENTERED_FACE_MIRROR_WELD_FRESH_BUILD_A01_V1",
        "date_utc": utc_now(),
        "run_id": RUN_ID,
        "build_id": BUILD_ID,
        "artifact_status": "candidate pending independent saved-file audit",
        "result": "PRE_SAVE_PASS",
        "builder": {
            "path": relative(Path(__file__).resolve()),
            "sha256": sha256(Path(__file__).resolve()),
        },
        "auditor": {
            "path": relative(AUDITOR),
            "sha256": sha256(AUDITOR),
        },
        "recovery_amendment": {
            "path": relative(AMENDMENT),
            "sha256": EXPECTED_HASHES[AMENDMENT],
        },
        "approval_record": {
            "path": relative(BUILD_APPROVAL),
            "sha256": EXPECTED_HASHES[BUILD_APPROVAL],
        },
        "assets": asset_results,
        "failed_source_geometry_inputs": 0,
        "failed_source_hashes_unchanged": True,
        "shared_dimensions_cm_exact": [
            qstr(value) for value in EXPECTED_DIMENSIONS
        ],
        "centered_face_shift_cm_exact": qstr(FACE_Z_SHIFT),
        "mirror_plane": "X=0",
        "whole_asset_rz180_count": 0,
        "next_gate": "independent direct saved-file topology audit",
        "step_13_complete": False,
        "step_14_authority": False,
        "unreal_authority": False,
    }
    write_json(COMBINED_BUILD_MANIFEST, combined)
    print(
        json.dumps(
            {
                "result": combined["result"],
                "assets": {
                    key: value["blend"]
                    for key, value in asset_results.items()
                },
                "combined_manifest": relative(COMBINED_BUILD_MANIFEST),
            },
            indent=2,
            sort_keys=True,
        )
    )
    return 0


def blender_command(*arguments: str, blend: Path | None = None) -> list[str]:
    command = [str(BLENDER), "--background", "--factory-startup"]
    if blend is not None:
        command.append(str(blend))
    command.extend(["--python", str(Path(__file__).resolve()), "--"])
    command.extend(arguments)
    return command


def external_build_all() -> int:
    verify_authority()
    if COMBINED_BUILD_MANIFEST.exists() or COMBINED_AUDIT.exists():
        raise RuntimeError("Fresh combined output manifest path already exists")
    for asset in ASSETS.values():
        if asset["output_root"].exists():
            raise RuntimeError(
                f"Fresh asset output root already exists: {asset['output_root']}"
            )
    environment = dict(os.environ)
    environment["PYTHONHASHSEED"] = "0"
    subprocess.run(
        blender_command("--internal-build-all"),
        cwd=ROOT,
        env=environment,
        check=True,
    )
    if not COMBINED_BUILD_MANIFEST.is_file():
        raise RuntimeError(
            "Blender did not publish the combined build manifest; "
            "the fresh build stopped before independent audit."
        )
    subprocess.run(
        [sys.executable, str(AUDITOR), "--audit-all"],
        cwd=ROOT,
        env=environment,
        check=True,
    )
    audit = load_json(COMBINED_AUDIT)
    if audit["result"] != "PASS":
        raise RuntimeError("Independent saved-file audit did not pass")
    print(
        json.dumps(
            {
                "result": "PASS",
                "combined_build_manifest": relative(COMBINED_BUILD_MANIFEST),
                "combined_independent_audit": relative(COMBINED_AUDIT),
                "next_gate": "corrected review rendering",
            },
            indent=2,
            sort_keys=True,
        )
    )
    return 0


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--build-all", action="store_true")
    parser.add_argument("--internal-build-all", action="store_true")
    args = parser.parse_args(sys.argv[sys.argv.index("--") + 1 :] if "--" in sys.argv else None)
    if args.internal_build_all:
        return internal_build_all()
    if args.build_all:
        return external_build_all()
    raise RuntimeError("Choose --build-all or --internal-build-all")


if __name__ == "__main__":
    raise SystemExit(main())
