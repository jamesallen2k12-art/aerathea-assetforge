#!/usr/bin/env python3
"""Create the Blood Axe A1 front-proportion trace guide.

This is a technical review overlay, not concept art. It records the front-view
landmark proportions that the DCC rebuild must satisfy before paint, texture, or
Unreal work continues.
"""

from __future__ import annotations

from pathlib import Path

from PIL import Image, ImageDraw, ImageFont


ROOT = Path(__file__).resolve().parents[2]
PROP_DIR = ROOT / "docs" / "assets" / "props" / "SM_GIA_BloodAxeCairnTarget_A1_A01"
SOURCE = PROP_DIR / "SM_GIA_BloodAxeCairnTarget_A1_A01_TargetFrontCrop.png"
OUTPUT = PROP_DIR / "SM_GIA_BloodAxeCairnTarget_A1_A01_A1_FrontTraceGuide.png"


TRACE = {
    "ground": {
        "color": (225, 170, 70, 145),
        "outline": (255, 195, 75, 255),
        "points": [(10, 252), (55, 238), (144, 235), (240, 238), (343, 248), (389, 282), (360, 325), (35, 323)],
    },
    "left_lashed_stack": {
        "color": (72, 190, 220, 110),
        "outline": (95, 225, 245, 255),
        "points": [(31, 142), (76, 120), (137, 128), (153, 178), (143, 226), (57, 242), (24, 202)],
    },
    "dominant_front_slab": {
        "color": (245, 92, 78, 105),
        "outline": (255, 115, 98, 255),
        "points": [(85, 130), (169, 104), (247, 139), (281, 218), (229, 301), (130, 291), (64, 215)],
    },
    "tall_rear_slab": {
        "color": (157, 102, 235, 100),
        "outline": (194, 140, 255, 255),
        "points": [(183, 22), (247, 41), (298, 214), (223, 234), (160, 126)],
    },
    "right_bound_support": {
        "color": (88, 145, 245, 105),
        "outline": (120, 175, 255, 255),
        "points": [(295, 116), (343, 129), (354, 219), (318, 250), (279, 221)],
    },
}

PAINT_GUIDES = [
    ("main paint centerline", [(151, 132), (189, 184), (213, 244), (224, 292)]),
    ("front paint left sweep", [(93, 164), (151, 182), (212, 180)]),
    ("front paint lower sweep", [(142, 227), (190, 244), (252, 248)]),
    ("rear slab paint", [(217, 56), (226, 103), (243, 177)]),
]

LOCK_LINES = [
    ("rear apex", (183, 22), (247, 41)),
    ("front slab base", (130, 291), (229, 301)),
    ("left stack rope zone", (36, 168), (153, 207)),
    ("right support rope zone", (283, 168), (352, 207)),
]


def text(draw: ImageDraw.ImageDraw, xy: tuple[int, int], label: str, fill: tuple[int, int, int, int]) -> None:
    draw.text(xy, label, fill=fill, font=ImageFont.load_default())


def main() -> None:
    source = Image.open(SOURCE).convert("RGBA")
    canvas = Image.new("RGBA", (source.width, source.height + 112), (42, 42, 42, 255))
    canvas.alpha_composite(source, (0, 0))
    overlay = Image.new("RGBA", source.size, (0, 0, 0, 0))
    draw = ImageDraw.Draw(overlay)

    for label, spec in TRACE.items():
        points = spec["points"]
        draw.polygon(points, fill=spec["color"], outline=spec["outline"])
        draw.line(points + [points[0]], fill=spec["outline"], width=3)
        lx = min(point[0] for point in points) + 4
        ly = min(point[1] for point in points) + 4
        text(draw, (lx, ly), label.replace("_", " "), spec["outline"])

    for label, points in PAINT_GUIDES:
        draw.line(points, fill=(210, 42, 34, 255), width=3, joint="curve")
        text(draw, (points[0][0] + 4, points[0][1] - 12), label, (245, 80, 72, 255))

    for label, start, end in LOCK_LINES:
        draw.line([start, end], fill=(255, 235, 145, 255), width=2)
        text(draw, (start[0] + 4, start[1] + 4), label, (255, 235, 145, 255))

    canvas.alpha_composite(overlay, (0, 0))
    footer = ImageDraw.Draw(canvas)
    footer_y = source.height + 8
    footer.rectangle([(0, source.height), (source.width, canvas.height)], fill=(32, 32, 32, 255))
    footer.text((10, footer_y), "A1 front trace locks before next DCC pass:", fill=(245, 245, 230, 255), font=ImageFont.load_default())
    footer.text((10, footer_y + 18), "1. dominant front slab stays low/slanted, not wall-like", fill=(245, 245, 230, 255), font=ImageFont.load_default())
    footer.text((10, footer_y + 34), "2. rear slab sits behind and narrower than the current proof", fill=(245, 245, 230, 255), font=ImageFont.load_default())
    footer.text((10, footer_y + 50), "3. left stack and right support use rope-zone bounds, not stick lattice", fill=(245, 245, 230, 255), font=ImageFont.load_default())
    footer.text((10, footer_y + 66), "4. no crack/highlight overlays until silhouette matches", fill=(245, 245, 230, 255), font=ImageFont.load_default())
    OUTPUT.parent.mkdir(parents=True, exist_ok=True)
    canvas.convert("RGB").save(OUTPUT)
    print(OUTPUT.relative_to(ROOT))


if __name__ == "__main__":
    main()
