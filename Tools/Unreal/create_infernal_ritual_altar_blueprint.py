import unreal


LEVEL_PATH = "/Game/Aerathea/Maps/L_Aerathea_Startup"
BLUEPRINT_PATH = "/Game/Aerathea/Blueprints/Infernals"
BLUEPRINT_ASSET_PATH = "{}/BP_INF_RitualAltar_A01".format(BLUEPRINT_PATH)
ALTAR_ACTOR_LABEL = "AET_PROD_INF_WorthinessAltar_A01"
FLOOR_ACTOR_LABEL = "AET_PROD_INF_CullingTrialFloor_A01"
ALTAR_MESH_PATH = "/Game/Aerathea/Props/Infernals/BalgorothCult/SM_INF_WorthinessAltar_A01"
NEXT_SLICE_TAG = "AET_NEXT_SLICE"
INF_CULT_TAG = "AET_INFERNAL_CULT_REVIEW"


MATERIAL_TARGETS = {
    "BrandGlowInactiveMaterial": "/Game/Aerathea/Materials/Instances/MI_INF_BrandGlowStates_A01_Inactive",
    "BrandGlowSmolderMaterial": "/Game/Aerathea/Materials/Instances/MI_INF_BrandGlowStates_A01_Smolder",
    "BrandGlowTrialActiveMaterial": "/Game/Aerathea/Materials/Instances/MI_INF_BrandGlowStates_A01_TrialActive",
    "BrandGlowAcceptedMaterial": "/Game/Aerathea/Materials/Instances/MI_INF_BrandGlowStates_A01_Accepted",
    "BrandGlowRejectedMaterial": "/Game/Aerathea/Materials/Instances/MI_INF_BrandGlowStates_A01_Rejected",
    "BrandGlowJudgmentPulseMaterial": "/Game/Aerathea/Materials/Instances/MI_INF_BrandGlowStates_A01_SorcererFocus",
}


NIAGARA_TARGETS = {
    "InactiveNiagaraSystem": "/Game/Aerathea/VFX/Infernals/WorthinessJudgment/NS_INF_Worthiness_Inactive_A01",
    "SmolderNiagaraSystem": "/Game/Aerathea/VFX/Infernals/WorthinessJudgment/NS_INF_Worthiness_Smolder_A01",
    "TrialActiveNiagaraSystem": "/Game/Aerathea/VFX/Infernals/WorthinessJudgment/NS_INF_Worthiness_TrialActive_A01",
    "AcceptedNiagaraSystem": "/Game/Aerathea/VFX/Infernals/WorthinessJudgment/NS_INF_Worthiness_Accepted_A01",
    "RejectedNiagaraSystem": "/Game/Aerathea/VFX/Infernals/WorthinessJudgment/NS_INF_Worthiness_Rejected_A01",
    "JudgmentPulseNiagaraSystem": "/Game/Aerathea/VFX/Infernals/WorthinessJudgment/NS_INF_Worthiness_JudgmentPulse_A01",
}


def ensure_directory(path):
    if not unreal.EditorAssetLibrary.does_directory_exist(path):
        unreal.EditorAssetLibrary.make_directory(path)


def safe_set(obj, prop, value):
    try:
        obj.set_editor_property(prop, value)
    except Exception as exc:
        unreal.log_warning("Could not set {}.{}: {}".format(type(obj).__name__, prop, exc))


def parent_class_for(unreal_class_name, readable_name):
    parent_type = getattr(unreal, unreal_class_name, None)
    if parent_type is None:
        raise RuntimeError("Compiled {} class is not available to Unreal Python".format(readable_name))
    return parent_type.static_class() if hasattr(parent_type, "static_class") else parent_type


def ensure_blueprint(asset_path, unreal_class_name, readable_name):
    package_path, asset_name = asset_path.rsplit("/", 1)
    ensure_directory(package_path)
    parent_class = parent_class_for(unreal_class_name, readable_name)

    if unreal.EditorAssetLibrary.does_asset_exist(asset_path):
        blueprint = unreal.load_asset(asset_path)
        current_parent = unreal.BlueprintEditorLibrary.get_blueprint_parent_class(blueprint)
        current_parent_name = current_parent.get_name() if current_parent is not None else "None"
        parent_class_name = parent_class.get_name()
        if current_parent != parent_class and current_parent_name != parent_class_name:
            unreal.log_warning("Reparenting {} from {} to {}.".format(asset_path, current_parent_name, readable_name))
            unreal.BlueprintEditorLibrary.reparent_blueprint(blueprint, parent_class)
        else:
            unreal.log("{} already parented to {}.".format(asset_path, current_parent_name))
    else:
        factory = unreal.BlueprintFactory()
        factory.set_editor_property("parent_class", parent_class)
        blueprint = unreal.AssetToolsHelpers.get_asset_tools().create_asset(
            asset_name=asset_name,
            package_path=package_path,
            asset_class=unreal.Blueprint,
            factory=factory,
        )
        if blueprint is None:
            raise RuntimeError("Failed to create {}".format(asset_path))
        unreal.log("Created {} from {}.".format(asset_path, readable_name))

    try:
        unreal.BlueprintEditorLibrary.compile_blueprint(blueprint)
    except Exception as exc:
        unreal.log_warning("Could not compile {} immediately: {}".format(asset_path, exc))
    unreal.EditorAssetLibrary.save_asset(asset_path)
    return blueprint


def load_blueprint_class(asset_path):
    loader = getattr(unreal.EditorAssetLibrary, "load_blueprint_class", None)
    if callable(loader):
        loaded_class = loader(asset_path)
        if loaded_class is not None:
            return loaded_class
    asset_name = asset_path.rsplit("/", 1)[-1]
    return unreal.load_object(None, "{}.{}_C".format(asset_path, asset_name))


def all_level_actors():
    actor_subsystem = unreal.get_editor_subsystem(unreal.EditorActorSubsystem)
    return list(actor_subsystem.get_all_level_actors())


def find_actor_by_label(label):
    for actor in all_level_actors():
        if actor.get_actor_label() == label:
            return actor
    return None


def tag_actor(actor):
    tags = list(actor.get_editor_property("tags"))
    for tag_name in (NEXT_SLICE_TAG, INF_CULT_TAG):
        tag = unreal.Name(tag_name)
        if tag not in tags:
            tags.append(tag)
    actor.set_editor_property("tags", tags)
    return actor


def retire_actor(actor):
    old_label = actor.get_actor_label()
    if old_label.startswith("AET_RETIRED_"):
        return
    actor.set_actor_label("AET_RETIRED_{}".format(old_label))
    try:
        actor.set_actor_hidden_in_game(True)
        actor.set_is_temporarily_hidden_in_editor(True)
        actor.set_actor_location(unreal.Vector(0.0, 0.0, -100000.0), False, True)
        actor.set_actor_scale3d(unreal.Vector(0.01, 0.01, 0.01))
        for component in actor.get_components_by_class(unreal.PrimitiveComponent):
            component.set_visibility(False, True)
            component.set_hidden_in_game(True, True)
    except Exception:
        pass
    unreal.log("Retired startup actor without deleting it: {}".format(old_label))


def floor_altar_snap_location():
    floor = find_actor_by_label(FLOOR_ACTOR_LABEL)
    if floor is None:
        return unreal.Vector(0.0, -75.0, 4.0)
    component = floor.get_component_by_class(unreal.StaticMeshComponent)
    if component is None:
        return unreal.Vector(0.0, -75.0, 4.0)
    socket_name = unreal.Name("snap_altar")
    try:
        if component.does_socket_exist(socket_name):
            return component.get_socket_location(socket_name)
    except Exception:
        pass
    return unreal.Vector(0.0, -75.0, 4.0)


def activate_actor_for_review(actor):
    actor.set_actor_hidden_in_game(False)
    actor.set_is_temporarily_hidden_in_editor(False)
    for component in actor.get_components_by_class(unreal.PrimitiveComponent):
        component_name = component.get_name()
        component_class = component.get_class().get_name()
        component.set_visibility(True, True)
        component.set_hidden_in_game(False, True)
        if component_class in {"BoxComponent", "CapsuleComponent", "SphereComponent"}:
            component.set_visibility(False, True)
            component.set_hidden_in_game(True, True)
        if component_name == "WorthinessNiagara":
            try:
                if component.get_asset() is None:
                    component.set_visibility(False, True)
                    component.set_hidden_in_game(True, True)
            except Exception:
                pass
    return actor


def spawn_blueprint_actor(label, asset_path, location):
    bp_class = load_blueprint_class(asset_path)
    if bp_class is None:
        raise RuntimeError("Could not load Blueprint class {}".format(asset_path))

    actor = find_actor_by_label(label)
    class_name = actor.get_class().get_name() if actor is not None else ""
    expected_fragment = asset_path.rsplit("/", 1)[-1]
    if actor is None or expected_fragment not in class_name:
        if actor is not None:
            retire_actor(actor)
        actor = unreal.EditorLevelLibrary.spawn_actor_from_class(
            bp_class,
            location,
            unreal.Rotator(0.0, 0.0, 0.0),
        )
    if actor is None:
        raise RuntimeError("Failed to spawn {}".format(label))

    actor.set_actor_label(label)
    actor.set_actor_location(location, False, True)
    actor.set_actor_rotation(unreal.Rotator(0.0, 0.0, 0.0), False)
    actor.set_actor_scale3d(unreal.Vector(1.0, 1.0, 1.0))
    tag_actor(actor)
    activate_actor_for_review(actor)
    return actor


def configure_ritual_altar_actor(actor):
    safe_set(actor, "AltarStaticMesh", unreal.load_asset(ALTAR_MESH_PATH))
    safe_set(actor, "BrandGlowMaterialSlotIndex", 4)
    safe_set(actor, "TrialProgress", 0.0)
    safe_set(actor, "JudgmentIntensity", 0.28)
    safe_set(actor, "RejectedSeverity", 0.0)
    safe_set(actor, "TrialDurationSeconds", 8.0)
    safe_set(actor, "JudgmentPulseSeconds", 1.25)
    safe_set(actor, "CooldownSeconds", 2.5)
    safe_set(actor, "InteractionRadiusCm", 170.0)
    safe_set(actor, "InteractionDepthCm", 90.0)
    safe_set(actor, "bUseNiagara", True)
    safe_set(actor, "bShowInteractionVolume", False)
    safe_set(actor, "bBindingHooksEnabled", True)
    safe_set(actor, "RitualBindingId", unreal.Name("Ritual_INF_CullingTrial_A01"))
    safe_set(actor, "ObjectiveBindingId", unreal.Name("OBJ_INF_ProveWorth_A01"))
    safe_set(actor, "UIStatePrefix", unreal.Name("UI.INF.RitualAltar"))
    safe_set(actor, "AudioEventPrefix", unreal.Name("Audio.INF.RitualAltar"))

    for prop_name, asset_path in MATERIAL_TARGETS.items():
        safe_set(actor, prop_name, unreal.load_asset(asset_path))
    for prop_name, asset_path in NIAGARA_TARGETS.items():
        safe_set(actor, prop_name, unreal.load_asset(asset_path))

    rerun = getattr(actor, "rerun_construction_scripts", None)
    if callable(rerun):
        rerun()
    activate_actor_for_review(actor)


def main():
    ensure_blueprint(BLUEPRINT_ASSET_PATH, "AETInfernalRitualAltarActor", "AAETInfernalRitualAltarActor")

    if not unreal.EditorLevelLibrary.load_level(LEVEL_PATH):
        raise RuntimeError("Failed to load level: {}".format(LEVEL_PATH))

    actor = spawn_blueprint_actor(
        ALTAR_ACTOR_LABEL,
        BLUEPRINT_ASSET_PATH,
        floor_altar_snap_location(),
    )
    configure_ritual_altar_actor(actor)

    if not unreal.EditorLevelLibrary.save_current_level():
        raise RuntimeError("Failed to save current level")

    for directory in {BLUEPRINT_PATH, "/Game/Aerathea/Maps"}:
        unreal.EditorAssetLibrary.save_directory(directory, only_if_is_dirty=True, recursive=True)

    unreal.log("Aerathea Infernal ritual altar Blueprint wiring complete.")


main()
