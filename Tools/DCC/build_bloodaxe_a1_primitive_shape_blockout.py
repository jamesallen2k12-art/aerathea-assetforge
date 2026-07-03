#!/usr/bin/env python3
"""Build the Blood Axe A1 primitive-shape blockout proof.

This pass intentionally uses only large primitive massing shapes. It is a
silhouette and overlap review lane, not texture work, paint work, or a
game-ready DCC candidate.
"""

from __future__ import annotations

import shutil
import sys
from pathlib import Path

import bpy
from mathutils import Vector


ROOT = Path(__file__).resolve().parents[2]
ASSET_NAME = "SM_GIA_BloodAxeCairnTarget_A1_A01"
SOURCE_TARGET = "docs/assets/visual_canon/BloodAxeCairnTargets_A01/VC_GIA_BloodAxe_CairnTarget_A1.png"
GEOMETRIC_REFERENCE = "docs/assets/reference/geometric_image_training/REF_AET_GeometricImageTraining_Primitives_A01.png"
REVIEW_ROOT = ROOT / "Saved" / "Automation" / "DCC" / ASSET_NAME
DOC_ROOT = ROOT / "docs" / "assets" / "props" / ASSET_NAME
BLEND_ROOT = (
    ROOT
    / "SourceAssets"
    / "Blender"
    / "Props"
    / "Giants"
    / "BloodAxe"
    / "CairnTargets"
    / "A1"
    / f"{ASSET_NAME}_A21_PrimitiveShapeBlockout"
)
REVIEW_PROOF = REVIEW_ROOT / f"{ASSET_NAME}_PrimitiveShapeBlockout_A21.png"
DOC_PROOF = DOC_ROOT / f"{ASSET_NAME}_PrimitiveShapeBlockout_A21.png"

SOURCE_W = 395.0
SOURCE_H = 345.0
SOURCE_BASELINE_Y = 325.0
WORLD_SCALE = 0.60

sys.path.insert(0, str(ROOT))

from Tools.DCC.build_next_slice_assets import add_asset_metadata, clear_scene, setup_scene  # noqa: E402


def ensure_dir(path: Path) -> None:
    path.mkdir(parents=True, exist_ok=True)


def img_to_world(point: tuple[float, float], x_offset: float = 0.0, z_offset: float = 0.0) -> tuple[float, float]:
    x, y = point
    return ((x - (SOURCE_W * 0.5)) * WORLD_SCALE + x_offset, (SOURCE_BASELINE_Y - y) * WORLD_SCALE + z_offset)


def make_collection(name: str) -> bpy.types.Collection:
    collection = bpy.data.collections.new(name)
    bpy.context.scene.collection.children.link(collection)
    return collection


def make_material(name: str, color: tuple[float, float, float], roughness: float = 0.94) -> bpy.types.Material:
    material = bpy.data.materials.new(name)
    material.diffuse_color = (color[0], color[1], color[2], 1.0)
    material.use_nodes = True
    bsdf = material.node_tree.nodes.get("Principled BSDF")
    if bsdf is not None:
        bsdf.inputs["Base Color"].default_value = (color[0], color[1], color[2], 1.0)
        bsdf.inputs["Roughness"].default_value = roughness
        bsdf.inputs["Metallic"].default_value = 0.0
    return material


def add_extruded_primitive(
    name: str,
    collection: bpy.types.Collection,
    image_points: list[tuple[float, float]],
    material: bpy.types.Material,
    front_y: float,
    depth: float,
    primitive_source: str,
    bevel_width: float = 0.0,
    x_offset: float = 0.0,
    z_offset: float = 0.0,
    back_scale: float = 0.96,
) -> bpy.types.Object:
    world_points = [img_to_world(point, x_offset=x_offset, z_offset=z_offset) for point in image_points]
    center_x = sum(point[0] for point in world_points) / len(world_points)
    center_z = sum(point[1] for point in world_points) / len(world_points)

    verts: list[tuple[float, float, float]] = []
    front: list[int] = []
    back: list[int] = []
    for x, z in world_points:
        front.append(len(verts))
        verts.append((x, front_y, z))
        back.append(len(verts))
        bx = center_x + ((x - center_x) * back_scale)
        bz = center_z + ((z - center_z) * back_scale)
        verts.append((bx, front_y + depth, bz))

    faces: list[tuple[int, ...]] = [tuple(front), tuple(reversed(back))]
    for index in range(len(image_points)):
        next_index = (index + 1) % len(image_points)
        faces.append((front[index], back[index], back[next_index], front[next_index]))

    mesh = bpy.data.meshes.new(f"{name}_Mesh")
    mesh.from_pydata(verts, [], faces)
    mesh.update()
    obj = bpy.data.objects.new(name, mesh)
    obj.data.materials.append(material)
    obj["Aerathea.PrimitiveSource"] = primitive_source
    obj["Aerathea.ShapePass"] = "A21 primitive silhouette blockout"
    collection.objects.link(obj)

    if bevel_width > 0:
        bpy.context.view_layer.objects.active = obj
        obj.select_set(True)
        bevel = obj.modifiers.new(f"{name}_PrimitiveEdgeCatch", "BEVEL")
        bevel.width = bevel_width
        bevel.segments = 1
        bevel.affect = "EDGES"
        bpy.ops.object.modifier_apply(modifier=bevel.name)
        obj.select_set(False)

    bpy.context.view_layer.objects.active = obj
    obj.select_set(True)
    bpy.ops.object.shade_flat()
    obj.select_set(False)
    return obj


def look_at(camera: bpy.types.Object, target: Vector) -> None:
    direction = target - camera.location
    camera.rotation_euler = direction.to_track_quat("-Z", "Y").to_euler()


def configure_review_scene() -> bpy.types.Object:
    world = bpy.context.scene.world or bpy.data.worlds.new("A21_PrimitiveWorld")
    bpy.context.scene.world = world
    world.color = (0.70, 0.70, 0.68)

    scene = bpy.context.scene
    try:
        scene.render.engine = "BLENDER_EEVEE"
        scene.eevee.use_gtao = True
        scene.eevee.gtao_distance = 2.0
        scene.eevee.gtao_factor = 0.20
        scene.eevee.taa_render_samples = 48
    except (AttributeError, TypeError):
        pass
    try:
        scene.render.use_freestyle = True
        line_set = scene.view_layers[0].freestyle_settings.linesets[0]
        line_set.linestyle.thickness = 1.35
        line_set.linestyle.color = (0.08, 0.08, 0.075)
    except (AttributeError, IndexError):
        pass
    scene.view_settings.view_transform = "Standard"
    scene.view_settings.look = "None"
    scene.view_settings.exposure = 0.98
    scene.view_settings.gamma = 1.0
    scene.render.film_transparent = False

    bpy.ops.object.light_add(type="AREA", location=(-165, -350, 290))
    key = bpy.context.object
    key.name = "A21_Primitive_Key_Area"
    key.data.energy = 62000.0
    key.data.size = 340.0

    bpy.ops.object.light_add(type="AREA", location=(200, -260, 185))
    fill = bpy.context.object
    fill.name = "A21_Primitive_Fill_Area"
    fill.data.energy = 38000.0
    fill.data.size = 380.0

    target = Vector((0.0, -20.0, 88.0))
    bpy.ops.object.camera_add(location=(0.0, -525.0, 98.0))
    camera = bpy.context.object
    camera.name = "A21_PrimitiveFrontReviewCamera"
    camera.data.type = "ORTHO"
    camera.data.ortho_scale = 288.0
    look_at(camera, target)
    bpy.context.scene.camera = camera
    return camera


def render(camera: bpy.types.Object, path: Path) -> None:
    ensure_dir(path.parent)
    scene = bpy.context.scene
    scene.camera = camera
    scene.render.resolution_x = 960
    scene.render.resolution_y = 720
    scene.render.filepath = str(path)
    bpy.ops.render.render(write_still=True)


def build_primitives(collection: bpy.types.Collection, materials: dict[str, bpy.types.Material]) -> list[bpy.types.Object]:
    objects: list[bpy.types.Object] = []

    objects.append(
        add_extruded_primitive(
            "A21_GroundContact_HexagonalPrism",
            collection,
            [(17, 256), (78, 239), (184, 236), (309, 244), (387, 282), (355, 322), (38, 323)],
            materials["earth"],
            front_y=-1.0,
            depth=76.0,
            primitive_source="geometric_training: hexagonal_prism / low irregular base",
            bevel_width=0.45,
            z_offset=-5.0,
            back_scale=0.985,
        )
    )
    objects.append(
        add_extruded_primitive(
            "A21_TallRearSlab_Parallelepiped",
            collection,
            [(184, 26), (247, 43), (294, 212), (224, 232)],
            materials["stone_dark"],
            front_y=7.0,
            depth=36.0,
            primitive_source="geometric_training: parallelepiped",
            bevel_width=0.55,
            x_offset=-5.0,
            z_offset=2.0,
            back_scale=0.94,
        )
    )
    objects.append(
        add_extruded_primitive(
            "A21_LeftStack_Bottom_Parallelepiped",
            collection,
            [(27, 205), (76, 186), (145, 199), (141, 226), (58, 241), (24, 224)],
            materials["stone_mid"],
            front_y=-25.0,
            depth=32.0,
            primitive_source="geometric_training: parallelepiped flattened slab",
            bevel_width=0.4,
            x_offset=-2.0,
            z_offset=-1.0,
            back_scale=0.93,
        )
    )
    objects.append(
        add_extruded_primitive(
            "A21_LeftStack_Middle_Parallelepiped",
            collection,
            [(39, 169), (80, 151), (144, 160), (153, 181), (100, 197), (35, 187)],
            materials["stone_light"],
            front_y=-27.0,
            depth=30.0,
            primitive_source="geometric_training: parallelepiped flattened slab",
            bevel_width=0.4,
            x_offset=-4.0,
            z_offset=-1.0,
            back_scale=0.93,
        )
    )
    objects.append(
        add_extruded_primitive(
            "A21_LeftStack_Upright_TetraCut",
            collection,
            [(59, 130), (78, 121), (99, 183), (84, 220), (53, 199)],
            materials["stone_dark"],
            front_y=-29.0,
            depth=24.0,
            primitive_source="geometric_training: tetrahedron-derived wedge / narrow block",
            bevel_width=0.35,
            x_offset=-4.0,
            z_offset=-1.5,
            back_scale=0.90,
        )
    )
    objects.append(
        add_extruded_primitive(
            "A21_RightSupport_Parallelepiped",
            collection,
            [(296, 119), (341, 130), (352, 216), (318, 246), (281, 221)],
            materials["stone_mid"],
            front_y=-21.0,
            depth=39.0,
            primitive_source="geometric_training: parallelepiped upright support",
            bevel_width=0.45,
            x_offset=2.0,
            z_offset=-1.0,
            back_scale=0.93,
        )
    )
    objects.append(
        add_extruded_primitive(
            "A21_FrontDominantSlab_HexagonalPrism",
            collection,
            [(90, 132), (170, 108), (246, 139), (278, 218), (229, 298), (130, 289), (66, 215)],
            materials["stone_front"],
            front_y=-43.0,
            depth=42.0,
            primitive_source="geometric_training: hexagonal_prism / dominant front mass",
            bevel_width=0.55,
            z_offset=-1.0,
            back_scale=0.94,
        )
    )
    objects.append(
        add_extruded_primitive(
            "A21_FrontLowerLip_TetraWedge",
            collection,
            [(113, 256), (178, 269), (226, 297), (131, 289)],
            materials["stone_shadow"],
            front_y=-44.0,
            depth=23.0,
            primitive_source="geometric_training: tetrahedron-derived lower wedge",
            bevel_width=0.28,
            z_offset=-1.25,
            back_scale=0.90,
        )
    )
    objects.append(
        add_extruded_primitive(
            "A21_RightFoot_OctaCut",
            collection,
            [(274, 222), (318, 247), (344, 240), (332, 279), (286, 292)],
            materials["stone_dark"],
            front_y=-32.0,
            depth=25.0,
            primitive_source="geometric_training: octahedron-derived foot wedge",
            bevel_width=0.32,
            z_offset=-4.0,
            back_scale=0.88,
        )
    )
    objects.append(
        add_extruded_primitive(
            "A21_LeftFoot_TetraCut",
            collection,
            [(43, 236), (88, 230), (112, 259), (65, 276)],
            materials["stone_shadow"],
            front_y=-31.0,
            depth=22.0,
            primitive_source="geometric_training: tetrahedron-derived foot wedge",
            bevel_width=0.3,
            z_offset=-5.0,
            back_scale=0.88,
        )
    )

    return objects


def main() -> None:
    clear_scene()
    setup_scene()
    materials = {
        "stone_front": make_material("M_A21_Primitive_FrontStone", (0.52, 0.50, 0.45)),
        "stone_mid": make_material("M_A21_Primitive_MidStone", (0.42, 0.41, 0.38)),
        "stone_dark": make_material("M_A21_Primitive_DarkStone", (0.29, 0.29, 0.27)),
        "stone_light": make_material("M_A21_Primitive_LightStone", (0.62, 0.60, 0.55)),
        "stone_shadow": make_material("M_A21_Primitive_ShadowStone", (0.24, 0.24, 0.22)),
        "earth": make_material("M_A21_Primitive_EarthContact", (0.34, 0.29, 0.22)),
    }
    collection = make_collection(f"{ASSET_NAME}_A21_PrimitiveShapeBlockout")
    objects = build_primitives(collection, materials)

    add_asset_metadata(
        ASSET_NAME,
        f"A21 primitive-shape silhouette proof against {SOURCE_TARGET}",
        f"/Game/Aerathea/Props/Giants/BloodAxe/CairnTargets/A1/{ASSET_NAME}",
    )
    for obj in objects:
        obj["Aerathea.Asset"] = ASSET_NAME
        obj["Aerathea.Status"] = "review_only_primitive_shape_blockout_pending_visual_review"
        obj["Aerathea.SourceTarget"] = SOURCE_TARGET
        obj["Aerathea.ReferenceVocabulary"] = GEOMETRIC_REFERENCE
        obj["Aerathea.NotGameReady"] = True
        obj["Aerathea.NoTextureApproval"] = True
        obj["Aerathea.NoPaintApproval"] = True

    camera = configure_review_scene()
    render(camera, REVIEW_PROOF)
    ensure_dir(DOC_PROOF.parent)
    shutil.copyfile(REVIEW_PROOF, DOC_PROOF)

    blend_path = BLEND_ROOT / f"{ASSET_NAME}_A21_PrimitiveShapeBlockout.blend"
    ensure_dir(blend_path.parent)
    bpy.ops.wm.save_as_mainfile(filepath=str(blend_path))
    print(f"A21 primitive shape blockout proof written: {DOC_PROOF}")


if __name__ == "__main__":
    main()
