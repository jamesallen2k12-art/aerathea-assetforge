#!/usr/bin/env python3
"""Build the first-pass Aerathea Infernal Hunter review source.

Run with:
    blender --background --python Tools/DCC/build_infernal_hunter.py

This creates deterministic review geometry for the approved fourth Infernal
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
REVIEW_ROOT = ROOT / "Saved" / "Automation" / "InfernalHunterReview"

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


ASSET_NAME = "SK_INF_Hunter_A01"
HEIGHT_CM = 214.0
SOURCE_REL = "Characters/Infernals/Hunter/SK_INF_Hunter_A01"
EXPORT_REL = "Characters/Infernals/Hunter/SK_INF_Hunter_A01"

INF_HUNTER_MATERIALS = {
    "M_INF_Hunter_Skin_Blockout_A01": (0.52, 0.075, 0.060),
    "M_INF_Hunter_HornClaw_Blockout_A01": (0.025, 0.020, 0.018),
    "M_INF_Hunter_Wing_Blockout_A01": (0.10, 0.035, 0.040),
    "M_INF_Hunter_HarnessLeather_Blockout_A01": (0.035, 0.034, 0.037),
    "M_INF_Hunter_PursuitArmor_Blockout_A01": (0.028, 0.026, 0.032),
    "M_INF_Hunter_BoneHorn_Blockout_A01": (0.50, 0.43, 0.32),
    "M_INF_Hunter_SightMarkGlow_Blockout_A01": (0.72, 0.06, 1.00),
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
    shoulder = height * 0.112
    hip = height * 0.055
    return [
        ("root", (0, 0, 0), (0, 0, max(8.0, height * 0.07)), None),
        ("pelvis", (0, 0, height * 0.44), (0, 0, height * 0.54), "root"),
        ("spine_01", (0, 0, height * 0.54), (0, 0, height * 0.67), "pelvis"),
        ("chest", (0, 0, height * 0.67), (0, 0, height * 0.79), "spine_01"),
        ("neck", (0, 0, height * 0.79), (0, 0, height * 0.84), "chest"),
        ("head", (0, 0, height * 0.84), (0, 0, height * 0.96), "neck"),
        ("tail_01", (-8, 0, height * 0.43), (-height * 0.17, 0, height * 0.34), "pelvis"),
        ("tail_02", (-height * 0.17, 0, height * 0.34), (-height * 0.40, 0, height * 0.20), "tail_01"),
        ("wing_l", (-6, shoulder * 0.60, height * 0.71), (-height * 0.16, shoulder * 1.04, height * 0.50), "chest"),
        ("wing_r", (-6, -shoulder * 0.60, height * 0.71), (-height * 0.16, -shoulder * 1.04, height * 0.50), "chest"),
        ("upperarm_l", (0, shoulder, height * 0.71), (height * 0.08, shoulder * 1.36, height * 0.53), "chest"),
        ("lowerarm_l", (height * 0.08, shoulder * 1.36, height * 0.53), (height * 0.13, shoulder * 1.44, height * 0.34), "upperarm_l"),
        ("hand_l", (height * 0.13, shoulder * 1.44, height * 0.34), (height * 0.24, shoulder * 1.44, height * 0.29), "lowerarm_l"),
        ("upperarm_r", (0, -shoulder, height * 0.71), (height * 0.08, -shoulder * 1.36, height * 0.53), "chest"),
        ("lowerarm_r", (height * 0.08, -shoulder * 1.36, height * 0.53), (height * 0.13, -shoulder * 1.44, height * 0.34), "upperarm_r"),
        ("hand_r", (height * 0.13, -shoulder * 1.44, height * 0.34), (height * 0.24, -shoulder * 1.44, height * 0.29), "lowerarm_r"),
        ("thigh_l", (0, hip, height * 0.44), (height * 0.08, hip * 1.12, height * 0.25), "pelvis"),
        ("calf_l", (height * 0.08, hip * 1.12, height * 0.25), (height * 0.12, hip * 1.05, height * 0.055), "thigh_l"),
        ("foot_l", (height * 0.12, hip * 1.05, height * 0.055), (height * 0.25, hip * 1.05, 4), "calf_l"),
        ("thigh_r", (0, -hip, height * 0.44), (height * 0.08, -hip * 1.12, height * 0.25), "pelvis"),
        ("calf_r", (height * 0.08, -hip * 1.12, height * 0.25), (height * 0.12, -hip * 1.05, height * 0.055), "thigh_r"),
        ("foot_r", (height * 0.12, -hip * 1.05, height * 0.055), (height * 0.25, -hip * 1.05, 4), "calf_r"),
    ]


def add_skull_belt(label: str, armature: bpy.types.Object, objects: list[bpy.types.Object], materials: dict[str, bpy.types.Material]) -> None:
    height = HEIGHT_CM
    bone = materials["M_INF_Hunter_BoneHorn_Blockout_A01"]
    armor = materials["M_INF_Hunter_PursuitArmor_Blockout_A01"]
    for index, y in enumerate((-10.0, 0.0, 10.0), 1):
        skull = add_ellipsoid_obj(f"{label}_SmallBoneMark_{index}", (22.0, y, height * 0.465), (3.4, 2.6, 3.2), bone, 8, 4)
        add_assigned(skull, armature, "pelvis", objects)
        jaw = add_box_obj(f"{label}_SmallBoneMark_{index}_Jaw", (25.0, y, height * 0.442), (2.2, 2.0, 1.6), bone)
        add_assigned(jaw, armature, "pelvis", objects)
    add_assigned(add_box_obj(f"{label}_Belt_LowWrapBand", (13.0, 0.0, height * 0.49), (5.0, 37.0, 3.2), armor), armature, "pelvis", objects)


def add_infernal_hunter(
    label: str,
    armature_name: str,
    materials: dict[str, bpy.types.Material],
) -> tuple[bpy.types.Object, list[bpy.types.Object]]:
    height = HEIGHT_CM
    shoulder = height * 0.112
    hip = height * 0.055
    wing_span = height * 0.43
    tail_len = height * 0.52

    armature = create_armature(armature_name, make_bones(height))
    objects: list[bpy.types.Object] = []

    skin = materials["M_INF_Hunter_Skin_Blockout_A01"]
    horn = materials["M_INF_Hunter_HornClaw_Blockout_A01"]
    wing = materials["M_INF_Hunter_Wing_Blockout_A01"]
    cloth = materials["M_INF_Hunter_HarnessLeather_Blockout_A01"]
    armor = materials["M_INF_Hunter_PursuitArmor_Blockout_A01"]
    bone = materials["M_INF_Hunter_BoneHorn_Blockout_A01"]
    glow = materials["M_INF_Hunter_SightMarkGlow_Blockout_A01"]

    body_parts = [
        (add_ellipsoid_obj(f"{label}_Pelvis", (0, 0, height * 0.44), (height * 0.050, hip * 1.12, height * 0.050), skin, 14, 7), "pelvis"),
        (add_ellipsoid_obj(f"{label}_Torso", (height * 0.025, 0, height * 0.61), (height * 0.070, shoulder * 0.78, height * 0.105), skin, 16, 8), "spine_01"),
        (add_ellipsoid_obj(f"{label}_Chest", (height * 0.027, 0, height * 0.71), (height * 0.078, shoulder * 0.94, height * 0.075), skin, 16, 8), "chest"),
        (add_cylinder_between(f"{label}_Neck", (height * 0.02, 0, height * 0.78), (height * 0.03, 0, height * 0.84), height * 0.018, skin, 10), "neck"),
        (add_ellipsoid_obj(f"{label}_Head", (height * 0.046, 0, height * 0.90), (height * 0.038, height * 0.034, height * 0.052), skin, 14, 7), "head"),
        (add_box_obj(f"{label}_Brow_Ridge", (height * 0.070, 0, height * 0.917), (height * 0.035, height * 0.055, height * 0.010), skin), "head"),
        (add_box_obj(f"{label}_Jaw", (height * 0.076, 0, height * 0.875), (height * 0.034, height * 0.044, height * 0.021), skin), "head"),
    ]
    for obj, bone_name in body_parts:
        add_assigned(obj, armature, bone_name, objects)

    for side, sign, suffix in (("L", 1, "l"), ("R", -1, "r")):
        add_assigned(add_cone_between(f"{label}_Horn_{side}_SweptMain", (5.0, sign * 5.0, height * 0.938), (-18.0, sign * 18.0, height * 1.000), 2.6, 0.6, bone, 10), armature, "head", objects)
        add_assigned(add_cone_between(f"{label}_Horn_{side}_LowSweep", (0.0, sign * 13.0, height * 0.920), (-27.0, sign * 29.0, height * 0.964), 2.0, 0.4, bone, 8), armature, "head", objects)
        add_assigned(add_diamond_obj(f"{label}_BrowSight_EyeGlow_{side}", (height * 0.080, sign * height * 0.013, height * 0.915), (1.4, 1.6, 2.2), glow), armature, "head", objects)

        add_assigned(add_cylinder_between(f"{label}_UpperArm_{side}", (0, sign * shoulder, height * 0.71), (height * 0.08, sign * shoulder * 1.36, height * 0.53), height * 0.019, skin, 12), armature, f"upperarm_{suffix}", objects)
        add_assigned(add_cylinder_between(f"{label}_LowerArm_{side}", (height * 0.08, sign * shoulder * 1.36, height * 0.53), (height * 0.13, sign * shoulder * 1.44, height * 0.34), height * 0.017, skin, 12), armature, f"lowerarm_{suffix}", objects)
        add_assigned(add_box_obj(f"{label}_HunterBracer_{side}_LightClawGuard", (height * 0.115, sign * shoulder * 1.42, height * 0.43), (height * 0.030, height * 0.042, height * 0.052), armor), armature, f"lowerarm_{suffix}", objects)
        add_assigned(add_box_obj(f"{label}_HunterBracer_{side}_SightBrand", (height * 0.134, sign * shoulder * 1.44, height * 0.43), (height * 0.009, height * 0.010, height * 0.060), glow), armature, f"lowerarm_{suffix}", objects)
        add_assigned(add_ellipsoid_obj(f"{label}_Hand_{side}_OpenClaw", (height * 0.18, sign * shoulder * 1.45, height * 0.305), (height * 0.027, height * 0.017, height * 0.019), skin, 10, 5), armature, f"hand_{suffix}", objects)
        add_assigned(add_ellipsoid_obj(f"{label}_ClawTargetMarkGlow_{side}", (height * 0.232, sign * shoulder * 1.48, height * 0.325), (3.2, 3.2, 3.2), glow, 8, 4), armature, f"hand_{suffix}", objects)
        for index, spread in enumerate((-0.014, 0.0, 0.014), 1):
            add_assigned(
                add_cone_between(
                    f"{label}_Claw_{side}_{index}",
                    (height * 0.205, sign * (shoulder * 1.45 + height * spread), height * 0.305),
                    (height * 0.260, sign * (shoulder * 1.45 + height * spread), height * 0.292),
                    max(0.45, height * 0.004),
                    0.0,
                    horn,
                    8,
                ),
                armature,
                f"hand_{suffix}",
                objects,
            )

        add_assigned(add_cylinder_between(f"{label}_Thigh_{side}", (0, sign * hip, height * 0.43), (height * 0.08, sign * hip * 1.12, height * 0.25), height * 0.023, skin, 12), armature, f"thigh_{suffix}", objects)
        add_assigned(add_cylinder_between(f"{label}_Calf_{side}", (height * 0.08, sign * hip * 1.12, height * 0.25), (height * 0.12, sign * hip * 1.05, height * 0.055), height * 0.018, skin, 12), armature, f"calf_{suffix}", objects)
        add_assigned(add_box_obj(f"{label}_ShinGuard_{side}_LightPlate", (height * 0.095, sign * hip * 1.08, height * 0.145), (height * 0.024, height * 0.030, height * 0.080), armor), armature, f"calf_{suffix}", objects)
        add_assigned(add_ellipsoid_obj(f"{label}_Foot_{side}_Clawed", (height * 0.19, sign * hip * 1.05, height * 0.030), (height * 0.049, height * 0.017, height * 0.016), skin, 10, 5), armature, f"foot_{suffix}", objects)

        root = (-height * 0.012, sign * shoulder * 0.58, height * 0.705)
        tip = (-wing_span, sign * (shoulder * 0.92 + wing_span * 0.16), height * 0.49)
        add_assigned(add_cylinder_between(f"{label}_Wing_{side}_LeadingFinger", root, tip, max(1.2, height * 0.008), horn, 8), armature, f"wing_{suffix}", objects)
        add_assigned(add_cylinder_between(f"{label}_Wing_{side}_LowerFinger", (-height * 0.045, sign * shoulder * 0.62, height * 0.66), (-wing_span * 0.78, sign * (shoulder * 0.84 + wing_span * 0.12), height * 0.40), max(0.9, height * 0.005), horn, 8), armature, f"wing_{suffix}", objects)
        add_assigned(add_ellipsoid_obj(f"{label}_Wing_{side}_TightMembrane", (-wing_span * 0.43, sign * (shoulder * 0.78 + wing_span * 0.09), height * 0.53), (max(4.0, wing_span * 0.36), max(3.0, wing_span * 0.075), max(5.0, height * 0.095)), wing, 10, 5), armature, f"wing_{suffix}", objects)
        add_assigned(add_box_obj(f"{label}_WingStrapAnchor_{side}", (-height * 0.002, sign * shoulder * 0.66, height * 0.685), (height * 0.030, height * 0.030, height * 0.040), armor), armature, f"wing_{suffix}", objects)
        add_assigned(add_diamond_obj(f"{label}_WingRootTargetMark_{side}", (-height * 0.010, sign * shoulder * 0.60, height * 0.69), (1.8, 2.2, 3.0), glow), armature, f"wing_{suffix}", objects)

    add_assigned(add_cylinder_between(f"{label}_Tail_Base", (-height * 0.03, 0, height * 0.42), (-tail_len * 0.50, 0, height * 0.30), height * 0.017, skin, 10), armature, "tail_01", objects)
    add_assigned(add_cone_between(f"{label}_Tail_BalanceTaper", (-tail_len * 0.50, 0, height * 0.30), (-tail_len, 0, height * 0.18), height * 0.015, max(0.7, height * 0.0045), skin, 10), armature, "tail_02", objects)
    add_assigned(add_box_obj(f"{label}_TailRootGuard_LightPlate", (-height * 0.095, 0, height * 0.35), (height * 0.050, height * 0.052, height * 0.035), armor), armature, "tail_01", objects)
    add_assigned(add_diamond_obj(f"{label}_TailTipTargetMarkGlow", (-tail_len, 0, height * 0.18), (2.5, 2.0, 2.7), glow), armature, "tail_02", objects)

    add_assigned(add_box_obj(f"{label}_LightChestPlate", (height * 0.088, 0, height * 0.665), (height * 0.018, shoulder * 1.05, height * 0.100), armor), armature, "chest", objects)
    add_assigned(add_diamond_obj(f"{label}_BrandGlow_Chest", (height * 0.100, 0, height * 0.665), (height * 0.006, height * 0.011, height * 0.026), glow), armature, "chest", objects)
    add_assigned(add_diamond_obj(f"{label}_TargetMark_Chest", (height * 0.106, 0, height * 0.708), (height * 0.007, height * 0.014, height * 0.024), glow), armature, "chest", objects)
    add_assigned(add_box_obj(f"{label}_Back_CloseWrapPlate", (-height * 0.030, 0, height * 0.68), (height * 0.020, shoulder * 1.00, height * 0.085), armor), armature, "chest", objects)
    add_assigned(add_box_obj(f"{label}_HoodCollar_CloseWrap", (height * 0.030, 0, height * 0.785), (height * 0.030, shoulder * 1.02, height * 0.040), cloth), armature, "neck", objects)
    add_assigned(add_box_obj(f"{label}_HarnessLeather_Front", (height * 0.070, 0, height * 0.33), (height * 0.014, shoulder * 0.62, height * 0.190), cloth), armature, "pelvis", objects)
    add_assigned(add_box_obj(f"{label}_HarnessLeather_Back", (-height * 0.040, 0, height * 0.35), (height * 0.012, shoulder * 0.56, height * 0.170), cloth), armature, "pelvis", objects)
    for side, sign in (("L", 1), ("R", -1)):
        add_assigned(add_box_obj(f"{label}_HarnessLeather_Side_{side}", (height * 0.018, sign * shoulder * 0.52, height * 0.35), (height * 0.012, height * 0.022, height * 0.155), cloth), armature, "pelvis", objects)
        add_assigned(add_box_obj(f"{label}_ShoulderWrapAnchor_{side}", (height * 0.020, sign * shoulder * 0.98, height * 0.735), (height * 0.035, height * 0.048, height * 0.030), armor), armature, "chest", objects)
        add_assigned(add_cone_between(f"{label}_ShoulderBoneSpike_{side}", (height * 0.028, sign * shoulder * 1.16, height * 0.746), (height * 0.056, sign * shoulder * 1.48, height * 0.760), height * 0.006, 0.0, bone, 7), armature, "chest", objects)

    add_skull_belt(label, armature, objects, materials)

    sockets = [
        ("SOCKET_hand_l_claw", (height * 0.260, shoulder * 1.45, height * 0.292), "hand_l"),
        ("SOCKET_hand_r_claw", (height * 0.260, -shoulder * 1.45, height * 0.292), "hand_r"),
        ("SOCKET_hand_l_cast", (height * 0.235, shoulder * 1.48, height * 0.325), "hand_l"),
        ("SOCKET_hand_r_cast", (height * 0.235, -shoulder * 1.48, height * 0.325), "hand_r"),
        ("SOCKET_vfx_hand_l", (height * 0.235, shoulder * 1.48, height * 0.325), "hand_l"),
        ("SOCKET_vfx_hand_r", (height * 0.235, -shoulder * 1.48, height * 0.325), "hand_r"),
        ("SOCKET_vfx_eye_l", (height * 0.080, height * 0.013, height * 0.915), "head"),
        ("SOCKET_vfx_eye_r", (height * 0.080, -height * 0.013, height * 0.915), "head"),
        ("SOCKET_vfx_brand_chest", (height * 0.106, 0, height * 0.67), "chest"),
        ("SOCKET_vfx_brand_forearm_l", (height * 0.108, shoulder * 1.60, height * 0.47), "lowerarm_l"),
        ("SOCKET_vfx_brand_forearm_r", (height * 0.108, -shoulder * 1.60, height * 0.47), "lowerarm_r"),
        ("SOCKET_vfx_wing_root_l", (-height * 0.010, shoulder * 0.60, height * 0.69), "wing_l"),
        ("SOCKET_vfx_wing_root_r", (-height * 0.010, -shoulder * 0.60, height * 0.69), "wing_r"),
        ("SOCKET_wing_l_tip", (-wing_span, shoulder * 0.92 + wing_span * 0.16, height * 0.49), "wing_l"),
        ("SOCKET_wing_r_tip", (-wing_span, -shoulder * 0.92 - wing_span * 0.16, height * 0.49), "wing_r"),
        ("SOCKET_tail_tip", (-tail_len, 0, height * 0.18), "tail_02"),
        ("SOCKET_vfx_tail_tip", (-tail_len, 0, height * 0.18), "tail_02"),
        ("SOCKET_vfx_regen_core", (height * 0.050, 0, height * 0.58), "spine_01"),
        ("SOCKET_vfx_mouth", (height * 0.087, 0, height * 0.875), "head"),
        ("SOCKET_vfx_target_mark", (height * 0.110, 0, height * 0.708), "chest"),
        ("SOCKET_vfx_brow_sight", (height * 0.086, 0, height * 0.918), "head"),
        ("SOCKET_vfx_pursuit_burst", (height * 0.050, 0, height * 0.66), "chest"),
        ("SOCKET_pounce_trace", (height * 0.238, 0, height * 0.39), "chest"),
        ("SOCKET_claw_takedown_trace", (height * 0.258, 0, height * 0.30), "chest"),
        ("SOCKET_tail_balance_trace", (-tail_len * 0.80, 0, height * 0.22), "tail_02"),
        ("SOCKET_tracking_center", (height * 0.07, 0, height * 0.43), "pelvis"),
        ("SOCKET_wing_burst_trace", (-height * 0.155, 0, height * 0.63), "chest"),
    ]
    for socket_name, location, bone_name in sockets:
        add_socket_empty(socket_name, location, armature, bone_name)

    return armature, objects


def export_asset() -> None:
    clear_scene()
    setup_scene()
    materials = create_materials(INF_HUNTER_MATERIALS)
    armature, objects = add_infernal_hunter(ASSET_NAME, f"SKEL_{ASSET_NAME}", materials)
    add_asset_metadata(
        ASSET_NAME,
        "First-pass Infernal Hunter class overlay with alert tracking posture, swept horns, folded pursuit wings, harness leather, light pursuit armor, brow sight glow, target-mark hooks, and pursuit/wing-burst trace sockets; final sculpt, retopo, skinning, physics, LODs, animation, and textures pending",
        "/Game/Aerathea/Characters/Infernals/Hunter/SK_INF_Hunter_A01",
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

    materials = create_materials(INF_HUNTER_MATERIALS)
    make_review_materials_readable(materials)
    add_infernal_hunter(ASSET_NAME, f"SKEL_{ASSET_NAME}", materials)
    add_scale_marker("Scale_Humanoid_180cm", 180.0, -170.0, materials["M_AET_ScaleMarker_Humanoid_A01"])
    add_label("Humanoid 180cm", (0, -170.0, 14.0), 10.0)
    add_scale_marker("Scale_GreaterBand_244cm", 244.0, 170.0, materials["M_AET_ScaleMarker_Blockout_A01"])
    add_label("Greater band 244cm", (0, 170.0, 14.0), 10.0)
    add_asset_metadata(
        ASSET_NAME,
        "Approved Infernal Hunter first-pass DCC review scene with 214 cm Standard/Greater-band pursuit tracker, 180 cm humanoid marker, and 244 cm Greater-band marker",
        "/Game/Aerathea/Characters/Infernals/Hunter/SK_INF_Hunter_A01",
    )

    bpy.ops.object.light_add(type="AREA", location=(520, -360, 430))
    key = bpy.context.object
    key.name = "AET_InfernalHunterReview_KeyLight"
    key.data.energy = 7200
    key.data.size = 560
    bpy.ops.object.light_add(type="AREA", location=(380, 350, 300))
    fill = bpy.context.object
    fill.name = "AET_InfernalHunterReview_FillLight"
    fill.data.energy = 3400
    fill.data.size = 700
    bpy.ops.object.light_add(type="SUN", location=(0, 0, 500), rotation=(math.radians(52), 0, math.radians(35)))
    sun = bpy.context.object
    sun.name = "AET_InfernalHunterReview_SunFill"
    sun.data.energy = 1.15

    bpy.ops.object.camera_add(location=(680, -540, 280))
    camera = bpy.context.object
    target = Vector((12, 0, 125))
    direction = target - Vector(camera.location)
    camera.rotation_euler = direction.to_track_quat("-Z", "Y").to_euler()
    camera.data.type = "ORTHO"
    camera.data.ortho_scale = 480
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
