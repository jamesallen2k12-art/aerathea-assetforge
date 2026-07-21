#!/usr/bin/env python3
"""Package and validate the exact Siege Breaker A02 DCC review board."""

from __future__ import annotations

import hashlib
import json
from pathlib import Path

from PIL import Image, ImageDraw, ImageFont, ImageOps, ImageStat


ROOT = Path(__file__).resolve().parents[2]
ASSET_ID = "SM_DRW_SiegeBreaker_Hammer_A01"
REVISION = "VisualFidelity_A02"
CONTRACT_ID = "SB-VF-A02"
OUTPUT_ROOT = ROOT / "Saved/Automation/DCC" / ASSET_ID / REVISION
BLEND_PATH = ROOT / "SourceAssets/Blender/Weapons/Dwarven" / ASSET_ID / f"{ASSET_ID}_DCCGameReady_{REVISION}.blend"
FULL_PATH = OUTPUT_ROOT / f"{ASSET_ID}_{REVISION}_FinalReview_Full.png"
HEAD_PATH = OUTPUT_ROOT / "details/head" / f"{ASSET_ID}_{REVISION}_Detail_head.png"
GRIP_PATH = OUTPUT_ROOT / "details/grip" / f"{ASSET_ID}_{REVISION}_Detail_grip.png"
POMMEL_PATH = OUTPUT_ROOT / "details/pommel" / f"{ASSET_ID}_{REVISION}_Detail_pommel.png"
FRONT_PATH = OUTPUT_ROOT / "orthographic_true/front.png"
BOARD_PATH = OUTPUT_ROOT / f"{ASSET_ID}_{REVISION}_FinalReviewBoard.png"
VALIDATION_PATH = ROOT / "docs/assets/blueprints" / ASSET_ID / "manifests/VISUAL_FIDELITY_A02_RENDER_VALIDATION.json"


def sha256(path: Path) -> str:
    digest = hashlib.sha256()
    with path.open("rb") as handle:
        for chunk in iter(lambda: handle.read(1024 * 1024), b""):
            digest.update(chunk)
    return digest.hexdigest()


def load_font(size: int, bold: bool = False):
    name = "DejaVuSans-Bold.ttf" if bold else "DejaVuSans.ttf"
    path = Path("/usr/share/fonts/truetype/dejavu") / name
    return ImageFont.truetype(str(path), size=size) if path.exists() else ImageFont.load_default()


def image_record(path: Path, expected_size: tuple[int, int]):
    with Image.open(path) as image:
        rgb = image.convert("RGB")
        extrema = rgb.convert("L").getextrema()
        stat = ImageStat.Stat(rgb.convert("L"))
        return {
            "path": str(path.relative_to(ROOT)),
            "sha256": sha256(path),
            "size_px": list(rgb.size),
            "expected_size_px": list(expected_size),
            "size_pass": rgb.size == expected_size,
            "luma_extrema": list(extrema),
            "luma_stddev": round(float(stat.stddev[0]), 6),
            "non_black_pass": extrema[1] > 24 and stat.stddev[0] > 4.0,
        }


def place_panel(canvas, draw, source_path: Path, box, label: str):
    x0, y0, x1, y1 = box
    panel_bg = (10, 15, 24)
    border = (70, 92, 122)
    draw.rounded_rectangle(box, radius=14, fill=panel_bg, outline=border, width=3)
    label_font = load_font(27, bold=True)
    label_y = y0 + 14
    draw.text((x0 + 18, label_y), label, font=label_font, fill=(205, 221, 240))
    image_box = (x0 + 12, y0 + 58, x1 - 12, y1 - 12)
    available = (image_box[2] - image_box[0], image_box[3] - image_box[1])
    with Image.open(source_path) as source:
        rendered = ImageOps.contain(source.convert("RGB"), available, Image.Resampling.LANCZOS)
    px = image_box[0] + (available[0] - rendered.width) // 2
    py = image_box[1] + (available[1] - rendered.height) // 2
    canvas.paste(rendered, (px, py))


def main() -> int:
    required = [BLEND_PATH, FULL_PATH, HEAD_PATH, GRIP_PATH, POMMEL_PATH, FRONT_PATH]
    missing = [str(path) for path in required if not path.exists()]
    if missing:
        raise FileNotFoundError(f"Missing review inputs: {missing}")

    ortho_manifest_path = OUTPUT_ROOT / "orthographic_true/render_manifest.json"
    full_manifest_path = OUTPUT_ROOT / "beauty_render_manifest.json"
    detail_manifest_paths = {
        focus: OUTPUT_ROOT / f"details/{focus}/beauty_render_manifest.json"
        for focus in ("head", "grip", "pommel")
    }
    ortho_manifest = json.loads(ortho_manifest_path.read_text(encoding="utf-8"))
    full_manifest = json.loads(full_manifest_path.read_text(encoding="utf-8"))
    detail_manifests = {
        focus: json.loads(path.read_text(encoding="utf-8"))
        for focus, path in detail_manifest_paths.items()
    }

    image_records = {
        "full": image_record(FULL_PATH, (1600, 2000)),
        "head": image_record(HEAD_PATH, (1200, 1200)),
        "grip": image_record(GRIP_PATH, (1200, 1200)),
        "pommel": image_record(POMMEL_PATH, (1200, 1200)),
        "front": image_record(FRONT_PATH, (2048, 2048)),
    }
    source_hash = sha256(BLEND_PATH)
    manifest_checks = {
        "ortho_source_hash": ortho_manifest.get("source_blend_sha256") == source_hash,
        "ortho_views": sorted(ortho_manifest.get("views", {})) == ["back", "bottom", "front", "left", "right", "top"],
        "ortho_resolution": ortho_manifest.get("resolution_px") == [2048, 2048],
        "full_hash": full_manifest.get("image_sha256") == image_records["full"]["sha256"],
        "full_focus": full_manifest.get("focus") == "full",
        "detail_hashes": all(
            detail_manifests[focus].get("image_sha256") == image_records[focus]["sha256"]
            for focus in ("head", "grip", "pommel")
        ),
        "detail_focus": all(detail_manifests[focus].get("focus") == focus for focus in ("head", "grip", "pommel")),
    }
    image_checks_pass = all(record["size_pass"] and record["non_black_pass"] for record in image_records.values())
    if not image_checks_pass or not all(manifest_checks.values()):
        raise RuntimeError(f"Render validation failed: images={image_records}, manifests={manifest_checks}")

    canvas = Image.new("RGB", (3200, 2100), (16, 22, 33))
    draw = ImageDraw.Draw(canvas)
    title_font = load_font(54, bold=True)
    subtitle_font = load_font(25)
    tag_font = load_font(23, bold=True)
    draw.text((44, 32), "SIEGE BREAKER — VISUAL FIDELITY A02", font=title_font, fill=(230, 239, 250))
    draw.text((48, 101), "AERATHEAN DWARVEN GREAT HAMMER  •  CONTRACT SB-VF-A02", font=subtitle_font, fill=(137, 165, 202))

    tags = [
        ("DCC GAME-READY CANDIDATE", (34, 82, 117)),
        ("38 / 38 TECHNICAL PASS", (43, 105, 75)),
        ("VISUAL APPROVAL PENDING", (119, 77, 31)),
        ("NOT UNREAL-VALIDATED", (91, 52, 70)),
    ]
    tx = 1480
    for label, color in tags:
        width = int(draw.textlength(label, font=tag_font)) + 34
        draw.rounded_rectangle((tx, 47, tx + width, 91), radius=12, fill=color)
        draw.text((tx + 17, 56), label, font=tag_font, fill=(244, 248, 252))
        tx += width + 16

    place_panel(canvas, draw, FULL_PATH, (40, 170, 1240, 2020), "FULL 3/4 REVIEW")
    place_panel(canvas, draw, HEAD_PATH, (1280, 170, 2220, 1110), "HEAD / BRACING / RUNESTONE")
    place_panel(canvas, draw, FRONT_PATH, (2260, 170, 3160, 1110), "TRUE FRONT ORTHOGRAPHIC")
    place_panel(canvas, draw, GRIP_PATH, (1280, 1150, 2200, 2020), "CRISSCROSS GRIP / SHAFT")
    place_panel(canvas, draw, POMMEL_PATH, (2240, 1150, 3160, 2020), "LAYERED POMMEL")

    canvas.save(BOARD_PATH, optimize=True)
    board_record = image_record(BOARD_PATH, (3200, 2100))
    result = {
        "schema": "aerathea.visual_fidelity_render_validation.v1",
        "asset_id": ASSET_ID,
        "revision": REVISION,
        "contract_id": CONTRACT_ID,
        "artifact_status": "proof only",
        "result": "pass",
        "pipeline_status": "DCC game-ready candidate",
        "source_blend": {"path": str(BLEND_PATH.relative_to(ROOT)), "sha256": source_hash},
        "images": image_records,
        "manifest_checks": manifest_checks,
        "review_board": board_record,
        "final_visual_approval": "pending Flamestrike",
        "unreal_authorized": False,
        "fully_game_ready": False,
    }
    VALIDATION_PATH.parent.mkdir(parents=True, exist_ok=True)
    VALIDATION_PATH.write_text(json.dumps(result, indent=2) + "\n", encoding="utf-8")
    print(BOARD_PATH)
    print(VALIDATION_PATH)
    print(f"RENDER_VALIDATION=pass BOARD_SHA256={board_record['sha256']}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
