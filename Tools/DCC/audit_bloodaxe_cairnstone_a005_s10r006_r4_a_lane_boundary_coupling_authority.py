#!/usr/bin/env python3
"""Read-only independent audit for A005 S10R-006-R4-A candidate records."""

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

CONTRACT = STEPS / "S10R_006_R4_A_LANE_BOUNDARY_COUPLING_AUTHORITY_DECISION_CONTRACT.md"
INPUT_LOCK = MANIFESTS / "S10R_006_R4_A_LANE_BOUNDARY_COUPLING_AUTHORITY_INPUT_LOCK.json"
DEPENDENCY = MANIFESTS / "S10R_006_R4_A_LANE_BOUNDARY_COUPLING_AUTHORITY_DEPENDENCY_AUDIT.json"
OPTIONS = MANIFESTS / "S10R_006_R4_A_LANE_BOUNDARY_COUPLING_AUTHORITY_OPTION_REGISTRY.json"
VALIDATION = MANIFESTS / "S10R_006_R4_A_LANE_BOUNDARY_COUPLING_AUTHORITY_VALIDATION.json"
R3_METHOD = MANIFESTS / "S10R_006_R3_A_ABSTRACT_FIELD_METHOD_A01_METHOD_REGISTRY.json"
OUTPUT = STEPS / "S10R_006_R4_A_LANE_BOUNDARY_COUPLING_AUTHORITY_DECISION_OUTPUT_RECORD.md"
HANDOFF = HANDOFFS / "S10R_006_R4_A_LANE_BOUNDARY_COUPLING_AUTHORITY_TO_DECISION_HANDOFF.md"

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


required_files = [
    CONTRACT,
    INPUT_LOCK,
    DEPENDENCY,
    OPTIONS,
    VALIDATION,
    R3_METHOD,
    OUTPUT,
    HANDOFF,
    *sorted(STATUS_PATHS),
]
missing_files = [str(path.relative_to(ROOT)) for path in required_files if not path.is_file()]
if missing_files:
    print(
        json.dumps(
            {
                "schema": "aerathea.s10r_006_r4_a_lane_boundary_coupling_authority_independent_audit.v1",
                "status": "fail_closed_missing_required_files",
                "artifact_classification": "proof only",
                "missing_files": missing_files,
            },
            indent=2,
        )
    )
    sys.exit(1)

input_lock = load_json(INPUT_LOCK)
dependency = load_json(DEPENDENCY)
options = load_json(OPTIONS)
validation = load_json(VALIDATION)
r3 = load_json(R3_METHOD)
output_text = OUTPUT.read_text(encoding="utf-8")
handoff_text = HANDOFF.read_text(encoding="utf-8")

# Gate 1: all fifteen inputs matched before any R4 execution write. The three
# controlled status records may change afterward only within this contract.
lock_results = []
for item in input_lock["locked_inputs"]:
    path = ROOT / item["path"]
    current = sha256(path)
    prewrite_match = (
        item["expected_sha256"] == item["actual_sha256"] and item["match"] is True
    )
    controlled = item["policy"] == "controlled prepared-contract status state"
    lock_results.append(
        {
            "path": item["path"],
            "prewrite_match": prewrite_match,
            "current_sha256": current,
            "controlled_status_update_after_prewrite": controlled
            and current != item["expected_sha256"],
            "valid": prewrite_match and (controlled or current == item["expected_sha256"]),
        }
    )
check(
    1,
    "all fifteen locked inputs match",
    len(lock_results) == 15 and all(item["valid"] for item in lock_results),
    lock_results,
)

# Gate 2
contract_text = CONTRACT.read_text(encoding="utf-8")
contract_ok = (
    sha256(CONTRACT) == "0fe60e337c4b5124677b1e09746002d1624210005024e7c8f08dcd37432a279d"
    and input_lock["execution_approval"]["approver"] == "Flamestrike"
    and input_lock["execution_approval"]["statement"] == "approved"
    and "A005-CR-S10R-006-R4-A-LBCA-DEC-A01" in contract_text
)
check(2, "contract hash and exact execution approval match", contract_ok, {
    "contract_sha256": sha256(CONTRACT),
    "approval": input_lock["execution_approval"],
})

# Gate 3
check(
    3,
    "R3 remains approved bounded symbolic interpretation only",
    r3["status"] == "approved_bounded_symbolic_method_no_field_coupling"
    and r3["technical_result"] == "pass_bounded_symbolic_method_registered_no_field_coupling"
    and r3["artifact_classification"]
    == "authoritative for bounded S10R-006-R3-A symbolic method only",
    {
        "status": r3["status"],
        "technical_result": r3["technical_result"],
        "artifact_classification": r3["artifact_classification"],
    },
)

# Gate 4
check(
    4,
    "lane and construction-record counts remain exact",
    len(r3["lanes"]) == 4
    and r3["authority_counts"]["symbolic_lanes"] == 4
    and r3["authority_counts"]["approved_construction_records"] == 12,
    {
        "lanes": len(r3["lanes"]),
        "records": r3["authority_counts"]["approved_construction_records"],
    },
)

# Gate 5
expected_lanes = [
    {
        "lane_id": "AFM-FRONT-LEFT",
        "owner_view": "front",
        "owner_plane": "XZ",
        "registered_side": "left",
        "trace_ids": ["F-BTIR-01", "F-BTIR-03", "F-BTIR-05"],
        "within_side_orders": [1, 2, 3],
        "u_stations": ["0", "1/2", "1"],
    },
    {
        "lane_id": "AFM-FRONT-RIGHT",
        "owner_view": "front",
        "owner_plane": "XZ",
        "registered_side": "right",
        "trace_ids": ["F-BTIR-02", "F-BTIR-04", "F-BTIR-06"],
        "within_side_orders": [1, 2, 3],
        "u_stations": ["0", "1/2", "1"],
    },
    {
        "lane_id": "AFM-LEFT-LEFT",
        "owner_view": "left",
        "owner_plane": "YZ",
        "registered_side": "left",
        "trace_ids": ["L-BTIR-01", "L-BTIR-03", "L-BTIR-05"],
        "within_side_orders": [1, 2, 3],
        "u_stations": ["0", "1/2", "1"],
    },
    {
        "lane_id": "AFM-LEFT-RIGHT",
        "owner_view": "left",
        "owner_plane": "YZ",
        "registered_side": "right",
        "trace_ids": ["L-BTIR-02", "L-BTIR-04", "L-BTIR-06"],
        "within_side_orders": [1, 2, 3],
        "u_stations": ["0", "1/2", "1"],
    },
]
check(5, "all lane identities and rank stations remain exact", r3["lanes"] == expected_lanes, r3["lanes"])

# Gate 6
endpoint = r3["boundary_family"]["endpoint_audit"]
check(
    6,
    "v=t and K80/N3 endpoint identities remain exact",
    r3["construction_frame"]["v_identity"] == "v = t"
    and endpoint
    == {"s_0": "0.8", "s_1": "1", "a_0": 56, "a_1": 70, "b_0": 44, "b_1": 55},
    {"v_identity": r3["construction_frame"]["v_identity"], "endpoint_audit": endpoint},
)

# Gate 7
weights = r3["between_trace_operator"]
check(
    7,
    "W_lane remains unevaluated and adjacent-record-only",
    weights["classification"] == "unevaluated symbolic record-weight descriptor"
    and weights["properties"]["adjacent_records_only"] is True
    and weights["properties"]["cross_lane_interpolation"] is False,
    weights,
)

# Gate 8
check(
    8,
    "H_v remains unevaluated",
    "registered unevaluated" in r3["boundary_family"]["classification"]
    and dependency["r3_authority"]["boundary_family"].endswith("registered unevaluated"),
    {
        "r3": r3["boundary_family"]["classification"],
        "dependency": dependency["r3_authority"]["boundary_family"],
    },
)

# Gate 9
coupling = r3["coupling"]
coupling_null_keys = [
    "lane_to_boundary_function",
    "angular_placement",
    "arc_length_placement",
    "source_to_target_transform",
    "cross_lane_seam",
    "top_upright_join",
]
check(
    9,
    "every R3 coupling field remains null or false",
    all(coupling[key] is None for key in coupling_null_keys)
    and coupling["closed_field"] is False
    and coupling["physical_field"] is False,
    coupling,
)

# Gate 10
holdouts = r3["holdouts"]
check(
    10,
    "all fourteen back/right records remain proof only",
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

# Gate 11
option_ids = [item["id"] for item in options["options"]]
check(
    11,
    "both required R4 options appear exactly once",
    option_ids == ["S10R-006-R4-A", "S10R-006-R4-BLOCK"]
    and len(set(option_ids)) == 2
    and all(option_ids.count(option_id) == 1 for option_id in option_ids)
    and all(option_id in output_text and option_id in handoff_text for option_id in option_ids),
    option_ids,
)

# Gate 12
check(
    12,
    "Flamestrike selection matches the candidate recommendation exactly",
    options["candidate_recommendation"] == "S10R-006-R4-A"
    and options["recommendation_classification"] == "candidate recommendation only"
    and options["recommendation_selected"] is True
    and options["selected_option"] == "S10R-006-R4-A"
    and options["options"][0]["selected"] is True
    and options["options"][0]["flamestrike_decision"] == "approved"
    and options["options"][1]["selected"] is False
    and options["options"][1]["flamestrike_decision"] == "not selected"
    and options["selection_record"]["approver"] == "Flamestrike"
    and options["selection_record"]["approval_statement"]
    == "ok lets follow your recommendation",
    {
        "recommendation": options["candidate_recommendation"],
        "recommendation_selected": options["recommendation_selected"],
        "selected_option": options["selected_option"],
    },
)

# Gate 13
route_a_definitions = options["options"][0]["current_rule_definitions"]
check(
    13,
    "no boundary parameter interval orientation or coupling function is defined",
    route_a_definitions["boundary_parameter"] is None
    and route_a_definitions["orientation"] is None
    and route_a_definitions["domain"] is None
    and route_a_definitions["endpoint_convention"] is None
    and route_a_definitions["per_lane_parameter_intervals"] == []
    and route_a_definitions["lane_to_boundary_function"] is None
    and route_a_definitions["angular_placement"] is None
    and route_a_definitions["arc_length_placement"] is None
    and all(
        options["definition_counts"][key] == 0
        for key in ["boundary_parameters", "parameter_intervals", "orientations", "coupling_functions"]
    ),
    {"definitions": route_a_definitions, "counts": options["definition_counts"]},
)

# Gate 14
sector = r3["sector_policy"]
check(
    14,
    "no seam join closure or 360-degree ownership is defined",
    all(
        sector[key] is False
        for key in [
            "front_left_front_right_join",
            "left_left_left_right_join",
            "front_left_view_join",
            "top_upright_join",
            "periodic_wrap",
            "closed_360_ownership",
        ]
    )
    and all(options["definition_counts"][key] == 0 for key in ["seams", "joins", "closures"]),
    {"sector_policy": sector, "definition_counts": options["definition_counts"]},
)

# Gate 15
zero_keys = [
    "physical_source_target_transforms",
    "physical_cross_view_pairs",
    "target_trace_coordinates",
    "field_samples",
    "fills",
    "surfaces",
    "topology",
    "geometry",
]
check(
    15,
    "every physical field fill surface topology and geometry count remains zero",
    all(r3["authority_counts"][key] == 0 for key in zero_keys)
    and all(options["definition_counts"][key] == 0 for key in zero_keys),
    {
        "r3": {key: r3["authority_counts"][key] for key in zero_keys},
        "r4": {key: options["definition_counts"][key] for key in zero_keys},
    },
)

# Gate 16
active_blocks = options["active_blocks"]
check(
    16,
    "all three blocks remain active with no resolved block",
    active_blocks
    == [
        {
            "id": "S10R-BLOCK-006",
            "status": "active_pending_separate_lane_boundary_coupling_rule_contract",
        },
        {"id": "S10R-BLOCK-008", "status": "active_unchanged"},
        {"id": "S10R-BLOCK-009", "status": "active_unchanged"},
    ]
    and options["resolved_block_ids"] == []
    and dependency["resolved_block_ids"] == [],
    {"active_blocks": active_blocks, "resolved_block_ids": options["resolved_block_ids"]},
)

# Gate 17
flags = options["authorization_flags"]
check(
    17,
    "only separate coupling-rule contract preparation is authorized",
    flags["coupling_rule_preparation_authorized"] is True
    and all(
        value is False
        for key, value in flags.items()
        if key != "coupling_rule_preparation_authorized"
    ),
    flags,
)

# Gate 18
git_lines = subprocess.run(
    ["git", "status", "--porcelain=v1", "-uall"],
    cwd=ROOT,
    check=True,
    text=True,
    capture_output=True,
).stdout.splitlines()
status_names = {path.name for path in STATUS_PATHS}
scoped_paths = {
    line[3:]
    for line in git_lines
    if len(line) >= 4
    and (
        "S10R_006_R4_A_LANE_BOUNDARY_COUPLING_AUTHORITY" in line[3:]
        or line[3:].endswith(
            "audit_bloodaxe_cairnstone_a005_s10r006_r4_a_lane_boundary_coupling_authority.py"
        )
        or Path(line[3:]).name in status_names
    )
}
status_markers = {
    A005 / "SM_GIA_BloodAxeCairnstone_A005_RESET_RESUME_STATE.md": [
        "S10R-006-R4-A Selection Closed",
        "Flamestrike selected `S10R-006-R4-A`",
    ],
    A005 / "SM_GIA_BloodAxeCairnstone_A005_APPROVAL_LOG.md": [
        "S10R-006-R4-A Coupling-Authority Option Selection",
        "Selected option: `S10R-006-R4-A`",
    ],
    A005 / "SM_GIA_BloodAxeCairnstone_A005_ARTIFACT_INDEX.md": [
        "S10R-006-R4-A Lane-Boundary Coupling Authority - Selected Route",
        "Flamestrike selected `S10R-006-R4-A`",
    ],
}
marker_evidence = {
    str(path.relative_to(ROOT)): {marker: marker in path.read_text(encoding="utf-8") for marker in markers}
    for path, markers in status_markers.items()
}
check(
    18,
    "changed paths match the execution allowlist",
    scoped_paths == EXPECTED_SCOPED_PATHS
    and all(all(result.values()) for result in marker_evidence.values()),
    {
        "scoped_paths": sorted(scoped_paths),
        "expected_paths": sorted(EXPECTED_SCOPED_PATHS),
        "status_markers": marker_evidence,
    },
)

# Gate 19
staged = subprocess.run(
    ["git", "diff", "--cached", "--name-only"],
    cwd=ROOT,
    check=True,
    text=True,
    capture_output=True,
).stdout.splitlines()
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

if [item["gate"] for item in checks] != list(range(1, 21)):
    raise RuntimeError("auditor gate numbering is not exactly 1..20")

failed = [item for item in checks if item["status"] == "fail"]
result = {
    "schema": "aerathea.s10r_006_r4_a_lane_boundary_coupling_authority_independent_audit.v1",
    "status": "pass" if not failed else "fail",
    "artifact_classification": "proof only",
    "gate_count": len(checks),
    "passed_gate_count": len(checks) - len(failed),
    "failed_gate_count": len(failed),
    "checks": checks,
}
print(json.dumps(result, indent=2))
sys.exit(0 if not failed else 1)
