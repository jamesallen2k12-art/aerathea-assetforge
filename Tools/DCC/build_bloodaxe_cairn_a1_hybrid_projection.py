#!/usr/bin/env python3
"""Build a revised A1 Blood Axe cairn from projection plus real volume.

Run with:
    blender --background --python Tools/DCC/build_bloodaxe_cairn_a1_hybrid_projection.py

This is the correction after the rejected procedural-complete pass:
- keep the A1 source projection on the front faces for art fidelity
- shrink and facet the backs so the asset no longer reads as flat cards
- add real side/back stone volume, rubble, and rawhide geometry
- render review views before any Unreal approval/import decision
"""

from __future__ import annotations

import math
import shutil
import sys
from array import array
from pathlib import Path

import bpy
from mathutils import Vector
from mathutils.geometry import tessellate_polygon
from PIL import Image, ImageDraw, ImageFont


ROOT = Path(__file__).resolve().parents[2]
SOURCE_ROOT = ROOT / "SourceAssets"
BLENDER_ROOT = SOURCE_ROOT / "Blender"
EXPORT_ROOT = SOURCE_ROOT / "Exports"
TEXTURE_ROOT = SOURCE_ROOT / "Textures"

ASSET_NAME = "SM_GIA_BloodAxeCairnSlabCluster_A01_HybridProjection"
REL_PATH = f"Props/Giants/BloodAxe/Cairns/{ASSET_NAME}"
UNREAL_PATH = f"/Game/Aerathea/Props/Giants/BloodAxe/Cairns/{ASSET_NAME}"
REVIEW_ROOT = ROOT / "Saved" / "Automation" / "DCC" / ASSET_NAME
TEXTURE_DIR = TEXTURE_ROOT / REL_PATH

REFERENCE_IMAGE = ROOT / "docs/assets/visual_canon/VC_GIA_BloodAxe_CairnStones_A01_A1_Crop.png"

FRONT_AB_RENDER = REVIEW_ROOT / f"{ASSET_NAME}_FrontABReview.png"
FRONT_RENDER = REVIEW_ROOT / f"{ASSET_NAME}_FrontOnlyReview.png"
THREE_QUARTER_RENDER = REVIEW_ROOT / f"{ASSET_NAME}_ThreeQuarterReview.png"
SIDE_RENDER = REVIEW_ROOT / f"{ASSET_NAME}_SideReview.png"
BACK_RENDER = REVIEW_ROOT / f"{ASSET_NAME}_BackReview.png"
BOARD_RENDER = REVIEW_ROOT / f"{ASSET_NAME}_ProjectionVolumeReviewBoard.png"

IMAGE_WIDTH = 360
IMAGE_HEIGHT = 430
IMAGE_CENTER_X = 180.0
GROUND_PX_Y = 340.0
TOP_PX_Y = 82.0
Z_SCALE = 154.0 / (GROUND_PX_Y - TOP_PX_Y)

sys.path.insert(0, str(ROOT))

from Tools.DCC.build_next_slice_assets import add_asset_metadata, clear_scene, setup_scene  # noqa: E402
from Tools.DCC import build_bloodaxe_cairn_a1_game_ready as a1_base  # noqa: E402


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


def clamp(value: float) -> float:
    return max(0.0, min(1.0, value))


def pixel_to_world(px: float, py: float, x_offset: float = 0.0) -> tuple[float, float]:
    x = (px - IMAGE_CENTER_X) + x_offset
    z = (GROUND_PX_Y - py) * Z_SCALE
    return x, z


def image_uv(px: float, py: float) -> tuple[float, float]:
    return px / IMAGE_WIDTH, 1.0 - py / IMAGE_HEIGHT


def procedural_noise(x: int, y: int, seed: int) -> float:
    value = (x * 374761393 + y * 668265263 + seed * 982451653) & 0xFFFFFFFF
    value = (value ^ (value >> 13)) * 1274126177 & 0xFFFFFFFF
    return ((value ^ (value >> 16)) & 0xFFFF) / 65535.0


def save_texture(path: Path, width: int, height: int, pixels: array) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    image = bpy.data.images.new(path.stem, width=width, height=height, alpha=True, float_buffer=False)
    image.pixels.foreach_set(pixels)
    image.filepath_raw = str(path)
    image.file_format = "PNG"
    image.save()
    bpy.data.images.remove(image)


def make_texture_sources() -> dict[str, Path]:
    TEXTURE_DIR.mkdir(parents=True, exist_ok=True)
    front_bc = TEXTURE_DIR / "T_GIA_BloodAxeCairnSlabCluster_A01_HybridProjection_BC.png"
    side_bc = TEXTURE_DIR / "T_GIA_BloodAxeCairnSlabCluster_A01_HybridStoneSide_BC.png"
    side_n = TEXTURE_DIR / "T_GIA_BloodAxeCairnSlabCluster_A01_HybridStoneSide_N.png"
    side_orm = TEXTURE_DIR / "T_GIA_BloodAxeCairnSlabCluster_A01_HybridStoneSide_ORM.png"
    shutil.copyfile(REFERENCE_IMAGE, front_bc)

    width = 1024
    height = 1024
    bc = array("f")
    normal = array("f")
    orm = array("f")
    for y in range(height):
        v = y / (height - 1)
        for x in range(width):
            u = x / (width - 1)
            n1 = procedural_noise(x, y, 941)
            n2 = procedural_noise(x // 5, y // 5, 1447)
            n3 = procedural_noise(x // 17, y // 17, 811)
            if v < 0.18:
                base = (
                    0.16 + n1 * 0.08,
                    0.105 + n2 * 0.055,
                    0.060 + n3 * 0.035,
                )
                roughness = 0.96
                occlusion = 0.52 + n1 * 0.22
            else:
                warm_edge = 0.045 if n3 > 0.72 else 0.0
                base = (
                    0.245 + n1 * 0.135 + warm_edge,
                    0.235 + n2 * 0.115 + warm_edge * 0.7,
                    0.205 + n1 * 0.090,
                )
                roughness = 0.90 + n2 * 0.08
                occlusion = 0.50 + n1 * 0.26
            bc.extend((clamp(base[0]), clamp(base[1]), clamp(base[2]), 1.0))
            height_value = (n1 - 0.5) * 0.16 + (n2 - 0.5) * 0.06
            normal.extend((clamp(0.5 + height_value), clamp(0.5 + (n3 - 0.5) * 0.12), 1.0, 1.0))
            orm.extend((clamp(occlusion), clamp(roughness), 0.0, 1.0))
    save_texture(side_bc, width, height, bc)
    save_texture(side_n, width, height, normal)
    save_texture(side_orm, width, height, orm)
    return {"front_bc": front_bc, "side_bc": side_bc, "side_n": side_n, "side_orm": side_orm}


def make_texture_material(
    name: str,
    bc_path: Path,
    normal_path: Path | None = None,
    roughness: float = 0.9,
) -> bpy.types.Material:
    material = bpy.data.materials.new(name)
    material.diffuse_color = (1.0, 1.0, 1.0, 1.0)
    material.use_nodes = True
    nodes = material.node_tree.nodes
    bsdf = nodes.get("Principled BSDF")
    if bsdf is None:
        return material
    texture = nodes.new(type="ShaderNodeTexImage")
    texture.image = bpy.data.images.load(str(bc_path))
    texture.extension = "CLIP"
    material.node_tree.links.new(texture.outputs["Color"], bsdf.inputs["Base Color"])
    bsdf.inputs["Roughness"].default_value = roughness
    bsdf.inputs["Metallic"].default_value = 0.0
    if normal_path is not None and normal_path.exists():
        normal_texture = nodes.new(type="ShaderNodeTexImage")
        normal_texture.image = bpy.data.images.load(str(normal_path))
        normal_texture.image.colorspace_settings.name = "Non-Color"
        normal_map = nodes.new(type="ShaderNodeNormalMap")
        normal_map.inputs["Strength"].default_value = 0.35
        material.node_tree.links.new(normal_texture.outputs["Color"], normal_map.inputs["Color"])
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


def make_reference_material(name: str) -> bpy.types.Material:
    material = bpy.data.materials.new(name)
    material.use_nodes = True
    nodes = material.node_tree.nodes
    nodes.clear()
    texture = nodes.new(type="ShaderNodeTexImage")
    texture.image = bpy.data.images.load(str(REFERENCE_IMAGE))
    emission = nodes.new(type="ShaderNodeEmission")
    output = nodes.new(type="ShaderNodeOutputMaterial")
    material.node_tree.links.new(texture.outputs["Color"], emission.inputs["Color"])
    material.node_tree.links.new(emission.outputs["Emission"], output.inputs["Surface"])
    return material


def simplify_polygon(points: list[tuple[float, float]], stride: int) -> list[tuple[float, float]]:
    if stride <= 1 or len(points) <= 6:
        return points
    simplified = [point for index, point in enumerate(points) if index % stride == 0]
    return simplified if len(simplified) >= 4 else points


def scaled_polygon(points: list[tuple[float, float]], scale: float) -> list[tuple[float, float]]:
    center_x = sum(px for px, _py in points) / len(points)
    center_y = sum(py for _px, py in points) / len(points)
    return [(center_x + (px - center_x) * scale, center_y + (py - center_y) * scale) for px, py in points]


def add_sculpted_shell(
    name: str,
    polygon_px: list[tuple[float, float]],
    front_y: float,
    thickness: float,
    materials: list[bpy.types.Material],
    collection: bpy.types.Collection,
    side_material_index: int,
    scale: float = 1.0,
) -> bpy.types.Object:
    points = scaled_polygon(polygon_px, scale)
    center_x = sum(px for px, _py in points) / len(points)
    center_y = sum(py for _px, py in points) / len(points)
    if side_material_index == 2:
        back_scale = 0.92
        back_drop = 2.0
        shell_depth = min(thickness, 12.0)
        bevel_width = 0.35
    elif side_material_index == 3:
        back_scale = 0.72
        back_drop = 1.0
        shell_depth = min(thickness, 11.0)
        bevel_width = 0.45
    else:
        back_scale = 0.62
        back_drop = 3.8
        shell_depth = max(12.0, min(thickness, 21.0))
        bevel_width = 0.75

    verts: list[tuple[float, float, float]] = []
    front_uvs: list[tuple[float, float]] = []
    for px, py in points:
        x, z = pixel_to_world(px, py)
        verts.append((x, front_y, z))
        front_uvs.append(image_uv(px, py))
    for index, (px, py) in enumerate(points):
        radial = 0.97 + ((index % 3) - 1) * 0.035
        back_px = center_x + (px - center_x) * back_scale * radial
        back_py = center_y + (py - center_y) * back_scale
        x, z = pixel_to_world(back_px, back_py)
        verts.append((x, front_y + shell_depth, z - back_drop))

    count = len(points)
    polygon_for_tess = [[Vector((verts[index][0], verts[index][2], 0.0)) for index in range(count)]]
    triangles = tessellate_polygon(polygon_for_tess)

    faces: list[tuple[int, ...]] = []
    material_indices: list[int] = []
    for tri in triangles:
        faces.append(tuple(tri))
        material_indices.append(0)
    for tri in triangles:
        faces.append(tuple(count + index for index in reversed(tri)))
        material_indices.append(side_material_index)
    for index in range(count):
        next_index = (index + 1) % count
        faces.append((index, next_index, count + next_index, count + index))
        material_indices.append(side_material_index)

    mesh = bpy.data.meshes.new(f"{name}_Mesh")
    mesh.from_pydata(verts, [], faces)
    mesh.update()
    uv_layer = mesh.uv_layers.new(name="AET_A1HybridProjectionUV")
    for polygon, material_index in zip(mesh.polygons, material_indices):
        polygon.material_index = material_index
        for local_index, loop_index in enumerate(polygon.loop_indices):
            vertex_index = mesh.loops[loop_index].vertex_index
            if material_index == 0:
                uv_layer.data[loop_index].uv = front_uvs[vertex_index % count]
            else:
                uv_layer.data[loop_index].uv = ((local_index % 2) * 0.55, 0.18 + (local_index // 2) * 0.48)

    obj = bpy.data.objects.new(name, mesh)
    for material in materials:
        obj.data.materials.append(material)
    collection.objects.link(obj)

    if bevel_width > 0.0:
        bevel = obj.modifiers.new("AET_HybridBrokenEdgeSoftening", "BEVEL")
        bevel.width = bevel_width
        bevel.segments = 1
        try:
            bevel.affect = "EDGES"
        except TypeError:
            pass
        set_active(obj)
        bpy.ops.object.modifier_apply(modifier=bevel.name)
    normal = obj.modifiers.new("AET_HybridWeightedNormals", "WEIGHTED_NORMAL")
    set_active(obj)
    bpy.ops.object.modifier_apply(modifier=normal.name)
    return obj


def build_lod_collection(
    collection: bpy.types.Collection,
    materials: list[bpy.types.Material],
    stride: int,
    scale: float,
    max_shells: int | None = None,
) -> list[bpy.types.Object]:
    objects: list[bpy.types.Object] = []
    specs = a1_base.shell_specs()
    if max_shells is not None:
        specs = specs[:max_shells]
    for spec in specs:
        points = simplify_polygon(spec["points"], stride)  # type: ignore[arg-type]
        objects.append(
            add_sculpted_shell(
                f"{collection.name}_{spec['name']}",
                points,
                float(spec["y"]),
                float(spec["depth"]),
                materials,
                collection,
                int(spec["side"]),
                scale=scale * float(spec.get("scale", 1.0)),
            )
        )
    return objects


def add_irregular_rock(
    name: str,
    location: tuple[float, float, float],
    size: tuple[float, float, float],
    rotation: tuple[float, float, float],
    material: bpy.types.Material,
    collection: bpy.types.Collection,
    bevel_width: float = 0.8,
) -> bpy.types.Object:
    bpy.ops.mesh.primitive_cube_add(size=1.0, location=location, rotation=rotation)
    obj = bpy.context.object
    obj.name = name
    obj.dimensions = size
    obj.data.materials.append(material)
    set_active(obj)
    bpy.ops.object.transform_apply(location=False, rotation=False, scale=True)
    if bevel_width > 0:
        bevel = obj.modifiers.new("AET_HybridRubbleBrokenEdges", "BEVEL")
        bevel.width = bevel_width
        bevel.segments = 1
        set_active(obj)
        bpy.ops.object.modifier_apply(modifier=bevel.name)
    normal = obj.modifiers.new("AET_HybridRubbleWeightedNormals", "WEIGHTED_NORMAL")
    set_active(obj)
    bpy.ops.object.modifier_apply(modifier=normal.name)
    link_to_collection(obj, collection)
    return obj


def add_cylinder_between(
    name: str,
    start: tuple[float, float, float],
    end: tuple[float, float, float],
    radius: float,
    material: bpy.types.Material,
    collection: bpy.types.Collection,
    vertices: int = 8,
) -> bpy.types.Object:
    start_vec = Vector(start)
    end_vec = Vector(end)
    direction = end_vec - start_vec
    length = direction.length
    midpoint = start_vec + direction * 0.5
    bpy.ops.mesh.primitive_cylinder_add(vertices=vertices, radius=radius, depth=length, location=midpoint)
    obj = bpy.context.object
    obj.name = name
    obj.rotation_euler = direction.to_track_quat("Z", "Y").to_euler()
    obj.data.materials.append(material)
    set_active(obj)
    bpy.ops.object.transform_apply(location=False, rotation=False, scale=True)
    link_to_collection(obj, collection)
    return obj


def add_physical_details(
    collection: bpy.types.Collection,
    stone_material: bpy.types.Material,
    earth_material: bpy.types.Material,
    rawhide_material: bpy.types.Material,
    lod_level: int,
) -> list[bpy.types.Object]:
    objects: list[bpy.types.Object] = []
    if lod_level <= 1:
        ropes = [
            ("Rawhide_LeftWrap_A", (-142.0, -31.0, 48.0), (-58.0, -26.0, 60.0), 1.8),
            ("Rawhide_LeftWrap_B", (-134.0, -37.0, 42.0), (-49.0, -32.0, 51.0), 1.55),
            ("Rawhide_MainSlabTie_A", (-72.0, -32.0, 68.0), (92.0, -22.0, 80.0), 1.45),
            ("Rawhide_RightUprightTie_A", (99.0, -10.0, 53.0), (151.0, 4.0, 64.0), 1.45),
        ]
        for name, start, end, radius in ropes:
            objects.append(add_cylinder_between(f"{collection.name}_{name}", start, end, radius, rawhide_material, collection))
    if lod_level == 0:
        rubble = [
            ("FrontPebble_A", (-118.0, -53.0, 8.0), (18.0, 11.0, 7.0), (0.1, 0.0, 0.25), stone_material),
            ("FrontPebble_B", (-69.0, -61.0, 10.0), (24.0, 14.0, 8.0), (0.0, 0.2, -0.3), stone_material),
            ("FrontPebble_C", (-4.0, -69.0, 7.0), (20.0, 12.0, 6.0), (0.2, 0.0, 0.5), stone_material),
            ("RightPebble_A", (145.0, -36.0, 12.0), (20.0, 14.0, 9.0), (-0.1, 0.1, 0.6), stone_material),
            ("BackRubble_A", (62.0, 37.0, 17.0), (34.0, 20.0, 13.0), (0.15, 0.25, -0.1), stone_material),
            ("LeftMudClump_A", (-154.0, -2.0, 6.0), (42.0, 23.0, 8.0), (0.0, 0.0, -0.45), earth_material),
            ("RightMudClump_A", (121.0, -59.0, 5.0), (36.0, 20.0, 7.0), (0.0, 0.0, 0.25), earth_material),
        ]
        for name, location, size, rotation, material in rubble:
            objects.append(add_irregular_rock(f"{collection.name}_{name}", location, size, rotation, material, collection))
    return objects


def add_collision_proxy(material: bpy.types.Material, collection: bpy.types.Collection) -> bpy.types.Object:
    bpy.ops.mesh.primitive_cube_add(size=1.0, location=(0.0, -6.0, 61.0), rotation=(0.0, 0.0, 0.0))
    obj = bpy.context.object
    obj.name = f"UCX_{ASSET_NAME}_00"
    obj.dimensions = (342.0, 64.0, 158.0)
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
        for current in obj.users_collection:
            current.hide_viewport = False
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


def add_reference_plate(material: bpy.types.Material, collection: bpy.types.Collection, x_offset: float) -> bpy.types.Object:
    top_left_x, top_left_z = pixel_to_world(0, 0, x_offset)
    bottom_right_x, bottom_right_z = pixel_to_world(IMAGE_WIDTH, IMAGE_HEIGHT, x_offset)
    y = 24.0
    verts = [
        (top_left_x, y, top_left_z),
        (top_left_x, y, bottom_right_z),
        (bottom_right_x, y, bottom_right_z),
        (bottom_right_x, y, top_left_z),
    ]
    mesh = bpy.data.meshes.new("HybridReview_A1ReferencePlate_Mesh")
    mesh.from_pydata(verts, [], [(0, 1, 2, 3)])
    mesh.update()
    uv_layer = mesh.uv_layers.new(name="AET_ReferenceUV")
    for loop_index, uv in zip(mesh.polygons[0].loop_indices, [(0, 1), (0, 0), (1, 0), (1, 1)]):
        uv_layer.data[loop_index].uv = uv
    obj = bpy.data.objects.new("HybridReview_A1ReferencePlate", mesh)
    obj.data.materials.append(material)
    collection.objects.link(obj)
    return obj


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
    scene.view_settings.exposure = 0.65
    scene.view_settings.gamma = 1.0
    if scene.world is not None:
        scene.world.color = (0.54, 0.53, 0.50)
    for name, kind, location, energy, size in [
        ("AET_Hybrid_Key", "AREA", (-260.0, -380.0, 420.0), 3200.0, 520.0),
        ("AET_Hybrid_Fill", "AREA", (260.0, -260.0, 210.0), 950.0, 620.0),
        ("AET_Hybrid_BackRim", "POINT", (-80.0, 230.0, 190.0), 280.0, 0.0),
    ]:
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


def render_reviews(reference_material: bpy.types.Material) -> None:
    REVIEW_ROOT.mkdir(parents=True, exist_ok=True)
    scene = bpy.context.scene
    scene.render.film_transparent = False

    review_collection = make_collection("HybridReview_A1_SourcePlate")
    add_reference_plate(reference_material, review_collection, -430.0)
    scene.render.resolution_x = 1600
    scene.render.resolution_y = 1000
    set_camera("AET_Hybrid_FrontABCamera", (-215.0, -720.0, 82.0), (-215.0, -7.0, 76.0), 820.0)
    scene.render.filepath = str(FRONT_AB_RENDER)
    bpy.ops.render.render(write_still=True)

    for obj in review_collection.objects:
        obj.hide_render = True

    scene.render.resolution_x = 1000
    scene.render.resolution_y = 1000
    set_camera("AET_Hybrid_FrontOnlyCamera", (0.0, -690.0, 82.0), (0.0, -7.0, 76.0), 290.0)
    scene.render.filepath = str(FRONT_RENDER)
    bpy.ops.render.render(write_still=True)

    set_camera("AET_Hybrid_ThreeQuarterCamera", (300.0, -520.0, 210.0), (0.0, -5.0, 72.0), 340.0)
    scene.render.filepath = str(THREE_QUARTER_RENDER)
    bpy.ops.render.render(write_still=True)

    set_camera("AET_Hybrid_SideCamera", (660.0, -65.0, 96.0), (0.0, -5.0, 70.0), 310.0)
    scene.render.filepath = str(SIDE_RENDER)
    bpy.ops.render.render(write_still=True)

    set_camera("AET_Hybrid_BackCamera", (10.0, 690.0, 98.0), (0.0, 0.0, 68.0), 320.0)
    scene.render.filepath = str(BACK_RENDER)
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
    board = Image.new("RGBA", (2400, 1500), (236, 233, 226, 255))
    draw = ImageDraw.Draw(board)
    title_font = font(34)
    body_font = font(22)
    draw.text((54, 34), "A1 hybrid projection + sculpted volume rebuild", fill=(28, 25, 22, 255), font=title_font)
    draw.text(
        (54, 82),
        "Goal: preserve the approved A1 front read while removing card-like side/back geometry.",
        fill=(58, 52, 45, 255),
        font=body_font,
    )

    source = Image.open(REFERENCE_IMAGE).convert("RGBA")
    front_ab = Image.open(FRONT_AB_RENDER).convert("RGBA")
    front = Image.open(FRONT_RENDER).convert("RGBA")
    three_quarter = Image.open(THREE_QUARTER_RENDER).convert("RGBA")
    side = Image.open(SIDE_RENDER).convert("RGBA")
    back = Image.open(BACK_RENDER).convert("RGBA")

    source.thumbnail((360, 430), Image.Resampling.LANCZOS)
    front_ab.thumbnail((1050, 656), Image.Resampling.LANCZOS)
    front.thumbnail((430, 430), Image.Resampling.LANCZOS)
    three_quarter.thumbnail((430, 430), Image.Resampling.LANCZOS)
    side.thumbnail((430, 430), Image.Resampling.LANCZOS)
    back.thumbnail((430, 430), Image.Resampling.LANCZOS)

    board.alpha_composite(source, (70, 165))
    board.alpha_composite(front_ab, (490, 140))
    board.alpha_composite(front, (60, 850))
    board.alpha_composite(three_quarter, (560, 850))
    board.alpha_composite(side, (1060, 850))
    board.alpha_composite(back, (1560, 850))

    draw.text((70, 615), "Source A1", fill=(42, 37, 32, 255), font=body_font)
    draw.text((490, 815), "A/B front match", fill=(42, 37, 32, 255), font=body_font)
    draw.text((60, 1290), "Front only", fill=(42, 37, 32, 255), font=body_font)
    draw.text((560, 1290), "3/4 volume check", fill=(42, 37, 32, 255), font=body_font)
    draw.text((1060, 1290), "Side thickness check", fill=(42, 37, 32, 255), font=body_font)
    draw.text((1560, 1290), "Back invented side", fill=(42, 37, 32, 255), font=body_font)
    board.save(BOARD_RENDER)


def build() -> None:
    clear_scene()
    setup_scene()
    add_review_lighting()
    texture_paths = make_texture_sources()

    front_material = make_texture_material("M_GIA_BloodAxeCairn_Hybrid_A1ProjectionFront_A01", texture_paths["front_bc"], roughness=0.86)
    side_material = make_texture_material("M_GIA_BloodAxeCairn_Hybrid_StoneSide_A01", texture_paths["side_bc"], texture_paths["side_n"], 0.91)
    earth_material = make_flat_material("M_GIA_BloodAxeCairn_Hybrid_AshMud_A01", (0.135, 0.085, 0.050, 1.0), 0.96)
    rawhide_material = make_flat_material("M_GIA_BloodAxeCairn_Hybrid_Rawhide_A01", (0.47, 0.285, 0.105, 1.0), 0.86)
    collision_material = make_flat_material("M_AET_CollisionProxy_ReviewOnly_A01", (0.1, 0.42, 0.95, 0.22))
    reference_material = make_reference_material("M_GIA_BloodAxeCairn_Hybrid_A1Reference_A01")
    materials = [front_material, side_material, earth_material, rawhide_material]

    lod0_collection = make_collection(f"{ASSET_NAME}_LOD0_HybridShells")
    lod1_collection = make_collection(f"{ASSET_NAME}_LOD1_HybridShells", hidden=True)
    lod2_collection = make_collection(f"{ASSET_NAME}_LOD2_HybridShells", hidden=True)
    lod3_collection = make_collection(f"{ASSET_NAME}_LOD3_HybridShells", hidden=True)
    collision_collection = make_collection(f"{ASSET_NAME}_Collision_Source", hidden=True)

    lod0_objects = build_lod_collection(lod0_collection, materials, 1, 1.0)
    lod0_objects += add_physical_details(lod0_collection, side_material, earth_material, rawhide_material, 0)
    lod1_objects = build_lod_collection(lod1_collection, materials, 2, 0.995)
    lod1_objects += add_physical_details(lod1_collection, side_material, earth_material, rawhide_material, 1)
    lod2_objects = build_lod_collection(lod2_collection, materials, 2, 0.985, max_shells=7)
    lod3_objects = build_lod_collection(lod3_collection, materials, 3, 0.96, max_shells=5)
    collision = add_collision_proxy(collision_material, collision_collection)

    add_asset_metadata(
        ASSET_NAME,
        "Revised A1 Blood Axe cairn candidate using source-image front projection plus sculpted real volume. Created after rejecting the procedural complete pass for poor art match.",
        UNREAL_PATH,
    )

    blend_path = BLENDER_ROOT / REL_PATH / f"{ASSET_NAME}.blend"
    export_path = EXPORT_ROOT / REL_PATH / f"{ASSET_NAME}.fbx"
    blend_path.parent.mkdir(parents=True, exist_ok=True)
    export_path.parent.mkdir(parents=True, exist_ok=True)

    render_reviews(reference_material)
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
