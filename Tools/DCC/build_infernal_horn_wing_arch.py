#!/usr/bin/env python3
"""Build first-pass Infernal horn-wing arch review assets.

Run with:
    blender --background --python Tools/DCC/build_infernal_horn_wing_arch.py

This creates a deterministic DCC review source for SM_INF_HornWingArch_A01.
It validates silhouette, passable threshold scale, material slots, authored
collision, and Unreal import paths; it is not final sculpted or painted art.
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
REVIEW_ROOT = ROOT / "Saved" / "Automation" / "InfernalHornWingArchReview"

sys.path.insert(0, str(ROOT))

from Tools.DCC.build_next_slice_assets import (  # noqa: E402
    add_asset_metadata,
    clear_scene,
    mesh_to_blender,
    setup_scene,
)
from Tools.DCC.generate_first_slice_meshes import Mesh  # noqa: E402


ASSET_NAME = "SM_INF_HornWingArch_A01"
REL_PATH = "Props/Infernals/BalgorothCult/SM_INF_HornWingArch_A01"
UNREAL_PATH = "/Game/Aerathea/Props/Infernals/BalgorothCult/SM_INF_HornWingArch_A01"


def materials(mesh: Mesh) -> dict[str, str]:
    return {
        "stone": mesh.material("M_INF_HornWingArch_CultStone_Blockout_A01", (0.050, 0.052, 0.057)),
        "scorched": mesh.material("M_INF_HornWingArch_ScorchedStone_Blockout_A01", (0.22, 0.055, 0.038)),
        "iron": mesh.material("M_INF_HornWingArch_ObsidianIron_Blockout_A01", (0.016, 0.015, 0.020)),
        "bone": mesh.material("M_INF_HornWingArch_BoneHorn_Blockout_A01", (0.57, 0.48, 0.34)),
        "glow": mesh.material("M_INF_HornWingArch_BrandGlow_Blockout_A01", (1.0, 0.17, 0.020)),
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


def arch_segment_prism(
    mesh: Mesh,
    name: str,
    inner_radius: float,
    outer_radius: float,
    start_deg: float,
    end_deg: float,
    center_z: float,
    y_min: float,
    y_max: float,
    material: str,
    segments: int = 4,
) -> None:
    obj = mesh.add_object(name, material)
    front_inner: list[int] = []
    front_outer: list[int] = []
    rear_inner: list[int] = []
    rear_outer: list[int] = []

    for index in range(segments + 1):
        t = index / segments
        angle = math.radians(start_deg + (end_deg - start_deg) * t)
        ca = math.cos(angle)
        sa = math.sin(angle)
        x_inner = ca * inner_radius
        z_inner = center_z + sa * inner_radius
        x_outer = ca * outer_radius
        z_outer = center_z + sa * outer_radius

        rear_inner.append(len(obj.verts) + 1)
        obj.verts.append((x_inner, y_max, z_inner))
        rear_outer.append(len(obj.verts) + 1)
        obj.verts.append((x_outer, y_max, z_outer))
        front_inner.append(len(obj.verts) + 1)
        obj.verts.append((x_inner, y_min, z_inner))
        front_outer.append(len(obj.verts) + 1)
        obj.verts.append((x_outer, y_min, z_outer))

    for index in range(segments):
        obj.faces.append((front_inner[index], front_inner[index + 1], front_outer[index + 1], front_outer[index]))
        obj.faces.append((rear_inner[index + 1], rear_inner[index], rear_outer[index], rear_outer[index + 1]))
        obj.faces.append((front_outer[index], front_outer[index + 1], rear_outer[index + 1], rear_outer[index]))
        obj.faces.append((front_inner[index + 1], front_inner[index], rear_inner[index], rear_inner[index + 1]))

    obj.faces.append((front_inner[0], front_outer[0], rear_outer[0], rear_inner[0]))
    obj.faces.append((front_outer[-1], front_inner[-1], rear_inner[-1], rear_outer[-1]))


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


def add_threshold_body(mesh: Mesh, m: dict[str, str]) -> None:
    mesh.add_box("Base_Left_CultStone_ClawedPlinth", (-205, 0, 24), (150, 215, 48), m["stone"])
    mesh.add_box("Base_Right_CultStone_ClawedPlinth", (205, 0, 24), (150, 215, 48), m["stone"])
    mesh.add_box("Base_Back_ScorchedBridgeStone", (0, 82, 18), (420, 42, 36), m["scorched"])

    mesh.add_box("Pier_Left_CultStone_InnerSlab", (-200, 0, 185), (92, 170, 370), m["stone"])
    mesh.add_box("Pier_Right_CultStone_InnerSlab", (200, 0, 185), (92, 170, 370), m["stone"])
    mesh.add_box("Pier_Left_ScorchedOuterRib", (-258, -4, 210), (38, 154, 330), m["scorched"])
    mesh.add_box("Pier_Right_ScorchedOuterRib", (258, -4, 210), (38, 154, 330), m["scorched"])

    for side, x in (("Left", -154), ("Right", 154)):
        mesh.add_box(f"InnerThroat_{side}_ObsidianIron_Liner", (x, -82, 210), (18, 24, 300), m["iron"])
        mesh.add_box(f"InnerThroat_{side}_BrandGlow_Slit", (x, -98, 228), (8, 8, 208), m["glow"])

    arch_blocks = [
        (8, 33, "stone"),
        (34, 58, "scorched"),
        (59, 88, "stone"),
        (89, 121, "scorched"),
        (122, 147, "stone"),
        (148, 172, "scorched"),
    ]
    for index, (start, end, material_key) in enumerate(arch_blocks, 1):
        arch_segment_prism(
            mesh,
            f"ArchBlock_{index:02d}_{material_key.title()}_HornThroat",
            150,
            245,
            start,
            end,
            360,
            -88,
            88,
            m[material_key],
            3,
        )

    arch_segment_prism(mesh, "ArchInner_ObsidianIron_CutEdge", 143, 158, 4, 176, 360, -102, -82, m["iron"], 10)
    arch_segment_prism(mesh, "ArchOuter_ObsidianIron_BackBand", 238, 255, 4, 176, 360, 82, 102, m["iron"], 10)
    mesh.add_box("Keystone_CultStone_BalgorothBrow", (0, -2, 535), (100, 184, 92), m["stone"])
    mesh.add_box("Keystone_BrandGlow_WatchingEye", (0, -102, 506), (88, 8, 24), m["glow"])


def add_wing_and_horn_language(mesh: Mesh, m: dict[str, str]) -> None:
    xz_triangle_prism(mesh, "Wing_Left_ObsidianIron_UpperBlade", ((-78, 492), (-315, 590), (-242, 448)), -54, 54, m["iron"])
    xz_triangle_prism(mesh, "Wing_Right_ObsidianIron_UpperBlade", ((78, 492), (315, 590), (242, 448)), -54, 54, m["iron"])
    xz_triangle_prism(mesh, "Wing_Left_ScorchedStone_LowerBlade", ((-108, 430), (-318, 468), (-205, 390)), -60, 60, m["scorched"])
    xz_triangle_prism(mesh, "Wing_Right_ScorchedStone_LowerBlade", ((108, 430), (318, 468), (205, 390)), -60, 60, m["scorched"])

    xz_triangle_prism(mesh, "Crown_Center_BoneHorn_Spear", ((-34, 540), (34, 540), (0, 650)), -40, 40, m["bone"])
    xz_triangle_prism(mesh, "Crown_Left_BoneHorn_Hook", ((-150, 504), (-88, 506), (-166, 602)), -38, 38, m["bone"])
    xz_triangle_prism(mesh, "Crown_Right_BoneHorn_Hook", ((150, 504), (88, 506), (166, 602)), -38, 38, m["bone"])
    xz_triangle_prism(mesh, "WingTip_Left_BoneHorn_Talon", ((-312, 500), (-248, 466), (-330, 570)), -35, 35, m["bone"])
    xz_triangle_prism(mesh, "WingTip_Right_BoneHorn_Talon", ((312, 500), (248, 466), (330, 570)), -35, 35, m["bone"])

    mesh.add_box("Crown_BackBrace_ObsidianIron", (0, 96, 468), (420, 24, 76), m["iron"])
    oriented_box(mesh, "Wing_Left_BackRib_ObsidianIron", (-210, 92, 500), 190, 26, 34, 153, m["iron"])
    oriented_box(mesh, "Wing_Right_BackRib_ObsidianIron", (210, 92, 500), 190, 26, 34, 27, m["iron"])

    for index, (x, z, yaw) in enumerate(((-102, 326, -18), (-62, 408, -8), (62, 408, 8), (102, 326, 18)), 1):
        oriented_box(mesh, f"BrandGroove_{index:02d}_GlowCarvedStroke", (x, -104, z), 96, 8, 8, yaw, m["glow"])


def add_socket_markers(mesh: Mesh, m: dict[str, str]) -> None:
    markers = [
        ("SocketMarker_snap_floor", (0, -112, 0)),
        ("SocketMarker_snap_altar", (0, -210, 0)),
        ("SocketMarker_guard_l", (-250, -205, 0)),
        ("SocketMarker_guard_r", (250, -205, 0)),
        ("SocketMarker_banner_l", (-222, -104, 376)),
        ("SocketMarker_banner_r", (222, -104, 376)),
        ("SocketMarker_vfx_crown", (0, -106, 612)),
        ("SocketMarker_vfx_eye", (0, -116, 506)),
        ("SocketMarker_vfx_inner_throat", (0, -116, 250)),
        ("SocketMarker_vfx_rejected_gap", (0, -118, 172)),
    ]
    for name, center in markers:
        mesh.add_box(name, center, (12, 12, 12), m["glow"])


def add_collision(mesh: Mesh, m: dict[str, str]) -> None:
    mesh.add_box(f"UCX_{ASSET_NAME}_00", (-205, 0, 205), (108, 196, 410), m["stone"])
    mesh.add_box(f"UCX_{ASSET_NAME}_01", (205, 0, 205), (108, 196, 410), m["stone"])
    mesh.add_box(f"UCX_{ASSET_NAME}_02", (0, 0, 438), (510, 196, 136), m["stone"])
    mesh.add_box(f"UCX_{ASSET_NAME}_03", (0, 84, 240), (332, 34, 300), m["stone"])


def add_horn_wing_arch_mesh() -> Mesh:
    mesh = Mesh(ASSET_NAME)
    m = materials(mesh)
    add_threshold_body(mesh, m)
    add_wing_and_horn_language(mesh, m)
    add_collision(mesh, m)
    return mesh


def make_materials_readable() -> None:
    for material in bpy.data.materials:
        if not material.name.startswith("M_INF_HornWingArch_"):
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


def compress_export_depth(objects: list[bpy.types.Object], factor: float = 0.82) -> None:
    bpy.ops.object.select_all(action="DESELECT")
    for obj in objects:
        obj.select_set(True)
        obj.scale.y *= factor
    if objects:
        bpy.context.view_layer.objects.active = objects[0]
        bpy.ops.object.transform_apply(location=False, rotation=False, scale=True)
    bpy.ops.object.select_all(action="DESELECT")


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
    add_marker_box(f"Review_{name}_Post", (x, -185, height * 0.5), (10, 10, height), material)
    add_marker_box(f"Review_{name}_Cap", (x, -185, height), (40, 10, 8), material)


def add_label(text: str, location: tuple[float, float, float], size: float = 18.0) -> None:
    bpy.ops.object.text_add(location=location, rotation=(math.radians(76), 0, 0))
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
    add_scale_marker("Human_180cm", 180, 410, marker_material)
    add_scale_marker("Infernal_274cm", 274, 462, marker_material)
    add_label("180 cm", (410, -204, 198), 16)
    add_label("274 cm", (462, -204, 292), 16)
    add_label("clear passable throat", (0, -210, 372), 18)

    bpy.ops.object.light_add(type="SUN", location=(0, -600, 900), rotation=(math.radians(48), 0, math.radians(28)))
    sun = bpy.context.object
    sun.name = "AET_InfernalHornWingArchReview_Sun"
    sun.data.energy = 1.0

    bpy.ops.object.light_add(type="AREA", location=(0, -720, 650))
    key = bpy.context.object
    key.name = "AET_InfernalHornWingArchReview_KeyLight"
    key.data.energy = 960
    key.data.size = 920

    bpy.ops.object.camera_add(location=(880, -1080, 470))
    camera = bpy.context.object
    target = Vector((0.0, 0.0, 315.0))
    direction = target - Vector(camera.location)
    camera.rotation_euler = direction.to_track_quat("-Z", "Y").to_euler()
    camera.data.type = "ORTHO"
    camera.data.ortho_scale = 960
    camera.data.clip_start = 1
    camera.data.clip_end = 5000
    scene.camera = camera

    scene.render.filepath = str(REVIEW_ROOT / f"{ASSET_NAME}_DCCReview.png")
    bpy.ops.render.render(write_still=True)


def build() -> None:
    clear_scene()
    setup_scene()
    mesh = add_horn_wing_arch_mesh()
    objects = mesh_to_blender(mesh)
    compress_export_depth(objects)
    make_materials_readable()

    add_asset_metadata(
        ASSET_NAME,
        "First-pass Infernal horn-wing cult arch DCC review source; final sculpt, UVs, textures, authored LODs, tuned collision, and Blueprint interaction behavior pending.",
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
