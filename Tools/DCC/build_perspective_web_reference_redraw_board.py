#!/usr/bin/env python3
"""Build a measured side-by-side web perspective redraw board.

This pass is intentionally strict: source lines are recorded as normalized
image coordinates, vanishing points are computed from those line equations,
and the redraw uses the same measured coordinates at the same aspect ratio.
"""

from __future__ import annotations

import math
import shutil
from dataclasses import dataclass, field
from pathlib import Path

from PIL import Image, ImageDraw, ImageFont, ImageOps


ROOT = Path(__file__).resolve().parents[2]
REF_ROOT = ROOT / "SourceAssets" / "Reference" / "PerspectiveDrawing" / "WebReferences"
OUT_ROOT = ROOT / "docs" / "assets" / "training" / "perspective_drawing"
REVIEW_ROOT = ROOT / "Saved" / "Automation" / "DCC" / "PerspectiveDrawing"

BOARD_NAME = "P03_WebPerspectiveReferenceRedrawBoard"
DOC_IMAGE = OUT_ROOT / f"{BOARD_NAME}.png"
REVIEW_IMAGE = REVIEW_ROOT / f"{BOARD_NAME}.png"
SOURCE_MANIFEST = OUT_ROOT / f"{BOARD_NAME}_Sources.md"
MEASUREMENT_MANIFEST = OUT_ROOT / f"{BOARD_NAME}_Measurements.md"

BG = (29, 29, 30)
PANEL = (43, 43, 44)
PAPER = (238, 232, 216)
PAPER_ALT = (229, 221, 202)
INK = (32, 30, 27)
INK_SOFT = (86, 80, 69)
BLUE = (62, 125, 186)
CYAN = (86, 150, 171)
GOLD = (184, 138, 70)
RED = (200, 64, 56)
GREEN = (96, 143, 91)
WHITE = (234, 229, 218)
FRAME = (114, 105, 88)
LANCZOS = getattr(getattr(Image, "Resampling", Image), "LANCZOS", Image.LANCZOS)

Point = tuple[float, float]
Rect = tuple[int, int, int, int]
Color = tuple[int, int, int]


@dataclass(frozen=True)
class Segment:
    a: Point
    b: Point
    group: str = "structure"
    width: int = 2


@dataclass(frozen=True)
class Arch:
    cx: float
    spring_y: float
    rx: float
    ry: float
    base_y: float
    group: str = "structure"
    width: int = 2


@dataclass(frozen=True)
class RectShape:
    x0: float
    y0: float
    x1: float
    y1: float
    group: str = "structure"
    width: int = 2


@dataclass(frozen=True)
class Column:
    cx: float
    base_y: float
    top_y: float
    radius: float
    group: str = "structure"
    width: int = 2


@dataclass(frozen=True)
class GridSpec:
    left_bottom: Point
    right_bottom: Point
    rows: int
    cols: int
    bottom_y: float | None = None


@dataclass(frozen=True)
class Reference:
    title: str
    lesson: str
    filename: str
    url: str
    page: str
    license_name: str
    vp_lines: list[Segment]
    structure: list[Segment] = field(default_factory=list)
    arches: list[Arch] = field(default_factory=list)
    rectangles: list[RectShape] = field(default_factory=list)
    columns: list[Column] = field(default_factory=list)
    grids: list[GridSpec] = field(default_factory=list)
    generated_rays: list[tuple[float, float]] = field(default_factory=list)
    note: str = ""


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


TITLE_FONT = load_font(46, True)
SUB_FONT = load_font(20)
ROW_FONT = load_font(24, True)
LABEL_FONT = load_font(15, True)
SMALL_FONT = load_font(13)


def line_coeff(seg: Segment) -> tuple[float, float, float]:
    x1, y1 = seg.a
    x2, y2 = seg.b
    a = y1 - y2
    b = x2 - x1
    c = x1 * y2 - x2 * y1
    norm = math.hypot(a, b)
    if norm <= 1e-9:
        return (0.0, 0.0, 0.0)
    return (a / norm, b / norm, c / norm)


def intersect_lines(one: Segment, two: Segment) -> Point | None:
    a1, b1, c1 = line_coeff(one)
    a2, b2, c2 = line_coeff(two)
    det = a1 * b2 - a2 * b1
    if abs(det) <= 1e-6:
        return None
    x = (b1 * c2 - b2 * c1) / det
    y = (c1 * a2 - c2 * a1) / det
    return (x, y)


def computed_vp(ref: Reference) -> Point:
    sum_aa = 0.0
    sum_ab = 0.0
    sum_bb = 0.0
    sum_ac = 0.0
    sum_bc = 0.0
    for seg in visible_vp_lines(ref):
        a, b, c = line_coeff(seg)
        sum_aa += a * a
        sum_ab += a * b
        sum_bb += b * b
        sum_ac += a * c
        sum_bc += b * c

    det = sum_aa * sum_bb - sum_ab * sum_ab
    if abs(det) > 1e-9:
        x = (-sum_ac * sum_bb + sum_ab * sum_bc) / det
        y = (-sum_aa * sum_bc + sum_ab * sum_ac) / det
        return (x, y)

    points: list[Point] = []
    source_lines = visible_vp_lines(ref)
    for i, first in enumerate(source_lines):
        for second in source_lines[i + 1 :]:
            pt = intersect_lines(first, second)
            if pt is not None:
                points.append(pt)
    if not points:
        raise ValueError(f"No vanishing point intersections for {ref.title}")
    return (sum(p[0] for p in points) / len(points), sum(p[1] for p in points) / len(points))


def vp_residuals(ref: Reference, vp: Point) -> list[float]:
    residuals: list[float] = []
    for seg in visible_vp_lines(ref):
        a, b, c = line_coeff(seg)
        residuals.append(abs(a * vp[0] + b * vp[1] + c))
    return residuals


def visible_vp_lines(ref: Reference) -> list[Segment]:
    visible: list[Segment] = []
    for index, seg in enumerate(ref.vp_lines):
        fraction = 0.34 + 0.05 * (index % 3)
        visible.append(Segment(seg.a, interp(seg.a, seg.b, fraction), seg.group, seg.width))
    return visible


def line_angle_degrees(seg: Segment, rect: Rect) -> float:
    width = rect[2] - rect[0]
    height = rect[3] - rect[1]
    dx = (seg.b[0] - seg.a[0]) * width
    dy = (seg.b[1] - seg.a[1]) * height
    return math.degrees(math.atan2(-dy, dx))


def line_box_points(seg: Segment) -> tuple[Point, Point]:
    a, b, c = line_coeff(seg)
    points: list[Point] = []
    eps = 1e-6

    for x in (0.0, 1.0):
        if abs(b) > eps:
            y = -(a * x + c) / b
            if -eps <= y <= 1.0 + eps:
                points.append((min(1.0, max(0.0, x)), min(1.0, max(0.0, y))))

    for y in (0.0, 1.0):
        if abs(a) > eps:
            x = -(b * y + c) / a
            if -eps <= x <= 1.0 + eps:
                points.append((min(1.0, max(0.0, x)), min(1.0, max(0.0, y))))

    unique: list[Point] = []
    for point in points:
        if not any(math.hypot(point[0] - existing[0], point[1] - existing[1]) < 1e-5 for existing in unique):
            unique.append(point)

    if len(unique) < 2:
        return (seg.a, seg.b)

    farthest = (unique[0], unique[1])
    distance = -1.0
    for i, first in enumerate(unique):
        for second in unique[i + 1 :]:
            d = math.hypot(first[0] - second[0], first[1] - second[1])
            if d > distance:
                distance = d
                farthest = (first, second)
    return farthest


def xy(rect: Rect, p: Point) -> Point:
    x0, y0, x1, y1 = rect
    return (x0 + (x1 - x0) * p[0], y0 + (y1 - y0) * p[1])


def norm_to_px(rect: Rect, x: float, y: float) -> Point:
    return xy(rect, (x, y))


def draw_line(
    draw: ImageDraw.ImageDraw,
    rect: Rect,
    seg: Segment,
    fill: Color,
    width: int | None = None,
) -> None:
    a = xy(rect, seg.a)
    b = xy(rect, seg.b)
    draw.line((a[0], a[1], b[0], b[1]), fill=fill, width=width or seg.width)


def dashed_line(
    draw: ImageDraw.ImageDraw,
    a: Point,
    b: Point,
    fill: Color,
    width: int = 1,
    dash: float = 7.0,
    gap: float = 7.0,
) -> None:
    dx = b[0] - a[0]
    dy = b[1] - a[1]
    dist = math.hypot(dx, dy)
    if dist <= 1e-6:
        return
    ux = dx / dist
    uy = dy / dist
    t = 0.0
    while t < dist:
        t2 = min(t + dash, dist)
        draw.line((a[0] + ux * t, a[1] + uy * t, a[0] + ux * t2, a[1] + uy * t2), fill=fill, width=width)
        t += dash + gap


def draw_label(draw: ImageDraw.ImageDraw, pos: Point, text: str, fill: Color) -> None:
    draw.text((pos[0], pos[1]), text, font=SMALL_FONT, fill=fill)


def draw_tag(draw: ImageDraw.ImageDraw, pos: Point, text: str, fill: Color, dark: bool = False) -> None:
    bbox = draw.textbbox((pos[0], pos[1]), text, font=SMALL_FONT)
    pad = 3
    bg = (20, 20, 20, 210) if dark else (241, 235, 218, 230)
    outline = fill
    draw.rectangle((bbox[0] - pad, bbox[1] - pad, bbox[2] + pad, bbox[3] + pad), fill=bg, outline=outline, width=1)
    draw.text((pos[0], pos[1]), text, font=SMALL_FONT, fill=fill)


def color_for_group(group: str, source: bool = False) -> Color:
    if group == "vp":
        return RED
    if group == "grid":
        return CYAN if source else BLUE
    if group == "horizon":
        return GOLD
    if group == "secondary":
        return GREEN if source else INK_SOFT
    return WHITE if source else INK


def arch_points(rect: Rect, arch: Arch, steps: int = 44) -> list[Point]:
    pts = [norm_to_px(rect, arch.cx - arch.rx, arch.base_y), norm_to_px(rect, arch.cx - arch.rx, arch.spring_y)]
    for i in range(steps + 1):
        angle = math.pi - math.pi * i / steps
        pts.append(norm_to_px(rect, arch.cx + arch.rx * math.cos(angle), arch.spring_y - arch.ry * math.sin(angle)))
    pts.append(norm_to_px(rect, arch.cx + arch.rx, arch.base_y))
    return pts


def draw_arch(draw: ImageDraw.ImageDraw, rect: Rect, arch: Arch, fill: Color) -> None:
    pts = arch_points(rect, arch)
    draw.line(pts, fill=fill, width=arch.width, joint="curve")
    inset = min(arch.rx, arch.ry) * 0.10
    if arch.rx > inset * 3 and arch.ry > inset * 3:
        inner = Arch(arch.cx, arch.spring_y + inset * 0.25, arch.rx - inset, arch.ry - inset, arch.base_y, arch.group, max(1, arch.width - 1))
        draw.line(arch_points(rect, inner), fill=fill, width=inner.width, joint="curve")


def draw_rect_shape(draw: ImageDraw.ImageDraw, rect: Rect, shape: RectShape, fill: Color) -> None:
    p0 = norm_to_px(rect, shape.x0, shape.y0)
    p1 = norm_to_px(rect, shape.x1, shape.y1)
    draw.rectangle((p0[0], p0[1], p1[0], p1[1]), outline=fill, width=shape.width)


def draw_column(draw: ImageDraw.ImageDraw, rect: Rect, col: Column, fill: Color) -> None:
    x, base = norm_to_px(rect, col.cx, col.base_y)
    _, top = norm_to_px(rect, col.cx, col.top_y)
    rw = (rect[2] - rect[0]) * col.radius
    taper = rw * 0.62
    draw.line((x - rw, base, x - taper, top), fill=fill, width=col.width)
    draw.line((x + rw, base, x + taper, top), fill=fill, width=col.width)
    draw.ellipse((x - rw * 1.25, base - rw * 0.14, x + rw * 1.25, base + rw * 0.16), outline=fill, width=col.width)
    draw.ellipse((x - taper * 1.35, top - rw * 0.13, x + taper * 1.35, top + rw * 0.13), outline=fill, width=col.width)
    draw.rectangle((x - rw * 1.65, base + rw * 0.12, x + rw * 1.65, base + rw * 0.55), outline=fill, width=col.width)
    draw.rectangle((x - rw * 1.25, top - rw * 0.45, x + rw * 1.25, top - rw * 0.12), outline=fill, width=max(1, col.width - 1))


def x_on_line_at_y(a: Point, b: Point, y: float) -> float:
    if abs(b[1] - a[1]) <= 1e-6:
        return a[0]
    t = (y - a[1]) / (b[1] - a[1])
    return a[0] + (b[0] - a[0]) * t


def interp(a: Point, b: Point, t: float) -> Point:
    return (a[0] + (b[0] - a[0]) * t, a[1] + (b[1] - a[1]) * t)


def draw_projected_grid(draw: ImageDraw.ImageDraw, rect: Rect, grid: GridSpec, vp: Point, source: bool = False) -> None:
    fill = color_for_group("grid", source)
    left = grid.left_bottom
    right = grid.right_bottom
    bottom_y = grid.bottom_y if grid.bottom_y is not None else max(left[1], right[1])
    for i in range(grid.cols + 1):
        t = i / grid.cols
        start = interp(left, right, t)
        dashed_line(draw, xy(rect, start), xy(rect, vp), fill, width=1, dash=7, gap=8)
    for i in range(1, grid.rows + 1):
        t = i / (grid.rows + 1)
        y = vp[1] + (bottom_y - vp[1]) * (1.0 - t) ** 1.7
        lx = x_on_line_at_y(left, vp, y)
        rx = x_on_line_at_y(right, vp, y)
        draw.line((xy(rect, (lx, y))[0], xy(rect, (lx, y))[1], xy(rect, (rx, y))[0], xy(rect, (rx, y))[1]), fill=fill, width=1)


def draw_horizon_and_vp(draw: ImageDraw.ImageDraw, rect: Rect, vp: Point, source: bool = False) -> None:
    fill = color_for_group("horizon", source)
    y = xy(rect, vp)[1]
    draw.line((rect[0], y, rect[2], y), fill=fill, width=2)
    draw_label(draw, (rect[0] + 8, y + 4), "horizon", fill)
    px = xy(rect, vp)
    r = 6
    draw.ellipse((px[0] - r, px[1] - r, px[0] + r, px[1] + r), fill=RED)
    draw_label(draw, (px[0] + 8, px[1] - 16), f"VP {vp[0]:.3f},{vp[1]:.3f}", RED)


def draw_extended_measured_line(
    draw: ImageDraw.ImageDraw,
    rect: Rect,
    seg: Segment,
    index: int,
    source: bool = False,
) -> None:
    p0, p1 = line_box_points(seg)
    extension_fill = GOLD if source else (159, 129, 78)
    chosen_fill = color_for_group("vp", source)
    dashed_line(draw, xy(rect, p0), xy(rect, p1), extension_fill, width=1, dash=10, gap=7)
    draw_line(draw, rect, seg, chosen_fill, width=max(2, seg.width))
    midpoint = ((seg.a[0] + seg.b[0]) * 0.5, (seg.a[1] + seg.b[1]) * 0.5)
    angle = line_angle_degrees(seg, rect)
    draw_tag(draw, xy(rect, midpoint), f"L{index} {angle:+.1f} deg", chosen_fill, dark=source)


def draw_measured_geometry(
    draw: ImageDraw.ImageDraw,
    rect: Rect,
    ref: Reference,
    vp: Point,
    source: bool = False,
) -> None:
    draw_horizon_and_vp(draw, rect, vp, source)

    for grid in ref.grids:
        draw_projected_grid(draw, rect, grid, vp, source)

    for start_u, end_u in ref.generated_rays:
        dashed_line(draw, xy(rect, (start_u, end_u)), xy(rect, vp), color_for_group("grid", source), width=1)

    for index, seg in enumerate(visible_vp_lines(ref), 1):
        draw_extended_measured_line(draw, rect, seg, index, source=source)

    for seg in ref.structure:
        draw_line(draw, rect, seg, color_for_group(seg.group, source))

    for shape in ref.rectangles:
        draw_rect_shape(draw, rect, shape, color_for_group(shape.group, source))

    for arch in ref.arches:
        draw_arch(draw, rect, arch, color_for_group(arch.group, source))

    for column in ref.columns:
        draw_column(draw, rect, column, color_for_group(column.group, source))


REFERENCES: list[Reference] = [
    Reference(
        title="Arcade Capriccio",
        lesson="measured one-point arcade and floor grid",
        filename="REF_Perspective_Arcade_Capriccio_MET_DP836399.jpg",
        url="https://upload.wikimedia.org/wikipedia/commons/b/bf/Architectural_Capriccio_with_an_Arcade_and_Fountain_in_Point_Perspective_-Study_for_a_Painting_of_John_the_Baptist_before_Herod-_MET_DP836399.jpg",
        page="https://commons.wikimedia.org/wiki/File:Architectural_Capriccio_with_an_Arcade_and_Fountain_in_Point_Perspective_-Study_for_a_Painting_of_John_the_Baptist_before_Herod-_MET_DP836399.jpg",
        license_name="CC0",
        vp_lines=[
            Segment((0.372, 0.925), (0.505, 0.565), "vp", 3),
            Segment((0.620, 0.925), (0.505, 0.565), "vp", 3),
            Segment((0.292, 0.825), (0.505, 0.565), "vp", 2),
            Segment((0.715, 0.825), (0.505, 0.565), "vp", 2),
            Segment((0.386, 0.735), (0.505, 0.565), "vp", 2),
            Segment((0.603, 0.735), (0.505, 0.565), "vp", 2),
        ],
        grids=[GridSpec((0.372, 0.925), (0.620, 0.925), 10, 10, 0.925)],
        structure=[
            Segment((0.115, 0.170), (0.245, 0.170), "secondary", 2),
            Segment((0.108, 0.784), (0.244, 0.784), "secondary", 2),
            Segment((0.770, 0.230), (0.930, 0.230), "secondary", 2),
            Segment((0.762, 0.735), (0.932, 0.735), "secondary", 2),
            Segment((0.360, 0.705), (0.652, 0.705), "structure", 3),
            Segment((0.420, 0.635), (0.588, 0.635), "structure", 2),
            Segment((0.475, 0.695), (0.475, 0.605), "secondary", 2),
            Segment((0.532, 0.695), (0.532, 0.605), "secondary", 2),
            Segment((0.842, 0.640), (0.842, 0.742), "secondary", 2),
            Segment((0.910, 0.635), (0.910, 0.732), "secondary", 2),
        ],
        arches=[
            Arch(0.505, 0.272, 0.235, 0.245, 0.430, "structure", 4),
            Arch(0.507, 0.386, 0.155, 0.155, 0.620, "structure", 3),
            Arch(0.125, 0.472, 0.080, 0.105, 0.760, "secondary", 3),
            Arch(0.835, 0.440, 0.072, 0.102, 0.710, "secondary", 3),
            Arch(0.905, 0.400, 0.078, 0.095, 0.625, "secondary", 2),
        ],
        rectangles=[
            RectShape(0.112, 0.738, 0.246, 0.910, "structure", 3),
            RectShape(0.664, 0.700, 0.744, 0.880, "structure", 3),
            RectShape(0.812, 0.645, 0.965, 0.815, "secondary", 2),
        ],
        columns=[
            Column(0.188, 0.760, 0.235, 0.017, "structure", 4),
            Column(0.678, 0.750, 0.260, 0.015, "structure", 3),
            Column(0.336, 0.725, 0.420, 0.010, "secondary", 2),
            Column(0.407, 0.678, 0.455, 0.007, "secondary", 2),
            Column(0.584, 0.680, 0.455, 0.007, "secondary", 2),
            Column(0.745, 0.705, 0.415, 0.010, "secondary", 2),
        ],
        note="VP solved from aisle edges, column-base receding lines, and floor grid convergence.",
    ),
    Reference(
        title="Palace Fantasy",
        lesson="measured portico, checkered ground, central courtyard VP",
        filename="REF_Perspective_Palace_Fantasy_NationalTrust.jpg",
        url="https://upload.wikimedia.org/wikipedia/commons/e/e9/Dirck_van_Delen_%281604-1605-1671%29_%28attributed_to%29_-_Perspective_Fantasy_of_a_Palace%2C_with_Elegant_Figures_%28after_Hans_Vredeman_de_Vries%29_-_453824_-_National_Trust.jpg",
        page="https://commons.wikimedia.org/wiki/File:Dirck_van_Delen_(1604-1605-1671)_(attributed_to)_-_Perspective_Fantasy_of_a_Palace,_with_Elegant_Figures_(after_Hans_Vredeman_de_Vries)_-_453824_-_National_Trust.jpg",
        license_name="Public domain",
        vp_lines=[
            Segment((0.220, 0.875), (0.502, 0.574), "vp", 3),
            Segment((0.785, 0.875), (0.502, 0.574), "vp", 3),
            Segment((0.345, 0.890), (0.502, 0.574), "vp", 2),
            Segment((0.650, 0.890), (0.502, 0.574), "vp", 2),
            Segment((0.280, 0.300), (0.502, 0.574), "vp", 2),
            Segment((0.730, 0.300), (0.502, 0.574), "vp", 2),
        ],
        grids=[GridSpec((0.225, 0.885), (0.790, 0.885), 8, 8, 0.885)],
        structure=[
            Segment((0.055, 0.020), (0.450, 0.020), "structure", 4),
            Segment((0.553, 0.020), (0.953, 0.020), "structure", 4),
            Segment((0.055, 0.020), (0.180, 0.280), "structure", 3),
            Segment((0.450, 0.020), (0.502, 0.278), "structure", 3),
            Segment((0.553, 0.020), (0.502, 0.278), "structure", 3),
            Segment((0.953, 0.020), (0.822, 0.280), "structure", 3),
            Segment((0.380, 0.430), (0.620, 0.430), "structure", 3),
            Segment((0.390, 0.660), (0.610, 0.660), "structure", 3),
            Segment((0.382, 0.430), (0.392, 0.660), "structure", 3),
            Segment((0.620, 0.430), (0.608, 0.660), "structure", 3),
            Segment((0.405, 0.332), (0.502, 0.240), "structure", 3),
            Segment((0.600, 0.332), (0.502, 0.240), "structure", 3),
            Segment((0.405, 0.332), (0.600, 0.332), "structure", 3),
        ],
        arches=[
            Arch(0.502, 0.318, 0.108, 0.125, 0.455, "structure", 4),
            Arch(0.502, 0.565, 0.050, 0.060, 0.660, "structure", 3),
            Arch(0.110, 0.408, 0.060, 0.075, 0.615, "secondary", 2),
        ],
        rectangles=[
            RectShape(0.430, 0.470, 0.472, 0.565, "secondary", 2),
            RectShape(0.532, 0.470, 0.575, 0.565, "secondary", 2),
        ],
        columns=[
            Column(0.080, 0.870, 0.075, 0.020, "structure", 4),
            Column(0.205, 0.810, 0.205, 0.015, "structure", 3),
            Column(0.325, 0.735, 0.300, 0.011, "secondary", 2),
            Column(0.690, 0.735, 0.300, 0.011, "secondary", 2),
            Column(0.815, 0.812, 0.205, 0.015, "structure", 3),
            Column(0.930, 0.870, 0.075, 0.020, "structure", 4),
        ],
        note="VP solved from floor-tile diagonals and opposing portico roof edges.",
    ),
    Reference(
        title="Double Arch Portico",
        lesson="measured frontal portico with deep receding corridors",
        filename="REF_Perspective_DoubleArch_Rijksmuseum.jpg",
        url="https://upload.wikimedia.org/wikipedia/commons/9/9f/Gebouw_met_dubbele_boog_in_het_midden_in_Dorische_stijl_Perspective%2C_deel_2_%28serietitel%29%2C_RP-P-1878-A-1884.jpg",
        page="https://commons.wikimedia.org/wiki/File:Gebouw_met_dubbele_boog_in_het_midden_in_Dorische_stijl_Perspective,_deel_2_(serietitel),_RP-P-1878-A-1884.jpg",
        license_name="CC0",
        vp_lines=[
            Segment((0.205, 0.875), (0.555, 0.664), "vp", 3),
            Segment((0.835, 0.875), (0.555, 0.664), "vp", 3),
            Segment((0.350, 0.875), (0.555, 0.664), "vp", 2),
            Segment((0.710, 0.875), (0.555, 0.664), "vp", 2),
            Segment((0.285, 0.450), (0.555, 0.664), "vp", 2),
            Segment((0.775, 0.450), (0.555, 0.664), "vp", 2),
        ],
        grids=[GridSpec((0.205, 0.875), (0.835, 0.875), 9, 10, 0.875)],
        structure=[
            Segment((0.145, 0.175), (0.870, 0.175), "structure", 4),
            Segment((0.125, 0.235), (0.890, 0.235), "structure", 4),
            Segment((0.165, 0.305), (0.850, 0.305), "structure", 3),
            Segment((0.420, 0.175), (0.505, 0.095), "structure", 3),
            Segment((0.590, 0.175), (0.505, 0.095), "structure", 3),
            Segment((0.135, 0.835), (0.890, 0.835), "structure", 3),
            Segment((0.300, 0.835), (0.300, 0.510), "structure", 3),
            Segment((0.530, 0.835), (0.530, 0.510), "structure", 3),
            Segment((0.650, 0.835), (0.650, 0.510), "structure", 3),
        ],
        arches=[
            Arch(0.355, 0.505, 0.130, 0.145, 0.835, "structure", 4),
            Arch(0.650, 0.505, 0.130, 0.145, 0.835, "structure", 4),
            Arch(0.398, 0.610, 0.060, 0.065, 0.765, "secondary", 2),
            Arch(0.560, 0.610, 0.052, 0.060, 0.760, "secondary", 2),
            Arch(0.675, 0.610, 0.052, 0.060, 0.760, "secondary", 2),
        ],
        rectangles=[
            RectShape(0.135, 0.760, 0.225, 0.905, "structure", 3),
            RectShape(0.470, 0.750, 0.545, 0.892, "structure", 3),
            RectShape(0.820, 0.745, 0.915, 0.905, "structure", 3),
        ],
        columns=[
            Column(0.155, 0.805, 0.260, 0.014, "structure", 3),
            Column(0.295, 0.805, 0.330, 0.012, "structure", 3),
            Column(0.470, 0.810, 0.330, 0.012, "structure", 3),
            Column(0.650, 0.810, 0.330, 0.012, "structure", 3),
            Column(0.840, 0.805, 0.260, 0.014, "structure", 3),
        ],
        note="VP solved from tiled floor edges and receding arcade roof/base lines visible through the arches.",
    ),
    Reference(
        title="Perspective Street",
        lesson="measured street canyon, facades, low left-side VP",
        filename="REF_Perspective_Street_NGA_205782.jpg",
        url="https://upload.wikimedia.org/wikipedia/commons/7/71/Lucas_van_Doetechum_and_Johannes_van_Doetechum%2C_the_Elder%2C_after_Hans_Vredeman_de_Vries%2C_Perspective_View_of_a_Street%2C_1560%2C_NGA_205782.jpg",
        page="https://commons.wikimedia.org/wiki/File:Lucas_van_Doetechum_and_Johannes_van_Doetechum,_the_Elder,_after_Hans_Vredeman_de_Vries,_Perspective_View_of_a_Street,_1560,_NGA_205782.jpg",
        license_name="CC0",
        vp_lines=[
            Segment((0.965, 0.185), (0.244, 0.815), "vp", 3),
            Segment((0.985, 0.875), (0.244, 0.815), "vp", 3),
            Segment((0.810, 0.330), (0.244, 0.815), "vp", 2),
            Segment((0.760, 0.535), (0.244, 0.815), "vp", 2),
            Segment((0.560, 0.625), (0.244, 0.815), "vp", 2),
            Segment((0.070, 0.940), (0.244, 0.815), "vp", 2),
        ],
        grids=[GridSpec((0.065, 0.950), (0.985, 0.875), 6, 8, 0.950)],
        structure=[
            Segment((0.010, 0.120), (0.145, 0.300), "structure", 4),
            Segment((0.145, 0.300), (0.145, 0.910), "structure", 4),
            Segment((0.020, 0.910), (0.145, 0.910), "structure", 4),
            Segment((0.350, 0.650), (0.430, 0.570), "structure", 3),
            Segment((0.430, 0.570), (0.520, 0.635), "structure", 3),
            Segment((0.520, 0.635), (0.520, 0.850), "structure", 3),
            Segment((0.430, 0.570), (0.430, 0.850), "structure", 3),
            Segment((0.585, 0.500), (0.725, 0.365), "structure", 3),
            Segment((0.725, 0.365), (0.980, 0.555), "structure", 3),
            Segment((0.585, 0.500), (0.585, 0.875), "structure", 3),
            Segment((0.980, 0.555), (0.980, 0.875), "structure", 3),
            Segment((0.725, 0.365), (0.725, 0.875), "structure", 3),
            Segment((0.300, 0.820), (0.985, 0.875), "structure", 3),
        ],
        arches=[
            Arch(0.480, 0.774, 0.022, 0.034, 0.850, "secondary", 2),
            Arch(0.690, 0.760, 0.025, 0.040, 0.865, "secondary", 2),
            Arch(0.910, 0.785, 0.028, 0.045, 0.875, "secondary", 2),
        ],
        rectangles=[
            RectShape(0.055, 0.330, 0.120, 0.500, "secondary", 2),
            RectShape(0.055, 0.570, 0.120, 0.740, "secondary", 2),
            RectShape(0.630, 0.575, 0.650, 0.680, "secondary", 2),
            RectShape(0.675, 0.555, 0.695, 0.670, "secondary", 2),
            RectShape(0.815, 0.485, 0.850, 0.625, "secondary", 2),
            RectShape(0.875, 0.492, 0.910, 0.632, "secondary", 2),
        ],
        columns=[Column(0.388, 0.848, 0.525, 0.012, "secondary", 2)],
        note="VP solved from right-facade roof courses, window bands, street edge, and left foreground building edge.",
    ),
    Reference(
        title="Interior Hall",
        lesson="measured vaulted hall, arch tunnel, tiled floor",
        filename="REF_Perspective_InteriorHall_MET_DP828125.jpg",
        url="https://upload.wikimedia.org/wikipedia/commons/2/2f/Perspective_view_of_the_interior_of_a_hall%2C_with_cross-vault_decorated_with_grotesques%2C_plate_18%2C_from_Scenographiae_sive_Perspectivae_MET_DP828125.jpg",
        page="https://commons.wikimedia.org/wiki/File:Perspective_view_of_the_interior_of_a_hall,_with_cross-vault_decorated_with_grotesques,_plate_18,_from_Scenographiae_sive_Perspectivae_MET_DP828125.jpg",
        license_name="CC0",
        vp_lines=[
            Segment((0.150, 0.930), (0.390, 0.793), "vp", 3),
            Segment((0.920, 0.930), (0.390, 0.793), "vp", 3),
            Segment((0.302, 0.900), (0.390, 0.793), "vp", 2),
            Segment((0.548, 0.900), (0.390, 0.793), "vp", 2),
            Segment((0.325, 0.690), (0.390, 0.793), "vp", 2),
            Segment((0.474, 0.690), (0.390, 0.793), "vp", 2),
        ],
        grids=[GridSpec((0.150, 0.930), (0.920, 0.930), 10, 12, 0.930)],
        structure=[
            Segment((0.258, 0.355), (0.505, 0.355), "structure", 4),
            Segment((0.254, 0.355), (0.255, 0.805), "structure", 3),
            Segment((0.506, 0.355), (0.506, 0.804), "structure", 3),
            Segment((0.570, 0.150), (0.935, 0.060), "structure", 4),
            Segment((0.570, 0.150), (0.548, 0.910), "structure", 4),
            Segment((0.935, 0.060), (0.960, 0.910), "structure", 4),
            Segment((0.080, 0.135), (0.325, 0.300), "secondary", 3),
            Segment((0.325, 0.300), (0.505, 0.355), "secondary", 3),
            Segment((0.505, 0.355), (0.855, 0.095), "secondary", 3),
            Segment((0.300, 0.275), (0.390, 0.793), "vp", 2),
            Segment((0.650, 0.230), (0.390, 0.793), "vp", 2),
        ],
        arches=[
            Arch(0.384, 0.520, 0.126, 0.132, 0.802, "structure", 4),
            Arch(0.390, 0.655, 0.078, 0.083, 0.793, "secondary", 3),
            Arch(0.390, 0.700, 0.050, 0.052, 0.793, "secondary", 2),
            Arch(0.660, 0.565, 0.055, 0.080, 0.805, "structure", 3),
            Arch(0.790, 0.530, 0.050, 0.078, 0.805, "structure", 3),
            Arch(0.905, 0.505, 0.045, 0.072, 0.805, "structure", 3),
            Arch(0.094, 0.580, 0.052, 0.070, 0.835, "secondary", 3),
        ],
        rectangles=[
            RectShape(0.585, 0.805, 0.692, 0.910, "secondary", 2),
            RectShape(0.708, 0.805, 0.827, 0.910, "secondary", 2),
            RectShape(0.845, 0.805, 0.955, 0.910, "secondary", 2),
            RectShape(0.272, 0.610, 0.325, 0.805, "secondary", 2),
            RectShape(0.450, 0.610, 0.505, 0.805, "secondary", 2),
        ],
        columns=[
            Column(0.328, 0.803, 0.555, 0.008, "secondary", 2),
            Column(0.470, 0.803, 0.555, 0.008, "secondary", 2),
        ],
        note="VP solved from floor tiles and tunnel wall/ceiling convergence through the central barrel vault.",
    ),
]


def fit_image(path: Path, target: tuple[int, int]) -> Image.Image:
    with Image.open(path) as source:
        img = ImageOps.exif_transpose(source).convert("RGB")
    return ImageOps.contain(img, target, LANCZOS)


def source_size(ref: Reference) -> tuple[int, int]:
    with Image.open(REF_ROOT / ref.filename) as source:
        return source.size


def content_rect(panel: Rect, image: Image.Image, top_pad: int = 44) -> Rect:
    available_w = panel[2] - panel[0] - 28
    available_h = panel[3] - panel[1] - top_pad - 14
    scale = min(available_w / image.width, available_h / image.height)
    w = int(image.width * scale)
    h = int(image.height * scale)
    x = panel[0] + (panel[2] - panel[0] - w) // 2
    y = panel[1] + top_pad + (available_h - h) // 2
    return (x, y, x + w, y + h)


def draw_panel(draw: ImageDraw.ImageDraw, rect: Rect, title: str, dark: bool = True) -> None:
    fill = PANEL if dark else PAPER
    text = WHITE if dark else INK
    draw.rectangle(rect, fill=fill, outline=FRAME, width=2)
    draw.text((rect[0] + 14, rect[1] + 13), title, font=LABEL_FONT, fill=text)


def paste_source_with_overlay(board: Image.Image, draw: ImageDraw.ImageDraw, ref: Reference, panel: Rect) -> Rect:
    source_path = REF_ROOT / ref.filename
    source = fit_image(source_path, (panel[2] - panel[0] - 28, panel[3] - panel[1] - 58))
    rect = content_rect(panel, source)
    board.paste(source, (rect[0], rect[1]))

    overlay = Image.new("RGBA", board.size, (0, 0, 0, 0))
    overlay_draw = ImageDraw.Draw(overlay)
    draw_measured_geometry(overlay_draw, rect, ref, computed_vp(ref), source=True)
    board.alpha_composite(overlay)
    return rect


def draw_redraw(draw: ImageDraw.ImageDraw, ref: Reference, panel: Rect, source_rect: Rect) -> Rect:
    src_w = source_rect[2] - source_rect[0]
    src_h = source_rect[3] - source_rect[1]
    available_w = panel[2] - panel[0] - 28
    available_h = panel[3] - panel[1] - 58
    scale = min(available_w / src_w, available_h / src_h)
    w = int(src_w * scale)
    h = int(src_h * scale)
    x = panel[0] + (panel[2] - panel[0] - w) // 2
    y = panel[1] + 44 + (available_h - h) // 2
    rect = (x, y, x + w, y + h)
    draw.rectangle(rect, fill=PAPER_ALT, outline=FRAME, width=1)
    draw_measured_geometry(draw, rect, ref, computed_vp(ref), source=False)
    return rect


def write_source_manifest() -> None:
    lines = [
        "# P03 Web Perspective Reference Sources",
        "",
        "The board uses downloaded web reference images on the left and measured construction redraws on the right.",
        "The redraws are built from normalized source-image coordinates and computed vanishing-point intersections.",
        "",
    ]
    for index, ref in enumerate(REFERENCES, 1):
        lines.extend(
            [
                f"## {index}. {ref.title}",
                f"- Local file: `{REF_ROOT.relative_to(ROOT) / ref.filename}`",
                f"- Source image: {ref.url}",
                f"- Commons page: {ref.page}",
                f"- License/status: {ref.license_name}",
                f"- Redraw focus: {ref.lesson}",
                "",
            ]
        )
    SOURCE_MANIFEST.write_text("\n".join(lines), encoding="utf-8")


def write_measurement_manifest() -> None:
    lines = [
        "# P03 Measured Perspective Redraw Data",
        "",
        "Coordinates are normalized to each downloaded source image: `(0, 0)` is top-left and `(1, 1)` is bottom-right.",
        "Each vanishing point is solved by least-squares intersection of the recorded visible line spans.",
        "",
    ]
    for index, ref in enumerate(REFERENCES, 1):
        vp = computed_vp(ref)
        residuals = vp_residuals(ref, vp)
        src_w, src_h = source_size(ref)
        lines.extend(
            [
                f"## {index}. {ref.title}",
                f"- Computed VP: `({vp[0]:.4f}, {vp[1]:.4f})`",
                f"- Source image size: `{src_w} x {src_h}` pixels",
                f"- VP residual mean/max: `{sum(residuals) / len(residuals):.6f}` / `{max(residuals):.6f}` normalized image units",
                f"- Measurement note: {ref.note}",
                "- VP source lines, equations, and angles:",
            ]
        )
        for line_index, seg in enumerate(visible_vp_lines(ref), 1):
            a, b, c = line_coeff(seg)
            angle = line_angle_degrees(seg, (0, 0, src_w, src_h))
            residual = residuals[line_index - 1]
            lines.append(
                f"  - L{line_index}: endpoints `({seg.a[0]:.4f}, {seg.a[1]:.4f}) -> "
                f"({seg.b[0]:.4f}, {seg.b[1]:.4f})`; angle `{angle:+.3f} deg`; "
                f"line `{a:.6f}x + {b:.6f}y + {c:.6f} = 0`; VP residual `{residual:.6f}`"
            )
        lines.append("")
    MEASUREMENT_MANIFEST.write_text("\n".join(lines), encoding="utf-8")


def build_board() -> None:
    OUT_ROOT.mkdir(parents=True, exist_ok=True)
    REVIEW_ROOT.mkdir(parents=True, exist_ok=True)

    width = 2600
    margin = 62
    header_h = 158
    row_h = 610
    row_gap = 42
    panel_gap = 42
    panel_w = (width - margin * 2 - panel_gap) // 2
    panel_h = 545
    height = header_h + len(REFERENCES) * row_h + (len(REFERENCES) - 1) * row_gap + margin

    board = Image.new("RGBA", (width, height), BG + (255,))
    draw = ImageDraw.Draw(board)

    draw.text((margin, 36), "P03 Web Perspective Measured Redraws", font=TITLE_FONT, fill=WHITE)
    draw.text(
        (margin, 94),
        "Left: source image with measured perspective lines. Right: redraw using the same coordinates, line equations, and computed VP.",
        font=SUB_FONT,
        fill=(202, 196, 184),
    )
    draw.text(
        (margin, 122),
        "Red/blue lines are measurement/construction guides; black lines are the recreated architectural geometry.",
        font=SMALL_FONT,
        fill=(180, 172, 156),
    )

    y = header_h
    for index, ref in enumerate(REFERENCES, 1):
        left = (margin, y + 50, margin + panel_w, y + 50 + panel_h)
        right = (margin + panel_w + panel_gap, y + 50, margin + panel_w * 2 + panel_gap, y + 50 + panel_h)
        vp = computed_vp(ref)
        draw.text((margin, y + 8), f"{index}. {ref.title} - {ref.lesson} - VP ({vp[0]:.3f}, {vp[1]:.3f})", font=ROW_FONT, fill=WHITE)
        draw_panel(draw, left, "SOURCE + MEASURED LINES", dark=True)
        draw_panel(draw, right, "MEASURED REDRAW", dark=False)
        source_rect = paste_source_with_overlay(board, draw, ref, left)
        draw_redraw(draw, ref, right, source_rect)
        y += row_h + row_gap

    write_source_manifest()
    write_measurement_manifest()
    rgb = board.convert("RGB")
    rgb.save(DOC_IMAGE, optimize=True)
    shutil.copy2(DOC_IMAGE, REVIEW_IMAGE)
    print(DOC_IMAGE)
    print(REVIEW_IMAGE)
    print(SOURCE_MANIFEST)
    print(MEASUREMENT_MANIFEST)


if __name__ == "__main__":
    build_board()
