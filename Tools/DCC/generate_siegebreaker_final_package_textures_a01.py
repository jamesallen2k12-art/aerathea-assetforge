#!/usr/bin/env python3
"""Author the deterministic Siege Breaker PBR texture candidate with Pillow."""

from __future__ import annotations

import argparse
import gc
import hashlib
import json
import math
import random
from pathlib import Path

from PIL import Image, ImageChops, ImageDraw, ImageEnhance, ImageFilter, ImageOps


ASSET_ID = "SM_DRW_SiegeBreaker_Hammer_A01"
SIZE = 2048
SEED = 0x51E6EB


def sha256(path: Path) -> str:
    digest = hashlib.sha256()
    with path.open("rb") as handle:
        for chunk in iter(lambda: handle.read(1024 * 1024), b""):
            digest.update(chunk)
    return digest.hexdigest()


def smooth_noise(rng: random.Random, cells: int) -> Image.Image:
    raw = bytes(rng.randrange(256) for _ in range(cells * cells))
    resampling = getattr(Image, "Resampling", Image)
    return Image.frombytes("L", (cells, cells), raw).resize((SIZE, SIZE), resampling.BICUBIC)


def layered_noise(rng: random.Random) -> Image.Image:
    low = smooth_noise(rng, 18)
    medium = smooth_noise(rng, 57)
    high = smooth_noise(rng, 173)
    return Image.blend(Image.blend(low, medium, 0.37), high, 0.20)


def colorize_noise(noise: Image.Image, shadow: tuple[int, int, int], highlight: tuple[int, int, int]) -> Image.Image:
    return ImageOps.colorize(ImageEnhance.Contrast(noise).enhance(1.16), shadow, highlight)


def crack_mask(rng: random.Random, count: int) -> Image.Image:
    canvas = Image.new("L", (SIZE, SIZE), 0)
    draw = ImageDraw.Draw(canvas)
    for _ in range(count):
        x = rng.randrange(SIZE)
        y = rng.randrange(SIZE)
        points = [(x, y)]
        heading = rng.random() * math.tau
        for _segment in range(rng.randrange(3, 8)):
            heading += rng.gauss(0.0, 0.55)
            length = rng.uniform(SIZE * 0.018, SIZE * 0.065)
            x = max(0, min(SIZE - 1, int(x + math.cos(heading) * length)))
            y = max(0, min(SIZE - 1, int(y + math.sin(heading) * length)))
            points.append((x, y))
        draw.line(points, fill=rng.randrange(150, 236), width=rng.randrange(2, 6))
    return canvas.filter(ImageFilter.GaussianBlur(0.65))


def scratch_mask(rng: random.Random, count: int, vertical_bias: bool) -> Image.Image:
    canvas = Image.new("L", (SIZE, SIZE), 0)
    draw = ImageDraw.Draw(canvas)
    for _ in range(count):
        x = rng.randrange(SIZE)
        y = rng.randrange(SIZE)
        length = rng.randrange(max(2, SIZE // 180), SIZE // 30)
        if vertical_bias:
            end = (max(0, min(SIZE - 1, x + rng.randrange(-3, 4))), min(SIZE - 1, y + length))
        else:
            angle = rng.random() * math.tau
            end = (
                max(0, min(SIZE - 1, int(x + math.cos(angle) * length))),
                max(0, min(SIZE - 1, int(y + math.sin(angle) * length))),
            )
        draw.line((x, y, *end), fill=rng.randrange(45, 146), width=1)
    return canvas


def normal_from_height(height: Image.Image, strength: float) -> Image.Image:
    source = height.convert("L")
    left = ImageChops.offset(source, -1, 0)
    right = ImageChops.offset(source, 1, 0)
    up = ImageChops.offset(source, 0, -1)
    down = ImageChops.offset(source, 0, 1)
    nx = ImageChops.subtract(left, right, scale=max(0.25, 2.0 / strength), offset=128)
    ny = ImageChops.subtract(up, down, scale=max(0.25, 2.0 / strength), offset=128)
    nz = Image.new("L", source.size, 245)
    return Image.merge("RGB", (nx, ny, nz))


def gray_curve(image: Image.Image, low: int, high: int, invert: bool = False) -> Image.Image:
    lut = []
    for value in range(256):
        t = value / 255.0
        if invert:
            t = 1.0 - t
        lut.append(int(max(0, min(255, low + (high - low) * t))))
    return image.convert("L").point(lut)


def save_set(
    out_dir: Path,
    family: str,
    base_color: Image.Image,
    height: Image.Image,
    ao: Image.Image,
    roughness: Image.Image,
    metallic: Image.Image,
    emissive: Image.Image,
    normal_strength: float,
) -> dict[str, str]:
    prefix = f"T_DRW_SiegeBreaker_Hammer_A01_{family}"
    payloads = {
        "BC": base_color.convert("RGB"),
        "N": normal_from_height(height, normal_strength),
        "ORM": Image.merge("RGB", (ao.convert("L"), roughness.convert("L"), metallic.convert("L"))),
        "E": Image.merge("RGB", (emissive.convert("L"),) * 3),
    }
    result: dict[str, str] = {}
    for suffix, image in payloads.items():
        path = out_dir / f"{prefix}_{suffix}.png"
        image.save(path, optimize=True)
        result[suffix] = str(path)
    return result


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--out-dir", required=True, type=Path)
    parser.add_argument("--manifest", required=True, type=Path)
    parser.add_argument(
        "--profile",
        choices=("final_package_a01", "visual_fidelity_a02", "pixel_reconstruction_a03"),
        default="final_package_a01",
    )
    args = parser.parse_args()
    args.out_dir.mkdir(parents=True, exist_ok=True)
    args.manifest.parent.mkdir(parents=True, exist_ok=True)
    rng = random.Random(SEED)

    zero = Image.new("L", (SIZE, SIZE), 0)
    full = Image.new("L", (SIZE, SIZE), 255)

    stone_noise = layered_noise(rng)
    cracks = crack_mask(rng, 165)
    stone_height = ImageChops.subtract(Image.blend(stone_noise, Image.new("L", stone_noise.size, 120), 0.34), cracks, scale=1.0)
    stone_palettes = {
        "final_package_a01": ((23, 29, 36), (68, 78, 91)),
        "visual_fidelity_a02": ((7, 10, 15), (39, 49, 61)),
        "pixel_reconstruction_a03": ((4, 7, 11), (48, 59, 72)),
    }
    stone_palette = stone_palettes[args.profile]
    stone_color = colorize_noise(stone_noise, *stone_palette)
    crack_darkener = ImageOps.colorize(ImageOps.invert(cracks), (7, 10, 14), (255, 255, 255))
    stone_color = ImageChops.multiply(stone_color, crack_darkener)
    stone = save_set(
        args.out_dir,
        "Stone",
        stone_color,
        stone_height,
        gray_curve(cracks, 216, 136, invert=True),
        gray_curve(stone_noise, 188, 232),
        zero,
        zero,
        6.0,
    )
    del stone_noise, cracks, stone_height, stone_color, crack_darkener
    gc.collect()

    bronze_noise = layered_noise(rng)
    bronze_scratches = scratch_mask(rng, 1900, False)
    bronze_height = ImageChops.add(gray_curve(bronze_noise, 30, 150), gray_curve(bronze_scratches, 0, 85), scale=1.0)
    bronze_palettes = {
        "final_package_a01": ((54, 27, 13), (175, 101, 45)),
        "visual_fidelity_a02": ((38, 17, 7), (154, 80, 29)),
        "pixel_reconstruction_a03": ((31, 13, 4), (174, 91, 28)),
    }
    bronze_palette = bronze_palettes[args.profile]
    bronze_color = colorize_noise(bronze_noise, *bronze_palette)
    patina = gray_curve(smooth_noise(rng, 91), 0, 255).point(lambda p: 210 if p > 200 else 0)
    bronze_color = Image.composite(Image.blend(bronze_color, Image.new("RGB", bronze_color.size, (34, 91, 78)), 0.48), bronze_color, patina)
    bronze = save_set(
        args.out_dir,
        "Bronze",
        bronze_color,
        bronze_height,
        gray_curve(bronze_noise, 198, 235),
        ImageChops.lighter(gray_curve(bronze_noise, 86, 154), gray_curve(bronze_scratches, 78, 152)),
        full,
        zero,
        4.5,
    )
    del bronze_noise, bronze_scratches, bronze_height, bronze_color, patina
    gc.collect()

    steel_noise = layered_noise(rng)
    steel_scratches = scratch_mask(rng, 2600, True)
    steel_height = ImageChops.add(gray_curve(steel_noise, 22, 110), gray_curve(steel_scratches, 0, 135), scale=1.0)
    steel_palettes = {
        "final_package_a01": ((22, 28, 36), (80, 91, 108)),
        "visual_fidelity_a02": ((9, 14, 21), (54, 65, 80)),
        "pixel_reconstruction_a03": ((6, 10, 16), (64, 78, 97)),
    }
    steel_palette = steel_palettes[args.profile]
    steel_color = colorize_noise(steel_noise, *steel_palette)
    steel_color = ImageChops.add(steel_color, Image.merge("RGB", (steel_scratches,) * 3), scale=1.25)
    steel = save_set(
        args.out_dir,
        "Steel",
        steel_color,
        steel_height,
        gray_curve(steel_noise, 190, 228),
        ImageChops.lighter(gray_curve(steel_noise, 72, 138), gray_curve(steel_scratches, 64, 148)),
        full,
        zero,
        5.0,
    )
    del steel_noise, steel_scratches, steel_height, steel_color
    gc.collect()

    leather_noise = layered_noise(rng)
    weave = Image.new("L", (SIZE, SIZE), 35)
    weave_draw = ImageDraw.Draw(weave)
    spacing = 42
    for offset in range(-SIZE, SIZE * 2, spacing):
        weave_draw.line((offset, 0, offset + SIZE, SIZE), fill=205, width=12)
        weave_draw.line((offset, SIZE, offset + SIZE, 0), fill=168, width=10)
    weave = weave.filter(ImageFilter.GaussianBlur(1.1))
    leather_height = Image.blend(leather_noise, weave, 0.68)
    leather_palettes = {
        "final_package_a01": ((40, 15, 9), (111, 54, 27)),
        "visual_fidelity_a02": ((58, 17, 6), (154, 72, 28)),
        "pixel_reconstruction_a03": ((29, 7, 3), (107, 43, 16)),
    }
    leather_palette = leather_palettes[args.profile]
    leather_color = colorize_noise(Image.blend(leather_noise, weave, 0.36), *leather_palette)
    leather = save_set(
        args.out_dir,
        "Leather",
        leather_color,
        leather_height,
        gray_curve(weave, 178, 218, invert=True),
        gray_curve(leather_noise, 154, 210),
        zero,
        zero,
        5.5,
    )
    del leather_noise, weave, weave_draw, leather_height, leather_color
    gc.collect()

    rune_noise = layered_noise(rng)
    rune_palettes = {
        "final_package_a01": ((3, 45, 116), (95, 225, 255)),
        "visual_fidelity_a02": ((2, 28, 76), (63, 211, 255)),
        "pixel_reconstruction_a03": ((0, 22, 69), (78, 226, 255)),
    }
    rune_palette = rune_palettes[args.profile]
    rune_color = colorize_noise(rune_noise, *rune_palette)
    rune_emissive = gray_curve(rune_noise, 190, 255)
    rune = save_set(
        args.out_dir,
        "Rune",
        rune_color,
        rune_noise,
        Image.new("L", (SIZE, SIZE), 236),
        Image.new("L", (SIZE, SIZE), 62),
        zero,
        rune_emissive,
        2.5,
    )
    del rune_noise, rune_color, rune_emissive
    gc.collect()

    sets = {"Stone": stone, "Bronze": bronze, "Steel": steel, "Leather": leather, "Rune": rune}
    output_files = sorted(path for family in sets.values() for path in family.values())
    manifest = {
        "schema": "aerathea.texture_candidate.v1",
        "asset_id": ASSET_ID,
        "artifact_status": "candidate",
        "authority": "verified final package material_spec.json and approved style reference",
        "interpretation": "deterministic authored PBR surface detail; no geometry or exact source-color authority",
        "resolution_px": [SIZE, SIZE],
        "seed": SEED,
        "profile": args.profile,
        "workflow": "PBR metallic-roughness; ORM channels R=AO G=Roughness B=Metallic",
        "texture_sets": sets,
        "files": [{"path": path, "sha256": sha256(Path(path))} for path in output_files],
    }
    args.manifest.write_text(json.dumps(manifest, indent=2) + "\n", encoding="utf-8")
    print(args.manifest)
    print(f"texture_sets={len(sets)} files={len(output_files)} resolution={SIZE}x{SIZE}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
