#!/usr/bin/env python3
"""Build first-pass Balgoroth sigil DCC review source.

Run with:
    blender --background --python Tools/DCC/build_infernal_balgoroth_sigil.py

This creates deterministic first-pass DCC source and FBX export for
SM_INF_BalgorothSigil_A01. It validates broad symbol readability, scale,
material lanes, collision policy, and Unreal import paths; it is not final
sculpted or painted art.
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
REVIEW_ROOT = ROOT / "Saved" / "Automation" / "InfernalBalgorothSigilReview"

sys.path.insert(0, str(ROOT))

from Tools.DCC.build_next_slice_assets import (  # noqa: E402
    add_asset_metadata,
    clear_scene,
    mesh_to_blender,
    setup_scene,
)
from Tools.DCC.generate_first_slice_meshes import Mesh  # noqa: E402


ASSET_NAME = "SM_INF_BalgorothSigil_A01"
REL_PATH = "Props/Infernals/BalgorothCult/SM_INF_BalgorothSigil_A01"
UNREAL_PATH = "/Game/Aerathea/Props/Infernals/BalgorothCult/Sigils/SM_INF_BalgorothSigil_A01"


def materials(mesh: Mesh) -> dict[str, str]:
    return {
        "basalt": mesh.material("MI_INF_CultStone_Basalt_A01", (0.050, 0.055, 0.062)),
        "scorched": mesh.material("MI_INF_CultStone_ScorchedRed_A01", (0.210, 0.055, 0.036)),
        "obsidian": mesh.material("MI_INF_CultStone_ObsidianInset_A01", (0.014, 0.013, 0.018)),
        "glow": mesh.material("MI_INF_CultStone_EmissiveChannel_A01", (1.000, 0.250, 0.035)),
    }


def xz_triangle_prism(
    mesh: Mesh,
    name: str,
    points: tuple[tuple[float, float], tuple[float, float], tuple[float, float]],
    y_min: float,
    y_max: float,
    material: str,
) -> None:
    obj = mesh.add_object(name, material)
    for y in (y_min, y_max):
        for x, z in points:
            obj.verts.append((x, y, z))
    obj.faces.extend(
        [
            (1, 2, 3),
            (4, 6, 5),
            (1, 4, 5, 2),
            (2, 5, 6, 3),
            (3, 6, 4, 1),
        ]
    )


def xz_oriented_box(
    mesh: Mesh,
    name: str,
    center: tuple[float, float, float],
    length: float,
    thickness: float,
    depth: float,
    angle_deg: float,
    material: str,
) -> None:
    cx, cy, cz = center
    half_l = length * 0.5
    half_t = thickness * 0.5
    half_d = depth * 0.5
    angle = math.radians(angle_deg)
    forward = (math.cos(angle), math.sin(angle))
    right = (-math.sin(angle), math.cos(angle))
    corners_2d = [(-half_l, -half_t), (half_l, -half_t), (half_l, half_t), (-half_l, half_t)]

    obj = mesh.add_object(name, material)
    for y in (cy - half_d, cy + half_d):
        for local_x, local_z in corners_2d:
            obj.verts.append(
                (
                    cx + forward[0] * local_x + right[0] * local_z,
                    y,
                    cz + forward[1] * local_x + right[1] * local_z,
                )
            )
    obj.faces.extend(
        [
            (1, 2, 3, 4),
            (5, 8, 7, 6),
            (1, 5, 6, 2),
            (2, 6, 7, 3),
            (3, 7, 8, 4),
            (4, 8, 5, 1),
        ]
    )


def xz_sector_prism(
    mesh: Mesh,
    name: str,
    center: tuple[float, float],
    inner_radius: float,
    outer_radius: float,
    start_deg: float,
    end_deg: float,
    y_min: float,
    y_max: float,
    material: str,
    segments: int = 5,
) -> None:
    cx, cz = center
    obj = mesh.add_object(name, material)
    front_inner: list[int] = []
    front_outer: list[int] = []
    back_inner: list[int] = []
    back_outer: list[int] = []

    for index in range(segments + 1):
        t = index / segments
        angle = math.radians(start_deg + (end_deg - start_deg) * t)
        ca = math.cos(angle)
        sa = math.sin(angle)
        back_inner.append(len(obj.verts) + 1)
        obj.verts.append((cx + ca * inner_radius, y_min, cz + sa * inner_radius))
        back_outer.append(len(obj.verts) + 1)
        obj.verts.append((cx + ca * outer_radius, y_min, cz + sa * outer_radius))
        front_inner.append(len(obj.verts) + 1)
        obj.verts.append((cx + ca * inner_radius, y_max, cz + sa * inner_radius))
        front_outer.append(len(obj.verts) + 1)
        obj.verts.append((cx + ca * outer_radius, y_max, cz + sa * outer_radius))

    for index in range(segments):
        obj.faces.append((front_inner[index], front_inner[index + 1], front_outer[index + 1], front_outer[index]))
        obj.faces.append((back_inner[index + 1], back_inner[index], back_outer[index], back_outer[index + 1]))
        obj.faces.append((back_outer[index], front_outer[index], front_outer[index + 1], back_outer[index + 1]))
        obj.faces.append((back_inner[index + 1], front_inner[index + 1], front_inner[index], back_inner[index]))

    obj.faces.append((back_inner[0], front_inner[0], front_outer[0], back_outer[0]))
    obj.faces.append((back_outer[-1], front_outer[-1], front_inner[-1], back_inner[-1]))


def add_horned_crown(mesh: Mesh, m: dict[str, str]) -> None:
    mesh.add_box("Relief_Obsidian_CrownBrow", (0, -17, 218), (178, 18, 16), m["obsidian"])
    for index, (x, tip_z, width, base_z) in enumerate(
        ((-88, 258, 42, 220), (-44, 286, 36, 220), (0, 314, 44, 220), (44, 286, 36, 220), (88, 258, 42, 220)),
        1,
    ):
        xz_triangle_prism(
            mesh,
            f"Relief_Obsidian_HornedCrownPoint_{index:02d}",
            ((x - width * 0.5, base_z), (x + width * 0.5, base_z), (x, tip_z)),
            -25,
            -11,
            m["obsidian"],
        )
    mesh.add_box("Channel_Glow_CrownCore", (0, -28, 230), (94, 7, 8), m["glow"])


def add_split_wing(mesh: Mesh, m: dict[str, str]) -> None:
    wing_specs = [
        ("LeftUpper", -82, 180, -176, 140, -28),
        ("LeftLower", -62, 148, -152, 102, -18),
        ("RightUpper", 82, 180, 176, 140, 28),
        ("RightLower", 62, 148, 152, 102, 18),
    ]
    for name, root_x, root_z, tip_x, tip_z, rake in wing_specs:
        xz_triangle_prism(
            mesh,
            f"Relief_Obsidian_SplitWing_{name}",
            ((root_x, root_z + 22), (root_x + rake, root_z - 22), (tip_x, tip_z)),
            -23,
            -9,
            m["obsidian"],
        )
    mesh.add_box("Relief_Scorched_CenterBloodlineSplit", (0, -18, 152), (22, 15, 114), m["scorched"])


def add_eye_and_ring(mesh: Mesh, m: dict[str, str]) -> None:
    xz_sector_prism(mesh, "Ring_Glow_BrokenCircle_01", (0, 150), 70, 84, 18, 132, -30, -25, m["glow"], 6)
    xz_sector_prism(mesh, "Ring_Glow_BrokenCircle_02", (0, 150), 70, 84, 154, 286, -30, -25, m["glow"], 7)
    xz_sector_prism(mesh, "Ring_Glow_BrokenCircle_03", (0, 150), 70, 84, 304, 342, -30, -25, m["glow"], 3)
    xz_triangle_prism(mesh, "Relief_Obsidian_EyeLeft", ((-58, 150), (-12, 172), (-12, 128)), -31, -17, m["obsidian"])
    xz_triangle_prism(mesh, "Relief_Obsidian_EyeRight", ((58, 150), (12, 172), (12, 128)), -31, -17, m["obsidian"])
    mesh.add_diamond("Channel_Glow_EmberEyeCore", (0, -34, 150), (28, 7, 28), m["glow"])


def add_tail_crescent_and_claws(mesh: Mesh, m: dict[str, str]) -> None:
    xz_sector_prism(mesh, "Relief_Obsidian_HookedTailCrescent_A", (0, 98), 104, 128, 210, 336, -24, -10, m["obsidian"], 8)
    xz_triangle_prism(mesh, "Relief_Obsidian_TailHook", ((118, 52), (170, 48), (132, 8)), -24, -10, m["obsidian"])
    for index, (x, z, angle) in enumerate(((-82, 80, -58), (-30, 70, -66), (22, 60, -74)), 1):
        xz_oriented_box(mesh, f"ClawSlash_Glow_CullingMark_{index:02d}", (x, -31, z), 112, 14, 6, angle, m["glow"])


def add_sigil_mesh() -> Mesh:
    mesh = Mesh(ASSET_NAME)
    m = materials(mesh)

    mesh.add_box("WallRelief_Basalt_BackSlab", (0, 0, 150), (320, 24, 300), m["basalt"])
    mesh.add_box("WallRelief_Scorched_InnerInset", (0, -15, 148), (260, 10, 230), m["scorched"])
    mesh.add_box("WallRelief_Basalt_LowerNameplate_NoText", (0, -22, 26), (238, 12, 28), m["basalt"])

    add_horned_crown(mesh, m)
    add_split_wing(mesh, m)
    add_eye_and_ring(mesh, m)
    add_tail_crescent_and_claws(mesh, m)

    # Simple wall collision only. Symbol relief remains visual-only to avoid
    # movement snagging and to keep this reusable as dressing.
    mesh.add_box(f"UCX_{ASSET_NAME}_00", (0, 0, 150), (324, 28, 304), m["basalt"])
    return mesh


def make_materials_readable() -> None:
    for material in bpy.data.materials:
        if not material.name.startswith("MI_INF_CultStone_"):
            continue
        color = material.diffuse_color
        material.use_nodes = True
        bsdf = material.node_tree.nodes.get("Principled BSDF")
        if bsdf is None:
            continue
        bsdf.inputs["Base Color"].default_value = color
        bsdf.inputs["Roughness"].default_value = 0.82
        if "ObsidianInset" in material.name:
            bsdf.inputs["Metallic"].default_value = 0.05
            bsdf.inputs["Roughness"].default_value = 0.42
        if "EmissiveChannel" in material.name:
            bsdf.inputs["Emission Color"].default_value = (1.0, 0.25, 0.035, 1.0)
            bsdf.inputs["Emission Strength"].default_value = 1.25


def hide_collision_for_review(objects: list[bpy.types.Object]) -> None:
    for obj in objects:
        if obj.name.startswith("UCX_"):
            obj.hide_render = True
            obj.display_type = "WIRE"


def review_material(name: str, color: tuple[float, float, float, float]) -> bpy.types.Material:
    material = bpy.data.materials.get(name) or bpy.data.materials.new(name)
    material.diffuse_color = color
    return material


def add_marker_box(name: str, location: tuple[float, float, float], scale: tuple[float, float, float], material: bpy.types.Material) -> None:
    bpy.ops.mesh.primitive_cube_add(size=1.0, location=location)
    obj = bpy.context.object
    obj.name = name
    obj.dimensions = scale
    bpy.ops.object.transform_apply(location=False, rotation=False, scale=True)
    obj.data.materials.append(material)


def add_scale_marker(name: str, height: float, x: float, material: bpy.types.Material) -> None:
    add_marker_box(f"Review_{name}_Post", (x, -88, height * 0.5), (8, 8, height), material)
    add_marker_box(f"Review_{name}_Cap", (x, -88, height), (32, 8, 6), material)


def add_label(text: str, location: tuple[float, float, float], size: float = 12.0) -> None:
    bpy.ops.object.text_add(location=location, rotation=(math.radians(76), 0, 0))
    obj = bpy.context.object
    obj.name = "Review_Label_" + text.replace(" ", "_")
    obj.data.body = text
    obj.data.align_x = "CENTER"
    obj.data.align_y = "CENTER"
    obj.data.size = size
    obj.data.materials.append(review_material("M_REVIEW_Label_Dark", (0.02, 0.02, 0.02, 1.0)))


def render_review() -> None:
    REVIEW_ROOT.mkdir(parents=True, exist_ok=True)
    scene = bpy.context.scene
    scene.render.resolution_x = 1700
    scene.render.resolution_y = 1200
    try:
        scene.eevee.taa_render_samples = 64
    except Exception:
        pass
    if scene.world is not None:
        scene.world.color = (0.55, 0.54, 0.50)

    marker_material = review_material("M_REVIEW_Scale_Marker", (0.82, 0.78, 0.64, 1.0))
    add_scale_marker("Human_180cm", 180, 220, marker_material)
    add_scale_marker("Infernal_274cm", 274, 265, marker_material)
    add_label("180 cm", (220, -76, 196), 12)
    add_label("274 cm", (265, -76, 290), 12)

    bpy.ops.object.light_add(type="SUN", location=(0, 620, 900), rotation=(math.radians(48), 0, math.radians(-28)))
    sun = bpy.context.object
    sun.name = "AET_BalgorothSigilReview_Sun"
    sun.data.energy = 0.85

    bpy.ops.object.light_add(type="AREA", location=(0, -580, 410))
    key = bpy.context.object
    key.name = "AET_BalgorothSigilReview_KeyLight"
    key.data.energy = 760
    key.data.size = 600

    bpy.ops.object.camera_add(location=(220, -780, 260))
    camera = bpy.context.object
    target = Vector((0.0, -18.0, 150.0))
    direction = target - Vector(camera.location)
    camera.rotation_euler = direction.to_track_quat("-Z", "Y").to_euler()
    camera.data.type = "ORTHO"
    camera.data.ortho_scale = 540
    camera.data.clip_start = 1
    camera.data.clip_end = 5000
    scene.camera = camera

    scene.render.filepath = str(REVIEW_ROOT / f"{ASSET_NAME}_DCCReview.png")
    bpy.ops.render.render(write_still=True)


def build() -> None:
    clear_scene()
    setup_scene()
    mesh = add_sigil_mesh()
    objects = mesh_to_blender(mesh)
    hide_collision_for_review(objects)
    make_materials_readable()

    add_asset_metadata(
        ASSET_NAME,
        "First-pass Balgoroth sigil DCC review source; final sculpt, UVs, authored textures, tuned LOD meshes, and Unreal sockets pending.",
        UNREAL_PATH,
    )

    blend_path = BLENDER_ROOT / REL_PATH / f"{ASSET_NAME}.blend"
    export_path = EXPORT_ROOT / REL_PATH / f"{ASSET_NAME}.fbx"
    blend_path.parent.mkdir(parents=True, exist_ok=True)
    export_path.parent.mkdir(parents=True, exist_ok=True)

    render_review()
    bpy.ops.wm.save_as_mainfile(filepath=str(blend_path))

    bpy.ops.object.select_all(action="DESELECT")
    for obj in objects:
        obj.select_set(True)
    if objects:
        bpy.context.view_layer.objects.active = objects[0]

    bpy.ops.export_scene.fbx(
        filepath=str(export_path),
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
    print(f"Built {blend_path.relative_to(ROOT)}")
    print(f"Exported {export_path.relative_to(ROOT)}")
    print(f"Rendered {REVIEW_ROOT.relative_to(ROOT)}/{ASSET_NAME}_DCCReview.png")


if __name__ == "__main__":
    build()
