#!/usr/bin/env python3
"""Package the audited shared-depth twin renders into one review board."""

from __future__ import annotations

import hashlib
import json
from pathlib import Path

from PIL import Image, ImageDraw, ImageFont


ROOT = Path(__file__).resolve().parents[2]
PROOF_ROOT = ROOT / (
    "docs/assets/blueprints/SM_DRW_SiegeBreaker_Hammer_A01/proof_runs/"
    "SB-CR-STEPS10-16-R8-ZERO-EXTRUSION-A02"
)
BOARD = PROOF_ROOT / "review/FRESH_TWIN_DCC_SOURCE_BUILDER_A01_REVIEW.png"
MANIFEST = (
    PROOF_ROOT
    / "manifests/FRESH_TWIN_DCC_SOURCE_BUILDER_A01_REVIEW_MANIFEST.json"
)
ASSETS = {
    "siege_breaker": {
        "asset_id": "SM_DRW_SiegeBreaker_Hammer_A01",
        "display_name": "SIEGE BREAKER",
        "treatment": "DOUBLE RUNE SIDED",
        "root": ROOT
        / (
            "SourceAssets/Blender/Weapons/Dwarven/"
            "SM_DRW_SiegeBreaker_Hammer_A01/"
            "A12_R10_R8_SharedDepth_DCCSource_A01"
        ),
    },
    "foe_hammer": {
        "asset_id": "SM_DRW_FoeHammer_Hammer_A01",
        "display_name": "FOE HAMMER",
        "treatment": "DOUBLE METAL-CENTER-PIECE SIDED",
        "root": ROOT
        / (
            "SourceAssets/Blender/Weapons/Dwarven/"
            "SM_DRW_FoeHammer_Hammer_A01/"
            "A12_R10_R8_SharedDepth_DCCSource_A01"
        ),
    },
}
VIEWS = ("front", "right", "top", "three_quarter")


def sha256(path: Path) -> str:
    digest = hashlib.sha256()
    with path.open("rb") as handle:
        for block in iter(lambda: handle.read(1024 * 1024), b""):
            digest.update(block)
    return digest.hexdigest()


def relative(path: Path) -> str:
    return str(path.resolve().relative_to(ROOT))


def load_json(path: Path) -> dict:
    return json.loads(path.read_text(encoding="utf-8"))


def resample_filter() -> int:
    if hasattr(Image, "Resampling"):
        return Image.Resampling.LANCZOS
    if hasattr(Image, "LANCZOS"):
        return Image.LANCZOS
    return Image.ANTIALIAS


def main() -> int:
    audits = {}
    render_manifests = {}
    for key, asset in ASSETS.items():
        audit_path = asset["root"] / "independent_saved_file_audit.json"
        render_manifest_path = asset["root"] / "render_manifest.json"
        audit = load_json(audit_path)
        render_manifest = load_json(render_manifest_path)
        if audit["result"] != "PASS":
            raise RuntimeError(f"{key} saved-file audit is not PASS")
        if render_manifest["independent_audit_sha256"] != sha256(audit_path):
            raise RuntimeError(f"{key} render did not use the current audit")
        for view in VIEWS:
            image_path = asset["root"] / "renders" / f"{view}.png"
            if (
                render_manifest["views"][view]["sha256"]
                != sha256(image_path)
            ):
                raise RuntimeError(f"{key} {view} image hash mismatch")
        audits[key] = audit
        render_manifests[key] = render_manifest

    font_root = Path("/usr/share/fonts/truetype/dejavu")
    title_font = ImageFont.truetype(
        str(font_root / "DejaVuSans-Bold.ttf"), 30
    )
    asset_font = ImageFont.truetype(
        str(font_root / "DejaVuSans-Bold.ttf"), 22
    )
    normal_font = ImageFont.truetype(
        str(font_root / "DejaVuSans.ttf"), 16
    )
    small_font = ImageFont.truetype(
        str(font_root / "DejaVuSans.ttf"), 13
    )
    tile = 300
    margin = 24
    header = 94
    row_label = 56
    footer = 60
    width = margin * 2 + tile * 4
    height = header + (row_label + tile) * 2 + footer
    board = Image.new("RGB", (width, height), (12, 17, 24))
    draw = ImageDraw.Draw(board)
    draw.text(
        (margin, 16),
        "AERATHEA — SHARED-DEPTH TWIN HAMMERS",
        font=title_font,
        fill=(232, 238, 245),
    )
    draw.text(
        (margin, 57),
        (
            "97.974428267601 × 44.299176584 × 170 cm  |  "
            "zero cross-asset XYZ difference"
        ),
        font=normal_font,
        fill=(148, 188, 226),
    )
    y = header
    for key in ("siege_breaker", "foe_hammer"):
        asset = ASSETS[key]
        audit = audits[key]
        draw.text(
            (margin, y + 8),
            f"{asset['display_name']} — {asset['treatment']}",
            font=asset_font,
            fill=(232, 238, 245),
        )
        draw.text(
            (width - 265, y + 14),
            f"AUDIT {audit['result']}  •  DCC SOURCE CANDIDATE",
            font=small_font,
            fill=(128, 218, 168),
        )
        y += row_label
        for index, view in enumerate(VIEWS):
            source = (
                asset["root"] / "renders" / f"{view}.png"
            )
            image = Image.open(source).convert("RGB")
            image.thumbnail((tile, tile), resample_filter())
            panel = Image.new("RGB", (tile, tile), (20, 27, 36))
            panel.paste(
                image,
                ((tile - image.width) // 2, (tile - image.height) // 2),
            )
            x = margin + index * tile
            board.paste(panel, (x, y))
            draw.rectangle(
                (x, y, x + tile - 1, y + tile - 1),
                outline=(63, 80, 98),
                width=1,
            )
            draw.text(
                (x + 9, y + 9),
                view.replace("_", " ").upper(),
                font=small_font,
                fill=(202, 214, 225),
            )
        y += tile
    draw.text(
        (margin, height - 42),
        (
            "Candidate visual review • exact shared base independently "
            "verified • Step 13 / export / Unreal remain locked"
        ),
        font=small_font,
        fill=(145, 157, 171),
    )
    BOARD.parent.mkdir(parents=True, exist_ok=True)
    board.save(BOARD)

    manifest = {
        "schema": "AERATHEA_FRESH_TWIN_DCC_SOURCE_REVIEW_A01_V1",
        "artifact_status": "candidate review evidence",
        "board": {
            "path": relative(BOARD),
            "sha256": sha256(BOARD),
        },
        "packager": {
            "path": relative(Path(__file__)),
            "sha256": sha256(Path(__file__)),
        },
        "assets": {
            key: {
                "asset_id": asset["asset_id"],
                "independent_audit_result": audits[key]["result"],
                "independent_audit_sha256": sha256(
                    asset["root"] / "independent_saved_file_audit.json"
                ),
                "render_manifest_sha256": sha256(
                    asset["root"] / "render_manifest.json"
                ),
            }
            for key, asset in ASSETS.items()
        },
        "prior_packaging_attempt": {
            "result": "FAIL",
            "scope": "board composition only",
            "cause": (
                "system Pillow does not expose Image.Resampling; all eight "
                "source renders completed and remained valid"
            ),
            "geometry_or_audit_affected": False,
        },
        "result": "PASS",
        "step_13_authority": False,
        "retopology_uv_bake_export_authority": False,
        "unreal_authority": False,
    }
    MANIFEST.write_text(
        json.dumps(manifest, indent=2, sort_keys=True) + "\n",
        encoding="utf-8",
    )
    print(f"Review board: {relative(BOARD)}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
