#!/usr/bin/env python3
"""Build the first-pass Aerathea Iona Siegebreaker Mek review source.

Run with:
    blender --background --python Tools/DCC/build_iona_siegebreaker_mek.py

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
REVIEW_ROOT = ROOT / "Saved" / "Automation" / "IonaSiegebreakerMekReview"

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


ASSET_NAME = "SK_GNM_IonaSiegebreakerMek_A01"
HEIGHT_CM = 420.0
SOURCE_REL = "Characters/Gnomes/Iona/SK_GNM_IonaSiegebreakerMek_A01"
EXPORT_REL = "Characters/Gnomes/Iona/SK_GNM_IonaSiegebreakerMek_A01"

IONA_MATERIALS = {
    "M_GNM_IonaMek_DarkIron_Blockout_A01": (0.065, 0.070, 0.075),
    "M_GNM_IonaMek_BrassCopper_Blockout_A01": (0.70, 0.43, 0.18),
    "M_GNM_IonaMek_LeatherCable_Blockout_A01": (0.16, 0.09, 0.055),
    "M_GNM_IonaMek_AetheriumGlow_Blockout_A01": (0.00, 0.55, 1.00),
    "M_GNM_IonaMek_CockpitGlass_Blockout_A01": (0.07, 0.18, 0.27),
    "M_GNM_IonaPilotSkin_Blockout_A01": (0.78, 0.55, 0.38),
    "M_GNM_IonaPilotHair_Blockout_A01": (0.72, 0.22, 0.36),
    "M_GNM_IonaPilotWorkwear_Blockout_A01": (0.18, 0.23, 0.28),
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
        bsdf.inputs["Roughness"].default_value = 0.84
        if "Emission Color" in bsdf.inputs:
            bsdf.inputs["Emission Color"].default_value = (color[0] * 0.12, color[1] * 0.12, color[2] * 0.12, 1.0)
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


def add_torus_obj(
    name: str,
    center: tuple[float, float, float],
    major_radius: float,
    minor_radius: float,
    material: bpy.types.Material,
    rotate_y_degrees: float = 90.0,
) -> bpy.types.Object:
    bpy.ops.mesh.primitive_torus_add(
        major_segments=32,
        minor_segments=8,
        major_radius=major_radius,
        minor_radius=minor_radius,
        location=center,
    )
    obj = bpy.context.object
    obj.name = name
    obj.data.name = f"{name}_Mesh"
    obj.rotation_euler[1] = math.radians(rotate_y_degrees)
    obj.data.materials.append(material)
    return obj


def add_vertical_bar(name: str, center: tuple[float, float, float], height: float, radius: float, material: bpy.types.Material) -> bpy.types.Object:
    x, y, z = center
    return add_cylinder_between(name, (x, y, z - height * 0.5), (x, y, z + height * 0.5), radius, material, 12)


def mek_bones() -> list[tuple[str, tuple[float, float, float], tuple[float, float, float], str | None]]:
    return [
        ("root", (0, 0, 0), (0, 0, 26), None),
        ("body_root", (0, 0, 112), (0, 0, 166), "root"),
        ("torso", (0, 0, 166), (0, 0, 286), "body_root"),
        ("cockpit", (34, 0, 270), (76, 0, 354), "torso"),
        ("core_chest", (48, 0, 226), (86, 0, 274), "torso"),
        ("core_back", (-58, 0, 240), (-84, 0, 354), "torso"),
        ("upperarm_l", (2, 102, 276), (44, 154, 218), "torso"),
        ("forearm_l", (44, 154, 218), (84, 174, 158), "upperarm_l"),
        ("fist_l", (84, 174, 158), (126, 184, 126), "forearm_l"),
        ("upperarm_r", (2, -102, 276), (44, -154, 218), "torso"),
        ("forearm_r", (44, -154, 218), (84, -174, 158), "upperarm_r"),
        ("fist_r", (84, -174, 158), (126, -184, 126), "forearm_r"),
        ("thigh_l", (0, 54, 120), (18, 70, 70), "body_root"),
        ("shin_l", (18, 70, 70), (32, 70, 24), "thigh_l"),
        ("foot_l", (32, 70, 24), (98, 70, 6), "shin_l"),
        ("thigh_r", (0, -54, 120), (18, -70, 70), "body_root"),
        ("shin_r", (18, -70, 70), (32, -70, 24), "thigh_r"),
        ("foot_r", (32, -70, 24), (98, -70, 6), "shin_r"),
        ("cannon_mount_l", (-34, 104, 340), (110, 124, 382), "torso"),
        ("cannon_mount_r", (-34, -104, 340), (110, -124, 382), "torso"),
        ("vent_l", (-78, 48, 282), (-78, 48, 412), "core_back"),
        ("vent_r", (-78, -48, 282), (-78, -48, 412), "core_back"),
    ]


def add_iona_mek(materials: dict[str, bpy.types.Material]) -> tuple[bpy.types.Object, list[bpy.types.Object]]:
    dark_iron = materials["M_GNM_IonaMek_DarkIron_Blockout_A01"]
    brass = materials["M_GNM_IonaMek_BrassCopper_Blockout_A01"]
    leather = materials["M_GNM_IonaMek_LeatherCable_Blockout_A01"]
    glow = materials["M_GNM_IonaMek_AetheriumGlow_Blockout_A01"]
    glass = materials["M_GNM_IonaMek_CockpitGlass_Blockout_A01"]
    skin = materials["M_GNM_IonaPilotSkin_Blockout_A01"]
    hair = materials["M_GNM_IonaPilotHair_Blockout_A01"]
    workwear = materials["M_GNM_IonaPilotWorkwear_Blockout_A01"]

    armature = create_armature(f"SKEL_{ASSET_NAME}", mek_bones())
    objects: list[bpy.types.Object] = []

    # Main hero Mek frame.
    add_assigned(add_ellipsoid_obj("IonaMek_BodyRoot_Gearbox", (0, 0, 124), (58, 76, 42), dark_iron, 20, 10), armature, "body_root", objects)
    add_assigned(add_ellipsoid_obj("IonaMek_Torso_CageMass", (8, 0, 228), (84, 96, 92), dark_iron, 22, 10), armature, "torso", objects)
    add_assigned(add_box_obj("IonaMek_Chest_HeroPlate", (72, 0, 226), (28, 74, 104), dark_iron), armature, "torso", objects)
    add_assigned(add_ellipsoid_obj("IonaMek_Chest_AetheriumCore", (92, 0, 236), (20, 28, 30), glow, 18, 8), armature, "core_chest", objects)
    add_assigned(add_torus_obj("IonaMek_Chest_BrassCoreRing", (94, 0, 236), 35, 4.2, brass), armature, "core_chest", objects)
    add_assigned(add_box_obj("IonaMek_Back_ReactorHousing", (-62, 0, 278), (42, 88, 96), dark_iron), armature, "core_back", objects)
    add_assigned(add_ellipsoid_obj("IonaMek_Back_ReactorGlow", (-92, 0, 304), (16, 22, 34), glow, 14, 6), armature, "core_back", objects)

    # Cockpit and pilot-envelope proxy.
    add_assigned(add_torus_obj("IonaMek_Cockpit_BrassGuardRing", (76, 0, 316), 48, 5.5, brass), armature, "cockpit", objects)
    add_assigned(add_box_obj("IonaMek_Cockpit_Backplate", (36, 0, 310), (30, 84, 64), dark_iron), armature, "cockpit", objects)
    add_assigned(add_box_obj("IonaMek_Cockpit_SmokeGlassLower", (80, 0, 288), (8, 66, 26), glass), armature, "cockpit", objects)
    add_assigned(add_box_obj("IonaMek_Harness_ChestYoke", (84, 0, 278), (12, 44, 22), leather), armature, "cockpit", objects)
    add_assigned(add_ellipsoid_obj("IonaPilot_TorsoProxy", (90, 0, 286), (11, 14, 20), workwear, 12, 6), armature, "cockpit", objects)
    add_assigned(add_ellipsoid_obj("IonaPilot_HeadProxy", (104, 0, 322), (10, 11, 13), skin, 14, 7), armature, "cockpit", objects)
    add_assigned(add_ellipsoid_obj("IonaPilot_PinkHairMass", (100, 0, 343), (12, 14, 16), hair, 14, 6), armature, "cockpit", objects)
    add_assigned(add_ellipsoid_obj("IonaPilot_EarLeft", (101, 14, 322), (3, 7, 5), skin, 8, 4), armature, "cockpit", objects)
    add_assigned(add_ellipsoid_obj("IonaPilot_EarRight", (101, -14, 322), (3, 7, 5), skin, 8, 4), armature, "cockpit", objects)
    add_assigned(add_torus_obj("IonaPilot_GoggleLeft", (114, 5, 326), 4.6, 0.8, brass), armature, "cockpit", objects)
    add_assigned(add_torus_obj("IonaPilot_GoggleRight", (114, -5, 326), 4.6, 0.8, brass), armature, "cockpit", objects)

    for side, sign, suffix in (("Left", 1, "l"), ("Right", -1, "r")):
        add_assigned(add_ellipsoid_obj(f"IonaMek_Shoulder_{side}_RoundArmor", (4, sign * 118, 286), (54, 54, 46), dark_iron, 18, 8), armature, "torso", objects)
        add_assigned(add_box_obj(f"IonaMek_Shoulder_{side}_BrassCap", (24, sign * 128, 292), (48, 36, 30), brass), armature, "torso", objects)
        add_assigned(add_cylinder_between(f"IonaMek_UpperArm_{side}_HeavyPiston", (14, sign * 118, 260), (46, sign * 154, 218), 13, dark_iron, 12), armature, f"upperarm_{suffix}", objects)
        add_assigned(add_cylinder_between(f"IonaMek_UpperArm_{side}_CopperHydraulic", (34, sign * 122, 256), (60, sign * 162, 194), 4.5, brass, 10), armature, f"upperarm_{suffix}", objects)
        add_assigned(add_ellipsoid_obj(f"IonaMek_Forearm_{side}_SiegeGauntlet", (80, sign * 174, 170), (42, 38, 52), dark_iron, 16, 8), armature, f"forearm_{suffix}", objects)
        add_assigned(add_box_obj(f"IonaMek_Fist_{side}_OversizedKnuckles", (124, sign * 184, 132), (62, 54, 42), dark_iron), armature, f"fist_{suffix}", objects)
        add_assigned(add_box_obj(f"IonaMek_Fist_{side}_BrassFingerBar", (154, sign * 184, 138), (18, 50, 12), brass), armature, f"fist_{suffix}", objects)
        add_assigned(add_ellipsoid_obj(f"IonaMek_Thigh_{side}_Armor", (16, sign * 58, 92), (34, 30, 50), dark_iron, 14, 7), armature, f"thigh_{suffix}", objects)
        add_assigned(add_box_obj(f"IonaMek_Knee_{side}_BrassGuard", (42, sign * 70, 70), (30, 34, 24), brass), armature, f"shin_{suffix}", objects)
        add_assigned(add_cylinder_between(f"IonaMek_Shin_{side}_DarkPiston", (28, sign * 70, 68), (38, sign * 70, 24), 15, dark_iron, 12), armature, f"shin_{suffix}", objects)
        add_assigned(add_box_obj(f"IonaMek_Foot_{side}_SiegeBoot", (68, sign * 70, 13), (92, 52, 26), dark_iron), armature, f"foot_{suffix}", objects)
        add_assigned(add_box_obj(f"IonaMek_Toe_{side}_BrassToePlate", (116, sign * 70, 10), (32, 46, 16), brass), armature, f"foot_{suffix}", objects)

    # Twin over-shoulder arc cannon mounts.
    for side, sign, suffix in (("Left", 1, "l"), ("Right", -1, "r")):
        add_assigned(add_cylinder_between(f"IonaMek_Cannon_{side}_ArcBarrel", (-24, sign * 108, 344), (122, sign * 126, 376), 19, dark_iron, 18), armature, f"cannon_mount_{suffix}", objects)
        add_assigned(add_cylinder_between(f"IonaMek_Cannon_{side}_AetheriumBore", (58, sign * 118, 362), (138, sign * 128, 382), 9, glow, 16), armature, f"cannon_mount_{suffix}", objects)
        add_assigned(add_ellipsoid_obj(f"IonaMek_Cannon_{side}_MuzzleGlow", (146, sign * 130, 384), (13, 13, 13), glow, 12, 6), armature, f"cannon_mount_{suffix}", objects)
        add_assigned(add_torus_obj(f"IonaMek_Cannon_{side}_MountCollar", (-22, sign * 104, 342), 23, 3.5, brass), armature, f"cannon_mount_{suffix}", objects)

    for side, sign, suffix in (("Left", 1, "l"), ("Right", -1, "r")):
        add_assigned(add_vertical_bar(f"IonaMek_BackVent_{side}_Stack", (-82, sign * 48, 350), 120, 10, brass), armature, f"vent_{suffix}", objects)
        add_assigned(add_ellipsoid_obj(f"IonaMek_BackVent_{side}_GlowCap", (-82, sign * 48, 416), (8, 8, 9), glow, 10, 5), armature, f"vent_{suffix}", objects)

    # Large readable cables, kept as geometry only where silhouette needs them.
    add_assigned(add_cylinder_between("IonaMek_Cable_LeftReactorToCannon", (-70, 34, 320), (18, 104, 350), 4.5, leather, 10), armature, "core_back", objects)
    add_assigned(add_cylinder_between("IonaMek_Cable_RightReactorToCannon", (-70, -34, 320), (18, -104, 350), 4.5, leather, 10), armature, "core_back", objects)
    add_assigned(add_cylinder_between("IonaMek_Cable_HarnessLeft", (60, 24, 292), (92, 18, 278), 2.8, leather, 8), armature, "cockpit", objects)
    add_assigned(add_cylinder_between("IonaMek_Cable_HarnessRight", (60, -24, 292), (92, -18, 278), 2.8, leather, 8), armature, "cockpit", objects)

    for socket_name, location, bone_name in [
        ("SOCKET_socket_pilot_harness", (84, 0, 284), "cockpit"),
        ("SOCKET_socket_cannon_l_mount", (-24, 108, 344), "cannon_mount_l"),
        ("SOCKET_socket_cannon_r_mount", (-24, -108, 344), "cannon_mount_r"),
        ("SOCKET_socket_cannon_l_muzzle", (146, 130, 384), "cannon_mount_l"),
        ("SOCKET_socket_cannon_r_muzzle", (146, -130, 384), "cannon_mount_r"),
        ("SOCKET_socket_core_chest", (94, 0, 236), "core_chest"),
        ("SOCKET_socket_core_back", (-92, 0, 304), "core_back"),
        ("SOCKET_socket_hand_l", (150, 184, 136), "fist_l"),
        ("SOCKET_socket_hand_r", (150, -184, 136), "fist_r"),
        ("SOCKET_socket_foot_l", (112, 70, 4), "foot_l"),
        ("SOCKET_socket_foot_r", (112, -70, 4), "foot_r"),
        ("SOCKET_socket_vent_l", (-82, 48, 414), "vent_l"),
        ("SOCKET_socket_vent_r", (-82, -48, 414), "vent_r"),
        ("SOCKET_socket_camera_focus", (108, 0, 330), "cockpit"),
        ("SOCKET_vfx_arc_l", (146, 130, 384), "cannon_mount_l"),
        ("SOCKET_vfx_arc_r", (146, -130, 384), "cannon_mount_r"),
    ]:
        add_socket_empty(socket_name, location, armature, bone_name)

    return armature, objects


def export_asset() -> None:
    clear_scene()
    setup_scene()
    materials = create_materials(IONA_MATERIALS)
    armature, objects = add_iona_mek(materials)
    add_asset_metadata(
        ASSET_NAME,
        "Approved first-pass Iona Siegebreaker Mek review source with 420 cm hero Mek scale, visible pilot envelope, twin arc-cannon mounts, fists, boots, and socket contract; final sculpt, retopo, skinning, physics, LODs, animation, and textures pending",
        "/Game/Aerathea/Characters/Gnomes/Iona/Mek/SK_GNM_IonaSiegebreakerMek_A01",
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
        bpy.context.scene.world.color = (0.58, 0.57, 0.54)

    materials = create_materials(IONA_MATERIALS)
    make_review_materials_readable(materials)
    add_iona_mek(materials)
    add_scale_marker("Scale_110cm_Gnome", 110.0, -250.0, materials["M_AET_ScaleMarker_Blockout_A01"])
    add_scale_marker("Scale_180cm_Human", 180.0, -185.0, materials["M_AET_ScaleMarker_Blockout_A01"])
    add_scale_marker("Scale_420cm_MekTarget", HEIGHT_CM, 245.0, materials["M_AET_ScaleMarker_Blockout_A01"])
    add_asset_metadata(
        ASSET_NAME,
        "Approved Iona Siegebreaker Mek first-pass DCC review scene with gnome/human/420 cm scale markers",
        "/Game/Aerathea/Characters/Gnomes/Iona/Mek/SK_GNM_IonaSiegebreakerMek_A01",
    )

    bpy.ops.object.light_add(type="SUN", location=(0, 0, 700), rotation=(math.radians(48), 0, math.radians(35)))
    bpy.context.object.data.energy = 1.15
    bpy.ops.object.light_add(type="AREA", location=(820, -380, 580))
    key = bpy.context.object
    key.name = "AET_IonaSiegebreakerMekReview_KeyLight"
    key.data.energy = 15000
    key.data.size = 820
    bpy.ops.object.light_add(type="AREA", location=(-250, 450, 420))
    fill = bpy.context.object
    fill.name = "AET_IonaSiegebreakerMekReview_FillLight"
    fill.data.energy = 2200
    fill.data.size = 680

    bpy.ops.object.camera_add(location=(820, -710, 335))
    camera = bpy.context.object
    target = Vector((32, 0, 214))
    direction = target - Vector(camera.location)
    camera.rotation_euler = direction.to_track_quat("-Z", "Y").to_euler()
    camera.data.type = "ORTHO"
    camera.data.ortho_scale = 545
    camera.data.clip_start = 1
    camera.data.clip_end = 6000
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
