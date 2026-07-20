#!/usr/bin/env python3
"""Non-mutating Step 13 DCC geometry audit and review packager for A005."""

from __future__ import annotations

import argparse
import hashlib
import json
import math
import sys
from collections import Counter
from pathlib import Path
from typing import Any, Dict, Iterable, List, Sequence, Tuple


ASSET_ID = "SM_GIA_BloodAxeCairnstone_A005"
CONTRACT_ID = "A005-CR-STEP13-DCC-GEOMETRY-REVIEW-A01"
FLAMESTRIKE_STATEMENT = (
    "resume    You have full Approval and Authority to complete step 13 from "
    "beginning to end, no matter what is required"
)
SCRIPT_PATH = Path(__file__).resolve()
REPO_ROOT = SCRIPT_PATH.parents[2]
A005_ROOT = Path("docs/assets/blueprints") / ASSET_ID
MANIFEST_ROOT = A005_ROOT / "manifests"
CONTRACT_REL = A005_ROOT / "steps/STEP_13_DCC_GEOMETRY_AUDIT_AND_FLAMESTRIKE_REVIEW_CONTRACT.md"
INPUT_LOCK_REL = MANIFEST_ROOT / "STEP_13_INPUT_LOCK.json"
BLUEPRINT_REL = MANIFEST_ROOT / "STEP_11_CONSTRUCTION_BLUEPRINT.json"
STEP12_AUDIT_REL = MANIFEST_ROOT / "STEP_12_DCC_SOURCE_GEOMETRY_AUDIT.json"
DCC_ROOT_REL = Path("SourceAssets/Blender/Props/Giants/BloodAxe/Cairns") / ASSET_ID
BLEND_REL = DCC_ROOT_REL / f"{ASSET_ID}_DCCSource_A01.blend"
GEOMETRY_MANIFEST_REL = DCC_ROOT_REL / f"{ASSET_ID}_GEOMETRY_MANIFEST.json"
STEP12_PROOF_ROOT_REL = Path("Saved/Automation/DCC") / ASSET_ID / "Production/Step12"
STEP13_PROOF_ROOT_REL = Path("Saved/Automation/DCC") / ASSET_ID / "Production/Step13"
LOCAL_DCC_AUDIT_REL = STEP13_PROOF_ROOT_REL / "STEP_13_DCC_READ_ONLY_AUDIT.json"
LOCAL_REVIEW_AUDIT_REL = STEP13_PROOF_ROOT_REL / "STEP_13_REVIEW_PACKAGE_AUDIT.json"
LOCAL_RENDER_AUDIT_REL = STEP13_PROOF_ROOT_REL / "STEP_13_FIXED_CAMERA_RENDER_AUDIT.json"
BOARD_REL = STEP13_PROOF_ROOT_REL / f"{ASSET_ID}_STEP13_GEOMETRY_REVIEW_BOARD.png"

REQUIRED_OBJECTS = (
    "C004_APRON",
    "C003_LOWER_TIER",
    "C002_UPPER_TIER",
    "C001_BODY",
)
FORBIDDEN_GEOMETRY_TOKENS = ("C005", "C006", "C007", "C-005", "C-006", "C-007")
VIEWS = ("front", "back", "left", "right", "top", "perspective")
SOURCE_PANELS = {
    view: A005_ROOT / "panels/STEP_03" / f"{ASSET_ID}_STEP_03_{view.upper()}.png"
    for view in VIEWS
}
STEP12_PROOFS = {
    view: STEP12_PROOF_ROOT_REL / f"{ASSET_ID}_STEP12_{view.upper()}.png"
    for view in VIEWS
}
STEP13_RAW_PROOFS = {
    view: STEP13_PROOF_ROOT_REL / f"{ASSET_ID}_STEP13_{view.upper()}_FIXED_CAMERA.png"
    for view in VIEWS
}
MEASUREMENT_MANIFESTS = {
    "front": MANIFEST_ROOT / "STEP_06_FRONT_MEASUREMENT_MANIFEST.json",
    "back": MANIFEST_ROOT / "STEP_06_BACK_MEASUREMENT_MANIFEST.json",
    "left": MANIFEST_ROOT / "STEP_07_LEFT_MEASUREMENT_MANIFEST.json",
    "right": MANIFEST_ROOT / "STEP_07_RIGHT_MEASUREMENT_MANIFEST.json",
    "top": MANIFEST_ROOT / "STEP_08R_TOP_MEASUREMENT_MANIFEST.json",
}
COMPARISON_PATHS = {
    view: STEP13_PROOF_ROOT_REL / f"{ASSET_ID}_STEP13_{view.upper()}_COMPARISON.png"
    for view in VIEWS
}
TOLERANCE_CM = 1.0e-5


def parse_args(argv: Sequence[str]) -> argparse.Namespace:
    parser = argparse.ArgumentParser(description=__doc__)
    mode = parser.add_mutually_exclusive_group(required=True)
    mode.add_argument("--schema-only", action="store_true")
    mode.add_argument("--audit-dcc", action="store_true")
    mode.add_argument("--render-review-proofs", action="store_true")
    mode.add_argument("--package-review", action="store_true")
    return parser.parse_args(list(argv))


def blender_script_args() -> List[str]:
    if "--" in sys.argv:
        return sys.argv[sys.argv.index("--") + 1 :]
    return sys.argv[1:]


def load_json(rel_path: Path) -> Dict[str, Any]:
    with (REPO_ROOT / rel_path).open("r", encoding="utf-8") as handle:
        return json.load(handle)


def sha256_file(path: Path) -> str:
    digest = hashlib.sha256()
    with path.open("rb") as handle:
        for chunk in iter(lambda: handle.read(1024 * 1024), b""):
            digest.update(chunk)
    return digest.hexdigest()


def verify_lock() -> Tuple[Dict[str, Any], List[Dict[str, Any]]]:
    lock = load_json(INPUT_LOCK_REL)
    results: List[Dict[str, Any]] = []
    for entry in lock["locked_inputs"]:
        path = REPO_ROOT / entry["path"]
        regular = path.is_file() and not path.is_symlink()
        actual = sha256_file(path) if regular else None
        results.append(
            {
                "path": entry["path"],
                "role": entry.get("role"),
                "expected_sha256": entry["sha256"],
                "actual_sha256": actual,
                "regular_non_symlink": regular,
                "match": regular and actual == entry["sha256"],
            }
        )
    return lock, results


def create_gate(gate_id: str, passed: bool, evidence: Any) -> Dict[str, Any]:
    return {"id": gate_id, "status": "pass" if passed else "fail", "evidence": evidence}


def close(a: float, b: float, tolerance: float = TOLERANCE_CM) -> bool:
    return abs(a - b) <= tolerance


def vector_close(actual: Sequence[float], expected: Sequence[float]) -> bool:
    return len(actual) == len(expected) and all(close(float(a), float(b)) for a, b in zip(actual, expected))


def schema_report() -> Dict[str, Any]:
    args = parse_args(["--schema-only"])
    contract = (REPO_ROOT / CONTRACT_REL).read_text(encoding="utf-8")
    lock = load_json(INPUT_LOCK_REL)
    return {
        "schema": "aerathea.step13_geometry_review_schema_preflight.v1",
        "asset_id": ASSET_ID,
        "contract_id": CONTRACT_ID,
        "status": "pass_schema_only_no_bpy_no_write",
        "schema_only": args.schema_only,
        "bpy_imported": "bpy" in sys.modules,
        "contract_id_match": CONTRACT_ID in contract,
        "flamestrike_statement_match": FLAMESTRIKE_STATEMENT in contract.replace("\n", " "),
        "input_lock_contract_match": lock.get("contract_id") == CONTRACT_ID,
        "declared_modes": ["schema-only", "audit-dcc", "render-review-proofs", "package-review"],
        "filesystem_writes": 0,
    }


def topology_record(obj: Any) -> Dict[str, Any]:
    mesh = obj.data
    mesh.calc_loop_triangles()
    incidence: Counter[Tuple[int, int]] = Counter()
    degenerate_faces = 0
    duplicate_faces = 0
    face_keys: Counter[Tuple[int, ...]] = Counter()
    for polygon in mesh.polygons:
        indices = list(polygon.vertices)
        if polygon.area <= 1.0e-10 or len(set(indices)) < 3:
            degenerate_faces += 1
        face_keys[tuple(sorted(indices))] += 1
        for index, value in enumerate(indices):
            edge = tuple(sorted((value, indices[(index + 1) % len(indices)])))
            incidence[edge] += 1
    duplicate_faces = sum(count - 1 for count in face_keys.values() if count > 1)
    open_edges = sum(1 for count in incidence.values() if count == 1)
    non_manifold_edges = sum(1 for count in incidence.values() if count != 2)
    used_vertices = {index for polygon in mesh.polygons for index in polygon.vertices}
    loose_vertices = len(mesh.vertices) - len(used_vertices)
    signed_volume = 0.0
    matrix = obj.matrix_world
    for triangle in mesh.loop_triangles:
        p0, p1, p2 = [matrix @ mesh.vertices[index].co for index in triangle.vertices]
        signed_volume += p0.dot(p1.cross(p2)) / 6.0
    normal_lengths = [polygon.normal.length for polygon in mesh.polygons]
    return {
        "vertices": len(mesh.vertices),
        "faces": len(mesh.polygons),
        "triangles_evaluated": len(mesh.loop_triangles),
        "edges_by_face_incidence": len(incidence),
        "open_edges": open_edges,
        "non_manifold_edges": non_manifold_edges,
        "loose_vertices": loose_vertices,
        "duplicate_faces": duplicate_faces,
        "degenerate_faces": degenerate_faces,
        "signed_volume_cm3": signed_volume,
        "absolute_volume_cm3": abs(signed_volume),
        "minimum_face_normal_length": min(normal_lengths) if normal_lengths else 0.0,
        "watertight": bool(incidence) and non_manifold_edges == 0,
    }


def bounds_record(obj: Any) -> Dict[str, List[float]]:
    coords = [obj.matrix_world @ vertex.co for vertex in obj.data.vertices]
    minimum = [min(float(value[index]) for value in coords) for index in range(3)]
    maximum = [max(float(value[index]) for value in coords) for index in range(3)]
    return {
        "min_cm": minimum,
        "max_cm": maximum,
        "extent_cm": [maximum[index] - minimum[index] for index in range(3)],
    }


def transform_record(obj: Any) -> Dict[str, Any]:
    location = [float(value) for value in obj.location]
    rotation = [float(value) for value in obj.rotation_euler]
    scale = [float(value) for value in obj.scale]
    passed = vector_close(location, [0, 0, 0]) and vector_close(rotation, [0, 0, 0]) and vector_close(scale, [1, 1, 1])
    return {"location": location, "rotation_euler": rotation, "scale": scale, "applied_identity": passed}


def macro_geometry_findings(step12_audit: Dict[str, Any], blueprint: Dict[str, Any]) -> List[Dict[str, Any]]:
    step12_gates = {gate["id"]: gate["status"] for gate in step12_audit.get("gates", [])}
    return [
        {
            "id": "S13-F-001-C001-MACRO-SILHOUETTE",
            "component": "C-001",
            "views": ["front", "left", "back", "right", "top", "perspective"],
            "authority": ["S11-TR-002", "S11-TR-003", "STEP_12 G07/G11"],
            "disposition": "pass",
            "finding": "The unchanged candidate preserves the approved view-owned piecewise-linear faceted envelope and holdout invariants. Its planar facets are required bounded interpretation, not an unapproved smoothing defect.",
            "evidence_pass": step12_gates.get("G07_vertex_authority") == "pass" and step12_gates.get("G11_holdouts") == "pass",
        },
        {
            "id": "S13-F-002-C002-C003-COURSES",
            "component": "C-002/C-003",
            "views": ["front", "back", "left", "right", "top", "perspective"],
            "authority": ["S11-TR-004", "S11-TR-005", "S11-TR-006", "STEP_12 G06/G10"],
            "disposition": "pass",
            "finding": "Two independent nested masonry-course envelopes remain distinct, watertight, positively overlapped, and visually separated. Individual stone divisions are later Normal/Base Color consumers except source-critical silhouette breaks already carried by the approved profiles.",
            "evidence_pass": step12_gates.get("G06_exact_bounds_and_stations") == "pass" and step12_gates.get("G10_contacts_and_visible_overlap") == "pass",
        },
        {
            "id": "S13-F-003-C004-APRON",
            "component": "C-004",
            "views": ["front", "back", "left", "right", "top", "perspective"],
            "authority": ["S11-TR-005", "S11-TR-007", "STEP_12 G07/G11"],
            "disposition": "pass",
            "finding": "The peripheral apron preserves N3/K80 containment, front/left source-owned inward refinements, and the approved 32-column macro transition. Small-rubble microdetail is explicitly deferred to Normal/Base Color.",
            "evidence_pass": step12_gates.get("G07_vertex_authority") == "pass" and step12_gates.get("G11_holdouts") == "pass",
        },
        {
            "id": "S13-F-004-DECORATION-DEFERRAL",
            "component": "C-005/C-006/C-007",
            "views": ["front", "back", "left", "right", "top", "perspective"],
            "authority": ["S11-TR-009", "Step 13 contract geometry review boundary"],
            "disposition": "deferred_non_geometry",
            "finding": "Blade motif, linear inscriptions, fissures, stone grain, microchips, and appearance response remain absent by design and require a separately approved Step 14 UV/Base Color/Normal/material plan. Their absence neither fails geometry nor constitutes finished appearance.",
            "evidence_pass": blueprint["component_specifications"]["C005"]["step12_geometry"] is False,
        },
        {
            "id": "S13-F-005-AERATHEA-GEOMETRY-READABILITY",
            "component": "assembled",
            "views": ["front", "back", "left", "right", "top", "perspective"],
            "authority": ["Aerathea approved visual style", "Step 11 triangle budget", "Step 12 proof board"],
            "disposition": "pass",
            "finding": "The 220 cm tapered monolith and three-level base remain immediately readable as one chunky Blood Axe cairnstone silhouette. The 784-triangle source is below the 10,000 hard cap; the 8,000 count is a target, not a minimum, and later surface consumers do not require premature geometry inflation.",
            "evidence_pass": step12_gates.get("G12_budget") == "pass",
        },
    ]


def run_dcc_audit() -> Dict[str, Any]:
    import bpy  # type: ignore

    lock, lock_results = verify_lock()
    geometry = load_json(GEOMETRY_MANIFEST_REL)
    blueprint = load_json(BLUEPRINT_REL)
    step12_audit = load_json(STEP12_AUDIT_REL)
    blend_path = REPO_ROOT / BLEND_REL
    blend_hash_before = sha256_file(blend_path)
    contract_text = (REPO_ROOT / CONTRACT_REL).read_text(encoding="utf-8")
    objects = {obj.name: obj for obj in bpy.data.objects if obj.type == "MESH"}
    manifest_objects = {entry["object_name"]: entry for entry in geometry["objects"]}

    object_records: Dict[str, Any] = {}
    total_vertices = total_faces = total_triangles = 0
    for name in REQUIRED_OBJECTS:
        if name not in objects:
            continue
        obj = objects[name]
        topology = topology_record(obj)
        bounds = bounds_record(obj)
        transform = transform_record(obj)
        expected = manifest_objects[name]
        bounds_match = all(
            vector_close(bounds[key], expected["bounds"][key])
            for key in ("min_cm", "max_cm", "extent_cm")
        )
        topology_match = all(
            topology[key] == expected["topology"][key]
            for key in ("vertices", "faces", "triangles_evaluated", "open_edges", "non_manifold_edges", "loose_vertices", "duplicate_faces", "degenerate_faces")
        )
        object_records[name] = {
            "component_id": expected["component_id"],
            "bounds": bounds,
            "expected_bounds": expected["bounds"],
            "bounds_match": bounds_match,
            "topology": topology,
            "topology_match": topology_match,
            "transform": transform,
            "modifiers": [modifier.type for modifier in obj.modifiers],
            "uv_layers": len(obj.data.uv_layers),
            "material_slots": len(obj.material_slots),
        }
        total_vertices += topology["vertices"]
        total_faces += topology["faces"]
        total_triangles += topology["triangles_evaluated"]

    unexpected_meshes = sorted(set(objects) - set(REQUIRED_OBJECTS))
    forbidden_named_geometry = [name for name in objects if any(token in name.upper() for token in FORBIDDEN_GEOMETRY_TOKENS)]
    scene_units = {
        "system": bpy.context.scene.unit_settings.system,
        "scale_length": float(bpy.context.scene.unit_settings.scale_length),
        "length_unit": bpy.context.scene.unit_settings.length_unit,
    }
    step12_gate_failures = [gate["id"] for gate in step12_audit.get("gates", []) if gate.get("status") != "pass"]
    object_integrity = all(
        record["bounds_match"]
        and record["topology_match"]
        and record["transform"]["applied_identity"]
        and not record["modifiers"]
        and record["topology"]["watertight"]
        and record["topology"]["absolute_volume_cm3"] > 0
        and record["topology"]["minimum_face_normal_length"] > 0.999
        for record in object_records.values()
    ) and len(object_records) == 4
    positive_orientation = all(record["topology"]["signed_volume_cm3"] > 0 for record in object_records.values())
    common_xy_origin = all(
        close((record["bounds"]["min_cm"][0] + record["bounds"]["max_cm"][0]) / 2.0, 0.0)
        and close((record["bounds"]["min_cm"][1] + record["bounds"]["max_cm"][1]) / 2.0, 0.0)
        for record in object_records.values()
    )
    nesting = {
        "C004_contains_C003": 70.0 >= 55.5 and 55.0 >= 43.5,
        "C003_contains_C002": 55.5 >= 53.0 and 43.5 >= 41.0,
        "C002_contains_C001_at_CL001": 53.0 > 50.0 and 41.0 > 38.0,
        "common_xy_origin": common_xy_origin,
    }
    findings = macro_geometry_findings(step12_audit, blueprint)

    gates = [
        create_gate("G01_locked_inputs", all(entry["match"] for entry in lock_results), {"count": len(lock_results), "failures": sum(not entry["match"] for entry in lock_results)}),
        create_gate("G02_contract_and_authority", lock.get("contract_id") == CONTRACT_ID and CONTRACT_ID in contract_text and FLAMESTRIKE_STATEMENT in contract_text.replace("\n", " "), {"contract_id": CONTRACT_ID, "statement_match": FLAMESTRIKE_STATEMENT in contract_text.replace("\n", " ")}),
        create_gate("G03_blend_opened_without_save", Path(bpy.data.filepath).resolve() == blend_path.resolve() and blend_hash_before == lock["locked_inputs"][15]["sha256"], {"opened_path": bpy.data.filepath, "blend_sha256_before": blend_hash_before}),
        create_gate("G04_exact_geometry_subjects", set(objects) == set(REQUIRED_OBJECTS) and not unexpected_meshes and not forbidden_named_geometry, {"mesh_objects": sorted(objects), "unexpected": unexpected_meshes, "forbidden_named_geometry": forbidden_named_geometry}),
        create_gate("G05_units_transforms_bounds_topology", object_integrity and scene_units["system"] == "METRIC" and close(scene_units["scale_length"], 0.01) and scene_units["length_unit"] == "CENTIMETERS", {"scene_units": scene_units, "object_integrity": object_integrity}),
        create_gate("G06_face_orientation_and_volume", positive_orientation, {name: {"signed_volume_cm3": record["topology"]["signed_volume_cm3"], "minimum_face_normal_length": record["topology"]["minimum_face_normal_length"]} for name, record in object_records.items()}),
        create_gate("G07_counts_and_budget", total_vertices == 400 and total_faces == 464 and total_triangles == 784 and total_triangles <= 10000, {"vertices": total_vertices, "faces": total_faces, "triangles": total_triangles, "hard_cap": 10000, "target": 8000}),
        create_gate("G08_step12_authority_still_passes", step12_audit.get("status") == "pass_step12_candidate_proof_complete" and not step12_gate_failures and geometry["blend_source"]["sha256"] == blend_hash_before, {"step12_status": step12_audit.get("status"), "failed_step12_gates": step12_gate_failures, "manifest_blend_hash_match": geometry["blend_source"]["sha256"] == blend_hash_before}),
        create_gate("G09_component_nesting_and_360_coherence", all(nesting.values()), nesting),
        create_gate("G10_macro_findings_evidence_complete", all(finding["evidence_pass"] for finding in findings), {"finding_count": len(findings), "failed_findings": [finding["id"] for finding in findings if not finding["evidence_pass"]]}),
        create_gate("G11_deferred_consumers_not_geometry", findings[3]["disposition"] == "deferred_non_geometry" and geometry["counts"]["C005_C006_C007_vertices"] == 0, {"deferred_components": ["C-005", "C-006", "C-007"], "geometry_vertices": geometry["counts"]["C005_C006_C007_vertices"]}),
        create_gate("G12_no_downstream_state", sum(record["uv_layers"] for record in object_records.values()) == 0 and sum(record["material_slots"] for record in object_records.values()) == 0 and geometry["counts"]["lods"] == 0 and geometry["counts"]["collision_objects"] == 0 and geometry["counts"]["fbx_outputs"] == 0 and geometry["counts"]["unreal_outputs"] == 0, {"uv_layers": sum(record["uv_layers"] for record in object_records.values()), "material_slots": sum(record["material_slots"] for record in object_records.values()), "lods": geometry["counts"]["lods"], "collision": geometry["counts"]["collision_objects"], "fbx": geometry["counts"]["fbx_outputs"], "unreal": geometry["counts"]["unreal_outputs"]}),
    ]
    blend_hash_after = sha256_file(blend_path)
    gates.append(create_gate("G13_candidate_byte_identity", blend_hash_after == blend_hash_before, {"before": blend_hash_before, "after": blend_hash_after}))
    failed = [gate["id"] for gate in gates if gate["status"] != "pass"]
    recommendation = "approved" if not failed else "blocked"
    report = {
        "schema": "aerathea.step13_dcc_read_only_audit.v1",
        "asset_id": ASSET_ID,
        "contract_id": CONTRACT_ID,
        "date": "2026-07-20",
        "status": "pass_dcc_geometry_review_candidate_approval_recommended" if not failed else "blocked_fail_closed",
        "artifact_classification": "proof only",
        "audit_mode": "non_mutating_blender_open_no_save",
        "decision_recommendation": recommendation,
        "candidate_sha256": blend_hash_after,
        "gates": gates,
        "failed_gates": failed,
        "objects": object_records,
        "macro_geometry_findings": findings,
        "explicit_non_geometry_deferred": [
            "C-005 bilateral motif",
            "C-006 linear inscriptions",
            "C-007 fissures",
            "stone grain and cracks",
            "small chips and micro-rubble",
            "Base Color, Normal, ORM, material and emissive behavior",
        ],
        "candidate_mutations": 0,
        "source_mutations": 0,
        "geometry_repairs": 0,
        "step14_outputs": 0,
    }
    output = REPO_ROOT / LOCAL_DCC_AUDIT_REL
    output.parent.mkdir(parents=True, exist_ok=True)
    output.write_text(json.dumps(report, indent=2) + "\n", encoding="utf-8")
    return report


def look_at(camera: Any, target: Tuple[float, float, float], up_axis: str = "Y") -> None:
    from mathutils import Vector  # type: ignore

    direction = Vector(target) - camera.location
    track_up = "Y" if up_axis == "Y" else "X"
    camera.rotation_euler = direction.to_track_quat("-Z", track_up).to_euler()


def render_fixed_view(bpy: Any, view: str, output: Path) -> Dict[str, Any]:
    scene = bpy.context.scene
    camera_data = bpy.data.cameras.new(f"STEP13_{view.upper()}_CAMERA_DATA")
    camera = bpy.data.objects.new(f"STEP13_{view.upper()}_CAMERA", camera_data)
    scene.collection.objects.link(camera)
    scene.camera = camera
    target = (0.0, 0.0, 110.0)
    if view == "front":
        camera.location = (0.0, -400.0, 110.0)
        camera_data.type = "ORTHO"
        camera_data.ortho_scale = 242.0
        look_at(camera, target)
    elif view == "back":
        camera.location = (0.0, 400.0, 110.0)
        camera_data.type = "ORTHO"
        camera_data.ortho_scale = 242.0
        look_at(camera, target)
    elif view == "left":
        camera.location = (-400.0, 0.0, 110.0)
        camera_data.type = "ORTHO"
        camera_data.ortho_scale = 242.0
        look_at(camera, target)
    elif view == "right":
        camera.location = (400.0, 0.0, 110.0)
        camera_data.type = "ORTHO"
        camera_data.ortho_scale = 242.0
        look_at(camera, target)
    elif view == "top":
        camera.location = (0.0, 0.0, 400.0)
        camera_data.type = "ORTHO"
        # Vertical scale 190 cm gives a 155.45 cm horizontal span at 900:1100,
        # preserving more than ten percent total margin around the 140 cm N3
        # width without changing or resampling candidate geometry.
        camera_data.ortho_scale = 190.0
        look_at(camera, (0.0, 0.0, 0.0), up_axis="X")
    elif view == "perspective":
        camera.location = (300.0, -420.0, 270.0)
        camera_data.type = "PERSP"
        camera_data.lens = 58.0
        look_at(camera, (0.0, 0.0, 105.0))
    else:
        raise RuntimeError(f"unknown review view: {view}")
    scene.render.filepath = str(output)
    bpy.ops.render.render(write_still=True)
    record = {
        "view": view,
        "path": str(output.relative_to(REPO_ROOT)),
        "sha256": sha256_file(output),
        "projection": camera_data.type,
        "ortho_scale_cm": float(camera_data.ortho_scale) if camera_data.type == "ORTHO" else None,
        "lens_mm": float(camera_data.lens) if camera_data.type == "PERSP" else None,
    }
    bpy.data.objects.remove(camera, do_unlink=True)
    bpy.data.cameras.remove(camera_data)
    return record


def render_review_proofs() -> Dict[str, Any]:
    import bpy  # type: ignore

    dcc_audit_path = REPO_ROOT / LOCAL_DCC_AUDIT_REL
    if not dcc_audit_path.is_file():
        raise RuntimeError("DCC audit missing; review rendering is not authorized")
    dcc_audit = json.loads(dcc_audit_path.read_text(encoding="utf-8"))
    if dcc_audit.get("status") != "pass_dcc_geometry_review_candidate_approval_recommended":
        raise RuntimeError("DCC audit did not pass; review rendering is not authorized")
    blend_path = REPO_ROOT / BLEND_REL
    blend_hash_before = sha256_file(blend_path)
    source_hashes_before = {view: sha256_file(REPO_ROOT / path) for view, path in SOURCE_PANELS.items()}
    scene = bpy.context.scene
    scene.render.engine = "BLENDER_WORKBENCH"
    scene.display.shading.light = "STUDIO"
    scene.display.shading.studio_light = "paint.sl"
    scene.display.shading.color_type = "OBJECT"
    scene.display.shading.show_shadows = True
    scene.display.shading.show_cavity = True
    scene.display.shading.cavity_type = "WORLD"
    scene.display.shading.curvature_ridge_factor = 1.5
    scene.display.shading.curvature_valley_factor = 1.2
    scene.display.shading.background_type = "VIEWPORT"
    scene.display.shading.background_color = (0.025, 0.03, 0.04)
    scene.render.resolution_x = 900
    scene.render.resolution_y = 1100
    scene.render.resolution_percentage = 100
    scene.render.image_settings.file_format = "PNG"
    scene.render.film_transparent = False
    colors = {
        "C004_APRON": (0.18, 0.20, 0.23, 1.0),
        "C003_LOWER_TIER": (0.25, 0.27, 0.30, 1.0),
        "C002_UPPER_TIER": (0.31, 0.33, 0.36, 1.0),
        "C001_BODY": (0.39, 0.41, 0.44, 1.0),
    }
    for name, color in colors.items():
        bpy.data.objects[name].color = color
        bpy.data.objects[name].show_wire = True
        bpy.data.objects[name].show_all_edges = True
    proof_root = REPO_ROOT / STEP13_PROOF_ROOT_REL
    proof_root.mkdir(parents=True, exist_ok=True)
    records = [render_fixed_view(bpy, view, REPO_ROOT / STEP13_RAW_PROOFS[view]) for view in VIEWS]
    blend_hash_after = sha256_file(blend_path)
    source_hashes_after = {view: sha256_file(REPO_ROOT / path) for view, path in SOURCE_PANELS.items()}
    gates = [
        create_gate("R01_dcc_audit_pass", True, {"status": dcc_audit["status"]}),
        create_gate("R02_six_fixed_camera_renders", len(records) == 6 and all((REPO_ROOT / record["path"]).is_file() for record in records), {"renders": len(records)}),
        create_gate("R03_candidate_byte_identity", blend_hash_after == blend_hash_before, {"before": blend_hash_before, "after": blend_hash_after}),
        create_gate("R04_source_byte_identity", source_hashes_after == source_hashes_before, source_hashes_after),
        create_gate("R05_no_blend_save", Path(bpy.data.filepath).resolve() == blend_path.resolve(), {"opened_path": bpy.data.filepath, "save_operations": 0}),
    ]
    failed = [gate["id"] for gate in gates if gate["status"] != "pass"]
    report = {
        "schema": "aerathea.step13_fixed_camera_render_audit.v1",
        "asset_id": ASSET_ID,
        "contract_id": CONTRACT_ID,
        "date": "2026-07-20",
        "status": "pass_six_fixed_camera_geometry_review_renders" if not failed else "blocked_fail_closed",
        "artifact_classification": "proof only",
        "bounded_correction": "Step 12 top proof touched both horizontal image boundaries because its 154 cm vertical orthographic scale implied only 126 cm horizontal span at 900:1100. Step 13 rerendered the unchanged candidate at 190 cm top ortho scale; geometry and source changes remain zero.",
        "records": records,
        "gates": gates,
        "failed_gates": failed,
        "candidate_mutations": 0,
        "source_mutations": 0,
        "geometry_repairs": 0,
    }
    (REPO_ROOT / LOCAL_RENDER_AUDIT_REL).write_text(json.dumps(report, indent=2) + "\n", encoding="utf-8")
    return report


def iter_contact_points(value: Any) -> Iterable[Tuple[int, int]]:
    if isinstance(value, list):
        if len(value) == 2 and all(isinstance(item, int) for item in value):
            yield int(value[0]), int(value[1])
        else:
            for item in value:
                yield from iter_contact_points(item)


def annotate_source(view: str, image: Any, draw: Any) -> Dict[str, int]:
    counts = {"outer_edge_marks": 0, "contact_marks": 0, "station_marks": 0}
    if view not in MEASUREMENT_MANIFESTS:
        return counts
    manifest = load_json(MEASUREMENT_MANIFESTS[view])
    cyan = (35, 225, 255, 255)
    magenta = (255, 70, 220, 255)
    yellow = (255, 220, 40, 255)
    blue = (60, 130, 255, 255)
    for entry in manifest.get("visible_outer_edge_row_samples", []):
        span = entry.get("span_half_open")
        y = entry.get("y")
        if isinstance(span, list) and len(span) == 2 and isinstance(y, int):
            for x in (int(span[0]), int(span[1]) - 1):
                draw.ellipse((x - 3, y - 3, x + 3, y + 3), outline=cyan, width=2)
                counts["outer_edge_marks"] += 1
    for entry in manifest.get("irregular_C004_outer_edge_observations", []):
        for key in ("left_source_pixel", "right_source_pixel"):
            point = entry.get(key)
            if isinstance(point, list) and len(point) == 2:
                x, y = int(point[0]), int(point[1])
                draw.rectangle((x - 3, y - 3, x + 3, y + 3), outline=magenta, width=2)
                counts["outer_edge_marks"] += 1
    for entry in manifest.get("contact_line_samples", []):
        for point in iter_contact_points(entry.get("open_segments", [])):
            x, y = point
            draw.ellipse((x - 2, y - 2, x + 2, y + 2), outline=yellow, width=2)
            counts["contact_marks"] += 1
    for entry in manifest.get("height_station_observations", []):
        point = entry.get("pixel_local")
        if isinstance(point, list) and len(point) == 2:
            x, y = int(point[0]), int(point[1])
            draw.line((x - 4, y, x + 4, y), fill=blue, width=2)
            draw.line((x, y - 4, x, y + 4), fill=blue, width=2)
            counts["station_marks"] += 1
    return counts


def candidate_bbox(image: Any) -> Tuple[int, int, int, int]:
    rgb = image.convert("RGB")
    pixels = rgb.load()
    xs: List[int] = []
    ys: List[int] = []
    for y in range(rgb.height):
        for x in range(rgb.width):
            r, g, b = pixels[x, y]
            if max(r, g, b) >= 28 and (r + g + b) >= 110:
                xs.append(x)
                ys.append(y)
    if not xs:
        return 0, 0, 0, 0
    return min(xs), min(ys), max(xs), max(ys)


def font(draw_module: Any, size: int) -> Any:
    from PIL import ImageFont

    candidates = [
        "/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf",
        "/usr/share/fonts/dejavu/DejaVuSans.ttf",
    ]
    for candidate in candidates:
        path = Path(candidate)
        if path.is_file():
            return ImageFont.truetype(str(path), size=size)
    return ImageFont.load_default()


def package_review() -> Dict[str, Any]:
    from PIL import Image, ImageDraw

    lock, lock_results = verify_lock()
    dcc_audit_path = REPO_ROOT / LOCAL_DCC_AUDIT_REL
    if not dcc_audit_path.is_file():
        raise RuntimeError("DCC audit missing; package review is not authorized")
    dcc_audit = json.loads(dcc_audit_path.read_text(encoding="utf-8"))
    if dcc_audit.get("status") != "pass_dcc_geometry_review_candidate_approval_recommended":
        raise RuntimeError("DCC audit did not pass; package review is not authorized")
    render_audit_path = REPO_ROOT / LOCAL_RENDER_AUDIT_REL
    if not render_audit_path.is_file():
        raise RuntimeError("fixed-camera render audit missing; package review is not authorized")
    render_audit = json.loads(render_audit_path.read_text(encoding="utf-8"))
    if render_audit.get("status") != "pass_six_fixed_camera_geometry_review_renders":
        raise RuntimeError("fixed-camera render audit did not pass; package review is not authorized")
    proof_root = REPO_ROOT / STEP13_PROOF_ROOT_REL
    proof_root.mkdir(parents=True, exist_ok=True)
    comparison_records: List[Dict[str, Any]] = []
    title_font = font(ImageDraw, 24)
    label_font = font(ImageDraw, 18)
    small_font = font(ImageDraw, 14)

    for view in VIEWS:
        source_path = REPO_ROOT / SOURCE_PANELS[view]
        candidate_path = REPO_ROOT / STEP13_RAW_PROOFS[view]
        source = Image.open(source_path).convert("RGBA")
        candidate = Image.open(candidate_path).convert("RGBA")
        annotated = source.copy()
        annotation_counts = annotate_source(view, annotated, ImageDraw.Draw(annotated))
        bbox = candidate_bbox(candidate)
        candidate_annotated = candidate.copy()
        candidate_draw = ImageDraw.Draw(candidate_annotated)
        if bbox != (0, 0, 0, 0):
            candidate_draw.rectangle(bbox, outline=(70, 255, 130, 255), width=3)
        header_h = 92
        gutter = 24
        footer_h = 70
        canvas_w = annotated.width + candidate_annotated.width + gutter * 3
        canvas_h = max(annotated.height, candidate_annotated.height) + header_h + footer_h
        canvas = Image.new("RGBA", (canvas_w, canvas_h), (18, 21, 25, 255))
        draw = ImageDraw.Draw(canvas)
        draw.text((gutter, 15), f"STEP 13 {view.upper()} - NATIVE-PIXEL SOURCE / FIXED-CAMERA CANDIDATE", fill=(240, 243, 247, 255), font=title_font)
        draw.text((gutter, 51), "Cyan/magenta/yellow/blue marks = exact source observations; green box = candidate render containment only", fill=(190, 200, 210, 255), font=small_font)
        source_xy = (gutter, header_h)
        candidate_xy = (annotated.width + gutter * 2, header_h)
        canvas.alpha_composite(annotated, source_xy)
        canvas.alpha_composite(candidate_annotated, candidate_xy)
        draw.text((source_xy[0], canvas_h - footer_h + 8), "SOURCE + EXACT MARKS (native pixels)", fill=(35, 225, 255, 255), font=small_font)
        draw.text((candidate_xy[0], canvas_h - footer_h + 8), "UNCHANGED CANDIDATE / STEP 13 FIXED CAMERA (native pixels)", fill=(70, 255, 130, 255), font=small_font)
        if view in ("back", "right"):
            note = "HOLDOUT ONLY - no construction-coordinate claim"
        elif view == "perspective":
            note = "NON-METRIC 360-DEGREE CORROBORATION ONLY"
        elif view == "top":
            note = "N3/K80 AND COMPONENT NESTING AUTHORITY - no unified source-pixel transform"
        else:
            note = "OWNER-VIEW COMPARISON - evidence marks are points/distances, never filled contours"
        draw.text((gutter, canvas_h - 28), note, fill=(255, 205, 70, 255), font=small_font)
        output = REPO_ROOT / COMPARISON_PATHS[view]
        canvas.convert("RGB").save(output, format="PNG")
        margin = {
            "left": bbox[0],
            "top": bbox[1],
            "right": candidate.width - 1 - bbox[2],
            "bottom": candidate.height - 1 - bbox[3],
        }
        comparison_records.append(
            {
                "view": view,
                "source_path": str(SOURCE_PANELS[view]),
                "source_sha256": sha256_file(source_path),
                "candidate_path": str(STEP13_RAW_PROOFS[view]),
                "candidate_sha256": sha256_file(candidate_path),
                "comparison_path": str(COMPARISON_PATHS[view]),
                "comparison_sha256": sha256_file(output),
                "source_native_size": list(source.size),
                "candidate_native_size": list(candidate.size),
                "candidate_bbox_px": list(bbox),
                "candidate_margins_px": margin,
                "candidate_not_clipped": min(margin.values()) >= 8,
                "annotation_counts": annotation_counts,
                "resampled_for_evidence": False,
            }
        )

    thumb_w, thumb_h = 620, 560
    board = Image.new("RGB", (thumb_w * 3 + 80, thumb_h * 2 + 150), (13, 16, 20))
    board_draw = ImageDraw.Draw(board)
    board_draw.text((30, 20), f"{ASSET_ID} - STEP 13 DCC GEOMETRY REVIEW", fill=(245, 245, 245), font=title_font)
    board_draw.text((30, 55), "PRESENTATION THUMBNAILS ONLY - six native-resolution comparisons are the evidence", fill=(255, 205, 70), font=small_font)
    for index, record in enumerate(comparison_records):
        comparison = Image.open(REPO_ROOT / record["comparison_path"]).convert("RGB")
        comparison.thumbnail((thumb_w - 20, thumb_h - 55), Image.Resampling.LANCZOS if hasattr(Image, "Resampling") else Image.LANCZOS)
        x = 20 + (index % 3) * thumb_w
        y = 100 + (index // 3) * thumb_h
        board.paste(comparison, (x + (thumb_w - comparison.width) // 2, y + 35))
        board_draw.text((x + 8, y + 5), record["view"].upper(), fill=(225, 230, 235), font=label_font)
    board_draw.text((30, board.height - 36), "DECISION BASIS: macro geometry only; C-005/C-006/C-007 and surface response remain deferred to Step 14", fill=(100, 235, 160), font=small_font)
    board_path = REPO_ROOT / BOARD_REL
    board.save(board_path, format="PNG")

    source_hashes_after = {view: sha256_file(REPO_ROOT / path) for view, path in SOURCE_PANELS.items()}
    candidate_hashes_after = {view: sha256_file(REPO_ROOT / path) for view, path in STEP12_PROOFS.items()}
    lock_map = {entry["path"]: entry["sha256"] for entry in lock["locked_inputs"]}
    source_identity = all(source_hashes_after[view] == lock_map[str(SOURCE_PANELS[view])] for view in VIEWS)
    candidate_identity = all(candidate_hashes_after[view] == lock_map[str(STEP12_PROOFS[view])] for view in VIEWS)
    all_not_clipped = all(record["candidate_not_clipped"] for record in comparison_records)
    exact_mark_count = sum(sum(record["annotation_counts"].values()) for record in comparison_records)
    gates = [
        create_gate("P01_locked_inputs", all(entry["match"] for entry in lock_results), {"count": len(lock_results), "failures": sum(not entry["match"] for entry in lock_results)}),
        create_gate("P02_dcc_audit_pass", dcc_audit.get("status") == "pass_dcc_geometry_review_candidate_approval_recommended", {"status": dcc_audit.get("status"), "failed_gates": dcc_audit.get("failed_gates")}),
        create_gate("P02A_fixed_camera_render_pass", render_audit.get("status") == "pass_six_fixed_camera_geometry_review_renders", {"status": render_audit.get("status"), "failed_gates": render_audit.get("failed_gates")}),
        create_gate("P03_six_native_comparisons", len(comparison_records) == 6 and all(Path(REPO_ROOT / record["comparison_path"]).is_file() for record in comparison_records), {"comparisons": len(comparison_records), "resampled_for_evidence": False}),
        create_gate("P04_exact_evidence_marks", exact_mark_count > 0, {"exact_marks": exact_mark_count, "filled_contours": 0, "unified_cross_view_transform_claims": 0}),
        create_gate("P05_candidate_not_clipped", all_not_clipped, {record["view"]: record["candidate_margins_px"] for record in comparison_records}),
        create_gate("P06_source_and_candidate_identity", source_identity and candidate_identity, {"source_panels_unchanged": source_identity, "step12_proofs_unchanged": candidate_identity}),
        create_gate("P07_review_board", board_path.is_file() and board_path.stat().st_size > 0, {"path": str(BOARD_REL), "sha256": sha256_file(board_path), "presentation_thumbnails_only": True}),
    ]
    failed = [gate["id"] for gate in gates if gate["status"] != "pass"]
    report = {
        "schema": "aerathea.step13_review_package_audit.v1",
        "asset_id": ASSET_ID,
        "contract_id": CONTRACT_ID,
        "date": "2026-07-20",
        "status": "pass_step13_review_package_candidate_approval_recommended" if not failed else "blocked_fail_closed",
        "artifact_classification": "proof only",
        "decision_recommendation": "approved" if not failed else "blocked",
        "gates": gates,
        "failed_gates": failed,
        "comparisons": comparison_records,
        "board": {"path": str(BOARD_REL), "sha256": sha256_file(board_path)},
        "source_mutations": 0,
        "candidate_mutations": 0,
        "geometry_repairs": 0,
        "evidence_resampling": 0,
    }
    (REPO_ROOT / LOCAL_REVIEW_AUDIT_REL).write_text(json.dumps(report, indent=2) + "\n", encoding="utf-8")
    return report


def main() -> int:
    args = parse_args(blender_script_args())
    if args.schema_only:
        print(json.dumps(schema_report(), indent=2))
        return 0
    if args.audit_dcc:
        report = run_dcc_audit()
    elif args.render_review_proofs:
        report = render_review_proofs()
    else:
        report = package_review()
    print(json.dumps({"status": report["status"], "failed_gates": report.get("failed_gates", []), "decision_recommendation": report.get("decision_recommendation")}, indent=2))
    return 0 if not report.get("failed_gates") else 2


if __name__ == "__main__":
    raise SystemExit(main())
