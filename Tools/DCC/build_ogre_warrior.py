#!/usr/bin/env python3
"""Build first-pass Ogre Warrior rivalry review assets."""

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
REVIEW_ROOT = ROOT / "Saved" / "Automation" / "OgreWarriorReview"

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


WARRIOR_MATERIALS = {
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


def add_spike_row(
    label: str,
    armature: bpy.types.Object,
    objects: list[bpy.types.Object],
    material: bpy.types.Material,
    centers: list[tuple[float, float, float]],
    bone: str,
) -> None:
    for index, center in enumerate(centers, 1):
        add_assigned(
            add_diamond_obj(f"{label}_Spike_{index:02d}", center, (12, 10, 22), material),
            armature,
            bone,
            objects,
        )


def add_warrior_gear(
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
    paint = materials["M_OGR_Warpaint_Blockout_A01"]
    forge = materials["M_OGR_TekGlow_Blockout_A01"]

    shoulder = height * 0.185
    arm_side = height * 0.235
    hip_side = height * 0.092

    # Symmetric brute armor: simple, brutal, and less technical than the Teknomancer.
    for side, sign, suffix in (("Left", 1, "l"), ("Right", -1, "r")):
        add_assigned(
            add_box_obj(
                f"{label}_Warrior_Shoulder_{side}_IronPlate",
                p((-2, sign * shoulder * 1.10, height * 0.775), 0),
                (70, 92, 42),
                iron,
            ),
            armature,
            "chest",
            objects,
        )
        add_assigned(
            add_box_obj(
                f"{label}_Warrior_Bracer_{side}_SpikedIron",
                p((18, sign * arm_side * 1.02, height * 0.47), 0),
                (64, 72, 60),
                iron,
            ),
            armature,
            f"lowerarm_{suffix}",
            objects,
        )
        add_spike_row(
            f"{label}_Warrior_Shoulder_{side}",
            armature,
            objects,
            iron,
            [
                p((6, sign * shoulder * 1.22, height * 0.815), 0),
                p((18, sign * shoulder * 1.04, height * 0.825), 0),
                p((-18, sign * shoulder * 1.02, height * 0.810), 0),
            ],
            "chest",
        )
        add_assigned(
            add_box_obj(
                f"{label}_Warrior_Knee_{side}_Iron",
                p((24, sign * hip_side * 1.30, height * 0.245), 0),
                (54, 56, 38),
                iron,
            ),
            armature,
            f"thigh_{suffix}",
            objects,
        )

    add_assigned(
        add_box_obj(f"{label}_Warrior_Chest_WarpaintSlash", p((58, 0, height * 0.67), 0), (12, 132, 26), paint),
        armature,
        "chest",
        objects,
    )
    add_assigned(
        add_box_obj(f"{label}_Warrior_Belt_IronDisk", p((58, 0, height * 0.49), 0), (56, 82, 62), iron),
        armature,
        "pelvis",
        objects,
    )
    add_assigned(
        add_ellipsoid_obj(f"{label}_Warrior_Belt_ForgeWindow", p((92, 0, height * 0.49), 0), (16, 22, 28), forge, 12, 6),
        armature,
        "pelvis",
        objects,
    )
    for index, y in enumerate((-58, -28, 0, 28, 58), 1):
        add_assigned(
            add_box_obj(
                f"{label}_Warrior_PlateSkirt_{index:02d}",
                p((48, y, height * 0.365), 0),
                (24, 22, 104),
                leather if index % 2 else iron,
            ),
            armature,
            "pelvis",
            objects,
        )

    # Left-side tower shield: the main melee-rival read.
    shield_y = arm_side * 1.36
    add_assigned(
        add_box_obj(f"{label}_Warrior_TowerShield_WoodCore", p((72, shield_y, height * 0.39), 0), (50, 42, 238), leather),
        armature,
        "hand_l",
        objects,
    )
    add_assigned(
        add_box_obj(f"{label}_Warrior_TowerShield_IronFrame", p((76, shield_y, height * 0.39), 0), (58, 50, 252), iron),
        armature,
        "hand_l",
        objects,
    )
    for z in (height * 0.24, height * 0.39, height * 0.54):
        add_assigned(
            add_box_obj(f"{label}_Warrior_TowerShield_CrossBand_{int(z)}", p((112, shield_y, z), 0), (18, 58, 22), brass),
            armature,
            "hand_l",
            objects,
        )
    add_assigned(
        add_ellipsoid_obj(f"{label}_Warrior_TowerShield_ForgeEye", p((118, shield_y, height * 0.46), 0), (12, 18, 26), forge, 12, 6),
        armature,
        "hand_l",
        objects,
    )
    add_assigned(
        add_ellipsoid_obj(f"{label}_Warrior_TowerShield_BoneTrophy", p((122, shield_y, height * 0.32), 0), (20, 12, 24), bone, 10, 5),
        armature,
        "hand_l",
        objects,
    )
    add_spike_row(
        f"{label}_Warrior_TowerShield",
        armature,
        objects,
        iron,
        [p((125, shield_y, height * 0.19), 0), p((126, shield_y, height * 0.61), 0), p((126, shield_y + 30, height * 0.40), 0)],
        "hand_l",
    )

    # Right-hand chained crusher hammer.
    hammer_y = -arm_side * 1.24
    add_assigned(
        add_cylinder_between(
            f"{label}_Warrior_Hammer_Handle_Leather",
            p((42, hammer_y, height * 0.31), 0),
            p((150, hammer_y - 12, height * 0.10), 0),
            9.0,
            leather,
            12,
        ),
        armature,
        "hand_r",
        objects,
    )
    add_assigned(
        add_box_obj(f"{label}_Warrior_Hammer_Head_IronBlock", p((164, hammer_y - 16, height * 0.105), 0), (118, 78, 84), iron),
        armature,
        "hand_r",
        objects,
    )
    add_assigned(
        add_box_obj(f"{label}_Warrior_Hammer_ForgeWindow", p((196, hammer_y - 16, height * 0.105), 0), (18, 50, 54), forge),
        armature,
        "hand_r",
        objects,
    )
    for offset in (-34, 0, 34):
        add_assigned(
            add_diamond_obj(f"{label}_Warrior_Hammer_BoneTooth_{offset}", p((124, hammer_y - 16 + offset, height * 0.155), 0), (12, 9, 18), bone),
            armature,
            "hand_r",
            objects,
        )
    add_assigned(
        add_cylinder_between(
            f"{label}_Warrior_Hammer_ChainHint",
            p((84, hammer_y + 18, height * 0.24), 0),
            p((150, hammer_y - 16, height * 0.145), 0),
            4.0,
            copper,
            8,
        ),
        armature,
        "hand_r",
        objects,
    )

    for socket_name, location, bone_name in [
        ("SOCKET_vfx_belt_forge", p((94, 0, height * 0.49), 0), "pelvis"),
        ("SOCKET_vfx_shield_core", p((122, shield_y, height * 0.46), 0), "hand_l"),
        ("SOCKET_vfx_hammer_core", p((198, hammer_y - 16, height * 0.105), 0), "hand_r"),
        ("SOCKET_head_fx", p((48, 0, height * 0.89), 0), "head"),
    ]:
        add_socket_empty(socket_name, location, armature, bone_name)


def build_warrior_variant() -> None:
    clear_scene()
    setup_scene()
    materials = create_materials(WARRIOR_MATERIALS)
    armature, objects = add_ogre_variant("Warrior", OGRE_BASE_MALE_ARMATURE_NAME, 330.0, 0.0, "male", materials)
    add_warrior_gear("Warrior", armature, objects, 330.0, materials)
    add_asset_metadata(
        "SK_OGR_Warrior_Rival_A01",
        "First-pass Ogre Warrior rivalry source over the Ogre male base; final sculpt, retopo, UVs, textures, skinning, and animation pending.",
        "/Game/Aerathea/Characters/Ogres/Warrior/SK_OGR_Warrior_Rival_A01",
    )
    export_path = EXPORT_ROOT / "Characters/Ogres/Warrior/SK_OGR_Warrior_Rival_A01/SK_OGR_Warrior_Rival_A01.fbx"
    export_skeletal_fbx(export_path, objects, armature, bake_anim=False)

    blend_path = BLENDER_ROOT / "Characters/Ogres/Warrior/SK_OGR_Warrior_Rival_A01/SK_OGR_Warrior_Rival_A01.blend"
    blend_path.parent.mkdir(parents=True, exist_ok=True)
    bpy.ops.wm.save_as_mainfile(filepath=str(blend_path))
    print(f"Built {blend_path.relative_to(ROOT)}")
    print(f"Exported {export_path.relative_to(ROOT)}")


def render_review() -> None:
    clear_scene()
    setup_scene()
    bpy.context.scene.view_settings.view_transform = "Standard"
    if bpy.context.scene.world is not None:
        bpy.context.scene.world.color = (0.68, 0.68, 0.64)

    materials = create_materials(WARRIOR_MATERIALS)
    make_review_materials_readable(materials)
    armature, objects = add_ogre_variant("Warrior", OGRE_BASE_MALE_ARMATURE_NAME, 330.0, 0.0, "male", materials)
    add_warrior_gear("Warrior", armature, objects, 330.0, materials)

    bpy.ops.object.light_add(type="SUN", location=(0, 0, 620), rotation=(math.radians(48), 0, math.radians(40)))
    bpy.context.object.data.energy = 1.45
    bpy.ops.object.light_add(type="AREA", location=(900, -220, 620))
    key = bpy.context.object
    key.name = "AET_WarriorReview_KeyLight"
    key.data.energy = 23000
    key.data.size = 780
    bpy.ops.object.light_add(type="AREA", location=(580, 420, 420))
    fill = bpy.context.object
    fill.name = "AET_WarriorReview_FillLight"
    fill.data.energy = 9000
    fill.data.size = 720

    bpy.ops.object.camera_add(location=(880, -720, 300))
    camera = bpy.context.object
    target = Vector((42, -8, 175))
    direction = target - Vector(camera.location)
    camera.rotation_euler = direction.to_track_quat("-Z", "Y").to_euler()
    camera.data.type = "ORTHO"
    camera.data.ortho_scale = 520
    camera.data.clip_start = 1
    camera.data.clip_end = 5000
    bpy.context.scene.camera = camera
    bpy.context.scene.render.resolution_x = 1400
    bpy.context.scene.render.resolution_y = 1400

    REVIEW_ROOT.mkdir(parents=True, exist_ok=True)
    output = REVIEW_ROOT / "SK_OGR_Warrior_Rival_A01_DCCReview.png"
    bpy.context.scene.render.filepath = str(output)
    bpy.ops.render.render(write_still=True)
    print(f"Rendered {output.relative_to(ROOT)}")


def main() -> None:
    build_warrior_variant()
    render_review()


if __name__ == "__main__":
    main()
