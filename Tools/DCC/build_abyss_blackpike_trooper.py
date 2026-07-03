#!/usr/bin/env python3
"""Build the first-pass Aerathea Abyss BlackPike Trooper review source.

Run with:
    blender --background --python Tools/DCC/build_abyss_blackpike_trooper.py

This creates deterministic review geometry for scale, silhouette, skeleton,
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
REVIEW_ROOT = ROOT / "Saved" / "Automation" / "AbyssBlackPikeReview"

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


ASSET_NAME = "SK_ABY_BlackPikeTrooper_A01"
HEIGHT_CM = 220.0
SOURCE_REL = "Creatures/Abyss/SK_ABY_BlackPikeTrooper_A01"
EXPORT_REL = "Creatures/Abyss/SK_ABY_BlackPikeTrooper_A01"

ABYSS_MATERIALS = {
    "M_ABY_CharredFlesh_Blockout_A01": (0.08, 0.065, 0.065),
    "M_ABY_ScorchedIron_Blockout_A01": (0.055, 0.052, 0.050),
    "M_ABY_AshCloth_Blockout_A01": (0.075, 0.060, 0.085),
    "M_ABY_BoneHorn_Blockout_A01": (0.58, 0.49, 0.36),
    "M_ABY_PikeBlackIron_Blockout_A01": (0.035, 0.034, 0.036),
    "M_ABY_VoidGlow_Blockout_A01": (0.55, 0.10, 1.00),
    "M_ABY_EmberFissure_Blockout_A01": (1.00, 0.22, 0.04),
    "M_AET_ScaleMarker_Blockout_A01": (0.12, 0.12, 0.12),
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
            bsdf.inputs["Emission Color"].default_value = (color[0] * 0.20, color[1] * 0.20, color[2] * 0.20, 1.0)
        if "Emission Strength" in bsdf.inputs:
            bsdf.inputs["Emission Strength"].default_value = 0.20
        if "Glow" in material.name or "Ember" in material.name:
            if "Emission Color" in bsdf.inputs:
                bsdf.inputs["Emission Color"].default_value = color
            if "Emission Strength" in bsdf.inputs:
                bsdf.inputs["Emission Strength"].default_value = 1.2


def add_assigned(obj: bpy.types.Object, armature: bpy.types.Object, bone: str, objects: list[bpy.types.Object]) -> None:
    assign_to_bone(obj, armature, bone)
    objects.append(obj)


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


def add_cone_between(
    name: str,
    start: tuple[float, float, float],
    end: tuple[float, float, float],
    radius: float,
    material: bpy.types.Material,
    vertices: int = 10,
) -> bpy.types.Object:
    start_v = Vector(start)
    end_v = Vector(end)
    mid = (start_v + end_v) * 0.5
    length = (end_v - start_v).length
    bpy.ops.mesh.primitive_cone_add(vertices=vertices, radius1=radius, radius2=0.0, depth=length, location=mid)
    obj = bpy.context.object
    obj.name = name
    direction = end_v - start_v
    obj.rotation_euler = direction.to_track_quat("Z", "Y").to_euler()
    obj.data.materials.append(material)
    return obj


def make_bones(height: float) -> list[tuple[str, tuple[float, float, float], tuple[float, float, float], str | None]]:
    shoulder = height * 0.145
    arm_side = height * 0.215
    hip_side = height * 0.075
    return [
        ("root", (0, 0, 0), (0, 0, 12), None),
        ("pelvis", (0, 0, height * 0.43), (0, 0, height * 0.51), "root"),
        ("spine_01", (0, 0, height * 0.51), (0, 0, height * 0.66), "pelvis"),
        ("chest", (0, 0, height * 0.66), (0, 0, height * 0.79), "spine_01"),
        ("neck", (0, 0, height * 0.79), (0, 0, height * 0.85), "chest"),
        ("head", (0, 0, height * 0.85), (0, 0, height * 0.98), "neck"),
        ("clavicle_l", (0, shoulder * 0.52, height * 0.75), (2, shoulder, height * 0.74), "chest"),
        ("upperarm_l", (2, shoulder, height * 0.74), (12, arm_side, height * 0.56), "clavicle_l"),
        ("lowerarm_l", (12, arm_side, height * 0.56), (20, arm_side * 1.03, height * 0.38), "upperarm_l"),
        ("hand_l", (20, arm_side * 1.03, height * 0.38), (38, arm_side * 1.04, height * 0.32), "lowerarm_l"),
        ("clavicle_r", (0, -shoulder * 0.52, height * 0.75), (2, -shoulder, height * 0.74), "chest"),
        ("upperarm_r", (2, -shoulder, height * 0.74), (12, -arm_side, height * 0.56), "clavicle_r"),
        ("lowerarm_r", (12, -arm_side, height * 0.56), (20, -arm_side * 1.03, height * 0.38), "upperarm_r"),
        ("hand_r", (20, -arm_side * 1.03, height * 0.38), (38, -arm_side * 1.04, height * 0.32), "lowerarm_r"),
        ("thigh_l", (0, hip_side, height * 0.43), (12, hip_side * 1.30, height * 0.23), "pelvis"),
        ("calf_l", (12, hip_side * 1.30, height * 0.23), (23, hip_side * 1.23, height * 0.055), "thigh_l"),
        ("foot_l", (23, hip_side * 1.23, height * 0.055), (58, hip_side * 1.23, 5), "calf_l"),
        ("thigh_r", (0, -hip_side, height * 0.43), (12, -hip_side * 1.30, height * 0.23), "pelvis"),
        ("calf_r", (12, -hip_side * 1.30, height * 0.23), (23, -hip_side * 1.23, height * 0.055), "thigh_r"),
        ("foot_r", (23, -hip_side * 1.23, height * 0.055), (58, -hip_side * 1.23, 5), "calf_r"),
    ]


def add_blackpike_trooper(
    label: str,
    armature_name: str,
    offset_y: float,
    materials: dict[str, bpy.types.Material],
) -> tuple[bpy.types.Object, list[bpy.types.Object]]:
    height = HEIGHT_CM
    shoulder = height * 0.145
    arm_side = height * 0.215
    hip_side = height * 0.075

    def p(point: tuple[float, float, float]) -> tuple[float, float, float]:
        return (point[0], point[1] + offset_y, point[2])

    armature = create_armature(armature_name, [(name, p(head), p(tail), parent) for name, head, tail, parent in make_bones(height)])
    objects: list[bpy.types.Object] = []

    flesh = materials["M_ABY_CharredFlesh_Blockout_A01"]
    iron = materials["M_ABY_ScorchedIron_Blockout_A01"]
    cloth = materials["M_ABY_AshCloth_Blockout_A01"]
    bone = materials["M_ABY_BoneHorn_Blockout_A01"]
    pike = materials["M_ABY_PikeBlackIron_Blockout_A01"]
    glow = materials["M_ABY_VoidGlow_Blockout_A01"]
    ember = materials["M_ABY_EmberFissure_Blockout_A01"]

    core_parts = [
        (add_ellipsoid_obj(f"{label}_Body_Pelvis", p((0, 0, height * 0.44)), (height * 0.055, hip_side * 1.25, height * 0.040), flesh, 16, 8), "pelvis"),
        (add_ellipsoid_obj(f"{label}_Body_Torso", p((0, 0, height * 0.60)), (height * 0.060, shoulder * 0.72, height * 0.080), flesh, 16, 8), "spine_01"),
        (add_ellipsoid_obj(f"{label}_Body_Chest", p((0, 0, height * 0.70)), (height * 0.064, shoulder * 0.92, height * 0.060), flesh, 16, 8), "chest"),
        (add_cylinder_between(f"{label}_Neck_Dark", p((4, 0, height * 0.79)), p((6, 0, height * 0.85)), height * 0.018, flesh, 10), "neck"),
        (add_ellipsoid_obj(f"{label}_Head_HelmetMass", p((12, 0, height * 0.91)), (height * 0.036, height * 0.034, height * 0.048), iron, 14, 7), "head"),
        (add_box_obj(f"{label}_Helm_BrowVisor", p((27, 0, height * 0.915)), (height * 0.040, height * 0.065, height * 0.014), iron), "head"),
        (add_box_obj(f"{label}_Helm_JawGuard", p((30, 0, height * 0.885)), (height * 0.036, height * 0.052, height * 0.025), iron), "head"),
        (add_box_obj(f"{label}_Chest_BlackPlate", p((24, 0, height * 0.675)), (height * 0.036, shoulder * 1.35, height * 0.120), iron), "chest"),
        (add_box_obj(f"{label}_Back_ArmorPlate", p((-30, 0, height * 0.66)), (height * 0.024, shoulder * 1.18, height * 0.130), iron), "chest"),
        (add_box_obj(f"{label}_Belt_Obsidian", p((24, 0, height * 0.49)), (height * 0.035, shoulder * 1.20, height * 0.028), iron), "pelvis"),
        (add_box_obj(f"{label}_TatteredCloth_Front", p((34, 0, height * 0.34)), (height * 0.020, shoulder * 0.70, height * 0.210), cloth), "pelvis"),
        (add_box_obj(f"{label}_TatteredCloth_Back", p((-25, 0, height * 0.36)), (height * 0.018, shoulder * 0.72, height * 0.185), cloth), "pelvis"),
        (add_diamond_obj(f"{label}_Chest_VoidFissure", p((44, 0, height * 0.69)), (height * 0.006, height * 0.013, height * 0.040), ember), "chest"),
    ]
    for obj, bone_name in core_parts:
        add_assigned(obj, armature, bone_name, objects)

    for side, sign, suffix in (("Left", 1, "l"), ("Right", -1, "r")):
        add_assigned(add_box_obj(f"{label}_Shoulder_{side}_CrescentPlate", p((8, sign * shoulder * 1.05, height * 0.745)), (height * 0.050, height * 0.080, height * 0.035), iron), armature, "chest", objects)
        add_assigned(add_cone_between(f"{label}_Shoulder_{side}_HornSpike", p((18, sign * shoulder * 1.45, height * 0.755)), p((38, sign * shoulder * 1.82, height * 0.790)), height * 0.010, bone, 8), armature, "chest", objects)
        add_assigned(add_cylinder_between(f"{label}_Arm_{side}_Upper", p((4, sign * shoulder, height * 0.72)), p((12, sign * arm_side, height * 0.56)), height * 0.020, flesh, 10), armature, f"upperarm_{suffix}", objects)
        add_assigned(add_cylinder_between(f"{label}_Arm_{side}_Lower", p((12, sign * arm_side, height * 0.56)), p((20, sign * arm_side * 1.03, height * 0.38)), height * 0.018, flesh, 10), armature, f"lowerarm_{suffix}", objects)
        add_assigned(add_box_obj(f"{label}_Bracer_{side}_BlackIron", p((18, sign * arm_side * 0.98, height * 0.47)), (height * 0.040, height * 0.055, height * 0.040), iron), armature, f"lowerarm_{suffix}", objects)
        add_assigned(add_ellipsoid_obj(f"{label}_Hand_{side}_ClawedGauntlet", p((38, sign * arm_side * 1.04, height * 0.32)), (height * 0.030, height * 0.020, height * 0.022), iron, 10, 5), armature, f"hand_{suffix}", objects)
        add_assigned(add_cylinder_between(f"{label}_Leg_{side}_Thigh", p((0, sign * hip_side, height * 0.43)), p((12, sign * hip_side * 1.30, height * 0.23)), height * 0.026, flesh, 10), armature, f"thigh_{suffix}", objects)
        add_assigned(add_cylinder_between(f"{label}_Leg_{side}_Calf", p((12, sign * hip_side * 1.30, height * 0.23)), p((24, sign * hip_side * 1.23, height * 0.055)), height * 0.021, flesh, 10), armature, f"calf_{suffix}", objects)
        add_assigned(add_box_obj(f"{label}_Greave_{side}_BlackIron", p((24, sign * hip_side * 1.28, height * 0.17)), (height * 0.042, height * 0.050, height * 0.070), iron), armature, f"calf_{suffix}", objects)
        add_assigned(add_box_obj(f"{label}_Foot_{side}_Sabaton", p((58, sign * hip_side * 1.23, height * 0.030)), (height * 0.130, height * 0.058, height * 0.035), iron), armature, f"foot_{suffix}", objects)

    for side, sign in (("Left", 1), ("Right", -1)):
        add_assigned(add_cone_between(f"{label}_Horn_{side}_Base", p((8, sign * 15, height * 0.955)), p((-8, sign * 30, height * 1.045)), height * 0.010, bone, 10), armature, "head", objects)
        add_assigned(add_cone_between(f"{label}_Horn_{side}_Tip", p((-8, sign * 30, height * 1.045)), p((-20, sign * 40, height * 1.095)), height * 0.007, bone, 8), armature, "head", objects)

    add_assigned(add_diamond_obj(f"{label}_EyeGlow_L", p((42, 7, height * 0.915)), (2.2, 2.0, 3.2), glow), armature, "head", objects)
    add_assigned(add_diamond_obj(f"{label}_EyeGlow_R", p((42, -7, height * 0.915)), (2.2, 2.0, 3.2), glow), armature, "head", objects)

    add_assigned(add_cylinder_between(f"{label}_Pike_BlackShaft", p((38, -82, 30)), p((28, -82, 314)), 3.4, pike, 12), armature, "hand_r", objects)
    add_assigned(add_diamond_obj(f"{label}_Pike_VoidBlade", p((24, -82, 330)), (18, 7, 34), pike), armature, "hand_r", objects)
    add_assigned(add_diamond_obj(f"{label}_Pike_VioletEdge", p((31, -88, 330)), (4, 2, 28), glow), armature, "hand_r", objects)
    add_assigned(add_box_obj(f"{label}_Pike_Crossbar", p((30, -82, 292)), (50, 6, 6), pike), armature, "hand_r", objects)
    add_assigned(add_box_obj(f"{label}_LeftForearm_ShieldLineVariantPlate", p((40, arm_side * 1.08, height * 0.43)), (height * 0.018, height * 0.085, height * 0.105), iron), armature, "lowerarm_l", objects)

    for socket_name, location, bone_name in [
        ("SOCKET_socket_weapon_r", p((38, -82, 90)), "hand_r"),
        ("SOCKET_socket_weapon_l", p((34, 48, 96)), "hand_l"),
        ("SOCKET_socket_pike_tip", p((24, -82, 330)), "hand_r"),
        ("SOCKET_socket_head_vfx", p((18, 0, height * 0.98)), "head"),
        ("SOCKET_socket_eye_l", p((42, 7, height * 0.915)), "head"),
        ("SOCKET_socket_eye_r", p((42, -7, height * 0.915)), "head"),
        ("SOCKET_socket_chest_core", p((46, 0, height * 0.69)), "chest"),
        ("SOCKET_socket_banner_back", p((-38, 0, height * 0.74)), "chest"),
        ("SOCKET_socket_ground_rift", p((42, 0, 3)), "root"),
        ("SOCKET_socket_hit_trace_pike", p((28, -82, 258)), "hand_r"),
    ]:
        add_socket_empty(socket_name, location, armature, bone_name)

    return armature, objects


def export_asset() -> None:
    clear_scene()
    setup_scene()
    materials = create_materials(ABYSS_MATERIALS)
    armature, objects = add_blackpike_trooper(ASSET_NAME, f"SKEL_{ASSET_NAME}", 0.0, materials)
    add_asset_metadata(
        ASSET_NAME,
        "First-pass DCC review Abyss BlackPike Trooper with pike silhouette, horned helm, armor mass, sockets, and scale lock; final sculpt, retopo, skinning, physics, LODs, animation, and textures pending",
        "/Game/Aerathea/Creatures/Abyss/Troops/BlackPikeTrooper/SK_ABY_BlackPikeTrooper_A01",
    )
    export_path = EXPORT_ROOT / EXPORT_REL / f"{ASSET_NAME}.fbx"
    export_skeletal_fbx(export_path, objects, armature, bake_anim=False)
    print(f"Exported {export_path.relative_to(ROOT)}")


def add_scale_marker(name: str, height: float, y: float, material: bpy.types.Material) -> None:
    add_ellipsoid_obj(f"{name}_Head", (0, y, height - 10), (8, 8, 10), material, 10, 5)
    add_cylinder_between(f"{name}_Body", (0, y, height - 24), (0, y, height * 0.42), max(3.5, height * 0.035), material, 10)
    add_cylinder_between(f"{name}_LegL", (0, y + height * 0.025, height * 0.42), (4, y + height * 0.035, 3), max(2.0, height * 0.018), material, 8)
    add_cylinder_between(f"{name}_LegR", (0, y - height * 0.025, height * 0.42), (4, y - height * 0.035, 3), max(2.0, height * 0.018), material, 8)


def render_review() -> None:
    clear_scene()
    setup_scene()
    bpy.context.scene.view_settings.view_transform = "Standard"
    bpy.context.scene.view_settings.exposure = 0.0
    bpy.context.scene.view_settings.gamma = 1.0
    if bpy.context.scene.world is not None:
        bpy.context.scene.world.color = (0.54, 0.50, 0.47)

    materials = create_materials(ABYSS_MATERIALS)
    make_review_materials_readable(materials)
    add_blackpike_trooper(ASSET_NAME, f"SKEL_{ASSET_NAME}", 0.0, materials)
    add_scale_marker("Scale_180cm_Human", 180.0, -150.0, materials["M_AET_ScaleMarker_Blockout_A01"])
    add_scale_marker("Scale_230cm_TrooperLimit", 230.0, 150.0, materials["M_AET_ScaleMarker_Blockout_A01"])
    add_asset_metadata(
        ASSET_NAME,
        "Approved BlackPike first-pass DCC review scene with 220 cm trooper, 180 cm humanoid marker, and 230 cm upper-range marker",
        "/Game/Aerathea/Creatures/Abyss/Troops/BlackPikeTrooper/SK_ABY_BlackPikeTrooper_A01",
    )

    bpy.ops.object.light_add(type="AREA", location=(540, -320, 460))
    key = bpy.context.object
    key.name = "AET_BlackPikeReview_KeyLight"
    key.data.energy = 3200
    key.data.size = 520
    bpy.ops.object.light_add(type="AREA", location=(360, 340, 300))
    fill = bpy.context.object
    fill.name = "AET_BlackPikeReview_FillLight"
    fill.data.energy = 900
    fill.data.size = 680

    bpy.ops.object.camera_add(location=(600, -420, 225))
    camera = bpy.context.object
    target = Vector((14, 0, 150))
    direction = target - Vector(camera.location)
    camera.rotation_euler = direction.to_track_quat("-Z", "Y").to_euler()
    camera.data.type = "ORTHO"
    camera.data.ortho_scale = 430
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
