#!/usr/bin/env python3
"""Create A001 oval footprint ratio evidence before geometry.

This pass resolves the raw-pixel visual ambiguity in the top view. The source
image has different centimeter-per-pixel values on X and Y, so a measured oval
can appear close to circular in pixel space. This script shows both views:

- raw source-pixel overlay, for registration against the scan
- centimeter-normalized footprint plot, for real width/depth validation

It does not generate mesh data, UVs, texture edits, inferred fill, movement, or
assembled components.
"""

from __future__ import annotations

import hashlib
import json
import math
from pathlib import Path
from typing import Iterable

from PIL import Image, ImageDraw, ImageFont


ROOT = Path(__file__).resolve().parents[2]
ASSET_NAME = "SM_GIA_BloodAxeCairnstone_A001"
SOURCE = ROOT / "docs/assets/reference/bloodaxe_cairnstone_asset/REF_GIA_BloodAxeCairnstoneAsset_A02_BlueprintTemplate.png"
OUT_DIR = ROOT / "Saved/Automation/DCC" / ASSET_NAME
EVIDENCE_DIR = OUT_DIR / "FreshEvidence" / "OvalFootprintRatios"

RESTART_MANIFEST = OUT_DIR / f"{ASSET_NAME}_A001BlueprintRestartManifest.json"
ORIENTATION_MANIFEST = OUT_DIR / f"{ASSET_NAME}_A001OrientationPixelManifest.json"
FORMULA_MANIFEST = OUT_DIR / f"{ASSET_NAME}_A001MeasurementFormulaManifest.json"
CENTER_MANIFEST = OUT_DIR / f"{ASSET_NAME}_A001PixelCountCenterManifest.json"
RADIAL_MANIFEST = OUT_DIR / f"{ASSET_NAME}_A001RadialTraceManifest.json"

OVAL_MANIFEST = OUT_DIR / f"{ASSET_NAME}_A001OvalFootprintRatioManifest.json"
OVAL_OVERLAY = OUT_DIR / f"{ASSET_NAME}_A001OvalFootprintRatioOverlay.png"
OVAL_REVIEW_BOARD = OUT_DIR / f"{ASSET_NAME}_A001OvalFootprintRatioReviewBoard.png"

TOP_SOURCE_CROP = (392, 1070, 724, 1450)

COLORS = {
    "primary_monolith": (228, 42, 42),
    "upper_socket_ring": (255, 138, 30),
    "support_base": (0, 185, 255),
    "assembly_origin": (205, 80, 255),
    "visible_pixel_center": (35, 190, 95),
}

# Reviewed visible ring points remain diagnostic because no separate world
# dimensions have been authored for this hidden/stacked layer yet.
UPPER_RING_VISIBLE_POINTS = [
    (528, 1117),
    (576, 1120),
    (616, 1139),
    (638, 1177),
    (641, 1224),
    (632, 1268),
    (606, 1304),
    (570, 1328),
    (528, 1336),
    (486, 1328),
    (451, 1304),
    (428, 1265),
    (423, 1223),
    (430, 1179),
    (455, 1143),
    (489, 1123),
]

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


def read_json(path: Path) -> dict[str, object]:
    return json.loads(path.read_text())


def verify_preconditions() -> tuple[dict[str, object], dict[str, object], dict[str, object], dict[str, object]]:
    for path in (RESTART_MANIFEST, ORIENTATION_MANIFEST, FORMULA_MANIFEST, CENTER_MANIFEST):
        if not path.exists():
            raise SystemExit(f"Missing required precondition manifest: {path}")

    restart = read_json(RESTART_MANIFEST)
    orientation = read_json(ORIENTATION_MANIFEST)
    formula = read_json(FORMULA_MANIFEST)
    centers = read_json(CENTER_MANIFEST)

    if restart.get("pixel_exact") is not True or restart.get("changed_pixels") != 0 or restart.get("max_rgb_delta") != 0:
        raise SystemExit("A001 source scanline proof is not exact; oval ratio pass is blocked.")

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

    blocking_states = [
        "geometry_generated",
        "uvs_generated",
        "components_moved",
        "components_rotated",
        "components_centered",
        "components_assembled",
        "inferred_fill_generated",
    ]
    for label, manifest in (("formula", formula), ("center", centers)):
        state = manifest.get("pre_geometry_state")
        if not isinstance(state, dict):
            raise SystemExit(f"{label} manifest is missing pre_geometry_state.")
        failed = [key for key in blocking_states if state.get(key) is not False]
        if failed:
            raise SystemExit(f"{label} manifest is no longer pre-geometry clean: {failed}")

    return restart, orientation, formula, centers


def center_lookup(centers: dict[str, object]) -> dict[str, list[float]]:
    result: dict[str, list[float]] = {}
    for item in centers.get("component_centers", []):
        if not isinstance(item, dict):
            continue
        stable_id = str(item.get("stable_component_id"))
        center = item.get("pixel_count_center")
        if isinstance(center, list) and len(center) == 2:
            result[stable_id] = [float(center[0]), float(center[1])]
    return result


def ellipse_points(box: list[int], steps: int = 96) -> list[tuple[float, float]]:
    left, top, right, bottom = box
    cx = (left + right) / 2.0
    cy = (top + bottom) / 2.0
    rx = (right - left) / 2.0
    ry = (bottom - top) / 2.0
    points: list[tuple[float, float]] = []
    for index in range(steps):
        angle = math.tau * index / steps
        points.append((cx + math.cos(angle) * rx, cy + math.sin(angle) * ry))
    return points


def polygon_bounds(points: Iterable[tuple[float, float]]) -> tuple[float, float, float, float]:
    pts = list(points)
    xs = [p[0] for p in pts]
    ys = [p[1] for p in pts]
    return min(xs), min(ys), max(xs), max(ys)


def cm_points(points: Iterable[tuple[float, float]], origin_px: tuple[float, float], cm_per_px: tuple[float, float]) -> list[tuple[float, float]]:
    ox, oy = origin_px
    sx, sy = cm_per_px
    return [((x - ox) * sx, (y - oy) * sy) for x, y in points]


def draw_cross(
    draw: ImageDraw.ImageDraw,
    xy: tuple[float, float],
    color: tuple[int, int, int],
    label: str,
    radius: int = 8,
) -> None:
    x = round(xy[0])
    y = round(xy[1])
    draw.line((x - radius, y, x + radius, y), fill=color, width=3)
    draw.line((x, y - radius, x, y + radius), fill=color, width=3)
    draw.ellipse((x - radius, y - radius, x + radius, y + radius), outline=color, width=2)
    draw.text((x + 10, y - 9), label, fill=color, font=font(11))


def draw_polyline(draw: ImageDraw.ImageDraw, points: list[tuple[float, float]], color: tuple[int, int, int], width: int = 3) -> None:
    if not points:
        return
    rounded = [(round(x), round(y)) for x, y in points]
    draw.line(rounded + [rounded[0]], fill=color, width=width)


def source_to_crop(point: tuple[float, float]) -> tuple[float, float]:
    return point[0] - TOP_SOURCE_CROP[0], point[1] - TOP_SOURCE_CROP[1]


def make_mask(source_size: tuple[int, int], points: list[tuple[float, float]], path: Path) -> int:
    mask = Image.new("L", source_size, 0)
    draw = ImageDraw.Draw(mask)
    draw.polygon([(round(x), round(y)) for x, y in points], fill=255)
    mask.save(path)
    hist = mask.histogram()
    return int(hist[255])


def build_records(formula: dict[str, object], centers: dict[str, object]) -> tuple[list[dict[str, object]], tuple[float, float], tuple[float, float]]:
    views = formula["views"]  # type: ignore[index]
    top = views["top"]  # type: ignore[index]
    top_boxes = top["component_boxes_px"]  # type: ignore[index]
    dimensions = formula["source_dimensions_cm"]  # type: ignore[index]
    cm_per_px = tuple(float(value) for value in top["cm_per_pixel"])  # type: ignore[index]

    support_box = [int(v) for v in top_boxes["support_object"]]  # type: ignore[index]
    formula_origin = (round((support_box[0] + support_box[2]) / 2.0), round((support_box[1] + support_box[3]) / 2.0))
    center_map = center_lookup(centers)

    specs = [
        {
            "stable_component_id": "primary_monolith",
            "component_name": "primary_monolith_measured_oval_envelope",
            "box": [int(v) for v in top_boxes["primary_object"]],  # type: ignore[index]
            "dimension_cm": [float(dimensions["primary_width"]), float(dimensions["primary_depth"])],  # type: ignore[index]
            "authority": "formula-derived measured oval candidate from authored 120cm x 90cm footprint",
            "status": "candidate_pending_review",
        },
        {
            "stable_component_id": "support_base",
            "component_name": "support_base_measured_oval_envelope",
            "box": support_box,
            "dimension_cm": [float(dimensions["support_width"]), float(dimensions["support_depth"])],  # type: ignore[index]
            "authority": "formula-derived measured oval candidate from authored 140cm x 110cm footprint",
            "status": "candidate_pending_review",
        },
    ]

    records: list[dict[str, object]] = []
    for spec in specs:
        box = list(spec["box"])  # type: ignore[arg-type]
        points_px = ellipse_points(box)
        points_cm = cm_points(points_px, formula_origin, cm_per_px)
        left, top_y, right, bottom = box
        width_px = right - left
        depth_px = bottom - top_y
        width_cm_from_px = width_px * cm_per_px[0]
        depth_cm_from_px = depth_px * cm_per_px[1]
        target_width_cm, target_depth_cm = spec["dimension_cm"]  # type: ignore[misc]
        record = {
            "stable_component_id": spec["stable_component_id"],
            "component_name": spec["component_name"],
            "source_view": "top",
            "top_formula_box_px": box,
            "formula_origin_px": [formula_origin[0], formula_origin[1]],
            "visible_pixel_count_center_px": center_map.get(str(spec["stable_component_id"])),
            "cm_per_pixel": [round(cm_per_px[0], 8), round(cm_per_px[1], 8)],
            "source_pixel_width_depth_px": [width_px, depth_px],
            "source_pixel_width_depth_ratio": round(width_px / depth_px, 6),
            "measured_width_depth_cm": [target_width_cm, target_depth_cm],
            "measured_width_depth_ratio": round(target_width_cm / target_depth_cm, 6),
            "box_converted_width_depth_cm": [round(width_cm_from_px, 4), round(depth_cm_from_px, 4)],
            "box_converted_width_depth_ratio": round(width_cm_from_px / depth_cm_from_px, 6),
            "ratio_error_abs": round(abs((width_cm_from_px / depth_cm_from_px) - (target_width_cm / target_depth_cm)), 6),
            "raw_pixel_preview_can_look_near_circular": True,
            "centimeter_normalized_preview_required": True,
            "authority": spec["authority"],
            "geometry_authority_status": spec["status"],
            "ellipse_points_px": [[round(x, 4), round(y, 4)] for x, y in points_px],
            "ellipse_points_cm": [[round(x, 4), round(y, 4)] for x, y in points_cm],
            "no_geometry_generated": True,
            "components_moved": False,
            "components_assembled": False,
        }
        records.append(record)

    upper_cm = cm_points(UPPER_RING_VISIBLE_POINTS, formula_origin, cm_per_px)
    min_x, min_y, max_x, max_y = polygon_bounds(UPPER_RING_VISIBLE_POINTS)
    upper_width_px = max_x - min_x
    upper_depth_px = max_y - min_y
    upper_width_cm = upper_width_px * cm_per_px[0]
    upper_depth_cm = upper_depth_px * cm_per_px[1]
    records.append(
        {
            "stable_component_id": "upper_socket_ring",
            "component_name": "upper_socket_ring_visible_envelope_diagnostic",
            "source_view": "top",
            "top_formula_box_px": None,
            "formula_origin_px": [formula_origin[0], formula_origin[1]],
            "visible_pixel_count_center_px": center_map.get("upper_socket_ring"),
            "cm_per_pixel": [round(cm_per_px[0], 8), round(cm_per_px[1], 8)],
            "source_pixel_width_depth_px": [round(upper_width_px, 4), round(upper_depth_px, 4)],
            "source_pixel_width_depth_ratio": round(upper_width_px / upper_depth_px, 6),
            "measured_width_depth_cm": None,
            "measured_width_depth_ratio": None,
            "box_converted_width_depth_cm": [round(upper_width_cm, 4), round(upper_depth_cm, 4)],
            "box_converted_width_depth_ratio": round(upper_width_cm / upper_depth_cm, 6),
            "ratio_error_abs": None,
            "raw_pixel_preview_can_look_near_circular": True,
            "centimeter_normalized_preview_required": True,
            "authority": "diagnostic visible shared/occluded envelope only; no independent world dimensions authored yet",
            "geometry_authority_status": "diagnostic_only_blocked_until_layer_dimensions_or_contact_formula_are_approved",
            "ellipse_points_px": [[float(x), float(y)] for x, y in UPPER_RING_VISIBLE_POINTS],
            "ellipse_points_cm": [[round(x, 4), round(y, 4)] for x, y in upper_cm],
            "no_geometry_generated": True,
            "components_moved": False,
            "components_assembled": False,
        }
    )

    return records, formula_origin, cm_per_px


def create_overlay(source: Image.Image, records: list[dict[str, object]], formula_origin: tuple[float, float]) -> None:
    overlay = source.copy()
    draw = ImageDraw.Draw(overlay)
    draw.rectangle((10, 10, 1120, 104), fill=(255, 255, 255), outline=(30, 30, 30), width=2)
    draw.text((24, 18), "A001 measured oval footprint ratio proof - evidence only", fill=(20, 18, 16), font=font(20))
    draw.text((24, 52), "Raw source pixels can look near-round because top X/Y centimeter scales differ.", fill=(80, 42, 92), font=font(15))
    draw.text((24, 76), "Geometry remains blocked until the normalized oval review is approved.", fill=(80, 42, 92), font=font(15))

    draw_cross(draw, formula_origin, COLORS["assembly_origin"], "formula origin")
    for record in records:
        stable_id = str(record["stable_component_id"])
        color = COLORS.get(stable_id, (255, 255, 255))
        points_px = [(float(x), float(y)) for x, y in record["ellipse_points_px"]]  # type: ignore[misc]
        draw_polyline(draw, points_px, color, 4)
        center = record.get("visible_pixel_count_center_px")
        if isinstance(center, list) and len(center) == 2:
            draw_cross(draw, (float(center[0]), float(center[1])), COLORS["visible_pixel_center"], f"{stable_id} visible center", 6)

    OVAL_OVERLAY.parent.mkdir(parents=True, exist_ok=True)
    overlay.save(OVAL_OVERLAY)


def cm_plot_transform(point: tuple[float, float], panel_box: tuple[int, int, int, int]) -> tuple[float, float]:
    left, top, right, bottom = panel_box
    cx = (left + right) / 2.0
    cy = (top + bottom) / 2.0
    scale = 4.2
    return cx + point[0] * scale, cy + point[1] * scale


def create_review_board(
    source: Image.Image,
    records: list[dict[str, object]],
    formula_origin: tuple[float, float],
    cm_per_px: tuple[float, float],
) -> None:
    board = Image.new("RGB", (1900, 1360), (245, 243, 238))
    draw = ImageDraw.Draw(board)
    draw.text((40, 28), "A001 Oval Footprint Ratio Review", fill=(24, 21, 18), font=font(30))
    draw.text((40, 74), "Raw source-pixel view plus centimeter-normalized view. Evidence only; no mesh generated.", fill=(55, 48, 42), font=font(18))

    source_panel = source.crop(TOP_SOURCE_CROP).copy()
    source_draw = ImageDraw.Draw(source_panel)
    draw_cross(source_draw, source_to_crop(formula_origin), COLORS["assembly_origin"], "formula origin", 7)
    for record in records:
        stable_id = str(record["stable_component_id"])
        color = COLORS.get(stable_id, (255, 255, 255))
        points = [source_to_crop((float(x), float(y))) for x, y in record["ellipse_points_px"]]  # type: ignore[misc]
        draw_polyline(source_draw, points, color, 3)
        center = record.get("visible_pixel_count_center_px")
        if isinstance(center, list) and len(center) == 2:
            draw_cross(source_draw, source_to_crop((float(center[0]), float(center[1]))), COLORS["visible_pixel_center"], "", 6)
    source_panel = source_panel.resize((664, 760), RESAMPLE_LANCZOS)
    board.paste(source_panel, (40, 130))
    draw.rectangle((40, 130, 704, 890), outline=(70, 64, 56), width=2)
    draw.text((40, 908), "Raw source-pixel overlay", fill=(32, 28, 24), font=font(20))

    panel = (820, 145, 1710, 725)
    draw.rectangle(panel, fill=(20, 20, 20), outline=(70, 64, 56), width=2)
    draw.text((820, 105), "Centimeter-normalized footprint view", fill=(32, 28, 24), font=font(20))

    # Grid lines in 10 cm increments.
    for cm in range(-80, 81, 10):
        x0, y0 = cm_plot_transform((cm, -65), panel)
        x1, y1 = cm_plot_transform((cm, 65), panel)
        draw.line((x0, y0, x1, y1), fill=(48, 48, 48), width=1)
    for cm in range(-60, 61, 10):
        x0, y0 = cm_plot_transform((-85, cm), panel)
        x1, y1 = cm_plot_transform((85, cm), panel)
        draw.line((x0, y0, x1, y1), fill=(48, 48, 48), width=1)
    x0, y0 = cm_plot_transform((-85, 0), panel)
    x1, y1 = cm_plot_transform((85, 0), panel)
    draw.line((x0, y0, x1, y1), fill=(105, 105, 105), width=2)
    x0, y0 = cm_plot_transform((0, -65), panel)
    x1, y1 = cm_plot_transform((0, 65), panel)
    draw.line((x0, y0, x1, y1), fill=(105, 105, 105), width=2)

    for record in records:
        stable_id = str(record["stable_component_id"])
        color = COLORS.get(stable_id, (255, 255, 255))
        cm_pts = [(float(x), float(y)) for x, y in record["ellipse_points_cm"]]  # type: ignore[misc]
        screen_pts = [cm_plot_transform(point, panel) for point in cm_pts]
        width = 4 if stable_id != "upper_socket_ring" else 3
        draw_polyline(draw, screen_pts, color, width)

    origin_screen = cm_plot_transform((0, 0), panel)
    draw_cross(draw, origin_screen, COLORS["assembly_origin"], "origin", 8)

    legend_x, legend_y = 825, 745
    legend_lines = [
        ("primary_monolith", "measured 120 x 90 cm oval candidate"),
        ("support_base", "measured 140 x 110 cm oval candidate"),
        ("upper_socket_ring", "visible shared envelope diagnostic only"),
        ("visible_pixel_center", "visible pixel-count centers are diagnostic here"),
    ]
    for i, (key, label) in enumerate(legend_lines):
        y = legend_y + i * 28
        draw.rectangle((legend_x, y + 5, legend_x + 22, y + 21), fill=COLORS[key])
        draw.text((legend_x + 34, y), label, fill=(42, 36, 30), font=font(16))

    table_x, table_y = 40, 960
    draw.rectangle((table_x, table_y, 1810, 1276), fill=(255, 255, 255), outline=(75, 68, 62), width=2)
    draw.text((table_x + 18, table_y + 18), "Ratio Check", fill=(24, 21, 18), font=font(22))
    draw.text((table_x + 18, table_y + 54), f"Top calibration: X={cm_per_px[0]:.6f} cm/px, Y={cm_per_px[1]:.6f} cm/px", fill=(48, 42, 36), font=font(16))
    headers = ["component", "source px W:D", "px ratio", "world cm W:D", "world ratio", "authority"]
    col_x = [58, 430, 655, 835, 1100, 1320]
    for x, header in zip(col_x, headers):
        draw.text((x, table_y + 92), header, fill=(24, 21, 18), font=font(15))
    for row, record in enumerate(records):
        y = table_y + 126 + row * 56
        component = str(record["stable_component_id"])
        px = record["source_pixel_width_depth_px"]
        cm = record["measured_width_depth_cm"] or record["box_converted_width_depth_cm"]
        px_ratio = record["source_pixel_width_depth_ratio"]
        cm_ratio = record["measured_width_depth_ratio"] or record["box_converted_width_depth_ratio"]
        authority = str(record["authority"])
        if len(authority) > 60:
            authority = authority[:57] + "..."
        draw.text((col_x[0], y), component, fill=(42, 36, 30), font=font(15))
        draw.text((col_x[1], y), f"{px[0]} x {px[1]}", fill=(42, 36, 30), font=font(15))  # type: ignore[index]
        draw.text((col_x[2], y), f"{px_ratio}", fill=(42, 36, 30), font=font(15))
        draw.text((col_x[3], y), f"{cm[0]} x {cm[1]}", fill=(42, 36, 30), font=font(15))  # type: ignore[index]
        draw.text((col_x[4], y), f"{cm_ratio}", fill=(42, 36, 30), font=font(15))
        draw.text((col_x[5], y), authority, fill=(42, 36, 30), font=font(15))

    rules = [
        "Raw pixel-space roundness is not approval authority when X/Y cm-per-pixel differs.",
        "The hard check is the world-space width/depth ratio: base 140/110 and primary 120/90.",
        "Visible pixel-count centers remain recorded, but they do not overwrite the measured formula origin.",
        "No source pixels, geometry, UVs, movement, rotation, centering, or assembly were changed.",
    ]
    for i, rule in enumerate(rules):
        draw.text((table_x + 18, table_y + 294 + i * 24), f"- {rule}", fill=(48, 42, 36), font=font(15))

    board.save(OVAL_REVIEW_BOARD)


def build_manifest(
    restart: dict[str, object],
    orientation: dict[str, object],
    formula: dict[str, object],
    centers: dict[str, object],
    records: list[dict[str, object]],
    formula_origin: tuple[float, float],
    cm_per_px: tuple[float, float],
) -> dict[str, object]:
    radial_status = "not_present"
    if RADIAL_MANIFEST.exists():
        radial_status = "prior_radial_board_is_diagnostic_only_until_oval_ratio_review_is_approved"
    return {
        "asset": ASSET_NAME,
        "status": "A001 oval footprint ratio evidence recorded before geometry",
        "source": str(SOURCE.relative_to(ROOT)),
        "source_sha256": sha256_file(SOURCE),
        "source_scanline_manifest": str(RESTART_MANIFEST.relative_to(ROOT)),
        "orientation_pixel_manifest": str(ORIENTATION_MANIFEST.relative_to(ROOT)),
        "measurement_formula_manifest": str(FORMULA_MANIFEST.relative_to(ROOT)),
        "pixel_count_center_manifest": str(CENTER_MANIFEST.relative_to(ROOT)),
        "prior_radial_trace_manifest": str(RADIAL_MANIFEST.relative_to(ROOT)) if RADIAL_MANIFEST.exists() else None,
        "prior_radial_trace_status": radial_status,
        "oval_footprint_overlay": str(OVAL_OVERLAY.relative_to(ROOT)),
        "oval_footprint_review_board": str(OVAL_REVIEW_BOARD.relative_to(ROOT)),
        "source_proof": {
            "restart_pixel_exact": restart.get("pixel_exact"),
            "restart_changed_pixels": restart.get("changed_pixels"),
            "restart_max_rgb_delta": restart.get("max_rgb_delta"),
            "orientation_mark_count": len(orientation.get("markers", [])) if isinstance(orientation.get("markers"), list) else None,
            "formula_status": formula.get("status"),
            "center_status": centers.get("status"),
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
        "formula_origin_policy": {
            "formula_origin_px": [formula_origin[0], formula_origin[1]],
            "formula_origin_source": "top formula support-object box rounded center; same source family as 140x110 and 120x90 measurement boxes",
            "visible_pixel_centers_are_diagnostic_for_this_oval_review": True,
            "formula_origin_does_not_move_source_components": True,
        },
        "oval_ratio_formula": {
            "cm_per_pixel_x": round(cm_per_px[0], 8),
            "cm_per_pixel_y": round(cm_per_px[1], 8),
            "raw_source_pixel_preview": "registration diagnostic only; can look near-circular",
            "centimeter_normalized_preview": "required footprint ratio authority for oval approval",
            "base_ratio": "140cm / 110cm",
            "primary_ratio": "120cm / 90cm",
            "not_used": [
                "perfect-circle assumption",
                "raw pixel-space roundness as approval authority",
                "visible color-density center as forced geometry origin",
                "mesh generation",
                "component movement",
            ],
        },
        "oval_footprint_records": records,
        "geometry_use_status": "candidate_pending_review; blocked_until_oval_ratio_board_is_approved_and_formula_archive_is_updated",
        "blocked_until_declared_next": [
            "review oval footprint ratio board",
            "approve or revise formula-origin versus visible-center authority",
            "approve or revise measured oval envelope as footprint candidate",
            "update formula archive if approved",
            "only then continue to geometry construction plan",
        ],
    }


def main() -> None:
    restart, orientation, formula, centers = verify_preconditions()
    source = Image.open(SOURCE).convert("RGB")
    EVIDENCE_DIR.mkdir(parents=True, exist_ok=True)

    records, formula_origin, cm_per_px = build_records(formula, centers)
    for record in records:
        points_px = [(float(x), float(y)) for x, y in record["ellipse_points_px"]]  # type: ignore[misc]
        mask_path = EVIDENCE_DIR / f"{ASSET_NAME}_{record['component_name']}_Mask.png"
        record["mask_path"] = str(mask_path.relative_to(ROOT))
        record["filled_pixel_count"] = make_mask(source.size, points_px, mask_path)

    create_overlay(source, records, formula_origin)
    create_review_board(source, records, formula_origin, cm_per_px)

    manifest = build_manifest(restart, orientation, formula, centers, records, formula_origin, cm_per_px)
    OVAL_MANIFEST.write_text(json.dumps(manifest, indent=2) + "\n")

    print(f"A001 oval footprint ratio manifest: {OVAL_MANIFEST}")
    print(f"A001 oval footprint ratio overlay: {OVAL_OVERLAY}")
    print(f"A001 oval footprint ratio review board: {OVAL_REVIEW_BOARD}")
    for record in records:
        print(
            f"{record['stable_component_id']}: px_ratio={record['source_pixel_width_depth_ratio']} "
            f"world_ratio={record['measured_width_depth_ratio'] or record['box_converted_width_depth_ratio']} "
            f"status={record['geometry_authority_status']}"
        )
    print("geometry_generated=False components_moved=False components_assembled=False")


if __name__ == "__main__":
    main()
