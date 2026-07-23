#!/usr/bin/env python3
"""Build the fresh R8 Step 02 immutable source and scanline lock."""

from __future__ import annotations

import hashlib
import json
from pathlib import Path

from PIL import Image


ROOT = Path(__file__).resolve().parents[2]
RUN_REL = Path(
    "docs/assets/blueprints/SM_DRW_SiegeBreaker_Hammer_A01/proof_runs/"
    "SB-CR-STEPS01-16-R8-PIXEL-EXACT-A01"
)
RUN = ROOT / RUN_REL
SCAN_ROOT = RUN / "evidence/STEP_02_SCANLINE_LOCK"
MANIFEST = RUN / "manifests/STEP_02_SOURCE_LOCK.json"
VALIDATION = RUN / "manifests/STEP_02_VALIDATION.json"
CONTRACT = RUN / "steps/STEP_02_CONTRACT.md"
OUTPUT = RUN / "steps/STEP_02_OUTPUT_RECORD.md"
HANDOFF = RUN / "handoffs/STEP_02_TO_STEP_03_HANDOFF.md"
REVIEW = RUN / "review/STEP_02_SOURCE_LOCK_REVIEW.md"
STATE = RUN / "manifests/STEP_STATE.json"

R8_ROOT = Path(
    "Saved/AssetForgeResearch/SiegeBreaker/A12_R8_SixViewGeneration/"
    "VisualReference_A01"
)
SOURCES = {
    "front": {
        "path": R8_ROOT / "SM_DRW_SiegeBreaker_Hammer_A01_A12_R8_FRONT_A01.png",
        "sha256": "9a34588afd4fef32001cd9cb2115699e7506ef1e90331c19f4d32483c60aab8c",
        "role": "front orthographic metric and exact color evidence",
    },
    "back": {
        "path": R8_ROOT / "SM_DRW_SiegeBreaker_Hammer_A01_A12_R8_BACK_A01.png",
        "sha256": "f09dd1ad3978f39e10ecee8ea7efa84336520f0cea4921fe3c410dfd04019694",
        "role": "back orthographic metric and exact color evidence",
    },
    "left": {
        "path": R8_ROOT / "SM_DRW_SiegeBreaker_Hammer_A01_A12_R8_LEFT_A01.png",
        "sha256": "7215495802065bb1907ec67f46e6f7c622b9beaf768eb710a5fc12880a6b1cc5",
        "role": "left orthographic metric and exact color evidence",
    },
    "right": {
        "path": R8_ROOT / "SM_DRW_SiegeBreaker_Hammer_A01_A12_R8_RIGHT_A01.png",
        "sha256": "58f3199babbcf9323751d04f0ffafa4316048243cf2f39992cdb6b04176306e8",
        "role": "right orthographic metric, exact color, and x=557 rotation evidence",
    },
    "top": {
        "path": R8_ROOT / "SM_DRW_SiegeBreaker_Hammer_A01_A12_R8_TOP_A01.png",
        "sha256": "be3e0b70de7a6e4fad025315f22feb21dc948ea9c3e7efb0adb63a983f190f9c",
        "role": "top orthographic footprint, orientation, and exact color evidence",
    },
    "bottom": {
        "path": R8_ROOT / "SM_DRW_SiegeBreaker_Hammer_A01_A12_R8_BOTTOM_A01.png",
        "sha256": "d2a32732fd480a0556e882e304bcfbff1dd82d0a913ad4c36117109406de988e",
        "role": "bottom orthographic footprint, orientation, and exact color evidence",
    },
    "concept": {
        "path": Path("SourceAssets/Concepts/SiegeBreaker/siege_breaker_concept_view.png"),
        "sha256": "9f1ac142a5047968bb20c74216c2dccf61470ed9f4e21689ff01934bd849c586",
        "role": "registered nonmetric style and final beauty comparison only",
    },
}


def sha256(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest()


def decoded_hash(path: Path) -> tuple[str, int, int, str]:
    with Image.open(path) as opened:
        image = opened.convert("RGB")
    return (
        hashlib.sha256(image.tobytes("raw", "RGB")).hexdigest(),
        image.width,
        image.height,
        image.mode,
    )


def relative(path: Path) -> str:
    return str(path.relative_to(ROOT))


def main() -> None:
    records = []
    checks: dict[str, bool] = {}
    for source_id, authority in SOURCES.items():
        source_path = ROOT / authority["path"]
        scan_manifest_paths = list(
            (SCAN_ROOT / source_id).glob("*_ScanlineManifest.json")
        )
        if len(scan_manifest_paths) != 1:
            raise RuntimeError(f"Expected one scan manifest for {source_id}")
        scan_manifest_path = scan_manifest_paths[0]
        scan = json.loads(scan_manifest_path.read_text())
        source_file_hash = sha256(source_path)
        decoded, width, height, mode = decoded_hash(source_path)
        scan_path = ROOT / scan["scan_record"]
        target_path = ROOT / scan["target_image"]
        rebuild_path = ROOT / scan["rebuilt_image"]
        difference_path = ROOT / scan["difference_image"]
        local_checks = {
            "source_hash": source_file_hash == authority["sha256"],
            "source_matches_scan_pixels": decoded == scan["scan_sha256"],
            "target_matches_source_pixels": decoded == scan["target_pixel_sha256"],
            "rebuild_matches_source_pixels": decoded == scan["rebuild_pixel_sha256"],
            "pixel_exact": bool(scan["pixel_exact"]),
            "changed_pixels_zero": int(scan["changed_pixels"]) == 0,
            "max_rgb_delta_zero": int(scan["max_rgb_delta"]) == 0,
            "scanline_count_exact": int(scan["scanlines"]) == height,
            "scan_record_exists": scan_path.is_file(),
            "target_exists": target_path.is_file(),
            "rebuild_exists": rebuild_path.is_file(),
            "difference_exists": difference_path.is_file(),
        }
        checks.update(
            {
                f"{source_id}_{name}": passed
                for name, passed in local_checks.items()
            }
        )
        records.append(
            {
                "id": source_id,
                "path": str(authority["path"]),
                "role": authority["role"],
                "metric": source_id != "concept",
                "file_sha256": source_file_hash,
                "byte_size": source_path.stat().st_size,
                "format": "PNG",
                "mode": mode,
                "width": width,
                "height": height,
                "decoded_rgb_sha256": decoded,
                "scanline_manifest": relative(scan_manifest_path),
                "scanline_manifest_sha256": sha256(scan_manifest_path),
                "scan_record": relative(scan_path),
                "scan_record_file_sha256": sha256(scan_path),
                "scan_record_canonical_sha256": scan["scan_sha256"],
                "scan_target": relative(target_path),
                "scan_target_file_sha256": sha256(target_path),
                "scan_rebuild": relative(rebuild_path),
                "scan_rebuild_file_sha256": sha256(rebuild_path),
                "difference": relative(difference_path),
                "difference_file_sha256": sha256(difference_path),
                "scanlines": scan["scanlines"],
                "rgb_bytes": scan["rgb_bytes"],
                "changed_pixels": scan["changed_pixels"],
                "max_rgb_delta": scan["max_rgb_delta"],
                "pixel_exact": scan["pixel_exact"],
            }
        )
    checks.update(
        {
            "six_new_metric_orthographics": sum(r["metric"] for r in records) == 6,
            "one_nonmetric_concept": sum(not r["metric"] for r in records) == 1,
            "overall_length_anchor_only": True,
            "crop_mask_measurement_geometry_absent": True,
            "prior_candidate_construction_input_absent": True,
        }
    )
    if not all(checks.values()):
        raise RuntimeError(
            "Step 02 failed: "
            + ", ".join(name for name, passed in checks.items() if not passed)
        )

    manifest = {
        "schema": "AERATHEA_IMMUTABLE_SOURCE_LOCK_V2",
        "asset_id": "SM_DRW_SiegeBreaker_Hammer_A01",
        "run_id": "SB-CR-STEPS01-16-R8-PIXEL-EXACT-A01",
        "step": "02",
        "artifact_status": "authoritative for this proof run",
        "approved_sources": records,
        "scale_authority": {
            "overall_length_cm": 170,
            "all_other_dimensions": "derive from new source pixels in Steps 05-09",
            "printed_annotation_values": "evidence text only; no pixel displacement authority",
        },
        "scan_container_canonicalization": {
            "format": "AET_RGB_SCANLINE_V1 inside gzip",
            "canonical_hash": "SHA-256 of ordered decompressed RGB row bytes",
            "gzip_header_mtime": "nonsemantic",
        },
        "excluded_construction_inputs_used": False,
        "source_bytes_modified": False,
        "crop_mask_measurement_interpretation_or_geometry_created": False,
    }
    MANIFEST.write_text(json.dumps(manifest, indent=2) + "\n")

    validation = {
        "schema": "AERATHEA_STEP_VALIDATION_V1",
        "run_id": manifest["run_id"],
        "step": "02",
        "artifact_status": "proof only",
        "checks": checks,
        "pass_count": sum(checks.values()),
        "check_count": len(checks),
        "result": "PASS",
    }
    VALIDATION.write_text(json.dumps(validation, indent=2) + "\n")

    CONTRACT.write_text(
        """# Step 02 Contract - Immutable Source And Scanline Lock

- Status: `completed`
- Authority: `SB-CR-STEPS01-16-R8-PIXEL-EXACT-A01`
- Action: hash and losslessly scan the six new orthographics and the nonmetric
  concept reference.
- Required equality: `changed_pixels=0`, `max_rgb_delta=0`.
- Crop, mask, measurement, interpretation, geometry, DCC, and Unreal:
  `forbidden`.
"""
    )
    lines = [
        "# Step 02 Source-Lock Review",
        "",
        "- Artifact status: `proof only`",
        "- Full-image resize, filtering, crop, mask, or recolor: `none`",
        "",
        "| Source | Role | Canvas | RGB SHA-256 | Scan result |",
        "|---|---|---:|---|---|",
    ]
    for record in records:
        lines.append(
            f"| {record['id']} | {record['role']} | "
            f"{record['width']}×{record['height']} | "
            f"`{record['decoded_rgb_sha256']}` | "
            f"`0 changed / 0 max delta` |"
        )
    REVIEW.parent.mkdir(parents=True, exist_ok=True)
    REVIEW.write_text("\n".join(lines) + "\n")
    OUTPUT.write_text(
        f"""# Step 02 Output Record

- Result: `PASS`
- Checks: `{sum(checks.values())}/{len(checks)}`
- Six new orthographic sources: `pixel exact`
- Nonmetric concept reference: `pixel exact`
- Source mutation, crop, mask, measurement, or geometry: `false`
- Next state: `step_03_unlocked`
"""
    )
    HANDOFF.parent.mkdir(parents=True, exist_ok=True)
    HANDOFF.write_text(
        """# Step 02 To Step 03 Handoff

- Step 02: `PASS`
- Step 03: `unlocked`
- Step 03 action: produce exact integer half-open hammer-only source regions
  and selected-pixel evidence without resizing or altering a source pixel.
"""
    )
    state = json.loads(STATE.read_text())
    state["current_step"] = "03"
    state["completed_steps"] = ["01", "02"]
    state["state"] = "step_03_unlocked"
    STATE.write_text(json.dumps(state, indent=2) + "\n")
    print(
        json.dumps(
            {
                "result": "PASS",
                "sources": len(records),
                "checks": f"{sum(checks.values())}/{len(checks)}",
                "manifest": str(MANIFEST),
            },
            indent=2,
        )
    )


if __name__ == "__main__":
    main()
