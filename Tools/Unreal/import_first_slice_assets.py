from pathlib import Path

import unreal


ROOT = Path(__file__).resolve().parents[2]
LEVEL_PATH = "/Game/Aerathea/Maps/L_Aerathea_Startup"
MATERIAL_PATH = "/Game/Aerathea/Materials"
BLUEPRINT_PATH = "/Game/Aerathea/Blueprints/Props"
FIRST_SLICE_TAG = "AET_FIRST_SLICE"

ASSETS = [
    {
        "name": "SM_AET_TargetDummy_A01",
        "source": ROOT / "SourceAssets/Exports/Props/Training/SM_AET_TargetDummy_A01/SM_AET_TargetDummy_A01.fbx",
        "destination": "/Game/Aerathea/Props/Training",
    },
    {
        "name": "SM_AET_PortalArch_A01",
        "source": ROOT / "SourceAssets/Exports/Props/Portal/SM_AET_PortalArch_A01/SM_AET_PortalArch_A01.fbx",
        "destination": "/Game/Aerathea/Props/Portal",
    },
    {
        "name": "SM_AET_ModularGroundTile_A01",
        "source": ROOT / "SourceAssets/Exports/Props/Environment/SM_AET_ModularGroundTile_A01/SM_AET_ModularGroundTile_A01.fbx",
        "destination": "/Game/Aerathea/Props/Environment",
    },
    {
        "name": "SM_MKG_WorkshopPropCrate_A01",
        "source": ROOT / "SourceAssets/Exports/Props/Mekgineer/SM_MKG_WorkshopPropCrate_A01/SM_MKG_WorkshopPropCrate_A01.fbx",
        "destination": "/Game/Aerathea/Props/Mekgineer",
    },
]

REPLACED_BLOCKOUT_LABELS = {
    "AET_BOOT_GroundTile_20m_A01",
    "AET_BOOT_PortalArch_LeftColumn_A01",
    "AET_BOOT_PortalArch_RightColumn_A01",
    "AET_BOOT_PortalArch_Capstone_A01",
    "AET_BOOT_PortalCore_Aetherium_A01",
    "AET_BOOT_TargetDummy_Blockout_A01",
    "AET_BOOT_TargetDummy_Crossbar_A01",
}


def ensure_directory(path):
    if not unreal.EditorAssetLibrary.does_directory_exist(path):
        unreal.EditorAssetLibrary.make_directory(path)


def safe_set(obj, prop, value):
    try:
        obj.set_editor_property(prop, value)
    except Exception as exc:
        unreal.log_warning("Could not set {}.{}: {}".format(type(obj).__name__, prop, exc))


def color_material(name, color, roughness=0.85, metallic=0.0, emissive=None):
    ensure_directory(MATERIAL_PATH)
    asset_path = "{}/{}".format(MATERIAL_PATH, name)

    if unreal.EditorAssetLibrary.does_asset_exist(asset_path):
        return unreal.load_asset(asset_path)

    material = unreal.AssetToolsHelpers.get_asset_tools().create_asset(
        asset_name=name,
        package_path=MATERIAL_PATH,
        asset_class=unreal.Material,
        factory=unreal.MaterialFactoryNew(),
    )
    if material is None:
        raise RuntimeError("Failed to create material {}".format(asset_path))

    mat_lib = unreal.MaterialEditingLibrary
    base = mat_lib.create_material_expression(
        material,
        unreal.MaterialExpressionConstant3Vector,
        -420,
        -80,
    )
    base.set_editor_property("constant", color)
    mat_lib.connect_material_property(base, "", unreal.MaterialProperty.MP_BASE_COLOR)

    rough = mat_lib.create_material_expression(
        material,
        unreal.MaterialExpressionConstant,
        -420,
        120,
    )
    rough.set_editor_property("r", roughness)
    mat_lib.connect_material_property(rough, "", unreal.MaterialProperty.MP_ROUGHNESS)

    metal = mat_lib.create_material_expression(
        material,
        unreal.MaterialExpressionConstant,
        -420,
        260,
    )
    metal.set_editor_property("r", metallic)
    mat_lib.connect_material_property(metal, "", unreal.MaterialProperty.MP_METALLIC)

    if emissive is not None:
        glow = mat_lib.create_material_expression(
            material,
            unreal.MaterialExpressionConstant3Vector,
            -420,
            420,
        )
        glow.set_editor_property("constant", emissive)
        mat_lib.connect_material_property(glow, "", unreal.MaterialProperty.MP_EMISSIVE_COLOR)

    mat_lib.recompile_material(material)
    unreal.EditorAssetLibrary.save_asset(asset_path)
    return material


def ensure_materials():
    return {
        "M_AET_Stone_Handpainted_A01": color_material(
            "M_AET_Stone_Handpainted_A01",
            unreal.LinearColor(0.34, 0.36, 0.37, 1.0),
        ),
        "M_AET_Timber_Handpainted_A01": color_material(
            "M_AET_Timber_Handpainted_A01",
            unreal.LinearColor(0.36, 0.22, 0.12, 1.0),
        ),
        "M_AET_DarkIron_A01": color_material(
            "M_AET_DarkIron_A01",
            unreal.LinearColor(0.08, 0.09, 0.10, 1.0),
            roughness=0.7,
            metallic=0.65,
        ),
        "M_AET_Brass_A01": color_material(
            "M_AET_Brass_A01",
            unreal.LinearColor(0.78, 0.55, 0.25, 1.0),
            roughness=0.55,
            metallic=0.8,
        ),
        "M_AET_AetheriumGlow_Blue_A01": color_material(
            "M_AET_AetheriumGlow_Blue_A01",
            unreal.LinearColor(0.05, 0.35, 0.95, 1.0),
            roughness=0.25,
            metallic=0.0,
            emissive=unreal.LinearColor(0.0, 1.2, 3.5, 1.0),
        ),
        "M_AET_Straw_A01": color_material(
            "M_AET_Straw_A01",
            unreal.LinearColor(0.72, 0.52, 0.20, 1.0),
        ),
        "M_AET_Leather_Dark_A01": color_material(
            "M_AET_Leather_Dark_A01",
            unreal.LinearColor(0.19, 0.11, 0.07, 1.0),
        ),
        "M_AET_PackedEarth_A01": color_material(
            "M_AET_PackedEarth_A01",
            unreal.LinearColor(0.25, 0.19, 0.13, 1.0),
        ),
        "M_AET_Moss_A01": color_material(
            "M_AET_Moss_A01",
            unreal.LinearColor(0.18, 0.30, 0.16, 1.0),
        ),
    }


def import_static_mesh(entry):
    if not entry["source"].exists():
        raise RuntimeError("Missing source FBX: {}".format(entry["source"]))

    ensure_directory(entry["destination"])

    fbx_ui = unreal.FbxImportUI()
    safe_set(fbx_ui, "import_mesh", True)
    safe_set(fbx_ui, "import_as_skeletal", False)
    safe_set(fbx_ui, "import_materials", False)
    safe_set(fbx_ui, "import_textures", False)

    static_data = fbx_ui.static_mesh_import_data
    safe_set(static_data, "combine_meshes", True)
    safe_set(static_data, "auto_generate_collision", False)
    safe_set(static_data, "generate_lightmap_u_vs", True)
    safe_set(static_data, "remove_degenerates", True)
    safe_set(static_data, "one_convex_hull_per_ucx", False)

    task = unreal.AssetImportTask()
    task.set_editor_property("filename", str(entry["source"]))
    task.set_editor_property("destination_path", entry["destination"])
    task.set_editor_property("destination_name", entry["name"])
    task.set_editor_property("replace_existing", True)
    task.set_editor_property("automated", True)
    task.set_editor_property("save", True)
    task.set_editor_property("options", fbx_ui)

    unreal.AssetToolsHelpers.get_asset_tools().import_asset_tasks([task])
    asset_path = "{}/{}".format(entry["destination"], entry["name"])
    mesh = unreal.load_asset(asset_path)
    if mesh is None:
        raise RuntimeError("Import did not produce expected static mesh: {}".format(asset_path))

    safe_set(mesh, "light_map_resolution", 64)
    unreal.EditorAssetLibrary.save_asset(asset_path)
    unreal.log("Imported first-slice static mesh: {}".format(asset_path))
    return mesh


def assign_project_materials(mesh, project_materials):
    static_materials = mesh.get_editor_property("static_materials")
    count = len(static_materials)
    for index, static_material in enumerate(static_materials):
        slot_name = str(static_material.get_editor_property("material_slot_name"))
        current = static_material.get_editor_property("material_interface")
        current_name = current.get_name() if current is not None else slot_name
        material = project_materials.get(slot_name) or project_materials.get(current_name)
        if material is not None:
            mesh.set_material(index, material)
    unreal.EditorAssetLibrary.save_loaded_asset(mesh)
    unreal.log("Synced {} material slots for {}".format(count, mesh.get_name()))


def ensure_portal_blueprint():
    ensure_directory(BLUEPRINT_PATH)
    asset_path = "{}/BP_AET_Portal_A01".format(BLUEPRINT_PATH)
    if unreal.EditorAssetLibrary.does_asset_exist(asset_path):
        return unreal.load_asset(asset_path)

    factory = unreal.BlueprintFactory()
    factory.set_editor_property("parent_class", unreal.Actor)
    blueprint = unreal.AssetToolsHelpers.get_asset_tools().create_asset(
        asset_name="BP_AET_Portal_A01",
        package_path=BLUEPRINT_PATH,
        asset_class=unreal.Blueprint,
        factory=factory,
    )
    if blueprint is None:
        raise RuntimeError("Failed to create {}".format(asset_path))
    unreal.EditorAssetLibrary.save_asset(asset_path)
    unreal.log("Created portal Blueprint asset shell: {}".format(asset_path))
    return blueprint


def tag_actor(actor):
    actor.set_editor_property("tags", [unreal.Name(FIRST_SLICE_TAG)])
    return actor


def clear_replaced_startup_actors():
    for actor in list(unreal.EditorLevelLibrary.get_all_level_actors()):
        label = actor.get_actor_label()
        tags = actor.get_editor_property("tags")
        if label in REPLACED_BLOCKOUT_LABELS or unreal.Name(FIRST_SLICE_TAG) in tags:
            unreal.EditorLevelLibrary.destroy_actor(actor)


def spawn_static_mesh(label, mesh, location, rotation=None, scale=None, material=None):
    rotation = rotation or unreal.Rotator(0, 0, 0)
    scale = scale or unreal.Vector(1, 1, 1)
    actor = unreal.EditorLevelLibrary.spawn_actor_from_class(
        unreal.StaticMeshActor,
        location,
        rotation,
    )
    actor.set_actor_label(label)
    actor.set_actor_scale3d(scale)
    tag_actor(actor)

    component = actor.get_component_by_class(unreal.StaticMeshComponent)
    if component is None:
        raise RuntimeError("Static mesh actor has no StaticMeshComponent: {}".format(label))
    component.set_static_mesh(mesh)
    if material is not None:
        component.set_material(0, material)
    return actor


def update_startup_level(meshes, materials):
    if not unreal.EditorLevelLibrary.load_level(LEVEL_PATH):
        raise RuntimeError("Failed to load level: {}".format(LEVEL_PATH))

    clear_replaced_startup_actors()

    tile = meshes["SM_AET_ModularGroundTile_A01"]
    for ix, x in enumerate(range(-800, 801, 400)):
        for iy, y in enumerate(range(-800, 801, 400)):
            spawn_static_mesh(
                "AET_PROD_GroundTile_A01_R{}_C{}".format(iy + 1, ix + 1),
                tile,
                unreal.Vector(x, y, 0),
            )

    spawn_static_mesh(
        "AET_PROD_TargetDummy_A01",
        meshes["SM_AET_TargetDummy_A01"],
        unreal.Vector(-50, 350, 0),
    )
    spawn_static_mesh(
        "AET_PROD_PortalArch_A01",
        meshes["SM_AET_PortalArch_A01"],
        unreal.Vector(350, 0, 0),
    )
    spawn_static_mesh(
        "AET_PROD_WorkshopCrate_A01",
        meshes["SM_MKG_WorkshopPropCrate_A01"],
        unreal.Vector(-235, 260, 0),
    )

    sphere = unreal.load_asset("/Engine/BasicShapes/Sphere.Sphere")
    if sphere is None:
        raise RuntimeError("Failed to load Engine sphere for portal core")
    spawn_static_mesh(
        "AET_PROD_PortalCore_Aetherium_A01",
        sphere,
        unreal.Vector(350, -18, 210),
        scale=unreal.Vector(1.05, 0.12, 1.55),
        material=materials["M_AET_AetheriumGlow_Blue_A01"],
    )

    if not unreal.EditorLevelLibrary.save_current_level():
        raise RuntimeError("Failed to save current level")
    unreal.EditorAssetLibrary.save_directory("/Game/Aerathea", only_if_is_dirty=False, recursive=True)
    unreal.log("Updated startup level with first-slice production assets.")


def main():
    materials = ensure_materials()
    meshes = {}
    for entry in ASSETS:
        mesh = import_static_mesh(entry)
        assign_project_materials(mesh, materials)
        meshes[entry["name"]] = mesh

    ensure_portal_blueprint()
    update_startup_level(meshes, materials)
    unreal.log("Aerathea first-slice import complete.")


main()
