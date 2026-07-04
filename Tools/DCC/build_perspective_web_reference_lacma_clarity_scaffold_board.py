#!/usr/bin/env python3
"""Build P14: LACMA perspective clarity and local-detail scaffold board.

P14 keeps the P13 high-resolution ratio discipline, then separates the problem:
- one full-image scaffold uses restrained X/Y/Z guides for readability;
- local crops spend their detection budget on floor, column, arch, arcade, and
  vault details;
- every crop stores its own processing width and converts endpoints against the
  same dimensions used by the extractor.
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
    choose_unique,
    draw_axis_line,
    is_horizontal,
    is_vertical,
    line_rank,
)
from build_perspective_web_reference_z_axis_board import screen_axis_penalty, z_depth_score


BOARD_NAME = "P14_LACMAGothicCathedralClarityScaffoldBoard"
DOC_IMAGE = OUT_ROOT / f"{BOARD_NAME}.png"
REVIEW_IMAGE = REVIEW_ROOT / f"{BOARD_NAME}.png"
MEASUREMENT_MANIFEST = OUT_ROOT / f"{BOARD_NAME}_Measurements.md"

SOURCE_URL = "https://collections.lacma.org/node/229641"
SOURCE_IMAGE_URL = "https://collections-images.lacma.org/images/13736/13736-1-primary.webp"
SOURCE_FILENAME = "REF_Perspective_GothicCathedral_LACMA_229641.webp"
GLOBAL_VP_HINT = (0.609, 0.632)

GOLD = (197, 142, 62)
MUTED = (145, 139, 126)
PAPER_DARK = (35, 35, 36)


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


@dataclass(frozen=True)
class PanelSpec:
    title: str
    focus: str
    crop: tuple[float, float, float, float]
    processing_width: int
    edge_percentile: float
    max_lines: int
    max_perspective_lines: int
    min_span_ratio: float
    vp_tolerance_ratio: float
    max_x: int
    max_y: int
    max_z: int


@dataclass(frozen=True)
class AxisSet:
    x: list[DetectedLine]
    y: list[DetectedLine]
    z: list[DetectedLine]


@dataclass(frozen=True)
class PanelResult:
    spec: PanelSpec
    reference: ReferenceSpec
    extraction: pixel.Extraction
    axes: AxisSet


PANEL_SPECS = [
    PanelSpec(
        "Full cathedral",
        "global scaffold and primary depth solve",
        (0.01, 0.015, 0.99, 0.985),
        1800,
        96.4,
        260,
        28,
        0.095,
        0.085,
        16,
        16,
        16,
    ),
    PanelSpec(
        "Floor grid",
        "tile corners, receding floor rows, and lower depth spacing",
        (0.08, 0.565, 0.94, 0.985),
        1500,
        95.8,
        230,
        30,
        0.075,
        0.115,
        18,
        6,
        24,
    ),
    PanelSpec(
        "Central nave",
        "arch stack, aisle depth, and central bay rhythm",
        (0.42, 0.10, 0.79, 0.82),
        1500,
        96.1,
        230,
        28,
        0.080,
        0.115,
        12,
        16,
        22,
    ),
    PanelSpec(
        "Right arcade",
        "side-wall arcade, gallery rails, and right depth family",
        (0.60, 0.08, 0.985, 0.80),
        1500,
        96.0,
        230,
        28,
        0.080,
        0.135,
        12,
        18,
        22,
    ),
    PanelSpec(
        "Left columns",
        "foreground column shafts, capitals, and vertical scale anchors",
        (0.15, 0.05, 0.51, 0.82),
        1500,
        96.1,
        230,
        24,
        0.085,
        0.135,
        10,
        22,
        18,
    ),
    PanelSpec(
        "Vault ribs",
        "ceiling ribs, upper arches, and overhead convergence",
        (0.30, 0.015, 0.83, 0.57),
        1500,
        96.2,
        240,
        28,
        0.075,
        0.135,
        14,
        12,
        24,
    ),
]


def crop_local_vp(crop: tuple[float, float, float, float]) -> tuple[float, float]:
    x0, y0, x1, y1 = crop
    return ((GLOBAL_VP_HINT[0] - x0) / (x1 - x0), (GLOBAL_VP_HINT[1] - y0) / (y1 - y0))


def to_reference_spec(spec: PanelSpec) -> ReferenceSpec:
    return ReferenceSpec(
        title=spec.title,
        filename=SOURCE_FILENAME,
        crop=spec.crop,
        vp_hint=crop_local_vp(spec.crop),
        edge_percentile=spec.edge_percentile,
        max_lines=spec.max_lines,
        max_perspective_lines=spec.max_perspective_lines,
        min_span_ratio=spec.min_span_ratio,
        vp_tolerance_ratio=spec.vp_tolerance_ratio,
    )


def extract_with_width(reference: ReferenceSpec, processing_width: int):
    original_resize = pixel.resize_for_processing

    def highres_resize(img, target_w=940):
        return original_resize(img, target_w=processing_width)

    pixel.resize_for_processing = highres_resize
    try:
        return pixel.extract(reference)
    finally:
        pixel.resize_for_processing = original_resize


def extraction_work_size(image: Image.Image, processing_width: int) -> tuple[int, int]:
    scale = processing_width / image.width
    return (processing_width, max(1, round(image.height * scale)))


def select_axes(extraction, spec: PanelSpec) -> AxisSet:
    perspective_ids = {id(line) for line in extraction.perspective_lines}
    others = [line for line in extraction.lines if id(line) not in perspective_ids]
    scale = spec.processing_width / 1500.0
    x_lines = choose_unique(
        sorted([line for line in others if is_horizontal(line)], key=line_rank, reverse=True),
        spec.max_x,
        theta_tol=2,
        rho_tol=18.0 * scale,
    )
    y_lines = choose_unique(
        sorted([line for line in others if is_vertical(line)], key=line_rank, reverse=True),
        spec.max_y,
        theta_tol=2,
        rho_tol=18.0 * scale,
    )
    z_candidates = [line for line in extraction.perspective_lines if abs(abs(line.angle_deg) - 90.0) > 7.0]
    strong_z = [line for line in z_candidates if screen_axis_penalty(line.angle_deg) >= 7.0]
    source = strong_z if len(strong_z) >= max(4, spec.max_z // 3) else z_candidates
    z_lines = choose_unique(
        sorted(source, key=z_depth_score, reverse=True),
        spec.max_z,
        theta_tol=2,
        rho_tol=16.0 * scale,
    )
    return AxisSet(x_lines, y_lines, sorted(z_lines, key=lambda line: line.angle_deg))


def build_results() -> list[PanelResult]:
    results: list[PanelResult] = []
    for panel_spec in PANEL_SPECS:
        reference = to_reference_spec(panel_spec)
        extraction = extract_with_width(reference, panel_spec.processing_width)
        axes = select_axes(extraction, panel_spec)
        results.append(PanelResult(panel_spec, reference, extraction, axes))
    return results


def draw_panel_frame(draw: ImageDraw.ImageDraw, rect: tuple[int, int, int, int], title: str, dark: bool) -> None:
    draw.rectangle(rect, fill=PANEL if dark else PAPER, outline=FRAME, width=2)
    draw.text((rect[0] + 14, rect[1] + 12), title, font=LABEL_FONT, fill=WHITE if dark else INK)


def draw_vp(draw: ImageDraw.ImageDraw, vp: tuple[float, float], rect: tuple[int, int, int, int], dark: bool, label: bool) -> None:
    px = normalized_to_rect(vp, rect)
    if rect[1] <= px[1] <= rect[3]:
        draw.line((rect[0], px[1], rect[2], px[1]), fill=GOLD, width=1)
    if rect[0] <= px[0] <= rect[2] and rect[1] <= px[1] <= rect[3]:
        draw.ellipse((px[0] - 7, px[1] - 7, px[0] + 7, px[1] + 7), fill=Z_RED)
        if label:
            draw_tag(draw, (px[0] + 9, px[1] - 18), f"Z-VP {vp[0]:.3f},{vp[1]:.3f}", Z_RED, dark)


def draw_axes(
    draw: ImageDraw.ImageDraw,
    result: PanelResult,
    rect: tuple[int, int, int, int],
    dark: bool,
    labels: bool,
    z_extension: bool,
    x_limit: int | None = None,
    y_limit: int | None = None,
    z_limit: int | None = None,
) -> None:
    work_size = extraction_work_size(result.extraction.crop, result.spec.processing_width)
    x_lines = result.axes.x[: x_limit or len(result.axes.x)]
    y_lines = result.axes.y[: y_limit or len(result.axes.y)]
    z_lines = result.axes.z[: z_limit or len(result.axes.z)]
    draw_vp(draw, result.extraction.vp_norm, rect, dark, labels)

    for index, line in enumerate(x_lines, 1):
        draw_axis_line(draw, line, rect, work_size, X_BLUE, f"X{index}" if labels else None, dark, width=2, extend=False)
    for index, line in enumerate(y_lines, 1):
        draw_axis_line(draw, line, rect, work_size, Y_GREEN, f"Y{index}" if labels else None, dark, width=2, extend=False)
    for index, line in enumerate(z_lines, 1):
        width = 4 if screen_axis_penalty(line.angle_deg) >= 18.0 else 3
        draw_axis_line(draw, line, rect, work_size, Z_RED, f"Z{index}" if labels else None, dark, width=width, extend=z_extension)


def draw_source_panel(
    board: Image.Image,
    draw: ImageDraw.ImageDraw,
    result: PanelResult,
    panel: tuple[int, int, int, int],
    title: str,
    labels: bool,
    limits: tuple[int | None, int | None, int | None] = (None, None, None),
) -> None:
    draw_panel_frame(draw, panel, title, dark=True)
    thumb = fit_image(result.extraction.crop, (panel[2] - panel[0] - 28, panel[3] - panel[1] - 60))
    image_rect = panel_image_rect(panel, thumb)
    board.paste(thumb, (image_rect[0], image_rect[1]))
    draw_axes(draw, result, image_rect, dark=True, labels=labels, z_extension=True, x_limit=limits[0], y_limit=limits[1], z_limit=limits[2])


def draw_scaffold_panel(
    board: Image.Image,
    draw: ImageDraw.ImageDraw,
    result: PanelResult,
    panel: tuple[int, int, int, int],
) -> None:
    draw_panel_frame(draw, panel, "CLEAN SCAFFOLD RECONSTRUCTION - FEWER LABELS", dark=False)
    line_art = soften_line_art(make_line_art(result.extraction.crop, result.reference))
    thumb = fit_image(line_art, (panel[2] - panel[0] - 28, panel[3] - panel[1] - 60))
    image_rect = panel_image_rect(panel, thumb)
    board.paste(thumb, (image_rect[0], image_rect[1]))
    draw_axes(draw, result, image_rect, dark=False, labels=False, z_extension=True, x_limit=10, y_limit=12, z_limit=14)

    key_x = panel[0] + 18
    key_y = panel[3] - 116
    entries = [
        (X_BLUE, "X: front-plane horizontals / floor rows"),
        (Y_GREEN, "Y: vertical scale anchors / columns"),
        (Z_RED, "Z: depth lines converging to solved VP"),
        (INK, "Clean scaffold hides line labels to reveal structure"),
        (INK, "Local crop panels below carry denser evidence"),
    ]
    for index, (color, text) in enumerate(entries):
        yy = key_y + index * 18
        draw.rectangle((key_x, yy + 3, key_x + 12, yy + 15), fill=color)
        draw.text((key_x + 18, yy), text, font=SMALL_FONT, fill=INK)


def draw_crop_panel(board: Image.Image, draw: ImageDraw.ImageDraw, result: PanelResult, panel: tuple[int, int, int, int]) -> None:
    title = f"{result.spec.title.upper()} - {len(result.axes.x)}/{len(result.axes.y)}/{len(result.axes.z)} X/Y/Z"
    draw_panel_frame(draw, panel, title, dark=True)
    thumb = fit_image(result.extraction.crop, (panel[2] - panel[0] - 28, panel[3] - panel[1] - 96))
    image_rect = panel_image_rect(panel, thumb)
    board.paste(thumb, (image_rect[0], image_rect[1]))
    draw_axes(draw, result, image_rect, dark=True, labels=False, z_extension=True)
    footer_y = panel[3] - 42
    draw.text((panel[0] + 16, footer_y), result.spec.focus, font=SMALL_FONT, fill=(210, 203, 190))
    draw.text(
        (panel[0] + 16, footer_y + 18),
        f"{result.spec.processing_width}px process | VP {result.extraction.vp_norm[0]:.3f},{result.extraction.vp_norm[1]:.3f} | edges {len(result.extraction.edge_pixels)}",
        font=SMALL_FONT,
        fill=(176, 169, 156),
    )


def normalized_endpoint(point, work_size):
    return (point[0] / max(1, work_size[0] - 1), point[1] / max(1, work_size[1] - 1))


def write_measurements(results: list[PanelResult]) -> None:
    lines = [
        "# P14 LACMA Gothic Cathedral Clarity Scaffold Data",
        "",
        "P14 separates global perspective measurement from local detail clarity. Every panel keeps endpoint ratios tied to its own extraction processing size.",
        "",
        f"- Source page: {SOURCE_URL}",
        f"- Source image URL: {SOURCE_IMAGE_URL}",
        f"- Source file: `{REF_ROOT.relative_to(OUT_ROOT.parents[3]) / SOURCE_FILENAME}`",
        f"- Global VP hint used for crop-local hints: `({GLOBAL_VP_HINT[0]:.6f}, {GLOBAL_VP_HINT[1]:.6f})`",
        "",
    ]
    for result in results:
        work_size = extraction_work_size(result.extraction.crop, result.spec.processing_width)
        lines.extend(
            [
                f"## {result.spec.title}",
                f"- Focus: {result.spec.focus}",
                f"- Crop: `{result.spec.crop}`",
                f"- Crop-local VP hint: `({result.reference.vp_hint[0]:.6f}, {result.reference.vp_hint[1]:.6f})`",
                f"- Solved VP: `({result.extraction.vp_norm[0]:.6f}, {result.extraction.vp_norm[1]:.6f})`",
                f"- Processing width/height: `{work_size[0]} x {work_size[1]}`",
                f"- Edge pixels: `{len(result.extraction.edge_pixels)}`",
                f"- Hough lines kept: `{len(result.extraction.lines)}`",
                f"- Displayed axes: `{len(result.axes.x)}` X, `{len(result.axes.y)}` Y, `{len(result.axes.z)}` Z",
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

    width = 3400
    margin = 64
    header_h = 158
    top_h = 1050
    top_gap = 48
    crop_gap = 34
    crop_panel_w = (width - margin * 2 - crop_gap * 2) // 3
    crop_panel_h = 565
    crop_rows = 2
    footer_h = 74
    height = header_h + top_h + top_gap + crop_rows * crop_panel_h + crop_gap + footer_h + margin

    board = Image.new("RGB", (width, height), BG)
    draw = ImageDraw.Draw(board)
    draw.text((margin, 30), "P14 LACMA Gothic Cathedral Clarity Scaffold", font=TITLE_FONT, fill=WHITE)
    draw.text(
        (margin, 84),
        "Full-image perspective scaffold plus local crop measurements for floor grid, columns, arches, arcade, and vault ribs.",
        font=SUB_FONT,
        fill=(205, 199, 188),
    )
    draw.text(
        (margin, 116),
        "Process rule: each crop keeps its own extraction width/height for endpoint normalization; density is increased locally, not by distorting global ratios.",
        font=SMALL_FONT,
        fill=(181, 174, 160),
    )

    panel_gap = 46
    top_panel_w = (width - margin * 2 - panel_gap) // 2
    left = (margin, header_h, margin + top_panel_w, header_h + top_h)
    right = (margin + top_panel_w + panel_gap, header_h, margin + top_panel_w * 2 + panel_gap, header_h + top_h)
    draw_source_panel(board, draw, full, left, "FULL SOURCE + RATIO-SAFE MEASUREMENTS", labels=True, limits=(12, 12, 16))
    draw_scaffold_panel(board, draw, full, right)

    start_y = header_h + top_h + top_gap
    for index, result in enumerate(local_results):
        row = index // 3
        col = index % 3
        x0 = margin + col * (crop_panel_w + crop_gap)
        y0 = start_y + row * (crop_panel_h + crop_gap)
        draw_crop_panel(board, draw, result, (x0, y0, x0 + crop_panel_w, y0 + crop_panel_h))

    footer_y = height - margin - footer_h + 10
    draw.text(
        (margin, footer_y),
        "P14 clarity pass: global scaffold is intentionally cleaner; local panels carry the extra reference density needed to fill missing structure.",
        font=ROW_FONT,
        fill=WHITE,
    )
    draw.text((margin, footer_y + 36), SOURCE_URL, font=SMALL_FONT, fill=(205, 199, 188))

    write_measurements(results)
    board.save(DOC_IMAGE, optimize=True)
    shutil.copy2(DOC_IMAGE, REVIEW_IMAGE)
    print(DOC_IMAGE)
    print(REVIEW_IMAGE)
    print(MEASUREMENT_MANIFEST)


if __name__ == "__main__":
    build_board()
