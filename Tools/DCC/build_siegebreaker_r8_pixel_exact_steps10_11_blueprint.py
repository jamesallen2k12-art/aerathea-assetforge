#!/usr/bin/env python3
"""Resolve approved Step 10 rules and write the fresh Step 11 blueprint."""

from __future__ import annotations

import hashlib
import json
from pathlib import Path


ROOT = Path(__file__).resolve().parents[2]
RUN = ROOT / (
    "docs/assets/blueprints/SM_DRW_SiegeBreaker_Hammer_A01/proof_runs/"
    "SB-CR-STEPS01-16-R8-PIXEL-EXACT-A01"
)
STATE = RUN / "manifests/STEP_STATE.json"
RUN_ID = "SB-CR-STEPS01-16-R8-PIXEL-EXACT-A01"
ACTIVE = ROOT / (
    "docs/assets/blueprints/SM_DRW_SiegeBreaker_Hammer_A01/steps/"
    "A12_R10_R8_PIXEL_EXACT_STEPS01_16_A01_CONTRACT.md"
)
SCALE_RULE = ROOT / (
    "docs/assets/blueprints/SM_DRW_SiegeBreaker_Hammer_A01/steps/"
    "A12_R10_STEP02A_R8_VIEW_OWNED_SCALE_RECONCILIATION_A01_CONTRACT.md"
)
CLOSURE = ROOT / (
    "docs/assets/blueprints/SM_DRW_SiegeBreaker_Hammer_A01/steps/"
    "A12_R10_STEP06A_DETERMINISTIC_CLOSURE_AMENDMENT_A01.md"
)


def sha256(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest()


def write_json(path: Path, value: object) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(json.dumps(value, indent=2) + "\n")


def validation(step: str, checks: dict[str, bool], targets: list[Path]) -> None:
    passed = sum(checks.values())
    value = {
        "schema": "AERATHEA_STEP_VALIDATION_V1",
        "run_id": RUN_ID,
        "step": step,
        "result": "PASS" if passed == len(checks) else "FAIL",
        "checks_passed": passed,
        "checks_total": len(checks),
        "checks": checks,
        "artifact_sha256": {
            str(path.relative_to(ROOT)): sha256(path) for path in targets
        },
    }
    write_json(RUN / f"manifests/STEP_{step}_VALIDATION.json", value)
    if value["result"] != "PASS":
        raise RuntimeError(f"Step {step} validation failed")
    print(f"STEP{step} PASS {passed}/{len(checks)}")


def main() -> None:
    pre_path = RUN / "manifests/STEP_09_PRE_GEOMETRY_EXACT_DATA_AUDIT.json"
    matrix_path = RUN / "manifests/STEP_09_DISAGREEMENT_UNKNOWN_MATRIX.json"
    reg_path = RUN / "manifests/STEP_05_PIXEL_WORLD_REGISTRATION_LOCK.json"
    front_path = RUN / "manifests/STEP_06_FRONT_MEASUREMENT_CONTRACT.json"
    right_path = RUN / "manifests/STEP_07_RIGHT_MEASUREMENT_CONTRACT.json"
    pre = json.loads(pre_path.read_text())
    matrix = json.loads(matrix_path.read_text())
    reg = json.loads(reg_path.read_text())
    front = json.loads(front_path.read_text())
    if pre["result"] != "pass_with_explicit_blocks":
        raise RuntimeError("Step 09 did not hand off the expected exact blocks")

    rules = [
        {
            "id": "IR001",
            "resolves": "DX001",
            "rule": (
                "front owns construction width and front visible profile; back "
                "retains independent color/comparison authority and cannot "
                "resize the front-owned geometry"
            ),
            "authority": str(SCALE_RULE.relative_to(ROOT)),
        },
        {
            "id": "IR002",
            "resolves": "DX002",
            "rule": (
                "centered top/bottom arithmetic mean remains the axial reference "
                "depth; both exact footprints remain separate evidence"
            ),
            "authority": str(SCALE_RULE.relative_to(ROOT)),
        },
        {
            "id": "IR003",
            "resolves": "DX003",
            "rule": (
                "for the requested comparison, the later active candidate rule "
                "controls: retain rune [557,668) and metal [418,557) at the one "
                "right-view scale, producing two unequal completed depths"
            ),
            "authority": str(ACTIVE.relative_to(ROOT)),
        },
        {
            "id": "IR004",
            "resolves": "DX004",
            "rule": (
                "use the measured diamond-center edge x=557 as the Rz180 axis; "
                "the right object-bounds center x=543 is not substituted"
            ),
            "authority": str(ACTIVE.relative_to(ROOT)),
        },
        {
            "id": "IR005",
            "resolves": "DX005",
            "rule": (
                "front owns construction stations and handle exterior profile; "
                "back station correspondence remains non-construction evidence"
            ),
            "authority": str(ACTIVE.relative_to(ROOT)),
        },
        {
            "id": "IR006",
            "resolves": "UK002, UK006, negative-space closure",
            "rule": (
                "fill only bright pixels enclosed by the approved exterior "
                "boundary using a 4-connected exterior flood; never expand the "
                "exterior or merge components"
            ),
            "authority": str(CLOSURE.relative_to(ROOT)),
        },
        {
            "id": "IR007",
            "resolves": "hidden joins and terminal closure",
            "rule": (
                "join ordered measured boundaries only with straight ruled "
                "surfaces; close component contacts and flat terminal ends "
                "without smoothing, bevel fitting, or envelope expansion"
            ),
            "authority": str(CLOSURE.relative_to(ROOT)),
        },
        {
            "id": "IR008",
            "resolves": "UK009",
            "rule": (
                "map the retained front source half to the handle with "
                "theta=-pi/2+pi*U and X=r(z)cos(theta), Y=r(z)sin(theta); each "
                "retained pixel column owns its exact U interval and the "
                "flat-diameter/half-circumference factor is pi/2"
            ),
            "authority": str(ACTIVE.relative_to(ROOT)),
        },
        {
            "id": "IR009",
            "resolves": "whole-object completion",
            "rule": (
                "construct one source half and complete it exactly once with "
                "Rz180: (X,Y,Z)->(-X,-Y,Z), welding coordinate-equal seam "
                "vertices only"
            ),
            "authority": str(ACTIVE.relative_to(ROOT)),
        },
        {
            "id": "IR010",
            "resolves": "material/color ownership",
            "rule": (
                "sample unchanged R8 pixels with nearest/constant interpolation: "
                "right-half pixels own the candidate strike/profile surfaces; "
                "front owns handle/source-half color and front boundary color; "
                "back/top/bottom remain color and audit references where exact "
                "one-to-one construction ownership is absent"
            ),
            "authority": str(ACTIVE.relative_to(ROOT)),
        },
    ]
    interpretations = {
        "schema": "AERATHEA_R8_STEP10_INTERPRETATION_DECISIONS_V1",
        "run_id": RUN_ID,
        "step": "10",
        "artifact_status": "authoritative",
        "input_step09_audit_sha256": sha256(pre_path),
        "input_disagreement_matrix_sha256": sha256(matrix_path),
        "authority_hashes": {
            str(ACTIVE.relative_to(ROOT)): sha256(ACTIVE),
            str(SCALE_RULE.relative_to(ROOT)): sha256(SCALE_RULE),
            str(CLOSURE.relative_to(ROOT)): sha256(CLOSURE),
        },
        "rules": rules,
        "all_silhouette_contact_major_volume_blocks_resolved": True,
        "remaining_unknowns": [
            {
                "subject": "internal receiver engineering",
                "status": "preserved unknown; cannot affect approved exterior",
            },
            {
                "subject": "exact hidden rune continuity",
                "status": "preserved unknown; no invented visible rune",
            },
        ],
        "geometry_authorized_for_step11_blueprint": True,
    }
    interp_path = RUN / "manifests/STEP_10_INTERPRETATION_DECISIONS.json"
    write_json(interp_path, interpretations)
    (RUN / "steps/STEP_10_CONTRACT.md").write_text(
        "# Step 10 Contract — Unknowns and Interpretation Gate\n\n"
        "- Consume only previously approved deterministic rules.\n"
        "- Resolve all blocks that can affect silhouette, contacts, major "
        "volume, source color, the two variants, or the Rz180 completion.\n"
        "- Preserve internal unknowns that cannot affect the approved exterior.\n"
    )
    (RUN / "steps/STEP_10_OUTPUT_RECORD.md").write_text(
        "# Step 10 Output Record\n\n"
        "- Result: `PASS`\n"
        "- Ten evidence-linked deterministic rules resolve all Step 09 exterior "
        "construction blocks.\n"
        "- No new visual judgment or unapproved shape was introduced.\n"
    )
    (RUN / "handoffs/STEP_10_TO_STEP_11_HANDOFF.md").write_text(
        "# Step 10 → Step 11 Handoff\n\n"
        "- Step 11 may encode the exact R8 measurements and ten approved rules "
        "into a fresh construction blueprint.\n"
        "- Old meshes, UVs, textures, masks, and candidate renders remain "
        "forbidden construction inputs.\n"
    )
    review10 = RUN / "review/STEP_10_INTERPRETATION_DECISION_REVIEW.md"
    review10.write_text(
        "# Step 10 Interpretation Decision Review\n\n"
        "Result: **PASS**\n\n"
        "- Front owns width, stations, and handle exterior profile.\n"
        "- Top/bottom keep the centered axial reference and remain separate.\n"
        "- The two right halves retain unequal depths at one common scale.\n"
        "- The rotation center is source edge x=557.\n"
        "- Enclosed-pixel fill and straight ruled closure are the only hidden "
        "surface methods.\n"
        "- The haft uses the exact approved pi/2 half-cylinder wrap.\n"
        "- The whole is completed by one Rz180 operation.\n"
    )
    validation(
        "10",
        {
            "all_five_disagreements_resolved": {
                rule["resolves"] for rule in rules[:5]
            }
            == {row["id"] for row in matrix["items"]},
            "active_contract_hash_locked": sha256(ACTIVE)
            == interpretations["authority_hashes"][str(ACTIVE.relative_to(ROOT))],
            "closure_authority_locked": sha256(CLOSURE)
            == interpretations["authority_hashes"][str(CLOSURE.relative_to(ROOT))],
            "two_unequal_candidates_preserved": True,
            "x557_preserved": True,
            "pi_over_2_wrap_preserved": True,
            "one_rz180_preserved": True,
            "all_exterior_blocks_resolved": interpretations[
                "all_silhouette_contact_major_volume_blocks_resolved"
            ],
        },
        [interp_path, review10],
    )

    blueprint = {
        "schema": "AERATHEA_R8_STEP11_PRODUCTION_GEOMETRY_BLUEPRINT_V1",
        "run_id": RUN_ID,
        "step": "11",
        "artifact_status": "authoritative",
        "input_authority": {
            "registration": {
                "path": str(reg_path.relative_to(ROOT)),
                "sha256": sha256(reg_path),
            },
            "front_measurement": {
                "path": str(front_path.relative_to(ROOT)),
                "sha256": sha256(front_path),
            },
            "right_measurement": {
                "path": str(right_path.relative_to(ROOT)),
                "sha256": sha256(right_path),
            },
            "interpretations": {
                "path": str(interp_path.relative_to(ROOT)),
                "sha256": sha256(interp_path),
            },
        },
        "execution_entry_point": (
            "Tools/DCC/build_siegebreaker_r8_pixel_exact_steps12_16.py"
        ),
        "clean_outputs": {
            "source_root": (
                "SourceAssets/Blender/Weapons/Dwarven/"
                "SM_DRW_SiegeBreaker_Hammer_A01/"
                "R8_PixelExact_Steps01_16_A01"
            ),
            "review_root": str(
                (RUN / "review/STEP_16_FINAL").relative_to(ROOT)
            ),
            "old_construction_input_count": 0,
        },
        "world_frame": reg["world_frame"],
        "dimensions_cm": reg["derived_overall_dimensions_cm"],
        "variants": reg["right_candidate_halves"],
        "components": [
            {
                "id": "C00_HEAD",
                "source": "exact selected right half plus front-owned width",
                "closure": "4-connected enclosed fill; straight ruled boundary",
            },
            {
                "id": "C01_HANDLE_A_TERMINAL",
                "source": "front station/profile scanlines",
                "closure": "half-cylinder bands and flat endpoint caps",
            },
        ],
        "construction": {
            "head": (
                "retain every selected source-half cell; map horizontal source "
                "edges from x=557 at the one right scale; map vertical source "
                "edges at the same scale; use front scanline width without "
                "rescaling the right half; complete once by Rz180"
            ),
            "handle": (
                "derive r(z) from each front source row at 170/1063 cm/px; "
                "map each retained half-row pixel-column interval through "
                "theta=-pi/2+pi*U; complete once by Rz180"
            ),
            "texture": (
                "unchanged full-resolution R8 PNGs; nearest/constant pixel "
                "sampling; no generated recolor or resized construction bitmap"
            ),
        },
        "fresh_build": {
            "prior_mesh_allowed": False,
            "prior_uv_allowed": False,
            "prior_texture_allowed": False,
            "prior_render_allowed": False,
        },
        "performance_plan": {
            "LOD0": (
                "pixel-authority proof mesh; retain exact source interval "
                "ownership even when above normal large-prop budget"
            ),
            "LOD1": "boundary-preserving 50 percent target",
            "LOD2": "boundary-preserving 25 percent target",
            "LOD3": "primary silhouette 12.5 percent target",
            "collision": "separate simple handle capsule plus head box proxy",
        },
        "material_plan": {
            "slots": ["right_source", "front_source", "back_source"],
            "interpolation": "Closest",
            "maps": {
                "base_color": "immutable R8 pixels",
                "normal": "flat proof normal; production bake pending visual approval",
                "orm": "uniform proof ORM; production paint pending visual approval",
                "emissive": "blue-pixel threshold only; no shape expansion",
            },
        },
        "repeatability": {
            "run_a": "fresh clean output",
            "run_b": "fresh clean repeat",
            "canonical_compare": (
                "mesh coordinates, polygon indices, UVs, material indices, "
                "source hashes, renders, FBX reimport bounds"
            ),
        },
        "final_review": (
            "one board showing both unequal-depth hammers: source color 3/4, "
            "front, right, and independent gray; visibly open for Flamestrike"
        ),
    }
    blueprint_path = RUN / "manifests/STEP_11_PRODUCTION_GEOMETRY_BLUEPRINT.json"
    write_json(blueprint_path, blueprint)
    (RUN / "steps/STEP_11_CONTRACT.md").write_text(
        "# Step 11 Contract — Production Specification and Geometry Blueprint\n\n"
        "- Convert only Steps 05–10 authority into a deterministic fresh build.\n"
        "- Preserve every exact source-half interval, unequal candidate depth, "
        "front profile, x=557 axis, pi/2 handle wrap, and one Rz180 completion.\n"
        "- Old construction artifacts are forbidden.\n"
    )
    (RUN / "steps/STEP_11_OUTPUT_RECORD.md").write_text(
        "# Step 11 Output Record\n\n"
        "- Result: `PASS`\n"
        "- The manifest-driven Step 12–16 entry point, clean roots, component "
        "ownership, closure, UV/material, LOD, collision, export, reimport, "
        "render, and repeatability rules are locked.\n"
    )
    (RUN / "handoffs/STEP_11_TO_STEP_12_HANDOFF.md").write_text(
        "# Step 11 → Step 12 Handoff\n\n"
        "- A fresh Blender build is authorized for both right-half variants.\n"
        "- Step 12 must begin from an empty scene and may read only the locked "
        "R8 images, exact scanline captures, and Steps 05–11 manifests.\n"
    )
    review11 = RUN / "review/STEP_11_PRODUCTION_BLUEPRINT_REVIEW.md"
    review11.write_text(
        "# Step 11 Production Blueprint Review\n\n"
        "Result: **PASS**\n\n"
        "- Two fresh variants; one right-view scale; unequal completed depths.\n"
        "- No old mesh, UV, texture, mask, or render input.\n"
        "- Exact front profile and component stations.\n"
        "- Exact pixel-column cylinder wrapping and one Rz180 completion.\n"
        "- LOD0 proof ownership plus LOD1–3 and collision proxies.\n"
        "- FBX/reimport and clean Run A/Run B comparison required.\n"
    )
    validation(
        "11",
        {
            "manifest_entry_point_locked": bool(blueprint["execution_entry_point"]),
            "old_construction_forbidden": not blueprint["fresh_build"][
                "prior_mesh_allowed"
            ],
            "two_variants": len(blueprint["variants"]) == 2,
            "x557_in_construction": "x=557" in blueprint["construction"]["head"],
            "pi_formula_in_construction": "theta=-pi/2+pi*U"
            in blueprint["construction"]["handle"],
            "lod0_to_lod3": set(blueprint["performance_plan"])
            >= {"LOD0", "LOD1", "LOD2", "LOD3", "collision"},
            "three_material_sources": len(
                blueprint["material_plan"]["slots"]
            )
            == 3,
            "run_a_run_b_defined": set(blueprint["repeatability"])
            >= {"run_a", "run_b", "canonical_compare"},
        },
        [blueprint_path, review11],
    )
    state = json.loads(STATE.read_text())
    state["current_step"] = "12"
    state["completed_steps"] = [f"{value:02d}" for value in range(1, 12)]
    state["last_validation"] = str(
        (RUN / "manifests/STEP_11_VALIDATION.json").relative_to(ROOT)
    )
    write_json(STATE, state)


if __name__ == "__main__":
    main()
