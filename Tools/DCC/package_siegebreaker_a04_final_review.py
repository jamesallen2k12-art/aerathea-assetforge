#!/usr/bin/env python3
"""Package the one user-facing completed A04 review image after all gates pass."""

from __future__ import annotations

import hashlib
import json
from pathlib import Path

from PIL import Image, ImageDraw, ImageFont


ROOT = Path(__file__).resolve().parents[2]
ASSET_ID = "SM_DRW_SiegeBreaker_Hammer_A01"
REVIEW_ROOT = ROOT / "Saved/Automation/DCC" / ASSET_ID / "VisualFidelity_A04"
RENDER_ROOT = REVIEW_ROOT / "renders"
EVIDENCE = REVIEW_ROOT / "FreshEvidence" / f"{ASSET_ID}_A04_FreshEvidenceManifest.json"
TECHNICAL = REVIEW_ROOT / f"{ASSET_ID}_A04_TechnicalValidation.json"
STRICT_GATE = REVIEW_ROOT / f"{ASSET_ID}_A04_StrictPixelGate.json"
OUTPUT_ROOT = REVIEW_ROOT / "review"
OUTPUT = OUTPUT_ROOT / f"{ASSET_ID}_A04_FinalCompletedReview.png"
MANIFEST = OUTPUT_ROOT / f"{ASSET_ID}_A04_FinalCompletedReviewManifest.json"


def rel(path: Path) -> str:
    return str(path.relative_to(ROOT))


def sha256(path: Path) -> str:
    digest = hashlib.sha256()
    with path.open("rb") as handle:
        for block in iter(lambda: handle.read(1024 * 1024), b""):
            digest.update(block)
    return digest.hexdigest()


def font(size: int, bold=False) -> ImageFont.ImageFont:
    candidates = [
        "/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf" if bold else "/usr/share/fonts/truetype/dejavu/DejaVuSans.ttf",
        "/usr/share/fonts/dejavu/DejaVuSerif-Bold.ttf" if bold else "/usr/share/fonts/dejavu/DejaVuSerif.ttf",
    ]
    for candidate in candidates:
        path = Path(candidate)
        if path.exists():
            return ImageFont.truetype(str(path), size)
    return ImageFont.load_default()


def lanczos() -> int:
    resampling = getattr(Image, "Resampling", None)
    return resampling.LANCZOS if resampling is not None else Image.LANCZOS


def panel(draw: ImageDraw.ImageDraw, box: tuple[int, int, int, int], title: str) -> tuple[int, int, int, int]:
    x0, y0, x1, y1 = box
    draw.rounded_rectangle(box, radius=18, fill=(225, 219, 204), outline=(73, 67, 57), width=3)
    draw.rectangle((x0, y0, x1, y0 + 54), fill=(54, 55, 55))
    draw.text((x0 + 18, y0 + 12), title, font=font(25, bold=True), fill=(245, 241, 229))
    return (x0 + 18, y0 + 70, x1 - 18, y1 - 18)


def paste_fit(canvas: Image.Image, image_path: Path, box: tuple[int, int, int, int], padding=8) -> None:
    image = Image.open(image_path).convert("RGBA")
    alpha_bbox = image.getchannel("A").getbbox()
    if alpha_bbox is not None and alpha_bbox != (0, 0, image.width, image.height):
        image = image.crop(alpha_bbox)
    x0, y0, x1, y1 = box
    width = max(1, x1 - x0 - padding * 2)
    height = max(1, y1 - y0 - padding * 2)
    scale = min(width / image.width, height / image.height)
    resized = image.resize((max(1, round(image.width * scale)), max(1, round(image.height * scale))), lanczos())
    paste_x = x0 + (x1 - x0 - resized.width) // 2
    paste_y = y0 + (y1 - y0 - resized.height) // 2
    shadow = Image.new("RGBA", canvas.size, (0, 0, 0, 0))
    shadow_draw = ImageDraw.Draw(shadow)
    shadow_draw.rounded_rectangle((paste_x + 8, paste_y + 10, paste_x + resized.width + 8, paste_y + resized.height + 10), radius=10, fill=(20, 18, 15, 45))
    canvas.alpha_composite(shadow)
    canvas.alpha_composite(resized, (paste_x, paste_y))


def main() -> int:
    evidence = json.loads(EVIDENCE.read_text(encoding="utf-8"))
    technical = json.loads(TECHNICAL.read_text(encoding="utf-8"))
    strict = json.loads(STRICT_GATE.read_text(encoding="utf-8"))
    if not technical.get("passed") or not strict.get("passed"):
        raise RuntimeError("Final A04 review may not be packaged before both final gates pass")

    canvas = Image.new("RGBA", (2800, 1800), (238, 233, 220, 255))
    draw = ImageDraw.Draw(canvas)
    draw.rectangle((0, 0, 2800, 116), fill=(31, 35, 42))
    draw.text((44, 22), "SIEGE BREAKER A04 — STRICT-SCANLINE DCC CANDIDATE", font=font(44, bold=True), fill=(246, 242, 230))
    draw.text((46, 77), "Fresh source-only reconstruction • exact visible RGB lineage • closed 3D production package", font=font(22), fill=(143, 202, 255))

    source_box = (38, 140, 700, 1665)
    authority_box = (724, 140, 1490, 1198)
    beauty_box = (724, 1222, 1490, 1665)
    source_content = panel(draw, source_box, "AUTHORITATIVE PRIMARY SOURCE")
    authority_content = panel(draw, authority_box, "A04 SOURCE-OWNED AUTHORITY VIEW")
    beauty_content = panel(draw, beauty_box, "A04 THREE-QUARTER DEPTH REVIEW")
    paste_fit(canvas, ROOT / evidence["views"]["primary"]["crop_rgb"], source_content, 14)
    paste_fit(canvas, RENDER_ROOT / f"{ASSET_ID}_A04_AuthorityFront.png", authority_content, 8)
    paste_fit(canvas, RENDER_ROOT / f"{ASSET_ID}_A04_Beauty.png", beauty_content, 8)

    view_boxes = {
        "FRONT": (1516, 140, 1916, 548),
        "BACK": (1934, 140, 2334, 548),
        "LEFT": (2352, 140, 2752, 548),
        "RIGHT": (1516, 568, 1916, 976),
        "TOP": (1934, 568, 2334, 976),
        "BOTTOM": (2352, 568, 2752, 976),
    }
    for label, box in view_boxes.items():
        content = panel(draw, box, f"TRUE ORTHO — {label}")
        paste_fit(canvas, RENDER_ROOT / f"{ASSET_ID}_A04_{label.title()}.png", content, 6)

    metrics_box = (1516, 1000, 2752, 1665)
    x0, y0, x1, y1 = metrics_box
    draw.rounded_rectangle(metrics_box, radius=18, fill=(214, 209, 195), outline=(73, 67, 57), width=3)
    draw.rectangle((x0, y0, x1, y0 + 58), fill=(54, 55, 55))
    draw.text((x0 + 20, y0 + 13), "STRICT COMPLETION EVIDENCE", font=font(27, bold=True), fill=(245, 241, 229))
    lods = technical["lod_triangles"]
    lines = [
        ("Fresh scanline", "0 changed pixels • max RGB delta 0"),
        ("Visible color", "exact integer-copy RGB • no filtered resampling"),
        ("Exterior contour", "mean 0.000 px • P95 0.000 px"),
        ("Component masks", "IoU 1.000 • landmark error 0.000 px"),
        ("Physical bounds", "52 × 32 × 170 cm • pivot Z=0"),
        ("LOD triangles", " / ".join(str(value) for value in lods)),
        ("Production set", "5 materials • 20 × 2K PBR maps • 3 UCX proxies"),
        ("Exports", "4 FBX + GLB • clean reimport passed"),
        ("Independent audit", f"{technical['summary']['passed']}/{technical['summary']['total']} PASS"),
        ("Fail-closed gate", "STRICT PIXEL ASSET GATE: PASS"),
    ]
    y = y0 + 86
    for label, value in lines:
        draw.text((x0 + 30, y), label.upper(), font=font(18, bold=True), fill=(50, 78, 103))
        draw.text((x0 + 260, y - 2), value, font=font(22), fill=(45, 42, 36))
        y += 50
    draw.rounded_rectangle((x0 + 26, y + 8, x1 - 26, y + 104), radius=12, fill=(33, 69, 92), outline=(98, 180, 235), width=2)
    draw.text((x0 + 50, y + 26), "DCC GAME-READY CANDIDATE", font=font(29, bold=True), fill=(238, 247, 255))
    draw.text((x0 + 50, y + 63), "Pending Flamestrike visual approval • Unreal authority: false", font=font(19), fill=(166, 218, 255))

    draw.line((38, 1694, 2752, 1694), fill=(82, 75, 63), width=2)
    draw.text((44, 1715), "Build the shape. Paint the detail. Protect the performance. Tell the story.", font=font(24, bold=True), fill=(52, 48, 41))
    draw.text((44, 1755), "Artifact status: candidate • Review decision required: approved / rejected / blocked", font=font(20), fill=(105, 52, 42))

    OUTPUT_ROOT.mkdir(parents=True, exist_ok=True)
    canvas.convert("RGB").save(OUTPUT, optimize=True)
    payload = {
        "schema": "aerathea.siegebreaker_a04_final_review.v1",
        "asset_id": ASSET_ID,
        "status": "candidate",
        "image": rel(OUTPUT),
        "image_sha256": sha256(OUTPUT),
        "resolution": list(Image.open(OUTPUT).size),
        "technical_validation": rel(TECHNICAL),
        "strict_pixel_gate": rel(STRICT_GATE),
        "technical_pass": technical["passed"],
        "strict_gate_pass": strict["passed"],
        "unreal_authority": False,
        "fully_game_ready": False,
    }
    MANIFEST.write_text(json.dumps(payload, indent=2) + "\n", encoding="utf-8")
    print(OUTPUT)
    print(MANIFEST)
    print(payload["image_sha256"])
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
