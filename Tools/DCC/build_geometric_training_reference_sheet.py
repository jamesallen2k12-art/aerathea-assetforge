#!/usr/bin/env python3
"""Promote local geometric training images into a tracked reference sheet."""

from __future__ import annotations

from pathlib import Path

from PIL import Image, ImageDraw, ImageFont


ROOT = Path(__file__).resolve().parents[2]
SOURCE_ROOT = Path("/home/james/Desktop/Aerathea/Geometric Image Training")
OUTPUT_ROOT = ROOT / "docs" / "assets" / "reference" / "geometric_image_training"
SHEET_PATH = OUTPUT_ROOT / "REF_AET_GeometricImageTraining_Primitives_A01.png"

SHAPES = [
    "Cube",
    "Parallelepiped",
    "Tetrahedron",
    "Regular Octahedron",
    "Hexagonal Prism",
    "Cylinder",
    "Dodecahedron",
    "Icosahedron",
    "Pentagonal Trapezohedron",
    "D100 Trapezohedron",
]

RESAMPLE_LANCZOS = getattr(Image, "Resampling", Image).LANCZOS


def safe_name(name: str) -> str:
    return name.lower().replace(" ", "_")


def load_font(size: int) -> ImageFont.ImageFont:
    for path in (
        "/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf",
        "/usr/share/fonts/truetype/liberation2/LiberationSans-Bold.ttf",
    ):
        if Path(path).exists():
            return ImageFont.truetype(path, size)
    return ImageFont.load_default()


def main() -> None:
    OUTPUT_ROOT.mkdir(parents=True, exist_ok=True)

    copied: list[tuple[str, Path]] = []
    for shape in SHAPES:
        source = SOURCE_ROOT / shape
        if not source.exists():
            raise FileNotFoundError(source)
        with Image.open(source) as image:
            rgb = image.convert("RGB")
            output = OUTPUT_ROOT / f"REF_AET_GeometricImageTraining_{safe_name(shape)}.png"
            rgb.save(output)
            copied.append((shape, output))

    thumb_w = 236
    thumb_h = 296
    label_h = 46
    pad = 20
    cols = 5
    rows = 2
    title_h = 72
    sheet_w = cols * thumb_w + (cols + 1) * pad
    sheet_h = title_h + rows * (thumb_h + label_h) + (rows + 1) * pad

    sheet = Image.new("RGB", (sheet_w, sheet_h), (34, 35, 36))
    draw = ImageDraw.Draw(sheet)
    title_font = load_font(24)
    label_font = load_font(18)
    note_font = load_font(13)

    draw.text((pad, 18), "Aerathea Geometric Image Training - Primitive Shape Reference", fill=(235, 232, 224), font=title_font)
    draw.text(
        (pad, 48),
        "Tracked recovery copy from /home/james/Desktop/Aerathea/Geometric Image Training",
        fill=(176, 172, 164),
        font=note_font,
    )

    for index, (shape, image_path) in enumerate(copied):
        col = index % cols
        row = index // cols
        x = pad + col * (thumb_w + pad)
        y = title_h + pad + row * (thumb_h + label_h + pad)
        with Image.open(image_path) as image:
            image.thumbnail((thumb_w, thumb_h), RESAMPLE_LANCZOS)
            thumb = Image.new("RGB", (thumb_w, thumb_h), (50, 51, 52))
            tx = (thumb_w - image.width) // 2
            ty = (thumb_h - image.height) // 2
            thumb.paste(image, (tx, ty))
        sheet.paste(thumb, (x, y))
        draw.rectangle((x, y, x + thumb_w - 1, y + thumb_h - 1), outline=(92, 88, 80), width=2)
        label = shape
        bbox = draw.textbbox((0, 0), label, font=label_font)
        lx = x + max(0, (thumb_w - (bbox[2] - bbox[0])) // 2)
        draw.text((lx, y + thumb_h + 12), label, fill=(232, 226, 214), font=label_font)

    sheet.save(SHEET_PATH)
    print(SHEET_PATH)


if __name__ == "__main__":
    main()
