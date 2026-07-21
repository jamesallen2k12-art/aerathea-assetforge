#!/usr/bin/env python3
"""Independently audit A005 A11 against A10 footprint authority."""

from __future__ import annotations

import importlib.util
import json
from pathlib import Path
from typing import Any, Dict, List


ROOT = Path(__file__).resolve().parents[2]
ASSET = "SM_GIA_BloodAxeCairnstone_A005"
SUPPORT = ROOT / "Tools/DCC/audit_bloodaxe_cairnstone_a005_visual_correction_a09.py"
BLUEPRINT_ROOT = Path("docs/assets/blueprints") / ASSET
PLAN_REL = BLUEPRINT_ROOT / "manifests/VISUAL_CORRECTION_A11_PLAN.json"
VALIDATION_REL = BLUEPRINT_ROOT / "manifests/VISUAL_CORRECTION_A11_VALIDATION.json"
DCC_ROOT = Path("SourceAssets/Blender/Props/Giants/BloodAxe/Cairns") / ASSET
BLEND_REL = DCC_ROOT / f"{ASSET}_DCCGameReady_VisualCorrection_A11.blend"
MANIFEST_REL = DCC_ROOT / f"{ASSET}_VISUAL_CORRECTION_A11_MANIFEST.json"
EXPORT_ROOT = Path("SourceAssets/Exports/Props/Giants/BloodAxe/Cairns") / ASSET / "VisualCorrection_A11"
OUTPUT_ROOT_REL = Path("Saved/Automation/DCC") / ASSET / "Production/VisualCorrection_A11"
FINAL_REL = OUTPUT_ROOT_REL / f"{ASSET}_FINAL_CORRECTED_3D_A11.png"
FINAL_RGBA_REL = OUTPUT_ROOT_REL / f"{ASSET}_FINAL_CORRECTED_3D_A11_OBJECT_RGBA.png"
FINAL_AUDIT_REL = OUTPUT_ROOT_REL / "FINAL_RENDER_AUDIT_A11.json"


def load_module() -> Any:
    spec = importlib.util.spec_from_file_location("a005_a09_audit_support", SUPPORT)
    if spec is None or spec.loader is None:
        raise RuntimeError(f"cannot load {SUPPORT}")
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


def component_bounds(obj: Any, indices: Any) -> Dict[str, List[float]]:
    values = [[float(obj.data.vertices[index].co[axis]) for index in indices] for axis in range(3)]
    minimum = [min(axis_values) for axis_values in values]
    maximum = [max(axis_values) for axis_values in values]
    return {"min": minimum, "max": maximum, "dimensions": [maximum[index] - minimum[index] for index in range(3)]}


def main() -> int:
    support = load_module()
    support.CONTRACT = "A005-CR-VISUAL-CORRECTION-A11"
    support.PLAN_REL = PLAN_REL
    support.VALIDATION_REL = VALIDATION_REL
    support.A09_BLEND_REL = BLEND_REL
    support.MANIFEST_REL = MANIFEST_REL
    support.EXPORT_ROOT = EXPORT_ROOT
    support.ASSEMBLED_FBX_RELS = {
        "LOD0": EXPORT_ROOT / f"{ASSET}_VisualCorrection_A11.fbx",
        "LOD1": EXPORT_ROOT / f"{ASSET}_VisualCorrection_A11_LOD1.fbx",
        "LOD2": EXPORT_ROOT / f"{ASSET}_VisualCorrection_A11_LOD2.fbx",
        "LOD3": EXPORT_ROOT / f"{ASSET}_VisualCorrection_A11_LOD3.fbx",
    }
    support.MODULE_FBX_RELS = {
        "C001": EXPORT_ROOT / "Modules" / f"{ASSET}_C001_Monolith_A11.fbx",
        "C002": EXPORT_ROOT / "Modules" / f"{ASSET}_C002_UpperCourse_A11.fbx",
        "C003": EXPORT_ROOT / "Modules" / f"{ASSET}_C003_LowerCourse_A11.fbx",
        "C004": EXPORT_ROOT / "Modules" / f"{ASSET}_C004_RubbleApron_A11.fbx",
    }
    support.MODULE_OBJECTS = {
        "C001": f"{ASSET}_C001_MONOLITH_A11",
        "C002": f"{ASSET}_C002_UPPER_COURSE_A11",
        "C003": f"{ASSET}_C003_LOWER_COURSE_A11",
        "C004": f"{ASSET}_C004_RUBBLE_APRON_A11",
    }
    support.OUTPUT_ROOT_REL = OUTPUT_ROOT_REL
    support.FINAL_REL = FINAL_REL
    support.FINAL_RGBA_REL = FINAL_RGBA_REL
    support.FINAL_AUDIT_REL = FINAL_AUDIT_REL
    support.A09_BC_REL = Path("SourceAssets/Textures/Props/Giants/BloodAxe/Cairns") / ASSET / "VisualCorrection_A11/T_GIA_BloodAxeCairnstone_A005_VF_A11_BC.png"

    legacy_result = support.main()
    validation_path = ROOT / VALIDATION_REL
    validation = json.loads(validation_path.read_text(encoding="utf-8"))
    plan = json.loads((ROOT / PLAN_REL).read_text(encoding="utf-8"))
    manifest = json.loads((ROOT / MANIFEST_REL).read_text(encoding="utf-8"))

    # A11 closes the three inherited receiver top loops. Reclassify the two
    # A09-only topology expectations against the A11 closed-receiver contract.
    for record in validation["gates"]:
        if record["id"] == "G05_module_components_and_counts":
            modules = record["detail"]
            components = [modules[name]["topology"]["components"] for name in ("C001", "C002", "C003", "C004")]
            declared_counts = [plan["modules"][name]["stone_count"] for name in ("C002", "C003", "C004")]
            passed = components == [1, 20, 25, 33] and declared_counts == [19, 24, 32] and manifest.get("A11_closed_receiver_top_caps") is True
            record.update(
                {
                    "status": "pass" if passed else "fail",
                    "detail": {
                        "component_counts": components,
                        "declared_visible_stone_counts": declared_counts,
                        "closed_receiver_components": 3,
                        "policy": "one closed receiver plus the declared independent stones in each A11 base module",
                    },
                }
            )
        elif record["id"] == "G10_topology_and_declared_open_receiver_collars":
            detail = record["detail"]
            lod0 = detail["LOD0"]
            module_topology = detail["modules"]
            passed = (
                lod0 == {"components": 79, "boundary_edges": 0, "nonmanifold_edges": 0, "degenerate_faces": 0}
                and [module_topology[name]["boundary_edges"] for name in ("C001", "C002", "C003", "C004")] == [0, 0, 0, 0]
            )
            record.update(
                {
                    "id": "G10_topology_and_closed_receiver_caps",
                    "status": "pass" if passed else "fail",
                    "detail": {
                        "LOD0": lod0,
                        "modules": module_topology,
                        "policy": "A11 closes all hidden receiver top loops; all LOD0 components are manifold and have no boundary edges",
                    },
                }
            )

    import bpy  # type: ignore

    bpy.ops.wm.open_mainfile(filepath=str(ROOT / BLEND_REL))
    c002 = bpy.data.objects[support.MODULE_OBJECTS["C002"]]
    components = support.component_indices(c002.data)
    component_records = [component_bounds(c002, indices) for indices in components]
    visible_components = [record for record in component_records if record["min"][2] >= 22.9]
    visible_min = [min(record["min"][axis] for record in visible_components) for axis in range(3)]
    visible_max = [max(record["max"][axis] for record in visible_components) for axis in range(3)]
    visible_dimensions = [visible_max[index] - visible_min[index] for index in range(3)]

    extra_gates = []

    def gate(gate_id: str, passed: bool, detail: Any) -> None:
        extra_gates.append({"id": gate_id, "status": "pass" if passed else "fail", "detail": detail})

    a10_record = plan["authority_inputs"]["a10_pixel_exact_measurement"]
    gate("G21_A10_measurement_authority", support.sha256_file(ROOT / a10_record["path"]) == a10_record["sha256"], a10_record)
    expected_extents = {component: plan["modules"][component]["outer_extent_cm"] for component in ("C002", "C003", "C004")}
    actual_extents = {component: manifest["a11_modules"][component]["outer_extent_cm"] for component in expected_extents}
    gate("G22_A10_exact_visible_footprints", all(support.close(actual_extents[name], expected_extents[name], 1.0e-6) for name in expected_extents), {"expected": expected_extents, "actual": actual_extents})
    interval = plan["modules"]["C002"]["approved_height_interval_cm"]
    height = visible_dimensions[2]
    gate("G23_C002_height_inside_approved_interval", len(visible_components) == 19 and interval[0] <= height <= interval[1] and abs(height - 11.25) <= 1.0e-4, {"visible_stone_components": len(visible_components), "actual_visible_bounds_cm": {"min": visible_min, "max": visible_max, "dimensions": visible_dimensions}, "approved_interval_cm": interval})
    receiver_policy = manifest.get("receiver_overlap_policy", "")
    gate("G24_hidden_interface_interpretation_declared", manifest.get("A11_construction_decisions_are_interpretation") is True and manifest.get("A11_top_contact_closure_claimed_as_evidence") is False and "source-hidden" in receiver_policy, {"receiver_overlap_policy": receiver_policy})
    gate("G25_no_A09_geometry_or_Unreal_escalation", manifest.get("A09_assembled_geometry_inputs") == 0 and manifest.get("unreal_outputs") == 0 and manifest.get("fully_game_ready") is False, {"A09_assembled_geometry_inputs": manifest.get("A09_assembled_geometry_inputs"), "unreal_outputs": manifest.get("unreal_outputs"), "fully_game_ready": manifest.get("fully_game_ready")})
    render_audit = json.loads((ROOT / FINAL_AUDIT_REL).read_text(encoding="utf-8"))
    gate("G26_owner_view_interface_background", render_audit["interface_alpha_gate"]["pass"] is True and render_audit["interface_alpha_gate"]["background_leak_pixels"] == 0 and manifest.get("A11_closed_receiver_top_caps") is True, {"interface_alpha_gate": render_audit["interface_alpha_gate"], "closed_receiver_top_caps": manifest.get("A11_closed_receiver_top_caps")})

    validation["gates"].extend(extra_gates)
    passed = sum(1 for record in validation["gates"] if record["status"] == "pass")
    total = len(validation["gates"])
    complete = passed == total
    validation.update(
        {
            "schema": "aerathea.a005_visual_correction_a11_validation.v1",
            "contract_id": "A005-CR-VISUAL-CORRECTION-A11",
            "status": "pass_candidate_pending_flamestrike_visual_review" if complete else "blocked_a11_independent_audit",
            "artifact_classification": "proof only",
            "pipeline_status": "DCC game-ready candidate" if complete else "candidate blocked",
            "gate_summary": {"passed": passed, "total": total},
            "legacy_support_result_before_A11_topology_reclassification": legacy_result,
        }
    )
    validation_path.write_text(json.dumps(validation, indent=2) + "\n", encoding="utf-8")
    print(json.dumps(validation, indent=2))
    return 0 if complete else 1


if __name__ == "__main__":
    raise SystemExit(main())
