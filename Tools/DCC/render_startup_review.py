#!/usr/bin/env python3
"""Render the Aerathea startup asset cluster from the review camera.

Run with:
    blender --background --python Tools/DCC/render_startup_review.py
"""

from __future__ import annotations

import math
import os
import sys
from pathlib import Path

import bpy
from mathutils import Vector


ROOT = Path(__file__).resolve().parents[2]
SHOW_REVIEW_MARKERS = os.environ.get("AET_REVIEW_MARKERS", "").lower() in {"1", "true", "yes", "on"}
DEFAULT_OUTPUT_PATH = ROOT / "Saved/Automation/StartupReview/AeratheaStartupReview_DCCCameraRetry.png"
if SHOW_REVIEW_MARKERS:
    DEFAULT_OUTPUT_PATH = ROOT / "Saved/Automation/StartupReview/AeratheaStartupReview_DCCMarkers.png"
OUTPUT_PATH = Path(os.environ.get("AET_REVIEW_OUTPUT", str(DEFAULT_OUTPUT_PATH)))

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
from Tools.DCC.build_next_slice_assets import (  # noqa: E402
    aether_shield_projector,
    aether_shield_wall,
    gear_mace,
    palisade_corner,
    palisade_endcap,
    palisade_gate,
    palisade_post,
    palisade_wall,
    ratchet_cleaver,
    tool_pack,
)
from Tools.DCC.generate_first_slice_meshes import ground_tile  # noqa: E402
from Tools.review_alignment_markers import REVIEW_ALIGNMENT_MARKERS  # noqa: E402


REVIEW_LOCATION = Vector((-4850.0, 3200.0, 2575.0))
REVIEW_TARGET = Vector((-70.0, 160.0, 110.0))
REVIEW_FOV_DEGREES = 65.0


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


def mesh_to_blender(
    mesh,
    name: str,
    location: tuple[float, float, float],
    yaw_degrees: float = 0.0,
    scale: tuple[float, float, float] = (1.0, 1.0, 1.0),
) -> None:
    parent = bpy.data.objects.new(name, None)
    parent.empty_display_type = "PLAIN_AXES"
    parent.location = location
    parent.rotation_euler[2] = math.radians(yaw_degrees)
    parent.scale = scale
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
    mesh_to_blender(ratchet_cleaver(), "AET_PROD_MKG_RatchetCleaver_A01", (-540, 282, 45), 16.0)
    mesh_to_blender(gear_mace(), "AET_PROD_MKG_GearMace_A01", (-620, 365, 45), -12.0)
    mesh_to_blender(tool_pack(), "AET_PROD_MKG_ToolPack_BackFit_A01", (-745, 520, 74), 0.0)
    add_shieldwall()

    mesh_to_blender(palisade_wall(), "AET_PROD_Palisade_Wall_A01", (-200, -660, 0))
    mesh_to_blender(palisade_post(), "AET_PROD_Palisade_Post_A01", (-430, -660, 0))
    mesh_to_blender(palisade_endcap(), "AET_PROD_Palisade_EndCap_A01", (70, -660, 0))
    mesh_to_blender(palisade_corner(), "AET_PROD_Palisade_Corner_A01", (360, -660, 0))
    mesh_to_blender(palisade_gate(), "AET_PROD_Palisade_Gate_A01", (140, -1020, 0))


def add_shieldwall() -> None:
    projector_mesh = aether_shield_projector()
    shield_mesh = aether_shield_wall()
    origin = Vector((260.0, 165.0, 0.0))
    active_projectors = 3
    shield_width = 700.0
    arc_height = 340.0
    segment_length = shield_width / float(active_projectors - 1)
    projector_center = float(active_projectors - 1) * 0.5

    for index in range(active_projectors):
        normalized = (float(index) - projector_center) / projector_center
        location = (
            origin.x - 55.0 * abs(normalized),
            origin.y + (float(index) - projector_center) * segment_length,
            origin.z,
        )
        mesh_to_blender(
            projector_mesh,
            f"AET_PROD_GNM_HeavyMekShieldwall_A01_Projector_{index + 1:02d}",
            location,
            -normalized * 14.0,
        )

    for index in range(active_projectors - 1):
        mid_index = float(index) + 0.5
        normalized = (mid_index - projector_center) / projector_center
        location = (
            origin.x + 32.0 - 24.0 * abs(normalized),
            origin.y + (mid_index - projector_center) * segment_length,
            origin.z,
        )
        mesh_to_blender(
            shield_mesh,
            f"AET_PROD_GNM_HeavyMekShieldwall_A01_ShieldPanel_{index + 1:02d}",
            location,
            -normalized * 8.0,
            (1.0, segment_length / 170.0, arc_height / 340.0),
        )


def add_review_alignment_markers() -> None:
    if not SHOW_REVIEW_MARKERS:
        return

    label_material = get_material("M_AET_ReviewMarker_Label", (1.0, 1.0, 1.0))
    for marker in REVIEW_ALIGNMENT_MARKERS:
        marker_id = marker["id"]
        x, y, z = marker["location"]
        # FBX export/import keeps the asset view aligned after an XY axis swap.
        dcc_location = (y, x, z)
        color = marker["color"]
        material = get_material(f"M_AET_ReviewMarker_{marker_id}", color[:3])

        bpy.ops.mesh.primitive_uv_sphere_add(
            segments=32,
            ring_count=16,
            radius=48.0 if marker_id != "E" else 62.0,
            location=dcc_location,
        )
        sphere = bpy.context.object
        sphere.name = f"AET_REVIEW_MARKER_{marker_id}"
        sphere.data.materials.append(material)

        curve = bpy.data.curves.new(f"AET_REVIEW_MARKER_LABEL_{marker_id}", "FONT")
        curve.body = marker["label"]
        curve.align_x = "CENTER"
        curve.align_y = "CENTER"
        curve.size = 145.0 if marker_id != "E" else 170.0
        label = bpy.data.objects.new(f"AET_REVIEW_MARKER_LABEL_{marker_id}", curve)
        label.location = (dcc_location[0], dcc_location[1], dcc_location[2] + 115.0)
        label.data.materials.append(label_material)
        bpy.context.collection.objects.link(label)


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
    add_review_alignment_markers()
    setup_camera_and_lights()
    render()


if __name__ == "__main__":
    main()
