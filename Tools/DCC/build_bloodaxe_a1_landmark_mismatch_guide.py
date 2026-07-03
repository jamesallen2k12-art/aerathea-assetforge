#!/usr/bin/env python3
"""Build a target-vs-proof landmark mismatch guide for Blood Axe A1."""

from __future__ import annotations

import argparse
import sys
from pathlib import Path

from PIL import Image, ImageDraw, ImageFont


ROOT = Path(__file__).resolve().parents[2]
sys.path.insert(0, str(ROOT))

from Tools.DCC.make_bloodaxe_a1_trace_guide import LOCK_LINES, PAINT_GUIDES, TRACE  # noqa: E402


PROP_DIR = ROOT / "docs/assets/props/SM_GIA_BloodAxeCairnTarget_A1_A01"
TARGET = PROP_DIR / "SM_GIA_BloodAxeCairnTarget_A1_A01_TargetFrontCrop.png"
DEFAULT_PROOF = PROP_DIR / "SM_GIA_BloodAxeCairnTarget_A1_A01_ContinuousSlabPass_A13.png"
DEFAULT_OUTPUT = PROP_DIR / "SM_GIA_BloodAxeCairnTarget_A1_A01_A1_LandmarkMismatchGuide_A14.png"


def font(size: int, bold: bool = False) -> ImageFont.ImageFont:
    name = "DejaVuSans-Bold.ttf" if bold else "DejaVuSans.ttf"
    path = Path("/usr/share/fonts/truetype/dejavu") / name
    if path.exists():
        return ImageFont.truetype(str(path), size=size)
    return ImageFont.load_default()


def fit(image: Image.Image, size: tuple[int, int]) -> Image.Image:
    image = image.convert("RGB")
    image.thumbnail(size, getattr(getattr(Image, "Resampling", Image), "LANCZOS"))
    return image


def scale_points(points: list[tuple[int, int]], source_size: tuple[int, int], target_box: tuple[int, int, int, int]) -> list[tuple[int, int]]:
    sx, sy = source_size
    x0, y0, x1, y1 = target_box
    tw = x1 - x0
    th = y1 - y0
    return [(int(x0 + (x / sx) * tw), int(y0 + (y / sy) * th)) for x, y in points]


def draw_trace(draw: ImageDraw.ImageDraw, source_size: tuple[int, int], box: tuple[int, int, int, int], alpha_fill: int) -> None:
    for label, spec in TRACE.items():
        fill = tuple(spec["color"][:3]) + (alpha_fill,)
        outline = spec["outline"]
        points = scale_points(spec["points"], source_size, box)
        draw.polygon(points, fill=fill, outline=outline)
        draw.line(points + [points[0]], fill=outline, width=3)
        lx = min(point[0] for point in points) + 5
        ly = min(point[1] for point in points) + 5
        draw.text((lx, ly), label.replace("_", " "), fill=outline, font=font(13, True))

    for label, points in PAINT_GUIDES:
        mapped = scale_points(points, source_size, box)
        draw.line(mapped, fill=(230, 46, 36, 255), width=4)
        draw.text((mapped[0][0] + 4, mapped[0][1] - 18), label, fill=(250, 85, 75, 255), font=font(12, True))

    for label, start, end in LOCK_LINES:
        mapped = scale_points([start, end], source_size, box)
        draw.line(mapped, fill=(255, 235, 145, 255), width=2)
        draw.text((mapped[0][0] + 4, mapped[0][1] + 4), label, fill=(255, 235, 145, 255), font=font(12, True))


def paste_center(canvas: Image.Image, image: Image.Image, box: tuple[int, int, int, int]) -> tuple[int, int, int, int]:
    x0, y0, x1, y1 = box
    x = x0 + ((x1 - x0) - image.width) // 2
    y = y0 + ((y1 - y0) - image.height) // 2
    canvas.paste(image, (x, y))
    return (x, y, x + image.width, y + image.height)


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--proof", type=Path, default=DEFAULT_PROOF)
    parser.add_argument("--output", type=Path, default=DEFAULT_OUTPUT)
    parser.add_argument("--title", default="Blood Axe A1 Landmark Mismatch Guide")
    parser.add_argument(
        "--subtitle",
        default="Purpose: lock silhouette/paint landmarks before the next DCC rebuild. A13 remains not approved.",
    )
    parser.add_argument("--proof-label", default="Rejected proof with same normalized landmarks")
    return parser.parse_args()


def main() -> None:
    args = parse_args()
    target = Image.open(TARGET).convert("RGB")
    proof = Image.open(args.proof).convert("RGB")

    canvas = Image.new("RGB", (1920, 1180), (28, 28, 30))
    draw = ImageDraw.Draw(canvas, "RGBA")
    title_font = font(34, True)
    label_font = font(22, True)
    body_font = font(18)

    draw.text((40, 30), args.title, fill=(238, 232, 220), font=title_font)
    draw.text((40, 78), args.subtitle, fill=(215, 198, 174), font=body_font)

    left_frame = (40, 145, 910, 760)
    right_frame = (1010, 145, 1880, 760)
    draw.rectangle(left_frame, outline=(96, 88, 76), width=2)
    draw.rectangle(right_frame, outline=(96, 88, 76), width=2)
    draw.text((left_frame[0], left_frame[1] - 34), "A1 target with locked landmarks", fill=(238, 232, 220), font=label_font)
    draw.text((right_frame[0], right_frame[1] - 34), args.proof_label, fill=(238, 232, 220), font=label_font)

    target_fit = fit(target, (820, 540))
    proof_fit = fit(proof, (820, 540))
    target_box = paste_center(canvas, target_fit, left_frame)
    proof_box = paste_center(canvas, proof_fit, right_frame)

    draw = ImageDraw.Draw(canvas, "RGBA")
    draw_trace(draw, target.size, target_box, 82)
    draw_trace(draw, target.size, proof_box, 42)

    notes = [
        "A13 correction requirements:",
        "1. Main slab must follow the red target polygon: lower, more irregular, less shield-like.",
        "2. Rear slab must sit behind the target front slab without becoming the dominant centered tower.",
        "3. Left lash stack and right support must fit the target side mass bounds before ropes are added.",
        "4. Paint should be derived from the red guide paths as a texture mask, not modeled as raised strip strokes.",
        "5. Suppress procedural speckle/noise until the silhouette and major planes match the concept.",
    ]
    y = 830
    for index, line in enumerate(notes):
        fill = (242, 232, 210) if index == 0 else (224, 218, 205)
        draw.text((40, y), line, fill=fill, font=label_font if index == 0 else body_font)
        y += 42 if index == 0 else 32

    output = args.output if args.output.is_absolute() else ROOT / args.output
    output.parent.mkdir(parents=True, exist_ok=True)
    canvas.save(output)
    print(output.relative_to(ROOT))


if __name__ == "__main__":
    main()
