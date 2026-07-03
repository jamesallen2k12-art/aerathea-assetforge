#!/usr/bin/env python3
"""Build Blood Axe cairn slab cluster A1 proof-of-concept DCC source.

Run with:
    blender --background --python Tools/DCC/build_bloodaxe_cairn_slab_cluster_poc.py

This creates a deterministic Blender source, FBX export, LOD source collections,
UCX collision proxy source, and proof render for
SM_GIA_BloodAxeCairnSlabCluster_A01. It is a proof-of-concept review target
based on candidate board A1, not approved final canon or final painted art.
"""

from __future__ import annotations

import math
import shutil
import sys
from array import array
from pathlib import Path

import bpy
from mathutils import Vector


ROOT = Path(__file__).resolve().parents[2]
SOURCE_ROOT = ROOT / "SourceAssets"
BLENDER_ROOT = SOURCE_ROOT / "Blender"
EXPORT_ROOT = SOURCE_ROOT / "Exports"
TEXTURE_ROOT = SOURCE_ROOT / "Textures"
ARMORPAINT_ROOT = SOURCE_ROOT / "ArmorPaint"
REVIEW_ROOT = ROOT / "Saved" / "Automation" / "DCC" / "SM_GIA_BloodAxeCairnSlabCluster_A01"
REFERENCE_IMAGE = ROOT / "docs/assets/visual_canon/VC_GIA_BloodAxe_CairnStones_A01_A1_Crop.png"
REVIEW_RENDER = REVIEW_ROOT / "SM_GIA_BloodAxeCairnSlabCluster_A01_DCCReview.png"
PAINTED_REVIEW_RENDER = REVIEW_ROOT / "SM_GIA_BloodAxeCairnSlabCluster_A01_PaintedDCCReview.png"
GAME_READY_REVIEW_RENDER = REVIEW_ROOT / "SM_GIA_BloodAxeCairnSlabCluster_A01_GameReadyReview.png"
PAINTED_APPROVAL_RENDER = REVIEW_ROOT / "SM_GIA_BloodAxeCairnSlabCluster_A01_PaintedApprovalReview.png"

sys.path.insert(0, str(ROOT))

from Tools.DCC.build_next_slice_assets import add_asset_metadata, clear_scene, setup_scene  # noqa: E402


ASSET_NAME = "SM_GIA_BloodAxeCairnSlabCluster_A01"
REL_PATH = "Props/Giants/BloodAxe/Cairns/SM_GIA_BloodAxeCairnSlabCluster_A01"
UNREAL_PATH = "/Game/Aerathea/Props/Giants/BloodAxe/Cairns/SM_GIA_BloodAxeCairnSlabCluster_A01"
TEXTURE_REL_PATH = "Props/Giants/BloodAxe/Cairns/SM_GIA_BloodAxeCairnSlabCluster_A01"

GIANT_FEMALE_BASELINE_CM = 442.0
GIANT_MALE_BASELINE_CM = 470.0


def make_collection(name: str, hidden: bool = False) -> bpy.types.Collection:
    collection = bpy.data.collections.new(name)
    bpy.context.scene.collection.children.link(collection)
    collection.hide_render = hidden
    collection.hide_viewport = hidden
    return collection


def move_to_collection(obj: bpy.types.Object, collection: bpy.types.Collection) -> None:
    for current in list(obj.users_collection):
        current.objects.unlink(obj)
    collection.objects.link(obj)


def set_active(obj: bpy.types.Object) -> None:
    bpy.ops.object.select_all(action="DESELECT")
    bpy.context.view_layer.objects.active = obj
    obj.select_set(True)


def color_shift(color: tuple[float, float, float, float], amount: float) -> tuple[float, float, float, float]:
    return (
        max(0.0, min(1.0, color[0] + amount)),
        max(0.0, min(1.0, color[1] + amount)),
        max(0.0, min(1.0, color[2] + amount)),
        color[3],
    )


def make_material(
    name: str,
    color: tuple[float, float, float, float],
    roughness: float = 0.9,
    noise_strength: float = 0.0,
    bump_strength: float = 0.0,
    bump_distance: float = 2.0,
) -> bpy.types.Material:
    material = bpy.data.materials.get(name)
    if material is None:
        material = bpy.data.materials.new(name)
    material.diffuse_color = color
    material.use_nodes = True
    nodes = material.node_tree.nodes
    bsdf = nodes.get("Principled BSDF")
    if bsdf is not None:
        bsdf.inputs["Base Color"].default_value = color
        bsdf.inputs["Roughness"].default_value = roughness
        bsdf.inputs["Metallic"].default_value = 0.0
        if noise_strength:
            noise = nodes.new(type="ShaderNodeTexNoise")
            noise.inputs["Scale"].default_value = 23.0
            noise.inputs["Detail"].default_value = 8.0
            noise.inputs["Roughness"].default_value = 0.58
            ramp = nodes.new(type="ShaderNodeValToRGB")
            ramp.color_ramp.elements[0].position = 0.24
            ramp.color_ramp.elements[0].color = color_shift(color, -noise_strength)
            ramp.color_ramp.elements[1].position = 1.0
            ramp.color_ramp.elements[1].color = color_shift(color, noise_strength)
            material.node_tree.links.new(noise.outputs["Fac"], ramp.inputs["Fac"])
            material.node_tree.links.new(ramp.outputs["Color"], bsdf.inputs["Base Color"])
            if bump_strength:
                bump = nodes.new(type="ShaderNodeBump")
                bump.inputs["Strength"].default_value = bump_strength
                bump.inputs["Distance"].default_value = bump_distance
                material.node_tree.links.new(noise.outputs["Fac"], bump.inputs["Height"])
                material.node_tree.links.new(bump.outputs["Normal"], bsdf.inputs["Normal"])
    return material


def make_image_material(name: str, image_path: Path) -> bpy.types.Material:
    material = bpy.data.materials.new(name)
    material.diffuse_color = (1.0, 1.0, 1.0, 1.0)
    material.use_nodes = True
    nodes = material.node_tree.nodes
    bsdf = nodes.get("Principled BSDF")
    if bsdf is None:
        return material
    texture = nodes.new(type="ShaderNodeTexImage")
    texture.image = bpy.data.images.load(str(image_path))
    material.node_tree.links.new(texture.outputs["Color"], bsdf.inputs["Base Color"])
    bsdf.inputs["Roughness"].default_value = 0.72
    return material


def make_vertex_color_material(name: str) -> bpy.types.Material:
    material = bpy.data.materials.get(name)
    if material is None:
        material = bpy.data.materials.new(name)
    material.diffuse_color = (0.22, 0.20, 0.17, 1.0)
    material.use_nodes = True
    nodes = material.node_tree.nodes
    bsdf = nodes.get("Principled BSDF")
    if bsdf is not None:
        attribute = nodes.new(type="ShaderNodeAttribute")
        attribute.attribute_name = "AET_VertexColor"
        material.node_tree.links.new(attribute.outputs["Color"], bsdf.inputs["Base Color"])
        noise = nodes.new(type="ShaderNodeTexNoise")
        noise.inputs["Scale"].default_value = 32.0
        noise.inputs["Detail"].default_value = 7.0
        noise.inputs["Roughness"].default_value = 0.62
        bump = nodes.new(type="ShaderNodeBump")
        bump.inputs["Strength"].default_value = 0.055
        bump.inputs["Distance"].default_value = 3.0
        material.node_tree.links.new(noise.outputs["Fac"], bump.inputs["Height"])
        material.node_tree.links.new(bump.outputs["Normal"], bsdf.inputs["Normal"])
        bsdf.inputs["Roughness"].default_value = 0.86
        bsdf.inputs["Metallic"].default_value = 0.0
    return material


def create_materials() -> dict[str, bpy.types.Material]:
    return {
        "stone_dark": make_material("M_GIA_BloodAxeCairnSlabCluster_StoneDark_A01", (0.058, 0.057, 0.052, 1.0), noise_strength=0.065, bump_strength=0.08, bump_distance=5.0),
        "stone_mid": make_material("M_GIA_BloodAxeCairnSlabCluster_StoneMid_A01", (0.088, 0.083, 0.072, 1.0), noise_strength=0.065, bump_strength=0.07, bump_distance=4.0),
        "stone_worn": make_material("M_GIA_BloodAxeCairnSlabCluster_StoneWorn_A01", (0.145, 0.128, 0.103, 1.0), noise_strength=0.055, bump_strength=0.055, bump_distance=3.0),
        "stone_edge": make_material("M_GIA_BloodAxeCairnSlabCluster_StoneEdgePaint_A01", (0.245, 0.218, 0.165, 1.0), noise_strength=0.035),
        "stone_cold_highlight": make_material("M_GIA_BloodAxeCairnSlabCluster_CoolStoneHighlight_A01", (0.125, 0.122, 0.108, 1.0), noise_strength=0.025),
        "stone_warm_highlight": make_material("M_GIA_BloodAxeCairnSlabCluster_WarmStonePaint_A01", (0.205, 0.178, 0.128, 1.0), noise_strength=0.03),
        "stone_shadow_paint": make_material("M_GIA_BloodAxeCairnSlabCluster_StoneShadowPaint_A01", (0.035, 0.034, 0.031, 1.0), noise_strength=0.012),
        "ash": make_material("M_GIA_BloodAxeCairnSlabCluster_AshMud_A01", (0.082, 0.077, 0.069, 1.0), noise_strength=0.04, bump_strength=0.035, bump_distance=2.0),
        "ash_light": make_material("M_GIA_BloodAxeCairnSlabCluster_AshLightPaint_A01", (0.22, 0.20, 0.17, 1.0), noise_strength=0.035),
        "mud": make_material("M_GIA_BloodAxeCairnSlabCluster_DarkMud_A01", (0.075, 0.052, 0.038, 1.0), noise_strength=0.035, bump_strength=0.03, bump_distance=1.5),
        "mud_wet": make_material("M_GIA_BloodAxeCairnSlabCluster_WetMudPaint_A01", (0.12, 0.075, 0.045, 1.0), noise_strength=0.025),
        "paint": make_material("M_GIA_BloodAxeCairnSlabCluster_OxideRedPaint_A01", (0.30, 0.026, 0.017, 1.0), noise_strength=0.055),
        "paint_dark": make_material("M_GIA_BloodAxeCairnSlabCluster_DriedBloodRedPaint_A01", (0.105, 0.010, 0.007, 1.0), noise_strength=0.02),
        "paint_chip": make_material("M_GIA_BloodAxeCairnSlabCluster_RedPaintChipBreak_A01", (0.078, 0.070, 0.055, 1.0), noise_strength=0.025),
        "rawhide": make_material("M_GIA_BloodAxeCairnSlabCluster_Rawhide_A01", (0.135, 0.078, 0.036, 1.0), noise_strength=0.035, bump_strength=0.025, bump_distance=1.2),
        "rawhide_light": make_material("M_GIA_BloodAxeCairnSlabCluster_RawhideWornEdge_A01", (0.22, 0.135, 0.065, 1.0), noise_strength=0.02),
        "rawhide_shadow": make_material("M_GIA_BloodAxeCairnSlabCluster_RawhideShadow_A01", (0.052, 0.032, 0.018, 1.0), noise_strength=0.012),
        "scar": make_material("M_GIA_BloodAxeCairnSlabCluster_DarkCrack_A01", (0.035, 0.032, 0.03, 1.0), noise_strength=0.01),
        "game_vertex": make_vertex_color_material("M_GIA_BloodAxeCairnSlabCluster_VertexPaint_A01"),
        "collision": make_material("M_AET_CollisionProxy_ReviewOnly_A01", (0.1, 0.42, 0.95, 0.22)),
        "marker": make_material("M_AET_ReviewMarker_Tan_A01", (0.78, 0.72, 0.58, 1.0)),
        "label": make_material("M_AET_ReviewLabel_Tan_A01", (0.86, 0.82, 0.70, 1.0)),
    }


def roughen_mesh(obj: bpy.types.Object, strength: float) -> None:
    for index, vertex in enumerate(obj.data.vertices):
        sx = -1.0 if index % 2 else 1.0
        sy = -1.0 if index % 3 else 1.0
        sz = -1.0 if index % 5 else 1.0
        vertex.co.x += sx * strength * (0.4 + (index % 4) * 0.12)
        vertex.co.y += sy * strength * (0.3 + (index % 5) * 0.09)
        vertex.co.z += sz * strength * (0.2 + (index % 3) * 0.08)


def smart_uv(obj: bpy.types.Object) -> None:
    set_active(obj)
    try:
        bpy.ops.object.mode_set(mode="EDIT")
        bpy.ops.mesh.select_all(action="SELECT")
        bpy.ops.uv.smart_project(angle_limit=math.radians(66), island_margin=0.025)
    finally:
        bpy.ops.object.mode_set(mode="OBJECT")


def add_slab(
    name: str,
    location: tuple[float, float, float],
    dimensions: tuple[float, float, float],
    rotation: tuple[float, float, float],
    material: bpy.types.Material,
    collection: bpy.types.Collection,
    roughness: float = 5.0,
    bevel: float = 2.5,
) -> bpy.types.Object:
    bpy.ops.mesh.primitive_cube_add(size=1.0, location=location, rotation=rotation)
    obj = bpy.context.object
    obj.name = name
    obj.dimensions = dimensions
    obj.data.materials.append(material)
    set_active(obj)
    bpy.ops.object.transform_apply(location=False, rotation=False, scale=True)
    roughen_mesh(obj, roughness)
    if bevel > 0:
        modifier = obj.modifiers.new("AET_BroadStoneBevel", "BEVEL")
        modifier.width = bevel
        modifier.segments = 1
        modifier.affect = "EDGES"
        set_active(obj)
        bpy.ops.object.modifier_apply(modifier=modifier.name)
    smart_uv(obj)
    move_to_collection(obj, collection)
    return obj


def add_faceted_slab(
    name: str,
    location: tuple[float, float, float],
    dimensions: tuple[float, float, float],
    rotation: tuple[float, float, float],
    material: bpy.types.Material,
    collection: bpy.types.Collection,
    bevel: float = 2.0,
    top_material: bpy.types.Material | None = None,
    side_variation_material: bpy.types.Material | None = None,
) -> bpy.types.Object:
    width, depth, height = dimensions
    outline = [
        (-0.46, -0.50),
        (-0.18, -0.54),
        (0.18, -0.48),
        (0.47, -0.42),
        (0.53, -0.12),
        (0.48, 0.19),
        (0.36, 0.48),
        (0.05, 0.54),
        (-0.24, 0.49),
        (-0.51, 0.31),
        (-0.55, 0.02),
        (-0.52, -0.29),
    ]
    verts: list[tuple[float, float, float]] = []
    bottom_indices: list[int] = []
    top_indices: list[int] = []
    for index, (x_factor, y_factor) in enumerate(outline):
        chip = (((index * 41) % 7) - 3) * 0.018
        x = x_factor * width * (1.0 + chip)
        y = y_factor * depth * (1.0 - chip * 0.7)
        bottom_indices.append(len(verts))
        verts.append((x, y, -height * (0.47 + (index % 3) * 0.018)))
        top_indices.append(len(verts))
        verts.append((x * (0.93 + (index % 4) * 0.014), y * (0.95 - (index % 2) * 0.018), height * (0.47 + (index % 5) * 0.014)))

    faces: list[tuple[int, ...]] = [tuple(reversed(bottom_indices)), tuple(top_indices)]
    for index in range(len(outline)):
        next_index = (index + 1) % len(outline)
        faces.append((bottom_indices[index], bottom_indices[next_index], top_indices[next_index], top_indices[index]))

    mesh = bpy.data.meshes.new(f"{name}_Mesh")
    mesh.from_pydata(verts, [], faces)
    mesh.update()
    obj = bpy.data.objects.new(name, mesh)
    obj.location = location
    obj.rotation_euler = rotation
    obj.data.materials.append(material)
    top_index = 0
    side_index = 0
    if top_material is not None:
        obj.data.materials.append(top_material)
        top_index = len(obj.data.materials) - 1
    if side_variation_material is not None:
        obj.data.materials.append(side_variation_material)
        side_index = len(obj.data.materials) - 1
    for face_index, polygon in enumerate(obj.data.polygons):
        if face_index == 1 and top_material is not None:
            polygon.material_index = top_index
        elif face_index > 1 and side_variation_material is not None and face_index % 3 == 0:
            polygon.material_index = side_index
    collection.objects.link(obj)
    if bevel > 0:
        modifier = obj.modifiers.new("AET_FacetedStoneEdgeBevel", "BEVEL")
        modifier.width = bevel
        modifier.segments = 1
        modifier.affect = "EDGES"
        set_active(obj)
        bpy.ops.object.modifier_apply(modifier=modifier.name)
    try:
        normal = obj.modifiers.new("AET_WeightedStoneNormals", "WEIGHTED_NORMAL")
        set_active(obj)
        bpy.ops.object.modifier_apply(modifier=normal.name)
    except Exception:
        pass
    smart_uv(obj)
    return obj


def add_broken_plate(
    name: str,
    location: tuple[float, float, float],
    width: float,
    height: float,
    thickness: float,
    rotation: tuple[float, float, float],
    material: bpy.types.Material,
    collection: bpy.types.Collection,
    top_material: bpy.types.Material | None = None,
    side_variation_material: bpy.types.Material | None = None,
    bevel: float = 1.6,
    variant: int = 0,
) -> bpy.types.Object:
    outlines = [
        [
            (-0.50, -0.49),
            (-0.35, -0.52),
            (-0.15, -0.47),
            (0.14, -0.51),
            (0.43, -0.45),
            (0.50, -0.18),
            (0.44, 0.12),
            (0.38, 0.42),
            (0.20, 0.50),
            (0.04, 0.44),
            (-0.12, 0.54),
            (-0.31, 0.46),
            (-0.48, 0.26),
            (-0.42, 0.02),
        ],
        [
            (-0.47, -0.50),
            (-0.22, -0.48),
            (0.06, -0.54),
            (0.36, -0.47),
            (0.49, -0.28),
            (0.44, 0.08),
            (0.52, 0.37),
            (0.28, 0.50),
            (0.10, 0.42),
            (-0.05, 0.56),
            (-0.28, 0.38),
            (-0.52, 0.18),
            (-0.43, -0.10),
        ],
        [
            (-0.52, -0.48),
            (-0.28, -0.54),
            (-0.02, -0.46),
            (0.27, -0.52),
            (0.50, -0.38),
            (0.42, -0.08),
            (0.48, 0.18),
            (0.32, 0.47),
            (0.08, 0.54),
            (-0.12, 0.44),
            (-0.33, 0.52),
            (-0.49, 0.24),
            (-0.45, -0.18),
        ],
    ]
    outline = outlines[variant % len(outlines)]
    verts: list[tuple[float, float, float]] = []
    front: list[int] = []
    back: list[int] = []
    for index, (x_factor, z_factor) in enumerate(outline):
        chip = (((index * 53 + variant * 19) % 11) - 5) * 0.012
        x = x_factor * width * (1.0 + chip)
        z = z_factor * height * (1.0 - chip * 0.5)
        y_front = -thickness * (0.50 + ((index + variant) % 3) * 0.018)
        y_back = thickness * (0.50 - ((index + variant) % 4) * 0.012)
        front.append(len(verts))
        verts.append((x, y_front, z))
        back.append(len(verts))
        verts.append((x * 0.96, y_back, z * (0.98 + (index % 2) * 0.018)))

    faces: list[tuple[int, ...]] = [tuple(front), tuple(reversed(back))]
    for index in range(len(outline)):
        next_index = (index + 1) % len(outline)
        faces.append((front[index], front[next_index], back[next_index], back[index]))

    mesh = bpy.data.meshes.new(f"{name}_Mesh")
    mesh.from_pydata(verts, [], faces)
    mesh.update()
    obj = bpy.data.objects.new(name, mesh)
    obj.location = location
    obj.rotation_euler = rotation
    obj.data.materials.append(material)
    top_index = 0
    side_index = 0
    if top_material is not None:
        obj.data.materials.append(top_material)
        top_index = len(obj.data.materials) - 1
    if side_variation_material is not None:
        obj.data.materials.append(side_variation_material)
        side_index = len(obj.data.materials) - 1
    for face_index, polygon in enumerate(obj.data.polygons):
        if face_index == 0 and top_material is not None:
            polygon.material_index = top_index
        elif face_index > 1 and side_variation_material is not None and face_index % 2 == 0:
            polygon.material_index = side_index
    collection.objects.link(obj)
    if bevel > 0:
        modifier = obj.modifiers.new("AET_ChippedPlateEdgeBevel", "BEVEL")
        modifier.width = bevel
        modifier.segments = 1
        modifier.affect = "EDGES"
        set_active(obj)
        bpy.ops.object.modifier_apply(modifier=modifier.name)
    try:
        normal = obj.modifiers.new("AET_ChippedPlateWeightedNormals", "WEIGHTED_NORMAL")
        set_active(obj)
        bpy.ops.object.modifier_apply(modifier=normal.name)
    except Exception:
        pass
    smart_uv(obj)
    return obj


def add_irregular_disc(
    name: str,
    location: tuple[float, float, float],
    radius_x: float,
    radius_y: float,
    height: float,
    material: bpy.types.Material,
    collection: bpy.types.Collection,
    vertices: int = 28,
    jitter: float = 0.12,
) -> bpy.types.Object:
    verts: list[tuple[float, float, float]] = []
    bottom: list[int] = []
    top: list[int] = []
    for index in range(vertices):
        angle = math.tau * index / vertices
        factor = 1.0 + (((index * 37) % 9) - 4) * jitter * 0.08
        x = math.cos(angle) * radius_x * factor
        y = math.sin(angle) * radius_y * factor
        bottom.append(len(verts))
        verts.append((x, y, -height * 0.5))
        top.append(len(verts))
        verts.append((x * 0.96, y * 0.96, height * 0.5))

    faces: list[tuple[int, ...]] = []
    faces.append(tuple(reversed(bottom)))
    faces.append(tuple(top))
    for index in range(vertices):
        next_index = (index + 1) % vertices
        faces.append((bottom[index], bottom[next_index], top[next_index], top[index]))

    mesh = bpy.data.meshes.new(f"{name}_Mesh")
    mesh.from_pydata(verts, [], faces)
    mesh.update()
    obj = bpy.data.objects.new(name, mesh)
    obj.location = location
    obj.data.materials.append(material)
    collection.objects.link(obj)
    smart_uv(obj)
    return obj


def add_rough_stone(
    name: str,
    location: tuple[float, float, float],
    scale: tuple[float, float, float],
    rotation: tuple[float, float, float],
    material: bpy.types.Material,
    collection: bpy.types.Collection,
    subdivisions: int = 1,
) -> bpy.types.Object:
    bpy.ops.mesh.primitive_ico_sphere_add(subdivisions=subdivisions, radius=1.0, location=location, rotation=rotation)
    obj = bpy.context.object
    obj.name = name
    obj.scale = scale
    obj.data.materials.append(material)
    set_active(obj)
    bpy.ops.object.transform_apply(location=False, rotation=True, scale=True)
    roughen_mesh(obj, 3.0)
    smart_uv(obj)
    move_to_collection(obj, collection)
    return obj


def add_box(
    name: str,
    location: tuple[float, float, float],
    dimensions: tuple[float, float, float],
    rotation: tuple[float, float, float],
    material: bpy.types.Material,
    collection: bpy.types.Collection,
    roughness: float = 0.0,
) -> bpy.types.Object:
    bpy.ops.mesh.primitive_cube_add(size=1.0, location=location, rotation=rotation)
    obj = bpy.context.object
    obj.name = name
    obj.dimensions = dimensions
    obj.data.materials.append(material)
    set_active(obj)
    bpy.ops.object.transform_apply(location=False, rotation=False, scale=True)
    if roughness:
        roughen_mesh(obj, roughness)
    smart_uv(obj)
    move_to_collection(obj, collection)
    return obj


def add_paint_patch(
    name: str,
    location: tuple[float, float, float],
    width: float,
    height: float,
    rotation: tuple[float, float, float],
    material: bpy.types.Material,
    collection: bpy.types.Collection,
    variant: int = 0,
    offset: float = 0.35,
) -> bpy.types.Object:
    outlines = [
        [
            (-0.50, -0.30),
            (-0.32, -0.42),
            (-0.08, -0.32),
            (0.20, -0.38),
            (0.50, -0.24),
            (0.43, 0.02),
            (0.52, 0.26),
            (0.18, 0.38),
            (-0.10, 0.28),
            (-0.34, 0.40),
            (-0.46, 0.14),
        ],
        [
            (-0.48, -0.24),
            (-0.20, -0.38),
            (0.08, -0.28),
            (0.34, -0.42),
            (0.50, -0.18),
            (0.38, 0.12),
            (0.48, 0.34),
            (0.10, 0.40),
            (-0.18, 0.25),
            (-0.42, 0.34),
        ],
        [
            (-0.50, -0.20),
            (-0.28, -0.34),
            (-0.04, -0.22),
            (0.26, -0.36),
            (0.48, -0.12),
            (0.44, 0.18),
            (0.20, 0.36),
            (-0.08, 0.26),
            (-0.34, 0.40),
            (-0.46, 0.08),
        ],
    ]
    outline = outlines[variant % len(outlines)]
    verts = []
    for index, (x_factor, z_factor) in enumerate(outline):
        chip = (((index * 29 + variant * 17) % 9) - 4) * 0.018
        verts.append((x_factor * width * (1.0 + chip), offset, z_factor * height * (1.0 - chip * 0.4)))
    mesh = bpy.data.meshes.new(f"{name}_Mesh")
    mesh.from_pydata(verts, [], [tuple(range(len(verts)))])
    mesh.update()
    obj = bpy.data.objects.new(name, mesh)
    obj.location = location
    obj.rotation_euler = rotation
    obj.data.materials.append(material)
    collection.objects.link(obj)
    smart_uv(obj)
    return obj


def add_cord(
    name: str,
    location: tuple[float, float, float],
    radius: float,
    depth: float,
    rotation: tuple[float, float, float],
    material: bpy.types.Material,
    collection: bpy.types.Collection,
) -> bpy.types.Object:
    bpy.ops.mesh.primitive_cylinder_add(vertices=8, radius=radius, depth=depth, location=location, rotation=rotation)
    obj = bpy.context.object
    obj.name = name
    obj.data.materials.append(material)
    set_active(obj)
    bpy.ops.object.transform_apply(location=False, rotation=False, scale=True)
    smart_uv(obj)
    move_to_collection(obj, collection)
    return obj


def add_scale_marker(name: str, height_cm: float, x: float, materials: dict[str, bpy.types.Material], collection: bpy.types.Collection) -> None:
    add_box(f"Review_{name}_Post", (x, 190, height_cm * 0.5), (8, 8, height_cm), (0, 0, 0), materials["marker"], collection)
    add_box(f"Review_{name}_Cap", (x, 190, height_cm), (42, 8, 6), (0, 0, 0), materials["marker"], collection)


def add_label(text: str, location: tuple[float, float, float], collection: bpy.types.Collection, size: float = 13.0) -> None:
    bpy.ops.object.text_add(location=location, rotation=(math.radians(72), 0, 0))
    obj = bpy.context.object
    obj.name = "Review_Label_" + text.replace(" ", "_").replace("/", "_")
    obj.data.body = text
    obj.data.align_x = "CENTER"
    obj.data.align_y = "CENTER"
    obj.data.size = size
    label_material = bpy.data.materials.get("M_AET_ReviewLabel_Tan_A01")
    if label_material is not None:
        obj.data.materials.append(label_material)
    move_to_collection(obj, collection)


def add_reference_plane(materials: dict[str, bpy.types.Material], collection: bpy.types.Collection) -> None:
    if not REFERENCE_IMAGE.exists():
        return
    material = make_image_material("M_GIA_BloodAxeCairnSlabCluster_A1Reference_A01", REFERENCE_IMAGE)
    bpy.ops.mesh.primitive_plane_add(size=1.0, location=(-330, 58, 178), rotation=(math.radians(90), 0, 0))
    plane = bpy.context.object
    plane.name = "Review_Reference_A1_CandidateCrop"
    plane.dimensions = (190, 216, 1)
    plane.data.materials.append(material)
    set_active(plane)
    bpy.ops.object.transform_apply(location=False, rotation=False, scale=True)
    move_to_collection(plane, collection)
    add_label("A1 reference", (-330, -62, 42), collection, 11)


def build_lod0(collection: bpy.types.Collection, materials: dict[str, bpy.types.Material]) -> list[bpy.types.Object]:
    objects: list[bpy.types.Object] = []
    objects.append(add_irregular_disc("LOD0_AshMudBase_IrregularFootprint", (0, 0, 5), 164, 116, 10, materials["ash"], collection, 32))
    objects.append(add_irregular_disc("LOD0_DarkMud_OffsetGrounding", (-32, -10, 11), 125, 72, 7, materials["mud"], collection, 24))

    main_rot = (math.radians(8), math.radians(-17), math.radians(-14))
    rear_rot = (math.radians(6), math.radians(-11), math.radians(9))
    left_rot = (math.radians(-2), math.radians(12), math.radians(-24))
    right_rot = (math.radians(-5), math.radians(21), math.radians(7))
    objects.append(add_broken_plate("LOD0_Stone_DominantPaintedLeaningSlab", (-38, -8, 58), 138, 54, 17, main_rot, materials["stone_mid"], collection, materials["stone_worn"], materials["stone_dark"], 1.5, 0))
    objects.append(add_broken_plate("LOD0_Stone_SecondaryPaintedCenterShard", (-4, 8, 72), 48, 104, 16, (math.radians(6), math.radians(-8), math.radians(-4)), materials["stone_dark"], collection, materials["stone_mid"], materials["stone_cold_highlight"], 1.2, 2))
    objects.append(add_broken_plate("LOD0_Stone_RearTallBlackShard", (30, 30, 82), 38, 112, 18, rear_rot, materials["stone_dark"], collection, materials["stone_mid"], materials["stone_cold_highlight"], 1.4, 1))
    objects.append(add_broken_plate("LOD0_Stone_LeftKnifeShard", (-78, 18, 58), 34, 72, 15, left_rot, materials["stone_dark"], collection, materials["stone_edge"], materials["stone_cold_highlight"], 1.2, 2))
    objects.append(add_broken_plate("LOD0_Stone_RightBrokenSupportPlate", (68, -18, 50), 42, 72, 17, right_rot, materials["stone_mid"], collection, materials["stone_worn"], materials["stone_dark"], 1.3, 1))
    objects.append(add_broken_plate("LOD0_Stone_BackLeftNarrowShard", (-54, 48, 54), 28, 70, 14, (math.radians(5), math.radians(-19), math.radians(26)), materials["stone_dark"], collection, materials["stone_mid"], materials["stone_cold_highlight"], 1.0, 0))
    objects.append(add_broken_plate("LOD0_Stone_FrontLowBrokenFace", (-40, -66, 32), 118, 38, 16, (math.radians(73), math.radians(0), math.radians(-5)), materials["stone_dark"], collection, materials["stone_edge"], materials["stone_cold_highlight"], 1.1, 2))

    for index, spec in enumerate(
        (
            ((-142, 45, 18), (22, 16, 14), (0, 0, 0), materials["stone_dark"]),
            ((-118, -72, 17), (28, 18, 15), (0, 0, math.radians(18)), materials["stone_worn"]),
            ((-76, -98, 16), (24, 16, 12), (0, 0, math.radians(-21)), materials["stone_dark"]),
            ((-28, -104, 16), (30, 20, 13), (0, 0, math.radians(12)), materials["stone_worn"]),
            ((28, -96, 17), (31, 20, 14), (0, 0, math.radians(-8)), materials["stone_dark"]),
            ((82, -88, 16), (24, 17, 12), (0, 0, math.radians(18)), materials["stone_worn"]),
            ((130, 18, 18), (28, 18, 18), (0, 0, math.radians(24)), materials["stone_mid"]),
            ((-12, 86, 18), (24, 15, 13), (0, 0, math.radians(-31)), materials["stone_worn"]),
            ((94, 72, 17), (20, 14, 12), (0, 0, math.radians(13)), materials["stone_dark"]),
            ((-144, -34, 16), (18, 12, 11), (0, 0, math.radians(-10)), materials["stone_dark"]),
            ((112, -58, 15), (22, 14, 11), (0, 0, math.radians(31)), materials["stone_dark"]),
            ((50, 72, 17), (18, 14, 12), (0, 0, math.radians(-12)), materials["stone_worn"]),
        ),
        1,
    ):
        loc, scale, rot, mat = spec
        objects.append(add_rough_stone(f"LOD0_SupportStone_{index:02d}", loc, scale, rot, mat, collection, 1))

    objects.append(add_box("LOD0_BloodAxePaint_MainWeatheredSlash", (-47, -31, 64), (84, 1.1, 5), (math.radians(8), math.radians(-17), math.radians(-16)), materials["paint"], collection, 0.12))
    objects.append(add_box("LOD0_BloodAxePaint_SecondaryBrokenSlash", (-17, -32, 58), (48, 1.1, 4), (math.radians(8), math.radians(-12), math.radians(-12)), materials["paint_dark"], collection, 0.10))
    objects.append(add_box("LOD0_BloodAxePaint_CrossFadedStroke", (-30, -33, 67), (5, 1.1, 34), (math.radians(8), math.radians(-17), math.radians(27)), materials["paint"], collection, 0.10))
    objects.append(add_box("LOD0_BloodAxePaint_LeftLowFragment", (-96, -39, 50), (34, 1.0, 4), left_rot, materials["paint"], collection, 0.10))
    objects.append(add_box("LOD0_BloodAxePaint_RearSlabOldMark", (25, 3, 93), (5, 1.0, 34), rear_rot, materials["paint_dark"], collection, 0.08))

    objects.append(add_box("LOD0_StoneScar_MainLongCrack", (-32, -37, 81), (34, 3, 3), (math.radians(8), math.radians(-17), math.radians(-30)), materials["scar"], collection, 0.12))
    objects.append(add_box("LOD0_StoneScar_RightVerticalSplit", (68, -42, 66), (3, 3, 34), right_rot, materials["scar"], collection, 0.12))
    objects.append(add_box("LOD0_StoneScar_LeftLowSplit", (-86, -38, 58), (3, 3, 21), left_rot, materials["scar"], collection, 0.08))
    objects.append(add_box("LOD0_StoneScar_RearTopChipShadow", (33, 4, 130), (30, 3, 5), rear_rot, materials["scar"], collection, 0.1))

    objects.append(add_cord("LOD0_RawhideCord_MainFrontBand", (-62, -50, 48), 2.4, 74, (math.radians(0), math.radians(91), math.radians(6)), materials["rawhide"], collection))
    objects.append(add_cord("LOD0_RawhideCord_SecondaryFrontBand", (-57, -55, 43), 1.9, 58, (math.radians(-2), math.radians(92), math.radians(12)), materials["rawhide"], collection))
    objects.append(add_rough_stone("LOD0_RawhideKnot_DarkSmallTie", (-91, -55, 50), (8, 6, 6), (math.radians(4), math.radians(8), math.radians(6)), materials["rawhide"], collection, 1))
    objects.append(add_cord("LOD0_RawhideCord_LooseTailLeft", (-100, -62, 50), 2.5, 34, (math.radians(91), math.radians(72), math.radians(-12)), materials["rawhide"], collection))
    objects.append(add_cord("LOD0_RawhideCord_LooseTailRight", (-48, -60, 50), 2.2, 28, (math.radians(88), math.radians(78), math.radians(16)), materials["rawhide"], collection))
    objects.append(add_cord("LOD0_RawhideCord_RearSlabTie", (27, 6, 68), 2.2, 48, (math.radians(8), math.radians(74), math.radians(8)), materials["rawhide"], collection))

    objects.extend(add_painted_poc_details(collection, materials, main_rot, rear_rot, left_rot, right_rot))
    return objects


def add_painted_poc_details(
    collection: bpy.types.Collection,
    materials: dict[str, bpy.types.Material],
    main_rot: tuple[float, float, float],
    rear_rot: tuple[float, float, float],
    left_rot: tuple[float, float, float],
    right_rot: tuple[float, float, float],
) -> list[bpy.types.Object]:
    objects: list[bpy.types.Object] = []

    paint_weathering_specs = (
        ("MainSlashDarkUndertone", (-42, -33, 64), (72, 1.0, 3), main_rot, materials["paint_dark"]),
        ("CrossSlashDarkBase", (-29, -34, 66), (4, 1.0, 30), (math.radians(8), math.radians(-17), math.radians(24)), materials["paint_dark"]),
        ("MainSlashChipA", (-68, -34, 64), (11, 1.0, 4), main_rot, materials["paint_chip"]),
        ("MainSlashChipB", (-32, -34, 65), (9, 1.0, 4), main_rot, materials["paint_chip"]),
        ("MainSlashChipC", (2, -34, 63), (10, 1.0, 4), main_rot, materials["paint_chip"]),
        ("CrossSlashChipUpper", (-27, -35, 79), (5, 1.0, 6), (math.radians(8), math.radians(-17), math.radians(24)), materials["paint_chip"]),
        ("CrossSlashChipLower", (-31, -35, 53), (5, 1.0, 7), (math.radians(8), math.radians(-17), math.radians(24)), materials["paint_chip"]),
    )
    for suffix, loc, dims, rot, material in paint_weathering_specs:
        objects.append(add_box(f"LOD0_PaintedPOC_RedMark_{suffix}", loc, dims, rot, material, collection, 0.08))

    ground_specs = (
        ("AshSweepLeft", (-98, -58, 18), 44, 18, 2.2, materials["ash_light"], 16),
        ("AshSweepRear", (-4, 60, 18), 54, 20, 2.0, materials["ash_light"], 18),
        ("WetMudUnderMain", (-18, -52, 17), 78, 22, 2.4, materials["mud_wet"], 18),
        ("DarkMudRightPool", (88, -16, 17), 46, 21, 2.2, materials["mud_wet"], 16),
    )
    for suffix, loc, radius_x, radius_y, height, material, verts in ground_specs:
        objects.append(add_irregular_disc(f"LOD0_PaintedPOC_Ground_{suffix}", loc, radius_x, radius_y, height, material, collection, verts, 0.18))

    return objects


def assign_vertex_color_material(obj: bpy.types.Object, material: bpy.types.Material) -> None:
    if getattr(obj, "type", None) != "MESH":
        return
    original_colors = [slot.material.diffuse_color[:] if slot.material else (0.5, 0.5, 0.5, 1.0) for slot in obj.material_slots]
    if not original_colors:
        original_colors = [(0.5, 0.5, 0.5, 1.0)]
    color_attr = obj.data.color_attributes.get("AET_VertexColor")
    if color_attr is None:
        color_attr = obj.data.color_attributes.new(name="AET_VertexColor", type="BYTE_COLOR", domain="CORNER")
    for polygon in obj.data.polygons:
        base_color = original_colors[min(polygon.material_index, len(original_colors) - 1)]
        for loop_index in polygon.loop_indices:
            loop = obj.data.loops[loop_index]
            n1 = procedural_noise(loop.vertex_index + len(obj.name) * 17, polygon.index + len(obj.name) * 29, 211)
            n2 = procedural_noise(loop.vertex_index + polygon.index * 7, len(obj.name) * 11, 307)
            red_read = base_color[0] > 0.22 and base_color[1] < 0.08
            rawhide_read = base_color[0] > 0.18 and base_color[1] > 0.08 and base_color[2] < 0.18 and not red_read
            if red_read:
                variation = 0.72 + n1 * 0.30
                color = (base_color[0] * variation, base_color[1] * variation, base_color[2] * variation, 1.0)
            elif rawhide_read:
                variation = 0.78 + n1 * 0.26
                color = (
                    base_color[0] * variation + n2 * 0.035,
                    base_color[1] * variation + n2 * 0.022,
                    base_color[2] * variation,
                    1.0,
                )
            else:
                variation = 0.70 + n1 * 0.36
                cool_shift = (n2 - 0.5) * 0.035
                color = (
                    clamp(base_color[0] * variation + cool_shift),
                    clamp(base_color[1] * variation + cool_shift),
                    clamp(base_color[2] * variation + cool_shift * 0.75),
                    1.0,
                )
            color_attr.data[loop_index].color = color
    obj.data.materials.clear()
    obj.data.materials.append(material)


def convert_collection_to_vertex_material(collection: bpy.types.Collection, material: bpy.types.Material) -> None:
    for obj in collection.objects:
        assign_vertex_color_material(obj, material)


def procedural_noise(x: int, y: int, seed: int) -> float:
    value = (x * 374761393 + y * 668265263 + seed * 982451653) & 0xFFFFFFFF
    value = (value ^ (value >> 13)) * 1274126177 & 0xFFFFFFFF
    return ((value ^ (value >> 16)) & 0xFFFF) / 65535.0


def clamp(value: float) -> float:
    return max(0.0, min(1.0, value))


def save_texture(path: Path, width: int, height: int, pixels: array) -> None:
    image = bpy.data.images.new(path.stem, width=width, height=height, alpha=True, float_buffer=False)
    image.pixels.foreach_set(pixels)
    image.filepath_raw = str(path)
    image.file_format = "PNG"
    image.save()
    bpy.data.images.remove(image)


def generate_texture_maps() -> dict[str, Path]:
    texture_dir = TEXTURE_ROOT / TEXTURE_REL_PATH
    texture_dir.mkdir(parents=True, exist_ok=True)
    width = 1024
    height = 1024
    bc = array("f")
    normal = array("f")
    orm = array("f")
    for y in range(height):
        v = y / (height - 1)
        for x in range(width):
            u = x / (width - 1)
            n1 = procedural_noise(x, y, 17)
            n2 = procedural_noise(x // 4, y // 4, 71)
            if v < 0.24:
                base = (0.10 + n1 * 0.09, 0.075 + n2 * 0.055, 0.048 + n1 * 0.035)
                roughness = 0.94
                occlusion = 0.58 + n2 * 0.18
            elif v < 0.68:
                red_mark = 0.47 < u < 0.57 or abs((u - 0.51) - (v - 0.42) * 0.65) < 0.025
                if red_mark and n1 > 0.24:
                    base = (0.42 + n2 * 0.18, 0.03 + n1 * 0.025, 0.022 + n2 * 0.018)
                else:
                    cold = 0.11 + n1 * 0.16
                    warm = 0.08 + n2 * 0.12
                    base = (cold + warm * 0.25, cold + warm * 0.18, cold + warm * 0.10)
                roughness = 0.88 + n2 * 0.08
                occlusion = 0.50 + n1 * 0.28
            elif v < 0.84:
                base = (0.23 + n1 * 0.20, 0.13 + n2 * 0.12, 0.065 + n1 * 0.05)
                roughness = 0.82 + n2 * 0.09
                occlusion = 0.60 + n1 * 0.18
            else:
                paint_wear = 0.35 + n1 * 0.45
                base = (0.28 + paint_wear * 0.44, 0.018 + n2 * 0.025, 0.012 + n1 * 0.025)
                roughness = 0.91
                occlusion = 0.64 + n2 * 0.20

            bc.extend((clamp(base[0]), clamp(base[1]), clamp(base[2]), 1.0))

            height_value = (n1 - 0.5) * 0.10 + (n2 - 0.5) * 0.06
            nx = clamp(0.5 + height_value)
            ny = clamp(0.5 + (procedural_noise(x, y, 113) - 0.5) * 0.13)
            normal.extend((nx, ny, 1.0, 1.0))

            orm.extend((clamp(occlusion), clamp(roughness), 0.0, 1.0))

    paths = {
        "BC": texture_dir / "T_GIA_BloodAxeCairnSlabCluster_A01_BC.png",
        "N": texture_dir / "T_GIA_BloodAxeCairnSlabCluster_A01_N.png",
        "ORM": texture_dir / "T_GIA_BloodAxeCairnSlabCluster_A01_ORM.png",
    }
    save_texture(paths["BC"], width, height, bc)
    save_texture(paths["N"], width, height, normal)
    save_texture(paths["ORM"], width, height, orm)
    return paths


def generate_painted_preview_maps() -> dict[str, list[Path]]:
    texture_dir = TEXTURE_ROOT / TEXTURE_REL_PATH
    armorpaint_dir = ARMORPAINT_ROOT / REL_PATH
    texture_dir.mkdir(parents=True, exist_ok=True)
    armorpaint_dir.mkdir(parents=True, exist_ok=True)
    width = 2048
    height = 2048
    bc = array("f")
    normal = array("f")
    orm = array("f")
    for y in range(height):
        v = y / (height - 1)
        for x in range(width):
            u = x / (width - 1)
            n1 = procedural_noise(x, y, 419)
            n2 = procedural_noise(x // 5, y // 5, 853)
            n3 = procedural_noise(x // 17, y // 17, 1447)
            red_diagonal = abs((v - 0.54) - (u - 0.43) * 0.34) < 0.032
            red_cross = abs((v - 0.52) + (u - 0.53) * 0.48) < 0.026 and 0.25 < u < 0.72
            red_old_vertical = 0.77 < u < 0.84 and 0.42 < v < 0.80
            red_mark = (red_diagonal or red_cross or red_old_vertical) and n1 > 0.18
            chipped = red_mark and n2 < 0.30

            if v < 0.23:
                base = (
                    0.075 + n1 * 0.070 + n3 * 0.025,
                    0.052 + n2 * 0.050,
                    0.035 + n1 * 0.030,
                )
                roughness = 0.95
                occlusion = 0.55 + n2 * 0.23
            elif red_mark and not chipped:
                fade = 0.55 + n2 * 0.38
                base = (
                    0.18 + fade * 0.28,
                    0.012 + n1 * 0.026,
                    0.008 + n2 * 0.020,
                )
                roughness = 0.89 + n3 * 0.06
                occlusion = 0.50 + n1 * 0.18
            elif 0.70 < u < 0.96 and 0.22 < v < 0.88 and n3 > 0.68:
                base = (
                    0.15 + n1 * 0.10,
                    0.088 + n2 * 0.070,
                    0.042 + n1 * 0.045,
                )
                roughness = 0.84 + n2 * 0.09
                occlusion = 0.62 + n1 * 0.18
            else:
                warm_edge = max(0.0, min(1.0, (n3 - 0.46) * 1.8))
                cold = 0.055 + n1 * 0.080
                warm = 0.030 + n2 * 0.075 + warm_edge * 0.060
                base = (
                    cold + warm * 0.95,
                    cold + warm * 0.70,
                    cold + warm * 0.38,
                )
                roughness = 0.87 + n2 * 0.08
                occlusion = 0.48 + n1 * 0.25

            bc.extend((clamp(base[0]), clamp(base[1]), clamp(base[2]), 1.0))

            height_value = (n1 - 0.5) * 0.14 + (n2 - 0.5) * 0.08
            nx = clamp(0.5 + height_value)
            ny = clamp(0.5 + (procedural_noise(x, y, 1789) - 0.5) * 0.14)
            normal.extend((nx, ny, 1.0, 1.0))

            orm.extend((clamp(occlusion), clamp(roughness), 0.0, 1.0))

    paths = {
        "BC": [
            texture_dir / "T_GIA_BloodAxeCairnSlabCluster_A01_BC_PaintedPreview.png",
            armorpaint_dir / "T_GIA_BloodAxeCairnSlabCluster_A01_BC_PaintedPreview.png",
        ],
        "N": [
            texture_dir / "T_GIA_BloodAxeCairnSlabCluster_A01_N_PaintedPreview.png",
            armorpaint_dir / "T_GIA_BloodAxeCairnSlabCluster_A01_N_PaintedPreview.png",
        ],
        "ORM": [
            texture_dir / "T_GIA_BloodAxeCairnSlabCluster_A01_ORM_PaintedPreview.png",
            armorpaint_dir / "T_GIA_BloodAxeCairnSlabCluster_A01_ORM_PaintedPreview.png",
        ],
    }
    for output_path in paths["BC"]:
        save_texture(output_path, width, height, bc)
    for output_path in paths["N"]:
        save_texture(output_path, width, height, normal)
    for output_path in paths["ORM"]:
        save_texture(output_path, width, height, orm)
    return paths


def build_simplified_lod(
    collection: bpy.types.Collection,
    materials: dict[str, bpy.types.Material],
    prefix: str,
    stone_count: int,
    include_lashing: bool,
) -> list[bpy.types.Object]:
    objects: list[bpy.types.Object] = []
    objects.append(add_irregular_disc(f"{prefix}_AshMudBase_Simplified", (0, 0, 4), 150, 104, 7, materials["ash"], collection, 18))
    objects.append(add_slab(f"{prefix}_Stone_PrimaryFallenSlab", (-28, -4, 42), (128, 48, 28), (math.radians(-8), math.radians(6), math.radians(-12)), materials["stone_mid"], collection, 4.0, 1.5))
    if stone_count >= 2:
        objects.append(add_slab(f"{prefix}_Stone_RearUprightMass", (32, 28, 72), (40, 30, 100), (math.radians(7), math.radians(-14), math.radians(12)), materials["stone_dark"], collection, 3.0, 1.4))
    if stone_count >= 3:
        objects.append(add_slab(f"{prefix}_Stone_LeftLowMass", (-105, -17, 34), (56, 40, 24), (math.radians(4), math.radians(-4), math.radians(-24)), materials["stone_worn"], collection, 3.0, 1.2))
    if stone_count >= 4:
        objects.append(add_slab(f"{prefix}_Stone_RightLeanMass", (75, -23, 48), (34, 30, 66), (math.radians(-6), math.radians(19), math.radians(-8)), materials["stone_mid"], collection, 3.0, 1.2))
    objects.append(add_box(f"{prefix}_BloodAxePaint_BroadSlash", (-38, -29, 65), (74, 4, 5), (math.radians(-8), math.radians(6), math.radians(-12)), materials["paint"], collection, 0.0))
    if include_lashing:
        objects.append(add_box(f"{prefix}_RawhideWrap_BroadFrontBand", (-61, -48, 54), (78, 6, 7), (math.radians(-4), math.radians(2), math.radians(6)), materials["rawhide"], collection, 0.0))
    return objects


def build_collision(collection: bpy.types.Collection, materials: dict[str, bpy.types.Material]) -> list[bpy.types.Object]:
    proxy = add_box(
        f"UCX_{ASSET_NAME}_00",
        (-8, -8, 48),
        (310, 210, 95),
        (0, 0, math.radians(-8)),
        materials["collision"],
        collection,
    )
    proxy.display_type = "WIRE"
    proxy.hide_render = True
    return [proxy]


def add_review_markers(materials: dict[str, bpy.types.Material], collection: bpy.types.Collection) -> None:
    add_scale_marker("Cairn_145cm", 145.0, 265, materials, collection)
    add_scale_marker("GiantFemale_442cm", GIANT_FEMALE_BASELINE_CM, 330, materials, collection)
    add_scale_marker("GiantMale_470cm", GIANT_MALE_BASELINE_CM, 390, materials, collection)
    add_label("145 cm POC", (265, 175, 166), collection, 11)
    add_label("442 cm female Giant", (330, 175, 462), collection, 11)
    add_label("470 cm male Giant", (390, 175, 490), collection, 11)
    add_label("SM_GIA_BloodAxeCairnSlabCluster_A01", (18, -168, 28), collection, 9)


def render_review(materials: dict[str, bpy.types.Material]) -> None:
    REVIEW_ROOT.mkdir(parents=True, exist_ok=True)
    scene = bpy.context.scene
    scene.render.resolution_x = 1900
    scene.render.resolution_y = 1200
    try:
        scene.eevee.taa_render_samples = 64
    except Exception:
        pass
    if scene.world is not None:
        scene.world.color = (0.58, 0.57, 0.53)

    review_collection = make_collection("Review_Reference_And_Markers")
    add_reference_plane(materials, review_collection)
    add_review_markers(materials, review_collection)

    bpy.ops.object.light_add(type="SUN", location=(0, -460, 760), rotation=(math.radians(50), 0, math.radians(24)))
    sun = bpy.context.object
    sun.name = "AET_CairnSlabClusterReview_Sun"
    sun.data.energy = 1.05

    bpy.ops.object.light_add(type="AREA", location=(-260, -420, 330))
    key = bpy.context.object
    key.name = "AET_CairnSlabClusterReview_KeyLight"
    key.data.energy = 700
    key.data.size = 500

    bpy.ops.object.light_add(type="AREA", location=(380, 240, 260))
    fill = bpy.context.object
    fill.name = "AET_CairnSlabClusterReview_FillLight"
    fill.data.energy = 185
    fill.data.size = 540

    bpy.ops.object.camera_add(location=(500, -680, 300))
    camera = bpy.context.object
    target = Vector((20.0, 0.0, 150.0))
    direction = target - Vector(camera.location)
    camera.rotation_euler = direction.to_track_quat("-Z", "Y").to_euler()
    camera.data.type = "ORTHO"
    camera.data.ortho_scale = 690
    camera.data.clip_start = 1
    camera.data.clip_end = 5000
    scene.camera = camera

    scene.render.filepath = str(REVIEW_RENDER)
    bpy.ops.render.render(write_still=True)
    shutil.copyfile(REVIEW_RENDER, PAINTED_REVIEW_RENDER)


def render_painted_approval() -> None:
    scene = bpy.context.scene
    scene.render.resolution_x = 1600
    scene.render.resolution_y = 1000
    for obj in bpy.data.objects:
        if obj.name.startswith("Review_") and obj.name != "Review_Reference_A1_CandidateCrop":
            obj.hide_render = True
        if obj.name.startswith("Review_Label_"):
            obj.hide_render = True

    if scene.world is not None:
        scene.world.color = (0.50, 0.49, 0.46)

    if scene.camera is not None:
        camera = scene.camera
        camera.location = (460, -660, 285)
        target = Vector((-120.0, 2.0, 118.0))
        direction = target - Vector(camera.location)
        camera.rotation_euler = direction.to_track_quat("-Z", "Y").to_euler()
        camera.data.type = "ORTHO"
        camera.data.ortho_scale = 540
        camera.data.clip_start = 1
        camera.data.clip_end = 5000

    scene.render.filepath = str(PAINTED_APPROVAL_RENDER)
    bpy.ops.render.render(write_still=True)


def object_triangle_count(obj: bpy.types.Object) -> int:
    obj.data.calc_loop_triangles()
    return len(obj.data.loop_triangles)


def collection_triangle_count(collection: bpy.types.Collection) -> int:
    return sum(object_triangle_count(obj) for obj in collection.objects if getattr(obj, "type", None) == "MESH")


def collection_bounds(collection: bpy.types.Collection) -> tuple[float, float, float]:
    points: list[Vector] = []
    for obj in collection.objects:
        if getattr(obj, "type", None) != "MESH":
            continue
        points.extend(obj.matrix_world @ Vector(corner) for corner in obj.bound_box)
    if not points:
        return (0.0, 0.0, 0.0)
    min_x = min(point.x for point in points)
    max_x = max(point.x for point in points)
    min_y = min(point.y for point in points)
    max_y = max(point.y for point in points)
    min_z = min(point.z for point in points)
    max_z = max(point.z for point in points)
    return (max_x - min_x, max_y - min_y, max_z - min_z)


def purge_unused_materials() -> None:
    for material in list(bpy.data.materials):
        if material.users == 0:
            bpy.data.materials.remove(material)


def export_selected_fbx(path: Path, objects: list[bpy.types.Object]) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    bpy.ops.object.select_all(action="DESELECT")
    for obj in objects:
        obj.hide_set(False)
        obj.hide_viewport = False
        for collection in obj.users_collection:
            collection.hide_viewport = False
        obj.select_set(True)
    if objects:
        bpy.context.view_layer.objects.active = objects[0]
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


def build() -> None:
    clear_scene()
    setup_scene()
    materials = create_materials()

    lod0_collection = make_collection(f"{ASSET_NAME}_LOD0_Export")
    lod1_collection = make_collection(f"{ASSET_NAME}_LOD1_Source", hidden=True)
    lod2_collection = make_collection(f"{ASSET_NAME}_LOD2_Source", hidden=True)
    lod3_collection = make_collection(f"{ASSET_NAME}_LOD3_Source", hidden=True)
    collision_collection = make_collection(f"{ASSET_NAME}_Collision_Source", hidden=True)

    lod0_objects = build_lod0(lod0_collection, materials)
    lod1_objects = build_simplified_lod(lod1_collection, materials, "LOD1", 4, True)
    lod2_objects = build_simplified_lod(lod2_collection, materials, "LOD2", 3, False)
    lod3_objects = build_simplified_lod(lod3_collection, materials, "LOD3", 2, False)
    collision_objects = build_collision(collision_collection, materials)
    texture_paths = generate_texture_maps()
    painted_preview_paths = generate_painted_preview_maps()

    add_asset_metadata(
        ASSET_NAME,
        "Art-match game-ready source based on Blood Axe cairn candidate A1. Includes jagged slab geometry, BC/N/ORM texture handoff maps, LOD source collections, UCX collision proxy source, proof render, and FBX handoffs. Candidate visual still waits for Flamestrike aesthetic approval before canon lock or Unreal placement.",
        UNREAL_PATH,
    )

    blend_path = BLENDER_ROOT / REL_PATH / f"{ASSET_NAME}.blend"
    export_path = EXPORT_ROOT / REL_PATH / f"{ASSET_NAME}.fbx"
    blend_path.parent.mkdir(parents=True, exist_ok=True)
    export_path.parent.mkdir(parents=True, exist_ok=True)

    render_review(materials)
    render_painted_approval()
    purge_unused_materials()
    bpy.ops.wm.save_as_mainfile(filepath=str(blend_path))

    export_selected_fbx(export_path, lod0_objects + collision_objects)
    export_selected_fbx(export_path.with_name(f"{ASSET_NAME}_LOD0.fbx"), lod0_objects)
    export_selected_fbx(export_path.with_name(f"{ASSET_NAME}_LOD1.fbx"), lod1_objects)
    export_selected_fbx(export_path.with_name(f"{ASSET_NAME}_LOD2.fbx"), lod2_objects)
    export_selected_fbx(export_path.with_name(f"{ASSET_NAME}_LOD3.fbx"), lod3_objects)

    width, depth, height = collection_bounds(lod0_collection)
    print(f"Built {blend_path.relative_to(ROOT)}")
    print(f"Exported {export_path.relative_to(ROOT)}")
    print(f"Rendered {REVIEW_RENDER.relative_to(ROOT)}")
    print(f"Rendered painted copy {PAINTED_REVIEW_RENDER.relative_to(ROOT)}")
    shutil.copyfile(PAINTED_REVIEW_RENDER, GAME_READY_REVIEW_RENDER)
    print(f"Rendered game-ready copy {GAME_READY_REVIEW_RENDER.relative_to(ROOT)}")
    print(f"Rendered painted approval review {PAINTED_APPROVAL_RENDER.relative_to(ROOT)}")
    for texture_type, texture_path in texture_paths.items():
        print(f"Texture {texture_type}: {texture_path.relative_to(ROOT)}")
    for texture_type, output_paths in painted_preview_paths.items():
        for texture_path in output_paths:
            print(f"Painted preview texture {texture_type}: {texture_path.relative_to(ROOT)}")
    print(f"LOD0 metrics: {len(lod0_objects)} mesh objects, {collection_triangle_count(lod0_collection)} tris, {width:.2f}w x {depth:.2f}d x {height:.2f}h cm")
    print(f"LOD1 tris: {collection_triangle_count(lod1_collection)}")
    print(f"LOD2 tris: {collection_triangle_count(lod2_collection)}")
    print(f"LOD3 tris: {collection_triangle_count(lod3_collection)}")
    print(f"Collision proxies: {len(collision_objects)}")


if __name__ == "__main__":
    build()
