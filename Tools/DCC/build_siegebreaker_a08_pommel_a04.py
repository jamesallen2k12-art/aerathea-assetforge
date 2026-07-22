#!/usr/bin/env python3
"""Build A08 Step 01 isolated pommel Attempt A04 in Blender only."""

from __future__ import annotations

import importlib.util
from pathlib import Path
from typing import Any, Tuple


ROOT = Path(__file__).resolve().parents[2]
BASE_PATH = ROOT / "Tools/DCC/build_siegebreaker_a08_pommel_a03.py"
spec = importlib.util.spec_from_file_location("siegebreaker_a08_pommel_a03", BASE_PATH)
if spec is None or spec.loader is None:
    raise RuntimeError("cannot load preserved A08 pommel A03 builder")
attempt = importlib.util.module_from_spec(spec)
spec.loader.exec_module(attempt)
base = attempt.base

base.OUTPUT_ROOT_REL = Path("SourceAssets/Blender/Weapons/Dwarven") / base.ASSET / "A08_BlenderOnly_Pommel_A04"
base.BLEND_REL = base.OUTPUT_ROOT_REL / f"{base.ASSET}_A08_Pommel_A04.blend"
base.MANIFEST_REL = Path("docs/assets/blueprints") / base.ASSET / "manifests/A08_STEP_01_POMMEL_A04_VALIDATION.json"
base.REVIEW_REL = Path("docs/assets/blueprints") / base.ASSET / "review/A08_STEP_01_POMMEL_A04_REVIEW.png"
base.SCRIPT_REL = Path("Tools/DCC/build_siegebreaker_a08_pommel_a04.py")


previous_material_principled = base.material_principled
previous_diamond_prism = base.diamond_prism
previous_diamond_frame = base.diamond_frame
previous_beam = base.beam_between_xz
previous_torus = base.add_torus
previous_cylinder = base.add_cylinder
previous_ring_loft = base.ring_loft


def material_principled(
    bpy: Any,
    name: str,
    color: Tuple[float, float, float, float],
    metallic: float,
    roughness: float,
    emission: Tuple[float, float, float, float] | None = None,
    emission_strength: float = 0.0,
) -> Any:
    if name == "M_A08_BlueRune":
        color = (0.012, 0.12, 0.32, 1.0)
        emission = (0.008, 0.18, 0.72, 1.0)
        emission_strength = 1.25
    if name == "M_A08_BlackenedSteel":
        color = (0.095, 0.12, 0.16, 1.0)
        roughness = 0.23
    return previous_material_principled(bpy, name, color, metallic, roughness, emission, emission_strength)


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
    if "FrontRecess" in name:
        center_z, width, height = 10.2, 6.9, 8.6
    elif "SteelInset" in name:
        center_z, width, height = 10.2, 5.65, 7.1
    elif "RuneCrystal" in name:
        center_z, width, height = 10.15, 2.55, 4.05
    return previous_diamond_prism(bpy, name, center_z, width, height, y_back, y_front, material, collection)


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
) -> Any:
    if "BronzeFrame" in prefix:
        center_z, width, height, thickness = 10.2, 7.25, 9.0, 0.46
    elif "SteelFrame" in prefix:
        center_z, width, height, thickness = 10.2, 5.95, 7.45, 0.30
    return previous_diamond_frame(bpy, prefix, center_z, width, height, y_value, depth, thickness, material, collection)


def beam_between_xz(
    bpy: Any,
    name: str,
    point_a: Tuple[float, float],
    point_b: Tuple[float, float],
    y_value: float,
    depth: float,
    thickness: float,
    material: Any,
    collection: Any,
) -> Any:
    if "UpperBrace" in name:
        y_value, depth, thickness = -3.25, 0.30, 0.42
        if "Left" in name:
            point_a, point_b = (-3.85, 14.2), (-2.65, 16.6)
        else:
            point_a, point_b = (3.85, 14.2), (2.65, 16.6)
    elif "LowerBrace" in name:
        y_value, depth, thickness = -3.15, 0.28, 0.34
        if "Left" in name:
            point_a, point_b = (-3.75, 6.4), (-2.65, 4.2)
        else:
            point_a, point_b = (3.75, 6.4), (2.65, 4.2)
    return previous_beam(bpy, name, point_a, point_b, y_value, depth, thickness, material, collection)


def add_torus(bpy: Any, name: str, major_radius: float, minor_radius: float, z_value: float, material: Any, collection: Any) -> Any:
    if "LowerForgedBand" in name:
        major_radius, minor_radius, z_value = 3.72, 0.28, 4.65
    elif "ShoulderBand" in name:
        major_radius, minor_radius, z_value = 4.38, 0.30, 14.55
    return previous_torus(bpy, name, major_radius, minor_radius, z_value, material, collection)


def add_cylinder(bpy: Any, name: str, radius: float, depth: float, z_value: float, material: Any, collection: Any, vertices: int = 16) -> Any:
    if "UpperCollar" in name:
        return base.ring_loft(
            bpy,
            name,
            ((15.25, 4.35, 3.65), (16.0, 4.72, 3.82), (16.55, 3.72, 3.18), (16.85, 3.35, 2.92)),
            12,
            material,
            collection,
        )
    return previous_cylinder(bpy, name, radius, depth, z_value, material, collection, vertices)


def ring_loft(
    bpy: Any,
    name: str,
    profiles: Any,
    segments: int,
    material: Any,
    collection: Any,
    phase: float = 0.39269908169872414,
) -> Any:
    if "FacetedBody" in name:
        phase = 0.0
    return previous_ring_loft(bpy, name, profiles, segments, material, collection, phase)


base.material_principled = material_principled
base.diamond_prism = diamond_prism
base.diamond_frame = diamond_frame
base.beam_between_xz = beam_between_xz
base.add_torus = add_torus
base.ring_loft = ring_loft
base.add_cylinder = add_cylinder


if __name__ == "__main__":
    raise SystemExit(base.main())
