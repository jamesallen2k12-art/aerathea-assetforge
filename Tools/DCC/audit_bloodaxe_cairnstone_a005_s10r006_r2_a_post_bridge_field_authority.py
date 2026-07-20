#!/usr/bin/env python3
"""Read-only independent audit for A005 S10R-006-R2-A candidate records."""

from __future__ import annotations

import hashlib
import json
import subprocess
import sys
from pathlib import Path


ROOT = Path(__file__).resolve().parents[2]
A005 = ROOT / "docs/assets/blueprints/SM_GIA_BloodAxeCairnstone_A005"
MANIFESTS = A005 / "manifests"
STEPS = A005 / "steps"
HANDOFFS = A005 / "handoffs"

INPUT_LOCK = MANIFESTS / "S10R_006_R2_A_POST_BRIDGE_FIELD_AUTHORITY_INPUT_LOCK.json"
DEPENDENCY_AUDIT = MANIFESTS / "S10R_006_R2_A_POST_BRIDGE_FIELD_AUTHORITY_DEPENDENCY_AUDIT.json"
OPTION_REGISTRY = MANIFESTS / "S10R_006_R2_A_POST_BRIDGE_FIELD_AUTHORITY_OPTION_REGISTRY.json"
VALIDATION = MANIFESTS / "S10R_006_R2_A_POST_BRIDGE_FIELD_AUTHORITY_VALIDATION.json"
BRIDGE_REGISTRY = MANIFESTS / "S10R_006_R1_A_NORMALIZED_PRIMARY_OWNER_BRIDGE_A01_DECISION_REGISTRY.json"
REMAINING_BLOCKS = MANIFESTS / "S10R_006_R1_A_NORMALIZED_PRIMARY_OWNER_BRIDGE_A01_REMAINING_BLOCKS.json"
OUTPUT = STEPS / "S10R_006_R2_A_POST_BRIDGE_FIELD_AUTHORITY_DECISION_OUTPUT_RECORD.md"
HANDOFF = HANDOFFS / "S10R_006_R2_A_POST_BRIDGE_FIELD_AUTHORITY_TO_DECISION_HANDOFF.md"
BASELINE_STATUS = Path("/tmp/a005_s10r006_r2_preexec_git_status.txt")
MUTABLE_STATUS_PATHS = {
    "docs/assets/blueprints/SM_GIA_BloodAxeCairnstone_A005/SM_GIA_BloodAxeCairnstone_A005_RESET_RESUME_STATE.md",
    "docs/assets/blueprints/SM_GIA_BloodAxeCairnstone_A005/SM_GIA_BloodAxeCairnstone_A005_APPROVAL_LOG.md",
    "docs/assets/blueprints/SM_GIA_BloodAxeCairnstone_A005/SM_GIA_BloodAxeCairnstone_A005_ARTIFACT_INDEX.md",
}


def sha256(path: Path) -> str:
    digest = hashlib.sha256()
    with path.open("rb") as handle:
        for chunk in iter(lambda: handle.read(1024 * 1024), b""):
            digest.update(chunk)
    return digest.hexdigest()


def load_json(path: Path) -> dict:
    with path.open("r", encoding="utf-8") as handle:
        return json.load(handle)


checks: list[dict] = []


def check(subject: str, condition: bool, evidence: object) -> None:
    checks.append({"subject": subject, "status": "pass" if condition else "fail", "evidence": evidence})


required = [INPUT_LOCK, DEPENDENCY_AUDIT, OPTION_REGISTRY, BRIDGE_REGISTRY, REMAINING_BLOCKS, OUTPUT, HANDOFF]
for path in required:
    check(f"required file exists: {path.relative_to(ROOT)}", path.is_file(), str(path.relative_to(ROOT)))

if any(item["status"] == "fail" for item in checks):
    print(json.dumps({"status": "fail", "checks": checks}, indent=2))
    sys.exit(1)

input_lock = load_json(INPUT_LOCK)
dependency = load_json(DEPENDENCY_AUDIT)
options = load_json(OPTION_REGISTRY)
bridge = load_json(BRIDGE_REGISTRY)
blocks = load_json(REMAINING_BLOCKS)

hash_results = []
for item in input_lock["locked_inputs"]:
    path = ROOT / item["path"]
    actual = sha256(path)
    prewrite_matched = item["expected_sha256"] == item["actual_sha256"] and item["match"] is True
    mutable_status_record = item["path"] in MUTABLE_STATUS_PATHS
    matched = prewrite_matched and (mutable_status_record or actual == item["expected_sha256"])
    hash_results.append({
        "path": item["path"],
        "prewrite_sha256": item["actual_sha256"],
        "current_sha256": actual,
        "controlled_status_update_after_prewrite": mutable_status_record and actual != item["expected_sha256"],
        "match": matched,
    })
check("all twelve locked inputs match", len(hash_results) == 12 and all(item["match"] for item in hash_results), hash_results)

approved = bridge["approved_mappings"]
holdouts = bridge["validation_holdouts"]
front = [item for item in approved if item["frozen_record"]["owner_view"] == "front"]
left = [item for item in approved if item["frozen_record"]["owner_view"] == "left"]
back_holdouts = [item for item in holdouts if item["view"] == "back"]
right_holdouts = [item for item in holdouts if item["view"] == "right"]

check("approved symbolic mapping count and owner split", len(approved) == 12 and len(front) == 6 and len(left) == 6, {"total": len(approved), "front": len(front), "left": len(left)})
check("proof-only holdout count and owner split", len(holdouts) == 14 and len(back_holdouts) == 6 and len(right_holdouts) == 8 and all(item["classification"] == "proof only validation holdout" for item in holdouts), {"total": len(holdouts), "back": len(back_holdouts), "right": len(right_holdouts)})

zero_keys = [
    "physical_source_target_transforms",
    "physical_cross_view_pairs",
    "target_trace_coordinates",
    "source_centers",
    "pivots",
    "anchors",
    "field_samples",
    "fills",
    "surfaces",
    "topology",
    "geometry",
]
authority_counts = bridge["authority_counts"]
check("bridge physical field and geometry authority remains zero", all(authority_counts[key] == 0 for key in zero_keys), {key: authority_counts[key] for key in zero_keys})

active_ids = [item["id"] for item in blocks["active_blocks"]]
check("all three active blocks preserved", active_ids == ["S10R-BLOCK-006", "S10R-BLOCK-008", "S10R-BLOCK-009"] and blocks["counts"]["resolved_block_ids"] == 0, {"active_ids": active_ids, "resolved": blocks["counts"]["resolved_block_ids"]})

option_ids = [item["id"] for item in options["options"]]
check("two required options appear exactly once", option_ids == ["S10R-006-R2-A", "S10R-006-R2-BLOCK"] and len(set(option_ids)) == 2, option_ids)
check("candidate recommendation is unselected", options["candidate_recommendation"] == "S10R-006-R2-A" and options["recommendation_classification"] == "candidate recommendation only" and options["selected_option"] is None and all(item["selected"] is False for item in options["options"]), {"recommendation": options["candidate_recommendation"], "selected_option": options["selected_option"]})

downstream_false = [
    "field_implementation_authorized",
    "step10_closeout_authorized",
    "step11_authorized",
    "dcc_authorized",
    "unreal_authorized",
    "production_authorized",
    "staging_authorized",
    "commit_authorized",
    "push_authorized",
]
check("all downstream authorization flags remain false", all(options[key] is False for key in downstream_false), {key: options[key] for key in downstream_false})
check("dependency audit resolves no block", dependency["resolved_block_ids"] == [] and len(dependency["active_blocks"]) == 3, {"resolved": dependency["resolved_block_ids"], "active": dependency["active_blocks"]})

output_text = OUTPUT.read_text(encoding="utf-8")
handoff_text = HANDOFF.read_text(encoding="utf-8")
required_output_markers = ["candidate_post_bridge_field_authority_decision_surface_ready_for_Flamestrike", "S10R-006-R2-A", "S10R-006-R2-BLOCK", "field samples, fills, surfaces, topology, and geometry: `0`", "No option selection"]
check("output record preserves candidate stop markers", all(marker in output_text for marker in required_output_markers), required_output_markers)
required_handoff_markers = ["S10R-006-R2-A", "S10R-006-R2-BLOCK", "resolved block IDs: none", "Required Decision Stop"]
check("decision handoff preserves both options and stop", all(marker in handoff_text for marker in required_handoff_markers), required_handoff_markers)

git_status = subprocess.run(["git", "status", "--porcelain=v1"], cwd=ROOT, check=True, text=True, capture_output=True).stdout.splitlines()
baseline = BASELINE_STATUS.read_text(encoding="utf-8").splitlines()
new_status_lines = sorted(set(git_status) - set(baseline))
allowed_new_paths = {
    "docs/assets/blueprints/SM_GIA_BloodAxeCairnstone_A005/manifests/S10R_006_R2_A_POST_BRIDGE_FIELD_AUTHORITY_INPUT_LOCK.json",
    "docs/assets/blueprints/SM_GIA_BloodAxeCairnstone_A005/manifests/S10R_006_R2_A_POST_BRIDGE_FIELD_AUTHORITY_DEPENDENCY_AUDIT.json",
    "docs/assets/blueprints/SM_GIA_BloodAxeCairnstone_A005/manifests/S10R_006_R2_A_POST_BRIDGE_FIELD_AUTHORITY_OPTION_REGISTRY.json",
    "docs/assets/blueprints/SM_GIA_BloodAxeCairnstone_A005/steps/S10R_006_R2_A_POST_BRIDGE_FIELD_AUTHORITY_DECISION_OUTPUT_RECORD.md",
    "docs/assets/blueprints/SM_GIA_BloodAxeCairnstone_A005/handoffs/S10R_006_R2_A_POST_BRIDGE_FIELD_AUTHORITY_TO_DECISION_HANDOFF.md",
    "Tools/DCC/audit_bloodaxe_cairnstone_a005_s10r006_r2_a_post_bridge_field_authority.py",
}
if VALIDATION.exists():
    allowed_new_paths.add(str(VALIDATION.relative_to(ROOT)))
parsed_new_paths = {line[3:] for line in new_status_lines if line.startswith("?? ")}
unexpected_lines = [line for line in new_status_lines if not line.startswith("?? ") or line[3:] not in allowed_new_paths]
check("new git-status paths match execution allowlist", parsed_new_paths == allowed_new_paths and not unexpected_lines, {"new_paths": sorted(parsed_new_paths), "allowed": sorted(allowed_new_paths), "unexpected": unexpected_lines})

staged = subprocess.run(["git", "diff", "--cached", "--name-only"], cwd=ROOT, check=True, text=True, capture_output=True).stdout.splitlines()
check("no path staged", staged == [], staged)

if VALIDATION.exists():
    validation = load_json(VALIDATION)
    validation_counts = validation.get("independent_validation", {})
    check("validation record declares only proof authority and passing gates", validation.get("artifact_classification") == "proof only" and validation_counts.get("failed_gate_count") == 0 and validation.get("status") == "pass_candidate_decision_package_ready_for_visible_review", {"status": validation.get("status"), "classification": validation.get("artifact_classification"), "failed": validation_counts.get("failed_gate_count")})

status_markers = {
    A005 / "SM_GIA_BloodAxeCairnstone_A005_RESET_RESUME_STATE.md": [
        "S10R-006-R2-A post-bridge field-authority candidate decision surface validated 20/20",
        "both options unselected",
        "S10R-BLOCK-006",
        "S10R-BLOCK-008",
        "S10R-BLOCK-009",
    ],
    A005 / "SM_GIA_BloodAxeCairnstone_A005_APPROVAL_LOG.md": [
        "## S10R-006-R2-A Post-Bridge Field-Authority Candidate Execution",
        "Selected option: none",
        "Corrected independent validation: `20/20` passed; `0` failed",
    ],
    A005 / "SM_GIA_BloodAxeCairnstone_A005_ARTIFACT_INDEX.md": [
        "## S10R-006-R2-A Post-Bridge Field-Authority Candidate - Validated 20/20",
        "Both options remain unselected",
        "field samples, fills, surfaces, topology, and",
    ],
}
status_evidence = {}
for path, markers in status_markers.items():
    text = path.read_text(encoding="utf-8")
    status_evidence[str(path.relative_to(ROOT))] = {marker: marker in text for marker in markers}
check("allowed A005 status records contain exact candidate and stop markers", all(all(values.values()) for values in status_evidence.values()), status_evidence)

failed = [item for item in checks if item["status"] == "fail"]
result = {
    "schema": "aerathea.s10r_006_r2_a_post_bridge_field_authority_independent_audit.v1",
    "status": "pass" if not failed else "fail",
    "artifact_classification": "proof only",
    "gate_count": len(checks),
    "passed_gate_count": len(checks) - len(failed),
    "failed_gate_count": len(failed),
    "checks": checks,
}
print(json.dumps(result, indent=2))
sys.exit(0 if not failed else 1)
