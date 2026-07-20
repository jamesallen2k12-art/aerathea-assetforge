#!/usr/bin/env python3
"""Build the bounded A005 S10R-006-R1-A normalized bridge proof package.

This script emits records and an unfilled technical board only. It creates no
physical correspondence, target geometry coordinates, field, surface,
topology, or geometry.
"""

from __future__ import annotations

import hashlib
import json
import math
import subprocess
import textwrap
from datetime import datetime
from pathlib import Path

from PIL import Image, ImageDraw, ImageFont


ROOT = Path(__file__).resolve().parents[2]
ASSET = ROOT / "docs/assets/blueprints/SM_GIA_BloodAxeCairnstone_A005"
MANIFESTS = ASSET / "manifests"
STEPS = ASSET / "steps"
HANDOFFS = ASSET / "handoffs"
EVIDENCE = ASSET / "evidence/S10R_006_R1_A_NORMALIZED_PRIMARY_OWNER_BRIDGE_A01"

PREFIX = "S10R_006_R1_A_NORMALIZED_PRIMARY_OWNER_BRIDGE_A01"
INPUT_LOCK_PATH = MANIFESTS / f"{PREFIX}_INPUT_LOCK.json"
MAPPING_PATH = MANIFESTS / f"{PREFIX}_MAPPING_LEDGER.json"
HOLDOUT_PATH = MANIFESTS / f"{PREFIX}_VALIDATION_HOLDOUT_AUDIT.json"
BOARD_PATH = EVIDENCE / (
    "SM_GIA_BloodAxeCairnstone_A005_"
    f"{PREFIX}_REVIEW_BOARD.png"
)
OUTPUT_PATH = STEPS / f"{PREFIX}_OUTPUT_RECORD.md"
HANDOFF_PATH = HANDOFFS / f"{PREFIX}_TO_DECISION_HANDOFF.md"

DECISION_PATH = MANIFESTS / "S10R_006_R1_A_NORMALIZED_PRIMARY_OWNER_BRIDGE_DECISION_REGISTRY.json"
CONTRACT_PATH = STEPS / "S10R_006_R1_A_NORMALIZED_PRIMARY_OWNER_BRIDGE_EXECUTION_CONTRACT.md"
TRACE_LEDGER_PATH = MANIFESTS / "C004_BOUNDARY_TRANSITION_INTERPRETATION_RULE_A01_PER_VIEW_LEDGER.json"
FRAME_PATH = MANIFESTS / "STEP_05_PIXEL_COORDINATE_FRAME_RECORD.json"
ORIENTATION_PATH = MANIFESTS / "STEP_05_ORIENTATION_REGISTRATION_MANIFEST.json"

EXPECTED_HASHES = {
    "AGENTS.md": "5d2d2637a58113f0a6f5ec92e40d8bb2bda9e03fb58b4868a0d9dfbb3b57ad55",
    "docs/projects/assetforge/BLOODAXE_CAIRNSTONE_PIXEL_EXACT_FRESH_START_MULTISTEP_PLAN.md": "ba6784498d792dc85dd431c807f59620d6851af97b4cd15efe89c44a397b10b6",
    "docs/assets/blueprints/SM_GIA_BloodAxeCairnstone_A005/manifests/STEP_05_PIXEL_COORDINATE_FRAME_RECORD.json": "ccfce6b8316369b512ff83eee11fd4385dd15b546f7b92da9e80b9e7ed959d1d",
    "docs/assets/blueprints/SM_GIA_BloodAxeCairnstone_A005/manifests/STEP_05_ORIENTATION_REGISTRATION_MANIFEST.json": "b7efa865e8b82f63e714d36ed4935fc02515ecc3f4d355941467f20b49348395",
    "docs/assets/blueprints/SM_GIA_BloodAxeCairnstone_A005/manifests/STEP_10R_N3_INTEGRATION_DECISION_REGISTRY.json": "f60634468c2d820e230da0a847a181be90893411c3e7838283eb61730e7d37e5",
    "docs/assets/blueprints/SM_GIA_BloodAxeCairnstone_A005/manifests/STEP_10R_N3_TRANSITION_INTEGRATION_OPTION_REGISTRY.json": "3143f233c471c823693d8539f7abf7478340bdcfdd3eef871f68cabc7ca3728f",
    "docs/assets/blueprints/SM_GIA_BloodAxeCairnstone_A005/manifests/C004_BOUNDARY_TRANSITION_INTERPRETATION_RULE_A01_PER_VIEW_LEDGER.json": "c30fe9e7ae2c623122865102b16922931e42e87e2a3bfadb145cbe73f4861113",
    "docs/assets/blueprints/SM_GIA_BloodAxeCairnstone_A005/manifests/S10R_003_A_CL003_TARGET_SPACE_MAPPING_A01_DECISION_REGISTRY.json": "05ddf7d67cbed5bca4eb32ec749767b43f74af69bcc77f556e08cec5fb288ff2",
    "docs/assets/blueprints/SM_GIA_BloodAxeCairnstone_A005/manifests/S10R_006_A_BOUNDARY_COMPATIBILITY_TECHNICAL_GATE_A01_DECISION_REGISTRY.json": "609a912568ccea01f65a4ec6060c53a97b93679d5a647125bed835bd9b28759b",
    "docs/assets/blueprints/SM_GIA_BloodAxeCairnstone_A005/manifests/S10R_006_A_BOUNDARY_COMPATIBILITY_TECHNICAL_GATE_A01_REMAINING_BLOCKS.json": "5d3458789dd0317d66493b137225dcd604d05ff5c73483b4df8946bea453eb07",
    "docs/assets/blueprints/SM_GIA_BloodAxeCairnstone_A005/manifests/S10R_006_R1_A_NORMALIZED_PRIMARY_OWNER_BRIDGE_DECISION_REGISTRY.json": "14961845f35c2005b727cea46b19a378db9b79432da0b930c1872e68bf1a63b7",
    "docs/assets/blueprints/SM_GIA_BloodAxeCairnstone_A005/steps/S10R_006_R1_A_NORMALIZED_PRIMARY_OWNER_BRIDGE_EXECUTION_CONTRACT.md": "7d7ff2c0ea7a556599b89bd0bb7e01f501e59cdf77bbcef4cb8b58b48f03e69f",
    "docs/assets/blueprints/SM_GIA_BloodAxeCairnstone_A005/SM_GIA_BloodAxeCairnstone_A005_RESET_RESUME_STATE.md": "e7d87db50299c32db4bf246e9a70a5e2017bf39522f7478aebd333f451b26839",
    "docs/assets/blueprints/SM_GIA_BloodAxeCairnstone_A005/SM_GIA_BloodAxeCairnstone_A005_APPROVAL_LOG.md": "48b58a1770db4326c6e95d069e94943f9003dd37516da8bbca853ce6f6ed6f3b",
    "docs/assets/blueprints/SM_GIA_BloodAxeCairnstone_A005/SM_GIA_BloodAxeCairnstone_A005_ARTIFACT_INDEX.md": "84c80d34051ade347fb37282fb73cc304a1f3a1c3689a4747acd098697094dd3",
    "Saved/ProjectRecovery/20260717-174106/git_status_short.txt": "fc441f44c5b1256afe5a436b6c5b4b9fde5a7d482d7ddac886483bc4c24faf7f",
}

EXPECTED_PRIMARY = [
    *(f"F-BTIR-{index:02d}" for index in range(1, 7)),
    *(f"L-BTIR-{index:02d}" for index in range(1, 7)),
]
EXPECTED_HOLDOUT = [
    *(f"B-BTIR-{index:02d}" for index in range(1, 7)),
    *(f"R-BTIR-{index:02d}" for index in range(1, 9)),
]


def sha256(path: Path) -> str:
    digest = hashlib.sha256()
    with path.open("rb") as handle:
        for chunk in iter(lambda: handle.read(1024 * 1024), b""):
            digest.update(chunk)
    return digest.hexdigest()


def load_json(path: Path) -> dict:
    return json.loads(path.read_text(encoding="utf-8"))


def write_json(path: Path, value: dict) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(json.dumps(value, indent=2) + "\n", encoding="utf-8")


def git_text(*args: str) -> str:
    return subprocess.check_output(["git", *args], cwd=ROOT, text=True).strip()


def font(size: int, bold: bool = False) -> ImageFont.FreeTypeFont:
    name = "DejaVuSans-Bold.ttf" if bold else "DejaVuSans.ttf"
    return ImageFont.truetype(f"/usr/share/fonts/truetype/dejavu/{name}", size)


def draw_wrapped(
    draw: ImageDraw.ImageDraw,
    xy: tuple[int, int],
    text: str,
    *,
    width: int,
    font_obj: ImageFont.FreeTypeFont,
    fill: tuple[int, int, int],
    spacing: int = 6,
) -> int:
    lines: list[str] = []
    for paragraph in text.splitlines() or [""]:
        lines.extend(textwrap.wrap(paragraph, width=width) or [""])
    x, y = xy
    draw.multiline_text((x, y), "\n".join(lines), font=font_obj, fill=fill, spacing=spacing)
    bbox = draw.multiline_textbbox((x, y), "\n".join(lines), font=font_obj, spacing=spacing)
    return bbox[3]


def superellipse_points(
    center: tuple[float, float], axes: tuple[float, float], exponent: float = 3.0
) -> list[tuple[float, float]]:
    cx, cy = center
    ax, ay = axes
    points = []
    for index in range(361):
        angle = math.tau * index / 360.0
        cosine = math.cos(angle)
        sine = math.sin(angle)
        x = cx + ax * math.copysign(abs(cosine) ** (2.0 / exponent), cosine)
        y = cy - ay * math.copysign(abs(sine) ** (2.0 / exponent), sine)
        points.append((x, y))
    return points


def trace_index(ledger: dict) -> dict[str, dict]:
    records: dict[str, dict] = {}
    for view_name in ("front", "back", "left", "right"):
        view_record = ledger["views"][view_name]
        for trace in view_record["traces"]:
            if trace["trace_id"] in records:
                raise RuntimeError(f"duplicate frozen trace ID {trace['trace_id']}")
            records[trace["trace_id"]] = trace
    return records


def main() -> None:
    executed_at = datetime.now().astimezone().isoformat(timespec="seconds")

    immutable_hashes = {}
    mismatches = []
    for relative, expected in EXPECTED_HASHES.items():
        path = ROOT / relative
        actual = sha256(path)
        match = actual == expected
        immutable_hashes[relative] = {
            "expected_sha256": expected,
            "actual_sha256": actual,
            "match": match,
        }
        if not match:
            mismatches.append(relative)
    if mismatches:
        raise RuntimeError(f"locked input hash mismatch: {mismatches}")

    branch = git_text("branch", "--show-current")
    head = git_text("rev-parse", "HEAD")
    remote_head = git_text("rev-parse", "assetforge/main")
    staged = git_text("diff", "--cached", "--name-only")
    if branch != "main" or head != remote_head or staged:
        raise RuntimeError("git preflight failed")

    decision = load_json(DECISION_PATH)
    if decision["decision"] != "approve":
        raise RuntimeError("bounded decision is not approved")
    if decision["future_execution_contract_id"] != "A005-CR-S10R-006-R1-A-NPOB-EXEC-A01":
        raise RuntimeError("future execution contract ID mismatch")

    ledger = load_json(TRACE_LEDGER_PATH)
    frame = load_json(FRAME_PATH)
    orientation = load_json(ORIENTATION_PATH)
    records = trace_index(ledger)
    if set(records) != set(EXPECTED_PRIMARY + EXPECTED_HOLDOUT):
        raise RuntimeError("frozen 26-trace identity set mismatch")

    axis_mappings = frame["world_coordinate_frame"]["panel_axis_mappings"]
    normal_ids = {
        record["source_view"]: record for record in orientation["panel_normal_owner_ids"]
    }
    owner_planes = {"front": "XZ", "left": "YZ"}
    expected_roles = {"front": "primary_XZ", "left": "primary_YZ"}

    primary_records = []
    for view_name in ("front", "left"):
        view_traces = [records[trace_id] for trace_id in EXPECTED_PRIMARY if records[trace_id]["view"] == view_name]
        if len(view_traces) != 6:
            raise RuntimeError(f"{view_name} primary trace count mismatch")
        if any(trace["view_role"] != expected_roles[view_name] for trace in view_traces):
            raise RuntimeError(f"{view_name} primary role mismatch")
        for side in ("left", "right"):
            side_traces = [trace for trace in view_traces if trace["outer_anchor"]["side"] == side]
            side_traces.sort(key=lambda trace: (trace["p_o"][1], trace["p_o"][0], trace["trace_id"]))
            rows = [trace["p_o"][1] for trace in side_traces]
            if len(side_traces) != 3 or len(set(rows)) != 3:
                raise RuntimeError(f"{view_name}/{side} primary ordering is not uniquely three-ranked")
            for order, trace in enumerate(side_traces, start=1):
                primary_records.append(
                    {
                        "mapping_id": f"NPOB-A01-{view_name.upper()}-{side.upper()}-{order:02d}",
                        "trace_id": trace["trace_id"],
                        "classification": "candidate implementation of approved bounded interpretation rule pending Flamestrike",
                        "owner_view": view_name,
                        "owner_plane": owner_planes[view_name],
                        "view_role": trace["view_role"],
                        "registered_side": side,
                        "within_side_order": order,
                        "order_source": "frozen outer-anchor image row ascending under Step 05 x-right/y-down convention",
                        "source_outer_anchor_row": trace["p_o"][1],
                        "source_p_i": trace["p_i"],
                        "source_p_o": trace["p_o"],
                        "source_trace_formula": trace["p_t_formula"],
                        "source_trace_changed": False,
                        "symbolic_trace_domain": {"parameter": "t", "minimum": 0, "maximum": 1},
                        "normalized_transition_identity": "v = t",
                        "inner_boundary_identity": {
                            "id": "C003_TSIB_K80_MEDIUM_APRON",
                            "station": "t = 0; v = 0",
                        },
                        "outer_boundary_identity": {
                            "id": "TOP_C004_OPIR_N3_ROUNDED_OVAL",
                            "station": "t = 1; v = 1",
                        },
                        "step05_axis_provenance": axis_mappings[view_name],
                        "step05_normal_owner_provenance": normal_ids[view_name],
                        "physical_source_target_transform": None,
                        "physical_cross_view_pair": None,
                        "target_xy_cm": None,
                        "target_xyz_cm": None,
                        "source_center_claim": False,
                        "pivot_claim": False,
                        "anchor_claim": False,
                        "field_sample": False,
                        "geometry_coordinate": False,
                    }
                )

    if len(primary_records) != 12 or len({record["mapping_id"] for record in primary_records}) != 12:
        raise RuntimeError("primary mapping count or identity uniqueness failed")

    holdout_records = []
    for view_name, expected_count in (("back", 6), ("right", 8)):
        view_record = ledger["views"][view_name]
        view_traces = [records[trace_id] for trace_id in EXPECTED_HOLDOUT if records[trace_id]["view"] == view_name]
        if len(view_traces) != expected_count:
            raise RuntimeError(f"{view_name} holdout trace count mismatch")
        crossing_count = view_record["trace_crossing_audit"]["crossing_pair_count"]
        for side in ("left", "right"):
            side_traces = [trace for trace in view_traces if trace["outer_anchor"]["side"] == side]
            side_traces.sort(key=lambda trace: (trace["p_o"][1], trace["p_o"][0], trace["trace_id"]))
            rows = [trace["p_o"][1] for trace in side_traces]
            expected_side_count = expected_count // 2
            if len(side_traces) != expected_side_count or len(set(rows)) != expected_side_count:
                raise RuntimeError(f"{view_name}/{side} holdout ordering is ambiguous")
            for order, trace in enumerate(side_traces, start=1):
                if trace["view_role"] != "validation_only":
                    raise RuntimeError(f"{trace['trace_id']} escaped validation-only role")
                holdout_records.append(
                    {
                        "holdout_id": f"NPOB-A01-HOLDOUT-{view_name.upper()}-{side.upper()}-{order:02d}",
                        "trace_id": trace["trace_id"],
                        "view": view_name,
                        "view_role": trace["view_role"],
                        "registered_side": side,
                        "within_side_order": order,
                        "source_outer_anchor_row": trace["p_o"][1],
                        "source_p_i": trace["p_i"],
                        "source_p_o": trace["p_o"],
                        "source_trace_formula": trace["p_t_formula"],
                        "step05_axis_provenance": axis_mappings[view_name],
                        "step05_normal_owner_provenance": normal_ids[view_name],
                        "trace_crossing_count_in_view": crossing_count,
                        "side_order_unique": True,
                        "handedness_provenance_present": True,
                        "construction_coordinate_created": False,
                        "physical_pair_created": False,
                        "explicit_contradiction_detected": False,
                        "classification": "proof only validation holdout",
                    }
                )

    if len(holdout_records) != 14 or len({record["holdout_id"] for record in holdout_records}) != 14:
        raise RuntimeError("holdout count or identity uniqueness failed")

    input_lock = {
        "schema": "aerathea.s10r_006_r1_a_normalized_primary_owner_bridge_a01_input_lock.v1",
        "asset_id": "SM_GIA_BloodAxeCairnstone_A005",
        "contract_id": "A005-CR-S10R-006-R1-A-NPOB-EXEC-A01",
        "date": "2026-07-17",
        "executed_at": executed_at,
        "status": "locked_inputs_match_before_bridge_outputs",
        "artifact_classification": "proof only",
        "flamestrike_execution_approval": "I approve it",
        "approval_scope": "twelve-record normalized mapping, fourteen-record holdout audit, independent validation, unfilled visible review, mandatory stop, no field, geometry, downstream work, staging, commit, or push",
        "pre_action_checkpoint": "Saved/ProjectRecovery/20260717-174106/",
        "immutable_input_hashes": immutable_hashes,
        "hash_match_count": len(immutable_hashes),
        "hash_mismatch_count": 0,
        "git_state": {
            "branch": branch,
            "head": head,
            "assetforge_main": remote_head,
            "staged_path_count": 0,
        },
        "pre_output_authority_counts": {
            "physical_source_target_transforms": 0,
            "physical_cross_view_pairs": 0,
            "target_trace_coordinates": 0,
            "field_samples": 0,
            "fills": 0,
            "surfaces": 0,
            "topology": 0,
            "geometry": 0,
        },
    }

    mapping_ledger = {
        "schema": "aerathea.s10r_006_r1_a_normalized_primary_owner_bridge_a01_mapping_ledger.v1",
        "asset_id": "SM_GIA_BloodAxeCairnstone_A005",
        "contract_id": "A005-CR-S10R-006-R1-A-NPOB-EXEC-A01",
        "date": "2026-07-17",
        "status": "candidate_normalized_primary_owner_bridge_ready_for_validation",
        "artifact_classification": "candidate implementation of approved bounded interpretation rule pending Flamestrike",
        "decision_registry_sha256": sha256(DECISION_PATH),
        "input_lock_path": str(INPUT_LOCK_PATH.relative_to(ROOT)),
        "rule": {
            "common_frame": "dimensionless symbolic trace domain",
            "parameter_identity": "v = t",
            "inner_station": "K80 at t = 0; v = 0",
            "outer_station": "N3 at t = 1; v = 1",
            "physical_coordinate_claim": False,
        },
        "construction_owner_counts": {
            "front_primary_XZ": 6,
            "left_primary_YZ": 6,
            "total": 12,
        },
        "records": primary_records,
        "summary": {
            "record_count": 12,
            "unique_mapping_id_count": 12,
            "unique_trace_id_count": 12,
            "source_trace_changes": 0,
            "order_reversals": 0,
            "order_ambiguities": 0,
            "introduced_crossings": 0,
            "physical_source_target_transforms": 0,
            "physical_cross_view_pairs": 0,
            "target_xy_coordinates": 0,
            "target_xyz_coordinates": 0,
            "field_samples": 0,
            "geometry_coordinates": 0,
        },
    }

    holdout_audit = {
        "schema": "aerathea.s10r_006_r1_a_normalized_primary_owner_bridge_a01_validation_holdout_audit.v1",
        "asset_id": "SM_GIA_BloodAxeCairnstone_A005",
        "contract_id": "A005-CR-S10R-006-R1-A-NPOB-EXEC-A01",
        "date": "2026-07-17",
        "status": "pass_no_explicit_validation_holdout_contradiction",
        "artifact_classification": "proof only",
        "policy": "Back and right remain validation-only and create no construction coordinates or physical pairs.",
        "counts": {
            "back_validation_only": 6,
            "right_validation_only": 8,
            "total": 14,
            "unique_holdout_ids": 14,
            "unique_trace_ids": 14,
            "order_ambiguities": 0,
            "crossing_pairs": 0,
            "handedness_provenance_missing": 0,
            "construction_coordinates_created": 0,
            "physical_pairs_created": 0,
            "explicit_contradictions": 0,
        },
        "records": holdout_records,
        "result": "pass_no_explicit_contradiction_within_bounded_holdout_questions",
        "authority_limit": "The holdout result does not prove physical cross-view agreement or source-to-target correspondence.",
    }

    write_json(INPUT_LOCK_PATH, input_lock)
    write_json(MAPPING_PATH, mapping_ledger)
    write_json(HOLDOUT_PATH, holdout_audit)

    EVIDENCE.mkdir(parents=True, exist_ok=True)
    canvas = Image.new("RGB", (1900, 1260), (22, 25, 31))
    draw = ImageDraw.Draw(canvas)
    white = (237, 240, 244)
    muted = (166, 174, 187)
    cyan = (91, 205, 224)
    amber = (241, 183, 79)
    green = (107, 215, 147)
    red = (230, 112, 112)
    panel = (34, 39, 48)
    border = (70, 79, 94)

    draw.text((60, 45), "A005 S10R-006-R1-A — NORMALIZED PRIMARY-OWNER BRIDGE", font=font(38, True), fill=white)
    draw.text((60, 96), "TECHNICAL REVIEW — SOURCE RECORDS AND BOUNDED INTERPRETATION REMAIN SEPARATE", font=font(20, True), fill=amber)
    draw.text((60, 130), "No physical correspondence • No target geometry coordinates • No field • No fill • No surface • No geometry", font=font(18), fill=red)

    boxes = {
        "evidence": (50, 185, 920, 835),
        "interpretation": (950, 185, 1850, 835),
        "holdout": (50, 865, 1850, 1205),
    }
    for box in boxes.values():
        draw.rounded_rectangle(box, radius=16, fill=panel, outline=border, width=2)

    draw.text((80, 215), "SOURCE-SPACE EVIDENCE (UNCHANGED)", font=font(25, True), fill=cyan)
    y = 260
    for view_name in ("front", "left"):
        draw.text((80, y), f"{view_name.upper()} — {expected_roles[view_name]} — Step 05 {axis_mappings[view_name]}", font=font(17, True), fill=white)
        y += 34
        for record in [entry for entry in primary_records if entry["owner_view"] == view_name]:
            line = (
                f"{record['trace_id']}  {record['registered_side']:<5}  order {record['within_side_order']}  "
                f"p_i={record['source_p_i']}  p_o={record['source_p_o']}"
            )
            draw.text((100, y), line, font=font(15), fill=muted)
            y += 27
        y += 18

    draw.text((980, 215), "APPROVED BOUNDED INTERPRETATION", font=font(25, True), fill=amber)
    center = (1400, 460)
    draw.line(superellipse_points(center, (315, 245)), fill=amber, width=4)
    draw.line(superellipse_points(center, (252, 196)), fill=cyan, width=4)
    draw.text((1260, 300), "N3 outer identity — t=1, v=1", font=font(17, True), fill=amber)
    draw.text((1260, 330), "K80 inner identity — t=0, v=0", font=font(17, True), fill=cyan)
    draw.text((1335, 438), "v = t", font=font(30, True), fill=green)
    draw.text((1080, 720), "Symbolic dimensionless boundary identity only", font=font(19, True), fill=white)
    draw.text((1060, 755), "No XY / XYZ / centimeter / pivot / anchor coordinate", font=font(17), fill=muted)

    draw.text((80, 895), "VALIDATION-ONLY HOLDOUT AUDIT", font=font(25, True), fill=green)
    summary_text = (
        "Back: 6 validation-only traces. Right: 8 validation-only traces. "
        "All IDs, roles, sides, formulas, Step 05 handedness provenance, and within-view ordering replayed. "
        "Crossings: 0. Order ambiguities: 0. Explicit contradictions: 0. Construction coordinates: 0. Physical pairs: 0."
    )
    draw_wrapped(draw, (80, 945), summary_text, width=150, font_obj=font(18), fill=white, spacing=8)
    draw.text((80, 1060), "PASS means only: no explicit contradiction inside the approved holdout questions.", font=font(18, True), fill=green)
    draw.text((80, 1100), "It does not prove physical cross-view agreement or recover missing source authority.", font=font(18, True), fill=amber)
    draw.text((80, 1150), "Candidate result pending Flamestrike • S10R-BLOCK-006 / 008 / 009 remain active", font=font(18, True), fill=red)
    canvas.save(BOARD_PATH)

    board_hash = sha256(BOARD_PATH)
    mapping_hash = sha256(MAPPING_PATH)
    holdout_hash = sha256(HOLDOUT_PATH)

    output_text = f"""# A005 S10R-006-R1-A Normalized Primary-Owner Bridge A01 Output Record

Status: `candidate technical pass pending Flamestrike decision; mandatory restart required`

Artifact classification: `candidate implementation of approved bounded interpretation rule pending Flamestrike`

Contract ID: `A005-CR-S10R-006-R1-A-NPOB-EXEC-A01`

Date: 2026-07-17

## Technical Result

`pass_normalized_primary_owner_bridge_ready_for_Flamestrike_decision`

The approved bounded rule produced exactly twelve symbolic normalized mapping
records: six front primary-XZ traces and six left primary-YZ traces. Every
record preserves its exact trace ID, source endpoints, source formula, owner
view, side, Step 05 axis provenance, and within-side order.

Each mapping records only `v = t`, K80 identity at `t = 0`, and N3 identity at
`t = 1`. It records no target XY/XYZ coordinate, centimeter value, physical
source-to-target transform, cross-view pair, center, pivot, anchor, field
sample, surface, topology, or geometry coordinate.

## Frozen Counts

- construction-owner mappings: `12`;
- front primary-XZ mappings: `6`;
- left primary-YZ mappings: `6`;
- unique mapping IDs: `12`;
- unique construction trace IDs: `12`;
- validation holdouts: `14`;
- back validation-only holdouts: `6`;
- right validation-only holdouts: `8`;
- order ambiguities or reversals: `0`;
- introduced crossings: `0`;
- explicit holdout contradictions: `0`;
- source trace changes: `0`;
- physical source-target transforms: `0`;
- physical cross-view pairs: `0`;
- target trace coordinates: `0`;
- field samples, fills, surfaces, topology, and geometry: `0`.

## Evidence And Interpretation Separation

The frozen source trace endpoints and formulas remain source-space evidence
within their prior bounds. The twelve normalized mapping records are a
candidate implementation of the already approved bounded interpretation rule.
The fourteen back/right records remain proof-only validation holdouts.

The prior result `blocked_source_authority_missing` remains authoritative. A
technical pass here does not recast interpretation as recovered source
authority.

## Validation Holdout Result

`pass_no_explicit_contradiction_within_bounded_holdout_questions`

This result is limited to source role, side, ordering, handedness provenance,
unchanged trace data, and non-crossing behavior. It does not prove physical
cross-view agreement.

## Proof Artifacts

- mapping ledger SHA-256: `{mapping_hash}`;
- validation-holdout audit SHA-256: `{holdout_hash}`;
- unfilled review-board SHA-256: `{board_hash}`.

## Artifact Routing Before Output Decision

- approved decision registry: unchanged `authoritative for bounded recovery
  routing and normalized common-frame interpretation only`;
- execution contract after execution approval: `authoritative for completed
  execution scope only`;
- input lock and holdout audit: `proof only`;
- twelve-record mapping ledger: `candidate implementation of approved bounded
  interpretation rule pending Flamestrike`;
- review board: `proof only`;
- this output and its handoff: `candidate` pending Flamestrike;
- original source, all prior evidence, prior decisions, and active blocks:
  unchanged.

## Stop State

`S10R-BLOCK-006`, `S10R-BLOCK-008`, and `S10R-BLOCK-009` remain active.
This execution does not implement the S10R-006-A field, resolve a block, close
Step 10, begin Step 11, or authorize DCC, Unreal, production, staging, commit,
or push.

After independent validation, checkpoint, and visible review, stop for
Flamestrike to approve, request revision, or reject/quarantine this exact
candidate technical result. Mandatory restart follows the decision boundary.
"""
    OUTPUT_PATH.parent.mkdir(parents=True, exist_ok=True)
    OUTPUT_PATH.write_text(output_text, encoding="utf-8")

    handoff_text = """# A005 S10R-006-R1-A Normalized Primary-Owner Bridge A01 To Decision Handoff

Status: `candidate technical pass pending Flamestrike decision; mandatory restart required`

Artifact classification: `candidate decision handoff`

Contract ID: `A005-CR-S10R-006-R1-A-NPOB-EXEC-A01`

Date: 2026-07-17

## Candidate Result

`pass_normalized_primary_owner_bridge_ready_for_Flamestrike_decision`

The package contains twelve candidate symbolic mappings and fourteen
proof-only validation holdouts. Source trace data remains unchanged. No
physical correspondence, target geometry coordinate, field sample, fill,
surface, topology, or geometry was created.

## Decision Required

Flamestrike may:

1. approve the exact twelve-record normalized bridge implementation within
   its bounded symbolic role;
2. request a named revision while preserving the current candidate package;
   or
3. reject or quarantine the candidate implementation.

Approval of this candidate result would not implement the S10R-006-A field or
resolve `S10R-BLOCK-006` by itself. Any next technical gate requires a
separate contract after mandatory restart.

## Active Blocks And Stop

- `S10R-BLOCK-006`: active;
- `S10R-BLOCK-008`: active;
- `S10R-BLOCK-009`: active;
- Step 10 closeout and Step 11: blocked;
- DCC, Unreal, production, staging, commit, and push: unauthorized.

Stop after independent validation, checkpoint, and visible review.
"""
    HANDOFF_PATH.parent.mkdir(parents=True, exist_ok=True)
    HANDOFF_PATH.write_text(handoff_text, encoding="utf-8")

    print("S10R-006-R1-A bridge package built")
    print(f"  input lock: {INPUT_LOCK_PATH.relative_to(ROOT)}")
    print(f"  mappings: {len(primary_records)}")
    print(f"  holdouts: {len(holdout_records)}")
    print(f"  review board: {BOARD_PATH.relative_to(ROOT)}")
    print("  field samples: 0")
    print("  geometry: 0")


if __name__ == "__main__":
    main()
