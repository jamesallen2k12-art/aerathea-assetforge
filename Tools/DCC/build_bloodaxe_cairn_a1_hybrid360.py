#!/usr/bin/env python3
"""Build A1 Blood Axe cairn as a front-faithful projection with authored 360 backing.

Run with:
    Tools/Blender/blender-4.5.11-linux-x64/blender --background --python Tools/DCC/build_bloodaxe_cairn_a1_hybrid360.py

This keeps the approved A1/Test2 front projection as the visual anchor, then
adds the previously omitted inferred back/side stone volumes so the asset can
be inspected as a 3D candidate instead of a front-only shell.
"""

from __future__ import annotations

import sys
from pathlib import Path

import bpy


ROOT = Path(__file__).resolve().parents[2]
sys.path.insert(0, str(ROOT))
for site_path in (
    "/usr/local/lib/python3.10/dist-packages",
    "/usr/lib/python3/dist-packages",
    "/usr/lib/python3.10/dist-packages",
):
    if site_path not in sys.path and Path(site_path).exists():
        sys.path.append(site_path)

from Tools.DCC import build_bloodaxe_cairn_a1_test2_manual as base  # noqa: E402

if not hasattr(base.Image, "Resampling"):
    class _CompatResampling:
        LANCZOS = base.Image.LANCZOS

    base.Image.Resampling = _CompatResampling


ASSET_NAME = "SM_GIA_BloodAxeCairnSlabCluster_A01_Hybrid360"
REL_PATH = f"Props/Giants/BloodAxe/Cairns/{ASSET_NAME}"
UNREAL_PATH = f"/Game/Aerathea/Props/Giants/BloodAxe/Cairns/{ASSET_NAME}"


def retarget_base_module() -> None:
    base.ASSET_NAME = ASSET_NAME
    base.REL_PATH = REL_PATH
    base.UNREAL_PATH = UNREAL_PATH
    base.REVIEW_ROOT = ROOT / "Saved" / "Automation" / "DCC" / ASSET_NAME
    base.TEXTURE_DIR = base.TEXTURE_ROOT / REL_PATH
    base.TEXTURE_BC = base.TEXTURE_DIR / "T_GIA_BloodAxeCairnSlabCluster_A01_Hybrid360_BC.png"
    base.TEXTURE_N = base.TEXTURE_DIR / "T_GIA_BloodAxeCairnSlabCluster_A01_Hybrid360_N.png"
    base.TEXTURE_ORM = base.TEXTURE_DIR / "T_GIA_BloodAxeCairnSlabCluster_A01_Hybrid360_ORM.png"
    base.PROJECTION_BRIGHTNESS = 1.32
    base.PROJECTION_CONTRAST = 1.10
    base.PROJECTION_SATURATION = 1.04


def strengthen_side_material(material: bpy.types.Material) -> None:
    material.diffuse_color = (0.50, 0.47, 0.38, 1.0)
    if not material.use_nodes:
        return
    bsdf = material.node_tree.nodes.get("Principled BSDF")
    if bsdf is None:
        return
    bsdf.inputs["Base Color"].default_value = (0.50, 0.47, 0.38, 1.0)
    if "Emission Color" in bsdf.inputs:
        bsdf.inputs["Emission Color"].default_value = (0.27, 0.25, 0.20, 1.0)
    if "Emission Strength" in bsdf.inputs:
        bsdf.inputs["Emission Strength"].default_value = 0.20


def strengthen_image_material(material: bpy.types.Material) -> None:
    if not material.use_nodes:
        return
    bsdf = material.node_tree.nodes.get("Principled BSDF")
    if bsdf is None:
        return
    if "Emission Color" in bsdf.inputs:
        bsdf.inputs["Emission Color"].default_value = (0.18, 0.16, 0.13, 1.0)
    if "Emission Strength" in bsdf.inputs:
        bsdf.inputs["Emission Strength"].default_value = 0.16


def add_backfill(lod_level: int, collection: bpy.types.Collection, side_material: bpy.types.Material) -> list[bpy.types.Object]:
    objects: list[bpy.types.Object] = []
    if lod_level <= 1:
        specs = [
            ("CentralRearBrokenSlab", (10.0, 72.0, 78.0), (42.0, 30.0, 118.0), (-0.12, -0.22, 0.10), 901),
            ("LeftRearShard", (-58.0, 66.0, 58.0), (34.0, 27.0, 86.0), (0.08, 0.18, -0.18), 902),
            ("RightRearShard", (84.0, 58.0, 52.0), (38.0, 28.0, 78.0), (-0.06, -0.16, 0.22), 903),
            ("LowBackFoundationA", (-72.0, 78.0, 21.0), (68.0, 30.0, 24.0), (0.06, 0.04, -0.16), 904),
            ("LowBackFoundationB", (42.0, 80.0, 20.0), (78.0, 30.0, 22.0), (-0.05, -0.03, 0.14), 905),
            ("RightFrontChock", (128.0, -49.0, 18.0), (44.0, 25.0, 20.0), (0.06, 0.12, -0.24), 906),
            ("LeftRearCairnChunk", (-126.0, 54.0, 28.0), (38.0, 30.0, 38.0), (-0.10, -0.08, 0.16), 907),
            ("BackPebbleRidge", (0.0, 108.0, 14.0), (112.0, 20.0, 16.0), (0.05, 0.02, 0.10), 908),
        ]
        for name, location, dimensions, rotation, seed in specs:
            objects.append(
                base.add_support_box(
                    f"Hybrid360_Turnaround_{name}_LOD{lod_level}",
                    collection,
                    side_material,
                    location,
                    dimensions,
                    rotation,
                    seed + lod_level,
                )
            )
    return objects


def build() -> None:
    retarget_base_module()
    base.make_texture_sources()
    base.clear_scene()
    base.setup_scene()
    base.add_review_lighting()
    materials = base.make_materials()
    strengthen_image_material(materials["image"])
    strengthen_side_material(materials["side"])

    lod_collections = [
        base.make_collection(f"{ASSET_NAME}_LOD{i}_Hybrid360", hidden=i > 0)
        for i in range(4)
    ]
    collision_collection = base.make_collection(f"{ASSET_NAME}_Collision_Source", hidden=True)

    lod_objects: list[list[bpy.types.Object]] = []
    for lod_level, collection in enumerate(lod_collections):
        objects = base.build_lod_collection(lod_level, materials, collection)
        objects.extend(add_backfill(lod_level, collection, materials["side"]))
        lod_objects.append(objects)

    collision = base.add_collision_proxy(materials["collision"], collision_collection)

    base.add_asset_metadata(
        ASSET_NAME,
        "A01 Hybrid360 DCC candidate: approved Test2 front projection plus authored turnaround backfill stones for 360-degree review. Review candidate only until Flamestrike approval.",
        UNREAL_PATH,
    )

    blend_path = base.BLENDER_ROOT / REL_PATH / f"{ASSET_NAME}.blend"
    export_path = base.EXPORT_ROOT / REL_PATH / f"{ASSET_NAME}.fbx"
    blend_path.parent.mkdir(parents=True, exist_ok=True)
    export_path.parent.mkdir(parents=True, exist_ok=True)

    base.render_reviews()
    base.build_review_board()
    bpy.ops.wm.save_as_mainfile(filepath=str(blend_path))

    base.export_selected_fbx(export_path, lod_objects[0] + [collision])
    for lod_level, objects in enumerate(lod_objects):
        base.export_selected_fbx(export_path.with_name(f"{ASSET_NAME}_LOD{lod_level}.fbx"), objects)
    base.export_selected_fbx(export_path.with_name(f"{ASSET_NAME}_UCX.fbx"), [collision])

    width, depth, height = base.collection_bounds(lod_collections[0])
    print(f"Built {blend_path.relative_to(ROOT)}")
    print(f"Exported {export_path.relative_to(ROOT)}")
    print(f"Texture {base.TEXTURE_BC.relative_to(ROOT)}")
    for lod_level, collection in enumerate(lod_collections):
        print(f"LOD{lod_level} tris: {base.collection_triangle_count(collection)}")
    print(f"LOD0 bounds: {width:.2f}w x {depth:.2f}d x {height:.2f}h cm")
    print("Collision proxies: 1")


if __name__ == "__main__":
    build()
