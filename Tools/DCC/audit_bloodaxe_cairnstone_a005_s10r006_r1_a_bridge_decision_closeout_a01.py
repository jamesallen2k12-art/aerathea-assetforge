#!/usr/bin/env python3
"""Emit and audit the bounded A005 S10R-006-R1-A bridge closeout.

The script copies each frozen mapping record without recalculation, records
only the separately approved decision classification, preserves the holdouts
as proof, and rejects every physical, field, geometry, or downstream claim.
"""

from __future__ import annotations

import argparse
import copy
import hashlib
import json
import subprocess
import sys
from collections import Counter
from datetime import datetime
from pathlib import Path


ROOT = Path(__file__).resolve().parents[2]
ASSET_REL = Path("docs/assets/blueprints/SM_GIA_BloodAxeCairnstone_A005")
ASSET = ROOT / ASSET_REL
MANIFESTS = ASSET / "manifests"
STEPS = ASSET / "steps"
HANDOFFS = ASSET / "handoffs"

CONTRACT_ID = "A005-CR-S10R-006-R1-A-NPOB-DC-A01"
CONTRACT = STEPS / "S10R_006_R1_A_NORMALIZED_PRIMARY_OWNER_BRIDGE_A01_DECISION_CLOSEOUT_CONTRACT.md"
ROUTE_DECISION = MANIFESTS / "S10R_006_R1_A_NORMALIZED_PRIMARY_OWNER_BRIDGE_DECISION_REGISTRY.json"
EXECUTION_CONTRACT = STEPS / "S10R_006_R1_A_NORMALIZED_PRIMARY_OWNER_BRIDGE_EXECUTION_CONTRACT.md"
INPUT_LOCK = MANIFESTS / "S10R_006_R1_A_NORMALIZED_PRIMARY_OWNER_BRIDGE_A01_INPUT_LOCK.json"
MAPPING = MANIFESTS / "S10R_006_R1_A_NORMALIZED_PRIMARY_OWNER_BRIDGE_A01_MAPPING_LEDGER.json"
HOLDOUT = MANIFESTS / "S10R_006_R1_A_NORMALIZED_PRIMARY_OWNER_BRIDGE_A01_VALIDATION_HOLDOUT_AUDIT.json"
TECHNICAL_VALIDATION = MANIFESTS / "S10R_006_R1_A_NORMALIZED_PRIMARY_OWNER_BRIDGE_A01_VALIDATION.json"
BOARD = ASSET / "evidence/S10R_006_R1_A_NORMALIZED_PRIMARY_OWNER_BRIDGE_A01/SM_GIA_BloodAxeCairnstone_A005_S10R_006_R1_A_NORMALIZED_PRIMARY_OWNER_BRIDGE_A01_REVIEW_BOARD.png"
TECHNICAL_OUTPUT = STEPS / "S10R_006_R1_A_NORMALIZED_PRIMARY_OWNER_BRIDGE_A01_OUTPUT_RECORD.md"
TECHNICAL_HANDOFF = HANDOFFS / "S10R_006_R1_A_NORMALIZED_PRIMARY_OWNER_BRIDGE_A01_TO_DECISION_HANDOFF.md"
PRIOR_DECISION = MANIFESTS / "S10R_006_A_BOUNDARY_COMPATIBILITY_TECHNICAL_GATE_A01_DECISION_REGISTRY.json"
PRIOR_BLOCKS = MANIFESTS / "S10R_006_A_BOUNDARY_COMPATIBILITY_TECHNICAL_GATE_A01_REMAINING_BLOCKS.json"

DECISION = MANIFESTS / "S10R_006_R1_A_NORMALIZED_PRIMARY_OWNER_BRIDGE_A01_DECISION_REGISTRY.json"
BLOCKS = MANIFESTS / "S10R_006_R1_A_NORMALIZED_PRIMARY_OWNER_BRIDGE_A01_REMAINING_BLOCKS.json"
CLOSEOUT_VALIDATION = MANIFESTS / "S10R_006_R1_A_NORMALIZED_PRIMARY_OWNER_BRIDGE_A01_DECISION_CLOSEOUT_VALIDATION.json"
OUTPUT = STEPS / "S10R_006_R1_A_NORMALIZED_PRIMARY_OWNER_BRIDGE_A01_DECISION_CLOSEOUT_OUTPUT_RECORD.md"
HANDOFF = HANDOFFS / "S10R_006_R1_A_NORMALIZED_PRIMARY_OWNER_BRIDGE_A01_TO_POST_DECISION_BLOCKED_ROUTING_HANDOFF.md"
RESET = ASSET / "SM_GIA_BloodAxeCairnstone_A005_RESET_RESUME_STATE.md"
APPROVAL = ASSET / "SM_GIA_BloodAxeCairnstone_A005_APPROVAL_LOG.md"
INDEX = ASSET / "SM_GIA_BloodAxeCairnstone_A005_ARTIFACT_INDEX.md"
BASELINE_STATUS = ROOT / "Saved/ProjectRecovery/20260717-180113/git_status_short.txt"


PRE_OUTPUT_HASHES = {
    "AGENTS.md": "5d2d2637a58113f0a6f5ec92e40d8bb2bda9e03fb58b4868a0d9dfbb3b57ad55",
    "docs/projects/assetforge/BLOODAXE_CAIRNSTONE_PIXEL_EXACT_FRESH_START_MULTISTEP_PLAN.md": "ba6784498d792dc85dd431c807f59620d6851af97b4cd15efe89c44a397b10b6",
    str(ASSET_REL / "SM_GIA_BloodAxeCairnstone_A005_RESET_RESUME_STATE.md"): "272befa9a47b78b993c75e54fc6e2a8120f81c7c445d54d90d418b90d71a9186",
    str(ASSET_REL / "SM_GIA_BloodAxeCairnstone_A005_APPROVAL_LOG.md"): "12a59ab72f5386dd5e52be7e77f661771edc87e78c8760f7913657c60d8d67dc",
    str(ASSET_REL / "SM_GIA_BloodAxeCairnstone_A005_ARTIFACT_INDEX.md"): "d75e37a0f4124cc376bde16a77387c02c7b94db00215909f757f68fd7997be77",
    str(ROUTE_DECISION.relative_to(ROOT)): "14961845f35c2005b727cea46b19a378db9b79432da0b930c1872e68bf1a63b7",
    str(EXECUTION_CONTRACT.relative_to(ROOT)): "7d7ff2c0ea7a556599b89bd0bb7e01f501e59cdf77bbcef4cb8b58b48f03e69f",
    str(INPUT_LOCK.relative_to(ROOT)): "3f5d446a248e57aa120449e5c7701f6727584dc78a279124f555609a68419b55",
    str(MAPPING.relative_to(ROOT)): "b69513e7cf9661e112b2f489ecc8932c472740089f2355e61cfcd4ac93c37dbc",
    str(HOLDOUT.relative_to(ROOT)): "d09e6adba7bde2bab729086b70d7fb3be215953ac72f29a6697b3c917211f1f2",
    str(TECHNICAL_VALIDATION.relative_to(ROOT)): "bd8ef3ec68db937a3062b4b63ebc3ab8946c4bdde3e8faf263d21b788de8400d",
    str(BOARD.relative_to(ROOT)): "d8ac6a958cf847055f3cd6b85295c87ae05b95c14d53b7a1e2ced6d768fbb181",
    str(TECHNICAL_OUTPUT.relative_to(ROOT)): "bf90c958dd946938b673be760735d422c38c07dee7277269adbcc4ed71b3b795",
    str(TECHNICAL_HANDOFF.relative_to(ROOT)): "d1e6c7eacef8a83e66272cd95d26e5ee0117edcc14ab9b961d344bd9444d95ca",
    str(PRIOR_DECISION.relative_to(ROOT)): "609a912568ccea01f65a4ec6060c53a97b93679d5a647125bed835bd9b28759b",
    str(PRIOR_BLOCKS.relative_to(ROOT)): "5d3458789dd0317d66493b137225dcd604d05ff5c73483b4df8946bea453eb07",
    "Saved/ProjectRecovery/20260717-175129/git_status_short.txt": "7d27234f06ddec3aaa58481a9493f07edd7a194b5be79b17c3ce0fc46d4c0cc4",
    str(CONTRACT.relative_to(ROOT)): "d6c806620c15722750f111dd4321d6f384d31a268c8b966d5587d411dd942415",
}

IMMUTABLE_AFTER_STATUS_UPDATES = {
    key: value
    for key, value in PRE_OUTPUT_HASHES.items()
    if key
    not in {
        str(RESET.relative_to(ROOT)),
        str(APPROVAL.relative_to(ROOT)),
        str(INDEX.relative_to(ROOT)),
    }
}

EXECUTION_CREATED = {
    str(DECISION.relative_to(ROOT)),
    str(BLOCKS.relative_to(ROOT)),
    str(CLOSEOUT_VALIDATION.relative_to(ROOT)),
    str(OUTPUT.relative_to(ROOT)),
    str(HANDOFF.relative_to(ROOT)),
    "Tools/DCC/audit_bloodaxe_cairnstone_a005_s10r006_r1_a_bridge_decision_closeout_a01.py",
}


def sha256(path: Path) -> str:
    digest = hashlib.sha256()
    with path.open("rb") as handle:
        for chunk in iter(lambda: handle.read(1024 * 1024), b""):
            digest.update(chunk)
    return digest.hexdigest()


def load_json(path: Path) -> dict:
    return json.loads(path.read_text(encoding="utf-8"))


def write_json(path: Path, value: dict) -> None:
    path.write_text(json.dumps(value, indent=2, ensure_ascii=False) + "\n", encoding="utf-8")


def now_local() -> str:
    return datetime.now().astimezone().isoformat(timespec="seconds")


def verify_hashes(expected: dict[str, str]) -> dict[str, dict[str, object]]:
    results = {}
    for rel, wanted in expected.items():
        path = ROOT / rel
        actual = sha256(path) if path.is_file() else None
        results[rel] = {
            "expected_sha256": wanted,
            "actual_sha256": actual,
            "match": actual == wanted,
        }
    return results


def all_match(results: dict[str, dict[str, object]]) -> bool:
    return all(item["match"] is True for item in results.values())


def git_output(*args: str) -> str:
    return subprocess.run(
        ["git", *args],
        cwd=ROOT,
        check=True,
        text=True,
        stdout=subprocess.PIPE,
        stderr=subprocess.PIPE,
    ).stdout.rstrip()


def status_paths(text: str) -> set[str]:
    paths = set()
    for line in text.splitlines():
        if not line:
            continue
        path = line[3:]
        if " -> " in path:
            path = path.split(" -> ", 1)[1]
        paths.add(path.strip())
    return paths


def emit_authority() -> None:
    precheck = verify_hashes(PRE_OUTPUT_HASHES)
    if not all_match(precheck):
        failures = [path for path, result in precheck.items() if not result["match"]]
        raise SystemExit(f"STOP: locked pre-output hash mismatch: {failures}")
    if git_output("branch", "--show-current") != "main":
        raise SystemExit("STOP: branch is not main")
    if git_output("rev-parse", "HEAD") != "f5259456b05a95ff5f7422ba2cabf0e288a85d03":
        raise SystemExit("STOP: HEAD changed")
    if git_output("rev-parse", "assetforge/main") != "f5259456b05a95ff5f7422ba2cabf0e288a85d03":
        raise SystemExit("STOP: assetforge/main changed")
    if git_output("diff", "--cached", "--name-only"):
        raise SystemExit("STOP: staged paths exist")

    mapping = load_json(MAPPING)
    holdout = load_json(HOLDOUT)
    technical_validation = load_json(TECHNICAL_VALIDATION)
    records = mapping.get("records", [])
    holdouts = holdout.get("records", [])
    if len(records) != 12:
        raise SystemExit(f"STOP: mapping ledger contains {len(records)} records, expected 12")
    if len(holdouts) != 14:
        raise SystemExit(f"STOP: holdout audit contains {len(holdouts)} records, expected 14")
    if technical_validation.get("passed_gate_count") != 24 or technical_validation.get("failed_gate_count") != 0:
        raise SystemExit("STOP: frozen technical validation is not 24/24 pass")

    copied = [
        {
            "mapping_id": record["mapping_id"],
            "trace_id": record["trace_id"],
            "frozen_record": copy.deepcopy(record),
            "decision_classification": "approved bounded interpretation",
            "authority_scope": "bounded symbolic normalized primary-owner bridge implementation only",
        }
        for record in records
    ]
    holdout_ids = [
        {
            "holdout_id": record["holdout_id"],
            "trace_id": record["trace_id"],
            "view": record["view"],
            "classification": "proof only validation holdout",
        }
        for record in holdouts
    ]

    decision = {
        "schema": "aerathea.s10r_006_r1_a_normalized_primary_owner_bridge_a01_decision_registry.v1",
        "asset_id": "SM_GIA_BloodAxeCairnstone_A005",
        "contract_id": CONTRACT_ID,
        "date": "2026-07-17",
        "executed_at": now_local(),
        "status": "normalized_primary_owner_bridge_twelve_record_bounded_symbolic_implementation_approved",
        "artifact_classification": "authoritative for bounded S10R-006-R1-A normalized primary-owner bridge implementation only",
        "technical_result": "pass_normalized_primary_owner_bridge_ready_for_Flamestrike_decision",
        "approval_chain": {
            "route_decision_approval": "yes approved",
            "bridge_execution_approval": "I approve it",
            "codex_evidence_recommendation": "approve the exact candidate result within its bounded symbolic scope",
            "flamestrike_result_approval": "I agree with your recommendation approved",
            "closeout_contract_preparation_approval": "approved create it",
            "closeout_execution_approval": "yes approved",
            "final_authority": "Flamestrike",
        },
        "decision": "Approve the exact twelve frozen mapping records as an approved bounded symbolic implementation of S10R-006-R1-A only; preserve all fourteen holdouts as proof only and preserve every physical, field, geometry, and downstream stop.",
        "approved_mappings": copied,
        "validation_holdouts": holdout_ids,
        "frozen_proof": {
            "mapping_ledger_sha256": PRE_OUTPUT_HASHES[str(MAPPING.relative_to(ROOT))],
            "holdout_audit_sha256": PRE_OUTPUT_HASHES[str(HOLDOUT.relative_to(ROOT))],
            "technical_validation_sha256": PRE_OUTPUT_HASHES[str(TECHNICAL_VALIDATION.relative_to(ROOT))],
            "technical_validation_gates_passed": 24,
            "technical_validation_gates_failed": 0,
            "review_board_sha256": PRE_OUTPUT_HASHES[str(BOARD.relative_to(ROOT))],
            "frozen_mapping_ledger_classification": mapping["artifact_classification"],
            "frozen_mapping_ledger_changed": False,
            "frozen_holdout_audit_classification": "proof only",
            "frozen_holdout_audit_changed": False,
        },
        "authority_counts": {
            "approved_bounded_symbolic_bridge_records": 12,
            "front_primary_XZ_records": 6,
            "left_primary_YZ_records": 6,
            "proof_only_validation_holdouts": 14,
            "back_validation_only_holdouts": 6,
            "right_validation_only_holdouts": 8,
            "source_trace_changes": 0,
            "order_ambiguities": 0,
            "order_reversals": 0,
            "introduced_crossings": 0,
            "explicit_bounded_holdout_contradictions": 0,
            "physical_source_target_transforms": 0,
            "physical_cross_view_pairs": 0,
            "target_trace_coordinates": 0,
            "source_centers": 0,
            "pivots": 0,
            "anchors": 0,
            "field_samples": 0,
            "fills": 0,
            "surfaces": 0,
            "topology": 0,
            "geometry": 0,
        },
        "interpretation_limits": {
            "source_measurement_claim": False,
            "physical_correspondence_claim": False,
            "physical_target_space_transform_claim": False,
            "physical_cross_view_agreement_claim": False,
            "target_coordinate_claim": False,
            "field_surface_topology_geometry_claim": False,
        },
        "historical_authority": {
            "blocked_source_authority_missing_result": "preserved_authoritative_technical_history",
            "prior_decision_registry_sha256": PRE_OUTPUT_HASHES[str(PRIOR_DECISION.relative_to(ROOT))],
            "prior_remaining_blocks_sha256": PRE_OUTPUT_HASHES[str(PRIOR_BLOCKS.relative_to(ROOT))],
        },
        "block_routing": {
            "S10R-BLOCK-006": "active_bounded_bridge_approved_no_field_and_no_physical_correspondence",
            "S10R-BLOCK-008": "active_prior_step10_decisions_pending",
            "S10R-BLOCK-009": "active_global_production_block",
        },
        "field_implementation_authorized": False,
        "step10_closeout_authorized": False,
        "step11_authorized": False,
        "dcc_authorized": False,
        "unreal_authorized": False,
        "production_authorized": False,
        "staging_authorized": False,
        "commit_authorized": False,
        "push_authorized": False,
        "next_gate": "none_selected_core_reassessment_required_after_mandatory_restart",
        "pre_action_checkpoint": "Saved/ProjectRecovery/20260717-180113/",
        "mandatory_restart_required": True,
        "pre_output_locked_input_verification": {
            "verified_before_output_writes": True,
            "matched": len(precheck),
            "total": len(precheck),
            "mismatches": 0,
            "hashes": precheck,
        },
    }

    remaining = {
        "schema": "aerathea.s10r_006_r1_a_normalized_primary_owner_bridge_a01_remaining_blocks.v1",
        "asset_id": "SM_GIA_BloodAxeCairnstone_A005",
        "contract_id": CONTRACT_ID,
        "date": "2026-07-17",
        "status": "bridge_decision_closed_all_three_blocks_and_downstream_stops_active",
        "artifact_classification": "authoritative for post-bridge-decision blocked routing only",
        "closed_decision": {
            "subject": "exact twelve-record bounded symbolic normalized primary-owner bridge implementation",
            "decision": "approved bounded interpretation",
            "resolved_block_ids": [],
        },
        "active_blocks": [
            {
                "id": "S10R-BLOCK-006",
                "subject": "S10R-006-A transition field and physical correspondence",
                "approved_condition": "exact twelve-record bounded symbolic normalized bridge",
                "blocked_fact": "No field exists and no physical source-to-target or cross-view correspondence was created.",
                "status": "active_bounded_bridge_approved_no_field_and_no_physical_correspondence",
                "field_sample_count": 0,
            },
            {
                "id": "S10R-BLOCK-008",
                "subject": "historical Step 10 decision set",
                "blocked_fact": "Historical Step 10 items not resolved by bounded decisions remain pending.",
                "status": "active_prior_step10_decisions_pending",
            },
            {
                "id": "S10R-BLOCK-009",
                "subject": "global production authority",
                "blocked_fact": "No filled footprint, source center, pivot, implemented field, topology, surface, or geometry authority exists.",
                "status": "active_global_production_block",
            },
        ],
        "counts": {
            "approved_bounded_symbolic_bridge_records": 12,
            "proof_only_validation_holdouts": 14,
            "resolved_block_ids": 0,
            "active_remaining_blocks": 3,
            "physical_correspondences": 0,
            "target_trace_coordinates": 0,
            "field_samples": 0,
            "fills": 0,
            "surfaces": 0,
            "topology": 0,
            "geometry": 0,
        },
        "historical_result": "blocked_source_authority_missing remains authoritative technical history",
        "step10_closeout": "blocked",
        "step11": "blocked",
        "dcc": "blocked",
        "unreal": "blocked",
        "production": "blocked",
        "staging_commit_push": "not_authorized",
        "next_gate": {
            "status": "none_selected_core_reassessment_required_after_mandatory_restart",
            "technical_method_selected": False,
            "contract_created_during_closeout": False,
            "execution_authorized": False,
        },
        "mandatory_restart_required": True,
    }

    write_json(DECISION, decision)
    write_json(BLOCKS, remaining)
    print(f"wrote {DECISION.relative_to(ROOT)}")
    print(f"wrote {BLOCKS.relative_to(ROOT)}")


def check(condition: bool, subject: str, evidence: object) -> dict:
    return {"subject": subject, "status": "pass" if condition else "fail", "evidence": evidence}


def validate() -> None:
    decision = load_json(DECISION)
    blocks = load_json(BLOCKS)
    mapping = load_json(MAPPING)
    holdout = load_json(HOLDOUT)
    technical_validation = load_json(TECHNICAL_VALIDATION)
    source_records = mapping["records"]
    copied = decision["approved_mappings"]
    holdouts = holdout["records"]

    exact_copy = len(copied) == len(source_records) == 12 and all(
        item["mapping_id"] == source["mapping_id"]
        and item["trace_id"] == source["trace_id"]
        and item["frozen_record"] == source
        for item, source in zip(copied, source_records)
    )
    mapping_ids = {item["mapping_id"] for item in copied}
    mapping_trace_ids = {item["trace_id"] for item in copied}
    owner_counts = Counter(item["frozen_record"]["owner_view"] for item in copied)
    holdout_ids = {item["holdout_id"] for item in holdouts}
    holdout_trace_ids = {item["trace_id"] for item in holdouts}
    holdout_counts = Counter(item["view"] for item in holdouts)
    symbolic_ok = all(
        item["frozen_record"]["normalized_transition_identity"] == "v = t"
        and item["frozen_record"]["inner_boundary_identity"]
        == {"id": "C003_TSIB_K80_MEDIUM_APRON", "station": "t = 0; v = 0"}
        and item["frozen_record"]["outer_boundary_identity"]
        == {"id": "TOP_C004_OPIR_N3_ROUNDED_OVAL", "station": "t = 1; v = 1"}
        for item in copied
    )
    holdout_roles_ok = all(
        item["view_role"] == "validation_only"
        and not item["construction_coordinate_created"]
        and not item["physical_pair_created"]
        and item["classification"] == "proof only validation holdout"
        for item in holdouts
    )
    physical_zero = all(
        item["frozen_record"]["physical_source_target_transform"] is None
        and item["frozen_record"]["physical_cross_view_pair"] is None
        and item["frozen_record"]["target_xy_cm"] is None
        and item["frozen_record"]["target_xyz_cm"] is None
        and not item["frozen_record"]["source_center_claim"]
        and not item["frozen_record"]["pivot_claim"]
        and not item["frozen_record"]["anchor_claim"]
        for item in copied
    )
    authority = decision["authority_counts"]
    immutable_hashes = verify_hashes(IMMUTABLE_AFTER_STATUS_UPDATES)

    baseline_paths = status_paths(BASELINE_STATUS.read_text(encoding="utf-8"))
    current_paths = status_paths(git_output("status", "--short"))
    newly_visible_paths = current_paths - baseline_paths
    validation_rel = str(CLOSEOUT_VALIDATION.relative_to(ROOT))
    unexpected_new_paths = sorted(newly_visible_paths - EXECUTION_CREATED)
    missing_created_paths = sorted(
        path for path in EXECUTION_CREATED if path not in current_paths and path != validation_rel
    )

    output_text = OUTPUT.read_text(encoding="utf-8")
    handoff_text = HANDOFF.read_text(encoding="utf-8")
    reset_text = RESET.read_text(encoding="utf-8")
    approval_text = APPROVAL.read_text(encoding="utf-8")
    index_text = INDEX.read_text(encoding="utf-8")
    agreement_tokens = [
        CONTRACT_ID,
        "approved bounded interpretation",
        "S10R-BLOCK-006",
        "S10R-BLOCK-008",
        "S10R-BLOCK-009",
        "mandatory restart",
    ]
    records_agree = all(
        all(token in text for token in agreement_tokens)
        for text in (output_text, handoff_text, reset_text, approval_text, index_text)
    )

    wmctrl = subprocess.run(["wmctrl", "-l"], text=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    windows = wmctrl.stdout if wmctrl.returncode == 0 else ""
    gedit = subprocess.run(["pgrep", "-af", "gedit"], text=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    processes = gedit.stdout if gedit.returncode in (0, 1) else ""
    visible_evidence = windows + "\n" + processes
    output_visible = OUTPUT.name in visible_evidence
    reset_visible = RESET.name in visible_evidence

    active = {item["id"]: item for item in blocks["active_blocks"]}
    classifications = Counter(item["decision_classification"] for item in copied)
    staged = [line for line in git_output("diff", "--cached", "--name-only").splitlines() if line]
    branch = git_output("branch", "--show-current")
    head = git_output("rev-parse", "HEAD")
    remote_head = git_output("rev-parse", "assetforge/main")

    gates = []
    add = lambda condition, subject, evidence: gates.append(check(condition, subject, evidence))
    precheck = decision["pre_output_locked_input_verification"]
    add(precheck["matched"] == 18 and precheck["mismatches"] == 0, "all eighteen locked inputs matched before output writes", precheck)
    add(sha256(CONTRACT) == PRE_OUTPUT_HASHES[str(CONTRACT.relative_to(ROOT))] and decision["contract_id"] == CONTRACT_ID, "visible contract hash and ID match", {"sha256": sha256(CONTRACT), "contract_id": decision["contract_id"]})
    expected_chain = {
        "route_decision_approval": "yes approved",
        "bridge_execution_approval": "I approve it",
        "codex_evidence_recommendation": "approve the exact candidate result within its bounded symbolic scope",
        "flamestrike_result_approval": "I agree with your recommendation approved",
        "closeout_contract_preparation_approval": "approved create it",
        "closeout_execution_approval": "yes approved",
        "final_authority": "Flamestrike",
    }
    add(decision["approval_chain"] == expected_chain, "route execution result preparation and closeout approvals are explicit", decision["approval_chain"])
    add(branch == "main" and head == remote_head == "f5259456b05a95ff5f7422ba2cabf0e288a85d03", "branch and local remote HEAD remain exact", {"branch": branch, "head": head, "assetforge_main": remote_head})
    add(decision["technical_result"] == "pass_normalized_primary_owner_bridge_ready_for_Flamestrike_decision", "technical result remains exact", decision["technical_result"])
    add(technical_validation["passed_gate_count"] == 24 and technical_validation["failed_gate_count"] == 0, "technical validation remains 24/24 pass", {"passed": technical_validation["passed_gate_count"], "failed": technical_validation["failed_gate_count"]})
    add(len(copied) == 12 and len(mapping_ids) == 12 and len(mapping_trace_ids) == 12, "decision contains twelve unique mapping and trace IDs", {"records": len(copied), "mapping_ids": len(mapping_ids), "trace_ids": len(mapping_trace_ids)})
    add(owner_counts == Counter({"front": 6, "left": 6}), "construction owners remain six front and six left", dict(owner_counts))
    add(exact_copy, "all twelve frozen mapping records copy without recalculation", {"matched": 12 if exact_copy else 0, "total": 12})
    add(symbolic_ok, "all twelve mappings remain exact v=t with K80 and N3 endpoint identities", symbolic_ok)
    summary = mapping["summary"]
    add(all(summary[key] == 0 for key in ("source_trace_changes", "order_reversals", "order_ambiguities", "introduced_crossings")), "source changes order defects and crossings remain zero", {key: summary[key] for key in ("source_trace_changes", "order_reversals", "order_ambiguities", "introduced_crossings")})
    add(len(holdouts) == 14 and len(holdout_ids) == 14 and len(holdout_trace_ids) == 14, "holdout audit contains fourteen unique holdout and trace IDs", {"records": len(holdouts), "holdout_ids": len(holdout_ids), "trace_ids": len(holdout_trace_ids)})
    add(holdout_counts == Counter({"back": 6, "right": 8}), "holdouts remain six back and eight right", dict(holdout_counts))
    add(holdout["counts"]["explicit_contradictions"] == 0, "explicit bounded holdout contradictions remain zero", holdout["counts"]["explicit_contradictions"])
    add(holdout_roles_ok, "all holdouts remain proof-only validation records with no construction coordinate or physical pair", holdout_roles_ok)
    add(physical_zero and all(authority[key] == 0 for key in ("physical_source_target_transforms", "physical_cross_view_pairs", "target_trace_coordinates", "source_centers", "pivots", "anchors")), "physical correspondence coordinate center pivot and anchor counts remain zero", {key: authority[key] for key in ("physical_source_target_transforms", "physical_cross_view_pairs", "target_trace_coordinates", "source_centers", "pivots", "anchors")})
    add(all(authority[key] == 0 for key in ("field_samples", "fills", "surfaces", "topology", "geometry")), "field fill surface topology and geometry counts remain zero", {key: authority[key] for key in ("field_samples", "fills", "surfaces", "topology", "geometry")})
    add(classifications == Counter({"approved bounded interpretation": 12}) and decision["artifact_classification"] == "authoritative for bounded S10R-006-R1-A normalized primary-owner bridge implementation only", "only the exact twelve records receive bounded interpretation decision authority", {"registry": decision["artifact_classification"], "record_classifications": dict(classifications)})
    add(all_match(immutable_hashes) and mapping["artifact_classification"] == "candidate implementation of approved bounded interpretation rule pending Flamestrike", "frozen package and mapping-ledger candidate classification remain unchanged", {"hashes": immutable_hashes, "mapping_ledger_classification": mapping["artifact_classification"]})
    historical = decision["historical_authority"]
    add(historical["blocked_source_authority_missing_result"] == "preserved_authoritative_technical_history" and sha256(PRIOR_DECISION) == historical["prior_decision_registry_sha256"] and sha256(PRIOR_BLOCKS) == historical["prior_remaining_blocks_sha256"], "prior blocked source-authority result remains authoritative technical history", historical)
    add(records_agree, "output handoff and three status records agree on bounded authority blocks and restart", {"required_tokens": agreement_tokens, "all_records_match": records_agree})
    add(not unexpected_new_paths and not missing_created_paths, "changed paths remain inside the closeout allowlist", {"baseline": "Saved/ProjectRecovery/20260717-180113/", "new_paths": sorted(newly_visible_paths), "execution_created": sorted(EXECUTION_CREATED), "unexpected": unexpected_new_paths, "missing": missing_created_paths})
    add(set(active) == {"S10R-BLOCK-006", "S10R-BLOCK-008", "S10R-BLOCK-009"} and blocks["counts"]["resolved_block_ids"] == 0, "all three blocks remain active and none is resolved", {"active": sorted(active), "resolved": blocks["counts"]["resolved_block_ids"]})
    add(all(blocks[key] == "blocked" for key in ("step10_closeout", "step11", "dcc", "unreal", "production")) and not any(decision[key] for key in ("field_implementation_authorized", "step10_closeout_authorized", "step11_authorized", "dcc_authorized", "unreal_authorized", "production_authorized")), "Step 10 closeout Step 11 DCC Unreal production and field remain blocked", {key: blocks[key] for key in ("step10_closeout", "step11", "dcc", "unreal", "production")})
    next_gate = blocks["next_gate"]
    add(next_gate["technical_method_selected"] is False and next_gate["contract_created_during_closeout"] is False and next_gate["execution_authorized"] is False and decision["next_gate"] == "none_selected_core_reassessment_required_after_mandatory_restart", "no next technical method or contract is selected or prepared", next_gate)
    add(not staged and branch == "main" and head == remote_head, "no closeout path is staged committed or pushed", {"branch": branch, "head": head, "staged_paths": staged, "commit_authorized": False, "push_authorized": False})
    add(output_visible and reset_visible, "closeout output and reset resume state are visibly opened", {"wmctrl_returncode": wmctrl.returncode, "output_visible": output_visible, "reset_visible": reset_visible, "matching_evidence": [line for line in visible_evidence.splitlines() if OUTPUT.name in line or RESET.name in line]})
    add(decision["mandatory_restart_required"] is True and blocks["mandatory_restart_required"] is True and "mandatory restart" in output_text.lower() and "mandatory restart" in handoff_text.lower(), "execution stops for mandatory restart", {"decision_registry": decision["mandatory_restart_required"], "remaining_blocks": blocks["mandatory_restart_required"], "next_action_executed": False})

    for number, gate in enumerate(gates, 1):
        gate["gate"] = f"G{number:02d}"
    passed = sum(gate["status"] == "pass" for gate in gates)
    failed = len(gates) - passed
    output_hashes = {
        str(path.relative_to(ROOT)): sha256(path)
        for path in (DECISION, BLOCKS, OUTPUT, HANDOFF, RESET, APPROVAL, INDEX, Path(__file__))
    }
    validation = {
        "schema": "aerathea.s10r_006_r1_a_normalized_primary_owner_bridge_a01_decision_closeout_validation.v1",
        "asset_id": "SM_GIA_BloodAxeCairnstone_A005",
        "contract_id": CONTRACT_ID,
        "date": "2026-07-17",
        "validated_at": now_local(),
        "status": "pass_bounded_bridge_decision_closeout_mandatory_restart" if failed == 0 else "fail_closeout_quarantine_and_stop",
        "artifact_classification": "proof only",
        "independent_auditor": str(Path(__file__).relative_to(ROOT)),
        "frozen_builder_or_technical_auditor_imported": False,
        "gate_count": len(gates),
        "passed_gate_count": passed,
        "failed_gate_count": failed,
        "pre_output_locked_hashes": precheck["hashes"],
        "immutable_package_hashes": immutable_hashes,
        "output_hashes_before_validation_write": output_hashes,
        "exact_counts": {
            "approved_bounded_symbolic_mappings": len(copied),
            "unique_mapping_ids": len(mapping_ids),
            "unique_mapping_trace_ids": len(mapping_trace_ids),
            "proof_only_holdouts": len(holdouts),
            "unique_holdout_ids": len(holdout_ids),
            "unique_holdout_trace_ids": len(holdout_trace_ids),
        },
        "authority_counts": authority,
        "changed_path_audit": gates[21]["evidence"],
        "visible_review_verification": gates[26]["evidence"],
        "gates": gates,
        "mandatory_restart_required": True,
    }
    write_json(CLOSEOUT_VALIDATION, validation)
    print(f"wrote {CLOSEOUT_VALIDATION.relative_to(ROOT)}")
    print(f"closeout validation: {passed}/{len(gates)} passed, {failed} failed")
    if failed:
        for gate in gates:
            if gate["status"] == "fail":
                print(f"FAIL {gate['gate']}: {gate['subject']}", file=sys.stderr)
        raise SystemExit(1)


def main() -> None:
    parser = argparse.ArgumentParser()
    group = parser.add_mutually_exclusive_group(required=True)
    group.add_argument("--emit-authority", action="store_true")
    group.add_argument("--validate", action="store_true")
    args = parser.parse_args()
    if args.emit_authority:
        emit_authority()
    else:
        validate()


if __name__ == "__main__":
    main()
