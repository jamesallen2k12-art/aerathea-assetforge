#!/usr/bin/env python3
"""Build an A1 image-relief cairn asset from the approved concept crop.

Run with:
    blender --background --python Tools/DCC/build_bloodaxe_cairn_a1_image_relief_asset.py

This follows the single-image / 2D-painting-to-3D workflow:
- isolate the approved painted image as a texture
- trace major visible layers into shallow mesh shells
- project the image onto those mesh faces
- add thickness, LODs, collision, and review renders

It is a camera-faithful relief asset candidate, not a fully inferred 360 sculpt.
"""

from __future__ import annotations

import math
import sys
from dataclasses import dataclass
from pathlib import Path

import bpy
from mathutils import Vector
from mathutils.geometry import tessellate_polygon
from PIL import Image, ImageDraw, ImageFilter, ImageFont


ROOT = Path(__file__).resolve().parents[2]
SOURCE_ROOT = ROOT / "SourceAssets"
BLENDER_ROOT = SOURCE_ROOT / "Blender"
EXPORT_ROOT = SOURCE_ROOT / "Exports"
TEXTURE_ROOT = SOURCE_ROOT / "Textures"

ASSET_NAME = "SM_GIA_BloodAxeCairnSlabCluster_A01_ImageRelief"
REL_PATH = f"Props/Giants/BloodAxe/Cairns/{ASSET_NAME}"
UNREAL_PATH = f"/Game/Aerathea/Props/Giants/BloodAxe/Cairns/{ASSET_NAME}"
REVIEW_ROOT = ROOT / "Saved/Automation/DCC" / ASSET_NAME

SOURCE_IMAGE = ROOT / "docs/assets/visual_canon/VC_GIA_BloodAxe_CairnStones_A01_A1_Crop.png"
TEXTURE_DIR = TEXTURE_ROOT / REL_PATH
TEXTURE_BC = TEXTURE_DIR / "T_GIA_BloodAxeCairnSlabCluster_A01_ImageRelief_BC.png"
TEXTURE_N = TEXTURE_DIR / "T_GIA_BloodAxeCairnSlabCluster_A01_ImageRelief_N.png"
TEXTURE_ORM = TEXTURE_DIR / "T_GIA_BloodAxeCairnSlabCluster_A01_ImageRelief_ORM.png"

IMAGE_WIDTH = 360
IMAGE_HEIGHT = 430
GROUND_BASELINE_PX = 368.0
PIXEL_SCALE_CM = 1.0

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
        3.0,
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
        5.0,
        2,
    ),
    ReliefLayer(
        "A1_ImageRelief_MainPaintedSlab",
        (
            (66, 255), (104, 226), (149, 207), (201, 219), (260, 245),
            (258, 282), (206, 306), (145, 299), (86, 282),
        ),
        -26.0,
        12.0,
        2,
    ),
    ReliefLayer(
        "A1_ImageRelief_RearTallSlab",
        (
            (154, 226), (160, 198), (166, 174), (176, 158), (191, 161),
            (207, 185), (216, 219), (205, 248), (182, 265), (164, 251),
        ),
        32.0,
        12.0,
        2,
    ),
    ReliefLayer(
        "A1_ImageRelief_LeftStoneStackBack",
        (
            (56, 258), (95, 229), (139, 239), (156, 268), (120, 297),
            (68, 290),
        ),
        -12.0,
        9.0,
        1,
    ),
    ReliefLayer(
        "A1_ImageRelief_LeftStoneStackFront",
        (
            (51, 289), (101, 274), (154, 292), (139, 317), (73, 314),
        ),
        -52.0,
        10.0,
        1,
    ),
    ReliefLayer(
        "A1_ImageRelief_RightUpright",
        (
            (240, 260), (250, 228), (266, 211), (282, 207), (295, 219),
            (299, 247), (292, 277), (270, 287), (250, 276),
        ),
        -6.0,
        10.0,
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
        5.0,
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
    source.putalpha(alpha)
    source = source.resize((IMAGE_WIDTH * 4, IMAGE_HEIGHT * 4), Image.Resampling.LANCZOS)
    source.save(TEXTURE_BC)
    Image.new("RGBA", source.size, (128, 128, 255, 255)).save(TEXTURE_N)
    Image.new("RGBA", source.size, (255, 190, 0, 255)).save(TEXTURE_ORM)


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
    material = bpy.data.materials.new("MI_GIA_BloodAxeCairn_A01_ImageRelief_BC")
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
            material.node_tree.links.new(texture.outputs["Color"], bsdf.inputs["Emission Color"])
        if "Emission Strength" in bsdf.inputs:
            bsdf.inputs["Emission Strength"].default_value = 0.35
    return material


def make_solid_material(name: str, color: tuple[float, float, float, float]) -> bpy.types.Material:
    material = bpy.data.materials.new(name)
    material.diffuse_color = color
    material.use_nodes = True
    bsdf = material.node_tree.nodes.get("Principled BSDF")
    if bsdf is not None:
        bsdf.inputs["Base Color"].default_value = color
        bsdf.inputs["Roughness"].default_value = 0.94
    return material


def make_materials() -> dict[str, bpy.types.Material]:
    return {
        "image": make_image_material(),
        "side": make_solid_material("M_GIA_BloodAxeCairn_A01_ImageRelief_SideStone", (0.22, 0.21, 0.18, 1.0)),
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


def add_collision_proxy(material: bpy.types.Material, collection: bpy.types.Collection) -> bpy.types.Object:
    bpy.ops.mesh.primitive_cube_add(size=1.0, location=(0.0, -10.0, 105.0))
    obj = bpy.context.object
    obj.name = f"UCX_{ASSET_NAME}_00"
    obj.dimensions = (338.0, 156.0, 220.0)
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
    scene.view_settings.exposure = 0.2
    scene.view_settings.gamma = 1.0
    if scene.world is not None:
        scene.world.color = (0.60, 0.58, 0.54)
    for name, kind, location, energy, size in [
        ("AET_ImageRelief_Key", "AREA", (-260.0, -420.0, 580.0), 7000.0, 520.0),
        ("AET_ImageRelief_Fill", "AREA", (260.0, -260.0, 300.0), 2600.0, 620.0),
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


def build_review_board() -> None:
    source = Image.open(SOURCE_IMAGE).convert("RGBA")
    front = Image.open(REVIEW_ROOT / f"{ASSET_NAME}_FrontMatchReview.png").convert("RGBA")
    angled = Image.open(REVIEW_ROOT / f"{ASSET_NAME}_AngledParallaxReview.png").convert("RGBA")
    side = Image.open(REVIEW_ROOT / f"{ASSET_NAME}_SideDepthReview.png").convert("RGBA")
    board = Image.new("RGBA", (2200, 1200), (238, 235, 228, 255))
    draw = ImageDraw.Draw(board)
    title_font = font(34)
    body_font = font(21)
    draw.text((52, 34), "A1 image-relief game asset proof", fill=(25, 23, 20, 255), font=title_font)
    draw.text(
        (52, 82),
        "Technique from the references: image-as-texture, traced mesh layers, shallow extrusion, and camera-matched projection.",
        fill=(58, 52, 45, 255),
        font=body_font,
    )
    source.thumbnail((380, 455), Image.Resampling.LANCZOS)
    front.thumbnail((480, 573), Image.Resampling.LANCZOS)
    angled.thumbnail((650, 433), Image.Resampling.LANCZOS)
    side.thumbnail((520, 347), Image.Resampling.LANCZOS)
    board.alpha_composite(source, (70, 180))
    board.alpha_composite(front, (500, 120))
    board.alpha_composite(angled, (1040, 155))
    board.alpha_composite(side, (1040, 640))
    draw.text((70, 650), "Source A1 crop", fill=(40, 36, 32, 255), font=body_font)
    draw.text((500, 720), "Front camera match", fill=(40, 36, 32, 255), font=body_font)
    draw.text((1040, 600), "Angled parallax view", fill=(40, 36, 32, 255), font=body_font)
    draw.text((1040, 1005), "Side/depth check", fill=(40, 36, 32, 255), font=body_font)
    board.save(REVIEW_ROOT / f"{ASSET_NAME}_ImageReliefReviewBoard.png")


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
        "A1 image-relief static mesh candidate using concept-projected traced layers. Camera-faithful relief asset, not a full 360 sculpt.",
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
