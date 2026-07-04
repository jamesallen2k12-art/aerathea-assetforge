#!/usr/bin/env python3
"""Build a strict source-measured line-art perspective board.

This board keeps the visual comparison close by redrawing each reference as
source-derived edge line art, then overlays the same detected perspective line
measurements used to solve the vanishing point.
"""

from __future__ import annotations

import shutil
from pathlib import Path

from PIL import Image, ImageDraw, ImageFilter, ImageFont, ImageOps

from build_perspective_web_reference_pixel_measured_board import (
    BG,
    FRAME,
    GOLD,
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
    ReferenceSpec,
    crop_source,
    draw_detected_line,
    draw_tag,
    extract,
    fit_image,
    normalized_to_rect,
    panel_image_rect,
    percentile_threshold,
    resize_for_processing,
)


BOARD_NAME = "P05_WebPerspectivePixelLineArtMeasuredBoard"
DOC_IMAGE = OUT_ROOT / f"{BOARD_NAME}.png"
REVIEW_IMAGE = REVIEW_ROOT / f"{BOARD_NAME}.png"
MEASUREMENT_MANIFEST = OUT_ROOT / f"{BOARD_NAME}_Measurements.md"

PAPER = (238, 232, 216)
INK_LIGHT = (67, 62, 54)


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


def make_line_art(source: Image.Image, spec: ReferenceSpec) -> Image.Image:
    gray = ImageOps.grayscale(source)
    gray = ImageOps.autocontrast(gray, cutoff=1)
    edges = gray.filter(ImageFilter.FIND_EDGES)
    edges = ImageOps.autocontrast(edges, cutoff=1)

    edge_threshold = percentile_threshold(edges, max(87.0, spec.edge_percentile - 7.0))
    edge_mask = edges.point(lambda p: 255 if p >= edge_threshold else 0, mode="L")
    mask = edge_mask.filter(ImageFilter.MaxFilter(3))

    base = Image.new("RGB", source.size, PAPER)
    ink_layer = Image.new("RGB", source.size, INK_LIGHT)
    base.paste(ink_layer, mask=mask)
    return base


def draw_panel(draw: ImageDraw.ImageDraw, rect: tuple[int, int, int, int], title: str, dark: bool) -> None:
    draw.rectangle(rect, fill=PANEL if dark else PAPER, outline=FRAME, width=2)
    draw.text((rect[0] + 14, rect[1] + 13), title, font=LABEL_FONT, fill=WHITE if dark else INK)


def display_lines(extraction: Extraction) -> list[DetectedLine]:
    ranked = sorted(
        extraction.perspective_lines,
        key=lambda line: (line.residual_to_vp_px, -line.span_px, -line.votes),
    )
    return ranked[:6]


def draw_measurements(
    draw: ImageDraw.ImageDraw,
    extraction: Extraction,
    rect: tuple[int, int, int, int],
    dark: bool,
) -> None:
    work_size = resize_for_processing(extraction.crop).size
    vp = normalized_to_rect(extraction.vp_norm, rect)
    draw.line((rect[0], vp[1], rect[2], vp[1]), fill=GOLD, width=2)
    draw.ellipse((vp[0] - 6, vp[1] - 6, vp[0] + 6, vp[1] + 6), fill=RED)
    draw_tag(draw, (vp[0] + 8, vp[1] - 17), f"VP {extraction.vp_norm[0]:.3f},{extraction.vp_norm[1]:.3f}", RED, dark)
    for index, line in enumerate(display_lines(extraction), 1):
        draw_detected_line(
            draw,
            line,
            rect,
            work_size,
            RED,
            f"L{index} {line.angle_deg:+.1f} deg",
            dark,
            width=3,
            extend=True,
        )


def write_measurements(extractions: list[Extraction]) -> None:
    lines = [
        "# P05 Pixel Line-Art Perspective Measurements",
        "",
        "Right-side redraws are generated from source edge pixels, then overlaid with detected perspective lines.",
        "The perspective lines are pixel-derived Hough detections; gold strokes are mathematical extensions of those detected line equations.",
        "",
    ]
    for index, extraction in enumerate(extractions, 1):
        spec = extraction.spec
        lines.extend(
            [
                f"## {index}. {spec.title}",
                f"- Source file: `{REF_ROOT.relative_to(OUT_ROOT.parents[3]) / spec.filename}`",
                f"- Display crop: `{spec.crop}`",
                f"- Solved VP: `({extraction.vp_norm[0]:.6f}, {extraction.vp_norm[1]:.6f})`",
                f"- VP residual mean/max: `{extraction.mean_residual_px:.3f}px` / `{extraction.max_residual_px:.3f}px`",
                "- Displayed measurement lines:",
            ]
        )
        work = resize_for_processing(extraction.crop)
        for line_index, line in enumerate(display_lines(extraction), 1):
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
    draw.text((margin, 34), "P05 Web Perspective Pixel-Line Redraws", font=TITLE_FONT, fill=WHITE)
    draw.text(
        (margin, 91),
        "Left: downloaded source crop with measured perspective extensions. Right: source-edge line redraw with the same math overlay.",
        font=SUB_FONT,
        fill=(205, 199, 188),
    )
    draw.text(
        (margin, 121),
        "No generic geometry is invented here: the visible line art and the red measured spans come from the source pixels.",
        font=SMALL_FONT,
        fill=(181, 174, 160),
    )

    y = header_h
    for index, extraction in enumerate(extractions, 1):
        left = (margin, y + 48, margin + panel_w, y + 48 + panel_h)
        right = (margin + panel_w + panel_gap, y + 48, margin + panel_w * 2 + panel_gap, y + 48 + panel_h)
        draw.text(
            (margin, y + 7),
            f"{index}. {extraction.spec.title} - measured VP ({extraction.vp_norm[0]:.3f}, {extraction.vp_norm[1]:.3f}) - residual {extraction.mean_residual_px:.1f}px",
            font=ROW_FONT,
            fill=WHITE,
        )

        draw_panel(draw, left, "SOURCE + MEASURED PERSPECTIVE LINES", dark=True)
        draw_panel(draw, right, "SOURCE-EDGE LINE REDRAW + SAME MEASUREMENTS", dark=False)

        source_thumb = fit_image(extraction.crop, (left[2] - left[0] - 28, left[3] - left[1] - 60))
        source_rect = panel_image_rect(left, source_thumb)
        board.paste(source_thumb, (source_rect[0], source_rect[1]))
        draw_measurements(draw, extraction, source_rect, dark=True)

        line_art = make_line_art(crop_source(extraction.spec), extraction.spec)
        line_art_thumb = fit_image(line_art, (right[2] - right[0] - 28, right[3] - right[1] - 60))
        redraw_rect = panel_image_rect(right, line_art_thumb)
        board.paste(line_art_thumb, (redraw_rect[0], redraw_rect[1]))
        draw_measurements(draw, extraction, redraw_rect, dark=False)
        y += row_h + row_gap

    write_measurements(extractions)
    board.save(DOC_IMAGE, optimize=True)
    shutil.copy2(DOC_IMAGE, REVIEW_IMAGE)
    print(DOC_IMAGE)
    print(REVIEW_IMAGE)
    print(MEASUREMENT_MANIFEST)


if __name__ == "__main__":
    build_board()
