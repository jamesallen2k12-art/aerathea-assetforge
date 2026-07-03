import unreal


LEVEL_PATH = "/Game/Aerathea/Maps/L_Aerathea_ReviewIsland"
REVIEW_TAG = unreal.Name("AET_REVIEW_ISLAND")
SLOT_TAG = unreal.Name("AET_REVIEW_SLOT")
TARGET_TAG = unreal.Name("AET_REVIEW_TARGET")
REVIEW_CAMERA_TAG = unreal.Name("AET_REVIEW_CAMERA")

EXPECTED_LABELS = [
    "AET_REVIEW_SkyDome_Unlit_A01",
    "AET_REVIEW_SkyBackdrop_North_Unlit_A01",
    "AET_REVIEW_SkyBackdrop_South_Unlit_A01",
    "AET_REVIEW_SkyBackdrop_East_Unlit_A01",
    "AET_REVIEW_SkyBackdrop_West_Unlit_A01",
    "AET_REVIEW_Floor_120m_A01",
    "AET_REVIEW_CentralPad_A01",
    "AET_REVIEW_KeyLight_Movable_A01",
    "AET_REVIEW_SkyAtmosphere_A01",
    "AET_REVIEW_SkyLight_Movable_A01",
    "AET_REVIEW_FillLight_North_Movable_A01",
    "AET_REVIEW_FillLight_South_Movable_A01",
    "AET_REVIEW_FillLight_East_Movable_A01",
    "AET_REVIEW_FillLight_West_Movable_A01",
    "AET_REVIEW_PostProcess_FixedExposure_A01",
    "AET_REVIEW_Camera_Main_A01",
    "AET_REVIEW_ReviewCameraDirector_A01",
    "AET_REVIEW_PlayerStart_A01",
    "AET_REVIEW_CurrentAsset_BloodAxeCairn_A01",
]
EXPECTED_SLOT_LABELS = ["AET_REVIEW_Slot_{}_A01".format(chr(ord("A") + i)) for i in range(12)]
CURRENT_MESH_PATH = "/Game/Aerathea/Props/Giants/BloodAxe/Cairns/SM_GIA_BloodAxeCairnSlabCluster_A01_Test2Manual"
CURRENT_MATERIAL_PATHS = [
    "/Game/Aerathea/Materials/Instances/MI_GIA_BloodAxeCairnSlabCluster_A01_Test2Manual_Projection",
    "/Game/Aerathea/Materials/Instances/MI_GIA_BloodAxeCairnSlabCluster_A01_Test2Manual_SideStone",
]
EXPECTED_UNLIT_REVIEW_MATERIALS = {
    "AET_REVIEW_Floor_120m_A01": "/Game/Aerathea/Materials/Review/M_AET_ReviewIsland_Floor_Unlit_A01",
    "AET_REVIEW_SkyDome_Unlit_A01": "/Game/Aerathea/Materials/Review/M_AET_ReviewIsland_Sky_Unlit_A01",
    "AET_REVIEW_SkyBackdrop_North_Unlit_A01": "/Game/Aerathea/Materials/Review/M_AET_ReviewIsland_Sky_Unlit_A01",
    "AET_REVIEW_SkyBackdrop_South_Unlit_A01": "/Game/Aerathea/Materials/Review/M_AET_ReviewIsland_Sky_Unlit_A01",
    "AET_REVIEW_SkyBackdrop_East_Unlit_A01": "/Game/Aerathea/Materials/Review/M_AET_ReviewIsland_Sky_Unlit_A01",
    "AET_REVIEW_SkyBackdrop_West_Unlit_A01": "/Game/Aerathea/Materials/Review/M_AET_ReviewIsland_Sky_Unlit_A01",
    "AET_REVIEW_CentralPad_A01": "/Game/Aerathea/Materials/Review/M_AET_ReviewIsland_Pad_Unlit_A01",
    "AET_REVIEW_Slot_A_A01": "/Game/Aerathea/Materials/Review/M_AET_ReviewIsland_Pad_Unlit_A01",
}


def all_level_actors():
    actor_subsystem = unreal.get_editor_subsystem(unreal.EditorActorSubsystem)
    return list(actor_subsystem.get_all_level_actors())


def actor_label(actor):
    try:
        return actor.get_actor_label()
    except Exception:
        return ""


def actor_tags(actor):
    try:
        return list(actor.get_editor_property("tags"))
    except Exception:
        return []


def actor_map():
    return {actor_label(actor): actor for actor in all_level_actors()}


def component_for_light(actor):
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


def path_without_object(asset):
    return asset.get_path_name().split(".", 1)[0]


def safe_get(obj, props, default=None):
    if isinstance(props, str):
        props = (props,)
    for prop in props:
        try:
            return obj.get_editor_property(prop)
        except Exception:
            pass
    return default


def validate_labels(actors, failures):
    for label in EXPECTED_LABELS + EXPECTED_SLOT_LABELS:
        if label not in actors:
            failures.append("Missing review island actor: {}".format(label))


def validate_tags(actors, failures):
    for label, actor in actors.items():
        if not label.startswith("AET_REVIEW_"):
            continue
        tags = actor_tags(actor)
        if REVIEW_TAG not in tags:
            failures.append("{} is missing {} tag".format(label, REVIEW_TAG))

    target = actors.get("AET_REVIEW_CurrentAsset_BloodAxeCairn_A01")
    if target is not None and TARGET_TAG not in actor_tags(target):
        failures.append("Current asset actor is missing {} tag".format(TARGET_TAG))

    for label in EXPECTED_SLOT_LABELS + ["AET_REVIEW_CentralPad_A01"]:
        actor = actors.get(label)
        if actor is not None and SLOT_TAG not in actor_tags(actor):
            failures.append("{} is missing {} tag".format(label, SLOT_TAG))

    camera = actors.get("AET_REVIEW_Camera_Main_A01")
    if camera is not None and REVIEW_CAMERA_TAG not in actor_tags(camera):
        failures.append("Review camera is missing {} tag".format(REVIEW_CAMERA_TAG))

    director = actors.get("AET_REVIEW_ReviewCameraDirector_A01")
    if director is not None and "AETReviewCameraDirector" not in director.get_class().get_name():
        failures.append(
            "AET_REVIEW_ReviewCameraDirector_A01 class is {}, expected AETReviewCameraDirector".format(
                director.get_class().get_name()
            )
        )


def validate_floor_and_slots(actors, failures):
    sky = actors.get("AET_REVIEW_SkyDome_Unlit_A01")
    if sky is not None:
        scale = sky.get_actor_scale3d()
        if scale.x < 180.0 or scale.y < 180.0 or scale.z < 110.0:
            failures.append("Review sky dome is too small: scale {}".format(scale))

    for label in [
        "AET_REVIEW_SkyBackdrop_North_Unlit_A01",
        "AET_REVIEW_SkyBackdrop_South_Unlit_A01",
        "AET_REVIEW_SkyBackdrop_East_Unlit_A01",
        "AET_REVIEW_SkyBackdrop_West_Unlit_A01",
    ]:
        actor = actors.get(label)
        if actor is None:
            continue
        scale = actor.get_actor_scale3d()
        if max(scale.x, scale.y) < 130.0 or scale.z < 68.0:
            failures.append("{} is too small for a review backdrop: scale {}".format(label, scale))

    floor = actors.get("AET_REVIEW_Floor_120m_A01")
    if floor is not None:
        scale = floor.get_actor_scale3d()
        if scale.x < 119.0 or scale.y < 119.0:
            failures.append("Review floor is too small: scale {}".format(scale))

    for label in EXPECTED_SLOT_LABELS:
        actor = actors.get(label)
        if actor is None:
            continue
        scale = actor.get_actor_scale3d()
        if scale.x < 5.5 or scale.y < 5.5:
            failures.append("{} pad is too small: scale {}".format(label, scale))

    central = actors.get("AET_REVIEW_CentralPad_A01")
    if central is not None:
        scale = central.get_actor_scale3d()
        if scale.x < 7.5 or scale.y < 7.5:
            failures.append("Central review pad is too small: scale {}".format(scale))


def validate_visible_review_materials(actors, failures):
    unlit_model = getattr(unreal.MaterialShadingModel, "MSM_UNLIT", None)
    for label, expected_path in EXPECTED_UNLIT_REVIEW_MATERIALS.items():
        actor = actors.get(label)
        if actor is None:
            continue
        component = actor.get_component_by_class(unreal.StaticMeshComponent)
        if component is None:
            failures.append("{} has no StaticMeshComponent for material validation".format(label))
            continue
        material = component.get_material(0)
        if material is None:
            failures.append("{} has no visible review material".format(label))
            continue
        material_path = path_without_object(material)
        if material_path != expected_path:
            failures.append("{} material is {}, expected {}".format(label, material_path, expected_path))
        if unlit_model is not None:
            parent = material
            try:
                shading_model = parent.get_editor_property("shading_model")
                if shading_model != unlit_model:
                    failures.append("{} material {} is {}, expected unlit".format(label, material_path, shading_model))
            except Exception:
                pass
        if label == "AET_REVIEW_SkyDome_Unlit_A01" and safe_get(material, ("two_sided", "TwoSided"), False) is False:
            failures.append("{} material {} is not two-sided".format(label, material_path))


def validate_lighting(actors, failures):
    sky_atmosphere = actors.get("AET_REVIEW_SkyAtmosphere_A01")
    if sky_atmosphere is None:
        failures.append("Missing SkyAtmosphere; SkyLight needs a sky source for stable review lighting")
    elif sky_atmosphere.get_class().get_name() != "SkyAtmosphere":
        failures.append(
            "AET_REVIEW_SkyAtmosphere_A01 class is {}, expected SkyAtmosphere".format(
                sky_atmosphere.get_class().get_name()
            )
        )

    key = actors.get("AET_REVIEW_KeyLight_Movable_A01")
    if key is not None:
        key_component = key.get_component_by_class(unreal.DirectionalLightComponent)
        if key_component is not None:
            atmosphere_sun = safe_get(
                key_component,
                ("atmosphere_sun_light", "b_atmosphere_sun_light"),
                None,
            )
            if atmosphere_sun is False:
                failures.append("AET_REVIEW_KeyLight_Movable_A01 is not marked as atmosphere sun light")

    for label in [
        "AET_REVIEW_KeyLight_Movable_A01",
        "AET_REVIEW_SkyLight_Movable_A01",
        "AET_REVIEW_FillLight_North_Movable_A01",
        "AET_REVIEW_FillLight_South_Movable_A01",
        "AET_REVIEW_FillLight_East_Movable_A01",
        "AET_REVIEW_FillLight_West_Movable_A01",
    ]:
        actor = actors.get(label)
        if actor is None:
            continue
        component = component_for_light(actor)
        if component is None:
            failures.append("{} has no light component".format(label))
            continue
        mobility = safe_get(component, "mobility")
        if mobility == unreal.ComponentMobility.STATIC:
            failures.append("{} is static; review lights must be movable to avoid unbuilt lighting".format(label))
        intensity = safe_get(component, "intensity", 0.0)
        if intensity <= 0.0:
            failures.append("{} has non-positive intensity {}".format(label, intensity))


def validate_post_process(actors, failures):
    actor = actors.get("AET_REVIEW_PostProcess_FixedExposure_A01")
    if actor is None:
        return
    unbound = safe_get(actor, ("unbound", "b_unbound", "infinite_extent_unbound"), False)
    if not unbound:
        failures.append("Post process volume is not unbound; exposure may vary by position")
    priority = safe_get(actor, "priority", 0.0)
    if priority < 50.0:
        failures.append("Post process volume priority is too low: {}".format(priority))


def validate_current_asset(actors, failures):
    actor = actors.get("AET_REVIEW_CurrentAsset_BloodAxeCairn_A01")
    if actor is None:
        return
    component = actor.get_component_by_class(unreal.StaticMeshComponent)
    if component is None:
        failures.append("Current asset has no StaticMeshComponent")
        return
    mesh = component.get_editor_property("static_mesh")
    if mesh is None:
        failures.append("Current asset has no static mesh assigned")
    elif path_without_object(mesh) != CURRENT_MESH_PATH:
        failures.append("Current asset mesh is {}, expected {}".format(path_without_object(mesh), CURRENT_MESH_PATH))
    override_paths = set()
    for index in range(len(CURRENT_MATERIAL_PATHS)):
        material = component.get_material(index)
        if material is None:
            failures.append("Current asset material slot {} is empty".format(index))
            continue
        override_paths.add(path_without_object(material))
    for material_path in CURRENT_MATERIAL_PATHS:
        if material_path not in override_paths:
            failures.append("Current asset is missing material override {}".format(material_path))


def validate_world_settings(failures):
    world = unreal.EditorLevelLibrary.get_editor_world()
    if world is None:
        failures.append("No editor world loaded")
        return
    settings = world.get_world_settings()
    if settings is None:
        failures.append("No world settings available")
        return
    force_no_precomputed = safe_get(settings, "force_no_precomputed_lighting", None)
    if force_no_precomputed is False:
        failures.append("force_no_precomputed_lighting is false; review island should avoid baked-lighting drift")


def main():
    if not unreal.EditorAssetLibrary.does_asset_exist(LEVEL_PATH):
        raise RuntimeError("Review island map does not exist: {}".format(LEVEL_PATH))
    if not unreal.EditorLevelLibrary.load_level(LEVEL_PATH):
        raise RuntimeError("Failed to load review island map: {}".format(LEVEL_PATH))

    failures = []
    actors = actor_map()
    validate_labels(actors, failures)
    validate_tags(actors, failures)
    validate_floor_and_slots(actors, failures)
    validate_visible_review_materials(actors, failures)
    validate_lighting(actors, failures)
    validate_post_process(actors, failures)
    validate_current_asset(actors, failures)
    validate_world_settings(failures)

    if failures:
        raise RuntimeError("Review island validation failed:\n- " + "\n- ".join(failures))

    unreal.log(
        "Aerathea review island validation passed: {} tagged actors, {} asset slots, fixed-lighting review map {}.".format(
            sum(1 for actor in actors.values() if REVIEW_TAG in actor_tags(actor)),
            len(EXPECTED_SLOT_LABELS) + 1,
            LEVEL_PATH,
        )
    )


if __name__ == "__main__":
    main()
