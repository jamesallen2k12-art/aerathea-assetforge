#!/usr/bin/env python3
"""Build first-pass Aerathea Infernal DCC review sources.

Run with:
    blender --background --python Tools/DCC/build_infernal_base.py

This creates deterministic review meshes for lifecycle stage scale, adult
scale, horns, wings, tail, claws, sockets, and export paths. It is not final
sculpted or painted production art.
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
REVIEW_ROOT = ROOT / "Saved" / "Automation" / "InfernalBaseReview"

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


INF_MATERIALS = {
    "M_INF_Skin_Blockout_A01": (0.62, 0.12, 0.08),
    "M_INF_HornClaw_Blockout_A01": (0.025, 0.020, 0.018),
    "M_INF_Wing_Blockout_A01": (0.16, 0.055, 0.045),
    "M_INF_Wrap_Blockout_A01": (0.10, 0.075, 0.055),
    "M_INF_BrandGlow_Blockout_A01": (1.0, 0.22, 0.03),
    "M_INF_ElderAsh_Blockout_A01": (0.40, 0.12, 0.10),
    "M_AET_ScaleMarker_Blockout_A01": (0.12, 0.12, 0.11),
    "M_AET_ScaleMarker_Humanoid_A01": (0.34, 0.38, 0.42),
}


LESSER_VARIANTS = [
    {
        "name": "SK_INF_Lesser_Spawn_A01",
        "label": "Spawn",
        "height": 80.0,
        "folder": "Characters/Infernals/SK_INF_Lesser_A01",
        "unreal": "/Game/Aerathea/Characters/Infernals/Lesser/SK_INF_Lesser_Spawn_A01",
        "stage": "spawn",
    },
    {
        "name": "SK_INF_Lesser_1stKill_A01",
        "label": "1st Kill",
        "height": 115.0,
        "folder": "Characters/Infernals/SK_INF_Lesser_A01",
        "unreal": "/Game/Aerathea/Characters/Infernals/Lesser/SK_INF_Lesser_1stKill_A01",
        "stage": "first_kill",
    },
    {
        "name": "SK_INF_Lesser_Blooded_A01",
        "label": "Blooded",
        "height": 150.0,
        "folder": "Characters/Infernals/SK_INF_Lesser_A01",
        "unreal": "/Game/Aerathea/Characters/Infernals/Lesser/SK_INF_Lesser_Blooded_A01",
        "stage": "blooded",
    },
    {
        "name": "SK_INF_Lesser_Elder_A01",
        "label": "Elder",
        "height": 220.0,
        "folder": "Characters/Infernals/SK_INF_Lesser_A01",
        "unreal": "/Game/Aerathea/Characters/Infernals/Lesser/SK_INF_Lesser_Elder_A01",
        "stage": "elder",
    },
    {
        "name": "SK_INF_Lesser_Ancient_A01",
        "label": "Ancient",
        "height": 250.0,
        "folder": "Characters/Infernals/SK_INF_Lesser_A01",
        "unreal": "/Game/Aerathea/Characters/Infernals/Lesser/SK_INF_Lesser_Ancient_A01",
        "stage": "ancient",
    },
]


ADULT_VARIANTS = [
    {
        "name": "SK_INF_Base_Compact_A01",
        "label": "Compact Adult",
        "height": 165.0,
        "folder": "Characters/Infernals/SK_INF_Base_A01",
        "unreal": "/Game/Aerathea/Characters/Infernals/Base/SK_INF_Base_Compact_A01",
        "stage": "compact",
    },
    {
        "name": "SK_INF_Base_Tall_A01",
        "label": "Tall Adult",
        "height": 245.0,
        "folder": "Characters/Infernals/SK_INF_Base_A01",
        "unreal": "/Game/Aerathea/Characters/Infernals/Base/SK_INF_Base_Tall_A01",
        "stage": "tall",
    },
]


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
            bsdf.inputs["Emission Color"].default_value = (color[0] * 0.25, color[1] * 0.18, color[2] * 0.16, 1.0)
        if "Emission Strength" in bsdf.inputs:
            bsdf.inputs["Emission Strength"].default_value = 0.18
        if "Glow" in material.name and "Emission Color" in bsdf.inputs:
            bsdf.inputs["Emission Color"].default_value = color
        if "Glow" in material.name and "Emission Strength" in bsdf.inputs:
            bsdf.inputs["Emission Strength"].default_value = 1.4


def p(point: tuple[float, float, float], offset_y: float) -> tuple[float, float, float]:
    return (point[0], point[1] + offset_y, point[2])


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
    return obj


def make_bones(height: float, offset_y: float) -> list[tuple[str, tuple[float, float, float], tuple[float, float, float], str | None]]:
    shoulder = height * 0.115
    hip = height * 0.055

    def pp(point: tuple[float, float, float]) -> tuple[float, float, float]:
        return p(point, offset_y)

    return [
        ("root", pp((0, 0, 0)), pp((0, 0, max(8.0, height * 0.07))), None),
        ("pelvis", pp((0, 0, height * 0.44)), pp((0, 0, height * 0.54)), "root"),
        ("spine_01", pp((0, 0, height * 0.54)), pp((0, 0, height * 0.67)), "pelvis"),
        ("chest", pp((0, 0, height * 0.67)), pp((0, 0, height * 0.79)), "spine_01"),
        ("neck", pp((0, 0, height * 0.79)), pp((0, 0, height * 0.84)), "chest"),
        ("head", pp((0, 0, height * 0.84)), pp((0, 0, height * 0.96)), "neck"),
        ("tail_01", pp((-8, 0, height * 0.43)), pp((-height * 0.17, 0, height * 0.34)), "pelvis"),
        ("tail_02", pp((-height * 0.17, 0, height * 0.34)), pp((-height * 0.34, 0, height * 0.22)), "tail_01"),
        ("wing_l", pp((-8, shoulder * 0.72, height * 0.73)), pp((-height * 0.15, shoulder * 1.42, height * 0.60)), "chest"),
        ("wing_r", pp((-8, -shoulder * 0.72, height * 0.73)), pp((-height * 0.15, -shoulder * 1.42, height * 0.60)), "chest"),
        ("upperarm_l", pp((0, shoulder, height * 0.73)), pp((height * 0.05, shoulder * 1.45, height * 0.56)), "chest"),
        ("lowerarm_l", pp((height * 0.05, shoulder * 1.45, height * 0.56)), pp((height * 0.08, shoulder * 1.55, height * 0.37)), "upperarm_l"),
        ("hand_l", pp((height * 0.08, shoulder * 1.55, height * 0.37)), pp((height * 0.18, shoulder * 1.55, height * 0.32)), "lowerarm_l"),
        ("upperarm_r", pp((0, -shoulder, height * 0.73)), pp((height * 0.05, -shoulder * 1.45, height * 0.56)), "chest"),
        ("lowerarm_r", pp((height * 0.05, -shoulder * 1.45, height * 0.56)), pp((height * 0.08, -shoulder * 1.55, height * 0.37)), "upperarm_r"),
        ("hand_r", pp((height * 0.08, -shoulder * 1.55, height * 0.37)), pp((height * 0.18, -shoulder * 1.55, height * 0.32)), "lowerarm_r"),
        ("thigh_l", pp((0, hip, height * 0.44)), pp((height * 0.04, hip * 1.2, height * 0.24)), "pelvis"),
        ("calf_l", pp((height * 0.04, hip * 1.2, height * 0.24)), pp((height * 0.07, hip * 1.15, height * 0.055)), "thigh_l"),
        ("foot_l", pp((height * 0.07, hip * 1.15, height * 0.055)), pp((height * 0.20, hip * 1.15, 4)), "calf_l"),
        ("thigh_r", pp((0, -hip, height * 0.44)), pp((height * 0.04, -hip * 1.2, height * 0.24)), "pelvis"),
        ("calf_r", pp((height * 0.04, -hip * 1.2, height * 0.24)), pp((height * 0.07, -hip * 1.15, height * 0.055)), "thigh_r"),
        ("foot_r", pp((height * 0.07, -hip * 1.15, height * 0.055)), pp((height * 0.20, -hip * 1.15, 4)), "calf_r"),
    ]


def add_assigned(obj: bpy.types.Object, armature: bpy.types.Object, bone: str, objects: list[bpy.types.Object]) -> None:
    assign_to_bone(obj, armature, bone)
    objects.append(obj)


def stage_params(stage: str) -> dict[str, float]:
    params = {
        "spawn": {"horn": 0.035, "wing": 0.14, "tail": 0.24, "claw": 0.025, "mass": 0.78, "ancient": 0.0},
        "first_kill": {"horn": 0.050, "wing": 0.22, "tail": 0.32, "claw": 0.034, "mass": 0.86, "ancient": 0.0},
        "blooded": {"horn": 0.065, "wing": 0.34, "tail": 0.42, "claw": 0.040, "mass": 0.94, "ancient": 0.0},
        "elder": {"horn": 0.090, "wing": 0.50, "tail": 0.52, "claw": 0.045, "mass": 1.0, "ancient": 0.0},
        "ancient": {"horn": 0.115, "wing": 0.52, "tail": 0.54, "claw": 0.048, "mass": 1.04, "ancient": 1.0},
        "compact": {"horn": 0.075, "wing": 0.42, "tail": 0.46, "claw": 0.040, "mass": 0.92, "ancient": 0.0},
        "tall": {"horn": 0.100, "wing": 0.54, "tail": 0.56, "claw": 0.048, "mass": 1.05, "ancient": 0.0},
    }
    return params[stage]


def add_infernal_variant(
    name: str,
    label: str,
    height: float,
    stage: str,
    offset_y: float,
    materials: dict[str, bpy.types.Material],
) -> tuple[bpy.types.Object, list[bpy.types.Object]]:
    armature = create_armature(f"SKEL_{name}", make_bones(height, offset_y))
    objects: list[bpy.types.Object] = []
    params = stage_params(stage)

    skin = materials["M_INF_ElderAsh_Blockout_A01"] if stage == "ancient" else materials["M_INF_Skin_Blockout_A01"]
    horn = materials["M_INF_HornClaw_Blockout_A01"]
    wing = materials["M_INF_Wing_Blockout_A01"]
    wrap = materials["M_INF_Wrap_Blockout_A01"]
    glow = materials["M_INF_BrandGlow_Blockout_A01"]

    shoulder = height * 0.115 * params["mass"]
    hip = height * 0.056 * params["mass"]
    wing_span = height * params["wing"]
    tail_len = height * params["tail"]

    def pp(point: tuple[float, float, float]) -> tuple[float, float, float]:
        return p(point, offset_y)

    # Main body.
    add_assigned(add_ellipsoid_obj(f"{label}_Pelvis", pp((0, 0, height * 0.45)), (height * 0.055, hip, height * 0.050), skin, 14, 7), armature, "pelvis", objects)
    add_assigned(add_ellipsoid_obj(f"{label}_Torso", pp((height * 0.02, 0, height * 0.62)), (height * 0.073, shoulder * 0.78, height * 0.105), skin, 16, 8), armature, "spine_01", objects)
    add_assigned(add_ellipsoid_obj(f"{label}_Chest", pp((height * 0.02, 0, height * 0.72)), (height * 0.080, shoulder, height * 0.075), skin, 16, 8), armature, "chest", objects)
    add_assigned(add_cylinder_between(f"{label}_Neck", pp((height * 0.02, 0, height * 0.78)), pp((height * 0.03, 0, height * 0.84)), height * 0.018, skin, 10), armature, "neck", objects)
    add_assigned(add_ellipsoid_obj(f"{label}_Head", pp((height * 0.045, 0, height * 0.90)), (height * 0.038, height * 0.034, height * 0.052), skin, 14, 7), armature, "head", objects)
    add_assigned(add_box_obj(f"{label}_Brow", pp((height * 0.067, 0, height * 0.915)), (height * 0.040, height * 0.062, height * 0.012), skin), armature, "head", objects)
    add_assigned(add_box_obj(f"{label}_Jaw", pp((height * 0.073, 0, height * 0.875)), (height * 0.038, height * 0.050, height * 0.024), skin), armature, "head", objects)

    # Horns.
    horn_radius = max(1.4, height * params["horn"] * 0.18)
    for side, sign, suffix in (("L", 1, "l"), ("R", -1, "r")):
        add_assigned(
            add_cone_between(
                f"{label}_Horn_{side}",
                pp((height * 0.030, sign * height * 0.025, height * 0.945)),
                pp((-height * 0.025, sign * height * params["horn"], height * (1.0 + params["horn"] * 0.55))),
                horn_radius,
                max(0.35, horn_radius * 0.22),
                horn,
                12,
            ),
            armature,
            "head",
            objects,
        )

    # Arms, hands, claws.
    for side, sign, suffix in (("L", 1, "l"), ("R", -1, "r")):
        add_assigned(add_cylinder_between(f"{label}_UpperArm_{side}", pp((0, sign * shoulder, height * 0.72)), pp((height * 0.05, sign * shoulder * 1.45, height * 0.56)), height * 0.018, skin, 10), armature, f"upperarm_{suffix}", objects)
        add_assigned(add_cylinder_between(f"{label}_LowerArm_{side}", pp((height * 0.05, sign * shoulder * 1.45, height * 0.56)), pp((height * 0.08, sign * shoulder * 1.55, height * 0.37)), height * 0.016, skin, 10), armature, f"lowerarm_{suffix}", objects)
        add_assigned(add_ellipsoid_obj(f"{label}_Hand_{side}", pp((height * 0.13, sign * shoulder * 1.56, height * 0.335)), (height * 0.030, height * 0.018, height * 0.022), skin, 10, 5), armature, f"hand_{suffix}", objects)
        claw_len = height * params["claw"]
        for index, spread in enumerate((-0.014, 0.0, 0.014), 1):
            add_assigned(
                add_cone_between(
                    f"{label}_Claw_{side}_{index}",
                    pp((height * 0.158, sign * (shoulder * 1.56 + height * spread), height * 0.335)),
                    pp((height * 0.158 + claw_len, sign * (shoulder * 1.56 + height * spread), height * 0.328)),
                    max(0.45, height * 0.004),
                    0.0,
                    horn,
                    8,
                ),
                armature,
                f"hand_{suffix}",
                objects,
            )

    # Legs and feet.
    for side, sign, suffix in (("L", 1, "l"), ("R", -1, "r")):
        add_assigned(add_cylinder_between(f"{label}_Thigh_{side}", pp((0, sign * hip, height * 0.43)), pp((height * 0.04, sign * hip * 1.2, height * 0.24)), height * 0.023, skin, 10), armature, f"thigh_{suffix}", objects)
        add_assigned(add_cylinder_between(f"{label}_Calf_{side}", pp((height * 0.04, sign * hip * 1.2, height * 0.24)), pp((height * 0.07, sign * hip * 1.15, height * 0.055)), height * 0.018, skin, 10), armature, f"calf_{suffix}", objects)
        add_assigned(add_ellipsoid_obj(f"{label}_Foot_{side}", pp((height * 0.15, sign * hip * 1.15, height * 0.030)), (height * 0.055, height * 0.020, height * 0.018), skin, 10, 5), armature, f"foot_{suffix}", objects)

    # Tail.
    add_assigned(add_cylinder_between(f"{label}_Tail_Base", pp((-height * 0.03, 0, height * 0.42)), pp((-tail_len * 0.52, 0, height * 0.31)), height * 0.020, skin, 10), armature, "tail_01", objects)
    add_assigned(add_cone_between(f"{label}_Tail_Taper", pp((-tail_len * 0.52, 0, height * 0.31)), pp((-tail_len, 0, height * 0.20)), height * 0.018, max(0.8, height * 0.006), skin, 10), armature, "tail_02", objects)

    # Folded wings and leading fingers.
    for side, sign, suffix in (("L", 1, "l"), ("R", -1, "r")):
        root = pp((-height * 0.02, sign * shoulder * 0.70, height * 0.72))
        tip = pp((-wing_span, sign * (shoulder * 1.35 + wing_span * 0.30), height * 0.48))
        add_assigned(add_cylinder_between(f"{label}_Wing_{side}_Finger", root, tip, max(1.0, height * 0.008), horn, 8), armature, f"wing_{suffix}", objects)
        add_assigned(add_ellipsoid_obj(f"{label}_Wing_{side}_FoldedMembrane", pp((-wing_span * 0.48, sign * (shoulder * 1.0 + wing_span * 0.16), height * 0.58)), (max(3.0, wing_span * 0.42), max(2.0, wing_span * 0.08), max(4.0, height * 0.10)), wing, 10, 5), armature, f"wing_{suffix}", objects)

    # Wraps, brand, and age marks.
    add_assigned(add_box_obj(f"{label}_RitualWrap_Waist", pp((height * 0.018, 0, height * 0.49)), (height * 0.045, shoulder * 1.55, height * 0.025), wrap), armature, "pelvis", objects)
    add_assigned(add_ellipsoid_obj(f"{label}_BrandGlow_Chest", pp((height * 0.075, 0, height * 0.67)), (height * 0.011, height * 0.013, height * 0.016), glow, 8, 4), armature, "chest", objects)
    if stage == "ancient":
        for mark_index, y in enumerate((-0.025, 0.025), 1):
            add_assigned(add_box_obj(f"{label}_AncientScar_{mark_index}", pp((height * 0.083, height * y, height * 0.71)), (height * 0.009, height * 0.005, height * 0.13), glow), armature, "chest", objects)

    for socket_name, location, bone_name in [
        ("SOCKET_vfx_eye_l", pp((height * 0.077, height * 0.012, height * 0.915)), "head"),
        ("SOCKET_vfx_eye_r", pp((height * 0.077, -height * 0.012, height * 0.915)), "head"),
        ("SOCKET_vfx_brand_chest", pp((height * 0.082, 0, height * 0.67)), "chest"),
        ("SOCKET_vfx_mouth", pp((height * 0.086, 0, height * 0.875)), "head"),
        ("SOCKET_vfx_regen_core", pp((height * 0.05, 0, height * 0.58)), "spine_01"),
        ("SOCKET_claw_l", pp((height * 0.18, shoulder * 1.56, height * 0.33)), "hand_l"),
        ("SOCKET_claw_r", pp((height * 0.18, -shoulder * 1.56, height * 0.33)), "hand_r"),
        ("SOCKET_tail_tip", pp((-tail_len, 0, height * 0.20)), "tail_02"),
        ("SOCKET_wing_l_tip", pp((-wing_span, shoulder * 1.35 + wing_span * 0.30 + offset_y, height * 0.48)), "wing_l"),
        ("SOCKET_wing_r_tip", pp((-wing_span, -shoulder * 1.35 - wing_span * 0.30 + offset_y, height * 0.48)), "wing_r"),
    ]:
        add_socket_empty(socket_name, location, armature, bone_name)

    return armature, objects


def export_variant(variant: dict[str, object]) -> None:
    clear_scene()
    setup_scene()
    materials = create_materials(INF_MATERIALS)
    armature, objects = add_infernal_variant(
        variant["name"],
        variant["label"],
        float(variant["height"]),
        variant["stage"],
        0.0,
        materials,
    )
    add_asset_metadata(
        variant["name"],
        "First-pass Infernal DCC review source; final sculpt, skinning, physics, LODs, and textures pending",
        variant["unreal"],
    )
    export_path = EXPORT_ROOT / f"{variant['folder']}/{variant['name']}.fbx"
    export_skeletal_fbx(export_path, objects, armature, bake_anim=False)
    print(f"Exported {export_path.relative_to(ROOT)}")


def add_scale_marker(name: str, height: float, y: float, material: bpy.types.Material) -> None:
    add_ellipsoid_obj(f"{name}_Head", (0, y, height - 10), (7, 7, 10), material, 10, 5)
    add_cylinder_between(f"{name}_Body", (0, y, height - 25), (0, y, height * 0.42), max(3.0, height * 0.030), material, 10)
    add_cylinder_between(f"{name}_LegL", (0, y + height * 0.030, height * 0.42), (5, y + height * 0.040, 3), max(1.6, height * 0.014), material, 8)
    add_cylinder_between(f"{name}_LegR", (0, y - height * 0.030, height * 0.42), (5, y - height * 0.040, 3), max(1.6, height * 0.014), material, 8)


def add_label(text: str, location: tuple[float, float, float], size: float = 13.0) -> None:
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
        bpy.context.scene.world.color = (0.54, 0.52, 0.50)

    materials = create_materials(INF_MATERIALS)
    make_review_materials_readable(materials)

    offsets = [-320.0, -220.0, -105.0, 35.0, 190.0, 335.0, 480.0]
    all_variants = LESSER_VARIANTS + ADULT_VARIANTS
    for variant, offset in zip(all_variants, offsets):
        add_infernal_variant(
            variant["name"].replace("SK_INF_", ""),
            variant["label"],
            float(variant["height"]),
            variant["stage"],
            offset,
            materials,
        )
        add_label(f"{variant['label']} {int(variant['height'])}cm", (0, offset, 14.0), 12.0)

    add_scale_marker("Scale_Humanoid_180cm", 180.0, -430.0, materials["M_AET_ScaleMarker_Humanoid_A01"])
    add_label("Humanoid 180cm", (0, -430.0, 14.0), 12.0)
    add_scale_marker("Scale_MaxAdult_274cm", 274.0, 595.0, materials["M_AET_ScaleMarker_Blockout_A01"])
    add_label("Max Adult 274cm", (0, 595.0, 14.0), 12.0)

    add_asset_metadata(
        "SK_INF_Base_A01_and_SK_INF_Lesser_A01",
        "Infernal first-pass DCC review scene with lifecycle stages and adult scale targets",
        "/Game/Aerathea/Characters/Infernals/",
    )

    bpy.ops.object.light_add(type="SUN", location=(0, 0, 500), rotation=(math.radians(48), 0, math.radians(35)))
    sun = bpy.context.object
    sun.name = "AET_InfernalReview_SunFill"
    sun.data.energy = 1.45

    bpy.ops.object.light_add(type="AREA", location=(760, -260, 450))
    key = bpy.context.object
    key.name = "AET_InfernalReview_KeyLight"
    key.data.energy = 10500
    key.data.size = 700
    bpy.ops.object.light_add(type="AREA", location=(620, 360, 330))
    fill = bpy.context.object
    fill.name = "AET_InfernalReview_FillLight"
    fill.data.energy = 4300
    fill.data.size = 700

    bpy.ops.object.camera_add(location=(760, -760, 265))
    camera = bpy.context.object
    target = Vector((4, 80, 132))
    direction = target - Vector(camera.location)
    camera.rotation_euler = direction.to_track_quat("-Z", "Y").to_euler()
    camera.data.type = "ORTHO"
    camera.data.ortho_scale = 900
    camera.data.clip_start = 1
    camera.data.clip_end = 4000
    bpy.context.scene.camera = camera
    bpy.context.scene.render.resolution_x = 1900
    bpy.context.scene.render.resolution_y = 1200

    for blend_path in [
        BLENDER_ROOT / "Characters/Infernals/SK_INF_Base_A01/SK_INF_Base_A01.blend",
        BLENDER_ROOT / "Characters/Infernals/SK_INF_Lesser_A01/SK_INF_Lesser_A01.blend",
    ]:
        blend_path.parent.mkdir(parents=True, exist_ok=True)
        bpy.ops.wm.save_as_mainfile(filepath=str(blend_path))
        print(f"Built {blend_path.relative_to(ROOT)}")

    REVIEW_ROOT.mkdir(parents=True, exist_ok=True)
    output = REVIEW_ROOT / "SK_INF_Lifecycle_A01_DCCReview.png"
    bpy.context.scene.render.filepath = str(output)
    bpy.ops.render.render(write_still=True)
    print(f"Rendered {output.relative_to(ROOT)}")


def main() -> None:
    for variant in LESSER_VARIANTS + ADULT_VARIANTS:
        export_variant(variant)
    render_review()


if __name__ == "__main__":
    main()
