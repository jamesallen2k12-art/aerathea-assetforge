#!/usr/bin/env python3
"""Approve A001 oval footprint authority and measure contact interfaces.

This pass records Flamestrike approval of the oval-footprint ratio board, marks
the prior radial trace as diagnostic/rejected for shape authority, and creates
the next contact/interface measurement board.

It does not generate mesh data, UVs, textures, inferred fill, movement, rotation,
centering, or assembled components.
"""

from __future__ import annotations

import hashlib
import json
from pathlib import Path
from typing import Any

from PIL import Image, ImageDraw, ImageFont


ROOT = Path(__file__).resolve().parents[2]
ASSET_NAME = "SM_GIA_BloodAxeCairnstone_A001"
SOURCE = ROOT / "docs/assets/reference/bloodaxe_cairnstone_asset/REF_GIA_BloodAxeCairnstoneAsset_A02_BlueprintTemplate.png"
OUT_DIR = ROOT / "Saved/Automation/DCC" / ASSET_NAME
EVIDENCE_DIR = OUT_DIR / "FreshEvidence" / "ContactInterfaces"

RESTART_MANIFEST = OUT_DIR / f"{ASSET_NAME}_A001BlueprintRestartManifest.json"
ORIENTATION_MANIFEST = OUT_DIR / f"{ASSET_NAME}_A001OrientationPixelManifest.json"
FORMULA_MANIFEST = OUT_DIR / f"{ASSET_NAME}_A001MeasurementFormulaManifest.json"
CENTER_MANIFEST = OUT_DIR / f"{ASSET_NAME}_A001PixelCountCenterManifest.json"
SNAP_MANIFEST = OUT_DIR / f"{ASSET_NAME}_A001SnapAnchorManifest.json"
OVAL_MANIFEST = OUT_DIR / f"{ASSET_NAME}_A001OvalFootprintRatioManifest.json"
RADIAL_MANIFEST = OUT_DIR / f"{ASSET_NAME}_A001RadialTraceManifest.json"

OVAL_APPROVAL_MANIFEST = OUT_DIR / f"{ASSET_NAME}_A001OvalFootprintApprovalManifest.json"
RADIAL_DECISION_MANIFEST = OUT_DIR / f"{ASSET_NAME}_A001RadialTraceReviewDecision.json"
CONTACT_MANIFEST = OUT_DIR / f"{ASSET_NAME}_A001ContactInterfaceManifest.json"
CONTACT_OVERLAY = OUT_DIR / f"{ASSET_NAME}_A001ContactInterfaceOverlay.png"
CONTACT_REVIEW_BOARD = OUT_DIR / f"{ASSET_NAME}_A001ContactInterfaceReviewBoard.png"

VIEWS = ("front", "back", "left", "right")
CONTACT_TOLERANCE_CM = 0.5

COLORS = {
    "formula_contact": (245, 207, 48),
    "primary_ring": (228, 42, 42),
    "ring_support": (0, 185, 255),
    "primary": (228, 42, 42),
    "support": (0, 185, 255),
    "ring": (255, 138, 30),
    "origin": (205, 80, 255),
}

RESAMPLE_LANCZOS = getattr(Image, "Resampling", Image).LANCZOS


def font(size: int) -> ImageFont.ImageFont:
    for candidate in (
        "/usr/share/fonts/truetype/dejavu/DejaVuSans.ttf",
        "/usr/share/fonts/truetype/liberation2/LiberationSans-Regular.ttf",
    ):
        try:
            return ImageFont.truetype(candidate, size)
        except OSError:
            continue
    return ImageFont.load_default()


def sha256_file(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest()


def read_json(path: Path) -> dict[str, Any]:
    return json.loads(path.read_text())


def verify_preconditions() -> tuple[dict[str, Any], dict[str, Any], dict[str, Any], dict[str, Any], dict[str, Any], dict[str, Any]]:
    for path in (RESTART_MANIFEST, ORIENTATION_MANIFEST, FORMULA_MANIFEST, CENTER_MANIFEST, SNAP_MANIFEST, OVAL_MANIFEST):
        if not path.exists():
            raise SystemExit(f"Missing required precondition manifest: {path}")

    restart = read_json(RESTART_MANIFEST)
    orientation = read_json(ORIENTATION_MANIFEST)
    formula = read_json(FORMULA_MANIFEST)
    centers = read_json(CENTER_MANIFEST)
    snap = read_json(SNAP_MANIFEST)
    oval = read_json(OVAL_MANIFEST)

    if restart.get("pixel_exact") is not True or restart.get("changed_pixels") != 0 or restart.get("max_rgb_delta") != 0:
        raise SystemExit("A001 source scanline proof is not exact; contact pass is blocked.")

    required_orientation_flags = [
        "no_movement_before_orientation_marks",
        "no_geometry_crop_before_orientation_marks",
        "no_rotation_before_orientation_marks",
        "no_centering_before_orientation_marks",
        "no_rebuild_before_orientation_marks",
        "no_assembly_before_orientation_marks",
    ]
    missing_flags = [key for key in required_orientation_flags if orientation.get(key) is not True]
    if missing_flags:
        raise SystemExit(f"Orientation manifest failed required flags: {missing_flags}")

    for label, manifest in (("formula", formula), ("center", centers), ("snap", snap), ("oval", oval)):
        state = manifest.get("pre_geometry_state")
        if not isinstance(state, dict):
            raise SystemExit(f"{label} manifest is missing pre_geometry_state.")
        for key in ("geometry_generated", "uvs_generated", "components_moved", "components_rotated", "components_centered", "components_assembled", "inferred_fill_generated"):
            if state.get(key) is not False:
                raise SystemExit(f"{label} manifest is no longer pre-geometry clean: {key}")

    return restart, orientation, formula, centers, snap, oval


def center_lookup(centers: dict[str, Any]) -> dict[str, list[float]]:
    result: dict[str, list[float]] = {}
    for item in centers.get("component_centers", []):
        if not isinstance(item, dict):
            continue
        center = item.get("pixel_count_center")
        if isinstance(center, list) and len(center) == 2:
            result[str(item.get("stable_component_id"))] = [float(center[0]), float(center[1])]
    return result


def approved_oval_records(oval: dict[str, Any]) -> list[dict[str, Any]]:
    records = []
    for record in oval.get("oval_footprint_records", []):
        if not isinstance(record, dict):
            continue
        if record.get("stable_component_id") in ("primary_monolith", "support_base"):
            approved = dict(record)
            approved["geometry_authority_status"] = "approved_formula_authority_for_A001_contact_and_geometry_planning"
            approved["approved_by"] = "Flamestrike"
            approved["approval_basis"] = "User approved the A001 oval footprint ratio review after raw-pixel/source-scale clarification."
            records.append(approved)
    return records


def write_approval_records(
    restart: dict[str, Any],
    orientation: dict[str, Any],
    formula: dict[str, Any],
    centers: dict[str, Any],
    oval: dict[str, Any],
) -> None:
    approved = approved_oval_records(oval)
    approval_manifest = {
        "asset": ASSET_NAME,
        "status": "A001 oval footprint ratios approved as formula authority before geometry",
        "source": str(SOURCE.relative_to(ROOT)),
        "source_sha256": sha256_file(SOURCE),
        "source_scanline_manifest": str(RESTART_MANIFEST.relative_to(ROOT)),
        "orientation_pixel_manifest": str(ORIENTATION_MANIFEST.relative_to(ROOT)),
        "measurement_formula_manifest": str(FORMULA_MANIFEST.relative_to(ROOT)),
        "pixel_count_center_manifest": str(CENTER_MANIFEST.relative_to(ROOT)),
        "oval_footprint_ratio_manifest": str(OVAL_MANIFEST.relative_to(ROOT)),
        "approval_source": "Flamestrike approved the A001 oval footprint ratio review in conversation.",
        "approved_records": approved,
        "promoted_formula_authority": {
            "primary_monolith": "120cm x 90cm measured oval footprint; raw pixel ratio remains diagnostic",
            "support_base": "140cm x 110cm measured oval footprint; raw pixel ratio remains diagnostic",
            "raw_pixel_roundness_policy": "diagnostic_only_when_X_and_Y_cm_per_pixel_differ",
            "visible_pixel_centers_policy": "comparison evidence; do not overwrite formula origin unless separately approved",
        },
        "source_proof": {
            "restart_pixel_exact": restart.get("pixel_exact"),
            "restart_changed_pixels": restart.get("changed_pixels"),
            "restart_max_rgb_delta": restart.get("max_rgb_delta"),
            "orientation_status": orientation.get("status"),
            "formula_status": formula.get("status"),
            "center_status": centers.get("status"),
            "oval_status": oval.get("status"),
        },
        "pre_geometry_state": {
            "geometry_generated": False,
            "uvs_generated": False,
            "components_moved": False,
            "components_rotated": False,
            "components_centered": False,
            "components_assembled": False,
            "inferred_fill_generated": False,
            "source_pixels_modified": False,
        },
        "next_required_step": "contact and attachment interface measurement before any geometry construction",
    }
    OVAL_APPROVAL_MANIFEST.write_text(json.dumps(approval_manifest, indent=2) + "\n")

    radial_decision = {
        "asset": ASSET_NAME,
        "status": "prior radial trace rejected as footprint-shape authority; retained as diagnostic evidence",
        "radial_trace_manifest": str(RADIAL_MANIFEST.relative_to(ROOT)) if RADIAL_MANIFEST.exists() else None,
        "decision_basis": [
            "A001 oval footprint ratio review was approved.",
            "The prior radial board looked too circular in raw source pixels.",
            "Raw source-pixel roundness is not authority when X/Y centimeter scales differ.",
            "Approved world-space footprint authority is primary 120x90cm and support/base 140x110cm.",
        ],
        "allowed_future_use": "diagnostic history only; not geometry authority; not source for mesh construction",
        "pre_geometry_state": approval_manifest["pre_geometry_state"],
    }
    RADIAL_DECISION_MANIFEST.write_text(json.dumps(radial_decision, indent=2) + "\n")


def unique_contact_lines(snap: dict[str, Any]) -> dict[tuple[str, str], dict[str, Any]]:
    found: dict[tuple[str, str], dict[str, Any]] = {}
    for anchor in snap.get("snap_anchors", []):
        if not isinstance(anchor, dict):
            continue
        view = anchor.get("source_view")
        line = anchor.get("pixel_line")
        anchor_id = str(anchor.get("anchor_id", ""))
        if view not in VIEWS or not isinstance(line, list) or len(line) != 4:
            continue
        if "PRIMARY_BOTTOM_CONTACT" in anchor_id:
            key = (str(view), "primary_to_upper_ring")
        elif "UPPER_RING_BOTTOM_CONTACT" in anchor_id:
            key = (str(view), "upper_ring_to_support_base")
        else:
            continue
        found.setdefault(
            key,
            {
                "source_view": view,
                "contact_id": key[1],
                "pixel_line": [int(v) for v in line],
                "paired_anchor_ids": [],
                "physical_layer_components": [],
                "snap_role": anchor.get("snap_role"),
            },
        )
        found[key]["paired_anchor_ids"].append(anchor_id)
        component = anchor.get("physical_layer_component")
        if component not in found[key]["physical_layer_components"]:
            found[key]["physical_layer_components"].append(component)
    return found


def measure_contacts(formula: dict[str, Any], centers: dict[str, Any], snap: dict[str, Any]) -> tuple[list[dict[str, Any]], dict[str, list[float]]]:
    views = formula["views"]
    dimensions = formula["source_dimensions_cm"]
    center_map = center_lookup(centers)
    lines = unique_contact_lines(snap)

    records: list[dict[str, Any]] = []
    for view in VIEWS:
        view_data = views[view]
        object_box = [int(v) for v in view_data["object_box_px"]]
        support_box = [int(v) for v in view_data["component_boxes_px"]["support_object"]]
        primary_box = [int(v) for v in view_data["component_boxes_px"]["primary_object"]]
        cm_per_px_x, cm_per_px_z = [float(v) for v in view_data["cm_per_pixel"]]
        bottom_y = object_box[3]
        formula_support_top_y = support_box[1]
        formula_support_top_z = (bottom_y - formula_support_top_y) * cm_per_px_z

        view_records = []
        for contact_id, label in (
            ("primary_to_upper_ring", "primary object to upper ring/socket"),
            ("upper_ring_to_support_base", "upper ring/socket to support/base"),
        ):
            contact = lines.get((view, contact_id))
            if contact is None:
                observed_y = None
                observed_z = None
                delta = None
                gate = "blocked_missing_snap_anchor"
                line_px = None
                span_cm = None
                paired_ids: list[str] = []
            else:
                line_px = contact["pixel_line"]
                observed_y = int(line_px[1])
                observed_z = (bottom_y - observed_y) * cm_per_px_z
                delta = observed_z - float(dimensions["support_height"])
                gate = "matches_support_height_formula" if abs(delta) <= CONTACT_TOLERANCE_CM else "disagrees_with_support_height_formula"
                span_cm = abs(int(line_px[2]) - int(line_px[0])) * cm_per_px_x
                paired_ids = list(contact["paired_anchor_ids"])

            view_records.append(
                {
                    "contact_id": contact_id,
                    "label": label,
                    "source_view": view,
                    "pixel_line": line_px,
                    "paired_anchor_ids": paired_ids,
                    "observed_contact_y_px": observed_y,
                    "observed_contact_z_cm": round(observed_z, 4) if observed_z is not None else None,
                    "expected_support_contact_z_cm": float(dimensions["support_height"]),
                    "delta_from_support_height_cm": round(delta, 4) if delta is not None else None,
                    "contact_line_span_cm": round(span_cm, 4) if span_cm is not None else None,
                    "gate": gate,
                }
            )

        records.append(
            {
                "source_view": view,
                "source_file": str(SOURCE.relative_to(ROOT)),
                "source_sha256": sha256_file(SOURCE),
                "object_box_px": object_box,
                "primary_formula_box_px": primary_box,
                "support_formula_box_px": support_box,
                "cm_per_pixel": [round(cm_per_px_x, 8), round(cm_per_px_z, 8)],
                "formula_support_contact_y_px": formula_support_top_y,
                "formula_support_contact_z_cm": round(formula_support_top_z, 4),
                "expected_support_height_cm": float(dimensions["support_height"]),
                "formula_support_contact_delta_cm": round(formula_support_top_z - float(dimensions["support_height"]), 4),
                "contact_records": view_records,
                "pixel_count_centers": {
                    "primary_monolith": center_map.get("primary_monolith"),
                    "upper_socket_ring": center_map.get("upper_socket_ring"),
                    "support_base": center_map.get("support_base"),
                },
                "no_geometry_generated": True,
                "components_moved": False,
                "components_assembled": False,
            }
        )
    return records, center_map


def draw_line(draw: ImageDraw.ImageDraw, line: list[int], offset: tuple[int, int], color: tuple[int, int, int], width: int = 4) -> None:
    ox, oy = offset
    draw.line((line[0] - ox, line[1] - oy, line[2] - ox, line[3] - oy), fill=color, width=width)


def create_overlay(source: Image.Image, records: list[dict[str, Any]]) -> None:
    overlay = source.copy()
    draw = ImageDraw.Draw(overlay)
    draw.rectangle((10, 10, 1180, 104), fill=(255, 255, 255), outline=(30, 30, 30), width=2)
    draw.text((24, 18), "A001 contact/interface measurement - evidence only", fill=(20, 18, 16), font=font(20))
    draw.text((24, 52), "Yellow=formula 35cm contact; red=primary-to-ring visible contact; cyan=ring-to-support visible contact.", fill=(80, 42, 92), font=font(15))
    draw.text((24, 76), "No mesh, UVs, source pixels, movement, rotation, centering, or assembly changed.", fill=(80, 42, 92), font=font(15))

    for record in records:
        object_box = record["object_box_px"]
        support_y = int(record["formula_support_contact_y_px"])
        draw.rectangle(tuple(object_box), outline=(255, 255, 255), width=2)
        draw.line((object_box[0], support_y, object_box[2], support_y), fill=COLORS["formula_contact"], width=4)
        for contact in record["contact_records"]:
            line = contact["pixel_line"]
            if not line:
                continue
            color = COLORS["primary_ring"] if contact["contact_id"] == "primary_to_upper_ring" else COLORS["ring_support"]
            draw.line(tuple(line), fill=color, width=4)

    CONTACT_OVERLAY.parent.mkdir(parents=True, exist_ok=True)
    overlay.save(CONTACT_OVERLAY)


def make_view_panel(source: Image.Image, record: dict[str, Any]) -> Image.Image:
    object_box = record["object_box_px"]
    pad = 34
    crop_box = (
        max(0, object_box[0] - pad),
        max(0, object_box[1] - pad),
        min(source.width, object_box[2] + pad),
        min(source.height, object_box[3] + pad),
    )
    panel = source.crop(crop_box).copy()
    draw = ImageDraw.Draw(panel)
    offset = (crop_box[0], crop_box[1])
    local_object = (object_box[0] - offset[0], object_box[1] - offset[1], object_box[2] - offset[0], object_box[3] - offset[1])
    draw.rectangle(local_object, outline=(255, 255, 255), width=2)
    support_y = int(record["formula_support_contact_y_px"])
    draw.line((local_object[0], support_y - offset[1], local_object[2], support_y - offset[1]), fill=COLORS["formula_contact"], width=4)

    for contact in record["contact_records"]:
        line = contact["pixel_line"]
        if not line:
            continue
        color = COLORS["primary_ring"] if contact["contact_id"] == "primary_to_upper_ring" else COLORS["ring_support"]
        draw_line(draw, line, offset, color)

    return panel.resize((360, 430), RESAMPLE_LANCZOS)


def create_review_board(source: Image.Image, records: list[dict[str, Any]]) -> None:
    board = Image.new("RGB", (1900, 1420), (245, 243, 238))
    draw = ImageDraw.Draw(board)
    draw.text((40, 28), "A001 Contact Interface Review", fill=(24, 21, 18), font=font(30))
    draw.text((40, 74), "Oval footprints approved. This board checks measured contact levels before geometry.", fill=(55, 48, 42), font=font(18))

    panel_positions = [(40, 130), (505, 130), (970, 130), (1435, 130)]
    for record, pos in zip(records, panel_positions):
        panel = make_view_panel(source, record)
        board.paste(panel, pos)
        draw.rectangle((pos[0], pos[1], pos[0] + panel.width, pos[1] + panel.height), outline=(70, 64, 56), width=2)
        draw.text((pos[0], pos[1] + panel.height + 12), str(record["source_view"]), fill=(32, 28, 24), font=font(20))

    legend_x, legend_y = 40, 608
    legend = [
        ("formula_contact", "formula support contact, expected 35 cm"),
        ("primary_ring", "visible primary-to-upper-ring contact"),
        ("ring_support", "visible upper-ring-to-support contact"),
    ]
    for index, (key, label) in enumerate(legend):
        y = legend_y + index * 30
        draw.rectangle((legend_x, y + 5, legend_x + 24, y + 23), fill=COLORS[key])
        draw.text((legend_x + 36, y), label, fill=(42, 36, 30), font=font(17))

    table_x, table_y = 40, 730
    draw.rectangle((table_x, table_y, 1810, 1285), fill=(255, 255, 255), outline=(75, 68, 62), width=2)
    draw.text((table_x + 18, table_y + 18), "Contact Height Check", fill=(24, 21, 18), font=font(22))
    draw.text((table_x + 18, table_y + 52), f"Tolerance: {CONTACT_TOLERANCE_CM} cm. Any disagreement blocks geometry until resolved.", fill=(48, 42, 36), font=font(16))

    headers = ["view", "formula y/z", "primary-ring y/z", "delta", "ring-support y/z", "delta", "gate"]
    col_x = [58, 205, 445, 705, 835, 1100, 1230]
    for x, header in zip(col_x, headers):
        draw.text((x, table_y + 92), header, fill=(24, 21, 18), font=font(15))

    any_disagreement = False
    for row, record in enumerate(records):
        y = table_y + 126 + row * 74
        contacts = {contact["contact_id"]: contact for contact in record["contact_records"]}
        primary_ring = contacts["primary_to_upper_ring"]
        ring_support = contacts["upper_ring_to_support_base"]
        gates = [primary_ring["gate"], ring_support["gate"]]
        row_fail = any(gate != "matches_support_height_formula" for gate in gates)
        any_disagreement = any_disagreement or row_fail
        gate_text = "BLOCKED" if row_fail else "PASS"
        gate_color = (160, 28, 28) if row_fail else (20, 120, 62)
        draw.text((col_x[0], y), str(record["source_view"]), fill=(42, 36, 30), font=font(15))
        draw.text((col_x[1], y), f"{record['formula_support_contact_y_px']} / {record['formula_support_contact_z_cm']}cm", fill=(42, 36, 30), font=font(15))
        draw.text((col_x[2], y), f"{primary_ring['observed_contact_y_px']} / {primary_ring['observed_contact_z_cm']}cm", fill=(42, 36, 30), font=font(15))
        draw.text((col_x[3], y), f"{primary_ring['delta_from_support_height_cm']}cm", fill=(42, 36, 30), font=font(15))
        draw.text((col_x[4], y), f"{ring_support['observed_contact_y_px']} / {ring_support['observed_contact_z_cm']}cm", fill=(42, 36, 30), font=font(15))
        draw.text((col_x[5], y), f"{ring_support['delta_from_support_height_cm']}cm", fill=(42, 36, 30), font=font(15))
        draw.text((col_x[6], y), gate_text, fill=gate_color, font=font(15))

    conclusion_y = table_y + 444
    conclusion = [
        "Finding: visible source contacts show two layer levels, not one flattened support contact.",
        "Implication: upper ring/socket needs its own measured height/contact interval before mesh construction.",
        "No geometry should be generated until this contact formula is approved or revised.",
    ]
    if any_disagreement:
        draw.text((table_x + 18, conclusion_y), "HARD GATE: BLOCKED BEFORE GEOMETRY", fill=(160, 28, 28), font=font(20))
    else:
        draw.text((table_x + 18, conclusion_y), "HARD GATE: CONTACT HEIGHTS MATCH CURRENT FORMULA", fill=(20, 120, 62), font=font(20))
    for index, line in enumerate(conclusion):
        draw.text((table_x + 18, conclusion_y + 36 + index * 26), f"- {line}", fill=(48, 42, 36), font=font(16))

    board.save(CONTACT_REVIEW_BOARD)


def build_contact_manifest(
    restart: dict[str, Any],
    orientation: dict[str, Any],
    formula: dict[str, Any],
    centers: dict[str, Any],
    snap: dict[str, Any],
    records: list[dict[str, Any]],
) -> dict[str, Any]:
    failing = []
    for record in records:
        for contact in record["contact_records"]:
            if contact["gate"] != "matches_support_height_formula":
                failing.append(
                    {
                        "source_view": record["source_view"],
                        "contact_id": contact["contact_id"],
                        "gate": contact["gate"],
                        "delta_from_support_height_cm": contact["delta_from_support_height_cm"],
                    }
                )

    return {
        "asset": ASSET_NAME,
        "status": "A001 contact/interface measurement evidence recorded before geometry",
        "source": str(SOURCE.relative_to(ROOT)),
        "source_sha256": sha256_file(SOURCE),
        "source_scanline_manifest": str(RESTART_MANIFEST.relative_to(ROOT)),
        "orientation_pixel_manifest": str(ORIENTATION_MANIFEST.relative_to(ROOT)),
        "measurement_formula_manifest": str(FORMULA_MANIFEST.relative_to(ROOT)),
        "pixel_count_center_manifest": str(CENTER_MANIFEST.relative_to(ROOT)),
        "snap_anchor_manifest": str(SNAP_MANIFEST.relative_to(ROOT)),
        "oval_footprint_approval_manifest": str(OVAL_APPROVAL_MANIFEST.relative_to(ROOT)),
        "radial_trace_review_decision": str(RADIAL_DECISION_MANIFEST.relative_to(ROOT)),
        "contact_interface_overlay": str(CONTACT_OVERLAY.relative_to(ROOT)),
        "contact_interface_review_board": str(CONTACT_REVIEW_BOARD.relative_to(ROOT)),
        "source_proof": {
            "restart_pixel_exact": restart.get("pixel_exact"),
            "restart_changed_pixels": restart.get("changed_pixels"),
            "restart_max_rgb_delta": restart.get("max_rgb_delta"),
            "orientation_status": orientation.get("status"),
            "formula_status": formula.get("status"),
            "center_status": centers.get("status"),
            "snap_status": snap.get("status"),
        },
        "pre_geometry_state": {
            "geometry_generated": False,
            "uvs_generated": False,
            "components_moved": False,
            "components_rotated": False,
            "components_centered": False,
            "components_assembled": False,
            "inferred_fill_generated": False,
            "source_pixels_modified": False,
        },
        "contact_formula_policy": {
            "current_formula_expected_support_height_cm": formula["source_dimensions_cm"]["support_height"],
            "contact_tolerance_cm": CONTACT_TOLERANCE_CM,
            "primary_to_upper_ring_and_upper_ring_to_support_are_separate": True,
            "single_flat_support_contact_is_not_approved_if_visible_lines_disagree": True,
            "visible_contact_lines_are_source_evidence": True,
        },
        "contact_interface_records": records,
        "hard_gate_status": "blocked_before_geometry" if failing else "passed_contact_height_check",
        "failing_contact_checks": failing,
        "required_next_decision": [
            "approve a separate upper ring/socket height interval derived from visible source contact lines",
            "or revise the contact-line selection if any source line was marked incorrectly",
            "then update the formula archive before geometry construction",
        ],
    }


def main() -> None:
    restart, orientation, formula, centers, snap, oval = verify_preconditions()
    source = Image.open(SOURCE).convert("RGB")
    EVIDENCE_DIR.mkdir(parents=True, exist_ok=True)

    write_approval_records(restart, orientation, formula, centers, oval)
    contact_records, _center_map = measure_contacts(formula, centers, snap)
    create_overlay(source, contact_records)
    create_review_board(source, contact_records)

    manifest = build_contact_manifest(restart, orientation, formula, centers, snap, contact_records)
    CONTACT_MANIFEST.write_text(json.dumps(manifest, indent=2) + "\n")

    print(f"A001 oval approval manifest: {OVAL_APPROVAL_MANIFEST}")
    print(f"A001 radial decision manifest: {RADIAL_DECISION_MANIFEST}")
    print(f"A001 contact interface manifest: {CONTACT_MANIFEST}")
    print(f"A001 contact interface overlay: {CONTACT_OVERLAY}")
    print(f"A001 contact interface review board: {CONTACT_REVIEW_BOARD}")
    print(f"hard_gate_status={manifest['hard_gate_status']}")
    for record in contact_records:
        view = record["source_view"]
        contacts = {item["contact_id"]: item for item in record["contact_records"]}
        print(
            f"{view}: formula={record['formula_support_contact_z_cm']}cm "
            f"primary-ring={contacts['primary_to_upper_ring']['observed_contact_z_cm']}cm "
            f"ring-support={contacts['upper_ring_to_support_base']['observed_contact_z_cm']}cm"
        )
    print("geometry_generated=False components_moved=False components_assembled=False")


if __name__ == "__main__":
    main()
