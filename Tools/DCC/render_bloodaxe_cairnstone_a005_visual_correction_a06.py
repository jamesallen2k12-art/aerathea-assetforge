#!/usr/bin/env python3
"""Render A005 A06 internal proofs or the single eligible final review."""

from __future__ import annotations

import argparse
import importlib.util
import json
import sys
from pathlib import Path
from typing import Any, List, Sequence


ROOT = Path(__file__).resolve().parents[2]
ASSET = "SM_GIA_BloodAxeCairnstone_A005"
CONTRACT = "A005-CR-VISUAL-CORRECTION-A06"
A04_RENDER = ROOT / "Tools/DCC/render_bloodaxe_cairnstone_a005_visual_correction_a04.py"
A06_BLEND = ROOT / "SourceAssets/Blender/Props/Giants/BloodAxe/Cairns/SM_GIA_BloodAxeCairnstone_A005/SM_GIA_BloodAxeCairnstone_A005_DCCGameReady_VisualCorrection_A06.blend"
OUTPUT_ROOT_REL = Path("Saved/Automation/DCC") / ASSET / "Production/VisualCorrection_A06"
FINAL_REL = OUTPUT_ROOT_REL / f"{ASSET}_FINAL_CORRECTED_3D_A06.png"
FINAL_RGBA_REL = OUTPUT_ROOT_REL / f"{ASSET}_FINAL_CORRECTED_3D_A06_OBJECT_RGBA.png"
FINAL_AUDIT_REL = OUTPUT_ROOT_REL / "FINAL_RENDER_AUDIT_A06.json"


def blender_args() -> List[str]:
    return sys.argv[sys.argv.index("--") + 1 :] if "--" in sys.argv else sys.argv[1:]


def parse_args(argv: Sequence[str]) -> argparse.Namespace:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--mode", choices=("attempt", "final"), required=True)
    parser.add_argument("--attempt-name", default="Attempt01")
    return parser.parse_args(list(argv))


def load_helper() -> Any:
    spec = importlib.util.spec_from_file_location("a005_a04_render_helpers", A04_RENDER)
    if spec is None or spec.loader is None:
        raise RuntimeError("cannot load A04 render helpers")
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


def shadeless_material(bpy: Any, source_material: Any) -> Any:
    material = bpy.data.materials.new("M_A005_A06_INTERNAL_SHADELESS")
    material.use_nodes = True
    nodes = material.node_tree.nodes
    links = material.node_tree.links
    nodes.clear()
    output = nodes.new("ShaderNodeOutputMaterial")
    emission = nodes.new("ShaderNodeEmission")
    image = nodes.new("ShaderNodeTexImage")
    source_node = next(
        node
        for node in source_material.node_tree.nodes
        if node.bl_idname == "ShaderNodeTexImage" and node.name == "A06_DIRECT_SOURCE_BASECOLOR"
    )
    image.image = source_node.image
    image.interpolation = "Linear"
    image.extension = "EXTEND"
    links.new(image.outputs["Color"], emission.inputs["Color"])
    links.new(emission.outputs["Emission"], output.inputs["Surface"])
    return material


def main() -> int:
    args = parse_args(blender_args())
    helper = load_helper()
    import bpy  # type: ignore

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
    attempt_root = OUTPUT_ROOT_REL / "InternalAttempts" / args.attempt_name
    proof_root = OUTPUT_ROOT_REL if args.mode == "final" else attempt_root

    shadeless = shadeless_material(bpy, source_material)
    lod0.data.materials[0] = shadeless
    helper.configure_scene(scene, (1024, 1024))
    scene.eevee.use_gtao = False
    scene.eevee.taa_render_samples = 1
    helper.remove_lights(bpy)
    front_camera = helper.make_camera(
        bpy, "A005_A06_FRONT_ORTHO", (0.0, -500.0, 110.0), (0.0, 0.0, 110.0), ortho_scale=250.0
    )
    front_shadeless_rel = proof_root / "A06_FRONT_SHADELESS_RGBA.png"
    front_shadeless = helper.render_png(bpy, front_shadeless_rel)
    bpy.data.objects.remove(front_camera, do_unlink=True)
    left_camera = helper.make_camera(
        bpy, "A005_A06_LEFT_ORTHO", (-500.0, 0.0, 110.0), (0.0, 0.0, 110.0), ortho_scale=250.0
    )
    left_shadeless_rel = proof_root / "A06_LEFT_SHADELESS_RGBA.png"
    left_shadeless = helper.render_png(bpy, left_shadeless_rel)
    bpy.data.objects.remove(left_camera, do_unlink=True)

    lod0.data.materials[0] = source_material
    helper.configure_scene(scene, (1024, 1024))
    helper.remove_lights(bpy)
    helper.area_light(bpy, "A005_A06_PROOF_FRONT", (0.0, -420.0, 145.0), 1950000.0, 420.0)
    helper.area_light(bpy, "A005_A06_PROOF_FILL", (-220.0, -260.0, 250.0), 480000.0, 360.0)
    front_lit_camera = helper.make_camera(
        bpy, "A005_A06_FRONT_LIT", (0.0, -500.0, 110.0), (0.0, 0.0, 110.0), ortho_scale=250.0
    )
    front_lit_rel = proof_root / "A06_FRONT_LIT_RGBA.png"
    front_lit = helper.render_png(bpy, front_lit_rel)
    bpy.data.objects.remove(front_lit_camera, do_unlink=True)

    helper.configure_scene(scene, (1400, 1600))
    helper.remove_lights(bpy)
    helper.area_light(bpy, "A005_A06_FINAL_FRONT", (0.0, -470.0, 165.0), 2200000.0, 430.0)
    helper.area_light(bpy, "A005_A06_FINAL_KEY", (-250.0, -330.0, 285.0), 1050000.0, 300.0)
    helper.area_light(bpy, "A005_A06_FINAL_FILL", (260.0, -350.0, 210.0), 260000.0, 380.0)
    helper.area_light(bpy, "A005_A06_FINAL_RIM", (180.0, 250.0, 300.0), 80000.0, 280.0)
    final_camera = helper.make_camera(
        bpy, "A005_A06_FINAL_REVIEW", (190.0, -560.0, 225.0), (0.0, 0.0, 102.0), lens=72.0
    )
    if args.mode == "final":
        rgba_rel = FINAL_RGBA_REL
        image_rel = FINAL_REL
        audit_rel = FINAL_AUDIT_REL
    else:
        rgba_rel = attempt_root / "A06_ATTEMPT_OBJECT_RGBA.png"
        image_rel = attempt_root / "A06_ATTEMPT.png"
        audit_rel = attempt_root / "A06_ATTEMPT_AUDIT.json"
    rgba = helper.render_png(bpy, rgba_rel)
    final = helper.composite_background(rgba)
    (ROOT / image_rel).parent.mkdir(parents=True, exist_ok=True)
    final.save(ROOT / image_rel, format="PNG")

    audit = {
        "schema": "aerathea.a005_visual_correction_a06_render_audit.v1",
        "asset_id": ASSET,
        "contract_id": CONTRACT,
        "status": "render_complete_pending_a06_independent_audit",
        "mode": args.mode,
        "path": str(image_rel),
        "object_rgba_path": str(rgba_rel),
        "size": list(final.size),
        "sha256": helper.sha256_file(ROOT / image_rel),
        "orientation": "upright source-oriented front three-quarter; complete oval replacement base and masonry crowns visible",
        "camera_location_cm": list(final_camera.location),
        "camera_target_cm": [0.0, 0.0, 102.0],
        "color_management": {"view_transform": "Standard", "look": "None", "exposure": 0.0, "gamma": 1.0},
        "background": "neutral off-white gradient; no ground plane or extra prop",
        "alpha_bounds": helper.alpha_bounds(rgba),
        "displayed_color": {
            "source_front_owned": helper.source_front_metrics(),
            "front_lit": helper.color_metrics(front_lit),
            "final": helper.color_metrics(rgba),
        },
        "proofs": {
            "front_shadeless": {
                "path": str(front_shadeless_rel),
                "sha256": helper.sha256_file(ROOT / front_shadeless_rel),
                "alpha_bounds": helper.alpha_bounds(front_shadeless),
            },
            "left_shadeless": {
                "path": str(left_shadeless_rel),
                "sha256": helper.sha256_file(ROOT / left_shadeless_rel),
                "alpha_bounds": helper.alpha_bounds(left_shadeless),
            },
            "front_lit": {
                "path": str(front_lit_rel),
                "sha256": helper.sha256_file(ROOT / front_lit_rel),
                "alpha_bounds": helper.alpha_bounds(front_lit),
            },
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
