#!/usr/bin/env python3
"""Build the bounded A005 Step 15 UV/texture/material candidate.

The schema-only path imports no bpy and performs no filesystem writes. The
build path is intended for Blender background mode and writes only the exact
Step 15 candidate outputs declared below.
"""

from __future__ import annotations

import argparse
import hashlib
import json
import math
import random
import sys
from collections import Counter, deque
from pathlib import Path
from typing import Any, Dict, Iterable, List, Sequence, Tuple


ASSET_ID = "SM_GIA_BloodAxeCairnstone_A005"
CONTRACT_ID = "A005-CR-STEP15-UV-TEXTURE-MATERIAL-CANDIDATE-A01"
SCRIPT_PATH = Path(__file__).resolve()
REPO_ROOT = SCRIPT_PATH.parents[2]
A005_REL = Path("docs/assets/blueprints") / ASSET_ID
MANIFESTS_REL = A005_REL / "manifests"
INPUT_LOCK_REL = MANIFESTS_REL / "STEP_15_INPUT_LOCK.json"
UV_PLAN_REL = MANIFESTS_REL / "STEP_14_UV_OWNERSHIP_PLAN.json"
BASE_PLAN_REL = MANIFESTS_REL / "STEP_14_BASE_COLOR_OWNERSHIP_MANIFEST.json"
MATERIAL_PLAN_REL = MANIFESTS_REL / "STEP_14_MATERIAL_INTERPRETATION_MANIFEST.json"
DELIVERY_PLAN_REL = MANIFESTS_REL / "STEP_14_TEXTURE_DELIVERY_AND_VALIDATION_PLAN.json"
PANEL_MANIFEST_REL = MANIFESTS_REL / "STEP_03_PANEL_CROP_MANIFEST.json"

DCC_REL = Path("SourceAssets/Blender/Props/Giants/BloodAxe/Cairns") / ASSET_ID
SOURCE_BLEND_REL = DCC_REL / f"{ASSET_ID}_DCCSource_A01.blend"
GEOMETRY_MANIFEST_REL = DCC_REL / f"{ASSET_ID}_GEOMETRY_MANIFEST.json"
CANDIDATE_BLEND_REL = DCC_REL / f"{ASSET_ID}_UVTextureMaterialCandidate_A01.blend"
CANDIDATE_MANIFEST_REL = DCC_REL / f"{ASSET_ID}_STEP15_CANDIDATE_MANIFEST.json"

TEXTURE_REL = Path("SourceAssets/Textures/Props/Giants/BloodAxe/Cairns") / ASSET_ID
MASK_REL = TEXTURE_REL / "Masks"
TECH_REL = TEXTURE_REL / "Technical"
BC_REL = TEXTURE_REL / f"T_GIA_BloodAxeCairnstone_A005_BC.png"
NORMAL_REL = TEXTURE_REL / f"T_GIA_BloodAxeCairnstone_A005_N.png"
ORM_REL = TEXTURE_REL / f"T_GIA_BloodAxeCairnstone_A005_ORM.png"
CLASS_REL = TECH_REL / f"{ASSET_ID}_TEXEL_CLASSIFICATION_A01.png"
AO_REL = TECH_REL / f"{ASSET_ID}_AO_BAKE_A01.png"
MASK_MANIFEST_REL = TECH_REL / f"{ASSET_ID}_SOURCE_MASK_MANIFEST_A01.json"

VIEWS = ("front", "back", "left", "right", "top")
OBJECTS = ("C004_APRON", "C003_LOWER_TIER", "C002_UPPER_TIER", "C001_BODY")
COMPONENTS = ("C-001", "C-002", "C-003", "C-004")
ATLAS_SIZE = 2048
APPROVED_SOURCE_HASH = "5b4af2275a70e2598e72361382fc7ea6ea318724ac928d71b2c200c768a93095"
RED_PREDICATE = lambda r, g, b: r - max(g, b) >= 18 and r >= 50

Vec2 = Tuple[float, float]
Vec3 = Tuple[float, float, float]


def parse_args(argv: Sequence[str]) -> argparse.Namespace:
    parser = argparse.ArgumentParser(description=__doc__)
    modes = parser.add_mutually_exclusive_group(required=True)
    modes.add_argument("--schema-only", action="store_true")
    modes.add_argument("--build", action="store_true")
    return parser.parse_args(list(argv))


def blender_script_args() -> List[str]:
    if "--" in sys.argv:
        return sys.argv[sys.argv.index("--") + 1 :]
    return sys.argv[1:]


def sha256_file(path: Path) -> str:
    digest = hashlib.sha256()
    with path.open("rb") as handle:
        for chunk in iter(lambda: handle.read(1024 * 1024), b""):
            digest.update(chunk)
    return digest.hexdigest()


def sha256_rgb(image: Any) -> str:
    return hashlib.sha256(image.convert("RGB").tobytes()).hexdigest()


def load_json(rel_path: Path) -> Dict[str, Any]:
    with (REPO_ROOT / rel_path).open("r", encoding="utf-8") as handle:
        return json.load(handle)


def validate_closed_world(value: str, label: str) -> None:
    for suffix in range(1, 5):
        legacy = f"SM_GIA_BloodAxeCairnstone_A{suffix:03d}"
        if legacy in value:
            raise RuntimeError(f"blocked legacy asset in {label}: {legacy}")
    if "CoreRecovery" in value:
        raise RuntimeError(f"blocked quarantined input in {label}")


def verify_input_lock() -> Tuple[Dict[str, Any], List[Dict[str, Any]]]:
    lock = load_json(INPUT_LOCK_REL)
    if lock.get("asset_id") != ASSET_ID or lock.get("contract_id") != CONTRACT_ID:
        raise RuntimeError("Step 15 input-lock identity mismatch")
    if not lock.get("locked"):
        raise RuntimeError("Step 15 input lock is not locked")
    entries = lock.get("locked_inputs", [])
    if lock.get("counts", {}).get("locked_inputs") != len(entries):
        raise RuntimeError("Step 15 locked-input count mismatch")
    results: List[Dict[str, Any]] = []
    for entry in entries:
        rel = entry["path"]
        validate_closed_world(rel, "locked input")
        path = REPO_ROOT / rel
        actual = sha256_file(path) if path.is_file() and not path.is_symlink() else None
        match = actual == entry["sha256"]
        results.append({"path": rel, "expected": entry["sha256"], "actual": actual, "match": match})
        if not match:
            raise RuntimeError(f"Step 15 locked-input mismatch: {rel}")
    if sha256_file(REPO_ROOT / SOURCE_BLEND_REL) != APPROVED_SOURCE_HASH:
        raise RuntimeError("approved source candidate hash mismatch")
    return lock, results


def source_panels() -> Dict[str, Path]:
    manifest = load_json(PANEL_MANIFEST_REL)
    mapping = {entry["id"]: Path(entry["path"]) for entry in manifest["panels"]}
    return {view: mapping[view] for view in (*VIEWS, "perspective")}


def verify_source_pixels(lock: Dict[str, Any]) -> List[Dict[str, Any]]:
    from PIL import Image

    expected = lock["source_pixel_hashes"]
    results: List[Dict[str, Any]] = []
    for view, rel in source_panels().items():
        with Image.open(REPO_ROOT / rel) as image:
            actual = sha256_rgb(image)
            size = list(image.size)
        match = actual == expected[view]
        results.append({"view": view, "path": str(rel), "size": size, "pixel_sha256": actual, "match": match})
        if not match:
            raise RuntimeError(f"source RGB identity mismatch: {view}")
    return results


def allowed_outputs() -> List[str]:
    outputs = [
        CANDIDATE_BLEND_REL,
        CANDIDATE_MANIFEST_REL,
        BC_REL,
        NORMAL_REL,
        ORM_REL,
        CLASS_REL,
        AO_REL,
        MASK_MANIFEST_REL,
    ]
    outputs.extend(MASK_REL / f"{ASSET_ID}_SOURCE_OWNED_MASK_{view.upper()}_A01.png" for view in VIEWS)
    return [str(path) for path in outputs]


def schema_report() -> Dict[str, Any]:
    lock, results = verify_input_lock()
    pixels = verify_source_pixels(lock)
    for value in (ASSET_ID, CONTRACT_ID, *allowed_outputs()):
        validate_closed_world(value, "schema declaration")
    return {
        "schema": "aerathea.step15_builder_schema_preflight.v1",
        "asset_id": ASSET_ID,
        "contract_id": CONTRACT_ID,
        "status": "pass_schema_only_no_output",
        "bpy_imported": "bpy" in sys.modules,
        "filesystem_writes": 0,
        "locked_inputs_verified": len(results),
        "source_pixels_verified": len(pixels),
        "allowed_outputs": allowed_outputs(),
        "step16_outputs": 0,
    }


def neighbors8(index: int, width: int, height: int) -> Iterable[int]:
    x = index % width
    y = index // width
    for dy in (-1, 0, 1):
        yy = y + dy
        if yy < 0 or yy >= height:
            continue
        for dx in (-1, 0, 1):
            if dx == 0 and dy == 0:
                continue
            xx = x + dx
            if 0 <= xx < width:
                yield yy * width + xx


def dilate(mask: bytearray, width: int, height: int, radius: int) -> bytearray:
    if radius <= 0:
        return bytearray(mask)
    horizontal = bytearray(width * height)
    for y in range(height):
        row = y * width
        active = [x for x in range(width) if mask[row + x]]
        for x in active:
            lo = max(0, x - radius)
            hi = min(width, x + radius + 1)
            horizontal[row + lo : row + hi] = b"\x01" * (hi - lo)
    result = bytearray(width * height)
    for y in range(height):
        lo = max(0, y - radius)
        hi = min(height, y + radius + 1)
        for yy in range(lo, hi):
            source = yy * width
            target = y * width
            for x in range(width):
                if horizontal[source + x]:
                    result[target + x] = 1
    return result


def components(mask: bytearray, width: int, height: int) -> List[List[int]]:
    seen = bytearray(width * height)
    found: List[List[int]] = []
    for start, value in enumerate(mask):
        if not value or seen[start]:
            continue
        seen[start] = 1
        queue: deque[int] = deque([start])
        current: List[int] = []
        while queue:
            index = queue.popleft()
            current.append(index)
            for neighbor in neighbors8(index, width, height):
                if mask[neighbor] and not seen[neighbor]:
                    seen[neighbor] = 1
                    queue.append(neighbor)
        found.append(current)
    return found


def paper_and_seed(image: Any) -> Tuple[Tuple[int, int, int], bytearray, int]:
    rgb = image.convert("RGB")
    width, height = rgb.size
    pixels = rgb.load()
    border: List[Tuple[int, int, int]] = []
    for y in range(height):
        for x in range(width):
            if x < 8 or x >= width - 8 or y < 8 or y >= height - 8:
                border.append(pixels[x, y])
    paper = tuple(sorted(pixel[channel] for pixel in border)[len(border) // 2] for channel in range(3))
    seed = bytearray(width * height)
    red_count = 0
    for y in range(height):
        for x in range(width):
            value = pixels[x, y]
            red = RED_PREDICATE(*value)
            if red:
                red_count += 1
            if max(abs(value[channel] - paper[channel]) for channel in range(3)) >= 24 or red:
                seed[y * width + x] = 1
    return paper, seed, red_count


def central_object_selection(seed: bytearray, width: int, height: int) -> Tuple[Tuple[int, int, int, int], bytearray, Dict[str, Any]]:
    # The approved matte predicate is evaluated before any growth.  Selecting
    # from a dilated foreground graph can connect the object to thin dimension
    # lines and labels; Attempt 01 proved that is not a safe ownership basis.
    groups = components(seed, width, height)
    if not groups:
        raise RuntimeError("no source foreground components")
    center_x = 0.5 * (width - 1)
    ranked: List[Tuple[int, float, List[int]]] = []
    for group in groups:
        xs = [index % width for index in group]
        horizontal_distance = abs((min(xs) + max(xs)) * 0.5 - center_x)
        ranked.append((len(group), -horizontal_distance, group))
    ranked.sort(key=lambda item: (item[0], item[1]), reverse=True)
    selected = ranked[0][2]
    selected_mask = bytearray(width * height)
    for index in selected:
        selected_mask[index] = 1
    if not selected:
        raise RuntimeError("central source foreground selection is empty")
    xs = [index % width for index in selected]
    ys = [index // width for index in selected]
    bbox = (min(xs), min(ys), max(xs), max(ys))
    bbox_width = bbox[2] - bbox[0] + 1
    bbox_height = bbox[3] - bbox[1] + 1
    second_size = ranked[1][0] if len(ranked) > 1 else 0
    dominance = float(len(selected)) / float(max(1, second_size))
    density = float(len(selected)) / float(bbox_width * bbox_height)
    center_offset_fraction = abs((bbox[0] + bbox[2]) * 0.5 - center_x) / float(width)
    safe = (
        dominance >= 8.0
        and density >= 0.40
        and center_offset_fraction <= 0.20
        and bbox_width >= int(math.floor(width * 0.35))
        and bbox_height >= int(math.floor(height * 0.50))
        and bbox[0] > 3
        and bbox[1] > 3
        and bbox[2] < width - 4
        and bbox[3] < height - 4
    )
    record = {
        "method": "largest_8_connected_raw_foreground_component_before_any_growth",
        "selected_pixels": len(selected),
        "second_largest_pixels": second_size,
        "dominance_ratio": dominance,
        "bbox_density": density,
        "horizontal_center_offset_fraction": center_offset_fraction,
        "component_count": len(groups),
        "safe_against_thin_external_annotation_components": safe,
    }
    if not safe:
        raise RuntimeError(f"source-object selection failed annotation-contamination preflight: {record}")
    return bbox, selected_mask, record


def face_normal(vertices: Sequence[Vec3]) -> Vec3:
    for index in range(1, len(vertices) - 1):
        a = vertices[0]
        b = vertices[index]
        c = vertices[index + 1]
        u = (b[0] - a[0], b[1] - a[1], b[2] - a[2])
        v = (c[0] - a[0], c[1] - a[1], c[2] - a[2])
        normal = (
            u[1] * v[2] - u[2] * v[1],
            u[2] * v[0] - u[0] * v[2],
            u[0] * v[1] - u[1] * v[0],
        )
        length = math.sqrt(sum(value * value for value in normal))
        if length > 1.0e-12:
            return tuple(value / length for value in normal)  # type: ignore[return-value]
    raise RuntimeError("degenerate face normal")


def hidden_face(authority: str, vertices: Sequence[Vec3]) -> bool:
    if authority in {
        "VAG-005-C001-HIDDEN-BOTTOM",
        "VAG-007-C002-HIDDEN-CLOSURES",
        "VAG-009-C003-HIDDEN-CLOSURES",
        "VAG-013-C004-Z0-BOTTOM",
        "VAG-014-CL001-CL003-HIDDEN-OVERLAP",
    }:
        return True
    if authority == "VAG-012-C004-FINAL-FIRST-CLOSURE-FACE":
        return min(vertex[2] for vertex in vertices) >= 10.0 - 1.0e-7
    return False


def normal_owner(normal: Vec3) -> str:
    nx, ny, nz = normal
    ax, ay = abs(nx), abs(ny)
    if nz > 0.0 and nz >= ax and nz >= ay:
        return "top"
    if ax > ay:
        return "right" if nx > 0.0 else "left"
    if ay > ax:
        return "back" if ny > 0.0 else "front"
    if nx >= 0.0 and ny >= 0.0:
        return "back"
    if nx < 0.0 and ny >= 0.0:
        return "left"
    if nx < 0.0 and ny < 0.0:
        return "front"
    return "right"


def project_point(point: Vec3, view: str, bbox: Tuple[int, int, int, int]) -> Tuple[float, float, float]:
    xmin, ymin, xmax, ymax = bbox
    width = max(1.0, float(xmax - xmin))
    height = max(1.0, float(ymax - ymin))
    x, y, z = point
    if view == "front":
        horizontal, hmin, hmax, depth = x, -70.0, 70.0, -y
    elif view == "back":
        horizontal, hmin, hmax, depth = -x, -70.0, 70.0, y
    elif view == "left":
        horizontal, hmin, hmax, depth = -y, -55.0, 55.0, -x
    elif view == "right":
        horizontal, hmin, hmax, depth = y, -55.0, 55.0, x
    elif view == "top":
        px = xmin + ((x + 70.0) / 140.0) * width
        py = ymin + ((55.0 - y) / 110.0) * height
        return px, py, z
    else:
        raise RuntimeError(f"unknown projection view: {view}")
    px = xmin + ((horizontal - hmin) / (hmax - hmin)) * width
    py = ymax - (z / 220.0) * height
    return px, py, depth


def triangle_pixels(points: Sequence[Tuple[float, float, float]], width: int, height: int) -> Iterable[Tuple[int, int, float]]:
    (x0, y0, z0), (x1, y1, z1), (x2, y2, z2) = points
    area = (x1 - x0) * (y2 - y0) - (y1 - y0) * (x2 - x0)
    if abs(area) < 1.0e-12:
        return
    xmin = max(0, int(math.floor(min(x0, x1, x2))))
    xmax = min(width - 1, int(math.ceil(max(x0, x1, x2))))
    ymin = max(0, int(math.floor(min(y0, y1, y2))))
    ymax = min(height - 1, int(math.ceil(max(y0, y1, y2))))
    for y in range(ymin, ymax + 1):
        py = y + 0.5
        for x in range(xmin, xmax + 1):
            px = x + 0.5
            w0 = ((x1 - px) * (y2 - py) - (y1 - py) * (x2 - px)) / area
            w1 = ((x2 - px) * (y0 - py) - (y2 - py) * (x0 - px)) / area
            w2 = 1.0 - w0 - w1
            if min(w0, w1, w2) >= -1.0e-9:
                yield x, y, w0 * z0 + w1 * z1 + w2 * z2


def build_face_records(geometry: Dict[str, Any]) -> List[Dict[str, Any]]:
    records: List[Dict[str, Any]] = []
    for object_entry in geometry["objects"]:
        vertices = [tuple(entry["coordinate_cm"]) for entry in object_entry["vertices"]]
        for face in object_entry["faces"]:
            points = [vertices[index] for index in face["vertex_indices"]]
            hidden = hidden_face(face["authority_group_id"], points)
            owner = "authored" if hidden else normal_owner(face_normal(points))
            records.append(
                {
                    "object_name": object_entry["object_name"],
                    "component_id": object_entry["component_id"],
                    "face_index": face["index"],
                    "authority_group_id": face["authority_group_id"],
                    "vertex_indices": face["vertex_indices"],
                    "vertices": points,
                    "owner": owner,
                    "hidden": hidden,
                }
            )
    return records


def raster_owner_view(face_records: Sequence[Dict[str, Any]], view: str, bbox: Tuple[int, int, int, int], width: int, height: int) -> Tuple[bytearray, List[int]]:
    depth = [-1.0e30] * (width * height)
    component_code = [0] * (width * height)
    component_to_code = {component: index + 1 for index, component in enumerate(COMPONENTS)}
    for face in face_records:
        if face["owner"] != view:
            continue
        projected = [project_point(point, view, bbox) for point in face["vertices"]]
        for index in range(1, len(projected) - 1):
            for x, y, value in triangle_pixels((projected[0], projected[index], projected[index + 1]), width, height):
                offset = y * width + x
                if value >= depth[offset]:
                    depth[offset] = value
                    component_code[offset] = component_to_code[face["component_id"]]
    coverage = bytearray(1 if code else 0 for code in component_code)
    return coverage, component_code


def apply_small_component_rule(mask: bytearray, width: int, height: int) -> bytearray:
    groups = components(mask, width, height)
    large = [group for group in groups if len(group) >= 64]
    large_mask = bytearray(width * height)
    for group in large:
        for index in group:
            large_mask[index] = 1
    near_large = dilate(large_mask, width, height, 2)
    result = bytearray(width * height)
    for group in groups:
        keep = len(group) >= 4 or any(near_large[index] for index in group)
        if keep:
            for index in group:
                result[index] = 1
    return result


def source_mask(seed: bytearray, coverage: bytearray, width: int, height: int) -> bytearray:
    grown = dilate(coverage, width, height, 1)
    intersected = bytearray(1 if seed[index] and grown[index] else 0 for index in range(width * height))
    return apply_small_component_rule(intersected, width, height)


def weighted_kmedoids(colors: Sequence[Tuple[int, int, int]], count: int = 8) -> List[Tuple[int, int, int]]:
    frequencies = Counter(colors)
    if not frequencies:
        return [(48, 45, 42)] * count
    candidates = sorted(frequencies, key=lambda color: (-frequencies[color], color))[:512]
    rng = random.Random(0)
    first = candidates[rng.randrange(len(candidates))]
    medoids = [first]
    while len(medoids) < min(count, len(candidates)):
        remaining = [color for color in candidates if color not in medoids]
        selected = max(
            remaining,
            key=lambda color: (
                min(sum(abs(color[channel] - medoid[channel]) for channel in range(3)) for medoid in medoids),
                tuple(-value for value in color),
            ),
        )
        medoids.append(selected)
    for _ in range(6):
        clusters: Dict[Tuple[int, int, int], List[Tuple[int, int, int]]] = {medoid: [] for medoid in medoids}
        for color in candidates:
            owner = min(medoids, key=lambda medoid: (sum(abs(color[channel] - medoid[channel]) for channel in range(3)), medoid))
            clusters[owner].append(color)
        updated: List[Tuple[int, int, int]] = []
        for old in medoids:
            cluster = clusters[old]
            best = min(
                cluster,
                key=lambda candidate: (
                    sum(
                        frequencies[other] * sum(abs(candidate[channel] - other[channel]) for channel in range(3))
                        for other in cluster
                    ),
                    candidate,
                ),
            )
            updated.append(best)
        if updated == medoids:
            break
        medoids = updated
    while len(medoids) < count:
        medoids.append(medoids[-1])
    return sorted(medoids)


def non_red(color: Tuple[int, int, int]) -> bool:
    return not RED_PREDICATE(*color)


def authored_color(palette: Sequence[Tuple[int, int, int]], x: int, y: int, component_code: int) -> Tuple[int, int, int]:
    block_x = x // 28
    block_y = y // 28
    index = (block_x * 17 + block_y * 31 + component_code * 13) % len(palette)
    return palette[index]


def face_uv_pixels(face: Dict[str, Any], bboxes: Dict[str, Tuple[int, int, int, int]], windows: Dict[str, List[int]], hidden_index: int) -> Tuple[List[Vec2], int]:
    if face["owner"] != "authored":
        view = face["owner"]
        rect = windows[view]
        pixels = []
        for point in face["vertices"]:
            px, py, _ = project_point(point, view, bboxes[view])
            pixels.append((rect[0] + px, rect[1] + py))
        return pixels, hidden_index
    zone_x0, zone_y0, zone_x1, zone_y1 = (16, 976, 2032, 2032)
    cell = 60
    columns = (zone_x1 - zone_x0) // cell
    row = hidden_index // columns
    column = hidden_index % columns
    if zone_y0 + (row + 1) * cell > zone_y1:
        raise RuntimeError("authored-zone face capacity exceeded")
    inner_min_x = zone_x0 + column * cell + 16
    inner_min_y = zone_y0 + row * cell + 16
    inner_size = cell - 32
    vertices = face["vertices"]
    normal = face_normal(vertices)
    dominant = max(range(3), key=lambda index: abs(normal[index]))
    axes = [axis for axis in range(3) if axis != dominant]
    coordinates = [(point[axes[0]], point[axes[1]]) for point in vertices]
    min_a = min(value[0] for value in coordinates)
    max_a = max(value[0] for value in coordinates)
    min_b = min(value[1] for value in coordinates)
    max_b = max(value[1] for value in coordinates)
    span_a = max(max_a - min_a, 1.0e-8)
    span_b = max(max_b - min_b, 1.0e-8)
    pixels = [
        (
            inner_min_x + 1 + ((value[0] - min_a) / span_a) * (inner_size - 2),
            inner_min_y + 1 + ((value[1] - min_b) / span_b) * (inner_size - 2),
        )
        for value in coordinates
    ]
    return pixels, hidden_index + 1


def polygon_mask(polygons: Sequence[Sequence[Vec2]], width: int, height: int) -> bytearray:
    from PIL import Image, ImageDraw

    image = Image.new("L", (width, height), 0)
    draw = ImageDraw.Draw(image)
    for polygon in polygons:
        draw.polygon([(round(x, 6), round(y, 6)) for x, y in polygon], fill=1)
    return bytearray(image.tobytes())


def build_maps_and_uv(face_records: List[Dict[str, Any]], panels: Dict[str, Any], uv_plan: Dict[str, Any], base_plan: Dict[str, Any]) -> Dict[str, Any]:
    from PIL import Image, ImageFilter

    windows = {entry["view"]: entry["rect"] for entry in uv_plan["uv0"]["source_windows_half_open_px"]}
    panel_paths = source_panels()
    bboxes: Dict[str, Tuple[int, int, int, int]] = {}
    masks: Dict[str, bytearray] = {}
    component_maps: Dict[str, List[int]] = {}
    panel_images: Dict[str, Any] = {}
    mask_records: List[Dict[str, Any]] = []
    palette_inputs: Dict[str, List[Tuple[int, int, int]]] = {component: [] for component in COMPONENTS}
    for view in VIEWS:
        image = Image.open(REPO_ROOT / panel_paths[view]).convert("RGB")
        panel_images[view] = image
        width, height = image.size
        paper, seed, raw_red_count = paper_and_seed(image)
        bbox, selected_object, selection = central_object_selection(seed, width, height)
        bboxes[view] = bbox
        coverage, component_map = raster_owner_view(face_records, view, bbox, width, height)
        mask = source_mask(seed, coverage, width, height)
        selected_or_near = dilate(selected_object, width, height, 2)
        outside_selected_or_near = sum(owned and not selected_or_near[index] for index, owned in enumerate(mask))
        if outside_selected_or_near:
            raise RuntimeError(f"{view} owner mask admits {outside_selected_or_near} pixels outside the selected source object")
        masks[view] = mask
        component_maps[view] = component_map
        pixels = image.load()
        component_counts = {component: 0 for component in COMPONENTS}
        red_owned = 0
        for index, owned in enumerate(mask):
            if not owned:
                continue
            x = index % width
            y = index // width
            color = pixels[x, y]
            code = component_map[index]
            component = COMPONENTS[code - 1] if code else "C-004"
            component_counts[component] += 1
            if RED_PREDICATE(*color):
                red_owned += 1
            elif non_red(color):
                palette_inputs[component].append(color)
        mask_path = REPO_ROOT / MASK_REL / f"{ASSET_ID}_SOURCE_OWNED_MASK_{view.upper()}_A01.png"
        Image.frombytes("L", (width, height), bytes(255 if value else 0 for value in mask)).save(mask_path, format="PNG")
        mask_records.append(
            {
                "view": view,
                "source_path": str(panel_paths[view]),
                "source_size": [width, height],
                "paper_rgb": list(paper),
                "raw_red_predicate_pixels": raw_red_count,
                "central_object_bbox_inclusive_px": list(bbox),
                "source_object_selection": selection,
                "coverage_pixels": sum(coverage),
                "owned_mask_pixels": sum(mask),
                "owned_pixels_outside_selected_object_or_2px_fringe": outside_selected_or_near,
                "owned_red_pixels": red_owned,
                "component_owned_pixels": component_counts,
                "mask_path": str(mask_path.relative_to(REPO_ROOT)),
                "mask_sha256": sha256_file(mask_path),
                "manual_pixel_edits": 0,
            }
        )

    palettes = {component: weighted_kmedoids(colors) for component, colors in palette_inputs.items()}
    global_colors = [color for colors in palette_inputs.values() for color in colors]
    global_palette = weighted_kmedoids(global_colors)
    component_code = {component: index + 1 for index, component in enumerate(COMPONENTS)}

    hidden_index = 0
    polygons: List[List[Vec2]] = []
    for face in face_records:
        pixels, hidden_index = face_uv_pixels(face, bboxes, windows, hidden_index)
        face["uv_pixels_top_left"] = [[round(x, 9), round(y, 9)] for x, y in pixels]
        polygons.append(pixels)

    coverage_atlas = polygon_mask(polygons, ATLAS_SIZE, ATLAS_SIZE)
    dilation_atlas = dilate(coverage_atlas, ATLAS_SIZE, ATLAS_SIZE, 16)
    classification = bytearray(ATLAS_SIZE * ATLAS_SIZE)
    for index in range(len(classification)):
        if coverage_atlas[index]:
            classification[index] = 2
        elif dilation_atlas[index]:
            classification[index] = 3

    atlas = Image.new("RGB", (ATLAS_SIZE, ATLAS_SIZE))
    atlas_pixels = atlas.load()
    component_atlas = [0] * (ATLAS_SIZE * ATLAS_SIZE)
    for y in range(ATLAS_SIZE):
        for x in range(ATLAS_SIZE):
            atlas_pixels[x, y] = authored_color(global_palette, x, y, 0)

    for view in VIEWS:
        rect = windows[view]
        image = panel_images[view]
        pixels = image.load()
        width, height = image.size
        mask = masks[view]
        component_map = component_maps[view]
        for y in range(height):
            for x in range(width):
                atlas_x = rect[0] + x
                atlas_y = rect[1] + y
                atlas_index = atlas_y * ATLAS_SIZE + atlas_x
                code = component_map[y * width + x]
                if code:
                    component_atlas[atlas_index] = code
                palette = palettes[COMPONENTS[code - 1]] if code else global_palette
                atlas_pixels[atlas_x, atlas_y] = authored_color(palette, atlas_x, atlas_y, code)
                if mask[y * width + x]:
                    atlas_pixels[atlas_x, atlas_y] = pixels[x, y]
                    classification[atlas_index] = 1

    authored_faces = [face for face in face_records if face["owner"] == "authored"]
    authored_polygons = [face["uv_pixels_top_left"] for face in authored_faces]
    for face, polygon in zip(authored_faces, authored_polygons):
        code = component_code[face["component_id"]]
        face_mask = polygon_mask([[(float(x), float(y)) for x, y in polygon]], ATLAS_SIZE, ATLAS_SIZE)
        for index, value in enumerate(face_mask):
            if value:
                component_atlas[index] = code
                x = index % ATLAS_SIZE
                y = index // ATLAS_SIZE
                atlas_pixels[x, y] = authored_color(palettes[face["component_id"]], x, y, code)

    atlas.save(REPO_ROOT / BC_REL, format="PNG")
    Image.frombytes("L", (ATLAS_SIZE, ATLAS_SIZE), bytes(classification)).save(REPO_ROOT / CLASS_REL, format="PNG")

    luminance = Image.new("L", (ATLAS_SIZE, ATLAS_SIZE), 128)
    lum_pixels = luminance.load()
    red_atlas = bytearray(ATLAS_SIZE * ATLAS_SIZE)
    for y in range(ATLAS_SIZE):
        for x in range(ATLAS_SIZE):
            color = atlas_pixels[x, y]
            value = int(round(0.2126 * color[0] + 0.7152 * color[1] + 0.0722 * color[2]))
            lum_pixels[x, y] = value
            if classification[y * ATLAS_SIZE + x] == 1 and RED_PREDICATE(*color):
                red_atlas[y * ATLAS_SIZE + x] = 1
    height_image = luminance.filter(ImageFilter.GaussianBlur(radius=1.1))
    heights = height_image.load()
    normal = Image.new("RGB", (ATLAS_SIZE, ATLAS_SIZE), (128, 128, 255))
    normal_pixels = normal.load()
    for y in range(1, ATLAS_SIZE - 1):
        for x in range(1, ATLAS_SIZE - 1):
            index = y * ATLAS_SIZE + x
            if not dilation_atlas[index]:
                continue
            left = float(heights[x - 1, y])
            right = float(heights[x + 1, y])
            up = float(heights[x, y - 1])
            down = float(heights[x, y + 1])
            dx = (right - left) / 255.0 * 1.4
            dy = (down - up) / 255.0 * 1.4
            red_near = any(
                red_atlas[yy * ATLAS_SIZE + xx]
                for yy in range(max(0, y - 1), min(ATLAS_SIZE, y + 2))
                for xx in range(max(0, x - 1), min(ATLAS_SIZE, x + 2))
            )
            if red_near:
                center_red = red_atlas[index]
                dx += (float(red_atlas[index - 1]) - float(red_atlas[index + 1])) * 0.28
                dy += (float(red_atlas[index - ATLAS_SIZE]) - float(red_atlas[index + ATLAS_SIZE])) * 0.28
                if center_red:
                    dx *= 1.08
                    dy *= 1.08
            nx, ny, nz = -dx, dy, 1.0
            length = math.sqrt(nx * nx + ny * ny + nz * nz)
            normal_pixels[x, y] = (
                int(round((nx / length * 0.5 + 0.5) * 255.0)),
                int(round((ny / length * 0.5 + 0.5) * 255.0)),
                int(round((nz / length * 0.5 + 0.5) * 255.0)),
            )
    normal.save(REPO_ROOT / NORMAL_REL, format="PNG")

    mask_manifest = {
        "schema": "aerathea.step15_source_mask_manifest.v1",
        "asset_id": ASSET_ID,
        "contract_id": CONTRACT_ID,
        "date": "2026-07-20",
        "status": "candidate_masks_generated_no_manual_edits",
        "artifact_classification": "candidate interpretation; not source evidence",
        "rule": base_plan["source_owned_mask_rule"],
        "records": mask_records,
        "palettes": {component: [list(color) for color in palette] for component, palette in palettes.items()},
        "global_fallback_palette": [list(color) for color in global_palette],
        "palette_algorithm": "weighted deterministic PAM over the 512 most frequent owned non-red source RGB triplets; seed 0; lexicographic tie break",
        "source_object_selection_rule": "largest 8-connected raw foreground-predicate component before any growth; minimum 8x dominance, 0.40 bbox density, central containment, and no border contact",
        "annotation_contamination_policy": "every owned pixel must remain within the selected raw object component or its two-pixel fringe; zero pixels outside required",
        "manual_pixel_edits": 0,
        "source_mutations": 0,
    }
    (REPO_ROOT / MASK_MANIFEST_REL).write_text(json.dumps(mask_manifest, indent=2) + "\n", encoding="utf-8")
    return {
        "face_records": face_records,
        "bboxes": {view: list(value) for view, value in bboxes.items()},
        "mask_records": mask_records,
        "palettes": mask_manifest["palettes"],
        "hidden_faces": hidden_index,
        "classification_counts": dict(Counter(classification)),
        "red_owned_atlas_pixels": sum(red_atlas),
        "component_atlas": component_atlas,
        "classification": classification,
        "red_atlas": red_atlas,
    }


def assign_uvs(bpy: Any, face_records: Sequence[Dict[str, Any]]) -> None:
    records_by_object: Dict[str, Dict[int, Dict[str, Any]]] = {name: {} for name in OBJECTS}
    for record in face_records:
        records_by_object[record["object_name"]][record["face_index"]] = record
    for object_name in OBJECTS:
        obj = bpy.data.objects[object_name]
        mesh = obj.data
        while mesh.uv_layers:
            mesh.uv_layers.remove(mesh.uv_layers[0])
        uv_layer = mesh.uv_layers.new(name="UVMap")
        owner_values: List[str] = []
        for polygon in mesh.polygons:
            record = records_by_object[object_name][polygon.index]
            pixels = record["uv_pixels_top_left"]
            if len(pixels) != len(polygon.loop_indices):
                raise RuntimeError(f"UV loop count mismatch: {object_name} face {polygon.index}")
            for loop_index, pixel in zip(polygon.loop_indices, pixels):
                u = float(pixel[0]) / ATLAS_SIZE
                v = 1.0 - float(pixel[1]) / ATLAS_SIZE
                uv_layer.data[loop_index].uv = (u, v)
            owner_values.append(record["owner"])
        obj["step15_face_owners"] = json.dumps(owner_values, separators=(",", ":"))
        obj["step15_uv_plan"] = "STEP_14_UV_OWNERSHIP_PLAN.json"


def configure_ao_bake(
    bpy: Any,
    classification: bytearray,
    face_records: Sequence[Dict[str, Any]],
) -> Dict[str, Any]:
    """Perform the Step 14-authorized equivalent audited ray bake.

    The approved Blender 3.0 Cycles texel bake exceeded the execution runtime
    ceiling after completing its first object. This equivalent path uses
    Blender's native BVH ray caster, 256 deterministic cosine-weighted
    hemisphere rays at every unchanged face-loop station, a 12 cm distance,
    and a 0.2 cm origin extrusion. Results are barycentrically interpolated
    over the already-assigned UV0 polygons.
    """
    from PIL import Image
    from mathutils import Vector  # type: ignore
    from mathutils.bvhtree import BVHTree  # type: ignore

    all_vertices: List[Vec3] = []
    all_faces: List[List[int]] = []
    for object_name in OBJECTS:
        obj = bpy.data.objects[object_name]
        offset = len(all_vertices)
        all_vertices.extend(tuple(float(value) for value in vertex.co) for vertex in obj.data.vertices)
        all_faces.extend([offset + int(index) for index in polygon.vertices] for polygon in obj.data.polygons)
    tree = BVHTree.FromPolygons(all_vertices, all_faces, all_triangles=False, epsilon=0.0)
    if tree is None:
        raise RuntimeError("Blender BVH construction failed")

    def radical_inverse(bits: int) -> float:
        bits = (bits << 16) | (bits >> 16)
        bits = ((bits & 0x55555555) << 1) | ((bits & 0xAAAAAAAA) >> 1)
        bits = ((bits & 0x33333333) << 2) | ((bits & 0xCCCCCCCC) >> 2)
        bits = ((bits & 0x0F0F0F0F) << 4) | ((bits & 0xF0F0F0F0) >> 4)
        bits = ((bits & 0x00FF00FF) << 8) | ((bits & 0xFF00FF00) >> 8)
        return bits * 2.3283064365386963e-10

    samples = 256
    distance = 12.0
    extrusion = 0.2
    ray_count = 0
    station_count = 0
    face_ao: Dict[Tuple[str, int], List[float]] = {}
    for face in face_records:
        normal = Vector(face_normal(face["vertices"]))
        tangent = normal.cross(Vector((0.0, 0.0, 1.0)))
        if tangent.length < 1.0e-8:
            tangent = normal.cross(Vector((0.0, 1.0, 0.0)))
        tangent.normalize()
        bitangent = normal.cross(tangent)
        bitangent.normalize()
        values: List[float] = []
        for point_tuple in face["vertices"]:
            point = Vector(point_tuple)
            origin = point + normal * extrusion
            hits = 0
            for sample_index in range(samples):
                u = (sample_index + 0.5) / samples
                v = radical_inverse(sample_index)
                radius = math.sqrt(u)
                phi = 2.0 * math.pi * v
                local_x = radius * math.cos(phi)
                local_y = radius * math.sin(phi)
                local_z = math.sqrt(max(0.0, 1.0 - u))
                direction = tangent * local_x + bitangent * local_y + normal * local_z
                location, _hit_normal, _face_index, hit_distance = tree.ray_cast(origin, direction, distance)
                if location is not None and hit_distance is not None and hit_distance <= distance:
                    hits += 1
            values.append(max(0.45, 1.0 - hits / samples))
            station_count += 1
            ray_count += samples
        face_ao[(face["object_name"], face["face_index"])] = values

    ao_values = bytearray([255]) * (ATLAS_SIZE * ATLAS_SIZE)
    rasterized_texels = bytearray(ATLAS_SIZE * ATLAS_SIZE)
    for face in face_records:
        pixels = [(float(value[0]), float(value[1])) for value in face["uv_pixels_top_left"]]
        values = face_ao[(face["object_name"], face["face_index"])]
        for index in range(1, len(pixels) - 1):
            points = (
                (pixels[0][0], pixels[0][1], values[0]),
                (pixels[index][0], pixels[index][1], values[index]),
                (pixels[index + 1][0], pixels[index + 1][1], values[index + 1]),
            )
            for x, y, value in triangle_pixels(points, ATLAS_SIZE, ATLAS_SIZE):
                atlas_index = y * ATLAS_SIZE + x
                ao_values[atlas_index] = max(115, min(255, int(round(value * 255.0))))
                rasterized_texels[atlas_index] = 1
    for atlas_index, value in enumerate(classification):
        if value not in (1, 2) or rasterized_texels[atlas_index]:
            continue
        x = atlas_index % ATLAS_SIZE
        y = atlas_index // ATLAS_SIZE
        neighbors = []
        for radius in (1, 2):
            for yy in range(max(0, y - radius), min(ATLAS_SIZE, y + radius + 1)):
                for xx in range(max(0, x - radius), min(ATLAS_SIZE, x + radius + 1)):
                    neighbor_index = yy * ATLAS_SIZE + xx
                    if rasterized_texels[neighbor_index]:
                        neighbors.append(ao_values[neighbor_index])
            if neighbors:
                break
        if neighbors:
            ao_values[atlas_index] = int(round(sum(neighbors) / len(neighbors)))
            rasterized_texels[atlas_index] = 1
    image = Image.frombytes("L", (ATLAS_SIZE, ATLAS_SIZE), bytes(ao_values)).convert("RGB")
    image.save(REPO_ROOT / AO_REL, format="PNG")
    target_misses = sum(1 for index, value in enumerate(classification) if value in (1, 2) and not rasterized_texels[index])
    if target_misses:
        raise RuntimeError(f"equivalent AO bake target raster misses: {target_misses}")
    return {
        "engine": "Blender BVHTree deterministic cosine-weighted hemisphere ray bake; Step 14 equivalently audited path",
        "samples": samples,
        "distance_cm": distance,
        "cage_extrusion_cm": extrusion,
        "margin_px": 16,
        "selected_to_active": False,
        "face_loop_stations": station_count,
        "rays_cast": ray_count,
        "target_raster_misses": target_misses,
        "path": str(AO_REL),
        "sha256": sha256_file(REPO_ROOT / AO_REL),
        "classified_texels": sum(1 for value in classification if value),
    }


def make_orm(classification: bytearray, red_atlas: bytearray) -> Dict[str, Any]:
    from PIL import Image

    ao_image = Image.open(REPO_ROOT / AO_REL).convert("RGB")
    ao_pixels = ao_image.load()
    orm = Image.new("RGB", (ATLAS_SIZE, ATLAS_SIZE), (255, 209, 0))
    orm_pixels = orm.load()
    ao_values: List[int] = []
    rough_values: List[int] = []
    for y in range(ATLAS_SIZE):
        for x in range(ATLAS_SIZE):
            index = y * ATLAS_SIZE + x
            if classification[index] == 0:
                ao = 255
                rough = int(round(0.82 * 255.0))
            else:
                ao = max(115, min(255, ao_pixels[x, y][0]))
                if red_atlas[index]:
                    ao = max(166, ao)
                    rough = int(round(0.64 * 255.0))
                else:
                    variation = ((x // 32) * 7 + (y // 32) * 11) % 33 - 16
                    rough = max(int(round(0.62 * 255.0)), min(int(round(0.90 * 255.0)), int(round(0.78 * 255.0)) + variation))
            orm_pixels[x, y] = (ao, rough, 0)
            ao_values.append(ao)
            rough_values.append(rough)
    orm.save(REPO_ROOT / ORM_REL, format="PNG")
    return {
        "ao_min": min(ao_values),
        "ao_max": max(ao_values),
        "roughness_min": min(rough_values),
        "roughness_max": max(rough_values),
        "metallic_unique": [0],
        "sha256": sha256_file(REPO_ROOT / ORM_REL),
    }


def create_material(bpy: Any) -> Any:
    material = bpy.data.materials.new("M_GIA_BloodAxeCairnstone_A005")
    material.use_nodes = True
    material.blend_method = "OPAQUE"
    material.use_backface_culling = True
    nodes = material.node_tree.nodes
    links = material.node_tree.links
    nodes.clear()
    output = nodes.new("ShaderNodeOutputMaterial")
    output.name = "A005_MATERIAL_OUTPUT"
    shader = nodes.new("ShaderNodeBsdfPrincipled")
    shader.name = "A005_DEFAULT_LIT"
    base = nodes.new("ShaderNodeTexImage")
    base.name = "T_GIA_BloodAxeCairnstone_A005_BC"
    base.image = bpy.data.images.load(str(REPO_ROOT / BC_REL), check_existing=False)
    base.image.colorspace_settings.name = "sRGB"
    normal_image = nodes.new("ShaderNodeTexImage")
    normal_image.name = "T_GIA_BloodAxeCairnstone_A005_N_DIRECTX"
    normal_image.image = bpy.data.images.load(str(REPO_ROOT / NORMAL_REL), check_existing=False)
    normal_image.image.colorspace_settings.name = "Linear"
    separate_normal = nodes.new("ShaderNodeSeparateRGB")
    invert_green = nodes.new("ShaderNodeMath")
    invert_green.operation = "SUBTRACT"
    invert_green.inputs[0].default_value = 1.0
    combine_normal = nodes.new("ShaderNodeCombineRGB")
    normal_map = nodes.new("ShaderNodeNormalMap")
    normal_map.space = "TANGENT"
    orm = nodes.new("ShaderNodeTexImage")
    orm.name = "T_GIA_BloodAxeCairnstone_A005_ORM"
    orm.image = bpy.data.images.load(str(REPO_ROOT / ORM_REL), check_existing=False)
    orm.image.colorspace_settings.name = "Linear"
    separate_orm = nodes.new("ShaderNodeSeparateRGB")
    links.new(base.outputs["Color"], shader.inputs["Base Color"])
    links.new(normal_image.outputs["Color"], separate_normal.inputs["Image"])
    links.new(separate_normal.outputs["R"], combine_normal.inputs["R"])
    links.new(separate_normal.outputs["G"], invert_green.inputs[1])
    links.new(invert_green.outputs[0], combine_normal.inputs["G"])
    links.new(separate_normal.outputs["B"], combine_normal.inputs["B"])
    links.new(combine_normal.outputs["Image"], normal_map.inputs["Color"])
    links.new(normal_map.outputs["Normal"], shader.inputs["Normal"])
    links.new(orm.outputs["Color"], separate_orm.inputs["Image"])
    links.new(separate_orm.outputs["G"], shader.inputs["Roughness"])
    links.new(separate_orm.outputs["B"], shader.inputs["Metallic"])
    shader.inputs["Emission"].default_value = (0.0, 0.0, 0.0, 1.0)
    shader.inputs["Emission Strength"].default_value = 0.0
    links.new(shader.outputs["BSDF"], output.inputs["Surface"])
    material["aerathea_shading_model"] = "Default Lit"
    material["aerathea_two_sided"] = False
    material["aerathea_emissive_enabled"] = False
    material["aerathea_orm_packing"] = "R=AO G=Roughness B=Metallic"
    for object_name in OBJECTS:
        obj = bpy.data.objects[object_name]
        obj.data.materials.clear()
        obj.data.materials.append(material)
    return material


def geometry_signature(bpy: Any) -> Dict[str, Any]:
    objects: List[Dict[str, Any]] = []
    totals = Counter()
    for name in OBJECTS:
        obj = bpy.data.objects[name]
        mesh = obj.data
        vertices = [[round(float(value), 9) for value in vertex.co] for vertex in mesh.vertices]
        faces = [list(polygon.vertices) for polygon in mesh.polygons]
        triangles = sum(max(1, len(face) - 2) for face in faces)
        totals.update(vertices=len(vertices), faces=len(faces), triangles=triangles)
        objects.append(
            {
                "object_name": name,
                "vertices": vertices,
                "faces": faces,
                "location": [round(float(value), 9) for value in obj.location],
                "rotation_euler": [round(float(value), 9) for value in obj.rotation_euler],
                "scale": [round(float(value), 9) for value in obj.scale],
            }
        )
    payload = json.dumps(objects, sort_keys=True, separators=(",", ":")).encode("utf-8")
    return {"sha256": hashlib.sha256(payload).hexdigest(), "objects": objects, "totals": dict(totals)}


def build_candidate() -> Dict[str, Any]:
    import bpy  # type: ignore

    lock, lock_results = verify_input_lock()
    pixel_results = verify_source_pixels(lock)
    source_hash_before = sha256_file(REPO_ROOT / SOURCE_BLEND_REL)
    if Path(bpy.data.filepath).resolve() != (REPO_ROOT / SOURCE_BLEND_REL).resolve():
        raise RuntimeError("builder must open the approved source candidate")
    geometry = load_json(GEOMETRY_MANIFEST_REL)
    uv_plan = load_json(UV_PLAN_REL)
    base_plan = load_json(BASE_PLAN_REL)
    material_plan = load_json(MATERIAL_PLAN_REL)
    delivery_plan = load_json(DELIVERY_PLAN_REL)
    before_signature = geometry_signature(bpy)
    face_records = build_face_records(geometry)
    for rel in (DCC_REL, TEXTURE_REL, MASK_REL, TECH_REL):
        (REPO_ROOT / rel).mkdir(parents=True, exist_ok=True)
    build_data = build_maps_and_uv(face_records, source_panels(), uv_plan, base_plan)
    assign_uvs(bpy, build_data["face_records"])
    ao_record = configure_ao_bake(
        bpy,
        build_data["classification"],
        build_data["face_records"],
    )
    orm_record = make_orm(build_data["classification"], build_data["red_atlas"])
    material = create_material(bpy)
    after_signature = geometry_signature(bpy)
    if after_signature != before_signature:
        raise RuntimeError("geometry changed during Step 15 build")
    scene = bpy.context.scene
    scene["aerathea_asset_id"] = ASSET_ID
    scene["aerathea_contract_id"] = CONTRACT_ID
    scene["artifact_classification"] = "candidate"
    scene["pipeline_status"] = "DCC source candidate"
    scene["dcc_game_ready"] = False
    scene["fully_game_ready"] = False
    scene["visual_canon"] = False
    scene["step15_geometry_changes"] = 0
    scene["step15_uv1_created"] = False
    scene["step15_emissive_created"] = False
    scene["step15_material_name"] = material.name
    scene.render.image_settings.file_format = "PNG"
    candidate_path = REPO_ROOT / CANDIDATE_BLEND_REL
    bpy.ops.wm.save_as_mainfile(filepath=str(candidate_path), check_existing=False)
    source_hash_after = sha256_file(REPO_ROOT / SOURCE_BLEND_REL)
    if source_hash_after != source_hash_before:
        raise RuntimeError("approved source candidate changed during Step 15 build")
    output_hashes = {
        "candidate_blend": sha256_file(candidate_path),
        "base_color": sha256_file(REPO_ROOT / BC_REL),
        "normal": sha256_file(REPO_ROOT / NORMAL_REL),
        "orm": sha256_file(REPO_ROOT / ORM_REL),
        "classification": sha256_file(REPO_ROOT / CLASS_REL),
        "ao_bake": sha256_file(REPO_ROOT / AO_REL),
        "mask_manifest": sha256_file(REPO_ROOT / MASK_MANIFEST_REL),
    }
    for record in build_data["mask_records"]:
        output_hashes[f"mask_{record['view']}"] = record["mask_sha256"]
    manifest = {
        "schema": "aerathea.step15_uv_texture_material_candidate_manifest.v1",
        "asset_id": ASSET_ID,
        "contract_id": CONTRACT_ID,
        "date": "2026-07-20",
        "status": "candidate_pending_independent_step15_audit",
        "artifact_classification": "candidate",
        "pipeline_status": "DCC source candidate",
        "source_candidate": {"path": str(SOURCE_BLEND_REL), "sha256_before": source_hash_before, "sha256_after": source_hash_after},
        "candidate_blend": {"path": str(CANDIDATE_BLEND_REL), "sha256": output_hashes["candidate_blend"]},
        "geometry": {"changes": 0, "signature": before_signature, "evaluated_triangles": 784},
        "uv0": {
            "name": "UVMap",
            "layers": 1,
            "faces_assigned": len(face_records),
            "source_windows": uv_plan["uv0"]["source_windows_half_open_px"],
            "authored_zone": uv_plan["uv0"]["authored_zone_half_open_px"],
            "hidden_face_islands": build_data["hidden_faces"],
            "minimum_dilation_px": 16,
            "minimum_window_gap_px": 32,
            "perspective_owns_texels": False,
        },
        "uv1": {"created": False, "deferred_to_step16": True},
        "masks": build_data["mask_records"],
        "texel_classification": {
            "path": str(CLASS_REL),
            "codes": {"0": "unused", "1": "exact source-owned mip-0 RGB", "2": "authored continuation", "3": "island dilation"},
            "counts": build_data["classification_counts"],
            "exactness_claim_limited_to_code": 1,
        },
        "maps": {
            "base_color": {"path": str(BC_REL), "resolution": [2048, 2048], "color_space": "sRGB", "bit_depth": 8, "added_ao": False, "color_grade": False},
            "normal": {"path": str(NORMAL_REL), "resolution": [2048, 2048], "color_space": "linear", "space": "tangent-space DirectX/Unreal", "displacement": False},
            "orm": {"path": str(ORM_REL), "resolution": [2048, 2048], "color_space": "linear", "packing": {"R": "Ambient Occlusion", "G": "Roughness", "B": "Metallic"}, **orm_record},
            "emissive": None,
        },
        "ao_bake": ao_record,
        "material": {
            "name": "M_GIA_BloodAxeCairnstone_A005",
            "slot_count": 1,
            "shared_across_objects": 4,
            "shading_model": "Default Lit",
            "blend_mode": "Opaque",
            "two_sided": False,
            "emissive_enabled": False,
            "emissive_texture": None,
            "base_color_ao_multiplication": False,
            "directx_green_preview_inverted_only_in_blender_nodes": True,
        },
        "mip_filter_policy": delivery_plan["mip_policy"] | {"filter_policy": delivery_plan["filter_policy"]},
        "decoration": {
            "semantic_ids": ["C-005", "C-006", "C-007"],
            "shared_consumer_mask": "RED_APPEARANCE_UNION",
            "owned_red_pixels": build_data["red_owned_atlas_pixels"],
            "hidden_copy": False,
            "cross_face_copy": False,
            "emissive": False,
        },
        "palettes": build_data["palettes"],
        "input_lock": {"path": str(INPUT_LOCK_REL), "verified": len(lock_results), "source_pixels_verified": len(pixel_results)},
        "output_hashes": output_hashes,
        "forbidden_outputs": {"geometry_changes": 0, "uv1": 0, "lod": 0, "collision": 0, "fbx": 0, "unreal": 0, "visual_canon": 0},
    }
    (REPO_ROOT / CANDIDATE_MANIFEST_REL).write_text(json.dumps(manifest, indent=2) + "\n", encoding="utf-8")
    manifest["candidate_manifest_sha256"] = sha256_file(REPO_ROOT / CANDIDATE_MANIFEST_REL)
    return manifest


def main() -> int:
    args = parse_args(blender_script_args())
    if args.schema_only:
        print(json.dumps(schema_report(), indent=2))
        return 0
    report = build_candidate()
    print(json.dumps({
        "status": report["status"],
        "candidate": report["candidate_blend"],
        "geometry_changes": report["geometry"]["changes"],
        "faces_assigned": report["uv0"]["faces_assigned"],
        "masks": len(report["masks"]),
        "maps": 3,
        "material_slots": report["material"]["slot_count"],
        "emissive": report["material"]["emissive_enabled"],
    }, indent=2))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
