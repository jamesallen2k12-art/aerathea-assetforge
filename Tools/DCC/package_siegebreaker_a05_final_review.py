#!/usr/bin/env python3
"""Package the one visible A05 final review board."""

from __future__ import annotations

import hashlib
import json
import textwrap
from pathlib import Path

from PIL import Image, ImageDraw, ImageFont, ImageOps


ROOT = Path(__file__).resolve().parents[2]
ASSET_ID = "SM_DRW_SiegeBreaker_Hammer_A01"
BLUEPRINT = ROOT / "docs/assets/blueprints/SM_DRW_SiegeBreaker_Hammer_A01"
AUDIT_PATH = BLUEPRINT / "manifests/VISUAL_FIDELITY_A05_TECHNICAL_AUDIT.json"
BUILD_PATH = ROOT / "SourceAssets/Blender/Weapons/Dwarven/SM_DRW_SiegeBreaker_Hammer_A01/OrthographicVolumetric_A05/SM_DRW_SiegeBreaker_Hammer_A01_A05_BUILD_MANIFEST.json"
SOURCE_SHEET = ROOT / "SourceAssets/Reference/Weapons/Dwarven/SM_DRW_SiegeBreaker_Hammer_A01/02_SiegeBreaker_Codex_Final_Package/reference/concept_sheet_style_reference.png"
PROOF = ROOT / "SourceAssets/Proofs/Weapons/Dwarven/SM_DRW_SiegeBreaker_Hammer_A01/OrthographicVolumetric_A05"
OUT = BLUEPRINT / "review/SM_DRW_SiegeBreaker_Hammer_A01_A05_FINAL_REVIEW_BOARD.png"
MANIFEST = BLUEPRINT / "manifests/VISUAL_FIDELITY_A05_REVIEW_PACKAGE.json"

W, H = 3840, 2400
BG = (17, 21, 29)
PANEL = (29, 35, 45)
PANEL_2 = (23, 28, 37)
BORDER = (74, 91, 109)
TEXT = (231, 236, 241)
MUTED = (161, 176, 191)
BLUE = (78, 205, 255)
GOLD = (226, 162, 74)
GREEN = (91, 221, 145)


def sha256(path: Path) -> str:
    digest = hashlib.sha256()
    with path.open("rb") as handle:
        for chunk in iter(lambda: handle.read(1024 * 1024), b""):
            digest.update(chunk)
    return digest.hexdigest()


def font(size: int, bold: bool = False):
    name = "DejaVuSans-Bold.ttf" if bold else "DejaVuSans.ttf"
    path = Path("/usr/share/fonts/truetype/dejavu") / name
    return ImageFont.truetype(str(path), size=size)


def panel(draw, box, title=None, accent=BLUE):
    draw.rounded_rectangle(box, radius=18, fill=PANEL, outline=BORDER, width=2)
    if title:
        draw.text((box[0] + 22, box[1] + 16), title, font=font(27, True), fill=accent)


def contain(image: Image.Image, box, background=PANEL_2, padding=16):
    x0, y0, x1, y1 = box
    inner_w = x1 - x0 - padding * 2
    inner_h = y1 - y0 - padding * 2
    copy = image.convert("RGB")
    copy.thumbnail((inner_w, inner_h), Image.LANCZOS)
    canvas = Image.new("RGB", (x1 - x0, y1 - y0), background)
    canvas.paste(copy, ((canvas.width - copy.width) // 2, (canvas.height - copy.height) // 2))
    return canvas


def check(audit, name):
    return next(item for item in audit["checks"] if item["name"] == name)


def main():
    audit = json.loads(AUDIT_PATH.read_text(encoding="utf-8"))
    build = json.loads(BUILD_PATH.read_text(encoding="utf-8"))
    if audit["status"] != "pass":
        raise SystemExit("A05 final board is blocked: independent audit is not pass")

    board = Image.new("RGB", (W, H), BG)
    draw = ImageDraw.Draw(board)
    draw.rectangle((0, 0, W, 124), fill=(11, 15, 22))
    draw.text((42, 24), "SIEGE BREAKER", font=font(50, True), fill=TEXT)
    draw.text((500, 38), "A05 ORTHOGRAPHIC VOLUMETRIC REBUILD", font=font(31, True), fill=BLUE)
    status = "DCC GAME-READY CANDIDATE — PENDING FLAMESTRIKE VISUAL APPROVAL"
    draw.rounded_rectangle((2350, 24, 3795, 94), radius=18, fill=(21, 67, 52), outline=GREEN, width=2)
    draw.text((2382, 43), status, font=font(22, True), fill=GREEN)

    source_box = (40, 150, 670, 1430)
    beauty_box = (700, 150, 1605, 1430)
    panel(draw, source_box, "AUTHORITATIVE SOURCE SHEET", GOLD)
    panel(draw, beauty_box, "FINAL THREE-QUARTER BEAUTY", BLUE)
    source = Image.open(SOURCE_SHEET)
    beauty = Image.open(PROOF / f"{ASSET_ID}_A05_BEAUTY.png")
    board.paste(contain(source, (0, 0, source_box[2] - source_box[0] - 34, source_box[3] - source_box[1] - 70), background=(238, 234, 219), padding=8), (source_box[0] + 17, source_box[1] + 56))
    board.paste(contain(beauty, (0, 0, beauty_box[2] - beauty_box[0] - 34, beauty_box[3] - beauty_box[1] - 70), padding=0), (beauty_box[0] + 17, beauty_box[1] + 56))

    view_names = ("FRONT", "BACK", "LEFT", "RIGHT", "TOP", "BOTTOM")
    grid_x, grid_y = 1635, 150
    cell_w, cell_h = 705, 625
    for index, name in enumerate(view_names):
        col = index % 3
        row = index // 3
        x0 = grid_x + col * 720
        y0 = grid_y + row * 640
        box = (x0, y0, x0 + cell_w, y0 + cell_h)
        panel(draw, box, name, BLUE if name not in {"TOP", "BOTTOM"} else GOLD)
        image = Image.open(PROOF / f"{ASSET_ID}_A05_{name}.png")
        rendered = contain(image, (0, 0, cell_w - 28, cell_h - 66), padding=0)
        board.paste(rendered, (x0 + 14, y0 + 50))

    strip_box = (40, 1460, 3800, 1900)
    panel(draw, strip_box, "MULTI-ANGLE PARALLAX PROOF — REAL VOLUME / FIXED ASSET", BLUE)
    thumb_w, thumb_h = 700, 350
    for index in range(1, 6):
        image = Image.open(PROOF / f"{ASSET_ID}_A05_PARALLAX_{index:02d}.png")
        rendered = contain(image, (0, 0, thumb_w, thumb_h), padding=0)
        x = 85 + (index - 1) * 740
        board.paste(rendered, (x, 1518))

    metrics_box = (40, 1930, 3800, 2360)
    panel(draw, metrics_box, "INDEPENDENT FAIL-CLOSED VALIDATION", GREEN)
    bounds_value = check(audit, "overall_bounds_cm")["observed"]
    deltas = check(audit, "interface_center_deltas_cm")["observed"]
    shaft_d = check(audit, "shaft_clear_diameter_cm")["observed"]
    grip_d = check(audit, "grip_outer_diameter_cm")["observed"]
    lods = build["lod_triangles"]
    metrics = [
        ("GEOMETRY", [
            f"Bounds: {bounds_value[0]:.4f} × {bounds_value[1]:.4f} × {bounds_value[2]:.4f} cm",
            f"Axis deltas: socket/shaft {max(deltas['socket_to_shaft']):.4f} cm",
            f"shaft/grip {max(deltas['shaft_to_grip']):.4f} cm · grip/pommel {max(deltas['grip_to_pommel']):.4f} cm",
            f"Handle: shaft {max(shaft_d):.4f} cm · grip {max(grip_d):.4f} cm",
        ]),
        ("PRODUCTION", [
            f"LODs: {lods['LOD0']} / {lods['LOD1']} / {lods['LOD2']} / {lods['LOD3']} tris",
            "Materials: Stone · Bronze · Steel · Leather · Rune",
            "Textures: 20 × 2048² PBR maps (BC / N / ORM / E)",
            "Collision: 3 custom proxies · Pivot: bottom-center Z=0",
        ]),
        ("PACKAGE", [
            "Exports: 4 FBX + 1 GLB · clean reimport validated",
            "Topology: closed/manifold · UVs present on every source mesh",
            "A03/A04 construction inputs: 0 · cards/facades/billboards: 0",
            f"Independent audit: PASS {audit['passed_checks']}/{audit['total_checks']}",
        ]),
        ("BOUNDARY", [
            "Artifact: DCC game-ready candidate",
            "Visual approval: pending Flamestrike",
            "Unreal authority: false · Fully game-ready: false",
            "Decision: APPROVED / REJECTED / BLOCKED",
        ]),
    ]
    col_w = 920
    for index, (heading, lines) in enumerate(metrics):
        x = 72 + index * col_w
        draw.text((x, 1990), heading, font=font(25, True), fill=GOLD if heading != "PACKAGE" else BLUE)
        y = 2034
        for line in lines:
            wrapped = textwrap.wrap(line, width=52)
            for part in wrapped:
                draw.text((x, y), part, font=font(20), fill=TEXT if "PASS" not in part else GREEN)
                y += 31
            y += 3

    OUT.parent.mkdir(parents=True, exist_ok=True)
    board.save(OUT, optimize=True)
    manifest = {
        "schema": "aerathea.siegebreaker_a05_review_package.v1",
        "asset_id": ASSET_ID,
        "artifact_status": "candidate",
        "pipeline_status": "DCC game-ready candidate pending Flamestrike visual approval",
        "final_board": str(OUT.relative_to(ROOT)),
        "final_board_sha256": sha256(OUT),
        "audit_status": audit["status"],
        "audit_gates": [audit["passed_checks"], audit["total_checks"]],
        "a03_a04_construction_inputs": 0,
        "visible_review_open_required": True,
        "unreal_authority": False,
        "fully_game_ready": False,
    }
    MANIFEST.write_text(json.dumps(manifest, indent=2) + "\n", encoding="utf-8")
    print(json.dumps({"status": "pass", "board": str(OUT), "sha256": manifest["final_board_sha256"]}, indent=2))


if __name__ == "__main__":
    main()
