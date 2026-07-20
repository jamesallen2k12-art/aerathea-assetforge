#!/usr/bin/env python3
"""Read-only independent audit for A005 S10R-006-R5-A rule records."""

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

CONTRACT = STEPS / "S10R_006_R5_A_LANE_BOUNDARY_COUPLING_RULE_A01_CONTRACT.md"
INPUT_LOCK = MANIFESTS / "S10R_006_R5_A_LANE_BOUNDARY_COUPLING_RULE_A01_INPUT_LOCK.json"
RULE = MANIFESTS / "S10R_006_R5_A_LANE_BOUNDARY_COUPLING_RULE_A01_RULE_REGISTRY.json"
FALSIFICATION = MANIFESTS / "S10R_006_R5_A_LANE_BOUNDARY_COUPLING_RULE_A01_FALSIFICATION_AUDIT.json"
VALIDATION = MANIFESTS / "S10R_006_R5_A_LANE_BOUNDARY_COUPLING_RULE_A01_VALIDATION.json"
R3 = MANIFESTS / "S10R_006_R3_A_ABSTRACT_FIELD_METHOD_A01_METHOD_REGISTRY.json"
R4 = MANIFESTS / "S10R_006_R4_A_LANE_BOUNDARY_COUPLING_AUTHORITY_OPTION_REGISTRY.json"
STEP05 = MANIFESTS / "STEP_05_PIXEL_COORDINATE_FRAME_RECORD.json"
OUTPUT = STEPS / "S10R_006_R5_A_LANE_BOUNDARY_COUPLING_RULE_A01_OUTPUT_RECORD.md"
HANDOFF = HANDOFFS / "S10R_006_R5_A_LANE_BOUNDARY_COUPLING_RULE_A01_TO_DECISION_HANDOFF.md"

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
    R3,
    R4,
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
                "schema": "aerathea.s10r_006_r5_a_lane_boundary_coupling_rule_a01_independent_audit.v1",
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
r3 = load_json(R3)
r4 = load_json(R4)
step05 = load_json(STEP05)
output_text = OUTPUT.read_text(encoding="utf-8")
handoff_text = HANDOFF.read_text(encoding="utf-8")

# Gate 1
hash_results = []
for item in input_lock["locked_inputs"]:
    current = sha256(ROOT / item["path"])
    prewrite_match = item["expected_sha256"] == item["actual_sha256"] and item["match"] is True
    controlled = item["policy"] == "controlled prepared-contract status state"
    hash_results.append(
        {
            "path": item["path"],
            "prewrite_match": prewrite_match,
            "current_sha256": current,
            "controlled_status_update_after_prewrite": controlled and current != item["expected_sha256"],
            "valid": prewrite_match and (controlled or current == item["expected_sha256"]),
        }
    )
check(1, "all eighteen locked inputs match", len(hash_results) == 18 and all(x["valid"] for x in hash_results), hash_results)

# Gate 2
contract_hash = sha256(CONTRACT)
check(
    2,
    "contract hash and exact execution approval match",
    contract_hash == "ac17ba4beb12d5370cce6562c3846a24f3541a062112bca02e2ef850d0134a96"
    and input_lock["execution_approval"]["approver"] == "Flamestrike"
    and input_lock["execution_approval"]["statement"] == "I approve",
    {"contract_sha256": contract_hash, "approval": input_lock["execution_approval"]},
)

# Gate 3
check(
    3,
    "R4-A remains sole selected preparation route",
    r4["selected_option"] == "S10R-006-R4-A"
    and [x["id"] for x in r4["options"] if x["selected"]] == ["S10R-006-R4-A"]
    and r4["selection_record"]["authority_granted"]
    == "preparation only of a separate bounded lane-to-H_v coupling-rule contract"
    and r4["selection_record"]["coupling_rule_authorized"] is False,
    {"selected_option": r4["selected_option"], "selection_record": r4["selection_record"]},
)

# Gate 4
check(
    4,
    "R3 remains approved bounded symbolic interpretation only",
    r3["status"] == "approved_bounded_symbolic_method_no_field_coupling"
    and r3["artifact_classification"] == "authoritative for bounded S10R-006-R3-A symbolic method only",
    {"status": r3["status"], "classification": r3["artifact_classification"]},
)

# Gate 5
check(
    5,
    "lane and construction-record counts remain exact",
    len(r3["lanes"]) == 4
    and r3["authority_counts"]["symbolic_lanes"] == 4
    and r3["authority_counts"]["approved_construction_records"] == 12,
    {"lanes": len(r3["lanes"]), "records": r3["authority_counts"]["approved_construction_records"]},
)

# Gate 6
expected_lanes = [
    ("AFM-FRONT-RIGHT", "front", "XZ", "right", ["F-BTIR-02", "F-BTIR-04", "F-BTIR-06"], "+X", "0", "[-1/2,1/2]"),
    ("AFM-LEFT-LEFT", "left", "YZ", "left", ["L-BTIR-01", "L-BTIR-03", "L-BTIR-05"], "+Y", "2", "[3/2,5/2]"),
    ("AFM-FRONT-LEFT", "front", "XZ", "left", ["F-BTIR-01", "F-BTIR-03", "F-BTIR-05"], "-X", "4", "[7/2,9/2]"),
    ("AFM-LEFT-RIGHT", "left", "YZ", "right", ["L-BTIR-02", "L-BTIR-04", "L-BTIR-06"], "-Y", "6", "[11/2,13/2]"),
]
lane_replay = [
    (
        x["lane_id"],
        x["owner_view"],
        x["owner_plane"],
        x["registered_side"],
        x["trace_ids"],
        x["cardinal_center"],
        x["q_center"],
        x["q_interval"],
    )
    for x in rule["lanes"]
]
r3_lane_by_id = {x["lane_id"]: x for x in r3["lanes"]}
r3_exact = all(
    r3_lane_by_id[x["lane_id"]]["owner_view"] == x["owner_view"]
    and r3_lane_by_id[x["lane_id"]]["owner_plane"] == x["owner_plane"]
    and r3_lane_by_id[x["lane_id"]]["registered_side"] == x["registered_side"]
    and r3_lane_by_id[x["lane_id"]]["trace_ids"] == x["trace_ids"]
    and r3_lane_by_id[x["lane_id"]]["within_side_orders"] == x["within_side_orders"] == [1, 2, 3]
    and r3_lane_by_id[x["lane_id"]]["u_stations"] == x["u_stations"] == ["0", "1/2", "1"]
    for x in rule["lanes"]
)
check(6, "all lane identities records orders and u stations remain exact", lane_replay == expected_lanes and r3_exact, lane_replay)

# Gate 7
axis = step05["world_coordinate_frame"]["panel_axis_mappings"]
axis_ok = (
    step05["world_coordinate_frame"]["handedness"] == "right_handed"
    and step05["world_coordinate_frame"]["world_up_axis"] == "+Z"
    and axis["front"]["image_x_right"] == "+X"
    and axis["left"]["image_x_right"] == "-Y"
    and rule["step05_axis_replay"]
    == {
        "frame_handedness": "right_handed",
        "up": "+Z",
        "front_image_right": "+X",
        "front_image_left": "-X",
        "left_image_right": "-Y",
        "left_image_left": "+Y",
        "classification": "evidence replay only",
    }
)
check(7, "Step 05 cardinal-axis mappings replay exactly", axis_ok, {"step05": axis, "rule": rule["step05_axis_replay"]})

# Gate 8
q = rule["abstract_parameter"]
check(
    8,
    "q orientation zero direction and non-periodic policy are exact",
    q["name"] == "q"
    and q["orientation"] == "increasing q is counterclockwise in the +X,+Y plane when viewed from +Z"
    and q["zero_direction"] == "+X"
    and q["periodic"] is False
    and q["modulus"] is None
    and q["wrap"] is None,
    q,
)

# Gate 9
check(
    9,
    "theta domain lane centers intervals and q_L formulas match contract",
    q["angular_conversion"] == "theta(q) = pi*q/4"
    and q["domain"] == "D_q = [-1/2,1/2] union [3/2,5/2] union [7/2,9/2] union [11/2,13/2]"
    and [x["q_center"] for x in rule["lanes"]] == ["0", "2", "4", "6"]
    and [x["q_interval"] for x in rule["lanes"]] == ["[-1/2,1/2]", "[3/2,5/2]", "[7/2,9/2]", "[11/2,13/2]"]
    and all(x["q_map"] == "q_L(u) = c_L + u - 1/2, 0 <= u <= 1" for x in rule["lanes"]),
    {"parameter": q, "lanes": rule["lanes"]},
)

# Gate 10
intervals = [
    (Fraction(-1, 2), Fraction(1, 2)),
    (Fraction(3, 2), Fraction(5, 2)),
    (Fraction(7, 2), Fraction(9, 2)),
    (Fraction(11, 2), Fraction(13, 2)),
]
check(
    10,
    "owned intervals are pairwise disjoint",
    all(intervals[i][1] < intervals[i + 1][0] for i in range(3))
    and rule["sector_policy"]["pairwise_disjoint_owned_intervals"] is True,
    [[str(a), str(b)] for a, b in intervals],
)

# Gate 11
expected_gaps = [("G_0", "(1/2,3/2)"), ("G_1", "(5/2,7/2)"), ("G_2", "(9/2,11/2)"), ("G_3", "(13/2,15/2)")]
actual_gaps = [(x["id"], x["q_interval"]) for x in rule["blocked_gaps"]]
check(
    11,
    "exactly four nonempty open gaps remain unowned",
    actual_gaps == expected_gaps
    and rule["sector_policy"]["blocked_open_gap_count"] == 4
    and all("unowned_blocked" in x["status"] for x in rule["blocked_gaps"]),
    rule["blocked_gaps"],
)

# Gate 12
sector = rule["sector_policy"]
check(
    12,
    "no wrap seam join or closed ownership is defined",
    q["final_first_endpoint_identification"] is False
    and sector["cross_lane_seam"] is None
    and sector["cross_view_seam"] is None
    and sector["front_left_view_join"] is None
    and sector["side_to_side_join"] is None
    and sector["top_upright_join"] is None
    and sector["periodic_wrap"] is False
    and sector["closed_360_ownership"] is False,
    sector,
)

# Gate 13
boundary = rule["boundary_family"]
check(
    13,
    "B_v matches the exact unevaluated signed-power formula",
    boundary["s"] == "s(v) = 0.8 + 0.2v"
    and boundary["a"] == "a(v) = 56 + 14v"
    and boundary["b"] == "b(v) = 44 + 11v"
    and boundary["signed_power"] == "spow_2_3(r) = sign(r) * abs(r)^(2/3)"
    and boundary["parameterization"] == "B_v(q) = (a(v)*spow_2_3(cos(theta(q))), b(v)*spow_2_3(sin(theta(q))))"
    and boundary["evaluated_samples"] == [],
    boundary,
)

# Gate 14
check(
    14,
    "symbolic B_v identity reduces to H_v without sampling",
    boundary["implicit_family"] == "H_v: abs(x/a(v))^3 + abs(y/b(v))^3 = 1"
    and boundary["symbolic_identity"] == "abs(B_x/a(v))^3 + abs(B_y/b(v))^3 = cos(theta(q))^2 + sin(theta(q))^2 = 1"
    and falsification["checks"][8]["id"] == "F09"
    and falsification["checks"][8]["status"] == "pass",
    {"implicit": boundary["implicit_family"], "identity": boundary["symbolic_identity"]},
)

# Gate 15
endpoint = r3["boundary_family"]["endpoint_audit"]
check(
    15,
    "v=t and K80/N3 endpoint identities remain exact",
    r3["construction_frame"]["v_identity"] == "v = t"
    and endpoint == {"s_0": "0.8", "s_1": "1", "a_0": 56, "a_1": 70, "b_0": 44, "b_1": 55}
    and rule["coupling_descriptor"]["v_identity"] == "v = t",
    {"v_identity": r3["construction_frame"]["v_identity"], "endpoints": endpoint},
)

# Gate 16
weights = r3["between_trace_operator"]
check(
    16,
    "W_L remains unevaluated adjacent-record-only and unchanged",
    weights["classification"] == "unevaluated symbolic record-weight descriptor"
    and weights["properties"]["adjacent_records_only"] is True
    and weights["properties"]["cross_lane_interpolation"] is False
    and rule["coupling_descriptor"]["record_weight_descriptor"]
    == "W_L(u,v) = {(T_j, v, 1-lambda), (T_(j+1), v, lambda)}",
    {"r3": weights, "r5": rule["coupling_descriptor"]["record_weight_descriptor"]},
)

# Gate 17
coupling = rule["coupling_descriptor"]
check(
    17,
    "C_L is approved bounded unevaluated interpretation only",
    coupling["boundary_map"] == "C_L(u,v) = B_v(q_L(u))"
    and coupling["classification"] == "approved bounded unevaluated symbolic interpretation descriptor only"
    and coupling["evaluated"] is False
    and coupling["physical_source_relation"] is False
    and coupling["target_coordinate_relation"] is False,
    coupling,
)

# Gate 18
holdouts = rule["holdouts"]
check(
    18,
    "all fourteen back/right records remain proof only",
    holdouts == {"classification": "proof only", "back_count": 6, "right_count": 8, "total": 14, "construction_use_authorized": False},
    holdouts,
)

# Gate 19
output_counts = rule["output_counts"]
no_instance_keys = [
    "per_record_parameter_instances",
    "evaluated_parameter_samples",
    "evaluated_boundary_samples",
    "evaluated_coupling_samples",
    "source_to_target_transforms",
    "physical_pairs",
    "target_coordinates",
    "centers",
    "pivots",
    "anchors",
]
check(
    19,
    "no parameter instance sample transform pair coordinate center pivot or anchor exists",
    all(output_counts[key] == 0 for key in no_instance_keys)
    and all(x["per_record_q_values"] == [] for x in rule["lanes"]),
    {key: output_counts[key] for key in no_instance_keys},
)

# Gate 20
field_keys = ["seams", "joins", "closures", "fields", "fills", "surfaces", "topology", "geometry"]
check(
    20,
    "seam join closure field fill surface topology and geometry counts remain zero",
    all(output_counts[key] == 0 for key in field_keys),
    {key: output_counts[key] for key in field_keys},
)

# Gate 21
check(
    21,
    "approved rule components remain bounded interpretation rather than source evidence",
    q["classification"] == "approved bounded dimensionless interpretation parameter only"
    and all(x["classification"] == "approved bounded interpretation only" for x in rule["lanes"])
    and boundary["classification"] == "approved bounded unevaluated interpretation formula only"
    and coupling["classification"] == "approved bounded unevaluated symbolic interpretation descriptor only"
    and q["physical_angle_claim"] is False
    and q["source_angle_claim"] is False,
    {"q": q["classification"], "boundary": boundary["classification"], "coupling": coupling["classification"]},
)

# Gate 22
active = rule["active_blocks"]
check(
    22,
    "all three blocks remain active and none is resolved",
    active == [
        {"id": "S10R-BLOCK-006", "status": "active_approved_lane_boundary_coupling_rule_four_corner_gaps_unowned_no_field"},
        {"id": "S10R-BLOCK-008", "status": "active_unchanged"},
        {"id": "S10R-BLOCK-009", "status": "active_unchanged"},
    ]
    and rule["resolved_block_ids"] == [],
    {"active": active, "resolved": rule["resolved_block_ids"]},
)

# Gate 23
flags = rule["authorization_flags"]
check(
    23,
    "candidate registration and bounded rule approval are true while evaluation implementation downstream and Git flags are false",
    flags["candidate_rule_registered"] is True
    and flags["coupling_rule_approved"] is True
    and all(
        value is False
        for key, value in flags.items()
        if key not in {"candidate_rule_registered", "coupling_rule_approved"}
    ),
    flags,
)

# Gate 24
git_lines = subprocess.run(
    ["git", "status", "--porcelain=v1", "-uall"], cwd=ROOT, check=True, text=True, capture_output=True
).stdout.splitlines()
status_names = {path.name for path in STATUS_PATHS}
scoped_paths = {
    line[3:]
    for line in git_lines
    if len(line) >= 4
    and (
        "S10R_006_R5_A_LANE_BOUNDARY_COUPLING_RULE_A01" in line[3:]
        or line[3:].endswith("audit_bloodaxe_cairnstone_a005_s10r006_r5_a_lane_boundary_coupling_rule_a01.py")
        or Path(line[3:]).name in status_names
    )
}
status_markers = {
    A005 / "SM_GIA_BloodAxeCairnstone_A005_RESET_RESUME_STATE.md": [
        "S10R-006-R5-A Approved Bounded Rule Decision Closeout",
        "active_approved_lane_boundary_coupling_rule_four_corner_gaps_unowned_no_field",
    ],
    A005 / "SM_GIA_BloodAxeCairnstone_A005_APPROVAL_LOG.md": [
        "S10R-006-R5-A Bounded Rule Decision",
        "Approval statement: `approved`",
    ],
    A005 / "SM_GIA_BloodAxeCairnstone_A005_ARTIFACT_INDEX.md": [
        "S10R-006-R5-A Lane-Boundary Coupling Rule A01 - Approved Bounded Rule",
        "four blocked corner gaps",
    ],
}
marker_evidence = {
    str(path.relative_to(ROOT)): {marker: marker in path.read_text(encoding="utf-8") for marker in markers}
    for path, markers in status_markers.items()
}
check(
    24,
    "changed paths match execution allowlist",
    scoped_paths == EXPECTED_SCOPED_PATHS and all(all(x.values()) for x in marker_evidence.values()),
    {"scoped_paths": sorted(scoped_paths), "expected_paths": sorted(EXPECTED_SCOPED_PATHS), "status_markers": marker_evidence},
)

# Gate 25
staged = subprocess.run(
    ["git", "diff", "--cached", "--name-only"], cwd=ROOT, check=True, text=True, capture_output=True
).stdout.splitlines()
check(25, "no path is staged", staged == [], staged)

# Gate 26
visible = validation["post_decision_visible_review"]
check(
    26,
    "approved output and handoff visibility verified before Core reassessment stop",
    visible["verified"] is True
    and visible["output_record"].startswith("verified in dedicated")
    and visible["decision_handoff"].startswith("verified in dedicated")
    and visible["global_desktop_titles_surfaced"] is False,
    visible,
)

if [x["gate"] for x in checks] != list(range(1, 27)):
    raise RuntimeError("auditor gates are not exactly 1..26")

failed = [x for x in checks if x["status"] == "fail"]
result = {
    "schema": "aerathea.s10r_006_r5_a_lane_boundary_coupling_rule_a01_independent_audit.v1",
    "status": "pass" if not failed else "fail",
    "artifact_classification": "proof only",
    "gate_count": len(checks),
    "passed_gate_count": len(checks) - len(failed),
    "failed_gate_count": len(failed),
    "checks": checks,
}
print(json.dumps(result, indent=2))
sys.exit(0 if not failed else 1)
