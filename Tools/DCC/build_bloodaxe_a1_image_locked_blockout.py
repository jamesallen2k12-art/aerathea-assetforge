#!/usr/bin/env python3
"""Build an image-locked Blood Axe A1 blockout proof.

This is a strict front-view DCC proof path for the BloodAxe A1 target. It uses
the approved A1 crop landmarks as camera-aligned geometry guides, then adds
shallow depth behind the traced stone faces. The output is for visual review
only until Flamestrike approves the concept-geometry match.
"""

from __future__ import annotations

import math
import sys
from pathlib import Path

import bpy
from mathutils import Vector


ROOT = Path(__file__).resolve().parents[2]
ASSET_NAME = "SM_GIA_BloodAxeCairnTarget_A1_A01"
REL_PATH = f"Props/Giants/BloodAxe/CairnTargets/A1/{ASSET_NAME}"
SOURCE_TARGET = "docs/assets/visual_canon/BloodAxeCairnTargets_A01/VC_GIA_BloodAxe_CairnTarget_A1.png"
TARGET_FRONT_CROP = ROOT / "docs" / "assets" / "props" / ASSET_NAME / f"{ASSET_NAME}_TargetFrontCrop.png"
REVIEW_ROOT = ROOT / "Saved" / "Automation" / "DCC" / ASSET_NAME
BLEND_ROOT = ROOT / "SourceAssets" / "Blender" / "Props" / "Giants" / "BloodAxe" / "CairnTargets" / "A1" / f"{ASSET_NAME}_A20_ImageLockedBlockout"

sys.path.insert(0, str(ROOT))

from Tools.DCC.build_next_slice_assets import add_asset_metadata, clear_scene, setup_scene  # noqa: E402
from Tools.DCC.make_bloodaxe_a1_trace_guide import LOCK_LINES, PAINT_GUIDES, TRACE  # noqa: E402


SOURCE_W = 395.0
SOURCE_H = 345.0
SOURCE_BASELINE_Y = 325.0
WORLD_SCALE = 0.60
USE_TARGET_PROJECTION = True


def ensure_dir(path: Path) -> None:
    path.mkdir(parents=True, exist_ok=True)


def img_to_world(point: tuple[int, int], x_offset: float = 0.0, z_offset: float = 0.0) -> tuple[float, float]:
    x, y = point
    return ((x - (SOURCE_W * 0.5)) * WORLD_SCALE + x_offset, (SOURCE_BASELINE_Y - y) * WORLD_SCALE + z_offset)


def make_material(name: str, color: tuple[float, float, float], roughness: float = 0.92) -> bpy.types.Material:
    material = bpy.data.materials.new(name)
    material.diffuse_color = (color[0], color[1], color[2], 1.0)
    material.use_nodes = True
    bsdf = material.node_tree.nodes.get("Principled BSDF")
    if bsdf is not None:
        bsdf.inputs["Base Color"].default_value = (color[0], color[1], color[2], 1.0)
        bsdf.inputs["Roughness"].default_value = roughness
        bsdf.inputs["Metallic"].default_value = 0.0
    return material


def make_projection_material() -> bpy.types.Material:
    material = bpy.data.materials.new("M_A20_A1_TargetProjectionGuide")
    material.diffuse_color = (1.0, 1.0, 1.0, 1.0)
    material.use_nodes = True
    material["Aerathea.MaterialPass"] = "temporary_a1_concept_projection_for_geometry_review"
    nodes = material.node_tree.nodes
    for node in list(nodes):
        nodes.remove(node)
    output = nodes.new(type="ShaderNodeOutputMaterial")
    output.location = (320, 0)
    emission = nodes.new(type="ShaderNodeEmission")
    emission.location = (70, 0)
    emission.inputs["Strength"].default_value = 0.88
    image_node = nodes.new(type="ShaderNodeTexImage")
    image_node.location = (-240, 0)
    image_node.image = bpy.data.images.load(str(TARGET_FRONT_CROP), check_existing=True)
    material.node_tree.links.new(image_node.outputs["Color"], emission.inputs["Color"])
    material.node_tree.links.new(emission.outputs["Emission"], output.inputs["Surface"])
    return material


def make_collection(name: str) -> bpy.types.Collection:
    collection = bpy.data.collections.new(name)
    bpy.context.scene.collection.children.link(collection)
    return collection


def add_extruded_trace_mesh(
    name: str,
    collection: bpy.types.Collection,
    points: list[tuple[int, int]],
    material: bpy.types.Material,
    front_y: float,
    depth: float,
    bevel_width: float,
    x_offset: float = 0.0,
    z_offset: float = 0.0,
    back_scale: float = 0.96,
) -> bpy.types.Object:
    front: list[int] = []
    back: list[int] = []
    verts: list[tuple[float, float, float]] = []
    world_points = [img_to_world(point, x_offset, z_offset) for point in points]
    center_x = sum(point[0] for point in world_points) / len(world_points)
    center_z = sum(point[1] for point in world_points) / len(world_points)
    for x, z in world_points:
        source_x = (x - x_offset) / WORLD_SCALE + (SOURCE_W * 0.5)
        source_y = SOURCE_BASELINE_Y - ((z - z_offset) / WORLD_SCALE)
        uv = (source_x / SOURCE_W, 1.0 - (source_y / SOURCE_H))
        front.append(len(verts))
        verts.append((x, front_y, z))
        back.append(len(verts))
        bx = center_x + ((x - center_x) * back_scale)
        bz = center_z + ((z - center_z) * back_scale)
        verts.append((bx, front_y + depth, bz))
        if "uvs" not in locals():
            uvs: list[tuple[float, float]] = []
        uvs.extend([uv, uv])

    faces: list[tuple[int, ...]] = [tuple(front), tuple(reversed(back))]
    for index in range(len(points)):
        next_index = (index + 1) % len(points)
        faces.append((front[index], back[index], back[next_index], front[next_index]))

    mesh = bpy.data.meshes.new(f"{name}_Mesh")
    mesh.from_pydata(verts, [], faces)
    mesh.update()
    uv_layer = mesh.uv_layers.new(name="UV0")
    for poly in mesh.polygons:
        for loop_index in poly.loop_indices:
            vertex_index = mesh.loops[loop_index].vertex_index
            uv_layer.data[loop_index].uv = uvs[vertex_index]
    obj = bpy.data.objects.new(name, mesh)
    obj.data.materials.append(material)
    collection.objects.link(obj)
    bpy.context.view_layer.objects.active = obj
    obj.select_set(True)
    if bevel_width > 0:
        bevel = obj.modifiers.new(f"{name}_BrokenEdgeBevel", "BEVEL")
        bevel.width = bevel_width
        bevel.segments = 1
        bevel.affect = "EDGES"
        bpy.ops.object.modifier_apply(modifier=bevel.name)
    bpy.ops.object.shade_flat()
    obj.select_set(False)
    return obj


def add_flat_polygon(
    name: str,
    collection: bpy.types.Collection,
    points: list[tuple[int, int]],
    material: bpy.types.Material,
    y: float,
    x_offset: float = 0.0,
    z_offset: float = 0.0,
) -> bpy.types.Object:
    world_points = [img_to_world(point, x_offset, z_offset) for point in points]
    verts = [(x, y, z) for x, z in world_points]
    mesh = bpy.data.meshes.new(f"{name}_Mesh")
    mesh.from_pydata(verts, [], [tuple(range(len(verts)))])
    mesh.update()
    uv_layer = mesh.uv_layers.new(name="UV0")
    for poly in mesh.polygons:
        for loop_index in poly.loop_indices:
            vertex_index = mesh.loops[loop_index].vertex_index
            source_x, source_z = world_points[vertex_index]
            px = (source_x - x_offset) / WORLD_SCALE + (SOURCE_W * 0.5)
            py = SOURCE_BASELINE_Y - ((source_z - z_offset) / WORLD_SCALE)
            uv_layer.data[loop_index].uv = (px / SOURCE_W, 1.0 - (py / SOURCE_H))
    obj = bpy.data.objects.new(name, mesh)
    obj.data.materials.append(material)
    obj["Aerathea.SurfaceTreatment"] = "camera_aligned_no_thickness_texture_mask_proof"
    try:
        obj.visible_shadow = False
    except AttributeError:
        pass
    collection.objects.link(obj)
    return obj


def add_stroke(
    name: str,
    collection: bpy.types.Collection,
    points: list[tuple[int, int]],
    material: bpy.types.Material,
    y: float,
    width: float,
    x_offset: float = 0.0,
    z_offset: float = 0.0,
) -> list[bpy.types.Object]:
    objects: list[bpy.types.Object] = []
    for index, (start, end) in enumerate(zip(points, points[1:])):
        sx, sz = img_to_world(start, x_offset, z_offset)
        ex, ez = img_to_world(end, x_offset, z_offset)
        dx = ex - sx
        dz = ez - sz
        length = math.hypot(dx, dz)
        if length < 0.01:
            continue
        nx = -dz / length
        nz = dx / length
        taper = 0.84 if index in {0, len(points) - 2} else 1.0
        half = width * taper * 0.5
        poly = [
            (sx + nx * half, y, sz + nz * half),
            (ex + nx * half, y, ez + nz * half),
            (ex - nx * half, y, ez - nz * half),
            (sx - nx * half, y, sz - nz * half),
        ]
        mesh = bpy.data.meshes.new(f"{name}_{index:02d}_Mesh")
        mesh.from_pydata(poly, [], [(0, 1, 2, 3)])
        mesh.update()
        obj = bpy.data.objects.new(f"{name}_{index:02d}", mesh)
        obj.data.materials.append(material)
        obj["Aerathea.SurfaceTreatment"] = "worn_oxide_pigment_camera_aligned_mask"
        try:
            obj.visible_shadow = False
        except AttributeError:
            pass
        collection.objects.link(obj)
        objects.append(obj)
    return objects


def add_rope(
    name: str,
    collection: bpy.types.Collection,
    points: list[tuple[int, int]],
    material: bpy.types.Material,
    y: float,
    radius: float,
) -> bpy.types.Object:
    curve = bpy.data.curves.new(f"{name}_Curve", "CURVE")
    curve.dimensions = "3D"
    curve.resolution_u = 2
    curve.bevel_depth = radius
    curve.bevel_resolution = 2
    curve.fill_mode = "FULL"
    spline = curve.splines.new("POLY")
    spline.points.add(len(points) - 1)
    for point, img_point in zip(spline.points, points):
        x, z = img_to_world(img_point)
        point.co = (x, y, z, 1.0)
    obj = bpy.data.objects.new(name, curve)
    obj.data.materials.append(material)
    collection.objects.link(obj)
    bpy.context.view_layer.objects.active = obj
    obj.select_set(True)
    bpy.ops.object.convert(target="MESH")
    obj = bpy.context.object
    obj.name = name
    bpy.ops.object.shade_flat()
    obj.select_set(False)
    return obj


def add_rubble(collection: bpy.types.Collection, material: bpy.types.Material) -> list[bpy.types.Object]:
    objects: list[bpy.types.Object] = []
    seeds = [
        (38, 293, 13, 8),
        (74, 300, 17, 9),
        (110, 304, 10, 6),
        (152, 309, 13, 8),
        (202, 313, 17, 9),
        (250, 307, 15, 8),
        (306, 300, 16, 9),
        (350, 292, 12, 7),
        (63, 248, 12, 8),
        (327, 249, 11, 8),
    ]
    for index, (px, py, sx, sz) in enumerate(seeds):
        points = [
            (px - sx, py + 2),
            (px - sx * 0.5, py - sz),
            (px + sx * 0.6, py - sz * 0.8),
            (px + sx, py + 3),
            (px + sx * 0.1, py + sz),
            (px - sx * 0.8, py + sz * 0.6),
        ]
        objects.append(add_extruded_trace_mesh(f"A20_Rubble_{index:02d}", collection, points, material, -48.0 - index * 0.08, 16.0, 0.5, back_scale=0.88))
    return objects


def configure_review_scene() -> tuple[bpy.types.Object, Vector]:
    world = bpy.context.scene.world or bpy.data.worlds.new("A20_ImageLockedWorld")
    bpy.context.scene.world = world
    world.color = (0.74, 0.72, 0.68)
    scene = bpy.context.scene
    try:
        scene.render.engine = "BLENDER_EEVEE"
        scene.eevee.use_gtao = True
        scene.eevee.gtao_distance = 1.4
        scene.eevee.gtao_factor = 0.10
        scene.eevee.taa_render_samples = 48
    except (AttributeError, TypeError):
        pass
    scene.view_settings.view_transform = "Standard"
    scene.view_settings.look = "None"
    scene.view_settings.exposure = 0.92
    scene.view_settings.gamma = 1.0
    scene.render.film_transparent = False

    bpy.ops.object.light_add(type="AREA", location=(-180, -320, 280))
    key = bpy.context.object
    key.name = "A20_Key_Area"
    key.data.energy = 68000.0
    key.data.size = 360.0

    bpy.ops.object.light_add(type="AREA", location=(200, -260, 190))
    fill = bpy.context.object
    fill.name = "A20_Fill_Area"
    fill.data.energy = 36000.0
    fill.data.size = 380.0

    target = Vector((0.0, -20.0, 86.0))
    bpy.ops.object.camera_add(location=(0.0, -525.0, 96.0))
    camera = bpy.context.object
    camera.name = "A20_ImageLockedReviewCamera"
    camera.data.type = "ORTHO"
    camera.data.ortho_scale = 285.0
    direction = target - camera.location
    camera.rotation_euler = direction.to_track_quat("-Z", "Y").to_euler()
    bpy.context.scene.camera = camera
    return camera, target


def render(camera: bpy.types.Object, path: Path) -> None:
    ensure_dir(path.parent)
    scene = bpy.context.scene
    scene.render.resolution_x = 960
    scene.render.resolution_y = 720
    scene.render.filepath = str(path)
    bpy.ops.render.render(write_still=True)


def main() -> None:
    clear_scene()
    setup_scene()
    materials = {
        "stone": make_material("M_A20_Stone_Mid", (0.315, 0.300, 0.260)),
        "stone_dark": make_material("M_A20_Stone_Dark", (0.205, 0.195, 0.170)),
        "stone_light": make_material("M_A20_Stone_Light", (0.56, 0.50, 0.38)),
        "earth": make_material("M_A20_Earth", (0.38, 0.235, 0.130)),
        "rawhide": make_material("M_A20_Rawhide", (0.48, 0.265, 0.110)),
        "red": make_material("M_A20_WornRedPigment", (0.39, 0.050, 0.036), 0.97),
    }
    materials["projection"] = make_projection_material()
    collection = make_collection(f"{ASSET_NAME}_A20_ImageLockedBlockout")

    guide_material = materials["projection"] if USE_TARGET_PROJECTION else materials["stone"]
    ground_material = materials["projection"] if USE_TARGET_PROJECTION else materials["earth"]
    rear_material = materials["projection"] if USE_TARGET_PROJECTION else materials["stone_dark"]

    add_extruded_trace_mesh("A20_GroundContact", collection, TRACE["ground"]["points"], ground_material, -4.0, 74.0, 0.4, z_offset=-5.0, back_scale=0.98)
    add_extruded_trace_mesh("A20_TallRearSlab", collection, TRACE["tall_rear_slab"]["points"], rear_material, 8.0, 32.0, 1.0, x_offset=-6.0, z_offset=2.0, back_scale=0.94)
    left_stack_stones = [
        [(34, 210), (70, 194), (135, 201), (144, 225), (58, 240), (25, 225)],
        [(39, 170), (80, 150), (145, 160), (153, 181), (98, 195), (35, 187)],
        [(60, 129), (77, 120), (96, 181), (83, 221), (53, 199)],
    ]
    for index, points in enumerate(left_stack_stones):
        add_extruded_trace_mesh(f"A20_LeftLashedStackStone_{index:02d}", collection, points, guide_material, -24.0 - index * 0.8, 30.0, 0.75, x_offset=-2.0, z_offset=-1.5, back_scale=0.92)
    add_extruded_trace_mesh("A20_RightBoundSupport", collection, TRACE["right_bound_support"]["points"], guide_material, -20.0, 36.0, 0.9, x_offset=3.0, z_offset=-1.0, back_scale=0.93)
    add_extruded_trace_mesh("A20_DominantFrontPaintedSlab", collection, TRACE["dominant_front_slab"]["points"], guide_material, -42.0, 40.0, 1.2, z_offset=-1.5, back_scale=0.94)

    if not USE_TARGET_PROJECTION:
        add_flat_polygon("A20_FrontSlabLowerShadowFacet", collection, [(92, 222), (130, 286), (226, 296), (250, 252), (188, 262), (132, 250)], materials["stone_dark"], -44.0)
        add_flat_polygon("A20_FrontSlabUpperLightFacet", collection, [(93, 134), (169, 108), (207, 128), (153, 156), (105, 164)], materials["stone_light"], -44.2)
        add_flat_polygon("A20_RightSupportDarkFacet", collection, [(325, 145), (345, 151), (348, 211), (322, 240), (331, 181)], materials["stone_dark"], -22.2)
        add_flat_polygon("A20_RearSlabLightFacet", collection, [(187, 27), (244, 44), (254, 88), (208, 80)], materials["stone_light"], 6.2)

    add_rubble(collection, materials["stone"])

    if not USE_TARGET_PROJECTION:
        for label, points in PAINT_GUIDES:
            if label == "rear slab paint":
                add_stroke(f"A20_Paint_{label.replace(' ', '_')}", collection, points, materials["red"], 5.5, 3.9, x_offset=-6.0, z_offset=2.0)
            else:
                add_stroke(f"A20_Paint_{label.replace(' ', '_')}", collection, points, materials["red"], -46.0, 4.8)

    for label, start, end in LOCK_LINES:
        if "rope zone" not in label:
            continue
        add_rope(f"A20_Rope_{label.replace(' ', '_')}", collection, [start, end], materials["rawhide"], -48.5, 0.88)
        sx, sz = img_to_world(start)
        ex, ez = img_to_world(end)
        for idx, (x, z) in enumerate([(sx, sz), (ex, ez)]):
            bpy.ops.mesh.primitive_uv_sphere_add(segments=8, ring_count=4, radius=2.2, location=(x, -50.0, z))
            knot = bpy.context.object
            knot.name = f"A20_RopeKnot_{label.replace(' ', '_')}_{idx}"
            knot.data.materials.append(materials["rawhide"])
            if knot.name not in collection.objects:
                collection.objects.link(knot)

    add_asset_metadata(
        ASSET_NAME,
        f"A20 image-locked DCC blockout proof pending visual review against {SOURCE_TARGET}",
        f"/Game/Aerathea/Props/Giants/BloodAxe/CairnTargets/A1/{ASSET_NAME}",
    )
    for obj in collection.objects:
        obj["Aerathea.Asset"] = ASSET_NAME
        obj["Aerathea.Status"] = "image_locked_blockout_proof_pending_visual_review"
        obj["Aerathea.SourceTarget"] = SOURCE_TARGET
        obj["Aerathea.NotGameReady"] = True

    camera, _target = configure_review_scene()
    render(camera, REVIEW_ROOT / f"{ASSET_NAME}_ImageLockedBlockout_A20.png")

    blend_path = BLEND_ROOT / f"{ASSET_NAME}_A20_ImageLockedBlockout.blend"
    ensure_dir(blend_path.parent)
    bpy.ops.wm.save_as_mainfile(filepath=str(blend_path))
    print(f"A20 image-locked blockout proof written: {REVIEW_ROOT / f'{ASSET_NAME}_ImageLockedBlockout_A20.png'}")


if __name__ == "__main__":
    main()
