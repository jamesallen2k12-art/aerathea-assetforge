#!/usr/bin/env python3
"""Independently audit Siege Breaker R8 Step 09A source ownership.

This validator does not import the builder. It independently decodes the
immutable captures, repeats the 4-connected exterior classification, replays
the declared candidate rules, reconstructs every review pixel, and writes only
the validation manifest.
"""

from __future__ import annotations

import ast
from collections import deque
from dataclasses import dataclass
from fractions import Fraction
import gzip
import hashlib
import io
import json
from pathlib import Path
from typing import Any

from PIL import Image, ImageDraw, ImageFont


ROOT = Path(__file__).resolve().parents[2]
ASSET = "SM_DRW_SiegeBreaker_Hammer_A01"
RUN_ID = "SB-CR-R8-STEP09A-COMPONENT-PIXEL-OWNERSHIP-A01"
RUN_ROOT = (
    ROOT
    / "docs/assets/blueprints"
    / ASSET
    / "proof_runs"
    / RUN_ID
)
INPUT_PATH = RUN_ROOT / "manifests/STEP_09A_INTERPRETATION_INPUT.json"
SCANLINE_PATH = RUN_ROOT / "evidence/STEP_09A_COMPONENT_SCANLINES.json.gz"
INDEX_PATH = (
    RUN_ROOT
    / "manifests/STEP_09A_BOUNDARY_AND_CORRESPONDENCE_INDEX.json"
)
VALIDATION_PATH = RUN_ROOT / "manifests/STEP_09A_VALIDATION.json"
BUILDER_PATH = (
    ROOT
    / "Tools/DCC/build_siegebreaker_r8_step09a_component_pixel_ownership.py"
)


@dataclass
class View:
    name: str
    source_path: Path
    capture_path: Path
    rectangle: tuple[int, int, int, int]
    width: int
    height: int
    selected: bytearray
    exterior: bytearray
    domain: bytearray
    source: Image.Image

    @property
    def x0(self) -> int:
        return self.rectangle[0]

    @property
    def y0(self) -> int:
        return self.rectangle[1]

    @property
    def x1(self) -> int:
        return self.rectangle[2]

    @property
    def y1(self) -> int:
        return self.rectangle[3]

    def index(self, x: int, y: int) -> int:
        return (y - self.y0) * self.width + (x - self.x0)


class Audit:
    def __init__(self) -> None:
        self.checks: list[dict[str, Any]] = []

    def check(
        self, label: str, condition: bool, evidence: Any | None = None
    ) -> None:
        item: dict[str, Any] = {
            "id": label,
            "result": "PASS" if condition else "FAIL",
        }
        if evidence is not None:
            item["evidence"] = evidence
        self.checks.append(item)

    @property
    def passed(self) -> int:
        return sum(item["result"] == "PASS" for item in self.checks)

    @property
    def failed(self) -> list[str]:
        return [
            item["id"] for item in self.checks if item["result"] == "FAIL"
        ]


def sha256_bytes(value: bytes) -> str:
    return hashlib.sha256(value).hexdigest()


def sha256(path: Path) -> str:
    return sha256_bytes(path.read_bytes())


def canonical_json_bytes(value: Any) -> bytes:
    return (
        json.dumps(value, sort_keys=True, separators=(",", ":"), ensure_ascii=True)
        + "\n"
    ).encode("utf-8")


def decode_view(name: str, spec: dict[str, Any], audit: Audit) -> View:
    source_path = ROOT / spec["source_path"]
    capture_path = ROOT / spec["capture_path"]
    audit.check(
        f"{name}_source_hash",
        source_path.is_file() and sha256(source_path) == spec["source_sha256"],
        spec["source_sha256"],
    )
    audit.check(
        f"{name}_capture_hash",
        capture_path.is_file() and sha256(capture_path) == spec["capture_sha256"],
        spec["capture_sha256"],
    )
    with gzip.open(capture_path, "rt", encoding="utf-8") as stream:
        capture = json.load(stream)
    rectangle = tuple(capture["rectangle_half_open"])
    audit.check(
        f"{name}_capture_schema_and_rectangle",
        capture.get("schema") == "AERATHEA_COMPLETE_HAMMER_RGBA_SCANLINES_V1"
        and list(rectangle) == spec["rectangle_half_open"],
        {"schema": capture.get("schema"), "rectangle_half_open": list(rectangle)},
    )
    x0, y0, x1, y1 = rectangle
    width = x1 - x0
    height = y1 - y0
    selected = bytearray(width * height)
    structure_ok = True
    prior_y = y0 - 1
    for row in capture["rows_with_exact_rgba"]:
        y = row["y"]
        if not (y0 <= y < y1 and y > prior_y):
            structure_ok = False
        prior_y = y
        prior_x1 = x0
        for run in row["runs"]:
            run_x0 = run["x0"]
            run_x1 = run["x1"]
            if not (x0 <= run_x0 < run_x1 <= x1 and run_x0 >= prior_x1):
                structure_ok = False
                continue
            prior_x1 = run_x1
            offset = (y - y0) * width
            for x in range(run_x0, run_x1):
                local = offset + x - x0
                if selected[local]:
                    structure_ok = False
                selected[local] = 1
    audit.check(f"{name}_capture_runs_well_formed", structure_ok)

    exterior = bytearray(width * height)
    queue: deque[int] = deque()

    def seed(local_x: int, local_y: int) -> None:
        index = local_y * width + local_x
        if not selected[index] and not exterior[index]:
            exterior[index] = 1
            queue.append(index)

    for local_x in range(width):
        seed(local_x, 0)
        seed(local_x, height - 1)
    for local_y in range(height):
        seed(0, local_y)
        seed(width - 1, local_y)
    while queue:
        index = queue.popleft()
        local_y, local_x = divmod(index, width)
        for next_x, next_y in (
            (local_x - 1, local_y),
            (local_x + 1, local_y),
            (local_x, local_y - 1),
            (local_x, local_y + 1),
        ):
            if not (0 <= next_x < width and 0 <= next_y < height):
                continue
            next_index = next_y * width + next_x
            if selected[next_index] or exterior[next_index]:
                continue
            exterior[next_index] = 1
            queue.append(next_index)
    domain = bytearray(
        1 if selected[index] or not exterior[index] else 0
        for index in range(width * height)
    )
    source = Image.open(source_path).convert("RGB")
    audit.check(
        f"{name}_source_contains_locked_rectangle",
        source.width >= x1 and source.height >= y1,
        {"source_size": [source.width, source.height]},
    )
    return View(
        name=name,
        source_path=source_path,
        capture_path=capture_path,
        rectangle=rectangle,
        width=width,
        height=height,
        selected=selected,
        exterior=exterior,
        domain=domain,
        source=source,
    )


def row_runs(
    view: View,
    mask: bytearray,
    y: int,
    limit: tuple[int, int] | None = None,
) -> list[list[int]]:
    if not view.y0 <= y < view.y1:
        return []
    start = view.x0 if limit is None else max(view.x0, limit[0])
    end = view.x1 if limit is None else min(view.x1, limit[1])
    offset = (y - view.y0) * view.width
    result: list[list[int]] = []
    x = start
    while x < end:
        if mask[offset + x - view.x0]:
            run_start = x
            x += 1
            while x < end and mask[offset + x - view.x0]:
                x += 1
            result.append([run_start, x])
        else:
            x += 1
    return result


def set_pixel(view: View, mask: bytearray, x: int, y: int) -> None:
    mask[view.index(x, y)] = 1


def empty(view: View) -> bytearray:
    return bytearray(view.width * view.height)


def mask_from_owner_record(
    view: View,
    component_id: str,
    record: dict[str, Any],
    audit: Audit,
) -> bytearray:
    mask = empty(view)
    structure_ok = True
    row_payload_ok = True
    prior_y = view.y0 - 1
    calculated_selected = 0
    calculated_enclosed = 0
    calculated_owner = 0
    for row in record["rows"]:
        y = row["y"]
        if not (view.y0 <= y < view.y1 and y > prior_y):
            structure_ok = False
            continue
        prior_y = y
        prior_x1 = view.x0
        for start, end in row["owner_runs_half_open"]:
            if not (
                view.x0 <= start < end <= view.x1 and start >= prior_x1
            ):
                structure_ok = False
                continue
            prior_x1 = end
            for x in range(start, end):
                index = view.index(x, y)
                if mask[index] or not view.domain[index]:
                    structure_ok = False
                mask[index] = 1
        expected_selected = [
            run
            for run in row_runs(view, mask, y)
            for _ in (0,)
        ]
        selected_mask = empty(view)
        enclosed_mask = empty(view)
        for start, end in row["owner_runs_half_open"]:
            for x in range(start, end):
                index = view.index(x, y)
                if view.selected[index]:
                    selected_mask[index] = 1
                else:
                    enclosed_mask[index] = 1
        selected_runs = row_runs(view, selected_mask, y)
        enclosed_runs = row_runs(view, enclosed_mask, y)
        if selected_runs != row["selected_runs_half_open"]:
            row_payload_ok = False
        if enclosed_runs != row["enclosed_source_runs_half_open"]:
            row_payload_ok = False
        owner_count = sum(
            end - start for start, end in row["owner_runs_half_open"]
        )
        if owner_count != row["owner_pixel_count"]:
            row_payload_ok = False
        calculated_owner += owner_count
        calculated_selected += sum(end - start for start, end in selected_runs)
        calculated_enclosed += sum(end - start for start, end in enclosed_runs)
        if expected_selected != row["owner_runs_half_open"]:
            row_payload_ok = False
    count_ok = (
        calculated_owner == record["owner_pixel_count"]
        and calculated_selected == record["selected_capture_pixel_count"]
        and calculated_enclosed == record["enclosed_source_pixel_count"]
        and calculated_owner == calculated_selected + calculated_enclosed
        and sum(mask) == calculated_owner
    )
    audit.check(
        f"{view.name}_{component_id}_owner_rows",
        structure_ok and row_payload_ok and count_ok,
        {
            "owner": calculated_owner,
            "selected": calculated_selected,
            "enclosed": calculated_enclosed,
        },
    )
    return mask


def interval_contains_edge(interval: list[int], edge: Fraction) -> bool:
    return Fraction(interval[0], 1) <= edge < Fraction(interval[1], 1)


def axis_observations(
    view: View, axis: Fraction, y0: int, y1: int
) -> tuple[dict[int, tuple[int, int]], dict[int, tuple[int, int]], set[int]]:
    left: dict[int, tuple[int, int]] = {}
    right: dict[int, tuple[int, int]] = {}
    absent: set[int] = set()
    for y in range(y0, y1):
        runs = row_runs(view, view.domain, y)
        center = next(
            (
                index
                for index, interval in enumerate(runs)
                if interval_contains_edge(interval, axis)
            ),
            None,
        )
        if center is None:
            absent.add(y)
            continue
        if center > 0:
            left[y] = (runs[center - 1][1], runs[center][0])
        if center + 1 < len(runs):
            right[y] = (runs[center][1], runs[center + 1][0])
    return left, right, absent


def interpolate(anchors: dict[int, Fraction], y: int) -> Fraction:
    if y in anchors:
        return anchors[y]
    ordered = sorted(anchors)
    lower = [value for value in ordered if value < y]
    upper = [value for value in ordered if value > y]
    if not lower:
        return anchors[upper[0]]
    if not upper:
        return anchors[lower[-1]]
    low = lower[-1]
    high = upper[0]
    return anchors[low] + (anchors[high] - anchors[low]) * Fraction(
        y - low, high - low
    )


def round_nearest_lower_half(value: Fraction) -> int:
    lower = value.numerator // value.denominator
    remainder = value.numerator - lower * value.denominator
    return lower if remainder * 2 <= value.denominator else lower + 1


def cut_series(
    observations: dict[int, tuple[int, int]], y0: int, y1: int
) -> dict[int, int]:
    anchors = {
        y: Fraction(first + second, 2)
        for y, (first, second) in observations.items()
    }
    if not anchors:
        raise RuntimeError("independent audit found no gap observations")
    return {
        y: round_nearest_lower_half(interpolate(anchors, y))
        for y in range(y0, y1)
    }


def anchor_series(
    anchors: list[list[int]], y0: int, y1: int
) -> dict[int, int]:
    values = {int(y): Fraction(int(x), 1) for y, x in anchors}
    return {
        y: round_nearest_lower_half(interpolate(values, y))
        for y in range(y0, y1)
    }


def expected_front(
    view: View, interpretation: dict[str, Any]
) -> tuple[dict[str, bytearray], dict[str, Any]]:
    axis = Fraction(interpretation["structural_axis_source_edge_x"], 1)
    stone_y0, stone_y1 = interpretation["stone_rows_half_open"]
    c01_y0, c01_y1 = interpretation["c01_rows_half_open"]
    c12_y0, c12_y1 = interpretation["c12_reserved_rows_half_open"]
    c06_y0, c06_y1 = interpretation["c06_rows_half_open"]
    left_observed, right_observed, absent = axis_observations(
        view, axis, stone_y0, stone_y1
    )
    if absent:
        raise RuntimeError(f"front axis absent on rows {sorted(absent)}")
    left_cuts = cut_series(left_observed, stone_y0, stone_y1)
    right_cuts = cut_series(right_observed, stone_y0, stone_y1)
    masks = {
        "C01_CENTER_CORE": empty(view),
        "C02_STONE_LEFT": empty(view),
        "C03_STONE_RIGHT": empty(view),
        "C06_UPPER_HAFT_CAP": empty(view),
        "C12_RESERVED_EXISTING_OWNER": empty(view),
    }
    for y in range(stone_y0, stone_y1):
        for x in range(view.x0, view.x1):
            if not view.domain[view.index(x, y)]:
                continue
            if x < left_cuts[y]:
                set_pixel(view, masks["C02_STONE_LEFT"], x, y)
            elif x >= right_cuts[y]:
                set_pixel(view, masks["C03_STONE_RIGHT"], x, y)
            elif c01_y0 <= y < c01_y1:
                set_pixel(view, masks["C01_CENTER_CORE"], x, y)
            elif c12_y0 <= y < c12_y1:
                set_pixel(view, masks["C12_RESERVED_EXISTING_OWNER"], x, y)
    for y in range(c06_y0, c06_y1):
        for x in range(view.x0, view.x1):
            if view.domain[view.index(x, y)]:
                set_pixel(view, masks["C06_UPPER_HAFT_CAP"], x, y)
    return masks, {
        "left_cuts": left_cuts,
        "right_cuts": right_cuts,
    }


def expected_axial(
    view: View, axis: Fraction
) -> tuple[dict[str, bytearray], dict[str, Any]]:
    left_observed, right_observed, absent = axis_observations(
        view, axis, view.y0, view.y1
    )
    left_cuts = cut_series(left_observed, view.y0, view.y1)
    right_cuts = cut_series(right_observed, view.y0, view.y1)
    masks = {
        "C02_STONE_LEFT": empty(view),
        "C03_STONE_RIGHT": empty(view),
        "CENTRAL_NON_STONE_RESERVED": empty(view),
    }
    for y in range(view.y0, view.y1):
        for x in range(view.x0, view.x1):
            if not view.domain[view.index(x, y)]:
                continue
            if y in absent:
                if Fraction(x + 1, 1) <= axis:
                    set_pixel(view, masks["C02_STONE_LEFT"], x, y)
                elif Fraction(x, 1) >= axis:
                    set_pixel(view, masks["C03_STONE_RIGHT"], x, y)
                else:
                    raise RuntimeError(
                        f"{view.name} absent-axis row owns crossing pixel"
                    )
            elif x < left_cuts[y]:
                set_pixel(view, masks["C02_STONE_LEFT"], x, y)
            elif x >= right_cuts[y]:
                set_pixel(view, masks["C03_STONE_RIGHT"], x, y)
            else:
                set_pixel(view, masks["CENTRAL_NON_STONE_RESERVED"], x, y)
    return masks, {
        "left_cuts": left_cuts,
        "right_cuts": right_cuts,
        "axis_absent": absent,
    }


def expected_right(
    view: View, interpretation: dict[str, Any]
) -> tuple[dict[str, bytearray], dict[str, Any]]:
    y0, y1 = interpretation["c04_rows_half_open"]
    rune_x0, rune_x1 = interpretation["candidate_intervals_half_open"][
        "rune_side"
    ]
    metal_x0, metal_x1 = interpretation["candidate_intervals_half_open"][
        "metal_center_piece_side"
    ]
    face_left = anchor_series(
        interpretation["metal_half_c04_left_edge_anchors"], y0, y1
    )
    masks = {
        "C04_RUNE_SIDE": empty(view),
        "C04_METAL_CENTER_PIECE_SIDE": empty(view),
        "C01_SIDE_RESERVED_IN_METAL_HALF": empty(view),
    }
    for y in range(y0, y1):
        for x in range(view.x0, view.x1):
            if not view.domain[view.index(x, y)]:
                continue
            if rune_x0 <= x < rune_x1:
                set_pixel(view, masks["C04_RUNE_SIDE"], x, y)
            if metal_x0 <= x < face_left[y]:
                set_pixel(view, masks["C01_SIDE_RESERVED_IN_METAL_HALF"], x, y)
            elif face_left[y] <= x < metal_x1:
                set_pixel(view, masks["C04_METAL_CENTER_PIECE_SIDE"], x, y)
    return masks, {"face_left": face_left}


def protected_runs(view: View, y: int, start: int, end: int) -> list[list[int]]:
    return row_runs(view, view.exterior, y, (start, end))


def front_boundaries(
    view: View,
    masks: dict[str, bytearray],
    aux: dict[str, Any],
    interpretation: dict[str, Any],
) -> tuple[list[dict[str, Any]], dict[str, Any]]:
    stone_y0, stone_y1 = interpretation["stone_rows_half_open"]
    c01_y0, c01_y1 = interpretation["c01_rows_half_open"]
    c06_y0, c06_y1 = interpretation["c06_rows_half_open"]
    central = bytearray(
        1
        if masks["C01_CENTER_CORE"][index]
        or masks["C12_RESERVED_EXISTING_OWNER"][index]
        else 0
        for index in range(view.width * view.height)
    )
    protected: list[dict[str, Any]] = []
    left_samples: list[dict[str, Any]] = []
    right_samples: list[dict[str, Any]] = []
    for y in range(stone_y0, stone_y1):
        left = row_runs(view, masks["C02_STONE_LEFT"], y)
        center = row_runs(view, central, y)
        right = row_runs(view, masks["C03_STONE_RIGHT"], y)
        if left and center:
            gap = protected_runs(view, y, left[-1][1], center[0][0])
            item: dict[str, Any] = {
                "y": y,
                "mode": "protected_gap" if gap else "shared_contact_cut",
                "c02_owner_edge_x": left[-1][1],
                "central_owner_edge_x": center[0][0],
                "partition_cut_edge_x": aux["left_cuts"][y],
            }
            if gap:
                item["protected_runs_half_open"] = gap
                protected.append(
                    {
                        "view": "front",
                        "y": y,
                        "between": "C02_STONE_LEFT and central owner",
                        "runs_half_open": gap,
                    }
                )
            left_samples.append(item)
        if center and right:
            gap = protected_runs(view, y, center[-1][1], right[0][0])
            item = {
                "y": y,
                "mode": "protected_gap" if gap else "shared_contact_cut",
                "central_owner_edge_x": center[-1][1],
                "c03_owner_edge_x": right[0][0],
                "partition_cut_edge_x": aux["right_cuts"][y],
            }
            if gap:
                item["protected_runs_half_open"] = gap
                protected.append(
                    {
                        "view": "front",
                        "y": y,
                        "between": "central owner and C03_STONE_RIGHT",
                        "runs_half_open": gap,
                    }
                )
            right_samples.append(item)
    boundaries = {
        "FRONT_C02_INNER_OWNER_EDGE": {
            "view": "front",
            "owner": "C02_STONE_LEFT",
            "adjacent": "central owner or protected negative space",
            "order": "source_y_ascending_world_z_descending",
            "samples": left_samples,
        },
        "FRONT_C03_INNER_OWNER_EDGE": {
            "view": "front",
            "owner": "C03_STONE_RIGHT",
            "adjacent": "central owner or protected negative space",
            "order": "source_y_ascending_world_z_descending",
            "samples": right_samples,
        },
        "FRONT_C01_C06_CONTACT": {
            "view": "front",
            "order": "source_x_ascending",
            "c01_last_source_row": c01_y1 - 1,
            "c01_owner_runs_half_open": row_runs(
                view, masks["C01_CENTER_CORE"], c01_y1 - 1
            ),
            "shared_source_edge_y": c06_y0,
            "c06_first_source_row": c06_y0,
            "c06_owner_runs_half_open": row_runs(
                view, masks["C06_UPPER_HAFT_CAP"], c06_y0
            ),
        },
        "FRONT_C06_C07_CONTACT": {
            "view": "front",
            "order": "source_x_ascending",
            "c06_last_source_row": c06_y1 - 1,
            "c06_owner_runs_half_open": row_runs(
                view, masks["C06_UPPER_HAFT_CAP"], c06_y1 - 1
            ),
            "shared_source_edge_y": c06_y1,
            "c07_existing_station_source_row": c06_y1,
            "c07_source_domain_runs_half_open": row_runs(
                view, view.domain, c06_y1
            ),
        },
        "FRONT_C12_RESERVED_C01_CONTACT": {
            "view": "front",
            "order": "source_x_ascending",
            "shared_source_edge_y": c01_y0,
            "classification": "candidate C01 upper visibility edge; C12 shape is not re-decided",
            "c12_reserved_last_source_row": c01_y0 - 1,
            "c12_reserved_runs_half_open": row_runs(
                view, masks["C12_RESERVED_EXISTING_OWNER"], c01_y0 - 1
            ),
            "c01_first_source_row": c01_y0,
            "c01_owner_runs_half_open": row_runs(
                view, masks["C01_CENTER_CORE"], c01_y0
            ),
        },
    }
    return protected, boundaries


def axial_boundaries(
    view: View,
    masks: dict[str, bytearray],
    aux: dict[str, Any],
) -> tuple[list[dict[str, Any]], dict[str, Any]]:
    protected: list[dict[str, Any]] = []
    left_samples: list[dict[str, Any]] = []
    right_samples: list[dict[str, Any]] = []
    separated: list[dict[str, Any]] = []
    for y in range(view.y0, view.y1):
        left = row_runs(view, masks["C02_STONE_LEFT"], y)
        center = row_runs(view, masks["CENTRAL_NON_STONE_RESERVED"], y)
        right = row_runs(view, masks["C03_STONE_RIGHT"], y)
        if center:
            if left:
                gap = protected_runs(view, y, left[-1][1], center[0][0])
                item: dict[str, Any] = {
                    "y": y,
                    "mode": "protected_gap" if gap else "shared_contact_cut",
                    "c02_owner_edge_x": left[-1][1],
                    "central_owner_edge_x": center[0][0],
                    "partition_cut_edge_x": aux["left_cuts"][y],
                }
                if gap:
                    item["protected_runs_half_open"] = gap
                    protected.append(
                        {
                            "view": view.name,
                            "y": y,
                            "between": "C02_STONE_LEFT and central non-stone owner",
                            "runs_half_open": gap,
                        }
                    )
                left_samples.append(item)
            if right:
                gap = protected_runs(view, y, center[-1][1], right[0][0])
                item = {
                    "y": y,
                    "mode": "protected_gap" if gap else "shared_contact_cut",
                    "central_owner_edge_x": center[-1][1],
                    "c03_owner_edge_x": right[0][0],
                    "partition_cut_edge_x": aux["right_cuts"][y],
                }
                if gap:
                    item["protected_runs_half_open"] = gap
                    protected.append(
                        {
                            "view": view.name,
                            "y": y,
                            "between": "central non-stone owner and C03_STONE_RIGHT",
                            "runs_half_open": gap,
                        }
                    )
                right_samples.append(item)
        elif left and right:
            gap = protected_runs(view, y, left[-1][1], right[0][0])
            if gap:
                protected.append(
                    {
                        "view": view.name,
                        "y": y,
                        "between": "C02_STONE_LEFT and C03_STONE_RIGHT with no central owner",
                        "runs_half_open": gap,
                    }
                )
            separated.append(
                {
                    "y": y,
                    "c02_owner_edge_x": left[-1][1],
                    "c03_owner_edge_x": right[0][0],
                    "protected_runs_half_open": gap,
                }
            )
    prefix = view.name.upper()
    return protected, {
        f"{prefix}_C02_INNER_OWNER_EDGE": {
            "view": view.name,
            "owner": "C02_STONE_LEFT",
            "adjacent": "central non-stone owner or protected negative space",
            "order": "source_y_ascending",
            "samples": left_samples,
        },
        f"{prefix}_C03_INNER_OWNER_EDGE": {
            "view": view.name,
            "owner": "C03_STONE_RIGHT",
            "adjacent": "central non-stone owner or protected negative space",
            "order": "source_y_ascending",
            "samples": right_samples,
        },
        f"{prefix}_STONE_SEPARATION_WITHOUT_CENTRAL_OWNER": {
            "view": view.name,
            "order": "source_y_ascending",
            "samples": separated,
        },
    }


def right_boundaries(
    view: View,
    masks: dict[str, bytearray],
    aux: dict[str, Any],
    interpretation: dict[str, Any],
) -> tuple[list[dict[str, Any]], dict[str, Any]]:
    y0, y1 = interpretation["c04_rows_half_open"]
    axis = interpretation["rotation_axis_source_edge_x"]
    intervals = interpretation["candidate_intervals_half_open"]
    protected: list[dict[str, Any]] = []
    samples: list[dict[str, Any]] = []
    for y in range(y0, y1):
        metal = row_runs(view, masks["C04_METAL_CENTER_PIECE_SIDE"], y)
        rune = row_runs(view, masks["C04_RUNE_SIDE"], y)
        reserved = row_runs(
            view, masks["C01_SIDE_RESERVED_IN_METAL_HALF"], y
        )
        metal_gap = (
            protected_runs(view, y, metal[0][0], metal[-1][1])
            if metal
            else []
        )
        rune_gap = (
            protected_runs(view, y, rune[0][0], rune[-1][1])
            if rune
            else []
        )
        if metal_gap:
            protected.append(
                {
                    "view": "right",
                    "candidate": "metal_center_piece_side",
                    "y": y,
                    "between": "C04 source-owned runs",
                    "runs_half_open": metal_gap,
                }
            )
        if rune_gap:
            protected.append(
                {
                    "view": "right",
                    "candidate": "rune_side",
                    "y": y,
                    "between": "C04 source-owned runs",
                    "runs_half_open": rune_gap,
                }
            )
        samples.append(
            {
                "y": y,
                "metal_face_left_edge_x": aux["face_left"][y],
                "rotation_axis_edge_x": axis,
                "metal_c04_owner_runs_half_open": metal,
                "rune_c04_owner_runs_half_open": rune,
                "c01_side_reserved_runs_half_open": reserved,
                "metal_protected_runs_half_open": metal_gap,
                "rune_protected_runs_half_open": rune_gap,
            }
        )
    return protected, {
        "RIGHT_C04_CANDIDATE_HALF_BOUNDARIES": {
            "view": "right",
            "order": "source_y_ascending_world_z_descending",
            "candidate_intervals_half_open": {
                "rune_side": intervals["rune_side"],
                "metal_center_piece_side": intervals[
                    "metal_center_piece_side"
                ],
            },
            "samples": samples,
        },
        "RIGHT_C04_TOP_BOTTOM_EDGES": {
            "view": "right",
            "order": "source_x_ascending",
            "top_source_edge_y": y0,
            "top_metal_owner_runs_half_open": row_runs(
                view, masks["C04_METAL_CENTER_PIECE_SIDE"], y0
            ),
            "top_rune_owner_runs_half_open": row_runs(
                view, masks["C04_RUNE_SIDE"], y0
            ),
            "bottom_source_edge_y": y1,
            "bottom_last_source_row": y1 - 1,
            "bottom_metal_owner_runs_half_open": row_runs(
                view, masks["C04_METAL_CENTER_PIECE_SIDE"], y1 - 1
            ),
            "bottom_rune_owner_runs_half_open": row_runs(
                view, masks["C04_RUNE_SIDE"], y1 - 1
            ),
        },
    }


def draw_point(
    draw: ImageDraw.ImageDraw,
    view: View,
    x: int,
    y: int,
    color: tuple[int, int, int],
    allowed: bytearray,
) -> None:
    if (
        view.x0 <= x < view.x1
        and view.y0 <= y < view.y1
        and allowed[view.index(x, y)]
    ):
        draw.point((x - view.x0, y - view.y0), fill=color)


def reproduce_marked(
    view: View,
    masks: dict[str, bytearray],
    boundaries: dict[str, Any],
    protected: list[dict[str, Any]],
) -> Image.Image:
    image = view.source.crop(view.rectangle)
    draw = ImageDraw.Draw(image)
    green = (0, 255, 120)
    orange = (255, 150, 0)
    cyan = (0, 220, 255)
    yellow = (255, 230, 0)
    blue = (0, 120, 255)
    magenta = (255, 0, 220)
    gray = (190, 190, 190)
    red = (255, 20, 20)
    if view.name == "front":
        central = bytearray(
            1
            if masks["C01_CENTER_CORE"][index]
            or masks["C12_RESERVED_EXISTING_OWNER"][index]
            else 0
            for index in range(view.width * view.height)
        )
        for sample in boundaries["FRONT_C02_INNER_OWNER_EDGE"]["samples"]:
            y = sample["y"]
            draw_point(
                draw,
                view,
                sample["c02_owner_edge_x"] - 1,
                y,
                green,
                masks["C02_STONE_LEFT"],
            )
            draw_point(
                draw,
                view,
                sample["central_owner_edge_x"],
                y,
                cyan,
                central,
            )
        for sample in boundaries["FRONT_C03_INNER_OWNER_EDGE"]["samples"]:
            y = sample["y"]
            draw_point(
                draw,
                view,
                sample["central_owner_edge_x"] - 1,
                y,
                cyan,
                central,
            )
            draw_point(
                draw,
                view,
                sample["c03_owner_edge_x"],
                y,
                orange,
                masks["C03_STONE_RIGHT"],
            )
        for boundary_id, color, component, row_key in (
            ("FRONT_C01_C06_CONTACT", cyan, "C01_CENTER_CORE", "c01_last_source_row"),
            ("FRONT_C01_C06_CONTACT", yellow, "C06_UPPER_HAFT_CAP", "c06_first_source_row"),
            ("FRONT_C06_C07_CONTACT", yellow, "C06_UPPER_HAFT_CAP", "c06_last_source_row"),
            ("FRONT_C12_RESERVED_C01_CONTACT", gray, "C12_RESERVED_EXISTING_OWNER", "c12_reserved_last_source_row"),
            ("FRONT_C12_RESERVED_C01_CONTACT", cyan, "C01_CENTER_CORE", "c01_first_source_row"),
        ):
            y = boundaries[boundary_id][row_key]
            for start, end in row_runs(view, masks[component], y):
                for x in range(start, end):
                    draw_point(draw, view, x, y, color, masks[component])
    elif view.name in ("top", "bottom"):
        prefix = view.name.upper()
        for sample in boundaries[f"{prefix}_C02_INNER_OWNER_EDGE"]["samples"]:
            y = sample["y"]
            draw_point(
                draw,
                view,
                sample["c02_owner_edge_x"] - 1,
                y,
                green,
                masks["C02_STONE_LEFT"],
            )
            draw_point(
                draw,
                view,
                sample["central_owner_edge_x"],
                y,
                gray,
                masks["CENTRAL_NON_STONE_RESERVED"],
            )
        for sample in boundaries[f"{prefix}_C03_INNER_OWNER_EDGE"]["samples"]:
            y = sample["y"]
            draw_point(
                draw,
                view,
                sample["central_owner_edge_x"] - 1,
                y,
                gray,
                masks["CENTRAL_NON_STONE_RESERVED"],
            )
            draw_point(
                draw,
                view,
                sample["c03_owner_edge_x"],
                y,
                orange,
                masks["C03_STONE_RIGHT"],
            )
        for sample in boundaries[
            f"{prefix}_STONE_SEPARATION_WITHOUT_CENTRAL_OWNER"
        ]["samples"]:
            y = sample["y"]
            draw_point(
                draw,
                view,
                sample["c02_owner_edge_x"] - 1,
                y,
                green,
                masks["C02_STONE_LEFT"],
            )
            draw_point(
                draw,
                view,
                sample["c03_owner_edge_x"],
                y,
                orange,
                masks["C03_STONE_RIGHT"],
            )
    else:
        for sample in boundaries["RIGHT_C04_CANDIDATE_HALF_BOUNDARIES"][
            "samples"
        ]:
            y = sample["y"]
            reserved = sample["c01_side_reserved_runs_half_open"]
            metal = sample["metal_c04_owner_runs_half_open"]
            rune = sample["rune_c04_owner_runs_half_open"]
            if reserved:
                draw_point(
                    draw,
                    view,
                    reserved[-1][1] - 1,
                    y,
                    gray,
                    masks["C01_SIDE_RESERVED_IN_METAL_HALF"],
                )
            if metal:
                draw_point(
                    draw,
                    view,
                    metal[0][0],
                    y,
                    magenta,
                    masks["C04_METAL_CENTER_PIECE_SIDE"],
                )
                draw_point(
                    draw,
                    view,
                    metal[-1][1] - 1,
                    y,
                    magenta,
                    masks["C04_METAL_CENTER_PIECE_SIDE"],
                )
            if rune:
                draw_point(
                    draw,
                    view,
                    rune[0][0],
                    y,
                    blue,
                    masks["C04_RUNE_SIDE"],
                )
                draw_point(
                    draw,
                    view,
                    rune[-1][1] - 1,
                    y,
                    blue,
                    masks["C04_RUNE_SIDE"],
                )
    for item in protected:
        for start, end in item["runs_half_open"]:
            if start < end:
                draw_point(draw, view, start, item["y"], red, view.exterior)
                draw_point(
                    draw, view, end - 1, item["y"], red, view.exterior
                )
    return image


def get_font(size: int) -> ImageFont.ImageFont:
    for path in (
        Path("/usr/share/fonts/truetype/dejavu/DejaVuSans.ttf"),
        Path("/usr/share/fonts/dejavu/DejaVuSans-Bold.ttf"),
    ):
        if path.is_file():
            return ImageFont.truetype(str(path), size=size)
    return ImageFont.load_default()


def reproduce_board(marked: dict[str, Image.Image]) -> Image.Image:
    board = Image.new("RGB", (2040, 1350), (238, 238, 238))
    draw = ImageDraw.Draw(board)
    title_font = get_font(34)
    label_font = get_font(24)
    small_font = get_font(19)
    draw.text(
        (40, 24),
        "Siege Breaker Step 09A — exact source marks only",
        fill=(20, 20, 20),
        font=title_font,
    )
    draw.text(
        (40, 70),
        "CANDIDATE ownership interpretation — no fills, hidden shapes, or geometry",
        fill=(120, 0, 0),
        font=label_font,
    )
    legend = (
        ((0, 255, 120), "C02 left stone edge"),
        ((255, 150, 0), "C03 right stone edge"),
        ((0, 220, 255), "C01 edge"),
        ((255, 230, 0), "C06 edge"),
        ((255, 0, 220), "C04 metal-half edge"),
        ((0, 120, 255), "C04 rune-half edge"),
        ((255, 20, 20), "protected gap endpoints"),
        ((190, 190, 190), "reserved existing/non-stone owner"),
    )
    for index, (color, label) in enumerate(legend):
        x = 40 + (index % 4) * 490
        y = 112 + (index // 4) * 30
        draw.rectangle((x, y, x + 16, y + 16), fill=color)
        draw.text((x + 23, y - 3), label, fill=(25, 25, 25), font=small_font)
    front = marked["front"].crop((0, 0, marked["front"].width, 462))
    right = marked["right"].crop((0, 0, marked["right"].width, 504))
    first_y = 220
    draw.text((90, first_y - 34), "FRONT", fill=(20, 20, 20), font=label_font)
    board.paste(front, (90, first_y))
    draw.text((790, first_y - 34), "RIGHT", fill=(20, 20, 20), font=label_font)
    board.paste(right, (790, first_y))
    axial_y = 780
    draw.text((35, axial_y - 34), "TOP", fill=(20, 20, 20), font=label_font)
    board.paste(marked["top"], (35, axial_y))
    draw.text((1030, axial_y - 34), "BOTTOM", fill=(20, 20, 20), font=label_font)
    board.paste(marked["bottom"], (1030, axial_y))
    draw.text(
        (40, 1312),
        "Thin marks identify exact source pixels/edges. Red marks identify exact "
        "source-connected empty-space endpoints.",
        fill=(25, 25, 25),
        font=small_font,
    )
    return board


def nonoverlap(masks: dict[str, bytearray]) -> tuple[bool, int]:
    overlaps = 0
    for values in zip(*masks.values()):
        if sum(values) > 1:
            overlaps += 1
    return overlaps == 0, overlaps


def main() -> int:
    audit = Audit()
    config = json.loads(INPUT_PATH.read_text(encoding="utf-8"))
    index = json.loads(INDEX_PATH.read_text(encoding="utf-8"))
    with gzip.open(SCANLINE_PATH, "rb") as stream:
        scan_payload = stream.read()
    scan = json.loads(scan_payload)

    audit.check(
        "identity_and_schema",
        config.get("schema") == "AERATHEA_R8_STEP09A_INTERPRETATION_INPUT_V1"
        and scan.get("schema") == "AERATHEA_R8_STEP09A_COMPONENT_SCANLINES_V1"
        and index.get("schema")
        == "AERATHEA_R8_STEP09A_BOUNDARY_CORRESPONDENCE_INDEX_V1"
        and {
            config.get("asset"),
            scan.get("asset"),
            index.get("asset"),
        }
        == {ASSET}
        and {
            config.get("run_id"),
            scan.get("run_id"),
            index.get("run_id"),
        }
        == {RUN_ID},
    )
    input_hash = sha256(INPUT_PATH)
    audit.check(
        "interpretation_input_hash_chain",
        scan.get("interpretation_input_sha256") == input_hash
        and index.get("interpretation_input_sha256") == input_hash,
        input_hash,
    )
    authority_paths = {
        "parent_step09_index_sha256": ROOT
        / "docs/assets/blueprints"
        / ASSET
        / "proof_runs/SB-CR-STEPS01-16-R8-PIXEL-EXACT-A01/manifests/STEP_09_INTEGRATED_EXACT_MEASUREMENT_INDEX.json",
        "recovery_step10_decisions_sha256": ROOT
        / "docs/assets/blueprints"
        / ASSET
        / "proof_runs/SB-CR-STEPS10-16-R8-ZERO-EXTRUSION-A02/manifests/STEP_10_INTERPRETATION_DECISIONS.json",
        "recovery_step10_numeric_precedence_sha256": ROOT
        / "docs/assets/blueprints"
        / ASSET
        / "proof_runs/SB-CR-STEPS10-16-R8-ZERO-EXTRUSION-A02/manifests/STEP_10_NUMERIC_SUBSTITUTION_CLARIFICATION.json",
    }
    for key, path in authority_paths.items():
        audit.check(
            f"authority_{key}",
            path.is_file() and sha256(path) == config["authority"][key],
            config["authority"][key],
        )
    approval_path = RUN_ROOT / config["authority"]["approval_record"]
    contract_path = RUN_ROOT / config["authority"]["execution_contract"]
    audit.check(
        "approval_and_contract_present",
        approval_path.is_file()
        and contract_path.is_file()
        and "approved" in approval_path.read_text(encoding="utf-8").lower()
        and "authorized by Flamestrike"
        in contract_path.read_text(encoding="utf-8"),
        {
            "approval_sha256": sha256(approval_path),
            "contract_sha256": sha256(contract_path),
        },
    )

    audit.check(
        "owning_and_nonowning_view_sets",
        set(config["immutable_inputs"]) == {"front", "right", "top", "bottom"}
        and set(config["locked_nonowning_inputs"]) == {"back", "left"},
    )
    views = {
        name: decode_view(name, spec, audit)
        for name, spec in config["immutable_inputs"].items()
    }
    nonowning = {
        name: decode_view(name, spec, audit)
        for name, spec in config["locked_nonowning_inputs"].items()
    }
    expected_nonowning = {
        name: {
            "source_sha256": sha256(view.source_path),
            "capture_sha256": sha256(view.capture_path),
            "rectangle_half_open": list(view.rectangle),
            "ownership_output_required": False,
        }
        for name, view in nonowning.items()
    }
    audit.check(
        "nonowning_hash_locks_recorded",
        scan.get("locked_nonowning_inputs") == expected_nonowning
        and index.get("locked_nonowning_inputs") == expected_nonowning,
        sorted(expected_nonowning),
    )

    gzip_bytes = SCANLINE_PATH.read_bytes()
    audit.check(
        "deterministic_canonical_scanline_payload",
        scan_payload == canonical_json_bytes(scan)
        and gzip_bytes[4:8] == b"\x00\x00\x00\x00"
        and index.get("component_scanline_file_sha256")
        == sha256_bytes(gzip_bytes)
        and index.get("component_scanline_canonical_sha256")
        == sha256_bytes(scan_payload),
        {
            "file_sha256": sha256_bytes(gzip_bytes),
            "canonical_sha256": sha256_bytes(scan_payload),
        },
    )

    actual_masks: dict[str, dict[str, bytearray]] = {}
    view_summaries: dict[str, Any] = {}
    for name, view in views.items():
        view_record = scan["views"][name]
        audit.check(
            f"{name}_scanline_header",
            view_record["source_sha256"] == sha256(view.source_path)
            and view_record["capture_sha256"] == sha256(view.capture_path)
            and view_record["rectangle_half_open"] == list(view.rectangle)
            and view_record["selected_capture_pixel_count"] == sum(view.selected)
            and view_record["enclosed_source_pixel_count"]
            == sum(view.domain) - sum(view.selected),
        )
        actual_masks[name] = {
            component: mask_from_owner_record(
                view, component, record, audit
            )
            for component, record in view_record["component_owners"].items()
        }
        okay, overlap_count = nonoverlap(actual_masks[name])
        audit.check(
            f"{name}_component_owner_nonoverlap",
            okay,
            {"overlap_pixel_count": overlap_count},
        )
        view_summaries[name] = {
            "selected_capture_pixels": sum(view.selected),
            "enclosed_source_pixels": sum(view.domain) - sum(view.selected),
            "component_owner_pixels": {
                component: sum(mask)
                for component, mask in actual_masks[name].items()
            },
        }

    top_axis_spec = config["axial_interpretation"][
        "top_center_source_edge_x"
    ]
    bottom_axis_spec = config["axial_interpretation"][
        "bottom_center_source_edge_x"
    ]
    expected_masks: dict[str, dict[str, bytearray]] = {}
    auxiliaries: dict[str, dict[str, Any]] = {}
    expected_masks["front"], auxiliaries["front"] = expected_front(
        views["front"], config["front_interpretation"]
    )
    expected_masks["right"], auxiliaries["right"] = expected_right(
        views["right"], config["right_interpretation"]
    )
    expected_masks["top"], auxiliaries["top"] = expected_axial(
        views["top"],
        Fraction(top_axis_spec["numerator"], top_axis_spec["denominator"]),
    )
    expected_masks["bottom"], auxiliaries["bottom"] = expected_axial(
        views["bottom"],
        Fraction(
            bottom_axis_spec["numerator"], bottom_axis_spec["denominator"]
        ),
    )
    for name in ("front", "right", "top", "bottom"):
        expected_keys = set(expected_masks[name])
        actual_keys = set(actual_masks[name])
        differences = {
            component: sum(
                first != second
                for first, second in zip(
                    actual_masks[name].get(component, empty(views[name])),
                    expected_masks[name].get(component, empty(views[name])),
                )
            )
            for component in sorted(expected_keys | actual_keys)
        }
        audit.check(
            f"{name}_independent_candidate_rule_replay",
            actual_keys == expected_keys
            and all(count == 0 for count in differences.values()),
            differences,
        )

    expected_protected: dict[str, list[dict[str, Any]]] = {}
    expected_boundaries: dict[str, Any] = {}
    expected_protected["front"], boundaries = front_boundaries(
        views["front"],
        expected_masks["front"],
        auxiliaries["front"],
        config["front_interpretation"],
    )
    expected_boundaries.update(boundaries)
    expected_protected["right"], boundaries = right_boundaries(
        views["right"],
        expected_masks["right"],
        auxiliaries["right"],
        config["right_interpretation"],
    )
    expected_boundaries.update(boundaries)
    for name in ("top", "bottom"):
        expected_protected[name], boundaries = axial_boundaries(
            views[name], expected_masks[name], auxiliaries[name]
        )
        expected_boundaries.update(boundaries)
    for name in ("front", "right", "top", "bottom"):
        actual_protected = scan["views"][name]["protected_negative_spaces"]
        protected_valid = True
        union = bytearray(views[name].width * views[name].height)
        for item in actual_protected:
            y = item["y"]
            for start, end in item["runs_half_open"]:
                if not (
                    views[name].x0 <= start < end <= views[name].x1
                    and views[name].y0 <= y < views[name].y1
                ):
                    protected_valid = False
                    continue
                for x in range(start, end):
                    pixel = views[name].index(x, y)
                    if (
                        not views[name].exterior[pixel]
                        or any(mask[pixel] for mask in actual_masks[name].values())
                    ):
                        protected_valid = False
                    union[pixel] = 1
        audit.check(
            f"{name}_protected_negative_space_replay",
            protected_valid
            and actual_protected == expected_protected[name],
            {
                "record_count": len(actual_protected),
                "unique_pixel_count": sum(union),
            },
        )
    audit.check(
        "boundary_edge_sets_independent_replay",
        index["boundaries"] == expected_boundaries,
        {
            "boundary_count": len(expected_boundaries),
            "boundary_ids": sorted(expected_boundaries),
        },
    )
    required_correspondence = [
        {
            "id": "CORR_C02_FRONT_TOP_BOTTOM_INNER_OWNER_EDGES",
            "component": "C02_STONE_LEFT",
            "ordered_boundary_ids": [
                "FRONT_C02_INNER_OWNER_EDGE",
                "TOP_C02_INNER_OWNER_EDGE",
                "BOTTOM_C02_INNER_OWNER_EDGE",
            ],
            "scope": "ordered exact source-edge sets only; no point pairing or surface created",
        },
        {
            "id": "CORR_C03_FRONT_TOP_BOTTOM_INNER_OWNER_EDGES",
            "component": "C03_STONE_RIGHT",
            "ordered_boundary_ids": [
                "FRONT_C03_INNER_OWNER_EDGE",
                "TOP_C03_INNER_OWNER_EDGE",
                "BOTTOM_C03_INNER_OWNER_EDGE",
            ],
            "scope": "ordered exact source-edge sets only; no point pairing or surface created",
        },
        {
            "id": "CORR_C04_RIGHT_CANDIDATE_FACE_EDGES",
            "component": "C04_STRIKE_FACE_POSITIVE_X",
            "ordered_boundary_ids": [
                "RIGHT_C04_CANDIDATE_HALF_BOUNDARIES",
                "RIGHT_C04_TOP_BOTTOM_EDGES",
            ],
            "scope": "two candidate-specific ordered source-edge sets about x=557",
        },
        {
            "id": "CORR_C01_C06_C07_FRONT_CONTACTS",
            "component": "C06_UPPER_HAFT_CAP",
            "ordered_boundary_ids": [
                "FRONT_C01_C06_CONTACT",
                "FRONT_C06_C07_CONTACT",
            ],
            "scope": "exact adjacent source-row edge sets only",
        },
    ]
    audit.check(
        "correspondence_groups_are_order_only",
        index["correspondence_groups"] == required_correspondence
        and all(
            boundary in expected_boundaries
            for group in required_correspondence
            for boundary in group["ordered_boundary_ids"]
        ),
        [group["id"] for group in required_correspondence],
    )

    reproduced_marked: dict[str, Image.Image] = {}
    review_changed_counts: dict[str, int] = {}
    for name in ("front", "right", "top", "bottom"):
        reproduced = reproduce_marked(
            views[name],
            expected_masks[name],
            expected_boundaries,
            expected_protected[name],
        )
        reproduced_marked[name] = reproduced
        review_spec = index["review_files"][name]
        actual_path = ROOT / review_spec["path"]
        actual = Image.open(actual_path).convert("RGB")
        source_crop = views[name].source.crop(views[name].rectangle)
        changed = sum(
            first != second
            for first, second in zip(
                reproduced.getdata(), source_crop.getdata()
            )
        )
        review_changed_counts[name] = changed
        audit.check(
            f"{name}_thin_mark_review_pixel_replay",
            actual.size == reproduced.size
            and actual.tobytes() == reproduced.tobytes()
            and sha256(actual_path) == review_spec["sha256"],
            {
                "size": list(reproduced.size),
                "changed_source_pixel_count": changed,
                "sha256": sha256(actual_path),
            },
        )
    reproduced_board = reproduce_board(reproduced_marked)
    board_spec = index["review_board"]
    board_path = ROOT / board_spec["path"]
    actual_board = Image.open(board_path).convert("RGB")
    audit.check(
        "combined_review_board_pixel_replay",
        actual_board.size == reproduced_board.size
        and actual_board.tobytes() == reproduced_board.tobytes()
        and sha256(board_path) == board_spec["sha256"]
        and board_spec["classification"]
        == "source pixels with thin exact marks only",
        {
            "size": list(actual_board.size),
            "sha256": sha256(board_path),
        },
    )

    flags_ok = (
        scan.get("geometry_created") is False
        and scan.get("candidate_fill_review_created") is False
        and index.get("production_blueprint_created") is False
        and index.get("blender_or_geometry_created") is False
        and index.get("export_or_unreal_created") is False
        and index["evidence_interpretation_separation"].get(
            "geometry_or_hidden_surface"
        )
        is False
    )
    audit.check("no_geometry_or_fill_flags", flags_ok)
    allowed_files = {
        "steps/STEP_09A_APPROVAL_RECORD.md",
        "steps/STEP_09A_CONTRACT.md",
        "steps/STEP_09A_OUTPUT_RECORD.md",
        "handoffs/STEP_09A_TO_STEP_11_HANDOFF.md",
        "manifests/STEP_STATE.json",
        "manifests/STEP_09A_INTERPRETATION_INPUT.json",
        "manifests/STEP_09A_BOUNDARY_AND_CORRESPONDENCE_INDEX.json",
        "manifests/STEP_09A_VALIDATION.json",
        "evidence/STEP_09A_COMPONENT_SCANLINES.json.gz",
        "evidence/STEP_09A_EXACT_MARKS/STEP_09A_FRONT_EXACT_MARKS.png",
        "evidence/STEP_09A_EXACT_MARKS/STEP_09A_RIGHT_EXACT_MARKS.png",
        "evidence/STEP_09A_EXACT_MARKS/STEP_09A_TOP_EXACT_MARKS.png",
        "evidence/STEP_09A_EXACT_MARKS/STEP_09A_BOTTOM_EXACT_MARKS.png",
        "review/STEP_09A_COMPONENT_PIXEL_OWNERSHIP_REVIEW.png",
    }
    current_files = {
        str(path.relative_to(RUN_ROOT))
        for path in RUN_ROOT.rglob("*")
        if path.is_file()
    }
    unexpected = sorted(current_files - allowed_files)
    geometry_extensions = {
        path
        for path in current_files
        if Path(path).suffix.lower()
        in {".blend", ".fbx", ".obj", ".gltf", ".glb", ".uasset", ".umap"}
    }
    audit.check(
        "run_artifact_allowlist_and_no_geometry",
        not unexpected and not geometry_extensions,
        {
            "unexpected": unexpected,
            "geometry_extensions": sorted(geometry_extensions),
        },
    )
    builder_tree = ast.parse(BUILDER_PATH.read_text(encoding="utf-8"))
    imported_roots: set[str] = set()
    for node in ast.walk(builder_tree):
        if isinstance(node, ast.Import):
            imported_roots.update(alias.name.split(".")[0] for alias in node.names)
        elif isinstance(node, ast.ImportFrom) and node.module:
            imported_roots.add(node.module.split(".")[0])
    disallowed_imports = imported_roots & {
        "bpy",
        "subprocess",
        "trimesh",
        "open3d",
        "torch",
    }
    audit.check(
        "builder_has_no_dcc_or_process_import",
        not disallowed_imports,
        {"imports": sorted(imported_roots)},
    )

    result = "PASS" if not audit.failed else "FAIL"
    validation = {
        "schema": "AERATHEA_R8_STEP09A_INDEPENDENT_VALIDATION_V1",
        "asset": ASSET,
        "run_id": RUN_ID,
        "artifact_status": "proof only",
        "result": result,
        "summary": {
            "passed": audit.passed,
            "total": len(audit.checks),
            "failed_check_ids": audit.failed,
        },
        "authority": {
            "interpretation_input_sha256": input_hash,
            "approval_record_sha256": sha256(approval_path),
            "execution_contract_sha256": sha256(contract_path),
            **{
                key: sha256(path)
                for key, path in authority_paths.items()
            },
        },
        "reconstructed_view_summary": view_summaries,
        "review_changed_source_pixel_counts": review_changed_counts,
        "checks": audit.checks,
        "geometry_or_blender_created": False,
        "candidate_fill_review_created": False,
        "decision": (
            "candidate pending Flamestrike source-ownership decision"
            if result == "PASS"
            else "Blueprint block: source authority missing"
        ),
    }
    VALIDATION_PATH.parent.mkdir(parents=True, exist_ok=True)
    VALIDATION_PATH.write_text(
        json.dumps(validation, indent=2, sort_keys=True) + "\n",
        encoding="utf-8",
    )
    print(
        f"AERATHEA_STEP09A_INDEPENDENT_AUDIT_{result} "
        f"{audit.passed}/{len(audit.checks)} "
        f"validation={VALIDATION_PATH.relative_to(ROOT)}"
    )
    if audit.failed:
        print("failed=" + ",".join(audit.failed))
        return 1
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
