#!/usr/bin/env python3
"""Clean-import the A04 GLB with the official Blender runtime."""

from __future__ import annotations

import hashlib
import json
from pathlib import Path

import bpy
from mathutils import Vector


ROOT = Path(__file__).resolve().parents[2]
ASSET_ID = "SM_DRW_SiegeBreaker_Hammer_A01"
REVISION = "StrictScanline_A04"
GLB = ROOT / "SourceAssets/Exports/Weapons/Dwarven" / ASSET_ID / REVISION / f"{ASSET_ID}.glb"
OUT = ROOT / "Saved/Automation/DCC" / ASSET_ID / "VisualFidelity_A04" / f"{ASSET_ID}_A04_GLB_CleanImportAudit.json"
CM = 0.01


def sha256(path: Path) -> str:
    digest = hashlib.sha256()
    with path.open("rb") as handle:
        for block in iter(lambda: handle.read(1024 * 1024), b""):
            digest.update(block)
    return digest.hexdigest()


def triangles(obj: bpy.types.Object) -> int:
    obj.data.calc_loop_triangles()
    return len(obj.data.loop_triangles)


def bounds(objects: list[bpy.types.Object]) -> tuple[list[float], list[float], list[float]]:
    points = [obj.matrix_world @ Vector(corner) for obj in objects for corner in obj.bound_box]
    minimum = [min(point[index] for point in points) / CM for index in range(3)]
    maximum = [max(point[index] for point in points) / CM for index in range(3)]
    extent = [maximum[index] - minimum[index] for index in range(3)]
    return minimum, maximum, extent


def main() -> int:
    bpy.ops.wm.read_factory_settings(use_empty=True)
    bpy.ops.import_scene.gltf(filepath=str(GLB))
    meshes = [obj for obj in bpy.context.scene.objects if obj.type == "MESH"]
    minimum, maximum, extent = bounds(meshes)
    payload = {
        "schema": "aerathea.siegebreaker_a04_glb_clean_import.v1",
        "asset_id": ASSET_ID,
        "revision": REVISION,
        "status": "proof only",
        "runtime": bpy.app.version_string,
        "glb": str(GLB.relative_to(ROOT)),
        "sha256": sha256(GLB),
        "mesh_count": len(meshes),
        "triangles": sum(triangles(obj) for obj in meshes),
        "bounds_min_cm": minimum,
        "bounds_max_cm": maximum,
        "bounds_extent_cm": extent,
        "uv_meshes": sum(1 for obj in meshes if obj.data.uv_layers),
        "passed": (
            len(meshes) > 0
            and all(abs(observed - expected) <= 0.02 for observed, expected in zip(extent, (52.0, 32.0, 170.0)))
        ),
    }
    OUT.parent.mkdir(parents=True, exist_ok=True)
    OUT.write_text(json.dumps(payload, indent=2) + "\n", encoding="utf-8")
    print(OUT)
    print("A04 GLB CLEAN IMPORT:", "PASS" if payload["passed"] else "FAIL")
    return 0 if payload["passed"] else 2


if __name__ == "__main__":
    raise SystemExit(main())
