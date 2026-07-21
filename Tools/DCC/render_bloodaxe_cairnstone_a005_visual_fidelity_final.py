#!/usr/bin/env python3
"""Render the single final A005 visual-fidelity recovery approval image."""

from __future__ import annotations

import json
import math
from pathlib import Path
from typing import Any, Sequence, Tuple


ASSET = "SM_GIA_BloodAxeCairnstone_A005"
ROOT = Path(__file__).resolve().parents[2]
OUTPUT_REL = Path("Saved/Automation/DCC") / ASSET / "Production/VisualFidelityRecovery_A01" / f"{ASSET}_FINAL_GAME_READY_ASSET.png"
AUDIT_REL = Path("Saved/Automation/DCC") / ASSET / "Production/VisualFidelityRecovery_A01" / "FINAL_RENDER_AUDIT.json"


def look_at(obj: Any, target: Sequence[float]) -> None:
    from mathutils import Vector  # type: ignore

    direction = Vector(target) - obj.location
    obj.rotation_euler = direction.to_track_quat("-Z", "Y").to_euler()


def material(bpy: Any, name: str, color: Tuple[float, float, float, float], roughness: float) -> Any:
    value = bpy.data.materials.new(name)
    value.use_nodes = True
    shader = value.node_tree.nodes.get("Principled BSDF")
    shader.inputs["Base Color"].default_value = color
    shader.inputs["Roughness"].default_value = roughness
    shader.inputs["Metallic"].default_value = 0.0
    return value


def area_light(bpy: Any, name: str, location: Sequence[float], energy: float, size: float, color: Sequence[float]) -> Any:
    data = bpy.data.lights.new(name, "AREA")
    data.energy = energy
    data.shape = "DISK"
    data.size = size
    data.color = color
    data.use_shadow = True
    data.use_contact_shadow = True
    obj = bpy.data.objects.new(name, data)
    bpy.context.scene.collection.objects.link(obj)
    obj.location = location
    look_at(obj, (0.0, 0.0, 100.0))
    return obj


def main() -> int:
    import bpy  # type: ignore

    lod0 = bpy.data.objects.get(f"{ASSET}_LOD0")
    if lod0 is None:
        raise RuntimeError("LOD0 missing")
    for obj in list(bpy.context.scene.objects):
        if obj.type == "MESH" and obj != lod0:
            obj.hide_render = True
            obj.hide_viewport = True
    lod0.hide_render = False
    lod0.hide_viewport = False

    bpy.ops.mesh.primitive_plane_add(size=900.0, location=(0.0, 0.0, -0.35))
    ground = bpy.context.object
    ground.name = "A005_FINAL_REVIEW_GROUND"
    ground.data.materials.append(material(bpy, "M_A005_FinalReviewGround", (0.13, 0.145, 0.17, 1.0), 0.78))

    world = bpy.context.scene.world
    if world is None:
        world = bpy.data.worlds.new("A005_FINAL_REVIEW_WORLD")
        bpy.context.scene.world = world
    world.use_nodes = True
    background = world.node_tree.nodes.get("Background")
    background.inputs["Color"].default_value = (0.13, 0.155, 0.20, 1.0)
    background.inputs["Strength"].default_value = 0.82

    area_light(bpy, "A005_KEY", (270.0, -330.0, 380.0), 8500.0, 230.0, (1.0, 0.77, 0.62))
    area_light(bpy, "A005_FILL", (-260.0, -210.0, 245.0), 5200.0, 280.0, (0.56, 0.70, 1.0))
    area_light(bpy, "A005_RIM", (180.0, 300.0, 315.0), 6500.0, 210.0, (0.82, 0.90, 1.0))
    area_light(bpy, "A005_FRONT_SOFT", (0.0, -410.0, 135.0), 3400.0, 200.0, (1.0, 0.52, 0.42))

    camera_data = bpy.data.cameras.new("A005_FINAL_REVIEW_CAMERA")
    camera = bpy.data.objects.new("A005_FINAL_REVIEW_CAMERA", camera_data)
    bpy.context.scene.collection.objects.link(camera)
    camera.location = (0.0, -565.0, 230.0)
    camera_data.lens = 67.0
    camera_data.sensor_width = 36.0
    camera_data.dof.use_dof = False
    look_at(camera, (0.0, 0.0, 106.0))
    bpy.context.scene.camera = camera

    scene = bpy.context.scene
    scene.render.engine = "BLENDER_EEVEE"
    scene.eevee.use_gtao = True
    scene.eevee.gtao_distance = 5.0
    scene.eevee.gtao_factor = 1.35
    scene.eevee.taa_render_samples = 160
    scene.render.resolution_x = 1400
    scene.render.resolution_y = 1600
    scene.render.resolution_percentage = 100
    scene.render.image_settings.file_format = "PNG"
    scene.render.film_transparent = False
    scene.view_settings.view_transform = "Standard"
    scene.view_settings.look = "None"
    scene.view_settings.exposure = 1.80
    scene.view_settings.gamma = 1.0
    scene.render.filepath = str(ROOT / OUTPUT_REL)
    (ROOT / OUTPUT_REL).parent.mkdir(parents=True, exist_ok=True)
    bpy.ops.render.render(write_still=True)

    from PIL import Image

    image = Image.open(ROOT / OUTPUT_REL).convert("RGB")
    extrema = image.getextrema()
    luminance = image.convert("L")
    histogram = luminance.histogram()
    pixels = image.width * image.height
    mean_luma = sum(index * count for index, count in enumerate(histogram)) / pixels
    dark_fraction = sum(histogram[:20]) / pixels
    light_fraction = sum(histogram[235:]) / pixels
    audit = {
        "schema": "aerathea.a005_final_render_audit.v1",
        "asset_id": ASSET,
        "status": "render_complete_pending_visual_fidelity_audit",
        "path": str(OUTPUT_REL),
        "size": list(image.size),
        "rgb_extrema": [list(value) for value in extrema],
        "mean_luminance": mean_luma,
        "near_black_fraction": dark_fraction,
        "near_white_fraction": light_fraction,
        "camera_location_cm": list(camera.location),
        "camera_target_cm": [0.0, 0.0, 106.0],
        "orientation": "upright source-matched front with slight top reveal",
        "review_markers": 0,
        "collision_visible": 0,
        "lod_visible": "LOD0 only",
    }
    (ROOT / AUDIT_REL).write_text(json.dumps(audit, indent=2) + "\n", encoding="utf-8")
    print(json.dumps(audit, indent=2))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
