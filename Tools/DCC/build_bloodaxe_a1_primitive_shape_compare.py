#!/usr/bin/env python3
"""Build the A1 target versus A21 primitive blockout comparison sheet."""

from __future__ import annotations

from pathlib import Path

from PIL import Image, ImageDraw, ImageFont


ROOT = Path(__file__).resolve().parents[2]
ASSET_NAME = "SM_GIA_BloodAxeCairnTarget_A1_A01"
DOC_ROOT = ROOT / "docs" / "assets" / "props" / ASSET_NAME
REVIEW_ROOT = ROOT / "Saved" / "Automation" / "DCC" / ASSET_NAME
TARGET = DOC_ROOT / f"{ASSET_NAME}_TargetFrontCrop.png"
PROOF = DOC_ROOT / f"{ASSET_NAME}_PrimitiveShapeBlockout_A21.png"
GEOMETRIC_REFERENCE = ROOT / "docs" / "assets" / "reference" / "geometric_image_training" / "REF_AET_GeometricImageTraining_Primitives_A01.png"
OUTPUT = DOC_ROOT / f"{ASSET_NAME}_A1_PrimitiveShapeBlockoutCompare_A21.png"
OPEN_REVIEW = REVIEW_ROOT / "A21_OpenReview.html"


def resample_filter() -> int:
    return getattr(getattr(Image, "Resampling", Image), "LANCZOS")


def font(size: int, bold: bool = False) -> ImageFont.ImageFont:
    candidates = [
        f"/usr/share/fonts/truetype/dejavu/DejaVuSans{'-Bold' if bold else ''}.ttf",
        "/usr/share/fonts/truetype/liberation2/LiberationSans-Bold.ttf" if bold else "/usr/share/fonts/truetype/liberation2/LiberationSans-Regular.ttf",
    ]
    for candidate in candidates:
        path = Path(candidate)
        if path.exists():
            return ImageFont.truetype(str(path), size=size)
    return ImageFont.load_default()


def fit_image(path: Path, max_size: tuple[int, int], background: tuple[int, int, int]) -> Image.Image:
    image = Image.open(path).convert("RGB")
    ratio = min(max_size[0] / image.width, max_size[1] / image.height)
    image = image.resize((max(1, int(image.width * ratio)), max(1, int(image.height * ratio))), resample_filter())
    fitted = Image.new("RGB", max_size, background)
    x = (max_size[0] - image.width) // 2
    y = (max_size[1] - image.height) // 2
    fitted.paste(image, (x, y))
    return fitted


def write_open_review() -> None:
    html = f"""<!doctype html>
<html>
<head>
  <meta charset="utf-8">
  <title>Blood Axe A1 A21 Primitive Shape Review</title>
  <style>
    body {{
      margin: 0;
      background: #1e1e1f;
      color: #eee8dd;
      font-family: Arial, sans-serif;
    }}
    main {{
      padding: 24px;
    }}
    h1 {{
      margin: 0 0 8px;
      font-size: 24px;
    }}
    p {{
      color: #cfc6b8;
      margin: 0 0 18px;
    }}
    img {{
      display: block;
      max-width: 100%;
      height: auto;
      border: 1px solid #5f584d;
      margin-bottom: 24px;
    }}
  </style>
</head>
<body>
  <main>
    <h1>Blood Axe A1 A21 Primitive Shape Review</h1>
    <p>Shape-only blockout: judge silhouette, overlap, and major masses. No texture, paint, rope, or Unreal approval.</p>
    <img src="{OUTPUT}" alt="A21 concept versus primitive blockout comparison">
    <img src="{PROOF}" alt="A21 primitive proof render">
  </main>
</body>
</html>
"""
    OPEN_REVIEW.parent.mkdir(parents=True, exist_ok=True)
    OPEN_REVIEW.write_text(html, encoding="utf-8")


def main() -> None:
    for path in (TARGET, PROOF, GEOMETRIC_REFERENCE):
        if not path.exists():
            raise FileNotFoundError(path)

    canvas = Image.new("RGB", (1920, 1000), (29, 29, 30))
    draw = ImageDraw.Draw(canvas)
    title_font = font(34, bold=True)
    label_font = font(24, bold=True)
    body_font = font(18)

    draw.text((40, 30), "Blood Axe A1 Primitive Shape Blockout Compare - A21", fill=(238, 232, 220), font=title_font)
    draw.text(
        (40, 78),
        "Review gate: silhouette, primitive massing, overlap, and footprint only. Paint, texture, rope, chips, UVs, LODs, FBX, and Unreal are blocked.",
        fill=(213, 197, 170),
        font=body_font,
    )

    left_box = (40, 140, 920, 810)
    right_box = (1000, 140, 1880, 810)
    for box in (left_box, right_box):
        draw.rectangle(box, outline=(98, 91, 78), width=2)

    draw.text((left_box[0], left_box[1] - 38), "Approved A1 Target Crop", fill=(236, 226, 205), font=label_font)
    draw.text((right_box[0], right_box[1] - 38), "A21 Primitive Geometry", fill=(236, 226, 205), font=label_font)

    target = fit_image(TARGET, (left_box[2] - left_box[0] - 40, left_box[3] - left_box[1] - 40), (38, 38, 39))
    proof = fit_image(PROOF, (right_box[2] - right_box[0] - 40, right_box[3] - right_box[1] - 40), (38, 38, 39))
    canvas.paste(target, (left_box[0] + 20, left_box[1] + 20))
    canvas.paste(proof, (right_box[0] + 20, right_box[1] + 20))

    notes = [
        "Primitive vocabulary used: hexagonal-prism front mass, parallelepiped rear/side slabs, tetra/octa-derived foot wedges.",
        "A21 intentionally removes projected concept texture and separate red paint geometry so the shape can be judged cleanly.",
        "Approval target for this pass: major silhouette and overlap direction only.",
        "Recommended next step after approval: lock primitive silhouette, then add controlled slab chips and surface-paint masks.",
    ]
    y = 846
    for note in notes:
        draw.text((40, y), note, fill=(225, 219, 206), font=body_font)
        y += 30

    OUTPUT.parent.mkdir(parents=True, exist_ok=True)
    canvas.save(OUTPUT)
    write_open_review()
    print(OUTPUT)
    print(OPEN_REVIEW)


if __name__ == "__main__":
    main()
