#!/usr/bin/env python3
"""Audit the record-only A005 S10R-006-A blocked-result closeout."""

from __future__ import annotations

import hashlib
import json
import subprocess
import sys
from pathlib import Path


ROOT = Path(__file__).resolve().parents[2]
ASSET_REL = Path("docs/assets/blueprints/SM_GIA_BloodAxeCairnstone_A005")
ASSET = ROOT / ASSET_REL
MANIFESTS = ASSET / "manifests"
STEPS = ASSET / "steps"
HANDOFFS = ASSET / "handoffs"
CONTRACT_ID = "A005-CR-S10R-006-A-BCTG-DC-A01"
HEAD = "f525945"

DECISION = MANIFESTS / "S10R_006_A_BOUNDARY_COMPATIBILITY_TECHNICAL_GATE_A01_DECISION_REGISTRY.json"
BLOCKS = MANIFESTS / "S10R_006_A_BOUNDARY_COMPATIBILITY_TECHNICAL_GATE_A01_REMAINING_BLOCKS.json"
VALIDATION = MANIFESTS / "S10R_006_A_BOUNDARY_COMPATIBILITY_TECHNICAL_GATE_A01_DECISION_CLOSEOUT_VALIDATION.json"
OUTPUT = STEPS / "S10R_006_A_BOUNDARY_COMPATIBILITY_TECHNICAL_GATE_A01_DECISION_CLOSEOUT_OUTPUT_RECORD.md"
HANDOFF = HANDOFFS / "S10R_006_A_BOUNDARY_COMPATIBILITY_TECHNICAL_GATE_A01_TO_BLOCKED_ROUTING_HANDOFF.md"
RESET = ASSET / "SM_GIA_BloodAxeCairnstone_A005_RESET_RESUME_STATE.md"
APPROVAL = ASSET / "SM_GIA_BloodAxeCairnstone_A005_APPROVAL_LOG.md"
INDEX = ASSET / "SM_GIA_BloodAxeCairnstone_A005_ARTIFACT_INDEX.md"
BASELINE_STATUS = ROOT / "Saved/ProjectRecovery/20260717-171757/git_status_short.txt"

LOCKED_HASHES = {
    "AGENTS.md": "5d2d2637a58113f0a6f5ec92e40d8bb2bda9e03fb58b4868a0d9dfbb3b57ad55",
    "docs/projects/assetforge/BLOODAXE_CAIRNSTONE_PIXEL_EXACT_FRESH_START_MULTISTEP_PLAN.md": "ba6784498d792dc85dd431c807f59620d6851af97b4cd15efe89c44a397b10b6",
    str(ASSET_REL / "steps/S10R_006_A_BOUNDARY_COMPATIBILITY_TECHNICAL_GATE_A01_CONTRACT.md"): "0f4e7fae93d9fe36beb4e0d5ad13cafaf1a2ea0864845c79ac574db75792bd8e",
    str(ASSET_REL / "manifests/S10R_006_A_BOUNDARY_COMPATIBILITY_TECHNICAL_GATE_A01_INPUT_LOCK.json"): "83198249ec146d19c378917598d85a1e646105c29a827b0f8e7e862f48a8c7aa",
    str(ASSET_REL / "manifests/S10R_006_A_BOUNDARY_COMPATIBILITY_TECHNICAL_GATE_A01_DEPENDENCY_AUDIT.json"): "2c25a23614f98de2145118194fdb44ffd5d50956184ecca55a1e9603a1788100",
    str(ASSET_REL / "manifests/S10R_006_A_BOUNDARY_COMPATIBILITY_TECHNICAL_GATE_A01_BOUNDARY_AUTHORITY_AUDIT.json"): "34be26075ca9af9bd8b7dedce974d5b748a2dd07124b7dc5f8613c9b23ec0832",
    str(ASSET_REL / "manifests/S10R_006_A_BOUNDARY_COMPATIBILITY_TECHNICAL_GATE_A01_VALIDATION.json"): "fa69ba67c76d17de5ab9edc570e021bf315d4e0501440d3ba6bece72deeb03b5",
    str(ASSET_REL / "evidence/S10R_006_A_BOUNDARY_COMPATIBILITY_TECHNICAL_GATE_A01/SM_GIA_BloodAxeCairnstone_A005_S10R_006_A_BOUNDARY_COMPATIBILITY_TECHNICAL_GATE_A01_REVIEW_BOARD.png"): "a02d8756ce5e010c41756b67ded2b6113ade283a7299397a200b99216754a051",
    str(ASSET_REL / "steps/S10R_006_A_BOUNDARY_COMPATIBILITY_TECHNICAL_GATE_A01_OUTPUT_RECORD.md"): "50ddc7da23a13b2bc34a7113d9ca1cc618e17f6764f44a039fc212631c81581b",
    str(ASSET_REL / "handoffs/S10R_006_A_BOUNDARY_COMPATIBILITY_TECHNICAL_GATE_A01_TO_DECISION_HANDOFF.md"): "8b2956415f2118b92ae340fac4337a37253831102762f45ad4a0d85489d61362",
    str(ASSET_REL / "steps/S10R_006_A_BOUNDARY_COMPATIBILITY_TECHNICAL_GATE_A01_DECISION_CLOSEOUT_CONTRACT.md"): "86560bbb76906ec5926fc90fdbf5e00c005fb84a2cfeac1ca3361e4caaec904b",
    "Saved/ProjectRecovery/20260717-162812/git_status_short.txt": "ce78802d2c6092c092e64f036bf89fef41bfe3a9ec999f17cde7ce2a78d30d22",
}

EXPECTED_NEW_PATHS = {
    str(DECISION.relative_to(ROOT)),
    str(BLOCKS.relative_to(ROOT)),
    str(VALIDATION.relative_to(ROOT)),
    str(OUTPUT.relative_to(ROOT)),
    str(HANDOFF.relative_to(ROOT)),
    "Tools/DCC/audit_bloodaxe_cairnstone_a005_s10r006a_decision_closeout_a01.py",
}


def sha256(path: Path) -> str:
    digest = hashlib.sha256()
    with path.open("rb") as handle:
        for chunk in iter(lambda: handle.read(1024 * 1024), b""):
            digest.update(chunk)
    return digest.hexdigest()


def load_json(path: Path) -> dict:
    return json.loads(path.read_text(encoding="utf-8"))


def require(condition: bool, message: str) -> None:
    if not condition:
        raise RuntimeError(message)


def status_paths(text: str) -> set[str]:
    paths = set()
    for line in text.splitlines():
        if not line or line.startswith("#") or len(line) < 4:
            continue
        paths.add(line[3:].split(" -> ")[-1])
    return paths


def main() -> int:
    for rel, expected in LOCKED_HASHES.items():
        path = ROOT / rel
        require(path.is_file(), f"missing locked input: {rel}")
        require(sha256(path) == expected, f"locked input hash mismatch: {rel}")

    branch = subprocess.run(
        ["git", "branch", "--show-current"], cwd=ROOT, check=True,
        capture_output=True, text=True
    ).stdout.strip()
    head = subprocess.run(
        ["git", "rev-parse", "--short", "HEAD"], cwd=ROOT, check=True,
        capture_output=True, text=True
    ).stdout.strip()
    staged = subprocess.run(
        ["git", "diff", "--cached", "--name-only"], cwd=ROOT, check=True,
        capture_output=True, text=True
    ).stdout.strip()
    require(branch == "main", f"unexpected branch: {branch}")
    require(head == HEAD, f"unexpected HEAD: {head}")
    require(not staged, "staged paths are forbidden")

    decision = load_json(DECISION)
    blocks = load_json(BLOCKS)
    validation = load_json(VALIDATION)
    require(decision["contract_id"] == CONTRACT_ID, "decision contract ID mismatch")
    require(decision["decision"] == "approve", "decision is not approve")
    require(decision["approved_result"] == "blocked_source_authority_missing", "wrong approved result")
    require(decision["frozen_proof"]["technical_validation_gates_passed"] == 29, "technical pass count changed")
    require(decision["frozen_proof"]["technical_validation_gates_failed"] == 0, "technical failure count changed")
    require(decision["trace_counts"]["required_registered_trace_boundaries"] == 26, "trace count changed")
    require(decision["trace_counts"]["common_frame_authority_available"] == 0, "unexpected common-frame authority")
    require(decision["trace_counts"]["common_frame_authority_missing"] == 26, "missing-authority count changed")
    require(decision["trace_counts"]["exact_comparisons_performed"] == 0, "unexpected comparison")
    require(decision["trace_counts"]["explicit_boundary_mismatches"] == 0, "unexpected mismatch")
    require(all(value == 0 for value in decision["authority_counts"].values()), "nonzero implementation authority")
    require(set(decision["active_blocks_preserved"]) == {"S10R-BLOCK-006", "S10R-BLOCK-008", "S10R-BLOCK-009"}, "active blocks changed")

    block_ids = {item["id"] for item in blocks["active_blocks"]}
    require(block_ids == {"S10R-BLOCK-006", "S10R-BLOCK-008", "S10R-BLOCK-009"}, "remaining-block IDs changed")
    require(blocks["step10_closeout"] == "blocked", "Step 10 closeout not blocked")
    require(blocks["step11"] == "blocked", "Step 11 not blocked")
    require(blocks["next_gate"]["recovery_contract_prepared"] is False, "recovery contract was prepared")

    output_text = OUTPUT.read_text(encoding="utf-8")
    handoff_text = HANDOFF.read_text(encoding="utf-8")
    reset_text = RESET.read_text(encoding="utf-8")
    approval_text = APPROVAL.read_text(encoding="utf-8")
    index_text = INDEX.read_text(encoding="utf-8")
    for text, label in ((output_text, "output"), (handoff_text, "handoff"), (reset_text, "reset"), (approval_text, "approval"), (index_text, "index")):
        require("blocked_source_authority_missing" in text, f"{label} missing result")
        require("S10R-BLOCK-006" in text and "S10R-BLOCK-008" in text and "S10R-BLOCK-009" in text, f"{label} missing active blocks")
    require("mandatory restart" in output_text.lower(), "output missing mandatory restart")
    require("mandatory restart" in handoff_text.lower(), "handoff missing mandatory restart")
    require("Candidate Pending Decision" not in reset_text.split("## Superseded Resume Boundary", 1)[0], "reset current boundary still pending")
    require("pending Flamestrike" not in approval_text.split("## S10R-006-A Boundary-Compatibility", 1)[0], "approval status still pending")
    require("Candidate Result Pending Decision" not in index_text.split("## S10R-003-A", 1)[0], "artifact index current heading still pending")

    require(validation["contract_id"] == CONTRACT_ID, "validation contract ID mismatch")
    require(validation["status"] == "pass_blocked_result_closeout", "validation status mismatch")
    require(validation["gate_count"] == 24, "validation gate count mismatch")
    require(validation["passed_gate_count"] == 24 and validation["failed_gate_count"] == 0, "validation is not 24/24 pass")
    for rel, expected in validation["output_hashes_before_validation_write"].items():
        require(sha256(ROOT / rel) == expected, f"closeout output hash mismatch: {rel}")

    baseline = status_paths(BASELINE_STATUS.read_text(encoding="utf-8"))
    current_text = subprocess.run(
        ["git", "status", "--short"], cwd=ROOT, check=True,
        capture_output=True, text=True
    ).stdout
    current = status_paths(current_text)
    new_paths = current - baseline
    require(new_paths == EXPECTED_NEW_PATHS, f"changed-path scope mismatch: {sorted(new_paths ^ EXPECTED_NEW_PATHS)}")

    print("PASS: A005 S10R-006-A decision closeout 24/24 gates")
    print("result: blocked_source_authority_missing")
    print("active blocks: S10R-BLOCK-006, S10R-BLOCK-008, S10R-BLOCK-009")
    print("field/surface/topology/geometry authority: 0")
    return 0


if __name__ == "__main__":
    try:
        sys.exit(main())
    except Exception as exc:
        print(f"FAIL: {exc}", file=sys.stderr)
        sys.exit(1)
