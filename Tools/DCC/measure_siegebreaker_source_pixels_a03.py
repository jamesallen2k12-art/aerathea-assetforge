"""Measure the approved Siege Breaker concept without altering source pixels.

This is an evidence-only pass. It crops declared source regions, extracts the
largest dark connected footprint inside each tightly bounded ROI, records exact
pixel spans and rendered-reference palette samples, and draws boundary/landmark
marks only. It does not create candidate geometry or inferred fills.
"""

from __future__ import annotations

from collections import Counter, deque
import hashlib
import json
from pathlib import Path

from PIL import Image, ImageDraw, ImageFont


ROOT = Path(__file__).resolve().parents[2]
ASSET_ID = "SM_DRW_SiegeBreaker_Hammer_A01"
CONTRACT_ID = "SB-VF-A03-PIXEL"
SOURCE = ROOT / "SourceAssets/Reference/Weapons/Dwarven" / ASSET_ID / "02_SiegeBreaker_Codex_Final_Package/reference/concept_sheet_style_reference.png"
OUTPUT = ROOT / "Saved/Automation/DCC" / ASSET_ID / "VisualFidelity_A03/measurement"
PANEL_OUTPUT = OUTPUT / "source_panels"
MANIFEST = ROOT / "docs/assets/blueprints" / ASSET_ID / "manifests/VISUAL_FIDELITY_A03_SOURCE_MEASUREMENTS.json"
REVIEW = ROOT / "docs/assets/blueprints" / ASSET_ID / "review/VISUAL_FIDELITY_A03_SOURCE_MEASUREMENT_AUDIT.md"

# Sheet coordinates are zero-based integer pixel centers. Crop boxes use PIL's
# left/top inclusive, right/bottom exclusive convention. ROIs exclude labels and
# dimension arrows as far as possible; the connected-footprint step rejects any
# remaining disconnected annotation.
PANELS = {
    "primary_3_4": (48, 88, 404, 982),
    "front": (470, 130, 670, 590),
    "back": (770, 130, 965, 590),
    "left": (490, 670, 660, 1030),
    "right": (790, 670, 950, 1030),
    "top": (40, 1065, 510, 1280),
    "bottom": (550, 1065, 1030, 1280),
}

# Source-sheet landmark boxes are explicit observation regions, not geometry.
# They partition the primary visible object for auditable ratios and palette
# sampling. Their edges are shown on the review board.
PRIMARY_REGIONS = {
    "head": (54, 96, 400, 421),
    "shaft": (199, 405, 285, 654),
    "grip": (201, 621, 281, 872),
    "pommel": (178, 852, 298, 974),
}


def sha256(path: Path) -> str:
    digest = hashlib.sha256()
    with path.open("rb") as handle:
        for chunk in iter(lambda: handle.read(1024 * 1024), b""):
            digest.update(chunk)
    return digest.hexdigest()


def largest_component(image: Image.Image, luminance_limit: int = 214) -> set[int]:
    rgb = image.convert("RGB")
    width, height = rgb.size
    candidate = bytearray(width * height)
    for index, (red, green, blue) in enumerate(rgb.getdata()):
        luminance = (red * 54 + green * 183 + blue * 19) // 256
        chroma = max(red, green, blue) - min(red, green, blue)
        candidate[index] = int(luminance <= luminance_limit or (chroma >= 34 and luminance <= 232))
    seen = bytearray(width * height)
    best = []
    for y in range(height):
        for x in range(width):
            start = y * width + x
            if not candidate[start] or seen[start]:
                continue
            queue = deque([start])
            seen[start] = 1
            component = []
            while queue:
                current = queue.popleft()
                py, px = divmod(current, width)
                component.append(current)
                for ny in range(max(0, py - 1), min(height, py + 2)):
                    for nx in range(max(0, px - 1), min(width, px + 2)):
                        neighbor = ny * width + nx
                        if not seen[neighbor] and candidate[neighbor]:
                            seen[neighbor] = 1
                            queue.append(neighbor)
            if len(component) > len(best):
                best = component
    return set(best)


def outer_boundary(mask: set[int], width: int, height: int) -> list[tuple[int, int]]:
    points = []
    for index in mask:
        y, x = divmod(index, width)
        if x == 0 or y == 0 or x == width - 1 or y == height - 1:
            points.append((int(x), int(y)))
            continue
        if not all(neighbor in mask for neighbor in (index - width, index + width, index - 1, index + 1)):
            points.append((int(x), int(y)))
    return points


def palette(image: Image.Image, mask: set[int], colors: int = 10) -> list[dict]:
    source_pixels = list(image.convert("RGB").getdata())
    pixels = [source_pixels[index] for index in sorted(mask)]
    if not pixels:
        return []
    sample = Image.new("RGB", (len(pixels), 1))
    sample.putdata(pixels)
    quantized = sample.quantize(colors=colors, method=0)
    palette_values = quantized.getpalette()
    counts = Counter(quantized.getdata())
    result = []
    for index, count in counts.most_common(colors):
        offset = index * 3
        rgb_value = palette_values[offset:offset + 3]
        result.append({"rgb_srgb_8bit": rgb_value, "pixel_count": count, "fraction": round(count / len(pixels), 6)})
    return result


def measure_panel(source: Image.Image, name: str, crop_box: tuple[int, int, int, int]) -> tuple[dict, Image.Image]:
    crop = source.crop(crop_box)
    rgb = crop.convert("RGB")
    width, height = rgb.size
    mask = largest_component(rgb)
    if not mask:
        raise RuntimeError(f"No connected source footprint in {name}")
    coordinates = [divmod(index, width) for index in mask]
    ys = [item[0] for item in coordinates]
    xs = [item[1] for item in coordinates]
    xmin, xmax = min(xs), max(xs)
    ymin, ymax = min(ys), max(ys)
    boundary = outer_boundary(mask, width, height)
    rows = {}
    columns = {}
    for y, x in coordinates:
        rows.setdefault(y, []).append(x)
        columns.setdefault(x, []).append(y)
    row_spans = []
    for y in range(ymin, ymax + 1):
        row_x = rows.get(y, [])
        if row_x:
            row_spans.append([y + crop_box[1], min(row_x) + crop_box[0], max(row_x) + crop_box[0]])
    column_spans = []
    for x in range(xmin, xmax + 1):
        col_y = columns.get(x, [])
        if col_y:
            column_spans.append([x + crop_box[0], min(col_y) + crop_box[1], max(col_y) + crop_box[1]])

    pixels = list(rgb.getdata())
    cyan_indices = [index for index in mask if pixels[index][2] >= 125 and pixels[index][1] >= 75 and pixels[index][2] - pixels[index][0] >= 36]
    cyan_coordinates = [divmod(index, width) for index in cyan_indices]
    cyan_y = [item[0] for item in cyan_coordinates]
    cyan_x = [item[1] for item in cyan_coordinates]
    cyan_record = {
        "pixel_count": len(cyan_x),
        "centroid_sheet_px": [round(sum(cyan_x) / len(cyan_x) + crop_box[0], 3), round(sum(cyan_y) / len(cyan_y) + crop_box[1], 3)] if cyan_x else None,
        "bounds_sheet_px_inclusive": [min(cyan_x) + crop_box[0], min(cyan_y) + crop_box[1], max(cyan_x) + crop_box[0], max(cyan_y) + crop_box[1]] if cyan_x else None,
    }
    measurement = {
        "panel": name,
        "crop_box_sheet_px_pil": list(crop_box),
        "footprint_method": "largest_8_connected_dark_or_chromatic_component_in_declared_tight_roi",
        "footprint_status": "candidate measurement pending board audit",
        "footprint_pixels": len(mask),
        "bounds_crop_px_inclusive": [xmin, ymin, xmax, ymax],
        "bounds_sheet_px_inclusive": [xmin + crop_box[0], ymin + crop_box[1], xmax + crop_box[0], ymax + crop_box[1]],
        "span_px_inclusive": [xmax - xmin + 1, ymax - ymin + 1],
        "aspect_width_over_height": round((xmax - xmin + 1) / (ymax - ymin + 1), 8),
        "centroid_sheet_px": [round(sum(xs) / len(xs) + crop_box[0], 3), round(sum(ys) / len(ys) + crop_box[1], 3)],
        "cyan_rendered_reference": cyan_record,
        "rendered_reference_palette": palette(rgb, mask),
        "row_spans_sheet_px": row_spans,
        "column_spans_sheet_px": column_spans,
    }
    marked = crop.convert("RGB")
    draw = ImageDraw.Draw(marked)
    for x, y in boundary:
        draw.point((x, y), fill=(225, 35, 35))
    draw.rectangle((xmin, ymin, xmax, ymax), outline=(25, 170, 255), width=1)
    return measurement, marked


def fit_inside(image: Image.Image, width: int, height: int) -> Image.Image:
    copy = image.copy()
    copy.thumbnail((width, height), Image.LANCZOS)
    return copy


def main() -> int:
    OUTPUT.mkdir(parents=True, exist_ok=True)
    PANEL_OUTPUT.mkdir(parents=True, exist_ok=True)
    MANIFEST.parent.mkdir(parents=True, exist_ok=True)
    REVIEW.parent.mkdir(parents=True, exist_ok=True)
    source = Image.open(SOURCE).convert("RGB")
    measurements = {}
    marked_panels = {}
    for name, crop_box in PANELS.items():
        measurement, marked = measure_panel(source, name, crop_box)
        measurements[name] = measurement
        crop_path = PANEL_OUTPUT / f"{name}_source_exact.png"
        marked_path = PANEL_OUTPUT / f"{name}_boundary_marks.png"
        source.crop(crop_box).save(crop_path)
        marked.save(marked_path)
        marked_panels[name] = marked

    primary_regions = {}
    for name, box in PRIMARY_REGIONS.items():
        region = source.crop(box).convert("RGB")
        region_mask = largest_component(region)
        primary_regions[name] = {
            "box_sheet_px_pil": list(box),
            "span_px": [box[2] - box[0], box[3] - box[1]],
            "rendered_reference_palette": palette(region, region_mask, 8),
        }

    primary_bounds = measurements["primary_3_4"]["bounds_sheet_px_inclusive"]
    primary_span = measurements["primary_3_4"]["span_px_inclusive"]
    region_ratios = {
        name: {
            "width_over_primary": round((box[2] - box[0]) / primary_span[0], 6),
            "height_over_primary": round((box[3] - box[1]) / primary_span[1], 6),
            "center_normalized_to_primary_bounds": [
                round((((box[0] + box[2] - 1) / 2) - primary_bounds[0]) / max(1, primary_span[0] - 1), 6),
                round((((box[1] + box[3] - 1) / 2) - primary_bounds[1]) / max(1, primary_span[1] - 1), 6),
            ],
        }
        for name, box in PRIMARY_REGIONS.items()
    }

    record = {
        "schema": "aerathea.siegebreaker.source_pixel_measurements.v1",
        "asset_id": ASSET_ID,
        "contract_id": CONTRACT_ID,
        "artifact_status": "candidate measurement pending exact board audit",
        "source": {
            "path": str(SOURCE.relative_to(ROOT)),
            "sha256": sha256(SOURCE),
            "size_px": list(source.size),
            "mode": source.mode,
            "source_pixels_modified": False,
        },
        "pixel_coordinate_frame": {
            "indexing": "zero_based_integer_pixel_centers",
            "origin": "center_of_top_left_pixel_is_0_0",
            "x_direction": "right",
            "y_direction": "down",
            "crop_box_convention": "PIL left/top inclusive right/bottom exclusive",
        },
        "authority": {
            "primary": "primary_3_4",
            "secondary": ["front", "back", "left", "right", "top", "bottom"],
            "secondary_policy": "usable only after conflict audit",
            "numeric_envelope_cm": [52, 32, 170],
            "rendered_color_not_albedo": True,
        },
        "panels": measurements,
        "primary_regions": primary_regions,
        "primary_region_ratios": region_ratios,
        "unknowns": [
            "hidden depth and occluded contacts are not determined by primary pixels",
            "rendered source RGB combines albedo, illumination, material response, and tone mapping",
            "secondary panel consistency must be audited before cross-view construction",
        ],
    }
    MANIFEST.write_text(json.dumps(record, indent=2) + "\n", encoding="utf-8")

    board = Image.new("RGB", (2200, 1600), (242, 239, 229))
    draw = ImageDraw.Draw(board)
    font = ImageFont.load_default()
    draw.text((40, 28), "SIEGE BREAKER A03 - SOURCE PIXEL MEASUREMENT AUDIT", fill=(28, 28, 28), font=font)
    draw.text((40, 48), "Red: extracted exact connected boundary  |  Cyan: inclusive bounds  |  Green: declared component observation boxes", fill=(28, 28, 28), font=font)
    primary = marked_panels["primary_3_4"].copy()
    pdraw = ImageDraw.Draw(primary)
    primary_crop = PANELS["primary_3_4"]
    for name, box in PRIMARY_REGIONS.items():
        local = (box[0] - primary_crop[0], box[1] - primary_crop[1], box[2] - primary_crop[0] - 1, box[3] - primary_crop[1] - 1)
        pdraw.rectangle(local, outline=(20, 170, 70), width=2)
        pdraw.text((local[0] + 3, local[1] + 3), name, fill=(20, 125, 55), font=font)
    primary = fit_inside(primary, 850, 1450)
    board.paste(primary, (40, 90))
    draw.text((40, 70), "PRIMARY 3/4 SOURCE VIEW", fill=(28, 28, 28), font=font)

    positions = {
        "front": (940, 90), "back": (1530, 90),
        "left": (940, 610), "right": (1530, 610),
        "top": (940, 1120), "bottom": (1530, 1120),
    }
    for name, position in positions.items():
        panel = fit_inside(marked_panels[name], 550, 420)
        board.paste(panel, position)
        span = measurements[name]["span_px_inclusive"]
        draw.text((position[0], position[1] - 18), f"{name.upper()}  measured span {span[0]} x {span[1]} px", fill=(28, 28, 28), font=font)
    board_path = OUTPUT / "SM_DRW_SiegeBreaker_Hammer_A01_A03_SourcePixelMeasurementBoard.png"
    board.save(board_path)

    checks = [
        ("source hash", record["source"]["sha256"] == "3308a7bd0f0830c9cd1b695b57077d9faf77a839bb3e70edc6afe87c68af8b74"),
        ("source dimensions", record["source"]["size_px"] == [1055, 1491]),
        ("all seven panels measured", len(measurements) == 7),
        ("primary connected footprint nonzero", measurements["primary_3_4"]["footprint_pixels"] > 50000),
        ("source pixels unchanged", record["source"]["source_pixels_modified"] is False),
        ("numeric envelope retained", record["authority"]["numeric_envelope_cm"] == [52, 32, 170]),
    ]
    passed = sum(int(value) for _, value in checks)
    lines = [
        "# Siege Breaker A03 Source Pixel Measurement Audit", "",
        f"- Result: `{'pass' if passed == len(checks) else 'fail'}`",
        f"- Gates: `{passed}/{len(checks)}`",
        "- Artifact status: `candidate measurement pending Flamestrike visual review`",
        f"- Source board: `{board_path.relative_to(ROOT)}`", "",
        "## Gates", "",
    ]
    lines.extend(f"- [{'x' if value else ' '}] {name}" for name, value in checks)
    lines += ["", "## Boundary", "", "No candidate fill or geometry was created. Only exact source crops, extracted boundary marks, declared observation boxes, formulas, ratios, and rendered-reference palette samples are present."]
    REVIEW.write_text("\n".join(lines) + "\n", encoding="utf-8")
    print(MANIFEST)
    print(REVIEW)
    print(board_path)
    print(f"MEASUREMENT_AUDIT={'pass' if passed == len(checks) else 'fail'} {passed}/{len(checks)}")
    return 0 if passed == len(checks) else 1


if __name__ == "__main__":
    raise SystemExit(main())
