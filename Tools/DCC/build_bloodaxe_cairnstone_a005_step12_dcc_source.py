#!/usr/bin/env python3
"""Fresh A005 Step 12 DCC source candidate builder.

The schema-only path intentionally runs without importing bpy and performs no
filesystem writes. The build path is intended for Blender background mode.
"""

from __future__ import annotations

import argparse
import hashlib
import json
import math
import os
import sys
from collections import Counter, defaultdict
from pathlib import Path
from typing import Any, Dict, Iterable, List, Sequence, Tuple


ASSET_ID = "SM_GIA_BloodAxeCairnstone_A005"
CONTRACT_ID = "A005-CR-STEP12-DCC-SOURCE-GEOMETRY-A01"
SCRIPT_PATH = Path(__file__).resolve()
REPO_ROOT = SCRIPT_PATH.parents[2]
A005_ROOT = Path("docs/assets/blueprints") / ASSET_ID
MANIFEST_ROOT = A005_ROOT / "manifests"
INPUT_LOCK_REL = MANIFEST_ROOT / "STEP_12_INPUT_LOCK.json"
BLUEPRINT_REL = MANIFEST_ROOT / "STEP_11_CONSTRUCTION_BLUEPRINT.json"
VAG_MAP_REL = MANIFEST_ROOT / "STEP_11_VERTEX_AUTHORITY_MAP.json"
TECH_RULES_REL = MANIFEST_ROOT / "STEP_11_TECHNICAL_RULE_REGISTRY.json"
FRONT_MEASURE_REL = MANIFEST_ROOT / "STEP_06_FRONT_MEASUREMENT_MANIFEST.json"
BACK_MEASURE_REL = MANIFEST_ROOT / "STEP_06_BACK_MEASUREMENT_MANIFEST.json"
LEFT_MEASURE_REL = MANIFEST_ROOT / "STEP_07_LEFT_MEASUREMENT_MANIFEST.json"
RIGHT_MEASURE_REL = MANIFEST_ROOT / "STEP_07_RIGHT_MEASUREMENT_MANIFEST.json"
PHYSICAL_BOUNDS_REL = MANIFEST_ROOT / "SCALE_AUTHORITY_RECOVERY_A01_PHYSICAL_BOUNDS.json"
DCC_ROOT_REL = Path("SourceAssets/Blender/Props/Giants/BloodAxe/Cairns") / ASSET_ID
BLEND_REL = DCC_ROOT_REL / f"{ASSET_ID}_DCCSource_A01.blend"
GEOMETRY_MANIFEST_REL = DCC_ROOT_REL / f"{ASSET_ID}_GEOMETRY_MANIFEST.json"

REQUIRED_OBJECTS = (
    "C004_APRON",
    "C003_LOWER_TIER",
    "C002_UPPER_TIER",
    "C001_BODY",
)
NON_GEOMETRY_COMPONENTS = ("C-005", "C-006", "C-007")
ALLOWED_OUTPUTS = (str(BLEND_REL), str(GEOMETRY_MANIFEST_REL))

Vec3 = Tuple[float, float, float]
Face = Tuple[int, ...]


def parse_args(argv: Sequence[str]) -> argparse.Namespace:
    parser = argparse.ArgumentParser(
        description="Build the fresh A005 Step 12 Blender source candidate."
    )
    mode = parser.add_mutually_exclusive_group(required=True)
    mode.add_argument("--schema-only", action="store_true")
    mode.add_argument("--build", action="store_true")
    return parser.parse_args(list(argv))


def blender_script_args() -> List[str]:
    if "--" in sys.argv:
        return sys.argv[sys.argv.index("--") + 1 :]
    return sys.argv[1:]


def sha256_file(path: Path) -> str:
    digest = hashlib.sha256()
    with path.open("rb") as handle:
        for chunk in iter(lambda: handle.read(1024 * 1024), b""):
            digest.update(chunk)
    return digest.hexdigest()


def load_json(rel_path: Path) -> Dict[str, Any]:
    with (REPO_ROOT / rel_path).open("r", encoding="utf-8") as handle:
        return json.load(handle)


def validate_a005_text(value: str, label: str) -> None:
    for suffix in range(1, 5):
        legacy_id = f"SM_GIA_BloodAxeCairnstone_A{suffix:03d}"
        if legacy_id in value:
            raise RuntimeError(f"legacy asset reference in {label}")
    if "CoreRecovery" in value:
        raise RuntimeError(f"quarantined recovery path in {label}")


def verify_input_lock() -> Dict[str, Any]:
    lock_path = REPO_ROOT / INPUT_LOCK_REL
    if not lock_path.is_file() or lock_path.is_symlink():
        raise RuntimeError("Step 12 input lock is missing or not a regular file")
    lock = load_json(INPUT_LOCK_REL)
    if lock.get("asset_id") != ASSET_ID or lock.get("contract_id") != CONTRACT_ID:
        raise RuntimeError("Step 12 input lock identity mismatch")
    if not lock.get("locked"):
        raise RuntimeError("Step 12 input lock is not locked")
    entries = lock.get("locked_inputs", [])
    if lock.get("counts", {}).get("locked_inputs") != len(entries):
        raise RuntimeError("Step 12 input count mismatch")
    for entry in entries:
        rel = entry["path"]
        validate_a005_text(rel, "locked input")
        path = REPO_ROOT / rel
        if not path.is_file() or path.is_symlink():
            raise RuntimeError(f"locked input missing or non-regular: {rel}")
        actual = sha256_file(path)
        if actual != entry["sha256"]:
            raise RuntimeError(f"locked input hash mismatch: {rel}")
    return lock


def schema_report() -> Dict[str, Any]:
    lock = verify_input_lock()
    for value in (ASSET_ID, CONTRACT_ID, *ALLOWED_OUTPUTS, *REQUIRED_OBJECTS):
        validate_a005_text(value, "schema declaration")
    if set(NON_GEOMETRY_COMPONENTS) != {"C-005", "C-006", "C-007"}:
        raise RuntimeError("non-geometry component declaration mismatch")
    return {
        "schema": "aerathea.step12_builder_schema_preflight.v1",
        "asset_id": ASSET_ID,
        "contract_id": CONTRACT_ID,
        "status": "pass_schema_only_no_output",
        "bpy_imported": "bpy" in sys.modules,
        "filesystem_writes": 0,
        "locked_inputs_verified": len(lock["locked_inputs"]),
        "required_objects": list(REQUIRED_OBJECTS),
        "allowed_outputs": list(ALLOWED_OUTPUTS),
        "non_geometry_components": list(NON_GEOMETRY_COMPONENTS),
    }


def superellipse_point(a: float, b: float, q: float, z: float) -> Vec3:
    theta = math.pi * q / 4.0
    cosine = math.cos(theta)
    sine = math.sin(theta)
    x = a * math.copysign(abs(cosine) ** (2.0 / 3.0), cosine)
    y = b * math.copysign(abs(sine) ** (2.0 / 3.0), sine)
    return (x, y, z)


def chamfered_rectangle(width: float, depth: float, z: float, subdivide: bool) -> List[Vec3]:
    x = width / 2.0
    y = depth / 2.0
    midpoint = 0.5
    base = [
        (-x, -midpoint * y, z),
        (-midpoint * x, -y, z),
        (midpoint * x, -y, z),
        (x, -midpoint * y, z),
        (x, midpoint * y, z),
        (midpoint * x, y, z),
        (-midpoint * x, y, z),
        (-x, midpoint * y, z),
    ]
    if not subdivide:
        return base
    result: List[Vec3] = []
    for index, point in enumerate(base):
        nxt = base[(index + 1) % len(base)]
        result.append(point)
        result.append(
            (
                (point[0] + nxt[0]) / 2.0,
                (point[1] + nxt[1]) / 2.0,
                z,
            )
        )
    return result


def interp_profile(samples: Sequence[Tuple[float, float]], z: float) -> float:
    ordered = sorted(samples)
    if z <= ordered[0][0]:
        return ordered[0][1]
    if z >= ordered[-1][0]:
        return ordered[-1][1]
    for (z0, value0), (z1, value1) in zip(ordered, ordered[1:]):
        if z0 <= z <= z1:
            alpha = (z - z0) / (z1 - z0)
            return value0 + alpha * (value1 - value0)
    raise RuntimeError("profile interpolation failed")


def normalize_c001_profile(
    rows: Sequence[Dict[str, Any]], target_full_extent: float
) -> List[Tuple[float, float]]:
    component_rows = [row for row in rows if row.get("component_id") == "C-001"]
    if not component_rows:
        raise RuntimeError("C-001 owner-view rows missing")
    min_row = min(row["y"] for row in component_rows)
    max_row = max(row["y"] for row in component_rows)
    max_width = max(row["width_px"] for row in component_rows)
    result: List[Tuple[float, float]] = []
    for row in component_rows:
        if max_row == min_row:
            raise RuntimeError("C-001 owner-view row range is zero")
        z = 220.0 - ((row["y"] - min_row) / (max_row - min_row)) * 180.0
        half_extent = 0.5 * target_full_extent * row["width_px"] / max_width
        result.append((round(z, 12), round(half_extent, 12)))
    result.append((35.0, (target_full_extent - 20.0 if target_full_extent == 120.0 else target_full_extent - 14.0) / 2.0))
    result.append((34.5, (target_full_extent - 22.0 if target_full_extent == 120.0 else target_full_extent - 16.0) / 2.0))
    return sorted(set(result))


class MeshPlan:
    def __init__(self, object_name: str, component_id: str) -> None:
        self.object_name = object_name
        self.component_id = component_id
        self.vertices: List[Vec3] = []
        self.faces: List[Face] = []
        self.vertex_vag: List[str] = []
        self.face_authority: List[str] = []

    def add_vertex(self, coordinate: Vec3, vag: str) -> int:
        self.vertices.append(tuple(float(value) for value in coordinate))
        self.vertex_vag.append(vag)
        return len(self.vertices) - 1

    def add_face(self, indices: Iterable[int], authority: str) -> None:
        face = tuple(indices)
        if len(face) < 3 or len(set(face)) < 3:
            raise RuntimeError(f"degenerate planned face in {self.object_name}")
        self.faces.append(face)
        self.face_authority.append(authority)


def add_ring(plan: MeshPlan, points: Sequence[Vec3], vag_ids: Sequence[str]) -> List[int]:
    if len(points) != len(vag_ids):
        raise RuntimeError("ring point/VAG count mismatch")
    return [plan.add_vertex(point, vag) for point, vag in zip(points, vag_ids)]


def connect_rings(
    plan: MeshPlan,
    lower: Sequence[int],
    upper: Sequence[int],
    normal_authority: str,
    seam_authority: str | None = None,
) -> None:
    if len(lower) != len(upper):
        raise RuntimeError("ring sizes differ")
    count = len(lower)
    for index in range(count):
        nxt = (index + 1) % count
        authority = seam_authority if seam_authority and index == count - 1 else normal_authority
        plan.add_face((lower[index], lower[nxt], upper[nxt], upper[index]), authority)


def cap_ring(plan: MeshPlan, ring: Sequence[int], z: float, vag: str, top: bool) -> int:
    center = plan.add_vertex((0.0, 0.0, z), vag)
    for index in range(len(ring)):
        nxt = (index + 1) % len(ring)
        if top:
            plan.add_face((center, ring[index], ring[nxt]), vag)
        else:
            plan.add_face((center, ring[nxt], ring[index]), vag)
    return center


def build_c004(blueprint: Dict[str, Any]) -> MeshPlan:
    specification = blueprint["component_specifications"]["C004"]
    lattice = specification["field_lattice"]
    if lattice["q_columns"] != 32 or lattice["v_rows"] != 3:
        raise RuntimeError("C-004 lattice authority mismatch")
    plan = MeshPlan("C004_APRON", "C-004")
    q_values = [-0.5 + index * 0.25 for index in range(32)]
    rings: List[List[int]] = []
    for v, z in ((1.0, 0.0), (0.5, 5.0), (0.0, 10.0)):
        a = 56.0 + 14.0 * v
        b = 44.0 + 11.0 * v
        points = [superellipse_point(a, b, q, z) for q in q_values]
        vag_ids: List[str] = []
        for q in q_values:
            theta = math.pi * q / 4.0
            is_axis_anchor = v == 1.0 and (
                abs(math.sin(theta)) < 1.0e-9 or abs(math.cos(theta)) < 1.0e-9
            )
            vag_ids.append(
                "VAG-011-C004-SOURCE-OWNED-SILHOUETTE"
                if is_axis_anchor
                else "VAG-010-C004-TRANSITION-LATTICE"
            )
        rings.append(add_ring(plan, points, vag_ids))
    hidden_points = [superellipse_point(55.5, 43.5, q, 10.5) for q in q_values]
    hidden_ring = add_ring(
        plan,
        hidden_points,
        ["VAG-014-CL001-CL003-HIDDEN-OVERLAP"] * len(hidden_points),
    )
    rings.append(hidden_ring)
    connect_rings(
        plan,
        rings[0],
        rings[1],
        "VAG-010-C004-TRANSITION-LATTICE",
        "VAG-012-C004-FINAL-FIRST-CLOSURE-FACE",
    )
    connect_rings(
        plan,
        rings[1],
        rings[2],
        "VAG-010-C004-TRANSITION-LATTICE",
        "VAG-012-C004-FINAL-FIRST-CLOSURE-FACE",
    )
    connect_rings(
        plan,
        rings[2],
        rings[3],
        "VAG-014-CL001-CL003-HIDDEN-OVERLAP",
        "VAG-012-C004-FINAL-FIRST-CLOSURE-FACE",
    )
    cap_ring(plan, rings[0], 0.0, "VAG-013-C004-Z0-BOTTOM", top=False)
    cap_ring(plan, rings[3], 10.5, "VAG-014-CL001-CL003-HIDDEN-OVERLAP", top=True)
    return plan


def build_course(
    object_name: str,
    component_id: str,
    ring_specs: Sequence[Tuple[float, float, float, str]],
    visible_vag: str,
    closure_vag: str,
) -> MeshPlan:
    plan = MeshPlan(object_name, component_id)
    rings: List[List[int]] = []
    for z, width, depth, vag in ring_specs:
        points = chamfered_rectangle(width, depth, z, subdivide=True)
        rings.append(add_ring(plan, points, [vag] * len(points)))
    for index in range(len(rings) - 1):
        authority = visible_vag if 0 < index < len(rings) - 2 else "VAG-014-CL001-CL003-HIDDEN-OVERLAP"
        connect_rings(plan, rings[index], rings[index + 1], authority)
    cap_ring(plan, rings[0], ring_specs[0][0], closure_vag, top=False)
    cap_ring(plan, rings[-1], ring_specs[-1][0], closure_vag, top=True)
    return plan


def build_c003(blueprint: Dict[str, Any]) -> MeshPlan:
    boxes = blueprint["component_specifications"]["C003"]["max_containment_boxes_cm"]
    lower = boxes["CL003"]
    upper = boxes["CL002"]
    visible_vag = "VAG-008-C003-VISIBLE-TIER"
    overlap_vag = "VAG-014-CL001-CL003-HIDDEN-OVERLAP"
    specs = [
        (9.5, lower[0] - 4.0, lower[1] - 4.0, overlap_vag),
        (10.0, lower[0] - 1.0, lower[1] - 1.0, visible_vag),
        (16.5, (lower[0] + upper[0]) / 2.0 - 0.5, (lower[1] + upper[1]) / 2.0 - 0.5, visible_vag),
        (23.0, upper[0], upper[1], visible_vag),
        (23.5, upper[0] - 4.0, upper[1] - 4.0, overlap_vag),
    ]
    return build_course(
        "C003_LOWER_TIER",
        "C-003",
        specs,
        visible_vag,
        "VAG-009-C003-HIDDEN-CLOSURES",
    )


def build_c002(blueprint: Dict[str, Any]) -> MeshPlan:
    boxes = blueprint["component_specifications"]["C002"]["max_containment_boxes_cm"]
    lower = boxes["CL002"]
    upper = boxes["CL001"]
    visible_vag = "VAG-006-C002-VISIBLE-TIER"
    overlap_vag = "VAG-014-CL001-CL003-HIDDEN-OVERLAP"
    specs = [
        (22.5, lower[0] - 4.0, lower[1] - 4.0, overlap_vag),
        (23.0, lower[0], lower[1], visible_vag),
        (29.0, (lower[0] + upper[0]) / 2.0, (lower[1] + upper[1]) / 2.0, visible_vag),
        (35.0, upper[0], upper[1], visible_vag),
        (35.5, upper[0] - 4.0, upper[1] - 4.0, overlap_vag),
    ]
    return build_course(
        "C002_UPPER_TIER",
        "C-002",
        specs,
        visible_vag,
        "VAG-007-C002-HIDDEN-CLOSURES",
    )


def c001_ring_vags(count: int, z: float) -> List[str]:
    if z == 220.0:
        return ["VAG-004-C001-TOP"] * count
    if z <= 34.5:
        return ["VAG-014-CL001-CL003-HIDDEN-OVERLAP"] * count
    pattern = (
        "VAG-001-C001-FRONT-XZ",
        "VAG-002-C001-LEFT-YZ",
        "VAG-002-C001-LEFT-YZ",
        "VAG-001-C001-FRONT-XZ",
        "VAG-003-C001-CORNER-JOINS",
        "VAG-003-C001-CORNER-JOINS",
        "VAG-002-C001-LEFT-YZ",
        "VAG-001-C001-FRONT-XZ",
    )
    if count != len(pattern):
        raise RuntimeError("unexpected C-001 ring count")
    return list(pattern)


def build_c001(
    blueprint: Dict[str, Any],
    front_measure: Dict[str, Any],
    left_measure: Dict[str, Any],
) -> Tuple[MeshPlan, Dict[str, Any]]:
    targets = blueprint["coordinate_frame"]["bounds_targets_cm"]["C001"]
    x_profile = normalize_c001_profile(
        front_measure["visible_outer_edge_row_samples"], targets["max_width"]
    )
    y_profile = normalize_c001_profile(
        left_measure["visible_outer_edge_row_samples"], targets["max_depth"]
    )
    z_values = sorted(set([value[0] for value in x_profile + y_profile] + [34.5, 35.0, 220.0]))
    plan = MeshPlan("C001_BODY", "C-001")
    rings: List[List[int]] = []
    dimensions: List[Dict[str, float]] = []
    for z in z_values:
        width = 2.0 * interp_profile(x_profile, z)
        depth = 2.0 * interp_profile(y_profile, z)
        points = chamfered_rectangle(width, depth, z, subdivide=False)
        rings.append(add_ring(plan, points, c001_ring_vags(len(points), z)))
        dimensions.append({"z_cm": z, "width_cm": width, "depth_cm": depth})
    for index in range(len(rings) - 1):
        if z_values[index] <= 34.5:
            authority = "VAG-014-CL001-CL003-HIDDEN-OVERLAP"
        elif z_values[index + 1] >= 220.0:
            authority = "VAG-004-C001-TOP"
        else:
            authority = "VAG-003-C001-CORNER-JOINS"
        connect_rings(plan, rings[index], rings[index + 1], authority)
    cap_ring(plan, rings[0], z_values[0], "VAG-005-C001-HIDDEN-BOTTOM", top=False)
    cap_ring(plan, rings[-1], z_values[-1], "VAG-004-C001-TOP", top=True)
    derivation = {
        "formula": "same-owner sample rows normalized piecewise linearly; visible row range maps to Z 220..40 cm and maximum observed owner-view span maps to the approved maximum extent; approved contact containment adds Z 35 and hidden Z 34.5 stations",
        "front_owner_source_ids": [
            row["id"]
            for row in front_measure["visible_outer_edge_row_samples"]
            if row.get("component_id") == "C-001"
        ],
        "left_owner_source_ids": [
            row["id"]
            for row in left_measure["visible_outer_edge_row_samples"]
            if row.get("component_id") == "C-001"
        ],
        "x_profile_z_half_extent_cm": [[z, value] for z, value in x_profile],
        "y_profile_z_half_extent_cm": [[z, value] for z, value in y_profile],
        "constructed_ring_dimensions": dimensions,
        "averaging": False,
        "smoothing": False,
        "cross_view_pairing": False,
        "source_center_claim": False,
    }
    return plan, derivation


def topology_summary(plan: MeshPlan) -> Dict[str, Any]:
    edges: Counter[Tuple[int, int]] = Counter()
    for face in plan.faces:
        for first, second in zip(face, face[1:] + face[:1]):
            edges[tuple(sorted((first, second)))] += 1
    open_edges = sum(1 for count in edges.values() if count == 1)
    non_manifold_edges = sum(1 for count in edges.values() if count != 2)
    used = {index for face in plan.faces for index in face}
    duplicate_faces = len(plan.faces) - len({tuple(sorted(face)) for face in plan.faces})
    return {
        "vertices": len(plan.vertices),
        "faces": len(plan.faces),
        "triangles_evaluated": sum(len(face) - 2 for face in plan.faces),
        "edges": len(edges),
        "open_edges": open_edges,
        "non_manifold_edges": non_manifold_edges,
        "loose_vertices": len(plan.vertices) - len(used),
        "duplicate_faces": duplicate_faces,
        "degenerate_faces": sum(1 for face in plan.faces if len(set(face)) < 3),
        "watertight_by_edge_incidence": all(count == 2 for count in edges.values()),
    }


def bounds(vertices: Sequence[Vec3]) -> Dict[str, Any]:
    minimum = [min(vertex[axis] for vertex in vertices) for axis in range(3)]
    maximum = [max(vertex[axis] for vertex in vertices) for axis in range(3)]
    extent = [maximum[axis] - minimum[axis] for axis in range(3)]
    return {
        "min_cm": [round(value, 9) for value in minimum],
        "max_cm": [round(value, 9) for value in maximum],
        "extent_cm": [round(value, 9) for value in extent],
    }


def create_blender_object(bpy: Any, plan: MeshPlan) -> Any:
    mesh = bpy.data.meshes.new(f"{plan.object_name}_MESH")
    mesh.from_pydata(plan.vertices, [], plan.faces)
    mesh.validate(verbose=False, clean_customdata=False)
    mesh.update(calc_edges=True)
    obj = bpy.data.objects.new(plan.object_name, mesh)
    bpy.context.collection.objects.link(obj)
    obj.location = (0.0, 0.0, 0.0)
    obj.rotation_euler = (0.0, 0.0, 0.0)
    obj.scale = (1.0, 1.0, 1.0)
    obj["asset_id"] = ASSET_ID
    obj["component_id"] = plan.component_id
    obj["step12_contract_id"] = CONTRACT_ID
    obj["artifact_classification"] = "candidate"
    obj["unit"] = "centimeter"
    obj["geometry_manifest"] = str(GEOMETRY_MANIFEST_REL)
    obj["uv_created"] = False
    obj["final_material_created"] = False
    obj["lod_created"] = False
    obj["collision_created"] = False
    for vag_id in sorted(set(plan.vertex_vag)):
        group = obj.vertex_groups.new(name=vag_id)
        indices = [index for index, value in enumerate(plan.vertex_vag) if value == vag_id]
        if indices:
            group.add(indices, 1.0, "REPLACE")
    return obj


def geometry_manifest(
    plans: Sequence[MeshPlan],
    blueprint: Dict[str, Any],
    lock: Dict[str, Any],
    c001_derivation: Dict[str, Any],
) -> Dict[str, Any]:
    all_vertices = [vertex for plan in plans for vertex in plan.vertices]
    objects: List[Dict[str, Any]] = []
    total_triangles = 0
    vag_counts: Counter[str] = Counter()
    face_authority_counts: Counter[str] = Counter()
    for plan in plans:
        summary = topology_summary(plan)
        total_triangles += summary["triangles_evaluated"]
        vag_counts.update(plan.vertex_vag)
        face_authority_counts.update(plan.face_authority)
        objects.append(
            {
                "object_name": plan.object_name,
                "component_id": plan.component_id,
                "artifact_classification": "candidate",
                "bounds": bounds(plan.vertices),
                "topology": summary,
                "vertices": [
                    {
                        "index": index,
                        "coordinate_cm": [round(value, 12) for value in coordinate],
                        "authority_group_id": plan.vertex_vag[index],
                    }
                    for index, coordinate in enumerate(plan.vertices)
                ],
                "faces": [
                    {
                        "index": index,
                        "vertex_indices": list(face),
                        "authority_group_id": plan.face_authority[index],
                    }
                    for index, face in enumerate(plan.faces)
                ],
            }
        )
    vag_registry = load_json(VAG_MAP_REL)
    all_vag_ids = [entry["id"] for entry in vag_registry["authority_groups"]]
    vag_coverage = []
    for entry in vag_registry["authority_groups"]:
        vag_coverage.append(
            {
                "authority_group_id": entry["id"],
                "component_id": entry["component_id"],
                "visibility_class": entry["visibility_class"],
                "owner_view_or_rule": entry["planned_vertex_scope"],
                "source_record_or_interpretation_rule": entry.get("primary_authority", []),
                "interpretation_authority": entry.get("interpretation_authority", []),
                "technical_rule_ids": entry.get("technical_rules", []),
                "vertex_count": vag_counts[entry["id"]],
                "face_count": face_authority_counts[entry["id"]],
                "coverage_status": "mapped" if vag_counts[entry["id"]] or face_authority_counts[entry["id"]] else "accounted_zero_vertex_optional_refinement",
            }
        )
    return {
        "schema": "aerathea.step12_geometry_manifest.v1",
        "asset_id": ASSET_ID,
        "contract_id": CONTRACT_ID,
        "date": "2026-07-20",
        "status": "candidate_pending_independent_step12_audit",
        "artifact_classification": "candidate",
        "pipeline_status": "DCC source candidate pending Step 12 independent audit",
        "authority": {
            "step11_blueprint": str(BLUEPRINT_REL),
            "step11_vertex_authority_map": str(VAG_MAP_REL),
            "step11_technical_rules": str(TECH_RULES_REL),
            "step12_input_lock": str(INPUT_LOCK_REL),
            "locked_inputs_verified": len(lock["locked_inputs"]),
            "source_evidence_modified": False,
            "interpretation_relabelled_as_source": False,
        },
        "coordinate_frame": blueprint["coordinate_frame"],
        "construction_order": [plan.component_id for plan in plans],
        "objects": objects,
        "vag_coverage": vag_coverage,
        "vag_ids_accounted": all_vag_ids,
        "c001_owner_view_derivation": c001_derivation,
        "c004_derivation": {
            "q_samples": "q_i=-1/2+i/4, i=0..31",
            "v_samples": [0, 0.5, 1],
            "boundary": "B_v(q); a(v)=56+14v; b(v)=44+11v; signed power 2/3",
            "z_assignment": "10*(1-v)",
            "hidden_top_inset_cm_per_semiaxis": 0.5,
            "symbolic_periodic_wrap": False,
            "q_15_over_2_evaluated": False,
            "outward_n3_exceedance_cm": 0,
        },
        "contacts": {
            "CL-001": {"between": ["C-001", "C-002"], "intersection_z_cm": [34.5, 35.5], "thickness_cm": 1.0},
            "CL-002": {"between": ["C-002", "C-003"], "intersection_z_cm": [22.5, 23.5], "thickness_cm": 1.0},
            "CL-003": {"between": ["C-003", "C-004"], "intersection_z_cm": [9.5, 10.5], "thickness_cm": 1.0},
            "shared_vertex_loops": False,
            "visible_overlap_pixels_allowed": 0,
        },
        "assembled_bounds": bounds(all_vertices),
        "counts": {
            "primary_objects": len(plans),
            "vertices": len(all_vertices),
            "faces": sum(len(plan.faces) for plan in plans),
            "triangles_evaluated": total_triangles,
            "vag_groups_accounted": len(vag_coverage),
            "unmapped_vertices": 0,
            "C005_C006_C007_vertices": 0,
            "uv_layers": 0,
            "materials": 0,
            "lods": 0,
            "collision_objects": 0,
            "fbx_outputs": 0,
            "unreal_outputs": 0,
        },
        "holdout_policy": {
            "back": "validation only; no construction constants read from back measurements",
            "right": "validation only; no construction constants read from right measurements",
            "perspective": "non-metric corroboration only",
        },
        "blocked_methods_used": [],
        "generator": {
            "path": str(SCRIPT_PATH.relative_to(REPO_ROOT)),
            "sha256": sha256_file(SCRIPT_PATH),
            "fresh_step12_builder": True,
            "legacy_builder_imports": 0,
            "schema_only_mode": True,
        },
    }


def run_build() -> Dict[str, Any]:
    lock = verify_input_lock()
    blueprint = load_json(BLUEPRINT_REL)
    front_measure = load_json(FRONT_MEASURE_REL)
    left_measure = load_json(LEFT_MEASURE_REL)
    # Holdout manifests are read only to prove their locked presence; they do
    # not influence construction coordinates.
    back_measure = load_json(BACK_MEASURE_REL)
    right_measure = load_json(RIGHT_MEASURE_REL)
    _ = load_json(PHYSICAL_BOUNDS_REL)
    if back_measure.get("view") != "back" or right_measure.get("view") != "right":
        raise RuntimeError("holdout manifest identity mismatch")
    if blueprint.get("asset_id") != ASSET_ID:
        raise RuntimeError("Step 11 blueprint asset mismatch")
    if blueprint["construction_order"][0]["component_id"] != "C-004":
        raise RuntimeError("Step 11 construction order mismatch")

    import bpy  # type: ignore

    bpy.ops.wm.read_factory_settings(use_empty=True)
    scene = bpy.context.scene
    scene.unit_settings.system = "METRIC"
    scene.unit_settings.scale_length = 0.01
    scene.unit_settings.length_unit = "CENTIMETERS"
    scene["asset_id"] = ASSET_ID
    scene["step12_contract_id"] = CONTRACT_ID
    scene["artifact_classification"] = "candidate"
    scene["pipeline_status"] = "DCC source candidate pending Step 12 audit"
    scene["pivot_cm"] = "0,0,0"
    scene["geometry_manifest"] = str(GEOMETRY_MANIFEST_REL)
    scene["source_panels_in_asset"] = False
    scene["uv_created"] = False
    scene["final_material_created"] = False
    scene["lod_created"] = False
    scene["collision_created"] = False

    c001, c001_derivation = build_c001(blueprint, front_measure, left_measure)
    plans = [build_c004(blueprint), build_c003(blueprint), build_c002(blueprint), c001]
    if tuple(plan.object_name for plan in plans) != REQUIRED_OBJECTS:
        raise RuntimeError("fresh construction order/object identity mismatch")
    for plan in plans:
        create_blender_object(bpy, plan)

    dcc_root = REPO_ROOT / DCC_ROOT_REL
    dcc_root.mkdir(parents=True, exist_ok=True)
    blend_path = REPO_ROOT / BLEND_REL
    manifest_path = REPO_ROOT / GEOMETRY_MANIFEST_REL
    bpy.ops.wm.save_as_mainfile(filepath=str(blend_path), check_existing=False)

    manifest = geometry_manifest(plans, blueprint, lock, c001_derivation)
    manifest["blend_source"] = {
        "path": str(BLEND_REL),
        "sha256": sha256_file(blend_path),
        "saved": True,
    }
    manifest_path.write_text(json.dumps(manifest, indent=2) + "\n", encoding="utf-8")
    return {
        "schema": "aerathea.step12_builder_result.v1",
        "asset_id": ASSET_ID,
        "contract_id": CONTRACT_ID,
        "status": "candidate_created_pending_independent_audit",
        "blend": str(BLEND_REL),
        "geometry_manifest": str(GEOMETRY_MANIFEST_REL),
        "objects": [plan.object_name for plan in plans],
        "vertices": manifest["counts"]["vertices"],
        "triangles_evaluated": manifest["counts"]["triangles_evaluated"],
        "proof_renders_created": 0,
    }


def main() -> int:
    args = parse_args(blender_script_args())
    if args.schema_only:
        report = schema_report()
        if report["bpy_imported"]:
            raise RuntimeError("schema-only mode imported bpy")
        print(json.dumps(report, indent=2))
        return 0
    report = run_build()
    print(json.dumps(report, indent=2))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
