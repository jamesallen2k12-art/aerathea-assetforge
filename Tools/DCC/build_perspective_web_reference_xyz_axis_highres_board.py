#!/usr/bin/env python3
"""Build P12: high-resolution X/Y/Z measured axis redraw board.

P12 increases measurement density after P11:
- source processing width increases from the default 940 px to 1500 px;
- Hough line caps are widened;
- visible axis lines increase to 12 X / 12 Y / 12 Z where evidence supports it.
"""

from __future__ import annotations

import shutil
from dataclasses import replace
from pathlib import Path

from PIL import Image, ImageDraw, ImageFont

import build_perspective_web_reference_pixel_measured_board as pixel
from build_perspective_web_reference_hybrid_measured_board import (
    BG,
    FRAME,
    INK,
    OUT_ROOT,
    PANEL,
    PAPER,
    REF_ROOT,
    REVIEW_ROOT,
    SPECS,
    WHITE,
    fit_image,
    make_line_art,
    panel_image_rect,
    soften_line_art,
)
from build_perspective_web_reference_pixel_measured_board import (
    DetectedLine,
    draw_tag,
    normalized_to_rect,
)
from build_perspective_web_reference_z_axis_board import screen_axis_penalty, z_depth_score


BOARD_NAME = "P12_WebPerspectiveXYZAxisHighResMeasuredRedrawBoard"
DOC_IMAGE = OUT_ROOT / f"{BOARD_NAME}.png"
REVIEW_IMAGE = REVIEW_ROOT / f"{BOARD_NAME}.png"
MEASUREMENT_MANIFEST = OUT_ROOT / f"{BOARD_NAME}_Measurements.md"
PROCESSING_WIDTH = 1500

X_BLUE = (47, 112, 190)
Y_GREEN = (58, 143, 84)
Z_RED = (224, 48, 38)
GOLD = (197, 142, 62)
GRAY = (112, 106, 96)


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


TITLE_FONT = load_font(44, True)
SUB_FONT = load_font(19)
ROW_FONT = load_font(23, True)
LABEL_FONT = load_font(15, True)
SMALL_FONT = load_font(12)


def highres_specs():
    specs = []
    for spec in SPECS:
        specs.append(
            replace(
                spec,
                max_lines=max(180, spec.max_lines * 2),
                max_perspective_lines=max(18, spec.max_perspective_lines + 8),
                min_span_ratio=max(0.10, spec.min_span_ratio * 0.72),
                vp_tolerance_ratio=spec.vp_tolerance_ratio * 1.25,
            )
        )
    return specs


def highres_extract(spec):
    original_resize = pixel.resize_for_processing

    def highres_resize(img, target_w=940):
        return original_resize(img, target_w=PROCESSING_WIDTH)

    pixel.resize_for_processing = highres_resize
    try:
        return pixel.extract(spec)
    finally:
        pixel.resize_for_processing = original_resize


def extraction_work_size(image):
    scale = PROCESSING_WIDTH / image.width
    return (PROCESSING_WIDTH, max(1, round(image.height * scale)))


def choose_unique(lines: list[DetectedLine], limit: int, theta_tol: int = 3, rho_tol: float = 22.0) -> list[DetectedLine]:
    selected: list[DetectedLine] = []
    for line in lines:
        if any(
            min(abs(line.theta_index - other.theta_index), 180 - abs(line.theta_index - other.theta_index)) <= theta_tol
            and abs(line.rho - other.rho) <= rho_tol
            for other in selected
        ):
            continue
        selected.append(line)
        if len(selected) >= limit:
            break
    return selected


def line_rank(line: DetectedLine) -> tuple[float, int, int]:
    return (line.span_px, line.support_count, line.votes)


def is_vertical(line: DetectedLine) -> bool:
    return abs(abs(line.angle_deg) - 90.0) <= 8.5


def is_horizontal(line: DetectedLine) -> bool:
    return min(abs(line.angle_deg), abs(abs(line.angle_deg) - 180.0)) <= 8.0


def axis_lines(extraction) -> tuple[list[DetectedLine], list[DetectedLine], list[DetectedLine]]:
    perspective_ids = {id(line) for line in extraction.perspective_lines}
    others = [line for line in extraction.lines if id(line) not in perspective_ids]
    x_lines = choose_unique(
        sorted([line for line in others if is_horizontal(line)], key=line_rank, reverse=True),
        12,
        theta_tol=3,
        rho_tol=24.0,
    )
    y_lines = choose_unique(
        sorted([line for line in others if is_vertical(line)], key=line_rank, reverse=True),
        12,
        theta_tol=3,
        rho_tol=24.0,
    )
    z_candidates = [line for line in extraction.perspective_lines if abs(abs(line.angle_deg) - 90.0) > 8.0]
    strong_z = [line for line in z_candidates if screen_axis_penalty(line.angle_deg) >= 8.0]
    source = strong_z if len(strong_z) >= 6 else z_candidates
    z_lines = choose_unique(
        sorted(source, key=z_depth_score, reverse=True),
        12,
        theta_tol=3,
        rho_tol=20.0,
    )
    return x_lines, y_lines, sorted(z_lines, key=lambda line: line.angle_deg)


def draw_panel(draw: ImageDraw.ImageDraw, rect: tuple[int, int, int, int], title: str, dark: bool) -> None:
    draw.rectangle(rect, fill=PANEL if dark else PAPER, outline=FRAME, width=2)
    draw.text((rect[0] + 14, rect[1] + 13), title, font=LABEL_FONT, fill=WHITE if dark else INK)


def draw_axis_overlay(draw: ImageDraw.ImageDraw, extraction, rect: tuple[int, int, int, int], dark: bool) -> None:
    work_size = extraction_work_size(extraction.crop)
    x_lines, y_lines, z_lines = axis_lines(extraction)
    vp = normalized_to_rect(extraction.vp_norm, rect)
    draw.line((rect[0], vp[1], rect[2], vp[1]), fill=GOLD, width=1)
    draw.ellipse((vp[0] - 7, vp[1] - 7, vp[0] + 7, vp[1] + 7), fill=Z_RED)
    draw_tag(draw, (vp[0] + 9, vp[1] - 18), f"Z-VP {extraction.vp_norm[0]:.3f},{extraction.vp_norm[1]:.3f}", Z_RED, dark)

    for index, line in enumerate(x_lines, 1):
        draw_axis_line(draw, line, rect, work_size, X_BLUE, f"X{index}", dark, width=2, extend=False)
    for index, line in enumerate(y_lines, 1):
        draw_axis_line(draw, line, rect, work_size, Y_GREEN, f"Y{index}", dark, width=2, extend=False)
    for index, line in enumerate(z_lines, 1):
        width = 4 if screen_axis_penalty(line.angle_deg) >= 18.0 else 3
        draw_axis_line(draw, line, rect, work_size, Z_RED, f"Z{index}", dark, width=width, extend=True)


def point_to_rect(point, work_size, rect):
    return (
        rect[0] + (point[0] / max(1, work_size[0] - 1)) * (rect[2] - rect[0]),
        rect[1] + (point[1] / max(1, work_size[1] - 1)) * (rect[3] - rect[1]),
    )


def line_box_points(equation):
    a, b, c = equation
    points = []
    if abs(b) > 1e-9:
        for x in (0.0, 1.0):
            y = -(a * x + c) / b
            if 0.0 <= y <= 1.0:
                points.append((x, y))
    if abs(a) > 1e-9:
        for y in (0.0, 1.0):
            x = -(b * y + c) / a
            if 0.0 <= x <= 1.0:
                points.append((x, y))
    unique = []
    for point in points:
        if not any(abs(point[0] - other[0]) < 1e-5 and abs(point[1] - other[1]) < 1e-5 for other in unique):
            unique.append(point)
    if len(unique) < 2:
        return None
    return unique[0], unique[1]


def norm_to_rect(point, rect):
    return (rect[0] + point[0] * (rect[2] - rect[0]), rect[1] + point[1] * (rect[3] - rect[1]))


def clip_segment_to_unit_box(p0, p1):
    x0, y0 = p0
    x1, y1 = p1
    dx = x1 - x0
    dy = y1 - y0
    t0 = 0.0
    t1 = 1.0
    checks = [(-dx, x0), (dx, 1.0 - x0), (-dy, y0), (dy, 1.0 - y0)]
    for p, q in checks:
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


def draw_axis_line(draw, line, rect, work_size, color, label, dark, width=2, extend=False):
    if extend:
        clipped = line_box_points(line.equation)
        if clipped is not None:
            a, b = clipped
            pa = norm_to_rect(a, rect)
            pb = norm_to_rect(b, rect)
            draw.line((pa[0], pa[1], pb[0], pb[1]), fill=(198, 142, 62), width=1)

    w = max(1, work_size[0] - 1)
    h = max(1, work_size[1] - 1)
    segment = clip_segment_to_unit_box(
        (line.segment_px[0][0] / w, line.segment_px[0][1] / h),
        (line.segment_px[1][0] / w, line.segment_px[1][1] / h),
    )
    if segment is None:
        return
    p0 = norm_to_rect(segment[0], rect)
    p1 = norm_to_rect(segment[1], rect)
    draw.line((p0[0], p0[1], p1[0], p1[1]), fill=color, width=width)
    if label:
        mid = ((p0[0] + p1[0]) * 0.5, (p0[1] + p1[1]) * 0.5)
        draw_tag(draw, mid, label, color, dark)


def draw_axis_key(draw: ImageDraw.ImageDraw, rect: tuple[int, int, int, int]) -> None:
    x = rect[0] + 18
    y = rect[3] - 128
    entries = [
        (X_BLUE, "X axis: width/front plane"),
        (Y_GREEN, "Y axis: height/front plane"),
        (Z_RED, "Z axis: depth/leading lines"),
        (INK, "High-res processing: 1500 px width"),
        (INK, "Expanded candidates: up to 180-220 lines"),
        (INK, "Visible target: up to 12 / 12 / 12 axis lines"),
    ]
    for index, (color, text) in enumerate(entries):
        yy = y + index * 19
        draw.rectangle((x, yy + 3, x + 12, yy + 15), fill=color)
        draw.text((x + 18, yy), text, font=SMALL_FONT, fill=INK)


def write_measurements(extractions) -> None:
    lines = [
        "# P12 High-Resolution X/Y/Z Axis-Family Perspective Redraw Data",
        "",
        "P12 increases processing resolution and candidate counts after P11. It uses 1500 px processing width, expanded Hough candidates, and up to 12 visible X/Y/Z lines per image.",
        "",
    ]
    for index, extraction in enumerate(extractions, 1):
        x_lines, y_lines, z_lines = axis_lines(extraction)
        lines.extend(
            [
                f"## {index}. {extraction.spec.title}",
                f"- Source file: `{REF_ROOT.relative_to(OUT_ROOT.parents[3]) / extraction.spec.filename}`",
                f"- Edge pixels used: `{len(extraction.edge_pixels)}`",
                f"- Hough lines kept: `{len(extraction.lines)}`",
                f"- Visible axis counts: `{len(x_lines)}` X, `{len(y_lines)}` Y, `{len(z_lines)}` Z",
                f"- Z-axis VP: `({extraction.vp_norm[0]:.6f}, {extraction.vp_norm[1]:.6f})`",
                f"- Z residual mean/max: `{extraction.mean_residual_px:.3f}px` / `{extraction.max_residual_px:.3f}px`",
                "- Z-axis measurement lines:",
            ]
        )
        work_size = extraction_work_size(extraction.crop)
        for line_index, line in enumerate(z_lines, 1):
            p0, p1 = line.segment_px
            n0 = (p0[0] / max(1, work_size[0] - 1), p0[1] / max(1, work_size[1] - 1))
            n1 = (p1[0] / max(1, work_size[0] - 1), p1[1] / max(1, work_size[1] - 1))
            a, b, c = line.equation
            lines.append(
                f"  - Z{line_index}: endpoints `({n0[0]:.6f}, {n0[1]:.6f}) -> ({n1[0]:.6f}, {n1[1]:.6f})`; "
                f"angle `{line.angle_deg:+.3f} deg`; equation `{a:.8f}x + {b:.8f}y + {c:.8f} = 0`; "
                f"support `{line.support_count}`; span `{line.span_px:.1f}px`; residual `{line.residual_to_vp_px:.3f}px`"
            )
        lines.append("")
    MEASUREMENT_MANIFEST.write_text("\n".join(lines), encoding="utf-8")


def build_board() -> None:
    OUT_ROOT.mkdir(parents=True, exist_ok=True)
    REVIEW_ROOT.mkdir(parents=True, exist_ok=True)
    extractions = [highres_extract(spec) for spec in highres_specs()]

    width = 3000
    margin = 64
    header_h = 174
    row_h = 700
    row_gap = 44
    panel_gap = 46
    panel_w = (width - margin * 2 - panel_gap) // 2
    panel_h = 630
    height = header_h + len(extractions) * row_h + (len(extractions) - 1) * row_gap + margin

    board = Image.new("RGB", (width, height), BG)
    draw = ImageDraw.Draw(board)
    draw.text((margin, 35), "P12 Web Perspective High-Resolution X/Y/Z Redraws", font=TITLE_FONT, fill=WHITE)
    draw.text(
        (margin, 93),
        "Left: high-res measured source axes. Right: source-edge redraw with denser X/Y/Z construction from higher-resolution evidence.",
        font=SUB_FONT,
        fill=(205, 199, 188),
    )
    draw.text(
        (margin, 124),
        "Applied resolution increase: more pixel evidence, more Hough candidates, more visible axis references with confidence filtering.",
        font=SMALL_FONT,
        fill=(181, 174, 160),
    )

    y = header_h
    for index, extraction in enumerate(extractions, 1):
        x_lines, y_lines, z_lines = axis_lines(extraction)
        left = (margin, y + 50, margin + panel_w, y + 50 + panel_h)
        right = (margin + panel_w + panel_gap, y + 50, margin + panel_w * 2 + panel_gap, y + 50 + panel_h)
        draw.text(
            (margin, y + 8),
            f"{index}. {extraction.spec.title} - high-res X/Y/Z {len(x_lines)}/{len(y_lines)}/{len(z_lines)} - Z-VP ({extraction.vp_norm[0]:.3f}, {extraction.vp_norm[1]:.3f})",
            font=ROW_FONT,
            fill=WHITE,
        )

        draw_panel(draw, left, "SOURCE + HIGH-RES X/Y/Z MEASUREMENTS", dark=True)
        draw_panel(draw, right, "HIGH-RES XYZ REDRAW: MORE AXIS REFERENCES", dark=False)

        source_thumb = fit_image(extraction.crop, (left[2] - left[0] - 28, left[3] - left[1] - 62))
        source_rect = panel_image_rect(left, source_thumb)
        board.paste(source_thumb, (source_rect[0], source_rect[1]))
        draw_axis_overlay(draw, extraction, source_rect, dark=True)

        line_art = soften_line_art(make_line_art(extraction.crop, extraction.spec))
        line_thumb = fit_image(line_art, (right[2] - right[0] - 28, right[3] - right[1] - 62))
        redraw_rect = panel_image_rect(right, line_thumb)
        board.paste(line_thumb, (redraw_rect[0], redraw_rect[1]))
        draw_axis_overlay(draw, extraction, redraw_rect, dark=False)
        draw_axis_key(draw, right)
        y += row_h + row_gap

    write_measurements(extractions)
    board.save(DOC_IMAGE, optimize=True)
    shutil.copy2(DOC_IMAGE, REVIEW_IMAGE)
    print(DOC_IMAGE)
    print(REVIEW_IMAGE)
    print(MEASUREMENT_MANIFEST)


if __name__ == "__main__":
    build_board()
