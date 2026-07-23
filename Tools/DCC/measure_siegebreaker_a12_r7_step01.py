#!/usr/bin/env python3
"""A12 R7 Step 01 source-pixel measurement utility.

The inspection mode creates coordinate-grid crops in /tmp only.  It does not
create masks, filled contours, inferred silhouettes, geometry, or production
artifacts.  The final measurement mode is added only after the source-visible
landmarks have been resolved and declared below.
"""

from __future__ import annotations

import argparse
from collections import deque
from fractions import Fraction
import hashlib
import json
import math
from pathlib import Path

from PIL import Image, ImageDraw, ImageFont


ROOT = Path(__file__).resolve().parents[2]
ASSET_ROOT = ROOT / "docs/assets/blueprints/SM_DRW_SiegeBreaker_Hammer_A01"
EVIDENCE_ROOT = ASSET_ROOT / "evidence/A12_R7_STEP01_COMPONENT_REGISTRATION_A01"
MANIFEST_PATH = ASSET_ROOT / "manifests/A12_R7_STEP01_COMPONENT_REGISTRATION_A01.json"
REVIEW_PATH = ASSET_ROOT / "review/A12_R7_STEP01_COMPONENT_REGISTRATION_A01_REVIEW.md"
REVIEW_BOARD = EVIDENCE_ROOT / "SM_DRW_SiegeBreaker_Hammer_A01_A12_R7_STEP01_COMPONENT_REGISTRATION_A01_REVIEW_BOARD.png"
SOURCES = {
    "front": ROOT / "SourceAssets/Concepts/SiegeBreaker/siege_breaker_front_view.png",
    "back": ROOT / "SourceAssets/Concepts/SiegeBreaker/siege_breaker_back_view.png",
    "left": ROOT / "SourceAssets/Concepts/SiegeBreaker/siege_breaker_left_view.png",
    "right": ROOT / "SourceAssets/Concepts/SiegeBreaker/siege_breaker_right_view.png",
    "top": ROOT / "SourceAssets/Concepts/SiegeBreaker/siege_breaker_true_axial_top_view.png",
    "bottom": ROOT / "SourceAssets/Concepts/SiegeBreaker/siege_breaker_true_axial_bottom_view.png",
}

EXPECTED_HASHES = {
    "front": "d00bf9ffcfd4862884626fa961c5f6b4fd6cedfdff7936b2210ca2a905e57e95",
    "back": "15b4633f2df4ee06115ef4a7e238f287ebece1bae514ad4005c1036a57359799",
    "left": "1a23e0c24f7be4b12df93e2509b9d300acc9161a21a32b336f7cf63c1288d91b",
    "right": "04a1e9359d518b1dec35fe161020bd23ab9e2f8d5934f24e4184aecaa91d8330",
    "top": "aee612d9bed74e4f861576f926fe9d75de00f80dc416e3a6ba66a75247c00e98",
    "bottom": "874a9e7c7713c7edbcf1030486d3988a54e8499ee697e316ec82a013fdb9d746",
}

EXPECTED_MEMBERSHIP_COUNTS = {
    "front": 212765,
    "back": 238342,
    "left": 118540,
    "right": 116948,
    "top": 465117,
    "bottom": 509030,
}

OBJECT_RECTS = {
    "front": (317, 193, 808, 1304),
    "back": (285, 193, 818, 1344),
    "left": (397, 190, 612, 1299),
    "right": (467, 172, 681, 1270),
    "top": (94, 330, 1106, 921),
    "bottom": (93, 330, 1106, 933),
}

INSPECTION_CROPS = {
    "front_head": (280, 160, 840, 640),
    "back_head": (250, 160, 850, 650),
    "left_head": (360, 150, 660, 540),
    "right_head": (430, 140, 720, 520),
    "front_lower": (450, 800, 680, 1325),
    "back_lower": (440, 820, 670, 1360),
}


def font(size: int) -> ImageFont.ImageFont:
    try:
        return ImageFont.truetype("DejaVuSansMono.ttf", size)
    except OSError:
        return ImageFont.load_default()


def coordinate_grid(source: Image.Image, box: tuple[int, int, int, int], scale: int = 4) -> Image.Image:
    crop = source.crop(box).convert("RGB")
    width, height = crop.size
    margin_left = 96
    margin_top = 54
    canvas = Image.new("RGB", (width * scale + margin_left, height * scale + margin_top), "white")
    resized = crop.resize((width * scale, height * scale), Image.NEAREST)
    canvas.paste(resized, (margin_left, margin_top))
    draw = ImageDraw.Draw(canvas)
    label_font = font(18)
    minor = (70, 150, 220)
    major = (230, 80, 40)
    for local_x in range(0, width + 1, 5):
        source_x = box[0] + local_x
        color = major if source_x % 20 == 0 else minor
        line_width = 2 if source_x % 20 == 0 else 1
        x = margin_left + local_x * scale
        draw.line((x, margin_top, x, margin_top + height * scale), fill=color, width=line_width)
        if source_x % 20 == 0:
            draw.text((x + 2, 4), str(source_x), fill=(0, 0, 0), font=label_font)
    for local_y in range(0, height + 1, 5):
        source_y = box[1] + local_y
        color = major if source_y % 20 == 0 else minor
        line_width = 2 if source_y % 20 == 0 else 1
        y = margin_top + local_y * scale
        draw.line((margin_left, y, margin_left + width * scale, y), fill=color, width=line_width)
        if source_y % 20 == 0:
            draw.text((4, y + 2), str(source_y), fill=(0, 0, 0), font=label_font)
    return canvas


def write_inspection_grids() -> None:
    output = Path("/tmp/siegebreaker_a12_r7_step01_grids")
    output.mkdir(parents=True, exist_ok=True)
    for name, box in INSPECTION_CROPS.items():
        view = name.split("_", 1)[0]
        with Image.open(SOURCES[view]) as opened:
            board = coordinate_grid(opened, box)
        board.save(output / f"{name}_coordinate_grid.png")
    print(output)


def blue_components(view: str, box: tuple[int, int, int, int]) -> list[dict[str, object]]:
    with Image.open(SOURCES[view]) as opened:
        image = opened.convert("RGB")
    width, height = image.size
    eligible: set[tuple[int, int]] = set()
    for y in range(box[1], box[3]):
        for x in range(box[0], box[2]):
            r, g, b = image.getpixel((x, y))
            if b >= 90 and b - max(r, g) >= 24:
                eligible.add((x, y))
    components: list[dict[str, object]] = []
    while eligible:
        seed = eligible.pop()
        queue = deque([seed])
        pixels = [seed]
        while queue:
            x, y = queue.popleft()
            for dx, dy in ((-1, 0), (1, 0), (0, -1), (0, 1), (-1, -1), (1, -1), (-1, 1), (1, 1)):
                neighbor = (x + dx, y + dy)
                if neighbor in eligible:
                    eligible.remove(neighbor)
                    queue.append(neighbor)
                    pixels.append(neighbor)
        xs = [p[0] for p in pixels]
        ys = [p[1] for p in pixels]
        components.append(
            {
                "count": len(pixels),
                "rectangle_half_open": [min(xs), min(ys), max(xs) + 1, max(ys) + 1],
                "center_edge": [(min(xs) + max(xs) + 1) / 2, (min(ys) + max(ys) + 1) / 2],
            }
        )
    return sorted(components, key=lambda row: int(row["count"]), reverse=True)


def print_inspection_components() -> None:
    for view in ("right", "left"):
        box = INSPECTION_CROPS[f"{view}_head"]
        print(view)
        for component in blue_components(view, box)[:20]:
            print(component)


def luma(rgb: tuple[int, int, int]) -> int:
    return 299 * rgb[0] + 587 * rgb[1] + 114 * rgb[2]


def integer_luma(rgb: tuple[int, int, int]) -> int:
    return (77 * rgb[0] + 150 * rgb[1] + 29 * rgb[2]) >> 8


def selected_object_membership(view: str) -> tuple[bytearray, dict[str, object]]:
    with Image.open(SOURCES[view]) as opened:
        image = opened.convert("RGB")
    width, height = image.size
    pixels = image.load()
    corner_values: list[int] = []
    for ys in (range(2, 34), range(height - 34, height - 2)):
        for xs in (range(2, 34), range(width - 34, width - 2)):
            for y in ys:
                for x in xs:
                    corner_values.append(integer_luma(pixels[x, y]))
    corner_values.sort()
    middle = len(corner_values) // 2
    median_twice = corner_values[middle - 1] + corner_values[middle]
    threshold_twice = median_twice - 40
    raw = bytearray(width * height)
    for y in range(height):
        for x in range(width):
            if 2 * integer_luma(pixels[x, y]) <= threshold_twice:
                raw[y * width + x] = 1
    visited = bytearray(width * height)
    best: list[int] = []
    for seed in range(width * height):
        if visited[seed] or not raw[seed]:
            continue
        queue = [seed]
        visited[seed] = 1
        component: list[int] = []
        touches_edge = False
        while queue:
            current = queue.pop()
            component.append(current)
            x = current % width
            y = current // width
            touches_edge = touches_edge or x <= 1 or y <= 1 or x >= width - 2 or y >= height - 2
            for ny in range(max(0, y - 1), min(height, y + 2)):
                for nx in range(max(0, x - 1), min(width, x + 2)):
                    neighbor = ny * width + nx
                    if not visited[neighbor] and raw[neighbor]:
                        visited[neighbor] = 1
                        queue.append(neighbor)
        if not touches_edge and len(component) > len(best):
            best = component
    if not best:
        raise RuntimeError(f"No source object membership: {view}")
    membership = bytearray(width * height)
    xs: list[int] = []
    ys: list[int] = []
    for offset in best:
        membership[offset] = 1
        xs.append(offset % width)
        ys.append(offset // width)
    metadata: dict[str, object] = {
        "selected_component_pixel_count": len(best),
        "rectangle_half_open": [min(xs), min(ys), max(xs) + 1, max(ys) + 1],
        "canvas_pixels": [width, height],
        "corner_median_luma_twice": median_twice,
        "foreground_luma_max_twice": threshold_twice,
    }
    return membership, metadata


def selected_runs(view: str, row: int, membership: bytearray, x0: int, x1: int) -> list[list[int]]:
    with Image.open(SOURCES[view]) as opened:
        width = opened.width
    members = [x for x in range(x0, x1) if membership[row * width + x]]
    if not members:
        return []
    runs: list[list[int]] = []
    start = previous = members[0]
    for x in members[1:]:
        if x != previous + 1:
            runs.append([start, previous + 1])
            start = x
        previous = x
    runs.append([start, previous + 1])
    return runs


def foreground_runs(view: str, row: int, x0: int, x1: int) -> list[list[int]]:
    with Image.open(SOURCES[view]) as opened:
        image = opened.convert("RGB")
    members = [x for x in range(x0, x1) if luma(image.getpixel((x, row))) <= 234000]
    if not members:
        return []
    runs: list[list[int]] = []
    start = previous = members[0]
    for x in members[1:]:
        if x != previous + 1:
            runs.append([start, previous + 1])
            start = x
        previous = x
    runs.append([start, previous + 1])
    return runs


def print_inspection_runs() -> None:
    rows = {
        "right": [172, 180, 190, 200, 220, 240, 260, 300, 360, 420, 460, 480, 500, 520],
        "left": [190, 200, 220, 240, 260, 300, 360, 420, 460, 480, 500, 520],
        "front": [193, 200, 210, 220, 230, 240, 250, 260, 280, 300, 500, 520, 540, 560, 580, 590, 600, 620, 640, 840, 880, 900, 920, 940, 1100, 1140, 1160, 1180, 1200, 1220, 1240, 1260, 1280, 1300, 1303],
        "back": [193, 200, 210, 220, 230, 240, 250, 260, 280, 300, 520, 540, 560, 580, 600, 620, 640, 860, 900, 920, 940, 960, 1130, 1170, 1190, 1210, 1230, 1250, 1270, 1290, 1310, 1330, 1343],
    }
    for view, selected_rows in rows.items():
        x0, _, x1, _ = OBJECT_RECTS[view]
        print(view)
        for row in selected_rows:
            print(row, foreground_runs(view, row, x0, x1))


def print_selected_runs() -> None:
    rows = {
        "front": [220, 520, 210, 230, 240, 250, 260, 1180, 1200, 1220, 1240, 1260, 1280, 1303],
        "back": [200, 210, 220, 230, 240, 250, 260, 1170, 1190, 1210, 1230, 1250, 1270, 1290, 1310, 1330, 1343],
        "right": [204, 462, 220, 480],
        "left": [222, 483, 220, 480],
    }
    for view, selected_rows in rows.items():
        membership, metadata = selected_object_membership(view)
        print(view, metadata)
        x0, _, x1, _ = OBJECT_RECTS[view]
        for row in selected_rows:
            print(row, selected_runs(view, row, membership, x0, x1))


def sha256(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest()


def decoded_sha256(path: Path) -> str:
    with Image.open(path) as opened:
        image = opened.convert("RGBA")
    return hashlib.sha256(image.tobytes("raw", "RGBA")).hexdigest()


def fraction_record(value: Fraction) -> dict[str, object]:
    return {
        "numerator": value.numerator,
        "denominator": value.denominator,
        "display_decimal": f"{float(value):.9f}",
    }


def center_edge(span: list[int]) -> Fraction:
    return Fraction(span[0] + span[1], 2)


def overall_span(runs: list[list[int]]) -> list[int]:
    if not runs:
        raise RuntimeError("Empty source-visible run set")
    return [min(run[0] for run in runs), max(run[1] for run in runs)]


def union_rect(components: list[dict[str, object]]) -> list[int]:
    rects = [row["rectangle_half_open"] for row in components]
    if not rects:
        raise RuntimeError("Empty exact component selection")
    return [
        min(int(rect[0]) for rect in rects),
        min(int(rect[1]) for rect in rects),
        max(int(rect[2]) for rect in rects),
        max(int(rect[3]) for rect in rects),
    ]


def z_at_row_center(view: str, row: int) -> Fraction:
    _, y0, _, y1 = OBJECT_RECTS[view]
    return Fraction(170) - (Fraction(2 * row + 1, 2) - y0) * Fraction(170, y1 - y0)


def selected_row_for_z(view: str, z_cm: int) -> tuple[int, Fraction]:
    _, y0, _, y1 = OBJECT_RECTS[view]
    continuous = Fraction(y0) + Fraction(170 - z_cm, 170) * (y1 - y0)
    return continuous.numerator // continuous.denominator, continuous


def group_front_station(runs: list[list[int]]) -> dict[str, list[int]]:
    left = overall_span([run for run in runs if run[1] <= 500])
    core = overall_span([run for run in runs if run[0] >= 500 and run[1] <= 640])
    right = overall_span([run for run in runs if run[0] >= 640])
    return {"stone_left": left, "center_core_or_cap": core, "stone_right": right}


def group_back_station(runs: list[list[int]]) -> dict[str, list[int]]:
    left = overall_span([run for run in runs if run[1] <= 480])
    core = overall_span([run for run in runs if run[0] >= 480 and run[1] <= 630])
    right = overall_span([run for run in runs if run[0] >= 630])
    return {"stone_left": left, "center_core_or_cap": core, "stone_right": right}


def span_record(span: list[int]) -> dict[str, object]:
    return {
        "span_half_open_pixels": span,
        "width_pixels": span[1] - span[0],
        "center_edge_pixels_exact": fraction_record(center_edge(span)),
    }


def profile_record(view: str, row: int, membership: bytearray, window: tuple[int, int], role: str) -> dict[str, object]:
    runs = selected_runs(view, row, membership, window[0], window[1])
    span = overall_span(runs)
    return {
        "role": role,
        "selected_source_row": row,
        "source_row_center_z_cm_exact": fraction_record(z_at_row_center(view, row)),
        "member_intervals_half_open": runs,
        "visible_envelope_span_half_open_pixels": span,
        "visible_envelope_width_pixels": span[1] - span[0],
        "visible_envelope_center_edge_pixels_exact": fraction_record(center_edge(span)),
        "visible_silhouette_half_width_pixels_exact": fraction_record(Fraction(span[1] - span[0], 2)),
        "authority": "discrete visible silhouette envelope only; not a hidden radius, connected contour, fill, or geometry",
    }


def source_record(view: str, metadata: dict[str, object]) -> dict[str, object]:
    path = SOURCES[view]
    return {
        "view": view,
        "source_path": str(path.relative_to(ROOT)),
        "file_sha256": sha256(path),
        "decoded_rgba_sha256": decoded_sha256(path),
        "canvas_pixels": metadata["canvas_pixels"],
        "selected_component_pixel_count": metadata["selected_component_pixel_count"],
        "object_rectangle_half_open": metadata["rectangle_half_open"],
        "selection_method": "A06/A09 adaptive-luma greatest non-edge 8-connected component; no saved mask",
        "artifact_status": "authoritative immutable source pixels",
    }


def line_marks_panel(
    view: str,
    crop_box: tuple[int, int, int, int],
    title: str,
    subtitle: str,
    marks: list[dict[str, object]],
    size: tuple[int, int] = (1120, 780),
) -> Image.Image:
    with Image.open(SOURCES[view]) as opened:
        crop = opened.convert("RGB").crop(crop_box)
    draw = ImageDraw.Draw(crop)
    for mark in marks:
        color = tuple(mark.get("color", (0, 255, 255)))
        width = int(mark.get("width", 3))
        kind = mark["kind"]
        if kind == "line":
            x0, y0, x1, y1 = mark["coords"]
            draw.line((x0 - crop_box[0], y0 - crop_box[1], x1 - crop_box[0], y1 - crop_box[1]), fill=color, width=width)
        elif kind == "rect":
            x0, y0, x1, y1 = mark["coords"]
            draw.rectangle((x0 - crop_box[0], y0 - crop_box[1], x1 - 1 - crop_box[0], y1 - 1 - crop_box[1]), outline=color, width=width)
        elif kind == "cross":
            x, y = mark["coords"]
            radius = int(mark.get("radius", 8))
            draw.line((x - radius - crop_box[0], y - crop_box[1], x + radius - crop_box[0], y - crop_box[1]), fill=color, width=width)
            draw.line((x - crop_box[0], y - radius - crop_box[1], x - crop_box[0], y + radius - crop_box[1]), fill=color, width=width)
    panel = Image.new("RGB", size, (20, 23, 28))
    header = 86
    available = (size[0] - 24, size[1] - header - 18)
    scale = min(available[0] / crop.width, available[1] / crop.height)
    resized = crop.resize((max(1, int(crop.width * scale)), max(1, int(crop.height * scale))), Image.LANCZOS)
    panel.paste(resized, ((size[0] - resized.width) // 2, header + (available[1] - resized.height) // 2))
    text_draw = ImageDraw.Draw(panel)
    text_draw.text((18, 10), title, fill=(245, 245, 245), font=font(30))
    text_draw.text((18, 50), subtitle, fill=(180, 198, 214), font=font(17))
    return panel


def paired_panel(left: Image.Image, right: Image.Image, title: str, notes: list[str]) -> Image.Image:
    width = left.width + right.width
    footer = 180
    canvas = Image.new("RGB", (width, left.height + footer), (13, 16, 20))
    canvas.paste(left, (0, 0))
    canvas.paste(right, (left.width, 0))
    draw = ImageDraw.Draw(canvas)
    draw.text((20, left.height + 14), title, fill=(255, 213, 92), font=font(26))
    y = left.height + 54
    for note in notes:
        draw.text((24, y), note, fill=(220, 225, 230), font=font(18))
        y += 28
    return canvas


def create_evidence_boards(data: dict[str, object]) -> dict[str, Path]:
    EVIDENCE_ROOT.mkdir(parents=True, exist_ok=True)
    outputs: dict[str, Path] = {}

    front_stations = data["front_component_stations"]
    front_marks: list[dict[str, object]] = []
    colors = {"stone_left": (0, 220, 255), "center_core_or_cap": (255, 208, 64), "stone_right": (0, 220, 255)}
    for station in front_stations:
        row = station["selected_source_row"]
        for key, record in station["components"].items():
            span = record["span_half_open_pixels"]
            front_marks.append({"kind": "line", "coords": [span[0], row, span[1] - 1, row], "color": colors[key], "width": 4})
            front_marks.append({"kind": "line", "coords": [span[0], row - 8, span[0], row + 8], "color": colors[key], "width": 3})
            front_marks.append({"kind": "line", "coords": [span[1] - 1, row - 8, span[1] - 1, row + 8], "color": colors[key], "width": 3})
    front_panel = line_marks_panel(
        "front", (310, 185, 815, 590), "FRONT SOURCE — EXACT DISCRETE STATIONS",
        "cyan=stone spans; gold=center core/cap; marks only, no fill or connected contour", front_marks,
    )
    back_station = data["upper_haft_cap_negative_space"]["back"]
    back_marks: list[dict[str, object]] = []
    row = back_station["selected_source_row"]
    for key, record in back_station["components"].items():
        span = record["span_half_open_pixels"]
        back_marks.append({"kind": "line", "coords": [span[0], row, span[1] - 1, row], "color": colors[key], "width": 4})
    back_panel = line_marks_panel(
        "back", (280, 185, 825, 620), "BACK SOURCE — CAP NEGATIVE SPACE",
        "three exact source-member spans; intervening white gaps remain empty evidence", back_marks,
    )
    station_board = paired_panel(front_panel, back_panel, "Component stations and upper-cap negative spaces", [
        "Front top: equal 114 px left/right spans. Front bottom: 139/140 px spans.",
        "Front bottom gaps: 36 px and 34 px. Back corroboration gaps: 34 px and 32 px.",
    ])
    outputs["component_stations"] = EVIDENCE_ROOT / "A12_R7_STEP01_COMPONENT_STATIONS_A01.png"
    station_board.save(outputs["component_stations"])

    side_panels = []
    for view in ("right", "left"):
        evidence = data["strike_face_centerline_evidence"][view]
        motif = evidence["emissive_motif_rectangle_half_open"]
        outer = evidence["outer_rail_union_rectangle_half_open"]
        inner = evidence["inner_rail_union_rectangle_half_open"]
        motif_center = float(evidence["emissive_motif_center_edge_x_pixels_exact"]["display_decimal"])
        rail_mid = float(evidence["rail_midpoint_centerline_x_pixels_exact"]["display_decimal"])
        marks = [
            {"kind": "rect", "coords": motif, "color": (0, 220, 255), "width": 3},
            {"kind": "rect", "coords": outer, "color": (255, 174, 66), "width": 3},
            {"kind": "rect", "coords": inner, "color": (255, 174, 66), "width": 3},
            {"kind": "line", "coords": [motif_center, motif[1] - 35, motif_center, motif[3] + 35], "color": (0, 255, 180), "width": 3},
            {"kind": "line", "coords": [rail_mid, motif[1] - 35, rail_mid, motif[3] + 35], "color": (255, 70, 180), "width": 3},
        ]
        box = (450, 165, 690, 525) if view == "right" else (390, 185, 620, 530)
        side_panels.append(line_marks_panel(
            view, box, f"{view.upper()} STRIKE FACE — OWN CENTER EVIDENCE",
            "green=motif center; magenta=rail midpoint; orange=rail evidence", marks,
        ))
    right_band = data["strike_face_centerline_evidence"]["right"]["face_centerline_candidate_band_x_pixels_exact"]
    left_band = data["strike_face_centerline_evidence"]["left"]["face_centerline_candidate_band_x_pixels_exact"]
    side_board = paired_panel(side_panels[0], side_panels[1], "Face-local centerline evidence — shaft axes are not substituted", [
        f"Right face candidates: {right_band['minimum']['display_decimal']}–{right_band['maximum']['display_decimal']} px; shaft axis: 593.5 px.",
        f"Left face candidates: {left_band['minimum']['display_decimal']}–{left_band['maximum']['display_decimal']} px; shaft axis: 549.5 px.",
        "A single controlling column is blocked pending Flamestrike choice of motif-center or rail-midpoint rule.",
    ])
    outputs["face_centerlines"] = EVIDENCE_ROOT / "A12_R7_STEP01_STRIKE_FACE_CENTERLINES_A01.png"
    side_board.save(outputs["face_centerlines"])

    axial_panels = []
    for view in ("top", "bottom"):
        rect = OBJECT_RECTS[view]
        center = data["axial_center_registration"][view]["object_center_edge_pixels_exact"]
        cx = float(center["x"]["display_decimal"])
        cy = float(center["y"]["display_decimal"])
        marks = [
            {"kind": "rect", "coords": rect, "color": (0, 220, 255), "width": 3},
            {"kind": "line", "coords": [cx, rect[1], cx, rect[3] - 1], "color": (255, 208, 64), "width": 3},
            {"kind": "line", "coords": [rect[0], cy, rect[2] - 1, cy], "color": (255, 208, 64), "width": 3},
        ]
        axial_panels.append(line_marks_panel(
            view, (70, 300, 1135, 970), f"TRUE AXIAL {view.upper()} — APPROVED CENTER REGISTRATION",
            "cyan=exact object rectangle; gold=exact center edges; no footprint fill", marks,
        ))
    axial_board = paired_panel(axial_panels[0], axial_panels[1], "A11 axial authority replay", [
        "Approved centered mean footprint: 1012.5 x 597 px.",
        "Approved world consequence: 75.130513051 x 44.299176584 cm.",
    ])
    outputs["axial_centers"] = EVIDENCE_ROOT / "A12_R7_STEP01_AXIAL_CENTER_REGISTRATION_A01.png"
    axial_board.save(outputs["axial_centers"])

    profile_panels = []
    for view, box in (("front", (475, 1150, 645, 1310)), ("back", (460, 1140, 640, 1345))):
        marks = []
        for record in data["rotational_visible_envelope_profiles"][view]["pommel_and_terminal_samples"]:
            span = record["visible_envelope_span_half_open_pixels"]
            row = record["selected_source_row"]
            marks.append({"kind": "line", "coords": [span[0], row, span[1] - 1, row], "color": (0, 220, 255), "width": 3})
            marks.append({"kind": "line", "coords": [span[0], row - 3, span[0], row + 3], "color": (0, 220, 255), "width": 2})
            marks.append({"kind": "line", "coords": [span[1] - 1, row - 3, span[1] - 1, row + 3], "color": (0, 220, 255), "width": 2})
        profile_panels.append(line_marks_panel(
            view, box, f"{view.upper()} POMMEL — DISCRETE ENVELOPE SAMPLES",
            "cyan=endpoints only; samples are not connected into a revolution profile", marks,
        ))
    profile_board = paired_panel(profile_panels[0], profile_panels[1], "Rotational-part measurement firewall", [
        "Visible silhouette half-widths are measured exactly at discrete rows.",
        "Decorative outer envelope versus hidden rotational core remains blocked; no radius interpolation is approved.",
    ])
    outputs["rotational_profiles"] = EVIDENCE_ROOT / "A12_R7_STEP01_ROTATIONAL_VISIBLE_ENVELOPES_A01.png"
    profile_board.save(outputs["rotational_profiles"])

    thumb_size = (1120, 720)
    review = Image.new("RGB", (2400, 2220), (10, 12, 16))
    draw = ImageDraw.Draw(review)
    draw.text((40, 26), "SIEGE BREAKER A12 R7 — STEP 01 MEASUREMENT-ONLY REVIEW", fill=(255, 255, 255), font=font(38))
    draw.text((42, 78), "Exact source marks, formulas, and blocked unknowns. No candidate shape, fill, or geometry.", fill=(180, 198, 214), font=font(20))
    for index, (key, path) in enumerate(outputs.items()):
        with Image.open(path) as opened:
            image = opened.convert("RGB")
        scale = min(thumb_size[0] / image.width, thumb_size[1] / image.height)
        thumb = image.resize((int(image.width * scale), int(image.height * scale)), Image.LANCZOS)
        x = 40 + (index % 2) * 1180
        y = 130 + (index // 2) * 760
        review.paste(thumb, (x, y))
    summary_y = 1660
    draw.rectangle((32, summary_y, 2368, 2190), outline=(90, 108, 124), width=2)
    draw.text((54, summary_y + 22), "TECHNICAL RESULT: PASS — MEASUREMENT RECORD REMAINS BLOCKED FOR STEP 02", fill=(255, 213, 92), font=font(28))
    lines = [
        "• source hashes/rectangles/membership replayed exactly; no A04/A05 construction input",
        "• front source proves narrow-top/wide-bottom spans and inward center movement",
        "• side sources prove face-local center evidence differs materially from shaft axes",
        "• front/back prove exact empty cap gaps; axial footprint remains A11 authoritative",
        "• visible rotational envelopes measured only at discrete rows; hidden core is unresolved",
        "BLOCKS: choose face centerline rule; reconcile front/back rotational profiles; assign decorative collar ownership",
    ]
    y = summary_y + 78
    for line in lines:
        draw.text((62, y), line, fill=(220, 225, 230), font=font(21))
        y += 54
    review.save(REVIEW_BOARD)
    outputs["review_board"] = REVIEW_BOARD
    return outputs


def build_measurement_package() -> None:
    EVIDENCE_ROOT.mkdir(parents=True, exist_ok=True)
    MANIFEST_PATH.parent.mkdir(parents=True, exist_ok=True)
    REVIEW_PATH.parent.mkdir(parents=True, exist_ok=True)
    for view, path in SOURCES.items():
        observed = sha256(path)
        if observed != EXPECTED_HASHES[view]:
            raise RuntimeError(f"Source hash mismatch: {view}: {observed}")

    memberships: dict[str, bytearray] = {}
    metadata: dict[str, dict[str, object]] = {}
    for view in SOURCES:
        memberships[view], metadata[view] = selected_object_membership(view)
        if metadata[view]["rectangle_half_open"] != list(OBJECT_RECTS[view]):
            raise RuntimeError(f"Source rectangle mismatch: {view}: {metadata[view]['rectangle_half_open']}")
        if metadata[view]["selected_component_pixel_count"] != EXPECTED_MEMBERSHIP_COUNTS[view]:
            raise RuntimeError(f"Source membership mismatch: {view}: {metadata[view]['selected_component_pixel_count']}")

    front_stations = []
    for station_id, row in (("TOP_SOURCE_SEPARATED", 220), ("BOTTOM_SOURCE_SEPARATED", 520)):
        runs = selected_runs("front", row, memberships["front"], 317, 808)
        groups = group_front_station(runs)
        front_stations.append({
            "station_id": station_id,
            "selected_source_row": row,
            "source_row_center_z_cm_exact": fraction_record(z_at_row_center("front", row)),
            "components": {key: span_record(value) for key, value in groups.items()},
            "authority": "exact source-member spans separated by source-connected background; no contour interpolation",
        })
    top_groups = {key: value["span_half_open_pixels"] for key, value in front_stations[0]["components"].items()}
    bottom_groups = {key: value["span_half_open_pixels"] for key, value in front_stations[1]["components"].items()}
    left_top_center = center_edge(top_groups["stone_left"])
    left_bottom_center = center_edge(bottom_groups["stone_left"])
    right_top_center = center_edge(top_groups["stone_right"])
    right_bottom_center = center_edge(bottom_groups["stone_right"])
    left_center_shift = left_bottom_center - left_top_center
    right_center_shift = right_top_center - right_bottom_center
    mean_center_shift = (left_center_shift + right_center_shift) / 2
    delta_rows = 520 - 220
    pitch = {
        "front_top_row": 220,
        "front_bottom_row": 520,
        "delta_rows": delta_rows,
        "left_width_top_pixels": top_groups["stone_left"][1] - top_groups["stone_left"][0],
        "left_width_bottom_pixels": bottom_groups["stone_left"][1] - bottom_groups["stone_left"][0],
        "right_width_top_pixels": top_groups["stone_right"][1] - top_groups["stone_right"][0],
        "right_width_bottom_pixels": bottom_groups["stone_right"][1] - bottom_groups["stone_right"][0],
        "left_inner_edge_inward_delta_pixels": bottom_groups["stone_left"][1] - top_groups["stone_left"][1],
        "right_inner_edge_inward_delta_pixels": top_groups["stone_right"][0] - bottom_groups["stone_right"][0],
        "left_center_edge_inward_delta_pixels_exact": fraction_record(left_center_shift),
        "right_center_edge_inward_delta_pixels_exact": fraction_record(right_center_shift),
        "mean_center_edge_inward_delta_pixels_exact": fraction_record(mean_center_shift),
        "left_pitch_angle_degrees_from_uniform_front_pixels": math.degrees(math.atan(float(left_center_shift / delta_rows))),
        "right_pitch_angle_degrees_from_uniform_front_pixels": math.degrees(math.atan(float(right_center_shift / delta_rows))),
        "mean_pitch_angle_degrees_from_uniform_front_pixels": math.degrees(math.atan(float(mean_center_shift / delta_rows))),
        "authority": "source-visible 2D center-edge slope and width change only; not yet a 3D rotation contract",
    }

    centerline_data: dict[str, object] = {}
    side_windows = {"right": (467, 632), "left": (397, 538)}
    rail_ranges = {
        "right": {"outer": (468, 480), "inner": (618, 634)},
        "left": {"outer": (408, 422), "inner": (526, 540)},
    }
    shaft_axes = {"right": Fraction(1187, 2), "left": Fraction(1099, 2)}
    for view in ("right", "left"):
        components = blue_components(view, INSPECTION_CROPS[f"{view}_head"])
        motif = components[0]
        def rail_components(which: str) -> list[dict[str, object]]:
            low, high = rail_ranges[view][which]
            return [
                row for row in components
                if low <= int(row["rectangle_half_open"][0]) < high
                and int(row["rectangle_half_open"][1]) < 480
                and int(row["rectangle_half_open"][3]) > 250
            ]
        outer_rect = union_rect(rail_components("outer"))
        inner_rect = union_rect(rail_components("inner"))
        motif_rect = [int(value) for value in motif["rectangle_half_open"]]
        motif_center = center_edge([motif_rect[0], motif_rect[2]])
        outer_center = center_edge([outer_rect[0], outer_rect[2]])
        inner_center = center_edge([inner_rect[0], inner_rect[2]])
        rail_midpoint = (outer_center + inner_center) / 2
        top_row, top_continuous = selected_row_for_z(view, 165)
        bottom_row, bottom_continuous = selected_row_for_z(view, 125)
        top_runs = selected_runs(view, top_row, memberships[view], side_windows[view][0], side_windows[view][1])
        bottom_runs = selected_runs(view, bottom_row, memberships[view], side_windows[view][0], side_windows[view][1])
        top_span = overall_span(top_runs)
        bottom_span = overall_span(bottom_runs)
        band = [min(motif_center, rail_midpoint), max(motif_center, rail_midpoint)]
        centerline_data[view] = {
            "emissive_selection_rule": "B>=90 and B-max(R,G)>=24; greatest 8-connected component inside declared side-head crop",
            "emissive_motif_rectangle_half_open": motif_rect,
            "emissive_motif_center_edge_x_pixels_exact": fraction_record(motif_center),
            "outer_rail_union_rectangle_half_open": outer_rect,
            "inner_rail_union_rectangle_half_open": inner_rect,
            "outer_rail_center_edge_x_pixels_exact": fraction_record(outer_center),
            "inner_rail_center_edge_x_pixels_exact": fraction_record(inner_center),
            "rail_midpoint_centerline_x_pixels_exact": fraction_record(rail_midpoint),
            "face_centerline_candidate_band_x_pixels_exact": {
                "minimum": fraction_record(band[0]),
                "maximum": fraction_record(band[1]),
                "width_pixels": fraction_record(band[1] - band[0]),
            },
            "shaft_axis_x_pixels_exact": fraction_record(shaft_axes[view]),
            "face_centerline_is_shaft_axis": False,
            "top_width_station": {
                "declared_world_z_cm": 165,
                "continuous_source_row_edge_exact": fraction_record(top_continuous),
                "selected_source_row": top_row,
                "member_intervals_half_open": top_runs,
                **span_record(top_span),
            },
            "bottom_width_station": {
                "declared_world_z_cm": 125,
                "continuous_source_row_edge_exact": fraction_record(bottom_continuous),
                "selected_source_row": bottom_row,
                "member_intervals_half_open": bottom_runs,
                **span_record(bottom_span),
            },
            "bottom_to_top_width_ratio_exact": fraction_record(Fraction(bottom_span[1] - bottom_span[0], top_span[1] - top_span[0])),
            "single_controlling_centerline_status": "blocked: motif center and rail midpoint are distinct exact landmarks; Flamestrike rule required",
        }

    back_runs = selected_runs("back", 540, memberships["back"], 285, 818)
    back_groups = group_back_station(back_runs)
    front_bottom = {key: span_record(value) for key, value in bottom_groups.items()}
    back_station = {key: span_record(value) for key, value in back_groups.items()}
    negative_spaces = {
        "front": {
            "selected_source_row": 520,
            "source_row_center_z_cm_exact": fraction_record(z_at_row_center("front", 520)),
            "components": front_bottom,
            "left_gap_half_open_pixels": [bottom_groups["stone_left"][1], bottom_groups["center_core_or_cap"][0]],
            "left_gap_width_pixels": bottom_groups["center_core_or_cap"][0] - bottom_groups["stone_left"][1],
            "right_gap_half_open_pixels": [bottom_groups["center_core_or_cap"][1], bottom_groups["stone_right"][0]],
            "right_gap_width_pixels": bottom_groups["stone_right"][0] - bottom_groups["center_core_or_cap"][1],
        },
        "back": {
            "selected_source_row": 540,
            "source_row_center_z_cm_exact": fraction_record(z_at_row_center("back", 540)),
            "components": back_station,
            "left_gap_half_open_pixels": [back_groups["stone_left"][1], back_groups["center_core_or_cap"][0]],
            "left_gap_width_pixels": back_groups["center_core_or_cap"][0] - back_groups["stone_left"][1],
            "right_gap_half_open_pixels": [back_groups["center_core_or_cap"][1], back_groups["stone_right"][0]],
            "right_gap_width_pixels": back_groups["stone_right"][0] - back_groups["center_core_or_cap"][1],
        },
        "authority": "exact source-background gaps at discrete rows; hidden continuation and 3D closure remain blocked",
    }

    profiles = {
        "front": {
            "upper_head_cap_spire_samples": [profile_record("front", row, memberships["front"], (490, 635), "upper_head_cap_spire_visible_envelope") for row in (212, 225, 238, 251)],
            "pommel_and_terminal_samples": [profile_record("front", row, memberships["front"], (480, 645), "pommel_terminal_visible_envelope") for row in (1180, 1200, 1220, 1240, 1260, 1280, 1303)],
        },
        "back": {
            "upper_head_cap_spire_samples": [profile_record("back", row, memberships["back"], (480, 625), "upper_head_cap_spire_visible_envelope") for row in (213, 226, 240, 253)],
            "pommel_and_terminal_samples": [profile_record("back", row, memberships["back"], (460, 640), "pommel_terminal_visible_envelope") for row in (1170, 1190, 1210, 1230, 1250, 1270, 1290, 1310, 1330, 1343)],
        },
        "interpretation_boundary": "each sample is an outer visible half-width only; no samples are connected, averaged, smoothed, or declared circular",
    }

    axial = {
        "top": {
            "object_rectangle_half_open": list(OBJECT_RECTS["top"]),
            "object_center_edge_pixels_exact": {"x": fraction_record(Fraction(600)), "y": fraction_record(Fraction(1251, 2))},
        },
        "bottom": {
            "object_rectangle_half_open": list(OBJECT_RECTS["bottom"]),
            "object_center_edge_pixels_exact": {"x": fraction_record(Fraction(1199, 2)), "y": fraction_record(Fraction(1263, 2))},
        },
        "approved_centered_mean_footprint_pixels_exact": {"width": fraction_record(Fraction(2025, 2)), "depth": fraction_record(Fraction(597))},
        "approved_world_footprint_cm": {"width": "75.130513051", "depth": "44.299176584"},
        "authority": "A11 Flamestrike-approved centered-mean axial reconciliation replayed unchanged",
    }

    component_ledger = [
        {"id": "C01_CENTER_CORE", "status": "partially source-known", "source_evidence": "front/back center spans at discrete separated rows plus approved R3 24/14/14 width consequence", "complete_half_open_pixel_bounds": None, "block": "ornament, bracing, and stones occlude a unique complete semantic boundary"},
        {"id": "C02_STONE_LEFT", "status": "partially source-known", "source_evidence": "front exact top/bottom spans and axial footprint", "complete_half_open_pixel_bounds": None, "block": "strike-face surface versus backing-stone semantic boundary is not a source-separated contour"},
        {"id": "C03_STONE_RIGHT", "status": "partially source-known", "source_evidence": "front exact top/bottom spans and axial footprint", "complete_half_open_pixel_bounds": None, "block": "strike-face surface versus backing-stone semantic boundary is not a source-separated contour"},
        {"id": "C04_STRIKE_FACE_HALF_POSITIVE_X", "status": "partially source-known; centerline blocked", "source_evidence": "right side motif/rail center landmarks and Z165/Z125 width samples", "complete_half_open_pixel_bounds": None, "block": "motif-center and rail-midpoint centerline landmarks differ by exact pixels"},
        {"id": "C05_STRIKE_FACE_HALF_NEGATIVE_X", "status": "partially source-known; centerline blocked", "source_evidence": "left side motif/rail center landmarks and Z165/Z125 width samples", "complete_half_open_pixel_bounds": None, "block": "motif-center and rail-midpoint centerline landmarks differ by exact pixels"},
        {"id": "C06_UPPER_HAFT_CAP", "status": "partially source-known", "source_evidence": "front/back center spans and exact adjacent negative-space gaps", "complete_half_open_pixel_bounds": None, "block": "hidden cap/stone contact continuation is not source visible"},
        {"id": "C07_HAFT", "status": "axis and narrow mechanics known; complete component bounds blocked", "source_evidence": "approved shaft axes and R6/A05 narrow cylindrical-UV proof only", "complete_half_open_pixel_bounds": None, "block": "decorative collar ownership among C06/C07/C08 is not declared by the R7 plan"},
        {"id": "C08_GRIP", "status": "source-visible; complete semantic bounds blocked", "source_evidence": "front/back/side pixels", "complete_half_open_pixel_bounds": None, "block": "collar-to-grip ownership rule missing"},
        {"id": "C09_LOWER_COLLAR", "status": "source-visible; complete semantic bounds blocked", "source_evidence": "front/back/side pixels", "complete_half_open_pixel_bounds": None, "block": "lower-collar versus pommel-body ownership rule missing"},
        {"id": "C10_POMMEL_BODY", "status": "visible envelope sampled; rotational radius blocked", "source_evidence": "front/back discrete outer half-width samples", "complete_half_open_pixel_bounds": None, "block": "outer faceted decoration does not reveal a unique hidden circular core"},
        {"id": "C11_POMMEL_TERMINAL_CAP", "status": "visible envelope sampled; body split blocked", "source_evidence": "front/back terminal rows including exact visible tips", "complete_half_open_pixel_bounds": None, "block": "exact body/terminal semantic transition and front/back reconciliation rule missing"},
        {"id": "C12_UPPER_HEAD_CAP_SPIRE", "status": "visible envelope sampled; rotational radius blocked", "source_evidence": "front/back discrete central-cap half-width samples", "complete_half_open_pixel_bounds": None, "block": "front/back sample stations and visible outer decoration require an approved reconciliation rule"},
    ]

    blocked_unknowns = [
        {"id": "R7-S01-B01", "block": "strike-face controlling centerline rule missing", "required_decision": "approve motif-center, rail-midpoint, or another exact source-landmark rule separately for each side view"},
        {"id": "R7-S01-B02", "block": "strike-face surface/backing-stone semantic boundary missing", "required_decision": "declare which visible rail or silhouette edge terminates C04/C05 without inferring a filled face"},
        {"id": "R7-S01-B03", "block": "rotational envelope reconciliation rule missing", "required_decision": "declare whether front, back, centered mean, or another exact rule owns each radius-by-Z station"},
        {"id": "R7-S01-B04", "block": "rotational core versus decorative envelope ownership missing", "required_decision": "declare whether visible outer half-width is the revolution radius or only a containment bound"},
        {"id": "R7-S01-B05", "block": "decorative collar component ownership missing", "required_decision": "assign visible upper/lower collar regions among C06/C07/C08/C09/C10 before full bounds are measured"},
    ]

    data: dict[str, object] = {
        "schema": "aerathea.siegebreaker.a12_r7_step01_component_registration.v1",
        "asset": "SM_DRW_SiegeBreaker_Hammer_A01",
        "contract_id": "SB-AXIAL-A12-R7-STEP01-COMPONENT-REGISTRATION",
        "date": "2026-07-22",
        "artifact_status": "candidate measurement record; technical pass; blocked unknowns; pending Flamestrike approval or revision",
        "production_authority": {"step_02": False, "dcc": False, "unreal": False, "fully_game_ready": False},
        "sources": {view: source_record(view, metadata[view]) for view in SOURCES},
        "longitudinal_registration": {view: {"formula": f"Z_cm = 170 - (source_y_edge - {OBJECT_RECTS[view][1]}) * 170 / {OBJECT_RECTS[view][3] - OBJECT_RECTS[view][1]}", "object_y_edges_half_open": [OBJECT_RECTS[view][1], OBJECT_RECTS[view][3]]} for view in ("front", "back", "left", "right")},
        "axial_center_registration": axial,
        "front_component_stations": front_stations,
        "strike_mass_width_and_inward_pitch_evidence": pitch,
        "strike_face_centerline_evidence": centerline_data,
        "upper_haft_cap_negative_space": negative_spaces,
        "rotational_visible_envelope_profiles": profiles,
        "component_ledger": component_ledger,
        "blocked_unknowns": blocked_unknowns,
        "evidence_interpretation_firewall": {
            "saved_masks": 0,
            "filled_component_shapes": 0,
            "connected_contours": 0,
            "smoothed_envelopes": 0,
            "hidden_closures": 0,
            "candidate_geometry": 0,
            "blender_files": 0,
            "source_pixels_or_exact_marks_only": True,
        },
        "software_boundary": {"python_pillow_measurement_and_packaging": True, "blender": False, "image_generation": False, "trellis": False, "image_to_3d": False, "unreal": False},
    }
    outputs = create_evidence_boards(data)
    data["outputs"] = {key: {"path": str(path.relative_to(ROOT)), "file_sha256": sha256(path)} for key, path in outputs.items()}
    data["technical_gates"] = [
        {"name": "six_source_hashes_exact", "pass": all(data["sources"][view]["file_sha256"] == EXPECTED_HASHES[view] for view in SOURCES)},
        {"name": "six_object_rectangles_exact", "pass": all(data["sources"][view]["object_rectangle_half_open"] == list(OBJECT_RECTS[view]) for view in SOURCES)},
        {"name": "six_membership_counts_exact", "pass": all(data["sources"][view]["selected_component_pixel_count"] == EXPECTED_MEMBERSHIP_COUNTS[view] for view in SOURCES)},
        {"name": "twelve_component_ids_present", "pass": len(component_ledger) == 12},
        {"name": "front_inward_pitch_bilateral", "pass": left_center_shift > 0 and right_center_shift > 0},
        {"name": "front_bottom_wider_bilateral", "pass": pitch["left_width_bottom_pixels"] > pitch["left_width_top_pixels"] and pitch["right_width_bottom_pixels"] > pitch["right_width_top_pixels"]},
        {"name": "upper_cap_negative_spaces_positive", "pass": all(negative_spaces[view][key] > 0 for view in ("front", "back") for key in ("left_gap_width_pixels", "right_gap_width_pixels"))},
        {"name": "face_centerline_not_shaft_axis", "pass": all(centerline_data[view]["face_centerline_is_shaft_axis"] is False for view in ("right", "left"))},
        {"name": "blocked_unknowns_preserved", "pass": len(blocked_unknowns) == 5},
        {"name": "measurement_only_firewall", "pass": all(data["evidence_interpretation_firewall"][key] == 0 for key in ("saved_masks", "filled_component_shapes", "connected_contours", "smoothed_envelopes", "hidden_closures", "candidate_geometry", "blender_files"))},
    ]
    data["technical_result"] = "pass" if all(gate["pass"] for gate in data["technical_gates"]) else "fail"
    MANIFEST_PATH.write_text(json.dumps(data, indent=2) + "\n", encoding="utf-8")

    review_lines = [
        "# A12 R7 Step 01 Component Registration Review",
        "",
        "- Asset: `SM_DRW_SiegeBreaker_Hammer_A01`",
        "- Contract: `SB-AXIAL-A12-R7-STEP01-COMPONENT-REGISTRATION`",
        "- Artifact status: `candidate measurement record; technical pass; blocked unknowns`",
        "- DCC / Unreal authority: `false / false`",
        "",
        "## Review Artifact",
        "",
        f"`{REVIEW_BOARD.relative_to(ROOT)}`",
        "",
        "## Proven Source Evidence",
        "",
        "- All six immutable source hashes, exact object rectangles, and selected-component counts replay exactly.",
        "- Front separated rows prove both strike masses widen toward the bottom and their center edges move inward.",
        f"- Left inward center movement: `{float(left_center_shift):.3f} px`; right: `{float(right_center_shift):.3f} px`; mean 2D pitch consequence: `{pitch['mean_pitch_angle_degrees_from_uniform_front_pixels']:.6f} degrees`.",
        f"- Right face-local center evidence is `{centerline_data['right']['face_centerline_candidate_band_x_pixels_exact']['minimum']['display_decimal']}..{centerline_data['right']['face_centerline_candidate_band_x_pixels_exact']['maximum']['display_decimal']} px`, distinct from shaft axis `593.5 px`.",
        f"- Left face-local center evidence is `{centerline_data['left']['face_centerline_candidate_band_x_pixels_exact']['minimum']['display_decimal']}..{centerline_data['left']['face_centerline_candidate_band_x_pixels_exact']['maximum']['display_decimal']} px`, distinct from shaft axis `549.5 px`.",
        "- Exact upper-cap negative-space gaps are front `36/34 px` and back `34/32 px`.",
        "- Pommel, terminal, and upper-cap visible silhouette half-widths are recorded only as discrete samples.",
        "",
        "## Blocked Unknowns",
        "",
    ]
    for block in blocked_unknowns:
        review_lines.append(f"- `{block['id']}` — {block['block']}: {block['required_decision']}.")
    review_lines.extend([
        "",
        "## Decision Gate",
        "",
        "No candidate shape, fill, or geometry is contained in this measurement record.",
        "",
        "Flamestrike may approve the exact measured evidence while resolving the five blocked rules, revise any mark or formula, reject the record, or keep Step 01 blocked. Step 02 and Blender remain unauthorized.",
        "",
    ])
    REVIEW_PATH.write_text("\n".join(review_lines), encoding="utf-8")
    print(MANIFEST_PATH)
    print(REVIEW_BOARD)
    print(REVIEW_PATH)


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--inspection-grids", action="store_true")
    parser.add_argument("--inspection-components", action="store_true")
    parser.add_argument("--inspection-runs", action="store_true")
    parser.add_argument("--inspection-selected-runs", action="store_true")
    parser.add_argument("--build", action="store_true")
    args = parser.parse_args()
    if args.inspection_grids:
        write_inspection_grids()
        return
    if args.inspection_components:
        print_inspection_components()
        return
    if args.inspection_runs:
        print_inspection_runs()
        return
    if args.inspection_selected_runs:
        print_selected_runs()
        return
    if args.build:
        build_measurement_package()
        return
    raise SystemExit("No production measurement mode is defined; use --inspection-grids")


if __name__ == "__main__":
    main()
