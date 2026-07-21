#!/usr/bin/env python3
"""Independently audit the A005 A08 individual-stone correction candidate."""

from __future__ import annotations

import argparse
import hashlib
import json
import math
import sys
from pathlib import Path
from typing import Any, Dict, List, Sequence, Set, Tuple


ROOT = Path(__file__).resolve().parents[2]
ASSET = "SM_GIA_BloodAxeCairnstone_A005"
CONTRACT = "A005-CR-VISUAL-CORRECTION-A08"
BLUEPRINT_ROOT = Path("docs/assets/blueprints") / ASSET
PLAN_REL = BLUEPRINT_ROOT / "manifests/VISUAL_CORRECTION_A08_PLAN.json"
MEASUREMENT_REL = BLUEPRINT_ROOT / "manifests/VISUAL_CORRECTION_A08_TOP_STONE_MEASUREMENT.json"
VALIDATION_REL = BLUEPRINT_ROOT / "manifests/VISUAL_CORRECTION_A08_VALIDATION.json"
DCC_ROOT = Path("SourceAssets/Blender/Props/Giants/BloodAxe/Cairns") / ASSET
A08_BLEND_REL = DCC_ROOT / f"{ASSET}_DCCGameReady_VisualCorrection_A08.blend"
A04_BLEND_REL = DCC_ROOT / f"{ASSET}_DCCGameReady_VisualCorrection_A04.blend"
MANIFEST_REL = DCC_ROOT / f"{ASSET}_VISUAL_CORRECTION_A08_MANIFEST.json"
EXPORT_ROOT = Path("SourceAssets/Exports/Props/Giants/BloodAxe/Cairns") / ASSET / "VisualCorrection_A08"
FBX_RELS = {
    "LOD0": EXPORT_ROOT / f"{ASSET}_VisualCorrection_A08.fbx",
    "LOD1": EXPORT_ROOT / f"{ASSET}_VisualCorrection_A08_LOD1.fbx",
    "LOD2": EXPORT_ROOT / f"{ASSET}_VisualCorrection_A08_LOD2.fbx",
    "LOD3": EXPORT_ROOT / f"{ASSET}_VisualCorrection_A08_LOD3.fbx",
}
OUTPUT_ROOT_REL = Path("Saved/Automation/DCC") / ASSET / "Production/VisualCorrection_A08"
FINAL_REL = OUTPUT_ROOT_REL / f"{ASSET}_FINAL_CORRECTED_3D_A08.png"
FINAL_RGBA_REL = OUTPUT_ROOT_REL / f"{ASSET}_FINAL_CORRECTED_3D_A08_OBJECT_RGBA.png"
FINAL_AUDIT_REL = OUTPUT_ROOT_REL / "FINAL_RENDER_AUDIT_A08.json"
MASK_MANIFEST_REL = Path("SourceAssets/Textures/Props/Giants/BloodAxe/Cairns") / ASSET / "Technical" / f"{ASSET}_SOURCE_MASK_MANIFEST_A01.json"
UV_PLAN_REL = BLUEPRINT_ROOT / "manifests/STEP_14_UV_OWNERSHIP_PLAN.json"
SOURCE_BC_REL = Path("SourceAssets/Textures/Props/Giants/BloodAxe/Cairns") / ASSET / "T_GIA_BloodAxeCairnstone_A005_BC.png"
A08_BC_REL = Path("SourceAssets/Textures/Props/Giants/BloodAxe/Cairns") / ASSET / "VisualCorrection_A08/T_GIA_BloodAxeCairnstone_A005_VF_A08_BC.png"


def blender_args() -> List[str]:
    return sys.argv[sys.argv.index("--") + 1 :] if "--" in sys.argv else []


def parse_args(argv: Sequence[str]) -> argparse.Namespace:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--technical-only", action="store_true")
    return parser.parse_args(list(argv))


def sha256_file(path: Path) -> str:
    digest = hashlib.sha256()
    with path.open("rb") as handle:
        for block in iter(lambda: handle.read(1024 * 1024), b""):
            digest.update(block)
    return digest.hexdigest()


def hash_json(value: Any) -> str:
    return hashlib.sha256(json.dumps(value, sort_keys=True, separators=(",", ":")).encode("utf-8")).hexdigest()


def load_json(rel: Path) -> Dict[str, Any]:
    return json.loads((ROOT / rel).read_text(encoding="utf-8"))


def close(first: Sequence[float], second: Sequence[float], tolerance: float = 1.0e-4) -> bool:
    return len(first) == len(second) and all(abs(float(a) - float(b)) <= tolerance for a, b in zip(first, second))


def mesh_triangles(mesh: Any) -> int:
    mesh.calc_loop_triangles()
    return len(mesh.loop_triangles)


def object_bounds(obj: Any) -> Dict[str, List[float]]:
    from mathutils import Vector  # type: ignore

    points = [obj.matrix_world @ Vector(corner) for corner in obj.bound_box]
    minimum = [min(float(point[index]) for point in points) for index in range(3)]
    maximum = [max(float(point[index]) for point in points) for index in range(3)]
    return {"min": minimum, "max": maximum, "dimensions": [maximum[index] - minimum[index] for index in range(3)]}


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


def component_records(obj: Any) -> Tuple[List[Dict[str, Any]], Dict[str, int]]:
    import bmesh  # type: ignore

    records: List[Dict[str, Any]] = []
    for indices in component_indices(obj.data):
        coords = [obj.data.vertices[index].co for index in indices]
        minimum = [min(float(point[axis]) for point in coords) for axis in range(3)]
        maximum = [max(float(point[axis]) for point in coords) for axis in range(3)]
        center = [sum(float(point[axis]) for point in coords) / len(coords) for axis in range(3)]
        records.append(
            {
                "indices": indices,
                "vertices": len(indices),
                "min": minimum,
                "max": maximum,
                "dimensions": [maximum[axis] - minimum[axis] for axis in range(3)],
                "center": center,
                "center_radius_xy": math.hypot(center[0], center[1]),
            }
        )
    bm = bmesh.new()
    bm.from_mesh(obj.data)
    topology = {
        "components": len(records),
        "boundary_edges": sum(1 for edge in bm.edges if len(edge.link_faces) == 1),
        "nonmanifold_edges": sum(1 for edge in bm.edges if len(edge.link_faces) not in (1, 2)),
        "degenerate_faces": sum(1 for face in bm.faces if face.calc_area() <= 1.0e-8),
    }
    bm.free()
    return records, topology


def aggregate_bounds(obj: Any, records: Sequence[Dict[str, Any]]) -> Dict[str, List[float]]:
    indices = {index for record in records for index in record["indices"]}
    points = [obj.data.vertices[index].co for index in indices]
    minimum = [min(float(point[axis]) for point in points) for axis in range(3)]
    maximum = [max(float(point[axis]) for point in points) for axis in range(3)]
    return {"min": minimum, "max": maximum, "dimensions": [maximum[axis] - minimum[axis] for axis in range(3)]}


def canonical_cycle(values: Sequence[Any]) -> Tuple[Any, ...]:
    sequence = tuple(values)
    variants = []
    for candidate in (sequence, tuple(reversed(sequence))):
        variants.extend(candidate[index:] + candidate[:index] for index in range(len(candidate)))
    return min(variants)


def component_signature(obj: Any, indices: Set[int]) -> Dict[str, Any]:
    mesh = obj.data
    uv_layer = mesh.uv_layers.get("UVMap")
    if uv_layer is None:
        raise RuntimeError(f"{obj.name} has no UVMap")

    def coord(index: int) -> Tuple[float, float, float]:
        point = mesh.vertices[index].co
        return tuple(round(float(point[axis]), 6) for axis in range(3))  # type: ignore[return-value]

    vertices = sorted(coord(index) for index in indices)
    geometry_faces = []
    uv_faces = []
    for polygon in mesh.polygons:
        if not all(int(index) in indices for index in polygon.vertices):
            continue
        geometry_faces.append(canonical_cycle([coord(int(index)) for index in polygon.vertices]))
        uv_record = []
        for loop_index in polygon.loop_indices:
            vertex_index = int(mesh.loops[loop_index].vertex_index)
            uv = uv_layer.data[loop_index].uv
            uv_record.append((coord(vertex_index), round(float(uv.x), 7), round(float(uv.y), 7)))
        uv_faces.append(canonical_cycle(uv_record))
    return {
        "vertex_count": len(vertices),
        "face_count": len(geometry_faces),
        "geometry_sha256": hash_json({"vertices": vertices, "faces": sorted(geometry_faces)}),
        "uv_sha256": hash_json(sorted(uv_faces)),
    }


def load_object_from_blend(bpy: Any, rel: Path, object_name: str) -> Any:
    with bpy.data.libraries.load(str(ROOT / rel), link=False) as (data_from, data_to):
        if object_name not in data_from.objects:
            raise RuntimeError(f"{object_name} missing from {rel}")
        data_to.objects = [object_name]
    result = data_to.objects[0]
    if result is None:
        raise RuntimeError(f"failed to load {object_name} from {rel}")
    return result


def source_owned_rgb_audit() -> Dict[str, Any]:
    from PIL import Image

    mask_manifest = load_json(MASK_MANIFEST_REL)
    uv_plan = load_json(UV_PLAN_REL)
    windows = {entry["view"]: entry["rect"] for entry in uv_plan["uv0"]["source_windows_half_open_px"]}
    source = Image.open(ROOT / SOURCE_BC_REL).convert("RGB")
    candidate = Image.open(ROOT / A08_BC_REL).convert("RGB")
    compared = 0
    mismatches = 0
    by_view: Dict[str, Any] = {}
    for record in mask_manifest["records"]:
        mask = Image.open(ROOT / record["mask_path"]).convert("L")
        rect = windows[record["view"]]
        source_panel = source.crop(tuple(rect))
        candidate_panel = candidate.crop(tuple(rect))
        view_compared = 0
        view_mismatches = 0
        for source_pixel, candidate_pixel, owned in zip(source_panel.getdata(), candidate_panel.getdata(), mask.getdata()):
            if owned <= 0:
                continue
            view_compared += 1
            if source_pixel != candidate_pixel:
                view_mismatches += 1
        compared += view_compared
        mismatches += view_mismatches
        by_view[record["view"]] = {"pixels_compared": view_compared, "mismatches": view_mismatches}
    return {"pixels_compared": compared, "mismatches": mismatches, "by_view": by_view}


def clean_fbx_reimport(bpy: Any, manifest: Dict[str, Any]) -> Dict[str, Any]:
    result: Dict[str, Any] = {}
    for lod_name, rel in FBX_RELS.items():
        bpy.ops.wm.read_factory_settings(use_empty=True)
        bpy.ops.import_scene.fbx(filepath=str(ROOT / rel), use_custom_normals=True)
        meshes = [obj for obj in bpy.context.scene.objects if obj.type == "MESH"]
        primary = [obj for obj in meshes if not obj.name.startswith("UCX_")]
        triangles = sum(mesh_triangles(obj.data) for obj in primary)
        expected = int(manifest["lods"][lod_name]["triangles"])
        result[lod_name] = {
            "mesh_objects": len(meshes),
            "primary_objects": len(primary),
            "primary_triangles": triangles,
            "expected_triangles": expected,
            "pass": len(primary) == 1 and triangles == expected,
        }
    return result


def main() -> int:
    args = parse_args(blender_args())
    import bpy  # type: ignore
    from PIL import Image

    plan = load_json(PLAN_REL)
    measurement = load_json(MEASUREMENT_REL)
    manifest = load_json(MANIFEST_REL)
    candidate_lods = {
        lod_name: load_object_from_blend(bpy, A08_BLEND_REL, f"{ASSET}_{lod_name}")
        for lod_name in ("LOD0", "LOD1", "LOD2", "LOD3")
    }
    lod0 = candidate_lods["LOD0"]
    records, topology = component_records(lod0)
    plinth = max(records, key=lambda record: record["max"][2])
    mortars = [record for record in records if record is not plinth and record["center_radius_xy"] < 20.0]
    stones = [record for record in records if record is not plinth and record not in mortars]
    c004 = [record for record in stones if record["max"][2] <= 9.001]
    c003 = [record for record in stones if record["min"][2] >= 9.749 and record["max"][2] <= 22.251]
    c002 = [record for record in stones if record["min"][2] >= 22.999 and record["max"][2] <= 34.251]
    course_records = {"C002": c002, "C003": c003, "C004": c004}
    course_bounds = {name: aggregate_bounds(lod0, values) for name, values in course_records.items()}
    mortar_bounds = [aggregate_bounds(lod0, [record]) for record in sorted(mortars, key=lambda record: record["min"][2])]

    a04_lod0 = load_object_from_blend(bpy, A04_BLEND_REL, f"{ASSET}_LOD0")
    a04_records, _ = component_records(a04_lod0)
    a04_plinth = max(a04_records, key=lambda record: record["max"][2])
    plinth_signatures = {
        "A04": component_signature(a04_lod0, a04_plinth["indices"]),
        "A08": component_signature(lod0, plinth["indices"]),
    }

    authority = {}
    for name, record in plan["authority_inputs"].items():
        actual = sha256_file(ROOT / record["path"])
        authority[name] = {"expected": record["sha256"], "actual": actual, "pass": actual == record["sha256"]}
    lods = {
        name: {
            "triangles": mesh_triangles(obj.data),
            "bounds": object_bounds(obj),
            "uv_layers": [layer.name for layer in obj.data.uv_layers],
            "materials": len(obj.data.materials),
        }
        for name, obj in candidate_lods.items()
    }
    material = lod0.data.materials[0] if len(lod0.data.materials) else None
    material_nodes = sorted(node.name for node in material.node_tree.nodes) if material and material.use_nodes else []
    uv_layer = lod0.data.uv_layers.get("UVMap")
    uv_range = {
        "minimum": [min(float(loop.uv[axis]) for loop in uv_layer.data) for axis in range(2)] if uv_layer else [],
        "maximum": [max(float(loop.uv[axis]) for loop in uv_layer.data) for axis in range(2)] if uv_layer else [],
    }
    per_stone_uv = bool(lod0.get("aerathea_A08_per_stone_uv"))
    with bpy.data.libraries.load(str(ROOT / A08_BLEND_REL), link=False) as (data_from, data_to):
        collisions = sorted(name for name in data_from.objects if name.startswith("UCX_"))
    source_rgb = source_owned_rgb_audit()
    export_hashes = {
        name: {"actual": sha256_file(ROOT / rel), "expected": manifest["exports"][name]["sha256"]}
        for name, rel in FBX_RELS.items()
    }
    clean_import = clean_fbx_reimport(bpy, manifest)

    gates: List[Dict[str, Any]] = []

    def gate(gate_id: str, passed: bool, detail: Any) -> None:
        gates.append({"id": gate_id, "status": "pass" if passed else "fail", "detail": detail})

    gate("G01_authority_hashes", all(record["pass"] for record in authority.values()), authority)
    gate(
        "G02_contract_and_classification",
        manifest.get("contract_id") == CONTRACT
        and manifest.get("artifact_classification") == "candidate"
        and manifest.get("replacement_base", {}).get("A07_geometry_inputs") == 0,
        {"contract": manifest.get("contract_id"), "classification": manifest.get("artifact_classification"), "replacement_base": manifest.get("replacement_base")},
    )
    gate("G03_lods_and_budget", [lods[name]["triangles"] for name in ("LOD0", "LOD1", "LOD2", "LOD3")] == [9104, 4186, 1910, 704] and 4000 <= lods["LOD0"]["triangles"] <= 10000, lods)
    gate("G04_bounds_and_pivot", all(close(lods[name]["bounds"]["dimensions"], [140.0, 110.0, 220.0]) and close(lods[name]["bounds"]["min"], [-70.0, -55.0, 0.0]) for name in lods), {name: lods[name]["bounds"] for name in lods})
    gate("G05_79_closed_components", topology == {"components": 79, "boundary_edges": 0, "nonmanifold_edges": 0, "degenerate_faces": 0}, topology)
    counts = {name: len(values) for name, values in course_records.items()}
    gate("G06_individual_stone_counts", counts == {"C002": 19, "C003": 24, "C004": 32} and len(mortars) == 3 and len(stones) == 75, {"courses": counts, "mortars": len(mortars), "stones": len(stones)})
    expected_bounds = {
        "C002": ([123.846154, 92.707424], [23.0, 34.25]),
        "C003": ([137.307692, 105.196507], [9.75, 22.25]),
        "C004": ([140.0, 110.0], [0.0, 9.0]),
    }
    bounds_pass = all(close(course_bounds[name]["dimensions"][:2], expected_bounds[name][0], 0.01) and close([course_bounds[name]["min"][2], course_bounds[name]["max"][2]], expected_bounds[name][1], 0.01) for name in expected_bounds)
    gate("G07_measured_course_bounds", bounds_pass, course_bounds)
    clearances = {
        "C004_to_C003": course_bounds["C003"]["min"][2] - course_bounds["C004"]["max"][2],
        "C003_to_C002": course_bounds["C002"]["min"][2] - course_bounds["C003"]["max"][2],
    }
    gate("G08_positive_course_clearances", all(value >= 0.75 - 1.0e-4 for value in clearances.values()), clearances)
    mortar_pass = len(mortar_bounds) == 3 and all(bounds["dimensions"][0] < 137.4 and bounds["dimensions"][1] < 105.3 for bounds in mortar_bounds)
    gate("G09_recessed_mortar_not_silhouette", mortar_pass, mortar_bounds)
    gate("G10_exact_A04_plinth_geometry_and_uv", plinth_signatures["A04"] == plinth_signatures["A08"], plinth_signatures)
    uv_ok = uv_layer is not None and all(-1.0e-6 <= value <= 1.000001 for value in (*uv_range["minimum"], *uv_range["maximum"]))
    gate("G11_material_and_uv", uv_ok and all(lods[name]["materials"] == 1 and lods[name]["uv_layers"] == ["UVMap", "LightmapUV"] for name in lods) and all(name in material_nodes for name in ("A08_DIRECT_SOURCE_BASECOLOR", "A08_DIRECTX_NORMAL", "A08_ORM_NONMETALLIC")) and per_stone_uv, {"lods": {name: {"materials": lods[name]["materials"], "uv_layers": lods[name]["uv_layers"]} for name in lods}, "material_nodes": material_nodes, "uv_range": uv_range, "per_stone_uv": per_stone_uv})
    gate("G12_collision_set", len(collisions) == 4, collisions)
    gate("G13_fbx_hashes", all(record["actual"] == record["expected"] for record in export_hashes.values()), export_hashes)
    gate("G14_clean_fbx_reimport", all(record["pass"] for record in clean_import.values()), clean_import)
    gate("G15_source_owned_rgb_exact", source_rgb["pixels_compared"] > 0 and source_rgb["mismatches"] == 0 and measurement["status"] == "pass_authoritative_measurement_gate", {"atlas": source_rgb, "measurement_status": measurement["status"]})
    gate("G16_A04_references_preserved", all(record["pass"] for record in manifest["preservation"].values()), manifest["preservation"])
    gate("G17_unreal_firewall", manifest.get("unreal_outputs") == 0 and manifest.get("fully_game_ready") is False and plan.get("unreal_authorized") is False, {"unreal_outputs": manifest.get("unreal_outputs"), "fully_game_ready": manifest.get("fully_game_ready"), "unreal_authorized": plan.get("unreal_authorized")})

    final_record: Dict[str, Any] = {"visual_gate": "not_evaluated_technical_only"}
    if not args.technical_only:
        final_audit = load_json(FINAL_AUDIT_REL)
        proofs = final_audit.get("proofs", {})
        proof_ok = all(
            key in proofs and min(proofs[key]["alpha_bounds"]["margins_px"].values()) >= 60
            for key in ("front_shadeless", "left_shadeless", "right_shadeless", "top_shadeless")
        ) and proofs["top_shadeless"].get("camera", "").startswith("true orthographic")
        gate("G18_fixed_proof_set", proof_ok, proofs)
        alpha = final_audit["alpha_bounds"]["margins_px"]
        render_rgba = Image.open(ROOT / FINAL_RGBA_REL).convert("RGBA")
        object_pixels = [(r, g, b) for r, g, b, value in render_rgba.getdata() if value >= 16]
        bright_fraction = sum(1 for pixel in object_pixels if min(pixel) >= 180 and max(pixel) - min(pixel) <= 20) / max(1, len(object_pixels))
        render_ok = final_audit["size"] == [1400, 1600] and min(alpha.values()) >= 80 and final_audit["review_markers"] == 0 and final_audit["collision_visible"] == 0 and final_audit["lod_visible"] == "LOD0 only" and bright_fraction <= 0.001
        gate("G19_final_review_integrity", render_ok, {"size": final_audit["size"], "margins": alpha, "review_markers": final_audit["review_markers"], "collision_visible": final_audit["collision_visible"], "lod_visible": final_audit["lod_visible"], "bright_fringe_fraction": bright_fraction})
        source_stone = final_audit["displayed_color"]["source_front_owned"]["stone_median_rgb"]
        final_stone = final_audit["displayed_color"]["final"]["stone_median_rgb"]
        stone_distance = math.sqrt(sum((int(first) - int(second)) ** 2 for first, second in zip(source_stone, final_stone)))
        gate("G20_displayed_stone_color", stone_distance <= 12.0, {"source": source_stone, "final": final_stone, "rgb_distance": stone_distance})
        final_record = {"path": str(FINAL_REL), "sha256": sha256_file(ROOT / FINAL_REL), "visual_gate": "pending Flamestrike"}

    passed = sum(1 for record in gates if record["status"] == "pass")
    complete = passed == len(gates)
    status = "pass_technical_candidate_ready_for_final_render" if args.technical_only and complete else "pass_candidate_pending_flamestrike_visual_review" if complete else "blocked_a08_independent_audit"
    validation = {
        "schema": "aerathea.a005_visual_correction_a08_validation.v1",
        "asset_id": ASSET,
        "contract_id": CONTRACT,
        "date": "2026-07-21",
        "status": status,
        "artifact_classification": "proof only",
        "pipeline_status": "DCC game-ready candidate" if complete and not args.technical_only else "candidate pending final proof" if complete else "candidate blocked",
        "fully_game_ready": False,
        "unreal_outputs": 0,
        "candidate": {"manifest": str(MANIFEST_REL), "manifest_sha256": sha256_file(ROOT / MANIFEST_REL)},
        "final_review_image": final_record,
        "gates": gates,
        "gate_summary": {"passed": passed, "total": len(gates)},
    }
    (ROOT / VALIDATION_REL).write_text(json.dumps(validation, indent=2) + "\n", encoding="utf-8")
    print(json.dumps(validation, indent=2))
    return 0 if complete else 1


if __name__ == "__main__":
    raise SystemExit(main())
