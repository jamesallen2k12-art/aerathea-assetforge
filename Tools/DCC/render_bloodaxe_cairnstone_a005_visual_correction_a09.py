#!/usr/bin/env python3
"""Render A005 A09 modular proofs and the eligible final review image."""

from __future__ import annotations

import argparse
import importlib.util
import json
import sys
from pathlib import Path
from typing import Any, Dict, List, Sequence, Tuple


ROOT = Path(__file__).resolve().parents[2]
ASSET = "SM_GIA_BloodAxeCairnstone_A005"
CONTRACT = "A005-CR-VISUAL-CORRECTION-A09"
A04_RENDER = ROOT / "Tools/DCC/render_bloodaxe_cairnstone_a005_visual_correction_a04.py"
A09_BLEND = ROOT / "SourceAssets/Blender/Props/Giants/BloodAxe/Cairns/SM_GIA_BloodAxeCairnstone_A005/SM_GIA_BloodAxeCairnstone_A005_DCCGameReady_VisualCorrection_A09.blend"
OUTPUT_ROOT_REL = Path("Saved/Automation/DCC") / ASSET / "Production/VisualCorrection_A09"
FINAL_REL = OUTPUT_ROOT_REL / f"{ASSET}_FINAL_CORRECTED_3D_A09.png"
FINAL_RGBA_REL = OUTPUT_ROOT_REL / f"{ASSET}_FINAL_CORRECTED_3D_A09_OBJECT_RGBA.png"
FINAL_AUDIT_REL = OUTPUT_ROOT_REL / "FINAL_RENDER_AUDIT_A09.json"
MODULE_OBJECTS = {
    "C002": f"{ASSET}_C002_UPPER_COURSE_A09",
    "C003": f"{ASSET}_C003_LOWER_COURSE_A09",
    "C004": f"{ASSET}_C004_RUBBLE_APRON_A09",
}
MODULE_TARGETS = {"C002": 28.0, "C003": 15.5, "C004": 5.0}


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
    material = bpy.data.materials.new("M_A005_A09_INTERNAL_SHADELESS")
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
        if node.bl_idname == "ShaderNodeTexImage" and node.name == "A09_DIRECT_SOURCE_BASECOLOR"
    )
    image.image = source_node.image
    image.interpolation = "Linear"
    image.extension = "EXTEND"
    links.new(image.outputs["Color"], emission.inputs["Color"])
    links.new(emission.outputs["Emission"], output.inputs["Surface"])
    return material


def set_only_mesh_visible(bpy: Any, visible: Any) -> None:
    for obj in bpy.context.scene.objects:
        if obj.type != "MESH":
            continue
        obj.hide_render = obj != visible
        obj.hide_viewport = obj != visible


def internal_alpha_holes(image: Any, y_start: int, y_end: int, threshold: int = 16) -> Dict[str, int]:
    alpha = image.getchannel("A")
    pixels = alpha.load()
    holes = 0
    rows_with_holes = 0
    maximum_row_holes = 0
    for row in range(max(0, y_start), min(image.height, y_end)):
        owned = [column for column in range(image.width) if pixels[column, row] >= threshold]
        if len(owned) < 2:
            continue
        row_holes = sum(1 for column in range(min(owned), max(owned) + 1) if pixels[column, row] < threshold)
        if row_holes:
            rows_with_holes += 1
            holes += row_holes
            maximum_row_holes = max(maximum_row_holes, row_holes)
    return {"pixels": holes, "rows": rows_with_holes, "maximum_row_pixels": maximum_row_holes}


def render_module_proofs(bpy: Any, helper: Any, modules: Dict[str, Any], shadeless: Any, proof_root: Path) -> Dict[str, Any]:
    scene = bpy.context.scene
    helper.remove_lights(bpy)
    scene.eevee.use_gtao = False
    scene.eevee.taa_render_samples = 1
    records: Dict[str, Any] = {}
    for component, obj in modules.items():
        set_only_mesh_visible(bpy, obj)
        source_material = obj.data.materials[0]
        obj.data.materials[0] = shadeless
        target_z = MODULE_TARGETS[component]
        helper.configure_scene(scene, (1200, 500))
        front_camera = helper.make_camera(
            bpy,
            f"A005_A09_{component}_FRONT_ORTHO",
            (0.0, -420.0, target_z),
            (0.0, 0.0, target_z),
            ortho_scale=62.0,
        )
        front_rel = proof_root / "Modules" / f"A09_{component}_FRONT_SHADELESS_RGBA.png"
        front = helper.render_png(bpy, front_rel)
        bpy.data.objects.remove(front_camera, do_unlink=True)

        helper.configure_scene(scene, (1024, 1024))
        top_camera = helper.make_camera(
            bpy,
            f"A005_A09_{component}_TOP_ORTHO",
            (0.0, 0.0, 360.0),
            (0.0, 0.0, 0.0),
            ortho_scale=158.0,
        )
        top_rel = proof_root / "Modules" / f"A09_{component}_TOP_SHADELESS_RGBA.png"
        top = helper.render_png(bpy, top_rel)
        bpy.data.objects.remove(top_camera, do_unlink=True)
        obj.data.materials[0] = source_material
        records[component] = {
            "front": {"path": str(front_rel), "sha256": helper.sha256_file(ROOT / front_rel), "alpha_bounds": helper.alpha_bounds(front)},
            "top": {"path": str(top_rel), "sha256": helper.sha256_file(ROOT / top_rel), "alpha_bounds": helper.alpha_bounds(top)},
        }
    return records


def main() -> int:
    args = parse_args(blender_args())
    helper = load_helper()
    import bpy  # type: ignore

    with bpy.data.libraries.load(str(A09_BLEND), link=False) as (data_from, data_to):
        data_to.objects = list(data_from.objects)
    for obj in data_to.objects:
        if obj is not None:
            bpy.context.scene.collection.objects.link(obj)

    lod0 = bpy.data.objects.get(f"{ASSET}_LOD0")
    if lod0 is None:
        raise RuntimeError("A09 LOD0 missing")
    modules = {component: bpy.data.objects.get(name) for component, name in MODULE_OBJECTS.items()}
    if any(obj is None for obj in modules.values()):
        raise RuntimeError("A09 module object missing")
    helper.clear_scene_support(bpy, lod0)
    scene = bpy.context.scene
    source_material = lod0.data.materials[0]
    shadeless = shadeless_material(bpy, source_material)
    attempt_root = OUTPUT_ROOT_REL / "InternalAttempts" / args.attempt_name
    proof_root = OUTPUT_ROOT_REL if args.mode == "final" else attempt_root

    module_records = render_module_proofs(bpy, helper, modules, shadeless, proof_root)

    set_only_mesh_visible(bpy, lod0)
    lod0.data.materials[0] = shadeless
    helper.configure_scene(scene, (1024, 1024))
    scene.eevee.use_gtao = False
    scene.eevee.taa_render_samples = 1
    helper.remove_lights(bpy)
    proof_specs: Dict[str, Tuple[Sequence[float], Sequence[float], float]] = {
        "front": ((0.0, -500.0, 110.0), (0.0, 0.0, 110.0), 250.0),
        "left": ((-500.0, 0.0, 110.0), (0.0, 0.0, 110.0), 250.0),
        "right": ((500.0, 0.0, 110.0), (0.0, 0.0, 110.0), 250.0),
        "top": ((0.0, 0.0, 500.0), (0.0, 0.0, 0.0), 170.0),
    }
    proof_images: Dict[str, Any] = {}
    proof_paths: Dict[str, Path] = {}
    for view, (location, target, ortho_scale) in proof_specs.items():
        camera = helper.make_camera(bpy, f"A005_A09_{view.upper()}_ORTHO", location, target, ortho_scale=ortho_scale)
        rel = proof_root / f"A09_{view.upper()}_SHADELESS_RGBA.png"
        proof_images[view] = helper.render_png(bpy, rel)
        proof_paths[view] = rel
        bpy.data.objects.remove(camera, do_unlink=True)

    lod0.data.materials[0] = source_material
    helper.configure_scene(scene, (1024, 1024))
    helper.remove_lights(bpy)
    helper.area_light(bpy, "A005_A09_PROOF_FRONT", (0.0, -420.0, 145.0), 1950000.0, 420.0)
    helper.area_light(bpy, "A005_A09_PROOF_FILL", (-220.0, -260.0, 250.0), 480000.0, 360.0)
    front_lit_camera = helper.make_camera(bpy, "A005_A09_FRONT_LIT", (0.0, -500.0, 110.0), (0.0, 0.0, 110.0), ortho_scale=250.0)
    front_lit_rel = proof_root / "A09_FRONT_LIT_RGBA.png"
    front_lit = helper.render_png(bpy, front_lit_rel)
    bpy.data.objects.remove(front_lit_camera, do_unlink=True)

    helper.configure_scene(scene, (1400, 1600))
    helper.remove_lights(bpy)
    helper.area_light(bpy, "A005_A09_FINAL_FRONT", (0.0, -470.0, 165.0), 2200000.0, 430.0)
    helper.area_light(bpy, "A005_A09_FINAL_KEY", (-250.0, -330.0, 285.0), 1050000.0, 300.0)
    helper.area_light(bpy, "A005_A09_FINAL_FILL", (260.0, -350.0, 210.0), 260000.0, 380.0)
    helper.area_light(bpy, "A005_A09_FINAL_RIM", (180.0, 250.0, 300.0), 80000.0, 280.0)
    final_camera = helper.make_camera(bpy, "A005_A09_FINAL_REVIEW", (150.0, -570.0, 235.0), (0.0, 0.0, 101.0), lens=74.0)
    if args.mode == "final":
        rgba_rel = FINAL_RGBA_REL
        image_rel = FINAL_REL
        audit_rel = FINAL_AUDIT_REL
    else:
        rgba_rel = attempt_root / "A09_ATTEMPT_OBJECT_RGBA.png"
        image_rel = attempt_root / "A09_ATTEMPT.png"
        audit_rel = attempt_root / "A09_ATTEMPT_AUDIT.json"
    rgba = helper.render_png(bpy, rgba_rel)
    final = helper.composite_background(rgba)
    (ROOT / image_rel).parent.mkdir(parents=True, exist_ok=True)
    final.save(ROOT / image_rel, format="PNG")

    proofs: Dict[str, Any] = {}
    for view, proof_image in proof_images.items():
        proofs[f"{view}_shadeless"] = {
            "path": str(proof_paths[view]),
            "sha256": helper.sha256_file(ROOT / proof_paths[view]),
            "alpha_bounds": helper.alpha_bounds(proof_image),
            "camera": "true orthographic +Z view; image x=+X and image y=+Y" if view == "top" else f"fixed source-owner {view} orthographic view",
            "ortho_scale_cm": proof_specs[view][2],
        }
    proofs["front_lit"] = {"path": str(front_lit_rel), "sha256": helper.sha256_file(ROOT / front_lit_rel), "alpha_bounds": helper.alpha_bounds(front_lit)}
    interface_bands = {
        "C001_C002": internal_alpha_holes(proof_images["front"], 820, 827),
        "C002_C003": internal_alpha_holes(proof_images["front"], 871, 878),
        "C003_C004": internal_alpha_holes(proof_images["front"], 925, 940),
    }
    interface_leak_pixels = sum(record["pixels"] for record in interface_bands.values())
    ground_rubble_context = internal_alpha_holes(proof_images["front"], 940, 963)
    audit = {
        "schema": "aerathea.a005_visual_correction_a09_render_audit.v1",
        "asset_id": ASSET,
        "contract_id": CONTRACT,
        "status": "render_complete_pending_a09_independent_audit",
        "mode": args.mode,
        "path": str(image_rel),
        "object_rgba_path": str(rgba_rel),
        "size": list(final.size),
        "sha256": helper.sha256_file(ROOT / image_rel),
        "orientation": "upright source-oriented elevated front three-quarter with ovoid base and staggered C004 rubble visible",
        "camera_location_cm": list(final_camera.location),
        "camera_target_cm": [0.0, 0.0, 101.0],
        "color_management": {"view_transform": "Standard", "look": "None", "exposure": 0.0, "gamma": 1.0},
        "background": "neutral off-white gradient; no ground plane or extra prop",
        "alpha_bounds": helper.alpha_bounds(rgba),
        "displayed_color": {"source_front_owned": helper.source_front_metrics(), "front_lit": helper.color_metrics(front_lit), "final": helper.color_metrics(rgba)},
        "module_proofs": module_records,
        "assembled_proofs": proofs,
        "interface_alpha_gate": {
            "method": "front orthographic alpha holes measured only across the three declared module-contact bands",
            "bands": interface_bands,
            "background_leak_pixels": interface_leak_pixels,
            "pass": interface_leak_pixels == 0,
        },
        "ground_rubble_alpha_context": {
            "classification": "diagnostic_only; exterior gaps below the receiver-supported C003/C004 contact remain source-consistent silhouette space",
            **ground_rubble_context,
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
