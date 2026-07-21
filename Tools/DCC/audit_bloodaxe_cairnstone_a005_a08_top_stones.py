#!/usr/bin/env python3
"""Measure source-visible A08 top-view stone cores without creating geometry."""

from __future__ import annotations

import hashlib
import json
import math
from pathlib import Path
from typing import Dict, Iterable, List, Sequence, Set, Tuple

from PIL import Image, ImageDraw, ImageFont


ROOT = Path(__file__).resolve().parents[2]
ASSET = "SM_GIA_BloodAxeCairnstone_A005"
TOP_REL = Path("docs/assets/blueprints") / ASSET / "panels/STEP_03/SM_GIA_BloodAxeCairnstone_A005_STEP_03_TOP.png"
A06_REL = Path("docs/assets/blueprints") / ASSET / "manifests/VISUAL_CORRECTION_A06_EXTERIOR_EDGE_AUDIT.json"
OUT_REL = Path("docs/assets/blueprints") / ASSET / "manifests/VISUAL_CORRECTION_A08_TOP_STONE_MEASUREMENT.json"
BOARD_REL = Path("docs/assets/blueprints") / ASSET / "evidence/VISUAL_CORRECTION_A08/SM_GIA_BloodAxeCairnstone_A005_A08_TOP_STONE_MEASUREMENT.png"
EXPECTED_TOP_SHA256 = "1bc9750b903a3d9e5689bee3c2c1c7094ccd554c361ff622aa9065d2c5287fdf"

Point = Tuple[int, int]


def sha256_file(path: Path) -> str:
    digest = hashlib.sha256()
    with path.open("rb") as handle:
        for block in iter(lambda: handle.read(1024 * 1024), b""):
            digest.update(block)
    return digest.hexdigest()


def connected(mask: Set[Point], width: int, height: int, minimum_area: int) -> List[List[Point]]:
    seen: Set[Point] = set()
    components: List[List[Point]] = []
    for start in sorted(mask, key=lambda item: (item[1], item[0])):
        if start in seen:
            continue
        pending = [start]
        seen.add(start)
        component: List[Point] = []
        while pending:
            x_value, y_value = pending.pop()
            component.append((x_value, y_value))
            for dx, dy in ((1, 0), (-1, 0), (0, 1), (0, -1)):
                neighbor = (x_value + dx, y_value + dy)
                if 0 <= neighbor[0] < width and 0 <= neighbor[1] < height and neighbor in mask and neighbor not in seen:
                    seen.add(neighbor)
                    pending.append(neighbor)
        if len(component) >= minimum_area:
            components.append(component)
    return components


def measure_course(image: Image.Image, inner_rho: float, outer_rho: float, area_cutoff: int) -> List[Dict[str, float]]:
    width, height = image.size
    pixels = image.load()
    center_x, center_y = 136.0, 145.0
    radius_x, radius_y = 104.0, 114.5
    neutral: Set[Point] = set()
    for y_value in range(height):
        for x_value in range(width):
            red, green, blue = pixels[x_value, y_value]
            rho = math.sqrt(((x_value - center_x) / radius_x) ** 2 + ((y_value - center_y) / radius_y) ** 2)
            is_neutral_stone = max(red, green, blue) < 225 and red - min(green, blue) < 28 and max(red, green, blue) > 18
            if inner_rho <= rho <= outer_rho and is_neutral_stone:
                neutral.add((x_value, y_value))
    eroded = {
        point
        for point in neutral
        if all((point[0] + dx, point[1] + dy) in neutral for dx, dy in ((0, 0), (1, 0), (-1, 0), (0, 1), (0, -1)))
    }
    components = connected(eroded, width, height, 12)
    records: List[Dict[str, float]] = []
    for component in components:
        if len(component) < area_cutoff:
            continue
        centroid_x = sum(point[0] for point in component) / len(component)
        centroid_y = sum(point[1] for point in component) / len(component)
        angle = (math.degrees(math.atan2((centroid_y - center_y) / radius_y, (centroid_x - center_x) / radius_x)) + 360.0) % 360.0
        records.append(
            {
                "source_core_area_px": len(component),
                "centroid_px": [round(centroid_x, 3), round(centroid_y, 3)],
                "construction_datum_angle_deg": round(angle, 6),
            }
        )
    records.sort(key=lambda item: item["construction_datum_angle_deg"])
    for index, record in enumerate(records, start=1):
        record["stone_id"] = f"S{index:02d}"
    return records


def angular_spacings(records: Sequence[Dict[str, float]]) -> List[float]:
    angles = [float(record["construction_datum_angle_deg"]) for record in records]
    return [round((angles[(index + 1) % len(angles)] - angle) % 360.0, 6) for index, angle in enumerate(angles)]


def make_board(image: Image.Image, courses: Dict[str, Sequence[Dict[str, float]]], output: Path) -> None:
    scale = 3
    source = image.resize((image.width * scale, image.height * scale), Image.NEAREST)
    board = Image.new("RGB", (source.width + 760, source.height), (24, 27, 30))
    board.paste(source, (0, 0))
    draw = ImageDraw.Draw(board)
    font = ImageFont.load_default()
    colors = {"C002": (0, 255, 255), "C003": (255, 211, 64)}
    for course_id, records in courses.items():
        color = colors[course_id]
        for index, record in enumerate(records, start=1):
            x_value, y_value = record["centroid_px"]
            point = (round(x_value * scale), round(y_value * scale))
            radius = 5
            draw.ellipse((point[0] - radius, point[1] - radius, point[0] + radius, point[1] + radius), outline=color, width=2)
            draw.text((point[0] + 7, point[1] - 5), str(index), fill=color, font=font)
    text_x = source.width + 24
    lines = [
        "A005 A08 TOP STONE MEASUREMENT",
        "MEASUREMENT ONLY - NO CANDIDATE FILLS",
        "",
        "C002 source-visible neutral cores: 19",
        "C003 source-visible neutral cores: 24",
        "C004 exact rubble count: BLOCKED",
        "C004 reason: occlusion + merged silhouettes",
        "",
        "Cyan marks: exact C002 source-core centroids",
        "Gold marks: exact C003 source-core centroids",
        "Numbers follow construction-datum angle order.",
        "Marks do not claim closed contours or hidden edges.",
        "",
        "Authoritative outer extents:",
        "C002 123.846154 x 92.707424 cm",
        "C003 137.307692 x 105.196507 cm",
        "C004 140.000000 x 110.000000 cm",
        "",
        "A08 bounded C004 rule: 32 independent rubble stones",
        "Source-exact C004 count claim: false",
    ]
    for line_index, line in enumerate(lines):
        draw.text((text_x, 28 + line_index * 24), line, fill=(235, 238, 240), font=font)
    output.parent.mkdir(parents=True, exist_ok=True)
    board.save(output)


def main() -> int:
    top_path = ROOT / TOP_REL
    if sha256_file(top_path) != EXPECTED_TOP_SHA256:
        raise RuntimeError("authoritative top panel hash mismatch")
    image = Image.open(top_path).convert("RGB")
    c002 = measure_course(image, 0.73, 0.92, 180)
    c003 = measure_course(image, 0.91, 1.05, 64)
    if len(c002) != 19 or len(c003) != 24:
        raise RuntimeError(f"stone-count gate failed: C002={len(c002)} C003={len(c003)}")
    a06 = json.loads((ROOT / A06_REL).read_text(encoding="utf-8"))
    report = {
        "schema": "aerathea.visual_correction_a08_top_stone_measurement.v1",
        "asset_id": ASSET,
        "contract_id": "A005-CR-VISUAL-CORRECTION-A08",
        "date": "2026-07-21",
        "status": "pass_authoritative_measurement_gate",
        "artifact_classification": "authoritative measurement record",
        "source": {"path": str(TOP_REL), "sha256": EXPECTED_TOP_SHA256, "size_px": list(image.size)},
        "method": {
            "description": "Exact RGB neutral-core scan in declared top-panel annuli, one-pixel cross erosion, four-connected components, declared area cutoffs, and centroid recording.",
            "construction_datum_px": [136.0, 145.0],
            "datum_claim": "calculation datum only; not a claimed source physical center",
            "candidate_fill_created": False,
            "geometry_created": False,
            "hidden_edge_inference": False,
        },
        "courses": {
            "C002": {"count": len(c002), "count_status": "source-visible separable core count", "records": c002, "angular_center_spacings_deg": angular_spacings(c002)},
            "C003": {"count": len(c003), "count_status": "source-visible separable core count", "records": c003, "angular_center_spacings_deg": angular_spacings(c003)},
            "C004": {"count": None, "count_status": "blocked", "reason": "Peripheral rubble occlusion, small merged silhouettes, and shadow prevent an exact source-visible stone count without interpretation."},
        },
        "outer_extents_cm": {
            "C002": [123.846154, 92.707424],
            "C003": [137.307692, 105.196507],
            "C004": [140.0, 110.0],
            "authority": str(A06_REL),
            "a06_status": a06["status"],
        },
        "inner_radial_limits": {
            "status": "visible discrete contacts retained; exact closed inner perimeters remain blocked",
            "construction_rule": "derive hidden inner stone edges only from exact A04 C001 containment and adjacent-course clearance; no source-exact closure claim",
        },
        "vertical_construction_rule_cm": {
            "C004": [0.0, 9.0],
            "C003": [9.75, 22.25],
            "C002": [23.0, 34.25],
            "minimum_intercourse_clearance": 0.75,
            "source_exact_height_claim": False,
        },
        "uv_orientation_requirements": {
            "per_stone_island": True,
            "top_faces": "source-top projection with preserved angular order",
            "outer_and_inner_side_faces": "local tangential U and physical-height V",
            "end_faces": "local radial U and physical-height V",
            "maximum_uv_aspect_ratio": 6.0,
            "vertical_smear_allowed": False,
        },
        "bounded_interpretation_after_gate": {
            "C004_count": 32,
            "authority": "Flamestrike full correction authority plus approved Step 11 32-sector C004 sampling",
            "source_exact_count_claim": False,
            "C002_C003_boundaries": "cyclic midpoints between adjacent measured neutral-core centroid angles",
            "boundary_claim": "construction-only; not source-owned closed contours",
        },
        "decision": "measurement gate passes; fresh A08 individual-stone geometry is authorized under the active contract",
        "unreal_authorized": False,
        "fully_game_ready": False,
    }
    output = ROOT / OUT_REL
    output.parent.mkdir(parents=True, exist_ok=True)
    output.write_text(json.dumps(report, indent=2) + "\n", encoding="utf-8")
    make_board(image, {"C002": c002, "C003": c003}, ROOT / BOARD_REL)
    print(json.dumps({"status": report["status"], "C002": len(c002), "C003": len(c003), "C004": "blocked", "manifest": str(OUT_REL), "board": str(BOARD_REL)}, indent=2))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
