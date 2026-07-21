#!/usr/bin/env python3
"""Independently replay the A005/A10 pixel-exact measurement package."""

from __future__ import annotations

import hashlib
import json
from fractions import Fraction
from pathlib import Path

from PIL import Image


ROOT = Path(__file__).resolve().parents[2]
ASSET = ROOT / "docs/assets/blueprints/SM_GIA_BloodAxeCairnstone_A005"
MANIFEST = ASSET / "manifests/VISUAL_CORRECTION_A10_PIXEL_EXACT_BASE_RECONCILIATION.json"
AUDIT = ASSET / "manifests/VISUAL_CORRECTION_A10_PIXEL_EXACT_BASE_RECONCILIATION_VALIDATION.json"


def sha256(path: Path) -> str:
    digest = hashlib.sha256()
    with path.open("rb") as handle:
        for block in iter(lambda: handle.read(1024 * 1024), b""):
            digest.update(block)
    return digest.hexdigest()


def exact_fraction(record: dict) -> Fraction:
    numerator, denominator = record["exact"].split("/")
    return Fraction(int(numerator), int(denominator))


def main() -> int:
    data = json.loads(MANIFEST.read_text(encoding="utf-8"))
    gates = []

    def gate(name: str, passed: bool, evidence) -> None:
        gates.append({"gate": name, "pass": bool(passed), "evidence": evidence})

    gate("manifest_status", data["status"] == "approved_authoritative_pixel_ratios_with_conditional_physical_conversion", data["status"])
    gate("artifact_classification", data["artifact_classification"] == "authoritative measurement record", data["artifact_classification"])
    gate("flamestrike_output_approval", data["flamestrike_output_approval"]["statement"] == "approved", data["flamestrike_output_approval"])

    source_images = {}
    for view, record in data["authority"]["source_panels"].items():
        path = ROOT / record["path"]
        actual_hash = sha256(path)
        gate(f"{view}_panel_hash", actual_hash == record["sha256"], actual_hash)
        source_images[view] = Image.open(path).convert("RGB")

    expected_spans = {
        "C001": (194, 115),
        "C002": (244, 155),
        "C003": (276, 193),
        "C004": (288, 221),
    }
    formula_failures = []
    rgb_failures = []
    for component, (expected_x, expected_y) in expected_spans.items():
        record = data["components"][component]
        x_record = record["front_X_owner"]
        y_record = record["left_Y_owner"]
        actual_x = x_record["pixel_center_delta_px"]
        actual_y = y_record["pixel_center_delta_px"]
        if (actual_x, actual_y) != (expected_x, expected_y):
            formula_failures.append({"component": component, "spans": [actual_x, actual_y]})

        expected_width = Fraction(140 * actual_x, 288)
        expected_depth = Fraction(110 * actual_y, 221)
        physical = record["conditional_physical_footprint_cm"]
        if exact_fraction(physical["width"]) != expected_width:
            formula_failures.append({"component": component, "axis": "X", "record": physical["width"]})
        if exact_fraction(physical["depth"]) != expected_depth:
            formula_failures.append({"component": component, "axis": "Y", "record": physical["depth"]})

        for owner_record, view in ((x_record, "front"), (y_record, "left")):
            for role in ("left_edge", "right_edge"):
                endpoint = owner_record[role]
                actual_rgb = list(source_images[view].getpixel(tuple(endpoint["pixel_local"])))
                if actual_rgb != endpoint["source_rgb"]:
                    rgb_failures.append({"component": component, "view": view, "role": role})

    gate("eight_owner_view_span_records", not formula_failures, formula_failures or expected_spans)
    gate("owner_view_endpoint_rgb", not rgb_failures, rgb_failures or "all 16 endpoint RGB values match")
    gate("consistent_pixel_center_delta_convention", data["method"]["pixel_span_convention"].startswith("distance between inclusive integer pixel centers"), data["method"]["pixel_span_convention"])
    gate("front_C004_denominator", data["method"]["front_C004_normalization_span_px"] == 288, data["method"]["front_C004_normalization_span_px"])
    gate("left_C004_denominator", data["method"]["left_C004_normalization_span_px"] == 221, data["method"]["left_C004_normalization_span_px"])

    contacts = data["top_interface_contact_reaudit"]
    contact_rgb_failures = []
    for point in contacts["points"]:
        actual_rgb = list(source_images["top"].getpixel(tuple(point["pixel_local"])))
        if actual_rgb != point["source_rgb"] or not point["rgb_match"]:
            contact_rgb_failures.append(point["id"])
    gate("top_contact_count", contacts["point_count"] == 48, contacts["point_count"])
    gate("top_contact_distribution", contacts["per_contact_counts"] == {"CL-001": 16, "CL-002": 16, "CL-003": 16}, contacts["per_contact_counts"])
    gate("top_contact_rgb", not contact_rgb_failures and contacts["rgb_mismatches"] == 0, contact_rgb_failures or "48/48 match")
    gate("top_contact_closure_blocked", not contacts["closure_authorized"], contacts["closure_authorized"])

    controls = data["method"]
    gate("no_threshold_ownership", not controls["threshold_derived_ownership_used"], controls["threshold_derived_ownership_used"])
    gate("no_segmentation", not controls["automated_segmentation_used"], controls["automated_segmentation_used"])
    gate("no_curve_fit", not controls["curve_or_oval_fit_created"], controls["curve_or_oval_fit_created"])
    gate("no_closed_contour", not controls["closed_contour_created"], controls["closed_contour_created"])
    gate("no_candidate_fill", not controls["candidate_fill_created"], controls["candidate_fill_created"])
    gate("no_geometry", not controls["geometry_created"], controls["geometry_created"])
    gate("source_unmodified", not controls["source_modified"], controls["source_modified"])
    gate("height_selection_blocked", data["conditional_height_intervals_cm"]["selected_course_heights"] is None, data["conditional_height_intervals_cm"]["selected_course_heights"])

    board = ROOT / data["review_board"]
    board_hash = sha256(board)
    gate("review_board_hash", board_hash == data["review_board_sha256"], board_hash)
    gate("review_board_dimensions", Image.open(board).size == (2800, 1900), list(Image.open(board).size))

    failures = [record for record in gates if not record["pass"]]
    output = {
        "schema": "aerathea.visual_correction_a10_pixel_exact_base_reconciliation_validation.v1",
        "asset_id": data["asset_id"],
        "measurement_id": data["measurement_id"],
        "date": "2026-07-21",
        "status": "pass_authoritative_measurement" if not failures else "fail",
        "artifact_classification": "proof only",
        "manifest": {"path": str(MANIFEST.relative_to(ROOT)), "sha256": sha256(MANIFEST)},
        "gate_count": len(gates),
        "pass_count": len(gates) - len(failures),
        "failure_count": len(failures),
        "gates": gates,
        "decision": "approved pixel-exact ratios replay; physical conversion remains conditional and geometry remains unauthorized" if not failures else "measurement package failed replay",
    }
    AUDIT.write_text(json.dumps(output, indent=2) + "\n", encoding="utf-8")
    print(json.dumps({"status": output["status"], "gates": len(gates), "passes": output["pass_count"], "failures": len(failures), "audit": str(AUDIT)}, indent=2))
    return 0 if not failures else 1


if __name__ == "__main__":
    raise SystemExit(main())
