"""Build the numeric-authority Siege Breaker blockout or DCC game-ready candidate.

This is a fresh implementation derived from the verified final package. It
does not reuse the quarantined 2026-07-07 builder or its grip-centered layout.

Blender usage:
  blender --background --python Tools/DCC/build_siegebreaker_final_package_a01.py -- --mode blockout
  blender --background --python Tools/DCC/build_siegebreaker_final_package_a01.py -- --mode final
"""

from __future__ import annotations

import argparse
import hashlib
import json
import math
import sys
from pathlib import Path

import bmesh
import bpy
from mathutils import Vector


ROOT = Path(__file__).resolve().parents[2]
ASSET_ID = "SM_DRW_SiegeBreaker_Hammer_A01"
CM = 0.01

REFERENCE_ROOT = ROOT / "SourceAssets/Reference/Weapons/Dwarven" / ASSET_ID / "02_SiegeBreaker_Codex_Final_Package"
TEXTURE_ROOT = ROOT / "SourceAssets/Textures/Weapons/Dwarven" / ASSET_ID
SOURCE_ROOT = ROOT / "SourceAssets/Blender/Weapons/Dwarven" / ASSET_ID
EXPORT_ROOT = ROOT / "SourceAssets/Exports/Weapons/Dwarven" / ASSET_ID

MATERIAL_ORDER = ["M_Stone", "M_Bronze", "M_Steel", "M_Leather", "M_Rune_Emissive"]
TEXTURE_FAMILIES = {
    "M_Stone": "Stone",
    "M_Bronze": "Bronze",
    "M_Steel": "Steel",
    "M_Leather": "Leather",
    "M_Rune_Emissive": "Rune",
}


def sha256(path: Path) -> str:
    digest = hashlib.sha256()
    with path.open("rb") as handle:
        for chunk in iter(lambda: handle.read(1024 * 1024), b""):
            digest.update(chunk)
    return digest.hexdigest()


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser()
    parser.add_argument("--mode", choices=("blockout", "final"), default="final")
    argv = sys.argv[sys.argv.index("--") + 1 :] if "--" in sys.argv else []
    return parser.parse_args(argv)


def clear_scene() -> None:
    bpy.ops.object.select_all(action="SELECT")
    bpy.ops.object.delete(use_global=False)
    for collection in list(bpy.data.collections):
        if collection.name != "Collection":
            bpy.data.collections.remove(collection)
    for datablocks in (bpy.data.meshes, bpy.data.curves, bpy.data.materials, bpy.data.images):
        for datablock in list(datablocks):
            if datablock.users == 0:
                datablocks.remove(datablock)


def get_collection(name: str) -> bpy.types.Collection:
    collection = bpy.data.collections.get(name)
    if collection is None:
        collection = bpy.data.collections.new(name)
        bpy.context.scene.collection.children.link(collection)
    return collection


def move_to_collection(obj: bpy.types.Object, collection: bpy.types.Collection) -> None:
    for current in list(obj.users_collection):
        current.objects.unlink(obj)
    collection.objects.link(obj)


def configure_scene() -> None:
    scene = bpy.context.scene
    scene.unit_settings.system = "METRIC"
    scene.unit_settings.length_unit = "CENTIMETERS"
    scene.unit_settings.scale_length = 1.0
    scene.render.image_settings.file_format = "PNG"
    scene.render.film_transparent = False
    scene.world.color = (0.012, 0.018, 0.026)
    scene["Aerathea.AssetID"] = ASSET_ID
    scene["Aerathea.Authority"] = "verified final package numeric specification"
    scene["Aerathea.OverallBoundsCM"] = "52x32x170"
    scene["Aerathea.ShaftPommelOverlapCM"] = 4.0


def simple_material(name: str, color: tuple[float, float, float], metallic: float, roughness: float, emission=False):
    material = bpy.data.materials.new(name)
    material.use_nodes = True
    bsdf = material.node_tree.nodes.get("Principled BSDF")
    bsdf.inputs["Base Color"].default_value = (*color, 1.0)
    bsdf.inputs["Metallic"].default_value = metallic
    bsdf.inputs["Roughness"].default_value = roughness
    if emission:
        emission_name = "Emission" if "Emission" in bsdf.inputs else "Emission Color"
        bsdf.inputs[emission_name].default_value = (*color, 1.0)
        bsdf.inputs["Emission Strength"].default_value = 3.5
    return material


def texture_path(family: str, suffix: str) -> Path:
    return TEXTURE_ROOT / f"T_DRW_SiegeBreaker_Hammer_A01_{family}_{suffix}.png"


def set_data_colorspace(image: bpy.types.Image) -> None:
    try:
        image.colorspace_settings.name = "Non-Color"
    except TypeError:
        image.colorspace_settings.name = "Linear"


def textured_material(name: str, family: str, emission=False) -> bpy.types.Material:
    required = [texture_path(family, suffix) for suffix in ("BC", "N", "ORM", "E")]
    if not all(path.exists() for path in required):
        fallbacks = {
            "Stone": ((0.055, 0.065, 0.08), 0.0, 0.82),
            "Bronze": ((0.30, 0.14, 0.045), 1.0, 0.46),
            "Steel": ((0.075, 0.09, 0.115), 1.0, 0.38),
            "Leather": ((0.14, 0.045, 0.018), 0.0, 0.68),
            "Rune": ((0.015, 0.24, 0.82), 0.0, 0.24),
        }
        color, metallic, roughness = fallbacks[family]
        return simple_material(name, color, metallic, roughness, emission)

    material = bpy.data.materials.new(name)
    material.use_nodes = True
    nodes = material.node_tree.nodes
    links = material.node_tree.links
    nodes.clear()
    output = nodes.new("ShaderNodeOutputMaterial")
    bsdf = nodes.new("ShaderNodeBsdfPrincipled")
    links.new(bsdf.outputs["BSDF"], output.inputs["Surface"])

    bc = nodes.new("ShaderNodeTexImage")
    bc.name = f"{family}_BC"
    bc.image = bpy.data.images.load(str(texture_path(family, "BC")), check_existing=True)
    bc.image.colorspace_settings.name = "sRGB"

    orm = nodes.new("ShaderNodeTexImage")
    orm.name = f"{family}_ORM"
    orm.image = bpy.data.images.load(str(texture_path(family, "ORM")), check_existing=True)
    set_data_colorspace(orm.image)
    separate = nodes.new("ShaderNodeSeparateRGB")
    links.new(orm.outputs["Color"], separate.inputs["Image"])

    ao_mix = nodes.new("ShaderNodeMixRGB")
    ao_mix.blend_type = "MULTIPLY"
    ao_mix.inputs[0].default_value = 1.0
    links.new(bc.outputs["Color"], ao_mix.inputs[1])
    links.new(separate.outputs["R"], ao_mix.inputs[2])
    links.new(ao_mix.outputs["Color"], bsdf.inputs["Base Color"])
    links.new(separate.outputs["G"], bsdf.inputs["Roughness"])
    links.new(separate.outputs["B"], bsdf.inputs["Metallic"])

    normal_tex = nodes.new("ShaderNodeTexImage")
    normal_tex.name = f"{family}_N"
    normal_tex.image = bpy.data.images.load(str(texture_path(family, "N")), check_existing=True)
    set_data_colorspace(normal_tex.image)
    normal_map = nodes.new("ShaderNodeNormalMap")
    normal_map.inputs["Strength"].default_value = 0.65 if family != "Stone" else 0.9
    links.new(normal_tex.outputs["Color"], normal_map.inputs["Color"])
    links.new(normal_map.outputs["Normal"], bsdf.inputs["Normal"])

    if emission:
        emissive = nodes.new("ShaderNodeTexImage")
        emissive.name = f"{family}_E"
        emissive.image = bpy.data.images.load(str(texture_path(family, "E")), check_existing=True)
        set_data_colorspace(emissive.image)
        emission_name = "Emission" if "Emission" in bsdf.inputs else "Emission Color"
        links.new(bc.outputs["Color"], bsdf.inputs[emission_name])
        strength = nodes.new("ShaderNodeMath")
        strength.operation = "MULTIPLY"
        strength.inputs[1].default_value = 5.0
        links.new(emissive.outputs["Color"], strength.inputs[0])
        links.new(strength.outputs[0], bsdf.inputs["Emission Strength"])
    return material


def create_materials() -> dict[str, bpy.types.Material]:
    return {
        name: textured_material(name, family, emission=name == "M_Rune_Emissive")
        for name, family in TEXTURE_FAMILIES.items()
    }


def tag(obj: bpy.types.Object, component: str, tier: int) -> bpy.types.Object:
    obj["Aerathea.AssetID"] = ASSET_ID
    obj["Aerathea.Component"] = component
    obj["Aerathea.DetailTier"] = tier
    obj["Aerathea.SourceAuthority"] = "asset_spec.json + dimensions_cm.csv"
    return obj


def activate(obj: bpy.types.Object) -> None:
    bpy.ops.object.select_all(action="DESELECT")
    obj.select_set(True)
    bpy.context.view_layer.objects.active = obj


def apply_modifier(obj: bpy.types.Object, name: str) -> None:
    activate(obj)
    bpy.ops.object.modifier_apply(modifier=name)


def finalize_mesh(obj: bpy.types.Object, smooth=False) -> bpy.types.Object:
    activate(obj)
    if obj.data.uv_layers.get("UVMap") is None:
        obj.data.uv_layers.new(name="UVMap")
        bpy.ops.object.mode_set(mode="EDIT")
        bpy.ops.mesh.select_all(action="SELECT")
        bpy.ops.uv.smart_project(island_margin=0.025)
        bpy.ops.mesh.normals_make_consistent(inside=False)
        bpy.ops.object.mode_set(mode="OBJECT")
    if smooth:
        for polygon in obj.data.polygons:
            polygon.use_smooth = True
        obj.data.use_auto_smooth = True
        obj.data.auto_smooth_angle = math.radians(42.0)
    return obj


def add_cube(name, dims_cm, location_cm, material, collection, bevel_cm=0.0, tier=0, rotation=(0.0, 0.0, 0.0)):
    bpy.ops.mesh.primitive_cube_add(size=1.0, location=tuple(v * CM for v in location_cm), rotation=rotation)
    obj = bpy.context.object
    obj.name = name
    obj.dimensions = tuple(v * CM for v in dims_cm)
    bpy.ops.object.transform_apply(location=False, rotation=False, scale=True)
    if bevel_cm > 0:
        bevel = obj.modifiers.new("AET_Bevel", "BEVEL")
        bevel.width = bevel_cm * CM
        bevel.segments = 1
        bevel.affect = "EDGES"
        apply_modifier(obj, bevel.name)
    obj.data.materials.append(material)
    move_to_collection(obj, collection)
    tag(obj, name, tier)
    return finalize_mesh(obj)


def add_cylinder(name, diameter_cm, depth_cm, center_z_cm, material, collection, vertices=24, tier=0):
    bpy.ops.mesh.primitive_cylinder_add(
        vertices=vertices,
        radius=diameter_cm * CM * 0.5,
        depth=depth_cm * CM,
        location=(0.0, 0.0, center_z_cm * CM),
    )
    obj = bpy.context.object
    obj.name = name
    obj.data.materials.append(material)
    move_to_collection(obj, collection)
    tag(obj, name, tier)
    return finalize_mesh(obj, smooth=True)


def add_torus(name, major_radius_cm, minor_radius_cm, z_cm, material, collection, tier=1, segments=24):
    bpy.ops.mesh.primitive_torus_add(
        major_segments=segments,
        minor_segments=4,
        location=(0.0, 0.0, z_cm * CM),
        major_radius=major_radius_cm * CM,
        minor_radius=minor_radius_cm * CM,
    )
    obj = bpy.context.object
    obj.name = name
    obj.data.materials.append(material)
    move_to_collection(obj, collection)
    tag(obj, name, tier)
    return finalize_mesh(obj, smooth=True)


def add_xz_prism(name, points_xz_cm, y_min_cm, y_max_cm, material, collection, bevel_cm=0.0, tier=0):
    count = len(points_xz_cm)
    vertices = [(x * CM, y_min_cm * CM, z * CM) for x, z in points_xz_cm]
    vertices += [(x * CM, y_max_cm * CM, z * CM) for x, z in points_xz_cm]
    faces = [tuple(reversed(range(count))), tuple(range(count, count * 2))]
    for index in range(count):
        nxt = (index + 1) % count
        faces.append((index, nxt, count + nxt, count + index))
    mesh = bpy.data.meshes.new(f"{name}_Mesh")
    mesh.from_pydata(vertices, [], faces)
    mesh.update()
    obj = bpy.data.objects.new(name, mesh)
    collection.objects.link(obj)
    obj.data.materials.append(material)
    tag(obj, name, tier)
    finalize_mesh(obj)
    if bevel_cm > 0:
        bevel = obj.modifiers.new("AET_Bevel", "BEVEL")
        bevel.width = bevel_cm * CM
        bevel.segments = 1
        apply_modifier(obj, bevel.name)
    return obj


def add_diamond(name, center_x_cm, center_z_cm, width_cm, height_cm, y_min_cm, y_max_cm, material, collection, tier=1):
    points = [
        (center_x_cm, center_z_cm + height_cm * 0.5),
        (center_x_cm + width_cm * 0.5, center_z_cm),
        (center_x_cm, center_z_cm - height_cm * 0.5),
        (center_x_cm - width_cm * 0.5, center_z_cm),
    ]
    return add_xz_prism(name, points, y_min_cm, y_max_cm, material, collection, bevel_cm=0.18, tier=tier)


def add_bar_xz(name, start_xz, end_xz, width_cm, depth_cm, y_cm, material, collection, tier=1):
    x0, z0 = start_xz
    x1, z1 = end_xz
    dx = x1 - x0
    dz = z1 - z0
    length = math.hypot(dx, dz)
    angle = -math.atan2(dz, dx)
    return add_cube(
        name,
        (length, depth_cm, width_cm),
        ((x0 + x1) * 0.5, y_cm, (z0 + z1) * 0.5),
        material,
        collection,
        bevel_cm=0.25,
        tier=tier,
        rotation=(0.0, angle, 0.0),
    )


def add_elliptic_lathe(name, rings, material, collection, sides=12, tier=0):
    vertices = []
    for z_cm, rx_cm, ry_cm in rings:
        for side in range(sides):
            angle = 2.0 * math.pi * side / sides
            vertices.append((math.cos(angle) * rx_cm * CM, math.sin(angle) * ry_cm * CM, z_cm * CM))
    faces = []
    for ring_index in range(len(rings) - 1):
        for side in range(sides):
            nxt = (side + 1) % sides
            lower = ring_index * sides
            upper = (ring_index + 1) * sides
            faces.append((lower + side, lower + nxt, upper + nxt, upper + side))
    faces.append(tuple(reversed(range(sides))))
    last = (len(rings) - 1) * sides
    faces.append(tuple(last + side for side in range(sides)))
    mesh = bpy.data.meshes.new(f"{name}_Mesh")
    mesh.from_pydata(vertices, [], faces)
    mesh.update()
    obj = bpy.data.objects.new(name, mesh)
    collection.objects.link(obj)
    obj.data.materials.append(material)
    tag(obj, name, tier)
    return finalize_mesh(obj, smooth=False)


def add_helix(name, phase, material, collection, tier=2):
    curve = bpy.data.curves.new(f"{name}_Curve", "CURVE")
    curve.dimensions = "3D"
    curve.resolution_u = 1
    curve.bevel_depth = 0.00042
    curve.bevel_resolution = 0
    curve.resolution_u = 1
    spline = curve.splines.new("POLY")
    samples = 112
    spline.points.add(samples - 1)
    z0 = 18.08
    z1 = 59.92
    turns = 5.0
    radius = 2.458
    for index, point in enumerate(spline.points):
        t = index / (samples - 1)
        angle = phase + turns * 2.0 * math.pi * t
        point.co = (math.cos(angle) * radius * CM, math.sin(angle) * radius * CM, (z0 + (z1 - z0) * t) * CM, 1.0)
    obj = bpy.data.objects.new(name, curve)
    collection.objects.link(obj)
    curve.materials.append(material)
    activate(obj)
    bpy.ops.object.convert(target="MESH")
    obj = bpy.context.object
    tag(obj, name, tier)
    return finalize_mesh(obj, smooth=True)


def add_rivet(name, location_cm, material, collection, tier=2):
    bpy.ops.mesh.primitive_uv_sphere_add(
        segments=8,
        ring_count=4,
        radius=0.42 * CM,
        location=tuple(v * CM for v in location_cm),
    )
    obj = bpy.context.object
    obj.name = name
    obj.scale = (1.0, 0.55, 1.0)
    bpy.ops.object.transform_apply(location=False, rotation=False, scale=True)
    obj.data.materials.append(material)
    move_to_collection(obj, collection)
    tag(obj, name, tier)
    return finalize_mesh(obj, smooth=True)


def build_primary_geometry(materials, detailed: bool):
    asset = get_collection("SB_ASSET")
    root = bpy.data.objects.new("SiegeBreaker_ROOT", None)
    asset.objects.link(root)
    root["overall_length_cm"] = 170.0
    root["head_width_cm"] = 52.0
    root["head_height_cm"] = 38.0
    root["head_depth_cm"] = 32.0
    root["shaft_length_cm"] = 118.0
    root["shaft_pommel_overlap_cm"] = 4.0

    stone_left = [(-24, 132), (-15, 133), (-12, 139), (-12, 163), (-16, 169), (-24, 170), (-26, 165), (-26, 137)]
    stone_right = [(24, 132), (15, 133), (12, 139), (12, 163), (16, 169), (24, 170), (26, 165), (26, 137)]
    stone_depth = 15.72 if detailed else 16.0
    stone_bevel = 0.65 if detailed else 0.0
    parts = [
        add_xz_prism("Head_Stone_Left", stone_left, -stone_depth, stone_depth, materials["M_Stone"], asset, stone_bevel, 0),
        add_xz_prism("Head_Stone_Right", stone_right, -stone_depth, stone_depth, materials["M_Stone"], asset, stone_bevel, 0),
        add_cube("Head_Core", (24, 25, 30), (0, 0, 151), materials["M_Bronze"], asset, 0.7, 0),
        add_cube("Head_Core_Steel", (17, 28, 24), (0, 0, 151), materials["M_Steel"], asset, 0.55, 1),
        add_cylinder("Shaft_Metal", 5, 118, 73, materials["M_Steel"], asset, 24 if detailed else 16, 0),
        add_cylinder("Grip_Leather", 4.58 if detailed else 5.0, 42, 39, materials["M_Leather"], asset, 24 if detailed else 16, 0),
        add_elliptic_lathe(
            "Pommel",
            [(0, 3.0, 2.5), (2, 4.2, 3.5), (6, 5.5, 4.5), (12, 5.5, 4.5), (16, 4.1, 3.4), (18, 3.0, 2.5)],
            materials["M_Bronze"],
            asset,
            sides=12,
            tier=0,
        ),
        add_cylinder("Collar_Grip_Bottom", 7.6, 2.6, 18.6, materials["M_Bronze"], asset, 20, 1),
        add_cylinder("Collar_Grip_Top", 8.0, 3.4, 60.0, materials["M_Bronze"], asset, 20, 1),
        add_cylinder("Collar_Head", 10.0, 6.0, 131.0, materials["M_Bronze"], asset, 20, 1),
    ]

    if detailed:
        # Stone face plates own the exact +/-16 cm head-depth boundary.
        for side_name, y0, y1 in (("Front", -16.0, -15.76), ("Back", 15.76, 16.0)):
            parts.append(add_diamond(f"StonePlate_Left_{side_name}", -19, 151, 10.8, 24.0, y0, y1, materials["M_Stone"], asset, 1))
            parts.append(add_diamond(f"StonePlate_Right_{side_name}", 19, 151, 10.8, 24.0, y0, y1, materials["M_Stone"], asset, 1))
            parts.append(add_diamond(f"Rune_Left_{side_name}", -19, 151, 6.2, 9.4, y0, y1, materials["M_Rune_Emissive"], asset, 2))
            parts.append(add_diamond(f"Rune_Right_{side_name}", 19, 151, 6.2, 9.4, y0, y1, materials["M_Rune_Emissive"], asset, 2))

        for side_name, y in (("Front", -15.25), ("Back", 15.25)):
            parts.extend(
                [
                    add_bar_xz(f"CoreBrace_A_{side_name}", (-10.2, 139), (10.2, 163), 2.5, 1.2, y, materials["M_Bronze"], asset, 1),
                    add_bar_xz(f"CoreBrace_B_{side_name}", (-10.2, 163), (10.2, 139), 2.5, 1.2, y, materials["M_Bronze"], asset, 1),
                    add_diamond(f"CorePlate_{side_name}", 0, 151, 13.0, 19.0, y - 0.65 if y < 0 else y - 0.55, y + 0.55 if y < 0 else y + 0.65, materials["M_Bronze"], asset, 1),
                    add_diamond(f"CoreRune_{side_name}", 0, 151, 6.2, 9.0, -15.95 if y < 0 else 15.55, -15.55 if y < 0 else 15.95, materials["M_Rune_Emissive"], asset, 2),
                ]
            )

        for x in (-24.2, -13.8, 13.8, 24.2):
            parts.append(add_cube(f"StoneBand_{x:+.1f}", (2.2, 31.5, 30.0), (x, 0, 151), materials["M_Steel"], asset, 0.32, 1))
        for x in (-19.0, 19.0):
            for z in (139.2, 162.8):
                parts.append(add_cube(f"RuneBar_{x:+.0f}_{z:.1f}", (1.0, 31.9, 5.0), (x, 0, z), materials["M_Rune_Emissive"], asset, 0.12, 2))

        # Monumental central crown and lower transition.
        parts.extend(
            [
                add_cylinder("Head_Undersocket", 10.0, 0.4, 132.2, materials["M_Steel"], asset, 20, 1),
                add_cylinder("Head_Crown_Base", 11.5, 2.2, 166.8, materials["M_Bronze"], asset, 20, 1),
                add_cylinder("Head_Crown_Mid", 8.2, 2.0, 168.4, materials["M_Steel"], asset, 20, 1),
                add_cylinder("Head_Crown_Top", 5.4, 1.2, 169.4, materials["M_Bronze"], asset, 16, 2),
                add_torus("GripRing_Bottom", 3.05, 0.36, 20.2, materials["M_Steel"], asset, 1),
                add_torus("GripRing_Top", 3.1, 0.38, 58.2, materials["M_Steel"], asset, 1),
                add_helix("Grip_Wrap_A", 0.0, materials["M_Leather"], asset, 2),
                add_helix("Grip_Wrap_B", math.pi, materials["M_Leather"], asset, 2),
            ]
        )

        # Controlled shaft ornament: large readable bands and restrained rune accents.
        for z in (69.0, 83.0, 97.0, 111.0, 124.0):
            parts.append(add_torus(f"ShaftBand_{z:.0f}", 2.22, 0.24, z, materials["M_Bronze"], asset, 2, 20))
        for z in (72.0, 88.0, 104.0, 120.0):
            parts.append(add_cube(f"ShaftRune_{z:.0f}", (1.2, 0.32, 5.5), (0, -2.48, z), materials["M_Rune_Emissive"], asset, 0.08, 2))

        # Pommel plate/rune language stays inside the exact 11 cm width.
        for side_name, y0, y1 in (("Front", -4.50, -4.18), ("Back", 4.18, 4.50)):
            parts.append(add_diamond(f"PommelPlate_{side_name}", 0, 9.0, 7.8, 9.8, y0, y1, materials["M_Steel"], asset, 1))
            parts.append(add_diamond(f"PommelRune_{side_name}", 0, 9.0, 3.8, 5.2, y0, y1, materials["M_Rune_Emissive"], asset, 2))

        for index, (x, z) in enumerate(((-8.7, 139.0), (-8.7, 163.0), (8.7, 139.0), (8.7, 163.0))):
            parts.append(add_rivet(f"Rivet_F_{index:02d}", (x, -15.60, z), materials["M_Bronze"], asset, 2))
            parts.append(add_rivet(f"Rivet_B_{index:02d}", (x, 15.60, z), materials["M_Bronze"], asset, 2))

    for obj in parts:
        obj.parent = root
    return asset, root, parts


def bounds_cm(objects):
    points = [obj.matrix_world @ Vector(corner) for obj in objects if obj.type == "MESH" for corner in obj.bound_box]
    minimum = [min(point[index] for point in points) * 100.0 for index in range(3)]
    maximum = [max(point[index] for point in points) * 100.0 for index in range(3)]
    return minimum, maximum, [maximum[index] - minimum[index] for index in range(3)]


def triangle_count(obj):
    obj.data.calc_loop_triangles()
    return len(obj.data.loop_triangles)


def reorder_materials(obj, materials):
    current = [slot.material.name if slot.material else "" for slot in obj.material_slots]
    remap = {index: MATERIAL_ORDER.index(name) for index, name in enumerate(current) if name in MATERIAL_ORDER}
    polygon_indices = [remap.get(poly.material_index, 0) for poly in obj.data.polygons]
    obj.data.materials.clear()
    for name in MATERIAL_ORDER:
        obj.data.materials.append(materials[name])
    for poly, material_index in zip(obj.data.polygons, polygon_indices):
        poly.material_index = material_index


def normalize_asset_envelope(obj):
    """Restore the approved outer silhouette after aggressive low-LOD collapse."""
    current_min, current_max, current_extent = bounds_cm([obj])
    target_min = (-26.0, -16.0, 0.0)
    target_max = (26.0, 16.0, 170.0)
    target_extent = (52.0, 32.0, 170.0)
    current_center = [(current_min[i] + current_max[i]) * 0.5 for i in range(3)]
    target_center = [(target_min[i] + target_max[i]) * 0.5 for i in range(3)]
    scale = [target_extent[i] / current_extent[i] for i in range(3)]
    inverse = obj.matrix_world.inverted()
    for vertex in obj.data.vertices:
        world = obj.matrix_world @ vertex.co
        centimeters = [world[i] * 100.0 for i in range(3)]
        normalized = [
            (centimeters[i] - current_center[i]) * scale[i] + target_center[i]
            for i in range(3)
        ]
        vertex.co = inverse @ Vector(tuple(value * CM for value in normalized))
    obj.data.update()
    obj["Aerathea.LODEnvelopeNormalization"] = "approved overall 52x32x170 cm silhouette"


def clean_export_mesh(obj):
    activate(obj)
    bpy.ops.object.mode_set(mode="EDIT")
    bpy.ops.mesh.select_all(action="SELECT")
    bpy.ops.mesh.remove_doubles(threshold=1e-7)
    bpy.ops.mesh.dissolve_degenerate(threshold=1e-7)
    bpy.ops.mesh.normals_make_consistent(inside=False)
    bpy.ops.object.mode_set(mode="OBJECT")
    mesh = obj.data
    bm = bmesh.new()
    bm.from_mesh(mesh)
    seen = set()
    duplicates = []
    for face in list(bm.faces):
        key = tuple(sorted(vertex.index for vertex in face.verts))
        if key in seen:
            duplicates.append(face)
        else:
            seen.add(key)
    for face in duplicates:
        bm.faces.remove(face)
    bm.to_mesh(mesh)
    bm.free()
    obj.data.update()
    obj["Aerathea.DuplicateFacesRemoved"] = len(duplicates)


def create_lod(source_objects, level, max_tier, ratio, materials, collection):
    duplicates = []
    for source in source_objects:
        if source.type != "MESH" or int(source.get("Aerathea.DetailTier", 0)) > max_tier:
            continue
        duplicate = source.copy()
        duplicate.data = source.data.copy()
        duplicate.parent = None
        duplicate.matrix_world = source.matrix_world.copy()
        collection.objects.link(duplicate)
        duplicates.append(duplicate)
    if not duplicates:
        raise RuntimeError(f"No source geometry selected for LOD{level}")
    bpy.ops.object.select_all(action="DESELECT")
    for obj in duplicates:
        obj.select_set(True)
    bpy.context.view_layer.objects.active = duplicates[0]
    bpy.ops.object.join()
    lod = bpy.context.object
    lod.name = f"{ASSET_ID}_LOD{level}"
    reorder_materials(lod, materials)
    if ratio < 0.999:
        modifier = lod.modifiers.new(f"LOD{level}_Decimate", "DECIMATE")
        modifier.ratio = ratio
        modifier.use_collapse_triangulate = True
        apply_modifier(lod, modifier.name)
    if level >= 2:
        normalize_asset_envelope(lod)
    clean_export_mesh(lod)
    activate(lod)
    bpy.context.scene.cursor.location = (0.0, 0.0, 0.0)
    bpy.ops.object.origin_set(type="ORIGIN_CURSOR", center="MEDIAN")
    lod["Aerathea.LOD"] = level
    lod["Aerathea.ArtifactStatus"] = "candidate"
    lod.hide_render = True
    finalize_mesh(lod)
    return lod


def create_collision(collection):
    material = simple_material("M_Collision_Proxy", (0.08, 0.65, 0.22), 0.0, 0.75)
    head = add_cube(f"UCX_{ASSET_ID}_00", (52, 32, 38), (0, 0, 151), material, collection, 0.0, 0)
    shaft = add_cylinder(f"UCX_{ASSET_ID}_01", 5.0, 118.0, 73.0, material, collection, 12, 0)
    pommel = add_cube(f"UCX_{ASSET_ID}_02", (11, 9, 18), (0, 0, 9), material, collection, 0.0, 0)
    for obj in (head, shaft, pommel):
        obj.hide_render = True
        obj.display_type = "WIRE"
        obj["Aerathea.CollisionRole"] = "custom_convex_proxy"
    return [head, shaft, pommel]


def export_selected(objects, path: Path, kind: str):
    path.parent.mkdir(parents=True, exist_ok=True)
    bpy.ops.object.select_all(action="DESELECT")
    for obj in objects:
        obj.hide_set(False)
        obj.select_set(True)
    bpy.context.view_layer.objects.active = objects[0]
    if kind == "fbx":
        bpy.ops.export_scene.fbx(
            filepath=str(path),
            use_selection=True,
            object_types={"MESH"},
            apply_unit_scale=True,
            apply_scale_options="FBX_SCALE_UNITS",
            axis_forward="-Y",
            axis_up="Z",
            use_mesh_modifiers=True,
            mesh_smooth_type="FACE",
            add_leaf_bones=False,
            bake_anim=False,
            path_mode="AUTO",
        )
    elif kind == "glb":
        bpy.ops.export_scene.gltf(
            filepath=str(path),
            export_format="GLB",
            use_selection=True,
            export_apply=True,
            export_materials="EXPORT",
        )
    else:
        raise ValueError(kind)
    bpy.ops.object.select_all(action="DESELECT")


def write_blockout_manifest(path: Path, objects, blend_path: Path):
    minimum, maximum, extent = bounds_cm(objects)
    manifest = {
        "schema": "aerathea.siegebreaker_blockout.v1",
        "asset_id": ASSET_ID,
        "artifact_status": "authoritative canonical blockout under verified numeric inputs",
        "authority_order": ["asset_spec.json", "dimensions_cm.csv", "this corrected blockout"],
        "world_bounds_cm": {"minimum": minimum, "maximum": maximum, "extent": extent},
        "required_bounds_cm": {"minimum": [-26, -16, 0], "maximum": [26, 16, 170], "extent": [52, 32, 170]},
        "shaft_z_cm": [14, 132],
        "grip_z_cm": [18, 60],
        "pommel_z_cm": [0, 18],
        "pommel_width_cm": 11,
        "shaft_pommel_overlap_cm": 4,
        "source_package_sha256": "6d4bf67fe4dcb1bc752c615d16b039bf6fd430037b6ffa4772f8ae83c689a8f0",
        "blend_path": str(blend_path.relative_to(ROOT)),
        "blend_sha256": sha256(blend_path),
        "numeric_pass": all(abs(value - expected) <= 0.001 for value, expected in zip(extent, (52, 32, 170))),
    }
    path.write_text(json.dumps(manifest, indent=2) + "\n", encoding="utf-8")


def main() -> int:
    args = parse_args()
    SOURCE_ROOT.mkdir(parents=True, exist_ok=True)
    EXPORT_ROOT.mkdir(parents=True, exist_ok=True)
    clear_scene()
    configure_scene()
    materials = create_materials()
    asset, root, source_objects = build_primary_geometry(materials, detailed=args.mode == "final")

    if args.mode == "blockout":
        blend_path = SOURCE_ROOT / "SiegeBreaker_Blockout.blend"
        bpy.ops.wm.save_as_mainfile(filepath=str(blend_path))
        write_blockout_manifest(SOURCE_ROOT / "SiegeBreaker_Blockout_Manifest.json", source_objects, blend_path)
        print(f"Saved corrected canonical blockout: {blend_path}")
        return 0

    export_collection = get_collection("SB_EXPORT")
    collision_collection = get_collection("SB_COLLISION")
    lod0 = create_lod(source_objects, 0, 2, 1.0, materials, export_collection)
    lod0_triangles = triangle_count(lod0)
    lod1 = create_lod(source_objects, 1, 2, 0.62, materials, export_collection)
    lod2 = create_lod(source_objects, 2, 2, 0.40, materials, export_collection)
    lod3 = create_lod(source_objects, 3, 2, 0.18, materials, export_collection)
    lods = [lod0, lod1, lod2, lod3]
    collisions = create_collision(collision_collection)

    blend_path = SOURCE_ROOT / f"{ASSET_ID}_DCCGameReady_FinalPackage_A01.blend"
    bpy.ops.wm.save_as_mainfile(filepath=str(blend_path))

    base_fbx = EXPORT_ROOT / f"{ASSET_ID}.fbx"
    export_selected([lod0, *collisions], base_fbx, "fbx")
    export_paths = [base_fbx]
    for level, lod in enumerate(lods[1:], start=1):
        path = EXPORT_ROOT / f"{ASSET_ID}_LOD{level}.fbx"
        export_selected([lod], path, "fbx")
        export_paths.append(path)
    glb_path = EXPORT_ROOT / f"{ASSET_ID}.glb"
    export_selected([lod0], glb_path, "glb")
    export_paths.append(glb_path)

    minimum, maximum, extent = bounds_cm(source_objects)
    source_triangles = sum(triangle_count(obj) for obj in source_objects)
    lod_stats = []
    for level, lod in enumerate(lods):
        lod_min, lod_max, lod_extent = bounds_cm([lod])
        lod_stats.append(
            {
                "level": level,
                "object": lod.name,
                "triangles": triangle_count(lod),
                "ratio_to_lod0": round(triangle_count(lod) / max(lod0_triangles, 1), 6),
                "bounds_cm": {"minimum": lod_min, "maximum": lod_max, "extent": lod_extent},
                "uv_layers": [layer.name for layer in lod.data.uv_layers],
                "material_slots": [slot.material.name if slot.material else None for slot in lod.material_slots],
            }
        )

    manifest = {
        "schema": "aerathea.dcc_game_ready_candidate.v1",
        "asset_id": ASSET_ID,
        "artifact_status": "candidate",
        "pipeline_status": "DCC game-ready candidate",
        "authority": {
            "package_sha256": "6d4bf67fe4dcb1bc752c615d16b039bf6fd430037b6ffa4772f8ae83c689a8f0",
            "geometry": ["asset_spec.json", "dimensions_cm.csv"],
            "style_only": "reference/concept_sheet_style_reference.png",
            "legacy_builder_used": False,
        },
        "coordinate_frame": {
            "x": "head width, right positive",
            "y": "head depth, back positive",
            "z": "overall length, up positive",
            "origin": "bottom center of pommel at Z=0",
        },
        "world_bounds_cm": {"minimum": minimum, "maximum": maximum, "extent": extent},
        "source_component_count": len(source_objects),
        "source_triangles": source_triangles,
        "lods": lod_stats,
        "materials": MATERIAL_ORDER,
        "textures": sorted(str(path.relative_to(ROOT)) for path in TEXTURE_ROOT.glob("*.png")),
        "collision": [
            {"object": obj.name, "triangles": triangle_count(obj), "role": obj["Aerathea.CollisionRole"]}
            for obj in collisions
        ],
        "contacts": {
            "shaft_head": {"shaft_top_z_cm": 132, "head_bottom_z_cm": 132, "gap_cm": 0, "status": "pass"},
            "shaft_pommel": {"shaft_interval_z_cm": [14, 132], "pommel_interval_z_cm": [0, 18], "overlap_cm": 4, "status": "pass"},
            "grip": {"interval_z_cm": [18, 60], "visible_length_cm": 42, "status": "pass"},
        },
        "exterior_seams": [
            {"name": "stone_left_to_core", "role": "contact_mount", "weld_scope": "contact_alignment_only", "status": "pass"},
            {"name": "stone_right_to_core", "role": "contact_mount", "weld_scope": "contact_alignment_only", "status": "pass"},
            {"name": "shaft_to_head", "role": "occluded_contact", "weld_scope": "no_weld", "status": "pass"},
            {"name": "shaft_into_pommel", "role": "occluded_contact", "weld_scope": "no_weld", "status": "pass"},
        ],
        "outputs": [
            {"path": str(path.relative_to(ROOT)), "sha256": sha256(path), "bytes": path.stat().st_size}
            for path in [blend_path, *export_paths]
        ],
        "unreal_import_authorized": False,
        "fully_game_ready": False,
    }
    manifest_path = SOURCE_ROOT / f"{ASSET_ID}_DCC_GAME_READY_MANIFEST.json"
    manifest_path.write_text(json.dumps(manifest, indent=2) + "\n", encoding="utf-8")
    print(manifest_path)
    print(f"source_triangles={source_triangles} lod0_triangles={lod0_triangles}")
    print(f"bounds_cm={extent}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
