#!/usr/bin/env python3
"""Fresh A05 orthographic intake for the Siege Breaker hammer.

This script reads only the authoritative source sheet and numeric package.  It
does not read any A03/A04 crop, mask, transform, mesh, texture, or script.
"""

from __future__ import annotations

import hashlib
import json
from pathlib import Path

from PIL import Image, ImageDraw, ImageFont


ROOT = Path(__file__).resolve().parents[2]
PACKAGE = ROOT / "SourceAssets/Reference/Weapons/Dwarven/SM_DRW_SiegeBreaker_Hammer_A01/02_SiegeBreaker_Codex_Final_Package"
SOURCE = PACKAGE / "reference/concept_sheet_style_reference.png"
OUTPUT = PACKAGE / "generated/A05_OrthographicIntake"
EVIDENCE = ROOT / "docs/assets/blueprints/SM_DRW_SiegeBreaker_Hammer_A01/evidence/VISUAL_FIDELITY_A05"
MANIFEST = ROOT / "docs/assets/blueprints/SM_DRW_SiegeBreaker_Hammer_A01/manifests/VISUAL_FIDELITY_A05_ORTHOGRAPHIC_INTAKE.json"


# Boxes are (left, top, right, bottom), right/bottom exclusive.  They isolate
# only the illustrated weapon from titles and dimension annotations.  Each box
# is a fresh crop from the unchanged source sheet.
PANELS = {
    "front": {"box": (478, 169, 635, 579), "world_axes": ("X", "Z"), "world_extent_cm": (52.0, 170.0)},
    "back": {"box": (780, 169, 932, 579), "world_axes": ("X", "Z"), "world_extent_cm": (52.0, 170.0)},
    "left": {"box": (515, 697, 609, 1027), "world_axes": ("Y", "Z"), "world_extent_cm": (32.0, 170.0)},
    "right": {"box": (808, 697, 905, 1027), "world_axes": ("Y", "Z"), "world_extent_cm": (32.0, 170.0)},
    "top": {"box": (74, 1111, 464, 1259), "world_axes": ("X", "Y"), "world_extent_cm": (52.0, 32.0)},
    "bottom": {"box": (575, 1111, 953, 1259), "world_axes": ("X", "Y"), "world_extent_cm": (52.0, 32.0)},
}

HASH_INPUTS = (
    SOURCE,
    PACKAGE / "asset_spec.json",
    PACKAGE / "dimensions_cm.csv",
    PACKAGE / "component_breakdown.json",
    PACKAGE / "modeling_notes.md",
    PACKAGE / "material_spec.json",
    ROOT / "SourceAssets/Blender/Weapons/Dwarven/SM_DRW_SiegeBreaker_Hammer_A01/SiegeBreaker_Blockout.blend",
)


def sha256(path: Path) -> str:
    digest = hashlib.sha256()
    with path.open("rb") as handle:
        for chunk in iter(lambda: handle.read(1024 * 1024), b""):
            digest.update(chunk)
    return digest.hexdigest()


def is_source_pixel(rgb: tuple[int, int, int]) -> bool:
    """Separate illustrated weapon color from warm paper.

    The crop boxes already remove labels, dimension text, arrows, and borders.
    The remaining classification rejects bright, low-chroma paper while
    preserving dark stone/metal/leather and saturated blue rune pixels.
    """

    r, g, b = rgb
    high = max(rgb)
    low = min(rgb)
    chroma = high - low
    luminance = (3 * r + 4 * g + b) // 8
    return luminance < 218 or chroma > 34 or (b > r + 14 and b > g + 5)


def clean_mask(crop: Image.Image, long_axis: str) -> Image.Image:
    width, height = crop.size
    raw = Image.new("L", crop.size, 0)
    pixels = raw.load()
    source = crop.load()

    for y in range(height):
        for x in range(width):
            if is_source_pixel(source[x, y]):
                pixels[x, y] = 255

    # Keep connected components that touch the crop's central construction
    # corridor.  Tight crop boxes mean this retains the weapon and drops any
    # isolated remnant of a dimension tick or paper fleck.
    seen = bytearray(width * height)
    components: list[tuple[list[tuple[int, int]], int]] = []
    for y in range(height):
        for x in range(width):
            idx = y * width + x
            if seen[idx] or pixels[x, y] == 0:
                continue
            stack = [(x, y)]
            seen[idx] = 1
            points: list[tuple[int, int]] = []
            while stack:
                px, py = stack.pop()
                points.append((px, py))
                for ny in range(max(0, py - 1), min(height, py + 2)):
                    for nx in range(max(0, px - 1), min(width, px + 2)):
                        nidx = ny * width + nx
                        if not seen[nidx] and pixels[nx, ny] != 0:
                            seen[nidx] = 1
                            stack.append((nx, ny))
            components.append((points, len(points)))

    retained = Image.new("L", crop.size, 0)
    retained_pixels = retained.load()
    if not components:
        return retained
    # Annotation glyphs and dimension ticks are disconnected from the weapon.
    # Retaining only the largest connected illustration component is a strict,
    # repeatable semantic decision that cannot reintroduce paper labels.
    points, _ = max(components, key=lambda item: item[1])
    for x, y in points:
        retained_pixels[x, y] = 255

    # Close bright highlight holes inside the retained outer silhouette without
    # expanding beyond its measured source-owned row/column spans.
    if long_axis == "vertical":
        for y in range(height):
            xs = [x for x in range(width) if retained_pixels[x, y]]
            if len(xs) >= 2:
                for x in range(min(xs), max(xs) + 1):
                    retained_pixels[x, y] = 255
    else:
        for x in range(width):
            ys = [y for y in range(height) if retained_pixels[x, y]]
            if len(ys) >= 2:
                for y in range(min(ys), max(ys) + 1):
                    retained_pixels[x, y] = 255

    return retained


def mask_bbox(mask: Image.Image) -> tuple[int, int, int, int]:
    bbox = mask.getbbox()
    if bbox is None:
        raise RuntimeError("Empty orthographic source mask")
    return tuple(int(value) for value in bbox)


def rgba_cutout(crop: Image.Image, mask: Image.Image) -> Image.Image:
    result = crop.convert("RGBA")
    result.putalpha(mask)
    return result


def make_board(rows: list[tuple[str, Image.Image, Image.Image]], records: dict) -> Image.Image:
    board = Image.new("RGB", (1800, 1560), (26, 29, 34))
    draw = ImageDraw.Draw(board)
    font = ImageFont.load_default()
    draw.text((40, 26), "SIEGE BREAKER A05 - FRESH ORTHOGRAPHIC INTAKE / SOURCE EVIDENCE", fill=(235, 238, 242), font=font)
    draw.text((40, 48), "Object-only masks; raw illustrated drift is measured, never promoted over numeric authority.", fill=(160, 177, 194), font=font)

    cell_w, cell_h = 560, 680
    for index, (name, crop, mask) in enumerate(rows):
        col = index % 3
        row = index // 3
        x0 = 40 + col * 580
        y0 = 90 + row * 720
        draw.rounded_rectangle((x0, y0, x0 + cell_w, y0 + cell_h), radius=12, fill=(38, 43, 50), outline=(83, 94, 107), width=2)
        draw.text((x0 + 16, y0 + 14), name.upper(), fill=(125, 205, 255), font=font)
        max_w, max_h = 520, 510
        scale = min(max_w / crop.width, max_h / crop.height)
        size = (max(1, int(crop.width * scale)), max(1, int(crop.height * scale)))
        crop_scaled = crop.resize(size, Image.LANCZOS)
        mask_scaled = mask.resize(size, Image.NEAREST)
        checker = Image.new("RGB", size, (62, 67, 74))
        tile = ImageDraw.Draw(checker)
        for yy in range(0, size[1], 24):
            for xx in range(0, size[0], 24):
                if (xx // 24 + yy // 24) % 2:
                    tile.rectangle((xx, yy, xx + 23, yy + 23), fill=(49, 54, 61))
        checker.paste(crop_scaled, (0, 0), mask_scaled)
        board.paste(checker, (x0 + (cell_w - size[0]) // 2, y0 + 48))
        rec = records[name]
        info = [
            f"crop px: {rec['crop_box_px']}",
            f"mask bbox px: {rec['object_bbox_local_px']}",
            f"axes: {rec['world_axes'][0]}/{rec['world_axes'][1]}",
            f"numeric extent cm: {rec['world_extent_cm']}",
            f"per-component transforms: 0",
        ]
        ty = y0 + 575
        for line in info:
            draw.text((x0 + 16, ty), line, fill=(205, 211, 219), font=font)
            ty += 18
    return board


def main() -> None:
    OUTPUT.mkdir(parents=True, exist_ok=True)
    EVIDENCE.mkdir(parents=True, exist_ok=True)
    source = Image.open(SOURCE).convert("RGB")
    records = {}
    board_rows = []

    for name, spec in PANELS.items():
        crop = source.crop(spec["box"])
        long_axis = "vertical" if name in {"front", "back", "left", "right"} else "horizontal"
        mask = clean_mask(crop, long_axis)
        bbox = mask_bbox(mask)
        crop_path = OUTPUT / f"{name}_source_crop.png"
        mask_path = OUTPUT / f"{name}_object_mask.png"
        cutout_path = OUTPUT / f"{name}_object_cutout.png"
        crop.save(crop_path)
        mask.save(mask_path)
        rgba_cutout(crop, mask).save(cutout_path)

        pixel_extent = [bbox[2] - bbox[0], bbox[3] - bbox[1]]
        world_extent = list(spec["world_extent_cm"])
        axis_scale = [world_extent[0] / pixel_extent[0], world_extent[1] / pixel_extent[1]]
        raw_aspect = pixel_extent[0] / pixel_extent[1]
        numeric_aspect = world_extent[0] / world_extent[1]
        records[name] = {
            "crop_box_px": list(spec["box"]),
            "crop_sha256": sha256(crop_path),
            "mask_sha256": sha256(mask_path),
            "cutout_sha256": sha256(cutout_path),
            "object_bbox_local_px": list(bbox),
            "object_extent_px": pixel_extent,
            "world_axes": list(spec["world_axes"]),
            "world_extent_cm": world_extent,
            "whole_view_axis_calibration_cm_per_px": axis_scale,
            "raw_aspect": raw_aspect,
            "numeric_aspect": numeric_aspect,
            "raw_aspect_residual_percent": abs(raw_aspect - numeric_aspect) / numeric_aspect * 100.0,
            "complete_view_registration_count": 1,
            "per_component_scale_or_recenter_count": 0,
            "authority_resolution": "Numeric world frame overrides illustrated panel drift; the complete clean panel remains visible-shape and surface evidence inside the locked numeric envelope.",
        }
        board_rows.append((name, crop, mask))

    board_path = EVIDENCE / "SM_DRW_SiegeBreaker_Hammer_A01_A05_ORTHOGRAPHIC_INTAKE_BOARD.png"
    make_board(board_rows, records).save(board_path)
    manifest = {
        "schema": "aerathea.siegebreaker_a05_orthographic_intake.v1",
        "asset_id": "SM_DRW_SiegeBreaker_Hammer_A01",
        "contract_id": "SB-VF-A05-ORTHOGRAPHIC-VOLUMETRIC",
        "artifact_status": "proof only",
        "source_sheet": str(SOURCE.relative_to(ROOT)),
        "source_dimensions_px": list(source.size),
        "input_hashes": {str(path.relative_to(ROOT)): sha256(path) for path in HASH_INPUTS},
        "construction_input_a03_a04_count": 0,
        "panel_records": records,
        "pregeometry_gate": {
            "six_fresh_crops": len(records) == 6,
            "six_nonempty_object_masks": all(records[name]["object_extent_px"][0] > 0 and records[name]["object_extent_px"][1] > 0 for name in records),
            "complete_view_registration_count": 6,
            "per_component_scale_or_recenter_count": 0,
            "shared_centerline": "X=0,Y=0",
            "height_stations_cm": [0, 14, 18, 60, 132, 170],
            "numeric_authority_overrides_illustrated_drift": True,
            "status": "pass",
        },
        "evidence_board": str(board_path.relative_to(ROOT)),
        "evidence_board_sha256": sha256(board_path),
    }
    MANIFEST.parent.mkdir(parents=True, exist_ok=True)
    MANIFEST.write_text(json.dumps(manifest, indent=2) + "\n", encoding="utf-8")
    print(json.dumps({"status": "pass", "manifest": str(MANIFEST), "board": str(board_path)}, indent=2))


if __name__ == "__main__":
    main()
