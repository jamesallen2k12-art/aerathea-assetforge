#!/usr/bin/env python3
"""Build the Aerathea 10 m universal portal arch source and FBX export.

Run with:
    blender --background --python Tools/DCC/build_portal_arch.py
"""

from __future__ import annotations

import sys
from pathlib import Path


ROOT = Path(__file__).resolve().parents[2]
sys.path.insert(0, str(ROOT))

from Tools.DCC.build_aerathea_blender_assets import AssetBuild, save_and_export  # noqa: E402
from Tools.DCC.generate_first_slice_meshes import portal_arch  # noqa: E402


def main() -> None:
    save_and_export(AssetBuild("Props/Portal/SM_AET_PortalArch_A01", portal_arch))


if __name__ == "__main__":
    main()
