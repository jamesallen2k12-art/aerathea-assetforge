#!/usr/bin/env python3
"""Build a faithful A1 concept trace/projection proof for the Blood Axe cairn.

Run with:
    blender --background --python Tools/DCC/build_bloodaxe_cairn_a1_faithful_trace.py

This pass deliberately prioritizes matching the approved A1 concept view. It
creates a camera-projected relief mesh from the source concept image, with LOD
variants and a simple collision proxy. It is not a final 360-degree game prop.
"""

from __future__ import annotations

import math
import shutil
import sys
from pathlib import Path

import bpy
from mathutils import Vector


ROOT = Path(__file__).resolve().parents[2]
SOURCE_ROOT = ROOT / "SourceAssets"
BLENDER_ROOT = SOURCE_ROOT / "Blender"
EXPORT_ROOT = SOURCE_ROOT / "Exports"
TEXTURE_ROOT = SOURCE_ROOT / "Textures"
REVIEW_ROOT = ROOT / "Saved" / "Automation" / "DCC" / "SM_GIA_BloodAxeCairnSlabCluster_A01_FaithfulTrace"
REFERENCE_IMAGE = ROOT / "docs/assets/visual_canon/VC_GIA_BloodAxe_CairnStones_A01_A1_Crop.png"

ASSET_NAME = "SM_GIA_BloodAxeCairnSlabCluster_A01_FaithfulTrace"
REL_PATH = f"Props/Giants/BloodAxe/Cairns/{ASSET_NAME}"
UNREAL_PATH = f"/Game/Aerathea/Props/Giants/BloodAxe/Cairns/{ASSET_NAME}"
TEXTURE_REL_PATH = f"Props/Giants/BloodAxe/Cairns/{ASSET_NAME}"
REVIEW_RENDER = REVIEW_ROOT / f"{ASSET_NAME}_ConceptTraceReview.png"
OVERLAY_RENDER = REVIEW_ROOT / f"{ASSET_NAME}_OverlayFitReview.png"
EXACT_PROJECTION_RENDER = REVIEW_ROOT / f"{ASSET_NAME}_ExactProjectionReview.png"

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


def make_emission_image_material(name: str, image: bpy.types.Image) -> bpy.types.Material:
    material = bpy.data.materials.new(name)
    material.use_nodes = True
    nodes = material.node_tree.nodes
    nodes.clear()
    texture = nodes.new(type="ShaderNodeTexImage")
    texture.image = image
    texture.extension = "CLIP"
    emission = nodes.new(type="ShaderNodeEmission")
    emission.inputs["Strength"].default_value = 1.0
    output = nodes.new(type="ShaderNodeOutputMaterial")
    material.node_tree.links.new(texture.outputs["Color"], emission.inputs["Color"])
    material.node_tree.links.new(emission.outputs["Emission"], output.inputs["Surface"])
    material.diffuse_color = (1.0, 1.0, 1.0, 1.0)
    return material


def make_flat_material(name: str, color: tuple[float, float, float, float]) -> bpy.types.Material:
    material = bpy.data.materials.new(name)
    material.diffuse_color = color
    material.use_nodes = True
    bsdf = material.node_tree.nodes.get("Principled BSDF")
    if bsdf is not None:
        bsdf.inputs["Base Color"].default_value = color
        bsdf.inputs["Roughness"].default_value = 0.92
        bsdf.inputs["Metallic"].default_value = 0.0
    return material


def point_in_polygon(px: float, py: float, polygon: list[tuple[float, float]]) -> bool:
    inside = False
    previous_x, previous_y = polygon[-1]
    for current_x, current_y in polygon:
        crosses = (current_y > py) != (previous_y > py)
        if crosses:
            slope_x = (previous_x - current_x) * (py - current_y) / (previous_y - current_y) + current_x
            if px < slope_x:
                inside = not inside
        previous_x, previous_y = current_x, current_y
    return inside


def image_pixel(pixels: list[float], width: int, height: int, px: int, py_from_top: int) -> tuple[float, float, float]:
    px = max(0, min(width - 1, px))
    py_from_top = max(0, min(height - 1, py_from_top))
    image_y = height - 1 - py_from_top
    index = (image_y * width + px) * 4
    return pixels[index], pixels[index + 1], pixels[index + 2]


def sample_block(pixels: list[float], width: int, height: int, px: int, py: int, cell: int) -> tuple[float, float, float, float, float]:
    samples = 0
    r_total = 0.0
    g_total = 0.0
    b_total = 0.0
    for yy in range(py, min(py + cell, height)):
        for xx in range(px, min(px + cell, width)):
            r, g, b = image_pixel(pixels, width, height, xx, yy)
            r_total += r
            g_total += g
            b_total += b
            samples += 1
    if samples == 0:
        return 0.0, 0.0, 0.0, 0.0, 0.0
    r = r_total / samples
    g = g_total / samples
    b = b_total / samples
    luminance = 0.2126 * r + 0.7152 * g + 0.0722 * b
    saturation = max(r, g, b) - min(r, g, b)
    return r, g, b, luminance, saturation


def foreground_mask(px: float, py: float, r: float, g: float, b: float, luminance: float, saturation: float) -> bool:
    if py < 70 or py > 352:
        return False
    trace_regions = [
        # Dirt/ash base and lower scatter.
        [(4, 284), (35, 263), (86, 252), (136, 268), (190, 292), (260, 273), (350, 286), (340, 321), (253, 338), (138, 342), (42, 329), (4, 309)],
        # Left stacked slab and tied lower stones.
        [(8, 229), (60, 202), (102, 188), (134, 214), (124, 263), (76, 288), (20, 272)],
        # Long front painted slab.
        [(66, 212), (132, 178), (249, 205), (297, 248), (238, 294), (124, 286), (58, 252)],
        # Tall rear painted shard.
        [(143, 165), (193, 82), (226, 98), (255, 206), (205, 229), (164, 214)],
        # Central small vertical shard.
        [(121, 170), (148, 136), (168, 221), (136, 235)],
        # Rear right upright stone.
        [(250, 176), (301, 158), (339, 228), (326, 282), (273, 264), (248, 218)],
        # Right low support and stones.
        [(250, 238), (318, 235), (350, 270), (335, 303), (274, 294), (229, 268)],
        # Left foreground rock and rope mass.
        [(34, 251), (98, 241), (143, 268), (128, 307), (62, 313), (16, 291)],
        # Rear left small spike and stack.
        [(70, 195), (112, 160), (134, 186), (114, 230), (76, 226)],
        # Right loose stones.
        [(300, 276), (351, 281), (348, 314), (301, 322), (272, 302)],
    ]
    if not any(point_in_polygon(px, py, region) for region in trace_regions):
        return False
    red_signal = r > 0.15 and r > g * 1.18 and r > b * 1.12
    brown_signal = r > b * 1.12 and g > b * 0.98 and luminance < 0.56
    dark_stone = luminance < 0.42
    warm_stone_or_rope = saturation > 0.028 and luminance < 0.64
    ground_shadow = py > 274 and luminance < 0.60 and (saturation > 0.012 or luminance < 0.50)
    return red_signal or brown_signal or dark_stone or warm_stone_or_rope or ground_shadow


def pixel_to_world(px: float, py: float, x_offset: float = 0.0) -> tuple[float, float]:
    x = (px - IMAGE_CENTER_X) * X_SCALE + x_offset
    z = (GROUND_PX_Y - py) * Z_SCALE
    return x, z


def build_projection_mesh(
    name: str,
    image: bpy.types.Image,
    pixels: list[float],
    material: bpy.types.Material,
    collection: bpy.types.Collection,
    cell: int,
    x_offset: float = 0.0,
) -> bpy.types.Object:
    verts: list[tuple[float, float, float]] = []
    faces: list[tuple[int, int, int, int]] = []
    face_uvs: list[list[tuple[float, float]]] = []
    for py in range(0, IMAGE_HEIGHT, cell):
        for px in range(0, IMAGE_WIDTH, cell):
            center_x = px + cell * 0.5
            center_y = py + cell * 0.5
            r, g, b, luminance, saturation = sample_block(pixels, IMAGE_WIDTH, IMAGE_HEIGHT, px, py, cell)
            if not foreground_mask(center_x, center_y, r, g, b, luminance, saturation):
                continue

            x0, z0 = pixel_to_world(px, py, x_offset)
            x1, z1 = pixel_to_world(min(px + cell, IMAGE_WIDTH), min(py + cell, IMAGE_HEIGHT), x_offset)
            depth = -10.0 - (1.0 - luminance) * 9.0 - max(0.0, (center_y - 210.0)) * 0.025

            base = len(verts)
            verts.extend(
                [
                    (x0, depth, z0),
                    (x0, depth, z1),
                    (x1, depth, z1),
                    (x1, depth, z0),
                ]
            )
            faces.append((base, base + 1, base + 2, base + 3))
            u0 = px / IMAGE_WIDTH
            u1 = min(px + cell, IMAGE_WIDTH) / IMAGE_WIDTH
            v0 = 1.0 - py / IMAGE_HEIGHT
            v1 = 1.0 - min(py + cell, IMAGE_HEIGHT) / IMAGE_HEIGHT
            face_uvs.append([(u0, v0), (u0, v1), (u1, v1), (u1, v0)])

    mesh = bpy.data.meshes.new(f"{name}_Mesh")
    mesh.from_pydata(verts, [], faces)
    mesh.update()
    uv_layer = mesh.uv_layers.new(name="AET_ConceptProjectionUV")
    for polygon, uvs in zip(mesh.polygons, face_uvs):
        for loop_index, uv in zip(polygon.loop_indices, uvs):
            uv_layer.data[loop_index].uv = uv
    obj = bpy.data.objects.new(name, mesh)
    obj.data.materials.append(material)
    collection.objects.link(obj)
    solidify = obj.modifiers.new("AET_TraceReliefThickness", "SOLIDIFY")
    solidify.thickness = 4.0
    solidify.offset = 0.0
    try:
        weighted = obj.modifiers.new("AET_TraceWeightedNormals", "WEIGHTED_NORMAL")
        set_active(obj)
        bpy.ops.object.modifier_apply(modifier=weighted.name)
    except Exception:
        pass
    return obj


def build_full_projection_mesh(
    name: str,
    pixels: list[float],
    material: bpy.types.Material,
    collection: bpy.types.Collection,
    cell: int,
    x_offset: float,
) -> bpy.types.Object:
    verts: list[tuple[float, float, float]] = []
    faces: list[tuple[int, int, int, int]] = []
    face_uvs: list[list[tuple[float, float]]] = []
    for py in range(0, IMAGE_HEIGHT, cell):
        for px in range(0, IMAGE_WIDTH, cell):
            _r, _g, _b, luminance, _saturation = sample_block(pixels, IMAGE_WIDTH, IMAGE_HEIGHT, px, py, cell)
            x0, z0 = pixel_to_world(px, py, x_offset)
            x1, z1 = pixel_to_world(min(px + cell, IMAGE_WIDTH), min(py + cell, IMAGE_HEIGHT), x_offset)
            depth = -8.0 - (1.0 - luminance) * 3.5
            base = len(verts)
            verts.extend(
                [
                    (x0, depth, z0),
                    (x0, depth, z1),
                    (x1, depth, z1),
                    (x1, depth, z0),
                ]
            )
            faces.append((base, base + 1, base + 2, base + 3))
            u0 = px / IMAGE_WIDTH
            u1 = min(px + cell, IMAGE_WIDTH) / IMAGE_WIDTH
            v0 = 1.0 - py / IMAGE_HEIGHT
            v1 = 1.0 - min(py + cell, IMAGE_HEIGHT) / IMAGE_HEIGHT
            face_uvs.append([(u0, v0), (u0, v1), (u1, v1), (u1, v0)])
    mesh = bpy.data.meshes.new(f"{name}_Mesh")
    mesh.from_pydata(verts, [], faces)
    mesh.update()
    uv_layer = mesh.uv_layers.new(name="AET_ExactProjectionUV")
    for polygon, uvs in zip(mesh.polygons, face_uvs):
        for loop_index, uv in zip(polygon.loop_indices, uvs):
            uv_layer.data[loop_index].uv = uv
    obj = bpy.data.objects.new(name, mesh)
    obj.data.materials.append(material)
    collection.objects.link(obj)
    return obj


def add_reference_plate(material: bpy.types.Material, collection: bpy.types.Collection, x_offset: float) -> bpy.types.Object:
    top_left_x, top_left_z = pixel_to_world(0, 0, x_offset)
    bottom_right_x, bottom_right_z = pixel_to_world(IMAGE_WIDTH, IMAGE_HEIGHT, x_offset)
    y = 18.0
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


def add_collision_proxy(material: bpy.types.Material, collection: bpy.types.Collection) -> bpy.types.Object:
    bpy.ops.mesh.primitive_cube_add(size=1.0, location=(0.0, -12.0, 70.0), rotation=(0.0, 0.0, 0.0))
    obj = bpy.context.object
    obj.name = f"UCX_{ASSET_NAME}_00"
    obj.dimensions = (335.0, 38.0, 160.0)
    obj.data.materials.append(material)
    set_active(obj)
    bpy.ops.object.transform_apply(location=False, rotation=False, scale=True)
    obj.display_type = "WIRE"
    obj.hide_render = True
    for current in list(obj.users_collection):
        current.objects.unlink(obj)
    collection.objects.link(obj)
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


def setup_camera(target_x: float, ortho_scale: float) -> None:
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


def render_review(reference_material: bpy.types.Material, projection_material: bpy.types.Material, pixels: list[float]) -> None:
    REVIEW_ROOT.mkdir(parents=True, exist_ok=True)
    scene = bpy.context.scene
    scene.render.resolution_x = 1600
    scene.render.resolution_y = 1000
    if scene.world is not None:
        scene.world.color = (0.50, 0.49, 0.46)

    review_collection = make_collection("Review_A1_Reference")
    add_reference_plate(reference_material, review_collection, -430.0)
    setup_camera(-215.0, 820.0)
    scene.render.filepath = str(REVIEW_RENDER)
    bpy.ops.render.render(write_still=True)

    for obj in review_collection.objects:
        obj.hide_render = True
    exact_collection = make_collection("Review_A1_ExactProjectionMesh")
    add_reference_plate(reference_material, exact_collection, -430.0)
    build_full_projection_mesh("Review_A1FullConceptProjectionMesh_Cell8", pixels, projection_material, exact_collection, 8, 0.0)
    setup_camera(-215.0, 820.0)
    scene.render.filepath = str(EXACT_PROJECTION_RENDER)
    bpy.ops.render.render(write_still=True)
    for obj in exact_collection.objects:
        obj.hide_render = True

    for obj in review_collection.objects:
        obj.hide_render = True
    overlay_collection = make_collection("Review_A1_Overlay")
    add_reference_plate(reference_material, overlay_collection, 0.0)
    for obj in overlay_collection.objects:
        obj.display_type = "TEXTURED"
    setup_camera(0.0, 310.0)
    scene.render.filepath = str(OVERLAY_RENDER)
    bpy.ops.render.render(write_still=True)
    for obj in overlay_collection.objects:
        obj.hide_render = True


def copy_reference_texture() -> bpy.types.Image:
    texture_dir = TEXTURE_ROOT / TEXTURE_REL_PATH
    texture_dir.mkdir(parents=True, exist_ok=True)
    projection_path = texture_dir / "T_GIA_BloodAxeCairnSlabCluster_A01_A1_ConceptProjection.png"
    shutil.copyfile(REFERENCE_IMAGE, projection_path)
    return bpy.data.images.load(str(projection_path))


def build() -> None:
    clear_scene()
    setup_scene()
    image = copy_reference_texture()
    pixels = list(image.pixels)

    projection_material = make_emission_image_material("M_GIA_BloodAxeCairn_A1_ConceptProjection_A01", image)
    reference_material = make_emission_image_material("M_GIA_BloodAxeCairn_A1_Reference_A01", image)
    collision_material = make_flat_material("M_AET_CollisionProxy_ReviewOnly_A01", (0.1, 0.42, 0.95, 0.22))

    lod0_collection = make_collection(f"{ASSET_NAME}_LOD0_ProjectionMesh")
    lod1_collection = make_collection(f"{ASSET_NAME}_LOD1_ProjectionMesh", hidden=True)
    lod2_collection = make_collection(f"{ASSET_NAME}_LOD2_ProjectionMesh", hidden=True)
    lod3_collection = make_collection(f"{ASSET_NAME}_LOD3_ProjectionMesh", hidden=True)
    collision_collection = make_collection(f"{ASSET_NAME}_Collision_Source", hidden=True)

    lod0 = build_projection_mesh("LOD0_A1ConceptProjectedRelief_Cell4", image, pixels, projection_material, lod0_collection, 4)
    lod1 = build_projection_mesh("LOD1_A1ConceptProjectedRelief_Cell8", image, pixels, projection_material, lod1_collection, 8)
    lod2 = build_projection_mesh("LOD2_A1ConceptProjectedRelief_Cell14", image, pixels, projection_material, lod2_collection, 14)
    lod3 = build_projection_mesh("LOD3_A1ConceptProjectedRelief_Cell24", image, pixels, projection_material, lod3_collection, 24)
    collision = add_collision_proxy(collision_material, collision_collection)

    add_asset_metadata(
        ASSET_NAME,
        "Faithful A1 concept trace/projection proof. Foreground concept pixels become a camera-projected relief mesh with UVs mapped to the exact source concept. This is for visual approval of the reconstruction process before full 360-degree game-ready modeling.",
        UNREAL_PATH,
    )

    blend_path = BLENDER_ROOT / REL_PATH / f"{ASSET_NAME}.blend"
    export_path = EXPORT_ROOT / REL_PATH / f"{ASSET_NAME}.fbx"
    blend_path.parent.mkdir(parents=True, exist_ok=True)
    export_path.parent.mkdir(parents=True, exist_ok=True)

    render_review(reference_material, projection_material, pixels)
    bpy.ops.wm.save_as_mainfile(filepath=str(blend_path))

    export_selected_fbx(export_path, [lod0, collision])
    export_selected_fbx(export_path.with_name(f"{ASSET_NAME}_LOD0.fbx"), [lod0])
    export_selected_fbx(export_path.with_name(f"{ASSET_NAME}_LOD1.fbx"), [lod1])
    export_selected_fbx(export_path.with_name(f"{ASSET_NAME}_LOD2.fbx"), [lod2])
    export_selected_fbx(export_path.with_name(f"{ASSET_NAME}_LOD3.fbx"), [lod3])

    width, depth, height = collection_bounds(lod0_collection)
    print(f"Built {blend_path.relative_to(ROOT)}")
    print(f"Exported {export_path.relative_to(ROOT)}")
    print(f"Rendered {REVIEW_RENDER.relative_to(ROOT)}")
    print(f"Rendered {OVERLAY_RENDER.relative_to(ROOT)}")
    print(f"Rendered {EXACT_PROJECTION_RENDER.relative_to(ROOT)}")
    print(f"LOD0 tris: {collection_triangle_count(lod0_collection)}")
    print(f"LOD1 tris: {collection_triangle_count(lod1_collection)}")
    print(f"LOD2 tris: {collection_triangle_count(lod2_collection)}")
    print(f"LOD3 tris: {collection_triangle_count(lod3_collection)}")
    print(f"LOD0 bounds: {width:.2f}w x {depth:.2f}d x {height:.2f}h cm")
    print(f"Collision proxies: 1")


if __name__ == "__main__":
    build()
