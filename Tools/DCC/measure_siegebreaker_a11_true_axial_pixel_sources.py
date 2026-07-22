#!/usr/bin/env python3
"""Measure the user-supplied Siege Breaker axial sources without interpretation.

This script reuses the established A06/A09 dark-pixel connected-component
selection.  It records source pixels and exact ratios only; it does not create
geometry, inferred contours, overlays, or replacement images.
"""

from __future__ import annotations

import hashlib
import json
from fractions import Fraction
from pathlib import Path

from PIL import Image

from build_a06_siegebreaker_step06_front_back_measurements import selected_membership


ROOT = Path(__file__).resolve().parents[2]
ASSET_ID = "SM_DRW_SiegeBreaker_Hammer_A01"
SOURCE_ROOT = ROOT / "SourceAssets/Concepts/SiegeBreaker"
OUTPUT = (
    ROOT
    / "docs/assets/blueprints"
    / ASSET_ID
    / "manifests/A11_TRUE_AXIAL_TOP_BOTTOM_PIXEL_MEASUREMENT.json"
)

SOURCES = {
    "top": {
        "path": SOURCE_ROOT / "siege_breaker_true_axial_top_view.png",
        "sha256": "aee612d9bed74e4f861576f926fe9d75de00f80dc416e3a6ba66a75247c00e98",
    },
    "bottom": {
        "path": SOURCE_ROOT / "siege_breaker_true_axial_bottom_view.png",
        "sha256": "874a9e7c7713c7edbcf1030486d3988a54e8499ee697e316ec82a013fdb9d746",
    },
}

# Existing approved A09 pixel registration.  The 170 cm overall length is the
# one physical anchor; transverse dimensions are consequences of source-pixel
# ratios, not printed width/depth labels.
FRONT_OBJECT_WIDTH_PX = 491
FRONT_OBJECT_LENGTH_PX = 1111
LEFT_OBJECT_DEPTH_PX = 215
LEFT_OBJECT_LENGTH_PX = 1109
OVERALL_LENGTH_CM = 170


def sha256(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest()


def exact(value: Fraction) -> dict[str, int | str]:
    return {
        "numerator": value.numerator,
        "denominator": value.denominator,
        "display_decimal": f"{float(value):.9f}",
    }


def measure_source(view: str, source: dict[str, object], front_width_cm: Fraction) -> dict[str, object]:
    path = source["path"]
    assert isinstance(path, Path)
    expected_sha = source["sha256"]
    actual_sha = sha256(path)
    if actual_sha != expected_sha:
        raise RuntimeError(f"{view} source hash mismatch: {actual_sha}")

    image = Image.open(path)
    if image.size != (1254, 1254):
        raise RuntimeError(f"{view} source dimensions changed: {image.size}")
    decoded = image.convert("RGBA").tobytes("raw", "RGBA")
    membership, metadata = selected_membership(image)
    x0, y0, x1, y1 = metadata["rectangle_half_open"]
    width_px = x1 - x0
    depth_px = y1 - y0
    cm_per_pixel_from_front_width = front_width_cm / width_px
    depth_cm_from_front_width = depth_px * cm_per_pixel_from_front_width

    return {
        "view": view,
        "source_path": str(path.relative_to(ROOT)),
        "file_sha256": actual_sha,
        "decoded_rgba_sha256": hashlib.sha256(decoded).hexdigest(),
        "canvas_pixels": [image.width, image.height],
        "user_declared_projection": "+Z top" if view == "top" else "-Z bottom",
        "selection_method": "A06/A09 adaptive-luma greatest non-edge 8-connected component",
        "selection_metadata": metadata,
        "object_rectangle_half_open": [x0, y0, x1, y1],
        "object_width_pixels": width_px,
        "object_depth_pixels": depth_px,
        "object_center_edge_pixels_exact": {
            "x": exact(Fraction(x0 + x1, 2)),
            "y": exact(Fraction(y0 + y1, 2)),
        },
        "width_to_depth_ratio_exact": exact(Fraction(width_px, depth_px)),
        "registration_using_existing_front_pixel_width": {
            "front_width_cm_exact": exact(front_width_cm),
            "cm_per_axial_pixel_exact": exact(cm_per_pixel_from_front_width),
            "depth_cm_consequence_exact": exact(depth_cm_from_front_width),
        },
        "printed_52x32_labels": "reference only; explicitly superseded by Flamestrike's pixel-measurement direction",
        "artifact_status": "authoritative source pixels and measured extent under approved reconciliation",
    }


def main() -> None:
    front_width_cm = Fraction(FRONT_OBJECT_WIDTH_PX * OVERALL_LENGTH_CM, FRONT_OBJECT_LENGTH_PX)
    left_depth_cm = Fraction(LEFT_OBJECT_DEPTH_PX * OVERALL_LENGTH_CM, LEFT_OBJECT_LENGTH_PX)
    views = {name: measure_source(name, source, front_width_cm) for name, source in SOURCES.items()}

    top_depth_cm = Fraction(
        views["top"]["registration_using_existing_front_pixel_width"]["depth_cm_consequence_exact"]["numerator"],
        views["top"]["registration_using_existing_front_pixel_width"]["depth_cm_consequence_exact"]["denominator"],
    )
    bottom_depth_cm = Fraction(
        views["bottom"]["registration_using_existing_front_pixel_width"]["depth_cm_consequence_exact"]["numerator"],
        views["bottom"]["registration_using_existing_front_pixel_width"]["depth_cm_consequence_exact"]["denominator"],
    )

    mean_width_px = Fraction(
        views["top"]["object_width_pixels"] + views["bottom"]["object_width_pixels"],
        2,
    )
    mean_depth_px = Fraction(
        views["top"]["object_depth_pixels"] + views["bottom"]["object_depth_pixels"],
        2,
    )
    common_cm_per_pixel = front_width_cm / mean_width_px
    approved_depth_cm = mean_depth_px * common_cm_per_pixel

    result = {
        "schema": "aerathea.siegebreaker_true_axial_pixel_measurement.v2",
        "asset_id": ASSET_ID,
        "date": "2026-07-22",
        "artifact_status": "authoritative measurement and reconciliation rule",
        "software_boundary": {
            "image_generation_used": False,
            "trellis_used": False,
            "image_to_3d_used": False,
            "blender_geometry_changed": False,
            "procedural_image_or_overlay_created": False,
        },
        "flamestrike_authority": {
            "source_identity": "Image 1 is Top View; Image 2 is Bottom View",
            "measurement_rule": "use pixel measurements",
            "printed_dimensions_control_geometry": False,
            "reconciliation_decision": "approved centered mean of top/bottom footprints; axial views own head depth; side view retains design/profile-detail authority but not head-depth scale",
        },
        "existing_a09_pixel_registration": {
            "overall_length_anchor_cm": OVERALL_LENGTH_CM,
            "front_object_pixels_width_by_length": [FRONT_OBJECT_WIDTH_PX, FRONT_OBJECT_LENGTH_PX],
            "left_object_pixels_depth_by_length": [LEFT_OBJECT_DEPTH_PX, LEFT_OBJECT_LENGTH_PX],
            "front_width_cm_exact": exact(front_width_cm),
            "left_depth_cm_exact": exact(left_depth_cm),
        },
        "axial_sources": views,
        "cross_view_evidence": {
            "top_vs_bottom_width_pixel_delta": abs(views["top"]["object_width_pixels"] - views["bottom"]["object_width_pixels"]),
            "top_vs_bottom_depth_pixel_delta": abs(views["top"]["object_depth_pixels"] - views["bottom"]["object_depth_pixels"]),
            "top_depth_cm_from_front_width_exact": exact(top_depth_cm),
            "bottom_depth_cm_from_front_width_exact": exact(bottom_depth_cm),
            "top_minus_left_depth_percent_exact": exact((top_depth_cm - left_depth_cm) / left_depth_cm * 100),
            "bottom_minus_left_depth_percent_exact": exact((bottom_depth_cm - left_depth_cm) / left_depth_cm * 100),
            "bottom_minus_top_depth_cm_exact": exact(bottom_depth_cm - top_depth_cm),
            "bottom_minus_top_depth_percent_of_top_exact": exact((bottom_depth_cm - top_depth_cm) / top_depth_cm * 100),
            "raw_evidence_verdict": "cross_view_depth_conflict",
            "resolution": "resolved by Flamestrike-approved centered-mean axial ownership rule",
        },
        "approved_reconciliation": {
            "alignment_rule": "register top and bottom on their exact object center edges",
            "formula": "arithmetic mean of exact top/bottom full object pixel extents",
            "mean_width_pixels_exact": exact(mean_width_px),
            "mean_depth_pixels_exact": exact(mean_depth_px),
            "common_cm_per_axial_pixel_exact": exact(common_cm_per_pixel),
            "approved_head_width_cm_exact": exact(front_width_cm),
            "approved_head_depth_cm_exact": exact(approved_depth_cm),
            "centered_residual_per_side_pixels_exact": {
                "top_width": exact((mean_width_px - views["top"]["object_width_pixels"]) / 2),
                "bottom_width": exact((views["bottom"]["object_width_pixels"] - mean_width_px) / 2),
                "top_depth": exact((mean_depth_px - views["top"]["object_depth_pixels"]) / 2),
                "bottom_depth": exact((views["bottom"]["object_depth_pixels"] - mean_depth_px) / 2),
            },
            "top_bottom_role": "authoritative for head X/Y footprint, depth scale, and their respective visible surface design",
            "side_role": "authoritative for visible side/profile design detail and longitudinal placement; not authoritative for head-depth scale",
            "status": "authoritative",
        },
        "geometry_authority": {
            "head_footprint_scale": True,
            "top_bottom_surface_design": True,
            "side_head_depth_scale": False,
            "blender_geometry_edit_executed": False,
        },
        "next_decision_required": "A separate Blender reconstruction step contract is required before geometry changes.",
    }

    OUTPUT.parent.mkdir(parents=True, exist_ok=True)
    OUTPUT.write_text(json.dumps(result, indent=2) + "\n", encoding="utf-8")
    print(json.dumps({
        "result": result["cross_view_evidence"]["resolution"],
        "output": str(OUTPUT.relative_to(ROOT)),
        "top_bbox": views["top"]["object_rectangle_half_open"],
        "bottom_bbox": views["bottom"]["object_rectangle_half_open"],
    }, sort_keys=True))


if __name__ == "__main__":
    main()
