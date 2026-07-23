#!/usr/bin/env python3
"""Independent source replay for Siege Breaker A12 R7 Step 01."""

from __future__ import annotations

from collections import deque
from fractions import Fraction
import hashlib
import json
import math
from pathlib import Path

from PIL import Image


ROOT = Path(__file__).resolve().parents[2]
ASSET = ROOT / "docs/assets/blueprints/SM_DRW_SiegeBreaker_Hammer_A01"
MANIFEST = ASSET / "manifests/A12_R7_STEP01_COMPONENT_REGISTRATION_A01.json"
AUDIT = ASSET / "manifests/A12_R7_STEP01_COMPONENT_REGISTRATION_A01_INDEPENDENT_AUDIT.json"
REVIEW = ASSET / "review/A12_R7_STEP01_COMPONENT_REGISTRATION_A01_REVIEW.md"
SOURCES = {
    "front": ROOT / "SourceAssets/Concepts/SiegeBreaker/siege_breaker_front_view.png",
    "back": ROOT / "SourceAssets/Concepts/SiegeBreaker/siege_breaker_back_view.png",
    "left": ROOT / "SourceAssets/Concepts/SiegeBreaker/siege_breaker_left_view.png",
    "right": ROOT / "SourceAssets/Concepts/SiegeBreaker/siege_breaker_right_view.png",
    "top": ROOT / "SourceAssets/Concepts/SiegeBreaker/siege_breaker_true_axial_top_view.png",
    "bottom": ROOT / "SourceAssets/Concepts/SiegeBreaker/siege_breaker_true_axial_bottom_view.png",
}
HASHES = {
    "front": "d00bf9ffcfd4862884626fa961c5f6b4fd6cedfdff7936b2210ca2a905e57e95",
    "back": "15b4633f2df4ee06115ef4a7e238f287ebece1bae514ad4005c1036a57359799",
    "left": "1a23e0c24f7be4b12df93e2509b9d300acc9161a21a32b336f7cf63c1288d91b",
    "right": "04a1e9359d518b1dec35fe161020bd23ab9e2f8d5934f24e4184aecaa91d8330",
    "top": "aee612d9bed74e4f861576f926fe9d75de00f80dc416e3a6ba66a75247c00e98",
    "bottom": "874a9e7c7713c7edbcf1030486d3988a54e8499ee697e316ec82a013fdb9d746",
}
RECTS = {
    "front": [317, 193, 808, 1304],
    "back": [285, 193, 818, 1344],
    "left": [397, 190, 612, 1299],
    "right": [467, 172, 681, 1270],
    "top": [94, 330, 1106, 921],
    "bottom": [93, 330, 1106, 933],
}
COUNTS = {"front": 212765, "back": 238342, "left": 118540, "right": 116948, "top": 465117, "bottom": 509030}


def sha(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest()


def luma(pixel: tuple[int, int, int]) -> int:
    return (77 * pixel[0] + 150 * pixel[1] + 29 * pixel[2]) >> 8


def membership(path: Path) -> tuple[bytearray, dict[str, object]]:
    image = Image.open(path).convert("RGB")
    width, height = image.size
    pixels = image.load()
    corners = []
    for ys in (range(2, 34), range(height - 34, height - 2)):
        for xs in (range(2, 34), range(width - 34, width - 2)):
            for y in ys:
                for x in xs:
                    corners.append(luma(pixels[x, y]))
    corners.sort()
    mid = len(corners) // 2
    threshold_twice = corners[mid - 1] + corners[mid] - 40
    eligible = bytearray(width * height)
    for y in range(height):
        for x in range(width):
            if 2 * luma(pixels[x, y]) <= threshold_twice:
                eligible[y * width + x] = 1
    seen = bytearray(width * height)
    candidates = []
    for seed in range(width * height):
        if seen[seed] or not eligible[seed]:
            continue
        queue = deque([seed])
        seen[seed] = 1
        component = []
        edge = False
        while queue:
            current = queue.popleft()
            component.append(current)
            y, x = divmod(current, width)
            edge = edge or x <= 1 or y <= 1 or x >= width - 2 or y >= height - 2
            for ny in range(max(0, y - 1), min(height, y + 2)):
                for nx in range(max(0, x - 1), min(width, x + 2)):
                    neighbor = ny * width + nx
                    if eligible[neighbor] and not seen[neighbor]:
                        seen[neighbor] = 1
                        queue.append(neighbor)
        if not edge:
            candidates.append(component)
    selected = max(candidates, key=len)
    result = bytearray(width * height)
    xs, ys = [], []
    for offset in selected:
        result[offset] = 1
        y, x = divmod(offset, width)
        xs.append(x)
        ys.append(y)
    return result, {
        "count": len(selected),
        "rect": [min(xs), min(ys), max(xs) + 1, max(ys) + 1],
        "width": width,
    }


def runs(selected: bytearray, width: int, row: int, x0: int, x1: int) -> list[list[int]]:
    values = [x for x in range(x0, x1) if selected[row * width + x]]
    result = []
    if not values:
        return result
    start = previous = values[0]
    for x in values[1:]:
        if x != previous + 1:
            result.append([start, previous + 1])
            start = x
        previous = x
    result.append([start, previous + 1])
    return result


def span(values: list[list[int]]) -> list[int]:
    return [min(value[0] for value in values), max(value[1] for value in values)]


def blue_components(path: Path, box: tuple[int, int, int, int]) -> list[dict[str, object]]:
    image = Image.open(path).convert("RGB")
    eligible = set()
    for y in range(box[1], box[3]):
        for x in range(box[0], box[2]):
            r, g, b = image.getpixel((x, y))
            if b >= 90 and b - max(r, g) >= 24:
                eligible.add((x, y))
    result = []
    while eligible:
        seed = eligible.pop()
        queue = deque([seed])
        points = [seed]
        while queue:
            x, y = queue.popleft()
            for dx, dy in ((-1, 0), (1, 0), (0, -1), (0, 1), (-1, -1), (1, -1), (-1, 1), (1, 1)):
                point = (x + dx, y + dy)
                if point in eligible:
                    eligible.remove(point)
                    queue.append(point)
                    points.append(point)
        xs = [p[0] for p in points]
        ys = [p[1] for p in points]
        result.append({"count": len(points), "rect": [min(xs), min(ys), max(xs) + 1, max(ys) + 1]})
    return sorted(result, key=lambda item: int(item["count"]), reverse=True)


def main() -> None:
    manifest = json.loads(MANIFEST.read_text(encoding="utf-8"))
    gates = []

    def check(name: str, condition: bool, evidence: object) -> None:
        gates.append({"name": name, "pass": bool(condition), "evidence": evidence})

    selected = {}
    meta = {}
    for view, path in SOURCES.items():
        selected[view], meta[view] = membership(path)
        check(f"{view}_hash", sha(path) == HASHES[view] == manifest["sources"][view]["file_sha256"], sha(path))
        check(f"{view}_rect", meta[view]["rect"] == RECTS[view] == manifest["sources"][view]["object_rectangle_half_open"], meta[view]["rect"])
        check(f"{view}_count", meta[view]["count"] == COUNTS[view] == manifest["sources"][view]["selected_component_pixel_count"], meta[view]["count"])

    front_top = runs(selected["front"], meta["front"]["width"], 220, 317, 808)
    front_bottom = runs(selected["front"], meta["front"]["width"], 520, 317, 808)
    expected_top = {"stone_left": [345, 459], "center_core_or_cap": [539, 587], "stone_right": [666, 780]}
    expected_bottom = {"stone_left": [337, 476], "center_core_or_cap": [512, 614], "stone_right": [648, 788]}
    observed_top = {
        "stone_left": span([value for value in front_top if value[1] <= 500]),
        "center_core_or_cap": span([value for value in front_top if value[0] >= 500 and value[1] <= 640]),
        "stone_right": span([value for value in front_top if value[0] >= 640]),
    }
    observed_bottom = {
        "stone_left": span([value for value in front_bottom if value[1] <= 500]),
        "center_core_or_cap": span([value for value in front_bottom if value[0] >= 500 and value[1] <= 640]),
        "stone_right": span([value for value in front_bottom if value[0] >= 640]),
    }
    check("front_top_component_spans", observed_top == expected_top, observed_top)
    check("front_bottom_component_spans", observed_bottom == expected_bottom, observed_bottom)
    pitch = manifest["strike_mass_width_and_inward_pitch_evidence"]
    left_shift = Fraction(sum(expected_bottom["stone_left"]), 2) - Fraction(sum(expected_top["stone_left"]), 2)
    right_shift = Fraction(sum(expected_top["stone_right"]), 2) - Fraction(sum(expected_bottom["stone_right"]), 2)
    check("bilateral_inward_center_shift", left_shift == Fraction(9, 2) and right_shift == 5, [float(left_shift), float(right_shift)])
    check("mean_pitch", abs(pitch["mean_pitch_angle_degrees_from_uniform_front_pixels"] - math.degrees(math.atan(float(Fraction(19, 4 * 300))))) < 1e-12, pitch["mean_pitch_angle_degrees_from_uniform_front_pixels"])

    back_row = runs(selected["back"], meta["back"]["width"], 540, 285, 818)
    check("back_negative_space_station", back_row == [[304, 466], [500, 606], [638, 800]], back_row)
    gaps = manifest["upper_haft_cap_negative_space"]
    check("front_negative_gaps", [gaps["front"]["left_gap_width_pixels"], gaps["front"]["right_gap_width_pixels"]] == [36, 34], gaps["front"])
    check("back_negative_gaps", [gaps["back"]["left_gap_width_pixels"], gaps["back"]["right_gap_width_pixels"]] == [34, 32], gaps["back"])

    for view, box, motif_rect in (
        ("right", (430, 140, 720, 520), [525, 311, 570, 407]),
        ("left", (360, 150, 660, 540), [450, 319, 496, 411]),
    ):
        components = blue_components(SOURCES[view], box)
        check(f"{view}_motif_component", components[0]["rect"] == motif_rect == manifest["strike_face_centerline_evidence"][view]["emissive_motif_rectangle_half_open"], components[0])
        check(f"{view}_face_not_shaft", manifest["strike_face_centerline_evidence"][view]["face_centerline_is_shaft_axis"] is False, manifest["strike_face_centerline_evidence"][view]["face_centerline_candidate_band_x_pixels_exact"])

    check("component_ledger_exact_ids", [row["id"] for row in manifest["component_ledger"]] == [
        "C01_CENTER_CORE", "C02_STONE_LEFT", "C03_STONE_RIGHT", "C04_STRIKE_FACE_HALF_POSITIVE_X",
        "C05_STRIKE_FACE_HALF_NEGATIVE_X", "C06_UPPER_HAFT_CAP", "C07_HAFT", "C08_GRIP",
        "C09_LOWER_COLLAR", "C10_POMMEL_BODY", "C11_POMMEL_TERMINAL_CAP", "C12_UPPER_HEAD_CAP_SPIRE",
    ], [row["id"] for row in manifest["component_ledger"]])
    check("five_blocks_preserved", len(manifest["blocked_unknowns"]) == 5, manifest["blocked_unknowns"])
    firewall = manifest["evidence_interpretation_firewall"]
    check("no_interpretation_outputs", all(firewall[key] == 0 for key in ("saved_masks", "filled_component_shapes", "connected_contours", "smoothed_envelopes", "hidden_closures", "candidate_geometry", "blender_files")), firewall)
    check("step02_and_dcc_false", manifest["production_authority"] == {"step_02": False, "dcc": False, "unreal": False, "fully_game_ready": False}, manifest["production_authority"])
    for name, record in manifest["outputs"].items():
        path = ROOT / record["path"]
        check(f"output_{name}_hash", path.is_file() and sha(path) == record["file_sha256"], record)
    review_text = REVIEW.read_text(encoding="utf-8")
    check("review_firewall", "No candidate shape, fill, or geometry" in review_text and "Step 02 and Blender remain unauthorized" in review_text, str(REVIEW.relative_to(ROOT)))
    check("manifest_technical_gates", manifest["technical_result"] == "pass" and all(row["pass"] for row in manifest["technical_gates"]), manifest["technical_gates"])

    result = {
        "schema": "aerathea.siegebreaker.a12_r7_step01_component_registration_independent_audit.v1",
        "asset": "SM_DRW_SiegeBreaker_Hammer_A01",
        "contract_id": manifest["contract_id"],
        "artifact_status": "proof only; technical audit cannot approve measurement interpretation or unblock Step 02",
        "gate_summary": {"passed": sum(1 for gate in gates if gate["pass"]), "total": len(gates), "result": "pass" if all(gate["pass"] for gate in gates) else "fail"},
        "gates": gates,
        "decision_boundary": "Flamestrike must approve or revise the measurement record and resolve its blocked rules. No audit grants geometry authority.",
    }
    AUDIT.write_text(json.dumps(result, indent=2) + "\n", encoding="utf-8")
    print(json.dumps(result["gate_summary"], indent=2))
    if result["gate_summary"]["result"] != "pass":
        raise SystemExit(1)


if __name__ == "__main__":
    main()
