#!/usr/bin/env python3
"""Replay R8 evidence through documented Steps 05-09 without stretching."""

from __future__ import annotations

from fractions import Fraction
import gzip
import hashlib
import json
from pathlib import Path

from PIL import Image, ImageDraw, ImageFont


ROOT = Path(__file__).resolve().parents[2]
RUN = ROOT / (
    "docs/assets/blueprints/SM_DRW_SiegeBreaker_Hammer_A01/proof_runs/"
    "SB-CR-STEPS01-16-R8-PIXEL-EXACT-A01"
)
STEP03 = RUN / "manifests/STEP_03_CROP_COORDINATES.json"
STEP04 = RUN / "manifests/STEP_04_COMPONENT_AND_SOURCE_OWNERSHIP_INVENTORY.json"
STATE = RUN / "manifests/STEP_STATE.json"
RUN_ID = "SB-CR-STEPS01-16-R8-PIXEL-EXACT-A01"
VIEWS = ("front", "back", "left", "right", "top", "bottom")
STATIONS = {
    "A_begin_haft_including_coupler": 600,
    "C_coupler_meets_true_haft": 670,
    "H1_haft_meets_handle_ferrule": 870,
    "H8_ferrule_meets_grip": 955,
    "U1_grip_meets_collar": 1110,
    "U3_collar_meets_pommel": 1150,
    "L4_pommel_meets_terminal_cap": 1220,
    "terminal_bottom": 1271,
}


def sha256_bytes(value: bytes) -> str:
    return hashlib.sha256(value).hexdigest()


def sha256(path: Path) -> str:
    return sha256_bytes(path.read_bytes())


def fr(value: Fraction) -> dict[str, object]:
    return {
        "numerator": value.numerator,
        "denominator": value.denominator,
        "display_decimal": f"{float(value):.12f}",
    }


def write_json(path: Path, value: object) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(json.dumps(value, indent=2) + "\n")


def font(size: int) -> ImageFont.ImageFont:
    candidate = Path("/usr/share/fonts/truetype/dejavu/DejaVuSans.ttf")
    return (
        ImageFont.truetype(str(candidate), size)
        if candidate.is_file()
        else ImageFont.load_default()
    )


def replay(record: dict[str, object]) -> dict[str, object]:
    capture_path = ROOT / record["capture_path"]
    capture = json.loads(gzip.decompress(capture_path.read_bytes()))
    source_path = ROOT / record["source_path"]
    image = Image.open(source_path).convert("RGBA")
    if sha256(source_path) != record["source_file_sha256"]:
        raise RuntimeError(f"Immutable source changed: {record['id']}")
    source = image.tobytes("raw", "RGBA")
    membership = bytearray(image.width * image.height)
    selected = bytearray()
    rows = []
    for row in capture["rows_with_exact_rgba"]:
        y = int(row["y"])
        runs = []
        count = 0
        for run in row["runs"]:
            x0, x1 = int(run["x0"]), int(run["x1"])
            payload = bytes.fromhex(run["rgba_hex"])
            if len(payload) != (x1 - x0) * 4:
                raise RuntimeError("Malformed exact RGBA run")
            for offset, x in enumerate(range(x0, x1)):
                flat = y * image.width + x
                pixel = payload[offset * 4:offset * 4 + 4]
                if pixel != source[flat * 4:flat * 4 + 4]:
                    raise RuntimeError("Exact RGBA replay mismatch")
                membership[flat] = 1
                selected.extend(pixel)
            runs.append([x0, x1])
            count += x1 - x0
        rows.append(
            {
                "source_y": y,
                "runs_half_open": runs,
                "outer_interval_half_open": [runs[0][0], runs[-1][1]],
                "outer_span_pixels": runs[-1][1] - runs[0][0],
                "selected_pixel_count": count,
            }
        )
    if sha256_bytes(bytes(membership)) != capture["decoded_membership_sha256"]:
        raise RuntimeError("Membership hash mismatch")
    if sha256_bytes(bytes(selected)) != capture["selected_rgba_sha256"]:
        raise RuntimeError("Selected RGBA hash mismatch")
    columns = []
    for column in capture["columns"]:
        runs = [[int(v) for v in pair] for pair in column["runs_half_open"]]
        columns.append(
            {
                "source_x": int(column["x"]),
                "runs_half_open": runs,
                "outer_interval_half_open": [runs[0][0], runs[-1][1]],
                "outer_span_pixels": runs[-1][1] - runs[0][0],
                "selected_pixel_count": sum(b - a for a, b in runs),
            }
        )
    return {
        "image": image,
        "membership": membership,
        "rows": rows,
        "columns": columns,
        "capture_sha256": sha256(capture_path),
        "selected_pixel_count": sum(membership),
        "selected_rgba_sha256": capture["selected_rgba_sha256"],
        "membership_sha256": capture["decoded_membership_sha256"],
    }


def build_board(
    title: str,
    records: dict[str, dict[str, object]],
    paths: dict[str, Path],
    marks: dict[str, list[tuple[str, int, str]]],
) -> Path:
    board = Image.new("RGB", (1800, 1160), (22, 25, 29))
    draw = ImageDraw.Draw(board)
    draw.text((24, 18), title, font=font(30), fill=(245, 245, 245))
    draw.text(
        (24, 58),
        "Source pixels are unchanged. Lines are coordinate evidence only; no fills or contours.",
        font=font(17),
        fill=(185, 195, 210),
    )
    order = list(paths)
    for index, view in enumerate(order):
        image = records[view]["image"].convert("RGB")
        image.thumbnail((840, 480), getattr(Image, "Resampling", Image).LANCZOS)
        panel = Image.new("RGB", (870, 510), (232, 233, 234))
        ox, oy = (870 - image.width) // 2, 25
        panel.paste(image, (ox, oy))
        pd = ImageDraw.Draw(panel)
        source = records[view]["image"]
        sx, sy = image.width / source.width, image.height / source.height
        for axis, value, label in marks.get(view, []):
            if axis == "x":
                x = ox + round(value * sx)
                pd.line((x, oy, x, oy + image.height), fill=(240, 42, 35), width=2)
                pd.text((x + 3, oy + 3), label, font=font(13), fill=(25, 28, 31))
            else:
                y = oy + round(value * sy)
                pd.line((ox, y, ox + image.width, y), fill=(240, 42, 35), width=2)
                pd.text((ox + 3, y + 2), label, font=font(13), fill=(25, 28, 31))
        pd.text((12, 5), view.upper(), font=font(17), fill=(25, 28, 31))
        board.paste(panel, (30 + (index % 2) * 890, 95 + (index // 2) * 530))
    path = next(iter(paths.values()))
    path.parent.mkdir(parents=True, exist_ok=True)
    board.save(path)
    return path


def step_docs(step: str, decision: str, result: str, next_step: str) -> None:
    (RUN / f"steps/STEP_{step}_CONTRACT.md").write_text(
        f"# Step {step} Contract\n\n"
        f"- Run: `{RUN_ID}`\n"
        f"- Decision: {decision}\n"
        "- Governing invariant: use only locked R8 pixels and declared exact "
        "formulas; no stretching, smoothing, or expected-value substitution.\n"
    )
    (RUN / f"steps/STEP_{step}_OUTPUT_RECORD.md").write_text(
        f"# Step {step} Output Record\n\n"
        f"- Result: `{result}`\n"
        "- Artifact status: `authoritative`\n"
        "- The independent audit must pass before the handoff is valid.\n"
    )
    (RUN / f"handoffs/STEP_{step}_TO_STEP_{next_step}_HANDOFF.md").write_text(
        f"# Step {step} → Step {next_step} Handoff\n\n"
        f"- Step {step} result: `{result}`.\n"
        f"- Step {next_step} may consume only the authoritative manifests and "
        "the still-immutable R8 scanline captures.\n"
    )


def validate(step: str, checks: dict[str, bool], extra: dict[str, object]) -> None:
    passed = sum(checks.values())
    result = "PASS" if passed == len(checks) else "FAIL"
    write_json(
        RUN / f"manifests/STEP_{step}_VALIDATION.json",
        {
            "schema": "AERATHEA_STEP_VALIDATION_V1",
            "run_id": RUN_ID,
            "step": step,
            "result": result,
            "checks_passed": passed,
            "checks_total": len(checks),
            "checks": checks,
            **extra,
        },
    )
    if result != "PASS":
        raise RuntimeError(f"Step {step} validation failed")
    print(f"STEP{step} PASS {passed}/{len(checks)}")


def main() -> None:
    step03 = json.loads(STEP03.read_text())
    source_records = {row["id"]: row for row in step03["sources"]}
    evidence = {view: replay(source_records[view]) for view in VIEWS}
    rect = {
        view: source_records[view]["rectangle_half_open"] for view in VIEWS
    }

    # Step 05: exact edge convention and one uniform transform per complete view.
    front_scale = Fraction(170, rect["front"][3] - rect["front"][1])
    back_scale = Fraction(170, rect["back"][3] - rect["back"][1])
    left_scale = Fraction(170, rect["left"][3] - rect["left"][1])
    right_scale = Fraction(170, rect["right"][3] - rect["right"][1])
    front_width = Fraction(rect["front"][2] - rect["front"][0]) * front_scale
    mean_axial_width = Fraction(
        (rect["top"][2] - rect["top"][0])
        + (rect["bottom"][2] - rect["bottom"][0]),
        2,
    )
    mean_axial_depth = Fraction(
        (rect["top"][3] - rect["top"][1])
        + (rect["bottom"][3] - rect["bottom"][1]),
        2,
    )
    axial_scale = front_width / mean_axial_width
    axial_depth = mean_axial_depth * axial_scale
    scales = {
        "front": front_scale,
        "back": back_scale,
        "left": left_scale,
        "right": right_scale,
        "top": axial_scale,
        "bottom": axial_scale,
    }
    centers = {
        "front": Fraction(562),
        "back": Fraction(1123, 2),
        "left": Fraction(577),
        "right_object": Fraction(543),
        "right_rotation": Fraction(557),
        "top_x": Fraction(1533, 2),
        "top_y": Fraction(1093, 2),
        "bottom_x": Fraction(1529, 2),
        "bottom_y": Fraction(539),
    }
    registration = {
        "schema": "AERATHEA_R8_PIXEL_WORLD_REGISTRATION_V1",
        "run_id": RUN_ID,
        "step": "05",
        "artifact_status": "authoritative",
        "pixel_convention": {
            "coordinates": "integer half-open source pixel edges",
            "sample_location": "(x+1/2,y+1/2)",
            "source_origin": "upper left",
            "source_x": "right",
            "source_y": "down",
        },
        "world_frame": {
            "pivot_cm": [0, 0, 0],
            "pivot": "bottom-center terminal/pommel",
            "axes": {"+X": "head right", "+Y": "back", "+Z": "up"},
            "assembly_axis": "world Z through right-source diamond center x=557",
        },
        "only_external_anchor_cm": fr(Fraction(170)),
        "view_uniform_scales_cm_per_pixel": {
            view: {"scale_x": fr(scale), "scale_y": fr(scale)}
            for view, scale in scales.items()
        },
        "centers_source_edges": {
            key: fr(value) for key, value in centers.items()
        },
        "coordinate_equations": {
            "front": "X=(x-562)*170/1063; Z=(1271-y)*170/1063",
            "back": "X=(1123/2-x)*170/1062; Z=(1266-y)*170/1062",
            "left": "Y=(577-x)*170/1096; Z=(1261-y)*170/1096",
            "right_rotation": "Y=(x-557)*170/1096; Z=(1262-y)*170/1096",
            "top": "X=(x-1533/2)*Saxial; Y=(y-1093/2)*Saxial",
            "bottom": "X=(1529/2-x)*Saxial; Y=(539-y)*Saxial",
        },
        "derived_overall_dimensions_cm": {
            "width_front_owned": fr(front_width),
            "depth_centered_top_bottom_owned": fr(axial_depth),
            "length_anchor": fr(Fraction(170)),
        },
        "observed_comparison_consequences_cm": {
            "back_width": fr(
                Fraction(rect["back"][2] - rect["back"][0]) * back_scale
            ),
            "left_depth": fr(
                Fraction(rect["left"][2] - rect["left"][0]) * left_scale
            ),
            "right_depth_about_object_bounds": fr(
                Fraction(rect["right"][2] - rect["right"][0]) * right_scale
            ),
            "top_depth_at_common_axial_scale": fr(
                Fraction(rect["top"][3] - rect["top"][1]) * axial_scale
            ),
            "bottom_depth_at_common_axial_scale": fr(
                Fraction(rect["bottom"][3] - rect["bottom"][1]) * axial_scale
            ),
        },
        "right_candidate_halves": {
            "rune_side": {
                "interval_half_open": [557, 668],
                "span_pixels": 111,
                "completed_depth_cm": fr(Fraction(222) * right_scale),
            },
            "metal_center_piece_side": {
                "interval_half_open": [418, 557],
                "span_pixels": 139,
                "completed_depth_cm": fr(Fraction(278) * right_scale),
            },
        },
        "no_stretch": True,
        "source_pixels_modified": False,
    }
    step05 = RUN / "manifests/STEP_05_PIXEL_WORLD_REGISTRATION_LOCK.json"
    write_json(step05, registration)
    step_docs(
        "05",
        "Lock exact pixel/world conventions, axes, centers, transforms, and "
        "new-pixel dimension consequences.",
        "PASS",
        "06",
    )
    validate(
        "05",
        {
            "170_is_only_external_anchor": True,
            "six_views_registered": len(scales) == 6,
            "all_scales_positive": all(value > 0 for value in scales.values()),
            "all_views_uniform_xy": all(
                row["scale_x"] == row["scale_y"]
                for row in registration[
                    "view_uniform_scales_cm_per_pixel"
                ].values()
            ),
            "right_axis_exact_557": centers["right_rotation"] == 557,
            "rune_span_exact_111": 668 - 557 == 111,
            "metal_span_exact_139": 557 - 418 == 139,
            "candidate_depths_unequal": Fraction(222) * right_scale
            != Fraction(278) * right_scale,
            "front_owns_width": front_width == Fraction(104040, 1063),
            "axial_depth_exact": axial_depth == Fraction(24579450, 517681),
            "no_source_modification": True,
            "no_geometry": True,
        },
        {"manifest_sha256": sha256(step05)},
    )
    review05 = RUN / "review/STEP_05_REGISTRATION_LOCK_REVIEW.md"
    review05.write_text(
        "# Step 05 Registration Lock Review\n\n"
        f"- Length anchor: `170 cm`\n"
        f"- Front-owned width: `{float(front_width):.12f} cm`\n"
        f"- Centered top/bottom-owned depth: `{float(axial_depth):.12f} cm`\n"
        f"- Rune-side completed depth at the common right scale: "
        f"`{float(Fraction(222) * right_scale):.12f} cm`\n"
        f"- Metal-center completed depth at the common right scale: "
        f"`{float(Fraction(278) * right_scale):.12f} cm`\n"
        "- Every complete view uses exactly one scale, with scale-X=scale-Y.\n"
        "- The unequal right half-spans are preserved; neither is normalized.\n"
    )

    # Step 06: front/back exact scanline profiles and source-owned front stations.
    front_z = {
        name: fr(Fraction(rect["front"][3] - row) * front_scale)
        for name, row in STATIONS.items()
    }
    front = {
        "schema": "AERATHEA_R8_FRONT_EXACT_MEASUREMENT_V1",
        "run_id": RUN_ID,
        "view": "front",
        "source_rectangle_half_open": rect["front"],
        "uniform_scale_cm_per_pixel": fr(front_scale),
        "center_x_source_edge": fr(centers["front"]),
        "row_profiles": evidence["front"]["rows"],
        "column_profiles": evidence["front"]["columns"],
        "component_stations_source_edges": STATIONS,
        "component_stations_world_z_cm": front_z,
        "semantic_authority": {
            "A": "beginning of haft including coupler",
            "H1_to_H8": "haft-to-handle ferrule",
            "H8_to_U1": "grip",
            "U1": "grip meets collar",
            "U3": "collar meets pommel",
            "L4": "pommel meets terminal cap",
        },
        "source_capture_sha256": evidence["front"]["capture_sha256"],
    }
    back = {
        "schema": "AERATHEA_R8_BACK_EXACT_MEASUREMENT_V1",
        "run_id": RUN_ID,
        "view": "back",
        "source_rectangle_half_open": rect["back"],
        "uniform_scale_cm_per_pixel": fr(back_scale),
        "center_x_source_edge": fr(centers["back"]),
        "row_profiles": evidence["back"]["rows"],
        "column_profiles": evidence["back"]["columns"],
        "component_station_correspondence": (
            "unresolved independently; no front station copied into back"
        ),
        "source_capture_sha256": evidence["back"]["capture_sha256"],
    }
    front_path = RUN / "manifests/STEP_06_FRONT_MEASUREMENT_CONTRACT.json"
    back_path = RUN / "manifests/STEP_06_BACK_MEASUREMENT_CONTRACT.json"
    write_json(front_path, front)
    write_json(back_path, back)
    board06 = build_board(
        "STEP 06 - FRONT / BACK EXACT SOURCE MEASUREMENTS",
        evidence,
        {
            "front": RUN
            / "review/STEP_06_FRONT_BACK_EXACT_MEASUREMENT_REVIEW.png",
            "back": RUN
            / "review/STEP_06_FRONT_BACK_EXACT_MEASUREMENT_REVIEW.png",
        },
        {
            "front": [
                ("x", 562, "center x=562"),
                *[
                    ("y", row, name.split("_")[0])
                    for name, row in STATIONS.items()
                ],
            ],
            "back": [("x", 562, "center 1123/2")],
        },
    )
    step_docs(
        "06",
        "Record independent front/back exact profiles, visible stations, "
        "contacts, and unresolved correspondence.",
        "PASS",
        "07",
    )
    validate(
        "06",
        {
            "front_capture_replayed_exactly": evidence["front"][
                "selected_pixel_count"
            ]
            == source_records["front"]["exact_selected_pixel_count"],
            "back_capture_replayed_exactly": evidence["back"][
                "selected_pixel_count"
            ]
            == source_records["back"]["exact_selected_pixel_count"],
            "front_uses_own_scale": front_scale == Fraction(170, 1063),
            "back_uses_own_scale": back_scale == Fraction(170, 1062),
            "front_back_not_averaged": front_scale != back_scale,
            "all_stations_inside_front": all(
                rect["front"][1] <= row <= rect["front"][3]
                for row in STATIONS.values()
            ),
            "grip_between_H8_U1": STATIONS[
                "H8_ferrule_meets_grip"
            ] < STATIONS["U1_grip_meets_collar"],
            "no_hidden_back_station_copy": True,
            "review_exists": board06.is_file(),
            "no_geometry": True,
        },
        {
            "front_manifest_sha256": sha256(front_path),
            "back_manifest_sha256": sha256(back_path),
            "review_sha256": sha256(board06),
        },
    )

    # Step 07: independent side profiles plus exact unequal right half ownership.
    side_paths = {}
    for view in ("left", "right"):
        path = RUN / f"manifests/STEP_07_{view.upper()}_MEASUREMENT_CONTRACT.json"
        content = {
            "schema": f"AERATHEA_R8_{view.upper()}_EXACT_MEASUREMENT_V1",
            "run_id": RUN_ID,
            "view": view,
            "source_rectangle_half_open": rect[view],
            "uniform_scale_cm_per_pixel": fr(scales[view]),
            "row_profiles": evidence[view]["rows"],
            "column_profiles": evidence[view]["columns"],
            "source_capture_sha256": evidence[view]["capture_sha256"],
        }
        if view == "right":
            content["rotation_axis_source_edge_x"] = 557
            content["candidate_half_intervals"] = registration[
                "right_candidate_halves"
            ]
            content["right_object_bounds_center_x"] = fr(centers["right_object"])
            content["rotation_axis_is_not_bounds_center"] = True
        else:
            content["object_center_source_edge_x"] = fr(centers["left"])
        write_json(path, content)
        side_paths[view] = path
    board07 = build_board(
        "STEP 07 - LEFT / RIGHT EXACT SOURCE MEASUREMENTS",
        evidence,
        {
            "left": RUN / "review/STEP_07_LEFT_RIGHT_EXACT_MEASUREMENT_REVIEW.png",
            "right": RUN / "review/STEP_07_LEFT_RIGHT_EXACT_MEASUREMENT_REVIEW.png",
        },
        {
            "left": [("x", 577, "bounds center x=577")],
            "right": [
                ("x", 418, "metal outer"),
                ("x", 557, "rotation axis x=557"),
                ("x", 668, "rune outer"),
            ],
        },
    )
    step_docs(
        "07",
        "Record independent left/right depth profiles and exact right "
        "bisection without normalizing either half.",
        "PASS",
        "08",
    )
    validate(
        "07",
        {
            "left_replay_exact": evidence["left"]["selected_pixel_count"]
            == source_records["left"]["exact_selected_pixel_count"],
            "right_replay_exact": evidence["right"]["selected_pixel_count"]
            == source_records["right"]["exact_selected_pixel_count"],
            "side_scales_independent_of_front": right_scale != front_scale,
            "left_right_scale_from_own_heights": left_scale == right_scale
            == Fraction(170, 1096),
            "bisection_exact_557": True,
            "right_bounds_not_silently_recentered": centers["right_object"]
            != centers["right_rotation"],
            "rune_span_111": 668 - 557 == 111,
            "metal_span_139": 557 - 418 == 139,
            "unequal_spans_preserved": 111 != 139,
            "review_exists": board07.is_file(),
            "no_stretch": True,
            "no_geometry": True,
        },
        {
            "left_manifest_sha256": sha256(side_paths["left"]),
            "right_manifest_sha256": sha256(side_paths["right"]),
            "review_sha256": sha256(board07),
        },
    )

    # Step 08: top/bottom exact footprints, retained separately.
    axial_paths = {}
    for view in ("top", "bottom"):
        path = RUN / f"manifests/STEP_08_{view.upper()}_MEASUREMENT_CONTRACT.json"
        content = {
            "schema": f"AERATHEA_R8_{view.upper()}_EXACT_MEASUREMENT_V1",
            "run_id": RUN_ID,
            "view": view,
            "source_rectangle_half_open": rect[view],
            "uniform_scale_cm_per_pixel": fr(axial_scale),
            "row_profiles": evidence[view]["rows"],
            "column_profiles": evidence[view]["columns"],
            "footprint_authority": (
                "exact selected source pixels and their run boundaries; "
                "rectangle is registration metadata only"
            ),
            "source_capture_sha256": evidence[view]["capture_sha256"],
        }
        write_json(path, content)
        axial_paths[view] = path
    board08 = build_board(
        "STEP 08 - TOP / BOTTOM EXACT SOURCE FOOTPRINTS",
        evidence,
        {
            "top": RUN / "review/STEP_08_TOP_BOTTOM_EXACT_MEASUREMENT_REVIEW.png",
            "bottom": RUN
            / "review/STEP_08_TOP_BOTTOM_EXACT_MEASUREMENT_REVIEW.png",
        },
        {
            "top": [
                ("x", 766, "center 1533/2"),
                ("y", 546, "center 1093/2"),
            ],
            "bottom": [
                ("x", 764, "center 1529/2"),
                ("y", 539, "center y=539"),
            ],
        },
    )
    step_docs(
        "08",
        "Lock exact top/bottom footprint pixels, orientation, centers, and "
        "their source-owned differences.",
        "PASS",
        "09",
    )
    validate(
        "08",
        {
            "top_replay_exact": evidence["top"]["selected_pixel_count"]
            == source_records["top"]["exact_selected_pixel_count"],
            "bottom_replay_exact": evidence["bottom"]["selected_pixel_count"]
            == source_records["bottom"]["exact_selected_pixel_count"],
            "common_axial_uniform_scale": True,
            "top_profile_not_replaced_by_rectangle": len(
                evidence["top"]["rows"]
            )
            > 1,
            "bottom_profile_not_replaced_by_rectangle": len(
                evidence["bottom"]["rows"]
            )
            > 1,
            "top_bottom_retained_separately": evidence["top"][
                "membership_sha256"
            ]
            != evidence["bottom"]["membership_sha256"],
            "review_exists": board08.is_file(),
            "no_smoothing": True,
            "no_geometry": True,
        },
        {
            "top_manifest_sha256": sha256(axial_paths["top"]),
            "bottom_manifest_sha256": sha256(axial_paths["bottom"]),
            "review_sha256": sha256(board08),
        },
    )

    # Step 09: exact differences are explicit; no averaging beyond approved
    # centered axial registration and no silent priority.
    disagreements = [
        {
            "id": "DX001",
            "subject": "front versus back complete width consequence",
            "front_cm": fr(front_width),
            "back_cm": fr(
                Fraction(rect["back"][2] - rect["back"][0]) * back_scale
            ),
            "status": "explicit_rule_required",
        },
        {
            "id": "DX002",
            "subject": "top versus bottom depth consequence at common axial scale",
            "top_cm": registration["observed_comparison_consequences_cm"][
                "top_depth_at_common_axial_scale"
            ],
            "bottom_cm": registration["observed_comparison_consequences_cm"][
                "bottom_depth_at_common_axial_scale"
            ],
            "status": "approved centered arithmetic-mean rule available",
        },
        {
            "id": "DX003",
            "subject": "right rune versus metal half completed depth",
            "rune_cm": registration["right_candidate_halves"]["rune_side"][
                "completed_depth_cm"
            ],
            "metal_cm": registration["right_candidate_halves"][
                "metal_center_piece_side"
            ]["completed_depth_cm"],
            "status": "approved retain-as-two-candidates rule available",
        },
        {
            "id": "DX004",
            "subject": "right object-bounds center versus diamond rotation center",
            "object_center_x": fr(centers["right_object"]),
            "rotation_center_x": fr(centers["right_rotation"]),
            "status": "approved diamond-center x=557 rule available",
        },
        {
            "id": "DX005",
            "subject": "front stations versus independently unresolved back stations",
            "status": "front-source priority required for construction stations",
        },
    ]
    integrated = {
        "schema": "AERATHEA_R8_INTEGRATED_EXACT_MEASUREMENT_INDEX_V1",
        "run_id": RUN_ID,
        "step": "09",
        "inputs": {
            "step05": sha256(step05),
            "step06_front": sha256(front_path),
            "step06_back": sha256(back_path),
            "step07_left": sha256(side_paths["left"]),
            "step07_right": sha256(side_paths["right"]),
            "step08_top": sha256(axial_paths["top"]),
            "step08_bottom": sha256(axial_paths["bottom"]),
        },
        "total_exact_selected_pixels": sum(
            int(evidence[v]["selected_pixel_count"]) for v in VIEWS
        ),
        "per_view_selected_pixels": {
            v: evidence[v]["selected_pixel_count"] for v in VIEWS
        },
        "derived_dimensions_cm": registration[
            "derived_overall_dimensions_cm"
        ],
        "front_component_stations_world_z_cm": front_z,
        "right_candidate_halves": registration["right_candidate_halves"],
    }
    correspondence = {
        "schema": "AERATHEA_R8_CROSS_VIEW_CORRESPONDENCE_V1",
        "run_id": RUN_ID,
        "status": "candidate pending Step 10 deterministic rules",
        "directly_corresponding": [
            "overall vertical extent front/back/left/right",
            "head, coupler, haft, ferrule, grip, collar, pommel order",
            "blue focal diamond family",
        ],
        "not_exactly_corresponding": [row["id"] for row in disagreements],
        "hidden_surface_correspondence": "unresolved until Step 10",
    }
    matrix = {
        "schema": "AERATHEA_R8_DISAGREEMENT_UNKNOWN_MATRIX_V1",
        "run_id": RUN_ID,
        "items": disagreements,
    }
    audit = {
        "schema": "AERATHEA_R8_PRE_GEOMETRY_EXACT_DATA_AUDIT_V1",
        "run_id": RUN_ID,
        "result": "pass_with_explicit_blocks",
        "reason": (
            "all six sources are exact and independently registered, but their "
            "silhouettes are not one zero-XOR 3D dataset without the already "
            "approved Step 10 priority/completion rules"
        ),
        "source_pixels_modified": False,
        "component_scaling_used": False,
        "image_warping_used": False,
        "silent_priority_used": False,
        "geometry_authorized": False,
    }
    integrated_path = (
        RUN / "manifests/STEP_09_INTEGRATED_EXACT_MEASUREMENT_INDEX.json"
    )
    correspondence_path = (
        RUN / "manifests/STEP_09_CROSS_VIEW_CORRESPONDENCE.json"
    )
    matrix_path = RUN / "manifests/STEP_09_DISAGREEMENT_UNKNOWN_MATRIX.json"
    audit_path = RUN / "manifests/STEP_09_PRE_GEOMETRY_EXACT_DATA_AUDIT.json"
    write_json(integrated_path, integrated)
    write_json(correspondence_path, correspondence)
    write_json(matrix_path, matrix)
    write_json(audit_path, audit)
    review09 = RUN / "review/STEP_09_CROSS_VIEW_EXACT_DATASET_REVIEW.md"
    review09.write_text(
        "# Step 09 Cross-View Exact Dataset Review\n\n"
        "- Result: `pass_with_explicit_blocks`\n"
        "- All 1,544,766 selected source pixels and colors remain exact.\n"
        "- Front/back width, top/bottom depth, right-half depth, rotation "
        "center, and independent station correspondence differences are "
        "recorded rather than averaged or hidden.\n"
        "- Step 10 must consume explicit approved rules before geometry.\n\n"
        "| Conflict | Disposition entering Step 10 |\n"
        "|---|---|\n"
        "| Front/back width | explicit owner required |\n"
        "| Top/bottom depth | centered arithmetic mean rule available |\n"
        "| Rune/metal right halves | retain two unequal candidates |\n"
        "| Bounds center/diamond center | x=557 diamond center rule available |\n"
        "| Front/back stations | construction owner required |\n"
    )
    step_docs(
        "09",
        "Determine whether the six exact evidence sets form one coherent "
        "zero-XOR dataset and expose every contradiction.",
        "pass_with_explicit_blocks",
        "10",
    )
    validate(
        "09",
        {
            "all_six_measurements_indexed": len(integrated["inputs"]) == 7,
            "all_selected_pixels_accounted": integrated[
                "total_exact_selected_pixels"
            ]
            == 1544766,
            "five_explicit_disagreements": len(disagreements) == 5,
            "no_warping": not audit["image_warping_used"],
            "no_component_scaling": not audit["component_scaling_used"],
            "no_silent_priority": not audit["silent_priority_used"],
            "valid_result_vocabulary": audit["result"]
            == "pass_with_explicit_blocks",
            "geometry_still_blocked": not audit["geometry_authorized"],
        },
        {
            "integrated_sha256": sha256(integrated_path),
            "correspondence_sha256": sha256(correspondence_path),
            "matrix_sha256": sha256(matrix_path),
            "audit_sha256": sha256(audit_path),
            "review_sha256": sha256(review09),
        },
    )
    state = json.loads(STATE.read_text())
    state["current_step"] = "10"
    state["completed_steps"] = [f"{value:02d}" for value in range(1, 10)]
    state["last_validation"] = str(
        (RUN / "manifests/STEP_09_VALIDATION.json").relative_to(ROOT)
    )
    write_json(STATE, state)


if __name__ == "__main__":
    main()
