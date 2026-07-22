#!/usr/bin/env python3
"""Build A08 Step 01 isolated pommel Attempt A02 in Blender only."""

from __future__ import annotations

import importlib.util
import math
from pathlib import Path
from typing import Any, Sequence, Tuple


ROOT = Path(__file__).resolve().parents[2]
BASE_PATH = ROOT / "Tools/DCC/build_siegebreaker_a08_pommel_a01.py"
spec = importlib.util.spec_from_file_location("siegebreaker_a08_pommel_a01", BASE_PATH)
if spec is None or spec.loader is None:
    raise RuntimeError("cannot load preserved A08 pommel A01 builder")
base = importlib.util.module_from_spec(spec)
spec.loader.exec_module(base)

base.OUTPUT_ROOT_REL = Path("SourceAssets/Blender/Weapons/Dwarven") / base.ASSET / "A08_BlenderOnly_Pommel_A02"
base.BLEND_REL = base.OUTPUT_ROOT_REL / f"{base.ASSET}_A08_Pommel_A02.blend"
base.MANIFEST_REL = Path("docs/assets/blueprints") / base.ASSET / "manifests/A08_STEP_01_POMMEL_A02_VALIDATION.json"
base.REVIEW_REL = Path("docs/assets/blueprints") / base.ASSET / "review/A08_STEP_01_POMMEL_A02_REVIEW.png"
base.SCRIPT_REL = Path("Tools/DCC/build_siegebreaker_a08_pommel_a02.py")


original_material_principled = base.material_principled
original_diamond_prism = base.diamond_prism
original_add_area_light = base.add_area_light


def material_principled(
    bpy: Any,
    name: str,
    color: Tuple[float, float, float, float],
    metallic: float,
    roughness: float,
    emission: Tuple[float, float, float, float] | None = None,
    emission_strength: float = 0.0,
) -> Any:
    overrides = {
        "M_A08_AgedBronze": (0.38, 0.18, 0.055, 1.0),
        "M_A08_BlackenedSteel": (0.065, 0.085, 0.12, 1.0),
        "M_A08_Recess": (0.012, 0.018, 0.030, 1.0),
    }
    return original_material_principled(
        bpy,
        name,
        overrides.get(name, color),
        metallic,
        min(0.42, roughness + 0.05),
        emission,
        emission_strength,
    )


def diamond_prism(
    bpy: Any,
    name: str,
    center_z: float,
    width: float,
    height: float,
    y_back: float,
    y_front: float,
    material: Any,
    collection: Any,
) -> Any:
    if "RuneCrystal" not in name:
        return original_diamond_prism(bpy, name, center_z, width, height, y_back, y_front, material, collection)
    inner_width = width * 0.58
    inner_height = height * 0.58
    outer = [(-width * 0.5, center_z), (0.0, center_z + height * 0.5), (width * 0.5, center_z), (0.0, center_z - height * 0.5)]
    inner = [(-inner_width * 0.5, center_z), (0.0, center_z + inner_height * 0.5), (inner_width * 0.5, center_z), (0.0, center_z - inner_height * 0.5)]
    vertices = (
        [(x, y_back, z) for x, z in outer]
        + [(x, y_back, z) for x, z in inner]
        + [(x, y_front, z) for x, z in outer]
        + [(x, y_front, z) for x, z in inner]
    )
    faces = []
    for index in range(4):
        nxt = (index + 1) % 4
        faces.append([8 + index, 8 + nxt, 12 + nxt, 12 + index])
        faces.append([index, 4 + index, 4 + nxt, nxt])
        faces.append([index, nxt, 8 + nxt, 8 + index])
        faces.append([4 + index, 12 + index, 12 + nxt, 4 + nxt])
    return base.create_mesh(bpy, name, vertices, faces, material, collection)


def source_crop_plane(bpy: Any, material: Any, collection: Any) -> Any:
    source_width = 1122.0
    source_height = 1402.0
    crop = {"left": 462.0, "top": 1052.0, "right": 674.0, "bottom": 1318.0}
    display_height = 18.0
    display_width = display_height * (crop["right"] - crop["left"]) / (crop["bottom"] - crop["top"])
    center_x = -10.5
    center_z = 9.0
    half_width = display_width * 0.5
    half_height = display_height * 0.5
    vertices = [
        (center_x - half_width, 1.0, center_z - half_height),
        (center_x + half_width, 1.0, center_z - half_height),
        (center_x + half_width, 1.0, center_z + half_height),
        (center_x - half_width, 1.0, center_z + half_height),
    ]
    obj = base.create_mesh(bpy, "Immutable_Source_Pommel_Display", vertices, [[0, 1, 2, 3]], material, collection)
    uv_layer = obj.data.uv_layers.new(name="UVMap")
    coordinates = [
        (crop["left"] / source_width, 1.0 - crop["bottom"] / source_height),
        (crop["right"] / source_width, 1.0 - crop["bottom"] / source_height),
        (crop["right"] / source_width, 1.0 - crop["top"] / source_height),
        (crop["left"] / source_width, 1.0 - crop["top"] / source_height),
    ]
    for loop_index, uv in enumerate(coordinates):
        uv_layer.data[loop_index].uv = uv
    obj["aerathea_source_path"] = str(base.SOURCE_REL)
    obj["aerathea_source_sha256"] = base.SOURCE_SHA256
    obj["aerathea_display_crop_pixels"] = str(crop)
    obj["aerathea_source_mutated"] = False
    return obj


def configure_camera(bpy: Any, collection: Any) -> Any:
    camera_data = bpy.data.cameras.new("A08_Pommel_Review_Camera")
    camera = bpy.data.objects.new("A08_Pommel_Review_Camera", camera_data)
    collection.objects.link(camera)
    camera.location = (0.0, -60.0, 10.0)
    camera.rotation_euler = (math.radians(90.0), 0.0, 0.0)
    camera.data.type = "ORTHO"
    camera.data.ortho_scale = 27.0
    bpy.context.scene.camera = camera
    return camera


def add_area_light(
    bpy: Any,
    name: str,
    location: Tuple[float, float, float],
    energy: float,
    size: float,
    collection: Any,
    target: Tuple[float, float, float],
) -> Any:
    return original_add_area_light(bpy, name, location, energy * 1.85, size, collection, target)


base.material_principled = material_principled
base.diamond_prism = diamond_prism
base.source_crop_plane = source_crop_plane
base.configure_camera = configure_camera
base.add_area_light = add_area_light


if __name__ == "__main__":
    raise SystemExit(base.main())
