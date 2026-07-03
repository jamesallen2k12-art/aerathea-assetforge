#!/usr/bin/env python3
"""Build the A1 faithful game-ready Blood Axe cairn candidate.

Run with:
    blender --background --python Tools/DCC/build_bloodaxe_cairn_a1_game_ready.py

This creates a real static-mesh prop from hand-traced A1 stone shells. The front
faces use concept-projected UVs so the approved source view stays close to the
concept, while backs/sides receive production-friendly stone/earth/rawhide
materials for 3D use.
"""

from __future__ import annotations

import math
import shutil
import sys
from array import array
from pathlib import Path

import bpy
from mathutils import Vector


ROOT = Path(__file__).resolve().parents[2]
SOURCE_ROOT = ROOT / "SourceAssets"
BLENDER_ROOT = SOURCE_ROOT / "Blender"
EXPORT_ROOT = SOURCE_ROOT / "Exports"
TEXTURE_ROOT = SOURCE_ROOT / "Textures"
REVIEW_ROOT = ROOT / "Saved" / "Automation" / "DCC" / "SM_GIA_BloodAxeCairnSlabCluster_A01_GameReady"
REFERENCE_IMAGE = ROOT / "docs/assets/visual_canon/VC_GIA_BloodAxe_CairnStones_A01_A1_Crop.png"

ASSET_NAME = "SM_GIA_BloodAxeCairnSlabCluster_A01_GameReady"
REL_PATH = f"Props/Giants/BloodAxe/Cairns/{ASSET_NAME}"
UNREAL_PATH = f"/Game/Aerathea/Props/Giants/BloodAxe/Cairns/{ASSET_NAME}"
TEXTURE_REL_PATH = f"Props/Giants/BloodAxe/Cairns/{ASSET_NAME}"

FRONT_REVIEW_RENDER = REVIEW_ROOT / f"{ASSET_NAME}_FrontMatchReview.png"
PERSPECTIVE_REVIEW_RENDER = REVIEW_ROOT / f"{ASSET_NAME}_PerspectiveReview.png"

IMAGE_WIDTH = 360
IMAGE_HEIGHT = 430
IMAGE_CENTER_X = 180.0
GROUND_PX_Y = 340.0
TOP_PX_Y = 82.0
X_SCALE = 1.0
Z_SCALE = 154.0 / (GROUND_PX_Y - TOP_PX_Y)

sys.path.insert(0, str(ROOT))

from Tools.DCC.build_next_slice_assets import add_asset_metadata, clear_scene, setup_scene  # noqa: E402


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


def pixel_to_world(px: float, py: float, x_offset: float = 0.0) -> tuple[float, float]:
    x = (px - IMAGE_CENTER_X) * X_SCALE + x_offset
    z = (GROUND_PX_Y - py) * Z_SCALE
    return x, z


def image_uv(px: float, py: float) -> tuple[float, float]:
    return px / IMAGE_WIDTH, 1.0 - py / IMAGE_HEIGHT


def clamp(value: float) -> float:
    return max(0.0, min(1.0, value))


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


def make_texture_material(
    name: str,
    bc_path: Path,
    normal_path: Path | None = None,
    orm_path: Path | None = None,
    roughness: float = 0.88,
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
        normal_map.inputs["Strength"].default_value = 0.42
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


def make_emission_reference_material(name: str, image_path: Path) -> bpy.types.Material:
    material = bpy.data.materials.new(name)
    material.use_nodes = True
    nodes = material.node_tree.nodes
    nodes.clear()
    texture = nodes.new(type="ShaderNodeTexImage")
    texture.image = bpy.data.images.load(str(image_path))
    emission = nodes.new(type="ShaderNodeEmission")
    output = nodes.new(type="ShaderNodeOutputMaterial")
    material.node_tree.links.new(texture.outputs["Color"], emission.inputs["Color"])
    material.node_tree.links.new(emission.outputs["Emission"], output.inputs["Surface"])
    return material


def generate_side_textures() -> dict[str, Path]:
    texture_dir = TEXTURE_ROOT / TEXTURE_REL_PATH
    width = 1024
    height = 1024
    bc = array("f")
    normal = array("f")
    orm = array("f")
    for y in range(height):
        v = y / (height - 1)
        for x in range(width):
            u = x / (width - 1)
            n1 = procedural_noise(x, y, 171)
            n2 = procedural_noise(x // 4, y // 4, 311)
            if v < 0.25:
                base = (0.18 + n1 * 0.10, 0.12 + n2 * 0.07, 0.07 + n1 * 0.05)
                roughness = 0.95
                occlusion = 0.58 + n2 * 0.20
            elif 0.76 < v and 0.08 < u < 0.44:
                base = (0.32 + n1 * 0.16, 0.20 + n2 * 0.10, 0.09 + n1 * 0.05)
                roughness = 0.82 + n2 * 0.10
                occlusion = 0.64 + n1 * 0.16
            else:
                warm = 0.09 + n2 * 0.12
                cold = 0.16 + n1 * 0.16
                base = (cold + warm * 0.80, cold + warm * 0.62, cold + warm * 0.36)
                roughness = 0.88 + n2 * 0.08
                occlusion = 0.50 + n1 * 0.25
            bc.extend((clamp(base[0]), clamp(base[1]), clamp(base[2]), 1.0))
            height_value = (n1 - 0.5) * 0.13 + (n2 - 0.5) * 0.08
            normal.extend((clamp(0.5 + height_value), clamp(0.5 + (procedural_noise(x, y, 577) - 0.5) * 0.12), 1.0, 1.0))
            orm.extend((clamp(occlusion), clamp(roughness), 0.0, 1.0))
    paths = {
        "front_bc": texture_dir / "T_GIA_BloodAxeCairnSlabCluster_A01_A1Projection_BC.png",
        "side_bc": texture_dir / "T_GIA_BloodAxeCairnSlabCluster_A01_GameReadySide_BC.png",
        "side_n": texture_dir / "T_GIA_BloodAxeCairnSlabCluster_A01_GameReadySide_N.png",
        "side_orm": texture_dir / "T_GIA_BloodAxeCairnSlabCluster_A01_GameReadySide_ORM.png",
    }
    texture_dir.mkdir(parents=True, exist_ok=True)
    shutil.copyfile(REFERENCE_IMAGE, paths["front_bc"])
    save_texture(paths["side_bc"], width, height, bc)
    save_texture(paths["side_n"], width, height, normal)
    save_texture(paths["side_orm"], width, height, orm)
    return paths


def simplify_polygon(points: list[tuple[float, float]], stride: int) -> list[tuple[float, float]]:
    if stride <= 1 or len(points) <= 6:
        return points
    simplified = [point for index, point in enumerate(points) if index % stride == 0]
    if len(simplified) < 4:
        return points
    return simplified


def add_shell(
    name: str,
    polygon_px: list[tuple[float, float]],
    front_y: float,
    thickness: float,
    materials: list[bpy.types.Material],
    collection: bpy.types.Collection,
    side_material_index: int,
    z_lift: float = 0.0,
    scale: float = 1.0,
) -> bpy.types.Object:
    center_x = sum(px for px, _py in polygon_px) / len(polygon_px)
    center_y = sum(py for _px, py in polygon_px) / len(polygon_px)
    scaled_points = []
    for px, py in polygon_px:
        scaled_points.append((center_x + (px - center_x) * scale, center_y + (py - center_y) * scale))

    verts: list[tuple[float, float, float]] = []
    for px, py in scaled_points:
        x, z = pixel_to_world(px, py)
        verts.append((x, front_y, z + z_lift))
    back_scale = 0.86
    back_drop = 3.0
    if side_material_index == 2:
        back_scale = 0.94
        back_drop = 1.0
    elif side_material_index == 3:
        back_scale = 0.82
        back_drop = 1.5
    for px, py in scaled_points:
        back_px = center_x + (px - center_x) * back_scale
        back_py = center_y + (py - center_y) * back_scale
        x, z = pixel_to_world(back_px, back_py)
        verts.append((x, front_y + thickness, z + z_lift - back_drop))

    count = len(scaled_points)
    back_points = verts[count : count * 2]
    back_center_index = len(verts)
    back_center_x = sum(point[0] for point in back_points) / count
    back_center_z = sum(point[2] for point in back_points) / count
    back_center_lift = 1.0 if side_material_index == 2 else 5.0
    verts.append((back_center_x, front_y + thickness + back_center_lift, back_center_z + back_center_lift * 0.45))

    faces: list[tuple[int, ...]] = [tuple(range(count))]
    for index in range(count):
        next_index = (index + 1) % count
        faces.append((count + next_index, count + index, back_center_index))
    for index in range(count):
        next_index = (index + 1) % count
        faces.append((index, next_index, count + next_index, count + index))

    mesh = bpy.data.meshes.new(f"{name}_Mesh")
    mesh.from_pydata(verts, [], faces)
    mesh.update()
    uv_layer = mesh.uv_layers.new(name="AET_A1ProjectionUV")

    front_uvs = [image_uv(px, py) for px, py in scaled_points]
    for loop_index, uv in zip(mesh.polygons[0].loop_indices, front_uvs):
        uv_layer.data[loop_index].uv = uv
    for polygon in mesh.polygons[1:]:
        polygon.material_index = side_material_index
        for local_index, loop_index in enumerate(polygon.loop_indices):
            uv_layer.data[loop_index].uv = ((local_index % 2) * 0.5, 0.25 + (local_index // 2) * 0.5)

    obj = bpy.data.objects.new(name, mesh)
    for material in materials:
        obj.data.materials.append(material)
    collection.objects.link(obj)

    bevel = obj.modifiers.new("AET_ShellEdgeSoftening", "BEVEL")
    bevel.width = 0.8
    bevel.segments = 1
    bevel.affect = "EDGES"
    set_active(obj)
    bpy.ops.object.modifier_apply(modifier=bevel.name)
    normal = obj.modifiers.new("AET_ShellWeightedNormals", "WEIGHTED_NORMAL")
    set_active(obj)
    bpy.ops.object.modifier_apply(modifier=normal.name)
    return obj


def shell_specs() -> list[dict[str, object]]:
    return [
        {
            "name": "A1_GroundAshMudBase",
            "points": [(5, 286), (44, 260), (94, 251), (145, 265), (203, 288), (263, 275), (350, 288), (340, 320), (251, 340), (139, 343), (42, 328), (4, 310)],
            "y": -2.0,
            "depth": 24.0,
            "side": 2,
        },
        {
            "name": "A1_LongFrontPaintedSlab",
            "points": [(62, 213), (128, 178), (246, 204), (299, 249), (238, 292), (122, 286), (56, 252)],
            "y": -20.0,
            "depth": 26.0,
            "side": 1,
            "scale": 1.01,
        },
        {
            "name": "A1_TallRearPaintedShard",
            "points": [(142, 166), (194, 82), (226, 98), (257, 206), (205, 229), (164, 214)],
            "y": 5.0,
            "depth": 28.0,
            "side": 1,
            "scale": 1.015,
        },
        {
            "name": "A1_LeftStackedStoneBlock",
            "points": [(10, 229), (59, 202), (104, 188), (135, 214), (123, 263), (76, 288), (20, 272)],
            "y": -12.0,
            "depth": 32.0,
            "side": 1,
        },
        {
            "name": "A1_RearRightUprightStone",
            "points": [(249, 176), (302, 158), (340, 228), (326, 282), (272, 264), (247, 218)],
            "y": 3.0,
            "depth": 30.0,
            "side": 1,
        },
        {
            "name": "A1_CentralNarrowShard",
            "points": [(121, 170), (148, 136), (168, 221), (136, 235)],
            "y": 0.0,
            "depth": 22.0,
            "side": 1,
        },
        {
            "name": "A1_LeftRearSpikeAndCap",
            "points": [(69, 195), (112, 160), (134, 186), (114, 230), (76, 226)],
            "y": -2.0,
            "depth": 22.0,
            "side": 1,
        },
        {
            "name": "A1_RightSupportStoneCluster",
            "points": [(250, 238), (318, 235), (350, 270), (335, 303), (274, 294), (229, 268)],
            "y": -13.0,
            "depth": 24.0,
            "side": 1,
        },
        {
            "name": "A1_LeftForegroundRopeMass",
            "points": [(34, 251), (98, 241), (143, 268), (128, 307), (62, 313), (16, 291)],
            "y": -24.0,
            "depth": 18.0,
            "side": 3,
        },
        {
            "name": "A1_RightLooseStoneScatter",
            "points": [(300, 276), (351, 281), (348, 314), (301, 322), (272, 302)],
            "y": -25.0,
            "depth": 17.0,
            "side": 1,
        },
        {
            "name": "A1_FrontPebbleScatter",
            "points": [(77, 294), (130, 289), (175, 311), (152, 334), (82, 328), (48, 311)],
            "y": -27.0,
            "depth": 13.0,
            "side": 2,
        },
    ]


def build_lod_collection(
    collection: bpy.types.Collection,
    materials: list[bpy.types.Material],
    stride: int,
    scale: float,
    max_shells: int | None = None,
) -> list[bpy.types.Object]:
    objects: list[bpy.types.Object] = []
    specs = shell_specs()
    if max_shells is not None:
        specs = specs[:max_shells]
    for spec in specs:
        points = simplify_polygon(spec["points"], stride)  # type: ignore[arg-type]
        objects.append(
            add_shell(
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


def add_collision_proxy(material: bpy.types.Material, collection: bpy.types.Collection) -> bpy.types.Object:
    bpy.ops.mesh.primitive_cube_add(size=1.0, location=(0.0, -9.0, 65.0), rotation=(0.0, 0.0, 0.0))
    obj = bpy.context.object
    obj.name = f"UCX_{ASSET_NAME}_00"
    obj.dimensions = (350.0, 62.0, 160.0)
    obj.data.materials.append(material)
    set_active(obj)
    bpy.ops.object.transform_apply(location=False, rotation=False, scale=True)
    obj.display_type = "WIRE"
    obj.hide_render = True
    for current in list(obj.users_collection):
        current.objects.unlink(obj)
    collection.objects.link(obj)
    return obj


def add_reference_plate(material: bpy.types.Material, collection: bpy.types.Collection, x_offset: float) -> bpy.types.Object:
    top_left_x, top_left_z = pixel_to_world(0, 0, x_offset)
    bottom_right_x, bottom_right_z = pixel_to_world(IMAGE_WIDTH, IMAGE_HEIGHT, x_offset)
    y = 22.0
    verts = [
        (top_left_x, y, top_left_z),
        (top_left_x, y, bottom_right_z),
        (bottom_right_x, y, bottom_right_z),
        (bottom_right_x, y, top_left_z),
    ]
    mesh = bpy.data.meshes.new("Review_A1ReferencePlate_Mesh")
    mesh.from_pydata(verts, [], [(0, 1, 2, 3)])
    mesh.update()
    uv_layer = mesh.uv_layers.new(name="AET_ReferenceUV")
    for loop_index, uv in zip(mesh.polygons[0].loop_indices, [(0, 1), (0, 0), (1, 0), (1, 1)]):
        uv_layer.data[loop_index].uv = uv
    obj = bpy.data.objects.new("Review_A1ReferencePlate", mesh)
    obj.data.materials.append(material)
    collection.objects.link(obj)
    return obj


def add_ground_shadow(material: bpy.types.Material, collection: bpy.types.Collection) -> bpy.types.Object:
    verts = [(0.0, -1.0, -4.0)]
    for index in range(48):
        angle = (index / 48.0) * math.tau
        verts.append((math.cos(angle) * 174.0, -1.0 + math.sin(angle) * 54.0, -4.0))
    faces = [tuple(range(49))]
    mesh = bpy.data.meshes.new("A1_GameReadyGroundContactPlane_Mesh")
    mesh.from_pydata(verts, [], faces)
    mesh.update()
    obj = bpy.data.objects.new("A1_GameReadyGroundContactPlane", mesh)
    obj.data.materials.append(material)
    collection.objects.link(obj)
    return obj


def add_review_lighting() -> None:
    scene = bpy.context.scene
    try:
        scene.view_settings.view_transform = "Standard"
    except TypeError:
        pass
    scene.view_settings.exposure = 1.15
    scene.view_settings.gamma = 1.0
    if scene.world is not None:
        scene.world.color = (0.62, 0.60, 0.56)
    lights = [
        ("AET_KeyLight_A01", "AREA", (-260.0, -360.0, 420.0), 1400.0, 520.0),
        ("AET_FillLight_A01", "AREA", (290.0, -260.0, 190.0), 430.0, 620.0),
        ("AET_RimLight_A01", "POINT", (0.0, 230.0, 190.0), 160.0, 0.0),
    ]
    for name, kind, location, energy, size in lights:
        data = bpy.data.lights.new(name, type=kind)
        data.energy = energy
        if kind == "AREA":
            data.size = size
        obj = bpy.data.objects.new(name, data)
        obj.location = location
        bpy.context.scene.collection.objects.link(obj)


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
        for collection in obj.users_collection:
            collection.hide_viewport = False
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


def setup_front_camera(target_x: float, ortho_scale: float) -> None:
    scene = bpy.context.scene
    bpy.ops.object.camera_add(location=(target_x, -720.0, 82.0))
    camera = bpy.context.object
    target = Vector((target_x, -8.0, 76.0))
    direction = target - Vector(camera.location)
    camera.rotation_euler = direction.to_track_quat("-Z", "Y").to_euler()
    camera.data.type = "ORTHO"
    camera.data.ortho_scale = ortho_scale
    camera.data.clip_start = 1
    camera.data.clip_end = 5000
    scene.camera = camera


def setup_perspective_camera() -> None:
    scene = bpy.context.scene
    bpy.ops.object.camera_add(location=(360.0, -520.0, 230.0))
    camera = bpy.context.object
    target = Vector((0.0, -6.0, 72.0))
    direction = target - Vector(camera.location)
    camera.rotation_euler = direction.to_track_quat("-Z", "Y").to_euler()
    camera.data.type = "ORTHO"
    camera.data.ortho_scale = 405
    camera.data.clip_start = 1
    camera.data.clip_end = 5000
    scene.camera = camera


def render_reviews(reference_material: bpy.types.Material, lod0_collection: bpy.types.Collection) -> None:
    REVIEW_ROOT.mkdir(parents=True, exist_ok=True)
    scene = bpy.context.scene
    scene.render.resolution_x = 1600
    scene.render.resolution_y = 1000
    if scene.world is not None:
        scene.world.color = (0.50, 0.49, 0.46)

    review_collection = make_collection("Review_A1_SourcePlate")
    add_reference_plate(reference_material, review_collection, -430.0)
    setup_front_camera(-215.0, 820.0)
    scene.render.filepath = str(FRONT_REVIEW_RENDER)
    bpy.ops.render.render(write_still=True)

    for obj in review_collection.objects:
        obj.hide_render = True
    setup_perspective_camera()
    scene.render.filepath = str(PERSPECTIVE_REVIEW_RENDER)
    bpy.ops.render.render(write_still=True)


def build() -> None:
    clear_scene()
    setup_scene()
    add_review_lighting()
    texture_paths = generate_side_textures()
    front_material = make_texture_material("M_GIA_BloodAxeCairn_A1ProjectionFront_A01", texture_paths["front_bc"], roughness=0.86)
    side_material = make_texture_material("M_GIA_BloodAxeCairn_GameReadyStoneSide_A01", texture_paths["side_bc"], texture_paths["side_n"], texture_paths["side_orm"], 0.9)
    earth_material = make_flat_material("M_GIA_BloodAxeCairn_GameReadyAshMudSide_A01", (0.10, 0.07, 0.045, 1.0), 0.95)
    rawhide_material = make_flat_material("M_GIA_BloodAxeCairn_GameReadyRawhideSide_A01", (0.20, 0.12, 0.045, 1.0), 0.86)
    collision_material = make_flat_material("M_AET_CollisionProxy_ReviewOnly_A01", (0.1, 0.42, 0.95, 0.22))
    reference_material = make_emission_reference_material("M_GIA_BloodAxeCairn_A1Reference_A01", REFERENCE_IMAGE)
    materials = [front_material, side_material, earth_material, rawhide_material]

    lod0_collection = make_collection(f"{ASSET_NAME}_LOD0_GameReadyShells")
    lod1_collection = make_collection(f"{ASSET_NAME}_LOD1_GameReadyShells", hidden=True)
    lod2_collection = make_collection(f"{ASSET_NAME}_LOD2_GameReadyShells", hidden=True)
    lod3_collection = make_collection(f"{ASSET_NAME}_LOD3_GameReadyShells", hidden=True)
    collision_collection = make_collection(f"{ASSET_NAME}_Collision_Source", hidden=True)

    lod0_objects = build_lod_collection(lod0_collection, materials, 1, 1.0)
    lod1_objects = build_lod_collection(lod1_collection, materials, 2, 0.995)
    lod2_objects = build_lod_collection(lod2_collection, materials, 2, 0.985, max_shells=7)
    lod3_objects = build_lod_collection(lod3_collection, materials, 3, 0.96, max_shells=5)
    collision = add_collision_proxy(collision_material, collision_collection)

    add_asset_metadata(
        ASSET_NAME,
        "Game-ready faithful A1 Blood Axe cairn candidate. Uses traced stone shells, concept-projected front UVs, production side/back materials, LOD0-LOD3 exports, collision proxy, and review renders. Final visual canon still requires Flamestrike approval.",
        UNREAL_PATH,
    )

    blend_path = BLENDER_ROOT / REL_PATH / f"{ASSET_NAME}.blend"
    export_path = EXPORT_ROOT / REL_PATH / f"{ASSET_NAME}.fbx"
    blend_path.parent.mkdir(parents=True, exist_ok=True)
    export_path.parent.mkdir(parents=True, exist_ok=True)

    render_reviews(reference_material, lod0_collection)
    bpy.ops.wm.save_as_mainfile(filepath=str(blend_path))

    export_selected_fbx(export_path, lod0_objects + [collision])
    export_selected_fbx(export_path.with_name(f"{ASSET_NAME}_LOD0.fbx"), lod0_objects)
    export_selected_fbx(export_path.with_name(f"{ASSET_NAME}_LOD1.fbx"), lod1_objects)
    export_selected_fbx(export_path.with_name(f"{ASSET_NAME}_LOD2.fbx"), lod2_objects)
    export_selected_fbx(export_path.with_name(f"{ASSET_NAME}_LOD3.fbx"), lod3_objects)

    width, depth, height = collection_bounds(lod0_collection)
    print(f"Built {blend_path.relative_to(ROOT)}")
    print(f"Exported {export_path.relative_to(ROOT)}")
    print(f"Rendered {FRONT_REVIEW_RENDER.relative_to(ROOT)}")
    print(f"Rendered {PERSPECTIVE_REVIEW_RENDER.relative_to(ROOT)}")
    for texture_name, texture_path in texture_paths.items():
        print(f"Texture {texture_name}: {texture_path.relative_to(ROOT)}")
    print(f"LOD0 tris: {collection_triangle_count(lod0_collection)}")
    print(f"LOD1 tris: {collection_triangle_count(lod1_collection)}")
    print(f"LOD2 tris: {collection_triangle_count(lod2_collection)}")
    print(f"LOD3 tris: {collection_triangle_count(lod3_collection)}")
    print(f"LOD0 bounds: {width:.2f}w x {depth:.2f}d x {height:.2f}h cm")
    print("Collision proxies: 1")


if __name__ == "__main__":
    build()
