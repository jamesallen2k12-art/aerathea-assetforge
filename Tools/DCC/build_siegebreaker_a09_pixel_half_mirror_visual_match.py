#!/usr/bin/env python3
"""Build the fresh Blender-only Siege Breaker A09 pixel-half visual match.

The recipe reads only immutable source PNGs and written A09 authority.  It
constructs X>=0, applies a Blender Mirror modifier at X=0, renders a source-
colored front pass and two three-quarter proof passes, and writes a validation
manifest.  No prior Siege Breaker mesh or blend is loaded.
"""

from __future__ import annotations

import hashlib
import json
import math
from collections import deque
from pathlib import Path

import bpy
from mathutils import Vector
from PIL import Image, ImageChops, ImageDraw, ImageFont, ImageStat


ROOT = Path(__file__).resolve().parents[2]
ASSET = "SM_DRW_SiegeBreaker_Hammer_A01"
ATTEMPT = "A09_PixelHalfMirror_VisualMatch_A01"
CONTRACT_ID = "SB-PHM-A09-FULL-MIRROR"
SOURCE_DIR = ROOT / "SourceAssets/Concepts/SiegeBreaker"
FRONT_PATH = SOURCE_DIR / "siege_breaker_front_view.png"
BACK_PATH = SOURCE_DIR / "siege_breaker_back_view.png"
LEFT_PATH = SOURCE_DIR / "siege_breaker_left_view.png"
CONCEPT_PATH = SOURCE_DIR / "siege_breaker_concept_view.png"

FRONT_RECT = (317, 193, 808, 1304)
BACK_RECT = (285, 193, 818, 1344)
LEFT_RECT = (397, 190, 612, 1299)
EXPECTED_COMPONENT_PIXELS = {"front": 212765, "back": 238342, "left": 118540}
EXPECTED_SHA256 = {
    "front": "d00bf9ffcfd4862884626fa961c5f6b4fd6cedfdff7936b2210ca2a905e57e95",
    "back": "15b4633f2df4ee06115ef4a7e238f287ebece1bae514ad4005c1036a57359799",
    "left": "1a23e0c24f7be4b12df93e2509b9d300acc9161a21a32b336f7cf63c1288d91b",
    "concept": "9f1ac142a5047968bb20c74216c2dccf61470ed9f4e21689ff01934bd849c586",
}

FRONT_SCALE = 170.0 / (FRONT_RECT[3] - FRONT_RECT[1])
LEFT_SCALE = 170.0 / (LEFT_RECT[3] - LEFT_RECT[1])
FRONT_CENTER_EDGE = (FRONT_RECT[0] + FRONT_RECT[2]) * 0.5
BACK_CENTER_EDGE = (BACK_RECT[0] + BACK_RECT[2]) * 0.5
LEFT_CENTER_EDGE = (LEFT_RECT[0] + LEFT_RECT[2]) * 0.5
TARGET_WIDTH = (FRONT_RECT[2] - FRONT_RECT[0]) * FRONT_SCALE
TARGET_DEPTH = (LEFT_RECT[2] - LEFT_RECT[0]) * LEFT_SCALE
TARGET_HEIGHT = 170.0

OUTPUT_ROOT = (
    ROOT
    / "SourceAssets/Blender/Weapons/Dwarven"
    / ASSET
    / ATTEMPT
)
LOCAL_RENDER_ROOT = OUTPUT_ROOT / "renders"
BLEND_PATH = OUTPUT_ROOT / f"{ASSET}_{ATTEMPT}.blend"
DOC_ROOT = ROOT / "docs/assets/blueprints" / ASSET
REVIEW_ROOT = DOC_ROOT / "review"
MANIFEST_PATH = DOC_ROOT / "manifests/A09_FULL_PIXEL_HALF_MIRROR_A01_VALIDATION.json"
FRONT_RENDER = REVIEW_ROOT / "A09_FULL_PIXEL_HALF_MIRROR_A01_FRONT.png"
COLOR_RENDER = REVIEW_ROOT / "A09_FULL_PIXEL_HALF_MIRROR_A01_COLOR_3Q.png"
GEOMETRY_RENDER = REVIEW_ROOT / "A09_FULL_PIXEL_HALF_MIRROR_A01_GEOMETRY_3Q.png"
REVIEW_BOARD = REVIEW_ROOT / "A09_FULL_PIXEL_HALF_MIRROR_A01_REVIEW.png"
MASK_PATH = OUTPUT_ROOT / "A09_front_scan_membership.png"


def sha256(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest()


def ensure_dirs() -> None:
    OUTPUT_ROOT.mkdir(parents=True, exist_ok=True)
    LOCAL_RENDER_ROOT.mkdir(parents=True, exist_ok=True)
    REVIEW_ROOT.mkdir(parents=True, exist_ok=True)


def integer_luma(rgb: tuple[int, int, int]) -> int:
    return (77 * rgb[0] + 150 * rgb[1] + 29 * rgb[2]) >> 8


def exact_component_mask(image: Image.Image, rect: tuple[int, int, int, int]) -> tuple[Image.Image, int]:
    """Replay the approved luma/8-connected greatest-component membership."""
    rgb = image.convert("RGB")
    width, height = rgb.size
    pixels = rgb.load()
    raw = bytearray(width * height)
    for y in range(height):
        for x in range(width):
            if integer_luma(pixels[x, y]) <= 234:
                raw[y * width + x] = 1

    visited = bytearray(width * height)
    best: list[int] = []
    for start in range(width * height):
        if visited[start] or not raw[start]:
            continue
        queue = [start]
        visited[start] = 1
        component: list[int] = []
        touches_edge = False
        while queue:
            current = queue.pop()
            component.append(current)
            x = current % width
            y = current // width
            if x <= 1 or y <= 1 or x >= width - 2 or y >= height - 2:
                touches_edge = True
            for ny in range(max(0, y - 1), min(height, y + 2)):
                for nx in range(max(0, x - 1), min(width, x + 2)):
                    neighbor = ny * width + nx
                    if visited[neighbor] or not raw[neighbor]:
                        continue
                    visited[neighbor] = 1
                    queue.append(neighbor)
        if not touches_edge and len(component) > len(best):
            best = component

    # Fill only holes enclosed by the exact selected component.  Exterior white
    # and source-connected negative space remain absent.
    selected_crop = Image.new("L", (rect[2] - rect[0], rect[3] - rect[1]), 0)
    selected_crop_pixels = selected_crop.load()
    for offset in best:
        x = offset % width
        y = offset // width
        if rect[0] <= x < rect[2] and rect[1] <= y < rect[3]:
            selected_crop_pixels[x - rect[0], y - rect[1]] = 255

    crop_width, crop_height = selected_crop.size
    selected_crop_bytes = selected_crop.tobytes()
    exterior = bytearray(crop_width * crop_height)
    queue: deque[int] = deque()
    for x in range(crop_width):
        for y in (0, crop_height - 1):
            offset = y * crop_width + x
            if selected_crop_bytes[offset] == 0 and not exterior[offset]:
                exterior[offset] = 1
                queue.append(offset)
    for y in range(crop_height):
        for x in (0, crop_width - 1):
            offset = y * crop_width + x
            if selected_crop_bytes[offset] == 0 and not exterior[offset]:
                exterior[offset] = 1
                queue.append(offset)
    while queue:
        current = queue.popleft()
        x = current % crop_width
        y = current // crop_width
        for nx, ny in ((x + 1, y), (x - 1, y), (x, y + 1), (x, y - 1)):
            if nx < 0 or ny < 0 or nx >= crop_width or ny >= crop_height:
                continue
            neighbor = ny * crop_width + nx
            if selected_crop_bytes[neighbor] or exterior[neighbor]:
                continue
            exterior[neighbor] = 1
            queue.append(neighbor)

    filled = Image.new("L", (crop_width, crop_height), 0)
    filled_pixels = filled.load()
    for y in range(crop_height):
        for x in range(crop_width):
            offset = y * crop_width + x
            if selected_crop_bytes[offset] or not exterior[offset]:
                filled_pixels[x, y] = 255
    return filled, len(best)


def mask_bbox_global(mask: Image.Image, rect: tuple[int, int, int, int]) -> tuple[int, int, int, int]:
    bbox = mask.getbbox()
    if bbox is None:
        raise RuntimeError("Empty source membership mask")
    return (rect[0] + bbox[0], rect[1] + bbox[1], rect[0] + bbox[2], rect[1] + bbox[3])


def profile_row_span(mask: Image.Image, row: int, search: int = 6) -> tuple[int, int]:
    pixels = mask.load()
    width, height = mask.size
    row = max(0, min(height - 1, row))
    for radius in range(search + 1):
        candidate_rows = [row] if radius == 0 else [max(0, row - radius), min(height - 1, row + radius)]
        xs: list[int] = []
        for candidate in candidate_rows:
            xs.extend(x for x in range(width) if pixels[x, candidate] > 0)
        if xs:
            return min(xs), max(xs) + 1
    raise RuntimeError(f"No profile membership near row {row}")


def depth_at_z(left_mask: Image.Image, z_cm: float) -> tuple[float, float]:
    source_edge_y = LEFT_RECT[1] + (TARGET_HEIGHT - z_cm) / LEFT_SCALE
    local_row = round(source_edge_y - LEFT_RECT[1] - 0.5)
    span = profile_row_span(left_mask, local_row)
    global_min_edge = LEFT_RECT[0] + span[0]
    global_max_edge = LEFT_RECT[0] + span[1]
    return (
        (global_min_edge - LEFT_CENTER_EDGE) * LEFT_SCALE,
        (global_max_edge - LEFT_CENTER_EDGE) * LEFT_SCALE,
    )


def clear_scene() -> None:
    bpy.ops.object.select_all(action="SELECT")
    bpy.ops.object.delete(use_global=False)
    for datablocks in (
        bpy.data.meshes,
        bpy.data.curves,
        bpy.data.materials,
        bpy.data.cameras,
        bpy.data.lights,
    ):
        for block in list(datablocks):
            if block.users == 0:
                datablocks.remove(block)
    base = bpy.context.scene.collection.children.get("Collection")
    if base is not None:
        base.name = "A09_SOURCE_HALF_AND_MIRROR"


def image_material(name: str, path: Path) -> bpy.types.Material:
    material = bpy.data.materials.new(name)
    material.use_nodes = True
    nodes = material.node_tree.nodes
    nodes.clear()
    output = nodes.new("ShaderNodeOutputMaterial")
    texture = nodes.new("ShaderNodeTexImage")
    texture.image = bpy.data.images.load(str(path), check_existing=True)
    texture.interpolation = "Closest"
    emission = nodes.new("ShaderNodeEmission")
    emission.inputs["Strength"].default_value = 1.0
    material.node_tree.links.new(texture.outputs["Color"], emission.inputs["Color"])
    material.node_tree.links.new(emission.outputs["Emission"], output.inputs["Surface"])
    material.diffuse_color = (0.18, 0.16, 0.14, 1.0)
    return material


def flat_material(name: str, color: tuple[float, float, float, float]) -> bpy.types.Material:
    material = bpy.data.materials.new(name)
    material.use_nodes = True
    bsdf = material.node_tree.nodes.get("Principled BSDF")
    bsdf.inputs["Base Color"].default_value = color
    bsdf.inputs["Roughness"].default_value = 0.72
    bsdf.inputs["Metallic"].default_value = 0.18
    material.diffuse_color = color
    return material


def build_half_mesh(
    front_image: Image.Image,
    front_mask: Image.Image,
    back_image: Image.Image,
    left_mask: Image.Image,
    materials: list[bpy.types.Material],
) -> tuple[bpy.types.Object, dict[str, int]]:
    mask_pixels = front_mask.load()
    front_rgb = front_image.convert("RGB").load()
    local_width, local_height = front_mask.size
    start_x = math.floor(FRONT_CENTER_EDGE) - FRONT_RECT[0]

    active: set[tuple[int, int]] = set()
    for local_y in range(local_height):
        for local_x in range(max(0, start_x), local_width):
            global_x = FRONT_RECT[0] + local_x
            global_center = global_x + 0.5
            if global_center + 1.0e-9 < FRONT_CENTER_EDGE:
                continue
            if mask_pixels[local_x, local_y] > 0:
                active.add((global_x, FRONT_RECT[1] + local_y))

    if not active:
        raise RuntimeError("No source-half pixels selected")

    def is_boundary_cell(x: int, y: int) -> bool:
        return any((x + dx, y + dy) not in active for dx, dy in ((1, 0), (-1, 0), (0, 1), (0, -1)))

    boundary = {cell for cell in active if is_boundary_cell(*cell)}

    vertices: list[tuple[float, float, float]] = []
    faces: list[tuple[int, ...]] = []
    face_uvs: list[list[tuple[float, float]]] = []
    face_materials: list[int] = []
    vertex_cache: dict[tuple[str, float, int], int] = {}

    def relief_at_corner(x_edge: float, y_edge: int) -> float:
        samples: list[int] = []
        touches_boundary = False
        for px in (math.floor(x_edge - 0.5), math.floor(x_edge + 0.01)):
            for py in (y_edge - 1, y_edge):
                if (px, py) not in active:
                    continue
                touches_boundary = touches_boundary or (px, py) in boundary
                samples.append(integer_luma(front_rgb[px, py]))
        if not samples or touches_boundary:
            return 0.0
        average = sum(samples) / len(samples)
        # Dark source pixels recess inward.  The bounded 0.72 cm maximum cannot
        # extend the measured owner-view envelope.
        return max(0.0, min(0.72, (234.0 - average) / 234.0 * 0.72))

    def vertex(side: str, x_edge: float, y_edge: int) -> int:
        key = (side, round(x_edge, 4), y_edge)
        if key in vertex_cache:
            return vertex_cache[key]
        world_x = (x_edge - FRONT_CENTER_EDGE) * FRONT_SCALE
        world_z = TARGET_HEIGHT - (y_edge - FRONT_RECT[1]) * FRONT_SCALE
        world_z = max(0.0, min(TARGET_HEIGHT, world_z))
        y_min, y_max = depth_at_z(left_mask, world_z)
        if side == "front":
            world_y = y_min + relief_at_corner(x_edge, y_edge)
        else:
            world_y = y_max
        index = len(vertices)
        vertices.append((world_x, world_y, world_z))
        vertex_cache[key] = index
        return index

    def front_uv(x_edge: float, y_edge: int) -> tuple[float, float]:
        return (x_edge / front_image.width, 1.0 - y_edge / front_image.height)

    def back_uv(x_edge: float, y_edge: int) -> tuple[float, float]:
        world_x = max(0.0, (x_edge - FRONT_CENTER_EDGE) * FRONT_SCALE)
        half_width = TARGET_WIDTH * 0.5
        outward = 0.0 if half_width <= 0.0 else world_x / half_width
        source_x = BACK_CENTER_EDGE - outward * (BACK_CENTER_EDGE - BACK_RECT[0])
        world_z = TARGET_HEIGHT - (y_edge - FRONT_RECT[1]) * FRONT_SCALE
        source_y = BACK_RECT[1] + (TARGET_HEIGHT - world_z) / TARGET_HEIGHT * (BACK_RECT[3] - BACK_RECT[1])
        return (source_x / back_image.width, 1.0 - source_y / back_image.height)

    def side_uv(world_y: float, world_z: float) -> tuple[float, float]:
        source_x = LEFT_CENTER_EDGE + world_y / LEFT_SCALE
        source_y = LEFT_RECT[1] + (TARGET_HEIGHT - world_z) / LEFT_SCALE
        return (source_x / 1122.0, 1.0 - source_y / 1402.0)

    def add_face(indices: tuple[int, ...], uvs: list[tuple[float, float]], material_index: int) -> None:
        faces.append(indices)
        face_uvs.append(uvs)
        face_materials.append(material_index)

    for x, y in sorted(active, key=lambda item: (item[1], item[0])):
        x0 = max(float(x), FRONT_CENTER_EDGE)
        x1 = float(x + 1)
        if x1 <= x0:
            continue
        f00 = vertex("front", x0, y)
        f10 = vertex("front", x1, y)
        f11 = vertex("front", x1, y + 1)
        f01 = vertex("front", x0, y + 1)
        b00 = vertex("back", x0, y)
        b10 = vertex("back", x1, y)
        b11 = vertex("back", x1, y + 1)
        b01 = vertex("back", x0, y + 1)

        add_face(
            (f00, f01, f11, f10),
            [front_uv(x0, y), front_uv(x0, y + 1), front_uv(x1, y + 1), front_uv(x1, y)],
            0,
        )
        add_face(
            (b00, b10, b11, b01),
            [back_uv(x0, y), back_uv(x1, y), back_uv(x1, y + 1), back_uv(x0, y + 1)],
            1,
        )

        edges = (
            ((-1, 0), x0, y, x0, y + 1, f00, f01, b01, b00),
            ((1, 0), x1, y + 1, x1, y, f11, f10, b10, b11),
            ((0, -1), x1, y, x0, y, f10, f00, b00, b10),
            ((0, 1), x0, y + 1, x1, y + 1, f01, f11, b11, b01),
        )
        for (dx, dy), ex0, ey0, ex1, ey1, fa, fb, bb, ba in edges:
            if (x + dx, y + dy) in active:
                continue
            if dx == -1 and abs(ex0 - FRONT_CENTER_EDGE) < 1.0e-6:
                continue
            world0 = vertices[fa]
            world1 = vertices[fb]
            uv0 = side_uv(world0[1], world0[2])
            uv1 = side_uv(world1[1], world1[2])
            uv2 = side_uv(vertices[bb][1], vertices[bb][2])
            uv3 = side_uv(vertices[ba][1], vertices[ba][2])
            add_face((fa, fb, bb, ba), [uv0, uv1, uv2, uv3], 2)

    mesh = bpy.data.meshes.new(f"{ASSET}_A09_SourceHalf_Mesh")
    mesh.from_pydata(vertices, [], faces)
    mesh.update(calc_edges=True)
    uv_layer = mesh.uv_layers.new(name="A09_ExactSourcePixelUV")
    for polygon, uvs, material_index in zip(mesh.polygons, face_uvs, face_materials):
        polygon.material_index = material_index
        for loop_index, uv in zip(polygon.loop_indices, uvs):
            uv_layer.data[loop_index].uv = uv

    obj = bpy.data.objects.new(f"{ASSET}_A09_SourceHalf_XPositive", mesh)
    bpy.context.scene.collection.objects.link(obj)
    for material in materials:
        obj.data.materials.append(material)
    obj["Aerathea.ContractID"] = CONTRACT_ID
    obj["Aerathea.ArtifactStatus"] = "DCC source candidate pending Flamestrike visual decision"
    obj["Aerathea.Construction"] = "fresh X>=0 native-pixel surface; Blender mirror at X=0"
    obj["Aerathea.PriorCandidateGeometryInputs"] = 0
    obj["Aerathea.SourceProjectionIsGeometryProof"] = False
    obj["Aerathea.VisualScaleCmPerPixel"] = FRONT_SCALE
    obj["Aerathea.SourceHalfActivePixels"] = len(active)

    bpy.context.view_layer.objects.active = obj
    obj.select_set(True)
    mirror = obj.modifiers.new("A09_ExactCenterPlaneMirror", "MIRROR")
    mirror.use_axis[0] = True
    mirror.use_clip = True
    mirror.use_mirror_merge = True
    mirror.merge_threshold = FRONT_SCALE * 0.01
    bpy.ops.object.modifier_apply(modifier=mirror.name)
    obj.name = f"{ASSET}_A09_CompleteMirroredModel"
    obj["Aerathea.MirrorApplied"] = True
    obj["Aerathea.SourceHalfPreservedByRule"] = True
    obj.select_set(False)

    return obj, {
        "source_half_active_pixels": len(active),
        "source_half_boundary_pixels": len(boundary),
        "half_vertices_before_mirror": len(vertices),
        "half_faces_before_mirror": len(faces),
        "complete_vertices": len(obj.data.vertices),
        "complete_polygons": len(obj.data.polygons),
    }


def add_camera(name: str, location: tuple[float, float, float], target: tuple[float, float, float], ortho: float) -> bpy.types.Object:
    data = bpy.data.cameras.new(name)
    data.type = "ORTHO"
    data.ortho_scale = ortho
    camera = bpy.data.objects.new(name, data)
    bpy.context.scene.collection.objects.link(camera)
    camera.location = location
    direction = Vector(target) - camera.location
    camera.rotation_euler = direction.to_track_quat("-Z", "Y").to_euler()
    return camera


def add_lighting() -> None:
    for name, energy, size, location in (
        ("A09_Key", 1350.0, 95.0, (-90.0, -130.0, 220.0)),
        ("A09_Fill", 850.0, 110.0, (120.0, -40.0, 120.0)),
        ("A09_Rim", 1100.0, 80.0, (40.0, 130.0, 180.0)),
    ):
        data = bpy.data.lights.new(name, "AREA")
        data.energy = energy
        data.size = size
        obj = bpy.data.objects.new(name, data)
        bpy.context.scene.collection.objects.link(obj)
        obj.location = location
        obj.rotation_euler = (Vector((0.0, 0.0, 85.0)) - obj.location).to_track_quat("-Z", "Y").to_euler()


def configure_scene() -> None:
    scene = bpy.context.scene
    scene.render.engine = "BLENDER_EEVEE"
    scene.eevee.use_gtao = True
    scene.eevee.gtao_distance = 6.0
    scene.eevee.gtao_factor = 1.25
    scene.render.image_settings.file_format = "PNG"
    scene.render.image_settings.color_mode = "RGB"
    scene.render.image_settings.color_depth = "8"
    scene.render.resolution_percentage = 100
    scene.render.film_transparent = False
    scene.world.use_nodes = True
    background = scene.world.node_tree.nodes.get("Background")
    background.inputs["Color"].default_value = (1.0, 1.0, 1.0, 1.0)
    background.inputs["Strength"].default_value = 0.8
    try:
        scene.view_settings.view_transform = "Standard"
        scene.view_settings.look = "None"
        scene.view_settings.exposure = 0.0
        scene.view_settings.gamma = 1.0
    except Exception:
        pass


def render(camera: bpy.types.Object, path: Path, width: int, height: int, override: bpy.types.Material | None = None) -> None:
    scene = bpy.context.scene
    scene.camera = camera
    scene.render.resolution_x = width
    scene.render.resolution_y = height
    scene.render.filepath = str(path)
    scene.view_layers[0].material_override = override
    bpy.ops.render.render(write_still=True)
    scene.view_layers[0].material_override = None


def render_geometry_proof(
    model: bpy.types.Object,
    camera: bpy.types.Object,
    path: Path,
    width: int,
    height: int,
    geometry_material: bpy.types.Material,
) -> None:
    original_materials = [slot.material for slot in model.material_slots]
    original_indices = [polygon.material_index for polygon in model.data.polygons]
    model.data.materials.clear()
    model.data.materials.append(geometry_material)
    for polygon in model.data.polygons:
        polygon.material_index = 0
    render(camera, path, width, height)
    model.data.materials.clear()
    for material in original_materials:
        model.data.materials.append(material)
    for polygon, material_index in zip(model.data.polygons, original_indices):
        polygon.material_index = material_index


def font(size: int) -> ImageFont.ImageFont:
    for candidate in (
        "/usr/share/fonts/truetype/dejavu/DejaVuSans.ttf",
        "/usr/share/fonts/dejavu-sans-fonts/DejaVuSans.ttf",
        "/usr/share/fonts/dejavu/DejaVuSans.ttf",
    ):
        if Path(candidate).exists():
            return ImageFont.truetype(candidate, size)
    return ImageFont.load_default()


def fit_panel(image: Image.Image, size: tuple[int, int], background: tuple[int, int, int] = (245, 243, 238)) -> Image.Image:
    value = image.convert("RGB")
    resampling = getattr(Image, "Resampling", Image)
    value.thumbnail(size, resampling.LANCZOS)
    panel = Image.new("RGB", size, background)
    panel.paste(value, ((size[0] - value.width) // 2, (size[1] - value.height) // 2))
    return panel


def compose_review(
    source: Image.Image,
    candidate: Image.Image,
    color_3q: Image.Image,
    geometry_3q: Image.Image,
    source_mask: Image.Image,
) -> dict[str, float | int]:
    source_rgb = source.convert("RGB")
    candidate_rgb = candidate.convert("RGB")
    crop_box = (250, 150, 875, 1365)
    source_crop = source_rgb.crop(crop_box)
    candidate_crop = candidate_rgb.crop(crop_box)
    difference = ImageChops.difference(source_crop, candidate_crop)
    amplified = difference.point(lambda value: min(255, value * 4))

    mask_global = Image.new("L", source_rgb.size, 0)
    mask_global.paste(source_mask, (FRONT_RECT[0], FRONT_RECT[1]))
    right_half_mask = Image.new("L", source_rgb.size, 0)
    right_pixels = right_half_mask.load()
    source_mask_pixels = mask_global.load()
    for y in range(source_rgb.height):
        for x in range(math.ceil(FRONT_CENTER_EDGE), source_rgb.width):
            if source_mask_pixels[x, y] > 0:
                right_pixels[x, y] = 255
    stat = ImageStat.Stat(ImageChops.difference(source_rgb, candidate_rgb), mask=right_half_mask)
    right_mean_abs_rgb = sum(stat.mean) / 3.0

    canvas = Image.new("RGB", (3000, 2050), (235, 232, 224))
    draw = ImageDraw.Draw(canvas)
    title = font(54)
    body = font(28)
    small = font(23)
    draw.text((70, 44), "Siege Breaker A09 - Full Pixel-Half Mirror Visual Match", fill=(28, 26, 23), font=title)
    draw.text(
        (72, 112),
        "Original source pixels -> fresh X>=0 Blender half -> exact center-plane mirror. Blender only; no generated imagery.",
        fill=(68, 62, 54),
        font=body,
    )
    panel_size = (680, 1280)
    panels = [
        ("UNCHANGED FRONT SOURCE", fit_panel(source_crop, panel_size)),
        ("BLENDER COMPLETED FRONT", fit_panel(candidate_crop, panel_size)),
        ("4× PIXEL DIFFERENCE", fit_panel(amplified, panel_size, (255, 255, 255))),
    ]
    for index, (label, panel) in enumerate(panels):
        x = 70 + index * 730
        draw.text((x, 175), label, fill=(43, 40, 36), font=body)
        canvas.paste(panel, (x, 220))
        draw.rectangle((x, 220, x + panel_size[0], 220 + panel_size[1]), outline=(94, 87, 77), width=3)

    proof_size = (650, 650)
    canvas.paste(fit_panel(color_3q, proof_size), (2250, 220))
    canvas.paste(fit_panel(geometry_3q, proof_size), (2250, 965))
    draw.text((2250, 175), "COLORED COMPLETE 3/4", fill=(43, 40, 36), font=body)
    draw.text((2250, 920), "UNTEXTURED GEOMETRY PROOF", fill=(43, 40, 36), font=body)
    draw.rectangle((2250, 220, 2900, 870), outline=(94, 87, 77), width=3)
    draw.rectangle((2250, 965, 2900, 1615), outline=(94, 87, 77), width=3)

    notes = [
        f"Uniform source scale: 170 / 1111 = {FRONT_SCALE:.9f} cm per pixel",
        f"Measured visual envelope: {TARGET_WIDTH:.6f} x {TARGET_DEPTH:.6f} x {TARGET_HEIGHT:.6f} cm",
        f"Right-half source-color mean absolute RGB delta: {right_mean_abs_rgb:.3f} / 255",
        "Geometry proof uses a flat material override; source projection cannot hide the mirrored volume.",
        "Status: DCC source candidate pending Flamestrike visual decision.",
    ]
    y = 1660
    for line in notes:
        draw.text((80, y), line, fill=(54, 49, 43), font=small)
        y += 58
    canvas.save(REVIEW_BOARD)
    return {"right_half_mean_absolute_rgb_delta": round(right_mean_abs_rgb, 6)}


def mesh_bounds(obj: bpy.types.Object) -> dict[str, list[float]]:
    coords = [obj.matrix_world @ vertex.co for vertex in obj.data.vertices]
    minimum = [min(value[index] for value in coords) for index in range(3)]
    maximum = [max(value[index] for value in coords) for index in range(3)]
    return {
        "min_cm": [round(value, 6) for value in minimum],
        "max_cm": [round(value, 6) for value in maximum],
        "dimensions_cm": [round(maximum[index] - minimum[index], 6) for index in range(3)],
    }


def symmetry_check(obj: bpy.types.Object) -> dict[str, int | bool]:
    coordinates = {
        (round(vertex.co.x, 5), round(vertex.co.y, 5), round(vertex.co.z, 5))
        for vertex in obj.data.vertices
    }
    missing = 0
    for x, y, z in coordinates:
        if (-x, y, z) not in coordinates:
            missing += 1
    return {"unique_vertices": len(coordinates), "missing_mirrored_vertices": missing, "pass": missing == 0}


def main() -> None:
    ensure_dirs()
    for name, path in (("front", FRONT_PATH), ("back", BACK_PATH), ("left", LEFT_PATH), ("concept", CONCEPT_PATH)):
        actual = sha256(path)
        if actual != EXPECTED_SHA256[name]:
            raise RuntimeError(f"Source hash mismatch for {name}: {actual}")

    front_image = Image.open(FRONT_PATH).convert("RGB")
    back_image = Image.open(BACK_PATH).convert("RGB")
    left_image = Image.open(LEFT_PATH).convert("RGB")
    front_mask, front_count = exact_component_mask(front_image, FRONT_RECT)
    back_mask, back_count = exact_component_mask(back_image, BACK_RECT)
    left_mask, left_count = exact_component_mask(left_image, LEFT_RECT)
    observed_counts = {"front": front_count, "back": back_count, "left": left_count}
    if observed_counts != EXPECTED_COMPONENT_PIXELS:
        raise RuntimeError(f"Exact membership replay mismatch: {observed_counts}")
    front_mask.save(MASK_PATH)

    clear_scene()
    configure_scene()
    materials = [
        image_material("MI_DRW_SiegeBreaker_A09_FrontSourcePixels", FRONT_PATH),
        image_material("MI_DRW_SiegeBreaker_A09_BackSourcePixels", BACK_PATH),
        image_material("MI_DRW_SiegeBreaker_A09_LeftSourcePixels", LEFT_PATH),
    ]
    geometry_material = flat_material("M_DRW_SiegeBreaker_A09_GeometryProof", (0.22, 0.26, 0.31, 1.0))
    model, build_stats = build_half_mesh(front_image, front_mask, back_image, left_mask, materials)
    add_lighting()

    source_px_per_cm = 1.0 / FRONT_SCALE
    front_ortho = TARGET_HEIGHT * front_image.height / (FRONT_RECT[3] - FRONT_RECT[1])
    image_center_x = front_image.width * 0.5
    image_center_y = front_image.height * 0.5
    object_center_px_x = (FRONT_RECT[0] + FRONT_RECT[2]) * 0.5
    object_center_px_y = (FRONT_RECT[1] + FRONT_RECT[3]) * 0.5
    camera_x = -(object_center_px_x - image_center_x) / source_px_per_cm
    camera_z = TARGET_HEIGHT * 0.5 + (object_center_px_y - image_center_y) / source_px_per_cm
    front_camera = add_camera(
        "CAM_A09_FrontPixelRegistered",
        (camera_x, -500.0, camera_z),
        (camera_x, 0.0, camera_z),
        front_ortho,
    )
    three_quarter = add_camera(
        "CAM_A09_CompletedThreeQuarter",
        (145.0, -235.0, 112.0),
        (0.0, 0.0, 84.0),
        205.0,
    )

    render(front_camera, FRONT_RENDER, front_image.width, front_image.height)
    render(three_quarter, COLOR_RENDER, 1200, 1500)
    render_geometry_proof(model, three_quarter, GEOMETRY_RENDER, 1200, 1500, geometry_material)

    bounds = mesh_bounds(model)
    symmetry = symmetry_check(model)
    model["Aerathea.Bounds"] = json.dumps(bounds, sort_keys=True)
    model["Aerathea.Symmetry"] = json.dumps(symmetry, sort_keys=True)
    bpy.ops.wm.save_as_mainfile(filepath=str(BLEND_PATH))

    comparison = compose_review(
        front_image,
        Image.open(FRONT_RENDER),
        Image.open(COLOR_RENDER),
        Image.open(GEOMETRY_RENDER),
        front_mask,
    )

    manifest = {
        "schema": "aerathea.siegebreaker.a09_pixel_half_mirror_validation.v1",
        "asset": ASSET,
        "attempt": ATTEMPT,
        "contract_id": CONTRACT_ID,
        "artifact_status": "DCC source candidate pending Flamestrike visual decision",
        "software": {"blender": bpy.app.version_string, "image_generation": False, "trellis": False},
        "source_hashes": {name: EXPECTED_SHA256[name] for name in EXPECTED_SHA256},
        "source_rectangles_half_open": {"front": FRONT_RECT, "back": BACK_RECT, "left": LEFT_RECT},
        "exact_component_membership_pixels": observed_counts,
        "visual_match_scale": {
            "authority": "uniform source-pixel proportions",
            "cm_per_front_pixel": FRONT_SCALE,
            "cm_per_left_pixel": LEFT_SCALE,
            "overall_length_anchor_cm": 170.0,
            "printed_52cm_width_used": False,
            "target_envelope_cm": [TARGET_WIDTH, TARGET_DEPTH, TARGET_HEIGHT],
        },
        "construction": {
            "source_half": "X>=0",
            "mirror_plane": "X=0",
            "mirror_applied": True,
            "prior_candidate_geometry_inputs": 0,
            "source_projection_is_geometry_proof": False,
            "inward_relief_max_cm": 0.72,
            **build_stats,
        },
        "mesh_bounds": bounds,
        "symmetry": symmetry,
        "comparison": comparison,
        "outputs": {
            "blend_local_only": str(BLEND_PATH.relative_to(ROOT)),
            "front_render": str(FRONT_RENDER.relative_to(ROOT)),
            "color_3q": str(COLOR_RENDER.relative_to(ROOT)),
            "geometry_3q": str(GEOMETRY_RENDER.relative_to(ROOT)),
            "review": str(REVIEW_BOARD.relative_to(ROOT)),
        },
        "output_hashes": {
            "blend": sha256(BLEND_PATH),
            "front_render": sha256(FRONT_RENDER),
            "color_3q": sha256(COLOR_RENDER),
            "geometry_3q": sha256(GEOMETRY_RENDER),
            "review": sha256(REVIEW_BOARD),
        },
        "unreal_authority": False,
        "fully_game_ready": False,
    }
    MANIFEST_PATH.write_text(json.dumps(manifest, indent=2) + "\n", encoding="utf-8")
    print(json.dumps({"status": "complete", "manifest": str(MANIFEST_PATH), "review": str(REVIEW_BOARD)}, indent=2))


if __name__ == "__main__":
    main()
