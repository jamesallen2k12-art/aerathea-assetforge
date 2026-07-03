#!/usr/bin/env python3
"""Prepare the A1 Blood Axe cairn concept crop for TripoSR."""

from pathlib import Path

from PIL import Image


ROOT = Path(__file__).resolve().parents[2]
SOURCE = ROOT / "docs/assets/visual_canon/VC_GIA_BloodAxe_CairnStones_A01_A1_Crop.png"
OUTPUT_DIR = ROOT / "SourceAssets/External/TripoSR/BloodAxeCairn_A1"
OUTPUT = OUTPUT_DIR / "BloodAxeCairn_A1_TripoSR_Input.png"


def main() -> None:
    OUTPUT_DIR.mkdir(parents=True, exist_ok=True)
    source = Image.open(SOURCE).convert("RGB")
    crop = source.crop((0, 112, 360, 356))
    canvas = Image.new("RGB", (512, 512), (128, 128, 128))
    crop.thumbnail((470, 360), Image.Resampling.LANCZOS)
    x = (canvas.width - crop.width) // 2
    y = 92
    canvas.paste(crop, (x, y))
    canvas.save(OUTPUT)
    print(OUTPUT.relative_to(ROOT))


if __name__ == "__main__":
    main()
