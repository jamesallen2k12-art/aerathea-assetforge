#!/usr/bin/env python3
"""Prepare Blood Axe A1 target-sheet crops for research-only multiview reference.

The generated images are not visual canon and are not production art. They are
temporary RGBA inputs for AssetForge/TRELLIS-AMD reference experiments.
"""

from __future__ import annotations

import json
from collections import deque
from pathlib import Path

from PIL import Image, ImageDraw, ImageFilter


ROOT = Path(__file__).resolve().parents[2]
SOURCE = ROOT / "docs" / "assets" / "visual_canon" / "BloodAxeCairnTargets_A01" / "VC_GIA_BloodAxe_CairnTarget_A1.png"
OUT_DIR = ROOT / "Saved" / "AssetForgeResearch" / "benchmarks" / "inputs" / "bloodaxe_a1_target_multiview"

# Boxes are hand-authored against the 1122 x 1402 A1 target sheet. They crop out
# labels where possible and keep only the object plus nearby ground contact.
CROP_BOXES = {
    "hero": (205, 55, 900, 585),
    "front": (42, 642, 420, 918),
    "right": (430, 632, 718, 924),
    "back": (715, 630, 1084, 920),
    "left": (310, 985, 818, 1288),
}


def color_distance(a: tuple[int, int, int], b: tuple[int, int, int]) -> float:
    return ((a[0] - b[0]) ** 2 + (a[1] - b[1]) ** 2 + (a[2] - b[2]) ** 2) ** 0.5


def median_color(colors: list[tuple[int, int, int]]) -> tuple[int, int, int]:
    channels = []
    for index in range(3):
        values = sorted(color[index] for color in colors)
        channels.append(values[len(values) // 2])
    return (channels[0], channels[1], channels[2])


def flood_background(image: Image.Image, tolerance: float = 42.0) -> list[list[bool]]:
    w, h = image.size
    pixels = image.load()
    corners = [pixels[0, 0], pixels[w - 1, 0], pixels[0, h - 1], pixels[w - 1, h - 1]]
    bg = median_color(corners)
    candidate = [[color_distance(pixels[x, y], bg) <= tolerance for x in range(w)] for y in range(h)]
    visited = [[False for _ in range(w)] for _ in range(h)]
    queue: deque[tuple[int, int]] = deque()

    for x in range(w):
        queue.append((0, x))
        queue.append((h - 1, x))
    for y in range(h):
        queue.append((y, 0))
        queue.append((y, w - 1))

    while queue:
        y, x = queue.popleft()
        if y < 0 or y >= h or x < 0 or x >= w or visited[y][x] or not candidate[y][x]:
            continue
        visited[y][x] = True
        queue.extend(((y - 1, x), (y + 1, x), (y, x - 1), (y, x + 1)))
    return visited


def keep_largest_component(mask: list[list[bool]]) -> list[list[bool]]:
    h = len(mask)
    w = len(mask[0]) if h else 0
    visited = [[False for _ in range(w)] for _ in range(h)]
    best: list[tuple[int, int]] = []

    for y0 in range(h):
        for x0 in range(w):
            if visited[y0][x0] or not mask[y0][x0]:
                continue
            component: list[tuple[int, int]] = []
            queue: deque[tuple[int, int]] = deque([(y0, x0)])
            visited[y0][x0] = True
            while queue:
                y, x = queue.popleft()
                component.append((y, x))
                for ny in (y - 1, y, y + 1):
                    for nx in (x - 1, x, x + 1):
                        if ny < 0 or ny >= h or nx < 0 or nx >= w or visited[ny][nx] or not mask[ny][nx]:
                            continue
                        visited[ny][nx] = True
                        queue.append((ny, nx))
            if len(component) > len(best):
                best = component

    cleaned = [[False for _ in range(w)] for _ in range(h)]
    for y, x in best:
        cleaned[y][x] = True
    return cleaned


def make_rgba_crop(source: Image.Image, name: str, box: tuple[int, int, int, int]) -> dict:
    crop = source.crop(box).convert("RGB")
    background = flood_background(crop)
    foreground = keep_largest_component([[not value for value in row] for row in background])
    alpha = Image.new("L", crop.size, 0)
    alpha_pixels = alpha.load()
    for y, row in enumerate(foreground):
        for x, value in enumerate(row):
            if value:
                alpha_pixels[x, y] = 255
    alpha = alpha.filter(ImageFilter.MaxFilter(7)).filter(ImageFilter.GaussianBlur(1.0))

    rgba = crop.convert("RGBA")
    rgba.putalpha(alpha)
    out_path = OUT_DIR / f"bloodaxe_a1_target_multiview_{name}.png"
    rgba.save(out_path)

    checker = Image.new("RGB", crop.size)
    pixels = checker.load()
    block = 20
    for y in range(crop.size[1]):
        for x in range(crop.size[0]):
            shade = 188 if ((x // block) + (y // block)) % 2 == 0 else 128
            pixels[x, y] = (shade, shade, shade)
    checker.paste(rgba, mask=alpha)
    checker_path = OUT_DIR / f"bloodaxe_a1_target_multiview_{name}_checker.png"
    checker.save(checker_path)

    return {
        "name": name,
        "box": list(box),
        "size": list(crop.size),
        "rgba": str(out_path.relative_to(ROOT)),
        "checker": str(checker_path.relative_to(ROOT)),
        "alpha_extrema": list(alpha.getextrema()),
        "bbox": list(alpha.getbbox()) if alpha.getbbox() else None,
    }


def make_contact_sheet(reports: list[dict]) -> Path:
    thumbs = []
    resample = getattr(getattr(Image, "Resampling", Image), "LANCZOS")
    for report in reports:
        image = Image.open(ROOT / report["checker"]).convert("RGB")
        image.thumbnail((260, 210), resample)
        thumb = Image.new("RGB", (280, 244), (42, 42, 42))
        thumb.paste(image, ((280 - image.width) // 2, 10))
        draw = ImageDraw.Draw(thumb)
        draw.text((10, 220), report["name"], fill=(245, 245, 230))
        thumbs.append(thumb)

    cols = 3
    rows = (len(thumbs) + cols - 1) // cols
    sheet = Image.new("RGB", (cols * 280, rows * 244), (28, 28, 28))
    for index, thumb in enumerate(thumbs):
        sheet.paste(thumb, ((index % cols) * 280, (index // cols) * 244))

    out_path = OUT_DIR / "bloodaxe_a1_target_multiview_contact_sheet.png"
    sheet.save(out_path)
    return out_path


def main() -> None:
    OUT_DIR.mkdir(parents=True, exist_ok=True)
    source = Image.open(SOURCE).convert("RGB")
    reports = [make_rgba_crop(source, name, box) for name, box in CROP_BOXES.items()]
    contact_sheet = make_contact_sheet(reports)
    manifest = {
        "source": str(SOURCE.relative_to(ROOT)),
        "source_size": list(source.size),
        "output_dir": str(OUT_DIR.relative_to(ROOT)),
        "contact_sheet": str(contact_sheet.relative_to(ROOT)),
        "views": reports,
        "note": "Research-only multiview inputs for TRELLIS-AMD reference. Not visual canon and not production art.",
    }
    manifest_path = OUT_DIR / "bloodaxe_a1_target_multiview_manifest.json"
    manifest_path.write_text(json.dumps(manifest, indent=2) + "\n", encoding="utf-8")
    print(json.dumps(manifest, indent=2))


if __name__ == "__main__":
    main()
