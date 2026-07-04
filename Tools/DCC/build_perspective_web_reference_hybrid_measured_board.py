#!/usr/bin/env python3
"""Build a hybrid measured perspective redraw board.

P07 combines the lessons from P05 and P06:
- P05: source-edge redraws preserve the actual visual silhouette.
- P06: classified Hough spans keep the math clean and auditable.

The right panel uses a faint source-edge redraw as the visual underdrawing,
then overlays the clean measured vector spans and VP formulas.
"""

from __future__ import annotations

import shutil
from pathlib import Path

from PIL import Image, ImageDraw, ImageFont

from build_perspective_web_reference_measured_vector_board import (
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
    draw_formula_key,
    draw_measured_overlay,
    extract,
    fit_image,
    panel_image_rect,
    resize_for_processing,
    structural_classes,
    displayed_perspective,
)
from build_perspective_web_reference_pixel_lineart_board import make_line_art


BOARD_NAME = "P07_WebPerspectiveHybridMeasuredRedrawBoard"
DOC_IMAGE = OUT_ROOT / f"{BOARD_NAME}.png"
REVIEW_IMAGE = REVIEW_ROOT / f"{BOARD_NAME}.png"
MEASUREMENT_MANIFEST = OUT_ROOT / f"{BOARD_NAME}_Measurements.md"


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


def soften_line_art(line_art: Image.Image) -> Image.Image:
    paper = Image.new("RGB", line_art.size, PAPER)
    return Image.blend(line_art.convert("RGB"), paper, 0.46)


def write_measurements(extractions) -> None:
    lines = [
        "# P07 Hybrid Measured Perspective Redraw Data",
        "",
        "P07 combines a faint source-edge redraw with classified measured Hough line spans.",
        "The underdrawing is source-derived edge line art; the overlay lines are source-pixel Hough detections with explicit angles/equations.",
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
                f"- Overlay lines: `{len(perspective)}` perspective, `{len(verticals)}` vertical, `{len(horizontals)}` horizontal, `{len(diagonals)}` secondary diagonal",
                "- Displayed perspective lines:",
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
                f"votes `{line.votes}`; support `{line.support_count}`; residual `{line.residual_to_vp_px:.3f}px`"
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
    draw.text((margin, 34), "P07 Web Perspective Hybrid Measured Redraws", font=TITLE_FONT, fill=WHITE)
    draw.text(
        (margin, 91),
        "Left: source crop with measured spans. Right: source-edge redraw underdrawing plus clean measured vector math.",
        font=SUB_FONT,
        fill=(205, 199, 188),
    )
    draw.text(
        (margin, 121),
        "This keeps the actual silhouette from the source pixels while removing generic invented geometry.",
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
        draw_panel(draw, right, "HYBRID REDRAW: SOURCE-EDGE UNDERLAY + MEASURED VECTORS", dark=False)

        source_thumb = fit_image(extraction.crop, (left[2] - left[0] - 28, left[3] - left[1] - 60))
        source_rect = panel_image_rect(left, source_thumb)
        board.paste(source_thumb, (source_rect[0], source_rect[1]))
        draw_measured_overlay(draw, extraction, source_rect, dark=True, clean=False)

        line_art = soften_line_art(make_line_art(extraction.crop, extraction.spec))
        line_thumb = fit_image(line_art, (right[2] - right[0] - 28, right[3] - right[1] - 60))
        redraw_rect = panel_image_rect(right, line_thumb)
        board.paste(line_thumb, (redraw_rect[0], redraw_rect[1]))
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
