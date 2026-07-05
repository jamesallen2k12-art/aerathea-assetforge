#!/usr/bin/env python3
"""Measure A001 source component contours and layer separation evidence.

This pass records contour/perimeter and layer-separation evidence only. It does
not generate mesh data, UVs, texture edits, inferred fill, or assembled parts.
"""

from __future__ import annotations

import hashlib
import json
from pathlib import Path

from PIL import Image, ImageDraw, ImageFont


ROOT = Path(__file__).resolve().parents[2]
ASSET_NAME = "SM_GIA_BloodAxeCairnstone_A001"
SOURCE = ROOT / "docs/assets/reference/bloodaxe_cairnstone_asset/REF_GIA_BloodAxeCairnstoneAsset_A02_BlueprintTemplate.png"
OUT_DIR = ROOT / "Saved/Automation/DCC" / ASSET_NAME
CONTOUR_DIR = OUT_DIR / "FreshEvidence" / "LayerContours"
RESTART_MANIFEST = OUT_DIR / f"{ASSET_NAME}_A001BlueprintRestartManifest.json"
ORIENTATION_MANIFEST = OUT_DIR / f"{ASSET_NAME}_A001OrientationPixelManifest.json"
FORMULA_MANIFEST = OUT_DIR / f"{ASSET_NAME}_A001MeasurementFormulaManifest.json"
CENTER_MANIFEST = OUT_DIR / f"{ASSET_NAME}_A001PixelCountCenterManifest.json"
SNAP_MANIFEST = OUT_DIR / f"{ASSET_NAME}_A001SnapAnchorManifest.json"
CONTOUR_MANIFEST = OUT_DIR / f"{ASSET_NAME}_A001LayerContourManifest.json"
CONTOUR_OVERLAY = OUT_DIR / f"{ASSET_NAME}_A001LayerContourOverlay.png"
CONTOUR_REVIEW_BOARD = OUT_DIR / f"{ASSET_NAME}_A001LayerContourReviewBoard.png"


TOP_SOURCE_CROP = (392, 1070, 724, 1450)


COLORS = {
    "primary_monolith": (228, 42, 42),
    "upper_socket_ring": (255, 138, 30),
    "support_base": (0, 185, 255),
    "assembled_top_footprint_review_only": (205, 80, 255),
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


def verify_preconditions() -> tuple[dict[str, object], dict[str, object], dict[str, object], dict[str, object], dict[str, object]]:
    for path in (RESTART_MANIFEST, ORIENTATION_MANIFEST, FORMULA_MANIFEST, CENTER_MANIFEST, SNAP_MANIFEST):
        if not path.exists():
            raise SystemExit(f"Missing required precondition manifest: {path}")

    restart = read_json(RESTART_MANIFEST)
    orientation = read_json(ORIENTATION_MANIFEST)
    formula = read_json(FORMULA_MANIFEST)
    centers = read_json(CENTER_MANIFEST)
    snap = read_json(SNAP_MANIFEST)

    if restart.get("pixel_exact") is not True or restart.get("changed_pixels") != 0 or restart.get("max_rgb_delta") != 0:
        raise SystemExit("A001 source scanline proof is not exact; contour pass is blocked.")

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
    for label, manifest in (("formula", formula), ("center", centers), ("snap", snap)):
        state = manifest.get("pre_geometry_state")
        if not isinstance(state, dict):
            raise SystemExit(f"{label} manifest is missing pre_geometry_state.")
        failed = [key for key in blocking_states if state.get(key) is not False]
        if failed:
            raise SystemExit(f"{label} manifest is no longer pre-geometry clean: {failed}")

    pair_validation = snap.get("paired_anchor_validation")
    if not isinstance(pair_validation, dict) or pair_validation.get("all_pairs_resolve") is not True:
        raise SystemExit("Snap anchor manifest does not have clean paired-anchor validation.")

    return restart, orientation, formula, centers, snap


def is_source_owned_object_pixel(rgb: tuple[int, int, int]) -> bool:
    r, g, b = rgb
    max_channel = max(r, g, b)
    min_channel = min(r, g, b)
    if r > 235 and g > 235 and b > 235 and (max_channel - min_channel) < 18:
        return False
    if r > 246 and g > 246 and b > 246:
        return False
    return True


def connected_object_pixels(
    image: Image.Image,
    window: tuple[int, int, int, int],
    seed: tuple[int, int],
) -> set[tuple[int, int]]:
    left, top, right, bottom = window
    seed_x, seed_y = seed
    if not (left <= seed_x < right and top <= seed_y < bottom):
        raise SystemExit(f"Seed pixel {seed} is outside source window {window}")

    image_pixels = image.load()
    if not is_source_owned_object_pixel(image_pixels[seed_x, seed_y]):
        raise SystemExit(f"Seed pixel {seed} is not source-owned object color: {image_pixels[seed_x, seed_y]}")

    connected = {(seed_x, seed_y)}
    stack = [(seed_x, seed_y)]
    while stack:
        x, y = stack.pop()
        for ny in (y - 1, y, y + 1):
            for nx in (x - 1, x, x + 1):
                if nx == x and ny == y:
                    continue
                if nx < left or nx >= right or ny < top or ny >= bottom:
                    continue
                if (nx, ny) in connected:
                    continue
                if is_source_owned_object_pixel(image_pixels[nx, ny]):
                    connected.add((nx, ny))
                    stack.append((nx, ny))
    return connected


def fill_row_spans(raw_pixels: set[tuple[int, int]]) -> set[tuple[int, int]]:
    by_row: dict[int, list[int]] = {}
    for x, y in raw_pixels:
        by_row.setdefault(y, []).append(x)

    filled: set[tuple[int, int]] = set()
    for y, xs in by_row.items():
        if len(xs) < 4:
            continue
        for x in range(min(xs), max(xs) + 1):
            filled.add((x, y))
    return filled


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


def save_mask(source_size: tuple[int, int], pixels: set[tuple[int, int]], path: Path) -> None:
    mask = Image.new("L", source_size, 0)
    mask_pixels = mask.load()
    for x, y in pixels:
        mask_pixels[x, y] = 255
    mask.save(path)


def component_center_records(centers: dict[str, object]) -> list[dict[str, object]]:
    records = []
    for item in centers.get("component_centers", []):
        if not isinstance(item, dict):
            continue
        stable_id = str(item.get("stable_component_id"))
        if stable_id == "assembled_top_footprint_review_only":
            stable_id = "assembled_top_footprint_review_only"
        if stable_id not in COLORS:
            continue
        records.append(item)
    return records


def measure_component_contour(source: Image.Image, item: dict[str, object]) -> dict[str, object]:
    stable_id = str(item["stable_component_id"])
    component_name = str(item["component_name"])
    window = tuple(item["window_px"])  # type: ignore[arg-type]
    seed = tuple(item["seed_px"])  # type: ignore[arg-type]
    raw_pixels = connected_object_pixels(source, window, seed)
    rejected_seed_filled_pixels = fill_row_spans(raw_pixels)
    reviewed_points = item.get("reviewed_perimeter_points_px")
    if reviewed_points:
        reviewed_perimeter_points = [(int(x), int(y)) for x, y in reviewed_points]  # type: ignore[misc]
        filled_pixels = polygon_pixels(source.size, reviewed_perimeter_points)
        contour_source_method = "reviewed_source_owned_perimeter_points"
        geometry_status = "candidate_pending_reviewed_perimeter_approval_and_formula_archive_update"
    else:
        reviewed_perimeter_points = []
        filled_pixels = rejected_seed_filled_pixels
        contour_source_method = "seed_connected_source_pixels_plus_filled_row_span"
        geometry_status = "candidate_pending_review_and_formula_archive_update"
    contour = contour_pixels(filled_pixels)
    if not contour:
        raise SystemExit(f"No contour pixels for {component_name}")

    raw_path = CONTOUR_DIR / f"{ASSET_NAME}_{component_name}_ConnectedRawMask.png"
    filled_path = CONTOUR_DIR / f"{ASSET_NAME}_{component_name}_FilledFootprintMask.png"
    contour_path = CONTOUR_DIR / f"{ASSET_NAME}_{component_name}_PerimeterContourMask.png"
    rejected_path = CONTOUR_DIR / f"{ASSET_NAME}_{component_name}_RejectedSeedConnectedFilledFootprintMask.png"
    save_mask(source.size, raw_pixels, raw_path)
    save_mask(source.size, filled_pixels, filled_path)
    save_mask(source.size, contour, contour_path)
    save_mask(source.size, rejected_seed_filled_pixels, rejected_path)

    xs = [x for x, _ in filled_pixels]
    ys = [y for _, y in filled_pixels]
    cx, cy = item["pixel_count_center"]  # type: ignore[misc]
    row_spans: dict[str, object] = {}
    for label, y_value in (
        ("top_quarter", round(min(ys) + (max(ys) - min(ys)) * 0.25)),
        ("center", round(float(cy))),
        ("bottom_quarter", round(min(ys) + (max(ys) - min(ys)) * 0.75)),
    ):
        row_xs = [x for x, y in filled_pixels if y == y_value]
        if row_xs:
            row_spans[label] = {
                "y_px": y_value,
                "left_px": min(row_xs),
                "right_px": max(row_xs),
                "span_px": max(row_xs) - min(row_xs) + 1,
            }

    return {
        "stable_component_id": stable_id,
        "component_name": component_name,
        "source_view": "top",
        "source_file": str(SOURCE.relative_to(ROOT)),
        "source_sha256": sha256_file(SOURCE),
        "source_scanline_manifest": str(RESTART_MANIFEST.relative_to(ROOT)),
        "pixel_count_center_manifest": str(CENTER_MANIFEST.relative_to(ROOT)),
        "window_px": list(window),
        "seed_px": list(seed),
        "pixel_count_center": item["pixel_count_center"],
        "rounded_pixel_count_center": item["rounded_pixel_count_center"],
        "center_type": item["alignment_center_type"],
        "raw_connected_pixel_count": len(raw_pixels),
        "filled_footprint_pixel_count": len(filled_pixels),
        "perimeter_pixel_count": len(contour),
        "filled_footprint_bounds_px": [min(xs), min(ys), max(xs) + 1, max(ys) + 1],
        "row_spans_px": row_spans,
        "connected_raw_mask_path": str(raw_path.relative_to(ROOT)),
        "filled_footprint_mask_path": str(filled_path.relative_to(ROOT)),
        "perimeter_contour_mask_path": str(contour_path.relative_to(ROOT)),
        "rejected_seed_connected_filled_mask_path": str(rejected_path.relative_to(ROOT)),
        "reusable_source_component": stable_id != "assembled_top_footprint_review_only",
        "geometry_authority_status": geometry_status,
        "contour_source_method": contour_source_method,
        "source_component_role": item["reuse_role"],
        "no_geometry_generated": True,
        "components_moved": False,
        "components_assembled": False,
    }
    if reviewed_perimeter_points:
        record["reviewed_perimeter_points_px"] = [list(point) for point in reviewed_perimeter_points]
        record["rejected_seed_mask_reason"] = item.get("rejected_seed_mask_reason")
        record["rejected_seed_connected_center"] = item.get("rejected_seed_connected_center")
        record["rejected_seed_connected_pixel_count"] = item.get("rejected_seed_connected_pixel_count")
    return record


def extract_layer_contact_records(snap: dict[str, object]) -> list[dict[str, object]]:
    records = []
    for anchor in snap.get("snap_anchors", []):
        if not isinstance(anchor, dict) or "pixel_line" not in anchor:
            continue
        anchor_id = str(anchor["anchor_id"])
        if "_TO_" not in anchor_id:
            continue
        records.append(
            {
                "anchor_id": anchor_id,
                "paired_anchor_id": anchor.get("paired_anchor_id"),
                "source_view": anchor.get("source_view"),
                "physical_layer_component": anchor.get("physical_layer_component"),
                "snap_role": anchor.get("snap_role"),
                "pixel_line": anchor.get("pixel_line"),
                "world_space_meaning": anchor.get("world_space_meaning"),
                "source": "A001 snap anchor manifest",
                "geometry_authority_status": "candidate_pending_contact_interface_review",
            }
        )
    return records


def draw_cross(draw: ImageDraw.ImageDraw, xy: tuple[float, float], color: tuple[int, int, int], label: str, radius: int = 8) -> None:
    x = round(xy[0])
    y = round(xy[1])
    draw.line((x - radius, y, x + radius, y), fill=color, width=3)
    draw.line((x, y - radius, x, y + radius), fill=color, width=3)
    draw.ellipse((x - radius, y - radius, x + radius, y + radius), outline=color, width=2)
    draw.text((x + 10, y - 9), label, fill=color, font=font(11))


def draw_contour(draw: ImageDraw.ImageDraw, pixels: set[tuple[int, int]], color: tuple[int, int, int]) -> None:
    for x, y in pixels:
        draw.point((x, y), fill=color)


def create_overlay(source: Image.Image, contour_records: list[dict[str, object]]) -> None:
    overlay = source.copy()
    draw = ImageDraw.Draw(overlay)
    draw.rectangle((10, 10, 1045, 88), fill=(255, 255, 255), outline=(30, 30, 30), width=2)
    draw.text((24, 18), "A001 layer contours - seed-connected source evidence, no geometry generated", fill=(20, 18, 16), font=font(20))
    draw.text((24, 50), "Rectangular top-support formula is blocked for geometry; contour evidence is pending review.", fill=(80, 42, 92), font=font(15))

    for record in contour_records:
        stable_id = str(record["stable_component_id"])
        color = COLORS[stable_id]
        mask = Image.open(ROOT / record["perimeter_contour_mask_path"]).convert("L")  # type: ignore[arg-type]
        mask_pixels = mask.load()
        contour = {
            (x, y)
            for y in range(mask.height)
            for x in range(mask.width)
            if mask_pixels[x, y] > 0
        }
        draw_contour(draw, contour, color)
        cx, cy = record["pixel_count_center"]  # type: ignore[misc]
        draw_cross(draw, (float(cx), float(cy)), color, stable_id)
    overlay.save(CONTOUR_OVERLAY)


def create_review_board(source: Image.Image, contour_records: list[dict[str, object]], contact_records: list[dict[str, object]]) -> None:
    board = Image.new("RGB", (1860, 1320), (245, 243, 238))
    draw = ImageDraw.Draw(board)
    draw.text((40, 28), "A001 Layer Contour And Separation Review", fill=(24, 21, 18), font=font(30))
    draw.text((40, 74), "Seed-connected component contours and side-view layer contact lines. Evidence only; no mesh generated.", fill=(55, 48, 42), font=font(18))

    top_panel = source.crop(TOP_SOURCE_CROP).copy()
    top_draw = ImageDraw.Draw(top_panel)
    for record in contour_records:
        stable_id = str(record["stable_component_id"])
        color = COLORS[stable_id]
        contour_mask = Image.open(ROOT / record["perimeter_contour_mask_path"]).convert("L")  # type: ignore[arg-type]
        mask_crop = contour_mask.crop(TOP_SOURCE_CROP)
        mask_pixels = mask_crop.load()
        for y in range(mask_crop.height):
            for x in range(mask_crop.width):
                if mask_pixels[x, y] > 0:
                    top_draw.point((x, y), fill=color)
        cx, cy = record["pixel_count_center"]  # type: ignore[misc]
        draw_cross(top_draw, (float(cx) - TOP_SOURCE_CROP[0], float(cy) - TOP_SOURCE_CROP[1]), color, stable_id)
    top_panel = top_panel.resize((664, 760), RESAMPLE_LANCZOS)
    board.paste(top_panel, (40, 130))
    draw.rectangle((40, 130, 704, 890), outline=(70, 64, 56), width=2)
    draw.text((40, 908), "Top contours and pixel-count centers", fill=(32, 28, 24), font=font(20))

    for index, record in enumerate(contour_records):
        fill_mask = Image.open(ROOT / record["filled_footprint_mask_path"]).convert("L")  # type: ignore[arg-type]
        preview = Image.new("RGB", source.size, (16, 16, 16))
        color = COLORS[str(record["stable_component_id"])]
        preview.paste(color, mask=fill_mask)
        crop = preview.crop(TOP_SOURCE_CROP).resize((332, 380), RESAMPLE_NEAREST)
        col = index % 2
        row = index // 2
        x = 760 + col * 500
        y = 130 + row * 500
        board.paste(crop, (x, y))
        draw.rectangle((x, y, x + crop.width, y + crop.height), outline=(70, 64, 56), width=2)
        draw.text((x, y + 396), str(record["stable_component_id"]), fill=(32, 28, 24), font=font(19))
        draw.text((x, y + 426), f"center: {record['pixel_count_center']}", fill=(58, 52, 46), font=font(16))
        draw.text((x, y + 452), f"perimeter px: {record['perimeter_pixel_count']}", fill=(58, 52, 46), font=font(16))
        draw.text((x, y + 478), f"bounds: {record['filled_footprint_bounds_px']}", fill=(58, 52, 46), font=font(16))

    side_text_x = 40
    side_text_y = 960
    draw.rectangle((side_text_x, side_text_y, 1720, 1260), fill=(255, 255, 255), outline=(75, 68, 62), width=2)
    draw.text((side_text_x + 18, side_text_y + 18), "Layer Separation Contact Lines", fill=(24, 21, 18), font=font(22))
    draw.text((side_text_x + 18, side_text_y + 58), f"line anchors recorded: {len(contact_records)}", fill=(48, 42, 36), font=font(17))
    draw.text((side_text_x + 18, side_text_y + 92), "These line anchors come from the snap-anchor manifest and remain evidence until contact-interface review.", fill=(48, 42, 36), font=font(17))
    rules = [
        "Rectangular top support box is not geometry authority.",
        "Seed-connected masks exclude detached labels and dimension marks.",
        "Asymmetric source centers remain valid if the measured footprint proves them.",
        "No component was moved, centered, rotated, assembled, or meshed.",
    ]
    for i, rule in enumerate(rules):
        draw.text((side_text_x + 18, side_text_y + 132 + i * 34), f"- {rule}", fill=(48, 42, 36), font=font(17))

    board.save(CONTOUR_REVIEW_BOARD)


def build_manifest(
    restart: dict[str, object],
    orientation: dict[str, object],
    formula: dict[str, object],
    centers: dict[str, object],
    snap: dict[str, object],
    contour_records: list[dict[str, object]],
    contact_records: list[dict[str, object]],
) -> dict[str, object]:
    return {
        "asset": ASSET_NAME,
        "status": "A001 layer contour and separation evidence recorded before geometry",
        "source": str(SOURCE.relative_to(ROOT)),
        "source_sha256": sha256_file(SOURCE),
        "source_scanline_manifest": str(RESTART_MANIFEST.relative_to(ROOT)),
        "orientation_pixel_manifest": str(ORIENTATION_MANIFEST.relative_to(ROOT)),
        "measurement_formula_manifest": str(FORMULA_MANIFEST.relative_to(ROOT)),
        "pixel_count_center_manifest": str(CENTER_MANIFEST.relative_to(ROOT)),
        "snap_anchor_manifest": str(SNAP_MANIFEST.relative_to(ROOT)),
        "layer_contour_overlay": str(CONTOUR_OVERLAY.relative_to(ROOT)),
        "layer_contour_review_board": str(CONTOUR_REVIEW_BOARD.relative_to(ROOT)),
        "source_proof": {
            "restart_pixel_exact": restart.get("pixel_exact"),
            "restart_changed_pixels": restart.get("changed_pixels"),
            "restart_max_rgb_delta": restart.get("max_rgb_delta"),
            "orientation_mark_count": len(orientation.get("markers", [])) if isinstance(orientation.get("markers"), list) else None,
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
        "rectangular_top_formula_status": {
            "prior_formula_manifest": str(FORMULA_MANIFEST.relative_to(ROOT)),
            "top_support_rectangular_box_is_geometry_authority": False,
            "status": "blocked_for_geometry_and_superseded_by_contour_evidence_after_review",
            "reason": "top-down support/base is oval, ring-like, irregular, and asymmetric; rectangular box is calibration/review only",
        },
        "contour_method": {
            "method": "seed-connected source pixels plus filled row-span footprint contour",
            "annotation_exclusion": "detached labels, arrows, dimension marks, borders, and unrelated artwork are excluded because they are not connected to the declared seed pixel inside the object window",
            "raw_visible_centers_are_diagnostic": True,
            "asymmetric_centers_allowed": True,
        },
        "reusable_source_components": [
            record
            for record in contour_records
            if record["stable_component_id"] != "assembled_top_footprint_review_only"
        ],
        "review_only_assembly_records": [
            record
            for record in contour_records
            if record["stable_component_id"] == "assembled_top_footprint_review_only"
        ],
        "layer_contact_line_records": contact_records,
        "geometry_use_status": "blocked_until_contour_review_surface_angle_edge_correspondence_contact_interface_and_formula_archive_pass",
        "blocked_until_declared_next": [
            "review layer contour board",
            "approve or revise contour masks",
            "surface-angle and edge-correspondence marker pass",
            "formal contact-interface measurement pass",
            "formula archive update that makes approved contours the geometry authority",
        ],
    }


def main() -> None:
    restart, orientation, formula, centers, snap = verify_preconditions()
    source = Image.open(SOURCE).convert("RGB")
    CONTOUR_DIR.mkdir(parents=True, exist_ok=True)
    center_records = component_center_records(centers)
    contour_records = [measure_component_contour(source, item) for item in center_records]
    contact_records = extract_layer_contact_records(snap)
    create_overlay(source, contour_records)
    create_review_board(source, contour_records, contact_records)
    manifest = build_manifest(restart, orientation, formula, centers, snap, contour_records, contact_records)
    CONTOUR_MANIFEST.write_text(json.dumps(manifest, indent=2) + "\n")
    print(f"A001 layer contour manifest: {CONTOUR_MANIFEST}")
    print(f"A001 layer contour overlay: {CONTOUR_OVERLAY}")
    print(f"A001 layer contour review board: {CONTOUR_REVIEW_BOARD}")
    for record in contour_records:
        print(
            f"{record['stable_component_id']}: center={record['pixel_count_center']} "
            f"bounds={record['filled_footprint_bounds_px']} perimeter={record['perimeter_pixel_count']}"
        )
    print(f"layer contact line records: {len(contact_records)}")
    print("geometry_generated=False components_moved=False components_assembled=False")


if __name__ == "__main__":
    main()
