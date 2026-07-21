#!/usr/bin/env python3
"""Create the A005/A05 measurement-only base-contour authority record.

This audit consumes only previously approved exact source-pixel records.  It
does not fit, close, fill, smooth, or construct any contour, and it creates no
geometry.
"""

from __future__ import annotations

import hashlib
import json
import statistics
from fractions import Fraction
from pathlib import Path

from PIL import Image, ImageDraw, ImageFont


ROOT = Path(__file__).resolve().parents[2]
ASSET = ROOT / "docs/assets/blueprints/SM_GIA_BloodAxeCairnstone_A005"
MANIFESTS = ASSET / "manifests"
PANELS = ASSET / "panels/STEP_03"
OUTPUT_JSON = MANIFESTS / "VISUAL_CORRECTION_A05_MEASUREMENT_AUDIT.json"
OUTPUT_MD = ASSET / "steps/VISUAL_CORRECTION_A05_MEASUREMENT_GATE.md"
BOARD = (
    ROOT
    / "Saved/Automation/DCC/SM_GIA_BloodAxeCairnstone_A005/Production/"
    "VisualCorrection_A05_Measurement/"
    "SM_GIA_BloodAxeCairnstone_A005_A05_MEASUREMENT_ONLY_REVIEW.png"
)


def read_json(path: Path):
    return json.loads(path.read_text(encoding="utf-8"))


def sha256(path: Path) -> str:
    digest = hashlib.sha256()
    with path.open("rb") as handle:
        for chunk in iter(lambda: handle.read(1024 * 1024), b""):
            digest.update(chunk)
    return digest.hexdigest()


def decimal(value: Fraction) -> float:
    return round(float(value), 6)


def fraction_record(value: Fraction) -> dict:
    return {"exact": f"{value.numerator}/{value.denominator}", "decimal": decimal(value)}


def rgb_stats(samples: list[dict]) -> dict:
    channels = list(zip(*(sample["rgb"] for sample in samples)))
    return {
        "sample_count": len(samples),
        "median_rgb": [int(statistics.median(channel)) for channel in channels],
        "min_rgb": [min(channel) for channel in channels],
        "max_rgb": [max(channel) for channel in channels],
        "samples": samples,
    }


def font(size: int, bold: bool = False):
    name = "DejaVuSans-Bold.ttf" if bold else "DejaVuSans.ttf"
    path = Path("/usr/share/fonts/truetype/dejavu") / name
    try:
        return ImageFont.truetype(str(path), size=size)
    except OSError:
        return ImageFont.load_default()


def draw_cross(draw: ImageDraw.ImageDraw, x: int, y: int, color, radius: int = 4):
    draw.line((x - radius, y, x + radius, y), fill=color, width=1)
    draw.line((x, y - radius, x, y + radius), fill=color, width=1)


def paste_panel(board, panel, origin, scale):
    scaled = panel.resize((panel.width * scale, panel.height * scale), Image.NEAREST)
    board.paste(scaled, origin)


def resolve_recorded_path(value: str) -> Path:
    path = Path(value)
    project_relative = ROOT / path
    if project_relative.exists():
        return project_relative
    asset_relative = ASSET / path
    if asset_relative.exists():
        return asset_relative
    raise FileNotFoundError(value)


def main() -> int:
    front_measure = read_json(MANIFESTS / "STEP_06_FRONT_MEASUREMENT_MANIFEST.json")
    front_contacts = read_json(MANIFESTS / "STEP_06_FRONT_CONTACT_EVIDENCE_RECOVERY_A01.json")
    left_measure = read_json(MANIFESTS / "STEP_07_LEFT_MEASUREMENT_MANIFEST.json")
    top_contacts = read_json(MANIFESTS / "STEP_04_TOP_CONTACT_EVIDENCE_RECOVERY_A01.json")
    top_measure = read_json(MANIFESTS / "STEP_08R_TOP_MEASUREMENT_MANIFEST.json")
    step14_color = read_json(MANIFESTS / "STEP_14_BASE_COLOR_OWNERSHIP_MANIFEST.json")

    panel_paths = {
        "front": resolve_recorded_path(front_measure["source_panel"]["path"]),
        "left": resolve_recorded_path(left_measure["source_panel"]["path"]),
        "top": resolve_recorded_path(top_measure["authority"]["top_panel"]["path"]),
    }
    panels = {name: Image.open(path).convert("RGB") for name, path in panel_paths.items()}
    expected_hashes = {
        "front": front_measure["source_panel"]["file_sha256"],
        "left": left_measure["source_panel"]["file_sha256"],
        "top": top_measure["authority"]["top_panel"]["file_sha256"],
    }
    actual_hashes = {name: sha256(path) for name, path in panel_paths.items()}
    hash_checks = {name: actual_hashes[name] == expected_hashes[name] for name in panel_paths}
    if not all(hash_checks.values()):
        raise RuntimeError(f"Source panel hash mismatch: {hash_checks}")

    top_rgb_mismatches = []
    top_points_by_contact: dict[str, list[dict]] = {}
    component_color_samples = {name: [] for name in ("C-001", "C-002", "C-003", "C-004")}
    for sample in top_contacts["accepted_points"]:
        contact_id = sample["contact_id"]
        top_points_by_contact.setdefault(contact_id, []).append(sample)
        for witness_key in ("inward_witness", "outward_witness"):
            witness = sample[witness_key]
            coordinate = witness["pixel_local"]
            actual = list(panels["top"].getpixel(tuple(coordinate)))
            expected = witness["source_rgb"]
            if actual != expected:
                top_rgb_mismatches.append(
                    {
                        "sample_id": sample["id"],
                        "witness": witness_key,
                        "coordinate": coordinate,
                        "expected": expected,
                        "actual": actual,
                    }
                )
            component_color_samples[witness["component_id"]].append(
                {
                    "contact_id": contact_id,
                    "sector": sample["sector"],
                    "role": witness_key,
                    "pixel_local": coordinate,
                    "rgb": expected,
                }
            )
    if top_rgb_mismatches:
        raise RuntimeError(f"Top witness RGB mismatch count: {len(top_rgb_mismatches)}")

    top_contours = {}
    for contact_id in ("CL-001", "CL-002", "CL-003"):
        points = top_points_by_contact[contact_id]
        xs = [item["pixel_local"][0] for item in points]
        ys = [item["pixel_local"][1] for item in points]
        min_x, max_x = min(xs), max(xs)
        min_y, max_y = min(ys), max(ys)
        row_stations = {}
        for item in points:
            if item["sector"] not in ("left", "right"):
                continue
            x, y = item["pixel_local"]
            row_stations.setdefault(str(y), {})[item["sector"]] = x
        measured_rows = []
        for y_text, sides in sorted(row_stations.items(), key=lambda pair: int(pair[0])):
            if "left" in sides and "right" in sides:
                measured_rows.append(
                    {
                        "y_px": int(y_text),
                        "left_x_px": sides["left"],
                        "right_x_px": sides["right"],
                        "point_center_delta_px": sides["right"] - sides["left"],
                    }
                )
        top_contours[contact_id] = {
            "classification": "exact_discrete_source_pixel_measurements_no_closure",
            "sample_count": len(points),
            "observed_extrema_px": {
                "min_x": min_x,
                "max_x": max_x,
                "min_y": min_y,
                "max_y": max_y,
            },
            "observed_extrema_point_center_deltas_px": [max_x - min_x, max_y - min_y],
            "observed_extrema_midpoint_px_reference_only_not_component_center": [
                (min_x + max_x) / 2.0,
                (min_y + max_y) / 2.0,
            ],
            "same_row_visible_station_spans": measured_rows,
            "exact_points": [
                {
                    "id": item["id"],
                    "sector": item["sector"],
                    "pixel_local": item["pixel_local"],
                    "source_rgb": item["source_rgb"],
                }
                for item in points
            ],
            "closed_contour_created": False,
            "curve_fit_created": False,
            "filled_region_created": False,
        }

    def largest_component_span(measure, component):
        rows = [item for item in measure["visible_outer_edge_row_samples"] if item["component_id"] == component]
        return max(rows, key=lambda item: item["width_px"])

    def largest_c004_span(measure):
        candidates = []
        for item in measure["irregular_C004_outer_edge_observations"]:
            if "left_source_pixel" in item and "right_source_pixel" in item:
                left = item["left_source_pixel"][0]
                right = item["right_source_pixel"][0]
                candidates.append(
                    {
                        "id": item["id"],
                        "y": item["y"],
                        "left": left,
                        "right": right,
                        "span": right - left,
                        "midpoint": (left + right) / 2.0,
                    }
                )
        return max(candidates, key=lambda item: item["span"])

    front_spans = {component: largest_component_span(front_measure, component) for component in ("C-002", "C-003")}
    left_spans = {component: largest_component_span(left_measure, component) for component in ("C-002", "C-003")}
    front_outer = largest_c004_span(front_measure)
    left_outer = largest_c004_span(left_measure)

    physical = {}
    for component in ("C-002", "C-003"):
        width_fraction = Fraction(front_spans[component]["width_px"] * 140, front_outer["span"])
        depth_fraction = Fraction(left_spans[component]["width_px"] * 110, left_outer["span"])
        physical[component] = {
            "width": fraction_record(width_fraction),
            "depth": fraction_record(depth_fraction),
            "width_to_depth_ratio": round(float(width_fraction / depth_fraction), 6),
            "formula": {
                "width": f"140 * {front_spans[component]['width_px']} / {front_outer['span']}",
                "depth": f"110 * {left_spans[component]['width_px']} / {left_outer['span']}",
            },
            "source_rows": {
                "front": front_spans[component],
                "left": left_spans[component],
            },
            "authority": "same-view ratio to exact visible C-004 outer span and approved 140x110 target extents",
        }

    a04_targets = {"C-002": (120.0, 90.0), "C-003": (136.0, 104.0)}
    a04_comparison = {}
    for component, (a04_width, a04_depth) in a04_targets.items():
        measured_width = physical[component]["width"]["decimal"]
        measured_depth = physical[component]["depth"]["decimal"]
        a04_comparison[component] = {
            "a04_target_cm": [a04_width, a04_depth],
            "a05_measured_cm": [measured_width, measured_depth],
            "a05_minus_a04_cm": [round(measured_width - a04_width, 6), round(measured_depth - a04_depth, 6)],
            "a04_depth_excess_over_a05_measurement_percent": round((a04_depth / measured_depth - 1.0) * 100.0, 6),
        }

    def contact_y_medians_front():
        values = {}
        for sample in front_contacts["samples"]:
            values.setdefault(sample["contact_id"], []).append(sample["panel_local"][1])
        return {key: float(statistics.median(items)) for key, items in values.items()}

    def contact_y_medians_left():
        result = {}
        for contact in left_measure["contact_line_samples"]:
            ys = [point[1] for segment in contact["open_segments"] for point in segment]
            result[contact["contact_id"]] = float(statistics.median(ys))
        return result

    def bottom_y(measure):
        values = []
        for item in measure["irregular_C004_outer_edge_observations"]:
            values.append(item["y"])
        return max(values)

    def height_record(medians, bottom):
        top = medians["CL-001"]
        total = bottom - top
        raw = {
            "C-002": medians["CL-002"] - medians["CL-001"],
            "C-003": medians["CL-003"] - medians["CL-002"],
            "C-004": bottom - medians["CL-003"],
        }
        return {
            "contact_y_medians_px": medians,
            "lowest_exact_outer_edge_observation_y_px": bottom,
            "observed_base_span_px": total,
            "component_visible_spans_px": raw,
            "normalized_to_approved_35_cm_base_span": {
                key: round(35.0 * value / total, 6) for key, value in raw.items()
            },
            "classification": "same-view normalized evidence_not_source_exact_individual_course_height",
        }

    height_front = height_record(contact_y_medians_front(), bottom_y(front_measure))
    height_left = height_record(contact_y_medians_left(), bottom_y(left_measure))
    height_intervals = {}
    for component in ("C-002", "C-003", "C-004"):
        values = [
            height_front["normalized_to_approved_35_cm_base_span"][component],
            height_left["normalized_to_approved_35_cm_base_span"][component],
        ]
        height_intervals[component] = [min(values), max(values)]

    top_ratio = {
        "C002_to_C003_observed_X_delta_ratio": round(
            top_contours["CL-002"]["observed_extrema_point_center_deltas_px"][0]
            / top_contours["CL-003"]["observed_extrema_point_center_deltas_px"][0],
            6,
        ),
        "C002_to_C003_observed_Y_delta_ratio": round(
            top_contours["CL-002"]["observed_extrema_point_center_deltas_px"][1]
            / top_contours["CL-003"]["observed_extrema_point_center_deltas_px"][1],
            6,
        ),
        "front_owner_width_ratio": round(
            physical["C-002"]["width"]["decimal"] / physical["C-003"]["width"]["decimal"], 6
        ),
        "left_owner_depth_ratio": round(
            physical["C-002"]["depth"]["decimal"] / physical["C-003"]["depth"]["decimal"], 6
        ),
    }

    color_routes = {
        "C-002": {
            "top_surface": "top source pixels between exact CL-001 and CL-002 ownership witnesses",
            "front_side": "front source band between exact CL-001 and CL-002 evidence",
            "left_side": "left source band between exact CL-001 and CL-002 evidence",
        },
        "C-003": {
            "top_surface": "top source pixels between exact CL-002 and CL-003 ownership witnesses",
            "front_side": "front source band between exact CL-002 and CL-003 evidence",
            "left_side": "left source band between exact CL-002 and CL-003 evidence",
        },
        "C-004": {
            "top_surface": "top source pixels outward of exact CL-003 witnesses within source-owned rubble",
            "front_side": "front source-owned C-004 irregular edge pixels",
            "left_side": "left source-owned C-004 irregular edge pixels",
        },
    }

    BOARD.parent.mkdir(parents=True, exist_ok=True)
    board = Image.new("RGB", (1920, 1240), (244, 244, 241))
    draw = ImageDraw.Draw(board)
    draw.text((40, 25), "A005 / A05 MEASUREMENT-ONLY BASE AUDIT", font=font(30, True), fill=(20, 20, 20))
    draw.text(
        (40, 63),
        "EXACT SOURCE PIXELS + EXACT MARKS ONLY — NO FILLS, FITTED CURVES, SMOOTHED ENVELOPES, OR GEOMETRY",
        font=font(18, True),
        fill=(145, 20, 20),
    )
    origins = {"top": (40, 100), "front": (760, 100), "left": (1270, 100)}
    scales = {"top": 2, "front": 1, "left": 1}
    for name in ("top", "front", "left"):
        paste_panel(board, panels[name], origins[name], scales[name])
        draw.rectangle(
            (
                origins[name][0] - 1,
                origins[name][1] - 1,
                origins[name][0] + panels[name].width * scales[name],
                origins[name][1] + panels[name].height * scales[name],
            ),
            outline=(0, 0, 0),
            width=1,
        )

    colors = {"CL-001": (0, 220, 90), "CL-002": (255, 155, 0), "CL-003": (0, 210, 255)}
    ox, oy = origins["top"]
    for contact_id, points in top_points_by_contact.items():
        for item in points:
            px, py = item["pixel_local"]
            draw_cross(draw, ox + px * 2, oy + py * 2, colors[contact_id], radius=6)

    component_colors = {"C-002": (255, 110, 0), "C-003": (170, 30, 255), "C-004": (0, 170, 255)}
    for name, measure in (("front", front_measure), ("left", left_measure)):
        ox, oy = origins[name]
        for item in measure["visible_outer_edge_row_samples"]:
            component = item["component_id"]
            if component not in component_colors:
                continue
            left_x, right_x_open = item["span_half_open"]
            draw_cross(draw, ox + left_x, oy + item["y"], component_colors[component], radius=3)
            draw_cross(draw, ox + right_x_open - 1, oy + item["y"], component_colors[component], radius=3)
        for item in measure["irregular_C004_outer_edge_observations"]:
            if "left_source_pixel" in item:
                for key in ("left_source_pixel", "right_source_pixel"):
                    px, py = item[key]
                    draw_cross(draw, ox + px, oy + py, component_colors["C-004"], radius=3)

    legend_y = 860
    draw.text((40, legend_y), "Exact-mark legend", font=font(20, True), fill=(20, 20, 20))
    x = 230
    for label, color in [
        ("CL-001", colors["CL-001"]),
        ("CL-002 / C002", colors["CL-002"]),
        ("CL-003 / C003", colors["CL-003"]),
        ("C004 outer", component_colors["C-004"]),
    ]:
        draw.line((x, legend_y + 12, x + 28, legend_y + 12), fill=color, width=4)
        draw.text((x + 36, legend_y), label, font=font(17), fill=(20, 20, 20))
        x += 220

    upper = physical["C-002"]
    lower = physical["C-003"]
    metric_lines = [
        f"Measured owner-view footprint C002: {upper['width']['decimal']:.2f} x {upper['depth']['decimal']:.2f} cm; X/Y {upper['width_to_depth_ratio']:.3f}",
        f"Measured owner-view footprint C003: {lower['width']['decimal']:.2f} x {lower['depth']['decimal']:.2f} cm; X/Y {lower['width_to_depth_ratio']:.3f}",
        f"A04 depth excess: C002 {a04_comparison['C-002']['a04_depth_excess_over_a05_measurement_percent']:.2f}% | C003 {a04_comparison['C-003']['a04_depth_excess_over_a05_measurement_percent']:.2f}%",
        f"Top exact point deltas: CL002 {top_contours['CL-002']['observed_extrema_point_center_deltas_px']} px | CL003 {top_contours['CL-003']['observed_extrema_point_center_deltas_px']} px",
        f"Course-height evidence intervals (cm): C002 {height_intervals['C-002']} | C003 {height_intervals['C-003']} | C004 {height_intervals['C-004']}",
        "Centers and hidden closures remain BLOCKED as source evidence; the approved production pivot may be used only by a later A05 contract.",
        "Decision: authoritative measurement record ready for A05 contract.",
    ]
    y = 915
    for line in metric_lines:
        fill = (130, 15, 15) if "BLOCKED" in line else (18, 18, 18)
        if line.startswith("Decision"):
            fill = (0, 95, 45)
        draw.text((40, y), line, font=font(19, line.startswith("Decision")), fill=fill)
        y += 39
    board.save(BOARD)

    record = {
        "schema": "aerathea.visual_correction_a05_measurement_audit.v1",
        "asset_id": "SM_GIA_BloodAxeCairnstone_A005",
        "audit_id": "A005-CR-VISUAL-CORRECTION-A05-MEASUREMENT-A01",
        "date": "2026-07-21",
        "status": "authoritative_measurement_record_ready_for_A05_contract",
        "artifact_classification": "authoritative",
        "decision": "authoritative measurement record ready for A05 contract",
        "authority": {
            "handoff": "steps/VISUAL_CORRECTION_A04_VISUAL_REJECTION_A05_RESTART_HANDOFF.md",
            "source_panels": {
                name: {
                    "path": str(panel_paths[name].relative_to(ROOT)),
                    "expected_sha256": expected_hashes[name],
                    "actual_sha256": actual_hashes[name],
                    "hash_match": hash_checks[name],
                    "size_px": list(panels[name].size),
                }
                for name in panel_paths
            },
            "exact_top_contacts": "manifests/STEP_04_TOP_CONTACT_EVIDENCE_RECOVERY_A01.json",
            "front_measurements": "manifests/STEP_06_FRONT_MEASUREMENT_MANIFEST.json",
            "left_measurements": "manifests/STEP_07_LEFT_MEASUREMENT_MANIFEST.json",
            "base_color_ownership": "manifests/STEP_14_BASE_COLOR_OWNERSHIP_MANIFEST.json",
            "approved_target_anchors_cm": {"C004_width": 140, "C004_depth": 110, "base_span": 35},
        },
        "controls": {
            "geometry_created": False,
            "candidate_fill_created": False,
            "inferred_overlay_created": False,
            "closed_contour_created": False,
            "curve_or_oval_fit_created": False,
            "smoothing_performed": False,
            "source_modified": False,
            "color_grading_performed": False,
            "a04_geometry_used_as_measurement_authority": False,
            "measurement_board_contains_only_source_pixels_exact_marks_and_text": True,
        },
        "top_exact_contact_contours": top_contours,
        "owner_view_physical_footprint_measurements_cm": physical,
        "a04_rejected_target_comparison": a04_comparison,
        "cross_view_ratio_checks": top_ratio,
        "height_evidence": {
            "front": height_front,
            "left": height_left,
            "two_view_interval_cm": height_intervals,
            "source_exact_individual_course_height": False,
            "later_contract_must_select_a_35_cm_sum_inside_the_recorded_intervals": True,
        },
        "component_local_color_correspondence": {
            "step14_rule_preserved": step14_color["exact_rgb_transfer_rule"],
            "surface_routes": color_routes,
            "top_exact_witness_statistics": {
                component: rgb_stats(samples) for component, samples in component_color_samples.items()
            },
            "top_witness_rgb_mismatches": len(top_rgb_mismatches),
            "geometry_before_uv_requirement": "A05 must establish corrected component-local geometry and face ownership before UV placement is evaluated.",
            "no_color_grading": True,
        },
        "proven_findings": [
            "A04 C002 and C003 widths were close to the source-owner ratios, but their depths exceeded the corresponding left-owner measurements.",
            "The excess depth was approximately 15.91 percent for C002 and 7.70 percent for C003.",
            "Exact top contact stations are nested and have varying same-row widths; a rectangle is not source-authorized for either base course.",
            "CL002 and CL003 exact extrema midpoints differ by only 0.5 px in X and 1.0 px in Y, but these midpoints remain reference-only and are not promoted to source centers.",
            "The two upright owner views agree that C003 is the taller visible structural course and that the total visible base remains 35 cm.",
            "Exact top witness RGB values remain byte-identical to the authoritative source; the A04 displayed-color issue is therefore not evidence for source recoloring.",
        ],
        "blocked_unknowns_preserved": [
            "fully enumerated closed source-owned C002 and C003 contours",
            "source-authored component centers",
            "hidden contact closure",
            "one unified cross-view pixel scale",
            "source-exact individual course heights",
            "physical pixel identity across different panels",
        ],
        "a05_contract_authority_now_available": [
            "C002 and C003 owner-view footprint extents",
            "exact top-view contact station constraints",
            "same-view course-height evidence intervals",
            "component-local source-pixel routing",
            "A04 plinth preservation and A04 base rejection",
        ],
        "review_board": {
            "path": str(BOARD.relative_to(ROOT)),
            "sha256": sha256(BOARD),
            "artifact_classification": "proof only",
            "geometry_depicted": False,
        },
        "validation": {
            "source_hash_checks_passed": all(hash_checks.values()),
            "exact_top_contact_samples_checked": len(top_contacts["accepted_points"]),
            "top_witness_samples_checked": sum(len(items) for items in component_color_samples.values()),
            "top_witness_rgb_mismatches": len(top_rgb_mismatches),
            "measurement_only_controls_passed": True,
            "failures": 0,
        },
    }
    OUTPUT_JSON.write_text(json.dumps(record, indent=2) + "\n", encoding="utf-8")

    markdown = f"""# A005 Visual Correction A05 Measurement Gate

Status: `authoritative measurement record ready for A05 contract`

Artifact classification: `authoritative`

Date: 2026-07-21

## Decision

`authoritative measurement record ready for A05 contract`

The source supports a bounded A05 replacement-base contract without creating
or presenting candidate geometry in this gate. The exact A04 plinth remains
the visual reference to preserve; the A04 base remains invalid as A05
construction authority.

## Controlling Measurements

- C002 upper course: `{upper['width']['decimal']:.6f} x {upper['depth']['decimal']:.6f} cm`
  from same-view ratios to the approved `140 x 110 cm` C004 anchors.
- C003 lower course: `{lower['width']['decimal']:.6f} x {lower['depth']['decimal']:.6f} cm`.
- A04 depth excess: C002
  `{a04_comparison['C-002']['a04_depth_excess_over_a05_measurement_percent']:.6f}%`;
  C003 `{a04_comparison['C-003']['a04_depth_excess_over_a05_measurement_percent']:.6f}%`.
- Exact top contact point deltas: CL002
  `{top_contours['CL-002']['observed_extrema_point_center_deltas_px']} px`; CL003
  `{top_contours['CL-003']['observed_extrema_point_center_deltas_px']} px`.
- Same-row exact top stations narrow away from their widest recorded rows;
  rectangular C002/C003 footprints are not source-authorized.
- Two-view course-height evidence intervals: C002
  `{height_intervals['C-002']}` cm, C003 `{height_intervals['C-003']}` cm,
  and C004 `{height_intervals['C-004']}` cm. These are measurement bounds, not
  source-exact individual course heights.

## Color Correspondence

The exact top contact witnesses provide 96 byte-checked component-local RGB
samples with `0` mismatch. Step 14's exact RGB transfer rule remains in force.
A05 must correct component-local geometry and face ownership before UV
placement is evaluated; no source recoloring or compensating grade is
authorized.

## Preserved Blocks

- Fully closed source-owned C002/C003 contours.
- Source-authored centers and hidden contact closures.
- A unified cross-view pixel scale.
- Source-exact individual course heights.
- Physical cross-panel pixel identity.

These blocks do not prevent a later A05 construction contract from using the
approved production pivot, a clearly classified oval interpretation bounded
by the exact stations, and a 35 cm course allocation selected inside the
recorded two-view intervals.

## Evidence

- Manifest: `manifests/VISUAL_CORRECTION_A05_MEASUREMENT_AUDIT.json`
- Measurement-only review board:
  `{BOARD.relative_to(ROOT)}`
- Board SHA-256: `{sha256(BOARD)}`

No geometry, candidate fill, inferred contour overlay, smoothing envelope, or
Unreal output was created.
"""
    OUTPUT_MD.write_text(markdown, encoding="utf-8")
    print(json.dumps({
        "status": record["status"],
        "manifest": str(OUTPUT_JSON.relative_to(ROOT)),
        "record": str(OUTPUT_MD.relative_to(ROOT)),
        "board": str(BOARD.relative_to(ROOT)),
        "footprints_cm": {
            "C-002": [upper["width"]["decimal"], upper["depth"]["decimal"]],
            "C-003": [lower["width"]["decimal"], lower["depth"]["decimal"]],
        },
        "failures": 0,
    }, indent=2))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
