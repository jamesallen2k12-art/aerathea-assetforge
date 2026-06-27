import unreal


LEVEL_PATH = "/Game/Aerathea/Maps/L_Aerathea_Startup"
GNOME_OGRE_BLUEPRINT_PATH = "/Game/Aerathea/Blueprints/GnomeOgre"
OGRE_BLUEPRINT_PATH = "/Game/Aerathea/Blueprints/Ogres"
CREATURE_BLUEPRINT_PATH = "/Game/Aerathea/Blueprints/Creatures"
GNOME_OGRE_VFX_PATH = "/Game/Aerathea/VFX/GnomeOgre"
OGRE_VFX_PATH = "/Game/Aerathea/VFX/Ogres"
CREATURE_VFX_PATH = "/Game/Aerathea/VFX/Creatures"
NEXT_SLICE_TAG = "AET_NEXT_SLICE"
ENCOUNTER_TAG = "AET_GNOME_OGRE_ENCOUNTER_WIRED"


BLUEPRINT_SPECS = [
    (
        "{}/BP_GNM_OGR_BattlefieldEncounter_A01".format(GNOME_OGRE_BLUEPRINT_PATH),
        "AETGnomeOgreBattlefieldEncounterActor",
        "AAETGnomeOgreBattlefieldEncounterActor",
    ),
    (
        "{}/BP_OGR_CrudeTekPylon_A01".format(OGRE_BLUEPRINT_PATH),
        "AETCrudeTekPylonActor",
        "AAETCrudeTekPylonActor",
    ),
    (
        "{}/BP_CRE_ManticoreInterrupt_A01".format(CREATURE_BLUEPRINT_PATH),
        "AETManticoreInterruptActor",
        "AAETManticoreInterruptActor",
    ),
]

ACTOR_BLUEPRINT_PATHS = {
    "AET_PROD_GNM_OGR_BattlefieldEncounter_A01": "{}/BP_GNM_OGR_BattlefieldEncounter_A01".format(GNOME_OGRE_BLUEPRINT_PATH),
    "AET_PROD_OGR_CrudeTekPylon_A01": "{}/BP_OGR_CrudeTekPylon_A01".format(OGRE_BLUEPRINT_PATH),
    "AET_PROD_CRE_Manticore_Interrupt_A01": "{}/BP_CRE_ManticoreInterrupt_A01".format(CREATURE_BLUEPRINT_PATH),
}

NIAGARA_SYSTEM_TARGETS = {
    "shieldwall": {
        "asset_path": "{}/NS_GNM_AetherShieldWall_A01".format(GNOME_OGRE_VFX_PATH),
        "template_path": "/Niagara/DefaultAssets/Templates/Systems/AttributeReaderTrails",
    },
    "pylon": {
        "asset_path": "{}/NS_OGR_CrudeTekPylon_A01".format(OGRE_VFX_PATH),
        "template_path": "/Niagara/DefaultAssets/Templates/Systems/RadialBurst",
    },
    "manticore": {
        "asset_path": "{}/NS_CRE_Manticore_Impact_A01".format(CREATURE_VFX_PATH),
        "template_path": "/Niagara/DefaultAssets/Templates/Systems/DirectionalBurst",
    },
}

NIAGARA_EMITTER_TARGETS = [
    ("{}/NE_GNM_ShieldEdgeBands_A01".format(GNOME_OGRE_VFX_PATH), "/Niagara/DefaultAssets/Templates/Emitters/StaticBeam"),
    ("{}/NE_GNM_ShieldSurfacePulse_A01".format(GNOME_OGRE_VFX_PATH), "/Niagara/DefaultAssets/Templates/Emitters/SingleLoopingParticle"),
    ("{}/NE_GNM_ShieldImpactRipple_A01".format(GNOME_OGRE_VFX_PATH), "/Niagara/DefaultAssets/Templates/Emitters/SimpleSpriteBurst"),
    ("{}/NE_GNM_ShieldOverloadSparks_A01".format(GNOME_OGRE_VFX_PATH), "/Niagara/DefaultAssets/Templates/Emitters/DirectionalBurst"),
    ("{}/NE_GNM_ShieldFailingFragments_A01".format(GNOME_OGRE_VFX_PATH), "/Niagara/DefaultAssets/Templates/Emitters/ConfettiBurst"),
    ("{}/NE_OGR_CrudeTekPylon_Overload_A01".format(OGRE_VFX_PATH), "/Niagara/DefaultAssets/Templates/Emitters/SimpleSpriteBurst"),
    ("{}/NE_CRE_Manticore_Impact_A01".format(CREATURE_VFX_PATH), "/Niagara/DefaultAssets/Templates/Emitters/DirectionalBurst"),
]


def ensure_directory(path):
    if not unreal.EditorAssetLibrary.does_directory_exist(path):
        unreal.EditorAssetLibrary.make_directory(path)


def safe_set(obj, prop, value):
    try:
        obj.set_editor_property(prop, value)
    except Exception as exc:
        unreal.log_warning("Could not set {}.{}: {}".format(type(obj).__name__, prop, exc))


def niagara_component_has_asset(component):
    get_asset = getattr(component, "get_asset", None)
    if callable(get_asset):
        try:
            if get_asset() is not None:
                return True
        except Exception:
            pass
    for prop_name in ("asset", "Asset"):
        try:
            if component.get_editor_property(prop_name) is not None:
                return True
        except Exception:
            continue
    return False


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


def ensure_blueprints():
    for asset_path, unreal_class_name, readable_name in BLUEPRINT_SPECS:
        ensure_blueprint(asset_path, unreal_class_name, readable_name)


def duplicate_template_asset(target_asset_path, template_asset_path):
    package_path, asset_name = target_asset_path.rsplit("/", 1)
    ensure_directory(package_path)

    if unreal.EditorAssetLibrary.does_asset_exist(target_asset_path):
        return unreal.load_asset(target_asset_path)

    template_asset = unreal.load_asset(template_asset_path)
    if template_asset is None:
        unreal.log_warning("Niagara template {} is not available; could not create {}.".format(template_asset_path, target_asset_path))
        return None

    duplicated = unreal.EditorAssetLibrary.duplicate_asset(template_asset_path, target_asset_path)
    if duplicated is None:
        duplicated = unreal.AssetToolsHelpers.get_asset_tools().duplicate_asset(
            asset_name=asset_name,
            package_path=package_path,
            original_object=template_asset,
        )
    if duplicated is None:
        unreal.log_warning("Could not duplicate Niagara template {} to {}.".format(template_asset_path, target_asset_path))
        return None

    unreal.EditorAssetLibrary.save_loaded_asset(duplicated)
    unreal.log("Created template-derived Niagara asset {} from {}.".format(target_asset_path, template_asset_path))
    return duplicated


def ensure_niagara_targets():
    targets = {}
    for key, spec in NIAGARA_SYSTEM_TARGETS.items():
        targets[key] = duplicate_template_asset(spec["asset_path"], spec["template_path"])

    for target_path, template_path in NIAGARA_EMITTER_TARGETS:
        duplicate_template_asset(target_path, template_path)

    return targets


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
    for tag_name in (NEXT_SLICE_TAG, ENCOUNTER_TAG):
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


def set_actor_transform(actor, location, rotation=None, scale=None):
    rotation = rotation or unreal.Rotator(0.0, 0.0, 0.0)
    scale = scale or unreal.Vector(1.0, 1.0, 1.0)
    try:
        actor.set_actor_location(location, False, True)
    except Exception:
        actor.set_actor_location(location, False, False)
    actor.set_actor_rotation(rotation, False)
    actor.set_actor_scale3d(scale)


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
        if component_name in {"PylonNiagara", "ImpactNiagara", "ShieldNiagara"}:
            if not niagara_component_has_asset(component):
                component.set_visibility(False, True)
                component.set_hidden_in_game(True, True)
    return actor


def spawn_blueprint_actor(label, asset_path, location, rotation=None, scale=None):
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
            rotation or unreal.Rotator(0.0, 0.0, 0.0),
        )
    if actor is None:
        raise RuntimeError("Failed to spawn {}".format(label))

    actor.set_actor_label(label)
    set_actor_transform(actor, location, rotation, scale)
    tag_actor(actor)
    activate_actor_for_review(actor)
    rerun = getattr(actor, "rerun_construction_scripts", None)
    if callable(rerun):
        rerun()
    return actor


def configure_pylon_actor(actor, pylon_niagara):
    safe_set(actor, "PylonStaticMesh", unreal.load_asset("/Game/Aerathea/Props/Ogres/Teknomancy/SM_OGR_CrudeTekPylon_A01"))
    if pylon_niagara is not None:
        safe_set(actor, "PylonNiagaraSystem", pylon_niagara)
    safe_set(actor, "OverloadPercent", 0.35)
    safe_set(actor, "DamagePercent", 0.0)
    safe_set(actor, "bPoweredVisible", True)
    safe_set(actor, "bUseNiagara", True)
    rerun = getattr(actor, "rerun_construction_scripts", None)
    if callable(rerun):
        rerun()
    activate_actor_for_review(actor)


def configure_manticore_interrupt_actor(actor, impact_niagara):
    safe_set(actor, "ManticoreSkeletalMesh", unreal.load_asset("/Game/Aerathea/Creatures/Manticores/SK_CRE_Manticore_Interrupt_A01"))
    if impact_niagara is not None:
        safe_set(actor, "ImpactNiagaraSystem", impact_niagara)
    safe_set(actor, "bVisibleDuringSetup", True)
    safe_set(actor, "SequenceProgress", 0.0)
    safe_set(actor, "EntryOffset", unreal.Vector(-220.0, 160.0, 0.0))
    safe_set(actor, "ImpactOffset", unreal.Vector(0.0, 0.0, 0.0))
    safe_set(actor, "RetreatOffset", unreal.Vector(260.0, -130.0, 0.0))
    safe_set(actor, "bUseNiagara", True)
    rerun = getattr(actor, "rerun_construction_scripts", None)
    if callable(rerun):
        rerun()
    activate_actor_for_review(actor)


def configure_shieldwall_actor(actor, shieldwall_niagara):
    if shieldwall_niagara is not None:
        safe_set(actor, "ShieldNiagaraSystem", shieldwall_niagara)
    safe_set(actor, "bUseNiagaraShield", True)
    safe_set(actor, "ImpactIntensity", 0.18)
    safe_set(actor, "OverloadPercent", 0.0)
    safe_set(actor, "ImpactLocationNormalized", 0.0)
    rerun = getattr(actor, "rerun_construction_scripts", None)
    if callable(rerun):
        rerun()
    activate_actor_for_review(actor)


def configure_encounter_actor(actor, actors_by_label):
    references = {
        "ShieldwallActor": "AET_PROD_GNM_HeavyMekShieldwall_A01",
        "GnomeHeavyMekActor": "AET_PROD_GNM_HeavyMek_Rivalry_A01",
        "OgreTeknomancerActor": "AET_PROD_OgreTeknomancer_A01",
        "OgreWarriorActor": "AET_PROD_OgreWarrior_Rival_A01",
        "CairnGateActor": "AET_PROD_OGR_CairnBattleGate_A01",
        "PylonObjectiveActor": "AET_PROD_OGR_CrudeTekPylon_A01",
        "OgreShamanActor": "AET_PROD_OgreShaman_A01",
        "OgreNecromancerActor": "AET_PROD_OgreNecromancer_A01",
        "ManticoreInterruptActor": "AET_PROD_CRE_Manticore_Interrupt_A01",
    }
    for prop_name, label in references.items():
        target = actors_by_label.get(label)
        if target is None:
            raise RuntimeError("Missing actor {} for encounter property {}".format(label, prop_name))
        safe_set(actor, prop_name, target)

    safe_set(actor, "bUsePlacedActors", True)
    safe_set(actor, "bEnablePylonObjective", True)
    safe_set(actor, "bEnableCasterReinforcements", True)
    safe_set(actor, "bEnableManticoreInterrupt", True)
    safe_set(actor, "bAutoStart", True)
    safe_set(actor, "bLoopForReview", True)
    safe_set(actor, "bAutoAdvanceReviewPhases", True)
    safe_set(actor, "ReviewPhaseDurationSeconds", 3.5)
    safe_set(actor, "EncounterWidthCm", 3200.0)
    safe_set(actor, "EncounterDepthCm", 2600.0)
    safe_set(actor, "ShieldImpactLocationNormalized", 0.0)
    safe_set(actor, "PylonOverloadPercent", 0.45)

    rerun = getattr(actor, "rerun_construction_scripts", None)
    if callable(rerun):
        rerun()
    validate = getattr(actor, "validate_dependencies", None)
    if callable(validate) and not validate():
        report = actor.get_editor_property("LastValidationReport")
        raise RuntimeError("Encounter dependency validation failed: {}".format(report))
    tag_actor(actor)
    activate_actor_for_review(actor)


def main():
    ensure_blueprints()
    niagara_targets = ensure_niagara_targets()
    shieldwall_niagara = niagara_targets.get("shieldwall")
    pylon_niagara = niagara_targets.get("pylon")
    manticore_niagara = niagara_targets.get("manticore")

    if not unreal.EditorLevelLibrary.load_level(LEVEL_PATH):
        raise RuntimeError("Failed to load level: {}".format(LEVEL_PATH))

    pylon_actor = spawn_blueprint_actor(
        "AET_PROD_OGR_CrudeTekPylon_A01",
        ACTOR_BLUEPRINT_PATHS["AET_PROD_OGR_CrudeTekPylon_A01"],
        unreal.Vector(-1260.0, -450.0, 0.0),
        unreal.Rotator(0.0, -10.0, 0.0),
    )
    configure_pylon_actor(pylon_actor, pylon_niagara)

    manticore_interrupt_actor = spawn_blueprint_actor(
        "AET_PROD_CRE_Manticore_Interrupt_A01",
        ACTOR_BLUEPRINT_PATHS["AET_PROD_CRE_Manticore_Interrupt_A01"],
        unreal.Vector(-1230.0, 890.0, 0.0),
        unreal.Rotator(0.0, -18.0, 0.0),
    )
    configure_manticore_interrupt_actor(manticore_interrupt_actor, manticore_niagara)

    encounter_actor = spawn_blueprint_actor(
        "AET_PROD_GNM_OGR_BattlefieldEncounter_A01",
        ACTOR_BLUEPRINT_PATHS["AET_PROD_GNM_OGR_BattlefieldEncounter_A01"],
        unreal.Vector(-600.0, -120.0, 0.0),
        unreal.Rotator(0.0, 0.0, 0.0),
    )

    shieldwall_actor = find_actor_by_label("AET_PROD_GNM_HeavyMekShieldwall_A01")
    if shieldwall_actor is None:
        raise RuntimeError("Missing shieldwall actor for encounter wiring")
    configure_shieldwall_actor(shieldwall_actor, shieldwall_niagara)

    actors_by_label = {actor.get_actor_label(): actor for actor in all_level_actors()}
    configure_encounter_actor(encounter_actor, actors_by_label)

    if not unreal.EditorLevelLibrary.save_current_level():
        raise RuntimeError("Failed to save current level")

    for directory in {
        GNOME_OGRE_BLUEPRINT_PATH,
        OGRE_BLUEPRINT_PATH,
        CREATURE_BLUEPRINT_PATH,
        GNOME_OGRE_VFX_PATH,
        OGRE_VFX_PATH,
        CREATURE_VFX_PATH,
        "/Game/Aerathea/Maps",
    }:
        unreal.EditorAssetLibrary.save_directory(directory, only_if_is_dirty=True, recursive=True)

    unreal.log("Aerathea Gnome/Ogre encounter wiring complete.")


main()
