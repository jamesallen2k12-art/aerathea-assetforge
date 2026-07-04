#!/usr/bin/env python3
"""Build P17: evidence-locked perspective reconstruction board.

P16 failed because it introduced hand-curated scaffold geometry too early.
P17 uses a stricter rule: every visible stroke is either an actual detected
source segment or a mathematically derived intersection from detected segment
equations. No invented arches, no guessed curves.
"""

from __future__ import annotations

import math
import shutil
from pathlib import Path

from PIL import Image, ImageDraw, ImageEnhance, ImageFont

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
from build_perspective_web_reference_xyz_axis_highres_board import (
    X_BLUE,
    Y_GREEN,
    Z_RED,
    line_box_points,
    line_rank,
    norm_to_rect,
)
from build_perspective_web_reference_z_axis_board import z_depth_score

import build_perspective_web_reference_lacma_clarity_scaffold_board as p14
import build_perspective_web_reference_lacma_ultradense10x_board as p15


BOARD_NAME = "P17_LACMAGothicCathedralEvidenceLockedReconstructionBoard"
DOC_IMAGE = OUT_ROOT / f"{BOARD_NAME}.png"
REVIEW_IMAGE = REVIEW_ROOT / f"{BOARD_NAME}.png"
MEASUREMENT_MANIFEST = OUT_ROOT / f"{BOARD_NAME}_Measurements.md"

SOURCE_URL = p14.SOURCE_URL
SOURCE_IMAGE_URL = p14.SOURCE_IMAGE_URL
SOURCE_FILENAME = p14.SOURCE_FILENAME

ORANGE = (232, 139, 36)
GOLD = (197, 142, 62)
GRAY = (112, 108, 98)

FULL_LIMITS = (70, 90, 125)
DETAIL_LIMITS = {
    "Floor grid 10x": (40, 8, 90),
    "Central nave 10x": (34, 55, 95),
    "Right arcade 10x": (45, 95, 95),
    "Left columns 10x": (35, 100, 80),
    "Vault ribs 10x": (45, 55, 105),
}


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


def rgba(color: tuple[int, int, int], alpha: int) -> tuple[int, int, int, int]:
    return (color[0], color[1], color[2], alpha)


def segment_rect_points(line, work_size: tuple[int, int], rect: Rect) -> tuple[Point, Point] | None:
    w = max(1, work_size[0] - 1)
    h = max(1, work_size[1] - 1)
    p0 = (line.segment_px[0][0] / w, line.segment_px[0][1] / h)
    p1 = (line.segment_px[1][0] / w, line.segment_px[1][1] / h)
    clipped = clip_unit_segment(p0, p1)
    if clipped is None:
        return None
    return norm_to_rect(clipped[0], rect), norm_to_rect(clipped[1], rect)


def clip_unit_segment(p0: Point, p1: Point) -> tuple[Point, Point] | None:
    x0, y0 = p0
    x1, y1 = p1
    dx = x1 - x0
    dy = y1 - y0
    t0 = 0.0
    t1 = 1.0
    for p, q in ((-dx, x0), (dx, 1.0 - x0), (-dy, y0), (dy, 1.0 - y0)):
        if abs(p) < 1e-9:
            if q < 0.0:
                return None
            continue
        r = q / p
        if p < 0:
            if r > t1:
                return None
            if r > t0:
                t0 = r
        else:
            if r < t0:
                return None
            if r < t1:
                t1 = r
    return (x0 + t0 * dx, y0 + t0 * dy), (x0 + t1 * dx, y0 + t1 * dy)


def ranked_axes(result: p14.PanelResult, limits: tuple[int, int, int]):
    x_limit, y_limit, z_limit = limits
    x_lines = sorted(result.axes.x, key=line_rank, reverse=True)[:x_limit]
    y_lines = sorted(result.axes.y, key=line_rank, reverse=True)[:y_limit]
    z_lines = sorted(result.axes.z, key=z_depth_score, reverse=True)[:z_limit]
    return x_lines, y_lines, z_lines


def confidence_alpha(line, family: str, clean: bool) -> int:
    span_weight = min(1.0, line.span_px / 900.0)
    support_weight = min(1.0, line.support_count / 850.0)
    base = 48 if not clean else 86
    if family == "Z":
        base += 22
    return int(min(210, base + span_weight * 72 + support_weight * 42))


def draw_endpoint(draw: ImageDraw.ImageDraw, point: Point, fill: tuple[int, int, int, int], radius: int) -> None:
    draw.ellipse((point[0] - radius, point[1] - radius, point[0] + radius, point[1] + radius), fill=fill)


def line_intersection(l1, l2) -> Point | None:
    a1, b1, c1 = l1.equation
    a2, b2, c2 = l2.equation
    det = a1 * b2 - a2 * b1
    if abs(det) < 1e-9:
        return None
    x = (b1 * c2 - b2 * c1) / det
    y = (c1 * a2 - c2 * a1) / det
    if -0.015 <= x <= 1.015 and -0.015 <= y <= 1.015:
        return (min(1.0, max(0.0, x)), min(1.0, max(0.0, y)))
    return None


def dedupe_points(points: list[Point], tolerance: float = 0.012) -> list[Point]:
    selected: list[Point] = []
    for point in points:
        if any(math.hypot(point[0] - other[0], point[1] - other[1]) <= tolerance for other in selected):
            continue
        selected.append(point)
    return selected


def derived_intersections(x_lines, z_lines, limit: int) -> list[Point]:
    points: list[Point] = []
    for x_line in x_lines[:24]:
        for z_line in z_lines[:44]:
            point = line_intersection(x_line, z_line)
            if point is not None and point[1] > 0.25:
                points.append(point)
    points.sort(key=lambda point: (point[1], point[0]))
    return dedupe_points(points)[:limit]


def clean_canvas(size: tuple[int, int]) -> Image.Image:
    img = Image.new("RGBA", size, PAPER + (255,))
    draw = ImageDraw.Draw(img)
    grid_x = max(36, size[0] // 30)
    grid_y = max(36, size[1] // 22)
    for x in range(0, size[0], grid_x):
        draw.line((x, 0, x, size[1]), fill=(211, 203, 185, 88), width=1)
    for y in range(0, size[1], grid_y):
        draw.line((0, y, size[0], y), fill=(211, 203, 185, 78), width=1)
    return img


def render_evidence_image(
    result: p14.PanelResult,
    limits: tuple[int, int, int],
    *,
    clean: bool,
    show_extensions: bool,
    show_intersections: bool,
    dim_source: bool,
) -> Image.Image:
    if clean:
        base = clean_canvas(result.extraction.crop.size)
    else:
        base = result.extraction.crop.convert("RGBA")
        if dim_source:
            base = ImageEnhance.Brightness(base).enhance(0.82)
            base = ImageEnhance.Contrast(base).enhance(0.94)

    rect = (0, 0, base.width, base.height)
    work_size = p14.extraction_work_size(result.extraction.crop, result.spec.processing_width)
    x_lines, y_lines, z_lines = ranked_axes(result, limits)

    overlay = Image.new("RGBA", base.size, (0, 0, 0, 0))
    draw = ImageDraw.Draw(overlay)
    vp = norm_to_rect(result.extraction.vp_norm, rect)
    if 0 <= vp[1] <= base.height:
        draw.line((0, vp[1], base.width, vp[1]), fill=rgba(GOLD, 125 if clean else 75), width=2)
    if 0 <= vp[0] <= base.width and 0 <= vp[1] <= base.height:
        draw.ellipse((vp[0] - 8, vp[1] - 8, vp[0] + 8, vp[1] + 8), fill=rgba(Z_RED, 235))

    families = [
        ("X", x_lines, X_BLUE),
        ("Y", y_lines, Y_GREEN),
        ("Z", z_lines, Z_RED),
    ]
    for family, lines, color in families:
        for index, line in enumerate(lines, 1):
            if show_extensions and family == "Z" and index <= 34:
                clipped = line_box_points(line.equation)
                if clipped is not None:
                    pa = norm_to_rect(clipped[0], rect)
                    pb = norm_to_rect(clipped[1], rect)
                    draw.line((pa[0], pa[1], pb[0], pb[1]), fill=rgba(GOLD, 34 if clean else 22), width=1)

            points = segment_rect_points(line, work_size, rect)
            if points is None:
                continue
            p0, p1 = points
            alpha = confidence_alpha(line, family, clean)
            width = 2 if clean else 1
            if family == "Z" and index <= 20:
                width += 1
            draw.line((p0[0], p0[1], p1[0], p1[1]), fill=rgba(color, alpha), width=width)
            if index <= 80 or clean:
                dot_radius = 3 if clean else 2
                dot_alpha = min(245, alpha + 40)
                draw_endpoint(draw, p0, rgba(color, dot_alpha), dot_radius)
                draw_endpoint(draw, p1, rgba(color, dot_alpha), dot_radius)

    if show_intersections:
        intersections = derived_intersections(x_lines, z_lines, 220 if clean else 120)
        for point in intersections:
            px = norm_to_rect(point, rect)
            draw_endpoint(draw, px, rgba(ORANGE, 205 if clean else 150), 3 if clean else 2)

    return Image.alpha_composite(base, overlay)


def draw_panel_frame(draw: ImageDraw.ImageDraw, rect: Rect, title: str, dark: bool) -> None:
    draw.rectangle(rect, fill=PANEL if dark else PAPER, outline=FRAME, width=2)
    draw.text((rect[0] + 14, rect[1] + 12), title, font=LABEL_FONT, fill=WHITE if dark else INK)


def paste_image(board: Image.Image, image: Image.Image, panel: Rect, top_pad: int = 48) -> Rect:
    thumb = fit_image(image, (panel[2] - panel[0] - 28, panel[3] - panel[1] - top_pad - 14))
    image_rect = panel_image_rect(panel, thumb, top_pad=top_pad)
    board.paste(thumb.convert("RGBA"), (image_rect[0], image_rect[1]))
    return image_rect


def draw_legend(draw: ImageDraw.ImageDraw, panel: Rect, dark: bool, counts: tuple[int, int, int]) -> None:
    x = panel[0] + 18
    y = panel[3] - 132
    fill = WHITE if dark else INK
    entries = [
        (X_BLUE, f"X source segments: {counts[0]}"),
        (Y_GREEN, f"Y source segments: {counts[1]}"),
        (Z_RED, f"Z source segments: {counts[2]}"),
        (ORANGE, "derived X/Z intersections"),
        (GOLD, "horizon / equation extensions"),
        (GRAY, "rule: no hand-drawn structure"),
    ]
    for index, (color, text) in enumerate(entries):
        yy = y + index * 19
        draw.rectangle((x, yy + 3, x + 12, yy + 15), fill=color)
        draw.text((x + 18, yy), text, font=SMALL_FONT, fill=fill)


def draw_detail_panel(board: Image.Image, draw: ImageDraw.ImageDraw, result: p14.PanelResult, panel: Rect) -> None:
    title = result.spec.title.upper()
    limits = DETAIL_LIMITS.get(result.spec.title, (45, 55, 90))
    counts = tuple(len(lines) for lines in ranked_axes(result, limits))
    draw_panel_frame(draw, panel, f"{title} - EVIDENCE LOCKED {counts[0]}/{counts[1]}/{counts[2]}", dark=True)

    inner_gap = 20
    top_pad = 48
    usable = (panel[0] + 14, panel[1] + top_pad, panel[2] - 14, panel[3] - 58)
    half_w = (usable[2] - usable[0] - inner_gap) // 2
    left_box = (usable[0], usable[1], usable[0] + half_w, usable[3])
    right_box = (usable[0] + half_w + inner_gap, usable[1], usable[2], usable[3])

    source_img = render_evidence_image(result, limits, clean=False, show_extensions=False, show_intersections=True, dim_source=True)
    clean_img = render_evidence_image(result, limits, clean=True, show_extensions=True, show_intersections=True, dim_source=False)
    paste_image(board, source_img, (left_box[0] - 6, left_box[1] - 36, left_box[2] + 6, left_box[3] + 6), top_pad=26)
    paste_image(board, clean_img, (right_box[0] - 6, right_box[1] - 36, right_box[2] + 6, right_box[3] + 6), top_pad=26)
    draw = ImageDraw.Draw(board)
    draw.text((panel[0] + 16, panel[3] - 42), result.spec.focus, font=SMALL_FONT, fill=(210, 203, 190))
    draw.text(
        (panel[0] + 16, panel[3] - 23),
        f"source-left / vector-right | {result.spec.processing_width}px process | no invented strokes",
        font=SMALL_FONT,
        fill=(176, 169, 156),
    )


def write_manifest(results: list[p14.PanelResult]) -> None:
    lines = [
        "# P17 LACMA Gothic Cathedral Evidence-Locked Reconstruction Data",
        "",
        "P17 corrects the failed P16 semantic scaffold by forbidding hand-curated geometry. Every visible stroke is a detected source segment or an X/Z equation-derived intersection.",
        "",
        f"- Source page: {SOURCE_URL}",
        f"- Source image URL: {SOURCE_IMAGE_URL}",
        f"- Source file: `{REF_ROOT.relative_to(OUT_ROOT.parents[3]) / SOURCE_FILENAME}`",
        "",
    ]
    for result in results:
        limits = FULL_LIMITS if result is results[0] else DETAIL_LIMITS.get(result.spec.title, (45, 55, 90))
        x_lines, y_lines, z_lines = ranked_axes(result, limits)
        intersections = derived_intersections(x_lines, z_lines, 220)
        work_size = p14.extraction_work_size(result.extraction.crop, result.spec.processing_width)
        lines.extend(
            [
                f"## {result.spec.title}",
                f"- Focus: {result.spec.focus}",
                f"- Processing width/height: `{work_size[0]} x {work_size[1]}`",
                f"- Solved VP: `({result.extraction.vp_norm[0]:.6f}, {result.extraction.vp_norm[1]:.6f})`",
                f"- Displayed evidence-locked lines: `{len(x_lines)}` X, `{len(y_lines)}` Y, `{len(z_lines)}` Z",
                f"- Derived X/Z intersections displayed: `{len(intersections)}`",
                f"- Hough lines kept before display filtering: `{len(result.extraction.lines)}`",
                "",
            ]
        )
        for family_name, family_lines in (("X", x_lines), ("Y", y_lines), ("Z", z_lines)):
            lines.append(f"### {family_name} source segments")
            for index, line in enumerate(family_lines, 1):
                p0, p1 = line.segment_px
                n0 = (p0[0] / max(1, work_size[0] - 1), p0[1] / max(1, work_size[1] - 1))
                n1 = (p1[0] / max(1, work_size[0] - 1), p1[1] / max(1, work_size[1] - 1))
                a, b, c = line.equation
                lines.append(
                    f"- {family_name}{index}: endpoints `({n0[0]:.6f}, {n0[1]:.6f}) -> ({n1[0]:.6f}, {n1[1]:.6f})`; "
                    f"angle `{line.angle_deg:+.3f} deg`; equation `{a:.8f}x + {b:.8f}y + {c:.8f} = 0`; "
                    f"support `{line.support_count}`; span `{line.span_px:.1f}px`; residual `{line.residual_to_vp_px:.3f}px`"
                )
            lines.append("")
    MEASUREMENT_MANIFEST.write_text("\n".join(lines), encoding="utf-8")


def build_board() -> None:
    OUT_ROOT.mkdir(parents=True, exist_ok=True)
    REVIEW_ROOT.mkdir(parents=True, exist_ok=True)
    results = p15.build_results()
    full = results[0]
    details = results[1:]

    width = 3800
    margin = 64
    header_h = 164
    top_h = 1020
    row_gap = 38
    panel_gap = 46
    detail_h = 570
    detail_gap = 34
    footer_h = 84
    height = header_h + top_h + row_gap + detail_h * 2 + detail_gap + footer_h + margin

    board = Image.new("RGBA", (width, height), BG + (255,))
    draw = ImageDraw.Draw(board)
    draw.text((margin, 30), "P17 Evidence-Locked Perspective Reconstruction", font=TITLE_FONT, fill=WHITE)
    draw.text(
        (margin, 84),
        "Every visible stroke is source-derived: detected line segment, equation extension, endpoint dot, or X/Z intersection. No hand-made scaffold geometry.",
        font=SUB_FONT,
        fill=(205, 199, 188),
    )
    draw.text(
        (margin, 116),
        "This corrects the P16 failure by keeping semantic interpretation out until the evidence layer is clean.",
        font=SMALL_FONT,
        fill=(181, 174, 160),
    )

    top_w = (width - margin * 2 - panel_gap) // 2
    left = (margin, header_h, margin + top_w, header_h + top_h)
    right = (margin + top_w + panel_gap, header_h, margin + top_w * 2 + panel_gap, header_h + top_h)
    draw_panel_frame(draw, left, "FULL SOURCE + EVIDENCE-LOCKED SEGMENTS", dark=True)
    source_full = render_evidence_image(full, FULL_LIMITS, clean=False, show_extensions=False, show_intersections=True, dim_source=True)
    paste_image(board, source_full, left, top_pad=50)
    draw_legend(draw, left, dark=True, counts=tuple(len(lines) for lines in ranked_axes(full, FULL_LIMITS)))

    draw_panel_frame(draw, right, "VECTOR-ONLY RECONSTRUCTION FROM SAME SOURCE SEGMENTS", dark=False)
    clean_full = render_evidence_image(full, FULL_LIMITS, clean=True, show_extensions=True, show_intersections=True, dim_source=False)
    paste_image(board, clean_full, right, top_pad=50)
    draw_legend(draw, right, dark=False, counts=tuple(len(lines) for lines in ranked_axes(full, FULL_LIMITS)))

    start_y = header_h + top_h + row_gap
    detail_w = (width - margin * 2 - detail_gap * 2) // 3
    for index, result in enumerate(details):
        row = index // 3
        col = index % 3
        x0 = margin + col * (detail_w + detail_gap)
        y0 = start_y + row * (detail_h + detail_gap)
        panel = (x0, y0, x0 + detail_w, y0 + detail_h)
        draw_detail_panel(board, ImageDraw.Draw(board), result, panel)

    if len(details) < 6:
        index = len(details)
        row = index // 3
        col = index % 3
        x0 = margin + col * (detail_w + detail_gap)
        y0 = start_y + row * (detail_h + detail_gap)
        panel = (x0, y0, x0 + detail_w, y0 + detail_h)
        draw = ImageDraw.Draw(board)
        draw_panel_frame(draw, panel, "PROCESS RULES", dark=False)
        rules = [
            "1. Source segments only.",
            "2. Endpoint dots expose actual detected references.",
            "3. Orange points are equation-derived intersections.",
            "4. Gold extensions are faint and marked as extensions.",
            "5. No guessed arches, curves, or columns.",
            "6. Semantic labels happen after this evidence layer is approved.",
        ]
        for i, rule in enumerate(rules):
            draw.text((panel[0] + 28, panel[1] + 78 + i * 42), rule, font=ROW_FONT, fill=INK)

    footer_y = height - margin - footer_h + 10
    draw = ImageDraw.Draw(board)
    draw.text(
        (margin, footer_y),
        "P17 result: this is the evidence layer to judge before any semantic redraw. If approved, P18 labels and traces structure from this layer.",
        font=ROW_FONT,
        fill=WHITE,
    )
    draw.text((margin, footer_y + 36), SOURCE_URL, font=SMALL_FONT, fill=(205, 199, 188))

    write_manifest(results)
    board.convert("RGB").save(DOC_IMAGE, optimize=True)
    shutil.copy2(DOC_IMAGE, REVIEW_IMAGE)
    print(DOC_IMAGE)
    print(REVIEW_IMAGE)
    print(MEASUREMENT_MANIFEST)


if __name__ == "__main__":
    build_board()
