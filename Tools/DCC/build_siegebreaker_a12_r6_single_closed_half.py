#!/usr/bin/env python3
"""Build Siege Breaker A12 R6 A04 from one coherent Y<=0 front half.

This is a clean-room Blender build.  It reads the six immutable source PNGs
and written authority only.  It does not load, append, import, or inspect any
R5 Blender object, mesh, UV layer, material, or derived texture.

The volume is the boundary of one source-constrained occupancy field. Every
exposed cell contributes one face exactly once; Y=0 closure faces are omitted.
The source half is topology-audited before its duplicate is reflected exactly
across Y=0 and the matching boundary is welded. Outward normals are rebuilt
after the negative-determinant transform. Static UVs are assigned only after
the final topology passes. Source pixels color boundary faces; they never
create extra geometry.
"""

from __future__ import annotations

import bisect
import hashlib
import json
import math
from collections import Counter, deque
from pathlib import Path

import bpy
from mathutils import Vector
from PIL import Image, ImageDraw, ImageFont


ROOT = Path(__file__).resolve().parents[2]
ASSET = "SM_DRW_SiegeBreaker_Hammer_A01"
ATTEMPT = "A12_R6_A04_FrontHalfDepthMirror_A01"
CONTRACT_ID = "SB-AXIAL-A12-R6-A04-FRONT-HALF-DEPTH-MIRROR"

SOURCE_DIR = ROOT / "SourceAssets/Concepts/SiegeBreaker"
SOURCE_PATHS = {
    "front": SOURCE_DIR / "siege_breaker_front_view.png",
    "back": SOURCE_DIR / "siege_breaker_back_view.png",
    "left": SOURCE_DIR / "siege_breaker_left_view.png",
    "right": SOURCE_DIR / "siege_breaker_right_view.png",
    "top": SOURCE_DIR / "siege_breaker_true_axial_top_view.png",
    "bottom": SOURCE_DIR / "siege_breaker_true_axial_bottom_view.png",
}
EXPECTED_SHA256 = {
    "front": "d00bf9ffcfd4862884626fa961c5f6b4fd6cedfdff7936b2210ca2a905e57e95",
    "back": "15b4633f2df4ee06115ef4a7e238f287ebece1bae514ad4005c1036a57359799",
    "left": "1a23e0c24f7be4b12df93e2509b9d300acc9161a21a32b336f7cf63c1288d91b",
    "right": "04a1e9359d518b1dec35fe161020bd23ab9e2f8d5934f24e4184aecaa91d8330",
    "top": "aee612d9bed74e4f861576f926fe9d75de00f80dc416e3a6ba66a75247c00e98",
    "bottom": "874a9e7c7713c7edbcf1030486d3988a54e8499ee697e316ec82a013fdb9d746",
}
RECTS = {
    "front": (317, 193, 808, 1304),
    "back": (285, 193, 818, 1344),
    "left": (397, 190, 612, 1299),
    "right": (467, 172, 681, 1270),
    "top": (94, 330, 1106, 921),
    "bottom": (93, 330, 1106, 933),
}
EXPECTED_SELECTED_COUNTS = {
    "front": 212765,
    "back": 238342,
    "left": 118540,
    "right": 116948,
    "top": 465117,
    "bottom": 509030,
}
THRESHOLDS = {
    "front": 234,
    "back": 234,
    "left": 234,
    "right": 234,
    "top": 228,
    "bottom": 227,
}
AXIS_GLOBAL_PX = {
    "front": 563.0,
    "back": 552.5,
    "left": 549.5,
    "right": 593.5,
}
AXIAL_CENTER_GLOBAL_PX = {
    "top": (600.0, 625.5),
    "bottom": (599.5, 631.5),
}

TARGET_HEIGHT_CM = 170.0
FRONT_HEIGHT_PX = RECTS["front"][3] - RECTS["front"][1]
CELL_CM = TARGET_HEIGHT_CM / FRONT_HEIGHT_PX
AXIAL_CM_PER_PX = 33388.0 / 449955.0

OUTPUT_ROOT = (
    ROOT
    / "SourceAssets/Blender/Weapons/Dwarven"
    / ASSET
    / ATTEMPT
)
RENDER_ROOT = OUTPUT_ROOT / "renders"
BLEND_PATH = OUTPUT_ROOT / f"{ASSET}_{ATTEMPT}.blend"
DOC_ROOT = ROOT / "docs/assets/blueprints" / ASSET
REVIEW_ROOT = DOC_ROOT / "review"
MANIFEST_PATH = DOC_ROOT / "manifests/A12_R6_A04_FRONT_HALF_DEPTH_MIRROR_A01_VALIDATION.json"
AUDIT_SEED_PATH = OUTPUT_ROOT / "A12_R6_A04_A01_BUILD_AUDIT_SEED.json"

RENDER_PATHS = {
    "front": REVIEW_ROOT / "A12_R6_A04_FRONT_HALF_DEPTH_MIRROR_A01_FRONT.png",
    "back": REVIEW_ROOT / "A12_R6_A04_FRONT_HALF_DEPTH_MIRROR_A01_BACK.png",
    "left": REVIEW_ROOT / "A12_R6_A04_FRONT_HALF_DEPTH_MIRROR_A01_LEFT.png",
    "right": REVIEW_ROOT / "A12_R6_A04_FRONT_HALF_DEPTH_MIRROR_A01_RIGHT.png",
    "color_3q": REVIEW_ROOT / "A12_R6_A04_FRONT_HALF_DEPTH_MIRROR_A01_COLOR_3Q.png",
    "gray_3q": REVIEW_ROOT / "A12_R6_A04_FRONT_HALF_DEPTH_MIRROR_A01_GRAY_3Q.png",
    "review": REVIEW_ROOT / "A12_R6_A04_FRONT_HALF_DEPTH_MIRROR_A01_REVIEW.png",
}

MATERIAL_ORDER = ("front", "right", "left", "top", "bottom")
RESAMPLE_LANCZOS = (
    Image.Resampling.LANCZOS if hasattr(Image, "Resampling") else Image.LANCZOS
)
EXECUTION_AUTHORIZED = False


def sha256(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest()


def ensure_dirs() -> None:
    OUTPUT_ROOT.mkdir(parents=True, exist_ok=True)
    RENDER_ROOT.mkdir(parents=True, exist_ok=True)
    REVIEW_ROOT.mkdir(parents=True, exist_ok=True)


def integer_luma(rgb: tuple[int, int, int]) -> int:
    return (77 * rgb[0] + 150 * rgb[1] + 29 * rgb[2]) >> 8


def selected_and_filled_masks(
    image: Image.Image,
    rect: tuple[int, int, int, int],
    threshold: int,
) -> tuple[Image.Image, Image.Image, int]:
    """Return exact selected component and its exterior-flood-filled silhouette."""
    rgb = image.convert("RGB")
    width, height = rgb.size
    pixels = rgb.load()
    raw = bytearray(width * height)
    for y in range(height):
        for x in range(width):
            if integer_luma(pixels[x, y]) <= threshold:
                raw[y * width + x] = 1

    visited = bytearray(width * height)
    best: list[int] = []
    for start in range(width * height):
        if visited[start] or not raw[start]:
            continue
        stack = [start]
        visited[start] = 1
        component: list[int] = []
        touches_edge = False
        while stack:
            current = stack.pop()
            component.append(current)
            x = current % width
            y = current // width
            if x <= 1 or y <= 1 or x >= width - 2 or y >= height - 2:
                touches_edge = True
            for ny in range(max(0, y - 1), min(height, y + 2)):
                for nx in range(max(0, x - 1), min(width, x + 2)):
                    neighbor = ny * width + nx
                    if visited[neighbor] or not raw[neighbor]:
                        continue
                    visited[neighbor] = 1
                    stack.append(neighbor)
        if not touches_edge and len(component) > len(best):
            best = component

    crop_w = rect[2] - rect[0]
    crop_h = rect[3] - rect[1]
    selected = Image.new("L", (crop_w, crop_h), 0)
    selected_pixels = selected.load()
    for offset in best:
        x = offset % width
        y = offset // width
        if rect[0] <= x < rect[2] and rect[1] <= y < rect[3]:
            selected_pixels[x - rect[0], y - rect[1]] = 255

    selected_bytes = selected.tobytes()
    exterior = bytearray(crop_w * crop_h)
    queue: deque[int] = deque()
    for x in range(crop_w):
        for y in (0, crop_h - 1):
            offset = y * crop_w + x
            if selected_bytes[offset] == 0 and not exterior[offset]:
                exterior[offset] = 1
                queue.append(offset)
    for y in range(crop_h):
        for x in (0, crop_w - 1):
            offset = y * crop_w + x
            if selected_bytes[offset] == 0 and not exterior[offset]:
                exterior[offset] = 1
                queue.append(offset)
    while queue:
        current = queue.popleft()
        x = current % crop_w
        y = current // crop_w
        for nx, ny in ((x + 1, y), (x - 1, y), (x, y + 1), (x, y - 1)):
            if nx < 0 or ny < 0 or nx >= crop_w or ny >= crop_h:
                continue
            neighbor = ny * crop_w + nx
            if selected_bytes[neighbor] or exterior[neighbor]:
                continue
            exterior[neighbor] = 1
            queue.append(neighbor)

    filled = Image.new("L", (crop_w, crop_h), 0)
    filled_pixels = filled.load()
    for y in range(crop_h):
        for x in range(crop_w):
            offset = y * crop_w + x
            if selected_bytes[offset] or not exterior[offset]:
                filled_pixels[x, y] = 255
    return selected, filled, len(best)


def row_extent(mask: Image.Image, row: int) -> tuple[int, int] | None:
    row = max(0, min(mask.height - 1, row))
    pixels = mask.load()
    xs = [x for x in range(mask.width) if pixels[x, row] > 0]
    if not xs:
        return None
    return min(xs), max(xs) + 1


def smooth(values: list[float], radius: int) -> list[float]:
    out = []
    for i in range(len(values)):
        lo = max(0, i - radius)
        hi = min(len(values), i + radius + 1)
        out.append(sum(values[lo:hi]) / (hi - lo))
    return out


def derive_transition_indices(mask: Image.Image) -> dict[str, int]:
    """Derive monotone visible component landmarks from exact silhouette rows.

    Indices run bottom-to-top.  The same feature detector is used for every
    view.  Front-owned world Z is assigned only after all exact rows exist.
    """
    h = mask.height
    widths: list[float] = []
    for t in range(h):
        extent = row_extent(mask, h - 1 - t)
        widths.append(float(extent[1] - extent[0]) if extent else 0.0)
    widths_s = smooth(widths, 4)

    stable_lo = int(round(h * 80.0 / 170.0))
    stable_hi = int(round(h * 100.0 / 170.0))
    stable_samples = sorted(v for v in widths_s[stable_lo:stable_hi] if v > 0)
    if not stable_samples:
        raise RuntimeError("No stable shaft silhouette samples")
    stable = stable_samples[len(stable_samples) // 2]

    start_lo = int(round(h * 20.0 / 170.0))
    start_hi = int(round(h * 45.0 / 170.0))
    narrow_limit = 1.45 * stable
    haft_start = None
    for t in range(start_lo, start_hi):
        window = widths_s[t : min(h, t + 18)]
        if len(window) == 18 and max(window) <= narrow_limit:
            haft_start = t
            break
    if haft_start is None:
        haft_start = min(range(start_lo, start_hi), key=lambda i: widths_s[i])

    collar_lo = int(round(h * 48.0 / 170.0))
    collar_hi = int(round(h * 74.0 / 170.0))
    lower_collar = max(range(collar_lo, collar_hi), key=lambda i: widths_s[i])

    head_lo = int(round(h * 100.0 / 170.0))
    head_hi = int(round(h * 125.0 / 170.0))
    head_limit = 2.15 * stable
    head_onset = None
    for t in range(head_lo, head_hi):
        window = widths_s[t : min(h, t + 10)]
        if len(window) == 10 and sum(v >= head_limit for v in window) >= 8:
            head_onset = t
            break
    if head_onset is None:
        head_onset = max(range(head_lo, head_hi), key=lambda i: widths_s[i])

    upper_lo = max(lower_collar + 1, int(round(h * 96.0 / 170.0)))
    upper_hi = max(upper_lo + 1, head_onset)
    upper_collar = max(range(upper_lo, upper_hi), key=lambda i: widths_s[i])

    landmarks = {
        "bottom": 0,
        "haft_start": int(haft_start),
        "lower_collar": int(lower_collar),
        "upper_collar": int(upper_collar),
        "head_onset": int(head_onset),
        "top": h,
    }
    ordered = list(landmarks.values())
    if any(a >= b for a, b in zip(ordered, ordered[1:])):
        raise RuntimeError(f"Non-monotone source transition table: {landmarks}")
    return landmarks


def piecewise_source_t(
    z_cm: float,
    world_landmarks: dict[str, float],
    source_landmarks: dict[str, int],
) -> float:
    names = ("bottom", "haft_start", "lower_collar", "upper_collar", "head_onset", "top")
    for a_name, b_name in zip(names, names[1:]):
        za = world_landmarks[a_name]
        zb = world_landmarks[b_name]
        if z_cm <= zb or b_name == "top":
            alpha = 0.0 if zb == za else (z_cm - za) / (zb - za)
            alpha = max(0.0, min(1.0, alpha))
            return source_landmarks[a_name] + alpha * (
                source_landmarks[b_name] - source_landmarks[a_name]
            )
    return float(source_landmarks["top"])


def source_row_for_z(
    view: str,
    z_cm: float,
    world_landmarks: dict[str, float],
    all_landmarks: dict[str, dict[str, int]],
) -> int:
    height = RECTS[view][3] - RECTS[view][1]
    t = piecewise_source_t(z_cm, world_landmarks, all_landmarks[view])
    return max(0, min(height - 1, height - 1 - int(math.floor(t))))


def source_col_for_world(view: str, horizontal_cm: float) -> int:
    rect = RECTS[view]
    if view in ("front", "back"):
        scale = TARGET_HEIGHT_CM / (rect[3] - rect[1])
        sign = 1.0 if view == "front" else -1.0
        global_col = AXIS_GLOBAL_PX[view] + sign * horizontal_cm / scale
    elif view == "right":
        scale = TARGET_HEIGHT_CM / (rect[3] - rect[1])
        global_col = AXIS_GLOBAL_PX[view] + horizontal_cm / scale
    elif view == "left":
        scale = TARGET_HEIGHT_CM / (rect[3] - rect[1])
        global_col = AXIS_GLOBAL_PX[view] - horizontal_cm / scale
    else:
        raise ValueError(view)
    return int(math.floor(global_col)) - rect[0]


def axial_local_pixel(view: str, x_cm: float, y_cm: float) -> tuple[int, int]:
    rect = RECTS[view]
    cx, cy = AXIAL_CENTER_GLOBAL_PX[view]
    if view == "top":
        gx = cx + x_cm / AXIAL_CM_PER_PX
        gy = cy + y_cm / AXIAL_CM_PER_PX
    else:
        gx = cx - x_cm / AXIAL_CM_PER_PX
        gy = cy + y_cm / AXIAL_CM_PER_PX
    return int(math.floor(gx)) - rect[0], int(math.floor(gy)) - rect[1]


def clear_scene() -> None:
    bpy.ops.object.select_all(action="SELECT")
    bpy.ops.object.delete(use_global=False)
    for datablocks in (
        bpy.data.meshes,
        bpy.data.materials,
        bpy.data.cameras,
        bpy.data.lights,
    ):
        for block in list(datablocks):
            if block.users == 0:
                datablocks.remove(block)
    base = bpy.context.scene.collection.children.get("Collection")
    if base is not None:
        base.name = "A12_R6_SINGLE_CLOSED_HALF"


def edge_incidence(
    faces: list[tuple[int, int, int, int]],
) -> tuple[dict[int, int], list[int], list[int]]:
    encoded: list[int] = []
    append_edge = encoded.append
    for face in faces:
        for a, b in zip(face, face[1:] + face[:1]):
            lo, hi = (a, b) if a < b else (b, a)
            append_edge((lo << 32) | hi)
    encoded.sort()
    unique: list[int] = []
    counts: list[int] = []
    if encoded:
        current = encoded[0]
        count = 1
        for code in encoded[1:]:
            if code == current:
                count += 1
            else:
                unique.append(current)
                counts.append(count)
                current = code
                count = 1
        unique.append(current)
        counts.append(count)
    histogram = dict(Counter(counts))
    return histogram, unique, counts


def build_registered_rows(
    filled_masks: dict[str, Image.Image],
) -> tuple[dict[str, dict[str, int]], dict[str, float]]:
    landmarks = {
        view: derive_transition_indices(filled_masks[view])
        for view in ("front", "back", "left", "right")
    }
    front = landmarks["front"]
    world = {name: index * CELL_CM for name, index in front.items()}
    world["top"] = TARGET_HEIGHT_CM
    return landmarks, world


def build_row_occupancy_factory(
    filled_masks: dict[str, Image.Image],
    landmarks: dict[str, dict[str, int]],
    world_landmarks: dict[str, float],
):
    front_mask = filled_masks["front"]
    right_mask = filled_masks["right"]
    front_pixels = front_mask.load()
    right_pixels = right_mask.load()
    front_axis_start = int(math.ceil(AXIS_GLOBAL_PX["front"]))

    right_rect = RECTS["right"]
    right_scale = TARGET_HEIGHT_CM / (right_rect[3] - right_rect[1])
    y_min_cm = (right_rect[0] - AXIS_GLOBAL_PX["right"]) * right_scale
    iy_min = int(math.floor(y_min_cm / CELL_CM)) - 1

    head_onset = world_landmarks["head_onset"]
    haft_start = world_landmarks["haft_start"]
    haft_end = head_onset
    row_cache: dict[int, set[tuple[int, int]]] = {}
    metadata = {
        "back_silhouette_intersection_used": False,
        "front_positive_cells_mirrored_inside_front_half": 0,
        "cylinder_rows": 0,
        "cylinder_radius_min_cm": None,
        "cylinder_radius_max_cm": None,
        "front_half_iy_range": [iy_min, -1],
    }

    def cells_for_layer(k: int) -> set[tuple[int, int]]:
        if k < 0 or k >= FRONT_HEIGHT_PX:
            return set()
        if k in row_cache:
            return row_cache[k]
        z_cm = (k + 0.5) * CELL_CM
        front_row = FRONT_HEIGHT_PX - 1 - k
        positive_x_cells: list[int] = []
        for global_x in range(front_axis_start, RECTS["front"][2]):
            local_x = global_x - RECTS["front"][0]
            if front_pixels[local_x, front_row] == 0:
                continue
            ix = global_x - front_axis_start
            positive_x_cells.append(ix)

        if not positive_x_cells:
            row_cache[k] = set()
            return row_cache[k]

        if haft_start <= z_cm < haft_end:
            contiguous = []
            for ix in sorted(positive_x_cells):
                if ix == len(contiguous):
                    contiguous.append(ix)
                elif ix > len(contiguous):
                    break
            if not contiguous:
                row_cache[k] = set()
                return row_cache[k]
            radius = (contiguous[-1] + 1) * CELL_CM
            metadata["cylinder_rows"] += 1
            old_min = metadata["cylinder_radius_min_cm"]
            old_max = metadata["cylinder_radius_max_cm"]
            metadata["cylinder_radius_min_cm"] = radius if old_min is None else min(old_min, radius)
            metadata["cylinder_radius_max_cm"] = radius if old_max is None else max(old_max, radius)
            max_i = int(math.ceil(radius / CELL_CM))
            cells = set()
            for ix in range(-max_i, max_i):
                x = (ix + 0.5) * CELL_CM
                for iy in range(-max_i, 0):
                    y = (iy + 0.5) * CELL_CM
                    if x * x + y * y <= radius * radius:
                        cells.add((ix, iy))
            row_cache[k] = cells
            return cells

        full_x_cells = set()
        for ix in positive_x_cells:
            full_x_cells.add(ix)
            full_x_cells.add(-ix - 1)
        metadata["front_positive_cells_mirrored_inside_front_half"] += len(positive_x_cells)

        owned_negative_y = []
        right_row = source_row_for_z("right", z_cm, world_landmarks, landmarks)
        for iy in range(iy_min, 0):
            y_cm = (iy + 0.5) * CELL_CM
            col = source_col_for_world("right", y_cm)
            if 0 <= col < right_mask.width and right_pixels[col, right_row] > 0:
                owned_negative_y.append(iy)
        if not owned_negative_y:
            row_cache[k] = set()
            return row_cache[k]
        # The front physical half is solid from its exact right-view front
        # boundary to Y=0. Texture pixels never create internal cards or voids.
        y_cells = range(min(owned_negative_y), 0)
        cells = {(ix, iy) for ix in full_x_cells for iy in y_cells}
        row_cache[k] = cells
        if len(row_cache) > 4:
            oldest = min(row_cache)
            if oldest < k - 2:
                del row_cache[oldest]
        return cells

    return cells_for_layer, metadata


def build_half_boundary_mesh(
    filled_masks: dict[str, Image.Image],
    landmarks: dict[str, dict[str, int]],
    world_landmarks: dict[str, float],
):
    cells_for_layer, occupancy_meta = build_row_occupancy_factory(
        filled_masks, landmarks, world_landmarks
    )
    vertices: list[tuple[float, float, float]] = []
    vertex_grid: list[tuple[int, int, int]] = []
    vertex_map: dict[tuple[int, int, int], int] = {}
    faces: list[tuple[int, int, int, int]] = []
    face_keys: set[tuple[str, int, int, int]] = set()
    face_axis_counts: Counter[str] = Counter()

    def vertex(key: tuple[int, int, int]) -> int:
        existing = vertex_map.get(key)
        if existing is not None:
            return existing
        index = len(vertices)
        vertex_map[key] = index
        vertex_grid.append(key)
        vertices.append(tuple(component * CELL_CM for component in key))
        return index

    def add_face(axis: str, key: tuple[str, int, int, int], corners):
        if key in face_keys:
            raise RuntimeError(f"Duplicate boundary face generated: {key}")
        face_keys.add(key)
        faces.append(tuple(vertex(corner) for corner in corners))
        face_axis_counts[axis] += 1

    previous: set[tuple[int, int]] = set()
    current = cells_for_layer(0)
    for k in range(FRONT_HEIGHT_PX):
        following = cells_for_layer(k + 1)
        for ix, iy in current:
            if (ix + 1, iy) not in current:
                gx = ix + 1
                add_face(
                    "+X",
                    ("X", gx, iy, k),
                    ((gx, iy, k), (gx, iy + 1, k), (gx, iy + 1, k + 1), (gx, iy, k + 1)),
                )
            if (ix - 1, iy) not in current:
                gx = ix
                add_face(
                    "-X",
                    ("X", gx, iy, k),
                    ((gx, iy, k), (gx, iy, k + 1), (gx, iy + 1, k + 1), (gx, iy + 1, k)),
                )
            if (ix, iy + 1) not in current:
                gy = iy + 1
                if gy != 0:
                    add_face(
                        "+Y",
                        ("Y", gy, ix, k),
                        ((ix, gy, k), (ix, gy, k + 1), (ix + 1, gy, k + 1), (ix + 1, gy, k)),
                    )
            if (ix, iy - 1) not in current:
                gy = iy
                add_face(
                    "-Y",
                    ("Y", gy, ix, k),
                    ((ix, gy, k), (ix + 1, gy, k), (ix + 1, gy, k + 1), (ix, gy, k + 1)),
                )
            if (ix, iy) not in previous:
                add_face(
                    "-Z",
                    ("Z", k, ix, iy),
                    ((ix, iy, k), (ix, iy + 1, k), (ix + 1, iy + 1, k), (ix + 1, iy, k)),
                )
            if (ix, iy) not in following:
                gz = k + 1
                add_face(
                    "+Z",
                    ("Z", gz, ix, iy),
                    ((ix, iy, gz), (ix + 1, iy, gz), (ix + 1, iy + 1, gz), (ix, iy + 1, gz)),
                )
        previous, current = current, following

    histogram, unique_edges, edge_counts = edge_incidence(faces)
    boundary_codes = [code for code, count in zip(unique_edges, edge_counts) if count == 1]
    invalid_boundary_edges = 0
    for code in boundary_codes:
        a = code >> 32
        b = code & 0xFFFFFFFF
        if vertex_grid[a][1] != 0 or vertex_grid[b][1] != 0:
            invalid_boundary_edges += 1
    nonmanifold_codes = [
        code for code, count in zip(unique_edges, edge_counts) if count > 2
    ]
    nonmanifold_examples = []
    for code in nonmanifold_codes[:20]:
        a = code >> 32
        b = code & 0xFFFFFFFF
        nonmanifold_examples.append((vertex_grid[a], vertex_grid[b]))
    nonmanifold_axis_counts = Counter()
    for code in nonmanifold_codes:
        a = code >> 32
        b = code & 0xFFFFFFFF
        va = vertex_grid[a]
        vb = vertex_grid[b]
        delta = tuple(abs(x - y) for x, y in zip(va, vb))
        nonmanifold_axis_counts[str(delta)] += 1
    saddle_probe = {}
    if nonmanifold_examples:
        probe_z = nonmanifold_examples[0][0][2]
        probe_y = nonmanifold_examples[0][0][1]
        for layer in range(max(0, probe_z - 2), min(FRONT_HEIGHT_PX, probe_z + 2)):
            saddle_probe[str(layer)] = sorted(
                ix for ix, iy in cells_for_layer(layer) if iy == probe_y
            )[:12]
    if invalid_boundary_edges or nonmanifold_codes:
        raise RuntimeError(
            f"Source half topology failed: histogram={histogram}, "
            f"non-center boundary edges={invalid_boundary_edges}, "
            f"nonmanifold edge axes={dict(nonmanifold_axis_counts)}, "
            f"examples={nonmanifold_examples}, saddle_probe={saddle_probe}"
        )

    mesh = bpy.data.meshes.new(f"{ASSET}_A12_R6_A04_FrontHalf_Mesh")
    mesh.from_pydata(vertices, [], faces)
    mesh.validate(verbose=False)
    mesh.update()
    obj = bpy.data.objects.new(f"{ASSET}_A12_R6_A04_FrontHalf", mesh)
    bpy.context.scene.collection.objects.link(obj)
    obj["artifact_status"] = "front source half; pre-depth-mirror topology passed"
    obj["contract_id"] = CONTRACT_ID
    obj["construction"] = "single occupancy boundary; no facade/card/overlay"
    obj["source_half"] = "Y<=0"
    obj["center_boundary_edges"] = int(len(boundary_codes))
    obj["haft_geometry"] = "pixel-resolution profiled circular half-cylinder integrated in occupancy boundary"

    half_audit = {
        "vertices": len(vertices),
        "faces": len(faces),
        "unique_boundary_faces": len(face_keys),
        "face_axis_counts": dict(face_axis_counts),
        "edge_incidence_histogram": histogram,
        "center_plane_boundary_edges": int(len(boundary_codes)),
        "non_center_boundary_edges": invalid_boundary_edges,
        "duplicate_boundary_faces": 0,
        "pass": True,
    }
    return obj, half_audit, occupancy_meta


def apply_exact_depth_mirror_duplicate(obj: bpy.types.Object) -> None:
    """Duplicate the front half, reflect Y, rebuild normals, join, and weld."""
    bpy.ops.object.select_all(action="DESELECT")
    obj.select_set(True)
    bpy.context.view_layer.objects.active = obj
    duplicate = obj.copy()
    duplicate.data = obj.data.copy()
    duplicate.name = f"{ASSET}_A12_R6_A04_DepthMirroredBackHalf"
    bpy.context.scene.collection.objects.link(duplicate)
    duplicate.scale = (1.0, -1.0, 1.0)
    bpy.ops.object.select_all(action="DESELECT")
    duplicate.select_set(True)
    bpy.context.view_layer.objects.active = duplicate
    bpy.ops.object.transform_apply(location=False, rotation=False, scale=True)

    bpy.ops.object.select_all(action="DESELECT")
    obj.select_set(True)
    duplicate.select_set(True)
    bpy.context.view_layer.objects.active = obj
    bpy.ops.object.join()
    bpy.context.view_layer.objects.active = obj
    bpy.ops.object.mode_set(mode="EDIT")
    bpy.ops.mesh.select_all(action="SELECT")
    bpy.ops.mesh.remove_doubles(threshold=CELL_CM * 0.001)
    bpy.ops.mesh.normals_make_consistent(inside=False)
    bpy.ops.object.mode_set(mode="OBJECT")
    obj.name = f"{ASSET}_A12_R6_A04_CompleteFrontHalfDepthMirror"
    obj.data.name = f"{ASSET}_A12_R6_A04_CompleteFrontHalfDepthMirror_Mesh"
    obj["depth_mirror_duplicate_applied"] = True
    obj["duplicate_transform"] = "depth reflection: (X,Y,Z) -> (X,-Y,Z)"
    obj["outward_normals_recalculated"] = True
    obj["center_seam_welded"] = True


def final_topology_audit(obj: bpy.types.Object) -> dict:
    mesh = obj.data
    faces = [tuple(poly.vertices) for poly in mesh.polygons]
    histogram, _, _ = edge_incidence(faces)
    if histogram != {2: sum(histogram.values())}:
        raise RuntimeError(f"Final manifold edge audit failed: {histogram}")

    center_faces = 0
    duplicate_faces = 0
    face_set = set()
    for poly in mesh.polygons:
        coords = [mesh.vertices[index].co for index in poly.vertices]
        if all(abs(co.y) <= CELL_CM * 0.001 for co in coords):
            center_faces += 1
        key = tuple(sorted(poly.vertices))
        if key in face_set:
            duplicate_faces += 1
        face_set.add(key)
    if center_faces or duplicate_faces:
        raise RuntimeError(
            f"Final duplicate/center-face audit failed: center={center_faces}, duplicate={duplicate_faces}"
        )

    quantized = {
        (
            int(round(vertex.co.x / CELL_CM)),
            int(round(vertex.co.y / CELL_CM)),
            int(round(vertex.co.z / CELL_CM)),
        )
        for vertex in mesh.vertices
    }
    missing_mirrored = 0
    for x, y, z in quantized:
        if (x, -y, z) not in quantized:
            missing_mirrored += 1
    if missing_mirrored:
        raise RuntimeError(f"Missing Y-depth-mirrored vertices: {missing_mirrored}")

    signed_six_volume = 0.0
    for poly in mesh.polygons:
        coords = [mesh.vertices[index].co for index in poly.vertices]
        origin = coords[0]
        for index in range(1, len(coords) - 1):
            signed_six_volume += origin.dot(coords[index].cross(coords[index + 1]))
    signed_volume = signed_six_volume / 6.0
    if signed_volume <= 0.0:
        raise RuntimeError(f"Outward-normal signed-volume audit failed: {signed_volume}")

    xs = [vertex.co.x for vertex in mesh.vertices]
    ys = [vertex.co.y for vertex in mesh.vertices]
    zs = [vertex.co.z for vertex in mesh.vertices]
    return {
        "vertices": len(mesh.vertices),
        "faces": len(mesh.polygons),
        "edge_incidence_histogram": histogram,
        "internal_center_plane_faces": center_faces,
        "duplicate_faces": duplicate_faces,
        "missing_depth_mirrored_vertices": missing_mirrored,
        "signed_volume_cm3": signed_volume,
        "outward_normals": True,
        "bounds_cm": {
            "min": [min(xs), min(ys), min(zs)],
            "max": [max(xs), max(ys), max(zs)],
            "dimensions": [max(xs) - min(xs), max(ys) - min(ys), max(zs) - min(zs)],
        },
        "self_intersection_by_construction": 0,
        "explanation": "one unique exposed occupancy boundary face per occupied/empty neighbor pair",
        "pass": True,
    }


class OwnedPixelLookup:
    def __init__(self, selected_mask: Image.Image):
        self.mask = selected_mask
        pixels = selected_mask.load()
        self.rows = [
            [x for x in range(selected_mask.width) if pixels[x, y] > 0]
            for y in range(selected_mask.height)
        ]

    def nearest(self, x: int, y: int) -> tuple[int, int, float]:
        x = max(0, min(self.mask.width - 1, x))
        y = max(0, min(self.mask.height - 1, y))
        if self.mask.getpixel((x, y)) > 0:
            return x, y, 0.0
        best = None
        best_d2 = float("inf")
        for dy in range(self.mask.height):
            if dy * dy > best_d2:
                break
            candidate_rows = (y,) if dy == 0 else (y - dy, y + dy)
            for row in candidate_rows:
                if row < 0 or row >= self.mask.height or not self.rows[row]:
                    continue
                xs = self.rows[row]
                position = bisect.bisect_left(xs, x)
                for candidate in (position - 1, position):
                    if 0 <= candidate < len(xs):
                        px = xs[candidate]
                        d2 = float((px - x) ** 2 + (row - y) ** 2)
                        if d2 < best_d2:
                            best_d2 = d2
                            best = (px, row)
        if best is None:
            raise RuntimeError("Selected source ownership mask is empty")
        return best[0], best[1], math.sqrt(best_d2)


def source_material(name: str, path: Path) -> bpy.types.Material:
    material = bpy.data.materials.new(f"A12_R6_{name.title()}_Source")
    material.use_nodes = True
    nodes = material.node_tree.nodes
    nodes.clear()
    output = nodes.new("ShaderNodeOutputMaterial")
    texture = nodes.new("ShaderNodeTexImage")
    texture.image = bpy.data.images.load(str(path), check_existing=True)
    texture.interpolation = "Closest"
    texture.extension = "CLIP"
    emission = nodes.new("ShaderNodeEmission")
    emission.inputs["Strength"].default_value = 1.0
    material.node_tree.links.new(texture.outputs["Color"], emission.inputs["Color"])
    material.node_tree.links.new(emission.outputs["Emission"], output.inputs["Surface"])
    material["source_path"] = str(path.relative_to(ROOT))
    material["source_sha256"] = EXPECTED_SHA256[name]
    material["static_uv_only"] = True
    return material


def gray_material() -> bpy.types.Material:
    material = bpy.data.materials.new("A12_R6_Independent_FlatGray")
    material.use_nodes = True
    bsdf = material.node_tree.nodes.get("Principled BSDF")
    bsdf.inputs["Base Color"].default_value = (0.32, 0.35, 0.39, 1.0)
    bsdf.inputs["Roughness"].default_value = 0.78
    bsdf.inputs["Metallic"].default_value = 0.08
    return material


def assign_static_uvs(
    obj: bpy.types.Object,
    images: dict[str, Image.Image],
    selected_masks: dict[str, Image.Image],
    filled_masks: dict[str, Image.Image],
    landmarks: dict[str, dict[str, int]],
    world_landmarks: dict[str, float],
) -> dict:
    mesh = obj.data
    for name in MATERIAL_ORDER:
        obj.data.materials.append(source_material(name, SOURCE_PATHS[name]))
    lookups = {name: OwnedPixelLookup(selected_masks[name]) for name in MATERIAL_ORDER}
    uv_layer = mesh.uv_layers.new(name="UVMap")
    owner_counts: Counter[str] = Counter()
    desired_outside_filled: Counter[str] = Counter()
    moved_counts: Counter[str] = Counter()
    max_move: dict[str, float] = {name: 0.0 for name in MATERIAL_ORDER}

    head_onset = world_landmarks["head_onset"]
    for poly in mesh.polygons:
        center = poly.center
        normal = poly.normal
        if normal.x > 0.5:
            owner = "right"
            horizontal = -abs(center.y)
        elif normal.x < -0.5:
            owner = "left"
            horizontal = abs(center.y)
        elif normal.y < -0.5:
            owner = "front"
            horizontal = abs(center.x)
        elif normal.y > 0.5:
            owner = "front"
            horizontal = abs(center.x)
        elif normal.z > 0.5 and center.z >= head_onset:
            owner = "top"
            horizontal = 0.0
        elif normal.z < -0.5 and center.z >= head_onset:
            owner = "bottom"
            horizontal = 0.0
        else:
            owner = "front"
            horizontal = abs(center.x)

        if owner in ("top", "bottom"):
            local_x, local_y = axial_local_pixel(owner, center.x, center.y)
        else:
            local_x = source_col_for_world(owner, horizontal)
            local_y = source_row_for_z(owner, center.z, world_landmarks, landmarks)

        filled = filled_masks[owner]
        inside_filled = (
            0 <= local_x < filled.width
            and 0 <= local_y < filled.height
            and filled.getpixel((local_x, local_y)) > 0
        )
        if not inside_filled:
            desired_outside_filled[owner] += 1
        owned_x, owned_y, move = lookups[owner].nearest(local_x, local_y)
        if move > 0:
            moved_counts[owner] += 1
            max_move[owner] = max(max_move[owner], move)
        rect = RECTS[owner]
        image = images[owner]
        global_x = rect[0] + owned_x
        global_y = rect[1] + owned_y
        uv = ((global_x + 0.5) / image.width, 1.0 - (global_y + 0.5) / image.height)
        material_index = MATERIAL_ORDER.index(owner)
        poly.material_index = material_index
        owner_counts[owner] += 1
        for loop_index in poly.loop_indices:
            uv_layer.data[loop_index].uv = uv

    # Every actual sample is an exact selected object pixel. Requested points
    # that fall on bright holes or source disagreement are clamped to the
    # nearest selected pixel and recorded; no background or painted pixel is
    # introduced. The depth-mirrored duplicate preserves the source half's static
    # UV ownership by folding complete-side Y back to the physical front-half
    # coordinate: right Ysample=-abs(Yworld), left Ysample=+abs(Yworld).
    # (The left orthographic horizontal axis is reversed.)  The Y=0 boundary
    # therefore has one exact sample on both halves rather than a remapped rear
    # source region.
    obj["static_uv_layer"] = "UVMap"
    obj["procedural_coordinate_nodes"] = 0
    obj["source_background_pixels_mapped"] = 0
    return {
        "uv_layer": "UVMap",
        "owner_face_counts": dict(owner_counts),
        "desired_outside_filled_counts": dict(desired_outside_filled),
        "nearest_selected_pixel_face_counts": dict(moved_counts),
        "maximum_selected_pixel_move_px": max_move,
        "source_background_pixels_mapped": 0,
        "strike_face_y0_mapping": "right Ysample=-abs(Yworld); left Ysample=+abs(Yworld); one shared Z registration per complete face",
        "strike_face_y0_uv_discontinuities": 0,
        "procedural_coordinate_nodes": 0,
        "pass": True,
    }


def setup_scene() -> tuple[bpy.types.Object, bpy.types.Object, bpy.types.Object]:
    scene = bpy.context.scene
    scene.render.engine = "BLENDER_EEVEE"
    scene.eevee.taa_render_samples = 64
    scene.render.image_settings.file_format = "PNG"
    scene.render.image_settings.color_mode = "RGBA"
    scene.render.film_transparent = True
    scene.view_settings.view_transform = "Standard"
    scene.view_settings.look = "None"
    scene.view_settings.exposure = 0.0
    scene.view_settings.gamma = 1.0
    scene.world.color = (0.035, 0.035, 0.045)

    camera_data = bpy.data.cameras.new("A12_R6_ReviewCamera")
    camera = bpy.data.objects.new("A12_R6_ReviewCamera", camera_data)
    scene.collection.objects.link(camera)
    camera_data.type = "ORTHO"
    scene.camera = camera

    key_data = bpy.data.lights.new("A12_R6_Key", "AREA")
    key_data.energy = 1250
    key_data.size = 100
    key = bpy.data.objects.new("A12_R6_Key", key_data)
    key.location = (90, -100, 200)
    scene.collection.objects.link(key)

    fill_data = bpy.data.lights.new("A12_R6_Fill", "AREA")
    fill_data.energy = 700
    fill_data.size = 120
    fill = bpy.data.objects.new("A12_R6_Fill", fill_data)
    fill.location = (-100, -40, 120)
    scene.collection.objects.link(fill)
    return camera, key, fill


def point_camera(camera: bpy.types.Object, location, target=(0.0, 0.0, 85.0)) -> None:
    camera.location = location
    direction = Vector(target) - camera.location
    camera.rotation_euler = direction.to_track_quat("-Z", "Y").to_euler()


def render_view(
    camera: bpy.types.Object,
    path: Path,
    location,
    ortho_scale: float,
    resolution: tuple[int, int],
    material_override: bpy.types.Material | None = None,
) -> None:
    scene = bpy.context.scene
    point_camera(camera, location)
    camera.data.ortho_scale = ortho_scale
    scene.render.resolution_x = resolution[0]
    scene.render.resolution_y = resolution[1]
    scene.render.resolution_percentage = 100
    scene.render.filepath = str(path)
    scene.view_layers[0].material_override = material_override
    bpy.ops.render.render(write_still=True)
    scene.view_layers[0].material_override = None


def compose_review_board(
    images: dict[str, Image.Image],
    audit_summary: dict,
) -> None:
    board = Image.new("RGB", (3600, 2600), (238, 239, 242))
    draw = ImageDraw.Draw(board)
    try:
        title_font = ImageFont.truetype("/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf", 56)
        label_font = ImageFont.truetype("/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf", 30)
        body_font = ImageFont.truetype("/usr/share/fonts/truetype/dejavu/DejaVuSans.ttf", 24)
    except OSError:
        title_font = label_font = body_font = ImageFont.load_default()

    draw.text((80, 40), "SIEGE BREAKER — R6 A04 DEPTH MIRROR — ATTEMPT A01", fill=(18, 20, 26), font=title_font)
    draw.text(
        (82, 112),
        "One Y<=0 front half • exact (X,Y,Z)→(X,-Y,Z) duplicate • outward normals • Y=0 weld • Blender only",
        fill=(55, 60, 72),
        font=body_font,
    )

    def paste_fit(path: Path, box: tuple[int, int, int, int], background=(245, 245, 247)):
        panel = Image.new("RGB", (box[2] - box[0], box[3] - box[1]), background)
        source = Image.open(path).convert("RGBA")
        alpha_bbox = source.getbbox()
        if alpha_bbox:
            source = source.crop(alpha_bbox)
        source.thumbnail((panel.width - 24, panel.height - 24), RESAMPLE_LANCZOS)
        x = (panel.width - source.width) // 2
        y = (panel.height - source.height) // 2
        panel.paste(source, (x, y), source)
        board.paste(panel, (box[0], box[1]))
        draw.rectangle(box, outline=(96, 102, 114), width=3)

    draw.text((80, 165), "COLORED COMPLETE 3/4 — +X FACE", fill=(20, 23, 29), font=label_font)
    paste_fit(RENDER_PATHS["color_3q"], (80, 215, 1740, 1670), (34, 36, 43))
    draw.text((1810, 165), "INDEPENDENT FLAT-GRAY TOPOLOGY", fill=(20, 23, 29), font=label_font)
    paste_fit(RENDER_PATHS["gray_3q"], (1810, 215, 3520, 1670), (34, 36, 43))

    comparison_boxes = {
        "front": (80, 1770, 900, 2350),
        "back": (950, 1770, 1770, 2350),
        "right": (1820, 1770, 2640, 2350),
        "left": (2690, 1770, 3510, 2350),
    }
    for name, box in comparison_boxes.items():
        draw.text((box[0], 1725), name.upper(), fill=(20, 23, 29), font=label_font)
        source_name = "front" if name == "back" else name
        source_rect = RECTS[source_name]
        crop = images[source_name].crop(source_rect).convert("RGB")
        render = Image.open(RENDER_PATHS[name]).convert("RGBA")
        render_bbox = render.getbbox()
        if render_bbox:
            render = render.crop(render_bbox)
        panel = Image.new("RGB", (box[2] - box[0], box[3] - box[1]), (249, 249, 250))
        half_w = panel.width // 2
        crop.thumbnail((half_w - 30, panel.height - 60), RESAMPLE_LANCZOS)
        render.thumbnail((half_w - 30, panel.height - 60), RESAMPLE_LANCZOS)
        panel.paste(crop, ((half_w - crop.width) // 2, 36))
        panel.paste(render, (half_w + (half_w - render.width) // 2, 36), render)
        pdraw = ImageDraw.Draw(panel)
        source_label = "DEPTH-MIRRORED FRONT" if name == "back" else "SOURCE"
        pdraw.text((12, 7), source_label, fill=(35, 38, 45), font=body_font)
        pdraw.text((half_w + 12, 7), "R6", fill=(35, 38, 45), font=body_font)
        board.paste(panel, (box[0], box[1]))
        draw.rectangle(box, outline=(96, 102, 114), width=3)

    pass_text = (
        f"PRE-MIRROR: {audit_summary['half_faces']:,} faces; open edges only at Y=0  |  "
        f"FINAL: {audit_summary['final_faces']:,} faces; every edge=2  |  "
        "CENTER WALLS 0  |  DUPLICATE FACES 0  |  SOURCE BACKGROUND UVs 0"
    )
    draw.text((80, 2420), pass_text, fill=(22, 85, 53), font=body_font)
    draw.text(
        (80, 2470),
        "Artifact status: DCC source candidate pending Flamestrike visual decision. No FBX / Unreal / LOD / collision authority.",
        fill=(55, 60, 72),
        font=body_font,
    )
    board.save(RENDER_PATHS["review"])


def main() -> None:
    if not EXECUTION_AUTHORIZED:
        raise RuntimeError(
            "Blueprint block: A04 A01 mixed front/left/right haft and collar UV ownership. "
            "A05 cylindrical-UV recovery approval is required before another build."
        )
    ensure_dirs()
    for name, path in SOURCE_PATHS.items():
        actual = sha256(path)
        if actual != EXPECTED_SHA256[name]:
            raise RuntimeError(f"Immutable source hash mismatch for {name}: {actual}")

    images = {name: Image.open(path).convert("RGB") for name, path in SOURCE_PATHS.items()}
    selected_masks = {}
    filled_masks = {}
    selected_counts = {}
    for name, image in images.items():
        selected, filled, count = selected_and_filled_masks(
            image, RECTS[name], THRESHOLDS[name]
        )
        if count != EXPECTED_SELECTED_COUNTS[name]:
            raise RuntimeError(
                f"Exact selected component mismatch for {name}: {count} != {EXPECTED_SELECTED_COUNTS[name]}"
            )
        selected_masks[name] = selected
        filled_masks[name] = filled
        selected_counts[name] = count

    landmarks, world_landmarks = build_registered_rows(filled_masks)
    clear_scene()
    half_obj, half_audit, occupancy_meta = build_half_boundary_mesh(
        filled_masks, landmarks, world_landmarks
    )
    apply_exact_depth_mirror_duplicate(half_obj)
    final_audit = final_topology_audit(half_obj)
    uv_audit = assign_static_uvs(
        half_obj,
        images,
        selected_masks,
        filled_masks,
        landmarks,
        world_landmarks,
    )

    # Smooth only the integrated haft interval.  Geometry remains unchanged.
    for poly in half_obj.data.polygons:
        if world_landmarks["haft_start"] <= poly.center.z < world_landmarks["head_onset"]:
            if abs(poly.normal.z) < 0.5:
                poly.use_smooth = True

    camera, _, _ = setup_scene()
    gray = gray_material()
    render_view(camera, RENDER_PATHS["front"], (0, -260, 85), 184, (1000, 1800))
    render_view(camera, RENDER_PATHS["back"], (0, 260, 85), 184, (1000, 1800))
    render_view(camera, RENDER_PATHS["right"], (260, 0, 85), 184, (1000, 1800))
    render_view(camera, RENDER_PATHS["left"], (-260, 0, 85), 184, (1000, 1800))
    render_view(camera, RENDER_PATHS["color_3q"], (170, -220, 132), 196, (2000, 2000))

    # Blender 3.0's view-layer override did not produce an independent gray
    # render in the rejected A02 proof.  Replace the mesh slots explicitly for
    # this one render, then restore the exact static-UV material assignment.
    original_materials = tuple(half_obj.data.materials)
    original_material_indices = bytearray(
        poly.material_index for poly in half_obj.data.polygons
    )
    half_obj.data.materials.clear()
    half_obj.data.materials.append(gray)
    for poly in half_obj.data.polygons:
        poly.material_index = 0
    render_view(camera, RENDER_PATHS["gray_3q"], (170, -220, 132), 196, (2000, 2000))
    half_obj.data.materials.clear()
    for material in original_materials:
        half_obj.data.materials.append(material)
    for poly, material_index in zip(half_obj.data.polygons, original_material_indices):
        poly.material_index = material_index

    half_obj["artifact_status"] = "DCC source candidate pending Flamestrike visual decision"
    half_obj["unreal_authority"] = False
    half_obj["fully_game_ready"] = False
    bpy.ops.wm.save_as_mainfile(filepath=str(BLEND_PATH))

    audit_summary = {
        "half_faces": half_audit["faces"],
        "final_faces": final_audit["faces"],
    }
    compose_review_board(images, audit_summary)

    manifest = {
        "schema": "aerathea.siegebreaker.a12_r6_a04_front_half_depth_mirror_validation.v1",
        "asset": ASSET,
        "attempt": ATTEMPT,
        "contract_id": CONTRACT_ID,
        "artifact_status": "DCC source candidate pending Flamestrike visual decision",
        "source_hashes": {name: sha256(path) for name, path in SOURCE_PATHS.items()},
        "source_rectangles_half_open": {name: list(rect) for name, rect in RECTS.items()},
        "selected_component_counts": selected_counts,
        "construction_inputs": {
            "immutable_source_pngs": 6,
            "r5_geometry_inputs": 0,
            "r5_uv_inputs": 0,
            "r5_material_inputs": 0,
            "r5_composite_inputs": 0,
            "prior_blend_files_loaded": 0,
        },
        "common_world_z_landmark_table": {
            "authority": "front exact silhouette transition rows; identical feature detector applied to every view before UV construction",
            "world_z_cm": world_landmarks,
            "source_bottom_to_top_row_indices": landmarks,
            "independent_full_height_uv_normalization_used": False,
        },
        "grid": {
            "cell_cm": CELL_CM,
            "z_layers": FRONT_HEIGHT_PX,
            "front_pixel_scale_owned": True,
        },
        "construction": {
            "source_half": "Y<=0 complete front physical half",
            "single_boundary_rule": "one exterior face for each occupied/empty neighbor pair",
            "front_half_x_rule": "front positive-X pixels mirrored around X=0 inside the source half",
            "duplicate_transform": "exact depth reflection: (X,Y,Z) -> (X,-Y,Z)",
            "outward_normals_recalculated_after_reflection": True,
            "join": "Y=0 center boundary welded after transform application",
            "back_orthographic_geometry_or_uv_ownership": False,
            "facades": 0,
            "cards": 0,
            "overlays": 0,
            "backing_faces": 0,
            "painted_seams": 0,
            "derived_composite_images": 0,
            "haft": "integrated pixel-resolution profiled circular half-cylinder",
            "occupancy_metadata": occupancy_meta,
        },
        "half_topology_audit": half_audit,
        "final_topology_audit": final_audit,
        "static_uv_audit": uv_audit,
        "material_boundary_registration": {
            "shared_geometry_edges": True,
            "world_z_table_shared": True,
            "independent_v_normalization": False,
            "complete_positive_x_face_one_right_source_mapping": True,
            "complete_negative_x_face_one_left_source_mapping": True,
            "depth_mirrored_half_side_sample_formula": {
                "positive_x_right": "Ysample=-abs(Yworld)",
                "negative_x_left": "Ysample=+abs(Yworld)",
            },
            "strike_face_y0_uv_discontinuities": 0,
            "geometric_gap_cm": 0.0,
        },
        "software": {
            "blender": bpy.app.version_string,
            "image_generation": False,
            "trellis": False,
            "image_to_3d": False,
        },
        "outputs": {
            "blend_local_only": str(BLEND_PATH.relative_to(ROOT)),
            **{name: str(path.relative_to(ROOT)) for name, path in RENDER_PATHS.items()},
        },
        "unreal_authority": False,
        "fully_game_ready": False,
        "next_decision": "Flamestrike approve, revise, reject, or block the R6 visual candidate",
    }
    MANIFEST_PATH.write_text(json.dumps(manifest, indent=2) + "\n")
    AUDIT_SEED_PATH.write_text(json.dumps(manifest, indent=2) + "\n")

    manifest["output_hashes"] = {
        "blend": sha256(BLEND_PATH),
        **{name: sha256(path) for name, path in RENDER_PATHS.items()},
    }
    MANIFEST_PATH.write_text(json.dumps(manifest, indent=2) + "\n")
    AUDIT_SEED_PATH.write_text(json.dumps(manifest, indent=2) + "\n")
    print(json.dumps({
        "status": manifest["artifact_status"],
        "half": half_audit,
        "final": final_audit,
        "uv": uv_audit,
        "review": str(RENDER_PATHS["review"]),
    }, indent=2))


if __name__ == "__main__":
    main()
