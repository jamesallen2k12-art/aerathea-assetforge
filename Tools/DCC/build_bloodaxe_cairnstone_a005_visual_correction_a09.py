#!/usr/bin/env python3
"""Build the approved A005 A09 modular-base visual correction candidate."""

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
CONTRACT = "A005-CR-VISUAL-CORRECTION-A09"
BLUEPRINT_ROOT = Path("docs/assets/blueprints") / ASSET
PLAN_REL = BLUEPRINT_ROOT / "manifests/VISUAL_CORRECTION_A09_PLAN.json"
MEASUREMENT_REL = BLUEPRINT_ROOT / "manifests/VISUAL_CORRECTION_A08_TOP_STONE_MEASUREMENT.json"
SOURCE_REL = Path("docs/assets/reference/bloodaxe_cairnstone_asset/REF_GIA_BloodAxeCairnstoneAsset_A02_BlueprintTemplate.png")
TEXTURE_ROOT = Path("SourceAssets/Textures/Props/Giants/BloodAxe/Cairns") / ASSET / "VisualCorrection_A09"
BC_REL = TEXTURE_ROOT / "T_GIA_BloodAxeCairnstone_A005_VF_A09_BC.png"
N_REL = TEXTURE_ROOT / "T_GIA_BloodAxeCairnstone_A005_VF_A09_N.png"
ORM_REL = TEXTURE_ROOT / "T_GIA_BloodAxeCairnstone_A005_VF_A09_ORM.png"
DCC_ROOT = Path("SourceAssets/Blender/Props/Giants/BloodAxe/Cairns") / ASSET
BLEND_REL = DCC_ROOT / f"{ASSET}_DCCGameReady_VisualCorrection_A09.blend"
MANIFEST_REL = DCC_ROOT / f"{ASSET}_VISUAL_CORRECTION_A09_MANIFEST.json"
EXPORT_ROOT = Path("SourceAssets/Exports/Props/Giants/BloodAxe/Cairns") / ASSET / "VisualCorrection_A09"
FBX_RELS = {
    "LOD0": EXPORT_ROOT / f"{ASSET}_VisualCorrection_A09.fbx",
    "LOD1": EXPORT_ROOT / f"{ASSET}_VisualCorrection_A09_LOD1.fbx",
    "LOD2": EXPORT_ROOT / f"{ASSET}_VisualCorrection_A09_LOD2.fbx",
    "LOD3": EXPORT_ROOT / f"{ASSET}_VisualCorrection_A09_LOD3.fbx",
}
MODULE_FBX_RELS = {
    "C001": EXPORT_ROOT / "Modules" / f"{ASSET}_C001_Monolith_A09.fbx",
    "C002": EXPORT_ROOT / "Modules" / f"{ASSET}_C002_UpperCourse_A09.fbx",
    "C003": EXPORT_ROOT / "Modules" / f"{ASSET}_C003_LowerCourse_A09.fbx",
    "C004": EXPORT_ROOT / "Modules" / f"{ASSET}_C004_RubbleApron_A09.fbx",
}
A08_MODULE_PATH = ROOT / "Tools/DCC/build_bloodaxe_cairnstone_a005_visual_correction_a08.py"

Vec3 = Tuple[float, float, float]


def blender_args() -> List[str]:
    return sys.argv[sys.argv.index("--") + 1 :] if "--" in sys.argv else sys.argv[1:]


def parse_args(argv: Sequence[str]) -> argparse.Namespace:
    parser = argparse.ArgumentParser(description=__doc__)
    mode = parser.add_mutually_exclusive_group(required=True)
    mode.add_argument("--schema-only", action="store_true")
    mode.add_argument("--build", action="store_true")
    return parser.parse_args(list(argv))


def load_module(name: str, path: Path) -> Any:
    spec = importlib.util.spec_from_file_location(name, path)
    if spec is None or spec.loader is None:
        raise RuntimeError(f"cannot load {path}")
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


def sha256_file(path: Path) -> str:
    digest = hashlib.sha256()
    with path.open("rb") as handle:
        for block in iter(lambda: handle.read(1024 * 1024), b""):
            digest.update(block)
    return digest.hexdigest()


def load_json(rel: Path) -> Dict[str, Any]:
    return json.loads((ROOT / rel).read_text(encoding="utf-8"))


def configure_a08_paths(a08: Any) -> None:
    a08.CONTRACT = CONTRACT
    a08.PLAN_REL = PLAN_REL
    a08.MEASUREMENT_REL = MEASUREMENT_REL
    a08.SOURCE_REL = SOURCE_REL
    a08.TEXTURE_ROOT = TEXTURE_ROOT
    a08.BC_REL = BC_REL
    a08.N_REL = N_REL
    a08.ORM_REL = ORM_REL
    a08.BLEND_REL = BLEND_REL
    a08.MANIFEST_REL = MANIFEST_REL
    a08.EXPORT_ROOT = EXPORT_ROOT
    a08.FBX_RELS = FBX_RELS


def elliptical_radius_factor(record: Dict[str, Any], records: Sequence[Dict[str, Any]]) -> float:
    datum_x, datum_y = 136.0, 145.0
    distances = []
    for candidate in records:
        x_value, y_value = candidate["centroid_px"]
        distances.append(math.hypot(float(x_value) - datum_x, float(y_value) - datum_y))
    median = sorted(distances)[len(distances) // 2]
    x_value, y_value = record["centroid_px"]
    distance = math.hypot(float(x_value) - datum_x, float(y_value) - datum_y)
    return max(0.965, min(1.035, 1.0 + (distance / median - 1.0) * 0.34))


def irregular_xy(angle: float, half_width: float, half_depth: float, phase: float, radial_factor: float = 1.0) -> Tuple[float, float]:
    modulation = 1.0 + 0.010 * math.sin(angle * 3.0 + phase) + 0.007 * math.sin(angle * 7.0 - phase * 0.65)
    return (
        half_width * math.cos(angle) * modulation * radial_factor,
        half_depth * math.sin(angle) * modulation * radial_factor,
    )


def irregular_stone(
    base: Any,
    bpy: Any,
    name: str,
    interval_deg: Tuple[float, float, float],
    outer_half: Tuple[float, float],
    inner_half: Tuple[float, float],
    z_range: Tuple[float, float],
    seed: int,
    collection: Any,
    source_factor: float,
    gap_deg: float,
    bevel_width: float,
) -> Any:
    start_deg, center_deg, end_deg = interval_deg
    available = max(2.0, end_deg - start_deg)
    gap = min(gap_deg, available * 0.13)
    angles = [math.radians(start_deg + gap), math.radians(center_deg), math.radians(end_deg - gap)]
    rng = random.Random(seed)
    lower, upper = z_range
    local_lower = lower + rng.uniform(0.0, 0.45)
    phase = rng.uniform(-math.pi, math.pi)
    outer_scales = [
        source_factor * rng.uniform(0.978, 0.994),
        source_factor * rng.uniform(0.992, 1.010),
        source_factor * rng.uniform(0.978, 0.994),
    ]
    inner_scales = [rng.uniform(0.968, 1.030), rng.uniform(0.962, 1.035), rng.uniform(0.968, 1.030)]
    top_offsets = [rng.uniform(-1.10, -0.18), rng.uniform(-0.52, 0.0), rng.uniform(-1.10, -0.18)]
    bottom: List[Vec3] = []
    top: List[Vec3] = []
    for angle, scale, offset in zip(angles, outer_scales, top_offsets):
        x_value, y_value = irregular_xy(angle, outer_half[0], outer_half[1], phase, scale)
        bottom.append((x_value, y_value, local_lower + rng.uniform(0.0, 0.08)))
        top.append((x_value, y_value, upper + offset))
    for angle, scale, offset in zip(reversed(angles), reversed(inner_scales), reversed(top_offsets)):
        x_value, y_value = irregular_xy(angle, inner_half[0], inner_half[1], phase + 0.4, scale)
        bottom.append((x_value, y_value, local_lower + rng.uniform(0.0, 0.08)))
        top.append((x_value, y_value, upper + offset - rng.uniform(0.0, 0.14)))
    vertices = [*bottom, *top]
    count = len(bottom)
    faces: List[List[int]] = [list(reversed(range(count))), list(range(count, count * 2))]
    for index in range(count):
        following = (index + 1) % count
        faces.append([index, following, count + following, count + index])
    result = base.create_mesh_object(bpy, name, vertices, faces, collection)
    if bevel_width > 0.0:
        modifier = result.modifiers.new("A09SourceStoneEdge", "BEVEL")
        modifier.width = bevel_width
        modifier.segments = 1
        modifier.affect = "EDGES"
        base.select_only(bpy, [result])
        bpy.ops.object.modifier_apply(modifier=modifier.name)
    result["aerathea_A09_source_conditioned_stone"] = True
    result["aerathea_A09_radial_factor"] = source_factor
    return result


def rubble_stone(
    base: Any,
    bpy: Any,
    name: str,
    angle_deg: float,
    outer_row: bool,
    z_range: Tuple[float, float],
    seed: int,
    collection: Any,
) -> Any:
    rng = random.Random(seed)
    angle = math.radians(angle_deg)
    if outer_row:
        center_half = (65.5, 50.5)
        tangential_length = rng.uniform(14.0, 19.0)
        radial_width = rng.uniform(8.0, 11.5)
    else:
        center_half = (60.5, 45.5)
        tangential_length = rng.uniform(12.5, 17.5)
        radial_width = rng.uniform(7.5, 10.5)
    center_x, center_y = irregular_xy(angle, center_half[0], center_half[1], seed * 0.0007, rng.uniform(0.985, 1.015))
    radial = (math.cos(angle), math.sin(angle))
    tangent_raw = (-center_half[0] * math.sin(angle), center_half[1] * math.cos(angle))
    tangent_length = math.hypot(tangent_raw[0], tangent_raw[1])
    tangent = (tangent_raw[0] / tangent_length, tangent_raw[1] / tangent_length)
    bottom_z = z_range[0] + rng.uniform(0.0, 0.65)
    height = rng.uniform(5.6, 9.4)
    count = 6
    bottom: List[Vec3] = []
    top: List[Vec3] = []
    for index in range(count):
        local_angle = math.tau * index / count + rng.uniform(-0.12, 0.12)
        scale = rng.uniform(0.82, 1.10)
        tangent_offset = math.cos(local_angle) * tangential_length * 0.5 * scale
        radial_offset = math.sin(local_angle) * radial_width * 0.5 * scale
        x_value = center_x + tangent[0] * tangent_offset + radial[0] * radial_offset
        y_value = center_y + tangent[1] * tangent_offset + radial[1] * radial_offset
        bottom.append((x_value, y_value, bottom_z + rng.uniform(0.0, 0.18)))
        top.append((x_value + radial[0] * rng.uniform(-0.30, 0.30), y_value + radial[1] * rng.uniform(-0.30, 0.30), bottom_z + height + rng.uniform(-0.85, 0.55)))
    vertices = [*bottom, *top]
    faces: List[List[int]] = [list(reversed(range(count))), list(range(count, count * 2))]
    for index in range(count):
        following = (index + 1) % count
        faces.append([index, following, count + following, count + index])
    result = base.create_mesh_object(bpy, name, vertices, faces, collection)
    result["aerathea_A09_source_conditioned_stone"] = True
    result["aerathea_A09_local_rubble_rock"] = True
    result["aerathea_A09_rubble_row"] = "outer" if outer_row else "inner"
    result["aerathea_A09_cluster_id"] = int((angle_deg % 360.0) // 45.0)
    return result


def receiver_bed(
    base: Any,
    bpy: Any,
    name: str,
    outer_xy: Tuple[float, float],
    inner_xy: Tuple[float, float],
    z_range: Tuple[float, float],
    segments: int,
    phase: float,
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
            x_value, y_value = irregular_xy(angle, dimensions[0] * 0.5, dimensions[1] * 0.5, phase)
            vertices.append((x_value, y_value, z_value))
    outer_bottom = 0
    inner_bottom = segments
    outer_top = segments * 2
    inner_top = segments * 3
    faces: List[List[int]] = []
    for index in range(segments):
        following = (index + 1) % segments
        faces.extend(
            [
                [outer_bottom + index, outer_bottom + following, outer_top + following, outer_top + index],
                [inner_bottom + following, inner_bottom + index, inner_top + index, inner_top + following],
                [outer_bottom + following, outer_bottom + index, inner_bottom + index, inner_bottom + following],
            ]
        )
    result = base.create_mesh_object(bpy, name, vertices, faces, collection)
    result["aerathea_A09_hidden_receiver"] = True
    result["aerathea_A09_receiver_z_cm"] = json.dumps(list(z_range))
    return result


def joined_course(
    a08: Any,
    base: Any,
    bpy: Any,
    name: str,
    records: Sequence[Dict[str, Any]],
    outer_xy: Tuple[float, float],
    inner_xy: Tuple[float, float],
    z_range: Tuple[float, float],
    receiver_outer: Tuple[float, float],
    receiver_inner: Tuple[float, float],
    receiver_z: Tuple[float, float],
    seed: int,
    collection: Any,
    bevel_width: float,
    role: str,
) -> Any:
    angles = [float(record["construction_datum_angle_deg"]) for record in records]
    intervals = a08.course_intervals(angles)
    stones = []
    for index, (record, interval) in enumerate(zip(records, intervals)):
        stones.append(
            irregular_stone(
                base,
                bpy,
                f"{name}_STONE_{index + 1:02d}",
                interval,
                (outer_xy[0] * 0.5, outer_xy[1] * 0.5),
                (inner_xy[0] * 0.5, inner_xy[1] * 0.5),
                z_range,
                seed + index * 97,
                collection,
                elliptical_radius_factor(record, records),
                0.20,
                bevel_width,
            )
        )
    base.select_only(bpy, stones)
    bpy.context.view_layer.objects.active = stones[0]
    bpy.ops.object.join()
    result = bpy.context.object
    result.name = name
    a08.fit_course_bounds(result, outer_xy, z_range)
    receiver = receiver_bed(base, bpy, f"{name}_HIDDEN_RECEIVER", receiver_outer, receiver_inner, receiver_z, 32, seed * 0.001, collection)
    base.select_only(bpy, [result, receiver])
    bpy.context.view_layer.objects.active = result
    bpy.ops.object.join()
    result = bpy.context.object
    result.name = name
    result["aerathea_structural_role"] = role
    result["aerathea_A09_module"] = name
    result["aerathea_individual_stone_count"] = len(stones)
    result["aerathea_A09_hidden_receiver_count"] = 1
    result["aerathea_outer_extents_cm"] = json.dumps(list(outer_xy))
    result["aerathea_visible_z_range_cm"] = json.dumps(list(z_range))
    return result


def joined_rubble(a08: Any, base: Any, bpy: Any, collection: Any) -> Any:
    rng = random.Random(90504)
    stones = []
    index = 0
    for outer_row, row_offset in ((True, 0.0), (False, 11.25)):
        for row_index in range(16):
            angle = row_index * 22.5 + row_offset + rng.uniform(-0.85, 0.85)
            stones.append(rubble_stone(base, bpy, f"APRON_CORE_STONE_{index + 1:02d}", angle, outer_row, (0.0, 9.0), 90504 + index * 113, collection))
            index += 1
    base.select_only(bpy, stones)
    bpy.context.view_layer.objects.active = stones[0]
    bpy.ops.object.join()
    result = bpy.context.object
    result.name = "APRON_CORE"
    a08.fit_course_bounds(result, (140.0, 110.0), (0.0, 9.0))
    receiver = receiver_bed(base, bpy, "APRON_CORE_HIDDEN_RECEIVER", (124.0, 92.0), (115.0, 81.0), (0.80, 10.00), 40, 0.81, collection)
    base.select_only(bpy, [result, receiver])
    bpy.context.view_layer.objects.active = result
    bpy.ops.object.join()
    result = bpy.context.object
    result.name = "APRON_CORE"
    result["aerathea_structural_role"] = "C004 peripheral rubble; 32 bounded stones in eight staggered clusters"
    result["aerathea_A09_module"] = "C004"
    result["aerathea_individual_stone_count"] = 32
    result["aerathea_A09_cluster_count"] = 8
    result["aerathea_A09_staggered_rows"] = 2
    result["aerathea_A09_hidden_receiver_count"] = 1
    result["aerathea_outer_extents_cm"] = json.dumps([140.0, 110.0])
    result["aerathea_visible_z_range_cm"] = json.dumps([0.0, 9.0])
    return result


def add_anchor(bpy: Any, name: str, collection: Any) -> Any:
    anchor = bpy.data.objects.new(name, None)
    anchor.empty_display_type = "PLAIN_AXES"
    anchor.empty_display_size = 6.0
    anchor.location = (0.0, 0.0, 0.0)
    anchor.rotation_euler = (0.0, 0.0, 0.0)
    anchor.scale = (1.0, 1.0, 1.0)
    anchor["aerathea_shared_origin_socket"] = True
    anchor["aerathea_socket_transform_cm"] = "location=[0,0,0];rotation=[0,0,0];scale=[1,1,1]"
    collection.objects.link(anchor)
    return anchor


def patch_builder(a08: Any) -> Dict[str, Any]:
    original_configure = a08.configure_base
    module_names: Dict[str, str] = {}

    def configure_base_a09(base: Any, a04: Any) -> None:
        original_configure(base, a04)
        inherited_loft = base.loft
        inherited_join = base.join_geometry
        inherited_materials = base.create_materials
        inherited_copy_textures = base.copy_textures
        inherited_assign_uv = base.assign_source_uv
        measurement = load_json(MEASUREMENT_REL)

        def copy_textures_a09() -> Dict[str, Dict[str, Any]]:
            records = inherited_copy_textures()
            for record in records.values():
                record.pop("a08_role", None)
                record["a09_role"] = "unchanged A04 source-color atlas retained for fresh A09 modules"
            return records

        def create_materials_a09(bpy: Any):
            stone, removable = inherited_materials(bpy)
            stone.name = "M_GIA_BloodAxeCairnstone_A005_VisualCorrection_A09"
            removable.name = "M_GIA_BloodAxeCairnstone_A005_A09_REMOVED_HELPER"
            for node in stone.node_tree.nodes:
                node.name = node.name.replace("A08", "A09")
            stone["aerathea_display_color_chain"] = "A09 source-owned color on modular irregular-ovoid stones and hidden receivers; no grading"
            return stone, removable

        def loft_a09(bpy: Any, name: str, profiles: Sequence[Tuple[float, float, float, float]], segments: int, exponent: float, collection: Any) -> Any:
            if name == "MONOLITH_BODY":
                result = inherited_loft(bpy, name, profiles, segments, exponent, collection)
                result["aerathea_A09_module"] = "C001"
                return result
            if name == "UPPER_COURSE_CORE":
                return joined_course(a08, base, bpy, name, measurement["courses"]["C002"]["records"], (123.846154, 92.707424), (98.0, 68.0), (23.0, 34.25), (120.5, 89.5), (95.0, 65.0), (21.70, 35.10), 90502, collection, 0.52, "C002 independent upper masonry module; 19 source-count stones")
            if name == "LOWER_COURSE_CORE":
                return joined_course(a08, base, bpy, name, measurement["courses"]["C003"]["records"], (137.307692, 105.196507), (112.0, 80.0), (9.75, 22.25), (133.5, 101.5), (108.0, 76.0), (7.90, 22.40), 90503, collection, 0.48, "C003 independent lower masonry module; 24 source-count stones")
            if name == "APRON_CORE":
                return joined_rubble(a08, base, bpy, collection)
            return inherited_loft(bpy, name, profiles, segments, exponent, collection)

        def join_geometry_a09(bpy: Any, objects: Sequence[Any], name: str, material: Any) -> Any:
            socket_collection = bpy.data.collections.get("A09_ALIGNMENT_SOCKETS")
            if socket_collection is None:
                socket_collection = bpy.data.collections.new("A09_ALIGNMENT_SOCKETS")
                bpy.context.scene.collection.children.link(socket_collection)
            for socket_name in ("SOCKET_A005_ROOT", "SOCKET_A005_C001", "SOCKET_A005_C002", "SOCKET_A005_C003", "SOCKET_A005_C004"):
                if bpy.data.objects.get(socket_name) is None:
                    add_anchor(bpy, socket_name, socket_collection)
            return inherited_join(bpy, objects, name, material)

        def assign_uv_a09(obj: Any) -> Dict[str, int]:
            from PIL import Image

            counts = inherited_assign_uv(obj)
            mesh = obj.data
            layer = mesh.uv_layers.get("UVMap")
            if layer is None:
                raise RuntimeError("A09 UVMap missing")
            components = a08.component_indices(mesh)
            plinth = max(components, key=lambda indices: max(float(mesh.vertices[index].co.z) for index in indices))
            receivers = []
            for indices in components:
                if indices is plinth:
                    continue
                center_x = sum(float(mesh.vertices[index].co.x) for index in indices) / len(indices)
                center_y = sum(float(mesh.vertices[index].co.y) for index in indices) / len(indices)
                if math.hypot(center_x, center_y) < 20.0:
                    receivers.append(indices)
            receiver_vertices = {index for indices in receivers for index in indices}
            uv_plan = base.load_json(base.UV_PLAN_REL)
            windows = {entry["view"]: entry["rect"] for entry in uv_plan["uv0"]["source_windows_half_open_px"]}
            mask_manifest = base.load_json(base.MASK_MANIFEST_REL)
            bboxes = {entry["view"]: entry["central_object_bbox_inclusive_px"] for entry in mask_manifest["records"]}
            row_spans: Dict[str, List[Any]] = {}
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
            reprojected_receiver_faces = 0
            for polygon in mesh.polygons:
                if float(polygon.normal.z) > 0.55 or not all(int(index) in receiver_vertices for index in polygon.vertices):
                    continue
                coordinates = [mesh.vertices[index].co for index in polygon.vertices]
                center = tuple(sum(float(point[axis]) for point in coordinates) / len(coordinates) for axis in range(3))
                normal = (float(polygon.normal.x), float(polygon.normal.y), float(polygon.normal.z))
                owner = base.face_owner(normal, center)
                if owner == "authored":
                    continue
                for loop_index in polygon.loop_indices:
                    point = mesh.vertices[mesh.loops[loop_index].vertex_index].co
                    panel = base.project_point((float(point.x), float(point.y), float(point.z)), owner, bboxes[owner], row_spans[owner])
                    rect = windows[owner]
                    layer.data[loop_index].uv = ((rect[0] + panel[0] + 0.5) / 2048.0, 1.0 - (rect[1] + panel[1] + 0.5) / 2048.0)
                reprojected_receiver_faces += 1
            obj["aerathea_A09_structure"] = "exact_A04_C001_plus_independent_C002_C003_C004_modules_plus_three_full_interface_receivers"
            obj["aerathea_A09_A08_course_geometry_inputs"] = 0
            obj["aerathea_A09_source_conditioned_ovoid"] = True
            obj["aerathea_A09_background_leak_target"] = 0
            obj["aerathea_A09_module_ids"] = json.dumps(["C001", "C002", "C003", "C004"])
            obj["aerathea_A09_source_reprojected_receiver_vertical_faces"] = reprojected_receiver_faces
            counts["source_reprojected_receiver_vertical_faces"] = reprojected_receiver_faces
            return counts

        base.copy_textures = copy_textures_a09
        base.create_materials = create_materials_a09
        base.loft = loft_a09
        base.join_geometry = join_geometry_a09
        base.assign_source_uv = assign_uv_a09

    a08.configure_base = configure_base_a09
    return {"module_names": module_names}


def export_module_fbx(bpy: Any, obj: Any, socket: Any, rel: Path) -> Dict[str, Any]:
    path = ROOT / rel
    path.parent.mkdir(parents=True, exist_ok=True)
    obj.hide_viewport = False
    obj.hide_render = True
    for candidate in bpy.context.selected_objects:
        candidate.select_set(False)
    obj.select_set(True)
    socket.select_set(True)
    bpy.context.view_layer.objects.active = obj
    bpy.ops.export_scene.fbx(
        filepath=str(path),
        use_selection=True,
        object_types={"MESH", "EMPTY"},
        apply_unit_scale=True,
        apply_scale_options="FBX_SCALE_UNITS",
        axis_forward="-Z",
        axis_up="Y",
        use_mesh_modifiers=True,
        use_mesh_edges=False,
        mesh_smooth_type="FACE",
        use_tspace=True,
        use_custom_props=True,
        add_leaf_bones=False,
        bake_anim=False,
        path_mode="STRIP",
        embed_textures=False,
    )
    obj.hide_viewport = True
    return {"path": str(rel), "sha256": sha256_file(path), "bytes": path.stat().st_size, "socket": socket.name}


def extract_modules_from_lod0(bpy: Any, a08: Any, lod0: Any) -> Tuple[Dict[str, str], Dict[str, Any]]:
    import bmesh

    module_collection = bpy.data.collections.get("A09_MODULAR_COMPONENTS")
    if module_collection is None:
        module_collection = bpy.data.collections.new("A09_MODULAR_COMPONENTS")
        bpy.context.scene.collection.children.link(module_collection)
    names = {
        "C001": f"{ASSET}_C001_MONOLITH_A09",
        "C002": f"{ASSET}_C002_UPPER_COURSE_A09",
        "C003": f"{ASSET}_C003_LOWER_COURSE_A09",
        "C004": f"{ASSET}_C004_RUBBLE_APRON_A09",
    }
    groups: Dict[str, set[int]] = {key: set() for key in names}
    component_counts: Dict[str, int] = {key: 0 for key in names}
    components = a08.component_indices(lod0.data)
    for indices in components:
        minimum_z = min(float(lod0.data.vertices[index].co.z) for index in indices)
        maximum_z = max(float(lod0.data.vertices[index].co.z) for index in indices)
        if maximum_z > 40.0:
            owner = "C001"
        elif maximum_z > 22.50:
            owner = "C002"
        elif maximum_z > 10.20:
            owner = "C003"
        else:
            owner = "C004"
        groups[owner].update(indices)
        component_counts[owner] += 1
    expected_counts = {"C001": 1, "C002": 20, "C003": 25, "C004": 33}
    if component_counts != expected_counts:
        raise RuntimeError(f"A09 module component classification mismatch: {component_counts}")

    module_names: Dict[str, str] = {}
    records: Dict[str, Any] = {}
    for component, name in names.items():
        duplicate = lod0.copy()
        duplicate.data = lod0.data.copy()
        duplicate.name = name
        module_collection.objects.link(duplicate)
        bm = bmesh.new()
        bm.from_mesh(duplicate.data)
        bm.verts.ensure_lookup_table()
        remove = [vertex for vertex in bm.verts if int(vertex.index) not in groups[component]]
        bmesh.ops.delete(bm, geom=remove, context="VERTS")
        bm.to_mesh(duplicate.data)
        bm.free()
        duplicate.data.update(calc_edges=True)
        duplicate.hide_render = True
        duplicate.hide_viewport = True
        duplicate["aerathea_A09_module_id"] = component
        duplicate["aerathea_shared_origin_cm"] = "[0,0,0]"
        duplicate["aerathea_exact_LOD0_UV_subset"] = True
        module_names[component] = duplicate.name
        records[component] = {
            "connected_components": component_counts[component],
            "vertices": len(duplicate.data.vertices),
            "triangles": sum(max(0, len(polygon.vertices) - 2) for polygon in duplicate.data.polygons),
            "uv_layers": [layer.name for layer in duplicate.data.uv_layers],
            "source": "exact assembled LOD0 connected-component and UV subset",
        }
    return module_names, records


def schema_report(a08: Any) -> Dict[str, Any]:
    configure_a08_paths(a08)
    report = a08.schema_report()
    report["schema"] = "aerathea.a005_visual_correction_a09_builder_preflight.v1"
    report["contract_id"] = CONTRACT
    report["a09_modules"] = ["C001", "C002", "C003", "C004"]
    report["a09_sockets"] = ["SOCKET_A005_ROOT", "SOCKET_A005_C001", "SOCKET_A005_C002", "SOCKET_A005_C003", "SOCKET_A005_C004"]
    report["a08_course_geometry_inputs"] = 0
    report["outputs"] = [str(BLEND_REL), str(MANIFEST_REL), str(BC_REL), str(N_REL), str(ORM_REL), *[str(path) for path in FBX_RELS.values()], *[str(path) for path in MODULE_FBX_RELS.values()]]
    return report


def build(a08: Any) -> Dict[str, Any]:
    configure_a08_paths(a08)
    state = patch_builder(a08)
    manifest = a08.build()

    import bpy  # type: ignore

    module_exports: Dict[str, Any] = {}
    socket_records: Dict[str, Any] = {}
    lod0 = bpy.data.objects[f"{ASSET}_LOD0"]
    extracted_names, module_subset_records = extract_modules_from_lod0(bpy, a08, lod0)
    state["module_names"].update(extracted_names)
    for component, rel in MODULE_FBX_RELS.items():
        obj = bpy.data.objects[state["module_names"][component]]
        socket = bpy.data.objects[f"SOCKET_A005_{component}"]
        module_exports[component] = export_module_fbx(bpy, obj, socket, rel)
    for name in ("SOCKET_A005_ROOT", "SOCKET_A005_C001", "SOCKET_A005_C002", "SOCKET_A005_C003", "SOCKET_A005_C004"):
        obj = bpy.data.objects[name]
        socket_records[name] = {
            "location_cm": [round(float(value), 8) for value in obj.location],
            "rotation_rad": [round(float(value), 8) for value in obj.rotation_euler],
            "scale": [round(float(value), 8) for value in obj.scale],
        }

    blend_path = ROOT / BLEND_REL
    bpy.ops.wm.save_as_mainfile(filepath=str(blend_path), check_existing=False)
    manifest.update(
        {
            "schema": "aerathea.a005_visual_correction_a09_candidate.v1",
            "contract_id": CONTRACT,
            "date": "2026-07-21",
            "status": "candidate_pending_a09_proof_and_independent_audit",
            "artifact_classification": "candidate",
            "pipeline_status": "DCC game-ready candidate pending A09 audit and Flamestrike review",
            "recovery_from": "A08 background leaks, regular circular read, disconnected debris apron, and exposed-face detail loss",
            "geometry_authority": "fresh A09 modular construction from retained A08 counts/extents and exact A04 C001; A08 course geometry inputs zero",
            "a09_modules": {
                "C001": {"object": state["module_names"]["C001"], "preserved_exact_A04": True},
                "C002": {"object": state["module_names"]["C002"], "stone_count": 19, "outer_cm": [123.846154, 92.707424], "receiver_z_cm": [21.70, 35.10]},
                "C003": {"object": state["module_names"]["C003"], "stone_count": 24, "outer_cm": [137.307692, 105.196507], "receiver_z_cm": [7.90, 22.40]},
                "C004": {"object": state["module_names"]["C004"], "stone_count": 32, "clusters": 8, "staggered_rows": 2, "outer_cm": [140.0, 110.0], "receiver_z_cm": [0.80, 10.00]},
            },
            "module_exports": module_exports,
            "module_subset_records": module_subset_records,
            "alignment_sockets": socket_records,
            "shared_origin_cm": [0.0, 0.0, 0.0],
            "A08_course_geometry_inputs": 0,
            "hidden_interface_receivers": 3,
            "receiver_overlap_policy": "hidden inset receivers overlap all three assembly contacts behind the visible stone silhouettes without changing approved outer maxima",
            "source_conditioned_irregular_ovoid": True,
            "C004_clustered_rubble": True,
            "background_leaks_allowed": 0,
            "blend": {"path": str(BLEND_REL), "sha256": sha256_file(blend_path)},
            "unreal_outputs": 0,
            "fully_game_ready": False,
            "visual_canon": False,
        }
    )
    (ROOT / MANIFEST_REL).write_text(json.dumps(manifest, indent=2) + "\n", encoding="utf-8")
    return manifest


def main() -> int:
    args = parse_args(blender_args())
    a08 = load_module("a005_a08_reference_support", A08_MODULE_PATH)
    report = schema_report(a08) if args.schema_only else build(a08)
    if args.schema_only and report.get("bpy_imported"):
        raise RuntimeError("schema-only path imported bpy")
    print(json.dumps(report, indent=2))
    return 0 if not str(report.get("status", "")).startswith("blocked") else 1


if __name__ == "__main__":
    raise SystemExit(main())
