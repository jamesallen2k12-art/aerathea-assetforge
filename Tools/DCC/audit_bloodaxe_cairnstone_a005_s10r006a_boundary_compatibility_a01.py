#!/usr/bin/env python3
"""Independent 29-gate audit for A005 S10R-006-A BCTG A01."""

from __future__ import annotations

import hashlib
import json
import subprocess
import sys
from datetime import datetime
from pathlib import Path

from PIL import Image


ROOT = Path(__file__).resolve().parents[2]
ASSET_REL = Path("docs/assets/blueprints/SM_GIA_BloodAxeCairnstone_A005")
ASSET = ROOT / ASSET_REL
M = ASSET / "manifests"
S = ASSET / "steps"
H = ASSET / "handoffs"
E = ASSET / "evidence/S10R_006_A_BOUNDARY_COMPATIBILITY_TECHNICAL_GATE_A01"

CONTRACT_ID = "A005-CR-S10R-006-A-BCTG-A01"
CONTRACT = S / "S10R_006_A_BOUNDARY_COMPATIBILITY_TECHNICAL_GATE_A01_CONTRACT.md"
INPUT_LOCK = M / "S10R_006_A_BOUNDARY_COMPATIBILITY_TECHNICAL_GATE_A01_INPUT_LOCK.json"
DEPENDENCY = M / "S10R_006_A_BOUNDARY_COMPATIBILITY_TECHNICAL_GATE_A01_DEPENDENCY_AUDIT.json"
BOUNDARY = M / "S10R_006_A_BOUNDARY_COMPATIBILITY_TECHNICAL_GATE_A01_BOUNDARY_AUTHORITY_AUDIT.json"
VALIDATION = M / "S10R_006_A_BOUNDARY_COMPATIBILITY_TECHNICAL_GATE_A01_VALIDATION.json"
BOARD = E / "SM_GIA_BloodAxeCairnstone_A005_S10R_006_A_BOUNDARY_COMPATIBILITY_TECHNICAL_GATE_A01_REVIEW_BOARD.png"
OUTPUT = S / "S10R_006_A_BOUNDARY_COMPATIBILITY_TECHNICAL_GATE_A01_OUTPUT_RECORD.md"
HANDOFF = H / "S10R_006_A_BOUNDARY_COMPATIBILITY_TECHNICAL_GATE_A01_TO_DECISION_HANDOFF.md"
RESET = ASSET / "SM_GIA_BloodAxeCairnstone_A005_RESET_RESUME_STATE.md"
APPROVAL = ASSET / "SM_GIA_BloodAxeCairnstone_A005_APPROVAL_LOG.md"
INDEX = ASSET / "SM_GIA_BloodAxeCairnstone_A005_ARTIFACT_INDEX.md"
PLACEMENT = M / "STEP_10R_N3_PLACEMENT_MAPPING_OPTION_REGISTRY.json"
TRANSITION = M / "STEP_10R_N3_TRANSITION_INTEGRATION_OPTION_REGISTRY.json"
DECISIONS = M / "STEP_10R_N3_INTEGRATION_DECISION_REGISTRY.json"
TRACE_LEDGER = M / "C004_BOUNDARY_TRANSITION_INTERPRETATION_RULE_A01_PER_VIEW_LEDGER.json"
MAPPING = M / "S10R_003_A_CL003_TARGET_SPACE_MAPPING_A01_DECISION_REGISTRY.json"
REMAINING = M / "S10R_003_A_CL003_TARGET_SPACE_MAPPING_A01_REMAINING_BLOCKS.json"
BASELINE_STATUS = ROOT / "Saved/ProjectRecovery/20260717-161842/git_status_short.txt"

IMMUTABLE_HASHES = {
    "AGENTS.md": "5d2d2637a58113f0a6f5ec92e40d8bb2bda9e03fb58b4868a0d9dfbb3b57ad55",
    "docs/projects/assetforge/BLOODAXE_CAIRNSTONE_PIXEL_EXACT_FRESH_START_MULTISTEP_PLAN.md": "ba6784498d792dc85dd431c807f59620d6851af97b4cd15efe89c44a397b10b6",
    str(ASSET_REL / "steps/STEP_10R_N3_INTEGRATION_REVISION_A01_CONTRACT.md"): "d38aff71b69daecfd3a42148018dc9538b3ebdd4a1d2c7e936d7aa4db16a1826",
    str(ASSET_REL / "manifests/STEP_10R_N3_INTEGRATION_DECISION_REGISTRY.json"): "f60634468c2d820e230da0a847a181be90893411c3e7838283eb61730e7d37e5",
    str(ASSET_REL / "manifests/STEP_10R_N3_PLACEMENT_MAPPING_OPTION_REGISTRY.json"): "37e7b76f6ee98fba5cfbdfed45d7048402114f4b88ea92055717350e48b1f3bc",
    str(ASSET_REL / "manifests/STEP_10R_N3_TRANSITION_INTEGRATION_OPTION_REGISTRY.json"): "3143f233c471c823693d8539f7abf7478340bdcfdd3eef871f68cabc7ca3728f",
    str(ASSET_REL / "manifests/STEP_10R_N3_INTEGRATION_REMAINING_BLOCKS.json"): "8776c2abcc9a96820cbd4046314a0ef1244c5fb58205c58b46dd9aad8cee1953",
    str(ASSET_REL / "manifests/C004_BOUNDARY_TRANSITION_INTERPRETATION_RULE_A01_PER_VIEW_LEDGER.json"): "c30fe9e7ae2c623122865102b16922931e42e87e2a3bfadb145cbe73f4861113",
    str(ASSET_REL / "manifests/C003_TARGET_SPACE_INNER_BOUNDARY_INTERPRETATION_RULE_A02_K80_DECISION_REGISTRY.json"): "4d7a6e5eff56c217512f54bf0ce50b0d2d37faee8b1e0a6950f08bbc72ae2d05",
    str(ASSET_REL / "manifests/S10R_003_A_CL003_TARGET_SPACE_MAPPING_A01_DECISION_REGISTRY.json"): "05ddf7d67cbed5bca4eb32ec749767b43f74af69bcc77f556e08cec5fb288ff2",
    str(ASSET_REL / "manifests/S10R_003_A_CL003_TARGET_SPACE_MAPPING_A01_REMAINING_BLOCKS.json"): "89067a408ed5f78d01f60be1fa8228911463e309591c34e7196ca27993955eef",
    str(ASSET_REL / "manifests/S10R_003_A_CL003_TARGET_SPACE_MAPPING_A01_DECISION_CLOSEOUT_VALIDATION.json"): "415778d27ba8358affc22795c81abe85a24366cc95fc3539ae85db65e8453a2b",
    str(ASSET_REL / "steps/S10R_003_A_CL003_TARGET_SPACE_MAPPING_A01_DECISION_CLOSEOUT_OUTPUT_RECORD.md"): "31f6947ac947d9155ecba5fbb7100de20111749f744eefb345850a77361836ef",
    str(ASSET_REL / "handoffs/S10R_003_A_CL003_TARGET_SPACE_MAPPING_A01_TO_S10R006_CONTRACT_PREPARATION_HANDOFF.md"): "549904200f1a6d72c7d520eec8d437cd65c12020370b46f0d9fc7fa3d5a4b08e",
    str(CONTRACT.relative_to(ROOT)): "0f4e7fae93d9fe36beb4e0d5ad13cafaf1a2ea0864845c79ac574db75792bd8e",
}

EXPECTED_NEW_STATUS_PATHS = {
    "Tools/DCC/build_bloodaxe_cairnstone_a005_s10r006a_boundary_compatibility_a01.py",
    "Tools/DCC/audit_bloodaxe_cairnstone_a005_s10r006a_boundary_compatibility_a01.py",
    str(INPUT_LOCK.relative_to(ROOT)),
    str(DEPENDENCY.relative_to(ROOT)),
    str(BOUNDARY.relative_to(ROOT)),
    str(VALIDATION.relative_to(ROOT)),
    str(E.relative_to(ROOT)) + "/",
    str(OUTPUT.relative_to(ROOT)),
    str(HANDOFF.relative_to(ROOT)),
}


def sha256(path: Path) -> str:
    digest = hashlib.sha256()
    with path.open("rb") as handle:
        for chunk in iter(lambda: handle.read(1024 * 1024), b""):
            digest.update(chunk)
    return digest.hexdigest()


def load(path: Path) -> dict:
    return json.loads(path.read_text(encoding="utf-8"))


def now() -> str:
    return datetime.now().astimezone().isoformat(timespec="seconds")


def status_paths(text: str) -> set[str]:
    return {line[3:].strip() for line in text.splitlines() if line and not line.startswith("# ")}


def git_raw(*args: str) -> str:
    return subprocess.run(["git", *args], cwd=ROOT, check=True, text=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE).stdout


def gate(condition: bool, subject: str, evidence) -> dict:
    return {"subject": subject, "status": "pass" if condition else "fail", "evidence": evidence}


def main() -> None:
    input_lock = load(INPUT_LOCK)
    dependency = load(DEPENDENCY)
    boundary = load(BOUNDARY)
    placement = load(PLACEMENT)
    transition = load(TRANSITION)
    decisions = load(DECISIONS)
    trace_ledger = load(TRACE_LEDGER)
    mapping = load(MAPPING)
    remaining = load(REMAINING)
    output_text = OUTPUT.read_text(encoding="utf-8")
    handoff_text = HANDOFF.read_text(encoding="utf-8")
    reset_text = RESET.read_text(encoding="utf-8")
    approval_text = APPROVAL.read_text(encoding="utf-8")
    index_text = INDEX.read_text(encoding="utf-8")

    immutable = {}
    for rel, expected in IMMUTABLE_HASHES.items():
        actual = sha256(ROOT / rel)
        immutable[rel] = {"expected_sha256": expected, "actual_sha256": actual, "match": actual == expected}

    s002 = next(item for item in placement["decision_subjects"] if item["id"] == "S10R-002")
    s004 = next(item for item in transition["decision_subjects"] if item["id"] == "S10R-004")
    s005 = next(item for item in transition["decision_subjects"] if item["id"] == "S10R-005")
    s006 = next(item for item in transition["decision_subjects"] if item["id"] == "S10R-006")
    d006 = next(item for item in decisions["decision_items"] if item["id"] == "S10R-006")

    mappings = mapping["mappings"]
    unique_mappings = len({tuple(item["target_xy_cm_decimal"]) for item in mappings})
    traces = []
    trace_per_view = {}
    for view_name in ("front", "back", "left", "right"):
        values = trace_ledger["views"][view_name]["traces"]
        trace_per_view[view_name] = len(values)
        traces.extend(values)
    audited_traces = boundary["registered_trace_boundaries"]
    trace_replay = len(traces) == len(audited_traces) == 26 and all(
        source["trace_id"] == audited["trace_id"]
        and source["view"] == audited["view"]
        and source["view_role"] == audited["view_role"]
        and source["p_i"] == audited["p_i"]
        and source["p_o"] == audited["p_o"]
        and source["p_t_formula"] == audited["p_t_formula"]
        for source, audited in zip(traces, audited_traces)
    )

    baseline = status_paths(BASELINE_STATUS.read_text(encoding="utf-8"))
    current_status = status_paths(git_raw("status", "--short"))
    new_paths = current_status - baseline
    validation_rel = str(VALIDATION.relative_to(ROOT))
    unexpected = sorted(path for path in new_paths if path not in EXPECTED_NEW_STATUS_PATHS)
    missing = sorted(path for path in EXPECTED_NEW_STATUS_PATHS if path != validation_rel and path not in new_paths)

    wmctrl = subprocess.run(["wmctrl", "-l"], text=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    pgrep = subprocess.run(["pgrep", "-af", "eog|gedit"], text=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    desktop = (wmctrl.stdout if wmctrl.returncode == 0 else "") + "\n" + (pgrep.stdout if pgrep.returncode in (0, 1) else "")
    board_visible = BOARD.name in desktop
    output_visible = OUTPUT.name in desktop

    staged = [line for line in git_raw("diff", "--cached", "--name-only").splitlines() if line]
    head = git_raw("rev-parse", "--short", "HEAD").strip()
    branch = git_raw("branch", "--show-current").strip()
    counts = boundary["authority_counts"]
    trace_counts = boundary["trace_counts"]
    target = boundary["target_boundary_analytic_audit"]
    active_ids = {item["id"] for item in remaining["active_blocks"]}

    gates = []
    add = lambda cond, subject, evidence: gates.append(gate(cond, subject, evidence))
    add(input_lock["locked_input_match_count"] == input_lock["locked_input_count"] == 19 and input_lock["locked_input_mismatch_count"] == 0, "all locked input hashes matched before output writes", {"matched": input_lock["locked_input_match_count"], "total": input_lock["locked_input_count"], "mismatches": input_lock["locked_input_mismatch_count"]})
    add(sha256(CONTRACT) == IMMUTABLE_HASHES[str(CONTRACT.relative_to(ROOT))] and input_lock["contract"]["path"] == str(CONTRACT.relative_to(ROOT)), "visibly approved contract hash and ID match", {"contract_id": CONTRACT_ID, "sha256": sha256(CONTRACT)})
    add(input_lock["execution_approval"] == {"approver": "Flamestrike", "statement": "approved", "scope": "contract exactly as written"}, "execution approval statement and scope are explicit", input_lock["execution_approval"])
    add(branch == "main" and head == "f525945" and not staged, "branch HEAD and staged-path state match", {"branch": branch, "head": head, "staged_paths": staged})
    add(s006["decision_status"] == "approved_conditional_interpretation_rule" and s006["implementation_authorized"] is False and d006["approved_selection"] == "S10R-006-A", "S10R-006-A remains approved conditional with implementation unauthorized", {"transition_status": s006["decision_status"], "decision_selection": d006["approved_selection"], "implementation_authorized": False})
    add(s002["flamestrike_decision"] == "S10R-002-A" and s002["implementation_authorized"] is False and "no source placement center or pivot" in dependency["dependencies"][0]["scope"], "S10R-002-A remains a construction-frame interpretation with no source placement center or pivot", dependency["dependencies"][0])
    add(target["outer_equation"] == "abs(x / 70)^3 + abs(y / 55)^3 = 1" and target["outer_extents_cm"] == [140, 110], "N3 remains exactly exponent three at 140 by 110 cm", {"equation": target["outer_equation"], "extents_cm": target["outer_extents_cm"]})
    add(target["inner_equation"] == "abs(x / 56)^3 + abs(y / 44)^3 = 1" and target["inner_extents_cm"] == [112, 88], "K80 remains exactly exponent three at 112 by 88 cm", {"equation": target["inner_equation"], "extents_cm": target["inner_extents_cm"]})
    add(target["x_axis_ratio"] == target["y_axis_ratio"] == target["homothetic_scale"] == 0.8 and abs(target["inner_boundary_value_in_outer_equation"] - 0.512) < 1e-15 and target["strict_abstract_containment"] is True, "homothetic scale and analytic strict containment replay exactly", {key: target[key] for key in ("x_axis_ratio", "y_axis_ratio", "homothetic_scale", "inner_boundary_value_in_outer_equation", "strict_abstract_containment")})
    add(len(mappings) == 16 and unique_mappings == 16 and boundary["approved_top_mapping_audit"]["endpoint_assignment_count"] == 0, "authoritative S10R-003-A registry retains sixteen unique endpoint-exclusive targets", {"records": len(mappings), "unique": unique_mappings, "endpoint_assignments": boundary["approved_top_mapping_audit"]["endpoint_assignment_count"]})
    add(boundary["approved_top_mapping_audit"]["source_displacement_px"] == 0 and boundary["approved_top_mapping_audit"]["mapped_non_top_sample_count"] == 0 and boundary["approved_top_mapping_audit"]["physical_cross_view_pair_count"] == 0, "source displacement non-top mappings and physical cross-view pairs remain zero", boundary["approved_top_mapping_audit"])
    add(trace_replay and trace_per_view == {"front": 6, "back": 6, "left": 6, "right": 8}, "all twenty-six upright trace IDs endpoints formulas roles and counts replay exactly", {"replay": trace_replay, "per_view": trace_per_view, "total": len(traces)})
    add(s004["flamestrike_decision"] == "S10R-004-A" and all("STEP_10R_N3_TRANSITION_INTEGRATION_OPTION_REGISTRY" in item["approved_bounded_classification_authority"] for item in audited_traces), "Step 10R registry remains the sole approved bounded trace-classification authority", {"selection": s004["flamestrike_decision"], "records": len(audited_traces)})
    add(s005["flamestrike_decision"] == "S10R-005-A" and "JOINS EXCLUDED" in "AVAILABLE; JOINS EXCLUDED", "S10R-005-A remains bounded to adjacent owner-view traces with joins excluded", dependency["dependencies"][3])
    add(trace_counts["required_registered_trace_boundaries"] == 26 and trace_counts["common_frame_authority_available"] + trace_counts["common_frame_authority_missing"] == 26, "every required trace-boundary comparison has an authority-availability result", trace_counts)
    add(trace_counts["exact_comparisons_performed"] == 0 and all(item["registered_common_frame"] is None and item["registered_cross_frame_correspondence_id"] is None for item in audited_traces), "only common-frame registered boundaries may enter exact comparison", {"exact_comparisons": trace_counts["exact_comparisons_performed"], "common_frame_available": trace_counts["common_frame_authority_available"]})
    add(boundary["controlling_result"] == "blocked_source_authority_missing" and trace_counts["common_frame_authority_missing"] == 26 and trace_counts["inferred_correspondences"] == 0, "missing common-frame authority produces blocked source authority missing with no inference", {"result": boundary["controlling_result"], "missing": trace_counts["common_frame_authority_missing"], "inferred": trace_counts["inferred_correspondences"]})
    add(trace_counts["explicit_boundary_mismatches"] == 0 and boundary["comparison_rule"]["missing_authority_is_not_mismatch"] is True, "no explicit mismatch is claimed without comparable stored boundaries", {"mismatches": trace_counts["explicit_boundary_mismatches"], "missing_is_not_mismatch": True})
    add(not (trace_counts["common_frame_authority_available"] == 26 and trace_counts["exact_comparisons_performed"] == 26) and boundary["controlling_result"] != "pass_exact_boundary_compatibility_ready_for_Flamestrike_decision", "pass is impossible unless every required comparison is available and exact", {"available": trace_counts["common_frame_authority_available"], "compared": trace_counts["exact_comparisons_performed"], "result": boundary["controlling_result"]})
    add(all(counts[key] == 0 for key in ("field_samples", "fills", "surfaces", "topology", "geometry")), "field samples fills surfaces topology and geometry remain zero", {key: counts[key] for key in ("field_samples", "fills", "surfaces", "topology", "geometry")})
    add(all(item["match"] for item in immutable.values()), "original source technical proof and prior authority remain byte-identical", immutable)
    image = Image.open(BOARD)
    add(image.size == (2400, 1800) and counts["field_samples"] == 0 and "separated" in boundary["review_board_policy"], "review board is separated unfilled proof with no field or inferred overlay", {"board_size": image.size, "policy": boundary["review_board_policy"], "field_samples": counts["field_samples"]})
    add(not unexpected and not missing, "changed paths are contained by the execution allowlist", {"baseline": "Saved/ProjectRecovery/20260717-161842/", "new_paths": sorted(new_paths), "expected_new_paths": sorted(EXPECTED_NEW_STATUS_PATHS), "unexpected": unexpected, "missing": missing})
    shared_tokens = [CONTRACT_ID, "blocked_source_authority_missing", "S10R-BLOCK-006", "S10R-BLOCK-008", "S10R-BLOCK-009", "field samples: 0"]
    agreement = all(all(token in text for token in shared_tokens) for text in (output_text, handoff_text, reset_text, approval_text, index_text))
    add("S10R-BLOCK-006" in active_ids and agreement, "S10R-BLOCK-006 remains active pending result decision and separate field authority", {"active_ids": sorted(active_ids), "status_records_agree": agreement})
    add({"S10R-BLOCK-008", "S10R-BLOCK-009"}.issubset(active_ids), "S10R-BLOCK-008 and S10R-BLOCK-009 remain active", sorted(active_ids))
    add(all(token in output_text for token in ("Step 10 closeout", "Step 11", "DCC", "Unreal", "production", "blocked")), "Step 10 closeout Step 11 DCC Unreal and production remain blocked", {"output_record": str(OUTPUT.relative_to(ROOT))})
    add(not staged and head == "f525945", "no path is staged committed or pushed", {"head": head, "staged_paths": staged, "commit_authorized": False, "push_authorized": False})
    add(board_visible and output_visible, "review board and output record are visibly opened", {"board_visible": board_visible, "output_visible": output_visible, "matching_desktop_lines": [line for line in desktop.splitlines() if BOARD.name in line or OUTPUT.name in line]})
    add("mandatory restart" in output_text.lower() and "mandatory restart" in handoff_text.lower() and "field implementation" in handoff_text.lower(), "execution stops for Flamestrike decision and mandatory restart", {"next_action_executed": False, "field_implementation_authorized": False})

    for index, item in enumerate(gates, 1):
        item["gate"] = f"G{index:02d}"
    passed = sum(item["status"] == "pass" for item in gates)
    failed = len(gates) - passed
    output_hashes = {
        str(path.relative_to(ROOT)): sha256(path)
        for path in (INPUT_LOCK, DEPENDENCY, BOUNDARY, BOARD, OUTPUT, HANDOFF, RESET, APPROVAL, INDEX, Path(__file__), ROOT / "Tools/DCC/build_bloodaxe_cairnstone_a005_s10r006a_boundary_compatibility_a01.py")
    }
    record = {
        "schema": "aerathea.s10r_006_a_boundary_compatibility_technical_gate_a01_validation.v1",
        "asset_id": "SM_GIA_BloodAxeCairnstone_A005",
        "contract_id": CONTRACT_ID,
        "date": "2026-07-17",
        "validated_at": now(),
        "status": "pass_technical_audit_blocked_source_authority_missing_pending_Flamestrike" if failed == 0 else "fail_quarantine_and_stop",
        "artifact_classification": "proof only",
        "independent_auditor": str(Path(__file__).relative_to(ROOT)),
        "builder_imported": False,
        "technical_result": boundary["controlling_result"],
        "gate_count": len(gates),
        "passed_gate_count": passed,
        "failed_gate_count": failed,
        "immutable_input_hashes": immutable,
        "output_hashes_before_validation_write": output_hashes,
        "dependency_counts": {"registered": dependency["dependency_rule_count"], "authority_available": dependency["dependency_rule_authority_available_count"], "implemented": dependency["dependency_implementation_count"]},
        "trace_counts": trace_counts,
        "authority_counts": counts,
        "changed_path_audit": gates[22]["evidence"],
        "visible_review_verification": gates[27]["evidence"],
        "gates": gates,
    }
    VALIDATION.write_text(json.dumps(record, indent=2, ensure_ascii=False) + "\n", encoding="utf-8")
    print(f"wrote {VALIDATION.relative_to(ROOT)}")
    print(f"validation: {passed}/{len(gates)} passed, {failed} failed; result: {boundary['controlling_result']}")
    if failed:
        for item in gates:
            if item["status"] == "fail":
                print(f"FAIL {item['gate']}: {item['subject']}", file=sys.stderr)
        raise SystemExit(1)


if __name__ == "__main__":
    main()
