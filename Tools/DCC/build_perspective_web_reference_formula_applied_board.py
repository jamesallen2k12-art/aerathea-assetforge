#!/usr/bin/env python3
"""Build P08 using researched perspective/rendering formulas.

This pass applies:
- Canny-style gradient edges with non-maximum suppression.
- Gradient-guided Hough line voting: rho = x cos(theta) + y sin(theta).
- Homogeneous line equations: ax + by + c = 0.
- Weighted least-squares vanishing point solve.
- Residual-based rejection before redrawing.
"""

from __future__ import annotations

import heapq
import math
import shutil
from dataclasses import dataclass
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
    fit_image,
    panel_image_rect,
)


BOARD_NAME = "P08_WebPerspectiveFormulaAppliedRedrawBoard"
DOC_IMAGE = OUT_ROOT / f"{BOARD_NAME}.png"
REVIEW_IMAGE = REVIEW_ROOT / f"{BOARD_NAME}.png"
MEASUREMENT_MANIFEST = OUT_ROOT / f"{BOARD_NAME}_Measurements.md"

PAPER = (239, 234, 219)
BLUE = (54, 119, 181)
GREEN = (75, 143, 87)
GRAY = (103, 98, 87)
CYAN = (94, 160, 180)
ORANGE = (189, 116, 58)

Point = tuple[float, float]
Rect = tuple[int, int, int, int]


@dataclass(frozen=True)
class EdgePoint:
    x: int
    y: int
    theta: int
    magnitude: float


@dataclass
class FormulaLine:
    theta: int
    rho: float
    votes: float
    support: int
    span: float
    segment_px: tuple[Point, Point]
    equation: tuple[float, float, float]
    angle_deg: float
    residual_px: float = 0.0
    weight: float = 1.0


@dataclass
class FormulaExtraction:
    title: str
    filename: str
    crop: Image.Image
    work_size: tuple[int, int]
    edge_count: int
    lines: list[FormulaLine]
    perspective: list[FormulaLine]
    verticals: list[FormulaLine]
    horizontals: list[FormulaLine]
    secondaries: list[FormulaLine]
    vp: Point
    mean_residual_px: float
    max_residual_px: float


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


TITLE_FONT = load_font(43, True)
SUB_FONT = load_font(19)
ROW_FONT = load_font(23, True)
LABEL_FONT = load_font(15, True)
SMALL_FONT = load_font(12)


def crop_source(spec) -> Image.Image:
    with Image.open(REF_ROOT / spec.filename) as source:
        img = ImageOps.exif_transpose(source).convert("RGB")
    w, h = img.size
    x0, y0, x1, y1 = spec.crop
    return img.crop((round(w * x0), round(h * y0), round(w * x1), round(h * y1)))


def resize_for_processing(img: Image.Image, width: int = 760) -> Image.Image:
    scale = width / img.width
    return img.resize((width, max(1, round(img.height * scale))), LANCZOS)


def percentile(values: list[float], pct: float) -> float:
    if not values:
        return 0.0
    ordered = sorted(values)
    index = max(0, min(len(ordered) - 1, round((pct / 100.0) * (len(ordered) - 1))))
    return ordered[index]


def sobel_edges(work: Image.Image, keep_percentile: float) -> list[EdgePoint]:
    gray = ImageOps.grayscale(work.filter(ImageFilter.GaussianBlur(radius=0.75)))
    pix = gray.load()
    w, h = gray.size
    magnitudes = [[0.0 for _x in range(w)] for _y in range(h)]
    angles = [[0 for _x in range(w)] for _y in range(h)]
    nonzero: list[float] = []

    for y in range(1, h - 1):
        for x in range(1, w - 1):
            p00 = pix[x - 1, y - 1]
            p01 = pix[x, y - 1]
            p02 = pix[x + 1, y - 1]
            p10 = pix[x - 1, y]
            p12 = pix[x + 1, y]
            p20 = pix[x - 1, y + 1]
            p21 = pix[x, y + 1]
            p22 = pix[x + 1, y + 1]
            gx = -p00 - 2 * p10 - p20 + p02 + 2 * p12 + p22
            gy = -p00 - 2 * p01 - p02 + p20 + 2 * p21 + p22
            mag = math.hypot(gx, gy)
            if mag > 0.0:
                theta = int(round(math.degrees(math.atan2(gy, gx)))) % 180
                magnitudes[y][x] = mag
                angles[y][x] = theta
                nonzero.append(mag)

    threshold = max(20.0, percentile(nonzero, keep_percentile))
    edges: list[EdgePoint] = []
    for y in range(2, h - 2):
        for x in range(2, w - 2):
            mag = magnitudes[y][x]
            if mag < threshold:
                continue
            theta = angles[y][x]
            direction = ((theta + 22) % 180) // 45
            if direction == 0:
                before, after = magnitudes[y][x - 1], magnitudes[y][x + 1]
            elif direction == 1:
                before, after = magnitudes[y - 1][x + 1], magnitudes[y + 1][x - 1]
            elif direction == 2:
                before, after = magnitudes[y - 1][x], magnitudes[y + 1][x]
            else:
                before, after = magnitudes[y - 1][x - 1], magnitudes[y + 1][x + 1]
            if mag >= before and mag >= after:
                edges.append(EdgePoint(x, y, theta, mag))

    if len(edges) > 42_000:
        step = max(1, len(edges) // 42_000)
        edges = edges[::step]
    return edges


def hough_candidates(edges: list[EdgePoint], width: int, height: int, limit: int) -> list[tuple[int, float, float]]:
    diag = math.hypot(width, height)
    rho_res = 2.0
    rho_bins = int(math.ceil((diag * 2) / rho_res)) + 1
    theta_count = 180
    accumulator = [[0.0 for _r in range(rho_bins)] for _t in range(theta_count)]
    cosines = [math.cos(math.radians(t)) for t in range(theta_count)]
    sines = [math.sin(math.radians(t)) for t in range(theta_count)]

    for edge in edges:
        for delta in (-2, -1, 0, 1, 2):
            theta = (edge.theta + delta) % theta_count
            rho = edge.x * cosines[theta] + edge.y * sines[theta]
            rho_index = int(round((rho + diag) / rho_res))
            if 0 <= rho_index < rho_bins:
                accumulator[theta][rho_index] += edge.magnitude

    raw: list[tuple[float, int, int]] = []
    for theta, row in enumerate(accumulator):
        raw.extend((score, theta, rho_index) for rho_index, score in heapq.nlargest(40, enumerate(row), key=lambda item: item[1]) if score > 0)

    selected: list[tuple[int, float, float]] = []
    for score, theta, rho_index in sorted(raw, reverse=True):
        rho = rho_index * rho_res - diag
        if any(min(abs(theta - old_theta), 180 - abs(theta - old_theta)) <= 4 and abs(rho - old_rho) <= 18 for old_theta, old_rho, _ in selected):
            continue
        selected.append((theta, rho, score))
        if len(selected) >= limit:
            break
    return selected


def angle_delta(a: int, b: int) -> int:
    diff = abs(a - b) % 180
    return min(diff, 180 - diff)


def line_from_hough(theta: int, rho: float, votes: float, edges: list[EdgePoint], width: int, height: int) -> FormulaLine | None:
    rad = math.radians(theta)
    cos_t = math.cos(rad)
    sin_t = math.sin(rad)
    dir_x = -sin_t
    dir_y = cos_t
    support_t: list[float] = []
    support_mag = 0.0
    for edge in edges:
        if angle_delta(edge.theta, theta) > 12:
            continue
        distance = abs(edge.x * cos_t + edge.y * sin_t - rho)
        if distance <= 1.75:
            support_t.append(edge.x * dir_x + edge.y * dir_y)
            support_mag += edge.magnitude
    if len(support_t) < 18:
        return None
    support_t.sort()
    lo = support_t[max(0, round(len(support_t) * 0.04))]
    hi = support_t[min(len(support_t) - 1, round(len(support_t) * 0.96))]
    span = abs(hi - lo)
    if span < min(width, height) * 0.13:
        return None

    p0 = (cos_t * rho + dir_x * lo, sin_t * rho + dir_y * lo)
    p1 = (cos_t * rho + dir_x * hi, sin_t * rho + dir_y * hi)
    equation = normalized_equation(p0, p1, width, height)
    angle = math.degrees(math.atan2(-(p1[1] - p0[1]), p1[0] - p0[0]))
    while angle <= -180:
        angle += 360
    while angle > 180:
        angle -= 360
    weight = max(1.0, support_mag * (span / max(width, height)))
    return FormulaLine(theta, rho, votes, len(support_t), span, (p0, p1), equation, angle, weight=weight)


def normalized_equation(p0: Point, p1: Point, width: int, height: int) -> tuple[float, float, float]:
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


def residual(line: FormulaLine, point: Point) -> float:
    a, b, c = line.equation
    return abs(a * point[0] + b * point[1] + c)


def weighted_solve(lines: list[FormulaLine]) -> Point:
    saa = sab = sbb = sac = sbc = 0.0
    for line in lines:
        a, b, c = line.equation
        w = line.weight
        saa += w * a * a
        sab += w * a * b
        sbb += w * b * b
        sac += w * a * c
        sbc += w * b * c
    det = saa * sbb - sab * sab
    if abs(det) <= 1e-9:
        return (0.5, 0.5)
    return ((-sac * sbb + sab * sbc) / det, (-saa * sbc + sab * sac) / det)


def intersection(first: FormulaLine, second: FormulaLine) -> Point | None:
    a1, b1, c1 = first.equation
    a2, b2, c2 = second.equation
    det = a1 * b2 - a2 * b1
    if abs(det) <= 1e-8:
        return None
    return ((b1 * c2 - b2 * c1) / det, (c1 * a2 - c2 * a1) / det)


def solve_dominant_vp(lines: list[FormulaLine], width: int, height: int) -> tuple[Point, list[FormulaLine]]:
    candidates: list[tuple[float, Point]] = []
    useful = [line for line in lines if not is_vertical(line)]
    for i, first in enumerate(useful):
        for second in useful[i + 1 :]:
            if angle_delta(first.theta, second.theta) < 8:
                continue
            pt = intersection(first, second)
            if pt is None:
                continue
            if -0.40 <= pt[0] <= 1.40 and -0.35 <= pt[1] <= 1.35:
                score = 0.0
                for line in useful:
                    r = residual(line, pt)
                    if r <= 0.028:
                        score += line.weight / (1.0 + r * max(width, height))
                candidates.append((score, pt))

    if not candidates:
        initial = weighted_solve(useful[: max(2, min(8, len(useful)))])
    else:
        initial = max(candidates, key=lambda item: item[0])[1]

    inliers = [line for line in useful if residual(line, initial) <= 0.034]
    if len(inliers) < 3:
        inliers = sorted(useful, key=lambda line: residual(line, initial))[: max(3, min(8, len(useful)))]
    vp = weighted_solve(inliers)
    refined = [line for line in useful if residual(line, vp) <= 0.030]
    if len(refined) >= 3:
        vp = weighted_solve(refined)
        inliers = refined
    for line in inliers:
        line.residual_px = residual(line, vp) * max(width, height)
    inliers.sort(key=lambda line: (line.residual_px, -line.span, -line.support))
    return vp, inliers[:8]


def is_vertical(line: FormulaLine) -> bool:
    return abs(abs(line.angle_deg) - 90.0) <= 9.0


def is_horizontal(line: FormulaLine) -> bool:
    return min(abs(line.angle_deg), abs(abs(line.angle_deg) - 180.0)) <= 8.0


def unique_lines(lines: list[FormulaLine], limit: int) -> list[FormulaLine]:
    selected: list[FormulaLine] = []
    for line in lines:
        if any(angle_delta(line.theta, other.theta) <= 4 and abs(line.rho - other.rho) <= 18 for other in selected):
            continue
        selected.append(line)
        if len(selected) >= limit:
            break
    return selected


def extract_formula(spec) -> FormulaExtraction:
    crop = crop_source(spec)
    work = resize_for_processing(crop)
    keep = max(91.0, spec.edge_percentile - 2.0)
    edges = sobel_edges(work, keep)
    candidates = hough_candidates(edges, work.width, work.height, 140)
    lines: list[FormulaLine] = []
    for theta, rho, votes in candidates:
        line = line_from_hough(theta, rho, votes, edges, work.width, work.height)
        if line is not None:
            lines.append(line)
    lines.sort(key=lambda line: (-line.weight, -line.span, -line.support))
    lines = unique_lines(lines, 85)
    vp, perspective = solve_dominant_vp(lines, work.width, work.height)
    perspective_ids = {id(line) for line in perspective}
    remaining = [line for line in lines if id(line) not in perspective_ids]
    verticals = unique_lines(sorted([line for line in remaining if is_vertical(line)], key=lambda line: (-line.span, -line.weight)), 10)
    horizontals = unique_lines(sorted([line for line in remaining if is_horizontal(line)], key=lambda line: (-line.span, -line.weight)), 10)
    used = {id(line) for line in verticals + horizontals}
    secondaries = unique_lines(sorted([line for line in remaining if id(line) not in used and not is_vertical(line) and not is_horizontal(line)], key=lambda line: (-line.span, -line.weight)), 8)
    residuals = [line.residual_px for line in perspective]
    return FormulaExtraction(
        title=spec.title,
        filename=spec.filename,
        crop=crop,
        work_size=work.size,
        edge_count=len(edges),
        lines=lines,
        perspective=perspective,
        verticals=verticals,
        horizontals=horizontals,
        secondaries=secondaries,
        vp=vp,
        mean_residual_px=sum(residuals) / len(residuals) if residuals else 0.0,
        max_residual_px=max(residuals) if residuals else 0.0,
    )


def to_rect_norm(point: Point, rect: Rect) -> Point:
    return (rect[0] + point[0] * (rect[2] - rect[0]), rect[1] + point[1] * (rect[3] - rect[1]))


def px_to_rect(point: Point, work_size: tuple[int, int], rect: Rect) -> Point:
    return (
        rect[0] + (point[0] / max(1, work_size[0] - 1)) * (rect[2] - rect[0]),
        rect[1] + (point[1] / max(1, work_size[1] - 1)) * (rect[3] - rect[1]),
    )


def line_box_points(equation: tuple[float, float, float]) -> tuple[Point, Point]:
    a, b, c = equation
    pts: list[Point] = []
    if abs(b) > 1e-9:
        for x in (0.0, 1.0):
            y = -(a * x + c) / b
            if -0.08 <= y <= 1.08:
                pts.append((x, min(1.0, max(0.0, y))))
    if abs(a) > 1e-9:
        for y in (0.0, 1.0):
            x = -(b * y + c) / a
            if -0.08 <= x <= 1.08:
                pts.append((min(1.0, max(0.0, x)), y))
    unique: list[Point] = []
    for pt in pts:
        if not any(math.hypot(pt[0] - other[0], pt[1] - other[1]) < 1e-5 for other in unique):
            unique.append(pt)
    if len(unique) < 2:
        return ((0.0, 0.0), (1.0, 1.0))
    best = (unique[0], unique[1])
    best_dist = -1.0
    for i, a_pt in enumerate(unique):
        for b_pt in unique[i + 1 :]:
            dist = math.hypot(a_pt[0] - b_pt[0], a_pt[1] - b_pt[1])
            if dist > best_dist:
                best = (a_pt, b_pt)
                best_dist = dist
    return best


def draw_tag(draw: ImageDraw.ImageDraw, pos: Point, text: str, color, dark: bool) -> None:
    bbox = draw.textbbox(pos, text, font=SMALL_FONT)
    bg = (20, 20, 20) if dark else PAPER
    draw.rectangle((bbox[0] - 3, bbox[1] - 3, bbox[2] + 3, bbox[3] + 3), fill=bg, outline=color, width=1)
    draw.text(pos, text, font=SMALL_FONT, fill=color)


def draw_line(draw: ImageDraw.ImageDraw, line: FormulaLine, rect: Rect, work_size: tuple[int, int], color, width: int, extend: bool = False, label: str | None = None, dark: bool = False) -> None:
    if extend:
        p0, p1 = line_box_points(line.equation)
        a = to_rect_norm(p0, rect)
        b = to_rect_norm(p1, rect)
        draw.line((a[0], a[1], b[0], b[1]), fill=GOLD, width=1)
    a = px_to_rect(line.segment_px[0], work_size, rect)
    b = px_to_rect(line.segment_px[1], work_size, rect)
    draw.line((a[0], a[1], b[0], b[1]), fill=color, width=width)
    if label:
        draw_tag(draw, ((a[0] + b[0]) * 0.5, (a[1] + b[1]) * 0.5), label, color, dark)


def make_edge_underlay(extraction: FormulaExtraction) -> Image.Image:
    work = resize_for_processing(extraction.crop, 1000)
    gray = ImageOps.grayscale(work.filter(ImageFilter.GaussianBlur(radius=0.45)))
    edges = gray.filter(ImageFilter.FIND_EDGES)
    edges = ImageOps.autocontrast(edges, cutoff=1)
    # Keep a light underdrawing: strong local edges only, no tonal fill.
    hist = edges.histogram()
    total = edges.width * edges.height
    running = 0
    cutoff = 220
    for value, amount in enumerate(hist):
        running += amount
        if running >= total * 0.90:
            cutoff = value
            break
    mask = edges.point(lambda p: 145 if p >= cutoff else 0, mode="L").filter(ImageFilter.MaxFilter(3))
    base = Image.new("RGB", edges.size, PAPER)
    ink_layer = Image.new("RGB", edges.size, (111, 106, 96))
    base.paste(ink_layer, mask=mask)
    return Image.blend(base, Image.new("RGB", base.size, PAPER), 0.22)


def draw_formula_overlay(draw: ImageDraw.ImageDraw, extraction: FormulaExtraction, rect: Rect, dark: bool, clean: bool) -> None:
    vp = to_rect_norm(extraction.vp, rect)
    draw.line((rect[0], vp[1], rect[2], vp[1]), fill=GOLD, width=2)
    draw.ellipse((vp[0] - 6, vp[1] - 6, vp[0] + 6, vp[1] + 6), fill=RED)
    draw_tag(draw, (vp[0] + 8, vp[1] - 17), f"VP {extraction.vp[0]:.3f},{extraction.vp[1]:.3f}", RED, dark)

    if clean:
        for line in extraction.horizontals:
            draw_line(draw, line, rect, extraction.work_size, BLUE, 2)
        for line in extraction.verticals:
            draw_line(draw, line, rect, extraction.work_size, GREEN, 2)
        for line in extraction.secondaries[:5]:
            draw_line(draw, line, rect, extraction.work_size, GRAY, 1)

    for index, line in enumerate(extraction.perspective, 1):
        draw_line(
            draw,
            line,
            rect,
            extraction.work_size,
            RED,
            3,
            extend=True,
            label=f"L{index} {line.angle_deg:+.1f} deg",
            dark=dark,
        )


def draw_panel(draw: ImageDraw.ImageDraw, rect: Rect, title: str, dark: bool) -> None:
    draw.rectangle(rect, fill=PANEL if dark else PAPER, outline=FRAME, width=2)
    draw.text((rect[0] + 14, rect[1] + 13), title, font=LABEL_FONT, fill=WHITE if dark else INK)


def write_measurements(extractions: list[FormulaExtraction]) -> None:
    lines = [
        "# P08 Formula-Applied Perspective Redraw Measurements",
        "",
        "P08 applies the researched formulas directly: Sobel gradients, Canny-style non-maximum suppression, gradient-guided Hough voting, homogeneous line equations, and weighted least-squares vanishing-point solving.",
        "",
    ]
    for index, extraction in enumerate(extractions, 1):
        lines.extend(
            [
                f"## {index}. {extraction.title}",
                f"- Source file: `{REF_ROOT.relative_to(OUT_ROOT.parents[3]) / extraction.filename}`",
                f"- Work size: `{extraction.work_size[0]} x {extraction.work_size[1]}`",
                f"- Non-maximum-suppressed edge points: `{extraction.edge_count}`",
                f"- Hough lines kept: `{len(extraction.lines)}`",
                f"- Weighted least-squares VP: `({extraction.vp[0]:.6f}, {extraction.vp[1]:.6f})`",
                f"- VP residual mean/max: `{extraction.mean_residual_px:.3f}px` / `{extraction.max_residual_px:.3f}px`",
                "- Perspective inliers:",
            ]
        )
        for line_index, line in enumerate(extraction.perspective, 1):
            p0, p1 = line.segment_px
            n0 = (p0[0] / max(1, extraction.work_size[0] - 1), p0[1] / max(1, extraction.work_size[1] - 1))
            n1 = (p1[0] / max(1, extraction.work_size[0] - 1), p1[1] / max(1, extraction.work_size[1] - 1))
            a, b, c = line.equation
            lines.append(
                f"  - L{line_index}: endpoints `({n0[0]:.6f}, {n0[1]:.6f}) -> ({n1[0]:.6f}, {n1[1]:.6f})`; "
                f"angle `{line.angle_deg:+.3f} deg`; equation `{a:.8f}x + {b:.8f}y + {c:.8f} = 0`; "
                f"support `{line.support}`; span `{line.span:.1f}px`; weight `{line.weight:.1f}`; residual `{line.residual_px:.3f}px`"
            )
        lines.append("")
    MEASUREMENT_MANIFEST.write_text("\n".join(lines), encoding="utf-8")


def build_board() -> None:
    OUT_ROOT.mkdir(parents=True, exist_ok=True)
    REVIEW_ROOT.mkdir(parents=True, exist_ok=True)
    extractions = [extract_formula(spec) for spec in SPECS]

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
    draw.text((margin, 34), "P08 Web Perspective Formula-Applied Redraws", font=TITLE_FONT, fill=WHITE)
    draw.text(
        (margin, 91),
        "Left: source crop with formula-derived perspective inliers. Right: edge underlay plus weighted line-equation redraw.",
        font=SUB_FONT,
        fill=(205, 199, 188),
    )
    draw.text(
        (margin, 121),
        "Canny-style edges -> gradient-guided Hough -> homogeneous lines -> weighted least-squares VP -> residual-filtered redraw.",
        font=SMALL_FONT,
        fill=(181, 174, 160),
    )

    y = header_h
    for index, extraction in enumerate(extractions, 1):
        left = (margin, y + 48, margin + panel_w, y + 48 + panel_h)
        right = (margin + panel_w + panel_gap, y + 48, margin + panel_w * 2 + panel_gap, y + 48 + panel_h)
        draw.text(
            (margin, y + 7),
            f"{index}. {extraction.title} - VP ({extraction.vp[0]:.3f}, {extraction.vp[1]:.3f}) - residual {extraction.mean_residual_px:.1f}px",
            font=ROW_FONT,
            fill=WHITE,
        )

        draw_panel(draw, left, "SOURCE + FORMULA-DERIVED PERSPECTIVE INLIERS", dark=True)
        draw_panel(draw, right, "FORMULA-APPLIED REDRAW: EDGE UNDERLAY + WEIGHTED LINE MODEL", dark=False)

        source_thumb = fit_image(extraction.crop, (left[2] - left[0] - 28, left[3] - left[1] - 60))
        source_rect = panel_image_rect(left, source_thumb)
        board.paste(source_thumb, (source_rect[0], source_rect[1]))
        draw_formula_overlay(draw, extraction, source_rect, dark=True, clean=False)

        underlay = make_edge_underlay(extraction)
        redraw_thumb = fit_image(underlay, (right[2] - right[0] - 28, right[3] - right[1] - 60))
        redraw_rect = panel_image_rect(right, redraw_thumb)
        board.paste(redraw_thumb, (redraw_rect[0], redraw_rect[1]))
        draw_formula_overlay(draw, extraction, redraw_rect, dark=False, clean=True)
        key_x = right[0] + 18
        key_y = right[3] - 76
        draw.text((key_x, key_y), "Hough: rho = x cos(theta) + y sin(theta)", font=SMALL_FONT, fill=INK)
        draw.text((key_x, key_y + 17), "Line: ax + by + c = 0", font=SMALL_FONT, fill=INK)
        draw.text((key_x, key_y + 34), "VP: weighted least-squares line intersection", font=SMALL_FONT, fill=INK)
        y += row_h + row_gap

    write_measurements(extractions)
    board.save(DOC_IMAGE, optimize=True)
    shutil.copy2(DOC_IMAGE, REVIEW_IMAGE)
    print(DOC_IMAGE)
    print(REVIEW_IMAGE)
    print(MEASUREMENT_MANIFEST)


if __name__ == "__main__":
    build_board()
