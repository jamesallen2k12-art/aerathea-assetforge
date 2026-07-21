#!/usr/bin/env python3
"""Extract fresh, lossless A04 Siege Breaker source evidence.

This script deliberately reads only the approved final-package concept sheet and
the fresh A04 scanline manifest.  It never reads an A01/A02/A03 Hammer output.
All crops are integer-coordinate copies with no resampling.  The primary object
and panel silhouettes are selected as the largest connected non-paper region in
their declared source windows, then recorded as exact masks, row spans, and
source-owned component records.
"""

from __future__ import annotations

import hashlib
import json
from collections import deque
from pathlib import Path
from typing import Any

from PIL import Image, ImageChops


ROOT = Path(__file__).resolve().parents[2]
ASSET_ID = "SM_DRW_SiegeBreaker_Hammer_A01"
PASS_ID = "VisualFidelity_A04"
SOURCE = ROOT / (
    "SourceAssets/Reference/Weapons/Dwarven/SM_DRW_SiegeBreaker_Hammer_A01/"
    "02_SiegeBreaker_Codex_Final_Package/reference/concept_sheet_style_reference.png"
)
REVIEW_ROOT = ROOT / "Saved/Automation/DCC" / ASSET_ID / PASS_ID
EVIDENCE_ROOT = REVIEW_ROOT / "FreshEvidence"
SCAN_MANIFEST = (
    EVIDENCE_ROOT
    / "ScanlineVerify"
    / f"{ASSET_ID}_A04_SourceSheet_ScanlineManifest.json"
)
EVIDENCE_MANIFEST = EVIDENCE_ROOT / f"{ASSET_ID}_A04_FreshEvidenceManifest.json"
PRE_GEOMETRY_AUDIT = EVIDENCE_ROOT / f"{ASSET_ID}_A04_PreGeometryAudit.json"


# Declared source windows are intentionally broad enough to contain one complete
# illustrated view while excluding neighboring view cells.  Object bounds are
# detected afresh inside each window.
VIEW_WINDOWS: dict[str, tuple[int, int, int, int]] = {
    "primary": (30, 85, 410, 975),
    "front": (430, 110, 705, 625),
    "back": (720, 110, 1000, 625),
    "left": (430, 625, 710, 1040),
    "right": (725, 625, 1000, 1040),
    "top": (35, 1040, 525, 1300),
    "bottom": (530, 1040, 1020, 1300),
}


# These are source-sheet row ownership boundaries, not geometry dimensions.
# They partition the connected primary illustration at visible construction
# transitions.  Numeric world intervals remain independently authoritative.
PRIMARY_COMPONENT_ROWS: dict[str, tuple[int, int]] = {
    "head": (104, 405),
    "shaft": (405, 650),
    "grip": (650, 824),
    "pommel": (824, 968),
}

WORLD_COMPONENT_INTERVALS_CM: dict[str, tuple[float, float]] = {
    "head": (132.0, 170.0),
    "shaft": (60.0, 132.0),
    "grip": (18.0, 60.0),
    "pommel": (0.0, 18.0),
}

WORLD_COMPONENT_WIDTHS_CM: dict[str, float] = {
    "head": 52.0,
    "shaft": 5.0,
    "grip": 5.0,
    "pommel": 11.0,
}

SECONDARY_COMPONENT_ROWS: dict[str, dict[str, tuple[int, int]]] = {
    "back": {"head": (170, 304), "shaft": (304, 418), "grip": (418, 528), "pommel": (528, 583)},
    "left": {"head": (693, 828), "shaft": (828, 904), "grip": (904, 960), "pommel": (960, 1003)},
    "right": {"head": (693, 828), "shaft": (828, 904), "grip": (904, 960), "pommel": (960, 1003)},
}

SECONDARY_VISIBLE_SPANS_CM: dict[str, dict[str, float]] = {
    "back": {"head": 52.0, "shaft": 5.0, "grip": 5.0, "pommel": 11.0},
    "left": {"head": 32.0, "shaft": 5.0, "grip": 5.0, "pommel": 9.0},
    "right": {"head": 32.0, "shaft": 5.0, "grip": 5.0, "pommel": 9.0},
}


def rel(path: Path) -> str:
    return str(path.relative_to(ROOT))


def file_sha256(path: Path) -> str:
    digest = hashlib.sha256()
    with path.open("rb") as handle:
        for block in iter(lambda: handle.read(1024 * 1024), b""):
            digest.update(block)
    return digest.hexdigest()


def pixel_sha256(image: Image.Image) -> str:
    return hashlib.sha256(image.convert("RGB").tobytes("raw", "RGB")).hexdigest()


def is_non_paper_pixel(rgb: tuple[int, int, int]) -> bool:
    red, green, blue = rgb
    luminance = (red + green + blue) / 3.0
    chroma = max(rgb) - min(rgb)
    return luminance < 215.0 or (chroma > 28 and luminance < 240.0)


def largest_connected_mask(crop: Image.Image) -> Image.Image:
    rgb = crop.convert("RGB")
    width, height = rgb.size
    pixels = rgb.load()
    visited = bytearray(width * height)
    largest: list[tuple[int, int]] = []

    for y in range(height):
        for x in range(width):
            index = y * width + x
            if visited[index] or not is_non_paper_pixel(pixels[x, y]):
                continue
            visited[index] = 1
            queue: deque[tuple[int, int]] = deque([(x, y)])
            component: list[tuple[int, int]] = []
            while queue:
                px, py = queue.popleft()
                component.append((px, py))
                for nx, ny in ((px - 1, py), (px + 1, py), (px, py - 1), (px, py + 1)):
                    if nx < 0 or nx >= width or ny < 0 or ny >= height:
                        continue
                    neighbor = ny * width + nx
                    if visited[neighbor] or not is_non_paper_pixel(pixels[nx, ny]):
                        continue
                    visited[neighbor] = 1
                    queue.append((nx, ny))
            if len(component) > len(largest):
                largest = component

    if not largest:
        raise RuntimeError("No connected source-owned object pixels found")
    mask = Image.new("L", (width, height), 0)
    mask_pixels = mask.load()
    for x, y in largest:
        mask_pixels[x, y] = 255
    return mask


def mask_bbox(mask: Image.Image) -> tuple[int, int, int, int]:
    bbox = mask.getbbox()
    if bbox is None:
        raise RuntimeError("Empty source mask")
    return tuple(int(value) for value in bbox)


def mask_area(mask: Image.Image) -> int:
    return sum(1 for value in mask.getdata() if value)


def exact_crop_record(source: Image.Image, view_name: str, window: tuple[int, int, int, int]) -> dict[str, Any]:
    window_crop = source.crop(window)
    window_mask = largest_connected_mask(window_crop)
    local_bbox = mask_bbox(window_mask)
    global_bbox = (
        window[0] + local_bbox[0],
        window[1] + local_bbox[1],
        window[0] + local_bbox[2],
        window[1] + local_bbox[3],
    )
    exact_rgb = source.crop(global_bbox).convert("RGB")
    exact_mask = window_mask.crop(local_bbox)
    rgba = exact_rgb.convert("RGBA")
    rgba.putalpha(exact_mask)

    stem = f"{ASSET_ID}_A04_{view_name.title()}"
    rgb_path = EVIDENCE_ROOT / f"{stem}_ExactVisiblePixels.png"
    mask_path = EVIDENCE_ROOT / f"{stem}_Mask.png"
    rgba_path = EVIDENCE_ROOT / f"{stem}_ExactRGBA.png"
    exact_rgb.save(rgb_path, optimize=True)
    exact_mask.save(mask_path, optimize=True)
    rgba.save(rgba_path, optimize=True)

    spans: list[dict[str, int]] = []
    mask_pixels = exact_mask.load()
    for local_y in range(exact_mask.height):
        xs = [x for x in range(exact_mask.width) if mask_pixels[x, local_y]]
        if not xs:
            continue
        spans.append(
            {
                "source_y": global_bbox[1] + local_y,
                "source_x_min": global_bbox[0] + min(xs),
                "source_x_max_inclusive": global_bbox[0] + max(xs),
                "pixel_width": max(xs) - min(xs) + 1,
            }
        )

    return {
        "view": view_name,
        "selection_method": "source_priority" if view_name == "primary" else "exact",
        "source_window_xyxy": list(window),
        "source_bbox_xyxy": list(global_bbox),
        "integer_coordinates": True,
        "resampling": "none",
        "crop_rgb": rel(rgb_path),
        "crop_rgba": rel(rgba_path),
        "mask": rel(mask_path),
        "crop_pixel_sha256": pixel_sha256(exact_rgb),
        "mask_file_sha256": file_sha256(mask_path),
        "mask_area_pixels": mask_area(exact_mask),
        "row_spans": spans,
    }


def build_primary_components(source: Image.Image, primary: dict[str, Any]) -> dict[str, Any]:
    primary_mask_path = ROOT / primary["mask"]
    primary_bbox = tuple(primary["source_bbox_xyxy"])
    primary_mask = Image.open(primary_mask_path).convert("L")
    components: dict[str, Any] = {}

    for component, (row_start, row_end) in PRIMARY_COMPONENT_ROWS.items():
        clipped_start = max(row_start, primary_bbox[1])
        clipped_end = min(row_end, primary_bbox[3])
        if clipped_end <= clipped_start:
            raise RuntimeError(f"Component {component} has no rows in the primary source mask")

        component_mask_full = Image.new("L", primary_mask.size, 0)
        src_pixels = primary_mask.load()
        dst_pixels = component_mask_full.load()
        for local_y in range(clipped_start - primary_bbox[1], clipped_end - primary_bbox[1]):
            for local_x in range(primary_mask.width):
                if src_pixels[local_x, local_y]:
                    dst_pixels[local_x, local_y] = 255

        local_bbox = mask_bbox(component_mask_full)
        global_bbox = (
            primary_bbox[0] + local_bbox[0],
            primary_bbox[1] + local_bbox[1],
            primary_bbox[0] + local_bbox[2],
            primary_bbox[1] + local_bbox[3],
        )
        component_rgb = source.crop(global_bbox).convert("RGB")
        component_mask = component_mask_full.crop(local_bbox)
        component_rgba = component_rgb.convert("RGBA")
        component_rgba.putalpha(component_mask)

        stem = f"{ASSET_ID}_A04_Primary_{component.title()}"
        rgb_path = EVIDENCE_ROOT / f"{stem}_ExactVisiblePixels.png"
        mask_path = EVIDENCE_ROOT / f"{stem}_Mask.png"
        rgba_path = EVIDENCE_ROOT / f"{stem}_ExactRGBA.png"
        component_rgb.save(rgb_path, optimize=True)
        component_mask.save(mask_path, optimize=True)
        component_rgba.save(rgba_path, optimize=True)

        spans: list[dict[str, int]] = []
        component_pixels = component_mask.load()
        for local_y in range(component_mask.height):
            xs = [x for x in range(component_mask.width) if component_pixels[x, local_y]]
            if not xs:
                continue
            spans.append(
                {
                    "source_y": global_bbox[1] + local_y,
                    "source_x_min": global_bbox[0] + min(xs),
                    "source_x_max_inclusive": global_bbox[0] + max(xs),
                    "pixel_width": max(xs) - min(xs) + 1,
                }
            )

        components[component] = {
            "component_owner": f"primary_{component}_component",
            "source_scope": "component_isolated",
            "selection_method": "source_priority",
            "source_rows_start_inclusive_end_exclusive": [clipped_start, clipped_end],
            "source_bbox_xyxy": list(global_bbox),
            "world_z_interval_cm": list(WORLD_COMPONENT_INTERVALS_CM[component]),
            "world_visible_width_cm": WORLD_COMPONENT_WIDTHS_CM[component],
            "source_to_world_formula": (
                "piecewise direct row/column mapping; no averaged or smoothed source measurement"
            ),
            "crop_rgb": rel(rgb_path),
            "crop_rgba": rel(rgba_path),
            "mask": rel(mask_path),
            "crop_pixel_sha256": pixel_sha256(component_rgb),
            "mask_file_sha256": file_sha256(mask_path),
            "mask_area_pixels": mask_area(component_mask),
            "row_spans": spans,
        }

    return components


def build_secondary_components(source: Image.Image, views: dict[str, Any]) -> dict[str, Any]:
    result: dict[str, Any] = {}
    for view_name, component_rows in SECONDARY_COMPONENT_ROWS.items():
        view = views[view_name]
        view_bbox = tuple(view["source_bbox_xyxy"])
        view_mask = Image.open(ROOT / view["mask"]).convert("L")
        result[view_name] = {}
        for component, (row_start, row_end) in component_rows.items():
            clipped_start = max(row_start, view_bbox[1])
            clipped_end = min(row_end, view_bbox[3])
            component_full = Image.new("L", view_mask.size, 0)
            src_pixels = view_mask.load()
            dst_pixels = component_full.load()
            for local_y in range(clipped_start - view_bbox[1], clipped_end - view_bbox[1]):
                for local_x in range(view_mask.width):
                    if src_pixels[local_x, local_y]:
                        dst_pixels[local_x, local_y] = 255
            local_bbox = mask_bbox(component_full)
            global_bbox = (
                view_bbox[0] + local_bbox[0],
                view_bbox[1] + local_bbox[1],
                view_bbox[0] + local_bbox[2],
                view_bbox[1] + local_bbox[3],
            )
            rgb = source.crop(global_bbox).convert("RGB")
            mask = component_full.crop(local_bbox)
            rgba = rgb.convert("RGBA")
            rgba.putalpha(mask)
            stem = f"{ASSET_ID}_A04_{view_name.title()}_{component.title()}"
            rgb_path = EVIDENCE_ROOT / f"{stem}_ExactVisiblePixels.png"
            mask_path = EVIDENCE_ROOT / f"{stem}_Mask.png"
            rgba_path = EVIDENCE_ROOT / f"{stem}_ExactRGBA.png"
            rgb.save(rgb_path, optimize=True)
            mask.save(mask_path, optimize=True)
            rgba.save(rgba_path, optimize=True)
            spans: list[dict[str, int]] = []
            mask_pixels = mask.load()
            for local_y in range(mask.height):
                xs = [x for x in range(mask.width) if mask_pixels[x, local_y]]
                if xs:
                    spans.append(
                        {
                            "source_y": global_bbox[1] + local_y,
                            "source_x_min": global_bbox[0] + min(xs),
                            "source_x_max_inclusive": global_bbox[0] + max(xs),
                            "pixel_width": max(xs) - min(xs) + 1,
                        }
                    )
            result[view_name][component] = {
                "component_owner": f"{view_name}_{component}_component",
                "source_scope": "component_isolated",
                "selection_method": "exact",
                "source_rows_start_inclusive_end_exclusive": [clipped_start, clipped_end],
                "source_bbox_xyxy": list(global_bbox),
                "world_z_interval_cm": list(WORLD_COMPONENT_INTERVALS_CM[component]),
                "world_visible_span_cm": SECONDARY_VISIBLE_SPANS_CM[view_name][component],
                "world_visible_axis": "X" if view_name == "back" else "Y",
                "crop_rgb": rel(rgb_path),
                "crop_rgba": rel(rgba_path),
                "mask": rel(mask_path),
                "crop_pixel_sha256": pixel_sha256(rgb),
                "mask_file_sha256": file_sha256(mask_path),
                "mask_area_pixels": mask_area(mask),
                "row_spans": spans,
            }
    return result


def exact_image_equal(left: Image.Image, right: Image.Image) -> bool:
    return ImageChops.difference(left.convert("RGB"), right.convert("RGB")).getbbox() is None


def main() -> int:
    EVIDENCE_ROOT.mkdir(parents=True, exist_ok=True)
    scan = json.loads(SCAN_MANIFEST.read_text(encoding="utf-8"))
    if not (
        scan.get("pixel_exact") is True
        and scan.get("changed_pixels") == 0
        and scan.get("max_rgb_delta") == 0
        and scan.get("mean_grayscale_delta") == 0.0
    ):
        raise RuntimeError("Fresh A04 scanline record is not zero-difference")

    source = Image.open(SOURCE).convert("RGB")
    views = {name: exact_crop_record(source, name, window) for name, window in VIEW_WINDOWS.items()}
    components = build_primary_components(source, views["primary"])
    secondary_components = build_secondary_components(source, views)

    manifest = {
        "schema": "aerathea.siegebreaker_a04_fresh_evidence.v1",
        "asset_id": ASSET_ID,
        "pass_id": PASS_ID,
        "status": "authoritative source evidence",
        "source": rel(SOURCE),
        "source_file_sha256": file_sha256(SOURCE),
        "source_pixel_sha256": pixel_sha256(source),
        "source_size_pixels": list(source.size),
        "fresh_scanline_manifest": rel(SCAN_MANIFEST),
        "fresh_scanline_result": {
            "format": scan["format"],
            "pixel_exact": scan["pixel_exact"],
            "changed_pixels": scan["changed_pixels"],
            "max_rgb_delta": scan["max_rgb_delta"],
            "mean_grayscale_delta": scan["mean_grayscale_delta"],
            "scan_sha256": scan["scan_sha256"],
        },
        "authority": {
            "primary_visible_projection": "primary",
            "secondary_depth_and_hidden_construction": ["front", "back", "left", "right", "top", "bottom"],
            "numeric_envelope_cm": [52.0, 32.0, 170.0],
            "prior_hammer_candidate_inputs": [],
            "visible_selection_methods": ["exact", "source_priority", "direct_constraint"],
            "visible_averaging": False,
            "filtered_resampling": False,
        },
        "views": views,
        "primary_components": components,
        "secondary_components": secondary_components,
        "unknowns": [
            "occluded back and internal socket topology",
            "hidden surface color continuation",
            "normal, roughness, metallic, and collision interpretation",
        ],
    }
    EVIDENCE_MANIFEST.write_text(json.dumps(manifest, indent=2) + "\n", encoding="utf-8")

    checks: list[dict[str, Any]] = []

    def add(name: str, passed: bool, detail: str) -> None:
        checks.append({"name": name, "passed": bool(passed), "detail": detail})

    add("fresh_scanline_zero_difference", scan["pixel_exact"] is True, str(manifest["fresh_scanline_result"]))
    add("source_hash_matches_locked_authority", file_sha256(SOURCE) == "3308a7bd0f0830c9cd1b695b57077d9faf77a839bb3e70edc6afe87c68af8b74", file_sha256(SOURCE))
    for name, view in views.items():
        bbox = tuple(view["source_bbox_xyxy"])
        extracted = Image.open(ROOT / view["crop_rgb"]).convert("RGB")
        add(f"{name}_integer_crop_exact", exact_image_equal(extracted, source.crop(bbox)), f"bbox={bbox}, resampling=none")
        add(f"{name}_mask_nonempty", view["mask_area_pixels"] > 0, f"area={view['mask_area_pixels']}")
        add(f"{name}_row_spans_present", bool(view["row_spans"]), f"rows={len(view['row_spans'])}")
    for name, component in components.items():
        bbox = tuple(component["source_bbox_xyxy"])
        extracted = Image.open(ROOT / component["crop_rgb"]).convert("RGB")
        add(f"component_{name}_integer_crop_exact", exact_image_equal(extracted, source.crop(bbox)), f"bbox={bbox}")
        add(f"component_{name}_source_owned_rows_present", bool(component["row_spans"]), f"rows={len(component['row_spans'])}")
    for view_name, view_components in secondary_components.items():
        for name, component in view_components.items():
            bbox = tuple(component["source_bbox_xyxy"])
            extracted = Image.open(ROOT / component["crop_rgb"]).convert("RGB")
            add(f"secondary_{view_name}_{name}_integer_crop_exact", exact_image_equal(extracted, source.crop(bbox)), f"bbox={bbox}")
            add(f"secondary_{view_name}_{name}_source_owned_rows_present", bool(component["row_spans"]), f"rows={len(component['row_spans'])}")

    passed = all(item["passed"] for item in checks)
    audit = {
        "schema": "aerathea.siegebreaker_a04_pregeometry_audit.v1",
        "asset_id": ASSET_ID,
        "pass_id": PASS_ID,
        "status": "proof only",
        "passed": passed,
        "evidence_manifest": rel(EVIDENCE_MANIFEST),
        "checks": checks,
        "failed_checks": [item for item in checks if not item["passed"]],
    }
    PRE_GEOMETRY_AUDIT.write_text(json.dumps(audit, indent=2) + "\n", encoding="utf-8")
    print(EVIDENCE_MANIFEST)
    print(PRE_GEOMETRY_AUDIT)
    print(f"A04 PRE-GEOMETRY AUDIT: {'PASS' if passed else 'FAIL'} ({len(checks)} checks)")
    return 0 if passed else 2


if __name__ == "__main__":
    raise SystemExit(main())
