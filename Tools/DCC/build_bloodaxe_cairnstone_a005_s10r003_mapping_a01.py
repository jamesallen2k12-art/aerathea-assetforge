#!/usr/bin/env python3
"""Build the bounded S10R-003-A CL-003 mapping candidate and review board."""

from __future__ import annotations

import hashlib
import json
import math
import subprocess
from datetime import datetime
from pathlib import Path

from PIL import Image, ImageDraw, ImageFont


ROOT = Path(__file__).resolve().parents[2]
ASSET = ROOT / "docs/assets/blueprints/SM_GIA_BloodAxeCairnstone_A005"
MANIFESTS = ASSET / "manifests"
EVIDENCE_DIR = ASSET / "evidence/S10R_003_A_CL003_TARGET_SPACE_MAPPING_A01"
CONTRACT = ASSET / "steps/S10R_003_A_CL003_TARGET_SPACE_MAPPING_EXECUTION_A01_CONTRACT.md"
INPUT_LOCK_OUT = MANIFESTS / "S10R_003_A_CL003_TARGET_SPACE_MAPPING_A01_INPUT_LOCK.json"
LEDGER_OUT = MANIFESTS / "S10R_003_A_CL003_TARGET_SPACE_MAPPING_A01_LEDGER.json"
BOARD_OUT = EVIDENCE_DIR / "SM_GIA_BloodAxeCairnstone_A005_S10R_003_A_CL003_TARGET_SPACE_MAPPING_A01_REVIEW_BOARD.png"
SOURCE_CONTACTS = MANIFESTS / "STEP_04_TOP_CONTACT_EVIDENCE_RECOVERY_A01.json"
SOURCE_PANEL = ASSET / "panels/STEP_03/SM_GIA_BloodAxeCairnstone_A005_STEP_03_TOP.png"
PRE_CHECKPOINT = ROOT / "Saved/ProjectRecovery/20260717-153840"

CONTRACT_ID = "A005-CR-S10R-003-A-MAP-A01"
CONTRACT_SHA256 = "10dc155b78e2d2e6f15a389a9a247db13450314df2d8e3bc9ba891901b3208f8"
HEAD = "f525945"
BRANCH = "main"

LOCKED_INPUTS = {
    "AGENTS.md": "5d2d2637a58113f0a6f5ec92e40d8bb2bda9e03fb58b4868a0d9dfbb3b57ad55",
    "docs/projects/assetforge/BLOODAXE_CAIRNSTONE_PIXEL_EXACT_FRESH_START_MULTISTEP_PLAN.md": "ba6784498d792dc85dd431c807f59620d6851af97b4cd15efe89c44a397b10b6",
    "docs/assets/blueprints/SM_GIA_BloodAxeCairnstone_A005/SM_GIA_BloodAxeCairnstone_A005_RESET_RESUME_STATE.md": "8a3d7b40c93f657093a74361e6511f45d1e34d6b5dab85c73b16abc949998a4d",
    "docs/assets/blueprints/SM_GIA_BloodAxeCairnstone_A005/SM_GIA_BloodAxeCairnstone_A005_APPROVAL_LOG.md": "b193da1f50a7fb375676d74b9d77a1664811d987687efdfa54979a9126bf8a82",
    "docs/assets/blueprints/SM_GIA_BloodAxeCairnstone_A005/handoffs/C003_TARGET_SPACE_INNER_BOUNDARY_INTERPRETATION_RULE_A02_K80_TO_S10R003_MAPPING_CONTRACT_PREPARATION_HANDOFF.md": "2fda3a3c07c0eb618339b35d094ff7cfa29ce8bf92c3c91089bcb6f208852d83",
    "docs/assets/blueprints/SM_GIA_BloodAxeCairnstone_A005/steps/C003_TARGET_SPACE_INNER_BOUNDARY_INTERPRETATION_RULE_A02_K80_DECISION_CLOSEOUT_OUTPUT_RECORD.md": "76c1d8f66ad82d24ce22381b433cc1b07c51933795ae257b65964231de6925ee",
    "docs/assets/blueprints/SM_GIA_BloodAxeCairnstone_A005/manifests/C003_TARGET_SPACE_INNER_BOUNDARY_INTERPRETATION_RULE_A02_K80_DECISION_REGISTRY.json": "4d7a6e5eff56c217512f54bf0ce50b0d2d37faee8b1e0a6950f08bbc72ae2d05",
    "docs/assets/blueprints/SM_GIA_BloodAxeCairnstone_A005/manifests/C003_TARGET_SPACE_INNER_BOUNDARY_INTERPRETATION_RULE_A02_K80_REMAINING_BLOCKS.json": "e3de4150df887e53e3dbc569339daa54b07b1a8bc72cecd7d0a67ab0a7aba883",
    "docs/assets/blueprints/SM_GIA_BloodAxeCairnstone_A005/manifests/C003_TARGET_SPACE_INNER_BOUNDARY_INTERPRETATION_RULE_A02_K80_DECISION_CLOSEOUT_VALIDATION.json": "2e5cab2fc8e7033ad7abc3d1c754f45861cd4d4c6005bcc047a811235912c33b",
    "docs/assets/blueprints/SM_GIA_BloodAxeCairnstone_A005/manifests/STEP_10R_N3_INTEGRATION_DECISION_REGISTRY.json": "f60634468c2d820e230da0a847a181be90893411c3e7838283eb61730e7d37e5",
    "docs/assets/blueprints/SM_GIA_BloodAxeCairnstone_A005/manifests/STEP_10R_N3_PLACEMENT_MAPPING_OPTION_REGISTRY.json": "37e7b76f6ee98fba5cfbdfed45d7048402114f4b88ea92055717350e48b1f3bc",
    "docs/assets/blueprints/SM_GIA_BloodAxeCairnstone_A005/manifests/STEP_08R_TOP_SECTOR_CLASSIFICATION.json": "e135db381c6255db0260b5e1ec1016acdc025066ebd784a319f989c8e911675f",
    "docs/assets/blueprints/SM_GIA_BloodAxeCairnstone_A005/manifests/STEP_04_TOP_CONTACT_EVIDENCE_RECOVERY_A01.json": "8f9fb86ef631e5785552a61f61e4a2d3085727f1a667bdf59cf904284b1b2eb0",
    "docs/assets/blueprints/SM_GIA_BloodAxeCairnstone_A005/manifests/STEP_09_CROSS_VIEW_CORRESPONDENCE_MANIFEST.json": "9efadda542ba2358c59b8d4fac4b731e5d877d2007aa1d03b3fe67abac29547f",
    "docs/assets/blueprints/SM_GIA_BloodAxeCairnstone_A005/manifests/C003_TARGET_SPACE_INNER_BOUNDARY_INTERPRETATION_RULE_A02_OPTION_REGISTRY.json": "ba24e6b5803deb6af15b5fcf1d7e95f2f088321a63775a32ff39d6350b7423aa",
    "docs/assets/blueprints/SM_GIA_BloodAxeCairnstone_A005/manifests/C003_TARGET_SPACE_INNER_BOUNDARY_INTERPRETATION_RULE_A02_CURVE_LEDGER.json": "dc04dab52e922786a99eaa7bbc52cb3620ac41c4784aae56a10b098423952410",
}

EXPECTED_SAMPLES = [
    ("top", 1, "T-CL003-TOP-01", (120, 47), (53, 46, 46)),
    ("top", 2, "T-CL003-TOP-02", (145, 46), (76, 71, 66)),
    ("top", 3, "T-CL003-TOP-03", (170, 46), (34, 31, 30)),
    ("top", 4, "T-CL003-TOP-04", (184, 49), (34, 18, 17)),
    ("bottom", 1, "T-CL003-BOTTOM-01", (90, 250), (18, 19, 13)),
    ("bottom", 2, "T-CL003-BOTTOM-02", (120, 252), (62, 59, 51)),
    ("bottom", 3, "T-CL003-BOTTOM-03", (150, 253), (48, 45, 47)),
    ("bottom", 4, "T-CL003-BOTTOM-04", (184, 249), (19, 12, 11)),
    ("left", 1, "T-CL003-LEFT-01", (49, 110), (32, 20, 17)),
    ("left", 2, "T-CL003-LEFT-02", (46, 135), (2, 0, 0)),
    ("left", 3, "T-CL003-LEFT-03", (45, 160), (15, 2, 2)),
    ("left", 4, "T-CL003-LEFT-04", (49, 190), (54, 9, 6)),
    ("right", 1, "T-CL003-RIGHT-01", (230, 110), (43, 39, 37)),
    ("right", 2, "T-CL003-RIGHT-02", (231, 135), (38, 37, 34)),
    ("right", 3, "T-CL003-RIGHT-03", (233, 160), (45, 10, 11)),
    ("right", 4, "T-CL003-RIGHT-04", (227, 190), (26, 9, 6)),
]

SECTOR_COLORS = {
    "top": (42, 135, 214),
    "right": (228, 151, 32),
    "bottom": (139, 82, 196),
    "left": (45, 153, 95),
}


def sha256(path: Path) -> str:
    digest = hashlib.sha256()
    with path.open("rb") as handle:
        for chunk in iter(lambda: handle.read(1024 * 1024), b""):
            digest.update(chunk)
    return digest.hexdigest()


def write_json(path: Path, payload: dict) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(json.dumps(payload, indent=2, sort_keys=False) + "\n", encoding="utf-8")


def git_value(*args: str) -> str:
    return subprocess.check_output(["git", *args], cwd=ROOT, text=True).strip()


def sign(value: float) -> float:
    if value > 0:
        return 1.0
    if value < 0:
        return -1.0
    return 0.0


def k80_point(theta: float) -> tuple[float, float]:
    cosine = math.cos(theta)
    sine = math.sin(theta)
    x = 56.0 * sign(cosine) * abs(cosine) ** (2.0 / 3.0)
    y = 44.0 * sign(sine) * abs(sine) ** (2.0 / 3.0)
    return x, y


def theta_for(sector: str, u: float) -> float:
    if sector == "top":
        return math.pi * (1.0 - u)
    if sector == "right":
        return math.pi / 2.0 - math.pi * u
    if sector == "bottom":
        return 2.0 * math.pi - math.pi * u
    if sector == "left":
        return 3.0 * math.pi / 2.0 - math.pi * u
    raise ValueError(f"Unsupported sector: {sector}")


def font(size: int, bold: bool = False) -> ImageFont.FreeTypeFont | ImageFont.ImageFont:
    name = "DejaVuSans-Bold.ttf" if bold else "DejaVuSans.ttf"
    try:
        return ImageFont.truetype(f"/usr/share/fonts/truetype/dejavu/{name}", size)
    except OSError:
        return ImageFont.load_default()


def draw_review_board(records: list[dict]) -> dict:
    source = Image.open(SOURCE_PANEL).convert("RGB")
    scale = 2
    source_display = source.resize((source.width * scale, source.height * scale), Image.NEAREST)

    board = Image.new("RGB", (2000, 1180), (242, 242, 238))
    draw = ImageDraw.Draw(board)
    title_font = font(34, True)
    heading_font = font(25, True)
    body_font = font(19)
    small_font = font(16)

    draw.text((54, 32), "A005 S10R-003-A CL-003 Target-Space Mapping A01", fill=(24, 24, 28), font=title_font)
    draw.text((54, 78), "CANDIDATE INTERPRETATION · ENDPOINT-EXCLUSIVE · NOT GEOMETRY · PENDING FLAMESTRIKE", fill=(154, 40, 40), font=heading_font)

    left_box = (44, 128, 930, 1088)
    right_box = (970, 128, 1956, 1088)
    draw.rounded_rectangle(left_box, radius=14, fill=(255, 255, 252), outline=(118, 118, 112), width=2)
    draw.rounded_rectangle(right_box, radius=14, fill=(255, 255, 252), outline=(118, 118, 112), width=2)
    draw.text((70, 152), "EVIDENCE — untouched source file, exact marks", fill=(30, 30, 34), font=heading_font)
    draw.text((996, 152), "INTERPRETATION — K80 target-space candidate", fill=(30, 30, 34), font=heading_font)

    sx = 140
    sy = 220
    board.paste(source_display, (sx, sy))
    draw.rectangle((sx - 2, sy - 2, sx + source_display.width + 1, sy + source_display.height + 1), outline=(70, 70, 70), width=2)
    for record in records:
        px, py = record["source_pixel_local"]
        cx = sx + px * scale
        cy = sy + py * scale
        color = SECTOR_COLORS[record["sector"]]
        radius = 8
        draw.ellipse((cx - radius, cy - radius, cx + radius, cy + radius), outline=color, width=3)
        draw.line((cx - 11, cy, cx + 11, cy), fill=color, width=1)
        draw.line((cx, cy - 11, cx, cy + 11), fill=color, width=1)

    draw.text((70, 1008), "Display: 2× nearest-neighbor. Source artifact is unchanged.", fill=(60, 60, 65), font=small_font)
    draw.text((70, 1035), "Marks are the 16 authoritative top-view CL-003 pixel centers only.", fill=(60, 60, 65), font=small_font)

    plot = (1090, 250, 1835, 900)
    px0 = (plot[0] + plot[2]) / 2.0
    py0 = (plot[1] + plot[3]) / 2.0
    plot_scale = min((plot[2] - plot[0]) / 122.0, (plot[3] - plot[1]) / 98.0)

    def project(x: float, y: float) -> tuple[int, int]:
        return int(round(px0 + x * plot_scale)), int(round(py0 - y * plot_scale))

    draw.line((*project(-61, 0), *project(61, 0)), fill=(205, 205, 202), width=1)
    draw.line((*project(0, -49), *project(0, 49)), fill=(205, 205, 202), width=1)

    curve = []
    for index in range(721):
        theta = 2.0 * math.pi * index / 720.0
        curve.append(project(*k80_point(theta)))
    draw.line(curve, fill=(48, 52, 58), width=3)

    endpoints = [(56, 0), (-56, 0), (0, 44), (0, -44)]
    for x, y in endpoints:
        cx, cy = project(x, y)
        draw.rectangle((cx - 6, cy - 6, cx + 6, cy + 6), outline=(180, 42, 42), width=3)

    for record in records:
        x, y = record["target_xy_cm"]
        cx, cy = project(x, y)
        color = SECTOR_COLORS[record["sector"]]
        draw.ellipse((cx - 8, cy - 8, cx + 8, cy + 8), fill=(255, 255, 252), outline=color, width=4)
        draw.text((cx + 10, cy - 11), str(record["local_rank"]), fill=color, font=small_font)

    legend_y = 932
    for idx, sector in enumerate(("top", "right", "bottom", "left")):
        lx = 1010 + idx * 215
        color = SECTOR_COLORS[sector]
        draw.ellipse((lx, legend_y, lx + 16, legend_y + 16), outline=color, width=3)
        draw.text((lx + 23, legend_y - 4), sector, fill=(42, 42, 46), font=body_font)
    draw.rectangle((1010, 980, 1024, 994), outline=(180, 42, 42), width=3)
    draw.text((1034, 974), "registered endpoint limit — no sample assigned", fill=(70, 55, 55), font=body_font)
    draw.text((1010, 1018), "u = {1/5, 2/5, 3/5, 4/5}; points are not joined across sectors.", fill=(55, 55, 60), font=body_font)
    draw.text((1010, 1049), "No source fit · no cross-view pair · no closure · no field · no geometry", fill=(154, 40, 40), font=body_font)

    EVIDENCE_DIR.mkdir(parents=True, exist_ok=True)
    board.save(BOARD_OUT, format="PNG", optimize=False)
    return {
        "path": str(BOARD_OUT.relative_to(ROOT)),
        "sha256": sha256(BOARD_OUT),
        "size_px": [board.width, board.height],
        "source_display_scale": "2x_nearest_neighbor",
        "source_mark_count": 16,
        "candidate_target_point_count": 16,
        "registered_endpoint_marker_count": 4,
        "candidate_fill_count": 0,
        "cross_sector_join_count": 0,
        "source_target_overlay_count": 0,
        "geometry_preview_count": 0,
        "line_only_target_curve": True,
    }


def main() -> None:
    if sha256(CONTRACT) != CONTRACT_SHA256:
        raise SystemExit("Contract hash mismatch; stop before outputs")
    if git_value("rev-parse", "--short", "HEAD") != HEAD:
        raise SystemExit("HEAD mismatch; stop before outputs")
    if git_value("branch", "--show-current") != BRANCH:
        raise SystemExit("Branch mismatch; stop before outputs")
    if not PRE_CHECKPOINT.is_dir():
        raise SystemExit("Required pre-action checkpoint is missing")

    input_records = []
    for rel_path, expected in LOCKED_INPUTS.items():
        path = ROOT / rel_path
        actual = sha256(path)
        input_records.append({"path": rel_path, "expected_sha256": expected, "actual_sha256": actual, "match": actual == expected})
    if not all(item["match"] for item in input_records):
        raise SystemExit("Locked input mismatch; stop before outputs")

    source_payload = json.loads(SOURCE_CONTACTS.read_text(encoding="utf-8"))
    authority = [point for point in source_payload["accepted_points"] if point["contact_id"] == "CL-003"]
    authority_by_id = {point["id"]: point for point in authority}
    if len(authority) != 16:
        raise SystemExit("Authoritative top CL-003 sample count is not 16")

    for sector, rank, sample_id, pixel, rgb in EXPECTED_SAMPLES:
        source = authority_by_id.get(sample_id)
        if source is None:
            raise SystemExit(f"Missing source sample {sample_id}")
        if source["sector"] != sector or tuple(source["pixel_local"]) != pixel or tuple(source["source_rgb"]) != rgb:
            raise SystemExit(f"Source authority mismatch for {sample_id}")

    input_lock = {
        "schema": "aerathea.s10r_003_a_cl003_target_space_mapping_a01_input_lock.v1",
        "asset_id": "SM_GIA_BloodAxeCairnstone_A005",
        "contract_id": CONTRACT_ID,
        "date": "2026-07-17",
        "executed_at": datetime.now().astimezone().isoformat(),
        "status": "locked_before_candidate_mapping_outputs",
        "artifact_classification": "proof only",
        "execution_approval": {"approver": "Flamestrike", "statement": "approved", "scope": "contract exactly as written"},
        "contract": {"path": str(CONTRACT.relative_to(ROOT)), "expected_sha256": CONTRACT_SHA256, "actual_sha256": sha256(CONTRACT), "match": True},
        "git": {"branch": BRANCH, "head": HEAD, "staged_paths": []},
        "pre_action_checkpoint": "Saved/ProjectRecovery/20260717-153840/",
        "locked_inputs": input_records,
        "locked_input_count": len(input_records),
        "locked_input_match_count": sum(1 for item in input_records if item["match"]),
        "locked_input_mismatch_count": sum(1 for item in input_records if not item["match"]),
        "source_lock": {
            "top_CL003_samples": 16,
            "all_view_CL003_samples": 47,
            "mapped_non_top_samples": 0,
            "source_displacement_px": 0,
            "source_panel_path": str(SOURCE_PANEL.relative_to(ROOT)),
            "source_panel_sha256": sha256(SOURCE_PANEL),
        },
        "pre_output_counts": {
            "source_to_target_mappings": 0,
            "target_CL003_coordinates": 0,
            "physical_cross_view_pairs": 0,
            "fields": 0,
            "surfaces": 0,
            "topology": 0,
            "geometry": 0,
        },
    }
    write_json(INPUT_LOCK_OUT, input_lock)

    records = []
    for sector, rank, sample_id, pixel, rgb in EXPECTED_SAMPLES:
        source = authority_by_id[sample_id]
        u = rank / 5.0
        theta = theta_for(sector, u)
        x, y = k80_point(theta)
        residual = abs((abs(x / 56.0) ** 3 + abs(y / 44.0) ** 3) - 1.0)
        endpoint_distance = min(math.dist((x, y), endpoint) for endpoint in ((56.0, 0.0), (-56.0, 0.0), (0.0, 44.0), (0.0, -44.0)))
        records.append({
            "mapping_id": f"S10R003A-{sector.upper()}-{rank:02d}",
            "source_id": sample_id,
            "sector": sector,
            "local_rank": rank,
            "source_sample_order_within_contact": source["sample_order_within_contact"],
            "source_pixel_local": list(pixel),
            "source_pixel_full": source["pixel_full_source"],
            "source_rgb": list(rgb),
            "source_authority": "authoritative exact discrete top-view CL-003 evidence",
            "source_displacement_px": 0,
            "u_exact": f"{rank}/5",
            "u_decimal": f"{u:.12f}",
            "theta_radians": f"{theta:.15f}",
            "theta_rule": {
                "top": "pi * (1 - u)",
                "right": "pi/2 - pi*u",
                "bottom": "2*pi - pi*u",
                "left": "3*pi/2 - pi*u",
            }[sector],
            "target_xy_cm": [x, y],
            "target_xy_cm_decimal": [f"{x:.12f}", f"{y:.12f}"],
            "K80_equation_residual": residual,
            "minimum_registered_endpoint_distance_cm": endpoint_distance,
            "endpoint_excluded": endpoint_distance > 1e-9,
            "classification": "candidate interpretation",
            "pending_Flamestrike_decision": True,
            "physical_cross_view_pair": False,
            "source_center_claim": False,
            "pivot_claim": False,
            "physical_C003_dimension_claim": False,
            "snap_anchor_authority": False,
            "geometry_vertex_authority": False,
        })

    board_record = draw_review_board(records)
    ledger = {
        "schema": "aerathea.s10r_003_a_cl003_target_space_mapping_a01_ledger.v1",
        "asset_id": "SM_GIA_BloodAxeCairnstone_A005",
        "contract_id": CONTRACT_ID,
        "date": "2026-07-17",
        "generated_at": datetime.now().astimezone().isoformat(),
        "status": "candidate_mapping_calculated_pending_Flamestrike",
        "artifact_classification": "candidate interpretation",
        "input_lock_sha256": sha256(INPUT_LOCK_OUT),
        "mapping_rule": {
            "name": "endpoint-exclusive equal-rank parameter mapping",
            "n_per_sector": 4,
            "u_rule": "r/(n+1)=r/5",
            "u_values_exact": ["1/5", "2/5", "3/5", "4/5"],
            "equal_arc_length_claim": False,
            "source_distance_fit": False,
            "endpoint_ownership_claim": False,
        },
        "K80": {
            "equation": "abs(x / 56)^3 + abs(y / 44)^3 = 1",
            "full_extents_cm": [112, 88],
            "origin": [0, 0],
            "origin_role": "mathematical construction convention only",
            "registered_axis_endpoints": {"positive_x": [56, 0], "negative_x": [-56, 0], "positive_y": [0, 44], "negative_y": [0, -44]},
            "serialization_decimal_places": 12,
        },
        "records": records,
        "counts": {
            "source_records_read": 16,
            "candidate_mappings": 16,
            "candidate_target_coordinates": 16,
            "unique_serialized_target_coordinates": len({tuple(item["target_xy_cm_decimal"]) for item in records}),
            "endpoint_assigned_samples": sum(1 for item in records if not item["endpoint_excluded"]),
            "mapped_non_top_samples": 0,
            "source_displacement_px": 0,
            "physical_cross_view_pairs": 0,
            "source_overlays": 0,
            "source_fit_calculations": 0,
            "closed_contact_loops": 0,
            "snap_anchors": 0,
            "filled_footprints": 0,
            "annuli": 0,
            "hidden_interfaces": 0,
            "fields": 0,
            "surfaces": 0,
            "topology": 0,
            "geometry": 0,
        },
        "review_board": board_record,
        "authority_limits": {
            "all_target_coordinates_are_interpretation": True,
            "source_evidence_modified": False,
            "source_center_or_pivot_created": False,
            "physical_C003_size_created": False,
            "geometry_ready_array_created": False,
            "automatic_approval": False,
            "step10_closeout_authorized": False,
            "step11_authorized": False,
            "production_authorized": False,
            "staging_commit_push_authorized": False,
        },
        "mandatory_stop": "visible candidate review before any promotion or downstream work",
    }
    write_json(LEDGER_OUT, ledger)

    print(f"Wrote {INPUT_LOCK_OUT.relative_to(ROOT)}")
    print(f"Wrote {LEDGER_OUT.relative_to(ROOT)}")
    print(f"Wrote {BOARD_OUT.relative_to(ROOT)}")
    print("Candidate mappings: 16; source displacement: 0; geometry: 0")


if __name__ == "__main__":
    main()
