#!/usr/bin/env python3
"""Rank A03 camera-search renders using the locked pixel-comparison metrics."""

from __future__ import annotations

import importlib.util
import json
from pathlib import Path

from PIL import Image


ROOT = Path(__file__).resolve().parents[2]
ASSET_ID = "SM_DRW_SiegeBreaker_Hammer_A01"
SEARCH = ROOT / "Saved/Automation/DCC" / ASSET_ID / "VisualFidelity_A03/camera_search"
MEASUREMENTS = ROOT / "docs/assets/blueprints" / ASSET_ID / "manifests/VISUAL_FIDELITY_A03_SOURCE_MEASUREMENTS.json"


def load_comparator():
    path = ROOT / "Tools/DCC/compare_siegebreaker_source_a03.py"
    spec = importlib.util.spec_from_file_location("siegebreaker_a03_comparator", path)
    if spec is None or spec.loader is None:
        raise RuntimeError(f"Cannot load comparator: {path}")
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


def main() -> int:
    compare = load_comparator()
    source_sheet = Image.open(compare.SOURCE).convert("RGB")
    measurement = json.loads(MEASUREMENTS.read_text(encoding="utf-8"))
    bounds = measurement["panels"]["primary_3_4"]["bounds_sheet_px_inclusive"]
    source = source_sheet.crop((bounds[0], bounds[1], bounds[2] + 1, bounds[3] + 1))
    source_mask = compare.largest_component(source)
    source_aspect = source.width / source.height
    search_manifest = json.loads((SEARCH / "camera_search_manifest.json").read_text(encoding="utf-8"))
    ranked = []
    for record in search_manifest["renders"]:
        image = Image.open(ROOT / record["path"]).convert("RGBA")
        registered, registration = compare.registered_render(image, source.size)
        render_mask = compare.alpha_mask(registered)
        union = len(source_mask | render_mask)
        iou = len(source_mask & render_mask) / union if union else 0.0
        row_error = compare.row_boundary_error(source_mask, render_mask, source.width, source.height) / source.width
        span = registration["original_alpha_span_px"]
        aspect_error = abs((span[0] / span[1]) / source_aspect - 1.0)
        # Equal normalized weighting: a pass-threshold score below 1.0 means
        # all three silhouette metrics are collectively inside their limits.
        score = aspect_error / 0.04 + (1.0 - iou) / (1.0 - 0.66) + row_error / 0.075
        ranked.append({
            **record,
            "aspect_error_percent": round(aspect_error * 100.0, 3),
            "silhouette_iou": round(iou, 6),
            "row_boundary_error_over_source_width": round(row_error, 6),
            "score": round(score, 6),
            "passes": {
                "aspect": aspect_error <= 0.04,
                "iou": iou >= 0.66,
                "row_error": row_error <= 0.075,
            },
        })
    ranked.sort(key=lambda item: item["score"])
    output = {
        "schema": "aerathea.siegebreaker.camera_search_evaluation.v1",
        "asset_id": ASSET_ID,
        "revision": "PixelReconstruction_A03",
        "contract_id": "SB-VF-A03-PIXEL",
        "artifact_status": "proof only",
        "selection_rule": "lowest normalized silhouette score; no geometry or source modification",
        "best": ranked[0],
        "ranked": ranked,
    }
    path = SEARCH / "camera_search_evaluation.json"
    path.write_text(json.dumps(output, indent=2) + "\n", encoding="utf-8")
    print(path)
    print(json.dumps(ranked[:5], indent=2))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
