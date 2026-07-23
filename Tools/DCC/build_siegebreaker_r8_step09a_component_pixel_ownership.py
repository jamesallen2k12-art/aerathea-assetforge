#!/usr/bin/env python3
"""Build the measurement-only Siege Breaker R8 Step 09A ownership package.

This script creates coordinate records and thin source-pixel marks only.
It creates no geometry, component-fill review, render, export, or Unreal data.
"""

from __future__ import annotations

from collections import deque
from dataclasses import dataclass
from fractions import Fraction
import gzip
import hashlib
import json
from pathlib import Path
from typing import Any, Iterable

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
MARK_ROOT = RUN_ROOT / "evidence/STEP_09A_EXACT_MARKS"
BOARD_PATH = RUN_ROOT / "review/STEP_09A_COMPONENT_PIXEL_OWNERSHIP_REVIEW.png"


@dataclass
class ViewData:
    name: str
    source_path: Path
    capture_path: Path
    rectangle: tuple[int, int, int, int]
    selected: bytearray
    exterior: bytearray
    domain: bytearray
    width: int
    height: int
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

    def in_rectangle(self, x: int, y: int) -> bool:
        return self.x0 <= x < self.x1 and self.y0 <= y < self.y1


def sha256(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest()


def canonical_json_bytes(value: Any) -> bytes:
    return (
        json.dumps(value, sort_keys=True, separators=(",", ":"), ensure_ascii=True)
        + "\n"
    ).encode("utf-8")


def write_json(path: Path, value: Any) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(
        json.dumps(value, indent=2, sort_keys=True) + "\n",
        encoding="utf-8",
    )


def write_deterministic_gzip(path: Path, value: Any) -> str:
    payload = canonical_json_bytes(value)
    path.parent.mkdir(parents=True, exist_ok=True)
    with path.open("wb") as raw:
        with gzip.GzipFile(filename="", mode="wb", fileobj=raw, mtime=0) as stream:
            stream.write(payload)
    return hashlib.sha256(payload).hexdigest()


def load_capture(view: str, spec: dict[str, Any]) -> ViewData:
    source_path = ROOT / spec["source_path"]
    capture_path = ROOT / spec["capture_path"]
    if sha256(source_path) != spec["source_sha256"]:
        raise RuntimeError(f"{view}: source hash mismatch")
    if sha256(capture_path) != spec["capture_sha256"]:
        raise RuntimeError(f"{view}: capture hash mismatch")

    with gzip.open(capture_path, "rt", encoding="utf-8") as stream:
        capture = json.load(stream)
    if capture["schema"] != "AERATHEA_COMPLETE_HAMMER_RGBA_SCANLINES_V1":
        raise RuntimeError(f"{view}: unexpected capture schema")
    rectangle = tuple(capture["rectangle_half_open"])
    if list(rectangle) != spec["rectangle_half_open"]:
        raise RuntimeError(f"{view}: rectangle mismatch")
    x0, y0, x1, y1 = rectangle
    width = x1 - x0
    height = y1 - y0
    selected = bytearray(width * height)
    for row in capture["rows_with_exact_rgba"]:
        y = row["y"]
        if not y0 <= y < y1:
            raise RuntimeError(f"{view}: capture row outside rectangle")
        offset = (y - y0) * width
        for run in row["runs"]:
            run_x0 = run["x0"]
            run_x1 = run["x1"]
            if not x0 <= run_x0 < run_x1 <= x1:
                raise RuntimeError(f"{view}: capture run outside rectangle")
            local_x0 = run_x0 - x0
            local_x1 = run_x1 - x0
            selected[offset + local_x0 : offset + local_x1] = (
                b"\x01" * (local_x1 - local_x0)
            )

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
    return ViewData(
        name=view,
        source_path=source_path,
        capture_path=capture_path,
        rectangle=rectangle,
        selected=selected,
        exterior=exterior,
        domain=domain,
        width=width,
        height=height,
        source=source,
    )


def row_runs(
    view: ViewData,
    mask: bytearray,
    y: int,
    limit: tuple[int, int] | None = None,
) -> list[list[int]]:
    if not view.y0 <= y < view.y1:
        return []
    start_x = view.x0 if limit is None else max(view.x0, limit[0])
    end_x = view.x1 if limit is None else min(view.x1, limit[1])
    offset = (y - view.y0) * view.width
    runs: list[list[int]] = []
    x = start_x
    while x < end_x:
        if mask[offset + x - view.x0]:
            run_start = x
            x += 1
            while x < end_x and mask[offset + x - view.x0]:
                x += 1
            runs.append([run_start, x])
        else:
            x += 1
    return runs


def intersection_runs(
    view: ViewData,
    first: bytearray,
    second: bytearray,
    y: int,
) -> list[list[int]]:
    mask = bytearray(view.width)
    offset = (y - view.y0) * view.width
    for local_x in range(view.width):
        if first[offset + local_x] and second[offset + local_x]:
            mask[local_x] = 1
    runs: list[list[int]] = []
    local_x = 0
    while local_x < view.width:
        if mask[local_x]:
            start = local_x
            local_x += 1
            while local_x < view.width and mask[local_x]:
                local_x += 1
            runs.append([view.x0 + start, view.x0 + local_x])
        else:
            local_x += 1
    return runs


def difference_runs(
    view: ViewData,
    first: bytearray,
    second: bytearray,
    y: int,
) -> list[list[int]]:
    mask = bytearray(view.width)
    offset = (y - view.y0) * view.width
    for local_x in range(view.width):
        if first[offset + local_x] and not second[offset + local_x]:
            mask[local_x] = 1
    runs: list[list[int]] = []
    local_x = 0
    while local_x < view.width:
        if mask[local_x]:
            start = local_x
            local_x += 1
            while local_x < view.width and mask[local_x]:
                local_x += 1
            runs.append([view.x0 + start, view.x0 + local_x])
        else:
            local_x += 1
    return runs


def runs_pixel_count(runs: Iterable[list[int]]) -> int:
    return sum(end - start for start, end in runs)


def component_row_records(
    view: ViewData, component: bytearray
) -> tuple[list[dict[str, Any]], int, int, int]:
    rows: list[dict[str, Any]] = []
    owner_total = 0
    selected_total = 0
    enclosed_total = 0
    for y in range(view.y0, view.y1):
        owner_runs = row_runs(view, component, y)
        if not owner_runs:
            continue
        selected_runs = intersection_runs(view, component, view.selected, y)
        enclosed_runs = difference_runs(view, component, view.selected, y)
        owner_count = runs_pixel_count(owner_runs)
        selected_count = runs_pixel_count(selected_runs)
        enclosed_count = runs_pixel_count(enclosed_runs)
        owner_total += owner_count
        selected_total += selected_count
        enclosed_total += enclosed_count
        rows.append(
            {
                "y": y,
                "owner_runs_half_open": owner_runs,
                "selected_runs_half_open": selected_runs,
                "enclosed_source_runs_half_open": enclosed_runs,
                "owner_pixel_count": owner_count,
            }
        )
    return rows, owner_total, selected_total, enclosed_total


def round_nearest_ties_lower(value: Fraction) -> int:
    lower = value.numerator // value.denominator
    remainder = value.numerator - lower * value.denominator
    if remainder * 2 <= value.denominator:
        return lower
    return lower + 1


def interpolate_fraction(
    anchors: dict[int, Fraction], target_y: int
) -> Fraction:
    exact = anchors.get(target_y)
    if exact is not None:
        return exact
    ordered = sorted(anchors)
    lower = [y for y in ordered if y < target_y]
    upper = [y for y in ordered if y > target_y]
    if not lower:
        return anchors[upper[0]]
    if not upper:
        return anchors[lower[-1]]
    lower_y = lower[-1]
    upper_y = upper[0]
    ratio = Fraction(target_y - lower_y, upper_y - lower_y)
    return anchors[lower_y] + (anchors[upper_y] - anchors[lower_y]) * ratio


def interval_contains_edge(interval: list[int], edge: Fraction) -> bool:
    return Fraction(interval[0], 1) <= edge < Fraction(interval[1], 1)


def axis_gap_observations(
    view: ViewData,
    axis_edge: Fraction,
    y_start: int,
    y_end: int,
) -> tuple[
    dict[int, tuple[int, int]],
    dict[int, tuple[int, int]],
    set[int],
]:
    left: dict[int, tuple[int, int]] = {}
    right: dict[int, tuple[int, int]] = {}
    axis_absent: set[int] = set()
    for y in range(y_start, y_end):
        runs = row_runs(view, view.domain, y)
        center_index = next(
            (
                index
                for index, interval in enumerate(runs)
                if interval_contains_edge(interval, axis_edge)
            ),
            None,
        )
        if center_index is None:
            axis_absent.add(y)
            continue
        if center_index > 0:
            left[y] = (
                runs[center_index - 1][1],
                runs[center_index][0],
            )
        if center_index + 1 < len(runs):
            right[y] = (
                runs[center_index][1],
                runs[center_index + 1][0],
            )
    return left, right, axis_absent


def cut_series(
    observations: dict[int, tuple[int, int]],
    y_start: int,
    y_end: int,
) -> dict[int, int]:
    if not observations:
        raise RuntimeError("No source gap observations available for contact cuts")
    anchors = {
        y: Fraction(first_edge + second_edge, 2)
        for y, (first_edge, second_edge) in observations.items()
    }
    return {
        y: round_nearest_ties_lower(interpolate_fraction(anchors, y))
        for y in range(y_start, y_end)
    }


def empty_mask(view: ViewData) -> bytearray:
    return bytearray(view.width * view.height)


def set_pixel(view: ViewData, mask: bytearray, x: int, y: int) -> None:
    mask[view.index(x, y)] = 1


def protected_runs_between(
    view: ViewData, y: int, start_x: int, end_x: int
) -> list[list[int]]:
    if end_x <= start_x:
        return []
    return row_runs(view, view.exterior, y, (start_x, end_x))


def build_front(
    view: ViewData, interpretation: dict[str, Any]
) -> tuple[dict[str, bytearray], list[dict[str, Any]], dict[str, Any]]:
    axis = Fraction(interpretation["structural_axis_source_edge_x"], 1)
    stone_y0, stone_y1 = interpretation["stone_rows_half_open"]
    c01_y0, c01_y1 = interpretation["c01_rows_half_open"]
    c12_y0, c12_y1 = interpretation["c12_reserved_rows_half_open"]
    c06_y0, c06_y1 = interpretation["c06_rows_half_open"]

    left_observed, right_observed, axis_absent = axis_gap_observations(
        view, axis, stone_y0, stone_y1
    )
    if axis_absent:
        raise RuntimeError(
            f"front: structural-axis domain absent on rows {sorted(axis_absent)}"
        )
    left_cuts = cut_series(left_observed, stone_y0, stone_y1)
    right_cuts = cut_series(right_observed, stone_y0, stone_y1)

    components = {
        "C01_CENTER_CORE": empty_mask(view),
        "C02_STONE_LEFT": empty_mask(view),
        "C03_STONE_RIGHT": empty_mask(view),
        "C06_UPPER_HAFT_CAP": empty_mask(view),
        "C12_RESERVED_EXISTING_OWNER": empty_mask(view),
    }

    for y in range(stone_y0, stone_y1):
        left_cut = left_cuts[y]
        right_cut = right_cuts[y]
        if not left_cut < axis < right_cut:
            raise RuntimeError(f"front: invalid contact cuts on row {y}")
        for x in range(view.x0, view.x1):
            if not view.domain[view.index(x, y)]:
                continue
            if x < left_cut:
                set_pixel(view, components["C02_STONE_LEFT"], x, y)
            elif x >= right_cut:
                set_pixel(view, components["C03_STONE_RIGHT"], x, y)
            elif c01_y0 <= y < c01_y1:
                set_pixel(view, components["C01_CENTER_CORE"], x, y)
            elif c12_y0 <= y < c12_y1:
                set_pixel(view, components["C12_RESERVED_EXISTING_OWNER"], x, y)

    for y in range(c06_y0, c06_y1):
        for x in range(view.x0, view.x1):
            if view.domain[view.index(x, y)]:
                set_pixel(view, components["C06_UPPER_HAFT_CAP"], x, y)

    protected: list[dict[str, Any]] = []
    left_samples: list[dict[str, Any]] = []
    right_samples: list[dict[str, Any]] = []
    central_union = bytearray(
        1
        if components["C01_CENTER_CORE"][index]
        or components["C12_RESERVED_EXISTING_OWNER"][index]
        else 0
        for index in range(view.width * view.height)
    )

    for y in range(stone_y0, stone_y1):
        left_runs = row_runs(view, components["C02_STONE_LEFT"], y)
        center_runs = row_runs(view, central_union, y)
        right_runs = row_runs(view, components["C03_STONE_RIGHT"], y)
        if left_runs and center_runs:
            left_edge = left_runs[-1][1]
            center_edge = center_runs[0][0]
            gap_runs = protected_runs_between(view, y, left_edge, center_edge)
            mode = "protected_gap" if gap_runs else "shared_contact_cut"
            sample = {
                "y": y,
                "mode": mode,
                "c02_owner_edge_x": left_edge,
                "central_owner_edge_x": center_edge,
                "partition_cut_edge_x": left_cuts[y],
            }
            if gap_runs:
                sample["protected_runs_half_open"] = gap_runs
                protected.append(
                    {
                        "view": "front",
                        "y": y,
                        "between": "C02_STONE_LEFT and central owner",
                        "runs_half_open": gap_runs,
                    }
                )
            left_samples.append(sample)
        if center_runs and right_runs:
            center_edge = center_runs[-1][1]
            right_edge = right_runs[0][0]
            gap_runs = protected_runs_between(view, y, center_edge, right_edge)
            mode = "protected_gap" if gap_runs else "shared_contact_cut"
            sample = {
                "y": y,
                "mode": mode,
                "central_owner_edge_x": center_edge,
                "c03_owner_edge_x": right_edge,
                "partition_cut_edge_x": right_cuts[y],
            }
            if gap_runs:
                sample["protected_runs_half_open"] = gap_runs
                protected.append(
                    {
                        "view": "front",
                        "y": y,
                        "between": "central owner and C03_STONE_RIGHT",
                        "runs_half_open": gap_runs,
                    }
                )
            right_samples.append(sample)

    c01_last_y = c01_y1 - 1
    c06_first_y = c06_y0
    c06_last_y = c06_y1 - 1
    c07_first_y = c06_y1
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
            "c01_last_source_row": c01_last_y,
            "c01_owner_runs_half_open": row_runs(
                view, components["C01_CENTER_CORE"], c01_last_y
            ),
            "shared_source_edge_y": c06_y0,
            "c06_first_source_row": c06_first_y,
            "c06_owner_runs_half_open": row_runs(
                view, components["C06_UPPER_HAFT_CAP"], c06_first_y
            ),
        },
        "FRONT_C06_C07_CONTACT": {
            "view": "front",
            "order": "source_x_ascending",
            "c06_last_source_row": c06_last_y,
            "c06_owner_runs_half_open": row_runs(
                view, components["C06_UPPER_HAFT_CAP"], c06_last_y
            ),
            "shared_source_edge_y": c07_first_y,
            "c07_existing_station_source_row": c07_first_y,
            "c07_source_domain_runs_half_open": row_runs(
                view, view.domain, c07_first_y
            ),
        },
        "FRONT_C12_RESERVED_C01_CONTACT": {
            "view": "front",
            "order": "source_x_ascending",
            "shared_source_edge_y": c01_y0,
            "classification": "candidate C01 upper visibility edge; C12 shape is not re-decided",
            "c12_reserved_last_source_row": c01_y0 - 1,
            "c12_reserved_runs_half_open": row_runs(
                view,
                components["C12_RESERVED_EXISTING_OWNER"],
                c01_y0 - 1,
            ),
            "c01_first_source_row": c01_y0,
            "c01_owner_runs_half_open": row_runs(
                view, components["C01_CENTER_CORE"], c01_y0
            ),
        },
    }
    return components, protected, boundaries


def build_axial(
    view: ViewData, axis_edge: Fraction
) -> tuple[dict[str, bytearray], list[dict[str, Any]], dict[str, Any]]:
    left_observed, right_observed, axis_absent = axis_gap_observations(
        view, axis_edge, view.y0, view.y1
    )
    left_cuts = cut_series(left_observed, view.y0, view.y1)
    right_cuts = cut_series(right_observed, view.y0, view.y1)
    components = {
        "C02_STONE_LEFT": empty_mask(view),
        "C03_STONE_RIGHT": empty_mask(view),
        "CENTRAL_NON_STONE_RESERVED": empty_mask(view),
    }

    for y in range(view.y0, view.y1):
        for x in range(view.x0, view.x1):
            if not view.domain[view.index(x, y)]:
                continue
            if y in axis_absent:
                if Fraction(x + 1, 1) <= axis_edge:
                    set_pixel(view, components["C02_STONE_LEFT"], x, y)
                elif Fraction(x, 1) >= axis_edge:
                    set_pixel(view, components["C03_STONE_RIGHT"], x, y)
                else:
                    raise RuntimeError(
                        f"{view.name}: axis crosses an owned pixel on absent row {y}"
                    )
                continue
            left_cut = left_cuts[y]
            right_cut = right_cuts[y]
            if not Fraction(left_cut, 1) < axis_edge < Fraction(right_cut, 1):
                raise RuntimeError(f"{view.name}: invalid contact cuts on row {y}")
            if x < left_cut:
                set_pixel(view, components["C02_STONE_LEFT"], x, y)
            elif x >= right_cut:
                set_pixel(view, components["C03_STONE_RIGHT"], x, y)
            else:
                set_pixel(view, components["CENTRAL_NON_STONE_RESERVED"], x, y)

    protected: list[dict[str, Any]] = []
    left_samples: list[dict[str, Any]] = []
    right_samples: list[dict[str, Any]] = []
    separated_samples: list[dict[str, Any]] = []

    for y in range(view.y0, view.y1):
        left_runs = row_runs(view, components["C02_STONE_LEFT"], y)
        center_runs = row_runs(view, components["CENTRAL_NON_STONE_RESERVED"], y)
        right_runs = row_runs(view, components["C03_STONE_RIGHT"], y)
        if center_runs:
            if left_runs:
                left_edge = left_runs[-1][1]
                center_edge = center_runs[0][0]
                gap_runs = protected_runs_between(view, y, left_edge, center_edge)
                sample = {
                    "y": y,
                    "mode": "protected_gap"
                    if gap_runs
                    else "shared_contact_cut",
                    "c02_owner_edge_x": left_edge,
                    "central_owner_edge_x": center_edge,
                    "partition_cut_edge_x": left_cuts[y],
                }
                if gap_runs:
                    sample["protected_runs_half_open"] = gap_runs
                    protected.append(
                        {
                            "view": view.name,
                            "y": y,
                            "between": "C02_STONE_LEFT and central non-stone owner",
                            "runs_half_open": gap_runs,
                        }
                    )
                left_samples.append(sample)
            if right_runs:
                center_edge = center_runs[-1][1]
                right_edge = right_runs[0][0]
                gap_runs = protected_runs_between(view, y, center_edge, right_edge)
                sample = {
                    "y": y,
                    "mode": "protected_gap"
                    if gap_runs
                    else "shared_contact_cut",
                    "central_owner_edge_x": center_edge,
                    "c03_owner_edge_x": right_edge,
                    "partition_cut_edge_x": right_cuts[y],
                }
                if gap_runs:
                    sample["protected_runs_half_open"] = gap_runs
                    protected.append(
                        {
                            "view": view.name,
                            "y": y,
                            "between": "central non-stone owner and C03_STONE_RIGHT",
                            "runs_half_open": gap_runs,
                        }
                    )
                right_samples.append(sample)
        elif left_runs and right_runs:
            left_edge = left_runs[-1][1]
            right_edge = right_runs[0][0]
            gap_runs = protected_runs_between(view, y, left_edge, right_edge)
            if gap_runs:
                protected.append(
                    {
                        "view": view.name,
                        "y": y,
                        "between": "C02_STONE_LEFT and C03_STONE_RIGHT with no central owner",
                        "runs_half_open": gap_runs,
                    }
                )
            separated_samples.append(
                {
                    "y": y,
                    "c02_owner_edge_x": left_edge,
                    "c03_owner_edge_x": right_edge,
                    "protected_runs_half_open": gap_runs,
                }
            )

    prefix = view.name.upper()
    boundaries = {
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
            "samples": separated_samples,
        },
    }
    return components, protected, boundaries


def anchor_series(
    anchors: list[list[int]], y_start: int, y_end: int
) -> dict[int, int]:
    values = {int(y): Fraction(int(x), 1) for y, x in anchors}
    return {
        y: round_nearest_ties_lower(interpolate_fraction(values, y))
        for y in range(y_start, y_end)
    }


def build_right(
    view: ViewData, interpretation: dict[str, Any]
) -> tuple[dict[str, bytearray], list[dict[str, Any]], dict[str, Any]]:
    y0, y1 = interpretation["c04_rows_half_open"]
    axis = interpretation["rotation_axis_source_edge_x"]
    rune_interval = tuple(
        interpretation["candidate_intervals_half_open"]["rune_side"]
    )
    metal_interval = tuple(
        interpretation["candidate_intervals_half_open"][
            "metal_center_piece_side"
        ]
    )
    face_left = anchor_series(
        interpretation["metal_half_c04_left_edge_anchors"], y0, y1
    )
    components = {
        "C04_RUNE_SIDE": empty_mask(view),
        "C04_METAL_CENTER_PIECE_SIDE": empty_mask(view),
        "C01_SIDE_RESERVED_IN_METAL_HALF": empty_mask(view),
    }
    for y in range(y0, y1):
        left_edge = face_left[y]
        if not metal_interval[0] <= left_edge <= axis:
            raise RuntimeError(f"right: invalid face-left edge on row {y}")
        for x in range(view.x0, view.x1):
            if not view.domain[view.index(x, y)]:
                continue
            if rune_interval[0] <= x < rune_interval[1]:
                set_pixel(view, components["C04_RUNE_SIDE"], x, y)
            if metal_interval[0] <= x < left_edge:
                set_pixel(
                    view,
                    components["C01_SIDE_RESERVED_IN_METAL_HALF"],
                    x,
                    y,
                )
            elif left_edge <= x < metal_interval[1]:
                set_pixel(
                    view,
                    components["C04_METAL_CENTER_PIECE_SIDE"],
                    x,
                    y,
                )

    protected: list[dict[str, Any]] = []
    samples: list[dict[str, Any]] = []
    for y in range(y0, y1):
        metal_runs = row_runs(
            view, components["C04_METAL_CENTER_PIECE_SIDE"], y
        )
        rune_runs = row_runs(view, components["C04_RUNE_SIDE"], y)
        reserved_runs = row_runs(
            view, components["C01_SIDE_RESERVED_IN_METAL_HALF"], y
        )
        metal_protected: list[list[int]] = []
        rune_protected: list[list[int]] = []
        if metal_runs:
            metal_protected = protected_runs_between(
                view, y, metal_runs[0][0], metal_runs[-1][1]
            )
        if rune_runs:
            rune_protected = protected_runs_between(
                view, y, rune_runs[0][0], rune_runs[-1][1]
            )
        if metal_protected:
            protected.append(
                {
                    "view": "right",
                    "candidate": "metal_center_piece_side",
                    "y": y,
                    "between": "C04 source-owned runs",
                    "runs_half_open": metal_protected,
                }
            )
        if rune_protected:
            protected.append(
                {
                    "view": "right",
                    "candidate": "rune_side",
                    "y": y,
                    "between": "C04 source-owned runs",
                    "runs_half_open": rune_protected,
                }
            )
        samples.append(
            {
                "y": y,
                "metal_face_left_edge_x": face_left[y],
                "rotation_axis_edge_x": axis,
                "metal_c04_owner_runs_half_open": metal_runs,
                "rune_c04_owner_runs_half_open": rune_runs,
                "c01_side_reserved_runs_half_open": reserved_runs,
                "metal_protected_runs_half_open": metal_protected,
                "rune_protected_runs_half_open": rune_protected,
            }
        )

    boundaries = {
        "RIGHT_C04_CANDIDATE_HALF_BOUNDARIES": {
            "view": "right",
            "order": "source_y_ascending_world_z_descending",
            "candidate_intervals_half_open": {
                "rune_side": list(rune_interval),
                "metal_center_piece_side": list(metal_interval),
            },
            "samples": samples,
        },
        "RIGHT_C04_TOP_BOTTOM_EDGES": {
            "view": "right",
            "order": "source_x_ascending",
            "top_source_edge_y": y0,
            "top_metal_owner_runs_half_open": row_runs(
                view, components["C04_METAL_CENTER_PIECE_SIDE"], y0
            ),
            "top_rune_owner_runs_half_open": row_runs(
                view, components["C04_RUNE_SIDE"], y0
            ),
            "bottom_source_edge_y": y1,
            "bottom_last_source_row": y1 - 1,
            "bottom_metal_owner_runs_half_open": row_runs(
                view, components["C04_METAL_CENTER_PIECE_SIDE"], y1 - 1
            ),
            "bottom_rune_owner_runs_half_open": row_runs(
                view, components["C04_RUNE_SIDE"], y1 - 1
            ),
        },
    }
    return components, protected, boundaries


def serialize_components(
    view: ViewData, components: dict[str, bytearray]
) -> dict[str, Any]:
    result: dict[str, Any] = {}
    for component_id, mask in components.items():
        rows, owner_total, selected_total, enclosed_total = component_row_records(
            view, mask
        )
        result[component_id] = {
            "owner_pixel_count": owner_total,
            "selected_capture_pixel_count": selected_total,
            "enclosed_source_pixel_count": enclosed_total,
            "rows": rows,
        }
    return result


def draw_owned_pixel(
    draw: ImageDraw.ImageDraw,
    view: ViewData,
    source_x: int,
    source_y: int,
    color: tuple[int, int, int],
    allowed: bytearray | None = None,
) -> None:
    if not view.in_rectangle(source_x, source_y):
        return
    if allowed is not None and not allowed[view.index(source_x, source_y)]:
        return
    draw.point((source_x - view.x0, source_y - view.y0), fill=color)


def make_marked_review(
    view: ViewData,
    components: dict[str, bytearray],
    boundaries: dict[str, Any],
    protected: list[dict[str, Any]],
) -> Path:
    crop = view.source.crop(view.rectangle)
    draw = ImageDraw.Draw(crop)
    green = (0, 255, 120)
    orange = (255, 150, 0)
    cyan = (0, 220, 255)
    yellow = (255, 230, 0)
    blue = (0, 120, 255)
    magenta = (255, 0, 220)
    gray = (190, 190, 190)
    red = (255, 20, 20)

    if view.name == "front":
        left = boundaries["FRONT_C02_INNER_OWNER_EDGE"]["samples"]
        right = boundaries["FRONT_C03_INNER_OWNER_EDGE"]["samples"]
        central = bytearray(
            1
            if components["C01_CENTER_CORE"][index]
            or components["C12_RESERVED_EXISTING_OWNER"][index]
            else 0
            for index in range(view.width * view.height)
        )
        for sample in left:
            y = sample["y"]
            draw_owned_pixel(
                draw,
                view,
                sample["c02_owner_edge_x"] - 1,
                y,
                green,
                components["C02_STONE_LEFT"],
            )
            draw_owned_pixel(
                draw,
                view,
                sample["central_owner_edge_x"],
                y,
                cyan,
                central,
            )
        for sample in right:
            y = sample["y"]
            draw_owned_pixel(
                draw,
                view,
                sample["central_owner_edge_x"] - 1,
                y,
                cyan,
                central,
            )
            draw_owned_pixel(
                draw,
                view,
                sample["c03_owner_edge_x"],
                y,
                orange,
                components["C03_STONE_RIGHT"],
            )
        for boundary_id, color, component_id, row_key in (
            (
                "FRONT_C01_C06_CONTACT",
                cyan,
                "C01_CENTER_CORE",
                "c01_last_source_row",
            ),
            (
                "FRONT_C01_C06_CONTACT",
                yellow,
                "C06_UPPER_HAFT_CAP",
                "c06_first_source_row",
            ),
            (
                "FRONT_C06_C07_CONTACT",
                yellow,
                "C06_UPPER_HAFT_CAP",
                "c06_last_source_row",
            ),
            (
                "FRONT_C12_RESERVED_C01_CONTACT",
                gray,
                "C12_RESERVED_EXISTING_OWNER",
                "c12_reserved_last_source_row",
            ),
            (
                "FRONT_C12_RESERVED_C01_CONTACT",
                cyan,
                "C01_CENTER_CORE",
                "c01_first_source_row",
            ),
        ):
            y = boundaries[boundary_id][row_key]
            for start, end in row_runs(view, components[component_id], y):
                for x in range(start, end):
                    draw_owned_pixel(
                        draw, view, x, y, color, components[component_id]
                    )
    elif view.name in ("top", "bottom"):
        prefix = view.name.upper()
        central = components["CENTRAL_NON_STONE_RESERVED"]
        for sample in boundaries[f"{prefix}_C02_INNER_OWNER_EDGE"]["samples"]:
            y = sample["y"]
            draw_owned_pixel(
                draw,
                view,
                sample["c02_owner_edge_x"] - 1,
                y,
                green,
                components["C02_STONE_LEFT"],
            )
            draw_owned_pixel(
                draw,
                view,
                sample["central_owner_edge_x"],
                y,
                gray,
                central,
            )
        for sample in boundaries[f"{prefix}_C03_INNER_OWNER_EDGE"]["samples"]:
            y = sample["y"]
            draw_owned_pixel(
                draw,
                view,
                sample["central_owner_edge_x"] - 1,
                y,
                gray,
                central,
            )
            draw_owned_pixel(
                draw,
                view,
                sample["c03_owner_edge_x"],
                y,
                orange,
                components["C03_STONE_RIGHT"],
            )
        for sample in boundaries[
            f"{prefix}_STONE_SEPARATION_WITHOUT_CENTRAL_OWNER"
        ]["samples"]:
            y = sample["y"]
            draw_owned_pixel(
                draw,
                view,
                sample["c02_owner_edge_x"] - 1,
                y,
                green,
                components["C02_STONE_LEFT"],
            )
            draw_owned_pixel(
                draw,
                view,
                sample["c03_owner_edge_x"],
                y,
                orange,
                components["C03_STONE_RIGHT"],
            )
    elif view.name == "right":
        for sample in boundaries["RIGHT_C04_CANDIDATE_HALF_BOUNDARIES"][
            "samples"
        ]:
            y = sample["y"]
            metal_runs = sample["metal_c04_owner_runs_half_open"]
            rune_runs = sample["rune_c04_owner_runs_half_open"]
            reserved_runs = sample["c01_side_reserved_runs_half_open"]
            if reserved_runs:
                draw_owned_pixel(
                    draw,
                    view,
                    reserved_runs[-1][1] - 1,
                    y,
                    gray,
                    components["C01_SIDE_RESERVED_IN_METAL_HALF"],
                )
            if metal_runs:
                draw_owned_pixel(
                    draw,
                    view,
                    metal_runs[0][0],
                    y,
                    magenta,
                    components["C04_METAL_CENTER_PIECE_SIDE"],
                )
                draw_owned_pixel(
                    draw,
                    view,
                    metal_runs[-1][1] - 1,
                    y,
                    magenta,
                    components["C04_METAL_CENTER_PIECE_SIDE"],
                )
            if rune_runs:
                draw_owned_pixel(
                    draw,
                    view,
                    rune_runs[0][0],
                    y,
                    blue,
                    components["C04_RUNE_SIDE"],
                )
                draw_owned_pixel(
                    draw,
                    view,
                    rune_runs[-1][1] - 1,
                    y,
                    blue,
                    components["C04_RUNE_SIDE"],
                )

    for item in protected:
        y = item["y"]
        for start, end in item["runs_half_open"]:
            if start < end:
                draw_owned_pixel(draw, view, start, y, red, view.exterior)
                draw_owned_pixel(draw, view, end - 1, y, red, view.exterior)

    MARK_ROOT.mkdir(parents=True, exist_ok=True)
    output = MARK_ROOT / f"STEP_09A_{view.name.upper()}_EXACT_MARKS.png"
    crop.save(output, format="PNG", optimize=False, compress_level=9)
    return output


def get_font(size: int) -> ImageFont.ImageFont:
    candidates = (
        Path("/usr/share/fonts/truetype/dejavu/DejaVuSans.ttf"),
        Path("/usr/share/fonts/dejavu/DejaVuSans-Bold.ttf"),
    )
    for path in candidates:
        if path.is_file():
            return ImageFont.truetype(str(path), size=size)
    return ImageFont.load_default()


def compose_board(marked: dict[str, Path]) -> None:
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
        legend_x = 40 + (index % 4) * 490
        legend_y = 112 + (index // 4) * 30
        draw.rectangle((legend_x, legend_y, legend_x + 16, legend_y + 16), fill=color)
        draw.text(
            (legend_x + 23, legend_y - 3),
            label,
            fill=(25, 25, 25),
            font=small_font,
        )

    images = {name: Image.open(path).convert("RGB") for name, path in marked.items()}
    front_head = images["front"].crop((0, 0, images["front"].width, 462))
    right_head = images["right"].crop((0, 0, images["right"].width, 504))
    first_y = 220
    draw.text((90, first_y - 34), "FRONT", fill=(20, 20, 20), font=label_font)
    board.paste(front_head, (90, first_y))
    draw.text((790, first_y - 34), "RIGHT", fill=(20, 20, 20), font=label_font)
    board.paste(right_head, (790, first_y))

    axial_y = 780
    draw.text((35, axial_y - 34), "TOP", fill=(20, 20, 20), font=label_font)
    board.paste(images["top"], (35, axial_y))
    draw.text((1030, axial_y - 34), "BOTTOM", fill=(20, 20, 20), font=label_font)
    board.paste(images["bottom"], (1030, axial_y))
    draw.text(
        (40, 1312),
        "Thin marks identify exact source pixels/edges. Red marks identify exact "
        "source-connected empty-space endpoints.",
        fill=(25, 25, 25),
        font=small_font,
    )
    BOARD_PATH.parent.mkdir(parents=True, exist_ok=True)
    board.save(BOARD_PATH, format="PNG", optimize=False, compress_level=9)


def main() -> None:
    config = json.loads(INPUT_PATH.read_text(encoding="utf-8"))
    views = {
        name: load_capture(name, spec)
        for name, spec in config["immutable_inputs"].items()
    }
    locked_nonowning_views = {
        name: load_capture(name, spec)
        for name, spec in config["locked_nonowning_inputs"].items()
    }

    front_components, front_protected, front_boundaries = build_front(
        views["front"], config["front_interpretation"]
    )
    right_components, right_protected, right_boundaries = build_right(
        views["right"], config["right_interpretation"]
    )
    top_axis = Fraction(
        config["axial_interpretation"]["top_center_source_edge_x"]["numerator"],
        config["axial_interpretation"]["top_center_source_edge_x"]["denominator"],
    )
    bottom_axis = Fraction(
        config["axial_interpretation"]["bottom_center_source_edge_x"][
            "numerator"
        ],
        config["axial_interpretation"]["bottom_center_source_edge_x"][
            "denominator"
        ],
    )
    top_components, top_protected, top_boundaries = build_axial(
        views["top"], top_axis
    )
    bottom_components, bottom_protected, bottom_boundaries = build_axial(
        views["bottom"], bottom_axis
    )

    all_components = {
        "front": front_components,
        "right": right_components,
        "top": top_components,
        "bottom": bottom_components,
    }
    all_protected = {
        "front": front_protected,
        "right": right_protected,
        "top": top_protected,
        "bottom": bottom_protected,
    }
    all_boundaries = {
        **front_boundaries,
        **right_boundaries,
        **top_boundaries,
        **bottom_boundaries,
    }

    scanline_record = {
        "schema": "AERATHEA_R8_STEP09A_COMPONENT_SCANLINES_V1",
        "asset": ASSET,
        "run_id": RUN_ID,
        "artifact_status": "candidate interpretation pending Flamestrike decision",
        "source_edge_convention": {
            "coordinates": "integer half-open source pixel edges",
            "pixel_sample": "(x+1/2,y+1/2)",
            "origin": "upper left",
        },
        "interpretation_input_sha256": sha256(INPUT_PATH),
        "locked_nonowning_inputs": {
            name: {
                "source_sha256": sha256(view.source_path),
                "capture_sha256": sha256(view.capture_path),
                "rectangle_half_open": list(view.rectangle),
                "ownership_output_required": False,
            }
            for name, view in locked_nonowning_views.items()
        },
        "views": {},
        "geometry_created": False,
        "candidate_fill_review_created": False,
    }
    for view_name in ("front", "right", "top", "bottom"):
        view = views[view_name]
        scanline_record["views"][view_name] = {
            "source_sha256": sha256(view.source_path),
            "capture_sha256": sha256(view.capture_path),
            "rectangle_half_open": list(view.rectangle),
            "selected_capture_pixel_count": sum(view.selected),
            "enclosed_source_pixel_count": sum(view.domain) - sum(view.selected),
            "component_owners": serialize_components(
                view, all_components[view_name]
            ),
            "protected_negative_spaces": all_protected[view_name],
        }
    scanline_canonical_sha256 = write_deterministic_gzip(
        SCANLINE_PATH, scanline_record
    )

    marked_paths = {
        "front": make_marked_review(
            views["front"],
            front_components,
            front_boundaries,
            front_protected,
        ),
        "right": make_marked_review(
            views["right"],
            right_components,
            right_boundaries,
            right_protected,
        ),
        "top": make_marked_review(
            views["top"], top_components, top_boundaries, top_protected
        ),
        "bottom": make_marked_review(
            views["bottom"],
            bottom_components,
            bottom_boundaries,
            bottom_protected,
        ),
    }
    compose_board(marked_paths)

    correspondence_groups = [
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
    index = {
        "schema": "AERATHEA_R8_STEP09A_BOUNDARY_CORRESPONDENCE_INDEX_V1",
        "asset": ASSET,
        "run_id": RUN_ID,
        "artifact_status": "candidate interpretation pending Flamestrike decision",
        "interpretation_input_sha256": sha256(INPUT_PATH),
        "locked_nonowning_inputs": {
            name: {
                "source_sha256": sha256(view.source_path),
                "capture_sha256": sha256(view.capture_path),
                "rectangle_half_open": list(view.rectangle),
                "ownership_output_required": False,
            }
            for name, view in locked_nonowning_views.items()
        },
        "component_scanline_file": str(SCANLINE_PATH.relative_to(ROOT)),
        "component_scanline_file_sha256": sha256(SCANLINE_PATH),
        "component_scanline_canonical_sha256": scanline_canonical_sha256,
        "boundaries": all_boundaries,
        "correspondence_groups": correspondence_groups,
        "review_files": {
            name: {
                "path": str(path.relative_to(ROOT)),
                "sha256": sha256(path),
            }
            for name, path in marked_paths.items()
        },
        "review_board": {
            "path": str(BOARD_PATH.relative_to(ROOT)),
            "sha256": sha256(BOARD_PATH),
            "classification": "source pixels with thin exact marks only",
        },
        "evidence_interpretation_separation": {
            "source_pixels_and_prior_membership": "authoritative evidence",
            "component_assignments_and_contact_cuts": "candidate interpretation",
            "correspondence": "ordered edge-set interpretation only",
            "geometry_or_hidden_surface": False,
        },
        "production_blueprint_created": False,
        "blender_or_geometry_created": False,
        "export_or_unreal_created": False,
        "decision": "candidate_pending_independent_audit",
    }
    write_json(INDEX_PATH, index)
    print(
        "AERATHEA_STEP09A_COMPONENT_OWNERSHIP_BUILT "
        f"scanlines={SCANLINE_PATH.relative_to(ROOT)} "
        f"review={BOARD_PATH.relative_to(ROOT)}"
    )


if __name__ == "__main__":
    main()
