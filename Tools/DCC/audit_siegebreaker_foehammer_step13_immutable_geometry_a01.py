#!/usr/bin/env python3
"""Step 13 read-only saved-geometry audit for the approved Dwarven hammer twins.

The script is deliberately independent of the builder.  It opens the two
locked .blend sources, observes their saved mesh data, and writes one Step 13
technical evidence record.  It never invokes a Blender save operator.
"""

from __future__ import annotations

import argparse
import hashlib
import json
import math
import os
import struct
import subprocess
import sys
from collections import Counter, defaultdict
from datetime import datetime, timezone
from fractions import Fraction
from pathlib import Path
from typing import Any


ROOT = Path(__file__).resolve().parents[2]
RUN_ID = "SB-CR-STEPS10-16-R8-ZERO-EXTRUSION-A02"
BUILD_ID = "FRESH_TWIN_DCC_SOURCE_BUILDER_A01"
STEP_ID = "STEP_13_IMMUTABLE_GEOMETRY_ARTISTIC_REVIEW_A01"
PROOF_ROOT = ROOT / (
    "docs/assets/blueprints/SM_DRW_SiegeBreaker_Hammer_A01/proof_runs/"
    "SB-CR-STEPS10-16-R8-ZERO-EXTRUSION-A02"
)
TECHNICAL_AUDIT = (
    PROOF_ROOT
    / "manifests"
    / f"{STEP_ID}_TECHNICAL_AUDIT.json"
)
BLENDER = ROOT / "Tools/External/Blender/blender-4.5.11-linux-x64/blender"

PLAN = ROOT / (
    "docs/assets/blueprints/SM_DRW_SiegeBreaker_Hammer_A01/"
    "SM_DRW_SiegeBreaker_Hammer_A01_STEPS_01_16_PROOF_OF_CONCEPT_PIPELINE_PLAN.md"
)
CONTRACT = PROOF_ROOT / "steps" / f"{STEP_ID}_CONTRACT.md"
STEP_STATE = PROOF_ROOT / "manifests/STEP_STATE.json"
BLUEPRINT = PROOF_ROOT / "manifests/SHARED_DEPTH_RECOVERY_BLUEPRINT_A01.json"
BLUEPRINT_LOCK = (
    PROOF_ROOT
    / "manifests/SHARED_DEPTH_RECOVERY_BLUEPRINT_A01_AUTHORITY_LOCK.json"
)
PERFORMANCE_AMENDMENT = (
    PROOF_ROOT
    / "steps/STEP_11B_HIGH_POLY_NANITE_PERFORMANCE_AMENDMENT_A01.md"
)
BUILDER_APPROVAL = (
    PROOF_ROOT / "steps/FRESH_TWIN_DCC_SOURCE_BUILDER_A01_APPROVAL_RECORD.md"
)
BUILDER_OUTPUT = (
    PROOF_ROOT / "steps/FRESH_TWIN_DCC_SOURCE_BUILDER_A01_OUTPUT_RECORD.md"
)
BUILDER_MANIFEST = (
    PROOF_ROOT / "manifests/FRESH_TWIN_DCC_SOURCE_BUILDER_A01_MANIFEST.json"
)
PRIOR_AUDIT = (
    PROOF_ROOT
    / "manifests/FRESH_TWIN_DCC_SOURCE_BUILDER_A01_INDEPENDENT_AUDIT.json"
)
VISUAL_APPROVAL = (
    PROOF_ROOT
    / "steps/FRESH_TWIN_DCC_SOURCE_BUILDER_A01_VISUAL_DECISION_APPROVAL_RECORD.md"
)
FOE_IDENTITY = ROOT / (
    "docs/assets/blueprints/SM_DRW_FoeHammer_Hammer_A01/"
    "SM_DRW_FoeHammer_Hammer_A01_IDENTITY_AND_RESUME_STATE.md"
)
OWNERSHIP_INDEX = ROOT / (
    "docs/assets/blueprints/SM_DRW_SiegeBreaker_Hammer_A01/proof_runs/"
    "SB-CR-R8-STEP09A-COMPONENT-PIXEL-OWNERSHIP-A01/manifests/"
    "STEP_09A_BOUNDARY_AND_CORRESPONDENCE_INDEX.json"
)

EXPECTED_DIMENSIONS = (
    Fraction(50719500, 517681),
    Fraction(6644212, 149985),
    Fraction(170, 1),
)
COMMON_HALF_DEPTH = Fraction(3322106, 149985)
EXPECTED_BUILDER_SHARED_HASH = (
    "ac0d08252ee71166842779bfb85904c4378ff1a9a4b8328d82dfac9c914e8049"
)
EXPECTED_SAVED_SHARED_HASH = (
    "f03b975b03141204b4a3c061306d8f48f8668e2a2bdcd214d1f72f555efe86c4"
)
PRIOR_APPROVED_FLOAT32_ENCODING_TOLERANCE_CM = 2.0e-5
SUPERSEDED_AUDIT_RECORD = {
    "technical_audit_sha256": (
        "c89210db6fe5ee19e528bdec9c4f4ad8c38b4c5723c74b3d6dfaa0fffc127d0f"
    ),
    "auditor_sha256": (
        "e7870555132e0ff9214f6edafaa0cd2bbfc626f3648fd3361db33b65f2fced98"
    ),
    "result": "FAIL",
    "classification": "superseded proof only",
    "correction": (
        "The first pass incorrectly required the Foe Hammer visible C04 owner "
        "pixels to fill its approved registration interval. The locked prior "
        "audit explicitly records that the interval is registration, not fill. "
        "The correction changes that check only; topology/contact failures and "
        "unchanged source hashes remain independently observed."
    ),
}

AUTHORITIES = {
    CONTRACT: "cc5b3185c851a229f44428b4544a19c490025095fcae2b5313fc3f5ae3f5d74b",
    PLAN: "53046eb839b94d9548dfc2e49471b3605a2fc882228ca5e4291db7390e584a2a",
    BLUEPRINT: "efdbd8795dff2031fcde9e734868ff4c617dc37ad1e7b3743c3727daea981d58",
    BLUEPRINT_LOCK: "6889b826481e5e11dd10775f2b81467b1014687b7fda9ebbff62d519bfff09bc",
    PERFORMANCE_AMENDMENT: "2e4276ea0adc32d8c6a21fb5bfbd46eacf627a9708c6187e56be1556eee76ba6",
    BUILDER_APPROVAL: "8b59685cf27656805ecf73385ab980c1d96dec2686ac1928f6f547f4dad787ef",
    BUILDER_OUTPUT: "6cc72297048abbef35ad2893396effbff8101bc196a304e14544ceb1d7cb7533",
    BUILDER_MANIFEST: "6e77b264cfceb9233f2f8b4ae8a9844a53069d8bcf724bd6b0699b8416181350",
    PRIOR_AUDIT: "f2c5434a61b15dcbb616a3c10c23bef0f91f62f4966d46b6d758dbc8dc9cc285",
    VISUAL_APPROVAL: "3ae3e8a823262870e3ea01cc4b33a470d68d3b5b7d8fe49049315d68e6c66eb7",
    FOE_IDENTITY: "63c17d6fbd5f27d6487b40ba163d6721bbfeb69a2bc46cee26453433f16e1944",
    BLENDER: "dc72290ee8651c93c4a946c012c5f2a034946fd320e6c3ab214fa23181427428",
}

ASSETS = {
    "siege_breaker": {
        "asset_id": "SM_DRW_SiegeBreaker_Hammer_A01",
        "display_name": "Siege Breaker",
        "variant": "rune_side",
        "completed_face_rule": "double rune sided",
        "local_half": Fraction(9435, 548),
        "source_interval": [557, 668],
        "source_owner": "OWN_RIGHT_C04_RUNE",
        "blend": ROOT / (
            "SourceAssets/Blender/Weapons/Dwarven/"
            "SM_DRW_SiegeBreaker_Hammer_A01/"
            "A12_R10_R8_SharedDepth_DCCSource_A01/"
            "SM_DRW_SiegeBreaker_Hammer_A01_DCCSource_SharedDepth_A01.blend"
        ),
        "manifest": ROOT / (
            "SourceAssets/Blender/Weapons/Dwarven/"
            "SM_DRW_SiegeBreaker_Hammer_A01/"
            "A12_R10_R8_SharedDepth_DCCSource_A01/build_manifest.json"
        ),
        "prior_saved_audit": ROOT / (
            "SourceAssets/Blender/Weapons/Dwarven/"
            "SM_DRW_SiegeBreaker_Hammer_A01/"
            "A12_R10_R8_SharedDepth_DCCSource_A01/"
            "independent_saved_file_audit.json"
        ),
        "sha256": "c69b415ac3429091c6aa77d24ffcd6d88bbd0f9fc711e3862c2c7e7b51034537",
    },
    "foe_hammer": {
        "asset_id": "SM_DRW_FoeHammer_Hammer_A01",
        "display_name": "Foe Hammer",
        "variant": "metal_center_piece_side",
        "completed_face_rule": "double metal-center-piece sided",
        "local_half": Fraction(11815, 548),
        "source_interval": [418, 557],
        "source_owner": "OWN_RIGHT_C04_METAL",
        "blend": ROOT / (
            "SourceAssets/Blender/Weapons/Dwarven/"
            "SM_DRW_FoeHammer_Hammer_A01/"
            "A12_R10_R8_SharedDepth_DCCSource_A01/"
            "SM_DRW_FoeHammer_Hammer_A01_DCCSource_SharedDepth_A01.blend"
        ),
        "manifest": ROOT / (
            "SourceAssets/Blender/Weapons/Dwarven/"
            "SM_DRW_FoeHammer_Hammer_A01/"
            "A12_R10_R8_SharedDepth_DCCSource_A01/build_manifest.json"
        ),
        "prior_saved_audit": ROOT / (
            "SourceAssets/Blender/Weapons/Dwarven/"
            "SM_DRW_FoeHammer_Hammer_A01/"
            "A12_R10_R8_SharedDepth_DCCSource_A01/"
            "independent_saved_file_audit.json"
        ),
        "sha256": "67737a3c561cd6462af3657ea93488af76f32a5815ee0b4d5887182d14c761d4",
    },
}

FORBIDDEN_GEOMETRY_MARKERS = (
    "bounding_box",
    "bbox",
    "footprint",
    "interval_rectangle",
    "backing_plate",
    "facade",
    "projection_fill",
    "projection_carrier",
    "detached_shell",
)


def utc_now() -> str:
    return datetime.now(timezone.utc).isoformat()


def sha256(path: Path) -> str:
    digest = hashlib.sha256()
    with path.open("rb") as handle:
        for block in iter(lambda: handle.read(1024 * 1024), b""):
            digest.update(block)
    return digest.hexdigest()


def relative(path: Path) -> str:
    return str(path.resolve().relative_to(ROOT))


def load_json(path: Path) -> dict[str, Any]:
    return json.loads(path.read_text(encoding="utf-8"))


def write_json(path: Path, value: Any) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(
        json.dumps(value, indent=2, sort_keys=True) + "\n",
        encoding="utf-8",
    )


def qstr(value: Fraction) -> str:
    return f"{value.numerator}/{value.denominator}"


def f32(value: float) -> float:
    return struct.unpack(">f", struct.pack(">f", value))[0]


def coordinate_bytes(point: tuple[float, float, float]) -> bytes:
    return struct.pack(">ddd", *point)


def custom_properties(owner: Any) -> dict[str, Any]:
    return {
        key: owner[key]
        for key in owner.keys()
        if key != "_RNA_UI"
    }


def verify_authorities() -> list[dict[str, Any]]:
    records: list[dict[str, Any]] = []
    for path, expected in AUTHORITIES.items():
        observed = sha256(path) if path.is_file() else None
        result = "PASS" if observed == expected else "FAIL"
        records.append(
            {
                "path": relative(path),
                "expected_sha256": expected,
                "observed_sha256": observed,
                "result": result,
            }
        )
        if result != "PASS":
            raise RuntimeError(f"Authority hash mismatch: {relative(path)}")

    state = load_json(STEP_STATE)
    contract_state = state.get("step_13_contract_candidate", {})
    state_checks = {
        "contract_hash_matches": contract_state.get("sha256")
        == AUTHORITIES[CONTRACT],
        "flamestrike_contract_decision_approved": contract_state.get(
            "flamestrike_contract_decision"
        )
        == "approved",
        "step_13_execution_authority_true": bool(
            contract_state.get("step_13_execution_authority")
        ),
        "read_only_blender_authority_true": bool(
            contract_state.get("blender_read_only_audit_and_render_authority")
        ),
        "geometry_modification_authority_false": not bool(
            contract_state.get("geometry_modification_authority")
        ),
        "downstream_production_authority_false": not bool(
            contract_state.get("downstream_production_authority")
        ),
        "unreal_authority_false": not bool(
            contract_state.get("unreal_authority")
        ),
    }
    records.append(
        {
            "path": relative(STEP_STATE),
            "observed_sha256": sha256(STEP_STATE),
            "checks": state_checks,
            "result": "PASS" if all(state_checks.values()) else "FAIL",
        }
    )
    if not all(state_checks.values()):
        raise RuntimeError("STEP_STATE does not authorize the exact read-only audit")

    prior = load_json(PRIOR_AUDIT)
    for asset_key, asset in ASSETS.items():
        prior_path = asset["prior_saved_audit"]
        expected = prior["asset_audits"][asset_key]["sha256"]
        observed = sha256(prior_path)
        prior_value = load_json(prior_path)
        tolerance = prior_value["observed_saved_mesh_bounds_cm"][
            "encoding_tolerance_cm"
        ]
        passed = (
            observed == expected
            and prior_value["result"] == "PASS"
            and tolerance == PRIOR_APPROVED_FLOAT32_ENCODING_TOLERANCE_CM
        )
        records.append(
            {
                "path": relative(prior_path),
                "expected_sha256": expected,
                "observed_sha256": observed,
                "locked_float32_encoding_tolerance_cm": tolerance,
                "tolerance_authority": relative(PRIOR_AUDIT),
                "result": "PASS" if passed else "FAIL",
            }
        )
        if not passed:
            raise RuntimeError(f"Prior saved audit lock mismatch: {asset_key}")
    return records


def mesh_world_vertices(obj: Any) -> list[tuple[float, float, float]]:
    return [
        tuple(float(value) for value in (obj.matrix_world @ vertex.co))
        for vertex in obj.data.vertices
    ]


def object_canonical_hash(
    obj: Any, world_points: list[tuple[float, float, float]]
) -> str:
    digest = hashlib.sha256()
    digest.update(obj.name.encode("utf-8") + b"\0")
    for key in (
        "Aerathea.Component",
        "Aerathea.SourceOwner",
        "Aerathea.EquationId",
        "Aerathea.Occurrence",
        "Aerathea.VariantLocalC04",
    ):
        digest.update(
            (key + "=" + str(obj.get(key, "")) + "\n").encode("utf-8")
        )
    for point in world_points:
        digest.update(coordinate_bytes(point))
    for polygon in obj.data.polygons:
        digest.update(struct.pack(">I", len(polygon.vertices)))
        for index in polygon.vertices:
            digest.update(struct.pack(">I", int(index)))
    materials = [
        (
            slot.material.name if slot.material else "",
            tuple(slot.material.diffuse_color) if slot.material else (),
        )
        for slot in obj.material_slots
    ]
    digest.update(repr(materials).encode("utf-8"))
    return digest.hexdigest()


def saved_shared_base_hash(
    objects: list[Any],
    world_points_by_object: dict[str, list[tuple[float, float, float]]],
) -> str:
    digest = hashlib.sha256()
    for obj in sorted(
        (
            item
            for item in objects
            if not bool(item.get("Aerathea.VariantLocalC04", False))
        ),
        key=lambda item: item.name,
    ):
        digest.update(obj.name.encode("utf-8") + b"\0")
        for key in (
            "Aerathea.Component",
            "Aerathea.SourceOwner",
            "Aerathea.EquationId",
            "Aerathea.Occurrence",
        ):
            digest.update(
                (key + "=" + str(obj.get(key, "")) + "\n").encode("utf-8")
            )
        for point in world_points_by_object[obj.name]:
            digest.update(struct.pack(">ddd", *point))
        for polygon in obj.data.polygons:
            digest.update(struct.pack(">I", len(polygon.vertices)))
            for index in polygon.vertices:
                digest.update(struct.pack(">I", int(index)))
        materials = [
            (
                slot.material.name if slot.material else "",
                tuple(slot.material.diffuse_color)
                if slot.material
                else (),
            )
            for slot in obj.material_slots
        ]
        digest.update(repr(materials).encode("utf-8"))
    return digest.hexdigest()


def authorized_surface_records(manifest: dict[str, Any]) -> dict[str, dict[str, Any]]:
    records = (
        manifest["shared_base"]["report"]["surface_provenance"]
        + manifest["variant_report"]["surface_provenance"]
    )
    return {record["record"]: record for record in records}


def base_record_name(name: str) -> str:
    return name.removesuffix("__RZ180")


def analyze_topology(
    objects: list[Any],
    world_points_by_object: dict[str, list[tuple[float, float, float]]],
) -> dict[str, Any]:
    import bmesh

    object_records: list[dict[str, Any]] = []
    assembly_boundary: dict[
        tuple[bytes, bytes], list[tuple[str, str, int]]
    ] = defaultdict(list)
    global_face_digests: dict[bytes, tuple[str, int]] = {}
    cross_object_duplicate_face_count = 0
    cross_object_duplicate_face_examples: list[dict[str, Any]] = []
    total_signed_volume = 0.0

    for obj in objects:
        bm = bmesh.new()
        bm.from_mesh(obj.data)
        bm.verts.ensure_lookup_table()
        bm.edges.ensure_lookup_table()
        bm.faces.ensure_lookup_table()
        bm.verts.index_update()
        bm.faces.index_update()
        bm.normal_update()
        points = world_points_by_object[obj.name]
        point_keys = [coordinate_bytes(point) for point in points]

        loose_edges = 0
        boundary_edges = 0
        nonmanifold_edges = 0
        winding_mismatch_edges = 0
        winding_mismatch_examples: list[dict[str, Any]] = []
        zero_area_faces = 0
        degenerate_faces = 0
        duplicate_faces = 0
        local_face_signatures: set[tuple[int, ...]] = set()
        signed_volume = 0.0

        for edge in bm.edges:
            linked = len(edge.link_faces)
            if linked == 0:
                loose_edges += 1
            elif linked == 1:
                boundary_edges += 1
                loop = edge.link_loops[0]
                start = point_keys[loop.vert.index]
                end = point_keys[loop.link_loop_next.vert.index]
                if start <= end:
                    key = (start, end)
                    direction = 1
                else:
                    key = (end, start)
                    direction = -1
                assembly_boundary[key].append(
                    (
                        obj.name,
                        str(obj.get("Aerathea.Component", "")),
                        direction,
                    )
                )
            elif linked > 2:
                nonmanifold_edges += 1
            elif not edge.is_contiguous:
                winding_mismatch_edges += 1
                if len(winding_mismatch_examples) < 20:
                    winding_mismatch_examples.append(
                        {
                            "edge_index": edge.index,
                            "face_indices": [
                                face.index for face in edge.link_faces
                            ],
                            "face_normal_dot": float(
                                edge.link_faces[0].normal.dot(
                                    edge.link_faces[1].normal
                                )
                            ),
                            "endpoints_cm": [
                                list(points[vertex.index])
                                for vertex in edge.verts
                            ],
                        }
                    )

        for face in bm.faces:
            area = float(face.calc_area())
            if area == 0.0:
                zero_area_faces += 1
            indices = tuple(sorted(vertex.index for vertex in face.verts))
            if len(set(indices)) < 3:
                degenerate_faces += 1
            if indices in local_face_signatures:
                duplicate_faces += 1
            else:
                local_face_signatures.add(indices)

            canonical_coordinates = b"".join(
                sorted(point_keys[vertex.index] for vertex in face.verts)
            )
            face_digest = hashlib.sha256(canonical_coordinates).digest()
            if face_digest in global_face_digests:
                other_object, other_face = global_face_digests[face_digest]
                cross_object_duplicate_face_count += 1
                if len(cross_object_duplicate_face_examples) < 20:
                    cross_object_duplicate_face_examples.append(
                        {
                            "object_a": other_object,
                            "face_a": other_face,
                            "object_b": obj.name,
                            "face_b": face.index,
                            "sha256": face_digest.hex(),
                        }
                    )
            else:
                global_face_digests[face_digest] = (obj.name, face.index)

            if len(face.verts) >= 3:
                p0 = obj.matrix_world @ face.verts[0].co
                for index in range(1, len(face.verts) - 1):
                    p1 = obj.matrix_world @ face.verts[index].co
                    p2 = obj.matrix_world @ face.verts[index + 1].co
                    signed_volume += float(p0.dot(p1.cross(p2))) / 6.0

        total_signed_volume += signed_volume
        surface_patch_pass = (
            loose_edges == 0
            and nonmanifold_edges == 0
            and winding_mismatch_edges == 0
            and zero_area_faces == 0
            and degenerate_faces == 0
            and duplicate_faces == 0
        )
        object_records.append(
            {
                "object": obj.name,
                "component": obj.get("Aerathea.Component"),
                "equation_id": obj.get("Aerathea.EquationId"),
                "topology_role": (
                    "authoritative source-owned surface patch; exact assembled "
                    "closure is the closed-volume gate"
                ),
                "vertices": len(bm.verts),
                "edges": len(bm.edges),
                "faces": len(bm.faces),
                "boundary_edges": boundary_edges,
                "loose_edges": loose_edges,
                "nonmanifold_edges_more_than_two_faces": nonmanifold_edges,
                "winding_mismatch_edges": winding_mismatch_edges,
                "winding_mismatch_examples": winding_mismatch_examples,
                "zero_area_faces_exact": zero_area_faces,
                "degenerate_faces": degenerate_faces,
                "duplicate_faces_within_object": duplicate_faces,
                "individual_object_closed": boundary_edges == 0,
                "individual_signed_volume_cm3": signed_volume,
                "surface_patch_topology_result": (
                    "PASS" if surface_patch_pass else "FAIL"
                ),
            }
        )
        bm.free()

    open_seams = 0
    nonmanifold_seams = 0
    seam_winding_mismatches = 0
    seam_incidence = Counter()
    seam_pair_counts: Counter[tuple[str, str]] = Counter()
    for participants in assembly_boundary.values():
        incidence = len(participants)
        seam_incidence[incidence] += 1
        if incidence < 2:
            open_seams += 1
        elif incidence > 2:
            nonmanifold_seams += 1
        else:
            if participants[0][2] + participants[1][2] != 0:
                seam_winding_mismatches += 1
            pair = tuple(
                sorted((participants[0][1], participants[1][1]))
            )
            seam_pair_counts[pair] += 1

    every_patch_clean = all(
        item["surface_patch_topology_result"] == "PASS"
        for item in object_records
    )
    assembled_closed_manifold = (
        every_patch_clean
        and open_seams == 0
        and nonmanifold_seams == 0
        and seam_winding_mismatches == 0
        and cross_object_duplicate_face_count == 0
        and total_signed_volume != 0.0
        and math.isfinite(total_signed_volume)
    )
    return {
        "interpretation_basis": (
            "The locked build stores each source-owned surface instruction as "
            "a mesh object. Every object is audited as a surface patch; exact "
            "world-coordinate boundary incidence across all authorized patches "
            "is the closed/manifold-volume decision."
        ),
        "object_results": object_records,
        "every_object_surface_patch_topology_pass": every_patch_clean,
        "assembly_boundary_edge_incidence_histogram": {
            str(key): value for key, value in sorted(seam_incidence.items())
        },
        "assembly_open_boundary_edges": open_seams,
        "assembly_nonmanifold_boundary_edges": nonmanifold_seams,
        "assembly_boundary_winding_mismatches": seam_winding_mismatches,
        "cross_object_duplicate_face_count": cross_object_duplicate_face_count,
        "cross_object_duplicate_face_examples": (
            cross_object_duplicate_face_examples
        ),
        "assembly_signed_volume_cm3": total_signed_volume,
        "assembly_closed_manifold_volume": assembled_closed_manifold,
        "exact_seam_component_pair_counts": [
            {
                "component_a": pair[0],
                "component_b": pair[1],
                "exact_shared_boundary_edge_count": count,
            }
            for pair, count in sorted(seam_pair_counts.items())
        ],
        "_assembly_boundary": assembly_boundary,
    }


def declared_contact_audit(
    manifest: dict[str, Any],
    objects: list[Any],
    assembly_boundary: dict[
        tuple[bytes, bytes], list[tuple[str, str, int]]
    ],
) -> dict[str, Any]:
    by_name = {obj.name: obj for obj in objects}
    transitions = manifest["shared_base"]["report"]["transition_report"]
    records: list[dict[str, Any]] = []
    for transition in transitions:
        lower = transition["lower_component"]
        upper = transition["upper_component"]
        expected_z = f32(float(Fraction(transition["world_z_exact"])))
        matched_edges = 0
        for key, participants in assembly_boundary.items():
            if len(participants) != 2:
                continue
            start_z = struct.unpack(">ddd", key[0])[2]
            end_z = struct.unpack(">ddd", key[1])[2]
            components = {participants[0][1], participants[1][1]}
            if (
                start_z == expected_z
                and end_z == expected_z
                and lower in components
                and upper in components
            ):
                matched_edges += 1

        contact_object_checks: list[dict[str, Any]] = []
        if transition["faces"] > 0:
            base = f"CONTACT_{upper}_TO_{lower}"
            for name in (base, base + "__RZ180"):
                obj = by_name.get(name)
                passed = (
                    obj is not None
                    and len(obj.data.polygons) == transition["faces"]
                    and obj.get("Aerathea.EquationId")
                    == "EQ_EXACT_PLANAR_HALF_ANNULAR_SHOULDER"
                )
                contact_object_checks.append(
                    {
                        "object": name,
                        "observed_faces": (
                            len(obj.data.polygons) if obj else None
                        ),
                        "expected_faces": transition["faces"],
                        "result": "PASS" if passed else "FAIL",
                    }
                )
            passed = all(
                item["result"] == "PASS" for item in contact_object_checks
            )
        else:
            passed = matched_edges > 0
        records.append(
            {
                **transition,
                "expected_world_z_float32_cm": expected_z,
                "direct_exact_shared_boundary_edge_count": matched_edges,
                "contact_objects": contact_object_checks,
                "result": "PASS" if passed else "FAIL",
            }
        )
    return {
        "declared_transition_count": len(records),
        "records": records,
        "result": (
            "PASS"
            if records and all(item["result"] == "PASS" for item in records)
            else "FAIL"
        ),
    }


def protected_negative_space_authority() -> dict[str, Any]:
    index = load_json(OWNERSHIP_INDEX)
    boundary_records = index["boundaries"]
    protected_samples = 0
    protected_runs = 0
    protected_pixel_span = 0
    protected_boundary_ids: list[str] = []
    for boundary_id, boundary in boundary_records.items():
        boundary_has_gap = False
        for sample in boundary.get("samples", []):
            runs = sample.get("protected_runs_half_open", [])
            if sample.get("mode") == "protected_gap" or runs:
                protected_samples += 1
                protected_runs += len(runs)
                protected_pixel_span += sum(
                    int(end) - int(start) for start, end in runs
                )
                boundary_has_gap = True
        if boundary_has_gap:
            protected_boundary_ids.append(boundary_id)
    return {
        "authority_path": relative(OWNERSHIP_INDEX),
        "authority_sha256": sha256(OWNERSHIP_INDEX),
        "protected_boundary_ids": protected_boundary_ids,
        "protected_sample_count": protected_samples,
        "protected_run_count": protected_runs,
        "protected_pixel_span_sum": protected_pixel_span,
        "direct_saved_geometry_preservation_test": (
            "PASS only when every saved surface identity and provenance record "
            "matches the authorized owner-cell manifest, no extra or forbidden "
            "fill object exists, and the exact assembled topology closes only "
            "through declared surface/contact/closure identities."
        ),
    }


def inspect_loaded_asset(
    bpy: Any,
    asset: dict[str, Any],
    source_hash_before: str,
) -> dict[str, Any]:
    scene = bpy.context.scene
    objects = sorted(
        (obj for obj in bpy.data.objects if obj.type == "MESH"),
        key=lambda item: item.name,
    )
    if not objects:
        raise RuntimeError("Saved source has no mesh objects")

    manifest = load_json(asset["manifest"])
    authorized = authorized_surface_records(manifest)
    world_points_by_object = {
        obj.name: mesh_world_vertices(obj) for obj in objects
    }
    all_points = [
        point
        for obj in objects
        for point in world_points_by_object[obj.name]
    ]
    minimum = [
        min(point[axis] for point in all_points) for axis in range(3)
    ]
    maximum = [
        max(point[axis] for point in all_points) for axis in range(3)
    ]
    dimensions = [
        maximum[axis] - minimum[axis] for axis in range(3)
    ]
    expected_decimal = [float(value) for value in EXPECTED_DIMENSIONS]
    residuals = [
        dimensions[axis] - expected_decimal[axis] for axis in range(3)
    ]
    prior_tolerance_pass = all(
        abs(value) <= PRIOR_APPROVED_FLOAT32_ENCODING_TOLERANCE_CM
        for value in residuals
    )

    topology = analyze_topology(objects, world_points_by_object)
    assembly_boundary = topology.pop("_assembly_boundary")
    contact_audit = declared_contact_audit(
        manifest, objects, assembly_boundary
    )

    unauthorized_objects: list[str] = []
    provenance_mismatches: list[dict[str, Any]] = []
    forbidden_hits: list[dict[str, str]] = []
    object_hashes: dict[str, str] = {}
    for obj in objects:
        base = base_record_name(obj.name)
        record = authorized.get(base)
        if record is None:
            unauthorized_objects.append(obj.name)
        else:
            observed = {
                "source_owner": obj.get("Aerathea.SourceOwner"),
                "equation_id": obj.get("Aerathea.EquationId"),
            }
            expected = {
                "source_owner": record["source_owner"],
                "equation_id": record["equation_id"],
            }
            if observed != expected:
                provenance_mismatches.append(
                    {
                        "object": obj.name,
                        "expected": expected,
                        "observed": observed,
                    }
                )
        serialized = json.dumps(
            {
                "name": obj.name,
                "properties": custom_properties(obj),
            },
            sort_keys=True,
            default=str,
        ).lower()
        for marker in FORBIDDEN_GEOMETRY_MARKERS:
            if marker in serialized:
                forbidden_hits.append(
                    {"object": obj.name, "marker": marker}
                )
        object_hashes[obj.name] = object_canonical_hash(
            obj, world_points_by_object[obj.name]
        )

    all_serialized_properties = json.dumps(
        {
            "scene": custom_properties(scene),
            "objects": {
                obj.name: custom_properties(obj) for obj in objects
            },
        },
        sort_keys=True,
        default=str,
    )
    forbidden_equation_absent = (
        "EQ_CANDIDATE_AXIAL_INTERSECTION"
        not in all_serialized_properties
    )

    identity_transforms = []
    transform_failures = []
    for obj in objects:
        identity = (
            tuple(float(value) for value in obj.location) == (0.0, 0.0, 0.0)
            and tuple(float(value) for value in obj.rotation_euler)
            == (0.0, 0.0, 0.0)
            and tuple(float(value) for value in obj.scale)
            == (1.0, 1.0, 1.0)
        )
        identity_transforms.append(identity)
        if not identity:
            transform_failures.append(
                {
                    "object": obj.name,
                    "location": list(obj.location),
                    "rotation_euler": list(obj.rotation_euler),
                    "scale": list(obj.scale),
                }
            )

    variant_objects = [
        obj
        for obj in objects
        if bool(obj.get("Aerathea.VariantLocalC04", False))
    ]
    local_faces = [
        obj
        for obj in variant_objects
        if bool(obj.get("Aerathea.LocalExtentAuditOwner", False))
    ]
    local_points = [
        point
        for obj in local_faces
        for point in world_points_by_object[obj.name]
    ]
    local_y_min = min(point[1] for point in local_points)
    local_y_max = max(point[1] for point in local_points)
    expected_local_half_f32 = f32(float(asset["local_half"]))
    local_extent_symmetric = local_y_min == -local_y_max
    local_extent_inside_registration_domain = (
        abs(local_y_min) <= expected_local_half_f32
        and abs(local_y_max) <= expected_local_half_f32
    )
    local_x_sides = {
        -1 if point[0] < 0.0 else 1 if point[0] > 0.0 else 0
        for point in local_points
    }
    doubled_local_treatment = (
        len(variant_objects) == 4
        and len(local_faces) == 2
        and local_x_sides.issuperset({-1, 1})
        and local_extent_symmetric
        and local_extent_inside_registration_domain
    )
    inside_common_envelope = all(
        abs(point[1]) <= f32(float(COMMON_HALF_DEPTH))
        for obj in variant_objects
        for point in world_points_by_object[obj.name]
    )

    observed_shared_hash = saved_shared_base_hash(
        objects, world_points_by_object
    )
    shared_object_hashes = {
        name: value
        for name, value in object_hashes.items()
        if not bool(
            next(obj for obj in objects if obj.name == name).get(
                "Aerathea.VariantLocalC04", False
            )
        )
    }
    source_hash_after = sha256(asset["blend"])

    checks = {
        "source_hash_before_matches_lock": source_hash_before
        == asset["sha256"],
        "source_hash_after_matches_lock": source_hash_after
        == asset["sha256"],
        "source_hash_before_equals_after": source_hash_before
        == source_hash_after,
        "asset_id_matches": scene.get("Aerathea.AssetId")
        == asset["asset_id"],
        "build_id_matches": scene.get("Aerathea.BuildId") == BUILD_ID,
        "variant_identity_matches": scene.get("Aerathea.LocalC04Treatment")
        == asset["variant"],
        "completed_face_rule_matches": scene.get("Aerathea.CompletedFaceRule")
        == asset["completed_face_rule"],
        "exact_expected_dimension_properties_match": [
            scene.get("Aerathea.ExpectedWidthCmExact"),
            scene.get("Aerathea.ExpectedDepthCmExact"),
            scene.get("Aerathea.ExpectedHeightCmExact"),
        ]
        == [qstr(value) for value in EXPECTED_DIMENSIONS],
        "direct_saved_bounds_within_locked_float32_encoding_tolerance": (
            prior_tolerance_pass
        ),
        "pivot_bottom_center_at_origin": minimum[2] == 0.0,
        "all_object_transforms_applied_identity": all(identity_transforms),
        "saved_shared_base_hash_matches_lock": observed_shared_hash
        == EXPECTED_SAVED_SHARED_HASH,
        "builder_shared_hash_scene_lock_matches": scene.get(
            "Aerathea.SharedBaseCanonicalSha256"
        )
        == EXPECTED_BUILDER_SHARED_HASH,
        "local_c04_object_count_four": len(variant_objects) == 4,
        "correct_doubled_local_treatment": doubled_local_treatment,
        "local_interval_matches": scene.get(
            "Aerathea.LocalC04SourceIntervalHalfOpen"
        )
        == f"[{asset['source_interval'][0]},{asset['source_interval'][1]})",
        "local_domain_exact_matches": scene.get(
            "Aerathea.LocalC04DomainHalfCmExact"
        )
        == qstr(asset["local_half"]),
        "local_y_mirror_count_one": int(
            scene.get("Aerathea.C04LocalYMirrorCount", -1)
        )
        == 1,
        "whole_asset_rz180_count_one": int(
            scene.get("Aerathea.WholeAssetRz180Count", -1)
        )
        == 1,
        "variant_inside_common_depth_envelope": inside_common_envelope,
        "every_mesh_object_authorized": not unauthorized_objects,
        "every_mesh_surface_provenance_matches": not provenance_mismatches,
        "forbidden_global_depth_equation_absent": forbidden_equation_absent,
        "forbidden_fill_geometry_markers_absent": not forbidden_hits,
        "assembled_closed_manifold_volume": topology[
            "assembly_closed_manifold_volume"
        ],
        "declared_contacts_pass": contact_audit["result"] == "PASS",
        "no_linked_libraries": len(bpy.data.libraries) == 0,
        "no_external_image_dependencies": all(
            not image.filepath for image in bpy.data.images
        ),
        "quarantined_geometry_read_count_zero": int(
            scene.get("Aerathea.QuarantinedGeometryReadCount", -1)
        )
        == 0,
    }

    negative_space = protected_negative_space_authority()
    negative_space["observed_authorized_mesh_object_count"] = len(objects)
    negative_space["unauthorized_mesh_object_count"] = len(
        unauthorized_objects
    )
    negative_space["forbidden_fill_marker_count"] = len(forbidden_hits)
    negative_space["assembled_only_from_declared_identities"] = (
        not unauthorized_objects
        and not provenance_mismatches
        and not forbidden_hits
        and topology["assembly_closed_manifold_volume"]
        and contact_audit["result"] == "PASS"
    )
    negative_space["result"] = (
        "PASS"
        if negative_space["assembled_only_from_declared_identities"]
        else "FAIL"
    )
    checks["protected_negative_space_evidence_pass"] = (
        negative_space["result"] == "PASS"
    )

    triangle_count = sum(
        sum(max(0, len(poly.vertices) - 2) for poly in obj.data.polygons)
        for obj in objects
    )
    result = "PASS" if all(checks.values()) else "FAIL"
    return {
        "asset_id": asset["asset_id"],
        "display_name": asset["display_name"],
        "variant": asset["variant"],
        "completed_face_rule": asset["completed_face_rule"],
        "artifact_status": "proof only",
        "result": result,
        "checks": checks,
        "source": {
            "path": relative(asset["blend"]),
            "sha256_before": source_hash_before,
            "sha256_after": source_hash_after,
            "byte_identical_after_inspection": source_hash_before
            == source_hash_after,
        },
        "identity_and_lineage": {
            "scene_properties": custom_properties(scene),
            "mesh_object_names": [obj.name for obj in objects],
            "unauthorized_mesh_objects": unauthorized_objects,
            "provenance_mismatches": provenance_mismatches,
            "forbidden_geometry_marker_hits": forbidden_hits,
        },
        "expected_dimensions_cm": {
            "exact": [qstr(value) for value in EXPECTED_DIMENSIONS],
            "decimal": expected_decimal,
        },
        "direct_observed_saved_mesh_bounds_cm": {
            "minimum": minimum,
            "maximum": maximum,
            "dimensions": dimensions,
            "signed_residual_from_exact_decimal": residuals,
            "absolute_residual_from_exact_decimal": [
                abs(value) for value in residuals
            ],
            "float32_encoding_tolerance_cm": (
                PRIOR_APPROVED_FLOAT32_ENCODING_TOLERANCE_CM
            ),
            "tolerance_authority": {
                "path": relative(PRIOR_AUDIT),
                "sha256": AUTHORITIES[PRIOR_AUDIT],
                "locked_asset_audit_path": relative(
                    asset["prior_saved_audit"]
                ),
            },
            "expected_and_observed_recorded_separately": True,
        },
        "pivot_and_transforms": {
            "approved_pivot_cm_exact": ["0/1", "0/1", "0/1"],
            "direct_observed_minimum_z_cm": minimum[2],
            "transform_failures": transform_failures,
        },
        "shared_base": {
            "builder_exact_canonical_sha256_expected": (
                EXPECTED_BUILDER_SHARED_HASH
            ),
            "builder_exact_canonical_sha256_scene": scene.get(
                "Aerathea.SharedBaseCanonicalSha256"
            ),
            "independently_derived_saved_canonical_sha256_expected": (
                EXPECTED_SAVED_SHARED_HASH
            ),
            "independently_derived_saved_canonical_sha256_observed": (
                observed_shared_hash
            ),
            "shared_object_canonical_sha256": shared_object_hashes,
        },
        "local_c04": {
            "approved_source_interval_half_open": asset["source_interval"],
            "approved_local_half_extent_cm_exact": qstr(asset["local_half"]),
            "approved_local_half_extent_cm_float32": expected_local_half_f32,
            "observed_local_y_min_cm": local_y_min,
            "observed_local_y_max_cm": local_y_max,
            "observed_local_extent_symmetric": local_extent_symmetric,
            "observed_local_extent_inside_registration_domain": (
                local_extent_inside_registration_domain
            ),
            "registration_domain_is_not_required_fill": True,
            "observed_local_x_signs": sorted(local_x_sides),
            "variant_mesh_objects": [obj.name for obj in variant_objects],
            "local_extent_mesh_objects": [obj.name for obj in local_faces],
            "inside_common_depth_envelope": inside_common_envelope,
        },
        "topology": topology,
        "declared_contacts": contact_audit,
        "protected_negative_spaces": negative_space,
        "direct_observed_counts": {
            "mesh_objects": len(objects),
            "vertices": sum(len(obj.data.vertices) for obj in objects),
            "polygons": sum(len(obj.data.polygons) for obj in objects),
            "triangles": triangle_count,
            "high_poly_counts_are_observed_not_a_pass_fail_budget": True,
        },
        "dependencies": {
            "linked_library_count": len(bpy.data.libraries),
            "external_image_dependency_count": sum(
                1 for image in bpy.data.images if image.filepath
            ),
            "quarantined_geometry_read_count": int(
                scene.get("Aerathea.QuarantinedGeometryReadCount", -1)
            ),
        },
        "object_canonical_sha256": object_hashes,
        "classification_if_pass": "DCC source candidate",
        "retopology_uv_bake_export_authority": False,
        "unreal_authority": False,
    }


def internal_audit() -> int:
    import bpy

    authority_checks = verify_authorities()
    source_hashes_before: dict[str, str] = {}
    for asset_key, asset in ASSETS.items():
        observed = sha256(asset["blend"])
        source_hashes_before[asset_key] = observed
        if observed != asset["sha256"]:
            raise RuntimeError(f"Immutable source hash mismatch: {asset_key}")

    asset_results: dict[str, Any] = {}
    for asset_key, asset in ASSETS.items():
        bpy.ops.wm.open_mainfile(filepath=str(asset["blend"]))
        asset_results[asset_key] = inspect_loaded_asset(
            bpy, asset, source_hashes_before[asset_key]
        )

    siege = asset_results["siege_breaker"]
    foe = asset_results["foe_hammer"]
    dimension_differences = [
        siege["direct_observed_saved_mesh_bounds_cm"]["dimensions"][axis]
        - foe["direct_observed_saved_mesh_bounds_cm"]["dimensions"][axis]
        for axis in range(3)
    ]
    bitwise_equal_dimensions = all(
        struct.pack(
            ">d",
            siege["direct_observed_saved_mesh_bounds_cm"]["dimensions"][axis],
        )
        == struct.pack(
            ">d",
            foe["direct_observed_saved_mesh_bounds_cm"]["dimensions"][axis],
        )
        for axis in range(3)
    )
    shared_object_differences = []
    siege_shared = siege["shared_base"]["shared_object_canonical_sha256"]
    foe_shared = foe["shared_base"]["shared_object_canonical_sha256"]
    for name in sorted(set(siege_shared) | set(foe_shared)):
        if siege_shared.get(name) != foe_shared.get(name):
            shared_object_differences.append(
                {
                    "object": name,
                    "siege_breaker_sha256": siege_shared.get(name),
                    "foe_hammer_sha256": foe_shared.get(name),
                }
            )

    cross_checks = {
        "siege_breaker_asset_audit_pass": siege["result"] == "PASS",
        "foe_hammer_asset_audit_pass": foe["result"] == "PASS",
        "observed_xyz_dimensions_bitwise_equal": bitwise_equal_dimensions,
        "observed_xyz_difference_exact_zero": dimension_differences
        == [0.0, 0.0, 0.0],
        "shared_saved_hashes_equal": siege["shared_base"][
            "independently_derived_saved_canonical_sha256_observed"
        ]
        == foe["shared_base"][
            "independently_derived_saved_canonical_sha256_observed"
        ]
        == EXPECTED_SAVED_SHARED_HASH,
        "no_cross_asset_difference_outside_tagged_local_c04": not (
            shared_object_differences
        ),
        "correct_twin_variant_identities": (
            siege["variant"] == "rune_side"
            and foe["variant"] == "metal_center_piece_side"
        ),
        "both_sources_byte_identical_after_audit": (
            siege["source"]["byte_identical_after_inspection"]
            and foe["source"]["byte_identical_after_inspection"]
        ),
    }
    result = "PASS" if all(cross_checks.values()) else "FAIL"
    output = {
        "schema": "AERATHEA_STEP_13_IMMUTABLE_GEOMETRY_TECHNICAL_AUDIT_V1",
        "date_utc": utc_now(),
        "run_id": RUN_ID,
        "step_id": STEP_ID,
        "artifact_status": f"proof only; {result}",
        "result": result,
        "audit_amendment_history": [SUPERSEDED_AUDIT_RECORD],
        "decision": (
            "technical audit passes; read-only review rendering may begin"
            if result == "PASS"
            else "technical audit failed; render path remains stopped"
        ),
        "authority_checks": authority_checks,
        "environment": {
            "blender_executable": {
                "path": relative(BLENDER),
                "sha256": sha256(BLENDER),
                "version": bpy.app.version_string,
            },
            "network_access_used": False,
            "source_save_operator_invoked": False,
            "execution_boundary": (
                "local locked files only; no network; no source write/save"
            ),
        },
        "topology_interpretation_record": {
            "status": "evidence-bound",
            "statement": (
                "Mesh objects are the locked manifest's source-owned surface "
                "records, not independently declared solid components. Each "
                "object receives explicit topology metrics; closed/manifold "
                "volume is decided by exact-coordinate assembled incidence."
            ),
            "authority": [
                relative(BUILDER_MANIFEST),
                relative(BLUEPRINT),
            ],
            "unapproved_tolerance_used": False,
        },
        "cross_asset_checks": cross_checks,
        "expected_shared_dimensions_cm_exact": [
            qstr(value) for value in EXPECTED_DIMENSIONS
        ],
        "direct_observed_cross_asset_dimension_difference_cm": (
            dimension_differences
        ),
        "shared_object_differences_outside_local_c04": (
            shared_object_differences
        ),
        "assets": asset_results,
        "assumptions": [],
        "interpretations": [
            (
                "Authoritative mesh objects are surface patches; assembled "
                "exact-coordinate topology owns the volume decision."
            ),
            (
                "Protected source-pixel gaps are preserved only if the saved "
                "assembly contains exactly the authorized owner/provenance "
                "object set, no forbidden fill identity, and passes declared "
                "contact plus exact assembled topology checks."
            ),
        ],
        "blockers_or_uncertainty": (
            []
            if result == "PASS"
            else [
                "One or more exact technical requirements failed; no rendering is authorized."
            ]
        ),
        "source_classification_before": {
            key: "DCC source candidate" for key in ASSETS
        },
        "source_classification_after": {
            key: "DCC source candidate" for key in ASSETS
        },
        "step_14_authority": False,
        "retopology_uv_bake_export_authority": False,
        "unreal_authority": False,
        "auditor": {
            "path": relative(Path(__file__)),
            "sha256": sha256(Path(__file__)),
        },
    }
    write_json(TECHNICAL_AUDIT, output)
    print(
        json.dumps(
            {
                "result": result,
                "technical_audit": relative(TECHNICAL_AUDIT),
                "cross_asset_checks": cross_checks,
                "asset_results": {
                    key: value["result"]
                    for key, value in asset_results.items()
                },
            },
            indent=2,
            sort_keys=True,
        )
    )
    return 0 if result == "PASS" else 2


def write_external_blocked(reason: str) -> None:
    source_records = {}
    for key, asset in ASSETS.items():
        source_records[key] = {
            "path": relative(asset["blend"]),
            "expected_sha256": asset["sha256"],
            "observed_sha256": (
                sha256(asset["blend"]) if asset["blend"].is_file() else None
            ),
        }
    write_json(
        TECHNICAL_AUDIT,
        {
            "schema": "AERATHEA_STEP_13_IMMUTABLE_GEOMETRY_TECHNICAL_AUDIT_V1",
            "date_utc": utc_now(),
            "run_id": RUN_ID,
            "step_id": STEP_ID,
            "artifact_status": "proof only; BLOCKED",
            "result": "BLOCKED",
            "decision": "render path remains stopped",
            "blocker": reason,
            "sources": source_records,
            "assumptions": [],
            "step_14_authority": False,
            "unreal_authority": False,
        },
    )


def external_audit() -> int:
    try:
        verify_authorities()
        for asset_key, asset in ASSETS.items():
            observed = sha256(asset["blend"])
            if observed != asset["sha256"]:
                raise RuntimeError(
                    f"Immutable source hash mismatch: {asset_key}"
                )
        if TECHNICAL_AUDIT.exists():
            existing_hash = sha256(TECHNICAL_AUDIT)
            if existing_hash != SUPERSEDED_AUDIT_RECORD[
                "technical_audit_sha256"
            ]:
                raise RuntimeError(
                    f"Step 13 technical audit already exists and is not the "
                    f"locked superseded pass: {relative(TECHNICAL_AUDIT)}"
                )
        command = [
            str(BLENDER),
            "--background",
            "--factory-startup",
            "--python",
            str(Path(__file__).resolve()),
            "--",
            "--internal-audit",
        ]
        environment = dict(os.environ)
        environment["PYTHONHASHSEED"] = "0"
        completed = subprocess.run(
            command,
            cwd=ROOT,
            env=environment,
            check=False,
        )
        if completed.returncode != 0:
            if not TECHNICAL_AUDIT.exists():
                write_external_blocked(
                    f"Blender audit exited {completed.returncode} before "
                    "producing its evidence record."
                )
            return completed.returncode
        audit = load_json(TECHNICAL_AUDIT)
        return 0 if audit["result"] == "PASS" else 2
    except Exception as exc:
        if not TECHNICAL_AUDIT.exists():
            write_external_blocked(str(exc))
        raise


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser()
    parser.add_argument("--audit", action="store_true")
    parser.add_argument("--internal-audit", action="store_true")
    return parser.parse_args(
        sys.argv[sys.argv.index("--") + 1 :] if "--" in sys.argv else None
    )


def main() -> int:
    args = parse_args()
    if args.internal_audit:
        return internal_audit()
    if args.audit:
        return external_audit()
    raise RuntimeError("Choose --audit or --internal-audit")


if __name__ == "__main__":
    raise SystemExit(main())
