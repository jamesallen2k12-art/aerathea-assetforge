#!/usr/bin/env python3
"""Build first-pass Ogre Teknomancer class-fit review assets."""

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
REVIEW_ROOT = ROOT / "Saved" / "Automation" / "OgreTeknomancerReview"

sys.path.insert(0, str(ROOT))

from Tools.DCC.build_next_slice_assets import (  # noqa: E402
    add_asset_metadata,
    add_box_obj,
    add_cylinder_between,
    add_ellipsoid_obj,
    add_socket_empty,
    assign_to_bone,
    clear_scene,
    create_materials,
    export_skeletal_fbx,
    setup_scene,
)
from Tools.DCC.build_ogre_base import (  # noqa: E402
    OGRE_MATERIALS,
    add_ogre_variant,
    make_review_materials_readable,
    p,
)


TEKNOMANCER_MATERIALS = {
    **OGRE_MATERIALS,
    "M_OGR_TekGlow_Blockout_A01": (1.0, 0.36, 0.03),
    "M_OGR_SootedCopper_Blockout_A01": (0.40, 0.18, 0.075),
}
OGRE_BASE_MALE_ARMATURE_NAME = "SKEL_SK_OGR_Base_Male_A01"


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


def add_assigned(obj: bpy.types.Object, armature: bpy.types.Object, bone: str, objects: list[bpy.types.Object]) -> None:
    assign_to_bone(obj, armature, bone)
    objects.append(obj)


def add_teknomancer_gear(
    label: str,
    armature: bpy.types.Object,
    objects: list[bpy.types.Object],
    height: float,
    materials: dict[str, bpy.types.Material],
) -> None:
    iron = materials["M_OGR_Iron_Blockout_A01"]
    brass = materials["M_OGR_Brass_Blockout_A01"]
    copper = materials["M_OGR_SootedCopper_Blockout_A01"]
    leather = materials["M_OGR_Leather_Blockout_A01"]
    bone = materials["M_OGR_Bone_Blockout_A01"]
    tek_glow = materials["M_OGR_TekGlow_Blockout_A01"]

    shoulder = height * 0.185
    arm_side = height * 0.235

    # Deliberately asymmetric: huge right-side machinery, exposed working left arm.
    add_assigned(
        add_box_obj(f"{label}_Tek_ShoulderRight_IronSlab", p((0, -shoulder * 1.15, height * 0.78), 0), (72, 92, 48), iron),
        armature,
        "chest",
        objects,
    )
    add_assigned(
        add_box_obj(f"{label}_Tek_ShoulderRight_SkullGuard", p((34, -shoulder * 1.32, height * 0.80), 0), (44, 54, 38), bone),
        armature,
        "chest",
        objects,
    )
    add_assigned(
        add_box_obj(f"{label}_Tek_ChestCrossBrace_Iron", p((52, 0, height * 0.68), 0), (24, shoulder * 1.72, 34), iron),
        armature,
        "chest",
        objects,
    )
    add_assigned(
        add_box_obj(f"{label}_Tek_BeltReactor_IronCage", p((58, 0, height * 0.50), 0), (54, 98, 62), iron),
        armature,
        "pelvis",
        objects,
    )
    add_assigned(
        add_ellipsoid_obj(f"{label}_Tek_BeltReactor_ForgeCore", p((92, 0, height * 0.50), 0), (20, 25, 31), tek_glow, 16, 8),
        armature,
        "pelvis",
        objects,
    )
    add_assigned(
        add_box_obj(f"{label}_Tek_BackEngine_IronBlock", p((-70, 0, height * 0.66), 0), (52, 110, 124), iron),
        armature,
        "chest",
        objects,
    )
    for side, sign in (("Left", 1), ("Right", -1)):
        add_assigned(
            add_cylinder_between(
                f"{label}_Tek_BackTank_{side}_Copper",
                p((-92, sign * 44, height * 0.56), 0),
                p((-92, sign * 44, height * 0.78), 0),
                15,
                copper,
                12,
            ),
            armature,
            "chest",
            objects,
        )
        add_assigned(
            add_cylinder_between(
                f"{label}_Tek_BackTank_{side}_GlowCore",
                p((-94, sign * 44, height * 0.60), 0),
                p((-94, sign * 44, height * 0.74), 0),
                7,
                tek_glow,
                10,
            ),
            armature,
            "chest",
            objects,
        )
    add_assigned(
        add_cylinder_between(f"{label}_Tek_Hose_BackToBracer_R", p((-48, -20, height * 0.66), 0), p((8, -arm_side, height * 0.53), 0), 5.0, copper, 10),
        armature,
        "chest",
        objects,
    )
    add_assigned(
        add_box_obj(f"{label}_Tek_BracerRight_ReactorPlate", p((16, -arm_side * 1.03, height * 0.46), 0), (62, 92, 70), iron),
        armature,
        "lowerarm_r",
        objects,
    )
    add_assigned(
        add_ellipsoid_obj(f"{label}_Tek_BracerRight_GlowVent", p((54, -arm_side * 1.08, height * 0.47), 0), (14, 24, 26), tek_glow, 12, 6),
        armature,
        "lowerarm_r",
        objects,
    )
    add_assigned(
        add_box_obj(f"{label}_Tek_BracerLeft_ToolClamp", p((14, arm_side * 1.02, height * 0.46), 0), (46, 66, 52), iron),
        armature,
        "lowerarm_l",
        objects,
    )
    add_assigned(
        add_box_obj(f"{label}_Tek_BracerLeft_BrassGauge", p((48, arm_side * 1.08, height * 0.46), 0), (18, 24, 24), brass),
        armature,
        "lowerarm_l",
        objects,
    )

    # Hammer is carried in the right hand for the review pose.
    hammer_center = p((88, -arm_side * 1.24, height * 0.18), 0)
    add_assigned(
        add_cylinder_between(f"{label}_Tek_Hammer_Handle", p((54, -arm_side * 1.18, height * 0.30), 0), p((156, -arm_side * 1.30, height * 0.06), 0), 9.0, leather, 12),
        armature,
        "hand_r",
        objects,
    )
    add_assigned(
        add_box_obj(f"{label}_Tek_Hammer_Head_IronCrusher", hammer_center, (112, 72, 82), iron),
        armature,
        "hand_r",
        objects,
    )
    add_assigned(
        add_box_obj(f"{label}_Tek_Hammer_ForgeWindow", p((122, -arm_side * 1.24, height * 0.18), 0), (18, 46, 52), tek_glow),
        armature,
        "hand_r",
        objects,
    )
    add_assigned(
        add_box_obj(f"{label}_Tek_Hammer_SpineSpike", p((160, -arm_side * 1.24, height * 0.22), 0), (44, 28, 28), iron),
        armature,
        "hand_r",
        objects,
    )
    for index, y in enumerate((-28, 0, 28), 1):
        add_assigned(
            add_diamond_obj(f"{label}_Tek_Hammer_RivetTooth_{index}", p((76, -arm_side * 1.24 + y, height * 0.235), 0), (12, 8, 18), bone),
            armature,
            "hand_r",
            objects,
        )

    for socket_name, location, bone_name in [
        ("SOCKET_vfx_hammer_core", p((122, -arm_side * 1.24, height * 0.18), 0), "hand_r"),
        ("SOCKET_vfx_bracer_l", p((50, arm_side * 1.08, height * 0.48), 0), "lowerarm_l"),
        ("SOCKET_vfx_bracer_r", p((58, -arm_side * 1.08, height * 0.48), 0), "lowerarm_r"),
        ("SOCKET_vfx_tek_core", p((94, 0, height * 0.50), 0), "pelvis"),
        ("SOCKET_weapon_socket_r", p((82, -arm_side * 1.18, height * 0.28), 0), "hand_r"),
        ("SOCKET_head_fx", p((48, 0, height * 0.89), 0), "head"),
    ]:
        add_socket_empty(socket_name, location, armature, bone_name)


def build_teknomancer_variant() -> None:
    clear_scene()
    setup_scene()
    materials = create_materials(TEKNOMANCER_MATERIALS)
    armature, objects = add_ogre_variant("Teknomancer", OGRE_BASE_MALE_ARMATURE_NAME, 330.0, 0.0, "male", materials)
    add_teknomancer_gear("Teknomancer", armature, objects, 330.0, materials)
    add_asset_metadata(
        "SK_OGR_Teknomancer_A01",
        "First-pass Ogre Teknomancer class-fit source over the Ogre male base; final sculpt, retopo, UVs, textures, skinning, and animation pending.",
        "/Game/Aerathea/Characters/Ogres/Teknomancer/SK_OGR_Teknomancer_A01",
    )
    export_path = EXPORT_ROOT / "Characters/Ogres/Teknomancer/SK_OGR_Teknomancer_A01/SK_OGR_Teknomancer_A01.fbx"
    export_skeletal_fbx(export_path, objects, armature, bake_anim=False)

    blend_path = BLENDER_ROOT / "Characters/Ogres/Teknomancer/SK_OGR_Teknomancer_A01/SK_OGR_Teknomancer_A01.blend"
    blend_path.parent.mkdir(parents=True, exist_ok=True)
    bpy.ops.wm.save_as_mainfile(filepath=str(blend_path))
    print(f"Built {blend_path.relative_to(ROOT)}")
    print(f"Exported {export_path.relative_to(ROOT)}")


def render_review() -> None:
    clear_scene()
    setup_scene()
    bpy.context.scene.view_settings.view_transform = "Standard"
    if bpy.context.scene.world is not None:
        bpy.context.scene.world.color = (0.58, 0.58, 0.55)

    materials = create_materials(TEKNOMANCER_MATERIALS)
    make_review_materials_readable(materials)
    armature, objects = add_ogre_variant("Teknomancer", OGRE_BASE_MALE_ARMATURE_NAME, 330.0, 0.0, "male", materials)
    add_teknomancer_gear("Teknomancer", armature, objects, 330.0, materials)

    bpy.ops.object.light_add(type="SUN", location=(0, 0, 620), rotation=(math.radians(48), 0, math.radians(40)))
    bpy.context.object.data.energy = 1.4
    bpy.ops.object.light_add(type="AREA", location=(900, -220, 620))
    key = bpy.context.object
    key.name = "AET_TeknomancerReview_KeyLight"
    key.data.energy = 15500
    key.data.size = 780

    bpy.ops.object.camera_add(location=(830, -650, 285))
    camera = bpy.context.object
    target = Vector((30, -10, 185))
    direction = target - Vector(camera.location)
    camera.rotation_euler = direction.to_track_quat("-Z", "Y").to_euler()
    camera.data.type = "ORTHO"
    camera.data.ortho_scale = 470
    camera.data.clip_start = 1
    camera.data.clip_end = 5000
    bpy.context.scene.camera = camera
    bpy.context.scene.render.resolution_x = 1400
    bpy.context.scene.render.resolution_y = 1400

    REVIEW_ROOT.mkdir(parents=True, exist_ok=True)
    output = REVIEW_ROOT / "SK_OGR_Teknomancer_A01_DCCReview.png"
    bpy.context.scene.render.filepath = str(output)
    bpy.ops.render.render(write_still=True)
    print(f"Rendered {output.relative_to(ROOT)}")


def main() -> None:
    build_teknomancer_variant()
    render_review()


if __name__ == "__main__":
    main()
