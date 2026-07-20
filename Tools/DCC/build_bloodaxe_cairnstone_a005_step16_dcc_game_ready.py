#!/usr/bin/env python3
"""Build the bounded A005 Step 16 DCC game-ready package.

Schema-only mode deliberately avoids importing bpy and cannot write outputs.
Build mode must run inside Blender 3.0+ with the approved Step 15 candidate as
the startup file.
"""

from __future__ import annotations

import argparse
import hashlib
import json
import math
import re
import sys
from pathlib import Path
from typing import Any, Dict, Iterable, List, Sequence, Tuple


REPO_ROOT = Path(__file__).resolve().parents[2]
SCRIPT_PATH = Path(__file__).resolve()
ASSET = "SM_GIA_BloodAxeCairnstone_A005"
CONTRACT_ID = "A005-CR-STEP16-DCC-GAME-READY-PACKAGE-A01"
SOURCE_NAMES = ["C004_APRON", "C003_LOWER_TIER", "C002_UPPER_TIER", "C001_BODY"]
COMPONENT_IDS = ["C-004", "C-003", "C-002", "C-001"]
MATERIAL_NAME = "M_GIA_BloodAxeCairnstone_A005"

ROOT_REL = Path("SourceAssets/Blender/Props/Giants/BloodAxe/Cairns") / ASSET
SOURCE_BLEND_REL = ROOT_REL / f"{ASSET}_UVTextureMaterialCandidate_A01.blend"
OUTPUT_BLEND_REL = ROOT_REL / f"{ASSET}_DCCGameReady_A01.blend"
OUTPUT_MANIFEST_REL = ROOT_REL / f"{ASSET}_STEP16_DCC_GAME_READY_MANIFEST.json"
INPUT_LOCK_REL = Path("docs/assets/blueprints") / ASSET / "manifests/STEP_16_INPUT_LOCK.json"
BLUEPRINT_REL = Path("docs/assets/blueprints") / ASSET / "manifests/STEP_11_CONSTRUCTION_BLUEPRINT.json"
STEP15_MANIFEST_REL = ROOT_REL / f"{ASSET}_STEP15_CANDIDATE_MANIFEST.json"
TEXTURE_ROOT_REL = Path("SourceAssets/Textures/Props/Giants/BloodAxe/Cairns") / ASSET
BC_REL = TEXTURE_ROOT_REL / f"T_GIA_BloodAxeCairnstone_A005_BC.png"
NORMAL_REL = TEXTURE_ROOT_REL / f"T_GIA_BloodAxeCairnstone_A005_N.png"
ORM_REL = TEXTURE_ROOT_REL / f"T_GIA_BloodAxeCairnstone_A005_ORM.png"
EXPORT_ROOT_REL = Path("SourceAssets/Exports/Props/Giants/BloodAxe/Cairns") / ASSET
FBX_RELS = {
    "LOD0": EXPORT_ROOT_REL / f"{ASSET}.fbx",
    "LOD1": EXPORT_ROOT_REL / f"{ASSET}_LOD1.fbx",
    "LOD2": EXPORT_ROOT_REL / f"{ASSET}_LOD2.fbx",
    "LOD3": EXPORT_ROOT_REL / f"{ASSET}_LOD3.fbx",
}

APPROVED_SOURCE_HASH = "7befa56a10003c2d424de3db40e2bc402075b79644b0944413e97c92db6cab89"
APPROVED_GEOMETRY_HASH = "3707e01bc1e6fabeb4cfc500f074cba66a604dd1d1aa781a6b06e57ff35a9c57"
LIGHTMAP_RESOLUTION = 128
LIGHTMAP_PADDING_TEXELS = 4
LIGHTMAP_CHART_INSET = 4.5 / LIGHTMAP_RESOLUTION
LOD_RATIOS = {"LOD0": 1.0, "LOD1": 0.5, "LOD2": 0.225, "LOD3": 0.10}
LOD_BUDGETS = {"LOD0": 10000, "LOD1": 4000, "LOD2": 1800, "LOD3": 700}

Vec2 = Tuple[float, float]
Vec3 = Tuple[float, float, float]


def parse_args(argv: Sequence[str]) -> argparse.Namespace:
    parser = argparse.ArgumentParser(description=__doc__)
    modes = parser.add_mutually_exclusive_group(required=True)
    modes.add_argument("--schema-only", action="store_true")
    modes.add_argument("--build", action="store_true")
    return parser.parse_args(argv)


def blender_script_args() -> List[str]:
    return list(sys.argv[sys.argv.index("--") + 1 :]) if "--" in sys.argv else list(sys.argv[1:])


def sha256_file(path: Path) -> str:
    digest = hashlib.sha256()
    with path.open("rb") as handle:
        for block in iter(lambda: handle.read(1024 * 1024), b""):
            digest.update(block)
    return digest.hexdigest()


def load_json(rel: Path) -> Dict[str, Any]:
    with (REPO_ROOT / rel).open("r", encoding="utf-8") as handle:
        return json.load(handle)


def write_json(rel: Path, payload: Dict[str, Any]) -> None:
    path = REPO_ROOT / rel
    path.parent.mkdir(parents=True, exist_ok=True)
    with path.open("w", encoding="utf-8") as handle:
        json.dump(payload, handle, indent=2, sort_keys=False)
        handle.write("\n")


def validate_closed_world(value: str, label: str) -> None:
    lowered = value.lower()
    if re.search(r"(?:^|[^0-9])a00[1-4](?:[^0-9]|$)", lowered):
        raise RuntimeError(f"{label} contains forbidden legacy asset token: {value}")
    if "quarantine" in lowered or "corerecovery" in lowered or "core_recovery" in lowered:
        raise RuntimeError(f"{label} contains forbidden recovery/quarantine input: {value}")


def verify_input_lock() -> Tuple[Dict[str, Any], List[Dict[str, Any]]]:
    lock = load_json(INPUT_LOCK_REL)
    if lock.get("contract_id") != CONTRACT_ID or not lock.get("locked"):
        raise RuntimeError("Step 16 input lock is not active")
    records: List[Dict[str, Any]] = []
    for entry in lock["locked_inputs"]:
        rel = Path(entry["path"])
        validate_closed_world(entry["path"], "locked input")
        path = REPO_ROOT / rel
        actual = sha256_file(path) if path.is_file() and not path.is_symlink() else None
        match = actual == entry["sha256"]
        records.append({"path": entry["path"], "expected": entry["sha256"], "actual": actual, "match": match})
        if not match:
            raise RuntimeError(f"locked input mismatch: {entry['path']}")
    if sha256_file(REPO_ROOT / SOURCE_BLEND_REL) != APPROVED_SOURCE_HASH:
        raise RuntimeError("approved Step 15 candidate hash mismatch")
    return lock, records


def schema_report() -> Dict[str, Any]:
    lock, records = verify_input_lock()
    outputs = [OUTPUT_BLEND_REL, OUTPUT_MANIFEST_REL, *FBX_RELS.values()]
    for rel in outputs:
        validate_closed_world(str(rel), "allowed output")
    return {
        "schema": "aerathea.step16_dcc_game_ready_builder_schema.v1",
        "asset_id": ASSET,
        "contract_id": CONTRACT_ID,
        "status": "pass_schema_only_no_bpy_no_writes",
        "locked_inputs": len(records),
        "all_locked_inputs_match": all(record["match"] for record in records),
        "approved_candidate_sha256": lock["approved_candidate_sha256"],
        "allowed_outputs": [str(rel) for rel in outputs],
        "required_lods": list(LOD_RATIOS),
        "required_collision_hulls": 4,
        "unreal_outputs": 0,
    }


def mesh_triangles(mesh: Any) -> int:
    return sum(max(0, len(polygon.vertices) - 2) for polygon in mesh.polygons)


def object_bounds(obj: Any) -> Dict[str, List[float]]:
    vertices = [obj.matrix_world @ vertex.co for vertex in obj.data.vertices]
    mins = [min(float(vertex[index]) for vertex in vertices) for index in range(3)]
    maxs = [max(float(vertex[index]) for vertex in vertices) for index in range(3)]
    return {
        "min": [round(value, 9) for value in mins],
        "max": [round(value, 9) for value in maxs],
        "dimensions": [round(maxs[index] - mins[index], 9) for index in range(3)],
    }


def uv_layer_hash(mesh: Any, name: str) -> str:
    layer = mesh.uv_layers.get(name)
    if layer is None:
        return ""
    payload = json.dumps(
        [[round(float(item.uv.x), 9), round(float(item.uv.y), 9)] for item in layer.data],
        separators=(",", ":"),
    ).encode("utf-8")
    return hashlib.sha256(payload).hexdigest()


def mesh_signature(obj: Any) -> Dict[str, Any]:
    mesh = obj.data
    payload = {
        "vertices": [[round(float(value), 9) for value in vertex.co] for vertex in mesh.vertices],
        "faces": [[int(index) for index in polygon.vertices] for polygon in mesh.polygons],
    }
    encoded = json.dumps(payload, sort_keys=True, separators=(",", ":")).encode("utf-8")
    return {
        "sha256": hashlib.sha256(encoded).hexdigest(),
        "vertices": len(mesh.vertices),
        "faces": len(mesh.polygons),
        "triangles": mesh_triangles(mesh),
        "bounds": object_bounds(obj),
        "uv_layers": [layer.name for layer in mesh.uv_layers],
        "uv0_sha256": uv_layer_hash(mesh, "UVMap"),
        "uv1_sha256": uv_layer_hash(mesh, "LightmapUV"),
        "material_slots": len(mesh.materials),
    }


def duplicate_and_decimate(bpy: Any, source: Any, lod_name: str, ratio: float) -> Any:
    duplicate = source.copy()
    duplicate.data = source.data.copy()
    duplicate.name = f"TMP_{source.name}_{lod_name}"
    bpy.context.scene.collection.objects.link(duplicate)
    target = object_bounds(source)
    if ratio < 1.0:
        modifier = duplicate.modifiers.new(name=f"{lod_name}_ApprovedOrderReduction", type="DECIMATE")
        modifier.decimate_type = "COLLAPSE"
        modifier.ratio = ratio
        modifier.use_collapse_triangulate = True
        bpy.context.view_layer.objects.active = duplicate
        duplicate.select_set(True)
        bpy.ops.object.modifier_apply(modifier=modifier.name)
        duplicate.select_set(False)

        current = object_bounds(duplicate)
        for vertex in duplicate.data.vertices:
            for axis in range(3):
                old_min = current["min"][axis]
                old_span = current["dimensions"][axis]
                new_min = target["min"][axis]
                new_span = target["dimensions"][axis]
                if old_span > 1e-12:
                    vertex.co[axis] = new_min + (float(vertex.co[axis]) - old_min) * new_span / old_span
        duplicate.data.update()
    return duplicate


def component_face_records(parts: Sequence[Tuple[str, Any]]) -> Tuple[List[Vec3], List[List[int]], List[List[Vec2]], List[List[Vec2]], List[Dict[str, Any]]]:
    vertices: List[Vec3] = []
    faces: List[List[int]] = []
    uv0_faces: List[List[Vec2]] = []
    uv1_faces: List[List[Vec2]] = []
    ranges: List[Dict[str, Any]] = []
    for component_index, (component_id, obj) in enumerate(parts):
        mesh = obj.data
        base_vertex = len(vertices)
        face_start = len(faces)
        for vertex in mesh.vertices:
            vertices.append(tuple(float(value) for value in vertex.co))
        uv0 = mesh.uv_layers.get("UVMap")
        uv1 = mesh.uv_layers.get("LightmapUV")
        if uv0 is None or uv1 is None:
            raise RuntimeError(f"{obj.name} is missing required UVMap or LightmapUV")
        for polygon in mesh.polygons:
            faces.append([base_vertex + int(index) for index in polygon.vertices])
            uv0_faces.append([tuple(float(uv0.data[loop_index].uv[axis]) for axis in range(2)) for loop_index in polygon.loop_indices])
            uv1_faces.append([tuple(float(uv1.data[loop_index].uv[axis]) for axis in range(2)) for loop_index in polygon.loop_indices])
        ranges.append(
            {
                "component_id": component_id,
                "component_slot": component_index,
                "source_object": SOURCE_NAMES[component_index],
                "vertex_start": base_vertex,
                "vertex_end_exclusive": len(vertices),
                "face_start": face_start,
                "face_end_exclusive": len(faces),
                "source_triangles": mesh_triangles(mesh),
            }
        )
    return vertices, faces, uv0_faces, uv1_faces, ranges


def classify_chart(mesh: Any, polygon: Any, bounds: Dict[str, List[float]]) -> str:
    normal_z = float(polygon.normal.z)
    if normal_z >= 0.95:
        return "top"
    if normal_z <= -0.95:
        return "bottom"
    return "side"


def assign_lightmap_uv(mesh: Any, ranges: Sequence[Dict[str, Any]]) -> Dict[str, Any]:
    old = mesh.uv_layers.get("LightmapUV")
    if old is not None:
        mesh.uv_layers.remove(old)
    layer = mesh.uv_layers.new(name="LightmapUV")
    chart_counts: Dict[str, int] = {}

    for enumerated_index, record in enumerate(ranges):
        component_index = int(record.get("component_slot", enumerated_index))
        vertex_indices = range(record["vertex_start"], record["vertex_end_exclusive"])
        coordinates = [mesh.vertices[index].co for index in vertex_indices]
        bounds = {
            "min": [min(float(vertex[axis]) for vertex in coordinates) for axis in range(3)],
            "max": [max(float(vertex[axis]) for vertex in coordinates) for axis in range(3)],
        }
        spans = [max(bounds["max"][axis] - bounds["min"][axis], 1e-12) for axis in range(3)]
        rx = max(spans[0] * 0.5, 1e-12)
        ry = max(spans[1] * 0.5, 1e-12)
        center_x = (bounds["min"][0] + bounds["max"][0]) * 0.5
        center_y = (bounds["min"][1] + bounds["max"][1]) * 0.5

        angles: Dict[int, float] = {}
        for index in vertex_indices:
            vertex = mesh.vertices[index].co
            angle = math.atan2((float(vertex.y) - center_y) / ry, (float(vertex.x) - center_x) / rx)
            angles[index] = (angle + math.tau) % math.tau
        seam = min(angles.values())
        normalized = {index: ((value - seam) % math.tau) / math.tau for index, value in angles.items()}

        side_values: Dict[int, List[float]] = {}
        side_max = 1.0
        for polygon_index in range(record["face_start"], record["face_end_exclusive"]):
            polygon = mesh.polygons[polygon_index]
            chart = classify_chart(mesh, polygon, bounds)
            chart_counts[f"{record['component_id']}:{chart}"] = chart_counts.get(f"{record['component_id']}:{chart}", 0) + 1
            if chart != "side":
                continue
            values = [normalized[int(index)] for index in polygon.vertices]
            if max(values) - min(values) > 0.5:
                values = [value + 1.0 if value < 0.5 else value for value in values]
            side_values[polygon_index] = values
            side_max = max(side_max, max(values))

        row_min = component_index * 0.25
        row_max = row_min + 0.25
        chart_boxes = {
            "side": (0.0 + LIGHTMAP_CHART_INSET, row_min + LIGHTMAP_CHART_INSET, 0.5 - LIGHTMAP_CHART_INSET, row_max - LIGHTMAP_CHART_INSET),
            "top": (0.5 + LIGHTMAP_CHART_INSET, row_min + LIGHTMAP_CHART_INSET, 0.75 - LIGHTMAP_CHART_INSET, row_max - LIGHTMAP_CHART_INSET),
            "bottom": (0.75 + LIGHTMAP_CHART_INSET, row_min + LIGHTMAP_CHART_INSET, 1.0 - LIGHTMAP_CHART_INSET, row_max - LIGHTMAP_CHART_INSET),
        }

        for polygon_index in range(record["face_start"], record["face_end_exclusive"]):
            polygon = mesh.polygons[polygon_index]
            chart = classify_chart(mesh, polygon, bounds)
            x0, y0, x1, y1 = chart_boxes[chart]
            for local_index, loop_index in enumerate(polygon.loop_indices):
                vertex = mesh.vertices[polygon.vertices[local_index]].co
                if chart == "side":
                    local_u = side_values[polygon_index][local_index] / side_max
                    local_v = (float(vertex.z) - bounds["min"][2]) / spans[2]
                else:
                    local_u = (float(vertex.x) - bounds["min"][0]) / spans[0]
                    local_v = (float(vertex.y) - bounds["min"][1]) / spans[1]
                layer.data[loop_index].uv = (x0 + local_u * (x1 - x0), y0 + local_v * (y1 - y0))

    return {
        "name": "LightmapUV",
        "resolution": LIGHTMAP_RESOLUTION,
        "minimum_padding_texels": LIGHTMAP_PADDING_TEXELS,
        "chart_inset_texels": LIGHTMAP_CHART_INSET * LIGHTMAP_RESOLUTION,
        "chart_count": len(chart_counts),
        "chart_face_counts": chart_counts,
        "sha256": uv_layer_hash(mesh, "LightmapUV"),
    }


def combine_parts(bpy: Any, lod_name: str, parts: Sequence[Tuple[str, Any]], material: Any) -> Tuple[Any, Dict[str, Any]]:
    vertices, faces, uv0_faces, uv1_faces, ranges = component_face_records(parts)
    mesh = bpy.data.meshes.new(f"{ASSET}_{lod_name}_MESH")
    mesh.from_pydata(vertices, [], faces)
    mesh.update(calc_edges=True)
    uv0 = mesh.uv_layers.new(name="UVMap")
    for polygon, values in zip(mesh.polygons, uv0_faces):
        for loop_index, value in zip(polygon.loop_indices, values):
            uv0.data[loop_index].uv = value
    uv1 = mesh.uv_layers.new(name="LightmapUV")
    for polygon, values in zip(mesh.polygons, uv1_faces):
        for loop_index, value in zip(polygon.loop_indices, values):
            uv1.data[loop_index].uv = value
    mesh.materials.append(material)
    for polygon in mesh.polygons:
        polygon.material_index = 0
    lightmap = assign_lightmap_uv(mesh, ranges)
    lightmap["method"] = "post-optimization component charts classified by closure normal"
    obj = bpy.data.objects.new(f"{ASSET}_{lod_name}", mesh)
    bpy.context.scene.collection.objects.link(obj)
    obj["aerathea_asset_id"] = ASSET
    obj["aerathea_lod"] = lod_name
    obj["aerathea_component_ranges_json"] = json.dumps(ranges, separators=(",", ":"))
    obj["aerathea_lightmap_resolution"] = LIGHTMAP_RESOLUTION
    obj["aerathea_lightmap_min_padding_texels"] = LIGHTMAP_PADDING_TEXELS
    obj["aerathea_artifact_classification"] = "candidate"
    return obj, {"ranges": ranges, "lightmap": lightmap}


def remove_object(bpy: Any, obj: Any) -> None:
    mesh = obj.data if obj.type == "MESH" else None
    bpy.data.objects.remove(obj, do_unlink=True)
    if mesh is not None and mesh.users == 0:
        bpy.data.meshes.remove(mesh)


def make_proxy_mesh(bpy: Any, name: str, vertices: Sequence[Vec3], proxy_shape: str, owner: str) -> Any:
    faces = [
        [3, 2, 1, 0],
        [4, 5, 6, 7],
        [0, 1, 5, 4],
        [1, 2, 6, 5],
        [2, 3, 7, 6],
        [3, 0, 4, 7],
    ]
    mesh = bpy.data.meshes.new(f"{name}_MESH")
    mesh.from_pydata(vertices, [], faces)
    mesh.update(calc_edges=True)
    obj = bpy.data.objects.new(name, mesh)
    bpy.context.scene.collection.objects.link(obj)
    obj["aerathea_collision_owner"] = owner
    obj["aerathea_proxy_shape"] = proxy_shape
    obj["aerathea_non_rendering_interpretation"] = True
    obj.display_type = "WIRE"
    obj.hide_render = True
    return obj


def source_bounds_tuple(obj: Any) -> Tuple[float, float, float, float, float, float]:
    bounds = object_bounds(obj)
    return (*bounds["min"], *bounds["max"])


def collision_proxy(bpy: Any, index: int, source: Any) -> Tuple[Any, Dict[str, Any]]:
    xmin, ymin, zmin, xmax, ymax, zmax = source_bounds_tuple(source)
    if source.name == "C001_BODY":
        bottom_x = max(abs(xmin), abs(xmax))
        bottom_y = max(abs(ymin), abs(ymax))
        span = zmax - zmin
        top_x = 0.0
        top_y = 0.0
        for vertex in source.data.vertices:
            t = (float(vertex.co.z) - zmin) / span if span else 1.0
            if t > 1e-9:
                top_x = max(top_x, (abs(float(vertex.co.x)) - bottom_x * (1.0 - t)) / t)
                top_y = max(top_y, (abs(float(vertex.co.y)) - bottom_y * (1.0 - t)) / t)
        top_x = max(top_x, 0.01)
        top_y = max(top_y, 0.01)
        vertices = [
            (-bottom_x, -bottom_y, zmin), (bottom_x, -bottom_y, zmin),
            (bottom_x, bottom_y, zmin), (-bottom_x, bottom_y, zmin),
            (-top_x, -top_y, zmax), (top_x, -top_y, zmax),
            (top_x, top_y, zmax), (-top_x, top_y, zmax),
        ]
        shape = "source-containing rectangular tapered frustum"
        parameters = {"bottom_half_extents": [bottom_x, bottom_y], "top_half_extents": [top_x, top_y], "z": [zmin, zmax]}
    else:
        vertices = [
            (xmin, ymin, zmin), (xmax, ymin, zmin), (xmax, ymax, zmin), (xmin, ymax, zmin),
            (xmin, ymin, zmax), (xmax, ymin, zmax), (xmax, ymax, zmax), (xmin, ymax, zmax),
        ]
        shape = "source-containing axis-aligned convex box"
        parameters = {"min": [xmin, ymin, zmin], "max": [xmax, ymax, zmax]}
    name = f"UCX_{ASSET}_{index:02d}"
    obj = make_proxy_mesh(bpy, name, vertices, shape, source.name)
    return obj, {
        "name": name,
        "owner": source.name,
        "component_id": COMPONENT_IDS[SOURCE_NAMES.index(source.name)],
        "shape": shape,
        "parameters": parameters,
        "vertices": len(obj.data.vertices),
        "faces": len(obj.data.polygons),
        "triangles": mesh_triangles(obj.data),
        "bounds": object_bounds(obj),
        "convex": True,
        "closed": True,
        "source_containment_by_construction": True,
        "artifact_classification": "collision interpretation",
    }


def select_only(bpy: Any, objects: Sequence[Any]) -> None:
    bpy.ops.object.select_all(action="DESELECT")
    for obj in objects:
        obj.hide_set(False)
        obj.select_set(True)
    bpy.context.view_layer.objects.active = objects[0]


def export_fbx(bpy: Any, rel: Path, render_object: Any, collisions: Sequence[Any]) -> Dict[str, Any]:
    output = REPO_ROOT / rel
    output.parent.mkdir(parents=True, exist_ok=True)
    selected = [render_object, *collisions]
    original_name = render_object.name
    original_hide_viewport = render_object.hide_viewport
    render_object.hide_viewport = False
    if rel == FBX_RELS["LOD0"]:
        render_object.name = ASSET
    select_only(bpy, selected)
    bpy.ops.export_scene.fbx(
        filepath=str(output),
        use_selection=True,
        object_types={"MESH"},
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
    render_object.name = original_name
    render_object.hide_viewport = original_hide_viewport
    return {
        "path": str(rel),
        "sha256": sha256_file(output),
        "bytes": output.stat().st_size,
        "render_object": original_name,
        "collision_objects": [obj.name for obj in collisions],
    }


def build_package() -> Dict[str, Any]:
    lock, lock_results = verify_input_lock()
    source_hash_before = sha256_file(REPO_ROOT / SOURCE_BLEND_REL)
    blueprint = load_json(BLUEPRINT_REL)
    step15 = load_json(STEP15_MANIFEST_REL)
    if step15["geometry"]["signature"]["sha256"] != APPROVED_GEOMETRY_HASH:
        raise RuntimeError("Step 15 approved geometry signature mismatch")

    import bpy  # type: ignore

    if Path(bpy.data.filepath).resolve() != (REPO_ROOT / SOURCE_BLEND_REL).resolve():
        raise RuntimeError("build mode must open the approved Step 15 candidate as the startup file")
    mesh_objects = {obj.name: obj for obj in bpy.context.scene.objects if obj.type == "MESH"}
    if set(mesh_objects) != set(SOURCE_NAMES):
        raise RuntimeError(f"startup mesh set mismatch: {sorted(mesh_objects)}")
    sources = [mesh_objects[name] for name in SOURCE_NAMES]
    material = bpy.data.materials.get(MATERIAL_NAME)
    if material is None:
        raise RuntimeError("approved shared material is missing")

    source_uv0_hashes = {source.name: uv_layer_hash(source.data, "UVMap") for source in sources}
    source_bounds = {source.name: object_bounds(source) for source in sources}
    for component_slot, (component_id, source) in enumerate(zip(COMPONENT_IDS, sources)):
        assign_lightmap_uv(
            source.data,
            [
                {
                    "component_id": component_id,
                    "component_slot": component_slot,
                    "source_object": source.name,
                    "vertex_start": 0,
                    "vertex_end_exclusive": len(source.data.vertices),
                    "face_start": 0,
                    "face_end_exclusive": len(source.data.polygons),
                }
            ],
        )
    lod_objects: Dict[str, Any] = {}
    lod_records: Dict[str, Any] = {}
    temporary: List[Any] = []

    for lod_name, ratio in LOD_RATIOS.items():
        if lod_name == "LOD0":
            parts = list(zip(COMPONENT_IDS, sources))
        else:
            parts = []
            for component_id, source in zip(COMPONENT_IDS, sources):
                duplicate = duplicate_and_decimate(bpy, source, lod_name, ratio)
                temporary.append(duplicate)
                parts.append((component_id, duplicate))
        combined, metadata = combine_parts(bpy, lod_name, parts, material)
        lod_objects[lod_name] = combined
        record = mesh_signature(combined)
        record.update(metadata)
        record["ratio_requested_from_actual_lod0"] = ratio
        record["budget_triangles"] = LOD_BUDGETS[lod_name]
        record["budget_pass"] = record["triangles"] <= LOD_BUDGETS[lod_name]
        record["artifact_classification"] = "candidate" if lod_name == "LOD0" else "optimization interpretation"
        lod_records[lod_name] = record

    for obj in temporary:
        remove_object(bpy, obj)

    collision_objects: List[Any] = []
    collision_records: List[Dict[str, Any]] = []
    collision_order = [sources[3], sources[2], sources[1], sources[0]]
    for index, source in enumerate(collision_order):
        obj, record = collision_proxy(bpy, index, source)
        collision_objects.append(obj)
        collision_records.append(record)

    for source in sources:
        remove_object(bpy, source)

    for lod_name, obj in lod_objects.items():
        obj.hide_render = lod_name != "LOD0"
        obj.hide_viewport = lod_name != "LOD0"
    for obj in collision_objects:
        obj.hide_render = True

    scene = bpy.context.scene
    scene.unit_settings.system = "METRIC"
    scene.unit_settings.scale_length = 0.01
    scene.unit_settings.length_unit = "CENTIMETERS"
    scene["aerathea_asset_id"] = ASSET
    scene["aerathea_contract_id"] = CONTRACT_ID
    scene["aerathea_pipeline_status"] = "DCC game-ready candidate pending Step 16 independent audit"
    scene["aerathea_fully_game_ready"] = False
    scene["aerathea_unreal_work_performed"] = False
    scene["aerathea_step17_approved"] = False
    scene["aerathea_visual_canon"] = False
    scene["aerathea_source_candidate_sha256"] = source_hash_before

    blend_path = REPO_ROOT / OUTPUT_BLEND_REL
    blend_path.parent.mkdir(parents=True, exist_ok=True)
    bpy.ops.wm.save_as_mainfile(filepath=str(blend_path), check_existing=False)

    exports: Dict[str, Any] = {}
    for lod_name, rel in FBX_RELS.items():
        exports[lod_name] = export_fbx(bpy, rel, lod_objects[lod_name], collision_objects if lod_name == "LOD0" else [])
    bpy.ops.object.select_all(action="DESELECT")

    source_hash_after = sha256_file(REPO_ROOT / SOURCE_BLEND_REL)
    if source_hash_after != source_hash_before:
        raise RuntimeError("immutable Step 15 candidate changed during Step 16 build")
    if not all(lod_records[name]["triangles"] > lod_records[next_name]["triangles"] for name, next_name in zip(["LOD0", "LOD1", "LOD2"], ["LOD1", "LOD2", "LOD3"])):
        raise RuntimeError("LOD triangle counts are not strictly monotonic")

    manifest: Dict[str, Any] = {
        "schema": "aerathea.step16_dcc_game_ready_package_manifest.v1",
        "asset_id": ASSET,
        "contract_id": CONTRACT_ID,
        "date": "2026-07-20",
        "status": "candidate_pending_step16_independent_audit",
        "artifact_classification": "candidate",
        "pipeline_status": "DCC game-ready candidate pending technical audit",
        "authority": {
            "step16_execution": lock["flamestrike_authority"]["step16_statement"],
            "focused_step15_visual_decision": "approved",
            "input_lock": str(INPUT_LOCK_REL),
            "locked_inputs": len(lock_results),
            "matched_inputs": sum(1 for result in lock_results if result["match"]),
            "pre_action_checkpoint": lock["pre_action_checkpoint"],
        },
        "immutable_source": {
            "path": str(SOURCE_BLEND_REL),
            "sha256_before": source_hash_before,
            "sha256_after": source_hash_after,
            "unchanged": source_hash_before == source_hash_after == APPROVED_SOURCE_HASH,
            "geometry_sha256": APPROVED_GEOMETRY_HASH,
            "source_uv0_hashes": source_uv0_hashes,
            "source_bounds": source_bounds,
        },
        "dcc_source": {
            "path": str(OUTPUT_BLEND_REL),
            "sha256": sha256_file(blend_path),
            "unit": "centimeter",
            "unreal_unit_equivalence": "1 Blender centimeter = 1 Unreal Unit",
            "pivot_cm": [0, 0, 0],
            "assembled_bounds_cm": lod_records["LOD0"]["bounds"],
        },
        "lods": lod_records,
        "lod_policy": {
            "actual_approved_lod0_triangles": lod_records["LOD0"]["triangles"],
            "planning_target_does_not_authorize_subdivision": True,
            "strictly_monotonic": True,
            "preservation": ["exact LOD0", "four disconnected component shells", "220/140/110 cm envelope", "four-layer read", "ground pivot"],
        },
        "lightmap_uv": {
            "name": "LightmapUV",
            "resolution": LIGHTMAP_RESOLUTION,
            "minimum_padding_texels": LIGHTMAP_PADDING_TEXELS,
            "chart_inset_texels": LIGHTMAP_CHART_INSET * LIGHTMAP_RESOLUTION,
            "charts_per_component": 3,
            "components": 4,
            "source_rgb_consumer": False,
            "artifact_classification": "UV interpretation",
        },
        "collision": {
            "strategy": blueprint["collision_plan"]["strategy"],
            "complex_as_simple": False,
            "hull_count": len(collision_records),
            "hulls": collision_records,
            "artifact_classification": "collision interpretation",
        },
        "material": {
            "name": MATERIAL_NAME,
            "slots_per_lod": 1,
            "opaque": True,
            "two_sided": False,
            "emissive": False,
            "redesign": False,
        },
        "textures": {
            "base_color": {"path": str(BC_REL), "sha256": sha256_file(REPO_ROOT / BC_REL)},
            "normal": {"path": str(NORMAL_REL), "sha256": sha256_file(REPO_ROOT / NORMAL_REL), "space": "DirectX tangent"},
            "orm": {"path": str(ORM_REL), "sha256": sha256_file(REPO_ROOT / ORM_REL), "packing": "R=AO G=Roughness B=Metallic"},
            "changed": False,
        },
        "fbx_package": exports,
        "evidence_interpretation": {
            "evidence": ["locked files and hashes", "approved LOD0 geometry", "approved UV0", "approved maps and material", "numeric audit outputs"],
            "interpretation": ["LightmapUV", "LOD1-LOD3 optimization", "collision proxies", "FBX consumer conversion", "rendered proof pixels"],
        },
        "forbidden_outputs": {
            "source_visual_redesign": 0,
            "material_redesign": 0,
            "texture_changes": 0,
            "unreal": 0,
            "step17_approval": 0,
            "fully_game_ready": 0,
            "visual_canon": 0,
        },
    }
    write_json(OUTPUT_MANIFEST_REL, manifest)
    manifest["manifest_sha256_before_self_reference"] = sha256_file(REPO_ROOT / OUTPUT_MANIFEST_REL)
    write_json(OUTPUT_MANIFEST_REL, manifest)
    return manifest


def main() -> int:
    args = parse_args(blender_script_args())
    report = schema_report() if args.schema_only else build_package()
    summary = {
        "status": report["status"],
        "asset_id": ASSET,
        "contract_id": CONTRACT_ID,
    }
    if args.build:
        summary.update(
            {
                "dcc_source": report["dcc_source"],
                "lod_triangles": {name: record["triangles"] for name, record in report["lods"].items()},
                "collision_hulls": report["collision"]["hull_count"],
                "fbx_files": len(report["fbx_package"]),
            }
        )
    print(json.dumps(summary, indent=2))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
