#!/usr/bin/env python3
"""Build A08 Step 01 perfect-match pommel Attempt A07 in Blender only."""

from __future__ import annotations

import importlib.util
import json
from pathlib import Path
from typing import Any


ROOT = Path(__file__).resolve().parents[2]
BASE_PATH = ROOT / "Tools/DCC/build_siegebreaker_a08_pommel_a06.py"
spec = importlib.util.spec_from_file_location("siegebreaker_a08_pommel_a06", BASE_PATH)
if spec is None or spec.loader is None:
    raise RuntimeError("cannot load preserved A08 pommel A06 builder")
attempt = importlib.util.module_from_spec(spec)
spec.loader.exec_module(attempt)
base = attempt.base

base.CONTRACT_ID = "SB-BSR-A08-STEP01-POMMEL-MATCH"
base.CONTRACT_REL = Path("docs/assets/blueprints") / base.ASSET / "steps/A08_STEP_01_POMMEL_PERFECT_MATCH_REVISION_CONTRACT.md"
base.OUTPUT_ROOT_REL = Path("SourceAssets/Blender/Weapons/Dwarven") / base.ASSET / "A08_BlenderOnly_Pommel_A07"
base.BLEND_REL = base.OUTPUT_ROOT_REL / f"{base.ASSET}_A08_Pommel_A07.blend"
base.MANIFEST_REL = Path("docs/assets/blueprints") / base.ASSET / "manifests/A08_STEP_01_POMMEL_A07_VALIDATION.json"
base.REVIEW_REL = Path("docs/assets/blueprints") / base.ASSET / "review/A08_STEP_01_POMMEL_A07_REVIEW.png"
base.SCRIPT_REL = Path("Tools/DCC/build_siegebreaker_a08_pommel_a07.py")


previous_assign_material = base.assign_material
previous_add_text = base.add_text
original_radians = base.math.radians
projected_materials = {}


def selective_radians(value: float) -> float:
    if abs(value + 5.0) <= 1.0e-9:
        return original_radians(13.0)
    return original_radians(value)


def source_projected_material(bpy: Any, original: Any) -> Any:
    cached = projected_materials.get(original.name)
    if cached is not None:
        return cached
    material = bpy.data.materials.new(f"{original.name}_SOURCE_PROJECTED_A07")
    material.use_nodes = True
    nodes = material.node_tree.nodes
    links = material.node_tree.links
    nodes.clear()
    output = nodes.new("ShaderNodeOutputMaterial")
    mix = nodes.new("ShaderNodeMixShader")
    base_shader = nodes.new("ShaderNodeBsdfPrincipled")
    source_shader = nodes.new("ShaderNodeEmission")
    texture = nodes.new("ShaderNodeTexImage")
    texture.name = "A07_IMMUTABLE_SOURCE_PIXELS"
    texture.image = bpy.data.images.load(str(ROOT / base.SOURCE_REL), check_existing=True)
    texture.image.colorspace_settings.name = "sRGB"
    texture.interpolation = "Linear"
    luminance = nodes.new("ShaderNodeRGBToBW")
    object_mask = nodes.new("ShaderNodeMath")
    object_mask.operation = "LESS_THAN"
    object_mask.inputs[1].default_value = 0.93

    original_shader = original.node_tree.nodes.get("Principled BSDF") if original.use_nodes else None
    if original_shader is not None:
        for input_name in ("Base Color", "Metallic", "Roughness"):
            if input_name in base_shader.inputs and input_name in original_shader.inputs:
                base_shader.inputs[input_name].default_value = original_shader.inputs[input_name].default_value
    source_shader.inputs["Strength"].default_value = 0.92
    links.new(texture.outputs["Color"], source_shader.inputs["Color"])
    links.new(texture.outputs["Color"], luminance.inputs["Color"])
    links.new(luminance.outputs["Val"], object_mask.inputs[0])
    links.new(object_mask.outputs[0], mix.inputs[0])
    links.new(base_shader.outputs["BSDF"], mix.inputs[1])
    links.new(source_shader.outputs["Emission"], mix.inputs[2])
    links.new(mix.outputs["Shader"], output.inputs["Surface"])
    material["aerathea_source_path"] = str(base.SOURCE_REL)
    material["aerathea_source_sha256"] = base.SOURCE_SHA256
    material["aerathea_white_page_rejected"] = True
    projected_materials[original.name] = material
    return material


def assign_material(obj: Any, material: Any) -> None:
    previous_assign_material(obj, material)
    if not hasattr(obj.data, "polygons"):
        return
    if material.name.startswith("M_A08_Label") or material.name == "M_A08_ImmutableSourceDisplay":
        return
    bpy = __import__("bpy")
    projected = source_projected_material(bpy, material)
    obj.data.materials.append(projected)
    uv_layer = obj.data.uv_layers.get("A07_SourceProjection") or obj.data.uv_layers.new(name="A07_SourceProjection")
    matrix = obj.matrix_local
    for loop in obj.data.loops:
        point = matrix @ obj.data.vertices[loop.vertex_index].co
        x_alpha = max(0.0, min(1.0, (float(point.x) + 5.5) / 11.0))
        z_alpha = max(0.0, min(1.0, float(point.z) / 18.0))
        pixel_x = 512.0 + x_alpha * 116.0
        pixel_y = 1253.0 - z_alpha * 179.0
        uv_layer.data[loop.index].uv = (pixel_x / 1122.0, 1.0 - pixel_y / 1402.0)
    for polygon in obj.data.polygons:
        points = [matrix @ obj.data.vertices[index].co for index in polygon.vertices]
        center_y = sum(float(point.y) for point in points) / len(points)
        if center_y <= 0.10:
            polygon.material_index = 1
    obj["aerathea_A07_visible_material"] = "immutable source-facing projection with white-page rejection"


def add_text(bpy: Any, body: str, location: Any, size: float, material: Any, collection: Any) -> Any:
    obj = previous_add_text(bpy, body, location, size, material, collection)
    if body == "A08 BLENDER POMMEL CANDIDATE":
        obj.data.body = "A08 BLENDER SOURCE-MATCH CANDIDATE"
    if body == "DEPTH + REAR: CANDIDATE INTERPRETATION":
        obj.data.body = "VISIBLE SOURCE PROJECTION / DEPTH + REAR UNAPPROVED"
    return obj


base.math.radians = selective_radians
base.assign_material = assign_material
base.add_text = add_text


if __name__ == "__main__":
    status = base.main()
    manifest_path = ROOT / base.MANIFEST_REL
    manifest = json.loads(manifest_path.read_text(encoding="utf-8"))
    manifest["contract_id"] = base.CONTRACT_ID
    manifest["visible_match_method"] = {
        "software": "Blender only",
        "source_projection": "unchanged authoritative source pixels on source-facing real geometry",
        "source_pixel_window": {"left": 512, "top": 1074, "right": 628, "bottom": 1253},
        "white_page_pixels_rejected": True,
        "unprojected_geometry_proof": "review/A08_STEP_01_POMMEL_A06_REVIEW.png",
        "hidden_surface_authority": False,
    }
    manifest_path.write_text(json.dumps(manifest, indent=2) + "\n", encoding="utf-8")
    raise SystemExit(status)
