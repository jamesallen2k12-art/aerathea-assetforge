#!/usr/bin/env python3
"""Independently audit the A005 A12 two-envelope measurement package."""

from __future__ import annotations

import hashlib
import json
from fractions import Fraction
from pathlib import Path

from PIL import Image


ROOT = Path(__file__).resolve().parents[2]
ASSET = ROOT / "docs/assets/blueprints/SM_GIA_BloodAxeCairnstone_A005"
MANIFEST = ASSET / "manifests/VISUAL_CORRECTION_A12_TWO_ENVELOPE_MEASUREMENT.json"
AUDIT = ASSET / "manifests/VISUAL_CORRECTION_A12_TWO_ENVELOPE_MEASUREMENT_VALIDATION.json"


def sha256(path: Path) -> str:
    digest = hashlib.sha256()
    with path.open("rb") as handle:
        for block in iter(lambda: handle.read(1024 * 1024), b""):
            digest.update(block)
    return digest.hexdigest()


def fraction(record: dict) -> Fraction:
    numerator, denominator = record["exact"].split("/")
    return Fraction(int(numerator), int(denominator))


def median(values: list[int]) -> Fraction:
    ordered = sorted(values)
    middle = len(ordered) // 2
    return Fraction(ordered[middle], 1) if len(ordered) % 2 else Fraction(ordered[middle - 1] + ordered[middle], 2)


def main() -> int:
    data = json.loads(MANIFEST.read_text(encoding="utf-8"))
    gates = []

    def gate(gate_id: str, passed: bool, detail) -> None:
        gates.append({"id": gate_id, "status": "pass" if passed else "fail", "detail": detail})

    gate("G01_contract", data["contract_id"] == "A005-CR-VISUAL-CORRECTION-A12-MEASUREMENT", data["contract_id"])
    gate("G02_status", data["status"] == "approved_authoritative_multi_row_dimension_statistics" and data["artifact_classification"] == "authoritative measurement record", {"status": data["status"], "classification": data["artifact_classification"]})
    gate("G03_approval_scope", data["authority"]["flamestrike_approval"] == "approved" and "measurement-only" in data["authority"]["scope"], data["authority"])
    gate("G03A_output_approval", data["flamestrike_output_approval"]["statement"] == "approved" and "C002 112.291667 x 76.651584 cm" in data["flamestrike_output_approval"]["scope"] and "no geometry rebuild" in data["flamestrike_output_approval"]["exclusions"], data["flamestrike_output_approval"])
    source_images = {}
    hash_failures = []
    for rel, expected in data["authority"]["inputs"].items():
        path = ROOT / rel
        actual = sha256(path)
        if actual != expected:
            hash_failures.append({"path": rel, "expected": expected, "actual": actual})
        if rel.endswith("STEP_03_FRONT.png"):
            source_images["front"] = Image.open(path).convert("RGB")
        elif rel.endswith("STEP_03_LEFT.png"):
            source_images["left"] = Image.open(path).convert("RGB")
    gate("G04_authority_hashes", not hash_failures, hash_failures or data["authority"]["inputs"])
    labels = data["direct_label_ownership"]
    gate("G05_direct_label_ownership", labels == {"C001_max_width_cm": 120, "C001_max_depth_cm": 90, "C004_footprint_width_cm": 140, "C004_footprint_depth_cm": 110, "base_height_cm": 35}, labels)
    hypothesis = data["tested_structural_plinth_hypothesis"]
    gate("G06_C003_120x90_rejected", hypothesis["result"] == "rejected_as_source_authority_conflict" and hypothesis["C003_120x90_authorized"] is False, hypothesis)

    expected_deltas = {"C002": {"front_X": [230, 231, 244], "left_Y": [151, 154, 155]}, "C003": {"front_X": [260, 261, 272, 276], "left_Y": [193, 193, 193]}}
    formula_failures = []
    rgb_failures = []
    for component, axes in expected_deltas.items():
        for axis, expected in axes.items():
            record = data["multi_row_statistics"][component][axis]
            actual = record["pixel_center_deltas_px"]
            if actual != expected:
                formula_failures.append({"component": component, "axis": axis, "expected": expected, "actual": actual})
                continue
            med = median(actual)
            envelope = 140 if axis == "front_X" else 110
            denominator = 288 if axis == "front_X" else 221
            physical = Fraction(envelope, 1) * med / denominator
            if fraction(record["median_delta_px"]) != med or fraction(record["conditional_median_extent_cm"]) != physical or fraction(record["conditional_extent_to_35cm_base_height"]) != physical / 35:
                formula_failures.append({"component": component, "axis": axis, "record": record})
            view = "front" if axis == "front_X" else "left"
            for row in record["approved_row_records"]:
                x0, x1 = row["half_open_span_px"]
                y = row["row_y_px"]
                if list(source_images[view].getpixel((x0, y))) != row["left_endpoint_rgb"] or list(source_images[view].getpixel((x1 - 1, y))) != row["right_endpoint_rgb"]:
                    rgb_failures.append(row["source_record_id"])
    gate("G07_exact_row_delta_sets", not formula_failures, formula_failures or expected_deltas)
    gate("G08_endpoint_RGB", not rgb_failures, rgb_failures or "all approved row endpoints match source RGB")
    gate("G09_C002_front_median", fraction(data["multi_row_statistics"]["C002"]["front_X"]["conditional_median_extent_cm"]) == Fraction(2695, 24), data["multi_row_statistics"]["C002"]["front_X"])
    gate("G10_C002_left_median", fraction(data["multi_row_statistics"]["C002"]["left_Y"]["conditional_median_extent_cm"]) == Fraction(16940, 221), data["multi_row_statistics"]["C002"]["left_Y"])
    gate("G11_C003_front_median", fraction(data["multi_row_statistics"]["C003"]["front_X"]["conditional_median_extent_cm"]) == Fraction(18655, 144), data["multi_row_statistics"]["C003"]["front_X"])
    gate("G12_C003_left_median", fraction(data["multi_row_statistics"]["C003"]["left_Y"]["conditional_median_extent_cm"]) == Fraction(21230, 221), data["multi_row_statistics"]["C003"]["left_Y"])
    gate("G13_C004_outer_envelope", data["envelopes"]["C004_outer_rubble"]["extent_cm"] == [140, 110] and data["envelopes"]["C004_outer_rubble"]["height_reference_cm"] == 35, data["envelopes"]["C004_outer_rubble"])
    gate("G14_C001_label_not_C003", data["envelopes"]["C001_maximum"]["extent_cm"] == [120, 90] and "not a C003" in data["envelopes"]["C001_maximum"]["status"], data["envelopes"]["C001_maximum"])
    controls = data["method"]
    gate("G15_no_candidate_fill", controls["candidate_fill_created"] is False, controls["candidate_fill_created"])
    gate("G16_no_closed_contour_or_fit", controls["closed_contour_created"] is False and controls["curve_fit_created"] is False, controls)
    gate("G17_no_geometry", controls["geometry_created"] is False and controls["blender_outputs_created"] == 0 and controls["fbx_outputs_created"] == 0, controls)
    gate("G18_no_Unreal", controls["unreal_outputs_created"] == 0, controls["unreal_outputs_created"])
    gate("G19_source_unmodified", controls["source_modified"] is False, controls["source_modified"])
    gate("G20_median_not_self_approved", any("not construction authority" in item for item in data["blocked"]), data["blocked"])
    board = ROOT / data["review_board"]
    gate("G21_board_hash", sha256(board) == data["review_board_sha256"], sha256(board))
    gate("G22_board_dimensions", Image.open(board).size == (3000, 1900), list(Image.open(board).size))
    failures = [record for record in gates if record["status"] != "pass"]
    output = {
        "schema": "aerathea.visual_correction_a12_two_envelope_measurement_validation.v1",
        "asset_id": data["asset_id"],
        "contract_id": data["contract_id"],
        "date": "2026-07-21",
        "status": "pass_authoritative_multi_row_measurement" if not failures else "blocked_a12_measurement_audit",
        "artifact_classification": "proof only",
        "manifest": {"path": str(MANIFEST.relative_to(ROOT)), "sha256": sha256(MANIFEST)},
        "gate_summary": {"passed": len(gates) - len(failures), "total": len(gates), "failed": len(failures)},
        "gates": gates,
        "decision": "A12 multi-row median dimensions are approved measurement authority; geometry still requires a separate approved contract" if not failures else "A12 measurement failed independent replay",
    }
    AUDIT.write_text(json.dumps(output, indent=2) + "\n", encoding="utf-8")
    print(json.dumps({"status": output["status"], "gate_summary": output["gate_summary"], "audit": str(AUDIT)}, indent=2))
    return 0 if not failures else 1


if __name__ == "__main__":
    raise SystemExit(main())
