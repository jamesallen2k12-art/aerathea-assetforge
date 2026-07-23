#!/usr/bin/env python3
"""Independently replay Step 03 rectangles, membership, and source RGBA."""

from __future__ import annotations

import gzip
import hashlib
import importlib.util
import json
from pathlib import Path

from PIL import Image


ROOT = Path(__file__).resolve().parents[2]
RUN = ROOT / (
    "docs/assets/blueprints/SM_DRW_SiegeBreaker_Hammer_A01/proof_runs/"
    "SB-CR-STEPS01-16-R8-PIXEL-EXACT-A01"
)
MANIFEST = RUN / "manifests/STEP_03_CROP_COORDINATES.json"
OUTPUT = RUN / "manifests/STEP_03_INDEPENDENT_AUDIT.json"
METHOD_PATH = ROOT / "Tools/DCC/measure_siegebreaker_a12_r10_r8_full_scanlines.py"


def sha256_bytes(value: bytes) -> str:
    return hashlib.sha256(value).hexdigest()


def sha256(path: Path) -> str:
    return sha256_bytes(path.read_bytes())


def load_selector():
    spec = importlib.util.spec_from_file_location("r8_selector_audit", METHOD_PATH)
    module = importlib.util.module_from_spec(spec)
    assert spec.loader is not None
    spec.loader.exec_module(module)
    return module


def main() -> None:
    manifest = json.loads(MANIFEST.read_text())
    selector = load_selector()
    checks = {}
    observed = {}
    for record in manifest["sources"]:
        view = record["id"]
        source_path = ROOT / record["source_path"]
        image, membership, metadata = selector.selected_object(source_path)
        capture = json.loads(
            gzip.decompress((ROOT / record["capture_path"]).read_bytes())
        )
        replay_membership = bytearray(image.width * image.height)
        replay_selected_rgba = bytearray()
        source_rgba = image.tobytes("raw", "RGBA")
        capture_locations = 0
        for row in capture["rows_with_exact_rgba"]:
            y = int(row["y"])
            for run in row["runs"]:
                x0, x1 = int(run["x0"]), int(run["x1"])
                payload = bytes.fromhex(run["rgba_hex"])
                checks[f"{view}_run_payload_{y}_{x0}"] = (
                    len(payload) == (x1 - x0) * 4
                )
                for offset, x in enumerate(range(x0, x1)):
                    flat = y * image.width + x
                    replay_membership[flat] = 1
                    pixel = payload[offset * 4:offset * 4 + 4]
                    replay_selected_rgba.extend(pixel)
                    checks[f"{view}_pixel_source_{y}_{x}"] = (
                        pixel == source_rgba[flat * 4:flat * 4 + 4]
                    )
                    capture_locations += 1
        compact_checks = {
            f"{view}_source_hash": sha256(source_path)
            == record["source_file_sha256"],
            f"{view}_rectangle_recomputed": metadata["rectangle_half_open"]
            == record["rectangle_half_open"],
            f"{view}_membership_recomputed": bytes(replay_membership)
            == bytes(membership),
            f"{view}_membership_hash": sha256_bytes(bytes(replay_membership))
            == record["decoded_membership_sha256"],
            f"{view}_selected_rgba_hash": sha256_bytes(
                bytes(replay_selected_rgba)
            )
            == record["selected_rgba_sha256"],
            f"{view}_pixel_count": capture_locations
            == record["exact_selected_pixel_count"],
            f"{view}_crop_hash": sha256(ROOT / record["crop_path"])
            == record["crop_file_sha256"],
            f"{view}_no_padding": record["padding_pixels"] == 0,
        }
        # Collapse the per-pixel source comparison into one mandatory check in
        # the output while still evaluating every pixel above.
        pixel_keys = [
            key for key in checks
            if key.startswith(f"{view}_pixel_source_")
            or key.startswith(f"{view}_run_payload_")
        ]
        compact_checks[f"{view}_every_capture_pixel_matches_source"] = all(
            checks[key] for key in pixel_keys
        )
        for key in pixel_keys:
            del checks[key]
        checks.update(compact_checks)
        observed[view] = {
            "rectangle_half_open": metadata["rectangle_half_open"],
            "selected_pixel_count": capture_locations,
            "membership_sha256": sha256_bytes(bytes(replay_membership)),
            "selected_rgba_sha256": sha256_bytes(bytes(replay_selected_rgba)),
        }
    checks.update(
        {
            "six_views": len(manifest["sources"]) == 6,
            "source_pixels_unmodified": manifest["source_pixels_modified"] is False,
            "no_resize_or_rotation": manifest[
                "resize_filter_cleanup_recolor_rotation"
            ]
            is False,
            "no_geometry": manifest["geometry_created"] is False,
        }
    )
    result = "PASS" if all(checks.values()) else "FAIL"
    output = {
        "schema": "AERATHEA_STEP03_INDEPENDENT_AUDIT_V1",
        "run_id": manifest["run_id"],
        "artifact_status": "proof only",
        "builder_not_imported": True,
        "selector_recomputed": True,
        "every_selected_location_and_rgba_replayed": True,
        "observed": observed,
        "checks": checks,
        "pass_count": sum(checks.values()),
        "check_count": len(checks),
        "result": result,
    }
    OUTPUT.write_text(json.dumps(output, indent=2) + "\n")
    print(
        json.dumps(
            {
                "result": result,
                "checks": f"{sum(checks.values())}/{len(checks)}",
                "selected_pixels_checked": sum(
                    value["selected_pixel_count"] for value in observed.values()
                ),
                "failures": [name for name, value in checks.items() if not value],
            },
            indent=2,
        )
    )
    if result != "PASS":
        raise RuntimeError("Step 03 independent audit failed")


if __name__ == "__main__":
    main()
