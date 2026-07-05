#!/usr/bin/env python3
"""Build the A001 DCC source candidate geometry proof.

Run with Blender:
    blender --background --python Tools/DCC/build_bloodaxe_cairnstone_a001_dcc_geometry_proof.py

This creates a measured geometry proof from approved A001 manifests only:
- no UVs
- no source textures
- no FBX/export
- no beauty render
- no old A02/A23/A26 generator logic
- no exterior weld/patch/stretch fix
"""

from __future__ import annotations

import json
import math
from pathlib import Path
from typing import Any

import bpy
from mathutils import Vector


ROOT = Path(__file__).resolve().parents[2]
ASSET_NAME = "SM_GIA_BloodAxeCairnstone_A001"
PROOF_NAME = f"{ASSET_NAME}_DCCGeometryProof"
OUT_DIR = ROOT / "Saved/Automation/DCC" / ASSET_NAME
GEOMETRY_PROOF_DIR = OUT_DIR / "GeometryProof"
BLEND_DIR = ROOT / "SourceAssets/Blender/Props/Giants/BloodAxe/Cairns" / PROOF_NAME
BLEND_PATH = BLEND_DIR / f"{PROOF_NAME}.blend"

PLAN_MANIFEST = OUT_DIR / f"{ASSET_NAME}_A001GeometryConstructionPlanManifest.json"
PREGEOMETRY_AUDIT_MANIFEST = OUT_DIR / f"{ASSET_NAME}_A001PreGeometryHardAuditManifest.json"
FORMULA_AUTHORITY_MANIFEST = OUT_DIR / f"{ASSET_NAME}_A001FormulaAuthorityManifest.json"
SURFACE_MARKER_MANIFEST = OUT_DIR / f"{ASSET_NAME}_A001SurfaceEdgeMarkerManifest.json"
OVAL_APPROVAL_MANIFEST = OUT_DIR / f"{ASSET_NAME}_A001OvalFootprintApprovalManifest.json"
LAYERED_CONTACT_APPROVAL_MANIFEST = OUT_DIR / f"{ASSET_NAME}_A001LayeredContactFormulaApprovalManifest.json"

PLAN_APPROVAL_MANIFEST = OUT_DIR / f"{ASSET_NAME}_A001GeometryConstructionPlanApprovalManifest.json"
GEOMETRY_MANIFEST = OUT_DIR / f"{ASSET_NAME}_A001DCCGeometryProofManifest.json"
SOURCE_IMAGE = ROOT / "docs/assets/reference/bloodaxe_cairnstone_asset/REF_GIA_BloodAxeCairnstoneAsset_A02_BlueprintTemplate.png"

RENDER_PATHS = {
    "front": GEOMETRY_PROOF_DIR / f"{PROOF_NAME}_FrontGeometryProof.png",
    "back": GEOMETRY_PROOF_DIR / f"{PROOF_NAME}_BackGeometryProof.png",
    "left": GEOMETRY_PROOF_DIR / f"{PROOF_NAME}_LeftGeometryProof.png",
    "right": GEOMETRY_PROOF_DIR / f"{PROOF_NAME}_RightGeometryProof.png",
    "top": GEOMETRY_PROOF_DIR / f"{PROOF_NAME}_TopGeometryProof.png",
    "angle": GEOMETRY_PROOF_DIR / f"{PROOF_NAME}_AngleGeometryProof.png",
}


def read_json(path: Path) -> dict[str, Any]:
    return json.loads(path.read_text())


def require_inputs() -> dict[str, dict[str, Any]]:
    paths = {
        "plan": PLAN_MANIFEST,
        "pregeometry_audit": PREGEOMETRY_AUDIT_MANIFEST,
        "formula_authority": FORMULA_AUTHORITY_MANIFEST,
        "surface_markers": SURFACE_MARKER_MANIFEST,
        "oval_approval": OVAL_APPROVAL_MANIFEST,
        "layered_contact_approval": LAYERED_CONTACT_APPROVAL_MANIFEST,
    }
    missing = [str(path) for path in paths.values() if not path.exists()]
    if missing:
        raise SystemExit("Missing geometry proof input manifest(s):\n" + "\n".join(missing))
    manifests = {name: read_json(path) for name, path in paths.items()}
    if manifests["pregeometry_audit"].get("gate_status") != "passed":
        raise SystemExit("Pre-geometry hard audit is not passed.")
    plan = manifests["plan"]
    if plan.get("approval_status") != "pending_Flamestrike_review":
        raise SystemExit("Unexpected plan approval status; refusing to infer approval state.")
    return manifests


def write_plan_approval(plan: dict[str, Any]) -> None:
    approval = {
        "asset": ASSET_NAME,
        "status": "A001 geometry construction plan approved for DCC source candidate geometry proof",
        "geometry_construction_plan_manifest": str(PLAN_MANIFEST.relative_to(ROOT)),
        "approval_source": "Flamestrike approved the A001 Geometry Construction Plan in conversation.",
        "approved_scope": {
            "allowed": "DCC source candidate geometry proof",
            "uv_generation": False,
            "texture_generation": False,
            "fbx_export": False,
            "unreal_import": False,
            "beauty_render": False,
            "fully_game_ready": False,
        },
        "plan_status_at_approval": plan.get("status"),
    }
    PLAN_APPROVAL_MANIFEST.write_text(json.dumps(approval, indent=2) + "\n")


def material(name: str, color: tuple[float, float, float, float]) -> bpy.types.Material:
    mat = bpy.data.materials.new(name)
    mat.diffuse_color = color
    return mat


def clear_scene() -> None:
    bpy.ops.object.select_all(action="SELECT")
    bpy.ops.object.delete()


def make_mesh(name: str, verts: list[tuple[float, float, float]], faces: list[tuple[int, ...]], mat: bpy.types.Material) -> bpy.types.Object:
    mesh = bpy.data.meshes.new(name)
    mesh.from_pydata(verts, [], faces)
    mesh.update()
    obj = bpy.data.objects.new(name, mesh)
    bpy.context.collection.objects.link(obj)
    obj.data.materials.append(mat)
    obj["Aerathea.Asset"] = ASSET_NAME
    obj["Aerathea.A001GeometryProof"] = True
    obj["Aerathea.NoUVsGenerated"] = True
    obj["Aerathea.NoTextureGenerated"] = True
    obj["Aerathea.NotGameReady"] = True
    return obj


def make_panel(name: str, verts: list[tuple[float, float, float]], mat: bpy.types.Material, component: str, source_view: str) -> bpy.types.Object:
    obj = make_mesh(name, verts, [(0, 1, 2, 3)], mat)
    obj["Aerathea.Component"] = component
    obj["Aerathea.SourceView"] = source_view
    obj["Aerathea.GeometryProofPanel"] = True
    return obj


def ellipse_cap(name: str, width: float, depth: float, z: float, mat: bpy.types.Material, component: str, segments: int = 64) -> bpy.types.Object:
    verts = [(0.0, 0.0, z)]
    for index in range(segments):
        angle = math.tau * index / segments
        verts.append((math.cos(angle) * width / 2.0, math.sin(angle) * depth / 2.0, z))
    faces = []
    for index in range(1, segments + 1):
        nxt = 1 if index == segments else index + 1
        faces.append((0, index, nxt))
    obj = make_mesh(name, verts, faces, mat)
    obj["Aerathea.Component"] = component
    obj["Aerathea.ApprovedMeasuredOvalEnvelope"] = True
    return obj


def make_curve_line(name: str, points: list[tuple[float, float, float]], mat: bpy.types.Material, bevel_depth: float = 0.65) -> bpy.types.Object:
    curve = bpy.data.curves.new(name, "CURVE")
    curve.dimensions = "3D"
    curve.resolution_u = 1
    curve.bevel_depth = bevel_depth
    curve.bevel_resolution = 2
    spline = curve.splines.new("POLY")
    spline.points.add(len(points) - 1)
    for point, coords in zip(spline.points, points):
        point.co = (coords[0], coords[1], coords[2], 1.0)
    obj = bpy.data.objects.new(name, curve)
    bpy.context.collection.objects.link(obj)
    obj.data.materials.append(mat)
    obj["Aerathea.GeometryProofMarker"] = True
    return obj


def line_rect(name: str, width: float, depth: float, z: float, mat: bpy.types.Material) -> None:
    pts = [
        (-width / 2, -depth / 2, z),
        (width / 2, -depth / 2, z),
        (width / 2, depth / 2, z),
        (-width / 2, depth / 2, z),
        (-width / 2, -depth / 2, z),
    ]
    make_curve_line(name, pts, mat, bevel_depth=0.45)


def span_cm(line: list[int], cm_per_px: list[float]) -> float:
    return abs(int(line[2]) - int(line[0])) * float(cm_per_px[0])


def dimensions_from_contacts(layered: dict[str, Any]) -> dict[str, Any]:
    by_view = {
        str(record["source_view"]): record
        for record in layered.get("approved_intervals", [])
        if isinstance(record, dict)
    }
    front = by_view["front"]
    back = by_view["back"]
    left = by_view["left"]
    right = by_view["right"]
    return {
        "front_top_width": span_cm(front["upper_ring_top_contact"]["pixel_line"], front["cm_per_pixel"]),
        "front_bottom_width": span_cm(front["upper_ring_bottom_contact"]["pixel_line"], front["cm_per_pixel"]),
        "front_top_z": float(front["upper_ring_top_contact"]["z_cm"]),
        "front_bottom_z": float(front["upper_ring_bottom_contact"]["z_cm"]),
        "back_top_width": span_cm(back["upper_ring_top_contact"]["pixel_line"], back["cm_per_pixel"]),
        "back_bottom_width": span_cm(back["upper_ring_bottom_contact"]["pixel_line"], back["cm_per_pixel"]),
        "back_top_z": float(back["upper_ring_top_contact"]["z_cm"]),
        "back_bottom_z": float(back["upper_ring_bottom_contact"]["z_cm"]),
        "left_top_depth": span_cm(left["upper_ring_top_contact"]["pixel_line"], left["cm_per_pixel"]),
        "left_bottom_depth": span_cm(left["upper_ring_bottom_contact"]["pixel_line"], left["cm_per_pixel"]),
        "left_top_z": float(left["upper_ring_top_contact"]["z_cm"]),
        "left_bottom_z": float(left["upper_ring_bottom_contact"]["z_cm"]),
        "right_top_depth": span_cm(right["upper_ring_top_contact"]["pixel_line"], right["cm_per_pixel"]),
        "right_bottom_depth": span_cm(right["upper_ring_bottom_contact"]["pixel_line"], right["cm_per_pixel"]),
        "right_top_z": float(right["upper_ring_top_contact"]["z_cm"]),
        "right_bottom_z": float(right["upper_ring_bottom_contact"]["z_cm"]),
    }


def build_geometry(manifests: dict[str, dict[str, Any]]) -> dict[str, Any]:
    primary_mat = material("M_A001_Primary_GeometryProof_Red", (0.75, 0.12, 0.10, 1.0))
    ring_mat = material("M_A001_UpperSocket_GeometryProof_Orange", (0.95, 0.48, 0.10, 1.0))
    support_mat = material("M_A001_Support_GeometryProof_Blue", (0.08, 0.38, 0.72, 1.0))
    cap_mat = material("M_A001_ApprovedOval_Cap_Proof", (0.24, 0.24, 0.24, 1.0))
    line_primary = material("M_A001_Marker_Red", (1.0, 0.04, 0.04, 1.0))
    line_ring = material("M_A001_Marker_Orange", (1.0, 0.58, 0.0, 1.0))
    line_support = material("M_A001_Marker_Cyan", (0.0, 0.78, 1.0, 1.0))
    line_yellow = material("M_A001_Marker_Yellow", (1.0, 0.86, 0.0, 1.0))

    dims = dimensions_from_contacts(manifests["layered_contact_approval"])
    primary_w, primary_d = 120.0, 90.0
    support_w, support_d = 140.0, 110.0

    # Approved measured oval reference caps. These are proof/reference surfaces,
    # not textured shipping caps.
    ellipse_cap("A001_Primary_Approved_120x90_TopOval_Proof", primary_w, primary_d, 220.0, cap_mat, "primary_monolith")
    ellipse_cap("A001_Support_Approved_140x110_BottomOval_Proof", support_w, support_d, 0.0, cap_mat, "support_base")
    line_rect("A001_Primary_120x90_Top_Approved_Outline", primary_w, primary_d, 222.0, line_primary)
    line_rect("A001_Support_140x110_Base_Approved_Outline", support_w, support_d, 1.5, line_support)

    # Primary source-view panels.
    make_panel(
        "A001_Primary_Front_SourcePanel",
        [(-primary_w / 2, -primary_d / 2, 220), (primary_w / 2, -primary_d / 2, 220), (dims["front_top_width"] / 2, -primary_d / 2, dims["front_top_z"]), (-dims["front_top_width"] / 2, -primary_d / 2, dims["front_top_z"])],
        primary_mat,
        "primary_monolith",
        "front",
    )
    make_panel(
        "A001_Primary_Back_SourcePanel",
        [(-primary_w / 2, primary_d / 2, 220), (-dims["back_top_width"] / 2, primary_d / 2, dims["back_top_z"]), (dims["back_top_width"] / 2, primary_d / 2, dims["back_top_z"]), (primary_w / 2, primary_d / 2, 220)],
        primary_mat,
        "primary_monolith",
        "back",
    )
    make_panel(
        "A001_Primary_Left_SourcePanel",
        [(-primary_w / 2, -primary_d / 2, 220), (-primary_w / 2, -dims["left_top_depth"] / 2, dims["left_top_z"]), (-primary_w / 2, dims["left_top_depth"] / 2, dims["left_top_z"]), (-primary_w / 2, primary_d / 2, 220)],
        primary_mat,
        "primary_monolith",
        "left",
    )
    make_panel(
        "A001_Primary_Right_SourcePanel",
        [(primary_w / 2, -primary_d / 2, 220), (primary_w / 2, primary_d / 2, 220), (primary_w / 2, dims["right_top_depth"] / 2, dims["right_top_z"]), (primary_w / 2, -dims["right_top_depth"] / 2, dims["right_top_z"])],
        primary_mat,
        "primary_monolith",
        "right",
    )

    # Upper socket/ring independent interval panels.
    make_panel(
        "A001_UpperSocket_Front_IntervalPanel",
        [(-dims["front_top_width"] / 2, -primary_d / 2, dims["front_top_z"]), (dims["front_top_width"] / 2, -primary_d / 2, dims["front_top_z"]), (dims["front_bottom_width"] / 2, -support_d / 2, dims["front_bottom_z"]), (-dims["front_bottom_width"] / 2, -support_d / 2, dims["front_bottom_z"])],
        ring_mat,
        "upper_socket_ring",
        "front",
    )
    make_panel(
        "A001_UpperSocket_Back_IntervalPanel",
        [(-dims["back_top_width"] / 2, primary_d / 2, dims["back_top_z"]), (-dims["back_bottom_width"] / 2, support_d / 2, dims["back_bottom_z"]), (dims["back_bottom_width"] / 2, support_d / 2, dims["back_bottom_z"]), (dims["back_top_width"] / 2, primary_d / 2, dims["back_top_z"])],
        ring_mat,
        "upper_socket_ring",
        "back",
    )
    make_panel(
        "A001_UpperSocket_Left_IntervalPanel",
        [(-primary_w / 2, -dims["left_top_depth"] / 2, dims["left_top_z"]), (-support_w / 2, -dims["left_bottom_depth"] / 2, dims["left_bottom_z"]), (-support_w / 2, dims["left_bottom_depth"] / 2, dims["left_bottom_z"]), (-primary_w / 2, dims["left_top_depth"] / 2, dims["left_top_z"])],
        ring_mat,
        "upper_socket_ring",
        "left",
    )
    make_panel(
        "A001_UpperSocket_Right_IntervalPanel",
        [(primary_w / 2, -dims["right_top_depth"] / 2, dims["right_top_z"]), (primary_w / 2, dims["right_top_depth"] / 2, dims["right_top_z"]), (support_w / 2, dims["right_bottom_depth"] / 2, dims["right_bottom_z"]), (support_w / 2, -dims["right_bottom_depth"] / 2, dims["right_bottom_z"])],
        ring_mat,
        "upper_socket_ring",
        "right",
    )

    # Support/base source-view panels.
    make_panel(
        "A001_Support_Front_SourcePanel",
        [(-dims["front_bottom_width"] / 2, -support_d / 2, dims["front_bottom_z"]), (dims["front_bottom_width"] / 2, -support_d / 2, dims["front_bottom_z"]), (support_w / 2, -support_d / 2, 0), (-support_w / 2, -support_d / 2, 0)],
        support_mat,
        "support_base",
        "front",
    )
    make_panel(
        "A001_Support_Back_SourcePanel",
        [(-dims["back_bottom_width"] / 2, support_d / 2, dims["back_bottom_z"]), (-support_w / 2, support_d / 2, 0), (support_w / 2, support_d / 2, 0), (dims["back_bottom_width"] / 2, support_d / 2, dims["back_bottom_z"])],
        support_mat,
        "support_base",
        "back",
    )
    make_panel(
        "A001_Support_Left_SourcePanel",
        [(-support_w / 2, -dims["left_bottom_depth"] / 2, dims["left_bottom_z"]), (-support_w / 2, -support_d / 2, 0), (-support_w / 2, support_d / 2, 0), (-support_w / 2, dims["left_bottom_depth"] / 2, dims["left_bottom_z"])],
        support_mat,
        "support_base",
        "left",
    )
    make_panel(
        "A001_Support_Right_SourcePanel",
        [(support_w / 2, -dims["right_bottom_depth"] / 2, dims["right_bottom_z"]), (support_w / 2, dims["right_bottom_depth"] / 2, dims["right_bottom_z"]), (support_w / 2, support_d / 2, 0), (support_w / 2, -support_d / 2, 0)],
        support_mat,
        "support_base",
        "right",
    )

    # Contact station marker lines.
    make_curve_line("A001_Primary_Front_BottomContact_Marker", [(-dims["front_top_width"] / 2, -primary_d / 2, dims["front_top_z"] + 1.2), (dims["front_top_width"] / 2, -primary_d / 2, dims["front_top_z"] + 1.2)], line_primary)
    make_curve_line("A001_Ring_Front_BottomContact_Marker", [(-dims["front_bottom_width"] / 2, -support_d / 2, dims["front_bottom_z"] + 1.2), (dims["front_bottom_width"] / 2, -support_d / 2, dims["front_bottom_z"] + 1.2)], line_support)
    make_curve_line("A001_Primary_Back_BottomContact_Marker", [(-dims["back_top_width"] / 2, primary_d / 2, dims["back_top_z"] + 1.2), (dims["back_top_width"] / 2, primary_d / 2, dims["back_top_z"] + 1.2)], line_primary)
    make_curve_line("A001_Ring_Back_BottomContact_Marker", [(-dims["back_bottom_width"] / 2, support_d / 2, dims["back_bottom_z"] + 1.2), (dims["back_bottom_width"] / 2, support_d / 2, dims["back_bottom_z"] + 1.2)], line_support)
    make_curve_line("A001_Old35cm_Reference_NotAuthority", [(-85, -72, 35), (85, -72, 35)], line_yellow, bevel_depth=0.45)

    for obj in bpy.context.scene.objects:
        obj.select_set(False)

    return {
        "front_top_width_cm": round(dims["front_top_width"], 4),
        "front_bottom_width_cm": round(dims["front_bottom_width"], 4),
        "back_top_width_cm": round(dims["back_top_width"], 4),
        "back_bottom_width_cm": round(dims["back_bottom_width"], 4),
        "left_top_depth_cm": round(dims["left_top_depth"], 4),
        "left_bottom_depth_cm": round(dims["left_bottom_depth"], 4),
        "right_top_depth_cm": round(dims["right_top_depth"], 4),
        "right_bottom_depth_cm": round(dims["right_bottom_depth"], 4),
    }


def setup_scene() -> None:
    bpy.context.scene.unit_settings.system = "METRIC"
    bpy.context.scene.unit_settings.scale_length = 0.01
    bpy.context.scene.render.engine = "BLENDER_EEVEE"
    bpy.context.scene.eevee.taa_render_samples = 32
    bpy.context.scene.render.resolution_x = 1400
    bpy.context.scene.render.resolution_y = 1050
    bpy.context.scene.view_settings.view_transform = "Standard"
    if "Medium High Contrast" in bpy.context.scene.view_settings.bl_rna.properties["look"].enum_items:
        bpy.context.scene.view_settings.look = "Medium High Contrast"
    else:
        bpy.context.scene.view_settings.look = "None"
    bpy.context.scene.world = bpy.data.worlds.new("A001_Proof_World") if not bpy.context.scene.world else bpy.context.scene.world
    bpy.context.scene.world.color = (0.78, 0.76, 0.70)
    light_data = bpy.data.lights.new("A001_GeometryProof_KeyLight", "AREA")
    light_data.energy = 450
    light_data.size = 600
    light = bpy.data.objects.new("A001_GeometryProof_KeyLight", light_data)
    bpy.context.collection.objects.link(light)
    light.location = (160, -220, 340)


def set_camera(label: str) -> None:
    cam_data = bpy.data.cameras.new(f"A001_{label}_Camera")
    cam = bpy.data.objects.new(f"A001_{label}_Camera", cam_data)
    bpy.context.collection.objects.link(cam)
    target = Vector((0, 0, 95))
    positions = {
        "front": Vector((0, -360, 112)),
        "back": Vector((0, 360, 112)),
        "left": Vector((-360, 0, 112)),
        "right": Vector((360, 0, 112)),
        "top": Vector((0, 0, 460)),
        "angle": Vector((230, -310, 210)),
    }
    cam.location = positions[label]
    direction = target - cam.location
    cam.rotation_euler = direction.to_track_quat("-Z", "Y").to_euler()
    cam.data.type = "ORTHO"
    cam.data.ortho_scale = 250 if label != "top" else 210
    bpy.context.scene.camera = cam


def render(label: str, path: Path) -> None:
    set_camera(label)
    bpy.context.scene.render.filepath = str(path)
    bpy.ops.render.render(write_still=True)


def write_manifest(manifests: dict[str, dict[str, Any]], proof_dimensions: dict[str, Any]) -> None:
    mesh_objects = [obj for obj in bpy.context.scene.objects if obj.type == "MESH"]
    curve_objects = [obj for obj in bpy.context.scene.objects if obj.type == "CURVE"]
    manifest = {
        "asset": ASSET_NAME,
        "status": "DCC source candidate geometry proof",
        "classification": "DCC source candidate",
        "source": str(SOURCE_IMAGE.relative_to(ROOT)),
        "geometry_construction_plan_approval_manifest": str(PLAN_APPROVAL_MANIFEST.relative_to(ROOT)),
        "geometry_construction_plan_manifest": str(PLAN_MANIFEST.relative_to(ROOT)),
        "pregeometry_audit_manifest": str(PREGEOMETRY_AUDIT_MANIFEST.relative_to(ROOT)),
        "blend": str(BLEND_PATH.relative_to(ROOT)),
        "proof_renders": {label: str(path.relative_to(ROOT)) for label, path in RENDER_PATHS.items()},
        "component_source": {
            "primary_monolith": "approved 120x90cm measured oval plus source-view primary panels",
            "upper_socket_ring": "approved per-view layered contact interval panels; no top cap authority claimed",
            "support_base": "approved 140x110cm measured oval plus source-view support panels",
        },
        "proof_dimensions_cm": proof_dimensions,
        "object_counts": {
            "mesh_objects": len(mesh_objects),
            "curve_marker_objects": len(curve_objects),
        },
        "mesh_state": {
            "geometry_generated": True,
            "uvs_generated": False,
            "textures_generated": False,
            "fbx_exported": False,
            "unreal_imported": False,
            "components_separate": True,
            "exterior_weld_applied": False,
            "beauty_render_generated": False,
        },
        "blocked_methods_enforced": [
            "no old contaminated generator logic",
            "no radial footprint authority",
            "no old 35cm contact flattening",
            "no cross-view averaged station values",
            "no stretch strip or detached cover shell",
            "no support/base projection onto primary",
            "no UV or texture generation",
            "no FBX export",
        ],
        "known_open_items": [
            "exterior seam weld validation still required",
            "UV and texture source ownership still blocked",
            "upper socket/ring top footprint remains diagnostic/shared/occluded",
            "this is not DCC game-ready and not fully game-ready",
        ],
    }
    GEOMETRY_MANIFEST.write_text(json.dumps(manifest, indent=2) + "\n")


def main() -> None:
    manifests = require_inputs()
    write_plan_approval(manifests["plan"])
    GEOMETRY_PROOF_DIR.mkdir(parents=True, exist_ok=True)
    BLEND_DIR.mkdir(parents=True, exist_ok=True)
    clear_scene()
    setup_scene()
    proof_dimensions = build_geometry(manifests)
    bpy.ops.wm.save_as_mainfile(filepath=str(BLEND_PATH))
    for label, path in RENDER_PATHS.items():
        render(label, path)
    write_manifest(manifests, proof_dimensions)
    print(f"A001 plan approval manifest: {PLAN_APPROVAL_MANIFEST}")
    print(f"A001 DCC geometry proof blend: {BLEND_PATH}")
    print(f"A001 DCC geometry proof manifest: {GEOMETRY_MANIFEST}")
    for label, path in RENDER_PATHS.items():
        print(f"A001 DCC geometry proof render {label}: {path}")


if __name__ == "__main__":
    main()
