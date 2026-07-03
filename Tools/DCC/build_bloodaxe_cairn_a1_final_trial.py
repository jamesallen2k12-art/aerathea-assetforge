#!/usr/bin/env python3
"""Build the final-trial Blood Axe cairn game asset from A01.

Run with:
    blender --background --python Tools/DCC/build_bloodaxe_cairn_a1_final_trial.py

This is the no-approval-stop trial pass requested by Flamestrike: true 360
stone volumes, A01-guided front projection material, inferred side/back stone
treatment, texture maps, LOD exports, collision, and review evidence.
"""

from __future__ import annotations

import math
import random
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

ASSET_NAME = "SM_GIA_BloodAxeCairnSlabCluster_A01_FinalTrial"
REL_PATH = f"Props/Giants/BloodAxe/Cairns/{ASSET_NAME}"
UNREAL_PATH = f"/Game/Aerathea/Props/Giants/BloodAxe/Cairns/{ASSET_NAME}"
REVIEW_ROOT = ROOT / "Saved" / "Automation" / "DCC" / ASSET_NAME
TEXTURE_DIR = TEXTURE_ROOT / REL_PATH

A01_REFERENCE = ROOT / "docs/assets/visual_canon/VC_GIA_BloodAxe_CairnStones_A01_A1_Crop.png"
TURNAROUND_REFERENCE = ROOT / "docs/assets/visual_canon/VC_GIA_BloodAxe_CairnStones_A01_A1_TurnaroundDraft_A01.png"

sys.path.insert(0, str(ROOT))

from Tools.DCC.build_next_slice_assets import add_asset_metadata, clear_scene, setup_scene  # noqa: E402


RNG = random.Random(3719)

PROJECTION_X_MIN = -190.0
PROJECTION_X_MAX = 190.0
PROJECTION_Z_MIN = 0.0
PROJECTION_Z_MAX = 178.0


POINTS = {
    "P01_RearTallSlabApex": (25.0, 38.0, 160.0),
    "P02_MainSlabFrontLeftCorner": (-112.0, -55.0, 55.0),
    "P03_MainSlabFrontRightCorner": (108.0, -46.0, 43.0),
    "P04_MainSlabRearLeftCorner": (-98.0, 31.0, 88.0),
    "P05_MainSlabRearRightCorner": (103.0, 34.0, 78.0),
    "P06_RightUprightApex": (125.0, 18.0, 111.0),
    "P07_LeftStackOuterCorner": (-155.0, -36.0, 42.0),
    "P08_LeftRearShardApex": (-54.0, 38.0, 116.0),
    "P09_RightLashingEndpoint": (133.0, -6.0, 63.0),
    "P10_LeftLashingEndpoint": (-72.0, -58.0, 52.0),
    "P11_BackStoneRoot": (9.0, 59.0, 24.0),
    "P12_FrontPebbleEdge": (13.0, -91.0, 8.0),
}


def make_collection(name: str, hidden: bool = False) -> bpy.types.Collection:
    collection = bpy.data.collections.new(name)
    bpy.context.scene.collection.children.link(collection)
    collection.hide_viewport = hidden
    collection.hide_render = hidden
    return collection


def set_active(obj: bpy.types.Object) -> None:
    bpy.ops.object.select_all(action="DESELECT")
    bpy.context.view_layer.objects.active = obj
    obj.select_set(True)


def link_to_collection(obj: bpy.types.Object, collection: bpy.types.Collection) -> None:
    for current in list(obj.users_collection):
        current.objects.unlink(obj)
    collection.objects.link(obj)


def make_material(
    name: str,
    color: tuple[float, float, float, float],
    roughness: float = 0.9,
    metallic: float = 0.0,
    emission_strength: float = 0.18,
) -> bpy.types.Material:
    material = bpy.data.materials.new(name)
    material.diffuse_color = color
    material.use_nodes = True
    bsdf = material.node_tree.nodes.get("Principled BSDF")
    if bsdf is not None:
        bsdf.inputs["Base Color"].default_value = color
        bsdf.inputs["Roughness"].default_value = roughness
        bsdf.inputs["Metallic"].default_value = metallic
        if "Emission Color" in bsdf.inputs:
            bsdf.inputs["Emission Color"].default_value = (color[0] * 0.55, color[1] * 0.55, color[2] * 0.55, 1.0)
        if "Emission Strength" in bsdf.inputs:
            bsdf.inputs["Emission Strength"].default_value = emission_strength
    return material


def ensure_dir(path: Path) -> None:
    path.mkdir(parents=True, exist_ok=True)


def clamp(value: float) -> float:
    return max(0.0, min(1.0, value))


def deterministic_noise(x: int, y: int, seed: int) -> float:
    value = (x * 374761393 + y * 668265263 + seed * 2654435761) & 0xFFFFFFFF
    value = (value ^ (value >> 13)) * 1274126177 & 0xFFFFFFFF
    return ((value ^ (value >> 16)) & 0xFFFF) / 65535.0


def save_texture(path: Path, width: int, height: int, pixels: array) -> None:
    ensure_dir(path.parent)
    image = bpy.data.images.new(path.stem, width=width, height=height, alpha=True, float_buffer=False)
    image.pixels.foreach_set(pixels)
    image.filepath_raw = str(path)
    image.file_format = "PNG"
    image.save()
    bpy.data.images.remove(image)


def texture_paths(label: str) -> dict[str, Path]:
    return {
        "bc": TEXTURE_DIR / f"T_GIA_BloodAxeCairnSlabCluster_A01_FinalTrial_{label}_BC.png",
        "n": TEXTURE_DIR / f"T_GIA_BloodAxeCairnSlabCluster_A01_FinalTrial_{label}_N.png",
        "orm": TEXTURE_DIR / f"T_GIA_BloodAxeCairnSlabCluster_A01_FinalTrial_{label}_ORM.png",
    }


def generate_noise_texture_set(
    label: str,
    base: tuple[float, float, float],
    accent: tuple[float, float, float],
    seed: int,
    width: int = 1024,
    height: int = 1024,
    metallic: float = 0.0,
    roughness_base: float = 0.84,
) -> dict[str, Path]:
    bc = array("f")
    normal = array("f")
    orm = array("f")
    for y in range(height):
        for x in range(width):
            fine = deterministic_noise(x, y, seed)
            broad = deterministic_noise(x // 13, y // 11, seed + 19)
            vein = 1.0 if deterministic_noise(x // 41, y // 37, seed + 43) > 0.955 else 0.0
            chip = 1.0 if deterministic_noise(x // 17, y // 19, seed + 71) > 0.988 else 0.0
            mix = clamp(fine * 0.20 + broad * 0.34 + vein * 0.14 + chip * 0.12)
            color = (
                base[0] * (1.0 - mix) + accent[0] * mix,
                base[1] * (1.0 - mix) + accent[1] * mix,
                base[2] * (1.0 - mix) + accent[2] * mix,
            )
            if chip:
                color = (clamp(color[0] + 0.09), clamp(color[1] + 0.075), clamp(color[2] + 0.055))
            bc.extend((clamp(color[0]), clamp(color[1]), clamp(color[2]), 1.0))

            bump = (fine - 0.5) * 0.20 + (broad - 0.5) * 0.10
            normal.extend((clamp(0.5 + bump), clamp(0.5 + (deterministic_noise(x, y, seed + 101) - 0.5) * 0.14), 1.0, 1.0))
            occlusion = clamp(0.50 + (1.0 - broad) * 0.34)
            roughness = clamp(roughness_base + fine * 0.10)
            orm.extend((occlusion, roughness, metallic, 1.0))

    paths = texture_paths(label)
    save_texture(paths["bc"], width, height, bc)
    save_texture(paths["n"], width, height, normal)
    save_texture(paths["orm"], width, height, orm)
    return paths


def generate_a01_projection_texture_set(width: int = 1024, height: int = 1024) -> dict[str, Path]:
    source = bpy.data.images.load(str(A01_REFERENCE))
    source_width, source_height = source.size
    source_pixels = array("f", [0.0] * (source_width * source_height * 4))
    source.pixels.foreach_get(source_pixels)

    bc = array("f")
    normal = array("f")
    orm = array("f")
    for y in range(height):
        for x in range(width):
            u = x / max(1, width - 1)
            v = y / max(1, height - 1)
            sx = min(source_width - 1, max(0, int(u * (source_width - 1))))
            sy = min(source_height - 1, max(0, int(v * (source_height - 1))))
            idx = ((sy * source_width) + sx) * 4
            r = source_pixels[idx]
            g = source_pixels[idx + 1]
            b = source_pixels[idx + 2]
            a = source_pixels[idx + 3]
            saturation = max(r, g, b) - min(r, g, b)
            near_gray_bg = saturation < 0.055 and 0.34 < r < 0.76 and 0.34 < g < 0.76 and 0.34 < b < 0.76
            if near_gray_bg:
                noise = deterministic_noise(x // 5, y // 5, 5101)
                broad = deterministic_noise(x // 41, y // 37, 5102)
                r = 0.160 + broad * 0.12 + noise * 0.045
                g = 0.148 + broad * 0.105 + noise * 0.038
                b = 0.118 + broad * 0.085 + noise * 0.032
                a = 1.0
            else:
                # Compress the painted source into the darker Blood Axe stone range,
                # while keeping red paint and warm highlights legible.
                r = clamp(r * 0.98 + 0.050)
                g = clamp(g * 0.94 + 0.038)
                b = clamp(b * 0.88 + 0.030)
            bc.extend((r, g, b, a))

            fine = deterministic_noise(x, y, 5201)
            normal.extend((clamp(0.5 + (fine - 0.5) * 0.18), clamp(0.5 + (deterministic_noise(x, y, 5202) - 0.5) * 0.12), 1.0, 1.0))
            orm.extend((0.64, 0.89, 0.0, 1.0))

    paths = texture_paths("A1Projection")
    save_texture(paths["bc"], width, height, bc)
    save_texture(paths["n"], width, height, normal)
    save_texture(paths["orm"], width, height, orm)
    bpy.data.images.remove(source)
    return paths


def make_texture_material(
    name: str,
    textures: dict[str, Path],
    roughness: float,
    diffuse_color: tuple[float, float, float, float],
) -> bpy.types.Material:
    material = bpy.data.materials.new(name)
    material.diffuse_color = diffuse_color
    material.use_nodes = True
    nodes = material.node_tree.nodes
    bsdf = nodes.get("Principled BSDF")
    if bsdf is None:
        return material
    base = nodes.new(type="ShaderNodeTexImage")
    base.image = bpy.data.images.load(str(textures["bc"]))
    material.node_tree.links.new(base.outputs["Color"], bsdf.inputs["Base Color"])
    normal_texture = nodes.new(type="ShaderNodeTexImage")
    normal_texture.image = bpy.data.images.load(str(textures["n"]))
    normal_texture.image.colorspace_settings.name = "Non-Color"
    normal_map = nodes.new(type="ShaderNodeNormalMap")
    normal_map.inputs["Strength"].default_value = 0.30
    material.node_tree.links.new(normal_texture.outputs["Color"], normal_map.inputs["Color"])
    material.node_tree.links.new(normal_map.outputs["Normal"], bsdf.inputs["Normal"])
    bsdf.inputs["Roughness"].default_value = roughness
    bsdf.inputs["Metallic"].default_value = 0.0
    return material


def make_materials() -> dict[str, bpy.types.Material]:
    projection = generate_a01_projection_texture_set()
    stone = generate_noise_texture_set("Stone", (0.215, 0.205, 0.165), (0.74, 0.66, 0.48), 6101, roughness_base=0.88)
    stone_dark = generate_noise_texture_set("DarkStone", (0.135, 0.125, 0.100), (0.46, 0.41, 0.31), 6107, roughness_base=0.91)
    earth = generate_noise_texture_set("EarthAsh", (0.170, 0.102, 0.060), (0.48, 0.30, 0.16), 6113, roughness_base=0.94)
    rawhide = generate_noise_texture_set("Rawhide", (0.31, 0.145, 0.052), (0.75, 0.46, 0.16), 6119, roughness_base=0.83)
    paint = generate_noise_texture_set("BloodAxeRedPaint", (0.42, 0.024, 0.018), (0.92, 0.085, 0.045), 6121, roughness_base=0.81)
    return {
        "projection": make_texture_material("M_GIA_BloodAxeCairn_FinalTrial_A1Projection_A01", projection, 0.88, (0.30, 0.28, 0.23, 1.0)),
        "stone": make_texture_material("M_GIA_BloodAxeCairn_FinalTrial_Stone_A01", stone, 0.90, (0.18, 0.17, 0.14, 1.0)),
        "stone_dark": make_texture_material("M_GIA_BloodAxeCairn_FinalTrial_DarkStone_A01", stone_dark, 0.93, (0.10, 0.095, 0.08, 1.0)),
        "earth": make_texture_material("M_GIA_BloodAxeCairn_FinalTrial_EarthAsh_A01", earth, 0.95, (0.13, 0.08, 0.045, 1.0)),
        "paint": make_texture_material("M_GIA_BloodAxeCairn_FinalTrial_BloodAxeRedPaint_A01", paint, 0.82, (0.50, 0.035, 0.022, 1.0)),
        "rawhide": make_texture_material("M_GIA_BloodAxeCairn_FinalTrial_Rawhide_A01", rawhide, 0.84, (0.42, 0.22, 0.075, 1.0)),
        "stone_light": make_material("M_GIA_BloodAxeCairn_FinalTrial_StoneHighlight_A01", (0.62, 0.54, 0.40, 1.0), 0.9),
        "stone_crack": make_material("M_GIA_BloodAxeCairn_FinalTrial_StoneCrack_A01", (0.035, 0.030, 0.026, 1.0), 0.96, emission_strength=0.02),
        "guide_red": make_material("M_AET_PointGuide_Red_A01", (1.0, 0.02, 0.01, 1.0), 0.5, emission_strength=0.65),
        "guide_orange": make_material("M_AET_PointGuide_Orange_A01", (1.0, 0.38, 0.01, 1.0), 0.5, emission_strength=0.65),
        "guide_green": make_material("M_AET_PointGuide_Green_A01", (0.0, 0.95, 0.16, 1.0), 0.5, emission_strength=0.65),
        "guide_blue": make_material("M_AET_PointGuide_Blue_A01", (0.03, 0.16, 1.0, 1.0), 0.5, emission_strength=0.65),
        "guide_purple": make_material("M_AET_PointGuide_Purple_A01", (0.62, 0.05, 1.0, 1.0), 0.5, emission_strength=0.65),
        "collision": make_material("M_AET_CollisionProxy_ReviewOnly_A01", (0.1, 0.42, 0.95, 0.20), 0.5, emission_strength=0.25),
    }


def assign_world_uvs(obj: bpy.types.Object, scale: float = 0.010) -> None:
    if getattr(obj, "type", None) != "MESH":
        return
    uv_layer = obj.data.uv_layers.new(name="AET_WorldTextureUV") if not obj.data.uv_layers else obj.data.uv_layers[0]
    for poly in obj.data.polygons:
        normal = poly.normal
        for loop_index in poly.loop_indices:
            vert = obj.data.vertices[obj.data.loops[loop_index].vertex_index]
            world = obj.matrix_world @ vert.co
            if abs(normal.z) > max(abs(normal.x), abs(normal.y)):
                u = world.x * scale
                v = world.y * scale
            elif abs(normal.x) > abs(normal.y):
                u = world.y * scale
                v = world.z * scale
            else:
                u = world.x * scale
                v = world.z * scale
            uv_layer.data[loop_index].uv = (u % 1.0, v % 1.0)


def assign_a01_projection_uvs(obj: bpy.types.Object) -> None:
    if getattr(obj, "type", None) != "MESH":
        return
    uv_layer = obj.data.uv_layers.new(name="AET_A01FrontProjectionUV") if not obj.data.uv_layers else obj.data.uv_layers[0]
    x_span = PROJECTION_X_MAX - PROJECTION_X_MIN
    z_span = PROJECTION_Z_MAX - PROJECTION_Z_MIN
    for poly in obj.data.polygons:
        for loop_index in poly.loop_indices:
            vert = obj.data.vertices[obj.data.loops[loop_index].vertex_index]
            world = obj.matrix_world @ vert.co
            u = clamp((world.x - PROJECTION_X_MIN) / x_span)
            v = clamp((world.z - PROJECTION_Z_MIN) / z_span)
            uv_layer.data[loop_index].uv = (u, v)


def make_a01_surface_object(obj: bpy.types.Object, side_material: bpy.types.Material) -> None:
    if getattr(obj, "type", None) != "MESH":
        return
    if len(obj.data.materials) == 1:
        obj.data.materials.append(side_material)
    uv_layer = obj.data.uv_layers.new(name="AET_A01MixedFaceUV") if not obj.data.uv_layers else obj.data.uv_layers[0]
    x_span = PROJECTION_X_MAX - PROJECTION_X_MIN
    z_span = PROJECTION_Z_MAX - PROJECTION_Z_MIN
    normal_matrix = obj.matrix_world.to_3x3()
    for poly in obj.data.polygons:
        world_normal = (normal_matrix @ poly.normal).normalized()
        use_projection = world_normal.z > 0.36 or world_normal.y < -0.28
        poly.material_index = 0 if use_projection else 1
        for loop_index in poly.loop_indices:
            vert = obj.data.vertices[obj.data.loops[loop_index].vertex_index]
            world = obj.matrix_world @ vert.co
            if use_projection:
                u = clamp((world.x - PROJECTION_X_MIN) / x_span)
                v = clamp((world.z - PROJECTION_Z_MIN) / z_span)
            elif abs(world_normal.x) > abs(world_normal.y):
                u = (world.y * 0.012) % 1.0
                v = (world.z * 0.012) % 1.0
            else:
                u = (world.x * 0.012) % 1.0
                v = (world.z * 0.012) % 1.0
            uv_layer.data[loop_index].uv = (u, v)


def irregular_footprint(length: float, width: float, inset: float = 0.08) -> list[tuple[float, float]]:
    lx = length / 2.0
    wy = width / 2.0
    return [
        (-lx * (1.0 - RNG.uniform(0.0, inset)), -wy * (1.0 - RNG.uniform(0.0, inset))),
        (-lx * 0.18, -wy * (1.0 + RNG.uniform(0.0, inset))),
        (lx * (1.0 - RNG.uniform(0.0, inset)), -wy * (0.88 + RNG.uniform(0.0, inset))),
        (lx * (0.92 + RNG.uniform(0.0, inset)), wy * 0.18),
        (lx * (0.72 + RNG.uniform(0.0, inset)), wy * (0.94 + RNG.uniform(0.0, inset))),
        (lx * 0.10, wy * (0.82 + RNG.uniform(0.0, inset))),
        (-lx * (0.96 + RNG.uniform(0.0, inset)), wy * (0.88 + RNG.uniform(0.0, inset))),
        (-lx * (0.86 + RNG.uniform(0.0, inset)), -wy * 0.12),
    ]


def add_prism(
    name: str,
    length: float,
    width: float,
    height: float,
    location: tuple[float, float, float],
    rotation: tuple[float, float, float],
    material: bpy.types.Material,
    collection: bpy.types.Collection,
    bevel_width: float = 1.6,
    footprint: list[tuple[float, float]] | None = None,
) -> bpy.types.Object:
    points = footprint if footprint is not None else irregular_footprint(length, width)
    verts = [(x, y, -height / 2.0) for x, y in points] + [(x, y, height / 2.0) for x, y in points]
    count = len(points)
    faces: list[tuple[int, ...]] = [tuple(reversed(range(count))), tuple(range(count, count * 2))]
    for index in range(count):
        next_index = (index + 1) % count
        faces.append((index, next_index, count + next_index, count + index))

    mesh = bpy.data.meshes.new(f"{name}_Mesh")
    mesh.from_pydata(verts, [], faces)
    mesh.update()
    obj = bpy.data.objects.new(name, mesh)
    obj.location = location
    obj.rotation_euler = rotation
    obj.data.materials.append(material)
    obj["aet_local_height_cm"] = height
    obj["aet_local_length_cm"] = length
    obj["aet_local_width_cm"] = width
    collection.objects.link(obj)
    if bevel_width > 0:
        bevel = obj.modifiers.new("AET_TurnaroundEdgeWear", "BEVEL")
        bevel.width = bevel_width
        bevel.segments = 1
        try:
            bevel.affect = "EDGES"
        except TypeError:
            pass
        set_active(obj)
        bpy.ops.object.modifier_apply(modifier=bevel.name)
    normal = obj.modifiers.new("AET_TurnaroundWeightedNormals", "WEIGHTED_NORMAL")
    set_active(obj)
    bpy.ops.object.modifier_apply(modifier=normal.name)
    assign_world_uvs(obj)
    return obj


def add_vertical_profile_slab(
    name: str,
    profile_xz: list[tuple[float, float]],
    depth: float,
    location: tuple[float, float, float],
    rotation: tuple[float, float, float],
    material: bpy.types.Material,
    collection: bpy.types.Collection,
    bevel_width: float = 1.6,
) -> bpy.types.Object:
    verts = [(x, -depth / 2.0, z) for x, z in profile_xz] + [(x, depth / 2.0, z) for x, z in profile_xz]
    count = len(profile_xz)
    faces: list[tuple[int, ...]] = [tuple(range(count)), tuple(reversed(range(count, count * 2)))]
    for index in range(count):
        next_index = (index + 1) % count
        faces.append((index, next_index, count + next_index, count + index))
    mesh = bpy.data.meshes.new(f"{name}_Mesh")
    mesh.from_pydata(verts, [], faces)
    mesh.update()
    obj = bpy.data.objects.new(name, mesh)
    obj.location = location
    obj.rotation_euler = rotation
    obj.data.materials.append(material)
    obj["aet_local_depth_cm"] = depth
    obj["aet_profile_min_x_cm"] = min(x for x, _z in profile_xz)
    obj["aet_profile_max_x_cm"] = max(x for x, _z in profile_xz)
    obj["aet_profile_min_z_cm"] = min(z for _x, z in profile_xz)
    obj["aet_profile_max_z_cm"] = max(z for _x, z in profile_xz)
    collection.objects.link(obj)
    if bevel_width > 0:
        bevel = obj.modifiers.new("AET_TurnaroundBrokenEdgeWear", "BEVEL")
        bevel.width = bevel_width
        bevel.segments = 1
        try:
            bevel.affect = "EDGES"
        except TypeError:
            pass
        set_active(obj)
        bpy.ops.object.modifier_apply(modifier=bevel.name)
    normal = obj.modifiers.new("AET_TurnaroundProfileWeightedNormals", "WEIGHTED_NORMAL")
    set_active(obj)
    bpy.ops.object.modifier_apply(modifier=normal.name)
    assign_world_uvs(obj)
    return obj


def add_earth_base(material: bpy.types.Material, collection: bpy.types.Collection, detail: int) -> bpy.types.Object:
    segments = 48 if detail == 0 else 28
    radius_x = 181.0
    radius_y = 111.0
    height = 7.0
    verts = []
    for z in (-height / 2.0, height / 2.0):
        for index in range(segments):
            angle = (index / segments) * math.tau
            noise = 0.88 + RNG.random() * 0.20
            verts.append((math.cos(angle) * radius_x * noise, math.sin(angle) * radius_y * noise, z))
    faces: list[tuple[int, ...]] = [tuple(reversed(range(segments))), tuple(range(segments, segments * 2))]
    for index in range(segments):
        next_index = (index + 1) % segments
        faces.append((index, next_index, segments + next_index, segments + index))
    mesh = bpy.data.meshes.new("A1_Turnaround_AshMudBase_Mesh")
    mesh.from_pydata(verts, [], faces)
    mesh.update()
    obj = bpy.data.objects.new("A1_Turnaround_AshMudBase", mesh)
    obj.location = (0.0, -4.0, 2.5)
    obj.data.materials.append(material)
    collection.objects.link(obj)
    assign_world_uvs(obj)
    return obj


def add_paint_strip(
    slab: bpy.types.Object,
    name: str,
    local_xy: tuple[float, float],
    size_xy: tuple[float, float],
    yaw: float,
    material: bpy.types.Material,
    collection: bpy.types.Collection,
) -> bpy.types.Object:
    height = float(slab.get("aet_local_height_cm", 8.0))
    cx, cy = local_xy
    sx, sy = size_xy[0] / 2.0, size_xy[1] / 2.0
    cos_y = math.cos(yaw)
    sin_y = math.sin(yaw)
    base = [(-sx, -sy), (sx, -sy), (sx, sy), (-sx, sy)]
    verts = []
    for x, y in base:
        rx = cx + x * cos_y - y * sin_y
        ry = cy + x * sin_y + y * cos_y
        verts.append((rx, ry, height / 2.0 + 0.22))
    mesh = bpy.data.meshes.new(f"{name}_Mesh")
    mesh.from_pydata(verts, [], [(0, 1, 2, 3)])
    mesh.update()
    obj = bpy.data.objects.new(name, mesh)
    obj.location = slab.location
    obj.rotation_euler = slab.rotation_euler
    obj.data.materials.append(material)
    collection.objects.link(obj)
    assign_world_uvs(obj)
    return obj


def add_front_face_paint(
    slab: bpy.types.Object,
    name: str,
    local_xz: tuple[float, float],
    size_xz: tuple[float, float],
    depth: float,
    yaw: float,
    material: bpy.types.Material,
    collection: bpy.types.Collection,
) -> bpy.types.Object:
    cx, cz = local_xz
    sx, sz = size_xz[0] / 2.0, size_xz[1] / 2.0
    cos_y = math.cos(yaw)
    sin_y = math.sin(yaw)
    base = [(-sx, -sz), (sx, -sz), (sx, sz), (-sx, sz)]
    verts = []
    for x, z in base:
        rx = cx + x * cos_y - z * sin_y
        rz = cz + x * sin_y + z * cos_y
        verts.append((rx, -depth / 2.0 - 0.32, rz))
    mesh = bpy.data.meshes.new(f"{name}_Mesh")
    mesh.from_pydata(verts, [], [(0, 1, 2, 3)])
    mesh.update()
    obj = bpy.data.objects.new(name, mesh)
    obj.location = slab.location
    obj.rotation_euler = slab.rotation_euler
    obj.data.materials.append(material)
    collection.objects.link(obj)
    assign_world_uvs(obj)
    return obj


def add_top_surface_details(
    slab: bpy.types.Object,
    prefix: str,
    materials: dict[str, bpy.types.Material],
    collection: bpy.types.Collection,
    crack_count: int,
    highlight_count: int,
    seed: int,
) -> list[bpy.types.Object]:
    detail_rng = random.Random(seed)
    length = float(slab.get("aet_local_length_cm", 80.0))
    width = float(slab.get("aet_local_width_cm", 32.0))
    objects: list[bpy.types.Object] = []
    for index in range(crack_count):
        x = detail_rng.uniform(-length * 0.38, length * 0.38)
        y = detail_rng.uniform(-width * 0.32, width * 0.32)
        objects.append(
            add_paint_strip(
                slab,
                f"{prefix}_DarkCrack_{index:02d}",
                (x, y),
                (detail_rng.uniform(10.0, 34.0), detail_rng.uniform(0.8, 1.7)),
                detail_rng.uniform(-0.95, 0.95),
                materials["stone_crack"],
                collection,
            )
        )
    for index in range(highlight_count):
        x = detail_rng.uniform(-length * 0.40, length * 0.40)
        y = detail_rng.uniform(-width * 0.38, width * 0.38)
        objects.append(
            add_paint_strip(
                slab,
                f"{prefix}_WarmEdgeHighlight_{index:02d}",
                (x, y),
                (detail_rng.uniform(9.0, 28.0), detail_rng.uniform(0.9, 1.9)),
                detail_rng.uniform(-0.85, 0.85),
                materials["stone_light"],
                collection,
            )
        )
    return objects


def add_front_surface_details(
    slab: bpy.types.Object,
    prefix: str,
    materials: dict[str, bpy.types.Material],
    collection: bpy.types.Collection,
    crack_count: int,
    highlight_count: int,
    seed: int,
) -> list[bpy.types.Object]:
    detail_rng = random.Random(seed)
    min_x = float(slab.get("aet_profile_min_x_cm", -24.0))
    max_x = float(slab.get("aet_profile_max_x_cm", 24.0))
    min_z = float(slab.get("aet_profile_min_z_cm", -42.0))
    max_z = float(slab.get("aet_profile_max_z_cm", 54.0))
    depth = float(slab.get("aet_local_depth_cm", 20.0))
    objects: list[bpy.types.Object] = []
    for index in range(crack_count):
        objects.append(
            add_front_face_paint(
                slab,
                f"{prefix}_FaceDarkCrack_{index:02d}",
                (detail_rng.uniform(min_x * 0.70, max_x * 0.70), detail_rng.uniform(min_z * 0.30, max_z * 0.74)),
                (detail_rng.uniform(1.2, 2.6), detail_rng.uniform(14.0, 38.0)),
                depth,
                detail_rng.uniform(-0.34, 0.34),
                materials["stone_crack"],
                collection,
            )
        )
    for index in range(highlight_count):
        objects.append(
            add_front_face_paint(
                slab,
                f"{prefix}_FaceWarmHighlight_{index:02d}",
                (detail_rng.uniform(min_x * 0.72, max_x * 0.72), detail_rng.uniform(min_z * 0.15, max_z * 0.78)),
                (detail_rng.uniform(1.4, 2.8), detail_rng.uniform(12.0, 32.0)),
                depth,
                detail_rng.uniform(-0.28, 0.28),
                materials["stone_light"],
                collection,
            )
        )
    return objects


def cylinder_between(
    name: str,
    start: Vector,
    end: Vector,
    radius: float,
    material: bpy.types.Material,
    collection: bpy.types.Collection,
    vertices: int = 8,
) -> bpy.types.Object:
    direction = end - start
    center = start + direction * 0.5
    bpy.ops.mesh.primitive_cylinder_add(vertices=vertices, radius=radius, depth=direction.length, location=center)
    obj = bpy.context.object
    obj.name = name
    obj.rotation_euler = direction.to_track_quat("Z", "Y").to_euler()
    obj.data.materials.append(material)
    link_to_collection(obj, collection)
    assign_world_uvs(obj)
    return obj


def local_to_world(obj: bpy.types.Object, local: tuple[float, float, float]) -> Vector:
    return obj.matrix_world @ Vector(local)


def add_lashing_on_slab(
    slab: bpy.types.Object,
    name: str,
    local_x: float,
    material: bpy.types.Material,
    collection: bpy.types.Collection,
    length: float,
    width: float,
    height: float,
) -> list[bpy.types.Object]:
    z = height / 2.0 + 1.1
    y0 = -width * 0.56
    y1 = width * 0.56
    offset = 2.6
    pieces = [
        cylinder_between(
            f"{name}_CordA",
            local_to_world(slab, (local_x - offset, y0, z)),
            local_to_world(slab, (local_x - offset, y1, z)),
            1.65,
            material,
            collection,
        ),
        cylinder_between(
            f"{name}_CordB",
            local_to_world(slab, (local_x + offset, y0, z)),
            local_to_world(slab, (local_x + offset, y1, z)),
            1.65,
            material,
            collection,
        ),
    ]
    for y in (y0, y1):
        pieces.append(
            cylinder_between(
                f"{name}_EdgeTie_{len(pieces)}",
                local_to_world(slab, (local_x - offset, y, z)),
                local_to_world(slab, (local_x + offset, y, z)),
                1.25,
                material,
                collection,
            )
        )
    return pieces


def add_pebbles(material: bpy.types.Material, collection: bpy.types.Collection, count: int) -> list[bpy.types.Object]:
    pebbles: list[bpy.types.Object] = []
    for index in range(count):
        angle = RNG.random() * math.tau
        radius = 40.0 + RNG.random() * 130.0
        x = math.cos(angle) * radius * (0.95 + RNG.random() * 0.18)
        y = math.sin(angle) * radius * 0.58 - 3.0
        if -62.0 < x < 78.0 and -46.0 < y < 47.0 and RNG.random() < 0.65:
            continue
        length = RNG.uniform(8.0, 23.0)
        width = RNG.uniform(6.0, 17.0)
        height = RNG.uniform(4.0, 11.0)
        pebble = add_prism(
            f"A1_Turnaround_Pebble_{index:02d}",
            length,
            width,
            height,
            (x, y, height / 2.0 + RNG.uniform(0.0, 2.0)),
            (RNG.uniform(-0.12, 0.12), RNG.uniform(-0.08, 0.08), RNG.uniform(0.0, math.tau)),
            material,
            collection,
            bevel_width=0.7,
        )
        pebbles.append(pebble)
    return pebbles


def add_guide_markers(materials: dict[str, bpy.types.Material], collection: bpy.types.Collection) -> None:
    palette = [
        materials["guide_red"],
        materials["guide_orange"],
        materials["guide_green"],
        materials["guide_blue"],
        materials["guide_purple"],
    ]
    for index, (point_id, coords) in enumerate(POINTS.items()):
        bpy.ops.mesh.primitive_uv_sphere_add(segments=12, ring_count=6, radius=4.0, location=coords)
        marker = bpy.context.object
        marker.name = f"GUIDE_{point_id}"
        marker.data.materials.append(palette[index % len(palette)])
        link_to_collection(marker, collection)


def build_asset_collection(
    collection: bpy.types.Collection,
    materials: dict[str, bpy.types.Material],
    detail: int,
) -> list[bpy.types.Object]:
    return build_asset_collection_a01_cairn(collection, materials, detail)


def build_asset_collection_a01_cairn(
    collection: bpy.types.Collection,
    materials: dict[str, bpy.types.Material],
    detail: int,
) -> list[bpy.types.Object]:
    objects: list[bpy.types.Object] = []
    objects.append(add_earth_base(materials["earth"], collection, detail))

    include_minor = detail <= 1
    include_paint = detail <= 2
    include_lashings = detail <= 1
    pebble_count = {0: 82, 1: 34, 2: 12, 3: 4}[detail]

    central = add_vertical_profile_slab(
        "A1_FinalA01_CentralLeaningPaintedSlab",
        [
            (-67.0, -72.0),
            (-37.0, -78.0),
            (22.0, -72.0),
            (62.0, -50.0),
            (72.0, 18.0),
            (48.0, 76.0),
            (16.0, 88.0),
            (-16.0, 74.0),
            (-50.0, 15.0),
        ],
        32.0,
        (0.0, -23.0, 84.0),
        (math.radians(9.0), math.radians(-7.0), math.radians(-9.0)),
        materials["projection"] if detail == 0 else materials["stone"],
        collection,
        bevel_width=1.2,
    )
    if detail == 0:
        make_a01_surface_object(central, materials["stone"])
    objects.append(central)

    rear = add_vertical_profile_slab(
        "A1_FinalA01_RearTallShard",
        [(-30.0, -64.0), (28.0, -67.0), (35.0, 42.0), (13.0, 87.0), (-16.0, 72.0), (-33.0, 7.0)],
        25.0,
        (34.0, 20.0, 84.0),
        (math.radians(-5.0), math.radians(9.0), math.radians(8.0)),
        materials["projection"] if detail == 0 else materials["stone_dark"],
        collection,
        bevel_width=1.0,
    )
    if detail == 0:
        make_a01_surface_object(rear, materials["stone_dark"])
    objects.append(rear)

    right = add_vertical_profile_slab(
        "A1_FinalA01_RightUprightShard",
        [(-25.0, -51.0), (27.0, -48.0), (31.0, 24.0), (18.0, 57.0), (-15.0, 49.0), (-31.0, -18.0)],
        28.0,
        (102.0, -3.0, 63.0),
        (math.radians(2.0), math.radians(-7.0), math.radians(-10.0)),
        materials["projection"] if detail == 0 else materials["stone"],
        collection,
        bevel_width=0.9,
    )
    if detail == 0:
        make_a01_surface_object(right, materials["stone"])
    objects.append(right)

    left_front = add_prism(
        "A1_FinalA01_LeftFrontBrokenStack",
        106.0,
        42.0,
        24.0,
        (-108.0, -35.0, 25.0),
        (math.radians(2.0), math.radians(3.0), math.radians(-15.0)),
        materials["projection"] if detail == 0 else materials["stone"],
        collection,
        bevel_width=0.7,
        footprint=[
            (-58.0, -18.0),
            (-28.0, -25.0),
            (23.0, -22.0),
            (58.0, -13.0),
            (56.0, 8.0),
            (38.0, 23.0),
            (-18.0, 19.0),
            (-61.0, 9.0),
        ],
    )
    if detail == 0:
        make_a01_surface_object(left_front, materials["stone"])
    objects.append(left_front)

    left_top: bpy.types.Object | None = None
    if detail <= 2:
        left_top = add_prism(
            "A1_FinalA01_LeftFrontCapStone",
            76.0,
            32.0,
            18.0,
            (-104.0, -39.0, 48.0),
            (math.radians(-3.0), math.radians(2.0), math.radians(-10.0)),
            materials["projection"] if detail == 0 else materials["stone"],
            collection,
            bevel_width=0.6,
            footprint=[
                (-45.0, -14.0),
                (-16.0, -18.0),
                (42.0, -12.0),
                (45.0, 5.0),
                (22.0, 18.0),
                (-31.0, 15.0),
                (-47.0, 2.0),
            ],
        )
        if detail == 0:
            make_a01_surface_object(left_top, materials["stone"])
        objects.append(left_top)

    if include_minor:
        left_rear = add_vertical_profile_slab(
            "A1_FinalA01_LeftRearNarrowShard",
            [(-18.0, -43.0), (17.0, -43.0), (20.0, 32.0), (4.0, 56.0), (-18.0, 21.0)],
            18.0,
            (-52.0, 18.0, 68.0),
            (math.radians(-5.0), math.radians(12.0), math.radians(10.0)),
            materials["stone_dark"],
            collection,
            bevel_width=1.4,
        )
        center_shard = add_vertical_profile_slab(
            "A1_FinalA01_CenterNeedleShard",
            [(-12.0, -47.0), (14.0, -48.0), (16.0, 38.0), (2.0, 61.0), (-12.0, 27.0)],
            15.0,
            (-13.0, 10.0, 72.0),
            (math.radians(-8.0), math.radians(-5.0), math.radians(-3.0)),
            materials["stone_dark"],
            collection,
            bevel_width=1.2,
        )
        right_support = add_prism(
            "A1_FinalA01_RightGroundSupportStone",
            48.0,
            28.0,
            24.0,
            (127.0, -35.0, 18.0),
            (math.radians(1.0), math.radians(-4.0), math.radians(11.0)),
            materials["stone"],
            collection,
            bevel_width=0.7,
            footprint=[
                (-23.0, -11.0),
                (-6.0, -14.0),
                (22.0, -8.0),
                (20.0, 8.0),
                (6.0, 13.0),
                (-22.0, 8.0),
            ],
        )
        rear_root = add_prism(
            "A1_FinalA01_BackRootStone",
            72.0,
            40.0,
            25.0,
            (4.0, 54.0, 21.0),
            (math.radians(0.0), math.radians(4.0), math.radians(12.0)),
            materials["stone"],
            collection,
            bevel_width=0.6,
            footprint=[
                (-36.0, -16.0),
                (-8.0, -21.0),
                (34.0, -13.0),
                (36.0, 9.0),
                (12.0, 20.0),
                (-33.0, 13.0),
            ],
        )
        objects.extend([left_rear, center_shard, right_support, rear_root])

    if include_paint:
        paint_objects = [
            add_front_face_paint(central, "A1_FinalA01_CentralPaint_LongDiagonal", (-2.0, -4.0), (142.0, 13.0), 32.0, math.radians(18.0), materials["paint"], collection),
            add_front_face_paint(central, "A1_FinalA01_CentralPaint_CrossA", (-35.0, 12.0), (72.0, 10.5), 32.0, math.radians(-34.0), materials["paint"], collection),
            add_front_face_paint(central, "A1_FinalA01_CentralPaint_CrossB", (32.0, 10.0), (66.0, 10.0), 32.0, math.radians(-27.0), materials["paint"], collection),
            add_front_face_paint(central, "A1_FinalA01_CentralPaint_LowerBrokenTail", (52.0, -30.0), (46.0, 7.5), 32.0, math.radians(10.0), materials["paint"], collection),
            add_front_face_paint(central, "A1_FinalA01_CentralStoneHighlightA", (-48.0, 45.0), (7.0, 54.0), 32.0, math.radians(-8.0), materials["stone_light"], collection),
            add_front_face_paint(central, "A1_FinalA01_CentralStoneHighlightB", (42.0, 32.0), (6.0, 42.0), 32.0, math.radians(11.0), materials["stone_light"], collection),
            add_front_face_paint(central, "A1_FinalA01_CentralStoneCrackA", (-20.0, 17.0), (4.0, 74.0), 32.0, math.radians(17.0), materials["stone_crack"], collection),
            add_front_face_paint(central, "A1_FinalA01_CentralStoneCrackB", (52.0, -4.0), (3.2, 52.0), 32.0, math.radians(-24.0), materials["stone_crack"], collection),
            add_front_face_paint(rear, "A1_FinalA01_RearPaintSlash", (0.0, 11.0), (17.0, 78.0), 25.0, math.radians(-13.0), materials["paint"], collection),
            add_front_face_paint(rear, "A1_FinalA01_RearStoneHighlight", (-13.0, 18.0), (6.0, 76.0), 25.0, math.radians(-6.0), materials["stone_light"], collection),
            add_front_face_paint(right, "A1_FinalA01_RightStoneCrack", (5.0, 7.0), (3.6, 52.0), 28.0, math.radians(5.0), materials["stone_crack"], collection),
        ]
        if detail == 0:
            paint_objects.extend(add_top_surface_details(left_front, "A1_Turnaround_LeftBase", materials, collection, 8, 5, 9302))
            if left_top is not None:
                paint_objects.extend(add_top_surface_details(left_top, "A1_Turnaround_LeftCap", materials, collection, 6, 4, 9303))
            paint_objects.extend(add_front_surface_details(rear, "A1_Turnaround_RearTallSlab", materials, collection, 10, 6, 9304))
            paint_objects.extend(add_front_surface_details(right, "A1_Turnaround_RightUpright", materials, collection, 7, 4, 9305))
        elif detail == 1:
            paint_objects.extend(add_top_surface_details(central, "A1_Turnaround_MainSlab_LOD1", materials, collection, 3, 1, 9311))
            paint_objects.extend(add_front_surface_details(rear, "A1_Turnaround_RearTallSlab_LOD1", materials, collection, 2, 1, 9312))
        objects.extend(paint_objects)

    if include_lashings:
        lashings = [
            ("A1_FinalA01_Lashing_LeftLoopA", (-82.0, -49.0, 56.0), (-115.0, 12.0, 45.0), 1.75),
            ("A1_FinalA01_Lashing_LeftLoopB", (-76.0, -48.0, 51.0), (-110.0, 13.0, 39.0), 1.55),
            ("A1_FinalA01_Lashing_RightLoopA", (60.0, -49.0, 60.0), (113.0, 10.0, 56.0), 1.85),
            ("A1_FinalA01_Lashing_RightLoopB", (65.0, -49.0, 54.0), (116.0, 10.0, 50.0), 1.55),
            ("A1_FinalA01_RearTieCord", (-18.0, 4.0, 98.0), (61.0, 14.0, 102.0), 1.45),
        ]
        for name, start, end, radius in lashings:
            objects.append(cylinder_between(name, Vector(start), Vector(end), radius, materials["rawhide"], collection))

    objects.extend(add_pebbles(materials["stone"], collection, pebble_count))
    return objects


def add_collision_proxy(material: bpy.types.Material, collection: bpy.types.Collection) -> bpy.types.Object:
    bpy.ops.mesh.primitive_cube_add(size=1.0, location=(0.0, -2.0, 82.0))
    obj = bpy.context.object
    obj.name = f"UCX_{ASSET_NAME}_00"
    obj.dimensions = (365.0, 215.0, 180.0)
    obj.data.materials.append(material)
    set_active(obj)
    bpy.ops.object.transform_apply(location=False, rotation=False, scale=True)
    obj.display_type = "WIRE"
    obj.hide_render = True
    link_to_collection(obj, collection)
    return obj


def object_triangle_count(obj: bpy.types.Object) -> int:
    if getattr(obj, "type", None) != "MESH":
        return 0
    obj.data.calc_loop_triangles()
    return len(obj.data.loop_triangles)


def collection_triangle_count(collection: bpy.types.Collection) -> int:
    return sum(object_triangle_count(obj) for obj in collection.objects)


def collection_bounds(collection: bpy.types.Collection) -> tuple[float, float, float]:
    points: list[Vector] = []
    for obj in collection.objects:
        if getattr(obj, "type", None) != "MESH" or obj.name.startswith("GUIDE_"):
            continue
        points.extend(obj.matrix_world @ Vector(corner) for corner in obj.bound_box)
    if not points:
        return 0.0, 0.0, 0.0
    return (
        max(point.x for point in points) - min(point.x for point in points),
        max(point.y for point in points) - min(point.y for point in points),
        max(point.z for point in points) - min(point.z for point in points),
    )


def export_selected_fbx(path: Path, objects: list[bpy.types.Object]) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    bpy.ops.object.select_all(action="DESELECT")
    for obj in objects:
        obj.hide_viewport = False
        obj.hide_set(False)
        obj.select_set(True)
        for collection in obj.users_collection:
            collection.hide_viewport = False
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


def make_joined_export_object(objects: list[bpy.types.Object]) -> bpy.types.Object:
    duplicates: list[bpy.types.Object] = []
    export_collection = make_collection(f"{ASSET_NAME}_FBXJoinedExport_Work")
    for obj in objects:
        if getattr(obj, "type", None) != "MESH":
            continue
        duplicate = obj.copy()
        duplicate.data = obj.data.copy()
        duplicate.matrix_world = obj.matrix_world.copy()
        duplicate.name = f"{obj.name}_FBXJoinCopy"
        export_collection.objects.link(duplicate)
        duplicates.append(duplicate)

    if not duplicates:
        raise RuntimeError("No mesh objects available for joined FBX export")

    bpy.ops.object.select_all(action="DESELECT")
    for duplicate in duplicates:
        duplicate.hide_viewport = False
        duplicate.hide_set(False)
        duplicate.select_set(True)
    bpy.context.view_layer.objects.active = duplicates[0]
    bpy.ops.object.join()
    joined = bpy.context.object
    joined.name = ASSET_NAME
    joined.data.name = f"{ASSET_NAME}_Mesh"
    joined["aet_export_joined_source"] = "true"
    return joined


def remove_object_and_mesh(obj: bpy.types.Object) -> None:
    mesh = obj.data if getattr(obj, "type", None) == "MESH" else None
    bpy.data.objects.remove(obj, do_unlink=True)
    if mesh is not None and mesh.users == 0:
        bpy.data.meshes.remove(mesh)


def export_game_fbx(path: Path, visual_objects: list[bpy.types.Object], collision: bpy.types.Object) -> None:
    joined = make_joined_export_object(visual_objects)
    try:
        export_selected_fbx(path, [joined, collision])
    finally:
        remove_object_and_mesh(joined)


def add_review_lighting() -> None:
    scene = bpy.context.scene
    try:
        scene.render.engine = "BLENDER_EEVEE_NEXT"
    except TypeError:
        try:
            scene.render.engine = "BLENDER_EEVEE"
        except TypeError:
            scene.render.engine = "BLENDER_WORKBENCH"
    shading = scene.display.shading
    for attr, value in (
        ("light", "STUDIO"),
        ("color_type", "MATERIAL"),
        ("background_type", "VIEWPORT"),
        ("show_cavity", True),
        ("show_shadows", True),
    ):
        if hasattr(shading, attr):
            try:
                setattr(shading, attr, value)
            except TypeError:
                pass
    if hasattr(shading, "background_color"):
        shading.background_color = (0.62, 0.60, 0.56)
    try:
        scene.view_settings.view_transform = "Standard"
    except TypeError:
        pass
    scene.view_settings.exposure = 1.15
    scene.view_settings.gamma = 1.0
    if scene.world is not None:
        scene.world.color = (0.56, 0.55, 0.52)
    lights = [
        ("AET_KeyLight_A01", "AREA", (-290.0, -380.0, 430.0), 118000.0, 520.0),
        ("AET_FillLight_A01", "AREA", (280.0, -210.0, 220.0), 62000.0, 620.0),
        ("AET_RimLight_A01", "POINT", (0.0, 260.0, 210.0), 22000.0, 0.0),
        ("AET_TopSoftLight_A01", "AREA", (0.0, 0.0, 540.0), 52000.0, 700.0),
    ]
    for name, kind, location, energy, size in lights:
        data = bpy.data.lights.new(name, type=kind)
        data.energy = energy
        if kind == "AREA":
            data.size = size
        obj = bpy.data.objects.new(name, data)
        obj.location = location
        bpy.context.scene.collection.objects.link(obj)


def set_camera_for_review(name: str, location: tuple[float, float, float], target: tuple[float, float, float], ortho_scale: float) -> None:
    scene = bpy.context.scene
    bpy.ops.object.camera_add(location=location)
    camera = bpy.context.object
    camera.name = name
    direction = Vector(target) - Vector(location)
    camera.rotation_euler = direction.to_track_quat("-Z", "Y").to_euler()
    camera.data.type = "ORTHO"
    camera.data.ortho_scale = ortho_scale
    camera.data.clip_start = 1
    camera.data.clip_end = 5000
    scene.camera = camera


def blit_resized_image_to_board(
    board: array,
    board_width: int,
    board_height: int,
    tile_width: int,
    tile_height: int,
    row: int,
    col: int,
    source_path: Path,
) -> None:
    image = bpy.data.images.load(str(source_path))
    src_width, src_height = image.size
    pixels = array("f", [0.0] * (src_width * src_height * 4))
    image.pixels.foreach_get(pixels)

    scale = min(tile_width / src_width, tile_height / src_height)
    draw_width = max(1, int(src_width * scale))
    draw_height = max(1, int(src_height * scale))
    x_pad = (tile_width - draw_width) // 2
    y_pad = (tile_height - draw_height) // 2
    x_offset = col * tile_width + x_pad
    y_offset = (board_height - ((row + 1) * tile_height)) + y_pad

    for y in range(draw_height):
        src_y = min(src_height - 1, int(y / scale))
        for x in range(draw_width):
            src_x = min(src_width - 1, int(x / scale))
            src_index = ((src_y * src_width) + src_x) * 4
            dst_index = (((y + y_offset) * board_width) + (x + x_offset)) * 4
            board[dst_index : dst_index + 4] = pixels[src_index : src_index + 4]
    bpy.data.images.remove(image)


def compose_final_review_board(render_paths: list[Path]) -> Path:
    tile_width = 800
    tile_height = 600
    cols = 3
    rows = 2
    board_width = tile_width * cols
    board_height = tile_height * rows
    board = array("f")
    for _ in range(board_width * board_height):
        board.extend((0.56, 0.55, 0.52, 1.0))

    board_inputs = [A01_REFERENCE] + render_paths
    for index, path in enumerate(board_inputs[: cols * rows]):
        blit_resized_image_to_board(
            board,
            board_width,
            board_height,
            tile_width,
            tile_height,
            index // cols,
            index % cols,
            path,
        )

    output_path = REVIEW_ROOT / f"{ASSET_NAME}_FinalGameReadyReviewBoard.png"
    board_image = bpy.data.images.new(output_path.stem, width=board_width, height=board_height, alpha=True, float_buffer=False)
    board_image.pixels.foreach_set(board)
    board_image.filepath_raw = str(output_path)
    board_image.file_format = "PNG"
    board_image.save()
    bpy.data.images.remove(board_image)
    return output_path


def render_reviews(lod0_collection: bpy.types.Collection, guide_collection: bpy.types.Collection) -> None:
    REVIEW_ROOT.mkdir(parents=True, exist_ok=True)
    scene = bpy.context.scene
    scene.render.resolution_x = 1280
    scene.render.resolution_y = 900

    guide_collection.hide_render = True
    reviews = [
        ("Front", (330.0, -560.0, 210.0), (0.0, 0.0, 60.0), 390.0),
        ("Beauty", (360.0, -520.0, 250.0), (0.0, -4.0, 64.0), 410.0),
        ("Right", (560.0, 0.0, 210.0), (0.0, 0.0, 62.0), 390.0),
        ("Back", (-330.0, 560.0, 210.0), (0.0, 0.0, 62.0), 390.0),
        ("Top", (0.0, 0.0, 720.0), (0.0, 0.0, 0.0), 410.0),
    ]
    render_paths: list[Path] = []
    for label, location, target, scale in reviews:
        set_camera_for_review(f"AET_{label}ReviewCamera", location, target, scale)
        render_path = REVIEW_ROOT / f"{ASSET_NAME}_{label}Review.png"
        scene.render.filepath = str(render_path)
        bpy.ops.render.render(write_still=True)
        render_paths.append(render_path)
    compose_final_review_board(render_paths)

    guide_collection.hide_render = False
    set_camera_for_review("AET_GuidePointReviewCamera", (360.0, -520.0, 250.0), (0.0, -4.0, 64.0), 410.0)
    scene.render.filepath = str(REVIEW_ROOT / f"{ASSET_NAME}_GuidePointReview.png")
    bpy.ops.render.render(write_still=True)


def build() -> None:
    clear_scene()
    setup_scene()
    add_review_lighting()
    materials = make_materials()

    lod0_collection = make_collection(f"{ASSET_NAME}_LOD0_FinalTrial")
    lod1_collection = make_collection(f"{ASSET_NAME}_LOD1_FinalTrial", hidden=True)
    lod2_collection = make_collection(f"{ASSET_NAME}_LOD2_FinalTrial", hidden=True)
    lod3_collection = make_collection(f"{ASSET_NAME}_LOD3_FinalTrial", hidden=True)
    guide_collection = make_collection(f"{ASSET_NAME}_GuidePoints", hidden=False)
    collision_collection = make_collection(f"{ASSET_NAME}_Collision_Source", hidden=True)

    lod0_objects = build_asset_collection(lod0_collection, materials, 0)
    lod1_objects = build_asset_collection(lod1_collection, materials, 1)
    lod2_objects = build_asset_collection(lod2_collection, materials, 2)
    lod3_objects = build_asset_collection(lod3_collection, materials, 3)
    collision = add_collision_proxy(materials["collision"], collision_collection)
    add_guide_markers(materials, guide_collection)

    add_asset_metadata(
        ASSET_NAME,
        "Final-trial Blood Axe cairn static prop built from A01 with real 360 stone volumes, A01-guided front projection material, texture maps, LOD exports, and collision. Pending Flamestrike aesthetic review after complete package validation.",
        UNREAL_PATH,
    )

    blend_path = BLENDER_ROOT / REL_PATH / f"{ASSET_NAME}.blend"
    export_path = EXPORT_ROOT / REL_PATH / f"{ASSET_NAME}.fbx"
    blend_path.parent.mkdir(parents=True, exist_ok=True)
    export_path.parent.mkdir(parents=True, exist_ok=True)
    TEXTURE_DIR.mkdir(parents=True, exist_ok=True)

    render_reviews(lod0_collection, guide_collection)
    bpy.ops.wm.save_as_mainfile(filepath=str(blend_path))

    export_game_fbx(export_path, lod0_objects, collision)
    export_selected_fbx(export_path.with_name(f"{ASSET_NAME}_LOD0.fbx"), lod0_objects)
    export_selected_fbx(export_path.with_name(f"{ASSET_NAME}_LOD1.fbx"), lod1_objects)
    export_selected_fbx(export_path.with_name(f"{ASSET_NAME}_LOD2.fbx"), lod2_objects)
    export_selected_fbx(export_path.with_name(f"{ASSET_NAME}_LOD3.fbx"), lod3_objects)

    width, depth, height = collection_bounds(lod0_collection)
    print(f"Built {blend_path.relative_to(ROOT)}")
    print(f"Exported {export_path.relative_to(ROOT)}")
    print(f"Reference A01 {A01_REFERENCE.relative_to(ROOT)}")
    print(f"Review board {(REVIEW_ROOT / f'{ASSET_NAME}_FinalGameReadyReviewBoard.png').relative_to(ROOT)}")
    print(f"LOD0 tris: {collection_triangle_count(lod0_collection)}")
    print(f"LOD1 tris: {collection_triangle_count(lod1_collection)}")
    print(f"LOD2 tris: {collection_triangle_count(lod2_collection)}")
    print(f"LOD3 tris: {collection_triangle_count(lod3_collection)}")
    print(f"LOD0 bounds: {width:.2f}w x {depth:.2f}d x {height:.2f}h cm")
    print("Collision proxies: 1")


if __name__ == "__main__":
    build()
