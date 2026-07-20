#!/usr/bin/env python3
"""Read-only audit for A005 Step 14 planning authority.

This script does not open Blender, create UVs, write textures, author materials,
or mutate project files. It prints one JSON audit report to stdout.
"""

from __future__ import annotations

import argparse
import hashlib
import json
import subprocess
import sys
from pathlib import Path
from typing import Any

from PIL import Image


ROOT = Path(__file__).resolve().parents[2]
ASSET = ROOT / "docs/assets/blueprints/SM_GIA_BloodAxeCairnstone_A005"
MANIFESTS = ASSET / "manifests"
CONTRACT_ID = "A005-CR-STEP14-UV-BASECOLOR-MATERIAL-PLAN-A01"
APPROVED_BLEND_HASH = "5b4af2275a70e2598e72361382fc7ea6ea318724ac928d71b2c200c768a93095"
BLEND = ROOT / "SourceAssets/Blender/Props/Giants/BloodAxe/Cairns/SM_GIA_BloodAxeCairnstone_A005/SM_GIA_BloodAxeCairnstone_A005_DCCSource_A01.blend"
GEOMETRY = ROOT / "SourceAssets/Blender/Props/Giants/BloodAxe/Cairns/SM_GIA_BloodAxeCairnstone_A005/SM_GIA_BloodAxeCairnstone_A005_GEOMETRY_MANIFEST.json"
TEXTURE_ROOT = ROOT / "SourceAssets/Textures/Props/Giants/BloodAxe/Cairns/SM_GIA_BloodAxeCairnstone_A005"


def sha256(path: Path) -> str:
    digest = hashlib.sha256()
    with path.open("rb") as handle:
        for chunk in iter(lambda: handle.read(1024 * 1024), b""):
            digest.update(chunk)
    return digest.hexdigest()


def load_json(path: Path) -> dict[str, Any]:
    with path.open("r", encoding="utf-8") as handle:
        return json.load(handle)


def decoded_rgb_hash(path: Path) -> tuple[str, list[int]]:
    with Image.open(path) as image:
        rgb = image.convert("RGB")
        return hashlib.sha256(rgb.tobytes()).hexdigest(), [rgb.width, rgb.height]


def red_count(path: Path) -> int:
    with Image.open(path) as image:
        rgb = image.convert("RGB")
        return sum(1 for red, green, blue in rgb.getdata() if red >= 50 and red - max(green, blue) >= 18)


def rectangles_overlap_area(a: list[int], b: list[int]) -> int:
    width = max(0, min(a[2], b[2]) - max(a[0], b[0]))
    height = max(0, min(a[3], b[3]) - max(a[1], b[1]))
    return width * height


def rectangle_gap(a: list[int], b: list[int]) -> int:
    if rectangles_overlap_area(a, b):
        return -1
    x_gap = max(0, max(a[0], b[0]) - min(a[2], b[2]))
    y_gap = max(0, max(a[1], b[1]) - min(a[3], b[3]))
    if x_gap and y_gap:
        return min(x_gap, y_gap)
    return max(x_gap, y_gap)


def changed_paths() -> list[str]:
    result = subprocess.run(
        ["git", "status", "--porcelain=v1", "-z"],
        cwd=ROOT,
        check=True,
        stdout=subprocess.PIPE,
    )
    fields = result.stdout.decode("utf-8", errors="surrogateescape").split("\0")
    paths: list[str] = []
    index = 0
    while index < len(fields) and fields[index]:
        entry = fields[index]
        status = entry[:2]
        path = entry[3:]
        if status[0] in {"R", "C"}:
            index += 1
            if index < len(fields):
                path = fields[index]
        paths.append(path)
        index += 1
    return sorted(paths)


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--final", action="store_true", help="require the tracked validation manifest")
    args = parser.parse_args()

    lock = load_json(MANIFESTS / "STEP_14_INPUT_LOCK.json")
    uv = load_json(MANIFESTS / "STEP_14_UV_OWNERSHIP_PLAN.json")
    base = load_json(MANIFESTS / "STEP_14_BASE_COLOR_OWNERSHIP_MANIFEST.json")
    material = load_json(MANIFESTS / "STEP_14_MATERIAL_INTERPRETATION_MANIFEST.json")
    delivery = load_json(MANIFESTS / "STEP_14_TEXTURE_DELIVERY_AND_VALIDATION_PLAN.json")
    geometry = load_json(GEOMETRY)

    gates: list[dict[str, Any]] = []

    def gate(gate_id: str, passed: bool, detail: Any) -> None:
        gates.append({"id": gate_id, "pass": bool(passed), "detail": detail})

    locked_results = []
    for item in lock["locked_inputs"]:
        path = ROOT / item["path"]
        actual = sha256(path) if path.is_file() else None
        locked_results.append({"path": item["path"], "expected": item["sha256"], "actual": actual, "match": actual == item["sha256"]})
    gate("G01_LOCKED_INPUTS", len(locked_results) == lock["counts"]["locked_inputs"] == 32 and all(item["match"] for item in locked_results), {"count": len(locked_results), "mismatches": [item for item in locked_results if not item["match"]]})

    panel_manifest = load_json(MANIFESTS / "STEP_03_PANEL_CROP_MANIFEST.json")
    pixel_results = []
    for panel in panel_manifest["panels"]:
        path = ROOT / panel["path"]
        actual_pixel, actual_size = decoded_rgb_hash(path)
        pixel_results.append({"id": panel["id"], "size": actual_size, "size_match": actual_size == [panel["width"], panel["height"]], "file_match": sha256(path) == panel["file_sha256"], "pixel_match": actual_pixel == panel["pixel_sha256"] == lock["source_pixel_hashes"][panel["id"]]})
    gate("G02_SOURCE_PANEL_RGB", len(pixel_results) == 6 and all(item["size_match"] and item["file_match"] and item["pixel_match"] for item in pixel_results), pixel_results)

    blend_hash = sha256(BLEND)
    gate("G03_APPROVED_CANDIDATE", blend_hash == APPROVED_BLEND_HASH == lock["approved_candidate_sha256"], blend_hash)
    gate("G04_GEOMETRY_IDENTITY", sha256(GEOMETRY) == next(item["sha256"] for item in lock["locked_inputs"] if item["path"].endswith("GEOMETRY_MANIFEST.json")) and geometry["counts"] == {"primary_objects": 4, "vertices": 400, "faces": 464, "triangles_evaluated": 784, "vag_groups_accounted": 14, "unmapped_vertices": 0, "C005_C006_C007_vertices": 0, "uv_layers": 0, "materials": 0, "lods": 0, "collision_objects": 0, "fbx_outputs": 0, "unreal_outputs": 0}, geometry["counts"])

    gate("G05_CONTRACT_SCOPE", lock["contract_id"] == uv["contract_id"] == base["contract_id"] == material["contract_id"] == delivery["contract_id"] == CONTRACT_ID and not lock["flamestrike_authority"]["step15_production_authorized"], CONTRACT_ID)
    gate("G06_UV0_CORE", uv["uv0"]["unique"] and uv["uv0"]["overlap_area_allowed"] == 0 and uv["uv0"]["texture_resolution_px"] == [2048, 2048] and uv["uv0"]["minimum_island_dilation_px"] == 16, uv["uv0"])
    gate("G07_MATERIAL_SLOT", uv["material_assignment"]["slot_count"] == 1 and uv["material_assignment"]["slot_name"] == "M_GIA_BloodAxeCairnstone_A005", uv["material_assignment"])

    windows = uv["uv0"]["source_windows_half_open_px"]
    window_shape_ok = all(item["rect"][2] - item["rect"][0] == item["size"][0] and item["rect"][3] - item["rect"][1] == item["size"][1] and 0 <= min(item["rect"]) and max(item["rect"]) <= 2048 for item in windows)
    window_pair_results = []
    for left_index in range(len(windows)):
        for right_index in range(left_index + 1, len(windows)):
            first, second = windows[left_index], windows[right_index]
            window_pair_results.append({"pair": [first["view"], second["view"]], "overlap_area": rectangles_overlap_area(first["rect"], second["rect"]), "gap_px": rectangle_gap(first["rect"], second["rect"])})
    gate("G08_SOURCE_WINDOWS", len(windows) == 5 and window_shape_ok and all(item["overlap_area"] == 0 and item["gap_px"] >= 32 for item in window_pair_results), {"windows": windows, "pairs": window_pair_results})
    gate("G09_OWNER_VIEWS", [item["view"] for item in windows] == ["front", "back", "left", "right", "top"] and not uv["uv0"]["perspective_owns_texels"], [item["view"] for item in windows])
    gate("G10_COMPONENT_ROUTING", [item["component_id"] for item in uv["uv0"]["component_face_routing"]] == ["C-001", "C-002", "C-003", "C-004"], uv["uv0"]["component_face_routing"])
    gate("G11_HIDDEN_ROUTING", all(item["hidden_groups"] for item in uv["uv0"]["component_face_routing"]) and uv["uv0"]["authored_zone_half_open_px"] == [16, 976, 2032, 2032], uv["uv0"]["authored_zone_half_open_px"])
    gate("G12_UV1_PLAN", uv["uv1"]["unique"] and uv["uv1"]["overlap_area_allowed"] == 0 and uv["uv1"]["planned_lightmap_resolution_px"] == 128 and uv["uv1"]["implementation_deferred_to_step16"], uv["uv1"])

    base_windows = base["source_owner_panels"]
    gate("G13_BASE_COLOR_SPEC", base["map"]["name"] == "T_GIA_BloodAxeCairnstone_A005_BC" and base["map"]["resolution_px"] == [2048, 2048] and base["map"]["bit_depth"] == 8 and base["map"]["color_space"] == "sRGB" and not base["map"]["baked_ao_added"] and not base["map"]["color_grading_allowed"], base["map"])
    gate("G14_BASE_WINDOWS_MATCH", [(item["view"], item["atlas_rect_half_open_px"]) for item in base_windows] == [(item["view"], item["rect"]) for item in windows], [(item["view"], item["atlas_rect_half_open_px"]) for item in base_windows])
    gate("G15_EXACT_RGB_RULE", base["exact_rgb_transfer_rule"]["coordinate_tolerance_px"] == 0 and not any(base["exact_rgb_transfer_rule"][key] for key in ("resizing", "warping", "interpolation", "grading")), base["exact_rgb_transfer_rule"])
    gate("G16_MASK_RULE", base["source_owned_mask_rule"]["not_source_evidence"] and not base["source_owned_mask_rule"]["manual_pixel_changes_allowed"] and "blocks" in base["source_owned_mask_rule"]["failure_policy"], base["source_owned_mask_rule"])

    panel_by_view = {panel["id"]: ROOT / panel["path"] for panel in panel_manifest["panels"]}
    red_results = [{"view": item["view"], "expected": item["raw_red_predicate_pixels"], "actual": red_count(panel_by_view[item["view"]])} for item in base_windows]
    gate("G17_RED_PREDICATE", all(item["expected"] == item["actual"] for item in red_results), red_results)
    routing = base["decoration_routing"]
    gate("G18_DECORATION_ROUTING", all(key in routing for key in ("C-005", "C-006", "C-007")) and all(not routing[key]["hidden_copy"] for key in ("C-005", "C-006", "C-007")) and not routing["cross_view_physical_identity_claimed"], routing)
    gate("G19_AUTHORED_CONTINUATION", base["authored_continuation"]["artifact_classification"] == "interpretation" and not base["authored_continuation"]["red_motif_allowed"] and not base["authored_continuation"]["cross_face_feature_copy_allowed"], base["authored_continuation"])
    gate("G20_PERSPECTIVE_BOUNDARY", not base["perspective_policy"]["base_color_owner"] and base["perspective_policy"]["atlas_window"] is None, base["perspective_policy"])

    gate("G21_MATERIAL_CORE", material["material"]["slot_count"] == 1 and material["material"]["shading_model"] == "Default Lit" and material["material"]["blend_mode"] == "Opaque" and not material["material"]["two_sided"], material["material"])
    gate("G22_NORMAL", material["normal"]["space"] == "tangent-space DirectX/Unreal" and not material["normal"]["displacement"] and not material["normal"]["parallax"] and len(material["normal"]["detail_interpretations"]) == 4, material["normal"])
    gate("G23_ORM", material["orm"]["packing"] == {"R": "Ambient Occlusion", "G": "Roughness", "B": "Metallic"} and material["orm"]["metallic"]["value"] == 0.0 and material["orm"]["metallic"]["required_every_texel"] and not material["orm"]["ao"]["base_color_multiplication"], material["orm"])
    gate("G24_BAKE", material["bake"]["target_resolution_px"] == [2048, 2048] and material["bake"]["ao_samples"] == 256 and material["bake"]["ao_distance_cm"] == 12.0 and material["bake"]["margin_px"] == 16 and material["bake"]["geometry_source_sha256"] == APPROVED_BLEND_HASH and not material["bake"]["base_color_baked"], material["bake"])
    gate("G25_EMISSIVE_REJECTED", material["emissive_decision"]["status"] == "rejected_and_absent_for_A005_A01" and not material["material"]["emissive_input_enabled"] and material["material"]["emissive_map"] is None and delivery["forbidden_map"] == "T_GIA_BloodAxeCairnstone_A005_E", material["emissive_decision"])

    map_names = [item["name"] for item in delivery["maps"]]
    gate("G26_DELIVERY_MAPS", map_names == ["T_GIA_BloodAxeCairnstone_A005_BC", "T_GIA_BloodAxeCairnstone_A005_N", "T_GIA_BloodAxeCairnstone_A005_ORM"] and all(item["resolution_px"] == [2048, 2048] for item in delivery["maps"]), delivery["maps"])
    gate("G27_MIP_FILTER", delivery["mip_policy"]["source_delivery"].startswith("lossless mip 0") and not delivery["mip_policy"]["mip_exactness_claimed"] and delivery["filter_policy"]["source_ingest"].startswith("nearest/point") and not delivery["filter_policy"]["filtered_source_raster_generation"], {"mip": delivery["mip_policy"], "filter": delivery["filter_policy"]})
    gate("G28_STEP15_GATES", len(delivery["step15_validation_gates"]) == 18 and [item["id"] for item in delivery["step15_validation_gates"]] == [f"S15-G{index:02d}-{suffix}" for index, suffix in enumerate(["INPUTS", "GEOMETRY", "UV0", "UV1", "WINDOWS", "MASKS", "RGB", "AUTHORED", "DECORATION", "BC", "NORMAL", "ORM", "BAKE", "MIPS", "MATERIAL", "RENDERS", "CLASSIFICATION", "FIREWALL"], start=1)], [item["id"] for item in delivery["step15_validation_gates"]])
    gate("G29_ZERO_PRODUCTION", all(value in (0, False) for value in delivery["step14_zero_output_assertions"].values()) and not TEXTURE_ROOT.exists() and geometry["counts"]["uv_layers"] == 0 and geometry["counts"]["materials"] == 0 and blend_hash == APPROVED_BLEND_HASH, {"assertions": delivery["step14_zero_output_assertions"], "texture_root_exists_live": TEXTURE_ROOT.exists()})

    required_documents = [
        ASSET / "review/STEP_14_UV_BASECOLOR_MATERIAL_PLAN_REVIEW.md",
        ASSET / "steps/STEP_14_OUTPUT_RECORD.md",
        ASSET / "handoffs/STEP_14_TO_STEP_15_HANDOFF.md",
        ASSET / "SM_GIA_BloodAxeCairnstone_A005_APPROVAL_LOG.md",
        ASSET / "SM_GIA_BloodAxeCairnstone_A005_ARTIFACT_INDEX.md",
        ASSET / "SM_GIA_BloodAxeCairnstone_A005_RESET_RESUME_STATE.md",
    ]
    gate("G30_REVIEW_CLOSEOUT_DOCS", all(path.is_file() for path in required_documents) and "Status: approved" in required_documents[0].read_text(encoding="utf-8") and "Status: complete" in required_documents[1].read_text(encoding="utf-8") and "Step 15 contract preparation only" in required_documents[2].read_text(encoding="utf-8"), [str(path.relative_to(ROOT)) for path in required_documents])

    allowed_asset_names = {
        "SM_GIA_BloodAxeCairnstone_A005_APPROVAL_LOG.md",
        "SM_GIA_BloodAxeCairnstone_A005_ARTIFACT_INDEX.md",
        "SM_GIA_BloodAxeCairnstone_A005_RESET_RESUME_STATE.md",
        "steps/STEP_14_UV_BASECOLOR_MATERIAL_INTERPRETATION_PLAN_CONTRACT.md",
        "steps/STEP_14_OUTPUT_RECORD.md",
        "handoffs/STEP_14_TO_STEP_15_HANDOFF.md",
        "review/STEP_14_UV_BASECOLOR_MATERIAL_PLAN_REVIEW.md",
        "manifests/STEP_14_INPUT_LOCK.json",
        "manifests/STEP_14_UV_OWNERSHIP_PLAN.json",
        "manifests/STEP_14_BASE_COLOR_OWNERSHIP_MANIFEST.json",
        "manifests/STEP_14_MATERIAL_INTERPRETATION_MANIFEST.json",
        "manifests/STEP_14_TEXTURE_DELIVERY_AND_VALIDATION_PLAN.json",
        "manifests/STEP_14_VALIDATION_MANIFEST.json",
    }
    all_changed = changed_paths()
    asset_prefix = "docs/assets/blueprints/SM_GIA_BloodAxeCairnstone_A005/"
    changed_asset = [path[len(asset_prefix):] for path in all_changed if path.startswith(asset_prefix)]
    unexpected_asset = sorted(set(changed_asset) - allowed_asset_names)
    scoped_tool = "Tools/DCC/audit_bloodaxe_cairnstone_a005_step14_plan.py"
    unexpected_scoped = [path for path in all_changed if ("SM_GIA_BloodAxeCairnstone_A005" in path or "a005_step14" in path.lower()) and not path.startswith(asset_prefix) and path != scoped_tool]
    gate("G31_CHANGED_PATH_FIREWALL", not unexpected_asset and not unexpected_scoped, {"changed_asset": changed_asset, "unexpected_asset": unexpected_asset, "unexpected_scoped": unexpected_scoped, "unrelated_preserved_count": len(all_changed) - len(changed_asset) - (1 if scoped_tool in all_changed else 0)})

    validation_path = MANIFESTS / "STEP_14_VALIDATION_MANIFEST.json"
    if args.final:
        validation = load_json(validation_path) if validation_path.is_file() else {}
        validation_ok = validation.get("status") == "pass_authoritative_step14_plan_complete" and validation.get("audit", {}).get("gates_passed") == 32 and validation.get("audit", {}).get("gates_total") == 32 and validation.get("audit", {}).get("failures") == []
        detail: Any = validation if validation else "missing"
    else:
        validation_ok = True
        detail = "first complete audit report will populate the tracked validation manifest"
    gate("G32_VALIDATION_RECORD", validation_ok, detail)

    failures = [item for item in gates if not item["pass"]]
    report = {
        "schema": "aerathea.step14_plan_read_only_audit.v1",
        "asset_id": "SM_GIA_BloodAxeCairnstone_A005",
        "contract_id": CONTRACT_ID,
        "mode": "final" if args.final else "first_complete",
        "status": "pass" if not failures else "fail_closed",
        "gates_total": len(gates),
        "gates_passed": len(gates) - len(failures),
        "failures": [item["id"] for item in failures],
        "candidate_sha256": blend_hash,
        "locked_inputs": len(locked_results),
        "source_panels": len(pixel_results),
        "texture_maps_created": 0,
        "uv_layers_created": 0,
        "materials_created": 0,
        "gates": gates,
    }
    json.dump(report, sys.stdout, indent=2, sort_keys=True)
    sys.stdout.write("\n")
    return 0 if not failures else 1


if __name__ == "__main__":
    raise SystemExit(main())
