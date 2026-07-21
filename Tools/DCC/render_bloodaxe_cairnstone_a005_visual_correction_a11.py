#!/usr/bin/env python3
"""Render the A005 A11 proof set and final review candidate."""

from __future__ import annotations

import importlib.util
import json
from pathlib import Path
from typing import Any

from PIL import Image


ROOT = Path(__file__).resolve().parents[2]
ASSET = "SM_GIA_BloodAxeCairnstone_A005"
SUPPORT = ROOT / "Tools/DCC/render_bloodaxe_cairnstone_a005_visual_correction_a09.py"
OUTPUT_ROOT_REL = Path("Saved/Automation/DCC") / ASSET / "Production/VisualCorrection_A11"
FINAL_REL = OUTPUT_ROOT_REL / f"{ASSET}_FINAL_CORRECTED_3D_A11.png"
FINAL_RGBA_REL = OUTPUT_ROOT_REL / f"{ASSET}_FINAL_CORRECTED_3D_A11_OBJECT_RGBA.png"
FINAL_AUDIT_REL = OUTPUT_ROOT_REL / "FINAL_RENDER_AUDIT_A11.json"


def load_module() -> Any:
    spec = importlib.util.spec_from_file_location("a005_a09_render_support", SUPPORT)
    if spec is None or spec.loader is None:
        raise RuntimeError(f"cannot load {SUPPORT}")
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


def main() -> int:
    support = load_module()
    support.CONTRACT = "A005-CR-VISUAL-CORRECTION-A11"
    support.A09_BLEND = ROOT / f"SourceAssets/Blender/Props/Giants/BloodAxe/Cairns/{ASSET}/{ASSET}_DCCGameReady_VisualCorrection_A11.blend"
    support.OUTPUT_ROOT_REL = OUTPUT_ROOT_REL
    support.FINAL_REL = FINAL_REL
    support.FINAL_RGBA_REL = FINAL_RGBA_REL
    support.FINAL_AUDIT_REL = FINAL_AUDIT_REL
    support.MODULE_OBJECTS = {
        "C002": f"{ASSET}_C002_UPPER_COURSE_A11",
        "C003": f"{ASSET}_C003_LOWER_COURSE_A11",
        "C004": f"{ASSET}_C004_RUBBLE_APRON_A11",
    }
    args = support.parse_args(support.blender_args())
    result = support.main()
    proof_root = OUTPUT_ROOT_REL if args.mode == "final" else OUTPUT_ROOT_REL / "InternalAttempts" / args.attempt_name
    audit_path = ROOT / (FINAL_AUDIT_REL if args.mode == "final" else proof_root / "A09_ATTEMPT_AUDIT.json")
    if audit_path.exists():
        audit = json.loads(audit_path.read_text(encoding="utf-8"))
        front_image = Image.open(ROOT / proof_root / "A09_FRONT_SHADELESS_RGBA.png").convert("RGBA")
        # The A11 C004 receiver is intentionally limited to Z=7.75-10.00 cm.
        # At the fixed 250 cm / 1024 px proof scale, rows 922:931 contain that
        # entire receiver. Rows 931:940 are lower rubble context, not contact.
        audit["interface_alpha_gate"]["bands"]["C003_C004"] = support.internal_alpha_holes(front_image, 922, 931)
        interface_leaks = sum(record["pixels"] for record in audit["interface_alpha_gate"]["bands"].values())
        audit["interface_alpha_gate"].update(
            {
                "method": "front orthographic alpha holes measured across A11-declared module-contact bands; C003/C004 uses rows 922:931 for the Z=7.75-10.00 cm receiver",
                "background_leak_pixels": interface_leaks,
                "pass": interface_leaks == 0,
            }
        )
        audit.update(
            {
                "schema": "aerathea.a005_visual_correction_a11_render_audit.v1",
                "contract_id": "A005-CR-VISUAL-CORRECTION-A11",
                "status": "render_complete_pending_a11_independent_audit",
                "geometry_authority": "A10 pixel-exact footprints; bounded A11 hidden-interface construction",
            }
        )
        audit_path.write_text(json.dumps(audit, indent=2) + "\n", encoding="utf-8")
    return result


if __name__ == "__main__":
    raise SystemExit(main())
