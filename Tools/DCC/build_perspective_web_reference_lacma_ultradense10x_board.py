#!/usr/bin/env python3
"""Build P15: ultra-dense 10x LACMA perspective measurement experiment.

P15 intentionally tests the user's request: multiply measurement/reference
density by roughly 10x while keeping endpoint ratios tied to the same
processing dimensions used during extraction. This is an experiment, not the
new baseline.
"""

from __future__ import annotations

import shutil
from dataclasses import replace
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
    make_line_art,
    panel_image_rect,
    soften_line_art,
)
from build_perspective_web_reference_pixel_measured_board import DetectedLine, normalized_to_rect
from build_perspective_web_reference_xyz_axis_highres_board import (
    X_BLUE,
    Y_GREEN,
    Z_RED,
    choose_unique,
    clip_segment_to_unit_box,
    is_horizontal,
    is_vertical,
    line_box_points,
    line_rank,
    norm_to_rect,
)
from build_perspective_web_reference_z_axis_board import screen_axis_penalty, z_depth_score

import build_perspective_web_reference_lacma_clarity_scaffold_board as p14


BOARD_NAME = "P15_LACMAGothicCathedralUltraDense10xMeasurementBoard"
DOC_IMAGE = OUT_ROOT / f"{BOARD_NAME}.png"
REVIEW_IMAGE = REVIEW_ROOT / f"{BOARD_NAME}.png"
MEASUREMENT_MANIFEST = OUT_ROOT / f"{BOARD_NAME}_Measurements.md"

SOURCE_URL = p14.SOURCE_URL
SOURCE_IMAGE_URL = p14.SOURCE_IMAGE_URL
SOURCE_FILENAME = p14.SOURCE_FILENAME

DENSITY_MULTIPLIER = 10

GOLD = (197, 142, 62)
LINE_GRAY = (112, 108, 98)


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


def ultra_panel_specs() -> list[p14.PanelSpec]:
    specs: list[p14.PanelSpec] = []
    for index, spec in enumerate(p14.PANEL_SPECS):
        processing_width = min(2400, round(spec.processing_width * (1.34 if index == 0 else 1.26)))
        specs.append(
            replace(
                spec,
                title=f"{spec.title} 10x",
                processing_width=processing_width,
                edge_percentile=max(94.2, spec.edge_percentile - 1.25),
                max_lines=spec.max_lines * DENSITY_MULTIPLIER,
                max_perspective_lines=spec.max_perspective_lines * DENSITY_MULTIPLIER,
                min_span_ratio=max(0.035, spec.min_span_ratio * 0.52),
                vp_tolerance_ratio=spec.vp_tolerance_ratio * 1.35,
                max_x=spec.max_x * DENSITY_MULTIPLIER,
                max_y=spec.max_y * DENSITY_MULTIPLIER,
                max_z=spec.max_z * DENSITY_MULTIPLIER,
            )
        )
    return specs


def select_axes_ultra(extraction, spec: p14.PanelSpec) -> p14.AxisSet:
    perspective_ids = {id(line) for line in extraction.perspective_lines}
    others = [line for line in extraction.lines if id(line) not in perspective_ids]
    scale = spec.processing_width / 1500.0
    x_lines = choose_unique(
        sorted([line for line in others if is_horizontal(line)], key=line_rank, reverse=True),
        spec.max_x,
        theta_tol=1,
        rho_tol=5.5 * scale,
    )
    y_lines = choose_unique(
        sorted([line for line in others if is_vertical(line)], key=line_rank, reverse=True),
        spec.max_y,
        theta_tol=1,
        rho_tol=5.5 * scale,
    )
    z_candidates = [line for line in extraction.perspective_lines if abs(abs(line.angle_deg) - 90.0) > 5.5]
    strong_z = [line for line in z_candidates if screen_axis_penalty(line.angle_deg) >= 5.5]
    source = strong_z if len(strong_z) >= max(8, spec.max_z // 5) else z_candidates
    z_lines = choose_unique(
        sorted(source, key=z_depth_score, reverse=True),
        spec.max_z,
        theta_tol=1,
        rho_tol=5.0 * scale,
    )
    return p14.AxisSet(x_lines, y_lines, sorted(z_lines, key=lambda line: line.angle_deg))


def build_results() -> list[p14.PanelResult]:
    results: list[p14.PanelResult] = []
    for spec in ultra_panel_specs():
        reference = p14.to_reference_spec(spec)
        extraction = p14.extract_with_width(reference, spec.processing_width)
        axes = select_axes_ultra(extraction, spec)
        results.append(p14.PanelResult(spec, reference, extraction, axes))
    return results


def rgba(color: tuple[int, int, int], alpha: int) -> tuple[int, int, int, int]:
    return (color[0], color[1], color[2], alpha)


def segment_rect_points(line: DetectedLine, work_size: tuple[int, int], rect: tuple[int, int, int, int]):
    w = max(1, work_size[0] - 1)
    h = max(1, work_size[1] - 1)
    segment = clip_segment_to_unit_box(
        (line.segment_px[0][0] / w, line.segment_px[0][1] / h),
        (line.segment_px[1][0] / w, line.segment_px[1][1] / h),
    )
    if segment is None:
        return None
    return norm_to_rect(segment[0], rect), norm_to_rect(segment[1], rect)


def draw_endpoint(draw: ImageDraw.ImageDraw, point: tuple[float, float], fill: tuple[int, int, int, int], radius: int = 2) -> None:
    draw.ellipse((point[0] - radius, point[1] - radius, point[0] + radius, point[1] + radius), fill=fill)


def draw_ultra_axes(
    image: Image.Image,
    result: p14.PanelResult,
    rect: tuple[int, int, int, int],
    labels: bool,
    point_stride: int = 1,
) -> Image.Image:
    base = image.convert("RGBA")
    overlay = Image.new("RGBA", base.size, (0, 0, 0, 0))
    draw = ImageDraw.Draw(overlay)
    work_size = p14.extraction_work_size(result.extraction.crop, result.spec.processing_width)
    vp = normalized_to_rect(result.extraction.vp_norm, rect)
    if rect[1] <= vp[1] <= rect[3]:
        draw.line((rect[0], vp[1], rect[2], vp[1]), fill=rgba(GOLD, 120), width=1)
    if rect[0] <= vp[0] <= rect[2] and rect[1] <= vp[1] <= rect[3]:
        draw.ellipse((vp[0] - 7, vp[1] - 7, vp[0] + 7, vp[1] + 7), fill=rgba(Z_RED, 230))
        if labels:
            draw.text((vp[0] + 10, vp[1] - 18), f"VP {result.extraction.vp_norm[0]:.3f},{result.extraction.vp_norm[1]:.3f}", font=SMALL_FONT, fill=rgba(Z_RED, 255))

    families = [
        (result.axes.x, X_BLUE, 56, 1, False),
        (result.axes.y, Y_GREEN, 58, 1, False),
        (result.axes.z, Z_RED, 86, 1, True),
    ]
    for lines, color, alpha, width, extend in families:
        for line_index, line in enumerate(lines, 1):
            if extend:
                clipped = line_box_points(line.equation)
                if clipped is not None:
                    pa = norm_to_rect(clipped[0], rect)
                    pb = norm_to_rect(clipped[1], rect)
                    draw.line((pa[0], pa[1], pb[0], pb[1]), fill=rgba(GOLD, 34), width=1)

            points = segment_rect_points(line, work_size, rect)
            if points is None:
                continue
            p0, p1 = points
            draw.line((p0[0], p0[1], p1[0], p1[1]), fill=rgba(color, alpha), width=width)
            if line_index % point_stride == 0:
                draw_endpoint(draw, p0, rgba(color, min(200, alpha + 70)), radius=2)
                draw_endpoint(draw, p1, rgba(color, min(200, alpha + 70)), radius=2)

    # Re-emphasize the strongest solved Z references so the ultra-dense field
    # still has a readable convergence family.
    for line in result.axes.z[:28]:
        points = segment_rect_points(line, work_size, rect)
        if points is None:
            continue
        p0, p1 = points
        draw.line((p0[0], p0[1], p1[0], p1[1]), fill=rgba(Z_RED, 178), width=2)

    return Image.alpha_composite(base, overlay)


def draw_panel_frame(draw: ImageDraw.ImageDraw, rect: tuple[int, int, int, int], title: str, dark: bool) -> None:
    draw.rectangle(rect, fill=PANEL if dark else PAPER, outline=FRAME, width=2)
    draw.text((rect[0] + 14, rect[1] + 12), title, font=LABEL_FONT, fill=WHITE if dark else INK)


def paste_panel_image(
    board: Image.Image,
    result: p14.PanelResult,
    panel: tuple[int, int, int, int],
    source: Image.Image,
    labels: bool,
    point_stride: int,
) -> tuple[Image.Image, tuple[int, int, int, int]]:
    thumb = fit_image(source, (panel[2] - panel[0] - 28, panel[3] - panel[1] - 64))
    image_rect = panel_image_rect(panel, thumb)
    board.paste(thumb.convert("RGBA"), (image_rect[0], image_rect[1]))
    board = draw_ultra_axes(board, result, image_rect, labels=labels, point_stride=point_stride)
    return board, image_rect


def draw_key(draw: ImageDraw.ImageDraw, panel: tuple[int, int, int, int], counts: tuple[int, int, int]) -> None:
    x = panel[0] + 18
    y = panel[3] - 126
    entries = [
        (X_BLUE, f"X refs: {counts[0]}"),
        (Y_GREEN, f"Y refs: {counts[1]}"),
        (Z_RED, f"Z refs: {counts[2]}"),
        (INK, "10x caps: Hough, VP candidates, visible references"),
        (INK, "Thin translucent strokes prevent complete overpaint"),
        (INK, "Endpoint dots expose reference-point density"),
    ]
    for index, (color, text) in enumerate(entries):
        yy = y + index * 18
        draw.rectangle((x, yy + 3, x + 12, yy + 15), fill=color)
        draw.text((x + 18, yy), text, font=SMALL_FONT, fill=INK)


def draw_crop_panel(board: Image.Image, draw: ImageDraw.ImageDraw, result: p14.PanelResult, panel: tuple[int, int, int, int]) -> Image.Image:
    counts = (len(result.axes.x), len(result.axes.y), len(result.axes.z))
    title = f"{result.spec.title.upper()} - {counts[0]}/{counts[1]}/{counts[2]} X/Y/Z"
    draw_panel_frame(draw, panel, title, dark=True)
    board, _image_rect = paste_panel_image(board, result, panel, result.extraction.crop, labels=False, point_stride=3)
    draw = ImageDraw.Draw(board)
    footer_y = panel[3] - 42
    draw.text((panel[0] + 16, footer_y), result.spec.focus, font=SMALL_FONT, fill=(210, 203, 190))
    draw.text(
        (panel[0] + 16, footer_y + 18),
        f"{result.spec.processing_width}px | Hough {result.spec.max_lines} | VP candidates {result.spec.max_perspective_lines} | edges {len(result.extraction.edge_pixels)}",
        font=SMALL_FONT,
        fill=(176, 169, 156),
    )
    return board


def normalized_endpoint(point, work_size):
    return (point[0] / max(1, work_size[0] - 1), point[1] / max(1, work_size[1] - 1))


def write_measurements(results: list[p14.PanelResult]) -> None:
    lines = [
        "# P15 LACMA Gothic Cathedral Ultra-Dense 10x Perspective Data",
        "",
        "P15 tests a 10x increase in measurement/reference density. It is an experiment and does not replace the cleaner P13/P14 boards unless visually approved.",
        "",
        f"- Source page: {SOURCE_URL}",
        f"- Source image URL: {SOURCE_IMAGE_URL}",
        f"- Source file: `{REF_ROOT.relative_to(OUT_ROOT.parents[3]) / SOURCE_FILENAME}`",
        f"- Density multiplier: `{DENSITY_MULTIPLIER}x` for Hough caps, VP caps, and visible axis-reference targets.",
        "",
    ]
    for result in results:
        work_size = p14.extraction_work_size(result.extraction.crop, result.spec.processing_width)
        counts = (len(result.axes.x), len(result.axes.y), len(result.axes.z))
        lines.extend(
            [
                f"## {result.spec.title}",
                f"- Focus: {result.spec.focus}",
                f"- Crop: `{result.spec.crop}`",
                f"- Processing width/height: `{work_size[0]} x {work_size[1]}`",
                f"- Edge percentile: `{result.spec.edge_percentile}`",
                f"- Hough line cap: `{result.spec.max_lines}`",
                f"- VP candidate cap: `{result.spec.max_perspective_lines}`",
                f"- Edge pixels: `{len(result.extraction.edge_pixels)}`",
                f"- Hough lines kept: `{len(result.extraction.lines)}`",
                f"- Displayed axes: `{counts[0]}` X, `{counts[1]}` Y, `{counts[2]}` Z",
                f"- Solved VP: `({result.extraction.vp_norm[0]:.6f}, {result.extraction.vp_norm[1]:.6f})`",
                f"- Z residual mean/max: `{result.extraction.mean_residual_px:.3f}px` / `{result.extraction.max_residual_px:.3f}px`",
                "",
            ]
        )
        for family_name, family_lines in (("X", result.axes.x), ("Y", result.axes.y), ("Z", result.axes.z)):
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
    results = build_results()
    full = results[0]
    local_results = results[1:]

    width = 3600
    margin = 64
    header_h = 160
    top_h = 1080
    top_gap = 46
    crop_gap = 34
    crop_panel_w = (width - margin * 2 - crop_gap * 2) // 3
    crop_panel_h = 580
    crop_rows = 2
    footer_h = 74
    height = header_h + top_h + top_gap + crop_rows * crop_panel_h + crop_gap + footer_h + margin

    board = Image.new("RGBA", (width, height), BG + (255,))
    draw = ImageDraw.Draw(board)
    draw.text((margin, 30), "P15 Ultra-Dense 10x Perspective Measurement Experiment", font=TITLE_FONT, fill=WHITE)
    draw.text(
        (margin, 84),
        "Same LACMA source, ratio-safe extraction, but measurement/reference density is multiplied by roughly 10x.",
        font=SUB_FONT,
        fill=(205, 199, 188),
    )
    draw.text(
        (margin, 116),
        "This tests whether more references improve clarity. Thin translucent strokes and endpoint dots expose the data without changing ratios.",
        font=SMALL_FONT,
        fill=(181, 174, 160),
    )

    panel_gap = 46
    top_panel_w = (width - margin * 2 - panel_gap) // 2
    left = (margin, header_h, margin + top_panel_w, header_h + top_h)
    right = (margin + top_panel_w + panel_gap, header_h, margin + top_panel_w * 2 + panel_gap, header_h + top_h)

    draw_panel_frame(draw, left, "FULL SOURCE + 10X ULTRA-DENSE REFERENCES", dark=True)
    board, _left_image = paste_panel_image(board, full, left, full.extraction.crop, labels=True, point_stride=2)

    draw = ImageDraw.Draw(board)
    draw_panel_frame(draw, right, "SOURCE-EDGE REDRAW + SAME 10X REFERENCES", dark=False)
    edge_source = soften_line_art(make_line_art(full.extraction.crop, full.reference))
    board, _right_image = paste_panel_image(board, full, right, edge_source, labels=False, point_stride=2)
    draw = ImageDraw.Draw(board)
    draw_key(draw, right, (len(full.axes.x), len(full.axes.y), len(full.axes.z)))

    start_y = header_h + top_h + top_gap
    for index, result in enumerate(local_results):
        row = index // 3
        col = index % 3
        x0 = margin + col * (crop_panel_w + crop_gap)
        y0 = start_y + row * (crop_panel_h + crop_gap)
        board = draw_crop_panel(board, ImageDraw.Draw(board), result, (x0, y0, x0 + crop_panel_w, y0 + crop_panel_h))

    draw = ImageDraw.Draw(board)
    footer_y = height - margin - footer_h + 10
    draw.text(
        (margin, footer_y),
        "P15 test: if this does not improve clarity, the limitation is semantic reconstruction, not raw reference count.",
        font=ROW_FONT,
        fill=WHITE,
    )
    draw.text((margin, footer_y + 36), SOURCE_URL, font=SMALL_FONT, fill=(205, 199, 188))

    write_measurements(results)
    board.convert("RGB").save(DOC_IMAGE, optimize=True)
    shutil.copy2(DOC_IMAGE, REVIEW_IMAGE)
    print(DOC_IMAGE)
    print(REVIEW_IMAGE)
    print(MEASUREMENT_MANIFEST)


if __name__ == "__main__":
    build_board()
