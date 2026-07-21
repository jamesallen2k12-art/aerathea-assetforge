#!/usr/bin/env python3
"""Render internal attempts or the single accepted A005 A02 final review image."""

from __future__ import annotations

import argparse
import hashlib
import json
import math
import sys
from pathlib import Path
from typing import Any, Dict, Iterable, List, Sequence, Tuple


ASSET = "SM_GIA_BloodAxeCairnstone_A005"
CONTRACT = "A005-CR-VISUAL-CORRECTION-A02"
ROOT = Path(__file__).resolve().parents[2]
OUTPUT_ROOT_REL = Path("Saved/Automation/DCC") / ASSET / "Production/VisualCorrection_A02"
FINAL_REL = OUTPUT_ROOT_REL / f"{ASSET}_FINAL_CORRECTED_3D_A02.png"
FINAL_RGBA_REL = OUTPUT_ROOT_REL / f"{ASSET}_FINAL_CORRECTED_3D_A02_OBJECT_RGBA.png"
FINAL_AUDIT_REL = OUTPUT_ROOT_REL / "FINAL_RENDER_AUDIT_A02.json"
MASK_MANIFEST_REL = Path("SourceAssets/Textures/Props/Giants/BloodAxe/Cairns") / ASSET / "Technical/SM_GIA_BloodAxeCairnstone_A005_SOURCE_MASK_MANIFEST_A01.json"


def blender_args() -> List[str]:
    return sys.argv[sys.argv.index("--") + 1 :] if "--" in sys.argv else sys.argv[1:]


def parse_args(argv: Sequence[str]) -> argparse.Namespace:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--mode", choices=("attempt", "final"), required=True)
    parser.add_argument("--attempt-name", default="Attempt01")
    return parser.parse_args(list(argv))


def sha256_file(path: Path) -> str:
    digest = hashlib.sha256()
    with path.open("rb") as handle:
        for block in iter(lambda: handle.read(1024 * 1024), b""):
            digest.update(block)
    return digest.hexdigest()


def look_at(obj: Any, target: Sequence[float]) -> None:
    from mathutils import Vector  # type: ignore

    direction = Vector(target) - obj.location
    obj.rotation_euler = direction.to_track_quat("-Z", "Y").to_euler()


def area_light(bpy: Any, name: str, location: Sequence[float], energy: float, size: float) -> Any:
    data = bpy.data.lights.new(name, "AREA")
    data.energy = energy
    data.shape = "DISK"
    data.size = size
    data.color = (1.0, 1.0, 1.0)
    data.use_shadow = True
    if hasattr(data, "use_contact_shadow"):
        data.use_contact_shadow = True
    obj = bpy.data.objects.new(name, data)
    bpy.context.scene.collection.objects.link(obj)
    obj.location = location
    look_at(obj, (0.0, 0.0, 105.0))
    return obj


def quantile(values: Sequence[int], fraction: float) -> int:
    if not values:
        return 0
    ordered = sorted(values)
    index = max(0, min(len(ordered) - 1, int(round((len(ordered) - 1) * fraction))))
    return int(ordered[index])


def median_rgb(pixels: Sequence[Tuple[int, int, int]]) -> List[int]:
    if not pixels:
        return [0, 0, 0]
    return [quantile([pixel[channel] for pixel in pixels], 0.5) for channel in range(3)]


def luminance(pixel: Tuple[int, int, int]) -> int:
    return int(round(0.2126 * pixel[0] + 0.7152 * pixel[1] + 0.0722 * pixel[2]))


def red_pixel(pixel: Tuple[int, int, int]) -> bool:
    return pixel[0] - max(pixel[1], pixel[2]) >= 18 and pixel[0] >= 50


def population_metrics(pixels: Sequence[Tuple[int, int, int]]) -> Dict[str, Any]:
    luma = [luminance(pixel) for pixel in pixels]
    return {
        "pixels": len(pixels),
        "median_rgb": median_rgb(pixels),
        "luminance": {
            "p10": quantile(luma, 0.10),
            "p50": quantile(luma, 0.50),
            "p90": quantile(luma, 0.90),
        },
    }


def displayed_color_metrics(render_rgba: Any) -> Dict[str, Any]:
    from PIL import Image

    mask_manifest = json.loads((ROOT / MASK_MANIFEST_REL).read_text(encoding="utf-8"))
    front = next(record for record in mask_manifest["records"] if record["view"] == "front")
    source = Image.open(ROOT / front["source_path"]).convert("RGB")
    source_mask = Image.open(ROOT / front["mask_path"]).convert("L")
    source_pixels = [
        pixel
        for pixel, owned in zip(source.getdata(), source_mask.getdata())
        if owned > 0
    ]
    render_pixels = [
        pixel[:3]
        for pixel in render_rgba.getdata()
        if pixel[3] >= 128
    ]
    source_stone = [pixel for pixel in source_pixels if not red_pixel(pixel)]
    source_red = [pixel for pixel in source_pixels if red_pixel(pixel)]
    render_stone = [pixel for pixel in render_pixels if not red_pixel(pixel)]
    render_red = [pixel for pixel in render_pixels if red_pixel(pixel)]
    source_stone_metrics = population_metrics(source_stone)
    render_stone_metrics = population_metrics(render_stone)
    source_red_metrics = population_metrics(source_red)
    render_red_metrics = population_metrics(render_red)
    median_delta = [
        render_stone_metrics["median_rgb"][index] - source_stone_metrics["median_rgb"][index]
        for index in range(3)
    ]
    return {
        "source_front_owned": {
            "all": population_metrics(source_pixels),
            "stone": source_stone_metrics,
            "red": source_red_metrics,
            "red_fraction": len(source_red) / max(1, len(source_pixels)),
        },
        "rendered_object": {
            "all": population_metrics(render_pixels),
            "stone": render_stone_metrics,
            "red": render_red_metrics,
            "red_fraction": len(render_red) / max(1, len(render_pixels)),
        },
        "stone_median_rgb_delta_render_minus_source": median_delta,
        "stone_median_rgb_distance": math.sqrt(sum(value * value for value in median_delta)),
        "stone_luminance_delta": {
            key: render_stone_metrics["luminance"][key] - source_stone_metrics["luminance"][key]
            for key in ("p10", "p50", "p90")
        },
    }


def alpha_bounds(image: Any) -> Dict[str, Any]:
    alpha = image.getchannel("A")
    bbox = alpha.point(lambda value: 255 if value >= 16 else 0).getbbox()
    if bbox is None:
        raise RuntimeError("A02 render contains no visible object pixels")
    left, top, right, bottom = bbox
    return {
        "bbox_half_open_px": [left, top, right, bottom],
        "margins_px": {
            "left": left,
            "top": top,
            "right": image.width - right,
            "bottom": image.height - bottom,
        },
        "coverage_fraction": sum(1 for value in alpha.getdata() if value >= 16) / (image.width * image.height),
    }


def projection_record(scene: Any, camera: Any) -> Dict[str, Any]:
    from bpy_extras.object_utils import world_to_camera_view  # type: ignore
    from mathutils import Vector  # type: ignore

    rows: Dict[str, float] = {}
    for label, z_value in (("ground", 0.0), ("apron_top", 10.0), ("lower_top", 23.0), ("upper_top", 35.0), ("asset_top", 220.0)):
        projected = world_to_camera_view(scene, camera, Vector((0.0, 0.0, z_value)))
        rows[label] = (1.0 - float(projected.y)) * scene.render.resolution_y
    return {
        "centerline_rows_px": rows,
        "band_heights_px": {
            "C004_APRON_0_10": abs(rows["ground"] - rows["apron_top"]),
            "C003_LOWER_10_23": abs(rows["apron_top"] - rows["lower_top"]),
            "C002_UPPER_23_35": abs(rows["lower_top"] - rows["upper_top"]),
        },
    }


def composite_background(rgba: Any) -> Any:
    from PIL import Image

    top = (196, 200, 205)
    bottom = (132, 138, 146)
    background = Image.new("RGB", rgba.size)
    pixels: List[Tuple[int, int, int]] = []
    for y in range(rgba.height):
        alpha = y / max(1, rgba.height - 1)
        color = tuple(int(round(top[index] * (1.0 - alpha) + bottom[index] * alpha)) for index in range(3))
        pixels.extend([color] * rgba.width)
    background.putdata(pixels)
    return Image.composite(rgba.convert("RGB"), background, rgba.getchannel("A"))


def main() -> int:
    args = parse_args(blender_args())
    import bpy  # type: ignore
    from PIL import Image

    lod0 = bpy.data.objects.get(f"{ASSET}_LOD0")
    if lod0 is None:
        raise RuntimeError("A02 LOD0 missing")
    for obj in list(bpy.context.scene.objects):
        if obj.type == "MESH" and obj != lod0:
            obj.hide_render = True
            obj.hide_viewport = True
        if obj.type in {"LIGHT", "CAMERA"}:
            bpy.data.objects.remove(obj, do_unlink=True)
    lod0.hide_render = False
    lod0.hide_viewport = False

    world = bpy.context.scene.world
    if world is None:
        world = bpy.data.worlds.new("A005_A02_REVIEW_WORLD")
        bpy.context.scene.world = world
    world.use_nodes = True
    background = world.node_tree.nodes.get("Background")
    background.inputs["Color"].default_value = (0.8, 0.8, 0.8, 1.0)
    background.inputs["Strength"].default_value = 0.0

    area_light(bpy, "A005_A02_KEY", (235.0, -350.0, 330.0), 1560000.0, 310.0)
    area_light(bpy, "A005_A02_FILL", (-245.0, -285.0, 225.0), 864000.0, 360.0)
    area_light(bpy, "A005_A02_FRONT", (0.0, -430.0, 125.0), 600000.0, 330.0)
    area_light(bpy, "A005_A02_RIM", (160.0, 270.0, 300.0), 432000.0, 260.0)

    camera_data = bpy.data.cameras.new("A005_A02_FINAL_REVIEW_CAMERA")
    camera = bpy.data.objects.new("A005_A02_FINAL_REVIEW_CAMERA", camera_data)
    bpy.context.scene.collection.objects.link(camera)
    camera.location = (0.0, -565.0, 182.0)
    camera_data.lens = 67.0
    camera_data.sensor_width = 36.0
    camera_data.dof.use_dof = False
    look_at(camera, (0.0, 0.0, 108.0))
    bpy.context.scene.camera = camera

    scene = bpy.context.scene
    scene.render.engine = "BLENDER_EEVEE"
    scene.eevee.use_gtao = True
    scene.eevee.gtao_distance = 5.0
    scene.eevee.gtao_factor = 1.1
    scene.eevee.taa_render_samples = 160
    scene.render.resolution_x = 1400
    scene.render.resolution_y = 1600
    scene.render.resolution_percentage = 100
    scene.render.image_settings.file_format = "PNG"
    scene.render.image_settings.color_mode = "RGBA"
    scene.render.film_transparent = True
    scene.view_settings.view_transform = "Standard"
    scene.view_settings.look = "None"
    scene.view_settings.exposure = 0.0
    scene.view_settings.gamma = 1.0

    if args.mode == "final":
        rgba_rel = FINAL_RGBA_REL
        output_rel = FINAL_REL
        audit_rel = FINAL_AUDIT_REL
    else:
        attempt_root = OUTPUT_ROOT_REL / "InternalAttempts"
        rgba_rel = attempt_root / f"{args.attempt_name}_OBJECT_RGBA.png"
        output_rel = attempt_root / f"{args.attempt_name}.png"
        audit_rel = attempt_root / f"{args.attempt_name}_AUDIT.json"
    for rel in (rgba_rel, output_rel, audit_rel):
        (ROOT / rel).parent.mkdir(parents=True, exist_ok=True)

    scene.render.filepath = str(ROOT / rgba_rel)
    bpy.ops.render.render(write_still=True)
    rgba = Image.open(ROOT / rgba_rel).convert("RGBA")
    final = composite_background(rgba)
    final.save(ROOT / output_rel, format="PNG")

    gray = final.convert("L")
    histogram = gray.histogram()
    pixel_count = final.width * final.height
    audit = {
        "schema": "aerathea.a005_visual_correction_a02_render_audit.v1",
        "asset_id": ASSET,
        "contract_id": CONTRACT,
        "status": "render_complete_pending_a02_independent_audit",
        "mode": args.mode,
        "path": str(output_rel),
        "object_rgba_path": str(rgba_rel),
        "size": list(final.size),
        "sha256": sha256_file(ROOT / output_rel),
        "rgb_extrema": [list(value) for value in final.getextrema()],
        "mean_luminance": sum(index * count for index, count in enumerate(histogram)) / pixel_count,
        "near_black_fraction": sum(histogram[:20]) / pixel_count,
        "near_white_fraction": sum(histogram[235:]) / pixel_count,
        "camera_location_cm": list(camera.location),
        "camera_target_cm": [0.0, 0.0, 108.0],
        "orientation": "upright source-matched front with slight top reveal",
        "review_markers": 0,
        "collision_visible": 0,
        "lod_visible": "LOD0 only",
        "background": "clean neutral gradient; no ground intersection",
        "color_management": {"view_transform": "Standard", "look": "None", "exposure": 0.0, "gamma": 1.0},
        "lights": "four neutral-white area lights; no colored lights",
        "alpha_bounds": alpha_bounds(rgba),
        "base_projection": projection_record(scene, camera),
        "displayed_color": displayed_color_metrics(rgba),
    }
    (ROOT / audit_rel).write_text(json.dumps(audit, indent=2) + "\n", encoding="utf-8")
    print(json.dumps(audit, indent=2))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
