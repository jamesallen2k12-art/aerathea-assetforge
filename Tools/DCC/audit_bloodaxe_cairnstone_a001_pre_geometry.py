#!/usr/bin/env python3
"""Run the A001 pre-geometry hard audit.

This audit records Flamestrike approval of the surface-edge marker board and
checks that the promoted A001 measurement evidence is ready for a geometry
construction plan. It is intentionally fail-closed and still generates no mesh,
UVs, textures, movement, rotation, centering, or assembly.
"""

from __future__ import annotations

import hashlib
import json
from pathlib import Path
from typing import Any

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
RADIAL_DECISION_MANIFEST = OUT_DIR / f"{ASSET_NAME}_A001RadialTraceReviewDecision.json"
OVAL_APPROVAL_MANIFEST = OUT_DIR / f"{ASSET_NAME}_A001OvalFootprintApprovalManifest.json"
LAYERED_CONTACT_APPROVAL_MANIFEST = OUT_DIR / f"{ASSET_NAME}_A001LayeredContactFormulaApprovalManifest.json"
FORMULA_AUTHORITY_MANIFEST = OUT_DIR / f"{ASSET_NAME}_A001FormulaAuthorityManifest.json"
SURFACE_MARKER_MANIFEST = OUT_DIR / f"{ASSET_NAME}_A001SurfaceEdgeMarkerManifest.json"

SURFACE_MARKER_APPROVAL_MANIFEST = OUT_DIR / f"{ASSET_NAME}_A001SurfaceEdgeMarkerApprovalManifest.json"
PREGEOMETRY_AUDIT_MANIFEST = OUT_DIR / f"{ASSET_NAME}_A001PreGeometryHardAuditManifest.json"
PREGEOMETRY_AUDIT_BOARD = OUT_DIR / f"{ASSET_NAME}_A001PreGeometryHardAuditReviewBoard.png"


REQUIRED_PRE_GEOMETRY_FALSE_KEYS = (
    "geometry_generated",
    "uvs_generated",
    "components_moved",
    "components_rotated",
    "components_centered",
    "components_assembled",
    "inferred_fill_generated",
)


def font(size: int) -> ImageFont.ImageFont:
    for candidate in (
        "/usr/share/fonts/truetype/dejavu/DejaVuSans.ttf",
        "/usr/share/fonts/truetype/liberation2/LiberationSans-Regular.ttf",
    ):
        try:
            return ImageFont.truetype(candidate, size)
        except OSError:
            continue
    return ImageFont.load_default()


def sha256_file(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest()


def read_json(path: Path) -> dict[str, Any]:
    return json.loads(path.read_text())


def add_check(checks: list[dict[str, Any]], name: str, passed: bool, detail: str, severity: str = "blocker") -> None:
    checks.append(
        {
            "name": name,
            "passed": bool(passed),
            "severity": severity,
            "detail": detail,
        }
    )


def pre_geometry_clean(manifest: dict[str, Any]) -> tuple[bool, list[str]]:
    state = manifest.get("pre_geometry_state")
    if not isinstance(state, dict):
        return False, ["missing_pre_geometry_state"]
    failed = [key for key in REQUIRED_PRE_GEOMETRY_FALSE_KEYS if state.get(key) is not False]
    if state.get("source_pixels_modified") not in (False, None):
        failed.append("source_pixels_modified")
    return not failed, failed


def load_required_manifests() -> dict[str, dict[str, Any]]:
    paths = {
        "restart": RESTART_MANIFEST,
        "orientation": ORIENTATION_MANIFEST,
        "formula": FORMULA_MANIFEST,
        "centers": CENTER_MANIFEST,
        "snap": SNAP_MANIFEST,
        "contours": CONTOUR_MANIFEST,
        "radial_decision": RADIAL_DECISION_MANIFEST,
        "oval_approval": OVAL_APPROVAL_MANIFEST,
        "layered_contact_approval": LAYERED_CONTACT_APPROVAL_MANIFEST,
        "formula_authority": FORMULA_AUTHORITY_MANIFEST,
        "surface_markers": SURFACE_MARKER_MANIFEST,
    }
    missing = [str(path) for path in paths.values() if not path.exists()]
    if missing:
        raise SystemExit("Missing required audit manifest(s):\n" + "\n".join(missing))
    return {name: read_json(path) for name, path in paths.items()}


def write_surface_marker_approval(manifests: dict[str, dict[str, Any]]) -> None:
    markers = manifests["surface_markers"]
    approval = {
        "asset": ASSET_NAME,
        "status": "A001 surface-edge marker board approved before geometry",
        "source": str(SOURCE.relative_to(ROOT)),
        "source_sha256": sha256_file(SOURCE),
        "surface_edge_marker_manifest": str(SURFACE_MARKER_MANIFEST.relative_to(ROOT)),
        "approval_source": "Flamestrike approved the A001 Surface Edge Marker Review in conversation.",
        "approved_marker_count": markers.get("surface_angle_and_edge_correspondence", {}).get("marker_count"),
        "approved_edge_pair_count": markers.get("surface_angle_and_edge_correspondence", {}).get("edge_pair_count"),
        "approved_layered_contact_formula_used": markers.get("surface_angle_and_edge_correspondence", {}).get("approved_layered_contact_formula_used"),
        "old_single_35cm_contact_used": markers.get("surface_angle_and_edge_correspondence", {}).get("old_single_35cm_contact_used"),
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
    SURFACE_MARKER_APPROVAL_MANIFEST.write_text(json.dumps(approval, indent=2) + "\n")


def run_audit(manifests: dict[str, dict[str, Any]]) -> list[dict[str, Any]]:
    checks: list[dict[str, Any]] = []

    restart = manifests["restart"]
    add_check(
        checks,
        "source_scanline_exact",
        restart.get("pixel_exact") is True and restart.get("changed_pixels") == 0 and restart.get("max_rgb_delta") == 0,
        "source scanline proof must be exact with changed_pixels=0 and max_rgb_delta=0",
    )

    orientation = manifests["orientation"]
    required_orientation_flags = [
        "no_movement_before_orientation_marks",
        "no_geometry_crop_before_orientation_marks",
        "no_rotation_before_orientation_marks",
        "no_centering_before_orientation_marks",
        "no_rebuild_before_orientation_marks",
        "no_assembly_before_orientation_marks",
    ]
    missing_orientation = [key for key in required_orientation_flags if orientation.get(key) is not True]
    add_check(
        checks,
        "orientation_marked_before_all_transform_work",
        not missing_orientation,
        f"missing/false orientation flags: {missing_orientation}",
    )

    for name, manifest in manifests.items():
        if name in {"restart", "orientation"}:
            continue
        clean, failed = pre_geometry_clean(manifest)
        add_check(checks, f"{name}_pre_geometry_clean", clean, f"pre-geometry failed keys: {failed}")

    formula = manifests["formula"]
    archive = formula.get("formula_archive", {})
    required_archive_keys = [
        "source_image_path",
        "pixel_convention",
        "coordinate_frame",
        "crop_boundary_formula",
        "component_split_formula",
        "calibration_formula",
        "center_origin_formula",
        "yaw_pitch_roll_formula",
        "contact_position_formula",
        "exterior_seam_position_formula",
        "formula_derived_measurement_mask_paths",
        "blocked_methods",
    ]
    missing_archive = [key for key in required_archive_keys if key not in archive]
    add_check(checks, "formula_archive_complete", not missing_archive, f"missing formula archive keys: {missing_archive}")

    formula_authority = manifests["formula_authority"]
    authorities = formula_authority.get("approved_geometry_formula_authorities", {})
    add_check(
        checks,
        "approved_oval_footprints_promoted",
        "120cm x 90cm" in str(authorities.get("primary_monolith_top_footprint", ""))
        and "140cm x 110cm" in str(authorities.get("support_base_top_footprint", "")),
        "primary/support top footprints must reference approved 120x90 and 140x110 formula authority",
    )
    add_check(
        checks,
        "upper_socket_top_is_not_false_independent_authority",
        "diagnostic" in str(authorities.get("upper_socket_top_footprint", "")).lower(),
        "upper socket top footprint must remain diagnostic/shared/occluded until a separate footprint formula is approved",
        severity="warning",
    )
    add_check(
        checks,
        "old_35cm_contact_demoted",
        "calibration" in str(authorities.get("old_35cm_support_height", "")).lower()
        and "approved per-view layered contact interval" in str(authorities.get("upper_socket_ring_contact_interval", "")),
        "old 35cm contact must be calibration/disagreement evidence; layered interval is contact authority",
    )

    radial = manifests["radial_decision"]
    add_check(
        checks,
        "radial_trace_demoted",
        radial.get("status") == "prior radial trace rejected as footprint-shape authority; retained as diagnostic evidence",
        "prior circular-looking radial pass must not be geometry authority",
    )

    oval = manifests["oval_approval"]
    approved_records = oval.get("approved_records", [])
    approved_ids = {record.get("stable_component_id") for record in approved_records if isinstance(record, dict)}
    add_check(
        checks,
        "oval_approval_records_present",
        {"primary_monolith", "support_base"}.issubset(approved_ids),
        f"approved oval record ids: {sorted(str(item) for item in approved_ids)}",
    )

    layered = manifests["layered_contact_approval"]
    intervals = layered.get("approved_intervals", [])
    interval_views = {record.get("source_view") for record in intervals if isinstance(record, dict)}
    no_average = all(record.get("no_average_used") is True for record in intervals if isinstance(record, dict))
    add_check(
        checks,
        "layered_contact_approval_records_present",
        {"front", "back", "left", "right"}.issubset(interval_views) and no_average,
        f"interval views={sorted(str(item) for item in interval_views)}, no_average={no_average}",
    )

    centers = manifests["centers"]
    center_ids = {record.get("stable_component_id") for record in centers.get("component_centers", []) if isinstance(record, dict)}
    add_check(
        checks,
        "pixel_count_centers_exist",
        {"primary_monolith", "upper_socket_ring", "support_base", "assembled_top_footprint_review_only"}.issubset(center_ids),
        f"center ids={sorted(str(item) for item in center_ids)}",
    )

    snap = manifests["snap"]
    snap_anchors = [item for item in snap.get("snap_anchors", []) if isinstance(item, dict)]
    zero_tol = all(
        anchor.get("allowed_translation_tolerance_px") == 0
        and anchor.get("allowed_yaw_tolerance_deg") == 0
        and anchor.get("allowed_pitch_tolerance_deg") == 0
        and anchor.get("allowed_roll_tolerance_deg") == 0
        for anchor in snap_anchors
    )
    add_check(
        checks,
        "snap_anchors_zero_tolerance",
        len(snap_anchors) >= 20 and zero_tol,
        f"snap anchors={len(snap_anchors)}, zero_tol={zero_tol}",
    )

    surface = manifests["surface_markers"]
    surface_summary = surface.get("surface_angle_and_edge_correspondence", {})
    normal_owners = surface_summary.get("normal_owners", {})
    markers = surface.get("markers", [])
    contact_markers = [
        item
        for item in markers
        if isinstance(item, dict) and item.get("marker_type") == "layer_contact_line"
    ]
    add_check(
        checks,
        "surface_markers_approved_formula_used",
        surface_summary.get("approved_layered_contact_formula_used") is True
        and surface_summary.get("old_single_35cm_contact_used") is False
        and surface_summary.get("marker_count", 0) >= 63
        and surface_summary.get("edge_pair_count", 0) >= 24,
        f"surface summary={surface_summary}",
    )
    add_check(
        checks,
        "normal_owners_declared",
        normal_owners == {"front": "-Y", "back": "+Y", "left": "-X", "right": "+X", "top": "+Z"},
        f"normal owners={normal_owners}",
    )
    add_check(
        checks,
        "layer_contact_markers_present",
        len(contact_markers) >= 16,
        f"layer contact marker count={len(contact_markers)}",
    )

    contours = manifests["contours"]
    reusable = [item for item in contours.get("reusable_source_components", []) if isinstance(item, dict)]
    add_check(
        checks,
        "reusable_source_components_recorded",
        len(reusable) >= 3,
        f"reusable component records={len(reusable)}",
    )

    return checks


def create_review_board(checks: list[dict[str, Any]]) -> None:
    blockers_failed = [check for check in checks if not check["passed"] and check["severity"] == "blocker"]
    warnings_failed = [check for check in checks if not check["passed"] and check["severity"] == "warning"]
    gate_status = "PASSED" if not blockers_failed else "BLOCKED"
    gate_color = (32, 128, 70) if gate_status == "PASSED" else (170, 35, 35)

    board = Image.new("RGB", (1900, 1500), (245, 243, 238))
    draw = ImageDraw.Draw(board)
    draw.text((40, 28), "A001 Pre-Geometry Hard Audit", fill=(24, 21, 18), font=font(30))
    draw.text((40, 74), "Checks promoted formula authority before any mesh construction. Evidence only; no geometry generated.", fill=(55, 48, 42), font=font(18))
    draw.text((40, 118), f"Gate Status: {gate_status}", fill=gate_color, font=font(28))

    x, y = 40, 180
    row_h = 38
    draw.rectangle((x, y, 1810, 1335), fill=(255, 255, 255), outline=(75, 68, 62), width=2)
    draw.text((x + 18, y + 16), "Audit Checks", fill=(24, 21, 18), font=font(22))

    start_y = y + 58
    for index, check in enumerate(checks):
        row_y = start_y + index * row_h
        if row_y > 1290:
            break
        passed = check["passed"]
        severity = check["severity"]
        color = (32, 128, 70) if passed else ((170, 35, 35) if severity == "blocker" else (175, 108, 25))
        status = "PASS" if passed else ("FAIL" if severity == "blocker" else "WARN")
        draw.text((x + 18, row_y), status, fill=color, font=font(16))
        draw.text((x + 108, row_y), check["name"], fill=(42, 36, 30), font=font(16))
        detail = str(check["detail"])
        if len(detail) > 112:
            detail = detail[:109] + "..."
        draw.text((x + 620, row_y), detail, fill=(70, 62, 54), font=font(14))

    summary_y = 1360
    draw.text((40, summary_y), "Next Step", fill=(24, 21, 18), font=font(22))
    if blockers_failed:
        text = "Fix failed blocker checks before geometry construction planning."
    else:
        text = "Proceed to a geometry construction plan. This is not approval to render or export a mesh yet."
    draw.text((40, summary_y + 36), text, fill=(48, 42, 36), font=font(18))
    if warnings_failed:
        draw.text((40, summary_y + 68), f"Warnings retained: {len(warnings_failed)}. They must remain tagged in the geometry plan.", fill=(145, 86, 18), font=font(16))

    board.save(PREGEOMETRY_AUDIT_BOARD)


def build_manifest(manifests: dict[str, dict[str, Any]], checks: list[dict[str, Any]]) -> dict[str, Any]:
    blockers_failed = [check for check in checks if not check["passed"] and check["severity"] == "blocker"]
    warnings_failed = [check for check in checks if not check["passed"] and check["severity"] == "warning"]
    return {
        "asset": ASSET_NAME,
        "status": "A001 pre-geometry hard audit passed" if not blockers_failed else "A001 pre-geometry hard audit blocked",
        "source": str(SOURCE.relative_to(ROOT)),
        "source_sha256": sha256_file(SOURCE),
        "source_scanline_manifest": str(RESTART_MANIFEST.relative_to(ROOT)),
        "orientation_pixel_manifest": str(ORIENTATION_MANIFEST.relative_to(ROOT)),
        "measurement_formula_manifest": str(FORMULA_MANIFEST.relative_to(ROOT)),
        "pixel_count_center_manifest": str(CENTER_MANIFEST.relative_to(ROOT)),
        "snap_anchor_manifest": str(SNAP_MANIFEST.relative_to(ROOT)),
        "layer_contour_manifest": str(CONTOUR_MANIFEST.relative_to(ROOT)),
        "radial_trace_review_decision": str(RADIAL_DECISION_MANIFEST.relative_to(ROOT)),
        "oval_footprint_approval_manifest": str(OVAL_APPROVAL_MANIFEST.relative_to(ROOT)),
        "layered_contact_approval_manifest": str(LAYERED_CONTACT_APPROVAL_MANIFEST.relative_to(ROOT)),
        "formula_authority_manifest": str(FORMULA_AUTHORITY_MANIFEST.relative_to(ROOT)),
        "surface_marker_manifest": str(SURFACE_MARKER_MANIFEST.relative_to(ROOT)),
        "surface_marker_approval_manifest": str(SURFACE_MARKER_APPROVAL_MANIFEST.relative_to(ROOT)),
        "pregeometry_audit_board": str(PREGEOMETRY_AUDIT_BOARD.relative_to(ROOT)),
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
        "gate_status": "passed" if not blockers_failed else "blocked",
        "blocker_failures": blockers_failed,
        "warning_failures": warnings_failed,
        "checks": checks,
        "geometry_plan_allowed": not blockers_failed,
        "mesh_generation_allowed": False,
        "render_or_export_allowed": False,
        "next_required_step": "geometry construction plan" if not blockers_failed else "fix blocker failures and rerun audit",
        "known_constraints_to_carry_forward": [
            "upper socket/ring top footprint remains diagnostic/shared/occluded until a separate footprint formula is approved",
            "old 35cm support height is calibration/disagreement evidence only for visible contacts",
            "approved geometry plan must use per-view layered contact intervals with no averaging",
            "radial trace is diagnostic history only, not footprint-shape authority",
        ],
    }


def main() -> None:
    manifests = load_required_manifests()
    write_surface_marker_approval(manifests)
    checks = run_audit(manifests)
    create_review_board(checks)
    manifest = build_manifest(manifests, checks)
    PREGEOMETRY_AUDIT_MANIFEST.write_text(json.dumps(manifest, indent=2) + "\n")

    print(f"A001 surface marker approval manifest: {SURFACE_MARKER_APPROVAL_MANIFEST}")
    print(f"A001 pre-geometry hard audit manifest: {PREGEOMETRY_AUDIT_MANIFEST}")
    print(f"A001 pre-geometry hard audit board: {PREGEOMETRY_AUDIT_BOARD}")
    print(f"gate_status={manifest['gate_status']}")
    print(f"blocker_failures={len(manifest['blocker_failures'])}")
    print(f"warning_failures={len(manifest['warning_failures'])}")
    print("geometry_generated=False components_moved=False components_assembled=False")


if __name__ == "__main__":
    main()
