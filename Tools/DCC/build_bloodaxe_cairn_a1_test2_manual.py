#!/usr/bin/env python3
"""Build Blood Axe cairn A01 Test 2 as a front-faithful 360 static prop.

Run with:
    blender --background --python Tools/DCC/build_bloodaxe_cairn_a1_image_relief_asset.py

This follows the user-approved single-image workflow for A01: isolate the
approved painting, trace the visible forms into mesh layers, project the image
onto the traced faces, deepen the layers into walk-around stone volumes, add
inferred side/back support geometry, then export with LODs, collision, and
review renders.
"""

from __future__ import annotations

import math
import sys
from dataclasses import dataclass
from pathlib import Path

import bpy
from mathutils import Vector
from mathutils.geometry import tessellate_polygon
from PIL import Image, ImageDraw, ImageEnhance, ImageFilter, ImageFont


ROOT = Path(__file__).resolve().parents[2]
SOURCE_ROOT = ROOT / "SourceAssets"
BLENDER_ROOT = SOURCE_ROOT / "Blender"
EXPORT_ROOT = SOURCE_ROOT / "Exports"
TEXTURE_ROOT = SOURCE_ROOT / "Textures"

ASSET_NAME = "SM_GIA_BloodAxeCairnSlabCluster_A01_Test2Manual"
REL_PATH = f"Props/Giants/BloodAxe/Cairns/{ASSET_NAME}"
UNREAL_PATH = f"/Game/Aerathea/Props/Giants/BloodAxe/Cairns/{ASSET_NAME}"
REVIEW_ROOT = ROOT / "Saved/Automation/DCC" / ASSET_NAME

SOURCE_IMAGE = ROOT / "docs/assets/visual_canon/VC_GIA_BloodAxe_CairnStones_A01_A1_Crop.png"
TEXTURE_DIR = TEXTURE_ROOT / REL_PATH
TEXTURE_BC = TEXTURE_DIR / "T_GIA_BloodAxeCairnSlabCluster_A01_Test2Manual_BC.png"
TEXTURE_N = TEXTURE_DIR / "T_GIA_BloodAxeCairnSlabCluster_A01_Test2Manual_N.png"
TEXTURE_ORM = TEXTURE_DIR / "T_GIA_BloodAxeCairnSlabCluster_A01_Test2Manual_ORM.png"
PAINT_PASS = "A01-Test2-Paint-01"

IMAGE_WIDTH = 360
IMAGE_HEIGHT = 430
GROUND_BASELINE_PX = 368.0
PIXEL_SCALE_CM = 1.0
PROJECTION_BRIGHTNESS = 1.06
PROJECTION_CONTRAST = 1.04
PROJECTION_SATURATION = 0.98

sys.path.insert(0, str(ROOT))

from Tools.DCC.build_next_slice_assets import add_asset_metadata, clear_scene, setup_scene  # noqa: E402


@dataclass(frozen=True)
class ReliefLayer:
    name: str
    points_px: tuple[tuple[float, float], ...]
    y_front: float
    thickness: float
    lod_max: int
    lod_min: int = 0
    material: str = "image"


SILHOUETTE = (
    (20, 335), (31, 309), (52, 293), (66, 263), (88, 240),
    (122, 224), (150, 207), (161, 176), (176, 158), (192, 161),
    (213, 188), (234, 216), (264, 205), (292, 220), (306, 252),
    (334, 276), (346, 311), (338, 338), (306, 354), (252, 366),
    (183, 368), (107, 357), (47, 346),
)

LAYERS = [
    ReliefLayer(
        "A1_ImageRelief_FullBackstop",
        SILHOUETTE,
        48.0,
        42.0,
        3,
        lod_min=3,
    ),
    ReliefLayer(
        "A1_ImageRelief_GroundRubbleApron",
        (
            (21, 333), (37, 305), (67, 288), (112, 289), (156, 307),
            (205, 300), (258, 291), (314, 301), (344, 321), (333, 344),
            (285, 360), (206, 367), (122, 355), (58, 344),
        ),
        -46.0,
        28.0,
        2,
    ),
    ReliefLayer(
        "A1_ImageRelief_MainPaintedSlab",
        (
            (66, 255), (104, 226), (149, 207), (201, 219), (260, 245),
            (258, 282), (206, 306), (145, 299), (86, 282),
        ),
        -26.0,
        44.0,
        2,
    ),
    ReliefLayer(
        "A1_ImageRelief_RearTallSlab",
        (
            (154, 226), (160, 198), (166, 174), (176, 158), (191, 161),
            (207, 185), (216, 219), (205, 248), (182, 265), (164, 251),
        ),
        32.0,
        48.0,
        2,
    ),
    ReliefLayer(
        "A1_ImageRelief_LeftStoneStackBack",
        (
            (56, 258), (95, 229), (139, 239), (156, 268), (120, 297),
            (68, 290),
        ),
        -12.0,
        36.0,
        1,
    ),
    ReliefLayer(
        "A1_ImageRelief_LeftStoneStackFront",
        (
            (51, 289), (101, 274), (154, 292), (139, 317), (73, 314),
        ),
        -52.0,
        34.0,
        1,
    ),
    ReliefLayer(
        "A1_ImageRelief_RightUpright",
        (
            (240, 260), (250, 228), (266, 211), (282, 207), (295, 219),
            (299, 247), (292, 277), (270, 287), (250, 276),
        ),
        -6.0,
        38.0,
        1,
    ),
    ReliefLayer(
        "A1_ImageRelief_FrontPebbleRubble",
        (
            (36, 310), (73, 294), (121, 296), (179, 319), (257, 295),
            (329, 307), (331, 333), (283, 350), (205, 357), (122, 350),
            (58, 337),
        ),
        -76.0,
        18.0,
        0,
    ),
]


def font(size: int) -> ImageFont.ImageFont:
    candidates = [
        "/usr/share/fonts/dejavu-sans-fonts/DejaVuSans.ttf",
        "/usr/share/fonts/dejavu/DejaVuSans.ttf",
    ]
    for path in candidates:
        if Path(path).exists():
            return ImageFont.truetype(path, size)
    return ImageFont.load_default()


def clamp_byte(value: float) -> int:
    return max(0, min(255, int(round(value))))


def clamp01(value: float) -> float:
    return max(0.0, min(1.0, value))


def mix_color(a: tuple[int, int, int], b: tuple[int, int, int], amount: float) -> tuple[int, int, int]:
    amount = clamp01(amount)
    return tuple(clamp_byte(a[index] * (1.0 - amount) + b[index] * amount) for index in range(3))


def multiply_color(color: tuple[int, int, int], amount: float) -> tuple[int, int, int]:
    return tuple(clamp_byte(channel * amount) for channel in color)


def painted_pixel_color(red: int, green: int, blue: int, x: int, y: int, edge: int) -> tuple[int, int, int]:
    luma = (0.299 * red) + (0.587 * green) + (0.114 * blue)
    value = clamp01((luma - 24.0) / 176.0)
    edge_strength = clamp01(edge / 170.0)

    red_mark = red > green * 1.25 and red > blue * 1.18 and red - green > 28 and red > 70
    rawhide = red > green * 1.04 and green > blue * 1.15 and 54 < luma < 142 and not red_mark
    earth = y > 270 and red > blue * 1.08 and luma < 118 and not red_mark

    if red_mark:
        color = mix_color((62, 20, 15), (154, 48, 34), value)
        color = mix_color(color, (94, 26, 19), edge_strength * 0.20)
        color = mix_color(color, (red, green, blue), 0.18)
    elif rawhide:
        color = mix_color((72, 43, 19), (164, 102, 39), value)
        color = mix_color(color, (red, green, blue), 0.18)
    elif earth:
        color = mix_color((42, 32, 25), (96, 69, 45), value)
        color = mix_color(color, (red, green, blue), 0.12)
    else:
        color = mix_color((50, 47, 40), (146, 136, 112), value)
        color = mix_color(color, (103, 86, 66), clamp01((red - blue) / 150.0) * 0.10)
        color = mix_color(color, (red, green, blue), 0.16)

    lower_shadow = clamp01((y - 245.0) / 145.0)
    shade = 1.0 - (edge_strength * 0.14) - (lower_shadow * 0.04)
    return multiply_color(color, shade)


def make_normal_from_height(height: Image.Image) -> Image.Image:
    pixels = height.load()
    normal = Image.new("RGBA", height.size, (128, 128, 255, 255))
    normal_pixels = normal.load()
    width, height_px = height.size
    strength = 7.0
    for y in range(height_px):
        y0 = max(0, y - 1)
        y1 = min(height_px - 1, y + 1)
        for x in range(width):
            x0 = max(0, x - 1)
            x1 = min(width - 1, x + 1)
            dx = (pixels[x0, y] - pixels[x1, y]) / 255.0 * strength
            dy = (pixels[x, y0] - pixels[x, y1]) / 255.0 * strength
            dz = 1.0
            length = math.sqrt((dx * dx) + (dy * dy) + (dz * dz))
            normal_pixels[x, y] = (
                clamp_byte((dx / length) * 127.5 + 127.5),
                clamp_byte((dy / length) * 127.5 + 127.5),
                clamp_byte((dz / length) * 127.5 + 127.5),
                255,
            )
    return normal


def make_texture_sources() -> None:
    TEXTURE_DIR.mkdir(parents=True, exist_ok=True)
    source = Image.open(SOURCE_IMAGE).convert("RGBA")
    alpha = Image.new("L", source.size, 0)
    mask_draw = ImageDraw.Draw(alpha)
    mask_draw.polygon(SILHOUETTE, fill=255)
    grayscale = source.convert("L")
    edge_map = grayscale.filter(ImageFilter.FIND_EDGES).filter(ImageFilter.GaussianBlur(radius=0.4))
    source_pixels = source.load()
    alpha_pixels = alpha.load()
    edge_pixels = edge_map.load()
    for y in range(source.height):
        for x in range(source.width):
            if alpha_pixels[x, y] == 0:
                continue
            red, green, blue, _ = source_pixels[x, y]
            luma = (red + green + blue) / 3.0
            chroma = max(red, green, blue) - min(red, green, blue)
            backdrop_pixel = chroma < 18 and 92 < luma < 184 and edge_pixels[x, y] < 16
            if backdrop_pixel:
                alpha_pixels[x, y] = 0
    for _ in range(2):
        alpha = alpha.filter(ImageFilter.GaussianBlur(radius=0.35))
    painted = Image.new("RGBA", source.size, (0, 0, 0, 0))
    painted_pixels = painted.load()
    for y in range(source.height):
        for x in range(source.width):
            opacity = alpha_pixels[x, y]
            if opacity == 0:
                continue
            red, green, blue, _ = source_pixels[x, y]
            paint_red, paint_green, paint_blue = painted_pixel_color(red, green, blue, x, y, edge_pixels[x, y])
            painted_pixels[x, y] = (paint_red, paint_green, paint_blue, opacity)

    adjusted = ImageEnhance.Brightness(painted.convert("RGB")).enhance(PROJECTION_BRIGHTNESS)
    adjusted = ImageEnhance.Contrast(adjusted).enhance(PROJECTION_CONTRAST)
    adjusted = ImageEnhance.Color(adjusted).enhance(PROJECTION_SATURATION)
    source = adjusted.convert("RGBA")
    source.putalpha(alpha)
    source = source.resize((IMAGE_WIDTH * 4, IMAGE_HEIGHT * 4), Image.Resampling.LANCZOS)
    alpha = alpha.resize(source.size, Image.Resampling.LANCZOS)
    source.putalpha(alpha)
    source.save(TEXTURE_BC)

    height = source.convert("L").filter(ImageFilter.GaussianBlur(radius=0.35))
    normal = make_normal_from_height(height)
    normal.putalpha(alpha)
    normal.save(TEXTURE_N)

    edge_large = edge_map.resize(source.size, Image.Resampling.LANCZOS)
    edge_large_pixels = edge_large.load()
    alpha_large_pixels = alpha.load()
    orm = Image.new("RGBA", source.size, (255, 225, 0, 255))
    orm_pixels = orm.load()
    for y in range(source.height):
        for x in range(source.width):
            opacity = alpha_large_pixels[x, y]
            edge_strength = clamp01(edge_large_pixels[x, y] / 185.0)
            ground_shadow = clamp01((y - source.height * 0.62) / (source.height * 0.30))
            ao = clamp_byte(255 - edge_strength * 72 - ground_shadow * 26)
            orm_pixels[x, y] = (ao, 226, 0, opacity)
    orm.save(TEXTURE_ORM)


def make_collection(name: str, hidden: bool = False) -> bpy.types.Collection:
    collection = bpy.data.collections.new(name)
    bpy.context.scene.collection.children.link(collection)
    collection.hide_viewport = hidden
    collection.hide_render = hidden
    return collection


def set_active(obj: bpy.types.Object) -> None:
    bpy.ops.object.select_all(action="DESELECT")
    bpy.context.view_layer.objects.active = obj
    obj.select_set(True)


def link_to_collection(obj: bpy.types.Object, collection: bpy.types.Collection) -> None:
    for current in list(obj.users_collection):
        current.objects.unlink(obj)
    collection.objects.link(obj)


def pixel_to_world(point_px: tuple[float, float], y: float) -> tuple[float, float, float]:
    px, py = point_px
    x = (px - IMAGE_WIDTH / 2.0) * PIXEL_SCALE_CM
    z = (GROUND_BASELINE_PX - py) * PIXEL_SCALE_CM
    return (x, y, z)


def pixel_to_uv(point_px: tuple[float, float]) -> tuple[float, float]:
    px, py = point_px
    return (px / IMAGE_WIDTH, 1.0 - py / IMAGE_HEIGHT)


def make_image_material() -> bpy.types.Material:
    material = bpy.data.materials.new("M_GIA_BloodAxeCairn_A01_Test2Manual_Projection")
    material.use_nodes = True
    material.diffuse_color = (1.0, 1.0, 1.0, 1.0)
    try:
        material.blend_method = "BLEND"
        material.use_screen_refraction = False
        material.show_transparent_back = True
    except Exception:
        pass
    nodes = material.node_tree.nodes
    bsdf = nodes.get("Principled BSDF")
    texture = nodes.new(type="ShaderNodeTexImage")
    texture.name = "A1_ImageRelief_Texture"
    texture.image = bpy.data.images.load(str(TEXTURE_BC))
    if bsdf is not None:
        material.node_tree.links.new(texture.outputs["Color"], bsdf.inputs["Base Color"])
        if "Alpha" in bsdf.inputs and "Alpha" in texture.outputs:
            material.node_tree.links.new(texture.outputs["Alpha"], bsdf.inputs["Alpha"])
        bsdf.inputs["Roughness"].default_value = 0.88
        if "Emission Color" in bsdf.inputs:
            bsdf.inputs["Emission Color"].default_value = (0.0, 0.0, 0.0, 1.0)
        if "Emission Strength" in bsdf.inputs:
            bsdf.inputs["Emission Strength"].default_value = 0.0
    return material


def make_solid_material(name: str, color: tuple[float, float, float, float]) -> bpy.types.Material:
    material = bpy.data.materials.new(name)
    material.diffuse_color = color
    material.use_nodes = True
    bsdf = material.node_tree.nodes.get("Principled BSDF")
    if bsdf is not None:
        bsdf.inputs["Base Color"].default_value = color
        bsdf.inputs["Roughness"].default_value = 0.94
        if "Emission Color" in bsdf.inputs:
            bsdf.inputs["Emission Color"].default_value = (color[0] * 0.45, color[1] * 0.45, color[2] * 0.45, 1.0)
        if "Emission Strength" in bsdf.inputs:
            bsdf.inputs["Emission Strength"].default_value = 0.12
    return material


def make_materials() -> dict[str, bpy.types.Material]:
    return {
        "image": make_image_material(),
        "side": make_solid_material("M_GIA_BloodAxeCairn_A01_Test2Manual_SideStone", (0.29, 0.27, 0.23, 1.0)),
        "collision": make_solid_material("M_AET_CollisionProxy_ReviewOnly_A01", (0.1, 0.42, 0.95, 0.25)),
    }


def build_extruded_layer(
    layer: ReliefLayer,
    materials: dict[str, bpy.types.Material],
    collection: bpy.types.Collection,
    lod_level: int,
) -> bpy.types.Object:
    simplify_step = max(1, lod_level + 1)
    points = list(layer.points_px)
    if lod_level > 0 and len(points) > 6:
        points = [point for index, point in enumerate(points) if index % simplify_step != simplify_step - 1]
        if len(points) < 5:
            points = list(layer.points_px)

    front_verts = [pixel_to_world(point, layer.y_front) for point in points]
    back_y = layer.y_front + layer.thickness
    back_verts = [pixel_to_world(point, back_y) for point in points]
    verts = front_verts + back_verts
    uvs = [pixel_to_uv(point) for point in points] * 2
    polygon_for_tess = [[Vector((vert[0], vert[2], 0.0)) for vert in front_verts]]
    triangles = tessellate_polygon(polygon_for_tess)

    faces: list[tuple[int, ...]] = []
    material_indices: list[int] = []
    for tri in triangles:
        faces.append(tuple(tri))
        material_indices.append(0)
    count = len(points)
    for tri in triangles:
        faces.append(tuple(count + index for index in reversed(tri)))
        material_indices.append(0)
    for index in range(count):
        next_index = (index + 1) % count
        faces.append((index, next_index, count + next_index, count + index))
        material_indices.append(1)

    mesh = bpy.data.meshes.new(f"{layer.name}_LOD{lod_level}_Mesh")
    mesh.from_pydata(verts, [], faces)
    mesh.update()
    obj = bpy.data.objects.new(f"{layer.name}_LOD{lod_level}", mesh)
    obj.data.materials.append(materials["image"])
    obj.data.materials.append(materials["side"])
    for polygon, material_index in zip(obj.data.polygons, material_indices):
        polygon.material_index = material_index

    uv_layer = obj.data.uv_layers.new(name="A1_ProjectedUV")
    for polygon in obj.data.polygons:
        for loop_index in polygon.loop_indices:
            vertex_index = obj.data.loops[loop_index].vertex_index
            uv_layer.data[loop_index].uv = uvs[vertex_index]

    collection.objects.link(obj)
    return obj


def build_lod_collection(
    lod_level: int,
    materials: dict[str, bpy.types.Material],
    collection: bpy.types.Collection,
) -> list[bpy.types.Object]:
    objects = []
    for layer in LAYERS:
        if layer.lod_min <= lod_level <= layer.lod_max:
            objects.append(build_extruded_layer(layer, materials, collection, lod_level))
    return objects


def roughen_mesh(obj: bpy.types.Object, amount: float, seed: int) -> None:
    for index, vertex in enumerate(obj.data.vertices):
        n1 = math.sin((index + 1) * 17.19 + seed * 0.11) * 0.5
        n2 = math.sin((index + 3) * 11.73 + seed * 0.23) * 0.5
        n3 = math.sin((index + 7) * 19.41 + seed * 0.31) * 0.5
        vertex.co.x += n1 * amount
        vertex.co.y += n2 * amount
        vertex.co.z += n3 * amount * 0.55


def add_support_box(
    name: str,
    collection: bpy.types.Collection,
    material: bpy.types.Material,
    location: tuple[float, float, float],
    dimensions: tuple[float, float, float],
    rotation: tuple[float, float, float],
    seed: int,
) -> bpy.types.Object:
    bpy.ops.mesh.primitive_cube_add(size=1.0, location=location, rotation=rotation)
    obj = bpy.context.object
    obj.name = name
    obj.dimensions = dimensions
    obj.data.materials.append(material)
    set_active(obj)
    bpy.ops.object.transform_apply(location=False, rotation=False, scale=True)
    bevel = obj.modifiers.new(f"{name}_ChippedReadableEdges", "BEVEL")
    bevel.width = max(0.8, min(dimensions) * 0.055)
    bevel.segments = 1
    bevel.affect = "EDGES"
    bpy.ops.object.modifier_apply(modifier=bevel.name)
    roughen_mesh(obj, max(0.6, min(dimensions) * 0.07), seed)
    try:
        bpy.ops.object.shade_flat()
    except Exception:
        pass
    link_to_collection(obj, collection)
    return obj


def add_inferred_360_supports(
    collection: bpy.types.Collection,
    material: bpy.types.Material,
    lod_level: int,
) -> list[bpy.types.Object]:
    if lod_level > 1:
        return []
    specs = [
        ("BackTallStoneMass", (12.0, 86.0, 94.0), (70.0, 50.0, 146.0), (0.03, -0.18, -0.10), 501),
        ("BackRightShoulderStone", (104.0, 62.0, 72.0), (58.0, 46.0, 106.0), (0.04, 0.20, 0.18), 502),
        ("BackLeftShoulderStone", (-76.0, 64.0, 62.0), (52.0, 42.0, 96.0), (-0.06, -0.15, -0.20), 503),
        ("RearLowFoundationA", (-108.0, 34.0, 28.0), (68.0, 44.0, 28.0), (0.10, 0.04, -0.11), 504),
        ("RearLowFoundationB", (56.0, 43.0, 24.0), (86.0, 42.0, 26.0), (-0.08, -0.02, 0.14), 505),
        ("RightRearLooseStone", (148.0, 52.0, 32.0), (34.0, 30.0, 28.0), (0.12, 0.08, 0.34), 506),
    ]
    return [
        add_support_box(f"Test2_Inferred360_{name}_LOD{lod_level}", collection, material, location, dimensions, rotation, seed)
        for name, location, dimensions, rotation, seed in specs
    ]


def add_collision_proxy(material: bpy.types.Material, collection: bpy.types.Collection) -> bpy.types.Object:
    bpy.ops.mesh.primitive_cube_add(size=1.0, location=(0.0, 0.0, 105.0))
    obj = bpy.context.object
    obj.name = f"UCX_{ASSET_NAME}_00"
    obj.dimensions = (338.0, 220.0, 220.0)
    obj.data.materials.append(material)
    set_active(obj)
    bpy.ops.object.transform_apply(location=False, rotation=False, scale=True)
    obj.display_type = "WIRE"
    obj.hide_render = True
    link_to_collection(obj, collection)
    return obj


def object_triangle_count(obj: bpy.types.Object) -> int:
    if obj.type != "MESH":
        return 0
    obj.data.calc_loop_triangles()
    return len(obj.data.loop_triangles)


def collection_triangle_count(collection: bpy.types.Collection) -> int:
    return sum(object_triangle_count(obj) for obj in collection.objects)


def collection_bounds(collection: bpy.types.Collection) -> tuple[float, float, float]:
    points = []
    for obj in collection.objects:
        if obj.type != "MESH":
            continue
        points.extend(obj.matrix_world @ Vector(corner) for corner in obj.bound_box)
    return (
        max(point.x for point in points) - min(point.x for point in points),
        max(point.y for point in points) - min(point.y for point in points),
        max(point.z for point in points) - min(point.z for point in points),
    )


def export_selected_fbx(path: Path, objects: list[bpy.types.Object]) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
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


def add_review_lighting() -> None:
    scene = bpy.context.scene
    try:
        scene.render.engine = "BLENDER_EEVEE_NEXT"
    except TypeError:
        scene.render.engine = "BLENDER_EEVEE"
    try:
        scene.view_settings.view_transform = "Standard"
    except TypeError:
        pass
    scene.view_settings.exposure = 0.0
    scene.view_settings.gamma = 1.0
    if scene.world is not None:
        scene.world.color = (0.50, 0.48, 0.44)
    for name, kind, location, energy, size in [
        ("AET_ImageRelief_Key", "AREA", (-260.0, -420.0, 580.0), 7200.0, 520.0),
        ("AET_ImageRelief_Fill", "AREA", (260.0, -260.0, 300.0), 2400.0, 620.0),
    ]:
        light_data = bpy.data.lights.new(name, type=kind)
        light_data.energy = energy
        if kind == "AREA":
            light_data.size = size
        light = bpy.data.objects.new(name, light_data)
        light.location = location
        bpy.context.scene.collection.objects.link(light)


def set_camera(name: str, location: tuple[float, float, float], target: tuple[float, float, float], ortho_scale: float) -> None:
    bpy.ops.object.camera_add(location=location)
    camera = bpy.context.object
    camera.name = name
    direction = Vector(target) - Vector(location)
    camera.rotation_euler = direction.to_track_quat("-Z", "Y").to_euler()
    camera.data.type = "ORTHO"
    camera.data.ortho_scale = ortho_scale
    camera.data.clip_start = 1
    camera.data.clip_end = 5000
    bpy.context.scene.camera = camera


def render_reviews() -> None:
    REVIEW_ROOT.mkdir(parents=True, exist_ok=True)
    scene = bpy.context.scene
    scene.render.resolution_x = 1200
    scene.render.resolution_y = 1433
    scene.render.film_transparent = False

    set_camera("AET_ImageRelief_FrontMatchCamera", (0.0, -900.0, 105.0), (0.0, 0.0, 105.0), 430.0)
    scene.render.filepath = str(REVIEW_ROOT / f"{ASSET_NAME}_FrontMatchReview.png")
    bpy.ops.render.render(write_still=True)

    scene.render.resolution_x = 1500
    scene.render.resolution_y = 1000
    set_camera("AET_ImageRelief_AngledParallaxCamera", (235.0, -800.0, 150.0), (0.0, -8.0, 105.0), 425.0)
    scene.render.filepath = str(REVIEW_ROOT / f"{ASSET_NAME}_AngledParallaxReview.png")
    bpy.ops.render.render(write_still=True)

    set_camera("AET_ImageRelief_SideDepthCamera", (620.0, -210.0, 120.0), (0.0, -10.0, 105.0), 390.0)
    scene.render.filepath = str(REVIEW_ROOT / f"{ASSET_NAME}_SideDepthReview.png")
    bpy.ops.render.render(write_still=True)

    scene.render.resolution_x = 1500
    scene.render.resolution_y = 1000
    set_camera("AET_Test2_BackCamera", (0.0, 760.0, 145.0), (0.0, 22.0, 102.0), 420.0)
    scene.render.filepath = str(REVIEW_ROOT / f"{ASSET_NAME}_BackReview.png")
    bpy.ops.render.render(write_still=True)

    set_camera("AET_Test2_TopCamera", (0.0, -430.0, 560.0), (0.0, -8.0, 72.0), 430.0)
    scene.render.filepath = str(REVIEW_ROOT / f"{ASSET_NAME}_TopReview.png")
    bpy.ops.render.render(write_still=True)


def build_review_board() -> None:
    source = Image.open(SOURCE_IMAGE).convert("RGBA")
    front = Image.open(REVIEW_ROOT / f"{ASSET_NAME}_FrontMatchReview.png").convert("RGBA")
    angled = Image.open(REVIEW_ROOT / f"{ASSET_NAME}_AngledParallaxReview.png").convert("RGBA")
    side = Image.open(REVIEW_ROOT / f"{ASSET_NAME}_SideDepthReview.png").convert("RGBA")
    back = Image.open(REVIEW_ROOT / f"{ASSET_NAME}_BackReview.png").convert("RGBA")
    top = Image.open(REVIEW_ROOT / f"{ASSET_NAME}_TopReview.png").convert("RGBA")
    board = Image.new("RGBA", (2400, 1200), (238, 235, 228, 255))
    draw = ImageDraw.Draw(board)
    title_font = font(34)
    body_font = font(21)
    draw.text((52, 34), "A01 Test 2 Paint-01 game asset proof", fill=(25, 23, 20, 255), font=title_font)
    draw.text(
        (52, 82),
        "Technique: A01 traced/deepened mesh with authored darker albedo, Blood Axe red paint, rawhide, earth, AO, and subdued review lighting.",
        fill=(58, 52, 45, 255),
        font=body_font,
    )
    source.thumbnail((390, 470), Image.Resampling.LANCZOS)
    front.thumbnail((410, 490), Image.Resampling.LANCZOS)
    angled.thumbnail((530, 353), Image.Resampling.LANCZOS)
    side.thumbnail((430, 287), Image.Resampling.LANCZOS)
    back.thumbnail((430, 287), Image.Resampling.LANCZOS)
    top.thumbnail((430, 287), Image.Resampling.LANCZOS)
    board.alpha_composite(source, (70, 170))
    board.alpha_composite(front, (500, 120))
    board.alpha_composite(angled, (960, 165))
    board.alpha_composite(side, (1530, 165))
    board.alpha_composite(back, (960, 635))
    board.alpha_composite(top, (1530, 635))
    draw.text((70, 660), "Source A01 crop", fill=(40, 36, 32, 255), font=body_font)
    draw.text((500, 650), "Front camera match", fill=(40, 36, 32, 255), font=body_font)
    draw.text((960, 540), "Angled parallax view", fill=(40, 36, 32, 255), font=body_font)
    draw.text((1530, 540), "Side/depth check", fill=(40, 36, 32, 255), font=body_font)
    draw.text((960, 1010), "Back/inferred volume", fill=(40, 36, 32, 255), font=body_font)
    draw.text((1530, 1010), "High-angle footprint", fill=(40, 36, 32, 255), font=body_font)
    board.save(REVIEW_ROOT / f"{ASSET_NAME}_FinalGameReadyReviewBoard.png")


def build() -> None:
    make_texture_sources()
    clear_scene()
    setup_scene()
    add_review_lighting()
    materials = make_materials()

    lod0_collection = make_collection(f"{ASSET_NAME}_LOD0_ImageRelief")
    lod1_collection = make_collection(f"{ASSET_NAME}_LOD1_ImageRelief", hidden=True)
    lod2_collection = make_collection(f"{ASSET_NAME}_LOD2_ImageRelief", hidden=True)
    lod3_collection = make_collection(f"{ASSET_NAME}_LOD3_ImageRelief", hidden=True)
    collision_collection = make_collection(f"{ASSET_NAME}_Collision_Source", hidden=True)

    lod0_objects = build_lod_collection(0, materials, lod0_collection)
    lod1_objects = build_lod_collection(1, materials, lod1_collection)
    lod2_objects = build_lod_collection(2, materials, lod2_collection)
    lod3_objects = build_lod_collection(3, materials, lod3_collection)
    collision = add_collision_proxy(materials["collision"], collision_collection)

    add_asset_metadata(
        ASSET_NAME,
        "A01 Test 2 front-faithful 360 static prop: traced concept projection, deep stone shells, inferred side/back support volumes, LOD source, and UCX collision.",
        UNREAL_PATH,
    )

    blend_path = BLENDER_ROOT / REL_PATH / f"{ASSET_NAME}.blend"
    export_path = EXPORT_ROOT / REL_PATH / f"{ASSET_NAME}.fbx"
    blend_path.parent.mkdir(parents=True, exist_ok=True)
    export_path.parent.mkdir(parents=True, exist_ok=True)

    render_reviews()
    build_review_board()
    bpy.ops.wm.save_as_mainfile(filepath=str(blend_path))

    export_selected_fbx(export_path, lod0_objects + [collision])
    export_selected_fbx(export_path.with_name(f"{ASSET_NAME}_LOD0.fbx"), lod0_objects)
    export_selected_fbx(export_path.with_name(f"{ASSET_NAME}_LOD1.fbx"), lod1_objects)
    export_selected_fbx(export_path.with_name(f"{ASSET_NAME}_LOD2.fbx"), lod2_objects)
    export_selected_fbx(export_path.with_name(f"{ASSET_NAME}_LOD3.fbx"), lod3_objects)

    width, depth, height = collection_bounds(lod0_collection)
    print(f"Built {blend_path.relative_to(ROOT)}")
    print(f"Exported {export_path.relative_to(ROOT)}")
    print(f"Texture {TEXTURE_BC.relative_to(ROOT)}")
    print(f"LOD0 tris: {collection_triangle_count(lod0_collection)}")
    print(f"LOD1 tris: {collection_triangle_count(lod1_collection)}")
    print(f"LOD2 tris: {collection_triangle_count(lod2_collection)}")
    print(f"LOD3 tris: {collection_triangle_count(lod3_collection)}")
    print(f"LOD0 bounds: {width:.2f}w x {depth:.2f}d x {height:.2f}h cm")
    print("Collision proxies: 1")


if __name__ == "__main__":
    build()
