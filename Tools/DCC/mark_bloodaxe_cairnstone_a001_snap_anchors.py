#!/usr/bin/env python3
"""Create A001 source-derived snap-anchor evidence.

This Blueprint step records attachment points, contact lines, and perimeter
anchors before any component reconstruction or assembly. It does not generate
mesh data, UVs, texture edits, inferred fill, or moved components.
"""

from __future__ import annotations

import hashlib
import json
from pathlib import Path

from PIL import Image, ImageDraw, ImageFont


ROOT = Path(__file__).resolve().parents[2]
ASSET_NAME = "SM_GIA_BloodAxeCairnstone_A001"
SOURCE = ROOT / "docs/assets/reference/bloodaxe_cairnstone_asset/REF_GIA_BloodAxeCairnstoneAsset_A02_BlueprintTemplate.png"
OUT_DIR = ROOT / "Saved/Automation/DCC" / ASSET_NAME
RESTART_MANIFEST = OUT_DIR / f"{ASSET_NAME}_A001BlueprintRestartManifest.json"
ORIENTATION_MANIFEST = OUT_DIR / f"{ASSET_NAME}_A001OrientationPixelManifest.json"
FORMULA_MANIFEST = OUT_DIR / f"{ASSET_NAME}_A001MeasurementFormulaManifest.json"
CENTER_MANIFEST = OUT_DIR / f"{ASSET_NAME}_A001PixelCountCenterManifest.json"
SNAP_MANIFEST = OUT_DIR / f"{ASSET_NAME}_A001SnapAnchorManifest.json"
SNAP_OVERLAY = OUT_DIR / f"{ASSET_NAME}_A001SnapAnchorOverlay.png"
SNAP_REVIEW_BOARD = OUT_DIR / f"{ASSET_NAME}_A001SnapAnchorReviewBoard.png"


VIEW_CROPS = {
    "front": (550, 128, 1036, 660),
    "back": (18, 664, 544, 1066),
    "left": (556, 664, 1038, 1066),
    "right": (18, 1068, 390, 1450),
    "top": (392, 1070, 724, 1450),
}


COLORS = {
    "primary_monolith": (228, 42, 42),
    "upper_socket_ring": (255, 138, 30),
    "support_base": (245, 207, 48),
    "top_perimeter": (0, 185, 255),
    "candidate_blocked": (205, 80, 255),
}


RESAMPLE_LANCZOS = getattr(Image, "Resampling", Image).LANCZOS


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


def sha256_file(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest()


def read_json(path: Path) -> dict[str, object]:
    return json.loads(path.read_text())


def verify_preconditions() -> tuple[dict[str, object], dict[str, object], dict[str, object], dict[str, object]]:
    for path in (RESTART_MANIFEST, ORIENTATION_MANIFEST, FORMULA_MANIFEST, CENTER_MANIFEST):
        if not path.exists():
            raise SystemExit(f"Missing required precondition manifest: {path}")

    restart = read_json(RESTART_MANIFEST)
    orientation = read_json(ORIENTATION_MANIFEST)
    formula = read_json(FORMULA_MANIFEST)
    centers = read_json(CENTER_MANIFEST)

    if restart.get("pixel_exact") is not True or restart.get("changed_pixels") != 0 or restart.get("max_rgb_delta") != 0:
        raise SystemExit("A001 source scanline proof is not exact; snap-anchor marking is blocked.")

    required_orientation_flags = [
        "no_movement_before_orientation_marks",
        "no_geometry_crop_before_orientation_marks",
        "no_rotation_before_orientation_marks",
        "no_centering_before_orientation_marks",
        "no_rebuild_before_orientation_marks",
        "no_assembly_before_orientation_marks",
    ]
    missing_flags = [key for key in required_orientation_flags if orientation.get(key) is not True]
    if missing_flags:
        raise SystemExit(f"Orientation manifest failed required flags: {missing_flags}")

    pre_geometry_state = formula.get("pre_geometry_state")
    if not isinstance(pre_geometry_state, dict):
        raise SystemExit("Formula manifest is missing pre_geometry_state.")
    blocking_states = [
        "geometry_generated",
        "uvs_generated",
        "components_moved",
        "components_rotated",
        "components_centered",
        "components_assembled",
        "inferred_fill_generated",
    ]
    failed = [key for key in blocking_states if pre_geometry_state.get(key) is not False]
    if failed:
        raise SystemExit(f"Formula manifest is no longer pre-geometry clean: {failed}")

    center_states = centers.get("pre_geometry_state")
    if not isinstance(center_states, dict):
        raise SystemExit("Center manifest is missing pre_geometry_state.")
    center_failed = [key for key in blocking_states if center_states.get(key) is not False]
    if center_failed:
        raise SystemExit(f"Center manifest is no longer pre-geometry clean: {center_failed}")

    required_center_components = {"primary_monolith", "upper_socket_ring", "support_base"}
    found_center_components: set[str] = set()
    for item in centers.get("component_centers", []):
        if isinstance(item, dict):
            found_center_components.add(str(item.get("stable_component_id")))
    missing_center_components = sorted(required_center_components - found_center_components)
    if missing_center_components:
        raise SystemExit(f"Center manifest missing required component centers: {missing_center_components}")

    return restart, orientation, formula, centers


def center_points(centers: dict[str, object]) -> dict[str, tuple[int, int]]:
    points: dict[str, tuple[int, int]] = {}
    for item in centers.get("component_centers", []):
        if not isinstance(item, dict):
            continue
        stable_id = str(item.get("stable_component_id"))
        if stable_id not in {"primary_monolith", "upper_socket_ring", "support_base"}:
            continue
        rounded = item.get("rounded_pixel_count_center")
        if not isinstance(rounded, list) or len(rounded) != 2:
            raise SystemExit(f"Component center for {stable_id} missing rounded_pixel_count_center")
        points[stable_id] = (int(rounded[0]), int(rounded[1]))
    return points


def base_anchor(
    anchor_id: str,
    component: str,
    view: str,
    snap_role: str,
    paired_anchor_id: str,
    world_meaning: str,
    *,
    pixel_coordinate: tuple[int, int] | None = None,
    pixel_line: tuple[int, int, int, int] | None = None,
    controls: tuple[str, ...] = ("position", "orientation", "contact"),
    status: str = "source_evidence_candidate",
    color_key: str | None = None,
    notes: str | None = None,
) -> dict[str, object]:
    if pixel_coordinate is None and pixel_line is None:
        raise ValueError(f"{anchor_id} needs a point or line.")
    if pixel_coordinate is not None and pixel_line is not None:
        raise ValueError(f"{anchor_id} cannot be both point and line.")

    item: dict[str, object] = {
        "source_file": str(SOURCE.relative_to(ROOT)),
        "source_sha256": sha256_file(SOURCE),
        "source_scanline_manifest": str(RESTART_MANIFEST.relative_to(ROOT)),
        "orientation_pixel_manifest": str(ORIENTATION_MANIFEST.relative_to(ROOT)),
        "measurement_formula_manifest": str(FORMULA_MANIFEST.relative_to(ROOT)),
        "pixel_count_center_manifest": str(CENTER_MANIFEST.relative_to(ROOT)),
        "anchor_id": anchor_id,
        "physical_layer_component": component,
        "source_view": view,
        "snap_role": snap_role,
        "paired_anchor_id": paired_anchor_id,
        "world_space_meaning": world_meaning,
        "allowed_translation_tolerance_px": 0,
        "allowed_translation_tolerance_cm": 0.0,
        "allowed_yaw_tolerance_deg": 0.0,
        "allowed_pitch_tolerance_deg": 0.0,
        "allowed_roll_tolerance_deg": 0.0,
        "controls": list(controls),
        "mark_type": "overlay_only_source_evidence",
        "hidden_non_shipping_candidate": True,
        "source_authored_visible_detail": False,
        "excluded_from_texture": True,
        "excluded_from_mesh": True,
        "excluded_from_render": True,
        "excluded_from_export": True,
        "selection_method": "manual source-pixel registration from the scan-verified source template before component reconstruction",
        "geometry_authority": False,
        "status": status,
        "blocked_methods": [
            "visual fit after reconstruction",
            "old renders",
            "old meshes",
            "old generator data",
            "bounding-box center anchors for non-rectangular components",
            "using one component anchor to deform another component",
        ],
        "color_rgb": list(COLORS[color_key or component]),
    }
    if pixel_coordinate is not None:
        item["pixel_coordinate"] = [pixel_coordinate[0], pixel_coordinate[1]]
    if pixel_line is not None:
        item["pixel_line"] = [pixel_line[0], pixel_line[1], pixel_line[2], pixel_line[3]]
    if notes:
        item["notes"] = notes
    return item


def line_pair(
    view: str,
    prefix: str,
    component_a: str,
    component_b: str,
    line: tuple[int, int, int, int],
    snap_role: str,
    meaning_a: str,
    meaning_b: str,
) -> list[dict[str, object]]:
    a_id = f"{prefix}_{component_a.upper()}_TO_{component_b.upper()}"
    b_id = f"{prefix}_{component_b.upper()}_TO_{component_a.upper()}"
    return [
        base_anchor(
            a_id,
            component_a,
            view,
            snap_role,
            b_id,
            meaning_a,
            pixel_line=line,
            color_key=component_a,
        ),
        base_anchor(
            b_id,
            component_b,
            view,
            snap_role,
            a_id,
            meaning_b,
            pixel_line=line,
            color_key=component_b,
        ),
    ]


def point_pair(
    view: str,
    prefix: str,
    component_a: str,
    component_b: str,
    point: tuple[int, int],
    snap_role: str,
    meaning_a: str,
    meaning_b: str,
    *,
    status: str = "source_evidence_candidate",
) -> list[dict[str, object]]:
    a_id = f"{prefix}_{component_a.upper()}_TO_{component_b.upper()}"
    b_id = f"{prefix}_{component_b.upper()}_TO_{component_a.upper()}"
    return [
        base_anchor(
            a_id,
            component_a,
            view,
            snap_role,
            b_id,
            meaning_a,
            pixel_coordinate=point,
            color_key="top_perimeter",
            status=status,
        ),
        base_anchor(
            b_id,
            component_b,
            view,
            snap_role,
            a_id,
            meaning_b,
            pixel_coordinate=point,
            color_key="upper_socket_ring",
            status=status,
        ),
    ]


def build_anchors(centers: dict[str, object]) -> list[dict[str, object]]:
    anchors: list[dict[str, object]] = []
    centers_by_component = center_points(centers)

    side_specs = {
        "front": {
            "primary_to_upper": (690, 478, 900, 478),
            "upper_to_lower": (650, 516, 944, 516),
        },
        "back": {
            "primary_to_upper": (170, 920, 394, 920),
            "upper_to_lower": (144, 952, 420, 952),
        },
        "left": {
            "primary_to_upper": (714, 950, 846, 950),
            "upper_to_lower": (676, 974, 886, 974),
        },
        "right": {
            "primary_to_upper": (114, 1362, 274, 1362),
            "upper_to_lower": (72, 1388, 312, 1388),
        },
    }
    for view, specs in side_specs.items():
        upper_prefix = f"{view.upper()}_PRIMARY_BOTTOM_CONTACT"
        lower_prefix = f"{view.upper()}_UPPER_RING_BOTTOM_CONTACT"
        anchors.extend(
            line_pair(
                view,
                upper_prefix,
                "primary_monolith",
                "upper_socket_ring",
                specs["primary_to_upper"],
                "bottom/top contact line",
                f"{view} primary object's lower contact edge in source pixels",
                f"{view} upper socket/ring top contact edge that receives the primary object",
            )
        )
        anchors.extend(
            line_pair(
                view,
                lower_prefix,
                "upper_socket_ring",
                "support_base",
                specs["upper_to_lower"],
                "bottom/top contact line",
                f"{view} upper socket/ring lower contact edge in source pixels",
                f"{view} lower base ring upper contact edge that receives the upper socket/ring",
            )
        )

    top_points = {
        "TOP_PRIMARY_BACK_PERIMETER": (550, 1148, "back perimeter"),
        "TOP_PRIMARY_FRONT_PERIMETER": (550, 1327, "front perimeter"),
        "TOP_PRIMARY_LEFT_PERIMETER": (446, 1238, "left perimeter"),
        "TOP_PRIMARY_RIGHT_PERIMETER": (654, 1238, "right perimeter"),
    }
    for prefix, (x, y, role) in top_points.items():
        anchors.extend(
            point_pair(
                "top",
                prefix,
                "primary_monolith",
                "upper_socket_ring",
                (x, y),
                role,
                f"top-view primary object {role} footprint point",
                f"top-view upper socket/ring inner {role} receiving point",
                status="source_evidence_candidate_blocked_until_pixel_count_contour_validation",
            )
        )

    support_points = {
        "TOP_UPPER_RING_BACK_OUTER_PERIMETER": (550, 1110, "back outer perimeter"),
        "TOP_UPPER_RING_FRONT_OUTER_PERIMETER": (550, 1364, "front outer perimeter"),
        "TOP_UPPER_RING_LEFT_OUTER_PERIMETER": (420, 1238, "left outer perimeter"),
        "TOP_UPPER_RING_RIGHT_OUTER_PERIMETER": (680, 1238, "right outer perimeter"),
    }
    for prefix, (x, y, role) in support_points.items():
        anchors.extend(
            point_pair(
                "top",
                prefix,
                "upper_socket_ring",
                "support_base",
                (x, y),
                role,
                f"top-view upper socket/ring {role} footprint point",
                f"top-view lower base ring matching {role} footprint point",
                status="source_evidence_candidate_blocked_until_pixel_count_contour_validation",
            )
        )

    center_candidates = [
        ("TOP_PRIMARY_CENTER_PIXEL_COUNT", "primary_monolith", centers_by_component["primary_monolith"]),
        ("TOP_UPPER_RING_CENTER_PIXEL_COUNT", "upper_socket_ring", centers_by_component["upper_socket_ring"]),
        ("TOP_SUPPORT_BASE_CENTER_PIXEL_COUNT", "support_base", centers_by_component["support_base"]),
    ]
    for anchor_id, component, point in center_candidates:
        anchors.append(
            base_anchor(
                anchor_id,
                component,
                "top",
                "pixel-count footprint center",
                "UNPAIRED_COMPONENT_CENTER_EVIDENCE",
                "top-view seed-connected filled-footprint pixel-count center from center manifest",
                pixel_coordinate=point,
                controls=("orientation",),
                status="source_evidence_center_from_pixel_count_manifest",
                color_key="candidate_blocked",
                notes="This center comes from the pixel-count center manifest. It is evidence for later alignment, not mesh geometry.",
            )
        )

    return anchors


def draw_anchor(draw: ImageDraw.ImageDraw, anchor: dict[str, object]) -> None:
    color = tuple(anchor["color_rgb"])  # type: ignore[arg-type]
    label = str(anchor["anchor_id"])
    if "pixel_line" in anchor:
        x1, y1, x2, y2 = anchor["pixel_line"]  # type: ignore[misc]
        draw.line((x1, y1, x2, y2), fill=color, width=4)
        draw.ellipse((x1 - 5, y1 - 5, x1 + 5, y1 + 5), fill=color)
        draw.ellipse((x2 - 5, y2 - 5, x2 + 5, y2 + 5), fill=color)
        draw.text((x1 + 4, y1 - 18), label, fill=color, font=font(11))
    else:
        x, y = anchor["pixel_coordinate"]  # type: ignore[misc]
        radius = 9
        draw.line((x - radius, y, x + radius, y), fill=color, width=3)
        draw.line((x, y - radius, x, y + radius), fill=color, width=3)
        draw.ellipse((x - radius, y - radius, x + radius, y + radius), outline=color, width=2)
        draw.text((x + 9, y - 10), label, fill=color, font=font(11))


def create_overlay(source: Image.Image, anchors: list[dict[str, object]]) -> None:
    overlay = source.copy()
    draw = ImageDraw.Draw(overlay)
    draw.rectangle((10, 10, 1045, 82), fill=(255, 255, 255), outline=(30, 30, 30), width=2)
    draw.text((24, 18), "A001 source-derived snap anchors - overlay only, no geometry or assembly", fill=(20, 18, 16), font=font(20))
    draw.text((24, 48), "Component centers come from the A001 pixel-count center manifest. Evidence only; no mesh generated.", fill=(80, 42, 92), font=font(15))
    for anchor in anchors:
        draw_anchor(draw, anchor)
    overlay.save(SNAP_OVERLAY)


def create_review_board(source: Image.Image, anchors: list[dict[str, object]]) -> None:
    board = Image.new("RGB", (1760, 1220), (245, 243, 238))
    draw = ImageDraw.Draw(board)
    draw.text((40, 28), "A001 Snap Anchor Review Board", fill=(24, 21, 18), font=font(30))
    draw.text((40, 74), "Paired attachment lines/points from scan-verified source. Evidence only until pixel-count contours pass.", fill=(55, 48, 42), font=font(18))

    for index, (view, crop) in enumerate(VIEW_CROPS.items()):
        col = index % 3
        row = index // 3
        x = 40 + col * 560
        y = 130 + row * 500
        panel = source.crop(crop).copy()
        panel_draw = ImageDraw.Draw(panel)
        offset_x, offset_y = crop[0], crop[1]
        for anchor in anchors:
            if anchor["source_view"] != view:
                continue
            shifted = dict(anchor)
            if "pixel_line" in shifted:
                x1, y1, x2, y2 = shifted["pixel_line"]  # type: ignore[misc]
                shifted["pixel_line"] = [x1 - offset_x, y1 - offset_y, x2 - offset_x, y2 - offset_y]
            if "pixel_coordinate" in shifted:
                px, py = shifted["pixel_coordinate"]  # type: ignore[misc]
                shifted["pixel_coordinate"] = [px - offset_x, py - offset_y]
            draw_anchor(panel_draw, shifted)
        panel.thumbnail((520, 430), RESAMPLE_LANCZOS)
        board.paste(panel, (x, y))
        draw.rectangle((x, y, x + panel.width, y + panel.height), outline=(70, 64, 56), width=2)
        draw.text((x, y + panel.height + 10), view.title(), fill=(32, 28, 24), font=font(20))

    legend_x, legend_y = 1160, 640
    draw.rectangle((legend_x, legend_y, 1700, 1128), fill=(255, 255, 255), outline=(75, 68, 62), width=2)
    draw.text((legend_x + 18, legend_y + 18), "Rules Enforced", fill=(24, 21, 18), font=font(22))
    rules = [
        "No mesh generated.",
        "No components moved, centered, rotated, or assembled.",
        "Paired IDs are required before reconstruction.",
        "Bounding-box centers cannot drive oval/ring alignment.",
        "Component centers come from the pixel-count center manifest.",
        "Any anchor disagreement stops the build; no averaging.",
    ]
    for i, rule in enumerate(rules):
        draw.text((legend_x + 18, legend_y + 58 + i * 42), f"- {rule}", fill=(48, 42, 36), font=font(17))

    board.save(SNAP_REVIEW_BOARD)


def paired_anchor_errors(anchors: list[dict[str, object]]) -> list[str]:
    by_id = {str(anchor["anchor_id"]): anchor for anchor in anchors}
    errors: list[str] = []
    for anchor in anchors:
        paired_id = str(anchor["paired_anchor_id"])
        if paired_id.startswith("UNPAIRED_"):
            continue
        pair = by_id.get(paired_id)
        if pair is None:
            errors.append(f"{anchor['anchor_id']} missing paired anchor {paired_id}")
            continue
        if pair.get("paired_anchor_id") != anchor["anchor_id"]:
            errors.append(f"{anchor['anchor_id']} pair {paired_id} does not point back")
        if anchor.get("source_view") != pair.get("source_view"):
            errors.append(f"{anchor['anchor_id']} pair {paired_id} source view mismatch")
        if anchor.get("pixel_line") != pair.get("pixel_line") and anchor.get("pixel_coordinate") != pair.get("pixel_coordinate"):
            errors.append(f"{anchor['anchor_id']} pair {paired_id} pixel evidence mismatch")
    return errors


def build_manifest(
    restart: dict[str, object],
    orientation: dict[str, object],
    formula: dict[str, object],
    centers: dict[str, object],
    anchors: list[dict[str, object]],
    pair_errors: list[str],
) -> dict[str, object]:
    paired = [a for a in anchors if not str(a["paired_anchor_id"]).startswith("UNPAIRED_")]
    blocked = [a for a in anchors if str(a["status"]).startswith("source_evidence_candidate_blocked") or str(a["status"]).startswith("blocked_")]
    return {
        "asset": ASSET_NAME,
        "status": "A001 source-derived snap anchors recorded before geometry reconstruction",
        "source": str(SOURCE.relative_to(ROOT)),
        "source_sha256": sha256_file(SOURCE),
        "source_scanline_manifest": str(RESTART_MANIFEST.relative_to(ROOT)),
        "orientation_pixel_manifest": str(ORIENTATION_MANIFEST.relative_to(ROOT)),
        "measurement_formula_manifest": str(FORMULA_MANIFEST.relative_to(ROOT)),
        "pixel_count_center_manifest": str(CENTER_MANIFEST.relative_to(ROOT)),
        "snap_anchor_overlay": str(SNAP_OVERLAY.relative_to(ROOT)),
        "snap_anchor_review_board": str(SNAP_REVIEW_BOARD.relative_to(ROOT)),
        "blueprint_steps_completed": [
            "Approved Source Intake",
            "Lossless Scanline Capture",
            "Registration Marks - source orientation pixels",
            "Source-Derived Snap Anchor Rule - evidence layer",
        ],
        "pre_geometry_state": {
            "geometry_generated": False,
            "uvs_generated": False,
            "components_moved": False,
            "components_rotated": False,
            "components_centered": False,
            "components_assembled": False,
            "inferred_fill_generated": False,
            "source_pixels_modified": False,
        },
        "source_proof": {
            "restart_pixel_exact": restart.get("pixel_exact"),
            "restart_changed_pixels": restart.get("changed_pixels"),
            "restart_max_rgb_delta": restart.get("max_rgb_delta"),
            "orientation_mark_count": len(orientation.get("markers", [])) if isinstance(orientation.get("markers"), list) else None,
            "formula_status": formula.get("status"),
            "center_status": centers.get("status"),
        },
        "component_center_policy": {
            "center_manifest": str(CENTER_MANIFEST.relative_to(ROOT)),
            "center_type": "seed-connected filled-footprint pixel-count centers",
            "old_shared_center_used": False,
            "bounding_box_centers_used": False,
            "raw_visible_color_density_centers_used": False,
        },
        "snap_anchor_counts": {
            "total": len(anchors),
            "paired": len(paired),
            "unpaired_review_only": len(anchors) - len(paired),
            "blocked_review_markers": len(blocked),
        },
        "paired_anchor_validation": {
            "all_pairs_resolve": not pair_errors,
            "errors": pair_errors,
            "rule": "Paired anchors must point to each other, use the same source view, and share the same source pixel evidence before assembly.",
        },
        "top_oval_ring_geometry_status": "pixel_count_centers_exist; contour/perimeter validation still required before mesh generation",
        "geometry_use_status": "blocked_for_mesh_generation_until_layer_contours_surface_angles_edge_correspondence_and_contact_interfaces_pass",
        "snap_anchors": anchors,
        "blocked_until_declared_next": [
            "oval/ring/irregular top footprint contours from source pixels",
            "layer separation manifest with clean measured level/contact lines",
            "surface-angle and edge-correspondence marker manifest for every exterior seam",
            "formula archive update replacing rectangular top support ownership with contour ownership",
        ],
        "hard_rules": [
            "Do not use the old shared center for final alignment.",
            "Do not use rectangular bounding-box centers for oval, ring, irregular, broken, organic, or tapered components.",
            "Do not move reconstructed parts by eye to make snap anchors fit.",
            "Do not average conflicting anchors.",
            "If anchors disagree, stop and remeasure the source pixels.",
        ],
    }


def main() -> None:
    restart, orientation, formula, centers = verify_preconditions()
    source = Image.open(SOURCE).convert("RGB")
    anchors = build_anchors(centers)
    pair_errors = paired_anchor_errors(anchors)
    create_overlay(source, anchors)
    create_review_board(source, anchors)
    manifest = build_manifest(restart, orientation, formula, centers, anchors, pair_errors)
    SNAP_MANIFEST.write_text(json.dumps(manifest, indent=2) + "\n")
    print(f"A001 snap anchor manifest: {SNAP_MANIFEST}")
    print(f"A001 snap anchor overlay: {SNAP_OVERLAY}")
    print(f"A001 snap anchor review board: {SNAP_REVIEW_BOARD}")
    print(f"snap anchors: {len(anchors)}")
    print(f"paired anchor errors: {len(pair_errors)}")
    print("geometry_generated=False components_moved=False components_assembled=False")


if __name__ == "__main__":
    main()
