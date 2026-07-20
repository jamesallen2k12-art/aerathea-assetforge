#!/usr/bin/env python3
"""Read-only independent audit for A005 S10R-006-R6-A authority records."""

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

CONTRACT = STEPS / "S10R_006_R6_A_CROSS_VIEW_CORNER_OWNERSHIP_AUTHORITY_DECISION_CONTRACT.md"
INPUT_LOCK = MANIFESTS / "S10R_006_R6_A_CROSS_VIEW_CORNER_OWNERSHIP_AUTHORITY_INPUT_LOCK.json"
DEPENDENCY = MANIFESTS / "S10R_006_R6_A_CROSS_VIEW_CORNER_OWNERSHIP_AUTHORITY_DEPENDENCY_AUDIT.json"
OPTIONS = MANIFESTS / "S10R_006_R6_A_CROSS_VIEW_CORNER_OWNERSHIP_AUTHORITY_OPTION_REGISTRY.json"
VALIDATION = MANIFESTS / "S10R_006_R6_A_CROSS_VIEW_CORNER_OWNERSHIP_AUTHORITY_VALIDATION.json"
R5 = MANIFESTS / "S10R_006_R5_A_LANE_BOUNDARY_COUPLING_RULE_A01_RULE_REGISTRY.json"
STEP05 = MANIFESTS / "STEP_05_PIXEL_COORDINATE_FRAME_RECORD.json"
AUTHORITY_DELTA = MANIFESTS / "STEP_10R_N3_INTEGRATION_AUTHORITY_DELTA.json"
I10 = MANIFESTS / "STEP_10_INTERPRETATION_OPTION_REGISTRY.json"
OUTPUT = STEPS / "S10R_006_R6_A_CROSS_VIEW_CORNER_OWNERSHIP_AUTHORITY_DECISION_OUTPUT_RECORD.md"
HANDOFF = HANDOFFS / "S10R_006_R6_A_CROSS_VIEW_CORNER_OWNERSHIP_AUTHORITY_TO_DECISION_HANDOFF.md"

STATUS_PATHS = {
    A005 / "SM_GIA_BloodAxeCairnstone_A005_RESET_RESUME_STATE.md",
    A005 / "SM_GIA_BloodAxeCairnstone_A005_APPROVAL_LOG.md",
    A005 / "SM_GIA_BloodAxeCairnstone_A005_ARTIFACT_INDEX.md",
}

EXPECTED_SCOPED_PATHS = {
    str(path.relative_to(ROOT))
    for path in {
        CONTRACT,
        INPUT_LOCK,
        DEPENDENCY,
        OPTIONS,
        VALIDATION,
        OUTPUT,
        HANDOFF,
        Path(__file__).resolve(),
        *STATUS_PATHS,
    }
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


def check(gate: int, subject: str, condition: bool, evidence: object) -> None:
    checks.append(
        {
            "gate": gate,
            "subject": subject,
            "status": "pass" if condition else "fail",
            "evidence": evidence,
        }
    )


required = [
    CONTRACT,
    INPUT_LOCK,
    DEPENDENCY,
    OPTIONS,
    VALIDATION,
    R5,
    STEP05,
    AUTHORITY_DELTA,
    I10,
    OUTPUT,
    HANDOFF,
    *sorted(STATUS_PATHS),
]
missing = [str(path.relative_to(ROOT)) for path in required if not path.is_file()]
if missing:
    print(json.dumps({"status": "fail_closed_missing_required_files", "missing_files": missing}, indent=2))
    sys.exit(1)

input_lock = load_json(INPUT_LOCK)
dependency = load_json(DEPENDENCY)
options = load_json(OPTIONS)
validation = load_json(VALIDATION)
r5 = load_json(R5)
step05 = load_json(STEP05)
authority_delta = load_json(AUTHORITY_DELTA)
i10 = load_json(I10)
output_text = OUTPUT.read_text(encoding="utf-8")
handoff_text = HANDOFF.read_text(encoding="utf-8")

# Gate 1
hash_results = []
for item in input_lock["locked_inputs"]:
    current = sha256(ROOT / item["path"])
    prewrite_match = item["expected_sha256"] == item["actual_sha256"] and item["match"] is True
    controlled = item["policy"] == "controlled candidate-status update after prewrite verification"
    hash_results.append(
        {
            "path": item["path"],
            "prewrite_match": prewrite_match,
            "current_sha256": current,
            "controlled_status_update_after_prewrite": controlled and current != item["expected_sha256"],
            "valid": prewrite_match and (controlled or current == item["expected_sha256"]),
        }
    )
check(1, "all thirteen locked inputs match", len(hash_results) == 13 and all(x["valid"] for x in hash_results), hash_results)

# Gate 2
contract_hash = sha256(CONTRACT)
check(
    2,
    "contract hash and exact execution approval match",
    contract_hash == "31026cb66c7d6bb7ece475e5a25400812e917a3268b5b5f3fd65a4159b0318f9"
    and input_lock["execution_approval"]["approver"] == "Flamestrike"
    and input_lock["execution_approval"]["statement"] == "approved",
    {"contract_sha256": contract_hash, "approval": input_lock["execution_approval"]},
)

# Gate 3
check(
    3,
    "R5 remains approved bounded symbolic interpretation for four arcs only",
    r5["status"] == "approved_bounded_symbolic_rule_four_blocked_corner_gaps_unowned"
    and r5["artifact_classification"] == "authoritative for bounded S10R-006-R5-A symbolic coupling rule only"
    and r5["flamestrike_decision"]["scope"] == "authoritative bounded symbolic interpretation for four owned cardinal arcs only",
    {"status": r5["status"], "classification": r5["artifact_classification"]},
)

# Gate 4
expected_intervals = ["[-1/2,1/2]", "[3/2,5/2]", "[7/2,9/2]", "[11/2,13/2]"]
check(
    4,
    "four R5 lane intervals remain exact",
    len(r5["lanes"]) == 4
    and [x["q_interval"] for x in r5["lanes"]] == expected_intervals
    and r5["sector_policy"]["pairwise_disjoint_owned_intervals"] is True,
    [x["q_interval"] for x in r5["lanes"]],
)

# Gate 5
expected_gaps = [("G_0", "(1/2,3/2)"), ("G_1", "(5/2,7/2)"), ("G_2", "(9/2,11/2)"), ("G_3", "(13/2,15/2)")]
actual_gaps = [(x["id"], x["q_interval"]) for x in r5["blocked_gaps"]]
check(
    5,
    "four exact open gaps remain unowned",
    actual_gaps == expected_gaps
    and options["preserved_gap_set"] == [
        {"id": "G_0", "q_interval": "(1/2,3/2)", "status": "unowned_blocked"},
        {"id": "G_1", "q_interval": "(5/2,7/2)", "status": "unowned_blocked"},
        {"id": "G_2", "q_interval": "(9/2,11/2)", "status": "unowned_blocked"},
        {"id": "G_3", "q_interval": "(13/2,15/2)", "status": "unowned_blocked_unwrapped"},
    ],
    {"r5": r5["blocked_gaps"], "r6": options["preserved_gap_set"]},
)

# Gate 6
q = r5["abstract_parameter"]
check(
    6,
    "q remains non-periodic unwrapped and unclosed",
    q["periodic"] is False
    and q["modulus"] is None
    and q["wrap"] is None
    and q["final_first_endpoint_identification"] is False
    and r5["sector_policy"]["closed_360_ownership"] is False,
    q,
)

# Gate 7
check(
    7,
    "q_L B_v and C_L remain unevaluated",
    all(x["per_record_q_values"] == [] for x in r5["lanes"])
    and r5["boundary_family"]["evaluated_samples"] == []
    and r5["coupling_descriptor"]["evaluated"] is False
    and r5["output_counts"]["evaluated_parameter_samples"] == 0
    and r5["output_counts"]["evaluated_boundary_samples"] == 0
    and r5["output_counts"]["evaluated_coupling_samples"] == 0,
    {"lanes": r5["lanes"], "boundary": r5["boundary_family"], "coupling": r5["coupling_descriptor"]},
)

# Gate 8
check(
    8,
    "all fourteen back right records remain proof only",
    r5["holdouts"] == {"classification": "proof only", "back_count": 6, "right_count": 8, "total": 14, "construction_use_authorized": False},
    r5["holdouts"],
)

# Gate 9
axis = step05["world_coordinate_frame"]["panel_axis_mappings"]
check(
    9,
    "Step 05 cardinal axes replay exactly",
    step05["world_coordinate_frame"]["handedness"] == "right_handed"
    and step05["world_coordinate_frame"]["world_up_axis"] == "+Z"
    and axis["front"]["image_x_right"] == "+X"
    and axis["left"]["image_x_right"] == "-Y"
    and dependency["step05_axis_authority"]["front_left"] == "-X"
    and dependency["step05_axis_authority"]["left_left"] == "+Y",
    {"step05": axis, "dependency": dependency["step05_axis_authority"]},
)

# Gate 10
i10_item = next(x for x in i10["decision_items"] if x["id"] == "I10-010")
delta_item = next(x for x in authority_delta["item_delta"] if x["old_item_id"] == "I10-010")
check(
    10,
    "historical I10-010 remains candidate and requires revision",
    i10["artifact_classification"] == "candidate"
    and i10_item["flamestrike_decision"] == "pending"
    and i10_item["approved_rule"] is None
    and delta_item["candidate_delta_classification"] == "requires_revision"
    and dependency["historical_i10_010"]["current_rule_authority"] is False,
    {"i10": i10_item, "delta": delta_item},
)

# Gate 11
option_ids = [x["id"] for x in options["options"]]
check(
    11,
    "both required R6 options appear exactly once",
    option_ids == ["S10R-006-R6-A", "S10R-006-R6-BLOCK"] and len(set(option_ids)) == 2,
    option_ids,
)

# Gate 12
check(
    12,
    "R6-A is the sole selected bounded preparation route",
    options["selected_option"] == "S10R-006-R6-A"
    and [x["id"] for x in options["options"] if x["selected"]] == ["S10R-006-R6-A"]
    and options["candidate_recommendation"] == {
        "option_id": "S10R-006-R6-A",
        "classification": "accepted evidence recommendation",
        "selected": True,
        "reason": "It is the smallest bounded gate that permits a later visible and rejectable revised rule proposal without assigning any corner.",
    }
    and options["selection_record"]["approver"] == "Flamestrike"
    and options["selection_record"]["approval_statement"] == "approved"
    and options["selection_record"]["authority_granted"]
    == "preparation only of one separate bounded cross-view corner-ownership rule contract",
    {"selected_option": options["selected_option"], "recommendation": options["candidate_recommendation"], "selection_record": options["selection_record"]},
)

# Gate 13
counts = options["output_counts"]
ownership_keys = ["gap_assignments", "gap_subintervals", "parameter_instances", "evaluated_samples", "corner_owners", "seams", "joins", "closures"]
check(13, "one option is selected while no gap allocation owner seam join or closure is defined", counts["selected_options"] == 1 and all(counts[k] == 0 for k in ownership_keys), {"selected_options": counts["selected_options"], **{k: counts[k] for k in ownership_keys}})

# Gate 14
physical_keys = ["source_to_target_transforms", "physical_pairs", "target_coordinates", "centers", "pivots", "anchors"]
check(14, "no transform pair coordinate center pivot or anchor exists", all(counts[k] == 0 for k in physical_keys), {k: counts[k] for k in physical_keys})

# Gate 15
field_keys = ["fields", "fills", "surfaces", "topology", "geometry"]
check(15, "field fill surface topology and geometry counts remain zero", all(counts[k] == 0 for k in field_keys), {k: counts[k] for k in field_keys})

# Gate 16
expected_blocks = [
    {"id": "S10R-BLOCK-006", "status": "active_pending_separate_cross_view_corner_ownership_rule_contract"},
    {"id": "S10R-BLOCK-008", "status": "active_unchanged"},
    {"id": "S10R-BLOCK-009", "status": "active_unchanged"},
]
check(16, "all three blocks remain active and none is resolved", options["active_blocks"] == expected_blocks and options["resolved_block_ids"] == [], {"active": options["active_blocks"], "resolved": options["resolved_block_ids"]})

# Gate 17
flags = options["authorization_flags"]
check(
    17,
    "candidate registration selection and preparation-only routing are true while rule evaluation implementation downstream and Git flags are false",
    flags["candidate_decision_surface_registered"] is True
    and flags["option_selected"] is True
    and flags["corner_rule_preparation_authorized"] is True
    and all(
        value is False
        for key, value in flags.items()
        if key not in {"candidate_decision_surface_registered", "option_selected", "corner_rule_preparation_authorized"}
    ),
    flags,
)

# Gate 18
git_lines = subprocess.run(["git", "status", "--porcelain=v1", "-uall"], cwd=ROOT, check=True, text=True, capture_output=True).stdout.splitlines()
status_names = {path.name for path in STATUS_PATHS}
scoped_paths = {
    line[3:]
    for line in git_lines
    if len(line) >= 4
    and (
        "S10R_006_R6_A_CROSS_VIEW_CORNER_OWNERSHIP_AUTHORITY" in line[3:]
        or line[3:].endswith("audit_bloodaxe_cairnstone_a005_s10r006_r6_a_cross_view_corner_ownership_authority.py")
        or Path(line[3:]).name in status_names
    )
}
status_markers = {
    A005 / "SM_GIA_BloodAxeCairnstone_A005_RESET_RESUME_STATE.md": ["S10R-006-R6-A Selected Preparation Route", "active_pending_separate_cross_view_corner_ownership_rule_contract"],
    A005 / "SM_GIA_BloodAxeCairnstone_A005_APPROVAL_LOG.md": ["S10R-006-R6-A Option Selection", "Approval statement: `approved`"],
    A005 / "SM_GIA_BloodAxeCairnstone_A005_ARTIFACT_INDEX.md": ["S10R-006-R6-A Cross-View Corner-Ownership Authority - Selected Route", "four unowned corner gaps"],
}
marker_evidence = {str(path.relative_to(ROOT)): {marker: marker in path.read_text(encoding="utf-8") for marker in markers} for path, markers in status_markers.items()}
check(18, "changed paths match execution allowlist", scoped_paths == EXPECTED_SCOPED_PATHS and all(all(x.values()) for x in marker_evidence.values()), {"scoped_paths": sorted(scoped_paths), "expected_paths": sorted(EXPECTED_SCOPED_PATHS), "status_markers": marker_evidence})

# Gate 19
staged = subprocess.run(["git", "diff", "--cached", "--name-only"], cwd=ROOT, check=True, text=True, capture_output=True).stdout.splitlines()
check(19, "no path is staged", staged == [], staged)

# Gate 20
visible = validation["post_decision_visible_review"]
check(
    20,
    "updated output and handoff visibility verified before post-decision stop",
    visible["verified"] is True
    and visible["output_record"].startswith("verified in dedicated")
    and visible["decision_handoff"].startswith("verified in dedicated")
    and visible["global_desktop_titles_surfaced"] is False,
    visible,
)

if [x["gate"] for x in checks] != list(range(1, 21)):
    raise RuntimeError("auditor gates are not exactly 1..20")

failed = [x for x in checks if x["status"] == "fail"]
result = {
    "schema": "aerathea.s10r_006_r6_a_cross_view_corner_ownership_authority_independent_audit.v1",
    "status": "pass" if not failed else "fail",
    "artifact_classification": "proof only",
    "gate_count": len(checks),
    "passed_gate_count": len(checks) - len(failed),
    "failed_gate_count": len(failed),
    "checks": checks,
}
print(json.dumps(result, indent=2))
sys.exit(0 if not failed else 1)
