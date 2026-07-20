#!/usr/bin/env python3
"""Read-only independent audit for the A005 post-R9 I10 reconciliation."""

from __future__ import annotations

import hashlib
import json
from pathlib import Path


ROOT = Path(__file__).resolve().parents[2]
BASE = ROOT / "docs/assets/blueprints/SM_GIA_BloodAxeCairnstone_A005"
LOCK = BASE / "manifests/S10R_008_R1_A_POST_R9_I10_RECONCILIATION_A01_INPUT_LOCK.json"
DELTA = BASE / "manifests/S10R_008_R1_A_POST_R9_I10_RECONCILIATION_A01_ITEM_AUTHORITY_DELTA.json"
ROUTES = BASE / "manifests/S10R_008_R1_A_POST_R9_I10_RECONCILIATION_A01_OPTION_REGISTRY.json"
CONTRACT = BASE / "steps/S10R_008_R1_A_POST_R9_I10_RECONCILIATION_A01_CONTRACT.md"
OUTPUT = BASE / "steps/S10R_008_R1_A_POST_R9_I10_RECONCILIATION_A01_OUTPUT_RECORD.md"
HANDOFF = BASE / "handoffs/S10R_008_R1_A_POST_R9_I10_RECONCILIATION_A01_TO_DECISION_HANDOFF.md"


def load_json(path: Path) -> dict:
    with path.open("r", encoding="utf-8") as handle:
        return json.load(handle)


def sha256(path: Path) -> str:
    digest = hashlib.sha256()
    with path.open("rb") as handle:
        for chunk in iter(lambda: handle.read(1024 * 1024), b""):
            digest.update(chunk)
    return digest.hexdigest()


def main() -> int:
    lock = load_json(LOCK)
    delta = load_json(DELTA)
    routes = load_json(ROUTES)
    contract_text = CONTRACT.read_text(encoding="utf-8")
    output_text = OUTPUT.read_text(encoding="utf-8")
    handoff_text = HANDOFF.read_text(encoding="utf-8")

    r3 = load_json(BASE / "manifests/S10R_006_R3_A_ABSTRACT_FIELD_METHOD_A01_METHOD_REGISTRY.json")
    r5 = load_json(BASE / "manifests/S10R_006_R5_A_LANE_BOUNDARY_COUPLING_RULE_A01_RULE_REGISTRY.json")
    r7 = load_json(BASE / "manifests/S10R_006_R7_A_CROSS_VIEW_CORNER_OWNERSHIP_RULE_A01_RULE_REGISTRY.json")
    r9 = load_json(BASE / "manifests/S10R_006_R9_A_CORNER_GAP_TO_FIELD_COUPLING_RULE_A01_RULE_REGISTRY.json")
    k80 = load_json(BASE / "manifests/C003_TARGET_SPACE_INNER_BOUNDARY_INTERPRETATION_RULE_A02_K80_DECISION_REGISTRY.json")
    mapping = load_json(BASE / "manifests/S10R_003_A_CL003_TARGET_SPACE_MAPPING_A01_DECISION_REGISTRY.json")

    gates: list[tuple[str, bool, str]] = []

    def gate(name: str, condition: bool, detail: str) -> None:
        gates.append((name, bool(condition), detail))

    immutable = lock["immutable_inputs"]
    mutable = lock["pre_action_mutable_status_snapshots"]
    immutable_mismatches = [
        entry["path"]
        for entry in immutable
        if not (ROOT / entry["path"]).is_file()
        or sha256(ROOT / entry["path"]) != entry["sha256"]
    ]
    mutable_mismatches = [
        entry["path"]
        for entry in mutable
        if not (ROOT / entry["path"]).is_file()
        or sha256(ROOT / entry["path"]) != entry["sha256"]
    ]

    gate("G01_contract_identity", "A005-CR-S10R-008-R1-A-POSTR9-I10-REC-A01" in contract_text, "contract ID present")
    gate("G02_contract_approval_scope", "ok proceed with your recommendation" in contract_text and "does not select a route" in contract_text, "approval and decision stop explicit")
    gate("G03_input_lock_counts", lock["counts"] == {"immutable_inputs": 19, "pre_action_mutable_status_snapshots": 3, "total_locked_or_snapshotted_inputs": 22}, "19 immutable plus 3 mutable snapshots")
    gate("G04_immutable_hashes", not immutable_mismatches, f"mismatches={immutable_mismatches}")
    gate("G05_mutable_pre_action_hashes", not mutable_mismatches, f"mismatches={mutable_mismatches}")
    gate("G06_k80_authority", k80["selected_option"]["id"] == "C003_TSIB_K80_MEDIUM_APRON" and not k80["selected_option"]["implementation_authorized"], "K80 bounded and unimplemented")
    gate("G07_mapping_authority", mapping["authority_counts"]["approved_source_to_target_mappings"] == 16 and mapping["implementation_authorized"] is False, "16 bounded mappings; no implementation")
    gate("G08_r3_status", r3["status"] == "approved_bounded_symbolic_method_no_field_coupling", "exact R3 status")
    gate("G09_r5_status", r5["status"] == "approved_bounded_symbolic_rule_four_blocked_corner_gaps_unowned", "exact R5 status")
    gate("G10_r7_status", r7["status"] == "approved_bounded_cross_view_corner_ownership_rule_registered_no_implementation", "exact R7 status")
    gate("G11_r9_status", r9["status"] == "approved_bounded_corner_gap_to_field_coupling_rule_registered_no_implementation", "exact R9 status")

    items = delta["decision_items"]
    expected_ids = [f"I10-{index:03d}" for index in range(1, 11)]
    actual_ids = [item["id"] for item in items]
    classes = [item["candidate_post_r9_classification"] for item in items]
    gate("G12_item_ids", actual_ids == expected_ids, f"ids={actual_ids}")
    gate("G13_item_count", len(items) == 10 and delta["counts"]["items_reconciled"] == 10, "10 items")
    gate("G14_all_items_pending", all(item["decision_level_complete"] is False for item in items) and delta["counts"]["current_dispositions_approved"] == 0, "0 current dispositions")
    gate("G15_classification_counts", classes.count("requires_revision") == 7 and classes.count("unaffected_candidate") == 2 and classes.count("blocked_by_dependency") == 1, "7 revision, 2 unaffected, 1 blocked")
    gate("G16_historical_preservation", delta["historical_files_modified"] is False and delta["historical_files_reclassified"] is False, "historical files unchanged")
    gate("G17_resolved_blocks_zero", delta["resolved_block_ids"] == [], "no block resolved")
    gate("G18_active_blocks", [item["id"] for item in delta["active_blocks"]] == ["S10R-BLOCK-006", "S10R-BLOCK-008", "S10R-BLOCK-009"], "three active blocks")

    zero_output_keys = [
        "q_instances", "u_instances", "v_instances", "owner_instances",
        "record_instances", "weight_instances", "boundary_instances",
        "samples", "source_assignments", "transforms", "physical_pairs",
        "target_coordinates", "centers", "pivots", "anchors", "seams",
        "joins", "closures", "fields", "fills", "surfaces", "topology",
        "geometry"
    ]
    gate("G19_r9_zero_outputs", all(r9["output_counts"][key] == 0 for key in zero_output_keys), "all R9 output counts remain zero")
    gate("G20_r9_no_evaluation_or_implementation", r9["authorization_flags"]["rule_evaluation_authorized"] is False and r9["authorization_flags"]["field_implementation_authorized"] is False, "R9 authorization flags false")

    route_ids = [route["id"] for route in routes["routes"]]
    gate("G21_route_registry", route_ids == ["S10R-008-R1-A", "S10R-008-R1-B", "S10R-008-R1-BLOCK"], f"routes={route_ids}")
    gate("G22_one_recommendation", sum(1 for route in routes["routes"] if route["candidate_recommendation"]) == 1 and routes["recommended_route"] == "S10R-008-R1-A", "A is sole recommendation")
    gate("G23_no_route_selected", routes["counts"]["selected_routes"] == 0 and routes["flamestrike_decision"] is None and all(not route["selected"] for route in routes["routes"]), "selection pending")
    gate("G24_all_authorizations_false", all(value is False for value in delta["authorization_flags"].values()) and all(value is False for value in routes["authorization_flags"].values()), "all downstream flags false")
    gate("G25_output_and_handoff_boundary", "No route is selected" in output_text and "No route is selected by this handoff" in handoff_text and "R9 evaluation and implementation remain excluded" in handoff_text, "candidate decision boundary explicit")

    passed = sum(1 for _, ok, _ in gates if ok)
    failed = len(gates) - passed
    result = {
        "technical_result": "pass_25_of_25" if failed == 0 else "blocked_independent_audit_failure",
        "gates_total": len(gates),
        "gates_passed": passed,
        "gates_failed": failed,
        "failed_gate_ids": [name for name, ok, _ in gates if not ok],
        "gates": [
            {"id": name, "status": "pass" if ok else "fail", "detail": detail}
            for name, ok, detail in gates
        ],
    }
    print(json.dumps(result, indent=2))
    return 0 if failed == 0 else 1


if __name__ == "__main__":
    raise SystemExit(main())
