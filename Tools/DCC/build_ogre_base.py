#!/usr/bin/env python3
"""Build the first-pass Aerathea Ogre base DCC review source.

Run with:
    blender --background --python Tools/DCC/build_ogre_base.py

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
REVIEW_ROOT = ROOT / "Saved" / "Automation" / "OgreBaseReview"

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


OGRE_MATERIALS = {
    "M_OGR_Skin_Blockout_A01": (0.48, 0.40, 0.31),
    "M_OGR_Warpaint_Blockout_A01": (0.24, 0.10, 0.06),
    "M_OGR_Leather_Blockout_A01": (0.20, 0.11, 0.07),
    "M_OGR_Iron_Blockout_A01": (0.12, 0.12, 0.11),
    "M_OGR_Brass_Blockout_A01": (0.64, 0.36, 0.16),
    "M_OGR_Bone_Blockout_A01": (0.66, 0.58, 0.43),
    "M_OGR_AetheriumGlow_Blockout_A01": (0.0, 0.55, 1.0),
    "M_OGR_NecroGlow_Blockout_A01": (0.16, 0.95, 0.28),
    "M_AET_ScaleMarker_Blockout_A01": (0.11, 0.11, 0.10),
    "M_AET_ScaleMarker_Anubisath_A01": (0.05, 0.05, 0.07),
    "M_AET_ScaleMarker_Giant_A01": (0.45, 0.56, 0.64),
}


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
            bsdf.inputs["Emission Color"].default_value = (color[0] * 0.35, color[1] * 0.35, color[2] * 0.35, 1.0)
        if "Emission Strength" in bsdf.inputs:
            bsdf.inputs["Emission Strength"].default_value = 0.28
        if "Glow" in material.name and "Emission Color" in bsdf.inputs:
            bsdf.inputs["Emission Color"].default_value = color
        if "Glow" in material.name and "Emission Strength" in bsdf.inputs:
            bsdf.inputs["Emission Strength"].default_value = 1.2


def p(point: tuple[float, float, float], offset_y: float) -> tuple[float, float, float]:
    return (point[0], point[1] + offset_y, point[2])


def make_bones(height: float, offset_y: float) -> list[tuple[str, tuple[float, float, float], tuple[float, float, float], str | None]]:
    shoulder = height * 0.175
    arm_side = height * 0.235
    hip_side = height * 0.085

    def pp(point: tuple[float, float, float]) -> tuple[float, float, float]:
        return p(point, offset_y)

    return [
        ("root", pp((0, 0, 0)), pp((0, 0, 18)), None),
        ("pelvis", pp((0, 0, height * 0.44)), pp((0, 0, height * 0.53)), "root"),
        ("spine_01", pp((0, 0, height * 0.53)), pp((0, 0, height * 0.67)), "pelvis"),
        ("chest", pp((0, 0, height * 0.67)), pp((0, 0, height * 0.80)), "spine_01"),
        ("neck", pp((0, 0, height * 0.80)), pp((0, 0, height * 0.85)), "chest"),
        ("head", pp((0, 0, height * 0.85)), pp((0, 0, height * 0.97)), "neck"),
        ("clavicle_l", pp((0, shoulder * 0.50, height * 0.76)), pp((0, shoulder, height * 0.75)), "chest"),
        ("upperarm_l", pp((0, shoulder, height * 0.75)), pp((8, arm_side, height * 0.57)), "clavicle_l"),
        ("lowerarm_l", pp((8, arm_side, height * 0.57)), pp((16, arm_side * 1.08, height * 0.37)), "upperarm_l"),
        ("hand_l", pp((16, arm_side * 1.08, height * 0.37)), pp((34, arm_side * 1.08, height * 0.30)), "lowerarm_l"),
        ("clavicle_r", pp((0, -shoulder * 0.50, height * 0.76)), pp((0, -shoulder, height * 0.75)), "chest"),
        ("upperarm_r", pp((0, -shoulder, height * 0.75)), pp((8, -arm_side, height * 0.57)), "clavicle_r"),
        ("lowerarm_r", pp((8, -arm_side, height * 0.57)), pp((16, -arm_side * 1.08, height * 0.37)), "upperarm_r"),
        ("hand_r", pp((16, -arm_side * 1.08, height * 0.37)), pp((34, -arm_side * 1.08, height * 0.30)), "lowerarm_r"),
        ("thigh_l", pp((0, hip_side, height * 0.44)), pp((12, hip_side * 1.28, height * 0.23)), "pelvis"),
        ("calf_l", pp((12, hip_side * 1.28, height * 0.23)), pp((24, hip_side * 1.22, height * 0.055)), "thigh_l"),
        ("foot_l", pp((24, hip_side * 1.22, height * 0.055)), pp((58, hip_side * 1.22, 5)), "calf_l"),
        ("thigh_r", pp((0, -hip_side, height * 0.44)), pp((12, -hip_side * 1.28, height * 0.23)), "pelvis"),
        ("calf_r", pp((12, -hip_side * 1.28, height * 0.23)), pp((24, -hip_side * 1.22, height * 0.055)), "thigh_r"),
        ("foot_r", pp((24, -hip_side * 1.22, height * 0.055)), pp((58, -hip_side * 1.22, 5)), "calf_r"),
    ]


def add_assigned(obj: bpy.types.Object, armature: bpy.types.Object, bone: str, objects: list[bpy.types.Object]) -> None:
    assign_to_bone(obj, armature, bone)
    objects.append(obj)


def add_ogre_variant(
    label: str,
    armature_name: str,
    height: float,
    offset_y: float,
    sex: str,
    materials: dict[str, bpy.types.Material],
) -> tuple[bpy.types.Object, list[bpy.types.Object]]:
    bones = make_bones(height, offset_y)
    armature = create_armature(armature_name, bones)
    objects: list[bpy.types.Object] = []

    skin = materials["M_OGR_Skin_Blockout_A01"]
    paint = materials["M_OGR_Warpaint_Blockout_A01"]
    leather = materials["M_OGR_Leather_Blockout_A01"]
    iron = materials["M_OGR_Iron_Blockout_A01"]
    brass = materials["M_OGR_Brass_Blockout_A01"]
    bone = materials["M_OGR_Bone_Blockout_A01"]
    aetherium = materials["M_OGR_AetheriumGlow_Blockout_A01"]
    necro = materials["M_OGR_NecroGlow_Blockout_A01"]

    sex_scale = 1.0 if sex == "male" else 0.92
    shoulder = height * (0.185 if sex == "male" else 0.165)
    arm_side = height * 0.235
    hip_side = height * (0.092 if sex == "male" else 0.098)

    def pp(point: tuple[float, float, float]) -> tuple[float, float, float]:
        return p(point, offset_y)

    body_parts = [
        (add_ellipsoid_obj(f"{label}_Body_Pelvis", pp((0, 0, height * 0.45)), (height * 0.080, hip_side * 1.25, height * 0.055), leather, 18, 8), "pelvis"),
        (add_ellipsoid_obj(f"{label}_Body_Belly", pp((0, 0, height * 0.58)), (height * 0.105, shoulder * 0.75, height * 0.105), skin, 20, 10), "spine_01"),
        (add_ellipsoid_obj(f"{label}_Body_Chest", pp((0, 0, height * 0.70)), (height * 0.125, shoulder, height * 0.095), skin, 20, 10), "chest"),
        (add_cylinder_between(f"{label}_Neck_Thick", pp((4, 0, height * 0.78)), pp((6, 0, height * 0.84)), height * 0.032, skin, 12), "neck"),
        (add_ellipsoid_obj(f"{label}_Head_HeavyJaw", pp((12, 0, height * 0.90)), (height * 0.055, height * 0.050, height * 0.065), skin, 18, 8), "head"),
        (add_box_obj(f"{label}_Jaw_Slab", pp((28, 0, height * 0.875)), (height * 0.052, height * 0.075, height * 0.035), skin), "head"),
        (add_box_obj(f"{label}_Brow_Plate", pp((18, 0, height * 0.925)), (height * 0.052, height * 0.090, height * 0.018), skin), "head"),
        (add_box_obj(f"{label}_Belt_IronWide", pp((22, 0, height * 0.49)), (height * 0.040, shoulder * 1.36, height * 0.035), iron), "pelvis"),
        (add_box_obj(f"{label}_Belt_BrassBuckle", pp((44, 0, height * 0.49)), (height * 0.035, height * 0.075, height * 0.048), brass), "pelvis"),
        (add_box_obj(f"{label}_Starter_WrapFront", pp((34, 0, height * 0.35)), (height * 0.035, shoulder * 0.70, height * 0.18), leather), "pelvis"),
        (add_box_obj(f"{label}_Starter_WrapBack", pp((-24, 0, height * 0.36)), (height * 0.030, shoulder * 0.65, height * 0.16), leather), "pelvis"),
        (add_box_obj(f"{label}_Chest_StrapsCross", pp((28, 0, height * 0.66)), (height * 0.026, shoulder * 1.04, height * 0.030), leather), "chest"),
        (add_ellipsoid_obj(f"{label}_Chest_AetheriumSocketPreview", pp((48, 0, height * 0.66)), (height * 0.016, height * 0.018, height * 0.020), aetherium, 10, 5), "chest"),
    ]
    if sex == "female":
        body_parts.append(
            (add_ellipsoid_obj(f"{label}_Hair_Mass", pp((-16, 0, height * 0.90)), (height * 0.040, height * 0.060, height * 0.090), leather, 12, 6), "head")
        )
    else:
        body_parts.append(
            (add_box_obj(f"{label}_Back_TekPackSocketBlock", pp((-38, 0, height * 0.64)), (height * 0.035, height * 0.12, height * 0.12), iron), "chest")
        )

    for obj, bone_name in body_parts:
        add_assigned(obj, armature, bone_name, objects)

    for side, sign, suffix in (("Left", 1, "l"), ("Right", -1, "r")):
        add_assigned(
            add_cylinder_between(
                f"{label}_Arm_{side}_Upper",
                pp((0, sign * shoulder, height * 0.735)),
                pp((8, sign * arm_side, height * 0.57)),
                height * 0.039 * sex_scale,
                skin,
                14,
            ),
            armature,
            f"upperarm_{suffix}",
            objects,
        )
        add_assigned(
            add_cylinder_between(
                f"{label}_Arm_{side}_Lower",
                pp((8, sign * arm_side, height * 0.57)),
                pp((16, sign * arm_side * 1.08, height * 0.37)),
                height * 0.035 * sex_scale,
                skin,
                14,
            ),
            armature,
            f"lowerarm_{suffix}",
            objects,
        )
        add_assigned(
            add_ellipsoid_obj(
                f"{label}_Hand_{side}_SlabPalm",
                pp((34, sign * arm_side * 1.10, height * 0.315)),
                (height * 0.052, height * 0.034, height * 0.044),
                skin,
                14,
                7,
            ),
            armature,
            f"hand_{suffix}",
            objects,
        )
        add_assigned(
            add_box_obj(
                f"{label}_Bracer_{side}_Iron",
                pp((12, sign * arm_side * 0.99, height * 0.46)),
                (height * 0.050, height * 0.065, height * 0.048),
                iron,
            ),
            armature,
            f"lowerarm_{suffix}",
            objects,
        )
        add_assigned(
            add_box_obj(
                f"{label}_Warpaint_{side}_UpperArm",
                pp((4, sign * shoulder * 1.10, height * 0.66)),
                (height * 0.016, height * 0.070, height * 0.024),
                paint,
            ),
            armature,
            f"upperarm_{suffix}",
            objects,
        )
        for index, y_offset in enumerate((-12, -4, 4, 12), 1):
            add_assigned(
                add_cylinder_between(
                    f"{label}_Hand_{side}_Finger_{index}",
                    pp((42, sign * (arm_side * 1.10 + y_offset), height * 0.315)),
                    pp((70, sign * (arm_side * 1.11 + y_offset), height * 0.295)),
                    height * 0.010,
                    skin,
                    8,
                ),
                armature,
                f"hand_{suffix}",
                objects,
            )
        add_assigned(
            add_cylinder_between(
                f"{label}_Hand_{side}_Thumb",
                pp((32, sign * arm_side * 1.08, height * 0.330)),
                pp((60, sign * (arm_side * 1.22), height * 0.340)),
                height * 0.012,
                skin,
                8,
            ),
            armature,
            f"hand_{suffix}",
            objects,
        )

        add_assigned(
            add_cylinder_between(
                f"{label}_Leg_{side}_Upper",
                pp((0, sign * hip_side, height * 0.44)),
                pp((12, sign * hip_side * 1.28, height * 0.23)),
                height * 0.048 * sex_scale,
                skin,
                14,
            ),
            armature,
            f"thigh_{suffix}",
            objects,
        )
        add_assigned(
            add_cylinder_between(
                f"{label}_Leg_{side}_Lower",
                pp((12, sign * hip_side * 1.28, height * 0.23)),
                pp((24, sign * hip_side * 1.22, height * 0.055)),
                height * 0.040 * sex_scale,
                skin,
                14,
            ),
            armature,
            f"calf_{suffix}",
            objects,
        )
        add_assigned(
            add_box_obj(
                f"{label}_Foot_{side}_Wrapped",
                pp((56, sign * hip_side * 1.22, height * 0.030)),
                (height * 0.145, height * 0.080, height * 0.045),
                leather,
            ),
            armature,
            f"foot_{suffix}",
            objects,
        )
        add_assigned(
            add_box_obj(
                f"{label}_KneePlate_{side}_Iron",
                pp((18, sign * hip_side * 1.28, height * 0.245)),
                (height * 0.036, height * 0.060, height * 0.038),
                iron,
            ),
            armature,
            f"thigh_{suffix}",
            objects,
        )

    for socket_name, location, bone_name in [
        ("SOCKET_hand_r_weapon", pp((40, -arm_side * 1.18, height * 0.32)), "hand_r"),
        ("SOCKET_hand_l_offhand", pp((40, arm_side * 1.18, height * 0.32)), "hand_l"),
        ("SOCKET_hand_r_twohand_grip", pp((52, -arm_side * 1.11, height * 0.37)), "hand_r"),
        ("SOCKET_hand_l_twohand_grip", pp((52, arm_side * 1.11, height * 0.37)), "hand_l"),
        ("SOCKET_back_large_weapon", pp((-48, -24, height * 0.67)), "chest"),
        ("SOCKET_back_shield", pp((-52, 24, height * 0.64)), "chest"),
        ("SOCKET_spine_teknomancy_pack", pp((-46, 0, height * 0.64)), "chest"),
        ("SOCKET_shoulder_l_large", pp((0, shoulder * 1.10, height * 0.76)), "chest"),
        ("SOCKET_shoulder_r_large", pp((0, -shoulder * 1.10, height * 0.76)), "chest"),
        ("SOCKET_belt_front", pp((46, 0, height * 0.49)), "pelvis"),
        ("SOCKET_belt_back", pp((-34, 0, height * 0.49)), "pelvis"),
        ("SOCKET_vfx_mouth", pp((48, 0, height * 0.88)), "head"),
        ("SOCKET_vfx_eye_l", pp((34, 8, height * 0.915)), "head"),
        ("SOCKET_vfx_eye_r", pp((34, -8, height * 0.915)), "head"),
        ("SOCKET_vfx_chest_core", pp((52, 0, height * 0.66)), "chest"),
        ("SOCKET_vfx_stomp_ground", pp((64, 0, 4)), "root"),
    ]:
        add_socket_empty(socket_name, location, armature, bone_name)

    if sex == "male":
        add_assigned(add_box_obj(f"{label}_Bone_TrophyBack", pp((-58, 0, height * 0.76)), (height * 0.025, height * 0.055, height * 0.14), bone), armature, "chest", objects)
    else:
        add_assigned(add_ellipsoid_obj(f"{label}_NecroCharm_Preview", pp((44, 0, height * 0.50)), (height * 0.016, height * 0.016, height * 0.020), necro, 10, 5), armature, "pelvis", objects)

    return armature, objects


def export_variant(name: str, label: str, height_cm: float, sex: str) -> None:
    clear_scene()
    setup_scene()
    materials = create_materials(OGRE_MATERIALS)
    armature, objects = add_ogre_variant(label, f"SKEL_{name}", height_cm, 0.0, sex, materials)
    add_asset_metadata(
        name,
        f"First-pass DCC review Ogre {sex} body source; final sculpt, skinning, physics, LODs, and textures pending",
        f"/Game/Aerathea/Characters/Ogres/Base/{name}",
    )
    export_path = EXPORT_ROOT / f"Characters/Ogres/SK_OGR_Base_A01/{name}.fbx"
    export_skeletal_fbx(export_path, objects, armature, bake_anim=False)
    print(f"Exported {export_path.relative_to(ROOT)}")


def add_scale_marker(name: str, height: float, y: float, material: bpy.types.Material) -> None:
    add_ellipsoid_obj(f"{name}_Head", (0, y, height - 11), (8, 8, 11), material, 10, 5)
    add_cylinder_between(f"{name}_Body", (0, y, height - 28), (0, y, height * 0.42), max(4.0, height * 0.035), material, 10)
    add_cylinder_between(f"{name}_LegL", (0, y + height * 0.030, height * 0.42), (5, y + height * 0.040, 3), max(2.0, height * 0.018), material, 8)
    add_cylinder_between(f"{name}_LegR", (0, y - height * 0.030, height * 0.42), (5, y - height * 0.040, 3), max(2.0, height * 0.018), material, 8)


def add_label(text: str, location: tuple[float, float, float], size: float = 18.0) -> None:
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
    bpy.context.scene.view_settings.exposure = 0.0
    bpy.context.scene.view_settings.gamma = 1.0
    if bpy.context.scene.world is not None:
        bpy.context.scene.world.color = (0.60, 0.60, 0.58)

    materials = create_materials(OGRE_MATERIALS)
    make_review_materials_readable(materials)
    add_scale_marker("Scale_Minotaur_Male_274cm", 274.0, -235.0, materials["M_AET_ScaleMarker_Blockout_A01"])
    add_scale_marker("Scale_Anubisath_Male_254cm", 254.0, -130.0, materials["M_AET_ScaleMarker_Anubisath_A01"])
    add_ogre_variant("Female", "SKEL_OGR_Base_Female_A01", 315.0, 0.0, "female", materials)
    add_ogre_variant("Male", "SKEL_OGR_Base_Male_A01", 330.0, 135.0, "male", materials)
    add_scale_marker("Scale_Giant_Male_470cm", 470.0, 300.0, materials["M_AET_ScaleMarker_Giant_A01"])

    add_label("Minotaur M 9ft", (0, -235.0, 20.0), 18.0)
    add_label("Anubisath M 8ft4", (0, -130.0, 20.0), 18.0)
    add_label("Ogre F 10ft6", (0, 0.0, 20.0), 18.0)
    add_label("Ogre M 11ft", (0, 135.0, 20.0), 18.0)
    add_label("Giant M 15ft8", (0, 300.0, 20.0), 18.0)

    add_asset_metadata(
        "SK_OGR_Base_A01",
        "Approved Ogre base first-pass DCC review scene with male/female baselines and scale markers",
        "/Game/Aerathea/Characters/Ogres/Base/",
    )

    bpy.ops.object.light_add(type="SUN", location=(0, 0, 620), rotation=(math.radians(48), 0, math.radians(40)))
    sun = bpy.context.object
    sun.name = "AET_OgreReview_SunFill"
    sun.data.energy = 1.6

    bpy.ops.object.light_add(type="AREA", location=(900, -160, 620))
    key = bpy.context.object
    key.name = "AET_OgreReview_KeyLight"
    key.data.energy = 14000
    key.data.size = 760
    bpy.ops.object.light_add(type="AREA", location=(760, 310, 420))
    fill = bpy.context.object
    fill.name = "AET_OgreReview_FillLight"
    fill.data.energy = 5200
    fill.data.size = 760

    bpy.ops.object.camera_add(location=(980, -620, 315))
    camera = bpy.context.object
    target = Vector((18, 78, 235))
    direction = target - Vector(camera.location)
    camera.rotation_euler = direction.to_track_quat("-Z", "Y").to_euler()
    camera.data.type = "ORTHO"
    camera.data.ortho_scale = 760
    camera.data.clip_start = 1
    camera.data.clip_end = 5000
    bpy.context.scene.camera = camera
    bpy.context.scene.render.resolution_x = 1800
    bpy.context.scene.render.resolution_y = 1200

    blend_path = BLENDER_ROOT / "Characters/Ogres/SK_OGR_Base_A01/SK_OGR_Base_A01.blend"
    blend_path.parent.mkdir(parents=True, exist_ok=True)
    bpy.ops.wm.save_as_mainfile(filepath=str(blend_path))
    print(f"Built {blend_path.relative_to(ROOT)}")

    REVIEW_ROOT.mkdir(parents=True, exist_ok=True)
    output = REVIEW_ROOT / "SK_OGR_Base_A01_DCCReview.png"
    bpy.context.scene.render.filepath = str(output)
    bpy.ops.render.render(write_still=True)
    print(f"Rendered {output.relative_to(ROOT)}")


def main() -> None:
    export_variant("SK_OGR_Base_Male_A01", "Male", 330.0, "male")
    export_variant("SK_OGR_Base_Female_A01", "Female", 315.0, "female")
    render_review()


if __name__ == "__main__":
    main()
