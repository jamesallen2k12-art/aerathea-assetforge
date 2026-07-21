#!/usr/bin/env python3
"""Build the bounded A005 A02 base-stack and displayed-color correction."""

from __future__ import annotations

import hashlib
import importlib.util
import json
import math
import shutil
import sys
from pathlib import Path
from typing import Any, Dict, List, Sequence, Tuple


ROOT = Path(__file__).resolve().parents[2]
ASSET = "SM_GIA_BloodAxeCairnstone_A005"
CONTRACT = "A005-CR-VISUAL-CORRECTION-A02"
PLAN_REL = Path("docs/assets/blueprints") / ASSET / "manifests/VISUAL_CORRECTION_A02_PLAN.json"
SOURCE_REL = Path("docs/assets/reference/bloodaxe_cairnstone_asset/REF_GIA_BloodAxeCairnstoneAsset_A02_BlueprintTemplate.png")
MASK_MANIFEST_REL = Path("SourceAssets/Textures/Props/Giants/BloodAxe/Cairns") / ASSET / "Technical/SM_GIA_BloodAxeCairnstone_A005_SOURCE_MASK_MANIFEST_A01.json"
OLD_TEXTURE_ROOT = Path("SourceAssets/Textures/Props/Giants/BloodAxe/Cairns") / ASSET
TEXTURE_ROOT = OLD_TEXTURE_ROOT / "VisualCorrection_A02"
BC_REL = TEXTURE_ROOT / f"T_GIA_BloodAxeCairnstone_A005_VF_A02_BC.png"
N_REL = TEXTURE_ROOT / f"T_GIA_BloodAxeCairnstone_A005_VF_A02_N.png"
ORM_REL = TEXTURE_ROOT / f"T_GIA_BloodAxeCairnstone_A005_VF_A02_ORM.png"
DCC_ROOT = Path("SourceAssets/Blender/Props/Giants/BloodAxe/Cairns") / ASSET
BLEND_REL = DCC_ROOT / f"{ASSET}_DCCGameReady_VisualCorrection_A02.blend"
MANIFEST_REL = DCC_ROOT / f"{ASSET}_VISUAL_CORRECTION_A02_MANIFEST.json"
EXPORT_ROOT = Path("SourceAssets/Exports/Props/Giants/BloodAxe/Cairns") / ASSET / "VisualCorrection_A02"
FBX_RELS = {
    "LOD0": EXPORT_ROOT / f"{ASSET}_VisualCorrection_A02.fbx",
    "LOD1": EXPORT_ROOT / f"{ASSET}_VisualCorrection_A02_LOD1.fbx",
    "LOD2": EXPORT_ROOT / f"{ASSET}_VisualCorrection_A02_LOD2.fbx",
    "LOD3": EXPORT_ROOT / f"{ASSET}_VisualCorrection_A02_LOD3.fbx",
}
A01_BLEND_REL = DCC_ROOT / f"{ASSET}_DCCGameReady_A02.blend"
A01_FINAL_REL = Path("Saved/Automation/DCC") / ASSET / "Production/VisualFidelityRecovery_A01" / f"{ASSET}_FINAL_GAME_READY_ASSET.png"
A01_MODULE_PATH = ROOT / "Tools/DCC/build_bloodaxe_cairnstone_a005_visual_fidelity_recovery.py"


def sha256_file(path: Path) -> str:
    digest = hashlib.sha256()
    with path.open("rb") as handle:
        for block in iter(lambda: handle.read(1024 * 1024), b""):
            digest.update(block)
    return digest.hexdigest()


def load_json(rel: Path) -> Dict[str, Any]:
    with (ROOT / rel).open("r", encoding="utf-8") as handle:
        return json.load(handle)


def load_a01_module() -> Any:
    spec = importlib.util.spec_from_file_location("a005_visual_fidelity_a01_builder", A01_MODULE_PATH)
    if spec is None or spec.loader is None:
        raise RuntimeError("cannot load the preserved A01 builder")
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


def deterministic_palette_field(size: Tuple[int, int], palette: Sequence[Sequence[int]]) -> Any:
    from PIL import Image

    low_size = (64, 64)
    values: List[int] = []
    for y in range(low_size[1]):
        for x in range(low_size[0]):
            wave = (
                0.50
                + 0.20 * math.sin(x * 0.31 + y * 0.17)
                + 0.16 * math.sin(x * 0.11 - y * 0.27 + 1.7)
                + 0.10 * math.sin(x * 0.47 + y * 0.39 + 0.6)
            )
            values.append(max(0, min(255, int(round(wave * 255.0)))))
    low = Image.new("L", low_size)
    low.putdata(values)
    resampling = getattr(Image, "Resampling", Image)
    field = low.resize(size, resampling.BILINEAR)
    indices = field.point(lambda value: min(len(palette) - 1, int(value) * len(palette) // 256))
    indexed = Image.frombytes("P", size, indices.tobytes())
    flattened: List[int] = []
    for color in palette:
        flattened.extend(int(channel) for channel in color[:3])
    flattened.extend([0] * (768 - len(flattened)))
    indexed.putpalette(flattened)
    return indexed.convert("RGB")


def corrected_copy_textures(base: Any) -> Dict[str, Dict[str, Any]]:
    from PIL import Image

    mapping = {
        BC_REL: OLD_TEXTURE_ROOT / "T_GIA_BloodAxeCairnstone_A005_BC.png",
        N_REL: OLD_TEXTURE_ROOT / "T_GIA_BloodAxeCairnstone_A005_N.png",
        ORM_REL: OLD_TEXTURE_ROOT / "T_GIA_BloodAxeCairnstone_A005_ORM.png",
    }
    (ROOT / TEXTURE_ROOT).mkdir(parents=True, exist_ok=True)
    mask_manifest = load_json(MASK_MANIFEST_REL)
    uv_plan = load_json(Path("docs/assets/blueprints") / ASSET / "manifests/STEP_14_UV_OWNERSHIP_PLAN.json")
    windows = {entry["view"]: entry["rect"] for entry in uv_plan["uv0"]["source_windows_half_open_px"]}
    palette = mask_manifest["global_fallback_palette"]
    records: Dict[str, Dict[str, Any]] = {}

    for destination_rel, source_rel in mapping.items():
        source = ROOT / source_rel
        destination = ROOT / destination_rel
        if destination_rel == BC_REL:
            source_color = Image.open(source).convert("RGB")
            corrected = deterministic_palette_field(source_color.size, palette)
            for record in mask_manifest["records"]:
                rect = windows[record["view"]]
                mask = Image.open(ROOT / record["mask_path"]).convert("L")
                expected = (rect[2] - rect[0], rect[3] - rect[1])
                if mask.size != expected:
                    raise RuntimeError(f"{record['view']} source mask/window size mismatch")
                binary = mask.point(lambda value: 255 if value > 0 else 0)
                corrected.paste(source_color.crop(tuple(rect)), (rect[0], rect[1]), binary)
            corrected.save(destination, format="PNG")
            correction = (
                "source-owned mip-0 RGB preserved exactly; every unowned texel replaced by deterministic "
                "low-frequency colors drawn only from the approved dark-stone fallback palette"
            )
        else:
            shutil.copy2(source, destination)
            correction = "none; approved Step 14 map preserved byte-for-byte"
        if destination_rel == ORM_REL:
            metallic_extrema = Image.open(destination).convert("RGB").getchannel("B").getextrema()
            if metallic_extrema != (0, 0):
                raise RuntimeError(f"ORM metallic channel is not identically zero: {metallic_extrema}")
        records[destination_rel.name] = {
            "path": str(destination_rel),
            "sha256": sha256_file(destination),
            "source_path": str(source_rel),
            "source_sha256": sha256_file(source),
            "a02_correction": correction,
            "recovery_role": "A02 source-authority-preserving displayed-color correction",
        }
    return records


def corrected_materials(base: Any, bpy: Any) -> Tuple[Any, Any]:
    stone = bpy.data.materials.new("M_GIA_BloodAxeCairnstone_A005_VisualCorrection_A02")
    stone.use_nodes = True
    stone.use_backface_culling = True
    nodes = stone.node_tree.nodes
    links = stone.node_tree.links
    nodes.clear()
    output = nodes.new("ShaderNodeOutputMaterial")
    shader = nodes.new("ShaderNodeBsdfPrincipled")
    base_color = nodes.new("ShaderNodeTexImage")
    base_color.name = "A02_DIRECT_SOURCE_BASECOLOR"
    base_color.image = bpy.data.images.load(str(ROOT / BC_REL), check_existing=False)
    base_color.image.colorspace_settings.name = "sRGB"
    base_color.interpolation = "Linear"

    normal_image = nodes.new("ShaderNodeTexImage")
    normal_image.name = "A02_DIRECTX_NORMAL"
    normal_image.image = bpy.data.images.load(str(ROOT / N_REL), check_existing=False)
    try:
        normal_image.image.colorspace_settings.name = "Non-Color"
    except TypeError:
        normal_image.image.colorspace_settings.name = "Linear"
    split_normal = nodes.new("ShaderNodeSeparateRGB")
    invert_green = nodes.new("ShaderNodeMath")
    invert_green.operation = "SUBTRACT"
    invert_green.inputs[0].default_value = 1.0
    combine_normal = nodes.new("ShaderNodeCombineRGB")
    normal_map = nodes.new("ShaderNodeNormalMap")
    normal_map.inputs["Strength"].default_value = 0.80

    orm = nodes.new("ShaderNodeTexImage")
    orm.name = "A02_ORM_NONMETALLIC"
    orm.image = bpy.data.images.load(str(ROOT / ORM_REL), check_existing=False)
    try:
        orm.image.colorspace_settings.name = "Non-Color"
    except TypeError:
        orm.image.colorspace_settings.name = "Linear"
    separate_orm = nodes.new("ShaderNodeSeparateRGB")

    links.new(base_color.outputs["Color"], shader.inputs["Base Color"])
    links.new(normal_image.outputs["Color"], split_normal.inputs["Image"])
    links.new(split_normal.outputs["R"], combine_normal.inputs["R"])
    links.new(split_normal.outputs["G"], invert_green.inputs[1])
    links.new(invert_green.outputs[0], combine_normal.inputs["G"])
    links.new(split_normal.outputs["B"], combine_normal.inputs["B"])
    links.new(combine_normal.outputs["Image"], normal_map.inputs["Color"])
    links.new(normal_map.outputs["Normal"], shader.inputs["Normal"])
    links.new(orm.outputs["Color"], separate_orm.inputs["Image"])
    links.new(separate_orm.outputs["G"], shader.inputs["Roughness"])
    links.new(separate_orm.outputs["B"], shader.inputs["Metallic"])
    links.new(shader.outputs["BSDF"], output.inputs["Surface"])
    shader.inputs["Specular"].default_value = 0.25

    stone["aerathea_map_set"] = "BaseColor/DirectXNormal/ORM"
    stone["aerathea_shading_model"] = "Default Lit"
    stone["aerathea_display_color_chain"] = "direct sRGB BaseColor; no gamma or grading"
    stone["aerathea_emissive"] = False
    stone["aerathea_metallic_required"] = 0.0
    stone["aerathea_roughness_authority"] = "ORM.G Step 14 range 0.55-0.90"

    removable = bpy.data.materials.new("M_GIA_BloodAxeCairnstone_A005_A02_REMOVED_HELPER")
    return stone, removable


def configure_base_module(base: Any) -> None:
    base.CONTRACT = CONTRACT
    base.PLAN_REL = PLAN_REL
    base.BC_REL = BC_REL
    base.N_REL = N_REL
    base.ORM_REL = ORM_REL
    base.TEXTURE_ROOT = TEXTURE_ROOT
    base.BLEND_REL = BLEND_REL
    base.MANIFEST_REL = MANIFEST_REL
    base.EXPORT_ROOT = EXPORT_ROOT
    base.FBX_RELS = FBX_RELS
    base.copy_textures = lambda: corrected_copy_textures(base)
    base.create_materials = lambda bpy: corrected_materials(base, bpy)

    original_loft = base.loft

    def corrected_loft(
        bpy: Any,
        name: str,
        profiles: Sequence[Tuple[float, float, float, float]],
        segments: int,
        exponent: float,
        collection: Any,
    ) -> Any:
        replacements = {
            "APRON_CORE": [
                (0.0, 138.0, 108.0, 0.0),
                (2.5, 140.0, 110.0, 0.35),
                (8.0, 126.0, 98.0, 0.65),
                (10.5, 112.0, 88.0, 0.0),
            ],
            "LOWER_COURSE_CORE": [
                (9.5, 110.0, 86.0, 0.0),
                (10.5, 112.0, 88.0, 0.18),
                (22.5, 108.0, 84.0, 0.28),
                (23.5, 106.0, 82.0, 0.0),
            ],
            "UPPER_COURSE_CORE": [
                (22.5, 104.0, 80.0, 0.0),
                (23.0, 106.0, 82.0, 0.15),
                (34.5, 102.0, 78.0, 0.22),
                (35.5, 100.0, 76.0, 0.0),
            ],
        }
        result = original_loft(bpy, name, replacements.get(name, profiles), segments, exponent, collection)
        if name == "MONOLITH_BODY":
            for vertex in result.data.vertices:
                vertex.co.x = max(-60.0, min(60.0, float(vertex.co.x)))
                vertex.co.y = max(-45.0, min(45.0, float(vertex.co.y)))
            result.data.update()
        return result

    base.loft = corrected_loft


def schema_only(base: Any) -> Dict[str, Any]:
    plan = load_json(PLAN_REL)
    source_hash = sha256_file(ROOT / SOURCE_REL)
    return {
        "schema": "aerathea.a005_visual_correction_a02_builder_preflight.v1",
        "asset_id": ASSET,
        "contract_id": CONTRACT,
        "status": "pass_schema_only_no_output" if source_hash == plan["source_authority"]["sha256"] else "blocked_source_hash",
        "bpy_imported": "bpy" in sys.modules,
        "source_sha256": source_hash,
        "outputs": [str(BLEND_REL), str(MANIFEST_REL), str(BC_REL), str(N_REL), str(ORM_REL), *[str(path) for path in FBX_RELS.values()]],
    }


def build(base: Any) -> Dict[str, Any]:
    configure_base_module(base)
    a01_blend_hash = sha256_file(ROOT / A01_BLEND_REL)
    a01_final_hash = sha256_file(ROOT / A01_FINAL_REL)
    manifest = base.build()
    manifest.update(
        {
            "schema": "aerathea.a005_visual_correction_a02_candidate.v1",
            "contract_id": CONTRACT,
            "status": "candidate_pending_independent_a02_audit",
            "artifact_classification": "candidate",
            "pipeline_status": "DCC game-ready candidate pending A02 correction audit",
            "first_divergence_repaired": "STEP_12_under_resolved_784_triangle_blockout",
            "a02_visual_defect_repaired": "A01_visual_rejection_base_stack_and_displayed_color",
            "a02_corrections": {
                "base_profiles": "C004/C003/C002 restored to the approved 0-10/10-23/23-35 cm stepped read with contained widths",
                "base_color": "source-owned pixels exact; unowned stripe propagation replaced by approved dark-stone palette continuation",
                "shader": "Default Lit direct Base Color, DirectX normal, ORM roughness/zero metallic; gamma lift and procedural bump removed",
                "presentation": "neutral lighting, zero exposure offset, lower pitch, full silhouette without ground intersection",
            },
            "a01_preservation": {
                "blend": {"path": str(A01_BLEND_REL), "sha256": a01_blend_hash},
                "final_image": {"path": str(A01_FINAL_REL), "sha256": a01_final_hash},
                "overwritten": False,
            },
            "base_component_targets_cm": {
                "C004_APRON": {"z": [0.0, 10.5], "max_width": 140.0, "max_depth": 110.0},
                "C003_LOWER_TIER": {"z": [9.5, 23.5], "max_width": 112.0, "max_depth": 88.0},
                "C002_UPPER_TIER": {"z": [22.5, 35.5], "max_width": 106.0, "max_depth": 82.0},
            },
            "unreal_outputs": 0,
            "fully_game_ready": False,
            "visual_canon": False,
        }
    )
    (ROOT / MANIFEST_REL).write_text(json.dumps(manifest, indent=2) + "\n", encoding="utf-8")
    return manifest


def main() -> int:
    base = load_a01_module()
    arguments = base.parse_args(base.blender_args())
    if arguments.schema_only:
        report = schema_only(base)
        if report["bpy_imported"]:
            raise RuntimeError("schema-only path imported bpy")
    else:
        report = build(base)
    print(json.dumps(report, indent=2))
    return 0 if not report["status"].startswith("blocked") else 1


if __name__ == "__main__":
    raise SystemExit(main())
