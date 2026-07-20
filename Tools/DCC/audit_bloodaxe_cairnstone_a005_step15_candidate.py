#!/usr/bin/env python3
"""Independent A005 Step 15 candidate audit and proof packager.

Schema mode is read-only and imports no bpy. Blender modes audit the saved
candidate or render fixed material proofs without saving the candidate.
Packaging mode creates local proof-only comparisons after technical pass.
"""

from __future__ import annotations

import argparse
import hashlib
import json
import math
import subprocess
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
BC_REL = TEXTURE_REL / "T_GIA_BloodAxeCairnstone_A005_BC.png"
NORMAL_REL = TEXTURE_REL / "T_GIA_BloodAxeCairnstone_A005_N.png"
ORM_REL = TEXTURE_REL / "T_GIA_BloodAxeCairnstone_A005_ORM.png"
CLASS_REL = TECH_REL / f"{ASSET_ID}_TEXEL_CLASSIFICATION_A01.png"
AO_REL = TECH_REL / f"{ASSET_ID}_AO_BAKE_A01.png"
MASK_MANIFEST_REL = TECH_REL / f"{ASSET_ID}_SOURCE_MASK_MANIFEST_A01.json"

PROOF_REL = Path("Saved/Automation/DCC") / ASSET_ID / "Production/Step15"
PREPROOF_AUDIT_REL = PROOF_REL / "STEP_15_PREPROOF_TECHNICAL_AUDIT.json"
MASK_PREFLIGHT_AUDIT_REL = PROOF_REL / "STEP_15_NATIVE_MASK_PREFLIGHT_AUDIT.json"
RENDER_AUDIT_REL = PROOF_REL / "STEP_15_FIXED_CAMERA_MATERIAL_RENDER_AUDIT.json"
REVIEW_AUDIT_REL = PROOF_REL / "STEP_15_REVIEW_PACKAGE_AUDIT.json"
FINAL_AUDIT_REL = PROOF_REL / "STEP_15_FINAL_18_GATE_AUDIT.json"
BOARD_REL = PROOF_REL / f"{ASSET_ID}_STEP15_UV_TEXTURE_MATERIAL_CANDIDATE_REVIEW_BOARD.png"

VIEWS = ("front", "back", "left", "right", "top", "perspective")
OWNERS = VIEWS[:5]
OBJECTS = ("C004_APRON", "C003_LOWER_TIER", "C002_UPPER_TIER", "C001_BODY")
COMPONENTS = ("C-001", "C-002", "C-003", "C-004")
ATLAS_SIZE = 2048
APPROVED_SOURCE_HASH = "5b4af2275a70e2598e72361382fc7ea6ea318724ac928d71b2c200c768a93095"

RAW_RENDER_RELS = {view: PROOF_REL / f"{ASSET_ID}_STEP15_{view.upper()}_MATERIAL.png" for view in VIEWS}
MASK_COMPARE_RELS = {view: PROOF_REL / f"{ASSET_ID}_STEP15_{view.upper()}_MASK_NATIVE_COMPARE.png" for view in OWNERS}
MATERIAL_COMPARE_RELS = {view: PROOF_REL / f"{ASSET_ID}_STEP15_{view.upper()}_MATERIAL_NATIVE_COMPARE.png" for view in VIEWS}

Vec2 = Tuple[float, float]
Vec3 = Tuple[float, float, float]


def parse_args(argv: Sequence[str]) -> argparse.Namespace:
    parser = argparse.ArgumentParser(description=__doc__)
    modes = parser.add_mutually_exclusive_group(required=True)
    modes.add_argument("--schema-only", action="store_true")
    modes.add_argument("--audit-dcc", action="store_true")
    modes.add_argument("--package-masks", action="store_true")
    modes.add_argument("--render-proofs", action="store_true")
    modes.add_argument("--package-review", action="store_true")
    modes.add_argument("--final", action="store_true")
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


def load_json(rel: Path) -> Dict[str, Any]:
    with (REPO_ROOT / rel).open("r", encoding="utf-8") as handle:
        return json.load(handle)


def validate_closed_world(value: str, label: str) -> None:
    for suffix in range(1, 5):
        legacy = f"SM_GIA_BloodAxeCairnstone_A{suffix:03d}"
        if legacy in value:
            raise RuntimeError(f"blocked legacy input in {label}: {legacy}")
    if "CoreRecovery" in value:
        raise RuntimeError(f"blocked quarantine input in {label}")


def verify_lock() -> Tuple[Dict[str, Any], List[Dict[str, Any]]]:
    lock = load_json(INPUT_LOCK_REL)
    if lock.get("asset_id") != ASSET_ID or lock.get("contract_id") != CONTRACT_ID or not lock.get("locked"):
        raise RuntimeError("Step 15 input-lock identity/state mismatch")
    results: List[Dict[str, Any]] = []
    for entry in lock["locked_inputs"]:
        validate_closed_world(entry["path"], "locked input")
        path = REPO_ROOT / entry["path"]
        actual = sha256_file(path) if path.is_file() and not path.is_symlink() else None
        results.append({"path": entry["path"], "expected": entry["sha256"], "actual": actual, "match": actual == entry["sha256"]})
    return lock, results


def panel_paths() -> Dict[str, Path]:
    manifest = load_json(PANEL_MANIFEST_REL)
    mapping = {entry["id"]: Path(entry["path"]) for entry in manifest["panels"]}
    return {view: mapping[view] for view in VIEWS}


def schema_report() -> Dict[str, Any]:
    lock, results = verify_lock()
    if not all(item["match"] for item in results):
        raise RuntimeError("locked-input mismatch")
    from PIL import Image

    pixel_results = []
    for view, rel in panel_paths().items():
        with Image.open(REPO_ROOT / rel) as image:
            actual = sha256_rgb(image)
        pixel_results.append({"view": view, "actual": actual, "expected": lock["source_pixel_hashes"][view], "match": actual == lock["source_pixel_hashes"][view]})
    if not all(item["match"] for item in pixel_results):
        raise RuntimeError("source RGB mismatch")
    return {
        "schema": "aerathea.step15_auditor_schema_preflight.v1",
        "asset_id": ASSET_ID,
        "contract_id": CONTRACT_ID,
        "status": "pass_schema_only_no_output",
        "bpy_imported": "bpy" in sys.modules,
        "filesystem_writes": 0,
        "locked_inputs_verified": len(results),
        "source_pixels_verified": len(pixel_results),
        "declared_gates": [entry["id"] for entry in load_json(DELIVERY_PLAN_REL)["step15_validation_gates"]],
    }


def gate(identifier: str, passed: bool | None, detail: Any) -> Dict[str, Any]:
    return {"id": identifier, "status": "pending" if passed is None else ("pass" if passed else "fail"), "detail": detail}


def face_normal(vertices: Sequence[Vec3]) -> Vec3:
    for index in range(1, len(vertices) - 1):
        a, b, c = vertices[0], vertices[index], vertices[index + 1]
        u = (b[0] - a[0], b[1] - a[1], b[2] - a[2])
        v = (c[0] - a[0], c[1] - a[1], c[2] - a[2])
        normal = (u[1] * v[2] - u[2] * v[1], u[2] * v[0] - u[0] * v[2], u[0] * v[1] - u[1] * v[0])
        length = math.sqrt(sum(value * value for value in normal))
        if length > 1.0e-12:
            return tuple(value / length for value in normal)  # type: ignore[return-value]
    raise RuntimeError("degenerate face")


def hidden_face(authority: str, vertices: Sequence[Vec3]) -> bool:
    if authority in {
        "VAG-005-C001-HIDDEN-BOTTOM",
        "VAG-007-C002-HIDDEN-CLOSURES",
        "VAG-009-C003-HIDDEN-CLOSURES",
        "VAG-013-C004-Z0-BOTTOM",
        "VAG-014-CL001-CL003-HIDDEN-OVERLAP",
    }:
        return True
    return authority == "VAG-012-C004-FINAL-FIRST-CLOSURE-FACE" and min(point[2] for point in vertices) >= 10.0 - 1.0e-7


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


def expected_face_owners(geometry: Dict[str, Any]) -> Dict[str, List[str]]:
    result: Dict[str, List[str]] = {}
    for obj in geometry["objects"]:
        vertices = [tuple(entry["coordinate_cm"]) for entry in obj["vertices"]]
        owners: List[str] = []
        for face in obj["faces"]:
            points = [vertices[index] for index in face["vertex_indices"]]
            owners.append("authored" if hidden_face(face["authority_group_id"], points) else normal_owner(face_normal(points)))
        result[obj["object_name"]] = owners
    return result


def geometry_audit(bpy: Any, geometry: Dict[str, Any]) -> Dict[str, Any]:
    expected = {entry["object_name"]: entry for entry in geometry["objects"]}
    records = []
    totals = Counter()
    exact = True
    tolerance = 1.0e-5
    for name in OBJECTS:
        obj = bpy.data.objects.get(name)
        if obj is None or obj.type != "MESH":
            exact = False
            records.append({"object_name": name, "match": False, "reason": "missing mesh"})
            continue
        manifest = expected[name]
        vertices = [[float(value) for value in vertex.co] for vertex in obj.data.vertices]
        expected_vertices = [entry["coordinate_cm"] for entry in manifest["vertices"]]
        vertex_match = len(vertices) == len(expected_vertices) and all(
            max(abs(actual[axis] - target[axis]) for axis in range(3)) <= tolerance
            for actual, target in zip(vertices, expected_vertices)
        )
        faces = [list(polygon.vertices) for polygon in obj.data.polygons]
        expected_faces = [entry["vertex_indices"] for entry in manifest["faces"]]
        face_match = faces == expected_faces
        transform_match = (
            max(abs(float(value)) for value in obj.location) <= tolerance
            and max(abs(float(value)) for value in obj.rotation_euler) <= tolerance
            and max(abs(float(value) - 1.0) for value in obj.scale) <= tolerance
        )
        triangles = sum(max(1, len(face) - 2) for face in faces)
        totals.update(vertices=len(vertices), faces=len(faces), triangles=triangles)
        match = vertex_match and face_match and transform_match
        exact = exact and match
        records.append({"object_name": name, "match": match, "vertex_match": vertex_match, "face_match": face_match, "transform_match": transform_match, "vertices": len(vertices), "faces": len(faces), "triangles": triangles})
    return {"match": exact and totals == Counter(vertices=400, faces=464, triangles=784), "totals": dict(totals), "records": records, "tolerance_cm": tolerance}


def polygon_area(polygon: Sequence[Vec2]) -> float:
    return 0.5 * sum(polygon[index][0] * polygon[(index + 1) % len(polygon)][1] - polygon[(index + 1) % len(polygon)][0] * polygon[index][1] for index in range(len(polygon)))


def line_intersection(a: Vec2, b: Vec2, c: Vec2, d: Vec2) -> Vec2:
    x1, y1 = a
    x2, y2 = b
    x3, y3 = c
    x4, y4 = d
    denominator = (x1 - x2) * (y3 - y4) - (y1 - y2) * (x3 - x4)
    if abs(denominator) < 1.0e-15:
        return b
    t = ((x1 - x3) * (y3 - y4) - (y1 - y3) * (x3 - x4)) / denominator
    return x1 + t * (x2 - x1), y1 + t * (y2 - y1)


def convex_intersection(subject: Sequence[Vec2], clip: Sequence[Vec2]) -> List[Vec2]:
    output = list(subject)
    orientation = 1.0 if polygon_area(clip) >= 0.0 else -1.0
    for index, c0 in enumerate(clip):
        c1 = clip[(index + 1) % len(clip)]
        source = output
        output = []
        if not source:
            break
        def inside(point: Vec2) -> bool:
            return orientation * ((c1[0] - c0[0]) * (point[1] - c0[1]) - (c1[1] - c0[1]) * (point[0] - c0[0])) >= -1.0e-9
        previous = source[-1]
        previous_inside = inside(previous)
        for current in source:
            current_inside = inside(current)
            if current_inside:
                if not previous_inside:
                    output.append(line_intersection(previous, current, c0, c1))
                output.append(current)
            elif previous_inside:
                output.append(line_intersection(previous, current, c0, c1))
            previous, previous_inside = current, current_inside
    return output


def bbox(polygon: Sequence[Vec2]) -> Tuple[float, float, float, float]:
    return min(x for x, _ in polygon), min(y for _, y in polygon), max(x for x, _ in polygon), max(y for _, y in polygon)


def bbox_overlap(a: Tuple[float, float, float, float], b: Tuple[float, float, float, float]) -> bool:
    return min(a[2], b[2]) > max(a[0], b[0]) and min(a[3], b[3]) > max(a[1], b[1])


def uv_audit(bpy: Any, geometry: Dict[str, Any], uv_plan: Dict[str, Any]) -> Dict[str, Any]:
    expected_owners = expected_face_owners(geometry)
    windows = {entry["view"]: entry["rect"] for entry in uv_plan["uv0"]["source_windows_half_open_px"]}
    zone = uv_plan["uv0"]["authored_zone_half_open_px"]
    polygons = []
    owner_match = True
    bounds_match = True
    face_count = 0
    layer_counts = {}
    for name in OBJECTS:
        obj = bpy.data.objects[name]
        mesh = obj.data
        layer_counts[name] = len(mesh.uv_layers)
        if len(mesh.uv_layers) != 1 or mesh.uv_layers[0].name != "UVMap":
            bounds_match = False
            continue
        stored = json.loads(obj.get("step15_face_owners", "[]"))
        owner_match = owner_match and stored == expected_owners[name]
        uv = mesh.uv_layers[0]
        for polygon in mesh.polygons:
            owner = expected_owners[name][polygon.index]
            points = [(float(uv.data[index].uv.x) * ATLAS_SIZE, (1.0 - float(uv.data[index].uv.y)) * ATLAS_SIZE) for index in polygon.loop_indices]
            rect = zone if owner == "authored" else windows[owner]
            inside = all(rect[0] - 1.0e-5 <= x <= rect[2] + 1.0e-5 and rect[1] - 1.0e-5 <= y <= rect[3] + 1.0e-5 for x, y in points)
            bounds_match = bounds_match and inside and all(-1.0e-6 <= x <= ATLAS_SIZE + 1.0e-6 and -1.0e-6 <= y <= ATLAS_SIZE + 1.0e-6 for x, y in points)
            polygons.append({"object_name": name, "face_index": polygon.index, "owner": owner, "points": points, "bbox": bbox(points), "area": abs(polygon_area(points))})
            face_count += 1
    overlaps = []
    for left_index in range(len(polygons)):
        left = polygons[left_index]
        for right_index in range(left_index + 1, len(polygons)):
            right = polygons[right_index]
            if not bbox_overlap(left["bbox"], right["bbox"]):
                continue
            clipped = convex_intersection(left["points"], right["points"])
            area = abs(polygon_area(clipped)) if len(clipped) >= 3 else 0.0
            if area > 1.0e-5:
                overlaps.append({"a": [left["object_name"], left["face_index"]], "b": [right["object_name"], right["face_index"]], "area_px2": area})
    return {
        "face_count": face_count,
        "all_faces_assigned_once": face_count == 464,
        "layer_counts": layer_counts,
        "uv0_only": all(value == 1 for value in layer_counts.values()),
        "owner_records_match": owner_match,
        "bounds_match": bounds_match,
        "positive_area_overlaps": overlaps[:100],
        "positive_area_overlap_count": len(overlaps),
        "polygons": polygons,
    }


def neighbors8(index: int, width: int, height: int) -> Iterable[int]:
    x, y = index % width, index // width
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
    result = bytearray(mask)
    frontier = bytearray(mask)
    for _ in range(radius):
        next_mask = bytearray(result)
        for index, value in enumerate(frontier):
            if value:
                for neighbor in neighbors8(index, width, height):
                    next_mask[neighbor] = 1
        frontier = bytearray(1 if next_mask[index] and not result[index] else 0 for index in range(width * height))
        result = next_mask
    return result


def connected_components(mask: bytearray, width: int, height: int) -> List[List[int]]:
    seen = bytearray(width * height)
    groups = []
    for start, value in enumerate(mask):
        if not value or seen[start]:
            continue
        seen[start] = 1
        queue: deque[int] = deque([start])
        group = []
        while queue:
            index = queue.popleft()
            group.append(index)
            for neighbor in neighbors8(index, width, height):
                if mask[neighbor] and not seen[neighbor]:
                    seen[neighbor] = 1
                    queue.append(neighbor)
        groups.append(group)
    return groups


def paper_seed(image: Any) -> bytearray:
    rgb = image.convert("RGB")
    width, height = rgb.size
    pixels = rgb.load()
    border = [pixels[x, y] for y in range(height) for x in range(width) if x < 8 or x >= width - 8 or y < 8 or y >= height - 8]
    paper = tuple(sorted(pixel[channel] for pixel in border)[len(border) // 2] for channel in range(3))
    seed = bytearray(width * height)
    for y in range(height):
        for x in range(width):
            r, g, b = pixels[x, y]
            red = r - max(g, b) >= 18 and r >= 50
            if max(abs((r, g, b)[channel] - paper[channel]) for channel in range(3)) >= 24 or red:
                seed[y * width + x] = 1
    return seed


def polygon_union_mask(polygons: Sequence[Sequence[Vec2]], width: int, height: int) -> bytearray:
    # Reproduce the declared depth-raster convention at integer pixel centers.
    # Pillow's inclusive polygon edges are intentionally not used because they
    # admit boundary pixels outside the half-open owner footprint.
    mask = bytearray(width * height)
    for polygon in polygons:
        for triangle_index in range(1, len(polygon) - 1):
            (x0, y0), (x1, y1), (x2, y2) = polygon[0], polygon[triangle_index], polygon[triangle_index + 1]
            area = (x1 - x0) * (y2 - y0) - (y1 - y0) * (x2 - x0)
            if abs(area) < 1.0e-12:
                continue
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
                        mask[y * width + x] = 1
    return mask


def apply_small_components(mask: bytearray, width: int, height: int) -> bytearray:
    groups = connected_components(mask, width, height)
    large = bytearray(width * height)
    for group in groups:
        if len(group) >= 64:
            for index in group:
                large[index] = 1
    near = dilate(large, width, height, 2)
    result = bytearray(width * height)
    for group in groups:
        if len(group) >= 4 or any(near[index] for index in group):
            for index in group:
                result[index] = 1
    return result


def independent_source_object_selection(seed: bytearray, width: int, height: int) -> Dict[str, Any]:
    groups = connected_components(seed, width, height)
    if not groups:
        return {"safe": False, "reason": "no foreground components"}
    center_x = 0.5 * (width - 1)
    ranked = []
    for group in groups:
        xs = [index % width for index in group]
        ys = [index // width for index in group]
        box = (min(xs), min(ys), max(xs), max(ys))
        ranked.append((len(group), -abs((box[0] + box[2]) * 0.5 - center_x), group, box))
    ranked.sort(key=lambda item: (item[0], item[1]), reverse=True)
    size, _, selected, box = ranked[0]
    second_size = ranked[1][0] if len(ranked) > 1 else 0
    box_width = box[2] - box[0] + 1
    box_height = box[3] - box[1] + 1
    dominance = float(size) / float(max(1, second_size))
    density = float(size) / float(box_width * box_height)
    center_offset_fraction = abs((box[0] + box[2]) * 0.5 - center_x) / float(width)
    safe = (
        dominance >= 8.0
        and density >= 0.40
        and center_offset_fraction <= 0.20
        and box_width >= int(math.floor(width * 0.35))
        and box_height >= int(math.floor(height * 0.50))
        and box[0] > 3
        and box[1] > 3
        and box[2] < width - 4
        and box[3] < height - 4
    )
    selected_mask = bytearray(width * height)
    for index in selected:
        selected_mask[index] = 1
    return {
        "safe": safe,
        "bbox": list(box),
        "selected_pixels": size,
        "second_largest_pixels": second_size,
        "dominance_ratio": dominance,
        "bbox_density": density,
        "horizontal_center_offset_fraction": center_offset_fraction,
        "selected_or_2px_fringe": dilate(selected_mask, width, height, 2),
    }


def masks_and_rgb_audit(uv: Dict[str, Any], uv_plan: Dict[str, Any]) -> Dict[str, Any]:
    from PIL import Image

    windows = {entry["view"]: entry["rect"] for entry in uv_plan["uv0"]["source_windows_half_open_px"]}
    base = Image.open(REPO_ROOT / BC_REL).convert("RGB")
    base_pixels = base.load()
    classification = Image.open(REPO_ROOT / CLASS_REL).convert("L")
    class_bytes = classification.tobytes()
    panel_map = panel_paths()
    records = []
    all_masks = True
    all_rgb = True
    all_annotation_safe = True
    owned_atlas = bytearray(ATLAS_SIZE * ATLAS_SIZE)
    for view in OWNERS:
        source = Image.open(REPO_ROOT / panel_map[view]).convert("RGB")
        width, height = source.size
        rect = windows[view]
        face_polygons = []
        for face in uv["polygons"]:
            if face["owner"] == view:
                face_polygons.append([(x - rect[0], y - rect[1]) for x, y in face["points"]])
        coverage = polygon_union_mask(face_polygons, width, height)
        seed = paper_seed(source)
        source_object = independent_source_object_selection(seed, width, height)
        grown = dilate(coverage, width, height, 1)
        expected = apply_small_components(bytearray(1 if seed[index] and grown[index] else 0 for index in range(width * height)), width, height)
        mask_path = REPO_ROOT / MASK_REL / f"{ASSET_ID}_SOURCE_OWNED_MASK_{view.upper()}_A01.png"
        actual = bytearray(1 if value else 0 for value in Image.open(mask_path).convert("L").tobytes())
        mask_match = actual == expected
        outside_selected_or_near = sum(
            owned and not source_object["selected_or_2px_fringe"][index]
            for index, owned in enumerate(actual)
        ) if source_object.get("safe") else sum(actual)
        manifest_record = next(entry for entry in load_json(MASK_MANIFEST_REL)["records"] if entry["view"] == view)
        annotation_safe = (
            source_object.get("safe") is True
            and manifest_record.get("central_object_bbox_inclusive_px") == source_object.get("bbox")
            and manifest_record.get("owned_pixels_outside_selected_object_or_2px_fringe") == 0
            and outside_selected_or_near == 0
        )
        rgb_mismatch = 0
        class_mismatch = 0
        source_pixels = source.load()
        for index, owned in enumerate(actual):
            if not owned:
                continue
            x, y = index % width, index // width
            atlas_x, atlas_y = rect[0] + x, rect[1] + y
            atlas_index = atlas_y * ATLAS_SIZE + atlas_x
            owned_atlas[atlas_index] = 1
            if base_pixels[atlas_x, atlas_y] != source_pixels[x, y]:
                rgb_mismatch += 1
            if class_bytes[atlas_index] != 1:
                class_mismatch += 1
        all_masks = all_masks and mask_match
        all_rgb = all_rgb and rgb_mismatch == 0 and class_mismatch == 0
        all_annotation_safe = all_annotation_safe and annotation_safe
        records.append({"view": view, "size": [width, height], "coverage_pixels": sum(coverage), "expected_mask_pixels": sum(expected), "actual_mask_pixels": sum(actual), "mask_match": mask_match, "annotation_safe": annotation_safe, "independent_source_object_bbox": source_object.get("bbox"), "dominance_ratio": source_object.get("dominance_ratio"), "bbox_density": source_object.get("bbox_density"), "owned_pixels_outside_selected_object_or_2px_fringe": outside_selected_or_near, "rgb_mismatch_pixels": rgb_mismatch, "classification_mismatch_pixels": class_mismatch, "mask_sha256": sha256_file(mask_path)})
    return {"masks_match": all_masks, "annotation_safe": all_annotation_safe, "rgb_exact": all_rgb, "records": records, "owned_atlas": owned_atlas, "classification": class_bytes}


def map_audit(mask_rgb: Dict[str, Any]) -> Dict[str, Any]:
    from PIL import Image

    base = Image.open(REPO_ROOT / BC_REL)
    normal = Image.open(REPO_ROOT / NORMAL_REL).convert("RGB")
    orm = Image.open(REPO_ROOT / ORM_REL).convert("RGB")
    ao = Image.open(REPO_ROOT / AO_REL).convert("RGB")
    classification = mask_rgb["classification"]
    owned = mask_rgb["owned_atlas"]
    class_counts = Counter(classification)
    valid_classes = set(class_counts).issubset({0, 1, 2, 3}) and class_counts[1] == sum(owned)
    authored_red = 0
    normal_length_min = 10.0
    normal_length_max = 0.0
    normal_negative_z = 0
    orm_pixels = orm.load()
    base_pixels = base.convert("RGB").load()
    normal_pixels = normal.load()
    ao_pixels = ao.load()
    metallic_nonzero = 0
    ao_out_of_range = 0
    rough_out_of_range = 0
    red_ao_low = 0
    for y in range(ATLAS_SIZE):
        for x in range(ATLAS_SIZE):
            index = y * ATLAS_SIZE + x
            r, g, b = base_pixels[x, y]
            if classification[index] != 1 and r - max(g, b) >= 18 and r >= 50:
                authored_red += 1
            nr, ng, nb = normal_pixels[x, y]
            vector = (nr / 255.0 * 2.0 - 1.0, ng / 255.0 * 2.0 - 1.0, nb / 255.0 * 2.0 - 1.0)
            length = math.sqrt(sum(value * value for value in vector))
            normal_length_min = min(normal_length_min, length)
            normal_length_max = max(normal_length_max, length)
            if vector[2] <= 0.0:
                normal_negative_z += 1
            ao_value, rough, metal = orm_pixels[x, y]
            if metal != 0:
                metallic_nonzero += 1
            if classification[index] and not (115 <= ao_value <= 255):
                ao_out_of_range += 1
            if not (140 <= rough <= 230):
                rough_out_of_range += 1
            if classification[index] == 1 and r - max(g, b) >= 18 and r >= 50 and ao_value < 166:
                red_ao_low += 1
    alpha_opaque = base.mode != "RGBA" or min(base.getchannel("A").getextrema()) == 255
    return {
        "base": {"size": list(base.size), "mode": base.mode, "alpha_opaque": alpha_opaque, "sha256": sha256_file(REPO_ROOT / BC_REL)},
        "normal": {"size": list(normal.size), "mode": normal.mode, "length_min": normal_length_min, "length_max": normal_length_max, "negative_z_pixels": normal_negative_z, "sha256": sha256_file(REPO_ROOT / NORMAL_REL)},
        "orm": {"size": list(orm.size), "mode": orm.mode, "metallic_nonzero": metallic_nonzero, "ao_out_of_range": ao_out_of_range, "roughness_out_of_range": rough_out_of_range, "red_ao_low": red_ao_low, "sha256": sha256_file(REPO_ROOT / ORM_REL)},
        "ao": {"size": list(ao.size), "mode": ao.mode, "sha256": sha256_file(REPO_ROOT / AO_REL), "extrema": ao.getextrema()},
        "classification": {"size": [ATLAS_SIZE, ATLAS_SIZE], "counts": dict(class_counts), "valid": valid_classes, "sha256": sha256_file(REPO_ROOT / CLASS_REL)},
        "authored_red_pixels": authored_red,
    }


def material_audit(bpy: Any) -> Dict[str, Any]:
    slot_counts = {}
    material_ids = []
    for name in OBJECTS:
        obj = bpy.data.objects[name]
        slot_counts[name] = len(obj.data.materials)
        if obj.data.materials:
            material_ids.append(obj.data.materials[0].as_pointer())
    material = bpy.data.materials.get("M_GIA_BloodAxeCairnstone_A005")
    if material is None or not material.use_nodes:
        return {"match": False, "reason": "material missing", "slot_counts": slot_counts}
    nodes = material.node_tree.nodes
    links = material.node_tree.links
    image_names = sorted(node.name for node in nodes if node.type == "TEX_IMAGE")
    emissive_links = [link for link in links if "Emission" in link.to_socket.name]
    emission_nodes = [node for node in nodes if node.type == "EMISSION"]
    displacement_links = [link for link in links if link.to_socket.name == "Displacement"]
    normal_green_inversion = any(node.type == "MATH" and node.operation == "SUBTRACT" for node in nodes)
    shared = len(material_ids) == 4 and len(set(material_ids)) == 1
    match = (
        shared
        and all(value == 1 for value in slot_counts.values())
        and material.blend_method == "OPAQUE"
        and material.use_backface_culling
        and image_names == ["T_GIA_BloodAxeCairnstone_A005_BC", "T_GIA_BloodAxeCairnstone_A005_N_DIRECTX", "T_GIA_BloodAxeCairnstone_A005_ORM"]
        and not emissive_links
        and not emission_nodes
        and not displacement_links
        and normal_green_inversion
        and not material.get("aerathea_emissive_enabled", True)
    )
    return {"match": match, "slot_counts": slot_counts, "shared_material": shared, "blend_method": material.blend_method, "two_sided": not material.use_backface_culling, "image_nodes": image_names, "emissive_links": len(emissive_links), "emission_nodes": len(emission_nodes), "displacement_links": len(displacement_links), "directx_preview_green_inversion": normal_green_inversion}


def changed_path_firewall(candidate_manifest: Dict[str, Any]) -> Dict[str, Any]:
    text = json.dumps(candidate_manifest, sort_keys=True)
    closed_world = not any(f"SM_GIA_BloodAxeCairnstone_A{suffix:03d}" in text for suffix in range(1, 5)) and "CoreRecovery" not in text
    result = subprocess.run(["git", "status", "--porcelain"], cwd=REPO_ROOT, check=True, capture_output=True, text=True)
    paths = []
    for line in result.stdout.splitlines():
        path = line[3:]
        if " -> " in path:
            path = path.split(" -> ", 1)[1]
        paths.append(path)
    scoped = [path for path in paths if ASSET_ID in path or "a005_step15" in path.lower()]
    allowed_prefixes = (
        str(A005_REL) + "/",
        str(DCC_REL) + "/",
        str(TEXTURE_REL) + "/",
    )
    allowed_exact = {
        "Tools/DCC/build_bloodaxe_cairnstone_a005_step15_candidate.py",
        "Tools/DCC/audit_bloodaxe_cairnstone_a005_step15_candidate.py",
    }
    unexpected = [path for path in scoped if path not in allowed_exact and not path.startswith(allowed_prefixes)]
    return {"match": closed_world and not unexpected, "candidate_inputs_closed_world": closed_world, "scoped_changed_paths": scoped, "unexpected_scoped_paths": unexpected, "unrelated_paths_preserved": len(paths) - len(scoped)}


def run_technical_audit(final: bool) -> Dict[str, Any]:
    import bpy  # type: ignore

    lock, lock_results = verify_lock()
    geometry = load_json(GEOMETRY_MANIFEST_REL)
    uv_plan = load_json(UV_PLAN_REL)
    base_plan = load_json(BASE_PLAN_REL)
    material_plan = load_json(MATERIAL_PLAN_REL)
    delivery = load_json(DELIVERY_PLAN_REL)
    candidate_manifest = load_json(CANDIDATE_MANIFEST_REL)
    blend_path = REPO_ROOT / CANDIDATE_BLEND_REL
    blend_hash_before = sha256_file(blend_path)
    if Path(bpy.data.filepath).resolve() != blend_path.resolve():
        raise RuntimeError("auditor must open the Step 15 candidate")
    geometry_result = geometry_audit(bpy, geometry)
    uv_result = uv_audit(bpy, geometry, uv_plan)
    masks_rgb = masks_and_rgb_audit(uv_result, uv_plan)
    maps = map_audit(masks_rgb)
    material = material_audit(bpy)
    firewall = changed_path_firewall(candidate_manifest)
    window_pairs = []
    windows = uv_plan["uv0"]["source_windows_half_open_px"]
    for left_index in range(len(windows)):
        for right_index in range(left_index + 1, len(windows)):
            a, b = windows[left_index]["rect"], windows[right_index]["rect"]
            overlap_x = max(0, min(a[2], b[2]) - max(a[0], b[0]))
            overlap_y = max(0, min(a[3], b[3]) - max(a[1], b[1]))
            gap_x = max(0, max(a[0], b[0]) - min(a[2], b[2]))
            gap_y = max(0, max(a[1], b[1]) - min(a[3], b[3]))
            gap = max(gap_x, gap_y)
            window_pairs.append({"pair": [windows[left_index]["view"], windows[right_index]["view"]], "overlap_area": overlap_x * overlap_y, "gap_px": gap})
    mask_manifest = load_json(MASK_MANIFEST_REL)
    proof = load_json(REVIEW_AUDIT_REL) if final and (REPO_ROOT / REVIEW_AUDIT_REL).is_file() else None
    source_hash_now = sha256_file(REPO_ROOT / SOURCE_BLEND_REL)
    scene = bpy.context.scene
    classification_ok = (
        scene.get("artifact_classification") == "candidate"
        and scene.get("pipeline_status") == "DCC source candidate"
        and not scene.get("dcc_game_ready", True)
        and not scene.get("fully_game_ready", True)
        and not scene.get("visual_canon", True)
    )
    bake = candidate_manifest["ao_bake"]
    bake_ok = (
        bake["samples"] == 256
        and bake["distance_cm"] == 12.0
        and bake["cage_extrusion_cm"] == 0.2
        and bake["margin_px"] == 16
        and not bake["selected_to_active"]
        and bake["sha256"] == maps["ao"]["sha256"]
        and bake.get("target_raster_misses") == 0
        and bake.get("rays_cast", 0) == bake.get("face_loop_stations", 0) * 256
        and maps["orm"]["ao_out_of_range"] == 0
    )
    mip_ok = (
        candidate_manifest["mip_filter_policy"]["source_delivery"].startswith("lossless mip 0")
        and not candidate_manifest["mip_filter_policy"]["mip_exactness_claimed"]
        and candidate_manifest["mip_filter_policy"]["filter_policy"]["source_ingest"].startswith("nearest/point")
        and candidate_manifest["texel_classification"]["exactness_claim_limited_to_code"] == 1
    )
    gates = [
        gate("S15-G01-INPUTS", all(item["match"] for item in lock_results) and source_hash_now == APPROVED_SOURCE_HASH, {"locked": len(lock_results), "failed": [item["path"] for item in lock_results if not item["match"]], "source_candidate_sha256": source_hash_now}),
        gate("S15-G02-GEOMETRY", geometry_result["match"] and candidate_manifest["geometry"]["changes"] == 0, geometry_result),
        gate("S15-G03-UV0", uv_result["all_faces_assigned_once"] and uv_result["uv0_only"] and uv_result["owner_records_match"] and uv_result["bounds_match"] and uv_result["positive_area_overlap_count"] == 0, {key: value for key, value in uv_result.items() if key != "polygons"}),
        gate("S15-G04-UV1", uv_result["uv0_only"] and not candidate_manifest["uv1"]["created"], {"layer_counts": uv_result["layer_counts"], "candidate_manifest": candidate_manifest["uv1"]}),
        gate("S15-G05-WINDOWS", len(windows) == 5 and all(item["overlap_area"] == 0 and item["gap_px"] >= 32 for item in window_pairs), {"windows": windows, "pairs": window_pairs}),
        gate("S15-G06-MASKS", masks_rgb["masks_match"] and masks_rgb["annotation_safe"] and len(mask_manifest["records"]) == 5 and mask_manifest["manual_pixel_edits"] == 0, masks_rgb["records"]),
        gate("S15-G07-RGB", masks_rgb["rgb_exact"], masks_rgb["records"]),
        gate("S15-G08-AUTHORED", maps["classification"]["valid"] and maps["classification"]["counts"].get(1, 0) > 0 and set(maps["classification"]["counts"]).issubset({0, 1, 2, 3}), maps["classification"]),
        gate("S15-G09-DECORATION", maps["authored_red_pixels"] == 0 and candidate_manifest["decoration"]["semantic_ids"] == ["C-005", "C-006", "C-007"] and not candidate_manifest["decoration"]["hidden_copy"] and not candidate_manifest["decoration"]["cross_face_copy"] and not candidate_manifest["decoration"]["emissive"], {"authored_red_pixels": maps["authored_red_pixels"], "decoration": candidate_manifest["decoration"]}),
        gate("S15-G10-BC", maps["base"]["size"] == [2048, 2048] and maps["base"]["mode"] in ("RGB", "RGBA") and maps["base"]["alpha_opaque"] and not candidate_manifest["maps"]["base_color"]["added_ao"] and not candidate_manifest["maps"]["base_color"]["color_grade"], maps["base"]),
        gate("S15-G11-NORMAL", maps["normal"]["size"] == [2048, 2048] and maps["normal"]["negative_z_pixels"] == 0 and 0.95 <= maps["normal"]["length_min"] <= 1.05 and 0.95 <= maps["normal"]["length_max"] <= 1.05 and candidate_manifest["maps"]["normal"]["space"] == "tangent-space DirectX/Unreal" and not candidate_manifest["maps"]["normal"]["displacement"], maps["normal"]),
        gate("S15-G12-ORM", maps["orm"]["size"] == [2048, 2048] and maps["orm"]["metallic_nonzero"] == 0 and maps["orm"]["roughness_out_of_range"] == 0 and maps["orm"]["red_ao_low"] == 0, maps["orm"]),
        gate("S15-G13-BAKE", bake_ok, {"bake": bake, "ao": maps["ao"], "orm_ao_out_of_range": maps["orm"]["ao_out_of_range"]}),
        gate("S15-G14-MIPS", mip_ok, candidate_manifest["mip_filter_policy"]),
        gate("S15-G15-MATERIAL", material["match"] and not (REPO_ROOT / TEXTURE_REL / "T_GIA_BloodAxeCairnstone_A005_E.png").exists(), material),
        gate("S15-G16-RENDERS", None if not final else bool(proof and proof.get("status") == "pass_step15_review_package_complete" and proof.get("counts") == {"fixed_material_renders": 6, "native_mask_comparisons": 5, "native_material_comparisons": 6, "review_boards": 1}), proof if proof else "pending until technical pass"),
        gate("S15-G17-CLASSIFICATION", classification_ok, {"artifact_classification": scene.get("artifact_classification"), "pipeline_status": scene.get("pipeline_status"), "dcc_game_ready": scene.get("dcc_game_ready"), "fully_game_ready": scene.get("fully_game_ready"), "visual_canon": scene.get("visual_canon")}),
        gate("S15-G18-FIREWALL", firewall["match"] and all(value == 0 for value in candidate_manifest["forbidden_outputs"].values()), {"firewall": firewall, "forbidden_outputs": candidate_manifest["forbidden_outputs"]}),
    ]
    blend_hash_after = sha256_file(blend_path)
    if blend_hash_after != blend_hash_before:
        gates[1] = gate("S15-G02-GEOMETRY", False, {"reason": "candidate changed during audit", "before": blend_hash_before, "after": blend_hash_after})
    failures = [item["id"] for item in gates if item["status"] == "fail"]
    pending = [item["id"] for item in gates if item["status"] == "pending"]
    if final:
        status = "pass_step15_all_18_gates" if not failures and not pending else "blocked_step15_candidate_gate_failure"
    else:
        status = "pass_step15_preproof_17_gates_render_authorized" if not failures and pending == ["S15-G16-RENDERS"] else "blocked_step15_candidate_gate_failure"
    report = {
        "schema": "aerathea.step15_candidate_independent_audit.v1",
        "asset_id": ASSET_ID,
        "contract_id": CONTRACT_ID,
        "date": "2026-07-20",
        "mode": "final" if final else "preproof",
        "status": status,
        "artifact_classification": "proof only",
        "gates_total": 18,
        "gates_passed": sum(item["status"] == "pass" for item in gates),
        "gates_pending": pending,
        "failures": failures,
        "gates": gates,
        "candidate_blend_sha256": blend_hash_after,
        "source_candidate_sha256": source_hash_now,
        "geometry_changes": 0,
        "source_mutations": 0,
        "step16_outputs": 0,
    }
    output = REPO_ROOT / (FINAL_AUDIT_REL if final else PREPROOF_AUDIT_REL)
    output.parent.mkdir(parents=True, exist_ok=True)
    output.write_text(json.dumps(report, indent=2) + "\n", encoding="utf-8")
    return report


def look_at(camera: Any, target: Tuple[float, float, float], up_axis: str = "Y") -> None:
    from mathutils import Vector  # type: ignore

    direction = Vector(target) - camera.location
    camera.rotation_euler = direction.to_track_quat("-Z", "Y" if up_axis == "Y" else "X").to_euler()


def render_view(bpy: Any, view: str, output: Path) -> Dict[str, Any]:
    scene = bpy.context.scene
    data = bpy.data.cameras.new(f"STEP15_{view.upper()}_CAMERA_DATA")
    camera = bpy.data.objects.new(f"STEP15_{view.upper()}_CAMERA", data)
    scene.collection.objects.link(camera)
    scene.camera = camera
    target = (0.0, 0.0, 110.0)
    if view == "front":
        camera.location = (0.0, -400.0, 110.0); data.type = "ORTHO"; data.ortho_scale = 242.0; look_at(camera, target)
    elif view == "back":
        camera.location = (0.0, 400.0, 110.0); data.type = "ORTHO"; data.ortho_scale = 242.0; look_at(camera, target)
    elif view == "left":
        camera.location = (-400.0, 0.0, 110.0); data.type = "ORTHO"; data.ortho_scale = 242.0; look_at(camera, target)
    elif view == "right":
        camera.location = (400.0, 0.0, 110.0); data.type = "ORTHO"; data.ortho_scale = 242.0; look_at(camera, target)
    elif view == "top":
        camera.location = (0.0, 0.0, 400.0); data.type = "ORTHO"; data.ortho_scale = 190.0; look_at(camera, (0.0, 0.0, 0.0), up_axis="X")
    elif view == "perspective":
        camera.location = (300.0, -420.0, 270.0); data.type = "PERSP"; data.lens = 58.0; look_at(camera, (0.0, 0.0, 105.0))
    else:
        raise RuntimeError(view)
    scene.render.filepath = str(output)
    bpy.ops.render.render(write_still=True)
    record = {"view": view, "path": str(output.relative_to(REPO_ROOT)), "sha256": sha256_file(output), "projection": data.type, "ortho_scale_cm": float(data.ortho_scale) if data.type == "ORTHO" else None, "lens_mm": float(data.lens) if data.type == "PERSP" else None}
    bpy.data.objects.remove(camera, do_unlink=True)
    bpy.data.cameras.remove(data)
    return record


def render_proofs() -> Dict[str, Any]:
    import bpy  # type: ignore

    audit = load_json(PREPROOF_AUDIT_REL)
    if audit.get("status") != "pass_step15_preproof_17_gates_render_authorized" or audit.get("failures"):
        raise RuntimeError("preproof technical audit did not authorize material rendering")
    blend_path = REPO_ROOT / CANDIDATE_BLEND_REL
    blend_before = sha256_file(blend_path)
    source_before = {view: sha256_file(REPO_ROOT / rel) for view, rel in panel_paths().items()}
    scene = bpy.context.scene
    scene.render.engine = "BLENDER_EEVEE"
    scene.eevee.use_gtao = True
    scene.eevee.gtao_distance = 12.0
    scene.eevee.gtao_factor = 1.15
    scene.render.resolution_x = 900
    scene.render.resolution_y = 1100
    scene.render.resolution_percentage = 100
    scene.render.image_settings.file_format = "PNG"
    scene.render.film_transparent = False
    try:
        scene.view_settings.view_transform = "Standard"
        scene.view_settings.look = "Medium High Contrast"
        scene.view_settings.exposure = 0.5
        scene.view_settings.gamma = 1.0
    except TypeError:
        pass
    world = scene.world or bpy.data.worlds.new("STEP15_WORLD")
    scene.world = world
    world.use_nodes = True
    background = world.node_tree.nodes.get("Background")
    background.inputs["Color"].default_value = (0.025, 0.03, 0.04, 1.0)
    background.inputs["Strength"].default_value = 0.65
    for obj in list(scene.objects):
        if obj.type in {"LIGHT", "CAMERA"}:
            bpy.data.objects.remove(obj, do_unlink=True)
    # Scale-neutral sun sources keep the 220 Blender-unit asset legible.  The
    # Attempt 01 area lights were physically too weak for this scene scale and
    # made the proof board nearly black despite an otherwise valid material.
    lights = [
        ("STEP15_KEY", "SUN", (260.0, -300.0, 360.0), 2.8, 0.16),
        ("STEP15_FILL", "SUN", (-260.0, -120.0, 220.0), 1.35, 0.28),
        ("STEP15_RIM", "SUN", (60.0, 320.0, 330.0), 1.8, 0.20),
    ]
    for name, kind, location, energy, angle in lights:
        data = bpy.data.lights.new(name + "_DATA", type=kind)
        data.energy = energy
        data.angle = angle
        obj = bpy.data.objects.new(name, data)
        obj.location = location
        scene.collection.objects.link(obj)
        look_at(obj, (0.0, 0.0, 100.0))
    root = REPO_ROOT / PROOF_REL
    root.mkdir(parents=True, exist_ok=True)
    records = [render_view(bpy, view, REPO_ROOT / RAW_RENDER_RELS[view]) for view in VIEWS]
    blend_after = sha256_file(blend_path)
    source_after = {view: sha256_file(REPO_ROOT / rel) for view, rel in panel_paths().items()}
    report = {
        "schema": "aerathea.step15_fixed_camera_material_render_audit.v1",
        "asset_id": ASSET_ID,
        "contract_id": CONTRACT_ID,
        "date": "2026-07-20",
        "status": "pass_six_fixed_camera_material_renders" if len(records) == 6 and blend_after == blend_before and source_after == source_before else "blocked_fail_closed",
        "artifact_classification": "proof only",
        "records": records,
        "candidate_sha256_before": blend_before,
        "candidate_sha256_after": blend_after,
        "source_hashes_unchanged": source_after == source_before,
        "save_operations": 0,
        "geometry_changes": 0,
    }
    (REPO_ROOT / RENDER_AUDIT_REL).write_text(json.dumps(report, indent=2) + "\n", encoding="utf-8")
    return report


def font(size: int, bold: bool = False) -> Any:
    from PIL import ImageFont

    path = "/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf" if bold else "/usr/share/fonts/truetype/dejavu/DejaVuSans.ttf"
    return ImageFont.truetype(path, size=size) if Path(path).is_file() else ImageFont.load_default()


def render_bbox(image: Any) -> Tuple[int, int, int, int]:
    rgb = image.convert("RGB")
    pixels = rgb.load()
    corner_samples = [pixels[0, 0], pixels[rgb.width - 1, 0], pixels[0, rgb.height - 1], pixels[rgb.width - 1, rgb.height - 1]]
    background = tuple(sum(sample[channel] for sample in corner_samples) // 4 for channel in range(3))
    xs, ys = [], []
    for y in range(rgb.height):
        for x in range(rgb.width):
            color = pixels[x, y]
            if max(abs(color[channel] - background[channel]) for channel in range(3)) >= 18:
                xs.append(x); ys.append(y)
    return (min(xs), min(ys), max(xs), max(ys)) if xs else (0, 0, 0, 0)


def package_masks() -> Dict[str, Any]:
    from PIL import Image, ImageDraw

    preproof = load_json(PREPROOF_AUDIT_REL)
    if preproof.get("status") != "pass_step15_preproof_17_gates_render_authorized":
        raise RuntimeError("technical preproof audit did not pass")
    root = REPO_ROOT / PROOF_REL
    root.mkdir(parents=True, exist_ok=True)
    title = font(24, True)
    small = font(14, False)
    paths = panel_paths()
    mask_records = []
    for view in OWNERS:
        source = Image.open(REPO_ROOT / paths[view]).convert("RGBA")
        mask = Image.open(REPO_ROOT / MASK_REL / f"{ASSET_ID}_SOURCE_OWNED_MASK_{view.upper()}_A01.png").convert("L")
        overlay = source.copy()
        tint = Image.new("RGBA", source.size, (0, 225, 255, 118))
        overlay.alpha_composite(Image.composite(tint, Image.new("RGBA", source.size, (0, 0, 0, 0)), mask))
        header = 78
        footer = 42
        gutter = 20
        canvas = Image.new("RGBA", (source.width * 2 + gutter * 3, source.height + header + footer), (15, 18, 22, 255))
        draw = ImageDraw.Draw(canvas)
        draw.text((gutter, 14), f"STEP 15 {view.upper()} NATIVE SOURCE / DETERMINISTIC OWNER MASK", fill=(245, 245, 245), font=title)
        draw.text((gutter, 48), "Cyan = interpreted source-owned mask; source pixels remain unmodified and unresampled", fill=(170, 205, 220), font=small)
        canvas.alpha_composite(source, (gutter, header))
        canvas.alpha_composite(overlay, (source.width + gutter * 2, header))
        draw.text((gutter, canvas.height - 30), "LOCKED SOURCE (native pixels)", fill=(225, 230, 235), font=small)
        draw.text((source.width + gutter * 2, canvas.height - 30), "SOURCE + MASK OVERLAY (native pixels)", fill=(0, 225, 255), font=small)
        output = REPO_ROOT / MASK_COMPARE_RELS[view]
        canvas.convert("RGB").save(output, format="PNG")
        mask_records.append({"view": view, "path": str(MASK_COMPARE_RELS[view]), "sha256": sha256_file(output), "source_native_size": list(source.size), "mask_native_size": list(mask.size), "source_resampled": False, "manual_mask_edits": 0})
    report = {
        "schema": "aerathea.step15_native_mask_preflight_audit.v1",
        "asset_id": ASSET_ID,
        "contract_id": CONTRACT_ID,
        "date": "2026-07-20",
        "status": "pass_five_native_mask_comparisons_ready_for_internal_inspection" if len(mask_records) == 5 else "blocked_fail_closed",
        "artifact_classification": "proof only",
        "technical_preproof_status": preproof["status"],
        "counts": {"native_mask_comparisons": len(mask_records)},
        "mask_comparisons": mask_records,
        "source_resampling": 0,
        "manual_mask_edits": 0,
    }
    (REPO_ROOT / MASK_PREFLIGHT_AUDIT_REL).write_text(json.dumps(report, indent=2) + "\n", encoding="utf-8")
    return report


def package_review() -> Dict[str, Any]:
    from PIL import Image, ImageDraw

    render_audit = load_json(RENDER_AUDIT_REL)
    if render_audit.get("status") != "pass_six_fixed_camera_material_renders":
        raise RuntimeError("fixed-camera material renders did not pass")
    mask_preflight = package_masks()
    if mask_preflight.get("status") != "pass_five_native_mask_comparisons_ready_for_internal_inspection":
        raise RuntimeError("native mask preflight package did not pass")
    root = REPO_ROOT / PROOF_REL
    root.mkdir(parents=True, exist_ok=True)
    title = font(24, True)
    label = font(17, True)
    small = font(14, False)
    paths = panel_paths()
    mask_records = mask_preflight["mask_comparisons"]
    material_records = []
    for view in VIEWS:
        source = Image.open(REPO_ROOT / paths[view]).convert("RGBA")
        render = Image.open(REPO_ROOT / RAW_RENDER_RELS[view]).convert("RGBA")
        box = render_bbox(render)
        margins = {"left": box[0], "top": box[1], "right": render.width - 1 - box[2], "bottom": render.height - 1 - box[3]}
        header = 82
        footer = 48
        gutter = 20
        canvas = Image.new("RGBA", (source.width + render.width + gutter * 3, max(source.height, render.height) + header + footer), (15, 18, 22, 255))
        draw = ImageDraw.Draw(canvas)
        draw.text((gutter, 14), f"STEP 15 {view.upper()} SOURCE / FIXED-CAMERA MATERIAL CANDIDATE", fill=(245, 245, 245), font=title)
        draw.text((gutter, 49), "Source and render shown at native pixels; rendered pixels are interpretation, never an exactness claim", fill=(185, 195, 205), font=small)
        canvas.alpha_composite(source, (gutter, header))
        canvas.alpha_composite(render, (source.width + gutter * 2, header))
        draw.text((gutter, canvas.height - 33), "LOCKED SOURCE", fill=(225, 230, 235), font=small)
        draw.text((source.width + gutter * 2, canvas.height - 33), "CANDIDATE MATERIAL PROOF", fill=(100, 235, 160), font=small)
        output = REPO_ROOT / MATERIAL_COMPARE_RELS[view]
        canvas.convert("RGB").save(output, format="PNG")
        material_records.append({"view": view, "path": str(MATERIAL_COMPARE_RELS[view]), "sha256": sha256_file(output), "source_native_size": list(source.size), "render_native_size": list(render.size), "render_bbox_px": list(box), "render_margins_px": margins, "not_clipped": min(margins.values()) >= 8, "source_resampled": False, "render_resampled_for_evidence": False})
    thumb_w, thumb_h = 600, 520
    board = Image.new("RGB", (thumb_w * 3 + 80, thumb_h * 2 + 150), (12, 15, 19))
    draw = ImageDraw.Draw(board)
    draw.text((30, 18), f"{ASSET_ID} - STEP 15 UV / TEXTURE / MATERIAL CANDIDATE", fill=(245, 245, 245), font=title)
    draw.text((30, 54), "PRESENTATION THUMBNAILS ONLY - native mask and material comparisons remain the evidence", fill=(255, 205, 70), font=small)
    for index, record in enumerate(material_records):
        comparison = Image.open(REPO_ROOT / record["path"]).convert("RGB")
        comparison.thumbnail((thumb_w - 20, thumb_h - 55), Image.Resampling.LANCZOS if hasattr(Image, "Resampling") else Image.LANCZOS)
        x = 20 + (index % 3) * thumb_w
        y = 100 + (index // 3) * thumb_h
        board.paste(comparison, (x + (thumb_w - comparison.width) // 2, y + 34))
        draw.text((x + 8, y + 4), record["view"].upper(), fill=(225, 230, 235), font=label)
    draw.text((30, board.height - 34), "CANDIDATE ONLY - exact source RGB is limited to declared owned mip-0 texels; not DCC game-ready or visual canon", fill=(100, 235, 160), font=small)
    board_path = REPO_ROOT / BOARD_REL
    board.save(board_path, format="PNG")
    counts = {"fixed_material_renders": 6, "native_mask_comparisons": 5, "native_material_comparisons": 6, "review_boards": 1}
    pass_status = len(mask_records) == 5 and len(material_records) == 6 and all(record["not_clipped"] for record in material_records) and board_path.is_file()
    report = {
        "schema": "aerathea.step15_review_package_audit.v1",
        "asset_id": ASSET_ID,
        "contract_id": CONTRACT_ID,
        "date": "2026-07-20",
        "status": "pass_step15_review_package_complete" if pass_status else "blocked_fail_closed",
        "artifact_classification": "proof only",
        "counts": counts,
        "mask_comparisons": mask_records,
        "material_comparisons": material_records,
        "board": {"path": str(BOARD_REL), "sha256": sha256_file(board_path), "presentation_thumbnails_only": True},
        "source_mutations": 0,
        "candidate_mutations": 0,
        "manual_mask_edits": 0,
        "evidence_resampling": 0,
    }
    (REPO_ROOT / REVIEW_AUDIT_REL).write_text(json.dumps(report, indent=2) + "\n", encoding="utf-8")
    return report


def main() -> int:
    args = parse_args(blender_script_args())
    if args.schema_only:
        report = schema_report()
    elif args.audit_dcc:
        report = run_technical_audit(final=False)
    elif args.package_masks:
        report = package_masks()
    elif args.render_proofs:
        report = render_proofs()
    elif args.package_review:
        report = package_review()
    else:
        report = run_technical_audit(final=True)
    print(json.dumps({key: report[key] for key in report if key in {"schema", "asset_id", "contract_id", "mode", "status", "gates_total", "gates_passed", "gates_pending", "failures", "counts", "board"}}, indent=2))
    return 0 if not report.get("failures") and not str(report.get("status", "")).startswith("blocked") else 1


if __name__ == "__main__":
    raise SystemExit(main())
