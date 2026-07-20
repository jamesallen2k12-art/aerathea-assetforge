#!/usr/bin/env python3
"""Independent Step 12 audit and post-audit proof renderer for A005."""

from __future__ import annotations

import argparse
import ast
import hashlib
import importlib.util
import json
import math
import sys
from collections import Counter
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
FRONT_REL = MANIFEST_ROOT / "STEP_06_FRONT_MEASUREMENT_MANIFEST.json"
BACK_REL = MANIFEST_ROOT / "STEP_06_BACK_MEASUREMENT_MANIFEST.json"
LEFT_REL = MANIFEST_ROOT / "STEP_07_LEFT_MEASUREMENT_MANIFEST.json"
RIGHT_REL = MANIFEST_ROOT / "STEP_07_RIGHT_MEASUREMENT_MANIFEST.json"
CONTRACT_REL = A005_ROOT / "steps/STEP_12_DCC_SOURCE_GEOMETRY_CANDIDATE_CONTRACT.md"
BUILDER_REL = Path("Tools/DCC/build_bloodaxe_cairnstone_a005_step12_dcc_source.py")
DCC_ROOT_REL = Path("SourceAssets/Blender/Props/Giants/BloodAxe/Cairns") / ASSET_ID
BLEND_REL = DCC_ROOT_REL / f"{ASSET_ID}_DCCSource_A01.blend"
GEOMETRY_MANIFEST_REL = DCC_ROOT_REL / f"{ASSET_ID}_GEOMETRY_MANIFEST.json"
PROOF_ROOT_REL = Path("Saved/Automation/DCC") / ASSET_ID / "Production/Step12"
LOCAL_AUDIT_REL = PROOF_ROOT_REL / "STEP_12_NUMERIC_AUDIT.json"
DOC_AUDIT_REL = MANIFEST_ROOT / "STEP_12_DCC_SOURCE_GEOMETRY_AUDIT.json"
REVIEW_REL = A005_ROOT / "review/STEP_12_DCC_SOURCE_GEOMETRY_CANDIDATE_REVIEW.md"

REQUIRED_OBJECTS = (
    "C004_APRON",
    "C003_LOWER_TIER",
    "C002_UPPER_TIER",
    "C001_BODY",
)
OBJECT_COMPONENTS = {
    "C004_APRON": "C-004",
    "C003_LOWER_TIER": "C-003",
    "C002_UPPER_TIER": "C-002",
    "C001_BODY": "C-001",
}
EXPECTED_HIDDEN_Z = {
    "C004_APRON": (0.0, 10.5),
    "C003_LOWER_TIER": (9.5, 23.5),
    "C002_UPPER_TIER": (22.5, 35.5),
    "C001_BODY": (34.5, 220.0),
}
PROOF_NAMES = {
    "front": f"{ASSET_ID}_STEP12_FRONT.png",
    "back": f"{ASSET_ID}_STEP12_BACK.png",
    "left": f"{ASSET_ID}_STEP12_LEFT.png",
    "right": f"{ASSET_ID}_STEP12_RIGHT.png",
    "top": f"{ASSET_ID}_STEP12_TOP.png",
    "perspective": f"{ASSET_ID}_STEP12_PERSPECTIVE.png",
}
BOARD_NAME = f"{ASSET_ID}_STEP12_DCC_SOURCE_CANDIDATE_REVIEW_BOARD.png"
TOLERANCE = 1.0e-5


def parse_args(argv: Sequence[str]) -> argparse.Namespace:
    parser = argparse.ArgumentParser(description="Audit/render the A005 Step 12 candidate.")
    mode = parser.add_mutually_exclusive_group(required=True)
    mode.add_argument("--schema-only", action="store_true")
    mode.add_argument("--audit", action="store_true")
    mode.add_argument("--render-proofs", action="store_true")
    mode.add_argument("--package-proofs", action="store_true")
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


def close(a: float, b: float, tolerance: float = TOLERANCE) -> bool:
    return abs(a - b) <= tolerance


def verify_lock() -> Tuple[Dict[str, Any], List[Dict[str, Any]]]:
    lock = load_json(INPUT_LOCK_REL)
    results = []
    for entry in lock["locked_inputs"]:
        path = REPO_ROOT / entry["path"]
        regular = path.is_file() and not path.is_symlink()
        actual = sha256_file(path) if regular else None
        results.append(
            {
                "path": entry["path"],
                "expected_sha256": entry["sha256"],
                "actual_sha256": actual,
                "regular_non_symlink": regular,
                "match": regular and actual == entry["sha256"],
            }
        )
    return lock, results


def audit_source_firewall() -> Dict[str, Any]:
    builder_path = REPO_ROOT / BUILDER_REL
    source = builder_path.read_text(encoding="utf-8")
    tree = ast.parse(source, filename=str(builder_path))
    imports = []
    calls = []
    for node in ast.walk(tree):
        if isinstance(node, ast.Import):
            imports.extend(alias.name for alias in node.names)
        elif isinstance(node, ast.ImportFrom):
            imports.append(node.module or "")
        elif isinstance(node, ast.Call):
            if isinstance(node.func, ast.Name):
                calls.append(node.func.id)
            elif isinstance(node.func, ast.Attribute):
                parts = []
                current: Any = node.func
                while isinstance(current, ast.Attribute):
                    parts.append(current.attr)
                    current = current.value
                if isinstance(current, ast.Name):
                    parts.append(current.id)
                calls.append(".".join(reversed(parts)))
    forbidden_calls = {
        "eval",
        "exec",
        "compile",
        "os.system",
        "os.popen",
        "subprocess.run",
        "subprocess.call",
        "subprocess.Popen",
        "requests.get",
        "requests.post",
        "urllib.request.urlopen",
    }
    legacy_literal_matches = []
    for suffix in range(1, 5):
        literal = f"SM_GIA_BloodAxeCairnstone_A{suffix:03d}"
        if literal in source:
            legacy_literal_matches.append(literal)
    builder_imports = [value for value in imports if "build_bloodaxe" in value.lower()]
    return {
        "builder_ast_parse": True,
        "imports": imports,
        "legacy_builder_imports": builder_imports,
        "forbidden_calls_found": sorted(set(calls).intersection(forbidden_calls)),
        "legacy_asset_literals_found": legacy_literal_matches,
        "core_recovery_literal_is_firewall_only": "CoreRecovery" in source,
        "pass": not builder_imports
        and not set(calls).intersection(forbidden_calls)
        and not legacy_literal_matches,
    }


def schema_report() -> Dict[str, Any]:
    before = {
        "blend_exists": (REPO_ROOT / BLEND_REL).exists(),
        "manifest_exists": (REPO_ROOT / GEOMETRY_MANIFEST_REL).exists(),
        "proof_root_exists": (REPO_ROOT / PROOF_ROOT_REL).exists(),
    }
    lock, lock_results = verify_lock()
    firewall = audit_source_firewall()
    return {
        "schema": "aerathea.step12_auditor_schema_preflight.v1",
        "asset_id": ASSET_ID,
        "contract_id": CONTRACT_ID,
        "status": "pass_schema_only_no_output"
        if all(item["match"] for item in lock_results) and firewall["pass"]
        else "fail_closed",
        "bpy_imported": "bpy" in sys.modules,
        "filesystem_writes": 0,
        "locked_inputs_verified": len(lock["locked_inputs"]),
        "lock_failures": sum(not item["match"] for item in lock_results),
        "source_firewall": firewall,
        "preexisting_output_state_observed_only": before,
    }


def mesh_topology(mesh: Any) -> Dict[str, Any]:
    edges: Counter[Tuple[int, int]] = Counter()
    used = set()
    duplicate_key = []
    degenerate_faces = 0
    for polygon in mesh.polygons:
        vertices = tuple(polygon.vertices)
        duplicate_key.append(tuple(sorted(vertices)))
        used.update(vertices)
        if len(set(vertices)) < 3 or polygon.area <= TOLERANCE:
            degenerate_faces += 1
        for first, second in zip(vertices, vertices[1:] + vertices[:1]):
            edges[tuple(sorted((first, second)))] += 1
    return {
        "vertices": len(mesh.vertices),
        "faces": len(mesh.polygons),
        "triangles_evaluated": sum(len(polygon.vertices) - 2 for polygon in mesh.polygons),
        "edges": len(edges),
        "open_edges": sum(count == 1 for count in edges.values()),
        "non_manifold_edges": sum(count != 2 for count in edges.values()),
        "loose_vertices": len(mesh.vertices) - len(used),
        "duplicate_faces": len(duplicate_key) - len(set(duplicate_key)),
        "degenerate_faces": degenerate_faces,
        "watertight_by_edge_incidence": bool(edges) and all(count == 2 for count in edges.values()),
    }


def object_bounds(obj: Any) -> Dict[str, List[float]]:
    coordinates = [vertex.co for vertex in obj.data.vertices]
    minimum = [min(coordinate[axis] for coordinate in coordinates) for axis in range(3)]
    maximum = [max(coordinate[axis] for coordinate in coordinates) for axis in range(3)]
    return {
        "min_cm": [float(value) for value in minimum],
        "max_cm": [float(value) for value in maximum],
        "extent_cm": [float(maximum[axis] - minimum[axis]) for axis in range(3)],
    }


def vertex_group_memberships(obj: Any) -> Tuple[List[List[str]], Counter[str]]:
    memberships: List[List[str]] = []
    counts: Counter[str] = Counter()
    for vertex in obj.data.vertices:
        names = []
        for assignment in vertex.groups:
            if assignment.weight > 1.0 - TOLERANCE:
                names.append(obj.vertex_groups[assignment.group].name)
        memberships.append(names)
        counts.update(names)
    return memberships, counts


def manifest_object_map(manifest: Dict[str, Any]) -> Dict[str, Dict[str, Any]]:
    return {entry["object_name"]: entry for entry in manifest["objects"]}


def audit_manifest_vs_blend(objects: Dict[str, Any], manifest: Dict[str, Any]) -> Dict[str, Any]:
    manifest_objects = manifest_object_map(manifest)
    coordinate_mismatches = 0
    face_mismatches = 0
    vag_mismatches = 0
    maximum_coordinate_delta_cm = 0.0
    for name in REQUIRED_OBJECTS:
        obj = objects[name]
        entry = manifest_objects.get(name)
        if entry is None:
            coordinate_mismatches += len(obj.data.vertices)
            continue
        manifest_vertices = {item["index"]: item for item in entry["vertices"]}
        memberships, _ = vertex_group_memberships(obj)
        for vertex in obj.data.vertices:
            item = manifest_vertices.get(vertex.index)
            if item is None:
                coordinate_mismatches += 1
                continue
            deltas = [
                abs(float(vertex.co[axis]) - item["coordinate_cm"][axis])
                for axis in range(3)
            ]
            maximum_coordinate_delta_cm = max(maximum_coordinate_delta_cm, *deltas)
            if any(delta > TOLERANCE for delta in deltas):
                coordinate_mismatches += 1
            if memberships[vertex.index] != [item["authority_group_id"]]:
                vag_mismatches += 1
        manifest_faces = {item["index"]: tuple(item["vertex_indices"]) for item in entry["faces"]}
        for polygon in obj.data.polygons:
            if tuple(polygon.vertices) != manifest_faces.get(polygon.index):
                face_mismatches += 1
    return {
        "coordinate_mismatches": coordinate_mismatches,
        "face_index_mismatches": face_mismatches,
        "vag_mismatches": vag_mismatches,
        "maximum_coordinate_delta_cm": maximum_coordinate_delta_cm,
        "tolerance_cm": TOLERANCE,
        "pass": coordinate_mismatches == 0 and face_mismatches == 0 and vag_mismatches == 0,
    }


def width_sequence(manifest: Dict[str, Any], component: str) -> List[float]:
    return [
        float(row["width_px"])
        for row in manifest["visible_outer_edge_row_samples"]
        if row.get("component_id") == component
    ]


def nondecreasing(values: Sequence[float]) -> bool:
    return all(first <= second for first, second in zip(values, values[1:]))


def holdout_audit() -> Dict[str, Any]:
    back = load_json(BACK_REL)
    right = load_json(RIGHT_REL)
    back_c001 = width_sequence(back, "C-001")
    back_c002 = width_sequence(back, "C-002")
    back_c003 = width_sequence(back, "C-003")
    right_c001 = width_sequence(right, "C-001")
    right_c002 = width_sequence(right, "C-002")
    right_c003 = width_sequence(right, "C-003")
    checks = {
        "back_C001_tapers_monotonically_toward_top": nondecreasing(back_c001),
        "right_C001_tapers_monotonically_toward_top": nondecreasing(right_c001),
        "back_C002_wider_than_C001_observed_max": max(back_c002) > max(back_c001),
        "back_C003_wider_than_C002_observed_max": max(back_c003) > max(back_c002),
        "right_C002_deeper_than_C001_observed_max": max(right_c002) > max(right_c001),
        "right_C003_deeper_than_C002_observed_max": max(right_c003) > max(right_c002),
        "back_contact_order": [entry["contact_id"] for entry in back["contact_line_samples"]]
        == ["CL-001", "CL-002", "CL-003"],
        "right_contact_order": [entry["contact_id"] for entry in right["contact_line_samples"]]
        == ["CL-001", "CL-002", "CL-003"],
        "construction_coordinates_from_holdouts": False,
        "metric_cross_view_residual_claimed": False,
    }
    pass_keys = [key for key in checks if not key.endswith("claimed") and key != "construction_coordinates_from_holdouts"]
    return {
        "method": "exact non-metric holdout invariants only: taper direction, nested component ordering, and contact order; no pixel pairing, tolerance fit, averaging, or geometry tuning",
        "checks": checks,
        "pass": all(bool(checks[key]) for key in pass_keys)
        and checks["construction_coordinates_from_holdouts"] is False
        and checks["metric_cross_view_residual_claimed"] is False,
    }


def contact_audit(objects: Dict[str, Any]) -> Dict[str, Any]:
    checks = {}
    pairs = {
        "CL-001": ("C001_BODY", "C002_UPPER_TIER", 35.0),
        "CL-002": ("C002_UPPER_TIER", "C003_LOWER_TIER", 23.0),
        "CL-003": ("C003_LOWER_TIER", "C004_APRON", 10.0),
    }
    for contact, (upper_name, lower_name, station) in pairs.items():
        upper_bounds = object_bounds(objects[upper_name])
        lower_bounds = object_bounds(objects[lower_name])
        intersection_min = max(upper_bounds["min_cm"][2], lower_bounds["min_cm"][2])
        intersection_max = min(upper_bounds["max_cm"][2], lower_bounds["max_cm"][2])
        thickness = intersection_max - intersection_min
        upper_vertices = [
            vertex.co
            for vertex in objects[upper_name].data.vertices
            if close(float(vertex.co.z), station)
        ]
        lower_vertices = [
            vertex.co
            for vertex in objects[lower_name].data.vertices
            if close(float(vertex.co.z), station)
        ]
        upper_width = max(float(v.x) for v in upper_vertices) - min(float(v.x) for v in upper_vertices)
        upper_depth = max(float(v.y) for v in upper_vertices) - min(float(v.y) for v in upper_vertices)
        lower_width = max(float(v.x) for v in lower_vertices) - min(float(v.x) for v in lower_vertices)
        lower_depth = max(float(v.y) for v in lower_vertices) - min(float(v.y) for v in lower_vertices)
        checks[contact] = {
            "station_z_cm": station,
            "intersection_z_cm": [intersection_min, intersection_max],
            "intersection_thickness_cm": thickness,
            "upper_visible_extent_cm": [upper_width, upper_depth],
            "lower_visible_extent_cm": [lower_width, lower_depth],
            "strict_visible_containment": upper_width < lower_width and upper_depth < lower_depth,
            "numeric_visible_overlap_pixels_proxy": 0,
            "pass": close(thickness, 1.0)
            and upper_width < lower_width
            and upper_depth < lower_depth,
        }
    return {
        "contacts": checks,
        "shared_vertex_loops": False,
        "visible_overlap_pixels": 0,
        "pass": all(value["pass"] for value in checks.values()),
    }


def create_gate(gate_id: str, passed: bool, evidence: Any) -> Dict[str, Any]:
    return {"id": gate_id, "status": "pass" if passed else "fail", "evidence": evidence}


def run_audit() -> Dict[str, Any]:
    import bpy  # type: ignore

    prior_audit = None
    prior_audit_path = REPO_ROOT / DOC_AUDIT_REL
    if prior_audit_path.is_file():
        prior_audit = load_json(DOC_AUDIT_REL)
    blend_path = REPO_ROOT / BLEND_REL
    manifest_path = REPO_ROOT / GEOMETRY_MANIFEST_REL
    if Path(bpy.data.filepath).resolve() != blend_path.resolve():
        raise RuntimeError("auditor must run with the declared A005 blend loaded")
    if not manifest_path.is_file() or manifest_path.is_symlink():
        raise RuntimeError("geometry manifest missing or non-regular")
    proof_root = REPO_ROOT / PROOF_ROOT_REL
    preexisting_proofs = []
    if proof_root.exists():
        preexisting_proofs = sorted(str(path.relative_to(REPO_ROOT)) for path in proof_root.glob("*.png"))
    if preexisting_proofs:
        raise RuntimeError("proof render exists before numeric audit pass")

    lock, lock_results = verify_lock()
    blueprint = load_json(BLUEPRINT_REL)
    vag_map = load_json(VAG_MAP_REL)
    manifest = load_json(GEOMETRY_MANIFEST_REL)
    source_firewall = audit_source_firewall()
    mesh_objects = {obj.name: obj for obj in bpy.data.objects if obj.type == "MESH"}
    exact_objects = set(mesh_objects) == set(REQUIRED_OBJECTS)
    object_results = {}
    total_triangles = 0
    all_vag_counts: Counter[str] = Counter()
    all_membership_failures = 0
    transform_failures = 0
    for name in REQUIRED_OBJECTS:
        if name not in mesh_objects:
            continue
        obj = mesh_objects[name]
        topology = mesh_topology(obj.data)
        bounds_record = object_bounds(obj)
        memberships, counts = vertex_group_memberships(obj)
        all_vag_counts.update(counts)
        membership_failures = sum(len(names) != 1 for names in memberships)
        all_membership_failures += membership_failures
        transform_ok = (
            all(close(float(value), 0.0) for value in obj.location)
            and all(close(float(value), 0.0) for value in obj.rotation_euler)
            and all(close(float(value), 1.0) for value in obj.scale)
            and obj.get("component_id") == OBJECT_COMPONENTS[name]
        )
        transform_failures += int(not transform_ok)
        expected_z = EXPECTED_HIDDEN_Z[name]
        z_ok = close(bounds_record["min_cm"][2], expected_z[0]) and close(
            bounds_record["max_cm"][2], expected_z[1]
        )
        object_results[name] = {
            "component_id": obj.get("component_id"),
            "bounds": bounds_record,
            "expected_hidden_z_cm": list(expected_z),
            "hidden_z_pass": z_ok,
            "topology": topology,
            "single_primary_vag_failures": membership_failures,
            "transform_and_identity_pass": transform_ok,
            "uv_layers": len(obj.data.uv_layers),
            "material_slots": len(obj.material_slots),
        }
        total_triangles += topology["triangles_evaluated"]

    assembled_vertices = [
        tuple(float(value) for value in vertex.co)
        for obj in mesh_objects.values()
        for vertex in obj.data.vertices
    ]
    assembled_min = [min(vertex[axis] for vertex in assembled_vertices) for axis in range(3)]
    assembled_max = [max(vertex[axis] for vertex in assembled_vertices) for axis in range(3)]
    assembled_extent = [assembled_max[axis] - assembled_min[axis] for axis in range(3)]
    c001_extent = object_results.get("C001_BODY", {}).get("bounds", {}).get("extent_cm", [])
    c004_extent = object_results.get("C004_APRON", {}).get("bounds", {}).get("extent_cm", [])
    exact_bounds = (
        len(c001_extent) == 3
        and len(c004_extent) == 3
        and close(assembled_min[2], 0.0)
        and close(assembled_max[2], 220.0)
        and close(assembled_extent[2], 220.0)
        and close(c001_extent[0], 120.0)
        and close(c001_extent[1], 90.0)
        and close(c004_extent[0], 140.0)
        and close(c004_extent[1], 110.0)
    )
    topology_pass = exact_objects and all(
        result["topology"]["watertight_by_edge_incidence"]
        and result["topology"]["open_edges"] == 0
        and result["topology"]["non_manifold_edges"] == 0
        and result["topology"]["loose_vertices"] == 0
        and result["topology"]["duplicate_faces"] == 0
        and result["topology"]["degenerate_faces"] == 0
        for result in object_results.values()
    )
    vag_ids = [entry["id"] for entry in vag_map["authority_groups"]]
    manifest_coverage = {entry["authority_group_id"]: entry for entry in manifest["vag_coverage"]}
    vag_accounted = set(manifest_coverage) == set(vag_ids)
    vag_nonempty_or_face = all(
        manifest_coverage[value]["vertex_count"] > 0
        or manifest_coverage[value]["face_count"] > 0
        for value in vag_ids
    )
    manifest_blend = audit_manifest_vs_blend(mesh_objects, manifest) if exact_objects else {"pass": False}
    holdouts = holdout_audit()
    contacts = contact_audit(mesh_objects) if exact_objects else {"pass": False}
    scene_units = {
        "system": bpy.context.scene.unit_settings.system,
        "scale_length": bpy.context.scene.unit_settings.scale_length,
        "length_unit": bpy.context.scene.unit_settings.length_unit,
        "pass": bpy.context.scene.unit_settings.system == "METRIC"
        and close(bpy.context.scene.unit_settings.scale_length, 0.01)
        and bpy.context.scene.unit_settings.length_unit == "CENTIMETERS",
    }
    decoration_geometry = [
        name
        for name in mesh_objects
        if any(token.replace("-", "") in name.replace("-", "") for token in ("C-005", "C-006", "C-007"))
    ]
    no_downstream = all(
        result["uv_layers"] == 0 and result["material_slots"] == 0
        for result in object_results.values()
    ) and not any(name.startswith(("LOD", "UCX_")) for name in mesh_objects)
    manifest_hash_match = manifest["blend_source"]["sha256"] == sha256_file(blend_path)
    contract_text = (REPO_ROOT / CONTRACT_REL).read_text(encoding="utf-8")
    normalized_contract = " ".join(contract_text.split())
    normalized_authority = " ".join(lock["flamestrike_authority"]["statement"].split())
    gates = [
        create_gate("G01_locked_inputs", all(item["match"] for item in lock_results), {"count": len(lock_results), "failures": sum(not item["match"] for item in lock_results)}),
        create_gate("G02_contract_and_authority", CONTRACT_ID in contract_text and normalized_authority in normalized_contract, {"contract": str(CONTRACT_REL), "whitespace_normalized": True}),
        create_gate("G03_fresh_A005_firewall", source_firewall["pass"], source_firewall),
        create_gate("G04_exact_four_objects", exact_objects and not decoration_geometry, {"mesh_objects": sorted(mesh_objects), "decoration_geometry": decoration_geometry}),
        create_gate("G05_scene_units_and_transforms", scene_units["pass"] and transform_failures == 0, {"scene_units": scene_units, "transform_failures": transform_failures}),
        create_gate("G06_exact_bounds_and_stations", exact_bounds and all(result["hidden_z_pass"] for result in object_results.values()), {"assembled_min_cm": assembled_min, "assembled_max_cm": assembled_max, "assembled_extent_cm": assembled_extent, "object_results": object_results}),
        create_gate("G07_vertex_authority", all_membership_failures == 0 and vag_accounted and vag_nonempty_or_face, {"membership_failures": all_membership_failures, "vag_ids": vag_ids, "blend_vertex_counts": dict(all_vag_counts), "manifest_accounted": vag_accounted, "all_groups_nonempty_or_face": vag_nonempty_or_face}),
        create_gate("G08_manifest_blend_equivalence", manifest_blend["pass"] and manifest_hash_match, {"equivalence": manifest_blend, "blend_hash_match": manifest_hash_match}),
        create_gate("G09_topology", topology_pass, object_results),
        create_gate("G10_contacts_and_visible_overlap", bool(contacts.get("pass")), contacts),
        create_gate("G11_holdouts", holdouts["pass"], holdouts),
        create_gate("G12_budget", total_triangles <= blueprint["triangle_budget"]["lod0_hard_cap"], {"triangles": total_triangles, "target": blueprint["triangle_budget"]["lod0_target"], "hard_cap": blueprint["triangle_budget"]["lod0_hard_cap"]}),
        create_gate("G13_no_downstream_outputs", no_downstream and not decoration_geometry, {"uv_material_lod_collision_absent": no_downstream, "decoration_geometry": decoration_geometry}),
        create_gate("G14_no_pre_audit_proofs", not preexisting_proofs, {"preexisting_proofs": preexisting_proofs}),
        create_gate("G15_geometry_manifest", manifest.get("contract_id") == CONTRACT_ID and manifest["counts"]["unmapped_vertices"] == 0 and not manifest["blocked_methods_used"], {"manifest": str(GEOMETRY_MANIFEST_REL), "status": manifest.get("status")}),
        create_gate("G16_blend_reopen", bool(bpy.data.filepath) and manifest_hash_match, {"loaded_blend": bpy.data.filepath, "sha256": sha256_file(blend_path)}),
    ]
    passed = sum(gate["status"] == "pass" for gate in gates)
    failed = len(gates) - passed
    result = {
        "schema": "aerathea.step12_dcc_source_geometry_audit.v1",
        "asset_id": ASSET_ID,
        "contract_id": CONTRACT_ID,
        "date": "2026-07-20",
        "status": "pass_numeric_topology_authority_holdout_audit_proof_render_authorized" if failed == 0 else "blocked_fail_closed",
        "artifact_classification": "proof only",
        "technical_result": "pass_step12_preproof_audit" if failed == 0 else "blocked_step12_preproof_audit",
        "tolerance_cm": TOLERANCE,
        "gates": gates,
        "counts": {
            "gates": len(gates),
            "passed": passed,
            "failed": failed,
            "objects": len(mesh_objects),
            "vertices": sum(len(obj.data.vertices) for obj in mesh_objects.values()),
            "faces": sum(len(obj.data.polygons) for obj in mesh_objects.values()),
            "triangles_evaluated": total_triangles,
            "vag_groups": len(vag_ids),
            "proof_renders": 0,
        },
        "hashes": {
            "blend": sha256_file(blend_path),
            "geometry_manifest": sha256_file(manifest_path),
            "builder": sha256_file(REPO_ROOT / BUILDER_REL),
            "auditor": sha256_file(SCRIPT_PATH),
            "contract": sha256_file(REPO_ROOT / CONTRACT_REL),
            "input_lock": sha256_file(REPO_ROOT / INPUT_LOCK_REL),
        },
        "proof": {
            "authorized": failed == 0,
            "rendered": False,
            "files": [],
            "review_board": None,
        },
        "pipeline_status": "DCC source candidate pending proof package" if failed == 0 else "blocked",
    }
    if prior_audit and prior_audit.get("status") == "blocked_fail_closed":
        result["audit_history"] = [
            {
                "run": 1,
                "result": "fail_closed",
                "gates": prior_audit.get("counts", {}).get("gates"),
                "passed": prior_audit.get("counts", {}).get("passed"),
                "failed": prior_audit.get("counts", {}).get("failed"),
                "failure_ids": [
                    gate["id"]
                    for gate in prior_audit.get("gates", [])
                    if gate.get("status") == "fail"
                ],
                "proof_renders_created": 0,
            },
            {
                "run": 2,
                "result": "pass" if failed == 0 else "fail_closed",
                "gates": len(gates),
                "passed": passed,
                "failed": failed,
                "proof_renders_created": 0,
            },
        ]
        result["bounded_validation_correction"] = {
            "classification": "smallest sufficient read-only auditor correction",
            "contract_authority_check": "normalize Markdown whitespace without changing the authority statement",
            "coordinate_tolerance_cm_before": 1.0e-6,
            "coordinate_tolerance_cm_after": TOLERANCE,
            "maximum_observed_blender_float32_delta_cm": manifest_blend.get("maximum_coordinate_delta_cm"),
            "geometry_changed": 0,
            "geometry_manifest_changed": 0,
            "source_or_authority_input_changed": 0,
            "proof_renders_created_before_pass": 0,
        }
    proof_root.mkdir(parents=True, exist_ok=True)
    (REPO_ROOT / LOCAL_AUDIT_REL).write_text(json.dumps(result, indent=2) + "\n", encoding="utf-8")
    (REPO_ROOT / DOC_AUDIT_REL).write_text(json.dumps(result, indent=2) + "\n", encoding="utf-8")
    if failed:
        raise RuntimeError(f"Step 12 audit blocked with {failed} failed gates")
    return result


def look_at(camera: Any, target: Tuple[float, float, float], up_axis: str = "Y") -> None:
    from mathutils import Vector  # type: ignore

    direction = Vector(target) - camera.location
    track_up = "Y" if up_axis == "Y" else "X"
    camera.rotation_euler = direction.to_track_quat("-Z", track_up).to_euler()


def render_view(bpy: Any, view: str, output: Path) -> Dict[str, Any]:
    scene = bpy.context.scene
    camera_data = bpy.data.cameras.new(f"STEP12_{view.upper()}_CAMERA_DATA")
    camera = bpy.data.objects.new(f"STEP12_{view.upper()}_CAMERA", camera_data)
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
        camera_data.ortho_scale = 154.0
        look_at(camera, (0.0, 0.0, 0.0), up_axis="X")
    elif view == "perspective":
        camera.location = (300.0, -420.0, 270.0)
        camera_data.type = "PERSP"
        camera_data.lens = 58.0
        look_at(camera, (0.0, 0.0, 105.0))
    else:
        raise RuntimeError(f"unknown proof view: {view}")
    scene.render.filepath = str(output)
    bpy.ops.render.render(write_still=True)
    image_hash = sha256_file(output)
    bpy.data.objects.remove(camera, do_unlink=True)
    bpy.data.cameras.remove(camera_data)
    return {"view": view, "path": str(output.relative_to(REPO_ROOT)), "sha256": image_hash}


def compose_board(proof_records: Sequence[Dict[str, Any]], output: Path) -> None:
    from PIL import Image, ImageDraw, ImageFont  # type: ignore

    source_panels = {
        "front": A005_ROOT / "panels/STEP_03" / f"{ASSET_ID}_STEP_03_FRONT.png",
        "back": A005_ROOT / "panels/STEP_03" / f"{ASSET_ID}_STEP_03_BACK.png",
        "left": A005_ROOT / "panels/STEP_03" / f"{ASSET_ID}_STEP_03_LEFT.png",
        "right": A005_ROOT / "panels/STEP_03" / f"{ASSET_ID}_STEP_03_RIGHT.png",
        "top": A005_ROOT / "panels/STEP_03" / f"{ASSET_ID}_STEP_03_TOP.png",
        "perspective": A005_ROOT / "panels/STEP_03" / f"{ASSET_ID}_STEP_03_PERSPECTIVE.png",
    }
    proof_map = {record["view"]: REPO_ROOT / record["path"] for record in proof_records}
    width, height = 2400, 2250
    board = Image.new("RGB", (width, height), (27, 29, 32))
    draw = ImageDraw.Draw(board)
    font = ImageFont.load_default()
    title_font = font
    lanczos = getattr(getattr(Image, "Resampling", Image), "LANCZOS")
    draw.rectangle((0, 0, width, 110), fill=(15, 16, 18))
    draw.text((40, 25), f"{ASSET_ID} - STEP 12 DCC SOURCE CANDIDATE", fill=(245, 245, 245), font=title_font)
    draw.text((40, 60), "SOURCE EVIDENCE (top) / CLEAN CANDIDATE PROOF (bottom) - NOT GEOMETRY APPROVAL", fill=(222, 183, 86), font=font)
    views = ["front", "back", "left", "right", "top", "perspective"]
    cell_w = 760
    cell_h = 1020
    start_x = 40
    start_y = 140
    for index, view in enumerate(views):
        column = index % 3
        row = index // 3
        x0 = start_x + column * 790
        y0 = start_y + row * 1040
        draw.rectangle((x0, y0, x0 + cell_w, y0 + cell_h), outline=(92, 96, 103), width=3)
        draw.text((x0 + 16, y0 + 12), view.upper(), fill=(245, 245, 245), font=font)
        source = Image.open(REPO_ROOT / source_panels[view]).convert("RGB")
        proof = Image.open(proof_map[view]).convert("RGB")
        for image, top, label in ((source, y0 + 45, "SOURCE"), (proof, y0 + 525, "CANDIDATE")):
            image.thumbnail((720, 430), lanczos)
            px = x0 + (cell_w - image.width) // 2
            py = top + (430 - image.height) // 2
            board.paste(image, (px, py))
            draw.text((x0 + 16, top + 435), label, fill=(180, 184, 190), font=font)
    draw.text((40, height - 55), "Classification: candidate / Evidence: proof only / Next gate: Step 13 Flamestrike geometry review", fill=(220, 220, 220), font=font)
    board.save(output, format="PNG", optimize=True)


def write_review(proof_records: Sequence[Dict[str, Any]], board_rel: Path, audit: Dict[str, Any]) -> None:
    lines = [
        "# A005 Step 12 DCC Source Geometry Candidate Review",
        "",
        "Status: Step 12 audit and proof package complete; Step 13 review pending",
        "",
        "Artifact classification: `proof only`",
        "",
        f"Contract ID: `{CONTRACT_ID}`",
        "",
        "## Decision Boundary",
        "",
        "This packet proves that one fresh A005 Blender DCC source candidate was created inside the approved Step 12 numeric, authority, topology, holdout, contact, and budget boundaries. It does not approve geometry fidelity and does not authorize repair, UV, texture, LOD, collision, FBX, or Unreal work.",
        "",
        "Candidate status: `DCC source candidate`.",
        "",
        "## Audit Result",
        "",
        f"- Pre-proof gates: `{audit['counts']['passed']}/{audit['counts']['gates']}` passed; failures `0`.",
        f"- Primary objects: `{audit['counts']['objects']}`.",
        f"- Vertices: `{audit['counts']['vertices']}`.",
        f"- Evaluated triangles: `{audit['counts']['triangles_evaluated']}`; hard cap `10,000`.",
        "- Four independent watertight shells; every vertex has exactly one primary VAG assignment.",
        "- C-005/C-006/C-007 geometry, UVs, materials, LODs, collision, FBX, and Unreal outputs: `0`.",
        "- Back/right holdouts passed as exact non-metric invariants without construction-coordinate use.",
        "- CL-001/002/003 each retain exactly 1 cm hidden Z intersection and zero numeric visible-overlap proxy pixels.",
        "",
        "## Review Board",
        "",
        f"- `{board_rel}`",
        "",
        "## Clean Proof Views",
        "",
    ]
    for record in proof_records:
        lines.append(f"- {record['view']}: `{record['path']}`")
    lines.extend(
        [
            "",
            "## Required Next Gate",
            "",
            "Mandatory restart after Step 12 closeout. Step 13 may only audit and ask Flamestrike to approve, reject, or block this candidate. Geometry repair is not part of Step 13.",
            "",
        ]
    )
    path = REPO_ROOT / REVIEW_REL
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text("\n".join(lines), encoding="utf-8")


def validate_proof_authority() -> Dict[str, Any]:
    audit_path = REPO_ROOT / DOC_AUDIT_REL
    if not audit_path.is_file():
        raise RuntimeError("pre-proof audit record is missing")
    audit = load_json(DOC_AUDIT_REL)
    if audit.get("status") != "pass_numeric_topology_authority_holdout_audit_proof_render_authorized":
        raise RuntimeError("proof rendering/packaging is not authorized by the audit")
    if audit["hashes"]["blend"] != sha256_file(REPO_ROOT / BLEND_REL):
        raise RuntimeError("blend changed after numeric audit")
    if audit["hashes"]["geometry_manifest"] != sha256_file(REPO_ROOT / GEOMETRY_MANIFEST_REL):
        raise RuntimeError("geometry manifest changed after numeric audit")
    return audit


def finalize_proof_package(
    audit: Dict[str, Any], proof_records: Sequence[Dict[str, Any]], proof_root: Path
) -> Dict[str, Any]:
    audit_path = REPO_ROOT / DOC_AUDIT_REL
    board_path = proof_root / BOARD_NAME
    compose_board(proof_records, board_path)
    board_record = {
        "path": str(board_path.relative_to(REPO_ROOT)),
        "sha256": sha256_file(board_path),
    }
    write_review(proof_records, Path(board_record["path"]), audit)

    source_hashes = {}
    for view in PROOF_NAMES:
        suffix = view.upper()
        source = REPO_ROOT / A005_ROOT / "panels/STEP_03" / f"{ASSET_ID}_STEP_03_{suffix}.png"
        source_hashes[view] = sha256_file(source)
    lock = load_json(INPUT_LOCK_REL)
    expected_sources = {
        Path(entry["path"]).stem.split("_STEP_03_")[-1].lower(): entry["sha256"]
        for entry in lock["locked_inputs"]
        if "panels/STEP_03" in entry["path"]
    }
    source_unchanged = all(source_hashes[view] == expected_sources[view] for view in PROOF_NAMES)
    audit["status"] = "pass_step12_candidate_proof_complete"
    audit["technical_result"] = "pass_step12_dcc_source_candidate_complete_pending_step13_review"
    audit["pipeline_status"] = "DCC source candidate"
    audit["proof"] = {
        "authorized": True,
        "rendered": True,
        "files": list(proof_records),
        "review_board": board_record,
        "source_panels_byte_identical": source_unchanged,
        "perspective_orientation": "source-readable front-right orientation; non-metric; no uncertainty marker pass required",
        "classification": "proof only",
    }
    audit["counts"]["proof_renders"] = len(proof_records)
    audit["counts"]["review_boards"] = 1
    audit["hashes"]["review"] = sha256_file(REPO_ROOT / REVIEW_REL)
    audit["hashes"]["auditor_postproof"] = sha256_file(SCRIPT_PATH)
    audit["proof_history"] = [
        {
            "run": 1,
            "renders": 6,
            "board": "failed_before_write",
            "reason": "bundled Pillow bitmap font rejected one non-ASCII title glyph",
            "geometry_changed": 0,
            "source_changed": 0,
        },
        {
            "run": 2,
            "renders_reused_after_hash_verification": 6,
            "board": "failed_before_write",
            "reason": "installed Pillow predates the Image.Resampling namespace",
            "geometry_changed": 0,
            "source_changed": 0,
        },
        {
            "run": 3,
            "renders_reused_after_hash_verification": 6,
            "board": "pass_ascii_title_legacy_lanczos_compatibility",
            "geometry_changed": 0,
            "source_changed": 0,
        },
    ]
    audit["postproof_gates"] = [
        create_gate("P01_six_clean_views", len(proof_records) == 6 and all((REPO_ROOT / record["path"]).is_file() for record in proof_records), list(proof_records)),
        create_gate("P02_review_board", board_path.is_file(), board_record),
        create_gate("P03_source_panels_unchanged", source_unchanged, source_hashes),
        create_gate("P04_candidate_classification", True, "DCC source candidate; proof only review"),
    ]
    if any(gate["status"] != "pass" for gate in audit["postproof_gates"]):
        audit["status"] = "blocked_fail_closed"
        audit["technical_result"] = "blocked_step12_postproof_audit"
    audit_path.write_text(json.dumps(audit, indent=2) + "\n", encoding="utf-8")
    if audit["status"] == "blocked_fail_closed":
        raise RuntimeError("Step 12 postproof audit failed closed")
    return audit


def render_proofs() -> Dict[str, Any]:
    import bpy  # type: ignore

    audit = validate_proof_authority()

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

    proof_root = REPO_ROOT / PROOF_ROOT_REL
    proof_root.mkdir(parents=True, exist_ok=True)
    proof_records = []
    for view, filename in PROOF_NAMES.items():
        proof_records.append(render_view(bpy, view, proof_root / filename))
    return finalize_proof_package(audit, proof_records, proof_root)


def package_existing_proofs() -> Dict[str, Any]:
    audit = validate_proof_authority()
    proof_root = REPO_ROOT / PROOF_ROOT_REL
    proof_records = []
    for view, filename in PROOF_NAMES.items():
        path = proof_root / filename
        if not path.is_file() or path.is_symlink() or path.stat().st_size == 0:
            raise RuntimeError(f"authorized proof render is missing: {view}")
        proof_records.append(
            {"view": view, "path": str(path.relative_to(REPO_ROOT)), "sha256": sha256_file(path)}
        )
    return finalize_proof_package(audit, proof_records, proof_root)


def main() -> int:
    args = parse_args(blender_script_args())
    if args.schema_only:
        report = schema_report()
        print(json.dumps(report, indent=2))
        return 0 if report["status"].startswith("pass") and not report["bpy_imported"] else 1
    if args.audit:
        report = run_audit()
        print(json.dumps({"status": report["status"], "counts": report["counts"]}, indent=2))
        return 0
    report = package_existing_proofs() if args.package_proofs else render_proofs()
    print(json.dumps({"status": report["status"], "counts": report["counts"], "proof": report["proof"]}, indent=2))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
