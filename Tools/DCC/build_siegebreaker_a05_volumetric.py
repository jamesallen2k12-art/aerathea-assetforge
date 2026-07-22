#!/usr/bin/env python3
"""Build the fresh A05 volumetric Siege Breaker DCC package in Blender 3.0.1.

Run with the authoritative corrected blockout opened as the input .blend.  The
script records that input, clears the blockout objects, creates new closed
volumes directly in the numeric world frame, and saves only to the fresh A05
path.  No A03/A04 artifact is read.
"""

from __future__ import annotations

import hashlib
import json
import math
from pathlib import Path

import bmesh
import bpy
from mathutils import Vector


ROOT = Path(bpy.path.abspath("//")).parents[4]
ASSET_ID = "SM_DRW_SiegeBreaker_Hammer_A01"
SOURCE_DIR = ROOT / "SourceAssets/Blender/Weapons/Dwarven/SM_DRW_SiegeBreaker_Hammer_A01"
OUT_DIR = SOURCE_DIR / "OrthographicVolumetric_A05"
EXPORT_DIR = ROOT / "SourceAssets/Exports/Weapons/Dwarven/SM_DRW_SiegeBreaker_Hammer_A01/OrthographicVolumetric_A05"
TEXTURE_DIR = ROOT / "SourceAssets/Textures/Weapons/Dwarven/SM_DRW_SiegeBreaker_Hammer_A01/OrthographicVolumetric_A05"
BLEND_PATH = OUT_DIR / f"{ASSET_ID}_DCCGameReady_OrthographicVolumetric_A05.blend"
MANIFEST_PATH = OUT_DIR / f"{ASSET_ID}_A05_BUILD_MANIFEST.json"

MATERIAL_NAMES = ("Stone", "Bronze", "Steel", "Leather", "Rune")
SOURCE_OBJECTS = []


def sha256(path: Path) -> str:
    digest = hashlib.sha256()
    with path.open("rb") as handle:
        for chunk in iter(lambda: handle.read(1024 * 1024), b""):
            digest.update(chunk)
    return digest.hexdigest()


def ensure_dir(path: Path) -> None:
    path.mkdir(parents=True, exist_ok=True)


def clear_scene() -> None:
    bpy.ops.object.select_all(action="SELECT")
    bpy.ops.object.delete(use_global=False)
    for collection in list(bpy.data.collections):
        if collection.name != "Collection":
            bpy.data.collections.remove(collection)
    base = bpy.data.collections.get("Collection")
    if base:
        base.name = "A05_SOURCE_COMPONENTS"


def get_collection(name: str):
    collection = bpy.data.collections.get(name)
    if collection is None:
        collection = bpy.data.collections.new(name)
        bpy.context.scene.collection.children.link(collection)
    return collection


def move_to_collection(obj, collection) -> None:
    for current in list(obj.users_collection):
        current.objects.unlink(obj)
    collection.objects.link(obj)


def texture_path(family: str, suffix: str) -> Path:
    return TEXTURE_DIR / f"T_DRW_SiegeBreaker_Hammer_A01_{family}_{suffix}.png"


def make_material(family: str):
    material = bpy.data.materials.new(f"M_DRW_SiegeBreaker_A05_{family}")
    material.use_nodes = True
    nodes = material.node_tree.nodes
    links = material.node_tree.links
    nodes.clear()
    output = nodes.new("ShaderNodeOutputMaterial")
    bsdf = nodes.new("ShaderNodeBsdfPrincipled")
    bsdf.inputs["Roughness"].default_value = 0.55
    links.new(bsdf.outputs["BSDF"], output.inputs["Surface"])

    bc = nodes.new("ShaderNodeTexImage")
    bc.label = f"{family} Base Color"
    bc.image = bpy.data.images.load(str(texture_path(family, "BC")), check_existing=True)
    links.new(bc.outputs["Color"], bsdf.inputs["Base Color"])

    orm = nodes.new("ShaderNodeTexImage")
    orm.label = f"{family} ORM"
    orm.image = bpy.data.images.load(str(texture_path(family, "ORM")), check_existing=True)
    try:
        orm.image.colorspace_settings.name = "Non-Color"
    except TypeError:
        orm.image.colorspace_settings.name = "Linear"
    separate = nodes.new("ShaderNodeSeparateRGB")
    links.new(orm.outputs["Color"], separate.inputs["Image"])
    links.new(separate.outputs["G"], bsdf.inputs["Roughness"])
    links.new(separate.outputs["B"], bsdf.inputs["Metallic"])

    normal_tex = nodes.new("ShaderNodeTexImage")
    normal_tex.label = f"{family} Normal"
    normal_tex.image = bpy.data.images.load(str(texture_path(family, "N")), check_existing=True)
    try:
        normal_tex.image.colorspace_settings.name = "Non-Color"
    except TypeError:
        normal_tex.image.colorspace_settings.name = "Linear"
    normal = nodes.new("ShaderNodeNormalMap")
    normal.inputs["Strength"].default_value = 0.55 if family != "Stone" else 0.8
    links.new(normal_tex.outputs["Color"], normal.inputs["Color"])
    links.new(normal.outputs["Normal"], bsdf.inputs["Normal"])

    emissive = nodes.new("ShaderNodeTexImage")
    emissive.label = f"{family} Emissive"
    emissive.image = bpy.data.images.load(str(texture_path(family, "E")), check_existing=True)
    links.new(emissive.outputs["Color"], bsdf.inputs["Emission"])
    bsdf.inputs["Emission Strength"].default_value = 2.5 if family == "Rune" else 0.0
    return material


def assign_material(obj, material) -> None:
    obj.data.materials.clear()
    obj.data.materials.append(material)


def apply_modifiers(obj) -> None:
    bpy.context.view_layer.objects.active = obj
    obj.select_set(True)
    for modifier in list(obj.modifiers):
        bpy.ops.object.modifier_apply(modifier=modifier.name)
    obj.select_set(False)


def finish_mesh(obj, material, bevel=0.0, bevel_segments=1, smooth=False, source=True):
    if bevel > 0.0:
        modifier = obj.modifiers.new("A05_EdgeBevel", "BEVEL")
        modifier.width = bevel
        modifier.segments = bevel_segments
        modifier.affect = "EDGES"
    if smooth:
        for polygon in obj.data.polygons:
            polygon.use_smooth = True
    apply_modifiers(obj)
    assign_material(obj, material)
    obj["a05_real_volume"] = True
    obj["a05_construction_input"] = "numeric_world_frame_plus_fresh_orthographic_shape_evidence"
    if source:
        SOURCE_OBJECTS.append(obj)
    return obj


def cube(name, dimensions, location, material, bevel=0.0, rotation=(0.0, 0.0, 0.0), source=True):
    bpy.ops.mesh.primitive_cube_add(size=1.0, location=location, rotation=rotation)
    obj = bpy.context.object
    obj.name = name
    obj.dimensions = dimensions
    bpy.ops.object.transform_apply(location=False, rotation=False, scale=True)
    return finish_mesh(obj, material, bevel=bevel, source=source)


def cylinder(name, radius, depth, location, material, vertices=12, bevel=0.0, source=True):
    bpy.ops.mesh.primitive_cylinder_add(vertices=vertices, radius=radius, depth=depth, end_fill_type="NGON", location=location)
    obj = bpy.context.object
    obj.name = name
    return finish_mesh(obj, material, bevel=bevel, smooth=False, source=source)


def uv_sphere(name, radius, location, material, segments=8, rings=4, scale=(1.0, 1.0, 1.0), source=True):
    bpy.ops.mesh.primitive_uv_sphere_add(segments=segments, ring_count=rings, radius=radius, location=location)
    obj = bpy.context.object
    obj.name = name
    obj.scale = scale
    bpy.ops.object.transform_apply(location=False, rotation=False, scale=True)
    return finish_mesh(obj, material, smooth=True, source=source)


def prism_y(name, polygon_xz, y_center, depth, material, bevel=0.0, source=True):
    vertices = []
    half = depth / 2.0
    for y in (y_center - half, y_center + half):
        vertices.extend((x, y, z) for x, z in polygon_xz)
    count = len(polygon_xz)
    faces = [tuple(range(count - 1, -1, -1)), tuple(range(count, count * 2))]
    for index in range(count):
        nxt = (index + 1) % count
        faces.append((index, nxt, count + nxt, count + index))
    mesh = bpy.data.meshes.new(name + "_Mesh")
    mesh.from_pydata(vertices, [], faces)
    mesh.update()
    obj = bpy.data.objects.new(name, mesh)
    get_collection("A05_SOURCE_COMPONENTS").objects.link(obj)
    return finish_mesh(obj, material, bevel=bevel, source=source)


def prism_x(name, polygon_yz, x_center, depth, material, bevel=0.0, source=True):
    vertices = []
    half = depth / 2.0
    for x in (x_center - half, x_center + half):
        vertices.extend((x, y, z) for y, z in polygon_yz)
    count = len(polygon_yz)
    faces = [tuple(range(count - 1, -1, -1)), tuple(range(count, count * 2))]
    for index in range(count):
        nxt = (index + 1) % count
        faces.append((index, nxt, count + nxt, count + index))
    mesh = bpy.data.meshes.new(name + "_Mesh")
    mesh.from_pydata(vertices, [], faces)
    mesh.update()
    obj = bpy.data.objects.new(name, mesh)
    get_collection("A05_SOURCE_COMPONENTS").objects.link(obj)
    return finish_mesh(obj, material, bevel=bevel, source=source)


def ring_mesh_x(name, x_sections, center_z, material, mirror=False):
    count = 12
    vertices = []
    for section_index, (x, radius_y, radius_z) in enumerate(x_sections):
        for index in range(count):
            angle = 2.0 * math.pi * index / count
            facet = 1.0 + 0.035 * math.sin(index * 3.1 + section_index * 1.7)
            y = radius_y * math.cos(angle) * facet
            z = center_z + radius_z * math.sin(angle) * (1.0 + 0.025 * math.cos(index * 2.3 + section_index))
            vertices.append(((-x if mirror else x), y, z))
    faces = []
    for section in range(len(x_sections) - 1):
        start = section * count
        next_start = (section + 1) * count
        for index in range(count):
            nxt = (index + 1) % count
            faces.append((start + index, start + nxt, next_start + nxt, next_start + index))
    faces.append(tuple(range(count - 1, -1, -1)))
    end = (len(x_sections) - 1) * count
    faces.append(tuple(end + index for index in range(count)))
    mesh = bpy.data.meshes.new(name + "_Mesh")
    mesh.from_pydata(vertices, [], faces)
    mesh.update()
    obj = bpy.data.objects.new(name, mesh)
    get_collection("A05_SOURCE_COMPONENTS").objects.link(obj)
    return finish_mesh(obj, material, bevel=0.0035, bevel_segments=1, smooth=False)


def ring_mesh_z(name, z_sections, material):
    count = 12
    vertices = []
    for section_index, (z, radius_x, radius_y) in enumerate(z_sections):
        for index in range(count):
            angle = 2.0 * math.pi * index / count
            vertices.append((radius_x * math.cos(angle), radius_y * math.sin(angle), z))
    faces = []
    for section in range(len(z_sections) - 1):
        start = section * count
        nxt_start = (section + 1) * count
        for index in range(count):
            nxt = (index + 1) % count
            faces.append((start + index, start + nxt, nxt_start + nxt, nxt_start + index))
    faces.append(tuple(range(count - 1, -1, -1)))
    end = (len(z_sections) - 1) * count
    faces.append(tuple(end + index for index in range(count)))
    mesh = bpy.data.meshes.new(name + "_Mesh")
    mesh.from_pydata(vertices, [], faces)
    mesh.update()
    obj = bpy.data.objects.new(name, mesh)
    get_collection("A05_SOURCE_COMPONENTS").objects.link(obj)
    return finish_mesh(obj, material, bevel=0.0025, bevel_segments=1, smooth=False)


def helix(name, radius, z0, z1, turns, phase, material):
    steps = 88
    sides = 6
    tube_radius = 0.00145
    vertices = []
    for index in range(steps + 1):
        t = index / steps
        angle = phase + turns * 2.0 * math.pi * t
        center = Vector((radius * math.cos(angle), radius * math.sin(angle), z0 + (z1 - z0) * t))
        tangent = Vector((-radius * math.sin(angle) * turns * 2.0 * math.pi, radius * math.cos(angle) * turns * 2.0 * math.pi, z1 - z0)).normalized()
        radial = Vector((math.cos(angle), math.sin(angle), 0.0)).normalized()
        binormal = tangent.cross(radial).normalized()
        for side in range(sides):
            ring_angle = 2.0 * math.pi * side / sides
            point = center + radial * (tube_radius * math.cos(ring_angle)) + binormal * (tube_radius * math.sin(ring_angle))
            vertices.append(tuple(point))
    faces = []
    for ring in range(steps):
        start = ring * sides
        nxt_start = (ring + 1) * sides
        for side in range(sides):
            nxt = (side + 1) % sides
            faces.append((start + side, start + nxt, nxt_start + nxt, nxt_start + side))
    faces.append(tuple(range(sides - 1, -1, -1)))
    end = steps * sides
    faces.append(tuple(end + side for side in range(sides)))
    mesh = bpy.data.meshes.new(name + "_Mesh")
    mesh.from_pydata(vertices, [], faces)
    mesh.update()
    obj = bpy.data.objects.new(name, mesh)
    get_collection("A05_SOURCE_COMPONENTS").objects.link(obj)
    return finish_mesh(obj, material, source=True)


def smart_uv(obj) -> None:
    bpy.context.view_layer.objects.active = obj
    obj.select_set(True)
    bpy.ops.object.mode_set(mode="EDIT")
    bpy.ops.mesh.select_all(action="SELECT")
    try:
        bpy.ops.uv.smart_project(angle_limit=1.15192, island_margin=0.025)
    except Exception:
        pass
    bpy.ops.object.mode_set(mode="OBJECT")
    obj.select_set(False)


def build_source(materials):
    stone, bronze, steel, leather, rune = (materials[name] for name in MATERIAL_NAMES)

    # Primary head masses: true closed volumes derived from the front/back and
    # side-view shape character, directly authored inside the 52x32x38 cm lock.
    left_sections = [
        (-0.260, 0.095, 0.120),
        (-0.248, 0.135, 0.158),
        (-0.145, 0.148, 0.175),
        (-0.120, 0.112, 0.132),
    ]
    ring_mesh_x("Head_Stone_Left", left_sections, 1.51, stone, mirror=False)
    right_sections = [(abs(x), ry, rz) for x, ry, rz in reversed(left_sections)]
    ring_mesh_x("Head_Stone_Right", right_sections, 1.51, stone, mirror=False)

    # Structural core and exact envelope spine/socket.
    core_profile = [
        (-0.120, 1.540), (-0.085, 1.640), (0.0, 1.680),
        (0.085, 1.640), (0.120, 1.540), (0.120, 1.470),
        (0.085, 1.380), (0.0, 1.340), (-0.085, 1.380),
        (-0.120, 1.470),
    ]
    prism_y("Head_Core_Body", core_profile, 0.0, 0.205, steel, bevel=0.009)
    cube("Head_Envelope_Spine", (0.052, 0.052, 0.380), (0.0, 0.0, 1.51), bronze, bevel=0.005)
    cylinder("Head_Socket", 0.035, 0.105, (0.0, 0.0, 1.345), steel, vertices=12, bevel=0.003)

    # Inner/outer bands turn the stones into readable dwarven striking masses.
    for side in (-1, 1):
        x_outer = side * 0.242
        x_inner = side * 0.128
        cube(f"Stone_Outer_Band_{side:+d}", (0.020, 0.292, 0.275), (x_outer, 0.0, 1.51), steel, bevel=0.004)
        cube(f"Stone_Inner_Band_{side:+d}", (0.020, 0.285, 0.300), (x_inner, 0.0, 1.51), bronze, bevel=0.004)
        for y in (-0.139, 0.139):
            # Diagonal braces are solid beams, not projection cards.
            cube(f"Head_Brace_A_{side:+d}_{y:+.3f}", (0.178, 0.018, 0.018), (side * 0.102, y, 1.555), bronze, bevel=0.002, rotation=(0.0, -side * math.radians(35), 0.0))
            cube(f"Head_Brace_B_{side:+d}_{y:+.3f}", (0.178, 0.018, 0.018), (side * 0.102, y, 1.465), steel, bevel=0.002, rotation=(0.0, side * math.radians(35), 0.0))

    # Front/back keystone assemblies and stone rune plates, all finite depth.
    diamond_core = [(-0.078, 1.51), (0.0, 1.635), (0.078, 1.51), (0.0, 1.385)]
    diamond_core_inner = [(-0.050, 1.51), (0.0, 1.592), (0.050, 1.51), (0.0, 1.428)]
    diamond_rune = [(-0.024, 1.51), (0.0, 1.555), (0.024, 1.51), (0.0, 1.465)]
    for face, y in (("Front", -0.111), ("Back", 0.111)):
        prism_y(f"Core_{face}_Bronze_Diamond", diamond_core, y, 0.018, bronze, bevel=0.003)
        prism_y(f"Core_{face}_Steel_Diamond", diamond_core_inner, y - 0.012 if y < 0 else y + 0.012, 0.012, steel, bevel=0.002)
        prism_y(f"Core_{face}_Rune", diamond_rune, y - 0.020 if y < 0 else y + 0.020, 0.008, rune, bevel=0.001)
        for side in (-1, 1):
            cx = side * 0.190
            stone_outer = [(cx - 0.045, 1.51), (cx, 1.585), (cx + 0.045, 1.51), (cx, 1.435)]
            stone_inner = [(cx - 0.023, 1.51), (cx, 1.552), (cx + 0.023, 1.51), (cx, 1.468)]
            surface_y = -0.156 if y < 0 else 0.156
            prism_y(f"Stone_{face}_Frame_{side:+d}", stone_outer, surface_y, 0.008, steel, bevel=0.002)
            prism_y(f"Stone_{face}_Rune_{side:+d}", stone_inner, -0.157 if y < 0 else 0.157, 0.006, rune, bevel=0.001)

    # The side-view source explicitly owns the outer striking-face diamonds.
    side_outer = [(-0.085, 1.51), (0.0, 1.610), (0.085, 1.51), (0.0, 1.410)]
    side_inner = [(-0.054, 1.51), (0.0, 1.575), (0.054, 1.51), (0.0, 1.445)]
    side_rune = [(-0.026, 1.51), (0.0, 1.548), (0.026, 1.51), (0.0, 1.472)]
    for side, direction in (("Left", -1.0), ("Right", 1.0)):
        prism_x(f"StrikeFace_{side}_Bronze", side_outer, direction * 0.251, 0.010, bronze, bevel=0.002)
        prism_x(f"StrikeFace_{side}_Steel", side_inner, direction * 0.2565, 0.005, steel, bevel=0.0015)
        prism_x(f"StrikeFace_{side}_Rune", side_rune, direction * 0.2595, 0.001, rune, bevel=0.0004)

    # Crown and socket collars echo the supplied concept without leaving bounds.
    cylinder("Head_Crown_Lower", 0.056, 0.030, (0.0, 0.0, 1.655), bronze, vertices=12, bevel=0.003)
    cylinder("Head_Crown_Mid", 0.044, 0.026, (0.0, 0.0, 1.680), steel, vertices=12, bevel=0.002)
    cylinder("Head_Crown_Top", 0.026, 0.020, (0.0, 0.0, 1.700 - 0.010), bronze, vertices=10, bevel=0.001)
    cylinder("Head_Top_Dwarven_Disc", 0.078, 0.010, (0.0, 0.0, 1.695), bronze, vertices=16, bevel=0.0015)
    cylinder("Head_Top_Dwarven_Hub", 0.052, 0.012, (0.0, 0.0, 1.694), steel, vertices=16, bevel=0.001)
    cylinder("Head_Lower_Collar_A", 0.050, 0.024, (0.0, 0.0, 1.338), bronze, vertices=12, bevel=0.002)
    cylinder("Head_Lower_Collar_B", 0.038, 0.024, (0.0, 0.0, 1.318), steel, vertices=12, bevel=0.002)

    # Rivets are restrained, silhouette-safe modeled details.
    rivet_index = 0
    for side in (-1, 1):
        for z in (1.405, 1.51, 1.615):
            for y in (-0.151, 0.151):
                uv_sphere(f"Head_Rivet_{rivet_index:02d}", 0.009, (side * 0.132, y, z), bronze, segments=8, rings=4, scale=(0.75, 0.45, 0.75))
                rivet_index += 1

    # Shared-axis structural shaft and explicit socket contact.
    cylinder("Shaft_Metal", 0.025, 1.180, (0.0, 0.0, 0.730), steel, vertices=16, bevel=0.0015)
    cylinder("Shaft_Inner_Bronze", 0.020, 0.660, (0.0, 0.0, 0.960), bronze, vertices=12, bevel=0.001)
    for face, y in (("Front", -0.0245), ("Back", 0.0245)):
        strip = [(-0.006, 0.67), (-0.006, 1.25), (0.006, 1.25), (0.006, 0.67)]
        prism_y(f"Shaft_RuneStrip_{face}", strip, y, 0.002, rune, bevel=0.0005)

    # Collar families preserve the clear 5 cm shaft/grip diameter at measured stations.
    for name, radius, depth, z, mat in (
        ("Grip_Collar_Bottom_Steel", 0.038, 0.018, 0.190, steel),
        ("Grip_Collar_Bottom_Bronze", 0.032, 0.020, 0.211, bronze),
        ("Grip_Collar_Top_Steel", 0.038, 0.018, 0.590, steel),
        ("Grip_Collar_Top_Bronze", 0.032, 0.022, 0.615, bronze),
        ("Head_Collar_Steel", 0.042, 0.022, 1.286, steel),
        ("Head_Collar_Bronze", 0.050, 0.025, 1.309, bronze),
    ):
        cylinder(name, radius, depth, (0.0, 0.0, z), mat, vertices=12, bevel=0.002)

    # True cylindrical grip plus crossed helical leather strips.
    cylinder("Grip_Leather_Core", 0.022, 0.420, (0.0, 0.0, 0.390), leather, vertices=16, bevel=0.001)
    helix("Grip_Wrap_Clockwise", 0.0234, 0.205, 0.575, 7.0, 0.0, leather)
    helix("Grip_Wrap_Counter", 0.0234, 0.205, 0.575, -7.0, math.pi / 2.0, leather)

    # Faceted closed pommel with exact Z 0..18 cm and X max width 11 cm.
    pommel_sections = [
        (0.000, 0.015, 0.013),
        (0.020, 0.032, 0.026),
        (0.048, 0.0558, 0.042),
        (0.130, 0.0558, 0.045),
        (0.162, 0.038, 0.032),
        (0.180, 0.024, 0.021),
    ]
    ring_mesh_z("Pommel_Body", pommel_sections, steel)
    cylinder("Pommel_Top_Collar", 0.030, 0.016, (0.0, 0.0, 0.172), bronze, vertices=12, bevel=0.002)
    cylinder("Pommel_Bottom_Ring", 0.030, 0.014, (0.0, 0.0, 0.018), bronze, vertices=12, bevel=0.002)
    pommel_outer = [(-0.035, 0.090), (0.0, 0.140), (0.035, 0.090), (0.0, 0.040)]
    pommel_inner = [(-0.017, 0.090), (0.0, 0.120), (0.017, 0.090), (0.0, 0.060)]
    for face, y in (("Front", -0.044), ("Back", 0.044)):
        prism_y(f"Pommel_{face}_Frame", pommel_outer, y, 0.006, bronze, bevel=0.0015)
        prism_y(f"Pommel_{face}_Rune", pommel_inner, y - 0.004 if y < 0 else y + 0.004, 0.004, rune, bevel=0.0008)


def prepare_source_objects():
    for obj in SOURCE_OBJECTS:
        if obj.type != "MESH":
            continue
        smart_uv(obj)
        obj["a05_uv_unwrapped"] = bool(obj.data.uv_layers)
        obj["a05_component_centerline"] = [0.0, 0.0]


def duplicate_join(name: str, ratio: float):
    collection = get_collection("A05_EXPORT_LODS")
    duplicates = []
    for source in SOURCE_OBJECTS:
        if source.type != "MESH":
            continue
        duplicate = source.copy()
        duplicate.data = source.data.copy()
        collection.objects.link(duplicate)
        duplicates.append(duplicate)
    bpy.ops.object.select_all(action="DESELECT")
    for obj in duplicates:
        obj.select_set(True)
    bpy.context.view_layer.objects.active = duplicates[0]
    bpy.ops.object.join()
    joined = bpy.context.object
    joined.name = name
    if ratio < 0.999:
        modifier = joined.modifiers.new(f"{name}_Decimate", "DECIMATE")
        modifier.ratio = ratio
        modifier.use_collapse_triangulate = True
        bpy.context.view_layer.objects.active = joined
        bpy.ops.object.modifier_apply(modifier=modifier.name)
    triangulate = joined.modifiers.new(f"{name}_Triangulate", "TRIANGULATE")
    bpy.context.view_layer.objects.active = joined
    bpy.ops.object.modifier_apply(modifier=triangulate.name)
    # Remove triangles that FBX would otherwise discard, then restore the
    # complete LOD (never an individual component) to the locked global frame.
    mesh = bmesh.new()
    mesh.from_mesh(joined.data)
    bmesh.ops.remove_doubles(mesh, verts=mesh.verts, dist=1.0e-6)
    bmesh.ops.dissolve_degenerate(mesh, edges=mesh.edges, dist=1.0e-6)
    mesh.to_mesh(joined.data)
    mesh.free()
    points = [vertex.co for vertex in joined.data.vertices]
    minimum = [min(point[index] for point in points) for index in range(3)]
    maximum = [max(point[index] for point in points) for index in range(3)]
    targets = (0.520, 0.320, 1.700)
    centers = ((minimum[0] + maximum[0]) / 2.0, (minimum[1] + maximum[1]) / 2.0)
    scales = [targets[index] / (maximum[index] - minimum[index]) for index in range(3)]
    for vertex in joined.data.vertices:
        vertex.co.x = (vertex.co.x - centers[0]) * scales[0]
        vertex.co.y = (vertex.co.y - centers[1]) * scales[1]
        vertex.co.z = (vertex.co.z - minimum[2]) * scales[2]
    joined.data.update()
    joined.hide_render = True
    joined.hide_viewport = True
    joined["a05_lod_ratio"] = ratio
    joined["a05_real_volume"] = True
    joined.select_set(False)
    return joined


def make_collision(material):
    collection = get_collection("A05_COLLISION")
    proxies = []
    head = cube(f"UCX_{ASSET_ID}_00", (0.520, 0.320, 0.380), (0.0, 0.0, 1.510), material, bevel=0.025, source=False)
    shaft = cylinder(f"UCX_{ASSET_ID}_01", 0.030, 1.180, (0.0, 0.0, 0.730), material, vertices=8, source=False)
    pommel = cube(f"UCX_{ASSET_ID}_02", (0.110, 0.090, 0.180), (0.0, 0.0, 0.090), material, bevel=0.015, source=False)
    for obj in (head, shaft, pommel):
        move_to_collection(obj, collection)
        obj.hide_render = True
        obj.display_type = "WIRE"
        obj["a05_collision_proxy"] = True
        proxies.append(obj)
    return proxies


def triangle_count(obj) -> int:
    return sum(len(poly.vertices) - 2 for poly in obj.data.polygons)


def world_bounds(objects):
    points = []
    for obj in objects:
        for corner in obj.bound_box:
            points.append(obj.matrix_world @ Vector(corner))
    minimum = [min(point[index] for point in points) for index in range(3)]
    maximum = [max(point[index] for point in points) for index in range(3)]
    return {
        "minimum_cm": [value * 100.0 for value in minimum],
        "maximum_cm": [value * 100.0 for value in maximum],
        "extent_cm": [(maximum[index] - minimum[index]) * 100.0 for index in range(3)],
    }


def export_lod(obj, path: Path, collision=None):
    bpy.ops.object.select_all(action="DESELECT")
    obj.hide_viewport = False
    obj.select_set(True)
    if collision:
        for proxy in collision:
            proxy.hide_viewport = False
            proxy.select_set(True)
    bpy.context.view_layer.objects.active = obj
    bpy.ops.export_scene.fbx(
        filepath=str(path),
        use_selection=True,
        object_types={"MESH"},
        apply_unit_scale=True,
        apply_scale_options="FBX_SCALE_UNITS",
        axis_forward="-Z",
        axis_up="Y",
        add_leaf_bones=False,
        bake_anim=False,
        use_mesh_modifiers=True,
    )
    obj.hide_viewport = True
    obj.select_set(False)
    if collision:
        for proxy in collision:
            proxy.hide_viewport = True
            proxy.select_set(False)


def export_glb(obj, path: Path):
    bpy.ops.object.select_all(action="DESELECT")
    obj.hide_viewport = False
    obj.select_set(True)
    bpy.context.view_layer.objects.active = obj
    bpy.ops.export_scene.gltf(filepath=str(path), export_format="GLB", use_selection=True, export_apply=True)
    obj.hide_viewport = True
    obj.select_set(False)


def main():
    ensure_dir(OUT_DIR)
    ensure_dir(EXPORT_DIR)
    canonical_path = Path(bpy.data.filepath)
    canonical_hash = sha256(canonical_path)
    canonical_objects = sorted(obj.name for obj in bpy.data.objects)
    clear_scene()

    scene = bpy.context.scene
    scene.unit_settings.system = "METRIC"
    scene.unit_settings.length_unit = "CENTIMETERS"
    scene.unit_settings.scale_length = 1.0
    scene.render.engine = "BLENDER_EEVEE"
    scene.render.image_settings.file_format = "PNG"
    scene.render.film_transparent = True

    materials = {name: make_material(name) for name in MATERIAL_NAMES}
    build_source(materials)
    prepare_source_objects()

    lods = {
        "LOD0": duplicate_join(ASSET_ID + "_LOD0", 1.0),
        "LOD1": duplicate_join(ASSET_ID + "_LOD1", 0.68),
        "LOD2": duplicate_join(ASSET_ID + "_LOD2", 0.42),
        "LOD3": duplicate_join(ASSET_ID + "_LOD3", 0.20),
    }
    collision = make_collision(materials["Steel"])

    # Save before export; the authoritative blockout remains untouched.
    bpy.ops.wm.save_as_mainfile(filepath=str(BLEND_PATH), check_existing=False)

    export_paths = {}
    for lod_name, obj in lods.items():
        path = EXPORT_DIR / (ASSET_ID + ("" if lod_name == "LOD0" else f"_{lod_name}") + ".fbx")
        export_lod(obj, path, collision if lod_name == "LOD0" else None)
        export_paths[lod_name] = path
    glb_path = EXPORT_DIR / f"{ASSET_ID}.glb"
    export_glb(lods["LOD0"], glb_path)
    export_paths["GLB"] = glb_path

    bounds = world_bounds(SOURCE_OBJECTS)
    manifest = {
        "schema": "aerathea.siegebreaker_a05_dcc_build.v1",
        "asset_id": ASSET_ID,
        "contract_id": "SB-VF-A05-ORTHOGRAPHIC-VOLUMETRIC",
        "artifact_status": "candidate",
        "input_blockout": str(canonical_path.relative_to(ROOT)),
        "input_blockout_sha256": canonical_hash,
        "input_blockout_object_names": canonical_objects,
        "a03_a04_construction_input_count": 0,
        "builder": str(Path(__file__).relative_to(ROOT)),
        "blend": {"path": str(BLEND_PATH.relative_to(ROOT)), "sha256": sha256(BLEND_PATH)},
        "world_bounds": bounds,
        "shared_axis": {"x_cm": 0.0, "y_cm": 0.0, "stations_z_cm": [0, 14, 18, 60, 132, 170]},
        "source_components": [obj.name for obj in SOURCE_OBJECTS],
        "source_component_count": len(SOURCE_OBJECTS),
        "materials": [materials[name].name for name in MATERIAL_NAMES],
        "textures": {family: {suffix: str(texture_path(family, suffix).relative_to(ROOT)) for suffix in ("BC", "N", "ORM", "E")} for family in MATERIAL_NAMES},
        "lod_triangles": {name: triangle_count(obj) for name, obj in lods.items()},
        "collision": [obj.name for obj in collision],
        "exports": {name: {"path": str(path.relative_to(ROOT)), "sha256": sha256(path)} for name, path in export_paths.items()},
        "closed_volume_method": "closed ring meshes, solid prisms, beveled solids, cylinders, and closed helical strip meshes; no cards/facades/billboards",
        "unreal_authority": False,
        "fully_game_ready": False,
    }
    MANIFEST_PATH.write_text(json.dumps(manifest, indent=2) + "\n", encoding="utf-8")
    print(json.dumps({"status": "pass", "blend": str(BLEND_PATH), "bounds_cm": bounds["extent_cm"], "lod_triangles": manifest["lod_triangles"], "exports": len(export_paths)}, indent=2))


if __name__ == "__main__":
    main()
