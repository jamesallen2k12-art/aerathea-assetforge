#!/usr/bin/env python3
"""Create A001 layered contact interval formula evidence.

This pass converts the contact-interface blocker into an explicit formula
candidate: the upper ring/socket is measured as its own view-owned interval
between primary-to-ring and ring-to-support contact lines.

No averages are used. No mesh, UVs, textures, movement, rotation, centering, or
assembly is generated.
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
EVIDENCE_DIR = OUT_DIR / "FreshEvidence" / "LayeredContactFormula"

RESTART_MANIFEST = OUT_DIR / f"{ASSET_NAME}_A001BlueprintRestartManifest.json"
ORIENTATION_MANIFEST = OUT_DIR / f"{ASSET_NAME}_A001OrientationPixelManifest.json"
FORMULA_MANIFEST = OUT_DIR / f"{ASSET_NAME}_A001MeasurementFormulaManifest.json"
CENTER_MANIFEST = OUT_DIR / f"{ASSET_NAME}_A001PixelCountCenterManifest.json"
OVAL_APPROVAL_MANIFEST = OUT_DIR / f"{ASSET_NAME}_A001OvalFootprintApprovalManifest.json"
CONTACT_MANIFEST = OUT_DIR / f"{ASSET_NAME}_A001ContactInterfaceManifest.json"

LAYERED_MANIFEST = OUT_DIR / f"{ASSET_NAME}_A001LayeredContactFormulaManifest.json"
LAYERED_OVERLAY = OUT_DIR / f"{ASSET_NAME}_A001LayeredContactFormulaOverlay.png"
LAYERED_REVIEW_BOARD = OUT_DIR / f"{ASSET_NAME}_A001LayeredContactFormulaReviewBoard.png"

VIEWS = ("front", "back", "left", "right")

COLORS = {
    "old_formula": (245, 207, 48),
    "upper_contact": (228, 42, 42),
    "lower_contact": (0, 185, 255),
    "interval_fill": (255, 138, 30),
    "support_fill": (70, 130, 155),
    "primary_fill": (125, 64, 64),
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
    for path in (RESTART_MANIFEST, ORIENTATION_MANIFEST, FORMULA_MANIFEST, CENTER_MANIFEST, OVAL_APPROVAL_MANIFEST, CONTACT_MANIFEST):
        if not path.exists():
            raise SystemExit(f"Missing required precondition manifest: {path}")

    restart = read_json(RESTART_MANIFEST)
    orientation = read_json(ORIENTATION_MANIFEST)
    formula = read_json(FORMULA_MANIFEST)
    centers = read_json(CENTER_MANIFEST)
    oval_approval = read_json(OVAL_APPROVAL_MANIFEST)
    contact = read_json(CONTACT_MANIFEST)

    if restart.get("pixel_exact") is not True or restart.get("changed_pixels") != 0 or restart.get("max_rgb_delta") != 0:
        raise SystemExit("A001 source scanline proof is not exact; layered contact pass is blocked.")

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

    for label, manifest in (("formula", formula), ("center", centers), ("oval_approval", oval_approval), ("contact", contact)):
        state = manifest.get("pre_geometry_state")
        if not isinstance(state, dict):
            raise SystemExit(f"{label} manifest is missing pre_geometry_state.")
        for key in ("geometry_generated", "uvs_generated", "components_moved", "components_rotated", "components_centered", "components_assembled", "inferred_fill_generated"):
            if state.get(key) is not False:
                raise SystemExit(f"{label} manifest is no longer pre-geometry clean: {key}")

    if contact.get("hard_gate_status") != "blocked_before_geometry":
        raise SystemExit("Layered contact formula pass expects the prior contact hard gate to be blocked.")

    return restart, orientation, formula, centers, oval_approval, contact


def contact_lookup(record: dict[str, Any]) -> dict[str, dict[str, Any]]:
    return {str(contact["contact_id"]): contact for contact in record["contact_records"]}


def build_interval_records(contact: dict[str, Any], formula: dict[str, Any]) -> list[dict[str, Any]]:
    records: list[dict[str, Any]] = []
    dimensions = formula["source_dimensions_cm"]
    for item in contact.get("contact_interface_records", []):
        if not isinstance(item, dict):
            continue
        view = str(item["source_view"])
        if view not in VIEWS:
            continue
        contacts = contact_lookup(item)
        upper = contacts["primary_to_upper_ring"]
        lower = contacts["upper_ring_to_support_base"]

        upper_y = int(upper["observed_contact_y_px"])
        lower_y = int(lower["observed_contact_y_px"])
        upper_z = float(upper["observed_contact_z_cm"])
        lower_z = float(lower["observed_contact_z_cm"])
        interval_px = abs(lower_y - upper_y)
        interval_cm = upper_z - lower_z
        support_visible_cm = lower_z
        primary_start_cm = upper_z
        old_formula_cm = float(item["formula_support_contact_z_cm"])

        records.append(
            {
                "source_view": view,
                "source_file": str(SOURCE.relative_to(ROOT)),
                "source_sha256": sha256_file(SOURCE),
                "object_box_px": item["object_box_px"],
                "cm_per_pixel": item["cm_per_pixel"],
                "old_single_support_formula_contact_y_px": item["formula_support_contact_y_px"],
                "old_single_support_formula_contact_z_cm": old_formula_cm,
                "old_authored_support_height_cm": float(dimensions["support_height"]),
                "upper_ring_top_contact": {
                    "contact_id": "primary_to_upper_ring",
                    "world_meaning": "primary object bottom touching upper ring/socket top",
                    "pixel_line": upper["pixel_line"],
                    "paired_anchor_ids": upper["paired_anchor_ids"],
                    "y_px": upper_y,
                    "z_cm": round(upper_z, 4),
                },
                "upper_ring_bottom_contact": {
                    "contact_id": "upper_ring_to_support_base",
                    "world_meaning": "upper ring/socket bottom touching support/base top",
                    "pixel_line": lower["pixel_line"],
                    "paired_anchor_ids": lower["paired_anchor_ids"],
                    "y_px": lower_y,
                    "z_cm": round(lower_z, 4),
                },
                "upper_ring_interval_px": interval_px,
                "upper_ring_interval_cm": round(interval_cm, 4),
                "support_visible_height_to_ring_bottom_cm": round(support_visible_cm, 4),
                "primary_starts_at_ring_top_cm": round(primary_start_cm, 4),
                "primary_ring_delta_from_old_support_formula_cm": round(upper_z - old_formula_cm, 4),
                "ring_support_delta_from_old_support_formula_cm": round(lower_z - old_formula_cm, 4),
                "no_average_used": True,
                "geometry_authority_status": "candidate_pending_review",
                "formula_role": "view-owned contact-height station; use as side-profile anchor after approval",
            }
        )
    return records


def draw_transparent_rect(panel: Image.Image, box: tuple[int, int, int, int], color: tuple[int, int, int], alpha: int) -> None:
    overlay = Image.new("RGBA", panel.size, (0, 0, 0, 0))
    draw = ImageDraw.Draw(overlay)
    draw.rectangle(box, fill=(*color, alpha))
    panel.alpha_composite(overlay)


def draw_source_lines(draw: ImageDraw.ImageDraw, record: dict[str, Any], offset: tuple[int, int]) -> None:
    ox, oy = offset
    object_box = record["object_box_px"]
    local_object = (object_box[0] - ox, object_box[1] - oy, object_box[2] - ox, object_box[3] - oy)
    draw.rectangle(local_object, outline=(255, 255, 255), width=2)
    old_y = int(record["old_single_support_formula_contact_y_px"]) - oy
    draw.line((local_object[0], old_y, local_object[2], old_y), fill=COLORS["old_formula"], width=4)
    upper = record["upper_ring_top_contact"]["pixel_line"]
    lower = record["upper_ring_bottom_contact"]["pixel_line"]
    draw.line((upper[0] - ox, upper[1] - oy, upper[2] - ox, upper[3] - oy), fill=COLORS["upper_contact"], width=5)
    draw.line((lower[0] - ox, lower[1] - oy, lower[2] - ox, lower[3] - oy), fill=COLORS["lower_contact"], width=5)


def create_overlay(source: Image.Image, records: list[dict[str, Any]]) -> None:
    overlay = source.convert("RGBA")
    draw = ImageDraw.Draw(overlay)
    draw.rectangle((10, 10, 1230, 108), fill=(255, 255, 255, 245), outline=(30, 30, 30), width=2)
    draw.text((24, 18), "A001 layered contact formula - evidence only", fill=(20, 18, 16), font=font(20))
    draw.text((24, 52), "Red=upper ring top contact; cyan=upper ring bottom contact; orange band=measured ring/socket interval.", fill=(80, 42, 92), font=font(15))
    draw.text((24, 78), "Per-view measured intervals only. No averaging, mesh generation, movement, or assembly.", fill=(80, 42, 92), font=font(15))

    for record in records:
        box = record["object_box_px"]
        upper_y = int(record["upper_ring_top_contact"]["y_px"])
        lower_y = int(record["upper_ring_bottom_contact"]["y_px"])
        draw_transparent_rect(overlay, (box[0], upper_y, box[2], lower_y), COLORS["interval_fill"], 72)
        draw_source_lines(draw, record, (0, 0))
    overlay.convert("RGB").save(LAYERED_OVERLAY)


def make_panel(source: Image.Image, record: dict[str, Any]) -> Image.Image:
    object_box = record["object_box_px"]
    pad = 34
    crop_box = (
        max(0, object_box[0] - pad),
        max(0, object_box[1] - pad),
        min(source.width, object_box[2] + pad),
        min(source.height, object_box[3] + pad),
    )
    panel = source.crop(crop_box).convert("RGBA")
    offset = (crop_box[0], crop_box[1])
    upper_y = int(record["upper_ring_top_contact"]["y_px"]) - offset[1]
    lower_y = int(record["upper_ring_bottom_contact"]["y_px"]) - offset[1]
    draw_transparent_rect(panel, (0, min(upper_y, lower_y), panel.width, max(upper_y, lower_y)), COLORS["interval_fill"], 90)
    draw = ImageDraw.Draw(panel)
    draw_source_lines(draw, record, offset)
    return panel.convert("RGB").resize((360, 430), RESAMPLE_LANCZOS)


def create_review_board(source: Image.Image, records: list[dict[str, Any]]) -> None:
    board = Image.new("RGB", (1900, 1420), (245, 243, 238))
    draw = ImageDraw.Draw(board)
    draw.text((40, 28), "A001 Layered Contact Formula Review", fill=(24, 21, 18), font=font(30))
    draw.text((40, 74), "Upper ring/socket measured as its own interval. Evidence only; no mesh generated.", fill=(55, 48, 42), font=font(18))

    panel_positions = [(40, 130), (505, 130), (970, 130), (1435, 130)]
    for record, pos in zip(records, panel_positions):
        panel = make_panel(source, record)
        board.paste(panel, pos)
        draw.rectangle((pos[0], pos[1], pos[0] + panel.width, pos[1] + panel.height), outline=(70, 64, 56), width=2)
        draw.text((pos[0], pos[1] + panel.height + 12), str(record["source_view"]), fill=(32, 28, 24), font=font(20))

    legend_x, legend_y = 40, 610
    legend = [
        ("upper_contact", "upper ring top contact: primary object begins here"),
        ("lower_contact", "upper ring bottom contact: support/base reaches here"),
        ("interval_fill", "measured upper ring/socket interval"),
        ("old_formula", "old single support-height contact, retained as disagreement evidence"),
    ]
    for index, (key, label) in enumerate(legend):
        y = legend_y + index * 30
        draw.rectangle((legend_x, y + 5, legend_x + 24, y + 23), fill=COLORS[key])
        draw.text((legend_x + 36, y), label, fill=(42, 36, 30), font=font(17))

    table_x, table_y = 40, 760
    draw.rectangle((table_x, table_y, 1810, 1305), fill=(255, 255, 255), outline=(75, 68, 62), width=2)
    draw.text((table_x + 18, table_y + 18), "Per-View Contact Interval Formula", fill=(24, 21, 18), font=font(22))
    draw.text((table_x + 18, table_y + 52), "No averages used. These are exact source-view station values pending approval.", fill=(48, 42, 36), font=font(16))

    headers = ["view", "ring bottom z", "ring top z", "ring interval", "support visible", "old formula z", "status"]
    col_x = [58, 195, 400, 600, 810, 1040, 1260]
    for x, header in zip(col_x, headers):
        draw.text((x, table_y + 92), header, fill=(24, 21, 18), font=font(15))

    for row, record in enumerate(records):
        y = table_y + 126 + row * 66
        draw.text((col_x[0], y), record["source_view"], fill=(42, 36, 30), font=font(15))
        draw.text((col_x[1], y), f"{record['upper_ring_bottom_contact']['z_cm']} cm", fill=(42, 36, 30), font=font(15))
        draw.text((col_x[2], y), f"{record['upper_ring_top_contact']['z_cm']} cm", fill=(42, 36, 30), font=font(15))
        draw.text((col_x[3], y), f"{record['upper_ring_interval_cm']} cm / {record['upper_ring_interval_px']} px", fill=(42, 36, 30), font=font(15))
        draw.text((col_x[4], y), f"{record['support_visible_height_to_ring_bottom_cm']} cm", fill=(42, 36, 30), font=font(15))
        draw.text((col_x[5], y), f"{record['old_single_support_formula_contact_z_cm']} cm", fill=(42, 36, 30), font=font(15))
        draw.text((col_x[6], y), "candidate", fill=(120, 74, 18), font=font(15))

    notes_y = table_y + 416
    notes = [
        "The old 35 cm support height remains calibration evidence, not layer-contact authority for this pass.",
        "Geometry remains blocked until this layered contact formula is approved or the source lines are revised.",
        "Later mesh construction must use these stations as contact anchors; do not flatten or average them.",
    ]
    draw.text((table_x + 18, notes_y), "Hard Gate State: candidate formula ready for review, geometry still blocked", fill=(160, 86, 20), font=font(20))
    for index, note in enumerate(notes):
        draw.text((table_x + 18, notes_y + 36 + index * 26), f"- {note}", fill=(48, 42, 36), font=font(16))

    board.save(LAYERED_REVIEW_BOARD)


def build_manifest(
    restart: dict[str, Any],
    orientation: dict[str, Any],
    formula: dict[str, Any],
    centers: dict[str, Any],
    oval_approval: dict[str, Any],
    contact: dict[str, Any],
    records: list[dict[str, Any]],
) -> dict[str, Any]:
    return {
        "asset": ASSET_NAME,
        "status": "A001 layered contact interval formula candidate recorded before geometry",
        "source": str(SOURCE.relative_to(ROOT)),
        "source_sha256": sha256_file(SOURCE),
        "source_scanline_manifest": str(RESTART_MANIFEST.relative_to(ROOT)),
        "orientation_pixel_manifest": str(ORIENTATION_MANIFEST.relative_to(ROOT)),
        "measurement_formula_manifest": str(FORMULA_MANIFEST.relative_to(ROOT)),
        "pixel_count_center_manifest": str(CENTER_MANIFEST.relative_to(ROOT)),
        "oval_footprint_approval_manifest": str(OVAL_APPROVAL_MANIFEST.relative_to(ROOT)),
        "contact_interface_manifest": str(CONTACT_MANIFEST.relative_to(ROOT)),
        "layered_contact_formula_overlay": str(LAYERED_OVERLAY.relative_to(ROOT)),
        "layered_contact_formula_review_board": str(LAYERED_REVIEW_BOARD.relative_to(ROOT)),
        "source_proof": {
            "restart_pixel_exact": restart.get("pixel_exact"),
            "restart_changed_pixels": restart.get("changed_pixels"),
            "restart_max_rgb_delta": restart.get("max_rgb_delta"),
            "orientation_status": orientation.get("status"),
            "formula_status": formula.get("status"),
            "center_status": centers.get("status"),
            "oval_approval_status": oval_approval.get("status"),
            "contact_status": contact.get("status"),
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
        "formula_policy": {
            "upper_ring_socket_is_separate_layer": True,
            "primary_to_upper_ring_contact_is_distinct": True,
            "upper_ring_to_support_contact_is_distinct": True,
            "single_support_height_formula_superseded_for_visible_contact_authority": True,
            "global_average_used": False,
            "view_owned_station_formula": True,
            "old_support_height_role": "calibration/disagreement evidence until a revised global layer model is approved",
        },
        "layered_contact_interval_records": records,
        "geometry_use_status": "candidate_pending_review; geometry_blocked_until_approved_and_formula_archive_promoted",
        "blocked_until_declared_next": [
            "review layered contact formula board",
            "approve or revise the source contact lines",
            "promote this layered formula into the A001 formula archive if approved",
            "then continue to edge/angle station checks before mesh generation",
        ],
    }


def main() -> None:
    restart, orientation, formula, centers, oval_approval, contact = verify_preconditions()
    source = Image.open(SOURCE).convert("RGB")
    EVIDENCE_DIR.mkdir(parents=True, exist_ok=True)
    records = build_interval_records(contact, formula)
    create_overlay(source, records)
    create_review_board(source, records)
    manifest = build_manifest(restart, orientation, formula, centers, oval_approval, contact, records)
    LAYERED_MANIFEST.write_text(json.dumps(manifest, indent=2) + "\n")

    print(f"A001 layered contact formula manifest: {LAYERED_MANIFEST}")
    print(f"A001 layered contact formula overlay: {LAYERED_OVERLAY}")
    print(f"A001 layered contact formula review board: {LAYERED_REVIEW_BOARD}")
    for record in records:
        print(
            f"{record['source_view']}: lower={record['upper_ring_bottom_contact']['z_cm']}cm "
            f"upper={record['upper_ring_top_contact']['z_cm']}cm "
            f"interval={record['upper_ring_interval_cm']}cm no_average=True"
        )
    print("geometry_generated=False components_moved=False components_assembled=False")


if __name__ == "__main__":
    main()
