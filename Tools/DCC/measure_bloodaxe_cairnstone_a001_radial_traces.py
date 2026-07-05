#!/usr/bin/env python3
"""Create A001 shared-origin radial perimeter trace evidence.

This pass tests the shared-origin radial perimeter method. It records reviewed
perimeter control points, ray samples, filled contour masks, calculated centers,
and deltas from the shared assembly origin. It does not generate mesh data,
UVs, texture edits, inferred fill, or assembled components.
"""

from __future__ import annotations

import hashlib
import json
import math
from pathlib import Path

from PIL import Image, ImageDraw, ImageFont


ROOT = Path(__file__).resolve().parents[2]
ASSET_NAME = "SM_GIA_BloodAxeCairnstone_A001"
SOURCE = ROOT / "docs/assets/reference/bloodaxe_cairnstone_asset/REF_GIA_BloodAxeCairnstoneAsset_A02_BlueprintTemplate.png"
OUT_DIR = ROOT / "Saved/Automation/DCC" / ASSET_NAME
RADIAL_DIR = OUT_DIR / "FreshEvidence" / "RadialPerimeterTraces"
RESTART_MANIFEST = OUT_DIR / f"{ASSET_NAME}_A001BlueprintRestartManifest.json"
ORIENTATION_MANIFEST = OUT_DIR / f"{ASSET_NAME}_A001OrientationPixelManifest.json"
FORMULA_MANIFEST = OUT_DIR / f"{ASSET_NAME}_A001MeasurementFormulaManifest.json"
CENTER_MANIFEST = OUT_DIR / f"{ASSET_NAME}_A001PixelCountCenterManifest.json"
SNAP_MANIFEST = OUT_DIR / f"{ASSET_NAME}_A001SnapAnchorManifest.json"
CONTOUR_MANIFEST = OUT_DIR / f"{ASSET_NAME}_A001LayerContourManifest.json"
RADIAL_MANIFEST = OUT_DIR / f"{ASSET_NAME}_A001RadialTraceManifest.json"
RADIAL_OVERLAY = OUT_DIR / f"{ASSET_NAME}_A001RadialTraceOverlay.png"
RADIAL_REVIEW_BOARD = OUT_DIR / f"{ASSET_NAME}_A001RadialTraceReviewBoard.png"


TOP_SOURCE_CROP = (392, 1070, 724, 1450)
RAY_COUNT = 32
ANGLE_STEP_DEG = 360.0 / RAY_COUNT


COLORS = {
    "primary_monolith": (228, 42, 42),
    "upper_socket_ring": (255, 138, 30),
    "support_base": (0, 185, 255),
    "assembled_top_footprint_review_only": (205, 80, 255),
}


RADIAL_COMPONENTS = {
    "primary_monolith": {
        "component_name": "primary_monolith_radial_footprint",
        "top_contour_classification": "independent_component_footprint",
        "perimeter_stop_rule": "reviewed source-owned top-face edge points, replacing rejected seed-connected mask",
        "source_component_role": "standalone_or_assembly_component",
        "visible_angular_sectors_deg": [[0.0, 360.0]],
        "occluded_angular_sectors_deg": [],
        "inferred_angular_sectors_deg": [],
        "reviewed_perimeter_control_points_px": [
            (463, 1148),
            (510, 1146),
            (560, 1146),
            (604, 1149),
            (626, 1162),
            (638, 1194),
            (638, 1244),
            (626, 1283),
            (595, 1298),
            (545, 1302),
            (494, 1298),
            (462, 1285),
            (445, 1252),
            (443, 1212),
            (450, 1176),
        ],
    },
    "upper_socket_ring": {
        "component_name": "upper_socket_ring_radial_shared_envelope",
        "top_contour_classification": "shared_stacked_layer_envelope",
        "perimeter_stop_rule": "reviewed shared upper/ring outer envelope; hidden overlap under primary remains occluded",
        "source_component_role": "assembly_component_with_occluded_inner_contact",
        "visible_angular_sectors_deg": [[0.0, 360.0]],
        "occluded_angular_sectors_deg": [[0.0, 360.0]],
        "inferred_angular_sectors_deg": [],
        "reviewed_perimeter_control_points_px": [
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
        ],
    },
    "support_base": {
        "component_name": "support_base_radial_outer_envelope",
        "top_contour_classification": "shared_stacked_layer_outer_envelope",
        "perimeter_stop_rule": "reviewed outer visible base footprint; hidden under upper layers remains occluded",
        "source_component_role": "standalone_or_assembly_component_with_occluded_top",
        "visible_angular_sectors_deg": [[0.0, 360.0]],
        "occluded_angular_sectors_deg": [[0.0, 360.0]],
        "inferred_angular_sectors_deg": [],
        "reviewed_perimeter_control_points_px": [
            (528, 1112),
            (578, 1118),
            (618, 1142),
            (642, 1182),
            (648, 1225),
            (640, 1270),
            (616, 1307),
            (578, 1332),
            (528, 1342),
            (478, 1332),
            (438, 1305),
            (414, 1266),
            (408, 1222),
            (416, 1178),
            (442, 1141),
            (482, 1118),
        ],
    },
    "assembled_top_footprint_review_only": {
        "component_name": "assembled_top_radial_review_envelope",
        "top_contour_classification": "review_only_assembled_footprint",
        "perimeter_stop_rule": "same reviewed outer visible base footprint used for full assembly review envelope",
        "source_component_role": "review_only_not_a_separate_export",
        "visible_angular_sectors_deg": [[0.0, 360.0]],
        "occluded_angular_sectors_deg": [],
        "inferred_angular_sectors_deg": [],
        "reviewed_perimeter_control_points_px": [
            (528, 1112),
            (578, 1118),
            (618, 1142),
            (642, 1182),
            (648, 1225),
            (640, 1270),
            (616, 1307),
            (578, 1332),
            (528, 1342),
            (478, 1332),
            (438, 1305),
            (414, 1266),
            (408, 1222),
            (416, 1178),
            (442, 1141),
            (482, 1118),
        ],
    },
}


RESAMPLE_LANCZOS = getattr(Image, "Resampling", Image).LANCZOS
RESAMPLE_NEAREST = getattr(Image, "Resampling", Image).NEAREST


def font(size: int) -> ImageFont.ImageFont:
    candidates = [
        "/usr/share/fonts/truetype/dejavu/DejaVuSans.ttf",
        "/usr/share/fonts/truetype/liberation2/LiberationSans-Regular.ttf",
    ]
    for candidate in candidates:
        try:
            return ImageFont.truetype(candidate, size)
        except OSError:
            continue
    return ImageFont.load_default()


def sha256_file(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest()


def read_json(path: Path) -> dict[str, object]:
    return json.loads(path.read_text())


def verify_preconditions() -> tuple[dict[str, object], dict[str, object], dict[str, object], dict[str, object], dict[str, object], dict[str, object]]:
    for path in (RESTART_MANIFEST, ORIENTATION_MANIFEST, FORMULA_MANIFEST, CENTER_MANIFEST, SNAP_MANIFEST, CONTOUR_MANIFEST):
        if not path.exists():
            raise SystemExit(f"Missing required precondition manifest: {path}")

    restart = read_json(RESTART_MANIFEST)
    orientation = read_json(ORIENTATION_MANIFEST)
    formula = read_json(FORMULA_MANIFEST)
    centers = read_json(CENTER_MANIFEST)
    snap = read_json(SNAP_MANIFEST)
    contours = read_json(CONTOUR_MANIFEST)

    if restart.get("pixel_exact") is not True or restart.get("changed_pixels") != 0 or restart.get("max_rgb_delta") != 0:
        raise SystemExit("A001 source scanline proof is not exact; radial trace pass is blocked.")

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
    for label, manifest in (
        ("formula", formula),
        ("center", centers),
        ("snap", snap),
        ("contour", contours),
    ):
        state = manifest.get("pre_geometry_state")
        if not isinstance(state, dict):
            raise SystemExit(f"{label} manifest is missing pre_geometry_state.")
        failed = [key for key in blocking_states if state.get(key) is not False]
        if failed:
            raise SystemExit(f"{label} manifest is no longer pre-geometry clean: {failed}")

    return restart, orientation, formula, centers, snap, contours


def shared_origin_from_centers(centers: dict[str, object]) -> tuple[float, float]:
    for item in centers.get("component_centers", []):
        if not isinstance(item, dict):
            continue
        if item.get("stable_component_id") == "assembled_top_footprint_review_only":
            center = item["pixel_count_center"]
            return float(center[0]), float(center[1])  # type: ignore[index]
    raise SystemExit("Could not find assembled_top_footprint_review_only center.")


def polygon_pixels(source_size: tuple[int, int], points: list[tuple[int, int]]) -> set[tuple[int, int]]:
    mask = Image.new("L", source_size, 0)
    draw = ImageDraw.Draw(mask)
    draw.polygon(points, fill=255)
    mask_pixels = mask.load()
    return {
        (x, y)
        for y in range(mask.height)
        for x in range(mask.width)
        if mask_pixels[x, y] > 0
    }


def contour_pixels(filled_pixels: set[tuple[int, int]]) -> set[tuple[int, int]]:
    contour: set[tuple[int, int]] = set()
    for x, y in filled_pixels:
        for nx, ny in ((x - 1, y), (x + 1, y), (x, y - 1), (x, y + 1)):
            if (nx, ny) not in filled_pixels:
                contour.add((x, y))
                break
    return contour


def centroid(pixels: set[tuple[int, int]]) -> tuple[float, float]:
    return sum(x for x, _ in pixels) / len(pixels), sum(y for _, y in pixels) / len(pixels)


def save_mask(source_size: tuple[int, int], pixels: set[tuple[int, int]], path: Path) -> None:
    mask = Image.new("L", source_size, 0)
    mask_pixels = mask.load()
    for x, y in pixels:
        mask_pixels[x, y] = 255
    mask.save(path)


def ray_segment_intersection(
    origin: tuple[float, float],
    direction: tuple[float, float],
    p1: tuple[int, int],
    p2: tuple[int, int],
) -> tuple[float, float, float] | None:
    ox, oy = origin
    dx, dy = direction
    x1, y1 = p1
    x2, y2 = p2
    sx = x2 - x1
    sy = y2 - y1
    det = -dx * sy + dy * sx
    if abs(det) < 1e-9:
        return None
    rx = x1 - ox
    ry = y1 - oy
    t = (-sy * rx + sx * ry) / det
    u = (-dy * rx + dx * ry) / det
    if t >= 0 and 0 <= u <= 1:
        return ox + t * dx, oy + t * dy, t
    return None


def sample_radial_points(
    origin: tuple[float, float],
    control_points: list[tuple[int, int]],
    ray_count: int,
) -> list[dict[str, object]]:
    samples: list[dict[str, object]] = []
    segments = list(zip(control_points, control_points[1:] + [control_points[0]]))
    for index in range(ray_count):
        angle_deg = index * (360.0 / ray_count)
        radians = math.radians(angle_deg)
        direction = (math.cos(radians), math.sin(radians))
        hits = [
            hit
            for p1, p2 in segments
            if (hit := ray_segment_intersection(origin, direction, p1, p2)) is not None
        ]
        if not hits:
            raise SystemExit(f"No radial perimeter hit at {angle_deg} degrees.")
        x, y, distance = min(hits, key=lambda item: item[2])
        samples.append(
            {
                "index": index,
                "angle_deg": round(angle_deg, 4),
                "perimeter_point_px": [round(x, 4), round(y, 4)],
                "rounded_perimeter_point_px": [round(x), round(y)],
                "radius_px": round(distance, 4),
            }
        )
    return samples


def measure_radial_component(
    source_size: tuple[int, int],
    shared_origin: tuple[float, float],
    stable_component_id: str,
    spec: dict[str, object],
) -> dict[str, object]:
    control_points = [(int(x), int(y)) for x, y in spec["reviewed_perimeter_control_points_px"]]  # type: ignore[misc]
    samples = sample_radial_points(shared_origin, control_points, RAY_COUNT)
    radial_points = [
        (int(point[0]), int(point[1]))
        for sample in samples
        for point in [sample["rounded_perimeter_point_px"]]  # type: ignore[index]
    ]
    filled_pixels = polygon_pixels(source_size, radial_points)
    perimeter_pixels = contour_pixels(filled_pixels)
    center_x, center_y = centroid(filled_pixels)
    delta_x = center_x - shared_origin[0]
    delta_y = center_y - shared_origin[1]
    xs = [x for x, _ in filled_pixels]
    ys = [y for _, y in filled_pixels]

    component_name = str(spec["component_name"])
    filled_path = RADIAL_DIR / f"{ASSET_NAME}_{component_name}_RadialFilledContourMask.png"
    perimeter_path = RADIAL_DIR / f"{ASSET_NAME}_{component_name}_RadialPerimeterMask.png"
    save_mask(source_size, filled_pixels, filled_path)
    save_mask(source_size, perimeter_pixels, perimeter_path)

    return {
        "stable_component_id": stable_component_id,
        "component_name": component_name,
        "source_view": "top",
        "top_contour_classification": spec["top_contour_classification"],
        "source_file": str(SOURCE.relative_to(ROOT)),
        "source_sha256": sha256_file(SOURCE),
        "source_scanline_manifest": str(RESTART_MANIFEST.relative_to(ROOT)),
        "shared_origin_px": [round(shared_origin[0], 4), round(shared_origin[1], 4)],
        "shared_origin_role": "approved assembled top footprint review center used as radial trace origin, not forced component recentering",
        "ray_count": RAY_COUNT,
        "angle_step_deg": ANGLE_STEP_DEG,
        "image_angle_convention": "0 degrees points right in source pixels; positive angles rotate down because image Y increases downward",
        "perimeter_stop_rule": spec["perimeter_stop_rule"],
        "reviewed_perimeter_control_points_px": [list(point) for point in control_points],
        "radial_perimeter_samples": samples,
        "visible_angular_sectors_deg": spec["visible_angular_sectors_deg"],
        "occluded_angular_sectors_deg": spec["occluded_angular_sectors_deg"],
        "inferred_angular_sectors_deg": spec["inferred_angular_sectors_deg"],
        "filled_contour_pixel_count": len(filled_pixels),
        "perimeter_pixel_count": len(perimeter_pixels),
        "calculated_footprint_center_px": [round(center_x, 4), round(center_y, 4)],
        "rounded_calculated_footprint_center_px": [round(center_x), round(center_y)],
        "center_delta_from_shared_origin_px": [round(delta_x, 4), round(delta_y, 4)],
        "filled_contour_bounds_px": [min(xs), min(ys), max(xs) + 1, max(ys) + 1],
        "filled_contour_mask_path": str(filled_path.relative_to(ROOT)),
        "perimeter_mask_path": str(perimeter_path.relative_to(ROOT)),
        "source_component_role": spec["source_component_role"],
        "geometry_authority_status": "candidate_pending_radial_trace_review_and_formula_archive_update",
        "not_a_circle_assumption": True,
        "no_geometry_generated": True,
        "components_moved": False,
        "components_assembled": False,
    }


def draw_cross(draw: ImageDraw.ImageDraw, xy: tuple[float, float], color: tuple[int, int, int], label: str, radius: int = 8) -> None:
    x = round(xy[0])
    y = round(xy[1])
    draw.line((x - radius, y, x + radius, y), fill=color, width=3)
    draw.line((x, y - radius, x, y + radius), fill=color, width=3)
    draw.ellipse((x - radius, y - radius, x + radius, y + radius), outline=color, width=2)
    draw.text((x + 10, y - 9), label, fill=color, font=font(11))


def create_overlay(source: Image.Image, shared_origin: tuple[float, float], records: list[dict[str, object]]) -> None:
    overlay = source.copy()
    draw = ImageDraw.Draw(overlay)
    draw.rectangle((10, 10, 1045, 92), fill=(255, 255, 255), outline=(30, 30, 30), width=2)
    draw.text((24, 18), "A001 shared-origin radial perimeter traces - evidence only", fill=(20, 18, 16), font=font(20))
    draw.text((24, 52), "Rays start at shared assembly origin; contours are reviewed perimeter traces, not perfect circles.", fill=(80, 42, 92), font=font(15))
    draw_cross(draw, shared_origin, (255, 0, 255), "shared origin")
    for record in records:
        color = COLORS[str(record["stable_component_id"])]
        points = [
            tuple(sample["rounded_perimeter_point_px"])  # type: ignore[arg-type]
            for sample in record["radial_perimeter_samples"]  # type: ignore[index]
        ]
        draw.line(points + [points[0]], fill=color, width=3)
        for point in points:
            draw.line((shared_origin[0], shared_origin[1], point[0], point[1]), fill=(245, 206, 35), width=1)
        cx, cy = record["calculated_footprint_center_px"]  # type: ignore[misc]
        draw_cross(draw, (float(cx), float(cy)), color, str(record["stable_component_id"]))
    overlay.save(RADIAL_OVERLAY)


def create_review_board(source: Image.Image, shared_origin: tuple[float, float], records: list[dict[str, object]]) -> None:
    board = Image.new("RGB", (1900, 1380), (245, 243, 238))
    draw = ImageDraw.Draw(board)
    draw.text((40, 28), "A001 Shared-Origin Radial Trace Review", fill=(24, 21, 18), font=font(30))
    draw.text((40, 74), "Radial samples from the shared origin to reviewed perimeters. Evidence only; no mesh generated.", fill=(55, 48, 42), font=font(18))

    top_panel = source.crop(TOP_SOURCE_CROP).copy()
    top_draw = ImageDraw.Draw(top_panel)
    shifted_origin = (shared_origin[0] - TOP_SOURCE_CROP[0], shared_origin[1] - TOP_SOURCE_CROP[1])
    draw_cross(top_draw, shifted_origin, (255, 0, 255), "origin", 7)
    for record in records:
        color = COLORS[str(record["stable_component_id"])]
        points = [
            (int(sample["rounded_perimeter_point_px"][0]) - TOP_SOURCE_CROP[0], int(sample["rounded_perimeter_point_px"][1]) - TOP_SOURCE_CROP[1])  # type: ignore[index]
            for sample in record["radial_perimeter_samples"]  # type: ignore[index]
        ]
        top_draw.line(points + [points[0]], fill=color, width=2)
        for point in points[::2]:
            top_draw.line((shifted_origin[0], shifted_origin[1], point[0], point[1]), fill=(245, 206, 35), width=1)
        cx, cy = record["calculated_footprint_center_px"]  # type: ignore[misc]
        draw_cross(top_draw, (float(cx) - TOP_SOURCE_CROP[0], float(cy) - TOP_SOURCE_CROP[1]), color, str(record["stable_component_id"]), 7)
    top_panel = top_panel.resize((664, 760), RESAMPLE_LANCZOS)
    board.paste(top_panel, (40, 130))
    draw.rectangle((40, 130, 704, 890), outline=(70, 64, 56), width=2)
    draw.text((40, 908), "Top source with radial contours and centers", fill=(32, 28, 24), font=font(20))

    for index, record in enumerate(records):
        mask = Image.open(ROOT / record["filled_contour_mask_path"]).convert("L")  # type: ignore[arg-type]
        preview = Image.new("RGB", source.size, (16, 16, 16))
        color = COLORS[str(record["stable_component_id"])]
        preview.paste(color, mask=mask)
        crop = preview.crop(TOP_SOURCE_CROP).resize((332, 380), RESAMPLE_NEAREST)
        col = index % 2
        row = index // 2
        x = 760 + col * 510
        y = 130 + row * 500
        board.paste(crop, (x, y))
        draw.rectangle((x, y, x + crop.width, y + crop.height), outline=(70, 64, 56), width=2)
        draw.text((x, y + 396), str(record["stable_component_id"]), fill=(32, 28, 24), font=font(19))
        draw.text((x, y + 426), f"center: {record['calculated_footprint_center_px']}", fill=(58, 52, 46), font=font(16))
        draw.text((x, y + 452), f"delta: {record['center_delta_from_shared_origin_px']}", fill=(58, 52, 46), font=font(16))
        draw.text((x, y + 478), f"pixels: {record['filled_contour_pixel_count']}", fill=(58, 52, 46), font=font(16))

    x, y = 40, 960
    draw.rectangle((x, y, 1760, 1300), fill=(255, 255, 255), outline=(75, 68, 62), width=2)
    draw.text((x + 18, y + 18), "Rules Enforced", fill=(24, 21, 18), font=font(22))
    rules = [
        f"Shared origin: {[round(shared_origin[0], 4), round(shared_origin[1], 4)]}",
        f"Ray count: {RAY_COUNT}; angle step: {ANGLE_STEP_DEG} degrees.",
        "Contours use reviewed perimeter points; no perfect-circle assumption.",
        "Shared origin is an assembly reference; each component center is recalculated after fill.",
        "Upper/base top envelopes are marked shared/occluded where layers overlap.",
        "No mesh, UVs, source-pixel edits, movement, rotation, centering, or assembly.",
    ]
    for i, rule in enumerate(rules):
        draw.text((x + 18, y + 58 + i * 36), f"- {rule}", fill=(48, 42, 36), font=font(17))

    board.save(RADIAL_REVIEW_BOARD)


def build_manifest(
    restart: dict[str, object],
    orientation: dict[str, object],
    formula: dict[str, object],
    centers: dict[str, object],
    snap: dict[str, object],
    contours: dict[str, object],
    shared_origin: tuple[float, float],
    records: list[dict[str, object]],
) -> dict[str, object]:
    return {
        "asset": ASSET_NAME,
        "status": "A001 shared-origin radial perimeter trace evidence recorded before geometry",
        "source": str(SOURCE.relative_to(ROOT)),
        "source_sha256": sha256_file(SOURCE),
        "source_scanline_manifest": str(RESTART_MANIFEST.relative_to(ROOT)),
        "orientation_pixel_manifest": str(ORIENTATION_MANIFEST.relative_to(ROOT)),
        "measurement_formula_manifest": str(FORMULA_MANIFEST.relative_to(ROOT)),
        "pixel_count_center_manifest": str(CENTER_MANIFEST.relative_to(ROOT)),
        "snap_anchor_manifest": str(SNAP_MANIFEST.relative_to(ROOT)),
        "layer_contour_manifest": str(CONTOUR_MANIFEST.relative_to(ROOT)),
        "radial_trace_overlay": str(RADIAL_OVERLAY.relative_to(ROOT)),
        "radial_trace_review_board": str(RADIAL_REVIEW_BOARD.relative_to(ROOT)),
        "source_proof": {
            "restart_pixel_exact": restart.get("pixel_exact"),
            "restart_changed_pixels": restart.get("changed_pixels"),
            "restart_max_rgb_delta": restart.get("max_rgb_delta"),
            "orientation_mark_count": len(orientation.get("markers", [])) if isinstance(orientation.get("markers"), list) else None,
            "formula_status": formula.get("status"),
            "center_status": centers.get("status"),
            "snap_status": snap.get("status"),
            "contour_status": contours.get("status"),
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
        "shared_origin_policy": {
            "shared_origin_px": [round(shared_origin[0], 4), round(shared_origin[1], 4)],
            "shared_origin_source": "assembled_top_footprint_review_only center from pixel-count center manifest",
            "shared_origin_is_snap_axis_candidate": True,
            "shared_origin_is_not_forced_component_center": True,
        },
        "radial_trace_formula": {
            "ray_count": RAY_COUNT,
            "angle_step_deg": ANGLE_STEP_DEG,
            "perimeter": "ray intersections against reviewed perimeter control polygon",
            "fill": "polygon fill from rounded radial perimeter samples",
            "center": "centroid of filled radial contour pixels",
            "not_used": [
                "perfect-circle assumption",
                "left/right radius only",
                "source-sheet labels or dimensions as perimeter stops",
                "forced recentering to shared origin",
            ],
        },
        "radial_trace_records": records,
        "geometry_use_status": "candidate_pending_review; blocked_until_formula_archive_update_contact_interface_and_pre_geometry_audit",
        "blocked_until_declared_next": [
            "review radial trace board",
            "approve or revise radial perimeter control points",
            "decide whether radial traces supersede prior contour evidence",
            "surface-angle marker pass",
            "contact-interface measurement pass",
            "formula archive update",
        ],
    }


def main() -> None:
    restart, orientation, formula, centers, snap, contours = verify_preconditions()
    source = Image.open(SOURCE).convert("RGB")
    RADIAL_DIR.mkdir(parents=True, exist_ok=True)
    shared_origin = shared_origin_from_centers(centers)
    records = [
        measure_radial_component(source.size, shared_origin, stable_component_id, spec)
        for stable_component_id, spec in RADIAL_COMPONENTS.items()
    ]
    create_overlay(source, shared_origin, records)
    create_review_board(source, shared_origin, records)
    manifest = build_manifest(restart, orientation, formula, centers, snap, contours, shared_origin, records)
    RADIAL_MANIFEST.write_text(json.dumps(manifest, indent=2) + "\n")
    print(f"A001 radial trace manifest: {RADIAL_MANIFEST}")
    print(f"A001 radial trace overlay: {RADIAL_OVERLAY}")
    print(f"A001 radial trace review board: {RADIAL_REVIEW_BOARD}")
    for record in records:
        print(
            f"{record['stable_component_id']}: center={record['calculated_footprint_center_px']} "
            f"delta={record['center_delta_from_shared_origin_px']} pixels={record['filled_contour_pixel_count']}"
        )
    print("geometry_generated=False components_moved=False components_assembled=False")


if __name__ == "__main__":
    main()
