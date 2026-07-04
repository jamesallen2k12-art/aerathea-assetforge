#!/usr/bin/env python3
"""Build an exact perspective drawing training board.

The board is original training material. It uses internet-sourced perspective
rules, but the drawings are generated from pinhole projection formulas instead
of traced from outside images.
"""

from __future__ import annotations

import math
from dataclasses import dataclass
from pathlib import Path
from typing import Callable, Iterable

from PIL import Image, ImageDraw, ImageFont


ROOT = Path(__file__).resolve().parents[2]
OUT_ROOT = ROOT / "docs" / "assets" / "training" / "perspective_drawing"
REVIEW_ROOT = ROOT / "Saved" / "Automation" / "DCC" / "PerspectiveDrawing"
BOARD_NAME = "P02_PerspectiveDrawing_ExactRedrawBoard"
DOC_IMAGE = OUT_ROOT / f"{BOARD_NAME}.png"
REVIEW_IMAGE = REVIEW_ROOT / f"{BOARD_NAME}.png"

BG = (29, 29, 30)
PANEL = (44, 44, 45)
PANEL_EDGE = (108, 100, 84)
INK = (232, 226, 214)
STRONG = (18, 18, 18)
CLEAN = (16, 18, 21)
GUIDE = (92, 126, 168)
GUIDE_LIGHT = (120, 151, 191)
HORIZON = (191, 151, 76)
VANISH = (199, 83, 76)
MEASURE = (128, 155, 105)
FACE_A = (212, 204, 184)
FACE_B = (174, 188, 192)
FACE_C = (143, 156, 166)


Point2 = tuple[float, float]
Point3 = tuple[float, float, float]
Rect = tuple[int, int, int, int]


def v_add(a: Point3, b: Point3) -> Point3:
    return (a[0] + b[0], a[1] + b[1], a[2] + b[2])


def v_sub(a: Point3, b: Point3) -> Point3:
    return (a[0] - b[0], a[1] - b[1], a[2] - b[2])


def v_mul(a: Point3, scalar: float) -> Point3:
    return (a[0] * scalar, a[1] * scalar, a[2] * scalar)


def dot(a: Point3, b: Point3) -> float:
    return a[0] * b[0] + a[1] * b[1] + a[2] * b[2]


def cross(a: Point3, b: Point3) -> Point3:
    return (
        a[1] * b[2] - a[2] * b[1],
        a[2] * b[0] - a[0] * b[2],
        a[0] * b[1] - a[1] * b[0],
    )


def length(a: Point3) -> float:
    return math.sqrt(dot(a, a))


def normalize(a: Point3) -> Point3:
    mag = length(a)
    if mag <= 1e-9:
        return (0.0, 0.0, 0.0)
    return (a[0] / mag, a[1] / mag, a[2] / mag)


def yaw_axes(yaw_degrees: float) -> tuple[Point3, Point3, Point3]:
    yaw = math.radians(yaw_degrees)
    u = (math.cos(yaw), 0.0, math.sin(yaw))
    v = (0.0, 1.0, 0.0)
    w = (-math.sin(yaw), 0.0, math.cos(yaw))
    return u, v, w


@dataclass
class Camera:
    position: Point3
    target: Point3
    focal: float

    def __post_init__(self) -> None:
        world_up = (0.0, 1.0, 0.0)
        self.forward = normalize(v_sub(self.target, self.position))
        self.right = normalize(cross(world_up, self.forward))
        self.up = normalize(cross(self.forward, self.right))

    def camera_space(self, point: Point3) -> Point3:
        rel = v_sub(point, self.position)
        return (dot(rel, self.right), dot(rel, self.up), dot(rel, self.forward))

    def direction_space(self, direction: Point3) -> Point3:
        return (dot(direction, self.right), dot(direction, self.up), dot(direction, self.forward))

    def project(self, point: Point3, rect: Rect) -> Point2 | None:
        x, y, z = self.camera_space(point)
        if z <= 0.05:
            return None
        cx = (rect[0] + rect[2]) * 0.5
        cy = (rect[1] + rect[3]) * 0.5
        return (cx + self.focal * x / z, cy - self.focal * y / z)

    def vp(self, direction: Point3, rect: Rect) -> Point2 | None:
        x, y, z = self.direction_space(direction)
        if abs(z) <= 1e-6:
            return None
        cx = (rect[0] + rect[2]) * 0.5
        cy = (rect[1] + rect[3]) * 0.5
        return (cx + self.focal * x / z, cy - self.focal * y / z)


def load_font(size: int, bold: bool = False) -> ImageFont.ImageFont:
    suffix = "-Bold" if bold else ""
    candidates = [
        f"/usr/share/fonts/truetype/dejavu/DejaVuSans{suffix}.ttf",
        "/usr/share/fonts/truetype/liberation2/LiberationSans-Bold.ttf" if bold else "/usr/share/fonts/truetype/liberation2/LiberationSans-Regular.ttf",
    ]
    for candidate in candidates:
        path = Path(candidate)
        if path.exists():
            return ImageFont.truetype(str(path), size=size)
    return ImageFont.load_default()


TITLE_FONT = load_font(50, True)
CARD_FONT = load_font(24, True)
LABEL_FONT = load_font(16, True)
SMALL_FONT = load_font(13, False)


def line(draw: ImageDraw.ImageDraw, a: Point2 | None, b: Point2 | None, fill: tuple[int, int, int], width: int = 2) -> None:
    if a is None or b is None:
        return
    draw.line((a[0], a[1], b[0], b[1]), fill=fill, width=width)


def dashed_line(
    draw: ImageDraw.ImageDraw,
    a: Point2 | None,
    b: Point2 | None,
    fill: tuple[int, int, int],
    width: int = 1,
    dash: float = 9.0,
    gap: float = 8.0,
) -> None:
    if a is None or b is None:
        return
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


def polyline(draw: ImageDraw.ImageDraw, points: Iterable[Point2 | None], fill: tuple[int, int, int], width: int = 2, closed: bool = False) -> None:
    pts = [point for point in points if point is not None]
    if len(pts) < 2:
        return
    if closed:
        pts.append(pts[0])
    draw.line(pts, fill=fill, width=width, joint="curve")


def polygon(draw: ImageDraw.ImageDraw, points: Iterable[Point2 | None], fill: tuple[int, int, int], outline: tuple[int, int, int] = CLEAN) -> None:
    pts = [point for point in points if point is not None]
    if len(pts) >= 3:
        draw.polygon(pts, fill=fill)
        draw.line(pts + [pts[0]], fill=outline, width=2)


def draw_label(draw: ImageDraw.ImageDraw, pos: Point2, text: str, fill: tuple[int, int, int] = INK) -> None:
    draw.text((pos[0], pos[1]), text, font=SMALL_FONT, fill=fill)


def draw_horizon(draw: ImageDraw.ImageDraw, rect: Rect, y: float) -> None:
    draw.line((rect[0], y, rect[2], y), fill=HORIZON, width=2)
    draw_label(draw, (rect[0] + 8, y + 4), "horizon / eye level", HORIZON)


def draw_vp(draw: ImageDraw.ImageDraw, point: Point2 | None, label: str) -> None:
    if point is None:
        return
    x, y = point
    r = 5
    draw.ellipse((x - r, y - r, x + r, y + r), fill=VANISH)
    draw_label(draw, (x + 7, y - 14), label, VANISH)


def box_points(center: Point3, size: Point3, yaw_degrees: float) -> tuple[list[Point3], list[tuple[int, int]]]:
    u, v, w = yaw_axes(yaw_degrees)
    verts: list[Point3] = []
    for sx in (-1.0, 1.0):
        for sy in (-1.0, 1.0):
            for sz in (-1.0, 1.0):
                point = center
                point = v_add(point, v_mul(u, sx * size[0] * 0.5))
                point = v_add(point, v_mul(v, sy * size[1] * 0.5))
                point = v_add(point, v_mul(w, sz * size[2] * 0.5))
                verts.append(point)
    edges: list[tuple[int, int]] = []
    for index, (sx, sy, sz) in enumerate((a, b, c) for a in (0, 1) for b in (0, 1) for c in (0, 1)):
        for delta in ((1, 0, 0), (0, 1, 0), (0, 0, 1)):
            nx, ny, nz = sx + delta[0], sy + delta[1], sz + delta[2]
            if nx <= 1 and ny <= 1 and nz <= 1:
                edges.append((index, nx * 4 + ny * 2 + nz))
    return verts, edges


def draw_box(draw: ImageDraw.ImageDraw, camera: Camera, rect: Rect, center: Point3, size: Point3, yaw: float, color: tuple[int, int, int] = CLEAN) -> None:
    verts, edges = box_points(center, size, yaw)
    projected = [camera.project(point, rect) for point in verts]
    for a, b in edges:
        line(draw, projected[a], projected[b], color, 2)


def draw_box_guides(draw: ImageDraw.ImageDraw, camera: Camera, rect: Rect, center: Point3, size: Point3, yaw: float, directions: list[Point3]) -> None:
    verts, _edges = box_points(center, size, yaw)
    for direction in directions:
        vp = camera.vp(direction, rect)
        draw_vp(draw, vp, "VP")
        for point in verts:
            projected = camera.project(point, rect)
            dashed_line(draw, projected, vp, GUIDE_LIGHT, 1)


def draw_one_point_cube(draw: ImageDraw.ImageDraw, rect: Rect, construction: bool) -> None:
    camera = Camera((0.0, 1.45, 0.0), (0.0, 1.45, 8.0), 300.0)
    center = (0.0, 1.45, 5.8)
    size = (1.95, 1.95, 1.95)
    vp = camera.vp((0.0, 0.0, 1.0), rect)
    if construction:
        draw_horizon(draw, rect, (rect[1] + rect[3]) * 0.5)
        draw_vp(draw, vp, "VP1")
        verts, _ = box_points(center, size, 0.0)
        for point in verts:
            if abs(point[2] - (center[2] - size[2] * 0.5)) < 0.01:
                dashed_line(draw, camera.project(point, rect), vp, GUIDE_LIGHT, 1)
    draw_box(draw, camera, rect, center, size, 0.0)


def draw_one_point_room(draw: ImageDraw.ImageDraw, rect: Rect, construction: bool) -> None:
    camera = Camera((0.0, 1.55, 0.0), (0.0, 1.55, 10.0), 250.0)
    vp = camera.vp((0.0, 0.0, 1.0), rect)
    near_z, far_z = 2.5, 10.0
    near = [(-3.2, 0.0, near_z), (3.2, 0.0, near_z), (3.2, 3.1, near_z), (-3.2, 3.1, near_z)]
    far = [(-1.8, 0.55, far_z), (1.8, 0.55, far_z), (1.8, 2.55, far_z), (-1.8, 2.55, far_z)]
    if construction:
        draw_horizon(draw, rect, camera.project((0.0, 1.55, 6.0), rect)[1])
        draw_vp(draw, vp, "VP1")
        for point in near:
            dashed_line(draw, camera.project(point, rect), vp, GUIDE_LIGHT, 1)
    for i in range(4):
        line(draw, camera.project(near[i], rect), camera.project(far[i], rect), CLEAN, 2)
    polyline(draw, [camera.project(point, rect) for point in far], CLEAN, 3, True)
    for z in (3.4, 4.5, 6.0, 8.0):
        line(draw, camera.project((-2.7, 0.0, z), rect), camera.project((2.7, 0.0, z), rect), MEASURE, 1)
    for x in (-2.0, -1.0, 0.0, 1.0, 2.0):
        line(draw, camera.project((x, 0.0, near_z), rect), camera.project((x * 0.55, 0.55, far_z), rect), MEASURE, 1)


def draw_one_point_road(draw: ImageDraw.ImageDraw, rect: Rect, construction: bool) -> None:
    camera = Camera((0.0, 1.35, 0.0), (0.0, 1.35, 10.0), 265.0)
    vp = camera.vp((0.0, 0.0, 1.0), rect)
    if construction:
        draw_horizon(draw, rect, camera.project((0.0, 1.35, 8.0), rect)[1])
        draw_vp(draw, vp, "VP1")
        for x in (-1.7, 1.7, -0.18, 0.18):
            dashed_line(draw, camera.project((x, 0.0, 2.0), rect), vp, GUIDE_LIGHT, 1)
    for x, width in ((-1.7, 3), (1.7, 3), (-0.18, 2), (0.18, 2)):
        line(draw, camera.project((x, 0.0, 2.0), rect), camera.project((x, 0.0, 15.0), rect), CLEAN, width)
    for z in (2.6, 3.5, 4.8, 6.7, 9.4, 13.0):
        line(draw, camera.project((-1.7, 0.0, z), rect), camera.project((1.7, 0.0, z), rect), MEASURE, 1)
    for z in (2.5, 4.0, 6.3, 9.7):
        line(draw, camera.project((-2.45, 0.0, z), rect), camera.project((-2.45, 0.95, z), rect), CLEAN, 2)
        line(draw, camera.project((2.45, 0.0, z), rect), camera.project((2.45, 0.95, z), rect), CLEAN, 2)


def draw_two_point_cube(draw: ImageDraw.ImageDraw, rect: Rect, construction: bool) -> None:
    camera = Camera((0.0, 1.55, 0.0), (0.0, 1.55, 9.0), 255.0)
    center = (0.0, 1.5, 5.8)
    size = (2.0, 2.0, 2.0)
    u, _v, w = yaw_axes(38.0)
    if construction:
        horizon_y = camera.project((0.0, 1.55, 8.0), rect)[1]
        draw_horizon(draw, rect, horizon_y)
        draw_box_guides(draw, camera, rect, center, size, 38.0, [u, w])
    draw_box(draw, camera, rect, center, size, 38.0)


def surface_point(origin: Point3, a_axis: Point3, b_axis: Point3, a: float, b: float) -> Point3:
    return v_add(v_add(origin, v_mul(a_axis, a)), v_mul(b_axis, b))


def draw_surface_rect(draw: ImageDraw.ImageDraw, camera: Camera, rect: Rect, origin: Point3, a_axis: Point3, b_axis: Point3, a0: float, b0: float, a1: float, b1: float) -> None:
    pts = [
        surface_point(origin, a_axis, b_axis, a0, b0),
        surface_point(origin, a_axis, b_axis, a1, b0),
        surface_point(origin, a_axis, b_axis, a1, b1),
        surface_point(origin, a_axis, b_axis, a0, b1),
    ]
    polyline(draw, [camera.project(point, rect) for point in pts], CLEAN, 1, True)


def draw_two_point_building(draw: ImageDraw.ImageDraw, rect: Rect, construction: bool) -> None:
    camera = Camera((0.0, 1.65, 0.0), (0.0, 1.65, 10.0), 245.0)
    center = (0.0, 1.75, 6.4)
    size = (2.8, 2.7, 2.0)
    yaw = 32.0
    u, v, w = yaw_axes(yaw)
    if construction:
        draw_horizon(draw, rect, camera.project((0.0, 1.65, 8.0), rect)[1])
        draw_box_guides(draw, camera, rect, center, size, yaw, [u, w])
    draw_box(draw, camera, rect, center, size, yaw)
    right_face_origin = v_add(v_add(center, v_mul(w, -size[2] * 0.5)), v_mul(u, size[0] * 0.5))
    left_face_origin = v_add(v_add(center, v_mul(u, -size[0] * 0.5)), v_mul(w, -size[2] * 0.5))
    for a in (-0.72, 0.12):
        for b in (-0.25, 0.55):
            draw_surface_rect(draw, camera, rect, right_face_origin, w, v, a, b, a + 0.44, b + 0.36)
    for a in (0.25, 0.95):
        for b in (-0.2, 0.62):
            draw_surface_rect(draw, camera, rect, left_face_origin, u, v, a, b, a + 0.38, b + 0.32)


def draw_two_point_stairs(draw: ImageDraw.ImageDraw, rect: Rect, construction: bool) -> None:
    camera = Camera((0.0, 1.45, 0.0), (0.0, 1.45, 9.0), 260.0)
    yaw = 31.0
    u, v, w = yaw_axes(yaw)
    origin = (-0.05, 0.0, 4.8)
    width = 2.2
    tread = 0.62
    rise = 0.32
    steps = 5
    if construction:
        draw_horizon(draw, rect, camera.project((0.0, 1.45, 8.0), rect)[1])
        draw_vp(draw, camera.vp(u, rect), "VP")
        draw_vp(draw, camera.vp(w, rect), "VP")
    side_profiles: list[list[Point3]] = []
    for side in (-width * 0.5, width * 0.5):
        pts = [v_add(origin, v_mul(u, side))]
        y = 0.0
        z = 0.0
        for _ in range(steps):
            y += rise
            pts.append(v_add(v_add(v_add(origin, v_mul(u, side)), v_mul(v, y)), v_mul(w, z)))
            z += tread
            pts.append(v_add(v_add(v_add(origin, v_mul(u, side)), v_mul(v, y)), v_mul(w, z)))
        side_profiles.append(pts)
        polyline(draw, [camera.project(point, rect) for point in pts], CLEAN, 2)
    for a, b in zip(side_profiles[0], side_profiles[1]):
        line(draw, camera.project(a, rect), camera.project(b, rect), CLEAN, 2)
        if construction:
            dashed_line(draw, camera.project(a, rect), camera.vp(u, rect), GUIDE_LIGHT, 1)


def draw_three_point_tower(draw: ImageDraw.ImageDraw, rect: Rect, construction: bool) -> None:
    camera = Camera((0.0, 1.05, 0.0), (0.0, 4.9, 10.0), 255.0)
    center = (0.0, 4.0, 8.2)
    size = (1.7, 5.6, 1.7)
    yaw = 34.0
    u, v, w = yaw_axes(yaw)
    if construction:
        vp_u = camera.vp(u, rect)
        vp_w = camera.vp(w, rect)
        vp_v = camera.vp(v, rect)
        if vp_u and vp_w:
            line(draw, vp_u, vp_w, HORIZON, 2)
        draw_vp(draw, vp_u, "VP1")
        draw_vp(draw, vp_w, "VP2")
        draw_vp(draw, vp_v, "VP3")
        draw_box_guides(draw, camera, rect, center, size, yaw, [u, w, v])
    draw_box(draw, camera, rect, center, size, yaw)


def circle_points(center: Point3, a_axis: Point3, b_axis: Point3, radius: float, segments: int = 96) -> list[Point3]:
    return [
        v_add(v_add(center, v_mul(a_axis, math.cos(math.tau * i / segments) * radius)), v_mul(b_axis, math.sin(math.tau * i / segments) * radius))
        for i in range(segments)
    ]


def draw_cylinder(draw: ImageDraw.ImageDraw, rect: Rect, construction: bool) -> None:
    camera = Camera((0.0, 1.35, 0.0), (0.0, 1.35, 9.0), 285.0)
    center = (0.0, 1.35, 5.6)
    bottom = (center[0], 0.35, center[2])
    top = (center[0], 2.35, center[2])
    if construction:
        draw_horizon(draw, rect, camera.project((0.0, 1.35, 8.0), rect)[1])
        for y in (0.35, 2.35):
            box = [(-1.0, y, 4.6), (1.0, y, 4.6), (1.0, y, 6.6), (-1.0, y, 6.6)]
            polyline(draw, [camera.project(point, rect) for point in box], GUIDE_LIGHT, 1, True)
            line(draw, camera.project((-1.0, y, 5.6), rect), camera.project((1.0, y, 5.6), rect), GUIDE_LIGHT, 1)
            line(draw, camera.project((0.0, y, 4.6), rect), camera.project((0.0, y, 6.6), rect), GUIDE_LIGHT, 1)
    top_ring = circle_points(top, (1.0, 0.0, 0.0), (0.0, 0.0, 1.0), 1.0)
    bottom_ring = circle_points(bottom, (1.0, 0.0, 0.0), (0.0, 0.0, 1.0), 1.0)
    polyline(draw, [camera.project(point, rect) for point in bottom_ring], CLEAN, 2, True)
    polyline(draw, [camera.project(point, rect) for point in top_ring], CLEAN, 3, True)
    for angle in (0.0, math.pi):
        x = math.cos(angle)
        z = math.sin(angle)
        line(draw, camera.project((x, bottom[1], bottom[2] + z), rect), camera.project((x, top[1], top[2] + z), rect), CLEAN, 2)


def arch_points(z: float, scale: float = 1.0) -> list[Point3]:
    pts: list[Point3] = [(-1.05 * scale, 0.0, z), (-1.05 * scale, 1.55 * scale, z)]
    for i in range(33):
        angle = math.pi - math.pi * i / 32
        pts.append((math.cos(angle) * 1.05 * scale, 1.55 * scale + math.sin(angle) * 1.05 * scale, z))
    pts.extend([(1.05 * scale, 0.0, z), (-1.05 * scale, 0.0, z)])
    return pts


def draw_archway(draw: ImageDraw.ImageDraw, rect: Rect, construction: bool) -> None:
    camera = Camera((0.0, 1.35, 0.0), (0.0, 1.35, 9.0), 295.0)
    vp = camera.vp((0.0, 0.0, 1.0), rect)
    near = arch_points(4.4, 1.0)
    far = arch_points(7.4, 0.72)
    if construction:
        draw_horizon(draw, rect, camera.project((0.0, 1.35, 8.0), rect)[1])
        draw_vp(draw, vp, "VP1")
        for point in (near[0], near[1], near[-3], near[-2]):
            dashed_line(draw, camera.project(point, rect), vp, GUIDE_LIGHT, 1)
    polyline(draw, [camera.project(point, rect) for point in far], MEASURE, 2)
    polyline(draw, [camera.project(point, rect) for point in near], CLEAN, 3)
    for a, b in zip((near[0], near[1], near[-3], near[-2]), (far[0], far[1], far[-3], far[-2])):
        line(draw, camera.project(a, rect), camera.project(b, rect), CLEAN, 2)


def draw_ground_circle(draw: ImageDraw.ImageDraw, rect: Rect, construction: bool) -> None:
    camera = Camera((0.0, 1.45, 0.0), (0.0, 1.45, 9.0), 285.0)
    square = [(-1.5, 0.0, 4.4), (1.5, 0.0, 4.4), (1.5, 0.0, 7.4), (-1.5, 0.0, 7.4)]
    circle = circle_points((0.0, 0.0, 5.9), (1.0, 0.0, 0.0), (0.0, 0.0, 1.0), 1.05)
    if construction:
        draw_horizon(draw, rect, camera.project((0.0, 1.45, 8.0), rect)[1])
        draw_vp(draw, camera.vp((0.0, 0.0, 1.0), rect), "VP1")
        polyline(draw, [camera.project(point, rect) for point in square], GUIDE_LIGHT, 1, True)
        line(draw, camera.project(square[0], rect), camera.project(square[2], rect), GUIDE_LIGHT, 1)
        line(draw, camera.project(square[1], rect), camera.project(square[3], rect), GUIDE_LIGHT, 1)
        line(draw, camera.project((-1.5, 0.0, 5.9), rect), camera.project((1.5, 0.0, 5.9), rect), GUIDE_LIGHT, 1)
        line(draw, camera.project((0.0, 0.0, 4.4), rect), camera.project((0.0, 0.0, 7.4), rect), GUIDE_LIGHT, 1)
    polyline(draw, [camera.project(point, rect) for point in square], CLEAN, 2, True)
    polyline(draw, [camera.project(point, rect) for point in circle], CLEAN, 3, True)


EXERCISES: list[tuple[str, str, Callable[[ImageDraw.ImageDraw, Rect, bool], None]]] = [
    ("01 One-Point Cube", "Depth edges converge to one central vanishing point.", draw_one_point_cube),
    ("02 One-Point Room", "Back wall is frontal; floor, ceiling, and wall edges recede to VP1.", draw_one_point_room),
    ("03 Road / Rails", "Parallel ground-plane edges shrink toward the horizon VP.", draw_one_point_road),
    ("04 Two-Point Cube", "Two horizontal edge families converge to two horizon VPs.", draw_two_point_cube),
    ("05 Two-Point Building", "Verticals stay vertical; both wall faces recede to separate VPs.", draw_two_point_building),
    ("06 Two-Point Stairs", "Treads, risers, and width use consistent VP families.", draw_two_point_stairs),
    ("07 Three-Point Tower", "Verticals also converge when the camera looks up.", draw_three_point_tower),
    ("08 Cylinder Ellipses", "Circles on horizontal planes project as exact conic curves.", draw_cylinder),
    ("09 One-Point Archway", "Matching front/back curves are joined by orthogonals to VP1.", draw_archway),
    ("10 Ground Circle", "A true circle inside a ground square projects as an ellipse-like conic.", draw_ground_circle),
]


def draw_card(image: Image.Image, draw: ImageDraw.ImageDraw, rect: Rect, title: str, rule: str, drawer: Callable[[ImageDraw.ImageDraw, Rect, bool], None]) -> None:
    x0, y0, x1, y1 = rect
    draw.rectangle(rect, fill=PANEL, outline=PANEL_EDGE, width=2)
    draw.text((x0 + 18, y0 + 12), title, font=CARD_FONT, fill=INK)
    draw.text((x0 + 18, y0 + 43), rule, font=SMALL_FONT, fill=(210, 197, 168))

    gutter = 18
    top = y0 + 72
    bottom = y1 - 18
    panel_w = (x1 - x0 - 54) // 2
    left = (x0 + 18, top, x0 + 18 + panel_w, bottom)
    right = (x0 + 36 + panel_w, top, x0 + 36 + panel_w + panel_w, bottom)
    for label, panel_rect, construction in (("construction", left, True), ("exact redraw", right, False)):
        draw.rectangle(panel_rect, fill=(238, 236, 228), outline=(119, 113, 101), width=2)
        draw.text((panel_rect[0] + 8, panel_rect[1] + 6), label, font=LABEL_FONT, fill=(54, 51, 46))
        panel_w = panel_rect[2] - panel_rect[0] - 2
        panel_h = panel_rect[3] - panel_rect[1] - 30
        panel_image = Image.new("RGB", (panel_w, panel_h), (238, 236, 228))
        panel_draw = ImageDraw.Draw(panel_image)
        inner = (gutter, 2, panel_w - gutter, panel_h - gutter)
        drawer(panel_draw, inner, construction)
        image_x = panel_rect[0] + 1
        image_y = panel_rect[1] + 29
        image.paste(panel_image, (image_x, image_y))


def build_board() -> None:
    cols = 2
    rows = 5
    pad = 26
    title_h = 112
    card_w = 1110
    card_h = 492
    width = cols * card_w + (cols + 1) * pad
    height = title_h + rows * card_h + (rows + 1) * pad
    image = Image.new("RGB", (width, height), BG)
    draw = ImageDraw.Draw(image)

    draw.rectangle((0, 0, width, 96), fill=(35, 35, 36))
    draw.text((34, 20), "P02 Perspective Drawing Exact Redraw Board", font=TITLE_FONT, fill=INK)
    draw.text((38, 75), "ten original side-by-side constructions generated from exact perspective projection rules", font=SMALL_FONT, fill=(220, 202, 168))

    for index, (title, rule, drawer) in enumerate(EXERCISES):
        col = index % cols
        row = index // cols
        x = pad + col * (card_w + pad)
        y = title_h + pad + row * (card_h + pad)
        draw_card(image, draw, (x, y, x + card_w, y + card_h), title, rule, drawer)

    for output in (DOC_IMAGE, REVIEW_IMAGE):
        output.parent.mkdir(parents=True, exist_ok=True)
        image.save(output)
    print(DOC_IMAGE)
    print(REVIEW_IMAGE)


if __name__ == "__main__":
    build_board()
