#!/usr/bin/env python3
"""Create the A001 geometry construction plan.

This is a planning pass only. It promotes the approved measurement evidence
into a mesh-construction recipe, but it does not generate mesh data, UVs,
textures, renders, movement, rotation, centering, or assembly.
"""

from __future__ import annotations

import hashlib
import json
from pathlib import Path
from textwrap import dedent
from typing import Any

from PIL import Image, ImageDraw, ImageFont


ROOT = Path(__file__).resolve().parents[2]
ASSET_NAME = "SM_GIA_BloodAxeCairnstone_A001"
SOURCE = ROOT / "docs/assets/reference/bloodaxe_cairnstone_asset/REF_GIA_BloodAxeCairnstoneAsset_A02_BlueprintTemplate.png"
OUT_DIR = ROOT / "Saved/Automation/DCC" / ASSET_NAME
DOC_PATH = ROOT / "docs/projects/assetforge/BLOODAXE_CAIRNSTONE_A001_GEOMETRY_CONSTRUCTION_PLAN.md"

PREGEOMETRY_AUDIT_MANIFEST = OUT_DIR / f"{ASSET_NAME}_A001PreGeometryHardAuditManifest.json"
FORMULA_AUTHORITY_MANIFEST = OUT_DIR / f"{ASSET_NAME}_A001FormulaAuthorityManifest.json"
SURFACE_MARKER_APPROVAL_MANIFEST = OUT_DIR / f"{ASSET_NAME}_A001SurfaceEdgeMarkerApprovalManifest.json"
SURFACE_MARKER_MANIFEST = OUT_DIR / f"{ASSET_NAME}_A001SurfaceEdgeMarkerManifest.json"
OVAL_APPROVAL_MANIFEST = OUT_DIR / f"{ASSET_NAME}_A001OvalFootprintApprovalManifest.json"
LAYERED_CONTACT_APPROVAL_MANIFEST = OUT_DIR / f"{ASSET_NAME}_A001LayeredContactFormulaApprovalManifest.json"
RADIAL_DECISION_MANIFEST = OUT_DIR / f"{ASSET_NAME}_A001RadialTraceReviewDecision.json"

PLAN_MANIFEST = OUT_DIR / f"{ASSET_NAME}_A001GeometryConstructionPlanManifest.json"
PLAN_BOARD = OUT_DIR / f"{ASSET_NAME}_A001GeometryConstructionPlanReviewBoard.png"


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


def require_clean_pre_geometry(name: str, manifest: dict[str, Any]) -> None:
    state = manifest.get("pre_geometry_state")
    if not isinstance(state, dict):
        raise SystemExit(f"{name} is missing pre_geometry_state.")
    for key in (
        "geometry_generated",
        "uvs_generated",
        "components_moved",
        "components_rotated",
        "components_centered",
        "components_assembled",
        "inferred_fill_generated",
        "source_pixels_modified",
    ):
        if state.get(key) is not False:
            raise SystemExit(f"{name} is not clean pre-geometry: {key}={state.get(key)!r}")


def load_inputs() -> dict[str, dict[str, Any]]:
    paths = {
        "pregeometry_audit": PREGEOMETRY_AUDIT_MANIFEST,
        "formula_authority": FORMULA_AUTHORITY_MANIFEST,
        "surface_marker_approval": SURFACE_MARKER_APPROVAL_MANIFEST,
        "surface_markers": SURFACE_MARKER_MANIFEST,
        "oval_approval": OVAL_APPROVAL_MANIFEST,
        "layered_contact_approval": LAYERED_CONTACT_APPROVAL_MANIFEST,
        "radial_decision": RADIAL_DECISION_MANIFEST,
    }
    missing = [str(path) for path in paths.values() if not path.exists()]
    if missing:
        raise SystemExit("Missing required plan input(s):\n" + "\n".join(missing))
    manifests = {name: read_json(path) for name, path in paths.items()}
    if manifests["pregeometry_audit"].get("gate_status") != "passed":
        raise SystemExit("Pre-geometry hard audit has not passed.")
    if manifests["pregeometry_audit"].get("geometry_plan_allowed") is not True:
        raise SystemExit("Pre-geometry audit does not allow geometry planning.")
    for name, manifest in manifests.items():
        require_clean_pre_geometry(name, manifest)
    return manifests


def approved_oval_by_id(oval: dict[str, Any]) -> dict[str, dict[str, Any]]:
    return {
        str(record["stable_component_id"]): record
        for record in oval.get("approved_records", [])
        if isinstance(record, dict)
    }


def contact_by_view(layered: dict[str, Any]) -> dict[str, dict[str, Any]]:
    return {
        str(record["source_view"]): record
        for record in layered.get("approved_intervals", [])
        if isinstance(record, dict)
    }


def build_component_plan(manifests: dict[str, dict[str, Any]]) -> list[dict[str, Any]]:
    oval = approved_oval_by_id(manifests["oval_approval"])
    contacts = contact_by_view(manifests["layered_contact_approval"])
    surface = manifests["surface_markers"].get("surface_angle_and_edge_correspondence", {})

    primary = oval["primary_monolith"]
    support = oval["support_base"]
    view_contacts = {
        view: {
            "ring_bottom_z_cm": data["upper_ring_bottom_contact"]["z_cm"],
            "ring_top_z_cm": data["upper_ring_top_contact"]["z_cm"],
            "ring_interval_cm": data["upper_ring_interval_cm"],
            "support_visible_height_cm": data["support_visible_height_to_ring_bottom_cm"],
            "primary_starts_at_z_cm": data["primary_starts_at_ring_top_cm"],
            "no_average_used": data["no_average_used"],
        }
        for view, data in sorted(contacts.items())
    }

    return [
        {
            "component_id": "primary_monolith",
            "export_role": "reusable source component; later may be combined into final static mesh after lineage is preserved",
            "geometry_source": "approved 120cm x 90cm measured oval top footprint plus front/back/left/right side markers",
            "top_footprint": primary["measured_width_depth_cm"],
            "top_formula_box_px": primary["top_formula_box_px"],
            "z_stations": {
                "top_z_cm": 220.0,
                "bottom_contact_by_view_cm": {
                    view: data["primary_starts_at_z_cm"] for view, data in view_contacts.items()
                },
            },
            "construction_recipe": [
                "Generate a separate primary side shell from view-owned exterior edge markers.",
                "Use the approved oval formula only for the top footprint envelope; do not use the rejected radial pass.",
                "Use the approved per-view primary-to-ring contact stations for the bottom loop; do not flatten to 35cm.",
                "Keep top cap UVs inside the primary top mask only.",
            ],
            "normal_owners": surface.get("normal_owners"),
            "blocked_methods": [
                "support/base projection onto primary",
                "old radial trace as footprint authority",
                "old 35cm contact flattening",
                "cross-view averaging",
            ],
        },
        {
            "component_id": "upper_socket_ring",
            "export_role": "reusable source component and contact layer between primary and support",
            "geometry_source": "approved per-view layered contact intervals plus surface-edge markers",
            "top_footprint": "diagnostic shared/occluded top envelope only until separate footprint formula is approved",
            "z_stations_by_view": view_contacts,
            "construction_recipe": [
                "Generate the ring/socket as an independent interval component.",
                "Use per-view top and bottom contact stations exactly as recorded; no global average.",
                "Do not inherit taper, normals, UVs, or side shell from the primary object.",
                "Hidden/occluded contact surfaces remain tagged and cannot override visible source data.",
            ],
            "normal_owners": surface.get("normal_owners"),
            "blocked_methods": [
                "merging ring into primary side shell",
                "copying/scaling support ring",
                "same-plane annulus bridge as exterior fix",
                "unapproved full top cap",
            ],
        },
        {
            "component_id": "support_base",
            "export_role": "reusable source component; base/support layer",
            "geometry_source": "approved 140cm x 110cm measured oval footprint plus approved ring-bottom contact stations",
            "top_footprint": support["measured_width_depth_cm"],
            "top_formula_box_px": support["top_formula_box_px"],
            "z_stations": {
                "bottom_z_cm": 0.0,
                "top_contact_by_view_cm": {
                    view: data["ring_bottom_z_cm"] for view, data in view_contacts.items()
                },
            },
            "construction_recipe": [
                "Generate the support/base as its own component from the approved 140x110cm oval footprint.",
                "Use approved upper-ring-to-support contact stations for the top contact loop.",
                "Support visible top/annulus must stay outside the primary component mask.",
                "Do not copy, resize, or project support/base pixels into the primary component.",
            ],
            "normal_owners": surface.get("normal_owners"),
            "blocked_methods": [
                "full top cap sampling under primary",
                "base layer copied onto primary",
                "old A02/A23/A26 generator logic",
                "stretch patches or detached shells",
            ],
        },
    ]


def build_plan(manifests: dict[str, dict[str, Any]]) -> dict[str, Any]:
    component_plan = build_component_plan(manifests)
    constraints = manifests["pregeometry_audit"].get("known_constraints_to_carry_forward", [])
    return {
        "asset": ASSET_NAME,
        "status": "A001 geometry construction plan candidate recorded; no mesh generated",
        "source": str(SOURCE.relative_to(ROOT)),
        "source_sha256": sha256_file(SOURCE),
        "pregeometry_audit_manifest": str(PREGEOMETRY_AUDIT_MANIFEST.relative_to(ROOT)),
        "formula_authority_manifest": str(FORMULA_AUTHORITY_MANIFEST.relative_to(ROOT)),
        "surface_marker_approval_manifest": str(SURFACE_MARKER_APPROVAL_MANIFEST.relative_to(ROOT)),
        "surface_marker_manifest": str(SURFACE_MARKER_MANIFEST.relative_to(ROOT)),
        "oval_footprint_approval_manifest": str(OVAL_APPROVAL_MANIFEST.relative_to(ROOT)),
        "layered_contact_approval_manifest": str(LAYERED_CONTACT_APPROVAL_MANIFEST.relative_to(ROOT)),
        "radial_decision_manifest": str(RADIAL_DECISION_MANIFEST.relative_to(ROOT)),
        "geometry_construction_plan_doc": str(DOC_PATH.relative_to(ROOT)),
        "geometry_construction_plan_board": str(PLAN_BOARD.relative_to(ROOT)),
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
        "plan_scope": {
            "allowed_now": "planning only",
            "mesh_generation_allowed_now": False,
            "render_or_export_allowed_now": False,
            "approval_required_to_generate_mesh_candidate": True,
            "next_after_approval": "generate DCC source candidate geometry proof, not final beauty render",
        },
        "component_plan": component_plan,
        "global_construction_rules": [
            "Build primary, upper socket/ring, and support/base independently before attachment.",
            "Use approved per-view station values; do not average contact disagreement away.",
            "Use exact source-derived markers for side edge correspondence and normal ownership.",
            "Preserve component lineage even if a later runtime mesh is combined.",
            "Texture and UV generation remain blocked until geometry proof passes.",
        ],
        "blocked_methods": [
            "old contaminated generator logic",
            "radial trace as footprint-shape authority",
            "single 35cm support height as visible contact authority",
            "copied/resized support-base layer",
            "primary/support full top cap mixing",
            "stretch strip, detached shell, cover-up plane, or visual patch",
            "global averaging of per-view contact stations",
        ],
        "validation_targets_for_mesh_candidate": [
            "geometry proof render with markers",
            "top/front/back/left/right orientation proof",
            "edge-loop gap report for exterior seams",
            "component lineage proof",
            "no UV/texture approval until geometry proof passes",
        ],
        "known_constraints_to_carry_forward": constraints,
        "approval_status": "pending_Flamestrike_review",
        "geometry_use_status": "candidate_pending_plan_review; mesh_generation_blocked_until_approved",
    }


def write_markdown(plan: dict[str, Any]) -> None:
    component_sections = []
    for component in plan["component_plan"]:
        recipes = "\n".join(f"- {line}" for line in component["construction_recipe"])
        blocked = "\n".join(f"- {line}" for line in component["blocked_methods"])
        component_sections.append(
            f"""## {component['component_id']}

Export role: {component['export_role']}

Geometry source: {component['geometry_source']}

Top footprint: `{component['top_footprint']}`

Construction:
{recipes}

Blocked:
{blocked}
"""
        )

    global_rules = "\n".join(f"- {line}" for line in plan["global_construction_rules"])
    validation = "\n".join(f"- {line}" for line in plan["validation_targets_for_mesh_candidate"])
    constraints = "\n".join(f"- {line}" for line in plan["known_constraints_to_carry_forward"])
    blocked = "\n".join(f"- {line}" for line in plan["blocked_methods"])
    components_md = "\n".join(component_sections)

    content = dedent(
        f"""\
        # BloodAxe Cairnstone A001 Geometry Construction Plan

        Status: `{plan['status']}`

        This is a planning artifact only. No mesh, UVs, textures, movement, rotation, centering, assembly, render, or export has been generated.

        ## Approved Inputs

        - Pre-geometry audit: `{plan['pregeometry_audit_manifest']}`
        - Formula authority: `{plan['formula_authority_manifest']}`
        - Surface marker approval: `{plan['surface_marker_approval_manifest']}`
        - Surface marker manifest: `{plan['surface_marker_manifest']}`
        - Oval footprint approval: `{plan['oval_footprint_approval_manifest']}`
        - Layered contact approval: `{plan['layered_contact_approval_manifest']}`
        - Radial decision: `{plan['radial_decision_manifest']}`

        ## Plan Scope

        - Allowed now: geometry construction planning only.
        - Mesh generation allowed now: `false`.
        - Render/export allowed now: `false`.
        - Approval required before mesh candidate generation: `true`.

        ## Global Construction Rules

        {global_rules}

        ## Components

        {components_md}

        ## Blocked Methods

        {blocked}

        ## Mesh Candidate Validation Targets

        {validation}

        ## Constraints To Carry Forward

        {constraints}
        """
    )
    DOC_PATH.write_text(content)


def draw_wrapped(draw: ImageDraw.ImageDraw, xy: tuple[int, int], text: str, fill: tuple[int, int, int], size: int, width: int, line_gap: int = 7) -> int:
    words = text.split()
    lines: list[str] = []
    current = ""
    fnt = font(size)
    for word in words:
        trial = f"{current} {word}".strip()
        if draw.textbbox((0, 0), trial, font=fnt)[2] <= width:
            current = trial
        else:
            if current:
                lines.append(current)
            current = word
    if current:
        lines.append(current)
    x, y = xy
    for line in lines:
        draw.text((x, y), line, fill=fill, font=fnt)
        y += size + line_gap
    return y


def create_board(plan: dict[str, Any]) -> None:
    board = Image.new("RGB", (1900, 1500), (245, 243, 238))
    draw = ImageDraw.Draw(board)
    draw.text((40, 28), "A001 Geometry Construction Plan", fill=(24, 21, 18), font=font(30))
    draw.text((40, 74), "Planning only. No mesh, UVs, textures, movement, assembly, render, or export generated.", fill=(55, 48, 42), font=font(18))
    draw.text((40, 118), "Status: Pending Flamestrike Review", fill=(145, 86, 18), font=font(24))

    x, y = 40, 170
    draw.rectangle((x, y, 1810, 420), fill=(255, 255, 255), outline=(75, 68, 62), width=2)
    draw.text((x + 18, y + 18), "Approved Authority", fill=(24, 21, 18), font=font(22))
    authority_lines = [
        "Primary top footprint: approved 120 x 90 cm measured oval.",
        "Support/base footprint: approved 140 x 110 cm measured oval.",
        "Upper socket/ring: approved per-view layered contact interval; no global average.",
        "Old 35 cm support height: calibration/disagreement evidence only.",
        "Radial trace: diagnostic history only, not footprint authority.",
    ]
    yy = y + 58
    for line in authority_lines:
        draw.text((x + 18, yy), f"- {line}", fill=(48, 42, 36), font=font(17))
        yy += 32

    component_y = 455
    col_w = 560
    for idx, component in enumerate(plan["component_plan"]):
        cx = 40 + idx * 610
        draw.rectangle((cx, component_y, cx + col_w, 1040), fill=(255, 255, 255), outline=(75, 68, 62), width=2)
        draw.text((cx + 18, component_y + 18), component["component_id"], fill=(24, 21, 18), font=font(22))
        yy = component_y + 58
        yy = draw_wrapped(draw, (cx + 18, yy), f"Source: {component['geometry_source']}", (48, 42, 36), 15, col_w - 36)
        yy += 8
        yy = draw_wrapped(draw, (cx + 18, yy), f"Top footprint: {component['top_footprint']}", (48, 42, 36), 15, col_w - 36)
        yy += 14
        draw.text((cx + 18, yy), "Construction", fill=(24, 21, 18), font=font(17))
        yy += 30
        for line in component["construction_recipe"][:4]:
            yy = draw_wrapped(draw, (cx + 18, yy), f"- {line}", (48, 42, 36), 14, col_w - 36)
        yy += 10
        draw.text((cx + 18, yy), "Blocked", fill=(130, 42, 32), font=font(17))
        yy += 30
        for line in component["blocked_methods"][:4]:
            yy = draw_wrapped(draw, (cx + 18, yy), f"- {line}", (92, 50, 40), 14, col_w - 36)

    y2 = 1080
    draw.rectangle((40, y2, 1810, 1405), fill=(255, 255, 255), outline=(75, 68, 62), width=2)
    draw.text((58, y2 + 18), "Approval Gate", fill=(24, 21, 18), font=font(22))
    gate_lines = [
        "Approve this plan to unlock a DCC source candidate geometry proof.",
        "The next output after approval is a geometry proof, not a beauty render or final export.",
        "Texture/UV/color proof remains blocked until geometry proof passes.",
        "Any plan change must be recorded before mesh generation.",
    ]
    yy = y2 + 60
    for line in gate_lines:
        draw.text((58, yy), f"- {line}", fill=(48, 42, 36), font=font(17))
        yy += 34

    draw.text((58, y2 + 220), "Mesh generation allowed now: false", fill=(160, 35, 35), font=font(18))
    draw.text((58, y2 + 255), "Render/export allowed now: false", fill=(160, 35, 35), font=font(18))

    PLAN_BOARD.parent.mkdir(parents=True, exist_ok=True)
    board.save(PLAN_BOARD)


def main() -> None:
    manifests = load_inputs()
    plan = build_plan(manifests)
    write_markdown(plan)
    create_board(plan)
    PLAN_MANIFEST.write_text(json.dumps(plan, indent=2) + "\n")
    print(f"A001 geometry construction plan manifest: {PLAN_MANIFEST}")
    print(f"A001 geometry construction plan doc: {DOC_PATH}")
    print(f"A001 geometry construction plan board: {PLAN_BOARD}")
    print("geometry_generated=False components_moved=False components_assembled=False")


if __name__ == "__main__":
    main()
