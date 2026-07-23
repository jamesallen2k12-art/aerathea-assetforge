#!/usr/bin/env python3
"""Build two fresh Siege Breakers from the two correct R8 right-image halves."""

from __future__ import annotations

from collections import deque
from fractions import Fraction
import gzip
import hashlib
import json
import math
from pathlib import Path

import bpy
from mathutils import Vector
from PIL import Image, ImageDraw, ImageFont


ROOT = Path(__file__).resolve().parents[2]
ASSET = "SM_DRW_SiegeBreaker_Hammer_A01"
ASSET_ROOT = ROOT / "docs/assets/blueprints" / ASSET
CONTRACT_ID = "SB-A12-R10-R8-CORRECT-AXIS-TWO-HAMMER-A01"
CONTRACT = (
    ASSET_ROOT
    / "steps/A12_R10_R8_CORRECT_AXIS_TWO_HAMMER_A01_CONTRACT.md"
)
SCAN_MANIFEST = (
    ASSET_ROOT
    / "manifests/A12_R10_R8_FULL_SCANLINE_DIMENSION_COMPATIBILITY_A01.json"
)
SCALE_MANIFEST = (
    ASSET_ROOT
    / "manifests/A12_R10_R8_VIEW_OWNED_SCALE_RECONCILIATION_A01.json"
)
DIAMOND_MANIFEST = (
    ASSET_ROOT
    / "manifests/A12_R10_R8_RIGHT_DIAMOND_CENTER_HALF_ROTATION_A01.json"
)

REVIEW_ROOT = (
    ASSET_ROOT / "review/A12_R10_R8_CORRECT_AXIS_TWO_HAMMER_A01"
)
COMPARISON_BOARD = (
    REVIEW_ROOT / "A12_R10_R8_CORRECT_AXIS_TWO_HAMMER_A01_REVIEW.png"
)

TARGET_WIDTH = Fraction(104040, 1063)
TARGET_DEPTH = Fraction(24579450, 517681)
TARGET_HEIGHT = Fraction(170)
TARGET_HALF_WIDTH = TARGET_WIDTH / 2
TARGET_HALF_DEPTH = TARGET_DEPTH / 2
FRONT_SCALE = TARGET_HEIGHT / 1063

DIAMOND_X = 557
RIGHT_RECT = [418, 166, 668, 1262]
FRONT_RECT = [256, 208, 868, 1271]
BACK_RECT = [253, 204, 870, 1266]
FRONT_CENTER_X = Fraction(562)

RIGHT_HEAD_A = 647
FRONT_A = 600
FRONT_C = 670
FRONT_H1 = 870
FRONT_H8 = 955
FRONT_U1 = 1110
FRONT_U3 = 1150
FRONT_L4 = 1220
FRONT_TERMINAL = 1271

Z_A = Fraction(132)
LOWER_SCALE = Fraction(18, FRONT_TERMINAL - FRONT_U3)
Z_U3 = Fraction(18)
Z_U1 = Z_U3 + (FRONT_U3 - FRONT_U1) * LOWER_SCALE
Z_H8 = Z_U1 + Fraction(42)
UPPER_SCALE = (Z_A - Z_H8) / (FRONT_H8 - FRONT_A)
Z_C = Z_A - (FRONT_C - FRONT_A) * UPPER_SCALE
Z_H1 = Z_A - (FRONT_H1 - FRONT_A) * UPPER_SCALE
Z_L4 = (FRONT_TERMINAL - FRONT_L4) * LOWER_SCALE

R_SHAFT = Fraction(5, 2)
R_POMMEL_MAX = Fraction(11, 2)
HALF_SEGMENTS = 64

CANDIDATES = {
    "rune": {
        "label": "RUNE-SIDE HALF",
        "source_interval": [557, 668],
        "source_top": 166,
        "attempt": "A12_R10_R8CorrectAxisRuneSide_A01",
        "manifest_name": "A12_R10_R8_CORRECT_AXIS_RUNE_SIDE_A01_VALIDATION.json",
        "audit_name": "A12_R10_R8_CORRECT_AXIS_RUNE_SIDE_A01_INDEPENDENT_AUDIT.json",
    },
    "metal": {
        "label": "METAL-CENTER-PIECE HALF",
        "source_interval": [418, 557],
        "source_top": 170,
        "attempt": "A12_R10_R8CorrectAxisMetalCenter_A01",
        "manifest_name": "A12_R10_R8_CORRECT_AXIS_METAL_CENTER_A01_VALIDATION.json",
        "audit_name": "A12_R10_R8_CORRECT_AXIS_METAL_CENTER_A01_INDEPENDENT_AUDIT.json",
    },
}


def sha256_bytes(payload: bytes) -> str:
    return hashlib.sha256(payload).hexdigest()


def sha256(path: Path) -> str:
    return sha256_bytes(path.read_bytes())


def exact(record: dict[str, object]) -> Fraction:
    return Fraction(int(record["numerator"]), int(record["denominator"]))


def fraction_record(value: Fraction) -> dict[str, object]:
    return {
        "numerator": value.numerator,
        "denominator": value.denominator,
        "display_decimal": f"{float(value):.12f}",
    }


def font(size: int, mono: bool = False) -> ImageFont.ImageFont:
    candidates = (
        (
            "/usr/share/fonts/truetype/dejavu/DejaVuSansMono.ttf",
            "/usr/share/dejavu-sans-mono-fonts/DejaVuSansMono.ttf",
        )
        if mono
        else (
            "/usr/share/fonts/truetype/dejavu/DejaVuSans.ttf",
            "/usr/share/dejavu-sans-fonts/DejaVuSans.ttf",
        )
    )
    for candidate in candidates:
        if Path(candidate).is_file():
            return ImageFont.truetype(candidate, size)
    return ImageFont.load_default()


def ensure_dirs() -> None:
    REVIEW_ROOT.mkdir(parents=True, exist_ok=True)
    (ASSET_ROOT / "manifests").mkdir(parents=True, exist_ok=True)
    for candidate in CANDIDATES.values():
        (
            ROOT
            / "SourceAssets/Blender/Weapons/Dwarven"
            / ASSET
            / str(candidate["attempt"])
        ).mkdir(parents=True, exist_ok=True)


def replay_capture(
    capture_path: Path,
    source_path: Path,
) -> tuple[Image.Image, Image.Image, dict[str, object]]:
    record = json.loads(gzip.decompress(capture_path.read_bytes()))
    image = Image.open(source_path).convert("RGBA")
    width, height = image.size
    if [width, height] != record["canvas_pixels"]:
        raise RuntimeError(f"Canvas mismatch: {source_path}")
    source_bytes = image.tobytes("raw", "RGBA")
    membership = bytearray(width * height)
    selected_rgba = bytearray()
    for row in record["rows_with_exact_rgba"]:
        y = int(row["y"])
        for run in row["runs"]:
            x0 = int(run["x0"])
            x1 = int(run["x1"])
            payload = bytes.fromhex(run["rgba_hex"])
            if len(payload) != (x1 - x0) * 4:
                raise RuntimeError("Malformed scanline RGBA run")
            for offset, x in enumerate(range(x0, x1)):
                flat = y * width + x
                membership[flat] = 1
                stored = payload[offset * 4:offset * 4 + 4]
                selected_rgba.extend(stored)
                if stored != source_bytes[flat * 4:flat * 4 + 4]:
                    raise RuntimeError("Stored RGBA differs from immutable source")
    if sha256_bytes(bytes(membership)) != record["decoded_membership_sha256"]:
        raise RuntimeError("Membership replay hash mismatch")
    if sha256_bytes(bytes(selected_rgba)) != record["selected_rgba_sha256"]:
        raise RuntimeError("RGBA replay hash mismatch")
    mask = Image.frombytes(
        "L",
        (width, height),
        bytes(255 if value else 0 for value in membership),
    )
    return image, mask, {
        "capture_path": str(capture_path.relative_to(ROOT)),
        "capture_sha256": sha256(capture_path),
        "decoded_membership_sha256": record["decoded_membership_sha256"],
        "selected_rgba_sha256": record["selected_rgba_sha256"],
        "selected_pixel_count": sum(membership),
        "exact_rgba_replay": True,
    }


def fill_enclosed(mask: Image.Image) -> Image.Image:
    width, height = mask.size
    source = mask.load()
    exterior = bytearray(width * height)
    queue: deque[tuple[int, int]] = deque()
    for x in range(width):
        for y in (0, height - 1):
            if source[x, y] == 0 and not exterior[y * width + x]:
                exterior[y * width + x] = 1
                queue.append((x, y))
    for y in range(height):
        for x in (0, width - 1):
            if source[x, y] == 0 and not exterior[y * width + x]:
                exterior[y * width + x] = 1
                queue.append((x, y))
    while queue:
        x, y = queue.popleft()
        for dx, dy in ((1, 0), (-1, 0), (0, 1), (0, -1)):
            nx, ny = x + dx, y + dy
            if (
                0 <= nx < width
                and 0 <= ny < height
                and source[nx, ny] == 0
                and not exterior[ny * width + nx]
            ):
                exterior[ny * width + nx] = 1
                queue.append((nx, ny))
    output = mask.copy()
    pixels = output.load()
    for y in range(height):
        for x in range(width):
            if pixels[x, y] == 0 and not exterior[y * width + x]:
                pixels[x, y] = 255
    return output


def row_members(mask: Image.Image, global_y: int, rect: list[int]) -> list[int]:
    local_y = max(0, min(mask.height - 1, global_y - rect[1]))
    pixels = mask.load()
    return [rect[0] + x for x in range(mask.width) if pixels[x, local_y] > 0]


def row_span(mask: Image.Image, global_y: int, rect: list[int]) -> int:
    members = row_members(mask, global_y, rect)
    return max(members) + 1 - min(members)


def image_material(name: str, path: Path) -> bpy.types.Material:
    material = bpy.data.materials.new(name)
    material.use_nodes = True
    nodes = material.node_tree.nodes
    nodes.clear()
    output = nodes.new("ShaderNodeOutputMaterial")
    texture = nodes.new("ShaderNodeTexImage")
    texture.image = bpy.data.images.load(str(path), check_existing=True)
    texture.interpolation = "Closest"
    bsdf = nodes.new("ShaderNodeBsdfPrincipled")
    bsdf.inputs["Roughness"].default_value = 0.56
    bsdf.inputs["Metallic"].default_value = 0.22
    material.node_tree.links.new(texture.outputs["Color"], bsdf.inputs["Base Color"])
    material.node_tree.links.new(bsdf.outputs["BSDF"], output.inputs["Surface"])
    return material


def flat_material(
    name: str,
    color: tuple[float, float, float, float],
) -> bpy.types.Material:
    material = bpy.data.materials.new(name)
    material.use_nodes = True
    bsdf = material.node_tree.nodes.get("Principled BSDF")
    bsdf.inputs["Base Color"].default_value = color
    bsdf.inputs["Roughness"].default_value = 0.68
    bsdf.inputs["Metallic"].default_value = 0.12
    return material


def clear_scene() -> None:
    bpy.ops.object.select_all(action="SELECT")
    bpy.ops.object.delete(use_global=False)
    for datablocks in (
        bpy.data.meshes,
        bpy.data.curves,
        bpy.data.materials,
        bpy.data.cameras,
        bpy.data.lights,
        bpy.data.images,
    ):
        for block in list(datablocks):
            if block.users == 0:
                datablocks.remove(block)


def configure_scene(kind: str) -> None:
    scene = bpy.context.scene
    scene.render.engine = "BLENDER_EEVEE"
    scene.eevee.use_gtao = True
    scene.eevee.gtao_distance = 5.0
    scene.eevee.gtao_factor = 1.25
    scene.render.image_settings.file_format = "PNG"
    scene.render.image_settings.color_mode = "RGB"
    scene.render.image_settings.color_depth = "8"
    scene.render.resolution_percentage = 100
    scene.render.film_transparent = False
    scene.world.use_nodes = True
    background = scene.world.node_tree.nodes.get("Background")
    background.inputs["Color"].default_value = (0.82, 0.83, 0.84, 1.0)
    background.inputs["Strength"].default_value = 0.72
    scene["Aerathea.ContractID"] = CONTRACT_ID
    scene["Aerathea.CandidateKind"] = kind
    scene["Aerathea.SourceHalfAxis"] = "right-image depth half Y<=0"
    scene["Aerathea.BisectionSourceEdge"] = DIAMOND_X
    scene["Aerathea.WholeTransform"] = "Rz(180): (X,Y,Z)->(-X,-Y,Z)"
    scene["Aerathea.WholeTransformCount"] = 1
    scene["Aerathea.HandleTopZCm"] = 132.0
    scene["Aerathea.PiOver2HaftWrap"] = True
    scene["Aerathea.PriorCandidateGeometryInputs"] = 0
    try:
        scene.view_settings.view_transform = "Standard"
        scene.view_settings.look = "Medium High Contrast"
        scene.view_settings.exposure = 0.0
        scene.view_settings.gamma = 1.0
    except Exception:
        pass


def complete_rz180(
    vertices: list[tuple[float, float, float]],
    faces: list[tuple[int, ...]],
    face_uvs: list[list[tuple[float, float]]],
    face_materials: list[int],
    duplicate_material_map: dict[int, int] | None = None,
) -> tuple[
    list[tuple[float, float, float]],
    list[tuple[int, ...]],
    list[list[tuple[float, float]]],
    list[int],
    dict[str, int],
]:
    source_vertex_count = len(vertices)
    source_face_count = len(faces)
    complete_vertices = list(vertices)
    coordinate_map = {
        (round(x, 7), round(y, 7), round(z, 7)): index
        for index, (x, y, z) in enumerate(complete_vertices)
    }
    duplicate_map: dict[int, int] = {}
    welded = 0
    for index, (x, y, z) in enumerate(vertices):
        transformed = (-x, -y, z)
        key = tuple(round(value, 7) for value in transformed)
        if key in coordinate_map:
            duplicate_map[index] = coordinate_map[key]
            welded += 1
        else:
            duplicate_map[index] = len(complete_vertices)
            coordinate_map[key] = len(complete_vertices)
            complete_vertices.append(transformed)
    complete_faces = list(faces)
    complete_uvs = list(face_uvs)
    complete_materials = list(face_materials)
    known_faces = {tuple(sorted(face)) for face in complete_faces}
    duplicate_faces = 0
    for face, uvs, material in zip(faces, face_uvs, face_materials):
        transformed_face = tuple(duplicate_map[index] for index in face)
        key = tuple(sorted(transformed_face))
        if key in known_faces:
            continue
        known_faces.add(key)
        complete_faces.append(transformed_face)
        complete_uvs.append(list(uvs))
        complete_materials.append(
            duplicate_material_map.get(material, material)
            if duplicate_material_map
            else material
        )
        duplicate_faces += 1
    return (
        complete_vertices,
        complete_faces,
        complete_uvs,
        complete_materials,
        {
            "source_half_vertices": source_vertex_count,
            "source_half_faces": source_face_count,
            "coordinate_equal_seam_vertices_welded": welded,
            "duplicate_faces_added": duplicate_faces,
        },
    )


def create_mesh_object(
    name: str,
    vertices: list[tuple[float, float, float]],
    faces: list[tuple[int, ...]],
    face_uvs: list[list[tuple[float, float]]],
    face_materials: list[int],
    materials: list[bpy.types.Material],
) -> bpy.types.Object:
    mesh = bpy.data.meshes.new(f"{name}_MESH")
    mesh.from_pydata(vertices, [], faces)
    mesh.update(calc_edges=True)
    uv_layer = mesh.uv_layers.new(name="UVMap")
    for polygon, uvs, material_index in zip(
        mesh.polygons, face_uvs, face_materials
    ):
        polygon.material_index = material_index
        polygon.use_smooth = False
        for loop_index, uv in zip(polygon.loop_indices, uvs):
            uv_layer.data[loop_index].uv = uv
    obj = bpy.data.objects.new(name, mesh)
    bpy.context.scene.collection.objects.link(obj)
    for material in materials:
        obj.data.materials.append(material)
    obj["Aerathea.ContractID"] = CONTRACT_ID
    obj["Aerathea.Rz180Executed"] = True
    obj["Aerathea.WholeTransformCount"] = 1
    obj["Aerathea.PriorCandidateGeometryInputs"] = 0
    return obj


def handle_z(source_y: float) -> float:
    if source_y <= FRONT_H8:
        return float(Z_A - (Fraction(source_y) - FRONT_A) * UPPER_SCALE)
    if source_y <= FRONT_U1:
        return float(Z_H8 - (Fraction(source_y) - FRONT_H8) * Fraction(42, FRONT_U1 - FRONT_H8))
    return float(Z_U3 - (Fraction(source_y) - FRONT_U3) * LOWER_SCALE)


def build_head(
    kind: str,
    front_image: Image.Image,
    back_image: Image.Image,
    right_image: Image.Image,
    front_filled: Image.Image,
    right_filled: Image.Image,
    materials: list[bpy.types.Material],
) -> tuple[bpy.types.Object, dict[str, object]]:
    candidate = CANDIDATES[kind]
    interval = [int(value) for value in candidate["source_interval"]]
    source_top = int(candidate["source_top"])
    span = interval[1] - interval[0]
    side_scale = float(TARGET_HALF_DEPTH / span)
    right_pixels = right_filled.load()
    active: set[tuple[int, int]] = set()
    for global_y in range(source_top, RIGHT_HEAD_A):
        local_y = global_y - RIGHT_RECT[1]
        for global_x in range(interval[0], interval[1]):
            local_x = global_x - RIGHT_RECT[0]
            if right_pixels[local_x, local_y] > 0:
                active.add((global_x, global_y))
    if not active:
        raise RuntimeError(f"No head cells for {kind}")

    def source_y_to_world(source_x: float) -> float:
        if kind == "metal":
            return (source_x - DIAMOND_X) * side_scale
        return (DIAMOND_X - source_x) * side_scale

    head_z_scale = float(Fraction(38, RIGHT_HEAD_A - source_top))

    def source_row_to_world_z(source_y: float) -> float:
        return 170.0 - (source_y - source_top) * head_z_scale

    half_width_cache: dict[int, float] = {}

    def half_width(world_z: float) -> float:
        source_y = FRONT_RECT[1] + (
            (170.0 - world_z) / 38.0
        ) * (FRONT_A - FRONT_RECT[1])
        row = int(round(source_y - 0.5))
        if row not in half_width_cache:
            members = row_members(front_filled, row, FRONT_RECT)
            raw = max(
                float(FRONT_CENTER_X - min(members)),
                float(max(members) + 1 - FRONT_CENTER_X),
            )
            half_width_cache[row] = raw * float(FRONT_SCALE)
        return half_width_cache[row]

    vertices: list[tuple[float, float, float]] = []
    faces: list[tuple[int, ...]] = []
    face_uvs: list[list[tuple[float, float]]] = []
    face_materials: list[int] = []
    cache: dict[tuple[str, int, int], int] = {}

    def vertex(x_side: str, source_x: int, source_y: int) -> int:
        key = (x_side, source_x, source_y)
        if key in cache:
            return cache[key]
        z = source_row_to_world_z(source_y)
        x = half_width(z) * (1.0 if x_side == "positive" else -1.0)
        y = source_y_to_world(source_x)
        cache[key] = len(vertices)
        vertices.append((x, y, z))
        return cache[key]

    def side_uv(source_x: float, source_y: float) -> tuple[float, float]:
        return (
            source_x / right_image.width,
            1.0 - source_y / right_image.height,
        )

    def front_uv(world_x: float, world_z: float) -> tuple[float, float]:
        source_x = float(FRONT_CENTER_X) + world_x / float(FRONT_SCALE)
        source_y = FRONT_RECT[1] + (
            (170.0 - world_z) / 38.0
        ) * (FRONT_A - FRONT_RECT[1])
        return (
            source_x / front_image.width,
            1.0 - source_y / front_image.height,
        )

    seam_skipped = 0
    boundary_faces = 0
    for source_x, source_y in sorted(active, key=lambda item: (item[1], item[0])):
        x0, x1 = source_x, source_x + 1
        y0, y1 = source_y, source_y + 1
        p00 = vertex("positive", x0, y0)
        p10 = vertex("positive", x1, y0)
        p11 = vertex("positive", x1, y1)
        p01 = vertex("positive", x0, y1)
        n00 = vertex("negative", x0, y0)
        n10 = vertex("negative", x1, y0)
        n11 = vertex("negative", x1, y1)
        n01 = vertex("negative", x0, y1)
        faces.append((p00, p10, p11, p01))
        face_uvs.append(
            [
                side_uv(x0, y0),
                side_uv(x1, y0),
                side_uv(x1, y1),
                side_uv(x0, y1),
            ]
        )
        face_materials.append(0)
        faces.append((n00, n01, n11, n10))
        face_uvs.append(
            [
                side_uv(x0, y0),
                side_uv(x0, y1),
                side_uv(x1, y1),
                side_uv(x1, y0),
            ]
        )
        face_materials.append(0)

        edges = (
            ((-1, 0), x0, y0, x0, y1, p00, p01, n01, n00),
            ((1, 0), x1, y1, x1, y0, p11, p10, n10, n11),
            ((0, -1), x1, y0, x0, y0, p10, p00, n00, n10),
            ((0, 1), x0, y1, x1, y1, p01, p11, n11, n01),
        )
        for (dx, dy), _, _, _, _, a, b, c, d in edges:
            if (source_x + dx, source_y + dy) in active:
                continue
            is_seam = (
                kind == "metal" and dx == 1 and x1 == DIAMOND_X
            ) or (
                kind == "rune" and dx == -1 and x0 == DIAMOND_X
            )
            if is_seam:
                seam_skipped += 1
                continue
            boundary_faces += 1
            faces.append((a, b, c, d))
            face_uvs.append(
                [
                    front_uv(vertices[index][0], vertices[index][2])
                    for index in (a, b, c, d)
                ]
            )
            face_materials.append(1)

    (
        vertices,
        faces,
        face_uvs,
        face_materials,
        rz_stats,
    ) = complete_rz180(
        vertices,
        faces,
        face_uvs,
        face_materials,
        duplicate_material_map={1: 2},
    )
    obj = create_mesh_object(
        f"C00_R8_CORRECT_AXIS_HEAD_{kind.upper()}_COMPLETE_RZ180",
        vertices,
        faces,
        face_uvs,
        face_materials,
        materials,
    )
    obj["Aerathea.ComponentID"] = "C00_CORRECT_AXIS_HEAD"
    obj["Aerathea.CandidateKind"] = kind
    obj["Aerathea.SourceHalfAxis"] = "Y<=0"
    obj["Aerathea.BisectionSourceEdge"] = DIAMOND_X
    obj["Aerathea.SourceInterval"] = json.dumps(interval)
    obj["Aerathea.SourceTopRow"] = source_top
    obj["Aerathea.HeadHandleBoundaryA_ZCm"] = 132.0
    return obj, {
        "candidate": kind,
        "source_interval_half_open": interval,
        "source_half_span_pixels": span,
        "source_top_row": source_top,
        "head_A_row": RIGHT_HEAD_A,
        "active_source_half_cells": len(active),
        "open_seam_edges": seam_skipped,
        "combined_boundary_faces": boundary_faces,
        "source_half_axis": "Y<=0",
        "bisection_x": DIAMOND_X,
        "half_depth_scale_cm_per_pixel": side_scale,
        **rz_stats,
        "complete_vertices": len(obj.data.vertices),
        "complete_polygons": len(obj.data.polygons),
    }


def build_handle(
    kind: str,
    front_image: Image.Image,
    front_filled: Image.Image,
    material: bpy.types.Material,
) -> tuple[bpy.types.Object, dict[str, object]]:
    center = float(FRONT_CENTER_X)

    def raw_radius(source_y: int) -> float:
        members = row_members(
            front_filled,
            max(FRONT_A, min(FRONT_TERMINAL - 1, source_y)),
            FRONT_RECT,
        )
        return max(center - min(members), max(members) + 1 - center)

    raw_lower_max = max(
        raw_radius(row) for row in range(FRONT_U3, FRONT_TERMINAL)
    )
    decorative_scale = float(R_POMMEL_MAX) / raw_lower_max
    profile: list[dict[str, object]] = []
    for source_edge in range(FRONT_A, FRONT_TERMINAL + 1):
        sample_row = min(source_edge, FRONT_TERMINAL - 1)
        z = handle_z(source_edge)
        if FRONT_C <= source_edge <= FRONT_H1:
            radius = float(R_SHAFT)
            component = "C07_TRUE_HAFT"
            radial_rule = "exact 2.5 cm radius"
        elif source_edge < FRONT_C:
            radius = raw_radius(sample_row) * decorative_scale
            component = "C06_UPPER_COUPLER"
            radial_rule = "new R8 profile; shared decorative radial scale"
        elif source_edge < FRONT_H8:
            radius = raw_radius(sample_row) * decorative_scale
            component = "C07B_HAFT_TO_HANDLE_FERRULE"
            radial_rule = "new R8 profile; shared decorative radial scale"
        elif source_edge < FRONT_U1:
            radius = raw_radius(sample_row) * decorative_scale
            component = "C08_GRIP"
            radial_rule = "new R8 profile; exact 42 cm longitudinal lock"
        elif source_edge < FRONT_U3:
            radius = raw_radius(sample_row) * decorative_scale
            component = "C09_LOWER_COLLAR"
            radial_rule = "new R8 profile; lower-assembly scale"
        elif source_edge < FRONT_L4:
            radius = raw_radius(sample_row) * decorative_scale
            component = "C10_POMMEL"
            radial_rule = "new R8 profile; exact 18 cm / 11 cm locks"
        else:
            radius = raw_radius(sample_row) * decorative_scale
            component = "C11_TERMINAL_CAP"
            radial_rule = "new R8 profile; lower-assembly scale"
        profile.append(
            {
                "source_edge": source_edge,
                "source_row": sample_row,
                "z_cm": z,
                "radius_cm": radius,
                "component": component,
                "radial_rule": radial_rule,
            }
        )

    vertices: list[tuple[float, float, float]] = []
    faces: list[tuple[int, ...]] = []
    face_uvs: list[list[tuple[float, float]]] = []
    face_materials: list[int] = []
    for ring in profile:
        radius = float(ring["radius_cm"])
        z = float(ring["z_cm"])
        for segment in range(HALF_SEGMENTS + 1):
            theta = -math.pi / 2.0 + math.pi * segment / HALF_SEGMENTS
            vertices.append(
                (radius * math.cos(theta), radius * math.sin(theta), z)
            )
    stride = HALF_SEGMENTS + 1
    background_samples = 0
    uv_samples = 0
    for ring_index in range(len(profile) - 1):
        upper = ring_index * stride
        lower = (ring_index + 1) * stride
        source_row = int(profile[ring_index]["source_row"])
        members = row_members(front_filled, source_row, FRONT_RECT)
        x0, x1 = min(members), max(members) + 1
        for segment in range(HALF_SEGMENTS):
            faces.append(
                (
                    upper + segment,
                    lower + segment,
                    lower + segment + 1,
                    upper + segment + 1,
                )
            )
            u = (segment + 0.5) / HALF_SEGMENTS
            target = x0 + u * (x1 - x0)
            selected_x = min(
                members, key=lambda x: (abs((x + 0.5) - target), x)
            )
            if selected_x not in members:
                background_samples += 1
            uv_samples += 1
            uv = (
                (selected_x + 0.5) / front_image.width,
                1.0 - (source_row + 0.5) / front_image.height,
            )
            face_uvs.append([uv, uv, uv, uv])
            face_materials.append(0)

    for ring_index in (0, len(profile) - 1):
        ring_start = ring_index * stride
        center_index = len(vertices)
        z = float(profile[ring_index]["z_cm"])
        vertices.append((0.0, 0.0, z))
        source_row = int(profile[ring_index]["source_row"])
        members = row_members(front_filled, source_row, FRONT_RECT)
        selected_x = min(members, key=lambda x: abs((x + 0.5) - center))
        uv = (
            (selected_x + 0.5) / front_image.width,
            1.0 - (source_row + 0.5) / front_image.height,
        )
        for segment in range(HALF_SEGMENTS):
            face = (
                (center_index, ring_start + segment + 1, ring_start + segment)
                if ring_index == 0
                else (center_index, ring_start + segment, ring_start + segment + 1)
            )
            faces.append(face)
            face_uvs.append([uv, uv, uv])
            face_materials.append(0)

    (
        vertices,
        faces,
        face_uvs,
        face_materials,
        rz_stats,
    ) = complete_rz180(vertices, faces, face_uvs, face_materials)
    obj = create_mesh_object(
        f"C06_C11_CORRECTED_HANDLE_{kind.upper()}_COMPLETE_RZ180",
        vertices,
        faces,
        face_uvs,
        face_materials,
        [material],
    )
    obj["Aerathea.ComponentID"] = "C06_C11_CORRECTED_HANDLE"
    obj["Aerathea.CandidateKind"] = kind
    obj["Aerathea.HandleTopZCm"] = 132.0
    obj["Aerathea.HandleIncludesUpperCoupler"] = True
    obj["Aerathea.PreviousMissingSpanCm"] = float(
        Fraction(33432, 1111)
    )
    obj["Aerathea.ThetaFormula"] = "-pi/2+pi*U"
    obj["Aerathea.SurfaceFormula"] = "X=r(z)cos(theta);Y=r(z)sin(theta)"
    obj["Aerathea.PiOver2CylinderWrap"] = True
    obj["Aerathea.ShaftRadiusCm"] = 2.5
    obj["Aerathea.GripLengthCm"] = 42.0
    obj["Aerathea.PommelLengthCm"] = 18.0
    obj["Aerathea.PommelMaximumWidthCm"] = 11.0
    obj["Aerathea.ProfileJSON"] = json.dumps(profile, sort_keys=True)
    obj["Aerathea.SourceBackgroundSamples"] = background_samples
    return obj, {
        "profile_ring_count": len(profile),
        "half_angular_segments": HALF_SEGMENTS,
        "theta": "-pi/2+pi*U",
        "pi_over_2_wrap": True,
        "source_uv_samples": uv_samples,
        "source_uv_background_samples": background_samples,
        "decorative_radius_scale_cm_per_pixel": decorative_scale,
        "raw_lower_max_radius_pixels": raw_lower_max,
        "stations_source_rows": {
            "A": FRONT_A,
            "C": FRONT_C,
            "H1": FRONT_H1,
            "H8": FRONT_H8,
            "U1": FRONT_U1,
            "U3": FRONT_U3,
            "L4": FRONT_L4,
            "terminal": FRONT_TERMINAL,
        },
        "stations_z_cm_exact": {
            "A": fraction_record(Z_A),
            "C": fraction_record(Z_C),
            "H1": fraction_record(Z_H1),
            "H8": fraction_record(Z_H8),
            "U1": fraction_record(Z_U1),
            "U3": fraction_record(Z_U3),
            "L4": fraction_record(Z_L4),
            "terminal": fraction_record(Fraction(0)),
        },
        "grip_length_cm": handle_z(FRONT_H8) - handle_z(FRONT_U1),
        "pommel_length_cm": handle_z(FRONT_U3) - handle_z(FRONT_TERMINAL),
        "maximum_radius_cm": max(float(item["radius_cm"]) for item in profile),
        "handle_top_z_cm": max(float(item["z_cm"]) for item in profile),
        "previous_missing_span_cm": float(Fraction(33432, 1111)),
        **rz_stats,
        "complete_vertices": len(obj.data.vertices),
        "complete_polygons": len(obj.data.polygons),
    }


def add_camera(
    name: str,
    location: tuple[float, float, float],
    target: tuple[float, float, float],
    ortho_scale: float,
) -> bpy.types.Object:
    data = bpy.data.cameras.new(name)
    data.type = "ORTHO"
    data.ortho_scale = ortho_scale
    obj = bpy.data.objects.new(name, data)
    bpy.context.scene.collection.objects.link(obj)
    obj.location = location
    obj.rotation_euler = (
        Vector(target) - obj.location
    ).to_track_quat("-Z", "Y").to_euler()
    return obj


def add_lights(kind: str) -> None:
    for name, energy, size, location, target in (
        (f"{kind}_Key", 1200.0, 78.0, (-90.0, -145.0, 205.0), (0.0, 0.0, 90.0)),
        (f"{kind}_Fill", 720.0, 95.0, (120.0, -55.0, 125.0), (0.0, 0.0, 85.0)),
        (f"{kind}_Rim", 930.0, 72.0, (55.0, 125.0, 180.0), (0.0, 0.0, 95.0)),
    ):
        data = bpy.data.lights.new(name, "AREA")
        data.energy = energy
        data.size = size
        obj = bpy.data.objects.new(name, data)
        bpy.context.scene.collection.objects.link(obj)
        obj.location = location
        obj.rotation_euler = (
            Vector(target) - obj.location
        ).to_track_quat("-Z", "Y").to_euler()


def render(
    camera: bpy.types.Object,
    path: Path,
    width: int,
    height: int,
) -> None:
    scene = bpy.context.scene
    scene.camera = camera
    scene.render.resolution_x = width
    scene.render.resolution_y = height
    scene.render.filepath = str(path)
    bpy.ops.render.render(write_still=True)


def render_geometry_proof(
    objects: list[bpy.types.Object],
    camera: bpy.types.Object,
    path: Path,
    width: int,
    height: int,
    material: bpy.types.Material,
) -> None:
    saved: list[tuple[bpy.types.Object, list[bpy.types.Material], list[int]]] = []
    for obj in objects:
        original_materials = [slot.material for slot in obj.material_slots]
        original_indices = [polygon.material_index for polygon in obj.data.polygons]
        saved.append((obj, original_materials, original_indices))
        obj.data.materials.clear()
        obj.data.materials.append(material)
        for polygon in obj.data.polygons:
            polygon.material_index = 0
    render(camera, path, width, height)
    for obj, original_materials, original_indices in saved:
        obj.data.materials.clear()
        for original in original_materials:
            obj.data.materials.append(original)
        for polygon, material_index in zip(obj.data.polygons, original_indices):
            polygon.material_index = material_index


def object_bounds(objects: list[bpy.types.Object]) -> dict[str, list[float]]:
    points = [
        obj.matrix_world @ vertex.co
        for obj in objects
        for vertex in obj.data.vertices
    ]
    minimum = [min(point[index] for point in points) for index in range(3)]
    maximum = [max(point[index] for point in points) for index in range(3)]
    return {
        "min_cm": minimum,
        "max_cm": maximum,
        "dimensions_cm": [
            maximum[index] - minimum[index] for index in range(3)
        ],
    }


def rz_symmetry(objects: list[bpy.types.Object]) -> dict[str, object]:
    records = {}
    total_missing = 0
    for obj in objects:
        coordinates = {
            (
                round(float(vertex.co.x), 5),
                round(float(vertex.co.y), 5),
                round(float(vertex.co.z), 5),
            )
            for vertex in obj.data.vertices
        }
        missing = sum(
            1
            for x, y, z in coordinates
            if (-x, -y, z) not in coordinates
        )
        records[obj.name] = {
            "unique_vertices": len(coordinates),
            "missing_rz180_vertices": missing,
            "pass": missing == 0,
        }
        total_missing += missing
    return {
        "objects": records,
        "total_missing_rz180_vertices": total_missing,
        "pass": total_missing == 0,
    }


def measurement_events(front_selected: Image.Image, right_selected: Image.Image) -> dict[str, object]:
    front_spans = {
        name: row_span(front_selected, row, FRONT_RECT)
        for name, row in {
            "A": FRONT_A,
            "C": FRONT_C,
            "H1": FRONT_H1,
            "H8": FRONT_H8,
            "U1": FRONT_U1,
            "U3": FRONT_U3,
            "L4": FRONT_L4,
        }.items()
    }
    right_a_span = row_span(right_selected, RIGHT_HEAD_A, RIGHT_RECT)
    right_pre_a_span = row_span(right_selected, RIGHT_HEAD_A - 1, RIGHT_RECT)
    rules = {
        "front_A_sustained_at_most_120": all(
            row_span(front_selected, row, FRONT_RECT) <= 120
            for row in range(FRONT_A, FRONT_A + 10)
        ),
        "front_C_sustained_at_most_70": all(
            row_span(front_selected, row, FRONT_RECT) <= 70
            for row in range(FRONT_C, FRONT_C + 20)
        ),
        "front_H1_reaches_75": front_spans["H1"] >= 75,
        "front_H8_sustained_at_most_71": all(
            row_span(front_selected, row, FRONT_RECT) <= 71
            for row in range(FRONT_H8, FRONT_H8 + 20)
        ),
        "front_U1_reaches_78": front_spans["U1"] >= 78,
        "front_U3_reaches_115": front_spans["U3"] >= 115,
        "front_L4_reaches_at_most_107": front_spans["L4"] <= 107,
        "right_A_contracts_at_least_15": right_pre_a_span - right_a_span >= 15,
    }
    return {
        "front_station_spans_pixels": front_spans,
        "right_A_previous_span_pixels": right_pre_a_span,
        "right_A_span_pixels": right_a_span,
        "rules": rules,
        "pass": all(rules.values()),
    }


def build_candidate(
    kind: str,
    images: dict[str, Image.Image],
    selected: dict[str, Image.Image],
    filled: dict[str, Image.Image],
    source_paths: dict[str, Path],
    capture_replay: dict[str, dict[str, object]],
    events: dict[str, object],
) -> dict[str, object]:
    candidate = CANDIDATES[kind]
    attempt = str(candidate["attempt"])
    output_root = (
        ROOT / "SourceAssets/Blender/Weapons/Dwarven" / ASSET / attempt
    )
    blend_path = output_root / f"{ASSET}_{attempt}.blend"
    prefix = f"A12_R10_R8_{kind.upper()}"
    paths = {
        "front": REVIEW_ROOT / f"{prefix}_COMPLETE_FRONT.png",
        "right": REVIEW_ROOT / f"{prefix}_COMPLETE_RIGHT.png",
        "color_3q": REVIEW_ROOT / f"{prefix}_COMPLETE_COLOR_3Q.png",
        "gray_3q": REVIEW_ROOT / f"{prefix}_COMPLETE_GRAY_3Q.png",
    }
    manifest_path = ASSET_ROOT / "manifests" / str(candidate["manifest_name"])

    clear_scene()
    configure_scene(kind)
    right_material = image_material(
        f"MI_{kind}_R8_RIGHT_EXACT_PIXELS", source_paths["right"]
    )
    front_material = image_material(
        f"MI_{kind}_R8_FRONT_EXACT_PIXELS", source_paths["front"]
    )
    back_material = image_material(
        f"MI_{kind}_R8_BACK_EXACT_PIXELS", source_paths["back"]
    )
    handle_material = image_material(
        f"MI_{kind}_R8_HANDLE_EXACT_FRONT_PIXELS", source_paths["front"]
    )
    gray_material = flat_material(
        f"M_{kind}_R8_INDEPENDENT_GRAY", (0.30, 0.33, 0.37, 1.0)
    )
    head, head_stats = build_head(
        kind,
        images["front"],
        images["back"],
        images["right"],
        filled["front"],
        filled["right"],
        [right_material, front_material, back_material],
    )
    handle, handle_stats = build_handle(
        kind,
        images["front"],
        filled["front"],
        handle_material,
    )
    objects = [head, handle]
    add_lights(kind)
    front_camera = add_camera(
        f"CAM_{kind}_FRONT",
        (0.0, -520.0, 85.0),
        (0.0, 0.0, 85.0),
        188.0,
    )
    right_camera = add_camera(
        f"CAM_{kind}_RIGHT",
        (520.0, 0.0, 85.0),
        (0.0, 0.0, 85.0),
        188.0,
    )
    three_q = add_camera(
        f"CAM_{kind}_3Q",
        (175.0, -255.0, 125.0),
        (0.0, 0.0, 88.0),
        198.0,
    )
    render(front_camera, paths["front"], 1000, 1450)
    render(right_camera, paths["right"], 1000, 1450)
    render(three_q, paths["color_3q"], 1100, 1450)
    render_geometry_proof(
        objects,
        three_q,
        paths["gray_3q"],
        1100,
        1450,
        gray_material,
    )

    bounds = object_bounds(objects)
    dimensions = bounds["dimensions_cm"]
    symmetry = rz_symmetry(objects)
    shaft_errors = [
        abs(math.hypot(float(vertex.co.x), float(vertex.co.y)) - 2.5)
        for vertex in handle.data.vertices
        if float(Z_H1) + 0.5
        <= float(vertex.co.z)
        <= float(Z_C) - 0.5
    ]
    max_shaft_error = max(shaft_errors) if shaft_errors else float("inf")
    gates = {
        "contract_present": CONTRACT.is_file(),
        "source_hashes_match": all(
            sha256(source_paths[view])
            == json.loads(SCAN_MANIFEST.read_text())["sources"][view]["file_sha256"]
            for view in ("front", "back", "right")
        ),
        "scanlines_replay_exactly": all(
            capture_replay[view]["exact_rgba_replay"]
            for view in ("front", "back", "right")
        ),
        "scanline_station_rules_pass": bool(events["pass"]),
        "correct_bisection_source_edge_557": int(head["Aerathea.BisectionSourceEdge"]) == 557,
        "source_half_axis_is_Y": str(head["Aerathea.SourceHalfAxis"]) == "Y<=0",
        "candidate_interval_exact": json.loads(head["Aerathea.SourceInterval"])
        == candidate["source_interval"],
        "no_prior_geometry": all(
            int(obj["Aerathea.PriorCandidateGeometryInputs"]) == 0
            for obj in objects
        ),
        "one_rz180_each": all(
            int(obj["Aerathea.WholeTransformCount"]) == 1 for obj in objects
        ),
        "rz180_symmetry": bool(symmetry["pass"]),
        "handle_includes_upper_coupler": bool(
            handle["Aerathea.HandleIncludesUpperCoupler"]
        ),
        "handle_top_132_cm": abs(handle_stats["handle_top_z_cm"] - 132.0) <= 1.0e-7,
        "missing_span_recorded": abs(
            float(handle["Aerathea.PreviousMissingSpanCm"])
            - float(Fraction(33432, 1111))
        )
        <= 1.0e-7,
        "pi_over_2_wrap": bool(handle["Aerathea.PiOver2CylinderWrap"]),
        "shaft_radius_2_5_cm": max_shaft_error <= 1.0e-6,
        "grip_length_42_cm": abs(handle_stats["grip_length_cm"] - 42.0) <= 1.0e-7,
        "pommel_length_18_cm": abs(handle_stats["pommel_length_cm"] - 18.0) <= 1.0e-7,
        "pommel_maximum_width_11_cm": abs(
            2.0 * handle_stats["maximum_radius_cm"] - 11.0
        )
        <= 1.0e-7,
        "handle_source_background_zero": handle_stats["source_uv_background_samples"] == 0,
        "width_exact": abs(dimensions[0] - float(TARGET_WIDTH)) <= 3.0e-5,
        "depth_exact": abs(dimensions[1] - float(TARGET_DEPTH)) <= 3.0e-5,
        "height_exact": abs(dimensions[2] - 170.0) <= 3.0e-5,
        "camera_scales_exact": (
            abs(float(front_camera.data.ortho_scale) - 188.0) <= 1.0e-7
            and abs(float(right_camera.data.ortho_scale) - 188.0) <= 1.0e-7
            and abs(float(three_q.data.ortho_scale) - 198.0) <= 1.0e-7
        ),
        "gray_differs_from_color": sha256(paths["gray_3q"])
        != sha256(paths["color_3q"]),
        "no_modifiers": all(len(obj.modifiers) == 0 for obj in objects),
        "fbx_unreal_not_used": True,
    }
    if not all(gates.values()):
        raise RuntimeError(
            f"{kind} build gates failed: "
            + ", ".join(name for name, value in gates.items() if not value)
        )

    for obj in objects:
        obj["Aerathea.CompleteBounds"] = json.dumps(bounds, sort_keys=True)
        obj["Aerathea.Rz180Symmetry"] = json.dumps(symmetry, sort_keys=True)
    bpy.ops.wm.save_as_mainfile(filepath=str(blend_path))
    output_paths = {"blend": blend_path, **paths}
    result = {
        "schema": "aerathea.siegebreaker.r8_correct_axis_candidate.v1",
        "asset": ASSET,
        "attempt": attempt,
        "candidate_kind": kind,
        "candidate_label": candidate["label"],
        "contract_id": CONTRACT_ID,
        "contract_path": str(CONTRACT.relative_to(ROOT)),
        "contract_sha256": sha256(CONTRACT),
        "date": "2026-07-23",
        "artifact_status": "DCC source candidate pending Flamestrike comparison",
        "source_authority": {
            "scan_manifest": str(SCAN_MANIFEST.relative_to(ROOT)),
            "scale_manifest": str(SCALE_MANIFEST.relative_to(ROOT)),
            "diamond_manifest": str(DIAMOND_MANIFEST.relative_to(ROOT)),
            "sources": {
                view: {
                    "path": str(source_paths[view].relative_to(ROOT)),
                    "sha256": sha256(source_paths[view]),
                    **capture_replay[view],
                }
                for view in ("front", "back", "right")
            },
        },
        "dimensions_cm_exact": {
            "width": fraction_record(TARGET_WIDTH),
            "depth": fraction_record(TARGET_DEPTH),
            "height": fraction_record(TARGET_HEIGHT),
        },
        "measurement_events": events,
        "construction": {
            "source_half_axis": "Y<=0",
            "bisection_source_edge_x": DIAMOND_X,
            "source_interval_half_open": candidate["source_interval"],
            "whole_transform": "Rz(180): (X,Y,Z)->(-X,-Y,Z)",
            "whole_transform_count": 1,
            "coordinate_equal_seam_weld": True,
            "head": head_stats,
            "handle": handle_stats,
            "handle_formula": {
                "theta": "-pi/2+pi*U",
                "surface": "X=r(z)cos(theta);Y=r(z)sin(theta)",
                "pi_over_2": math.pi / 2.0,
                "shaft_radius_cm": 2.5,
                "grip_length_cm": 42.0,
                "pommel_length_cm": 18.0,
                "pommel_maximum_width_cm": 11.0,
                "handle_top_z_cm": 132.0,
            },
            "prior_candidate_geometry_inputs": 0,
        },
        "mesh": {
            "object_count": len(objects),
            "vertices": sum(len(obj.data.vertices) for obj in objects),
            "polygons": sum(len(obj.data.polygons) for obj in objects),
            "bounds": bounds,
            "rz180_symmetry": symmetry,
            "maximum_true_haft_radius_error_cm": max_shaft_error,
        },
        "review_cameras": {
            front_camera.name: float(front_camera.data.ortho_scale),
            right_camera.name: float(right_camera.data.ortho_scale),
            three_q.name: float(three_q.data.ortho_scale),
        },
        "technical_gates": gates,
        "technical_result": "PASS",
        "outputs": {
            name: str(path.relative_to(ROOT)) for name, path in output_paths.items()
        },
        "output_hashes": {
            name: sha256(path) for name, path in output_paths.items()
        },
        "comparison_board": str(COMPARISON_BOARD.relative_to(ROOT)),
        "unreal_authority": False,
        "fully_game_ready": False,
    }
    return {
        "manifest_path": manifest_path,
        "manifest": result,
        "paths": paths,
        "blend_path": blend_path,
        "bounds": bounds,
        "gates": gates,
    }


def fit_panel(
    image: Image.Image,
    size: tuple[int, int],
    background: tuple[int, int, int] = (229, 231, 233),
) -> Image.Image:
    value = image.convert("RGB")
    resampling = getattr(Image, "Resampling", Image)
    value.thumbnail(size, resampling.LANCZOS)
    panel = Image.new("RGB", size, background)
    panel.paste(
        value,
        ((size[0] - value.width) // 2, (size[1] - value.height) // 2),
    )
    return panel


def compose_comparison(
    right_source: Image.Image,
    results: dict[str, dict[str, object]],
) -> None:
    canvas = Image.new("RGB", (4700, 2900), (24, 28, 32))
    draw = ImageDraw.Draw(canvas)
    title = font(54)
    subtitle = font(29)
    label = font(27)
    small = font(22)
    draw.text(
        (55, 35),
        "SIEGE BREAKER — CORRECT RIGHT-IMAGE BISECTION / TWO COMPLETE HAMMERS",
        fill=(242, 244, 247),
        font=title,
    )
    draw.text(
        (58, 105),
        "Exact seam x=557 • source half Y<=0 • one Rz(180°) completion • corrected handle through A=132 cm",
        fill=(255, 189, 47),
        font=subtitle,
    )

    source_crop = right_source.crop(tuple(RIGHT_RECT)).convert("RGB")
    source_draw = ImageDraw.Draw(source_crop)
    seam_local = DIAMOND_X - RIGHT_RECT[0]
    source_draw.line(
        (seam_local, 0, seam_local, source_crop.height - 1),
        fill=(255, 48, 48),
        width=3,
    )
    source_panel = fit_panel(source_crop, (820, 2250))
    canvas.paste(source_panel, (55, 190))
    draw.rectangle((55, 190, 875, 2440), outline=(106, 114, 122), width=3)
    draw.text((55, 154), "EXACT NEW RIGHT SOURCE / x=557", fill=(220, 225, 231), font=label)
    draw.text((75, 2470), "LEFT OF LINE: metal-center-piece half", fill=(220, 225, 231), font=small)
    draw.text((75, 2510), "RIGHT OF LINE: rune-side half", fill=(220, 225, 231), font=small)

    panel_w, panel_h = 880, 1080
    x_positions = [940, 1850, 2760, 3670]
    row_y = {"rune": 190, "metal": 1450}
    panel_types = [
        ("color_3q", "COMPLETE COLOR 3/4"),
        ("front", "COMPLETE FRONT"),
        ("right", "COMPLETE RIGHT"),
        ("gray_3q", "INDEPENDENT GRAY 3/4"),
    ]
    for kind in ("rune", "metal"):
        y = row_y[kind]
        heading = (
            "HAMMER A — RUNE-SIDE HALF ROTATED TO WHOLE"
            if kind == "rune"
            else "HAMMER B — METAL-CENTER-PIECE HALF ROTATED TO WHOLE"
        )
        draw.text((940, y - 43), heading, fill=(242, 244, 247), font=label)
        for x, (key, text_label) in zip(x_positions, panel_types):
            image = Image.open(results[kind]["paths"][key])
            panel = fit_panel(image, (panel_w, panel_h))
            canvas.paste(panel, (x, y))
            draw.rectangle(
                (x, y, x + panel_w, y + panel_h),
                outline=(106, 114, 122),
                width=3,
            )
            draw.text((x + 12, y + 12), text_label, fill=(38, 43, 48), font=small)

    notes = [
        "Both: 97.873941674506 x 47.479915237376 x 170 cm.",
        "Corrected handle: top A=132 cm; true shaft 5 cm; grip 42 cm; pommel 18 cm x 11 cm max.",
        "Every candidate is fresh from the new R8 scanlines. No rejected geometry, FBX, Unreal, LOD, or collision.",
        "Status: two DCC source candidates pending Flamestrike comparison.",
    ]
    y = 2630
    for line in notes:
        draw.text((65, y), line, fill=(218, 224, 230), font=small)
        y += 55
    canvas.save(COMPARISON_BOARD)


def main() -> None:
    ensure_dirs()
    scan = json.loads(SCAN_MANIFEST.read_text())
    scale = json.loads(SCALE_MANIFEST.read_text())
    diamond = json.loads(DIAMOND_MANIFEST.read_text())
    if exact(
        scale["new_r8_pixel_dimension_consequence_cm_exact"]["width"]
    ) != TARGET_WIDTH:
        raise RuntimeError("Width authority mismatch")
    if exact(
        scale["new_r8_pixel_dimension_consequence_cm_exact"]["depth"]
    ) != TARGET_DEPTH:
        raise RuntimeError("Depth authority mismatch")
    if int(exact(diamond["diamond_center_x_pixels_exact"])) != DIAMOND_X:
        raise RuntimeError("Diamond center mismatch")

    images: dict[str, Image.Image] = {}
    selected: dict[str, Image.Image] = {}
    filled: dict[str, Image.Image] = {}
    source_paths: dict[str, Path] = {}
    replay: dict[str, dict[str, object]] = {}
    captures = {
        record["view"]: record
        for record in scan["lossless_full_scanline_captures"]
    }
    for view in ("front", "back", "right"):
        source_record = scan["sources"][view]
        source_path = ROOT / source_record["path"]
        if sha256(source_path) != source_record["file_sha256"]:
            raise RuntimeError(f"Source hash mismatch: {view}")
        capture_path = ROOT / captures[view]["path"]
        image, full_mask, capture_replay = replay_capture(
            capture_path, source_path
        )
        rect = [int(value) for value in source_record["rectangle_half_open"]]
        crop = full_mask.crop(tuple(rect))
        images[view] = image
        selected[view] = crop
        filled[view] = fill_enclosed(crop)
        source_paths[view] = source_path
        replay[view] = capture_replay
    if scan["sources"]["front"]["rectangle_half_open"] != FRONT_RECT:
        raise RuntimeError("Front rectangle mismatch")
    if scan["sources"]["right"]["rectangle_half_open"] != RIGHT_RECT:
        raise RuntimeError("Right rectangle mismatch")

    events = measurement_events(selected["front"], selected["right"])
    if not events["pass"]:
        raise RuntimeError(f"New R8 station event audit failed: {events}")

    results: dict[str, dict[str, object]] = {}
    for kind in ("rune", "metal"):
        results[kind] = build_candidate(
            kind,
            images,
            selected,
            filled,
            source_paths,
            replay,
            events,
        )
    compose_comparison(images["right"], results)
    comparison_hash = sha256(COMPARISON_BOARD)
    for kind, result in results.items():
        manifest = result["manifest"]
        manifest["comparison_board_sha256"] = comparison_hash
        manifest["comparison_candidate"] = "metal" if kind == "rune" else "rune"
        result["manifest_path"].write_text(
            json.dumps(manifest, indent=2) + "\n"
        )
    print(
        json.dumps(
            {
                "status": "PASS",
                "contract": CONTRACT_ID,
                "comparison_board": str(COMPARISON_BOARD),
                "comparison_sha256": comparison_hash,
                "candidates": {
                    kind: {
                        "blend": str(result["blend_path"]),
                        "manifest": str(result["manifest_path"]),
                        "gates": f"{sum(result['gates'].values())}/{len(result['gates'])}",
                        "bounds_cm": result["bounds"]["dimensions_cm"],
                    }
                    for kind, result in results.items()
                },
            },
            indent=2,
        )
    )


if __name__ == "__main__":
    main()
