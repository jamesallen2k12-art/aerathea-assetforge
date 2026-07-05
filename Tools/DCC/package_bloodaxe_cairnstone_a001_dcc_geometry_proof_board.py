#!/usr/bin/env python3
"""Package A001 DCC geometry proof renders into a single review board."""

from __future__ import annotations

import json
from pathlib import Path
from typing import Any

from PIL import Image, ImageDraw, ImageFont


ROOT = Path(__file__).resolve().parents[2]
ASSET_NAME = "SM_GIA_BloodAxeCairnstone_A001"
OUT_DIR = ROOT / "Saved/Automation/DCC" / ASSET_NAME
MANIFEST_PATH = OUT_DIR / f"{ASSET_NAME}_A001DCCGeometryProofManifest.json"
BOARD_PATH = OUT_DIR / f"{ASSET_NAME}_A001DCCGeometryProofReviewBoard.png"


def load_font(size: int) -> ImageFont.FreeTypeFont | ImageFont.ImageFont:
    candidates = [
        "/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf",
        "/usr/share/fonts/truetype/dejavu/DejaVuSans.ttf",
    ]
    for candidate in candidates:
        path = Path(candidate)
        if path.exists():
            return ImageFont.truetype(str(path), size)
    return ImageFont.load_default()


def read_manifest() -> dict[str, Any]:
    if not MANIFEST_PATH.exists():
        raise SystemExit(f"Missing DCC geometry proof manifest: {MANIFEST_PATH}")
    return json.loads(MANIFEST_PATH.read_text())


def fit_image(image: Image.Image, box: tuple[int, int]) -> Image.Image:
    fitted = image.copy()
    resample = getattr(getattr(Image, "Resampling", Image), "LANCZOS")
    fitted.thumbnail(box, resample)
    canvas = Image.new("RGB", box, (42, 42, 42))
    x = (box[0] - fitted.width) // 2
    y = (box[1] - fitted.height) // 2
    canvas.paste(fitted.convert("RGB"), (x, y))
    return canvas


def draw_wrapped_text(draw: ImageDraw.ImageDraw, xy: tuple[int, int], text: str, font: ImageFont.ImageFont, fill: tuple[int, int, int], width: int, line_height: int) -> int:
    words = text.split()
    lines: list[str] = []
    line = ""
    for word in words:
        candidate = f"{line} {word}".strip()
        if draw.textbbox((0, 0), candidate, font=font)[2] <= width:
            line = candidate
        else:
            if line:
                lines.append(line)
            line = word
    if line:
        lines.append(line)
    x, y = xy
    for row in lines:
        draw.text((x, y), row, font=font, fill=fill)
        y += line_height
    return y


def main() -> None:
    manifest = read_manifest()
    proof_renders = manifest.get("proof_renders", {})
    labels = ["front", "back", "left", "right", "top", "angle"]
    missing = [
        label
        for label in labels
        if label not in proof_renders or not (ROOT / proof_renders[label]).exists()
    ]
    if missing:
        raise SystemExit("Missing proof render(s): " + ", ".join(missing))

    title_font = load_font(34)
    label_font = load_font(23)
    body_font = load_font(20)
    small_font = load_font(16)

    tile_w, tile_h = 620, 470
    margin = 34
    gap = 22
    header_h = 150
    footer_h = 178
    board_w = margin * 2 + tile_w * 3 + gap * 2
    board_h = header_h + tile_h * 2 + gap + footer_h + margin
    board = Image.new("RGB", (board_w, board_h), (28, 28, 28))
    draw = ImageDraw.Draw(board)

    draw.rectangle((0, 0, board_w, header_h), fill=(38, 38, 36))
    draw.text((margin, 26), "A001 DCC Source Candidate Geometry Proof", font=title_font, fill=(245, 236, 210))
    draw.text(
        (margin, 76),
        "Fresh A001 measured geometry only: components separate, no UVs, no textures, no FBX, no Unreal import, no beauty render.",
        font=body_font,
        fill=(210, 205, 190),
    )
    draw.text(
        (margin, 108),
        "Colors: primary object red, independent contact/socket layer orange, support/base blue, approved measured footprint guides grey/cyan/yellow.",
        font=small_font,
        fill=(188, 188, 176),
    )

    for index, label in enumerate(labels):
        row = index // 3
        col = index % 3
        x = margin + col * (tile_w + gap)
        y = header_h + row * (tile_h + gap)
        draw.rectangle((x - 2, y - 2, x + tile_w + 2, y + tile_h + 2), outline=(95, 95, 88), width=2)
        render = Image.open(ROOT / proof_renders[label])
        fitted = fit_image(render, (tile_w, tile_h - 38))
        board.paste(fitted, (x, y + 38))
        draw.rectangle((x, y, x + tile_w, y + 38), fill=(50, 50, 46))
        draw.text((x + 12, y + 8), label.upper(), font=label_font, fill=(245, 236, 210))

    footer_y = header_h + tile_h * 2 + gap + 24
    draw.rectangle((0, footer_y - 18, board_w, board_h), fill=(38, 38, 36))
    proof_dimensions = manifest.get("proof_dimensions_cm", {})
    dimensions_text = (
        "Proof dimensions from approved manifests: "
        f"front {proof_dimensions.get('front_top_width_cm')}->{proof_dimensions.get('front_bottom_width_cm')}cm, "
        f"back {proof_dimensions.get('back_top_width_cm')}->{proof_dimensions.get('back_bottom_width_cm')}cm, "
        f"left {proof_dimensions.get('left_top_depth_cm')}->{proof_dimensions.get('left_bottom_depth_cm')}cm, "
        f"right {proof_dimensions.get('right_top_depth_cm')}->{proof_dimensions.get('right_bottom_depth_cm')}cm."
    )
    y = draw_wrapped_text(draw, (margin, footer_y), dimensions_text, body_font, (220, 214, 198), board_w - margin * 2, 28)
    status_text = (
        "Validation status: DCC source candidate only. Exterior seam weld, UV ownership, texture synthesis, FBX export, and Unreal validation remain blocked "
        "until this geometry proof is reviewed."
    )
    draw_wrapped_text(draw, (margin, y + 14), status_text, body_font, (220, 214, 198), board_w - margin * 2, 28)

    board.save(BOARD_PATH)
    manifest["review_board"] = str(BOARD_PATH.relative_to(ROOT))
    MANIFEST_PATH.write_text(json.dumps(manifest, indent=2) + "\n")
    print(BOARD_PATH)


if __name__ == "__main__":
    main()
