#!/usr/bin/env python3
"""Build first-pass DCC review sources for the remaining Gnome/Ogre encounter assets.

These are deterministic review meshes for scale, silhouette, sockets, import
paths, and encounter readability. They are not final sculpted/painted assets.
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
REVIEW_ROOT = ROOT / "Saved" / "Automation" / "GnomeOgreRemainingReview"

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
    polish_mesh_object,
    setup_scene,
)
from Tools.DCC.build_ogre_base import (  # noqa: E402
    OGRE_MATERIALS,
    add_ogre_variant,
    p,
)


PREFERRED_VIEW_TRANSFORM = "Standard"
OGRE_BASE_MALE_ARMATURE_NAME = "SKEL_SK_OGR_Base_Male_A01"

PYLON_MATERIALS = {
    "M_OGR_CairnStone_Blockout_A01": (0.24, 0.25, 0.24),
    "M_OGR_Iron_Blockout_A01": (0.10, 0.10, 0.09),
    "M_OGR_Brass_Blockout_A01": (0.60, 0.34, 0.13),
    "M_OGR_SootedCopper_Blockout_A01": (0.40, 0.18, 0.075),
    "M_OGR_Leather_Blockout_A01": (0.20, 0.11, 0.07),
    "M_OGR_Warpaint_Blockout_A01": (0.28, 0.075, 0.035),
    "M_OGR_TekGlow_Blockout_A01": (1.0, 0.36, 0.025),
}

MANTICORE_MATERIALS = {
    "M_CRE_Manticore_Body_Blockout_A01": (0.50, 0.32, 0.15),
    "M_CRE_Manticore_Mane_Blockout_A01": (0.10, 0.07, 0.045),
    "M_CRE_Manticore_Wing_Blockout_A01": (0.20, 0.075, 0.055),
    "M_CRE_Manticore_TailClaw_Blockout_A01": (0.17, 0.13, 0.095),
    "M_CRE_Manticore_Venom_Blockout_A01": (0.18, 0.95, 0.30),
    "M_AET_ScaleMarker_Blockout_A01": (0.12, 0.12, 0.11),
}

CASTER_MATERIALS = {
    **OGRE_MATERIALS,
    "M_OGR_RuneGlow_Blockout_A01": (0.15, 0.62, 1.0),
    "M_OGR_StormRuneGlow_Blockout_A01": (0.26, 0.82, 1.0),
    "M_OGR_ShamanStone_Blockout_A01": (0.31, 0.32, 0.29),
    "M_OGR_FurMantle_Blockout_A01": (0.28, 0.20, 0.13),
    "M_OGR_GraveCloth_Blockout_A01": (0.055, 0.055, 0.052),
    "M_OGR_TombMetal_Blockout_A01": (0.095, 0.11, 0.10),
}


def add_cone_between(
    name: str,
    start: tuple[float, float, float],
    end: tuple[float, float, float],
    radius_base: float,
    radius_tip: float,
    material: bpy.types.Material,
    vertices: int = 12,
) -> bpy.types.Object:
    a = Vector(start)
    b = Vector(end)
    midpoint = (a + b) * 0.5
    direction = b - a
    length = direction.length
    bpy.ops.mesh.primitive_cone_add(
        vertices=vertices,
        radius1=radius_base,
        radius2=radius_tip,
        depth=length,
        location=midpoint,
    )
    obj = bpy.context.object
    obj.name = name
    obj.data.name = f"{name}_Mesh"
    obj.rotation_euler = direction.to_track_quat("Z", "Y").to_euler()
    bpy.ops.object.transform_apply(location=False, rotation=False, scale=True)
    obj.data.materials.append(material)
    polish_mesh_object(obj)
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
    polish_mesh_object(obj)
    return obj


def add_assigned(obj: bpy.types.Object, armature: bpy.types.Object, bone: str, objects: list[bpy.types.Object]) -> None:
    assign_to_bone(obj, armature, bone)
    objects.append(obj)


def set_review_materials(materials: dict[str, bpy.types.Material]) -> None:
    for material in materials.values():
        color = material.diffuse_color
        material.use_nodes = True
        bsdf = material.node_tree.nodes.get("Principled BSDF")
        if bsdf is None:
            continue
        bsdf.inputs["Base Color"].default_value = color
        bsdf.inputs["Roughness"].default_value = 0.84
        if "Glow" in material.name:
            bsdf.inputs["Emission Color"].default_value = color
            bsdf.inputs["Emission Strength"].default_value = 1.25


def add_review_lights(camera_location: tuple[float, float, float], key_target: tuple[float, float, float]) -> None:
    bpy.ops.object.light_add(type="SUN", location=(0, 0, 700), rotation=(math.radians(48), 0, math.radians(42)))
    sun = bpy.context.object
    sun.name = "AET_Review_SunFill"
    sun.data.energy = 1.35

    bpy.ops.object.light_add(type="AREA", location=(camera_location[0] * 0.55, camera_location[1] * 0.75, camera_location[2] + 280))
    key = bpy.context.object
    key.name = "AET_Review_KeyLight"
    key.data.energy = 13000
    key.data.size = 760

    bpy.ops.object.light_add(type="AREA", location=(key_target[0] - 420, key_target[1] + 520, key_target[2] + 240))
    fill = bpy.context.object
    fill.name = "AET_Review_FillLight"
    fill.data.energy = 4200
    fill.data.size = 720


def render_review(
    output: Path,
    camera_location: tuple[float, float, float],
    target: tuple[float, float, float],
    ortho_scale: float,
    resolution: tuple[int, int] = (1800, 1200),
) -> None:
    bpy.context.scene.view_settings.view_transform = PREFERRED_VIEW_TRANSFORM
    bpy.context.scene.view_settings.exposure = 0.0
    bpy.context.scene.view_settings.gamma = 1.0
    if bpy.context.scene.world is not None:
        bpy.context.scene.world.color = (0.58, 0.57, 0.55)
    add_review_lights(camera_location, target)
    bpy.ops.object.camera_add(location=camera_location)
    camera = bpy.context.object
    direction = Vector(target) - Vector(camera.location)
    camera.rotation_euler = direction.to_track_quat("-Z", "Y").to_euler()
    camera.data.type = "ORTHO"
    camera.data.ortho_scale = ortho_scale
    camera.data.clip_start = 1
    camera.data.clip_end = 7000
    bpy.context.scene.camera = camera
    bpy.context.scene.render.resolution_x = resolution[0]
    bpy.context.scene.render.resolution_y = resolution[1]
    output.parent.mkdir(parents=True, exist_ok=True)
    bpy.context.scene.render.filepath = str(output)
    bpy.ops.render.render(write_still=True)
    print(f"Rendered {output.relative_to(ROOT)}")


def export_static_fbx(path: Path) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    bpy.ops.object.select_all(action="DESELECT")
    for obj in bpy.context.scene.objects:
        if obj.type == "MESH":
            obj.select_set(True)
    bpy.ops.export_scene.fbx(
        filepath=str(path),
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
    print(f"Exported {path.relative_to(ROOT)}")


def build_crude_tek_pylon() -> None:
    clear_scene()
    setup_scene()
    materials = create_materials(PYLON_MATERIALS)
    set_review_materials(materials)
    stone = materials["M_OGR_CairnStone_Blockout_A01"]
    iron = materials["M_OGR_Iron_Blockout_A01"]
    brass = materials["M_OGR_Brass_Blockout_A01"]
    copper = materials["M_OGR_SootedCopper_Blockout_A01"]
    leather = materials["M_OGR_Leather_Blockout_A01"]
    paint = materials["M_OGR_Warpaint_Blockout_A01"]
    glow = materials["M_OGR_TekGlow_Blockout_A01"]

    # Ground pivot is centered under the rough cairn base.
    for index, (x, y, sx, sy, rot) in enumerate(
        [(-70, -55, 145, 95, -8), (75, -48, 152, 100, 7), (-35, 45, 175, 95, 4), (95, 54, 120, 90, -5)],
        1,
    ):
        obj = add_box_obj(f"Pylon_Base_CairnSlab_{index:02d}", (x, y, 18), (sx, sy, 36), stone)
        obj.rotation_euler[2] = math.radians(rot)

    add_box_obj("Pylon_Base_IronClamp_Front", (48, -98, 46), (165, 30, 42), iron)
    add_box_obj("Pylon_Base_IronClamp_Back", (-30, 98, 46), (155, 30, 42), iron)
    add_box_obj("Pylon_Base_WarpaintSlash", (82, -116, 70), (110, 7, 28), paint)

    add_cylinder_between("Pylon_Core_StoneColumn_A", (0, 0, 48), (0, 0, 302), 44, stone, 12)
    add_box_obj("Pylon_Core_IronBrace_Lower", (18, 0, 110), (42, 132, 44), iron)
    add_box_obj("Pylon_Core_IronBrace_Mid", (-18, 0, 190), (42, 118, 42), iron)
    add_box_obj("Pylon_Core_IronBrace_Upper", (12, 0, 270), (38, 102, 36), iron)
    add_ellipsoid_obj("Pylon_Core_RuneHeat_CrackedEngine", (56, 0, 206), (30, 36, 76), glow, 16, 8)
    add_box_obj("Pylon_Core_BrassCage_Vertical", (88, 0, 206), (22, 88, 158), brass)
    add_box_obj("Pylon_Core_BrassCage_CrossbarTop", (88, 0, 276), (28, 122, 20), brass)
    add_box_obj("Pylon_Core_BrassCage_CrossbarBottom", (88, 0, 136), (28, 122, 20), brass)

    for side, sign in (("Left", 1), ("Right", -1)):
        add_cylinder_between(
            f"Pylon_SideTank_{side}_CopperPressureVessel",
            (-48, sign * 96, 74),
            (-48, sign * 96, 255),
            24,
            copper,
            14,
        )
        add_cylinder_between(
            f"Pylon_SideTank_{side}_GlowVent",
            (-52, sign * 96, 112),
            (-52, sign * 96, 218),
            8,
            glow,
            10,
        )
        add_cylinder_between(
            f"Pylon_Cable_{side}_LeatherWrapped",
            (-48, sign * 96, 165),
            (60, sign * 52, 210),
            7,
            leather,
            10,
        )
        add_box_obj(f"Pylon_Conductor_{side}_IronFork", (6, sign * 124, 342), (36, 52, 90), iron)
        add_diamond_obj(f"Pylon_Conductor_{side}_RuneShard", (52, sign * 128, 354), (16, 13, 34), glow)

    add_cylinder_between("Pylon_TopArc_LeftIron", (-20, 74, 316), (42, 26, 420), 10, iron, 10)
    add_cylinder_between("Pylon_TopArc_RightIron", (-20, -74, 316), (42, -26, 420), 10, iron, 10)
    add_box_obj("Pylon_TopArc_BrassBridge", (48, 0, 422), (34, 92, 28), brass)
    add_diamond_obj("Pylon_TopArc_UnstableRuneHeat", (72, 0, 436), (28, 22, 42), glow)

    add_box_obj("Pylon_ServicePanel_Iron", (112, 0, 118), (18, 68, 58), iron)
    add_box_obj("Pylon_ServicePanel_BrassGauge", (124, -22, 124), (9, 18, 18), brass)
    add_box_obj("Pylon_ServicePanel_RawToggle", (126, 20, 124), (10, 10, 28), leather)

    # UCX hulls remain broad and gameplay-oriented.
    add_box_obj("UCX_SM_OGR_CrudeTekPylon_A01_00", (15, 0, 34), (265, 245, 68), stone)
    add_box_obj("UCX_SM_OGR_CrudeTekPylon_A01_01", (14, 0, 190), (142, 156, 270), stone)
    add_box_obj("UCX_SM_OGR_CrudeTekPylon_A01_02", (-48, 96, 165), (62, 62, 196), stone)
    add_box_obj("UCX_SM_OGR_CrudeTekPylon_A01_03", (-48, -96, 165), (62, 62, 196), stone)
    add_box_obj("UCX_SM_OGR_CrudeTekPylon_A01_04", (42, 0, 384), (142, 168, 124), stone)

    add_asset_metadata(
        "SM_OGR_CrudeTekPylon_A01",
        "First-pass Ogre Crude Tek Pylon DCC review source; final sculpt, UVs, textures, Blueprint behavior, and tuned collision pending.",
        "/Game/Aerathea/Props/Ogres/Teknomancy/SM_OGR_CrudeTekPylon_A01",
    )
    blend_path = BLENDER_ROOT / "Props/Ogres/Teknomancy/SM_OGR_CrudeTekPylon_A01/SM_OGR_CrudeTekPylon_A01.blend"
    export_path = EXPORT_ROOT / "Props/Ogres/Teknomancy/SM_OGR_CrudeTekPylon_A01/SM_OGR_CrudeTekPylon_A01.fbx"
    blend_path.parent.mkdir(parents=True, exist_ok=True)
    bpy.ops.wm.save_as_mainfile(filepath=str(blend_path))
    print(f"Built {blend_path.relative_to(ROOT)}")
    export_static_fbx(export_path)
    render_review(
        REVIEW_ROOT / "SM_OGR_CrudeTekPylon_A01_DCCReview.png",
        (780, -610, 390),
        (20, 0, 215),
        620,
    )


def make_manticore_bones() -> list[tuple[str, tuple[float, float, float], tuple[float, float, float], str | None]]:
    return [
        ("root", (0, 0, 0), (0, 0, 28), None),
        ("pelvis", (-105, 0, 126), (-42, 0, 138), "root"),
        ("spine_01", (-42, 0, 138), (34, 0, 154), "pelvis"),
        ("spine_02", (34, 0, 154), (104, 0, 176), "spine_01"),
        ("spine_03", (104, 0, 176), (164, 0, 204), "spine_02"),
        ("chest", (164, 0, 204), (214, 0, 224), "spine_03"),
        ("neck_01", (214, 0, 224), (256, 0, 256), "chest"),
        ("neck_02", (256, 0, 256), (292, 0, 284), "neck_01"),
        ("head", (292, 0, 284), (338, 0, 292), "neck_02"),
        ("jaw", (322, 0, 274), (360, 0, 268), "head"),
        ("ear_l", (298, 18, 306), (292, 40, 332), "head"),
        ("ear_r", (298, -18, 306), (292, -40, 332), "head"),
        ("clavicle_fl", (132, 44, 184), (132, 70, 160), "chest"),
        ("upperarm_fl", (132, 70, 160), (150, 82, 92), "clavicle_fl"),
        ("lowerarm_fl", (150, 82, 92), (176, 86, 32), "upperarm_fl"),
        ("paw_fl", (176, 86, 32), (220, 88, 5), "lowerarm_fl"),
        ("clavicle_fr", (132, -44, 184), (132, -70, 160), "chest"),
        ("upperarm_fr", (132, -70, 160), (150, -82, 92), "clavicle_fr"),
        ("lowerarm_fr", (150, -82, 92), (176, -86, 32), "upperarm_fr"),
        ("paw_fr", (176, -86, 32), (220, -88, 5), "lowerarm_fr"),
        ("thigh_bl", (-96, 50, 128), (-118, 72, 78), "pelvis"),
        ("calf_bl", (-118, 72, 78), (-92, 74, 30), "thigh_bl"),
        ("hock_bl", (-92, 74, 30), (-42, 76, 12), "calf_bl"),
        ("paw_bl", (-42, 76, 12), (8, 76, 5), "hock_bl"),
        ("thigh_br", (-96, -50, 128), (-118, -72, 78), "pelvis"),
        ("calf_br", (-118, -72, 78), (-92, -74, 30), "thigh_br"),
        ("hock_br", (-92, -74, 30), (-42, -76, 12), "calf_br"),
        ("paw_br", (-42, -76, 12), (8, -76, 5), "hock_br"),
        ("wing_l_root", (78, 58, 208), (44, 116, 230), "chest"),
        ("wing_l_upper", (44, 116, 230), (-44, 244, 248), "wing_l_root"),
        ("wing_l_lower", (-44, 244, 248), (-112, 384, 214), "wing_l_upper"),
        ("wing_l_hand", (-112, 384, 214), (-160, 476, 170), "wing_l_lower"),
        ("wing_l_tip", (-160, 476, 170), (-174, 520, 118), "wing_l_hand"),
        ("wing_r_root", (78, -58, 208), (44, -116, 230), "chest"),
        ("wing_r_upper", (44, -116, 230), (-44, -244, 248), "wing_r_root"),
        ("wing_r_lower", (-44, -244, 248), (-112, -384, 214), "wing_r_upper"),
        ("wing_r_hand", (-112, -384, 214), (-160, -476, 170), "wing_r_lower"),
        ("wing_r_tip", (-160, -476, 170), (-174, -520, 118), "wing_r_hand"),
        ("tail_01", (-150, 0, 140), (-208, 0, 210), "pelvis"),
        ("tail_02", (-208, 0, 210), (-246, 0, 294), "tail_01"),
        ("tail_03", (-246, 0, 294), (-238, 0, 382), "tail_02"),
        ("tail_04", (-238, 0, 382), (-190, 0, 454), "tail_03"),
        ("tail_05", (-190, 0, 454), (-118, 0, 492), "tail_04"),
        ("tail_06", (-118, 0, 492), (-44, 0, 500), "tail_05"),
        ("tail_07", (-44, 0, 500), (18, 0, 486), "tail_06"),
        ("tail_08", (18, 0, 486), (70, 0, 458), "tail_07"),
        ("tail_stinger_base", (70, 0, 458), (112, 0, 428), "tail_08"),
        ("tail_stinger_tip", (112, 0, 428), (150, 0, 394), "tail_stinger_base"),
    ]


def add_wing_membrane(
    name: str,
    root: tuple[float, float, float],
    mid: tuple[float, float, float],
    tip: tuple[float, float, float],
    trailing: tuple[float, float, float],
    material: bpy.types.Material,
) -> bpy.types.Object:
    verts = [root, mid, tip, trailing]
    faces = [(0, 1, 2, 3), (3, 2, 1, 0)]
    mesh = bpy.data.meshes.new(f"{name}_Mesh")
    mesh.from_pydata(verts, [], faces)
    mesh.update()
    obj = bpy.data.objects.new(name, mesh)
    bpy.context.collection.objects.link(obj)
    obj.data.materials.append(material)
    polish_mesh_object(obj)
    return obj


def add_manticore_variant(
    label: str,
    armature_name: str,
    materials: dict[str, bpy.types.Material],
    interrupt: bool = False,
) -> tuple[bpy.types.Object, list[bpy.types.Object]]:
    armature = create_armature(armature_name, make_manticore_bones())
    objects: list[bpy.types.Object] = []
    body = materials["M_CRE_Manticore_Body_Blockout_A01"]
    mane = materials["M_CRE_Manticore_Mane_Blockout_A01"]
    wing = materials["M_CRE_Manticore_Wing_Blockout_A01"]
    tail = materials["M_CRE_Manticore_TailClaw_Blockout_A01"]
    venom = materials["M_CRE_Manticore_Venom_Blockout_A01"]

    body_offset = 0 if not interrupt else 10
    add_assigned(add_ellipsoid_obj(f"{label}_Body_LionRear", (-74, 0, 126), (124, 68, 56), body, 20, 10), armature, "pelvis", objects)
    add_assigned(add_ellipsoid_obj(f"{label}_Body_PowerChest", (94, 0, 162), (140, 74, 72), body, 20, 10), armature, "chest", objects)
    add_assigned(add_ellipsoid_obj(f"{label}_Neck_ManeMass", (226, 0, 230), (68, 48, 74), mane, 16, 8), armature, "neck_01", objects)
    add_assigned(add_ellipsoid_obj(f"{label}_Head_LionPredator", (310, 0, 282 + body_offset), (48, 35, 35), body, 16, 8), armature, "head", objects)
    add_assigned(add_box_obj(f"{label}_Muzzle_Block", (352, 0, 270 + body_offset), (62, 38, 28), body), armature, "head", objects)
    add_assigned(add_box_obj(f"{label}_Jaw_Dark", (352, 0, 252 + body_offset), (58, 34, 14), mane), armature, "jaw", objects)
    for side, sign in (("Left", 1), ("Right", -1)):
        add_assigned(add_cone_between(f"{label}_Ear_{side}", (300, sign * 20, 308), (292, sign * 44, 338), 9, 2, mane, 8), armature, f"ear_{'l' if sign > 0 else 'r'}", objects)
        add_assigned(add_box_obj(f"{label}_Mane_Clump_{side}_01", (220, sign * 42, 218), (78, 26, 84), mane), armature, "neck_01", objects)
        add_assigned(add_box_obj(f"{label}_Mane_Clump_{side}_02", (174, sign * 48, 186), (74, 24, 76), mane), armature, "chest", objects)

    for side, sign, prefix, upper, lower, foot in (
        ("Left", 1, "Fore", "upperarm_fl", "lowerarm_fl", "paw_fl"),
        ("Right", -1, "Fore", "upperarm_fr", "lowerarm_fr", "paw_fr"),
        ("Left", 1, "Hind", "thigh_bl", "calf_bl", "paw_bl"),
        ("Right", -1, "Hind", "thigh_br", "calf_br", "paw_br"),
    ):
        is_fore = prefix == "Fore"
        x0 = 138 if is_fore else -108
        y0 = 74 * sign
        add_assigned(add_cylinder_between(f"{label}_{prefix}Leg_{side}_Upper", (x0, y0, 152 if is_fore else 128), (x0 + (22 if is_fore else -8), y0 + 10 * sign, 78), 16 if is_fore else 18, body, 12), armature, upper, objects)
        add_assigned(add_cylinder_between(f"{label}_{prefix}Leg_{side}_Lower", (x0 + (22 if is_fore else -8), y0 + 10 * sign, 78), (x0 + (46 if is_fore else 28), y0 + 12 * sign, 20), 13, body, 12), armature, lower, objects)
        add_assigned(add_box_obj(f"{label}_{prefix}Paw_{side}", (x0 + (78 if is_fore else 70), y0 + 12 * sign, 9), (62, 28, 18), body), armature, foot, objects)
        for index, claw_y in enumerate((-9, 0, 9), 1):
            add_assigned(
                add_cone_between(
                    f"{label}_{prefix}Claw_{side}_{index}",
                    (x0 + (108 if is_fore else 100), y0 + 12 * sign + claw_y, 9),
                    (x0 + (132 if is_fore else 124), y0 + 12 * sign + claw_y, 5),
                    4,
                    0,
                    tail,
                    8,
                ),
                armature,
                foot,
                objects,
            )

    for side, sign, suffix in (("Left", 1, "l"), ("Right", -1, "r")):
        root = (78, sign * 58, 208)
        upper_tip = (-44, sign * 244, 248)
        lower_tip = (-112, sign * 384, 214)
        hand_tip = (-160, sign * 476, 170)
        final_tip = (-174, sign * 520, 118)
        add_assigned(add_cylinder_between(f"{label}_Wing_{side}_RootArm", root, upper_tip, 9, tail, 10), armature, f"wing_{suffix}_upper", objects)
        add_assigned(add_cylinder_between(f"{label}_Wing_{side}_LowerArm", upper_tip, lower_tip, 7, tail, 10), armature, f"wing_{suffix}_lower", objects)
        add_assigned(add_cylinder_between(f"{label}_Wing_{side}_FingerMain", lower_tip, final_tip, 5, tail, 10), armature, f"wing_{suffix}_hand", objects)
        add_assigned(add_wing_membrane(f"{label}_Wing_{side}_Membrane_Main", root, upper_tip, final_tip, (34, sign * 206, 112), wing), armature, f"wing_{suffix}_lower", objects)
        add_assigned(add_wing_membrane(f"{label}_Wing_{side}_Membrane_Outer", upper_tip, lower_tip, final_tip, (-42, sign * 338, 96), wing), armature, f"wing_{suffix}_hand", objects)
        if interrupt:
            add_assigned(add_box_obj(f"{label}_Wing_{side}_TornNotch_Silhouette", (-88, sign * 420, 126), (42, 22, 14), venom), armature, f"wing_{suffix}_hand", objects)

    tail_points = [
        (-150, 0, 140),
        (-208, 0, 210),
        (-246, 0, 294),
        (-238, 0, 382),
        (-190, 0, 454),
        (-118, 0, 492),
        (-44, 0, 500),
        (18, 0, 486),
        (70, 0, 458),
    ]
    for index, (start, end) in enumerate(zip(tail_points, tail_points[1:]), 1):
        add_assigned(add_cylinder_between(f"{label}_TailSegment_{index:02d}", start, end, max(9, 22 - index), tail, 12), armature, f"tail_{index:02d}", objects)
        add_assigned(add_box_obj(f"{label}_TailArmorPlate_{index:02d}", ((start[0] + end[0]) * 0.5, 0, (start[2] + end[2]) * 0.5 + 12), (34, 44 - index * 2, 10), tail), armature, f"tail_{index:02d}", objects)
    add_assigned(add_cone_between(f"{label}_TailStinger_Hooked", (70, 0, 458), (150, 0, 394), 24, 4, tail, 12), armature, "tail_stinger_base", objects)
    add_assigned(add_diamond_obj(f"{label}_TailStinger_VenomNode", (128, 0, 414), (14, 12, 18), venom), armature, "tail_stinger_base", objects)

    if interrupt:
        for index, x in enumerate((70, 126, 186, 258), 1):
            add_assigned(add_box_obj(f"{label}_BattleScar_Glow_{index:02d}", (x, -42, 190 + index * 8), (36, 6, 8), venom), armature, "chest" if x < 220 else "neck_01", objects)

    for socket_name, location, bone_name in [
        ("SOCKET_socket_head_fx", (334, 0, 294), "head"),
        ("SOCKET_socket_mouth_fx", (374, 0, 270), "head"),
        ("SOCKET_socket_bite_trace", (386, 0, 264), "jaw"),
        ("SOCKET_socket_claw_l", (252, 86, 6), "paw_fl"),
        ("SOCKET_socket_claw_r", (252, -86, 6), "paw_fr"),
        ("SOCKET_socket_foot_l", (196, 86, 6), "paw_fl"),
        ("SOCKET_socket_foot_r", (196, -86, 6), "paw_fr"),
        ("SOCKET_socket_wing_l_root", (78, 58, 208), "wing_l_root"),
        ("SOCKET_socket_wing_r_root", (78, -58, 208), "wing_r_root"),
        ("SOCKET_socket_wing_l_tip", (-174, 520, 118), "wing_l_tip"),
        ("SOCKET_socket_wing_r_tip", (-174, -520, 118), "wing_r_tip"),
        ("SOCKET_socket_tail_base", (-150, 0, 140), "tail_01"),
        ("SOCKET_socket_tail_mid", (-190, 0, 454), "tail_04"),
        ("SOCKET_socket_tail_stinger", (150, 0, 394), "tail_stinger_tip"),
        ("SOCKET_socket_vfx_venom_drip", (142, 0, 404), "tail_stinger_tip"),
        ("SOCKET_socket_vfx_landing_dust", (42, 0, 6), "root"),
        ("SOCKET_socket_back_variant", (30, 0, 224), "spine_02"),
    ]:
        add_socket_empty(socket_name, location, armature, bone_name)

    return armature, objects


def export_manticore(name: str, folder: str, unreal_path: str, interrupt: bool = False) -> None:
    clear_scene()
    setup_scene()
    materials = create_materials(MANTICORE_MATERIALS)
    set_review_materials(materials)
    armature, objects = add_manticore_variant(
        name.replace("SK_CRE_", "").replace("_A01", ""),
        "SKEL_CRE_Manticore_A01",
        materials,
        interrupt=interrupt,
    )
    add_asset_metadata(
        name,
        "First-pass Manticore DCC review source; final sculpt, retopo, skinning, physics, LODs, animation, and textures pending.",
        unreal_path,
    )
    blend_path = BLENDER_ROOT / folder / f"{name}.blend"
    export_path = EXPORT_ROOT / folder / f"{name}.fbx"
    blend_path.parent.mkdir(parents=True, exist_ok=True)
    bpy.ops.wm.save_as_mainfile(filepath=str(blend_path))
    print(f"Built {blend_path.relative_to(ROOT)}")
    export_skeletal_fbx(export_path, objects, armature, bake_anim=False)
    print(f"Exported {export_path.relative_to(ROOT)}")

    # Add lightweight scale markers only to the review render scene.
    scale_mat = materials["M_AET_ScaleMarker_Blockout_A01"]
    add_ellipsoid_obj("Scale_Ogre_330cm_Head", (0, -690, 315), (18, 18, 22), scale_mat, 10, 5)
    add_cylinder_between("Scale_Ogre_330cm_Body", (0, -690, 292), (0, -690, 130), 16, scale_mat, 10)
    add_cylinder_between("Scale_Mek_360cm_Body", (0, 690, 340), (0, 690, 130), 24, scale_mat, 10)
    render_review(
        REVIEW_ROOT / f"{name}_DCCReview.png",
        (1040, -1060, 540),
        (42, 0, 220),
        1260,
        (2000, 1250),
    )


def add_shaman_gear(
    label: str,
    armature: bpy.types.Object,
    objects: list[bpy.types.Object],
    height: float,
    materials: dict[str, bpy.types.Material],
) -> None:
    iron = materials["M_OGR_Iron_Blockout_A01"]
    leather = materials["M_OGR_Leather_Blockout_A01"]
    bone = materials["M_OGR_Bone_Blockout_A01"]
    stone = materials["M_OGR_ShamanStone_Blockout_A01"]
    fur = materials["M_OGR_FurMantle_Blockout_A01"]
    glow = materials["M_OGR_StormRuneGlow_Blockout_A01"]
    shoulder = height * 0.185
    arm_side = height * 0.235

    add_assigned(add_box_obj(f"{label}_FurMantle_BroadShoulders", p((-12, 0, height * 0.745), 0), (62, shoulder * 2.6, 58), fur), armature, "chest", objects)
    add_assigned(add_box_obj(f"{label}_RuneWheel_BackStone", p((-70, 0, height * 0.68), 0), (36, 148, 148), stone), armature, "chest", objects)
    add_assigned(add_diamond_obj(f"{label}_RuneWheel_CenterGlow", p((-92, 0, height * 0.68), 0), (18, 18, 28), glow), armature, "chest", objects)
    for y in (-56, 0, 56):
        add_assigned(add_box_obj(f"{label}_RuneWheel_StoneSpoke_{y}", p((-96, y, height * 0.68), 0), (22, 12, 122), stone), armature, "chest", objects)
    add_assigned(add_box_obj(f"{label}_Chest_RuneTotem", p((58, 0, height * 0.64), 0), (24, 48, 78), stone), armature, "chest", objects)
    add_assigned(add_diamond_obj(f"{label}_Chest_RuneGlow", p((78, 0, height * 0.65), 0), (12, 14, 20), glow), armature, "chest", objects)
    for side, sign, suffix in (("Left", 1, "l"), ("Right", -1, "r")):
        add_assigned(add_box_obj(f"{label}_BoneCharm_{side}_Shoulder", p((38, sign * shoulder * 1.2, height * 0.73), 0), (22, 36, 42), bone), armature, "chest", objects)
        add_assigned(add_box_obj(f"{label}_HideBracer_{side}", p((18, sign * arm_side * 1.03, height * 0.46), 0), (48, 66, 54), leather), armature, f"lowerarm_{suffix}", objects)

    staff_y = -arm_side * 1.30
    add_assigned(add_cylinder_between(f"{label}_Staff_StonewoodShaft", p((72, staff_y, height * 0.20), 0), p((116, staff_y, height * 0.92), 0), 8, leather, 12), armature, "hand_r", objects)
    add_assigned(add_box_obj(f"{label}_Staff_StoneHead", p((122, staff_y, height * 0.92), 0), (72, 46, 58), stone), armature, "hand_r", objects)
    add_assigned(add_diamond_obj(f"{label}_Staff_StormRuneGlow", p((142, staff_y, height * 0.94), 0), (18, 16, 28), glow), armature, "hand_r", objects)
    add_assigned(add_cone_between(f"{label}_Staff_BoneTine_Left", p((120, staff_y + 20, height * 0.92), 0), p((154, staff_y + 34, height * 0.98), 0), 5, 0, bone, 8), armature, "hand_r", objects)
    add_assigned(add_cone_between(f"{label}_Staff_BoneTine_Right", p((120, staff_y - 20, height * 0.92), 0), p((154, staff_y - 34, height * 0.98), 0), 5, 0, bone, 8), armature, "hand_r", objects)

    for socket_name, location, bone_name in [
        ("SOCKET_vfx_staff_head", p((142, staff_y, height * 0.94), 0), "hand_r"),
        ("SOCKET_vfx_rune_wheel", p((-96, 0, height * 0.68), 0), "chest"),
        ("SOCKET_vfx_totem_chest", p((80, 0, height * 0.65), 0), "chest"),
        ("SOCKET_weapon_staff_r", p((84, staff_y, height * 0.36), 0), "hand_r"),
        ("SOCKET_head_fx", p((48, 0, height * 0.89), 0), "head"),
    ]:
        add_socket_empty(socket_name, location, armature, bone_name)


def add_necromancer_gear(
    label: str,
    armature: bpy.types.Object,
    objects: list[bpy.types.Object],
    height: float,
    materials: dict[str, bpy.types.Material],
) -> None:
    iron = materials["M_OGR_TombMetal_Blockout_A01"]
    cloth = materials["M_OGR_GraveCloth_Blockout_A01"]
    leather = materials["M_OGR_Leather_Blockout_A01"]
    bone = materials["M_OGR_Bone_Blockout_A01"]
    glow = materials["M_OGR_NecroGlow_Blockout_A01"]
    shoulder = height * 0.185
    arm_side = height * 0.235

    add_assigned(add_box_obj(f"{label}_GraveCloth_Hood", p((12, 0, height * 0.91), 0), (72, 92, 72), cloth), armature, "head", objects)
    add_assigned(add_box_obj(f"{label}_GraveCloth_RobeFront", p((46, 0, height * 0.55), 0), (40, shoulder * 1.24, height * 0.38), cloth), armature, "spine_01", objects)
    add_assigned(add_box_obj(f"{label}_TombPlate_Chest", p((70, 0, height * 0.66), 0), (22, 96, 86), iron), armature, "chest", objects)
    add_assigned(add_diamond_obj(f"{label}_Chest_NecroGlow", p((86, 0, height * 0.66), 0), (12, 16, 24), glow), armature, "chest", objects)
    add_assigned(add_box_obj(f"{label}_Back_TombstonePlate", p((-64, 0, height * 0.66), 0), (42, 126, 136), iron), armature, "chest", objects)
    for index, y in enumerate((-46, -18, 18, 46), 1):
        add_assigned(add_ellipsoid_obj(f"{label}_SkullBelt_{index:02d}", p((62, y, height * 0.48), 0), (14, 11, 14), bone, 10, 5), armature, "pelvis", objects)
    for side, sign, suffix in (("Left", 1, "l"), ("Right", -1, "r")):
        add_assigned(add_box_obj(f"{label}_TombBracer_{side}", p((18, sign * arm_side * 1.03, height * 0.46), 0), (50, 70, 56), iron), armature, f"lowerarm_{suffix}", objects)
        add_assigned(add_diamond_obj(f"{label}_BracerGlow_{side}", p((54, sign * arm_side * 1.08, height * 0.46), 0), (10, 12, 18), glow), armature, f"lowerarm_{suffix}", objects)

    staff_y = -arm_side * 1.30
    add_assigned(add_cylinder_between(f"{label}_Staff_BlackShaft", p((70, staff_y, height * 0.18), 0), p((112, staff_y, height * 0.90), 0), 8, leather, 12), armature, "hand_r", objects)
    add_assigned(add_ellipsoid_obj(f"{label}_Staff_GraveLanternCage", p((126, staff_y, height * 0.88), 0), (28, 26, 42), iron, 12, 6), armature, "hand_r", objects)
    add_assigned(add_ellipsoid_obj(f"{label}_Staff_NecroLanternGlow", p((132, staff_y, height * 0.88), 0), (14, 14, 24), glow, 10, 5), armature, "hand_r", objects)
    add_assigned(add_cone_between(f"{label}_Staff_BoneHook", p((126, staff_y, height * 0.91), 0), p((168, staff_y - 24, height * 0.97), 0), 5, 0, bone, 8), armature, "hand_r", objects)

    for socket_name, location, bone_name in [
        ("SOCKET_vfx_lantern_core", p((132, staff_y, height * 0.88), 0), "hand_r"),
        ("SOCKET_vfx_chest_necro", p((88, 0, height * 0.66), 0), "chest"),
        ("SOCKET_vfx_bracer_l", p((54, arm_side * 1.08, height * 0.46), 0), "lowerarm_l"),
        ("SOCKET_vfx_bracer_r", p((54, -arm_side * 1.08, height * 0.46), 0), "lowerarm_r"),
        ("SOCKET_weapon_staff_r", p((84, staff_y, height * 0.36), 0), "hand_r"),
        ("SOCKET_head_fx", p((48, 0, height * 0.89), 0), "head"),
    ]:
        add_socket_empty(socket_name, location, armature, bone_name)


def export_ogre_caster(name: str, label: str, folder: str, unreal_path: str, gear_fn) -> None:
    clear_scene()
    setup_scene()
    materials = create_materials(CASTER_MATERIALS)
    set_review_materials(materials)
    armature, objects = add_ogre_variant(label, OGRE_BASE_MALE_ARMATURE_NAME, 330.0, 0.0, "male", materials)
    gear_fn(label, armature, objects, 330.0, materials)
    add_asset_metadata(
        name,
        f"First-pass Ogre {label} class-fit source over Ogre male base; final sculpt, retopo, UVs, textures, skinning, and animation pending.",
        unreal_path,
    )
    blend_path = BLENDER_ROOT / folder / f"{name}.blend"
    export_path = EXPORT_ROOT / folder / f"{name}.fbx"
    blend_path.parent.mkdir(parents=True, exist_ok=True)
    bpy.ops.wm.save_as_mainfile(filepath=str(blend_path))
    print(f"Built {blend_path.relative_to(ROOT)}")
    export_skeletal_fbx(export_path, objects, armature, bake_anim=False)
    print(f"Exported {export_path.relative_to(ROOT)}")
    render_review(
        REVIEW_ROOT / f"{name}_DCCReview.png",
        (900, -640, 420),
        (24, 0, 178),
        520,
    )


def main() -> None:
    build_crude_tek_pylon()
    export_manticore(
        "SK_CRE_Manticore_A01",
        "Creatures/Manticores/SK_CRE_Manticore_A01",
        "/Game/Aerathea/Creatures/Manticores/Base/SK_CRE_Manticore_A01",
        interrupt=False,
    )
    export_manticore(
        "SK_CRE_Manticore_Interrupt_A01",
        "Creatures/Manticores/SK_CRE_Manticore_Interrupt_A01",
        "/Game/Aerathea/Creatures/Manticores/SK_CRE_Manticore_Interrupt_A01",
        interrupt=True,
    )
    export_ogre_caster(
        "SK_OGR_Shaman_A01",
        "Shaman",
        "Characters/Ogres/Shaman/SK_OGR_Shaman_A01",
        "/Game/Aerathea/Characters/Ogres/Shaman/SK_OGR_Shaman_A01",
        add_shaman_gear,
    )
    export_ogre_caster(
        "SK_OGR_Necromancer_A01",
        "Necromancer",
        "Characters/Ogres/Necromancer/SK_OGR_Necromancer_A01",
        "/Game/Aerathea/Characters/Ogres/Necromancer/SK_OGR_Necromancer_A01",
        add_necromancer_gear,
    )


if __name__ == "__main__":
    main()
