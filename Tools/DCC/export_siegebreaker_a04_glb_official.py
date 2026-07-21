#!/usr/bin/env python3
"""Export A04 LOD0 to GLB with the official Blender runtime and close its manifest."""

from __future__ import annotations

import hashlib
import json
from pathlib import Path

import bpy


ROOT = Path(__file__).resolve().parents[2]
ASSET_ID = "SM_DRW_SiegeBreaker_Hammer_A01"
REVISION = "StrictScanline_A04"
GLB_PATH = ROOT / "SourceAssets/Exports/Weapons/Dwarven" / ASSET_ID / REVISION / f"{ASSET_ID}.glb"
BUILD_MANIFEST = ROOT / "SourceAssets/Blender/Weapons/Dwarven" / ASSET_ID / f"{ASSET_ID}_{REVISION}_BUILD_MANIFEST.json"


def sha256(path: Path) -> str:
    digest = hashlib.sha256()
    with path.open("rb") as handle:
        for block in iter(lambda: handle.read(1024 * 1024), b""):
            digest.update(block)
    return digest.hexdigest()


def main() -> int:
    collection = bpy.data.collections.get("SB_A04_LOD0")
    if collection is None:
        raise RuntimeError("SB_A04_LOD0 collection not found in A04 source blend")
    objects = [obj for obj in collection.all_objects if obj.type == "MESH"]
    if not objects:
        raise RuntimeError("A04 LOD0 contains no mesh objects")
    bpy.ops.object.select_all(action="DESELECT")
    for obj in objects:
        obj.hide_set(False)
        obj.select_set(True)
    bpy.context.view_layer.objects.active = objects[0]
    GLB_PATH.parent.mkdir(parents=True, exist_ok=True)
    bpy.ops.export_scene.gltf(
        filepath=str(GLB_PATH),
        export_format="GLB",
        use_selection=True,
        export_apply=True,
        export_materials="EXPORT",
    )
    if not GLB_PATH.exists() or GLB_PATH.stat().st_size == 0:
        raise RuntimeError("Official Blender runtime did not create the A04 GLB")
    manifest = json.loads(BUILD_MANIFEST.read_text(encoding="utf-8"))
    manifest["exports"]["LOD0_GLB"] = {
        "path": str(GLB_PATH.relative_to(ROOT)),
        "sha256": sha256(GLB_PATH),
        "bytes": GLB_PATH.stat().st_size,
        "status": "complete",
        "runtime": bpy.app.version_string,
    }
    BUILD_MANIFEST.write_text(json.dumps(manifest, indent=2) + "\n", encoding="utf-8")
    print(GLB_PATH)
    print(BUILD_MANIFEST)
    print("A04 GLB EXPORT COMPLETE")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
