#!/usr/bin/env python3
"""Render and record the rejected A005 A06 top-projection mismatch."""

from __future__ import annotations

import hashlib
import importlib.util
import json
from pathlib import Path
from typing import Any


ROOT = Path(__file__).resolve().parents[2]
ASSET = "SM_GIA_BloodAxeCairnstone_A005"
A06_BLEND = ROOT / (
    "SourceAssets/Blender/Props/Giants/BloodAxe/Cairns/"
    "SM_GIA_BloodAxeCairnstone_A005/"
    "SM_GIA_BloodAxeCairnstone_A005_DCCGameReady_VisualCorrection_A06.blend"
)
A06_RENDER_HELPER = ROOT / "Tools/DCC/render_bloodaxe_cairnstone_a005_visual_correction_a06.py"
SOURCE_TOP = ROOT / (
    "docs/assets/blueprints/SM_GIA_BloodAxeCairnstone_A005/panels/STEP_03/"
    "SM_GIA_BloodAxeCairnstone_A005_STEP_03_TOP.png"
)
OUTPUT_ROOT = ROOT / (
    "Saved/Automation/DCC/SM_GIA_BloodAxeCairnstone_A005/CoreRecovery/"
    "20260721_A06_TopProjectionDrift"
)
TOP_RGBA = OUTPUT_ROOT / "A005_A06_REJECTED_TOP_ORTHO_RGBA.png"
TOP_DISPLAY = OUTPUT_ROOT / "A005_A06_REJECTED_TOP_ORTHO.png"
BOARD = OUTPUT_ROOT / "A005_A06_TOP_PROJECTION_DRIFT_REVIEW.png"
AUDIT = OUTPUT_ROOT / "A005_A06_TOP_PROJECTION_DRIFT_AUDIT.json"


def load_module(path: Path, name: str) -> Any:
    spec = importlib.util.spec_from_file_location(name, path)
    if spec is None or spec.loader is None:
        raise RuntimeError(f"cannot load {path}")
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


def sha256_file(path: Path) -> str:
    digest = hashlib.sha256()
    with path.open("rb") as stream:
        for chunk in iter(lambda: stream.read(1024 * 1024), b""):
            digest.update(chunk)
    return digest.hexdigest()


def fit(image: Any, maximum: tuple[int, int]) -> Any:
    from PIL import Image

    result = image.copy()
    result.thumbnail(maximum, Image.LANCZOS)
    return result


def main() -> int:
    import bpy  # type: ignore
    from PIL import Image, ImageDraw, ImageFont

    OUTPUT_ROOT.mkdir(parents=True, exist_ok=True)
    render_helper = load_module(A06_RENDER_HELPER, "a005_a06_render_for_top_recovery")
    helper = render_helper.load_helper()

    with bpy.data.libraries.load(str(A06_BLEND), link=False) as (data_from, data_to):
        data_to.objects = list(data_from.objects)
    for obj in data_to.objects:
        if obj is not None:
            bpy.context.scene.collection.objects.link(obj)

    lod0 = bpy.data.objects.get(f"{ASSET}_LOD0")
    if lod0 is None:
        raise RuntimeError("A06 LOD0 missing")
    helper.clear_scene_support(bpy, lod0)
    scene = bpy.context.scene
    source_material = lod0.data.materials[0]
    lod0.data.materials[0] = render_helper.shadeless_material(bpy, source_material)
    helper.configure_scene(scene, (1024, 1024), transparent=True)
    scene.eevee.use_gtao = False
    scene.eevee.taa_render_samples = 1
    helper.remove_lights(bpy)
    top_camera = helper.make_camera(
        bpy,
        "A005_A06_REJECTED_TOP_ORTHO",
        (0.0, 0.0, 500.0),
        (0.0, 0.0, 0.0),
        ortho_scale=170.0,
    )
    top_rgba_rel = TOP_RGBA.relative_to(ROOT)
    top_rgba = helper.render_png(bpy, top_rgba_rel)
    top_display = helper.composite_background(top_rgba)
    top_display.save(TOP_DISPLAY, format="PNG")
    bpy.data.objects.remove(top_camera, do_unlink=True)

    source = Image.open(SOURCE_TOP).convert("RGB")
    source_panel = fit(source, (700, 790))
    render_panel = fit(top_display.convert("RGB"), (790, 790))
    board = Image.new("RGB", (1720, 1120), (245, 244, 240))
    draw = ImageDraw.Draw(board)
    font_path = "/usr/share/fonts/truetype/dejavu/DejaVuSans.ttf"
    bold_path = "/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf"
    title_font = ImageFont.truetype(bold_path, 34)
    heading_font = ImageFont.truetype(bold_path, 24)
    body_font = ImageFont.truetype(font_path, 20)
    small_font = ImageFont.truetype(font_path, 17)
    draw.text((55, 35), "A005 A06 TOP-PROJECTION CORE RECOVERY — PROOF ONLY", fill=(38, 35, 32), font=title_font)
    draw.text((85, 100), "AUTHORITATIVE ORIGINAL TOP PANEL", fill=(38, 35, 32), font=heading_font)
    draw.text((900, 100), "REJECTED A06 — TRUE ORTHOGRAPHIC TOP", fill=(135, 25, 22), font=heading_font)
    board.paste(source_panel, (55 + (760 - source_panel.width) // 2, 145))
    board.paste(render_panel, (870 + (790 - render_panel.width) // 2, 145))

    target_c002 = (123.846154, 92.707424)
    target_c003 = (137.307692, 105.196507)
    crown_c002 = (116.0, 87.0)
    crown_c003 = (130.0, 99.0)
    lines = [
        "Root cause: A06 validated maximum shell bounds, not the visible upper crown projection seen from above.",
        f"C002 visible crown: {crown_c002[0]:.3f} × {crown_c002[1]:.3f} cm; source-derived exterior target: {target_c002[0]:.3f} × {target_c002[1]:.3f} cm.",
        f"C002 total deficit: {target_c002[0]-crown_c002[0]:.3f} × {target_c002[1]-crown_c002[1]:.3f} cm ({(target_c002[0]-crown_c002[0])/2:.3f} / {(target_c002[1]-crown_c002[1])/2:.3f} cm per side).",
        f"C003 visible crown: {crown_c003[0]:.3f} × {crown_c003[1]:.3f} cm; source-derived exterior target: {target_c003[0]:.3f} × {target_c003[1]:.3f} cm.",
        f"C003 total deficit: {target_c003[0]-crown_c003[0]:.3f} × {target_c003[1]-crown_c003[1]:.3f} cm ({(target_c003[0]-crown_c003[0])/2:.3f} / {(target_c003[1]-crown_c003[1])/2:.3f} cm per side).",
    ]
    y = 955
    for index, line in enumerate(lines):
        draw.text((60, y), line, fill=(135, 25, 22) if index == 0 else (38, 35, 32), font=body_font if index == 0 else small_font)
        y += 29
    board.save(BOARD, format="PNG")

    audit = {
        "schema": "aerathea.a005_a06_top_projection_core_recovery.v1",
        "asset_id": ASSET,
        "status": "drift_confirmed_stop_before_geometry",
        "artifact_status": "proof only",
        "source_top": {
            "path": str(SOURCE_TOP.relative_to(ROOT)),
            "sha256": sha256_file(SOURCE_TOP),
            "annotated_monolith_max_cm": [120.0, 90.0],
            "annotated_base_footprint_cm": [140.0, 110.0],
        },
        "rejected_a06": {
            "blend_path": str(A06_BLEND.relative_to(ROOT)),
            "blend_sha256": sha256_file(A06_BLEND),
            "top_render_path": str(TOP_DISPLAY.relative_to(ROOT)),
            "top_render_sha256": sha256_file(TOP_DISPLAY),
            "review_board_path": str(BOARD.relative_to(ROOT)),
            "review_board_sha256": sha256_file(BOARD),
        },
        "visible_crown_projection_cm": {
            "C002": list(crown_c002),
            "C003": list(crown_c003),
        },
        "source_derived_exterior_target_cm": {
            "C002": list(target_c002),
            "C003": list(target_c003),
            "C004": [140.0, 110.0],
        },
        "total_projection_deficit_cm": {
            "C002": [target_c002[0] - crown_c002[0], target_c002[1] - crown_c002[1]],
            "C003": [target_c003[0] - crown_c003[0], target_c003[1] - crown_c003[1]],
        },
        "root_cause": "A06 placed each source-derived maximum exterior span on a lower side ring, then tapered the visible top crown inward; its audit checked only whole-component bounds and omitted the top-visible crown extent.",
        "first_drift_action": "A06 masonry-course ring specification and G06 maximum-bounds gate accepted as proof of top-view silhouette fidelity.",
        "recovery_boundary": "Preserve A06 as rejected/quarantined. No repair-forward. Build a fresh correction only from the original top-view exterior targets after recording this drift.",
    }
    AUDIT.write_text(json.dumps(audit, indent=2) + "\n", encoding="utf-8")
    print(json.dumps(audit, indent=2))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
