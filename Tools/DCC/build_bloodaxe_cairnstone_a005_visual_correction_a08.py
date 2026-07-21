#!/usr/bin/env python3
"""Build the A005 A08 individual-stone visual correction candidate."""

from __future__ import annotations

import argparse
import hashlib
import importlib.util
import json
import math
import random
import sys
from pathlib import Path
from typing import Any, Dict, List, Sequence, Set, Tuple


ROOT = Path(__file__).resolve().parents[2]
ASSET = "SM_GIA_BloodAxeCairnstone_A005"
CONTRACT = "A005-CR-VISUAL-CORRECTION-A08"
BLUEPRINT_ROOT = Path("docs/assets/blueprints") / ASSET
PLAN_REL = BLUEPRINT_ROOT / "manifests/VISUAL_CORRECTION_A08_PLAN.json"
MEASUREMENT_REL = BLUEPRINT_ROOT / "manifests/VISUAL_CORRECTION_A08_TOP_STONE_MEASUREMENT.json"
SOURCE_REL = Path("docs/assets/reference/bloodaxe_cairnstone_asset/REF_GIA_BloodAxeCairnstoneAsset_A02_BlueprintTemplate.png")
MASK_MANIFEST_REL = Path("SourceAssets/Textures/Props/Giants/BloodAxe/Cairns") / ASSET / "Technical/SM_GIA_BloodAxeCairnstone_A005_SOURCE_MASK_MANIFEST_A01.json"
TEXTURE_PARENT = Path("SourceAssets/Textures/Props/Giants/BloodAxe/Cairns") / ASSET
TEXTURE_ROOT = TEXTURE_PARENT / "VisualCorrection_A08"
BC_REL = TEXTURE_ROOT / "T_GIA_BloodAxeCairnstone_A005_VF_A08_BC.png"
N_REL = TEXTURE_ROOT / "T_GIA_BloodAxeCairnstone_A005_VF_A08_N.png"
ORM_REL = TEXTURE_ROOT / "T_GIA_BloodAxeCairnstone_A005_VF_A08_ORM.png"
DCC_ROOT = Path("SourceAssets/Blender/Props/Giants/BloodAxe/Cairns") / ASSET
BLEND_REL = DCC_ROOT / f"{ASSET}_DCCGameReady_VisualCorrection_A08.blend"
MANIFEST_REL = DCC_ROOT / f"{ASSET}_VISUAL_CORRECTION_A08_MANIFEST.json"
EXPORT_ROOT = Path("SourceAssets/Exports/Props/Giants/BloodAxe/Cairns") / ASSET / "VisualCorrection_A08"
FBX_RELS = {
    "LOD0": EXPORT_ROOT / f"{ASSET}_VisualCorrection_A08.fbx",
    "LOD1": EXPORT_ROOT / f"{ASSET}_VisualCorrection_A08_LOD1.fbx",
    "LOD2": EXPORT_ROOT / f"{ASSET}_VisualCorrection_A08_LOD2.fbx",
    "LOD3": EXPORT_ROOT / f"{ASSET}_VisualCorrection_A08_LOD3.fbx",
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


def course_intervals(source_center_angles_deg: Sequence[float]) -> List[Tuple[float, float, float]]:
    angles = sorted(float(value) for value in source_center_angles_deg)
    result: List[Tuple[float, float, float]] = []
    for index, angle in enumerate(angles):
        previous = angles[index - 1] - (360.0 if index == 0 else 0.0)
        following = angles[(index + 1) % len(angles)] + (360.0 if index + 1 == len(angles) else 0.0)
        start_source = (previous + angle) * 0.5
        end_source = (angle + following) * 0.5
        # Source image angles increase clockwise because image Y points down.
        # World +Y points up, so reverse the interval for source-aligned top view.
        result.append((-end_source, -angle, -start_source))
    return result


def stone_island(
    base: Any,
    bpy: Any,
    name: str,
    interval_deg: Tuple[float, float, float],
    outer_half: Tuple[float, float],
    inner_half: Tuple[float, float],
    z_range: Tuple[float, float],
    seed: int,
    collection: Any,
    gap_deg: float,
    bevel_width: float,
) -> Any:
    start_deg, center_deg, end_deg = interval_deg
    available = max(2.0, end_deg - start_deg)
    gap = min(gap_deg, available * 0.15)
    angles = [math.radians(start_deg + gap), math.radians(center_deg), math.radians(end_deg - gap)]
    rng = random.Random(seed)
    rubble = "APRON_CORE" in name
    outer_scales = [rng.uniform(0.935, 0.985), rng.uniform(0.965, 1.0), rng.uniform(0.935, 0.985)] if rubble else [rng.uniform(0.972, 0.992), rng.uniform(0.988, 1.0), rng.uniform(0.972, 0.992)]
    inner_scales = [rng.uniform(0.955, 1.045), rng.uniform(0.950, 1.055), rng.uniform(0.955, 1.045)] if rubble else [rng.uniform(0.982, 1.018), rng.uniform(0.978, 1.020), rng.uniform(0.982, 1.018)]
    lower, upper = z_range
    local_lower = lower + rng.uniform(0.0, 2.45 if rubble else 0.82)
    if rubble:
        crown_drop = rng.uniform(0.0, 3.10)
        top_offsets = [
            -crown_drop + rng.uniform(-1.20, -0.10),
            -crown_drop + rng.uniform(-0.65, 0.0),
            -crown_drop + rng.uniform(-1.20, -0.10),
        ]
    else:
        top_offsets = [rng.uniform(-1.15, -0.10), rng.uniform(-0.72, 0.0), rng.uniform(-1.15, -0.10)]
    path_bottom: List[Vec3] = []
    path_top: List[Vec3] = []
    for angle, scale, offset in zip(angles, outer_scales, top_offsets):
        x_value, y_value = superellipse_xy(angle, outer_half[0] * scale, outer_half[1] * scale)
        path_bottom.append((x_value, y_value, local_lower + rng.uniform(0.0, 0.10)))
        path_top.append((x_value, y_value, upper + offset))
    for angle, scale, offset in zip(reversed(angles), reversed(inner_scales), reversed(top_offsets)):
        x_value, y_value = superellipse_xy(angle, inner_half[0] * scale, inner_half[1] * scale)
        path_bottom.append((x_value, y_value, local_lower + rng.uniform(0.0, 0.10)))
        path_top.append((x_value, y_value, upper + offset - rng.uniform(0.0, 0.16)))
    vertices = [*path_bottom, *path_top]
    count = len(path_bottom)
    faces: List[List[int]] = [list(reversed(range(count))), list(range(count, count * 2))]
    for index in range(count):
        following = (index + 1) % count
        faces.append([index, following, count + following, count + index])
    result = base.create_mesh_object(bpy, name, vertices, faces, collection)
    if bevel_width > 0.0:
        modifier = result.modifiers.new("IndividualStoneEdge", "BEVEL")
        modifier.width = bevel_width
        modifier.segments = 1
        modifier.affect = "EDGES"
        base.select_only(bpy, [result])
        bpy.ops.object.modifier_apply(modifier=modifier.name)
    result["aerathea_individual_stone_island"] = True
    return result


def mortar_bed(
    base: Any,
    bpy: Any,
    name: str,
    outer_xy: Tuple[float, float],
    inner_xy: Tuple[float, float],
    z_range: Tuple[float, float],
    segments: int,
    collection: Any,
) -> Any:
    vertices: List[Vec3] = []
    for z_value, dimensions in (
        (z_range[0], outer_xy),
        (z_range[0], inner_xy),
        (z_range[1], outer_xy),
        (z_range[1], inner_xy),
    ):
        for index in range(segments):
            angle = math.tau * index / segments
            x_value, y_value = superellipse_xy(angle, dimensions[0] * 0.5, dimensions[1] * 0.5)
            vertices.append((x_value, y_value, z_value))
    outer_bottom = 0
    inner_bottom = segments
    outer_top = segments * 2
    inner_top = segments * 3
    faces: List[List[int]] = []
    for index in range(segments):
        following = (index + 1) % segments
        faces.append([outer_bottom + index, outer_bottom + following, outer_top + following, outer_top + index])
        faces.append([inner_bottom + following, inner_bottom + index, inner_top + index, inner_top + following])
        faces.append([outer_top + index, outer_top + following, inner_top + following, inner_top + index])
        faces.append([outer_bottom + following, outer_bottom + index, inner_bottom + index, inner_bottom + following])
    result = base.create_mesh_object(bpy, name, vertices, faces, collection)
    result["aerathea_mortar_bed"] = True
    result["aerathea_masonry_shell"] = False
    return result


def fit_course_bounds(obj: Any, target_xy: Tuple[float, float], target_z: Tuple[float, float]) -> None:
    coordinates = [vertex.co for vertex in obj.data.vertices]
    minimum = [min(float(point[axis]) for point in coordinates) for axis in range(3)]
    maximum = [max(float(point[axis]) for point in coordinates) for axis in range(3)]
    targets = ((-target_xy[0] * 0.5, target_xy[0] * 0.5), (-target_xy[1] * 0.5, target_xy[1] * 0.5), target_z)
    for vertex in obj.data.vertices:
        for axis in range(3):
            old_span = maximum[axis] - minimum[axis]
            new_min, new_max = targets[axis]
            vertex.co[axis] = new_min + (float(vertex.co[axis]) - minimum[axis]) * (new_max - new_min) / old_span
    obj.data.update(calc_edges=True)


def individual_course(
    base: Any,
    bpy: Any,
    name: str,
    source_angles_deg: Sequence[float],
    outer_xy: Tuple[float, float],
    inner_xy: Tuple[float, float],
    z_range: Tuple[float, float],
    seed: int,
    collection: Any,
    gap_deg: float,
    bevel_width: float,
    role: str,
    mortar_outer_xy: Tuple[float, float],
    mortar_inner_xy: Tuple[float, float],
    mortar_z: Tuple[float, float],
    mortar_segments: int,
) -> Any:
    stones = [
        stone_island(
            base,
            bpy,
            f"{name}_STONE_{index + 1:02d}",
            interval,
            (outer_xy[0] * 0.5, outer_xy[1] * 0.5),
            (inner_xy[0] * 0.5, inner_xy[1] * 0.5),
            z_range,
            seed + index * 97,
            collection,
            gap_deg,
            bevel_width,
        )
        for index, interval in enumerate(course_intervals(source_angles_deg))
    ]
    base.select_only(bpy, stones)
    bpy.context.view_layer.objects.active = stones[0]
    bpy.ops.object.join()
    result = bpy.context.object
    result.name = name
    fit_course_bounds(result, outer_xy, z_range)
    bed = mortar_bed(base, bpy, f"{name}_MORTAR_BED", mortar_outer_xy, mortar_inner_xy, mortar_z, mortar_segments, collection)
    base.select_only(bpy, [result, bed])
    bpy.context.view_layer.objects.active = result
    bpy.ops.object.join()
    result = bpy.context.object
    result.name = name
    result["aerathea_structural_role"] = role
    result["aerathea_individual_stone_count"] = len(stones)
    result["aerathea_continuous_annular_shell"] = False
    result["aerathea_recessed_mortar_bed_count"] = 1
    result["aerathea_outer_extents_cm"] = json.dumps(list(outer_xy))
    result["aerathea_visible_z_range_cm"] = json.dumps(list(z_range))
    return result


def component_indices(mesh: Any) -> List[Set[int]]:
    adjacency: List[Set[int]] = [set() for _ in mesh.vertices]
    for edge in mesh.edges:
        first, second = (int(value) for value in edge.vertices)
        adjacency[first].add(second)
        adjacency[second].add(first)
    remaining = set(range(len(mesh.vertices)))
    result: List[Set[int]] = []
    while remaining:
        start = remaining.pop()
        pending = [start]
        component = {start}
        while pending:
            current = pending.pop()
            for neighbor in adjacency[current]:
                if neighbor in remaining:
                    remaining.remove(neighbor)
                    component.add(neighbor)
                    pending.append(neighbor)
        result.append(component)
    return result


def configure_base(base: Any, a04: Any) -> None:
    base_original_loft = base.loft
    base_original_decimate = base.decimate_lod

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
    a04_copy_textures = base.copy_textures
    a04_create_materials = base.create_materials
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

    measurement = load_json(MEASUREMENT_REL)
    c002_angles = [record["construction_datum_angle_deg"] for record in measurement["courses"]["C002"]["records"]]
    c003_angles = [record["construction_datum_angle_deg"] for record in measurement["courses"]["C003"]["records"]]
    rng = random.Random(80504)
    c004_angles = [index * 11.25 + (0.0 if index % 8 == 0 else rng.uniform(-2.35, 2.35)) for index in range(32)]

    def copy_textures_a08() -> Dict[str, Dict[str, Any]]:
        records = a04_copy_textures()
        for record in records.values():
            record["a08_role"] = "A04 source-regenerated atlas retained; individual stones receive per-island UV routing"
        return records

    def loft_a08(
        bpy: Any,
        name: str,
        profiles: Sequence[Tuple[float, float, float, float]],
        segments: int,
        exponent: float,
        collection: Any,
    ) -> Any:
        if name == "MONOLITH_BODY":
            result = base_original_loft(bpy, name, a04.plinth_profiles(), 92, 4.5, collection)
            result["aerathea_structural_role"] = "exact A04 C001 plinth visual construction"
            result["aerathea_A04_plinth_preserved"] = True
            return result
        if name == "UPPER_COURSE_CORE":
            return individual_course(base, bpy, name, c002_angles, (123.846154, 92.707424), (99.0, 70.0), (23.0, 34.25), 80502, collection, 0.70, 0.58, "C002 upper course; 19 individual source-count stones", (118.0, 86.0), (98.0, 69.0), (22.40, 33.25), 24)
        if name == "LOWER_COURSE_CORE":
            return individual_course(base, bpy, name, c003_angles, (137.307692, 105.196507), (116.0, 84.0), (9.75, 22.25), 80503, collection, 0.55, 0.52, "C003 lower course; 24 individual source-count stones", (130.0, 98.0), (114.5, 82.5), (9.15, 21.70), 32)
        if name == "APRON_CORE":
            return individual_course(base, bpy, name, c004_angles, (140.0, 110.0), (124.0, 90.0), (0.0, 9.0), 80504, collection, 0.68, 0.0, "C004 peripheral rubble; 32 bounded independent stones", (130.0, 96.0), (121.5, 87.5), (0.70, 6.20), 32)
        return base_original_loft(bpy, name, profiles, segments, exponent, collection)

    def create_materials_a08(bpy: Any):
        stone, removable = a04_create_materials(bpy)
        stone.name = "M_GIA_BloodAxeCairnstone_A005_VisualCorrection_A08"
        removable.name = "M_GIA_BloodAxeCairnstone_A005_A08_REMOVED_HELPER"
        for node in stone.node_tree.nodes:
            if node.name == "A04_DIRECT_SOURCE_BASECOLOR":
                node.name = "A08_DIRECT_SOURCE_BASECOLOR"
            elif node.name == "A04_DIRECTX_NORMAL":
                node.name = "A08_DIRECTX_NORMAL"
            elif node.name == "A04_ORM_NONMETALLIC":
                node.name = "A08_ORM_NONMETALLIC"
        stone["aerathea_display_color_chain"] = "A08 exact A04 C001 UV plus disconnected per-stone source-owner UV; no grading"
        return stone, removable

    def decimate_lod_a08(bpy: Any, source: Any, name: str, ratio: float) -> Any:
        import bmesh

        result = base_original_decimate(bpy, source, name, ratio)
        bm = bmesh.new()
        bm.from_mesh(result.data)
        seen = set()
        duplicates = []
        for face in bm.faces:
            signature = tuple(
                sorted(
                    tuple(round(float(vertex.co[axis]), 6) for axis in range(3))
                    for vertex in face.verts
                )
            )
            if signature in seen:
                duplicates.append(face)
            else:
                seen.add(signature)
        if duplicates:
            bmesh.ops.delete(bm, geom=duplicates, context="FACES_ONLY")
            bm.to_mesh(result.data)
            result.data.update(calc_edges=True)
        bm.free()
        result["aerathea_duplicate_reduced_lod_faces_removed"] = len(duplicates)
        return result

    def assign_uv_a08(obj: Any) -> Dict[str, int]:
        from PIL import Image

        counts = a04_assign_uv(obj)
        mesh = obj.data
        layer = mesh.uv_layers.get("UVMap")
        if layer is None:
            raise RuntimeError("A08 UVMap missing")
        components = component_indices(mesh)
        plinth = max(components, key=lambda indices: max(float(mesh.vertices[index].co.z) for index in indices))
        non_plinth = [indices for indices in components if indices is not plinth]
        stones = []
        mortars = []
        for indices in non_plinth:
            center_x = sum(float(mesh.vertices[index].co.x) for index in indices) / len(indices)
            center_y = sum(float(mesh.vertices[index].co.y) for index in indices) / len(indices)
            (mortars if math.hypot(center_x, center_y) < 20.0 else stones).append(indices)
        stones.sort(
            key=lambda indices: (
                round(min(float(mesh.vertices[index].co.z) for index in indices), 3),
                math.atan2(
                    sum(float(mesh.vertices[index].co.y) for index in indices) / len(indices),
                    sum(float(mesh.vertices[index].co.x) for index in indices) / len(indices),
                ),
            )
        )
        uv_plan = base.load_json(base.UV_PLAN_REL)
        windows = {entry["view"]: entry["rect"] for entry in uv_plan["uv0"]["source_windows_half_open_px"]}
        mask_manifest = base.load_json(base.MASK_MANIFEST_REL)
        bboxes = {entry["view"]: entry["central_object_bbox_inclusive_px"] for entry in mask_manifest["records"]}
        row_spans: Dict[str, List[Tuple[int, int]]] = {}
        for mask_record in mask_manifest["records"]:
            view = mask_record["view"]
            mask = Image.open(ROOT / mask_record["mask_path"]).convert("L")
            pixels = mask.load()
            spans: List[Any] = []
            for row in range(mask.height):
                owned = [column for column in range(mask.width) if pixels[column, row] > 0]
                spans.append((min(owned), max(owned)) if owned else None)
            populated = [index for index, span in enumerate(spans) if span is not None]
            for row, span in enumerate(spans):
                if span is None:
                    spans[row] = spans[min(populated, key=lambda candidate: abs(candidate - row))]
            row_spans[view] = spans
        c004_vertices = {
            index
            for indices in stones
            if max(float(mesh.vertices[index].co.z) for index in indices) <= 9.001
            for index in indices
        }
        mortar_vertices = {index for indices in mortars for index in indices}
        source_reprojected_faces = 0
        for polygon in mesh.polygons:
            if all(int(index) in plinth for index in polygon.vertices) or all(int(index) in mortar_vertices for index in polygon.vertices):
                continue
            is_c004 = all(int(index) in c004_vertices for index in polygon.vertices)
            if not is_c004 and float(polygon.normal.z) <= 0.55:
                continue
            coordinates = [mesh.vertices[index].co for index in polygon.vertices]
            center = tuple(sum(float(point[axis]) for point in coordinates) / len(coordinates) for axis in range(3))
            normal = (float(polygon.normal.x), float(polygon.normal.y), float(polygon.normal.z))
            owner = "top" if normal[2] > 0.55 else base.face_owner(normal, center)
            if owner == "authored":
                continue
            for loop_index in polygon.loop_indices:
                point = mesh.vertices[mesh.loops[loop_index].vertex_index].co
                panel = base.project_point((float(point.x), float(point.y), float(point.z)), owner, bboxes[owner], row_spans[owner])
                rect = windows[owner]
                layer.data[loop_index].uv = ((rect[0] + panel[0] + 0.5) / 2048.0, 1.0 - (rect[1] + panel[1] + 0.5) / 2048.0)
            source_reprojected_faces += 1
        mortar_faces = 0
        mortar_min_z = min(float(mesh.vertices[index].co.z) for index in mortar_vertices)
        mortar_max_z = max(float(mesh.vertices[index].co.z) for index in mortar_vertices)
        for polygon in mesh.polygons:
            if not all(int(index) in mortar_vertices for index in polygon.vertices):
                continue
            for loop_index in polygon.loop_indices:
                point = mesh.vertices[mesh.loops[loop_index].vertex_index].co
                angle_value = (math.atan2(float(point.y), float(point.x)) + math.pi) / math.tau
                height_value = (float(point.z) - mortar_min_z) / max(mortar_max_z - mortar_min_z, 1.0e-6)
                pixel_x = 1672.0 + angle_value * 96.0
                pixel_y = 1912.0 + (1.0 - height_value) * 64.0
                layer.data[loop_index].uv = (pixel_x / 2048.0, 1.0 - pixel_y / 2048.0)
            mortar_faces += 1
        obj["aerathea_A08_structure"] = "exact_A04_C001_plus_75_individual_stone_islands_plus_3_recessed_mortar_beds"
        obj["aerathea_A08_individual_stone_counts"] = json.dumps({"C002": 19, "C003": 24, "C004": 32})
        obj["aerathea_A08_A07_geometry_input_count"] = 0
        obj["aerathea_A08_per_stone_uv"] = True
        obj["aerathea_A08_stone_uv_routing"] = "disconnected per-stone islands retain approved A04 cardinal/top source-owner projection"
        obj["aerathea_A08_source_reprojected_stone_faces"] = source_reprojected_faces
        obj["aerathea_A08_mortar_components"] = len(mortars)
        obj["aerathea_A08_mortar_faces"] = mortar_faces
        counts["individual_stone_components"] = len(stones)
        counts["recessed_mortar_components"] = len(mortars)
        return counts

    base.copy_textures = copy_textures_a08
    base.loft = loft_a08
    base.decimate_lod = decimate_lod_a08
    base.create_materials = create_materials_a08
    base.assign_source_uv = assign_uv_a08


def schema_report() -> Dict[str, Any]:
    plan = load_json(PLAN_REL)
    checks: Dict[str, Any] = {}
    for name, record in plan["authority_inputs"].items():
        path = ROOT / record["path"]
        actual = sha256_file(path) if path.is_file() else None
        checks[name] = {"path": record["path"], "expected_sha256": record["sha256"], "actual_sha256": actual, "pass": actual == record["sha256"]}
    measurement = load_json(MEASUREMENT_REL)
    passed = all(record["pass"] for record in checks.values()) and measurement["status"] == "pass_authoritative_measurement_gate"
    return {
        "schema": "aerathea.a005_visual_correction_a08_builder_preflight.v1",
        "asset_id": ASSET,
        "contract_id": CONTRACT,
        "status": "pass_schema_only_no_output" if passed else "blocked_authority",
        "bpy_imported": "bpy" in sys.modules,
        "authority_inputs": checks,
        "measurement_status": measurement["status"],
        "source_counts": {"C002": measurement["courses"]["C002"]["count"], "C003": measurement["courses"]["C003"]["count"], "C004": "blocked_source_exact"},
        "bounded_C004_count": 32,
        "a07_geometry_inputs": 0,
        "outputs": [str(BLEND_REL), str(MANIFEST_REL), str(BC_REL), str(N_REL), str(ORM_REL), *[str(path) for path in FBX_RELS.values()]],
    }


def build() -> Dict[str, Any]:
    preflight = schema_report()
    if preflight["status"] != "pass_schema_only_no_output":
        raise RuntimeError("A08 authority preflight blocked")
    base = load_module("a005_a08_packaging", BASE_MODULE_PATH)
    a04 = load_module("a005_a04_reference", A04_MODULE_PATH)
    configure_base(base, a04)
    preservation_paths = {"A04_blend": A04_BLEND_REL, "A04_manifest": A04_MANIFEST_REL, "A04_final": A04_FINAL_REL}
    before = {name: sha256_file(ROOT / path) for name, path in preservation_paths.items()}
    manifest = base.build()
    manifest.update(
        {
            "schema": "aerathea.a005_visual_correction_a08_candidate.v1",
            "contract_id": CONTRACT,
            "date": "2026-07-21",
            "status": "candidate_pending_a08_independent_audit",
            "artifact_classification": "candidate",
            "pipeline_status": "DCC game-ready candidate pending A08 audit and Flamestrike review",
            "recovery_from": "A07 ring deformation, course overlap, continuous-shell false pass, and component-level UV smear",
            "geometry_authority": "A08 measurement-first individual-stone construction; exact A04 C001; A07 geometry inputs zero",
            "a04_plinth_preservation": {"reference_blend": str(A04_BLEND_REL), "reference_final": str(A04_FINAL_REL), "required_exact_geometry_and_uv": True},
            "a08_structure": {
                "C001": {"role": "exact A04 plinth visual construction", "preserved": True},
                "C002": {"role": "upper masonry course", "stone_islands": 19, "source_count": True, "outer_cm": [123.846154, 92.707424], "z_cm": [23.0, 34.25]},
                "C003": {"role": "lower masonry course", "stone_islands": 24, "source_count": True, "outer_cm": [137.307692, 105.196507], "z_cm": [9.75, 22.25]},
                "C004": {"role": "peripheral rubble apron", "stone_islands": 32, "source_count": False, "bounded_rule": True, "outer_cm": [140.0, 110.0], "z_cm": [0.0, 9.0]},
            },
            "course_clearances_cm": {"C004_to_C003": 0.75, "C003_to_C002": 0.75},
            "individual_islands_total": 75,
            "recessed_mortar_beds": 3,
            "connected_shells_total": 79,
            "continuous_annular_shells": 0,
            "replacement_base": {"A04_base_geometry_inputs": 0, "A06_geometry_inputs": 0, "A07_geometry_inputs": 0},
            "uv_color": {"exact_A04_C001_uv": True, "per_stone_cardinal_and_top_source_projection": True, "mortar_authored_hidden_transition_zone": True, "vertical_smear_allowed": False, "color_grading": False},
            "preservation": {
                name: {"path": str(path), "sha256_before": digest, "sha256_after": sha256_file(ROOT / path), "pass": digest == sha256_file(ROOT / path)}
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
