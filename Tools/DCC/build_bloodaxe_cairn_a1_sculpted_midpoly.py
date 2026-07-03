#!/usr/bin/env python3
"""Build A1 Blood Axe cairn as a sculpted mid-poly DCC candidate.

Run with:
    Tools/Blender/blender-4.5.11-linux-x64/blender --background --python Tools/DCC/build_bloodaxe_cairn_a1_sculpted_midpoly.py

This branch is the true-geometry follow-up after projection and blockout
failures. It uses authored slabs, rubble, rawhide cords, red paint decals, and
crack/highlight decals to match the approved A1 turnaround without relying on
image cards as the visible asset surface.
"""

from __future__ import annotations

import math
import random
import sys
from pathlib import Path

import bpy
from mathutils import Vector


ROOT = Path(__file__).resolve().parents[2]
SOURCE_ROOT = ROOT / "SourceAssets"
BLENDER_ROOT = SOURCE_ROOT / "Blender"
EXPORT_ROOT = SOURCE_ROOT / "Exports"
REVIEW_ROOT = ROOT / "Saved" / "Automation" / "DCC" / "SM_GIA_BloodAxeCairnSlabCluster_A01_SculptedMidpoly"

ASSET_NAME = "SM_GIA_BloodAxeCairnSlabCluster_A01_SculptedMidpoly"
REL_PATH = f"Props/Giants/BloodAxe/Cairns/{ASSET_NAME}"
UNREAL_PATH = f"/Game/Aerathea/Props/Giants/BloodAxe/Cairns/{ASSET_NAME}"

sys.path.insert(0, str(ROOT))
from Tools.DCC.build_next_slice_assets import add_asset_metadata, clear_scene, setup_scene  # noqa: E402


RNG = random.Random(88017)


def ensure_dir(path: Path) -> None:
    path.mkdir(parents=True, exist_ok=True)


def make_material(name: str, color: tuple[float, float, float], roughness: float = 0.9, emission: float = 0.10) -> bpy.types.Material:
    material = bpy.data.materials.new(name)
    material.diffuse_color = (color[0], color[1], color[2], 1.0)
    material.use_nodes = True
    bsdf = material.node_tree.nodes.get("Principled BSDF")
    if bsdf is not None:
        bsdf.inputs["Base Color"].default_value = (color[0], color[1], color[2], 1.0)
        bsdf.inputs["Roughness"].default_value = roughness
        bsdf.inputs["Metallic"].default_value = 0.0
        if "Emission Color" in bsdf.inputs:
            bsdf.inputs["Emission Color"].default_value = (color[0] * 0.45, color[1] * 0.45, color[2] * 0.45, 1.0)
        if "Emission Strength" in bsdf.inputs:
            bsdf.inputs["Emission Strength"].default_value = emission
    return material


def make_materials() -> dict[str, bpy.types.Material]:
    return {
        "stone": make_material("M_GIA_BloodAxeCairn_Sculpted_Stone_A01", (0.43, 0.405, 0.335), 0.92, 0.12),
        "stone_dark": make_material("M_GIA_BloodAxeCairn_Sculpted_DarkStone_A01", (0.22, 0.205, 0.175), 0.94, 0.08),
        "stone_light": make_material("M_GIA_BloodAxeCairn_Sculpted_WarmChip_A01", (0.78, 0.72, 0.55), 0.88, 0.18),
        "crack": make_material("M_GIA_BloodAxeCairn_Sculpted_DarkCrack_A01", (0.055, 0.048, 0.040), 0.96, 0.02),
        "earth": make_material("M_GIA_BloodAxeCairn_Sculpted_AshMud_A01", (0.33, 0.215, 0.125), 0.98, 0.08),
        "rawhide": make_material("M_GIA_BloodAxeCairn_Sculpted_Rawhide_A01", (0.72, 0.44, 0.17), 0.82, 0.13),
        "paint": make_material("M_GIA_BloodAxeCairn_Sculpted_OxideRed_A01", (0.62, 0.055, 0.038), 0.88, 0.12),
        "collision": make_material("M_AET_CollisionProxy_ReviewOnly_A01", (0.0, 0.35, 0.90), 0.5, 0.2),
    }


def make_collection(name: str, hidden: bool = False) -> bpy.types.Collection:
    col = bpy.data.collections.new(name)
    bpy.context.scene.collection.children.link(col)
    col.hide_viewport = hidden
    col.hide_render = hidden
    return col


def set_active(obj: bpy.types.Object) -> None:
    bpy.ops.object.select_all(action="DESELECT")
    bpy.context.view_layer.objects.active = obj
    obj.select_set(True)


def move_to(obj: bpy.types.Object, col: bpy.types.Collection) -> None:
    for current in list(obj.users_collection):
        current.objects.unlink(obj)
    col.objects.link(obj)


def apply_modifiers(obj: bpy.types.Object) -> None:
    set_active(obj)
    for mod in list(obj.modifiers):
        bpy.ops.object.modifier_apply(modifier=mod.name)


def roughen(obj: bpy.types.Object, amount: float, seed: int) -> None:
    for index, vertex in enumerate(obj.data.vertices):
        vertex.co.x += (math.sin(index * 17.19 + seed) * 0.5) * amount
        vertex.co.y += (math.sin(index * 11.73 + seed * 1.7) * 0.5) * amount
        vertex.co.z += (math.sin(index * 19.41 + seed * 2.1) * 0.5) * amount * 0.62


def add_irregular_slab(
    name: str,
    col: bpy.types.Collection,
    material: bpy.types.Material,
    dims: tuple[float, float, float],
    loc: tuple[float, float, float],
    rot: tuple[float, float, float],
    seed: int,
    bevel: float = 1.2,
    rough: float = 2.0,
) -> bpy.types.Object:
    bpy.ops.mesh.primitive_cube_add(size=1.0, location=loc, rotation=rot)
    obj = bpy.context.object
    obj.name = name
    obj.dimensions = dims
    obj.data.materials.append(material)
    set_active(obj)
    bpy.ops.object.transform_apply(location=False, rotation=False, scale=True)
    bevel_mod = obj.modifiers.new("AET_chipped_slab_edges", "BEVEL")
    bevel_mod.width = bevel
    bevel_mod.segments = 1
    normal = obj.modifiers.new("AET_weighted_normals", "WEIGHTED_NORMAL")
    apply_modifiers(obj)
    roughen(obj, rough, seed)
    obj["aet_length_cm"] = dims[0]
    obj["aet_width_cm"] = dims[1]
    obj["aet_height_cm"] = dims[2]
    move_to(obj, col)
    return obj


def add_profile_slab(
    name: str,
    col: bpy.types.Collection,
    material: bpy.types.Material,
    profile: list[tuple[float, float]],
    depth: float,
    loc: tuple[float, float, float],
    rot: tuple[float, float, float],
    seed: int,
    bevel: float = 1.1,
) -> bpy.types.Object:
    verts = [(x, -depth / 2.0, z) for x, z in profile] + [(x, depth / 2.0, z) for x, z in profile]
    count = len(profile)
    faces: list[tuple[int, ...]] = [tuple(range(count)), tuple(reversed(range(count, count * 2)))]
    for index in range(count):
        next_index = (index + 1) % count
        faces.append((index, next_index, count + next_index, count + index))
    mesh = bpy.data.meshes.new(f"{name}_Mesh")
    mesh.from_pydata(verts, [], faces)
    mesh.update()
    obj = bpy.data.objects.new(name, mesh)
    obj.location = loc
    obj.rotation_euler = rot
    obj.data.materials.append(material)
    obj["aet_profile_min_x"] = min(x for x, _ in profile)
    obj["aet_profile_max_x"] = max(x for x, _ in profile)
    obj["aet_profile_min_z"] = min(z for _, z in profile)
    obj["aet_profile_max_z"] = max(z for _, z in profile)
    obj["aet_depth_cm"] = depth
    col.objects.link(obj)
    bevel_mod = obj.modifiers.new("AET_profile_edge_wear", "BEVEL")
    bevel_mod.width = bevel
    bevel_mod.segments = 1
    normal = obj.modifiers.new("AET_weighted_normals", "WEIGHTED_NORMAL")
    apply_modifiers(obj)
    roughen(obj, 1.6, seed)
    return obj


def add_low_rock(
    name: str,
    col: bpy.types.Collection,
    material: bpy.types.Material,
    loc: tuple[float, float, float],
    scale: tuple[float, float, float],
    rot: tuple[float, float, float],
    seed: int,
    subdivisions: int = 1,
) -> bpy.types.Object:
    bpy.ops.mesh.primitive_ico_sphere_add(subdivisions=subdivisions, radius=1.0, location=loc, rotation=rot)
    obj = bpy.context.object
    obj.name = name
    obj.scale = scale
    obj.data.materials.append(material)
    set_active(obj)
    bpy.ops.object.transform_apply(location=False, rotation=False, scale=True)
    roughen(obj, max(scale) * 0.10, seed)
    try:
        bpy.ops.object.shade_flat()
    except Exception:
        pass
    move_to(obj, col)
    return obj


def local_to_world(obj: bpy.types.Object, coords: tuple[float, float, float]) -> Vector:
    return obj.matrix_world @ Vector(coords)


def cylinder_between(name: str, col: bpy.types.Collection, material: bpy.types.Material, start: Vector, end: Vector, radius: float, vertices: int = 8) -> bpy.types.Object:
    direction = end - start
    center = start + direction * 0.5
    bpy.ops.mesh.primitive_cylinder_add(vertices=vertices, radius=radius, depth=direction.length, location=center)
    obj = bpy.context.object
    obj.name = name
    obj.rotation_euler = direction.to_track_quat("Z", "Y").to_euler()
    obj.data.materials.append(material)
    move_to(obj, col)
    return obj


def add_top_decal(
    parent: bpy.types.Object,
    name: str,
    col: bpy.types.Collection,
    material: bpy.types.Material,
    center: tuple[float, float],
    size: tuple[float, float],
    yaw: float,
    z_offset: float,
) -> bpy.types.Object:
    sx, sy = size[0] * 0.5, size[1] * 0.5
    c, s = math.cos(yaw), math.sin(yaw)
    verts = []
    for x, y in [(-sx, -sy), (sx, -sy), (sx, sy), (-sx, sy)]:
        rx = center[0] + x * c - y * s
        ry = center[1] + x * s + y * c
        verts.append((rx, ry, z_offset))
    mesh = bpy.data.meshes.new(f"{name}_Mesh")
    mesh.from_pydata(verts, [], [(0, 1, 2, 3)])
    mesh.update()
    obj = bpy.data.objects.new(name, mesh)
    obj.location = parent.location
    obj.rotation_euler = parent.rotation_euler
    obj.data.materials.append(material)
    col.objects.link(obj)
    return obj


def add_face_decal(
    parent: bpy.types.Object,
    name: str,
    col: bpy.types.Collection,
    material: bpy.types.Material,
    center: tuple[float, float],
    size: tuple[float, float],
    yaw: float,
    y_offset: float,
) -> bpy.types.Object:
    sx, sz = size[0] * 0.5, size[1] * 0.5
    c, s = math.cos(yaw), math.sin(yaw)
    verts = []
    for x, z in [(-sx, -sz), (sx, -sz), (sx, sz), (-sx, sz)]:
        rx = center[0] + x * c - z * s
        rz = center[1] + x * s + z * c
        verts.append((rx, y_offset, rz))
    mesh = bpy.data.meshes.new(f"{name}_Mesh")
    mesh.from_pydata(verts, [], [(0, 1, 2, 3)])
    mesh.update()
    obj = bpy.data.objects.new(name, mesh)
    obj.location = parent.location
    obj.rotation_euler = parent.rotation_euler
    obj.data.materials.append(material)
    col.objects.link(obj)
    return obj


def add_lashing_band(parent: bpy.types.Object, prefix: str, col: bpy.types.Collection, material: bpy.types.Material, local_x: float, width: float, top_z: float) -> list[bpy.types.Object]:
    pieces = []
    for xoff in (-5.0, -1.8, 1.8, 5.0):
        pieces.append(
            cylinder_between(
                f"{prefix}_Cord_{xoff:+.1f}",
                col,
                material,
                local_to_world(parent, (local_x + xoff, -width * 0.52, top_z)),
                local_to_world(parent, (local_x + xoff, width * 0.52, top_z)),
                1.35,
            )
        )
    for y in (-width * 0.52, width * 0.52):
        pieces.append(
            cylinder_between(
                f"{prefix}_EdgeTie_{y:+.1f}",
                col,
                material,
                local_to_world(parent, (local_x - 6.4, y, top_z + 0.6)),
                local_to_world(parent, (local_x + 6.4, y, top_z - 0.6)),
                1.0,
            )
        )
    return pieces


def add_earth_base(col: bpy.types.Collection, material: bpy.types.Material, detail: int) -> bpy.types.Object:
    segments = {0: 60, 1: 36, 2: 22, 3: 14}[detail]
    footprint = []
    for index in range(segments):
        angle = math.tau * index / segments
        n = 0.86 + RNG.random() * 0.22
        footprint.append((math.cos(angle) * 170.0 * n, math.sin(angle) * 105.0 * n))
    verts = [(x, y, -3.5) for x, y in footprint] + [(x * 0.98, y * 0.98, 3.5) for x, y in footprint]
    faces: list[tuple[int, ...]] = [tuple(reversed(range(segments))), tuple(range(segments, segments * 2))]
    for index in range(segments):
        nxt = (index + 1) % segments
        faces.append((index, nxt, segments + nxt, segments + index))
    mesh = bpy.data.meshes.new("A1_Sculpted_AshMudBase_Mesh")
    mesh.from_pydata(verts, [], faces)
    mesh.update()
    obj = bpy.data.objects.new(f"A1_Sculpted_AshMudBase_LOD{detail}", mesh)
    obj.location = (0.0, -5.0, 4.0)
    obj.data.materials.append(material)
    col.objects.link(obj)
    return obj


def add_stone_details(obj: bpy.types.Object, prefix: str, col: bpy.types.Collection, mats: dict[str, bpy.types.Material], top_z: float, length: float, width: float, seed: int, count: int) -> list[bpy.types.Object]:
    rng = random.Random(seed)
    details = []
    for index in range(count):
        details.append(
            add_top_decal(
                obj,
                f"{prefix}_WarmChip_{index:02d}",
                col,
                mats["stone_light"],
                (rng.uniform(-length * 0.40, length * 0.40), rng.uniform(-width * 0.38, width * 0.38)),
                (rng.uniform(9, 28), rng.uniform(1.1, 2.4)),
                rng.uniform(-0.9, 0.9),
                top_z + 0.30,
            )
        )
    for index in range(max(5, count // 2)):
        details.append(
            add_top_decal(
                obj,
                f"{prefix}_DarkCrack_{index:02d}",
                col,
                mats["crack"],
                (rng.uniform(-length * 0.42, length * 0.42), rng.uniform(-width * 0.36, width * 0.36)),
                (rng.uniform(14, 38), rng.uniform(0.8, 1.7)),
                rng.uniform(-0.9, 0.9),
                top_z + 0.34,
            )
        )
    return details


def build_lod(col: bpy.types.Collection, mats: dict[str, bpy.types.Material], detail: int) -> list[bpy.types.Object]:
    objects: list[bpy.types.Object] = [add_earth_base(col, mats["earth"], detail)]
    include_detail = detail == 0
    include_minor = detail <= 1
    include_paint = detail <= 2
    include_rope = detail <= 1

    central = add_irregular_slab(
        f"A1_Sculpted_MainPaintedFallenSlab_LOD{detail}",
        col,
        mats["stone"],
        (224.0, 72.0, 24.0),
        (0.0, -16.0, 51.0),
        (math.radians(2.5), math.radians(-15.0), math.radians(-8.0)),
        100 + detail,
        1.2,
        3.0,
    )
    objects.append(central)

    rear = add_profile_slab(
        f"A1_Sculpted_RearTallBrokenSlab_LOD{detail}",
        col,
        mats["stone_dark"],
        [(-33, -65), (24, -64), (35, 14), (24, 58), (2, 79), (-22, 61), (-36, 7)],
        28.0,
        (20.0, 33.0, 76.0),
        (math.radians(-11.0), math.radians(8.0), math.radians(8.0)),
        200 + detail,
        1.2,
    )
    objects.append(rear)

    right = add_profile_slab(
        f"A1_Sculpted_RightBoundUpright_LOD{detail}",
        col,
        mats["stone"],
        [(-28, -43), (23, -42), (31, 15), (12, 53), (-17, 45), (-30, -8)],
        30.0,
        (112.0, 4.0, 55.0),
        (math.radians(2.0), math.radians(-7.0), math.radians(-11.0)),
        300 + detail,
        1.0,
    )
    objects.append(right)

    left_low = add_irregular_slab(
        f"A1_Sculpted_LeftStackLowSlab_LOD{detail}",
        col,
        mats["stone"],
        (112.0, 40.0, 22.0),
        (-102.0, -37.0, 27.0),
        (math.radians(1.0), math.radians(2.0), math.radians(-12.0)),
        400 + detail,
        0.8,
        1.8,
    )
    objects.append(left_low)
    if detail <= 2:
        left_cap = add_irregular_slab(
            f"A1_Sculpted_LeftStackTopSlab_LOD{detail}",
            col,
            mats["stone"],
            (82.0, 34.0, 17.0),
            (-105.0, -45.0, 46.0),
            (math.radians(-2.0), math.radians(2.0), math.radians(-8.0)),
            410 + detail,
            0.7,
            1.5,
        )
        objects.append(left_cap)

    if include_minor:
        objects.extend(
            [
                add_profile_slab(
                    f"A1_Sculpted_LeftRearShard_LOD{detail}",
                    col,
                    mats["stone_dark"],
                    [(-15, -35), (14, -34), (18, 23), (3, 48), (-16, 18)],
                    18.0,
                    (-48.0, 26.0, 57.0),
                    (math.radians(-7), math.radians(12), math.radians(11)),
                    500 + detail,
                    0.9,
                ),
                add_profile_slab(
                    f"A1_Sculpted_CenterNeedleShard_LOD{detail}",
                    col,
                    mats["stone_dark"],
                    [(-9, -36), (10, -35), (13, 24), (2, 47), (-10, 22)],
                    13.0,
                    (-15.0, 20.0, 58.0),
                    (math.radians(-9), math.radians(-5), math.radians(-4)),
                    510 + detail,
                    0.8,
                ),
            ]
        )

    if include_paint:
        objects.extend(
            [
                add_top_decal(central, f"A1_Sculpted_MainRedLongStroke_LOD{detail}", col, mats["paint"], (-8, -2), (150, 13), math.radians(18), 12.35),
                add_top_decal(central, f"A1_Sculpted_MainRedCrossA_LOD{detail}", col, mats["paint"], (-45, 14), (82, 11), math.radians(-31), 12.50),
                add_top_decal(central, f"A1_Sculpted_MainRedCrossB_LOD{detail}", col, mats["paint"], (34, 7), (74, 10), math.radians(-24), 12.65),
                add_face_decal(rear, f"A1_Sculpted_RearRedSlash_LOD{detail}", col, mats["paint"], (0, 10), (14, 58), math.radians(-12), -14.2),
                add_face_decal(right, f"A1_Sculpted_RightRedScuff_LOD{detail}", col, mats["paint"], (4, 5), (8, 42), math.radians(2), -15.4),
            ]
        )

    if include_detail:
        objects.extend(add_stone_details(central, "A1_Sculpted_Main", col, mats, 12.9, 210, 66, 700, 26))
        rng = random.Random(930)
        for index in range(16):
            objects.append(
                add_face_decal(
                    rear,
                    f"A1_Sculpted_RearWarmChip_{index:02d}",
                    col,
                    mats["stone_light"],
                    (rng.uniform(-22, 20), rng.uniform(-28, 54)),
                    (rng.uniform(1.2, 2.8), rng.uniform(10, 24)),
                    rng.uniform(-0.26, 0.26),
                    -14.3,
                )
            )
        for index in range(10):
            objects.append(
                add_face_decal(
                    right,
                    f"A1_Sculpted_RightWarmChip_{index:02d}",
                    col,
                    mats["stone_light"],
                    (rng.uniform(-18, 18), rng.uniform(-24, 42)),
                    (rng.uniform(1.2, 2.6), rng.uniform(9, 22)),
                    rng.uniform(-0.24, 0.24),
                    -15.2,
                )
            )

    if include_rope:
        objects.extend(add_lashing_band(central, f"A1_Sculpted_LeftRawhideBind_LOD{detail}", col, mats["rawhide"], -72.0, 66.0, 15.2))
        objects.extend(add_lashing_band(central, f"A1_Sculpted_RightRawhideBind_LOD{detail}", col, mats["rawhide"], 72.0, 66.0, 15.2))
        objects.append(cylinder_between(f"A1_Sculpted_RightUprightRawhideFront_LOD{detail}", col, mats["rawhide"], local_to_world(right, (-27, -15, 2)), local_to_world(right, (27, -15, 3)), 1.9))
        objects.append(cylinder_between(f"A1_Sculpted_RightUprightRawhideBack_LOD{detail}", col, mats["rawhide"], local_to_world(right, (-26, 15, 3)), local_to_world(right, (26, 15, 2)), 1.6))

    pebble_count = {0: 74, 1: 34, 2: 12, 3: 0}[detail]
    for index in range(pebble_count):
        angle = RNG.random() * math.tau
        radius = 45.0 + RNG.random() * 128.0
        x = math.cos(angle) * radius * 1.02
        y = math.sin(angle) * radius * 0.62 - 5.0
        if -83 < x < 83 and -48 < y < 46 and RNG.random() < 0.78:
            continue
        sx = RNG.uniform(6, 17)
        sy = RNG.uniform(4, 13)
        sz = RNG.uniform(2.5, 7.5)
        objects.append(add_low_rock(f"A1_Sculpted_Rubble_{index:02d}_LOD{detail}", col, mats["stone"], (x, y, 8 + sz), (sx, sy, sz), (RNG.uniform(-0.2, 0.2), RNG.uniform(-0.18, 0.18), RNG.uniform(0, math.tau)), 8000 + index + detail * 100))

    return [obj for obj in objects if getattr(obj, "type", None) == "MESH"]


def add_collision(col: bpy.types.Collection, material: bpy.types.Material) -> bpy.types.Object:
    bpy.ops.mesh.primitive_cube_add(size=1.0, location=(0.0, -4.0, 80.0))
    obj = bpy.context.object
    obj.name = f"UCX_{ASSET_NAME}_00"
    obj.dimensions = (330.0, 220.0, 165.0)
    obj.data.materials.append(material)
    set_active(obj)
    bpy.ops.object.transform_apply(location=False, rotation=False, scale=True)
    obj.display_type = "WIRE"
    obj.hide_render = True
    move_to(obj, col)
    return obj


def tri_count(obj: bpy.types.Object) -> int:
    obj.data.calc_loop_triangles()
    return len(obj.data.loop_triangles)


def col_tri_count(col: bpy.types.Collection) -> int:
    return sum(tri_count(obj) for obj in col.objects if getattr(obj, "type", None) == "MESH")


def col_bounds(col: bpy.types.Collection) -> tuple[float, float, float]:
    points = []
    for obj in col.objects:
        if getattr(obj, "type", None) == "MESH":
            points.extend(obj.matrix_world @ Vector(corner) for corner in obj.bound_box)
    return (
        max(p.x for p in points) - min(p.x for p in points),
        max(p.y for p in points) - min(p.y for p in points),
        max(p.z for p in points) - min(p.z for p in points),
    )


def export_fbx(path: Path, objects: list[bpy.types.Object]) -> None:
    ensure_dir(path.parent)
    bpy.ops.object.select_all(action="DESELECT")
    for obj in objects:
        obj.hide_viewport = False
        obj.hide_set(False)
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


def setup_lighting() -> None:
    scene = bpy.context.scene
    try:
        scene.render.engine = "BLENDER_EEVEE_NEXT"
    except TypeError:
        scene.render.engine = "BLENDER_EEVEE"
    scene.view_settings.view_transform = "Standard"
    scene.view_settings.exposure = 0.52
    scene.view_settings.gamma = 1.0
    if scene.world:
        scene.world.color = (0.68, 0.66, 0.60)
    for name, kind, loc, energy, size in [
        ("AET_Sculpted_Key", "AREA", (-300, -420, 440), 110000, 520),
        ("AET_Sculpted_Fill", "AREA", (340, -160, 300), 68000, 680),
        ("AET_Sculpted_Rim", "POINT", (0, 320, 250), 22000, 0),
        ("AET_Sculpted_Top", "AREA", (0, 0, 560), 56000, 760),
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
    scene.render.resolution_x = 1700
    scene.render.resolution_y = 1050
    if hasattr(scene, "eevee") and hasattr(scene.eevee, "taa_render_samples"):
        scene.eevee.taa_render_samples = 64
    reviews = [
        ("Front", (330, -570, 290), (0, -6, 52), 355),
        ("Right", (610, -5, 260), (0, -2, 55), 355),
        ("Back", (-300, 580, 260), (0, 0, 55), 355),
        ("Left", (-610, 0, 260), (0, -2, 55), 355),
        ("Top", (0, 0, 720), (0, 0, 0), 360),
        ("Beauty", (360, -525, 320), (0, -5, 56), 382),
    ]
    for label, loc, target, scale in reviews:
        set_camera(f"AET_Sculpted_{label}Camera", loc, target, scale)
        scene.render.filepath = str(REVIEW_ROOT / f"{ASSET_NAME}_{label}Review.png")
        bpy.ops.render.render(write_still=True)


def build() -> None:
    clear_scene()
    setup_scene()
    setup_lighting()
    mats = make_materials()
    lod_cols = [make_collection(f"{ASSET_NAME}_LOD{i}", hidden=i > 0) for i in range(4)]
    collision_col = make_collection(f"{ASSET_NAME}_Collision_Source", hidden=True)
    lod_objects = [build_lod(lod_cols[i], mats, i) for i in range(4)]
    collision = add_collision(collision_col, mats["collision"])

    add_asset_metadata(
        ASSET_NAME,
        "A01 sculpted mid-poly DCC candidate using approved A1 crop and turnaround as reference; authored stone geometry, red paint, rawhide lashings, LODs, and collision. Review candidate only.",
        UNREAL_PATH,
    )

    render_reviews()

    blend_path = BLENDER_ROOT / REL_PATH / f"{ASSET_NAME}.blend"
    export_path = EXPORT_ROOT / REL_PATH / f"{ASSET_NAME}.fbx"
    ensure_dir(blend_path.parent)
    ensure_dir(export_path.parent)
    bpy.ops.wm.save_as_mainfile(filepath=str(blend_path))
    export_fbx(export_path, lod_objects[0] + [collision])
    for idx, objects in enumerate(lod_objects):
        export_fbx(export_path.with_name(f"{ASSET_NAME}_LOD{idx}.fbx"), objects)
    export_fbx(export_path.with_name(f"{ASSET_NAME}_UCX.fbx"), [collision])

    bounds = col_bounds(lod_cols[0])
    print(f"Built {blend_path.relative_to(ROOT)}")
    print(f"Exported {export_path.relative_to(ROOT)}")
    for idx, col in enumerate(lod_cols):
        print(f"LOD{idx} tris: {col_tri_count(col)}")
    print(f"LOD0 bounds: {bounds[0]:.2f}w x {bounds[1]:.2f}d x {bounds[2]:.2f}h cm")
    print("Collision proxies: 1")


if __name__ == "__main__":
    build()
