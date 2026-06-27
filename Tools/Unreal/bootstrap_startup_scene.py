import unreal


LEVEL_PATH = "/Game/Aerathea/Maps/L_Aerathea_Startup"
MATERIAL_PATH = "/Game/Aerathea/Materials"
BOOTSTRAP_TAG = "AET_BOOTSTRAP"


def ensure_directory(path):
    if not unreal.EditorAssetLibrary.does_directory_exist(path):
        unreal.EditorAssetLibrary.make_directory(path)


def load_or_create_level():
    if unreal.EditorAssetLibrary.does_asset_exist(LEVEL_PATH):
        unreal.log("Loading startup level: {}".format(LEVEL_PATH))
        if not unreal.EditorLevelLibrary.load_level(LEVEL_PATH):
            raise RuntimeError("Failed to load startup level: {}".format(LEVEL_PATH))
    else:
        unreal.log("Creating startup level: {}".format(LEVEL_PATH))
        if not unreal.EditorLevelLibrary.new_level(LEVEL_PATH):
            raise RuntimeError("Failed to create startup level: {}".format(LEVEL_PATH))


def color_material(name, color, roughness=0.85, metallic=0.0, emissive=None):
    ensure_directory(MATERIAL_PATH)
    asset_path = "{}/{}".format(MATERIAL_PATH, name)

    if unreal.EditorAssetLibrary.does_asset_exist(asset_path):
        return unreal.load_asset(asset_path)

    asset_tools = unreal.AssetToolsHelpers.get_asset_tools()
    material = asset_tools.create_asset(
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


def tagged(actor):
    actor.set_editor_property("tags", [unreal.Name(BOOTSTRAP_TAG)])
    return actor


def clear_bootstrap_actors():
    for actor in unreal.EditorLevelLibrary.get_all_level_actors():
        if unreal.Name(BOOTSTRAP_TAG) in actor.get_editor_property("tags"):
            unreal.EditorLevelLibrary.destroy_actor(actor)


def spawn_mesh(label, mesh, location, rotation, scale, material=None):
    actor = unreal.EditorLevelLibrary.spawn_actor_from_class(unreal.StaticMeshActor, location, rotation)
    actor.set_actor_label(label)
    actor.set_actor_scale3d(scale)
    tagged(actor)

    component = actor.get_component_by_class(unreal.StaticMeshComponent)
    if component is None:
        raise RuntimeError("Static mesh actor has no StaticMeshComponent: {}".format(label))

    component.set_static_mesh(mesh)
    if material is not None:
        component.set_material(0, material)

    return actor


def spawn_light(label, cls, location, rotation):
    actor = unreal.EditorLevelLibrary.spawn_actor_from_class(cls, location, rotation)
    actor.set_actor_label(label)
    tagged(actor)
    return actor


def safe_set(obj, prop, value):
    try:
        obj.set_editor_property(prop, value)
    except Exception:
        pass


def spawn_text(label, text, location, rotation, size=64.0):
    actor = unreal.EditorLevelLibrary.spawn_actor_from_class(
        unreal.TextRenderActor,
        location,
        rotation,
    )
    actor.set_actor_label(label)
    tagged(actor)
    component = actor.get_component_by_class(unreal.TextRenderComponent)
    if component is not None:
        component.set_text(text)
        component.set_editor_property("world_size", size)
    return actor


def build_scene():
    stone = color_material(
        "M_AET_Stone_Handpainted_A01",
        unreal.LinearColor(0.34, 0.36, 0.37, 1.0),
    )
    timber = color_material(
        "M_AET_Timber_Handpainted_A01",
        unreal.LinearColor(0.36, 0.22, 0.12, 1.0),
    )
    dark_iron = color_material(
        "M_AET_DarkIron_A01",
        unreal.LinearColor(0.08, 0.09, 0.10, 1.0),
        roughness=0.7,
        metallic=0.65,
    )
    brass = color_material(
        "M_AET_Brass_A01",
        unreal.LinearColor(0.78, 0.55, 0.25, 1.0),
        roughness=0.55,
        metallic=0.8,
    )
    aetherium = color_material(
        "M_AET_AetheriumGlow_Blue_A01",
        unreal.LinearColor(0.05, 0.35, 0.95, 1.0),
        roughness=0.25,
        metallic=0.0,
        emissive=unreal.LinearColor(0.0, 1.2, 3.5, 1.0),
    )

    cube = unreal.load_asset("/Engine/BasicShapes/Cube.Cube")
    plane = unreal.load_asset("/Engine/BasicShapes/Plane.Plane")
    sphere = unreal.load_asset("/Engine/BasicShapes/Sphere.Sphere")
    cylinder = unreal.load_asset("/Engine/BasicShapes/Cylinder.Cylinder")

    if None in (cube, plane, sphere, cylinder):
        raise RuntimeError("Failed to load one or more Engine BasicShapes meshes")

    clear_bootstrap_actors()

    spawn_mesh(
        "AET_BOOT_GroundTile_20m_A01",
        plane,
        unreal.Vector(0, 0, 0),
        unreal.Rotator(0, 0, 0),
        unreal.Vector(20, 20, 1),
        stone,
    )

    spawn_mesh(
        "AET_BOOT_PlayerScale_180cm",
        cylinder,
        unreal.Vector(-350, -350, 90),
        unreal.Rotator(0, 0, 0),
        unreal.Vector(0.35, 0.35, 1.8),
        brass,
    )
    spawn_mesh(
        "AET_BOOT_GnomeScale_110cm",
        cylinder,
        unreal.Vector(-260, -350, 55),
        unreal.Rotator(0, 0, 0),
        unreal.Vector(0.28, 0.28, 1.1),
        timber,
    )
    spawn_mesh(
        "AET_BOOT_MinotaurScale_270cm",
        cylinder,
        unreal.Vector(-460, -350, 135),
        unreal.Rotator(0, 0, 0),
        unreal.Vector(0.55, 0.55, 2.7),
        dark_iron,
    )

    # Rough portal silhouette: chunky columns, broad capstone, and restrained blue core.
    spawn_mesh(
        "AET_BOOT_PortalArch_LeftColumn_A01",
        cube,
        unreal.Vector(250, 0, 180),
        unreal.Rotator(0, 0, 0),
        unreal.Vector(0.55, 0.7, 3.6),
        stone,
    )
    spawn_mesh(
        "AET_BOOT_PortalArch_RightColumn_A01",
        cube,
        unreal.Vector(450, 0, 180),
        unreal.Rotator(0, 0, 0),
        unreal.Vector(0.55, 0.7, 3.6),
        stone,
    )
    spawn_mesh(
        "AET_BOOT_PortalArch_Capstone_A01",
        cube,
        unreal.Vector(350, 0, 370),
        unreal.Rotator(0, 0, 0),
        unreal.Vector(2.7, 0.85, 0.55),
        stone,
    )
    spawn_mesh(
        "AET_BOOT_PortalCore_Aetherium_A01",
        sphere,
        unreal.Vector(350, 0, 185),
        unreal.Rotator(0, 0, 0),
        unreal.Vector(1.1, 0.12, 1.65),
        aetherium,
    )

    spawn_mesh(
        "AET_BOOT_TargetDummy_Blockout_A01",
        cylinder,
        unreal.Vector(-50, 350, 105),
        unreal.Rotator(0, 0, 0),
        unreal.Vector(0.45, 0.45, 2.1),
        timber,
    )
    spawn_mesh(
        "AET_BOOT_TargetDummy_Crossbar_A01",
        cube,
        unreal.Vector(-50, 350, 180),
        unreal.Rotator(0, 0, 0),
        unreal.Vector(1.6, 0.18, 0.18),
        dark_iron,
    )

    key_light = spawn_light(
        "AET_BOOT_KeyLight_Directional",
        unreal.DirectionalLight,
        unreal.Vector(0, 0, 800),
        unreal.Rotator(-45, -35, 0),
    )
    key_component = key_light.get_component_by_class(unreal.DirectionalLightComponent)
    if key_component is not None:
        safe_set(key_component, "forward_shading_priority", 1)
        safe_set(key_component, "ForwardShadingPriority", 1)
    spawn_light(
        "AET_BOOT_SkyLight",
        unreal.SkyLight,
        unreal.Vector(0, 0, 400),
        unreal.Rotator(0, 0, 0),
    )

    camera = unreal.EditorLevelLibrary.spawn_actor_from_class(
        unreal.CameraActor,
        unreal.Vector(-720, -920, 520),
        unreal.Rotator(-24, 0, -38),
    )
    camera.set_actor_label("AET_BOOT_Camera_Overview")
    tagged(camera)

    spawn_text(
        "AET_BOOT_Label_StyleTarget",
        "Aerathea Classic+ Bootstrap",
        unreal.Vector(0, -520, 240),
        unreal.Rotator(0, 0, 0),
        52.0,
    )


def main():
    load_or_create_level()
    build_scene()

    if not unreal.EditorLevelLibrary.save_current_level():
        raise RuntimeError("Failed to save current level")

    unreal.EditorAssetLibrary.save_directory("/Game/Aerathea", only_if_is_dirty=False, recursive=True)
    unreal.log("Aerathea startup bootstrap scene complete.")


main()
