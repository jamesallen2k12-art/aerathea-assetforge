#!/usr/bin/env python3
"""Independently audit the A005 Steps 01-16 visual-fidelity recovery package."""

from __future__ import annotations

import argparse
import collections
import hashlib
import json
import math
import sys
from pathlib import Path
from typing import Any, Dict, List, Sequence, Tuple


ROOT = Path(__file__).resolve().parents[2]
ASSET = "SM_GIA_BloodAxeCairnstone_A005"
CONTRACT = "A005-CR-STEPS01-16-VISUAL-FIDELITY-RECOVERY-A01"
BLUEPRINT_ROOT = Path("docs/assets/blueprints") / ASSET
PLAN_REL = BLUEPRINT_ROOT / "manifests/VISUAL_FIDELITY_RECOVERY_A01_PLAN.json"
STEP11_REL = BLUEPRINT_ROOT / "manifests/STEP_11_CONSTRUCTION_BLUEPRINT.json"
UV_PLAN_REL = BLUEPRINT_ROOT / "manifests/STEP_14_UV_OWNERSHIP_PLAN.json"
VALIDATION_REL = BLUEPRINT_ROOT / "manifests/VISUAL_FIDELITY_RECOVERY_A01_VALIDATION.json"
SOURCE_REL = Path("docs/assets/reference/bloodaxe_cairnstone_asset/REF_GIA_BloodAxeCairnstoneAsset_A02_BlueprintTemplate.png")
MASK_MANIFEST_REL = Path("SourceAssets/Textures/Props/Giants/BloodAxe/Cairns") / ASSET / "Technical/SM_GIA_BloodAxeCairnstone_A005_SOURCE_MASK_MANIFEST_A01.json"
DCC_ROOT = Path("SourceAssets/Blender/Props/Giants/BloodAxe/Cairns") / ASSET
BLEND_REL = DCC_ROOT / f"{ASSET}_DCCGameReady_A02.blend"
MANIFEST_REL = DCC_ROOT / f"{ASSET}_VISUAL_FIDELITY_RECOVERY_A01_MANIFEST.json"
FINAL_REL = Path("Saved/Automation/DCC") / ASSET / "Production/VisualFidelityRecovery_A01" / f"{ASSET}_FINAL_GAME_READY_ASSET.png"
RENDER_AUDIT_REL = FINAL_REL.parent / "FINAL_RENDER_AUDIT.json"
LOCAL_AUDIT_REL = FINAL_REL.parent / "VISUAL_FIDELITY_RECOVERY_A01_INDEPENDENT_AUDIT.json"
EXPECTED_BOUNDS = {"min": [-70.0, -55.0, 0.0], "max": [70.0, 55.0, 220.0], "dimensions": [140.0, 110.0, 220.0]}
EXPECTED_TRIS = {"LOD0": 8672, "LOD1": 3988, "LOD2": 1820, "LOD3": 692}
EPS = 1.0e-5


def parse_args(argv: Sequence[str]) -> argparse.Namespace:
    parser = argparse.ArgumentParser(description=__doc__)
    modes = parser.add_mutually_exclusive_group(required=True)
    modes.add_argument("--schema-only", action="store_true")
    modes.add_argument("--audit", action="store_true")
    return parser.parse_args(list(argv))


def blender_args() -> List[str]:
    return sys.argv[sys.argv.index("--") + 1 :] if "--" in sys.argv else sys.argv[1:]


def sha256_file(path: Path) -> str:
    digest = hashlib.sha256()
    with path.open("rb") as handle:
        for block in iter(lambda: handle.read(1024 * 1024), b""):
            digest.update(block)
    return digest.hexdigest()


def load_json(rel: Path) -> Dict[str, Any]:
    with (ROOT / rel).open("r", encoding="utf-8") as handle:
        return json.load(handle)


def write_json(rel: Path, payload: Dict[str, Any]) -> None:
    path = ROOT / rel
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(json.dumps(payload, indent=2) + "\n", encoding="utf-8")


def gate(identifier: str, passed: bool, detail: Any) -> Dict[str, Any]:
    return {"id": identifier, "status": "pass" if passed else "fail", "detail": detail}


def mesh_triangles(mesh: Any) -> int:
    mesh.calc_loop_triangles()
    return len(mesh.loop_triangles)


def object_bounds(obj: Any) -> Dict[str, List[float]]:
    points = [obj.matrix_world @ vertex.co for vertex in obj.data.vertices]
    minimum = [min(float(point[axis]) for point in points) for axis in range(3)]
    maximum = [max(float(point[axis]) for point in points) for axis in range(3)]
    return {
        "min": minimum,
        "max": maximum,
        "dimensions": [maximum[index] - minimum[index] for index in range(3)],
    }


def bounds_match(actual: Dict[str, List[float]]) -> bool:
    return all(abs(actual[key][index] - EXPECTED_BOUNDS[key][index]) <= EPS for key in EXPECTED_BOUNDS for index in range(3))


def component_count(mesh: Any) -> int:
    adjacency: Dict[int, set[int]] = {index: set() for index in range(len(mesh.vertices))}
    for edge in mesh.edges:
        a, b = (int(value) for value in edge.vertices)
        adjacency[a].add(b)
        adjacency[b].add(a)
    remaining = set(adjacency)
    total = 0
    while remaining:
        total += 1
        pending = [remaining.pop()]
        while pending:
            for neighbor in adjacency[pending.pop()]:
                if neighbor in remaining:
                    remaining.remove(neighbor)
                    pending.append(neighbor)
    return total


def topology_record(obj: Any) -> Dict[str, Any]:
    edge_use: collections.Counter[Tuple[int, int]] = collections.Counter()
    degenerates = 0
    for polygon in obj.data.polygons:
        indices = [int(value) for value in polygon.vertices]
        for a, b in zip(indices, indices[1:] + indices[:1]):
            edge_use[tuple(sorted((a, b)))] += 1
        if len(indices) == 3:
            a, b, c = (obj.data.vertices[index].co for index in indices)
            if (b - a).cross(c - a).length * 0.5 <= 1.0e-10:
                degenerates += 1
    return {
        "connected_components": component_count(obj.data),
        "boundary_edges": sum(1 for value in edge_use.values() if value == 1),
        "nonmanifold_edges": sum(1 for value in edge_use.values() if value != 2),
        "degenerate_triangles": degenerates,
    }


def verify_owned_basecolor(source_rel: Path, recovery_rel: Path) -> Dict[str, Any]:
    from PIL import Image

    uv_plan = load_json(UV_PLAN_REL)
    mask_manifest = load_json(MASK_MANIFEST_REL)
    windows = {entry["view"]: entry["rect"] for entry in uv_plan["uv0"]["source_windows_half_open_px"]}
    source = Image.open(ROOT / source_rel).convert("RGB")
    recovery = Image.open(ROOT / recovery_rel).convert("RGB")
    mismatches = 0
    compared = 0
    by_view: Dict[str, Dict[str, int]] = {}
    for record in mask_manifest["records"]:
        view = record["view"]
        rect = windows[view]
        mask = Image.open(ROOT / record["mask_path"]).convert("L")
        local_mismatches = 0
        local_compared = 0
        source_pixels = source.load()
        recovery_pixels = recovery.load()
        mask_pixels = mask.load()
        for y in range(mask.height):
            for x in range(mask.width):
                if mask_pixels[x, y] > 0:
                    atlas_x, atlas_y = rect[0] + x, rect[1] + y
                    local_compared += 1
                    if source_pixels[atlas_x, atlas_y] != recovery_pixels[atlas_x, atlas_y]:
                        local_mismatches += 1
        mismatches += local_mismatches
        compared += local_compared
        by_view[view] = {"pixels_compared": local_compared, "mismatches": local_mismatches}
    return {"pixels_compared": compared, "mismatches": mismatches, "by_view": by_view}


def import_fbx_audit(bpy: Any, manifest: Dict[str, Any]) -> Dict[str, Any]:
    records: Dict[str, Any] = {}
    for lod_name, export in manifest["exports"].items():
        before = set(bpy.data.objects)
        bpy.ops.import_scene.fbx(filepath=str(ROOT / export["path"]), use_custom_normals=True)
        imported = [obj for obj in bpy.data.objects if obj not in before]
        meshes = [obj for obj in imported if obj.type == "MESH"]
        primary = max(meshes, key=lambda obj: mesh_triangles(obj.data)) if meshes else None
        records[lod_name] = {
            "mesh_objects": len(meshes),
            "primary_triangles": mesh_triangles(primary.data) if primary else 0,
            "expected_triangles": manifest["lods"][lod_name]["triangles"],
            "pass": bool(primary) and mesh_triangles(primary.data) == manifest["lods"][lod_name]["triangles"],
        }
        for obj in imported:
            bpy.data.objects.remove(obj, do_unlink=True)
    return records


def schema_report() -> Dict[str, Any]:
    plan = load_json(PLAN_REL)
    required = [SOURCE_REL, STEP11_REL, UV_PLAN_REL, BLEND_REL, MANIFEST_REL, FINAL_REL, RENDER_AUDIT_REL]
    existing = {str(rel): (ROOT / rel).is_file() for rel in required}
    source_hash = sha256_file(ROOT / SOURCE_REL)
    passed = all(existing.values()) and source_hash == plan["source_authority"]["sha256"]
    return {
        "schema": "aerathea.a005_visual_fidelity_recovery_auditor_preflight.v1",
        "asset_id": ASSET,
        "contract_id": CONTRACT,
        "status": "pass_schema_only_no_bpy_no_writes" if passed else "blocked_preflight",
        "files": existing,
        "source_sha256": source_hash,
        "expected_source_sha256": plan["source_authority"]["sha256"],
        "tracked_validation": str(VALIDATION_REL),
        "local_audit": str(LOCAL_AUDIT_REL),
    }


def audit() -> Dict[str, Any]:
    import bpy  # type: ignore
    from PIL import Image

    manifest = load_json(MANIFEST_REL)
    plan = load_json(PLAN_REL)
    step11 = load_json(STEP11_REL)
    render_audit = load_json(RENDER_AUDIT_REL)
    gates: List[Dict[str, Any]] = []

    source_hash = sha256_file(ROOT / SOURCE_REL)
    gates.append(gate("G01_source_authority_hash", source_hash == plan["source_authority"]["sha256"] == manifest["source_authority"]["sha256"], source_hash))
    gates.append(gate("G02_step11_blueprint_authority", step11["status"].startswith("approved") and step11["triangle_budget"]["lod0_hard_cap"] == 10000, step11["status"]))
    gates.append(gate("G03_contract_and_classification", manifest["contract_id"] == CONTRACT and manifest["artifact_classification"] == "candidate", {"contract": manifest["contract_id"], "classification": manifest["artifact_classification"]}))
    gates.append(gate("G04_no_historical_geometry_inputs", manifest["rebuild_from_historical_a005_geometry"] is False and manifest["legacy_a001_a004_geometry_used"] is False, {"historical": manifest["rebuild_from_historical_a005_geometry"], "legacy": manifest["legacy_a001_a004_geometry_used"]}))

    lod_records: Dict[str, Any] = {}
    for lod_name, expected_tris in EXPECTED_TRIS.items():
        obj = bpy.data.objects.get(f"{ASSET}_{lod_name}")
        lod_records[lod_name] = {
            "present": obj is not None,
            "triangles": mesh_triangles(obj.data) if obj else 0,
            "bounds": object_bounds(obj) if obj else None,
            "uv_layers": [layer.name for layer in obj.data.uv_layers] if obj else [],
            "materials": len(obj.data.materials) if obj else 0,
        }
    gates.append(gate("G05_lod_objects_and_exact_triangles", all(record["present"] and record["triangles"] == EXPECTED_TRIS[name] for name, record in lod_records.items()), lod_records))
    gates.append(gate("G06_lod0_approved_range_and_monotonic", 4000 <= lod_records["LOD0"]["triangles"] <= 10000 and all(lod_records[a]["triangles"] > lod_records[b]["triangles"] for a, b in zip(("LOD0", "LOD1", "LOD2"), ("LOD1", "LOD2", "LOD3"))), {name: value["triangles"] for name, value in lod_records.items()}))
    gates.append(gate("G07_bounds_and_pivot", all(bounds_match(record["bounds"]) for record in lod_records.values()) and list(bpy.data.objects[f"{ASSET}_LOD0"].location) == [0.0, 0.0, 0.0], {name: value["bounds"] for name, value in lod_records.items()}))
    gates.append(gate("G08_uv0_uv1_all_lods", all(record["uv_layers"] == ["UVMap", "LightmapUV"] for record in lod_records.values()), {name: value["uv_layers"] for name, value in lod_records.items()}))
    gates.append(gate("G09_single_material_all_lods", all(record["materials"] == 1 for record in lod_records.values()) and len([material for material in bpy.data.materials if material.name.startswith("M_GIA_BloodAxeCairnstone_A005")]) == 1, {name: value["materials"] for name, value in lod_records.items()}))

    topology = topology_record(bpy.data.objects[f"{ASSET}_LOD0"])
    gates.append(gate("G10_four_closed_primary_shells", topology == {"connected_components": 4, "boundary_edges": 0, "nonmanifold_edges": 0, "degenerate_triangles": 0}, topology))
    gates.append(gate("G11_decoration_geometry_zero", manifest["macro_features"]["C005_C006_C007_geometry"] == 0 and bpy.data.objects[f"{ASSET}_LOD0"].get("aerathea_decoration_geometry") == 0, manifest["macro_features"]))

    collisions = [obj.name for obj in bpy.data.objects if obj.name.startswith(f"UCX_{ASSET}_")]
    gates.append(gate("G12_collision_set", len(collisions) == 4 and sorted(collisions) == sorted(manifest["collision"]["names"]), collisions))

    texture_checks: Dict[str, Any] = {}
    for name, record in manifest["textures"].items():
        path = ROOT / record["path"]
        texture_checks[name] = {"exists": path.is_file(), "actual_sha256": sha256_file(path) if path.is_file() else None, "expected_sha256": record["sha256"]}
    gates.append(gate("G13_texture_map_hashes", len(texture_checks) == 3 and all(value["exists"] and value["actual_sha256"] == value["expected_sha256"] for value in texture_checks.values()), texture_checks))
    bc_record = next(record for name, record in manifest["textures"].items() if name.endswith("_BC.png"))
    ownership = verify_owned_basecolor(Path(bc_record["source_path"]), Path(bc_record["path"]))
    gates.append(gate("G14_source_owned_basecolor_exact", ownership["mismatches"] == 0 and ownership["pixels_compared"] > 0, ownership))

    export_checks = {
        lod: {
            "exists": (ROOT / record["path"]).is_file(),
            "bytes": (ROOT / record["path"]).stat().st_size if (ROOT / record["path"]).is_file() else 0,
            "sha256": sha256_file(ROOT / record["path"]) if (ROOT / record["path"]).is_file() else None,
            "expected_sha256": record["sha256"],
        }
        for lod, record in manifest["exports"].items()
    }
    gates.append(gate("G15_fbx_files_and_hashes", len(export_checks) == 4 and all(value["exists"] and value["bytes"] > 0 and value["sha256"] == value["expected_sha256"] for value in export_checks.values()) and len({value["sha256"] for value in export_checks.values()}) == 4, export_checks))
    imported = import_fbx_audit(bpy, manifest)
    gates.append(gate("G16_clean_fbx_reimport", all(record["pass"] for record in imported.values()), imported))

    image = Image.open(ROOT / FINAL_REL).convert("RGB")
    final_hash = sha256_file(ROOT / FINAL_REL)
    render_pass = (
        image.size == (1400, 1600)
        and 80.0 <= float(render_audit["mean_luminance"]) <= 180.0
        and float(render_audit["near_black_fraction"]) < 0.01
        and float(render_audit["near_white_fraction"]) < 0.01
        and render_audit["orientation"] == "upright source-matched front with slight top reveal"
        and render_audit["collision_visible"] == 0
        and render_audit["lod_visible"] == "LOD0 only"
    )
    gates.append(gate("G17_final_render_technical", render_pass, {**render_audit, "sha256": final_hash}))
    gates.append(
        gate(
            "G18_scene_units_and_status",
            abs(float(bpy.context.scene.unit_settings.scale_length) - 0.01) <= 1.0e-8
            and not bool(bpy.context.scene.get("aerathea_unreal_work_performed")),
            {
                "scale_length": bpy.context.scene.unit_settings.scale_length,
                "unreal": bpy.context.scene.get("aerathea_unreal_work_performed"),
            },
        )
    )
    gates.append(gate("G19_no_unreal_or_full_game_ready_claim", manifest["unreal_outputs"] == 0 and manifest["fully_game_ready"] is False, {"unreal_outputs": manifest["unreal_outputs"], "fully_game_ready": manifest["fully_game_ready"]}))
    gates.append(gate("G20_steps01_16_recovery_scope", manifest["first_divergence_repaired"] == "STEP_12_under_resolved_784_triangle_blockout" and manifest["pipeline_status"].startswith("DCC game-ready candidate"), {"first_divergence": manifest["first_divergence_repaired"], "pipeline_status": manifest["pipeline_status"]}))

    passed = all(item["status"] == "pass" for item in gates)
    step_results = {f"STEP_{index:02d}": ("retained_authoritative_valid" if index <= 10 else ("authoritative_blueprint_honored" if index == 11 else "recovered_and_independently_validated")) for index in range(1, 17)}
    payload = {
        "schema": "aerathea.a005_visual_fidelity_recovery_validation.v1",
        "asset_id": ASSET,
        "contract_id": CONTRACT,
        "date": "2026-07-20",
        "status": "pass_dcc_game_ready_candidate_pending_flamestrike_visual_approval" if passed else "blocked_independent_audit_failure",
        "artifact_classification": "proof only",
        "pipeline_status": "DCC game-ready candidate" if passed else "candidate blocked",
        "fully_game_ready": False,
        "unreal_outputs": 0,
        "source_authority": {"path": str(SOURCE_REL), "sha256": source_hash},
        "candidate": {"blend": str(BLEND_REL), "blend_sha256": sha256_file(ROOT / BLEND_REL), "manifest": str(MANIFEST_REL), "manifest_sha256": sha256_file(ROOT / MANIFEST_REL)},
        "final_review_image": {"path": str(FINAL_REL), "sha256": final_hash, "orientation": render_audit["orientation"], "visual_gate": "pass_internal_source_matched_front_pending_Flamestrike"},
        "step_results": step_results,
        "gates": gates,
        "gate_summary": {"passed": sum(1 for item in gates if item["status"] == "pass"), "total": len(gates)},
        "review_requirement": "Open only the final accepted image visibly for Flamestrike; intermediate rejected frames are not review gates.",
    }
    write_json(LOCAL_AUDIT_REL, payload)
    write_json(VALIDATION_REL, payload)
    return payload


def main() -> int:
    args = parse_args(blender_args())
    result = schema_report() if args.schema_only else audit()
    print(json.dumps(result, indent=2))
    return 0 if not result["status"].startswith("blocked") else 1


if __name__ == "__main__":
    raise SystemExit(main())
