import math

import unreal


LEVEL_PATH = "/Game/Aerathea/Maps/L_Aerathea_ReviewIsland"
MATERIAL_PATH = "/Game/Aerathea/Materials/Review"
REVIEW_TAG = "AET_REVIEW_ISLAND"
SLOT_TAG = "AET_REVIEW_SLOT"
TARGET_TAG = "AET_REVIEW_TARGET"
REVIEW_CAMERA_TAG = "AET_REVIEW_CAMERA"

CURRENT_ASSET = {
    "label": "AET_REVIEW_CurrentAsset_BloodAxeCairn_A01",
    "mesh": "/Game/Aerathea/Props/Giants/BloodAxe/Cairns/SM_GIA_BloodAxeCairnSlabCluster_A01_Test2Manual",
    "materials": [
        "/Game/Aerathea/Materials/Instances/MI_GIA_BloodAxeCairnSlabCluster_A01_Test2Manual_Projection",
        "/Game/Aerathea/Materials/Instances/MI_GIA_BloodAxeCairnSlabCluster_A01_Test2Manual_SideStone",
    ],
    "location": unreal.Vector(0.0, 0.0, 8.0),
    "yaw": -18.0,
}


def review_rotator(pitch, yaw, roll=0.0):
    return unreal.Rotator(roll, pitch, yaw)


def look_at_rotation(source, target):
    math_library = getattr(unreal, "MathLibrary", None)
    if math_library is not None:
        try:
            return math_library.find_look_at_rotation(source, target)
        except Exception:
            pass
    dx = target.x - source.x
    dy = target.y - source.y
    dz = target.z - source.z
    yaw = math.degrees(math.atan2(dy, dx))
    horizontal = math.sqrt((dx * dx) + (dy * dy))
    pitch = math.degrees(math.atan2(dz, horizontal))
    return review_rotator(pitch, yaw)


def safe_set(obj, props, value):
    if isinstance(props, str):
        props = (props,)
    for prop in props:
        try:
            obj.set_editor_property(prop, value)
            return prop
        except Exception:
            pass
    unreal.log_warning("Could not set {}.{}.".format(type(obj).__name__, "/".join(props)))
    return None


def ensure_directory(path):
    if not unreal.EditorAssetLibrary.does_directory_exist(path):
        unreal.EditorAssetLibrary.make_directory(path)


def all_level_actors():
    actor_subsystem = unreal.get_editor_subsystem(unreal.EditorActorSubsystem)
    return list(actor_subsystem.get_all_level_actors())


def tag_actor(actor, *extra_tags):
    tags = list(actor.get_editor_property("tags"))
    for tag in (REVIEW_TAG,) + extra_tags:
        tag_name = unreal.Name(tag)
        if tag_name not in tags:
            tags.append(tag_name)
    actor.set_editor_property("tags", tags)
    return actor


def set_actor_transform(actor, location, rotation=None, scale=None):
    rotation = rotation or review_rotator(0.0, 0.0)
    scale = scale or unreal.Vector(1.0, 1.0, 1.0)
    try:
        actor.set_actor_location(location, False, True)
    except Exception:
        actor.set_actor_location(location, False, False)
    try:
        actor.set_actor_rotation(rotation, False)
    except Exception:
        pass
    actor.set_actor_scale3d(scale)


def set_movable(component):
    if component is None:
        return
    try:
        component.set_mobility(unreal.ComponentMobility.MOVABLE)
        return
    except Exception:
        pass
    safe_set(component, "mobility", unreal.ComponentMobility.MOVABLE)


def color_material(name, color, roughness=0.88, metallic=0.0, emissive=None, unlit=False, two_sided=False):
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

    if unlit:
        shading_model = getattr(unreal.MaterialShadingModel, "MSM_UNLIT", None)
        if shading_model is not None:
            safe_set(material, "shading_model", shading_model)
        emissive = emissive or color
    if two_sided:
        safe_set(material, ("two_sided", "TwoSided"), True)

    mat_lib = unreal.MaterialEditingLibrary
    base = mat_lib.create_material_expression(material, unreal.MaterialExpressionConstant3Vector, -420, -80)
    base.set_editor_property("constant", color)
    mat_lib.connect_material_property(base, "", unreal.MaterialProperty.MP_BASE_COLOR)

    rough = mat_lib.create_material_expression(material, unreal.MaterialExpressionConstant, -420, 100)
    rough.set_editor_property("r", roughness)
    mat_lib.connect_material_property(rough, "", unreal.MaterialProperty.MP_ROUGHNESS)

    metal = mat_lib.create_material_expression(material, unreal.MaterialExpressionConstant, -420, 240)
    metal.set_editor_property("r", metallic)
    mat_lib.connect_material_property(metal, "", unreal.MaterialProperty.MP_METALLIC)

    if emissive is not None:
        glow = mat_lib.create_material_expression(material, unreal.MaterialExpressionConstant3Vector, -420, 390)
        glow.set_editor_property("constant", emissive)
        mat_lib.connect_material_property(glow, "", unreal.MaterialProperty.MP_EMISSIVE_COLOR)

    mat_lib.recompile_material(material)
    unreal.EditorAssetLibrary.save_loaded_asset(material)
    return material


def load_or_create_level():
    ensure_directory("/Game/Aerathea/Maps")
    if unreal.EditorAssetLibrary.does_asset_exist(LEVEL_PATH):
        unreal.log("Loading review island level: {}".format(LEVEL_PATH))
        if not unreal.EditorLevelLibrary.load_level(LEVEL_PATH):
            raise RuntimeError("Failed to load review island level: {}".format(LEVEL_PATH))
    else:
        unreal.log("Creating review island level: {}".format(LEVEL_PATH))
        if not unreal.EditorLevelLibrary.new_level(LEVEL_PATH):
            raise RuntimeError("Failed to create review island level: {}".format(LEVEL_PATH))


def clear_review_actors():
    for actor in all_level_actors():
        label = actor.get_actor_label()
        tags = list(actor.get_editor_property("tags"))
        if unreal.Name(REVIEW_TAG) in tags or label.startswith("AET_REVIEW_"):
            unreal.EditorLevelLibrary.destroy_actor(actor)


def load_basic_mesh(path):
    mesh = unreal.load_asset(path)
    if mesh is None:
        raise RuntimeError("Missing engine basic shape {}".format(path))
    return mesh


def configure_static_mesh_component(component, mesh, material=None, collision=True, cast_shadow=False):
    if component is None:
        raise RuntimeError("Missing StaticMeshComponent")
    component.set_static_mesh(mesh)
    if material is not None:
        component.set_material(0, material)
    component.set_mobility(unreal.ComponentMobility.STATIC)
    component.set_cast_shadow(cast_shadow)
    if collision:
        component.set_collision_enabled(unreal.CollisionEnabled.QUERY_AND_PHYSICS)
        if hasattr(component, "set_collision_profile_name"):
            component.set_collision_profile_name("BlockAll")
    else:
        component.set_collision_enabled(unreal.CollisionEnabled.NO_COLLISION)


def spawn_mesh(label, mesh, location, scale, material, rotation=None, collision=True, cast_shadow=False, extra_tag=None):
    actor = unreal.EditorLevelLibrary.spawn_actor_from_class(
        unreal.StaticMeshActor,
        location,
        rotation or review_rotator(0.0, 0.0),
    )
    if actor is None:
        raise RuntimeError("Failed to spawn {}".format(label))
    actor.set_actor_label(label)
    set_actor_transform(actor, location, rotation or review_rotator(0.0, 0.0), scale)
    tag_actor(actor, *(tuple([extra_tag]) if extra_tag else tuple()))
    component = actor.get_component_by_class(unreal.StaticMeshComponent)
    configure_static_mesh_component(component, mesh, material, collision=collision, cast_shadow=cast_shadow)
    return actor


def spawn_text(label, text, location, size=52.0, yaw=-90.0):
    actor = unreal.EditorLevelLibrary.spawn_actor_from_class(
        unreal.TextRenderActor,
        location,
        review_rotator(0.0, yaw),
    )
    if actor is None:
        raise RuntimeError("Failed to spawn {}".format(label))
    actor.set_actor_label(label)
    tag_actor(actor)
    component = actor.get_component_by_class(unreal.TextRenderComponent)
    if component is not None:
        component.set_text(text)
        safe_set(component, "world_size", size)
        horizontal_alignment = getattr(unreal, "HorizontalTextAligment", None)
        vertical_alignment = getattr(unreal, "VerticalTextAligment", None)
        if horizontal_alignment is not None:
            safe_set(component, "horizontal_alignment", horizontal_alignment.EHTA_CENTER)
        if vertical_alignment is not None:
            safe_set(component, "vertical_alignment", vertical_alignment.EVRTA_TEXT_CENTER)
    return actor


def light_component(actor):
    for cls in (
        unreal.DirectionalLightComponent,
        unreal.SkyLightComponent,
        getattr(unreal, "RectLightComponent", None),
        unreal.PointLightComponent,
    ):
        if cls is None:
            continue
        component = actor.get_component_by_class(cls)
        if component is not None:
            return component
    return None


def spawn_light(label, cls, location, rotation, intensity=None):
    actor = unreal.EditorLevelLibrary.spawn_actor_from_class(cls, location, rotation)
    if actor is None:
        raise RuntimeError("Failed to spawn {}".format(label))
    actor.set_actor_label(label)
    tag_actor(actor, "AET_REVIEW_LIGHTING")
    component = light_component(actor)
    set_movable(component)
    if component is not None:
        if intensity is not None:
            safe_set(component, "intensity", intensity)
        safe_set(component, "cast_shadows", False)
        safe_set(component, "affects_world", True)
    return actor


def build_materials():
    return {
        "floor": color_material(
            "M_AET_ReviewIsland_Floor_Unlit_A01",
            unreal.LinearColor(0.31, 0.32, 0.31, 1.0),
            roughness=0.94,
            unlit=True,
        ),
        "grid": color_material(
            "M_AET_ReviewIsland_GridLine_Unlit_A01",
            unreal.LinearColor(0.55, 0.57, 0.56, 1.0),
            roughness=0.92,
            unlit=True,
        ),
        "pad": color_material(
            "M_AET_ReviewIsland_Pad_Unlit_A01",
            unreal.LinearColor(0.40, 0.41, 0.39, 1.0),
            roughness=0.9,
            unlit=True,
        ),
        "pad_edge": color_material(
            "M_AET_ReviewIsland_PadEdge_Unlit_A01",
            unreal.LinearColor(0.70, 0.74, 0.76, 1.0),
            roughness=0.75,
            metallic=0.25,
            unlit=True,
        ),
        "axis_x": color_material(
            "M_AET_ReviewIsland_AxisX_Unlit_A01",
            unreal.LinearColor(0.85, 0.16, 0.10, 1.0),
            roughness=0.82,
            unlit=True,
        ),
        "axis_y": color_material(
            "M_AET_ReviewIsland_AxisY_Unlit_A01",
            unreal.LinearColor(0.12, 0.68, 0.22, 1.0),
            roughness=0.82,
            unlit=True,
        ),
        "scale": color_material(
            "M_AET_ReviewIsland_ScaleMarker_Unlit_A01",
            unreal.LinearColor(0.95, 0.80, 0.32, 1.0),
            roughness=0.62,
            metallic=0.35,
            unlit=True,
        ),
        "sky": color_material(
            "M_AET_ReviewIsland_Sky_Unlit_A01",
            unreal.LinearColor(0.50, 0.65, 0.78, 1.0),
            roughness=1.0,
            unlit=True,
            two_sided=True,
        ),
    }


def build_sky_background(cube, sphere, materials):
    sky = spawn_mesh(
        "AET_REVIEW_SkyDome_Unlit_A01",
        sphere,
        unreal.Vector(0.0, 0.0, 2600.0),
        unreal.Vector(190.0, 190.0, 120.0),
        materials["sky"],
        collision=False,
        cast_shadow=False,
    )
    component = sky.get_component_by_class(unreal.StaticMeshComponent)
    if component is not None:
        component.set_collision_enabled(unreal.CollisionEnabled.NO_COLLISION)
        component.set_cast_shadow(False)
        safe_set(component, "visible_in_ray_tracing", False)

    backdrop_specs = [
        ("North", unreal.Vector(0.0, 6250.0, 3600.0), unreal.Vector(140.0, 0.16, 72.0)),
        ("South", unreal.Vector(0.0, -6250.0, 3600.0), unreal.Vector(140.0, 0.16, 72.0)),
        ("East", unreal.Vector(6250.0, 0.0, 3600.0), unreal.Vector(0.16, 140.0, 72.0)),
        ("West", unreal.Vector(-6250.0, 0.0, 3600.0), unreal.Vector(0.16, 140.0, 72.0)),
    ]
    for name, location, scale in backdrop_specs:
        wall = spawn_mesh(
            "AET_REVIEW_SkyBackdrop_{}_Unlit_A01".format(name),
            cube,
            location,
            scale,
            materials["sky"],
            collision=False,
            cast_shadow=False,
        )
        component = wall.get_component_by_class(unreal.StaticMeshComponent)
        if component is not None:
            component.set_collision_enabled(unreal.CollisionEnabled.NO_COLLISION)
            component.set_cast_shadow(False)

    return sky


def build_floor(cube, materials):
    spawn_mesh(
        "AET_REVIEW_Floor_120m_A01",
        cube,
        unreal.Vector(0.0, 0.0, -5.0),
        unreal.Vector(120.0, 120.0, 0.10),
        materials["floor"],
    )

    edge_specs = [
        ("North", unreal.Vector(0.0, 6000.0, 12.0), unreal.Vector(120.0, 0.12, 0.20)),
        ("South", unreal.Vector(0.0, -6000.0, 12.0), unreal.Vector(120.0, 0.12, 0.20)),
        ("East", unreal.Vector(6000.0, 0.0, 12.0), unreal.Vector(0.12, 120.0, 0.20)),
        ("West", unreal.Vector(-6000.0, 0.0, 12.0), unreal.Vector(0.12, 120.0, 0.20)),
    ]
    for name, location, scale in edge_specs:
        spawn_mesh(
            "AET_REVIEW_Perimeter_{}_A01".format(name),
            cube,
            location,
            scale,
            materials["pad_edge"],
            collision=False,
        )

    for index, offset in enumerate(range(-5000, 5001, 1000), start=1):
        spawn_mesh(
            "AET_REVIEW_Grid_X_{:02d}".format(index),
            cube,
            unreal.Vector(float(offset), 0.0, 2.0),
            unreal.Vector(0.025, 120.0, 0.015),
            materials["grid"],
            collision=False,
        )
        spawn_mesh(
            "AET_REVIEW_Grid_Y_{:02d}".format(index),
            cube,
            unreal.Vector(0.0, float(offset), 2.0),
            unreal.Vector(120.0, 0.025, 0.015),
            materials["grid"],
            collision=False,
        )

    spawn_mesh(
        "AET_REVIEW_Axis_X_Red_A01",
        cube,
        unreal.Vector(0.0, -150.0, 7.0),
        unreal.Vector(18.0, 0.06, 0.04),
        materials["axis_x"],
        collision=False,
    )
    spawn_mesh(
        "AET_REVIEW_Axis_Y_Green_A01",
        cube,
        unreal.Vector(-150.0, 0.0, 7.0),
        unreal.Vector(0.06, 18.0, 0.04),
        materials["axis_y"],
        collision=False,
    )


def build_pads(cube, materials):
    spawn_mesh(
        "AET_REVIEW_CentralPad_A01",
        cube,
        unreal.Vector(0.0, 0.0, 4.0),
        unreal.Vector(8.0, 8.0, 0.08),
        materials["pad"],
        extra_tag=SLOT_TAG,
    )
    spawn_text(
        "AET_REVIEW_Label_CentralPad_A01",
        "CURRENT ASSET REVIEW",
        unreal.Vector(0.0, -560.0, 35.0),
        size=44.0,
    )

    labels = [chr(ord("A") + i) for i in range(12)]
    positions = []
    start_x = -3600.0
    start_y = 2800.0
    spacing_x = 2400.0
    spacing_y = 1600.0
    for row in range(3):
        for col in range(4):
            positions.append(unreal.Vector(start_x + col * spacing_x, start_y - row * spacing_y, 4.0))

    for label, location in zip(labels, positions):
        spawn_mesh(
            "AET_REVIEW_Slot_{}_A01".format(label),
            cube,
            location,
            unreal.Vector(6.0, 6.0, 0.08),
            materials["pad"],
            extra_tag=SLOT_TAG,
        )
        spawn_text(
            "AET_REVIEW_Label_Slot_{}_A01".format(label),
            "SLOT {}".format(label),
            unreal.Vector(location.x, location.y - 430.0, 35.0),
            size=38.0,
        )


def build_scale_references(cube, cylinder, materials):
    scale_specs = [
        ("1m", 100.0, unreal.Vector(-5150.0, -4200.0, 50.0)),
        ("2m", 200.0, unreal.Vector(-5000.0, -4200.0, 100.0)),
        ("5m", 500.0, unreal.Vector(-4750.0, -4200.0, 250.0)),
        ("11m", 1100.0, unreal.Vector(-4300.0, -4200.0, 550.0)),
    ]
    for label, height_cm, location in scale_specs:
        spawn_mesh(
            "AET_REVIEW_Scale_{}_A01".format(label.replace("m", "M")),
            cylinder,
            location,
            unreal.Vector(0.18, 0.18, height_cm / 100.0),
            materials["scale"],
            collision=False,
        )
        spawn_text(
            "AET_REVIEW_Label_Scale_{}_A01".format(label.replace("m", "M")),
            label,
            unreal.Vector(location.x, location.y - 160.0, 24.0),
            size=32.0,
        )

    spawn_mesh(
        "AET_REVIEW_ScaleRail_10m_A01",
        cube,
        unreal.Vector(-4700.0, -4700.0, 12.0),
        unreal.Vector(10.0, 0.06, 0.06),
        materials["scale"],
        collision=False,
    )
    spawn_text(
        "AET_REVIEW_Label_ScaleRail_10m_A01",
        "10m SCALE RAIL",
        unreal.Vector(-4700.0, -4900.0, 30.0),
        size=32.0,
    )


def configure_lighting():
    key = spawn_light(
        "AET_REVIEW_KeyLight_Movable_A01",
        unreal.DirectionalLight,
        unreal.Vector(0.0, 0.0, 7000.0),
        review_rotator(-55.0, -35.0),
        intensity=2.4,
    )
    key_component = key.get_component_by_class(unreal.DirectionalLightComponent)
    if key_component is not None:
        safe_set(key_component, ("forward_shading_priority", "ForwardShadingPriority"), 1)
        safe_set(key_component, ("atmosphere_sun_light", "b_atmosphere_sun_light"), True)
        safe_set(key_component, "atmosphere_sun_light_index", 0)

    sky_atmosphere_class = getattr(unreal, "SkyAtmosphere", None)
    if sky_atmosphere_class is not None:
        sky_atmosphere = unreal.EditorLevelLibrary.spawn_actor_from_class(
            sky_atmosphere_class,
            unreal.Vector(0.0, 0.0, 0.0),
            review_rotator(0.0, 0.0),
        )
        if sky_atmosphere is None:
            raise RuntimeError("Failed to spawn AET_REVIEW_SkyAtmosphere_A01")
        sky_atmosphere.set_actor_label("AET_REVIEW_SkyAtmosphere_A01")
        tag_actor(sky_atmosphere, "AET_REVIEW_LIGHTING")
    else:
        unreal.log_warning("SkyAtmosphere class is unavailable; SkyLight may report missing sky source")

    sky = spawn_light(
        "AET_REVIEW_SkyLight_Movable_A01",
        unreal.SkyLight,
        unreal.Vector(0.0, 0.0, 500.0),
        review_rotator(0.0, 0.0),
        intensity=1.8,
    )
    sky_component = sky.get_component_by_class(unreal.SkyLightComponent)
    if sky_component is not None:
        safe_set(sky_component, ("real_time_capture", "RealTimeCapture"), True)

    light_class = getattr(unreal, "RectLight", None) or unreal.PointLight
    fill_specs = [
        ("North", unreal.Vector(0.0, 3600.0, 2200.0), review_rotator(-80.0, -90.0), 2600.0),
        ("South", unreal.Vector(0.0, -3600.0, 2200.0), review_rotator(-80.0, 90.0), 2600.0),
        ("East", unreal.Vector(3600.0, 0.0, 2200.0), review_rotator(-80.0, 180.0), 2200.0),
        ("West", unreal.Vector(-3600.0, 0.0, 2200.0), review_rotator(-80.0, 0.0), 2200.0),
    ]
    for name, location, rotation, intensity in fill_specs:
        actor = spawn_light(
            "AET_REVIEW_FillLight_{}_Movable_A01".format(name),
            light_class,
            location,
            rotation,
            intensity=intensity,
        )
        component = light_component(actor)
        if component is not None:
            safe_set(component, "attenuation_radius", 9000.0)
            safe_set(component, "source_width", 6000.0)
            safe_set(component, "source_height", 6000.0)


def configure_post_process():
    pp_class = getattr(unreal, "PostProcessVolume", None)
    if pp_class is None:
        raise RuntimeError("PostProcessVolume class is unavailable")

    actor = unreal.EditorLevelLibrary.spawn_actor_from_class(
        pp_class,
        unreal.Vector(0.0, 0.0, 400.0),
        review_rotator(0.0, 0.0),
    )
    if actor is None:
        raise RuntimeError("Failed to spawn fixed exposure post-process volume")
    actor.set_actor_label("AET_REVIEW_PostProcess_FixedExposure_A01")
    tag_actor(actor, "AET_REVIEW_LIGHTING")
    safe_set(actor, ("unbound", "b_unbound", "infinite_extent_unbound"), True)
    safe_set(actor, "priority", 100.0)
    safe_set(actor, "blend_weight", 1.0)
    safe_set(actor, "enabled", True)

    settings = actor.get_editor_property("settings")
    if settings is not None:
        method = getattr(getattr(unreal, "AutoExposureMethod", object), "AEM_MANUAL", None)
        if method is not None:
            safe_set(settings, ("override_auto_exposure_method", "b_override_auto_exposure_method"), True)
            safe_set(settings, "auto_exposure_method", method)
        exposure_fields = {
            ("override_auto_exposure_min_brightness", "b_override_auto_exposure_min_brightness"): True,
            ("override_auto_exposure_max_brightness", "b_override_auto_exposure_max_brightness"): True,
            ("override_auto_exposure_bias", "b_override_auto_exposure_bias"): True,
            ("auto_exposure_min_brightness", "auto_exposure_min_ev100"): 1.0,
            ("auto_exposure_max_brightness", "auto_exposure_max_ev100"): 1.0,
            ("auto_exposure_bias", "auto_exposure_bias_backup"): 0.0,
        }
        for props, value in exposure_fields.items():
            safe_set(settings, props, value)
        safe_set(actor, "settings", settings)


def configure_world_settings():
    world = unreal.EditorLevelLibrary.get_editor_world()
    if world is None:
        return
    settings = world.get_world_settings()
    if settings is None:
        return
    safe_set(settings, "force_no_precomputed_lighting", True)
    safe_set(settings, "enable_world_bounds_checks", False)
    safe_set(settings, "kill_z", -100000.0)


def place_current_asset():
    mesh = unreal.load_asset(CURRENT_ASSET["mesh"])
    if mesh is None:
        unreal.log_warning("Current review asset mesh is missing; leaving central pad empty: {}".format(CURRENT_ASSET["mesh"]))
        return None

    actor = unreal.EditorLevelLibrary.spawn_actor_from_class(
        unreal.StaticMeshActor,
        CURRENT_ASSET["location"],
        review_rotator(0.0, CURRENT_ASSET["yaw"]),
    )
    if actor is None:
        raise RuntimeError("Failed to spawn current review asset")
    actor.set_actor_label(CURRENT_ASSET["label"])
    tag_actor(actor, TARGET_TAG)
    set_actor_transform(
        actor,
        CURRENT_ASSET["location"],
        review_rotator(0.0, CURRENT_ASSET["yaw"]),
        unreal.Vector(1.0, 1.0, 1.0),
    )
    component = actor.get_component_by_class(unreal.StaticMeshComponent)
    configure_static_mesh_component(component, mesh, material=None, collision=True, cast_shadow=True)
    for index, material_path in enumerate(CURRENT_ASSET["materials"]):
        material = unreal.load_asset(material_path)
        if material is not None:
            component.set_material(index, material)
    spawn_text(
        "AET_REVIEW_Label_CurrentAsset_BloodAxeCairn_A01",
        "A01 BLOOD AXE CAIRN - PAINT-01",
        unreal.Vector(0.0, 540.0, 42.0),
        size=34.0,
        yaw=90.0,
    )
    return actor


def configure_camera_and_start():
    camera_location = unreal.Vector(-2500.0, -3600.0, 1850.0)
    camera_target = unreal.Vector(0.0, 0.0, 120.0)
    camera_rotation = look_at_rotation(camera_location, camera_target)

    camera = unreal.EditorLevelLibrary.spawn_actor_from_class(unreal.CameraActor, camera_location, camera_rotation)
    if camera is None:
        raise RuntimeError("Failed to spawn review camera")
    camera.set_actor_label("AET_REVIEW_Camera_Main_A01")
    tag_actor(camera, REVIEW_CAMERA_TAG)
    component = camera.get_component_by_class(unreal.CameraComponent)
    if component is not None:
        safe_set(component, "field_of_view", 52.0)
        safe_set(component, "auto_activate", True)
    safe_set(camera, "auto_activate_for_player", unreal.AutoReceiveInput.PLAYER0)

    player_start_class = getattr(unreal, "PlayerStart", None)
    if player_start_class is not None:
        player_start = unreal.EditorLevelLibrary.spawn_actor_from_class(player_start_class, camera_location, camera_rotation)
        if player_start is not None:
            player_start.set_actor_label("AET_REVIEW_PlayerStart_A01")
            tag_actor(player_start)

    director_class = getattr(unreal, "AETReviewCameraDirector", None)
    if director_class is not None:
        director = unreal.EditorLevelLibrary.spawn_actor_from_class(
            director_class,
            unreal.Vector(-2350.0, -3450.0, 1760.0),
            camera_rotation,
        )
        if director is not None:
            director.set_actor_label("AET_REVIEW_ReviewCameraDirector_A01")
            tag_actor(director)
            safe_set(director, ("review_camera_tag", "ReviewCameraTag"), unreal.Name(REVIEW_CAMERA_TAG))
            safe_set(director, ("capture_review_screenshot", "b_capture_review_screenshot", "bCaptureReviewScreenshot"), False)
    else:
        unreal.log_warning("AETReviewCameraDirector class unavailable; Play review will use default camera behavior")


def build_review_island():
    cube = load_basic_mesh("/Engine/BasicShapes/Cube.Cube")
    cylinder = load_basic_mesh("/Engine/BasicShapes/Cylinder.Cylinder")
    sphere = load_basic_mesh("/Engine/BasicShapes/Sphere.Sphere")
    materials = build_materials()

    clear_review_actors()
    configure_world_settings()
    build_sky_background(cube, sphere, materials)
    build_floor(cube, materials)
    build_pads(cube, materials)
    build_scale_references(cube, cylinder, materials)
    configure_lighting()
    configure_post_process()
    place_current_asset()
    configure_camera_and_start()


def main():
    load_or_create_level()
    build_review_island()
    if not unreal.EditorLevelLibrary.save_current_level():
        raise RuntimeError("Failed to save {}".format(LEVEL_PATH))
    unreal.EditorAssetLibrary.save_directory("/Game/Aerathea/Maps", only_if_is_dirty=True, recursive=False)
    unreal.EditorAssetLibrary.save_directory(MATERIAL_PATH, only_if_is_dirty=True, recursive=True)
    unreal.log("Aerathea review island created: {}".format(LEVEL_PATH))


if __name__ == "__main__":
    main()
