#!/usr/bin/env python3
"""Build a cleaner measured-vector perspective redraw board.

P05 proved that source-derived redraws match better, but raw edge pixels carry
paper grain, engraving hatching, and paint texture. P06 keeps the strict math:
all redraw strokes are Hough-detected source-pixel line spans, classified into
perspective, vertical, horizontal, and secondary structure.
"""

from __future__ import annotations

import math
import shutil
from pathlib import Path

from PIL import Image, ImageDraw, ImageFont

from build_perspective_web_reference_pixel_measured_board import (
    BG,
    CYAN,
    FRAME,
    GOLD,
    GREEN,
    INK,
    LANCZOS,
    OUT_ROOT,
    PANEL,
    RED,
    REF_ROOT,
    REVIEW_ROOT,
    SPECS,
    WHITE,
    DetectedLine,
    Extraction,
    draw_detected_line,
    draw_tag,
    extract,
    fit_image,
    normalized_to_rect,
    panel_image_rect,
    resize_for_processing,
)


BOARD_NAME = "P06_WebPerspectiveMeasuredVectorRedrawBoard"
DOC_IMAGE = OUT_ROOT / f"{BOARD_NAME}.png"
REVIEW_IMAGE = REVIEW_ROOT / f"{BOARD_NAME}.png"
MEASUREMENT_MANIFEST = OUT_ROOT / f"{BOARD_NAME}_Measurements.md"

PAPER = (238, 232, 216)
BLUE = (57, 119, 182)
ORANGE = (184, 119, 62)
GRAY = (114, 108, 96)
LIGHT_GRID = (168, 184, 188)


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


def folded_angle(angle: float) -> float:
    out = angle
    while out <= -180.0:
        out += 360.0
    while out > 180.0:
        out -= 360.0
    return out


def is_vertical(line: DetectedLine) -> bool:
    return abs(abs(line.angle_deg) - 90.0) <= 8.0


def is_horizontal(line: DetectedLine) -> bool:
    folded = min(abs(line.angle_deg), abs(abs(line.angle_deg) - 180.0))
    return folded <= 7.0


def is_duplicate(line: DetectedLine, selected: list[DetectedLine], theta_tol: int = 4, rho_tol: float = 18.0) -> bool:
    for other in selected:
        theta_delta = min(abs(line.theta_index - other.theta_index), 180 - abs(line.theta_index - other.theta_index))
        if theta_delta <= theta_tol and abs(line.rho - other.rho) <= rho_tol:
            return True
    return False


def choose_unique(lines: list[DetectedLine], limit: int, theta_tol: int = 4, rho_tol: float = 18.0) -> list[DetectedLine]:
    selected: list[DetectedLine] = []
    for line in lines:
        if is_duplicate(line, selected, theta_tol, rho_tol):
            continue
        selected.append(line)
        if len(selected) >= limit:
            break
    return selected


def displayed_perspective(extraction: Extraction) -> list[DetectedLine]:
    ranked = sorted(
        extraction.perspective_lines,
        key=lambda line: (line.residual_to_vp_px, -line.span_px, -line.votes),
    )
    return choose_unique(ranked, 7, theta_tol=3, rho_tol=14.0)


def structural_classes(extraction: Extraction) -> tuple[list[DetectedLine], list[DetectedLine], list[DetectedLine]]:
    perspective_ids = {id(line) for line in extraction.perspective_lines}
    others = [line for line in extraction.lines if id(line) not in perspective_ids]
    verticals = choose_unique(
        sorted([line for line in others if is_vertical(line)], key=lambda line: (-line.span_px, -line.support_count, -line.votes)),
        12,
        theta_tol=3,
        rho_tol=22.0,
    )
    horizontals = choose_unique(
        sorted([line for line in others if is_horizontal(line)], key=lambda line: (-line.span_px, -line.support_count, -line.votes)),
        12,
        theta_tol=3,
        rho_tol=22.0,
    )
    used = {id(line) for line in verticals + horizontals}
    diagonals = choose_unique(
        sorted(
            [
                line
                for line in others
                if id(line) not in used and not is_vertical(line) and not is_horizontal(line) and line.span_px >= min(resize_for_processing(extraction.crop).size) * 0.18
            ],
            key=lambda line: (-line.span_px, -line.support_count, -line.votes),
        ),
        8,
        theta_tol=5,
        rho_tol=24.0,
    )
    return verticals, horizontals, diagonals


def draw_vp_and_horizon(draw: ImageDraw.ImageDraw, extraction: Extraction, rect: tuple[int, int, int, int], dark: bool) -> None:
    vp = normalized_to_rect(extraction.vp_norm, rect)
    draw.line((rect[0], vp[1], rect[2], vp[1]), fill=GOLD, width=2)
    draw.ellipse((vp[0] - 6, vp[1] - 6, vp[0] + 6, vp[1] + 6), fill=RED)
    draw_tag(draw, (vp[0] + 8, vp[1] - 17), f"VP {extraction.vp_norm[0]:.3f},{extraction.vp_norm[1]:.3f}", RED, dark)


def draw_measured_overlay(
    draw: ImageDraw.ImageDraw,
    extraction: Extraction,
    rect: tuple[int, int, int, int],
    dark: bool,
    clean: bool,
) -> None:
    work_size = resize_for_processing(extraction.crop).size
    draw_vp_and_horizon(draw, extraction, rect, dark)
    verticals, horizontals, diagonals = structural_classes(extraction)

    if clean:
        for line in horizontals:
            draw_detected_line(draw, line, rect, work_size, BLUE, None, dark, width=2, extend=False)
        for line in verticals:
            draw_detected_line(draw, line, rect, work_size, GREEN, None, dark, width=2, extend=False)
        for line in diagonals:
            draw_detected_line(draw, line, rect, work_size, GRAY, None, dark, width=1, extend=False)
    else:
        for line in horizontals[:8]:
            draw_detected_line(draw, line, rect, work_size, BLUE, None, dark, width=1, extend=False)
        for line in verticals[:8]:
            draw_detected_line(draw, line, rect, work_size, GREEN, None, dark, width=1, extend=False)

    for index, line in enumerate(displayed_perspective(extraction), 1):
        label = f"L{index} {line.angle_deg:+.1f} deg"
        draw_detected_line(draw, line, rect, work_size, RED, label, dark, width=3, extend=True)


def draw_formula_key(draw: ImageDraw.ImageDraw, rect: tuple[int, int, int, int]) -> None:
    x = rect[0] + 16
    y = rect[3] - 72
    draw.text((x, y), "line: ax + by + c = 0", font=SMALL_FONT, fill=INK)
    draw.text((x, y + 17), "VP: least-squares intersection", font=SMALL_FONT, fill=INK)
    draw.text((x, y + 34), "red spans: detected source pixels", font=SMALL_FONT, fill=INK)


def draw_panel(draw: ImageDraw.ImageDraw, rect: tuple[int, int, int, int], title: str, dark: bool) -> None:
    draw.rectangle(rect, fill=PANEL if dark else PAPER, outline=FRAME, width=2)
    draw.text((rect[0] + 14, rect[1] + 13), title, font=LABEL_FONT, fill=WHITE if dark else INK)


def write_measurements(extractions: list[Extraction]) -> None:
    lines = [
        "# P06 Measured Vector Perspective Redraw Data",
        "",
        "P06 applies the lesson from P05: keep source-pixel measurement, but remove paper grain and texture by redrawing only classified Hough line spans.",
        "Perspective lines, verticals, horizontals, and secondary diagonals are all detected from the downloaded image pixels.",
        "For each perspective line: `ax + by + c = 0`; the vanishing point is the least-squares intersection of selected red lines.",
        "",
    ]
    for index, extraction in enumerate(extractions, 1):
        verticals, horizontals, diagonals = structural_classes(extraction)
        perspective = displayed_perspective(extraction)
        lines.extend(
            [
                f"## {index}. {extraction.spec.title}",
                f"- Source file: `{REF_ROOT.relative_to(OUT_ROOT.parents[3]) / extraction.spec.filename}`",
                f"- Solved VP: `({extraction.vp_norm[0]:.6f}, {extraction.vp_norm[1]:.6f})`",
                f"- VP residual mean/max: `{extraction.mean_residual_px:.3f}px` / `{extraction.max_residual_px:.3f}px`",
                f"- Displayed lines: `{len(perspective)}` perspective, `{len(verticals)}` vertical, `{len(horizontals)}` horizontal, `{len(diagonals)}` secondary diagonal",
                "- Perspective measurement lines:",
            ]
        )
        work = resize_for_processing(extraction.crop)
        for line_index, line in enumerate(perspective, 1):
            p0, p1 = line.segment_px
            n0 = (p0[0] / max(1, work.width - 1), p0[1] / max(1, work.height - 1))
            n1 = (p1[0] / max(1, work.width - 1), p1[1] / max(1, work.height - 1))
            a, b, c = line.equation
            lines.append(
                f"  - L{line_index}: endpoints `({n0[0]:.6f}, {n0[1]:.6f}) -> ({n1[0]:.6f}, {n1[1]:.6f})`; "
                f"angle `{line.angle_deg:+.3f} deg`; equation `{a:.8f}x + {b:.8f}y + {c:.8f} = 0`; "
                f"votes `{line.votes}`; support `{line.support_count}`; span `{line.span_px:.1f}px`; residual `{line.residual_to_vp_px:.3f}px`"
            )
        lines.append("")
    MEASUREMENT_MANIFEST.write_text("\n".join(lines), encoding="utf-8")


def build_board() -> None:
    OUT_ROOT.mkdir(parents=True, exist_ok=True)
    REVIEW_ROOT.mkdir(parents=True, exist_ok=True)
    extractions = [extract(spec) for spec in SPECS]

    width = 2700
    margin = 62
    header_h = 164
    row_h = 620
    row_gap = 40
    panel_gap = 42
    panel_w = (width - margin * 2 - panel_gap) // 2
    panel_h = 555
    height = header_h + len(extractions) * row_h + (len(extractions) - 1) * row_gap + margin

    board = Image.new("RGB", (width, height), BG)
    draw = ImageDraw.Draw(board)
    draw.text((margin, 34), "P06 Web Perspective Measured Vector Redraws", font=TITLE_FONT, fill=WHITE)
    draw.text(
        (margin, 91),
        "Left: source crop with measured spans. Right: clean vector redraw made only from source-detected line equations.",
        font=SUB_FONT,
        fill=(205, 199, 188),
    )
    draw.text(
        (margin, 121),
        "Red = perspective spans + extensions. Green = verticals. Blue = horizontals. Gray = secondary detected structure.",
        font=SMALL_FONT,
        fill=(181, 174, 160),
    )

    y = header_h
    for index, extraction in enumerate(extractions, 1):
        left = (margin, y + 48, margin + panel_w, y + 48 + panel_h)
        right = (margin + panel_w + panel_gap, y + 48, margin + panel_w * 2 + panel_gap, y + 48 + panel_h)
        draw.text(
            (margin, y + 7),
            f"{index}. {extraction.spec.title} - VP ({extraction.vp_norm[0]:.3f}, {extraction.vp_norm[1]:.3f}) - residual {extraction.mean_residual_px:.1f}px",
            font=ROW_FONT,
            fill=WHITE,
        )

        draw_panel(draw, left, "SOURCE + DETECTED MEASUREMENTS", dark=True)
        draw_panel(draw, right, "CLEAN VECTOR REDRAW FROM DETECTED SOURCE LINES", dark=False)

        source_thumb = fit_image(extraction.crop, (left[2] - left[0] - 28, left[3] - left[1] - 60))
        source_rect = panel_image_rect(left, source_thumb)
        board.paste(source_thumb, (source_rect[0], source_rect[1]))
        draw_measured_overlay(draw, extraction, source_rect, dark=True, clean=False)

        redraw_rect = panel_image_rect(right, source_thumb)
        draw.rectangle(redraw_rect, fill=PAPER, outline=FRAME, width=1)
        draw_measured_overlay(draw, extraction, redraw_rect, dark=False, clean=True)
        draw_formula_key(draw, right)
        y += row_h + row_gap

    write_measurements(extractions)
    board.save(DOC_IMAGE, optimize=True)
    shutil.copy2(DOC_IMAGE, REVIEW_IMAGE)
    print(DOC_IMAGE)
    print(REVIEW_IMAGE)
    print(MEASUREMENT_MANIFEST)


if __name__ == "__main__":
    build_board()
