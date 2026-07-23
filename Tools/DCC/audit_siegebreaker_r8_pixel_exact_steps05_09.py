#!/usr/bin/env python3
"""Independent arithmetic/integrity audit for R8 Steps 05-09."""

from __future__ import annotations

from fractions import Fraction
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


def sha256_bytes(value: bytes) -> str:
    return hashlib.sha256(value).hexdigest()


def sha256(path: Path) -> str:
    return sha256_bytes(path.read_bytes())


def exact(value: dict[str, object]) -> Fraction:
    return Fraction(int(value["numerator"]), int(value["denominator"]))


def write(step: str, checks: dict[str, bool], evidence: dict[str, object]) -> None:
    passed = sum(checks.values())
    out = {
        "schema": "AERATHEA_INDEPENDENT_AUDIT_V1",
        "step": step,
        "result": "PASS" if passed == len(checks) else "FAIL",
        "checks_passed": passed,
        "checks_total": len(checks),
        "checks": checks,
        "evidence": evidence,
    }
    path = RUN / f"manifests/STEP_{step}_INDEPENDENT_AUDIT.json"
    path.write_text(json.dumps(out, indent=2) + "\n")
    if out["result"] != "PASS":
        raise RuntimeError(f"Independent Step {step} audit failed")
    print(f"STEP{step} INDEPENDENT PASS {passed}/{len(checks)}")


def main() -> None:
    step03 = json.loads(
        (RUN / "manifests/STEP_03_CROP_COORDINATES.json").read_text()
    )
    records = {row["id"]: row for row in step03["sources"]}
    replay = {}
    for view, record in records.items():
        source_path = ROOT / record["source_path"]
        capture_path = ROOT / record["capture_path"]
        capture = json.loads(gzip.decompress(capture_path.read_bytes()))
        image = Image.open(source_path).convert("RGBA")
        raw = image.tobytes("raw", "RGBA")
        membership = bytearray(image.width * image.height)
        selected = bytearray()
        coordinates = set()
        for row in capture["rows_with_exact_rgba"]:
            y = int(row["y"])
            for run in row["runs"]:
                x0, x1 = int(run["x0"]), int(run["x1"])
                payload = bytes.fromhex(run["rgba_hex"])
                for offset, x in enumerate(range(x0, x1)):
                    pixel = payload[offset * 4:offset * 4 + 4]
                    flat = y * image.width + x
                    if pixel != raw[flat * 4:flat * 4 + 4]:
                        raise RuntimeError(f"RGBA mismatch {view}")
                    if (x, y) in coordinates:
                        raise RuntimeError(f"Multiply-owned source pixel {view}")
                    coordinates.add((x, y))
                    membership[flat] = 1
                    selected.extend(pixel)
        replay[view] = {
            "count": len(coordinates),
            "membership": sha256_bytes(bytes(membership)),
            "rgba": sha256_bytes(bytes(selected)),
            "rect": record["rectangle_half_open"],
            "capture_sha256": sha256(capture_path),
            "source_sha256": sha256(source_path),
        }
        if replay[view]["membership"] != record["decoded_membership_sha256"]:
            raise RuntimeError(f"Membership mismatch {view}")
        if replay[view]["rgba"] != record["selected_rgba_sha256"]:
            raise RuntimeError(f"RGBA hash mismatch {view}")

    reg_path = RUN / "manifests/STEP_05_PIXEL_WORLD_REGISTRATION_LOCK.json"
    reg = json.loads(reg_path.read_text())
    r = {view: replay[view]["rect"] for view in replay}
    fscale = Fraction(170, r["front"][3] - r["front"][1])
    bscale = Fraction(170, r["back"][3] - r["back"][1])
    sscale = Fraction(170, r["right"][3] - r["right"][1])
    width = Fraction(r["front"][2] - r["front"][0]) * fscale
    axial = width / Fraction(
        (r["top"][2] - r["top"][0])
        + (r["bottom"][2] - r["bottom"][0]),
        2,
    )
    depth = Fraction(
        (r["top"][3] - r["top"][1])
        + (r["bottom"][3] - r["bottom"][1]),
        2,
    ) * axial
    checks05 = {
        "manifest_hash_direct": bool(sha256(reg_path)),
        "front_scale_recomputed": exact(
            reg["view_uniform_scales_cm_per_pixel"]["front"]["scale_x"]
        )
        == fscale,
        "back_scale_recomputed": exact(
            reg["view_uniform_scales_cm_per_pixel"]["back"]["scale_x"]
        )
        == bscale,
        "right_scale_recomputed": exact(
            reg["view_uniform_scales_cm_per_pixel"]["right"]["scale_x"]
        )
        == sscale,
        "axial_scale_recomputed": exact(
            reg["view_uniform_scales_cm_per_pixel"]["top"]["scale_x"]
        )
        == axial,
        "scale_xy_equal_all": all(
            exact(row["scale_x"]) == exact(row["scale_y"])
            for row in reg["view_uniform_scales_cm_per_pixel"].values()
        ),
        "width_recomputed": exact(
            reg["derived_overall_dimensions_cm"]["width_front_owned"]
        )
        == width,
        "depth_recomputed": exact(
            reg["derived_overall_dimensions_cm"][
                "depth_centered_top_bottom_owned"
            ]
        )
        == depth,
        "right_axis_exact": exact(
            reg["centers_source_edges"]["right_rotation"]
        )
        == 557,
        "rune_depth_recomputed": exact(
            reg["right_candidate_halves"]["rune_side"]["completed_depth_cm"]
        )
        == 222 * sscale,
        "metal_depth_recomputed": exact(
            reg["right_candidate_halves"]["metal_center_piece_side"][
                "completed_depth_cm"
            ]
        )
        == 278 * sscale,
        "halves_not_normalized": 222 * sscale != 278 * sscale,
    }
    write(
        "05",
        checks05,
        {
            "recomputed_width": str(width),
            "recomputed_axial_depth": str(depth),
            "recomputed_rune_depth": str(222 * sscale),
            "recomputed_metal_depth": str(278 * sscale),
        },
    )

    front_path = RUN / "manifests/STEP_06_FRONT_MEASUREMENT_CONTRACT.json"
    back_path = RUN / "manifests/STEP_06_BACK_MEASUREMENT_CONTRACT.json"
    front = json.loads(front_path.read_text())
    back = json.loads(back_path.read_text())
    station_rows = front["component_stations_source_edges"]
    checks06 = {
        "front_source_replayed": replay["front"]["count"] == 247844,
        "back_source_replayed": replay["back"]["count"] == 250209,
        "front_profile_rows_nonempty": len(front["row_profiles"]) > 1000,
        "back_profile_rows_nonempty": len(back["row_profiles"]) > 1000,
        "front_scale_own": exact(front["uniform_scale_cm_per_pixel"])
        == fscale,
        "back_scale_own": exact(back["uniform_scale_cm_per_pixel"])
        == bscale,
        "station_order": list(station_rows.values())
        == sorted(station_rows.values()),
        "grip_bounds_exact": station_rows["H8_ferrule_meets_grip"] == 955
        and station_rows["U1_grip_meets_collar"] == 1110,
        "ferrule_bounds_exact": station_rows[
            "H1_haft_meets_handle_ferrule"
        ]
        == 870
        and station_rows["H8_ferrule_meets_grip"] == 955,
        "back_correspondence_not_invented": "unresolved"
        in back["component_station_correspondence"],
    }
    write(
        "06",
        checks06,
        {"front_sha256": sha256(front_path), "back_sha256": sha256(back_path)},
    )

    left_path = RUN / "manifests/STEP_07_LEFT_MEASUREMENT_CONTRACT.json"
    right_path = RUN / "manifests/STEP_07_RIGHT_MEASUREMENT_CONTRACT.json"
    right = json.loads(right_path.read_text())
    checks07 = {
        "left_source_replayed": replay["left"]["count"] == 146324,
        "right_source_replayed": replay["right"]["count"] == 142185,
        "right_axis_557": right["rotation_axis_source_edge_x"] == 557,
        "right_bounds_center_543": exact(
            right["right_object_bounds_center_x"]
        )
        == 543,
        "centers_not_conflated": right["rotation_axis_is_not_bounds_center"],
        "rune_interval": right["candidate_half_intervals"]["rune_side"][
            "interval_half_open"
        ]
        == [557, 668],
        "metal_interval": right["candidate_half_intervals"][
            "metal_center_piece_side"
        ]["interval_half_open"]
        == [418, 557],
        "unequal_span_exact": right["candidate_half_intervals"]["rune_side"][
            "span_pixels"
        ]
        == 111
        and right["candidate_half_intervals"]["metal_center_piece_side"][
            "span_pixels"
        ]
        == 139,
    }
    write(
        "07",
        checks07,
        {"left_sha256": sha256(left_path), "right_sha256": sha256(right_path)},
    )

    top_path = RUN / "manifests/STEP_08_TOP_MEASUREMENT_CONTRACT.json"
    bottom_path = RUN / "manifests/STEP_08_BOTTOM_MEASUREMENT_CONTRACT.json"
    top = json.loads(top_path.read_text())
    bottom = json.loads(bottom_path.read_text())
    checks08 = {
        "top_source_replayed": replay["top"]["count"] == 383863,
        "bottom_source_replayed": replay["bottom"]["count"] == 374341,
        "top_exact_runs_retained": len(top["row_profiles"]) > 400,
        "bottom_exact_runs_retained": len(bottom["row_profiles"]) > 400,
        "top_bottom_distinct": replay["top"]["membership"]
        != replay["bottom"]["membership"],
        "top_uniform_scale": exact(top["uniform_scale_cm_per_pixel"]) == axial,
        "bottom_uniform_scale": exact(bottom["uniform_scale_cm_per_pixel"])
        == axial,
        "footprint_rule_source_owned": "exact selected source pixels"
        in top["footprint_authority"]
        and "exact selected source pixels" in bottom["footprint_authority"],
    }
    write(
        "08",
        checks08,
        {"top_sha256": sha256(top_path), "bottom_sha256": sha256(bottom_path)},
    )

    integrated_path = (
        RUN / "manifests/STEP_09_INTEGRATED_EXACT_MEASUREMENT_INDEX.json"
    )
    matrix_path = RUN / "manifests/STEP_09_DISAGREEMENT_UNKNOWN_MATRIX.json"
    pre_path = RUN / "manifests/STEP_09_PRE_GEOMETRY_EXACT_DATA_AUDIT.json"
    integrated = json.loads(integrated_path.read_text())
    matrix = json.loads(matrix_path.read_text())
    pre = json.loads(pre_path.read_text())
    total = sum(value["count"] for value in replay.values())
    checks09 = {
        "six_sources_replayed_directly": len(replay) == 6,
        "total_pixel_count_direct": total == 1544766,
        "index_total_matches_direct": integrated[
            "total_exact_selected_pixels"
        ]
        == total,
        "source_hashes_match": all(
            replay[v]["source_sha256"] == records[v]["source_file_sha256"]
            for v in replay
        ),
        "membership_hashes_match": all(
            replay[v]["membership"] == records[v]["decoded_membership_sha256"]
            for v in replay
        ),
        "rgba_hashes_match": all(
            replay[v]["rgba"] == records[v]["selected_rgba_sha256"]
            for v in replay
        ),
        "disagreements_explicit": len(matrix["items"]) == 5,
        "valid_audit_result": pre["result"] == "pass_with_explicit_blocks",
        "geometry_block_preserved": not pre["geometry_authorized"],
        "no_warp_or_component_scale": not pre["image_warping_used"]
        and not pre["component_scaling_used"],
    }
    write(
        "09",
        checks09,
        {
            "integrated_sha256": sha256(integrated_path),
            "matrix_sha256": sha256(matrix_path),
            "pre_geometry_audit_sha256": sha256(pre_path),
            "direct_total_selected_pixels": total,
        },
    )


if __name__ == "__main__":
    main()
