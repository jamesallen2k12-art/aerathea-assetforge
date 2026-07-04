#!/usr/bin/env python3
"""Build P16: semantic scaffold reconstruction from LACMA perspective evidence.

P16 follows the lesson from P14/P15: raw reference count helps only a little.
This pass converts the measured perspective into named construction geometry:
floor grid, column centerlines, arch envelopes, bay spacing, and vault ribs.
"""

from __future__ import annotations

import shutil
from dataclasses import dataclass
from pathlib import Path

from PIL import Image, ImageDraw, ImageFont

from build_perspective_web_reference_hybrid_measured_board import (
    BG,
    FRAME,
    INK,
    OUT_ROOT,
    PANEL,
    PAPER,
    REF_ROOT,
    REVIEW_ROOT,
    WHITE,
    fit_image,
    panel_image_rect,
)
from build_perspective_web_reference_pixel_measured_board import normalized_to_rect

import build_perspective_web_reference_lacma_clarity_scaffold_board as p14


BOARD_NAME = "P16_LACMAGothicCathedralSemanticScaffoldBoard"
DOC_IMAGE = OUT_ROOT / f"{BOARD_NAME}.png"
REVIEW_IMAGE = REVIEW_ROOT / f"{BOARD_NAME}.png"
MEASUREMENT_MANIFEST = OUT_ROOT / f"{BOARD_NAME}_Measurements.md"

SOURCE_URL = p14.SOURCE_URL
SOURCE_IMAGE_URL = p14.SOURCE_IMAGE_URL
SOURCE_FILENAME = p14.SOURCE_FILENAME

FLOOR_BLUE = (40, 111, 190)
COLUMN_GREEN = (34, 142, 85)
DEPTH_RED = (216, 52, 42)
ARCH_VIOLET = (128, 83, 172)
VAULT_CYAN = (42, 145, 160)
GOLD = (197, 142, 62)
ANCHOR_ORANGE = (234, 146, 44)


def load_font(size: int, bold: bool = False) -> ImageFont.ImageFont:
    suffix = "-Bold" if bold else ""
    candidates = [
        f"/usr/share/fonts/truetype/dejavu/DejaVuSans{suffix}.ttf",
        "/usr/share/fonts/truetype/liberation2/LiberationSans-Bold.ttf"
        if bold
        else "/usr/share/fonts/truetype/liberation2/LiberationSans-Regular.ttf",
    ]
    for candidate in candidates:
        path = Path(candidate)
        if path.exists():
            return ImageFont.truetype(str(path), size=size)
    return ImageFont.load_default()


TITLE_FONT = load_font(42, True)
SUB_FONT = load_font(18)
ROW_FONT = load_font(21, True)
LABEL_FONT = load_font(14, True)
SMALL_FONT = load_font(12)


Point = tuple[float, float]
Rect = tuple[int, int, int, int]


@dataclass(frozen=True)
class DetailCrop:
    title: str
    purpose: str
    crop: tuple[float, float, float, float]


DETAIL_CROPS = [
    DetailCrop("Floor Grid", "tile-corner anchors and receding floor spacing", (0.05, 0.54, 0.96, 0.985)),
    DetailCrop("Column And Arcade", "vertical shaft centers, bases, capitals, and side arcade rhythm", (0.12, 0.07, 0.98, 0.84)),
    DetailCrop("Central Nave", "nested arch envelopes and repeated bay spacing", (0.40, 0.12, 0.77, 0.84)),
    DetailCrop("Vault Ribs", "upper rib curves and overhead convergence", (0.24, 0.02, 0.86, 0.58)),
]


def full_reference():
    return p14.to_reference_spec(p14.PANEL_SPECS[0])


def full_extraction():
    reference = full_reference()
    extraction = p14.extract_with_width(reference, p14.PANEL_SPECS[0].processing_width)
    return reference, extraction


def lerp(a: Point, b: Point, t: float) -> Point:
    return (a[0] + (b[0] - a[0]) * t, a[1] + (b[1] - a[1]) * t)


def qbezier(p0: Point, p1: Point, p2: Point, steps: int = 36) -> list[Point]:
    points: list[Point] = []
    for i in range(steps + 1):
        t = i / steps
        a = lerp(p0, p1, t)
        b = lerp(p1, p2, t)
        points.append(lerp(a, b, t))
    return points


def cbezier(p0: Point, p1: Point, p2: Point, p3: Point, steps: int = 42) -> list[Point]:
    points: list[Point] = []
    for i in range(steps + 1):
        t = i / steps
        a = lerp(p0, p1, t)
        b = lerp(p1, p2, t)
        c = lerp(p2, p3, t)
        d = lerp(a, b, t)
        e = lerp(b, c, t)
        points.append(lerp(d, e, t))
    return points


def pt(point: Point, size: tuple[int, int]) -> tuple[float, float]:
    return (point[0] * size[0], point[1] * size[1])


def draw_norm_line(
    draw: ImageDraw.ImageDraw,
    size: tuple[int, int],
    a: Point,
    b: Point,
    fill: tuple[int, int, int, int],
    width: int = 3,
) -> None:
    pa = pt(a, size)
    pb = pt(b, size)
    draw.line((pa[0], pa[1], pb[0], pb[1]), fill=fill, width=width)


def draw_norm_polyline(
    draw: ImageDraw.ImageDraw,
    size: tuple[int, int],
    points: list[Point],
    fill: tuple[int, int, int, int],
    width: int = 3,
) -> None:
    if len(points) < 2:
        return
    draw.line([pt(point, size) for point in points], fill=fill, width=width, joint="curve")


def draw_anchor(draw: ImageDraw.ImageDraw, size: tuple[int, int], point: Point, fill: tuple[int, int, int, int], radius: int = 5) -> None:
    x, y = pt(point, size)
    draw.ellipse((x - radius, y - radius, x + radius, y + radius), fill=fill, outline=(25, 24, 22, 220), width=1)


def floor_grid(vp: Point) -> tuple[list[tuple[Point, Point]], list[tuple[Point, Point]], list[Point]]:
    bottom_points = [(x, 0.965) for x in (0.045, 0.105, 0.175, 0.255, 0.345, 0.445, 0.555, 0.675, 0.805, 0.94)]
    depth_rays = [(point, vp) for point in bottom_points]
    left_edge = (0.03, 0.94)
    right_edge = (0.97, 0.92)
    row_ts = [0.08, 0.15, 0.23, 0.32, 0.43, 0.55, 0.68, 0.80, 0.90]
    cross_rows = [(lerp(left_edge, vp, t), lerp(right_edge, vp, t)) for t in row_ts]
    anchors: list[Point] = []
    for t in row_ts:
        for point in bottom_points:
            anchors.append(lerp(point, vp, t))
    return depth_rays, cross_rows, anchors


def column_guides() -> list[tuple[Point, Point, str]]:
    return [
        ((0.165, 0.11), (0.165, 0.91), "left foreground column"),
        ((0.245, 0.08), (0.245, 0.92), "left aisle column"),
        ((0.395, 0.00), (0.395, 0.90), "central left pier"),
        ((0.485, 0.04), (0.485, 0.82), "inner nave pier"),
        ((0.565, 0.30), (0.565, 0.76), "rear left column"),
        ((0.630, 0.34), (0.630, 0.77), "rear nave column"),
        ((0.720, 0.08), (0.720, 0.84), "right inner pier"),
        ((0.805, 0.07), (0.805, 0.88), "right arcade pier"),
        ((0.900, 0.06), (0.900, 0.90), "right wall pier"),
        ((0.965, 0.04), (0.965, 0.90), "right edge pier"),
    ]


def central_arches() -> list[tuple[Point, Point, Point, str]]:
    return [
        ((0.538, 0.735), (0.622, 0.420), (0.706, 0.735), "near central arch"),
        ((0.565, 0.670), (0.626, 0.365), (0.686, 0.670), "second central arch"),
        ((0.585, 0.605), (0.628, 0.323), (0.668, 0.605), "third central arch"),
        ((0.600, 0.545), (0.630, 0.292), (0.653, 0.545), "rear arch"),
        ((0.610, 0.500), (0.631, 0.268), (0.646, 0.500), "far arch"),
    ]


def side_arches() -> list[tuple[Point, Point, Point, str]]:
    return [
        ((0.725, 0.790), (0.815, 0.455), (0.900, 0.790), "right foreground arcade"),
        ((0.785, 0.705), (0.860, 0.470), (0.940, 0.705), "right middle arcade"),
        ((0.850, 0.645), (0.915, 0.470), (0.985, 0.645), "right rear arcade"),
        ((0.058, 0.555), (0.190, 0.080), (0.335, 0.555), "left foreground arch"),
        ((0.198, 0.610), (0.310, 0.265), (0.405, 0.610), "left inner arch"),
    ]


def vault_curves() -> list[tuple[list[Point], str]]:
    return [
        (cbezier((0.435, 0.020), (0.520, 0.150), (0.578, 0.300), (0.622, 0.420)), "left high rib to central arch"),
        (cbezier((0.805, 0.045), (0.730, 0.160), (0.668, 0.300), (0.622, 0.420)), "right high rib to central arch"),
        (cbezier((0.490, 0.180), (0.565, 0.250), (0.603, 0.360), (0.626, 0.500)), "left nested nave rib"),
        (cbezier((0.720, 0.170), (0.675, 0.265), (0.645, 0.380), (0.626, 0.500)), "right nested nave rib"),
        (cbezier((0.330, 0.045), (0.405, 0.230), (0.445, 0.420), (0.500, 0.640)), "left vault sweep"),
        (cbezier((0.980, 0.080), (0.895, 0.250), (0.810, 0.430), (0.735, 0.650)), "right vault sweep"),
    ]


def bay_spacing(vp: Point) -> list[tuple[Point, Point]]:
    left_path = [(0.500, 0.730), (0.530, 0.665), (0.555, 0.600), (0.575, 0.540), (0.592, 0.495), (0.604, 0.455)]
    right_path = [(0.735, 0.728), (0.710, 0.665), (0.690, 0.600), (0.675, 0.540), (0.662, 0.495), (0.651, 0.455)]
    pairs = list(zip(left_path, right_path))
    pairs.append((lerp(left_path[-1], vp, 0.35), lerp(right_path[-1], vp, 0.35)))
    return pairs


def semantic_anchor_points(vp: Point) -> dict[str, list[Point]]:
    _rays, _rows, floor_points = floor_grid(vp)
    column_points = [point for top, bottom, _label in column_guides() for point in (top, bottom)]
    arch_points = [point for left, apex, right, _label in central_arches() + side_arches() for point in (left, apex, right)]
    bay_points = [point for left, right in bay_spacing(vp) for point in (left, right)]
    return {
        "floor tile intersections": floor_points,
        "column bases/capitals": column_points,
        "arch bases/apexes": arch_points,
        "bay spacing endpoints": bay_points,
        "vanishing point": [vp],
    }


def rgba(color: tuple[int, int, int], alpha: int) -> tuple[int, int, int, int]:
    return (color[0], color[1], color[2], alpha)


def draw_semantic_scaffold(
    image: Image.Image,
    vp: Point,
    *,
    source_mode: bool,
    draw_crop_boxes: bool = False,
) -> Image.Image:
    canvas = image.convert("RGBA")
    size = canvas.size
    overlay = Image.new("RGBA", canvas.size, (0, 0, 0, 0))
    draw = ImageDraw.Draw(overlay)

    depth_rays, cross_rows, floor_points = floor_grid(vp)
    for start, end in depth_rays:
        draw_norm_line(draw, size, start, end, rgba(DEPTH_RED, 90 if source_mode else 190), width=2 if source_mode else 3)
    for start, end in cross_rows:
        draw_norm_line(draw, size, start, end, rgba(FLOOR_BLUE, 100 if source_mode else 210), width=2 if source_mode else 3)

    for top, bottom, _label in column_guides():
        draw_norm_line(draw, size, top, bottom, rgba(COLUMN_GREEN, 115 if source_mode else 230), width=2 if source_mode else 4)
        tick = 0.018
        for point in (top, bottom):
            draw_norm_line(draw, size, (point[0] - tick, point[1]), (point[0] + tick, point[1]), rgba(COLUMN_GREEN, 125 if source_mode else 230), width=2)

    for left, apex, right, _label in central_arches():
        draw_norm_polyline(draw, size, qbezier(left, apex, right), rgba(ARCH_VIOLET, 140 if source_mode else 230), width=3 if source_mode else 5)
        draw_norm_line(draw, size, left, (left[0], left[1] + 0.095), rgba(ARCH_VIOLET, 90 if source_mode else 180), width=2)
        draw_norm_line(draw, size, right, (right[0], right[1] + 0.095), rgba(ARCH_VIOLET, 90 if source_mode else 180), width=2)

    for left, apex, right, _label in side_arches():
        draw_norm_polyline(draw, size, qbezier(left, apex, right), rgba(ARCH_VIOLET, 105 if source_mode else 205), width=3 if source_mode else 4)

    for curve, _label in vault_curves():
        draw_norm_polyline(draw, size, curve, rgba(VAULT_CYAN, 125 if source_mode else 220), width=3 if source_mode else 5)

    for start, end in bay_spacing(vp):
        draw_norm_line(draw, size, start, end, rgba(GOLD, 105 if source_mode else 210), width=2 if source_mode else 3)

    # Anchor dots are more restrained on the source panel and stronger on clean/detail panels.
    anchor_alpha = 135 if source_mode else 225
    for point in floor_points[::4 if source_mode else 2]:
        draw_anchor(draw, size, point, rgba(FLOOR_BLUE, anchor_alpha), radius=3 if source_mode else 4)
    for top, bottom, _label in column_guides():
        draw_anchor(draw, size, top, rgba(COLUMN_GREEN, anchor_alpha), radius=4)
        draw_anchor(draw, size, bottom, rgba(COLUMN_GREEN, anchor_alpha), radius=4)
    for left, apex, right, _label in central_arches() + side_arches():
        draw_anchor(draw, size, left, rgba(ANCHOR_ORANGE, anchor_alpha), radius=4)
        draw_anchor(draw, size, apex, rgba(ANCHOR_ORANGE, anchor_alpha), radius=5)
        draw_anchor(draw, size, right, rgba(ANCHOR_ORANGE, anchor_alpha), radius=4)

    vp_px = pt(vp, size)
    draw.line((0, vp_px[1], size[0], vp_px[1]), fill=rgba(GOLD, 145 if source_mode else 230), width=2)
    draw.ellipse((vp_px[0] - 10, vp_px[1] - 10, vp_px[0] + 10, vp_px[1] + 10), fill=rgba(DEPTH_RED, 245))

    if draw_crop_boxes:
        for crop in DETAIL_CROPS:
            x0, y0 = pt((crop.crop[0], crop.crop[1]), size)
            x1, y1 = pt((crop.crop[2], crop.crop[3]), size)
            draw.rectangle((x0, y0, x1, y1), outline=rgba(WHITE, 180), width=3)
            draw.text((x0 + 10, y0 + 8), crop.title, font=SMALL_FONT, fill=rgba(WHITE, 230))

    return Image.alpha_composite(canvas, overlay)


def clean_canvas(size: tuple[int, int]) -> Image.Image:
    img = Image.new("RGBA", size, PAPER + (255,))
    draw = ImageDraw.Draw(img)
    # Subtle ruled construction background.
    step = max(32, size[0] // 32)
    for x in range(0, size[0], step):
        draw.line((x, 0, x, size[1]), fill=(210, 202, 184, 90), width=1)
    for y in range(0, size[1], step):
        draw.line((0, y, size[0], y), fill=(210, 202, 184, 70), width=1)
    return img


def crop_norm(image: Image.Image, crop: tuple[float, float, float, float]) -> Image.Image:
    w, h = image.size
    x0, y0, x1, y1 = crop
    return image.crop((round(x0 * w), round(y0 * h), round(x1 * w), round(y1 * h)))


def draw_panel_frame(draw: ImageDraw.ImageDraw, rect: Rect, title: str, dark: bool) -> None:
    draw.rectangle(rect, fill=PANEL if dark else PAPER, outline=FRAME, width=2)
    draw.text((rect[0] + 14, rect[1] + 12), title, font=LABEL_FONT, fill=WHITE if dark else INK)


def paste_image(board: Image.Image, image: Image.Image, panel: Rect, top_pad: int = 48) -> Rect:
    thumb = fit_image(image, (panel[2] - panel[0] - 28, panel[3] - panel[1] - top_pad - 14))
    image_rect = panel_image_rect(panel, thumb, top_pad=top_pad)
    board.paste(thumb.convert("RGBA"), (image_rect[0], image_rect[1]))
    return image_rect


def draw_legend(draw: ImageDraw.ImageDraw, rect: Rect, dark: bool) -> None:
    fill = WHITE if dark else INK
    x = rect[0] + 18
    y = rect[3] - 132
    entries = [
        (FLOOR_BLUE, "floor rows / tile intersections"),
        (DEPTH_RED, "depth rays to solved vanishing point"),
        (COLUMN_GREEN, "column centerlines and base/capital ticks"),
        (ARCH_VIOLET, "arch envelopes and arcade rhythm"),
        (VAULT_CYAN, "vault rib curves"),
        (GOLD, "bay spacing / horizon"),
    ]
    for index, (color, text) in enumerate(entries):
        yy = y + index * 19
        draw.rectangle((x, yy + 3, x + 12, yy + 15), fill=color)
        draw.text((x + 18, yy), text, font=SMALL_FONT, fill=fill)


def write_manifest(vp: Point) -> None:
    anchors = semantic_anchor_points(vp)
    lines = [
        "# P16 LACMA Gothic Cathedral Semantic Scaffold Data",
        "",
        "P16 pivots from raw line-density experiments to semantic reconstruction. The scaffold is curated from P13-P15 measured evidence and visible architectural landmarks.",
        "",
        f"- Source page: {SOURCE_URL}",
        f"- Source image URL: {SOURCE_IMAGE_URL}",
        f"- Source file: `{REF_ROOT.relative_to(OUT_ROOT.parents[3]) / SOURCE_FILENAME}`",
        f"- Solved full-image VP used: `({vp[0]:.6f}, {vp[1]:.6f})`",
        f"- Floor grid rays: `{len(floor_grid(vp)[0])}`",
        f"- Floor cross rows: `{len(floor_grid(vp)[1])}`",
        f"- Column centerlines: `{len(column_guides())}`",
        f"- Central arch envelopes: `{len(central_arches())}`",
        f"- Side arch envelopes: `{len(side_arches())}`",
        f"- Vault rib curves: `{len(vault_curves())}`",
        f"- Bay spacing cross sections: `{len(bay_spacing(vp))}`",
        "",
        "## Anchor Groups",
        "",
    ]
    for name, points in anchors.items():
        lines.append(f"### {name} ({len(points)})")
        for index, point in enumerate(points, 1):
            lines.append(f"- {index:03d}: `({point[0]:.6f}, {point[1]:.6f})`")
        lines.append("")
    lines.extend(
        [
            "## Detail Crops",
            "",
        ]
    )
    for crop in DETAIL_CROPS:
        lines.append(f"- {crop.title}: `{crop.crop}` - {crop.purpose}")
    MEASUREMENT_MANIFEST.write_text("\n".join(lines), encoding="utf-8")


def build_board() -> None:
    OUT_ROOT.mkdir(parents=True, exist_ok=True)
    REVIEW_ROOT.mkdir(parents=True, exist_ok=True)
    reference, extraction = full_extraction()
    source = extraction.crop.convert("RGBA")
    vp = extraction.vp_norm

    source_anchor = draw_semantic_scaffold(source, vp, source_mode=True, draw_crop_boxes=True)
    clean_scaffold = draw_semantic_scaffold(clean_canvas(source.size), vp, source_mode=False)

    width = 3600
    margin = 64
    header_h = 160
    top_h = 1060
    panel_gap = 46
    detail_gap = 34
    detail_h = 520
    footer_h = 84
    height = header_h + top_h + detail_gap + detail_h + footer_h + margin

    board = Image.new("RGBA", (width, height), BG + (255,))
    draw = ImageDraw.Draw(board)
    draw.text((margin, 30), "P16 Semantic Perspective Scaffold Reconstruction", font=TITLE_FONT, fill=WHITE)
    draw.text(
        (margin, 84),
        "Measured perspective evidence converted into named construction geometry: floor grid, columns, arches, bay spacing, and vault ribs.",
        font=SUB_FONT,
        fill=(205, 199, 188),
    )
    draw.text(
        (margin, 116),
        "This is the recommended pivot after P15: fewer raw references, more semantic structure.",
        font=SMALL_FONT,
        fill=(181, 174, 160),
    )

    top_panel_w = (width - margin * 2 - panel_gap) // 2
    left = (margin, header_h, margin + top_panel_w, header_h + top_h)
    right = (margin + top_panel_w + panel_gap, header_h, margin + top_panel_w * 2 + panel_gap, header_h + top_h)
    draw_panel_frame(draw, left, "SOURCE + SEMANTIC ANCHORS / DETAIL CROP BOXES", dark=True)
    paste_image(board, source_anchor, left, top_pad=50)
    draw_legend(draw, left, dark=True)

    draw_panel_frame(draw, right, "CLEAN SEMANTIC SCAFFOLD - NO RAW DETECTION CLUTTER", dark=False)
    paste_image(board, clean_scaffold, right, top_pad=50)
    draw_legend(draw, right, dark=False)

    detail_w = (width - margin * 2 - detail_gap * 3) // 4
    y0 = header_h + top_h + detail_gap
    for index, detail in enumerate(DETAIL_CROPS):
        x0 = margin + index * (detail_w + detail_gap)
        panel = (x0, y0, x0 + detail_w, y0 + detail_h)
        draw_panel_frame(draw, panel, detail.title.upper(), dark=False)
        detail_crop = crop_norm(clean_scaffold, detail.crop)
        paste_image(board, detail_crop, panel, top_pad=50)
        draw.text((panel[0] + 16, panel[3] - 42), detail.purpose, font=SMALL_FONT, fill=INK)
        draw.text((panel[0] + 16, panel[3] - 22), f"crop {detail.crop}", font=SMALL_FONT, fill=(94, 88, 76))

    footer_y = height - margin - footer_h + 10
    draw.text(
        (margin, footer_y),
        "P16 result: explicit structure is now separated from measurement density; this is the pass to judge for clarity.",
        font=ROW_FONT,
        fill=WHITE,
    )
    draw.text((margin, footer_y + 36), SOURCE_URL, font=SMALL_FONT, fill=(205, 199, 188))

    write_manifest(vp)
    board.convert("RGB").save(DOC_IMAGE, optimize=True)
    shutil.copy2(DOC_IMAGE, REVIEW_IMAGE)
    print(DOC_IMAGE)
    print(REVIEW_IMAGE)
    print(MEASUREMENT_MANIFEST)


if __name__ == "__main__":
    build_board()
