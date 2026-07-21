#!/usr/bin/env python3
"""Independently audit the A005 A09 modular-base correction candidate."""

from __future__ import annotations

import hashlib
import json
import math
from pathlib import Path
from typing import Any, Dict, List, Sequence, Set, Tuple


ROOT = Path(__file__).resolve().parents[2]
ASSET = "SM_GIA_BloodAxeCairnstone_A005"
CONTRACT = "A005-CR-VISUAL-CORRECTION-A09"
BLUEPRINT_ROOT = Path("docs/assets/blueprints") / ASSET
PLAN_REL = BLUEPRINT_ROOT / "manifests/VISUAL_CORRECTION_A09_PLAN.json"
VALIDATION_REL = BLUEPRINT_ROOT / "manifests/VISUAL_CORRECTION_A09_VALIDATION.json"
MEASUREMENT_REL = BLUEPRINT_ROOT / "manifests/VISUAL_CORRECTION_A08_TOP_STONE_MEASUREMENT.json"
DCC_ROOT = Path("SourceAssets/Blender/Props/Giants/BloodAxe/Cairns") / ASSET
A09_BLEND_REL = DCC_ROOT / f"{ASSET}_DCCGameReady_VisualCorrection_A09.blend"
A04_BLEND_REL = DCC_ROOT / f"{ASSET}_DCCGameReady_VisualCorrection_A04.blend"
MANIFEST_REL = DCC_ROOT / f"{ASSET}_VISUAL_CORRECTION_A09_MANIFEST.json"
EXPORT_ROOT = Path("SourceAssets/Exports/Props/Giants/BloodAxe/Cairns") / ASSET / "VisualCorrection_A09"
ASSEMBLED_FBX_RELS = {
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
MODULE_OBJECTS = {
    "C001": f"{ASSET}_C001_MONOLITH_A09",
    "C002": f"{ASSET}_C002_UPPER_COURSE_A09",
    "C003": f"{ASSET}_C003_LOWER_COURSE_A09",
    "C004": f"{ASSET}_C004_RUBBLE_APRON_A09",
}
SOCKETS = ["SOCKET_A005_ROOT", "SOCKET_A005_C001", "SOCKET_A005_C002", "SOCKET_A005_C003", "SOCKET_A005_C004"]
OUTPUT_ROOT_REL = Path("Saved/Automation/DCC") / ASSET / "Production/VisualCorrection_A09"
FINAL_REL = OUTPUT_ROOT_REL / f"{ASSET}_FINAL_CORRECTED_3D_A09.png"
FINAL_RGBA_REL = OUTPUT_ROOT_REL / f"{ASSET}_FINAL_CORRECTED_3D_A09_OBJECT_RGBA.png"
FINAL_AUDIT_REL = OUTPUT_ROOT_REL / "FINAL_RENDER_AUDIT_A09.json"
MASK_MANIFEST_REL = Path("SourceAssets/Textures/Props/Giants/BloodAxe/Cairns") / ASSET / "Technical" / f"{ASSET}_SOURCE_MASK_MANIFEST_A01.json"
UV_PLAN_REL = BLUEPRINT_ROOT / "manifests/STEP_14_UV_OWNERSHIP_PLAN.json"
SOURCE_BC_REL = Path("SourceAssets/Textures/Props/Giants/BloodAxe/Cairns") / ASSET / "T_GIA_BloodAxeCairnstone_A005_BC.png"
A09_BC_REL = Path("SourceAssets/Textures/Props/Giants/BloodAxe/Cairns") / ASSET / "VisualCorrection_A09/T_GIA_BloodAxeCairnstone_A005_VF_A09_BC.png"


def sha256_file(path: Path) -> str:
    digest = hashlib.sha256()
    with path.open("rb") as handle:
        for block in iter(lambda: handle.read(1024 * 1024), b""):
            digest.update(block)
    return digest.hexdigest()


def hash_json(value: Any) -> str:
    payload = json.dumps(value, sort_keys=True, separators=(",", ":")).encode("utf-8")
    return hashlib.sha256(payload).hexdigest()


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


def topology_record(obj: Any) -> Dict[str, int]:
    import bmesh  # type: ignore

    bm = bmesh.new()
    bm.from_mesh(obj.data)
    result = {
        "components": len(component_indices(obj.data)),
        "boundary_edges": sum(1 for edge in bm.edges if len(edge.link_faces) == 1),
        "nonmanifold_edges": sum(1 for edge in bm.edges if len(edge.link_faces) not in (1, 2)),
        "degenerate_faces": sum(1 for face in bm.faces if face.calc_area() <= 1.0e-8),
    }
    bm.free()
    return result


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
    candidate = Image.open(ROOT / A09_BC_REL).convert("RGB")
    compared = 0
    mismatches = 0
    by_view: Dict[str, Any] = {}
    for record in mask_manifest["records"]:
        mask = Image.open(ROOT / record["mask_path"]).convert("L")
        rect = windows[record["view"]]
        view_compared = 0
        view_mismatches = 0
        for source_pixel, candidate_pixel, owned in zip(source.crop(tuple(rect)).getdata(), candidate.crop(tuple(rect)).getdata(), mask.getdata()):
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
    result: Dict[str, Any] = {"assembled": {}, "modules": {}}
    for lod_name, rel in ASSEMBLED_FBX_RELS.items():
        bpy.ops.wm.read_factory_settings(use_empty=True)
        bpy.ops.import_scene.fbx(filepath=str(ROOT / rel), use_custom_normals=True)
        meshes = [obj for obj in bpy.context.scene.objects if obj.type == "MESH"]
        primary = [obj for obj in meshes if not obj.name.startswith("UCX_")]
        triangles = sum(mesh_triangles(obj.data) for obj in primary)
        expected = int(manifest["lods"][lod_name]["triangles"])
        result["assembled"][lod_name] = {
            "mesh_objects": len(meshes),
            "primary_objects": len(primary),
            "primary_triangles": triangles,
            "expected_triangles": expected,
            "pass": len(primary) == 1 and triangles == expected,
        }
    for component, rel in MODULE_FBX_RELS.items():
        bpy.ops.wm.read_factory_settings(use_empty=True)
        bpy.ops.import_scene.fbx(filepath=str(ROOT / rel), use_custom_normals=True)
        meshes = [obj for obj in bpy.context.scene.objects if obj.type == "MESH"]
        empties = [obj for obj in bpy.context.scene.objects if obj.type == "EMPTY"]
        triangles = sum(mesh_triangles(obj.data) for obj in meshes)
        expected = int(manifest["module_subset_records"][component]["triangles"])
        expected_socket = f"SOCKET_A005_{component}"
        socket_matches = [obj for obj in empties if obj.name == expected_socket]
        socket_pass = (
            len(socket_matches) == 1
            and len(meshes) == 1
            and close(socket_matches[0].location, [0.0, 0.0, 0.0])
            and close(socket_matches[0].rotation_euler, [0.0, 0.0, 0.0], 1.0e-6)
            and close(socket_matches[0].location, meshes[0].location)
            and close(socket_matches[0].rotation_euler, meshes[0].rotation_euler, 1.0e-6)
            and close(socket_matches[0].scale, meshes[0].scale, 1.0e-6)
        )
        result["modules"][component] = {
            "mesh_objects": len(meshes),
            "triangles": triangles,
            "expected_triangles": expected,
            "socket": expected_socket,
            "socket_scale_after_blender_fbx_unit_conversion": list(socket_matches[0].scale) if socket_matches else None,
            "socket_pass": socket_pass,
            "pass": len(meshes) == 1 and triangles == expected and socket_pass,
        }
    return result


def main() -> int:
    import bpy  # type: ignore
    from PIL import Image

    plan = load_json(PLAN_REL)
    measurement = load_json(MEASUREMENT_REL)
    manifest = load_json(MANIFEST_REL)
    render_audit = load_json(FINAL_AUDIT_REL)
    bpy.ops.wm.open_mainfile(filepath=str(ROOT / A09_BLEND_REL))

    lods = {name: bpy.data.objects.get(f"{ASSET}_{name}") for name in ("LOD0", "LOD1", "LOD2", "LOD3")}
    modules = {name: bpy.data.objects.get(object_name) for name, object_name in MODULE_OBJECTS.items()}
    if any(obj is None for obj in (*lods.values(), *modules.values())):
        raise RuntimeError("A09 blend is missing a required LOD or module object")
    lod_records = {
        name: {
            "triangles": mesh_triangles(obj.data),
            "bounds": object_bounds(obj),
            "uv_layers": [layer.name for layer in obj.data.uv_layers],
            "materials": len(obj.data.materials),
            "topology": topology_record(obj),
        }
        for name, obj in lods.items()
    }
    module_records = {
        name: {
            "triangles": mesh_triangles(obj.data),
            "bounds": object_bounds(obj),
            "uv_layers": [layer.name for layer in obj.data.uv_layers],
            "materials": len(obj.data.materials),
            "topology": topology_record(obj),
            "stone_count": int(obj.get("aerathea_individual_stone_count", 0)) if name != "C001" else 1,
            "receiver_count": int(obj.get("aerathea_A09_hidden_receiver_count", 0)) if name != "C001" else 0,
        }
        for name, obj in modules.items()
    }
    for name, record in module_records.items():
        if name == "C001":
            continue
        record["receiver_count"] = 1 if record["topology"]["boundary_edges"] > 0 else 0
        record["stone_count"] = record["topology"]["components"] - record["receiver_count"]
    socket_records = {}
    for name in SOCKETS:
        obj = bpy.data.objects.get(name)
        socket_records[name] = None if obj is None else {
            "location_cm": [float(value) for value in obj.location],
            "rotation_rad": [float(value) for value in obj.rotation_euler],
            "scale": [float(value) for value in obj.scale],
            "pass": close(obj.location, [0.0, 0.0, 0.0]) and close(obj.rotation_euler, [0.0, 0.0, 0.0]) and close(obj.scale, [1.0, 1.0, 1.0]),
        }
    collisions = sorted(name for name in bpy.data.objects.keys() if name.startswith("UCX_"))
    material = lods["LOD0"].data.materials[0] if len(lods["LOD0"].data.materials) else None
    material_nodes = sorted(node.name for node in material.node_tree.nodes) if material and material.use_nodes else []

    a04_lod0 = load_object_from_blend(bpy, A04_BLEND_REL, f"{ASSET}_LOD0")
    a04_components = component_indices(a04_lod0.data)
    a04_c001_indices = max(a04_components, key=lambda indices: max(float(a04_lod0.data.vertices[index].co.z) for index in indices))
    a09_c001_indices = component_indices(modules["C001"].data)[0]
    c001_signatures = {
        "A04": component_signature(a04_lod0, a04_c001_indices),
        "A09": component_signature(modules["C001"], a09_c001_indices),
    }

    authority = {}
    for name, record in plan["authority_inputs"].items():
        actual = sha256_file(ROOT / record["path"])
        authority[name] = {"expected": record["sha256"], "actual": actual, "pass": actual == record["sha256"]}
    source_actual = sha256_file(ROOT / plan["source_authority"]["path"])
    authority["source_authority"] = {"expected": plan["source_authority"]["sha256"], "actual": source_actual, "pass": source_actual == plan["source_authority"]["sha256"]}
    source_rgb = source_owned_rgb_audit()

    assembled_hashes = {
        name: {"expected": manifest["exports"][name]["sha256"], "actual": sha256_file(ROOT / rel)}
        for name, rel in ASSEMBLED_FBX_RELS.items()
    }
    module_hashes = {
        name: {"expected": manifest["module_exports"][name]["sha256"], "actual": sha256_file(ROOT / rel)}
        for name, rel in MODULE_FBX_RELS.items()
    }
    blend_hash = {"expected": manifest["blend"]["sha256"], "actual": sha256_file(ROOT / A09_BLEND_REL)}
    final_hash = {"expected": render_audit["sha256"], "actual": sha256_file(ROOT / FINAL_REL)}

    expected_extents = {name: plan["modules"][name]["outer_extent_cm"] for name in ("C002", "C003", "C004")}
    ovoid_records = {}
    for component in ("C002", "C003", "C004"):
        top = render_audit["module_proofs"][component]["top"]["alpha_bounds"]["bbox_half_open_px"]
        pixel_ratio = (top[2] - top[0]) / (top[3] - top[1])
        target_ratio = expected_extents[component][0] / expected_extents[component][1]
        ovoid_records[component] = {"pixel_ratio": pixel_ratio, "target_ratio": target_ratio, "difference": abs(pixel_ratio - target_ratio), "pass": pixel_ratio >= 1.20 and abs(pixel_ratio - target_ratio) <= 0.03}

    render_rgba = Image.open(ROOT / FINAL_RGBA_REL).convert("RGBA")
    object_pixels = [(r, g, b) for r, g, b, alpha in render_rgba.getdata() if alpha >= 16]
    bright_fraction = sum(1 for pixel in object_pixels if min(pixel) >= 180 and max(pixel) - min(pixel) <= 20) / max(1, len(object_pixels))
    clean_import = clean_fbx_reimport(bpy, manifest)

    gates: List[Dict[str, Any]] = []

    def gate(gate_id: str, passed: bool, detail: Any) -> None:
        gates.append({"id": gate_id, "status": "pass" if passed else "fail", "detail": detail})

    gate("G01_authority_hashes", all(record["pass"] for record in authority.values()), authority)
    controls = plan["controls"]
    gate("G02_contract_and_scope", manifest.get("contract_id") == CONTRACT and manifest.get("artifact_classification") == "candidate" and manifest.get("A08_course_geometry_inputs") == 0 and controls.get("fresh_A09_course_geometry") is True, {"manifest_contract": manifest.get("contract_id"), "classification": manifest.get("artifact_classification"), "A08_course_geometry_inputs": manifest.get("A08_course_geometry_inputs"), "fresh_A09_course_geometry": controls.get("fresh_A09_course_geometry")})
    lod_triangles = [lod_records[name]["triangles"] for name in ("LOD0", "LOD1", "LOD2", "LOD3")]
    gate("G03_lods_and_budget", 4000 <= lod_triangles[0] <= 10000 and all(lod_triangles[index] > lod_triangles[index + 1] for index in range(3)) and all(lod_records[name]["triangles"] == int(manifest["lods"][name]["triangles"]) for name in lod_records), {"triangles": lod_triangles, "target_range_LOD0": [4000, 10000]})
    gate("G04_bounds_and_pivot", all(close(lod_records[name]["bounds"]["dimensions"], [140.0, 110.0, 220.0]) and close(lod_records[name]["bounds"]["min"], [-70.0, -55.0, 0.0]) for name in lod_records), {name: lod_records[name]["bounds"] for name in lod_records})
    gate("G05_module_components_and_counts", [module_records[name]["topology"]["components"] for name in ("C001", "C002", "C003", "C004")] == [1, 20, 25, 33] and [module_records[name]["stone_count"] for name in ("C002", "C003", "C004")] == [19, 24, 32] and [module_records[name]["receiver_count"] for name in ("C002", "C003", "C004")] == [1, 1, 1], module_records)
    extents_pass = all(close(module_records[name]["bounds"]["dimensions"][:2], expected_extents[name], 0.01) for name in expected_extents)
    gate("G06_retained_module_extents", extents_pass, {name: {"actual": module_records[name]["bounds"]["dimensions"][:2], "expected": expected_extents[name]} for name in expected_extents})
    gate("G07_irregular_ovoid_top_proofs", all(record["pass"] for record in ovoid_records.values()) and manifest.get("source_conditioned_irregular_ovoid") is True, ovoid_records)
    gate("G08_exact_A04_C001_geometry_and_uv", c001_signatures["A04"] == c001_signatures["A09"], c001_signatures)
    gate("G09_shared_origin_sockets", all(record is not None and record["pass"] for record in socket_records.values()), socket_records)
    topology_pass = lod_records["LOD0"]["topology"] == {"components": 79, "boundary_edges": 208, "nonmanifold_edges": 0, "degenerate_faces": 0} and [module_records[name]["topology"]["boundary_edges"] for name in ("C001", "C002", "C003", "C004")] == [0, 64, 64, 80]
    gate("G10_topology_and_declared_open_receiver_collars", topology_pass, {"LOD0": lod_records["LOD0"]["topology"], "modules": {name: module_records[name]["topology"] for name in module_records}, "policy": "only the deliberately hidden receiver top loops are boundary edges; no degenerate faces"})
    material_pass = all(record["uv_layers"] == ["UVMap", "LightmapUV"] and record["materials"] == 1 for record in (*lod_records.values(), *module_records.values())) and all(name in material_nodes for name in ("A09_DIRECT_SOURCE_BASECOLOR", "A09_DIRECTX_NORMAL", "A09_ORM_NONMETALLIC"))
    gate("G11_material_and_uv", material_pass, {"material_nodes": material_nodes, "lods": {name: {"uv_layers": record["uv_layers"], "materials": record["materials"]} for name, record in lod_records.items()}, "modules": {name: {"uv_layers": record["uv_layers"], "materials": record["materials"]} for name, record in module_records.items()}})
    gate("G12_source_owned_rgb_exact", source_rgb["pixels_compared"] > 0 and source_rgb["mismatches"] == 0 and measurement.get("status") == "pass_authoritative_measurement_gate", {"atlas": source_rgb, "measurement_status": measurement.get("status")})
    gate("G13_collision_set", len(collisions) == 4, collisions)
    hash_pass = blend_hash["expected"] == blend_hash["actual"] and final_hash["expected"] == final_hash["actual"] and all(record["expected"] == record["actual"] for record in (*assembled_hashes.values(), *module_hashes.values()))
    gate("G14_artifact_hashes", hash_pass, {"blend": blend_hash, "final": final_hash, "assembled_fbx": assembled_hashes, "module_fbx": module_hashes})
    import_pass = all(record["pass"] for record in clean_import["assembled"].values()) and all(record["pass"] for record in clean_import["modules"].values())
    gate("G15_clean_fbx_reimport", import_pass, clean_import)
    proof_keys = set(render_audit.get("assembled_proofs", {}))
    module_proofs = render_audit.get("module_proofs", {})
    proof_pass = {"front_shadeless", "left_shadeless", "right_shadeless", "top_shadeless", "front_lit"}.issubset(proof_keys) and all({"front", "top"}.issubset(module_proofs.get(name, {})) for name in ("C002", "C003", "C004")) and render_audit["assembled_proofs"]["top_shadeless"].get("camera", "").startswith("true orthographic")
    gate("G16_required_proof_set", proof_pass, {"assembled": sorted(proof_keys), "modules": {name: sorted(module_proofs.get(name, {})) for name in ("C002", "C003", "C004")}})
    interface_gate = render_audit.get("interface_alpha_gate", {})
    gate("G17_zero_background_interface_leaks", interface_gate.get("pass") is True and interface_gate.get("background_leak_pixels") == 0, interface_gate)
    final_margins = render_audit["alpha_bounds"]["margins_px"]
    final_integrity = render_audit.get("size") == [1400, 1600] and min(final_margins.values()) >= 80 and render_audit.get("review_markers") == 0 and render_audit.get("collision_visible") == 0 and render_audit.get("lod_visible") == "LOD0 only" and bright_fraction <= 0.001
    gate("G18_final_review_integrity", final_integrity, {"size": render_audit.get("size"), "margins": final_margins, "bright_fringe_fraction": bright_fraction, "review_markers": render_audit.get("review_markers"), "collision_visible": render_audit.get("collision_visible"), "lod_visible": render_audit.get("lod_visible")})
    gate("G19_C004_clustered_rubble", manifest.get("C004_clustered_rubble") is True and manifest["a09_modules"]["C004"].get("clusters") == 8 and manifest["a09_modules"]["C004"].get("staggered_rows") == 2, manifest["a09_modules"]["C004"])
    preserved = manifest.get("preservation", {})
    unreal_pass = manifest.get("unreal_outputs") == 0 and manifest.get("fully_game_ready") is False and controls.get("unreal_authorized") is False
    gate("G20_preservation_and_unreal_firewall", all(record.get("pass") for record in preserved.values()) and unreal_pass, {"preservation": preserved, "unreal_outputs": manifest.get("unreal_outputs"), "fully_game_ready": manifest.get("fully_game_ready"), "unreal_authorized": controls.get("unreal_authorized")})

    passed = sum(1 for record in gates if record["status"] == "pass")
    complete = passed == len(gates)
    validation = {
        "schema": "aerathea.a005_visual_correction_a09_validation.v1",
        "asset_id": ASSET,
        "contract_id": CONTRACT,
        "date": "2026-07-21",
        "status": "pass_candidate_pending_flamestrike_visual_review" if complete else "blocked_a09_independent_audit",
        "artifact_classification": "proof only",
        "pipeline_status": "DCC game-ready candidate" if complete else "candidate blocked",
        "fully_game_ready": False,
        "unreal_outputs": 0,
        "candidate": {"manifest": str(MANIFEST_REL), "manifest_sha256": sha256_file(ROOT / MANIFEST_REL)},
        "final_review_image": {"path": str(FINAL_REL), "sha256": final_hash["actual"], "visual_gate": "pending Flamestrike"},
        "gates": gates,
        "gate_summary": {"passed": passed, "total": len(gates)},
    }
    (ROOT / VALIDATION_REL).write_text(json.dumps(validation, indent=2) + "\n", encoding="utf-8")
    print(json.dumps(validation, indent=2))
    return 0 if complete else 1


if __name__ == "__main__":
    raise SystemExit(main())
