#!/usr/bin/env python3
"""Emit and audit the bounded A005 S10R-003-A mapping decision closeout.

This script never recalculates mapping coordinates.  It copies the exact
registered fields from the frozen candidate ledger after checking every
immutable closeout input, and it validates only the record-level authority
and blocked-routing delta approved by A005-CR-S10R-003-A-MAP-DC-A01.
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

CONTRACT_ID = "A005-CR-S10R-003-A-MAP-DC-A01"
CONTRACT = STEPS / "S10R_003_A_CL003_TARGET_SPACE_MAPPING_A01_DECISION_CLOSEOUT_CONTRACT.md"
LEDGER = MANIFESTS / "S10R_003_A_CL003_TARGET_SPACE_MAPPING_A01_LEDGER.json"
MAPPING_VALIDATION = MANIFESTS / "S10R_003_A_CL003_TARGET_SPACE_MAPPING_A01_VALIDATION.json"
DECISION = MANIFESTS / "S10R_003_A_CL003_TARGET_SPACE_MAPPING_A01_DECISION_REGISTRY.json"
BLOCKS = MANIFESTS / "S10R_003_A_CL003_TARGET_SPACE_MAPPING_A01_REMAINING_BLOCKS.json"
CLOSEOUT_VALIDATION = MANIFESTS / "S10R_003_A_CL003_TARGET_SPACE_MAPPING_A01_DECISION_CLOSEOUT_VALIDATION.json"
OUTPUT = STEPS / "S10R_003_A_CL003_TARGET_SPACE_MAPPING_A01_DECISION_CLOSEOUT_OUTPUT_RECORD.md"
HANDOFF = HANDOFFS / "S10R_003_A_CL003_TARGET_SPACE_MAPPING_A01_TO_S10R006_CONTRACT_PREPARATION_HANDOFF.md"
RESET = ASSET / "SM_GIA_BloodAxeCairnstone_A005_RESET_RESUME_STATE.md"
APPROVAL = ASSET / "SM_GIA_BloodAxeCairnstone_A005_APPROVAL_LOG.md"
INDEX = ASSET / "SM_GIA_BloodAxeCairnstone_A005_ARTIFACT_INDEX.md"
BASELINE_STATUS = ROOT / "Saved/ProjectRecovery/20260717-155655/git_status_short.txt"


PRE_OUTPUT_HASHES = {
    "AGENTS.md": "5d2d2637a58113f0a6f5ec92e40d8bb2bda9e03fb58b4868a0d9dfbb3b57ad55",
    "docs/projects/assetforge/BLOODAXE_CAIRNSTONE_PIXEL_EXACT_FRESH_START_MULTISTEP_PLAN.md": "ba6784498d792dc85dd431c807f59620d6851af97b4cd15efe89c44a397b10b6",
    str(ASSET_REL / "SM_GIA_BloodAxeCairnstone_A005_RESET_RESUME_STATE.md"): "d8d475d4dcc285dac9cf80abd177d77850290f052071a1de8c79081451b914a8",
    str(ASSET_REL / "SM_GIA_BloodAxeCairnstone_A005_APPROVAL_LOG.md"): "b3c2c827eb4ae25a4a400de3d38a9cdd5ba3ebeb33a5d45dd86367e3e8e04f96",
    str(ASSET_REL / "SM_GIA_BloodAxeCairnstone_A005_ARTIFACT_INDEX.md"): "de04e0aa584a3d526f4d53d6f0da1425890cb5b7a9a5aa9edb6404396882e000",
    str(ASSET_REL / "steps/S10R_003_A_CL003_TARGET_SPACE_MAPPING_EXECUTION_A01_CONTRACT.md"): "10dc155b78e2d2e6f15a389a9a247db13450314df2d8e3bc9ba891901b3208f8",
    str(ASSET_REL / "manifests/S10R_003_A_CL003_TARGET_SPACE_MAPPING_A01_INPUT_LOCK.json"): "f49e239bea3b7f163cecc73718772c42a9284b87d7a3aa37d684db6c98110e2c",
    str(ASSET_REL / "manifests/S10R_003_A_CL003_TARGET_SPACE_MAPPING_A01_LEDGER.json"): "eb4cf1d9cab090cf1b7b668924b7510b10374a43768e8cd520656ee13859bbfa",
    str(ASSET_REL / "manifests/S10R_003_A_CL003_TARGET_SPACE_MAPPING_A01_VALIDATION.json"): "e5b3b35463a0d8a77076569319a4e27213dd2a900e14edae2007dbf27c828c5f",
    str(ASSET_REL / "evidence/S10R_003_A_CL003_TARGET_SPACE_MAPPING_A01/SM_GIA_BloodAxeCairnstone_A005_S10R_003_A_CL003_TARGET_SPACE_MAPPING_A01_REVIEW_BOARD.png"): "69f028375ee4da0bf3c1b6e4b19403611637e1daa9733645b688a922caf3f9b7",
    str(ASSET_REL / "steps/S10R_003_A_CL003_TARGET_SPACE_MAPPING_A01_OUTPUT_RECORD.md"): "2a06aac73ab2b60e8d62921b405007c4e42164b8bbdb4a69ef8e67daad6a0d7d",
    str(ASSET_REL / "handoffs/S10R_003_A_CL003_TARGET_SPACE_MAPPING_A01_TO_DECISION_HANDOFF.md"): "34c8c23e22c6c2191fdb1d6763c2956c10202fc04df30f10dc0e16dedbe68621",
    str(ASSET_REL / "manifests/C003_TARGET_SPACE_INNER_BOUNDARY_INTERPRETATION_RULE_A02_K80_DECISION_REGISTRY.json"): "4d7a6e5eff56c217512f54bf0ce50b0d2d37faee8b1e0a6950f08bbc72ae2d05",
    str(ASSET_REL / "manifests/C003_TARGET_SPACE_INNER_BOUNDARY_INTERPRETATION_RULE_A02_K80_REMAINING_BLOCKS.json"): "e3de4150df887e53e3dbc569339daa54b07b1a8bc72cecd7d0a67ab0a7aba883",
    str(ASSET_REL / "manifests/STEP_10R_N3_INTEGRATION_DECISION_REGISTRY.json"): "f60634468c2d820e230da0a847a181be90893411c3e7838283eb61730e7d37e5",
    str(ASSET_REL / "manifests/STEP_10R_N3_PLACEMENT_MAPPING_OPTION_REGISTRY.json"): "37e7b76f6ee98fba5cfbdfed45d7048402114f4b88ea92055717350e48b1f3bc",
    str(ASSET_REL / "manifests/STEP_10R_N3_TRANSITION_INTEGRATION_OPTION_REGISTRY.json"): "3143f233c471c823693d8539f7abf7478340bdcfdd3eef871f68cabc7ca3728f",
    str(ASSET_REL / "manifests/STEP_10R_N3_INTEGRATION_REMAINING_BLOCKS.json"): "8776c2abcc9a96820cbd4046314a0ef1244c5fb58205c58b46dd9aad8cee1953",
    "Saved/ProjectRecovery/20260717-154740/git_status_short.txt": "05b997525bbdd8f2811c2bccdd12748e33c42207d8156cade6f9cff9687f5070",
    str(ASSET_REL / "steps/S10R_003_A_CL003_TARGET_SPACE_MAPPING_A01_DECISION_CLOSEOUT_CONTRACT.md"): "506943f3b6d92c7c1170c3addb9baa1641ad4026b3ea7d4062a61d09f7f33660",
}

TECHNICAL_HASHES = {
    key: value
    for key, value in PRE_OUTPUT_HASHES.items()
    if any(
        marker in key
        for marker in (
            "MAPPING_EXECUTION_A01_CONTRACT",
            "MAPPING_A01_INPUT_LOCK",
            "MAPPING_A01_LEDGER",
            "MAPPING_A01_VALIDATION",
            "MAPPING_A01_REVIEW_BOARD",
            "MAPPING_A01_OUTPUT_RECORD",
            "MAPPING_A01_TO_DECISION_HANDOFF",
        )
    )
}

PRIOR_AUTHORITY_HASHES = {
    key: value
    for key, value in PRE_OUTPUT_HASHES.items()
    if key in ("AGENTS.md", "docs/projects/assetforge/BLOODAXE_CAIRNSTONE_PIXEL_EXACT_FRESH_START_MULTISTEP_PLAN.md")
    or "K80_DECISION_REGISTRY" in key
    or "K80_REMAINING_BLOCKS" in key
    or "STEP_10R_" in key
}
PRIOR_AUTHORITY_HASHES.update(
    {
        str(ASSET_REL / "panels/STEP_03/SM_GIA_BloodAxeCairnstone_A005_STEP_03_TOP.png"): "1bc9750b903a3d9e5689bee3c2c1c7094ccd554c361ff622aa9065d2c5287fdf",
        str(ASSET_REL / "manifests/STEP_04_TOP_CONTACT_EVIDENCE_RECOVERY_A01.json"): "8f9fb86ef631e5785552a61f61e4a2d3085727f1a667bdf59cf904284b1b2eb0",
        str(ASSET_REL / "manifests/STEP_08R_TOP_SECTOR_CLASSIFICATION.json"): "e135db381c6255db0260b5e1ec1016acdc025066ebd784a319f989c8e911675f",
        str(ASSET_REL / "manifests/STEP_09_CROSS_VIEW_CORRESPONDENCE_MANIFEST.json"): "9efadda542ba2358c59b8d4fac4b731e5d877d2007aa1d03b3fe67abac29547f",
        str(ASSET_REL / "manifests/C003_TARGET_SPACE_INNER_BOUNDARY_INTERPRETATION_RULE_A02_OPTION_REGISTRY.json"): "ba24e6b5803deb6af15b5fcf1d7e95f2f088321a63775a32ff39d6350b7423aa",
        str(ASSET_REL / "manifests/C003_TARGET_SPACE_INNER_BOUNDARY_INTERPRETATION_RULE_A02_CURVE_LEDGER.json"): "dc04dab52e922786a99eaa7bbc52cb3620ac41c4784aae56a10b098423952410",
    }
)

EXECUTION_CREATED = {
    str(DECISION.relative_to(ROOT)),
    str(BLOCKS.relative_to(ROOT)),
    str(CLOSEOUT_VALIDATION.relative_to(ROOT)),
    str(OUTPUT.relative_to(ROOT)),
    str(HANDOFF.relative_to(ROOT)),
    "Tools/DCC/audit_bloodaxe_cairnstone_a005_s10r003_mapping_decision_closeout_a01.py",
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
        results[rel] = {"expected_sha256": wanted, "actual_sha256": actual, "match": actual == wanted}
    return results


def all_match(results: dict[str, dict[str, object]]) -> bool:
    return all(item["match"] is True for item in results.values())


def emit_authority() -> None:
    precheck = verify_hashes(PRE_OUTPUT_HASHES)
    if not all_match(precheck):
        failures = [path for path, result in precheck.items() if not result["match"]]
        raise SystemExit(f"STOP: locked pre-output hash mismatch: {failures}")

    ledger = load_json(LEDGER)
    mapping_validation = load_json(MAPPING_VALIDATION)
    records = ledger.get("records", [])
    if len(records) != 16:
        raise SystemExit(f"STOP: frozen ledger contains {len(records)} records, expected 16")
    if mapping_validation.get("passed_gate_count") != 31 or mapping_validation.get("failed_gate_count") != 0:
        raise SystemExit("STOP: frozen mapping validation is not 31/31 pass")

    copied = []
    for record in records:
        copied.append(
            {
                "mapping_id": record["mapping_id"],
                "source_id": record["source_id"],
                "sector": record["sector"],
                "local_rank": record["local_rank"],
                "source_sample_order_within_contact": record["source_sample_order_within_contact"],
                "u_exact": record["u_exact"],
                "u_decimal": record["u_decimal"],
                "target_xy_cm_decimal": copy.deepcopy(record["target_xy_cm_decimal"]),
                "source_displacement_px": record["source_displacement_px"],
                "mapped_view": "top",
                "physical_cross_view_pair": False,
                "source_center_claim": False,
                "pivot_claim": False,
                "physical_C003_dimension_claim": False,
                "snap_anchor_authority": False,
                "field_sample_authority": False,
                "geometry_vertex_authority": False,
                "artifact_classification": "approved bounded interpretation",
                "authority_scope": "abstract target-space CL-003 coordinate only",
            }
        )

    decision = {
        "schema": "aerathea.s10r_003_a_cl003_target_space_mapping_a01_decision_registry.v1",
        "asset_id": "SM_GIA_BloodAxeCairnstone_A005",
        "contract_id": CONTRACT_ID,
        "date": "2026-07-17",
        "executed_at": now_local(),
        "status": "sixteen_record_endpoint_exclusive_mapping_approved_bounded_interpretation",
        "artifact_classification": "authoritative for bounded S10R-003-A mapping only",
        "decision_subject": "exact 16-record endpoint-exclusive equal-rank mapping to abstract K80 CL-003 target coordinates",
        "approval_chain": {
            "flamestrike_delegation": "you choose based on evidence",
            "codex_evidence_decision": "approve",
            "flamestrike_decision_affirmation": "great approved",
            "closeout_contract_preparation_approval": "approved",
            "closeout_execution_approval": "approved",
            "final_authority": "Flamestrike",
        },
        "mapping_rule": copy.deepcopy(ledger["mapping_rule"]),
        "K80": copy.deepcopy(ledger["K80"]),
        "frozen_proof": {
            "ledger_sha256": PRE_OUTPUT_HASHES[str(LEDGER.relative_to(ROOT))],
            "mapping_validation_sha256": PRE_OUTPUT_HASHES[str(MAPPING_VALIDATION.relative_to(ROOT))],
            "mapping_validation_gates_passed": 31,
            "mapping_validation_gates_failed": 0,
            "review_board_sha256": PRE_OUTPUT_HASHES[str((ASSET / "evidence/S10R_003_A_CL003_TARGET_SPACE_MAPPING_A01/SM_GIA_BloodAxeCairnstone_A005_S10R_003_A_CL003_TARGET_SPACE_MAPPING_A01_REVIEW_BOARD.png").relative_to(ROOT))],
            "frozen_ledger_artifact_classification": "candidate interpretation",
            "frozen_ledger_changed": False,
        },
        "mappings": copied,
        "authority_counts": {
            "approved_source_to_target_mappings": 16,
            "approved_abstract_target_CL003_coordinates": 16,
            "approved_top_view_source_ids_consumed": 16,
            "mapped_non_top_samples": 0,
            "source_displacement_px": 0,
            "physical_cross_view_pairs": 0,
            "source_centers": 0,
            "pivots": 0,
            "physical_C003_dimensions": 0,
            "snap_anchors": 0,
            "CL002_closures": 0,
            "annuli": 0,
            "hidden_interfaces": 0,
            "filled_footprints": 0,
            "fields": 0,
            "surfaces": 0,
            "topology": 0,
            "geometry": 0,
        },
        "interpretation_limits": {
            "equal_arc_length_claim": False,
            "source_distance_fit": False,
            "source_measurement_claim": False,
            "physical_cross_view_correspondence_claim": False,
            "source_center_claim": False,
            "pivot_claim": False,
            "physical_C003_dimension_claim": False,
            "snap_anchor_claim": False,
            "contact_closure_claim": False,
            "field_surface_topology_geometry_claim": False,
        },
        "block_routing": {
            "C003-TSIB-A02-K80-BLOCK-001": "resolved_at_bounded_mapping_authority_level",
            "S10R-BLOCK-003": "historical_record_unchanged_resolved_at_bounded_S10R003A_mapping_level",
            "S10R-BLOCK-006": "active_mapping_dependency_satisfied_boundary_compatibility_and_technical_gates_unexecuted_no_field",
            "S10R-BLOCK-008": "active_prior_step10_decisions_pending",
            "S10R-BLOCK-009": "active_global_production_block",
        },
        "implementation_authorized": False,
        "step10_closeout_authorized": False,
        "step11_authorized": False,
        "dcc_authorized": False,
        "unreal_authorized": False,
        "production_authorized": False,
        "staging_authorized": False,
        "commit_authorized": False,
        "push_authorized": False,
        "next_gate": "after mandatory restart, possible preparation only of a separate S10R-006-A boundary-compatibility and technical-gate contract",
        "pre_closeout_checkpoint": "Saved/ProjectRecovery/20260717-155655/",
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
        "schema": "aerathea.s10r_003_a_cl003_target_space_mapping_a01_remaining_blocks.v1",
        "asset_id": "SM_GIA_BloodAxeCairnstone_A005",
        "contract_id": CONTRACT_ID,
        "date": "2026-07-17",
        "status": "bounded_mapping_approved_field_step10_step11_and_production_blocked",
        "artifact_classification": "authoritative for post-mapping blocked routing only",
        "resolved_conditions": [
            {
                "id": "C003-TSIB-A02-K80-BLOCK-001",
                "resolution": "resolved_at_bounded_mapping_authority_level",
                "historical_record_changed": False,
                "authority_expansion_beyond_mapping": False,
            },
            {
                "id": "S10R-BLOCK-003",
                "resolution": "resolved_at_bounded_S10R003A_mapping_level",
                "historical_record_changed": False,
                "authority_expansion_beyond_mapping": False,
            },
        ],
        "active_blocks": [
            {
                "id": "S10R-BLOCK-006",
                "subject": "S10R-006-A normalized ruled field",
                "dependency_state": "S10R-003-A bounded mapping dependency satisfied",
                "blocked_fact": "Every declared boundary-compatibility and technical gate remains unexecuted; no field sample exists.",
                "status": "active_pending_separate_boundary_compatibility_and_technical_gate_contract",
                "field_sample_count": 0,
                "blocked_consumers": ["I10-004", "I10-006", "I10-007", "I10-008", "Step 10 closeout"],
            },
            {
                "id": "S10R-BLOCK-008",
                "subject": "historical Step 10 decision set",
                "blocked_fact": "Historical Step 10 items not resolved by bounded Step 10R decisions remain pending.",
                "status": "active_prior_step10_decisions_pending",
                "blocked_consumers": ["Step 10 closeout", "Step 11"],
            },
            {
                "id": "S10R-BLOCK-009",
                "subject": "global production authority",
                "blocked_fact": "No filled footprint, source center, pivot, implemented field, topology, surface, or geometry authority exists.",
                "status": "active_global_production_block",
                "blocked_consumers": ["DCC", "Unreal", "production"],
            },
        ],
        "counts": {
            "approved_bounded_mappings": 16,
            "resolved_mapping_conditions": 2,
            "active_remaining_blocks": 3,
            "field_samples": 0,
            "surfaces": 0,
            "topology": 0,
            "geometry": 0,
        },
        "preserved_unknowns": [
            "boundary compatibility for S10R-006-A",
            "all declared S10R-006-A technical gate outcomes",
            "CL-002 closure",
            "C-003 annulus and hidden interfaces",
            "source center, pivot, placement, and physical C-003 dimensions",
            "continuous transition field",
            "surface, topology, and geometry",
            "remaining historical Step 10 decisions",
        ],
        "step10_closeout": "blocked",
        "step11": "blocked",
        "dcc": "blocked",
        "unreal": "blocked",
        "production": "blocked",
        "staging_commit_push": "not_authorized",
        "next_gate": {
            "status": "possible_contract_preparation_only_after_mandatory_restart",
            "name": "separate S10R-006-A boundary-compatibility and technical-gate contract",
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
    return {
        "subject": subject,
        "status": "pass" if condition else "fail",
        "evidence": evidence,
    }


def git_output(*args: str) -> str:
    return subprocess.run(
        ["git", *args], cwd=ROOT, check=True, text=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE
    ).stdout.strip()


def status_paths(text: str) -> set[str]:
    paths = set()
    for line in text.splitlines():
        if not line or line.startswith("# "):
            continue
        paths.add(line[3:].strip())
    return paths


def validate() -> None:
    decision = load_json(DECISION)
    blocks = load_json(BLOCKS)
    ledger = load_json(LEDGER)
    mapping_validation = load_json(MAPPING_VALIDATION)
    mappings = decision.get("mappings", [])
    frozen = ledger.get("records", [])

    exact_fields = ["mapping_id", "source_id", "sector", "local_rank", "u_exact", "u_decimal", "target_xy_cm_decimal"]
    exact_copy = len(mappings) == len(frozen) == 16 and all(
        all(mapped.get(field) == source.get(field) for field in exact_fields)
        for mapped, source in zip(mappings, frozen)
    )
    unique_targets = len({tuple(record["target_xy_cm_decimal"]) for record in mappings})
    endpoint_hits = sum(not source.get("endpoint_excluded", False) for source in frozen)
    duplicate_targets = len(mappings) - unique_targets
    source_displacement = sum(record.get("source_displacement_px", 0) for record in mappings)
    mapped_non_top = sum(record.get("mapped_view") != "top" for record in mappings)
    physical_pairs = sum(bool(record.get("physical_cross_view_pair")) for record in mappings)
    claims = decision["authority_counts"]
    technical_hashes = verify_hashes(TECHNICAL_HASHES)
    prior_hashes = verify_hashes(PRIOR_AUTHORITY_HASHES)

    baseline_paths = status_paths(BASELINE_STATUS.read_text(encoding="utf-8"))
    current_status_text = subprocess.run(
        ["git", "status", "--short"],
        cwd=ROOT,
        check=True,
        text=True,
        stdout=subprocess.PIPE,
        stderr=subprocess.PIPE,
    ).stdout
    current_paths = status_paths(current_status_text)
    newly_visible_paths = current_paths - baseline_paths
    allowed_status_updates = {str(path.relative_to(ROOT)) for path in (RESET, APPROVAL, INDEX)}
    anticipated = EXECUTION_CREATED | allowed_status_updates
    unexpected_new_paths = sorted(newly_visible_paths - EXECUTION_CREATED)
    validation_rel = str(CLOSEOUT_VALIDATION.relative_to(ROOT))
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
    gedit_process = subprocess.run(["pgrep", "-af", "gedit"], text=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    gedit_processes = gedit_process.stdout if gedit_process.returncode in (0, 1) else ""
    visible_desktop_evidence = windows + "\n" + gedit_processes
    output_visible = "S10R_003_A_CL003_TARGET_SPACE_MAPPING_A01_DECISION_CLOSEOUT_OUTPUT_RECORD.md" in visible_desktop_evidence
    reset_visible = "SM_GIA_BloodAxeCairnstone_A005_RESET_RESUME_STATE.md" in visible_desktop_evidence

    s10r006_files = [
        str(path.relative_to(ROOT))
        for path in ASSET.rglob("*S10R_006_A*")
        if "S10R_003_A_CL003_TARGET_SPACE_MAPPING_A01_TO_S10R006_CONTRACT_PREPARATION_HANDOFF.md" not in path.name
    ]
    staged_paths = [line for line in git_output("diff", "--cached", "--name-only").splitlines() if line]
    head = git_output("rev-parse", "--short", "HEAD")
    branch = git_output("branch", "--show-current")

    gates = []
    add = lambda condition, subject, evidence: gates.append(check(condition, subject, evidence))
    add(decision["pre_output_locked_input_verification"]["matched"] == 20 and decision["pre_output_locked_input_verification"]["mismatches"] == 0, "all locked input hashes matched before output writes", decision["pre_output_locked_input_verification"])
    add(sha256(CONTRACT) == PRE_OUTPUT_HASHES[str(CONTRACT.relative_to(ROOT))], "visibly approved closeout contract hash matches", {"sha256": sha256(CONTRACT), "contract_id": CONTRACT_ID})
    chain = decision["approval_chain"]
    add(chain == {"flamestrike_delegation": "you choose based on evidence", "codex_evidence_decision": "approve", "flamestrike_decision_affirmation": "great approved", "closeout_contract_preparation_approval": "approved", "closeout_execution_approval": "approved", "final_authority": "Flamestrike"}, "delegation selection affirmation preparation and execution approval chain is explicit", chain)
    add(mapping_validation.get("passed_gate_count") == 31 and mapping_validation.get("failed_gate_count") == 0, "frozen mapping validation remains 31/31 pass", {"passed": mapping_validation.get("passed_gate_count"), "failed": mapping_validation.get("failed_gate_count")})
    add(len(frozen) == 16, "frozen ledger still contains exactly sixteen records", len(frozen))
    add(exact_copy, "all source IDs sectors ranks u values and coordinates copy exactly", {"matched": 16 if exact_copy else 0, "total": 16, "fields": exact_fields})
    add(unique_targets == 16, "all sixteen target coordinates remain unique", {"unique": unique_targets, "total": len(mappings)})
    add(endpoint_hits == 0 and duplicate_targets == 0, "endpoint assignments and duplicate coordinates remain zero", {"endpoint_assignments": endpoint_hits, "duplicate_coordinates": duplicate_targets})
    add(source_displacement == 0, "source displacement remains zero pixels", source_displacement)
    add(mapped_non_top == 0, "mapped non-top samples remain zero", mapped_non_top)
    add(physical_pairs == 0, "physical cross-view pairs remain zero", physical_pairs)
    add(all(claims[key] == 0 for key in ("source_centers", "pivots", "physical_C003_dimensions", "snap_anchors")), "center pivot physical-size and snap-anchor claims remain zero", {key: claims[key] for key in ("source_centers", "pivots", "physical_C003_dimensions", "snap_anchors")})
    add(all(claims[key] == 0 for key in ("CL002_closures", "annuli", "hidden_interfaces", "filled_footprints")), "closure annulus hidden-interface and filled-footprint counts remain zero", {key: claims[key] for key in ("CL002_closures", "annuli", "hidden_interfaces", "filled_footprints")})
    add(all(claims[key] == 0 for key in ("fields", "surfaces", "topology", "geometry")), "field surface topology and geometry counts remain zero", {key: claims[key] for key in ("fields", "surfaces", "topology", "geometry")})
    add(all_match(technical_hashes), "technical mapping proof files remain byte-identical", technical_hashes)
    add(all_match(prior_hashes), "original source and prior authority remain unchanged", prior_hashes)
    classifications = Counter(record.get("artifact_classification") for record in mappings)
    add(len(mappings) == 16 and classifications == Counter({"approved bounded interpretation": 16}) and decision["artifact_classification"] == "authoritative for bounded S10R-003-A mapping only", "only the exact mapping is classified approved bounded interpretation", {"registry": decision["artifact_classification"], "mapping_classifications": dict(classifications)})
    routing = decision["block_routing"]
    add(routing["C003-TSIB-A02-K80-BLOCK-001"] == "resolved_at_bounded_mapping_authority_level" and "bounded_S10R003A_mapping_level" in routing["S10R-BLOCK-003"], "mapping execution condition is resolved only at bounded authority level", {key: routing[key] for key in ("C003-TSIB-A02-K80-BLOCK-001", "S10R-BLOCK-003")})
    active = {item["id"]: item for item in blocks["active_blocks"]}
    add("S10R-BLOCK-006" in active and active["S10R-BLOCK-006"].get("field_sample_count") == 0 and "technical_gate_contract" in active["S10R-BLOCK-006"]["status"], "S10R-BLOCK-006 remains active pending separate compatibility and technical gates and creates no field", active.get("S10R-BLOCK-006"))
    add(set(active) == {"S10R-BLOCK-006", "S10R-BLOCK-008", "S10R-BLOCK-009"}, "S10R-BLOCK-008 and S10R-BLOCK-009 remain active", {"active_block_ids": sorted(active)})
    add(all(blocks[key] == "blocked" for key in ("step10_closeout", "step11", "dcc", "unreal", "production")) and not any(decision[key] for key in ("step10_closeout_authorized", "step11_authorized", "dcc_authorized", "unreal_authorized", "production_authorized")), "Step 10 closeout Step 11 DCC Unreal and production remain blocked", {key: blocks[key] for key in ("step10_closeout", "step11", "dcc", "unreal", "production")})
    add(not unexpected_new_paths and not missing_created_paths, "changed paths are contained by the closeout allowlist", {"baseline_checkpoint": "Saved/ProjectRecovery/20260717-155655/", "execution_created_paths": sorted(EXECUTION_CREATED), "allowed_status_updates": sorted(allowed_status_updates), "new_paths_since_baseline": sorted(newly_visible_paths), "unexpected_new_paths": unexpected_new_paths, "missing_created_paths": missing_created_paths, "allowlist": sorted(anticipated)})
    add(not staged_paths and head == "f525945" and branch == "main", "no closeout path is staged committed or pushed", {"branch": branch, "head": head, "staged_paths": staged_paths, "commit_authorized": False, "push_authorized": False})
    add(records_agree, "approval log artifact index reset state output registry blocks and handoff agree", {"required_tokens": agreement_tokens, "all_records_match": records_agree})
    route_phrase = "preparation only" in handoff_text and "S10R-006-A" in handoff_text and "after mandatory restart" in handoff_text.lower()
    add(route_phrase and blocks["next_gate"]["execution_authorized"] is False, "handoff routes only to possible separate S10R-006-A contract preparation after restart", blocks["next_gate"])
    add(not s10r006_files and blocks["next_gate"]["contract_created_during_closeout"] is False, "no S10R-006-A contract or output is created during closeout", {"matching_files": s10r006_files, "created": False})
    add(output_visible and reset_visible, "closeout output and reset resume state are visibly opened", {"wmctrl_returncode": wmctrl.returncode, "gedit_process_query_returncode": gedit_process.returncode, "output_window_visible": output_visible, "reset_window_visible": reset_visible, "matching_visible_desktop_evidence": [line for line in visible_desktop_evidence.splitlines() if "S10R_003_A_CL003_TARGET_SPACE_MAPPING_A01_DECISION_CLOSEOUT_OUTPUT_RECORD.md" in line or "SM_GIA_BloodAxeCairnstone_A005_RESET_RESUME_STATE.md" in line]})
    add(decision["mandatory_restart_required"] is True and blocks["mandatory_restart_required"] is True and "mandatory restart" in output_text and "mandatory restart" in handoff_text, "session stops for mandatory restart", {"decision_registry": decision["mandatory_restart_required"], "remaining_blocks": blocks["mandatory_restart_required"], "next_action_executed": False})

    for number, gate in enumerate(gates, 1):
        gate["gate"] = f"G{number:02d}"
    passed = sum(gate["status"] == "pass" for gate in gates)
    failed = len(gates) - passed
    output_hashes = {
        str(path.relative_to(ROOT)): sha256(path)
        for path in (DECISION, BLOCKS, OUTPUT, HANDOFF, RESET, APPROVAL, INDEX, Path(__file__))
    }
    validation = {
        "schema": "aerathea.s10r_003_a_cl003_target_space_mapping_a01_decision_closeout_validation.v1",
        "asset_id": "SM_GIA_BloodAxeCairnstone_A005",
        "contract_id": CONTRACT_ID,
        "date": "2026-07-17",
        "validated_at": now_local(),
        "status": "pass_bounded_mapping_decision_closeout_mandatory_restart" if failed == 0 else "fail_closeout_quarantine_and_stop",
        "artifact_classification": "proof only",
        "independent_auditor": str(Path(__file__).relative_to(ROOT)),
        "frozen_builder_or_mapping_auditor_imported": False,
        "gate_count": len(gates),
        "passed_gate_count": passed,
        "failed_gate_count": failed,
        "pre_output_locked_hashes": decision["pre_output_locked_input_verification"]["hashes"],
        "technical_mapping_proof_hashes": technical_hashes,
        "prior_authority_hashes": prior_hashes,
        "output_hashes_before_validation_write": output_hashes,
        "exact_mapping_counts": {
            "ledger_records": len(frozen),
            "approved_mapping_records": len(mappings),
            "unique_target_coordinates": unique_targets,
            "endpoint_assignments": endpoint_hits,
            "duplicate_target_coordinates": duplicate_targets,
            "source_displacement_px": source_displacement,
            "mapped_non_top_samples": mapped_non_top,
            "physical_cross_view_pairs": physical_pairs,
        },
        "authority_counts": claims,
        "changed_path_audit": gates[21]["evidence"],
        "visible_review_verification": gates[26]["evidence"],
        "gates": gates,
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
