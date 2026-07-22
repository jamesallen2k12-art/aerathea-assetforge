#!/usr/bin/env python3
"""Build the fresh Siege Breaker R5 registered one-half mirror candidate.

R5 consumes only the immutable front/back/left/right source PNGs.  The front
positive half supplies world X, the corresponding reversed back half supplies
back color, and the registered right view supplies world Y depth.  The complete
positive-X mesh is mirrored at X=0; the reversed left view owns negative-X side
pixels.  The haft is a true profiled cylinder with separate front/back 180-degree
material sets and one static UVMap.  No R4 geometry or blend is loaded.
"""

from __future__ import annotations

import hashlib
import json
import math
import statistics
import sys
from pathlib import Path

import bpy
from mathutils import Vector
from PIL import Image, ImageDraw, ImageFont


ROOT = Path(__file__).resolve().parents[2]
sys.path.insert(0, str(ROOT / "Tools/DCC"))
import build_siegebreaker_a09_pixel_half_mirror_visual_match as a09  # noqa: E402


ASSET = "SM_DRW_SiegeBreaker_Hammer_A01"
CONTRACT_ID = "SB-AXIAL-A12-R5-FOUR-VIEW-WHOLE-ASSEMBLY"
ATTEMPT = "A12_R5_CylindricalHaft_A04"
SOURCE_DIR = ROOT / "SourceAssets/Concepts/SiegeBreaker"
SOURCES = {
    "front": SOURCE_DIR / "siege_breaker_front_view.png",
    "back": SOURCE_DIR / "siege_breaker_back_view.png",
    "left": SOURCE_DIR / "siege_breaker_left_view.png",
    "right": SOURCE_DIR / "siege_breaker_right_view.png",
}
RECTS = {
    "front": (317, 193, 808, 1304),
    "back": (285, 193, 818, 1344),
    "left": (397, 190, 612, 1299),
    "right": (467, 172, 681, 1270),
}
EXPECTED_COUNTS = {"front": 212765, "back": 238342, "left": 118540, "right": 116948}
EXPECTED_HASHES = {
    "front": "d00bf9ffcfd4862884626fa961c5f6b4fd6cedfdff7936b2210ca2a905e57e95",
    "back": "15b4633f2df4ee06115ef4a7e238f287ebece1bae514ad4005c1036a57359799",
    "left": "1a23e0c24f7be4b12df93e2509b9d300acc9161a21a32b336f7cf63c1288d91b",
    "right": "04a1e9359d518b1dec35fe161020bd23ab9e2f8d5934f24e4184aecaa91d8330",
}
TARGET_HEIGHT = 170.0
AXIS_STATIONS = (90.0, 95.0, 100.0)

OUTPUT_ROOT = ROOT / "SourceAssets/Blender/Weapons/Dwarven" / ASSET / ATTEMPT
RENDER_ROOT = OUTPUT_ROOT / "renders"
BLEND_PATH = OUTPUT_ROOT / f"{ASSET}_{ATTEMPT}.blend"
DOC_ROOT = ROOT / "docs/assets/blueprints" / ASSET
REVIEW_ROOT = DOC_ROOT / "review"
MANIFEST_PATH = DOC_ROOT / "manifests/A12_R5_CYLINDRICAL_HAFT_A04_VALIDATION.json"
RENDER_PATHS = {
    "front": REVIEW_ROOT / "A12_R5_CYLINDRICAL_HAFT_A04_FRONT.png",
    "back": REVIEW_ROOT / "A12_R5_CYLINDRICAL_HAFT_A04_BACK.png",
    "left": REVIEW_ROOT / "A12_R5_CYLINDRICAL_HAFT_A04_LEFT.png",
    "right": REVIEW_ROOT / "A12_R5_CYLINDRICAL_HAFT_A04_RIGHT.png",
    "color_3q": REVIEW_ROOT / "A12_R5_CYLINDRICAL_HAFT_A04_COLOR_3Q.png",
    "geometry_3q": REVIEW_ROOT / "A12_R5_CYLINDRICAL_HAFT_A04_GEOMETRY_3Q.png",
    "review": REVIEW_ROOT / "A12_R5_CYLINDRICAL_HAFT_A04_REVIEW.png",
}
LEFT_COMPOSITE_PATH = OUTPUT_ROOT / "A12_R5_left_owner_over_mirrored_right_pixels.png"
BACK_COMPOSITE_PATH = OUTPUT_ROOT / "A12_R5_back_owner_over_reversed_front_pixels.png"
FRONT_HAFT_TEXTURE_PATH = OUTPUT_ROOT / "A12_R5_front_haft_15708_static_uv.png"
BACK_HAFT_TEXTURE_PATH = OUTPUT_ROOT / "A12_R5_back_haft_15708_static_uv.png"
HAFT_Z_MIN_CM = 30.0
HAFT_Z_MAX_CM = 109.25
HAFT_TEXTURE_WIDTH_FACTOR = 1.5708
HAFT_HALF_ANGULAR_SEGMENTS = 16


def sha256(path: Path) -> str:
    digest = hashlib.sha256()
    with path.open("rb") as handle:
        for block in iter(lambda: handle.read(1024 * 1024), b""):
            digest.update(block)
    return digest.hexdigest()


def ensure_dirs() -> None:
    OUTPUT_ROOT.mkdir(parents=True, exist_ok=True)
    RENDER_ROOT.mkdir(parents=True, exist_ok=True)
    REVIEW_ROOT.mkdir(parents=True, exist_ok=True)


def scale_for(view: str) -> float:
    rect = RECTS[view]
    return TARGET_HEIGHT / float(rect[3] - rect[1])


def source_row(mask: Image.Image, view: str, z_cm: float) -> int:
    scale = scale_for(view)
    return max(0, min(mask.height - 1, int(round((TARGET_HEIGHT - z_cm) / scale - 0.5))))


def row_span(mask: Image.Image, view: str, z_cm: float, search: int = 7) -> tuple[int, int, int]:
    row = source_row(mask, view, z_cm)
    pixels = mask.load()
    for radius in range(search + 1):
        candidates = [row] if radius == 0 else [max(0, row - radius), min(mask.height - 1, row + radius)]
        for candidate in candidates:
            xs = [x for x in range(mask.width) if pixels[x, candidate] > 0]
            if xs:
                return min(xs), max(xs) + 1, candidate
    raise RuntimeError(f"No {view} membership near Z={z_cm:.6f} cm")


def derive_axis(mask: Image.Image, view: str) -> tuple[float, list[dict[str, float | int | list[int]]]]:
    rect = RECTS[view]
    samples: list[dict[str, float | int | list[int]]] = []
    centers: list[float] = []
    for station in AXIS_STATIONS:
        x0, x1, row = row_span(mask, view, station)
        global_center = rect[0] + (x0 + x1) * 0.5
        centers.append(global_center)
        samples.append(
            {
                "z_cm": station,
                "local_row": row,
                "local_interval_half_open": [x0, x1],
                "global_center_edge_px": global_center,
            }
        )
    return float(statistics.median(centers)), samples


def registered_depth(mask: Image.Image, axis_px: float, z_cm: float) -> tuple[float, float]:
    x0, x1, _ = row_span(mask, "right", z_cm)
    rect = RECTS["right"]
    scale = scale_for("right")
    return ((rect[0] + x0 - axis_px) * scale, (rect[0] + x1 - axis_px) * scale)


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
    return material


def build_haft_texture(
    view: str,
    image: Image.Image,
    mask: Image.Image,
    output_path: Path,
) -> dict[str, object]:
    """Create a deterministic source-pixel unwrap widened by exactly 1.5708.

    Every output row is sampled from the exact source-owned diameter at the
    corresponding Z.  Nearest-neighbor sampling preserves source pixel values;
    no painting, filling, synthesis, or generated imagery is used.
    """
    scale = scale_for(view)
    height = max(2, int(round((HAFT_Z_MAX_CM - HAFT_Z_MIN_CM) / scale)) + 1)
    spans: list[tuple[int, int, int]] = []
    maximum_diameter = 0
    for output_y in range(height):
        fraction = output_y / float(height - 1)
        z_cm = HAFT_Z_MAX_CM - fraction * (HAFT_Z_MAX_CM - HAFT_Z_MIN_CM)
        x0, x1, local_y = row_span(mask, view, z_cm)
        spans.append((x0, x1, local_y))
        maximum_diameter = max(maximum_diameter, x1 - x0)
    width = max(2, int(round(maximum_diameter * HAFT_TEXTURE_WIDTH_FACTOR)))
    result = Image.new("RGB", (width, height))
    result_pixels = result.load()
    source_pixels = image.load()
    rect = RECTS[view]
    source_samples: set[tuple[int, int]] = set()
    for output_y, (x0, x1, local_y) in enumerate(spans):
        diameter = max(1, x1 - x0)
        global_y = rect[1] + local_y
        for output_x in range(width):
            source_local_x = x0 + min(diameter - 1, int((output_x + 0.5) * diameter / width))
            global_x = rect[0] + source_local_x
            result_pixels[output_x, output_y] = source_pixels[global_x, global_y]
            source_samples.add((global_x, global_y))
    result.save(output_path)
    return {
        "view": view,
        "z_interval_cm": [HAFT_Z_MIN_CM, HAFT_Z_MAX_CM],
        "maximum_source_diameter_px": maximum_diameter,
        "widen_factor": HAFT_TEXTURE_WIDTH_FACTOR,
        "output_dimensions_px": [width, height],
        "resampling": "nearest exact source-pixel sampling",
        "unique_source_pixels_sampled": len(source_samples),
        "generated_imagery": False,
    }


def uv_for(view: str, world_x: float, world_y: float, world_z: float, axes: dict[str, float], images: dict[str, Image.Image]) -> tuple[float, float]:
    scale = scale_for(view)
    if view == "front":
        source_x = axes[view] + world_x / scale
    elif view == "back":
        source_x = axes[view] - world_x / scale
    elif view == "right":
        source_x = axes[view] + world_y / scale
    elif view == "left":
        # The opposite-X camera supplies the visual reversal.  World Y remains
        # registered with the same sign so the source is not double-flipped.
        source_x = axes[view] + world_y / scale
    else:
        raise ValueError(view)
    source_y = RECTS[view][1] + (TARGET_HEIGHT - world_z) / scale
    return (source_x / images[view].width, 1.0 - source_y / images[view].height)


def build_registered_half(
    images: dict[str, Image.Image],
    masks: dict[str, Image.Image],
    axes: dict[str, float],
    materials: list[bpy.types.Material],
) -> tuple[bpy.types.Object, dict[str, object]]:
    front_mask = masks["front"]
    front_pixels = front_mask.load()
    front_rgb = images["front"].convert("RGB").load()
    front_rect = RECTS["front"]
    front_scale = scale_for("front")
    axis = axes["front"]
    start_local = max(0, int(math.floor(axis)) - front_rect[0])

    active: set[tuple[int, int]] = set()
    haft_pixels_removed = 0
    for local_y in range(front_mask.height):
        for local_x in range(start_local, front_mask.width):
            global_x = front_rect[0] + local_x
            if global_x + 1.0 <= axis + 1.0e-9:
                continue
            if front_pixels[local_x, local_y] == 0:
                continue
            global_y = front_rect[1] + local_y
            world_z_center = TARGET_HEIGHT - (global_y + 0.5 - front_rect[1]) * front_scale
            if HAFT_Z_MIN_CM <= world_z_center < HAFT_Z_MAX_CM:
                haft_pixels_removed += 1
                continue
            active.add((global_x, global_y))
    if not active:
        raise RuntimeError("R5 positive source half is empty")

    def boundary_cell(x: int, y: int) -> bool:
        return any((x + dx, y + dy) not in active for dx, dy in ((1, 0), (-1, 0), (0, 1), (0, -1)))

    boundary = {cell for cell in active if boundary_cell(*cell)}
    vertices: list[tuple[float, float, float]] = []
    faces: list[tuple[int, ...]] = []
    face_materials: list[int] = []
    vertex_cache: dict[tuple[str, float, int], int] = {}

    def relief(x_edge: float, y_edge: int) -> float:
        values: list[int] = []
        touches = False
        for px in (math.floor(x_edge - 0.5), math.floor(x_edge + 0.01)):
            for py in (y_edge - 1, y_edge):
                if (px, py) not in active:
                    continue
                touches = touches or (px, py) in boundary
                values.append(a09.integer_luma(front_rgb[px, py]))
        if not values or touches:
            return 0.0
        return max(0.0, min(0.45, (234.0 - sum(values) / len(values)) / 234.0 * 0.45))

    def vertex(side: str, x_edge: float, y_edge: int) -> int:
        key = (side, round(x_edge, 5), y_edge)
        if key in vertex_cache:
            return vertex_cache[key]
        world_x = (x_edge - axis) * front_scale
        world_z = max(0.0, min(TARGET_HEIGHT, TARGET_HEIGHT - (y_edge - front_rect[1]) * front_scale))
        depth_min, depth_max = registered_depth(masks["right"], axes["right"], world_z)
        world_y = depth_min + relief(x_edge, y_edge) if side == "front" else depth_max
        index = len(vertices)
        vertices.append((world_x, world_y, world_z))
        vertex_cache[key] = index
        return index

    def add_face(indices: tuple[int, ...], material_index: int) -> None:
        faces.append(indices)
        face_materials.append(material_index)

    for x, y in sorted(active, key=lambda item: (item[1], item[0])):
        x0 = max(float(x), axis)
        x1 = float(x + 1)
        if x1 <= x0:
            continue
        f00, f10 = vertex("front", x0, y), vertex("front", x1, y)
        f11, f01 = vertex("front", x1, y + 1), vertex("front", x0, y + 1)
        b00, b10 = vertex("back", x0, y), vertex("back", x1, y)
        b11, b01 = vertex("back", x1, y + 1), vertex("back", x0, y + 1)
        add_face((f00, f01, f11, f10), 0)
        add_face((b00, b10, b11, b01), 1)
        edges = (
            ((-1, 0), x0, f00, f01, b01, b00),
            ((1, 0), x1, f11, f10, b10, b11),
            ((0, -1), None, f10, f00, b00, b10),
            ((0, 1), None, f01, f11, b11, b01),
        )
        for (dx, dy), edge_x, fa, fb, bb, ba in edges:
            if (x + dx, y + dy) in active:
                continue
            if dx == -1 and edge_x is not None and abs(edge_x - axis) < 1.0e-6:
                continue
            add_face((fa, fb, bb, ba), 2)

    mesh = bpy.data.meshes.new(f"{ASSET}_R5_SourceHalf_Mesh")
    mesh.from_pydata(vertices, [], faces)
    mesh.update(calc_edges=True)
    obj = bpy.data.objects.new(f"{ASSET}_R5_SourceHalf_XPositive", mesh)
    bpy.context.scene.collection.objects.link(obj)
    for material in materials:
        obj.data.materials.append(material)
    for polygon, material_index in zip(mesh.polygons, face_materials):
        polygon.material_index = material_index

    bpy.context.view_layer.objects.active = obj
    obj.select_set(True)
    mirror = obj.modifiers.new("R5_ExactCenterPlaneMirror", "MIRROR")
    mirror.use_axis[0] = True
    mirror.use_clip = True
    mirror.use_mirror_merge = True
    mirror.merge_threshold = front_scale * 0.01
    bpy.ops.object.modifier_apply(modifier=mirror.name)
    obj.select_set(False)
    obj.name = f"{ASSET}_A12_R5_CompleteMirroredAssembly"

    uv_layer = obj.data.uv_layers.new(name="A12_R5_FixedRegisteredFourViewUV")
    material_counts = {"front": 0, "back": 0, "right": 0, "left": 0}
    view_for_index = {0: "front", 1: "back", 2: "right", 3: "left"}
    for polygon in obj.data.polygons:
        center_x = sum(obj.data.vertices[index].co.x for index in polygon.vertices) / len(polygon.vertices)
        if polygon.material_index == 2 and center_x < -1.0e-6:
            polygon.material_index = 3
        view = view_for_index[polygon.material_index]
        material_counts[view] += 1
        for loop_index in polygon.loop_indices:
            coordinate = obj.data.vertices[obj.data.loops[loop_index].vertex_index].co
            uv_layer.data[loop_index].uv = uv_for(view, coordinate.x, coordinate.y, coordinate.z, axes, images)

    obj["Aerathea.ContractID"] = CONTRACT_ID
    obj["Aerathea.ArtifactStatus"] = "DCC source candidate pending Flamestrike visual decision"
    obj["Aerathea.Construction"] = "fresh registered X>=0 source half; exact X=0 mirror"
    obj["Aerathea.PriorCandidateGeometryInputs"] = 0
    obj["Aerathea.DepthAuthority"] = "registered right-view pixels about measured shaft axis"
    obj["Aerathea.LeftViewRole"] = "reversed -X surface pixels and comparison; no independent geometry"
    obj["Aerathea.A11DepthUsed"] = False
    obj["Aerathea.MirrorApplied"] = True
    obj["Aerathea.HaftGeometry"] = "removed from facade; supplied by separate true cylindrical object"

    return obj, {
        "source_half_active_pixels": len(active),
        "source_half_boundary_pixels": len(boundary),
        "half_vertices_before_mirror": len(vertices),
        "half_faces_before_mirror": len(faces),
        "complete_vertices": len(obj.data.vertices),
        "complete_polygons": len(obj.data.polygons),
        "material_face_counts": material_counts,
        "front_pixels_rejected_by_back_membership_intersection": 0,
        "haft_source_pixels_removed_from_facade": haft_pixels_removed,
    }


def build_cylindrical_haft(
    masks: dict[str, Image.Image],
    axes: dict[str, float],
    materials: list[bpy.types.Material],
) -> tuple[bpy.types.Object, dict[str, object]]:
    """Build the approved X>=0 profiled cylinder, mirror it, and assign static UVs."""
    front_mask = masks["front"]
    front_rect = RECTS["front"]
    front_scale = scale_for("front")
    ring_segments = max(2, int(round((HAFT_Z_MAX_CM - HAFT_Z_MIN_CM) / front_scale)))
    ring_count = ring_segments + 1
    angle_count = HAFT_HALF_ANGULAR_SEGMENTS + 1
    vertices: list[tuple[float, float, float]] = []
    radii: list[float] = []

    for ring_index in range(ring_count):
        fraction = ring_index / float(ring_segments)
        z_cm = HAFT_Z_MIN_CM + fraction * (HAFT_Z_MAX_CM - HAFT_Z_MIN_CM)
        _x0, x1, _row = row_span(front_mask, "front", z_cm)
        radius = max(front_scale * 0.5, (front_rect[0] + x1 - axes["front"]) * front_scale)
        radii.append(radius)
        for angle_index in range(angle_count):
            theta = -math.pi * 0.5 + math.pi * angle_index / HAFT_HALF_ANGULAR_SEGMENTS
            vertices.append((radius * math.cos(theta), radius * math.sin(theta), z_cm))

    faces: list[tuple[int, ...]] = []
    face_materials: list[int] = []
    for ring_index in range(ring_segments):
        base0 = ring_index * angle_count
        base1 = (ring_index + 1) * angle_count
        for angle_index in range(HAFT_HALF_ANGULAR_SEGMENTS):
            faces.append(
                (
                    base0 + angle_index,
                    base0 + angle_index + 1,
                    base1 + angle_index + 1,
                    base1 + angle_index,
                )
            )
            theta_mid = -math.pi * 0.5 + math.pi * (angle_index + 0.5) / HAFT_HALF_ANGULAR_SEGMENTS
            face_materials.append(0 if math.sin(theta_mid) < 0.0 else 1)

    bottom_center = len(vertices)
    vertices.append((0.0, 0.0, HAFT_Z_MIN_CM))
    top_center = len(vertices)
    vertices.append((0.0, 0.0, HAFT_Z_MAX_CM))
    top_base = (ring_count - 1) * angle_count
    for angle_index in range(HAFT_HALF_ANGULAR_SEGMENTS):
        theta_mid = -math.pi * 0.5 + math.pi * (angle_index + 0.5) / HAFT_HALF_ANGULAR_SEGMENTS
        material_index = 0 if math.sin(theta_mid) < 0.0 else 1
        faces.append((bottom_center, angle_index + 1, angle_index))
        face_materials.append(material_index)
        faces.append((top_center, top_base + angle_index, top_base + angle_index + 1))
        face_materials.append(material_index)

    mesh = bpy.data.meshes.new(f"{ASSET}_R5_CylindricalHaftHalf_Mesh")
    mesh.from_pydata(vertices, [], faces)
    mesh.update(calc_edges=True)
    obj = bpy.data.objects.new(f"{ASSET}_R5_CylindricalHaft_XPositive", mesh)
    bpy.context.scene.collection.objects.link(obj)
    for material in materials:
        obj.data.materials.append(material)
    for polygon, material_index in zip(mesh.polygons, face_materials):
        polygon.material_index = material_index
        polygon.use_smooth = len(polygon.vertices) == 4

    bpy.context.view_layer.objects.active = obj
    obj.select_set(True)
    mirror = obj.modifiers.new("R5_CylindricalHaft_ExactCenterPlaneMirror", "MIRROR")
    mirror.use_axis[0] = True
    mirror.use_clip = True
    mirror.use_mirror_merge = True
    mirror.merge_threshold = front_scale * 0.01
    bpy.ops.object.modifier_apply(modifier=mirror.name)
    obj.select_set(False)
    obj.name = f"{ASSET}_A12_R5_CylindricalHaft_CompleteMirror"

    uv_layer = obj.data.uv_layers.new(name="UVMap")
    uv_ranges = {"front": [1.0, 0.0, 1.0, 0.0], "back": [1.0, 0.0, 1.0, 0.0]}
    for polygon in obj.data.polygons:
        owner = "front" if polygon.material_index == 0 else "back"
        for loop_index in polygon.loop_indices:
            coordinate = obj.data.vertices[obj.data.loops[loop_index].vertex_index].co
            angle = math.atan2(coordinate.y, coordinate.x)
            if owner == "front":
                if angle > 0.0:
                    angle -= 2.0 * math.pi
                u = (angle + math.pi) / math.pi
            else:
                if angle < 0.0:
                    angle += 2.0 * math.pi
                u = angle / math.pi
            v = (coordinate.z - HAFT_Z_MIN_CM) / (HAFT_Z_MAX_CM - HAFT_Z_MIN_CM)
            u = max(0.0, min(1.0, u))
            v = max(0.0, min(1.0, v))
            uv_layer.data[loop_index].uv = (u, v)
            uv_ranges[owner][0] = min(uv_ranges[owner][0], u)
            uv_ranges[owner][1] = max(uv_ranges[owner][1], u)
            uv_ranges[owner][2] = min(uv_ranges[owner][2], v)
            uv_ranges[owner][3] = max(uv_ranges[owner][3], v)

    obj["Aerathea.ContractID"] = CONTRACT_ID
    obj["Aerathea.ArtifactStatus"] = "DCC source candidate pending Flamestrike visual decision"
    obj["Aerathea.Component"] = "true cylindrical haft"
    obj["Aerathea.Construction"] = "profiled X>=0 half; exact X=0 mirror"
    obj["Aerathea.Axis"] = "X=0,Y=0"
    obj["Aerathea.FrontFaceSetDegrees"] = 180
    obj["Aerathea.BackFaceSetDegrees"] = 180
    obj["Aerathea.StaticUVMap"] = "UVMap"
    obj["Aerathea.UVHorizontalRange"] = "0..1 per front/back 180-degree island"
    obj["Aerathea.TextureWidenFactor"] = HAFT_TEXTURE_WIDTH_FACTOR
    obj["Aerathea.ProceduralCoordinates"] = False
    obj["Aerathea.FutureFBXApplyScalings"] = "FBX All"
    obj["Aerathea.FutureFBXAddLeafBones"] = False
    obj["Aerathea.MirrorApplied"] = True

    return obj, {
        "geometry": "true profiled circular cylinder",
        "z_interval_cm": [HAFT_Z_MIN_CM, HAFT_Z_MAX_CM],
        "profile_authority": "front positive-half pixel radius at each source-registered Z row",
        "ring_count": ring_count,
        "full_angular_segments": HAFT_HALF_ANGULAR_SEGMENTS * 2,
        "radius_min_cm": round(min(radii), 6),
        "radius_max_cm": round(max(radii), 6),
        "complete_vertices": len(obj.data.vertices),
        "complete_polygons": len(obj.data.polygons),
        "materials": [material.name for material in materials],
        "material_slots": len(obj.material_slots),
        "uv_layer_names": [layer.name for layer in obj.data.uv_layers],
        "static_uv_ranges_u_v": uv_ranges,
        "front_half_degrees": 180,
        "back_half_degrees": 180,
        "procedural_coordinate_nodes": 0,
        "mirror_applied": True,
    }


def build_left_owner_composite(
    images: dict[str, Image.Image],
    masks: dict[str, Image.Image],
    axes: dict[str, float],
) -> dict[str, int]:
    """Copy exact left pixels first, then mirrored right pixels into undefined cells."""
    result = images["left"].copy()
    result_pixels = result.load()
    left_mask = masks["left"]
    right_mask = masks["right"]
    left_rect = RECTS["left"]
    right_rect = RECTS["right"]
    left_scale = scale_for("left")
    right_scale = scale_for("right")
    left_pixels = images["left"].load()
    right_pixels = images["right"].load()
    copied_left = 0
    copied_right_fallback = 0
    for global_y in range(result.height):
        world_z = TARGET_HEIGHT - (global_y + 0.5 - left_rect[1]) * left_scale
        if not (0.0 <= world_z <= TARGET_HEIGHT):
            continue
        right_source_y = right_rect[1] + (TARGET_HEIGHT - world_z) / right_scale
        right_local_y = int(math.floor(right_source_y - right_rect[1]))
        for global_x in range(result.width):
            local_x = global_x - left_rect[0]
            local_y = global_y - left_rect[1]
            if 0 <= local_x < left_mask.width and 0 <= local_y < left_mask.height and left_mask.getpixel((local_x, local_y)) > 0:
                result_pixels[global_x, global_y] = left_pixels[global_x, global_y]
                copied_left += 1
                continue
            world_y = (global_x + 0.5 - axes["left"]) * left_scale
            right_source_x = axes["right"] + world_y / right_scale
            right_local_x = int(math.floor(right_source_x - right_rect[0]))
            if not (0 <= right_local_x < right_mask.width and 0 <= right_local_y < right_mask.height):
                continue
            if right_mask.getpixel((right_local_x, right_local_y)) == 0:
                continue
            source_global_x = right_rect[0] + right_local_x
            source_global_y = right_rect[1] + right_local_y
            result_pixels[global_x, global_y] = right_pixels[source_global_x, source_global_y]
            copied_right_fallback += 1
    result.save(LEFT_COMPOSITE_PATH)
    return {"left_owner_pixels": copied_left, "mirrored_right_fallback_pixels": copied_right_fallback}


def build_back_owner_composite(
    images: dict[str, Image.Image],
    masks: dict[str, Image.Image],
    axes: dict[str, float],
) -> dict[str, int]:
    """Preserve exact back pixels and fill only undefined mapped cells from front."""
    result = images["back"].copy()
    result_pixels = result.load()
    back_mask = masks["back"]
    front_mask = masks["front"]
    back_rect = RECTS["back"]
    front_rect = RECTS["front"]
    back_scale = scale_for("back")
    front_scale = scale_for("front")
    back_pixels = images["back"].load()
    front_pixels = images["front"].load()
    copied_back = 0
    copied_front_fallback = 0
    for global_y in range(result.height):
        world_z = TARGET_HEIGHT - (global_y + 0.5 - back_rect[1]) * back_scale
        if not (0.0 <= world_z <= TARGET_HEIGHT):
            continue
        front_source_y = front_rect[1] + (TARGET_HEIGHT - world_z) / front_scale
        front_local_y = int(math.floor(front_source_y - front_rect[1]))
        for global_x in range(result.width):
            local_x = global_x - back_rect[0]
            local_y = global_y - back_rect[1]
            if 0 <= local_x < back_mask.width and 0 <= local_y < back_mask.height and back_mask.getpixel((local_x, local_y)) > 0:
                result_pixels[global_x, global_y] = back_pixels[global_x, global_y]
                copied_back += 1
                continue
            world_x = (axes["back"] - (global_x + 0.5)) * back_scale
            front_source_x = axes["front"] + world_x / front_scale
            front_local_x = int(math.floor(front_source_x - front_rect[0]))
            if not (0 <= front_local_x < front_mask.width and 0 <= front_local_y < front_mask.height):
                continue
            if front_mask.getpixel((front_local_x, front_local_y)) == 0:
                continue
            source_global_x = front_rect[0] + front_local_x
            source_global_y = front_rect[1] + front_local_y
            result_pixels[global_x, global_y] = front_pixels[source_global_x, source_global_y]
            copied_front_fallback += 1
    result.save(BACK_COMPOSITE_PATH)
    return {"back_owner_pixels": copied_back, "reversed_front_fallback_pixels": copied_front_fallback}


def combined_mesh_bounds(objects: list[bpy.types.Object]) -> dict[str, list[float]]:
    coordinates = [obj.matrix_world @ vertex.co for obj in objects for vertex in obj.data.vertices]
    minimum = [min(value[index] for value in coordinates) for index in range(3)]
    maximum = [max(value[index] for value in coordinates) for index in range(3)]
    return {
        "min_cm": [round(value, 6) for value in minimum],
        "max_cm": [round(value, 6) for value in maximum],
        "dimensions_cm": [round(maximum[index] - minimum[index], 6) for index in range(3)],
    }


def render_geometry_proof_all(
    objects: list[bpy.types.Object],
    camera: bpy.types.Object,
    path: Path,
    width: int,
    height: int,
    geometry_material: bpy.types.Material,
) -> None:
    """Temporarily replace every mesh material so source color cannot survive."""
    saved: list[tuple[bpy.types.Object, list[bpy.types.Material | None], list[int]]] = []
    for obj in objects:
        original_materials = [slot.material for slot in obj.material_slots]
        original_indices = [polygon.material_index for polygon in obj.data.polygons]
        saved.append((obj, original_materials, original_indices))
        obj.data.materials.clear()
        obj.data.materials.append(geometry_material)
        for polygon in obj.data.polygons:
            polygon.material_index = 0
    a09.render(camera, path, width, height)
    for obj, original_materials, original_indices in saved:
        obj.data.materials.clear()
        for material in original_materials:
            if material is not None:
                obj.data.materials.append(material)
        for polygon, material_index in zip(obj.data.polygons, original_indices):
            polygon.material_index = material_index


def add_camera(name: str, location: tuple[float, float, float], target: tuple[float, float, float], ortho: float) -> bpy.types.Object:
    data = bpy.data.cameras.new(name)
    data.type = "ORTHO"
    data.ortho_scale = ortho
    camera = bpy.data.objects.new(name, data)
    bpy.context.scene.collection.objects.link(camera)
    camera.location = location
    camera.rotation_euler = (Vector(target) - camera.location).to_track_quat("-Z", "Y").to_euler()
    return camera


def font(size: int) -> ImageFont.ImageFont:
    for candidate in (
        "/usr/share/fonts/truetype/dejavu/DejaVuSans.ttf",
        "/usr/share/fonts/dejavu-sans-fonts/DejaVuSans.ttf",
        "/usr/share/fonts/DejaVuSans.ttf",
    ):
        if Path(candidate).exists():
            return ImageFont.truetype(candidate, size)
    return ImageFont.load_default()


def fit_panel(image: Image.Image, size: tuple[int, int], background: tuple[int, int, int] = (246, 244, 239)) -> Image.Image:
    value = image.convert("RGB")
    resampling = getattr(Image, "Resampling", Image)
    value.thumbnail(size, resampling.LANCZOS)
    panel = Image.new("RGB", size, background)
    panel.paste(value, ((size[0] - value.width) // 2, (size[1] - value.height) // 2))
    return panel


def compose_review(images: dict[str, Image.Image], axes: dict[str, float], bounds: dict[str, list[float]]) -> None:
    canvas = Image.new("RGB", (3600, 3000), (234, 231, 223))
    draw = ImageDraw.Draw(canvas)
    title, body, small = font(50), font(25), font(21)
    draw.text((65, 35), "Siege Breaker R5 - Registered Half + True Cylindrical Haft", fill=(28, 26, 23), font=title)
    draw.text((67, 98), "Fresh X>=0 assembly; exact X=0 mirror; true circular haft with separate static-UV front/back 180-degree owners.", fill=(66, 60, 52), font=body)
    panel_size = (800, 690)
    for column, view in enumerate(("front", "back", "left", "right")):
        x = 55 + column * 885
        source_crop = images[view].crop(RECTS[view])
        candidate = Image.open(RENDER_PATHS[view]).convert("RGB")
        draw.text((x, 155), f"{view.upper()} SOURCE", fill=(42, 39, 35), font=body)
        canvas.paste(fit_panel(source_crop, panel_size), (x, 195))
        draw.rectangle((x, 195, x + panel_size[0], 195 + panel_size[1]), outline=(90, 83, 73), width=3)
        draw.text((x, 925), f"R5 {view.upper()} RENDER", fill=(42, 39, 35), font=body)
        canvas.paste(fit_panel(candidate, panel_size), (x, 965))
        draw.rectangle((x, 965, x + panel_size[0], 965 + panel_size[1]), outline=(90, 83, 73), width=3)

    proof_size = (980, 980)
    canvas.paste(fit_panel(Image.open(RENDER_PATHS["color_3q"]), proof_size), (340, 1775))
    canvas.paste(fit_panel(Image.open(RENDER_PATHS["geometry_3q"]), proof_size), (1370, 1775))
    draw.text((340, 1725), "COLORED COMPLETE 3/4", fill=(42, 39, 35), font=body)
    draw.text((1370, 1725), "GRAY GEOMETRY / CENTER-SEAM PROOF", fill=(42, 39, 35), font=body)
    draw.rectangle((340, 1775, 1320, 2755), outline=(90, 83, 73), width=3)
    draw.rectangle((1370, 1775, 2350, 2755), outline=(90, 83, 73), width=3)
    notes = [
        "Geometry input: original source pixels only; R4D mesh inputs: 0.",
        f"Shaft axes px: front {axes['front']:.3f}; back {axes['back']:.3f}; left {axes['left']:.3f}; right {axes['right']:.3f}.",
        f"Bounds cm: {bounds['dimensions_cm'][0]:.6f} x {bounds['dimensions_cm'][1]:.6f} x {bounds['dimensions_cm'][2]:.6f}.",
        "Haft: true profiled cylinder, X/Y radius from front pixels, static UVMap, U=0..1 per 180-degree half.",
        "Right view owns non-haft depth; left source is reversed for -X pixels only.",
        "No generated imagery, TRELLIS, FBX export, or Unreal execution.",
        "Status: DCC source candidate pending Flamestrike visual decision.",
    ]
    y = 1815
    for line in notes:
        draw.text((2440, y), line, fill=(52, 48, 42), font=small)
        y += 78
    canvas.save(RENDER_PATHS["review"])


def main() -> None:
    ensure_dirs()
    observed_hashes = {name: sha256(path) for name, path in SOURCES.items()}
    if observed_hashes != EXPECTED_HASHES:
        raise RuntimeError(f"R5 source hash mismatch: {observed_hashes}")

    images = {name: Image.open(path).convert("RGB") for name, path in SOURCES.items()}
    masks: dict[str, Image.Image] = {}
    counts: dict[str, int] = {}
    for view in SOURCES:
        masks[view], counts[view] = a09.exact_component_mask(images[view], RECTS[view])
    if counts != EXPECTED_COUNTS:
        raise RuntimeError(f"R5 source membership mismatch: {counts}")

    axes: dict[str, float] = {}
    axis_samples: dict[str, list[dict[str, float | int | list[int]]]] = {}
    for view in SOURCES:
        axes[view], axis_samples[view] = derive_axis(masks[view], view)
    left_composite_stats = build_left_owner_composite(images, masks, axes)
    back_composite_stats = build_back_owner_composite(images, masks, axes)
    haft_texture_stats = {
        "front": build_haft_texture("front", images["front"], masks["front"], FRONT_HAFT_TEXTURE_PATH),
        "back": build_haft_texture("back", images["back"], masks["back"], BACK_HAFT_TEXTURE_PATH),
    }

    a09.clear_scene()
    a09.configure_scene()
    collection = bpy.context.scene.collection.children.get("A09_SOURCE_HALF_AND_MIRROR")
    if collection is not None:
        collection.name = "A12_R5_REGISTERED_ONE_HALF_AND_MIRROR"

    materials = [
        image_material("MI_DRW_SiegeBreaker_R5_FrontOwnerPixels", SOURCES["front"]),
        image_material("MI_DRW_SiegeBreaker_R5_BackOwnerOverReversedFrontPixels", BACK_COMPOSITE_PATH),
        image_material("MI_DRW_SiegeBreaker_R5_RightOwnerPixels", SOURCES["right"]),
        image_material("MI_DRW_SiegeBreaker_R5_LeftOwnerOverMirroredRightPixels", LEFT_COMPOSITE_PATH),
    ]
    haft_materials = [
        image_material("Front_Material", FRONT_HAFT_TEXTURE_PATH),
        image_material("Back_Material", BACK_HAFT_TEXTURE_PATH),
    ]
    geometry_material = a09.flat_material("M_DRW_SiegeBreaker_R5_GeometryProof", (0.24, 0.28, 0.34, 1.0))
    model, build_stats = build_registered_half(images, masks, axes, materials)
    haft, haft_build_stats = build_cylindrical_haft(masks, axes, haft_materials)
    models = [model, haft]
    a09.add_lighting()

    front_camera = add_camera("CAM_R5_FRONT", (0.0, -520.0, 85.0), (0.0, 0.0, 85.0), 190.0)
    back_camera = add_camera("CAM_R5_BACK", (0.0, 520.0, 85.0), (0.0, 0.0, 85.0), 190.0)
    left_camera = add_camera("CAM_R5_LEFT", (-520.0, 0.0, 85.0), (0.0, 0.0, 85.0), 190.0)
    right_camera = add_camera("CAM_R5_RIGHT", (520.0, 0.0, 85.0), (0.0, 0.0, 85.0), 190.0)
    three_quarter = add_camera("CAM_R5_COLOR_3Q", (145.0, -235.0, 112.0), (0.0, 0.0, 84.0), 205.0)

    for view, camera in (("front", front_camera), ("back", back_camera), ("left", left_camera), ("right", right_camera)):
        a09.render(camera, RENDER_PATHS[view], 1000, 1200)
    a09.render(three_quarter, RENDER_PATHS["color_3q"], 1400, 1600)
    render_geometry_proof_all(models, three_quarter, RENDER_PATHS["geometry_3q"], 1400, 1600, geometry_material)

    bpy.ops.wm.save_as_mainfile(filepath=str(BLEND_PATH))
    bounds = combined_mesh_bounds(models)
    compose_review(images, axes, bounds)
    manifest = {
        "schema": "aerathea.siegebreaker.a12_r5_cylindrical_haft_validation.v2",
        "asset": ASSET,
        "contract_id": CONTRACT_ID,
        "attempt": ATTEMPT,
        "artifact_status": "DCC source candidate pending Flamestrike visual decision",
        "source_hashes": observed_hashes,
        "source_rectangles_half_open": {key: list(value) for key, value in RECTS.items()},
        "source_membership_counts": counts,
        "source_scale_cm_per_pixel": {view: scale_for(view) for view in SOURCES},
        "registered_shaft_axes_global_px": axes,
        "shaft_axis_samples": axis_samples,
        "left_surface_pixel_composite": left_composite_stats,
        "back_surface_pixel_composite": back_composite_stats,
        "haft_texture_derivation": haft_texture_stats,
        "construction": {
            "source_half": "X>=0",
            "front_owner": "front positive half",
            "back_owner": "corresponding reversed back image-left half",
            "depth_owner": "registered right view",
            "left_owner": "reversed -X surface pixels; no independent geometry",
            "mirror_plane": "X=0",
            "mirror_applied": True,
            "prior_candidate_geometry_inputs": 0,
            "a11_depth_used": False,
            "source_connected_empty_space_preserved": True,
            "haft": "true circular profiled cylinder built as X>=0 half and mirrored at X=0",
            "haft_radius_authority": "front positive-half pixels; identical X/Y radius by cylinder definition",
            "haft_right_view_role": "shaft-axis registration and comparison; no elliptical scaling",
            "haft_static_uv": True,
            "haft_front_back_material_degrees": [180, 180],
            "haft_uv_u_range_per_half": [0.0, 1.0],
            "haft_texture_widen_factor": HAFT_TEXTURE_WIDTH_FACTOR,
        },
        "build": build_stats,
        "haft_build": haft_build_stats,
        "mesh": {
            "bounds": bounds,
            "objects": {
                model.name: {"scale": list(model.scale), "location": list(model.location)},
                haft.name: {"scale": list(haft.scale), "location": list(haft.location)},
            },
        },
        "software": {"blender": bpy.app.version_string, "image_generation": False, "trellis": False, "image_to_3d": False},
        "deferred_export_record": {
            "executed": False,
            "fbx_apply_scalings": "FBX All",
            "fbx_add_leaf_bones": False,
            "unreal_static_uv_required": True,
        },
        "unreal_authority": False,
        "fully_game_ready": False,
        "outputs": {key: str(path.relative_to(ROOT)) for key, path in RENDER_PATHS.items()} | {"blend_local_only": str(BLEND_PATH.relative_to(ROOT))},
    }
    MANIFEST_PATH.write_text(json.dumps(manifest, indent=2) + "\n", encoding="utf-8")
    output_hashes = {key: sha256(path) for key, path in RENDER_PATHS.items()}
    output_hashes["blend_local_only"] = sha256(BLEND_PATH)
    output_hashes["left_owner_composite_local_only"] = sha256(LEFT_COMPOSITE_PATH)
    output_hashes["back_owner_composite_local_only"] = sha256(BACK_COMPOSITE_PATH)
    output_hashes["front_haft_texture_local_only"] = sha256(FRONT_HAFT_TEXTURE_PATH)
    output_hashes["back_haft_texture_local_only"] = sha256(BACK_HAFT_TEXTURE_PATH)
    manifest["output_hashes"] = output_hashes
    MANIFEST_PATH.write_text(json.dumps(manifest, indent=2) + "\n", encoding="utf-8")
    print(json.dumps(manifest, indent=2))


if __name__ == "__main__":
    main()
