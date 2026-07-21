#!/usr/bin/env python3
"""Render A005 A04 internal proofs or the single eligible final review image."""

from __future__ import annotations

import argparse
import hashlib
import json
import math
import sys
from pathlib import Path
from typing import Any, Dict, List, Sequence, Tuple


ROOT = Path(__file__).resolve().parents[2]
ASSET = "SM_GIA_BloodAxeCairnstone_A005"
CONTRACT = "A005-CR-VISUAL-CORRECTION-A04"
SOURCE_PANEL_REL = Path("docs/assets/blueprints") / ASSET / "panels/STEP_03" / f"{ASSET}_STEP_03_FRONT.png"
MASK_MANIFEST_REL = Path("SourceAssets/Textures/Props/Giants/BloodAxe/Cairns") / ASSET / "Technical" / f"{ASSET}_SOURCE_MASK_MANIFEST_A01.json"
OUTPUT_ROOT_REL = Path("Saved/Automation/DCC") / ASSET / "Production/VisualCorrection_A04"
FINAL_REL = OUTPUT_ROOT_REL / f"{ASSET}_FINAL_CORRECTED_3D_A04.png"
FINAL_RGBA_REL = OUTPUT_ROOT_REL / f"{ASSET}_FINAL_CORRECTED_3D_A04_OBJECT_RGBA.png"
FINAL_AUDIT_REL = OUTPUT_ROOT_REL / "FINAL_RENDER_AUDIT_A04.json"


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


def load_json(rel: Path) -> Dict[str, Any]:
    with (ROOT / rel).open("r", encoding="utf-8") as handle:
        return json.load(handle)


def look_at(obj: Any, target: Sequence[float]) -> None:
    from mathutils import Vector  # type: ignore

    obj.rotation_euler = (Vector(target) - obj.location).to_track_quat("-Z", "Y").to_euler()


def clear_scene_support(bpy: Any, lod0: Any) -> None:
    for obj in list(bpy.context.scene.objects):
        if obj.type == "MESH" and obj != lod0:
            obj.hide_render = True
            obj.hide_viewport = True
        if obj.type in {"LIGHT", "CAMERA"}:
            bpy.data.objects.remove(obj, do_unlink=True)
    lod0.hide_render = False
    lod0.hide_viewport = False


def remove_lights(bpy: Any) -> None:
    for obj in list(bpy.context.scene.objects):
        if obj.type == "LIGHT":
            bpy.data.objects.remove(obj, do_unlink=True)


def area_light(bpy: Any, name: str, location: Sequence[float], energy: float, size: float) -> Any:
    data = bpy.data.lights.new(name, "AREA")
    data.energy = energy
    data.size = size
    obj = bpy.data.objects.new(name, data)
    bpy.context.scene.collection.objects.link(obj)
    obj.location = location
    look_at(obj, (0.0, 0.0, 105.0))
    return obj


def make_camera(
    bpy: Any,
    name: str,
    location: Sequence[float],
    target: Sequence[float],
    lens: float = 72.0,
    ortho_scale: float = 0.0,
) -> Any:
    data = bpy.data.cameras.new(name)
    obj = bpy.data.objects.new(name, data)
    bpy.context.scene.collection.objects.link(obj)
    obj.location = location
    look_at(obj, target)
    if ortho_scale > 0.0:
        data.type = "ORTHO"
        data.ortho_scale = ortho_scale
    else:
        data.lens = lens
        data.sensor_width = 36.0
    data.dof.use_dof = False
    bpy.context.scene.camera = obj
    return obj


def configure_scene(scene: Any, resolution: Tuple[int, int], transparent: bool = True) -> None:
    scene.render.engine = "BLENDER_EEVEE"
    scene.eevee.use_gtao = True
    scene.eevee.gtao_distance = 3.0
    scene.eevee.gtao_factor = 0.72
    scene.eevee.taa_render_samples = 192
    scene.render.resolution_x = resolution[0]
    scene.render.resolution_y = resolution[1]
    scene.render.resolution_percentage = 100
    scene.render.image_settings.file_format = "PNG"
    scene.render.image_settings.color_mode = "RGBA"
    scene.render.film_transparent = transparent
    scene.view_settings.view_transform = "Standard"
    scene.view_settings.look = "None"
    scene.view_settings.exposure = 0.0
    scene.view_settings.gamma = 1.0


def render_png(bpy: Any, rel: Path) -> Any:
    from PIL import Image

    path = ROOT / rel
    path.parent.mkdir(parents=True, exist_ok=True)
    bpy.context.scene.render.filepath = str(path)
    bpy.ops.render.render(write_still=True)
    return Image.open(path).convert("RGBA")


def alpha_bounds(image: Any) -> Dict[str, Any]:
    alpha = image.getchannel("A")
    bbox = alpha.point(lambda value: 255 if value >= 16 else 0).getbbox()
    if bbox is None:
        raise RuntimeError("A04 render contains no visible object pixels")
    left, top, right, bottom = bbox
    return {
        "bbox_half_open_px": [left, top, right, bottom],
        "margins_px": {"left": left, "top": top, "right": image.width - right, "bottom": image.height - bottom},
        "coverage_fraction": sum(1 for value in alpha.getdata() if value >= 16) / (image.width * image.height),
    }


def shadeless_material(bpy: Any, source_material: Any) -> Any:
    material = bpy.data.materials.new("M_A005_A04_INTERNAL_SHADELESS")
    material.use_nodes = True
    nodes = material.node_tree.nodes
    links = material.node_tree.links
    nodes.clear()
    output = nodes.new("ShaderNodeOutputMaterial")
    emission = nodes.new("ShaderNodeEmission")
    image = nodes.new("ShaderNodeTexImage")
    source_node = next(node for node in source_material.node_tree.nodes if node.bl_idname == "ShaderNodeTexImage" and node.name == "A04_DIRECT_SOURCE_BASECOLOR")
    image.image = source_node.image
    image.interpolation = "Linear"
    image.extension = "EXTEND"
    links.new(image.outputs["Color"], emission.inputs["Color"])
    links.new(emission.outputs["Emission"], output.inputs["Surface"])
    return material


def median_rgb(pixels: Sequence[Tuple[int, int, int]]) -> List[int]:
    if not pixels:
        return [0, 0, 0]
    return [sorted(pixel[channel] for pixel in pixels)[len(pixels) // 2] for channel in range(3)]


def color_metrics(image: Any) -> Dict[str, Any]:
    pixels: List[Tuple[int, int, int]] = []
    red: List[Tuple[int, int, int]] = []
    stone: List[Tuple[int, int, int]] = []
    for r_value, g_value, b_value, alpha in image.getdata():
        if alpha < 16:
            continue
        pixel = (r_value, g_value, b_value)
        pixels.append(pixel)
        if r_value >= g_value * 1.45 and r_value >= b_value * 1.30 and r_value - min(g_value, b_value) >= 18:
            red.append(pixel)
        else:
            stone.append(pixel)
    return {
        "pixels": len(pixels),
        "median_rgb": median_rgb(pixels),
        "stone_median_rgb": median_rgb(stone),
        "red_median_rgb": median_rgb(red),
        "red_fraction": len(red) / max(1, len(pixels)),
    }


def source_front_metrics() -> Dict[str, Any]:
    from PIL import Image

    manifest = load_json(MASK_MANIFEST_REL)
    record = next(item for item in manifest["records"] if item["view"] == "front")
    panel = Image.open(ROOT / SOURCE_PANEL_REL).convert("RGB")
    mask = Image.open(ROOT / record["mask_path"]).convert("L")
    rgba = Image.new("RGBA", panel.size)
    rgba.putdata([(*pixel, owned) for pixel, owned in zip(panel.getdata(), mask.getdata())])
    return color_metrics(rgba)


def composite_background(rgba: Any) -> Any:
    from PIL import Image

    top = (244, 244, 242)
    bottom = (214, 217, 216)
    background = Image.new("RGB", rgba.size)
    values: List[Tuple[int, int, int]] = []
    for row in range(rgba.height):
        factor = row / max(1, rgba.height - 1)
        color = tuple(int(round(top[index] * (1.0 - factor) + bottom[index] * factor)) for index in range(3))
        values.extend([color] * rgba.width)
    background.putdata(values)
    return Image.composite(rgba.convert("RGB"), background, rgba.getchannel("A"))


def main() -> int:
    args = parse_args(blender_args())
    import bpy  # type: ignore

    lod0 = bpy.data.objects.get(f"{ASSET}_LOD0")
    if lod0 is None:
        raise RuntimeError("A04 LOD0 missing")
    clear_scene_support(bpy, lod0)
    scene = bpy.context.scene
    source_material = lod0.data.materials[0]
    attempt_root = OUTPUT_ROOT_REL / "InternalAttempts" / args.attempt_name
    proof_root = OUTPUT_ROOT_REL if args.mode == "final" else attempt_root

    # Exact front/left shadeless routing proofs.
    shadeless = shadeless_material(bpy, source_material)
    lod0.data.materials[0] = shadeless
    configure_scene(scene, (1024, 1024))
    scene.eevee.use_gtao = False
    scene.eevee.taa_render_samples = 1
    remove_lights(bpy)
    front_camera = make_camera(bpy, "A005_A04_FRONT_ORTHO", (0.0, -500.0, 110.0), (0.0, 0.0, 110.0), ortho_scale=250.0)
    front_shadeless_rel = proof_root / "A04_FRONT_SHADELESS_RGBA.png"
    front_shadeless = render_png(bpy, front_shadeless_rel)
    bpy.data.objects.remove(front_camera, do_unlink=True)
    left_camera = make_camera(bpy, "A005_A04_LEFT_ORTHO", (-500.0, 0.0, 110.0), (0.0, 0.0, 110.0), ortho_scale=250.0)
    left_shadeless_rel = proof_root / "A04_LEFT_SHADELESS_RGBA.png"
    left_shadeless = render_png(bpy, left_shadeless_rel)
    bpy.data.objects.remove(left_camera, do_unlink=True)

    # Lit orthographic structural proof.
    lod0.data.materials[0] = source_material
    configure_scene(scene, (1024, 1024))
    remove_lights(bpy)
    area_light(bpy, "A005_A04_PROOF_FRONT", (0.0, -420.0, 145.0), 1950000.0, 420.0)
    area_light(bpy, "A005_A04_PROOF_FILL", (-220.0, -260.0, 250.0), 480000.0, 360.0)
    front_lit_camera = make_camera(bpy, "A005_A04_FRONT_LIT", (0.0, -500.0, 110.0), (0.0, 0.0, 110.0), ortho_scale=250.0)
    front_lit_rel = proof_root / "A04_FRONT_LIT_RGBA.png"
    front_lit = render_png(bpy, front_lit_rel)
    bpy.data.objects.remove(front_lit_camera, do_unlink=True)

    # Source-oriented three-quarter final: slight elevation exposes both slab ledges.
    configure_scene(scene, (1400, 1600))
    remove_lights(bpy)
    area_light(bpy, "A005_A04_FINAL_FRONT", (0.0, -470.0, 165.0), 2200000.0, 430.0)
    area_light(bpy, "A005_A04_FINAL_KEY", (-250.0, -330.0, 285.0), 1050000.0, 300.0)
    area_light(bpy, "A005_A04_FINAL_FILL", (260.0, -350.0, 210.0), 260000.0, 380.0)
    area_light(bpy, "A005_A04_FINAL_RIM", (180.0, 250.0, 300.0), 80000.0, 280.0)
    final_camera = make_camera(bpy, "A005_A04_FINAL_REVIEW", (190.0, -560.0, 210.0), (0.0, 0.0, 105.0), lens=72.0)
    if args.mode == "final":
        rgba_rel = FINAL_RGBA_REL
        image_rel = FINAL_REL
        audit_rel = FINAL_AUDIT_REL
    else:
        rgba_rel = attempt_root / "A04_ATTEMPT_OBJECT_RGBA.png"
        image_rel = attempt_root / "A04_ATTEMPT.png"
        audit_rel = attempt_root / "A04_ATTEMPT_AUDIT.json"
    rgba = render_png(bpy, rgba_rel)
    final = composite_background(rgba)
    (ROOT / image_rel).parent.mkdir(parents=True, exist_ok=True)
    final.save(ROOT / image_rel, format="PNG")

    audit = {
        "schema": "aerathea.a005_visual_correction_a04_render_audit.v1",
        "asset_id": ASSET,
        "contract_id": CONTRACT,
        "status": "render_complete_pending_a04_independent_audit",
        "mode": args.mode,
        "path": str(image_rel),
        "object_rgba_path": str(rgba_rel),
        "size": list(final.size),
        "sha256": sha256_file(ROOT / image_rel),
        "orientation": "upright source-oriented front three-quarter; slab ledges visible",
        "camera_location_cm": list(final_camera.location),
        "camera_target_cm": [0.0, 0.0, 105.0],
        "color_management": {"view_transform": "Standard", "look": "None", "exposure": 0.0, "gamma": 1.0},
        "background": "neutral off-white gradient; no ground plane or extra prop",
        "alpha_bounds": alpha_bounds(rgba),
        "displayed_color": {"source_front_owned": source_front_metrics(), "front_lit": color_metrics(front_lit), "final": color_metrics(rgba)},
        "proofs": {
            "front_shadeless": {"path": str(front_shadeless_rel), "sha256": sha256_file(ROOT / front_shadeless_rel), "alpha_bounds": alpha_bounds(front_shadeless)},
            "left_shadeless": {"path": str(left_shadeless_rel), "sha256": sha256_file(ROOT / left_shadeless_rel), "alpha_bounds": alpha_bounds(left_shadeless)},
            "front_lit": {"path": str(front_lit_rel), "sha256": sha256_file(ROOT / front_lit_rel), "alpha_bounds": alpha_bounds(front_lit)},
        },
        "review_markers": 0,
        "collision_visible": 0,
        "lod_visible": "LOD0 only",
    }
    (ROOT / audit_rel).write_text(json.dumps(audit, indent=2) + "\n", encoding="utf-8")
    print(json.dumps(audit, indent=2))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
