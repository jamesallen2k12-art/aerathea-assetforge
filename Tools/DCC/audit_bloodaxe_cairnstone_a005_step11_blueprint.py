#!/usr/bin/env python3
"""Read-only fail-closed audit for the A005 Step 11 planning package."""

from __future__ import annotations

import argparse
import hashlib
import json
import subprocess
import sys
from pathlib import Path
from typing import Any


ROOT = Path(__file__).resolve().parents[2]
A005 = ROOT / "docs/assets/blueprints/SM_GIA_BloodAxeCairnstone_A005"
CONTRACT_ID = "A005-CR-STEP11-PROD-SPEC-GCB-A01"
AUTHORITY_STATEMENT = (
    "resume, I am giving you full authority to do whatever you need to to complete "
    "step 11 from start to finish, You have full approval and Authority"
)

LOCK = A005 / "manifests/STEP_11_INPUT_LOCK.json"
RULES = A005 / "manifests/STEP_11_TECHNICAL_RULE_REGISTRY.json"
VERTICES = A005 / "manifests/STEP_11_VERTEX_AUTHORITY_MAP.json"
BLUEPRINT = A005 / "manifests/STEP_11_CONSTRUCTION_BLUEPRINT.json"
VALIDATION = A005 / "manifests/STEP_11_VALIDATION_MANIFEST.json"
CONTRACT = A005 / "steps/STEP_11_PRODUCTION_SPECIFICATION_AND_GEOMETRY_CONSTRUCTION_BLUEPRINT_CONTRACT.md"
REVIEW = A005 / "review/STEP_11_PRODUCTION_BLUEPRINT_REVIEW.md"
OUTPUT = A005 / "steps/STEP_11_OUTPUT_RECORD.md"
HANDOFF = A005 / "handoffs/STEP_11_TO_STEP_12_HANDOFF.md"

REQUIRED_BLUEPRINT_FILES = [LOCK, RULES, VERTICES, BLUEPRINT, CONTRACT]
REQUIRED_FINAL_FILES = REQUIRED_BLUEPRINT_FILES + [VALIDATION, REVIEW, OUTPUT, HANDOFF]

ALLOWED_CHANGED_PATHS = {
    "Tools/DCC/audit_bloodaxe_cairnstone_a005_step11_blueprint.py",
    "docs/assets/blueprints/SM_GIA_BloodAxeCairnstone_A005/manifests/STEP_11_INPUT_LOCK.json",
    "docs/assets/blueprints/SM_GIA_BloodAxeCairnstone_A005/manifests/STEP_11_TECHNICAL_RULE_REGISTRY.json",
    "docs/assets/blueprints/SM_GIA_BloodAxeCairnstone_A005/manifests/STEP_11_VERTEX_AUTHORITY_MAP.json",
    "docs/assets/blueprints/SM_GIA_BloodAxeCairnstone_A005/manifests/STEP_11_CONSTRUCTION_BLUEPRINT.json",
    "docs/assets/blueprints/SM_GIA_BloodAxeCairnstone_A005/manifests/STEP_11_VALIDATION_MANIFEST.json",
    "docs/assets/blueprints/SM_GIA_BloodAxeCairnstone_A005/review/STEP_11_PRODUCTION_BLUEPRINT_REVIEW.md",
    "docs/assets/blueprints/SM_GIA_BloodAxeCairnstone_A005/steps/STEP_11_PRODUCTION_SPECIFICATION_AND_GEOMETRY_CONSTRUCTION_BLUEPRINT_CONTRACT.md",
    "docs/assets/blueprints/SM_GIA_BloodAxeCairnstone_A005/steps/STEP_11_OUTPUT_RECORD.md",
    "docs/assets/blueprints/SM_GIA_BloodAxeCairnstone_A005/handoffs/STEP_11_TO_STEP_12_HANDOFF.md",
    "docs/assets/blueprints/SM_GIA_BloodAxeCairnstone_A005/SM_GIA_BloodAxeCairnstone_A005_APPROVAL_LOG.md",
    "docs/assets/blueprints/SM_GIA_BloodAxeCairnstone_A005/SM_GIA_BloodAxeCairnstone_A005_ARTIFACT_INDEX.md",
    "docs/assets/blueprints/SM_GIA_BloodAxeCairnstone_A005/SM_GIA_BloodAxeCairnstone_A005_RESET_RESUME_STATE.md",
}

RESERVED_PRODUCTION_PATHS = [
    ROOT / "SourceAssets/Blender/Props/Giants/BloodAxe/Cairns/SM_GIA_BloodAxeCairnstone_A005",
    ROOT / "SourceAssets/Exports/Props/Giants/BloodAxe/Cairns/SM_GIA_BloodAxeCairnstone_A005",
    ROOT / "SourceAssets/Textures/Props/Giants/BloodAxe/Cairns/SM_GIA_BloodAxeCairnstone_A005",
    ROOT / "Saved/Automation/DCC/SM_GIA_BloodAxeCairnstone_A005/Production",
    ROOT / "Content/Aerathea/Props/Giants/BloodAxe/Cairns/SM_GIA_BloodAxeCairnstone_A005.uasset",
]
PREEXISTING_CORE_RECOVERY_ROOT = (
    ROOT / "Saved/Automation/DCC/SM_GIA_BloodAxeCairnstone_A005/CoreRecovery"
)


def sha256(path: Path) -> str:
    digest = hashlib.sha256()
    with path.open("rb") as handle:
        for block in iter(lambda: handle.read(1024 * 1024), b""):
            digest.update(block)
    return digest.hexdigest()


def load_json(path: Path) -> dict[str, Any]:
    with path.open("r", encoding="utf-8") as handle:
        value = json.load(handle)
    if not isinstance(value, dict):
        raise ValueError(f"top-level JSON value must be an object: {path}")
    return value


class Audit:
    def __init__(self) -> None:
        self.gates: list[dict[str, Any]] = []

    def check(self, gate_id: str, condition: bool, detail: Any) -> None:
        self.gates.append(
            {
                "id": gate_id,
                "status": "pass" if condition else "fail",
                "detail": detail,
            }
        )

    @property
    def failures(self) -> list[dict[str, Any]]:
        return [gate for gate in self.gates if gate["status"] == "fail"]


def git_changed_paths() -> set[str]:
    result = subprocess.run(
        ["git", "status", "--porcelain=v1", "--untracked-files=all"],
        cwd=ROOT,
        check=True,
        text=True,
        stdout=subprocess.PIPE,
        stderr=subprocess.PIPE,
    )
    paths: set[str] = set()
    for raw in result.stdout.splitlines():
        if len(raw) < 4:
            continue
        path = raw[3:]
        if " -> " in path:
            path = path.split(" -> ", 1)[1]
        paths.add(path)
    return paths


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument(
        "--phase",
        choices=("blueprint", "final"),
        default="blueprint",
        help="final additionally requires closeout/review/handoff outputs",
    )
    args = parser.parse_args()

    audit = Audit()
    required = REQUIRED_FINAL_FILES if args.phase == "final" else REQUIRED_BLUEPRINT_FILES
    missing = [str(path.relative_to(ROOT)) for path in required if not path.is_file()]
    symlinks = [str(path.relative_to(ROOT)) for path in required if path.is_symlink()]
    audit.check("G01_required_files", not missing and not symlinks, {"missing": missing, "symlinks": symlinks})
    if missing or symlinks:
        print(json.dumps({"phase": args.phase, "gates": audit.gates, "failures": len(audit.failures)}, indent=2))
        return 1

    try:
        lock = load_json(LOCK)
        rules = load_json(RULES)
        vertices = load_json(VERTICES)
        blueprint = load_json(BLUEPRINT)
        validation = load_json(VALIDATION) if args.phase == "final" else None
    except (OSError, ValueError, json.JSONDecodeError) as exc:
        audit.check("G02_json_parse", False, str(exc))
        print(json.dumps({"phase": args.phase, "gates": audit.gates, "failures": len(audit.failures)}, indent=2))
        return 1
    audit.check("G02_json_parse", True, "all required JSON objects parsed")

    contract_ids = {lock.get("contract_id"), rules.get("contract_id"), vertices.get("contract_id"), blueprint.get("contract_id")}
    if validation is not None:
        contract_ids.add(validation.get("contract_id"))
    audit.check("G03_contract_id", contract_ids == {CONTRACT_ID}, sorted(str(value) for value in contract_ids))
    audit.check(
        "G04_flamestrike_authority",
        lock.get("flamestrike_authority", {}).get("statement") == AUTHORITY_STATEMENT
        and blueprint.get("approval", {}).get("authority_statement") == AUTHORITY_STATEMENT,
        "exact authority statement replayed",
    )

    locked_inputs = lock.get("locked_inputs", [])
    input_results: list[dict[str, Any]] = []
    for record in locked_inputs:
        rel = record.get("path")
        expected = record.get("sha256")
        path = ROOT / str(rel)
        exists = path.is_file() and not path.is_symlink()
        observed = sha256(path) if exists else None
        input_results.append({"path": rel, "exists": exists, "expected": expected, "observed": observed, "match": exists and observed == expected})
    input_counts_match = len(locked_inputs) == lock.get("counts", {}).get("locked_inputs") == 42
    audit.check(
        "G05_locked_inputs",
        input_counts_match and all(record["match"] for record in input_results),
        {"declared": lock.get("counts", {}).get("locked_inputs"), "actual": len(locked_inputs), "mismatches": [r for r in input_results if not r["match"]]},
    )

    expected_rule_ids = {
        "S11-TR-001-CONSTRUCTION-FRAME",
        "S11-TR-002-OWNER-VIEW-CONSTRAINT-NORMALIZATION",
        "S11-TR-003-C001-FACETED-SECTOR-CONSTRUCTION",
        "S11-TR-004-BASE-VERTICAL-STATIONS",
        "S11-TR-005-INDEPENDENT-BASE-CONTAINMENT",
        "S11-TR-006-HIDDEN-CLOSURE-AND-OVERLAP",
        "S11-TR-007-C004-FIELD-SAMPLING-AND-SEAM",
        "S11-TR-008-RUNTIME-TOPOLOGY-ARRANGEMENT",
        "S11-TR-009-DECORATION-GEOMETRY-CLASSIFICATION",
        "S11-TR-010-REVIEW-PROJECTION",
    }
    observed_rule_ids = {record.get("id") for record in rules.get("rules", [])}
    audit.check(
        "G06_technical_rules",
        observed_rule_ids == expected_rule_ids
        and rules.get("counts", {}).get("technical_rules") == 10
        and rules.get("authority_boundary", {}).get("geometry_created") is False,
        {"missing": sorted(expected_rule_ids - observed_rule_ids), "extra": sorted(str(v) for v in observed_rule_ids - expected_rule_ids)},
    )

    groups = vertices.get("authority_groups", [])
    group_ids = [record.get("id") for record in groups]
    semantic_consumers = {record.get("component_id") for record in vertices.get("non_vertex_consumers", [])}
    audit.check(
        "G07_vertex_authority_coverage",
        len(groups) == 14
        and len(set(group_ids)) == 14
        and vertices.get("counts", {}).get("unmapped_planned_vertex_classes") == 0
        and semantic_consumers == {"C-005", "C-006", "C-007"},
        {"groups": len(groups), "unique": len(set(group_ids)), "non_vertex_consumers": sorted(str(v) for v in semantic_consumers)},
    )
    forbidden_claim_terms = ("source center", "physical cross-view", "unified", "source seam", "shared")
    groups_with_no_boundary = [record.get("id") for record in groups if not record.get("blocked_claims")]
    groups_without_authority = [record.get("id") for record in groups if not record.get("primary_authority")]
    audit.check(
        "G08_group_boundaries",
        not groups_with_no_boundary and not groups_without_authority,
        {"without_blocked_claims": groups_with_no_boundary, "without_primary_authority": groups_without_authority, "forbidden_claim_categories": forbidden_claim_terms},
    )

    identity = blueprint.get("identity", {})
    coordinate = blueprint.get("coordinate_frame", {})
    bounds = coordinate.get("bounds_targets_cm", {})
    audit.check(
        "G09_identity_and_role",
        identity.get("asset_name") == "SM_GIA_BloodAxeCairnstone_A005"
        and identity.get("asset_type") == "Static Mesh"
        and blueprint.get("status") == "approved_authoritative_step11_production_specification",
        identity,
    )
    audit.check(
        "G10_coordinate_and_bounds",
        coordinate.get("unit") == "centimeter"
        and coordinate.get("origin_cm") == [0, 0, 0]
        and coordinate.get("pivot_cm") == [0, 0, 0]
        and bounds.get("assembled", {}).get("height") == 220
        and bounds.get("C001", {}) == {"max_width": 120, "max_depth": 90}
        and bounds.get("C004", {}) == {"max_width": 140, "max_depth": 110}
        and bounds.get("assembled_base", {}).get("height") == 35,
        bounds,
    )

    order = blueprint.get("construction_order", [])
    order_ids = [record.get("component_id") for record in order]
    audit.check(
        "G11_construction_order",
        order_ids == ["C-004", "C-003", "C-002", "C-001", "C-005_C-006_C-007"],
        order_ids,
    )
    component_specs = blueprint.get("component_specifications", {})
    audit.check(
        "G12_semantic_components",
        set(component_specs) == {"C001", "C002", "C003", "C004", "C005", "C006", "C007"}
        and blueprint.get("counts", {}).get("semantic_components") == 7,
        sorted(component_specs),
    )

    contacts = blueprint.get("contacts_and_hidden_interfaces", {})
    audit.check(
        "G13_contacts_and_overlap",
        contacts.get("source_visible_contact_samples_total") == 127
        and contacts.get("required_intersection_thickness_cm") == 1
        and contacts.get("visible_overlap_pixels_allowed") == 0
        and contacts.get("CL001", {}).get("source_samples") == 40
        and contacts.get("CL002", {}).get("source_samples") == 40
        and contacts.get("CL003", {}).get("source_samples") == 47
        and contacts.get("CL003", {}).get("target_mappings") == 16
        and all(not contacts.get(key, {}).get("shared_loop") for key in ("CL001", "CL002", "CL003")),
        contacts,
    )

    c004 = component_specs.get("C004", {})
    audit.check(
        "G14_n3_k80_scope",
        c004.get("outer_boundary") == "N3: abs(x/70)^3+abs(y/55)^3=1"
        and c004.get("inner_CL003_boundary") == "K80: abs(x/56)^3+abs(y/44)^3=1"
        and c004.get("field_lattice", {}).get("q_columns") == 32
        and c004.get("field_lattice", {}).get("v_rows") == 3
        and c004.get("bottom") == "flat undecorated Z=0 N3-bounded cap",
        c004,
    )

    topology = blueprint.get("topology_plan", {})
    audit.check(
        "G15_topology_and_runtime",
        topology.get("primary_shells") == 4
        and topology.get("each_primary_shell_watertight") is True
        and topology.get("runtime_static_meshes") == 1
        and topology.get("non_manifold_edges_allowed") == 0
        and topology.get("open_boundary_edges_allowed_per_primary_shell") == 0
        and topology.get("degenerate_faces_allowed") == 0,
        topology,
    )

    budget = blueprint.get("triangle_budget", {})
    allocation = sum(budget.get("planning_allocation", {}).values()) if isinstance(budget.get("planning_allocation"), dict) else -1
    lods = blueprint.get("lod_plan", [])
    audit.check(
        "G16_triangle_and_lod_plan",
        budget.get("lod0_target") == 8000
        and budget.get("lod0_hard_cap") == 10000
        and 4000 <= budget.get("lod0_target", 0) <= 10000
        and allocation == 8000
        and [record.get("target_tris") for record in lods] == [8000, 4000, 1800, 700],
        {"target": budget.get("lod0_target"), "cap": budget.get("lod0_hard_cap"), "allocation": allocation, "lods": lods},
    )

    collision = blueprint.get("collision_plan", {})
    uv = blueprint.get("uv_material_texture_plan", {})
    audit.check(
        "G17_collision_uv_material_planning",
        collision.get("hull_count_target") == 4
        and len(collision.get("hulls", [])) == 4
        and collision.get("step11_collision_created") is False
        and uv.get("planning_level_only") is True
        and uv.get("step14_remains_authority_gate") is True
        and uv.get("material_slot_count") == 1
        and uv.get("step11_maps_created") == 0
        and uv.get("optional_emissive_status") == "unapproved and absent unless Step 14 explicitly approves",
        {"collision": collision, "uv_material": uv},
    )

    scope = blueprint.get("scope", {})
    zero_scope = all(
        scope.get(key) is False
        for key in (
            "dcc_created",
            "geometry_created",
            "texture_created",
            "fbx_created",
            "collision_created",
            "lod_created",
            "unreal_work_performed",
            "legacy_A001_A004_asset_specific_data_used",
        )
    )
    audit.check("G18_zero_production_scope", scope.get("planning_only") is True and zero_scope, scope)
    existing_production = [str(path.relative_to(ROOT)) for path in RESERVED_PRODUCTION_PATHS if path.exists()]
    automation_root = PREEXISTING_CORE_RECOVERY_ROOT.parent
    unexpected_automation_children = []
    if automation_root.exists():
        unexpected_automation_children = [
            str(path.relative_to(ROOT))
            for path in automation_root.iterdir()
            if path.name != "CoreRecovery"
        ]
    audit.check(
        "G19_production_roots_absent",
        not existing_production
        and not unexpected_automation_children
        and PREEXISTING_CORE_RECOVERY_ROOT.is_dir(),
        {
            "existing_production": existing_production,
            "unexpected_automation_children": unexpected_automation_children,
            "preexisting_core_recovery_root": str(PREEXISTING_CORE_RECOVERY_ROOT.relative_to(ROOT)),
        },
    )

    future_paths = blueprint.get("future_paths", {})
    future_values = [
        value
        for key, value in future_paths.items()
        if key not in {"created_in_step11", "automation_root_preexisting_content"}
        and isinstance(value, str)
    ]
    bad_future_paths = [value for value in future_values if "A005" not in value or any(token in value for token in ("A001", "A002", "A003", "A004"))]
    audit.check("G20_future_paths", future_paths.get("created_in_step11") is False and not bad_future_paths, bad_future_paths)

    holdouts = vertices.get("holdouts", {})
    reviews = blueprint.get("review_views", [])
    review_ids = {record.get("id") for record in reviews}
    audit.check(
        "G21_holdouts_and_review_views",
        "validation only" in holdouts.get("back", "")
        and "validation only" in holdouts.get("right", "")
        and review_ids == {"RV-FRONT", "RV-BACK", "RV-LEFT", "RV-RIGHT", "RV-TOP", "RV-PERSPECTIVE"}
        and len(blueprint.get("validators", [])) == 10,
        {"holdouts": holdouts, "review_ids": sorted(str(value) for value in review_ids)},
    )

    blocked = blueprint.get("blocked_methods", [])
    required_block_fragments = ["A001-A004", "averaging", "projection shell", "shared exact contact loop", "DCC/geometry/texture/FBX/Unreal"]
    missing_blocks = [fragment for fragment in required_block_fragments if not any(fragment in item for item in blocked)]
    audit.check("G22_blocked_methods", len(blocked) >= 15 and not missing_blocks, {"count": len(blocked), "missing": missing_blocks})

    contract_text = CONTRACT.read_text(encoding="utf-8")
    audit.check(
        "G23_contract_boundary",
        CONTRACT_ID in contract_text
        and "Blender or DCC launch" in contract_text
        and "Step 12" in contract_text
        and "mandatory restart" in contract_text,
        "contract contains planning boundary, Step 12 stop, and restart",
    )

    changed = git_changed_paths()
    relevant_changed = {path for path in changed if path.startswith("docs/assets/blueprints/SM_GIA_BloodAxeCairnstone_A005/") or path == "Tools/DCC/audit_bloodaxe_cairnstone_a005_step11_blueprint.py"}
    outside_allowlist = sorted(relevant_changed - ALLOWED_CHANGED_PATHS)
    audit.check("G24_changed_path_allowlist", not outside_allowlist, {"relevant_changed": sorted(relevant_changed), "outside_allowlist": outside_allowlist})

    if args.phase == "final":
        assert validation is not None
        review_text = REVIEW.read_text(encoding="utf-8")
        output_text = OUTPUT.read_text(encoding="utf-8")
        handoff_text = HANDOFF.read_text(encoding="utf-8")
        audit.check(
            "G25_visible_review_boundary",
            "PLANNING ONLY" in review_text and "NO GEOMETRY" in review_text and CONTRACT_ID in review_text,
            "review packet labeling",
        )
        audit.check(
            "G26_output_and_handoff",
            "authoritative" in output_text
            and "Step 11 is complete" in output_text
            and "Step 12" in handoff_text
            and "mandatory restart" in handoff_text
            and "DCC" in handoff_text,
            "authoritative output and preparation-only Step 12 handoff",
        )
        audit.check(
            "G27_validation_record",
            validation.get("technical_result") == "pass_authoritative_step11_blueprint_complete_mandatory_restart"
            and validation.get("counts", {}).get("failed_gates") == 0
            and validation.get("scope", {}).get("production_outputs_created") == 0,
            validation,
        )

    result = {
        "schema": "aerathea.step11_blueprint_audit_result.v1",
        "asset_id": "SM_GIA_BloodAxeCairnstone_A005",
        "contract_id": CONTRACT_ID,
        "phase": args.phase,
        "technical_result": "pass" if not audit.failures else "fail_closed",
        "counts": {
            "gates": len(audit.gates),
            "passed": len(audit.gates) - len(audit.failures),
            "failed": len(audit.failures),
        },
        "gates": audit.gates,
    }
    print(json.dumps(result, indent=2, sort_keys=True))
    return 0 if not audit.failures else 1


if __name__ == "__main__":
    sys.exit(main())
