#!/usr/bin/env python3
"""Build first-pass Gnome Heavy Mek rivalry review assets."""

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
REVIEW_ROOT = ROOT / "Saved" / "Automation" / "GnomeHeavyMekReview"

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


MEK_MATERIALS = {
    "M_GNM_Mek_DarkIron_Blockout_A01": (0.08, 0.09, 0.10),
    "M_GNM_Mek_Brass_Blockout_A01": (0.78, 0.55, 0.25),
    "M_GNM_Mek_Copper_Blockout_A01": (0.52, 0.25, 0.10),
    "M_GNM_Mek_BluePanel_Blockout_A01": (0.05, 0.16, 0.34),
    "M_GNM_Mek_AetheriumGlow_Blockout_A01": (0.0, 0.55, 1.0),
    "M_GNM_MekPilotSkin_Blockout_A01": (0.78, 0.55, 0.38),
    "M_GNM_MekPilotWorkwear_Blockout_A01": (0.18, 0.24, 0.29),
    "M_GNM_MekPilotHair_Blockout_A01": (0.38, 0.12, 0.62),
    "M_GNM_Mek_Leather_Blockout_A01": (0.18, 0.10, 0.06),
}


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


def add_assigned(obj: bpy.types.Object, armature: bpy.types.Object, bone: str, objects: list[bpy.types.Object]) -> None:
    assign_to_bone(obj, armature, bone)
    objects.append(obj)


def mek_bones() -> list[tuple[str, tuple[float, float, float], tuple[float, float, float], str | None]]:
    return [
        ("root", (0, 0, 0), (0, 0, 24), None),
        ("pelvis", (0, 0, 104), (0, 0, 142), "root"),
        ("torso", (0, 0, 142), (0, 0, 246), "pelvis"),
        ("cockpit", (28, 0, 238), (48, 0, 322), "torso"),
        ("reactor", (-48, 0, 230), (-48, 0, 350), "torso"),
        ("upperarm_l", (0, 88, 238), (24, 132, 178), "torso"),
        ("lowerarm_l", (24, 132, 178), (54, 146, 108), "upperarm_l"),
        ("hand_l", (54, 146, 108), (76, 146, 72), "lowerarm_l"),
        ("cannon_l", (62, 146, 128), (132, 146, 112), "lowerarm_l"),
        ("upperarm_r", (0, -88, 238), (24, -132, 178), "torso"),
        ("lowerarm_r", (24, -132, 178), (54, -146, 108), "upperarm_r"),
        ("hand_r", (54, -146, 108), (76, -146, 72), "lowerarm_r"),
        ("hammer_r", (76, -146, 72), (150, -152, 38), "hand_r"),
        ("thigh_l", (0, 44, 110), (18, 58, 62), "pelvis"),
        ("calf_l", (18, 58, 62), (28, 58, 22), "thigh_l"),
        ("foot_l", (28, 58, 22), (82, 58, 6), "calf_l"),
        ("thigh_r", (0, -44, 110), (18, -58, 62), "pelvis"),
        ("calf_r", (18, -58, 62), (28, -58, 22), "thigh_r"),
        ("foot_r", (28, -58, 22), (82, -58, 6), "calf_r"),
    ]


def add_gnome_heavy_mek() -> tuple[bpy.types.Object, list[bpy.types.Object]]:
    materials = create_materials(MEK_MATERIALS)
    dark_iron = materials["M_GNM_Mek_DarkIron_Blockout_A01"]
    brass = materials["M_GNM_Mek_Brass_Blockout_A01"]
    copper = materials["M_GNM_Mek_Copper_Blockout_A01"]
    blue = materials["M_GNM_Mek_BluePanel_Blockout_A01"]
    glow = materials["M_GNM_Mek_AetheriumGlow_Blockout_A01"]
    skin = materials["M_GNM_MekPilotSkin_Blockout_A01"]
    workwear = materials["M_GNM_MekPilotWorkwear_Blockout_A01"]
    hair = materials["M_GNM_MekPilotHair_Blockout_A01"]
    leather = materials["M_GNM_Mek_Leather_Blockout_A01"]

    armature = create_armature("SKEL_GNM_HeavyMek_Rivalry_A01", mek_bones())
    objects: list[bpy.types.Object] = []

    # Main frame.
    add_assigned(add_ellipsoid_obj("Mek_PelvisGearbox", (0, 0, 116), (46, 58, 34), dark_iron, 18, 8), armature, "pelvis", objects)
    add_assigned(add_ellipsoid_obj("Mek_TorsoArmorMass", (4, 0, 202), (66, 78, 72), dark_iron, 20, 10), armature, "torso", objects)
    add_assigned(add_box_obj("Mek_ChestBlueHeraldryPlate", (64, 0, 194), (20, 52, 78), blue), armature, "torso", objects)
    add_assigned(add_ellipsoid_obj("Mek_ChestAetheriumCore", (76, 0, 205), (18, 24, 24), glow, 16, 8), armature, "torso", objects)
    add_assigned(add_torus_obj("Mek_ChestBrassCoreRing", (78, 0, 205), 29, 3.6, brass), armature, "torso", objects)
    add_assigned(add_torus_obj("Mek_CockpitBrassRing", (60, 0, 282), 40, 5.0, brass), armature, "cockpit", objects)
    add_assigned(add_box_obj("Mek_CockpitDarkBackplate", (24, 0, 280), (28, 76, 54), dark_iron), armature, "cockpit", objects)

    # Visible gnome pilot.
    add_assigned(add_ellipsoid_obj("Pilot_TorsoHarness", (70, 0, 260), (11, 14, 18), workwear, 12, 6), armature, "cockpit", objects)
    add_assigned(add_ellipsoid_obj("Pilot_Head", (82, 0, 291), (10, 11, 13), skin, 14, 7), armature, "cockpit", objects)
    add_assigned(add_ellipsoid_obj("Pilot_HairMass", (78, 0, 308), (11, 13, 9), hair, 12, 6), armature, "cockpit", objects)
    add_assigned(add_ellipsoid_obj("Pilot_EarLeft", (80, 13, 292), (3, 7, 5), skin, 8, 4), armature, "cockpit", objects)
    add_assigned(add_ellipsoid_obj("Pilot_EarRight", (80, -13, 292), (3, 7, 5), skin, 8, 4), armature, "cockpit", objects)
    add_assigned(add_torus_obj("Pilot_GoggleLeft", (92, 5, 294), 4.2, 0.7, brass), armature, "cockpit", objects)
    add_assigned(add_torus_obj("Pilot_GoggleRight", (92, -5, 294), 4.2, 0.7, brass), armature, "cockpit", objects)
    add_assigned(add_box_obj("Pilot_ControlGripLeft", (82, 18, 254), (10, 4, 18), leather), armature, "cockpit", objects)
    add_assigned(add_box_obj("Pilot_ControlGripRight", (82, -18, 254), (10, 4, 18), leather), armature, "cockpit", objects)

    # Shoulders, arms, cannon, and hammer/tool arm.
    for side, sign in (("Left", 1), ("Right", -1)):
        suffix = "l" if sign > 0 else "r"
        add_assigned(add_ellipsoid_obj(f"Mek_Shoulder_{side}_DarkIronShell", (0, sign * 100, 244), (48, 48, 42), dark_iron, 18, 8), armature, "torso", objects)
        add_assigned(add_box_obj(f"Mek_Shoulder_{side}_BlueCap", (18, sign * 110, 252), (44, 34, 30), blue), armature, "torso", objects)
        add_assigned(add_torus_obj(f"Mek_Shoulder_{side}_BrassBearing", (22, sign * 84, 232), 24, 3.2, brass), armature, f"upperarm_{suffix}", objects)
        add_assigned(add_cylinder_between(f"Mek_UpperArm_{side}_Piston", (12, sign * 105, 220), (24, sign * 132, 178), 11, dark_iron, 12), armature, f"upperarm_{suffix}", objects)
        add_assigned(add_cylinder_between(f"Mek_UpperArm_{side}_CopperHydraulic", (32, sign * 112, 208), (42, sign * 136, 160), 4.2, copper, 10), armature, f"upperarm_{suffix}", objects)
        add_assigned(add_ellipsoid_obj(f"Mek_Forearm_{side}_ArmorMass", (48, sign * 142, 132), (30, 30, 46), dark_iron, 14, 7), armature, f"lowerarm_{suffix}", objects)
        add_assigned(add_box_obj(f"Mek_Hand_{side}_Clamp", (74, sign * 146, 78), (26, 28, 22), dark_iron), armature, f"hand_{suffix}", objects)

    add_assigned(add_cylinder_between("Mek_LeftAetherCannon_Barrel", (54, 146, 138), (128, 146, 114), 18, dark_iron, 16), armature, "cannon_l", objects)
    add_assigned(add_cylinder_between("Mek_LeftAetherCannon_GlowBore", (92, 146, 128), (134, 146, 112), 9, glow, 16), armature, "cannon_l", objects)
    add_assigned(add_ellipsoid_obj("Mek_LeftAetherCannon_MuzzleGlow", (140, 146, 110), (11, 11, 11), glow, 12, 6), armature, "cannon_l", objects)
    add_assigned(add_box_obj("Mek_LeftShieldEmitter_Vane", (50, 165, 154), (36, 9, 58), blue), armature, "lowerarm_l", objects)

    add_assigned(add_cylinder_between("Mek_RightHammer_Handle", (74, -146, 76), (142, -152, 38), 7.5, brass, 12), armature, "hammer_r", objects)
    add_assigned(add_box_obj("Mek_RightHammer_Head", (154, -154, 34), (52, 34, 32), dark_iron), armature, "hammer_r", objects)
    add_assigned(add_ellipsoid_obj("Mek_RightHammer_AetheriumCore", (158, -154, 34), (10, 10, 10), glow, 10, 5), armature, "hammer_r", objects)

    # Legs and feet.
    for side, sign in (("Left", 1), ("Right", -1)):
        suffix = "l" if sign > 0 else "r"
        add_assigned(add_ellipsoid_obj(f"Mek_Thigh_{side}_Armor", (14, sign * 48, 86), (26, 24, 42), dark_iron, 14, 7), armature, f"thigh_{suffix}", objects)
        add_assigned(add_box_obj(f"Mek_Knee_{side}_BluePlate", (38, sign * 56, 66), (24, 26, 20), blue), armature, f"calf_{suffix}", objects)
        add_assigned(add_cylinder_between(f"Mek_Calf_{side}_Piston", (24, sign * 58, 64), (32, sign * 58, 22), 13, dark_iron, 12), armature, f"calf_{suffix}", objects)
        add_assigned(add_box_obj(f"Mek_Foot_{side}_OversizedBoot", (58, sign * 58, 11), (78, 42, 22), dark_iron), armature, f"foot_{suffix}", objects)
        add_assigned(add_box_obj(f"Mek_Toe_{side}_FrontPlate", (96, sign * 58, 8), (28, 38, 14), brass), armature, f"foot_{suffix}", objects)

    # Back reactor and exhaust silhouette.
    add_assigned(add_box_obj("Mek_BackReactor_Block", (-54, 0, 254), (34, 66, 72), dark_iron), armature, "reactor", objects)
    add_assigned(add_ellipsoid_obj("Mek_BackReactor_AetheriumCore", (-76, 0, 298), (13, 18, 26), glow, 12, 6), armature, "reactor", objects)
    for index, y in enumerate((-36, 0, 36), 1):
        add_assigned(add_cylinder_between(f"Mek_BackStack_{index}", (-62, y, 292), (-62, y, 374), 9.5, brass, 12), armature, "reactor", objects)
        add_assigned(add_ellipsoid_obj(f"Mek_BackStack_{index}_BlueVent", (-62, y, 378), (7, 7, 8), glow, 10, 5), armature, "reactor", objects)

    # Socket empties mirror the Unreal mesh sockets authored by the import script.
    for socket_name, location, bone_name in [
        ("SOCKET_vfx_reactor_core", (-76, 0, 298), "reactor"),
        ("SOCKET_vfx_shield_l", (52, 168, 154), "lowerarm_l"),
        ("SOCKET_vfx_shield_r", (26, -112, 232), "upperarm_r"),
        ("SOCKET_weapon_cannon_muzzle", (142, 146, 110), "cannon_l"),
        ("SOCKET_pilot_hatch", (62, 0, 298), "cockpit"),
        ("SOCKET_foot_l", (82, 58, 8), "foot_l"),
        ("SOCKET_foot_r", (82, -58, 8), "foot_r"),
        ("SOCKET_vfx_stomp_l", (88, 58, 4), "foot_l"),
        ("SOCKET_vfx_stomp_r", (88, -58, 4), "foot_r"),
        ("SOCKET_weapon_hammer_socket", (154, -154, 34), "hammer_r"),
        ("SOCKET_vfx_chest_core", (78, 0, 205), "torso"),
    ]:
        add_socket_empty(socket_name, location, armature, bone_name)

    return armature, objects


def build_heavy_mek() -> None:
    clear_scene()
    setup_scene()
    armature, objects = add_gnome_heavy_mek()
    add_asset_metadata(
        "SK_GNM_HeavyMek_Rivalry_A01",
        "First-pass Gnome heavy Mek rivalry review mesh; final sculpt, rig, UVs, textures, tuned physics, and animation pending.",
        "/Game/Aerathea/Characters/Gnomes/Meks/SK_GNM_HeavyMek_Rivalry_A01",
    )
    export_path = EXPORT_ROOT / "Characters/Gnomes/Meks/SK_GNM_HeavyMek_Rivalry_A01/SK_GNM_HeavyMek_Rivalry_A01.fbx"
    export_skeletal_fbx(export_path, objects, armature, bake_anim=False)

    blend_path = BLENDER_ROOT / "Characters/Gnomes/Meks/SK_GNM_HeavyMek_Rivalry_A01/SK_GNM_HeavyMek_Rivalry_A01.blend"
    blend_path.parent.mkdir(parents=True, exist_ok=True)
    bpy.ops.wm.save_as_mainfile(filepath=str(blend_path))
    print(f"Built {blend_path.relative_to(ROOT)}")
    print(f"Exported {export_path.relative_to(ROOT)}")


def render_review() -> None:
    clear_scene()
    setup_scene()
    bpy.context.scene.view_settings.view_transform = "Standard"
    if bpy.context.scene.world is not None:
        bpy.context.scene.world.color = (0.55, 0.55, 0.53)

    add_gnome_heavy_mek()

    bpy.ops.object.light_add(type="SUN", location=(0, 0, 680), rotation=(math.radians(48), 0, math.radians(35)))
    bpy.context.object.data.energy = 1.35
    bpy.ops.object.light_add(type="AREA", location=(800, -300, 540))
    key = bpy.context.object
    key.name = "AET_GnomeHeavyMekReview_KeyLight"
    key.data.energy = 14000
    key.data.size = 760

    bpy.ops.object.camera_add(location=(720, -640, 290))
    camera = bpy.context.object
    target = Vector((28, 0, 190))
    direction = target - Vector(camera.location)
    camera.rotation_euler = direction.to_track_quat("-Z", "Y").to_euler()
    camera.data.type = "ORTHO"
    camera.data.ortho_scale = 430
    camera.data.clip_start = 1
    camera.data.clip_end = 5000
    bpy.context.scene.camera = camera
    bpy.context.scene.render.resolution_x = 1400
    bpy.context.scene.render.resolution_y = 1400

    REVIEW_ROOT.mkdir(parents=True, exist_ok=True)
    output = REVIEW_ROOT / "SK_GNM_HeavyMek_Rivalry_A01_DCCReview.png"
    bpy.context.scene.render.filepath = str(output)
    bpy.ops.render.render(write_still=True)
    print(f"Rendered {output.relative_to(ROOT)}")


def main() -> None:
    build_heavy_mek()
    render_review()


if __name__ == "__main__":
    main()
