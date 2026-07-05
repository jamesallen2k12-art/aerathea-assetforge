#!/usr/bin/env python3
"""Start Blood Axe Cairnstone A001 from the AetherForge Blueprint.

This script intentionally performs only the first Blueprint-approved stage:
full-source scanline capture and restart manifest creation. It does not create
crops, masks, geometry, UVs, contact fixes, or inferred surfaces.
"""

from __future__ import annotations

import gzip
import hashlib
import json
from pathlib import Path

from PIL import Image, ImageChops, ImageDraw, ImageFont


ROOT = Path(__file__).resolve().parents[2]
ASSET_NAME = "SM_GIA_BloodAxeCairnstone_A001"
SOURCE = ROOT / "docs/assets/reference/bloodaxe_cairnstone_asset/REF_GIA_BloodAxeCairnstoneAsset_A02_BlueprintTemplate.png"
BLUEPRINT = ROOT / "docs/projects/assetforge/AETHERFORGE_BLUEPRINTS.md"
OUT_DIR = ROOT / "Saved/Automation/DCC" / ASSET_NAME
SCAN_DIR = OUT_DIR / "FreshEvidence" / "ScanlineCapture"


def ensure_dir(path: Path) -> None:
    path.mkdir(parents=True, exist_ok=True)


def sha256_bytes(data: bytes) -> str:
    return hashlib.sha256(data).hexdigest()


def sha256_file(path: Path) -> str:
    return sha256_bytes(path.read_bytes())


def max_rgb_delta(diff: Image.Image) -> int:
    extrema = diff.getextrema()
    return max(channel[1] for channel in extrema)


def changed_pixels(diff: Image.Image) -> int:
    return sum(1 for pixel in diff.getdata() if pixel != (0, 0, 0))


def font(size: int) -> ImageFont.ImageFont:
    candidates = [
        "/usr/share/fonts/truetype/dejavu/DejaVuSans.ttf",
        "/usr/share/fonts/truetype/liberation2/LiberationSans-Regular.ttf",
    ]
    for candidate in candidates:
        try:
            return ImageFont.truetype(candidate, size)
        except OSError:
            continue
    return ImageFont.load_default()


def create_source_proof_board(source_path: Path, rebuilt_path: Path, diff_path: Path, out_path: Path, manifest: dict[str, object]) -> None:
    source = Image.open(source_path).convert("RGB")
    rebuilt = Image.open(rebuilt_path).convert("RGB")
    diff = Image.open(diff_path).convert("RGB")
    board = Image.new("RGB", (1800, 1180), (245, 243, 238))
    draw = ImageDraw.Draw(board)
    title = font(32)
    body = font(20)
    caption = font(16)
    draw.text((40, 30), "Blood Axe Cairnstone A001 - Blueprint Restart Source Proof", fill=(22, 20, 18), font=title)
    draw.text((40, 78), "Stage 1 only: full source scanline capture. No crops, masks, geometry, UVs, or fixes generated.", fill=(55, 48, 42), font=body)
    max_w, max_h = 520, 735
    resample_nearest = getattr(getattr(Image, "Resampling", Image), "NEAREST")
    for label, image, x in (("Source", source, 40), ("Rebuilt From Scanlines", rebuilt, 640), ("Difference", diff, 1240)):
        preview = image.copy()
        preview.thumbnail((max_w, max_h), resample_nearest)
        board.paste(preview, (x, 140))
        draw.rectangle((x, 140, x + max_w, 140 + max_h), outline=(70, 64, 56), width=2)
        draw.text((x, 895), label, fill=(28, 25, 22), font=body)
    proof_lines = [
        f"pixel_exact: {manifest['pixel_exact']}",
        f"changed_pixels: {manifest['changed_pixels']}",
        f"max_rgb_delta: {manifest['max_rgb_delta']}",
        f"source_sha256: {manifest['source_sha256']}",
        "Blueprint rule: no downstream step may proceed unless this proof is exact.",
    ]
    y = 940
    for line in proof_lines:
        draw.text((40, y), line, fill=(36, 32, 28), font=caption)
        y += 28
    board.save(out_path)


def main() -> None:
    ensure_dir(SCAN_DIR)
    source = Image.open(SOURCE).convert("RGB")
    raw = source.tobytes()
    target_path = SCAN_DIR / f"{ASSET_NAME}_SourceTemplate_ScanTarget.png"
    scan_path = SCAN_DIR / f"{ASSET_NAME}_SourceTemplate.rgbscan.gz"
    rebuilt_path = SCAN_DIR / f"{ASSET_NAME}_SourceTemplate_RebuiltFromScanlines.png"
    diff_path = SCAN_DIR / f"{ASSET_NAME}_SourceTemplate_Difference.png"
    board_path = OUT_DIR / f"{ASSET_NAME}_A001BlueprintRestart_SourceProofBoard.png"
    manifest_path = OUT_DIR / f"{ASSET_NAME}_A001BlueprintRestartManifest.json"

    source.save(target_path)
    with gzip.open(scan_path, "wb") as handle:
        handle.write(raw)
    with gzip.open(scan_path, "rb") as handle:
        rebuilt_raw = handle.read()
    rebuilt = Image.frombytes("RGB", source.size, rebuilt_raw)
    rebuilt.save(rebuilt_path)
    diff = ImageChops.difference(source, rebuilt)
    diff.save(diff_path)

    manifest: dict[str, object] = {
        "asset": ASSET_NAME,
        "status": "A001 blueprint restart stage 1 source proof",
        "blueprint": str(BLUEPRINT.relative_to(ROOT)),
        "source": str(SOURCE.relative_to(ROOT)),
        "source_size_px": list(source.size),
        "source_mode": source.mode,
        "source_sha256": sha256_file(SOURCE),
        "blueprint_sha256": sha256_file(BLUEPRINT),
        "pixel_exact": raw == rebuilt_raw,
        "changed_pixels": changed_pixels(diff),
        "max_rgb_delta": max_rgb_delta(diff),
        "scanline_raw_sha256": sha256_bytes(raw),
        "target_sha256": sha256_file(target_path),
        "rebuilt_sha256": sha256_file(rebuilt_path),
        "fresh_pass_rule": {
            "fresh_data_only": True,
            "prior_candidate_outputs_used": False,
            "prior_asset_specific_generator_copied": False,
            "old_review_renders_used_as_source": False,
            "non_blueprint_methods_used": False,
        },
        "completed_blueprint_steps": [
            "Approved Source Intake",
            "Lossless Scanline Capture",
        ],
        "blocked_until_declared_next": [
            "source decomposition crop-boundary formulas",
            "pixel convention",
            "coordinate frame",
            "calibration formulas",
            "formula-derived measurement masks",
        ],
        "outputs": {
            "scanline_path": str(scan_path.relative_to(ROOT)),
            "target_path": str(target_path.relative_to(ROOT)),
            "rebuilt_path": str(rebuilt_path.relative_to(ROOT)),
            "difference_path": str(diff_path.relative_to(ROOT)),
            "source_proof_board": str(board_path.relative_to(ROOT)),
        },
        "rule": "A001 restarts from full-source scanline proof only. No crops, masks, geometry, UVs, contact fixes, inferred fill, or visual fixes are generated in this stage.",
    }
    if not manifest["pixel_exact"] or manifest["changed_pixels"] != 0 or manifest["max_rgb_delta"] != 0:
        raise SystemExit("A001 source scanline proof failed; stopping.")
    ensure_dir(OUT_DIR)
    create_source_proof_board(target_path, rebuilt_path, diff_path, board_path, manifest)
    manifest_path.write_text(json.dumps(manifest, indent=2) + "\n")
    print(f"A001 source proof manifest: {manifest_path}")
    print(f"A001 source proof board: {board_path}")
    print("pixel_exact=True changed_pixels=0 max_rgb_delta=0")


if __name__ == "__main__":
    main()
