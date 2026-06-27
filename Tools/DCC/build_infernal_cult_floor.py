#!/usr/bin/env python3
"""Build the first Balgoroth cult floor DCC review source.

Run with:
    blender --background --python Tools/DCC/build_infernal_cult_floor.py

This creates a deterministic first-pass static mesh for
SM_INF_CullingTrialFloor_A01. It validates scale, symbols, pivots, material
slots, flat traversal collision, and Unreal import paths; it is not final
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
REVIEW_ROOT = ROOT / "Saved" / "Automation" / "InfernalCultFloorReview"

sys.path.insert(0, str(ROOT))

from Tools.DCC.build_next_slice_assets import (  # noqa: E402
    add_asset_metadata,
    clear_scene,
    mesh_to_blender,
    setup_scene,
)
from Tools.DCC.generate_first_slice_meshes import Mesh  # noqa: E402


ASSET_NAME = "SM_INF_CullingTrialFloor_A01"
REL_PATH = "Props/Infernals/BalgorothCult/SM_INF_CullingTrialFloor_A01"
UNREAL_PATH = "/Game/Aerathea/Props/Infernals/BalgorothCult/SM_INF_CullingTrialFloor_A01"


def materials(mesh: Mesh) -> dict[str, str]:
    return {
        "stone": mesh.material("M_INF_CultStone_Blockout_A01", (0.055, 0.060, 0.065)),
        "scorched": mesh.material("M_INF_ScorchedStone_Blockout_A01", (0.24, 0.060, 0.035)),
        "iron": mesh.material("M_INF_ObsidianIron_Blockout_A01", (0.018, 0.018, 0.022)),
        "glow": mesh.material("M_INF_RitualGlow_Blockout_A01", (1.0, 0.18, 0.025)),
    }


def sector_prism(
    mesh: Mesh,
    name: str,
    inner_radius: float,
    outer_radius: float,
    start_deg: float,
    end_deg: float,
    z_min: float,
    z_max: float,
    material: str,
    segments: int = 5,
) -> None:
    obj = mesh.add_object(name, material)
    top_inner: list[int] = []
    top_outer: list[int] = []
    bottom_inner: list[int] = []
    bottom_outer: list[int] = []

    for index in range(segments + 1):
        t = index / segments
        angle = math.radians(start_deg + (end_deg - start_deg) * t)
        ca = math.cos(angle)
        sa = math.sin(angle)
        bottom_inner.append(len(obj.verts) + 1)
        obj.verts.append((ca * inner_radius, sa * inner_radius, z_min))
        bottom_outer.append(len(obj.verts) + 1)
        obj.verts.append((ca * outer_radius, sa * outer_radius, z_min))
        top_inner.append(len(obj.verts) + 1)
        obj.verts.append((ca * inner_radius, sa * inner_radius, z_max))
        top_outer.append(len(obj.verts) + 1)
        obj.verts.append((ca * outer_radius, sa * outer_radius, z_max))

    for index in range(segments):
        obj.faces.append((top_inner[index], top_inner[index + 1], top_outer[index + 1], top_outer[index]))
        obj.faces.append((bottom_inner[index + 1], bottom_inner[index], bottom_outer[index], bottom_outer[index + 1]))
        obj.faces.append((bottom_outer[index], top_outer[index], top_outer[index + 1], bottom_outer[index + 1]))
        obj.faces.append((bottom_inner[index + 1], top_inner[index + 1], top_inner[index], bottom_inner[index]))

    obj.faces.append((bottom_inner[0], top_inner[0], top_outer[0], bottom_outer[0]))
    obj.faces.append((bottom_outer[-1], top_outer[-1], top_inner[-1], bottom_inner[-1]))


def oriented_box(
    mesh: Mesh,
    name: str,
    center: tuple[float, float, float],
    length: float,
    width: float,
    height: float,
    yaw_deg: float,
    material: str,
) -> None:
    cx, cy, cz = center
    half_l = length * 0.5
    half_w = width * 0.5
    half_h = height * 0.5
    angle = math.radians(yaw_deg)
    forward = (math.cos(angle), math.sin(angle))
    right = (-math.sin(angle), math.cos(angle))
    corners_2d = [
        (-half_l, -half_w),
        (half_l, -half_w),
        (half_l, half_w),
        (-half_l, half_w),
    ]

    obj = mesh.add_object(name, material)
    for z in (cz - half_h, cz + half_h):
        for local_x, local_y in corners_2d:
            obj.verts.append(
                (
                    cx + forward[0] * local_x + right[0] * local_y,
                    cy + forward[1] * local_x + right[1] * local_y,
                    z,
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


def triangle_prism(
    mesh: Mesh,
    name: str,
    points: tuple[tuple[float, float], tuple[float, float], tuple[float, float]],
    z_min: float,
    z_max: float,
    material: str,
) -> None:
    obj = mesh.add_object(name, material)
    for z in (z_min, z_max):
        for x, y in points:
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


def add_floor_mesh() -> Mesh:
    mesh = Mesh(ASSET_NAME)
    m = materials(mesh)

    # Broad modular slab language: 8 wedge modules, each about 45 degrees.
    for index in range(8):
        start = index * 45.0 + 2.0
        end = (index + 1) * 45.0 - 2.0
        mat = m["stone"] if index % 2 == 0 else m["scorched"]
        sector_prism(mesh, f"Wedge_{index + 1:02d}_BasaltSlab", 150.0, 420.0, start, end, 0.0, 20.0, mat)

    sector_prism(mesh, "CenterDisc_CultStone_HornCrownBase", 0.0, 148.0, 0.0, 360.0, 0.0, 24.0, m["stone"], 32)

    # Raised rim pieces are visual only; collision remains flat.
    for index in range(8):
        sector_prism(
            mesh,
            f"Rim_{index + 1:02d}_ObsidianIronRaised",
            422.0,
            455.0,
            index * 45.0 + 1.0,
            (index + 1) * 45.0 - 1.0,
            0.0,
            32.0,
            m["iron"],
            3,
        )

    # Broken emissive ritual ring, with an intentional rejected gap facing +X.
    ring_segments = [
        (25.0, 82.0),
        (92.0, 150.0),
        (160.0, 218.0),
        (228.0, 286.0),
        (296.0, 335.0),
    ]
    for index, (start, end) in enumerate(ring_segments, 1):
        sector_prism(mesh, f"RitualRing_{index:02d}_EmberChannel", 292.0, 310.0, start, end, 20.0, 24.0, m["glow"], 5)

    for angle in (0, 45, 90, 135, 180, 225, 270, 315):
        radius = 286.0
        center = (math.cos(math.radians(angle)) * radius * 0.5, math.sin(math.radians(angle)) * radius * 0.5, 23.0)
        oriented_box(mesh, f"RadialChannel_{angle:03d}_ScorchedInset", center, radius, 10.0, 5.0, angle, m["scorched"])

    # Horned crown and split-wing top sigil. These sit proud of the center disc
    # so they remain readable in the startup review camera.
    oriented_box(mesh, "Sigil_CenterSpine_ObsidianIron", (0.0, 0.0, 28.0), 150.0, 20.0, 7.0, 90.0, m["iron"])
    oriented_box(mesh, "Sigil_LeftWing_ObsidianIron", (-58.0, -16.0, 28.0), 132.0, 22.0, 7.0, 155.0, m["iron"])
    oriented_box(mesh, "Sigil_RightWing_ObsidianIron", (58.0, -16.0, 28.0), 132.0, 22.0, 7.0, 25.0, m["iron"])
    oriented_box(mesh, "Sigil_BrokenCircleGap_ScorchedEdge", (130.0, 0.0, 25.0), 68.0, 24.0, 6.0, 0.0, m["scorched"])

    for offset_x, tip_y, base_y, width in (
        (-82.0, 96.0, 38.0, 38.0),
        (-42.0, 118.0, 42.0, 34.0),
        (0.0, 140.0, 44.0, 40.0),
        (42.0, 118.0, 42.0, 34.0),
        (82.0, 96.0, 38.0, 38.0),
    ):
        triangle_prism(
            mesh,
            f"Sigil_HornPoint_{int(offset_x + 100):03d}_ObsidianIron",
            ((offset_x - width * 0.5, base_y), (offset_x + width * 0.5, base_y), (offset_x, tip_y)),
            24.0,
            31.0,
            m["iron"],
        )

    # Claw scoring: three broad readable grooves, not small scratches.
    for index, lateral in enumerate((-28.0, 0.0, 28.0), 1):
        oriented_box(
            mesh,
            f"ClawSlash_{index:02d}_EmberGroove",
            (-182.0, 270.0 + lateral, 24.0),
            142.0,
            14.0,
            5.0,
            112.0,
            m["glow"],
        )

    # Simple authored flat collision. The raised rim is left visual-only for
    # movement safety in first-pass review.
    sector_prism(mesh, f"UCX_{ASSET_NAME}_00", 0.0, 420.0, 0.0, 360.0, 16.0, 20.0, m["stone"], 24)
    return mesh


def make_materials_readable() -> None:
    for material in bpy.data.materials:
        if not material.name.startswith("M_INF_"):
            continue
        color = material.diffuse_color
        material.use_nodes = True
        bsdf = material.node_tree.nodes.get("Principled BSDF")
        if bsdf is None:
            continue
        bsdf.inputs["Base Color"].default_value = color
        bsdf.inputs["Roughness"].default_value = 0.86
        if "ObsidianIron" in material.name:
            bsdf.inputs["Metallic"].default_value = 0.45
            bsdf.inputs["Roughness"].default_value = 0.62
        if "RitualGlow" in material.name:
            bsdf.inputs["Emission Color"].default_value = (2.8, 0.20, 0.02, 1.0)
            bsdf.inputs["Emission Strength"].default_value = 1.8


def render_review() -> None:
    REVIEW_ROOT.mkdir(parents=True, exist_ok=True)
    scene = bpy.context.scene
    scene.render.resolution_x = 1800
    scene.render.resolution_y = 1300
    scene.eevee.taa_render_samples = 64

    bpy.ops.object.light_add(type="AREA", location=(0, -500, 620))
    key = bpy.context.object
    key.name = "Review_KeyLight"
    key.data.energy = 520
    key.data.size = 620

    bpy.ops.object.camera_add(location=(0, 0, 1100))
    camera = bpy.context.object
    scene.camera = camera
    camera.data.type = "ORTHO"
    camera.data.ortho_scale = 1300
    camera.data.clip_end = 3000
    direction = Vector((0.0, 0.0, 16.0)) - camera.location
    camera.rotation_euler = direction.to_track_quat("-Z", "Y").to_euler()

    scene.render.filepath = str(REVIEW_ROOT / f"{ASSET_NAME}_DCCReview.png")
    bpy.ops.render.render(write_still=True)


def build() -> None:
    clear_scene()
    setup_scene()
    mesh = add_floor_mesh()
    objects = mesh_to_blender(mesh)
    make_materials_readable()

    add_asset_metadata(
        ASSET_NAME,
        "First-pass Balgoroth cult floor DCC review source; final sculpt, UVs, textures, authored LODs, and gameplay collision tuning pending",
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
