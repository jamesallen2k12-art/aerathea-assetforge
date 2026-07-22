#!/usr/bin/env python3
"""Generate the fresh, source-clean A05 2K PBR texture package."""

from __future__ import annotations

import hashlib
import json
import math
import random
from pathlib import Path

from PIL import Image, ImageDraw, ImageFilter


ROOT = Path(__file__).resolve().parents[2]
OUT = ROOT / "SourceAssets/Textures/Weapons/Dwarven/SM_DRW_SiegeBreaker_Hammer_A01/OrthographicVolumetric_A05"
MANIFEST = OUT / "SM_DRW_SiegeBreaker_Hammer_A01_A05_TEXTURE_MANIFEST.json"
SIZE = 2048
WORK = 512
SEED = 520321

FAMILIES = {
    "Stone": {"base": (24, 29, 34), "rough": 218, "metal": 0, "accent": (62, 74, 82)},
    "Bronze": {"base": (111, 66, 28), "rough": 116, "metal": 255, "accent": (189, 122, 55)},
    "Steel": {"base": (46, 53, 61), "rough": 98, "metal": 255, "accent": (102, 116, 126)},
    "Leather": {"base": (84, 38, 20), "rough": 172, "metal": 0, "accent": (145, 78, 42)},
    "Rune": {"base": (12, 92, 150), "rough": 60, "metal": 0, "accent": (78, 210, 255)},
}


def sha256(path: Path) -> str:
    digest = hashlib.sha256()
    with path.open("rb") as handle:
        for chunk in iter(lambda: handle.read(1024 * 1024), b""):
            digest.update(chunk)
    return digest.hexdigest()


def clamp(value: int) -> int:
    return max(0, min(255, value))


def upscale(image: Image.Image, normal: bool = False) -> Image.Image:
    method = Image.BICUBIC if normal else Image.LANCZOS
    return image.resize((SIZE, SIZE), method)


def base_color(family: str, spec: dict, rng: random.Random) -> Image.Image:
    image = Image.new("RGB", (WORK, WORK), spec["base"])
    pixels = image.load()
    base = spec["base"]
    for y in range(WORK):
        for x in range(WORK):
            wave = math.sin((x + y * 0.37) * 0.055) * 5.0
            noise = rng.randint(-12, 12)
            value = int(wave + noise)
            pixels[x, y] = tuple(clamp(channel + value) for channel in base)

    draw = ImageDraw.Draw(image)
    accent = spec["accent"]
    if family == "Stone":
        for _ in range(95):
            x = rng.randrange(WORK)
            y = rng.randrange(WORK)
            points = [(x, y)]
            for _ in range(rng.randint(2, 6)):
                x += rng.randint(-28, 28)
                y += rng.randint(10, 48)
                points.append((x, y))
            draw.line(points, fill=(18, 22, 25), width=rng.choice((1, 1, 2)))
            if rng.random() < 0.6:
                draw.line([(px + 2, py) for px, py in points], fill=accent, width=1)
    elif family in {"Bronze", "Steel"}:
        for _ in range(140):
            x = rng.randrange(WORK)
            y = rng.randrange(WORK)
            length = rng.randint(10, 70)
            draw.line((x, y, min(WORK - 1, x + length), y + rng.randint(-2, 2)), fill=accent, width=1)
        for _ in range(70):
            x, y = rng.randrange(WORK), rng.randrange(WORK)
            radius = rng.randint(1, 4)
            draw.ellipse((x - radius, y - radius, x + radius, y + radius), fill=(30, 28, 25))
    elif family == "Leather":
        for offset in range(-WORK, WORK * 2, 28):
            draw.line((offset, 0, offset - WORK, WORK), fill=(33, 15, 10), width=4)
            draw.line((offset + 14, 0, offset + 14 + WORK, WORK), fill=accent, width=2)
        for y in range(14, WORK, 28):
            draw.line((0, y, WORK, y), fill=(39, 18, 12), width=1)
    else:
        for x in range(0, WORK, 48):
            draw.line((x, 0, x, WORK), fill=accent, width=4)
        for y in range(0, WORK, 48):
            draw.line((0, y, WORK, y), fill=(27, 119, 171), width=2)
    return upscale(image)


def normal_map(family: str, rng: random.Random) -> Image.Image:
    height = Image.new("L", (WORK, WORK), 128)
    draw = ImageDraw.Draw(height)
    if family == "Stone":
        for _ in range(90):
            x, y = rng.randrange(WORK), rng.randrange(WORK)
            points = [(x, y)]
            for _ in range(rng.randint(2, 5)):
                x += rng.randint(-24, 24)
                y += rng.randint(8, 42)
                points.append((x, y))
            draw.line(points, fill=rng.randint(40, 85), width=rng.choice((1, 2, 3)))
    elif family == "Leather":
        for offset in range(-WORK, WORK * 2, 28):
            draw.line((offset, 0, offset - WORK, WORK), fill=182, width=5)
            draw.line((offset + 14, 0, offset + 14 + WORK, WORK), fill=76, width=4)
    else:
        for _ in range(100):
            x, y = rng.randrange(WORK), rng.randrange(WORK)
            draw.line((x, y, min(WORK - 1, x + rng.randint(5, 55)), y), fill=rng.randint(100, 158), width=1)
    height = height.filter(ImageFilter.GaussianBlur(radius=0.8))
    hp = height.load()
    normal = Image.new("RGB", (WORK, WORK), (128, 128, 255))
    np = normal.load()
    strength = 2.3 if family == "Stone" else 1.3
    for y in range(1, WORK - 1):
        for x in range(1, WORK - 1):
            dx = (hp[x - 1, y] - hp[x + 1, y]) * strength
            dy = (hp[x, y - 1] - hp[x, y + 1]) * strength
            length = math.sqrt(dx * dx + dy * dy + 255.0 * 255.0)
            np[x, y] = (clamp(int(128 + 127 * dx / length)), clamp(int(128 + 127 * dy / length)), clamp(int(128 + 127 * 255.0 / length)))
    return upscale(normal, normal=True)


def orm_map(spec: dict, rng: random.Random) -> Image.Image:
    image = Image.new("RGB", (WORK, WORK), (224, spec["rough"], spec["metal"]))
    pixels = image.load()
    for y in range(WORK):
        for x in range(WORK):
            grain = rng.randint(-18, 18)
            ao = clamp(224 + grain // 3)
            rough = clamp(spec["rough"] + grain)
            pixels[x, y] = (ao, rough, spec["metal"])
    return upscale(image)


def emissive_map(family: str) -> Image.Image:
    image = Image.new("RGB", (WORK, WORK), (0, 0, 0))
    if family == "Rune":
        draw = ImageDraw.Draw(image)
        draw.rectangle((0, 0, WORK, WORK), fill=(8, 78, 140))
        for y in range(0, WORK, 48):
            draw.rectangle((0, y + 10, WORK, y + 30), fill=(12, 112, 184))
            draw.line((0, y + 20, WORK, y + 20), fill=(70, 220, 255), width=4)
        image = image.filter(ImageFilter.GaussianBlur(radius=2.0))
    return upscale(image)


def main() -> None:
    OUT.mkdir(parents=True, exist_ok=True)
    records = {}
    for index, (family, spec) in enumerate(FAMILIES.items()):
        rng = random.Random(SEED + index * 101)
        prefix = f"T_DRW_SiegeBreaker_Hammer_A01_{family}"
        paths = {
            "BC": OUT / f"{prefix}_BC.png",
            "N": OUT / f"{prefix}_N.png",
            "ORM": OUT / f"{prefix}_ORM.png",
            "E": OUT / f"{prefix}_E.png",
        }
        base_color(family, spec, rng).save(paths["BC"], optimize=True)
        normal_map(family, rng).save(paths["N"], optimize=True)
        orm_map(spec, rng).save(paths["ORM"], optimize=True)
        emissive_map(family).save(paths["E"], optimize=True)
        records[family] = {key: {"path": str(path.relative_to(ROOT)), "sha256": sha256(path), "size": [SIZE, SIZE]} for key, path in paths.items()}

    manifest = {
        "schema": "aerathea.siegebreaker_a05_texture_package.v1",
        "asset_id": "SM_DRW_SiegeBreaker_Hammer_A01",
        "artifact_status": "candidate",
        "generator": str(Path(__file__).relative_to(ROOT)),
        "source_sheet_pixels_used": False,
        "paper_labels_arrows_borders_shadows_used": False,
        "workflow": "PBR metallic-roughness; ORM R=AO G=roughness B=metallic",
        "resolution": [SIZE, SIZE],
        "families": records,
    }
    MANIFEST.write_text(json.dumps(manifest, indent=2) + "\n", encoding="utf-8")
    print(json.dumps({"status": "pass", "families": len(records), "maps": len(records) * 4, "manifest": str(MANIFEST)}, indent=2))


if __name__ == "__main__":
    main()
