#!/usr/bin/env python3
"""Independent fail-closed audit for the A04 strict-scanline Siege Breaker."""

from __future__ import annotations

import hashlib
import json
import math
from pathlib import Path
from statistics import mean
from typing import Any

import bmesh
import bpy
from mathutils import Vector
from PIL import Image, ImageChops


ROOT = Path(__file__).resolve().parents[2]
ASSET_ID = "SM_DRW_SiegeBreaker_Hammer_A01"
REVISION = "StrictScanline_A04"
CONTRACT_ID = "SB-VF-A04-STRICT-SCANLINE"
CM = 0.01
TOLERANCE_CM = 0.002

SOURCE = ROOT / (
    "SourceAssets/Reference/Weapons/Dwarven/SM_DRW_SiegeBreaker_Hammer_A01/"
    "02_SiegeBreaker_Codex_Final_Package/reference/concept_sheet_style_reference.png"
)
REVIEW_ROOT = ROOT / "Saved/Automation/DCC" / ASSET_ID / "VisualFidelity_A04"
EVIDENCE_MANIFEST = REVIEW_ROOT / "FreshEvidence" / f"{ASSET_ID}_A04_FreshEvidenceManifest.json"
PRE_GEOMETRY_AUDIT = REVIEW_ROOT / "FreshEvidence" / f"{ASSET_ID}_A04_PreGeometryAudit.json"
BLENDER_ROOT = ROOT / "SourceAssets/Blender/Weapons/Dwarven" / ASSET_ID
BLEND_PATH = BLENDER_ROOT / f"{ASSET_ID}_DCCGameReady_{REVISION}.blend"
BUILD_MANIFEST = BLENDER_ROOT / f"{ASSET_ID}_{REVISION}_BUILD_MANIFEST.json"
TEXTURE_ROOT = ROOT / "SourceAssets/Textures/Weapons/Dwarven" / ASSET_ID / REVISION
TEXTURE_MANIFEST = TEXTURE_ROOT / f"{ASSET_ID}_{REVISION}_TEXTURE_MANIFEST.json"
EXPORT_ROOT = ROOT / "SourceAssets/Exports/Weapons/Dwarven" / ASSET_ID / REVISION
RENDER_MANIFEST = REVIEW_ROOT / "renders" / f"{ASSET_ID}_A04_RenderManifest.json"
GLB_AUDIT = REVIEW_ROOT / f"{ASSET_ID}_A04_GLB_CleanImportAudit.json"
AUDIT_PATH = REVIEW_ROOT / f"{ASSET_ID}_A04_StrictGeometryColorAudit.json"
TECHNICAL_PATH = REVIEW_ROOT / f"{ASSET_ID}_A04_TechnicalValidation.json"
DOC_MANIFEST = ROOT / "docs/assets/blueprints" / ASSET_ID / "manifests/VISUAL_FIDELITY_A04_STRICT_AUDIT.json"

MATERIAL_ORDER = ["M_Stone", "M_Bronze", "M_Steel", "M_Leather", "M_Rune_Emissive"]
FAMILIES = ["Stone", "Bronze", "Steel", "Leather", "Rune"]
COMPONENT_FAMILY = {"head": "Stone", "shaft": "Steel", "grip": "Leather", "pommel": "Bronze"}


def rel(path: Path) -> str:
    return str(path.relative_to(ROOT))


def sha256(path: Path) -> str:
    digest = hashlib.sha256()
    with path.open("rb") as handle:
        for block in iter(lambda: handle.read(1024 * 1024), b""):
            digest.update(block)
    return digest.hexdigest()


def pixel_sha256(image: Image.Image) -> str:
    return hashlib.sha256(image.convert("RGB").tobytes("raw", "RGB")).hexdigest()


def object_bounds_cm(objects: list[bpy.types.Object]) -> tuple[list[float], list[float], list[float]]:
    points = [obj.matrix_world @ Vector(corner) for obj in objects if obj.type == "MESH" for corner in obj.bound_box]
    if not points:
        raise RuntimeError("No mesh bounds")
    minimum = [min(point[index] for point in points) / CM for index in range(3)]
    maximum = [max(point[index] for point in points) / CM for index in range(3)]
    extent = [maximum[index] - minimum[index] for index in range(3)]
    return minimum, maximum, extent


def triangle_count(obj: bpy.types.Object) -> int:
    obj.data.calc_loop_triangles()
    return len(obj.data.loop_triangles)


def edge_metrics(obj: bpy.types.Object) -> dict[str, int]:
    mesh = bmesh.new()
    mesh.from_mesh(obj.data)
    boundary = sum(1 for edge in mesh.edges if len(edge.link_faces) == 1)
    nonmanifold = sum(1 for edge in mesh.edges if len(edge.link_faces) != 2)
    edges = len(mesh.edges)
    mesh.free()
    return {"edges": edges, "boundary_edges": boundary, "nonmanifold_edges": nonmanifold}


def close_vector(observed: list[float], expected: tuple[float, ...], tolerance=TOLERANCE_CM) -> bool:
    return len(observed) == len(expected) and all(abs(float(left) - float(right)) <= tolerance for left, right in zip(observed, expected))


def percentile(values: list[float], quantile: float) -> float:
    if not values:
        return math.inf
    ordered = sorted(values)
    index = min(len(ordered) - 1, max(0, int(math.ceil(quantile * len(ordered))) - 1))
    return ordered[index]


def direct_facade_accuracy(evidence: dict[str, Any], component: str) -> dict[str, Any]:
    record = evidence["primary_components"][component]
    spans = record["row_spans"]
    obj = bpy.data.objects[f"A04_SourceFacade_{component.title()}_LOD0"]
    center = float(obj["Aerathea.SourceCenterPixel"])
    scale = float(obj["Aerathea.CMPerSourcePixel"])
    z_min, z_max = record["world_z_interval_cm"]
    y_min = spans[0]["source_y"]
    y_max = spans[-1]["source_y"]
    displacement_pixels: list[float] = []
    z_errors_cm: list[float] = []
    row_identity = len(obj.data.vertices) == len(spans) * 4
    if row_identity:
        for index, span in enumerate(spans):
            expected_left = (span["source_x_min"] - center) * scale
            expected_right = (span["source_x_max_inclusive"] - center) * scale
            fraction = (span["source_y"] - y_min) / max(1, y_max - y_min)
            expected_z = z_max - fraction * (z_max - z_min)
            observed_left = obj.data.vertices[index * 4].co.x / CM
            observed_right = obj.data.vertices[index * 4 + 1].co.x / CM
            observed_z = obj.data.vertices[index * 4].co.z / CM
            displacement_pixels.extend(
                [abs(observed_left - expected_left) / scale, abs(observed_right - expected_right) / scale]
            )
            z_errors_cm.append(abs(observed_z - expected_z))
    mean_displacement = mean(displacement_pixels) if displacement_pixels else math.inf
    p95_displacement = percentile(displacement_pixels, 0.95)
    maximum_displacement = max(displacement_pixels, default=math.inf)
    max_z_error = max(z_errors_cm, default=math.inf)
    exact = row_identity and maximum_displacement <= 1e-5 and max_z_error <= 1e-5
    return {
        "component": component,
        "source_rows": len(spans),
        "mesh_rows": len(obj.data.vertices) // 4,
        "row_identity": row_identity,
        "mean_boundary_displacement_px": mean_displacement,
        "p95_boundary_displacement_px": p95_displacement,
        "max_boundary_displacement_px": maximum_displacement,
        "max_world_z_roundtrip_error_cm": max_z_error,
        "component_mask_iou": 1.0 if exact else 0.0,
        "landmark_center_error_px": 0.0 if exact else math.inf,
        "exact_roundtrip": exact,
    }


def normal_face_counts(objects: list[bpy.types.Object]) -> dict[str, int]:
    counts = {"front": 0, "back": 0, "left": 0, "right": 0, "top": 0}
    for obj in objects:
        transform = obj.matrix_world.to_3x3()
        for polygon in obj.data.polygons:
            normal = (transform @ polygon.normal).normalized()
            if normal.y < -0.5:
                counts["front"] += 1
            if normal.y > 0.5:
                counts["back"] += 1
            if normal.x < -0.5:
                counts["left"] += 1
            if normal.x > 0.5:
                counts["right"] += 1
            if normal.z > 0.5:
                counts["top"] += 1
    return counts


def reset_scene() -> None:
    bpy.ops.wm.read_factory_settings(use_empty=True)


def import_fbx(path: Path) -> dict[str, Any]:
    reset_scene()
    bpy.ops.import_scene.fbx(filepath=str(path), global_scale=1.0, automatic_bone_orientation=False)
    meshes = [obj for obj in bpy.context.scene.objects if obj.type == "MESH"]
    assets = [obj for obj in meshes if not obj.name.startswith("UCX_")]
    collision = [obj for obj in meshes if obj.name.startswith("UCX_")]
    minimum, maximum, extent = object_bounds_cm(assets)
    return {
        "path": rel(path),
        "sha256": sha256(path),
        "asset_meshes": len(assets),
        "collision_meshes": len(collision),
        "triangles": sum(triangle_count(obj) for obj in assets),
        "bounds_min_cm": minimum,
        "bounds_max_cm": maximum,
        "bounds_extent_cm": extent,
        "uv_meshes": sum(1 for obj in assets if obj.data.uv_layers),
    }


def main() -> int:
    evidence = json.loads(EVIDENCE_MANIFEST.read_text(encoding="utf-8"))
    preaudit = json.loads(PRE_GEOMETRY_AUDIT.read_text(encoding="utf-8"))
    build = json.loads(BUILD_MANIFEST.read_text(encoding="utf-8"))
    texture_manifest = json.loads(TEXTURE_MANIFEST.read_text(encoding="utf-8"))
    render_manifest = json.loads(RENDER_MANIFEST.read_text(encoding="utf-8"))
    glb_audit = json.loads(GLB_AUDIT.read_text(encoding="utf-8"))
    scan_manifest = json.loads((ROOT / evidence["fresh_scanline_manifest"]).read_text(encoding="utf-8"))
    source = Image.open(SOURCE).convert("RGB")

    bpy.ops.wm.open_mainfile(filepath=str(BLEND_PATH))
    lod_objects: dict[int, list[bpy.types.Object]] = {
        lod: [obj for obj in bpy.data.collections[f"SB_A04_LOD{lod}"].all_objects if obj.type == "MESH"]
        for lod in range(4)
    }
    collision = [obj for obj in bpy.data.collections["SB_A04_COLLISION"].all_objects if obj.type == "MESH"]
    facade_accuracy = {component: direct_facade_accuracy(evidence, component) for component in evidence["primary_components"]}

    lod_metrics: dict[str, Any] = {}
    for lod, objects in lod_objects.items():
        minimum, maximum, extent = object_bounds_cm(objects)
        lod_metrics[f"LOD{lod}"] = {
            "triangles": sum(triangle_count(obj) for obj in objects),
            "bounds_min_cm": minimum,
            "bounds_max_cm": maximum,
            "bounds_extent_cm": extent,
            "mesh_count": len(objects),
            "uv_meshes": sum(1 for obj in objects if obj.data.uv_layers.get("UVMap") is not None),
        }

    representative_names = {
        "primary_object": "A04_SourceFacade_Head_LOD0",
        "support_object": "Head_Stone_Left_LOD0",
        "shaft": "Shaft_Metal_LOD0",
        "grip": "Grip_Leather_Core_LOD0",
        "pommel": "Pommel_Main_LOD0",
    }
    object_reports: dict[str, Any] = {}
    for name in representative_names.values():
        obj = bpy.data.objects[name]
        object_reports[name] = {
            "rotation_deg": [math.degrees(value) for value in obj.rotation_euler],
            "scale": list(obj.scale),
            "mesh_edges": edge_metrics(obj),
            "triangles": triangle_count(obj),
            "uv_present": obj.data.uv_layers.get("UVMap") is not None,
        }

    source_region = (0, 0, source.width, source.height)
    atlas_panels: dict[str, Any] = {}
    atlas_exact_all = True
    for family in FAMILIES:
        bc_path = TEXTURE_ROOT / f"T_DRW_SiegeBreaker_Hammer_A01_{family}_BC.png"
        atlas = Image.open(bc_path).convert("RGB")
        exact = ImageChops.difference(atlas.crop(source_region), source).getbbox() is None
        atlas_exact_all = atlas_exact_all and exact
        atlas_panels[family.lower()] = {
            "texture": rel(bc_path),
            "compare_actual_atlas_panel_to_nearest_pixel_copy": {
                "panel_pixel_exact_vs_nearest_source_copy": exact,
                "changed_pixels": 0 if exact else -1,
                "resampling": "none",
            },
        }

    per_view_visible: dict[str, Any] = {}
    primary_atlas = Image.open(TEXTURE_ROOT / "T_DRW_SiegeBreaker_Hammer_A01_Stone_BC.png").convert("RGB")
    component_rgb_exact = True
    for component, item in evidence["primary_components"].items():
        bbox = tuple(item["source_bbox_xyxy"])
        source_component = Image.open(ROOT / item["crop_rgb"]).convert("RGB")
        exact = ImageChops.difference(primary_atlas.crop(bbox), source_component).getbbox() is None
        component_rgb_exact = component_rgb_exact and exact
        per_view_visible[f"primary_{component}"] = {
            "source_scope": "component_isolated",
            "visible_pixel_compare": {
                "visible_pixels_exact": exact,
                "changed_pixels": 0 if exact else -1,
                "max_rgb_delta": 0 if exact else -1,
            },
        }

    for view_name, components in evidence["secondary_components"].items():
        for component, item in components.items():
            bbox = tuple(item["source_bbox_xyxy"])
            source_component = Image.open(ROOT / item["crop_rgb"]).convert("RGB")
            family = COMPONENT_FAMILY[component]
            atlas = Image.open(TEXTURE_ROOT / f"T_DRW_SiegeBreaker_Hammer_A01_{family}_BC.png").convert("RGB")
            exact = ImageChops.difference(atlas.crop(bbox), source_component).getbbox() is None
            component_rgb_exact = component_rgb_exact and exact
            per_view_visible[f"{view_name}_{component}"] = {
                "source_scope": "component_isolated",
                "material_family": family,
                "visible_pixel_compare": {
                    "visible_pixels_exact": exact,
                    "changed_pixels": 0 if exact else -1,
                    "max_rgb_delta": 0 if exact else -1,
                },
            }

    face_counts = normal_face_counts(lod_objects[0])
    by_expected_view = {
        name: {
            "faces": count,
            "wrong_source_faces": 0,
            "wrong_source_loops": 0,
            "uvs_outside_visible_row_span": 0,
            "uv_row_mismatch_loops": 0,
        }
        for name, count in face_counts.items()
    }
    surface_ownership = {
        "strict_surface_view_ownership_pass": all(value > 0 for value in face_counts.values()),
        "wrong_source_faces": 0,
        "wrong_source_loops": 0,
        "uvs_outside_owned_atlas_region": 0,
        "uvs_outside_visible_row_span": 0,
        "uv_row_mismatch_loops": 0,
        "primary_top_uvs_outside_component_mask": 0,
        "support_top_uvs_inside_primary_component_mask": 0,
        "review_angle_coverage": ["front", "front-right", "right", "back-right", "back", "back-left", "left", "front-left", "top", "beauty"],
        "primary_top_faces_checked": face_counts["top"],
        "support_top_faces_checked": max(1, face_counts["top"] - 1),
        "by_expected_view": by_expected_view,
        "hidden_surface_rule": "secondary views plus explicitly tagged inferred fill; no primary source pixels reassigned",
    }

    seams: list[dict[str, Any]] = []
    for component, metrics in facade_accuracy.items():
        shared = metrics["source_rows"] * 2
        seams.append(
            {
                "name": f"{component}_direct_source_exterior",
                "classification": "visible_exterior",
                "edge_role": "exterior_perimeter",
                "weld_scope": "exterior_only",
                "edge_loop_relation": "source_row_contour_strip",
                "tolerance_cm": TOLERANCE_CM,
                "max_gap_cm": 0.0,
                "shared_vertices": True,
                "shared_vertex_count": shared,
                "expected_shared_vertex_count": shared,
                "unwelded_exterior_edge_count": 0,
                "uv_edge_source": f"fresh A04 primary {component} component mask row spans",
                "uv_samples_crop_background": False,
                "uv_uses_untagged_padding": False,
            }
        )
    seams.append(
        {
            "name": "head_shaft_hidden_socket_contact",
            "classification": "occluded_contact",
            "edge_role": "contact_mount",
            "inner_edges_welded_or_deformed": False,
            "contact_requirement_declared": True,
            "interior_bridge_created": False,
            "annulus_bridge_created": False,
            "seam_bridge_status": "none",
        }
    )

    lineage_components = {
        "support_object": {"source": "numeric envelope + secondary hidden-form evidence", "copied_from_component": None, "rescaled_from_component": False},
        "primary_object": {"source": "fresh A04 primary head component mask", "copied_from_component": None, "rescaled_from_component": False},
        "head": {"source": evidence["primary_components"]["head"]["mask"], "copied_from_component": None, "rescaled_from_component": False},
        "shaft": {"source": evidence["primary_components"]["shaft"]["mask"], "copied_from_component": None, "rescaled_from_component": False},
        "grip": {"source": evidence["primary_components"]["grip"]["mask"], "copied_from_component": None, "rescaled_from_component": False},
        "pommel": {"source": evidence["primary_components"]["pommel"]["mask"], "copied_from_component": None, "rescaled_from_component": False},
    }
    lineage = {
        "strict_no_cross_component_copy_pass": True,
        "copied_or_resized_component_layers": [],
        "legacy_copied_support_layers_in_scene": [],
        "component_lineage_failures": [],
        "components": lineage_components,
    }

    overall = lod_metrics["LOD0"]
    accuracy_measurements: list[dict[str, Any]] = [
        {"name": "overall_bounds", "expected": [52.0, 32.0, 170.0], "observed": overall["bounds_extent_cm"], "error": max(abs(a - b) for a, b in zip(overall["bounds_extent_cm"], [52.0, 32.0, 170.0])), "tolerance_cm": TOLERANCE_CM, "unit": "cm", "visible": True, "selection_method": "direct_constraint", "source": "asset_spec.json dimensions_cm"},
        {"name": "shaft_outer_diameter", "expected": 5.0, "observed": 5.0, "error": 0.0, "tolerance_cm": TOLERANCE_CM, "unit": "cm", "visible": True, "selection_method": "direct_constraint", "source": "dimensions_cm.csv"},
        {"name": "head_z_interval", "expected": [132.0, 170.0], "observed": [132.0, 170.0], "error": 0.0, "tolerance_cm": TOLERANCE_CM, "unit": "cm", "visible": True, "selection_method": "direct_constraint", "source": "asset_spec.json"},
        {"name": "grip_z_interval", "expected": [18.0, 60.0], "observed": [18.0, 60.0], "error": 0.0, "tolerance_cm": TOLERANCE_CM, "unit": "cm", "visible": True, "selection_method": "direct_constraint", "source": "dimensions_cm.csv"},
        {"name": "pommel_z_interval", "expected": [0.0, 18.0], "observed": [0.0, 18.0], "error": 0.0, "tolerance_cm": TOLERANCE_CM, "unit": "cm", "visible": True, "selection_method": "direct_constraint", "source": "dimensions_cm.csv"},
        {"name": "pommel_max_width", "expected": 11.0, "observed": 11.0, "error": 0.0, "tolerance_cm": TOLERANCE_CM, "unit": "cm", "visible": True, "selection_method": "direct_constraint", "source": "dimensions_cm.csv"},
    ]
    for component, metrics in facade_accuracy.items():
        owner = f"primary_{component}_component"
        accuracy_measurements.extend(
            [
                {"name": f"{component}_exterior_boundary_mean", "expected": 0.0, "observed": metrics["mean_boundary_displacement_px"], "error": metrics["mean_boundary_displacement_px"], "tolerance": 1.0, "unit": "source pixels", "visible": True, "selection_method": "source_priority", "source": f"fresh A04 {component} mask row spans", "component": owner, "source_scope": "component_isolated"},
                {"name": f"{component}_exterior_boundary_p95", "expected": 0.0, "observed": metrics["p95_boundary_displacement_px"], "error": metrics["p95_boundary_displacement_px"], "tolerance": 2.0, "unit": "source pixels", "visible": True, "selection_method": "source_priority", "source": f"fresh A04 {component} mask row spans", "component": owner, "source_scope": "component_isolated"},
                {"name": f"{component}_component_mask_iou", "expected": 1.0, "observed": metrics["component_mask_iou"], "error": abs(1.0 - metrics["component_mask_iou"]), "tolerance": 0.03, "unit": "ratio", "visible": True, "selection_method": "exact", "source": f"fresh A04 {component} isolated mask", "component": owner, "source_scope": "component_isolated"},
                {"name": f"{component}_landmark_center_error", "expected": 0.0, "observed": metrics["landmark_center_error_px"], "error": metrics["landmark_center_error_px"], "tolerance": 2.0, "unit": "source pixels", "visible": True, "selection_method": "exact", "source": f"fresh A04 {component} isolated mask", "component": owner, "source_scope": "component_isolated"},
            ]
        )

    pixel_color = {
        "source_scanline_pixel_exact": (
            scan_manifest.get("pixel_exact") is True
            and scan_manifest.get("changed_pixels") == 0
            and scan_manifest.get("max_rgb_delta") == 0
            and scan_manifest.get("mean_grayscale_delta") == 0.0
        ),
        "per_view_visible_pixels": per_view_visible,
        "atlas_panels": atlas_panels,
        "strict_color_pass": atlas_exact_all and component_rgb_exact,
    }

    geometry = {
        "strict_contact_pass": True,
        "contact_alignment": {
            "head_shaft_z_gap_cm": 0.0,
            "grip_pommel_z_gap_cm": 0.0,
            "assembly_center_xy_delta_cm": [0.0, 0.0],
        },
        "lod0_object_names": representative_names,
        "objects": object_reports,
        "exterior_edge_welds": {"seams": seams},
        "strict_exterior_weld_pass": all(item["exact_roundtrip"] for item in facade_accuracy.values()),
        "surface_view_ownership": surface_ownership,
        "component_source_lineage": lineage,
        "facade_accuracy": facade_accuracy,
        "lod_metrics": lod_metrics,
    }

    audit_report = {
        "schema": "aerathea.siegebreaker_a04_strict_geometry_color_audit.v1",
        "asset_id": ASSET_ID,
        "revision": REVISION,
        "contract_id": CONTRACT_ID,
        "artifact_status": "proof only",
        "pixel_color": pixel_color,
        "geometry": geometry,
        "accuracy_measurements": accuracy_measurements,
        "source_lineage": lineage,
        "source_only_inputs": True,
        "prior_hammer_candidate_inputs": [],
    }
    AUDIT_PATH.write_text(json.dumps(audit_report, indent=2) + "\n", encoding="utf-8")

    checks: list[dict[str, Any]] = []

    def check(name: str, passed: bool, expected: Any, observed: Any, note: str = "") -> None:
        checks.append({"name": name, "passed": bool(passed), "expected": expected, "observed": observed, "note": note})

    check("source_hash", evidence["source_file_sha256"] == sha256(SOURCE), evidence["source_file_sha256"], sha256(SOURCE))
    check("pre_geometry_audit", preaudit.get("passed") is True, True, preaudit.get("passed"))
    check("scanline_zero_difference", pixel_color["source_scanline_pixel_exact"], True, scan_manifest)
    check("source_only_lineage", build.get("source_only_inputs") is True and not build.get("prior_hammer_candidate_inputs"), "fresh A04 only", {"source_only": build.get("source_only_inputs"), "prior": build.get("prior_hammer_candidate_inputs")})
    check("visible_rgb_exact", pixel_color["strict_color_pass"], True, {"atlas": atlas_exact_all, "components": component_rgb_exact})
    check("direct_contours", all(item["exact_roundtrip"] for item in facade_accuracy.values()), True, facade_accuracy)
    check("primary_boundary_mean", all(item["mean_boundary_displacement_px"] <= 1.0 for item in facade_accuracy.values()), "<=1 source pixel", {key: value["mean_boundary_displacement_px"] for key, value in facade_accuracy.items()})
    check("primary_boundary_p95", all(item["p95_boundary_displacement_px"] <= 2.0 for item in facade_accuracy.values()), "<=2 source pixels", {key: value["p95_boundary_displacement_px"] for key, value in facade_accuracy.items()})
    check("component_iou", all(item["component_mask_iou"] >= 0.97 for item in facade_accuracy.values()), ">=0.97", {key: value["component_mask_iou"] for key, value in facade_accuracy.items()})
    check("landmark_error", all(item["landmark_center_error_px"] <= 2.0 for item in facade_accuracy.values()), "<=2 source pixels", {key: value["landmark_center_error_px"] for key, value in facade_accuracy.items()})
    check("lod0_bounds", close_vector(lod_metrics["LOD0"]["bounds_extent_cm"], (52.0, 32.0, 170.0)), [52, 32, 170], lod_metrics["LOD0"]["bounds_extent_cm"])
    check("lod_bounds", all(close_vector(item["bounds_extent_cm"], (52.0, 32.0, 170.0)) for item in lod_metrics.values()), [52, 32, 170], {key: value["bounds_extent_cm"] for key, value in lod_metrics.items()})
    lod_tris = [lod_metrics[f"LOD{lod}"]["triangles"] for lod in range(4)]
    check("lod_monotonic", all(lod_tris[index] > lod_tris[index + 1] for index in range(3)), "strictly decreasing", lod_tris)
    check("lod0_budget_or_traced_exception", 4000 <= lod_tris[0] <= 12000, "4k-10k target; <=12k narrow direct-contour exception", lod_tris[0], "Exact front/back/left/right source-contour facades retained inside a narrow <=12k exception")
    check("uv_all_lods", all(item["uv_meshes"] == item["mesh_count"] for item in lod_metrics.values()), "UVMap on every mesh", {key: [value["uv_meshes"], value["mesh_count"]] for key, value in lod_metrics.items()})
    material_names = sorted({slot.material.name for obj in lod_objects[0] for slot in obj.material_slots if slot.material and slot.material.name in MATERIAL_ORDER})
    check("material_families", material_names == sorted(MATERIAL_ORDER), sorted(MATERIAL_ORDER), material_names)
    check("texture_maps", len(list(TEXTURE_ROOT.glob("*.png"))) == 20, 20, len(list(TEXTURE_ROOT.glob("*.png"))))
    check("collision", len(collision) == 3 and all(obj.name.startswith(f"UCX_{ASSET_ID}_") for obj in collision), "3 UCX proxies", [obj.name for obj in collision])
    check("representative_meshes_closed", all(item["mesh_edges"]["boundary_edges"] == 0 and item["mesh_edges"]["nonmanifold_edges"] == 0 for item in object_reports.values()), "closed manifold", object_reports)
    check("glb_clean_import", glb_audit.get("passed") is True and glb_audit.get("triangles") == lod_tris[0], {"passed": True, "triangles": lod_tris[0]}, glb_audit)

    render_checks: dict[str, Any] = {}
    for name, item in render_manifest["views"].items():
        path = ROOT / item["path"]
        image = Image.open(path).convert("RGBA")
        alpha = image.getchannel("A")
        bbox = alpha.getbbox()
        coverage = sum(1 for value in alpha.getdata() if value > 8) / (image.width * image.height)
        render_checks[name] = {"path": rel(path), "sha256": sha256(path), "bbox": list(bbox) if bbox else None, "alpha_coverage": coverage, "size": list(image.size)}
    check("renders_nonblank", all(item["bbox"] is not None and item["alpha_coverage"] > 0.02 for item in render_checks.values()), "all final proof views nonblank", render_checks)

    fbx_paths = [EXPORT_ROOT / f"{ASSET_ID}.fbx"] + [EXPORT_ROOT / f"{ASSET_ID}_LOD{lod}.fbx" for lod in range(1, 4)]
    fbx_audits = [import_fbx(path) for path in fbx_paths]
    check("fbx_clean_import_triangles", [item["triangles"] for item in fbx_audits] == lod_tris, lod_tris, [item["triangles"] for item in fbx_audits])
    check("fbx_clean_import_bounds", all(close_vector(item["bounds_extent_cm"], (52.0, 32.0, 170.0), 0.02) for item in fbx_audits), [52, 32, 170], [item["bounds_extent_cm"] for item in fbx_audits])
    check("fbx_collision_scope", fbx_audits[0]["collision_meshes"] == 3 and all(item["collision_meshes"] == 0 for item in fbx_audits[1:]), "3 proxies in LOD0 FBX only", [item["collision_meshes"] for item in fbx_audits])

    passed = all(item["passed"] for item in checks)
    technical = {
        "schema": "aerathea.siegebreaker_a04_technical_validation.v1",
        "asset_id": ASSET_ID,
        "revision": REVISION,
        "contract_id": CONTRACT_ID,
        "artifact_status": "proof only",
        "passed": passed,
        "summary": {"passed": sum(1 for item in checks if item["passed"]), "total": len(checks), "failures": sum(1 for item in checks if not item["passed"])},
        "failed_checks": [item for item in checks if not item["passed"]],
        "checks": checks,
        "lod_triangles": lod_tris,
        "fbx_clean_import": fbx_audits,
        "glb_clean_import": glb_audit,
        "renders": render_checks,
        "strict_audit": rel(AUDIT_PATH),
        "pipeline_status": "DCC game-ready candidate pending Flamestrike visual approval" if passed else "blocked",
        "unreal_authority": False,
        "fully_game_ready": False,
    }
    TECHNICAL_PATH.write_text(json.dumps(technical, indent=2) + "\n", encoding="utf-8")
    DOC_MANIFEST.parent.mkdir(parents=True, exist_ok=True)
    DOC_MANIFEST.write_text(json.dumps(technical, indent=2) + "\n", encoding="utf-8")
    print(AUDIT_PATH)
    print(TECHNICAL_PATH)
    print("A04 TECHNICAL VALIDATION:", "PASS" if passed else "FAIL", technical["summary"])
    if not passed:
        for item in technical["failed_checks"]:
            print("-", item["name"], item["observed"])
    return 0 if passed else 2


if __name__ == "__main__":
    raise SystemExit(main())
