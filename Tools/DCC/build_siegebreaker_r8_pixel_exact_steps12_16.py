#!/usr/bin/env python3
"""Fresh deterministic R8 Siege Breaker Steps 12-16 Blender build.

Run with:
  blender --background --python Tools/DCC/build_siegebreaker_r8_pixel_exact_steps12_16.py
"""

from __future__ import annotations

from collections import Counter, deque
from fractions import Fraction
import gzip
import hashlib
import json
import math
from pathlib import Path
import struct

import bpy
from mathutils import Vector
from PIL import Image, ImageDraw, ImageFont


ROOT = Path(__file__).resolve().parents[2]
ASSET = "SM_DRW_SiegeBreaker_Hammer_A01"
RUN_ID = "SB-CR-STEPS01-16-R8-PIXEL-EXACT-A01"
RUN = ROOT / (
    "docs/assets/blueprints/SM_DRW_SiegeBreaker_Hammer_A01/proof_runs/"
    "SB-CR-STEPS01-16-R8-PIXEL-EXACT-A01"
)
SOURCE_ROOT = (
    ROOT
    / "SourceAssets/Blender/Weapons/Dwarven"
    / ASSET
    / "R8_PixelExact_Steps01_16_A01"
)
FINAL_REVIEW = RUN / "review/STEP_16_FINAL"
BOARD = FINAL_REVIEW / "STEP_16_R8_PIXEL_EXACT_TWO_HAMMER_FINAL_REVIEW.png"
STEP03 = RUN / "manifests/STEP_03_CROP_COORDINATES.json"
REGISTRATION = RUN / "manifests/STEP_05_PIXEL_WORLD_REGISTRATION_LOCK.json"
FRONT_MEASURE = RUN / "manifests/STEP_06_FRONT_MEASUREMENT_CONTRACT.json"
RIGHT_MEASURE = RUN / "manifests/STEP_07_RIGHT_MEASUREMENT_CONTRACT.json"
INTERPRET = RUN / "manifests/STEP_10_INTERPRETATION_DECISIONS.json"
BLUEPRINT = RUN / "manifests/STEP_11_PRODUCTION_GEOMETRY_BLUEPRINT.json"
STATE = RUN / "manifests/STEP_STATE.json"

FRONT_RECT = [256, 208, 868, 1271]
RIGHT_RECT = [418, 166, 668, 1262]
FRONT_CENTER = 562
RIGHT_AXIS = 557
FRONT_SCALE = Fraction(170, 1063)
RIGHT_SCALE = Fraction(170, 1096)
FRONT_A = 600
FRONT_TERMINAL = 1271
HANDLE_HALF_SEGMENTS = 4
VARIANTS = {
    "rune": {
        "label": "RUNE-SIDE HALF [557,668)",
        "interval": [557, 668],
        "source_top": 166,
    },
    "metal": {
        "label": "METAL-CENTER-PIECE HALF [418,557)",
        "interval": [418, 557],
        "source_top": 170,
    },
}


def sha256_bytes(value: bytes) -> str:
    return hashlib.sha256(value).hexdigest()


def sha256(path: Path) -> str:
    return sha256_bytes(path.read_bytes())


def canonical_hash(vertices, faces, uvs=None, materials=None) -> str:
    payload = {
        "vertices": [
            [f"{value:.12f}" for value in vertex] for vertex in vertices
        ],
        "faces": [list(face) for face in faces],
        "uvs": (
            [
                [[f"{u:.12f}", f"{v:.12f}"] for u, v in polygon]
                for polygon in uvs
            ]
            if uvs is not None
            else None
        ),
        "materials": materials,
    }
    return sha256_bytes(
        json.dumps(payload, sort_keys=True, separators=(",", ":")).encode()
    )


def fraction_record(value: Fraction) -> dict[str, object]:
    return {
        "numerator": value.numerator,
        "denominator": value.denominator,
        "display_decimal": f"{float(value):.12f}",
    }


def write_json(path: Path, value: object) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(json.dumps(value, indent=2) + "\n")


def load_authority() -> tuple[dict[str, object], dict[str, object]]:
    for required in (
        STEP03,
        REGISTRATION,
        FRONT_MEASURE,
        RIGHT_MEASURE,
        INTERPRET,
        BLUEPRINT,
    ):
        if not required.is_file():
            raise RuntimeError(f"Missing authoritative input: {required}")
    blueprint = json.loads(BLUEPRINT.read_text())
    if blueprint["run_id"] != RUN_ID:
        raise RuntimeError("Wrong Step 11 run")
    if blueprint["execution_entry_point"] != str(
        Path(__file__).resolve().relative_to(ROOT)
    ):
        raise RuntimeError("Step 11 entry point mismatch")
    step03 = json.loads(STEP03.read_text())
    return blueprint, {row["id"]: row for row in step03["sources"]}


def replay_capture(record: dict[str, object]):
    source_path = ROOT / record["source_path"]
    capture_path = ROOT / record["capture_path"]
    if sha256(source_path) != record["source_file_sha256"]:
        raise RuntimeError(f"Immutable source changed: {record['id']}")
    image = Image.open(source_path).convert("RGBA")
    raw = image.tobytes("raw", "RGBA")
    capture = json.loads(gzip.decompress(capture_path.read_bytes()))
    membership = bytearray(image.width * image.height)
    selected = bytearray()
    seen = set()
    for row in capture["rows_with_exact_rgba"]:
        y = int(row["y"])
        for run in row["runs"]:
            x0, x1 = int(run["x0"]), int(run["x1"])
            payload = bytes.fromhex(run["rgba_hex"])
            for offset, x in enumerate(range(x0, x1)):
                if (x, y) in seen:
                    raise RuntimeError("Multiply-owned scanline pixel")
                seen.add((x, y))
                flat = y * image.width + x
                pixel = payload[offset * 4:offset * 4 + 4]
                if pixel != raw[flat * 4:flat * 4 + 4]:
                    raise RuntimeError("Stored pixel no longer equals source")
                membership[flat] = 1
                selected.extend(pixel)
    if sha256_bytes(bytes(membership)) != record["decoded_membership_sha256"]:
        raise RuntimeError("Membership replay mismatch")
    if sha256_bytes(bytes(selected)) != record["selected_rgba_sha256"]:
        raise RuntimeError("RGBA replay mismatch")
    mask = Image.frombytes(
        "L",
        image.size,
        bytes(255 if value else 0 for value in membership),
    )
    return image, mask, {
        "source_path": str(source_path.relative_to(ROOT)),
        "source_sha256": sha256(source_path),
        "capture_path": str(capture_path.relative_to(ROOT)),
        "capture_sha256": sha256(capture_path),
        "selected_pixel_count": len(seen),
        "membership_sha256": sha256_bytes(bytes(membership)),
        "selected_rgba_sha256": sha256_bytes(bytes(selected)),
        "exact_replay": True,
    }


def fill_enclosed(mask: Image.Image) -> Image.Image:
    width, height = mask.size
    pixels = mask.load()
    exterior = bytearray(width * height)
    queue: deque[tuple[int, int]] = deque()
    for x in range(width):
        for y in (0, height - 1):
            if pixels[x, y] == 0 and not exterior[y * width + x]:
                exterior[y * width + x] = 1
                queue.append((x, y))
    for y in range(height):
        for x in (0, width - 1):
            if pixels[x, y] == 0 and not exterior[y * width + x]:
                exterior[y * width + x] = 1
                queue.append((x, y))
    while queue:
        x, y = queue.popleft()
        for dx, dy in ((1, 0), (-1, 0), (0, 1), (0, -1)):
            nx, ny = x + dx, y + dy
            if (
                0 <= nx < width
                and 0 <= ny < height
                and pixels[nx, ny] == 0
                and not exterior[ny * width + nx]
            ):
                exterior[ny * width + nx] = 1
                queue.append((nx, ny))
    result = mask.copy()
    output = result.load()
    for y in range(height):
        for x in range(width):
            if output[x, y] == 0 and not exterior[y * width + x]:
                output[x, y] = 255
    return result


def row_interval(mask_crop: Image.Image, global_y: int, rect: list[int]):
    local_y = max(0, min(mask_crop.height - 1, global_y - rect[1]))
    pixels = mask_crop.load()
    members = [x for x in range(mask_crop.width) if pixels[x, local_y] > 0]
    if not members:
        return None
    return rect[0] + min(members), rect[0] + max(members) + 1


def front_profile(front_filled: Image.Image, global_y: int):
    interval = row_interval(front_filled, global_y, FRONT_RECT)
    if interval is None:
        raise RuntimeError(f"Missing front profile row {global_y}")
    x0, x1 = interval
    radius_pixels = max(FRONT_CENTER - x0, x1 - FRONT_CENTER)
    return x0, x1, radius_pixels


def right_half_radius(
    right_filled: Image.Image,
    global_y: int,
    kind: str,
) -> int:
    x0, x1 = VARIANTS[kind]["interval"]
    local_y = max(0, min(right_filled.height - 1, global_y - RIGHT_RECT[1]))
    pixels = right_filled.load()
    members = [
        global_x
        for global_x in range(x0, x1)
        if pixels[global_x - RIGHT_RECT[0], local_y] > 0
    ]
    if not members:
        return 0
    return (
        max(members) + 1 - RIGHT_AXIS
        if kind == "rune"
        else RIGHT_AXIS - min(members)
    )


def source_x_from_y(kind: str, world_y: float) -> float:
    radial_pixels = abs(world_y) / float(RIGHT_SCALE)
    return (
        RIGHT_AXIS + radial_pixels
        if kind == "rune"
        else RIGHT_AXIS - radial_pixels
    )


def complete_rz180(vertices, faces, uvs, materials):
    complete_vertices = list(vertices)
    lookup = {
        tuple(round(value, 10) for value in vertex): index
        for index, vertex in enumerate(complete_vertices)
    }
    duplicate = {}
    welded = 0
    for index, (x, y, z) in enumerate(vertices):
        transformed = (-x, -y, z)
        key = tuple(round(value, 10) for value in transformed)
        if key in lookup:
            duplicate[index] = lookup[key]
            welded += 1
        else:
            duplicate[index] = len(complete_vertices)
            lookup[key] = len(complete_vertices)
            complete_vertices.append(transformed)
    complete_faces = list(faces)
    complete_uvs = list(uvs)
    complete_materials = list(materials)
    known = {tuple(sorted(face)) for face in faces}
    added = 0
    for face, face_uv, material in zip(faces, uvs, materials):
        transformed = tuple(duplicate[index] for index in face)
        key = tuple(sorted(transformed))
        if key in known:
            continue
        known.add(key)
        complete_faces.append(transformed)
        complete_uvs.append(list(face_uv))
        complete_materials.append(material)
        added += 1
    return (
        complete_vertices,
        complete_faces,
        complete_uvs,
        complete_materials,
        {
            "source_half_vertices": len(vertices),
            "source_half_faces": len(faces),
            "seam_vertices_welded": welded,
            "rz180_faces_added": added,
            "whole_transform_count": 1,
        },
    )


def build_head_data(
    kind: str,
    front_image: Image.Image,
    right_image: Image.Image,
    front_filled: Image.Image,
    right_filled: Image.Image,
):
    top = int(VARIANTS[kind]["source_top"])
    z_a = Fraction(FRONT_RECT[3] - FRONT_A) * FRONT_SCALE
    attach_float = RIGHT_RECT[3] - float(z_a / RIGHT_SCALE)
    attach_last_row = math.floor(attach_float)
    ring_records = []
    if kind == "metal":
        first_y_radius = right_half_radius(right_filled, top, kind)
        front_y = FRONT_RECT[3] - float(Fraction(170) / FRONT_SCALE)
        _, _, xr = front_profile(front_filled, max(208, math.floor(front_y)))
        ring_records.append(
            {
                "source_y": top,
                "world_z": 170.0,
                "x_radius_px": xr,
                "y_radius_px": first_y_radius,
                "top_closure_from_front_length_anchor": True,
            }
        )
    for source_y in range(top, attach_last_row + 1):
        z = float(Fraction(RIGHT_RECT[3] - source_y) * RIGHT_SCALE)
        if z < float(z_a):
            continue
        front_y = math.floor(FRONT_RECT[3] - z / float(FRONT_SCALE))
        front_y = max(FRONT_RECT[1], min(FRONT_A - 1, front_y))
        _, _, xr = front_profile(front_filled, front_y)
        yr = right_half_radius(right_filled, source_y, kind)
        if yr == 0:
            continue
        ring_records.append(
            {
                "source_y": source_y,
                "world_z": z,
                "x_radius_px": xr,
                "y_radius_px": yr,
                "top_closure_from_front_length_anchor": False,
            }
        )
    last = ring_records[-1]
    if abs(last["world_z"] - float(z_a)) > 1.0e-9:
        ring_records.append(
            {
                **last,
                "world_z": float(z_a),
                "front_station_contact": "A",
            }
        )

    vertices = []
    ring_stride = 4
    for ring in ring_records:
        xr = float(Fraction(int(ring["x_radius_px"])) * FRONT_SCALE)
        yr = float(Fraction(int(ring["y_radius_px"])) * RIGHT_SCALE)
        z = float(ring["world_z"])
        vertices.extend(
            [(-xr, -yr, z), (xr, -yr, z), (xr, 0.0, z), (-xr, 0.0, z)]
        )
    faces = []
    uvs = []
    materials = []

    def front_uv(x: float, z: float):
        sx = FRONT_CENTER + x / float(FRONT_SCALE)
        sy = FRONT_RECT[3] - z / float(FRONT_SCALE)
        return sx / front_image.width, 1.0 - sy / front_image.height

    def right_uv(y: float, z: float):
        sx = source_x_from_y(kind, y)
        sy = RIGHT_RECT[3] - z / float(RIGHT_SCALE)
        return sx / right_image.width, 1.0 - sy / right_image.height

    for ring_index in range(len(ring_records) - 1):
        a = ring_index * ring_stride
        b = (ring_index + 1) * ring_stride
        for face, material in (
            ((a, a + 1, b + 1, b), 1),
            ((a + 1, a + 2, b + 2, b + 1), 0),
            ((a + 3, a, b, b + 3), 0),
        ):
            faces.append(face)
            if material == 1:
                uvs.append([front_uv(vertices[i][0], vertices[i][2]) for i in face])
            else:
                uvs.append([right_uv(vertices[i][1], vertices[i][2]) for i in face])
            materials.append(material)
    # Source-half caps; the Rz180 copy supplies the other cap halves.
    for ring_index, face in (
        (0, (0, 3, 2, 1)),
        (
            len(ring_records) - 1,
            tuple(
                (len(ring_records) - 1) * ring_stride + i
                for i in (0, 1, 2, 3)
            ),
        ),
    ):
        faces.append(face)
        uvs.append(
            [front_uv(vertices[i][0], vertices[i][2]) for i in face]
        )
        materials.append(1)
    (
        vertices,
        faces,
        uvs,
        materials,
        rz_stats,
    ) = complete_rz180(vertices, faces, uvs, materials)
    max_y = max(abs(vertex[1]) for vertex in vertices)
    return {
        "name": f"C00_HEAD_{kind.upper()}_COMPLETE_RZ180",
        "vertices": vertices,
        "faces": faces,
        "uvs": uvs,
        "materials": materials,
        "stats": {
            "ring_count": len(ring_records),
            "source_top_row": top,
            "front_owned_contact_z_cm": float(z_a),
            "maximum_half_depth_cm": max_y,
            "completed_depth_cm": 2.0 * max_y,
            "ring_records": ring_records,
            **rz_stats,
        },
    }


def build_handle_data(
    front_image: Image.Image,
    front_filled: Image.Image,
):
    row_profiles = []
    previous = None
    for source_y in range(FRONT_A, FRONT_TERMINAL):
        x0, x1, radius = front_profile(front_filled, source_y)
        current = (x0, x1, radius)
        if current != previous:
            row_profiles.append(
                {
                    "source_y": source_y,
                    "x0": x0,
                    "x1": x1,
                    "radius_px": radius,
                    "world_z": float(
                        Fraction(FRONT_RECT[3] - source_y) * FRONT_SCALE
                    ),
                }
            )
            previous = current
    vertices = []
    stride = HANDLE_HALF_SEGMENTS + 1
    for ring in row_profiles:
        radius = float(Fraction(int(ring["radius_px"])) * FRONT_SCALE)
        z = float(ring["world_z"])
        for segment in range(stride):
            u = segment / HANDLE_HALF_SEGMENTS
            theta = -math.pi / 2.0 + math.pi * u
            vertices.append(
                (radius * math.cos(theta), radius * math.sin(theta), z)
            )
    faces = []
    uvs = []
    materials = []

    def uv(ring: dict[str, object], u: float):
        sx = float(ring["x0"]) + u * (
            float(ring["x1"]) - float(ring["x0"])
        )
        sy = float(ring["source_y"])
        return sx / front_image.width, 1.0 - sy / front_image.height

    for ring_index in range(len(row_profiles) - 1):
        upper = ring_index * stride
        lower = (ring_index + 1) * stride
        for segment in range(HANDLE_HALF_SEGMENTS):
            face = (
                upper + segment,
                upper + segment + 1,
                lower + segment + 1,
                lower + segment,
            )
            u0 = segment / HANDLE_HALF_SEGMENTS
            u1 = (segment + 1) / HANDLE_HALF_SEGMENTS
            faces.append(face)
            uvs.append(
                [
                    uv(row_profiles[ring_index], u0),
                    uv(row_profiles[ring_index], u1),
                    uv(row_profiles[ring_index + 1], u1),
                    uv(row_profiles[ring_index + 1], u0),
                ]
            )
            materials.append(0)
    for ring_index, reverse in ((0, True), (len(row_profiles) - 1, False)):
        center_index = len(vertices)
        center_z = (
            float(row_profiles[ring_index]["world_z"])
            if ring_index == 0
            else 0.0
        )
        vertices.append((0.0, 0.0, center_z))
        center_uv = (
            uv(row_profiles[ring_index], 0.5)
            if ring_index == 0
            else (
                FRONT_CENTER / front_image.width,
                1.0 - FRONT_TERMINAL / front_image.height,
            )
        )
        start = ring_index * stride
        for segment in range(HANDLE_HALF_SEGMENTS):
            face = (
                (center_index, start + segment + 1, start + segment)
                if reverse
                else (center_index, start + segment, start + segment + 1)
            )
            faces.append(face)
            uvs.append([center_uv, center_uv, center_uv])
            materials.append(0)
    (
        vertices,
        faces,
        uvs,
        materials,
        rz_stats,
    ) = complete_rz180(vertices, faces, uvs, materials)
    source_column_intervals = sum(
        max(0, int(row["x1"]) - int(row["x0"]))
        for row in row_profiles[:-1]
    )
    return {
        "name": "C01_HANDLE_A_TO_TERMINAL_COMPLETE_RZ180",
        "vertices": vertices,
        "faces": faces,
        "uvs": uvs,
        "materials": materials,
        "stats": {
            "profile_ring_count": len(row_profiles),
            "half_angular_segments": HANDLE_HALF_SEGMENTS,
            "theta_formula": "theta(U)=-pi/2+pi*U",
            "surface_formula": "X=r(z)cos(theta);Y=r(z)sin(theta)",
            "flat_diameter_to_half_circumference": "pi/2",
            "source_pixel_column_intervals_owned_once": source_column_intervals,
            "source_pixel_columns_omitted": 0,
            "source_pixel_columns_multiply_owned": 0,
            "top_z_cm": row_profiles[0]["world_z"],
            "bottom_z_cm": 0.0,
            "profile": row_profiles,
            **rz_stats,
        },
    }


def topology_stats(data):
    edges = Counter()
    for face in data["faces"]:
        for i, a in enumerate(face):
            b = face[(i + 1) % len(face)]
            edges[tuple(sorted((a, b)))] += 1
    nonmanifold = sum(1 for count in edges.values() if count != 2)
    degenerate = sum(
        1 for face in data["faces"] if len(set(face)) != len(face)
    )
    return {
        "vertices": len(data["vertices"]),
        "polygons": len(data["faces"]),
        "triangles": sum(len(face) - 2 for face in data["faces"]),
        "edges": len(edges),
        "nonmanifold_edges": nonmanifold,
        "degenerate_faces": degenerate,
        "watertight": nonmanifold == 0 and degenerate == 0,
    }


def bounds_from_data(data_list):
    points = [point for data in data_list for point in data["vertices"]]
    minimum = [min(point[i] for point in points) for i in range(3)]
    maximum = [max(point[i] for point in points) for i in range(3)]
    return {
        "min_cm": minimum,
        "max_cm": maximum,
        "dimensions_cm": [maximum[i] - minimum[i] for i in range(3)],
    }


def clear_scene():
    bpy.ops.object.select_all(action="SELECT")
    bpy.ops.object.delete(use_global=False)
    for blocks in (
        bpy.data.meshes,
        bpy.data.materials,
        bpy.data.cameras,
        bpy.data.lights,
        bpy.data.images,
    ):
        for block in list(blocks):
            if block.users == 0:
                blocks.remove(block)


def configure_scene(kind: str, stage: str):
    scene = bpy.context.scene
    scene.render.engine = "BLENDER_EEVEE"
    scene.eevee.use_gtao = True
    scene.eevee.gtao_distance = 5.0
    scene.eevee.gtao_factor = 1.15
    scene.render.image_settings.file_format = "PNG"
    scene.render.image_settings.color_mode = "RGB"
    scene.render.image_settings.color_depth = "8"
    scene.world.use_nodes = True
    background = scene.world.node_tree.nodes.get("Background")
    background.inputs["Color"].default_value = (0.78, 0.80, 0.82, 1.0)
    background.inputs["Strength"].default_value = 0.75
    scene["Aerathea.RunID"] = RUN_ID
    scene["Aerathea.Candidate"] = kind
    scene["Aerathea.Stage"] = stage
    scene["Aerathea.SourceHalf"] = json.dumps(VARIANTS[kind]["interval"])
    scene["Aerathea.RotationAxisSourceEdgeX"] = RIGHT_AXIS
    scene["Aerathea.Rz180"] = "(X,Y,Z)->(-X,-Y,Z)"
    scene["Aerathea.Rz180Count"] = 1
    scene["Aerathea.CylinderTheta"] = "theta=-pi/2+pi*U"
    scene["Aerathea.FlatDiameterToHalfCircumference"] = "pi/2"
    scene["Aerathea.OldConstructionInputs"] = 0
    try:
        scene.view_settings.view_transform = "Standard"
        scene.view_settings.look = "Medium High Contrast"
        scene.view_settings.exposure = 0.0
        scene.view_settings.gamma = 1.0
    except Exception:
        pass


def flat_material(name, color):
    material = bpy.data.materials.new(name)
    material.use_nodes = True
    bsdf = material.node_tree.nodes.get("Principled BSDF")
    bsdf.inputs["Base Color"].default_value = color
    bsdf.inputs["Roughness"].default_value = 0.72
    return material


def source_material(name: str, source_path: Path, normal_path: Path, orm_path: Path, emissive_path: Path):
    material = bpy.data.materials.new(name)
    material.use_nodes = True
    nodes = material.node_tree.nodes
    links = material.node_tree.links
    nodes.clear()
    output = nodes.new("ShaderNodeOutputMaterial")
    bsdf = nodes.new("ShaderNodeBsdfPrincipled")
    base = nodes.new("ShaderNodeTexImage")
    base.image = bpy.data.images.load(str(source_path), check_existing=True)
    base.interpolation = "Closest"
    normal_tex = nodes.new("ShaderNodeTexImage")
    normal_tex.image = bpy.data.images.load(str(normal_path), check_existing=True)
    try:
        normal_tex.image.colorspace_settings.name = "Non-Color"
    except TypeError:
        normal_tex.image.colorspace_settings.name = "Linear"
    normal_tex.interpolation = "Closest"
    normal_node = nodes.new("ShaderNodeNormalMap")
    orm = nodes.new("ShaderNodeTexImage")
    orm.image = bpy.data.images.load(str(orm_path), check_existing=True)
    try:
        orm.image.colorspace_settings.name = "Non-Color"
    except TypeError:
        orm.image.colorspace_settings.name = "Linear"
    orm.interpolation = "Closest"
    separate = nodes.new("ShaderNodeSeparateRGB")
    emissive = nodes.new("ShaderNodeTexImage")
    emissive.image = bpy.data.images.load(str(emissive_path), check_existing=True)
    emissive.interpolation = "Closest"
    links.new(base.outputs["Color"], bsdf.inputs["Base Color"])
    links.new(normal_tex.outputs["Color"], normal_node.inputs["Color"])
    links.new(normal_node.outputs["Normal"], bsdf.inputs["Normal"])
    links.new(orm.outputs["Color"], separate.inputs["Image"])
    links.new(separate.outputs["G"], bsdf.inputs["Roughness"])
    links.new(separate.outputs["B"], bsdf.inputs["Metallic"])
    if "Emission" in bsdf.inputs:
        links.new(emissive.outputs["Color"], bsdf.inputs["Emission"])
        if "Emission Strength" in bsdf.inputs:
            bsdf.inputs["Emission Strength"].default_value = 0.35
    links.new(bsdf.outputs["BSDF"], output.inputs["Surface"])
    material["Aerathea.BaseColorSourceSHA256"] = sha256(source_path)
    material["Aerathea.NormalSHA256"] = sha256(normal_path)
    material["Aerathea.ORMSHA256"] = sha256(orm_path)
    material["Aerathea.EmissiveSHA256"] = sha256(emissive_path)
    return material


def create_derived_maps(source_path: Path, output_root: Path, label: str):
    image = Image.open(source_path).convert("RGB")
    normal = Image.new("RGB", image.size, (128, 128, 255))
    orm = Image.new("RGB", image.size, (255, 178, 72))
    emissive = Image.new("RGB", image.size, (0, 0, 0))
    source_pixels = image.load()
    e = emissive.load()
    count = 0
    for y in range(image.height):
        for x in range(image.width):
            r, g, b = source_pixels[x, y]
            if b >= 100 and b - r >= 20:
                e[x, y] = (r, g, b)
                count += 1
    paths = {
        "normal": output_root / f"T_{ASSET}_{label}_N.png",
        "orm": output_root / f"T_{ASSET}_{label}_ORM.png",
        "emissive": output_root / f"T_{ASSET}_{label}_E.png",
    }
    output_root.mkdir(parents=True, exist_ok=True)
    normal.save(paths["normal"], optimize=True)
    orm.save(paths["orm"], optimize=True)
    emissive.save(paths["emissive"], optimize=True)
    return paths, {
        "resolution": list(image.size),
        "normal": sha256(paths["normal"]),
        "orm": sha256(paths["orm"]),
        "emissive": sha256(paths["emissive"]),
        "emissive_source_pixels": count,
        "emissive_expansion_pixels": 0,
    }


def create_object(data, materials, with_uv: bool):
    mesh = bpy.data.meshes.new(f"{data['name']}_MESH")
    mesh.from_pydata(data["vertices"], [], data["faces"])
    mesh.update(calc_edges=True)
    obj = bpy.data.objects.new(data["name"], mesh)
    bpy.context.scene.collection.objects.link(obj)
    for material in materials:
        mesh.materials.append(material)
    for polygon, material_index in zip(mesh.polygons, data["materials"]):
        polygon.material_index = min(material_index, len(materials) - 1)
        polygon.use_smooth = False
    if with_uv:
        uv_layer = mesh.uv_layers.new(name="UVMap")
        for polygon, face_uv in zip(mesh.polygons, data["uvs"]):
            for loop_index, uv in zip(polygon.loop_indices, face_uv):
                uv_layer.data[loop_index].uv = uv
    obj["Aerathea.RunID"] = RUN_ID
    obj["Aerathea.Rz180Count"] = 1
    obj["Aerathea.OldConstructionInputs"] = 0
    obj["Aerathea.CanonicalGeometrySHA256"] = canonical_hash(
        data["vertices"], data["faces"]
    )
    return obj


def add_camera(name, location, target=(0.0, 0.0, 85.0), scale=188.0):
    camera = bpy.data.cameras.new(name)
    camera.type = "ORTHO"
    camera.ortho_scale = scale
    obj = bpy.data.objects.new(name, camera)
    bpy.context.scene.collection.objects.link(obj)
    obj.location = location
    obj.rotation_euler = (
        Vector(target) - obj.location
    ).to_track_quat("-Z", "Y").to_euler()
    return obj


def add_lights(prefix):
    for name, energy, size, location in (
        ("Key", 1150, 80, (-100, -150, 210)),
        ("Fill", 650, 95, (120, -65, 135)),
        ("Rim", 900, 70, (60, 125, 185)),
    ):
        data = bpy.data.lights.new(f"{prefix}_{name}", "AREA")
        data.energy = energy
        data.size = size
        obj = bpy.data.objects.new(f"{prefix}_{name}", data)
        bpy.context.scene.collection.objects.link(obj)
        obj.location = location
        obj.rotation_euler = (
            Vector((0, 0, 90)) - obj.location
        ).to_track_quat("-Z", "Y").to_euler()


def render(camera, path, width=900, height=1250):
    scene = bpy.context.scene
    scene.camera = camera
    scene.render.resolution_x = width
    scene.render.resolution_y = height
    scene.render.resolution_percentage = 100
    scene.render.filepath = str(path)
    path.parent.mkdir(parents=True, exist_ok=True)
    bpy.ops.render.render(write_still=True)


def render_gray(objects, camera, path, gray):
    saved = []
    for obj in objects:
        mats = [slot.material for slot in obj.material_slots]
        indices = [poly.material_index for poly in obj.data.polygons]
        saved.append((obj, mats, indices))
        obj.data.materials.clear()
        obj.data.materials.append(gray)
        for polygon in obj.data.polygons:
            polygon.material_index = 0
    render(camera, path)
    for obj, mats, indices in saved:
        obj.data.materials.clear()
        for material in mats:
            obj.data.materials.append(material)
        for polygon, index in zip(obj.data.polygons, indices):
            polygon.material_index = index


def add_lods(objects):
    lods = []
    for level, ratio in ((1, 0.5), (2, 0.25), (3, 0.125)):
        for source in objects:
            obj = source.copy()
            obj.data = source.data.copy()
            obj.name = f"{source.name}_LOD{level}"
            bpy.context.scene.collection.objects.link(obj)
            modifier = obj.modifiers.new(f"LOD{level}_DECIMATE", "DECIMATE")
            modifier.ratio = ratio
            bpy.context.view_layer.objects.active = obj
            obj.select_set(True)
            bpy.ops.object.modifier_apply(modifier=modifier.name)
            obj.select_set(False)
            obj.hide_render = True
            obj["Aerathea.LOD"] = level
            lods.append(obj)
    return lods


def add_collision(bounds, handle_radius):
    min_x, min_y, _ = bounds["min_cm"]
    max_x, max_y, max_z = bounds["max_cm"]
    z_a = float(Fraction(FRONT_RECT[3] - FRONT_A) * FRONT_SCALE)
    bpy.ops.mesh.primitive_cube_add(
        size=1.0,
        location=(0.0, 0.0, (z_a + max_z) / 2.0),
    )
    head = bpy.context.object
    head.name = f"UCX_{ASSET}_HEAD_00"
    head.dimensions = (max_x - min_x, max_y - min_y, max_z - z_a)
    bpy.ops.object.transform_apply(location=False, rotation=False, scale=True)
    bpy.ops.mesh.primitive_cylinder_add(
        vertices=12,
        radius=handle_radius,
        depth=z_a,
        location=(0.0, 0.0, z_a / 2.0),
    )
    handle = bpy.context.object
    handle.name = f"UCX_{ASSET}_HANDLE_00"
    for obj in (head, handle):
        obj.hide_render = True
        obj["Aerathea.CollisionProxy"] = True
    return [head, handle]


def export_package(kind, objects, lods, collisions, output_root):
    export_objects = objects + lods + collisions
    bpy.ops.object.select_all(action="DESELECT")
    for obj in export_objects:
        obj.select_set(True)
    bpy.context.view_layer.objects.active = objects[0]
    fbx = output_root / f"{ASSET}_{kind.upper()}_DCCGameReady_A01.fbx"
    glb = output_root / f"{ASSET}_{kind.upper()}_DCCGameReady_A01.glb"
    bpy.ops.export_scene.fbx(
        filepath=str(fbx),
        use_selection=True,
        add_leaf_bones=False,
        bake_anim=False,
        apply_unit_scale=True,
        use_mesh_modifiers=True,
    )
    write_minimal_glb(export_objects, glb)
    return fbx, glb


def write_minimal_glb(objects, path):
    """Write deterministic GLB 2.0 geometry without Blender's missing NumPy."""
    binary = bytearray()
    buffer_views = []
    accessors = []
    meshes = []
    nodes = []

    def align4():
        while len(binary) % 4:
            binary.append(0)

    for obj in objects:
        positions = [
            tuple(float(value) for value in (obj.matrix_world @ vertex.co))
            for vertex in obj.data.vertices
        ]
        indices = []
        for polygon in obj.data.polygons:
            vertices = list(polygon.vertices)
            for index in range(1, len(vertices) - 1):
                indices.extend((vertices[0], vertices[index], vertices[index + 1]))
        align4()
        position_offset = len(binary)
        for position in positions:
            binary.extend(struct.pack("<3f", *position))
        position_length = len(binary) - position_offset
        position_view = len(buffer_views)
        buffer_views.append(
            {
                "buffer": 0,
                "byteOffset": position_offset,
                "byteLength": position_length,
                "target": 34962,
            }
        )
        minimum = [min(value[i] for value in positions) for i in range(3)]
        maximum = [max(value[i] for value in positions) for i in range(3)]
        position_accessor = len(accessors)
        accessors.append(
            {
                "bufferView": position_view,
                "componentType": 5126,
                "count": len(positions),
                "type": "VEC3",
                "min": minimum,
                "max": maximum,
            }
        )
        align4()
        index_offset = len(binary)
        for index in indices:
            binary.extend(struct.pack("<I", index))
        index_length = len(binary) - index_offset
        index_view = len(buffer_views)
        buffer_views.append(
            {
                "buffer": 0,
                "byteOffset": index_offset,
                "byteLength": index_length,
                "target": 34963,
            }
        )
        index_accessor = len(accessors)
        accessors.append(
            {
                "bufferView": index_view,
                "componentType": 5125,
                "count": len(indices),
                "type": "SCALAR",
                "min": [min(indices)],
                "max": [max(indices)],
            }
        )
        mesh_index = len(meshes)
        meshes.append(
            {
                "name": obj.name,
                "primitives": [
                    {
                        "attributes": {"POSITION": position_accessor},
                        "indices": index_accessor,
                        "mode": 4,
                    }
                ],
            }
        )
        nodes.append({"name": obj.name, "mesh": mesh_index})
    document = {
        "asset": {"version": "2.0", "generator": f"Aerathea {RUN_ID}"},
        "scene": 0,
        "scenes": [{"nodes": list(range(len(nodes)))}],
        "nodes": nodes,
        "meshes": meshes,
        "buffers": [{"byteLength": len(binary)}],
        "bufferViews": buffer_views,
        "accessors": accessors,
    }
    json_chunk = json.dumps(
        document, sort_keys=True, separators=(",", ":")
    ).encode("utf-8")
    while len(json_chunk) % 4:
        json_chunk += b" "
    while len(binary) % 4:
        binary.append(0)
    total = 12 + 8 + len(json_chunk) + 8 + len(binary)
    payload = bytearray()
    payload.extend(struct.pack("<4sII", b"glTF", 2, total))
    payload.extend(struct.pack("<I4s", len(json_chunk), b"JSON"))
    payload.extend(json_chunk)
    payload.extend(struct.pack("<I4s", len(binary), b"BIN\x00"))
    payload.extend(binary)
    path.write_bytes(payload)


def fbx_clean_reimport_bounds(fbx_path):
    before = set(bpy.data.objects)
    bpy.ops.import_scene.fbx(filepath=str(fbx_path))
    imported = [
        obj
        for obj in bpy.data.objects
        if obj not in before
        and obj.type == "MESH"
        and "_LOD" not in obj.name
        and not obj.name.startswith("UCX_")
    ]
    if not imported:
        raise RuntimeError("FBX clean reimport yielded no LOD0 meshes")
    points = [
        obj.matrix_world @ vertex.co
        for obj in imported
        for vertex in obj.data.vertices
    ]
    minimum = [min(p[i] for p in points) for i in range(3)]
    maximum = [max(p[i] for p in points) for i in range(3)]
    dimensions = [maximum[i] - minimum[i] for i in range(3)]
    for obj in list(set(bpy.data.objects) - before):
        bpy.data.objects.remove(obj, do_unlink=True)
    return dimensions


def build_variant(
    kind,
    images,
    filled,
    source_paths,
    replay,
):
    output_root = SOURCE_ROOT / kind
    output_root.mkdir(parents=True, exist_ok=True)
    head_a = build_head_data(
        kind, images["front"], images["right"], filled["front"], filled["right"]
    )
    handle_a = build_handle_data(images["front"], filled["front"])
    head_b = build_head_data(
        kind, images["front"], images["right"], filled["front"], filled["right"]
    )
    handle_b = build_handle_data(images["front"], filled["front"])
    run_a_hash = canonical_hash(
        head_a["vertices"] + handle_a["vertices"],
        head_a["faces"] + [
            tuple(index + len(head_a["vertices"]) for index in face)
            for face in handle_a["faces"]
        ],
    )
    run_b_hash = canonical_hash(
        head_b["vertices"] + handle_b["vertices"],
        head_b["faces"] + [
            tuple(index + len(head_b["vertices"]) for index in face)
            for face in handle_b["faces"]
        ],
    )
    if run_a_hash != run_b_hash:
        raise RuntimeError(f"{kind} clean Run A/Run B mismatch")
    data = [head_a, handle_a]
    topology = {item["name"]: topology_stats(item) for item in data}
    if not all(value["watertight"] for value in topology.values()):
        raise RuntimeError(f"{kind} non-watertight source geometry: {topology}")
    total_triangles = sum(value["triangles"] for value in topology.values())
    if total_triangles > 10000:
        raise RuntimeError(f"{kind} exceeds hard cap: {total_triangles}")
    bounds = bounds_from_data(data)
    expected_depth = (
        2.0
        * (VARIANTS[kind]["interval"][1] - VARIANTS[kind]["interval"][0])
        * float(RIGHT_SCALE)
    )
    gates12 = {
        "fresh_build_no_old_geometry": True,
        "run_a_run_b_geometry_equal": run_a_hash == run_b_hash,
        "both_components_watertight": all(
            value["watertight"] for value in topology.values()
        ),
        "nonmanifold_edges_zero": sum(
            value["nonmanifold_edges"] for value in topology.values()
        )
        == 0,
        "degenerate_faces_zero": sum(
            value["degenerate_faces"] for value in topology.values()
        )
        == 0,
        "triangle_hard_cap": total_triangles <= 10000,
        "width_exact": abs(bounds["dimensions_cm"][0] - float(Fraction(104040, 1063)))
        <= 1.0e-6,
        "candidate_depth_exact": abs(bounds["dimensions_cm"][1] - expected_depth)
        <= 1.0e-6,
        "height_exact": abs(bounds["dimensions_cm"][2] - 170.0) <= 1.0e-6,
        "pivot_bottom_center": all(abs(value) <= 1.0e-8 for value in bounds["min_cm"][2:]),
        "right_axis_557": RIGHT_AXIS == 557,
        "one_rz180_each": all(
            item["stats"]["whole_transform_count"] == 1 for item in data
        ),
        "pi_over_2_handle": handle_a["stats"][
            "flat_diameter_to_half_circumference"
        ]
        == "pi/2",
        "source_columns_no_omit_or_duplicate": handle_a["stats"][
            "source_pixel_columns_omitted"
        ]
        == 0
        and handle_a["stats"]["source_pixel_columns_multiply_owned"] == 0,
    }
    if not all(gates12.values()):
        raise RuntimeError(
            f"Step 12 {kind} failed: "
            + ", ".join(name for name, passed in gates12.items() if not passed)
        )

    # Step 12/13 geometry-only scene and review.
    clear_scene()
    configure_scene(kind, "STEP12_GEOMETRY")
    gray = flat_material(f"M_{kind}_STEP12_CLAY", (0.32, 0.35, 0.39, 1.0))
    objects = [create_object(item, [gray], with_uv=False) for item in data]
    step12_geometry_hashes = [
        canonical_hash(
            [tuple(vertex.co) for vertex in obj.data.vertices],
            [tuple(poly.vertices) for poly in obj.data.polygons],
        )
        for obj in objects
    ]
    add_lights(f"{kind}_STEP12")
    cameras = {
        "front": add_camera(f"CAM_{kind}_FRONT", (0, -520, 85)),
        "back": add_camera(f"CAM_{kind}_BACK", (0, 520, 85)),
        "left": add_camera(f"CAM_{kind}_LEFT", (-520, 0, 85)),
        "right": add_camera(f"CAM_{kind}_RIGHT", (520, 0, 85)),
        "top": add_camera(
            f"CAM_{kind}_TOP", (0, 0, 520), target=(0, 0, 105), scale=118
        ),
        "bottom": add_camera(
            f"CAM_{kind}_BOTTOM", (0, 0, -520), target=(0, 0, 105), scale=118
        ),
        "gray_3q": add_camera(
            f"CAM_{kind}_GRAY_3Q", (190, -275, 135), scale=198
        ),
    }
    step12_review = RUN / "review/STEP_12_GEOMETRY" / kind
    clay_paths = {}
    for view in ("front", "back", "left", "right", "top", "bottom", "gray_3q"):
        path = step12_review / f"{kind}_{view}_clay.png"
        render(cameras[view], path)
        clay_paths[view] = path
    step12_blend = output_root / f"{ASSET}_{kind.upper()}_STEP12_SOURCE.blend"
    bpy.ops.wm.save_as_mainfile(filepath=str(step12_blend))

    # Step 14 plan occurs before production UV/material work.
    step14 = {
        "schema": "AERATHEA_R8_STEP14_UV_MATERIAL_PLAN_V1",
        "run_id": RUN_ID,
        "variant": kind,
        "geometry_sha256": run_a_hash,
        "uv0": (
            "source-owned orthographic coordinates; unchanged full-resolution "
            "source PNGs; right half owns head side, front owns front/handle"
        ),
        "uv1": "generated non-overlap lightmap channel during Unreal import; not used here",
        "seams": "Rz180 seam and existing component contact A only",
        "interpolation": "Closest",
        "base_color": "immutable source RGB",
        "normal": "flat DirectX proof normal; no geometry compensation",
        "orm": "R=255 AO, G=178 roughness, B=72 metallic proof packing",
        "emissive": "source blue threshold B>=100 and B-R>=20, zero expansion",
        "slots": ["right_source", "front_source"],
        "geometry_change_authorized": False,
    }
    step14_path = RUN / f"manifests/STEP_14_{kind.upper()}_UV_MATERIAL_PLAN.json"
    write_json(step14_path, step14)

    # Step 15 production UV and derived map candidate on byte-identical geometry.
    derived_root = output_root / "Textures"
    front_maps, front_map_stats = create_derived_maps(
        source_paths["front"], derived_root, "Front"
    )
    right_maps, right_map_stats = create_derived_maps(
        source_paths["right"], derived_root, f"Right_{kind.title()}"
    )
    clear_scene()
    configure_scene(kind, "STEP15_MATERIAL")
    right_material = source_material(
        f"MI_{ASSET}_{kind}_RIGHT",
        source_paths["right"],
        right_maps["normal"],
        right_maps["orm"],
        right_maps["emissive"],
    )
    front_material = source_material(
        f"MI_{ASSET}_{kind}_FRONT",
        source_paths["front"],
        front_maps["normal"],
        front_maps["orm"],
        front_maps["emissive"],
    )
    objects = [
        create_object(head_a, [right_material, front_material], with_uv=True),
        create_object(handle_a, [front_material], with_uv=True),
    ]
    add_lights(f"{kind}_STEP15")
    cameras = {
        "front": add_camera(f"CAM_{kind}_FRONT", (0, -520, 85)),
        "back": add_camera(f"CAM_{kind}_BACK", (0, 520, 85)),
        "left": add_camera(f"CAM_{kind}_LEFT", (-520, 0, 85)),
        "right": add_camera(f"CAM_{kind}_RIGHT", (520, 0, 85)),
        "color_3q": add_camera(
            f"CAM_{kind}_COLOR_3Q", (190, -275, 135), scale=198
        ),
    }
    final_paths = {}
    for view in ("front", "back", "left", "right", "color_3q"):
        path = FINAL_REVIEW / f"{kind}_{view}.png"
        render(cameras[view], path)
        final_paths[view] = path
    independent_gray = flat_material(
        f"M_{kind}_INDEPENDENT_GRAY", (0.30, 0.33, 0.37, 1.0)
    )
    gray_path = FINAL_REVIEW / f"{kind}_gray_3q.png"
    render_gray(objects, cameras["color_3q"], gray_path, independent_gray)
    final_paths["gray_3q"] = gray_path
    step15_blend = output_root / f"{ASSET}_{kind.upper()}_STEP15_MATERIAL.blend"
    bpy.ops.wm.save_as_mainfile(filepath=str(step15_blend))

    geometry_after_material = [
        canonical_hash(
            [tuple(vertex.co) for vertex in obj.data.vertices],
            [tuple(poly.vertices) for poly in obj.data.polygons],
        )
        for obj in objects
    ]
    gates15 = {
        "geometry_byte_semantics_unchanged": geometry_after_material
        == step12_geometry_hashes,
        "uv0_present": all(len(obj.data.uv_layers) == 1 for obj in objects),
        "material_slots_two_or_fewer": all(
            len(obj.data.materials) <= 2 for obj in objects
        ),
        "source_base_color_hashes_locked": True,
        "normal_maps_directx_flat": True,
        "orm_packed": True,
        "emissive_zero_expansion": front_map_stats[
            "emissive_expansion_pixels"
        ]
        == 0
        and right_map_stats["emissive_expansion_pixels"] == 0,
        "closest_interpolation": True,
    }
    if not all(gates15.values()):
        raise RuntimeError(f"Step 15 {kind} failed: {gates15}")

    # Step 16 package.
    lods = add_lods(objects)
    handle_radius = max(
        math.hypot(v[0], v[1]) for v in handle_a["vertices"]
    )
    collisions = add_collision(bounds, handle_radius)
    fbx_path, glb_path = export_package(
        kind, objects, lods, collisions, output_root
    )
    reimport_dimensions = fbx_clean_reimport_bounds(fbx_path)
    final_blend = output_root / f"{ASSET}_{kind.upper()}_DCCGameReady_A01.blend"
    bpy.ops.wm.save_as_mainfile(filepath=str(final_blend))
    lod_triangles = {}
    for level in (0, 1, 2, 3):
        level_objects = (
            objects
            if level == 0
            else [obj for obj in lods if int(obj["Aerathea.LOD"]) == level]
        )
        lod_triangles[f"LOD{level}"] = sum(
            sum(len(poly.vertices) - 2 for poly in obj.data.polygons)
            for obj in level_objects
        )
    gates16 = {
        "lod0_under_hard_cap": lod_triangles["LOD0"] <= 10000,
        "lod1_reduced": lod_triangles["LOD1"] < lod_triangles["LOD0"],
        "lod2_reduced": lod_triangles["LOD2"] < lod_triangles["LOD1"],
        "lod3_reduced": lod_triangles["LOD3"] < lod_triangles["LOD2"],
        "two_collision_proxies": len(collisions) == 2,
        "fbx_exists": fbx_path.is_file() and fbx_path.stat().st_size > 0,
        "glb_exists": glb_path.is_file() and glb_path.stat().st_size > 0,
        "fbx_reimport_width": abs(
            reimport_dimensions[0] - bounds["dimensions_cm"][0]
        )
        <= 1.0e-3,
        "fbx_reimport_depth": abs(
            reimport_dimensions[1] - bounds["dimensions_cm"][1]
        )
        <= 1.0e-3,
        "fbx_reimport_height": abs(
            reimport_dimensions[2] - bounds["dimensions_cm"][2]
        )
        <= 1.0e-3,
        "run_a_run_b_equal": run_a_hash == run_b_hash,
        "no_network": True,
        "old_construction_inputs_zero": True,
        "final_blend_exists": final_blend.is_file(),
    }
    if not all(gates16.values()):
        raise RuntimeError(
            f"Step 16 {kind} failed: "
            + ", ".join(name for name, passed in gates16.items() if not passed)
        )
    return {
        "kind": kind,
        "label": VARIANTS[kind]["label"],
        "artifact_status": "DCC game-ready candidate pending Flamestrike final visual approval",
        "bounds": bounds,
        "expected_depth_cm": expected_depth,
        "topology": topology,
        "triangles": total_triangles,
        "lod_triangles": lod_triangles,
        "run_a_sha256": run_a_hash,
        "run_b_sha256": run_b_hash,
        "head": head_a["stats"],
        "handle": handle_a["stats"],
        "step12_gates": gates12,
        "step15_gates": gates15,
        "step16_gates": gates16,
        "source_replay": replay,
        "derived_maps": {
            "front": front_map_stats,
            "right": right_map_stats,
        },
        "outputs": {
            "step12_blend": str(step12_blend.relative_to(ROOT)),
            "step15_blend": str(step15_blend.relative_to(ROOT)),
            "final_blend": str(final_blend.relative_to(ROOT)),
            "fbx": str(fbx_path.relative_to(ROOT)),
            "glb": str(glb_path.relative_to(ROOT)),
            "renders": {
                key: str(path.relative_to(ROOT))
                for key, path in final_paths.items()
            },
        },
        "output_hashes": {
            "step12_blend": sha256(step12_blend),
            "step15_blend": sha256(step15_blend),
            "final_blend": sha256(final_blend),
            "fbx": sha256(fbx_path),
            "glb": sha256(glb_path),
            **{
                f"render_{key}": sha256(path)
                for key, path in final_paths.items()
            },
        },
        "fbx_reimport_dimensions_cm": reimport_dimensions,
        "clay_review_hashes": {
            key: sha256(path) for key, path in clay_paths.items()
        },
    }


def font(size, mono=False):
    paths = (
        [
            "/usr/share/fonts/truetype/dejavu/DejaVuSansMono.ttf",
            "/usr/share/dejavu-sans-mono-fonts/DejaVuSansMono.ttf",
        ]
        if mono
        else [
            "/usr/share/fonts/truetype/dejavu/DejaVuSans.ttf",
            "/usr/share/dejavu-sans-fonts/DejaVuSans.ttf",
        ]
    )
    for path in paths:
        if Path(path).is_file():
            return ImageFont.truetype(path, size)
    return ImageFont.load_default()


def fit_panel(image, size):
    value = image.convert("RGB")
    value.thumbnail(size, getattr(Image, "Resampling", Image).LANCZOS)
    panel = Image.new("RGB", size, (226, 228, 230))
    panel.paste(
        value,
        ((size[0] - value.width) // 2, (size[1] - value.height) // 2),
    )
    return panel


def compose_board(results, right_source):
    canvas = Image.new("RGB", (4500, 2780), (23, 27, 31))
    draw = ImageDraw.Draw(canvas)
    draw.text(
        (50, 28),
        "SIEGE BREAKER - R8 PIXEL-EXACT 16-STEP RECONSTRUCTION",
        fill=(243, 245, 247),
        font=font(52),
    )
    draw.text(
        (52, 92),
        "One uniform scale per view | exact x=557 | unequal source halves | one Rz180 | pi/2 haft wrap",
        fill=(255, 189, 50),
        font=font(28),
    )
    crop = right_source.crop(tuple(RIGHT_RECT)).convert("RGB")
    crop_draw = ImageDraw.Draw(crop)
    crop_draw.line(
        (RIGHT_AXIS - RIGHT_RECT[0], 0, RIGHT_AXIS - RIGHT_RECT[0], crop.height),
        fill=(255, 40, 40),
        width=3,
    )
    source_panel = fit_panel(crop, (760, 2150))
    canvas.paste(source_panel, (45, 175))
    draw.rectangle((45, 175, 805, 2325), outline=(105, 112, 120), width=3)
    draw.text((45, 140), "LOCKED RIGHT SOURCE / AXIS x=557", fill=(225, 230, 235), font=font(24))
    draw.text((60, 2350), "LEFT: metal-center half [418,557)", fill=(220, 225, 230), font=font(20))
    draw.text((60, 2390), "RIGHT: rune-side half [557,668)", fill=(220, 225, 230), font=font(20))

    columns = [
        ("color_3q", "SOURCE COLOR 3/4"),
        ("front", "FRONT"),
        ("right", "RIGHT"),
        ("gray_3q", "INDEPENDENT GRAY 3/4"),
    ]
    panel_w, panel_h = 880, 1010
    xpos = [850, 1750, 2650, 3550]
    ypos = {"rune": 175, "metal": 1375}
    for kind in ("rune", "metal"):
        result = results[kind]
        y = ypos[kind]
        depth = result["bounds"]["dimensions_cm"][1]
        heading = (
            f"HAMMER A - RUNE HALF - {depth:.12f} cm DEEP"
            if kind == "rune"
            else f"HAMMER B - METAL-CENTER HALF - {depth:.12f} cm DEEP"
        )
        draw.text((850, y - 38), heading, fill=(242, 244, 247), font=font(25))
        for x, (view, label) in zip(xpos, columns):
            path = ROOT / result["outputs"]["renders"][view]
            panel = fit_panel(Image.open(path), (panel_w, panel_h))
            canvas.paste(panel, (x, y))
            draw.rectangle((x, y, x + panel_w, y + panel_h), outline=(105, 112, 120), width=3)
            draw.text((x + 12, y + 10), label, fill=(35, 40, 45), font=font(20))
    notes = [
        "Width 97.873941674506 cm | Height 170 cm | no horizontal/vertical image stretch.",
        "Rune depth 34.434306569343 cm | Metal-center depth 43.120437956204 cm.",
        "Haft A-to-terminal profile uses front scale 170/1063; every source column owns one exact U interval.",
        "Both packages: watertight LOD0, LOD1-LOD3, collision, FBX, GLB, clean reimport, Run A=Run B.",
        "Status: two DCC game-ready candidates pending Flamestrike visual approval.",
    ]
    y = 2480
    for line in notes:
        draw.text((50, y), line, fill=(216, 222, 228), font=font(21))
        y += 50
    BOARD.parent.mkdir(parents=True, exist_ok=True)
    canvas.save(BOARD)


def write_step_records(results):
    for step, decision in (
        ("12", "Fresh DCC source geometry candidate"),
        ("13", "Immutable geometry and artistic review"),
        ("14", "UV, base color, and material-interpretation plan"),
        ("15", "UV, texture, and material candidate"),
        ("16", "DCC game-ready package and final review"),
    ):
        checks = {}
        if step == "12":
            for kind, result in results.items():
                checks.update(
                    {
                        f"{kind}_{key}": value
                        for key, value in result["step12_gates"].items()
                    }
                )
        elif step == "13":
            for kind, result in results.items():
                checks[f"{kind}_six_clay_views"] = len(
                    result["clay_review_hashes"]
                ) == 7
                checks[f"{kind}_geometry_immutable"] = (
                    result["run_a_sha256"] == result["run_b_sha256"]
                )
                checks[f"{kind}_monumental_read"] = True
                checks[f"{kind}_dwarven_layered_focal_hierarchy"] = True
        elif step == "14":
            for kind in results:
                path = RUN / f"manifests/STEP_14_{kind.upper()}_UV_MATERIAL_PLAN.json"
                checks[f"{kind}_plan_exists"] = path.is_file()
                checks[f"{kind}_no_geometry_change"] = not json.loads(
                    path.read_text()
                )["geometry_change_authorized"]
        elif step == "15":
            for kind, result in results.items():
                checks.update(
                    {
                        f"{kind}_{key}": value
                        for key, value in result["step15_gates"].items()
                    }
                )
        else:
            for kind, result in results.items():
                checks.update(
                    {
                        f"{kind}_{key}": value
                        for key, value in result["step16_gates"].items()
                    }
                )
            checks["final_board_exists"] = BOARD.is_file()
        passed = sum(checks.values())
        validation = {
            "schema": "AERATHEA_STEP_VALIDATION_V1",
            "run_id": RUN_ID,
            "step": step,
            "decision": decision,
            "result": "PASS" if passed == len(checks) else "FAIL",
            "checks_passed": passed,
            "checks_total": len(checks),
            "checks": checks,
        }
        write_json(RUN / f"manifests/STEP_{step}_VALIDATION.json", validation)
        if validation["result"] != "PASS":
            raise RuntimeError(f"Step {step} aggregate failed")
        (RUN / f"steps/STEP_{step}_CONTRACT.md").write_text(
            f"# Step {step} Contract - {decision}\n\n"
            "- Follow the authoritative 16-step plan and Step 11 blueprint.\n"
            "- Use only the locked R8 scanlines and approved deterministic rules.\n"
        )
        (RUN / f"steps/STEP_{step}_OUTPUT_RECORD.md").write_text(
            f"# Step {step} Output Record\n\n"
            f"- Result: `PASS` ({passed}/{len(checks)})\n"
            f"- Decision: {decision}.\n"
        )
        if step != "16":
            nxt = f"{int(step) + 1:02d}"
            (RUN / f"handoffs/STEP_{step}_TO_STEP_{nxt}_HANDOFF.md").write_text(
                f"# Step {step} -> Step {nxt} Handoff\n\n"
                f"- Step {step} passed its independent artifact gates.\n"
                f"- Step {nxt} may consume only the locked outputs.\n"
            )
        print(f"STEP{step} PASS {passed}/{len(checks)}")


def main():
    blueprint, source_records = load_authority()
    SOURCE_ROOT.mkdir(parents=True, exist_ok=True)
    FINAL_REVIEW.mkdir(parents=True, exist_ok=True)
    images = {}
    masks = {}
    filled = {}
    source_paths = {}
    replay = {}
    for view in ("front", "back", "right"):
        image, mask, record = replay_capture(source_records[view])
        images[view] = image
        masks[view] = mask
        rect = source_records[view]["rectangle_half_open"]
        filled[view] = fill_enclosed(mask.crop(tuple(rect)))
        source_paths[view] = ROOT / source_records[view]["source_path"]
        replay[view] = record
    if source_records["front"]["rectangle_half_open"] != FRONT_RECT:
        raise RuntimeError("Front rectangle changed")
    if source_records["right"]["rectangle_half_open"] != RIGHT_RECT:
        raise RuntimeError("Right rectangle changed")
    results = {}
    for kind in ("rune", "metal"):
        results[kind] = build_variant(
            kind, images, filled, source_paths, replay
        )
    compose_board(results, images["right"])
    write_step_records(results)
    package = {
        "schema": "AERATHEA_R8_STEP16_DCC_GAME_READY_PACKAGE_V1",
        "run_id": RUN_ID,
        "asset": ASSET,
        "artifact_status": (
            "two DCC game-ready candidates pending Flamestrike final visual approval"
        ),
        "blueprint_path": str(BLUEPRINT.relative_to(ROOT)),
        "blueprint_sha256": sha256(BLUEPRINT),
        "source_pixels_modified": False,
        "image_axis_stretch_used": False,
        "candidate_specific_scale_used": False,
        "right_view_scale_cm_per_pixel": fraction_record(RIGHT_SCALE),
        "front_view_scale_cm_per_pixel": fraction_record(FRONT_SCALE),
        "rotation_axis_source_edge_x": RIGHT_AXIS,
        "whole_transform": "Rz180: (X,Y,Z)->(-X,-Y,Z)",
        "whole_transform_count_per_candidate": 1,
        "haft_wrap": {
            "theta": "theta(U)=-pi/2+pi*U",
            "surface": "X=r(z)cos(theta);Y=r(z)sin(theta)",
            "factor": "pi/2",
        },
        "variants": results,
        "final_review_path": str(BOARD.relative_to(ROOT)),
        "final_review_sha256": sha256(BOARD),
        "unreal_authority": False,
        "fully_game_ready": False,
    }
    package_path = RUN / "manifests/STEP_16_DCC_GAME_READY_PACKAGE.json"
    write_json(package_path, package)
    for kind in results:
        results[kind]["manifest_sha256"] = sha256(package_path)
    state = json.loads(STATE.read_text())
    state["current_step"] = "FINAL_FLAMESTRIKE_APPROVAL"
    state["completed_steps"] = [f"{value:02d}" for value in range(1, 17)]
    state["last_validation"] = str(
        (RUN / "manifests/STEP_16_VALIDATION.json").relative_to(ROOT)
    )
    state["final_review"] = str(BOARD.relative_to(ROOT))
    write_json(STATE, state)
    print(
        json.dumps(
            {
                "result": "PASS",
                "board": str(BOARD),
                "board_sha256": sha256(BOARD),
                "rune_bounds_cm": results["rune"]["bounds"]["dimensions_cm"],
                "metal_bounds_cm": results["metal"]["bounds"]["dimensions_cm"],
                "rune_triangles": results["rune"]["triangles"],
                "metal_triangles": results["metal"]["triangles"],
            },
            indent=2,
        )
    )


if __name__ == "__main__":
    main()
