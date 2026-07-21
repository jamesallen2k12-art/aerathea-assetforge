"""Build the canonical Siege Breaker blockout from authoritative dimensions.

Run in Blender's Scripting workspace. The script creates collection SB_ASSET and
saves generated/SiegeBreaker_Blockout.blend beside this package.
"""
from pathlib import Path
import bpy

CM = 0.01
COLLECTION_NAME = "SB_ASSET"


def clear_scene():
    bpy.ops.object.select_all(action="SELECT")
    bpy.ops.object.delete(use_global=False)
    for collection in list(bpy.data.collections):
        if collection.name != "Collection":
            bpy.data.collections.remove(collection)


def move_to_collection(obj, collection):
    for current in list(obj.users_collection):
        current.objects.unlink(obj)
    collection.objects.link(obj)


def material(name, color, metallic=0.0, roughness=0.5, emission=None):
    mat = bpy.data.materials.get(name) or bpy.data.materials.new(name)
    mat.diffuse_color = (*color, 1.0)
    mat.use_nodes = True
    bsdf = mat.node_tree.nodes.get("Principled BSDF")
    bsdf.inputs["Base Color"].default_value = (*color, 1.0)
    bsdf.inputs["Metallic"].default_value = metallic
    bsdf.inputs["Roughness"].default_value = roughness
    if emission is not None:
        if "Emission Color" in bsdf.inputs:
            bsdf.inputs["Emission Color"].default_value = (*emission, 1.0)
            bsdf.inputs["Emission Strength"].default_value = 3.0
        elif "Emission" in bsdf.inputs:
            bsdf.inputs["Emission"].default_value = (*emission, 1.0)
            bsdf.inputs["Emission Strength"].default_value = 3.0
    return mat


def add_cube(name, dims_cm, location_cm, mat, bevel_cm=0.6):
    bpy.ops.mesh.primitive_cube_add(size=1, location=tuple(v * CM for v in location_cm))
    obj = bpy.context.object
    obj.name = name
    obj.dimensions = tuple(v * CM for v in dims_cm)
    bpy.ops.object.transform_apply(location=False, rotation=False, scale=True)
    bevel = obj.modifiers.new("Bevel", "BEVEL")
    bevel.width = bevel_cm * CM
    bevel.segments = 2
    obj.data.materials.append(mat)
    return obj


def add_cylinder(name, diameter_cm, length_cm, center_z_cm, mat, vertices=48):
    bpy.ops.mesh.primitive_cylinder_add(
        vertices=vertices,
        radius=diameter_cm * CM / 2,
        depth=length_cm * CM,
        location=(0, 0, center_z_cm * CM),
    )
    obj = bpy.context.object
    obj.name = name
    obj.data.materials.append(mat)
    return obj


def add_ico(name, dims_cm, location_cm, mat):
    bpy.ops.mesh.primitive_ico_sphere_add(subdivisions=2, radius=1, location=tuple(v * CM for v in location_cm))
    obj = bpy.context.object
    obj.name = name
    obj.scale = tuple(v * CM / 2 for v in dims_cm)
    bpy.ops.object.transform_apply(location=False, rotation=False, scale=True)
    obj.data.materials.append(mat)
    return obj


def main():
    clear_scene()
    scene = bpy.context.scene
    scene.unit_settings.system = "METRIC"
    scene.unit_settings.length_unit = "CENTIMETERS"

    asset = bpy.data.collections.new(COLLECTION_NAME)
    scene.collection.children.link(asset)

    stone = material("M_Stone", (0.055, 0.065, 0.075), 0.0, 0.82)
    bronze = material("M_Bronze", (0.23, 0.12, 0.045), 1.0, 0.45)
    steel = material("M_Steel", (0.08, 0.09, 0.105), 1.0, 0.38)
    leather = material("M_Leather", (0.12, 0.045, 0.02), 0.0, 0.68)
    rune = material("M_Rune_Emissive", (0.02, 0.18, 0.5), 0.1, 0.22, emission=(0.05, 0.45, 1.0))

    parts = []
    # Head envelope: X 52, Y 32, Z 38; Z = 132..170.
    parts.append(add_cube("Head_Core", (24, 26, 30), (0, 0, 151), bronze, 0.8))
    parts.append(add_cube("Head_Stone_Left", (14, 32, 38), (-19, 0, 151), stone, 1.4))
    parts.append(add_cube("Head_Stone_Right", (14, 32, 38), (19, 0, 151), stone, 1.4))
    parts.append(add_cube("Head_Brace_Left", (3, 28, 32), (-11, 0, 151), steel, 0.4))
    parts.append(add_cube("Head_Brace_Right", (3, 28, 32), (11, 0, 151), steel, 0.4))
    # Front/back rune cores, intentionally thin and non-authoritative to envelope.
    parts.append(add_cube("Rune_Core_Front", (10, 1.0, 16), (0, -13.5, 151), rune, 0.6))
    parts.append(add_cube("Rune_Core_Back", (8, 1.0, 14), (0, 13.5, 151), rune, 0.6))

    # Structural shaft Z 14..132, 118 cm.
    parts.append(add_cylinder("Shaft_Metal", 5, 118, 73, steel))
    # Visible grip Z 18..60, 42 cm.
    parts.append(add_cylinder("Grip_Leather", 5, 42, 39, leather))
    # Collars.
    for z, diameter, length in ((18, 8, 3), (60, 8, 4), (132, 10, 6)):
        parts.append(add_cylinder(f"Collar_{z}", diameter, length, z, bronze))

    # Pommel Z 0..18.
    parts.append(add_ico("Pommel", (11, 9, 18), (0, 0, 9), bronze))
    parts.append(add_cube("Pommel_Rune_Front", (5, 1, 6), (0, -4.6, 9), rune, 0.3))
    parts.append(add_cube("Pommel_Rune_Back", (4, 1, 5), (0, 4.6, 9), rune, 0.3))

    for obj in parts:
        move_to_collection(obj, asset)
        obj["asset_name"] = "Siege Breaker"

    root = bpy.data.objects.new("SiegeBreaker_ROOT", None)
    asset.objects.link(root)
    root["overall_length_cm"] = 170
    root["head_width_cm"] = 52
    root["head_height_cm"] = 38
    root["head_depth_cm"] = 32
    root["shaft_length_cm"] = 118
    root["shaft_pommel_overlap_cm"] = 4
    for obj in parts:
        obj.parent = root

    out = Path(__file__).resolve().parent.parent / "generated"
    out.mkdir(parents=True, exist_ok=True)
    blend_path = out / "SiegeBreaker_Blockout.blend"
    bpy.ops.wm.save_as_mainfile(filepath=str(blend_path))
    print(f"Saved canonical blockout: {blend_path}")


if __name__ == "__main__":
    main()
