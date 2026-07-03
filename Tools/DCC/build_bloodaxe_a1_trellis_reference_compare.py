#!/usr/bin/env python3
"""Build a diagnostic comparison sheet for the Blood Axe A1 TRELLIS reference."""

from __future__ import annotations

import json
from pathlib import Path

from PIL import Image, ImageDraw, ImageFont


ROOT = Path("/home/james/Projects/Aerathea")
ASSET_DOC_DIR = ROOT / "docs/assets/props/SM_GIA_BloodAxeCairnTarget_A1_A01"
BENCH_DIR = ROOT / "Saved/AssetForgeResearch/benchmarks/outputs/trellis-amd/bloodaxe_a1_target_multiview_mesh"

TARGET_SHEET = ASSET_DOC_DIR / "SM_GIA_BloodAxeCairnTarget_A1_A01_TargetMultiviewPrep_A10.png"
THREEQUARTER = BENCH_DIR / "bloodaxe_a1_target_multiview_mesh_internal_threequarter.png"
SIDE = BENCH_DIR / "bloodaxe_a1_target_multiview_mesh_internal_side.png"
REPORT_JSON = BENCH_DIR / "bloodaxe_a1_target_multiview_mesh.json"
OUTPUT = ASSET_DOC_DIR / "SM_GIA_BloodAxeCairnTarget_A1_A01_TRELLISReferenceCompare_A11.png"


def resample_filter() -> int:
    return getattr(getattr(Image, "Resampling", Image), "LANCZOS")


def font(size: int) -> ImageFont.ImageFont:
    candidates = [
        "/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf",
        "/usr/share/fonts/truetype/dejavu/DejaVuSans.ttf",
    ]
    for candidate in candidates:
        path = Path(candidate)
        if path.exists():
            return ImageFont.truetype(str(path), size=size)
    return ImageFont.load_default()


def fit_image(path: Path, max_size: tuple[int, int]) -> Image.Image:
    image = Image.open(path).convert("RGB")
    image.thumbnail(max_size, resample_filter())
    return image


def paste_centered(canvas: Image.Image, image: Image.Image, box: tuple[int, int, int, int]) -> None:
    x0, y0, x1, y1 = box
    x = x0 + ((x1 - x0) - image.width) // 2
    y = y0 + ((y1 - y0) - image.height) // 2
    canvas.paste(image, (x, y))


def main() -> None:
    for path in [TARGET_SHEET, THREEQUARTER, SIDE, REPORT_JSON]:
        if not path.exists():
            raise FileNotFoundError(path)

    report = json.loads(REPORT_JSON.read_text(encoding="utf-8"))
    raw_mesh = report["raw_mesh"]
    extents = raw_mesh["extents"]
    smallest = min(extents)
    largest = max(extents)
    ratio = smallest / largest if largest else 0.0

    canvas = Image.new("RGB", (1920, 1220), (28, 28, 30))
    draw = ImageDraw.Draw(canvas)
    title_font = font(34)
    label_font = font(22)
    body_font = font(18)

    draw.text((40, 30), "Blood Axe A1 TRELLIS-AMD Reference Compare", fill=(238, 232, 220), font=title_font)
    draw.text(
        (40, 78),
        "Research-only diagnostic: volume/landmark guide, not visual canon, not approval art, not a DCC source candidate.",
        fill=(210, 190, 165),
        font=body_font,
    )

    left_box = (40, 135, 930, 960)
    right_top = (985, 135, 1880, 545)
    right_bottom = (985, 610, 1880, 1020)

    draw.rectangle(left_box, outline=(95, 88, 78), width=2)
    draw.rectangle(right_top, outline=(95, 88, 78), width=2)
    draw.rectangle(right_bottom, outline=(95, 88, 78), width=2)

    draw.text((left_box[0], left_box[1] - 34), "Prepared A1 target crops", fill=(235, 225, 205), font=label_font)
    draw.text((right_top[0], right_top[1] - 34), "TRELLIS neutral geometry - three-quarter", fill=(235, 225, 205), font=label_font)
    draw.text((right_bottom[0], right_bottom[1] - 34), "TRELLIS neutral geometry - side", fill=(235, 225, 205), font=label_font)

    paste_centered(canvas, fit_image(TARGET_SHEET, (860, 790)), left_box)
    paste_centered(canvas, fit_image(THREEQUARTER, (860, 380)), right_top)
    paste_centered(canvas, fit_image(SIDE, (860, 380)), right_bottom)

    stats = [
        f"Raw mesh: {raw_mesh['vertices']:,} vertices / {raw_mesh['faces']:,} faces",
        f"Extents: {extents[0]:.3f} x {extents[1]:.3f} x {extents[2]:.3f}; smallest/largest ratio {ratio:.3f}",
        f"Elapsed: {report['elapsed_seconds']:.1f}s on {report['gpu']} using {report['mode']} mesh output",
        "Use: derive broad A1 thickness, rear slab height, front slab overlap, and side mass landmarks.",
        "Do not use: raw shards, micro-noise, texture/paint, UVs, collision, LODs, or final silhouette approval.",
    ]
    y = 1062
    for line in stats:
        draw.text((40, y), line, fill=(224, 218, 205), font=body_font)
        y += 30

    OUTPUT.parent.mkdir(parents=True, exist_ok=True)
    canvas.save(OUTPUT)
    print(OUTPUT)


if __name__ == "__main__":
    main()
