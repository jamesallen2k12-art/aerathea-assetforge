#!/usr/bin/env python3
"""Independently audit and prove the A005 Step 16 DCC game-ready package.

Schema-only mode avoids bpy and writes nothing. Technical audit, proof render,
and final validation modes run in Blender with the Step 16 DCC source open.
"""

from __future__ import annotations

import argparse
import collections
import hashlib
import json
import math
import re
import sys
from pathlib import Path
from typing import Any, Dict, Iterable, List, Sequence, Tuple


REPO_ROOT = Path(__file__).resolve().parents[2]
ASSET = "SM_GIA_BloodAxeCairnstone_A005"
CONTRACT_ID = "A005-CR-STEP16-DCC-GAME-READY-PACKAGE-A01"
SOURCE_NAMES = ["C004_APRON", "C003_LOWER_TIER", "C002_UPPER_TIER", "C001_BODY"]
COMPONENT_IDS = ["C-004", "C-003", "C-002", "C-001"]
MATERIAL_NAME = "M_GIA_BloodAxeCairnstone_A005"

ROOT_REL = Path("SourceAssets/Blender/Props/Giants/BloodAxe/Cairns") / ASSET
SOURCE_BLEND_REL = ROOT_REL / f"{ASSET}_UVTextureMaterialCandidate_A01.blend"
DCC_BLEND_REL = ROOT_REL / f"{ASSET}_DCCGameReady_A01.blend"
MANIFEST_REL = ROOT_REL / f"{ASSET}_STEP16_DCC_GAME_READY_MANIFEST.json"
STEP15_MANIFEST_REL = ROOT_REL / f"{ASSET}_STEP15_CANDIDATE_MANIFEST.json"
INPUT_LOCK_REL = Path("docs/assets/blueprints") / ASSET / "manifests/STEP_16_INPUT_LOCK.json"
VALIDATION_REL = Path("docs/assets/blueprints") / ASSET / "manifests/STEP_16_VALIDATION_MANIFEST.json"
TEXTURE_ROOT_REL = Path("SourceAssets/Textures/Props/Giants/BloodAxe/Cairns") / ASSET
BC_REL = TEXTURE_ROOT_REL / "T_GIA_BloodAxeCairnstone_A005_BC.png"
NORMAL_REL = TEXTURE_ROOT_REL / "T_GIA_BloodAxeCairnstone_A005_N.png"
ORM_REL = TEXTURE_ROOT_REL / "T_GIA_BloodAxeCairnstone_A005_ORM.png"
EXPORT_ROOT_REL = Path("SourceAssets/Exports/Props/Giants/BloodAxe/Cairns") / ASSET
FBX_RELS = {
    "LOD0": EXPORT_ROOT_REL / f"{ASSET}.fbx",
    "LOD1": EXPORT_ROOT_REL / f"{ASSET}_LOD1.fbx",
    "LOD2": EXPORT_ROOT_REL / f"{ASSET}_LOD2.fbx",
    "LOD3": EXPORT_ROOT_REL / f"{ASSET}_LOD3.fbx",
}
PROOF_ROOT_REL = Path("Saved/Automation/DCC") / ASSET / "Production/Step16"
PREPROOF_REL = PROOF_ROOT_REL / "STEP_16_PREPROOF_TECHNICAL_AUDIT.json"
FBX_AUDIT_REL = PROOF_ROOT_REL / "STEP_16_IMPORTED_FBX_AUDIT.json"
PROOF_AUDIT_REL = PROOF_ROOT_REL / "STEP_16_DCC_PROOF_AUDIT.json"
BOARD_REL = PROOF_ROOT_REL / f"{ASSET}_STEP16_DCC_GAME_READY_REVIEW_BOARD.png"
RENDER_RELS = {lod: PROOF_ROOT_REL / f"{ASSET}_STEP16_{lod}.png" for lod in ("LOD0", "LOD1", "LOD2", "LOD3")}
RENDER_RELS["COLLISION"] = PROOF_ROOT_REL / f"{ASSET}_STEP16_COLLISION.png"
RENDER_RELS["IMPORTED_FBX"] = PROOF_ROOT_REL / f"{ASSET}_STEP16_IMPORTED_FBX.png"

APPROVED_SOURCE_HASH = "7befa56a10003c2d424de3db40e2bc402075b79644b0944413e97c92db6cab89"
APPROVED_GEOMETRY_HASH = "3707e01bc1e6fabeb4cfc500f074cba66a604dd1d1aa781a6b06e57ff35a9c57"
LIGHTMAP_RESOLUTION = 128
LIGHTMAP_PADDING_TEXELS = 4
LIGHTMAP_CHART_INSET = 4.5 / LIGHTMAP_RESOLUTION
LOD_BUDGETS = {"LOD0": 10000, "LOD1": 4000, "LOD2": 1800, "LOD3": 700}
EXPECTED_BOUNDS = {"min": [-70.0, -55.0, 0.0], "max": [70.0, 55.0, 220.0], "dimensions": [140.0, 110.0, 220.0]}
EPS = 1e-6

Vec2 = Tuple[float, float]
Vec3 = Tuple[float, float, float]


def parse_args(argv: Sequence[str]) -> argparse.Namespace:
    parser = argparse.ArgumentParser(description=__doc__)
    modes = parser.add_mutually_exclusive_group(required=True)
    modes.add_argument("--schema-only", action="store_true")
    modes.add_argument("--audit", action="store_true")
    modes.add_argument("--render-proofs", action="store_true")
    modes.add_argument("--final", action="store_true")
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
        raise RuntimeError(f"{label} contains forbidden legacy token: {value}")
    if "quarantine" in lowered or "corerecovery" in lowered or "core_recovery" in lowered:
        raise RuntimeError(f"{label} contains forbidden recovery/quarantine input: {value}")


def verify_lock() -> Tuple[Dict[str, Any], List[Dict[str, Any]]]:
    lock = load_json(INPUT_LOCK_REL)
    if lock.get("contract_id") != CONTRACT_ID or not lock.get("locked"):
        raise RuntimeError("Step 16 input lock is not active")
    results: List[Dict[str, Any]] = []
    for entry in lock["locked_inputs"]:
        validate_closed_world(entry["path"], "locked input")
        path = REPO_ROOT / entry["path"]
        actual = sha256_file(path) if path.is_file() and not path.is_symlink() else None
        results.append({"path": entry["path"], "expected": entry["sha256"], "actual": actual, "match": actual == entry["sha256"]})
    return lock, results


def schema_report() -> Dict[str, Any]:
    lock, results = verify_lock()
    return {
        "schema": "aerathea.step16_dcc_game_ready_auditor_schema.v1",
        "asset_id": ASSET,
        "contract_id": CONTRACT_ID,
        "status": "pass_schema_only_no_bpy_no_writes" if all(item["match"] for item in results) else "blocked_locked_input_mismatch",
        "locked_inputs": len(results),
        "matched_inputs": sum(1 for item in results if item["match"]),
        "approved_candidate_sha256": lock["approved_candidate_sha256"],
        "technical_gates": 17,
        "proof_outputs": [str(path) for path in [*RENDER_RELS.values(), BOARD_REL, PROOF_AUDIT_REL]],
        "tracked_final_validation": str(VALIDATION_REL),
        "unreal_outputs": 0,
    }


def gate(identifier: str, passed: bool | None, detail: Any) -> Dict[str, Any]:
    return {"id": identifier, "status": "pending" if passed is None else ("pass" if passed else "fail"), "detail": detail}


def mesh_triangles(mesh: Any) -> int:
    return sum(max(0, len(polygon.vertices) - 2) for polygon in mesh.polygons)


def object_world_vertices(obj: Any) -> List[Vec3]:
    return [tuple(float(value) for value in (obj.matrix_world @ vertex.co)) for vertex in obj.data.vertices]


def bounds_from_vertices(vertices: Sequence[Vec3]) -> Dict[str, List[float]]:
    mins = [min(vertex[axis] for vertex in vertices) for axis in range(3)]
    maxs = [max(vertex[axis] for vertex in vertices) for axis in range(3)]
    return {
        "min": [round(value, 7) for value in mins],
        "max": [round(value, 7) for value in maxs],
        "dimensions": [round(maxs[axis] - mins[axis], 7) for axis in range(3)],
    }


def bounds_match(actual: Dict[str, List[float]], expected: Dict[str, List[float]], tolerance: float = EPS) -> bool:
    return all(abs(actual[key][index] - expected[key][index]) <= tolerance for key in ("min", "max", "dimensions") for index in range(3))


def uv_layer_hash(mesh: Any, name: str) -> str:
    layer = mesh.uv_layers.get(name)
    if layer is None:
        return ""
    payload = json.dumps([[round(float(item.uv.x), 9), round(float(item.uv.y), 9)] for item in layer.data], separators=(",", ":")).encode("utf-8")
    return hashlib.sha256(payload).hexdigest()


def edge_counts(mesh: Any) -> collections.Counter[Tuple[int, int]]:
    counts: collections.Counter[Tuple[int, int]] = collections.Counter()
    for polygon in mesh.polygons:
        indices = [int(index) for index in polygon.vertices]
        for start, end in zip(indices, indices[1:] + indices[:1]):
            counts[tuple(sorted((start, end)))] += 1
    return counts


def connected_component_count(mesh: Any) -> int:
    adjacency: Dict[int, set[int]] = {index: set() for index in range(len(mesh.vertices))}
    for (start, end), count in edge_counts(mesh).items():
        if count:
            adjacency[start].add(end)
            adjacency[end].add(start)
    remaining = set(adjacency)
    components = 0
    while remaining:
        components += 1
        stack = [remaining.pop()]
        while stack:
            for neighbor in adjacency[stack.pop()]:
                if neighbor in remaining:
                    remaining.remove(neighbor)
                    stack.append(neighbor)
    return components


def triangle_area(a: Vec3, b: Vec3, c: Vec3) -> float:
    ab = (b[0] - a[0], b[1] - a[1], b[2] - a[2])
    ac = (c[0] - a[0], c[1] - a[1], c[2] - a[2])
    cross = (ab[1] * ac[2] - ab[2] * ac[1], ab[2] * ac[0] - ab[0] * ac[2], ab[0] * ac[1] - ab[1] * ac[0])
    return 0.5 * math.sqrt(sum(value * value for value in cross))


def mesh_volume_and_degenerates(obj: Any) -> Tuple[float, int]:
    vertices = object_world_vertices(obj)
    volume = 0.0
    degenerates = 0
    for polygon in obj.data.polygons:
        indices = [int(index) for index in polygon.vertices]
        anchor = vertices[indices[0]]
        for offset in range(1, len(indices) - 1):
            b = vertices[indices[offset]]
            c = vertices[indices[offset + 1]]
            if triangle_area(anchor, b, c) <= 1e-10:
                degenerates += 1
            volume += (
                anchor[0] * (b[1] * c[2] - b[2] * c[1])
                - anchor[1] * (b[0] * c[2] - b[2] * c[0])
                + anchor[2] * (b[0] * c[1] - b[1] * c[0])
            ) / 6.0
    return volume, degenerates


def polygon_area_2d(polygon: Sequence[Vec2]) -> float:
    return abs(sum(polygon[index][0] * polygon[(index + 1) % len(polygon)][1] - polygon[(index + 1) % len(polygon)][0] * polygon[index][1] for index in range(len(polygon)))) * 0.5


def signed_area_2d(polygon: Sequence[Vec2]) -> float:
    return sum(polygon[index][0] * polygon[(index + 1) % len(polygon)][1] - polygon[(index + 1) % len(polygon)][0] * polygon[index][1] for index in range(len(polygon))) * 0.5


def line_intersection(a: Vec2, b: Vec2, c: Vec2, d: Vec2) -> Vec2:
    ab = (b[0] - a[0], b[1] - a[1])
    cd = (d[0] - c[0], d[1] - c[1])
    denominator = ab[0] * cd[1] - ab[1] * cd[0]
    if abs(denominator) < 1e-15:
        return b
    t = ((c[0] - a[0]) * cd[1] - (c[1] - a[1]) * cd[0]) / denominator
    return (a[0] + t * ab[0], a[1] + t * ab[1])


def convex_intersection(subject: Sequence[Vec2], clip: Sequence[Vec2]) -> List[Vec2]:
    output = list(subject)
    if not output:
        return []
    clip_points = list(clip)
    if signed_area_2d(clip_points) < 0:
        clip_points.reverse()
    for start, end in zip(clip_points, clip_points[1:] + clip_points[:1]):
        input_points = output
        output = []
        if not input_points:
            break
        previous = input_points[-1]
        for current in input_points:
            current_inside = (end[0] - start[0]) * (current[1] - start[1]) - (end[1] - start[1]) * (current[0] - start[0]) >= -1e-12
            previous_inside = (end[0] - start[0]) * (previous[1] - start[1]) - (end[1] - start[1]) * (previous[0] - start[0]) >= -1e-12
            if current_inside:
                if not previous_inside:
                    output.append(line_intersection(previous, current, start, end))
                output.append(current)
            elif previous_inside:
                output.append(line_intersection(previous, current, start, end))
            previous = current
    return output


def bbox_2d(points: Sequence[Vec2]) -> Tuple[float, float, float, float]:
    return (min(point[0] for point in points), min(point[1] for point in points), max(point[0] for point in points), max(point[1] for point in points))


def bbox_overlap(a: Tuple[float, float, float, float], b: Tuple[float, float, float, float]) -> bool:
    return a[0] < b[2] - 1e-12 and b[0] < a[2] - 1e-12 and a[1] < b[3] - 1e-12 and b[1] < a[3] - 1e-12


def classify_chart(mesh: Any, polygon: Any, component_bounds: Dict[str, List[float]]) -> str:
    normal_z = float(polygon.normal.z)
    if normal_z >= 0.95:
        return "top"
    if normal_z <= -0.95:
        return "bottom"
    return "side"


def lightmap_audit(obj: Any, ranges: Sequence[Dict[str, Any]]) -> Dict[str, Any]:
    mesh = obj.data
    layer = mesh.uv_layers.get("LightmapUV")
    if layer is None:
        return {"pass": False, "reason": "LightmapUV missing"}
    polygons: List[Tuple[int, str, List[Vec2], Tuple[float, float, float, float]]] = []
    chart_counts: Dict[str, int] = {}
    chart_containment_failures: List[int] = []
    bounds_failures = 0
    degenerate_uv_faces = 0

    for component_index, record in enumerate(ranges):
        coords = [mesh.vertices[index].co for index in range(record["vertex_start"], record["vertex_end_exclusive"])]
        component_bounds = {
            "min": [min(float(vertex[axis]) for vertex in coords) for axis in range(3)],
            "max": [max(float(vertex[axis]) for vertex in coords) for axis in range(3)],
        }
        row_min = component_index * 0.25
        row_max = row_min + 0.25
        boxes = {
            "side": (LIGHTMAP_CHART_INSET, row_min + LIGHTMAP_CHART_INSET, 0.5 - LIGHTMAP_CHART_INSET, row_max - LIGHTMAP_CHART_INSET),
            "top": (0.5 + LIGHTMAP_CHART_INSET, row_min + LIGHTMAP_CHART_INSET, 0.75 - LIGHTMAP_CHART_INSET, row_max - LIGHTMAP_CHART_INSET),
            "bottom": (0.75 + LIGHTMAP_CHART_INSET, row_min + LIGHTMAP_CHART_INSET, 1.0 - LIGHTMAP_CHART_INSET, row_max - LIGHTMAP_CHART_INSET),
        }
        for polygon_index in range(record["face_start"], record["face_end_exclusive"]):
            polygon = mesh.polygons[polygon_index]
            points = [(float(layer.data[loop_index].uv.x), float(layer.data[loop_index].uv.y)) for loop_index in polygon.loop_indices]
            chart = classify_chart(mesh, polygon, component_bounds)
            chart_id = f"{record['component_id']}:{chart}"
            chart_counts[chart_id] = chart_counts.get(chart_id, 0) + 1
            expected = boxes[chart]
            if any(point[0] < -EPS or point[0] > 1.0 + EPS or point[1] < -EPS or point[1] > 1.0 + EPS for point in points):
                bounds_failures += 1
            if any(point[0] < expected[0] - EPS or point[0] > expected[2] + EPS or point[1] < expected[1] - EPS or point[1] > expected[3] + EPS for point in points):
                chart_containment_failures.append(polygon_index)
            if polygon_area_2d(points) <= 1e-12:
                degenerate_uv_faces += 1
            polygons.append((polygon_index, chart_id, points, bbox_2d(points)))

    overlap_pairs: List[List[int]] = []
    for first_index, (polygon_a, chart_a, points_a, bbox_a) in enumerate(polygons):
        for polygon_b, chart_b, points_b, bbox_b in polygons[first_index + 1 :]:
            if chart_a != chart_b or not bbox_overlap(bbox_a, bbox_b):
                continue
            intersection = convex_intersection(points_a, points_b)
            if len(intersection) >= 3 and polygon_area_2d(intersection) > 1e-10:
                overlap_pairs.append([polygon_a, polygon_b])
                if len(overlap_pairs) >= 20:
                    break
        if len(overlap_pairs) >= 20:
            break
    minimum_chart_gap_texels = 2.0 * LIGHTMAP_CHART_INSET * LIGHTMAP_RESOLUTION
    passed = (
        len(mesh.uv_layers) == 2
        and [uv.name for uv in mesh.uv_layers] == ["UVMap", "LightmapUV"]
        and len(chart_counts) == 12
        and bounds_failures == 0
        and not chart_containment_failures
        and degenerate_uv_faces == 0
        and not overlap_pairs
        and minimum_chart_gap_texels >= LIGHTMAP_PADDING_TEXELS
    )
    return {
        "pass": passed,
        "uv_layers": [uv.name for uv in mesh.uv_layers],
        "charts": len(chart_counts),
        "chart_face_counts": chart_counts,
        "minimum_chart_gap_texels": minimum_chart_gap_texels,
        "required_padding_texels": LIGHTMAP_PADDING_TEXELS,
        "bounds_failures": bounds_failures,
        "chart_containment_failures": chart_containment_failures[:20],
        "degenerate_uv_faces": degenerate_uv_faces,
        "positive_area_overlap_pairs": overlap_pairs,
        "sha256": uv_layer_hash(mesh, "LightmapUV"),
    }


def load_candidate_objects(bpy: Any) -> List[Any]:
    with bpy.data.libraries.load(str(REPO_ROOT / SOURCE_BLEND_REL), link=False) as (source, target):
        if any(name not in source.objects for name in SOURCE_NAMES):
            raise RuntimeError("approved Step 15 candidate library is missing source objects")
        target.objects = list(SOURCE_NAMES)
    return [obj for obj in target.objects if obj is not None]


def compare_lod0_to_candidate(bpy: Any, lod0: Any, ranges: Sequence[Dict[str, Any]], expected_geometry: Dict[str, Any]) -> Dict[str, Any]:
    expected_by_name = {record["object_name"]: record for record in expected_geometry["objects"]}
    loaded = load_candidate_objects(bpy)
    loaded_by_requested = dict(zip(SOURCE_NAMES, loaded))
    geometry_failures: List[str] = []
    uv_failures: List[str] = []
    for record in ranges:
        name = record["source_object"]
        expected = expected_by_name[name]
        vertex_start = record["vertex_start"]
        actual_vertices = [[round(float(value), 9) for value in lod0.data.vertices[index].co] for index in range(vertex_start, record["vertex_end_exclusive"])]
        if actual_vertices != expected["vertices"]:
            geometry_failures.append(f"{name}:vertices")
        actual_faces = [[int(index) - vertex_start for index in lod0.data.polygons[face_index].vertices] for face_index in range(record["face_start"], record["face_end_exclusive"])]
        if actual_faces != expected["faces"]:
            geometry_failures.append(f"{name}:faces")

        source_obj = loaded_by_requested[name]
        source_uv = source_obj.data.uv_layers.get("UVMap")
        lod_uv = lod0.data.uv_layers.get("UVMap")
        if source_uv is None or lod_uv is None:
            uv_failures.append(f"{name}:missing")
        else:
            source_polygons = list(source_obj.data.polygons)
            for local_face, face_index in enumerate(range(record["face_start"], record["face_end_exclusive"])):
                source_values = [(round(float(source_uv.data[index].uv.x), 9), round(float(source_uv.data[index].uv.y), 9)) for index in source_polygons[local_face].loop_indices]
                actual_values = [(round(float(lod_uv.data[index].uv.x), 9), round(float(lod_uv.data[index].uv.y), 9)) for index in lod0.data.polygons[face_index].loop_indices]
                if source_values != actual_values:
                    uv_failures.append(f"{name}:face:{local_face}")
                    break
    for obj in loaded:
        mesh = obj.data
        bpy.data.objects.remove(obj, do_unlink=True)
        if mesh.users == 0:
            bpy.data.meshes.remove(mesh)
    return {
        "geometry_match": not geometry_failures,
        "uv0_match": not uv_failures,
        "geometry_failures": geometry_failures,
        "uv_failures": uv_failures,
        "expected_geometry_sha256": APPROVED_GEOMETRY_HASH,
    }


def topology_audit(obj: Any) -> Dict[str, Any]:
    counts = edge_counts(obj.data)
    volume, degenerates = mesh_volume_and_degenerates(obj)
    return {
        "vertices": len(obj.data.vertices),
        "faces": len(obj.data.polygons),
        "triangles": mesh_triangles(obj.data),
        "boundary_edges": sum(1 for count in counts.values() if count == 1),
        "nonmanifold_edges": sum(1 for count in counts.values() if count != 2),
        "connected_components": connected_component_count(obj.data),
        "signed_volume_cm3": volume,
        "degenerate_triangles": degenerates,
        "bounds": bounds_from_vertices(object_world_vertices(obj)),
    }


def material_audit(bpy: Any, lod_objects: Dict[str, Any]) -> Dict[str, Any]:
    material = bpy.data.materials.get(MATERIAL_NAME)
    if material is None or not material.use_nodes:
        return {"pass": False, "reason": "material missing"}
    nodes = material.node_tree.nodes
    image_names = sorted(node.image.name for node in nodes if node.type == "TEX_IMAGE" and node.image is not None)
    slot_counts = {name: len(obj.data.materials) for name, obj in lod_objects.items()}
    slot_names = {name: [slot.name for slot in obj.data.materials] for name, obj in lod_objects.items()}
    passed = (
        all(value == 1 for value in slot_counts.values())
        and all(value == [MATERIAL_NAME] for value in slot_names.values())
        and material.blend_method == "OPAQUE"
        and material.use_backface_culling
        and not material.get("aerathea_emissive_enabled", True)
        and set(image_names) == {BC_REL.name, NORMAL_REL.name, ORM_REL.name}
    )
    return {
        "pass": passed,
        "slot_counts": slot_counts,
        "slot_names": slot_names,
        "blend_mode": material.blend_method,
        "two_sided": not material.use_backface_culling,
        "emissive": material.get("aerathea_emissive_enabled", True),
        "image_nodes": image_names,
    }


def collision_audit(collisions: Sequence[Any], manifest: Dict[str, Any], expected_geometry: Dict[str, Any]) -> Dict[str, Any]:
    expected_names = [f"UCX_{ASSET}_{index:02d}" for index in range(4)]
    by_name = {obj.name: obj for obj in collisions}
    failures: List[str] = []
    records: List[Dict[str, Any]] = []
    source_by_name = {record["object_name"]: record for record in expected_geometry["objects"]}
    manifest_by_name = {record["name"]: record for record in manifest["collision"]["hulls"]}
    if sorted(by_name) != expected_names:
        failures.append("name_set")
    for name in expected_names:
        obj = by_name.get(name)
        if obj is None:
            continue
        topology = topology_audit(obj)
        if topology["connected_components"] != 1 or topology["nonmanifold_edges"] != 0 or topology["degenerate_triangles"] != 0 or topology["signed_volume_cm3"] <= 0:
            failures.append(f"{name}:topology_or_volume")
        if len(obj.data.vertices) != 8 or len(obj.data.polygons) != 6 or len(obj.data.materials) != 0:
            failures.append(f"{name}:simple_shape")
        record = manifest_by_name[name]
        source = source_by_name[record["owner"]]
        containment_failures = 0
        params = record["parameters"]
        for vertex in source["vertices"]:
            x, y, z = [float(value) for value in vertex]
            if "min" in params:
                inside = all(params["min"][axis] - EPS <= (x, y, z)[axis] <= params["max"][axis] + EPS for axis in range(3))
            else:
                zmin, zmax = params["z"]
                t = (z - zmin) / (zmax - zmin) if zmax != zmin else 1.0
                half_x = params["bottom_half_extents"][0] * (1.0 - t) + params["top_half_extents"][0] * t
                half_y = params["bottom_half_extents"][1] * (1.0 - t) + params["top_half_extents"][1] * t
                inside = zmin - EPS <= z <= zmax + EPS and abs(x) <= half_x + EPS and abs(y) <= half_y + EPS
            if not inside:
                containment_failures += 1
        if containment_failures:
            failures.append(f"{name}:containment")
        records.append({"name": name, "topology": topology, "source_vertices_outside": containment_failures, "artifact_classification": "collision interpretation"})
    return {"pass": not failures, "expected_names": expected_names, "failures": failures, "records": records}


def imported_fbx_audit(bpy: Any, manifest: Dict[str, Any]) -> Dict[str, Any]:
    original_scene = bpy.context.window.scene
    package_records: Dict[str, Any] = {}
    overall = True
    for lod_name, rel in FBX_RELS.items():
        scene = bpy.data.scenes.new(f"STEP16_IMPORT_{lod_name}")
        bpy.context.window.scene = scene
        bpy.ops.import_scene.fbx(filepath=str(REPO_ROOT / rel), use_custom_normals=True)
        meshes = [obj for obj in scene.objects if obj.type == "MESH"]
        collisions = [obj for obj in meshes if obj.name.startswith("UCX_")]
        renders = [obj for obj in meshes if not obj.name.startswith("UCX_")]
        expected = manifest["lods"][lod_name]
        render = renders[0] if len(renders) == 1 else None
        record: Dict[str, Any] = {
            "path": str(rel),
            "sha256": sha256_file(REPO_ROOT / rel),
            "mesh_names": sorted(obj.name for obj in meshes),
            "render_mesh_count": len(renders),
            "collision_mesh_count": len(collisions),
        }
        if render is not None:
            raw_bounds = bounds_from_vertices(object_world_vertices(render))
            imported_vertices_cm = [tuple(value * 100.0 for value in vertex) for vertex in object_world_vertices(render)]
            actual_bounds = bounds_from_vertices(imported_vertices_cm)
            record.update(
                {
                    "triangles": mesh_triangles(render.data),
                    "vertices": len(render.data.vertices),
                    "raw_blender_meter_bounds": raw_bounds,
                    "bounds_cm": actual_bounds,
                    "uv_layers": [layer.name for layer in render.data.uv_layers],
                    "material_slots": [slot.name.split(".")[0] for slot in render.data.materials],
                }
            )
            record["pass"] = (
                record["triangles"] == expected["triangles"]
                and bounds_match(actual_bounds, expected["bounds"], 1e-4)
                and set(record["uv_layers"]) == {"UVMap", "LightmapUV"}
                and len(render.data.materials) == 1
                and (len(collisions) == 4 if lod_name == "LOD0" else len(collisions) == 0)
            )
        else:
            record["pass"] = False
        overall = overall and record["pass"] and record["sha256"] == manifest["fbx_package"][lod_name]["sha256"]
        package_records[lod_name] = record
        bpy.context.window.scene = original_scene
        imported_objects = list(scene.objects)
        bpy.data.scenes.remove(scene)
        for obj in imported_objects:
            mesh = obj.data if obj.type == "MESH" else None
            if obj.users == 0:
                bpy.data.objects.remove(obj)
            if mesh is not None and mesh.users == 0:
                bpy.data.meshes.remove(mesh)
    bpy.context.window.scene = original_scene
    report = {
        "schema": "aerathea.step16_imported_fbx_audit.v1",
        "asset_id": ASSET,
        "contract_id": CONTRACT_ID,
        "status": "pass_imported_fbx_geometry_and_triangle_validation" if overall else "blocked_imported_fbx_validation_failure",
        "pass": overall,
        "packages": package_records,
        "unreal_import_performed": False,
        "artifact_classification": "proof only",
    }
    write_json(FBX_AUDIT_REL, report)
    return report


def technical_audit(final: bool) -> Dict[str, Any]:
    lock, lock_results = verify_lock()
    manifest = load_json(MANIFEST_REL)
    expected_step15 = load_json(STEP15_MANIFEST_REL)
    import bpy  # type: ignore

    if Path(bpy.data.filepath).resolve() != (REPO_ROOT / DCC_BLEND_REL).resolve():
        raise RuntimeError("audit modes must open the Step 16 DCC source as the startup file")
    blend_hash_before = sha256_file(REPO_ROOT / DCC_BLEND_REL)
    source_hash_before = sha256_file(REPO_ROOT / SOURCE_BLEND_REL)
    mesh_objects = {obj.name: obj for obj in bpy.context.scene.objects if obj.type == "MESH"}
    lod_objects = {lod: mesh_objects.get(f"{ASSET}_{lod}") for lod in ("LOD0", "LOD1", "LOD2", "LOD3")}
    collisions = [obj for obj in mesh_objects.values() if obj.name.startswith(f"UCX_{ASSET}_")]
    required_objects_present = all(obj is not None for obj in lod_objects.values()) and len(collisions) == 4 and len(mesh_objects) == 8
    if not required_objects_present:
        lod_objects = {name: obj for name, obj in lod_objects.items() if obj is not None}

    topology = {name: topology_audit(obj) for name, obj in lod_objects.items()}
    ranges = {name: json.loads(obj["aerathea_component_ranges_json"]) for name, obj in lod_objects.items()}
    lod0_compare = compare_lod0_to_candidate(bpy, lod_objects["LOD0"], ranges["LOD0"], expected_step15["geometry"]["signature"])
    lightmaps = {name: lightmap_audit(obj, ranges[name]) for name, obj in lod_objects.items()}
    material = material_audit(bpy, lod_objects)
    collision = collision_audit(collisions, manifest, expected_step15["geometry"]["signature"])
    imported = imported_fbx_audit(bpy, manifest)
    triangles = {name: topology[name]["triangles"] for name in topology}
    strict_monotonic = all(triangles[first] > triangles[second] for first, second in (("LOD0", "LOD1"), ("LOD1", "LOD2"), ("LOD2", "LOD3")))
    budgets = all(triangles[name] <= LOD_BUDGETS[name] for name in triangles)
    topology_pass = all(record["nonmanifold_edges"] == 0 and record["connected_components"] == 4 and record["degenerate_triangles"] == 0 and record["signed_volume_cm3"] > 0 for record in topology.values())
    bounds_pass = all(bounds_match(record["bounds"], EXPECTED_BOUNDS, EPS) for record in topology.values())
    transforms_pass = all(tuple(round(float(value), 7) for value in obj.location) == (0.0, 0.0, 0.0) and tuple(round(float(value), 7) for value in obj.rotation_euler) == (0.0, 0.0, 0.0) and tuple(round(float(value), 7) for value in obj.scale) == (1.0, 1.0, 1.0) for obj in lod_objects.values())
    texture_hashes = {
        "base_color": sha256_file(REPO_ROOT / BC_REL),
        "normal": sha256_file(REPO_ROOT / NORMAL_REL),
        "orm": sha256_file(REPO_ROOT / ORM_REL),
    }
    texture_pass = texture_hashes == {
        "base_color": lock["locked_inputs"][-3]["sha256"],
        "normal": lock["locked_inputs"][-2]["sha256"],
        "orm": lock["locked_inputs"][-1]["sha256"],
    }
    export_hashes = {name: sha256_file(REPO_ROOT / rel) if (REPO_ROOT / rel).is_file() else None for name, rel in FBX_RELS.items()}
    export_pass = all(export_hashes[name] == manifest["fbx_package"][name]["sha256"] for name in FBX_RELS)
    dcc_manifest_pass = (
        manifest["contract_id"] == CONTRACT_ID
        and manifest["immutable_source"]["sha256_before"] == APPROVED_SOURCE_HASH
        and manifest["immutable_source"]["sha256_after"] == APPROVED_SOURCE_HASH
        and manifest["immutable_source"]["geometry_sha256"] == APPROVED_GEOMETRY_HASH
        and manifest["dcc_source"]["sha256"] == blend_hash_before
    )
    classification_pass = (
        manifest["artifact_classification"] == "candidate"
        and manifest["forbidden_outputs"] == {
            "source_visual_redesign": 0,
            "material_redesign": 0,
            "texture_changes": 0,
            "unreal": 0,
            "step17_approval": 0,
            "fully_game_ready": 0,
            "visual_canon": 0,
        }
        and not bool(bpy.context.scene.get("aerathea_unreal_work_performed"))
        and not bool(bpy.context.scene.get("aerathea_step17_approved"))
        and not bool(bpy.context.scene.get("aerathea_fully_game_ready"))
    )
    proof = load_json(PROOF_AUDIT_REL) if final and (REPO_ROOT / PROOF_AUDIT_REL).is_file() else None

    gates = [
        gate("S16-G01-INPUTS", all(item["match"] for item in lock_results), {"locked": len(lock_results), "failed": [item["path"] for item in lock_results if not item["match"]]}),
        gate("S16-G02-SOURCE", source_hash_before == APPROVED_SOURCE_HASH, {"source_sha256": source_hash_before, "expected": APPROVED_SOURCE_HASH}),
        gate("S16-G03-DCC-MANIFEST", dcc_manifest_pass, {"blend_sha256": blend_hash_before, "manifest_sha256": manifest["dcc_source"]["sha256"]}),
        gate("S16-G04-OBJECT-SET", required_objects_present, {"mesh_objects": sorted(mesh_objects), "lod_objects": sorted(lod_objects), "collision_count": len(collisions)}),
        gate("S16-G05-LOD0-GEOMETRY", lod0_compare["geometry_match"] and triangles.get("LOD0") == 784, lod0_compare),
        gate("S16-G06-LOD0-UV0", lod0_compare["uv0_match"], {"match": lod0_compare["uv0_match"], "failures": lod0_compare["uv_failures"]}),
        gate("S16-G07-TEXTURES", texture_pass, texture_hashes),
        gate("S16-G08-MATERIAL", material["pass"], material),
        gate("S16-G09-LIGHTMAP-UV", all(result["pass"] for result in lightmaps.values()), lightmaps),
        gate("S16-G10-LOD-BUDGETS", strict_monotonic and budgets, {"triangles": triangles, "budgets": LOD_BUDGETS, "strict_monotonic": strict_monotonic}),
        gate("S16-G11-LOD-TOPOLOGY", topology_pass, topology),
        gate("S16-G12-BOUNDS-PIVOT-SCALE", bounds_pass and transforms_pass and abs(float(bpy.context.scene.unit_settings.scale_length) - 0.01) <= 1e-8, {"expected_bounds": EXPECTED_BOUNDS, "bounds_pass": bounds_pass, "transforms_pass": transforms_pass, "scale_length": bpy.context.scene.unit_settings.scale_length}),
        gate("S16-G13-COLLISION", collision["pass"], collision),
        gate("S16-G14-FBX-PACKAGE", export_pass, {"hashes": export_hashes, "files": len(export_hashes)}),
        gate("S16-G15-FBX-IMPORT", imported["pass"], imported),
        gate("S16-G16-CLASSIFICATION-FIREWALL", classification_pass, {"manifest_forbidden_outputs": manifest["forbidden_outputs"], "scene_unreal": bpy.context.scene.get("aerathea_unreal_work_performed"), "scene_step17": bpy.context.scene.get("aerathea_step17_approved")}),
        gate("S16-G17-PROOFS", None if not final else bool(proof and proof.get("status") == "pass_step16_dcc_proof_package" and proof.get("counts") == {"lod_renders": 4, "collision_renders": 1, "imported_fbx_renders": 1, "review_boards": 1} and all(item["not_clipped"] for item in proof.get("renders", []))), proof if proof else "pending until technical pass"),
    ]
    blend_hash_after = sha256_file(REPO_ROOT / DCC_BLEND_REL)
    source_hash_after = sha256_file(REPO_ROOT / SOURCE_BLEND_REL)
    mutation_pass = blend_hash_after == blend_hash_before and source_hash_after == source_hash_before
    if not mutation_pass:
        gates[2] = gate("S16-G03-DCC-MANIFEST", False, {"reason": "audit mutated DCC or source blend", "dcc_before": blend_hash_before, "dcc_after": blend_hash_after, "source_before": source_hash_before, "source_after": source_hash_after})
    failures = [entry["id"] for entry in gates if entry["status"] == "fail"]
    pending = [entry["id"] for entry in gates if entry["status"] == "pending"]
    if final:
        status = "pass_step16_dcc_game_ready_candidate_complete" if not failures and not pending else "blocked_step16_technical_gate_failure"
    else:
        status = "pass_step16_preproof_16_gates_render_authorized" if not failures and pending == ["S16-G17-PROOFS"] else "blocked_step16_technical_gate_failure"
    report = {
        "schema": "aerathea.step16_dcc_game_ready_validation.v1",
        "asset_id": ASSET,
        "contract_id": CONTRACT_ID,
        "date": "2026-07-20",
        "status": status,
        "artifact_classification": "proof only" if not final else "authoritative Step 16 technical result",
        "pipeline_status": "DCC game-ready candidate" if status == "pass_step16_dcc_game_ready_candidate_complete" else "DCC source candidate during Step 16 validation",
        "candidate_sha256": blend_hash_after,
        "source_sha256": source_hash_after,
        "manifest_path": str(MANIFEST_REL),
        "manifest_sha256": sha256_file(REPO_ROOT / MANIFEST_REL),
        "gates_total": len(gates),
        "gates_passed": sum(entry["status"] == "pass" for entry in gates),
        "gates_pending": len(pending),
        "gates_failed": len(failures),
        "failures": failures,
        "pending": pending,
        "gates": gates,
        "lod_triangles": triangles,
        "fbx_import_audit": str(FBX_AUDIT_REL),
        "proof_audit": str(PROOF_AUDIT_REL) if final else None,
        "classification": {
            "artifact_status": "candidate",
            "pipeline_status": "DCC game-ready candidate" if final and not failures else "DCC source candidate",
            "fully_game_ready": False,
            "approved_library_asset": False,
            "visual_canon": False,
            "step17_approved": False,
        },
        "forbidden_outputs": {"unreal": 0, "step17_approval": 0, "fully_game_ready": 0, "visual_canon": 0},
    }
    write_json(VALIDATION_REL if final else PREPROOF_REL, report)
    return report


def look_at(camera: Any, target: Vec3) -> None:
    from mathutils import Vector  # type: ignore

    direction = Vector(target) - camera.location
    camera.rotation_euler = direction.to_track_quat("-Z", "Y").to_euler()


def create_neutral_material(bpy: Any, name: str, color: Tuple[float, float, float, float], metallic: float = 0.0, roughness: float = 0.7) -> Any:
    material = bpy.data.materials.get(name) or bpy.data.materials.new(name)
    material.use_nodes = True
    node = material.node_tree.nodes.get("Principled BSDF")
    node.inputs["Base Color"].default_value = color
    node.inputs["Metallic"].default_value = metallic
    node.inputs["Roughness"].default_value = roughness
    return material


def configure_render_scene(bpy: Any, scene: Any) -> Tuple[Any, Any]:
    for obj in list(scene.objects):
        if obj.type in {"CAMERA", "LIGHT"}:
            bpy.data.objects.remove(obj, do_unlink=True)
    scene.render.engine = "BLENDER_EEVEE"
    scene.eevee.use_gtao = True
    scene.eevee.gtao_distance = 20.0
    scene.eevee.gtao_factor = 1.1
    scene.render.resolution_x = 720
    scene.render.resolution_y = 720
    scene.render.resolution_percentage = 100
    scene.render.image_settings.file_format = "PNG"
    scene.render.film_transparent = False
    if scene.world is None:
        scene.world = bpy.data.worlds.new(f"{scene.name}_STEP16_PROOF_WORLD")
    scene.world.color = (0.045, 0.055, 0.07)
    scene.view_settings.view_transform = "Standard"
    scene.view_settings.look = "None"
    scene.view_settings.exposure = 0.0
    scene.view_settings.gamma = 1.0

    camera_data = bpy.data.cameras.new("STEP16_PROOF_CAMERA")
    camera = bpy.data.objects.new("STEP16_PROOF_CAMERA", camera_data)
    scene.collection.objects.link(camera)
    camera.location = (315.0, -405.0, 275.0)
    camera_data.type = "ORTHO"
    camera_data.ortho_scale = 285.0
    look_at(camera, (0.0, 0.0, 108.0))
    scene.camera = camera

    key_data = bpy.data.lights.new("STEP16_KEY", type="AREA")
    key_data.energy = 850.0
    key_data.size = 230.0
    key = bpy.data.objects.new("STEP16_KEY", key_data)
    key.location = (-190.0, -230.0, 330.0)
    look_at(key, (0.0, 0.0, 90.0))
    scene.collection.objects.link(key)
    fill_data = bpy.data.lights.new("STEP16_FILL", type="AREA")
    fill_data.energy = 500.0
    fill_data.size = 180.0
    fill = bpy.data.objects.new("STEP16_FILL", fill_data)
    fill.location = (220.0, 80.0, 220.0)
    look_at(fill, (0.0, 0.0, 90.0))
    scene.collection.objects.link(fill)
    return camera, key


def framing_record(scene: Any, camera: Any, objects: Sequence[Any]) -> Dict[str, Any]:
    from bpy_extras.object_utils import world_to_camera_view  # type: ignore

    coordinates = []
    for obj in objects:
        for vertex in obj.data.vertices:
            projected = world_to_camera_view(scene, camera, obj.matrix_world @ vertex.co)
            coordinates.append((float(projected.x), float(projected.y), float(projected.z)))
    margins = {
        "left": min(item[0] for item in coordinates),
        "right": 1.0 - max(item[0] for item in coordinates),
        "bottom": min(item[1] for item in coordinates),
        "top": 1.0 - max(item[1] for item in coordinates),
    }
    return {"normalized_margins": margins, "all_in_front": all(item[2] > 0 for item in coordinates), "not_clipped": min(margins.values()) >= 0.025 and all(item[2] > 0 for item in coordinates)}


def render_current_scene(bpy: Any, label: str, rel: Path, visible: Sequence[Any]) -> Dict[str, Any]:
    scene = bpy.context.scene
    camera = scene.camera
    bpy.context.view_layer.update()
    frame = framing_record(scene, camera, visible)
    output = REPO_ROOT / rel
    output.parent.mkdir(parents=True, exist_ok=True)
    scene.render.filepath = str(output)
    bpy.ops.render.render(write_still=True)
    return {"label": label, "path": str(rel), "sha256": sha256_file(output), "not_clipped": frame["not_clipped"], "framing": frame}


def render_proofs() -> Dict[str, Any]:
    preflight = technical_audit(final=False)
    if preflight["status"] != "pass_step16_preproof_16_gates_render_authorized":
        raise RuntimeError(f"technical preproof audit did not authorize renders: {preflight['failures']}")
    import bpy  # type: ignore

    blend_hash_before = sha256_file(REPO_ROOT / DCC_BLEND_REL)
    scene = bpy.context.scene
    camera, _key = configure_render_scene(bpy, scene)
    mesh_objects = [obj for obj in scene.objects if obj.type == "MESH"]
    lod_objects = {lod: next(obj for obj in mesh_objects if obj.name == f"{ASSET}_{lod}") for lod in ("LOD0", "LOD1", "LOD2", "LOD3")}
    collisions = [obj for obj in mesh_objects if obj.name.startswith("UCX_")]
    render_records: List[Dict[str, Any]] = []

    for lod_name, obj in lod_objects.items():
        for mesh in mesh_objects:
            mesh.hide_render = mesh is not obj
        render_records.append(render_current_scene(bpy, lod_name, RENDER_RELS[lod_name], [obj]))

    collision_material = create_neutral_material(bpy, "STEP16_COLLISION_PROOF_ORANGE", (0.9, 0.12, 0.025, 1.0), metallic=0.05, roughness=0.35)
    for mesh in mesh_objects:
        mesh.hide_render = mesh not in [lod_objects["LOD0"], *collisions]
    for obj in collisions:
        obj.hide_render = False
        obj.data.materials.clear()
        obj.data.materials.append(collision_material)
        modifier = obj.modifiers.get("STEP16_PROOF_WIREFRAME") or obj.modifiers.new("STEP16_PROOF_WIREFRAME", "WIREFRAME")
        modifier.thickness = 0.55
        modifier.use_replace = True
    render_records.append(render_current_scene(bpy, "COLLISION", RENDER_RELS["COLLISION"], [lod_objects["LOD0"], *collisions]))

    original_scene = scene
    import_scene = bpy.data.scenes.new("STEP16_IMPORTED_FBX_PROOF")
    bpy.context.window.scene = import_scene
    bpy.ops.import_scene.fbx(filepath=str(REPO_ROOT / FBX_RELS["LOD0"]), use_custom_normals=True)
    camera, _key = configure_render_scene(bpy, import_scene)
    imported_meshes = [obj for obj in import_scene.objects if obj.type == "MESH"]
    imported_render = [obj for obj in imported_meshes if not obj.name.startswith("UCX_")]
    imported_collision = [obj for obj in imported_meshes if obj.name.startswith("UCX_")]
    imported_vertices = [vertex for obj in imported_meshes for vertex in object_world_vertices(obj)]
    imported_bounds = bounds_from_vertices(imported_vertices)
    imported_center = tuple((imported_bounds["min"][axis] + imported_bounds["max"][axis]) * 0.5 for axis in range(3))
    imported_span = max(imported_bounds["dimensions"])
    camera.location = (
        imported_center[0] + imported_span * 1.45,
        imported_center[1] - imported_span * 1.85,
        imported_center[2] + imported_span * 1.25,
    )
    camera.data.ortho_scale = imported_span * 1.45
    look_at(camera, imported_center)
    neutral = create_neutral_material(bpy, "STEP16_IMPORTED_FBX_STONE", (0.29, 0.32, 0.34, 1.0), roughness=0.82)
    for obj in imported_render:
        obj.data.materials.clear()
        obj.data.materials.append(neutral)
    for obj in imported_collision:
        obj.data.materials.clear()
        obj.data.materials.append(collision_material)
        modifier = obj.modifiers.new("STEP16_PROOF_WIREFRAME", "WIREFRAME")
        modifier.thickness = 0.55
        modifier.use_replace = True
    render_records.append(render_current_scene(bpy, "IMPORTED_FBX", RENDER_RELS["IMPORTED_FBX"], imported_meshes))
    bpy.context.window.scene = original_scene

    from PIL import Image, ImageDraw, ImageFont  # type: ignore

    def font(size: int, bold: bool = False) -> Any:
        path = Path("/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf" if bold else "/usr/share/fonts/truetype/dejavu/DejaVuSans.ttf")
        return ImageFont.truetype(str(path), size=size) if path.is_file() else ImageFont.load_default()

    width, height = 1800, 1330
    board = Image.new("RGB", (width, height), (18, 22, 28))
    draw = ImageDraw.Draw(board)
    draw.text((40, 28), f"{ASSET} — STEP 16 DCC GAME-READY CANDIDATE", fill=(238, 241, 244), font=font(31, True))
    draw.text((40, 72), "PROOF ONLY — Step 17 approval and Unreal import remain separate", fill=(255, 198, 64), font=font(19, True))
    triangles = preflight["lod_triangles"]
    draw.text((40, 105), f"LOD triangles: {triangles} | Collision: 4 convex UCX hulls | LightmapUV: 128 px / >=4 px", fill=(182, 196, 210), font=font(17))
    thumb_w, thumb_h = 540, 520
    positions = [(35, 150), (630, 150), (1225, 150), (35, 740), (630, 740), (1225, 740)]
    resampling = getattr(Image, "Resampling", Image)
    thumbnail_filter = getattr(resampling, "LANCZOS", Image.BICUBIC)
    for record, position in zip(render_records, positions):
        image = Image.open(REPO_ROOT / record["path"]).convert("RGB")
        image.thumbnail((thumb_w, thumb_h - 45), thumbnail_filter)
        x = position[0] + (thumb_w - image.width) // 2
        y = position[1] + 40 + (thumb_h - 45 - image.height) // 2
        board.paste(image, (x, y))
        draw.rectangle((position[0], position[1], position[0] + thumb_w, position[1] + thumb_h), outline=(72, 84, 98), width=2)
        label = record["label"]
        suffix = f" — {triangles[label]} tris" if label in triangles else " — proof-only overlay"
        draw.text((position[0] + 12, position[1] + 10), label + suffix, fill=(230, 235, 240), font=font(18, True))
    board_path = REPO_ROOT / BOARD_REL
    board_path.parent.mkdir(parents=True, exist_ok=True)
    board.save(board_path)

    blend_hash_after = sha256_file(REPO_ROOT / DCC_BLEND_REL)
    pass_status = blend_hash_after == blend_hash_before and all(record["not_clipped"] for record in render_records) and board_path.is_file()
    report = {
        "schema": "aerathea.step16_dcc_proof_audit.v1",
        "asset_id": ASSET,
        "contract_id": CONTRACT_ID,
        "status": "pass_step16_dcc_proof_package" if pass_status else "blocked_step16_dcc_proof_failure",
        "artifact_classification": "proof only",
        "candidate_sha256_before": blend_hash_before,
        "candidate_sha256_after": blend_hash_after,
        "candidate_unchanged": blend_hash_after == blend_hash_before,
        "counts": {"lod_renders": 4, "collision_renders": 1, "imported_fbx_renders": 1, "review_boards": 1},
        "renders": render_records,
        "board": {"path": str(BOARD_REL), "sha256": sha256_file(board_path), "presentation_thumbnails_only": True},
        "interpretation_notice": "rendered pixels, LOD optimization, LightmapUV, collision, and FBX conversion are interpretation; locked LOD0 and hashes remain evidence",
        "unreal_work_performed": False,
        "step17_approval_performed": False,
    }
    write_json(PROOF_AUDIT_REL, report)
    return report


def main() -> int:
    args = parse_args(blender_script_args())
    if args.schema_only:
        report = schema_report()
    elif args.audit:
        report = technical_audit(final=False)
    elif args.render_proofs:
        report = render_proofs()
    else:
        report = technical_audit(final=True)
    print(json.dumps({key: report.get(key) for key in ("status", "asset_id", "contract_id", "gates_passed", "gates_pending", "gates_failed", "failures") if key in report}, indent=2))
    return 0 if not str(report.get("status", "")).startswith("blocked") else 2


if __name__ == "__main__":
    raise SystemExit(main())
