#!/usr/bin/env python3
"""Independently audit the fresh R8 Step 02 source lock."""

from __future__ import annotations

import gzip
import hashlib
import json
from pathlib import Path

from PIL import Image


ROOT = Path(__file__).resolve().parents[2]
RUN = ROOT / (
    "docs/assets/blueprints/SM_DRW_SiegeBreaker_Hammer_A01/proof_runs/"
    "SB-CR-STEPS01-16-R8-PIXEL-EXACT-A01"
)
LOCK = RUN / "manifests/STEP_02_SOURCE_LOCK.json"
OUTPUT = RUN / "manifests/STEP_02_INDEPENDENT_AUDIT.json"
MAGIC = b"AET_RGB_SCANLINE_V1\n"


def sha256_bytes(value: bytes) -> str:
    return hashlib.sha256(value).hexdigest()


def sha256(path: Path) -> str:
    return sha256_bytes(path.read_bytes())


def replay(scan_path: Path) -> tuple[int, int, bytes]:
    with gzip.open(scan_path, "rb") as scan:
        if scan.readline() != MAGIC:
            raise RuntimeError("scan magic mismatch")
        width, height, channels, mode = scan.readline().decode().split()
        width_i = int(width)
        height_i = int(height)
        if channels != "3" or mode != "RGB":
            raise RuntimeError("scan metadata mismatch")
        rows = []
        for expected in range(height_i):
            index = int.from_bytes(scan.read(4), "big")
            if index != expected:
                raise RuntimeError("scanline index mismatch")
            row = scan.read(width_i * 3)
            if len(row) != width_i * 3:
                raise RuntimeError("short scanline")
            rows.append(row)
        if scan.read(1):
            raise RuntimeError("unexpected scan payload")
    return width_i, height_i, b"".join(rows)


def main() -> None:
    lock = json.loads(LOCK.read_text())
    checks: dict[str, bool] = {}
    observed = {}
    for record in lock["approved_sources"]:
        source_path = ROOT / record["path"]
        scan_path = ROOT / record["scan_record"]
        with Image.open(source_path) as opened:
            source = opened.convert("RGB")
        source_bytes = source.tobytes("raw", "RGB")
        width, height, replay_bytes = replay(scan_path)
        source_id = record["id"]
        source_checks = {
            "source_file_hash": sha256(source_path) == record["file_sha256"],
            "source_canvas": [source.width, source.height] == [width, height],
            "decoded_hash": sha256_bytes(source_bytes)
            == record["decoded_rgb_sha256"],
            "replay_byte_count": len(replay_bytes) == len(source_bytes),
            "replay_bytes_equal": replay_bytes == source_bytes,
            "replay_hash_equal": sha256_bytes(replay_bytes)
            == record["scan_record_canonical_sha256"],
            "declared_zero_difference": (
                record["changed_pixels"] == 0
                and record["max_rgb_delta"] == 0
                and record["pixel_exact"] is True
            ),
        }
        checks.update(
            {
                f"{source_id}_{name}": passed
                for name, passed in source_checks.items()
            }
        )
        observed[source_id] = {
            "width": width,
            "height": height,
            "rgb_bytes": len(replay_bytes),
            "decoded_rgb_sha256": sha256_bytes(replay_bytes),
        }
    checks.update(
        {
            "source_count_seven": len(lock["approved_sources"]) == 7,
            "metric_source_count_six": sum(
                bool(record["metric"]) for record in lock["approved_sources"]
            )
            == 6,
            "only_170_cm_scale_anchor": lock["scale_authority"][
                "overall_length_cm"
            ]
            == 170,
            "other_dimensions_deferred": "derive"
            in lock["scale_authority"]["all_other_dimensions"],
            "source_bytes_unmodified": lock["source_bytes_modified"] is False,
            "no_later_stage_output": lock[
                "crop_mask_measurement_interpretation_or_geometry_created"
            ]
            is False,
        }
    )
    result = "PASS" if all(checks.values()) else "FAIL"
    audit = {
        "schema": "AERATHEA_STEP02_INDEPENDENT_AUDIT_V1",
        "run_id": lock["run_id"],
        "artifact_status": "proof only",
        "builder_not_imported": True,
        "scan_records_replayed_directly": True,
        "observed": observed,
        "checks": checks,
        "pass_count": sum(checks.values()),
        "check_count": len(checks),
        "result": result,
    }
    OUTPUT.write_text(json.dumps(audit, indent=2) + "\n")
    print(
        json.dumps(
            {
                "result": result,
                "checks": f"{sum(checks.values())}/{len(checks)}",
                "output": str(OUTPUT),
                "failures": [name for name, value in checks.items() if not value],
            },
            indent=2,
        )
    )
    if result != "PASS":
        raise RuntimeError("Step 02 independent audit failed")


if __name__ == "__main__":
    main()
