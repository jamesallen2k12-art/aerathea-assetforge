#!/usr/bin/env python3
"""Build A08 Step 01 isolated pommel Attempt A06 in Blender only."""

from __future__ import annotations

import importlib.util
from pathlib import Path
from typing import Any, List, Tuple


ROOT = Path(__file__).resolve().parents[2]
BASE_PATH = ROOT / "Tools/DCC/build_siegebreaker_a08_pommel_a05.py"
spec = importlib.util.spec_from_file_location("siegebreaker_a08_pommel_a05", BASE_PATH)
if spec is None or spec.loader is None:
    raise RuntimeError("cannot load preserved A08 pommel A05 builder")
attempt = importlib.util.module_from_spec(spec)
spec.loader.exec_module(attempt)
base = attempt.base

base.OUTPUT_ROOT_REL = Path("SourceAssets/Blender/Weapons/Dwarven") / base.ASSET / "A08_BlenderOnly_Pommel_A06"
base.BLEND_REL = base.OUTPUT_ROOT_REL / f"{base.ASSET}_A08_Pommel_A06.blend"
base.MANIFEST_REL = Path("docs/assets/blueprints") / base.ASSET / "manifests/A08_STEP_01_POMMEL_A06_VALIDATION.json"
base.REVIEW_REL = Path("docs/assets/blueprints") / base.ASSET / "review/A08_STEP_01_POMMEL_A06_REVIEW.png"
base.SCRIPT_REL = Path("Tools/DCC/build_siegebreaker_a08_pommel_a06.py")


previous_diamond_frame = base.diamond_frame


def plate_silver_material(bpy: Any) -> Any:
    existing = bpy.data.materials.get("M_A08_PlateSilver")
    if existing is not None:
        return existing
    material = bpy.data.materials.new("M_A08_PlateSilver")
    material.use_nodes = True
    shader = material.node_tree.nodes.get("Principled BSDF")
    shader.inputs["Base Color"].default_value = (0.16, 0.19, 0.24, 1.0)
    shader.inputs["Metallic"].default_value = 0.90
    shader.inputs["Roughness"].default_value = 0.20
    return material


def add_rivet(bpy: Any, name: str, x_value: float, z_value: float, material: Any, collection: Any) -> Any:
    bpy.ops.mesh.primitive_ico_sphere_add(subdivisions=1, radius=0.15, location=(x_value, -4.92, z_value))
    obj = bpy.context.active_object
    obj.name = name
    for linked in list(obj.users_collection):
        linked.objects.unlink(obj)
    collection.objects.link(obj)
    base.assign_material(obj, material)
    return obj


def panel_frame(
    bpy: Any,
    prefix: str,
    x0: float,
    x1: float,
    z0: float,
    z1: float,
    material: Any,
    collection: Any,
) -> List[Any]:
    y_value = -3.82
    depth = 0.24
    thickness = 0.22
    return [
        base.beam_between_xz(bpy, f"{prefix}_Top", (x0, z1), (x1, z1), y_value, depth, thickness, material, collection),
        base.beam_between_xz(bpy, f"{prefix}_Bottom", (x0, z0), (x1, z0), y_value, depth, thickness, material, collection),
        base.beam_between_xz(bpy, f"{prefix}_Outer", (x0, z0), (x0, z1), y_value, depth, thickness, material, collection),
        base.beam_between_xz(bpy, f"{prefix}_Inner", (x1, z0), (x1, z1), y_value, depth, thickness, material, collection),
    ]


def diamond_frame(
    bpy: Any,
    prefix: str,
    center_z: float,
    width: float,
    height: float,
    y_value: float,
    depth: float,
    thickness: float,
    material: Any,
    collection: Any,
) -> List[Any]:
    frame_material = plate_silver_material(bpy) if "BronzeFrame" in prefix else material
    objects = list(previous_diamond_frame(bpy, prefix, center_z, width, height, y_value, depth, thickness, frame_material, collection))
    if "BronzeFrame" not in prefix:
        return objects
    objects.extend(panel_frame(bpy, "SB_C006_LeftPanelFrame_A08", -4.78, -3.42, 7.8, 12.25, material, collection))
    objects.extend(panel_frame(bpy, "SB_C006_RightPanelFrame_A08", 3.42, 4.78, 7.8, 12.25, material, collection))
    rivet_positions = [(-2.65, 12.9), (2.65, 12.9), (-2.65, 7.45), (2.65, 7.45), (-4.10, 10.0), (4.10, 10.0)]
    for index, (x_value, z_value) in enumerate(rivet_positions, 1):
        objects.append(add_rivet(bpy, f"SB_C006_Pommel_Rivet_{index:02d}_A08", x_value, z_value, material, collection))
    return objects


base.diamond_frame = diamond_frame


if __name__ == "__main__":
    raise SystemExit(base.main())
