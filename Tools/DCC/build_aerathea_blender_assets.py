#!/usr/bin/env python3
"""Build Aerathea Blender source files and Unreal FBX exports.

Run with:
    blender --background --python Tools/DCC/build_aerathea_blender_assets.py

The first-slice geometry reuses the approved deterministic mesh definitions
from generate_first_slice_meshes.py, but this script creates native .blend
source files and exports FBX from Blender.
"""

from __future__ import annotations

import math
import sys
from dataclasses import dataclass
from pathlib import Path

import bpy
from mathutils import Euler


ROOT = Path(__file__).resolve().parents[2]
SOURCE_ROOT = ROOT / "SourceAssets"
BLENDER_ROOT = SOURCE_ROOT / "Blender"
EXPORT_ROOT = SOURCE_ROOT / "Exports"

sys.path.insert(0, str(ROOT))

from Tools.DCC.generate_first_slice_meshes import (  # noqa: E402
    Mesh,
    create_common_materials,
    ground_tile,
    portal_arch,
    target_dummy,
    workshop_crate,
)


@dataclass(frozen=True)
class AssetBuild:
    rel_path: str
    factory: object

    @property
    def name(self) -> str:
        return self.rel_path.split("/")[-1]

    @property
    def blend_path(self) -> Path:
        return BLENDER_ROOT / self.rel_path / f"{self.name}.blend"

    @property
    def export_path(self) -> Path:
        return EXPORT_ROOT / self.rel_path / f"{self.name}.fbx"


def add_triangular_prism(
    mesh: Mesh,
    name: str,
    x_base: float,
    x_tip: float,
    half_width: float,
    half_thickness: float,
    z: float,
    material: str,
) -> None:
    obj = mesh.add_object(name, material)
    obj.verts.extend(
        [
            (x_base, -half_width, z - half_thickness),
            (x_base, half_width, z - half_thickness),
            (x_tip, 0, z - half_thickness),
            (x_base, -half_width, z + half_thickness),
            (x_base, half_width, z + half_thickness),
            (x_tip, 0, z + half_thickness),
        ]
    )
    obj.faces.extend(
        [
            (1, 2, 3),
            (4, 6, 5),
            (1, 4, 5, 2),
            (2, 5, 6, 3),
            (3, 6, 4, 1),
        ]
    )


def aether_knife() -> Mesh:
    mesh = Mesh("SM_MKG_AetherKnife_A01")
    m = create_common_materials(mesh)
    add_triangular_prism(mesh, "Blade_DarkIron_BroadTri", 3, 41, 7, 1.7, 0, m["dark_iron"])
    mesh.add_box("Blade_Spine_Brass", (14, 0, 2.2), (25, 2.3, 1.2), m["brass"])
    mesh.add_box("Guard_Brass_Block", (0, 0, 0), (5, 18, 8), m["brass"])
    mesh.add_cylinder("Grip_Leather_Wrap", (-13, 0, 0), 4.3, 23, m["leather"], "x", 14)
    mesh.add_cylinder("Grip_Brass_EndBand", (-2, 0, 0), 4.8, 3, m["brass"], "x", 14)
    mesh.add_cylinder("Pommel_Brass_Cap", (-26, 0, 0), 5.5, 5, m["brass"], "x", 14)
    mesh.add_diamond("Aetherium_Pommel_Inset", (-29, 0, 0), (3.5, 5.5, 5.5), m["aetherium"])
    mesh.add_box("UCX_SM_MKG_AetherKnife_A01_00", (5, 0, 0), (72, 20, 10), m["stone"])
    return mesh


def aether_core_unit() -> Mesh:
    mesh = Mesh("SM_MKG_AetherCoreUnit_A01")
    m = create_common_materials(mesh)
    mesh.add_box("Housing_DarkIron_Frame", (0, 0, 26), (45, 22, 52), m["dark_iron"])
    mesh.add_box("Front_Brass_Plate", (0, -12.4, 30), (38, 3, 40), m["brass"])
    mesh.add_box("Rear_Mount_DarkIron", (0, 13, 25), (38, 5, 48), m["dark_iron"])
    mesh.add_diamond("Core_Aetherium_Crystal", (0, -15, 31), (16, 7, 24), m["aetherium"])
    mesh.add_box("Core_Window_Frame", (0, -16.2, 31), (24, 3, 31), m["brass"])
    for x in (-31, 31):
        mesh.add_cylinder(f"Side_Cylinder_{x}", (x, 0, 31), 7, 44, m["brass"], "z", 16)
        mesh.add_box(f"Side_Strut_{x}_Upper", (x, -1, 51), (10, 27, 5), m["dark_iron"])
        mesh.add_box(f"Side_Strut_{x}_Lower", (x, -1, 11), (10, 27, 5), m["dark_iron"])
    for x in (-18, 18):
        mesh.add_box(f"Leather_Strap_{x}", (x, 14.5, 27), (8, 4, 56), m["leather"])
    mesh.add_cylinder("Top_Handle_Brass", (0, 0, 57), 4, 34, m["brass"], "x", 14)
    mesh.add_box("UCX_SM_MKG_AetherCoreUnit_A01_00", (0, 0, 28), (72, 34, 62), m["stone"])
    return mesh


def spark_pistol() -> Mesh:
    mesh = Mesh("SM_MKG_SparkPistol_A01")
    m = create_common_materials(mesh)
    mesh.add_cylinder("Barrel_DarkIron_Thick", (16, 0, 8), 4.8, 36, m["dark_iron"], "x", 18)
    mesh.add_cylinder("Muzzle_Ring_DarkIron", (36, 0, 8), 6.2, 7, m["dark_iron"], "x", 18)
    mesh.add_cylinder("Chamber_Brass_Round", (1, 0, 8), 9.0, 17, m["brass"], "y", 18)
    mesh.add_box("Receiver_DarkIron_Block", (-9, 0, 7), (18, 14, 13), m["dark_iron"])
    mesh.add_box("Grip_Leather_Compact", (-14, 0, -9), (8, 11, 27), m["leather"])
    mesh.add_box("Grip_Brass_Base", (-14, 0, -23), (12, 13, 4), m["brass"])
    mesh.add_box("Trigger_Guard_Brass_Front", (-3, 0, -7), (4, 3, 12), m["brass"])
    mesh.add_box("Trigger_Guard_Brass_Bottom", (-8, 0, -13), (13, 3, 4), m["brass"])
    mesh.add_diamond("Aetherium_Capacitor_Side", (2, -10, 8), (10, 5, 12), m["aetherium"])
    mesh.add_box("UCX_SM_MKG_SparkPistol_A01_00", (8, 0, 1), (58, 22, 42), m["stone"])
    return mesh


def aetherium_grenade() -> Mesh:
    mesh = Mesh("SM_MKG_AetheriumGrenade_A01")
    m = create_common_materials(mesh)
    mesh.add_ellipsoid("Shell_DarkIron_Oval", (0, 0, 0), (11, 11, 13), m["dark_iron"], 8, 18)
    mesh.add_cylinder("Equator_Brass_Rib", (0, 0, 0), 11.8, 4, m["brass"], "z", 18)
    for angle in (0, 60, 120):
        x = math.cos(math.radians(angle)) * 5.5
        y = math.sin(math.radians(angle)) * 5.5
        mesh.add_box(f"Vertical_Brass_Rib_{angle}", (x, y, 0), (4, 3, 25), m["brass"])
    mesh.add_diamond("Core_Aetherium_Window", (0, -12, 0), (9, 4, 10), m["aetherium"])
    mesh.add_cylinder("Top_Cap_Brass", (0, 0, 16), 6, 7, m["brass"], "z", 16)
    mesh.add_cylinder("Pull_Ring_DarkIron", (0, 0, 23), 5, 2.2, m["dark_iron"], "x", 14)
    mesh.add_box("UCX_SM_MKG_AetheriumGrenade_A01_00", (0, 0, 1), (27, 27, 34), m["stone"])
    return mesh


ASSETS = [
    AssetBuild("Props/Training/SM_AET_TargetDummy_A01", target_dummy),
    AssetBuild("Props/Portal/SM_AET_PortalArch_A01", portal_arch),
    AssetBuild("Props/Environment/SM_AET_ModularGroundTile_A01", ground_tile),
    AssetBuild("Props/Mekgineer/SM_MKG_WorkshopPropCrate_A01", workshop_crate),
    AssetBuild("Kits/Mekgineer/Armory/SM_MKG_AetherKnife_A01", aether_knife),
    AssetBuild("Kits/Mekgineer/Armory/SM_MKG_AetherCoreUnit_A01", aether_core_unit),
    AssetBuild("Kits/Mekgineer/Armory/SM_MKG_SparkPistol_A01", spark_pistol),
    AssetBuild("Kits/Mekgineer/Armory/SM_MKG_AetheriumGrenade_A01", aetherium_grenade),
]


def clear_scene() -> None:
    bpy.ops.object.select_all(action="SELECT")
    bpy.ops.object.delete()


def setup_scene() -> None:
    scene = bpy.context.scene
    scene.unit_settings.system = "METRIC"
    scene.unit_settings.scale_length = 0.01
    try:
        scene.render.engine = "BLENDER_EEVEE_NEXT"
    except TypeError:
        scene.render.engine = "BLENDER_EEVEE"


def get_material(name: str, color: tuple[float, float, float]) -> bpy.types.Material:
    material = bpy.data.materials.new(name)
    material.diffuse_color = (color[0], color[1], color[2], 1.0)
    material.use_nodes = True
    bsdf = material.node_tree.nodes.get("Principled BSDF")
    if bsdf is not None:
        bsdf.inputs["Base Color"].default_value = (color[0], color[1], color[2], 1.0)
        bsdf.inputs["Roughness"].default_value = 0.82
        if "Aetherium" in name or "Glow" in name:
            bsdf.inputs["Emission Color"].default_value = (0.0, 0.8, 2.8, 1.0)
            bsdf.inputs["Emission Strength"].default_value = 1.6
    return material


def mesh_to_blender(mesh: Mesh) -> None:
    materials = {name: get_material(name, color) for name, color in mesh.materials.items()}
    for source_obj in mesh.objects:
        blender_mesh = bpy.data.meshes.new(source_obj.name)
        faces = [tuple(index - 1 for index in face) for face in source_obj.faces]
        blender_mesh.from_pydata(source_obj.verts, [], faces)
        blender_mesh.update()

        obj = bpy.data.objects.new(source_obj.name, blender_mesh)
        bpy.context.collection.objects.link(obj)
        obj.data.materials.append(materials[source_obj.material])
        for polygon in obj.data.polygons:
            polygon.material_index = 0

        if source_obj.name.startswith("UCX_"):
            obj.display_type = "WIRE"
            obj.show_wire = True


def add_asset_metadata(asset_name: str) -> None:
    empty = bpy.data.objects.new(f"{asset_name}_ProductionNotes", None)
    empty.empty_display_type = "PLAIN_AXES"
    empty.empty_display_size = 8
    empty["AeratheaStatus"] = "Blender source generated from approved production package"
    empty["Units"] = "Centimeters"
    empty["Pipeline"] = "Source .blend -> FBX -> Unreal static mesh import"
    bpy.context.collection.objects.link(empty)


def save_and_export(asset: AssetBuild) -> None:
    clear_scene()
    setup_scene()

    mesh = asset.factory()
    mesh_to_blender(mesh)
    add_asset_metadata(asset.name)

    asset.blend_path.parent.mkdir(parents=True, exist_ok=True)
    asset.export_path.parent.mkdir(parents=True, exist_ok=True)

    bpy.ops.wm.save_as_mainfile(filepath=str(asset.blend_path))
    bpy.ops.export_scene.fbx(
        filepath=str(asset.export_path),
        use_selection=False,
        object_types={"MESH"},
        mesh_smooth_type="FACE",
        global_scale=1.0,
        apply_unit_scale=False,
        apply_scale_options="FBX_SCALE_NONE",
        axis_forward="X",
        axis_up="Z",
        bake_space_transform=False,
        add_leaf_bones=False,
    )
    print(f"Built {asset.blend_path.relative_to(ROOT)}")
    print(f"Exported {asset.export_path.relative_to(ROOT)}")


def main() -> None:
    for asset in ASSETS:
        save_and_export(asset)


if __name__ == "__main__":
    main()
