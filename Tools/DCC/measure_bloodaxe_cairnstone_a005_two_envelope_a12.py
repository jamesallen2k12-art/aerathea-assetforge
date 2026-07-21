#!/usr/bin/env python3
"""Build the A005 A12 two-envelope, multi-row measurement board."""

from __future__ import annotations

import hashlib
import json
from fractions import Fraction
from pathlib import Path

from PIL import Image, ImageDraw, ImageFont


ROOT = Path(__file__).resolve().parents[2]
ASSET = ROOT / "docs/assets/blueprints/SM_GIA_BloodAxeCairnstone_A005"
MANIFESTS = ASSET / "manifests"
PANELS = ASSET / "panels/STEP_03"
FRONT_PANEL = PANELS / "SM_GIA_BloodAxeCairnstone_A005_STEP_03_FRONT.png"
LEFT_PANEL = PANELS / "SM_GIA_BloodAxeCairnstone_A005_STEP_03_LEFT.png"
FRONT_MANIFEST = MANIFESTS / "STEP_06_FRONT_MEASUREMENT_MANIFEST.json"
LEFT_MANIFEST = MANIFESTS / "STEP_07_LEFT_MEASUREMENT_MANIFEST.json"
A10_MANIFEST = MANIFESTS / "VISUAL_CORRECTION_A10_PIXEL_EXACT_BASE_RECONCILIATION.json"
OUTPUT_JSON = MANIFESTS / "VISUAL_CORRECTION_A12_TWO_ENVELOPE_MEASUREMENT.json"
VALIDATION_JSON = MANIFESTS / "VISUAL_CORRECTION_A12_TWO_ENVELOPE_MEASUREMENT_VALIDATION.json"
OUTPUT_MD = ASSET / "steps/VISUAL_CORRECTION_A12_TWO_ENVELOPE_MEASUREMENT_OUTPUT.md"
BOARD = ROOT / "Saved/Automation/DCC/SM_GIA_BloodAxeCairnstone_A005/Production/VisualCorrection_A12_Measurement/SM_GIA_BloodAxeCairnstone_A005_A12_TWO_ENVELOPE_RECONCILIATION.png"

EXPECTED_HASHES = {
    FRONT_PANEL: "262071198bc0d409e9b68af5ac4f3c6a4768a90b1fd199342035a8a82342c2c5",
    LEFT_PANEL: "52212ba783d026a008929e3946cac934281de7d2daec2ada316205059258cba4",
    FRONT_MANIFEST: "c71932bef2016808d24fdc9aed47b9f4a3c32f59bdd45a551aab6804d877ecef",
    LEFT_MANIFEST: "e08d868925967a05d465cecadc4810a3f3e2b3cdb5be342e32ebdd807e0e9725",
    A10_MANIFEST: "09452319172cdca60f024e106e20eef52a5567eac04e0f2fda73985370b3e156",
}

COLORS = {"C002": (245, 133, 20), "C003": (0, 145, 205), "C004": (128, 60, 205)}


def sha256(path: Path) -> str:
    digest = hashlib.sha256()
    with path.open("rb") as handle:
        for block in iter(lambda: handle.read(1024 * 1024), b""):
            digest.update(block)
    return digest.hexdigest()


def font(size: int, bold: bool = False, mono: bool = False):
    family = "DejaVuSansMono" if mono else "DejaVuSans"
    suffix = "-Bold" if bold else ""
    try:
        return ImageFont.truetype(f"/usr/share/fonts/truetype/dejavu/{family}{suffix}.ttf", size)
    except OSError:
        return ImageFont.load_default()


def exact(value: Fraction) -> dict:
    return {"exact": f"{value.numerator}/{value.denominator}", "decimal": round(float(value), 9)}


def median(values: list[int]) -> Fraction:
    ordered = sorted(values)
    middle = len(ordered) // 2
    if len(ordered) % 2:
        return Fraction(ordered[middle], 1)
    return Fraction(ordered[middle - 1] + ordered[middle], 2)


def rows_for(manifest: dict, component: str) -> list[dict]:
    return [record for record in manifest["visible_outer_edge_row_samples"] if record["component_id"] == f"C-{component[-3:]}"]


def statistic(view: str, component: str, rows: list[dict], denominator: int, envelope_cm: int, base_height_cm: int, image: Image.Image) -> dict:
    records = []
    deltas = []
    for row in rows:
        x0, x1 = row["span_half_open"]
        delta = (x1 - 1) - x0
        deltas.append(delta)
        records.append(
            {
                "source_record_id": row["id"],
                "row_y_px": row["y"],
                "half_open_span_px": [x0, x1],
                "pixel_center_delta_px": delta,
                "left_endpoint_rgb": list(image.getpixel((x0, row["y"]))),
                "right_endpoint_rgb": list(image.getpixel((x1 - 1, row["y"]))),
            }
        )
    median_delta = median(deltas)
    physical = Fraction(envelope_cm, 1) * median_delta / denominator
    ratio = physical / base_height_cm
    maximum_delta = max(deltas)
    maximum_physical = Fraction(envelope_cm * maximum_delta, denominator)
    return {
        "view": view,
        "component": component,
        "approved_row_records": records,
        "pixel_center_deltas_px": deltas,
        "minimum_delta_px": min(deltas),
        "maximum_delta_px": maximum_delta,
        "median_delta_px": exact(median_delta),
        "conditional_median_extent_cm": exact(physical),
        "conditional_extent_to_35cm_base_height": exact(ratio),
        "A10_widest_row_extent_cm": exact(maximum_physical),
        "median_reduction_from_A10_cm": exact(maximum_physical - physical),
        "formula": f"{envelope_cm} * median({deltas}) / {denominator}",
        "premise": f"conditional on C004 {envelope_cm} cm owner-axis extent and 35 cm total base height",
    }


def draw_row_marks(draw: ImageDraw.ImageDraw, origin: tuple[int, int], scale: int, records: list[dict], color: tuple[int, int, int]) -> None:
    for record in records:
        x0, x1 = record["half_open_span_px"]
        y = record["row_y_px"]
        p0 = (origin[0] + x0 * scale, origin[1] + y * scale)
        p1 = (origin[0] + (x1 - 1) * scale, origin[1] + y * scale)
        draw.line((*p0, *p1), fill=color, width=3)
        for x, yy in (p0, p1):
            draw.line((x - 7, yy, x + 7, yy), fill=color, width=2)
            draw.line((x, yy - 7, x, yy + 7), fill=color, width=2)


def main() -> int:
    for path, expected in EXPECTED_HASHES.items():
        actual = sha256(path)
        if actual != expected:
            raise RuntimeError(f"authority hash mismatch for {path}: {actual}")

    front_image = Image.open(FRONT_PANEL).convert("RGB")
    left_image = Image.open(LEFT_PANEL).convert("RGB")
    front = json.loads(FRONT_MANIFEST.read_text(encoding="utf-8"))
    left = json.loads(LEFT_MANIFEST.read_text(encoding="utf-8"))
    a10 = json.loads(A10_MANIFEST.read_text(encoding="utf-8"))
    front_labels = front["world_measurement_status"]["direct_source_labels_cm"]
    left_labels = left["world_measurement_status"]["direct_source_labels_cm"]
    expected_labels = {
        "C001_max_width_cm": 120,
        "C001_max_depth_cm": 90,
        "C004_footprint_width_cm": 140,
        "C004_footprint_depth_cm": 110,
        "base_height_cm": 35,
    }
    actual_labels = {
        "C001_max_width_cm": front_labels["C-001_max_width"],
        "C001_max_depth_cm": left_labels["C-001_max_depth"],
        "C004_footprint_width_cm": front_labels["C-004_footprint_width"],
        "C004_footprint_depth_cm": left_labels["C-004_footprint_depth"],
        "base_height_cm": front_labels["base_height"],
    }
    if actual_labels != expected_labels or left_labels["base_height"] != 35:
        raise RuntimeError(f"unexpected direct labels: {actual_labels}")

    statistics = {
        "C002": {
            "front_X": statistic("front", "C002", rows_for(front, "C002"), 288, 140, 35, front_image),
            "left_Y": statistic("left", "C002", rows_for(left, "C002"), 221, 110, 35, left_image),
        },
        "C003": {
            "front_X": statistic("front", "C003", rows_for(front, "C003"), 288, 140, 35, front_image),
            "left_Y": statistic("left", "C003", rows_for(left, "C003"), 221, 110, 35, left_image),
        },
    }

    c004_front = a10["components"]["C004"]["front_X_owner"]
    c004_left = a10["components"]["C004"]["left_Y_owner"]
    output = {
        "schema": "aerathea.visual_correction_a12_two_envelope_measurement.v1",
        "asset_id": "SM_GIA_BloodAxeCairnstone_A005",
        "contract_id": "A005-CR-VISUAL-CORRECTION-A12-MEASUREMENT",
        "date": "2026-07-21",
        "status": "candidate_measurement_pending_flamestrike_review",
        "artifact_classification": "candidate",
        "authority": {
            "flamestrike_approval": "approved",
            "scope": "measurement-only two-envelope reconciliation; no geometry rebuild",
            "inputs": {str(path.relative_to(ROOT)): sha256(path) for path in EXPECTED_HASHES},
        },
        "direct_label_ownership": actual_labels,
        "tested_structural_plinth_hypothesis": {
            "hypothesis": "map the direct 120 x 90 cm labels to C003 as a structural-plinth envelope",
            "result": "rejected_as_source_authority_conflict",
            "reason": "the approved front and left measurement records explicitly assign 120 cm width and 90 cm depth to C001 maximum dimensions; no direct source label assigns 120 x 90 cm to C003",
            "C003_120x90_authorized": False,
        },
        "envelopes": {
            "C004_outer_rubble": {"extent_cm": [140, 110], "height_reference_cm": 35, "width_to_height": exact(Fraction(4, 1)), "depth_to_height": exact(Fraction(22, 7)), "status": "direct_source_label_authority"},
            "C001_maximum": {"extent_cm": [120, 90], "height_reference_cm": 220, "status": "direct_source_label_authority; not a C003 plinth label"},
        },
        "multi_row_statistics": statistics,
        "C004_normalization_evidence": {
            "front": c004_front,
            "left": c004_left,
            "interior_owned": False,
            "use": "axis normalization only",
        },
        "method": {
            "statistic": "median of every approved manual row sample for the component and owner view",
            "pixel_span_convention": "distance between inclusive endpoint pixel centers",
            "comparison": "A10 widest approved row versus A12 multi-row median",
            "candidate_fill_created": False,
            "closed_contour_created": False,
            "curve_fit_created": False,
            "geometry_created": False,
            "blender_outputs_created": 0,
            "fbx_outputs_created": 0,
            "unreal_outputs_created": 0,
            "source_modified": False,
        },
        "finding": "The 120 x 90 mapping cannot authorize C003. The multi-row median is the evidence-backed statistic that tests whether isolated protruding stones inflated the A10 widest-row construction extents.",
        "blocked": [
            "The median statistic is not construction authority until Flamestrike approves this A12 result.",
            "C004 interior ownership and continuous contours remain unproven.",
            "No new hidden interface, socket, or course-height construction is authorized.",
        ],
        "decision_requested": "approve, reject, or mark blocked the A12 multi-row median statistic as the dimensional basis for a separate geometry contract",
        "review_board": str(BOARD.relative_to(ROOT)),
        "validation_artifact": str(VALIDATION_JSON.relative_to(ROOT)),
    }

    BOARD.parent.mkdir(parents=True, exist_ok=True)
    board = Image.new("RGB", (3000, 1900), (246, 245, 242))
    draw = ImageDraw.Draw(board)
    draw.text((40, 24), "A005 / A12 TWO-ENVELOPE + MULTI-ROW DIMENSION RECONCILIATION", fill=(25, 25, 25), font=font(34, True))
    draw.text((40, 68), "SOURCE PIXELS + EXACT ROW MARKS + DECLARED FORMULAS ONLY — NO FILLS, CONTOUR FITS, OR GEOMETRY", fill=(145, 18, 18), font=font(19, True))
    origins = {"front": (40, 110), "left": (1050, 110)}
    scale = 2
    board.paste(front_image.resize((front_image.width * scale, front_image.height * scale), Image.NEAREST), origins["front"])
    board.paste(left_image.resize((left_image.width * scale, left_image.height * scale), Image.NEAREST), origins["left"])
    for component in ("C002", "C003"):
        draw_row_marks(draw, origins["front"], scale, statistics[component]["front_X"]["approved_row_records"], COLORS[component])
        draw_row_marks(draw, origins["left"], scale, statistics[component]["left_Y"]["approved_row_records"], COLORS[component])
    for view, record in (("front", c004_front), ("left", c004_left)):
        origin = origins[view]
        y = record["row_y_px"]
        endpoints = (record["left_edge"]["pixel_local"], record["right_edge"]["pixel_local"])
        p0 = (origin[0] + endpoints[0][0] * scale, origin[1] + y * scale)
        p1 = (origin[0] + endpoints[1][0] * scale, origin[1] + y * scale)
        draw.line((*p0, *p1), fill=COLORS["C004"], width=3)

    x = 2050
    draw.text((x, 120), "DIRECT LABEL OWNERSHIP", fill=(20, 20, 20), font=font(25, True))
    direct_lines = [
        "C004 rubble footprint: 140 x 110 cm",
        "Total base height: 35 cm",
        "C001 maximum: 120 x 90 cm",
        "",
        "TEST: assign 120 x 90 to C003",
        "RESULT: REJECTED AS AUTHORITY",
        "The label records explicitly own C001,",
        "not the structural masonry course.",
    ]
    yy = 170
    for index, line in enumerate(direct_lines):
        color = (145, 18, 18) if index >= 4 else (35, 35, 35)
        draw.text((x, yy), line, fill=color, font=font(19, index in (0, 1, 2, 5)))
        yy += 36

    draw.text((40, 1190), "MULTI-ROW STATISTIC (PIXEL-CENTER DELTAS; CONDITIONAL ON C004 140 x 110)", fill=(20, 20, 20), font=font(25, True))
    draw.text((40, 1240), "COMP AXIS   APPROVED ROW DELTAS       A10 MAX CM   MEDIAN CM   REDUCTION   MEDIAN / 35", fill=(40, 40, 40), font=font(20, True, True))
    yy = 1280
    for component in ("C002", "C003"):
        for axis in ("front_X", "left_Y"):
            record = statistics[component][axis]
            label = (
                f"{component:<4} {axis:<7} {str(record['pixel_center_deltas_px']):<25} "
                f"{record['A10_widest_row_extent_cm']['decimal']:>10.3f}   "
                f"{record['conditional_median_extent_cm']['decimal']:>9.3f}   "
                f"{record['median_reduction_from_A10_cm']['decimal']:>9.3f}   "
                f"{record['conditional_extent_to_35cm_base_height']['decimal']:>9.4f}"
            )
            draw.text((40, yy), label, fill=COLORS[component], font=font(21, True, True))
            yy += 42

    yy += 24
    draw.text((40, yy), "EVIDENCE FINDING", fill=(20, 20, 20), font=font(24, True))
    yy += 42
    draw.text((40, yy), "The C003 120 x 90 hypothesis conflicts with label ownership. Multi-row medians reduce front-width inflation from isolated protruding stones.", fill=(0, 100, 45), font=font(20, True))
    yy += 38
    draw.text((40, yy), "Median values remain candidate measurement until Flamestrike approves them; C004 interior, closed contours, geometry, and hidden interfaces remain blocked.", fill=(120, 65, 0), font=font(19, True))
    board.save(BOARD)

    output["review_board_sha256"] = sha256(BOARD)
    OUTPUT_JSON.write_text(json.dumps(output, indent=2) + "\n", encoding="utf-8")
    c2x = statistics["C002"]["front_X"]["conditional_median_extent_cm"]["decimal"]
    c2y = statistics["C002"]["left_Y"]["conditional_median_extent_cm"]["decimal"]
    c3x = statistics["C003"]["front_X"]["conditional_median_extent_cm"]["decimal"]
    c3y = statistics["C003"]["left_Y"]["conditional_median_extent_cm"]["decimal"]
    OUTPUT_MD.write_text(
        "\n".join(
            [
                "# A005 Visual Correction A12 Two-Envelope Measurement Output",
                "",
                "Status: `candidate measurement pending Flamestrike review`",
                "",
                "Artifact classification: `candidate`",
                "",
                "Contract ID: `A005-CR-VISUAL-CORRECTION-A12-MEASUREMENT`",
                "",
                "## Result",
                "",
                "The direct `120 x 90 cm` labels cannot authorize C003: the approved source records explicitly assign them to C001 maximum width/depth. The tested structural-plinth mapping is rejected as an authority conflict.",
                "",
                "The evidence-backed alternative is the median of every approved C002/C003 row sample rather than A10's single widest row. Conditional on C004 remaining `140 x 110 cm`, the candidate median extents are:",
                "",
                f"- C002: `{c2x:.6f} x {c2y:.6f} cm`.",
                f"- C003: `{c3x:.6f} x {c3y:.6f} cm`.",
                "- C004: direct label authority remains `140 x 110 cm`.",
                "",
                "These median values are not geometry authority until Flamestrike approves this A12 measurement result.",
                "",
                "## Evidence",
                "",
                f"- Manifest: `{OUTPUT_JSON.relative_to(ASSET)}`",
                f"- Validation: `{VALIDATION_JSON.relative_to(ASSET)}`",
                f"- Review board: `{BOARD.relative_to(ROOT)}`",
                f"- Board SHA-256: `{output['review_board_sha256']}`",
                "",
                "No source, Blender, FBX, texture, material, collision, LOD, Unreal, or canon artifact was modified.",
                "",
                "## Decision Gate",
                "",
                "Flamestrike may approve the multi-row median statistic for a separate geometry contract, reject it, or mark the measurement blocked. No rebuild is authorized by this output.",
                "",
            ]
        ),
        encoding="utf-8",
    )
    print(json.dumps({"status": output["status"], "board": str(BOARD), "board_sha256": output["review_board_sha256"], "candidate_median_cm": {"C002": [c2x, c2y], "C003": [c3x, c3y]}}, indent=2))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
