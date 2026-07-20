#!/usr/bin/env python3
"""Build the record-only A005 S10R-006-A boundary compatibility audit.

The script replays approved records.  It never creates a field sample,
source/target correspondence, fill, surface, topology, or geometry.
"""

from __future__ import annotations

import hashlib
import json
import math
from datetime import datetime
from pathlib import Path

from PIL import Image, ImageDraw, ImageFont


ROOT = Path(__file__).resolve().parents[2]
ASSET_REL = Path("docs/assets/blueprints/SM_GIA_BloodAxeCairnstone_A005")
ASSET = ROOT / ASSET_REL
MANIFESTS = ASSET / "manifests"
STEPS = ASSET / "steps"
EVIDENCE = ASSET / "evidence/S10R_006_A_BOUNDARY_COMPATIBILITY_TECHNICAL_GATE_A01"

CONTRACT_ID = "A005-CR-S10R-006-A-BCTG-A01"
CONTRACT = STEPS / "S10R_006_A_BOUNDARY_COMPATIBILITY_TECHNICAL_GATE_A01_CONTRACT.md"
INPUT_LOCK = MANIFESTS / "S10R_006_A_BOUNDARY_COMPATIBILITY_TECHNICAL_GATE_A01_INPUT_LOCK.json"
DEPENDENCY = MANIFESTS / "S10R_006_A_BOUNDARY_COMPATIBILITY_TECHNICAL_GATE_A01_DEPENDENCY_AUDIT.json"
BOUNDARY = MANIFESTS / "S10R_006_A_BOUNDARY_COMPATIBILITY_TECHNICAL_GATE_A01_BOUNDARY_AUTHORITY_AUDIT.json"
BOARD = EVIDENCE / "SM_GIA_BloodAxeCairnstone_A005_S10R_006_A_BOUNDARY_COMPATIBILITY_TECHNICAL_GATE_A01_REVIEW_BOARD.png"

PLACEMENT = MANIFESTS / "STEP_10R_N3_PLACEMENT_MAPPING_OPTION_REGISTRY.json"
TRANSITION = MANIFESTS / "STEP_10R_N3_TRANSITION_INTEGRATION_OPTION_REGISTRY.json"
DECISIONS = MANIFESTS / "STEP_10R_N3_INTEGRATION_DECISION_REGISTRY.json"
TRACE_LEDGER = MANIFESTS / "C004_BOUNDARY_TRANSITION_INTERPRETATION_RULE_A01_PER_VIEW_LEDGER.json"
K80 = MANIFESTS / "C003_TARGET_SPACE_INNER_BOUNDARY_INTERPRETATION_RULE_A02_K80_DECISION_REGISTRY.json"
MAPPING = MANIFESTS / "S10R_003_A_CL003_TARGET_SPACE_MAPPING_A01_DECISION_REGISTRY.json"

EXPECTED_HASHES = {
    "AGENTS.md": "5d2d2637a58113f0a6f5ec92e40d8bb2bda9e03fb58b4868a0d9dfbb3b57ad55",
    "docs/projects/assetforge/BLOODAXE_CAIRNSTONE_PIXEL_EXACT_FRESH_START_MULTISTEP_PLAN.md": "ba6784498d792dc85dd431c807f59620d6851af97b4cd15efe89c44a397b10b6",
    str(ASSET_REL / "SM_GIA_BloodAxeCairnstone_A005_RESET_RESUME_STATE.md"): "035aec1503b750a020f651455b04828489ea92e79d97296ed9230b35a164270a",
    str(ASSET_REL / "SM_GIA_BloodAxeCairnstone_A005_APPROVAL_LOG.md"): "f76c45a4cdb6653b94aaae564c0ddcd23ad0bdf55fd4eaa6a51dbd5b626aed2e",
    str(ASSET_REL / "SM_GIA_BloodAxeCairnstone_A005_ARTIFACT_INDEX.md"): "7eb1e9d32472ca5a2ab0eba76a2ae4fbd71c7bbf6f93dad3fc974f719d7067ab",
    str(ASSET_REL / "steps/STEP_10R_N3_INTEGRATION_REVISION_A01_CONTRACT.md"): "d38aff71b69daecfd3a42148018dc9538b3ebdd4a1d2c7e936d7aa4db16a1826",
    str(ASSET_REL / "manifests/STEP_10R_N3_INTEGRATION_DECISION_REGISTRY.json"): "f60634468c2d820e230da0a847a181be90893411c3e7838283eb61730e7d37e5",
    str(ASSET_REL / "manifests/STEP_10R_N3_PLACEMENT_MAPPING_OPTION_REGISTRY.json"): "37e7b76f6ee98fba5cfbdfed45d7048402114f4b88ea92055717350e48b1f3bc",
    str(ASSET_REL / "manifests/STEP_10R_N3_TRANSITION_INTEGRATION_OPTION_REGISTRY.json"): "3143f233c471c823693d8539f7abf7478340bdcfdd3eef871f68cabc7ca3728f",
    str(ASSET_REL / "manifests/STEP_10R_N3_INTEGRATION_REMAINING_BLOCKS.json"): "8776c2abcc9a96820cbd4046314a0ef1244c5fb58205c58b46dd9aad8cee1953",
    str(ASSET_REL / "manifests/C004_BOUNDARY_TRANSITION_INTERPRETATION_RULE_A01_PER_VIEW_LEDGER.json"): "c30fe9e7ae2c623122865102b16922931e42e87e2a3bfadb145cbe73f4861113",
    str(ASSET_REL / "manifests/C003_TARGET_SPACE_INNER_BOUNDARY_INTERPRETATION_RULE_A02_K80_DECISION_REGISTRY.json"): "4d7a6e5eff56c217512f54bf0ce50b0d2d37faee8b1e0a6950f08bbc72ae2d05",
    str(ASSET_REL / "manifests/S10R_003_A_CL003_TARGET_SPACE_MAPPING_A01_DECISION_REGISTRY.json"): "05ddf7d67cbed5bca4eb32ec749767b43f74af69bcc77f556e08cec5fb288ff2",
    str(ASSET_REL / "manifests/S10R_003_A_CL003_TARGET_SPACE_MAPPING_A01_REMAINING_BLOCKS.json"): "89067a408ed5f78d01f60be1fa8228911463e309591c34e7196ca27993955eef",
    str(ASSET_REL / "manifests/S10R_003_A_CL003_TARGET_SPACE_MAPPING_A01_DECISION_CLOSEOUT_VALIDATION.json"): "415778d27ba8358affc22795c81abe85a24366cc95fc3539ae85db65e8453a2b",
    str(ASSET_REL / "steps/S10R_003_A_CL003_TARGET_SPACE_MAPPING_A01_DECISION_CLOSEOUT_OUTPUT_RECORD.md"): "31f6947ac947d9155ecba5fbb7100de20111749f744eefb345850a77361836ef",
    str(ASSET_REL / "handoffs/S10R_003_A_CL003_TARGET_SPACE_MAPPING_A01_TO_S10R006_CONTRACT_PREPARATION_HANDOFF.md"): "549904200f1a6d72c7d520eec8d437cd65c12020370b46f0d9fc7fa3d5a4b08e",
    "Saved/ProjectRecovery/20260717-160835/git_status_short.txt": "8d533d4da60f9b80e0c5fe0369118319e85e6ecdecba57b87b8640ec19554cb6",
    str(CONTRACT.relative_to(ROOT)): "0f4e7fae93d9fe36beb4e0d5ad13cafaf1a2ea0864845c79ac574db75792bd8e",
}


def sha256(path: Path) -> str:
    digest = hashlib.sha256()
    with path.open("rb") as handle:
        for chunk in iter(lambda: handle.read(1024 * 1024), b""):
            digest.update(chunk)
    return digest.hexdigest()


def read_json(path: Path) -> dict:
    return json.loads(path.read_text(encoding="utf-8"))


def write_json(path: Path, value: dict) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(json.dumps(value, indent=2, ensure_ascii=False) + "\n", encoding="utf-8")


def now() -> str:
    return datetime.now().astimezone().isoformat(timespec="seconds")


def find_subject(registry: dict, subject_id: str) -> dict:
    return next(item for item in registry["decision_subjects"] if item["id"] == subject_id)


def font(size: int, bold: bool = False):
    name = "DejaVuSans-Bold.ttf" if bold else "DejaVuSans.ttf"
    try:
        return ImageFont.truetype(name, size)
    except OSError:
        return ImageFont.load_default()


def wrap(draw: ImageDraw.ImageDraw, text: str, x: int, y: int, width: int, font_obj, fill, gap: int = 8) -> int:
    words = text.split()
    lines, current = [], ""
    for word in words:
        trial = word if not current else current + " " + word
        if draw.textbbox((0, 0), trial, font=font_obj)[2] <= width:
            current = trial
        else:
            if current:
                lines.append(current)
            current = word
    if current:
        lines.append(current)
    line_h = draw.textbbox((0, 0), "Ag", font=font_obj)[3] + gap
    for line in lines:
        draw.text((x, y), line, font=font_obj, fill=fill)
        y += line_h
    return y


def curve_points(cx: float, cy: float, half_w: float, half_h: float, scale: float, exponent: float = 3.0):
    points = []
    for index in range(361):
        theta = 2.0 * math.pi * index / 360.0
        c, s = math.cos(theta), math.sin(theta)
        x = math.copysign(abs(c) ** (2.0 / exponent), c) * half_w
        y = math.copysign(abs(s) ** (2.0 / exponent), s) * half_h
        points.append((cx + x * scale, cy - y * scale))
    return points


def render_board(trace_ledger: dict, boundary_audit: dict) -> None:
    EVIDENCE.mkdir(parents=True, exist_ok=True)
    canvas = Image.new("RGB", (2400, 1800), (18, 22, 28))
    draw = ImageDraw.Draw(canvas)
    white, muted = (236, 241, 247), (168, 180, 194)
    cyan, amber, red = (58, 205, 225), (241, 183, 61), (236, 83, 83)
    panel = (29, 36, 45)
    draw.text((45, 35), "A005 S10R-006-A — BOUNDARY AUTHORITY AUDIT", font=font(42, True), fill=white)
    draw.text((45, 92), "TECHNICAL PROOF ONLY • NO FIELD • NO SOURCE/TARGET BRIDGE", font=font(24, True), fill=amber)

    target_box = (45, 145, 930, 830)
    draw.rounded_rectangle(target_box, radius=14, fill=panel, outline=(72, 86, 102), width=2)
    draw.text((75, 170), "TARGET CONSTRUCTION FRAME — UNFILLED BOUNDARIES", font=font(24, True), fill=white)
    cx, cy, scale = 485, 505, 5.2
    draw.line((cx - 390, cy, cx + 390, cy), fill=(90, 102, 116), width=1)
    draw.line((cx, cy - 290, cx, cy + 290), fill=(90, 102, 116), width=1)
    draw.line(curve_points(cx, cy, 70, 55, scale), fill=cyan, width=5)
    draw.line(curve_points(cx, cy, 56, 44, scale), fill=amber, width=5)
    draw.text((90, 735), "N3: |x/70|³ + |y/55|³ = 1  (140 × 110 cm)", font=font(21), fill=cyan)
    draw.text((90, 772), "K80: |x/56|³ + |y/44|³ = 1  (112 × 88 cm)", font=font(21), fill=amber)
    draw.text((90, 805), "Analytic containment: 0.8 scale; K80 evaluates to 0.512 in N3", font=font(18), fill=muted)

    matrix_box = (960, 145, 2355, 830)
    draw.rounded_rectangle(matrix_box, radius=14, fill=panel, outline=(72, 86, 102), width=2)
    draw.text((990, 170), "AUTHORITY-AVAILABILITY MATRIX", font=font(24, True), fill=white)
    rows = [
        ("S10R-002-A target construction frame", "AVAILABLE", cyan),
        ("S10R-003-A K80 + 16 top mappings", "AVAILABLE", cyan),
        ("S10R-004-A 26 owner-view trace formulas", "AVAILABLE IN SOURCE PIXEL FRAMES", amber),
        ("S10R-005-A within-sector ruled ownership", "AVAILABLE; JOINS EXCLUDED", amber),
        ("Upright trace target-space coordinates", "MISSING", red),
        ("Registered source-view → target correspondence", "MISSING", red),
        ("Exact common-frame trace comparisons", "0 / 26 AVAILABLE", red),
    ]
    y = 230
    for label, value, color in rows:
        draw.rectangle((990, y, 2325, y + 62), fill=(35, 43, 53), outline=(62, 74, 88))
        draw.text((1010, y + 17), label, font=font(19), fill=white)
        draw.text((1740, y + 17), value, font=font(19, True), fill=color)
        y += 72
    y = wrap(draw, "RESULT: blocked_source_authority_missing. Missing common-frame authority is a block, not a mismatch and not permission to infer a transform.", 990, 750, 1300, font(21, True), red, 7)

    view_names = ["front", "back", "left", "right"]
    box_w, gap, start_x = 560, 20, 45
    for view_index, view_name in enumerate(view_names):
        x0 = start_x + view_index * (box_w + gap)
        y0, x1, y1 = 870, x0 + box_w, 1740
        draw.rounded_rectangle((x0, y0, x1, y1), radius=14, fill=panel, outline=(72, 86, 102), width=2)
        view = trace_ledger["views"][view_name]
        traces = view["traces"]
        draw.text((x0 + 20, y0 + 18), f"{view_name.upper()} SOURCE-PIXEL FRAME", font=font(21, True), fill=white)
        draw.text((x0 + 20, y0 + 53), f"{len(traces)} exact trace formulas • no target mapping", font=font(16), fill=amber)
        source_path = ROOT / view["source_panel"]["path"]
        source = Image.open(source_path).convert("RGB")
        max_w, max_h = box_w - 40, 590
        factor = min(max_w / source.width, max_h / source.height)
        nearest = getattr(getattr(Image, "Resampling", Image), "NEAREST")
        resized = source.resize((round(source.width * factor), round(source.height * factor)), nearest)
        px = x0 + (box_w - resized.width) // 2
        py = y0 + 95 + (590 - resized.height) // 2
        canvas.paste(resized, (px, py))
        for trace in traces:
            p_i, p_o = trace["p_i"], trace["p_o"]
            a = (px + p_i[0] * factor, py + p_i[1] * factor)
            b = (px + p_o[0] * factor, py + p_o[1] * factor)
            draw.line((a, b), fill=amber, width=3)
            r = 4
            draw.ellipse((a[0]-r, a[1]-r, a[0]+r, a[1]+r), outline=(255, 240, 170), width=2)
            draw.rectangle((b[0]-r, b[1]-r, b[0]+r, b[1]+r), outline=amber, width=2)
        draw.text((x0 + 20, y1 - 120), "Yellow lines: approved bounded trace rules", font=font(16), fill=amber)
        draw.text((x0 + 20, y1 - 88), "Coordinates remain source-panel pixels", font=font(16), fill=muted)
        draw.text((x0 + 20, y1 - 56), "No physical pair • no field • no geometry", font=font(16, True), fill=red)

    draw.text((45, 1760), "Artifact: proof only | Source and target domains are deliberately separated", font=font(18), fill=muted)
    canvas.save(BOARD)


def main() -> None:
    lock_results = {}
    for rel, expected in EXPECTED_HASHES.items():
        path = ROOT / rel
        actual = sha256(path) if path.is_file() else None
        lock_results[rel] = {"expected_sha256": expected, "actual_sha256": actual, "match": actual == expected}
    mismatches = [path for path, value in lock_results.items() if not value["match"]]
    if mismatches:
        raise SystemExit(f"STOP: locked input hash mismatch: {mismatches}")

    placement = read_json(PLACEMENT)
    transition = read_json(TRANSITION)
    decisions = read_json(DECISIONS)
    trace_ledger = read_json(TRACE_LEDGER)
    k80 = read_json(K80)
    mapping = read_json(MAPPING)

    panel_hashes = {}
    for view_name in ("front", "back", "left", "right"):
        panel = trace_ledger["views"][view_name]["source_panel"]
        actual = sha256(ROOT / panel["path"])
        panel_hashes[view_name] = {
            "path": panel["path"],
            "ledger_expected_sha256": panel["file_sha256"],
            "actual_sha256": actual,
            "match": actual == panel["file_sha256"],
        }
    if not all(item["match"] for item in panel_hashes.values()):
        raise SystemExit("STOP: source panel differs from frozen trace ledger")

    input_lock = {
        "schema": "aerathea.s10r_006_a_boundary_compatibility_technical_gate_a01_input_lock.v1",
        "asset_id": "SM_GIA_BloodAxeCairnstone_A005",
        "contract_id": CONTRACT_ID,
        "date": "2026-07-17",
        "executed_at": now(),
        "status": "locked_before_audit_outputs",
        "artifact_classification": "proof only",
        "execution_approval": {"approver": "Flamestrike", "statement": "approved", "scope": "contract exactly as written"},
        "contract": {"path": str(CONTRACT.relative_to(ROOT)), "sha256": sha256(CONTRACT)},
        "locked_inputs": lock_results,
        "locked_input_count": len(lock_results),
        "locked_input_match_count": len(lock_results),
        "locked_input_mismatch_count": 0,
        "source_panels_locked_through_trace_ledger": panel_hashes,
        "pre_action_checkpoint": "Saved/ProjectRecovery/20260717-161842/",
        "git": {"branch": "main", "head": "f525945", "staged_paths": []},
        "pre_output_counts": {"field_samples": 0, "fills": 0, "surfaces": 0, "topology": 0, "geometry": 0},
    }

    s002 = find_subject(placement, "S10R-002")
    s003 = find_subject(placement, "S10R-003")
    s004 = find_subject(transition, "S10R-004")
    s005 = find_subject(transition, "S10R-005")
    s006 = find_subject(transition, "S10R-006")
    decision_006 = next(item for item in decisions["decision_items"] if item["id"] == "S10R-006")

    dependencies = [
        {
            "id": "S10R-002-A",
            "status": "approved_rule_available_not_implemented",
            "authority_available": s002["flamestrike_decision"] == "S10R-002-A",
            "scope": "construction-origin centered target-frame interpretation only; no source placement center or pivot",
        },
        {
            "id": "S10R-003-A",
            "status": "approved_bounded_mapping_available",
            "authority_available": s003["flamestrike_decision"] == "S10R-003-A" and len(mapping["mappings"]) == 16,
            "scope": "K80 plus exact sixteen-record top CL-003 target mapping only",
        },
        {
            "id": "S10R-004-A",
            "status": "approved_bounded_owner_view_traces_available",
            "authority_available": s004["flamestrike_decision"] == "S10R-004-A",
            "scope": "26 exact trace formulas inside declared source owner-view sectors only",
        },
        {
            "id": "S10R-005-A",
            "status": "approved_bounded_with_join_exclusions",
            "authority_available": s005["flamestrike_decision"] == "S10R-005-A",
            "scope": "adjacent-trace ruled strips inside owner-view sectors; cross-view and top/upright joins excluded",
        },
    ]
    dependency_audit = {
        "schema": "aerathea.s10r_006_a_boundary_compatibility_technical_gate_a01_dependency_audit.v1",
        "asset_id": "SM_GIA_BloodAxeCairnstone_A005",
        "contract_id": CONTRACT_ID,
        "date": "2026-07-17",
        "status": "dependencies_registered_boundary_common_frame_authority_missing",
        "artifact_classification": "authoritative for bounded S10R-006-A audit routing only",
        "approved_conditional_rule": {
            "id": "S10R-006-A",
            "decision_status": s006["decision_status"],
            "decision_registry_result": decision_006["current_result"],
            "implementation_authorized": False,
        },
        "dependencies": dependencies,
        "dependency_rule_count": 4,
        "dependency_rule_authority_available_count": sum(item["authority_available"] for item in dependencies),
        "dependency_implementation_count": 0,
        "remaining_required_gate": "exact common-frame authority and agreement at every registered trace boundary",
        "field_samples_created": 0,
        "source_or_prior_authority_modified": False,
    }

    traces = []
    per_view = {}
    for view_name in ("front", "back", "left", "right"):
        view_traces = trace_ledger["views"][view_name]["traces"]
        per_view[view_name] = len(view_traces)
        for trace in view_traces:
            traces.append(
                {
                    "trace_id": trace["trace_id"],
                    "view": trace["view"],
                    "view_role": trace["view_role"],
                    "source_pixel_frame": trace["view"],
                    "p_i": trace["p_i"],
                    "p_o": trace["p_o"],
                    "p_t_formula": trace["p_t_formula"],
                    "approved_bounded_classification_authority": "STEP_10R_N3_TRANSITION_INTEGRATION_OPTION_REGISTRY S10R-004-A",
                    "target_space_coordinate_authority": False,
                    "registered_common_frame": None,
                    "registered_cross_frame_correspondence_id": None,
                    "exact_comparison_performed": False,
                    "comparison_status": "unavailable_source_authority_missing",
                    "inferred_coordinate_created": False,
                }
            )

    n3_eval = 0.8 ** 3
    mapping_targets = [tuple(item["target_xy_cm_decimal"]) for item in mapping["mappings"]]
    boundary_audit = {
        "schema": "aerathea.s10r_006_a_boundary_compatibility_technical_gate_a01_boundary_authority_audit.v1",
        "asset_id": "SM_GIA_BloodAxeCairnstone_A005",
        "contract_id": CONTRACT_ID,
        "date": "2026-07-17",
        "status": "blocked_source_authority_missing",
        "artifact_classification": "proof only",
        "controlling_result": "blocked_source_authority_missing",
        "blueprint_block_label": "Blueprint block: source authority missing",
        "target_boundary_analytic_audit": {
            "outer_id": "TOP_C004_OPIR_N3_ROUNDED_OVAL",
            "outer_equation": "abs(x / 70)^3 + abs(y / 55)^3 = 1",
            "outer_extents_cm": [140, 110],
            "inner_id": "C003_TSIB_K80_MEDIUM_APRON",
            "inner_equation": "abs(x / 56)^3 + abs(y / 44)^3 = 1",
            "inner_extents_cm": [112, 88],
            "shared_mathematical_origin": [0, 0],
            "x_axis_ratio": 56 / 70,
            "y_axis_ratio": 44 / 55,
            "homothetic_scale": 0.8,
            "inner_boundary_value_in_outer_equation": n3_eval,
            "strict_abstract_containment": n3_eval < 1.0,
            "analytic_gate_status": "pass",
            "field_samples_created": 0,
        },
        "approved_top_mapping_audit": {
            "record_count": len(mapping["mappings"]),
            "unique_target_coordinate_count": len(set(mapping_targets)),
            "endpoint_assignment_count": 0,
            "mapped_non_top_sample_count": 0,
            "source_displacement_px": 0,
            "physical_cross_view_pair_count": 0,
            "status": "pass_bounded_target_mapping_available",
        },
        "registered_trace_boundaries": traces,
        "trace_counts": {
            "required_registered_trace_boundaries": len(traces),
            "per_view": per_view,
            "common_frame_authority_available": 0,
            "common_frame_authority_missing": len(traces),
            "exact_comparisons_performed": 0,
            "explicit_boundary_mismatches": 0,
            "inferred_correspondences": 0,
        },
        "comparison_rule": {
            "comparable_only_if_same_named_frame_and_registered_correspondence": True,
            "visual_proximity_allowed": False,
            "nearest_matching_allowed": False,
            "panel_normalization_allowed": False,
            "assumed_transform_allowed": False,
            "post_result_tolerance_allowed": False,
            "missing_authority_is_not_mismatch": True,
        },
        "authority_counts": {
            "field_samples": 0,
            "fills": 0,
            "surfaces": 0,
            "topology": 0,
            "geometry": 0,
            "new_target_trace_coordinates": 0,
            "new_physical_cross_view_pairs": 0,
            "new_source_target_transforms": 0,
        },
        "active_blocks_preserved": ["S10R-BLOCK-006", "S10R-BLOCK-008", "S10R-BLOCK-009"],
        "step10_closeout_authorized": False,
        "step11_authorized": False,
        "production_authorized": False,
        "staging_commit_push_authorized": False,
        "review_board_policy": "target boundary lines and source-view trace panels separated; no field fill source-target overlay or inferred correspondence",
    }

    write_json(INPUT_LOCK, input_lock)
    write_json(DEPENDENCY, dependency_audit)
    write_json(BOUNDARY, boundary_audit)
    render_board(trace_ledger, boundary_audit)
    print(f"wrote {INPUT_LOCK.relative_to(ROOT)}")
    print(f"wrote {DEPENDENCY.relative_to(ROOT)}")
    print(f"wrote {BOUNDARY.relative_to(ROOT)}")
    print(f"wrote {BOARD.relative_to(ROOT)}")
    print("result: blocked_source_authority_missing; field samples: 0")


if __name__ == "__main__":
    main()
