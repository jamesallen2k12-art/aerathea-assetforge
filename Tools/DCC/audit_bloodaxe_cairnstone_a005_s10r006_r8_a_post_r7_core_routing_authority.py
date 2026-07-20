#!/usr/bin/env python3
"""Read-only independent audit for A005 S10R-006-R8-A routing records."""

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

CONTRACT = STEPS / "S10R_006_R8_A_POST_R7_CORE_ROUTING_AUTHORITY_DECISION_CONTRACT.md"
INPUT_LOCK = MANIFESTS / "S10R_006_R8_A_POST_R7_CORE_ROUTING_AUTHORITY_INPUT_LOCK.json"
DEPENDENCY = MANIFESTS / "S10R_006_R8_A_POST_R7_CORE_ROUTING_AUTHORITY_DEPENDENCY_AUDIT.json"
OPTIONS = MANIFESTS / "S10R_006_R8_A_POST_R7_CORE_ROUTING_AUTHORITY_OPTION_REGISTRY.json"
VALIDATION = MANIFESTS / "S10R_006_R8_A_POST_R7_CORE_ROUTING_AUTHORITY_VALIDATION.json"
R3 = MANIFESTS / "S10R_006_R3_A_ABSTRACT_FIELD_METHOD_A01_METHOD_REGISTRY.json"
R5 = MANIFESTS / "S10R_006_R5_A_LANE_BOUNDARY_COUPLING_RULE_A01_RULE_REGISTRY.json"
R7 = MANIFESTS / "S10R_006_R7_A_CROSS_VIEW_CORNER_OWNERSHIP_RULE_A01_RULE_REGISTRY.json"
OUTPUT = STEPS / "S10R_006_R8_A_POST_R7_CORE_ROUTING_AUTHORITY_DECISION_OUTPUT_RECORD.md"
HANDOFF = HANDOFFS / "S10R_006_R8_A_POST_R7_CORE_ROUTING_AUTHORITY_TO_DECISION_HANDOFF.md"


def sha256(path: Path) -> str:
    digest = hashlib.sha256()
    with path.open("rb") as handle:
        for chunk in iter(lambda: handle.read(1024 * 1024), b""):
            digest.update(chunk)
    return digest.hexdigest()


def load_json(path: Path) -> dict:
    with path.open("r", encoding="utf-8") as handle:
        return json.load(handle)


def git_status_records() -> list[tuple[bytes, str]]:
    raw = subprocess.check_output(
        ["git", "status", "--porcelain=v1", "-z", "--untracked-files=all"],
        cwd=ROOT,
    )
    parts = raw.split(b"\0")
    records: list[tuple[bytes, str]] = []
    index = 0
    while index < len(parts) and parts[index]:
        record = parts[index]
        status = record[:2].decode("utf-8")
        path = record[3:].decode("utf-8")
        records.append((record + b"\0", path))
        index += 1
        if status[0] in "RC" and index < len(parts):
            index += 1
    return records


required = [
    CONTRACT,
    INPUT_LOCK,
    DEPENDENCY,
    OPTIONS,
    VALIDATION,
    R3,
    R5,
    R7,
    OUTPUT,
    HANDOFF,
    Path(__file__).resolve(),
]
missing = [str(path.relative_to(ROOT)) for path in required if not path.is_file()]
if missing:
    print(
        json.dumps(
            {
                "schema": "aerathea.s10r_006_r8_a_post_r7_core_routing_authority_independent_audit.v1",
                "status": "fail_closed_missing_required_files",
                "missing_files": missing,
            },
            indent=2,
        )
    )
    sys.exit(1)

input_lock = load_json(INPUT_LOCK)
dependency = load_json(DEPENDENCY)
options = load_json(OPTIONS)
validation = load_json(VALIDATION)
r3 = load_json(R3)
r5 = load_json(R5)
r7 = load_json(R7)
output_text = OUTPUT.read_text(encoding="utf-8")
handoff_text = HANDOFF.read_text(encoding="utf-8")

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


# Gate 1: the ten immutable inputs remain byte-identical, while the three
# status records were exact at prewrite and may change only through their
# controlled result-record policy.
hash_results = []
for item in input_lock["locked_inputs"]:
    current = sha256(ROOT / item["path"])
    prewrite_match = (
        item["expected_sha256"] == item["actual_sha256"] and item["match"] is True
    )
    controlled = item["policy"].startswith("controlled ")
    valid = prewrite_match and (controlled or current == item["expected_sha256"])
    hash_results.append(
        {
            "path": item["path"],
            "prewrite_match": prewrite_match,
            "current_sha256": current,
            "controlled_status_update_after_prewrite": controlled
            and current != item["expected_sha256"],
            "valid": valid,
        }
    )
check(
    1,
    "all thirteen locked inputs match",
    len(hash_results) == 13 and all(item["valid"] for item in hash_results),
    hash_results,
)

# Gate 2
approval = input_lock["execution_approval"]
contract_hash = sha256(CONTRACT)
check(
    2,
    "contract hash and exact execution approval match",
    contract_hash == "41ed12c69fd911fe0fd789f4605fd3d577ef8f0beb15b3833a1a646983be4066"
    and approval["approver"] == "Flamestrike"
    and approval["statement"] == "approved"
    and approval["route_selection_granted"] is False,
    {"contract_sha256": contract_hash, "execution_approval": approval},
)

# Gate 3
check(
    3,
    "R3 symbolic method remains approved and unevaluated",
    r3["status"] == "approved_bounded_symbolic_method_no_field_coupling"
    and r3["artifact_classification"]
    == "authoritative for bounded S10R-006-R3-A symbolic method only"
    and r3["between_trace_operator"]["classification"]
    == "unevaluated symbolic record-weight descriptor"
    and r3["authority_counts"]["field_samples"] == 0
    and r3["authorization_flags"]["method_implementation_authorized"] is False,
    {"status": r3["status"], "authority_counts": r3["authority_counts"]},
)

# Gate 4
check(
    4,
    "R5 four-lane q/B_v/C_L rule remains approved and unevaluated",
    r5["status"] == "approved_bounded_symbolic_rule_four_blocked_corner_gaps_unowned"
    and len(r5["lanes"]) == 4
    and r5["coupling_descriptor"]["evaluated"] is False
    and r5["boundary_family"]["evaluated_samples"] == []
    and r5["authorization_flags"]["coupling_rule_approved"] is True
    and r5["authorization_flags"]["rule_evaluation_authorized"] is False,
    {"status": r5["status"], "lane_count": len(r5["lanes"])},
)

# Gate 5
check(
    5,
    "R7 four-gap owner-label rule remains approved and unevaluated",
    r7["status"]
    == "approved_bounded_cross_view_corner_ownership_rule_registered_no_implementation"
    and len(r7["gaps"]) == 4
    and r7["candidate_gap_rule"]["approved"] is True
    and r7["candidate_gap_rule"]["evaluated"] is False
    and all(item["owner_instances"] == [] for item in r7["gaps"])
    and r7["authorization_flags"]["rule_evaluation_authorized"] is False,
    {"status": r7["status"], "gap_count": len(r7["gaps"])},
)

# Gate 6
expected_lanes = [
    ("AFM-FRONT-RIGHT", "+X", "[-1/2,1/2]"),
    ("AFM-LEFT-LEFT", "+Y", "[3/2,5/2]"),
    ("AFM-FRONT-LEFT", "-X", "[7/2,9/2]"),
    ("AFM-LEFT-RIGHT", "-Y", "[11/2,13/2]"),
]
expected_gaps = [
    ("G_0", "(1/2,3/2)"),
    ("G_1", "(5/2,7/2)"),
    ("G_2", "(9/2,11/2)"),
    ("G_3", "(13/2,15/2)"),
]
r5_lanes = [
    (item["lane_id"], item["cardinal_center"], item["q_interval"])
    for item in r5["lanes"]
]
r7_lanes = [
    (item["lane_id"], item["cardinal_label"], item["q_interval"])
    for item in r7["preserved_owned_lanes"]
]
audit_lanes = [
    (item["lane_id"], item["cardinal_label"], item["q_interval"])
    for item in dependency["exact_interval_replay"]["r5_owned_lanes"]
]
r5_gaps = [(item["id"], item["q_interval"]) for item in r5["blocked_gaps"]]
r7_gaps = [(item["id"], item["open_interval"]) for item in r7["gaps"]]
audit_gaps = [
    (item["gap_id"], item["q_interval"])
    for item in dependency["exact_interval_replay"]["r7_symbolic_gaps"]
]
check(
    6,
    "R5 lane intervals and R7 gap intervals replay exactly",
    expected_lanes == r5_lanes == r7_lanes == audit_lanes
    and expected_gaps == r5_gaps == r7_gaps == audit_gaps,
    {"lanes": audit_lanes, "gaps": audit_gaps},
)

# Gate 7
endpoint_policy = "each lane owns both endpoints of its own closed interval; open gaps are unowned"
tie_policy = "single successor owner label at the exact symbolic midpoint"
check(
    7,
    "R5 endpoint ownership and R7 successor-at-tie policy remain unchanged",
    r5["abstract_parameter"]["endpoint_convention"] == endpoint_policy
    and dependency["exact_interval_replay"]["r5_endpoint_policy"] == endpoint_policy
    and r7["candidate_gap_rule"]["tie_policy"] == tie_policy
    and dependency["exact_interval_replay"]["r7_tie_policy"] == tie_policy
    and r7["endpoint_policy"]["existing_r5_lane_endpoints_mutated"] is False,
    {"endpoint_policy": endpoint_policy, "tie_policy": tie_policy},
)

# Gate 8
r5_q = r5["abstract_parameter"]
r7_q = r7["abstract_parameter_reference"]
check(
    8,
    "q remains non-periodic and unwrapped",
    r5_q["periodic"] is False
    and r5_q["modulus"] is None
    and r5_q["wrap"] is None
    and r5_q["final_first_endpoint_identification"] is False
    and r7_q["periodic"] is False
    and r7_q["unwrapped"] is True
    and r7_q["wrap"] is None
    and r7_q["final_first_endpoint_identification"] is False
    and dependency["exact_interval_replay"]["q_periodic"] is False
    and dependency["exact_interval_replay"]["q_unwrapped"] is True,
    {"r5_q": r5_q, "r7_q": r7_q},
)

# Gate 9
holdouts = [r3["holdouts"], r5["holdouts"], r7["holdouts"], dependency["holdouts"]]
check(
    9,
    "all fourteen back/right records remain proof only",
    all(
        item["classification"] == "proof only"
        and item["back_count"] == 6
        and item["right_count"] == 8
        and item["total"] == 14
        and item["construction_use_authorized"] is False
        for item in holdouts
    ),
    holdouts,
)

# Gate 10
expected_routes = ["S10R-006-R8-A", "S10R-006-R8-B", "S10R-006-R8-BLOCK"]
actual_routes = [item["id"] for item in options["options"]]
check(
    10,
    "exactly R8-A R8-B and R8-BLOCK are registered",
    actual_routes == expected_routes
    and dependency["candidate_route_separation"]["required_route_ids"] == expected_routes
    and dependency["candidate_route_separation"]["candidate_route_count"] == 3,
    actual_routes,
)

# Gate 11
selection = options["selection_record"]
check(
    11,
    "selected route count remains zero",
    all(item["selected"] is False for item in options["options"])
    and selection["selected_option"] is None
    and selection["selected_option_count"] == 0
    and dependency["candidate_route_separation"]["selected_route_count"] == 0
    and dependency["candidate_route_separation"]["selected_route"] is None,
    selection,
)

# Gate 12
recommendation = options["recommendation"]
check(
    12,
    "R8-A is recommendation only",
    recommendation["option_id"] == "S10R-006-R8-A"
    and recommendation["classification"] == "candidate interpretation only"
    and recommendation["selected"] is False
    and recommendation["authority"] is False
    and dependency["recommendation"]["route_id"] == "S10R-006-R8-A"
    and dependency["recommendation"]["selected"] is False
    and selection["recommendation_is_selection"] is False
    and selection["recommendation_is_authority"] is False,
    recommendation,
)

# Gate 13
definition_counts = [dependency["definition_counts"], options["definition_counts"]]
check(
    13,
    "no coupling or join rule is prepared or approved",
    all(
        item["prepared_coupling_rules"] == 0
        and item["approved_coupling_rules"] == 0
        and item["prepared_join_rules"] == 0
        and item["approved_join_rules"] == 0
        for item in definition_counts
    )
    and all(item["rule_prepared"] is False and item["rule_approved"] is False for item in options["options"]),
    definition_counts,
)

# Gates 14 and 15
instance_keys = [
    "q_instances",
    "u_instances",
    "owner_instances",
    "record_instances",
    "samples",
    "coordinates",
    "transforms",
    "physical_pairs",
    "centers",
    "pivots",
    "anchors",
]
structure_keys = ["seams", "joins", "closures", "fields", "fills", "surfaces", "topology", "geometry"]
count_sources = [dependency["output_counts"], options["output_counts"]]
check(
    14,
    "q u owner and record instances samples coordinates transforms pairs centers pivots and anchors remain zero",
    all(source[key] == 0 for source in count_sources for key in instance_keys),
    {key: [source[key] for source in count_sources] for key in instance_keys},
)
check(
    15,
    "seams joins closures fields fills surfaces topology and geometry remain zero",
    all(source[key] == 0 for source in count_sources for key in structure_keys),
    {key: [source[key] for source in count_sources] for key in structure_keys},
)

# Gate 16
expected_blocks = [
    (
        "S10R-BLOCK-006",
        "active_approved_cross_view_corner_ownership_rule_no_field_no_seam_no_join_no_closure",
    ),
    ("S10R-BLOCK-008", "active_unchanged"),
    ("S10R-BLOCK-009", "active_unchanged"),
]
dependency_blocks = [(item["id"], item["status"]) for item in dependency["active_blocks"]]
option_blocks = [(item["id"], item["status"]) for item in options["active_blocks"]]
r7_blocks = [(item["id"], item["status"]) for item in r7["active_blocks"]]
check(
    16,
    "all three blocks remain active and resolved block IDs remain empty",
    dependency_blocks == expected_blocks == option_blocks == r7_blocks
    and dependency["resolved_block_ids"] == []
    and options["resolved_block_ids"] == []
    and r7["resolved_block_ids"] == [],
    {"blocks": dependency_blocks, "resolved_block_ids": dependency["resolved_block_ids"]},
)

# Gate 17
flag_sets = [dependency["authorization_flags"], options["authorization_flags"]]
flags_valid = all(flags["candidate_decision_surface_registered"] is True for flags in flag_sets)
flags_valid = flags_valid and all(
    value is False
    for flags in flag_sets
    for key, value in flags.items()
    if key != "candidate_decision_surface_registered"
)
check(
    17,
    "evaluation implementation downstream and Git flags remain false",
    flags_valid,
    flag_sets,
)

# Gate 18: preserve the exact unrelated pre-existing worktree fingerprint and
# require the complete execution path set with zero staged paths.
allowlist = set(input_lock["execution_allowlist"])
records = git_status_records()
outside_records = [record for record, path in records if path not in allowlist]
outside_paths = [path for _, path in records if path not in allowlist]
scoped_paths = {path for _, path in records if path in allowlist}
outside_digest = hashlib.sha256(b"".join(outside_records)).hexdigest()
staged_raw = subprocess.check_output(
    ["git", "diff", "--cached", "--name-only", "-z"], cwd=ROOT
)
staged_paths = [item.decode("utf-8") for item in staged_raw.split(b"\0") if item]
expected_r8_docs = {
    str(path.relative_to(ROOT))
    for directory in (MANIFESTS, STEPS, HANDOFFS)
    for path in directory.glob("*S10R_006_R8_A_POST_R7_CORE_ROUTING_AUTHORITY*")
}
allowed_r8_docs = {
    path
    for path in allowlist
    if "S10R_006_R8_A_POST_R7_CORE_ROUTING_AUTHORITY" in path
}
branch = subprocess.check_output(["git", "branch", "--show-current"], cwd=ROOT, text=True).strip()
head = subprocess.check_output(["git", "rev-parse", "HEAD"], cwd=ROOT, text=True).strip()
scope_ok = (
    len(outside_records)
    == input_lock["git_preexecution"]["outside_execution_allowlist_record_count"]
    and outside_digest
    == input_lock["git_preexecution"]["outside_execution_allowlist_porcelain_v1_z_sha256"]
    and scoped_paths == allowlist
    and expected_r8_docs == allowed_r8_docs
    and staged_paths == []
    and branch == input_lock["branch"]
    and head == input_lock["head"]
)
check(
    18,
    "changed paths match the execution allowlist and no path is staged",
    scope_ok,
    {
        "outside_allowlist_record_count": len(outside_records),
        "outside_allowlist_sha256": outside_digest,
        "outside_path_sample": outside_paths[:5],
        "scoped_paths": sorted(scoped_paths),
        "r8_docs": sorted(expected_r8_docs),
        "staged_paths": staged_paths,
        "branch": branch,
        "head": head,
    },
)

# Gate 19
try:
    window_titles = subprocess.check_output(["wmctrl", "-l"], text=True)
except (FileNotFoundError, subprocess.CalledProcessError):
    window_titles = ""
output_title = "A005_R8_ROUTING_OUTPUT_REVIEW"
handoff_title = "A005_R8_ROUTING_HANDOFF_REVIEW"
visibility = validation["visible_review"]
visible_ok = (
    visibility["verified"] is True
    and visibility["output_record_visible"] is True
    and visibility["decision_handoff_visible"] is True
    and visibility["output_review_window"] == output_title
    and visibility["handoff_review_window"] == handoff_title
    and visibility["modified_output_editor_buffer_used_as_authority"] is False
    and output_title in window_titles
    and handoff_title in window_titles
    and "candidate_post_R7_core_routing_decision_surface_ready_for_Flamestrike" in output_text
    and "candidate_post_R7_core_routing_decision_surface_ready_for_Flamestrike" in handoff_text
    and all(route in output_text and route in handoff_text for route in expected_routes)
)
check(
    19,
    "output and handoff visibility are verified before the mandatory stop",
    visible_ok,
    {
        "validation_visibility": visibility,
        "output_title_found": output_title in window_titles,
        "handoff_title_found": handoff_title in window_titles,
    },
)

failed = [item for item in checks if item["status"] != "pass"]
result = {
    "schema": "aerathea.s10r_006_r8_a_post_r7_core_routing_authority_independent_audit.v1",
    "status": "pass_19_of_19" if not failed else "fail_closed",
    "technical_result": (
        "candidate_post_R7_core_routing_decision_surface_ready_for_Flamestrike"
        if not failed
        else "blocked_post_R7_routing_authority_dependency_or_scope_failure"
    ),
    "gate_count": len(checks),
    "passed_gate_count": len(checks) - len(failed),
    "failed_gate_count": len(failed),
    "checks": checks,
}
print(json.dumps(result, indent=2))
sys.exit(0 if not failed else 1)
