#!/usr/bin/env python3
"""Build P13: single high-resolution web reference X/Y/Z perspective board.

This pass applies the P12 process to a new high-resolution web source:
- source image is downloaded from LACMA at 2560 x 1981 px;
- processing width increases to 1800 px;
- Hough candidates and visible axis references are expanded;
- output keeps source, measured overlay, and source-edge redraw side by side.
"""

from __future__ import annotations

import shutil
from dataclasses import dataclass
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
    WHITE,
    fit_image,
    make_line_art,
    panel_image_rect,
    soften_line_art,
)
from build_perspective_web_reference_pixel_measured_board import (
    DetectedLine,
    ReferenceSpec,
    draw_tag,
    normalized_to_rect,
)
from build_perspective_web_reference_xyz_axis_highres_board import (
    X_BLUE,
    Y_GREEN,
    Z_RED,
    GOLD,
    choose_unique,
    draw_axis_line,
    is_horizontal,
    is_vertical,
    line_rank,
)
from build_perspective_web_reference_z_axis_board import screen_axis_penalty, z_depth_score


BOARD_NAME = "P13_LACMAGothicCathedralHighResXYZPerspectiveBoard"
DOC_IMAGE = OUT_ROOT / f"{BOARD_NAME}.png"
REVIEW_IMAGE = REVIEW_ROOT / f"{BOARD_NAME}.png"
MEASUREMENT_MANIFEST = OUT_ROOT / f"{BOARD_NAME}_Measurements.md"

SOURCE_URL = "https://collections.lacma.org/node/229641"
SOURCE_IMAGE_URL = "https://collections-images.lacma.org/images/13736/13736-1-primary.webp"

SOURCE_SPEC = ReferenceSpec(
    "LACMA Gothic Cathedral Interior",
    "REF_Perspective_GothicCathedral_LACMA_229641.webp",
    (0.01, 0.015, 0.99, 0.985),
    (0.585, 0.695),
    96.4,
    260,
    28,
    0.095,
    0.085,
)

PROCESSING_WIDTH = 1800
MAX_AXIS_LINES = 16


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
ROW_FONT = load_font(22, True)
LABEL_FONT = load_font(14, True)
SMALL_FONT = load_font(12)


@dataclass(frozen=True)
class AxisSet:
    x: list[DetectedLine]
    y: list[DetectedLine]
    z: list[DetectedLine]


def highres_extract(spec: ReferenceSpec):
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


def axis_lines_dense(extraction) -> AxisSet:
    perspective_ids = {id(line) for line in extraction.perspective_lines}
    others = [line for line in extraction.lines if id(line) not in perspective_ids]
    x_lines = choose_unique(
        sorted([line for line in others if is_horizontal(line)], key=line_rank, reverse=True),
        MAX_AXIS_LINES,
        theta_tol=2,
        rho_tol=18.0,
    )
    y_lines = choose_unique(
        sorted([line for line in others if is_vertical(line)], key=line_rank, reverse=True),
        MAX_AXIS_LINES,
        theta_tol=2,
        rho_tol=18.0,
    )
    z_candidates = [line for line in extraction.perspective_lines if abs(abs(line.angle_deg) - 90.0) > 8.0]
    strong_z = [line for line in z_candidates if screen_axis_penalty(line.angle_deg) >= 8.0]
    source = strong_z if len(strong_z) >= 8 else z_candidates
    z_lines = choose_unique(
        sorted(source, key=z_depth_score, reverse=True),
        MAX_AXIS_LINES,
        theta_tol=2,
        rho_tol=16.0,
    )
    return AxisSet(x_lines, y_lines, sorted(z_lines, key=lambda line: line.angle_deg))


def draw_panel(draw: ImageDraw.ImageDraw, rect: tuple[int, int, int, int], title: str, dark: bool) -> None:
    draw.rectangle(rect, fill=PANEL if dark else PAPER, outline=FRAME, width=2)
    draw.text((rect[0] + 14, rect[1] + 13), title, font=LABEL_FONT, fill=WHITE if dark else INK)


def draw_dense_overlay(
    draw: ImageDraw.ImageDraw,
    extraction,
    axes: AxisSet,
    rect: tuple[int, int, int, int],
    dark: bool,
) -> None:
    work_size = extraction_work_size(extraction.crop)
    vp = normalized_to_rect(extraction.vp_norm, rect)
    draw.line((rect[0], vp[1], rect[2], vp[1]), fill=GOLD, width=1)
    draw.ellipse((vp[0] - 7, vp[1] - 7, vp[0] + 7, vp[1] + 7), fill=Z_RED)
    draw_tag(draw, (vp[0] + 9, vp[1] - 18), f"Z-VP {extraction.vp_norm[0]:.3f},{extraction.vp_norm[1]:.3f}", Z_RED, dark)

    for index, line in enumerate(axes.x, 1):
        draw_axis_line(draw, line, rect, work_size, X_BLUE, f"X{index}", dark, width=2, extend=False)
    for index, line in enumerate(axes.y, 1):
        draw_axis_line(draw, line, rect, work_size, Y_GREEN, f"Y{index}", dark, width=2, extend=False)
    for index, line in enumerate(axes.z, 1):
        width = 4 if screen_axis_penalty(line.angle_deg) >= 18.0 else 3
        draw_axis_line(draw, line, rect, work_size, Z_RED, f"Z{index}", dark, width=width, extend=True)


def draw_axis_key(draw: ImageDraw.ImageDraw, rect: tuple[int, int, int, int]) -> None:
    x = rect[0] + 18
    y = rect[3] - 130
    entries = [
        (X_BLUE, "X axis: width/front plane"),
        (Y_GREEN, "Y axis: height/front plane"),
        (Z_RED, "Z axis: depth/leading lines"),
        (INK, f"Processing width: {PROCESSING_WIDTH} px"),
        (INK, "Expanded candidates: 260 Hough lines / 28 VP lines"),
        (INK, f"Visible target: up to {MAX_AXIS_LINES} / {MAX_AXIS_LINES} / {MAX_AXIS_LINES} axis lines"),
    ]
    for index, (color, text) in enumerate(entries):
        yy = y + index * 19
        draw.rectangle((x, yy + 3, x + 12, yy + 15), fill=color)
        draw.text((x + 18, yy), text, font=SMALL_FONT, fill=INK)


def normalized_endpoint(point, work_size):
    return (point[0] / max(1, work_size[0] - 1), point[1] / max(1, work_size[1] - 1))


def write_measurements(extraction, axes: AxisSet) -> None:
    lines = [
        "# P13 LACMA Gothic Cathedral High-Resolution X/Y/Z Perspective Data",
        "",
        "P13 applies the P12 dense X/Y/Z perspective process to one new high-resolution web reference.",
        "",
        f"- Source page: {SOURCE_URL}",
        f"- Source image URL: {SOURCE_IMAGE_URL}",
        f"- Source file: `{REF_ROOT.relative_to(OUT_ROOT.parents[3]) / SOURCE_SPEC.filename}`",
        f"- Processing width: `{PROCESSING_WIDTH}px`",
        f"- Hough line cap: `{SOURCE_SPEC.max_lines}`",
        f"- VP candidate cap: `{SOURCE_SPEC.max_perspective_lines}`",
        f"- Edge pixels used: `{len(extraction.edge_pixels)}`",
        f"- Hough lines kept: `{len(extraction.lines)}`",
        f"- Visible axis counts: `{len(axes.x)}` X, `{len(axes.y)}` Y, `{len(axes.z)}` Z",
        f"- Z-axis VP: `({extraction.vp_norm[0]:.6f}, {extraction.vp_norm[1]:.6f})`",
        f"- Z residual mean/max: `{extraction.mean_residual_px:.3f}px` / `{extraction.max_residual_px:.3f}px`",
        "",
        "## Displayed Axis Measurements",
        "",
    ]
    work_size = extraction_work_size(extraction.crop)
    for family_name, family_lines in (("X", axes.x), ("Y", axes.y), ("Z", axes.z)):
        lines.append(f"### {family_name} axis")
        for line_index, line in enumerate(family_lines, 1):
            n0 = normalized_endpoint(line.segment_px[0], work_size)
            n1 = normalized_endpoint(line.segment_px[1], work_size)
            a, b, c = line.equation
            lines.append(
                f"- {family_name}{line_index}: endpoints `({n0[0]:.6f}, {n0[1]:.6f}) -> ({n1[0]:.6f}, {n1[1]:.6f})`; "
                f"angle `{line.angle_deg:+.3f} deg`; equation `{a:.8f}x + {b:.8f}y + {c:.8f} = 0`; "
                f"support `{line.support_count}`; span `{line.span_px:.1f}px`; residual `{line.residual_to_vp_px:.3f}px`"
            )
        lines.append("")
    MEASUREMENT_MANIFEST.write_text("\n".join(lines), encoding="utf-8")


def build_board() -> None:
    OUT_ROOT.mkdir(parents=True, exist_ok=True)
    REVIEW_ROOT.mkdir(parents=True, exist_ok=True)
    extraction = highres_extract(SOURCE_SPEC)
    axes = axis_lines_dense(extraction)

    width = 3200
    margin = 64
    header_h = 160
    panel_gap = 46
    panel_w = (width - margin * 2 - panel_gap) // 2
    panel_h = 1220
    footer_h = 92
    height = header_h + panel_h + footer_h + margin

    board = Image.new("RGB", (width, height), BG)
    draw = ImageDraw.Draw(board)
    draw.text((margin, 34), "P13 LACMA Gothic Cathedral High-Resolution X/Y/Z Perspective", font=TITLE_FONT, fill=WHITE)
    draw.text(
        (margin, 90),
        "Left: downloaded high-res source with dense measured axes. Right: source-edge redraw with the same measured construction.",
        font=SUB_FONT,
        fill=(205, 199, 188),
    )
    draw.text(
        (margin, 122),
        f"Applied new process: {PROCESSING_WIDTH}px source processing, expanded Hough candidates, and up to {MAX_AXIS_LINES} references per X/Y/Z family.",
        font=SMALL_FONT,
        fill=(181, 174, 160),
    )

    left = (margin, header_h, margin + panel_w, header_h + panel_h)
    right = (margin + panel_w + panel_gap, header_h, margin + panel_w * 2 + panel_gap, header_h + panel_h)
    draw_panel(draw, left, "SOURCE + HIGH-RES X/Y/Z MEASUREMENTS", dark=True)
    draw_panel(draw, right, "SOURCE-EDGE REDRAW + SAME X/Y/Z CONSTRUCTION", dark=False)

    source_thumb = fit_image(extraction.crop, (left[2] - left[0] - 28, left[3] - left[1] - 62))
    source_rect = panel_image_rect(left, source_thumb)
    board.paste(source_thumb, (source_rect[0], source_rect[1]))
    draw_dense_overlay(draw, extraction, axes, source_rect, dark=True)

    line_art = soften_line_art(make_line_art(extraction.crop, extraction.spec))
    line_thumb = fit_image(line_art, (right[2] - right[0] - 28, right[3] - right[1] - 62))
    redraw_rect = panel_image_rect(right, line_thumb)
    board.paste(line_thumb, (redraw_rect[0], redraw_rect[1]))
    draw_dense_overlay(draw, extraction, axes, redraw_rect, dark=False)
    draw_axis_key(draw, right)

    footer_y = header_h + panel_h + 24
    draw.text(
        (margin, footer_y),
        f"Reference counts: X/Y/Z {len(axes.x)}/{len(axes.y)}/{len(axes.z)}  |  Z-VP ({extraction.vp_norm[0]:.3f}, {extraction.vp_norm[1]:.3f})  |  Source: LACMA public web reference",
        font=ROW_FONT,
        fill=WHITE,
    )
    draw.text((margin, footer_y + 40), SOURCE_URL, font=SMALL_FONT, fill=(205, 199, 188))

    write_measurements(extraction, axes)
    board.save(DOC_IMAGE, optimize=True)
    shutil.copy2(DOC_IMAGE, REVIEW_IMAGE)
    print(DOC_IMAGE)
    print(REVIEW_IMAGE)
    print(MEASUREMENT_MANIFEST)


if __name__ == "__main__":
    build_board()
