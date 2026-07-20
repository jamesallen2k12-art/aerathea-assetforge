#!/usr/bin/env python3
"""Read-only independent audit for the final A005 Step 10 disposition."""

from __future__ import annotations

import hashlib
import json
import subprocess
from pathlib import Path


ROOT = Path(__file__).resolve().parents[2]
BASE = ROOT / "docs/assets/blueprints/SM_GIA_BloodAxeCairnstone_A005"
PREFIX = "S10R_008_R2_A_FINAL_STEP10_TEN_ITEM_DISPOSITION_A01"
LOCK = BASE / f"manifests/{PREFIX}_INPUT_LOCK.json"
DECISIONS = BASE / f"manifests/{PREFIX}_DECISION_REGISTRY.json"
REJECTED = BASE / f"manifests/{PREFIX}_REJECTED_OPTION_RECORD.json"
OWNERSHIP = BASE / f"manifests/{PREFIX}_SOURCE_INTERPRETATION_OWNERSHIP_MAP.json"
BLOCKS = BASE / f"manifests/{PREFIX}_REMAINING_BLOCKS.json"
CONTRACT = BASE / f"steps/{PREFIX}_CONTRACT.md"
OUTPUT = BASE / f"steps/{PREFIX}_OUTPUT_RECORD.md"
HANDOFF = BASE / f"handoffs/{PREFIX}_TO_STEP11_HANDOFF.md"
ORIGINAL_OPTIONS = BASE / "manifests/STEP_10_INTERPRETATION_OPTION_REGISTRY.json"
R9 = BASE / "manifests/S10R_006_R9_A_CORNER_GAP_TO_FIELD_COUPLING_RULE_A01_RULE_REGISTRY.json"
BASELINE_STATUS = ROOT / "Saved/ProjectRecovery/20260720-142349/git_status_short.txt"


def load_json(path: Path) -> dict:
    with path.open("r", encoding="utf-8") as handle:
        return json.load(handle)


def sha256(path: Path) -> str:
    digest = hashlib.sha256()
    with path.open("rb") as handle:
        for chunk in iter(lambda: handle.read(1024 * 1024), b""):
            digest.update(chunk)
    return digest.hexdigest()


def git_lines(*args: str) -> list[str]:
    result = subprocess.run(
        ["git", *args], cwd=ROOT, check=True, text=True,
        stdout=subprocess.PIPE, stderr=subprocess.PIPE,
    )
    return [line for line in result.stdout.splitlines() if line]


def main() -> int:
    lock = load_json(LOCK)
    decisions = load_json(DECISIONS)
    rejected = load_json(REJECTED)
    ownership = load_json(OWNERSHIP)
    blocks = load_json(BLOCKS)
    original = load_json(ORIGINAL_OPTIONS)
    r9 = load_json(R9)
    contract_text = CONTRACT.read_text(encoding="utf-8")
    output_text = OUTPUT.read_text(encoding="utf-8")
    handoff_text = HANDOFF.read_text(encoding="utf-8")

    gates: list[tuple[str, bool, str]] = []

    def gate(name: str, condition: bool, detail: str) -> None:
        gates.append((name, bool(condition), detail))

    immutable_mismatches = [
        item["path"] for item in lock["immutable_inputs"]
        if not (ROOT / item["path"]).is_file()
        or sha256(ROOT / item["path"]) != item["sha256"]
    ]
    mutable_mismatches = [
        item["path"] for item in lock["pre_action_mutable_status_snapshots"]
        if not (ROOT / item["path"]).is_file()
        or sha256(ROOT / item["path"]) != item["sha256"]
    ]

    gate("G01_contract_identity", "A005-CR-S10R-008-R2-A-FINAL-I10-DISP-A01" in contract_text, "contract ID present")
    gate("G02_full_flamestrike_authority", "full approval and authorization to complete this step" in contract_text, "exact delegated authority recorded")
    gate("G03_blueprint_boundary", "does not override the higher-priority Step 10 Blueprint boundary" in contract_text and "R9 evaluation" in contract_text, "implementation exclusion explicit")
    gate("G04_input_lock_counts", lock["counts"] == {"immutable_inputs": 22, "pre_action_mutable_status_snapshots": 3, "total_locked_or_snapshotted_inputs": 25}, "22 immutable plus 3 mutable")
    gate("G05_immutable_hashes", not immutable_mismatches, f"mismatches={immutable_mismatches}")
    gate("G06_mutable_pre_action_hashes", not mutable_mismatches, f"mismatches={mutable_mismatches}")

    expected_ids = [f"I10-{index:03d}" for index in range(1, 11)]
    items = decisions["decision_items"]
    item_ids = [item["id"] for item in items]
    expected_rule_ids = [
        "I10-001-R1-A-TARGET-SPACE-NO-RECTIFICATION",
        "I10-002-R1-A-VIEW-OWNED-FACETED-ENVELOPE",
        "I10-003-R1-A-SEPARATE-NESTED-COURSES",
        "I10-004-R1-A-N3-OUTER-PERIMETER",
        "I10-005-R1-A-FACE-OWNED-VISIBLE-DECORATION",
        "I10-006-R1-B-INDEPENDENT-WATERTIGHT-OCCLUDED-OVERLAP",
        "I10-007-R1-A-FLAT-Z0-BOTTOM",
        "I10-008-R1-A-SEPARATE-PRIMARY-WATERTIGHT-COMPONENTS",
        "I10-009-R1-A-CONSTRUCTION-ORIGIN-GROUND-PIVOT",
        "I10-010-R1-A-R5-R7-R9-BOUNDED-OWNERSHIP",
    ]
    gate("G07_route_a_selected", decisions["route_decision"]["selected"] == "S10R-008-R1-A" and decisions["route_decision"]["not_selected"] == ["S10R-008-R1-B", "S10R-008-R1-BLOCK"], "exact route selection")
    gate("G08_item_ids", item_ids == expected_ids, f"ids={item_ids}")
    gate("G09_item_count", len(items) == 10 and decisions["counts"]["current_dispositions"] == 10, "10 current dispositions")
    gate("G10_rule_ids", [item["approved_rule_id"] for item in items] == expected_rule_ids, "ten expected current rule IDs")
    gate("G11_all_approved_interpretation", all(item["decision"] == "approved_interpretation_rule" for item in items), "all ten are approved interpretation rules")
    gate("G12_all_bounded_classification", all(item["artifact_classification"] == "authoritative bounded interpretation" for item in items), "all ten bounded")
    gate("G13_all_unimplemented", all(item["implementation_status"] == "not_started" for item in items), "implementation not started")
    gate("G14_every_item_has_nonclaims", all(item["non_claims"] for item in items), "explicit non-claims on every item")
    gate("G15_decision_counts", decisions["counts"]["approved_interpretation_rules"] == 10 and decisions["counts"]["remains_blocked_items"] == 0 and decisions["counts"]["implemented_rules"] == 0 and decisions["counts"]["evaluated_rules"] == 0, "10 approved; zero pending/evaluated/implemented")
    gate("G16_global_zero_outputs", all(value == 0 for value in decisions["global_non_claims"].values()), "all global output counts zero")
    gate("G17_r9_zero_outputs", all(value == 0 for value in r9["output_counts"].values()), "R9 output counts remain zero")
    gate("G18_r9_authorization_unchanged", r9["authorization_flags"]["rule_evaluation_authorized"] is False and r9["authorization_flags"]["field_implementation_authorized"] is False, "R9 still unevaluated and unimplemented")

    original_option_ids = {
        option["id"]
        for item in original["decision_items"]
        for option in item["options"]
    }
    accounted_option_ids = (
        {item["id"] for item in rejected["superseded_candidate_options"]}
        | {item["id"] for item in rejected["rejected_candidate_options"]}
        | set(rejected["not_selected_block_options"])
    )
    gate("G19_historical_options_exact", original_option_ids == accounted_option_ids and len(original_option_ids) == 30, "30/30 historical options accounted")
    gate("G20_historical_option_counts", rejected["counts"] == {"superseded_candidate_options": 10, "rejected_candidate_options": 10, "not_selected_block_options": 10, "historical_options_accounted": 30, "historical_files_modified": 0}, "10 superseded, 10 rejected, 10 block options")
    gate("G21_historical_preservation", decisions["counts"]["historical_authority_files_modified"] == 0 and rejected["historical_registry_modified"] is False, "historical files unchanged")
    gate("G22_ownership_complete", ownership["counts"]["approved_interpretation_items"] == 10 and ownership["counts"]["pending_interpretation_items"] == 0 and ownership["source_and_interpretation_separated"] is True, "ownership complete and separated")

    resolved_ids = [item["id"] for item in blocks["resolved_blocks"]]
    active_ids = [item["id"] for item in blocks["active_blocks"]]
    gate("G23_decision_blocks_resolved", resolved_ids == ["S10R-BLOCK-006", "S10R-BLOCK-008"], "006 and 008 resolved at decision level")
    gate("G24_production_block_active", active_ids == ["S10R-BLOCK-009"] and blocks["counts"]["active_remaining_blocks"] == 1, "009 remains active")
    gate("G25_step10_complete", blocks["routing"]["step10_complete"] is True and blocks["routing"]["mandatory_restart_required"] is True, "Step 10 complete with restart")
    gate("G26_step11_boundary", blocks["routing"]["step11_contract_preparation_authorized_after_restart"] is True and blocks["routing"]["step11_execution_authorized"] is False, "Step 11 preparation only")
    gate("G27_output_boundary", "Step 10 decision gate: complete" in output_text and "Evaluated R9 instances: `0`" in output_text and "Step 11 execution: not authorized" in output_text, "output preserves zero implementation")
    gate("G28_handoff_boundary", "Step 11 contract preparation only after restart" in handoff_text and "Still Unauthorized" in handoff_text, "handoff is preparation-only")

    staged = git_lines("diff", "--cached", "--name-only")
    gate("G29_no_precloseout_staging", staged == [], f"staged={staged}")

    baseline = set(BASELINE_STATUS.read_text(encoding="utf-8").splitlines())
    current = set(git_lines("status", "--short"))
    new_status = current - baseline
    allowed_new_status = {
        f"?? Tools/DCC/audit_bloodaxe_cairnstone_a005_s10r008_r2_a_final_step10_ten_item_disposition_a01.py",
        f"?? docs/assets/blueprints/SM_GIA_BloodAxeCairnstone_A005/steps/{PREFIX}_CONTRACT.md",
        f"?? docs/assets/blueprints/SM_GIA_BloodAxeCairnstone_A005/manifests/{PREFIX}_INPUT_LOCK.json",
        f"?? docs/assets/blueprints/SM_GIA_BloodAxeCairnstone_A005/manifests/{PREFIX}_DECISION_REGISTRY.json",
        f"?? docs/assets/blueprints/SM_GIA_BloodAxeCairnstone_A005/manifests/{PREFIX}_REJECTED_OPTION_RECORD.json",
        f"?? docs/assets/blueprints/SM_GIA_BloodAxeCairnstone_A005/manifests/{PREFIX}_SOURCE_INTERPRETATION_OWNERSHIP_MAP.json",
        f"?? docs/assets/blueprints/SM_GIA_BloodAxeCairnstone_A005/manifests/{PREFIX}_REMAINING_BLOCKS.json",
        f"?? docs/assets/blueprints/SM_GIA_BloodAxeCairnstone_A005/steps/{PREFIX}_OUTPUT_RECORD.md",
        f"?? docs/assets/blueprints/SM_GIA_BloodAxeCairnstone_A005/handoffs/{PREFIX}_TO_STEP11_HANDOFF.md",
    }
    gate("G30_prevalidation_write_scope", new_status == allowed_new_status, f"new_status={sorted(new_status)}")

    passed = sum(1 for _, ok, _ in gates if ok)
    failed = len(gates) - passed
    result = {
        "technical_result": "pass_30_of_30" if failed == 0 else "blocked_final_step10_audit_failure",
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
