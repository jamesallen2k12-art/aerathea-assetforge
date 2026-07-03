#!/usr/bin/env python3
"""Build the completed 360 Blood Axe cairn slab cluster candidate.

Run with:
    blender --background --python Tools/DCC/build_bloodaxe_cairn_a1_complete_asset.py

This is the full-static-prop pass after the image-relief proof. It keeps the
approved Blood Axe cairn read, but it is authored as actual 360-degree stone
volumes with side/back treatment, painted Blood Axe marks, rawhide bindings,
texture sets, LOD source exports, collision proxy, and review renders.
"""

from __future__ import annotations

import math
import sys
from array import array
from pathlib import Path

import bpy
from mathutils import Matrix, Vector


ROOT = Path(__file__).resolve().parents[2]
SOURCE_ROOT = ROOT / "SourceAssets"
BLENDER_ROOT = SOURCE_ROOT / "Blender"
EXPORT_ROOT = SOURCE_ROOT / "Exports"
TEXTURE_ROOT = SOURCE_ROOT / "Textures"
REVIEW_ROOT = ROOT / "Saved" / "Automation" / "DCC" / "SM_GIA_BloodAxeCairnSlabCluster_A01_Complete"

ASSET_NAME = "SM_GIA_BloodAxeCairnSlabCluster_A01_Complete"
REL_PATH = f"Props/Giants/BloodAxe/Cairns/{ASSET_NAME}"
UNREAL_PATH = f"/Game/Aerathea/Props/Giants/BloodAxe/Cairns/{ASSET_NAME}"

sys.path.insert(0, str(ROOT))

from Tools.DCC.build_next_slice_assets import add_asset_metadata, clear_scene, setup_scene  # noqa: E402


def ensure_dir(path: Path) -> None:
    path.mkdir(parents=True, exist_ok=True)


def deterministic_noise(x: int, y: int, seed: int) -> float:
    value = (x * 374761393 + y * 668265263 + seed * 2654435761) & 0xFFFFFFFF
    value = (value ^ (value >> 13)) * 1274126177 & 0xFFFFFFFF
    return ((value ^ (value >> 16)) & 0xFFFF) / 65535.0


def clamp(value: float) -> float:
    return max(0.0, min(1.0, value))


def save_texture(path: Path, width: int, height: int, pixels: array) -> None:
    ensure_dir(path.parent)
    image = bpy.data.images.new(path.stem, width=width, height=height, alpha=True, float_buffer=False)
    image.pixels.foreach_set(pixels)
    image.filepath_raw = str(path)
    image.file_format = "PNG"
    image.save()
    bpy.data.images.remove(image)


def generate_texture_set(label: str, base: tuple[float, float, float], accent: tuple[float, float, float], seed: int) -> dict[str, Path]:
    texture_dir = TEXTURE_ROOT / REL_PATH
    ensure_dir(texture_dir)
    width = 1024
    height = 1024
    bc = array("f")
    normal = array("f")
    orm = array("f")
    for y in range(height):
        for x in range(width):
            n1 = deterministic_noise(x, y, seed)
            n2 = deterministic_noise(x // 5, y // 5, seed + 17)
            vein = 1.0 if deterministic_noise(x // 29, y // 23, seed + 41) > 0.94 else 0.0
            chip = 1.0 if deterministic_noise(x // 17, y // 19, seed + 71) > 0.985 else 0.0
            mix = ((n1 * 0.34) + (n2 * 0.24) + (vein * 0.06) + (chip * 0.05)) * 0.62
            color = (
                base[0] * (1.0 - mix) + accent[0] * mix,
                base[1] * (1.0 - mix) + accent[1] * mix,
                base[2] * (1.0 - mix) + accent[2] * mix,
            )
            if chip:
                color = (min(color[0] + 0.10, 1.0), min(color[1] + 0.085, 1.0), min(color[2] + 0.065, 1.0))
            bc.extend((clamp(color[0]), clamp(color[1]), clamp(color[2]), 1.0))

            bump = ((n1 - 0.5) * 0.18) + ((n2 - 0.5) * 0.08)
            normal.extend((clamp(0.5 + bump), clamp(0.5 + (deterministic_noise(x, y, seed + 101) - 0.5) * 0.12), 1.0, 1.0))
            occlusion = 0.54 + (1.0 - n2) * 0.28
            roughness = 0.82 + n1 * 0.13
            orm.extend((clamp(occlusion), clamp(roughness), 0.0, 1.0))

    paths = {
        "bc": texture_dir / f"T_GIA_BloodAxeCairnSlabCluster_A01_Complete_{label}_BC.png",
        "n": texture_dir / f"T_GIA_BloodAxeCairnSlabCluster_A01_Complete_{label}_N.png",
        "orm": texture_dir / f"T_GIA_BloodAxeCairnSlabCluster_A01_Complete_{label}_ORM.png",
    }
    save_texture(paths["bc"], width, height, bc)
    save_texture(paths["n"], width, height, normal)
    save_texture(paths["orm"], width, height, orm)
    return paths


def generate_textures() -> dict[str, dict[str, Path]]:
    return {
        "stone": generate_texture_set("Stone", (0.34, 0.32, 0.27), (0.78, 0.71, 0.57), 1103),
        "earth": generate_texture_set("EarthAsh", (0.16, 0.11, 0.073), (0.43, 0.30, 0.17), 2207),
        "rawhide": generate_texture_set("Rawhide", (0.32, 0.17, 0.065), (0.70, 0.42, 0.17), 3301),
        "red": generate_texture_set("BloodAxeRedPaint", (0.58, 0.045, 0.032), (0.95, 0.16, 0.07), 4409),
    }


def make_texture_material(name: str, textures: dict[str, Path], roughness: float) -> bpy.types.Material:
    material = bpy.data.materials.new(name)
    material.diffuse_color = (1.0, 1.0, 1.0, 1.0)
    material.use_nodes = True
    nodes = material.node_tree.nodes
    bsdf = nodes.get("Principled BSDF")
    if bsdf is None:
        return material

    base = nodes.new(type="ShaderNodeTexImage")
    base.image = bpy.data.images.load(str(textures["bc"]))
    material.node_tree.links.new(base.outputs["Color"], bsdf.inputs["Base Color"])
    bsdf.inputs["Roughness"].default_value = roughness
    bsdf.inputs["Metallic"].default_value = 0.0

    normal_texture = nodes.new(type="ShaderNodeTexImage")
    normal_texture.image = bpy.data.images.load(str(textures["n"]))
    normal_texture.image.colorspace_settings.name = "Non-Color"
    normal_map = nodes.new(type="ShaderNodeNormalMap")
    normal_map.inputs["Strength"].default_value = 0.35
    material.node_tree.links.new(normal_texture.outputs["Color"], normal_map.inputs["Color"])
    material.node_tree.links.new(normal_map.outputs["Normal"], bsdf.inputs["Normal"])
    return material


def make_materials(texture_paths: dict[str, dict[str, Path]]) -> dict[str, bpy.types.Material]:
    return {
        "stone": make_texture_material("M_GIA_BloodAxeCairn_CompleteStone_A01", texture_paths["stone"], 0.9),
        "earth": make_texture_material("M_GIA_BloodAxeCairn_CompleteEarthAsh_A01", texture_paths["earth"], 0.94),
        "rawhide": make_texture_material("M_GIA_BloodAxeCairn_CompleteRawhide_A01", texture_paths["rawhide"], 0.86),
        "red": make_texture_material("M_GIA_BloodAxeCairn_CompleteBloodAxeRedPaint_A01", texture_paths["red"], 0.78),
    }


def make_collection(name: str, hidden: bool = False) -> bpy.types.Collection:
    collection = bpy.data.collections.new(name)
    bpy.context.scene.collection.children.link(collection)
    collection.hide_viewport = hidden
    collection.hide_render = hidden
    return collection


def move_to_collection(obj: bpy.types.Object, collection: bpy.types.Collection) -> None:
    for current in list(obj.users_collection):
        current.objects.unlink(obj)
    collection.objects.link(obj)


def set_active(obj: bpy.types.Object) -> None:
    bpy.ops.object.select_all(action="DESELECT")
    bpy.context.view_layer.objects.active = obj
    obj.select_set(True)


def roughen_mesh(obj: bpy.types.Object, amount: float, seed: int) -> None:
    for index, vertex in enumerate(obj.data.vertices):
        n1 = deterministic_noise(index, seed, seed + 13) - 0.5
        n2 = deterministic_noise(seed, index, seed + 29) - 0.5
        n3 = deterministic_noise(index + 5, seed + 7, seed + 43) - 0.5
        vertex.co.x += n1 * amount
        vertex.co.y += n2 * amount
        vertex.co.z += n3 * amount * 0.6


def add_rough_box(
    name: str,
    collection: bpy.types.Collection,
    material: bpy.types.Material,
    location: tuple[float, float, float],
    dimensions: tuple[float, float, float],
    rotation: tuple[float, float, float],
    seed: int,
    bevel_scale: float = 0.06,
    rough_scale: float = 0.10,
) -> bpy.types.Object:
    bpy.ops.mesh.primitive_cube_add(size=1.0, location=location, rotation=rotation)
    obj = bpy.context.object
    obj.name = name
    obj.dimensions = dimensions
    obj.data.materials.append(material)
    set_active(obj)
    bpy.ops.object.transform_apply(location=False, rotation=False, scale=True)
    bevel_width = max(0.6, min(dimensions) * bevel_scale)
    bevel = obj.modifiers.new(f"{name}_ReadableEdgeBevel", "BEVEL")
    bevel.width = bevel_width
    bevel.segments = 1
    bevel.affect = "EDGES"
    bpy.ops.object.modifier_apply(modifier=bevel.name)
    roughen_mesh(obj, min(dimensions) * rough_scale, seed)
    bpy.ops.object.shade_flat()
    move_to_collection(obj, collection)
    return obj


def add_small_stone(
    name: str,
    collection: bpy.types.Collection,
    material: bpy.types.Material,
    location: tuple[float, float, float],
    scale: tuple[float, float, float],
    rotation: tuple[float, float, float],
    seed: int,
) -> bpy.types.Object:
    bpy.ops.mesh.primitive_ico_sphere_add(subdivisions=1, radius=1.0, location=location, rotation=rotation)
    obj = bpy.context.object
    obj.name = name
    obj.scale = scale
    obj.data.materials.append(material)
    set_active(obj)
    bpy.ops.object.transform_apply(location=False, rotation=False, scale=True)
    roughen_mesh(obj, min(scale) * 0.12, seed)
    bpy.ops.object.shade_flat()
    move_to_collection(obj, collection)
    return obj


def add_irregular_disc(
    name: str,
    collection: bpy.types.Collection,
    material: bpy.types.Material,
    radius_x: float,
    radius_y: float,
    depth: float,
    segments: int,
    seed: int,
) -> bpy.types.Object:
    verts: list[tuple[float, float, float]] = []
    bottom: list[int] = []
    top: list[int] = []
    for index in range(segments):
        angle = (math.tau * index) / segments
        n = 0.84 + deterministic_noise(index, seed, seed + 5) * 0.27
        x = math.cos(angle) * radius_x * n
        y = math.sin(angle) * radius_y * (0.86 + deterministic_noise(seed, index, seed + 9) * 0.22)
        bottom.append(len(verts))
        verts.append((x, y, 0.0))
        top.append(len(verts))
        verts.append((x * 0.94, y * 0.94, depth + deterministic_noise(index, seed + 3, seed + 11) * 3.0))
    bottom_center = len(verts)
    verts.append((0.0, 0.0, 0.0))
    top_center = len(verts)
    verts.append((0.0, 0.0, depth + 1.5))
    faces: list[tuple[int, ...]] = []
    for index in range(segments):
        next_index = (index + 1) % segments
        faces.append((bottom[index], bottom[next_index], top[next_index], top[index]))
        faces.append((bottom_center, bottom[index], bottom[next_index]))
        faces.append((top_center, top[next_index], top[index]))
    mesh = bpy.data.meshes.new(f"{name}_Mesh")
    mesh.from_pydata(verts, [], faces)
    mesh.update()
    obj = bpy.data.objects.new(name, mesh)
    obj.data.materials.append(material)
    collection.objects.link(obj)
    return obj


def add_paint_strip(
    name: str,
    collection: bpy.types.Collection,
    material: bpy.types.Material,
    location: tuple[float, float, float],
    dimensions: tuple[float, float, float],
    rotation: tuple[float, float, float],
    seed: int,
) -> bpy.types.Object:
    return add_rough_box(name, collection, material, location, dimensions, rotation, seed, bevel_scale=0.12, rough_scale=0.04)


def build_asset_lod(collection: bpy.types.Collection, materials: dict[str, bpy.types.Material], lod: int) -> list[bpy.types.Object]:
    objects: list[bpy.types.Object] = []
    prefix = f"LOD{lod}"
    detail = lod == 0
    mid = lod <= 1

    objects.append(add_irregular_disc(f"{prefix}_AshMudGroundingMound", collection, materials["earth"], 185.0, 128.0, 9.0, 34 if detail else 18, 100 + lod))
    objects.append(add_irregular_disc(f"{prefix}_FrontMudAndStoneScuff", collection, materials["earth"], 122.0, 72.0, 6.0, 24 if detail else 14, 120 + lod))
    objects[-1].location = (-18.0, -32.0, 5.0)

    slab_specs = [
        ("DominantBloodAxeFaceSlab", (-12, -22, 55), (210, 54, 27), (math.radians(6), math.radians(-4), math.radians(-10)), 201),
        ("RearUprightOathStone", (58, 42, 83), (58, 35, 148), (math.radians(-8), math.radians(8), math.radians(-15)), 202),
        ("LeftStackedForeSlab", (-105, -28, 39), (112, 48, 25), (math.radians(2), math.radians(-8), math.radians(9)), 203),
        ("RightStandingGuardStone", (122, -3, 58), (44, 39, 92), (math.radians(2), math.radians(-9), math.radians(7)), 204),
        ("RearLowSupportSlab", (-42, 40, 51), (128, 42, 31), (math.radians(-3), math.radians(5), math.radians(13)), 205),
        ("FrontBrokenCapstone", (28, -75, 31), (116, 36, 20), (math.radians(4), math.radians(5), math.radians(-4)), 206),
    ]
    if detail:
        slab_specs.extend(
            [
                ("NeedleShardRearLeft", (-4, 33, 91), (26, 22, 88), (math.radians(-12), math.radians(-7), math.radians(6)), 207),
                ("SmallRightStakeStone", (162, -24, 41), (30, 25, 56), (math.radians(5), math.radians(-5), math.radians(13)), 208),
                ("LeftBackBrokenShard", (-155, 18, 34), (42, 32, 50), (math.radians(-6), math.radians(8), math.radians(-18)), 209),
            ]
        )
    elif mid:
        slab_specs.extend(
            [
                ("NeedleShardRearLeft", (-4, 33, 91), (24, 21, 80), (math.radians(-12), math.radians(-7), math.radians(6)), 207),
                ("SmallRightStakeStone", (162, -24, 41), (28, 24, 50), (math.radians(5), math.radians(-5), math.radians(13)), 208),
            ]
        )

    for label, location, dimensions, rotation, seed in slab_specs:
        objects.append(add_rough_box(f"{prefix}_Stone_{label}", collection, materials["stone"], location, dimensions, rotation, seed + lod * 31))

    if mid:
        paint_specs = [
            ("MainLongBloodAxeStroke", (-18, -49, 73), (145, 8, 2.2), (math.radians(8), math.radians(-4), math.radians(-17)), 301),
            ("MainSplitAxeStrokeLeft", (-46, -48, 76), (72, 7, 2.2), (math.radians(8), math.radians(-4), math.radians(22)), 302),
            ("MainSplitAxeStrokeRight", (30, -45, 80), (82, 7, 2.2), (math.radians(8), math.radians(-4), math.radians(-43)), 303),
            ("RearStoneWarPaintSlashA", (49, 17, 126), (56, 7, 2.0), (math.radians(-8), math.radians(8), math.radians(-35)), 304),
            ("RearStoneWarPaintSlashB", (72, 15, 102), (48, 6, 2.0), (math.radians(-8), math.radians(8), math.radians(18)), 305),
            ("LeftForeSlabRedSmear", (-104, -58, 52), (76, 7, 2.0), (math.radians(5), math.radians(-6), math.radians(0)), 306),
        ]
        for label, location, dimensions, rotation, seed in paint_specs:
            objects.append(add_paint_strip(f"{prefix}_BloodAxePaint_{label}", collection, materials["red"], location, dimensions, rotation, seed + lod * 37))

    if detail:
        rawhide_specs = [
            ("CenterRawhideBindingA", (-52, -55, 63), (72, 8, 5), (math.radians(8), math.radians(-4), math.radians(73)), 401),
            ("CenterRawhideBindingB", (-38, -54, 67), (66, 7, 5), (math.radians(8), math.radians(-4), math.radians(76)), 402),
            ("RightStoneLashing", (128, -30, 55), (52, 6, 5), (math.radians(8), math.radians(-4), math.radians(94)), 403),
        ]
        for label, location, dimensions, rotation, seed in rawhide_specs:
            objects.append(add_paint_strip(f"{prefix}_Rawhide_{label}", collection, materials["rawhide"], location, dimensions, rotation, seed))

        pebble_specs = [
            (-142, -73, 17, (17, 12, 8), 501),
            (-92, -95, 16, (19, 13, 8), 502),
            (-28, -108, 14, (13, 11, 7), 503),
            (66, -101, 16, (20, 11, 8), 504),
            (145, -77, 17, (15, 12, 9), 505),
            (176, 35, 18, (18, 13, 10), 506),
            (-175, 36, 17, (22, 14, 10), 507),
            (8, 92, 18, (18, 13, 9), 508),
        ]
        for x, y, z, scale, seed in pebble_specs:
            objects.append(
                add_small_stone(
                    f"{prefix}_LooseStone_{seed}",
                    collection,
                    materials["stone"],
                    (x, y, z),
                    scale,
                    (math.radians(seed % 17), math.radians(seed % 11), math.radians(seed % 29)),
                    seed,
                )
            )

    return objects


def add_collision_proxy(collection: bpy.types.Collection, material: bpy.types.Material) -> bpy.types.Object:
    obj = add_rough_box(
        f"UCX_{ASSET_NAME}_00",
        collection,
        material,
        (0.0, -3.0, 72.0),
        (365.0, 250.0, 155.0),
        (0.0, 0.0, 0.0),
        9001,
        bevel_scale=0.01,
        rough_scale=0.0,
    )
    obj.hide_viewport = True
    obj.hide_render = True
    return obj


def object_triangles(objects: list[bpy.types.Object]) -> int:
    total = 0
    for obj in objects:
        if obj.type != "MESH":
            continue
        total += sum(max(1, len(poly.vertices) - 2) for poly in obj.data.polygons)
    return total


def export_objects(objects: list[bpy.types.Object], path: Path) -> None:
    ensure_dir(path.parent)
    bpy.ops.object.select_all(action="DESELECT")
    for obj in objects:
        obj.select_set(True)
    bpy.context.view_layer.objects.active = objects[0]
    bpy.ops.export_scene.fbx(
        filepath=str(path),
        use_selection=True,
        object_types={"MESH"},
        apply_unit_scale=True,
        apply_scale_options="FBX_SCALE_UNITS",
        add_leaf_bones=False,
        bake_space_transform=False,
        mesh_smooth_type="FACE",
    )


def look_at(camera: bpy.types.Object, target: Vector) -> None:
    direction = target - camera.location
    camera.rotation_euler = direction.to_track_quat("-Z", "Y").to_euler()


def configure_review_scene() -> tuple[bpy.types.Object, Vector]:
    world = bpy.context.scene.world or bpy.data.worlds.new("AeratheaDCCWorld")
    bpy.context.scene.world = world
    world.color = (0.62, 0.62, 0.62)

    scene = bpy.context.scene
    scene.view_settings.view_transform = "Standard"
    scene.view_settings.look = "None"
    scene.view_settings.exposure = 0.45
    scene.view_settings.gamma = 1.0

    bpy.ops.object.light_add(type="AREA", location=(-260, -300, 420))
    key = bpy.context.object
    key.name = "AET_DCC_Key_Area"
    key.data.energy = 1200.0
    key.data.size = 420.0

    bpy.ops.object.light_add(type="POINT", location=(260, -240, 180))
    fill = bpy.context.object
    fill.name = "AET_DCC_Fill_Point"
    fill.data.energy = 260.0
    fill.data.shadow_soft_size = 380.0

    bpy.ops.object.camera_add(location=(315, -430, 220))
    camera = bpy.context.object
    camera.name = "AET_DCC_ReviewCamera"
    camera.data.lens = 45
    camera.data.sensor_width = 32
    bpy.context.scene.camera = camera
    target = Vector((0.0, -4.0, 68.0))
    look_at(camera, target)
    return camera, target


def render_view(camera: bpy.types.Object, target: Vector, location: tuple[float, float, float], path: Path, resolution: tuple[int, int]) -> None:
    camera.location = location
    look_at(camera, target)
    ensure_dir(path.parent)
    scene = bpy.context.scene
    scene.render.resolution_x = resolution[0]
    scene.render.resolution_y = resolution[1]
    scene.eevee.taa_render_samples = 64
    scene.render.filepath = str(path)
    bpy.ops.render.render(write_still=True)


def compose_review_board(image_paths: list[Path], output_path: Path, tile_width: int, tile_height: int) -> None:
    cols = 2
    rows = 2
    board_width = tile_width * cols
    board_height = tile_height * rows
    board = array("f", [0.0] * (board_width * board_height * 4))
    for tile_index, path in enumerate(image_paths):
        image = bpy.data.images.load(str(path))
        pixels = array("f", [0.0] * (tile_width * tile_height * 4))
        image.pixels.foreach_get(pixels)
        col = tile_index % cols
        row = tile_index // cols
        x_offset = col * tile_width
        y_offset = (rows - 1 - row) * tile_height
        for y in range(tile_height):
            for x in range(tile_width):
                src_index = ((y * tile_width) + x) * 4
                dst_index = (((y + y_offset) * board_width) + (x + x_offset)) * 4
                board[dst_index : dst_index + 4] = pixels[src_index : src_index + 4]
        bpy.data.images.remove(image)

    ensure_dir(output_path.parent)
    board_image = bpy.data.images.new(output_path.stem, width=board_width, height=board_height, alpha=True, float_buffer=False)
    board_image.pixels.foreach_set(board)
    board_image.filepath_raw = str(output_path)
    board_image.file_format = "PNG"
    board_image.save()
    bpy.data.images.remove(board_image)


def add_metadata_to_objects(objects: list[bpy.types.Object]) -> None:
    add_asset_metadata(
        ASSET_NAME,
        "complete 360 game-ready candidate pending Flamestrike aesthetic review",
        UNREAL_PATH,
    )
    for obj in objects:
        obj["Aerathea.Asset"] = ASSET_NAME
        obj["Aerathea.UnrealPath"] = UNREAL_PATH
        obj["Aerathea.AssetType"] = "Static Mesh"
        obj["Aerathea.Faction"] = "Blood Axe Giants"
        obj["Aerathea.Status"] = "complete_360_game_ready_candidate_pending_flamestrike_review"
        obj["Aerathea.SourceMethod"] = "hand_authored_360_dcc_from_approved_a1_concept_direction"
        obj["Aerathea.Collision"] = "UCX broad hull plus Unreal simple collision validation"


def main() -> None:
    clear_scene()
    setup_scene()
    texture_paths = generate_textures()
    materials = make_materials(texture_paths)

    lod0_collection = make_collection(f"{ASSET_NAME}_LOD0")
    lod1_collection = make_collection(f"{ASSET_NAME}_LOD1", hidden=True)
    lod2_collection = make_collection(f"{ASSET_NAME}_LOD2", hidden=True)
    lod3_collection = make_collection(f"{ASSET_NAME}_LOD3", hidden=True)
    collision_collection = make_collection(f"{ASSET_NAME}_Collision", hidden=True)

    lod0_objects = build_asset_lod(lod0_collection, materials, 0)
    lod1_objects = build_asset_lod(lod1_collection, materials, 1)
    lod2_objects = build_asset_lod(lod2_collection, materials, 2)
    lod3_objects = build_asset_lod(lod3_collection, materials, 3)
    collision = add_collision_proxy(collision_collection, materials["stone"])
    add_metadata_to_objects(lod0_objects + lod1_objects + lod2_objects + lod3_objects + [collision])

    export_dir = EXPORT_ROOT / REL_PATH
    export_objects(lod0_objects + [collision], export_dir / f"{ASSET_NAME}.fbx")
    export_objects(lod0_objects, export_dir / f"{ASSET_NAME}_LOD0.fbx")
    export_objects(lod1_objects, export_dir / f"{ASSET_NAME}_LOD1.fbx")
    export_objects(lod2_objects, export_dir / f"{ASSET_NAME}_LOD2.fbx")
    export_objects(lod3_objects, export_dir / f"{ASSET_NAME}_LOD3.fbx")

    camera, target = configure_review_scene()
    render_paths = [
        REVIEW_ROOT / f"{ASSET_NAME}_FrontReview.png",
        REVIEW_ROOT / f"{ASSET_NAME}_ThreeQuarterReview.png",
        REVIEW_ROOT / f"{ASSET_NAME}_SideReview.png",
        REVIEW_ROOT / f"{ASSET_NAME}_BackReview.png",
    ]
    view_locations = [
        (0, -520, 175),
        (330, -430, 225),
        (520, -20, 205),
        (155, 490, 215),
    ]
    for path, location in zip(render_paths, view_locations):
        render_view(camera, target, location, path, (960, 540))
    compose_review_board(render_paths, REVIEW_ROOT / f"{ASSET_NAME}_CompleteTurntableReview.png", 960, 540)

    blend_path = BLENDER_ROOT / REL_PATH / f"{ASSET_NAME}.blend"
    ensure_dir(blend_path.parent)
    bpy.ops.wm.save_as_mainfile(filepath=str(blend_path))

    print(
        "Built {}: LOD0 {} tris, LOD1 {} tris, LOD2 {} tris, LOD3 {} tris. Exports: {}".format(
            ASSET_NAME,
            object_triangles(lod0_objects),
            object_triangles(lod1_objects),
            object_triangles(lod2_objects),
            object_triangles(lod3_objects),
            export_dir,
        )
    )


if __name__ == "__main__":
    main()
