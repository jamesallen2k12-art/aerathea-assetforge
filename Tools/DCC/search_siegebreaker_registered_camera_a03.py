"""Render a bounded A03 camera grid for pixel-registered silhouette selection.

This is a proof-only search.  It never alters the asset, geometry, materials,
or source pixels; it varies only distance, yaw, and pitch around the locked
primary 3/4 orientation.
"""

from __future__ import annotations

import importlib.util
import json
import math
from pathlib import Path

import bpy


ROOT = Path(__file__).resolve().parents[2]
ASSET_ID = "SM_DRW_SiegeBreaker_Hammer_A01"
BLEND_PATH = ROOT / "SourceAssets/Blender/Weapons/Dwarven" / ASSET_ID / f"{ASSET_ID}_DCCGameReady_PixelReconstruction_A03.blend"
OUTPUT = ROOT / "Saved/Automation/DCC" / ASSET_ID / "VisualFidelity_A03/camera_search"


def load_renderer():
    path = ROOT / "Tools/DCC/render_siegebreaker_pixel_reconstruction_a03.py"
    spec = importlib.util.spec_from_file_location("siegebreaker_a03_renderer", path)
    if spec is None or spec.loader is None:
        raise RuntimeError(f"Cannot load renderer: {path}")
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


def main() -> int:
    renderer = load_renderer()
    OUTPUT.mkdir(parents=True, exist_ok=True)
    bpy.ops.wm.open_mainfile(filepath=str(BLEND_PATH))
    scene = bpy.context.scene
    renderer.source_objects()
    scene.camera = renderer.camera("CAM_SB_A03_SEARCH", (-1.3, -2.72, 2.04), (0.0, 0.0, 0.91), 70.0)
    renderer.configure(scene, 360, 480, False)
    scene.cycles.samples = 1
    scene.cycles.use_denoising = False
    # Alpha is the measured authority for this search; simple illumination is
    # retained so each proof remains human-readable if inspected.
    renderer.area("SB_A03_SearchKey", (-2.7, -3.2, 4.2), 420.0, 3.0, (1.0, 0.72, 0.43))
    renderer.area("SB_A03_SearchFill", (3.2, -2.1, 2.5), 220.0, 4.0, (0.40, 0.58, 1.0))
    target_z = 0.91
    baseline_distance = math.hypot(1.30, 2.72)
    records = []
    for distance in (2.35, 2.50, 2.65):
        for yaw_deg in (47.0, 50.0, 53.0):
            for pitch_deg in (22.5, 24.0, 25.5):
                yaw = math.radians(yaw_deg)
                pitch = math.radians(pitch_deg)
                location = (
                    -distance * math.sin(yaw),
                    -distance * math.cos(yaw),
                    target_z + distance * math.tan(pitch),
                )
                lens = 70.0 * distance / baseline_distance
                cam = renderer.camera("CAM_SB_A03_SEARCH", location, (0.0, 0.0, target_z), lens=lens)
                scene.camera = cam
                key = f"d{distance:.3f}_y{yaw_deg:.1f}_p{pitch_deg:.1f}".replace(".", "p")
                path = OUTPUT / f"{key}.png"
                scene.render.filepath = str(path)
                bpy.ops.render.render(write_still=True)
                records.append({
                    "key": key,
                    "path": str(path.relative_to(ROOT)),
                    "distance_m": distance,
                    "yaw_deg": yaw_deg,
                    "pitch_deg": pitch_deg,
                    "location_m": [round(value, 8) for value in location],
                    "target_m": [0.0, 0.0, target_z],
                    "lens_mm": round(lens, 8),
                })
    manifest = {
        "schema": "aerathea.siegebreaker.camera_search.v1",
        "asset_id": ASSET_ID,
        "revision": "PixelReconstruction_A03",
        "contract_id": "SB-VF-A03-PIXEL",
        "artifact_status": "proof only",
        "asset_changed": False,
        "variables": ["camera_distance", "camera_yaw", "camera_pitch"],
        "renders": records,
    }
    manifest_path = OUTPUT / "camera_search_manifest.json"
    manifest_path.write_text(json.dumps(manifest, indent=2) + "\n", encoding="utf-8")
    print(manifest_path)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
