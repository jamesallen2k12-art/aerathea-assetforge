#!/usr/bin/env python3
"""Build a pixel-derived perspective redraw board from web references.

This is the strict measurement pass:
- edges are extracted from the downloaded source pixels;
- straight lines are detected with a pure-Python Hough transform;
- perspective candidates are selected by extension toward a broad VP search
  zone, then solved with least-squares line intersection;
- the redraw panel is built from the detected line equations and support spans.
"""

from __future__ import annotations

import heapq
import math
import shutil
from dataclasses import dataclass
from pathlib import Path

from PIL import Image, ImageDraw, ImageFilter, ImageFont, ImageOps


ROOT = Path(__file__).resolve().parents[2]
REF_ROOT = ROOT / "SourceAssets" / "Reference" / "PerspectiveDrawing" / "WebReferences"
OUT_ROOT = ROOT / "docs" / "assets" / "training" / "perspective_drawing"
REVIEW_ROOT = ROOT / "Saved" / "Automation" / "DCC" / "PerspectiveDrawing"

BOARD_NAME = "P04_WebPerspectivePixelMeasuredRedrawBoard"
DOC_IMAGE = OUT_ROOT / f"{BOARD_NAME}.png"
REVIEW_IMAGE = REVIEW_ROOT / f"{BOARD_NAME}.png"
MEASUREMENT_MANIFEST = OUT_ROOT / f"{BOARD_NAME}_Measurements.md"

BG = (28, 28, 29)
PANEL = (43, 43, 44)
PAPER = (235, 228, 210)
INK = (29, 28, 25)
INK_SOFT = (94, 88, 76)
WHITE = (236, 232, 222)
FRAME = (116, 107, 88)
RED = (216, 58, 48)
GOLD = (196, 142, 68)
BLUE = (65, 128, 188)
CYAN = (88, 161, 182)
GREEN = (88, 146, 92)
MAGENTA = (178, 76, 168)
LANCZOS = getattr(getattr(Image, "Resampling", Image), "LANCZOS", Image.LANCZOS)

Point = tuple[float, float]
Rect = tuple[int, int, int, int]


@dataclass(frozen=True)
class ReferenceSpec:
    title: str
    filename: str
    crop: tuple[float, float, float, float]
    vp_hint: Point
    edge_percentile: float
    max_lines: int
    max_perspective_lines: int
    min_span_ratio: float
    vp_tolerance_ratio: float


@dataclass
class DetectedLine:
    theta_index: int
    rho: float
    votes: int
    segment_px: tuple[Point, Point]
    support_count: int
    span_px: float
    angle_deg: float
    equation: tuple[float, float, float]
    distance_to_hint_px: float
    residual_to_vp_px: float = 0.0


@dataclass
class Extraction:
    spec: ReferenceSpec
    crop: Image.Image
    edge_pixels: list[tuple[int, int]]
    lines: list[DetectedLine]
    perspective_lines: list[DetectedLine]
    vp_px: Point
    vp_norm: Point
    mean_residual_px: float
    max_residual_px: float


SPECS = [
    ReferenceSpec(
        "Arcade Capriccio",
        "REF_Perspective_Arcade_Capriccio_MET_DP836399.jpg",
        (0.02, 0.03, 0.98, 0.97),
        (0.505, 0.565),
        97.0,
        95,
        10,
        0.16,
        0.055,
    ),
    ReferenceSpec(
        "Palace Fantasy",
        "REF_Perspective_Palace_Fantasy_NationalTrust.jpg",
        (0.00, 0.00, 1.00, 1.00),
        (0.502, 0.574),
        96.0,
        95,
        10,
        0.16,
        0.060,
    ),
    ReferenceSpec(
        "Double Arch Portico",
        "REF_Perspective_DoubleArch_Rijksmuseum.jpg",
        (0.10, 0.14, 0.90, 0.91),
        (0.569, 0.681),
        96.5,
        95,
        10,
        0.15,
        0.060,
    ),
    ReferenceSpec(
        "Perspective Street",
        "REF_Perspective_Street_NGA_205782.jpg",
        (0.01, 0.02, 0.99, 0.96),
        (0.239, 0.846),
        96.8,
        110,
        12,
        0.18,
        0.070,
    ),
    ReferenceSpec(
        "Interior Hall",
        "REF_Perspective_InteriorHall_MET_DP828125.jpg",
        (0.04, 0.05, 0.96, 0.95),
        (0.380, 0.826),
        96.7,
        105,
        12,
        0.16,
        0.065,
    ),
]


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


def crop_source(spec: ReferenceSpec) -> Image.Image:
    with Image.open(REF_ROOT / spec.filename) as source:
        img = ImageOps.exif_transpose(source).convert("RGB")
    w, h = img.size
    x0, y0, x1, y1 = spec.crop
    box = (round(w * x0), round(h * y0), round(w * x1), round(h * y1))
    return img.crop(box)


def resize_for_processing(img: Image.Image, target_w: int = 940) -> Image.Image:
    scale = target_w / img.width
    target_h = max(1, round(img.height * scale))
    return img.resize((target_w, target_h), LANCZOS)


def percentile_threshold(image: Image.Image, percentile: float) -> int:
    histogram = image.histogram()
    total = image.width * image.height
    target = total * percentile / 100.0
    count = 0
    for value, amount in enumerate(histogram):
        count += amount
        if count >= target:
            return value
    return 255


def collect_edge_pixels(work: Image.Image, percentile: float) -> list[tuple[int, int]]:
    gray = ImageOps.grayscale(work)
    gray = ImageOps.autocontrast(gray, cutoff=1)
    edges = gray.filter(ImageFilter.FIND_EDGES)
    edges = ImageOps.autocontrast(edges, cutoff=1)
    threshold = max(24, percentile_threshold(edges, percentile))
    pixels = edges.load()
    out: list[tuple[int, int]] = []
    stride = 1 if work.width * work.height < 700_000 else 2
    margin = 3
    for y in range(margin, work.height - margin, stride):
        for x in range(margin, work.width - margin, stride):
            if pixels[x, y] >= threshold:
                out.append((x, y))
    if len(out) > 70_000:
        step = max(1, len(out) // 70_000)
        out = out[::step]
    return out


def hough_peaks(edge_pixels: list[tuple[int, int]], width: int, height: int, max_lines: int) -> list[tuple[int, float, int]]:
    diag = math.hypot(width, height)
    rho_res = 2.0
    rho_bins = int(math.ceil((diag * 2.0) / rho_res)) + 1
    rho_offset = diag
    theta_count = 180
    cosines = [math.cos(math.radians(theta)) for theta in range(theta_count)]
    sines = [math.sin(math.radians(theta)) for theta in range(theta_count)]
    accumulator = [[0] * rho_bins for _ in range(theta_count)]

    for x, y in edge_pixels:
        for theta in range(theta_count):
            rho = x * cosines[theta] + y * sines[theta]
            rho_index = int(round((rho + rho_offset) / rho_res))
            if 0 <= rho_index < rho_bins:
                accumulator[theta][rho_index] += 1

    best: list[tuple[int, int, int]] = []
    for theta, row in enumerate(accumulator):
        row_best = heapq.nlargest(80, enumerate(row), key=lambda item: item[1])
        best.extend((votes, theta, rho_index) for rho_index, votes in row_best if votes > 0)

    selected: list[tuple[int, float, int]] = []
    theta_radius = 5
    rho_radius = 18
    for votes, theta, rho_index in sorted(best, reverse=True):
        rho = rho_index * rho_res - rho_offset
        if any(min(abs(theta - old_theta), 180 - abs(theta - old_theta)) <= theta_radius and abs(rho - old_rho) <= rho_radius for old_theta, old_rho, _old_votes in selected):
            continue
        selected.append((theta, rho, votes))
        if len(selected) >= max_lines * 2:
            break
    return selected


def hough_line_support(
    theta: int,
    rho: float,
    votes: int,
    edge_pixels: list[tuple[int, int]],
    width: int,
    height: int,
    hint_px: Point,
    min_span_ratio: float,
) -> DetectedLine | None:
    angle = math.radians(theta)
    cos_t = math.cos(angle)
    sin_t = math.sin(angle)
    dir_x = -sin_t
    dir_y = cos_t
    support: list[float] = []
    for x, y in edge_pixels:
        if abs(x * cos_t + y * sin_t - rho) <= 1.7:
            support.append(x * dir_x + y * dir_y)

    if len(support) < 26:
        return None

    support.sort()
    low_index = max(0, int(len(support) * 0.03))
    high_index = min(len(support) - 1, int(len(support) * 0.97))
    t0 = support[low_index]
    t1 = support[high_index]
    span = abs(t1 - t0)
    if span < min(width, height) * min_span_ratio:
        return None

    p0 = (cos_t * rho + dir_x * t0, sin_t * rho + dir_y * t0)
    p1 = (cos_t * rho + dir_x * t1, sin_t * rho + dir_y * t1)
    dx = p1[0] - p0[0]
    dy = p1[1] - p0[1]
    angle_deg = math.degrees(math.atan2(-dy, dx))
    while angle_deg <= -180.0:
        angle_deg += 360.0
    while angle_deg > 180.0:
        angle_deg -= 360.0
    distance_to_hint = abs(hint_px[0] * cos_t + hint_px[1] * sin_t - rho)
    equation = normalized_equation_from_pixels(p0, p1, width, height)
    return DetectedLine(theta, rho, votes, (p0, p1), len(support), span, angle_deg, equation, distance_to_hint)


def normalized_equation_from_pixels(p0: Point, p1: Point, width: int, height: int) -> tuple[float, float, float]:
    x0 = p0[0] / max(1, width - 1)
    y0 = p0[1] / max(1, height - 1)
    x1 = p1[0] / max(1, width - 1)
    y1 = p1[1] / max(1, height - 1)
    a = y0 - y1
    b = x1 - x0
    c = x0 * y1 - x1 * y0
    norm = math.hypot(a, b)
    if norm <= 1e-9:
        return (0.0, 0.0, 0.0)
    return (a / norm, b / norm, c / norm)


def solve_vp(lines: list[DetectedLine]) -> Point:
    sum_aa = sum_ab = sum_bb = sum_ac = sum_bc = 0.0
    for line in lines:
        a, b, c = line.equation
        sum_aa += a * a
        sum_ab += a * b
        sum_bb += b * b
        sum_ac += a * c
        sum_bc += b * c
    det = sum_aa * sum_bb - sum_ab * sum_ab
    if abs(det) <= 1e-9:
        return (0.5, 0.5)
    return ((-sum_ac * sum_bb + sum_ab * sum_bc) / det, (-sum_aa * sum_bc + sum_ab * sum_ac) / det)


def residual_norm(line: DetectedLine, vp: Point) -> float:
    a, b, c = line.equation
    return abs(a * vp[0] + b * vp[1] + c)


def verticalish(angle_deg: float) -> bool:
    folded = abs(abs(angle_deg) - 90.0)
    return folded < 9.0


def select_perspective_lines(lines: list[DetectedLine], spec: ReferenceSpec, width: int, height: int) -> tuple[list[DetectedLine], Point]:
    hint_px = (spec.vp_hint[0] * width, spec.vp_hint[1] * height)
    tolerance_px = spec.vp_tolerance_ratio * math.hypot(width, height)
    candidates = [line for line in lines if line.distance_to_hint_px <= tolerance_px and not verticalish(line.angle_deg)]
    if len(candidates) < 4:
        candidates = [line for line in lines if line.distance_to_hint_px <= tolerance_px * 1.7 and not verticalish(line.angle_deg)]
    if len(candidates) < 2:
        candidates = sorted([line for line in lines if not verticalish(line.angle_deg)], key=lambda line: line.distance_to_hint_px)[: max(2, spec.max_perspective_lines)]

    candidates = sorted(candidates, key=lambda line: (-line.votes, line.distance_to_hint_px))[: max(2, spec.max_perspective_lines * 2)]
    vp = solve_vp(candidates)
    refined = sorted(candidates, key=lambda line: residual_norm(line, vp))[: max(2, spec.max_perspective_lines)]
    vp = solve_vp(refined)
    for line in refined:
        line.residual_to_vp_px = residual_norm(line, vp) * max(width, height)
    refined.sort(key=lambda line: (-line.span_px, line.residual_to_vp_px, -line.votes))
    return refined[: spec.max_perspective_lines], vp


def extract(spec: ReferenceSpec) -> Extraction:
    crop = crop_source(spec)
    work = resize_for_processing(crop)
    edge_pixels = collect_edge_pixels(work, spec.edge_percentile)
    hint_px = (spec.vp_hint[0] * work.width, spec.vp_hint[1] * work.height)
    peaks = hough_peaks(edge_pixels, work.width, work.height, spec.max_lines)
    lines: list[DetectedLine] = []
    for theta, rho, votes in peaks:
        detected = hough_line_support(theta, rho, votes, edge_pixels, work.width, work.height, hint_px, spec.min_span_ratio)
        if detected is not None:
            lines.append(detected)
    lines.sort(key=lambda line: (-line.votes, -line.span_px))
    lines = lines[: spec.max_lines]
    perspective_lines, vp_norm = select_perspective_lines(lines, spec, work.width, work.height)
    vp_px = (vp_norm[0] * work.width, vp_norm[1] * work.height)
    residuals = [line.residual_to_vp_px for line in perspective_lines]
    return Extraction(
        spec=spec,
        crop=crop,
        edge_pixels=edge_pixels,
        lines=lines,
        perspective_lines=perspective_lines,
        vp_px=vp_px,
        vp_norm=vp_norm,
        mean_residual_px=sum(residuals) / len(residuals) if residuals else 0.0,
        max_residual_px=max(residuals) if residuals else 0.0,
    )


def fit_image(image: Image.Image, target: tuple[int, int]) -> Image.Image:
    return ImageOps.contain(image, target, LANCZOS)


def panel_image_rect(panel: Rect, image: Image.Image, top_pad: int = 46) -> Rect:
    available_w = panel[2] - panel[0] - 28
    available_h = panel[3] - panel[1] - top_pad - 14
    scale = min(available_w / image.width, available_h / image.height)
    w = round(image.width * scale)
    h = round(image.height * scale)
    x = panel[0] + (panel[2] - panel[0] - w) // 2
    y = panel[1] + top_pad + (available_h - h) // 2
    return (x, y, x + w, y + h)


def px_to_rect(point: Point, work_size: tuple[int, int], rect: Rect) -> Point:
    x = rect[0] + (point[0] / max(1, work_size[0] - 1)) * (rect[2] - rect[0])
    y = rect[1] + (point[1] / max(1, work_size[1] - 1)) * (rect[3] - rect[1])
    return (x, y)


def normalized_to_rect(point: Point, rect: Rect) -> Point:
    return (rect[0] + point[0] * (rect[2] - rect[0]), rect[1] + point[1] * (rect[3] - rect[1]))


def line_box_points_from_equation(equation: tuple[float, float, float]) -> tuple[Point, Point]:
    a, b, c = equation
    points: list[Point] = []
    eps = 1e-8
    for x in (0.0, 1.0):
        if abs(b) > eps:
            y = -(a * x + c) / b
            if -0.05 <= y <= 1.05:
                points.append((x, min(1.0, max(0.0, y))))
    for y in (0.0, 1.0):
        if abs(a) > eps:
            x = -(b * y + c) / a
            if -0.05 <= x <= 1.05:
                points.append((min(1.0, max(0.0, x)), y))
    unique: list[Point] = []
    for point in points:
        if not any(math.hypot(point[0] - other[0], point[1] - other[1]) < 1e-5 for other in unique):
            unique.append(point)
    if len(unique) < 2:
        return ((0.0, 0.0), (1.0, 1.0))
    best = (unique[0], unique[1])
    best_dist = -1.0
    for i, first in enumerate(unique):
        for second in unique[i + 1 :]:
            dist = math.hypot(first[0] - second[0], first[1] - second[1])
            if dist > best_dist:
                best = (first, second)
                best_dist = dist
    return best


def draw_tag(draw: ImageDraw.ImageDraw, pos: Point, text: str, fill: tuple[int, int, int], dark: bool) -> None:
    bbox = draw.textbbox(pos, text, font=SMALL_FONT)
    pad = 3
    bg = (22, 22, 22) if dark else (241, 235, 219)
    draw.rectangle((bbox[0] - pad, bbox[1] - pad, bbox[2] + pad, bbox[3] + pad), fill=bg, outline=fill, width=1)
    draw.text(pos, text, font=SMALL_FONT, fill=fill)


def draw_detected_line(
    draw: ImageDraw.ImageDraw,
    line: DetectedLine,
    rect: Rect,
    work_size: tuple[int, int],
    color: tuple[int, int, int],
    label: str | None,
    dark: bool,
    width: int = 2,
    extend: bool = False,
) -> None:
    if extend:
        p0_norm, p1_norm = line_box_points_from_equation(line.equation)
        p0 = normalized_to_rect(p0_norm, rect)
        p1 = normalized_to_rect(p1_norm, rect)
        draw.line((p0[0], p0[1], p1[0], p1[1]), fill=GOLD, width=1)
    a = px_to_rect(line.segment_px[0], work_size, rect)
    b = px_to_rect(line.segment_px[1], work_size, rect)
    draw.line((a[0], a[1], b[0], b[1]), fill=color, width=width)
    if label:
        mid = ((a[0] + b[0]) * 0.5, (a[1] + b[1]) * 0.5)
        draw_tag(draw, mid, label, color, dark)


def draw_overlay(draw: ImageDraw.ImageDraw, extraction: Extraction, rect: Rect, source: bool) -> None:
    work_size = resize_for_processing(extraction.crop).size
    vp = normalized_to_rect(extraction.vp_norm, rect)
    horizon_y = vp[1]
    draw.line((rect[0], horizon_y, rect[2], horizon_y), fill=GOLD, width=2)
    draw.ellipse((vp[0] - 6, vp[1] - 6, vp[0] + 6, vp[1] + 6), fill=RED)
    draw_tag(draw, (vp[0] + 8, vp[1] - 17), f"VP {extraction.vp_norm[0]:.3f},{extraction.vp_norm[1]:.3f}", RED, source)

    perspective_ids = {id(line) for line in extraction.perspective_lines}
    structural = [line for line in extraction.lines if id(line) not in perspective_ids][:28]
    for line in structural:
        color = GREEN if abs(abs(line.angle_deg) - 90.0) < 9.0 else CYAN
        draw_detected_line(draw, line, rect, work_size, color, None, source, width=1, extend=False)

    for index, line in enumerate(extraction.perspective_lines, 1):
        label = f"L{index} {line.angle_deg:+.1f}"
        draw_detected_line(draw, line, rect, work_size, RED, label, source, width=3, extend=True)


def draw_panel(draw: ImageDraw.ImageDraw, rect: Rect, title: str, dark: bool) -> None:
    draw.rectangle(rect, fill=PANEL if dark else PAPER, outline=FRAME, width=2)
    draw.text((rect[0] + 14, rect[1] + 13), title, font=LABEL_FONT, fill=WHITE if dark else INK)


def write_measurements(extractions: list[Extraction]) -> None:
    lines = [
        "# P04 Pixel-Measured Perspective Redraw Data",
        "",
        "This pass detects source edges, runs a Hough line transform, extends detected line equations, and solves vanishing points from those detected lines.",
        "Coordinates are normalized to the displayed crop for each source image.",
        "",
    ]
    for index, extraction in enumerate(extractions, 1):
        spec = extraction.spec
        lines.extend(
            [
                f"## {index}. {spec.title}",
                f"- Source file: `{REF_ROOT.relative_to(ROOT) / spec.filename}`",
                f"- Crop: `{spec.crop}`",
                f"- Edge pixels used: `{len(extraction.edge_pixels)}`",
                f"- Hough lines kept: `{len(extraction.lines)}`",
                f"- Perspective lines used for VP: `{len(extraction.perspective_lines)}`",
                f"- Solved VP: `({extraction.vp_norm[0]:.6f}, {extraction.vp_norm[1]:.6f})`",
                f"- VP residual mean/max: `{extraction.mean_residual_px:.3f}px` / `{extraction.max_residual_px:.3f}px` on the processing crop",
                "- Perspective measurement lines:",
            ]
        )
        for line_index, line in enumerate(extraction.perspective_lines, 1):
            p0, p1 = line.segment_px
            work = resize_for_processing(extraction.crop)
            n0 = (p0[0] / max(1, work.width - 1), p0[1] / max(1, work.height - 1))
            n1 = (p1[0] / max(1, work.width - 1), p1[1] / max(1, work.height - 1))
            a, b, c = line.equation
            lines.append(
                f"  - L{line_index}: endpoints `({n0[0]:.6f}, {n0[1]:.6f}) -> ({n1[0]:.6f}, {n1[1]:.6f})`; "
                f"angle `{line.angle_deg:+.3f} deg`; votes `{line.votes}`; support `{line.support_count}`; "
                f"span `{line.span_px:.1f}px`; line `{a:.8f}x + {b:.8f}y + {c:.8f} = 0`; "
                f"VP residual `{line.residual_to_vp_px:.3f}px`"
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
    row_h = 600
    row_gap = 40
    panel_gap = 42
    panel_w = (width - margin * 2 - panel_gap) // 2
    panel_h = 535
    height = header_h + len(extractions) * row_h + (len(extractions) - 1) * row_gap + margin

    board = Image.new("RGB", (width, height), BG)
    draw = ImageDraw.Draw(board)
    draw.text((margin, 34), "P04 Web Perspective Pixel-Measured Redraws", font=TITLE_FONT, fill=WHITE)
    draw.text(
        (margin, 91),
        "Left: source crop with pixel-detected line spans and mathematical extensions. Right: redraw from those detected line equations.",
        font=SUB_FONT,
        fill=(205, 199, 188),
    )
    draw.text(
        (margin, 121),
        "Red = detected perspective lines used for VP. Gold = extended line equations. Green/blue = additional detected structural lines.",
        font=SMALL_FONT,
        fill=(181, 174, 160),
    )

    y = header_h
    for index, extraction in enumerate(extractions, 1):
        spec = extraction.spec
        left = (margin, y + 48, margin + panel_w, y + 48 + panel_h)
        right = (margin + panel_w + panel_gap, y + 48, margin + panel_w * 2 + panel_gap, y + 48 + panel_h)
        draw.text(
            (margin, y + 7),
            f"{index}. {spec.title} - pixel VP ({extraction.vp_norm[0]:.3f}, {extraction.vp_norm[1]:.3f}) - residual {extraction.mean_residual_px:.1f}px",
            font=ROW_FONT,
            fill=WHITE,
        )

        draw_panel(draw, left, "SOURCE PIXELS + DETECTED MEASUREMENTS", dark=True)
        draw_panel(draw, right, "REDRAW FROM DETECTED LINE EQUATIONS", dark=False)

        source_thumb = fit_image(extraction.crop, (left[2] - left[0] - 28, left[3] - left[1] - 60))
        source_rect = panel_image_rect(left, source_thumb)
        board.paste(source_thumb, (source_rect[0], source_rect[1]))
        draw_overlay(draw, extraction, source_rect, source=True)

        redraw_rect = panel_image_rect(right, source_thumb)
        draw.rectangle(redraw_rect, fill=PAPER, outline=FRAME, width=1)
        draw_overlay(draw, extraction, redraw_rect, source=False)
        y += row_h + row_gap

    write_measurements(extractions)
    board.save(DOC_IMAGE, optimize=True)
    shutil.copy2(DOC_IMAGE, REVIEW_IMAGE)
    print(DOC_IMAGE)
    print(REVIEW_IMAGE)
    print(MEASUREMENT_MANIFEST)


if __name__ == "__main__":
    build_board()
