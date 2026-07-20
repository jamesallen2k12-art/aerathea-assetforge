#!/usr/bin/env python3
"""Read-only Core audit for A005 S10R-006-R3-A AFM A01."""

from __future__ import annotations

import hashlib
import json
import subprocess
from pathlib import Path


ROOT = Path(__file__).resolve().parents[2]
BASE = ROOT / "docs/assets/blueprints/SM_GIA_BloodAxeCairnstone_A005"
M = BASE / "manifests"
S = BASE / "steps"
H = BASE / "handoffs"

PATHS = {
    "input": M / "S10R_006_R3_A_ABSTRACT_FIELD_METHOD_A01_INPUT_LOCK.json",
    "method": M / "S10R_006_R3_A_ABSTRACT_FIELD_METHOD_A01_METHOD_REGISTRY.json",
    "dependency": M / "S10R_006_R3_A_ABSTRACT_FIELD_METHOD_A01_DEPENDENCY_AUDIT.json",
    "validation": M / "S10R_006_R3_A_ABSTRACT_FIELD_METHOD_A01_VALIDATION.json",
    "selection": M / "S10R_006_R2_A_POST_BRIDGE_FIELD_AUTHORITY_OPTION_REGISTRY.json",
    "bridge": M / "S10R_006_R1_A_NORMALIZED_PRIMARY_OWNER_BRIDGE_A01_DECISION_REGISTRY.json",
    "contract": S / "S10R_006_R3_A_ABSTRACT_FIELD_METHOD_A01_CONTRACT.md",
    "output": S / "S10R_006_R3_A_ABSTRACT_FIELD_METHOD_A01_OUTPUT_RECORD.md",
    "handoff": H / "S10R_006_R3_A_ABSTRACT_FIELD_METHOD_A01_TO_DECISION_HANDOFF.md",
}

EXPECTED_LANES = [
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

ALLOWED_R3 = {
    "Tools/DCC/audit_bloodaxe_cairnstone_a005_s10r006_r3_a_abstract_field_method_a01.py",
    "docs/assets/blueprints/SM_GIA_BloodAxeCairnstone_A005/handoffs/S10R_006_R3_A_ABSTRACT_FIELD_METHOD_A01_TO_DECISION_HANDOFF.md",
    "docs/assets/blueprints/SM_GIA_BloodAxeCairnstone_A005/manifests/S10R_006_R3_A_ABSTRACT_FIELD_METHOD_A01_DEPENDENCY_AUDIT.json",
    "docs/assets/blueprints/SM_GIA_BloodAxeCairnstone_A005/manifests/S10R_006_R3_A_ABSTRACT_FIELD_METHOD_A01_INPUT_LOCK.json",
    "docs/assets/blueprints/SM_GIA_BloodAxeCairnstone_A005/manifests/S10R_006_R3_A_ABSTRACT_FIELD_METHOD_A01_METHOD_REGISTRY.json",
    "docs/assets/blueprints/SM_GIA_BloodAxeCairnstone_A005/manifests/S10R_006_R3_A_ABSTRACT_FIELD_METHOD_A01_VALIDATION.json",
    "docs/assets/blueprints/SM_GIA_BloodAxeCairnstone_A005/steps/S10R_006_R3_A_ABSTRACT_FIELD_METHOD_A01_CONTRACT.md",
    "docs/assets/blueprints/SM_GIA_BloodAxeCairnstone_A005/steps/S10R_006_R3_A_ABSTRACT_FIELD_METHOD_A01_OUTPUT_RECORD.md",
}


def load(path: Path):
    return json.loads(path.read_text(encoding="utf-8"))


def sha(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest()


checks = []


def gate(subject: str, ok: bool, evidence):
    checks.append(
        {
            "gate": len(checks) + 1,
            "subject": subject,
            "status": "pass" if ok else "fail",
            "evidence": evidence,
        }
    )


required = all(path.exists() for path in PATHS.values())
gate("all required contract and package files exist", required, [str(p.relative_to(ROOT)) for p in PATHS.values()])

data = {name: load(path) for name, path in PATHS.items() if path.suffix == ".json"}
input_lock = data["input"]
method = data["method"]
dependency = data["dependency"]
selection = data["selection"]
bridge = data["bridge"]
validation = data["validation"]

locked = input_lock["immutable_locked_inputs"]["sha256"]
hash_results = {
    path: {"expected": expected, "current": sha(ROOT / path)}
    for path, expected in locked.items()
}
gate(
    "all fifteen immutable input hashes match",
    len(hash_results) == 15 and all(v["expected"] == v["current"] for v in hash_results.values()),
    hash_results,
)

contract_ok = (
    sha(PATHS["contract"]) == input_lock["contract_sha256"]
    and input_lock["execution_approval"]["statement"] == "approved"
)
gate("approved visible contract hash and execution approval match", contract_ok, {
    "contract_sha256": sha(PATHS["contract"]),
    "approval": input_lock["execution_approval"],
})

selected = [item["id"] for item in selection["options"] if item["selected"]]
gate(
    "R2 selects only the bounded A route with no field authority",
    selection["selected_option"] == "S10R-006-R2-A"
    and selected == ["S10R-006-R2-A"]
    and selection["selection_record"]["field_implementation_authorized"] is False
    and selection["selection_record"]["resolved_block_ids"] == [],
    {"selected_option": selection["selected_option"], "selected": selected},
)

frozen = [item["frozen_record"] for item in bridge["approved_mappings"]]
frozen_projection = [
    {
        "trace_id": r["trace_id"],
        "owner_view": r["owner_view"],
        "owner_plane": r["owner_plane"],
        "registered_side": r["registered_side"],
        "within_side_order": r["within_side_order"],
        "normalized_transition_identity": r["normalized_transition_identity"],
        "inner_station": r["inner_boundary_identity"]["station"],
        "outer_station": r["outer_boundary_identity"]["station"],
    }
    for r in frozen
]
expected_projection = []
for lane in EXPECTED_LANES:
    for trace_id, order in zip(lane["trace_ids"], lane["within_side_orders"]):
        expected_projection.append(
            {
                "trace_id": trace_id,
                "owner_view": lane["owner_view"],
                "owner_plane": lane["owner_plane"],
                "registered_side": lane["registered_side"],
                "within_side_order": order,
                "normalized_transition_identity": "v = t",
                "inner_station": "t = 0; v = 0",
                "outer_station": "t = 1; v = 1",
            }
        )
gate("twelve frozen construction records match exact lane identities", frozen_projection == expected_projection, {
    "record_count": len(frozen_projection),
})

gate("method registry contains exactly four exact three-record lanes", method["lanes"] == EXPECTED_LANES, method["lanes"])

gate(
    "all lane stations are exact normalized rank only",
    all(lane["u_stations"] == ["0", "1/2", "1"] for lane in method["lanes"])
    and method["construction_frame"]["u_meaning"] == "normalized within-lane rank only",
    [lane["u_stations"] for lane in method["lanes"]],
)

gate(
    "v=t and endpoint identities remain exact",
    method["construction_frame"]["v_identity"] == "v = t"
    and all(r["normalized_transition_identity"] == "v = t" for r in frozen)
    and all(r["inner_boundary_identity"]["station"] == "t = 0; v = 0" for r in frozen)
    and all(r["outer_boundary_identity"]["station"] == "t = 1; v = 1" for r in frozen),
    method["construction_frame"],
)

operator = method["between_trace_operator"]
gate(
    "unevaluated adjacent-record operator is exact",
    operator["interval_index"] == "j(u) = min(floor(2u), 1)"
    and operator["local_weight"] == "lambda(u) = 2u - j(u)"
    and operator["properties"]["j_range"] == [0, 1]
    and operator["properties"]["lambda_range"] == [0, 1]
    and operator["properties"]["weight_sum"] == "1"
    and operator["properties"]["adjacent_records_only"] is True
    and operator["properties"]["cross_lane_interpolation"] is False,
    operator,
)

family = method["boundary_family"]
gate(
    "K80 N3 and homothetic family formulas and endpoints are exact",
    family["k80"] == "abs(x / 56)^3 + abs(y / 44)^3 = 1"
    and family["n3"] == "abs(x / 70)^3 + abs(y / 55)^3 = 1"
    and family["scale"] == "s(v) = 0.8 + 0.2v"
    and family["a"] == "a(v) = 70s(v) = 56 + 14v"
    and family["b"] == "b(v) = 55s(v) = 44 + 11v"
    and family["endpoint_audit"] == {"s_0": "0.8", "s_1": "1", "a_0": 56, "a_1": 70, "b_0": 44, "b_1": 55},
    family,
)

coupling = method["coupling"]
gate(
    "all lane boundary seam and physical couplings remain absent",
    coupling["lane_to_boundary_function"] is None
    and coupling["angular_placement"] is None
    and coupling["arc_length_placement"] is None
    and coupling["source_to_target_transform"] is None
    and coupling["cross_lane_seam"] is None
    and coupling["top_upright_join"] is None
    and coupling["closed_field"] is False
    and coupling["physical_field"] is False,
    coupling,
)

holdouts = bridge["validation_holdouts"]
gate(
    "fourteen back right records remain proof-only holdouts",
    len(holdouts) == 14
    and sum(item["view"] == "back" for item in holdouts) == 6
    and sum(item["view"] == "right" for item in holdouts) == 8
    and method["holdouts"]["construction_use_authorized"] is False,
    method["holdouts"],
)

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
counts = method["authority_counts"]
gate("all physical field and geometry authority counts remain zero", all(counts[k] == 0 for k in zero_keys), counts)

active = {item["id"]: item["status"] for item in method["active_blocks"]}
gate(
    "all three blocks remain active and none resolves",
    set(active) == {"S10R-BLOCK-006", "S10R-BLOCK-008", "S10R-BLOCK-009"}
    and all(value.startswith("active") for value in active.values())
    and method["resolved_block_ids"] == [],
    active,
)

flags = method["authorization_flags"]
decision = method["flamestrike_decision"]
gate(
    "bounded method decision is approved while all implementation downstream and git flags remain false",
    decision["decision"] == "approve"
    and decision["statement"] == "approved"
    and decision["scope"] == "authoritative bounded symbolic interpretation only"
    and decision["resolved_block_ids"] == []
    and decision["field_implementation_authorized"] is False
    and decision["coupling_rule_authorized"] is False
    and all(value is False for value in flags.values()),
    {"decision": decision, "authorization_flags": flags},
)

gate(
    "dependency audit preserves missing coupling and creates no authority",
    dependency["status"] == "pass_bounded_dependencies_exact_missing_coupling_preserved"
    and len(dependency["missing_authority"]) == 7
    and dependency["authority_effect"] == {
        "physical_authority_created": False,
        "field_authority_created": False,
        "geometry_authority_created": False,
        "downstream_authority_created": False,
    },
    dependency["authority_effect"],
)

output_text = PATHS["output"].read_text(encoding="utf-8")
output_markers = [
    "pass_bounded_symbolic_method_registered_no_field_coupling",
    "Flamestrike Method Decision",
    "No approved record defines a map",
    "field samples: 0",
    "resolved block IDs: none",
    "Required Stop",
]
gate("output record contains exact result and stop markers", all(x in output_text for x in output_markers), output_markers)

handoff_text = PATHS["handoff"].read_text(encoding="utf-8")
handoff_markers = [
    "Candidate Recommendation",
    "Closed Method Decision",
    "bounded symbolic interpretation",
    "all three blocks remain active",
    "This decision authorizes no field implementation",
    "Required Decision Stop — Completed",
]
gate("decision handoff preserves candidate decision and implementation stop", all(x in handoff_text for x in handoff_markers), handoff_markers)

status = subprocess.run(
    ["git", "status", "--porcelain=v1", "-uall"],
    cwd=ROOT,
    text=True,
    capture_output=True,
    check=True,
).stdout.splitlines()
r3_paths = set()
for line in status:
    path = line[3:]
    if "S10R_006_R3_A_" in path or "s10r006_r3_a_" in path:
        r3_paths.add(path)
gate("R3 changed paths match the exact execution allowlist", r3_paths == ALLOWED_R3, {
    "actual": sorted(r3_paths),
    "allowed": sorted(ALLOWED_R3),
    "unexpected": sorted(r3_paths - ALLOWED_R3),
})

staged = subprocess.run(
    ["git", "diff", "--cached", "--name-only"],
    cwd=ROOT,
    text=True,
    capture_output=True,
    check=True,
).stdout.splitlines()
gate("no path is staged", staged == [], staged)

failed = sum(item["status"] == "fail" for item in checks)
report = {
    "schema": "aerathea.s10r_006_r3_a_abstract_field_method_a01_independent_audit.v1",
    "status": "pass" if failed == 0 else "fail",
    "artifact_classification": "proof only",
    "gate_count": len(checks),
    "passed_gate_count": len(checks) - failed,
    "failed_gate_count": failed,
    "checks": checks,
}
print(json.dumps(report, indent=2))
raise SystemExit(1 if failed else 0)
