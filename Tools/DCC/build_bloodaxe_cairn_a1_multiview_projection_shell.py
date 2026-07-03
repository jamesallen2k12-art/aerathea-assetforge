#!/usr/bin/env python3
"""Build A1 Blood Axe cairn as a multi-view projection shell candidate.

Run with:
    blender --background --python Tools/DCC/build_bloodaxe_cairn_a1_multiview_projection_shell.py

This is a DCC source candidate for visual matching only. It projects the
approved turnaround's front, right, back, left, and top views onto simple
orthographic shells so the front-only failure can be tested against all
approved view angles. It is not visual canon and not fully game-ready.
"""

from __future__ import annotations

import math
import sys
from dataclasses import dataclass
from pathlib import Path

import bpy
from mathutils import Vector
from PIL import Image, ImageDraw, ImageFilter, ImageFont


ROOT = Path(__file__).resolve().parents[2]
SOURCE_ROOT = ROOT / "SourceAssets"
BLENDER_ROOT = SOURCE_ROOT / "Blender"
EXPORT_ROOT = SOURCE_ROOT / "Exports"
TEXTURE_ROOT = SOURCE_ROOT / "Textures"

ASSET_NAME = "SM_GIA_BloodAxeCairnSlabCluster_A01_MultiViewProjectionShell"
REL_PATH = f"Props/Giants/BloodAxe/Cairns/{ASSET_NAME}"
UNREAL_PATH = f"/Game/Aerathea/Props/Giants/BloodAxe/Cairns/{ASSET_NAME}"
REVIEW_ROOT = ROOT / "Saved" / "Automation" / "DCC" / ASSET_NAME
TEXTURE_DIR = TEXTURE_ROOT / REL_PATH

TURNAROUND = ROOT / "docs/assets/visual_canon/VC_GIA_BloodAxe_CairnStones_A01_A1_TurnaroundDraft_A01.png"

sys.path.insert(0, str(ROOT))
from Tools.DCC.build_next_slice_assets import add_asset_metadata, clear_scene, setup_scene  # noqa: E402


@dataclass(frozen=True)
class ViewSpec:
    name: str
    box: tuple[int, int, int, int]
    plane: str
    location: tuple[float, float, float]
    width_cm: float
    height_cm: float


VIEWS = [
    ViewSpec("Front", (58, 66, 492, 268), "front", (0.0, -88.0, 105.0), 335.0, 210.0),
    ViewSpec("Right", (1028, 66, 1470, 294), "right", (120.0, 0.0, 105.0), 220.0, 210.0),
    ViewSpec("Back", (540, 307, 985, 535), "back", (0.0, 88.0, 105.0), 335.0, 210.0),
    ViewSpec("Left", (52, 625, 492, 858), "left", (-120.0, 0.0, 105.0), 220.0, 210.0),
    ViewSpec("Top", (1072, 650, 1462, 900), "top", (0.0, 0.0, 8.0), 335.0, 220.0),
]


def resample_lanczos() -> int:
    if hasattr(Image, "Resampling"):
        return Image.Resampling.LANCZOS
    return Image.LANCZOS


def ensure_dir(path: Path) -> None:
    path.mkdir(parents=True, exist_ok=True)


def font(size: int) -> ImageFont.ImageFont:
    for path in (
        "/usr/share/fonts/dejavu-sans-fonts/DejaVuSans.ttf",
        "/usr/share/fonts/dejavu/DejaVuSans.ttf",
    ):
        if Path(path).exists():
            return ImageFont.truetype(path, size)
    return ImageFont.load_default()


def masked_crop(source: Image.Image, spec: ViewSpec) -> Path:
    ensure_dir(TEXTURE_DIR)
    crop = source.crop(spec.box).convert("RGBA")
    crop = crop.resize((1024, 512), resample_lanczos())
    pixels = crop.load()
    width, height = crop.size
    corners = [
        crop.getpixel((4, 4)),
        crop.getpixel((width - 5, 4)),
        crop.getpixel((4, height - 5)),
        crop.getpixel((width - 5, height - 5)),
    ]
    bg = tuple(int(sum(pixel[i] for pixel in corners) / len(corners)) for i in range(3))
    alpha = Image.new("L", crop.size, 0)
    alpha_pixels = alpha.load()
    for y in range(height):
        for x in range(width):
            red, green, blue, _ = pixels[x, y]
            dist = abs(red - bg[0]) + abs(green - bg[1]) + abs(blue - bg[2])
            marker = max(red, green, blue) - min(red, green, blue) > 90 and max(red, green, blue) > 170
            if dist > 34 and not marker:
                alpha_pixels[x, y] = 255
    alpha = alpha.filter(ImageFilter.MaxFilter(5)).filter(ImageFilter.GaussianBlur(radius=0.6))
    crop.putalpha(alpha)
    path = TEXTURE_DIR / f"T_GIA_BloodAxeCairnSlabCluster_A01_MultiView_{spec.name}_BC.png"
    crop.save(path)
    return path


def make_textures() -> dict[str, Path]:
    source = Image.open(TURNAROUND).convert("RGBA")
    return {spec.name: masked_crop(source, spec) for spec in VIEWS}


def make_projection_material(name: str, texture: Path) -> bpy.types.Material:
    material = bpy.data.materials.new(name)
    material.diffuse_color = (1.0, 1.0, 1.0, 1.0)
    material.use_nodes = True
    material.blend_method = "BLEND"
    material.show_transparent_back = True
    nodes = material.node_tree.nodes
    bsdf = nodes.get("Principled BSDF")
    tex = nodes.new(type="ShaderNodeTexImage")
    tex.image = bpy.data.images.load(str(texture))
    if bsdf is not None:
        material.node_tree.links.new(tex.outputs["Color"], bsdf.inputs["Base Color"])
        if "Alpha" in tex.outputs and "Alpha" in bsdf.inputs:
            material.node_tree.links.new(tex.outputs["Alpha"], bsdf.inputs["Alpha"])
        bsdf.inputs["Roughness"].default_value = 0.88
        if "Emission Color" in bsdf.inputs:
            bsdf.inputs["Emission Color"].default_value = (0.14, 0.12, 0.10, 1.0)
        if "Emission Strength" in bsdf.inputs:
            bsdf.inputs["Emission Strength"].default_value = 0.16
    return material


def make_solid_material(name: str, color: tuple[float, float, float, float]) -> bpy.types.Material:
    material = bpy.data.materials.new(name)
    material.diffuse_color = color
    material.use_nodes = True
    bsdf = material.node_tree.nodes.get("Principled BSDF")
    if bsdf is not None:
        bsdf.inputs["Base Color"].default_value = color
        bsdf.inputs["Roughness"].default_value = 0.92
        if "Emission Color" in bsdf.inputs:
            bsdf.inputs["Emission Color"].default_value = (color[0] * 0.45, color[1] * 0.45, color[2] * 0.45, 1.0)
        if "Emission Strength" in bsdf.inputs:
            bsdf.inputs["Emission Strength"].default_value = 0.12
    return material


def make_collection(name: str, hidden: bool = False) -> bpy.types.Collection:
    collection = bpy.data.collections.new(name)
    bpy.context.scene.collection.children.link(collection)
    collection.hide_viewport = hidden
    collection.hide_render = hidden
    return collection


def add_plane(spec: ViewSpec, material: bpy.types.Material, collection: bpy.types.Collection, lod: int) -> bpy.types.Object:
    w = spec.width_cm / 2.0
    h = spec.height_cm / 2.0
    if spec.plane == "front":
        verts = [(-w, 0, -h), (w, 0, -h), (w, 0, h), (-w, 0, h)]
    elif spec.plane == "back":
        verts = [(w, 0, -h), (-w, 0, -h), (-w, 0, h), (w, 0, h)]
    elif spec.plane == "right":
        verts = [(0, w, -h), (0, -w, -h), (0, -w, h), (0, w, h)]
    elif spec.plane == "left":
        verts = [(0, -w, -h), (0, w, -h), (0, w, h), (0, -w, h)]
    else:
        # Top view is horizontal XY, with image top toward positive Y.
        verts = [(-w, -h, 0), (w, -h, 0), (w, h, 0), (-w, h, 0)]
    mesh = bpy.data.meshes.new(f"{ASSET_NAME}_{spec.name}_LOD{lod}_Mesh")
    mesh.from_pydata(verts, [], [(0, 1, 2, 3)])
    mesh.update()
    obj = bpy.data.objects.new(f"{ASSET_NAME}_{spec.name}_LOD{lod}", mesh)
    obj.location = spec.location
    obj.data.materials.append(material)
    uv = obj.data.uv_layers.new(name="A1_MultiViewUV")
    for polygon in obj.data.polygons:
        coords = [(0, 0), (1, 0), (1, 1), (0, 1)]
        for loop_index, coord in zip(polygon.loop_indices, coords):
            uv.data[loop_index].uv = coord
    collection.objects.link(obj)
    return obj


def set_active(obj: bpy.types.Object) -> None:
    bpy.ops.object.select_all(action="DESELECT")
    bpy.context.view_layer.objects.active = obj
    obj.select_set(True)


def move_to(obj: bpy.types.Object, collection: bpy.types.Collection) -> None:
    for current in list(obj.users_collection):
        current.objects.unlink(obj)
    collection.objects.link(obj)


def add_support(name: str, collection: bpy.types.Collection, material: bpy.types.Material, loc: tuple[float, float, float], dims: tuple[float, float, float], rot: tuple[float, float, float]) -> bpy.types.Object:
    bpy.ops.mesh.primitive_cube_add(size=1.0, location=loc, rotation=rot)
    obj = bpy.context.object
    obj.name = name
    obj.dimensions = dims
    obj.data.materials.append(material)
    set_active(obj)
    bpy.ops.object.transform_apply(location=False, rotation=False, scale=True)
    bevel = obj.modifiers.new("AET_projection_shell_chipped_edges", "BEVEL")
    bevel.width = max(1.0, min(dims) * 0.06)
    bevel.segments = 1
    bpy.ops.object.modifier_apply(modifier=bevel.name)
    move_to(obj, collection)
    return obj


def add_supports(collection: bpy.types.Collection, material: bpy.types.Material, lod: int) -> list[bpy.types.Object]:
    if lod > 1:
        return []
    specs = [
        ("RearCoreStone", (0.0, 60.0, 74.0), (46.0, 28.0, 118.0), (-0.10, -0.20, 0.10)),
        ("LeftSideCoreStone", (-84.0, 28.0, 45.0), (34.0, 80.0, 64.0), (0.08, 0.12, -0.18)),
        ("RightSideCoreStone", (92.0, 18.0, 42.0), (36.0, 78.0, 62.0), (-0.07, -0.10, 0.16)),
        ("GroundCore", (0.0, 0.0, 15.0), (246.0, 152.0, 24.0), (0.0, 0.0, 0.03)),
    ]
    return [
        add_support(f"{ASSET_NAME}_{name}_LOD{lod}", collection, material, loc, dims, rot)
        for name, loc, dims, rot in specs
    ]


def add_collision(material: bpy.types.Material, collection: bpy.types.Collection) -> bpy.types.Object:
    bpy.ops.mesh.primitive_cube_add(size=1.0, location=(0.0, 0.0, 92.0))
    obj = bpy.context.object
    obj.name = f"UCX_{ASSET_NAME}_00"
    obj.dimensions = (340.0, 230.0, 190.0)
    obj.data.materials.append(material)
    set_active(obj)
    bpy.ops.object.transform_apply(location=False, rotation=False, scale=True)
    obj.display_type = "WIRE"
    obj.hide_render = True
    move_to(obj, collection)
    return obj


def triangle_count(obj: bpy.types.Object) -> int:
    obj.data.calc_loop_triangles()
    return len(obj.data.loop_triangles)


def collection_triangles(collection: bpy.types.Collection) -> int:
    return sum(triangle_count(obj) for obj in collection.objects if obj.type == "MESH")


def collection_bounds(collection: bpy.types.Collection) -> tuple[float, float, float]:
    points = []
    for obj in collection.objects:
        if obj.type == "MESH":
            points.extend(obj.matrix_world @ Vector(corner) for corner in obj.bound_box)
    return (
        max(point.x for point in points) - min(point.x for point in points),
        max(point.y for point in points) - min(point.y for point in points),
        max(point.z for point in points) - min(point.z for point in points),
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
        scene.render.engine = "BLENDER_EEVEE"
    except TypeError:
        pass
    try:
        scene.view_settings.view_transform = "Standard"
    except TypeError:
        pass
    scene.view_settings.exposure = 0.0
    scene.view_settings.gamma = 1.0
    if scene.world:
        scene.world.color = (0.54, 0.52, 0.48)
    for name, loc, energy, size in [
        ("AET_MultiView_Key", (-260, -420, 560), 8200, 520),
        ("AET_MultiView_Fill", (280, 220, 350), 4200, 620),
    ]:
        data = bpy.data.lights.new(name, "AREA")
        data.energy = energy
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
    scene.render.resolution_x = 1500
    scene.render.resolution_y = 1000
    reviews = [
        ("Front", (0, -720, 130), (0, 0, 92), 355),
        ("Right", (680, 0, 130), (0, 0, 92), 355),
        ("Back", (0, 720, 130), (0, 0, 92), 355),
        ("Left", (-680, 0, 130), (0, 0, 92), 355),
        ("Top", (0, 0, 720), (0, 0, 0), 360),
        ("Beauty", (360, -540, 260), (0, 0, 92), 380),
    ]
    for label, loc, target, scale in reviews:
        set_camera(f"AET_MultiView_{label}Camera", loc, target, scale)
        scene.render.filepath = str(REVIEW_ROOT / f"{ASSET_NAME}_{label}Review.png")
        bpy.ops.render.render(write_still=True)


def build_review_board() -> None:
    source = Image.open(TURNAROUND).convert("RGBA")
    front = Image.open(REVIEW_ROOT / f"{ASSET_NAME}_FrontReview.png").convert("RGBA")
    right = Image.open(REVIEW_ROOT / f"{ASSET_NAME}_RightReview.png").convert("RGBA")
    back = Image.open(REVIEW_ROOT / f"{ASSET_NAME}_BackReview.png").convert("RGBA")
    top = Image.open(REVIEW_ROOT / f"{ASSET_NAME}_TopReview.png").convert("RGBA")
    board = Image.new("RGBA", (2400, 1200), (238, 235, 228, 255))
    draw = ImageDraw.Draw(board)
    draw.text((52, 32), "A01 Multi-view projection shell DCC candidate", fill=(25, 23, 20, 255), font=font(32))
    draw.text((52, 78), "Purpose: test approved front/right/back/top concept matching before true sculpted 360 lock.", fill=(58, 52, 45, 255), font=font(21))
    source.thumbnail((780, 520), resample_lanczos())
    front.thumbnail((420, 280), resample_lanczos())
    right.thumbnail((420, 280), resample_lanczos())
    back.thumbnail((420, 280), resample_lanczos())
    top.thumbnail((420, 280), resample_lanczos())
    board.alpha_composite(source, (58, 150))
    board.alpha_composite(front, (900, 150))
    board.alpha_composite(right, (1420, 150))
    board.alpha_composite(back, (900, 620))
    board.alpha_composite(top, (1420, 620))
    draw.text((58, 700), "Approved multi-angle turnaround", fill=(40, 36, 32, 255), font=font(20))
    draw.text((900, 450), "DCC Front shell", fill=(40, 36, 32, 255), font=font(20))
    draw.text((1420, 450), "DCC Right shell", fill=(40, 36, 32, 255), font=font(20))
    draw.text((900, 920), "DCC Back shell", fill=(40, 36, 32, 255), font=font(20))
    draw.text((1420, 920), "DCC Top shell", fill=(40, 36, 32, 255), font=font(20))
    board.save(REVIEW_ROOT / f"{ASSET_NAME}_ReviewBoard.png")


def build() -> None:
    clear_scene()
    setup_scene()
    setup_lighting()
    textures = make_textures()
    materials = {name: make_projection_material(f"M_GIA_BloodAxeCairn_A01_MultiView_{name}", path) for name, path in textures.items()}
    side_material = make_solid_material("M_GIA_BloodAxeCairn_A01_MultiView_SideStone", (0.42, 0.39, 0.32, 1.0))
    collision_material = make_solid_material("M_AET_CollisionProxy_ReviewOnly_A01", (0.1, 0.42, 0.95, 0.25))

    lod_collections = [make_collection(f"{ASSET_NAME}_LOD{i}", hidden=i > 0) for i in range(4)]
    collision_collection = make_collection(f"{ASSET_NAME}_Collision_Source", hidden=True)

    lod_objects: list[list[bpy.types.Object]] = []
    for lod in range(4):
        objects = []
        for spec in VIEWS:
            if lod >= 2 and spec.name in {"Left", "Right"}:
                continue
            objects.append(add_plane(spec, materials[spec.name], lod_collections[lod], lod))
        objects.extend(add_supports(lod_collections[lod], side_material, lod))
        lod_objects.append(objects)

    collision = add_collision(collision_material, collision_collection)
    add_asset_metadata(
        ASSET_NAME,
        "A01 multi-view projection shell candidate using approved turnaround front/right/back/left/top panels. DCC source candidate only; not fully game-ready or canon.",
        UNREAL_PATH,
    )

    render_reviews()
    build_review_board()

    blend_path = BLENDER_ROOT / REL_PATH / f"{ASSET_NAME}.blend"
    export_path = EXPORT_ROOT / REL_PATH / f"{ASSET_NAME}.fbx"
    ensure_dir(blend_path.parent)
    ensure_dir(export_path.parent)
    bpy.ops.wm.save_as_mainfile(filepath=str(blend_path))

    export_fbx(export_path, lod_objects[0] + [collision])
    for lod, objects in enumerate(lod_objects):
        export_fbx(export_path.with_name(f"{ASSET_NAME}_LOD{lod}.fbx"), objects)
    export_fbx(export_path.with_name(f"{ASSET_NAME}_UCX.fbx"), [collision])

    width, depth, height = collection_bounds(lod_collections[0])
    print(f"Built {blend_path.relative_to(ROOT)}")
    print(f"Exported {export_path.relative_to(ROOT)}")
    for lod, collection in enumerate(lod_collections):
        print(f"LOD{lod} tris: {collection_triangles(collection)}")
    print(f"LOD0 bounds: {width:.2f}w x {depth:.2f}d x {height:.2f}h cm")
    print("Collision proxies: 1")


if __name__ == "__main__":
    build()
