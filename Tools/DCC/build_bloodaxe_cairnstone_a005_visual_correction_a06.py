#!/usr/bin/env python3
"""Build the A005 A06 measured oval replacement-base candidate."""

from __future__ import annotations

import argparse
import hashlib
import importlib.util
import json
import math
import random
import sys
from pathlib import Path
from typing import Any, Dict, List, Sequence, Tuple


ROOT = Path(__file__).resolve().parents[2]
ASSET = "SM_GIA_BloodAxeCairnstone_A005"
CONTRACT = "A005-CR-VISUAL-CORRECTION-A06"
BLUEPRINT_ROOT = Path("docs/assets/blueprints") / ASSET
PLAN_REL = BLUEPRINT_ROOT / "manifests/VISUAL_CORRECTION_A06_PLAN.json"
MEASUREMENT_REL = BLUEPRINT_ROOT / "manifests/VISUAL_CORRECTION_A06_EXTERIOR_EDGE_AUDIT.json"
SOURCE_REL = Path("docs/assets/reference/bloodaxe_cairnstone_asset/REF_GIA_BloodAxeCairnstoneAsset_A02_BlueprintTemplate.png")
MASK_MANIFEST_REL = Path("SourceAssets/Textures/Props/Giants/BloodAxe/Cairns") / ASSET / "Technical/SM_GIA_BloodAxeCairnstone_A005_SOURCE_MASK_MANIFEST_A01.json"
TEXTURE_PARENT = Path("SourceAssets/Textures/Props/Giants/BloodAxe/Cairns") / ASSET
TEXTURE_ROOT = TEXTURE_PARENT / "VisualCorrection_A06"
BC_REL = TEXTURE_ROOT / "T_GIA_BloodAxeCairnstone_A005_VF_A06_BC.png"
N_REL = TEXTURE_ROOT / "T_GIA_BloodAxeCairnstone_A005_VF_A06_N.png"
ORM_REL = TEXTURE_ROOT / "T_GIA_BloodAxeCairnstone_A005_VF_A06_ORM.png"
DCC_ROOT = Path("SourceAssets/Blender/Props/Giants/BloodAxe/Cairns") / ASSET
BLEND_REL = DCC_ROOT / f"{ASSET}_DCCGameReady_VisualCorrection_A06.blend"
MANIFEST_REL = DCC_ROOT / f"{ASSET}_VISUAL_CORRECTION_A06_MANIFEST.json"
EXPORT_ROOT = Path("SourceAssets/Exports/Props/Giants/BloodAxe/Cairns") / ASSET / "VisualCorrection_A06"
FBX_RELS = {
    "LOD0": EXPORT_ROOT / f"{ASSET}_VisualCorrection_A06.fbx",
    "LOD1": EXPORT_ROOT / f"{ASSET}_VisualCorrection_A06_LOD1.fbx",
    "LOD2": EXPORT_ROOT / f"{ASSET}_VisualCorrection_A06_LOD2.fbx",
    "LOD3": EXPORT_ROOT / f"{ASSET}_VisualCorrection_A06_LOD3.fbx",
}
BASE_MODULE_PATH = ROOT / "Tools/DCC/build_bloodaxe_cairnstone_a005_visual_fidelity_recovery.py"
A04_MODULE_PATH = ROOT / "Tools/DCC/build_bloodaxe_cairnstone_a005_visual_correction_a04.py"
A04_BLEND_REL = DCC_ROOT / f"{ASSET}_DCCGameReady_VisualCorrection_A04.blend"
A04_MANIFEST_REL = DCC_ROOT / f"{ASSET}_VISUAL_CORRECTION_A04_MANIFEST.json"
A04_FINAL_REL = Path("Saved/Automation/DCC") / ASSET / "Production/VisualCorrection_A04" / f"{ASSET}_FINAL_CORRECTED_3D_A04.png"

Vec3 = Tuple[float, float, float]


def blender_args() -> List[str]:
    return sys.argv[sys.argv.index("--") + 1 :] if "--" in sys.argv else sys.argv[1:]


def parse_args(argv: Sequence[str]) -> argparse.Namespace:
    parser = argparse.ArgumentParser(description=__doc__)
    mode = parser.add_mutually_exclusive_group(required=True)
    mode.add_argument("--schema-only", action="store_true")
    mode.add_argument("--build", action="store_true")
    return parser.parse_args(list(argv))


def sha256_file(path: Path) -> str:
    digest = hashlib.sha256()
    with path.open("rb") as handle:
        for block in iter(lambda: handle.read(1024 * 1024), b""):
            digest.update(block)
    return digest.hexdigest()


def load_json(rel: Path) -> Dict[str, Any]:
    return json.loads((ROOT / rel).read_text(encoding="utf-8"))


def load_module(name: str, path: Path) -> Any:
    spec = importlib.util.spec_from_file_location(name, path)
    if spec is None or spec.loader is None:
        raise RuntimeError(f"cannot load {path}")
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


def superellipse_xy(angle: float, half_width: float, half_depth: float, exponent: float = 2.0) -> Tuple[float, float]:
    cosine = math.cos(angle)
    sine = math.sin(angle)
    return (
        half_width * math.copysign(abs(cosine) ** (2.0 / exponent), cosine),
        half_depth * math.copysign(abs(sine) ** (2.0 / exponent), sine),
    )


def masonry_course_shell(
    base: Any,
    bpy: Any,
    name: str,
    blocks: int,
    columns_per_block: int,
    rings_spec: Sequence[Tuple[float, float, float, str]],
    seed: int,
    collection: Any,
    joint_depth: float = 3.20,
    surface_inset: Tuple[float, float] = (-2.10, -0.25),
    crown_drop: Tuple[float, float] = (0.08, 0.72),
    side_z_variation: Tuple[float, float] = (-0.62, 0.68),
) -> Any:
    """One watertight elliptical course with modeled block crowns and joints."""
    rng = random.Random(seed)
    columns = blocks * columns_per_block
    # Preserve exact cardinal stations while varying the stones inside each
    # quadrant.  This removes the gear-like cadence of equal wedges without
    # sacrificing the measured owner-view footprint extrema.
    quadrant_counts = [blocks // 4] * 4
    for index in range(blocks % 4):
        quadrant_counts[index] += 1
    angular_widths: List[float] = []
    for count in quadrant_counts:
        weights = [rng.uniform(0.74, 1.28) for _ in range(count)]
        total = sum(weights)
        angular_widths.extend([(math.pi * 0.5) * weight / total for weight in weights])
    block_starts: List[float] = []
    cursor = -math.pi * 0.5
    for value in angular_widths:
        block_starts.append(cursor)
        cursor += value
    radial_offsets = [rng.uniform(*surface_inset) for _ in range(blocks)]
    crown_drops = [rng.uniform(*crown_drop) for _ in range(blocks)]
    side_z_offsets = [rng.uniform(*side_z_variation) for _ in range(blocks)]
    maximum_width = max(item[1] for item in rings_spec)
    maximum_depth = max(item[2] for item in rings_spec)

    rings: List[List[Vec3]] = []
    for z_value, width, depth, role in rings_spec:
        ring: List[Vec3] = []
        for column in range(columns):
            block = column // columns_per_block
            phase = column % columns_per_block
            angle = block_starts[block] + angular_widths[block] * phase / columns_per_block
            if phase == 0:
                radial = -joint_depth
            elif phase in (1, columns_per_block - 1):
                radial = -joint_depth * 0.34
            else:
                radial = radial_offsets[block]
            if role == "hidden":
                radial *= 0.10
            elif role == "side":
                radial *= 0.72
            else:
                radial *= 1.0
            cardinal_x = abs(abs(math.cos(angle)) - 1.0) < 1.0e-7
            cardinal_y = abs(abs(math.sin(angle)) - 1.0) < 1.0e-7
            if (cardinal_x and abs(width - maximum_width) < 1.0e-7) or (
                cardinal_y and abs(depth - maximum_depth) < 1.0e-7
            ):
                radial = 0.0
            x_value, y_value = superellipse_xy(angle, width * 0.5, depth * 0.5, 2.0)
            scale = max(0.84, 1.0 + radial / max(width * 0.5, depth * 0.5))
            local_z = z_value
            if role == "top":
                local_z -= crown_drops[block]
                if phase == 0:
                    local_z -= 0.70
                elif phase in (1, columns_per_block - 1):
                    local_z -= 0.24
            elif role == "side":
                local_z += side_z_offsets[block]
                if phase == 0:
                    local_z -= 0.24
            ring.append((x_value * scale, y_value * scale, local_z))
        rings.append(ring)
    vertices = [point for ring in rings for point in ring]
    faces: List[List[int]] = []
    for ring_index in range(len(rings) - 1):
        lower = ring_index * columns
        upper = (ring_index + 1) * columns
        for column in range(columns):
            nxt = (column + 1) % columns
            faces.append([lower + column, lower + nxt, upper + nxt, upper + column])
    bottom_center = len(vertices)
    vertices.append((0.0, 0.0, min(point[2] for point in rings[0])))
    top_center = len(vertices)
    vertices.append((0.0, 0.0, max(point[2] for point in rings[-1])))
    top_start = (len(rings) - 1) * columns
    for column in range(columns):
        nxt = (column + 1) % columns
        faces.append([bottom_center, nxt, column])
        faces.append([top_center, top_start + column, top_start + nxt])
    result = base.create_mesh_object(bpy, name, vertices, faces, collection)
    result["aerathea_masonry_blocks"] = blocks
    result["aerathea_modeled_joint_count"] = blocks
    result["aerathea_oval_exponent"] = 2.0
    result["aerathea_top_crowns_modeled"] = True
    result["aerathea_rectangular_slab"] = False
    return result


def source_panel_y_a06(view: str, z_value: float) -> float:
    mappings = {
        "front": ((35.0, 340.0), (25.5, 360.0), (10.5, 397.0), (0.0, 425.0)),
        "back": ((35.0, 233.0), (25.5, 267.0), (10.5, 300.0), (0.0, 305.0)),
        "left": ((35.0, 238.0), (25.5, 262.0), (10.5, 292.0), (0.0, 310.0)),
        "right": ((35.0, 225.0), (25.5, 248.0), (10.5, 277.0), (0.0, 283.0)),
    }
    stations = mappings[view]
    if z_value >= stations[0][0]:
        return stations[0][1]
    if z_value <= stations[-1][0]:
        return stations[-1][1]
    for first, second in zip(stations, stations[1:]):
        if second[0] <= z_value <= first[0]:
            alpha = (z_value - first[0]) / (second[0] - first[0])
            return first[1] + alpha * (second[1] - first[1])
    raise RuntimeError(view)


def base_half_extent_a06(z_value: float, axis: str) -> float:
    if z_value <= 10.5:
        outer = 70.0 if axis == "x" else 55.0
        inner = 68.653846 if axis == "x" else 52.598254
        return outer + (inner - outer) * max(0.0, z_value) / 10.5
    if z_value <= 25.5:
        lower = 68.653846 if axis == "x" else 52.598254
        upper = 64.5 if axis == "x" else 49.0
        return lower + (upper - lower) * (z_value - 10.5) / 15.0
    lower = 61.923077 if axis == "x" else 46.353712
    upper = 58.5 if axis == "x" else 44.0
    return lower + (upper - lower) * min(1.0, max(0.0, (z_value - 25.5) / 9.5))


def configure_base(base: Any, a04: Any) -> None:
    base_original_loft = base.loft
    base_original_project = base.project_point
    base_original_assign_uv = base.assign_source_uv

    a04.CONTRACT = CONTRACT
    a04.PLAN_REL = PLAN_REL
    a04.TEXTURE_ROOT = TEXTURE_ROOT
    a04.BC_REL = BC_REL
    a04.N_REL = N_REL
    a04.ORM_REL = ORM_REL
    a04.BLEND_REL = BLEND_REL
    a04.MANIFEST_REL = MANIFEST_REL
    a04.EXPORT_ROOT = EXPORT_ROOT
    a04.FBX_RELS = FBX_RELS
    a04.configure_base(base)
    a04_materials = base.create_materials
    a04_assign_uv = base.assign_source_uv

    base.CONTRACT = CONTRACT
    base.PLAN_REL = PLAN_REL
    base.SOURCE_REL = SOURCE_REL
    base.MASK_MANIFEST_REL = MASK_MANIFEST_REL
    base.OLD_TEXTURE_ROOT = TEXTURE_PARENT
    base.TEXTURE_ROOT = TEXTURE_ROOT
    base.BC_REL = BC_REL
    base.N_REL = N_REL
    base.ORM_REL = ORM_REL
    base.BLEND_REL = BLEND_REL
    base.MANIFEST_REL = MANIFEST_REL
    base.EXPORT_ROOT = EXPORT_ROOT
    base.FBX_RELS = FBX_RELS

    def loft_a06(
        bpy: Any,
        name: str,
        profiles: Sequence[Tuple[float, float, float, float]],
        segments: int,
        exponent: float,
        collection: Any,
    ) -> Any:
        if name == "MONOLITH_BODY":
            result = base_original_loft(bpy, name, a04.plinth_profiles(), 92, 4.5, collection)
            result["aerathea_structural_role"] = "exact A04 plinth visual construction"
            result["aerathea_A04_plinth_preserved"] = True
            return result
        if name == "APRON_CORE":
            result = masonry_course_shell(
                base,
                bpy,
                name,
                24,
                4,
                (
                    (0.0, 125.0, 88.0, "hidden"),
                    (1.7, 140.0, 110.0, "side"),
                    (4.5, 138.0, 107.0, "side"),
                    (7.2, 136.5, 103.0, "top"),
                    (10.5, 137.307692, 105.196507, "top"),
                ),
                70504,
                collection,
                joint_depth=4.6,
                surface_inset=(-3.8, -0.45),
                crown_drop=(0.35, 1.75),
                side_z_variation=(-1.15, 1.25),
            )
            result["aerathea_structural_role"] = "shallow peripheral oval rubble apron; not a slab"
            return result
        if name == "LOWER_COURSE_CORE":
            result = masonry_course_shell(
                base,
                bpy,
                name,
                19,
                6,
                (
                    (10.0, 130.0, 100.0, "hidden"),
                    (10.5, 137.307692, 105.196507, "side"),
                    (12.2, 137.307692, 105.196507, "side"),
                    (24.2, 130.0, 99.0, "side"),
                    (25.5, 130.0, 99.0, "top"),
                    (25.5, 123.846154, 92.707424, "top"),
                ),
                70503,
                collection,
                joint_depth=4.1,
                surface_inset=(-2.6, -0.35),
                crown_drop=(0.18, 0.92),
                side_z_variation=(-0.78, 0.86),
            )
            result["aerathea_structural_role"] = "larger lower measured oval masonry course"
            return result
        if name == "UPPER_COURSE_CORE":
            result = masonry_course_shell(
                base,
                bpy,
                name,
                17,
                6,
                (
                    (25.0, 113.0, 84.0, "hidden"),
                    (25.5, 123.846154, 92.707424, "side"),
                    (27.0, 123.846154, 92.707424, "side"),
                    (33.8, 116.0, 87.0, "side"),
                    (35.0, 116.0, 87.0, "top"),
                    (35.0, 96.0, 68.0, "top"),
                ),
                70502,
                collection,
                joint_depth=3.8,
                surface_inset=(-2.35, -0.30),
                crown_drop=(0.16, 0.82),
                side_z_variation=(-0.72, 0.80),
            )
            result["aerathea_structural_role"] = "upper supporting measured oval masonry course"
            return result
        return base_original_loft(bpy, name, profiles, segments, exponent, collection)

    def project_point_a06(point: Vec3, view: str, bbox: Sequence[int], row_spans: Sequence[Tuple[int, int]]):
        x_value, y_value, z_value = point
        if view == "top":
            if z_value >= 36.0:
                return base_original_project(point, view, bbox, row_spans)
            if z_value >= 25.0:
                center_x, center_y = 139.5, 148.5
                half_px_x, half_px_y = 92.0, 96.5
                half_cm_x, half_cm_y = 123.846154 * 0.5, 92.707424 * 0.5
                return (
                    center_x + max(-1.0, min(1.0, x_value / half_cm_x)) * half_px_x,
                    center_y - max(-1.0, min(1.0, y_value / half_cm_y)) * half_px_y,
                )
            if z_value >= 10.0:
                center_x, center_y = 139.0, 149.5
                half_px_x, half_px_y = 102.0, 109.5
                half_cm_x, half_cm_y = 137.307692 * 0.5, 105.196507 * 0.5
                return (
                    center_x + max(-1.0, min(1.0, x_value / half_cm_x)) * half_px_x,
                    center_y - max(-1.0, min(1.0, y_value / half_cm_y)) * half_px_y,
                )
            return base_original_project(point, view, bbox, row_spans)
        if view in ("front", "back", "left", "right"):
            panel_y = source_panel_y_a06(view, max(0.0, min(220.0, z_value))) if z_value < 34.0 else a04.source_panel_y(view, z_value)
            horizontal = {"front": x_value, "back": -x_value, "left": -y_value, "right": y_value}[view]
            axis = "x" if view in ("front", "back") else "y"
            half_extent = a04.interpolate_profile(z_value, axis) if z_value >= 34.0 else base_half_extent_a06(z_value, axis)
            row = max(0, min(len(row_spans) - 1, int(round(panel_y))))
            span_min, span_max = row_spans[row]
            inset = 3.0
            normalized = max(0.0, min(1.0, (horizontal + half_extent) / max(2.0 * half_extent, 1.0e-9)))
            return (span_min + inset + normalized * max(1.0, span_max - span_min - 2.0 * inset), panel_y)
        return base_original_project(point, view, bbox, row_spans)

    def create_materials_a06(bpy: Any):
        stone, removable = a04_materials(bpy)
        stone.name = "M_GIA_BloodAxeCairnstone_A005_VisualCorrection_A06"
        removable.name = "M_GIA_BloodAxeCairnstone_A005_A06_REMOVED_HELPER"
        for node in stone.node_tree.nodes:
            if node.name == "A04_DIRECT_SOURCE_BASECOLOR":
                node.name = "A06_DIRECT_SOURCE_BASECOLOR"
            elif node.name == "A04_DIRECTX_NORMAL":
                node.name = "A06_DIRECTX_NORMAL"
            elif node.name == "A04_ORM_NONMETALLIC":
                node.name = "A06_ORM_NONMETALLIC"
        stone["aerathea_display_color_chain"] = "A06 component-local exact source RGB; no gamma or grading"
        return stone, removable

    def assign_uv_a06(obj: Any) -> Dict[str, int]:
        # Capture A06's source-panel routing for the replacement base, then
        # run A04's authoritative UV pass so every C001/plinth loop remains
        # exactly equivalent to the approved A04 construction.
        counts = base_original_assign_uv(obj)
        source_layer = obj.data.uv_layers.get("UVMap")
        if source_layer is None:
            raise RuntimeError("A06 source UVMap missing")
        texel_center = 0.5 / 2048.0
        source_uv = [
            (float(loop.uv.x) + texel_center, float(loop.uv.y) - texel_center)
            for loop in source_layer.data
        ]
        a04_assign_uv(obj)
        layer = obj.data.uv_layers.get("UVMap")
        if layer is None:
            raise RuntimeError("A06 UVMap missing")
        adjacency = [set() for _ in obj.data.vertices]
        for edge in obj.data.edges:
            first, second = (int(value) for value in edge.vertices)
            adjacency[first].add(second)
            adjacency[second].add(first)
        remaining = set(range(len(obj.data.vertices)))
        components = []
        while remaining:
            start = remaining.pop()
            pending = [start]
            component = {start}
            while pending:
                current = pending.pop()
                for other in adjacency[current]:
                    if other in remaining:
                        remaining.remove(other)
                        component.add(other)
                        pending.append(other)
            components.append(component)
        plinth_indices = max(
            components,
            key=lambda component: max(float(obj.data.vertices[index].co.z) for index in component),
        )
        # Restore A06 source-panel ownership only on the three replacement
        # base components.  Connected-component ownership avoids altering the
        # irregular A04 plinth foot, whose exact vertices extend below 35 cm.
        c004_authored_faces = 0
        for polygon in obj.data.polygons:
            if all(int(index) in plinth_indices for index in polygon.vertices):
                continue
            for loop_index in polygon.loop_indices:
                layer.data[loop_index].uv = source_uv[loop_index]
        obj["aerathea_A06_structure"] = "preserved_A04_plinth_on_measured_oval_upper_and_lower_masonry_courses"
        obj["aerathea_A06_component_footprints_cm"] = json.dumps(
            {"C002": [123.846154, 92.707424], "C003": [137.307692, 105.196507], "C004": [140.0, 110.0]}
        )
        obj["aerathea_A06_component_local_top_uv"] = True
        obj["aerathea_A06_C004_authored_stone_faces"] = c004_authored_faces
        obj["aerathea_A06_color_grading"] = False
        return counts

    base.loft = loft_a06
    base.project_point = project_point_a06
    base.create_materials = create_materials_a06
    base.assign_source_uv = assign_uv_a06


def schema_report() -> Dict[str, Any]:
    plan = load_json(PLAN_REL)
    checks = {}
    for name, record in plan["authority_inputs"].items():
        path = ROOT / record["path"]
        actual = sha256_file(path) if path.is_file() else None
        checks[name] = {"path": record["path"], "expected_sha256": record["sha256"], "actual_sha256": actual, "pass": actual == record["sha256"]}
    measurement = load_json(MEASUREMENT_REL)
    passed = all(item["pass"] for item in checks.values()) and measurement["decision"] == "authoritative exterior-edge measurement record ready for A06 contract"
    return {
        "schema": "aerathea.a005_visual_correction_a06_builder_preflight.v1",
        "asset_id": ASSET,
        "contract_id": CONTRACT,
        "status": "pass_schema_only_no_output" if passed else "blocked_authority",
        "bpy_imported": "bpy" in sys.modules,
        "authority_inputs": checks,
        "measurement_decision": measurement["decision"],
        "a04_base_geometry_inputs": 0,
        "a04_plinth_construction_preserved": True,
        "outputs": [str(BLEND_REL), str(MANIFEST_REL), str(BC_REL), str(N_REL), str(ORM_REL), *[str(path) for path in FBX_RELS.values()]],
    }


def build() -> Dict[str, Any]:
    preflight = schema_report()
    if preflight["status"] != "pass_schema_only_no_output":
        raise RuntimeError("A06 authority preflight blocked")
    base = load_module("a005_a06_packaging", BASE_MODULE_PATH)
    a04 = load_module("a005_a04_reference", A04_MODULE_PATH)
    configure_base(base, a04)
    preservation_paths = {
        "A04_blend": A04_BLEND_REL,
        "A04_manifest": A04_MANIFEST_REL,
        "A04_final": A04_FINAL_REL,
    }
    before = {name: sha256_file(ROOT / path) for name, path in preservation_paths.items()}
    manifest = base.build()
    manifest.update(
        {
            "schema": "aerathea.a005_visual_correction_a06_candidate.v1",
            "contract_id": CONTRACT,
            "date": "2026-07-21",
            "status": "candidate_pending_a06_independent_audit",
            "artifact_classification": "candidate",
            "pipeline_status": "DCC game-ready candidate pending A06 audit and Flamestrike review",
            "recovery_from": "A05 visually rejected internal-alignment footprint interpretation",
            "geometry_authority": "A06 exterior-edge top-owned extents plus explicitly classified n=2 oval construction; A04 base geometry inputs zero",
            "a04_plinth_preservation": {
                "construction": "same A04 profile stations, 92 segments, exponent 4.5, projection, UV and material response",
                "reference_blend": str(A04_BLEND_REL),
                "reference_final": str(A04_FINAL_REL),
            },
            "a06_structure": {
                "C001": {"role": "exact A04 plinth visual construction", "preserved": True},
                "C002": {"role": "upper exterior-measured oval masonry course", "footprint_cm": [123.846154, 92.707424], "height_cm": 9.5, "blocks": 17, "oval_exponent": 2.0},
                "C003": {"role": "larger lower exterior-measured oval masonry course", "footprint_cm": [137.307692, 105.196507], "height_cm": 15.0, "blocks": 19, "oval_exponent": 2.0},
                "C004": {"role": "shallow oval peripheral rubble apron", "footprint_cm": [140.0, 110.0], "height_cm": 10.5, "blocks": 24, "oval_exponent": 2.0},
            },
            "replacement_base": {"A04_base_retained": False, "A04_base_hidden": False, "A04_base_geometry_inputs": 0},
            "uv_color": {"component_local_top_routing": True, "component_local_vertical_routing": True, "color_grading": False},
            "preservation": {
                name: {
                    "path": str(path),
                    "sha256_before": digest,
                    "sha256_after": sha256_file(ROOT / path),
                    "pass": digest == sha256_file(ROOT / path),
                }
                for name, (path, digest) in ((key, (preservation_paths[key], value)) for key, value in before.items())
            },
            "unreal_outputs": 0,
            "fully_game_ready": False,
            "visual_canon": False,
        }
    )
    (ROOT / MANIFEST_REL).write_text(json.dumps(manifest, indent=2) + "\n", encoding="utf-8")
    return manifest


def main() -> int:
    args = parse_args(blender_args())
    report = schema_report() if args.schema_only else build()
    if args.schema_only and report["bpy_imported"]:
        raise RuntimeError("schema-only path imported bpy")
    print(json.dumps(report, indent=2))
    return 0 if not report["status"].startswith("blocked") else 1


if __name__ == "__main__":
    raise SystemExit(main())
