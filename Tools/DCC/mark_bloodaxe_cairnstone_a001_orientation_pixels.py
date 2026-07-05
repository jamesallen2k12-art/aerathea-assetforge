#!/usr/bin/env python3
"""Create A001 orientation-pixel evidence before any geometry decomposition.

This is a Blueprint evidence step only. It does not crop for geometry, move,
rotate, center, rebuild, assemble, or generate mesh data.
"""

from __future__ import annotations

import json
from pathlib import Path

from PIL import Image, ImageDraw, ImageFont


ROOT = Path(__file__).resolve().parents[2]
ASSET_NAME = "SM_GIA_BloodAxeCairnstone_A001"
SOURCE = ROOT / "docs/assets/reference/bloodaxe_cairnstone_asset/REF_GIA_BloodAxeCairnstoneAsset_A02_BlueprintTemplate.png"
OUT_DIR = ROOT / "Saved/Automation/DCC" / ASSET_NAME
RESTART_MANIFEST = OUT_DIR / f"{ASSET_NAME}_A001BlueprintRestartManifest.json"
ORIENTATION_MANIFEST = OUT_DIR / f"{ASSET_NAME}_A001OrientationPixelManifest.json"
ORIENTATION_OVERLAY = OUT_DIR / f"{ASSET_NAME}_A001OrientationPixelOverlay.png"


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


def marker(
    label: str,
    component: str,
    view: str,
    xy: tuple[int, int],
    world_meaning: str,
    color: tuple[int, int, int],
) -> dict[str, object]:
    return {
        "source_file": str(SOURCE.relative_to(ROOT)),
        "source_scanline_manifest": str(RESTART_MANIFEST.relative_to(ROOT)),
        "component_name": component,
        "source_view": view,
        "orientation_pixel_label": label,
        "pixel_coordinate": [xy[0], xy[1]],
        "world_meaning": world_meaning,
        "mark_type": "overlay_only",
        "excluded_from_texture": True,
        "excluded_from_mesh": True,
        "excluded_from_render": True,
        "excluded_from_export": True,
        "selection_method": "manual orientation-pixel pick from scan-verified source before geometry decomposition",
        "geometry_authority": False,
        "color_rgb": [color[0], color[1], color[2]],
    }


def draw_cross(draw: ImageDraw.ImageDraw, xy: tuple[int, int], color: tuple[int, int, int], label: str) -> None:
    x, y = xy
    radius = 8
    draw.line((x - radius, y, x + radius, y), fill=color, width=3)
    draw.line((x, y - radius, x, y + radius), fill=color, width=3)
    draw.ellipse((x - radius, y - radius, x + radius, y + radius), outline=color, width=2)
    draw.text((x + 10, y - 9), label, fill=color, font=font(13))


def main() -> None:
    if not RESTART_MANIFEST.exists():
        raise SystemExit(f"Missing A001 restart manifest: {RESTART_MANIFEST}")
    restart = json.loads(RESTART_MANIFEST.read_text())
    if restart.get("pixel_exact") is not True or restart.get("changed_pixels") != 0 or restart.get("max_rgb_delta") != 0:
        raise SystemExit("A001 source scanline proof is not exact; orientation marking is blocked.")

    red = (226, 38, 38)
    cyan = (0, 185, 255)
    yellow = (245, 206, 35)
    green = (46, 190, 80)
    orange = (255, 132, 28)
    magenta = (210, 70, 255)

    markers = [
        marker("FRONT_PRIMARY_CENTERLINE_TOP", "primary_object", "front", (794, 159), "front-view primary object vertical centerline near top", red),
        marker("FRONT_PRIMARY_CENTER", "primary_object", "front", (794, 330), "front-facing primary object center/orientation identity", red),
        marker("FRONT_CONTACT_CENTER", "primary_to_support_contact", "front", (794, 478), "front-view contact relationship between primary object and support object", orange),
        marker("FRONT_SUPPORT_CENTER", "support_object", "front", (794, 530), "front-view support/base centerline", yellow),
        marker("BACK_PRIMARY_CENTERLINE_TOP", "primary_object", "back", (282, 686), "back-view primary object vertical centerline near top", cyan),
        marker("BACK_PRIMARY_CENTER", "primary_object", "back", (282, 820), "back-facing primary object center/orientation identity", cyan),
        marker("BACK_CONTACT_CENTER", "primary_to_support_contact", "back", (282, 920), "back-view contact relationship between primary object and support object", orange),
        marker("BACK_SUPPORT_CENTER", "support_object", "back", (282, 960), "back-view support/base centerline", yellow),
        marker("LEFT_PRIMARY_CENTERLINE_TOP", "primary_object", "left", (780, 682), "left-view primary object vertical centerline near top", green),
        marker("LEFT_PRIMARY_CENTER", "primary_object", "left", (780, 835), "left-facing primary object center/orientation identity", green),
        marker("LEFT_CONTACT_CENTER", "primary_to_support_contact", "left", (780, 950), "left-view contact relationship between primary object and support object", orange),
        marker("LEFT_SUPPORT_CENTER", "support_object", "left", (780, 980), "left-view support/base centerline", yellow),
        marker("RIGHT_PRIMARY_CENTERLINE_TOP", "primary_object", "right", (193, 1092), "right-view primary object vertical centerline near top", magenta),
        marker("RIGHT_PRIMARY_CENTER", "primary_object", "right", (193, 1245), "right-facing primary object center/orientation identity", magenta),
        marker("RIGHT_CONTACT_CENTER", "primary_to_support_contact", "right", (193, 1362), "right-view contact relationship between primary object and support object", orange),
        marker("RIGHT_SUPPORT_CENTER", "support_object", "right", (193, 1394), "right-view support/base centerline", yellow),
        marker("TOP_SHARED_COMPONENT_CENTER", "support_object+primary_object", "top", (550, 1238), "top-view shared orientation center before any movement or centering", red),
        marker("TOP_FRONT_DIRECTION", "source_orientation", "top", (550, 1342), "top-view front direction marker to be validated in coordinate-frame step", orange),
        marker("TOP_BACK_DIRECTION", "source_orientation", "top", (550, 1130), "top-view back direction marker to be validated in coordinate-frame step", cyan),
        marker("TOP_LEFT_DIRECTION", "source_orientation", "top", (430, 1238), "top-view left direction marker to be validated in coordinate-frame step", green),
        marker("TOP_RIGHT_DIRECTION", "source_orientation", "top", (670, 1238), "top-view right direction marker to be validated in coordinate-frame step", magenta),
        marker("TOP_PRIMARY_FRONT_EDGE_RELATION", "primary_object", "top", (550, 1327), "top-view primary object front-side footprint relation before geometry masks", orange),
        marker("TOP_PRIMARY_BACK_EDGE_RELATION", "primary_object", "top", (550, 1148), "top-view primary object back-side footprint relation before geometry masks", cyan),
        marker("TOP_SUPPORT_FRONT_EDGE_RELATION", "support_object", "top", (550, 1364), "top-view support front-side footprint relation before geometry masks", yellow),
        marker("TOP_SUPPORT_BACK_EDGE_RELATION", "support_object", "top", (550, 1110), "top-view support back-side footprint relation before geometry masks", yellow),
    ]

    image = Image.open(SOURCE).convert("RGB")
    overlay = image.copy()
    draw = ImageDraw.Draw(overlay)
    draw.rectangle((10, 10, 1045, 66), fill=(255, 255, 255), outline=(30, 30, 30), width=2)
    draw.text((24, 20), "A001 orientation pixels - overlay only, not source, texture, mesh, render, or export data", fill=(20, 18, 16), font=font(20))
    for item in markers:
        color = tuple(item["color_rgb"])  # type: ignore[arg-type]
        xy = tuple(item["pixel_coordinate"])  # type: ignore[arg-type]
        draw_cross(draw, xy, color, str(item["orientation_pixel_label"]))

    manifest = {
        "asset": ASSET_NAME,
        "status": "A001 orientation pixels recorded before geometry decomposition",
        "source": str(SOURCE.relative_to(ROOT)),
        "source_scanline_manifest": str(RESTART_MANIFEST.relative_to(ROOT)),
        "orientation_overlay": str(ORIENTATION_OVERLAY.relative_to(ROOT)),
        "blueprint_steps_completed": [
            "Approved Source Intake",
            "Lossless Scanline Capture",
            "Registration Marks - source orientation pixels",
        ],
        "no_movement_before_orientation_marks": True,
        "no_geometry_crop_before_orientation_marks": True,
        "no_rotation_before_orientation_marks": True,
        "no_centering_before_orientation_marks": True,
        "no_rebuild_before_orientation_marks": True,
        "no_assembly_before_orientation_marks": True,
        "geometry_generated": False,
        "crops_generated_for_geometry": False,
        "source_pixels_modified": False,
        "markers": markers,
        "blocked_until_declared_next": [
            "pixel convention",
            "coordinate frame",
            "source decomposition crop-boundary formulas",
            "calibration formulas",
            "formula-derived measurement masks",
        ],
        "rule": "Orientation pixels are marked before crop-for-geometry, movement, rotation, centering, rebuild, or assembly. The overlay is evidence only and must not alter source pixels or generated asset data.",
    }

    OUT_DIR.mkdir(parents=True, exist_ok=True)
    overlay.save(ORIENTATION_OVERLAY)
    ORIENTATION_MANIFEST.write_text(json.dumps(manifest, indent=2) + "\n")
    print(f"A001 orientation manifest: {ORIENTATION_MANIFEST}")
    print(f"A001 orientation overlay: {ORIENTATION_OVERLAY}")
    print(f"orientation markers: {len(markers)}")


if __name__ == "__main__":
    main()
