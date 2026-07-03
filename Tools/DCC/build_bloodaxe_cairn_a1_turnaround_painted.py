#!/usr/bin/env python3
"""Build the A1 Blood Axe cairn turnaround-painted DCC candidate.

Run with:
    Tools/Blender/blender-4.5.11-linux-x64/blender --background --python Tools/DCC/build_bloodaxe_cairn_a1_turnaround_painted.py

This pass is the first strict multi-angle repair after the rejected/provisional
branches. It uses the approved A1 crop plus the A1 multi-angle turnaround guide
as the visual source and keeps the result as a review candidate, not canon.
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
REVIEW_ROOT = ROOT / "Saved" / "Automation" / "DCC" / "SM_GIA_BloodAxeCairnSlabCluster_A01_TurnaroundPainted"

ASSET_NAME = "SM_GIA_BloodAxeCairnSlabCluster_A01_TurnaroundPainted"
REL_PATH = f"Props/Giants/BloodAxe/Cairns/{ASSET_NAME}"
UNREAL_PATH = f"/Game/Aerathea/Props/Giants/BloodAxe/Cairns/{ASSET_NAME}"

SOURCE_CROP = ROOT / "docs/assets/visual_canon/VC_GIA_BloodAxe_CairnStones_A01_A1_Crop.png"
TURNAROUND = ROOT / "docs/assets/visual_canon/VC_GIA_BloodAxe_CairnStones_A01_A1_TurnaroundDraft_A01.png"

sys.path.insert(0, str(ROOT))
from Tools.DCC.build_next_slice_assets import add_asset_metadata, clear_scene, setup_scene  # noqa: E402


RNG = random.Random(812703)


def ensure_dir(path: Path) -> None:
    path.mkdir(parents=True, exist_ok=True)


def noise(x: int, y: int, seed: int) -> float:
    value = (x * 374761393 + y * 668265263 + seed * 362437) & 0xFFFFFFFF
    value = ((value ^ (value >> 13)) * 1274126177) & 0xFFFFFFFF
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


def texture_set(label: str, base: tuple[float, float, float], warm: tuple[float, float, float], seed: int) -> dict[str, Path]:
    texture_dir = TEXTURE_ROOT / REL_PATH
    width = 1024
    height = 1024
    bc = array("f")
    normal = array("f")
    orm = array("f")
    for y in range(height):
        for x in range(width):
            fine = noise(x, y, seed)
            broad = noise(x // 17, y // 19, seed + 31)
            vein = noise(x // 43, y // 29, seed + 71)
            chip = noise(x // 11, y // 13, seed + 113)
            warmth = 0.18 * broad + 0.12 * fine + (0.16 if vein > 0.91 else 0.0)
            color = (
                base[0] * (1.0 - warmth) + warm[0] * warmth,
                base[1] * (1.0 - warmth) + warm[1] * warmth,
                base[2] * (1.0 - warmth) + warm[2] * warmth,
            )
            if chip > 0.985:
                color = (color[0] + 0.11, color[1] + 0.10, color[2] + 0.08)
            bc.extend((clamp(color[0]), clamp(color[1]), clamp(color[2]), 1.0))

            bump_x = (fine - 0.5) * 0.20
            bump_y = (noise(y, x, seed + 151) - 0.5) * 0.14
            normal.extend((clamp(0.5 + bump_x), clamp(0.5 + bump_y), 1.0, 1.0))
            occlusion = 0.55 + (1.0 - broad) * 0.30
            roughness = 0.83 + fine * 0.13
            orm.extend((clamp(occlusion), clamp(roughness), 0.0, 1.0))

    paths = {
        "bc": texture_dir / f"T_GIA_BloodAxeCairnSlabCluster_A01_TurnaroundPainted_{label}_BC.png",
        "n": texture_dir / f"T_GIA_BloodAxeCairnSlabCluster_A01_TurnaroundPainted_{label}_N.png",
        "orm": texture_dir / f"T_GIA_BloodAxeCairnSlabCluster_A01_TurnaroundPainted_{label}_ORM.png",
    }
    save_texture(paths["bc"], width, height, bc)
    save_texture(paths["n"], width, height, normal)
    save_texture(paths["orm"], width, height, orm)
    return paths


def generate_textures() -> dict[str, dict[str, Path]]:
    return {
        "stone": texture_set("DarkHighlandStone", (0.335, 0.315, 0.265), (0.74, 0.69, 0.54), 1001),
        "earth": texture_set("AshMud", (0.245, 0.150, 0.085), (0.62, 0.43, 0.24), 2003),
        "rawhide": texture_set("Rawhide", (0.54, 0.315, 0.115), (0.96, 0.69, 0.30), 3007),
        "paint": texture_set("OxideRedPaint", (0.56, 0.050, 0.035), (0.98, 0.20, 0.080), 4009),
    }


def make_material(
    name: str,
    color: tuple[float, float, float],
    textures: dict[str, Path] | None = None,
    roughness: float = 0.88,
    review_emission: float = 0.14,
) -> bpy.types.Material:
    material = bpy.data.materials.new(name)
    material.diffuse_color = (color[0], color[1], color[2], 1.0)
    material.use_nodes = True
    nodes = material.node_tree.nodes
    bsdf = nodes.get("Principled BSDF")
    if bsdf is not None:
        bsdf.inputs["Base Color"].default_value = (color[0], color[1], color[2], 1.0)
        bsdf.inputs["Roughness"].default_value = roughness
        bsdf.inputs["Metallic"].default_value = 0.0
        if "Emission Color" in bsdf.inputs:
            bsdf.inputs["Emission Color"].default_value = (color[0] * 0.62, color[1] * 0.62, color[2] * 0.62, 1.0)
        if "Emission Strength" in bsdf.inputs:
            bsdf.inputs["Emission Strength"].default_value = review_emission
        if textures is not None:
            base = nodes.new(type="ShaderNodeTexImage")
            base.image = bpy.data.images.load(str(textures["bc"]))
            material.node_tree.links.new(base.outputs["Color"], bsdf.inputs["Base Color"])
            ntex = nodes.new(type="ShaderNodeTexImage")
            ntex.image = bpy.data.images.load(str(textures["n"]))
            ntex.image.colorspace_settings.name = "Non-Color"
            normal = nodes.new(type="ShaderNodeNormalMap")
            normal.inputs["Strength"].default_value = 0.32
            material.node_tree.links.new(ntex.outputs["Color"], normal.inputs["Color"])
            material.node_tree.links.new(normal.outputs["Normal"], bsdf.inputs["Normal"])
    return material


def make_materials(paths: dict[str, dict[str, Path]]) -> dict[str, bpy.types.Material]:
    return {
        "stone": make_material("M_GIA_BloodAxeCairn_TurnaroundPainted_DarkStone_A01", (0.46, 0.435, 0.36), paths["stone"], 0.92),
        "stone_light": make_material("M_GIA_BloodAxeCairn_TurnaroundPainted_StoneEdgeWarm_A01", (0.82, 0.76, 0.59), None, 0.88),
        "stone_dark": make_material("M_GIA_BloodAxeCairn_TurnaroundPainted_DeepCrack_A01", (0.060, 0.055, 0.048), None, 0.96),
        "earth": make_material("M_GIA_BloodAxeCairn_TurnaroundPainted_AshMud_A01", (0.39, 0.25, 0.14), paths["earth"], 0.96),
        "rawhide": make_material("M_GIA_BloodAxeCairn_TurnaroundPainted_Rawhide_A01", (0.78, 0.49, 0.20), paths["rawhide"], 0.82),
        "paint": make_material("M_GIA_BloodAxeCairn_TurnaroundPainted_OxideRed_A01", (0.74, 0.065, 0.045), paths["paint"], 0.88),
        "collision": make_material("M_AET_CollisionProxy_ReviewOnly_A01", (0.0, 0.30, 0.85), None, 0.5),
    }


def collection(name: str, hidden: bool = False) -> bpy.types.Collection:
    col = bpy.data.collections.new(name)
    bpy.context.scene.collection.children.link(col)
    col.hide_viewport = hidden
    col.hide_render = hidden
    return col


def move_to(obj: bpy.types.Object, col: bpy.types.Collection) -> None:
    for current in list(obj.users_collection):
        current.objects.unlink(obj)
    col.objects.link(obj)


def activate(obj: bpy.types.Object) -> None:
    bpy.ops.object.select_all(action="DESELECT")
    bpy.context.view_layer.objects.active = obj
    obj.select_set(True)


def apply_modifiers(obj: bpy.types.Object) -> None:
    activate(obj)
    for mod in list(obj.modifiers):
        bpy.ops.object.modifier_apply(modifier=mod.name)


def roughen(obj: bpy.types.Object, amount: float, seed: int) -> None:
    for idx, vert in enumerate(obj.data.vertices):
        vert.co.x += (noise(idx, seed, seed + 11) - 0.5) * amount
        vert.co.y += (noise(seed, idx, seed + 17) - 0.5) * amount
        vert.co.z += (noise(idx + 3, seed + 5, seed + 23) - 0.5) * amount * 0.72


def add_prism(
    name: str,
    col: bpy.types.Collection,
    material: bpy.types.Material,
    footprint: list[tuple[float, float]],
    height: float,
    location: tuple[float, float, float],
    rotation: tuple[float, float, float],
    seed: int,
    top_scale: float = 0.86,
    bevel: float = 1.2,
    rough: float = 3.0,
) -> bpy.types.Object:
    verts = []
    for x, y in footprint:
        verts.append((x, y, -height / 2.0))
    for x, y in footprint:
        n = 0.93 + noise(int(x * 4), int(y * 4), seed) * 0.14
        verts.append((x * top_scale * n, y * top_scale * n, height / 2.0))
    count = len(footprint)
    faces: list[tuple[int, ...]] = [tuple(reversed(range(count))), tuple(range(count, count * 2))]
    for idx in range(count):
        nxt = (idx + 1) % count
        faces.append((idx, nxt, count + nxt, count + idx))
    mesh = bpy.data.meshes.new(f"{name}_Mesh")
    mesh.from_pydata(verts, [], faces)
    mesh.update()
    obj = bpy.data.objects.new(name, mesh)
    obj.location = location
    obj.rotation_euler = rotation
    obj.data.materials.append(material)
    col.objects.link(obj)
    if bevel > 0:
        mod = obj.modifiers.new("AET_readable_chipped_bevel", "BEVEL")
        mod.width = bevel
        mod.segments = 1
    normal = obj.modifiers.new("AET_weighted_normals", "WEIGHTED_NORMAL")
    apply_modifiers(obj)
    roughen(obj, rough, seed)
    bpy.ops.object.shade_flat()
    return obj


def add_profile_slab(
    name: str,
    col: bpy.types.Collection,
    material: bpy.types.Material,
    profile: list[tuple[float, float]],
    depth: float,
    location: tuple[float, float, float],
    rotation: tuple[float, float, float],
    seed: int,
    bevel: float = 1.4,
) -> bpy.types.Object:
    verts = [(x, -depth / 2.0, z) for x, z in profile] + [(x, depth / 2.0, z) for x, z in profile]
    count = len(profile)
    faces: list[tuple[int, ...]] = [tuple(range(count)), tuple(reversed(range(count, count * 2)))]
    for idx in range(count):
        nxt = (idx + 1) % count
        faces.append((idx, nxt, count + nxt, count + idx))
    mesh = bpy.data.meshes.new(f"{name}_Mesh")
    mesh.from_pydata(verts, [], faces)
    mesh.update()
    obj = bpy.data.objects.new(name, mesh)
    obj.location = location
    obj.rotation_euler = rotation
    obj.data.materials.append(material)
    obj["aet_profile_min_x_cm"] = min(x for x, _ in profile)
    obj["aet_profile_max_x_cm"] = max(x for x, _ in profile)
    obj["aet_profile_min_z_cm"] = min(z for _, z in profile)
    obj["aet_profile_max_z_cm"] = max(z for _, z in profile)
    obj["aet_local_depth_cm"] = depth
    col.objects.link(obj)
    mod = obj.modifiers.new("AET_broken_profile_bevel", "BEVEL")
    mod.width = bevel
    mod.segments = 1
    normal = obj.modifiers.new("AET_weighted_normals", "WEIGHTED_NORMAL")
    apply_modifiers(obj)
    roughen(obj, 2.6, seed)
    bpy.ops.object.shade_flat()
    return obj


def add_curve_between(name: str, col: bpy.types.Collection, material: bpy.types.Material, start: Vector, end: Vector, radius: float) -> bpy.types.Object:
    curve = bpy.data.curves.new(name, "CURVE")
    curve.dimensions = "3D"
    curve.resolution_u = 2
    curve.bevel_depth = radius
    curve.bevel_resolution = 2
    spl = curve.splines.new("POLY")
    spl.points.add(1)
    spl.points[0].co = (start.x, start.y, start.z, 1.0)
    spl.points[1].co = (end.x, end.y, end.z, 1.0)
    obj = bpy.data.objects.new(name, curve)
    obj.data.materials.append(material)
    col.objects.link(obj)
    activate(obj)
    bpy.ops.object.convert(target="MESH")
    converted = bpy.context.object
    converted.name = name
    move_to(converted, col)
    return converted


def world(obj: bpy.types.Object, local: tuple[float, float, float]) -> Vector:
    return obj.matrix_world @ Vector(local)


def add_top_mark(
    slab: bpy.types.Object,
    name: str,
    col: bpy.types.Collection,
    material: bpy.types.Material,
    local_xy: tuple[float, float],
    size_xy: tuple[float, float],
    yaw: float,
    z_offset: float,
) -> bpy.types.Object:
    sx = size_xy[0] * 0.5
    sy = size_xy[1] * 0.5
    cx, cy = local_xy
    c = math.cos(yaw)
    s = math.sin(yaw)
    corners = [(-sx, -sy), (sx, -sy), (sx, sy), (-sx, sy)]
    verts = []
    for x, y in corners:
        rx = cx + x * c - y * s
        ry = cy + x * s + y * c
        verts.append((rx, ry, z_offset))
    mesh = bpy.data.meshes.new(f"{name}_Mesh")
    mesh.from_pydata(verts, [], [(0, 1, 2, 3)])
    mesh.update()
    obj = bpy.data.objects.new(name, mesh)
    obj.location = slab.location
    obj.rotation_euler = slab.rotation_euler
    obj.data.materials.append(material)
    col.objects.link(obj)
    return obj


def add_face_mark(
    slab: bpy.types.Object,
    name: str,
    col: bpy.types.Collection,
    material: bpy.types.Material,
    local_xz: tuple[float, float],
    size_xz: tuple[float, float],
    yaw: float,
    y_offset: float,
) -> bpy.types.Object:
    sx = size_xz[0] * 0.5
    sz = size_xz[1] * 0.5
    cx, cz = local_xz
    c = math.cos(yaw)
    s = math.sin(yaw)
    verts = []
    for x, z in [(-sx, -sz), (sx, -sz), (sx, sz), (-sx, sz)]:
        rx = cx + x * c - z * s
        rz = cz + x * s + z * c
        verts.append((rx, y_offset, rz))
    mesh = bpy.data.meshes.new(f"{name}_Mesh")
    mesh.from_pydata(verts, [], [(0, 1, 2, 3)])
    mesh.update()
    obj = bpy.data.objects.new(name, mesh)
    obj.location = slab.location
    obj.rotation_euler = slab.rotation_euler
    obj.data.materials.append(material)
    col.objects.link(obj)
    return obj


def add_lashing_band(slab: bpy.types.Object, prefix: str, col: bpy.types.Collection, material: bpy.types.Material, local_x: float, width: float, height: float) -> list[bpy.types.Object]:
    objects = []
    z = height * 0.5 + 3.0
    for offset in (-5.4, -1.8, 1.8, 5.4):
        objects.append(add_curve_between(f"{prefix}_cord_{offset:+.1f}", col, material, world(slab, (local_x + offset, -width * 0.50, z)), world(slab, (local_x + offset, width * 0.50, z)), 1.15))
    for y in (-width * 0.50, width * 0.50):
        objects.append(add_curve_between(f"{prefix}_cross_{y:+.0f}", col, material, world(slab, (local_x - 7.5, y, z + 1.2)), world(slab, (local_x + 7.5, y, z - 1.2)), 0.9))
    return objects


def add_earth_base(col: bpy.types.Collection, material: bpy.types.Material, detail: int) -> bpy.types.Object:
    segments = {0: 72, 1: 44, 2: 28, 3: 18}[detail]
    footprint = []
    for idx in range(segments):
        angle = math.tau * idx / segments
        n = 0.82 + noise(idx, 0, 5101 + detail) * 0.28
        footprint.append((math.cos(angle) * 178.0 * n, math.sin(angle) * 104.0 * n))
    obj = add_prism(
        f"A1_TurnaroundPainted_AshMudBase_LOD{detail}",
        col,
        material,
        footprint,
        8.0,
        (0.0, -4.0, 4.0),
        (0.0, 0.0, 0.0),
        5101 + detail,
        top_scale=0.94,
        bevel=0.2,
        rough=1.2,
    )
    return obj


def add_pebbles(col: bpy.types.Collection, material: bpy.types.Material, detail: int) -> list[bpy.types.Object]:
    count = {0: 70, 1: 30, 2: 10, 3: 0}[detail]
    objects = []
    for idx in range(count):
        angle = RNG.random() * math.tau
        radius = 48.0 + RNG.random() * 150.0
        x = math.cos(angle) * radius * 1.05
        y = math.sin(angle) * radius * 0.66 - 5.0
        if -105.0 < x < 105.0 and -58.0 < y < 52.0 and RNG.random() < 0.74:
            continue
        sx = RNG.uniform(7.0, 22.0)
        sy = RNG.uniform(5.0, 16.0)
        h = RNG.uniform(3.0, 11.0)
        footprint = [(-sx, -sy), (sx * 0.75, -sy * 1.05), (sx, sy * 0.6), (-sx * 0.9, sy)]
        objects.append(
            add_prism(
                f"A1_TurnaroundPainted_RubbleStone_{idx:02d}_LOD{detail}",
                col,
                material,
                footprint,
                h,
                (x, y, h * 0.5 + 6.0),
                (RNG.uniform(-0.12, 0.12), RNG.uniform(-0.10, 0.10), RNG.uniform(0.0, math.tau)),
                6200 + idx + detail * 100,
                top_scale=0.72,
                bevel=0.45,
                rough=0.8,
            )
        )
    return objects


def build_lod(col: bpy.types.Collection, mats: dict[str, bpy.types.Material], detail: int) -> list[bpy.types.Object]:
    objects: list[bpy.types.Object] = [add_earth_base(col, mats["earth"], detail)]
    include_minor = detail <= 1
    include_detail = detail == 0
    include_paint = detail <= 2
    include_lash = detail <= 1

    central = add_prism(
        f"A1_TurnaroundPainted_MainFallenPaintedSlab_LOD{detail}",
        col,
        mats["stone"],
        [(-126, -40), (-103, -53), (-55, -47), (-4, -54), (49, -42), (119, -31), (130, 2), (101, 31), (43, 38), (-12, 35), (-63, 44), (-111, 29), (-133, 3)],
        22.0,
        (-3.0, -16.0, 45.0),
        (math.radians(1.5), math.radians(-18.0), math.radians(-8.0)),
        7010 + detail,
        top_scale=0.82,
        bevel=1.1,
        rough=2.8,
    )
    objects.append(central)

    rear = add_profile_slab(
        f"A1_TurnaroundPainted_RearTallBrokenSlab_LOD{detail}",
        col,
        mats["stone"],
        [(-34, -58), (25, -57), (34, 8), (26, 42), (4, 67), (-17, 57), (-30, 19), (-37, -14)],
        28.0,
        (20.0, 39.0, 68.0),
        (math.radians(-12.0), math.radians(9.0), math.radians(10.0)),
        7110 + detail,
        bevel=1.25,
    )
    objects.append(rear)

    right = add_profile_slab(
        f"A1_TurnaroundPainted_RightBoundUpright_LOD{detail}",
        col,
        mats["stone"],
        [(-30, -39), (25, -39), (31, 15), (12, 50), (-16, 43), (-30, -8)],
        34.0,
        (116.0, 10.0, 51.0),
        (math.radians(1.0), math.radians(-7.0), math.radians(-10.0)),
        7210 + detail,
        bevel=1.1,
    )
    objects.append(right)

    left_base = add_prism(
        f"A1_TurnaroundPainted_LeftFrontStackBase_LOD{detail}",
        col,
        mats["stone"],
        [(-65, -20), (-26, -28), (30, -22), (67, -9), (59, 15), (28, 27), (-28, 20), (-70, 8)],
        23.0,
        (-100.0, -36.0, 24.0),
        (math.radians(1.5), math.radians(2.0), math.radians(-12.0)),
        7310 + detail,
        top_scale=0.78,
        bevel=0.8,
        rough=1.8,
    )
    objects.append(left_base)

    left_cap = None
    if detail <= 2:
        left_cap = add_prism(
            f"A1_TurnaroundPainted_LeftFrontStackCap_LOD{detail}",
            col,
            mats["stone"],
            [(-45, -15), (-18, -21), (45, -12), (48, 7), (25, 20), (-33, 17), (-48, 0)],
            18.0,
            (-101.0, -47.0, 43.0),
            (math.radians(-2.0), math.radians(2.0), math.radians(-8.0)),
            7410 + detail,
            top_scale=0.80,
            bevel=0.7,
            rough=1.5,
        )
        objects.append(left_cap)

    if include_minor:
        objects.extend(
            [
                add_profile_slab(
                    f"A1_TurnaroundPainted_LeftRearShard_LOD{detail}",
                    col,
                    mats["stone"],
                    [(-16, -35), (17, -35), (20, 22), (4, 45), (-17, 19)],
                    20.0,
                    (-48.0, 31.0, 55.0),
                    (math.radians(-7.0), math.radians(12.0), math.radians(10.0)),
                    7510 + detail,
                    bevel=1.0,
                ),
                add_profile_slab(
                    f"A1_TurnaroundPainted_CenterNarrowShard_LOD{detail}",
                    col,
                    mats["stone"],
                    [(-11, -39), (13, -39), (16, 30), (3, 52), (-12, 26)],
                    15.0,
                    (-14.0, 22.0, 58.0),
                    (math.radians(-9.0), math.radians(-5.0), math.radians(-4.0)),
                    7610 + detail,
                    bevel=0.9,
                ),
                add_prism(
                    f"A1_TurnaroundPainted_RightSupportStone_LOD{detail}",
                    col,
                    mats["stone"],
                    [(-33, -14), (-8, -18), (33, -10), (31, 12), (8, 18), (-31, 10)],
                    38.0,
                    (120.0, -29.0, 24.0),
                    (math.radians(1.0), math.radians(-4.0), math.radians(8.0)),
                    7710 + detail,
                    top_scale=0.76,
                    bevel=0.7,
                    rough=1.2,
                ),
                add_prism(
                    f"A1_TurnaroundPainted_BackRootCounterStone_LOD{detail}",
                    col,
                    mats["stone"],
                    [(-42, -17), (-12, -24), (40, -15), (44, 9), (12, 23), (-38, 15)],
                    28.0,
                    (4.0, 58.0, 19.0),
                    (math.radians(0.0), math.radians(4.0), math.radians(13.0)),
                    7810 + detail,
                    top_scale=0.77,
                    bevel=0.7,
                    rough=1.2,
                ),
            ]
        )

    if include_paint:
        objects.extend(
            [
                add_top_mark(central, f"A1_TurnaroundPainted_MainRedLongStroke_LOD{detail}", col, mats["paint"], (-9.0, -2.0), (155.0, 13.0), math.radians(18.0), 15.1),
                add_top_mark(central, f"A1_TurnaroundPainted_MainRedCrossStrokeA_LOD{detail}", col, mats["paint"], (-47.0, 14.0), (84.0, 11.0), math.radians(-31.0), 15.3),
                add_top_mark(central, f"A1_TurnaroundPainted_MainRedCrossStrokeB_LOD{detail}", col, mats["paint"], (38.0, 6.0), (74.0, 10.0), math.radians(-24.0), 15.5),
                add_face_mark(rear, f"A1_TurnaroundPainted_RearRedSlash_LOD{detail}", col, mats["paint"], (0.0, 12.0), (15.0, 60.0), math.radians(-13.0), -14.6),
                add_face_mark(right, f"A1_TurnaroundPainted_RightSmallRedScuff_LOD{detail}", col, mats["paint"], (8.0, 6.0), (9.0, 45.0), math.radians(3.0), -17.4),
            ]
        )

    if include_detail:
        detail_rng = random.Random(9101)
        for idx in range(20):
            objects.append(add_top_mark(central, f"A1_TurnaroundPainted_MainWarmChip_{idx:02d}", col, mats["stone_light"], (detail_rng.uniform(-105, 104), detail_rng.uniform(-35, 32)), (detail_rng.uniform(9, 30), detail_rng.uniform(1.2, 2.5)), detail_rng.uniform(-0.9, 0.9), 15.7))
        for idx in range(16):
            objects.append(add_top_mark(central, f"A1_TurnaroundPainted_MainDarkCrack_{idx:02d}", col, mats["stone_dark"], (detail_rng.uniform(-105, 104), detail_rng.uniform(-35, 32)), (detail_rng.uniform(14, 40), detail_rng.uniform(1.0, 2.1)), detail_rng.uniform(-0.9, 0.9), 15.8))
        for idx in range(14):
            objects.append(add_face_mark(rear, f"A1_TurnaroundPainted_RearWarmChip_{idx:02d}", col, mats["stone_light"], (detail_rng.uniform(-24, 24), detail_rng.uniform(-34, 54)), (detail_rng.uniform(1.4, 3.2), detail_rng.uniform(10, 24)), detail_rng.uniform(-0.28, 0.28), -14.4))
        for idx in range(10):
            objects.append(add_face_mark(right, f"A1_TurnaroundPainted_RightWarmChip_{idx:02d}", col, mats["stone_light"], (detail_rng.uniform(-20, 20), detail_rng.uniform(-28, 45)), (detail_rng.uniform(1.3, 3.0), detail_rng.uniform(10, 26)), detail_rng.uniform(-0.25, 0.25), -18.0))

    if include_lash:
        objects.extend(add_lashing_band(central, f"A1_TurnaroundPainted_LeftRawhideBind_LOD{detail}", col, mats["rawhide"], -72.0, 74.0, 28.0))
        objects.extend(add_lashing_band(central, f"A1_TurnaroundPainted_RightRawhideBind_LOD{detail}", col, mats["rawhide"], 72.0, 74.0, 28.0))
        objects.append(add_curve_between(f"A1_TurnaroundPainted_RightUprightFrontCord_LOD{detail}", col, mats["rawhide"], world(right, (-29.0, -18.0, 8.0)), world(right, (31.0, -18.0, 9.0)), 2.5))
        objects.append(add_curve_between(f"A1_TurnaroundPainted_RightUprightBackCord_LOD{detail}", col, mats["rawhide"], world(right, (-27.0, 18.0, 9.0)), world(right, (29.0, 18.0, 8.0)), 2.1))

    objects.extend(add_pebbles(col, mats["stone"], detail))
    return [obj for obj in objects if getattr(obj, "type", None) == "MESH"]


def add_collision(col: bpy.types.Collection, material: bpy.types.Material) -> bpy.types.Object:
    bpy.ops.mesh.primitive_cube_add(size=1.0, location=(0.0, -4.0, 70.0))
    obj = bpy.context.object
    obj.name = f"UCX_{ASSET_NAME}_00"
    obj.dimensions = (390.0, 250.0, 170.0)
    obj.data.materials.append(material)
    activate(obj)
    bpy.ops.object.transform_apply(location=False, rotation=False, scale=True)
    obj.display_type = "WIRE"
    obj.hide_render = True
    move_to(obj, col)
    return obj


def smart_uv(objects: list[bpy.types.Object]) -> None:
    bpy.ops.object.select_all(action="DESELECT")
    for obj in objects:
        obj.select_set(True)
    if objects:
        bpy.context.view_layer.objects.active = objects[0]
        bpy.ops.object.mode_set(mode="EDIT")
        bpy.ops.mesh.select_all(action="SELECT")
        bpy.ops.uv.smart_project(angle_limit=math.radians(66.0), island_margin=0.03)
        bpy.ops.object.mode_set(mode="OBJECT")


def tri_count(obj: bpy.types.Object) -> int:
    obj.data.calc_loop_triangles()
    return len(obj.data.loop_triangles)


def col_tri_count(col: bpy.types.Collection) -> int:
    return sum(tri_count(obj) for obj in col.objects if getattr(obj, "type", None) == "MESH")


def col_bounds(col: bpy.types.Collection) -> tuple[float, float, float]:
    pts: list[Vector] = []
    for obj in col.objects:
        if getattr(obj, "type", None) != "MESH":
            continue
        pts.extend(obj.matrix_world @ Vector(corner) for corner in obj.bound_box)
    return (
        max(p.x for p in pts) - min(p.x for p in pts),
        max(p.y for p in pts) - min(p.y for p in pts),
        max(p.z for p in pts) - min(p.z for p in pts),
    )


def export_fbx(path: Path, objects: list[bpy.types.Object]) -> None:
    ensure_dir(path.parent)
    bpy.ops.object.select_all(action="DESELECT")
    for obj in objects:
        obj.select_set(True)
        obj.hide_set(False)
        obj.hide_viewport = False
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


def setup_lighting() -> None:
    scene = bpy.context.scene
    try:
        scene.render.engine = "BLENDER_EEVEE_NEXT"
    except TypeError:
        scene.render.engine = "BLENDER_EEVEE"
    scene.view_settings.view_transform = "Standard"
    scene.view_settings.exposure = 0.85
    scene.view_settings.gamma = 1.0
    if scene.world:
        scene.world.color = (0.78, 0.76, 0.70)
    for name, kind, loc, energy, size in [
        ("AET_KeyLight", "AREA", (-310, -420, 420), 125000, 500),
        ("AET_FillLight", "AREA", (310, -160, 260), 76000, 620),
        ("AET_BackRim", "POINT", (0, 310, 260), 24000, 0),
        ("AET_TopSoft", "AREA", (0, 0, 560), 72000, 740),
    ]:
        data = bpy.data.lights.new(name, kind)
        data.energy = energy
        if kind == "AREA":
            data.size = size
        obj = bpy.data.objects.new(name, data)
        obj.location = loc
        bpy.context.scene.collection.objects.link(obj)


def set_camera(name: str, loc: tuple[float, float, float], target: tuple[float, float, float], scale: float) -> None:
    bpy.ops.object.camera_add(location=loc)
    cam = bpy.context.object
    cam.name = name
    direction = Vector(target) - Vector(loc)
    cam.rotation_euler = direction.to_track_quat("-Z", "Y").to_euler()
    cam.data.type = "ORTHO"
    cam.data.ortho_scale = scale
    cam.data.clip_start = 1
    cam.data.clip_end = 5000
    bpy.context.scene.camera = cam


def render_reviews() -> None:
    ensure_dir(REVIEW_ROOT)
    scene = bpy.context.scene
    scene.render.resolution_x = 1800
    scene.render.resolution_y = 1150
    scene.eevee.taa_render_samples = 64
    reviews = [
        ("Front", (340, -590, 330), (0, -5, 52), 382),
        ("Right", (610, 0, 285), (0, -2, 55), 382),
        ("Back", (-350, 600, 285), (0, 0, 55), 382),
        ("Left", (-610, 0, 285), (0, -2, 55), 382),
        ("Top", (0, 0, 770), (0, 0, 0), 392),
        ("Beauty", (370, -555, 335), (0, -5, 56), 398),
    ]
    for label, loc, target, scale in reviews:
        set_camera(f"AET_{label}ReviewCamera", loc, target, scale)
        scene.render.filepath = str(REVIEW_ROOT / f"{ASSET_NAME}_{label}Review.png")
        bpy.ops.render.render(write_still=True)


def build() -> None:
    clear_scene()
    setup_scene()
    setup_lighting()
    paths = generate_textures()
    mats = make_materials(paths)

    lod_cols = [collection(f"{ASSET_NAME}_LOD{i}") for i in range(4)]
    for col in lod_cols[1:]:
        col.hide_viewport = True
        col.hide_render = True
    collision_col = collection(f"{ASSET_NAME}_Collision_Source", hidden=True)

    lod_objects = [build_lod(lod_cols[i], mats, i) for i in range(4)]
    for objs in lod_objects:
        smart_uv(objs)
    collision = add_collision(collision_col, mats["collision"])

    add_asset_metadata(
        ASSET_NAME,
        "A1 Blood Axe cairn turnaround-painted DCC candidate using approved crop and multi-angle turnaround guide. Review candidate only until Flamestrike approves visual match in DCC and Unreal.",
        UNREAL_PATH,
    )

    render_reviews()

    blend_path = BLENDER_ROOT / REL_PATH / f"{ASSET_NAME}.blend"
    export_path = EXPORT_ROOT / REL_PATH / f"{ASSET_NAME}.fbx"
    ensure_dir(blend_path.parent)
    ensure_dir(export_path.parent)
    bpy.ops.wm.save_as_mainfile(filepath=str(blend_path))

    export_fbx(export_path, lod_objects[0] + [collision])
    for idx, objs in enumerate(lod_objects):
        export_fbx(export_path.with_name(f"{ASSET_NAME}_LOD{idx}.fbx"), objs)
    export_fbx(export_path.with_name(f"{ASSET_NAME}_UCX.fbx"), [collision])

    bounds = col_bounds(lod_cols[0])
    print(f"Built {blend_path.relative_to(ROOT)}")
    print(f"Exported {export_path.relative_to(ROOT)}")
    print(f"Source crop {SOURCE_CROP.relative_to(ROOT)}")
    print(f"Turnaround guide {TURNAROUND.relative_to(ROOT)}")
    for idx, col in enumerate(lod_cols):
        print(f"LOD{idx} tris: {col_tri_count(col)}")
    print(f"LOD0 bounds: {bounds[0]:.2f}w x {bounds[1]:.2f}d x {bounds[2]:.2f}h cm")
    print("Collision proxies: 1")


if __name__ == "__main__":
    build()
