#!/usr/bin/env python3
"""Build first-pass Infernal worthiness altar review assets.

Run with:
    blender --background --python Tools/DCC/build_infernal_worthiness_altar.py

This creates a deterministic DCC review source for
SM_INF_WorthinessAltar_A01. It validates silhouette, snap scale, material
lanes, authored collision, and Unreal import paths; it is not final sculpted
or painted art.
"""

from __future__ import annotations

import math
import sys
from pathlib import Path

import bpy
from mathutils import Vector


ROOT = Path(__file__).resolve().parents[2]
SOURCE_ROOT = ROOT / "SourceAssets"
BLENDER_ROOT = SOURCE_ROOT / "Blender"
EXPORT_ROOT = SOURCE_ROOT / "Exports"
REVIEW_ROOT = ROOT / "Saved" / "Automation" / "InfernalWorthinessAltarReview"

sys.path.insert(0, str(ROOT))

from Tools.DCC.build_next_slice_assets import (  # noqa: E402
    add_asset_metadata,
    clear_scene,
    mesh_to_blender,
    setup_scene,
)
from Tools.DCC.generate_first_slice_meshes import Mesh  # noqa: E402


ASSET_NAME = "SM_INF_WorthinessAltar_A01"
REL_PATH = "Props/Infernals/BalgorothCult/SM_INF_WorthinessAltar_A01"
UNREAL_PATH = "/Game/Aerathea/Props/Infernals/BalgorothCult/SM_INF_WorthinessAltar_A01"


def materials(mesh: Mesh) -> dict[str, str]:
    return {
        "stone": mesh.material("M_INF_WorthinessAltar_CultStone_Blockout_A01", (0.050, 0.052, 0.057)),
        "scorched": mesh.material("M_INF_WorthinessAltar_ScorchedStone_Blockout_A01", (0.22, 0.055, 0.038)),
        "iron": mesh.material("M_INF_WorthinessAltar_ObsidianIron_Blockout_A01", (0.016, 0.015, 0.020)),
        "bone": mesh.material("M_INF_WorthinessAltar_BoneHorn_Blockout_A01", (0.57, 0.48, 0.34)),
        "glow": mesh.material("M_INF_WorthinessAltar_BrandGlow_Blockout_A01", (1.0, 0.17, 0.020)),
    }


def oriented_box(
    mesh: Mesh,
    name: str,
    center: tuple[float, float, float],
    length: float,
    width: float,
    height: float,
    yaw_deg: float,
    material: str,
) -> None:
    cx, cy, cz = center
    half_l = length * 0.5
    half_w = width * 0.5
    half_h = height * 0.5
    angle = math.radians(yaw_deg)
    forward = (math.cos(angle), math.sin(angle))
    right = (-math.sin(angle), math.cos(angle))
    corners_2d = [(-half_l, -half_w), (half_l, -half_w), (half_l, half_w), (-half_l, half_w)]

    obj = mesh.add_object(name, material)
    for z in (cz - half_h, cz + half_h):
        for local_x, local_y in corners_2d:
            obj.verts.append(
                (
                    cx + forward[0] * local_x + right[0] * local_y,
                    cy + forward[1] * local_x + right[1] * local_y,
                    z,
                )
            )
    obj.faces.extend(
        [
            (1, 2, 3, 4),
            (5, 8, 7, 6),
            (1, 5, 6, 2),
            (2, 6, 7, 3),
            (3, 7, 8, 4),
            (4, 8, 5, 1),
        ]
    )


def xz_triangle_prism(
    mesh: Mesh,
    name: str,
    points: tuple[tuple[float, float], tuple[float, float], tuple[float, float]],
    y_min: float,
    y_max: float,
    material: str,
) -> None:
    obj = mesh.add_object(name, material)
    for y in (y_min, y_max):
        for x, z in points:
            obj.verts.append((x, y, z))
    obj.faces.extend(
        [
            (1, 2, 3),
            (4, 6, 5),
            (1, 4, 5, 2),
            (2, 5, 6, 3),
            (3, 6, 4, 1),
        ]
    )


def add_altar_body(mesh: Mesh, m: dict[str, str]) -> None:
    mesh.add_box("Base_CultStone_HeavyPlinth", (0, -20, 18), (320, 210, 36), m["stone"])
    mesh.add_box("Base_ScorchedStone_RearStep", (0, -112, 42), (282, 48, 48), m["scorched"])
    mesh.add_box("Base_CultStone_FrontStep", (0, 90, 45), (262, 52, 40), m["stone"])
    mesh.add_box("TopSlab_ScorchedStone_OfferingDeck", (0, -6, 78), (262, 148, 34), m["scorched"])
    mesh.add_box("TopSlab_ObsidianIron_FrontLip", (0, 78, 98), (236, 20, 22), m["iron"])
    mesh.add_box("TopSlab_ObsidianIron_BackLip", (0, -78, 98), (236, 20, 22), m["iron"])

    for side, x in (("Left", -148), ("Right", 148)):
        mesh.add_box(f"Base_{side}_ObsidianIron_ClawFoot", (x, 44, 32), (34, 70, 34), m["iron"])
        mesh.add_box(f"Base_{side}_ScorchedStone_RearShoulder", (x, -100, 64), (30, 70, 52), m["scorched"])


def add_backplate_and_wings(mesh: Mesh, m: dict[str, str]) -> None:
    mesh.add_box("Backplate_CultStone_JudgmentSlab", (0, -118, 166), (228, 32, 252), m["stone"])
    mesh.add_box("Backplate_ScorchedStone_InnerBurnPanel", (0, -137, 166), (164, 10, 184), m["scorched"])
    mesh.add_box("Backplate_ObsidianIron_LeftFrame", (-114, -137, 171), (12, 14, 224), m["iron"])
    mesh.add_box("Backplate_ObsidianIron_RightFrame", (114, -137, 171), (12, 14, 224), m["iron"])
    mesh.add_box("Backplate_ObsidianIron_TopFrame", (0, -137, 286), (224, 14, 16), m["iron"])

    xz_triangle_prism(mesh, "Wing_Left_CultStone_UpperSlab", ((-95, 108), (-195, 254), (-156, 96)), -134, -78, m["stone"])
    xz_triangle_prism(mesh, "Wing_Right_CultStone_UpperSlab", ((95, 108), (195, 254), (156, 96)), -134, -78, m["stone"])
    xz_triangle_prism(mesh, "Wing_Left_ScorchedStone_LowerSlab", ((-126, 78), (-196, 176), (-170, 46)), -128, -72, m["scorched"])
    xz_triangle_prism(mesh, "Wing_Right_ScorchedStone_LowerSlab", ((126, 78), (196, 176), (170, 46)), -128, -72, m["scorched"])
    oriented_box(mesh, "Wing_Left_ObsidianIron_BackRib", (-150, -110, 172), 130, 18, 18, 58, m["iron"])
    oriented_box(mesh, "Wing_Right_ObsidianIron_BackRib", (150, -110, 172), 130, 18, 18, 122, m["iron"])

    xz_triangle_prism(mesh, "Crown_Center_BoneHorn_Spear", ((-28, 286), (28, 286), (0, 356)), -140, -86, m["bone"])
    xz_triangle_prism(mesh, "Crown_Left_BoneHorn_Hook", ((-111, 274), (-72, 282), (-142, 340)), -138, -90, m["bone"])
    xz_triangle_prism(mesh, "Crown_Right_BoneHorn_Hook", ((111, 274), (72, 282), (142, 340)), -138, -90, m["bone"])
    xz_triangle_prism(mesh, "WingTip_Left_BoneHorn_Talon", ((-186, 188), (-156, 164), (-202, 236)), -126, -84, m["bone"])
    xz_triangle_prism(mesh, "WingTip_Right_BoneHorn_Talon", ((186, 188), (156, 164), (202, 236)), -126, -84, m["bone"])


def add_basin_and_brand_channels(mesh: Mesh, m: dict[str, str]) -> None:
    mesh.add_cylinder("Basin_ObsidianIron_OfferingRim", (0, -6, 108), 57, 20, m["iron"], "z", 24)
    mesh.add_cylinder("Basin_ScorchedStone_InnerBowl", (0, -6, 116), 45, 10, m["scorched"], "z", 24)
    mesh.add_cylinder("Basin_BrandGlow_EmberCore", (0, -6, 123), 34, 6, m["glow"], "z", 20)

    oriented_box(mesh, "BrandGlow_RingLink_FrontStroke", (0, 72, 99), 152, 8, 7, 0, m["glow"])
    oriented_box(mesh, "BrandGlow_RingLink_LeftStroke", (-62, 37, 100), 96, 8, 7, 50, m["glow"])
    oriented_box(mesh, "BrandGlow_RingLink_RightStroke", (62, 37, 100), 96, 8, 7, 130, m["glow"])
    oriented_box(mesh, "BrandGlow_RejectedGap_BroadCrack", (87, 70, 102), 86, 9, 8, -32, m["glow"])

    for index, (x, z, height) in enumerate(((-42, 200, 112), (0, 214, 138), (42, 200, 112)), 1):
        mesh.add_box(f"Backplate_BrandGlow_ClawStroke_{index:02d}", (x, -144, z), (8, 7, height), m["glow"])

    mesh.add_box("Backplate_BrandGlow_JudgmentEye", (0, -146, 264), (84, 7, 16), m["glow"])
    mesh.add_box("Front_ObsidianIron_InteractionPlate", (0, 118, 96), (148, 12, 42), m["iron"])


def add_collision(mesh: Mesh, m: dict[str, str]) -> None:
    mesh.add_box(f"UCX_{ASSET_NAME}_00", (0, -20, 35), (330, 220, 70), m["stone"])
    mesh.add_box(f"UCX_{ASSET_NAME}_01", (0, -6, 92), (274, 158, 56), m["stone"])
    mesh.add_box(f"UCX_{ASSET_NAME}_02", (0, -118, 166), (238, 38, 256), m["stone"])
    mesh.add_box(f"UCX_{ASSET_NAME}_03", (-150, -104, 146), (96, 70, 188), m["stone"])
    mesh.add_box(f"UCX_{ASSET_NAME}_04", (150, -104, 146), (96, 70, 188), m["stone"])


def add_worthiness_altar_mesh() -> Mesh:
    mesh = Mesh(ASSET_NAME)
    m = materials(mesh)
    add_altar_body(mesh, m)
    add_backplate_and_wings(mesh, m)
    add_basin_and_brand_channels(mesh, m)
    add_collision(mesh, m)
    return mesh


def make_materials_readable() -> None:
    for material in bpy.data.materials:
        if not material.name.startswith("M_INF_WorthinessAltar_"):
            continue
        color = material.diffuse_color
        material.use_nodes = True
        bsdf = material.node_tree.nodes.get("Principled BSDF")
        if bsdf is None:
            continue
        bsdf.inputs["Base Color"].default_value = color
        bsdf.inputs["Roughness"].default_value = 0.84
        if "ObsidianIron" in material.name:
            bsdf.inputs["Metallic"].default_value = 0.42
            bsdf.inputs["Roughness"].default_value = 0.62
        if "BoneHorn" in material.name:
            bsdf.inputs["Roughness"].default_value = 0.70
        if "BrandGlow" in material.name:
            bsdf.inputs["Emission Color"].default_value = (3.0, 0.26, 0.025, 1.0)
            bsdf.inputs["Emission Strength"].default_value = 1.9


def hide_collision_for_review(objects: list[bpy.types.Object]) -> None:
    for obj in objects:
        if obj.name.startswith("UCX_"):
            obj.hide_render = True
            obj.display_type = "WIRE"


def review_material(name: str, color: tuple[float, float, float, float]) -> bpy.types.Material:
    material = bpy.data.materials.get(name) or bpy.data.materials.new(name)
    material.diffuse_color = color
    return material


def add_marker_box(name: str, location: tuple[float, float, float], scale: tuple[float, float, float], material: bpy.types.Material) -> None:
    bpy.ops.mesh.primitive_cube_add(size=1.0, location=location)
    obj = bpy.context.object
    obj.name = name
    obj.dimensions = scale
    bpy.ops.object.transform_apply(location=False, rotation=False, scale=True)
    obj.data.materials.append(material)


def add_scale_marker(name: str, height: float, x: float, material: bpy.types.Material) -> None:
    add_marker_box(f"Review_{name}_Post", (x, 138, height * 0.5), (9, 9, height), material)
    add_marker_box(f"Review_{name}_Cap", (x, 138, height), (36, 9, 7), material)


def add_label(text: str, location: tuple[float, float, float], size: float = 15.0) -> None:
    bpy.ops.object.text_add(location=location, rotation=(math.radians(74), 0, 0))
    obj = bpy.context.object
    obj.name = "Review_Label_" + text.replace(" ", "_")
    obj.data.body = text
    obj.data.align_x = "CENTER"
    obj.data.align_y = "CENTER"
    obj.data.size = size
    obj.data.materials.append(review_material("M_REVIEW_Label_Dark", (0.02, 0.02, 0.02, 1.0)))


def render_review() -> None:
    REVIEW_ROOT.mkdir(parents=True, exist_ok=True)
    scene = bpy.context.scene
    scene.render.resolution_x = 1800
    scene.render.resolution_y = 1300
    try:
        scene.eevee.taa_render_samples = 64
    except Exception:
        pass
    if scene.world is not None:
        scene.world.color = (0.56, 0.55, 0.52)

    marker_material = review_material("M_REVIEW_Scale_Marker", (0.82, 0.78, 0.64, 1.0))
    add_scale_marker("Lesser_90cm", 90, 286, marker_material)
    add_scale_marker("Human_180cm", 180, 334, marker_material)
    add_scale_marker("Infernal_274cm", 274, 386, marker_material)
    add_label("90 cm", (286, 124, 108), 13)
    add_label("180 cm", (334, 124, 198), 14)
    add_label("274 cm", (386, 124, 292), 14)
    add_label("front interaction", (0, 144, 132), 15)
    add_label("snap pivot", (0, 144, 22), 14)

    bpy.ops.object.light_add(type="SUN", location=(0, 620, 900), rotation=(math.radians(48), 0, math.radians(-28)))
    sun = bpy.context.object
    sun.name = "AET_InfernalWorthinessAltarReview_Sun"
    sun.data.energy = 1.0

    bpy.ops.object.light_add(type="AREA", location=(0, 690, 520))
    key = bpy.context.object
    key.name = "AET_InfernalWorthinessAltarReview_KeyLight"
    key.data.energy = 820
    key.data.size = 720

    bpy.ops.object.camera_add(location=(610, 780, 365))
    camera = bpy.context.object
    target = Vector((0.0, -20.0, 165.0))
    direction = target - Vector(camera.location)
    camera.rotation_euler = direction.to_track_quat("-Z", "Y").to_euler()
    camera.data.type = "ORTHO"
    camera.data.ortho_scale = 610
    camera.data.clip_start = 1
    camera.data.clip_end = 5000
    scene.camera = camera

    scene.render.filepath = str(REVIEW_ROOT / f"{ASSET_NAME}_DCCReview.png")
    bpy.ops.render.render(write_still=True)


def build() -> None:
    clear_scene()
    setup_scene()
    mesh = add_worthiness_altar_mesh()
    objects = mesh_to_blender(mesh)
    hide_collision_for_review(objects)
    make_materials_readable()

    add_asset_metadata(
        ASSET_NAME,
        "First-pass Infernal worthiness altar DCC review source; final sculpt, UVs, textures, authored LOD meshes, tuned collision, and Blueprint interaction behavior pending.",
        UNREAL_PATH,
    )

    blend_path = BLENDER_ROOT / REL_PATH / f"{ASSET_NAME}.blend"
    export_path = EXPORT_ROOT / REL_PATH / f"{ASSET_NAME}.fbx"
    blend_path.parent.mkdir(parents=True, exist_ok=True)
    export_path.parent.mkdir(parents=True, exist_ok=True)

    render_review()
    bpy.ops.wm.save_as_mainfile(filepath=str(blend_path))

    bpy.ops.object.select_all(action="DESELECT")
    for obj in objects:
        obj.select_set(True)
    if objects:
        bpy.context.view_layer.objects.active = objects[0]

    bpy.ops.export_scene.fbx(
        filepath=str(export_path),
        use_selection=True,
        object_types={"MESH"},
        mesh_smooth_type="FACE",
        global_scale=1.0,
        apply_unit_scale=False,
        apply_scale_options="FBX_SCALE_NONE",
        axis_forward="X",
        axis_up="Z",
        bake_space_transform=False,
        add_leaf_bones=False,
    )
    print(f"Built {blend_path.relative_to(ROOT)}")
    print(f"Exported {export_path.relative_to(ROOT)}")
    print(f"Rendered {REVIEW_ROOT.relative_to(ROOT)}/{ASSET_NAME}_DCCReview.png")


if __name__ == "__main__":
    build()
