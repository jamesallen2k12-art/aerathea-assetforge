#!/usr/bin/env python3
"""Build A08 Step 01 isolated pommel Attempt A05 in Blender only."""

from __future__ import annotations

import importlib.util
import math
from pathlib import Path
from typing import Any, List, Sequence, Tuple


ROOT = Path(__file__).resolve().parents[2]
BASE_PATH = ROOT / "Tools/DCC/build_siegebreaker_a08_pommel_a04.py"
spec = importlib.util.spec_from_file_location("siegebreaker_a08_pommel_a04", BASE_PATH)
if spec is None or spec.loader is None:
    raise RuntimeError("cannot load preserved A08 pommel A04 builder")
attempt = importlib.util.module_from_spec(spec)
spec.loader.exec_module(attempt)
base = attempt.base

base.OUTPUT_ROOT_REL = Path("SourceAssets/Blender/Weapons/Dwarven") / base.ASSET / "A08_BlenderOnly_Pommel_A05"
base.BLEND_REL = base.OUTPUT_ROOT_REL / f"{base.ASSET}_A08_Pommel_A05.blend"
base.MANIFEST_REL = Path("docs/assets/blueprints") / base.ASSET / "manifests/A08_STEP_01_POMMEL_A05_VALIDATION.json"
base.REVIEW_REL = Path("docs/assets/blueprints") / base.ASSET / "review/A08_STEP_01_POMMEL_A05_REVIEW.png"
base.SCRIPT_REL = Path("Tools/DCC/build_siegebreaker_a08_pommel_a05.py")


previous_source_crop_plane = base.source_crop_plane
previous_add_text = base.add_text
previous_diamond_prism = base.diamond_prism


def source_crop_plane(bpy: Any, material: Any, collection: Any) -> Any:
    obj = previous_source_crop_plane(bpy, material, collection)
    obj.location.y = -11.0
    obj["aerathea_review_depth_correction"] = "A05 source display only; source pixels unchanged"
    return obj


def add_text(bpy: Any, body: str, location: Tuple[float, float, float], size: float, material: Any, collection: Any) -> Any:
    obj = previous_add_text(bpy, body, location, size, material, collection)
    if body in {"AUTHORITATIVE SOURCE", "UNCHANGED CONCEPT UV WINDOW"}:
        obj.location.y = -10.0
    return obj


def append_beam_prism(
    vertices: List[Tuple[float, float, float]],
    faces: List[List[int]],
    point_a: Tuple[float, float],
    point_b: Tuple[float, float],
    width: float,
    y_back: float,
    y_front: float,
) -> None:
    ax, az = point_a
    bx, bz = point_b
    dx, dz = bx - ax, bz - az
    length = max(math.hypot(dx, dz), 1.0e-8)
    nx, nz = -dz / length * width * 0.5, dx / length * width * 0.5
    outline = [(ax + nx, az + nz), (bx + nx, bz + nz), (bx - nx, bz - nz), (ax - nx, az - nz)]
    start = len(vertices)
    vertices.extend([(x, y_back, z) for x, z in outline])
    vertices.extend([(x, y_front, z) for x, z in outline])
    faces.extend([[start, start + 3, start + 2, start + 1], [start + 4, start + 5, start + 6, start + 7]])
    for index in range(4):
        nxt = (index + 1) % 4
        faces.append([start + index, start + nxt, start + 4 + nxt, start + 4 + index])


def source_rune_mesh(bpy: Any, name: str, center_z: float, y_back: float, y_front: float, material: Any, collection: Any) -> Any:
    vertices: List[Tuple[float, float, float]] = []
    faces: List[List[int]] = []
    # Small upper diamond.
    upper_center = center_z + 1.05
    upper = [(-0.76, upper_center), (0.0, upper_center + 0.72), (0.76, upper_center), (0.0, upper_center - 0.72)]
    for first, second in zip(upper, upper[1:] + upper[:1]):
        append_beam_prism(vertices, faces, first, second, 0.24, y_back, y_front)
    # Narrow connector and the source-visible lower open loop.
    segments = [
        ((0.0, upper_center - 0.72), (0.0, center_z + 0.10)),
        ((0.0, center_z + 0.10), (-0.88, center_z - 0.52)),
        ((-0.88, center_z - 0.52), (-0.88, center_z - 1.38)),
        ((-0.88, center_z - 1.38), (0.0, center_z - 2.02)),
        ((0.0, center_z - 2.02), (0.88, center_z - 1.38)),
        ((0.88, center_z - 1.38), (0.88, center_z - 0.52)),
    ]
    for first, second in segments:
        append_beam_prism(vertices, faces, first, second, 0.24, y_back, y_front)
    return base.create_mesh(bpy, name, vertices, faces, material, collection)


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
    if "RuneCrystal" in name:
        return source_rune_mesh(bpy, name, center_z, y_back, y_front, material, collection)
    return previous_diamond_prism(bpy, name, center_z, width, height, y_back, y_front, material, collection)


base.source_crop_plane = source_crop_plane
base.add_text = add_text
base.diamond_prism = diamond_prism


if __name__ == "__main__":
    raise SystemExit(base.main())
