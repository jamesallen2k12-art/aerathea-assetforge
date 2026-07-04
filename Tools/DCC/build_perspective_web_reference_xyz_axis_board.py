#!/usr/bin/env python3
"""Build P11: measured X/Y/Z axis-family perspective redraw board.

P10 correctly emphasized the projected Z-depth leading lines. P11 adds X and Y
back as separate measured axis families:
- X axis: front-facing width lines, near-horizontal in one-point perspective.
- Y axis: height lines, near-vertical in one-point perspective.
- Z axis: receding depth lines converging on the vanishing point.

The goal is not to let X/Y dominate; it is to show the full construction triad
cleanly so later asset drawing can build forms in three dimensions.
"""

from __future__ import annotations

import math
import shutil
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
    SPECS,
    WHITE,
    extract,
    fit_image,
    make_line_art,
    panel_image_rect,
    resize_for_processing,
    soften_line_art,
    structural_classes,
)
from build_perspective_web_reference_pixel_measured_board import (
    DetectedLine,
    draw_detected_line,
    draw_tag,
    normalized_to_rect,
)
from build_perspective_web_reference_z_axis_board import screen_axis_penalty, z_axis_lines


BOARD_NAME = "P11_WebPerspectiveXYZAxisMeasuredRedrawBoard"
DOC_IMAGE = OUT_ROOT / f"{BOARD_NAME}.png"
REVIEW_IMAGE = REVIEW_ROOT / f"{BOARD_NAME}.png"
MEASUREMENT_MANIFEST = OUT_ROOT / f"{BOARD_NAME}_Measurements.md"

X_BLUE = (52, 118, 190)
Y_GREEN = (64, 146, 88)
Z_RED = (220, 52, 42)
GOLD = (197, 142, 62)
MUTED = (128, 124, 116)


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


def draw_panel(draw: ImageDraw.ImageDraw, rect: tuple[int, int, int, int], title: str, dark: bool) -> None:
    draw.rectangle(rect, fill=PANEL if dark else PAPER, outline=FRAME, width=2)
    draw.text((rect[0] + 14, rect[1] + 13), title, font=LABEL_FONT, fill=WHITE if dark else INK)


def line_rank(line: DetectedLine) -> tuple[float, float, int]:
    return (line.span_px, line.support_count, line.votes)


def choose_unique(lines: list[DetectedLine], limit: int, theta_tol: int = 3, rho_tol: float = 18.0) -> list[DetectedLine]:
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


def x_axis_lines(extraction) -> list[DetectedLine]:
    _verticals, horizontals, _diagonals = structural_classes(extraction)
    ranked = sorted(horizontals, key=line_rank, reverse=True)
    return choose_unique(ranked, 7, theta_tol=3, rho_tol=20.0)


def y_axis_lines(extraction) -> list[DetectedLine]:
    verticals, _horizontals, _diagonals = structural_classes(extraction)
    ranked = sorted(verticals, key=line_rank, reverse=True)
    return choose_unique(ranked, 7, theta_tol=3, rho_tol=20.0)


def clipped_z_axis_lines(extraction) -> list[DetectedLine]:
    lines = z_axis_lines(extraction)
    return lines[:8]


def axis_summary(extraction) -> tuple[list[DetectedLine], list[DetectedLine], list[DetectedLine]]:
    return x_axis_lines(extraction), y_axis_lines(extraction), clipped_z_axis_lines(extraction)


def draw_axis_overlay(draw: ImageDraw.ImageDraw, extraction, rect: tuple[int, int, int, int], dark: bool, show_all: bool) -> None:
    work_size = resize_for_processing(extraction.crop).size
    x_lines, y_lines, z_lines = axis_summary(extraction)

    vp = normalized_to_rect(extraction.vp_norm, rect)
    draw.line((rect[0], vp[1], rect[2], vp[1]), fill=GOLD, width=1)
    draw.ellipse((vp[0] - 7, vp[1] - 7, vp[0] + 7, vp[1] + 7), fill=Z_RED)
    draw_tag(draw, (vp[0] + 9, vp[1] - 18), f"Z-VP {extraction.vp_norm[0]:.3f},{extraction.vp_norm[1]:.3f}", Z_RED, dark)

    if show_all:
        for index, line in enumerate(x_lines, 1):
            draw_detected_line(draw, line, rect, work_size, X_BLUE, f"X{index}", dark, width=2, extend=False)
        for index, line in enumerate(y_lines, 1):
            draw_detected_line(draw, line, rect, work_size, Y_GREEN, f"Y{index}", dark, width=2, extend=False)
    else:
        for line in x_lines:
            draw_detected_line(draw, line, rect, work_size, X_BLUE, None, dark, width=1, extend=False)
        for line in y_lines:
            draw_detected_line(draw, line, rect, work_size, Y_GREEN, None, dark, width=1, extend=False)

    for index, line in enumerate(z_lines, 1):
        z_strength = screen_axis_penalty(line.angle_deg)
        width = 4 if z_strength >= 18.0 else 3
        draw_detected_line(draw, line, rect, work_size, Z_RED, f"Z{index} {line.angle_deg:+.1f}", dark, width=width, extend=True)


def draw_axis_key(draw: ImageDraw.ImageDraw, rect: tuple[int, int, int, int]) -> None:
    x = rect[0] + 18
    y = rect[3] - 112
    entries = [
        (X_BLUE, "X axis: front-facing width / horizontal support"),
        (Y_GREEN, "Y axis: height / vertical support"),
        (Z_RED, "Z axis: receding depth / leading lines"),
        (INK, "Z line equation: ax + by + c = 0"),
        (INK, "Z-VP: least-squares intersection"),
    ]
    for index, (color, text) in enumerate(entries):
        yy = y + index * 19
        draw.rectangle((x, yy + 3, x + 12, yy + 15), fill=color)
        draw.text((x + 18, yy), text, font=SMALL_FONT, fill=INK)


def write_measurements(extractions) -> None:
    lines = [
        "# P11 X/Y/Z Axis-Family Perspective Redraw Data",
        "",
        "P11 uses all three projected construction axes: X horizontal/front-width, Y vertical/height, and Z receding/depth.",
        "Z remains the leading perspective family; X and Y are support axes that define the front-facing planes.",
        "",
    ]
    for index, extraction in enumerate(extractions, 1):
        x_lines, y_lines, z_lines = axis_summary(extraction)
        lines.extend(
            [
                f"## {index}. {extraction.spec.title}",
                f"- Source file: `{REF_ROOT.relative_to(OUT_ROOT.parents[3]) / extraction.spec.filename}`",
                f"- Z-axis VP: `({extraction.vp_norm[0]:.6f}, {extraction.vp_norm[1]:.6f})`",
                f"- Axis counts: `{len(x_lines)}` X, `{len(y_lines)}` Y, `{len(z_lines)}` Z",
                f"- Z residual mean/max: `{extraction.mean_residual_px:.3f}px` / `{extraction.max_residual_px:.3f}px`",
                "- Z-axis measurement lines:",
            ]
        )
        work = resize_for_processing(extraction.crop)
        for line_index, line in enumerate(z_lines, 1):
            p0, p1 = line.segment_px
            n0 = (p0[0] / max(1, work.width - 1), p0[1] / max(1, work.height - 1))
            n1 = (p1[0] / max(1, work.width - 1), p1[1] / max(1, work.height - 1))
            a, b, c = line.equation
            lines.append(
                f"  - Z{line_index}: endpoints `({n0[0]:.6f}, {n0[1]:.6f}) -> ({n1[0]:.6f}, {n1[1]:.6f})`; "
                f"angle `{line.angle_deg:+.3f} deg`; equation `{a:.8f}x + {b:.8f}y + {c:.8f} = 0`; "
                f"support `{line.support_count}`; span `{line.span_px:.1f}px`; residual `{line.residual_to_vp_px:.3f}px`"
            )
        lines.append("- X/Y support line counts are recorded visually on the board; they remain secondary to the Z leading family.")
        lines.append("")
    MEASUREMENT_MANIFEST.write_text("\n".join(lines), encoding="utf-8")


def build_board() -> None:
    OUT_ROOT.mkdir(parents=True, exist_ok=True)
    REVIEW_ROOT.mkdir(parents=True, exist_ok=True)
    extractions = [extract(spec) for spec in SPECS]

    width = 2700
    margin = 62
    header_h = 168
    row_h = 635
    row_gap = 40
    panel_gap = 42
    panel_w = (width - margin * 2 - panel_gap) // 2
    panel_h = 570
    height = header_h + len(extractions) * row_h + (len(extractions) - 1) * row_gap + margin

    board = Image.new("RGB", (width, height), BG)
    draw = ImageDraw.Draw(board)
    draw.text((margin, 34), "P11 Web Perspective X/Y/Z Axis-Family Redraws", font=TITLE_FONT, fill=WHITE)
    draw.text(
        (margin, 91),
        "Left: source crop with X/Y/Z measured axes. Right: source-edge redraw with full tri-axis construction overlay.",
        font=SUB_FONT,
        fill=(205, 199, 188),
    )
    draw.text(
        (margin, 121),
        "Applied correction: use all three axes, but keep Z as the depth-leading family and X/Y as support-plane axes.",
        font=SMALL_FONT,
        fill=(181, 174, 160),
    )

    y = header_h
    for index, extraction in enumerate(extractions, 1):
        x_lines, y_lines, z_lines = axis_summary(extraction)
        left = (margin, y + 48, margin + panel_w, y + 48 + panel_h)
        right = (margin + panel_w + panel_gap, y + 48, margin + panel_w * 2 + panel_gap, y + 48 + panel_h)
        draw.text(
            (margin, y + 7),
            f"{index}. {extraction.spec.title} - X/Y/Z counts {len(x_lines)}/{len(y_lines)}/{len(z_lines)} - Z-VP ({extraction.vp_norm[0]:.3f}, {extraction.vp_norm[1]:.3f})",
            font=ROW_FONT,
            fill=WHITE,
        )

        draw_panel(draw, left, "SOURCE + X/Y/Z AXIS MEASUREMENTS", dark=True)
        draw_panel(draw, right, "XYZ REDRAW: EDGE UNDERLAY + TRI-AXIS CONSTRUCTION", dark=False)

        source_thumb = fit_image(extraction.crop, (left[2] - left[0] - 28, left[3] - left[1] - 60))
        source_rect = panel_image_rect(left, source_thumb)
        board.paste(source_thumb, (source_rect[0], source_rect[1]))
        draw_axis_overlay(draw, extraction, source_rect, dark=True, show_all=True)

        line_art = soften_line_art(make_line_art(extraction.crop, extraction.spec))
        line_thumb = fit_image(line_art, (right[2] - right[0] - 28, right[3] - right[1] - 60))
        redraw_rect = panel_image_rect(right, line_thumb)
        board.paste(line_thumb, (redraw_rect[0], redraw_rect[1]))
        draw_axis_overlay(draw, extraction, redraw_rect, dark=False, show_all=True)
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
