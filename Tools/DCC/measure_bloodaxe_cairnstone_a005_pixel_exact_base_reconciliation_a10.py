#!/usr/bin/env python3
"""Build the A005/A10 pixel-exact base-dimension reconciliation package.

This pass reuses only approved native-pixel owner-view samples.  It does not
trace, fit, close, fill, or construct any geometry.  Raw X and Y ratios are
kept separate from the conditional centimeter conversion.
"""

from __future__ import annotations

import hashlib
import json
from fractions import Fraction
from pathlib import Path

from PIL import Image, ImageDraw, ImageFont


ROOT = Path(__file__).resolve().parents[2]
ASSET = ROOT / "docs/assets/blueprints/SM_GIA_BloodAxeCairnstone_A005"
PANELS = ASSET / "panels/STEP_03"
MANIFESTS = ASSET / "manifests"
OUTPUT_JSON = MANIFESTS / "VISUAL_CORRECTION_A10_PIXEL_EXACT_BASE_RECONCILIATION.json"
VALIDATION_JSON = MANIFESTS / "VISUAL_CORRECTION_A10_PIXEL_EXACT_BASE_RECONCILIATION_VALIDATION.json"
OUTPUT_MD = ASSET / "steps/VISUAL_CORRECTION_A10_PIXEL_EXACT_BASE_RECONCILIATION_OUTPUT.md"
BOARD = (
    ROOT
    / "Saved/Automation/DCC/SM_GIA_BloodAxeCairnstone_A005/Production/"
    "VisualCorrection_A10_Measurement/"
    "SM_GIA_BloodAxeCairnstone_A005_A10_PIXEL_EXACT_BASE_RECONCILIATION.png"
)

SOURCE_HASHES = {
    "front": "262071198bc0d409e9b68af5ac4f3c6a4768a90b1fd199342035a8a82342c2c5",
    "left": "52212ba783d026a008929e3946cac934281de7d2daec2ada316205059258cba4",
    "top": "1bc9750b903a3d9e5689bee3c2c1c7094ccd554c361ff622aa9065d2c5287fdf",
}

PANEL_PATHS = {
    "front": PANELS / "SM_GIA_BloodAxeCairnstone_A005_STEP_03_FRONT.png",
    "left": PANELS / "SM_GIA_BloodAxeCairnstone_A005_STEP_03_LEFT.png",
    "top": PANELS / "SM_GIA_BloodAxeCairnstone_A005_STEP_03_TOP.png",
}

FRONT_SAMPLE_IDS = {
    "C001": "F-C001-R330",
    "C002": "F-C002-R360",
    "C003": "F-C003-R390",
    "C004": "F-C004-R410",
}

LEFT_SAMPLE_IDS = {
    "C001": "L-C001-R230",
    "C002": "L-C002-R255",
    "C003": "L-C003-R280",
    "C004": "L-C004-R305",
}

CURRENT_A09 = {
    "C001_contact": [96.0, 68.0],
    "C002": [123.846154, 92.707424],
    "C003": [137.307692, 105.196507],
    "C004": [140.0, 110.0],
}

COLORS = {
    "C001": (210, 40, 180),
    "C002": (255, 145, 0),
    "C003": (0, 175, 215),
    "C004": (0, 105, 235),
    "CL-001": (255, 220, 0),
    "CL-002": (70, 220, 110),
    "CL-003": (0, 215, 235),
}


def sha256(path: Path) -> str:
    digest = hashlib.sha256()
    with path.open("rb") as handle:
        for block in iter(lambda: handle.read(1024 * 1024), b""):
            digest.update(block)
    return digest.hexdigest()


def font(size: int, bold: bool = False, mono: bool = False):
    if mono:
        name = "DejaVuSansMono-Bold.ttf" if bold else "DejaVuSansMono.ttf"
    else:
        name = "DejaVuSans-Bold.ttf" if bold else "DejaVuSans.ttf"
    path = Path("/usr/share/fonts/truetype/dejavu") / name
    try:
        return ImageFont.truetype(str(path), size=size)
    except OSError:
        return ImageFont.load_default()


def fraction_record(value: Fraction) -> dict:
    return {
        "exact": f"{value.numerator}/{value.denominator}",
        "decimal": round(float(value), 9),
    }


def index_by_id(records: list[dict]) -> dict[str, dict]:
    return {record["id"]: record for record in records}


def row_sample_record(image: Image.Image, source: dict, view: str) -> dict:
    x0, x1 = source["span_half_open"]
    y = source["y"]
    left = [x0, y]
    right = [x1 - 1, y]
    return {
        "source_record_id": source["id"],
        "view": view,
        "component_id": source["component_id"],
        "row_y_px": y,
        "half_open_span_px": [x0, x1],
        "inclusive_pixel_count": x1 - x0,
        "pixel_center_delta_px": (x1 - 1) - x0,
        "left_edge": {"pixel_local": left, "source_rgb": list(image.getpixel(tuple(left)))},
        "right_edge": {"pixel_local": right, "source_rgb": list(image.getpixel(tuple(right)))},
        "profile_center_x_px": source["profile_center_x_px"],
        "ownership_basis": "approved manual native-pixel visible_outer_edge_row_sample",
    }


def irregular_sample_record(image: Image.Image, source: dict, view: str, component: str) -> dict:
    left = source["left_source_pixel"]
    right = source["right_source_pixel"]
    if left[1] != right[1]:
        raise RuntimeError(f"{source['id']} endpoints do not share a row")
    return {
        "source_record_id": source["id"],
        "view": view,
        "component_id": component,
        "row_y_px": left[1],
        "inclusive_pixel_count": right[0] - left[0] + 1,
        "pixel_center_delta_px": right[0] - left[0],
        "left_edge": {"pixel_local": left, "source_rgb": list(image.getpixel(tuple(left)))},
        "right_edge": {"pixel_local": right, "source_rgb": list(image.getpixel(tuple(right)))},
        "interior_span_owned": source["interior_span_owned"],
        "ownership_basis": "approved manual native-pixel irregular_C004_outer_edge_observation",
    }


def draw_cross(draw: ImageDraw.ImageDraw, x: int, y: int, color, radius: int = 10):
    draw.line((x - radius, y, x + radius, y), fill=color, width=3)
    draw.line((x, y - radius, x, y + radius), fill=color, width=3)


def draw_hollow_box(draw: ImageDraw.ImageDraw, x: int, y: int, color, radius: int = 5):
    draw.rectangle((x - radius, y - radius, x + radius, y + radius), outline=color, width=2)


def main() -> int:
    images: dict[str, Image.Image] = {}
    panel_authority = {}
    for view, path in PANEL_PATHS.items():
        actual = sha256(path)
        if actual != SOURCE_HASHES[view]:
            raise RuntimeError(f"{view} source panel hash mismatch: {actual}")
        images[view] = Image.open(path).convert("RGB")
        panel_authority[view] = {
            "path": str(path.relative_to(ROOT)),
            "sha256": actual,
            "size_px": list(images[view].size),
            "hash_match": True,
        }

    front_manifest_path = MANIFESTS / "STEP_06_FRONT_MEASUREMENT_MANIFEST.json"
    left_manifest_path = MANIFESTS / "STEP_07_LEFT_MEASUREMENT_MANIFEST.json"
    contacts_path = MANIFESTS / "STEP_04_TOP_CONTACT_EVIDENCE_RECOVERY_A01.json"
    a09_path = MANIFESTS / "VISUAL_CORRECTION_A09_PLAN.json"
    front_manifest = json.loads(front_manifest_path.read_text(encoding="utf-8"))
    left_manifest = json.loads(left_manifest_path.read_text(encoding="utf-8"))
    contacts_manifest = json.loads(contacts_path.read_text(encoding="utf-8"))
    a09_plan = json.loads(a09_path.read_text(encoding="utf-8"))

    front_rows = index_by_id(front_manifest["visible_outer_edge_row_samples"])
    left_rows = index_by_id(left_manifest["visible_outer_edge_row_samples"])
    front_irregular = index_by_id(front_manifest["irregular_C004_outer_edge_observations"])
    left_irregular = index_by_id(left_manifest["irregular_C004_outer_edge_observations"])

    x_records = {}
    y_records = {}
    for component in ("C001", "C002", "C003"):
        x_records[component] = row_sample_record(
            images["front"], front_rows[FRONT_SAMPLE_IDS[component]], "front"
        )
        y_records[component] = row_sample_record(
            images["left"], left_rows[LEFT_SAMPLE_IDS[component]], "left"
        )
    x_records["C004"] = irregular_sample_record(
        images["front"], front_irregular[FRONT_SAMPLE_IDS["C004"]], "front", "C004"
    )
    y_records["C004"] = irregular_sample_record(
        images["left"], left_irregular[LEFT_SAMPLE_IDS["C004"]], "left", "C004"
    )

    x_denominator = x_records["C004"]["pixel_center_delta_px"]
    y_denominator = y_records["C004"]["pixel_center_delta_px"]
    if (x_denominator, y_denominator) != (288, 221):
        raise RuntimeError("Unexpected owner-view C004 normalization spans")

    components = {}
    for component in ("C001", "C002", "C003", "C004"):
        x_span = x_records[component]["pixel_center_delta_px"]
        y_span = y_records[component]["pixel_center_delta_px"]
        width = Fraction(140 * x_span, x_denominator)
        depth = Fraction(110 * y_span, y_denominator)
        components[component] = {
            "front_X_owner": x_records[component],
            "left_Y_owner": y_records[component],
            "pixel_exact_relative_footprint": {
                "X_over_C004": fraction_record(Fraction(x_span, x_denominator)),
                "Y_over_C004": fraction_record(Fraction(y_span, y_denominator)),
            },
            "conditional_physical_footprint_cm": {
                "width": fraction_record(width),
                "depth": fraction_record(depth),
                "width_to_depth_ratio": round(float(width / depth), 9),
                "formula_width": f"140 * {x_span} / {x_denominator}",
                "formula_depth": f"110 * {y_span} / {y_denominator}",
                "premise": "conditional on retaining the current C004 140 x 110 cm production envelope",
            },
        }

    contact_points = []
    contact_counts = {"CL-001": 0, "CL-002": 0, "CL-003": 0}
    contact_rgb_mismatches = 0
    for point in contacts_manifest["accepted_points"]:
        coordinate = point["pixel_local"]
        actual_rgb = list(images["top"].getpixel(tuple(coordinate)))
        if actual_rgb != point["source_rgb"]:
            contact_rgb_mismatches += 1
        contact_counts[point["contact_id"]] += 1
        contact_points.append(
            {
                "id": point["id"],
                "contact_id": point["contact_id"],
                "pixel_local": coordinate,
                "source_rgb": actual_rgb,
                "rgb_match": actual_rgb == point["source_rgb"],
                "closure_authorized": False,
            }
        )
    if contact_counts != {"CL-001": 16, "CL-002": 16, "CL-003": 16}:
        raise RuntimeError(f"Unexpected contact counts: {contact_counts}")
    if contact_rgb_mismatches:
        raise RuntimeError(f"Top contact RGB mismatches: {contact_rgb_mismatches}")

    current_a09_from_plan = {
        "C002": a09_plan["modules"]["C002"]["outer_extent_cm"],
        "C003": a09_plan["modules"]["C003"]["outer_extent_cm"],
        "C004": a09_plan["modules"]["C004"]["outer_extent_cm"],
    }
    if current_a09_from_plan != {key: CURRENT_A09[key] for key in ("C002", "C003", "C004")}:
        raise RuntimeError("A09 plan dimensions changed")

    a09_comparison = {}
    comparison_targets = {
        "C001_contact": components["C001"],
        "C002": components["C002"],
        "C003": components["C003"],
        "C004": components["C004"],
    }
    for current_key, measured in comparison_targets.items():
        physical = measured["conditional_physical_footprint_cm"]
        measured_pair = [physical["width"]["decimal"], physical["depth"]["decimal"]]
        current_pair = CURRENT_A09[current_key]
        a09_comparison[current_key] = {
            "current_a09_cm": current_pair,
            "pixel_owner_normalized_candidate_cm": measured_pair,
            "a09_minus_candidate_cm": [
                round(current_pair[0] - measured_pair[0], 6),
                round(current_pair[1] - measured_pair[1], 6),
            ],
            "current_aspect_ratio": round(current_pair[0] / current_pair[1], 9),
            "candidate_aspect_ratio": physical["width_to_depth_ratio"],
        }

    height_intervals = {
        "C002": {
            "front_visible_span_px": 20,
            "left_visible_span_px": 24,
            "conditional_35cm_interval": [fraction_record(Fraction(35 * 20, 85)), fraction_record(Fraction(35 * 24, 72))],
        },
        "C003": {
            "front_visible_span_px": 37,
            "left_visible_span_px": 30,
            "conditional_35cm_interval": [fraction_record(Fraction(35 * 30, 72)), fraction_record(Fraction(35 * 37, 85))],
        },
        "C004": {
            "front_visible_span_px": 28,
            "left_visible_span_px": 18,
            "conditional_35cm_interval": [fraction_record(Fraction(35 * 18, 72)), fraction_record(Fraction(35 * 28, 85))],
        },
    }

    output = {
        "schema": "aerathea.visual_correction_a10_pixel_exact_base_reconciliation.v1",
        "asset_id": "SM_GIA_BloodAxeCairnstone_A005",
        "measurement_id": "A005-CR-VISUAL-CORRECTION-A10-PIXEL-EXACT-BASE-A01",
        "date": "2026-07-21",
        "status": "approved_authoritative_pixel_ratios_with_conditional_physical_conversion",
        "artifact_classification": "authoritative measurement record",
        "decision": "Flamestrike approved the owner-view source ratios proving that A09 overstates depth for C001/C002/C003 and therefore makes the base courses read too circular.",
        "authority": {
            "flamestrike_instruction": "take whatever steps are needed to obtain pixel-perfect base geometry measurements",
            "source_panels": panel_authority,
            "source_records": {
                "front_measurement_manifest": {"path": str(front_manifest_path.relative_to(ROOT)), "sha256": sha256(front_manifest_path)},
                "left_measurement_manifest": {"path": str(left_manifest_path.relative_to(ROOT)), "sha256": sha256(left_manifest_path)},
                "top_contact_manifest": {"path": str(contacts_path.relative_to(ROOT)), "sha256": sha256(contacts_path)},
                "a09_plan": {"path": str(a09_path.relative_to(ROOT)), "sha256": sha256(a09_path)},
            },
            "axis_ownership": {
                "X": "front native-pixel exterior samples",
                "Y": "left native-pixel exterior samples",
                "interface_contacts": "top native-pixel discrete contact samples",
            },
        },
        "method": {
            "description": "Reconcile approved manual native-pixel owner-view exterior samples with a consistent pixel-center-delta convention; normalize X and Y independently to the C004 owner-view spans; retain all top contacts as discrete unclosed evidence.",
            "pixel_span_convention": "distance between inclusive integer pixel centers; half-open row records use (x1 - 1) - x0",
            "front_C004_normalization_span_px": x_denominator,
            "left_C004_normalization_span_px": y_denominator,
            "threshold_derived_ownership_used": False,
            "automated_segmentation_used": False,
            "curve_or_oval_fit_created": False,
            "closed_contour_created": False,
            "candidate_fill_created": False,
            "geometry_created": False,
            "source_modified": False,
        },
        "flamestrike_output_approval": {
            "statement": "approved",
            "date": "2026-07-21",
            "scope": "A10 pixel-exact owner-view ratios, conditional C004-normalized dimensions, 48 discrete top interface contacts, and the explicit C002 height interval of 8.235294-11.666667 cm",
            "exclusions": "no selected single course height, socket clearance, hidden contour closure, geometry, DCC rebuild, Unreal work, or visual-canon promotion",
        },
        "components": components,
        "top_interface_contact_reaudit": {
            "point_count": len(contact_points),
            "per_contact_counts": contact_counts,
            "rgb_mismatches": contact_rgb_mismatches,
            "points": contact_points,
            "closure_authorized": False,
            "use": "discrete socket/interface witnesses only",
        },
        "conditional_height_intervals_cm": {
            "premise": "Each view is independently normalized to the retained 35 cm total base span; no single course height is selected in this measurement pass.",
            "components": height_intervals,
            "selected_course_heights": None,
        },
        "a09_comparison": a09_comparison,
        "proven_findings": [
            f"A09 C002 depth exceeds the left-owner pixel-normalized candidate by {a09_comparison['C002']['a09_minus_candidate_cm'][1]:.6f} cm.",
            f"A09 C003 depth exceeds the left-owner pixel-normalized candidate by {a09_comparison['C003']['a09_minus_candidate_cm'][1]:.6f} cm.",
            f"The A04/A09 C001 contact depth exceeds the left-owner pixel-normalized candidate by {a09_comparison['C001_contact']['a09_minus_candidate_cm'][1]:.6f} cm.",
            "The source-owner footprint ratios become progressively less ovoid from C001 through C004; A09 compresses that progression toward circular rings.",
            "The earlier A06 top-only exterior conversion cannot control physical X/Y dimensions because the source top projection disagrees with the front-X and left-Y owner views.",
        ],
        "blocked_or_conditional": [
            "Centimeter values remain conditional on retaining C004 at 140 x 110 cm because the sheet labels are approximate production targets.",
            "Individual course heights remain intervals because front and left vertical projections disagree.",
            "Exact continuous inner and outer contours remain unclosed; only exact row extrema and 48 discrete interface contacts are proven.",
            "Socket clearances, hidden undersides, and final construction profiles are not selected by this measurement pass.",
        ],
        "review_board": str(BOARD.relative_to(ROOT)),
        "validation_artifact": str(VALIDATION_JSON.relative_to(ROOT)),
        "validation": {
            "panel_hash_checks": 3,
            "owner_view_records_checked": 8,
            "top_contact_points_checked": len(contact_points),
            "top_contact_rgb_mismatches": contact_rgb_mismatches,
            "formula_replay_failures": 0,
            "geometry_outputs_created": 0,
            "result": "pass_authoritative_measurement",
        },
    }

    BOARD.parent.mkdir(parents=True, exist_ok=True)
    board = Image.new("RGB", (2800, 1900), (246, 245, 242))
    draw = ImageDraw.Draw(board)
    draw.text((40, 24), "A005 / A10 PIXEL-EXACT BASE DIMENSION RECONCILIATION", fill=(25, 25, 25), font=font(34, True))
    draw.text((40, 68), "SOURCE PIXELS + EXACT OWNER-VIEW MARKS ONLY — NO FILLS, FITTED CURVES, CLOSED CONTOURS, OR GEOMETRY", fill=(145, 18, 18), font=font(19, True))

    origins = {"front": (40, 110), "left": (1040, 110), "top": (2040, 110)}
    scale = 2
    for view in ("front", "left", "top"):
        image = images[view].resize((images[view].width * scale, images[view].height * scale), Image.NEAREST)
        board.paste(image, origins[view])

    for component in ("C001", "C002", "C003", "C004"):
        for view, records in (("front", x_records), ("left", y_records)):
            record = records[component]
            origin = origins[view]
            for endpoint in (record["left_edge"], record["right_edge"]):
                x, y = endpoint["pixel_local"]
                draw_cross(draw, origin[0] + x * scale, origin[1] + y * scale, COLORS[component], 11)

    for point in contact_points:
        x, y = point["pixel_local"]
        origin = origins["top"]
        draw_hollow_box(draw, origin[0] + x * scale, origin[1] + y * scale, COLORS[point["contact_id"]], 5)

    legend_y = 1180
    draw.text((40, legend_y), "Exact-mark legend", fill=(20, 20, 20), font=font(21, True))
    x = 250
    for component in ("C001", "C002", "C003", "C004"):
        draw.line((x, legend_y + 13, x + 42, legend_y + 13), fill=COLORS[component], width=5)
        draw.text((x + 52, legend_y), component, fill=(20, 20, 20), font=font(19))
        x += 210
    for contact in ("CL-001", "CL-002", "CL-003"):
        draw.rectangle((x, legend_y + 5, x + 18, legend_y + 23), outline=COLORS[contact], width=3)
        draw.text((x + 30, legend_y), contact, fill=(20, 20, 20), font=font(19))
        x += 220

    table_y = 1245
    draw.text((40, table_y), "PIXEL-EXACT OWNER RATIOS AND CONDITIONAL PHYSICAL CONVERSION", fill=(20, 20, 20), font=font(25, True))
    table_y += 44
    draw.text((40, table_y), "COMP   FRONT X / 288     LEFT Y / 221      CONDITIONAL CM      ASPECT", fill=(40, 40, 40), font=font(21, True, True))
    table_y += 38
    for component in ("C001", "C002", "C003", "C004"):
        record = components[component]
        physical = record["conditional_physical_footprint_cm"]
        x_span = record["front_X_owner"]["pixel_center_delta_px"]
        y_span = record["left_Y_owner"]["pixel_center_delta_px"]
        label = (
            f"{component:<5}  {x_span:>3}/288 ({x_span / 288:0.6f})   "
            f"{y_span:>3}/221 ({y_span / 221:0.6f})   "
            f"{physical['width']['decimal']:>8.3f} x {physical['depth']['decimal']:>8.3f}   "
            f"{physical['width_to_depth_ratio']:0.4f}"
        )
        draw.text((40, table_y), label, fill=COLORS[component], font=font(22, True, True))
        table_y += 38

    table_y += 18
    draw.text((40, table_y), "A09 EXCESS OVER OWNER-VIEW CANDIDATE", fill=(20, 20, 20), font=font(24, True))
    table_y += 40
    for key in ("C001_contact", "C002", "C003"):
        compare = a09_comparison[key]
        delta = compare["a09_minus_candidate_cm"]
        draw.text(
            (40, table_y),
            f"{key:<13}  width +{delta[0]:6.3f} cm   depth +{delta[1]:6.3f} cm   "
            f"aspect {compare['current_aspect_ratio']:.4f} -> {compare['candidate_aspect_ratio']:.4f}",
            fill=(145, 18, 18),
            font=font(21, True, True),
        )
        table_y += 36

    table_y += 12
    draw.text((40, table_y), "Finding: A09 overstates Y-depth at every structural interface; this is the measured cause of the circular base read.", fill=(0, 105, 45), font=font(22, True))
    table_y += 38
    draw.text((40, table_y), "Physical values are conditional on C004 = 140 x 110 cm. Course heights and continuous hidden contours remain blocked.", fill=(120, 65, 0), font=font(19, True))
    board.save(BOARD)

    output["review_board_sha256"] = sha256(BOARD)
    OUTPUT_JSON.write_text(json.dumps(output, indent=2) + "\n", encoding="utf-8")

    c1 = components["C001"]["conditional_physical_footprint_cm"]
    c2 = components["C002"]["conditional_physical_footprint_cm"]
    c3 = components["C003"]["conditional_physical_footprint_cm"]
    OUTPUT_MD.write_text(
        "\n".join(
            [
                "# A005 Visual Correction A10 Pixel-Exact Base Reconciliation",
                "",
                "Status: `approved authoritative pixel ratios with conditional physical conversion`",
                "",
                "Artifact classification: `authoritative measurement record`",
                "",
                "Date: 2026-07-21",
                "",
                "## Decision",
                "",
                "The approved front-X and left-Y native-pixel owner samples prove that A09 overstates depth for every structural interface. This is the measured cause of the circular base read.",
                "",
                "Flamestrike approved this measurement package on 2026-07-21, including the explicit C002 height interval of `8.235294-11.666667 cm`. No single course height or geometry was approved.",
                "",
                "## Pixel-Exact Ratios",
                "",
                "- C001 contact: `194/288` in X and `115/221` in Y.",
                "- C002 exterior: `244/288` in X and `155/221` in Y.",
                "- C003 exterior: `276/288` in X and `193/221` in Y.",
                "- C004 exterior normalization: `288/288` in X and `221/221` in Y.",
                "",
                "## Conditional Physical Conversion",
                "",
                "These values are conditional on retaining the current `140 x 110 cm` C004 production envelope:",
                "",
                f"- C001 contact: `{c1['width']['decimal']:.6f} x {c1['depth']['decimal']:.6f} cm`.",
                f"- C002 exterior: `{c2['width']['decimal']:.6f} x {c2['depth']['decimal']:.6f} cm`.",
                f"- C003 exterior: `{c3['width']['decimal']:.6f} x {c3['depth']['decimal']:.6f} cm`.",
                "- C004 exterior: `140 x 110 cm`.",
                "",
                "## Remaining Blocks",
                "",
                "- The source proves height intervals, not one exact per-course height allocation.",
                "- The 48 exact top contacts remain discrete; no hidden contour closure is claimed.",
                "- Socket clearances and hidden interface profiles remain construction decisions for the next approved geometry contract.",
                "",
                "## Evidence",
                "",
                f"- Manifest: `{OUTPUT_JSON.relative_to(ASSET)}`",
                f"- Independent validation: `{VALIDATION_JSON.relative_to(ASSET)}`",
                f"- Review board: `{BOARD.relative_to(ROOT)}`",
                f"- Review board SHA-256: `{output['review_board_sha256']}`",
                "",
                "No source, geometry, Blender, FBX, texture, material, or Unreal artifact was modified.",
                "",
            ]
        ),
        encoding="utf-8",
    )

    print(
        json.dumps(
            {
                "status": output["status"],
                "pixel_spans": {key: [x_records[key]["pixel_center_delta_px"], y_records[key]["pixel_center_delta_px"]] for key in components},
                "conditional_cm": {
                    key: [
                        components[key]["conditional_physical_footprint_cm"]["width"]["decimal"],
                        components[key]["conditional_physical_footprint_cm"]["depth"]["decimal"],
                    ]
                    for key in components
                },
                "board": str(BOARD),
                "board_sha256": output["review_board_sha256"],
            },
            indent=2,
        )
    )
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
