#!/usr/bin/env python3
"""Build A08 Step 01 isolated pommel Attempt A03 in Blender only."""

from __future__ import annotations

import importlib.util
import math
from pathlib import Path
from typing import Any


ROOT = Path(__file__).resolve().parents[2]
BASE_PATH = ROOT / "Tools/DCC/build_siegebreaker_a08_pommel_a02.py"
spec = importlib.util.spec_from_file_location("siegebreaker_a08_pommel_a02", BASE_PATH)
if spec is None or spec.loader is None:
    raise RuntimeError("cannot load preserved A08 pommel A02 builder")
attempt = importlib.util.module_from_spec(spec)
spec.loader.exec_module(attempt)
base = attempt.base

base.OUTPUT_ROOT_REL = Path("SourceAssets/Blender/Weapons/Dwarven") / base.ASSET / "A08_BlenderOnly_Pommel_A03"
base.BLEND_REL = base.OUTPUT_ROOT_REL / f"{base.ASSET}_A08_Pommel_A03.blend"
base.MANIFEST_REL = Path("docs/assets/blueprints") / base.ASSET / "manifests/A08_STEP_01_POMMEL_A03_VALIDATION.json"
base.REVIEW_REL = Path("docs/assets/blueprints") / base.ASSET / "review/A08_STEP_01_POMMEL_A03_REVIEW.png"
base.SCRIPT_REL = Path("Tools/DCC/build_siegebreaker_a08_pommel_a03.py")


def configure_camera(bpy: Any, collection: Any) -> Any:
    camera_data = bpy.data.cameras.new("A08_Pommel_Review_Camera")
    camera = bpy.data.objects.new("A08_Pommel_Review_Camera", camera_data)
    collection.objects.link(camera)
    camera.location = (0.0, -60.0, 9.0)
    camera.rotation_euler = (math.radians(90.0), 0.0, 0.0)
    camera.data.type = "ORTHO"
    camera.data.ortho_scale = 46.0
    bpy.context.scene.camera = camera
    return camera


base.configure_camera = configure_camera


if __name__ == "__main__":
    raise SystemExit(base.main())
