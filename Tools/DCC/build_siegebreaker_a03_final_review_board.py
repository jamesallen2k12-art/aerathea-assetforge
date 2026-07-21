#!/usr/bin/env python3
"""Build the visible A03 final DCC review board from audited proof images."""

from __future__ import annotations

import hashlib
import json
from pathlib import Path

from PIL import Image, ImageDraw, ImageFont


ROOT = Path(__file__).resolve().parents[2]
ASSET_ID = "SM_DRW_SiegeBreaker_Hammer_A01"
BLUEPRINT = ROOT / "docs/assets/blueprints" / ASSET_ID
MEASUREMENT = BLUEPRINT / "manifests/VISUAL_FIDELITY_A03_SOURCE_MEASUREMENTS.json"
COMPARISON = BLUEPRINT / "manifests/VISUAL_FIDELITY_A03_PIXEL_COMPARISON.json"
AUDIT = BLUEPRINT / "manifests/VISUAL_FIDELITY_A03_TECHNICAL_AUDIT.json"
SOURCE = ROOT / "SourceAssets/Reference/Weapons/Dwarven" / ASSET_ID / "02_SiegeBreaker_Codex_Final_Package/reference/concept_sheet_style_reference.png"
PROOF_ROOT = ROOT / "Saved/Automation/DCC" / ASSET_ID / "VisualFidelity_A03"
FINAL = PROOF_ROOT / "matched_source_view" / f"{ASSET_ID}_A03_SourceMatched_Final.png"
ORTHOS = PROOF_ROOT / "orthographic_true"
OUTPUT = PROOF_ROOT / "review"
BOARD = OUTPUT / f"{ASSET_ID}_A03_FinalDCCReviewBoard.png"
PACKAGE = BLUEPRINT / "manifests/VISUAL_FIDELITY_A03_REVIEW_PACKAGE.json"
RESAMPLE = getattr(Image, "Resampling", Image).LANCZOS


def sha256(path: Path) -> str:
    digest = hashlib.sha256()
    with path.open("rb") as handle:
        for chunk in iter(lambda: handle.read(1024 * 1024), b""):
            digest.update(chunk)
    return digest.hexdigest()


def font(size, bold=False):
    candidates = [
        Path("/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf" if bold else "/usr/share/fonts/truetype/dejavu/DejaVuSans.ttf"),
        Path("/usr/share/fonts/dejavu/DejaVuSans-Bold.ttf" if bold else "/usr/share/fonts/dejavu/DejaVuSans.ttf"),
    ]
    for path in candidates:
        if path.exists():
            return ImageFont.truetype(str(path), size=size)
    return ImageFont.load_default()


def alpha_crop(image: Image.Image):
    rgba = image.convert("RGBA")
    bbox = rgba.getchannel("A").getbbox()
    return rgba.crop(bbox) if bbox else rgba


def fit(image: Image.Image, size, background=(239, 235, 222, 255), margin=12):
    image = alpha_crop(image)
    available = (max(1, size[0] - margin * 2), max(1, size[1] - margin * 2))
    scale = min(available[0] / image.width, available[1] / image.height)
    resized = image.resize((max(1, round(image.width * scale)), max(1, round(image.height * scale))), RESAMPLE)
    panel = Image.new("RGBA", size, background)
    panel.alpha_composite(resized, ((size[0] - resized.width) // 2, (size[1] - resized.height) // 2))
    return panel.convert("RGB")


def main() -> int:
    OUTPUT.mkdir(parents=True, exist_ok=True)
    measurement = json.loads(MEASUREMENT.read_text(encoding="utf-8"))
    comparison = json.loads(COMPARISON.read_text(encoding="utf-8"))
    audit = json.loads(AUDIT.read_text(encoding="utf-8"))
    bounds = measurement["panels"]["primary_3_4"]["bounds_sheet_px_inclusive"]
    source = Image.open(SOURCE).convert("RGB").crop((bounds[0], bounds[1], bounds[2] + 1, bounds[3] + 1))
    final = Image.open(FINAL).convert("RGBA")

    paper = (239, 235, 222)
    ink = (28, 28, 28)
    border = (104, 98, 86)
    board = Image.new("RGB", (3000, 1800), paper)
    draw = ImageDraw.Draw(board)
    title_font = font(34, True)
    heading_font = font(23, True)
    body_font = font(19, False)
    small_font = font(17, False)
    draw.text((40, 24), "SIEGE BREAKER A03 — PIXEL-RECONSTRUCTED DCC CANDIDATE", fill=ink, font=title_font)
    draw.text((40, 66), "Primary source pixels + exact 52 × 32 × 170 cm envelope; no A01/A02 geometry reused", fill=ink, font=body_font)

    primary_boxes = [(40, 125, 560, 1515), (620, 125, 1140, 1515)]
    primary_titles = ["AUTHORITATIVE 3/4 CONCEPT", "A03 SOURCE-MATCHED FINAL"]
    primary_images = [source.convert("RGBA"), final]
    for box, title, image in zip(primary_boxes, primary_titles, primary_images):
        x0, y0, x1, y1 = box
        draw.text((x0, y0 - 34), title, fill=ink, font=heading_font)
        board.paste(fit(image, (x1 - x0, y1 - y0)), (x0, y0))
        draw.rectangle(box, outline=border, width=2)

    views = ("front", "back", "left", "right", "top", "bottom")
    view_titles = ("FRONT", "BACK", "LEFT", "RIGHT", "TOP", "BOTTOM")
    cell_w, cell_h = 560, 650
    start_x, start_y = 1200, 125
    for index, (name, title) in enumerate(zip(views, view_titles)):
        column = index % 3
        row = index // 3
        x0 = start_x + column * 590
        y0 = start_y + row * 700
        draw.text((x0, y0 - 34), f"TRUE ORTHO — {title}", fill=ink, font=heading_font)
        image = Image.open(ORTHOS / f"{name}.png").convert("RGBA")
        board.paste(fit(image, (cell_w, cell_h), margin=8), (x0, y0))
        draw.rectangle((x0, y0, x0 + cell_w, y0 + cell_h), outline=border, width=2)

    metrics = comparison["metrics"]
    lods = [item["observed"] for item in audit["checks"] if item["id"] == "G19_LOD_MONOTONIC"][0]
    footer_y = 1550
    draw.line((40, footer_y - 20, 2960, footer_y - 20), fill=border, width=2)
    draw.text((40, footer_y), f"Pixel gate: {comparison['summary']['passed']}/{comparison['summary']['total']} PASS", fill=ink, font=heading_font)
    draw.text((390, footer_y), f"Technical audit: {audit['summary']['passed']}/{audit['summary']['total']} PASS", fill=ink, font=heading_font)
    draw.text((850, footer_y), "Status: candidate — pending Flamestrike visual approval", fill=ink, font=heading_font)
    draw.text((40, footer_y + 48), f"Aspect error {metrics['aspect_error_percent']}%   |   Silhouette IoU {metrics['silhouette_iou_after_height_registration']}   |   Row error {metrics['mean_row_boundary_error_over_source_width']} source width   |   Cyan centroid {metrics['cyan_centroid_distance_over_source_height']} source height", fill=ink, font=body_font)
    draw.text((40, footer_y + 83), f"LOD triangles: {lods[0]} / {lods[1]} / {lods[2]} / {lods[3]}   |   5 materials   |   20 × 2K PBR maps   |   3 UCX collision proxies   |   FBX + GLB clean reimport", fill=ink, font=body_font)
    draw.text((40, footer_y + 118), "Unreal authority: false   |   Fully game-ready: false   |   Orthographic views are fixed-object technical proofs, not replacements for visual judgment.", fill=ink, font=small_font)
    board.save(BOARD)

    proofs = [FINAL, *(ORTHOS / f"{name}.png" for name in views), PROOF_ROOT / "comparison" / f"{ASSET_ID}_A03_PixelRegisteredComparisonBoard.png"]
    package = {
        "schema": "aerathea.siegebreaker.a03_review_package.v1",
        "asset_id": ASSET_ID,
        "revision": "PixelReconstruction_A03",
        "contract_id": "SB-VF-A03-PIXEL",
        "artifact_status": "candidate",
        "pipeline_status": "DCC game-ready candidate pending Flamestrike visual approval",
        "review_board": {"path": str(BOARD.relative_to(ROOT)), "sha256": sha256(BOARD)},
        "proofs": [{"path": str(path.relative_to(ROOT)), "sha256": sha256(path)} for path in proofs],
        "pixel_comparison": {"path": str(COMPARISON.relative_to(ROOT)), "sha256": sha256(COMPARISON), "result": comparison["result"], "gates": comparison["summary"]},
        "technical_audit": {"path": str(AUDIT.relative_to(ROOT)), "sha256": sha256(AUDIT), "result": audit["result"], "gates": audit["summary"]},
        "final_visual_approval": "pending Flamestrike",
        "unreal_authorized": False,
        "fully_game_ready": False,
    }
    PACKAGE.write_text(json.dumps(package, indent=2) + "\n", encoding="utf-8")
    print(BOARD)
    print(PACKAGE)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
