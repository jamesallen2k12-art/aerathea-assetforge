#!/usr/bin/env python3
"""Render the internal A05 orthographic, beauty, and parallax proof set."""

from __future__ import annotations

import hashlib
import json
import math
from pathlib import Path

import bpy
from mathutils import Vector


ROOT = Path(bpy.path.abspath("//")).parents[5]
ASSET_ID = "SM_DRW_SiegeBreaker_Hammer_A01"
OUT = ROOT / "SourceAssets/Proofs/Weapons/Dwarven/SM_DRW_SiegeBreaker_Hammer_A01/OrthographicVolumetric_A05"
MANIFEST = OUT / f"{ASSET_ID}_A05_RENDER_MANIFEST.json"


def sha256(path: Path) -> str:
    digest = hashlib.sha256()
    with path.open("rb") as handle:
        for chunk in iter(lambda: handle.read(1024 * 1024), b""):
            digest.update(chunk)
    return digest.hexdigest()


def target_object(obj, target):
    direction = Vector(target) - obj.location
    obj.rotation_euler = direction.to_track_quat("-Z", "Y").to_euler()


def make_camera():
    data = bpy.data.cameras.new("A05_ReviewCamera_Data")
    camera = bpy.data.objects.new("A05_ReviewCamera", data)
    bpy.context.scene.collection.objects.link(camera)
    bpy.context.scene.camera = camera
    return camera


def add_area(name, location, energy, size, color):
    data = bpy.data.lights.new(name + "_Data", "AREA")
    data.energy = energy
    data.size = size
    data.color = color
    light = bpy.data.objects.new(name, data)
    light.location = location
    bpy.context.scene.collection.objects.link(light)
    target_object(light, (0.0, 0.0, 0.95))
    return light


def configure_scene():
    scene = bpy.context.scene
    scene.render.engine = "BLENDER_EEVEE"
    scene.eevee.use_gtao = True
    scene.eevee.gtao_distance = 3.0
    scene.eevee.gtao_factor = 1.25
    scene.eevee.use_soft_shadows = True
    scene.render.resolution_x = 760
    scene.render.resolution_y = 1040
    scene.render.resolution_percentage = 100
    scene.render.image_settings.file_format = "PNG"
    scene.render.image_settings.color_mode = "RGBA"
    scene.render.film_transparent = False
    scene.render.use_file_extension = True
    scene.world.color = (0.012, 0.016, 0.024)
    try:
        scene.view_settings.view_transform = "Filmic"
        scene.view_settings.look = "Medium High Contrast"
        scene.view_settings.exposure = -0.15
        scene.view_settings.gamma = 1.0
    except Exception:
        pass
    scene.camera.data.dof.use_dof = False


def add_stage():
    bpy.ops.mesh.primitive_plane_add(size=9.0, location=(0.0, 0.0, -0.006))
    plane = bpy.context.object
    plane.name = "A05_RenderOnly_Ground"
    material = bpy.data.materials.new("A05_RenderOnly_GroundMaterial")
    material.use_nodes = True
    bsdf = material.node_tree.nodes.get("Principled BSDF")
    bsdf.inputs["Base Color"].default_value = (0.015, 0.020, 0.029, 1.0)
    bsdf.inputs["Roughness"].default_value = 0.72
    plane.data.materials.append(material)

    add_area("A05_Key", (2.4, -3.2, 3.4), 620.0, 3.0, (0.78, 0.88, 1.0))
    add_area("A05_Fill", (-3.4, -1.2, 2.1), 360.0, 2.8, (0.45, 0.62, 1.0))
    add_area("A05_WarmRim", (2.0, 3.2, 2.8), 520.0, 2.4, (1.0, 0.52, 0.24))
    add_area("A05_Top", (-0.8, 0.6, 4.5), 420.0, 2.0, (0.65, 0.78, 1.0))
    add_area("A05_LowerFill", (-1.2, -2.2, 0.65), 240.0, 1.8, (1.0, 0.58, 0.32))


def render(camera, name, position, target, projection, scale_or_lens, resolution=(760, 1040)):
    scene = bpy.context.scene
    ground = bpy.data.objects.get("A05_RenderOnly_Ground")
    if ground:
        ground.hide_render = name == "BOTTOM"
    camera.location = position
    target_object(camera, target)
    camera.data.type = projection
    if projection == "ORTHO":
        camera.data.ortho_scale = scale_or_lens
    else:
        camera.data.lens = scale_or_lens
    scene.render.resolution_x, scene.render.resolution_y = resolution
    path = OUT / f"{ASSET_ID}_A05_{name}.png"
    scene.render.filepath = str(path)
    bpy.ops.render.render(write_still=True)
    if ground:
        ground.hide_render = False
    return path


def main():
    OUT.mkdir(parents=True, exist_ok=True)
    camera = make_camera()
    configure_scene()
    add_stage()

    records = {}
    views = {
        "FRONT": ((0.0, -4.2, 0.88), (0.0, 0.0, 0.86), "ORTHO", 1.88, (760, 1040)),
        "BACK": ((0.0, 4.2, 0.88), (0.0, 0.0, 0.86), "ORTHO", 1.88, (760, 1040)),
        "LEFT": ((-4.2, 0.0, 0.88), (0.0, 0.0, 0.86), "ORTHO", 1.88, (760, 1040)),
        "RIGHT": ((4.2, 0.0, 0.88), (0.0, 0.0, 0.86), "ORTHO", 1.88, (760, 1040)),
        "TOP": ((0.0, 0.0, 4.2), (0.0, 0.0, 1.51), "ORTHO", 0.62, (760, 760)),
        "BOTTOM": ((0.0, 0.0, -3.5), (0.0, 0.0, 1.51), "ORTHO", 0.62, (760, 760)),
        "BEAUTY": ((2.05, -2.80, 2.30), (0.0, 0.0, 0.94), "PERSP", 62.0, (960, 1200)),
    }
    for name, args in views.items():
        path = render(camera, name, *args)
        records[name] = {"path": str(path.relative_to(ROOT)), "sha256": sha256(path), "camera_position": list(args[0]), "target": list(args[1]), "projection": args[2], "scale_or_lens": args[3]}

    parallax = []
    for index, angle_deg in enumerate((-60, -30, 0, 30, 60)):
        angle = math.radians(angle_deg - 90)
        radius = 3.25
        position = (radius * math.cos(angle), radius * math.sin(angle), 2.0)
        path = render(camera, f"PARALLAX_{index + 1:02d}", position, (0.0, 0.0, 1.0), "PERSP", 64.0, (620, 760))
        parallax.append({"path": str(path.relative_to(ROOT)), "sha256": sha256(path), "yaw_deg": angle_deg})

    manifest = {
        "schema": "aerathea.siegebreaker_a05_render_set.v1",
        "asset_id": ASSET_ID,
        "artifact_status": "proof only",
        "blend": str(Path(bpy.data.filepath).relative_to(ROOT)),
        "views": records,
        "parallax": parallax,
        "render_engine": "BLENDER_EEVEE",
        "fixed_object": True,
        "intermediate_review_visibility": "internal only",
    }
    MANIFEST.write_text(json.dumps(manifest, indent=2) + "\n", encoding="utf-8")
    print(json.dumps({"status": "pass", "renders": len(records) + len(parallax), "manifest": str(MANIFEST)}, indent=2))


if __name__ == "__main__":
    main()
