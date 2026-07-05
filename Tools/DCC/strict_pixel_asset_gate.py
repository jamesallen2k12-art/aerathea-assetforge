#!/usr/bin/env python3
"""Strict validation gate for pixel-measured DCC asset passes.

This gate is intentionally fail-closed. Run it after an asset-specific audit
script and before presenting proof renders for review.

Example:
    python3 Tools/DCC/strict_pixel_asset_gate.py \
      --audit Saved/Automation/DCC/ASSET/ASSET_GeometryColorGuidanceAudit.json \
      --generator Tools/DCC/build_asset.py
"""

from __future__ import annotations

import argparse
import json
import math
import re
import sys
from pathlib import Path
from typing import Any


DEFAULT_TOLERANCE_CM = 0.001
ALLOWED_VISIBLE_SELECTION_METHODS = {"exact", "source_priority", "outer_envelope", "inner_envelope", "direct_constraint"}
BLOCKED_VISIBLE_SELECTION_METHODS = {"average", "mean", "smoothed_average", "blend", "interpolated_average"}


GENERATOR_BLOCKERS: tuple[tuple[str, str], ...] = (
    (
        "visible_atlas_lanczos_resize",
        r"atlas\.paste\([^\n]+\.resize\([^\n]+resample_lanczos\(\)",
    ),
    (
        "explicit_base_to_stone_z_gap",
        r"MONOLITH_BOTTOM_Z_CM\s*=\s*BASE_HEIGHT_CM\s*\+",
    ),
    (
        "measured_top_ring_scaled_after_capture",
        r"outer\s*=\s*scale_ring_to_bounds\(outer,",
    ),
    (
        "measured_visible_geometry_replaced_by_superellipse",
        r"monolith_rings\.append\([^\n]+superellipse_ring\(",
    ),
    (
        "nearby_row_search_tolerance_for_visible_measurement",
        r"def\s+row_span\([^)]*search:\s*int\s*=\s*[1-9]",
    ),
)


def read_json(path: Path) -> dict[str, Any]:
    return json.loads(path.read_text(encoding="utf-8"))


def add_result(results: list[dict[str, Any]], name: str, passed: bool, detail: str) -> None:
    results.append({"name": name, "passed": bool(passed), "detail": detail})


def as_number(value: Any) -> float | None:
    if isinstance(value, bool):
        return None
    if isinstance(value, (int, float)):
        return float(value)
    return None


def check_pixel_color(report: dict[str, Any], results: list[dict[str, Any]]) -> None:
    pixel = report.get("pixel_color", {})
    add_result(
        results,
        "source_scanline_pixel_exact",
        pixel.get("source_scanline_pixel_exact") is True,
        "source scanline capture must rebuild with zero changed pixels",
    )

    per_view = pixel.get("per_view_visible_pixels", {})
    if not per_view:
        add_result(results, "per_view_visible_pixels_present", False, "no per-view visible-pixel evidence found")
    for view_name, item in sorted(per_view.items()):
        visible = item.get("visible_pixel_compare", {})
        add_result(
            results,
            f"{view_name}_visible_pixels_exact",
            visible.get("visible_pixels_exact") is True,
            f"visible source pixels for {view_name} must match exported texture exactly",
        )

    atlas_panels = pixel.get("atlas_panels", {})
    if atlas_panels:
        for view_name, item in sorted(atlas_panels.items()):
            panel = item.get("compare_actual_atlas_panel_to_nearest_pixel_copy", {})
            add_result(
                results,
                f"{view_name}_atlas_panel_no_resample_color_drift",
                panel.get("panel_pixel_exact_vs_nearest_source_copy") is True,
                f"atlas panel for {view_name} must be an exact nearest-copy result, not filtered/resampled color",
            )

    add_result(
        results,
        "strict_color_pass",
        pixel.get("strict_color_pass") is True,
        "aggregate color gate from the audit must pass",
    )


def check_geometry(report: dict[str, Any], results: list[dict[str, Any]], tolerance_cm: float) -> None:
    geometry = report.get("geometry", {})
    contact = geometry.get("contact_alignment", {})
    measurements = (
        report.get("accuracy_measurements")
        or report.get("geometry_accuracy", {}).get("measurements")
        or report.get("measurement_accuracy", {}).get("measurements")
        or []
    )
    declared_center_offsets = [
        item for item in measurements
        if isinstance(item, dict)
        and (
            "center_offset" in str(item.get("name", "")).lower()
            or "center" in str(item.get("source", item.get("constraint", ""))).lower()
        )
        and isinstance(item.get("error"), (int, float))
        and abs(float(item.get("error"))) <= float(item.get("tolerance", item.get("tolerance_cm", tolerance_cm)))
    ]
    add_result(
        results,
        "strict_contact_pass",
        geometry.get("strict_contact_pass") is True,
        "aggregate contact gate from the audit must pass",
    )

    for key, value in sorted(contact.items()):
        if key.endswith("_z_gap_cm"):
            number = as_number(value)
            add_result(
                results,
                key,
                number is not None and abs(number) <= tolerance_cm,
                f"{key} must be <= {tolerance_cm} cm from zero; observed {value}",
            )
        elif key.endswith("_center_xy_delta_cm") and isinstance(value, list):
            max_delta = max((abs(float(item)) for item in value), default=math.inf)
            center_delta_valid = max_delta <= tolerance_cm or bool(declared_center_offsets)
            add_result(
                results,
                key,
                center_delta_valid,
                f"{key} must be zero or match a declared source-measured center offset; observed {value}",
            )

    lod0_names = geometry.get("lod0_object_names", {})
    objects = geometry.get("objects", {})
    for label, name in sorted(lod0_names.items()):
        if isinstance(name, list):
            add_result(
                results,
                f"{label}_empty_or_valid_detector_list",
                not name,
                f"{label} detector list must be empty unless separately validated; observed {name}",
            )
            continue
        if not name:
            add_result(results, f"{label}_lod0_object_present", False, f"missing LOD0 object for {label}")
            continue
        item = objects.get(name, {})
        rotation = item.get("rotation_deg", [])
        max_rotation = max((abs(float(value)) for value in rotation), default=math.inf)
        add_result(
            results,
            f"{label}_rotation_zeroed",
            max_rotation <= 0.0001,
            f"{label} object rotation must be applied/zeroed before export; observed {rotation}",
        )
        edges = item.get("mesh_edges", {})
        add_result(
            results,
            f"{label}_no_boundary_or_nonmanifold_edges",
            edges.get("boundary_edges") == 0 and edges.get("nonmanifold_edges") == 0,
            f"{label} mesh must be closed; edge metrics {edges}",
        )


def normalize_key(value: Any) -> str:
    return str(value or "").strip().lower().replace(" ", "_").replace("-", "_")


def seam_list_from_report(report: dict[str, Any]) -> list[dict[str, Any]]:
    geometry = report.get("geometry", {})
    candidates = (
        geometry.get("exterior_edge_welds"),
        geometry.get("weld_measurements"),
        report.get("exterior_edge_welds"),
        report.get("weld_measurements"),
        geometry.get("seam_classifications"),
        report.get("seam_classifications"),
    )
    for candidate in candidates:
        if isinstance(candidate, dict):
            seams = candidate.get("seams")
            if isinstance(seams, list):
                return [item for item in seams if isinstance(item, dict)]
        if isinstance(candidate, list):
            return [item for item in candidate if isinstance(item, dict)]
    return []


def check_exterior_edge_welds(report: dict[str, Any], results: list[dict[str, Any]], default_tolerance_cm: float) -> None:
    geometry = report.get("geometry", {})
    strict_weld_pass = geometry.get("strict_exterior_weld_pass", report.get("strict_exterior_weld_pass"))
    seams = seam_list_from_report(report)
    add_result(
        results,
        "seam_classifications_present",
        bool(seams),
        "strict pixel assets must classify exterior, interior, occluded, or inferred hidden seams",
    )

    allowed_classifications = {
        "visible_exterior",
        "visible_exterior_seam",
        "exterior",
        "interior",
        "interior_seam",
        "occluded_contact",
        "occluded_contact_seam",
        "inferred_hidden",
        "inferred_hidden_seam",
    }
    exterior_classifications = {"visible_exterior", "visible_exterior_seam", "exterior"}
    hidden_classifications = {"interior", "interior_seam", "occluded_contact", "occluded_contact_seam", "inferred_hidden", "inferred_hidden_seam"}
    non_exterior_edge_roles = {
        "interior_edge",
        "contact_mount",
        "occluded_edge",
        "inferred_hidden_edge",
        "annulus",
        "same_plane_annulus",
        "concentric_loop",
    }
    disallowed_exterior_bridge_relations = {
        "same_plane_annulus",
        "concentric_loop",
        "contact_mount",
        "interior_bridge",
        "interior_edge",
        "occluded_edge",
        "non_exterior",
    }
    bridge_statuses = {"unified_mesh_bridge", "documented_unified_mesh_bridge", "shared_exterior_vertices"}

    for index, seam in enumerate(seams):
        name = str(seam.get("name") or seam.get("seam") or f"seam_{index}")
        safe_name = re.sub(r"[^A-Za-z0-9_]+", "_", name).strip("_")
        classification = normalize_key(seam.get("classification"))
        edge_role = normalize_key(seam.get("edge_role", seam.get("weld_edge_role")))
        weld_scope = normalize_key(seam.get("weld_scope"))
        edge_loop_relation = normalize_key(seam.get("edge_loop_relation", seam.get("loop_relation")))
        tolerance = float(seam.get("tolerance_cm", seam.get("tolerance", default_tolerance_cm)))

        add_result(
            results,
            f"seam_{safe_name}_classification_declared",
            classification in allowed_classifications,
            f"{name} must classify the seam; observed '{classification or 'missing'}'",
        )

        if classification in exterior_classifications:
            add_result(
                results,
                f"seam_{safe_name}_edge_role_exterior_perimeter",
                edge_role == "exterior_perimeter",
                f"{name} visible exterior weld must declare edge_role=exterior_perimeter; observed '{edge_role or 'missing'}'",
            )
            add_result(
                results,
                f"seam_{safe_name}_weld_scope_exterior_only",
                weld_scope == "exterior_only",
                f"{name} visible exterior weld must declare weld_scope=exterior_only; observed '{weld_scope or 'missing'}'",
            )
            add_result(
                results,
                f"seam_{safe_name}_not_interior_or_annulus_bridge",
                edge_loop_relation not in disallowed_exterior_bridge_relations,
                f"{name} visible exterior weld cannot be a same-plane annulus, concentric-loop, contact-mount, or interior bridge; observed '{edge_loop_relation or 'missing'}'",
            )
            max_gap = (
                as_number(seam.get("max_gap_cm"))
                if "max_gap_cm" in seam
                else as_number(seam.get("max_exterior_edge_gap_cm", seam.get("max_gap")))
            )
            add_result(
                results,
                f"seam_{safe_name}_max_gap_within_tolerance",
                max_gap is not None and abs(max_gap) <= tolerance,
                f"{name} visible exterior max gap must be <= {tolerance} cm; observed {max_gap}",
            )

            shared_count = seam.get("shared_vertex_count", seam.get("welded_shared_vertex_count"))
            expected_shared = seam.get("expected_shared_vertex_count", seam.get("expected_welded_shared_vertex_count"))
            try:
                shared_count_number = int(shared_count)
                expected_shared_number = int(expected_shared)
            except (TypeError, ValueError):
                shared_count_number = -1
                expected_shared_number = 0
            bridge_status = normalize_key(seam.get("seam_bridge_status"))
            bridge_scope = normalize_key(seam.get("seam_bridge_scope", seam.get("bridge_scope")))
            shared_or_bridged = (
                seam.get("welded") is True
                or seam.get("shared_vertices") is True
                or (expected_shared_number > 0 and shared_count_number >= expected_shared_number)
                or bridge_status in bridge_statuses
            )
            add_result(
                results,
                f"seam_{safe_name}_shared_or_bridged",
                shared_or_bridged,
                f"{name} must prove shared exterior vertices or a documented unified mesh bridge",
            )
            if bridge_status in bridge_statuses:
                add_result(
                    results,
                    f"seam_{safe_name}_bridge_scope_perimeter_only",
                    bridge_scope in {"perimeter_only", "exterior_perimeter_only", "exterior_only"},
                    f"{name} bridge must be perimeter-only; observed bridge_scope '{bridge_scope or 'missing'}'",
                )

            unwelded = (
                as_number(seam.get("unwelded_exterior_edge_count"))
                if "unwelded_exterior_edge_count" in seam
                else as_number(seam.get("unwelded_edge_count"))
            )
            add_result(
                results,
                f"seam_{safe_name}_no_unwelded_exterior_edges",
                unwelded is not None and int(unwelded) == 0,
                f"{name} must report zero unwelded visible exterior edges; observed {unwelded}",
            )

            uv_source = str(seam.get("uv_edge_source") or seam.get("uv_source") or "")
            uv_samples_background = seam.get("uv_samples_crop_background")
            uses_untagged_padding = seam.get("uv_uses_untagged_padding")
            add_result(
                results,
                f"seam_{safe_name}_uv_edge_source_valid",
                bool(uv_source) and uv_samples_background is False and uses_untagged_padding is not True,
                f"{name} visible seam UVs must name a valid edge source and must not sample crop background or untagged padding",
            )

        if classification in hidden_classifications:
            inner_deformed = seam.get("inner_edges_welded_or_deformed")
            contact_requirement = seam.get("contact_requirement_declared")
            bridge_status = normalize_key(seam.get("seam_bridge_status"))
            interior_bridge_created = seam.get("interior_bridge_created")
            annulus_bridge_created = seam.get("annulus_bridge_created")
            add_result(
                results,
                f"seam_{safe_name}_inner_edges_preserved_or_declared",
                inner_deformed is not True or contact_requirement is True,
                f"{name} hidden/interior edges must not be welded or deformed without a declared contact requirement",
            )
            add_result(
                results,
                f"seam_{safe_name}_no_interior_or_annulus_bridge_as_fix",
                interior_bridge_created is not True
                and annulus_bridge_created is not True
                and bridge_status not in {"unified_mesh_bridge", "documented_unified_mesh_bridge"},
                f"{name} hidden/interior/contact seam must not create a same-plane annulus, contact-mount, or interior bridge as an exterior fix",
            )

        if edge_role in non_exterior_edge_roles:
            add_result(
                results,
                f"seam_{safe_name}_non_exterior_role_not_classified_exterior",
                classification not in exterior_classifications,
                f"{name} has non-exterior edge_role '{edge_role}' and must not be classified as a visible exterior weld",
            )

    add_result(
        results,
        "strict_exterior_weld_pass",
        strict_weld_pass is True,
        "aggregate exterior seam weld gate from the audit must pass",
    )


def check_surface_view_ownership(report: dict[str, Any], results: list[dict[str, Any]]) -> None:
    geometry = report.get("geometry", {})
    surface = (
        geometry.get("surface_view_ownership")
        or report.get("surface_view_ownership")
        or report.get("pixel_color", {}).get("surface_view_ownership")
        or {}
    )
    add_result(
        results,
        "surface_view_ownership_present",
        isinstance(surface, dict) and bool(surface),
        "visible surfaces must prove view-owned atlas mapping for front, back, left, right, top, and review angles",
    )
    if not isinstance(surface, dict) or not surface:
        return

    add_result(
        results,
        "strict_surface_view_ownership_pass",
        surface.get("strict_surface_view_ownership_pass") is True,
        "aggregate surface view ownership gate from the audit must pass",
    )
    for key in (
        "wrong_source_faces",
        "wrong_source_loops",
        "uvs_outside_owned_atlas_region",
        "uvs_outside_visible_row_span",
        "uv_row_mismatch_loops",
        "primary_top_uvs_outside_component_mask",
        "support_top_uvs_inside_primary_component_mask",
    ):
        value = surface.get(key)
        add_result(
            results,
            f"surface_view_ownership_{key}_zero",
            isinstance(value, int) and value == 0,
            f"{key} must be zero; observed {value}",
        )

    required_angles = {"front", "front-right", "right", "back-right", "back", "back-left", "left", "front-left", "top", "beauty"}
    observed_angles = {str(item) for item in surface.get("review_angle_coverage", [])}
    missing_angles = sorted(required_angles - observed_angles)
    add_result(
        results,
        "surface_view_ownership_all_review_angles_present",
        not missing_angles,
        f"all-angle review coverage must include {sorted(required_angles)}; missing {missing_angles}",
    )
    primary_top_faces = surface.get("primary_top_faces_checked")
    add_result(
        results,
        "surface_view_ownership_primary_top_faces_checked",
        isinstance(primary_top_faces, int) and primary_top_faces > 0,
        f"primary top faces must be checked against the primary-only top component mask; observed {primary_top_faces}",
    )
    support_top_faces = surface.get("support_top_faces_checked")
    add_result(
        results,
        "surface_view_ownership_support_top_faces_checked",
        isinstance(support_top_faces, int) and support_top_faces > 0,
        f"support top faces must be checked against the primary-only top component mask to prove they stay outside it; observed {support_top_faces}",
    )

    by_view = surface.get("by_expected_view", {})
    for view_name in ("front", "back", "left", "right", "top"):
        item = by_view.get(view_name, {}) if isinstance(by_view, dict) else {}
        faces = item.get("faces")
        add_result(
            results,
            f"surface_view_ownership_{view_name}_faces_present",
            isinstance(faces, int) and faces > 0,
            f"{view_name} must have checked visible faces; observed {faces}",
        )
        for key in ("wrong_source_faces", "wrong_source_loops"):
            value = item.get(key)
            add_result(
                results,
                f"surface_view_ownership_{view_name}_{key}_zero",
                isinstance(value, int) and value == 0,
                f"{view_name} {key} must be zero; observed {value}",
            )
        if view_name in {"front", "back", "left", "right"}:
            for key in ("uvs_outside_visible_row_span", "uv_row_mismatch_loops"):
                value = item.get(key)
                add_result(
                    results,
                    f"surface_view_ownership_{view_name}_{key}_zero",
                    isinstance(value, int) and value == 0,
                    f"{view_name} {key} must be zero; observed {value}",
                )


def check_component_source_lineage(report: dict[str, Any], results: list[dict[str, Any]]) -> None:
    geometry = report.get("geometry", {})
    lineage = (
        geometry.get("component_source_lineage")
        or report.get("component_source_lineage")
        or report.get("source_lineage")
        or {}
    )
    add_result(
        results,
        "component_source_lineage_present",
        isinstance(lineage, dict) and bool(lineage),
        "multi-component strict pixel assets must report component source lineage",
    )
    if not isinstance(lineage, dict) or not lineage:
        return

    copied_or_resized = lineage.get("copied_or_resized_component_layers", [])
    legacy_layers = lineage.get("legacy_copied_support_layers_in_scene", [])
    component_failures = lineage.get("component_lineage_failures", [])
    components = lineage.get("components", {})
    add_result(
        results,
        "component_source_lineage_strict_pass",
        lineage.get("strict_no_cross_component_copy_pass") is True,
        "component lineage audit must pass: no support/base layer may be copied, resized, projected, or inherited into the primary component",
    )
    add_result(
        results,
        "component_source_lineage_no_copied_or_resized_layers",
        isinstance(copied_or_resized, list) and not copied_or_resized,
        f"copied/resized component layers are forbidden; observed {copied_or_resized}",
    )
    add_result(
        results,
        "component_source_lineage_no_legacy_support_layers",
        isinstance(legacy_layers, list) and not legacy_layers,
        f"legacy lower/upper copied support layers must not exist in the scene; observed {legacy_layers}",
    )
    add_result(
        results,
        "component_source_lineage_no_component_failures",
        isinstance(component_failures, list) and not component_failures,
        f"components must declare independent source ownership with no copied/rescaled parent; observed {component_failures}",
    )
    add_result(
        results,
        "component_source_lineage_required_components_present",
        isinstance(components, dict) and {"support_object", "primary_object"}.issubset(set(components.keys())),
        "component lineage must include support_object and primary_object",
    )
    if isinstance(components, dict):
        for component_name, item in components.items():
            if not isinstance(item, dict):
                add_result(
                    results,
                    f"component_source_lineage_{component_name}_valid",
                    False,
                    f"{component_name} lineage entry must be an object",
                )
                continue
            add_result(
                results,
                f"component_source_lineage_{component_name}_not_copied",
                item.get("copied_from_component") in (None, "", False),
                f"{component_name} must not copy geometry or texture ownership from another component",
            )
            add_result(
                results,
                f"component_source_lineage_{component_name}_not_rescaled_from_other_component",
                item.get("rescaled_from_component") is not True,
                f"{component_name} must not be a rescaled version of another component",
            )


def check_generator(generator: Path, results: list[dict[str, Any]]) -> None:
    text = generator.read_text(encoding="utf-8")
    for name, pattern in GENERATOR_BLOCKERS:
        matched = re.search(pattern, text, flags=re.MULTILINE)
        add_result(
            results,
            f"generator_no_{name}",
            matched is None,
            f"generator must not contain strict-pixel blocker pattern: {name}",
        )


def numeric_error(observed: Any, expected: Any) -> float | None:
    if isinstance(observed, (int, float)) and isinstance(expected, (int, float)):
        return abs(float(observed) - float(expected))
    if isinstance(observed, list) and isinstance(expected, list) and len(observed) == len(expected):
        try:
            return max(abs(float(left) - float(right)) for left, right in zip(observed, expected))
        except (TypeError, ValueError):
            return None
    return None


def check_accuracy_measurements(report: dict[str, Any], results: list[dict[str, Any]], default_tolerance_cm: float) -> None:
    measurements = (
        report.get("accuracy_measurements")
        or report.get("geometry_accuracy", {}).get("measurements")
        or report.get("measurement_accuracy", {}).get("measurements")
        or []
    )
    add_result(
        results,
        "accuracy_measurements_present",
        bool(measurements),
        "strict pixel assets must report generic observed-vs-expected source accuracy measurements",
    )
    for index, item in enumerate(measurements):
        name = str(item.get("name") or f"measurement_{index}")
        visible = item.get("visible", True) is True
        expected = item.get("expected")
        observed = item.get("observed")
        error = item.get("error")
        if error is None:
            error = numeric_error(observed, expected)
        tolerance = float(item.get("tolerance", item.get("tolerance_cm", default_tolerance_cm)))
        unit = str(item.get("unit", item.get("units", "cm")))
        selection_method = str(item.get("selection_method", item.get("method", ""))).strip().lower()
        component = str(item.get("component", item.get("component_owner", item.get("owner_component", "")))).strip()
        source_scope = normalize_key(item.get("source_scope", item.get("mask_scope", item.get("measurement_scope"))))

        add_result(
            results,
            f"accuracy_{name}_has_source",
            bool(item.get("source") or item.get("source_view") or item.get("constraint")),
            f"{name} must name the source measurement or constraint it was checked against",
        )
        add_result(
            results,
            f"accuracy_{name}_has_error",
            isinstance(error, (int, float)),
            f"{name} must report numeric error from observed-vs-expected measurement",
        )
        if isinstance(error, (int, float)):
            add_result(
                results,
                f"accuracy_{name}_within_tolerance",
                abs(float(error)) <= tolerance,
                f"{name} error must be <= {tolerance} {unit}; observed error {error}",
            )
        if visible:
            add_result(
                results,
                f"accuracy_{name}_visible_not_averaged",
                selection_method not in BLOCKED_VISIBLE_SELECTION_METHODS,
                f"{name} is visible geometry and must not use an averaging method; observed method '{selection_method or 'missing'}'",
            )
            add_result(
                results,
                f"accuracy_{name}_visible_selection_method_declared",
                selection_method in ALLOWED_VISIBLE_SELECTION_METHODS,
                f"{name} visible selection method must be one of {sorted(ALLOWED_VISIBLE_SELECTION_METHODS)}; observed '{selection_method or 'missing'}'",
            )
            pixel_component_measurement = selection_method != "direct_constraint"
            if pixel_component_measurement:
                add_result(
                    results,
                    f"accuracy_{name}_visible_component_owner_declared",
                    bool(component),
                    f"{name} is visible geometry and must declare the component owner measured from source pixels",
                )
                add_result(
                    results,
                    f"accuracy_{name}_visible_component_scope_not_full_object",
                    source_scope not in {"", "full_object", "full_object_mask", "assembled_object", "combined_mask"},
                    f"{name} is visible component geometry and must not be validated from a full-object or combined mask; observed scope '{source_scope or 'missing'}'",
                )
                if component and any(token in name.lower() for token in ("primary", "stone", "monolith")):
                    add_result(
                        results,
                        f"accuracy_{name}_primary_component_isolated",
                        source_scope in {"component_isolated", "primary_component", "central_stone_component", "bloodaxe_stone_component"},
                        f"{name} must be measured from a primary-component-isolated mask; observed scope '{source_scope or 'missing'}'",
                    )


def write_report(path: Path, payload: dict[str, Any]) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(json.dumps(payload, indent=2) + "\n", encoding="utf-8")


def main() -> int:
    parser = argparse.ArgumentParser(description="Fail-closed strict pixel asset validation gate.")
    parser.add_argument("--audit", required=True, type=Path, help="Asset audit JSON path.")
    parser.add_argument("--generator", type=Path, help="Optional generator script to scan for known strict-pixel blockers.")
    parser.add_argument("--out", type=Path, help="Optional JSON gate report path.")
    parser.add_argument("--tolerance-cm", type=float, default=DEFAULT_TOLERANCE_CM)
    args = parser.parse_args()

    report = read_json(args.audit)
    results: list[dict[str, Any]] = []
    check_pixel_color(report, results)
    check_geometry(report, results, args.tolerance_cm)
    check_exterior_edge_welds(report, results, args.tolerance_cm)
    check_surface_view_ownership(report, results)
    check_component_source_lineage(report, results)
    check_accuracy_measurements(report, results, args.tolerance_cm)
    if args.generator is not None:
        check_generator(args.generator, results)

    passed = all(item["passed"] for item in results)
    payload = {
        "audit": str(args.audit),
        "generator": str(args.generator) if args.generator else None,
        "tolerance_cm": args.tolerance_cm,
        "passed": passed,
        "failed_checks": [item for item in results if not item["passed"]],
        "results": results,
    }
    if args.out is not None:
        write_report(args.out, payload)

    print("STRICT PIXEL ASSET GATE:", "PASS" if passed else "FAIL")
    for item in payload["failed_checks"]:
        print(f"- {item['name']}: {item['detail']}")
    return 0 if passed else 2


if __name__ == "__main__":
    raise SystemExit(main())
