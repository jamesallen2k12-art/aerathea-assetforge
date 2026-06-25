#!/usr/bin/env python3
"""Render the Aerathea startup asset cluster from the review camera.

Run with:
    blender --background --python Tools/DCC/render_startup_review.py
"""

from __future__ import annotations

import math
import sys
from pathlib import Path

import bpy
from mathutils import Vector


ROOT = Path(__file__).resolve().parents[2]
OUTPUT_PATH = ROOT / "Saved/Automation/StartupReview/AeratheaStartupReview_DCCCameraRetry.png"

sys.path.insert(0, str(ROOT))

from Tools.DCC.build_aerathea_blender_assets import (  # noqa: E402
    aether_core_unit,
    aether_knife,
    aetherium_grenade,
    portal_arch,
    spark_pistol,
    target_dummy,
    workshop_crate,
)
from Tools.DCC.generate_first_slice_meshes import ground_tile  # noqa: E402


REVIEW_LOCATION = Vector((-2350.0, 1600.0, 1280.0))
REVIEW_TARGET = Vector((-70.0, 160.0, 110.0))
REVIEW_FOV_DEGREES = 70.0


def clear_scene() -> None:
    bpy.ops.object.select_all(action="SELECT")
    bpy.ops.object.delete()


def setup_scene() -> None:
    scene = bpy.context.scene
    scene.unit_settings.system = "METRIC"
    scene.unit_settings.scale_length = 0.01
    scene.render.resolution_x = 1280
    scene.render.resolution_y = 720
    scene.render.film_transparent = False
    if "Filmic" in scene.view_settings.bl_rna.properties["view_transform"].enum_items:
        scene.view_settings.view_transform = "Filmic"
    else:
        scene.view_settings.view_transform = "Standard"
    look_items = scene.view_settings.bl_rna.properties["look"].enum_items
    if "Medium High Contrast" in look_items:
        scene.view_settings.look = "Medium High Contrast"
    scene.view_settings.exposure = 0.0
    scene.view_settings.gamma = 1.0
    try:
        scene.render.engine = "BLENDER_EEVEE_NEXT"
        scene.eevee.taa_render_samples = 64
    except Exception:
        scene.render.engine = "BLENDER_EEVEE"
        scene.eevee.taa_render_samples = 64
    world = scene.world or bpy.data.worlds.new("World")
    scene.world = world
    world.color = (0.035, 0.038, 0.045)


def get_material(name: str, color: tuple[float, float, float]) -> bpy.types.Material:
    material = bpy.data.materials.get(name)
    if material is not None:
        return material

    material = bpy.data.materials.new(name)
    material.diffuse_color = (color[0], color[1], color[2], 1.0)
    material.use_nodes = True
    bsdf = material.node_tree.nodes.get("Principled BSDF")
    if bsdf is not None:
        bsdf.inputs["Base Color"].default_value = (color[0], color[1], color[2], 1.0)
        bsdf.inputs["Roughness"].default_value = 0.82
        if "Aetherium" in name or "Glow" in name:
            bsdf.inputs["Emission Color"].default_value = (0.0, 0.85, 2.8, 1.0)
            bsdf.inputs["Emission Strength"].default_value = 1.8
    return material


def mesh_to_blender(mesh, name: str, location: tuple[float, float, float], yaw_degrees: float = 0.0) -> None:
    parent = bpy.data.objects.new(name, None)
    parent.empty_display_type = "PLAIN_AXES"
    parent.location = location
    parent.rotation_euler[2] = math.radians(yaw_degrees)
    bpy.context.collection.objects.link(parent)

    materials = {mat_name: get_material(mat_name, color) for mat_name, color in mesh.materials.items()}
    for source_obj in mesh.objects:
        if source_obj.name.startswith("UCX_"):
            continue
        blender_mesh = bpy.data.meshes.new(f"{name}_{source_obj.name}")
        faces = [tuple(index - 1 for index in face) for face in source_obj.faces]
        blender_mesh.from_pydata(source_obj.verts, [], faces)
        blender_mesh.update()

        obj = bpy.data.objects.new(f"{name}_{source_obj.name}", blender_mesh)
        obj.parent = parent
        obj.data.materials.append(materials[source_obj.material])
        for polygon in obj.data.polygons:
            polygon.material_index = 0
        bpy.context.collection.objects.link(obj)


def add_startup_assets() -> None:
    tile_mesh = ground_tile()
    for row, y in enumerate(range(-800, 801, 400), start=1):
        for col, x in enumerate(range(-800, 801, 400), start=1):
            mesh_to_blender(tile_mesh, f"AET_PROD_GroundTile_A01_R{row}_C{col}", (x, y, -8))

    mesh_to_blender(target_dummy(), "AET_PROD_TargetDummy_A01", (-50, 350, 0))
    mesh_to_blender(portal_arch(), "AET_PROD_Portal_A01", (350, 0, 0))
    mesh_to_blender(workshop_crate(), "AET_PROD_WorkshopCrate_A01", (-235, 260, 0))
    mesh_to_blender(aether_knife(), "AET_PROD_MKG_AetherKnife_A01", (-395, 190, 42), 18.0)
    mesh_to_blender(spark_pistol(), "AET_PROD_MKG_SparkPistol_A01", (-465, 190, 50), -15.0)
    mesh_to_blender(aether_core_unit(), "AET_PROD_MKG_AetherCoreUnit_A01", (-360, 270, 28), 12.0)
    mesh_to_blender(aetherium_grenade(), "AET_PROD_MKG_AetheriumGrenade_A01", (-455, 275, 24), -10.0)


def look_at(obj: bpy.types.Object, target: Vector) -> None:
    direction = target - obj.location
    obj.rotation_euler = direction.to_track_quat("-Z", "Y").to_euler()


def setup_camera_and_lights() -> None:
    camera_data = bpy.data.cameras.new("AET_PROD_Camera_Review_A01")
    camera = bpy.data.objects.new("AET_PROD_Camera_Review_A01", camera_data)
    camera.location = REVIEW_LOCATION
    camera_data.angle = math.radians(REVIEW_FOV_DEGREES)
    camera_data.lens = 28
    camera_data.clip_end = 100000.0
    look_at(camera, REVIEW_TARGET)
    bpy.context.collection.objects.link(camera)
    bpy.context.scene.camera = camera

    sun_data = bpy.data.lights.new("AET_BOOT_KeyLight_Directional", "SUN")
    sun = bpy.data.objects.new("AET_BOOT_KeyLight_Directional", sun_data)
    sun.rotation_euler = (math.radians(40), math.radians(0), math.radians(-35))
    sun_data.energy = 3.2
    bpy.context.collection.objects.link(sun)

    fill_data = bpy.data.lights.new("AET_PROD_ReviewFillLight_A01", "AREA")
    fill = bpy.data.objects.new("AET_PROD_ReviewFillLight_A01", fill_data)
    fill.location = (-420, -520, 760)
    fill_data.energy = 700
    fill_data.size = 900
    bpy.context.collection.objects.link(fill)


def render() -> None:
    OUTPUT_PATH.parent.mkdir(parents=True, exist_ok=True)
    bpy.context.scene.render.filepath = str(OUTPUT_PATH)
    bpy.ops.render.render(write_still=True)
    print(f"Rendered {OUTPUT_PATH.relative_to(ROOT)}")


def main() -> None:
    clear_scene()
    setup_scene()
    add_startup_assets()
    setup_camera_and_lights()
    render()


if __name__ == "__main__":
    main()
