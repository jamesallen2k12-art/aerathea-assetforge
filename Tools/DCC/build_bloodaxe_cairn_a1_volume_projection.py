#!/usr/bin/env python3
"""Build the A1 Blood Axe cairn as real volume with source-projected paint.

Run with:
    blender --background --python Tools/DCC/build_bloodaxe_cairn_a1_volume_projection.py

This pass avoids the failed relief/card construction. It starts from the
turnaround rebuild's real stone volumes, removes blockout paint decals, and
projects the approved A1 concept image onto front/top-facing stone surfaces.
"""

from __future__ import annotations

import shutil
import sys
from pathlib import Path

import bpy
from mathutils import Vector
from PIL import Image, ImageDraw, ImageFont


ROOT = Path(__file__).resolve().parents[2]
SOURCE_ROOT = ROOT / "SourceAssets"
BLENDER_ROOT = SOURCE_ROOT / "Blender"
EXPORT_ROOT = SOURCE_ROOT / "Exports"
TEXTURE_ROOT = SOURCE_ROOT / "Textures"

ASSET_NAME = "SM_GIA_BloodAxeCairnSlabCluster_A01_VolumeProjection"
REL_PATH = f"Props/Giants/BloodAxe/Cairns/{ASSET_NAME}"
UNREAL_PATH = f"/Game/Aerathea/Props/Giants/BloodAxe/Cairns/{ASSET_NAME}"
REVIEW_ROOT = ROOT / "Saved" / "Automation" / "DCC" / ASSET_NAME
TEXTURE_DIR = TEXTURE_ROOT / REL_PATH

REFERENCE_IMAGE = ROOT / "docs/assets/visual_canon/VC_GIA_BloodAxe_CairnStones_A01_A1_Crop.png"
SOURCE_SIDE_TEXTURE_DIR = TEXTURE_ROOT / "Props/Giants/BloodAxe/Cairns/SM_GIA_BloodAxeCairnSlabCluster_A01_HybridProjection"

FRONT_RENDER = REVIEW_ROOT / f"{ASSET_NAME}_FrontReview.png"
THREE_QUARTER_RENDER = REVIEW_ROOT / f"{ASSET_NAME}_ThreeQuarterReview.png"
SIDE_RENDER = REVIEW_ROOT / f"{ASSET_NAME}_SideReview.png"
BACK_RENDER = REVIEW_ROOT / f"{ASSET_NAME}_BackReview.png"
BOARD_RENDER = REVIEW_ROOT / f"{ASSET_NAME}_ConceptToVolumeReviewBoard.png"

IMAGE_WIDTH = 360.0
IMAGE_HEIGHT = 430.0
GROUND_PX_Y = 340.0
Z_SCALE = 154.0 / (340.0 - 82.0)
PROJECT_CAMERA_DIR = Vector((0.48, -0.82, 0.30)).normalized()

sys.path.insert(0, str(ROOT))

from Tools.DCC.build_next_slice_assets import add_asset_metadata, clear_scene, setup_scene  # noqa: E402
from Tools.DCC import build_bloodaxe_cairn_a1_turnaround_rebuild as turnaround  # noqa: E402


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


def make_texture_sources() -> dict[str, Path]:
    TEXTURE_DIR.mkdir(parents=True, exist_ok=True)
    front = TEXTURE_DIR / "T_GIA_BloodAxeCairnSlabCluster_A01_VolumeProjection_BC.png"
    side = TEXTURE_DIR / "T_GIA_BloodAxeCairnSlabCluster_A01_VolumeProjectionSide_BC.png"
    normal = TEXTURE_DIR / "T_GIA_BloodAxeCairnSlabCluster_A01_VolumeProjectionSide_N.png"
    shutil.copyfile(REFERENCE_IMAGE, front)
    source_side = SOURCE_SIDE_TEXTURE_DIR / "T_GIA_BloodAxeCairnSlabCluster_A01_HybridStoneSide_BC.png"
    source_normal = SOURCE_SIDE_TEXTURE_DIR / "T_GIA_BloodAxeCairnSlabCluster_A01_HybridStoneSide_N.png"
    if source_side.exists():
        shutil.copyfile(source_side, side)
    else:
        Image.new("RGBA", (512, 512), (70, 68, 58, 255)).save(side)
    if source_normal.exists():
        shutil.copyfile(source_normal, normal)
    else:
        Image.new("RGBA", (512, 512), (128, 128, 255, 255)).save(normal)
    return {"front": front, "side": side, "normal": normal}


def make_texture_material(name: str, texture_path: Path, normal_path: Path | None = None, roughness: float = 0.9) -> bpy.types.Material:
    material = bpy.data.materials.new(name)
    material.diffuse_color = (1.0, 1.0, 1.0, 1.0)
    material.use_nodes = True
    nodes = material.node_tree.nodes
    bsdf = nodes.get("Principled BSDF")
    if bsdf is None:
        return material
    texture = nodes.new(type="ShaderNodeTexImage")
    texture.image = bpy.data.images.load(str(texture_path))
    texture.extension = "CLIP"
    material.node_tree.links.new(texture.outputs["Color"], bsdf.inputs["Base Color"])
    bsdf.inputs["Roughness"].default_value = roughness
    if "Emission Color" in bsdf.inputs and "Emission Strength" in bsdf.inputs and "A1Front" in name:
        material.node_tree.links.new(texture.outputs["Color"], bsdf.inputs["Emission Color"])
        bsdf.inputs["Emission Strength"].default_value = 0.10
    if normal_path is not None and normal_path.exists():
        normal = nodes.new(type="ShaderNodeTexImage")
        normal.image = bpy.data.images.load(str(normal_path))
        normal.image.colorspace_settings.name = "Non-Color"
        normal_map = nodes.new(type="ShaderNodeNormalMap")
        normal_map.inputs["Strength"].default_value = 0.34
        material.node_tree.links.new(normal.outputs["Color"], normal_map.inputs["Color"])
        material.node_tree.links.new(normal_map.outputs["Normal"], bsdf.inputs["Normal"])
    return material


def make_flat_material(name: str, color: tuple[float, float, float, float], roughness: float = 0.9) -> bpy.types.Material:
    material = bpy.data.materials.new(name)
    material.diffuse_color = color
    material.use_nodes = True
    bsdf = material.node_tree.nodes.get("Principled BSDF")
    if bsdf is not None:
        bsdf.inputs["Base Color"].default_value = color
        bsdf.inputs["Roughness"].default_value = roughness
        bsdf.inputs["Metallic"].default_value = 0.0
    return material


def world_to_projection_uv(point: Vector) -> tuple[float, float]:
    px = point.x + 180.0
    py = GROUND_PX_Y - point.z / Z_SCALE
    return max(0.0, min(1.0, px / IMAGE_WIDTH)), max(0.0, min(1.0, 1.0 - py / IMAGE_HEIGHT))


def remove_blockout_decals(objects: list[bpy.types.Object]) -> list[bpy.types.Object]:
    rejected_tokens = (
        "MainPaint",
        "PaintSlash",
        "Highlight",
        "DarkCrack",
        "StoneCrack",
        "FaceWarm",
        "FaceDark",
        "Cord",
        "Lashing",
        "EdgeTie",
        "Bind",
    )
    kept: list[bpy.types.Object] = []
    for obj in objects:
        if any(token in obj.name for token in rejected_tokens):
            bpy.data.objects.remove(obj, do_unlink=True)
        else:
            kept.append(obj)
    return kept


def apply_art_match_transforms(objects: list[bpy.types.Object], detail: int) -> None:
    if detail > 1:
        return
    for obj in objects:
        name = obj.name
        if "RightRawhideUpright" in name:
            obj.scale.x *= 0.72
            obj.scale.y *= 0.82
            obj.scale.z *= 0.78
            obj.location.x += 6.0
            obj.location.y -= 4.0
            obj.location.z -= 8.0
        elif "RearTallBrokenSlab" in name:
            obj.scale.x *= 0.80
            obj.scale.y *= 0.84
            obj.scale.z *= 0.82
            obj.location.x -= 8.0
            obj.location.y += 2.0
            obj.location.z -= 8.0
        elif "LeftRearShard" in name or "CenterNarrowShard" in name:
            obj.scale.x *= 0.82
            obj.scale.y *= 0.86
            obj.scale.z *= 0.88
            obj.location.z -= 4.0
        elif "AshMudBase" in name:
            obj.scale.x *= 0.88
            obj.scale.y *= 0.80
        elif "RightSupportStone" in name:
            obj.scale.x *= 0.82
            obj.scale.y *= 0.86
            obj.location.x += 3.0
        elif "MainFallenPaintedSlab" in name:
            obj.location.z -= 2.5
            obj.scale.y *= 0.92


def is_projectable_stone(obj: bpy.types.Object) -> bool:
    if obj.type != "MESH":
        return False
    name = obj.name
    if "Cord" in name or "Lashing" in name or "EdgeTie" in name or "Bind" in name:
        return False
    if "AshMudBase" in name or "MudClump" in name:
        return False
    if "Pebble" in name:
        return False
    return "A1_Turnaround" in name or "Stone" in name or "Slab" in name


def apply_projected_materials(
    objects: list[bpy.types.Object],
    front_material: bpy.types.Material,
    side_material: bpy.types.Material,
    pebble_material: bpy.types.Material,
    earth_material: bpy.types.Material,
) -> None:
    for obj in objects:
        if obj.type != "MESH":
            continue
        if "AshMudBase" in obj.name or "MudClump" in obj.name:
            obj.data.materials.clear()
            obj.data.materials.append(earth_material)
            continue
        if "Pebble" in obj.name:
            obj.data.materials.clear()
            obj.data.materials.append(pebble_material)
            continue
        if not is_projectable_stone(obj):
            continue

        obj.data.materials.clear()
        obj.data.materials.append(front_material)
        obj.data.materials.append(side_material)
        uv_layer = obj.data.uv_layers.new(name="AET_A1VolumeProjectionUV")
        normal_matrix = obj.matrix_world.to_3x3()
        for polygon in obj.data.polygons:
            world_normal = (normal_matrix @ polygon.normal).normalized()
            visible_from_a1 = world_normal.dot(PROJECT_CAMERA_DIR) > 0.08 or world_normal.z > 0.42
            polygon.material_index = 0 if visible_from_a1 else 1
            for loop_index in polygon.loop_indices:
                vertex_index = obj.data.loops[loop_index].vertex_index
                world_point = obj.matrix_world @ obj.data.vertices[vertex_index].co
                if visible_from_a1:
                    uv_layer.data[loop_index].uv = world_to_projection_uv(world_point)
                else:
                    uv_layer.data[loop_index].uv = (0.18 + (loop_index % 3) * 0.31, 0.22 + (loop_index % 2) * 0.46)


def add_collision_proxy(material: bpy.types.Material, collection: bpy.types.Collection) -> bpy.types.Object:
    bpy.ops.mesh.primitive_cube_add(size=1.0, location=(0.0, -2.0, 67.0))
    obj = bpy.context.object
    obj.name = f"UCX_{ASSET_NAME}_00"
    obj.dimensions = (365.0, 215.0, 164.0)
    obj.data.materials.append(material)
    set_active(obj)
    bpy.ops.object.transform_apply(location=False, rotation=False, scale=True)
    obj.display_type = "WIRE"
    obj.hide_render = True
    link_to_collection(obj, collection)
    return obj


def object_triangle_count(obj: bpy.types.Object) -> int:
    if getattr(obj, "type", None) != "MESH":
        return 0
    obj.data.calc_loop_triangles()
    return len(obj.data.loop_triangles)


def collection_triangle_count(collection: bpy.types.Collection) -> int:
    return sum(object_triangle_count(obj) for obj in collection.objects)


def collection_bounds(collection: bpy.types.Collection) -> tuple[float, float, float]:
    points: list[Vector] = []
    for obj in collection.objects:
        if getattr(obj, "type", None) != "MESH":
            continue
        points.extend(obj.matrix_world @ Vector(corner) for corner in obj.bound_box)
    if not points:
        return 0.0, 0.0, 0.0
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
        for collection in obj.users_collection:
            collection.hide_viewport = False
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
    scene.view_settings.exposure = 0.92
    scene.view_settings.gamma = 1.0
    if scene.world is not None:
        scene.world.color = (0.56, 0.55, 0.52)
    lights = [
        ("AET_VolumeProjection_Key", "AREA", (-290.0, -380.0, 430.0), 6800.0, 520.0),
        ("AET_VolumeProjection_Fill", "AREA", (280.0, -210.0, 220.0), 2600.0, 620.0),
        ("AET_VolumeProjection_Rim", "POINT", (0.0, 260.0, 210.0), 700.0, 0.0),
        ("AET_VolumeProjection_Top", "AREA", (0.0, 0.0, 540.0), 2200.0, 700.0),
    ]
    for name, kind, location, energy, size in lights:
        data = bpy.data.lights.new(name, type=kind)
        data.energy = energy
        if kind == "AREA":
            data.size = size
        obj = bpy.data.objects.new(name, data)
        obj.location = location
        bpy.context.scene.collection.objects.link(obj)


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
    scene.render.resolution_y = 900
    views = [
        (FRONT_RENDER, "AET_VolumeProjection_FrontCamera", (330.0, -560.0, 210.0), (0.0, 0.0, 60.0), 365.0),
        (THREE_QUARTER_RENDER, "AET_VolumeProjection_ThreeQuarterCamera", (360.0, -520.0, 250.0), (0.0, -4.0, 64.0), 390.0),
        (SIDE_RENDER, "AET_VolumeProjection_SideCamera", (560.0, 0.0, 210.0), (0.0, 0.0, 62.0), 365.0),
        (BACK_RENDER, "AET_VolumeProjection_BackCamera", (-330.0, 560.0, 210.0), (0.0, 0.0, 62.0), 365.0),
    ]
    for path, name, location, target, scale in views:
        set_camera(name, location, target, scale)
        scene.render.filepath = str(path)
        bpy.ops.render.render(write_still=True)


def font(size: int) -> ImageFont.ImageFont:
    candidates = [
        "/usr/share/fonts/dejavu-sans-fonts/DejaVuSans.ttf",
        "/usr/share/fonts/dejavu/DejaVuSans.ttf",
    ]
    for path in candidates:
        if Path(path).exists():
            return ImageFont.truetype(path, size)
    return ImageFont.load_default()


def build_review_board() -> None:
    board = Image.new("RGBA", (2200, 1320), (236, 233, 226, 255))
    draw = ImageDraw.Draw(board)
    title_font = font(34)
    body_font = font(22)
    draw.text((54, 34), "A1 real-volume projection rebuild", fill=(28, 25, 22, 255), font=title_font)
    draw.text(
        (54, 82),
        "Real stone volumes first; A1 concept art projected onto front/top surfaces; side/back use inferred stone material.",
        fill=(58, 52, 45, 255),
        font=body_font,
    )
    images = [
        ("Source A1", REFERENCE_IMAGE, (70, 160), (340, 406)),
        ("Front projected volume", FRONT_RENDER, (480, 150), (500, 375)),
        ("3/4 volume", THREE_QUARTER_RENDER, (1030, 150), (500, 375)),
        ("Side", SIDE_RENDER, (480, 650), (500, 375)),
        ("Back", BACK_RENDER, (1030, 650), (500, 375)),
    ]
    for label, path, location, max_size in images:
        image = Image.open(path).convert("RGBA")
        image.thumbnail(max_size, Image.Resampling.LANCZOS)
        board.alpha_composite(image, location)
        draw.text((location[0], location[1] + max_size[1] + 16), label, fill=(42, 37, 32, 255), font=body_font)
    board.save(BOARD_RENDER)


def build_lod(
    collection: bpy.types.Collection,
    detail: int,
    front_material: bpy.types.Material,
    side_material: bpy.types.Material,
    pebble_material: bpy.types.Material,
    earth_material: bpy.types.Material,
) -> list[bpy.types.Object]:
    source_materials = turnaround.make_materials()
    objects = turnaround.build_asset_collection(collection, source_materials, detail)
    objects = remove_blockout_decals(objects)
    apply_art_match_transforms(objects, detail)
    apply_projected_materials(objects, front_material, side_material, pebble_material, earth_material)
    return objects


def build() -> None:
    clear_scene()
    setup_scene()
    add_review_lighting()
    texture_paths = make_texture_sources()

    front_material = make_texture_material("M_GIA_BloodAxeCairn_VolumeProjection_A1Front_A01", texture_paths["front"], roughness=0.86)
    side_material = make_texture_material("M_GIA_BloodAxeCairn_VolumeProjection_SideStone_A01", texture_paths["side"], texture_paths["normal"], 0.91)
    pebble_material = make_texture_material("M_GIA_BloodAxeCairn_VolumeProjection_PebbleStone_A01", texture_paths["side"], texture_paths["normal"], 0.92)
    earth_material = make_flat_material("M_GIA_BloodAxeCairn_VolumeProjection_AshMud_A01", (0.13, 0.085, 0.048, 1.0), 0.96)
    rawhide_material = make_flat_material("M_GIA_BloodAxeCairn_VolumeProjection_Rawhide_A01", (0.42, 0.255, 0.095, 1.0), 0.86)
    collision_material = make_flat_material("M_AET_CollisionProxy_ReviewOnly_A01", (0.1, 0.42, 0.95, 0.22))

    lod0_collection = make_collection(f"{ASSET_NAME}_LOD0_VolumeProjection")
    lod1_collection = make_collection(f"{ASSET_NAME}_LOD1_VolumeProjection", hidden=True)
    lod2_collection = make_collection(f"{ASSET_NAME}_LOD2_VolumeProjection", hidden=True)
    lod3_collection = make_collection(f"{ASSET_NAME}_LOD3_VolumeProjection", hidden=True)
    collision_collection = make_collection(f"{ASSET_NAME}_Collision_Source", hidden=True)

    lod0_objects = build_lod(lod0_collection, 0, front_material, side_material, pebble_material, earth_material)
    lod1_objects = build_lod(lod1_collection, 1, front_material, side_material, pebble_material, earth_material)
    lod2_objects = build_lod(lod2_collection, 2, front_material, side_material, pebble_material, earth_material)
    lod3_objects = build_lod(lod3_collection, 3, front_material, side_material, pebble_material, earth_material)
    rawhide_tokens = ("Cord", "Lashing", "EdgeTie", "Bind")
    for obj in lod0_objects + lod1_objects:
        if obj.type == "MESH" and any(token in obj.name for token in rawhide_tokens):
            obj.data.materials.clear()
            obj.data.materials.append(rawhide_material)
    collision = add_collision_proxy(collision_material, collision_collection)

    add_asset_metadata(
        ASSET_NAME,
        "A1 Blood Axe cairn real-volume projection candidate. Uses turnaround geometry with A1 source art projected onto visible stone surfaces; replaces failed billboard/relief approach.",
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
    print(f"Rendered {BOARD_RENDER.relative_to(ROOT)}")
    print(f"LOD0 tris: {collection_triangle_count(lod0_collection)}")
    print(f"LOD1 tris: {collection_triangle_count(lod1_collection)}")
    print(f"LOD2 tris: {collection_triangle_count(lod2_collection)}")
    print(f"LOD3 tris: {collection_triangle_count(lod3_collection)}")
    print(f"LOD0 bounds: {width:.2f}w x {depth:.2f}d x {height:.2f}h cm")
    print("Collision proxies: 1")


if __name__ == "__main__":
    build()
