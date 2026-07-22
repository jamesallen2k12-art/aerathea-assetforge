#!/usr/bin/env python3
"""Independent, fail-closed Blender audit for Siege Breaker A05."""

from __future__ import annotations

import hashlib
import json
from pathlib import Path

import bmesh
import bpy
import numpy as np
from mathutils import Vector


ROOT = Path(bpy.path.abspath("//")).parents[5]
ASSET_ID = "SM_DRW_SiegeBreaker_Hammer_A01"
EXPORT_DIR = ROOT / "SourceAssets/Exports/Weapons/Dwarven/SM_DRW_SiegeBreaker_Hammer_A01/OrthographicVolumetric_A05"
TEXTURE_DIR = ROOT / "SourceAssets/Textures/Weapons/Dwarven/SM_DRW_SiegeBreaker_Hammer_A01/OrthographicVolumetric_A05"
PROOF_DIR = ROOT / "SourceAssets/Proofs/Weapons/Dwarven/SM_DRW_SiegeBreaker_Hammer_A01/OrthographicVolumetric_A05"
MANIFEST = ROOT / "docs/assets/blueprints/SM_DRW_SiegeBreaker_Hammer_A01/manifests/VISUAL_FIDELITY_A05_TECHNICAL_AUDIT.json"
REPORT = ROOT / "docs/assets/blueprints/SM_DRW_SiegeBreaker_Hammer_A01/review/VISUAL_FIDELITY_A05_TECHNICAL_AUDIT.md"


def sha256(path: Path) -> str:
    digest = hashlib.sha256()
    with path.open("rb") as handle:
        for chunk in iter(lambda: handle.read(1024 * 1024), b""):
            digest.update(chunk)
    return digest.hexdigest()


def evaluated_points(obj):
    depsgraph = bpy.context.evaluated_depsgraph_get()
    evaluated = obj.evaluated_get(depsgraph)
    mesh = evaluated.to_mesh()
    try:
        return [obj.matrix_world @ vertex.co for vertex in mesh.vertices]
    finally:
        evaluated.to_mesh_clear()


def bounds(objects):
    points = []
    for obj in objects:
        points.extend(evaluated_points(obj))
    if not points:
        raise RuntimeError("Cannot audit empty object set")
    minimum = [min(point[index] for point in points) for index in range(3)]
    maximum = [max(point[index] for point in points) for index in range(3)]
    return {
        "minimum_cm": [value * 100.0 for value in minimum],
        "maximum_cm": [value * 100.0 for value in maximum],
        "extent_cm": [(maximum[index] - minimum[index]) * 100.0 for index in range(3)],
        "center_cm": [((maximum[index] + minimum[index]) / 2.0) * 100.0 for index in range(3)],
    }


def triangles(obj):
    return sum(len(polygon.vertices) - 2 for polygon in obj.data.polygons)


def nonmanifold_edges(obj):
    mesh = bmesh.new()
    mesh.from_mesh(obj.data)
    try:
        return sum(1 for edge in mesh.edges if not edge.is_manifold)
    finally:
        mesh.free()


def close(actual, expected, tolerance):
    if isinstance(expected, (list, tuple)):
        return all(abs(float(a) - float(e)) <= tolerance for a, e in zip(actual, expected))
    return abs(float(actual) - float(expected)) <= tolerance


def sample_texture(path: Path):
    image = bpy.data.images.load(str(path), check_existing=False)
    width, height = image.size
    buffer = np.empty(width * height * 4, dtype=np.float32)
    image.pixels.foreach_get(buffer)
    rgba = buffer.reshape((-1, 4))
    indices = np.linspace(0, len(rgba) - 1, min(4096, len(rgba)), dtype=np.int64)
    rgb = rgba[indices, :3]
    high = rgb.max(axis=1)
    low = rgb.min(axis=1)
    paper_samples = int(np.count_nonzero((rgb[:, 0] > 0.82) & (rgb[:, 1] > 0.80) & (rgb[:, 2] > 0.72) & ((high - low) < 0.12)))
    max_rgb = float(high.max())
    count = int(len(indices))
    bpy.data.images.remove(image)
    return {"size": [int(width), int(height)], "paper_like_samples": paper_samples, "samples": count, "max_rgb": max_rgb}


def add_check(checks, name, observed, expected, passed):
    checks.append({"name": name, "observed": observed, "expected": expected, "pass": bool(passed)})


def clear_objects():
    bpy.ops.object.select_all(action="SELECT")
    bpy.ops.object.delete(use_global=False)


def clean_import_fbx(path: Path):
    clear_objects()
    before = set(bpy.data.objects)
    bpy.ops.import_scene.fbx(filepath=str(path), use_image_search=False)
    meshes = [obj for obj in bpy.data.objects if obj not in before and obj.type == "MESH" and not obj.name.startswith("UCX_")]
    if not meshes:
        return {"pass": False, "reason": "no primary mesh"}
    primary = max(meshes, key=lambda obj: triangles(obj))
    return {"pass": True, "name": primary.name, "triangles": triangles(primary), "bounds": bounds([primary])}


def clean_import_glb(path: Path):
    clear_objects()
    before = set(bpy.data.objects)
    bpy.ops.import_scene.gltf(filepath=str(path))
    meshes = [obj for obj in bpy.data.objects if obj not in before and obj.type == "MESH"]
    if not meshes:
        return {"pass": False, "reason": "no mesh"}
    primary = max(meshes, key=lambda obj: triangles(obj))
    return {"pass": True, "name": primary.name, "triangles": triangles(primary), "bounds": bounds([primary])}


def main():
    checks = []
    source_collection = bpy.data.collections.get("A05_SOURCE_COMPONENTS")
    source = [obj for obj in source_collection.objects if obj.type == "MESH"] if source_collection else []
    add_check(checks, "source_component_count", len(source), ">= 20", len(source) >= 20)

    observed_bounds = bounds(source)
    add_check(checks, "overall_bounds_cm", observed_bounds["extent_cm"], [52.0, 32.0, 170.0], close(observed_bounds["extent_cm"], [52.0, 32.0, 170.0], 0.02))
    add_check(checks, "origin_bottom_cm", observed_bounds["minimum_cm"][2], 0.0, close(observed_bounds["minimum_cm"][2], 0.0, 0.02))

    by_name = {obj.name: obj for obj in source}
    required_primary = ("Head_Stone_Left", "Head_Stone_Right", "Head_Core_Body", "Shaft_Metal", "Grip_Leather_Core", "Pommel_Body")
    add_check(checks, "primary_components_present", sorted(name for name in required_primary if name in by_name), list(required_primary), all(name in by_name for name in required_primary))
    primary_bounds = {name: bounds([by_name[name]]) for name in required_primary if name in by_name}
    real_volume = {name: all(axis > 0.10 for axis in record["extent_cm"]) for name, record in primary_bounds.items()}
    add_check(checks, "primary_components_are_3d_volumes", real_volume, "all true", all(real_volume.values()) and len(real_volume) == len(required_primary))

    shaft = primary_bounds["Shaft_Metal"]
    grip_objects = [obj for obj in source if obj.name.startswith("Grip_Leather") or obj.name.startswith("Grip_Wrap")]
    grip = bounds(grip_objects)
    pommel = primary_bounds["Pommel_Body"]
    socket = bounds([by_name["Head_Socket"]])
    add_check(checks, "shaft_interval_cm", [shaft["minimum_cm"][2], shaft["maximum_cm"][2]], [14.0, 132.0], close([shaft["minimum_cm"][2], shaft["maximum_cm"][2]], [14.0, 132.0], 0.02))
    add_check(checks, "grip_interval_cm", [grip["minimum_cm"][2], grip["maximum_cm"][2]], [18.0, 60.0], close([grip["minimum_cm"][2], grip["maximum_cm"][2]], [18.0, 60.0], 0.02))
    add_check(checks, "pommel_interval_cm", [pommel["minimum_cm"][2], pommel["maximum_cm"][2]], [0.0, 18.0], close([pommel["minimum_cm"][2], pommel["maximum_cm"][2]], [0.0, 18.0], 0.02))
    add_check(checks, "shaft_clear_diameter_cm", shaft["extent_cm"][:2], [5.0, 5.0], close(shaft["extent_cm"][:2], [5.0, 5.0], 0.02))
    add_check(checks, "grip_outer_diameter_cm", grip["extent_cm"][:2], [5.0, 5.0], close(grip["extent_cm"][:2], [5.0, 5.0], 0.08))
    add_check(checks, "pommel_max_width_cm", pommel["extent_cm"][0], 11.0, close(pommel["extent_cm"][0], 11.0, 0.02))
    add_check(checks, "shaft_pommel_overlap_cm", pommel["maximum_cm"][2] - shaft["minimum_cm"][2], 4.0, close(pommel["maximum_cm"][2] - shaft["minimum_cm"][2], 4.0, 0.02))

    centers = {
        "socket": socket["center_cm"][:2],
        "shaft": shaft["center_cm"][:2],
        "grip": grip["center_cm"][:2],
        "pommel": pommel["center_cm"][:2],
    }
    deltas = {
        "socket_to_shaft": [abs(centers["socket"][i] - centers["shaft"][i]) for i in range(2)],
        "shaft_to_grip": [abs(centers["shaft"][i] - centers["grip"][i]) for i in range(2)],
        "grip_to_pommel": [abs(centers["grip"][i] - centers["pommel"][i]) for i in range(2)],
    }
    add_check(checks, "interface_center_deltas_cm", deltas, "each axis <= 0.05", all(value <= 0.05 for pair in deltas.values() for value in pair))

    missing_uv = [obj.name for obj in source if not obj.data.uv_layers]
    add_check(checks, "uv_unwrap", missing_uv, "none missing", not missing_uv)
    nonmanifold = {obj.name: nonmanifold_edges(obj) for obj in source}
    nonmanifold = {name: count for name, count in nonmanifold.items() if count}
    add_check(checks, "closed_manifold_source_meshes", nonmanifold, "zero non-manifold edges", not nonmanifold)

    material_names = sorted({material.name for obj in source for material in obj.data.materials if material})
    add_check(checks, "five_material_families", material_names, "5 A05 material families", len(material_names) == 5 and all(token in " ".join(material_names) for token in ("Stone", "Bronze", "Steel", "Leather", "Rune")))

    lod_names = [ASSET_ID + "_LOD0", ASSET_ID + "_LOD1", ASSET_ID + "_LOD2", ASSET_ID + "_LOD3"]
    lods = [bpy.data.objects.get(name) for name in lod_names]
    lod_counts = [triangles(obj) if obj else 0 for obj in lods]
    add_check(checks, "lod0_budget", lod_counts[0], "3000..8000 triangles", 3000 <= lod_counts[0] <= 8000)
    add_check(checks, "lod_triangle_reduction", lod_counts, "strictly descending LOD0..LOD3", all(lods) and all(lod_counts[index] > lod_counts[index + 1] for index in range(3)))
    lod0_slots = [material.name for material in lods[0].data.materials if material] if lods[0] else []
    add_check(checks, "lod0_material_slots", lod0_slots, "exactly 5 unique slots", len(lod0_slots) == 5 and len(set(lod0_slots)) == 5)

    collision = [obj for obj in bpy.data.objects if obj.name.startswith("UCX_" + ASSET_ID)]
    add_check(checks, "custom_collision_proxies", sorted(obj.name for obj in collision), "3 proxies", len(collision) == 3)

    forbidden_tokens = ("A03", "A04", "PixelReconstruction", "StrictScanline")
    lineage_strings = [obj.name for obj in source] + material_names
    lineage_strings.extend(image.filepath for image in bpy.data.images)
    forbidden_hits = sorted(value for value in lineage_strings if any(token in value for token in forbidden_tokens))
    add_check(checks, "a03_a04_construction_inputs", forbidden_hits, "zero", not forbidden_hits)

    texture_records = {}
    for family in ("Stone", "Bronze", "Steel", "Leather", "Rune"):
        for suffix in ("BC", "N", "ORM", "E"):
            path = TEXTURE_DIR / f"T_DRW_SiegeBreaker_Hammer_A01_{family}_{suffix}.png"
            key = f"{family}_{suffix}"
            if path.exists():
                sample = sample_texture(path)
                texture_records[key] = {"path": str(path.relative_to(ROOT)), "sha256": sha256(path), **sample}
            else:
                texture_records[key] = {"missing": True}
    add_check(checks, "twenty_2k_texture_maps", len(texture_records), "20 existing 2048x2048 maps", len(texture_records) == 20 and all(record.get("size") == [2048, 2048] for record in texture_records.values()))
    base_paper = {key: record["paper_like_samples"] for key, record in texture_records.items() if key.endswith("_BC") and record.get("paper_like_samples", 0)}
    add_check(checks, "base_color_background_contamination", base_paper, "zero paper-like samples", not base_paper)
    non_rune_emission = {key: record["max_rgb"] for key, record in texture_records.items() if key.endswith("_E") and not key.startswith("Rune") and record.get("max_rgb", 0.0) > 0.01}
    add_check(checks, "emissive_scope", non_rune_emission, "only Rune emits", not non_rune_emission and texture_records["Rune_E"].get("max_rgb", 0.0) > 0.1)

    export_paths = {
        "LOD0": EXPORT_DIR / f"{ASSET_ID}.fbx",
        "LOD1": EXPORT_DIR / f"{ASSET_ID}_LOD1.fbx",
        "LOD2": EXPORT_DIR / f"{ASSET_ID}_LOD2.fbx",
        "LOD3": EXPORT_DIR / f"{ASSET_ID}_LOD3.fbx",
        "GLB": EXPORT_DIR / f"{ASSET_ID}.glb",
    }
    export_records = {name: {"path": str(path.relative_to(ROOT)), "exists": path.exists(), "bytes": path.stat().st_size if path.exists() else 0, "sha256": sha256(path) if path.exists() else None} for name, path in export_paths.items()}
    add_check(checks, "production_exports", export_records, "4 FBX + 1 GLB nonempty", all(record["exists"] and record["bytes"] > 1024 for record in export_records.values()))

    render_paths = [PROOF_DIR / f"{ASSET_ID}_A05_{name}.png" for name in ("FRONT", "BACK", "LEFT", "RIGHT", "TOP", "BOTTOM", "BEAUTY")]
    render_paths.extend(PROOF_DIR / f"{ASSET_ID}_A05_PARALLAX_{index:02d}.png" for index in range(1, 6))
    render_hashes = {path.name: sha256(path) if path.exists() else None for path in render_paths}
    add_check(checks, "render_set", render_hashes, "12 existing renders", all(render_hashes.values()) and len(render_hashes) == 12)
    parallax_hashes = [render_hashes[f"{ASSET_ID}_A05_PARALLAX_{index:02d}.png"] for index in range(1, 6)]
    add_check(checks, "multi_angle_parallax", parallax_hashes, "5 unique observed images", None not in parallax_hashes and len(set(parallax_hashes)) == 5)

    # Clean imports are performed last because they replace the current scene.
    reimports = {}
    expected_counts = dict(zip(("LOD0", "LOD1", "LOD2", "LOD3"), lod_counts))
    for name in ("LOD0", "LOD1", "LOD2", "LOD3"):
        reimports[name] = clean_import_fbx(export_paths[name])
    reimports["GLB"] = clean_import_glb(export_paths["GLB"])
    reimport_ok = True
    for name in ("LOD0", "LOD1", "LOD2", "LOD3"):
        record = reimports[name]
        triangle_delta = abs(record.get("triangles", -1000000) - expected_counts[name])
        allowed_triangle_delta = max(2, int(round(expected_counts[name] * 0.002)))
        record["source_triangle_count"] = expected_counts[name]
        record["triangle_delta"] = triangle_delta
        record["allowed_triangle_delta"] = allowed_triangle_delta
        reimport_ok = reimport_ok and record.get("pass", False) and triangle_delta <= allowed_triangle_delta
        if record.get("pass"):
            reimport_ok = reimport_ok and close(record["bounds"]["extent_cm"], [52.0, 32.0, 170.0], 0.05)
    reimport_ok = reimport_ok and reimports["GLB"].get("pass", False) and reimports["GLB"].get("triangles") == expected_counts["LOD0"] and close(reimports["GLB"]["bounds"]["extent_cm"], [52.0, 32.0, 170.0], 0.05)
    add_check(checks, "clean_reimports", reimports, "triangles and bounds preserved", reimport_ok)

    passed = all(check["pass"] for check in checks)
    result = {
        "schema": "aerathea.siegebreaker_a05_independent_audit.v1",
        "asset_id": ASSET_ID,
        "contract_id": "SB-VF-A05-ORTHOGRAPHIC-VOLUMETRIC",
        "artifact_status": "proof only",
        "auditor": str(Path(__file__).relative_to(ROOT)),
        "builder_manifest_read": False,
        "status": "pass" if passed else "fail",
        "passed_checks": sum(1 for check in checks if check["pass"]),
        "total_checks": len(checks),
        "checks": checks,
        "texture_records": texture_records,
        "clean_reimports": reimports,
    }
    MANIFEST.parent.mkdir(parents=True, exist_ok=True)
    REPORT.parent.mkdir(parents=True, exist_ok=True)
    MANIFEST.write_text(json.dumps(result, indent=2) + "\n", encoding="utf-8")
    report_lines = [
        "# Siege Breaker A05 Independent Technical Audit",
        "",
        f"- Status: `{'pass' if passed else 'fail'}`",
        f"- Gates: `{result['passed_checks']}/{result['total_checks']}`",
        "- Artifact status: `proof only`",
        "- Builder manifest read: `false`",
        "- Unreal authority: `false`",
        "",
        "## Gate Results",
        "",
    ]
    report_lines.extend(f"- `{'PASS' if check['pass'] else 'FAIL'}` — {check['name']}: observed `{check['observed']}`; expected `{check['expected']}`" for check in checks)
    REPORT.write_text("\n".join(report_lines) + "\n", encoding="utf-8")
    print(json.dumps({"status": result["status"], "passed": result["passed_checks"], "total": result["total_checks"], "failed": [check["name"] for check in checks if not check["pass"]], "manifest": str(MANIFEST)}, indent=2))
    if not passed:
        raise SystemExit(2)


if __name__ == "__main__":
    main()
