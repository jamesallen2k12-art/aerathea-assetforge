#!/usr/bin/env python3
"""Create A001 surface-angle and edge-correspondence evidence.

This pass records source-view edge IDs, height stations, normal owners, and
corner/seam correspondence before geometry. It does not create mesh data, UVs,
texture edits, inferred fill, or assembled components.
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
CONTOUR_MANIFEST = OUT_DIR / f"{ASSET_NAME}_A001LayerContourManifest.json"
OVAL_APPROVAL_MANIFEST = OUT_DIR / f"{ASSET_NAME}_A001OvalFootprintApprovalManifest.json"
LAYERED_CONTACT_MANIFEST = OUT_DIR / f"{ASSET_NAME}_A001LayeredContactFormulaManifest.json"
LAYERED_CONTACT_APPROVAL_MANIFEST = OUT_DIR / f"{ASSET_NAME}_A001LayeredContactFormulaApprovalManifest.json"
FORMULA_AUTHORITY_MANIFEST = OUT_DIR / f"{ASSET_NAME}_A001FormulaAuthorityManifest.json"
SURFACE_MANIFEST = OUT_DIR / f"{ASSET_NAME}_A001SurfaceEdgeMarkerManifest.json"
SURFACE_OVERLAY = OUT_DIR / f"{ASSET_NAME}_A001SurfaceEdgeMarkerOverlay.png"
SURFACE_REVIEW_BOARD = OUT_DIR / f"{ASSET_NAME}_A001SurfaceEdgeMarkerReviewBoard.png"


VIEW_CROPS = {
    "front": (550, 128, 1036, 660),
    "back": (18, 664, 544, 1066),
    "left": (556, 664, 1038, 1066),
    "right": (18, 1068, 390, 1450),
    "top": (392, 1070, 724, 1450),
}


NORMAL_OWNERS = {
    "front": "-Y",
    "back": "+Y",
    "left": "-X",
    "right": "+X",
    "top": "+Z",
}


COLORS = {
    "primary_monolith": (228, 42, 42),
    "upper_socket_ring": (255, 138, 30),
    "support_base": (245, 207, 48),
    "top": (0, 185, 255),
    "station": (205, 80, 255),
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


def verify_preconditions() -> tuple[dict[str, object], dict[str, object], dict[str, object], dict[str, object], dict[str, object], dict[str, object], dict[str, object], dict[str, object]]:
    for path in (
        RESTART_MANIFEST,
        ORIENTATION_MANIFEST,
        FORMULA_MANIFEST,
        CENTER_MANIFEST,
        SNAP_MANIFEST,
        CONTOUR_MANIFEST,
        OVAL_APPROVAL_MANIFEST,
        LAYERED_CONTACT_MANIFEST,
    ):
        if not path.exists():
            raise SystemExit(f"Missing required precondition manifest: {path}")

    restart = read_json(RESTART_MANIFEST)
    orientation = read_json(ORIENTATION_MANIFEST)
    formula = read_json(FORMULA_MANIFEST)
    centers = read_json(CENTER_MANIFEST)
    snap = read_json(SNAP_MANIFEST)
    contours = read_json(CONTOUR_MANIFEST)
    oval_approval = read_json(OVAL_APPROVAL_MANIFEST)
    layered_contact = read_json(LAYERED_CONTACT_MANIFEST)

    if restart.get("pixel_exact") is not True or restart.get("changed_pixels") != 0 or restart.get("max_rgb_delta") != 0:
        raise SystemExit("A001 source scanline proof is not exact; surface-edge marker pass is blocked.")

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

    blocking_states = [
        "geometry_generated",
        "uvs_generated",
        "components_moved",
        "components_rotated",
        "components_centered",
        "components_assembled",
        "inferred_fill_generated",
    ]
    for label, manifest in (
        ("formula", formula),
        ("center", centers),
        ("snap", snap),
        ("contour", contours),
        ("oval_approval", oval_approval),
        ("layered_contact", layered_contact),
    ):
        state = manifest.get("pre_geometry_state")
        if not isinstance(state, dict):
            raise SystemExit(f"{label} manifest is missing pre_geometry_state.")
        failed = [key for key in blocking_states if state.get(key) is not False]
        if failed:
            raise SystemExit(f"{label} manifest is no longer pre-geometry clean: {failed}")

    if layered_contact.get("status") != "A001 layered contact interval formula candidate recorded before geometry":
        raise SystemExit("Layered contact formula manifest has an unexpected status.")

    return restart, orientation, formula, centers, snap, contours, oval_approval, layered_contact


def marker(
    marker_id: str,
    component: str,
    source_view: str,
    marker_type: str,
    world_meaning: str,
    *,
    pixel_coordinate: tuple[int, int] | None = None,
    pixel_line: tuple[int, int, int, int] | None = None,
    edge_id: str | None = None,
    paired_marker_ids: list[str] | None = None,
    height_station_cm: float | None = None,
    layer_contact: str | None = None,
    normal_owner: str | None = None,
    status: str = "source_evidence_marker",
) -> dict[str, object]:
    if pixel_coordinate is None and pixel_line is None:
        raise ValueError(f"{marker_id} needs a point or a line")
    if pixel_coordinate is not None and pixel_line is not None:
        raise ValueError(f"{marker_id} cannot be both point and line")

    item: dict[str, object] = {
        "source_file": str(SOURCE.relative_to(ROOT)),
        "source_sha256": sha256_file(SOURCE),
        "source_scanline_manifest": str(RESTART_MANIFEST.relative_to(ROOT)),
        "orientation_pixel_manifest": str(ORIENTATION_MANIFEST.relative_to(ROOT)),
        "measurement_formula_manifest": str(FORMULA_MANIFEST.relative_to(ROOT)),
        "pixel_count_center_manifest": str(CENTER_MANIFEST.relative_to(ROOT)),
        "snap_anchor_manifest": str(SNAP_MANIFEST.relative_to(ROOT)),
        "layer_contour_manifest": str(CONTOUR_MANIFEST.relative_to(ROOT)),
        "marker_id": marker_id,
        "component": component,
        "source_view": source_view,
        "marker_type": marker_type,
        "world_meaning": world_meaning,
        "normal_owner": normal_owner or NORMAL_OWNERS.get(source_view),
        "edge_id": edge_id,
        "paired_marker_ids": paired_marker_ids or [],
        "height_station_cm": height_station_cm,
        "layer_contact": layer_contact,
        "mark_type": "overlay_only_source_evidence",
        "excluded_from_texture": True,
        "excluded_from_mesh": True,
        "excluded_from_render": True,
        "excluded_from_export": True,
        "geometry_authority": False,
        "status": status,
    }
    if pixel_coordinate is not None:
        item["pixel_coordinate"] = [pixel_coordinate[0], pixel_coordinate[1]]
    if pixel_line is not None:
        item["pixel_line"] = [pixel_line[0], pixel_line[1], pixel_line[2], pixel_line[3]]
    return item


def build_side_markers(formula: dict[str, object], layered_contact: dict[str, object]) -> list[dict[str, object]]:
    views = formula["views"]  # type: ignore[index]
    by_view = {
        str(record["source_view"]): record
        for record in layered_contact.get("layered_contact_interval_records", [])
        if isinstance(record, dict)
    }
    markers: list[dict[str, object]] = []
    for view, record in by_view.items():
        view_up = view.upper()
        view_data = views[view]  # type: ignore[index]
        primary_box = [int(value) for value in view_data["component_boxes_px"]["primary_object"]]  # type: ignore[index]
        support_box = [int(value) for value in view_data["component_boxes_px"]["support_object"]]  # type: ignore[index]
        object_box = [int(value) for value in view_data["object_box_px"]]  # type: ignore[index]

        upper_contact = record["upper_ring_top_contact"]  # type: ignore[index]
        lower_contact = record["upper_ring_bottom_contact"]  # type: ignore[index]
        upper_line = [int(value) for value in upper_contact["pixel_line"]]  # type: ignore[index]
        lower_line = [int(value) for value in lower_contact["pixel_line"]]  # type: ignore[index]
        upper_z = float(upper_contact["z_cm"])  # type: ignore[index]
        lower_z = float(lower_contact["z_cm"])  # type: ignore[index]

        markers.append(
            marker(
                f"{view_up}_PRIMARY_TOP_STATION_220CM",
                "primary_monolith",
                view,
                "height_station",
                f"{view} primary monolith top height station",
                pixel_line=(primary_box[0], primary_box[1], primary_box[2], primary_box[1]),
                height_station_cm=220.0,
                edge_id=f"{view}_primary_top_edge",
            )
        )
        markers.append(
            marker(
                f"{view_up}_PRIMARY_BOTTOM_TO_UPPER_RING_CONTACT",
                "primary_monolith",
                view,
                "layer_contact_line",
                f"{view} primary monolith bottom contact line to upper socket ring",
                pixel_line=(upper_line[0], upper_line[1], upper_line[2], upper_line[3]),
                height_station_cm=upper_z,
                layer_contact="primary_monolith_to_upper_socket_ring",
                edge_id=f"{view}_primary_bottom_contact",
            )
        )
        markers.append(
            marker(
                f"{view_up}_UPPER_SOCKET_TOP_CONTACT",
                "upper_socket_ring",
                view,
                "layer_contact_line",
                f"{view} upper socket/ring top contact line to primary monolith",
                pixel_line=(upper_line[0], upper_line[1], upper_line[2], upper_line[3]),
                height_station_cm=upper_z,
                layer_contact="upper_socket_ring_to_primary_monolith",
                edge_id=f"{view}_upper_socket_top_contact",
            )
        )
        markers.append(
            marker(
                f"{view_up}_UPPER_SOCKET_BOTTOM_CONTACT",
                "upper_socket_ring",
                view,
                "layer_contact_line",
                f"{view} upper socket/ring bottom contact line to support base",
                pixel_line=(lower_line[0], lower_line[1], lower_line[2], lower_line[3]),
                height_station_cm=lower_z,
                layer_contact="upper_socket_ring_to_support_base",
                edge_id=f"{view}_upper_socket_bottom_contact",
            )
        )
        markers.append(
            marker(
                f"{view_up}_SUPPORT_BASE_TOP_TO_UPPER_RING_CONTACT",
                "support_base",
                view,
                "layer_contact_line",
                f"{view} support/base top contact line to upper socket ring",
                pixel_line=(lower_line[0], lower_line[1], lower_line[2], lower_line[3]),
                height_station_cm=lower_z,
                layer_contact="support_base_to_upper_socket_ring",
                edge_id=f"{view}_support_base_top_contact",
            )
        )
        markers.append(
            marker(
                f"{view_up}_SUPPORT_BASE_BOTTOM_0CM",
                "support_base",
                view,
                "height_station",
                f"{view} support/base bottom height station",
                pixel_line=(object_box[0], object_box[3], object_box[2], object_box[3]),
                height_station_cm=0.0,
                edge_id=f"{view}_support_base_bottom_edge",
            )
        )
        for side_label, top_x, bottom_x in (
            ("left", primary_box[0], upper_line[0]),
            ("right", primary_box[2], upper_line[2]),
        ):
            markers.append(
                marker(
                    f"{view_up}_PRIMARY_{side_label.upper()}_SIDE_EDGE",
                    "primary_monolith",
                    view,
                    "exterior_edge_correspondence",
                    f"{view} primary monolith {side_label} exterior edge",
                    pixel_line=(top_x, primary_box[1], bottom_x, upper_line[1]),
                    edge_id=f"{view}_primary_{side_label}_side_edge",
                    paired_marker_ids=[],
                )
            )
        for side_label, top_x, bottom_x in (
            ("left", upper_line[0], lower_line[0]),
            ("right", upper_line[2], lower_line[2]),
        ):
            markers.append(
                marker(
                    f"{view_up}_UPPER_SOCKET_{side_label.upper()}_SIDE_EDGE",
                    "upper_socket_ring",
                    view,
                    "exterior_edge_correspondence",
                    f"{view} upper socket/ring {side_label} exterior edge",
                    pixel_line=(top_x, upper_line[1], bottom_x, lower_line[1]),
                    edge_id=f"{view}_upper_socket_{side_label}_side_edge",
                    paired_marker_ids=[],
                )
            )
        for side_label, top_x, bottom_x in (
            ("left", lower_line[0], support_box[0]),
            ("right", lower_line[2], support_box[2]),
        ):
            markers.append(
                marker(
                    f"{view_up}_SUPPORT_BASE_{side_label.upper()}_OUTER_EDGE",
                    "support_base",
                    view,
                    "exterior_edge_correspondence",
                    f"{view} support/base {side_label} exterior edge",
                    pixel_line=(top_x, lower_line[1], bottom_x, object_box[3]),
                    edge_id=f"{view}_support_base_{side_label}_outer_edge",
                    paired_marker_ids=[],
                )
            )
    return markers


def build_top_markers(oval_approval: dict[str, object], contours: dict[str, object]) -> list[dict[str, object]]:
    markers: list[dict[str, object]] = []
    approved_oval_records = {}
    for record in oval_approval.get("approved_records", []):
        if isinstance(record, dict):
            approved_oval_records[str(record["stable_component_id"])] = record

    for component, role in (
        ("primary_monolith", "approved_120x90cm_measured_oval_envelope"),
        ("support_base", "approved_140x110cm_measured_oval_envelope"),
    ):
        record = approved_oval_records.get(component)
        if not record:
            continue
        left, top, right, bottom = [int(value) for value in record["top_formula_box_px"]]  # type: ignore[index]
        cx, cy = record["formula_origin_px"]  # type: ignore[index]
        color_edge = component.upper()
        markers.extend(
            [
                marker(
                    f"TOP_{color_edge}_FORMULA_ORIGIN",
                    component,
                    "top",
                    "formula_origin",
                    f"top-view {component} {role} formula origin",
                    pixel_coordinate=(round(float(cx)), round(float(cy))),
                    edge_id=f"top_{component}_formula_origin",
                    normal_owner="+Z",
                    status="approved_oval_formula_authority_marker",
                ),
                marker(
                    f"TOP_{color_edge}_FRONT_EDGE",
                    component,
                    "top",
                    "top_edge_correspondence",
                    f"top-view {component} front edge marker",
                    pixel_line=(left, bottom, right, bottom),
                    edge_id=f"top_{component}_front_edge",
                    normal_owner="+Z",
                    status="approved_oval_formula_authority_marker",
                ),
                marker(
                    f"TOP_{color_edge}_BACK_EDGE",
                    component,
                    "top",
                    "top_edge_correspondence",
                    f"top-view {component} back edge marker",
                    pixel_line=(left, top, right, top),
                    edge_id=f"top_{component}_back_edge",
                    normal_owner="+Z",
                    status="approved_oval_formula_authority_marker",
                ),
                marker(
                    f"TOP_{color_edge}_LEFT_EDGE",
                    component,
                    "top",
                    "top_edge_correspondence",
                    f"top-view {component} left edge marker",
                    pixel_line=(left, top, left, bottom),
                    edge_id=f"top_{component}_left_edge",
                    normal_owner="+Z",
                    status="approved_oval_formula_authority_marker",
                ),
                marker(
                    f"TOP_{color_edge}_RIGHT_EDGE",
                    component,
                    "top",
                    "top_edge_correspondence",
                    f"top-view {component} right edge marker",
                    pixel_line=(right, top, right, bottom),
                    edge_id=f"top_{component}_right_edge",
                    normal_owner="+Z",
                    status="approved_oval_formula_authority_marker",
                ),
            ]
        )

    diagnostic_components = {}
    for record in contours.get("reusable_source_components", []):
        if isinstance(record, dict):
            diagnostic_components[str(record["stable_component_id"])] = record

    record = diagnostic_components.get("upper_socket_ring")
    if record:
        left, top, right, bottom = record["filled_footprint_bounds_px"]  # type: ignore[index]
        cx, cy = record["pixel_count_center"]  # type: ignore[index]
        markers.extend(
            [
                marker(
                    "TOP_UPPER_SOCKET_RING_DIAGNOSTIC_CENTER",
                    "upper_socket_ring",
                    "top",
                    "diagnostic_shared_envelope_center",
                    "top-view upper socket/ring diagnostic shared envelope center; not approved independent footprint authority",
                    pixel_coordinate=(round(float(cx)), round(float(cy))),
                    edge_id="top_upper_socket_ring_diagnostic_center",
                    normal_owner="+Z",
                    status="diagnostic_only_shared_envelope_marker",
                ),
                marker(
                    "TOP_UPPER_SOCKET_RING_DIAGNOSTIC_FRONT_EDGE",
                    "upper_socket_ring",
                    "top",
                    "diagnostic_shared_envelope_line",
                    "top-view upper socket/ring diagnostic shared envelope front edge; not independent geometry authority",
                    pixel_line=(left, bottom, right, bottom),
                    edge_id="top_upper_socket_ring_diagnostic_front_edge",
                    normal_owner="+Z",
                    status="diagnostic_only_shared_envelope_marker",
                ),
                marker(
                    "TOP_UPPER_SOCKET_RING_DIAGNOSTIC_BACK_EDGE",
                    "upper_socket_ring",
                    "top",
                    "diagnostic_shared_envelope_line",
                    "top-view upper socket/ring diagnostic shared envelope back edge; not independent geometry authority",
                    pixel_line=(left, top, right, top),
                    edge_id="top_upper_socket_ring_diagnostic_back_edge",
                    normal_owner="+Z",
                    status="diagnostic_only_shared_envelope_marker",
                ),
                marker(
                    "TOP_UPPER_SOCKET_RING_DIAGNOSTIC_LEFT_EDGE",
                    "upper_socket_ring",
                    "top",
                    "diagnostic_shared_envelope_line",
                    "top-view upper socket/ring diagnostic shared envelope left edge; not independent geometry authority",
                    pixel_line=(left, top, left, bottom),
                    edge_id="top_upper_socket_ring_diagnostic_left_edge",
                    normal_owner="+Z",
                    status="diagnostic_only_shared_envelope_marker",
                ),
                marker(
                    "TOP_UPPER_SOCKET_RING_DIAGNOSTIC_RIGHT_EDGE",
                    "upper_socket_ring",
                    "top",
                    "diagnostic_shared_envelope_line",
                    "top-view upper socket/ring diagnostic shared envelope right edge; not independent geometry authority",
                    pixel_line=(right, top, right, bottom),
                    edge_id="top_upper_socket_ring_diagnostic_right_edge",
                    normal_owner="+Z",
                    status="diagnostic_only_shared_envelope_marker",
                ),
            ]
        )
    return markers


def add_pairing(markers: list[dict[str, object]]) -> None:
    pair_groups = {
        "front_primary_left_side_edge": ["front_primary_left_side_edge", "left_primary_right_side_edge"],
        "front_primary_right_side_edge": ["front_primary_right_side_edge", "right_primary_left_side_edge"],
        "back_primary_left_side_edge": ["back_primary_left_side_edge", "left_primary_left_side_edge"],
        "back_primary_right_side_edge": ["back_primary_right_side_edge", "right_primary_right_side_edge"],
        "front_upper_socket_left_side_edge": ["front_upper_socket_left_side_edge", "left_upper_socket_right_side_edge"],
        "front_upper_socket_right_side_edge": ["front_upper_socket_right_side_edge", "right_upper_socket_left_side_edge"],
        "back_upper_socket_left_side_edge": ["back_upper_socket_left_side_edge", "left_upper_socket_left_side_edge"],
        "back_upper_socket_right_side_edge": ["back_upper_socket_right_side_edge", "right_upper_socket_right_side_edge"],
        "front_support_base_left_outer_edge": ["front_support_base_left_outer_edge", "left_support_base_right_outer_edge"],
        "front_support_base_right_outer_edge": ["front_support_base_right_outer_edge", "right_support_base_left_outer_edge"],
        "back_support_base_left_outer_edge": ["back_support_base_left_outer_edge", "left_support_base_left_outer_edge"],
        "back_support_base_right_outer_edge": ["back_support_base_right_outer_edge", "right_support_base_right_outer_edge"],
    }
    by_edge = {str(item.get("edge_id")): item for item in markers}
    for members in pair_groups.values():
        present = [by_edge[edge] for edge in members if edge in by_edge]
        ids = [str(item["marker_id"]) for item in present]
        for item in present:
            item["paired_marker_ids"] = [marker_id for marker_id in ids if marker_id != item["marker_id"]]


def write_approval_and_formula_authority(
    restart: dict[str, object],
    orientation: dict[str, object],
    formula: dict[str, object],
    centers: dict[str, object],
    contours: dict[str, object],
    oval_approval: dict[str, object],
    layered_contact: dict[str, object],
) -> None:
    approved_intervals = []
    for record in layered_contact.get("layered_contact_interval_records", []):
        if not isinstance(record, dict):
            continue
        approved = dict(record)
        approved["geometry_authority_status"] = "approved_layered_contact_formula_authority"
        approved["approved_by"] = "Flamestrike"
        approved["approval_basis"] = "User approved the A001 layered contact formula review in conversation."
        approved_intervals.append(approved)

    approval_manifest = {
        "asset": ASSET_NAME,
        "status": "A001 layered contact formula approved before geometry",
        "source": str(SOURCE.relative_to(ROOT)),
        "source_sha256": sha256_file(SOURCE),
        "source_scanline_manifest": str(RESTART_MANIFEST.relative_to(ROOT)),
        "orientation_pixel_manifest": str(ORIENTATION_MANIFEST.relative_to(ROOT)),
        "measurement_formula_manifest": str(FORMULA_MANIFEST.relative_to(ROOT)),
        "pixel_count_center_manifest": str(CENTER_MANIFEST.relative_to(ROOT)),
        "oval_footprint_approval_manifest": str(OVAL_APPROVAL_MANIFEST.relative_to(ROOT)),
        "layered_contact_formula_manifest": str(LAYERED_CONTACT_MANIFEST.relative_to(ROOT)),
        "approval_source": "Flamestrike approved the A001 layered contact formula review in conversation.",
        "approved_intervals": approved_intervals,
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
    }
    LAYERED_CONTACT_APPROVAL_MANIFEST.write_text(json.dumps(approval_manifest, indent=2) + "\n")

    authority_manifest = {
        "asset": ASSET_NAME,
        "status": "A001 promoted formula authority recorded before geometry",
        "source": str(SOURCE.relative_to(ROOT)),
        "source_sha256": sha256_file(SOURCE),
        "source_scanline_manifest": str(RESTART_MANIFEST.relative_to(ROOT)),
        "orientation_pixel_manifest": str(ORIENTATION_MANIFEST.relative_to(ROOT)),
        "base_formula_archive": str(FORMULA_MANIFEST.relative_to(ROOT)),
        "oval_footprint_approval_manifest": str(OVAL_APPROVAL_MANIFEST.relative_to(ROOT)),
        "layered_contact_approval_manifest": str(LAYERED_CONTACT_APPROVAL_MANIFEST.relative_to(ROOT)),
        "approved_geometry_formula_authorities": {
            "primary_monolith_top_footprint": "approved 120cm x 90cm measured oval envelope from oval footprint approval",
            "support_base_top_footprint": "approved 140cm x 110cm measured oval envelope from oval footprint approval",
            "upper_socket_ring_contact_interval": "approved per-view layered contact interval; no global average",
            "old_35cm_support_height": "calibration/disagreement evidence only for visible contacts in this pass",
            "upper_socket_top_footprint": "diagnostic shared/occluded top envelope only until separate footprint formula is approved",
        },
        "approved_contact_intervals": approved_intervals,
        "source_proof": {
            "restart_pixel_exact": restart.get("pixel_exact"),
            "restart_changed_pixels": restart.get("changed_pixels"),
            "restart_max_rgb_delta": restart.get("max_rgb_delta"),
            "orientation_status": orientation.get("status"),
            "formula_status": formula.get("status"),
            "center_status": centers.get("status"),
            "contour_status": contours.get("status"),
            "oval_approval_status": oval_approval.get("status"),
            "layered_contact_status": layered_contact.get("status"),
        },
        "pre_geometry_state": approval_manifest["pre_geometry_state"],
        "blocked_until_declared_next": [
            "surface-angle and edge-correspondence marker approval",
            "pre-geometry hard audit",
            "geometry construction plan",
        ],
    }
    FORMULA_AUTHORITY_MANIFEST.write_text(json.dumps(authority_manifest, indent=2) + "\n")


def draw_marker(draw: ImageDraw.ImageDraw, item: dict[str, object], show_label: bool = True) -> None:
    component = str(item["component"])
    color = COLORS.get(component, COLORS["station"])
    label = str(item["marker_id"])
    if "pixel_line" in item:
        x1, y1, x2, y2 = item["pixel_line"]  # type: ignore[misc]
        draw.line((x1, y1, x2, y2), fill=color, width=3)
        if show_label:
            draw.text((x1 + 4, y1 - 14), label, fill=color, font=font(10))
    else:
        x, y = item["pixel_coordinate"]  # type: ignore[misc]
        radius = 8
        draw.line((x - radius, y, x + radius, y), fill=color, width=3)
        draw.line((x, y - radius, x, y + radius), fill=color, width=3)
        draw.ellipse((x - radius, y - radius, x + radius, y + radius), outline=color, width=2)
        if show_label:
            draw.text((x + 10, y - 8), label, fill=color, font=font(10))


def create_overlay(source: Image.Image, markers: list[dict[str, object]]) -> None:
    overlay = source.copy()
    draw = ImageDraw.Draw(overlay)
    draw.rectangle((10, 10, 1045, 88), fill=(255, 255, 255), outline=(30, 30, 30), width=2)
    draw.text((24, 18), "A001 surface-angle and edge-correspondence markers - evidence only", fill=(20, 18, 16), font=font(20))
    draw.text((24, 50), "Normal owners, height stations, contacts, and edge IDs recorded before geometry.", fill=(80, 42, 92), font=font(15))
    for item in markers:
        draw_marker(draw, item)
    overlay.save(SURFACE_OVERLAY)


def create_review_board(source: Image.Image, markers: list[dict[str, object]]) -> None:
    board = Image.new("RGB", (1860, 1320), (245, 243, 238))
    draw = ImageDraw.Draw(board)
    draw.text((40, 28), "A001 Surface Edge Marker Review", fill=(24, 21, 18), font=font(30))
    draw.text((40, 74), "Normal owners, height stations, contact lines, and edge IDs. Evidence only; no mesh generated.", fill=(55, 48, 42), font=font(18))

    for index, (view, crop) in enumerate(VIEW_CROPS.items()):
        col = index % 3
        row = index // 3
        x = 40 + col * 590
        y = 130 + row * 500
        panel = source.crop(crop).copy()
        panel_draw = ImageDraw.Draw(panel)
        offset_x, offset_y = crop[0], crop[1]
        for item in markers:
            if item["source_view"] != view:
                continue
            shifted = dict(item)
            if "pixel_line" in shifted:
                x1, y1, x2, y2 = shifted["pixel_line"]  # type: ignore[misc]
                shifted["pixel_line"] = [x1 - offset_x, y1 - offset_y, x2 - offset_x, y2 - offset_y]
            if "pixel_coordinate" in shifted:
                px, py = shifted["pixel_coordinate"]  # type: ignore[misc]
                shifted["pixel_coordinate"] = [px - offset_x, py - offset_y]
            draw_marker(panel_draw, shifted, show_label=False)
        panel.thumbnail((540, 430), RESAMPLE_LANCZOS)
        board.paste(panel, (x, y))
        draw.rectangle((x, y, x + panel.width, y + panel.height), outline=(70, 64, 56), width=2)
        draw.text((x, y + panel.height + 10), f"{view.title()} normal {NORMAL_OWNERS[view]}", fill=(32, 28, 24), font=font(20))

    x, y = 1180, 650
    draw.rectangle((x, y, 1780, 1190), fill=(255, 255, 255), outline=(75, 68, 62), width=2)
    draw.text((x + 18, y + 18), "Validation Notes", fill=(24, 21, 18), font=font(22))
    notes = [
        f"markers recorded: {len(markers)}",
        "front/back/left/right/top normal owners are explicit",
        "height stations and contact lines are source-pixel evidence",
        "paired edge IDs prevent side swaps during reassembly",
        "no mesh, UVs, movement, centering, rotation, or assembly",
    ]
    for i, note in enumerate(notes):
        draw.text((x + 18, y + 58 + i * 38), f"- {note}", fill=(48, 42, 36), font=font(17))

    board.save(SURFACE_REVIEW_BOARD)


def build_manifest(
    restart: dict[str, object],
    orientation: dict[str, object],
    formula: dict[str, object],
    centers: dict[str, object],
    snap: dict[str, object],
    contours: dict[str, object],
    oval_approval: dict[str, object],
    layered_contact: dict[str, object],
    markers: list[dict[str, object]],
) -> dict[str, object]:
    return {
        "asset": ASSET_NAME,
        "status": "A001 surface-angle and edge-correspondence markers recorded before geometry",
        "source": str(SOURCE.relative_to(ROOT)),
        "source_sha256": sha256_file(SOURCE),
        "source_scanline_manifest": str(RESTART_MANIFEST.relative_to(ROOT)),
        "orientation_pixel_manifest": str(ORIENTATION_MANIFEST.relative_to(ROOT)),
        "measurement_formula_manifest": str(FORMULA_MANIFEST.relative_to(ROOT)),
        "pixel_count_center_manifest": str(CENTER_MANIFEST.relative_to(ROOT)),
        "snap_anchor_manifest": str(SNAP_MANIFEST.relative_to(ROOT)),
        "layer_contour_manifest": str(CONTOUR_MANIFEST.relative_to(ROOT)),
        "oval_footprint_approval_manifest": str(OVAL_APPROVAL_MANIFEST.relative_to(ROOT)),
        "layered_contact_formula_manifest": str(LAYERED_CONTACT_MANIFEST.relative_to(ROOT)),
        "layered_contact_approval_manifest": str(LAYERED_CONTACT_APPROVAL_MANIFEST.relative_to(ROOT)),
        "formula_authority_manifest": str(FORMULA_AUTHORITY_MANIFEST.relative_to(ROOT)),
        "surface_marker_overlay": str(SURFACE_OVERLAY.relative_to(ROOT)),
        "surface_marker_review_board": str(SURFACE_REVIEW_BOARD.relative_to(ROOT)),
        "source_proof": {
            "restart_pixel_exact": restart.get("pixel_exact"),
            "restart_changed_pixels": restart.get("changed_pixels"),
            "restart_max_rgb_delta": restart.get("max_rgb_delta"),
            "orientation_mark_count": len(orientation.get("markers", [])) if isinstance(orientation.get("markers"), list) else None,
            "formula_status": formula.get("status"),
            "center_status": centers.get("status"),
            "snap_status": snap.get("status"),
            "contour_status": contours.get("status"),
            "oval_approval_status": oval_approval.get("status"),
            "layered_contact_status": layered_contact.get("status"),
        },
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
        "surface_angle_and_edge_correspondence": {
            "normal_owners": NORMAL_OWNERS,
            "marker_count": len(markers),
            "edge_pair_count": sum(1 for item in markers if item["paired_marker_ids"]),
            "approved_layered_contact_formula_used": True,
            "old_single_35cm_contact_used": False,
            "rule": "Geometry may not be assembled until exterior edges, approved layer height stations, contact lines, and normal owners are recorded.",
        },
        "markers": markers,
        "geometry_use_status": "candidate_pending_surface_marker_review; blocked_until_pre_geometry_audit",
        "blocked_until_declared_next": [
            "surface marker board review",
            "pre-geometry hard audit",
        ],
    }


def main() -> None:
    restart, orientation, formula, centers, snap, contours, oval_approval, layered_contact = verify_preconditions()
    source = Image.open(SOURCE).convert("RGB")
    write_approval_and_formula_authority(restart, orientation, formula, centers, contours, oval_approval, layered_contact)
    markers = build_side_markers(formula, layered_contact) + build_top_markers(oval_approval, contours)
    add_pairing(markers)
    create_overlay(source, markers)
    create_review_board(source, markers)
    manifest = build_manifest(restart, orientation, formula, centers, snap, contours, oval_approval, layered_contact, markers)
    SURFACE_MANIFEST.write_text(json.dumps(manifest, indent=2) + "\n")
    print(f"A001 layered contact approval manifest: {LAYERED_CONTACT_APPROVAL_MANIFEST}")
    print(f"A001 formula authority manifest: {FORMULA_AUTHORITY_MANIFEST}")
    print(f"A001 surface marker manifest: {SURFACE_MANIFEST}")
    print(f"A001 surface marker overlay: {SURFACE_OVERLAY}")
    print(f"A001 surface marker review board: {SURFACE_REVIEW_BOARD}")
    print(f"surface markers: {len(markers)}")
    print(f"paired edge markers: {sum(1 for item in markers if item['paired_marker_ids'])}")
    print("geometry_generated=False components_moved=False components_assembled=False")


if __name__ == "__main__":
    main()
