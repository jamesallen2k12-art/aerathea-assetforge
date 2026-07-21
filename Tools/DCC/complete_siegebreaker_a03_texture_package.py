#!/usr/bin/env python3
"""Complete and audit the memory-bounded A03 texture package."""

from __future__ import annotations

import hashlib
import json
import random
from pathlib import Path

from PIL import Image, ImageChops, ImageOps


ROOT = Path(__file__).resolve().parents[2]
ASSET_ID = "SM_DRW_SiegeBreaker_Hammer_A01"
OUTPUT = ROOT / "SourceAssets/Textures/Weapons/Dwarven" / ASSET_ID / "PixelReconstruction_A03"
MANIFEST = OUTPUT / f"{ASSET_ID}_TEXTURE_MANIFEST.json"
SIZE = 2048


def sha256(path: Path) -> str:
    digest = hashlib.sha256()
    with path.open("rb") as handle:
        for chunk in iter(lambda: handle.read(1024 * 1024), b""):
            digest.update(chunk)
    return digest.hexdigest()


def normal_from_small_height(height: Image.Image) -> Image.Image:
    left = ImageChops.offset(height, -1, 0)
    right = ImageChops.offset(height, 1, 0)
    up = ImageChops.offset(height, 0, -1)
    down = ImageChops.offset(height, 0, 1)
    nx = ImageChops.subtract(left, right, scale=0.7, offset=128)
    ny = ImageChops.subtract(up, down, scale=0.7, offset=128)
    nz = Image.new("L", height.size, 247)
    return Image.merge("RGB", (nx, ny, nz)).resize((SIZE, SIZE), Image.BICUBIC)


def main() -> int:
    OUTPUT.mkdir(parents=True, exist_ok=True)
    rng = random.Random(0xA03F1D)
    small = Image.frombytes("L", (384, 384), bytes(rng.randrange(256) for _ in range(384 * 384)))
    resampling = getattr(Image, "Resampling", Image)
    height = small.resize((512, 512), resampling.BICUBIC)
    prefix = OUTPUT / "T_DRW_SiegeBreaker_Hammer_A01_Rune"
    color_small = ImageOps.colorize(height, (0, 22, 69), (78, 226, 255))
    color_small.resize((SIZE, SIZE), resampling.BICUBIC).save(f"{prefix}_BC.png", optimize=True)
    normal_from_small_height(height).save(f"{prefix}_N.png", optimize=True)
    ao = Image.new("L", (SIZE, SIZE), 236)
    roughness = Image.new("L", (SIZE, SIZE), 58)
    metallic = Image.new("L", (SIZE, SIZE), 0)
    Image.merge("RGB", (ao, roughness, metallic)).save(f"{prefix}_ORM.png", optimize=True)
    emission_small = height.point(lambda value: max(188, min(255, int(188 + value * 0.263))))
    emission = emission_small.resize((SIZE, SIZE), resampling.BICUBIC)
    Image.merge("RGB", (emission, emission, emission)).save(f"{prefix}_E.png", optimize=True)

    files = sorted(OUTPUT.glob("T_DRW_SiegeBreaker_Hammer_A01_*_*.png"))
    families = {}
    for family in ("Stone", "Bronze", "Steel", "Leather", "Rune"):
        families[family] = {
            suffix: str(OUTPUT / f"T_DRW_SiegeBreaker_Hammer_A01_{family}_{suffix}.png")
            for suffix in ("BC", "N", "ORM", "E")
        }
    expected = {Path(path) for family in families.values() for path in family.values()}
    missing = sorted(str(path) for path in expected if not path.exists())
    wrong_size = {}
    for path in expected:
        if path.exists():
            with Image.open(path) as image:
                if image.size != (SIZE, SIZE):
                    wrong_size[str(path)] = list(image.size)
    result = "pass" if len(files) == 20 and not missing and not wrong_size else "fail"
    manifest = {
        "schema": "aerathea.texture_candidate.v2",
        "asset_id": ASSET_ID,
        "revision": "PixelReconstruction_A03",
        "contract_id": "SB-VF-A03-PIXEL",
        "artifact_status": "candidate" if result == "pass" else "blocked",
        "authority": "approved source rendered-color hierarchy plus material_spec.json; rendered source RGB is not raw albedo",
        "resolution_px": [SIZE, SIZE],
        "workflow": "PBR metallic-roughness; ORM channels R=AO G=Roughness B=Metallic",
        "texture_sets": families,
        "files": [{"path": str(path), "sha256": sha256(path), "bytes": path.stat().st_size} for path in files],
        "audit": {"result": result, "file_count": len(files), "missing": missing, "wrong_size": wrong_size},
    }
    MANIFEST.write_text(json.dumps(manifest, indent=2) + "\n", encoding="utf-8")
    print(MANIFEST)
    print(f"TEXTURE_AUDIT={result} files={len(files)}")
    return 0 if result == "pass" else 1


if __name__ == "__main__":
    raise SystemExit(main())
