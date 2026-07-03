#!/usr/bin/env python3
"""Create a mesh-overlay study for the approved A1 cairn turnaround.

Run with:
    python Tools/DCC/build_bloodaxe_cairn_a1_mesh_overlay_study.py

This is a technical reconstruction aid, not final art. It detects the colored
contact markers on the approved turnaround sheet, draws view-local wire
overlays, and builds one combined 3D wire image from shared landmark points.
"""

from __future__ import annotations

import math
from collections import deque
from dataclasses import dataclass
from pathlib import Path
from typing import Iterable

import numpy as np
from PIL import Image, ImageDraw, ImageFont


ROOT = Path(__file__).resolve().parents[2]
REFERENCE = ROOT / "docs/assets/visual_canon/VC_GIA_BloodAxe_CairnStones_A01_A1_TurnaroundDraft_A01.png"
ASSET_NAME = "SM_GIA_BloodAxeCairnSlabCluster_A01_MeshOverlayStudy"
REVIEW_ROOT = ROOT / "Saved/Automation/DCC" / ASSET_NAME

TURNAROUND_OVERLAY = REVIEW_ROOT / f"{ASSET_NAME}_TurnaroundMeshOverlay.png"
TOPOLOGY_OVERLAY = REVIEW_ROOT / f"{ASSET_NAME}_TurnaroundTopologyOverlay.png"
COMBINED_3D_WIRE = REVIEW_ROOT / f"{ASSET_NAME}_Combined3DWireOverlay.png"
COMBINED_3D_CAGE = REVIEW_ROOT / f"{ASSET_NAME}_Combined3DControlCage.png"
REVIEW_BOARD = REVIEW_ROOT / f"{ASSET_NAME}_OverlayReviewBoard.png"
TOPOLOGY_BOARD = REVIEW_ROOT / f"{ASSET_NAME}_TopologyReviewBoard.png"


@dataclass(frozen=True)
class ViewBox:
    name: str
    box: tuple[int, int, int, int]
    color: tuple[int, int, int, int]

    def point(self, u: float, v: float) -> tuple[float, float]:
        x0, y0, x1, y1 = self.box
        return (x0 + (x1 - x0) * u, y0 + (y1 - y0) * v)


@dataclass(frozen=True)
class Marker:
    x: float
    y: float
    area: int
    color: tuple[int, int, int]


VIEW_BOXES = [
    ViewBox("FRONT", (58, 66, 492, 268), (0, 205, 255, 220)),
    ViewBox("FRONT-RIGHT 3/4", (540, 66, 980, 268), (0, 170, 255, 220)),
    ViewBox("RIGHT SIDE", (1028, 66, 1470, 294), (255, 170, 0, 220)),
    ViewBox("BACK-RIGHT 3/4", (52, 325, 488, 538), (80, 230, 120, 220)),
    ViewBox("BACK", (540, 307, 985, 535), (40, 215, 120, 220)),
    ViewBox("BACK-LEFT 3/4", (1026, 327, 1472, 538), (80, 220, 255, 220)),
    ViewBox("LEFT SIDE", (52, 625, 492, 858), (185, 120, 255, 220)),
    ViewBox("FRONT-LEFT 3/4", (540, 620, 985, 855), (255, 95, 95, 220)),
    ViewBox("TOP ORTHO", (1072, 650, 1462, 900), (255, 215, 70, 220)),
]


POINTS_3D = {
    "P01_RearTallSlabApex": (25.0, 38.0, 160.0),
    "P02_MainSlabFrontLeftCorner": (-112.0, -55.0, 55.0),
    "P03_MainSlabFrontRightCorner": (108.0, -46.0, 43.0),
    "P04_MainSlabRearLeftCorner": (-98.0, 31.0, 88.0),
    "P05_MainSlabRearRightCorner": (103.0, 34.0, 78.0),
    "P06_RightUprightApex": (125.0, 18.0, 111.0),
    "P07_LeftStackOuterCorner": (-155.0, -36.0, 42.0),
    "P08_LeftRearShardApex": (-54.0, 38.0, 116.0),
    "P09_RightLashingEndpoint": (133.0, -6.0, 63.0),
    "P10_LeftLashingEndpoint": (-72.0, -58.0, 52.0),
    "P11_BackStoneRoot": (9.0, 59.0, 24.0),
    "P12_FrontPebbleEdge": (13.0, -91.0, 8.0),
    "I01_RearSlabLeftRoot": (-24.0, 47.0, 18.0),
    "I02_RearSlabRightRoot": (73.0, 48.0, 19.0),
    "I03_RightUprightRoot": (112.0, -9.0, 18.0),
    "I04_RightUprightBackRoot": (145.0, 22.0, 20.0),
    "I05_LeftStackFrontRoot": (-150.0, -63.0, 18.0),
    "I06_LeftStackBackRoot": (-118.0, 15.0, 25.0),
    "I07_BaseBackLeft": (-138.0, 70.0, 5.0),
    "I08_BaseBackRight": (150.0, 70.0, 5.0),
    "I09_BaseFrontRight": (158.0, -86.0, 5.0),
    "I10_BaseFrontLeft": (-162.0, -86.0, 5.0),
}


EDGE_GROUPS = [
    ("main fallen slab top", (195, 40, 35, 255), [
        ("P02_MainSlabFrontLeftCorner", "P03_MainSlabFrontRightCorner"),
        ("P03_MainSlabFrontRightCorner", "P05_MainSlabRearRightCorner"),
        ("P05_MainSlabRearRightCorner", "P04_MainSlabRearLeftCorner"),
        ("P04_MainSlabRearLeftCorner", "P02_MainSlabFrontLeftCorner"),
        ("P10_LeftLashingEndpoint", "P09_RightLashingEndpoint"),
    ]),
    ("rear standing slab", (35, 95, 225, 255), [
        ("I01_RearSlabLeftRoot", "P01_RearTallSlabApex"),
        ("P01_RearTallSlabApex", "I02_RearSlabRightRoot"),
        ("I02_RearSlabRightRoot", "P11_BackStoneRoot"),
        ("P11_BackStoneRoot", "I01_RearSlabLeftRoot"),
        ("P08_LeftRearShardApex", "P01_RearTallSlabApex"),
    ]),
    ("right upright", (250, 165, 35, 255), [
        ("I03_RightUprightRoot", "P06_RightUprightApex"),
        ("P06_RightUprightApex", "I04_RightUprightBackRoot"),
        ("I04_RightUprightBackRoot", "P09_RightLashingEndpoint"),
        ("P09_RightLashingEndpoint", "I03_RightUprightRoot"),
    ]),
    ("left stack", (135, 60, 220, 255), [
        ("I05_LeftStackFrontRoot", "P07_LeftStackOuterCorner"),
        ("P07_LeftStackOuterCorner", "I06_LeftStackBackRoot"),
        ("I06_LeftStackBackRoot", "P04_MainSlabRearLeftCorner"),
        ("P10_LeftLashingEndpoint", "I05_LeftStackFrontRoot"),
    ]),
    ("ground footprint", (90, 70, 45, 255), [
        ("I10_BaseFrontLeft", "I09_BaseFrontRight"),
        ("I09_BaseFrontRight", "I08_BaseBackRight"),
        ("I08_BaseBackRight", "I07_BaseBackLeft"),
        ("I07_BaseBackLeft", "I10_BaseFrontLeft"),
        ("P12_FrontPebbleEdge", "P11_BackStoneRoot"),
    ]),
]


VIEW_CONTROL_NET = [
    # outer footprint and rubble apron
    (0.10, 0.78), (0.20, 0.65), (0.38, 0.59), (0.58, 0.61), (0.82, 0.67),
    (0.93, 0.79), (0.76, 0.88), (0.52, 0.88), (0.30, 0.85), (0.17, 0.84),
    # central fallen slab
    (0.25, 0.59), (0.38, 0.48), (0.54, 0.45), (0.74, 0.51), (0.84, 0.63),
    (0.66, 0.70), (0.45, 0.70), (0.29, 0.69), (0.52, 0.58),
    # rear standing pieces
    (0.47, 0.54), (0.51, 0.30), (0.56, 0.12), (0.62, 0.33), (0.63, 0.58),
    (0.42, 0.52), (0.40, 0.37), (0.35, 0.64),
    # left stack and right upright
    (0.11, 0.69), (0.21, 0.56), (0.32, 0.68), (0.19, 0.81),
    (0.76, 0.57), (0.87, 0.38), (0.94, 0.68), (0.84, 0.80),
]


CONTROL_TRIANGLES = [
    (0, 1, 9), (1, 2, 10), (1, 10, 27), (2, 3, 18), (3, 4, 14),
    (4, 5, 14), (5, 6, 34), (6, 7, 15), (7, 8, 16), (8, 9, 17),
    (10, 11, 17), (11, 12, 18), (12, 13, 18), (13, 14, 18),
    (14, 15, 18), (15, 16, 18), (16, 17, 18), (17, 10, 18),
    (19, 20, 24), (20, 21, 22), (20, 22, 23), (19, 23, 24),
    (24, 25, 26), (10, 24, 17), (11, 19, 12), (12, 20, 13),
    (27, 28, 29), (27, 29, 30), (28, 10, 29), (29, 17, 30),
    (31, 32, 33), (31, 33, 34), (13, 31, 14), (14, 34, 15),
]


CAGE_FACES = [
    ("main slab", (180, 35, 28, 70), [
        ("P02_MainSlabFrontLeftCorner", "P03_MainSlabFrontRightCorner", "P05_MainSlabRearRightCorner"),
        ("P02_MainSlabFrontLeftCorner", "P05_MainSlabRearRightCorner", "P04_MainSlabRearLeftCorner"),
        ("P02_MainSlabFrontLeftCorner", "P10_LeftLashingEndpoint", "P04_MainSlabRearLeftCorner"),
        ("P03_MainSlabFrontRightCorner", "P09_RightLashingEndpoint", "P05_MainSlabRearRightCorner"),
    ]),
    ("rear slab", (50, 95, 220, 65), [
        ("I01_RearSlabLeftRoot", "P08_LeftRearShardApex", "P01_RearTallSlabApex"),
        ("I01_RearSlabLeftRoot", "P01_RearTallSlabApex", "I02_RearSlabRightRoot"),
        ("I02_RearSlabRightRoot", "P01_RearTallSlabApex", "P11_BackStoneRoot"),
    ]),
    ("right upright", (245, 160, 30, 70), [
        ("I03_RightUprightRoot", "P06_RightUprightApex", "P09_RightLashingEndpoint"),
        ("P09_RightLashingEndpoint", "P06_RightUprightApex", "I04_RightUprightBackRoot"),
    ]),
    ("left stack", (135, 60, 220, 65), [
        ("I05_LeftStackFrontRoot", "P07_LeftStackOuterCorner", "P10_LeftLashingEndpoint"),
        ("P07_LeftStackOuterCorner", "I06_LeftStackBackRoot", "P04_MainSlabRearLeftCorner"),
    ]),
    ("base", (120, 90, 55, 55), [
        ("I10_BaseFrontLeft", "I09_BaseFrontRight", "I08_BaseBackRight"),
        ("I10_BaseFrontLeft", "I08_BaseBackRight", "I07_BaseBackLeft"),
    ]),
]


def font(size: int) -> ImageFont.ImageFont:
    candidates = [
        "/usr/share/fonts/dejavu-sans-fonts/DejaVuSans.ttf",
        "/usr/share/fonts/dejavu/DejaVuSans.ttf",
    ]
    for path in candidates:
        if Path(path).exists():
            return ImageFont.truetype(path, size)
    return ImageFont.load_default()


def hsv_from_rgb(color: np.ndarray) -> tuple[np.ndarray, np.ndarray, np.ndarray]:
    r, g, b = color[..., 0], color[..., 1], color[..., 2]
    maxc = np.max(color, axis=-1)
    minc = np.min(color, axis=-1)
    delta = maxc - minc
    hue = np.zeros_like(maxc)
    nonzero = delta > 0.0001
    red = nonzero & (maxc == r)
    green = nonzero & (maxc == g)
    blue = nonzero & (maxc == b)
    hue[red] = ((g[red] - b[red]) / delta[red]) % 6.0
    hue[green] = ((b[green] - r[green]) / delta[green]) + 2.0
    hue[blue] = ((r[blue] - g[blue]) / delta[blue]) + 4.0
    hue /= 6.0
    sat = np.divide(delta, maxc, out=np.zeros_like(delta), where=maxc > 0)
    val = maxc
    return hue, sat, val


def detect_markers(image: Image.Image) -> list[Marker]:
    rgb = np.asarray(image.convert("RGB"), dtype=np.float32) / 255.0
    _hue, sat, val = hsv_from_rgb(rgb)
    mask = (sat > 0.52) & (val > 0.52)
    visited = np.zeros(mask.shape, dtype=bool)
    height, width = mask.shape
    markers: list[Marker] = []

    for y in range(height):
        for x in range(width):
            if visited[y, x] or not mask[y, x]:
                continue
            queue: deque[tuple[int, int]] = deque([(x, y)])
            visited[y, x] = True
            pixels: list[tuple[int, int]] = []
            while queue:
                px, py = queue.popleft()
                pixels.append((px, py))
                for ny in range(py - 1, py + 2):
                    for nx in range(px - 1, px + 2):
                        if nx == px and ny == py:
                            continue
                        if nx < 0 or ny < 0 or nx >= width or ny >= height:
                            continue
                        if visited[ny, nx] or not mask[ny, nx]:
                            continue
                        visited[ny, nx] = True
                        queue.append((nx, ny))
            area = len(pixels)
            if not 12 <= area <= 260:
                continue
            xs = np.array([point[0] for point in pixels], dtype=np.float32)
            ys = np.array([point[1] for point in pixels], dtype=np.float32)
            colors = np.asarray(image.convert("RGB"))[ys.astype(int), xs.astype(int)]
            markers.append(
                Marker(
                    x=float(xs.mean()),
                    y=float(ys.mean()),
                    area=area,
                    color=tuple(int(v) for v in colors.mean(axis=0)),
                )
            )
    return markers


def markers_in_view(markers: Iterable[Marker], view: ViewBox) -> list[Marker]:
    x0, y0, x1, y1 = view.box
    return [marker for marker in markers if x0 <= marker.x <= x1 and y0 <= marker.y <= y1]


def convex_hull(points: list[tuple[float, float]]) -> list[tuple[float, float]]:
    if len(points) <= 2:
        return points
    sorted_points = sorted(set(points))

    def cross(o: tuple[float, float], a: tuple[float, float], b: tuple[float, float]) -> float:
        return (a[0] - o[0]) * (b[1] - o[1]) - (a[1] - o[1]) * (b[0] - o[0])

    lower: list[tuple[float, float]] = []
    for point in sorted_points:
        while len(lower) >= 2 and cross(lower[-2], lower[-1], point) <= 0:
            lower.pop()
        lower.append(point)
    upper: list[tuple[float, float]] = []
    for point in reversed(sorted_points):
        while len(upper) >= 2 and cross(upper[-2], upper[-1], point) <= 0:
            upper.pop()
        upper.append(point)
    return lower[:-1] + upper[:-1]


def draw_polyline(
    draw: ImageDraw.ImageDraw,
    points: list[tuple[float, float]],
    color: tuple[int, int, int, int],
    width: int,
    close: bool = True,
) -> None:
    if len(points) < 2:
        return
    line_points = points + [points[0]] if close else points
    draw.line(line_points, fill=color, width=width, joint="curve")


def draw_view_mesh(draw: ImageDraw.ImageDraw, view: ViewBox, markers: list[Marker]) -> None:
    x0, y0, x1, y1 = view.box
    view_points = [view.point(u, v) for u, v in [
        (0.10, 0.74), (0.22, 0.56), (0.43, 0.48), (0.66, 0.50),
        (0.83, 0.61), (0.91, 0.78), (0.73, 0.88), (0.42, 0.86),
        (0.18, 0.83),
    ]]
    draw_polyline(draw, view_points, (40, 180, 220, 190), 3)

    main_slab = [view.point(u, v) for u, v in [
        (0.22, 0.58), (0.44, 0.45), (0.72, 0.48), (0.83, 0.60),
        (0.55, 0.71), (0.28, 0.70),
    ]]
    draw_polyline(draw, main_slab, (220, 35, 25, 230), 4)
    draw.line([view.point(0.33, 0.61), view.point(0.71, 0.53)], fill=(220, 35, 25, 210), width=3)
    draw.line([view.point(0.46, 0.48), view.point(0.57, 0.70)], fill=(220, 35, 25, 190), width=2)

    rear_slab = [view.point(u, v) for u, v in [
        (0.46, 0.50), (0.54, 0.13), (0.61, 0.33), (0.60, 0.61),
    ]]
    draw_polyline(draw, rear_slab, (45, 95, 230, 225), 3)

    side_stack = [view.point(u, v) for u, v in [(0.08, 0.67), (0.24, 0.57), (0.34, 0.72), (0.18, 0.82)]]
    draw_polyline(draw, side_stack, (150, 70, 225, 210), 3)
    right_upright = [view.point(u, v) for u, v in [(0.76, 0.55), (0.88, 0.34), (0.95, 0.68), (0.83, 0.78)]]
    draw_polyline(draw, right_upright, (255, 155, 40, 215), 3)

    if len(markers) >= 3:
        hull = convex_hull([(marker.x, marker.y) for marker in markers])
        draw_polyline(draw, hull, (255, 235, 50, 240), 3)
        for center in hull:
            draw.line([center, view.point(0.50, 0.61)], fill=(255, 235, 50, 125), width=1)

    title_font = font(20)
    draw.rectangle((x0, y0, x1, y1), outline=view.color, width=2)
    draw.text((x0 + 8, y0 + 6), view.name, fill=(20, 20, 20, 255), font=title_font)


def draw_marker_labels(draw: ImageDraw.ImageDraw, markers: list[Marker]) -> None:
    label_font = font(14)
    sorted_markers = sorted(markers, key=lambda item: (item.y, item.x))
    for index, marker in enumerate(sorted_markers, 1):
        radius = 6
        fill = (*marker.color, 255)
        outline = (255, 255, 255, 255)
        draw.ellipse((marker.x - radius, marker.y - radius, marker.x + radius, marker.y + radius), fill=fill, outline=outline, width=2)
        label = f"M{index:02d}"
        draw.text((marker.x + 7, marker.y - 7), label, fill=(20, 20, 20, 240), font=label_font)


def add_unique_point(points: list[tuple[float, float]], point: tuple[float, float], min_distance: float) -> int:
    px, py = point
    for index, (x, y) in enumerate(points):
        if math.hypot(px - x, py - y) <= min_distance:
            return index
    points.append(point)
    return len(points) - 1


def draw_topology_view(draw: ImageDraw.ImageDraw, view: ViewBox, markers: list[Marker]) -> None:
    x0, y0, x1, y1 = view.box
    width = x1 - x0
    height = y1 - y0
    points = [view.point(u, v) for u, v in VIEW_CONTROL_NET]
    marker_indices: list[int] = []
    for marker in markers:
        marker_indices.append(add_unique_point(points, (marker.x, marker.y), 10.0))

    triangle_fill = (30, 180, 220, 28)
    triangle_line = (245, 250, 255, 205)
    important_line = (30, 210, 245, 235)
    for triangle in CONTROL_TRIANGLES:
        tri_points = [points[index] for index in triangle]
        draw.polygon(tri_points, fill=triangle_fill)
        draw.line([tri_points[0], tri_points[1], tri_points[2], tri_points[0]], fill=triangle_line, width=2)

    center = view.point(0.52, 0.61)
    for index in marker_indices:
        mx, my = points[index]
        nearest = sorted(
            range(len(VIEW_CONTROL_NET)),
            key=lambda control_index: math.hypot(mx - points[control_index][0], my - points[control_index][1]),
        )[:3]
        for control_index in nearest:
            cx, cy = points[control_index]
            if math.hypot(mx - cx, my - cy) < max(width, height) * 0.34:
                draw.line((mx, my, cx, cy), fill=(255, 230, 60, 210), width=2)
        draw.line((mx, my, center[0], center[1]), fill=(255, 120, 40, 155), width=1)

    outline = [points[index] for index in [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]]
    draw_polyline(draw, outline, important_line, 4)
    for point in points[:len(VIEW_CONTROL_NET)]:
        draw.ellipse((point[0] - 2.5, point[1] - 2.5, point[0] + 2.5, point[1] + 2.5), fill=(255, 255, 255, 230))
    for marker in markers:
        draw.ellipse((marker.x - 6, marker.y - 6, marker.x + 6, marker.y + 6), fill=(*marker.color, 255), outline=(255, 255, 255, 255), width=2)

    title_font = font(18)
    draw.rectangle((x0, y0, x1, y1), outline=view.color, width=2)
    draw.text((x0 + 8, y0 + 6), view.name, fill=(15, 15, 15, 255), font=title_font)


def build_topology_overlay(image: Image.Image, markers: list[Marker]) -> None:
    overlay = image.convert("RGBA")
    shade = Image.new("RGBA", overlay.size, (0, 0, 0, 0))
    draw = ImageDraw.Draw(shade, "RGBA")
    for view in VIEW_BOXES:
        draw_topology_view(draw, view, markers_in_view(markers, view))
    label_font = font(22)
    draw.rectangle((28, 20, 760, 62), fill=(255, 255, 255, 220))
    draw.text(
        (40, 30),
        "Topology overlay: white/cyan triangle net plus detected contact nodes for mesh rebuild.",
        fill=(20, 20, 20, 255),
        font=label_font,
    )
    Image.alpha_composite(overlay, shade).save(TOPOLOGY_OVERLAY)


def build_turnaround_overlay(image: Image.Image, markers: list[Marker]) -> None:
    overlay = image.convert("RGBA")
    layer = Image.new("RGBA", overlay.size, (255, 255, 255, 0))
    draw = ImageDraw.Draw(layer, "RGBA")
    for view in VIEW_BOXES:
        draw_view_mesh(draw, view, markers_in_view(markers, view))
    draw_marker_labels(draw, markers)
    note_font = font(22)
    draw.rectangle((28, 20, 760, 58), fill=(255, 255, 255, 210))
    draw.text(
        (40, 28),
        "Mesh overlay study: yellow hulls use detected contact markers; colored wires show proposed surface groups.",
        fill=(20, 20, 20, 255),
        font=note_font,
    )
    output = Image.alpha_composite(overlay, layer)
    output.save(TURNAROUND_OVERLAY)


def rotate_point(point: tuple[float, float, float], yaw: float, pitch: float) -> tuple[float, float, float]:
    x, y, z = point
    cosy, siny = math.cos(yaw), math.sin(yaw)
    x1 = x * cosy - y * siny
    y1 = x * siny + y * cosy
    cosp, sinp = math.cos(pitch), math.sin(pitch)
    y2 = y1 * cosp - z * sinp
    z2 = y1 * sinp + z * cosp
    return x1, y2, z2


def project(point: tuple[float, float, float], width: int, height: int, scale: float = 2.2) -> tuple[float, float, float]:
    rotated = rotate_point(point, math.radians(-38.0), math.radians(-22.0))
    x, y, z = rotated
    return width * 0.50 + x * scale, height * 0.58 - z * scale, y


def draw_depth_line(
    draw: ImageDraw.ImageDraw,
    a: tuple[float, float, float],
    b: tuple[float, float, float],
    color: tuple[int, int, int, int],
    width: int,
) -> None:
    shade = max(0.45, min(1.0, 0.70 + ((a[2] + b[2]) * 0.5) / 420.0))
    shaded = tuple(int(component * shade) if idx < 3 else component for idx, component in enumerate(color))
    draw.line((a[0], a[1], b[0], b[1]), fill=shaded, width=width)


def build_combined_3d_wire() -> None:
    width, height = 1600, 1000
    canvas = Image.new("RGBA", (width, height), (246, 244, 238, 255))
    draw = ImageDraw.Draw(canvas, "RGBA")
    title_font = font(34)
    label_font = font(18)
    small_font = font(15)

    draw.text((46, 32), "A1 Multi-View Contact Mesh Overlay - Combined 3D Wire", fill=(30, 28, 24, 255), font=title_font)
    draw.text(
        (48, 78),
        "This is a reconstruction guide, not final geometry. It merges shared landmarks from the visible concept angles.",
        fill=(70, 66, 58, 255),
        font=label_font,
    )

    projected = {key: project(value, width, height) for key, value in POINTS_3D.items()}

    base = [project(POINTS_3D[key], width, height) for key in ["I10_BaseFrontLeft", "I09_BaseFrontRight", "I08_BaseBackRight", "I07_BaseBackLeft"]]
    draw.polygon([(point[0], point[1]) for point in base], fill=(120, 90, 55, 45), outline=(120, 90, 55, 140))

    all_segments: list[tuple[float, tuple[int, int, int, int], tuple[str, str]]] = []
    for _group_name, color, edges in EDGE_GROUPS:
        for edge in edges:
            depth = (projected[edge[0]][2] + projected[edge[1]][2]) * 0.5
            all_segments.append((depth, color, edge))
    for _depth, color, (a_key, b_key) in sorted(all_segments):
        draw_depth_line(draw, projected[a_key], projected[b_key], color, 5)

    for index, (key, point) in enumerate(sorted(projected.items()), 1):
        x, y, depth = point
        color = (220, 45, 40, 255) if key.startswith("P") else (55, 95, 180, 210)
        radius = 7 if key.startswith("P") else 5
        draw.ellipse((x - radius, y - radius, x + radius, y + radius), fill=color, outline=(255, 255, 255, 255), width=2)
        if key.startswith("P"):
            draw.text((x + 8, y - 8), key.split("_", 1)[0], fill=(25, 25, 25, 255), font=small_font)

    legend_x = 1115
    legend_y = 160
    draw.rounded_rectangle((legend_x, legend_y, 1545, legend_y + 255), radius=10, fill=(255, 255, 255, 220), outline=(80, 75, 65, 180), width=2)
    draw.text((legend_x + 20, legend_y + 18), "Wire groups", fill=(35, 32, 28, 255), font=label_font)
    for row, (name, color, _edges) in enumerate(EDGE_GROUPS):
        y = legend_y + 58 + row * 36
        draw.line((legend_x + 24, y + 8, legend_x + 80, y + 8), fill=color, width=6)
        draw.text((legend_x + 96, y), name, fill=(45, 42, 36, 255), font=small_font)

    warning = (
        "Use this to rebuild the mesh: preserve the P-point silhouette, then infer missing underside/back faces manually."
    )
    draw.text((48, 936), warning, fill=(120, 55, 35, 255), font=label_font)
    canvas.save(COMBINED_3D_WIRE)


def build_combined_3d_cage() -> None:
    width, height = 1600, 1000
    canvas = Image.new("RGBA", (width, height), (245, 243, 238, 255))
    draw = ImageDraw.Draw(canvas, "RGBA")
    title_font = font(34)
    label_font = font(18)
    small_font = font(15)
    draw.text((46, 32), "A1 Combined 3D Control Cage", fill=(28, 26, 22, 255), font=title_font)
    draw.text(
        (48, 78),
        "Translucent faces show the rebuild cage implied by the contact points. This is the mesh target, not final topology.",
        fill=(70, 66, 58, 255),
        font=label_font,
    )

    projected = {key: project(value, width, height, scale=2.35) for key, value in POINTS_3D.items()}
    sorted_faces: list[tuple[float, tuple[int, int, int, int], tuple[str, str, str]]] = []
    for _name, color, faces in CAGE_FACES:
        for face in faces:
            depth = sum(projected[key][2] for key in face) / 3.0
            sorted_faces.append((depth, color, face))
    for _depth, color, face in sorted(sorted_faces):
        pts = [(projected[key][0], projected[key][1]) for key in face]
        draw.polygon(pts, fill=color, outline=(25, 25, 25, 160))
        draw.line([pts[0], pts[1], pts[2], pts[0]], fill=(20, 20, 20, 205), width=3)

    for _group_name, color, edges in EDGE_GROUPS:
        for a_key, b_key in edges:
            draw_depth_line(draw, projected[a_key], projected[b_key], color, 5)

    for key, point in sorted(projected.items()):
        x, y, _depth = point
        is_primary = key.startswith("P")
        radius = 7 if is_primary else 5
        fill = (215, 45, 38, 255) if is_primary else (55, 95, 180, 230)
        draw.ellipse((x - radius, y - radius, x + radius, y + radius), fill=fill, outline=(255, 255, 255, 255), width=2)
        if is_primary:
            draw.text((x + 8, y - 8), key.split("_", 1)[0], fill=(25, 25, 25, 255), font=small_font)

    note_y = 880
    draw.rounded_rectangle((46, note_y, 1185, note_y + 72), radius=8, fill=(255, 255, 255, 230), outline=(110, 100, 88, 180), width=2)
    draw.text(
        (66, note_y + 18),
        "Next DCC pass should build separate jagged stone shells from this cage, then add side/back thickness and rubble.",
        fill=(85, 50, 32, 255),
        font=label_font,
    )
    canvas.save(COMBINED_3D_CAGE)


def build_review_board() -> None:
    overlay = Image.open(TURNAROUND_OVERLAY).convert("RGBA")
    wire = Image.open(COMBINED_3D_WIRE).convert("RGBA")
    board_width, board_height = 2000, 1100
    board = Image.new("RGBA", (board_width, board_height), (238, 235, 228, 255))
    draw = ImageDraw.Draw(board, "RGBA")
    title_font = font(30)
    draw.text((50, 28), "A1 contact-point overlay and combined 3D wire study", fill=(25, 23, 20, 255), font=title_font)
    overlay.thumbnail((980, 920), Image.Resampling.LANCZOS)
    wire.thumbnail((900, 780), Image.Resampling.LANCZOS)
    board.alpha_composite(overlay, (40, 120))
    board.alpha_composite(wire, (1060, 150))
    draw.text((50, 1030), "Left: overlay on every visible concept angle. Right: shared 3D landmark wire/proxy.", fill=(55, 50, 44, 255), font=font(20))
    board.save(REVIEW_BOARD)


def build_topology_board() -> None:
    topology = Image.open(TOPOLOGY_OVERLAY).convert("RGBA")
    cage = Image.open(COMBINED_3D_CAGE).convert("RGBA")
    board_width, board_height = 2200, 1200
    board = Image.new("RGBA", (board_width, board_height), (238, 235, 228, 255))
    draw = ImageDraw.Draw(board, "RGBA")
    title_font = font(32)
    body_font = font(20)
    draw.text((52, 32), "A1 topology/control-cage overlay", fill=(25, 23, 20, 255), font=title_font)
    draw.text(
        (52, 76),
        "This is the practical version of the mesh overlay: triangulate each visible angle, then merge shared contact points into a 3D rebuild cage.",
        fill=(56, 52, 45, 255),
        font=body_font,
    )
    topology.thumbnail((1080, 940), Image.Resampling.LANCZOS)
    cage.thumbnail((980, 820), Image.Resampling.LANCZOS)
    board.alpha_composite(topology, (42, 150))
    board.alpha_composite(cage, (1160, 190))
    draw.text((52, 1116), "Left: topology over every concept angle. Right: combined 3D control cage for the next Blender rebuild.", fill=(55, 50, 44, 255), font=body_font)
    board.save(TOPOLOGY_BOARD)


def main() -> None:
    REVIEW_ROOT.mkdir(parents=True, exist_ok=True)
    image = Image.open(REFERENCE).convert("RGB")
    markers = detect_markers(image)
    build_turnaround_overlay(image, markers)
    build_topology_overlay(image, markers)
    build_combined_3d_wire()
    build_combined_3d_cage()
    build_review_board()
    build_topology_board()
    print(f"Detected markers: {len(markers)}")
    print(f"Wrote {TURNAROUND_OVERLAY.relative_to(ROOT)}")
    print(f"Wrote {TOPOLOGY_OVERLAY.relative_to(ROOT)}")
    print(f"Wrote {COMBINED_3D_WIRE.relative_to(ROOT)}")
    print(f"Wrote {COMBINED_3D_CAGE.relative_to(ROOT)}")
    print(f"Wrote {REVIEW_BOARD.relative_to(ROOT)}")
    print(f"Wrote {TOPOLOGY_BOARD.relative_to(ROOT)}")


if __name__ == "__main__":
    main()
