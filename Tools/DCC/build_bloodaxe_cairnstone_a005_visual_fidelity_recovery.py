#!/usr/bin/env python3
"""Build the A005 Steps 01-16 visual-fidelity recovery candidate.

The build starts from the authoritative A02 source dimensions and source-owned
texture atlas. It does not open or derive geometry from the quarantined A005
Step 12/15/16 meshes.
"""

from __future__ import annotations

import argparse
import hashlib
import json
import math
import random
import shutil
import sys
from pathlib import Path
from typing import Any, Dict, Iterable, List, Sequence, Tuple


ASSET = "SM_GIA_BloodAxeCairnstone_A005"
CONTRACT = "A005-CR-STEPS01-16-VISUAL-FIDELITY-RECOVERY-A01"
SCRIPT = Path(__file__).resolve()
ROOT = SCRIPT.parents[2]
BLUEPRINT_ROOT = Path("docs/assets/blueprints") / ASSET
PLAN_REL = BLUEPRINT_ROOT / "manifests/VISUAL_FIDELITY_RECOVERY_A01_PLAN.json"
SOURCE_REL = Path("docs/assets/reference/bloodaxe_cairnstone_asset/REF_GIA_BloodAxeCairnstoneAsset_A02_BlueprintTemplate.png")
UV_PLAN_REL = BLUEPRINT_ROOT / "manifests/STEP_14_UV_OWNERSHIP_PLAN.json"
MASK_MANIFEST_REL = Path("SourceAssets/Textures/Props/Giants/BloodAxe/Cairns") / ASSET / "Technical/SM_GIA_BloodAxeCairnstone_A005_SOURCE_MASK_MANIFEST_A01.json"
OLD_TEXTURE_ROOT = Path("SourceAssets/Textures/Props/Giants/BloodAxe/Cairns") / ASSET
TEXTURE_ROOT = OLD_TEXTURE_ROOT / "VisualFidelityRecovery_A01"
BC_REL = TEXTURE_ROOT / f"T_GIA_BloodAxeCairnstone_A005_VF_A01_BC.png"
N_REL = TEXTURE_ROOT / f"T_GIA_BloodAxeCairnstone_A005_VF_A01_N.png"
ORM_REL = TEXTURE_ROOT / f"T_GIA_BloodAxeCairnstone_A005_VF_A01_ORM.png"
DCC_ROOT = Path("SourceAssets/Blender/Props/Giants/BloodAxe/Cairns") / ASSET
BLEND_REL = DCC_ROOT / f"{ASSET}_DCCGameReady_A02.blend"
MANIFEST_REL = DCC_ROOT / f"{ASSET}_VISUAL_FIDELITY_RECOVERY_A01_MANIFEST.json"
EXPORT_ROOT = Path("SourceAssets/Exports/Props/Giants/BloodAxe/Cairns") / ASSET / "VisualFidelityRecovery_A01"
FBX_RELS = {
    "LOD0": EXPORT_ROOT / f"{ASSET}_A02.fbx",
    "LOD1": EXPORT_ROOT / f"{ASSET}_A02_LOD1.fbx",
    "LOD2": EXPORT_ROOT / f"{ASSET}_A02_LOD2.fbx",
    "LOD3": EXPORT_ROOT / f"{ASSET}_A02_LOD3.fbx",
}

TARGET_BOUNDS = (140.0, 110.0, 220.0)
LOD_RATIOS = {"LOD0": 1.0, "LOD1": 0.46, "LOD2": 0.21, "LOD3": 0.08}
REQUIRED_FEATURES = (
    "rounded_irregular_tapered_monolith",
    "two_independent_annular_masonry_courses",
    "irregular_peripheral_apron_shell",
    "face_owned_blood_axe_basecolor_normal_consumer",
    "face_owned_red_fissure_and_rune_basecolor_normal_consumers",
    "dark_weathered_stone_material",
)

Vec2 = Tuple[float, float]
Vec3 = Tuple[float, float, float]


def parse_args(argv: Sequence[str]) -> argparse.Namespace:
    parser = argparse.ArgumentParser()
    mode = parser.add_mutually_exclusive_group(required=True)
    mode.add_argument("--schema-only", action="store_true")
    mode.add_argument("--build", action="store_true")
    return parser.parse_args(list(argv))


def blender_args() -> List[str]:
    if "--" in sys.argv:
        return sys.argv[sys.argv.index("--") + 1 :]
    return sys.argv[1:]


def sha256_file(path: Path) -> str:
    digest = hashlib.sha256()
    with path.open("rb") as handle:
        for chunk in iter(lambda: handle.read(1024 * 1024), b""):
            digest.update(chunk)
    return digest.hexdigest()


def load_json(rel: Path) -> Dict[str, Any]:
    with (ROOT / rel).open("r", encoding="utf-8") as handle:
        return json.load(handle)


def schema_report() -> Dict[str, Any]:
    plan = load_json(PLAN_REL)
    source = ROOT / SOURCE_REL
    if sha256_file(source) != plan["source_authority"]["sha256"]:
        raise RuntimeError("authoritative source hash mismatch")
    return {
        "schema": "aerathea.a005_visual_fidelity_builder_preflight.v1",
        "asset_id": ASSET,
        "contract_id": CONTRACT,
        "status": "pass_schema_only_no_output",
        "bpy_imported": "bpy" in sys.modules,
        "source_sha256": sha256_file(source),
        "target_bounds_cm": list(TARGET_BOUNDS),
        "lod0_triangle_gate": [4000, 10000],
        "required_features": list(REQUIRED_FEATURES),
        "outputs": [str(BLEND_REL), str(MANIFEST_REL), *[str(value) for value in FBX_RELS.values()]],
    }


def select_only(bpy: Any, objects: Sequence[Any]) -> None:
    bpy.ops.object.mode_set(mode="OBJECT") if bpy.context.object and bpy.context.object.mode != "OBJECT" else None
    bpy.ops.object.select_all(action="DESELECT")
    for obj in objects:
        obj.hide_set(False)
        obj.select_set(True)
    bpy.context.view_layer.objects.active = objects[0]


def apply_transform(bpy: Any, obj: Any) -> None:
    select_only(bpy, [obj])
    bpy.ops.object.transform_apply(location=False, rotation=True, scale=True)


def mesh_triangles(mesh: Any) -> int:
    mesh.calc_loop_triangles()
    return len(mesh.loop_triangles)


def object_bounds(obj: Any) -> Dict[str, List[float]]:
    points = [obj.matrix_world @ obj.data.vertices[index].co for index in range(len(obj.data.vertices))]
    minimum = [min(float(point[axis]) for point in points) for axis in range(3)]
    maximum = [max(float(point[axis]) for point in points) for axis in range(3)]
    return {
        "min": minimum,
        "max": maximum,
        "dimensions": [maximum[index] - minimum[index] for index in range(3)],
    }


def create_mesh_object(bpy: Any, name: str, vertices: Sequence[Vec3], faces: Sequence[Sequence[int]], collection: Any) -> Any:
    mesh = bpy.data.meshes.new(f"{name}_MESH")
    mesh.from_pydata(vertices, [], faces)
    mesh.validate(verbose=False, clean_customdata=False)
    mesh.update(calc_edges=True)
    obj = bpy.data.objects.new(name, mesh)
    collection.objects.link(obj)
    return obj


def superellipse_ring(a: float, b: float, z: float, segments: int, exponent: float, noise_seed: int, noise_amp: float) -> List[Vec3]:
    result: List[Vec3] = []
    for index in range(segments):
        angle = math.tau * index / segments
        cosine = math.cos(angle)
        sine = math.sin(angle)
        x = a * math.copysign(abs(cosine) ** (2.0 / exponent), cosine)
        y = b * math.copysign(abs(sine) ** (2.0 / exponent), sine)
        if index % (segments // 4) != 0:
            noise = noise_amp * (
                0.55 * math.sin(index * 1.733 + noise_seed * 0.71)
                + 0.30 * math.sin(index * 3.117 - noise_seed * 0.43)
            )
            radial_x = x / max(a, 1.0e-9)
            radial_y = y / max(b, 1.0e-9)
            x += radial_x * noise
            y += radial_y * noise
        result.append((x, y, z))
    return result


def loft(bpy: Any, name: str, profiles: Sequence[Tuple[float, float, float, float]], segments: int, exponent: float, collection: Any) -> Any:
    vertices: List[Vec3] = []
    faces: List[List[int]] = []
    for ring_index, (z, width, depth, noise) in enumerate(profiles):
        vertices.extend(superellipse_ring(width * 0.5, depth * 0.5, z, segments, exponent, ring_index + 17, noise))
    rings = len(profiles)
    for ring in range(rings - 1):
        for index in range(segments):
            nxt = (index + 1) % segments
            lower = ring * segments
            upper = (ring + 1) * segments
            faces.append([lower + index, lower + nxt, upper + nxt, upper + index])
    bottom_center = len(vertices)
    vertices.append((0.0, 0.0, profiles[0][0]))
    top_center = len(vertices)
    vertices.append((0.0, 0.0, profiles[-1][0]))
    for index in range(segments):
        nxt = (index + 1) % segments
        faces.append([bottom_center, nxt, index])
        top = (rings - 1) * segments
        faces.append([top_center, top + index, top + nxt])
    return create_mesh_object(bpy, name, vertices, faces, collection)


def add_material_slots(obj: Any, stone: Any, pigment: Any, pigment_only: bool = False) -> None:
    obj.data.materials.clear()
    obj.data.materials.append(stone)
    obj.data.materials.append(pigment)
    for polygon in obj.data.polygons:
        polygon.material_index = 1 if pigment_only else 0


def bevelled_block(bpy: Any, name: str, center: Vec3, dimensions: Vec3, rotation_z: float, bevel: float, stone: Any, pigment: Any, collection: Any, rng: random.Random) -> Any:
    bpy.ops.mesh.primitive_cube_add(size=1.0, location=center, rotation=(0.0, 0.0, rotation_z))
    obj = bpy.context.object
    obj.name = name
    for old in list(obj.users_collection):
        old.objects.unlink(obj)
    collection.objects.link(obj)
    obj.dimensions = dimensions
    apply_transform(bpy, obj)
    for vertex in obj.data.vertices:
        vertex.co.x += rng.uniform(-0.5, 0.5)
        vertex.co.y += rng.uniform(-0.35, 0.35)
        vertex.co.z += rng.uniform(-0.3, 0.3)
    modifier = obj.modifiers.new("HandCutEdgeBevel", "BEVEL")
    modifier.width = bevel
    modifier.segments = 1
    modifier.affect = "EDGES"
    select_only(bpy, [obj])
    bpy.ops.object.modifier_apply(modifier=modifier.name)
    add_material_slots(obj, stone, pigment)
    return obj


def masonry_course(bpy: Any, prefix: str, count: int, rx: float, ry: float, z_center: float, height: float, stone: Any, pigment: Any, collection: Any, seed: int) -> List[Any]:
    rng = random.Random(seed)
    result: List[Any] = []
    for index in range(count):
        angle = math.tau * index / count + rng.uniform(-0.025, 0.025)
        x = rx * math.cos(angle)
        y = ry * math.sin(angle)
        tangent_x = -rx * math.sin(angle)
        tangent_y = ry * math.cos(angle)
        rotation = math.atan2(tangent_y, tangent_x)
        tangent_length = 18.5 + rng.uniform(-2.0, 2.5)
        radial_depth = 15.0 + rng.uniform(-1.8, 1.8)
        block_height = height + rng.uniform(-1.0, 1.2)
        result.append(
            bevelled_block(
                bpy,
                f"{prefix}_{index:02d}",
                (x, y, z_center + rng.uniform(-0.35, 0.35)),
                (tangent_length, radial_depth, block_height),
                rotation + rng.uniform(-0.04, 0.04),
                1.25,
                stone,
                pigment,
                collection,
                rng,
            )
        )
    return result


def rubble_stones(bpy: Any, stone: Any, pigment: Any, collection: Any) -> List[Any]:
    rng = random.Random(5005)
    result: List[Any] = []
    count = 32
    for index in range(count):
        angle = math.tau * index / count + rng.uniform(-0.045, 0.045)
        radius_x = 62.0 + rng.uniform(-2.5, 2.5)
        radius_y = 47.0 + rng.uniform(-2.0, 2.0)
        x = radius_x * math.cos(angle)
        y = radius_y * math.sin(angle)
        bpy.ops.mesh.primitive_ico_sphere_add(subdivisions=1, radius=1.0, location=(x, y, 5.0 + rng.uniform(-0.5, 1.5)))
        obj = bpy.context.object
        obj.name = f"RUBBLE_{index:02d}"
        for old in list(obj.users_collection):
            old.objects.unlink(obj)
        collection.objects.link(obj)
        obj.scale = (
            rng.uniform(5.0, 8.5),
            rng.uniform(4.0, 6.8),
            rng.uniform(4.2, 8.0),
        )
        obj.rotation_euler = (
            rng.uniform(-0.25, 0.25),
            rng.uniform(-0.25, 0.25),
            angle + rng.uniform(-0.5, 0.5),
        )
        apply_transform(bpy, obj)
        add_material_slots(obj, stone, pigment)
        result.append(obj)
    return result


def body_half_depth(z: float) -> float:
    stations = [(35.0, 38.0), (45.0, 43.0), (65.0, 45.0), (100.0, 40.0), (140.0, 34.0), (180.0, 28.0), (220.0, 23.0)]
    if z <= stations[0][0]:
        return stations[0][1]
    for (z0, value0), (z1, value1) in zip(stations, stations[1:]):
        if z0 <= z <= z1:
            alpha = (z - z0) / (z1 - z0)
            return value0 + alpha * (value1 - value0)
    return stations[-1][1]


def body_half_width(z: float) -> float:
    stations = [(35.0, 50.0), (45.0, 58.0), (65.0, 59.0), (100.0, 52.0), (140.0, 45.0), (180.0, 37.0), (220.0, 32.0)]
    if z <= stations[0][0]:
        return stations[0][1]
    for (z0, value0), (z1, value1) in zip(stations, stations[1:]):
        if z0 <= z <= z1:
            alpha = (z - z0) / (z1 - z0)
            return value0 + alpha * (value1 - value0)
    return stations[-1][1]


def prism_polygon(
    bpy: Any,
    name: str,
    xz: Sequence[Tuple[float, float]],
    outward: float,
    thickness: float,
    stone: Any,
    pigment: Any,
    collection: Any,
    pigment_only: bool = True,
) -> Any:
    vertices: List[Vec3] = []
    for x, z in xz:
        y = -body_half_depth(z) - outward
        vertices.append((x, y, z))
    for x, z in xz:
        y = -body_half_depth(z) - outward - thickness
        vertices.append((x, y, z))
    count = len(xz)
    faces: List[List[int]] = [list(range(count)), list(reversed(range(count, count * 2)))]
    for index in range(count):
        nxt = (index + 1) % count
        faces.append([index, nxt, count + nxt, count + index])
    obj = create_mesh_object(bpy, name, vertices, faces, collection)
    add_material_slots(obj, stone, pigment, pigment_only=pigment_only)
    return obj


def relief_line(
    bpy: Any,
    name: str,
    xz: Sequence[Tuple[float, float]],
    closed: bool,
    stone: Any,
    pigment: Any,
    collection: Any,
    bevel_depth: float = 0.72,
    outward: float = 1.15,
    pigment_only: bool = True,
) -> Any:
    curve = bpy.data.curves.new(f"{name}_CURVE", "CURVE")
    curve.dimensions = "3D"
    curve.resolution_u = 1
    curve.resolution_v = 0
    curve.bevel_depth = bevel_depth
    curve.bevel_resolution = 0
    curve.resolution_u = 1
    curve.use_fill_caps = True
    spline = curve.splines.new("POLY")
    spline.points.add(len(xz) - 1)
    for point, (x, z) in zip(spline.points, xz):
        point.co = (x, -body_half_depth(z) - outward, z, 1.0)
    spline.use_cyclic_u = closed
    obj = bpy.data.objects.new(name, curve)
    collection.objects.link(obj)
    curve.materials.append(pigment)
    select_only(bpy, [obj])
    bpy.ops.object.convert(target="MESH")
    obj = bpy.context.object
    add_material_slots(obj, stone, pigment, pigment_only=pigment_only)
    return obj


def axe_relief(bpy: Any, stone: Any, pigment: Any, collection: Any) -> List[Any]:
    left = [(-2.8, 161.0), (-10.0, 180.0), (-27.0, 187.0), (-23.0, 174.0), (-31.0, 158.0), (-25.0, 145.0), (-13.0, 150.0), (-10.0, 160.0)]
    right = [(-x, z) for x, z in left]
    filled: List[Tuple[str, List[Tuple[float, float]]]] = [
        ("AXE_SHAFT_RELIEF", [(-2.7, 67.0), (2.7, 67.0), (3.2, 162.0), (-3.2, 162.0)]),
        ("AXE_LEFT_BLADE_RELIEF", left),
        ("AXE_RIGHT_BLADE_RELIEF", right),
        ("AXE_POMMEL_RELIEF", [(0.0, 57.0), (7.0, 67.0), (0.0, 78.0), (-7.0, 67.0)]),
    ]
    result = [prism_polygon(bpy, name, points, 1.35, 0.6, stone, pigment, collection) for name, points in filled]
    ornament_paths: List[Tuple[str, List[Tuple[float, float]], bool, bool]] = [
        ("AXE_LEFT_INNER_CUT", [(-6.0, 161.0), (-13.0, 174.0), (-22.0, 179.0), (-19.0, 169.0), (-24.0, 158.0), (-19.0, 150.0)], False, False),
        ("AXE_RIGHT_INNER_CUT", [(6.0, 161.0), (13.0, 174.0), (22.0, 179.0), (19.0, 169.0), (24.0, 158.0), (19.0, 150.0)], False, False),
        ("AXE_UPPER_RUNE_STEM", [(0.0, 190.0), (0.0, 216.0)], False, True),
        ("AXE_UPPER_RUNE_A", [(0.0, 190.0), (5.0, 196.0), (0.0, 202.0), (-5.0, 196.0)], True, True),
        ("AXE_UPPER_RUNE_B", [(0.0, 204.0), (4.0, 209.0), (0.0, 214.0), (-4.0, 209.0)], True, True),
        ("AXE_LOWER_RUNE", [(0.0, 80.0), (5.0, 86.0), (0.0, 92.0), (-5.0, 86.0)], True, True),
    ]
    for name, points, closed, pigment_only in ornament_paths:
        result.append(
            relief_line(
                bpy,
                name,
                points,
                closed,
                stone,
                pigment,
                collection,
                bevel_depth=0.62 if pigment_only else 0.48,
                outward=2.05,
                pigment_only=pigment_only,
            )
        )
    return result


def front_surface_stones(bpy: Any, stone: Any, pigment: Any, collection: Any) -> List[Any]:
    """Source-critical irregular face stones; gaps retain visible fissure channels."""
    rng = random.Random(120512)
    rows = [(39.0, 69.0, 4), (70.5, 103.0, 4), (104.5, 137.0, 4), (138.5, 169.0, 4), (170.5, 198.0, 3), (199.5, 218.5, 3)]
    result: List[Any] = []
    for row_index, (z0, z1, columns) in enumerate(rows):
        zmid = (z0 + z1) * 0.5
        half_width = body_half_width(zmid) - 2.2
        step = (half_width * 2.0) / columns
        for column in range(columns):
            x0 = -half_width + column * step + 0.8
            x1 = -half_width + (column + 1) * step - 0.8
            if (row_index + column) % 2:
                x0 += 0.65
                x1 += 0.35
            lower_l = z0 + rng.uniform(0.2, 1.2)
            lower_r = z0 + rng.uniform(0.2, 1.2)
            upper_l = z1 - rng.uniform(0.2, 1.2)
            upper_r = z1 - rng.uniform(0.2, 1.2)
            points = [
                (x0 + rng.uniform(-0.8, 0.5), lower_l),
                ((x0 + x1) * 0.5 + rng.uniform(-1.0, 1.0), min(lower_l, lower_r) + rng.uniform(-0.4, 0.8)),
                (x1 + rng.uniform(-0.5, 0.8), lower_r),
                (x1 + rng.uniform(-0.7, 0.5), (z0 + z1) * 0.5 + rng.uniform(-1.8, 1.8)),
                (x1 + rng.uniform(-0.6, 0.5), upper_r),
                ((x0 + x1) * 0.5 + rng.uniform(-1.0, 1.0), max(upper_l, upper_r) + rng.uniform(-0.8, 0.4)),
                (x0 + rng.uniform(-0.5, 0.7), upper_l),
                (x0 + rng.uniform(-0.5, 0.7), (z0 + z1) * 0.5 + rng.uniform(-1.8, 1.8)),
            ]
            obj = prism_polygon(
                bpy,
                f"FRONT_FACE_STONE_{row_index:02d}_{column:02d}",
                points,
                0.32,
                0.48,
                stone,
                pigment,
                collection,
                pigment_only=False,
            )
            modifier = obj.modifiers.new("ChippedStoneEdge", "BEVEL")
            modifier.width = 0.42
            modifier.segments = 1
            modifier.affect = "EDGES"
            select_only(bpy, [obj])
            bpy.ops.object.modifier_apply(modifier=modifier.name)
            result.append(obj)
    return result


def right_surface_plate(bpy: Any, name: str, yz: Sequence[Tuple[float, float]], outward: float, thickness: float, stone: Any, pigment: Any, collection: Any) -> Any:
    vertices: List[Vec3] = []
    for y, z in yz:
        vertices.append((body_half_width(z) + outward, y, z))
    for y, z in yz:
        vertices.append((body_half_width(z) + outward + thickness, y, z))
    count = len(yz)
    faces: List[List[int]] = [list(reversed(range(count))), list(range(count, count * 2))]
    for index in range(count):
        nxt = (index + 1) % count
        faces.append([index, count + index, count + nxt, nxt])
    obj = create_mesh_object(bpy, name, vertices, faces, collection)
    add_material_slots(obj, stone, pigment)
    return obj


def right_surface_stones(bpy: Any, stone: Any, pigment: Any, collection: Any) -> List[Any]:
    rng = random.Random(120513)
    rows = [(40.0, 76.0), (77.5, 116.0), (117.5, 157.0), (158.5, 194.0), (195.5, 218.5)]
    result: List[Any] = []
    for row_index, (z0, z1) in enumerate(rows):
        zmid = (z0 + z1) * 0.5
        front = -body_half_depth(zmid) + 1.3
        back = 5.0
        middle = (front + back) * 0.5
        for column, (y0, y1) in enumerate(((front, middle - 0.8), (middle + 0.8, back))):
            points = [
                (y0 + rng.uniform(-0.5, 0.5), z0 + rng.uniform(0.3, 1.0)),
                (y1 + rng.uniform(-0.5, 0.5), z0 + rng.uniform(0.3, 1.0)),
                (y1 + rng.uniform(-0.5, 0.5), (z0 + z1) * 0.5 + rng.uniform(-1.4, 1.4)),
                (y1 + rng.uniform(-0.5, 0.5), z1 - rng.uniform(0.3, 1.0)),
                (y0 + rng.uniform(-0.5, 0.5), z1 - rng.uniform(0.3, 1.0)),
                (y0 + rng.uniform(-0.5, 0.5), (z0 + z1) * 0.5 + rng.uniform(-1.4, 1.4)),
            ]
            obj = right_surface_plate(bpy, f"RIGHT_FACE_STONE_{row_index:02d}_{column:02d}", points, 0.32, 0.48, stone, pigment, collection)
            modifier = obj.modifiers.new("ChippedStoneEdge", "BEVEL")
            modifier.width = 0.42
            modifier.segments = 1
            modifier.affect = "EDGES"
            select_only(bpy, [obj])
            bpy.ops.object.modifier_apply(modifier=modifier.name)
            result.append(obj)
    return result


def fissure_relief(bpy: Any, stone: Any, pigment: Any, collection: Any) -> List[Any]:
    paths = [
        ("FISSURE_LEFT_MAJOR", [(-42.0, 42.0), (-35.0, 61.0), (-40.0, 82.0), (-31.0, 105.0), (-35.0, 130.0), (-28.0, 151.0), (-32.0, 176.0), (-27.0, 198.0), (-29.0, 218.0)]),
        ("FISSURE_RIGHT_MAJOR", [(43.0, 42.0), (35.0, 65.0), (39.0, 88.0), (31.0, 111.0), (36.0, 134.0), (29.0, 157.0), (33.0, 181.0), (27.0, 202.0), (29.0, 218.0)]),
        ("FISSURE_LOWER_LEFT_BRANCH", [(-37.0, 70.0), (-52.0, 79.0), (-57.0, 92.0)]),
        ("FISSURE_LEFT_MID_BRANCH", [(-33.0, 122.0), (-48.0, 132.0), (-52.0, 145.0)]),
        ("FISSURE_LEFT_HIGH_BRANCH", [(-30.0, 177.0), (-43.0, 187.0), (-46.0, 200.0)]),
        ("FISSURE_LOWER_RIGHT_BRANCH", [(37.0, 69.0), (51.0, 80.0), (55.0, 93.0)]),
        ("FISSURE_RIGHT_MID_BRANCH", [(33.0, 122.0), (47.0, 132.0), (50.0, 146.0)]),
        ("FISSURE_RIGHT_HIGH_BRANCH", [(31.0, 178.0), (43.0, 188.0), (45.0, 201.0)]),
        ("FISSURE_CROWN_LEFT", [(-4.0, 214.0), (-12.0, 218.0), (-18.0, 220.0)]),
        ("FISSURE_CROWN_RIGHT", [(4.0, 214.0), (12.0, 218.0), (18.0, 220.0)]),
        ("SIDE_RUNE_LEFT", [(-39.0, 96.0), (-34.0, 103.0), (-39.0, 110.0), (-34.0, 117.0), (-39.0, 126.0)]),
        ("SIDE_RUNE_RIGHT", [(39.0, 96.0), (34.0, 103.0), (39.0, 110.0), (34.0, 117.0), (39.0, 126.0)]),
    ]
    return [
        relief_line(bpy, name, points, False, stone, pigment, collection, bevel_depth=0.42, outward=1.15, pigment_only=True)
        for name, points in paths
    ]


def copy_textures() -> Dict[str, Dict[str, Any]]:
    mapping = {
        BC_REL: OLD_TEXTURE_ROOT / "T_GIA_BloodAxeCairnstone_A005_BC.png",
        N_REL: OLD_TEXTURE_ROOT / "T_GIA_BloodAxeCairnstone_A005_N.png",
        ORM_REL: OLD_TEXTURE_ROOT / "T_GIA_BloodAxeCairnstone_A005_ORM.png",
    }
    (ROOT / TEXTURE_ROOT).mkdir(parents=True, exist_ok=True)
    result: Dict[str, Dict[str, Any]] = {}
    for destination_rel, source_rel in mapping.items():
        source = ROOT / source_rel
        destination = ROOT / destination_rel
        shutil.copy2(source, destination)
        correction = "none"
        if destination_rel == BC_REL:
            from PIL import Image, ImageFilter, ImageOps
            from collections import deque

            uv_plan = load_json(UV_PLAN_REL)
            mask_manifest = load_json(MASK_MANIFEST_REL)
            windows = {entry["view"]: entry["rect"] for entry in uv_plan["uv0"]["source_windows_half_open_px"]}
            source_color = Image.open(destination).convert("RGB")
            noise = Image.effect_noise(source_color.size, 25.0).filter(ImageFilter.GaussianBlur(radius=1.1))
            continuation = ImageOps.colorize(noise, black=(28, 27, 26), white=(92, 86, 80))
            owned_atlas = Image.new("L", source_color.size, 0)
            for record in mask_manifest["records"]:
                mask = Image.open(ROOT / record["mask_path"]).convert("L")
                rect = windows[record["view"]]
                expected = (rect[2] - rect[0], rect[3] - rect[1])
                if mask.size != expected:
                    raise RuntimeError(f"{record['view']} source mask/window size mismatch")
                binary_mask = mask.point(lambda value: 255 if value > 0 else 0)
                owned_atlas.paste(binary_mask, (rect[0], rect[1]))
                panel = source_color.crop(tuple(rect))
                values = list(panel.getdata())
                mask_values = list(mask.getdata())
                filled = bytearray(1 if value > 0 else 0 for value in mask_values)
                pending = deque(index for index, value in enumerate(filled) if value)
                width, height = expected
                while pending:
                    index = pending.popleft()
                    x = index % width
                    y = index // width
                    neighbors = []
                    if x > 0:
                        neighbors.append(index - 1)
                    if x + 1 < width:
                        neighbors.append(index + 1)
                    if y > 0:
                        neighbors.append(index - width)
                    if y + 1 < height:
                        neighbors.append(index + width)
                    for neighbor in neighbors:
                        if not filled[neighbor]:
                            values[neighbor] = values[index]
                            filled[neighbor] = 1
                            pending.append(neighbor)
                if not all(filled):
                    raise RuntimeError(f"{record['view']} continuation propagation stalled")
                filled_panel = Image.new("RGB", expected)
                filled_panel.putdata(values)
                continuation.paste(filled_panel, (rect[0], rect[1]))
            preserved = Image.composite(source_color, continuation, owned_atlas)
            preserved.save(destination, format="PNG")
            correction = "source-owned pixels preserved exactly; unowned view padding receives deterministic nearest-boundary stone continuation; authored zone receives deterministic dark stone"
        elif destination_rel == N_REL:
            from PIL import Image

            normal = Image.open(destination).convert("RGB")
            blue = normal.getchannel("B")
            invalid = blue.point(lambda value: 255 if value < 96 else 0)
            invalid_count = sum(1 for value in invalid.getdata() if value)
            normal.paste((128, 128, 255), mask=invalid)
            normal.save(destination, format="PNG")
            correction = f"{invalid_count} unsupported low-Z normal texels replaced by flat tangent normal"
        result[destination_rel.name] = {
            "path": str(destination_rel),
            "sha256": sha256_file(destination),
            "source_path": str(source_rel),
            "source_sha256": sha256_file(source),
            "recovery_correction": correction,
            "recovery_role": "source-owned color/material response preserved; remapped to corrected geometry",
        }
    return result


def create_materials(bpy: Any) -> Tuple[Any, Any]:
    stone = bpy.data.materials.new("M_GIA_BloodAxeCairnstone_A005_VF_A01_Stone")
    stone.use_nodes = True
    stone.use_backface_culling = True
    nodes = stone.node_tree.nodes
    links = stone.node_tree.links
    nodes.clear()
    output = nodes.new("ShaderNodeOutputMaterial")
    shader = nodes.new("ShaderNodeBsdfPrincipled")
    base = nodes.new("ShaderNodeTexImage")
    base.image = bpy.data.images.load(str(ROOT / BC_REL), check_existing=False)
    base.image.colorspace_settings.name = "sRGB"
    normal_image = nodes.new("ShaderNodeTexImage")
    normal_image.image = bpy.data.images.load(str(ROOT / N_REL), check_existing=False)
    try:
        normal_image.image.colorspace_settings.name = "Non-Color"
    except TypeError:
        normal_image.image.colorspace_settings.name = "Linear"
    split_normal = nodes.new("ShaderNodeSeparateRGB")
    invert_green = nodes.new("ShaderNodeMath")
    invert_green.operation = "SUBTRACT"
    invert_green.inputs[0].default_value = 1.0
    combine_normal = nodes.new("ShaderNodeCombineRGB")
    normal_map = nodes.new("ShaderNodeNormalMap")
    normal_map.inputs["Strength"].default_value = 1.25
    orm = nodes.new("ShaderNodeTexImage")
    orm.image = bpy.data.images.load(str(ROOT / ORM_REL), check_existing=False)
    try:
        orm.image.colorspace_settings.name = "Non-Color"
    except TypeError:
        orm.image.colorspace_settings.name = "Linear"
    separate = nodes.new("ShaderNodeSeparateRGB")
    coordinates = nodes.new("ShaderNodeTexCoord")
    noise = nodes.new("ShaderNodeTexNoise")
    noise.inputs["Scale"].default_value = 6.5
    noise.inputs["Detail"].default_value = 4.0
    noise.inputs["Roughness"].default_value = 0.72
    fallback_ramp = nodes.new("ShaderNodeValToRGB")
    fallback_ramp.color_ramp.elements[0].position = 0.22
    fallback_ramp.color_ramp.elements[0].color = (0.150, 0.138, 0.126, 1.0)
    fallback_ramp.color_ramp.elements[1].position = 0.80
    fallback_ramp.color_ramp.elements[1].color = (0.390, 0.355, 0.320, 1.0)
    base_luminance = nodes.new("ShaderNodeRGBToBW")
    source_valid = nodes.new("ShaderNodeMath")
    source_valid.operation = "GREATER_THAN"
    source_valid.inputs[1].default_value = 0.003
    source_gamma = nodes.new("ShaderNodeGamma")
    source_gamma.inputs["Gamma"].default_value = 0.58
    source_or_fallback = nodes.new("ShaderNodeMixRGB")
    source_or_fallback.blend_type = "MIX"
    links.new(coordinates.outputs["Generated"], noise.inputs["Vector"])
    links.new(noise.outputs["Fac"], fallback_ramp.inputs["Fac"])
    links.new(base.outputs["Color"], base_luminance.inputs["Color"])
    links.new(base_luminance.outputs["Val"], source_valid.inputs[0])
    links.new(base.outputs["Color"], source_gamma.inputs["Color"])
    links.new(source_valid.outputs[0], source_or_fallback.inputs[0])
    links.new(fallback_ramp.outputs["Color"], source_or_fallback.inputs[1])
    links.new(source_gamma.outputs["Color"], source_or_fallback.inputs[2])
    links.new(source_or_fallback.outputs["Color"], shader.inputs["Base Color"])
    links.new(normal_image.outputs["Color"], split_normal.inputs["Image"])
    links.new(split_normal.outputs["R"], combine_normal.inputs["R"])
    links.new(split_normal.outputs["G"], invert_green.inputs[1])
    links.new(invert_green.outputs[0], combine_normal.inputs["G"])
    links.new(split_normal.outputs["B"], combine_normal.inputs["B"])
    links.new(combine_normal.outputs["Image"], normal_map.inputs["Color"])
    bump = nodes.new("ShaderNodeBump")
    bump.inputs["Strength"].default_value = 0.24
    bump.inputs["Distance"].default_value = 0.16
    links.new(noise.outputs["Fac"], bump.inputs["Height"])
    links.new(normal_map.outputs["Normal"], bump.inputs["Normal"])
    links.new(bump.outputs["Normal"], shader.inputs["Normal"])
    links.new(orm.outputs["Color"], separate.inputs["Image"])
    links.new(separate.outputs["G"], shader.inputs["Roughness"])
    links.new(separate.outputs["B"], shader.inputs["Metallic"])
    shader.inputs["Specular"].default_value = 0.32
    links.new(shader.outputs["BSDF"], output.inputs["Surface"])
    stone["aerathea_map_set"] = "BaseColor/DirectXNormal/ORM"
    stone["aerathea_emissive"] = False

    pigment = bpy.data.materials.new("M_GIA_BloodAxeCairnstone_A005_VF_A01_BloodPigment")
    pigment.use_nodes = True
    pigment.use_backface_culling = True
    pnodes = pigment.node_tree.nodes
    plinks = pigment.node_tree.links
    pshader = pnodes.get("Principled BSDF")
    pcoords = pnodes.new("ShaderNodeTexCoord")
    pnoise = pnodes.new("ShaderNodeTexNoise")
    pnoise.inputs["Scale"].default_value = 5.0
    pnoise.inputs["Detail"].default_value = 3.0
    pnoise.inputs["Roughness"].default_value = 0.72
    pramp = pnodes.new("ShaderNodeValToRGB")
    pramp.color_ramp.elements[0].position = 0.22
    pramp.color_ramp.elements[0].color = (0.055, 0.0015, 0.0006, 1.0)
    pramp.color_ramp.elements[1].position = 0.82
    pramp.color_ramp.elements[1].color = (0.34, 0.010, 0.003, 1.0)
    pbump = pnodes.new("ShaderNodeBump")
    pbump.inputs["Strength"].default_value = 0.22
    pbump.inputs["Distance"].default_value = 0.08
    plinks.new(pcoords.outputs["Generated"], pnoise.inputs["Vector"])
    plinks.new(pnoise.outputs["Fac"], pramp.inputs["Fac"])
    plinks.new(pramp.outputs["Color"], pshader.inputs["Base Color"])
    plinks.new(pnoise.outputs["Fac"], pbump.inputs["Height"])
    plinks.new(pbump.outputs["Normal"], pshader.inputs["Normal"])
    pshader.inputs["Roughness"].default_value = 0.56
    pshader.inputs["Metallic"].default_value = 0.0
    pshader.inputs["Specular"].default_value = 0.38
    pshader.inputs["Emission"].default_value = (0.035, 0.0005, 0.0002, 1.0)
    pshader.inputs["Emission Strength"].default_value = 0.18
    pigment["aerathea_role"] = "restrained Blood Axe fissure and shallow relief accent"
    return stone, pigment


def join_geometry(bpy: Any, objects: Sequence[Any], name: str, stone: Any, pigment: Any = None) -> Any:
    select_only(bpy, list(objects))
    bpy.context.view_layer.objects.active = objects[0]
    bpy.ops.object.join()
    result = bpy.context.object
    result.name = name
    result.data.materials.clear()
    result.data.materials.append(stone)
    if pigment is None:
        for polygon in result.data.polygons:
            polygon.material_index = 0
    else:
        result.data.materials.append(pigment)
    return result


def densify_profiles(profiles: Sequence[Tuple[float, float, float, float]]) -> List[Tuple[float, float, float, float]]:
    result: List[Tuple[float, float, float, float]] = []
    for first, second in zip(profiles, profiles[1:]):
        result.append(first)
        result.append(tuple((first[index] + second[index]) * 0.5 for index in range(4)))
    result.append(profiles[-1])
    return result


def normalize_bounds(obj: Any) -> None:
    current = object_bounds(obj)
    for vertex in obj.data.vertices:
        for axis, target in enumerate(TARGET_BOUNDS):
            old_min = current["min"][axis]
            old_span = current["dimensions"][axis]
            if old_span <= 1.0e-12:
                raise RuntimeError("zero-span recovery geometry")
            vertex.co[axis] = (float(vertex.co[axis]) - old_min) * target / old_span
            if axis in (0, 1):
                vertex.co[axis] -= target * 0.5
    obj.data.update()


def face_owner(normal: Vec3, center: Vec3) -> str:
    nx, ny, nz = normal
    if nz > 0.55:
        return "top"
    if nz < -0.55:
        return "authored"
    x, y, _ = center
    normalized_x = abs(x) / 70.0
    normalized_y = abs(y) / 55.0
    if normalized_x >= normalized_y:
        return "right" if x >= 0.0 else "left"
    return "back" if y >= 0.0 else "front"


def target_half_width_at_z(z: float) -> float:
    if z <= 10.5:
        return 70.0
    if z <= 23.5:
        alpha = (z - 10.5) / 13.0
        return 58.0 + alpha * (53.0 - 58.0)
    if z <= 36.0:
        alpha = (z - 23.5) / 12.5
        return 54.0 + alpha * (50.0 - 54.0)
    return body_half_width(z)


def target_half_depth_at_z(z: float) -> float:
    if z <= 10.5:
        return 55.0
    if z <= 23.5:
        alpha = (z - 10.5) / 13.0
        return 46.0 + alpha * (41.0 - 46.0)
    if z <= 36.0:
        alpha = (z - 23.5) / 12.5
        return 42.0 + alpha * (38.0 - 42.0)
    return body_half_depth(z)


def project_point(point: Vec3, view: str, bbox: Sequence[int], row_spans: Sequence[Tuple[int, int]]) -> Vec2:
    xmin, ymin, xmax, ymax = bbox
    width = max(1.0, float(xmax - xmin))
    height = max(1.0, float(ymax - ymin))
    x, y, z = point
    if view == "front":
        horizontal, half_extent = x, target_half_width_at_z(z)
    elif view == "back":
        horizontal, half_extent = -x, target_half_width_at_z(z)
    elif view == "left":
        horizontal, half_extent = -y, target_half_depth_at_z(z)
    elif view == "right":
        horizontal, half_extent = y, target_half_depth_at_z(z)
    elif view == "top":
        return (xmin + ((x + 70.0) / 140.0) * width, ymin + ((55.0 - y) / 110.0) * height)
    else:
        raise RuntimeError(view)
    panel_y = ymax - (z / 220.0) * height
    row = max(0, min(len(row_spans) - 1, int(round(panel_y))))
    span_min, span_max = row_spans[row]
    normalized = max(0.0, min(1.0, (horizontal + half_extent) / max(2.0 * half_extent, 1.0e-9)))
    span_width = span_max - span_min
    inset = max(2, int(round(span_width * 0.075))) if span_width >= 8 else 0
    inset_min = float(span_min + inset)
    inset_max = float(span_max - inset)
    return (inset_min + normalized * (inset_max - inset_min), panel_y)


def polygon_normal(mesh: Any, polygon: Any) -> Vec3:
    value = polygon.normal
    return (float(value.x), float(value.y), float(value.z))


def assign_source_uv(obj: Any) -> Dict[str, int]:
    from PIL import Image

    uv_plan = load_json(UV_PLAN_REL)
    mask_manifest = load_json(MASK_MANIFEST_REL)
    windows = {entry["view"]: entry["rect"] for entry in uv_plan["uv0"]["source_windows_half_open_px"]}
    bboxes = {entry["view"]: entry["central_object_bbox_inclusive_px"] for entry in mask_manifest["records"]}
    row_span_map: Dict[str, List[Tuple[int, int]]] = {}
    for record in mask_manifest["records"]:
        mask = Image.open(ROOT / record["mask_path"]).convert("L")
        pixels = mask.load()
        spans: List[Any] = []
        for row in range(mask.height):
            owned = [column for column in range(mask.width) if pixels[column, row] > 0]
            spans.append((min(owned), max(owned)) if owned else None)
        populated = [index for index, span in enumerate(spans) if span is not None]
        if not populated:
            raise RuntimeError(f"{record['view']} source owner mask is empty")
        for row, span in enumerate(spans):
            if span is None:
                nearest = min(populated, key=lambda candidate: abs(candidate - row))
                spans[row] = spans[nearest]
        row_span_map[record["view"]] = spans
    mesh = obj.data
    while mesh.uv_layers:
        mesh.uv_layers.remove(mesh.uv_layers[0])
    layer = mesh.uv_layers.new(name="UVMap")
    counts: Dict[str, int] = {view: 0 for view in ("front", "back", "left", "right", "top", "authored")}
    for polygon in mesh.polygons:
        coordinates = [mesh.vertices[index].co for index in polygon.vertices]
        center = tuple(sum(float(point[axis]) for point in coordinates) / len(coordinates) for axis in range(3))
        owner = face_owner(polygon_normal(mesh, polygon), center)
        counts[owner] += 1
        for loop_index in polygon.loop_indices:
            vertex = mesh.vertices[mesh.loops[loop_index].vertex_index].co
            point = (float(vertex.x), float(vertex.y), float(vertex.z))
            if owner == "authored":
                pixel = (1840.0 + (point[0] % 18.0), 1840.0 + (point[1] % 18.0))
            else:
                panel = project_point(point, owner, bboxes[owner], row_span_map[owner])
                rect = windows[owner]
                pixel = (rect[0] + panel[0], rect[1] + panel[1])
            layer.data[loop_index].uv = (pixel[0] / 2048.0, 1.0 - pixel[1] / 2048.0)
    return counts


def assign_lightmap_uv(bpy: Any, obj: Any) -> None:
    mesh = obj.data
    old = mesh.uv_layers.get("LightmapUV")
    if old is not None:
        mesh.uv_layers.remove(old)
    layer = mesh.uv_layers.new(name="LightmapUV")
    mesh.uv_layers.active = layer
    select_only(bpy, [obj])
    bpy.ops.object.mode_set(mode="EDIT")
    bpy.ops.mesh.select_all(action="SELECT")
    bpy.ops.uv.smart_project(island_margin=0.03)
    bpy.ops.object.mode_set(mode="OBJECT")
    mesh.uv_layers.active = mesh.uv_layers.get("UVMap")


def decimate_lod(bpy: Any, source: Any, name: str, ratio: float) -> Any:
    duplicate = source.copy()
    duplicate.data = source.data.copy()
    duplicate.name = name
    bpy.context.scene.collection.objects.link(duplicate)
    if ratio < 1.0:
        target = object_bounds(source)
        modifier = duplicate.modifiers.new("SilhouetteFirstReduction", "DECIMATE")
        modifier.decimate_type = "COLLAPSE"
        modifier.ratio = ratio
        modifier.use_collapse_triangulate = True
        select_only(bpy, [duplicate])
        bpy.ops.object.modifier_apply(modifier=modifier.name)
        current = object_bounds(duplicate)
        for vertex in duplicate.data.vertices:
            for axis in range(3):
                old_min = current["min"][axis]
                old_span = current["dimensions"][axis]
                new_min = target["min"][axis]
                new_span = target["dimensions"][axis]
                if old_span > 1.0e-12:
                    vertex.co[axis] = new_min + (float(vertex.co[axis]) - old_min) * new_span / old_span
        duplicate.data.update()
    assign_lightmap_uv(bpy, duplicate)
    duplicate["aerathea_lod"] = name.rsplit("_", 1)[-1]
    return duplicate


def box_proxy(bpy: Any, name: str, minimum: Vec3, maximum: Vec3) -> Any:
    xmin, ymin, zmin = minimum
    xmax, ymax, zmax = maximum
    vertices = [
        (xmin, ymin, zmin), (xmax, ymin, zmin), (xmax, ymax, zmin), (xmin, ymax, zmin),
        (xmin, ymin, zmax), (xmax, ymin, zmax), (xmax, ymax, zmax), (xmin, ymax, zmax),
    ]
    faces = [[3, 2, 1, 0], [4, 5, 6, 7], [0, 1, 5, 4], [1, 2, 6, 5], [2, 3, 7, 6], [3, 0, 4, 7]]
    obj = create_mesh_object(bpy, name, vertices, faces, bpy.context.scene.collection)
    obj.display_type = "WIRE"
    obj.hide_render = True
    obj["aerathea_collision_interpretation"] = True
    return obj


def collision_set(bpy: Any) -> List[Any]:
    return [
        box_proxy(bpy, f"UCX_{ASSET}_00", (-60.0, -45.0, 34.0), (60.0, 45.0, 220.0)),
        box_proxy(bpy, f"UCX_{ASSET}_01", (-53.0, -41.0, 22.0), (53.0, 41.0, 36.0)),
        box_proxy(bpy, f"UCX_{ASSET}_02", (-58.0, -46.0, 9.0), (58.0, 46.0, 24.0)),
        box_proxy(bpy, f"UCX_{ASSET}_03", (-70.0, -55.0, 0.0), (70.0, 55.0, 11.0)),
    ]


def export_fbx(bpy: Any, obj: Any, collisions: Sequence[Any], rel: Path) -> Dict[str, Any]:
    path = ROOT / rel
    path.parent.mkdir(parents=True, exist_ok=True)
    selected = [obj, *collisions]
    original = obj.name
    original_hide_viewport = obj.hide_viewport
    obj.hide_viewport = False
    if collisions:
        obj.name = ASSET
    select_only(bpy, selected)
    bpy.ops.export_scene.fbx(
        filepath=str(path),
        use_selection=True,
        object_types={"MESH"},
        apply_unit_scale=True,
        apply_scale_options="FBX_SCALE_UNITS",
        axis_forward="-Z",
        axis_up="Y",
        use_mesh_modifiers=True,
        use_mesh_edges=False,
        mesh_smooth_type="FACE",
        use_tspace=True,
        use_custom_props=True,
        add_leaf_bones=False,
        bake_anim=False,
        path_mode="STRIP",
        embed_textures=False,
    )
    obj.name = original
    obj.hide_viewport = original_hide_viewport
    return {"path": str(rel), "sha256": sha256_file(path), "bytes": path.stat().st_size}


def build() -> Dict[str, Any]:
    plan = load_json(PLAN_REL)
    source_path = ROOT / SOURCE_REL
    if sha256_file(source_path) != plan["source_authority"]["sha256"]:
        raise RuntimeError("authoritative source hash mismatch")

    import bpy  # type: ignore

    bpy.ops.wm.read_factory_settings(use_empty=True)
    scene = bpy.context.scene
    scene.unit_settings.system = "METRIC"
    scene.unit_settings.scale_length = 0.01
    scene.unit_settings.length_unit = "CENTIMETERS"
    scene.render.engine = "BLENDER_EEVEE"
    scene["aerathea_asset_id"] = ASSET
    scene["aerathea_contract_id"] = CONTRACT
    scene["aerathea_pipeline_status"] = "DCC game-ready candidate pending recovery audit"
    scene["aerathea_fully_game_ready"] = False
    scene["aerathea_unreal_work_performed"] = False

    texture_records = copy_textures()
    stone, pigment = create_materials(bpy)
    detail_collection = bpy.data.collections.new("A005_VISUAL_FIDELITY_BUILD_PARTS")
    scene.collection.children.link(detail_collection)
    parts: List[Any] = []

    body_profiles = [
        (34.0, 96.0, 72.0, 0.0), (35.0, 100.0, 76.0, 0.45), (44.0, 116.0, 86.0, 0.9),
        (55.0, 120.0, 90.0, 1.2), (66.0, 118.0, 88.0, 1.0), (78.0, 113.0, 84.0, 1.1),
        (91.0, 108.0, 80.0, 1.0), (105.0, 102.0, 76.0, 1.15), (120.0, 96.0, 71.0, 0.9),
        (135.0, 90.0, 66.0, 1.1), (150.0, 84.0, 61.0, 0.95), (165.0, 78.0, 57.0, 0.9),
        (180.0, 73.0, 53.0, 0.8), (194.0, 69.0, 50.0, 0.75), (206.0, 66.0, 48.0, 0.6),
        (216.0, 65.0, 47.0, 0.45), (220.0, 64.0, 46.0, 0.0),
    ]
    body = loft(bpy, "MONOLITH_BODY", densify_profiles(body_profiles), 112, 3.8, detail_collection)
    body.data.materials.append(stone)
    parts.append(body)

    apron = loft(
        bpy,
        "APRON_CORE",
        [(0.0, 140.0, 110.0, 0.0), (3.0, 138.0, 108.0, 0.8), (7.5, 126.0, 98.0, 1.1), (10.5, 116.0, 90.0, 0.5)],
        64,
        3.0,
        detail_collection,
    )
    apron.data.materials.append(stone)
    parts.append(apron)
    lower_core = loft(bpy, "LOWER_COURSE_CORE", [(9.0, 114.0, 90.0, 0.0), (12.0, 116.0, 92.0, 0.35), (22.0, 108.0, 84.0, 0.45), (24.0, 106.0, 82.0, 0.0)], 48, 3.5, detail_collection)
    upper_core = loft(bpy, "UPPER_COURSE_CORE", [(22.0, 106.0, 82.0, 0.0), (24.0, 108.0, 84.0, 0.35), (34.0, 102.0, 78.0, 0.35), (36.0, 100.0, 76.0, 0.0)], 48, 3.5, detail_collection)
    for core in (lower_core, upper_core):
        core.data.materials.append(stone)
        parts.append(core)

    lod0 = join_geometry(bpy, parts, f"{ASSET}_LOD0", stone)
    bpy.data.materials.remove(pigment, do_unlink=True)
    normalize_bounds(lod0)
    triangulate = lod0.modifiers.new("DeterministicExportTriangulation", "TRIANGULATE")
    triangulate.quad_method = "BEAUTY"
    triangulate.ngon_method = "BEAUTY"
    select_only(bpy, [lod0])
    bpy.ops.object.modifier_apply(modifier=triangulate.name)
    lod0.data.update(calc_edges=True)
    uv_owner_counts = assign_source_uv(lod0)
    assign_lightmap_uv(bpy, lod0)
    lod0["aerathea_lod"] = "LOD0"
    lod0["aerathea_macro_features"] = json.dumps(REQUIRED_FEATURES)
    lod0["aerathea_primary_shells"] = 4
    lod0["aerathea_decoration_geometry"] = 0
    lod0["aerathea_decoration_consumers"] = json.dumps(["C-005", "C-006", "C-007"])
    lod0["aerathea_source_authority_sha256"] = plan["source_authority"]["sha256"]
    lod0["aerathea_artifact_classification"] = "candidate"

    lods: Dict[str, Any] = {"LOD0": lod0}
    for lod_name, ratio in LOD_RATIOS.items():
        if lod_name == "LOD0":
            continue
        lods[lod_name] = decimate_lod(bpy, lod0, f"{ASSET}_{lod_name}", ratio)
    collisions = collision_set(bpy)

    for name, obj in lods.items():
        obj.hide_render = name != "LOD0"
        obj.hide_viewport = name != "LOD0"
    for proxy in collisions:
        proxy.hide_render = True

    lod_records: Dict[str, Any] = {}
    for name, obj in lods.items():
        bounds = object_bounds(obj)
        lod_records[name] = {
            "object": obj.name,
            "vertices": len(obj.data.vertices),
            "polygons": len(obj.data.polygons),
            "triangles": mesh_triangles(obj.data),
            "bounds_cm": {key: [round(value, 6) for value in values] for key, values in bounds.items()},
            "uv_layers": [layer.name for layer in obj.data.uv_layers],
            "material_slots": len(obj.data.materials),
            "ratio_requested": LOD_RATIOS[name],
        }
    if not 4000 <= lod_records["LOD0"]["triangles"] <= 10000:
        raise RuntimeError(f"LOD0 triangle gate failed: {lod_records['LOD0']['triangles']}")
    if not all(lod_records[first]["triangles"] > lod_records[second]["triangles"] for first, second in zip(("LOD0", "LOD1", "LOD2"), ("LOD1", "LOD2", "LOD3"))):
        raise RuntimeError("LOD triangles are not strictly monotonic")

    blend_path = ROOT / BLEND_REL
    blend_path.parent.mkdir(parents=True, exist_ok=True)
    bpy.ops.wm.save_as_mainfile(filepath=str(blend_path), check_existing=False)
    exports = {
        name: export_fbx(bpy, obj, collisions if name == "LOD0" else [], FBX_RELS[name])
        for name, obj in lods.items()
    }
    select_only(bpy, [lod0])

    manifest = {
        "schema": "aerathea.a005_visual_fidelity_recovery_candidate.v1",
        "asset_id": ASSET,
        "contract_id": CONTRACT,
        "date": "2026-07-20",
        "status": "candidate_pending_independent_visual_fidelity_recovery_audit",
        "artifact_classification": "candidate",
        "pipeline_status": "DCC game-ready candidate pending recovery audit",
        "source_authority": {"path": str(SOURCE_REL), "sha256": sha256_file(source_path), "modified": False},
        "first_divergence_repaired": "STEP_12_under_resolved_784_triangle_blockout",
        "rebuild_from_historical_a005_geometry": False,
        "legacy_a001_a004_geometry_used": False,
        "dimensions_cm": {"target": list(TARGET_BOUNDS), "actual": lod_records["LOD0"]["bounds_cm"]["dimensions"], "pivot": [0, 0, 0]},
        "macro_features": {
            "required": list(REQUIRED_FEATURES),
            "present": list(REQUIRED_FEATURES),
            "primary_shells": 4,
            "C005_C006_C007_geometry": 0,
            "decoration_implementation": "source-owned BaseColor and Normal consumers per Step 11 and Step 14",
        },
        "lods": lod_records,
        "collision": {"count": len(collisions), "names": [obj.name for obj in collisions], "strategy": "four custom source-containing convex boxes"},
        "materials": {"count": 1, "names": [stone.name], "emissive": "none; source red is BaseColor/Normal-owned"},
        "textures": texture_records,
        "uv0_owner_face_counts": uv_owner_counts,
        "exports": exports,
        "blend": {"path": str(BLEND_REL), "sha256": sha256_file(blend_path)},
        "unreal_outputs": 0,
        "fully_game_ready": False,
        "visual_canon": False,
    }
    manifest_path = ROOT / MANIFEST_REL
    manifest_path.write_text(json.dumps(manifest, indent=2) + "\n", encoding="utf-8")
    return manifest


def main() -> int:
    args = parse_args(blender_args())
    if args.schema_only:
        report = schema_report()
        if report["bpy_imported"]:
            raise RuntimeError("schema-only path imported bpy")
    else:
        report = build()
    print(json.dumps(report, indent=2))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
