#!/usr/bin/env python3
"""Build the first-pass Aerathea Giant base DCC review source.

Run with:
    blender --background --python Tools/DCC/build_giant_base.py

This creates deterministic review meshes for scale, proportions, skeleton,
sockets, and export paths. It is not final sculpted or painted production art.
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
REVIEW_ROOT = ROOT / "Saved" / "Automation" / "GiantBaseReview"

sys.path.insert(0, str(ROOT))

from Tools.DCC.build_next_slice_assets import (  # noqa: E402
    add_asset_metadata,
    add_box_obj,
    add_cylinder_between,
    add_ellipsoid_obj,
    add_socket_empty,
    assign_to_bone,
    clear_scene,
    create_armature,
    create_materials,
    export_skeletal_fbx,
    get_material,
    setup_scene,
)


GIANT_MATERIALS = {
    "M_GIA_Skin_Blockout_A01": (0.58, 0.41, 0.30),
    "M_GIA_Tattoo_Blockout_A01": (0.15, 0.25, 0.29),
    "M_GIA_Leather_Blockout_A01": (0.24, 0.13, 0.07),
    "M_GIA_Fur_Blockout_A01": (0.30, 0.25, 0.20),
    "M_GIA_Hair_Blockout_A01": (0.10, 0.08, 0.06),
    "M_GIA_Iron_Blockout_A01": (0.18, 0.18, 0.17),
    "M_GIA_Stone_Blockout_A01": (0.34, 0.36, 0.34),
    "M_GIA_RuneGlow_Blockout_A01": (0.0, 0.55, 1.0),
    "M_AET_ScaleMarker_Blockout_A01": (0.12, 0.12, 0.12),
}

GIANT_TEMPLATE_HEIGHT_CM = 457.0
GIANT_MALE_BASELINE_CM = 470.0
GIANT_FEMALE_BASELINE_CM = 442.0


def make_review_materials_readable(materials: dict[str, bpy.types.Material]) -> None:
    for material in materials.values():
        color = material.diffuse_color
        material.use_nodes = True
        bsdf = material.node_tree.nodes.get("Principled BSDF")
        if bsdf is None:
            continue
        bsdf.inputs["Base Color"].default_value = color
        bsdf.inputs["Roughness"].default_value = 0.88
        if "Emission Color" in bsdf.inputs:
            bsdf.inputs["Emission Color"].default_value = color
        if "Emission Strength" in bsdf.inputs:
            bsdf.inputs["Emission Strength"].default_value = 0.45


def p(point: tuple[float, float, float], offset_y: float) -> tuple[float, float, float]:
    return (point[0], point[1] + offset_y, point[2])


def scaled(point: tuple[float, float, float], scale: float) -> tuple[float, float, float]:
    return (point[0] * scale, point[1] * scale, point[2] * scale)


def make_bones(scale: float, offset_y: float) -> list[tuple[str, tuple[float, float, float], tuple[float, float, float], str | None]]:
    def sp(point: tuple[float, float, float]) -> tuple[float, float, float]:
        return p(scaled(point, scale), offset_y)

    return [
        ("root", sp((0, 0, 0)), sp((0, 0, 24)), None),
        ("pelvis", sp((0, 0, 205)), sp((0, 0, 238)), "root"),
        ("spine_01", sp((0, 0, 238)), sp((0, 0, 302)), "pelvis"),
        ("chest", sp((0, 0, 302)), sp((0, 0, 352)), "spine_01"),
        ("neck", sp((0, 0, 352)), sp((0, 0, 380)), "chest"),
        ("head", sp((0, 0, 380)), sp((0, 0, 454)), "neck"),
        ("clavicle_l", sp((0, 26, 340)), sp((0, 55, 336)), "chest"),
        ("upperarm_l", sp((0, 55, 336)), sp((2, 88, 252)), "clavicle_l"),
        ("lowerarm_l", sp((2, 88, 252)), sp((4, 100, 170)), "upperarm_l"),
        ("hand_l", sp((4, 100, 170)), sp((8, 104, 132)), "lowerarm_l"),
        ("clavicle_r", sp((0, -26, 340)), sp((0, -55, 336)), "chest"),
        ("upperarm_r", sp((0, -55, 336)), sp((2, -88, 252)), "clavicle_r"),
        ("lowerarm_r", sp((2, -88, 252)), sp((4, -100, 170)), "upperarm_r"),
        ("hand_r", sp((4, -100, 170)), sp((8, -104, 132)), "lowerarm_r"),
        ("thigh_l", sp((0, 28, 210)), sp((10, 38, 104)), "pelvis"),
        ("calf_l", sp((10, 38, 104)), sp((18, 38, 24)), "thigh_l"),
        ("foot_l", sp((18, 38, 24)), sp((52, 38, 5)), "calf_l"),
        ("thigh_r", sp((0, -28, 210)), sp((10, -38, 104)), "pelvis"),
        ("calf_r", sp((10, -38, 104)), sp((18, -38, 24)), "thigh_r"),
        ("foot_r", sp((18, -38, 24)), sp((52, -38, 5)), "calf_r"),
    ]


def add_tattoo_band(
    name: str,
    center: tuple[float, float, float],
    size: tuple[float, float, float],
    material: bpy.types.Material,
    bone: str,
    armature: bpy.types.Object,
    objects: list[bpy.types.Object],
) -> None:
    obj = add_box_obj(name, center, size, material)
    assign_to_bone(obj, armature, bone)
    objects.append(obj)


def add_giant_variant(
    label: str,
    armature_name: str,
    scale: float,
    offset_y: float,
    materials: dict[str, bpy.types.Material],
) -> tuple[bpy.types.Object, list[bpy.types.Object]]:
    bones = make_bones(scale, offset_y)
    armature = create_armature(armature_name, bones)
    objects: list[bpy.types.Object] = []

    skin = materials["M_GIA_Skin_Blockout_A01"]
    tattoo = materials["M_GIA_Tattoo_Blockout_A01"]
    leather = materials["M_GIA_Leather_Blockout_A01"]
    fur = materials["M_GIA_Fur_Blockout_A01"]
    hair = materials["M_GIA_Hair_Blockout_A01"]
    iron = materials["M_GIA_Iron_Blockout_A01"]
    stone = materials["M_GIA_Stone_Blockout_A01"]
    glow = materials["M_GIA_RuneGlow_Blockout_A01"]

    def sp(point: tuple[float, float, float]) -> tuple[float, float, float]:
        return p(scaled(point, scale), offset_y)

    def sr(radii: tuple[float, float, float]) -> tuple[float, float, float]:
        return scaled(radii, scale)

    body_parts = [
        (add_ellipsoid_obj(f"{label}_Body_Pelvis", sp((0, 0, 214)), sr((34, 48, 30)), leather, 18, 8), "pelvis"),
        (add_ellipsoid_obj(f"{label}_Body_Torso", sp((0, 0, 292)), sr((48, 55, 70)), skin, 20, 10), "spine_01"),
        (add_ellipsoid_obj(f"{label}_Body_Chest", sp((0, 0, 338)), sr((54, 68, 54)), skin, 20, 10), "chest"),
        (add_ellipsoid_obj(f"{label}_Head_HeavyBrow", sp((8, 0, 412)), sr((28, 26, 38)), skin, 20, 10), "head"),
        (add_box_obj(f"{label}_Jaw_Block", sp((20, 0, 392)), sr((24, 30, 20)), skin), "head"),
        (add_ellipsoid_obj(f"{label}_Fur_Mantle", sp((-8, 0, 354)), sr((34, 82, 22)), fur, 16, 8), "chest"),
        (add_box_obj(f"{label}_Leather_KiltFront", sp((24, 0, 165)), sr((12, 48, 92)), leather), "pelvis"),
        (add_box_obj(f"{label}_Leather_KiltBack", sp((-18, 0, 170)), sr((10, 48, 88)), leather), "pelvis"),
        (add_box_obj(f"{label}_Belt_StoneBuckle", sp((36, 0, 226)), sr((16, 34, 24)), stone), "pelvis"),
        (add_ellipsoid_obj(f"{label}_Rune_Talisman", sp((42, 0, 300)), sr((6, 6, 10)), glow, 10, 5), "chest"),
        (add_cylinder_between(f"{label}_Hair_BraidBack_01", sp((-28, 12, 416)), sp((-36, 18, 292)), 5 * scale, hair, 10), "head"),
        (add_cylinder_between(f"{label}_Hair_BraidBack_02", sp((-28, -12, 416)), sp((-36, -18, 292)), 5 * scale, hair, 10), "head"),
        (add_cylinder_between(f"{label}_Arm_Left_Upper", sp((0, 57, 330)), sp((4, 88, 252)), 14 * scale, skin, 14), "upperarm_l"),
        (add_cylinder_between(f"{label}_Arm_Left_Lower", sp((4, 88, 252)), sp((8, 101, 170)), 12 * scale, skin, 14), "lowerarm_l"),
        (add_ellipsoid_obj(f"{label}_Hand_Left_LargePalm", sp((14, 106, 143)), sr((18, 15, 20)), skin, 14, 7), "hand_l"),
        (add_cylinder_between(f"{label}_Arm_Right_Upper", sp((0, -57, 330)), sp((4, -88, 252)), 14 * scale, skin, 14), "upperarm_r"),
        (add_cylinder_between(f"{label}_Arm_Right_Lower", sp((4, -88, 252)), sp((8, -101, 170)), 12 * scale, skin, 14), "lowerarm_r"),
        (add_ellipsoid_obj(f"{label}_Hand_Right_LargePalm", sp((14, -106, 143)), sr((18, 15, 20)), skin, 14, 7), "hand_r"),
        (add_cylinder_between(f"{label}_Leg_Left_Upper", sp((2, 30, 204)), sp((13, 39, 106)), 18 * scale, skin, 14), "thigh_l"),
        (add_cylinder_between(f"{label}_Leg_Left_Lower", sp((13, 39, 106)), sp((20, 39, 28)), 15 * scale, skin, 14), "calf_l"),
        (add_box_obj(f"{label}_Foot_Left_Wrapped", sp((48, 39, 12)), sr((58, 34, 22)), leather), "foot_l"),
        (add_cylinder_between(f"{label}_Leg_Right_Upper", sp((2, -30, 204)), sp((13, -39, 106)), 18 * scale, skin, 14), "thigh_r"),
        (add_cylinder_between(f"{label}_Leg_Right_Lower", sp((13, -39, 106)), sp((20, -39, 28)), 15 * scale, skin, 14), "calf_r"),
        (add_box_obj(f"{label}_Foot_Right_Wrapped", sp((48, -39, 12)), sr((58, 34, 22)), leather), "foot_r"),
    ]
    for obj, bone in body_parts:
        assign_to_bone(obj, armature, bone)
        objects.append(obj)

    for side, sign, bone in (("Left", 1, "hand_l"), ("Right", -1, "hand_r")):
        for idx, y_offset in enumerate((-11, -4, 4, 11), 1):
            obj = add_cylinder_between(
                f"{label}_Hand_{side}_Finger_{idx}",
                sp((20, sign * (107 + y_offset), 145)),
                sp((48, sign * (109 + y_offset), 134)),
                3.2 * scale,
                skin,
                8,
            )
            assign_to_bone(obj, armature, bone)
            objects.append(obj)
        thumb = add_cylinder_between(
            f"{label}_Hand_{side}_Thumb",
            sp((14, sign * 104, 154)),
            sp((40, sign * 126, 164)),
            3.8 * scale,
            skin,
            8,
        )
        assign_to_bone(thumb, armature, bone)
        objects.append(thumb)

    for side, sign in (("Left", 1), ("Right", -1)):
        add_tattoo_band(f"{label}_Tattoo_{side}_UpperArmBand", sp((5, sign * 67, 310)), sr((4, 26, 8)), tattoo, f"upperarm_{'l' if sign > 0 else 'r'}", armature, objects)
        add_tattoo_band(f"{label}_Bracer_{side}_Iron", sp((9, sign * 96, 202)), sr((10, 24, 20)), iron, f"lowerarm_{'l' if sign > 0 else 'r'}", armature, objects)
        add_tattoo_band(f"{label}_Tattoo_{side}_ThighMark", sp((9, sign * 38, 170)), sr((5, 28, 18)), tattoo, f"thigh_{'l' if sign > 0 else 'r'}", armature, objects)

    for socket_name, location, bone_name in [
        ("SOCKET_hand_r_weapon", sp((20, -122, 150)), "hand_r"),
        ("SOCKET_hand_l_offhand", sp((20, 122, 150)), "hand_l"),
        ("SOCKET_hand_r_twohand_grip", sp((28, -116, 168)), "hand_r"),
        ("SOCKET_hand_l_twohand_grip", sp((28, 116, 168)), "hand_l"),
        ("SOCKET_back_large_weapon", sp((-40, -18, 330)), "chest"),
        ("SOCKET_back_shield", sp((-44, 18, 318)), "chest"),
        ("SOCKET_belt_tool_l", sp((18, 54, 218)), "pelvis"),
        ("SOCKET_belt_tool_r", sp((18, -54, 218)), "pelvis"),
        ("SOCKET_head_hair_ornament", sp((12, 0, 452)), "head"),
        ("SOCKET_chest_talisman", sp((42, 0, 300)), "chest"),
        ("SOCKET_vfx_rune_hand_l", sp((24, 112, 151)), "hand_l"),
        ("SOCKET_vfx_rune_hand_r", sp((24, -112, 151)), "hand_r"),
        ("SOCKET_vfx_stomp_ground", sp((50, 0, 4)), "root"),
    ]:
        add_socket_empty(socket_name, location, armature, bone_name)

    return armature, objects


def export_variant(name: str, gender_label: str, height_cm: float) -> None:
    clear_scene()
    setup_scene()
    materials = create_materials(GIANT_MATERIALS)
    scale = height_cm / GIANT_TEMPLATE_HEIGHT_CM
    armature, objects = add_giant_variant(gender_label, f"SKEL_{name}", scale, 0.0, materials)
    add_asset_metadata(
        name,
        f"First-pass DCC review Giant {gender_label.lower()} body source at {height_cm:.0f} cm A04 baseline; final sculpt, skinning, physics, LODs, and textures pending",
        f"/Game/Aerathea/Characters/Giants/Base/{name}",
    )
    export_path = EXPORT_ROOT / f"Characters/Giants/SK_GIA_Base_A01/{name}.fbx"
    export_skeletal_fbx(export_path, objects, armature, bake_anim=False)
    print(f"Exported {export_path.relative_to(ROOT)}")


def add_scale_marker(name: str, height: float, y: float, materials: dict[str, bpy.types.Material]) -> None:
    mat = materials["M_AET_ScaleMarker_Blockout_A01"]
    add_ellipsoid_obj(f"{name}_Head", (0, y, height - 10), (8, 8, 10), mat, 10, 5)
    add_cylinder_between(f"{name}_Body", (0, y, height - 24), (0, y, height * 0.42), max(3.5, height * 0.035), mat, 10)
    add_cylinder_between(f"{name}_LegL", (0, y + height * 0.025, height * 0.42), (4, y + height * 0.035, 3), max(2.0, height * 0.018), mat, 8)
    add_cylinder_between(f"{name}_LegR", (0, y - height * 0.025, height * 0.42), (4, y - height * 0.035, 3), max(2.0, height * 0.018), mat, 8)


def render_review() -> None:
    clear_scene()
    setup_scene()
    bpy.context.scene.view_settings.view_transform = "Standard"
    bpy.context.scene.view_settings.exposure = 0.0
    bpy.context.scene.view_settings.gamma = 1.0
    if bpy.context.scene.world is not None:
        bpy.context.scene.world.color = (0.62, 0.62, 0.62)
    materials = create_materials(GIANT_MATERIALS)
    make_review_materials_readable(materials)
    add_giant_variant("Male", "SKEL_GIA_Base_Male_A01", GIANT_MALE_BASELINE_CM / GIANT_TEMPLATE_HEIGHT_CM, -82.0, materials)
    add_giant_variant("Female", "SKEL_GIA_Base_Female_A01", GIANT_FEMALE_BASELINE_CM / GIANT_TEMPLATE_HEIGHT_CM, 112.0, materials)
    add_scale_marker("Scale_180cm_Human", 180.0, -250.0, materials)
    add_scale_marker("Scale_110cm_Gnome", 110.0, -315.0, materials)
    add_scale_marker("Scale_270cm_Minotaur", 270.0, 300.0, materials)

    add_asset_metadata(
        "SK_GIA_Base_A01",
        "Approved Giant base first-pass DCC review scene with 470 cm male and 442 cm female A04 baselines and scale markers",
        "/Game/Aerathea/Characters/Giants/Base/",
    )

    bpy.ops.object.light_add(type="AREA", location=(780, -360, 660))
    key = bpy.context.object
    key.name = "AET_GiantReview_KeyLight"
    key.data.energy = 4200
    key.data.size = 720
    bpy.ops.object.light_add(type="AREA", location=(720, 260, 380))
    fill = bpy.context.object
    fill.name = "AET_GiantReview_FillLight"
    fill.data.energy = 1800
    fill.data.size = 900
    bpy.ops.object.camera_add(location=(1000, 0, 265))
    camera = bpy.context.object
    target = Vector((10, 0, 235))
    direction = target - Vector(camera.location)
    camera.rotation_euler = direction.to_track_quat("-Z", "Y").to_euler()
    camera.data.type = "ORTHO"
    camera.data.ortho_scale = 720
    bpy.context.scene.camera = camera
    bpy.context.scene.render.resolution_x = 1800
    bpy.context.scene.render.resolution_y = 1200

    blend_path = BLENDER_ROOT / "Characters/Giants/SK_GIA_Base_A01/SK_GIA_Base_A01.blend"
    blend_path.parent.mkdir(parents=True, exist_ok=True)
    bpy.ops.wm.save_as_mainfile(filepath=str(blend_path))
    print(f"Built {blend_path.relative_to(ROOT)}")

    REVIEW_ROOT.mkdir(parents=True, exist_ok=True)
    bpy.context.scene.render.filepath = str(REVIEW_ROOT / "SK_GIA_Base_A01_DCCReview.png")
    bpy.ops.render.render(write_still=True)
    print(f"Rendered {(REVIEW_ROOT / 'SK_GIA_Base_A01_DCCReview.png').relative_to(ROOT)}")


def main() -> None:
    export_variant("SK_GIA_Base_Male_A01", "Male", GIANT_MALE_BASELINE_CM)
    export_variant("SK_GIA_Base_Female_A01", "Female", GIANT_FEMALE_BASELINE_CM)
    render_review()


if __name__ == "__main__":
    main()
