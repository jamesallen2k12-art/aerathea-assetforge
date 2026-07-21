"""Independent technical audit for Siege Breaker pixel reconstruction A03."""

from __future__ import annotations

import hashlib
import json
import struct
from pathlib import Path

import bpy
from mathutils import Vector


ROOT = Path(__file__).resolve().parents[2]
ASSET_ID = "SM_DRW_SiegeBreaker_Hammer_A01"
REVISION = "PixelReconstruction_A03"
CONTRACT_ID = "SB-VF-A03-PIXEL"
SOURCE_ROOT = ROOT / "SourceAssets/Blender/Weapons/Dwarven" / ASSET_ID
BLEND_PATH = SOURCE_ROOT / f"{ASSET_ID}_DCCGameReady_{REVISION}.blend"
MANIFEST_PATH = SOURCE_ROOT / f"{ASSET_ID}_{REVISION.upper()}_MANIFEST.json"
EXPORT_ROOT = ROOT / "SourceAssets/Exports/Weapons/Dwarven" / ASSET_ID / REVISION
TEXTURE_ROOT = ROOT / "SourceAssets/Textures/Weapons/Dwarven" / ASSET_ID / REVISION
BLUEPRINT_ROOT = ROOT / "docs/assets/blueprints" / ASSET_ID
MEASUREMENT_PATH = BLUEPRINT_ROOT / "manifests/VISUAL_FIDELITY_A03_SOURCE_MEASUREMENTS.json"
CONFLICT_PATH = BLUEPRINT_ROOT / "manifests/VISUAL_FIDELITY_A03_CROSS_VIEW_CONFLICT_AUDIT.json"
COMPARISON_PATH = BLUEPRINT_ROOT / "manifests/VISUAL_FIDELITY_A03_PIXEL_COMPARISON.json"
VALIDATION_PATH = BLUEPRINT_ROOT / "manifests/VISUAL_FIDELITY_A03_TECHNICAL_AUDIT.json"
REVIEW_PATH = BLUEPRINT_ROOT / "review/VISUAL_FIDELITY_A03_TECHNICAL_AUDIT.md"
RENDER_ROOT = ROOT / "Saved/Automation/DCC" / ASSET_ID / "VisualFidelity_A03"
MATERIAL_ORDER = ["M_Stone", "M_Bronze", "M_Steel", "M_Leather", "M_Rune_Emissive"]
TOLERANCE_CM = 0.002


def sha256(path: Path) -> str:
    digest = hashlib.sha256()
    with path.open("rb") as handle:
        for chunk in iter(lambda: handle.read(1024 * 1024), b""):
            digest.update(chunk)
    return digest.hexdigest()


def png_size(path: Path):
    with path.open("rb") as handle:
        header = handle.read(24)
    if len(header) != 24 or header[:8] != b"\x89PNG\r\n\x1a\n" or header[12:16] != b"IHDR":
        raise ValueError(f"Not a PNG: {path}")
    return list(struct.unpack(">II", header[16:24]))


def bounds_cm(objects):
    points = [obj.matrix_world @ Vector(corner) for obj in objects if obj.type == "MESH" for corner in obj.bound_box]
    if not points:
        raise RuntimeError("No mesh bounds")
    minimum = [min(point[index] for point in points) * 100.0 for index in range(3)]
    maximum = [max(point[index] for point in points) * 100.0 for index in range(3)]
    extent = [maximum[index] - minimum[index] for index in range(3)]
    return minimum, maximum, extent


def triangle_count(obj):
    obj.data.calc_loop_triangles()
    return len(obj.data.loop_triangles)


def close_vector(observed, expected, tolerance=TOLERANCE_CM):
    return all(abs(float(a) - float(b)) <= tolerance for a, b in zip(observed, expected))


def reset_scene():
    bpy.ops.wm.read_factory_settings(use_empty=True)


def import_fbx(path: Path):
    reset_scene()
    bpy.ops.import_scene.fbx(filepath=str(path), global_scale=1.0, automatic_bone_orientation=False)
    meshes = [obj for obj in bpy.context.scene.objects if obj.type == "MESH"]
    asset_meshes = [obj for obj in meshes if not obj.name.startswith("UCX_")]
    collision_meshes = [obj for obj in meshes if obj.name.startswith("UCX_")]
    minimum, maximum, extent = bounds_cm(asset_meshes)
    return {
        "path": str(path.relative_to(ROOT)),
        "asset_mesh_count": len(asset_meshes),
        "collision_mesh_count": len(collision_meshes),
        "bounds_cm": {"minimum": minimum, "maximum": maximum, "extent": extent},
        "triangles": sum(triangle_count(obj) for obj in asset_meshes),
    }


def import_glb(path: Path):
    reset_scene()
    bpy.ops.import_scene.gltf(filepath=str(path))
    meshes = [obj for obj in bpy.context.scene.objects if obj.type == "MESH"]
    minimum, maximum, extent = bounds_cm(meshes)
    return {
        "path": str(path.relative_to(ROOT)),
        "mesh_count": len(meshes),
        "bounds_cm": {"minimum": minimum, "maximum": maximum, "extent": extent},
        "triangles": sum(triangle_count(obj) for obj in meshes),
    }


def main() -> int:
    checks = []

    def check(check_id, condition, expected, observed, note=""):
        checks.append({"id": check_id, "pass": bool(condition), "expected": expected, "observed": observed, "note": note})

    manifest = json.loads(MANIFEST_PATH.read_text(encoding="utf-8"))
    measurement = json.loads(MEASUREMENT_PATH.read_text(encoding="utf-8"))
    conflict = json.loads(CONFLICT_PATH.read_text(encoding="utf-8"))
    comparison = json.loads(COMPARISON_PATH.read_text(encoding="utf-8"))
    check("G01_CONTRACT_ID", manifest.get("contract_id") == CONTRACT_ID, CONTRACT_ID, manifest.get("contract_id"))
    measurement_source = measurement.get("source", {})
    measurement_panels = set(measurement.get("panels", {}))
    measurement_regions = set(measurement.get("primary_regions", {}))
    measurement_pass = (
        measurement_source.get("sha256") == "3308a7bd0f0830c9cd1b695b57077d9faf77a839bb3e70edc6afe87c68af8b74"
        and measurement_source.get("size_px") == [1055, 1491]
        and measurement_source.get("source_pixels_modified") is False
        and measurement_panels == {"primary_3_4", "front", "back", "left", "right", "top", "bottom"}
        and measurement_regions == {"head", "shaft", "grip", "pommel"}
    )
    check("G02_SOURCE_MEASUREMENT", measurement_pass, "locked source hash/size, seven measured panels, four primary regions, unmodified pixels", {"source": measurement_source, "panels": sorted(measurement_panels), "regions": sorted(measurement_regions)})
    check("G03_CROSS_VIEW_CONFLICT_DECLARED", conflict.get("result") == "pass_with_declared_cross_view_scale_conflict", "pass_with_declared_cross_view_scale_conflict", conflict.get("result"))
    check("G04_PIXEL_COMPARISON", comparison.get("result") == "pass" and comparison.get("summary", {}).get("passed") == 5, "pass 5/5", {"result": comparison.get("result"), "summary": comparison.get("summary")})
    check("G05_NO_A01_A02_GEOMETRY", manifest.get("authority", {}).get("a01_a02_geometry_used") is False, False, manifest.get("authority", {}).get("a01_a02_geometry_used"))

    bpy.ops.wm.open_mainfile(filepath=str(BLEND_PATH))
    scene = bpy.context.scene
    asset_collection = bpy.data.collections["SB_ASSET"]
    source_objects = [obj for obj in asset_collection.all_objects if obj.type == "MESH"]
    names = {obj.name for obj in source_objects}
    minimum, maximum, extent = bounds_cm(source_objects)
    check("G06_OVERALL_MIN", close_vector(minimum, (-26, -16, 0)), [-26, -16, 0], minimum)
    check("G07_OVERALL_MAX", close_vector(maximum, (26, 16, 170)), [26, 16, 170], maximum)
    check("G08_OVERALL_EXTENT", close_vector(extent, (52, 32, 170)), [52, 32, 170], extent)

    head_objects = [obj for obj in source_objects if obj.name.startswith(("Head_", "Stone", "Core", "Rivet_Core"))]
    head_min, head_max, head_extent = bounds_cm(head_objects)
    check("G09_HEAD_BOUNDS", close_vector(head_min, (-26, -16, 132)) and close_vector(head_max, (26, 16, 170)), {"min": [-26, -16, 132], "max": [26, 16, 170]}, {"min": head_min, "max": head_max, "extent": head_extent})

    shaft_min, shaft_max, shaft_extent = bounds_cm([bpy.data.objects["Shaft_Metal"]])
    check("G10_SHAFT_ANCHOR", close_vector(shaft_min, (-2.5, -2.5, 14)) and close_vector(shaft_max, (2.5, 2.5, 132)), {"min": [-2.5, -2.5, 14], "max": [2.5, 2.5, 132]}, {"min": shaft_min, "max": shaft_max, "extent": shaft_extent})

    grip_objects = [obj for obj in source_objects if obj.name == "Grip_Leather" or obj.name.startswith("Grip_Wrap_")]
    grip_min, grip_max, grip_extent = bounds_cm(grip_objects)
    grip_diameter = max(grip_extent[0], grip_extent[1])
    check("G11_GRIP_ANCHOR", abs(grip_min[2] - 18.0) <= TOLERANCE_CM and abs(grip_max[2] - 60.0) <= TOLERANCE_CM and abs(grip_diameter - 5.0) <= 0.01, {"z": [18, 60], "outer_diameter": 5}, {"min": grip_min, "max": grip_max, "extent": grip_extent, "outer_diameter": grip_diameter})

    pommel_min, pommel_max, pommel_extent = bounds_cm([bpy.data.objects["Pommel"]])
    check("G12_POMMEL_ANCHOR", close_vector(pommel_min, (-5.5, -4.5, 0)) and close_vector(pommel_max, (5.5, 4.5, 18)), {"min": [-5.5, -4.5, 0], "max": [5.5, 4.5, 18]}, {"min": pommel_min, "max": pommel_max, "extent": pommel_extent})
    check("G13_SHAFT_POMMEL_OVERLAP", min(132, 18) - max(14, 0) == 4, 4, 4)
    check("G14_SOURCE_TRANSFORMS", all(all(abs(float(value) - 1.0) <= 1e-5 for value in obj.scale) for obj in source_objects), "all source mesh scales applied", {obj.name: list(obj.scale) for obj in source_objects if any(abs(float(value) - 1.0) > 1e-5 for value in obj.scale)})
    check("G15_SOURCE_UV", all(obj.data.uv_layers.get("UVMap") is not None for obj in source_objects), "UVMap on every source mesh", [obj.name for obj in source_objects if obj.data.uv_layers.get("UVMap") is None])
    check("G16_OBJECT_AUTHORITY_FLAGS", scene.get("Aerathea.A01A02GeometryUsed") is False and all(obj.get("Aerathea.A01A02GeometryUsed") is False for obj in source_objects), False, {"scene": scene.get("Aerathea.A01A02GeometryUsed"), "invalid_objects": [obj.name for obj in source_objects if obj.get("Aerathea.A01A02GeometryUsed") is not False]})

    lods = [bpy.data.objects[f"{ASSET_ID}_LOD{level}"] for level in range(4)]
    lod_triangles = [triangle_count(obj) for obj in lods]
    lod_ratios = [value / lod_triangles[0] for value in lod_triangles]
    check("G17_LOD0_LARGE_PROP_BUDGET", 4000 <= lod_triangles[0] <= 10000, [4000, 10000], lod_triangles[0])
    check("G18_LOD_RATIOS", 0.55 <= lod_ratios[1] <= 0.70 and 0.34 <= lod_ratios[2] <= 0.48 and 0.14 <= lod_ratios[3] <= 0.22, {"LOD1": [0.55, 0.70], "LOD2": [0.34, 0.48], "LOD3": [0.14, 0.22]}, {f"LOD{index}": round(value, 6) for index, value in enumerate(lod_ratios)})
    check("G19_LOD_MONOTONIC", all(lod_triangles[index] > lod_triangles[index + 1] for index in range(3)), "strictly decreasing", lod_triangles)
    lod_bounds = [bounds_cm([obj])[2] for obj in lods]
    check("G20_LOD_SILHOUETTE_BOUNDS", all(close_vector(item, (52, 32, 170), 0.02) for item in lod_bounds), [52, 32, 170], lod_bounds)
    check("G21_MATERIAL_SLOTS", all([slot.material.name for slot in obj.material_slots] == MATERIAL_ORDER for obj in lods), MATERIAL_ORDER, {obj.name: [slot.material.name for slot in obj.material_slots] for obj in lods})
    check("G22_LOD_UV", all(obj.data.uv_layers.get("UVMap") is not None for obj in lods), "UVMap on every LOD", [obj.name for obj in lods if obj.data.uv_layers.get("UVMap") is None])
    check("G23_PIVOT", all(obj.location.length <= 1e-6 for obj in lods), [0, 0, 0], {obj.name: list(obj.location) for obj in lods})

    collision_objects = [obj for obj in bpy.data.collections["SB_COLLISION"].all_objects if obj.type == "MESH"]
    collision_names = sorted(obj.name for obj in collision_objects)
    check("G24_COLLISION", len(collision_objects) == 3 and all(name.startswith(f"UCX_{ASSET_ID}_") for name in collision_names), "3 named custom proxies", collision_names)

    texture_manifest_path = TEXTURE_ROOT / f"{ASSET_ID}_TEXTURE_MANIFEST.json"
    texture_manifest = json.loads(texture_manifest_path.read_text(encoding="utf-8"))
    texture_files = sorted(TEXTURE_ROOT.glob("*.png"))
    sizes = {path.name: png_size(path) for path in texture_files}
    check("G25_TEXTURE_PACKAGE", len(texture_files) == 20 and all(size == [2048, 2048] for size in sizes.values()), "20 maps at 2048x2048", sizes)
    expected_hashes = {Path(item["path"]).name: item["sha256"] for item in texture_manifest["files"]}
    actual_hashes = {path.name: sha256(path) for path in texture_files}
    check("G26_TEXTURE_HASHES", expected_hashes == actual_hashes, expected_hashes, actual_hashes)

    feature_groups = manifest.get("required_feature_groups", {})
    check("G27_SOURCE_FEATURE_GROUPS", all(feature_groups.get(key) for key in ("faceted_runestone_masses", "stone_crack_and_rail_system", "layered_architectural_core", "engraved_shaft", "dense_crossed_grip", "compact_faceted_pommel")), "all six source feature groups populated", {key: len(value) for key, value in feature_groups.items()})
    wraps = sorted(name for name in names if name.startswith("Grip_Wrap_"))
    directions = sorted(bpy.data.objects[name].get("Aerathea.WrapDirection", "") for name in wraps)
    check("G28_CROSSED_GRIP", len(wraps) == 2 and directions == ["ascending", "descending"], {"count": 2, "directions": ["ascending", "descending"]}, {"objects": wraps, "directions": directions})

    export_files = [EXPORT_ROOT / f"{ASSET_ID}.fbx"] + [EXPORT_ROOT / f"{ASSET_ID}_LOD{level}.fbx" for level in range(1, 4)] + [EXPORT_ROOT / f"{ASSET_ID}.glb"]
    check("G29_EXPORT_FILES", all(path.exists() and path.stat().st_size > 0 for path in export_files), "all FBX/GLB files nonzero", {str(path.relative_to(ROOT)): path.stat().st_size if path.exists() else 0 for path in export_files})
    fbx_audits = [import_fbx(path) for path in export_files[:4]]
    check("G30_IMPORTED_FBX_TRIANGLES", [item["triangles"] for item in fbx_audits] == lod_triangles, lod_triangles, [item["triangles"] for item in fbx_audits])
    check("G31_IMPORTED_FBX_BOUNDS", all(close_vector(item["bounds_cm"]["extent"], (52, 32, 170), 0.02) for item in fbx_audits), [52, 32, 170], [item["bounds_cm"]["extent"] for item in fbx_audits])
    check("G32_IMPORTED_FBX_COLLISION", fbx_audits[0]["collision_mesh_count"] == 3 and all(item["collision_mesh_count"] == 0 for item in fbx_audits[1:]), "3 proxies in base FBX only", [item["collision_mesh_count"] for item in fbx_audits])
    glb_audit = import_glb(export_files[4])
    check("G33_IMPORTED_GLB", glb_audit["triangles"] == lod_triangles[0] and close_vector(glb_audit["bounds_cm"]["extent"], (52, 32, 170), 0.02), {"triangles": lod_triangles[0], "bounds": [52, 32, 170]}, {"triangles": glb_audit["triangles"], "bounds": glb_audit["bounds_cm"]["extent"]})

    final_render = RENDER_ROOT / "matched_source_view" / f"{ASSET_ID}_A03_SourceMatched_Final.png"
    ortho_manifest_path = RENDER_ROOT / "orthographic_true/render_manifest.json"
    ortho_manifest = json.loads(ortho_manifest_path.read_text(encoding="utf-8"))
    ortho_files = [ROOT / ortho_manifest["views"][name]["path"] for name in ("front", "back", "left", "right", "top", "bottom")]
    matched_manifest_path = RENDER_ROOT / "matched_source_view/render_manifest.json"
    matched_manifest = json.loads(matched_manifest_path.read_text(encoding="utf-8"))
    blend_hash = sha256(BLEND_PATH)
    check("G34_FINAL_MATCHED_RENDER", final_render.exists() and png_size(final_render) == [1600, 2200] and matched_manifest.get("source_blend_sha256") == blend_hash, {"resolution": [1600, 2200], "source_blend_sha256": blend_hash}, {"resolution": png_size(final_render) if final_render.exists() else None, "source_blend_sha256": matched_manifest.get("source_blend_sha256")})
    check("G35_ORTHOGRAPHIC_PROOFS", all(path.exists() and png_size(path) == [1536, 1536] for path in ortho_files) and ortho_manifest.get("source_blend_sha256") == blend_hash, {"views": "six fixed-object 1536px", "source_blend_sha256": blend_hash}, {"views": {path.name: png_size(path) if path.exists() else None for path in ortho_files}, "source_blend_sha256": ortho_manifest.get("source_blend_sha256")})
    check("G36_STATUS_BOUNDARY", manifest.get("artifact_status") == "candidate" and manifest.get("unreal_import_authorized") is False and manifest.get("fully_game_ready") is False, {"artifact_status": "candidate", "unreal": False, "fully_game_ready": False}, {key: manifest.get(key) for key in ("artifact_status", "unreal_import_authorized", "fully_game_ready")})

    passed = sum(1 for item in checks if item["pass"])
    failures = [item for item in checks if not item["pass"]]
    report = {
        "schema": "aerathea.siegebreaker.a03_technical_audit.v1",
        "asset_id": ASSET_ID,
        "revision": REVISION,
        "contract_id": CONTRACT_ID,
        "artifact_status": "proof only",
        "result": "pass" if not failures else "fail",
        "summary": {"passed": passed, "total": len(checks), "failures": len(failures)},
        "pipeline_status": "DCC game-ready candidate pending Flamestrike visual approval" if not failures else "blocked",
        "checks": checks,
        "fbx_import_audits": fbx_audits,
        "glb_import_audit": glb_audit,
        "source_blend": {"path": str(BLEND_PATH.relative_to(ROOT)), "sha256": sha256(BLEND_PATH)},
        "dcc_manifest": {"path": str(MANIFEST_PATH.relative_to(ROOT)), "sha256": sha256(MANIFEST_PATH)},
        "pixel_comparison": {"path": str(COMPARISON_PATH.relative_to(ROOT)), "sha256": sha256(COMPARISON_PATH)},
        "final_visual_approval": "pending Flamestrike",
        "unreal_authorized": False,
    }
    VALIDATION_PATH.write_text(json.dumps(report, indent=2) + "\n", encoding="utf-8")
    lines = [
        "# Siege Breaker A03 Technical Audit", "",
        f"- Result: `{report['result']}`", f"- Gates: `{passed}/{len(checks)}`",
        f"- Pipeline status: `{report['pipeline_status']}`", "- Artifact classification: `proof only`",
        "- Final visual approval: pending Flamestrike", "- Unreal authority: false", "", "## Gate Results", "",
    ]
    lines.extend(f"- [{'x' if item['pass'] else ' '}] `{item['id']}`" for item in checks)
    if failures:
        lines += ["", "## Failures", ""]
        lines.extend(f"- `{item['id']}`: expected `{item['expected']}`, observed `{item['observed']}`" for item in failures)
    REVIEW_PATH.write_text("\n".join(lines) + "\n", encoding="utf-8")
    print(VALIDATION_PATH)
    print(REVIEW_PATH)
    print(f"AUDIT_RESULT={report['result']} PASSED={passed}/{len(checks)}")
    return 0 if not failures else 1


if __name__ == "__main__":
    raise SystemExit(main())
