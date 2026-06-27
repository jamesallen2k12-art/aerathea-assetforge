#!/usr/bin/env python3
"""Build first-pass Ogre cairn battle gate review assets."""

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
REVIEW_ROOT = ROOT / "Saved" / "Automation" / "OgreCairnGateReview"

sys.path.insert(0, str(ROOT))

from Tools.DCC.build_next_slice_assets import (  # noqa: E402
    add_asset_metadata,
    clear_scene,
    mesh_to_blender,
    setup_scene,
)
from Tools.DCC.generate_first_slice_meshes import Mesh  # noqa: E402


ASSET_NAME = "SM_OGR_CairnBattleGate_A01"
REL_PATH = "Props/Ogres/CairnFortifications/SM_OGR_CairnBattleGate_A01"
UNREAL_PATH = "/Game/Aerathea/Props/Ogres/CairnFortifications/SM_OGR_CairnBattleGate_A01"


def materials(mesh: Mesh) -> dict[str, str]:
    return {
        "stone": mesh.material("M_OGR_CairnStone_Blockout_A01", (0.24, 0.25, 0.24)),
        "iron": mesh.material("M_OGR_Iron_Blockout_A01", (0.08, 0.08, 0.075)),
        "timber": mesh.material("M_AET_Timber_Handpainted_A01", (0.25, 0.14, 0.07)),
        "bone": mesh.material("M_OGR_Bone_Blockout_A01", (0.64, 0.56, 0.42)),
        "banner": mesh.material("M_OGR_Warpaint_Blockout_A01", (0.27, 0.07, 0.035)),
        "glow": mesh.material("M_OGR_TekGlow_Blockout_A01", (1.0, 0.34, 0.025)),
        "brass": mesh.material("M_OGR_Brass_Blockout_A01", (0.52, 0.28, 0.11)),
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


def add_stone_course(mesh: Mesh, m: dict[str, str], prefix: str, x_center: float, width: float, depth: float, z_base: float) -> None:
    block_count = 4
    block_width = width / block_count
    for index in range(block_count):
        x = x_center - width * 0.5 + block_width * (index + 0.5)
        y_offset = -10 if (index % 2) else 10
        mesh.add_box(
            f"{prefix}_CourseBlock_{int(z_base):03d}_{index + 1:02d}",
            (x, y_offset, z_base + 24),
            (block_width - 8, depth, 48),
            m["stone"],
        )


def add_tower(mesh: Mesh, m: dict[str, str], side_name: str, x: float) -> None:
    mesh.add_cylinder(f"Tower_{side_name}_CairnCore_Lower", (x, 0, 185), 128, 370, m["stone"], "z", 12)
    mesh.add_cylinder(f"Tower_{side_name}_CairnCore_Upper", (x, 0, 475), 110, 210, m["stone"], "z", 12)
    for z in (80, 150, 220, 290, 360, 430, 500, 570):
        mesh.add_cylinder(f"Tower_{side_name}_StoneCourse_{z}", (x, 0, z), 132 if z < 390 else 116, 18, m["stone"], "z", 12)
    mesh.add_box(f"Tower_{side_name}_BasePlinth", (x, 0, 28), (310, 250, 56), m["stone"])
    mesh.add_box(f"Tower_{side_name}_IronWindowBar_Front", (x, -122, 350), (58, 12, 84), m["iron"])
    mesh.add_box(f"Tower_{side_name}_GlowWindow_Front", (x, -130, 350), (34, 8, 52), m["glow"])
    mesh.add_box(f"Tower_{side_name}_IronWindowBar_Upper", (x, -110, 535), (44, 12, 64), m["iron"])
    mesh.add_box(f"Tower_{side_name}_GlowWindow_Upper", (x, -118, 535), (24, 8, 38), m["glow"])

    for index, offset_x in enumerate((-95, -32, 32, 95), 1):
        mesh.add_box(
            f"Tower_{side_name}_Crenel_{index:02d}",
            (x + offset_x, -4, 626),
            (42, 74, 70),
            m["stone"],
        )
    for index, offset_x in enumerate((-118, -58, 0, 58, 118), 1):
        mesh.add_diamond(
            f"Tower_{side_name}_TopSpike_{index:02d}",
            (x + offset_x, -8, 690),
            (32, 32, 88),
            m["iron"],
        )


def add_wall_and_gate(mesh: Mesh, m: dict[str, str]) -> None:
    mesh.add_box("Base_CairnStone_Platform", (0, 0, 28), (1360, 260, 56), m["stone"])
    mesh.add_box("Wall_Left_CairnStone_Block", (-690, 10, 190), (300, 190, 300), m["stone"])
    mesh.add_box("Wall_Right_CairnStone_Block", (690, 10, 190), (300, 190, 300), m["stone"])
    for prefix, x_center in (("Wall_Left", -690), ("Wall_Right", 690)):
        for z in (70, 130, 190, 250, 310):
            add_stone_course(mesh, m, prefix, x_center, 300, 205, z)
        for index, x_offset in enumerate((-110, -40, 40, 110), 1):
            mesh.add_diamond(f"{prefix}_TopSpike_{index:02d}", (x_center + x_offset, -34, 390), (28, 28, 74), m["iron"])

    mesh.add_box("Arch_CairnStone_TopBeam", (0, 0, 545), (590, 210, 100), m["stone"])
    mesh.add_box("Arch_CairnStone_LeftPier", (-250, 0, 305), (110, 205, 420), m["stone"])
    mesh.add_box("Arch_CairnStone_RightPier", (250, 0, 305), (110, 205, 420), m["stone"])
    for index, x in enumerate(range(-220, 221, 55), 1):
        mesh.add_box(f"Arch_CairnStone_Course_{index:02d}", (x, -8, 505), (44, 220, 54), m["stone"])

    # Closed gate visual: timber slabs behind iron portcullis.
    for index, x in enumerate((-108, -54, 54, 108), 1):
        mesh.add_box(f"Gate_Timber_DoubleDoorPlank_{index:02d}", (x, -92, 245), (44, 28, 360), m["timber"])
    mesh.add_box("Gate_Timber_CrossBeam_Upper", (0, -112, 350), (330, 32, 38), m["timber"])
    mesh.add_box("Gate_Timber_CrossBeam_Lower", (0, -112, 160), (330, 32, 38), m["timber"])
    for index, x in enumerate(range(-180, 181, 60), 1):
        mesh.add_box(f"Gate_Portcullis_VerticalBar_{index:02d}", (x, -132, 250), (18, 22, 410), m["iron"])
        mesh.add_diamond(f"Gate_Portcullis_BottomSpike_{index:02d}", (x, -132, 34), (22, 22, 76), m["iron"])
    for index, z in enumerate((112, 212, 312, 412), 1):
        mesh.add_box(f"Gate_Portcullis_HorizontalBand_{index:02d}", (0, -139, z), (420, 20, 20), m["iron"])


def add_ogre_identity_details(mesh: Mesh, m: dict[str, str]) -> None:
    # Skull crest and horned warning mark.
    mesh.add_ellipsoid("Crest_Skull_Bone_HeavyBrow", (0, -142, 648), (74, 42, 58), m["bone"], 8, 16)
    mesh.add_box("Crest_Skull_JawPlate", (0, -146, 594), (84, 30, 34), m["bone"])
    mesh.add_diamond("Crest_Skull_Horn_Left", (-82, -142, 666), (118, 28, 46), m["bone"])
    mesh.add_diamond("Crest_Skull_Horn_Right", (82, -142, 666), (118, 28, 46), m["bone"])
    mesh.add_box("Crest_Skull_EyeGlow_Left", (-26, -181, 654), (14, 8, 12), m["glow"])
    mesh.add_box("Crest_Skull_EyeGlow_Right", (26, -181, 654), (14, 8, 12), m["glow"])
    mesh.add_box("Crest_Iron_BackPlate", (0, -154, 628), (220, 18, 126), m["iron"])

    for side_name, x in (("Left", -318), ("Right", 318)):
        mesh.add_box(f"Banner_{side_name}_Cloth_RedDrop", (x, -156, 365), (72, 12, 210), m["banner"])
        mesh.add_box(f"Banner_{side_name}_IronTopBar", (x, -160, 478), (96, 14, 16), m["iron"])
        mesh.add_box(f"Banner_{side_name}_WarMark_ForgeSlash", (x, -168, 372), (14, 7, 112), m["glow"])
        mesh.add_diamond(f"Banner_{side_name}_BottomTornPoint", (x, -156, 246), (58, 10, 66), m["banner"])
        for index, z in enumerate((430, 395, 360, 325), 1):
            mesh.add_box(f"Chain_{side_name}_Hint_{index:02d}", (x + (index % 2) * 10 - 5, -174, z), (18, 9, 22), m["iron"])

    for side_name, x in (("Left", -540), ("Right", 540)):
        mesh.add_cylinder(f"Brazier_{side_name}_IronBowl", (x, -155, 312), 42, 20, m["iron"], "z", 16)
        mesh.add_cylinder(f"Brazier_{side_name}_ForgeGlow", (x, -155, 334), 30, 24, m["glow"], "z", 16)
        mesh.add_box(f"Brazier_{side_name}_StoneBracket", (x, -78, 260), (92, 48, 88), m["stone"])
        mesh.add_diamond(f"Brazier_{side_name}_CrownSpike_A", (x - 36, -155, 364), (18, 18, 52), m["iron"])
        mesh.add_diamond(f"Brazier_{side_name}_CrownSpike_B", (x + 36, -155, 364), (18, 18, 52), m["iron"])

    # Hoist silhouettes. These are intentionally broad, not chain-by-chain detail.
    for side_name, sign in (("Left", -1), ("Right", 1)):
        x = sign * 365
        mesh.add_box(f"Hoist_{side_name}_IronBeam", (x, -145, 548), (138, 28, 28), m["iron"])
        oriented_box(mesh, f"Hoist_{side_name}_ChainHint_A", (x + sign * 60, -165, 458), 20, 12, 155, 0, m["iron"])
        oriented_box(mesh, f"Hoist_{side_name}_ChainHint_B", (x - sign * 10, -165, 438), 20, 12, 120, 0, m["iron"])


def add_collision(mesh: Mesh, m: dict[str, str]) -> None:
    mesh.add_box(f"UCX_{ASSET_NAME}_00", (-470, 0, 305), (370, 270, 610), m["stone"])
    mesh.add_box(f"UCX_{ASSET_NAME}_01", (470, 0, 305), (370, 270, 610), m["stone"])
    mesh.add_box(f"UCX_{ASSET_NAME}_02", (0, 0, 560), (640, 245, 170), m["stone"])
    mesh.add_box(f"UCX_{ASSET_NAME}_03", (0, -105, 240), (430, 70, 430), m["stone"])
    mesh.add_box(f"UCX_{ASSET_NAME}_04", (-705, 0, 190), (320, 230, 380), m["stone"])
    mesh.add_box(f"UCX_{ASSET_NAME}_05", (705, 0, 190), (320, 230, 380), m["stone"])


def add_socket_markers(mesh: Mesh, m: dict[str, str]) -> None:
    markers = [
        ("SocketMarker_snap_wall_l", (-870, 0, 70)),
        ("SocketMarker_snap_wall_r", (870, 0, 70)),
        ("SocketMarker_gate_center", (0, -160, 120)),
        ("SocketMarker_portcullis_top", (0, -142, 468)),
        ("SocketMarker_portcullis_bottom", (0, -142, 38)),
        ("SocketMarker_vfx_brazier_l", (-540, -155, 352)),
        ("SocketMarker_vfx_brazier_r", (540, -155, 352)),
        ("SocketMarker_vfx_gate_forge", (0, -150, 310)),
        ("SocketMarker_vfx_skull_crest", (0, -170, 670)),
        ("SocketMarker_socket_banner_l", (-318, -160, 480)),
        ("SocketMarker_socket_banner_r", (318, -160, 480)),
        ("SocketMarker_ai_gate_defender_l", (-300, -310, 0)),
        ("SocketMarker_ai_gate_defender_r", (300, -310, 0)),
    ]
    for name, center in markers:
        mesh.add_box(name, center, (12, 12, 12), m["glow"])


def add_cairn_gate_mesh() -> Mesh:
    mesh = Mesh(ASSET_NAME)
    m = materials(mesh)
    add_wall_and_gate(mesh, m)
    add_tower(mesh, m, "Left", -455)
    add_tower(mesh, m, "Right", 455)
    add_ogre_identity_details(mesh, m)
    add_collision(mesh, m)
    add_socket_markers(mesh, m)
    return mesh


def make_materials_readable() -> None:
    for material in bpy.data.materials:
        if not (material.name.startswith("M_OGR_") or material.name.startswith("M_AET_Timber")):
            continue
        color = material.diffuse_color
        material.use_nodes = True
        bsdf = material.node_tree.nodes.get("Principled BSDF")
        if bsdf is None:
            continue
        bsdf.inputs["Base Color"].default_value = color
        bsdf.inputs["Roughness"].default_value = 0.84
        if "Iron" in material.name or "Brass" in material.name:
            bsdf.inputs["Metallic"].default_value = 0.45
            bsdf.inputs["Roughness"].default_value = 0.64
        if "TekGlow" in material.name:
            bsdf.inputs["Emission Color"].default_value = (2.8, 0.58, 0.02, 1.0)
            bsdf.inputs["Emission Strength"].default_value = 1.6


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
        scene.world.color = (0.58, 0.58, 0.54)

    bpy.ops.object.light_add(type="SUN", location=(0, -600, 900), rotation=(math.radians(50), 0, math.radians(35)))
    sun = bpy.context.object
    sun.name = "AET_OgreCairnGateReview_Sun"
    sun.data.energy = 1.15

    bpy.ops.object.light_add(type="AREA", location=(0, -650, 640))
    key = bpy.context.object
    key.name = "AET_OgreCairnGateReview_KeyLight"
    key.data.energy = 900
    key.data.size = 920

    bpy.ops.object.camera_add(location=(1050, -1220, 620))
    camera = bpy.context.object
    target = Vector((0.0, 0.0, 315.0))
    direction = target - Vector(camera.location)
    camera.rotation_euler = direction.to_track_quat("-Z", "Y").to_euler()
    camera.data.type = "ORTHO"
    camera.data.ortho_scale = 1500
    camera.data.clip_start = 1
    camera.data.clip_end = 5000
    scene.camera = camera

    scene.render.filepath = str(REVIEW_ROOT / f"{ASSET_NAME}_DCCReview.png")
    bpy.ops.render.render(write_still=True)


def build() -> None:
    clear_scene()
    setup_scene()
    mesh = add_cairn_gate_mesh()
    objects = mesh_to_blender(mesh)
    make_materials_readable()

    add_asset_metadata(
        ASSET_NAME,
        "First-pass Ogre cairn battle gate DCC review source; final sculpt, UVs, textures, authored LODs, tuned collision, modular variants, and Blueprint gate behavior pending.",
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
