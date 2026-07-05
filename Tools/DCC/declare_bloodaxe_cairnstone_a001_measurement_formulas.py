#!/usr/bin/env python3
"""Declare A001 pixel-perfect measurement formulas and evidence masks.

This Blueprint step creates formula evidence only. It does not generate mesh,
UVs, assembled components, contact fixes, inferred fill, or DCC geometry.
"""

from __future__ import annotations

import json
import hashlib
from pathlib import Path

from PIL import Image, ImageDraw, ImageFont


ROOT = Path(__file__).resolve().parents[2]
ASSET_NAME = "SM_GIA_BloodAxeCairnstone_A001"
SOURCE = ROOT / "docs/assets/reference/bloodaxe_cairnstone_asset/REF_GIA_BloodAxeCairnstoneAsset_A02_BlueprintTemplate.png"
OUT_DIR = ROOT / "Saved/Automation/DCC" / ASSET_NAME
MASK_DIR = OUT_DIR / "FreshEvidence" / "FormulaMeasurementMasks"
RESTART_MANIFEST = OUT_DIR / f"{ASSET_NAME}_A001BlueprintRestartManifest.json"
ORIENTATION_MANIFEST = OUT_DIR / f"{ASSET_NAME}_A001OrientationPixelManifest.json"
FORMULA_MANIFEST = OUT_DIR / f"{ASSET_NAME}_A001MeasurementFormulaManifest.json"
FORMULA_OVERLAY = OUT_DIR / f"{ASSET_NAME}_A001MeasurementFormulaOverlay.png"
FORMULA_MASK_BOARD = OUT_DIR / f"{ASSET_NAME}_A001FormulaMaskReviewBoard.png"


SOURCE_DIMS_CM = {
    "overall_height": 220.0,
    "support_width": 140.0,
    "support_depth": 110.0,
    "support_height": 35.0,
    "primary_width": 120.0,
    "primary_depth": 90.0,
    "primary_height": 185.0,
}


VIEW_BOXES = {
    "front": {
        "source_view": "front",
        "component_axis": "width",
        "support_span_cm": SOURCE_DIMS_CM["support_width"],
        "primary_span_cm": SOURCE_DIMS_CM["primary_width"],
        "object_box_px": (648, 156, 946, 558),
        "centerline_x_px": 794,
        "front_direction": "-Y",
    },
    "back": {
        "source_view": "back",
        "component_axis": "width",
        "support_span_cm": SOURCE_DIMS_CM["support_width"],
        "primary_span_cm": SOURCE_DIMS_CM["primary_width"],
        "object_box_px": (142, 684, 422, 990),
        "centerline_x_px": 282,
        "front_direction": "+Y",
    },
    "left": {
        "source_view": "left",
        "component_axis": "depth",
        "support_span_cm": SOURCE_DIMS_CM["support_depth"],
        "primary_span_cm": SOURCE_DIMS_CM["primary_depth"],
        "object_box_px": (674, 680, 888, 1002),
        "centerline_x_px": 780,
        "front_direction": "-X",
    },
    "right": {
        "source_view": "right",
        "component_axis": "depth",
        "support_span_cm": SOURCE_DIMS_CM["support_depth"],
        "primary_span_cm": SOURCE_DIMS_CM["primary_depth"],
        "object_box_px": (70, 1090, 314, 1418),
        "centerline_x_px": 193,
        "front_direction": "+X",
    },
    "top": {
        "source_view": "top",
        "component_axis": "footprint",
        "support_span_cm": [SOURCE_DIMS_CM["support_width"], SOURCE_DIMS_CM["support_depth"]],
        "primary_span_cm": [SOURCE_DIMS_CM["primary_width"], SOURCE_DIMS_CM["primary_depth"]],
        "object_box_px": (414, 1108, 685, 1367),
        "center_px": (550, 1238),
        "front_direction": "down_in_source_image",
    },
}


def ensure_dir(path: Path) -> None:
    path.mkdir(parents=True, exist_ok=True)


def sha256_file(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest()


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


def verify_preconditions() -> tuple[dict[str, object], dict[str, object]]:
    if not RESTART_MANIFEST.exists():
        raise SystemExit(f"Missing restart manifest: {RESTART_MANIFEST}")
    if not ORIENTATION_MANIFEST.exists():
        raise SystemExit(f"Missing orientation manifest: {ORIENTATION_MANIFEST}")
    restart = json.loads(RESTART_MANIFEST.read_text())
    orientation = json.loads(ORIENTATION_MANIFEST.read_text())
    if restart.get("pixel_exact") is not True or restart.get("changed_pixels") != 0 or restart.get("max_rgb_delta") != 0:
        raise SystemExit("A001 source scanline proof is not exact; formula declaration is blocked.")
    required_orientation_flags = [
        "no_movement_before_orientation_marks",
        "no_geometry_crop_before_orientation_marks",
        "no_rotation_before_orientation_marks",
        "no_centering_before_orientation_marks",
        "no_rebuild_before_orientation_marks",
        "no_assembly_before_orientation_marks",
    ]
    missing = [key for key in required_orientation_flags if orientation.get(key) is not True]
    if missing:
        raise SystemExit(f"Orientation manifest failed required flags: {missing}")
    return restart, orientation


def box_size(box: tuple[int, int, int, int]) -> tuple[int, int]:
    return box[2] - box[0], box[3] - box[1]


def side_component_boxes(spec: dict[str, object]) -> dict[str, tuple[int, int, int, int]]:
    left, top, right, bottom = spec["object_box_px"]  # type: ignore[misc]
    center_x = int(spec["centerline_x_px"])
    width_px = right - left
    height_px = bottom - top
    primary_width_px = width_px * float(spec["primary_span_cm"]) / float(spec["support_span_cm"])
    primary_left = round(center_x - primary_width_px * 0.5)
    primary_right = round(center_x + primary_width_px * 0.5)
    support_height_px = height_px * SOURCE_DIMS_CM["support_height"] / SOURCE_DIMS_CM["overall_height"]
    support_top = round(bottom - support_height_px)
    return {
        "support_object": (left, support_top, right, bottom),
        "primary_object": (primary_left, top, primary_right, support_top),
        "full_object": (left, top, right, bottom),
    }


def top_component_boxes(spec: dict[str, object]) -> dict[str, tuple[int, int, int, int]]:
    left, top, right, bottom = spec["object_box_px"]  # type: ignore[misc]
    center_x, center_y = spec["center_px"]  # type: ignore[misc]
    width_px = right - left
    depth_px = bottom - top
    primary_width_px = width_px * SOURCE_DIMS_CM["primary_width"] / SOURCE_DIMS_CM["support_width"]
    primary_depth_px = depth_px * SOURCE_DIMS_CM["primary_depth"] / SOURCE_DIMS_CM["support_depth"]
    primary = (
        round(center_x - primary_width_px * 0.5),
        round(center_y - primary_depth_px * 0.5),
        round(center_x + primary_width_px * 0.5),
        round(center_y + primary_depth_px * 0.5),
    )
    return {
        "support_object": (left, top, right, bottom),
        "primary_object": primary,
        "full_object": (left, top, right, bottom),
    }


def make_mask(size: tuple[int, int], boxes: list[tuple[int, int, int, int]]) -> Image.Image:
    mask = Image.new("L", size, 0)
    draw = ImageDraw.Draw(mask)
    for box in boxes:
        draw.rectangle((box[0], box[1], box[2] - 1, box[3] - 1), fill=255)
    return mask


def write_masks(source_size: tuple[int, int], component_boxes: dict[str, dict[str, tuple[int, int, int, int]]]) -> dict[str, dict[str, str]]:
    ensure_dir(MASK_DIR)
    paths: dict[str, dict[str, str]] = {}
    for view_name, boxes in component_boxes.items():
        paths[view_name] = {}
        for component_name in ("full_object", "support_object", "primary_object"):
            mask = make_mask(source_size, [boxes[component_name]])
            path = MASK_DIR / f"{ASSET_NAME}_{view_name.title()}_{component_name.title().replace('_', '')}_FormulaMask.png"
            mask.save(path)
            paths[view_name][component_name] = str(path.relative_to(ROOT))
        if view_name == "top":
            support = boxes["support_object"]
            primary = boxes["primary_object"]
            visible_support = Image.new("L", source_size, 0)
            draw = ImageDraw.Draw(visible_support)
            draw.rectangle((support[0], support[1], support[2] - 1, support[3] - 1), fill=255)
            draw.rectangle((primary[0], primary[1], primary[2] - 1, primary[3] - 1), fill=0)
            path = MASK_DIR / f"{ASSET_NAME}_Top_SupportVisibleMinusPrimary_FormulaMask.png"
            visible_support.save(path)
            paths[view_name]["support_visible_minus_primary"] = str(path.relative_to(ROOT))
    return paths


def draw_box(draw: ImageDraw.ImageDraw, box: tuple[int, int, int, int], color: tuple[int, int, int], label: str, width: int = 3) -> None:
    draw.rectangle((box[0], box[1], box[2], box[3]), outline=color, width=width)
    draw.text((box[0] + 4, box[1] + 4), label, fill=color, font=font(14))


def draw_centerline(draw: ImageDraw.ImageDraw, box: tuple[int, int, int, int], x: int, color: tuple[int, int, int]) -> None:
    draw.line((x, box[1], x, box[3]), fill=color, width=2)


def create_overlay(source: Image.Image, component_boxes: dict[str, dict[str, tuple[int, int, int, int]]]) -> None:
    overlay = source.copy()
    draw = ImageDraw.Draw(overlay)
    title_font = font(20)
    draw.rectangle((10, 10, 1045, 70), fill=(255, 255, 255), outline=(30, 30, 30), width=2)
    draw.text((24, 22), "A001 formula-derived measurement boxes - evidence only, no geometry generated", fill=(20, 18, 16), font=title_font)
    colors = {
        "full_object": (35, 130, 255),
        "support_object": (245, 206, 35),
        "primary_object": (230, 45, 45),
    }
    for view_name, boxes in component_boxes.items():
        draw_box(draw, boxes["full_object"], colors["full_object"], f"{view_name} full measurement frame", 2)
        draw_box(draw, boxes["support_object"], colors["support_object"], f"{view_name} support", 3)
        draw_box(draw, boxes["primary_object"], colors["primary_object"], f"{view_name} primary", 3)
        spec = VIEW_BOXES[view_name]
        if view_name == "top":
            cx, cy = spec["center_px"]  # type: ignore[misc]
            draw.line((cx - 18, cy, cx + 18, cy), fill=(255, 120, 20), width=3)
            draw.line((cx, cy - 18, cx, cy + 18), fill=(255, 120, 20), width=3)
        else:
            draw_centerline(draw, boxes["full_object"], int(spec["centerline_x_px"]), (255, 120, 20))
    overlay.save(FORMULA_OVERLAY)


def create_mask_board(source: Image.Image, mask_paths: dict[str, dict[str, str]]) -> None:
    board = Image.new("RGB", (1800, 1320), (245, 243, 238))
    draw = ImageDraw.Draw(board)
    draw.text((40, 30), "A001 Formula Measurement Masks", fill=(24, 21, 18), font=font(30))
    draw.text((40, 76), "Formula-owned measurement evidence only. Diagnostic texture masks are not geometry authority.", fill=(55, 48, 42), font=font(18))
    cells = [
        ("front primary", "front", "primary_object"),
        ("front support", "front", "support_object"),
        ("back primary", "back", "primary_object"),
        ("back support", "back", "support_object"),
        ("left primary", "left", "primary_object"),
        ("left support", "left", "support_object"),
        ("right primary", "right", "primary_object"),
        ("right support", "right", "support_object"),
        ("top primary", "top", "primary_object"),
        ("top support visible", "top", "support_visible_minus_primary"),
    ]
    for index, (label, view, key) in enumerate(cells):
        col = index % 5
        row = index // 5
        x = 40 + col * 345
        y = 135 + row * 545
        mask = Image.open(ROOT / mask_paths[view][key]).convert("L")
        preview = Image.new("RGB", source.size, (20, 20, 20))
        preview.paste((255, 255, 255), mask=mask)
        preview.thumbnail((305, 455), Image.NEAREST)
        board.paste(preview, (x, y))
        draw.rectangle((x, y, x + 305, y + 455), outline=(70, 64, 56), width=2)
        draw.text((x, y + 470), label, fill=(32, 28, 24), font=font(18))
    board.save(FORMULA_MASK_BOARD)


def build_manifest(
    restart: dict[str, object],
    orientation: dict[str, object],
    component_boxes: dict[str, dict[str, tuple[int, int, int, int]]],
    mask_paths: dict[str, dict[str, str]],
) -> dict[str, object]:
    views: dict[str, object] = {}
    for view_name, spec in VIEW_BOXES.items():
        boxes = component_boxes[view_name]
        full_w, full_h = box_size(boxes["full_object"])
        item: dict[str, object] = {
            "source_view": view_name,
            "object_box_px": list(boxes["full_object"]),
            "object_box_formula": "source-landmark edge pixels in full scan coordinates, recorded before crop-for-geometry",
            "component_boxes_px": {name: list(box) for name, box in boxes.items()},
            "formula_mask_paths": mask_paths[view_name],
            "crop_boundary_authority": "declared source-landmark pixels from scan-verified full source, not threshold cleanup",
            "diagnostic_masks_geometry_authority": False,
        }
        if view_name == "top":
            cm_w, cm_d = spec["support_span_cm"]  # type: ignore[misc]
            item["cm_per_pixel"] = [cm_w / full_w, cm_d / full_h]
            item["component_split_formulas"] = {
                "primary_width_px": "support_width_px * 120cm / 140cm, centered on top shared component center",
                "primary_depth_px": "support_depth_px * 90cm / 110cm, centered on top shared component center",
                "support_visible_mask": "support_object_formula_box minus primary_object_formula_box",
            }
        else:
            item["cm_per_pixel"] = [float(spec["support_span_cm"]) / full_w, SOURCE_DIMS_CM["overall_height"] / full_h]
            item["component_split_formulas"] = {
                "primary_width_or_depth_px": "full_object_width_px * primary_component_cm / support_component_cm, centered on source orientation centerline",
                "support_height_px": "full_object_height_px * 35cm / 220cm",
                "primary_height_px": "full_object_height_px * 185cm / 220cm",
            }
        views[view_name] = item
    formula_archive = {
        "source_image_path": str(SOURCE.relative_to(ROOT)),
        "source_sha256": sha256_file(SOURCE),
        "source_scanline_manifest": str(RESTART_MANIFEST.relative_to(ROOT)),
        "orientation_pixel_manifest": str(ORIENTATION_MANIFEST.relative_to(ROOT)),
        "pixel_convention": "half-open rectangles [left, top, right, bottom); integer orientation marks identify pixel centers; dimensions use edge-to-edge spans",
        "coordinate_frame": "centimeter-authored, +Z up, -Y front, +Y back, +X right, -X left; origin remains uncommitted until top shared center formula is validated",
        "crop_boundary_formula": {
            view_name: "full-scan source landmark box recorded as [left, top, right, bottom); span_px = right-left or bottom-top; no threshold cleanup owns crop geometry"
            for view_name in VIEW_BOXES
        },
        "component_split_formula": {
            "side_primary_span": "primary_span_px = full_object_span_px * primary_component_cm / support_component_cm, centered on recorded orientation centerline pixel",
            "side_support_height": "support_height_px = full_object_height_px * 35cm / 220cm from bottom edge upward",
            "side_primary_height": "primary_height_px = full_object_height_px * 185cm / 220cm above support",
            "top_primary_width": "primary_width_px = support_width_px * 120cm / 140cm, centered on top shared component center",
            "top_primary_depth": "primary_depth_px = support_depth_px * 90cm / 110cm, centered on top shared component center",
            "top_support_visible": "support_visible_mask = support_formula_box - primary_formula_box",
        },
        "calibration_formula": {
            "front_back_x": "cm_per_px_x = 140cm / full_object_width_px",
            "left_right_x": "cm_per_px_x = 110cm / full_object_width_px",
            "side_z": "cm_per_px_z = 220cm / full_object_height_px",
            "top_x": "cm_per_px_x = 140cm / support_width_px",
            "top_y": "cm_per_px_y = 110cm / support_depth_px",
        },
        "center_origin_formula": {
            "side_centerline": "recorded orientation centerline pixel remains the local center reference for side formula boxes",
            "top_center": "recorded TOP_SHARED_COMPONENT_CENTER pixel is the future assembly-origin candidate; no centering is performed in this step",
        },
        "yaw_pitch_roll_formula": {
            "default": "yaw=0, pitch=0, roll=0 until source orientation formula proves otherwise",
            "top_direction_validation": "top front/back/left/right direction markers define orientation before assembly",
        },
        "contact_position_formula": {
            "support_primary_z_contact": "primary_bottom_z_cm = support_height_cm = 35cm",
            "visible_contact_policy": "gap_cm must be 0 unless an approved rule declares otherwise",
            "xy_contact_policy": "primary/support relationship is derived from top shared center and formula component boxes",
        },
        "exterior_seam_position_formula": {
            "side_edges": "visible exterior side seams must use matching formula-derived edge positions from owned source views",
            "top_edges": "top visible support surface excludes the primary formula box",
            "no_contact_bridge": "contact, annulus, hidden, or interior edges cannot be used as exterior seam fixes",
        },
        "formula_derived_measurement_mask_paths": mask_paths,
        "diagnostic_masks_do_not_own_geometry": True,
        "blocked_methods": [
            "threshold cleanup as geometry authority",
            "largest-blob cleanup as geometry authority",
            "averaged measurements",
            "old generator behavior",
            "copied prior asset-specific generator",
            "hidden center drops",
            "annulus/contact bridge tricks",
            "stretch patches",
            "detached cover-up shells",
            "old renders or meshes as source",
            "non-Blueprint methods",
        ],
    }
    return {
        "asset": ASSET_NAME,
        "status": "A001 measurement formulas declared before geometry",
        "source": str(SOURCE.relative_to(ROOT)),
        "source_sha256": sha256_file(SOURCE),
        "source_scanline_manifest": str(RESTART_MANIFEST.relative_to(ROOT)),
        "orientation_pixel_manifest": str(ORIENTATION_MANIFEST.relative_to(ROOT)),
        "formula_overlay": str(FORMULA_OVERLAY.relative_to(ROOT)),
        "formula_mask_review_board": str(FORMULA_MASK_BOARD.relative_to(ROOT)),
        "formula_archive": formula_archive,
        "source_dimensions_cm": SOURCE_DIMS_CM,
        "pixel_convention": {
            "source_origin": "top-left pixel of full scan image",
            "pixel_coordinate_meaning": "integer coordinates identify pixel centers for point marks",
            "box_convention": "half-open rectangles [left, top, right, bottom); right and bottom are exclusive",
            "span_formula": "span_px = right - left or bottom - top",
            "measurement_style": "edge-to-edge pixel span for dimension calibration; centerline pixels are recorded separately",
        },
        "coordinate_frame": {
            "world_units": "centimeters",
            "unreal_scale": "1 Unreal unit = 1 cm",
            "world_up": "+Z",
            "front": "-Y",
            "back": "+Y",
            "right": "+X",
            "left": "-X",
            "top": "+Z",
            "origin_policy": "top-view shared component center becomes assembly origin only after formula validation; no centering has occurred in this stage",
            "component_yaw_pitch_roll_policy": "0/0/0 until a source orientation formula proves otherwise",
        },
        "formula_authority": {
            "geometry_defining_masks": "formula-derived measurement masks only",
            "texture_material_masks": "diagnostic or texture extraction only; not geometry authority",
            "threshold_cleanup_used_for_geometry": False,
            "largest_blob_used_for_geometry": False,
            "old_generator_behavior_used": False,
            "non_blueprint_methods_used": False,
        },
        "views": views,
        "pre_geometry_state": {
            "geometry_generated": False,
            "uvs_generated": False,
            "components_moved": False,
            "components_rotated": False,
            "components_centered": False,
            "components_assembled": False,
            "inferred_fill_generated": False,
        },
        "completed_blueprint_steps": [
            "Approved Source Intake",
            "Lossless Scanline Capture",
            "Registration Marks - source orientation pixels",
            "Pixel Convention",
            "Coordinate Frame",
            "Calibration",
            "Measurement Contract formula basis",
        ],
        "blocked_until_declared_next": [
            "source decomposition crop outputs from formula boxes",
            "component measurement contracts for each visible feature",
            "disagreement policy per edge/profile",
            "geometry construction plan",
        ],
    }


def main() -> None:
    restart, orientation = verify_preconditions()
    source = Image.open(SOURCE).convert("RGB")
    component_boxes: dict[str, dict[str, tuple[int, int, int, int]]] = {}
    for view_name, spec in VIEW_BOXES.items():
        if view_name == "top":
            component_boxes[view_name] = top_component_boxes(spec)
        else:
            component_boxes[view_name] = side_component_boxes(spec)
    mask_paths = write_masks(source.size, component_boxes)
    create_overlay(source, component_boxes)
    create_mask_board(source, mask_paths)
    manifest = build_manifest(restart, orientation, component_boxes, mask_paths)
    FORMULA_MANIFEST.write_text(json.dumps(manifest, indent=2) + "\n")
    print(f"A001 formula manifest: {FORMULA_MANIFEST}")
    print(f"A001 formula overlay: {FORMULA_OVERLAY}")
    print(f"A001 formula mask board: {FORMULA_MASK_BOARD}")
    print("geometry_generated=False components_moved=False components_assembled=False")


if __name__ == "__main__":
    main()
