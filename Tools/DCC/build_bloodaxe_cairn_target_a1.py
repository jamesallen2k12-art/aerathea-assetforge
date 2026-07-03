#!/usr/bin/env python3
"""Build Blood Axe cairn target A1 DCC source candidate.

Run with:
    blender --background --python Tools/DCC/build_bloodaxe_cairn_target_a1.py

This build is targeted at the clearer BloodAxe A1 concept image:
docs/assets/visual_canon/BloodAxeCairnTargets_A01/VC_GIA_BloodAxe_CairnTarget_A1.png

The output is a DCC source candidate for concept-geometry review. It should not
be treated as fully game-ready or imported to Unreal until the side-by-side
comparison against the source target passes visual approval.
"""

from __future__ import annotations

import math
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
REVIEW_ROOT = ROOT / "Saved" / "Automation" / "DCC" / "SM_GIA_BloodAxeCairnTarget_A1_A01"

ASSET_NAME = "SM_GIA_BloodAxeCairnTarget_A1_A01"
REL_PATH = f"Props/Giants/BloodAxe/CairnTargets/A1/{ASSET_NAME}"
UNREAL_PATH = f"/Game/Aerathea/Props/Giants/BloodAxe/CairnTargets/A1/{ASSET_NAME}"
SOURCE_TARGET = "docs/assets/visual_canon/BloodAxeCairnTargets_A01/VC_GIA_BloodAxe_CairnTarget_A1.png"

sys.path.insert(0, str(ROOT))

from Tools.DCC.build_next_slice_assets import add_asset_metadata, clear_scene, setup_scene  # noqa: E402


def ensure_dir(path: Path) -> None:
    path.mkdir(parents=True, exist_ok=True)


def deterministic_noise(x: int, y: int, seed: int) -> float:
    value = (x * 374761393 + y * 668265263 + seed * 2654435761) & 0xFFFFFFFF
    value = (value ^ (value >> 13)) * 1274126177 & 0xFFFFFFFF
    return ((value ^ (value >> 16)) & 0xFFFF) / 65535.0


def clamp(value: float) -> float:
    return max(0.0, min(1.0, value))


def save_texture(path: Path, width: int, height: int, pixels: array) -> None:
    ensure_dir(path.parent)
    image = bpy.data.images.new(path.stem, width=width, height=height, alpha=True, float_buffer=False)
    image.pixels.foreach_set(pixels)
    image.filepath_raw = str(path)
    image.file_format = "PNG"
    image.save()
    bpy.data.images.remove(image)


def generate_texture_set(label: str, base: tuple[float, float, float], accent: tuple[float, float, float], seed: int) -> dict[str, Path]:
    texture_dir = TEXTURE_ROOT / REL_PATH
    ensure_dir(texture_dir)
    width = 512
    height = 512
    bc = array("f")
    normal = array("f")
    orm = array("f")
    for y in range(height):
        for x in range(width):
            n1 = deterministic_noise(x, y, seed)
            n2 = deterministic_noise(x // 5, y // 5, seed + 17)
            vein = 1.0 if deterministic_noise(x // 29, y // 23, seed + 41) > 0.94 else 0.0
            chip = 1.0 if deterministic_noise(x // 13, y // 19, seed + 71) > 0.985 else 0.0
            mix = ((n1 * 0.34) + (n2 * 0.24) + (vein * 0.07) + (chip * 0.05)) * 0.68
            color = (
                base[0] * (1.0 - mix) + accent[0] * mix,
                base[1] * (1.0 - mix) + accent[1] * mix,
                base[2] * (1.0 - mix) + accent[2] * mix,
            )
            if chip:
                color = (min(color[0] + 0.10, 1.0), min(color[1] + 0.085, 1.0), min(color[2] + 0.065, 1.0))
            bc.extend((clamp(color[0]), clamp(color[1]), clamp(color[2]), 1.0))

            bump = ((n1 - 0.5) * 0.18) + ((n2 - 0.5) * 0.08)
            normal.extend((clamp(0.5 + bump), clamp(0.5 + (deterministic_noise(x, y, seed + 101) - 0.5) * 0.12), 1.0, 1.0))
            occlusion = 0.56 + (1.0 - n2) * 0.26
            roughness = 0.84 + n1 * 0.12
            orm.extend((clamp(occlusion), clamp(roughness), 0.0, 1.0))

    file_label = label.replace(" ", "")
    paths = {
        "bc": texture_dir / f"T_GIA_BloodAxeCairnTarget_A1_A01_{file_label}_BC.png",
        "n": texture_dir / f"T_GIA_BloodAxeCairnTarget_A1_A01_{file_label}_N.png",
        "orm": texture_dir / f"T_GIA_BloodAxeCairnTarget_A1_A01_{file_label}_ORM.png",
    }
    save_texture(paths["bc"], width, height, bc)
    save_texture(paths["n"], width, height, normal)
    save_texture(paths["orm"], width, height, orm)
    return paths


def generate_textures() -> dict[str, dict[str, Path]]:
    return {
        "stone": generate_texture_set("Stone", (0.22, 0.215, 0.19), (0.58, 0.52, 0.42), 5103),
        "earth": generate_texture_set("Earth", (0.18, 0.115, 0.07), (0.50, 0.32, 0.17), 6207),
        "rawhide": generate_texture_set("Rawhide", (0.42, 0.23, 0.09), (0.78, 0.50, 0.22), 7301),
        "red": generate_texture_set("RedPaint", (0.62, 0.055, 0.040), (1.0, 0.17, 0.07), 8409),
    }


def make_texture_material(name: str, textures: dict[str, Path], roughness: float, review_color: tuple[float, float, float]) -> bpy.types.Material:
    material = bpy.data.materials.new(name)
    material.diffuse_color = (review_color[0], review_color[1], review_color[2], 1.0)
    material.use_nodes = True
    nodes = material.node_tree.nodes
    bsdf = nodes.get("Principled BSDF")
    if bsdf is None:
        return material

    material["Aerathea.TextureBC"] = str(textures["bc"].relative_to(ROOT))
    material["Aerathea.TextureN"] = str(textures["n"].relative_to(ROOT))
    material["Aerathea.TextureORM"] = str(textures["orm"].relative_to(ROOT))
    bsdf.inputs["Base Color"].default_value = (review_color[0], review_color[1], review_color[2], 1.0)
    bsdf.inputs["Roughness"].default_value = roughness
    bsdf.inputs["Metallic"].default_value = 0.0
    return material


def make_materials(texture_paths: dict[str, dict[str, Path]]) -> dict[str, bpy.types.Material]:
    return {
        "stone": make_texture_material("M_GIA_BloodAxeCairnTarget_A1_A01_Stone", texture_paths["stone"], 0.91, (0.42, 0.39, 0.32)),
        "earth": make_texture_material("M_GIA_BloodAxeCairnTarget_A1_A01_Earth", texture_paths["earth"], 0.95, (0.27, 0.17, 0.09)),
        "rawhide": make_texture_material("M_GIA_BloodAxeCairnTarget_A1_A01_Rawhide", texture_paths["rawhide"], 0.86, (0.58, 0.34, 0.13)),
        "red": make_texture_material("M_GIA_BloodAxeCairnTarget_A1_A01_RedPaint", texture_paths["red"], 0.78, (0.72, 0.045, 0.035)),
    }


def make_collection(name: str, hidden: bool = False) -> bpy.types.Collection:
    collection = bpy.data.collections.new(name)
    bpy.context.scene.collection.children.link(collection)
    collection.hide_viewport = hidden
    collection.hide_render = hidden
    return collection


def move_to_collection(obj: bpy.types.Object, collection: bpy.types.Collection) -> None:
    for current in list(obj.users_collection):
        current.objects.unlink(obj)
    collection.objects.link(obj)


def set_active(obj: bpy.types.Object) -> None:
    bpy.ops.object.select_all(action="DESELECT")
    bpy.context.view_layer.objects.active = obj
    obj.select_set(True)


def roughen_mesh(obj: bpy.types.Object, amount: float, seed: int) -> None:
    for index, vertex in enumerate(obj.data.vertices):
        n1 = deterministic_noise(index, seed, seed + 13) - 0.5
        n2 = deterministic_noise(seed, index, seed + 29) - 0.5
        n3 = deterministic_noise(index + 5, seed + 7, seed + 43) - 0.5
        vertex.co.x += n1 * amount
        vertex.co.y += n2 * amount
        vertex.co.z += n3 * amount * 0.75


def add_rough_box(
    name: str,
    collection: bpy.types.Collection,
    material: bpy.types.Material,
    location: tuple[float, float, float],
    dimensions: tuple[float, float, float],
    rotation: tuple[float, float, float],
    seed: int,
    bevel_scale: float = 0.055,
    rough_scale: float = 0.12,
) -> bpy.types.Object:
    bpy.ops.mesh.primitive_cube_add(size=1.0, location=location, rotation=rotation)
    obj = bpy.context.object
    obj.name = name
    obj.dimensions = dimensions
    obj.data.materials.append(material)
    set_active(obj)
    bpy.ops.object.transform_apply(location=False, rotation=False, scale=True)
    bevel_width = max(0.45, min(dimensions) * bevel_scale)
    bevel = obj.modifiers.new(f"{name}_BrokenEdgeBevel", "BEVEL")
    bevel.width = bevel_width
    bevel.segments = 1
    bevel.affect = "EDGES"
    bpy.ops.object.modifier_apply(modifier=bevel.name)
    roughen_mesh(obj, min(dimensions) * rough_scale, seed)
    bpy.ops.object.shade_flat()
    move_to_collection(obj, collection)
    return obj


def add_tapered_slab(
    name: str,
    collection: bpy.types.Collection,
    material: bpy.types.Material,
    location: tuple[float, float, float],
    dimensions: tuple[float, float, float],
    rotation: tuple[float, float, float],
    seed: int,
    top_scale_x: float = 0.72,
    top_scale_y: float = 0.86,
    top_offset: tuple[float, float] = (0.0, 0.0),
    bevel_scale: float = 0.045,
    rough_scale: float = 0.115,
) -> bpy.types.Object:
    width, depth, height = dimensions
    bx = width * 0.5
    by = depth * 0.5
    tx = width * top_scale_x * 0.5
    ty = depth * top_scale_y * 0.5
    ox, oy = top_offset
    verts = [
        (-bx, -by, -height * 0.5),
        (bx, -by, -height * 0.5),
        (bx * 0.94, by, -height * 0.5),
        (-bx * 0.88, by, -height * 0.5),
        (-tx + ox, -ty + oy, height * 0.5),
        (tx + ox, -ty + oy, height * 0.5),
        (tx * 0.86 + ox, ty + oy, height * 0.5),
        (-tx * 0.94 + ox, ty + oy, height * 0.5),
    ]
    faces = [
        (0, 1, 2, 3),
        (4, 7, 6, 5),
        (0, 4, 5, 1),
        (1, 5, 6, 2),
        (2, 6, 7, 3),
        (3, 7, 4, 0),
    ]
    mesh = bpy.data.meshes.new(f"{name}_Mesh")
    mesh.from_pydata(verts, [], faces)
    mesh.update()
    obj = bpy.data.objects.new(name, mesh)
    obj.location = location
    obj.rotation_euler = rotation
    obj.data.materials.append(material)
    collection.objects.link(obj)
    set_active(obj)
    bevel_width = max(0.35, min(dimensions) * bevel_scale)
    bevel = obj.modifiers.new(f"{name}_BrokenEdgeBevel", "BEVEL")
    bevel.width = bevel_width
    bevel.segments = 1
    bevel.affect = "EDGES"
    bpy.ops.object.modifier_apply(modifier=bevel.name)
    roughen_mesh(obj, min(dimensions) * rough_scale, seed)
    bpy.ops.object.shade_flat()
    return obj


def add_paint_strip(
    name: str,
    collection: bpy.types.Collection,
    material: bpy.types.Material,
    location: tuple[float, float, float],
    dimensions: tuple[float, float, float],
    rotation: tuple[float, float, float],
    seed: int,
) -> bpy.types.Object:
    return add_rough_box(name, collection, material, location, dimensions, rotation, seed, bevel_scale=0.16, rough_scale=0.035)


def add_small_stone(
    name: str,
    collection: bpy.types.Collection,
    material: bpy.types.Material,
    location: tuple[float, float, float],
    scale: tuple[float, float, float],
    rotation: tuple[float, float, float],
    seed: int,
) -> bpy.types.Object:
    bpy.ops.mesh.primitive_ico_sphere_add(subdivisions=1, radius=1.0, location=location, rotation=rotation)
    obj = bpy.context.object
    obj.name = name
    obj.scale = scale
    obj.data.materials.append(material)
    set_active(obj)
    bpy.ops.object.transform_apply(location=False, rotation=False, scale=True)
    roughen_mesh(obj, min(scale) * 0.18, seed)
    bpy.ops.object.shade_flat()
    move_to_collection(obj, collection)
    return obj


def add_irregular_ground(
    name: str,
    collection: bpy.types.Collection,
    material: bpy.types.Material,
    radius_x: float,
    radius_y: float,
    depth: float,
    segments: int,
    seed: int,
    location: tuple[float, float, float] = (0.0, 0.0, 0.0),
) -> bpy.types.Object:
    verts: list[tuple[float, float, float]] = []
    bottom: list[int] = []
    top: list[int] = []
    for index in range(segments):
        angle = (math.tau * index) / segments
        front_bias = 0.82 if math.sin(angle) < -0.45 else 1.0
        rear_bias = 1.12 if math.sin(angle) > 0.50 else 1.0
        n = 0.78 + deterministic_noise(index, seed, seed + 5) * 0.32
        x = math.cos(angle) * radius_x * n
        y = math.sin(angle) * radius_y * (0.78 + deterministic_noise(seed, index, seed + 9) * 0.27) * front_bias * rear_bias
        bottom.append(len(verts))
        verts.append((x, y, 0.0))
        top.append(len(verts))
        verts.append((x * 0.93, y * 0.91, depth + deterministic_noise(index, seed + 3, seed + 11) * 3.0))
    bottom_center = len(verts)
    verts.append((0.0, 0.0, 0.0))
    top_center = len(verts)
    verts.append((0.0, 0.0, depth + 1.5))
    faces: list[tuple[int, ...]] = []
    for index in range(segments):
        next_index = (index + 1) % segments
        faces.append((bottom[index], bottom[next_index], top[next_index], top[index]))
        faces.append((bottom_center, bottom[index], bottom[next_index]))
        faces.append((top_center, top[next_index], top[index]))
    mesh = bpy.data.meshes.new(f"{name}_Mesh")
    mesh.from_pydata(verts, [], faces)
    mesh.update()
    obj = bpy.data.objects.new(name, mesh)
    obj.location = location
    obj.data.materials.append(material)
    collection.objects.link(obj)
    return obj


def add_lod_ground(collection: bpy.types.Collection, materials: dict[str, bpy.types.Material], lod: int) -> list[bpy.types.Object]:
    objects: list[bpy.types.Object] = []
    segments = 42 if lod == 0 else 28 if lod == 1 else 18 if lod == 2 else 12
    objects.append(add_irregular_ground(f"LOD{lod}_IrregularMudAshTerrainContact", collection, materials["earth"], 190.0, 145.0, 8.0, segments, 101 + lod))
    if lod <= 1:
        objects.append(add_irregular_ground(f"LOD{lod}_FrontBrokenMudLip", collection, materials["earth"], 132.0, 58.0, 4.5, 20, 121 + lod, (-20.0, -72.0, 5.0)))
        objects.append(add_irregular_ground(f"LOD{lod}_RearAshAndStoneScatter", collection, materials["earth"], 112.0, 76.0, 4.0, 18, 141 + lod, (16.0, 86.0, 5.0)))
    return objects


def build_asset_lod(collection: bpy.types.Collection, materials: dict[str, bpy.types.Material], lod: int) -> list[bpy.types.Object]:
    objects = add_lod_ground(collection, materials, lod)
    prefix = f"LOD{lod}"
    detail = lod == 0
    mid = lod <= 1
    low = lod <= 2

    slab_specs = [
        ("DominantDiagonalFrontSlab", (-4, -38, 67), (192, 34, 132), (math.radians(-25), math.radians(-7), math.radians(-14)), 201, 0.68, 0.80, (-18.0, 3.0)),
        ("TallRearOathSlab", (38, 51, 113), (82, 40, 186), (math.radians(-7), math.radians(9), math.radians(-9)), 202, 0.62, 0.86, (-8.0, 2.0)),
        ("RightUprightSupportStone", (122, -3, 68), (50, 34, 108), (math.radians(3), math.radians(-8), math.radians(8)), 206, 0.58, 0.86, (4.0, 1.0)),
        ("RightRearSupportStone", (154, 36, 65), (42, 32, 94), (math.radians(-5), math.radians(6), math.radians(15)), 207, 0.60, 0.86, (-2.0, 0.0)),
    ]
    primary_specs = [
        ("LeftBundledStackLowSlab", (-117, -25, 34), (112, 44, 24), (math.radians(2), math.radians(-7), math.radians(8)), 203),
        ("LeftBundledStackMidSlab", (-127, -26, 57), (98, 40, 22), (math.radians(-1), math.radians(5), math.radians(-6)), 204),
        ("LeftBundledStackTopSlab", (-112, -23, 79), (84, 35, 20), (math.radians(4), math.radians(-5), math.radians(13)), 205),
        ("RearLowCounterweight", (-42, 56, 48), (132, 42, 42), (math.radians(-4), math.radians(4), math.radians(10)), 208),
    ]
    if low:
        primary_specs.extend(
            [
                ("FrontBrokenFootStone", (42, -92, 30), (122, 34, 28), (math.radians(3), math.radians(4), math.radians(-5)), 209),
                ("RearGroundLockStone", (26, 118, 33), (142, 36, 30), (math.radians(2), math.radians(-4), math.radians(2)), 210),
            ]
        )
    if mid:
        primary_specs.extend(
            [
                ("LeftBackBrokenShard", (-166, 20, 48), (42, 32, 72), (math.radians(-7), math.radians(8), math.radians(-18)), 211),
                ("RearNeedleShardLeft", (-8, 72, 91), (26, 22, 96), (math.radians(-11), math.radians(-7), math.radians(7)), 212),
                ("RearNeedleShardRight", (92, 92, 78), (30, 24, 80), (math.radians(8), math.radians(5), math.radians(21)), 213),
            ]
        )
    if detail:
        primary_specs.extend(
            [
                ("FrontLeftGroundShard", (-62, -107, 25), (58, 26, 32), (math.radians(5), math.radians(7), math.radians(-23)), 214),
                ("FarRightSmallSupportShard", (179, -34, 44), (27, 24, 58), (math.radians(5), math.radians(-8), math.radians(18)), 215),
                ("BackLeftButtressShard", (-116, 95, 41), (74, 38, 54), (math.radians(-8), math.radians(-4), math.radians(-14)), 216),
                ("BackRightButtressShard", (128, 102, 44), (74, 34, 58), (math.radians(5), math.radians(7), math.radians(14)), 217),
            ]
        )

    for label, location, dimensions, rotation, seed, top_scale_x, top_scale_y, top_offset in slab_specs:
        objects.append(
            add_tapered_slab(
                f"{prefix}_Stone_{label}",
                collection,
                materials["stone"],
                location,
                dimensions,
                rotation,
                seed + lod * 31,
                top_scale_x,
                top_scale_y,
                top_offset,
            )
        )

    for label, location, dimensions, rotation, seed in primary_specs:
        objects.append(add_rough_box(f"{prefix}_Stone_{label}", collection, materials["stone"], location, dimensions, rotation, seed + lod * 31))

    if mid:
        paint_specs = [
            ("MainDiagonalAxeStroke", (-17, -79, 91), (132, 8, 2.4), (math.radians(-25), math.radians(-7), math.radians(-17)), 301),
            ("MainCrossAxeStrokeUpper", (-38, -80, 105), (74, 7, 2.4), (math.radians(-25), math.radians(-7), math.radians(26)), 302),
            ("MainCrossAxeStrokeLower", (30, -78, 75), (82, 7, 2.4), (math.radians(-25), math.radians(-7), math.radians(-46)), 303),
            ("LeftStackRedSmear", (-126, -50, 70), (70, 6, 2.1), (math.radians(2), math.radians(-6), math.radians(5)), 304),
            ("RearSlabSmallWarMark", (53, 18, 142), (52, 6, 2.0), (math.radians(-7), math.radians(9), math.radians(-32)), 305),
        ]
        if lod == 0:
            paint_specs.extend(
                [
                    ("MainShortRaggedBottomStroke", (12, -77, 58), (56, 6, 2.0), (math.radians(-25), math.radians(-7), math.radians(8)), 306),
                    ("RightSupportSmallMark", (128, -31, 77), (40, 5, 2.0), (math.radians(3), math.radians(-9), math.radians(36)), 307),
                ]
            )
        for label, location, dimensions, rotation, seed in paint_specs:
            objects.append(add_paint_strip(f"{prefix}_BloodAxePaint_{label}", collection, materials["red"], location, dimensions, rotation, seed + lod * 37))

    if detail:
        rawhide_specs = [
            ("LeftStackBindingVerticalA", (-152, -52, 60), (7, 6, 78), (math.radians(3), math.radians(-3), math.radians(3)), 401),
            ("LeftStackBindingVerticalB", (-92, -51, 60), (7, 6, 75), (math.radians(1), math.radians(4), math.radians(-5)), 402),
            ("LeftStackBindingDiagonalA", (-121, -53, 60), (86, 6, 5), (math.radians(2), math.radians(-4), math.radians(37)), 403),
            ("LeftStackBindingDiagonalB", (-121, -54, 58), (82, 6, 5), (math.radians(2), math.radians(-4), math.radians(-35)), 404),
            ("RightSupportRawhideTie", (137, -33, 63), (54, 6, 5), (math.radians(5), math.radians(-8), math.radians(91)), 405),
            ("RearCounterweightBinding", (-30, 103, 53), (86, 6, 5), (math.radians(-4), math.radians(4), math.radians(77)), 406),
        ]
        for label, location, dimensions, rotation, seed in rawhide_specs:
            objects.append(add_paint_strip(f"{prefix}_Rawhide_{label}", collection, materials["rawhide"], location, dimensions, rotation, seed))

        pebble_specs = [
            (-152, -82, 16, (18, 12, 8), 501),
            (-96, -106, 15, (20, 13, 8), 502),
            (-30, -118, 14, (14, 11, 7), 503),
            (70, -112, 16, (21, 12, 8), 504),
            (142, -82, 17, (16, 12, 9), 505),
            (182, 34, 18, (18, 13, 10), 506),
            (-182, 36, 17, (22, 14, 10), 507),
            (3, 97, 18, (18, 13, 9), 508),
            (-124, 125, 17, (21, 14, 10), 509),
            (-48, 148, 16, (17, 12, 8), 510),
            (52, 151, 16, (19, 13, 9), 511),
            (136, 118, 18, (22, 14, 10), 512),
        ]
        for x, y, z, scale, seed in pebble_specs:
            objects.append(
                add_small_stone(
                    f"{prefix}_LooseGroundStone_{seed}",
                    collection,
                    materials["stone"],
                    (x, y, z),
                    scale,
                    (math.radians(seed % 17), math.radians(seed % 11), math.radians(seed % 29)),
                    seed,
                )
            )

    return objects


def add_collision_proxy(collection: bpy.types.Collection, material: bpy.types.Material) -> bpy.types.Object:
    obj = add_rough_box(
        f"UCX_{ASSET_NAME}_00",
        collection,
        material,
        (0.0, 8.0, 82.0),
        (392.0, 318.0, 184.0),
        (0.0, 0.0, 0.0),
        9001,
        bevel_scale=0.01,
        rough_scale=0.0,
    )
    obj.hide_viewport = True
    obj.hide_render = True
    return obj


def object_triangles(objects: list[bpy.types.Object]) -> int:
    total = 0
    for obj in objects:
        if obj.type != "MESH":
            continue
        total += sum(max(1, len(poly.vertices) - 2) for poly in obj.data.polygons)
    return total


def export_objects(objects: list[bpy.types.Object], path: Path) -> None:
    ensure_dir(path.parent)
    collection_states: list[tuple[bpy.types.Collection, bool, bool]] = []
    object_states: list[tuple[bpy.types.Object, bool, bool, bool]] = []
    seen_collections: set[str] = set()
    for obj in objects:
        object_states.append((obj, obj.hide_viewport, obj.hide_render, obj.hide_get()))
        obj.hide_viewport = False
        obj.hide_render = False
        obj.hide_set(False)
        for collection in obj.users_collection:
            if collection.name in seen_collections:
                continue
            seen_collections.add(collection.name)
            collection_states.append((collection, collection.hide_viewport, collection.hide_render))
            collection.hide_viewport = False
            collection.hide_render = False
    bpy.context.view_layer.update()

    bpy.ops.object.select_all(action="DESELECT")
    for obj in objects:
        obj.select_set(True)
    bpy.context.view_layer.objects.active = objects[0]
    try:
        bpy.ops.export_scene.fbx(
            filepath=str(path),
            use_selection=True,
            object_types={"MESH"},
            apply_unit_scale=True,
            apply_scale_options="FBX_SCALE_UNITS",
            add_leaf_bones=False,
            bake_space_transform=False,
            mesh_smooth_type="FACE",
        )
    finally:
        for obj, hide_viewport, hide_render, hide_get in object_states:
            obj.hide_viewport = hide_viewport
            obj.hide_render = hide_render
            obj.hide_set(hide_get)
        for collection, hide_viewport, hide_render in collection_states:
            collection.hide_viewport = hide_viewport
            collection.hide_render = hide_render
        bpy.ops.object.select_all(action="DESELECT")
        bpy.context.view_layer.update()


def look_at(camera: bpy.types.Object, target: Vector) -> None:
    direction = target - camera.location
    camera.rotation_euler = direction.to_track_quat("-Z", "Y").to_euler()


def configure_review_scene() -> tuple[bpy.types.Object, Vector]:
    world = bpy.context.scene.world or bpy.data.worlds.new("AeratheaDCCWorld")
    bpy.context.scene.world = world
    world.color = (0.70, 0.70, 0.70)

    scene = bpy.context.scene
    scene.view_settings.view_transform = "Standard"
    scene.view_settings.look = "None"
    scene.view_settings.exposure = 1.18
    scene.view_settings.gamma = 1.0

    bpy.ops.object.light_add(type="AREA", location=(-260, -320, 430))
    key = bpy.context.object
    key.name = "AET_DCC_Key_Area"
    key.data.energy = 2400.0
    key.data.size = 430.0

    bpy.ops.object.light_add(type="POINT", location=(280, -240, 190))
    fill = bpy.context.object
    fill.name = "AET_DCC_Fill_Point"
    fill.data.energy = 780.0
    fill.data.shadow_soft_size = 380.0

    bpy.ops.object.light_add(type="AREA", location=(250, 340, 270))
    rim = bpy.context.object
    rim.name = "AET_DCC_Back_Rim_Area"
    rim.data.energy = 980.0
    rim.data.size = 360.0

    bpy.ops.object.camera_add(location=(315, -430, 220))
    camera = bpy.context.object
    camera.name = "AET_DCC_ReviewCamera"
    camera.data.type = "ORTHO"
    camera.data.ortho_scale = 385.0
    camera.data.lens = 45
    camera.data.sensor_width = 32
    bpy.context.scene.camera = camera
    target = Vector((0.0, -2.0, 75.0))
    look_at(camera, target)
    return camera, target


def render_view(camera: bpy.types.Object, target: Vector, location: tuple[float, float, float], path: Path, resolution: tuple[int, int]) -> None:
    camera.location = location
    look_at(camera, target)
    ensure_dir(path.parent)
    scene = bpy.context.scene
    scene.render.resolution_x = resolution[0]
    scene.render.resolution_y = resolution[1]
    if hasattr(scene, "eevee"):
        scene.eevee.taa_render_samples = 16
    scene.render.filepath = str(path)
    bpy.ops.render.render(write_still=True)


def compose_review_board(image_paths: list[Path], output_path: Path, tile_width: int, tile_height: int) -> None:
    cols = 3
    rows = 2
    board_width = tile_width * cols
    board_height = tile_height * rows
    board = array("f", [0.055] * (board_width * board_height * 4))
    for pixel in range(3, len(board), 4):
        board[pixel] = 1.0

    for tile_index, path in enumerate(image_paths):
        image = bpy.data.images.load(str(path))
        pixels = array("f", [0.0] * (tile_width * tile_height * 4))
        image.pixels.foreach_get(pixels)
        col = tile_index % cols
        row = tile_index // cols
        x_offset = col * tile_width
        y_offset = (rows - 1 - row) * tile_height
        for y in range(tile_height):
            for x in range(tile_width):
                src_index = ((y * tile_width) + x) * 4
                dst_index = (((y + y_offset) * board_width) + (x + x_offset)) * 4
                board[dst_index : dst_index + 4] = pixels[src_index : src_index + 4]
        bpy.data.images.remove(image)

    ensure_dir(output_path.parent)
    board_image = bpy.data.images.new(output_path.stem, width=board_width, height=board_height, alpha=True, float_buffer=False)
    board_image.pixels.foreach_set(board)
    board_image.filepath_raw = str(output_path)
    board_image.file_format = "PNG"
    board_image.save()
    bpy.data.images.remove(board_image)


def add_metadata_to_objects(objects: list[bpy.types.Object]) -> None:
    add_asset_metadata(
        ASSET_NAME,
        f"DCC source candidate pending concept-geometry review against {SOURCE_TARGET}",
        UNREAL_PATH,
    )
    for obj in objects:
        obj["Aerathea.Asset"] = ASSET_NAME
        obj["Aerathea.UnrealPath"] = UNREAL_PATH
        obj["Aerathea.AssetType"] = "Static Mesh"
        obj["Aerathea.Faction"] = "Blood Axe Giants"
        obj["Aerathea.Status"] = "dcc_source_candidate_pending_concept_geometry_review"
        obj["Aerathea.SourceTarget"] = SOURCE_TARGET
        obj["Aerathea.SourceMethod"] = "hand_authored_dcc_candidate_against_clear_bloodaxe_a1_multiview_target"
        obj["Aerathea.Collision"] = "broad_ucx_hull_for_primary_slab_cluster_only"


def main() -> None:
    clear_scene()
    setup_scene()
    texture_paths = generate_textures()
    materials = make_materials(texture_paths)

    lod0_collection = make_collection(f"{ASSET_NAME}_LOD0")
    lod1_collection = make_collection(f"{ASSET_NAME}_LOD1", hidden=True)
    lod2_collection = make_collection(f"{ASSET_NAME}_LOD2", hidden=True)
    lod3_collection = make_collection(f"{ASSET_NAME}_LOD3", hidden=True)
    collision_collection = make_collection(f"{ASSET_NAME}_Collision", hidden=True)

    lod0_objects = build_asset_lod(lod0_collection, materials, 0)
    lod1_objects = build_asset_lod(lod1_collection, materials, 1)
    lod2_objects = build_asset_lod(lod2_collection, materials, 2)
    lod3_objects = build_asset_lod(lod3_collection, materials, 3)
    collision = add_collision_proxy(collision_collection, materials["stone"])
    add_metadata_to_objects(lod0_objects + lod1_objects + lod2_objects + lod3_objects + [collision])

    export_dir = EXPORT_ROOT / REL_PATH
    export_objects(lod0_objects, export_dir / f"{ASSET_NAME}.fbx")
    export_objects(lod0_objects, export_dir / f"{ASSET_NAME}_LOD0.fbx")
    export_objects(lod1_objects, export_dir / f"{ASSET_NAME}_LOD1.fbx")
    export_objects(lod2_objects, export_dir / f"{ASSET_NAME}_LOD2.fbx")
    export_objects(lod3_objects, export_dir / f"{ASSET_NAME}_LOD3.fbx")
    export_objects([collision], export_dir / f"{ASSET_NAME}_UCX.fbx")

    camera, target = configure_review_scene()
    render_paths = [
        REVIEW_ROOT / f"{ASSET_NAME}_FrontReview.png",
        REVIEW_ROOT / f"{ASSET_NAME}_RightReview.png",
        REVIEW_ROOT / f"{ASSET_NAME}_BackReview.png",
        REVIEW_ROOT / f"{ASSET_NAME}_LeftReview.png",
        REVIEW_ROOT / f"{ASSET_NAME}_HeroReview.png",
    ]
    view_locations = [
        (0, -545, 178),
        (545, -8, 205),
        (60, 545, 212),
        (-545, -8, 205),
        (340, -455, 238),
    ]
    for path, location in zip(render_paths, view_locations):
        render_view(camera, target, location, path, (960, 540))
    compose_review_board(render_paths, REVIEW_ROOT / f"{ASSET_NAME}_DCCProofTurntable.png", 960, 540)

    blend_path = BLENDER_ROOT / REL_PATH / f"{ASSET_NAME}.blend"
    ensure_dir(blend_path.parent)
    bpy.ops.wm.save_as_mainfile(filepath=str(blend_path))

    print(
        "Built {}: LOD0 {} tris, LOD1 {} tris, LOD2 {} tris, LOD3 {} tris. Exports: {}".format(
            ASSET_NAME,
            object_triangles(lod0_objects),
            object_triangles(lod1_objects),
            object_triangles(lod2_objects),
            object_triangles(lod3_objects),
            export_dir,
        )
    )


if __name__ == "__main__":
    main()
