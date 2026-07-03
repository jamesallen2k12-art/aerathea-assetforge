#!/usr/bin/env python3
"""Build shared Blood Axe cairn variant texture candidates.

Run with:
    python3 Tools/DCC/build_bloodaxe_cairn_variant_textures.py

The batch meshes use vertex color for broad material identity. This script
derives a neutral shared BC/N/ORM detail layer from existing Blood Axe cairn
source swatches so the same one-slot material can add stone grain, ash scuffs,
and worn surface breakup without overriding those vertex-color regions.
"""

from __future__ import annotations

import math
from pathlib import Path

from PIL import Image, ImageDraw, ImageFont, ImageOps


ROOT = Path(__file__).resolve().parents[2]
SOURCE_ROOT = (
    ROOT
    / "SourceAssets"
    / "Textures"
    / "Props"
    / "Giants"
    / "BloodAxe"
    / "Cairns"
    / "SM_GIA_BloodAxeCairnSlabCluster_A01_TurnaroundPainted"
)
OUTPUT_ROOT = (
    ROOT
    / "SourceAssets"
    / "Textures"
    / "Props"
    / "Giants"
    / "BloodAxe"
    / "Cairns"
    / "KIT_GIA_BloodAxeCairnVariantBatch_A01"
)
DOC_ROOT = ROOT / "docs" / "assets" / "kits" / "KIT_GIA_BloodAxeCairnVariantBatch_A01"
SAVED_ROOT = ROOT / "Saved" / "Automation" / "DCC" / "BloodAxeCairnVariants_A01"

SIZE = 1024
PREFIX = "T_GIA_BloodAxeCairnVariants_A01"
RESAMPLE_BICUBIC = getattr(getattr(Image, "Resampling", Image), "BICUBIC", Image.BICUBIC)


SOURCE_MAPS = {
    "stone_bc": SOURCE_ROOT / "T_GIA_BloodAxeCairnSlabCluster_A01_TurnaroundPainted_DarkHighlandStone_BC.png",
    "ash_bc": SOURCE_ROOT / "T_GIA_BloodAxeCairnSlabCluster_A01_TurnaroundPainted_AshMud_BC.png",
    "rawhide_bc": SOURCE_ROOT / "T_GIA_BloodAxeCairnSlabCluster_A01_TurnaroundPainted_Rawhide_BC.png",
    "stone_n": SOURCE_ROOT / "T_GIA_BloodAxeCairnSlabCluster_A01_TurnaroundPainted_DarkHighlandStone_N.png",
    "stone_orm": SOURCE_ROOT / "T_GIA_BloodAxeCairnSlabCluster_A01_TurnaroundPainted_DarkHighlandStone_ORM.png",
}


def load_source(path: Path) -> Image.Image:
    if not path.exists():
        raise FileNotFoundError(path)
    return Image.open(path).convert("RGB").resize((SIZE, SIZE), RESAMPLE_BICUBIC)


def clamp_channel(value: float) -> int:
    return max(0, min(255, int(round(value))))


def luma(pixel: tuple[int, int, int]) -> float:
    return (0.2126 * pixel[0]) + (0.7152 * pixel[1]) + (0.0722 * pixel[2])


def blended_detail(stone: Image.Image, ash: Image.Image, rawhide: Image.Image) -> Image.Image:
    stone_l = ImageOps.autocontrast(stone.convert("L"))
    ash_l = ImageOps.autocontrast(ash.convert("L"))
    rawhide_l = ImageOps.autocontrast(rawhide.convert("L"))
    detail = Image.new("L", (SIZE, SIZE))

    stone_px = stone_l.load()
    ash_px = ash_l.load()
    raw_px = rawhide_l.load()
    out_px = detail.load()
    for y in range(SIZE):
        for x in range(SIZE):
            low_freq = 0.5 + 0.5 * math.sin((x * 0.011) + (y * 0.006))
            value = (stone_px[x, y] * 0.70) + (ash_px[x, y] * 0.20) + (raw_px[x, y] * 0.10)
            value = (value * 0.88) + (low_freq * 28.0)
            out_px[x, y] = clamp_channel(value)

    draw = ImageDraw.Draw(detail)
    for i in range(58):
        x0 = (i * 197 + 73) % SIZE
        y0 = (i * 113 + 41) % SIZE
        length = 70 + ((i * 31) % 180)
        angle = ((i * 23) % 180) * math.pi / 180.0
        x1 = x0 + math.cos(angle) * length
        y1 = y0 + math.sin(angle) * length
        shade = 42 + ((i * 19) % 44)
        draw.line((x0, y0, x1, y1), fill=shade, width=1 + (i % 2))

    detail = detail.filter(Image.Filter.SMOOTH_MORE) if hasattr(Image, "Filter") else detail
    return ImageOps.autocontrast(detail)


def make_base_color(detail: Image.Image) -> Image.Image:
    detail_px = detail.load()
    base = Image.new("RGB", (SIZE, SIZE))
    out_px = base.load()
    for y in range(SIZE):
        for x in range(SIZE):
            d = detail_px[x, y] / 255.0
            edge_chip = 1.0 if d > 0.82 else 0.0
            soot = 1.0 if d < 0.18 else 0.0
            value = 212.0 + (d * 34.0) + (edge_chip * 6.0) - (soot * 16.0)
            out_px[x, y] = (
                clamp_channel(value * 1.02),
                clamp_channel(value * 0.99),
                clamp_channel(value * 0.91),
            )
    return base


def make_normal_from_height(height: Image.Image, strength: float = 4.0) -> Image.Image:
    height_px = height.load()
    normal = Image.new("RGB", (SIZE, SIZE))
    out_px = normal.load()
    for y in range(SIZE):
        ym = max(0, y - 1)
        yp = min(SIZE - 1, y + 1)
        for x in range(SIZE):
            xm = max(0, x - 1)
            xp = min(SIZE - 1, x + 1)
            dx = (height_px[xp, y] - height_px[xm, y]) / 255.0
            dy = (height_px[x, yp] - height_px[x, ym]) / 255.0
            nx = -dx * strength
            ny = -dy * strength
            nz = 1.0
            inv_len = 1.0 / math.sqrt((nx * nx) + (ny * ny) + (nz * nz))
            out_px[x, y] = (
                clamp_channel((nx * inv_len * 0.5 + 0.5) * 255.0),
                clamp_channel((ny * inv_len * 0.5 + 0.5) * 255.0),
                clamp_channel((nz * inv_len * 0.5 + 0.5) * 255.0),
            )
    return normal


def make_orm(detail: Image.Image) -> Image.Image:
    detail_px = detail.load()
    orm = Image.new("RGB", (SIZE, SIZE))
    out_px = orm.load()
    for y in range(SIZE):
        for x in range(SIZE):
            d = detail_px[x, y] / 255.0
            crack = 1.0 if d < 0.22 else 0.0
            ao = 190.0 + (d * 60.0) - (crack * 36.0)
            roughness = 218.0 + ((1.0 - d) * 28.0)
            out_px[x, y] = (clamp_channel(ao), clamp_channel(roughness), 0)
    return orm


def blend_normals(source_normal: Image.Image, generated_normal: Image.Image) -> Image.Image:
    src = source_normal.resize((SIZE, SIZE), RESAMPLE_BICUBIC)
    src_px = src.load()
    gen_px = generated_normal.load()
    output = Image.new("RGB", (SIZE, SIZE))
    out_px = output.load()
    for y in range(SIZE):
        for x in range(SIZE):
            source = src_px[x, y]
            generated = gen_px[x, y]
            out_px[x, y] = (
                clamp_channel((source[0] * 0.45) + (generated[0] * 0.55)),
                clamp_channel((source[1] * 0.45) + (generated[1] * 0.55)),
                clamp_channel((source[2] * 0.45) + (generated[2] * 0.55)),
            )
    return output


def proof_sheet(base_color: Image.Image, normal: Image.Image, orm: Image.Image) -> Image.Image:
    pad = 24
    label_h = 44
    tile_w = 320
    tile_h = 320
    width = (tile_w * 3) + (pad * 4)
    height = tile_h + label_h + (pad * 2)
    sheet = Image.new("RGB", (width, height), (24, 24, 22))
    draw = ImageDraw.Draw(sheet)
    try:
        font = ImageFont.truetype("DejaVuSans.ttf", 22)
        small = ImageFont.truetype("DejaVuSans.ttf", 14)
    except OSError:
        font = ImageFont.load_default()
        small = ImageFont.load_default()

    entries = (
        ("BC - neutral detail multiplier", base_color),
        ("N - shared stone grain", normal),
        ("ORM - AO/Roughness/Metallic", orm),
    )
    for index, (label, image) in enumerate(entries):
        x = pad + index * (tile_w + pad)
        y = pad
        sheet.paste(image.resize((tile_w, tile_h), RESAMPLE_BICUBIC), (x, y))
        draw.rectangle((x, y, x + tile_w, y + tile_h), outline=(91, 84, 66), width=1)
        draw.text((x, y + tile_h + 10), label, fill=(226, 220, 198), font=font)
    draw.text((pad, height - 18), "Shared candidate for vertex-color Blood Axe cairn variants; pending Flamestrike final approval.", fill=(154, 149, 130), font=small)
    return sheet


def save_outputs() -> dict[str, Path]:
    OUTPUT_ROOT.mkdir(parents=True, exist_ok=True)
    DOC_ROOT.mkdir(parents=True, exist_ok=True)
    SAVED_ROOT.mkdir(parents=True, exist_ok=True)

    stone = load_source(SOURCE_MAPS["stone_bc"])
    ash = load_source(SOURCE_MAPS["ash_bc"])
    rawhide = load_source(SOURCE_MAPS["rawhide_bc"])
    source_normal = load_source(SOURCE_MAPS["stone_n"])

    detail = blended_detail(stone, ash, rawhide)
    base_color = make_base_color(detail)
    generated_normal = make_normal_from_height(detail)
    normal = blend_normals(source_normal, generated_normal)
    orm = make_orm(detail)

    outputs = {
        "bc": OUTPUT_ROOT / f"{PREFIX}_BC.png",
        "normal": OUTPUT_ROOT / f"{PREFIX}_N.png",
        "orm": OUTPUT_ROOT / f"{PREFIX}_ORM.png",
        "proof": DOC_ROOT / "BloodAxeCairnVariants_A01_TextureReviewSheet.png",
        "proof_saved": SAVED_ROOT / "BloodAxeCairnVariants_A01_TextureReviewSheet.png",
    }
    base_color.save(outputs["bc"])
    normal.save(outputs["normal"])
    orm.save(outputs["orm"])
    sheet = proof_sheet(base_color, normal, orm)
    sheet.save(outputs["proof"])
    sheet.save(outputs["proof_saved"])
    return outputs


def main() -> None:
    outputs = save_outputs()
    for key, path in outputs.items():
        print(f"{key}: {path.relative_to(ROOT)}")


if __name__ == "__main__":
    main()
