#!/usr/bin/env python3
"""Independently audit the A11 Siege Breaker axial-source pixel record."""

from __future__ import annotations

import hashlib
import json
from collections import deque
from fractions import Fraction
from pathlib import Path

from PIL import Image


ROOT = Path(__file__).resolve().parents[2]
ASSET_ID = "SM_DRW_SiegeBreaker_Hammer_A01"
DOC_ROOT = ROOT / "docs/assets/blueprints" / ASSET_ID
MANIFEST = DOC_ROOT / "manifests/A11_TRUE_AXIAL_TOP_BOTTOM_PIXEL_MEASUREMENT.json"
AUDIT = DOC_ROOT / "manifests/A11_TRUE_AXIAL_TOP_BOTTOM_PIXEL_MEASUREMENT_INDEPENDENT_AUDIT.json"
A09_BLEND = (
    ROOT
    / "SourceAssets/Blender/Weapons/Dwarven"
    / ASSET_ID
    / "A09_PixelHalfMirror_VisualMatch_A01"
    / f"{ASSET_ID}_A09_PixelHalfMirror_VisualMatch_A01.blend"
)
A09_BLEND_SHA256 = "06ffb121d00cddb7b9e30a60067a5036a851d285f15daca3bffe3a663fd6d78f"


def sha256(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest()


def luma(r: int, g: int, b: int) -> int:
    return (77 * r + 150 * g + 29 * b) >> 8


def independent_component(image: Image.Image) -> tuple[list[int], int]:
    rgb_image = image.convert("RGB")
    width, height = rgb_image.size
    rgb = rgb_image.tobytes("raw", "RGB")
    values: list[int] = []
    for y_range in (range(2, 34), range(height - 34, height - 2)):
        for x_range in (range(2, 34), range(width - 34, width - 2)):
            for y in y_range:
                for x in x_range:
                    offset = (y * width + x) * 3
                    values.append(luma(rgb[offset], rgb[offset + 1], rgb[offset + 2]))
    values.sort()
    middle = len(values) // 2
    threshold_twice = values[middle - 1] + values[middle] - 40
    eligible = bytearray(width * height)
    for index in range(width * height):
        offset = index * 3
        eligible[index] = 2 * luma(rgb[offset], rgb[offset + 1], rgb[offset + 2]) <= threshold_twice

    visited = bytearray(width * height)
    candidates: list[tuple[int, int, int, int, int]] = []
    for seed in range(width * height):
        if visited[seed] or not eligible[seed]:
            continue
        queue = deque([seed])
        visited[seed] = 1
        count = 0
        x0, y0, x1, y1 = width, height, -1, -1
        touches_edge = False
        while queue:
            current = queue.popleft()
            y, x = divmod(current, width)
            count += 1
            x0, y0, x1, y1 = min(x0, x), min(y0, y), max(x1, x), max(y1, y)
            touches_edge = touches_edge or x == 0 or y == 0 or x == width - 1 or y == height - 1
            for ny in range(max(0, y - 1), min(height, y + 2)):
                for nx in range(max(0, x - 1), min(width, x + 2)):
                    neighbor = ny * width + nx
                    if neighbor != current and eligible[neighbor] and not visited[neighbor]:
                        visited[neighbor] = 1
                        queue.append(neighbor)
        if not touches_edge:
            candidates.append((count, x0, y0, x1 + 1, y1 + 1))
    candidates.sort(reverse=True)
    if not candidates or (len(candidates) > 1 and candidates[0][0] == candidates[1][0]):
        raise RuntimeError("independent component selection failed")
    count, x0, y0, x1, y1 = candidates[0]
    return [x0, y0, x1, y1], count


def fraction(record: dict[str, object]) -> Fraction:
    return Fraction(int(record["numerator"]), int(record["denominator"]))


def main() -> None:
    manifest = json.loads(MANIFEST.read_text(encoding="utf-8"))
    checks: list[dict[str, object]] = []

    def check(name: str, passed: bool, observed: object) -> None:
        checks.append({"check": name, "pass": bool(passed), "observed": observed})

    check("manifest_schema", manifest["schema"] == "aerathea.siegebreaker_true_axial_pixel_measurement.v2", manifest["schema"])
    check("pixel_rule", manifest["flamestrike_authority"]["measurement_rule"] == "use pixel measurements", manifest["flamestrike_authority"])
    check("printed_dimensions_not_geometry_authority", manifest["flamestrike_authority"]["printed_dimensions_control_geometry"] is False, manifest["flamestrike_authority"])

    for view in ("top", "bottom"):
        record = manifest["axial_sources"][view]
        path = ROOT / record["source_path"]
        image = Image.open(path)
        bbox, count = independent_component(image)
        check(f"{view}_file_hash", sha256(path) == record["file_sha256"], sha256(path))
        check(f"{view}_canvas", list(image.size) == record["canvas_pixels"], list(image.size))
        check(f"{view}_bbox", bbox == record["object_rectangle_half_open"], bbox)
        check(f"{view}_component_count", count == record["selection_metadata"]["selected_component_pixel_count"], count)
        width = bbox[2] - bbox[0]
        depth = bbox[3] - bbox[1]
        check(f"{view}_pixel_dimensions", [width, depth] == [record["object_width_pixels"], record["object_depth_pixels"]], [width, depth])
        derived_depth = Fraction(491 * 170, 1111) * Fraction(depth, width)
        recorded_depth = fraction(record["registration_using_existing_front_pixel_width"]["depth_cm_consequence_exact"])
        check(f"{view}_depth_formula", derived_depth == recorded_depth, str(derived_depth))

    approved = manifest["approved_reconciliation"]
    check("raw_conflict_preserved", manifest["cross_view_evidence"]["raw_evidence_verdict"] == "cross_view_depth_conflict", manifest["cross_view_evidence"])
    check("conflict_resolved", manifest["cross_view_evidence"]["resolution"] == "resolved by Flamestrike-approved centered-mean axial ownership rule", manifest["cross_view_evidence"])
    check("mean_width_pixels", fraction(approved["mean_width_pixels_exact"]) == Fraction(2025, 2), approved["mean_width_pixels_exact"])
    check("mean_depth_pixels", fraction(approved["mean_depth_pixels_exact"]) == Fraction(597), approved["mean_depth_pixels_exact"])
    check("common_scale", fraction(approved["common_cm_per_axial_pixel_exact"]) == Fraction(33388, 449955), approved["common_cm_per_axial_pixel_exact"])
    check("approved_depth", fraction(approved["approved_head_depth_cm_exact"]) == Fraction(6644212, 149985), approved["approved_head_depth_cm_exact"])
    check("axial_depth_authority", manifest["geometry_authority"]["head_footprint_scale"] is True, manifest["geometry_authority"])
    check("side_depth_superseded", manifest["geometry_authority"]["side_head_depth_scale"] is False, manifest["geometry_authority"])
    check("blender_unchanged_by_reconciliation", manifest["geometry_authority"]["blender_geometry_edit_executed"] is False, manifest["geometry_authority"])
    check("no_image_generation", manifest["software_boundary"]["image_generation_used"] is False, manifest["software_boundary"])
    check("a09_blend_unchanged", A09_BLEND.exists() and sha256(A09_BLEND) == A09_BLEND_SHA256, sha256(A09_BLEND) if A09_BLEND.exists() else "missing")

    passed = sum(1 for row in checks if row["pass"])
    result = {
        "schema": "aerathea.siegebreaker_true_axial_pixel_measurement_independent_audit.v2",
        "asset_id": ASSET_ID,
        "date": "2026-07-22",
        "artifact_status": "proof only",
        "manifest_path": str(MANIFEST.relative_to(ROOT)),
        "manifest_sha256": sha256(MANIFEST),
        "checks_passed": passed,
        "checks_total": len(checks),
        "verdict": "pass" if passed == len(checks) else "fail",
        "checks": checks,
    }
    AUDIT.write_text(json.dumps(result, indent=2) + "\n", encoding="utf-8")
    print(json.dumps({"verdict": result["verdict"], "passed": passed, "total": len(checks), "output": str(AUDIT.relative_to(ROOT))}, sort_keys=True))
    if result["verdict"] != "pass":
        raise SystemExit(1)


if __name__ == "__main__":
    main()
