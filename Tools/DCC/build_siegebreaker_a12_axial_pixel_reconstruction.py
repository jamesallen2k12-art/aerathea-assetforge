#!/usr/bin/env python3
"""Build the Siege Breaker A12 axial-source correction in Blender.

The script recreates the approved A09 half/mirror model from its immutable
front/back/left pixels, remaps only the head depth using the approved A11
centered top/bottom footprint, and adds top/bottom source-facing Blender
geometry built from exact source masks.  No generated image or image-to-3D
software is used.
"""

from __future__ import annotations

import hashlib
import json
import math
import sys
from collections import deque
from fractions import Fraction
from pathlib import Path

import bpy
from PIL import Image, ImageChops, ImageDraw, ImageFont, ImageStat
from mathutils import Vector


SCRIPT_DIR = Path(__file__).resolve().parent
if str(SCRIPT_DIR) not in sys.path:
    sys.path.insert(0, str(SCRIPT_DIR))

import build_siegebreaker_a09_pixel_half_mirror_visual_match as a09
from build_a06_siegebreaker_step06_front_back_measurements import selected_membership


ROOT = Path(__file__).resolve().parents[2]
ASSET = "SM_DRW_SiegeBreaker_Hammer_A01"
ATTEMPT = "A12_AxialPixelReconstruction_A01"
CONTRACT_ID = "SB-AXIAL-A12-RECONSTRUCTION"
SOURCE_DIR = ROOT / "SourceAssets/Concepts/SiegeBreaker"
TOP_PATH = SOURCE_DIR / "siege_breaker_true_axial_top_view.png"
BOTTOM_PATH = SOURCE_DIR / "siege_breaker_true_axial_bottom_view.png"
A11_PATH = (
    ROOT
    / "docs/assets/blueprints"
    / ASSET
    / "manifests/A11_TRUE_AXIAL_TOP_BOTTOM_PIXEL_MEASUREMENT.json"
)
A09_BLEND = (
    ROOT
    / "SourceAssets/Blender/Weapons/Dwarven"
    / ASSET
    / "A09_PixelHalfMirror_VisualMatch_A01"
    / f"{ASSET}_A09_PixelHalfMirror_VisualMatch_A01.blend"
)

EXPECTED_SHA256 = {
    "front": "d00bf9ffcfd4862884626fa961c5f6b4fd6cedfdff7936b2210ca2a905e57e95",
    "back": "15b4633f2df4ee06115ef4a7e238f287ebece1bae514ad4005c1036a57359799",
    "left": "1a23e0c24f7be4b12df93e2509b9d300acc9161a21a32b336f7cf63c1288d91b",
    "concept": "9f1ac142a5047968bb20c74216c2dccf61470ed9f4e21689ff01934bd849c586",
    "top": "aee612d9bed74e4f861576f926fe9d75de00f80dc416e3a6ba66a75247c00e98",
    "bottom": "874a9e7c7713c7edbcf1030486d3988a54e8499ee697e316ec82a013fdb9d746",
    "a11": "46877ab4b0142d8141deb4feab234f461a31e61e118d3ce7b41e0b3679786096",
    "a09_blend": "06ffb121d00cddb7b9e30a60067a5036a851d285f15daca3bffe3a663fd6d78f",
}
EXPECTED_A11_RECTS = {"top": [94, 330, 1106, 921], "bottom": [93, 330, 1106, 933]}
EXPECTED_A11_COUNTS = {"top": 465117, "bottom": 509030}
COMMON_SCALE = float(Fraction(33388, 449955))
TARGET_WIDTH = float(Fraction(83470, 1111))
TARGET_DEPTH = float(Fraction(6644212, 149985))
TARGET_HEIGHT = 170.0
HEAD_Z_MIN = 132.0
HEAD_Z_MAX = 170.0
RELIEF_STEP_PX = 3.0
RELIEF_MAX_CM = 0.45
CORE_WIDTH_RATIO = float(Fraction(24, 52))
STONE_WIDTH_RATIO_EACH = float(Fraction(14, 52))
CORE_WIDTH = TARGET_WIDTH * CORE_WIDTH_RATIO
STONE_WIDTH_EACH = TARGET_WIDTH * STONE_WIDTH_RATIO_EACH
CORE_HALF_WIDTH = CORE_WIDTH * 0.5
COMPONENT_SEPARATION_APPROVED = True

OUTPUT_ROOT = ROOT / "SourceAssets/Blender/Weapons/Dwarven" / ASSET / ATTEMPT
LOCAL_RENDER_ROOT = OUTPUT_ROOT / "renders"
BLEND_PATH = OUTPUT_ROOT / f"{ASSET}_{ATTEMPT}.blend"
DOC_ROOT = ROOT / "docs/assets/blueprints" / ASSET
REVIEW_ROOT = DOC_ROOT / "review"
MANIFEST_PATH = DOC_ROOT / "manifests/A12_AXIAL_PIXEL_RECONSTRUCTION_A01_VALIDATION.json"
MASK_PATHS = {
    "top": OUTPUT_ROOT / "A12_true_top_filled_footprint.png",
    "bottom": OUTPUT_ROOT / "A12_true_bottom_filled_footprint.png",
}
RENDER_PATHS = {
    "front": REVIEW_ROOT / "A12_AXIAL_PIXEL_RECONSTRUCTION_A01_FRONT.png",
    "top": REVIEW_ROOT / "A12_AXIAL_PIXEL_RECONSTRUCTION_A01_TOP_HEAD_ISOLATED.png",
    "bottom": REVIEW_ROOT / "A12_AXIAL_PIXEL_RECONSTRUCTION_A01_BOTTOM_HEAD_ISOLATED.png",
    "color_3q": REVIEW_ROOT / "A12_AXIAL_PIXEL_RECONSTRUCTION_A01_COLOR_3Q.png",
    "geometry_3q": REVIEW_ROOT / "A12_AXIAL_PIXEL_RECONSTRUCTION_A01_GEOMETRY_3Q.png",
}
REVIEW_BOARD = REVIEW_ROOT / "A12_AXIAL_PIXEL_RECONSTRUCTION_A01_REVIEW.png"


def sha256(path: Path) -> str:
    digest = hashlib.sha256()
    with path.open("rb") as handle:
        for block in iter(lambda: handle.read(1024 * 1024), b""):
            digest.update(block)
    return digest.hexdigest()


def ensure_dirs() -> None:
    OUTPUT_ROOT.mkdir(parents=True, exist_ok=True)
    LOCAL_RENDER_ROOT.mkdir(parents=True, exist_ok=True)
    REVIEW_ROOT.mkdir(parents=True, exist_ok=True)
    MANIFEST_PATH.parent.mkdir(parents=True, exist_ok=True)


def filled_a11_mask(path: Path, view: str) -> tuple[Image.Image, Image.Image, dict[str, object]]:
    source = Image.open(path).convert("RGB")
    membership, metadata = selected_membership(source)
    rect = metadata["rectangle_half_open"]
    if rect != EXPECTED_A11_RECTS[view]:
        raise RuntimeError(f"{view} A11 rectangle mismatch: {rect}")
    if metadata["selected_component_pixel_count"] != EXPECTED_A11_COUNTS[view]:
        raise RuntimeError(f"{view} A11 membership mismatch: {metadata}")

    x0, y0, x1, y1 = rect
    width, height = x1 - x0, y1 - y0
    selected = bytearray(width * height)
    for y in range(height):
        for x in range(width):
            selected[y * width + x] = membership[(y0 + y) * source.width + x0 + x]

    exterior = bytearray(width * height)
    queue: deque[int] = deque()
    for x in range(width):
        for y in (0, height - 1):
            index = y * width + x
            if not selected[index] and not exterior[index]:
                exterior[index] = 1
                queue.append(index)
    for y in range(height):
        for x in (0, width - 1):
            index = y * width + x
            if not selected[index] and not exterior[index]:
                exterior[index] = 1
                queue.append(index)
    while queue:
        current = queue.popleft()
        cy, cx = divmod(current, width)
        for nx, ny in ((cx + 1, cy), (cx - 1, cy), (cx, cy + 1), (cx, cy - 1)):
            if nx < 0 or ny < 0 or nx >= width or ny >= height:
                continue
            neighbor = ny * width + nx
            if selected[neighbor] or exterior[neighbor]:
                continue
            exterior[neighbor] = 1
            queue.append(neighbor)

    filled = Image.new("L", (width, height), 0)
    pixels = filled.load()
    for y in range(height):
        for x in range(width):
            index = y * width + x
            if selected[index] or not exterior[index]:
                pixels[x, y] = 255
    if filled.getbbox() != (0, 0, width, height):
        raise RuntimeError(f"{view} filled mask lost measured boundary: {filled.getbbox()}")
    return source, filled, metadata


def column_span(mask: Image.Image, source_x_edge: float) -> tuple[int, int]:
    pixels = mask.load()
    width, height = mask.size
    column = max(0, min(width - 1, int(math.floor(source_x_edge))))
    for radius in range(7):
        candidates = [column] if radius == 0 else [max(0, column - radius), min(width - 1, column + radius)]
        for candidate in candidates:
            ys = [y for y in range(height) if pixels[candidate, y] > 0]
            if ys:
                return min(ys), max(ys) + 1
    raise RuntimeError(f"no axial footprint near source x={source_x_edge}")


def source_y_edges(mask: Image.Image, world_x: float, view: str) -> tuple[float, float]:
    width, height = mask.size
    source_x_edge = width * 0.5 + world_x / COMMON_SCALE
    y0, y1 = column_span(mask, source_x_edge)
    return ((height * 0.5 - y1) * COMMON_SCALE, (height * 0.5 - y0) * COMMON_SCALE)


def mean_axial_edges(top_mask: Image.Image, bottom_mask: Image.Image, world_x: float) -> tuple[float, float]:
    top_min, top_max = source_y_edges(top_mask, abs(world_x), "top")
    bottom_min, bottom_max = source_y_edges(bottom_mask, abs(world_x), "bottom")
    return ((top_min + bottom_min) * 0.5, (top_max + bottom_max) * 0.5)


def remap_stone_depth(
    model: bpy.types.Object,
    left_mask: Image.Image,
    top_mask: Image.Image,
    bottom_mask: Image.Image,
) -> dict[str, float | int]:
    changed = 0
    remapped_vertices: list[bpy.types.MeshVertex] = []
    for vertex in model.data.vertices:
        x, old_y, z = float(vertex.co.x), float(vertex.co.y), float(vertex.co.z)
        old_min, old_max = a09.depth_at_z(left_mask, z)
        new_min, new_max = mean_axial_edges(top_mask, bottom_mask, x)
        if old_max - old_min <= 1.0e-9:
            fraction = 0.5
        else:
            fraction = max(0.0, min(1.0, (old_y - old_min) / (old_max - old_min)))
        vertex.co.y = new_min + fraction * (new_max - new_min)
        remapped_vertices.append(vertex)
        changed += 1

    pre_normalize_min = min(float(vertex.co.y) for vertex in remapped_vertices)
    pre_normalize_max = max(float(vertex.co.y) for vertex in remapped_vertices)
    pre_normalize_depth = pre_normalize_max - pre_normalize_min
    if pre_normalize_depth <= 1.0e-9:
        raise RuntimeError("A12 head depth remap collapsed")
    source_center = (pre_normalize_min + pre_normalize_max) * 0.5
    normalize_scale = TARGET_DEPTH / pre_normalize_depth
    for vertex in remapped_vertices:
        vertex.co.y = (float(vertex.co.y) - source_center) * normalize_scale

    observed_min = min(float(vertex.co.y) for vertex in remapped_vertices)
    observed_max = max(float(vertex.co.y) for vertex in remapped_vertices)
    model.data.update()
    return {
        "vertices_remapped": changed,
        "pre_normalize_head_vertex_y_min_cm": pre_normalize_min,
        "pre_normalize_head_vertex_y_max_cm": pre_normalize_max,
        "pre_normalize_head_vertex_depth_cm": pre_normalize_depth,
        "centered_mean_depth_normalization_scale": normalize_scale,
        "head_vertex_y_min_cm": observed_min,
        "head_vertex_y_max_cm": observed_max,
        "head_vertex_depth_cm": observed_max - observed_min,
    }


def partition_front_components(front_mask: Image.Image) -> tuple[Image.Image, Image.Image, dict[str, object]]:
    """Split the exact source membership at the pixel-scaled 24:14:14 boundary."""
    width, height = front_mask.size
    source_pixels = front_mask.load()
    core_mask = Image.new("L", (width, height), 0)
    stone_mask = Image.new("L", (width, height), 0)
    core_pixels = core_mask.load()
    stone_pixels = stone_mask.load()
    core_count = 0
    stone_count = 0
    for local_y in range(height):
        for local_x in range(width):
            if source_pixels[local_x, local_y] == 0:
                continue
            global_center_x = a09.FRONT_RECT[0] + local_x + 0.5
            world_x = (global_center_x - a09.FRONT_CENTER_EDGE) * a09.FRONT_SCALE
            if abs(world_x) < CORE_HALF_WIDTH:
                core_pixels[local_x, local_y] = 255
                core_count += 1
            else:
                stone_pixels[local_x, local_y] = 255
                stone_count += 1
    if core_count + stone_count != sum(1 for value in front_mask.getdata() if value):
        raise RuntimeError("A12 component partition lost source membership")
    return core_mask, stone_mask, {
        "ratio_core_leftstone_rightstone": [24, 14, 14],
        "core_width_cm": CORE_WIDTH,
        "stone_width_each_cm": STONE_WIDTH_EACH,
        "core_half_width_cm": CORE_HALF_WIDTH,
        "core_source_pixels": core_count,
        "two_stone_source_pixels": stone_count,
    }


def assign_axial_owner_materials(
    model: bpy.types.Object,
    top_source: Image.Image,
    bottom_source: Image.Image,
    top_material: bpy.types.Material,
    bottom_material: bpy.types.Material,
    minimum_z: float | None,
) -> dict[str, int]:
    """Put axial source pixels on the real remapped head boundary.

    The A09 volume already contains closed silhouette-boundary faces.  After
    the A11 depth remap these faces are the physical top/bottom surfaces of the
    candidate, so they own the source material.  Constant-Z source projections
    remain proof-only and never enter completed-assembly renders.
    """
    top_material_index = len(model.data.materials)
    model.data.materials.append(top_material)
    bottom_material_index = len(model.data.materials)
    model.data.materials.append(bottom_material)
    uv_layer = model.data.uv_layers.active
    if uv_layer is None:
        raise RuntimeError("A12 main volume has no source UV layer")

    counts = {"top_boundary_faces": 0, "bottom_boundary_faces": 0}
    for polygon in model.data.polygons:
        if polygon.material_index != 2:
            continue
        if minimum_z is not None and min(float(model.data.vertices[index].co.z) for index in polygon.vertices) < minimum_z - 1.0e-6:
            continue
        if polygon.normal.z > 0.5:
            view = "top"
            source = top_source
            material_index = top_material_index
            counts["top_boundary_faces"] += 1
        elif polygon.normal.z < -0.5:
            view = "bottom"
            source = bottom_source
            material_index = bottom_material_index
            counts["bottom_boundary_faces"] += 1
        else:
            continue
        width = EXPECTED_A11_RECTS[view][2] - EXPECTED_A11_RECTS[view][0]
        height = EXPECTED_A11_RECTS[view][3] - EXPECTED_A11_RECTS[view][1]
        for loop_index in polygon.loop_indices:
            vertex = model.data.vertices[model.data.loops[loop_index].vertex_index]
            local_x = width * 0.5 + float(vertex.co.x) / COMMON_SCALE
            local_y = height * 0.5 - float(vertex.co.y) / COMMON_SCALE
            global_x = EXPECTED_A11_RECTS[view][0] + local_x
            global_y = EXPECTED_A11_RECTS[view][1] + local_y
            uv_layer.data[loop_index].uv = (
                global_x / source.width,
                1.0 - global_y / source.height,
            )
        polygon.material_index = material_index

    if counts["top_boundary_faces"] == 0 or counts["bottom_boundary_faces"] == 0:
        raise RuntimeError(f"A12 axial material ownership found no boundary faces: {counts}")
    model["Aerathea.AxialOwnerMaterialsIntegrated"] = True
    model["Aerathea.AxialOwnerFaceCounts"] = json.dumps(counts, sort_keys=True)
    model.data.update()
    return counts


def boundary_loops(mask: Image.Image) -> list[list[tuple[float, float]]]:
    pixels = mask.load()
    width, height = mask.size

    def active(x: int, y: int) -> bool:
        return 0 <= x < width and 0 <= y < height and pixels[x, y] > 0

    edges: list[tuple[tuple[int, int], tuple[int, int]]] = []
    for y in range(height):
        for x in range(width):
            if not active(x, y):
                continue
            if not active(x - 1, y):
                edges.append(((x, y), (x, y + 1)))
            if not active(x + 1, y):
                edges.append(((x + 1, y + 1), (x + 1, y)))
            if not active(x, y - 1):
                edges.append(((x + 1, y), (x, y)))
            if not active(x, y + 1):
                edges.append(((x, y + 1), (x + 1, y + 1)))

    outgoing: dict[tuple[int, int], tuple[int, int]] = {}
    for start, end in edges:
        if start in outgoing:
            raise RuntimeError(f"ambiguous boundary at {start}")
        outgoing[start] = end

    loops: list[list[tuple[float, float]]] = []
    unused = set(outgoing)
    while unused:
        start = min(unused)
        current = start
        loop: list[tuple[float, float]] = []
        while True:
            if current not in unused and current != start:
                raise RuntimeError(f"open or intersecting boundary at {current}")
            if current == start and loop:
                break
            loop.append((float(current[0]), float(current[1])))
            unused.discard(current)
            current = outgoing[current]
        loops.append(loop)
    loops.sort(key=len, reverse=True)
    return loops


def clip_polygon_right_half(points: list[tuple[float, float]], center_x: float) -> list[tuple[float, float]]:
    output: list[tuple[float, float]] = []
    previous = points[-1]
    previous_inside = previous[0] >= center_x
    for current in points:
        current_inside = current[0] >= center_x
        if current_inside != previous_inside:
            denominator = current[0] - previous[0]
            if abs(denominator) < 1.0e-12:
                intersection = (center_x, current[1])
            else:
                t = (center_x - previous[0]) / denominator
                intersection = (center_x, previous[1] + t * (current[1] - previous[1]))
            output.append(intersection)
        if current_inside:
            output.append(current)
        previous = current
        previous_inside = current_inside
    cleaned: list[tuple[float, float]] = []
    for point in output:
        if not cleaned or point != cleaned[-1]:
            cleaned.append(point)
    if cleaned and cleaned[0] == cleaned[-1]:
        cleaned.pop()
    if len(cleaned) < 3:
        raise RuntimeError("right-half boundary clip produced no polygon")
    return cleaned


def world_xy(local_x: float, local_y: float, width: int, height: int, view: str) -> tuple[float, float]:
    x = (local_x - width * 0.5) * COMMON_SCALE
    y = (height * 0.5 - local_y) * COMMON_SCALE
    return x, y


def apply_x_mirror(obj: bpy.types.Object, modifier_name: str) -> None:
    bpy.context.view_layer.objects.active = obj
    obj.select_set(True)
    modifier = obj.modifiers.new(modifier_name, "MIRROR")
    modifier.use_axis[0] = True
    modifier.use_clip = True
    modifier.use_mirror_merge = True
    modifier.merge_threshold = COMMON_SCALE * 0.01
    bpy.ops.object.modifier_apply(modifier=modifier.name)
    obj["Aerathea.MirrorApplied"] = True
    obj.select_set(False)


def build_axial_cap(
    view: str,
    source: Image.Image,
    mask: Image.Image,
    materials: list[bpy.types.Material],
) -> tuple[bpy.types.Object, dict[str, object]]:
    loops = boundary_loops(mask)
    if len(loops) != 1:
        raise RuntimeError(f"{view} expected one filled footprint loop, got {len(loops)}")
    width, height = mask.size
    polygon = clip_polygon_right_half(loops[0], width * 0.5)
    xy = [world_xy(x, y, width, height, view) for x, y in polygon]
    area_twice = sum(
        xy[index][0] * xy[(index + 1) % len(xy)][1]
        - xy[(index + 1) % len(xy)][0] * xy[index][1]
        for index in range(len(xy))
    )
    want_positive = view == "top"
    if (area_twice > 0.0) != want_positive:
        polygon.reverse()
        xy.reverse()

    if view == "top":
        visible_z, inside_z = 168.45, 167.95
    else:
        visible_z, inside_z = 133.55, 134.05
    vertices = [(x, y, visible_z) for x, y in xy] + [(x, y, inside_z) for x, y in xy]
    count = len(xy)
    outer = tuple(range(count))
    inner = tuple(range(2 * count - 1, count - 1, -1))
    faces: list[tuple[int, ...]] = [outer, inner]
    face_uvs: list[list[tuple[float, float]]] = []
    outer_uv = [
        ((x + EXPECTED_A11_RECTS[view][0]) / source.width, 1.0 - (y + EXPECTED_A11_RECTS[view][1]) / source.height)
        for x, y in polygon
    ]
    face_uvs.append(outer_uv)
    face_uvs.append(list(reversed(outer_uv)))
    face_materials = [0, 1]
    for index in range(count):
        nxt = (index + 1) % count
        faces.append((index, nxt, count + nxt, count + index))
        face_uvs.append([(0.0, 0.0), (1.0, 0.0), (1.0, 1.0), (0.0, 1.0)])
        face_materials.append(1)

    mesh = bpy.data.meshes.new(f"{ASSET}_A12_{view.title()}CapHalf_Mesh")
    mesh.from_pydata(vertices, [], faces)
    mesh.update(calc_edges=True)
    uv_layer = mesh.uv_layers.new(name=f"A12_{view.title()}_ExactSourceUV")
    for face, uvs, material_index in zip(mesh.polygons, face_uvs, face_materials):
        face.material_index = material_index
        for loop_index, uv in zip(face.loop_indices, uvs):
            uv_layer.data[loop_index].uv = uv
    obj = bpy.data.objects.new(f"{ASSET}_A12_{view.title()}Cap_XPositive", mesh)
    bpy.context.scene.collection.objects.link(obj)
    for material in materials:
        obj.data.materials.append(material)
    obj["Aerathea.SourceView"] = view
    obj["Aerathea.ArtifactStatus"] = "proof only; head-isolated source backing; hidden from completed assembly"
    obj["Aerathea.Construction"] = "exact filled source footprint boundary; X>=0 half; closed head-isolated proof cap"
    apply_x_mirror(obj, f"A12_{view.title()}Cap_ExactCenterMirror")
    obj.name = f"{ASSET}_A12_{view.title()}ClosedSourceCap"
    obj.hide_render = True
    return obj, {
        "boundary_loops": len(loops),
        "full_boundary_edges": len(loops[0]),
        "half_boundary_vertices": len(polygon),
        "complete_vertices": len(obj.data.vertices),
        "complete_polygons": len(obj.data.polygons),
        "visible_z_cm": visible_z,
        "inside_z_cm": inside_z,
    }


def source_luma(source: Image.Image, global_x: float, global_y: float) -> int:
    x = max(0, min(source.width - 1, int(math.floor(global_x))))
    y = max(0, min(source.height - 1, int(math.floor(global_y))))
    return a09.integer_luma(source.getpixel((x, y)))


def build_axial_relief(
    view: str,
    source: Image.Image,
    mask: Image.Image,
    material: bpy.types.Material,
) -> tuple[bpy.types.Object, dict[str, object]]:
    width, height = mask.size
    center = width * 0.5
    x_edges = [center]
    while x_edges[-1] < width:
        x_edges.append(min(float(width), x_edges[-1] + RELIEF_STEP_PX))
    y_edges = [0.0]
    while y_edges[-1] < height:
        y_edges.append(min(float(height), y_edges[-1] + RELIEF_STEP_PX))

    mask_pixels = mask.load()
    vertices: list[tuple[float, float, float]] = []
    vertex_uvs: list[tuple[float, float]] = []
    faces: list[tuple[int, int, int, int]] = []
    cache: dict[tuple[int, int], int] = {}

    def relief_vertex(ix: int, iy: int) -> int:
        key = (ix, iy)
        if key in cache:
            return cache[key]
        local_x, local_y = x_edges[ix], y_edges[iy]
        global_x = EXPECTED_A11_RECTS[view][0] + local_x
        global_y = EXPECTED_A11_RECTS[view][1] + local_y
        luma = source_luma(source, global_x, global_y)
        inward = max(0.0, min(RELIEF_MAX_CM, (234.0 - min(234, luma)) / 234.0 * RELIEF_MAX_CM))
        x, y = world_xy(local_x, local_y, width, height, view)
        z = HEAD_Z_MAX - inward if view == "top" else HEAD_Z_MIN + inward
        index = len(vertices)
        vertices.append((x, y, z))
        vertex_uvs.append((global_x / source.width, 1.0 - global_y / source.height))
        cache[key] = index
        return index

    for iy in range(len(y_edges) - 1):
        for ix in range(len(x_edges) - 1):
            center_x = int(min(width - 1, math.floor((x_edges[ix] + x_edges[ix + 1]) * 0.5)))
            center_y = int(min(height - 1, math.floor((y_edges[iy] + y_edges[iy + 1]) * 0.5)))
            if mask_pixels[center_x, center_y] == 0:
                continue
            v00 = relief_vertex(ix, iy)
            v10 = relief_vertex(ix + 1, iy)
            v11 = relief_vertex(ix + 1, iy + 1)
            v01 = relief_vertex(ix, iy + 1)
            faces.append((v00, v01, v11, v10) if view == "top" else (v00, v10, v11, v01))

    mesh = bpy.data.meshes.new(f"{ASSET}_A12_{view.title()}ReliefHalf_Mesh")
    mesh.from_pydata(vertices, [], faces)
    mesh.update(calc_edges=True)
    uv_layer = mesh.uv_layers.new(name=f"A12_{view.title()}_ReliefSourceUV")
    for face in mesh.polygons:
        for loop_index in face.loop_indices:
            uv_layer.data[loop_index].uv = vertex_uvs[mesh.loops[loop_index].vertex_index]
    obj = bpy.data.objects.new(f"{ASSET}_A12_{view.title()}Relief_XPositive", mesh)
    bpy.context.scene.collection.objects.link(obj)
    obj.data.materials.append(material)
    obj["Aerathea.SourceView"] = view
    obj["Aerathea.ArtifactStatus"] = "proof only; head-isolated source projection; hidden from completed assembly"
    obj["Aerathea.Construction"] = f"{RELIEF_STEP_PX:g}px sampled inward proof relief; exact source UV; X>=0 half; solidified inward"
    obj["Aerathea.ReliefMaxCm"] = RELIEF_MAX_CM
    apply_x_mirror(obj, f"A12_{view.title()}Relief_ExactCenterMirror")
    bpy.context.view_layer.objects.active = obj
    obj.select_set(True)
    solidify = obj.modifiers.new(f"A12_{view.title()}Relief_InwardSolidify", "SOLIDIFY")
    solidify.thickness = 0.06
    solidify.offset = -1.0
    solidify.use_even_offset = True
    bpy.ops.object.modifier_apply(modifier=solidify.name)
    obj["Aerathea.Solidified"] = True
    obj.select_set(False)
    obj.name = f"{ASSET}_A12_{view.title()}SourceRelief"
    obj.hide_render = True
    return obj, {
        "grid_step_pixels": RELIEF_STEP_PX,
        "inward_relief_max_cm": RELIEF_MAX_CM,
        "solidify_thickness_cm": 0.06,
        "closed_surface": True,
        "half_faces_before_mirror": len(faces),
        "complete_vertices": len(obj.data.vertices),
        "complete_polygons": len(obj.data.polygons),
    }


def configure_scene() -> None:
    a09.configure_scene()
    scene = bpy.context.scene
    scene.render.image_settings.color_mode = "RGB"
    scene.render.resolution_percentage = 100


def add_camera(name: str, location: tuple[float, float, float], target: tuple[float, float, float], ortho: float) -> bpy.types.Object:
    return a09.add_camera(name, location, target, ortho)


def axial_camera(view: str, rect: list[int]) -> bpy.types.Object:
    canvas = 1254
    object_center_x = (rect[0] + rect[2]) * 0.5
    object_center_y = (rect[1] + rect[3]) * 0.5
    target_x = (canvas * 0.5 - object_center_x) * COMMON_SCALE
    target_y = (object_center_y - canvas * 0.5) * COMMON_SCALE
    if view == "top":
        location = (target_x, target_y, 520.0)
        target = (target_x, target_y, 151.0)
    else:
        location = (target_x, target_y, -220.0)
        target = (target_x, target_y, 151.0)
    return add_camera(f"CAM_A12_{view.upper()}_PIXEL_REGISTERED", location, target, canvas * COMMON_SCALE)


def render(camera: bpy.types.Object, path: Path, width: int, height: int, override: bpy.types.Material | None = None) -> None:
    scene = bpy.context.scene
    scene.camera = camera
    scene.render.resolution_x = width
    scene.render.resolution_y = height
    scene.render.filepath = str(path)
    scene.view_layers[0].material_override = override
    bpy.ops.render.render(write_still=True)
    scene.view_layers[0].material_override = None


def render_geometry_objects(
    objects: list[bpy.types.Object],
    camera: bpy.types.Object,
    path: Path,
    width: int,
    height: int,
    material: bpy.types.Material,
) -> None:
    saved: dict[str, tuple[list[bpy.types.Material | None], list[int]]] = {}
    for obj in objects:
        saved[obj.name] = (
            [slot.material for slot in obj.material_slots],
            [polygon.material_index for polygon in obj.data.polygons],
        )
        obj.data.materials.clear()
        obj.data.materials.append(material)
        for polygon in obj.data.polygons:
            polygon.material_index = 0
    render(camera, path, width, height)
    for obj in objects:
        materials, indices = saved[obj.name]
        obj.data.materials.clear()
        for value in materials:
            obj.data.materials.append(value)
        for polygon, material_index in zip(obj.data.polygons, indices):
            polygon.material_index = material_index


def render_head_isolated(
    view: str,
    camera: bpy.types.Object,
    path: Path,
    models: list[bpy.types.Object],
    cap_objects: dict[str, bpy.types.Object],
    relief_objects: dict[str, bpy.types.Object],
) -> None:
    all_objects = [*models, *cap_objects.values(), *relief_objects.values()]
    states = {obj.name: obj.hide_render for obj in all_objects}
    for model in models:
        model.hide_render = True
    for name in ("top", "bottom"):
        visible = name == view
        cap_objects[name].hide_render = not visible
        relief_objects[name].hide_render = not visible
    render(camera, path, 1254, 1254)
    for obj in all_objects:
        obj.hide_render = states[obj.name]


def bounds_objects(objects: list[bpy.types.Object]) -> dict[str, list[float]]:
    points: list[Vector] = []
    for obj in objects:
        points.extend(obj.matrix_world @ vertex.co for vertex in obj.data.vertices)
    minimum = [min(float(point[axis]) for point in points) for axis in range(3)]
    maximum = [max(float(point[axis]) for point in points) for axis in range(3)]
    return {
        "minimum_cm": minimum,
        "maximum_cm": maximum,
        "dimensions_cm": [maximum[axis] - minimum[axis] for axis in range(3)],
    }


def symmetry(objects: list[bpy.types.Object]) -> dict[str, object]:
    missing = 0
    unique_total = 0
    per_object = {}
    for obj in objects:
        coords = {(round(v.co.x, 5), round(v.co.y, 5), round(v.co.z, 5)) for v in obj.data.vertices}
        object_missing = sum(1 for x, y, z in coords if (-x, y, z) not in coords)
        per_object[obj.name] = {"unique_vertices": len(coords), "missing_mirrored_vertices": object_missing}
        missing += object_missing
        unique_total += len(coords)
    return {"unique_vertices": unique_total, "missing_mirrored_vertices": missing, "pass": missing == 0, "per_object": per_object}


def font(size: int) -> ImageFont.ImageFont:
    return a09.font(size)


def fit_panel(image: Image.Image, size: tuple[int, int], background: tuple[int, int, int] = (245, 243, 238)) -> Image.Image:
    return a09.fit_panel(image, size, background)


def axial_difference(source: Image.Image, candidate: Image.Image, mask: Image.Image, rect: list[int]) -> dict[str, float]:
    source_rgb = source.convert("RGB")
    candidate_rgb = candidate.convert("RGB")
    global_mask = Image.new("L", source_rgb.size, 0)
    global_mask.paste(mask, (rect[0], rect[1]))
    right_mask = Image.new("L", source_rgb.size, 0)
    right_pixels = right_mask.load()
    mask_pixels = global_mask.load()
    center = (rect[0] + rect[2]) * 0.5
    for y in range(source_rgb.height):
        for x in range(math.ceil(center), source_rgb.width):
            if mask_pixels[x, y] > 0:
                right_pixels[x, y] = 255
    difference = ImageChops.difference(source_rgb, candidate_rgb)
    stat = ImageStat.Stat(difference, mask=right_mask)
    return {"right_half_mean_absolute_rgb_delta": round(sum(stat.mean) / 3.0, 6)}


def compose_review(
    sources: dict[str, Image.Image],
    masks: dict[str, Image.Image],
    bounds: dict[str, list[float]],
    counts: dict[str, int],
) -> dict[str, dict[str, float]]:
    board = Image.new("RGB", (3600, 3000), (228, 224, 216))
    draw = ImageDraw.Draw(board)
    title = font(60)
    subtitle = font(31)
    label = font(34)
    body = font(27)
    small = font(23)
    draw.rectangle((0, 0, 3600, 210), fill=(29, 34, 41))
    draw.text((70, 35), "SIEGE BREAKER A12 R3 - COMPONENT-SEPARATED AXIAL RECONSTRUCTION", fill=(245, 242, 233), font=title)
    draw.text((72, 125), "TWO MIRRORED STONES + CENTERED CORE | PIXEL-SCALED 24:14:14 | BLENDER ONLY", fill=(173, 207, 229), font=subtitle)

    axial_crops = {
        "top": (55, 285, 1145, 970),
        "bottom": (55, 285, 1145, 980),
    }
    columns = [(80, "top", "TOP SOURCE", sources["top"].crop(axial_crops["top"])),
               (950, "top", "A12 TOP - HEAD ISOLATED", Image.open(RENDER_PATHS["top"]).crop(axial_crops["top"])),
               (1820, "bottom", "BOTTOM SOURCE", sources["bottom"].crop(axial_crops["bottom"])),
               (2690, "bottom", "A12 BOTTOM - HEAD ISOLATED", Image.open(RENDER_PATHS["bottom"]).crop(axial_crops["bottom"]))]
    for x, _, text_label, image in columns:
        draw.text((x, 250), text_label, fill=(39, 42, 47), font=label)
        panel = fit_panel(image, (800, 720))
        board.paste(panel, (x, 305))
        draw.rectangle((x, 305, x + 800, 1025), outline=(91, 88, 82), width=3)

    front_source_crop = Image.open(a09.FRONT_PATH).convert("RGB").crop((250, 150, 875, 1365))
    front_render_crop = Image.open(RENDER_PATHS["front"]).convert("RGB").crop((250, 150, 875, 1365))
    lower = [
        (80, "UNCHANGED FRONT SOURCE", front_source_crop),
        (950, "A12 COMPLETED FRONT", front_render_crop),
        (1820, "A12 COLORED 3/4", Image.open(RENDER_PATHS["color_3q"])),
        (2690, "A12 GEOMETRY 3/4", Image.open(RENDER_PATHS["geometry_3q"])),
    ]
    for x, text_label, image in lower:
        draw.text((x, 1100), text_label, fill=(39, 42, 47), font=label)
        panel = fit_panel(image, (800, 1280))
        board.paste(panel, (x, 1155))
        draw.rectangle((x, 1155, x + 800, 2435), outline=(91, 88, 82), width=3)

    comparison = {
        view: axial_difference(sources[view], Image.open(RENDER_PATHS[view]), masks[view], EXPECTED_A11_RECTS[view])
        for view in ("top", "bottom")
    }
    dims = bounds["dimensions_cm"]
    notes = [
        f"Approved mean footprint: 1012.5 x 597 px = {TARGET_WIDTH:.6f} x {TARGET_DEPTH:.6f} cm; overall length {TARGET_HEIGHT:.3f} cm.",
        "Flat top/bottom projections are proof only; source ownership is integrated onto the separated stone/core boundary faces.",
        f"Top/bottom right-half RGB deltas: {comparison['top']['right_half_mean_absolute_rgb_delta']:.3f} / {comparison['bottom']['right_half_mean_absolute_rgb_delta']:.3f} of 255.",
        f"Evaluated complete bounds: {dims[0]:.6f} x {dims[1]:.6f} x {dims[2]:.6f} cm; mesh objects {counts['objects']}; polygons {counts['polygons']}.",
        "Status: DCC source candidate pending Flamestrike visual decision. No image generation, TRELLIS, export, or Unreal work.",
    ]
    draw.rectangle((0, 2510, 3600, 3000), fill=(35, 39, 45))
    y = 2570
    for line in notes:
        draw.text((75, y), line, fill=(235, 232, 222), font=body if y == 2570 else small)
        y += 72
    board.save(REVIEW_BOARD)
    return comparison


def main() -> None:
    if not COMPONENT_SEPARATION_APPROVED:
        raise RuntimeError(
            "Blueprint block: A12 R3 component-separation correction is not approved"
        )
    ensure_dirs()
    paths = {
        "front": a09.FRONT_PATH,
        "back": a09.BACK_PATH,
        "left": a09.LEFT_PATH,
        "concept": a09.CONCEPT_PATH,
        "top": TOP_PATH,
        "bottom": BOTTOM_PATH,
        "a11": A11_PATH,
        "a09_blend": A09_BLEND,
    }
    for name, path in paths.items():
        observed = sha256(path)
        if observed != EXPECTED_SHA256[name]:
            raise RuntimeError(f"authority hash mismatch for {name}: {observed}")

    a11 = json.loads(A11_PATH.read_text(encoding="utf-8"))
    if a11["schema"] != "aerathea.siegebreaker_true_axial_pixel_measurement.v2":
        raise RuntimeError(f"unexpected A11 schema: {a11['schema']}")
    if a11["approved_reconciliation"]["status"] != "authoritative":
        raise RuntimeError("A11 reconciliation is not authoritative")

    front_image = Image.open(a09.FRONT_PATH).convert("RGB")
    back_image = Image.open(a09.BACK_PATH).convert("RGB")
    left_image = Image.open(a09.LEFT_PATH).convert("RGB")
    front_mask, front_count = a09.exact_component_mask(front_image, a09.FRONT_RECT)
    back_mask, back_count = a09.exact_component_mask(back_image, a09.BACK_RECT)
    left_mask, left_count = a09.exact_component_mask(left_image, a09.LEFT_RECT)
    observed_a09_counts = {"front": front_count, "back": back_count, "left": left_count}
    if observed_a09_counts != a09.EXPECTED_COMPONENT_PIXELS:
        raise RuntimeError(f"A09 membership replay mismatch: {observed_a09_counts}")

    top_source, top_mask, top_meta = filled_a11_mask(TOP_PATH, "top")
    bottom_source, bottom_mask, bottom_meta = filled_a11_mask(BOTTOM_PATH, "bottom")
    top_mask.save(MASK_PATHS["top"])
    bottom_mask.save(MASK_PATHS["bottom"])
    sources = {"top": top_source, "bottom": bottom_source}
    masks = {"top": top_mask, "bottom": bottom_mask}

    a09.clear_scene()
    configure_scene()
    front_material = a09.image_material("MI_DRW_SiegeBreaker_A12_FrontSourcePixels", a09.FRONT_PATH)
    back_material = a09.image_material("MI_DRW_SiegeBreaker_A12_BackSourcePixels", a09.BACK_PATH)
    side_material = a09.image_material("MI_DRW_SiegeBreaker_A12_LeftSourcePixels", a09.LEFT_PATH)
    top_material = a09.image_material("MI_DRW_SiegeBreaker_A12_TopSourcePixels", TOP_PATH)
    bottom_material = a09.image_material("MI_DRW_SiegeBreaker_A12_BottomSourcePixels", BOTTOM_PATH)
    edge_material = a09.flat_material("M_DRW_SiegeBreaker_A12_AxialEdge", (0.11, 0.13, 0.16, 1.0))
    proof_material = a09.flat_material("M_DRW_SiegeBreaker_A12_GeometryProof", (0.24, 0.28, 0.34, 1.0))

    core_mask, stone_mask, component_partition = partition_front_components(front_mask)
    core_model, core_build_stats = a09.build_half_mesh(
        front_image,
        core_mask,
        back_image,
        left_mask,
        [front_material, back_material, side_material],
    )
    stone_model, stone_build_stats = a09.build_half_mesh(
        front_image,
        stone_mask,
        back_image,
        left_mask,
        [front_material, back_material, side_material],
    )
    depth_remap = remap_stone_depth(stone_model, left_mask, top_mask, bottom_mask)
    stone_axial_owner_faces = assign_axial_owner_materials(
        stone_model,
        top_source,
        bottom_source,
        top_material,
        bottom_material,
        None,
    )
    core_axial_owner_faces = assign_axial_owner_materials(
        core_model,
        top_source,
        bottom_source,
        top_material,
        bottom_material,
        HEAD_Z_MIN,
    )
    core_model.name = f"{ASSET}_A12_CenteredCoreAndShaft"
    core_model.data.name = f"{ASSET}_A12_CenteredCoreAndShaft_Mesh"
    stone_model.name = f"{ASSET}_A12_TwoMirroredStoneStrikeMasses"
    stone_model.data.name = f"{ASSET}_A12_TwoMirroredStoneStrikeMasses_Mesh"
    for model, role in ((core_model, "centered metal core and shaft"), (stone_model, "two mirrored stone strike masses")):
        model["Aerathea.ContractID"] = CONTRACT_ID
        model["Aerathea.CorrectionID"] = "SB-AXIAL-A12-R3-COMPONENT-SEPARATION"
        model["Aerathea.ArtifactStatus"] = "DCC source candidate pending Flamestrike visual decision"
        model["Aerathea.ComponentRole"] = role
        model["Aerathea.TopBottomProofProjectionIsCandidateGeometry"] = False
    core_model["Aerathea.DepthAuthority"] = "proven A09 front/back/left pixel build"
    core_model["Aerathea.ComponentWidthCm"] = CORE_WIDTH
    stone_model["Aerathea.DepthAuthority"] = "A11 centered mean axial pixels"
    stone_model["Aerathea.ApprovedHeadDepthCm"] = TARGET_DEPTH
    stone_model["Aerathea.ComponentWidthEachCm"] = STONE_WIDTH_EACH
    stone_model["Aerathea.SideViewControlsHeadDepth"] = False

    cap_objects = {}
    relief_objects = {}
    axial_stats = {}
    for view, source, mask, material in (
        ("top", top_source, top_mask, top_material),
        ("bottom", bottom_source, bottom_mask, bottom_material),
    ):
        cap, cap_stats = build_axial_cap(view, source, mask, [material, edge_material])
        relief, relief_stats = build_axial_relief(view, source, mask, material)
        cap_objects[view] = cap
        relief_objects[view] = relief
        axial_stats[view] = {
            "selected_component_pixels": EXPECTED_A11_COUNTS[view],
            "filled_footprint_pixels": sum(1 for value in mask.getdata() if value),
            "source_rectangle_half_open": EXPECTED_A11_RECTS[view],
            "cap": cap_stats,
            "relief": relief_stats,
        }

    candidate_objects = [core_model, stone_model]
    proof_backings = [*cap_objects.values(), *relief_objects.values()]
    a09.add_lighting()
    source_px_per_cm = 1.0 / a09.FRONT_SCALE
    front_ortho = TARGET_HEIGHT * front_image.height / (a09.FRONT_RECT[3] - a09.FRONT_RECT[1])
    image_center_x = front_image.width * 0.5
    image_center_y = front_image.height * 0.5
    object_center_px_x = (a09.FRONT_RECT[0] + a09.FRONT_RECT[2]) * 0.5
    object_center_px_y = (a09.FRONT_RECT[1] + a09.FRONT_RECT[3]) * 0.5
    camera_x = -(object_center_px_x - image_center_x) / source_px_per_cm
    camera_z = TARGET_HEIGHT * 0.5 + (object_center_px_y - image_center_y) / source_px_per_cm
    front_camera = add_camera("CAM_A12_FRONT_PIXEL_REGISTERED", (camera_x, -520.0, camera_z), (camera_x, 0.0, camera_z), front_ortho)
    top_camera = axial_camera("top", EXPECTED_A11_RECTS["top"])
    bottom_camera = axial_camera("bottom", EXPECTED_A11_RECTS["bottom"])
    three_quarter = add_camera("CAM_A12_COMPLETED_THREE_QUARTER", (145.0, -235.0, 112.0), (0.0, 0.0, 84.0), 205.0)

    render(front_camera, RENDER_PATHS["front"], front_image.width, front_image.height)
    render_head_isolated("top", top_camera, RENDER_PATHS["top"], candidate_objects, cap_objects, relief_objects)
    render_head_isolated("bottom", bottom_camera, RENDER_PATHS["bottom"], candidate_objects, cap_objects, relief_objects)
    render(three_quarter, RENDER_PATHS["color_3q"], 1400, 1600)
    render_geometry_objects(candidate_objects, three_quarter, RENDER_PATHS["geometry_3q"], 1400, 1600, proof_material)

    bounds = bounds_objects(candidate_objects)
    symmetry_result = symmetry(candidate_objects)
    counts = {
        "objects": len(candidate_objects),
        "vertices": sum(len(obj.data.vertices) for obj in candidate_objects),
        "polygons": sum(len(obj.data.polygons) for obj in candidate_objects),
        "proof_backing_objects": len(proof_backings),
    }
    for obj in candidate_objects:
        obj["Aerathea.CompleteBounds"] = json.dumps(bounds, sort_keys=True)
        obj["Aerathea.CompleteSymmetry"] = json.dumps(symmetry_result, sort_keys=True)
    bpy.ops.wm.save_as_mainfile(filepath=str(BLEND_PATH))

    comparison = compose_review(sources, masks, bounds, counts)
    after_a09_hash = sha256(A09_BLEND)
    if after_a09_hash != EXPECTED_SHA256["a09_blend"]:
        raise RuntimeError(f"A09 source changed during A12 build: {after_a09_hash}")

    outputs = {
        "blend_local_only": str(BLEND_PATH.relative_to(ROOT)),
        **{name: str(path.relative_to(ROOT)) for name, path in RENDER_PATHS.items()},
        "review": str(REVIEW_BOARD.relative_to(ROOT)),
        "top_filled_mask_local_only": str(MASK_PATHS["top"].relative_to(ROOT)),
        "bottom_filled_mask_local_only": str(MASK_PATHS["bottom"].relative_to(ROOT)),
    }
    manifest = {
        "schema": "aerathea.siegebreaker.a12_axial_pixel_reconstruction_validation.v1",
        "asset": ASSET,
        "attempt": ATTEMPT,
        "contract_id": CONTRACT_ID,
        "artifact_status": "DCC source candidate pending Flamestrike visual decision",
        "software": {
            "blender": bpy.app.version_string,
            "image_generation": False,
            "trellis": False,
            "image_to_3d": False,
        },
        "authority_hashes": EXPECTED_SHA256,
        "a09_source_hash_after_build": after_a09_hash,
        "a09_source_unchanged": after_a09_hash == EXPECTED_SHA256["a09_blend"],
        "approved_axial_rule": {
            "mean_footprint_pixels": [1012.5, 597.0],
            "common_cm_per_pixel": COMMON_SCALE,
            "head_width_cm": TARGET_WIDTH,
            "head_depth_cm": TARGET_DEPTH,
            "declared_core_head_z_interval_cm": [HEAD_Z_MIN, HEAD_Z_MAX],
            "stone_depth_applies_to_complete_source_visible_stone_silhouette": True,
            "top_bottom_own_head_depth": True,
            "side_view_owns_head_depth": False,
        },
        "source_measurements": {
            "a09_component_pixels": observed_a09_counts,
            "top_metadata": top_meta,
            "bottom_metadata": bottom_meta,
        },
        "construction": {
            "component_partition": component_partition,
            "centered_core_and_shaft": core_build_stats,
            "two_mirrored_stone_strike_masses": stone_build_stats,
            "stone_depth_remap": depth_remap,
            "axial_owner_material_faces": {
                "centered_core_and_shaft": core_axial_owner_faces,
                "two_mirrored_stone_strike_masses": stone_axial_owner_faces,
            },
            "axial_surfaces": axial_stats,
            "source_half": "X>=0",
            "mirror_plane": "X=0",
            "all_mesh_mirrors_applied": all(bool(obj.get("Aerathea.MirrorApplied")) for obj in [*candidate_objects, *proof_backings]),
            "prior_candidate_geometry_inputs": 0,
            "internal_rejected_attempts": [
                "A12 R0 axial backing/relief and bottom-orientation failure",
                "A12 R1 owner-view-correct constant-Z projection sheets invalid in completed assembly",
                "A12 R2 monolithic Z=132 depth application created false center stone and horizontal ledge",
            ],
            "global_z132_to_z138_transition_used": False,
            "proof_backings_hidden_from_completed_renders": all(obj.hide_render for obj in proof_backings),
        },
        "mesh": {"counts": counts, "bounds": bounds, "symmetry": symmetry_result},
        "comparison": comparison,
        "outputs": outputs,
        "output_hashes": {name: sha256(ROOT / relative) for name, relative in outputs.items()},
        "unreal_authority": False,
        "fully_game_ready": False,
    }
    MANIFEST_PATH.write_text(json.dumps(manifest, indent=2) + "\n", encoding="utf-8")
    print(json.dumps({"status": "complete", "blend": str(BLEND_PATH), "review": str(REVIEW_BOARD), "counts": counts}, indent=2))


if __name__ == "__main__":
    main()
