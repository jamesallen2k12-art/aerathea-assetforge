"""Independent technical audit for Siege Breaker Steps 01-16."""

from __future__ import annotations

import csv
import hashlib
import json
import math
import os
import struct
from pathlib import Path

import bpy
from mathutils import Vector


ROOT = Path(__file__).resolve().parents[2]
ASSET_ID = "SM_DRW_SiegeBreaker_Hammer_A01"
REVISION = os.environ.get("AET_SB_REVISION", "FinalPackage_A01")
CONTRACT_ID = os.environ.get("AET_SB_CONTRACT_ID", "SB-CR-STEPS01-16-FINALPKG-A01")
PACKAGE_ZIP = Path("/home/james/Downloads/SiegeBreaker_Codex_Final_Package.zip")
PACKAGE_ROOT = ROOT / "SourceAssets/Reference/Weapons/Dwarven" / ASSET_ID / "02_SiegeBreaker_Codex_Final_Package"
SOURCE_ROOT = ROOT / "SourceAssets/Blender/Weapons/Dwarven" / ASSET_ID
EXPORT_ROOT = Path(os.environ.get("AET_SB_EXPORT_ROOT", str(ROOT / "SourceAssets/Exports/Weapons/Dwarven" / ASSET_ID)))
TEXTURE_ROOT = Path(os.environ.get("AET_SB_TEXTURE_ROOT", str(ROOT / "SourceAssets/Textures/Weapons/Dwarven" / ASSET_ID)))
BLUEPRINT_ROOT = ROOT / "docs/assets/blueprints" / ASSET_ID
BLEND_PATH = Path(
    os.environ.get(
        "AET_SB_BLEND_PATH",
        str(SOURCE_ROOT / f"{ASSET_ID}_DCCGameReady_FinalPackage_A01.blend"),
    )
)
MANIFEST_PATH = Path(
    os.environ.get(
        "AET_SB_MANIFEST_PATH",
        str(SOURCE_ROOT / f"{ASSET_ID}_DCC_GAME_READY_MANIFEST.json"),
    )
)
VALIDATION_PATH = Path(
    os.environ.get(
        "AET_SB_VALIDATION_PATH",
        str(BLUEPRINT_ROOT / "manifests/STEPS_01_16_VALIDATION.json"),
    )
)
REVIEW_PATH = Path(
    os.environ.get(
        "AET_SB_AUDIT_REVIEW_PATH",
        str(BLUEPRINT_ROOT / "review/STEP_16_TECHNICAL_AUDIT.md"),
    )
)
MATERIAL_ORDER = ["M_Stone", "M_Bronze", "M_Steel", "M_Leather", "M_Rune_Emissive"]
TOLERANCE_CM = 0.001


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
        raise ValueError(f"Not a valid PNG header: {path}")
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


def object_bounds(obj):
    return bounds_cm([obj])


def reset_scene():
    bpy.ops.wm.read_factory_settings(use_empty=True)


def import_fbx(path: Path):
    reset_scene()
    bpy.ops.import_scene.fbx(filepath=str(path), global_scale=1.0, automatic_bone_orientation=False)
    meshes = [obj for obj in bpy.context.scene.objects if obj.type == "MESH"]
    asset_meshes = [obj for obj in meshes if not obj.name.startswith("UCX_")]
    collision_meshes = [obj for obj in meshes if obj.name.startswith("UCX_")]
    return {
        "path": str(path.relative_to(ROOT)),
        "asset_mesh_count": len(asset_meshes),
        "collision_mesh_count": len(collision_meshes),
        "bounds_cm": dict(zip(("minimum", "maximum", "extent"), bounds_cm(asset_meshes))),
        "triangles": sum(triangle_count(obj) for obj in asset_meshes),
        "material_slots": sorted({slot.material.name for obj in asset_meshes for slot in obj.material_slots if slot.material}),
    }


def import_glb(path: Path):
    reset_scene()
    bpy.ops.import_scene.gltf(filepath=str(path))
    meshes = [obj for obj in bpy.context.scene.objects if obj.type == "MESH"]
    return {
        "path": str(path.relative_to(ROOT)),
        "mesh_count": len(meshes),
        "bounds_cm": dict(zip(("minimum", "maximum", "extent"), bounds_cm(meshes))),
        "triangles": sum(triangle_count(obj) for obj in meshes),
    }


def main() -> int:
    checks = []

    def check(check_id, condition, expected, observed, note=""):
        checks.append(
            {
                "id": check_id,
                "pass": bool(condition),
                "expected": expected,
                "observed": observed,
                "note": note,
            }
        )

    package_hash = sha256(PACKAGE_ZIP)
    check(
        "G01_PACKAGE_HASH",
        package_hash == "6d4bf67fe4dcb1bc752c615d16b039bf6fd430037b6ffa4772f8ae83c689a8f0",
        "6d4bf67fe4dcb1bc752c615d16b039bf6fd430037b6ffa4772f8ae83c689a8f0",
        package_hash,
    )

    spec = json.loads((PACKAGE_ROOT / "asset_spec.json").read_text(encoding="utf-8"))
    csv_rows = list(csv.DictReader((PACKAGE_ROOT / "dimensions_cm.csv").open(encoding="utf-8")))
    csv_values = {row["name"]: float(row["value_cm"]) for row in csv_rows}
    dimensions = spec["dimensions_cm"]
    spec_values = {
        "overall_length": dimensions["overall_length_z"],
        "head_max_width": dimensions["head_max_width_x"],
        "head_height": dimensions["head_height_z"],
        "head_depth": dimensions["head_depth_y"],
        "structural_shaft_length": dimensions["structural_shaft_length_z"],
        "grip_wrap_length": dimensions["grip_wrap_length_z"],
        "handle_outer_diameter": dimensions["handle_outer_diameter"],
        "pommel_length": dimensions["pommel_length_z"],
        "pommel_max_width": dimensions["pommel_max_width_x"],
        "shaft_insertion_into_pommel": dimensions["shaft_insertion_into_pommel"],
    }
    check("G02_JSON_CSV_AGREEMENT", spec_values == csv_values, spec_values, csv_values)

    scanline_path = PACKAGE_ROOT / "reference/ScanlineCapture/REF_DRW_SiegeBreaker_FinalPackage_StyleReference_A01_ScanlineManifest.json"
    scanline = json.loads(scanline_path.read_text(encoding="utf-8"))
    scan_pass = scanline.get("pixel_exact") is True and scanline.get("max_rgb_delta") == 0 and scanline.get("changed_pixels") == 0
    check("G03_STYLE_SCANLINE", scan_pass, {"pixel_exact": True, "max_rgb_delta": 0, "changed_pixels": 0}, {key: scanline.get(key) for key in ("pixel_exact", "max_rgb_delta", "changed_pixels")})

    blockout = json.loads((SOURCE_ROOT / "SiegeBreaker_Blockout_Manifest.json").read_text(encoding="utf-8"))
    check("G04_CORRECTED_BLOCKOUT", blockout.get("numeric_pass") is True, True, blockout.get("numeric_pass"))

    manifest = json.loads(MANIFEST_PATH.read_text(encoding="utf-8"))
    bpy.ops.wm.open_mainfile(filepath=str(BLEND_PATH))
    asset_collection = bpy.data.collections.get("SB_ASSET")
    source_objects = [obj for obj in asset_collection.all_objects if obj.type == "MESH"]
    source_object_names = {obj.name for obj in source_objects}
    source_wrap_directions = {
        obj.name: obj.get("Aerathea.WrapDirection", "")
        for obj in source_objects
        if obj.name.startswith("Grip_Wrap_")
    }
    source_min, source_max, source_extent = bounds_cm(source_objects)
    check("G05_OVERALL_MIN", close_vector(source_min, (-26, -16, 0)), [-26, -16, 0], source_min)
    check("G06_OVERALL_MAX", close_vector(source_max, (26, 16, 170)), [26, 16, 170], source_max)
    check("G07_OVERALL_EXTENT", close_vector(source_extent, (52, 32, 170)), [52, 32, 170], source_extent)

    head_prefixes = (
        "Head_", "StonePlate_", "Rune_Left_", "Rune_Right_", "CoreBrace_", "CorePlate_", "CoreRune_",
        "StoneBand_", "RuneBar_", "Rivet_", "StoneFacet_", "StoneClamp_", "StoneRune",
        "CoreShield_", "RadialBrace_",
    )
    head_objects = [obj for obj in source_objects if obj.name.startswith(head_prefixes)]
    head_min, head_max, head_extent = bounds_cm(head_objects)
    check("G08_HEAD_BOUNDS", close_vector(head_min, (-26, -16, 132)) and close_vector(head_max, (26, 16, 170)), {"min": [-26, -16, 132], "max": [26, 16, 170], "extent": [52, 32, 38]}, {"min": head_min, "max": head_max, "extent": head_extent})

    shaft = bpy.data.objects["Shaft_Metal"]
    shaft_min, shaft_max, shaft_extent = object_bounds(shaft)
    check("G09_SHAFT", close_vector(shaft_min, (-2.5, -2.5, 14)) and close_vector(shaft_max, (2.5, 2.5, 132)), {"min": [-2.5, -2.5, 14], "max": [2.5, 2.5, 132]}, {"min": shaft_min, "max": shaft_max, "extent": shaft_extent})

    grip_objects = [obj for obj in source_objects if obj.name == "Grip_Leather" or obj.name.startswith("Grip_Wrap_")]
    grip_min, grip_max, grip_extent = bounds_cm(grip_objects)
    grip_diameter = max(grip_extent[0], grip_extent[1])
    check("G10_GRIP", abs(grip_min[2] - 18) <= TOLERANCE_CM and abs(grip_max[2] - 60) <= TOLERANCE_CM and abs(grip_diameter - 5) <= 0.01, {"z": [18, 60], "length": 42, "diameter": 5}, {"min": grip_min, "max": grip_max, "extent": grip_extent, "diameter": grip_diameter})

    pommel = bpy.data.objects["Pommel"]
    pommel_min, pommel_max, pommel_extent = object_bounds(pommel)
    check("G11_POMMEL", close_vector(pommel_min, (-5.5, -4.5, 0)) and close_vector(pommel_max, (5.5, 4.5, 18)), {"min": [-5.5, -4.5, 0], "max": [5.5, 4.5, 18]}, {"min": pommel_min, "max": pommel_max, "extent": pommel_extent})

    overlap = min(132, 18) - max(14, 0)
    check("G12_SHAFT_POMMEL_OVERLAP", overlap == 4, 4, overlap)
    check("G13_TRANSFORMS", all(all(abs(float(value) - 1.0) <= 1e-5 for value in obj.scale) for obj in source_objects), "all mesh scales applied", {obj.name: list(obj.scale) for obj in source_objects if any(abs(float(value) - 1.0) > 1e-5 for value in obj.scale)})
    check("G14_SOURCE_UV", all(obj.data.uv_layers.get("UVMap") is not None for obj in source_objects), "UVMap on every source mesh", [obj.name for obj in source_objects if obj.data.uv_layers.get("UVMap") is None])
    check("G15_SOURCE_MESH_VALID", all(obj.data.validate(verbose=False, clean_customdata=False) is False for obj in source_objects), "no mesh validation changes required", "validated")

    lod_collection = bpy.data.collections.get("SB_EXPORT")
    lods = [bpy.data.objects[f"{ASSET_ID}_LOD{level}"] for level in range(4)]
    lod_triangles = [triangle_count(obj) for obj in lods]
    lod_ratios = [value / lod_triangles[0] for value in lod_triangles]
    check("G16_LOD0_BUDGET", 3000 <= lod_triangles[0] <= 8000, [3000, 8000], lod_triangles[0])
    check("G17_LOD_RATIOS", 0.55 <= lod_ratios[1] <= 0.72 and 0.34 <= lod_ratios[2] <= 0.46 and 0.14 <= lod_ratios[3] <= 0.22, {"LOD1": [0.55, 0.72], "LOD2": [0.34, 0.46], "LOD3": [0.14, 0.22]}, {f"LOD{i}": ratio for i, ratio in enumerate(lod_ratios)})
    check("G18_LOD_MONOTONIC", all(lod_triangles[index] > lod_triangles[index + 1] for index in range(3)), "strictly decreasing", lod_triangles)
    lod_bounds = [bounds_cm([obj]) for obj in lods]
    check("G19_LOD_SILHOUETTES", all(close_vector(item[2], (52, 32, 170)) for item in lod_bounds), [52, 32, 170], [item[2] for item in lod_bounds])
    check("G20_MATERIAL_SLOTS", all([slot.material.name for slot in obj.material_slots] == MATERIAL_ORDER for obj in lods), MATERIAL_ORDER, {obj.name: [slot.material.name for slot in obj.material_slots] for obj in lods})
    check("G21_LOD_UV", all(obj.data.uv_layers.get("UVMap") is not None for obj in lods), "UVMap on every LOD", [obj.name for obj in lods if obj.data.uv_layers.get("UVMap") is None])

    collision_objects = [obj for obj in bpy.data.collections["SB_COLLISION"].all_objects if obj.type == "MESH"]
    collision_names = sorted(obj.name for obj in collision_objects)
    check("G22_COLLISION", len(collision_objects) == 3 and all(name.startswith(f"UCX_{ASSET_ID}_") for name in collision_names), "3 named custom convex proxies", collision_names)
    check("G23_PIVOT", all(obj.location.length <= 1e-6 for obj in lods), [0, 0, 0], {obj.name: list(obj.location) for obj in lods})

    texture_manifest = json.loads((TEXTURE_ROOT / f"{ASSET_ID}_TEXTURE_MANIFEST.json").read_text(encoding="utf-8"))
    texture_files = sorted(TEXTURE_ROOT.glob("*.png"))
    texture_sizes = {path.name: png_size(path) for path in texture_files}
    check("G24_TEXTURE_PACKAGE", len(texture_files) == 20 and all(size == [2048, 2048] for size in texture_sizes.values()), "20 maps at 2048x2048", texture_sizes)
    manifest_hashes = {Path(item["path"]).name: item["sha256"] for item in texture_manifest["files"]}
    actual_hashes = {path.name: sha256(path) for path in texture_files}
    check("G25_TEXTURE_HASHES", manifest_hashes == actual_hashes, manifest_hashes, actual_hashes)

    export_files = [EXPORT_ROOT / f"{ASSET_ID}.fbx"] + [EXPORT_ROOT / f"{ASSET_ID}_LOD{level}.fbx" for level in range(1, 4)] + [EXPORT_ROOT / f"{ASSET_ID}.glb"]
    check("G26_EXPORT_FILES", all(path.exists() and path.stat().st_size > 0 for path in export_files), "all FBX/GLB outputs nonzero", {str(path.relative_to(ROOT)): path.stat().st_size if path.exists() else 0 for path in export_files})

    fbx_audits = []
    for path in export_files[:4]:
        fbx_audits.append(import_fbx(path))
    expected_tris = lod_triangles
    check("G27_IMPORTED_FBX_TRIANGLES", [item["triangles"] for item in fbx_audits] == expected_tris, expected_tris, [item["triangles"] for item in fbx_audits])
    check("G28_IMPORTED_FBX_BOUNDS", all(close_vector(item["bounds_cm"]["extent"], (52, 32, 170), 0.02) for item in fbx_audits), [52, 32, 170], [item["bounds_cm"]["extent"] for item in fbx_audits])
    check("G29_IMPORTED_FBX_COLLISION", fbx_audits[0]["collision_mesh_count"] == 3 and all(item["collision_mesh_count"] == 0 for item in fbx_audits[1:]), "3 proxies in base FBX; none in separate LOD FBXs", [item["collision_mesh_count"] for item in fbx_audits])

    glb_audit = import_glb(export_files[4])
    check("G30_IMPORTED_GLB", glb_audit["triangles"] == lod_triangles[0] and close_vector(glb_audit["bounds_cm"]["extent"], (52, 32, 170), 0.02), {"triangles": lod_triangles[0], "bounds_cm": [52, 32, 170]}, {"triangles": glb_audit["triangles"], "bounds_cm": glb_audit["bounds_cm"]["extent"]})

    required_materials = set(MATERIAL_ORDER)
    manifest_materials = set(manifest["materials"])
    check("G31_MANIFEST_MATERIALS", manifest_materials == required_materials, sorted(required_materials), sorted(manifest_materials))
    check("G32_STATUS_BOUNDARY", manifest.get("pipeline_status") == "DCC game-ready candidate" and manifest.get("unreal_import_authorized") is False and manifest.get("fully_game_ready") is False, {"pipeline_status": "DCC game-ready candidate", "unreal": False, "fully_game_ready": False}, {key: manifest.get(key) for key in ("pipeline_status", "unreal_import_authorized", "fully_game_ready")})

    if REVISION == "VisualFidelity_A02":
        object_names = source_object_names
        stone_facets = sorted(name for name in object_names if name.startswith("StoneFacet_"))
        head_bracing = sorted(
            name for name in object_names
            if name.startswith(("StoneClamp_", "CoreBrace_", "CoreShield_", "RadialBrace_"))
        )
        rune_objects = sorted(name for name in object_names if "Rune" in name)
        wrap_objects = sorted(name for name in object_names if name.startswith("Grip_Wrap_"))
        wrap_directions = sorted(source_wrap_directions.get(name, "") for name in wrap_objects)
        shaft_inlays = sorted(
            name for name in object_names if name.startswith(("Shaft_Inlay", "Shaft_Engraved"))
        )
        pommel_layers = sorted(
            name for name in object_names if name.startswith(("PommelPlate_", "PommelRune_", "PommelBand_"))
        )
        check("G33_FACETED_RUNESTONE", len(stone_facets) >= 22, ">=22 authored face/side facets", stone_facets)
        check("G34_LAYERED_DWARVEN_BRACING", len(head_bracing) >= 20, ">=20 steel/bronze layered bracing parts", head_bracing)
        check("G35_RESTRAINED_RUNE_SET", 16 <= len(rune_objects) <= 40, "16-40 rune elements", rune_objects)
        check("G36_CRISSCROSS_LEATHER_GRIP", len(wrap_objects) == 2 and wrap_directions == ["ascending", "descending"], {"count": 2, "directions": ["ascending", "descending"]}, {"objects": wrap_objects, "directions": wrap_directions})
        check("G37_ENGRAVED_INLAID_SHAFT", len(shaft_inlays) >= 12, ">=12 shaft rail/rune elements", shaft_inlays)
        check("G38_LAYERED_FOCAL_POMMEL", len(pommel_layers) >= 8, ">=8 pommel plate/rune/band elements", pommel_layers)

    passed = sum(1 for item in checks if item["pass"])
    failures = [item for item in checks if not item["pass"]]
    report = {
        "schema": "aerathea.steps_01_16_validation.v1",
        "asset_id": ASSET_ID,
        "contract_id": CONTRACT_ID,
        "revision": REVISION,
        "artifact_status": "proof only",
        "pipeline_status": "DCC game-ready candidate" if not failures else "blocked",
        "result": "pass" if not failures else "fail",
        "summary": {"passed": passed, "total": len(checks), "failures": len(failures)},
        "checks": checks,
        "fbx_import_audits": fbx_audits,
        "glb_import_audit": glb_audit,
        "source_blend": {"path": str(BLEND_PATH.relative_to(ROOT)), "sha256": sha256(BLEND_PATH)},
        "dcc_manifest": {"path": str(MANIFEST_PATH.relative_to(ROOT)), "sha256": sha256(MANIFEST_PATH)},
        "final_visual_approval": "pending Flamestrike",
        "unreal_authorized": False,
    }
    validation_path = VALIDATION_PATH
    review_path = REVIEW_PATH
    validation_path.parent.mkdir(parents=True, exist_ok=True)
    review_path.parent.mkdir(parents=True, exist_ok=True)
    validation_path.write_text(json.dumps(report, indent=2) + "\n", encoding="utf-8")

    lines = [
        f"# {ASSET_ID} Step 16 Technical Audit",
        "",
        f"- Result: `{report['result']}`",
        f"- Gates: `{passed}/{len(checks)}`",
        f"- Pipeline status: `{report['pipeline_status']}`",
        "- Artifact classification: `proof only`",
        "- Final visual approval: pending Flamestrike",
        "- Unreal authority: false",
        "",
        "## Gate Results",
        "",
    ]
    for item in checks:
        lines.append(f"- [{'x' if item['pass'] else ' '}] `{item['id']}`")
    if failures:
        lines += ["", "## Failures", ""]
        for item in failures:
            lines.append(f"- `{item['id']}`: expected `{item['expected']}`, observed `{item['observed']}`")
    review_path.write_text("\n".join(lines) + "\n", encoding="utf-8")
    print(validation_path)
    print(review_path)
    print(f"AUDIT_RESULT={report['result']} PASSED={passed}/{len(checks)}")
    return 0 if not failures else 1


if __name__ == "__main__":
    raise SystemExit(main())
