#!/usr/bin/env python3
"""Read-only independent audit for A005 S10R-006-R7-A rule records."""

from __future__ import annotations

import hashlib
import json
import subprocess
import sys
from fractions import Fraction
from pathlib import Path


ROOT = Path(__file__).resolve().parents[2]
A005 = ROOT / "docs/assets/blueprints/SM_GIA_BloodAxeCairnstone_A005"
MANIFESTS = A005 / "manifests"
STEPS = A005 / "steps"
HANDOFFS = A005 / "handoffs"

CONTRACT = STEPS / "S10R_006_R7_A_CROSS_VIEW_CORNER_OWNERSHIP_RULE_A01_CONTRACT.md"
INPUT_LOCK = MANIFESTS / "S10R_006_R7_A_CROSS_VIEW_CORNER_OWNERSHIP_RULE_A01_INPUT_LOCK.json"
RULE = MANIFESTS / "S10R_006_R7_A_CROSS_VIEW_CORNER_OWNERSHIP_RULE_A01_RULE_REGISTRY.json"
FALSIFICATION = MANIFESTS / "S10R_006_R7_A_CROSS_VIEW_CORNER_OWNERSHIP_RULE_A01_FALSIFICATION_AUDIT.json"
VALIDATION = MANIFESTS / "S10R_006_R7_A_CROSS_VIEW_CORNER_OWNERSHIP_RULE_A01_VALIDATION.json"
R5 = MANIFESTS / "S10R_006_R5_A_LANE_BOUNDARY_COUPLING_RULE_A01_RULE_REGISTRY.json"
R6 = MANIFESTS / "S10R_006_R6_A_CROSS_VIEW_CORNER_OWNERSHIP_AUTHORITY_OPTION_REGISTRY.json"
STEP05 = MANIFESTS / "STEP_05_PIXEL_COORDINATE_FRAME_RECORD.json"
OUTPUT = STEPS / "S10R_006_R7_A_CROSS_VIEW_CORNER_OWNERSHIP_RULE_A01_OUTPUT_RECORD.md"
HANDOFF = HANDOFFS / "S10R_006_R7_A_CROSS_VIEW_CORNER_OWNERSHIP_RULE_A01_TO_DECISION_HANDOFF.md"

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
        RULE,
        FALSIFICATION,
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
    RULE,
    FALSIFICATION,
    VALIDATION,
    R5,
    R6,
    STEP05,
    OUTPUT,
    HANDOFF,
    *sorted(STATUS_PATHS),
]
missing = [str(path.relative_to(ROOT)) for path in required if not path.is_file()]
if missing:
    print(
        json.dumps(
            {
                "schema": "aerathea.s10r_006_r7_a_cross_view_corner_ownership_rule_a01_independent_audit.v1",
                "status": "fail_closed_missing_required_files",
                "missing_files": missing,
            },
            indent=2,
        )
    )
    sys.exit(1)

input_lock = load_json(INPUT_LOCK)
rule = load_json(RULE)
falsification = load_json(FALSIFICATION)
validation = load_json(VALIDATION)
r5 = load_json(R5)
r6 = load_json(R6)
step05 = load_json(STEP05)
output_text = OUTPUT.read_text(encoding="utf-8")
handoff_text = HANDOFF.read_text(encoding="utf-8")

# Gate 1
hash_results = []
for item in input_lock["locked_inputs"]:
    current = sha256(ROOT / item["path"])
    prewrite_match = item["expected_sha256"] == item["actual_sha256"] and item["match"] is True
    controlled = item["policy"].startswith("controlled ")
    valid = prewrite_match and (controlled or current == item["expected_sha256"])
    hash_results.append(
        {
            "path": item["path"],
            "prewrite_match": prewrite_match,
            "current_sha256": current,
            "controlled_status_update_after_prewrite": controlled and current != item["expected_sha256"],
            "valid": valid,
        }
    )
check(
    1,
    "all sixteen locked inputs match",
    len(hash_results) == 16 and all(item["valid"] for item in hash_results),
    hash_results,
)

# Gate 2
contract_hash = sha256(CONTRACT)
approval = input_lock["execution_approval"]
check(
    2,
    "contract hash and exact execution approval match",
    contract_hash == "d1c0905cc51d3b33d000d07f27b6aff05979f9c6ffde4f9145b53b0e1047e431"
    and approval["approver"] == "Flamestrike"
    and approval["statement"] == "approved",
    {"contract_sha256": contract_hash, "approval": approval},
)

# Gate 3
selected_r6 = [item["id"] for item in r6["options"] if item["selected"]]
check(
    3,
    "R6-A remains the selected preparation-only route",
    r6["selected_option"] == "S10R-006-R6-A"
    and selected_r6 == ["S10R-006-R6-A"]
    and r6["selection_record"]["authority_granted"]
    == "preparation only of one separate bounded cross-view corner-ownership rule contract"
    and r6["selection_record"]["corner_rule_authorized"] is False,
    {"selected_option": r6["selected_option"], "selection_record": r6["selection_record"]},
)

# Gate 4
check(
    4,
    "R5 remains approved bounded interpretation for four owned arcs only",
    r5["status"] == "approved_bounded_symbolic_rule_four_blocked_corner_gaps_unowned"
    and r5["artifact_classification"]
    == "authoritative for bounded S10R-006-R5-A symbolic coupling rule only"
    and r5["authorization_flags"]["coupling_rule_approved"] is True
    and r5["authorization_flags"]["rule_evaluation_authorized"] is False,
    {"status": r5["status"], "classification": r5["artifact_classification"]},
)

# Gate 5
expected_lanes = [
    ("AFM-FRONT-RIGHT", "+X", "[-1/2,1/2]"),
    ("AFM-LEFT-LEFT", "+Y", "[3/2,5/2]"),
    ("AFM-FRONT-LEFT", "-X", "[7/2,9/2]"),
    ("AFM-LEFT-RIGHT", "-Y", "[11/2,13/2]"),
]
actual_lanes = [(item["lane_id"], item["cardinal_label"], item["q_interval"]) for item in rule["preserved_owned_lanes"]]
expected_gaps = [
    ("G_0", "(1/2,3/2)"),
    ("G_1", "(5/2,7/2)"),
    ("G_2", "(9/2,11/2)"),
    ("G_3", "(13/2,15/2)"),
]
actual_gaps = [(item["id"], item["open_interval"]) for item in rule["gaps"]]
r5_lanes = [(item["lane_id"], item["cardinal_center"], item["q_interval"]) for item in r5["lanes"]]
r5_gaps = [(item["id"], item["q_interval"]) for item in r5["blocked_gaps"]]
check(
    5,
    "four R5 owned intervals and four open gaps replay exactly",
    actual_lanes == expected_lanes == r5_lanes and actual_gaps == expected_gaps == r5_gaps,
    {"lanes": actual_lanes, "gaps": actual_gaps},
)

# Gate 6
q = rule["abstract_parameter_reference"]
check(
    6,
    "q remains non-periodic unwrapped and unevaluated",
    q["periodic"] is False
    and q["unwrapped"] is True
    and q["modulus"] is None
    and q["wrap"] is None
    and q["final_first_endpoint_identification"] is False
    and q["evaluated_q_instances"] == [],
    q,
)

# Gate 7
axis = step05["world_coordinate_frame"]["panel_axis_mappings"]
expected_adjacency = [
    ("AFM-FRONT-RIGHT / +X", "AFM-LEFT-LEFT / +Y"),
    ("AFM-LEFT-LEFT / +Y", "AFM-FRONT-LEFT / -X"),
    ("AFM-FRONT-LEFT / -X", "AFM-LEFT-RIGHT / -Y"),
    ("AFM-LEFT-RIGHT / -Y", "AFM-FRONT-RIGHT / +X label-only successor"),
]
actual_adjacency = [(item["predecessor"], item["successor"]) for item in rule["gaps"]]
axis_ok = (
    step05["world_coordinate_frame"]["handedness"] == "right_handed"
    and step05["world_coordinate_frame"]["world_up_axis"] == "+Z"
    and axis["front"]["image_x_right"] == "+X"
    and axis["left"]["image_x_right"] == "-Y"
    and rule["step05_axis_replay"]["counterclockwise_cardinal_order_from_positive_x"]
    == ["+X", "+Y", "-X", "-Y"]
)
check(7, "gap adjacencies use only approved construction-lane labels", axis_ok and actual_adjacency == expected_adjacency, actual_adjacency)

# Gate 8
midpoint_evidence = []
midpoint_ok = True
for index, gap in enumerate(rule["gaps"]):
    a = Fraction(gap["a"])
    b = Fraction(gap["b"])
    expected_definition = f"m_{index} = ({gap['a']} + {gap['b']}) / 2"
    valid = a < b and gap["midpoint_symbol"] == f"m_{index}" and gap["midpoint_definition"] == expected_definition
    midpoint_ok = midpoint_ok and valid
    midpoint_evidence.append({"id": gap["id"], "definition": gap["midpoint_definition"], "valid": valid})
check(8, "every m_k is an exact symbolic rational midpoint", midpoint_ok, midpoint_evidence)

# Gate 9
expected_lower = [
    "1/2 < q < m_0 -> AFM-FRONT-RIGHT / +X",
    "5/2 < q < m_1 -> AFM-LEFT-LEFT / +Y",
    "9/2 < q < m_2 -> AFM-FRONT-LEFT / -X",
    "13/2 < q < m_3 -> AFM-LEFT-RIGHT / -Y",
]
actual_lower = [item["lower_branch"] for item in rule["gaps"]]
check(9, "each lower branch maps only to its predecessor label", actual_lower == expected_lower, actual_lower)

# Gate 10
expected_upper = [
    "m_0 <= q < 3/2 -> AFM-LEFT-LEFT / +Y",
    "m_1 <= q < 7/2 -> AFM-FRONT-LEFT / -X",
    "m_2 <= q < 11/2 -> AFM-LEFT-RIGHT / -Y",
    "m_3 <= q < 15/2 -> AFM-FRONT-RIGHT / +X label-only successor",
]
actual_upper = [item["upper_branch"] for item in rule["gaps"]]
check(10, "each upper branch maps only to its successor label", actual_upper == expected_upper, actual_upper)

# Gate 11
check(
    11,
    "branches are total and disjoint over every open gap",
    all(item["branch_totality"] == f"symbolically total over {item['id']}" for item in rule["gaps"])
    and all(item["branch_intersection"] == "empty" for item in rule["gaps"])
    and rule["candidate_gap_rule"]["tie_policy"] == "single successor owner label at the exact symbolic midpoint",
    {"gaps": rule["gaps"], "tie_policy": rule["candidate_gap_rule"]["tie_policy"]},
)

# Gate 12
endpoint = rule["endpoint_policy"]
check(
    12,
    "existing R5 endpoint ownership is unchanged",
    endpoint["existing_r5_lane_endpoints_mutated"] is False
    and endpoint["gap_endpoints_reassigned"] is False
    and all(item["endpoint_ownership"] == "unchanged approved R5 lane ownership" for item in rule["preserved_owned_lanes"]),
    endpoint,
)

# Gate 13
g3 = rule["gaps"][3]
check(
    13,
    "G_3 creates no wrap modulo new lane or endpoint identification",
    g3["id"] == "G_3"
    and g3["periodic_wrap"] is False
    and g3["new_lane_created"] is False
    and g3["q_15_over_2_identified_with_q_minus_1_over_2"] is False,
    g3,
)

# Gate 14
history = rule["historical_i10_010_a"]
check(
    14,
    "historical I10-010-A remains revision-required candidate history",
    history
    == {
        "classification": "candidate history",
        "step10r_status": "requires_revision",
        "copied_as_authority": False,
        "modified": False,
    },
    history,
)

# Gate 15
holdouts = rule["holdouts"]
check(
    15,
    "fourteen back/right records remain proof only",
    holdouts
    == {
        "classification": "proof only",
        "back_count": 6,
        "right_count": 8,
        "total": 14,
        "construction_use_authorized": False,
    },
    holdouts,
)

# Gate 16
forbidden_policy_keys = [
    "owner_label_change_is_geometry_seam",
    "continuity_defined",
    "interpolation_defined",
    "top_upright_owner_defined",
    "top_upright_join_defined",
    "cross_lane_seam_defined",
    "cross_view_seam_defined",
    "endpoint_join_defined",
    "closure_defined",
]
check(
    16,
    "no top/upright ownership seam join interpolation or closure is defined",
    all(endpoint[key] is False for key in forbidden_policy_keys),
    {key: endpoint[key] for key in forbidden_policy_keys},
)

# Gate 17
flags = rule["authorization_flags"]
check(
    17,
    "bounded symbolic rule is approved only within the exact Flamestrike decision scope",
    rule["artifact_classification"]
    == "authoritative for bounded S10R-006-R7-A symbolic corner-ownership rule only"
    and rule["technical_result"]
    == "pass_approved_bounded_cross_view_corner_ownership_rule_registered_no_implementation"
    and rule["candidate_gap_rule"]["classification"] == "approved bounded symbolic interpretation only"
    and rule["candidate_gap_rule"]["approved"] is True
    and rule["execution_record"]["candidate_rule_decision"] == "approve"
    and rule["execution_record"]["candidate_rule_decision_statement"] == "approved"
    and rule["execution_record"]["candidate_rule_approved"] is True
    and flags["candidate_rule_registered"] is True
    and flags["corner_ownership_rule_approved"] is True,
    {"status": rule["status"], "execution_record": rule["execution_record"], "flags": flags},
)

# Gate 18
counts = rule["output_counts"]
instance_keys = [
    "per_point_owner_instances",
    "evaluated_q_instances",
    "evaluated_midpoint_samples",
    "samples",
    "source_pixels_assigned",
    "source_normals_assigned",
    "source_to_target_transforms",
    "physical_pairs",
    "target_coordinates",
    "centers",
    "pivots",
    "anchors",
]
check(
    18,
    "owner and q instances samples coordinates transforms pairs centers pivots and anchors remain zero",
    all(counts[key] == 0 for key in instance_keys) and all(item["owner_instances"] == [] for item in rule["gaps"]),
    {key: counts[key] for key in instance_keys},
)

# Gate 19
field_keys = ["seams", "joins", "closures", "fields", "fills", "surfaces", "topology", "geometry"]
check(
    19,
    "fields fills surfaces topology and geometry remain zero",
    all(counts[key] == 0 for key in field_keys),
    {key: counts[key] for key in field_keys},
)

# Gate 20
expected_blocks = [
    {"id": "S10R-BLOCK-006", "status": "active_approved_cross_view_corner_ownership_rule_no_field_no_seam_no_join_no_closure"},
    {"id": "S10R-BLOCK-008", "status": "active_unchanged"},
    {"id": "S10R-BLOCK-009", "status": "active_unchanged"},
]
check(
    20,
    "all three blocks remain active and resolved block IDs remain empty",
    rule["active_blocks"] == expected_blocks and rule["resolved_block_ids"] == [],
    {"active": rule["active_blocks"], "resolved": rule["resolved_block_ids"]},
)

# Gate 21
check(
    21,
    "evaluation implementation downstream and Git authorization flags remain false",
    flags["candidate_rule_registered"] is True
    and flags["corner_ownership_rule_approved"] is True
    and all(
        value is False
        for key, value in flags.items()
        if key not in {"candidate_rule_registered", "corner_ownership_rule_approved"}
    ),
    flags,
)

# Gate 22
git_lines = subprocess.run(
    ["git", "status", "--porcelain=v1", "-uall"], cwd=ROOT, check=True, text=True, capture_output=True
).stdout.splitlines()
status_names = {path.name for path in STATUS_PATHS}
scoped_paths = {
    line[3:]
    for line in git_lines
    if len(line) >= 4
    and (
        "S10R_006_R7_A_CROSS_VIEW_CORNER_OWNERSHIP_RULE_A01" in line[3:]
        or line[3:].endswith("audit_bloodaxe_cairnstone_a005_s10r006_r7_a_cross_view_corner_ownership_rule_a01.py")
        or Path(line[3:]).name in status_names
    )
}
staged = subprocess.run(
    ["git", "diff", "--cached", "--name-only"], cwd=ROOT, check=True, text=True, capture_output=True
).stdout.splitlines()
status_markers = {
    A005 / "SM_GIA_BloodAxeCairnstone_A005_RESET_RESUME_STATE.md": [
        "S10R-006-R7-A Approved Bounded Rule Decision Closeout",
        "active_approved_cross_view_corner_ownership_rule_no_field_no_seam_no_join_no_closure",
    ],
    A005 / "SM_GIA_BloodAxeCairnstone_A005_APPROVAL_LOG.md": [
        "S10R-006-R7-A Bounded Rule Decision",
        "Decision statement: `approved`",
    ],
    A005 / "SM_GIA_BloodAxeCairnstone_A005_ARTIFACT_INDEX.md": [
        "S10R-006-R7-A Cross-View Corner-Ownership Rule A01 - Approved Bounded Rule",
        "Core reassessment only",
    ],
}
marker_evidence = {
    str(path.relative_to(ROOT)): {marker: marker in path.read_text(encoding="utf-8") for marker in markers}
    for path, markers in status_markers.items()
}
check(
    22,
    "changed paths match execution allowlist and no path is staged",
    scoped_paths == EXPECTED_SCOPED_PATHS and staged == [] and all(all(item.values()) for item in marker_evidence.values()),
    {
        "scoped_paths": sorted(scoped_paths),
        "expected_paths": sorted(EXPECTED_SCOPED_PATHS),
        "staged": staged,
        "status_markers": marker_evidence,
    },
)

# Gate 23
visible = validation["post_decision_visible_review"]
validation_gate_23 = validation["validation_gates"][22]
falsification_f22 = falsification["checks"][21]
check(
    23,
    "output and handoff visibility verified before mandatory stop",
    visible["verified"] is True
    and visible["output_record"].startswith("verified in visible gedit window")
    and visible["decision_handoff"].startswith("verified in visible gedit window")
    and visible["global_desktop_titles_surfaced"] is False
    and validation_gate_23["gate"] == 23
    and validation_gate_23["status"] == "pass"
    and falsification_f22["id"] == "F22"
    and falsification_f22["status"] == "pass"
    and "pass_approved_bounded_cross_view_corner_ownership_rule_registered_no_implementation" in output_text
    and "Required Post-Decision Stop" in handoff_text,
    {"visible_review": visible, "validation_gate_23": validation_gate_23, "falsification_f22": falsification_f22},
)

if [item["gate"] for item in checks] != list(range(1, 24)):
    raise RuntimeError("auditor gates are not exactly 1..23")

failed = [item for item in checks if item["status"] == "fail"]
result = {
    "schema": "aerathea.s10r_006_r7_a_cross_view_corner_ownership_rule_a01_independent_audit.v1",
    "status": "pass" if not failed else "fail",
    "artifact_classification": "proof only",
    "gate_count": len(checks),
    "passed_gate_count": len(checks) - len(failed),
    "failed_gate_count": len(failed),
    "checks": checks,
}
print(json.dumps(result, indent=2))
sys.exit(0 if not failed else 1)
