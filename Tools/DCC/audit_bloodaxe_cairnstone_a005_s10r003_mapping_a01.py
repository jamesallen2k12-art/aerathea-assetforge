#!/usr/bin/env python3
"""Independently audit the bounded S10R-003-A mapping candidate."""

from __future__ import annotations

import hashlib
import json
import math
import subprocess
from collections import Counter, defaultdict
from datetime import datetime
from pathlib import Path

from PIL import Image


ROOT = Path(__file__).resolve().parents[2]
ASSET = ROOT / "docs/assets/blueprints/SM_GIA_BloodAxeCairnstone_A005"
MANIFESTS = ASSET / "manifests"
CONTRACT = ASSET / "steps/S10R_003_A_CL003_TARGET_SPACE_MAPPING_EXECUTION_A01_CONTRACT.md"
INPUT_LOCK = MANIFESTS / "S10R_003_A_CL003_TARGET_SPACE_MAPPING_A01_INPUT_LOCK.json"
LEDGER = MANIFESTS / "S10R_003_A_CL003_TARGET_SPACE_MAPPING_A01_LEDGER.json"
VALIDATION_OUT = MANIFESTS / "S10R_003_A_CL003_TARGET_SPACE_MAPPING_A01_VALIDATION.json"
SOURCE_CONTACTS = MANIFESTS / "STEP_04_TOP_CONTACT_EVIDENCE_RECOVERY_A01.json"
SOURCE_PANEL = ASSET / "panels/STEP_03/SM_GIA_BloodAxeCairnstone_A005_STEP_03_TOP.png"
PRE_STATUS = ROOT / "Saved/ProjectRecovery/20260717-153840/git_status_short.txt"
OUTPUT_RECORD = ASSET / "steps/S10R_003_A_CL003_TARGET_SPACE_MAPPING_A01_OUTPUT_RECORD.md"
DECISION_HANDOFF = ASSET / "handoffs/S10R_003_A_CL003_TARGET_SPACE_MAPPING_A01_TO_DECISION_HANDOFF.md"
BUILDER = ROOT / "Tools/DCC/build_bloodaxe_cairnstone_a005_s10r003_mapping_a01.py"
AUDITOR = ROOT / "Tools/DCC/audit_bloodaxe_cairnstone_a005_s10r003_mapping_a01.py"

CONTRACT_SHA256 = "10dc155b78e2d2e6f15a389a9a247db13450314df2d8e3bc9ba891901b3208f8"
ENDPOINTS = ((56.0, 0.0), (-56.0, 0.0), (0.0, 44.0), (0.0, -44.0))


def sha256(path: Path) -> str:
    digest = hashlib.sha256()
    with path.open("rb") as handle:
        for chunk in iter(lambda: handle.read(1024 * 1024), b""):
            digest.update(chunk)
    return digest.hexdigest()


def sign(value: float) -> float:
    return 1.0 if value > 0 else (-1.0 if value < 0 else 0.0)


def independent_theta(sector: str, rank: int) -> float:
    u = rank / 5.0
    rules = {
        "top": lambda: math.pi - math.pi * u,
        "right": lambda: 0.5 * math.pi - math.pi * u,
        "bottom": lambda: 2.0 * math.pi - math.pi * u,
        "left": lambda: 1.5 * math.pi - math.pi * u,
    }
    return rules[sector]()


def independent_point(sector: str, rank: int) -> tuple[float, float, float]:
    theta = independent_theta(sector, rank)
    c = math.cos(theta)
    s = math.sin(theta)
    return 56.0 * sign(c) * abs(c) ** (2.0 / 3.0), 44.0 * sign(s) * abs(s) ** (2.0 / 3.0), theta


def parse_status_paths(text: str) -> set[str]:
    paths = set()
    for line in text.splitlines():
        if len(line) >= 4:
            paths.add(line[3:].strip())
    return paths


def main() -> None:
    input_lock = json.loads(INPUT_LOCK.read_text(encoding="utf-8"))
    ledger = json.loads(LEDGER.read_text(encoding="utf-8"))
    contacts = json.loads(SOURCE_CONTACTS.read_text(encoding="utf-8"))
    records = ledger["records"]
    authority = {item["id"]: item for item in contacts["accepted_points"] if item["contact_id"] == "CL-003"}
    gates = []

    def gate(number: int, subject: str, passed: bool, evidence) -> None:
        gates.append({"gate": f"G{number:02d}", "subject": subject, "status": "pass" if passed else "fail", "evidence": evidence})

    locked_matches = [item["match"] and sha256(ROOT / item["path"]) == item["expected_sha256"] for item in input_lock["locked_inputs"]]
    gate(1, "all locked input hashes match before output writes", all(locked_matches), {"matched": sum(locked_matches), "total": len(locked_matches)})
    gate(2, "contract hash and approved contract identity", sha256(CONTRACT) == CONTRACT_SHA256 and input_lock["contract_id"] == "A005-CR-S10R-003-A-MAP-A01", {"sha256": sha256(CONTRACT), "approval": input_lock["execution_approval"]})
    gate(3, "exactly sixteen approved top-view CL-003 records", len(records) == 16 and len(authority) == 16, {"ledger": len(records), "authority": len(authority)})

    source_match_count = 0
    for item in records:
        source = authority.get(item["source_id"])
        if source and source["sector"] == item["sector"] and source["pixel_local"] == item["source_pixel_local"] and source["pixel_full_source"] == item["source_pixel_full"] and source["source_rgb"] == item["source_rgb"]:
            source_match_count += 1
    gate(4, "source IDs sectors ranks pixels and RGB match authority", source_match_count == 16, {"matched": source_match_count, "total": 16})

    sector_counts = Counter(item["sector"] for item in records)
    gate(5, "four samples in each of four sectors", sector_counts == Counter({"top": 4, "bottom": 4, "left": 4, "right": 4}), dict(sector_counts))
    gate(6, "source coordinates and artifacts remain byte-identical", sha256(SOURCE_PANEL) == input_lock["source_lock"]["source_panel_sha256"] and sha256(SOURCE_CONTACTS) == next(item["expected_sha256"] for item in input_lock["locked_inputs"] if item["path"].endswith("STEP_04_TOP_CONTACT_EVIDENCE_RECOVERY_A01.json")), {"source_panel_sha256": sha256(SOURCE_PANEL), "source_contacts_sha256": sha256(SOURCE_CONTACTS)})

    k80 = ledger["K80"]
    gate(7, "K80 formula extents origin role endpoints and sectors remain locked", k80["equation"] == "abs(x / 56)^3 + abs(y / 44)^3 = 1" and k80["full_extents_cm"] == [112, 88] and k80["origin_role"] == "mathematical construction convention only" and len(k80["registered_axis_endpoints"]) == 4, k80)

    u_exact = defaultdict(list)
    for item in records:
        u_exact[item["sector"]].append(item["u_exact"])
    expected_u = ["1/5", "2/5", "3/5", "4/5"]
    gate(8, "only exact endpoint-exclusive rank parameters are used", all(values == expected_u for values in u_exact.values()), dict(u_exact))

    expected_theta_rules = {"top": "pi * (1 - u)", "right": "pi/2 - pi*u", "bottom": "2*pi - pi*u", "left": "3*pi/2 - pi*u"}
    theta_rule_pass = all(item["theta_rule"] == expected_theta_rules[item["sector"]] and abs(float(item["theta_radians"]) - independent_theta(item["sector"], item["local_rank"])) < 1e-14 for item in records)
    gate(9, "only the four registered angular rules are used", theta_rule_pass, expected_theta_rules)
    gate(10, "exactly sixteen target records are produced", ledger["counts"]["candidate_target_coordinates"] == 16 and len(records) == 16, ledger["counts"]["candidate_target_coordinates"])

    residuals = [abs(abs(item["target_xy_cm"][0] / 56.0) ** 3 + abs(item["target_xy_cm"][1] / 44.0) ** 3 - 1.0) for item in records]
    gate(11, "every target lies on K80", max(residuals) < 1e-12, {"max_residual": max(residuals), "tolerance": 1e-12})

    replay_matches = 0
    for item in records:
        x, y, _ = independent_point(item["sector"], item["local_rank"])
        if item["target_xy_cm_decimal"] == [f"{x:.12f}", f"{y:.12f}"]:
            replay_matches += 1
    gate(12, "all coordinates replay to twelve decimal places", replay_matches == 16, {"matched": replay_matches, "total": 16})

    serialized = [tuple(item["target_xy_cm_decimal"]) for item in records]
    gate(13, "all sixteen serialized target coordinates are unique", len(set(serialized)) == 16, {"unique": len(set(serialized)), "total": 16})
    endpoint_hits = sum(1 for item in records if min(math.dist(tuple(item["target_xy_cm"]), endpoint) for endpoint in ENDPOINTS) <= 1e-9)
    gate(14, "no target equals a registered endpoint", endpoint_hits == 0, {"endpoint_hits": endpoint_hits})
    gate(15, "no source sample maps more than once", len({item["source_id"] for item in records}) == 16, {"unique_source_ids": len({item["source_id"] for item in records})})

    by_sector = defaultdict(list)
    for item in records:
        by_sector[item["sector"]].append(item)
    monotonic = all(all(float(a["theta_radians"]) > float(b["theta_radians"]) for a, b in zip(sorted(items, key=lambda row: row["local_rank"]), sorted(items, key=lambda row: row["local_rank"])[1:])) for items in by_sector.values())
    gate(16, "within-sector parameter order is strictly monotonic", monotonic, {sector: [item["theta_radians"] for item in sorted(items, key=lambda row: row["local_rank"])] for sector, items in by_sector.items()})

    half_plane = all((item["sector"] != "top" or item["target_xy_cm"][1] > 0) and (item["sector"] != "bottom" or item["target_xy_cm"][1] < 0) and (item["sector"] != "right" or item["target_xy_cm"][0] > 0) and (item["sector"] != "left" or item["target_xy_cm"][0] < 0) for item in records)
    gate(17, "every target stays in its matching sector half-plane", half_plane, {"records_checked": 16})
    no_snap = len(set(serialized)) == 16 and all(not item["snap_anchor_authority"] for item in records)
    gate(18, "adjacent sectors share no mapped coordinate or snap claim", no_snap, {"duplicates": 16 - len(set(serialized)), "snap_claims": sum(bool(item["snap_anchor_authority"]) for item in records)})
    gate(19, "source displacement remains zero", all(item["source_displacement_px"] == 0 for item in records) and ledger["counts"]["source_displacement_px"] == 0, {"displacement_px": ledger["counts"]["source_displacement_px"]})
    gate(20, "source overlays and fit calculations remain zero", ledger["counts"]["source_overlays"] == 0 and ledger["counts"]["source_fit_calculations"] == 0, {"source_overlays": ledger["counts"]["source_overlays"], "source_fit_calculations": ledger["counts"]["source_fit_calculations"]})
    gate(21, "physical cross-view pairings remain zero", ledger["counts"]["physical_cross_view_pairs"] == 0 and all(not item["physical_cross_view_pair"] for item in records), {"physical_cross_view_pairs": ledger["counts"]["physical_cross_view_pairs"]})
    gate(22, "non-top mapped samples remain zero", ledger["counts"]["mapped_non_top_samples"] == 0, {"mapped_non_top_samples": ledger["counts"]["mapped_non_top_samples"]})

    forbidden_claims = sum(bool(item[key]) for item in records for key in ("source_center_claim", "pivot_claim", "physical_C003_dimension_claim", "snap_anchor_authority", "geometry_vertex_authority"))
    gate(23, "center pivot placement physical-size and anchor claims remain zero", forbidden_claims == 0, {"forbidden_claims": forbidden_claims})
    gate(24, "CL-002 closure annuli hidden interfaces and footprints remain zero", all(ledger["counts"][key] == 0 for key in ("filled_footprints", "annuli", "hidden_interfaces", "closed_contact_loops")), {key: ledger["counts"][key] for key in ("filled_footprints", "annuli", "hidden_interfaces", "closed_contact_loops")})
    gate(25, "fields surfaces topology and geometry remain zero", all(ledger["counts"][key] == 0 for key in ("fields", "surfaces", "topology", "geometry")), {key: ledger["counts"][key] for key in ("fields", "surfaces", "topology", "geometry")})

    board_path = ROOT / ledger["review_board"]["path"]
    with Image.open(board_path) as board:
        board_size = [board.width, board.height]
    board_pass = ledger["review_board"]["line_only_target_curve"] and ledger["review_board"]["candidate_fill_count"] == 0 and ledger["review_board"]["cross_sector_join_count"] == 0 and ledger["review_board"]["source_target_overlay_count"] == 0 and ledger["review_board"]["geometry_preview_count"] == 0 and sha256(board_path) == ledger["review_board"]["sha256"]
    gate(26, "review board is line-only separated unfilled and labeled by construction", board_pass, {"sha256": sha256(board_path), "size_px": board_size, "metadata": ledger["review_board"]})
    gate(27, "independent auditor reproduces calculations without builder arrays", replay_matches == 16, {"independent_replays": replay_matches, "builder_module_imported": False})
    status_flag_match = all(item["classification"] == "candidate interpretation" and item["pending_Flamestrike_decision"] for item in records)
    gate(28, "builder and auditor agree on coordinates and status flags", replay_matches == 16 and status_flag_match, {"coordinate_matches": replay_matches, "status_matches": sum(1 for item in records if item["classification"] == "candidate interpretation" and item["pending_Flamestrike_decision"])})

    baseline_paths = parse_status_paths(PRE_STATUS.read_text(encoding="utf-8"))
    current_status_text = subprocess.check_output(["git", "status", "--short"], cwd=ROOT, text=True)
    current_paths = parse_status_paths(current_status_text)
    new_paths = sorted(current_paths - baseline_paths)
    allowed_prefixes = (
        "Tools/DCC/build_bloodaxe_cairnstone_a005_s10r003_mapping_a01.py",
        "Tools/DCC/audit_bloodaxe_cairnstone_a005_s10r003_mapping_a01.py",
        "docs/assets/blueprints/SM_GIA_BloodAxeCairnstone_A005/manifests/S10R_003_A_CL003_TARGET_SPACE_MAPPING_A01_",
        "docs/assets/blueprints/SM_GIA_BloodAxeCairnstone_A005/evidence/S10R_003_A_CL003_TARGET_SPACE_MAPPING_A01",
        "docs/assets/blueprints/SM_GIA_BloodAxeCairnstone_A005/steps/S10R_003_A_CL003_TARGET_SPACE_MAPPING_A01_OUTPUT_RECORD.md",
        "docs/assets/blueprints/SM_GIA_BloodAxeCairnstone_A005/handoffs/S10R_003_A_CL003_TARGET_SPACE_MAPPING_A01_TO_DECISION_HANDOFF.md",
    )
    unexpected = [path for path in new_paths if not any(path.startswith(prefix) for prefix in allowed_prefixes)]
    gate(29, "changed paths are contained by the execution allowlist", not unexpected, {"new_paths": new_paths, "unexpected_paths": unexpected})

    staged = subprocess.check_output(["git", "diff", "--cached", "--name-only"], cwd=ROOT, text=True).splitlines()
    gate(30, "no path is staged committed or pushed", not staged and subprocess.check_output(["git", "rev-parse", "--short", "HEAD"], cwd=ROOT, text=True).strip() == "f525945", {"staged_paths": staged, "head": subprocess.check_output(["git", "rev-parse", "--short", "HEAD"], cwd=ROOT, text=True).strip()})
    stop_pass = ledger["mandatory_stop"] == "visible candidate review before any promotion or downstream work" and not ledger["authority_limits"]["step10_closeout_authorized"] and not ledger["authority_limits"]["step11_authorized"] and not ledger["authority_limits"]["production_authorized"]
    gate(31, "execution stops at visible candidate review", stop_pass, {"mandatory_stop": ledger["mandatory_stop"], "authority_limits": ledger["authority_limits"]})

    passed = sum(item["status"] == "pass" for item in gates)
    failed = len(gates) - passed
    validation = {
        "schema": "aerathea.s10r_003_a_cl003_target_space_mapping_a01_validation.v1",
        "asset_id": "SM_GIA_BloodAxeCairnstone_A005",
        "contract_id": "A005-CR-S10R-003-A-MAP-A01",
        "date": "2026-07-17",
        "validated_at": datetime.now().astimezone().isoformat(),
        "status": "pass_candidate_mapping_pending_Flamestrike" if failed == 0 else "fail_quarantine_required",
        "artifact_classification": "proof only",
        "independent_auditor": "Tools/DCC/audit_bloodaxe_cairnstone_a005_s10r003_mapping_a01.py",
        "builder_imported": False,
        "input_lock_sha256": sha256(INPUT_LOCK),
        "ledger_sha256": sha256(LEDGER),
        "review_board_sha256": sha256(board_path),
        "output_hashes_before_validation": {
            "input_lock": sha256(INPUT_LOCK),
            "mapping_ledger": sha256(LEDGER),
            "review_board": sha256(board_path),
            "output_record": sha256(OUTPUT_RECORD),
            "decision_handoff": sha256(DECISION_HANDOFF),
            "builder": sha256(BUILDER),
            "independent_auditor": sha256(AUDITOR),
        },
        "gate_count": len(gates),
        "passed_gate_count": passed,
        "failed_gate_count": failed,
        "gates": gates,
        "technical_result": "sixteen_endpoint_exclusive_candidate_interpretation_mappings_validated" if failed == 0 else "candidate_mapping_validation_failed",
        "authority_effect": "none_pending_Flamestrike_decision",
        "source_displacement_px": 0,
        "physical_cross_view_pairs": 0,
        "fields_surfaces_topology_geometry": 0,
        "step10_closeout_authorized": False,
        "step11_authorized": False,
        "production_authorized": False,
        "staging_commit_push_authorized": False,
    }
    VALIDATION_OUT.write_text(json.dumps(validation, indent=2) + "\n", encoding="utf-8")
    print(f"Wrote {VALIDATION_OUT.relative_to(ROOT)}")
    print(f"Validation gates: {passed}/{len(gates)} pass; failures: {failed}")
    if failed:
        raise SystemExit(1)


if __name__ == "__main__":
    main()
