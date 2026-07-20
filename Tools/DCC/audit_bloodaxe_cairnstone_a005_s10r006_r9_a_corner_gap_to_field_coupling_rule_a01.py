#!/usr/bin/env python3
"""Read-only first complete audit for A005 R9 corner-gap coupling rule."""

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

CONTRACT = STEPS / "S10R_006_R9_A_CORNER_GAP_TO_FIELD_COUPLING_RULE_A01_CONTRACT.md"
INPUT_LOCK = MANIFESTS / "S10R_006_R9_A_CORNER_GAP_TO_FIELD_COUPLING_RULE_A01_INPUT_LOCK.json"
REGISTRY = MANIFESTS / "S10R_006_R9_A_CORNER_GAP_TO_FIELD_COUPLING_RULE_A01_RULE_REGISTRY.json"
VALIDATION = MANIFESTS / "S10R_006_R9_A_CORNER_GAP_TO_FIELD_COUPLING_RULE_A01_VALIDATION.json"
OUTPUT = STEPS / "S10R_006_R9_A_CORNER_GAP_TO_FIELD_COUPLING_RULE_A01_OUTPUT_RECORD.md"
HANDOFF = HANDOFFS / "S10R_006_R9_A_CORNER_GAP_TO_FIELD_COUPLING_RULE_A01_TO_DECISION_HANDOFF.md"

R3 = MANIFESTS / "S10R_006_R3_A_ABSTRACT_FIELD_METHOD_A01_METHOD_REGISTRY.json"
R5 = MANIFESTS / "S10R_006_R5_A_LANE_BOUNDARY_COUPLING_RULE_A01_RULE_REGISTRY.json"
R7 = MANIFESTS / "S10R_006_R7_A_CROSS_VIEW_CORNER_OWNERSHIP_RULE_A01_RULE_REGISTRY.json"
R8 = MANIFESTS / "S10R_006_R8_R2_A_GATE10_WORDING_CORRECTION_OPTION_REGISTRY.json"
R8_VALIDATION = MANIFESTS / "S10R_006_R8_R2_A_GATE10_WORDING_CORRECTION_VALIDATION.json"

OUTPUT_TITLE = "A005_R9_CGFC_RULE_OUTPUT_REVIEW"
HANDOFF_TITLE = "A005_R9_CGFC_RULE_HANDOFF_REVIEW"
PASS_RESULT = "pass_candidate_bounded_corner_gap_to_field_coupling_rule_registered_no_implementation"
BLOCK_RESULT = "blocked_corner_gap_to_field_coupling_rule_dependency_or_scope_failure"


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
        return {
            "return_code": result.returncode,
            "output_title_found": OUTPUT_TITLE in result.stdout,
            "handoff_title_found": HANDOFF_TITLE in result.stdout,
            "stderr": result.stderr.strip(),
        }
    except FileNotFoundError as exc:
        return {"return_code":127,"output_title_found":False,"handoff_title_found":False,"stderr":str(exc)}


required = [CONTRACT,INPUT_LOCK,REGISTRY,VALIDATION,OUTPUT,HANDOFF,R3,R5,R7,R8,R8_VALIDATION,Path(__file__).resolve()]
missing = [str(path.relative_to(ROOT)) for path in required if not path.is_file()]
if missing:
    print(json.dumps({
        "schema":"aerathea.s10r_006_r9_a_corner_gap_to_field_coupling_rule_a01_independent_audit.v1",
        "status":"fail_closed_missing_required_files",
        "missing_files":missing,
    },indent=2))
    sys.exit(1)

input_lock = load_json(INPUT_LOCK)
registry = load_json(REGISTRY)
validation = load_json(VALIDATION)
r3 = load_json(R3)
r5 = load_json(R5)
r7 = load_json(R7)
r8 = load_json(R8)
r8_validation = load_json(R8_VALIDATION)
output_text = OUTPUT.read_text(encoding="utf-8")
handoff_text = HANDOFF.read_text(encoding="utf-8")

checks: list[dict] = []


def check(gate: int, subject: str, condition: bool, evidence: object) -> None:
    checks.append({"gate":gate,"subject":subject,"status":"pass" if condition else "fail","evidence":evidence})


# Gate 1
hash_results = []
for item in input_lock["locked_inputs"]:
    current = sha256(ROOT / item["path"])
    prewrite_match = item["expected_sha256"] == item["actual_sha256"] and item["match"] is True
    controlled = item["policy"].startswith("controlled ")
    valid = prewrite_match and (controlled or current == item["expected_sha256"])
    hash_results.append({"path":item["path"],"prewrite_match":prewrite_match,"current_sha256":current,"controlled_status_update_after_prewrite":controlled and current != item["expected_sha256"],"valid":valid})
check(1,"every locked preparation input and contract hash match",len(hash_results)==17 and all(item["valid"] for item in hash_results) and sha256(CONTRACT)==input_lock["contract_sha256"],hash_results)

# Gate 2
approval = input_lock["execution_approval"]
check(2,"Flamestrike separately approved execution of the exact contract",approval["approver"]=="Flamestrike" and approval["statement"]=="approved" and approval["candidate_rule_approval_granted"] is False and approval["rule_evaluation_granted"] is False and approval["implementation_granted"] is False,approval)

# Gate 3
selected = [item["id"] for item in r8["options"] if item["selected"]]
selection = r8["selection_record"]
check(3,"R8-A remains the only selected route",selected==["S10R-006-R8-A"] and selection["selected_option"]=="S10R-006-R8-A" and selection["selected_option_count"]==1 and r8["authorization_flags"]["gap_coupling_contract_preparation_authorized"] is True and r8_validation["route_selection_closeout"]["status"]=="pass_12_of_12",{"selected":selected,"selection":selection,"closeout":r8_validation["route_selection_closeout"]["status"]})

# Gate 4
r3_ok = r3["status"]=="approved_bounded_symbolic_method_no_field_coupling" and r3["authorization_flags"]["method_implementation_authorized"] is False
r5_ok = r5["status"]=="approved_bounded_symbolic_rule_four_blocked_corner_gaps_unowned" and r5["coupling_descriptor"]["evaluated"] is False and r5["authorization_flags"]["rule_evaluation_authorized"] is False
r7_ok = r7["status"]=="approved_bounded_cross_view_corner_ownership_rule_registered_no_implementation" and r7["candidate_gap_rule"]["evaluated"] is False and r7["authorization_flags"]["rule_evaluation_authorized"] is False
check(4,"R3 R5 and R7 remain approved bounded and unevaluated",r3_ok and r5_ok and r7_ok,{"r3":r3["status"],"r5":r5["status"],"r7":r7["status"]})

# Gate 5
expected_lanes = [("AFM-FRONT-RIGHT","+X","[-1/2,1/2]"),("AFM-LEFT-LEFT","+Y","[3/2,5/2]"),("AFM-FRONT-LEFT","-X","[7/2,9/2]"),("AFM-LEFT-RIGHT","-Y","[11/2,13/2]")]
expected_gaps = [("G_0","(1/2,3/2)"),("G_1","(5/2,7/2)"),("G_2","(9/2,11/2)"),("G_3","(13/2,15/2)")]
r5_lanes = [(item["lane_id"],item["cardinal_center"],item["q_interval"]) for item in r5["lanes"]]
r7_lanes = [(item["lane_id"],item["cardinal_label"],item["q_interval"]) for item in r7["preserved_owned_lanes"]]
reg_lanes = [(item["lane_id"],item["cardinal_label"],item["q_interval"]) for item in registry["preserved_owned_lanes"]]
r7_gaps = [(item["id"],item["open_interval"]) for item in r7["gaps"]]
reg_gaps = [(item["id"],item["open_interval"]) for item in registry["gaps"]]
check(5,"four R5 closed lane intervals and four R7 open gaps replay exactly",expected_lanes==r5_lanes==r7_lanes==reg_lanes and expected_gaps==r7_gaps==reg_gaps,{"lanes":reg_lanes,"gaps":reg_gaps})

# Gate 6
endpoint_policy = "each lane owns both endpoints of its own closed interval; open gaps are unowned"
tie_policy = "single successor owner label at the exact symbolic midpoint"
check(6,"R5 endpoint ownership and R7 successor-at-tie policy remain unchanged",r5["abstract_parameter"]["endpoint_convention"]==endpoint_policy and r7["candidate_gap_rule"]["tie_policy"]==tie_policy and r7["endpoint_policy"]["existing_r5_lane_endpoints_mutated"] is False,{"endpoint_policy":endpoint_policy,"tie_policy":tie_policy})

# Gate 7
q = registry["abstract_parameter_reference"]
check(7,"q remains non-periodic and unwrapped with 15/2 excluded",q["combined_symbolic_domain"]=="[-1/2,15/2)" and q["periodic"] is False and q["unwrapped"] is True and q["wrap"] is None and q["q_15_over_2_in_domain"] is False and q["final_first_endpoint_identification"] is False and registry["gaps"][3]["q_15_over_2_identified_with_q_minus_1_over_2"] is False,q)

# Gate 8
expected_selectors = [
    ("G_0","1/2 < q < m_0 -> AFM-FRONT-RIGHT / +X, u=1","m_0 <= q < 3/2 -> AFM-LEFT-LEFT / +Y, u=0"),
    ("G_1","5/2 < q < m_1 -> AFM-LEFT-LEFT / +Y, u=1","m_1 <= q < 7/2 -> AFM-FRONT-LEFT / -X, u=0"),
    ("G_2","9/2 < q < m_2 -> AFM-FRONT-LEFT / -X, u=1","m_2 <= q < 11/2 -> AFM-LEFT-RIGHT / -Y, u=0"),
    ("G_3","13/2 < q < m_3 -> AFM-LEFT-RIGHT / -Y, u=1","m_3 <= q < 15/2 -> AFM-FRONT-RIGHT / +X label-only successor, u=0, no wrap"),
]
actual_selectors = [(item["id"],item["lower_endpoint_selector"],item["upper_endpoint_selector"]) for item in registry["gaps"]]
expected_owners = [
    ("G_0","1/2 < q < m_0 -> AFM-FRONT-RIGHT / +X","m_0 <= q < 3/2 -> AFM-LEFT-LEFT / +Y"),
    ("G_1","5/2 < q < m_1 -> AFM-LEFT-LEFT / +Y","m_1 <= q < 7/2 -> AFM-FRONT-LEFT / -X"),
    ("G_2","9/2 < q < m_2 -> AFM-FRONT-LEFT / -X","m_2 <= q < 11/2 -> AFM-LEFT-RIGHT / -Y"),
    ("G_3","13/2 < q < m_3 -> AFM-LEFT-RIGHT / -Y","m_3 <= q < 15/2 -> AFM-FRONT-RIGHT / +X label-only successor"),
]
actual_owners = [(item["id"],item["lower_owner_branch"],item["upper_owner_branch"]) for item in registry["gaps"]]
check(8,"endpoint selector contains exactly eight predecessor-u1 and successor-u0 branches",actual_selectors==expected_selectors and actual_owners==expected_owners and registry["definition_counts"]["endpoint_selector_branches"]==8 and registry["definition_counts"]["owner_branches"]==8,{"selectors":actual_selectors,"owners":actual_owners})

# Gate 9
expected_weights = [f"W^G_{index}(q,v) = W_{{ell(O_{index}(q))}}(e_{index}(q),v)" for index in range(4)]
actual_weights = [item["gap_weight_descriptor"] for item in registry["gaps"]]
endpoints = registry["r3_endpoint_identity_replay"]
check(9,"gap weight descriptors reference only R3 endpoint identities",actual_weights==expected_weights and registry["candidate_rule"]["gap_weight_descriptor"]=="W^G_k(q,v) = W_{ell(O_k(q))}(e_k(q),v)" and endpoints["u_0_identity"]=="T_0" and endpoints["u_1_identity"]=="T_2" and endpoints["gap_permitted_endpoint_selector_values"]==["0","1"] and registry["candidate_rule"]["physical_correspondence_claim"] is False,{"weights":actual_weights,"endpoints":endpoints})

# Gate 10
expected_boundaries = [f"C^G_{index}(q,v) = B_v(q)" for index in range(4)]
actual_boundaries = [item["gap_boundary_descriptor"] for item in registry["gaps"]]
check(10,"gap boundary descriptors equal unevaluated B_v(q) only",actual_boundaries==expected_boundaries and registry["candidate_rule"]["gap_boundary_descriptor"]=="C^G_k(q,v) = B_v(q)" and registry["candidate_rule"]["evaluated"] is False and registry["r5_boundary_replay"]["evaluated_samples"]==[],actual_boundaries)

# Gate 11
rule = registry["candidate_rule"]
lane_case = "C*(q,v) = C_L(u,v) when q=q_L(u), q in the owned interval of L, 0 <= u <= 1"
gap_case = "C*(q,v) = C^G_k(q,v) when q in G_k"
expected_tuples = [f"K_{index}(q,v) = (O_{index}(q), e_{index}(q), W^G_{index}(q,v), C^G_{index}(q,v))" for index in range(4)]
actual_tuples = [item["coupling_tuple"] for item in registry["gaps"]]
check(11,"unified descriptor preserves C_L on lanes and uses C_G only in gaps",rule["unified_descriptor_lane_case"]==lane_case and rule["unified_descriptor_gap_case"]==gap_case and rule["coupling_tuple"]=="K_k(q,v) = (O_k(q), e_k(q), W^G_k(q,v), C^G_k(q,v))" and actual_tuples==expected_tuples and all(item["coupling"]=="C_L(u,v) = B_v(q_L(u))" for item in registry["preserved_owned_lanes"]),{"lane_case":rule["unified_descriptor_lane_case"],"gap_case":rule["unified_descriptor_gap_case"],"tuples":actual_tuples})

# Gate 12
check(12,"no lane-local u is extrapolated outside zero through one",rule["gap_local_continuous_u_defined"] is False and rule["lane_local_u_extrapolated"] is False and rule["cross_lane_interpolation_defined"] is False and endpoints["continuous_gap_local_u_defined"] is False and endpoints["lane_u_extrapolation"] is False,{"rule":rule,"endpoint_replay":endpoints})

# Gate 13
defs = registry["definition_counts"]
check(13,"exactly one candidate rule is registered and remains unapproved",registry["status"]=="candidate_bounded_corner_gap_to_field_coupling_rule_registered_no_implementation" and registry["artifact_classification"]=="candidate" and registry["technical_result"]==PASS_RESULT and defs["candidate_rules"]==1 and defs["registered_candidate_rules"]==1 and defs["approved_rules"]==0 and rule["approved"] is False,defs)

# Gates 14-16
counts = registry["output_counts"]
instance_keys = ["q_instances","u_instances","v_instances","owner_instances","record_instances","weight_instances","boundary_instances","samples"]
source_keys = ["source_assignments","source_normals","transforms","physical_pairs","target_coordinates","centers","pivots","anchors"]
structure_keys = ["seams","joins","closures","fields","fills","surfaces","topology","geometry"]
check(14,"all parameter owner record weight boundary instances and samples remain zero",all(counts[key]==0 for key in instance_keys),{key:counts[key] for key in instance_keys})
check(15,"all source assignments transforms pairs and target coordinates remain zero",all(counts[key]==0 for key in source_keys),{key:counts[key] for key in source_keys})
check(16,"all seams joins closures fields fills surfaces topology and geometry remain zero",all(counts[key]==0 for key in structure_keys),{key:counts[key] for key in structure_keys})

# Gate 17
holdouts = [r3["holdouts"],r5["holdouts"],r7["holdouts"],registry["holdouts"]]
check(17,"all fourteen back and right records remain proof only",all(item["classification"]=="proof only" and item["total"]==14 and item["construction_use_authorized"] is False for item in holdouts),holdouts)

# Gate 18
expected_blocks = [("S10R-BLOCK-006","active_candidate_corner_gap_to_field_coupling_rule_registered_no_field_no_seam_no_join_no_closure"),("S10R-BLOCK-008","active_unchanged"),("S10R-BLOCK-009","active_unchanged")]
actual_blocks = [(item["id"],item["status"]) for item in registry["active_blocks"]]
check(18,"all three blocks remain active and resolved block IDs remain empty",actual_blocks==expected_blocks and registry["resolved_block_ids"]==[],{"blocks":actual_blocks,"resolved":registry["resolved_block_ids"]})

# Gate 19
flags = registry["authorization_flags"]
flags_ok = flags["candidate_rule_registered"] is True and all(value is False for key,value in flags.items() if key!="candidate_rule_registered")
check(19,"evaluation implementation downstream and Git authority flags remain false",flags_ok,flags)

# Gate 20
allowlist = set(input_lock["execution_allowlist"])
records = git_status_records()
outside_records = [record for record,path in records if path not in allowlist]
scoped_paths = {path for _,path in records if path in allowlist}
outside_digest = hashlib.sha256(b"".join(outside_records)).hexdigest()
staged_raw = subprocess.check_output(["git","diff","--cached","--name-only","-z"],cwd=ROOT)
staged_paths = [item.decode("utf-8") for item in staged_raw.split(b"\0") if item]
expected_docs = {str(path.relative_to(ROOT)) for directory in (MANIFESTS,STEPS,HANDOFFS) for path in directory.glob("*S10R_006_R9_A_CORNER_GAP_TO_FIELD_COUPLING_RULE_A01*") if path != CONTRACT}
allowed_docs = {path for path in allowlist if "S10R_006_R9_A_CORNER_GAP_TO_FIELD_COUPLING_RULE_A01" in path}
branch = subprocess.check_output(["git","branch","--show-current"],cwd=ROOT,text=True).strip()
head = subprocess.check_output(["git","rev-parse","HEAD"],cwd=ROOT,text=True).strip()
scope_ok = len(outside_records)==input_lock["git_preexecution"]["outside_execution_allowlist_record_count"] and outside_digest==input_lock["git_preexecution"]["outside_execution_allowlist_porcelain_v1_z_sha256"] and scoped_paths==allowlist and expected_docs==allowed_docs and staged_paths==[] and branch==input_lock["branch"] and head==input_lock["head"]
check(20,"changed paths match the execution allowlist and no path is staged",scope_ok,{"outside_count":len(outside_records),"outside_sha256":outside_digest,"scoped_paths":sorted(scoped_paths),"expected_docs":sorted(expected_docs),"staged_paths":staged_paths,"branch":branch,"head":head})

# Gate 21
audit = validation["independent_audit"]
first_ok = audit["complete_run_count_before_this_audit"]==0 and audit["status"]=="not_yet_run" and audit["expected_gate_count"]==22 and audit["complete_run_count_after_audit"]==0
check(21,"first complete independent audit passes every gate",first_ok,audit)

# Gate 22
visibility = validation["visible_review"]
live = desktop_sample()
visible_ok = visibility["preflight_verified"] is True and visibility["output_record_visible"] is True and visibility["decision_handoff_visible"] is True and visibility["wmctrl_return_code"]==0 and live["return_code"]==0 and live["output_title_found"] and live["handoff_title_found"] and PASS_RESULT in output_text and "S10R-006-R9-A-CGFC-A01" in output_text and "S10R-006-R9-A-CGFC-A01" in handoff_text
check(22,"final output and handoff are visibly presented",visible_ok,{"validation":visibility,"live_sample":live})

failed = [item for item in checks if item["status"]!="pass"]
result = {
    "schema":"aerathea.s10r_006_r9_a_corner_gap_to_field_coupling_rule_a01_independent_audit.v1",
    "status":"pass_22_of_22_first_complete_run" if not failed else "fail_closed_first_complete_run",
    "technical_result":PASS_RESULT if not failed else BLOCK_RESULT,
    "complete_run_ordinal":1,
    "gate_count":len(checks),
    "passed_gate_count":len(checks)-len(failed),
    "failed_gate_count":len(failed),
    "checks":checks,
}
print(json.dumps(result,indent=2))
sys.exit(0 if not failed else 1)
