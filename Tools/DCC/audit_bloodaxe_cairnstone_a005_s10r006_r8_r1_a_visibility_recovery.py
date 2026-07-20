#!/usr/bin/env python3
"""Read-only first-and-only complete audit for A005 R8-R1 recovery."""

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

CONTRACT = STEPS / "S10R_006_R8_R1_A_VISIBILITY_RECOVERY_CONTRACT.md"
INPUT_LOCK = MANIFESTS / "S10R_006_R8_R1_A_VISIBILITY_RECOVERY_INPUT_LOCK.json"
EQUIVALENCE = MANIFESTS / "S10R_006_R8_R1_A_VISIBILITY_RECOVERY_CONTENT_EQUIVALENCE_AUDIT.json"
OPTIONS = MANIFESTS / "S10R_006_R8_R1_A_VISIBILITY_RECOVERY_OPTION_REGISTRY.json"
VALIDATION = MANIFESTS / "S10R_006_R8_R1_A_VISIBILITY_RECOVERY_VALIDATION.json"
OUTPUT = STEPS / "S10R_006_R8_R1_A_VISIBILITY_RECOVERY_DECISION_OUTPUT_RECORD.md"
HANDOFF = HANDOFFS / "S10R_006_R8_R1_A_VISIBILITY_RECOVERY_TO_DECISION_HANDOFF.md"

ORIGINAL_CONTRACT = STEPS / "S10R_006_R8_A_POST_R7_CORE_ROUTING_AUTHORITY_DECISION_CONTRACT.md"
ORIGINAL_INPUT = MANIFESTS / "S10R_006_R8_A_POST_R7_CORE_ROUTING_AUTHORITY_INPUT_LOCK.json"
ORIGINAL_DEPENDENCY = MANIFESTS / "S10R_006_R8_A_POST_R7_CORE_ROUTING_AUTHORITY_DEPENDENCY_AUDIT.json"
ORIGINAL_OPTIONS = MANIFESTS / "S10R_006_R8_A_POST_R7_CORE_ROUTING_AUTHORITY_OPTION_REGISTRY.json"
ORIGINAL_VALIDATION = MANIFESTS / "S10R_006_R8_A_POST_R7_CORE_ROUTING_AUTHORITY_VALIDATION.json"
ORIGINAL_OUTPUT = STEPS / "S10R_006_R8_A_POST_R7_CORE_ROUTING_AUTHORITY_DECISION_OUTPUT_RECORD.md"
ORIGINAL_HANDOFF = HANDOFFS / "S10R_006_R8_A_POST_R7_CORE_ROUTING_AUTHORITY_TO_DECISION_HANDOFF.md"
ORIGINAL_AUDITOR = ROOT / "Tools/DCC/audit_bloodaxe_cairnstone_a005_s10r006_r8_a_post_r7_core_routing_authority.py"

R3 = MANIFESTS / "S10R_006_R3_A_ABSTRACT_FIELD_METHOD_A01_METHOD_REGISTRY.json"
R5 = MANIFESTS / "S10R_006_R5_A_LANE_BOUNDARY_COUPLING_RULE_A01_RULE_REGISTRY.json"
R7 = MANIFESTS / "S10R_006_R7_A_CROSS_VIEW_CORNER_OWNERSHIP_RULE_A01_RULE_REGISTRY.json"

OUTPUT_TITLE = "A005_R8_R1_OUTPUT_REVIEW"
HANDOFF_TITLE = "A005_R8_R1_HANDOFF_REVIEW"


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


def desktop_sample() -> dict:
    try:
        result = subprocess.run(
            ["wmctrl", "-l"],
            check=False,
            text=True,
            stdout=subprocess.PIPE,
            stderr=subprocess.PIPE,
        )
        titles = result.stdout
        return {
            "return_code": result.returncode,
            "output_title_found": OUTPUT_TITLE in titles,
            "handoff_title_found": HANDOFF_TITLE in titles,
            "stderr": result.stderr.strip(),
        }
    except FileNotFoundError as exc:
        return {
            "return_code": 127,
            "output_title_found": False,
            "handoff_title_found": False,
            "stderr": str(exc),
        }


required = [
    CONTRACT,
    INPUT_LOCK,
    EQUIVALENCE,
    OPTIONS,
    VALIDATION,
    OUTPUT,
    HANDOFF,
    ORIGINAL_CONTRACT,
    ORIGINAL_INPUT,
    ORIGINAL_DEPENDENCY,
    ORIGINAL_OPTIONS,
    ORIGINAL_VALIDATION,
    ORIGINAL_OUTPUT,
    ORIGINAL_HANDOFF,
    ORIGINAL_AUDITOR,
    R3,
    R5,
    R7,
    Path(__file__).resolve(),
]
missing = [str(path.relative_to(ROOT)) for path in required if not path.is_file()]
if missing:
    print(json.dumps({
        "schema": "aerathea.s10r_006_r8_r1_a_visibility_recovery_independent_audit.v1",
        "status": "fail_closed_missing_required_files",
        "missing_files": missing,
    }, indent=2))
    sys.exit(1)

input_lock = load_json(INPUT_LOCK)
equivalence = load_json(EQUIVALENCE)
options = load_json(OPTIONS)
validation = load_json(VALIDATION)
original_input = load_json(ORIGINAL_INPUT)
original_dependency = load_json(ORIGINAL_DEPENDENCY)
original_options = load_json(ORIGINAL_OPTIONS)
original_validation = load_json(ORIGINAL_VALIDATION)
r3 = load_json(R3)
r5 = load_json(R5)
r7 = load_json(R7)
source_contract_text = ORIGINAL_CONTRACT.read_text(encoding="utf-8")
output_text = OUTPUT.read_text(encoding="utf-8")
handoff_text = HANDOFF.read_text(encoding="utf-8")

checks: list[dict] = []


def check(gate: int, subject: str, condition: bool, evidence: object) -> None:
    checks.append({
        "gate": gate,
        "subject": subject,
        "status": "pass" if condition else "fail",
        "evidence": evidence,
    })


# Gate 1
hash_results = []
for item in input_lock["locked_inputs"]:
    current = sha256(ROOT / item["path"])
    prewrite_match = item["expected_sha256"] == item["actual_sha256"] and item["match"] is True
    controlled = item["policy"].startswith("controlled ")
    valid = prewrite_match and (controlled or current == item["expected_sha256"])
    hash_results.append({
        "path": item["path"],
        "prewrite_match": prewrite_match,
        "current_sha256": current,
        "controlled_status_update_after_prewrite": controlled and current != item["expected_sha256"],
        "valid": valid,
    })
check(1, "every locked preparation input matches", len(hash_results) == 16 and all(item["valid"] for item in hash_results), hash_results)

# Gate 2
approval = input_lock["execution_approval"]
contract_hash = sha256(CONTRACT)
check(
    2,
    "recovery contract hash and exact execution approval match",
    contract_hash == "4226f1b9230172db104f8839b246cefd6d848adc12bf1466d318303892d20319"
    and approval["approver"] == "Flamestrike"
    and approval["statement"] == "approved"
    and approval["route_selection_granted"] is False
    and approval["coupling_or_join_contract_authority_granted"] is False,
    {"contract_sha256": contract_hash, "approval": approval},
)

# Gate 3
original_contract_hash = sha256(ORIGINAL_CONTRACT)
check(3, "original R8 contract remains byte-identical", original_contract_hash == "41ed12c69fd911fe0fd789f4605fd3d577ef8f0beb15b3833a1a646983be4066", original_contract_hash)

# Gate 4
quarantine_paths = {
    ORIGINAL_INPUT: "648ce499b48223bf451b04b535ff0146135b718f204dcd13f3582c53139610bb",
    ORIGINAL_DEPENDENCY: "1a0768fda05ac21a6b4293b6626f3a7036c557a6457193e6370dad70779efc97",
    ORIGINAL_OPTIONS: "ab1d0e2a49bb26e074b4f3758a59088d8994c71cf53628f451653c859b599c11",
    ORIGINAL_VALIDATION: "827ded5cfb1d6e96d0a2bc03e8e5be8564dd53bd11ae0cf1772e39c1e42397b8",
    ORIGINAL_OUTPUT: "20682d2a8788b98b0ffc81b98b0894ce672977dda00b259b0fd2b76ec82e0129",
    ORIGINAL_HANDOFF: "96e635dfc13c6864eb1d7f67a4805e837cb103b70597314e784fb134ab8912a5",
    ORIGINAL_AUDITOR: "29928c8ff0ea31529e9421b92f0122e0c62ca37a33b72cd92bb3f37bd1b161cd",
}
quarantine_hashes = {str(path.relative_to(ROOT)): sha256(path) for path in quarantine_paths}
quarantine_ok = all(quarantine_hashes[str(path.relative_to(ROOT))] == expected for path, expected in quarantine_paths.items())
quarantine_ok = quarantine_ok and original_options["artifact_classification"] == "quarantined"
quarantine_ok = quarantine_ok and original_options["authorization_flags"]["candidate_decision_surface_registered"] is False
quarantine_ok = quarantine_ok and original_validation["failure_record"]["candidate_surface_registered"] is False
quarantine_ok = quarantine_ok and original_dependency["execution_failure"]["candidate_surface_registered"] is False
check(4, "every quarantined R8 failure record remains byte-identical and quarantined", quarantine_ok, quarantine_hashes)

# Gate 5
r3_ok = r3["status"] == "approved_bounded_symbolic_method_no_field_coupling" and r3["authorization_flags"]["method_implementation_authorized"] is False
r5_ok = r5["status"] == "approved_bounded_symbolic_rule_four_blocked_corner_gaps_unowned" and r5["coupling_descriptor"]["evaluated"] is False and r5["authorization_flags"]["rule_evaluation_authorized"] is False
r7_ok = r7["status"] == "approved_bounded_cross_view_corner_ownership_rule_registered_no_implementation" and r7["candidate_gap_rule"]["evaluated"] is False and r7["authorization_flags"]["rule_evaluation_authorized"] is False
check(5, "R3 R5 and R7 remain approved bounded and unevaluated", r3_ok and r5_ok and r7_ok, {"r3": r3["status"], "r5": r5["status"], "r7": r7["status"]})

# Gate 6
expected_lanes = [
    ("AFM-FRONT-RIGHT", "+X", "[-1/2,1/2]"),
    ("AFM-LEFT-LEFT", "+Y", "[3/2,5/2]"),
    ("AFM-FRONT-LEFT", "-X", "[7/2,9/2]"),
    ("AFM-LEFT-RIGHT", "-Y", "[11/2,13/2]"),
]
expected_gaps = [("G_0", "(1/2,3/2)"), ("G_1", "(5/2,7/2)"), ("G_2", "(9/2,11/2)"), ("G_3", "(13/2,15/2)")]
r5_lanes = [(item["lane_id"], item["cardinal_center"], item["q_interval"]) for item in r5["lanes"]]
r7_lanes = [(item["lane_id"], item["cardinal_label"], item["q_interval"]) for item in r7["preserved_owned_lanes"]]
r5_gaps = [(item["id"], item["q_interval"]) for item in r5["blocked_gaps"]]
r7_gaps = [(item["id"], item["open_interval"]) for item in r7["gaps"]]
check(6, "four R5 lane intervals and four R7 gap intervals replay exactly", expected_lanes == r5_lanes == r7_lanes and expected_gaps == r5_gaps == r7_gaps, {"lanes": r5_lanes, "gaps": r7_gaps})

# Gate 7
endpoint_policy = "each lane owns both endpoints of its own closed interval; open gaps are unowned"
tie_policy = "single successor owner label at the exact symbolic midpoint"
check(7, "R5 endpoint ownership and R7 successor-at-tie policy remain unchanged", r5["abstract_parameter"]["endpoint_convention"] == endpoint_policy and r7["candidate_gap_rule"]["tie_policy"] == tie_policy and r7["endpoint_policy"]["existing_r5_lane_endpoints_mutated"] is False, {"endpoint_policy": endpoint_policy, "tie_policy": tie_policy})

# Gate 8
r5_q = r5["abstract_parameter"]
r7_q = r7["abstract_parameter_reference"]
check(8, "q remains non-periodic and unwrapped", r5_q["periodic"] is False and r5_q["wrap"] is None and r5_q["final_first_endpoint_identification"] is False and r7_q["periodic"] is False and r7_q["unwrapped"] is True and r7_q["wrap"] is None, {"r5_q": r5_q, "r7_q": r7_q})

# Gate 9
holdouts = [r3["holdouts"], r5["holdouts"], r7["holdouts"]]
check(9, "all fourteen back/right records remain proof only", all(item["classification"] == "proof only" and item["total"] == 14 and item["construction_use_authorized"] is False for item in holdouts), holdouts)

# Gate 10
expected_routes = [
    ("S10R-006-R8-A", "later preparation only of one separate bounded corner-gap-to-field coupling rule contract"),
    ("S10R-006-R8-B", "later preparation only of one separate bounded top/upright join rule contract"),
    ("S10R-006-R8-BLOCK", "preserve the current approved symbolic records and no-field block"),
]
actual_routes = [(item["id"], item["candidate_result"]) for item in options["options"]]
source_has_routes = all(route_id in source_contract_text and wording in source_contract_text for route_id, wording in expected_routes)
check(10, "fresh registry contains exactly R8-A R8-B and R8-BLOCK with exact wording", actual_routes == expected_routes and source_has_routes, actual_routes)

# Gate 11
selection = options["selection_record"]
check(11, "selected route count remains zero and selected route remains null", all(item["selected"] is False for item in options["options"]) and selection["selected_option"] is None and selection["selected_option_count"] == 0, selection)

# Gate 12
recommendation = options["recommendation"]
check(12, "R8-A remains candidate recommendation only", recommendation["option_id"] == "S10R-006-R8-A" and recommendation["classification"] == "candidate interpretation only" and recommendation["selected"] is False and recommendation["authority"] is False and selection["recommendation_is_selection"] is False and selection["recommendation_is_authority"] is False, recommendation)

# Gate 13
counts = options["definition_counts"]
check(13, "no coupling or join rule is prepared or approved", counts["prepared_coupling_rules"] == 0 and counts["approved_coupling_rules"] == 0 and counts["prepared_join_rules"] == 0 and counts["approved_join_rules"] == 0 and all(item["rule_prepared"] is False and item["rule_approved"] is False for item in options["options"]), counts)

# Gates 14 and 15
instance_keys = ["q_instances", "u_instances", "owner_instances", "record_instances", "samples", "coordinates", "transforms", "physical_pairs", "centers", "pivots", "anchors"]
structure_keys = ["seams", "joins", "closures", "fields", "fills", "surfaces", "topology", "geometry"]
output_counts = options["output_counts"]
check(14, "instances samples coordinates transforms pairs centers pivots and anchors remain zero", all(output_counts[key] == 0 for key in instance_keys), {key: output_counts[key] for key in instance_keys})
check(15, "seams joins closures fields fills surfaces topology and geometry remain zero", all(output_counts[key] == 0 for key in structure_keys), {key: output_counts[key] for key in structure_keys})

# Gate 16
expected_blocks = [
    ("S10R-BLOCK-006", "active_approved_cross_view_corner_ownership_rule_no_field_no_seam_no_join_no_closure"),
    ("S10R-BLOCK-008", "active_unchanged"),
    ("S10R-BLOCK-009", "active_unchanged"),
]
actual_blocks = [(item["id"], item["status"]) for item in options["active_blocks"]]
check(16, "all three blocks remain active and resolved block IDs remain empty", actual_blocks == expected_blocks and options["resolved_block_ids"] == [], {"blocks": actual_blocks, "resolved": options["resolved_block_ids"]})

# Gate 17
flags = options["authorization_flags"]
flags_ok = flags["candidate_decision_surface_registered"] is True and all(value is False for key, value in flags.items() if key != "candidate_decision_surface_registered")
check(17, "evaluation implementation downstream and Git flags remain false", flags_ok, flags)

# Gate 18
equivalent_routes = [(item["id"], item["candidate_result"]) for item in equivalence["exact_routes"]]
equivalence_ok = equivalence["status"] == "pass_exact_route_and_authority_boundary_equivalence" and equivalence["summary"]["passed_check_count"] == 8 and equivalence["summary"]["failed_check_count"] == 0 and equivalence["forbidden_differences_detected"] == [] and equivalent_routes == expected_routes
check(18, "fresh package is content-equivalent with only allowed recovery differences", equivalence_ok, equivalence)

# Gate 19
allowlist = set(input_lock["execution_allowlist"])
records = git_status_records()
outside_records = [record for record, path in records if path not in allowlist]
scoped_paths = {path for _, path in records if path in allowlist}
outside_digest = hashlib.sha256(b"".join(outside_records)).hexdigest()
staged_raw = subprocess.check_output(["git", "diff", "--cached", "--name-only", "-z"], cwd=ROOT)
staged_paths = [item.decode("utf-8") for item in staged_raw.split(b"\0") if item]
expected_docs = {str(path.relative_to(ROOT)) for directory in (MANIFESTS, STEPS, HANDOFFS) for path in directory.glob("*S10R_006_R8_R1_A_VISIBILITY_RECOVERY*")}
allowed_docs = {path for path in allowlist if "S10R_006_R8_R1_A_VISIBILITY_RECOVERY" in path}
branch = subprocess.check_output(["git", "branch", "--show-current"], cwd=ROOT, text=True).strip()
head = subprocess.check_output(["git", "rev-parse", "HEAD"], cwd=ROOT, text=True).strip()
scope_ok = len(outside_records) == input_lock["git_preexecution"]["outside_execution_allowlist_record_count"] and outside_digest == input_lock["git_preexecution"]["outside_execution_allowlist_porcelain_v1_z_sha256"] and scoped_paths == allowlist and expected_docs == allowed_docs and staged_paths == [] and branch == input_lock["branch"] and head == input_lock["head"]
check(19, "changed paths match recovery allowlist and no path is staged", scope_ok, {"outside_count": len(outside_records), "outside_sha256": outside_digest, "scoped_paths": sorted(scoped_paths), "expected_docs": sorted(expected_docs), "staged_paths": staged_paths, "branch": branch, "head": head})

# Gate 20: first live desktop sample.
preflight = desktop_sample()
visibility = validation["visible_review"]
preflight_ok = preflight["return_code"] == 0 and preflight["output_title_found"] and preflight["handoff_title_found"] and visibility["preflight_verified"] is True and visibility["output_record_visible"] is True and visibility["decision_handoff_visible"] is True and visibility["wmctrl_return_code"] == 0
check(20, "desktop preflight succeeds with both exact persistent titles", preflight_ok, {"live_sample": preflight, "validation_record": visibility})

# Gate 21: this invocation is admitted only while the validation record still
# proves no previous complete R8-R1 auditor run occurred.
audit_record = validation["independent_audit"]
first_only_ok = audit_record["complete_run_count_before_this_audit"] == 0 and audit_record["status"] == "not_yet_run" and audit_record["expected_gate_count"] == 22
check(21, "first and only complete independent audit passes every gate in one run", first_only_ok, audit_record)

# Gate 22: final live desktop sample after every substantive audit check.
final_sample = desktop_sample()
final_ok = final_sample["return_code"] == 0 and final_sample["output_title_found"] and final_sample["handoff_title_found"] and "candidate_post_R7_core_routing_decision_surface_recovered_and_ready_for_Flamestrike" in output_text and "candidate_post_R7_core_routing_decision_surface_recovered_and_ready_for_Flamestrike" in handoff_text and all(route_id in output_text and route_id in handoff_text for route_id, _ in expected_routes)
check(22, "final desktop sample again finds both exact titles", final_ok, final_sample)

failed = [item for item in checks if item["status"] != "pass"]
result = {
    "schema": "aerathea.s10r_006_r8_r1_a_visibility_recovery_independent_audit.v1",
    "status": "pass_22_of_22_first_and_only_complete_run" if not failed else "fail_closed_first_complete_run",
    "technical_result": "candidate_post_R7_core_routing_decision_surface_recovered_and_ready_for_Flamestrike" if not failed else "blocked_R8_visibility_recovery_dependency_or_liveness_failure",
    "complete_run_ordinal": 1,
    "gate_count": len(checks),
    "passed_gate_count": len(checks) - len(failed),
    "failed_gate_count": len(failed),
    "checks": checks,
}
print(json.dumps(result, indent=2))
sys.exit(0 if not failed else 1)
