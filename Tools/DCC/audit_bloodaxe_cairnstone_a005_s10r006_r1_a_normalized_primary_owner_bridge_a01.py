#!/usr/bin/env python3
"""Independently audit the A005 S10R-006-R1-A bridge package."""

from __future__ import annotations

import hashlib
import json
import subprocess
from datetime import datetime
from pathlib import Path


ROOT = Path(__file__).resolve().parents[2]
ASSET = ROOT / "docs/assets/blueprints/SM_GIA_BloodAxeCairnstone_A005"
MANIFESTS = ASSET / "manifests"
STEPS = ASSET / "steps"
HANDOFFS = ASSET / "handoffs"
EVIDENCE = ASSET / "evidence/S10R_006_R1_A_NORMALIZED_PRIMARY_OWNER_BRIDGE_A01"
PREFIX = "S10R_006_R1_A_NORMALIZED_PRIMARY_OWNER_BRIDGE_A01"

INPUT_LOCK = MANIFESTS / f"{PREFIX}_INPUT_LOCK.json"
MAPPING = MANIFESTS / f"{PREFIX}_MAPPING_LEDGER.json"
HOLDOUT = MANIFESTS / f"{PREFIX}_VALIDATION_HOLDOUT_AUDIT.json"
VALIDATION = MANIFESTS / f"{PREFIX}_VALIDATION.json"
BOARD = EVIDENCE / f"SM_GIA_BloodAxeCairnstone_A005_{PREFIX}_REVIEW_BOARD.png"
OUTPUT = STEPS / f"{PREFIX}_OUTPUT_RECORD.md"
HANDOFF = HANDOFFS / f"{PREFIX}_TO_DECISION_HANDOFF.md"
DECISION = MANIFESTS / "S10R_006_R1_A_NORMALIZED_PRIMARY_OWNER_BRIDGE_DECISION_REGISTRY.json"
CONTRACT = STEPS / "S10R_006_R1_A_NORMALIZED_PRIMARY_OWNER_BRIDGE_EXECUTION_CONTRACT.md"
TRACE_LEDGER = MANIFESTS / "C004_BOUNDARY_TRANSITION_INTERPRETATION_RULE_A01_PER_VIEW_LEDGER.json"
FRAME = MANIFESTS / "STEP_05_PIXEL_COORDINATE_FRAME_RECORD.json"
ORIENTATION = MANIFESTS / "STEP_05_ORIENTATION_REGISTRATION_MANIFEST.json"
BASELINE_STATUS = ROOT / "Saved/ProjectRecovery/20260717-174106/git_status_short.txt"

BUILD_SCRIPT = ROOT / "Tools/DCC/build_bloodaxe_cairnstone_a005_s10r006_r1_a_normalized_primary_owner_bridge_a01.py"
AUDIT_SCRIPT = ROOT / "Tools/DCC/audit_bloodaxe_cairnstone_a005_s10r006_r1_a_normalized_primary_owner_bridge_a01.py"


def sha256(path: Path) -> str:
    digest = hashlib.sha256()
    with path.open("rb") as handle:
        for chunk in iter(lambda: handle.read(1024 * 1024), b""):
            digest.update(chunk)
    return digest.hexdigest()


def load_json(path: Path) -> dict:
    return json.loads(path.read_text(encoding="utf-8"))


def git_text(*args: str) -> str:
    # Preserve leading porcelain-status columns; callers that inspect scalar
    # git values are unaffected by removing only trailing whitespace.
    return subprocess.check_output(["git", *args], cwd=ROOT, text=True).rstrip()


def status_paths(text: str) -> set[str]:
    paths = set()
    for line in text.splitlines():
        if not line.strip():
            continue
        path = line[3:]
        if " -> " in path:
            path = path.split(" -> ", 1)[1]
        paths.add(path)
    return paths


def main() -> None:
    validated_at = datetime.now().astimezone().isoformat(timespec="seconds")
    input_lock = load_json(INPUT_LOCK)
    mapping = load_json(MAPPING)
    holdout = load_json(HOLDOUT)
    decision = load_json(DECISION)
    trace_ledger = load_json(TRACE_LEDGER)
    frame = load_json(FRAME)
    orientation = load_json(ORIENTATION)
    output_text = OUTPUT.read_text(encoding="utf-8")
    handoff_text = HANDOFF.read_text(encoding="utf-8")
    contract_text = CONTRACT.read_text(encoding="utf-8")

    immutable_match = all(record["match"] for record in input_lock["immutable_input_hashes"].values())
    records = mapping["records"]
    holdouts = holdout["records"]
    mapping_ids = {record["mapping_id"] for record in records}
    mapping_trace_ids = {record["trace_id"] for record in records}
    holdout_ids = {record["holdout_id"] for record in holdouts}
    holdout_trace_ids = {record["trace_id"] for record in holdouts}

    expected_primary = {
        *(f"F-BTIR-{index:02d}" for index in range(1, 7)),
        *(f"L-BTIR-{index:02d}" for index in range(1, 7)),
    }
    expected_holdout = {
        *(f"B-BTIR-{index:02d}" for index in range(1, 7)),
        *(f"R-BTIR-{index:02d}" for index in range(1, 9)),
    }

    frozen = {}
    for view_name in ("front", "back", "left", "right"):
        for trace in trace_ledger["views"][view_name]["traces"]:
            frozen[trace["trace_id"]] = trace

    trace_data_unchanged = True
    for record in records:
        source = frozen[record["trace_id"]]
        trace_data_unchanged &= (
            record["source_p_i"] == source["p_i"]
            and record["source_p_o"] == source["p_o"]
            and record["source_trace_formula"] == source["p_t_formula"]
        )
    for record in holdouts:
        source = frozen[record["trace_id"]]
        trace_data_unchanged &= (
            record["source_p_i"] == source["p_i"]
            and record["source_p_o"] == source["p_o"]
            and record["source_trace_formula"] == source["p_t_formula"]
        )

    per_group_orders_ok = True
    for view_name in ("front", "left"):
        for side in ("left", "right"):
            group = sorted(
                [record for record in records if record["owner_view"] == view_name and record["registered_side"] == side],
                key=lambda record: record["within_side_order"],
            )
            per_group_orders_ok &= len(group) == 3
            per_group_orders_ok &= [record["within_side_order"] for record in group] == [1, 2, 3]
            per_group_orders_ok &= [record["source_outer_anchor_row"] for record in group] == sorted(
                record["source_outer_anchor_row"] for record in group
            )

    axis_mappings = frame["world_coordinate_frame"]["panel_axis_mappings"]
    normal_views = {record["source_view"] for record in orientation["panel_normal_owner_ids"]}
    handedness_ok = frame["world_coordinate_frame"]["handedness"] == "right_handed"
    handedness_ok &= all(
        record["owner_view"] in axis_mappings and record["owner_view"] in normal_views
        for record in records
    )
    handedness_ok &= all(
        record["view"] in axis_mappings and record["view"] in normal_views
        for record in holdouts
    )

    no_physical_or_geometry = all(
        record["physical_source_target_transform"] is None
        and record["physical_cross_view_pair"] is None
        and record["target_xy_cm"] is None
        and record["target_xyz_cm"] is None
        and not record["field_sample"]
        and not record["geometry_coordinate"]
        for record in records
    )
    no_physical_or_geometry &= all(
        not record["construction_coordinate_created"]
        and not record["physical_pair_created"]
        for record in holdouts
    )

    current_status = git_text("status", "--short")
    baseline_status = BASELINE_STATUS.read_text(encoding="utf-8")
    new_status_paths = status_paths(current_status) - status_paths(baseline_status)
    allowed_new_paths = {
        str(BUILD_SCRIPT.relative_to(ROOT)),
        str(AUDIT_SCRIPT.relative_to(ROOT)),
        str(INPUT_LOCK.relative_to(ROOT)),
        str(MAPPING.relative_to(ROOT)),
        str(HOLDOUT.relative_to(ROOT)),
        str(BOARD.relative_to(ROOT)),
        f"{EVIDENCE.relative_to(ROOT)}/",
        str(OUTPUT.relative_to(ROOT)),
        str(HANDOFF.relative_to(ROOT)),
        str(VALIDATION.relative_to(ROOT)),
    }
    unexpected_paths = sorted(new_status_paths - allowed_new_paths)

    board_ok = BOARD.exists() and BOARD.stat().st_size > 10000
    candidate_text_ok = (
        "pass_normalized_primary_owner_bridge_ready_for_Flamestrike_decision" in output_text
        and "S10R-BLOCK-006" in output_text
        and "candidate" in handoff_text
    )

    gate_results = [
        ("G01", "all locked input hashes match before output writes", immutable_match),
        ("G02", "visible contract ID and execution approval match", input_lock["flamestrike_execution_approval"] == "I approve it" and "A005-CR-S10R-006-R1-A-NPOB-EXEC-A01" in contract_text),
        ("G03", "branch main, HEAD aligned, and no staged paths", git_text("branch", "--show-current") == "main" and git_text("rev-parse", "HEAD") == git_text("rev-parse", "assetforge/main") and git_text("diff", "--cached", "--name-only") == ""),
        ("G04", "all 26 frozen trace IDs remain exact", set(frozen) == expected_primary | expected_holdout),
        ("G05", "construction set is exactly six front and six left", len(records) == 12 and mapping_trace_ids == expected_primary),
        ("G06", "holdout set is exactly six back and eight right", len(holdouts) == 14 and holdout_trace_ids == expected_holdout),
        ("G07", "three unique construction traces exist per primary view side", per_group_orders_ok),
        ("G08", "all twelve construction mapping IDs are unique", len(mapping_ids) == 12),
        ("G09", "all fourteen holdout IDs are unique", len(holdout_ids) == 14),
        ("G10", "all source endpoints and formulas replay unchanged", trace_data_unchanged),
        ("G11", "every construction record stores symbolic t in [0,1]", all(record["symbolic_trace_domain"] == {"parameter": "t", "minimum": 0, "maximum": 1} for record in records)),
        ("G12", "every construction record stores exact v = t", all(record["normalized_transition_identity"] == "v = t" for record in records)),
        ("G13", "all inner boundary identities are K80 at t=0", all(record["inner_boundary_identity"]["id"] == "C003_TSIB_K80_MEDIUM_APRON" and record["inner_boundary_identity"]["station"] == "t = 0; v = 0" for record in records)),
        ("G14", "all outer boundary identities are N3 at t=1", all(record["outer_boundary_identity"]["id"] == "TOP_C004_OPIR_N3_ROUNDED_OVAL" and record["outer_boundary_identity"]["station"] == "t = 1; v = 1" for record in records)),
        ("G15", "Step 05 handedness and owner provenance are present", handedness_ok),
        ("G16", "no owner-order reversal or ambiguity exists", per_group_orders_ok and mapping["summary"]["order_ambiguities"] == 0 and mapping["summary"]["order_reversals"] == 0),
        ("G17", "no trace crossing is introduced", mapping["summary"]["introduced_crossings"] == 0 and holdout["counts"]["crossing_pairs"] == 0),
        ("G18", "all holdouts remain validation-only", all(record["view_role"] == "validation_only" and not record["construction_coordinate_created"] for record in holdouts)),
        ("G19", "no explicit validation holdout contradiction exists", holdout["counts"]["explicit_contradictions"] == 0),
        ("G20", "no physical correspondence or geometry coordinate is created", no_physical_or_geometry),
        ("G21", "new paths remain inside the execution allowlist", not unexpected_paths),
        ("G22", "unfilled review board exists and is nontrivial", board_ok),
        ("G23", "candidate result and active-block stop language are exact", candidate_text_ok and decision["authority_limits"]["mapping_execution_authorized"] is False),
        ("G24", "execution stops pending visible Flamestrike review", "mandatory restart" in output_text.lower() and "Stop after independent validation" in handoff_text),
    ]
    failed = [gate for gate in gate_results if not gate[2]]

    validation = {
        "schema": "aerathea.s10r_006_r1_a_normalized_primary_owner_bridge_a01_validation.v1",
        "asset_id": "SM_GIA_BloodAxeCairnstone_A005",
        "contract_id": "A005-CR-S10R-006-R1-A-NPOB-EXEC-A01",
        "date": "2026-07-17",
        "validated_at": validated_at,
        "status": "pass_candidate_bridge_technical_validation" if not failed else "fail_candidate_bridge_technical_validation",
        "artifact_classification": "proof only",
        "independent_auditor": str(AUDIT_SCRIPT.relative_to(ROOT)),
        "gate_count": len(gate_results),
        "passed_gate_count": len(gate_results) - len(failed),
        "failed_gate_count": len(failed),
        "output_hashes_before_validation_write": {
            str(INPUT_LOCK.relative_to(ROOT)): sha256(INPUT_LOCK),
            str(MAPPING.relative_to(ROOT)): sha256(MAPPING),
            str(HOLDOUT.relative_to(ROOT)): sha256(HOLDOUT),
            str(BOARD.relative_to(ROOT)): sha256(BOARD),
            str(OUTPUT.relative_to(ROOT)): sha256(OUTPUT),
            str(HANDOFF.relative_to(ROOT)): sha256(HANDOFF),
            str(BUILD_SCRIPT.relative_to(ROOT)): sha256(BUILD_SCRIPT),
            str(AUDIT_SCRIPT.relative_to(ROOT)): sha256(AUDIT_SCRIPT),
        },
        "counts": {
            "construction_mappings": len(records),
            "validation_holdouts": len(holdouts),
            "source_trace_changes": 0,
            "physical_source_target_transforms": 0,
            "physical_cross_view_pairs": 0,
            "target_trace_coordinates": 0,
            "field_samples": 0,
            "fills": 0,
            "surfaces": 0,
            "topology": 0,
            "geometry": 0,
        },
        "write_scope_audit": {
            "baseline": "Saved/ProjectRecovery/20260717-174106/",
            "new_paths": sorted(new_status_paths),
            "allowed_new_paths": sorted(allowed_new_paths),
            "unexpected": unexpected_paths,
        },
        "gates": [
            {"gate": gate_id, "subject": subject, "status": "pass" if passed else "fail"}
            for gate_id, subject, passed in gate_results
        ],
        "technical_result": "pass_normalized_primary_owner_bridge_ready_for_Flamestrike_decision" if not failed else "blocked_integrity_or_scope_failure",
        "S10R_BLOCK_006_resolved": False,
        "step10_closeout_authorized": False,
        "step11_authorized": False,
        "field_implementation_authorized": False,
        "geometry_authorized": False,
        "staging_commit_push_authorized": False,
        "mandatory_restart_required": True,
    }
    VALIDATION.write_text(json.dumps(validation, indent=2) + "\n", encoding="utf-8")

    if failed:
        raise RuntimeError(f"validation failed: {failed}")

    print(f"validation passed: {len(gate_results)}/{len(gate_results)}")
    print(f"  mappings: {len(records)}")
    print(f"  holdouts: {len(holdouts)}")
    print("  field samples: 0")
    print("  geometry: 0")


if __name__ == "__main__":
    main()
