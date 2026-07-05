#!/usr/bin/env python3
"""Measure A001 top-view pixel-count centers before assembly.

This evidence pass counts source-owned pixels inside declared component windows.
It produces review masks and center markers only. It does not generate mesh,
move components, assemble components, infer geometry, or alter source pixels.
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
CENTER_DIR = OUT_DIR / "FreshEvidence" / "PixelCountCenters"
RESTART_MANIFEST = OUT_DIR / f"{ASSET_NAME}_A001BlueprintRestartManifest.json"
ORIENTATION_MANIFEST = OUT_DIR / f"{ASSET_NAME}_A001OrientationPixelManifest.json"
FORMULA_MANIFEST = OUT_DIR / f"{ASSET_NAME}_A001MeasurementFormulaManifest.json"
CENTER_MANIFEST = OUT_DIR / f"{ASSET_NAME}_A001PixelCountCenterManifest.json"
CENTER_OVERLAY = OUT_DIR / f"{ASSET_NAME}_A001PixelCountCenterOverlay.png"
CENTER_REVIEW_BOARD = OUT_DIR / f"{ASSET_NAME}_A001PixelCountCenterReviewBoard.png"


REFERENCE_CENTER = (550.0, 1238.0)


COMPONENTS = {
    "primary_monolith_footprint": {
        "stable_component_id": "primary_monolith",
        "source_view": "top",
        "window_px": (454, 1142, 662, 1336),
        "seed_px": (550, 1238),
        "reviewed_perimeter_points_px": [
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
        "reviewed_perimeter_replaces_seed_mask": True,
        "rejected_seed_mask_reason": "seed-connected source mask clipped/undercounted the true primary monolith right/lower edge because pale edge pixels and artifacts failed the object-pixel test",
        "color": (228, 42, 42),
        "reuse_role": "standalone_or_assembly_component",
        "world_meaning": "top-view filled footprint for the main vertical stone",
    },
    "upper_socket_ring_outer_footprint": {
        "stable_component_id": "upper_socket_ring",
        "source_view": "top",
        "window_px": (423, 1117, 648, 1358),
        "seed_px": (500, 1125),
        "color": (255, 138, 30),
        "reuse_role": "standalone_or_assembly_component",
        "world_meaning": "top-view outer footprint candidate for the upper socket/ring layer",
    },
    "support_base_outer_footprint": {
        "stable_component_id": "support_base",
        "source_view": "top",
        "window_px": (413, 1114, 648, 1358),
        "seed_px": (500, 1125),
        "color": (0, 185, 255),
        "reuse_role": "standalone_or_assembly_component",
        "world_meaning": "top-view outer footprint for the full support/base layer",
    },
    "full_top_assembly_footprint": {
        "stable_component_id": "assembled_top_footprint_review_only",
        "source_view": "top",
        "window_px": (413, 1114, 648, 1358),
        "seed_px": (500, 1125),
        "color": (205, 80, 255),
        "reuse_role": "review_only_not_a_separate_export",
        "world_meaning": "top-view filled assembly footprint for comparison only",
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


def verify_preconditions() -> tuple[dict[str, object], dict[str, object], dict[str, object]]:
    for path in (RESTART_MANIFEST, ORIENTATION_MANIFEST, FORMULA_MANIFEST):
        if not path.exists():
            raise SystemExit(f"Missing required precondition manifest: {path}")

    restart = read_json(RESTART_MANIFEST)
    orientation = read_json(ORIENTATION_MANIFEST)
    formula = read_json(FORMULA_MANIFEST)

    if restart.get("pixel_exact") is not True or restart.get("changed_pixels") != 0 or restart.get("max_rgb_delta") != 0:
        raise SystemExit("A001 source scanline proof is not exact; pixel-count centers are blocked.")

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

    pre_geometry_state = formula.get("pre_geometry_state")
    if not isinstance(pre_geometry_state, dict):
        raise SystemExit("Formula manifest is missing pre_geometry_state.")
    blocking_states = [
        "geometry_generated",
        "uvs_generated",
        "components_moved",
        "components_rotated",
        "components_centered",
        "components_assembled",
        "inferred_fill_generated",
    ]
    failed = [key for key in blocking_states if pre_geometry_state.get(key) is not False]
    if failed:
        raise SystemExit(f"Formula manifest is no longer pre-geometry clean: {failed}")

    return restart, orientation, formula


def is_source_owned_object_pixel(rgb: tuple[int, int, int]) -> bool:
    r, g, b = rgb
    max_channel = max(r, g, b)
    min_channel = min(r, g, b)
    if r > 235 and g > 235 and b > 235 and (max_channel - min_channel) < 18:
        return False
    if r > 246 and g > 246 and b > 246:
        return False
    return True


def collect_raw_pixels(image: Image.Image, window: tuple[int, int, int, int]) -> set[tuple[int, int]]:
    left, top, right, bottom = window
    pixels = image.load()
    owned: set[tuple[int, int]] = set()
    for y in range(top, bottom):
        for x in range(left, right):
            if is_source_owned_object_pixel(pixels[x, y]):
                owned.add((x, y))
    return owned


def connected_object_pixels(
    image: Image.Image,
    window: tuple[int, int, int, int],
    seed: tuple[int, int],
) -> set[tuple[int, int]]:
    left, top, right, bottom = window
    seed_x, seed_y = seed
    if not (left <= seed_x < right and top <= seed_y < bottom):
        raise SystemExit(f"Seed pixel {seed} is outside declared source window {window}")

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


def fill_row_spans(raw_pixels: set[tuple[int, int]], window: tuple[int, int, int, int]) -> set[tuple[int, int]]:
    left, top, right, bottom = window
    by_row: dict[int, list[int]] = {}
    for x, y in raw_pixels:
        by_row.setdefault(y, []).append(x)

    filled: set[tuple[int, int]] = set()
    min_pixels_per_row = 4
    for y in range(top, bottom):
        xs = by_row.get(y, [])
        if len(xs) < min_pixels_per_row:
            continue
        row_left = max(left, min(xs))
        row_right = min(right - 1, max(xs))
        for x in range(row_left, row_right + 1):
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


def save_mask(source_size: tuple[int, int], pixels: set[tuple[int, int]], path: Path) -> None:
    mask = Image.new("L", source_size, 0)
    mask_pixels = mask.load()
    for x, y in pixels:
        mask_pixels[x, y] = 255
    mask.save(path)


def centroid(pixels: set[tuple[int, int]]) -> tuple[float, float]:
    count = len(pixels)
    return sum(x for x, _ in pixels) / count, sum(y for _, y in pixels) / count


def measure_pixels(name: str, spec: dict[str, object], source: Image.Image) -> dict[str, object]:
    window = tuple(spec["window_px"])  # type: ignore[arg-type]
    seed = tuple(spec["seed_px"])  # type: ignore[arg-type]
    raw_window_pixels = collect_raw_pixels(source, window)
    raw_pixels = connected_object_pixels(source, window, seed)
    seed_filled_pixels = fill_row_spans(raw_pixels, window)
    reviewed_points = spec.get("reviewed_perimeter_points_px")
    if reviewed_points:
        reviewed_perimeter_points = [(int(x), int(y)) for x, y in reviewed_points]  # type: ignore[misc]
        filled_pixels = polygon_pixels(source.size, reviewed_perimeter_points)
        final_center_type = "reviewed_source_owned_perimeter_filled_footprint_center"
    else:
        reviewed_perimeter_points = []
        filled_pixels = seed_filled_pixels
        final_center_type = "seed_connected_filled_row_span_footprint_center"

    if not raw_window_pixels:
        raise SystemExit(f"No raw source pixels counted for {name}")
    if not raw_pixels:
        raise SystemExit(f"No object row-run pixels selected for {name}")
    if not filled_pixels:
        raise SystemExit(f"No pixels counted for {name}")

    raw_center_x, raw_center_y = centroid(raw_pixels)
    center_x, center_y = centroid(filled_pixels)
    xs = [x for x, _ in filled_pixels]
    ys = [y for _, y in filled_pixels]
    delta_x = center_x - REFERENCE_CENTER[0]
    delta_y = center_y - REFERENCE_CENTER[1]
    distance = (delta_x * delta_x + delta_y * delta_y) ** 0.5

    raw_mask_path = CENTER_DIR / f"{ASSET_NAME}_{name}_RawSourceOwnedPixelMask.png"
    filled_mask_path = CENTER_DIR / f"{ASSET_NAME}_{name}_FilledFootprintCenterMask.png"
    rejected_seed_filled_mask_path = CENTER_DIR / f"{ASSET_NAME}_{name}_RejectedSeedConnectedFilledFootprintMask.png"
    save_mask(source.size, raw_pixels, raw_mask_path)
    save_mask(source.size, filled_pixels, filled_mask_path)
    save_mask(source.size, seed_filled_pixels, rejected_seed_filled_mask_path)

    result = {
        "component_name": name,
        "stable_component_id": spec["stable_component_id"],
        "source_file": str(SOURCE.relative_to(ROOT)),
        "source_sha256": sha256_file(SOURCE),
        "source_scanline_manifest": str(RESTART_MANIFEST.relative_to(ROOT)),
        "source_view": spec["source_view"],
        "world_meaning": spec["world_meaning"],
        "reuse_role": spec["reuse_role"],
        "window_px": list(spec["window_px"]),
        "seed_px": list(spec["seed_px"]),
        "raw_source_owned_pixel_count": len(raw_pixels),
        "raw_window_source_pixel_count": len(raw_window_pixels),
        "annotation_excluded_pixel_count": len(raw_window_pixels) - len(raw_pixels),
        "raw_visible_pixel_center": [round(raw_center_x, 4), round(raw_center_y, 4)],
        "filled_footprint_pixel_count": len(filled_pixels),
        "pixel_count_center": [round(center_x, 4), round(center_y, 4)],
        "alignment_center_type": final_center_type,
        "rounded_pixel_count_center": [round(center_x), round(center_y)],
        "source_owned_pixel_bounds": [min(xs), min(ys), max(xs) + 1, max(ys) + 1],
        "comparison_reference_center": [REFERENCE_CENTER[0], REFERENCE_CENTER[1]],
        "delta_from_reference_center_px": [round(delta_x, 4), round(delta_y, 4)],
        "distance_from_reference_center_px": round(distance, 4),
        "raw_mask_path": str(raw_mask_path.relative_to(ROOT)),
        "filled_footprint_mask_path": str(filled_mask_path.relative_to(ROOT)),
        "rejected_seed_connected_filled_mask_path": str(rejected_seed_filled_mask_path.relative_to(ROOT)),
        "mask_is_geometry_authority": False,
        "center_is_alignment_candidate": True,
        "selection_method": "declared top-view object-only source window plus declared seed pixel; count non-background source pixels; keep only source-owned pixels connected to the seed; if seed mask visibly clips true silhouette, replace with reviewed source-owned perimeter polygon; center is the final filled footprint centroid",
        "geometry_generated": False,
        "components_moved": False,
        "components_assembled": False,
        "visible_texture_modified": False,
        "color_rgb": list(spec["color"]),
    }
    if reviewed_perimeter_points:
        result["reviewed_perimeter_points_px"] = [list(point) for point in reviewed_perimeter_points]
        result["reviewed_perimeter_replaces_seed_mask"] = bool(spec.get("reviewed_perimeter_replaces_seed_mask"))
        result["rejected_seed_mask_reason"] = spec.get("rejected_seed_mask_reason")
        result["rejected_seed_connected_center"] = [
            round(sum(x for x, _ in seed_filled_pixels) / len(seed_filled_pixels), 4),
            round(sum(y for _, y in seed_filled_pixels) / len(seed_filled_pixels), 4),
        ]
        result["rejected_seed_connected_pixel_count"] = len(seed_filled_pixels)
    return result


def draw_cross(draw: ImageDraw.ImageDraw, xy: tuple[float, float], color: tuple[int, int, int], label: str, radius: int = 10) -> None:
    x = round(xy[0])
    y = round(xy[1])
    draw.line((x - radius, y, x + radius, y), fill=color, width=3)
    draw.line((x, y - radius, x, y + radius), fill=color, width=3)
    draw.ellipse((x - radius, y - radius, x + radius, y + radius), outline=color, width=2)
    draw.text((x + 12, y - 10), label, fill=color, font=font(12))


def draw_window(draw: ImageDraw.ImageDraw, window: list[int] | tuple[int, int, int, int], color: tuple[int, int, int], label: str) -> None:
    left, top, right, bottom = window
    draw.rectangle((left, top, right, bottom), outline=color, width=2)
    draw.text((left + 4, top + 4), label, fill=color, font=font(12))


def create_overlay(source: Image.Image, results: list[dict[str, object]]) -> None:
    overlay = source.copy()
    draw = ImageDraw.Draw(overlay)
    draw.rectangle((10, 10, 1045, 84), fill=(255, 255, 255), outline=(30, 30, 30), width=2)
    draw.text((24, 18), "A001 pixel-count centers - source-owned pixels, no geometry generated", fill=(20, 18, 16), font=font(20))
    draw.text((24, 48), "Bounding-box/shared center is comparison only. Component centers below must drive alignment after approval.", fill=(65, 42, 35), font=font(15))
    draw_cross(draw, REFERENCE_CENTER, (20, 20, 20), "old shared review center", 8)
    for result in results:
        color = tuple(result["color_rgb"])  # type: ignore[arg-type]
        draw_window(draw, result["window_px"], color, str(result["component_name"]))
        center = result["pixel_count_center"]
        draw_cross(draw, (float(center[0]), float(center[1])), color, str(result["stable_component_id"]))
    overlay.save(CENTER_OVERLAY)


def create_review_board(source: Image.Image, results: list[dict[str, object]]) -> None:
    board = Image.new("RGB", (1800, 1280), (245, 243, 238))
    draw = ImageDraw.Draw(board)
    draw.text((40, 28), "A001 Pixel-Count Center Review", fill=(24, 21, 18), font=font(30))
    draw.text((40, 76), "Masks show counted source-owned pixels. These are center evidence only until approved.", fill=(55, 48, 42), font=font(18))

    source_crop = (392, 1070, 724, 1450)
    top_panel = source.crop(source_crop).copy()
    panel_draw = ImageDraw.Draw(top_panel)
    for result in results:
        color = tuple(result["color_rgb"])  # type: ignore[arg-type]
        center = result["pixel_count_center"]
        shifted_center = (float(center[0]) - source_crop[0], float(center[1]) - source_crop[1])
        shifted_window = [
            result["window_px"][0] - source_crop[0],  # type: ignore[index]
            result["window_px"][1] - source_crop[1],  # type: ignore[index]
            result["window_px"][2] - source_crop[0],  # type: ignore[index]
            result["window_px"][3] - source_crop[1],  # type: ignore[index]
        ]
        draw_window(panel_draw, shifted_window, color, str(result["component_name"]))
        draw_cross(panel_draw, shifted_center, color, str(result["stable_component_id"]), 8)
    top_panel = top_panel.resize((664, 760), RESAMPLE_LANCZOS)
    board.paste(top_panel, (40, 130))
    draw.rectangle((40, 130, 704, 890), outline=(70, 64, 56), width=2)
    draw.text((40, 908), "Top-view center overlay", fill=(32, 28, 24), font=font(20))

    for index, result in enumerate(results):
        mask = Image.open(ROOT / result["filled_footprint_mask_path"]).convert("L")  # type: ignore[arg-type]
        preview = Image.new("RGB", source.size, (16, 16, 16))
        color = tuple(result["color_rgb"])  # type: ignore[arg-type]
        preview.paste(color, mask=mask)
        crop = preview.crop(source_crop)
        crop = crop.resize((332, 380), RESAMPLE_NEAREST)
        col = index % 2
        row = index // 2
        x = 760 + col * 500
        y = 130 + row * 500
        board.paste(crop, (x, y))
        draw.rectangle((x, y, x + crop.width, y + crop.height), outline=(70, 64, 56), width=2)
        draw.text((x, y + 396), str(result["component_name"]), fill=(32, 28, 24), font=font(19))
        draw.text((x, y + 426), f"filled count: {result['filled_footprint_pixel_count']}", fill=(58, 52, 46), font=font(16))
        draw.text((x, y + 452), f"center: {result['pixel_count_center']}", fill=(58, 52, 46), font=font(16))
        draw.text((x, y + 478), f"delta: {result['delta_from_reference_center_px']}", fill=(58, 52, 46), font=font(16))

    board.save(CENTER_REVIEW_BOARD)


def build_manifest(
    restart: dict[str, object],
    orientation: dict[str, object],
    formula: dict[str, object],
    results: list[dict[str, object]],
) -> dict[str, object]:
    max_distance = max(float(item["distance_from_reference_center_px"]) for item in results)
    return {
        "asset": ASSET_NAME,
        "status": "A001 pixel-count centers recorded before component movement or assembly",
        "source": str(SOURCE.relative_to(ROOT)),
        "source_sha256": sha256_file(SOURCE),
        "source_scanline_manifest": str(RESTART_MANIFEST.relative_to(ROOT)),
        "orientation_pixel_manifest": str(ORIENTATION_MANIFEST.relative_to(ROOT)),
        "measurement_formula_manifest": str(FORMULA_MANIFEST.relative_to(ROOT)),
        "pixel_count_center_overlay": str(CENTER_OVERLAY.relative_to(ROOT)),
        "pixel_count_center_review_board": str(CENTER_REVIEW_BOARD.relative_to(ROOT)),
        "blueprint_steps_completed": [
            "Approved Source Intake",
            "Lossless Scanline Capture",
            "Registration Marks - source orientation pixels",
            "Pixel-Count Center Rule - top-view source-owned pixel centers",
        ],
        "source_proof": {
            "restart_pixel_exact": restart.get("pixel_exact"),
            "restart_changed_pixels": restart.get("changed_pixels"),
            "restart_max_rgb_delta": restart.get("max_rgb_delta"),
            "orientation_mark_count": len(orientation.get("markers", [])) if isinstance(orientation.get("markers"), list) else None,
            "formula_status": formula.get("status"),
        },
        "reference_center_policy": {
            "old_shared_center": [REFERENCE_CENTER[0], REFERENCE_CENTER[1]],
            "old_shared_center_is_geometry_authority": False,
            "old_shared_center_is_alignment_authority": False,
            "use": "comparison marker only",
        },
        "pixel_ownership_formula": {
            "source_window": "declared per component in full source pixel coordinates",
            "included_pixel": "pixel inside declared component window and not light source-sheet background",
            "background_rejection": "r>235 and g>235 and b>235 and channel range<18, or r/g/b all >246",
            "annotation_exclusion": "tight object-only windows exclude source-sheet labels, arrows, dimension text, borders, and unrelated artwork from center authority",
            "raw_visible_center": "recorded as diagnostic only because cracks, symbols, shadows, and highlights bias color-density center",
            "filled_footprint_center": "for each counted row, fill from first source-owned pixel to last source-owned pixel; center_x=sum(filled_x)/count; center_y=sum(filled_y)/count",
            "reviewed_perimeter_replacement": "if seed-connected evidence visibly clips a true source edge, reviewed perimeter points replace the seed mask for that component and the rejected seed mask remains archived",
            "not_used": [
                "bounding-box center as final authority",
                "averaged center",
                "largest-blob reshape",
                "smoothing",
                "dilation",
                "erosion",
                "post-fit movement",
            ],
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
        "component_centers": results,
        "max_distance_from_old_shared_center_px": round(max_distance, 4),
        "geometry_use_status": "review_required_before_alignment_or_snap_anchor_authority",
        "blocked_until_declared_next": [
            "review pixel-count center masks",
            "approve component center authority or revise source-owned pixel windows",
            "update snap anchors to reference approved component centers",
            "replace rectangular top support ownership with source-owned contour/mask ownership before geometry",
        ],
    }


def main() -> None:
    restart, orientation, formula = verify_preconditions()
    source = Image.open(SOURCE).convert("RGB")
    CENTER_DIR.mkdir(parents=True, exist_ok=True)
    results: list[dict[str, object]] = []

    for name, spec in COMPONENTS.items():
        result = measure_pixels(name, spec, source)
        results.append(result)

    create_overlay(source, results)
    create_review_board(source, results)
    manifest = build_manifest(restart, orientation, formula, results)
    CENTER_MANIFEST.write_text(json.dumps(manifest, indent=2) + "\n")

    print(f"A001 pixel-count center manifest: {CENTER_MANIFEST}")
    print(f"A001 pixel-count center overlay: {CENTER_OVERLAY}")
    print(f"A001 pixel-count center review board: {CENTER_REVIEW_BOARD}")
    for result in results:
        print(f"{result['component_name']}: filled_count={result['filled_footprint_pixel_count']} center={result['pixel_count_center']} raw_center={result['raw_visible_pixel_center']} delta={result['delta_from_reference_center_px']}")
    print("geometry_generated=False components_moved=False components_assembled=False")


if __name__ == "__main__":
    main()
