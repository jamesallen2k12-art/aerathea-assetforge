#!/usr/bin/env python3
"""Build the first-pass Aerathea Infernal Warrior review source.

Run with:
    blender --background --python Tools/DCC/build_infernal_warrior.py

This creates deterministic review geometry for the approved second Infernal
class child. It is not final sculpted or painted production art.
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
REVIEW_ROOT = ROOT / "Saved" / "Automation" / "InfernalWarriorReview"

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
    setup_scene,
)


ASSET_NAME = "SK_INF_Warrior_A01"
HEIGHT_CM = 238.0
SOURCE_REL = "Characters/Infernals/Warrior/SK_INF_Warrior_A01"
EXPORT_REL = "Characters/Infernals/Warrior/SK_INF_Warrior_A01"

INF_WARRIOR_MATERIALS = {
    "M_INF_Warrior_Skin_Blockout_A01": (0.62, 0.11, 0.075),
    "M_INF_Warrior_HornClaw_Blockout_A01": (0.025, 0.020, 0.018),
    "M_INF_Warrior_Wing_Blockout_A01": (0.14, 0.045, 0.040),
    "M_INF_Warrior_RitualCloth_Blockout_A01": (0.075, 0.055, 0.052),
    "M_INF_Warrior_ObsidianArmor_Blockout_A01": (0.035, 0.032, 0.038),
    "M_INF_Warrior_BoneOrnaments_Blockout_A01": (0.58, 0.49, 0.35),
    "M_INF_Warrior_AbyssalGlow_Blockout_A01": (1.00, 0.24, 0.035),
    "M_AET_ScaleMarker_Blockout_A01": (0.12, 0.12, 0.11),
    "M_AET_ScaleMarker_Humanoid_A01": (0.34, 0.38, 0.42),
}


def make_review_materials_readable(materials: dict[str, bpy.types.Material]) -> None:
    for material in materials.values():
        color = material.diffuse_color
        material.use_nodes = True
        bsdf = material.node_tree.nodes.get("Principled BSDF")
        if bsdf is None:
            continue
        bsdf.inputs["Base Color"].default_value = color
        bsdf.inputs["Roughness"].default_value = 0.86
        if "Emission Color" in bsdf.inputs:
            bsdf.inputs["Emission Color"].default_value = (color[0] * 0.18, color[1] * 0.15, color[2] * 0.12, 1.0)
        if "Emission Strength" in bsdf.inputs:
            bsdf.inputs["Emission Strength"].default_value = 0.15
        if "Glow" in material.name:
            if "Emission Color" in bsdf.inputs:
                bsdf.inputs["Emission Color"].default_value = color
            if "Emission Strength" in bsdf.inputs:
                bsdf.inputs["Emission Strength"].default_value = 1.35


def add_assigned(obj: bpy.types.Object, armature: bpy.types.Object, bone: str, objects: list[bpy.types.Object]) -> None:
    assign_to_bone(obj, armature, bone)
    objects.append(obj)


def add_cone_between(
    name: str,
    start: tuple[float, float, float],
    end: tuple[float, float, float],
    radius_base: float,
    radius_tip: float,
    material: bpy.types.Material,
    vertices: int = 10,
) -> bpy.types.Object:
    start_v = Vector(start)
    end_v = Vector(end)
    midpoint = (start_v + end_v) * 0.5
    direction = end_v - start_v
    bpy.ops.mesh.primitive_cone_add(
        vertices=vertices,
        radius1=radius_base,
        radius2=radius_tip,
        depth=direction.length,
        location=midpoint,
    )
    obj = bpy.context.object
    obj.name = name
    obj.data.name = f"{name}_Mesh"
    obj.rotation_euler = direction.to_track_quat("Z", "Y").to_euler()
    bpy.ops.object.transform_apply(location=False, rotation=False, scale=True)
    obj.data.materials.append(material)
    return obj


def add_diamond_obj(
    name: str,
    center: tuple[float, float, float],
    radii: tuple[float, float, float],
    material: bpy.types.Material,
) -> bpy.types.Object:
    x, y, z = radii
    cx, cy, cz = center
    verts = [
        (cx, cy, cz + z),
        (cx + x, cy, cz),
        (cx, cy + y, cz),
        (cx - x, cy, cz),
        (cx, cy - y, cz),
        (cx, cy, cz - z),
    ]
    faces = [
        (0, 1, 2),
        (0, 2, 3),
        (0, 3, 4),
        (0, 4, 1),
        (5, 2, 1),
        (5, 3, 2),
        (5, 4, 3),
        (5, 1, 4),
    ]
    mesh = bpy.data.meshes.new(f"{name}_Mesh")
    mesh.from_pydata(verts, [], faces)
    mesh.update()
    obj = bpy.data.objects.new(name, mesh)
    bpy.context.collection.objects.link(obj)
    obj.data.materials.append(material)
    return obj


def make_bones(height: float) -> list[tuple[str, tuple[float, float, float], tuple[float, float, float], str | None]]:
    shoulder = height * 0.118
    hip = height * 0.056
    return [
        ("root", (0, 0, 0), (0, 0, max(8.0, height * 0.07)), None),
        ("pelvis", (0, 0, height * 0.44), (0, 0, height * 0.54), "root"),
        ("spine_01", (0, 0, height * 0.54), (0, 0, height * 0.67), "pelvis"),
        ("chest", (0, 0, height * 0.67), (0, 0, height * 0.79), "spine_01"),
        ("neck", (0, 0, height * 0.79), (0, 0, height * 0.84), "chest"),
        ("head", (0, 0, height * 0.84), (0, 0, height * 0.96), "neck"),
        ("tail_01", (-8, 0, height * 0.43), (-height * 0.17, 0, height * 0.34), "pelvis"),
        ("tail_02", (-height * 0.17, 0, height * 0.34), (-height * 0.40, 0, height * 0.20), "tail_01"),
        ("wing_l", (-8, shoulder * 0.72, height * 0.73), (-height * 0.22, shoulder * 1.70, height * 0.60), "chest"),
        ("wing_r", (-8, -shoulder * 0.72, height * 0.73), (-height * 0.22, -shoulder * 1.70, height * 0.60), "chest"),
        ("upperarm_l", (0, shoulder, height * 0.73), (height * 0.06, shoulder * 1.52, height * 0.56), "chest"),
        ("lowerarm_l", (height * 0.06, shoulder * 1.52, height * 0.56), (height * 0.09, shoulder * 1.62, height * 0.37), "upperarm_l"),
        ("hand_l", (height * 0.09, shoulder * 1.62, height * 0.37), (height * 0.19, shoulder * 1.62, height * 0.32), "lowerarm_l"),
        ("upperarm_r", (0, -shoulder, height * 0.73), (height * 0.06, -shoulder * 1.52, height * 0.56), "chest"),
        ("lowerarm_r", (height * 0.06, -shoulder * 1.52, height * 0.56), (height * 0.09, -shoulder * 1.62, height * 0.37), "upperarm_r"),
        ("hand_r", (height * 0.09, -shoulder * 1.62, height * 0.37), (height * 0.19, -shoulder * 1.62, height * 0.32), "lowerarm_r"),
        ("thigh_l", (0, hip, height * 0.44), (height * 0.04, hip * 1.20, height * 0.24), "pelvis"),
        ("calf_l", (height * 0.04, hip * 1.20, height * 0.24), (height * 0.07, hip * 1.15, height * 0.055), "thigh_l"),
        ("foot_l", (height * 0.07, hip * 1.15, height * 0.055), (height * 0.20, hip * 1.15, 4), "calf_l"),
        ("thigh_r", (0, -hip, height * 0.44), (height * 0.04, -hip * 1.20, height * 0.24), "pelvis"),
        ("calf_r", (height * 0.04, -hip * 1.20, height * 0.24), (height * 0.07, -hip * 1.15, height * 0.055), "thigh_r"),
        ("foot_r", (height * 0.07, -hip * 1.15, height * 0.055), (height * 0.20, -hip * 1.15, 4), "calf_r"),
    ]


def add_skull_belt(label: str, armature: bpy.types.Object, objects: list[bpy.types.Object], materials: dict[str, bpy.types.Material]) -> None:
    height = HEIGHT_CM
    bone = materials["M_INF_Warrior_BoneOrnaments_Blockout_A01"]
    armor = materials["M_INF_Warrior_ObsidianArmor_Blockout_A01"]
    for index, y in enumerate((-24.0, -12.0, 0.0, 12.0, 24.0), 1):
        skull = add_ellipsoid_obj(f"{label}_SkullBelt_{index}", (31.0, y, height * 0.465), (5.2, 4.2, 5.0), bone, 10, 5)
        add_assigned(skull, armature, "pelvis", objects)
        jaw = add_box_obj(f"{label}_SkullBelt_{index}_Jaw", (35.0, y, height * 0.438), (4.0, 3.4, 2.4), bone)
        add_assigned(jaw, armature, "pelvis", objects)
    add_assigned(add_box_obj(f"{label}_Belt_ObsidianBand", (20.0, 0.0, height * 0.49), (7.0, 58.0, 5.0), armor), armature, "pelvis", objects)


def add_infernal_warrior(
    label: str,
    armature_name: str,
    materials: dict[str, bpy.types.Material],
) -> tuple[bpy.types.Object, list[bpy.types.Object]]:
    height = HEIGHT_CM
    shoulder = height * 0.118
    hip = height * 0.056
    wing_span = height * 0.50
    tail_len = height * 0.48

    armature = create_armature(armature_name, make_bones(height))
    objects: list[bpy.types.Object] = []

    skin = materials["M_INF_Warrior_Skin_Blockout_A01"]
    horn = materials["M_INF_Warrior_HornClaw_Blockout_A01"]
    wing = materials["M_INF_Warrior_Wing_Blockout_A01"]
    cloth = materials["M_INF_Warrior_RitualCloth_Blockout_A01"]
    armor = materials["M_INF_Warrior_ObsidianArmor_Blockout_A01"]
    bone = materials["M_INF_Warrior_BoneOrnaments_Blockout_A01"]
    glow = materials["M_INF_Warrior_AbyssalGlow_Blockout_A01"]

    body_parts = [
        (add_ellipsoid_obj(f"{label}_Pelvis", (0, 0, height * 0.45), (height * 0.060, hip * 1.35, height * 0.054), skin, 14, 7), "pelvis"),
        (add_ellipsoid_obj(f"{label}_Torso", (height * 0.02, 0, height * 0.62), (height * 0.086, shoulder * 0.96, height * 0.112), skin, 16, 8), "spine_01"),
        (add_ellipsoid_obj(f"{label}_Chest", (height * 0.02, 0, height * 0.72), (height * 0.096, shoulder * 1.18, height * 0.084), skin, 16, 8), "chest"),
        (add_cylinder_between(f"{label}_Neck", (height * 0.02, 0, height * 0.78), (height * 0.03, 0, height * 0.84), height * 0.018, skin, 10), "neck"),
        (add_ellipsoid_obj(f"{label}_Head", (height * 0.046, 0, height * 0.90), (height * 0.038, height * 0.034, height * 0.052), skin, 14, 7), "head"),
        (add_box_obj(f"{label}_Brow_Ridge", (height * 0.070, 0, height * 0.917), (height * 0.041, height * 0.064, height * 0.012), skin), "head"),
        (add_box_obj(f"{label}_Jaw", (height * 0.076, 0, height * 0.875), (height * 0.040, height * 0.050, height * 0.025), skin), "head"),
    ]
    for obj, bone_name in body_parts:
        add_assigned(obj, armature, bone_name, objects)

    for side, sign, suffix in (("L", 1, "l"), ("R", -1, "r")):
        add_assigned(add_cone_between(f"{label}_Horn_{side}_CrownMain", (6.0, sign * 6.0, height * 0.94), (-14.0, sign * 25.0, height * 1.025), 3.2, 0.8, bone, 12), armature, "head", objects)
        add_assigned(add_cone_between(f"{label}_Horn_{side}_Outer", (2.0, sign * 15.0, height * 0.925), (-24.0, sign * 43.0, height * 0.995), 2.6, 0.6, bone, 10), armature, "head", objects)
        add_assigned(add_diamond_obj(f"{label}_EyeGlow_{side}", (height * 0.080, sign * height * 0.013, height * 0.915), (1.6, 1.7, 2.6), glow), armature, "head", objects)

        add_assigned(add_cylinder_between(f"{label}_UpperArm_{side}", (0, sign * shoulder, height * 0.72), (height * 0.06, sign * shoulder * 1.52, height * 0.56), height * 0.023, skin, 12), armature, f"upperarm_{suffix}", objects)
        add_assigned(add_cylinder_between(f"{label}_LowerArm_{side}", (height * 0.06, sign * shoulder * 1.52, height * 0.56), (height * 0.09, sign * shoulder * 1.62, height * 0.37), height * 0.021, skin, 12), armature, f"lowerarm_{suffix}", objects)
        add_assigned(add_box_obj(f"{label}_WarriorBracer_{side}_HeavyClawGuard", (height * 0.087, sign * shoulder * 1.58, height * 0.47), (height * 0.045, height * 0.070, height * 0.060), armor), armature, f"lowerarm_{suffix}", objects)
        add_assigned(add_box_obj(f"{label}_WarriorBracer_{side}_RageBrand", (height * 0.114, sign * shoulder * 1.61, height * 0.47), (height * 0.012, height * 0.012, height * 0.080), glow), armature, f"lowerarm_{suffix}", objects)
        add_assigned(add_ellipsoid_obj(f"{label}_Hand_{side}_OpenClaw", (height * 0.14, sign * shoulder * 1.64, height * 0.335), (height * 0.031, height * 0.019, height * 0.022), skin, 10, 5), armature, f"hand_{suffix}", objects)
        add_assigned(add_ellipsoid_obj(f"{label}_ClawRageGlow_{side}", (height * 0.19, sign * shoulder * 1.67, height * 0.36), (5.8, 5.8, 5.8), glow, 10, 5), armature, f"hand_{suffix}", objects)
        for index, spread in enumerate((-0.014, 0.0, 0.014), 1):
            add_assigned(
                add_cone_between(
                    f"{label}_Claw_{side}_{index}",
                    (height * 0.163, sign * (shoulder * 1.64 + height * spread), height * 0.335),
                    (height * 0.208, sign * (shoulder * 1.64 + height * spread), height * 0.327),
                    max(0.45, height * 0.004),
                    0.0,
                    horn,
                    8,
                ),
                armature,
                f"hand_{suffix}",
                objects,
            )

        add_assigned(add_cylinder_between(f"{label}_Thigh_{side}", (0, sign * hip, height * 0.43), (height * 0.04, sign * hip * 1.20, height * 0.24), height * 0.028, skin, 12), armature, f"thigh_{suffix}", objects)
        add_assigned(add_cylinder_between(f"{label}_Calf_{side}", (height * 0.04, sign * hip * 1.20, height * 0.24), (height * 0.07, sign * hip * 1.15, height * 0.055), height * 0.022, skin, 12), armature, f"calf_{suffix}", objects)
        add_assigned(add_box_obj(f"{label}_Greave_{side}_ObsidianPlate", (height * 0.058, sign * hip * 1.18, height * 0.155), (height * 0.036, height * 0.040, height * 0.105), armor), armature, f"calf_{suffix}", objects)
        add_assigned(add_ellipsoid_obj(f"{label}_Foot_{side}_Clawed", (height * 0.15, sign * hip * 1.15, height * 0.030), (height * 0.055, height * 0.020, height * 0.018), skin, 10, 5), armature, f"foot_{suffix}", objects)

        root = (-height * 0.02, sign * shoulder * 0.72, height * 0.72)
        tip = (-wing_span, sign * (shoulder * 1.36 + wing_span * 0.35), height * 0.50)
        add_assigned(add_cylinder_between(f"{label}_Wing_{side}_LeadingFinger", root, tip, max(1.2, height * 0.008), horn, 8), armature, f"wing_{suffix}", objects)
        add_assigned(add_cylinder_between(f"{label}_Wing_{side}_LowerFinger", (-height * 0.05, sign * shoulder * 0.75, height * 0.67), (-wing_span * 0.78, sign * (shoulder * 1.22 + wing_span * 0.23), height * 0.42), max(1.0, height * 0.006), horn, 8), armature, f"wing_{suffix}", objects)
        add_assigned(add_ellipsoid_obj(f"{label}_Wing_{side}_MantleMembrane", (-wing_span * 0.46, sign * (shoulder * 1.00 + wing_span * 0.17), height * 0.56), (max(4.0, wing_span * 0.44), max(3.0, wing_span * 0.10), max(5.0, height * 0.11)), wing, 10, 5), armature, f"wing_{suffix}", objects)
        add_assigned(add_box_obj(f"{label}_WingRootGuard_{side}", (-height * 0.005, sign * shoulder * 0.82, height * 0.695), (height * 0.050, height * 0.050, height * 0.055), armor), armature, f"wing_{suffix}", objects)
        add_assigned(add_diamond_obj(f"{label}_WingRootGlow_{side}", (-height * 0.015, sign * shoulder * 0.74, height * 0.70), (2.5, 3.0, 4.0), glow), armature, f"wing_{suffix}", objects)

    add_assigned(add_cylinder_between(f"{label}_Tail_Base", (-height * 0.03, 0, height * 0.42), (-tail_len * 0.52, 0, height * 0.31), height * 0.020, skin, 10), armature, "tail_01", objects)
    add_assigned(add_cone_between(f"{label}_Tail_Taper", (-tail_len * 0.52, 0, height * 0.31), (-tail_len, 0, height * 0.20), height * 0.018, max(0.8, height * 0.006), skin, 10), armature, "tail_02", objects)
    add_assigned(add_box_obj(f"{label}_TailRootGuard_Obsidian", (-height * 0.115, 0, height * 0.35), (height * 0.075, height * 0.080, height * 0.048), armor), armature, "tail_01", objects)
    add_assigned(add_diamond_obj(f"{label}_TailTipGlow", (-tail_len, 0, height * 0.20), (4.0, 3.0, 4.0), glow), armature, "tail_02", objects)

    add_assigned(add_box_obj(f"{label}_ObsidianChestPlate", (height * 0.092, 0, height * 0.665), (height * 0.026, shoulder * 1.55, height * 0.145), armor), armature, "chest", objects)
    add_assigned(add_diamond_obj(f"{label}_BrandGlow_Chest", (height * 0.104, 0, height * 0.67), (height * 0.008, height * 0.014, height * 0.038), glow), armature, "chest", objects)
    add_assigned(add_diamond_obj(f"{label}_RageCore_Chest", (height * 0.116, 0, height * 0.715), (height * 0.010, height * 0.020, height * 0.032), glow), armature, "chest", objects)
    add_assigned(add_box_obj(f"{label}_Back_ObsidianMantlePlate", (-height * 0.035, 0, height * 0.69), (height * 0.030, shoulder * 1.35, height * 0.110), armor), armature, "chest", objects)
    add_assigned(add_box_obj(f"{label}_RitualCloth_Front", (height * 0.075, 0, height * 0.33), (height * 0.018, shoulder * 0.80, height * 0.250), cloth), armature, "pelvis", objects)
    add_assigned(add_box_obj(f"{label}_RitualCloth_Back", (-height * 0.045, 0, height * 0.35), (height * 0.016, shoulder * 0.72, height * 0.215), cloth), armature, "pelvis", objects)
    for side, sign in (("L", 1), ("R", -1)):
        add_assigned(add_box_obj(f"{label}_RitualCloth_Side_{side}", (height * 0.018, sign * shoulder * 0.68, height * 0.35), (height * 0.014, height * 0.030, height * 0.200), cloth), armature, "pelvis", objects)
        add_assigned(add_box_obj(f"{label}_WarriorPauldron_{side}_ObsidianBone", (height * 0.018, sign * shoulder * 1.18, height * 0.745), (height * 0.060, height * 0.088, height * 0.040), bone), armature, "chest", objects)
        add_assigned(add_cone_between(f"{label}_PauldronHorn_{side}", (height * 0.030, sign * shoulder * 1.42, height * 0.765), (height * 0.066, sign * shoulder * 1.94, height * 0.795), height * 0.012, 0.0, bone, 8), armature, "chest", objects)

    add_skull_belt(label, armature, objects, materials)

    sockets = [
        ("SOCKET_hand_l_claw", (height * 0.208, shoulder * 1.64, height * 0.327), "hand_l"),
        ("SOCKET_hand_r_claw", (height * 0.208, -shoulder * 1.64, height * 0.327), "hand_r"),
        ("SOCKET_hand_l_cast", (height * 0.195, shoulder * 1.67, height * 0.36), "hand_l"),
        ("SOCKET_hand_r_cast", (height * 0.195, -shoulder * 1.67, height * 0.36), "hand_r"),
        ("SOCKET_vfx_hand_l", (height * 0.195, shoulder * 1.67, height * 0.36), "hand_l"),
        ("SOCKET_vfx_hand_r", (height * 0.195, -shoulder * 1.67, height * 0.36), "hand_r"),
        ("SOCKET_vfx_eye_l", (height * 0.080, height * 0.013, height * 0.915), "head"),
        ("SOCKET_vfx_eye_r", (height * 0.080, -height * 0.013, height * 0.915), "head"),
        ("SOCKET_vfx_brand_chest", (height * 0.106, 0, height * 0.67), "chest"),
        ("SOCKET_vfx_brand_forearm_l", (height * 0.108, shoulder * 1.60, height * 0.47), "lowerarm_l"),
        ("SOCKET_vfx_brand_forearm_r", (height * 0.108, -shoulder * 1.60, height * 0.47), "lowerarm_r"),
        ("SOCKET_vfx_wing_root_l", (-height * 0.015, shoulder * 0.74, height * 0.70), "wing_l"),
        ("SOCKET_vfx_wing_root_r", (-height * 0.015, -shoulder * 0.74, height * 0.70), "wing_r"),
        ("SOCKET_wing_l_tip", (-wing_span, shoulder * 1.36 + wing_span * 0.35, height * 0.50), "wing_l"),
        ("SOCKET_wing_r_tip", (-wing_span, -shoulder * 1.36 - wing_span * 0.35, height * 0.50), "wing_r"),
        ("SOCKET_tail_tip", (-tail_len, 0, height * 0.20), "tail_02"),
        ("SOCKET_vfx_tail_tip", (-tail_len, 0, height * 0.20), "tail_02"),
        ("SOCKET_vfx_regen_core", (height * 0.050, 0, height * 0.58), "spine_01"),
        ("SOCKET_vfx_mouth", (height * 0.087, 0, height * 0.875), "head"),
        ("SOCKET_vfx_rage_core", (height * 0.122, 0, height * 0.715), "chest"),
        ("SOCKET_tail_sweep_trace", (-tail_len * 0.80, 0, height * 0.24), "tail_02"),
        ("SOCKET_wing_buffet_trace", (-height * 0.18, 0, height * 0.67), "chest"),
        ("SOCKET_body_check_trace", (height * 0.13, 0, height * 0.68), "chest"),
    ]
    for socket_name, location, bone_name in sockets:
        add_socket_empty(socket_name, location, armature, bone_name)

    return armature, objects


def export_asset() -> None:
    clear_scene()
    setup_scene()
    materials = create_materials(INF_WARRIOR_MATERIALS)
    armature, objects = add_infernal_warrior(ASSET_NAME, f"SKEL_{ASSET_NAME}", materials)
    add_asset_metadata(
        ASSET_NAME,
        "First-pass Infernal Warrior class overlay with horn crown, folded wings, heavy claw bracers, wing-root guards, tail-root armor, rage core, skull belt, and melee trace sockets; final sculpt, retopo, skinning, physics, LODs, animation, and textures pending",
        "/Game/Aerathea/Characters/Infernals/Warrior/SK_INF_Warrior_A01",
    )
    export_path = EXPORT_ROOT / EXPORT_REL / f"{ASSET_NAME}.fbx"
    export_skeletal_fbx(export_path, objects, armature, bake_anim=False)
    print(f"Exported {export_path.relative_to(ROOT)}")


def add_scale_marker(name: str, height: float, y: float, material: bpy.types.Material) -> None:
    add_ellipsoid_obj(f"{name}_Head", (0, y, height - 10), (8, 8, 10), material, 10, 5)
    add_cylinder_between(f"{name}_Body", (0, y, height - 24), (0, y, height * 0.42), max(3.5, height * 0.035), material, 10)
    add_cylinder_between(f"{name}_LegL", (0, y + height * 0.025, height * 0.42), (4, y + height * 0.035, 3), max(2.0, height * 0.018), material, 8)
    add_cylinder_between(f"{name}_LegR", (0, y - height * 0.025, height * 0.42), (4, y - height * 0.035, 3), max(2.0, height * 0.018), material, 8)


def add_label(text: str, location: tuple[float, float, float], size: float = 11.0) -> None:
    curve = bpy.data.curves.new(f"{text}_LabelCurve", "FONT")
    curve.body = text
    curve.align_x = "CENTER"
    curve.align_y = "CENTER"
    curve.size = size
    obj = bpy.data.objects.new(f"{text}_Label", curve)
    obj.location = location
    obj.rotation_euler[0] = math.radians(72)
    bpy.context.collection.objects.link(obj)


def render_review() -> None:
    clear_scene()
    setup_scene()
    bpy.context.scene.view_settings.view_transform = "Standard"
    bpy.context.scene.view_settings.exposure = 0.55
    bpy.context.scene.view_settings.gamma = 1.0
    if bpy.context.scene.world is not None:
        bpy.context.scene.world.color = (0.62, 0.60, 0.56)

    materials = create_materials(INF_WARRIOR_MATERIALS)
    make_review_materials_readable(materials)
    add_infernal_warrior(ASSET_NAME, f"SKEL_{ASSET_NAME}", materials)
    add_scale_marker("Scale_Humanoid_180cm", 180.0, -185.0, materials["M_AET_ScaleMarker_Humanoid_A01"])
    add_label("Humanoid 180cm", (0, -185.0, 14.0), 11.0)
    add_scale_marker("Scale_GreaterBand_244cm", 244.0, 180.0, materials["M_AET_ScaleMarker_Blockout_A01"])
    add_label("Greater band 244cm", (0, 180.0, 14.0), 11.0)
    add_asset_metadata(
        ASSET_NAME,
        "Approved Infernal Warrior first-pass DCC review scene with 238 cm Greater-band natural-weapon fighter, 180 cm humanoid marker, and 244 cm Greater-band marker",
        "/Game/Aerathea/Characters/Infernals/Warrior/SK_INF_Warrior_A01",
    )

    bpy.ops.object.light_add(type="AREA", location=(520, -360, 430))
    key = bpy.context.object
    key.name = "AET_InfernalWarriorReview_KeyLight"
    key.data.energy = 7200
    key.data.size = 560
    bpy.ops.object.light_add(type="AREA", location=(380, 350, 300))
    fill = bpy.context.object
    fill.name = "AET_InfernalWarriorReview_FillLight"
    fill.data.energy = 3400
    fill.data.size = 700
    bpy.ops.object.light_add(type="SUN", location=(0, 0, 500), rotation=(math.radians(52), 0, math.radians(35)))
    sun = bpy.context.object
    sun.name = "AET_InfernalWarriorReview_SunFill"
    sun.data.energy = 1.15

    bpy.ops.object.camera_add(location=(680, -540, 280))
    camera = bpy.context.object
    target = Vector((10, 0, 138))
    direction = target - Vector(camera.location)
    camera.rotation_euler = direction.to_track_quat("-Z", "Y").to_euler()
    camera.data.type = "ORTHO"
    camera.data.ortho_scale = 500
    bpy.context.scene.camera = camera
    bpy.context.scene.render.resolution_x = 1500
    bpy.context.scene.render.resolution_y = 1500

    blend_path = BLENDER_ROOT / SOURCE_REL / f"{ASSET_NAME}.blend"
    blend_path.parent.mkdir(parents=True, exist_ok=True)
    bpy.ops.wm.save_as_mainfile(filepath=str(blend_path))
    print(f"Built {blend_path.relative_to(ROOT)}")

    REVIEW_ROOT.mkdir(parents=True, exist_ok=True)
    review_path = REVIEW_ROOT / f"{ASSET_NAME}_DCCReview.png"
    bpy.context.scene.render.filepath = str(review_path)
    bpy.ops.render.render(write_still=True)
    print(f"Rendered {review_path.relative_to(ROOT)}")


def main() -> None:
    export_asset()
    render_review()


if __name__ == "__main__":
    main()
