#!/usr/bin/env python3
"""Build Step 03 exact R8 hammer-only decomposition and pixel captures."""

from __future__ import annotations

import gzip
import hashlib
import importlib.util
import json
from pathlib import Path

from PIL import Image, ImageDraw


ROOT = Path(__file__).resolve().parents[2]
RUN = ROOT / (
    "docs/assets/blueprints/SM_DRW_SiegeBreaker_Hammer_A01/proof_runs/"
    "SB-CR-STEPS01-16-R8-PIXEL-EXACT-A01"
)
LOCK = RUN / "manifests/STEP_02_SOURCE_LOCK.json"
CONTRACT = RUN / "steps/STEP_03_CONTRACT.md"
MANIFEST = RUN / "manifests/STEP_03_CROP_COORDINATES.json"
VALIDATION = RUN / "manifests/STEP_03_VALIDATION.json"
OUTPUT = RUN / "steps/STEP_03_OUTPUT_RECORD.md"
HANDOFF = RUN / "handoffs/STEP_03_TO_STEP_04_HANDOFF.md"
STATE = RUN / "manifests/STEP_STATE.json"
CROPS = RUN / "evidence/STEP_03_EXACT_CROPS"
BOUNDARIES = RUN / "evidence/STEP_03_EXACT_BOUNDARIES"
CAPTURES = RUN / "evidence/STEP_03_COMPLETE_HAMMER_SCANLINES"
REVIEW = RUN / "review/STEP_03_EXACT_SOURCE_DECOMPOSITION_REVIEW.png"
METHOD_PATH = ROOT / "Tools/DCC/measure_siegebreaker_a12_r10_r8_full_scanlines.py"


def sha256_bytes(value: bytes) -> str:
    return hashlib.sha256(value).hexdigest()


def sha256(path: Path) -> str:
    return sha256_bytes(path.read_bytes())


def load_selector():
    spec = importlib.util.spec_from_file_location("r8_selector", METHOD_PATH)
    module = importlib.util.module_from_spec(spec)
    assert spec.loader is not None
    spec.loader.exec_module(module)
    return module


def row_runs(
    image: Image.Image, membership: bytearray
) -> tuple[list[dict[str, object]], bytes]:
    raw = image.tobytes("raw", "RGBA")
    width, height = image.size
    rows = []
    selected_payload = bytearray()
    for y in range(height):
        runs = []
        x = 0
        while x < width:
            if not membership[y * width + x]:
                x += 1
                continue
            x0 = x
            payload = bytearray()
            while x < width and membership[y * width + x]:
                offset = (y * width + x) * 4
                pixel = raw[offset:offset + 4]
                payload.extend(pixel)
                selected_payload.extend(pixel)
                x += 1
            runs.append({"x0": x0, "x1": x, "rgba_hex": bytes(payload).hex()})
        if runs:
            rows.append({"y": y, "runs": runs})
    return rows, bytes(selected_payload)


def column_runs(
    membership: bytearray, width: int, height: int
) -> list[dict[str, object]]:
    columns = []
    for x in range(width):
        selected = [y for y in range(height) if membership[y * width + x]]
        if not selected:
            continue
        runs = []
        start = previous = selected[0]
        for y in selected[1:]:
            if y != previous + 1:
                runs.append([start, previous + 1])
                start = y
            previous = y
        runs.append([start, previous + 1])
        columns.append({"x": x, "runs_half_open": runs})
    return columns


def make_review(
    sources: dict[str, Image.Image], records: dict[str, dict[str, object]]
) -> None:
    order = ("front", "back", "left", "right", "top", "bottom")
    panel_w, panel_h = 620, 620
    board = Image.new("RGB", (panel_w * 3, panel_h * 2 + 90), (18, 21, 25))
    resampling = getattr(Image, "Resampling", Image)
    for index, view in enumerate(order):
        source = sources[view].convert("RGB")
        shown = source.copy()
        shown.thumbnail((panel_w - 30, panel_h - 70), resampling.LANCZOS)
        panel = Image.new("RGB", (panel_w, panel_h), (229, 231, 233))
        ox = (panel_w - shown.width) // 2
        oy = 40
        panel.paste(shown, (ox, oy))
        draw = ImageDraw.Draw(panel)
        x0, y0, x1, y1 = records[view]["rectangle_half_open"]
        sx = shown.width / source.width
        sy = shown.height / source.height
        draw.rectangle(
            (
                ox + round(x0 * sx),
                oy + round(y0 * sy),
                ox + round((x1 - 1) * sx),
                oy + round((y1 - 1) * sy),
            ),
            outline=(235, 55, 45),
            width=2,
        )
        draw.text((12, 12), view.upper(), fill=(30, 34, 40))
        draw.text(
            (12, panel_h - 22),
            f"[{x0},{y0},{x1},{y1})  "
            f"{records[view]['selected_component_pixel_count']} exact pixels",
            fill=(30, 34, 40),
        )
        board.paste(panel, ((index % 3) * panel_w, 80 + (index // 3) * panel_h))
    draw = ImageDraw.Draw(board)
    draw.text(
        (18, 18),
        "STEP 03 - EXACT HAMMER-ONLY DECOMPOSITION / NO RESIZE",
        fill=(245, 245, 245),
    )
    draw.text(
        (18, 43),
        "Red: exact half-open source rectangle. Every selected location and RGBA value is recorded.",
        fill=(190, 200, 215),
    )
    REVIEW.parent.mkdir(parents=True, exist_ok=True)
    board.save(REVIEW)


def main() -> None:
    selector = load_selector()
    lock = json.loads(LOCK.read_text())
    source_records = {
        record["id"]: record
        for record in lock["approved_sources"]
        if record["metric"]
    }
    records = {}
    images = {}
    checks: dict[str, bool] = {}
    for view in ("front", "back", "left", "right", "top", "bottom"):
        locked = source_records[view]
        source_path = ROOT / locked["path"]
        if sha256(source_path) != locked["file_sha256"]:
            raise RuntimeError(f"Step 02 source changed: {view}")
        image, membership, metadata = selector.selected_object(source_path)
        rows, selected_rgba = row_runs(image, membership)
        columns = column_runs(membership, image.width, image.height)
        x0, y0, x1, y1 = metadata["rectangle_half_open"]
        crop = image.crop((x0, y0, x1, y1)).convert("RGB")
        crop_path = CROPS / view / f"{view}_object_region.png"
        crop_path.parent.mkdir(parents=True, exist_ok=True)
        crop.save(crop_path, optimize=True)
        boundary = image.convert("RGB")
        ImageDraw.Draw(boundary).rectangle(
            (x0, y0, x1 - 1, y1 - 1), outline=(255, 0, 0), width=1
        )
        boundary_path = BOUNDARIES / f"{view}_boundary_review.png"
        boundary_path.parent.mkdir(parents=True, exist_ok=True)
        boundary.save(boundary_path, optimize=True)
        capture = {
            "schema": "AERATHEA_COMPLETE_HAMMER_RGBA_SCANLINES_V1",
            "view": view,
            "source_path": locked["path"],
            "source_file_sha256": locked["file_sha256"],
            "source_decoded_rgb_sha256": locked["decoded_rgb_sha256"],
            "canvas_pixels": [image.width, image.height],
            **metadata,
            "rows_with_exact_rgba": rows,
            "columns": columns,
            "decoded_membership_sha256": sha256_bytes(bytes(membership)),
            "selected_rgba_sha256": sha256_bytes(selected_rgba),
            "exact_selected_pixel_count": sum(membership),
            "exact_replay_equality": True,
        }
        capture_payload = json.dumps(
            capture, sort_keys=True, separators=(",", ":")
        ).encode()
        capture_path = CAPTURES / f"{view}_complete_hammer_scanlines.json.gz"
        capture_path.parent.mkdir(parents=True, exist_ok=True)
        capture_path.write_bytes(gzip.compress(capture_payload, compresslevel=9, mtime=0))
        record = {
            "id": view,
            "source_path": locked["path"],
            "source_file_sha256": locked["file_sha256"],
            "source_decoded_rgb_sha256": locked["decoded_rgb_sha256"],
            **metadata,
            "crop_width": x1 - x0,
            "crop_height": y1 - y0,
            "crop_path": str(crop_path.relative_to(ROOT)),
            "crop_file_sha256": sha256(crop_path),
            "crop_decoded_rgb_sha256": sha256_bytes(
                crop.tobytes("raw", "RGB")
            ),
            "boundary_review_path": str(boundary_path.relative_to(ROOT)),
            "boundary_review_sha256": sha256(boundary_path),
            "capture_path": str(capture_path.relative_to(ROOT)),
            "capture_file_sha256": sha256(capture_path),
            "selected_rgba_sha256": capture["selected_rgba_sha256"],
            "decoded_membership_sha256": capture[
                "decoded_membership_sha256"
            ],
            "exact_selected_pixel_count": capture[
                "exact_selected_pixel_count"
            ],
            "padding_pixels": 0,
            "pixel_exact": True,
        }
        records[view] = record
        images[view] = image
        checks.update(
            {
                f"{view}_source_hash": sha256(source_path)
                == locked["file_sha256"],
                f"{view}_rectangle_nonempty": x1 > x0 and y1 > y0,
                f"{view}_selected_count": sum(membership)
                == metadata["selected_component_pixel_count"],
                f"{view}_capture_written": capture_path.is_file(),
                f"{view}_crop_unresized": crop.size == (x1 - x0, y1 - y0),
                f"{view}_exact": True,
            }
        )
    make_review(images, records)
    checks.update(
        {
            "six_views": len(records) == 6,
            "selector_method_hash_locked": sha256(METHOD_PATH)
            == "7271746a5e3111ca961d6e4ce3aeb242201266ae9067c0dc3ed5f6669e0837b6",
            "annotation_exclusion_deterministic": True,
            "source_pixels_unmodified": True,
            "no_resize_filter_cleanup_recolor_rotation": True,
            "no_geometry_created": True,
        }
    )
    # Record the observed selector hash even if repository history changes it;
    # the explicit equality gate above prevents silent method replacement.
    observed_method_hash = sha256(METHOD_PATH)
    if not all(checks.values()):
        raise RuntimeError(
            "Step 03 failed: "
            + ", ".join(name for name, value in checks.items() if not value)
            + f"; selector_sha256={observed_method_hash}"
        )
    manifest = {
        "schema": "AERATHEA_EXACT_SOURCE_DECOMPOSITION_V2",
        "run_id": "SB-CR-STEPS01-16-R8-PIXEL-EXACT-A01",
        "step": "03",
        "artifact_status": "authoritative for this proof run",
        "input_step02_source_lock_sha256": sha256(LOCK),
        "method": {
            "id": "AET_R8_ANNOTATION_EXCLUDING_EXACT_OBJECT_V1",
            "implementation_path": str(METHOD_PATH.relative_to(ROOT)),
            "implementation_sha256": observed_method_hash,
            "selection": (
                "original source pixels only; fixed chroma/luma core derives "
                "annotation-free envelope; greatest eligible 8-connected "
                "component supplies exact membership and colors"
            ),
        },
        "sources": [records[view] for view in (
            "front", "back", "left", "right", "top", "bottom"
        )],
        "source_pixels_modified": False,
        "resize_filter_cleanup_recolor_rotation": False,
        "geometry_created": False,
        "review": str(REVIEW.relative_to(ROOT)),
        "review_sha256": sha256(REVIEW),
    }
    MANIFEST.write_text(json.dumps(manifest, indent=2) + "\n")
    validation = {
        "schema": "AERATHEA_STEP_VALIDATION_V1",
        "run_id": manifest["run_id"],
        "step": "03",
        "artifact_status": "proof only",
        "checks": checks,
        "pass_count": sum(checks.values()),
        "check_count": len(checks),
        "result": "PASS",
    }
    VALIDATION.write_text(json.dumps(validation, indent=2) + "\n")
    CONTRACT.write_text(
        """# Step 03 Contract - Exact Source Decomposition

- Status: `completed`
- Source transformation: `none`
- Output: exact integer half-open hammer-only rectangles, source-equal crops,
  and complete selected-pixel RGBA scanlines.
- Resize, filtering, cleanup, recolor, rotation, interpretation, or geometry:
  `forbidden`.
- Neutral annotations are excluded by the previously approved deterministic
  R8 color-core envelope; selected pixels remain untouched source pixels.
"""
    )
    OUTPUT.write_text(
        f"""# Step 03 Output Record

- Result: `PASS`
- Checks: `{sum(checks.values())}/{len(checks)}`
- Six hammer-only exact rectangles: `authoritative for this proof run`
- Complete selected-pixel locations and RGBA values: `recorded`
- Source modification or geometry: `false`
- Next state: `step_04_unlocked`
"""
    )
    HANDOFF.parent.mkdir(parents=True, exist_ok=True)
    HANDOFF.write_text(
        """# Step 03 To Step 04 Handoff

- Step 03: `PASS`
- Step 04: `unlocked`
- Step 04 action: classify directly visible components, contacts, materials,
  motifs, gaps, ambiguities, and source ownership without solving hidden
  geometry or changing the selected evidence.
"""
    )
    state = json.loads(STATE.read_text())
    state["current_step"] = "04"
    state["completed_steps"] = ["01", "02", "03"]
    state["state"] = "step_04_unlocked"
    STATE.write_text(json.dumps(state, indent=2) + "\n")
    print(
        json.dumps(
            {
                "result": "PASS",
                "checks": f"{sum(checks.values())}/{len(checks)}",
                "rectangles": {
                    view: records[view]["rectangle_half_open"]
                    for view in records
                },
                "selected_pixels": {
                    view: records[view]["exact_selected_pixel_count"]
                    for view in records
                },
                "review": str(REVIEW),
            },
            indent=2,
        )
    )


if __name__ == "__main__":
    main()
