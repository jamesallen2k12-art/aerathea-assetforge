#!/usr/bin/env python3
"""Build P10: Z-axis leading-line perspective redraw board.

This pass applies the user's correction: leading lines should follow projected
scene depth (Z axis), not screen-space X/Y support lines. X/Y detections are
suppressed; only measured receding line spans, their extensions, and the solved
vanishing point are emphasized.
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
)
from build_perspective_web_reference_pixel_measured_board import (
    DetectedLine,
    draw_detected_line,
    draw_tag,
    normalized_to_rect,
)


BOARD_NAME = "P10_WebPerspectiveZAxisLeadingLineRedrawBoard"
DOC_IMAGE = OUT_ROOT / f"{BOARD_NAME}.png"
REVIEW_IMAGE = REVIEW_ROOT / f"{BOARD_NAME}.png"
MEASUREMENT_MANIFEST = OUT_ROOT / f"{BOARD_NAME}_Measurements.md"

RED = (220, 52, 42)
GOLD = (197, 142, 62)
MUTED = (136, 132, 124)
Z_FILL = (255, 245, 228)


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


def screen_axis_penalty(angle: float) -> float:
    x_delta = min(abs(angle), abs(abs(angle) - 180.0))
    y_delta = abs(abs(angle) - 90.0)
    return min(x_delta, y_delta)


def z_depth_score(line: DetectedLine) -> float:
    # Strong Z-axis candidates are long, supported, near the VP family, and not
    # merely screen-horizontal or screen-vertical X/Y scaffold lines.
    axis_delta = max(0.0, screen_axis_penalty(line.angle_deg) - 6.0)
    axis_weight = min(1.0, axis_delta / 24.0)
    residual_weight = 1.0 / (1.0 + max(0.0, line.residual_to_vp_px))
    return line.span_px * (1.0 + line.support_count / 500.0) * (0.40 + 0.60 * axis_weight) * residual_weight


def z_axis_lines(extraction) -> list[DetectedLine]:
    candidates = [
        line
        for line in extraction.perspective_lines
        if abs(abs(line.angle_deg) - 90.0) > 8.0
    ]
    strong = [line for line in candidates if screen_axis_penalty(line.angle_deg) >= 10.0]
    source = strong if len(strong) >= 4 else candidates
    ranked = sorted(source, key=z_depth_score, reverse=True)
    selected: list[DetectedLine] = []
    for line in ranked:
        if any(
            min(abs(line.theta_index - other.theta_index), 180 - abs(line.theta_index - other.theta_index)) <= 3
            and abs(line.rho - other.rho) <= 14.0
            for other in selected
        ):
            continue
        selected.append(line)
        if len(selected) >= 8:
            break
    return sorted(selected, key=lambda line: line.angle_deg)


def draw_z_overlay(draw: ImageDraw.ImageDraw, extraction, rect: tuple[int, int, int, int], dark: bool) -> None:
    work_size = resize_for_processing(extraction.crop).size
    vp = normalized_to_rect(extraction.vp_norm, rect)
    draw.line((rect[0], vp[1], rect[2], vp[1]), fill=GOLD, width=1)
    draw.ellipse((vp[0] - 7, vp[1] - 7, vp[0] + 7, vp[1] + 7), fill=RED)
    draw_tag(draw, (vp[0] + 9, vp[1] - 18), f"Z-VP {extraction.vp_norm[0]:.3f},{extraction.vp_norm[1]:.3f}", RED, dark)

    lines = z_axis_lines(extraction)
    for index, line in enumerate(lines, 1):
        axis_delta = screen_axis_penalty(line.angle_deg)
        width = 4 if axis_delta >= 18.0 else 3
        label = f"Z{index} {line.angle_deg:+.1f} deg"
        draw_detected_line(draw, line, rect, work_size, RED, label, dark, width=width, extend=True)


def draw_z_cone(draw: ImageDraw.ImageDraw, extraction, rect: tuple[int, int, int, int]) -> None:
    lines = z_axis_lines(extraction)
    if len(lines) < 2:
        return
    work_size = resize_for_processing(extraction.crop).size
    vp = normalized_to_rect(extraction.vp_norm, rect)
    endpoints: list[tuple[float, float]] = []
    for line in lines:
        for point in line.segment_px:
            x = rect[0] + (point[0] / max(1, work_size[0] - 1)) * (rect[2] - rect[0])
            y = rect[1] + (point[1] / max(1, work_size[1] - 1)) * (rect[3] - rect[1])
            if math.hypot(x - vp[0], y - vp[1]) > 80:
                endpoints.append((x, y))
    if len(endpoints) < 2:
        return
    endpoints.sort(key=lambda p: math.atan2(p[1] - vp[1], p[0] - vp[0]))
    polygon = [vp, endpoints[0], endpoints[-1]]
    overlay = Image.new("RGBA", (rect[2] - rect[0], rect[3] - rect[1]), (0, 0, 0, 0))
    local = ImageDraw.Draw(overlay)
    local.polygon(
        [(p[0] - rect[0], p[1] - rect[1]) for p in polygon],
        fill=(255, 210, 120, 28),
        outline=(220, 52, 42, 95),
    )
    draw.bitmap((rect[0], rect[1]), overlay)


def draw_key(draw: ImageDraw.ImageDraw, rect: tuple[int, int, int, int]) -> None:
    x = rect[0] + 18
    y = rect[3] - 92
    lines = [
        "Z axis = receding scene-depth line family",
        "X/Y support lines suppressed",
        "Z line: ax + by + c = 0",
        "Z-VP: least-squares intersection",
    ]
    for index, text in enumerate(lines):
        draw.text((x, y + index * 18), text, font=SMALL_FONT, fill=INK)


def write_measurements(extractions) -> None:
    lines = [
        "# P10 Z-Axis Leading-Line Perspective Redraw Data",
        "",
        "P10 applies the correction that the review should emphasize projected scene-depth/Z-axis leading lines, not screen-space X/Y lines.",
        "The source-edge underlay remains for visual comparison, but only measured Z-family perspective spans are highlighted and used as the visual guide.",
        "",
    ]
    for index, extraction in enumerate(extractions, 1):
        z_lines = z_axis_lines(extraction)
        lines.extend(
            [
                f"## {index}. {extraction.spec.title}",
                f"- Source file: `{REF_ROOT.relative_to(OUT_ROOT.parents[3]) / extraction.spec.filename}`",
                f"- Z-axis VP: `({extraction.vp_norm[0]:.6f}, {extraction.vp_norm[1]:.6f})`",
                f"- Z-family residual mean/max: `{extraction.mean_residual_px:.3f}px` / `{extraction.max_residual_px:.3f}px`",
                f"- Displayed Z-axis leading lines: `{len(z_lines)}`",
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
                f"angle `{line.angle_deg:+.3f} deg`; screen-axis penalty `{screen_axis_penalty(line.angle_deg):.3f} deg`; "
                f"equation `{a:.8f}x + {b:.8f}y + {c:.8f} = 0`; support `{line.support_count}`; "
                f"span `{line.span_px:.1f}px`; residual `{line.residual_to_vp_px:.3f}px`"
            )
        lines.append("")
    MEASUREMENT_MANIFEST.write_text("\n".join(lines), encoding="utf-8")


def build_board() -> None:
    OUT_ROOT.mkdir(parents=True, exist_ok=True)
    REVIEW_ROOT.mkdir(parents=True, exist_ok=True)
    extractions = [extract(spec) for spec in SPECS]

    width = 2700
    margin = 62
    header_h = 168
    row_h = 625
    row_gap = 40
    panel_gap = 42
    panel_w = (width - margin * 2 - panel_gap) // 2
    panel_h = 560
    height = header_h + len(extractions) * row_h + (len(extractions) - 1) * row_gap + margin

    board = Image.new("RGB", (width, height), BG)
    draw = ImageDraw.Draw(board)
    draw.text((margin, 34), "P10 Web Perspective Z-Axis Leading-Line Redraws", font=TITLE_FONT, fill=WHITE)
    draw.text(
        (margin, 91),
        "Left: source crop with only measured depth/Z leading lines. Right: source-edge redraw with X/Y suppressed and Z emphasized.",
        font=SUB_FONT,
        fill=(205, 199, 188),
    )
    draw.text(
        (margin, 121),
        "Applied correction: solve and show the receding Z-axis family first; use X/Y lines only as hidden support, not visual drivers.",
        font=SMALL_FONT,
        fill=(181, 174, 160),
    )

    y = header_h
    for index, extraction in enumerate(extractions, 1):
        left = (margin, y + 48, margin + panel_w, y + 48 + panel_h)
        right = (margin + panel_w + panel_gap, y + 48, margin + panel_w * 2 + panel_gap, y + 48 + panel_h)
        z_count = len(z_axis_lines(extraction))
        draw.text(
            (margin, y + 7),
            f"{index}. {extraction.spec.title} - Z-VP ({extraction.vp_norm[0]:.3f}, {extraction.vp_norm[1]:.3f}) - {z_count} Z lines",
            font=ROW_FONT,
            fill=WHITE,
        )

        draw_panel(draw, left, "SOURCE + Z-AXIS LEADING LINES ONLY", dark=True)
        draw_panel(draw, right, "Z-AXIS REDRAW: SOURCE-EDGE UNDERLAY, X/Y SUPPRESSED", dark=False)

        source_thumb = fit_image(extraction.crop, (left[2] - left[0] - 28, left[3] - left[1] - 60))
        source_rect = panel_image_rect(left, source_thumb)
        board.paste(source_thumb, (source_rect[0], source_rect[1]))
        draw_z_overlay(draw, extraction, source_rect, dark=True)

        line_art = soften_line_art(make_line_art(extraction.crop, extraction.spec))
        line_thumb = fit_image(line_art, (right[2] - right[0] - 28, right[3] - right[1] - 60))
        redraw_rect = panel_image_rect(right, line_thumb)
        board.paste(line_thumb, (redraw_rect[0], redraw_rect[1]))
        draw_z_overlay(draw, extraction, redraw_rect, dark=False)
        draw_key(draw, right)
        y += row_h + row_gap

    write_measurements(extractions)
    board.save(DOC_IMAGE, optimize=True)
    shutil.copy2(DOC_IMAGE, REVIEW_IMAGE)
    print(DOC_IMAGE)
    print(REVIEW_IMAGE)
    print(MEASUREMENT_MANIFEST)


if __name__ == "__main__":
    build_board()
