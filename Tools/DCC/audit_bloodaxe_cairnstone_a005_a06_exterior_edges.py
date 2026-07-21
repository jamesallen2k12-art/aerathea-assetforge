#!/usr/bin/env python3
"""Record the A005/A06 exterior-edge-only base measurement authority.

The audit distinguishes visible component exterior edges from the older
CL-002/CL-003 alignment/contact witnesses.  It creates exact marks only: no
filled contour, fitted curve, smoothing envelope, or geometry.
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
OUTPUT_JSON = ASSET / "manifests/VISUAL_CORRECTION_A06_EXTERIOR_EDGE_AUDIT.json"
OUTPUT_MD = ASSET / "steps/VISUAL_CORRECTION_A06_MEASUREMENT_GATE.md"
BOARD = (
    ROOT
    / "Saved/Automation/DCC/SM_GIA_BloodAxeCairnstone_A005/Production/"
    "VisualCorrection_A06_Measurement/"
    "SM_GIA_BloodAxeCairnstone_A005_A06_EXTERIOR_EDGE_MEASUREMENT_ONLY_REVIEW.png"
)

PANEL_RECORDS = {
    "front": {
        "path": PANELS / "SM_GIA_BloodAxeCairnstone_A005_STEP_03_FRONT.png",
        "sha256": "262071198bc0d409e9b68af5ac4f3c6a4768a90b1fd199342035a8a82342c2c5",
    },
    "left": {
        "path": PANELS / "SM_GIA_BloodAxeCairnstone_A005_STEP_03_LEFT.png",
        "sha256": "52212ba783d026a008929e3946cac934281de7d2daec2ada316205059258cba4",
    },
    "top": {
        "path": PANELS / "SM_GIA_BloodAxeCairnstone_A005_STEP_03_TOP.png",
        "sha256": "1bc9750b903a3d9e5689bee3c2c1c7094ccd554c361ff622aa9065d2c5287fdf",
    },
}

# Exact visible outside limits selected from the source-owned top panel.
# These are not CL-002/CL-003 alignment/contact samples.  Horizontal and
# vertical extrema are kept as separate observations; no contour is closed.
TOP_EXTENTS = {
    "C002": {
        "x": {"negative": [48, 160], "positive": [232, 160]},
        "y": {"positive": [140, 52], "negative": [140, 245]},
        "classification": "visible component exterior edge over lower course",
    },
    "C003": {
        "x": {"negative": [35, 160], "positive": [239, 160]},
        "y": {"positive": [140, 38], "negative": [140, 257]},
        "classification": "visible component exterior edge over peripheral apron",
    },
    "C004": {
        "x": {"negative": [31, 160], "positive": [239, 160]},
        "y": {"positive": [140, 31], "negative": [140, 260]},
        "classification": "visible outer silhouette against source paper",
    },
}

# Multiple owner-view exterior silhouettes are retained as cross-checks.  The
#ir projected row widths change with Z and therefore do not replace the
# top-owned maximum plan extents.
OWNER_VIEW_CROSSCHECKS = {
    "front": {
        "C002": [
            {"row": 345, "left": 135, "right_exclusive": 366},
            {"row": 355, "left": 134, "right_exclusive": 366},
            {"row": 360, "left": 127, "right_exclusive": 372},
        ],
        "C003": [
            {"row": 375, "left": 120, "right_exclusive": 381},
            {"row": 385, "left": 115, "right_exclusive": 388},
            {"row": 390, "left": 111, "right_exclusive": 388},
        ],
    },
    "left": {
        "C002": [
            {"row": 240, "left": 154, "right_exclusive": 306},
            {"row": 250, "left": 153, "right_exclusive": 308},
            {"row": 255, "left": 152, "right_exclusive": 308},
        ],
        "C003": [
            {"row": 265, "left": 133, "right_exclusive": 327},
            {"row": 275, "left": 133, "right_exclusive": 327},
            {"row": 280, "left": 133, "right_exclusive": 327},
        ],
    },
}


def sha256(path: Path) -> str:
    digest = hashlib.sha256()
    with path.open("rb") as handle:
        for block in iter(lambda: handle.read(1024 * 1024), b""):
            digest.update(block)
    return digest.hexdigest()


def fraction_record(value: Fraction) -> dict:
    return {
        "exact": f"{value.numerator}/{value.denominator}",
        "decimal": round(float(value), 6),
    }


def font(size: int, bold: bool = False):
    name = "DejaVuSans-Bold.ttf" if bold else "DejaVuSans.ttf"
    path = Path("/usr/share/fonts/truetype/dejavu") / name
    try:
        return ImageFont.truetype(str(path), size=size)
    except OSError:
        return ImageFont.load_default()


def draw_cross(draw: ImageDraw.ImageDraw, x: int, y: int, color, radius: int = 5):
    draw.line((x - radius, y, x + radius, y), fill=color, width=1)
    draw.line((x, y - radius, x, y + radius), fill=color, width=1)


def endpoint_record(image: Image.Image, coordinate: list[int]) -> dict:
    return {"pixel_local": coordinate, "source_rgb": list(image.getpixel(tuple(coordinate)))}


def main() -> int:
    images = {}
    panel_authority = {}
    for name, record in PANEL_RECORDS.items():
        actual = sha256(record["path"])
        if actual != record["sha256"]:
            raise RuntimeError(f"{name} panel hash mismatch")
        images[name] = Image.open(record["path"]).convert("RGB")
        panel_authority[name] = {
            "path": str(record["path"].relative_to(ROOT)),
            "expected_sha256": record["sha256"],
            "actual_sha256": actual,
            "hash_match": True,
            "size_px": list(images[name].size),
        }

    top_records = {}
    top_image = images["top"]
    for component, axes in TOP_EXTENTS.items():
        x_negative = axes["x"]["negative"]
        x_positive = axes["x"]["positive"]
        y_positive = axes["y"]["positive"]
        y_negative = axes["y"]["negative"]
        top_records[component] = {
            "classification": axes["classification"],
            "x": {
                "negative": endpoint_record(top_image, x_negative),
                "positive": endpoint_record(top_image, x_positive),
                "span_px": x_positive[0] - x_negative[0],
            },
            "y": {
                "positive": endpoint_record(top_image, y_positive),
                "negative": endpoint_record(top_image, y_negative),
                "span_px": y_negative[1] - y_positive[1],
            },
            "closed_contour_created": False,
            "filled_region_created": False,
            "curve_fit_created": False,
        }

    c004_x = top_records["C004"]["x"]["span_px"]
    c004_y = top_records["C004"]["y"]["span_px"]
    dimensions = {}
    for component in ("C002", "C003"):
        width = Fraction(top_records[component]["x"]["span_px"] * 140, c004_x)
        depth = Fraction(top_records[component]["y"]["span_px"] * 110, c004_y)
        dimensions[component] = {
            "maximum_footprint_cm": [fraction_record(width), fraction_record(depth)],
            "formula": {
                "width": f"140 * {top_records[component]['x']['span_px']} / {c004_x}",
                "depth": f"110 * {top_records[component]['y']['span_px']} / {c004_y}",
            },
            "basis": "same-top-panel ratio of verified component exterior span to verified C004 outer silhouette span",
        }

    crosschecks = {}
    for view, components in OWNER_VIEW_CROSSCHECKS.items():
        image = images[view]
        crosschecks[view] = {}
        for component, rows in components.items():
            crosschecks[view][component] = []
            for row in rows:
                left = row["left"]
                right = row["right_exclusive"] - 1
                crosschecks[view][component].append(
                    {
                        **row,
                        "span_px": row["right_exclusive"] - left,
                        "left_rgb": list(image.getpixel((left, row["row"]))),
                        "right_rgb": list(image.getpixel((right, row["row"]))),
                        "classification": "visible exterior silhouette row; cross-check only",
                    }
                )

    output = {
        "schema": "aerathea.visual_correction_a06_exterior_edge_audit.v1",
        "asset_id": "SM_GIA_BloodAxeCairnstone_A005",
        "audit_id": "A005-CR-VISUAL-CORRECTION-A06-EXTERIOR-EDGE-A01",
        "date": "2026-07-21",
        "status": "pass_authoritative_exterior_edge_measurement",
        "artifact_classification": "authoritative measurement record",
        "decision": "authoritative exterior-edge measurement record ready for A06 contract",
        "authority": {
            "handoff": "steps/VISUAL_CORRECTION_A05_VISUAL_REJECTION_A06_RESTART_HANDOFF.md",
            "flamestrike_authority": "full approval and authority to continue correcting the base geometry and present the completed image",
            "source_panels": panel_authority,
            "approved_overall_footprint_cm": [140, 110],
        },
        "controls": {
            "alignment_contact_spans_used_as_outer_dimensions": False,
            "geometry_created": False,
            "candidate_fill_created": False,
            "inferred_overlay_created": False,
            "closed_contour_created": False,
            "curve_or_oval_fit_created": False,
            "source_modified": False,
            "color_grading_performed": False,
        },
        "top_exterior_edge_records": top_records,
        "owner_view_crosschecks": crosschecks,
        "derived_physical_footprints": dimensions,
        "superseded_a05_footprints_cm": {
            "C002": [119.097222, 77.647059],
            "C003": [134.652778, 96.561086],
        },
        "review_board": str(BOARD.relative_to(ROOT)),
    }

    BOARD.parent.mkdir(parents=True, exist_ok=True)
    board = Image.new("RGB", (1900, 1120), (246, 245, 242))
    draw = ImageDraw.Draw(board)
    draw.text((40, 24), "A005 / A06 EXTERIOR-EDGE MEASUREMENT-ONLY AUDIT", fill=(25, 25, 25), font=font(30, True))
    draw.text((40, 64), "EXACT SOURCE PIXELS + EXACT MARKS ONLY — NO FILLS, FITTED CURVES, SMOOTHED ENVELOPES, OR GEOMETRY", fill=(145, 18, 18), font=font(18, True))

    colors = {"C002": (255, 145, 0), "C003": (0, 175, 215), "C004": (0, 135, 235)}
    top_scaled = top_image.resize((top_image.width * 2, top_image.height * 2), Image.NEAREST)
    board.paste(top_scaled, (40, 105))
    for component, record in top_records.items():
        color = colors[component]
        for axis in ("x", "y"):
            for role in ("negative", "positive"):
                point = record[axis][role]["pixel_local"]
                draw_cross(draw, 40 + point[0] * 2, 105 + point[1] * 2, color, 8)

    front_scaled = images["front"].resize((483, 525), Image.NEAREST)
    left_scaled = images["left"].resize((484, 401), Image.NEAREST)
    board.paste(front_scaled, (760, 105))
    board.paste(left_scaled, (1280, 105))
    for view, origin in (("front", (760, 105)), ("left", (1280, 105))):
        for component, rows in crosschecks[view].items():
            for row in rows:
                draw_cross(draw, origin[0] + row["left"], origin[1] + row["row"], colors[component], 4)
                draw_cross(draw, origin[0] + row["right_exclusive"] - 1, origin[1] + row["row"], colors[component], 4)

    y = 880
    draw.text((40, y), "Exact-mark legend:", fill=(20, 20, 20), font=font(17, True))
    for index, component in enumerate(("C002", "C003", "C004")):
        x = 220 + index * 260
        draw.line((x, y + 10, x + 32, y + 10), fill=colors[component], width=4)
        draw.text((x + 42, y), f"{component} exterior", fill=(20, 20, 20), font=font(17))
    y += 52
    for component in ("C002", "C003"):
        target = dimensions[component]["maximum_footprint_cm"]
        draw.text(
            (40, y),
            f"{component} exterior footprint: {target[0]['decimal']:.2f} x {target[1]['decimal']:.2f} cm",
            fill=(20, 20, 20),
            font=font(21, True),
        )
        y += 34
    draw.text((40, y + 8), "A05 internal alignment/contact footprint values are superseded and are not reused.", fill=(145, 18, 18), font=font(18))
    draw.text((40, y + 42), "Decision: authoritative exterior-edge measurement record ready for A06 contract.", fill=(0, 105, 45), font=font(20, True))
    board.save(BOARD)

    output["review_board_sha256"] = sha256(BOARD)
    OUTPUT_JSON.write_text(json.dumps(output, indent=2) + "\n", encoding="utf-8")

    c002 = dimensions["C002"]["maximum_footprint_cm"]
    c003 = dimensions["C003"]["maximum_footprint_cm"]
    OUTPUT_MD.write_text(
        "\n".join(
            [
                "# A005 Visual Correction A06 Exterior-Edge Measurement Gate",
                "",
                "Status: `authoritative exterior-edge measurement record ready for A06 contract`",
                "",
                "Artifact classification: `authoritative measurement record`",
                "",
                "Date: 2026-07-21",
                "",
                "## Decision",
                "",
                "The top-owned outside limits of C002 and C003 are separately identified from the older internal CL-002/CL-003 alignment/contact witnesses. The exterior spans are sufficient for a bounded A06 correction contract.",
                "",
                "## Controlling Exterior Dimensions",
                "",
                f"- C002: `{c002[0]['decimal']:.6f} x {c002[1]['decimal']:.6f} cm` from exact ratios `{dimensions['C002']['formula']['width']}` and `{dimensions['C002']['formula']['depth']}`.",
                f"- C003: `{c003[0]['decimal']:.6f} x {c003[1]['decimal']:.6f} cm` from exact ratios `{dimensions['C003']['formula']['width']}` and `{dimensions['C003']['formula']['depth']}`.",
                "- C004 remains the approved `140 x 110 cm` outside footprint.",
                "- A05 values `119.097222 x 77.647059 cm` and `134.652778 x 96.561086 cm` remain invalid and superseded.",
                "",
                "## Controls",
                "",
                "No candidate fill, contour closure, fitted curve, smoothed envelope, geometry, UV change, source edit, or color grade was created. Front/left exterior silhouette rows are cross-checks only; they do not replace the top-owned maximum plan extents.",
                "",
                "## Evidence",
                "",
                f"- Audit: `{OUTPUT_JSON.relative_to(ASSET)}`",
                f"- Review board: `{BOARD.relative_to(ROOT)}`",
                f"- Board SHA-256: `{output['review_board_sha256']}`",
                "",
                "## Next Gate",
                "",
                "A06 may replace only the quarantined A05 C002/C003 footprint dimensions, preserve the exact A04 plinth, retain the improved A05 oval masonry treatment as reference only, and end at one audited DCC review image. Unreal and Step 17 remain unauthorized.",
                "",
            ]
        ),
        encoding="utf-8",
    )
    print(json.dumps({"decision": output["decision"], "dimensions": dimensions, "board": str(BOARD)}, indent=2))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
