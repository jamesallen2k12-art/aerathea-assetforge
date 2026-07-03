import unreal


LEVEL_PATH = "/Game/Aerathea/Maps/L_Aerathea_Startup"
MESH_PATH = "/Game/Aerathea/Props/Giants/BloodAxe/MovedCamp/SM_GIA_BloodAxeMovedCampLowCairnRemnant_A01"
MATERIAL_INSTANCE_PATH = "/Game/Aerathea/Materials/Instances/MI_GIA_BloodAxeMovedCampLowCairnRemnant_A01"

ACTOR_LABEL = "AET_PROD_GIA_BloodAxeMovedCampLowCairnRemnant_A01"
ACTOR_LOCATION = unreal.Vector(1280.0, 430.0, 0.0)
ACTOR_YAW = -18.0
REVIEW_TAGS = [
    "AET_FIRST_SLICE",
    "AET_BLOODAXE_MOVED_CAMP_REVIEW",
    "AET_STATIC_REVIEW_TARGET",
]


def review_rotator(pitch, yaw, roll=0.0):
    return unreal.Rotator(roll, pitch, yaw)


def safe_set(obj, prop, value):
    try:
        obj.set_editor_property(prop, value)
    except Exception as exc:
        unreal.log_warning("Could not set {}.{}: {}".format(type(obj).__name__, prop, exc))


def all_level_actors():
    actor_subsystem = unreal.get_editor_subsystem(unreal.EditorActorSubsystem)
    return list(actor_subsystem.get_all_level_actors())


def find_actor_by_label(label):
    for actor in all_level_actors():
        if actor.get_actor_label() == label:
            return actor
    return None


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
            component.set_collision_enabled(unreal.CollisionEnabled.NO_COLLISION)
    except Exception:
        pass
    unreal.log("Retired startup actor without deleting it: {}".format(old_label))


def tag_actor(actor):
    tags = list(actor.get_editor_property("tags"))
    for tag in REVIEW_TAGS:
        tag_name = unreal.Name(tag)
        if tag_name not in tags:
            tags.append(tag_name)
    actor.set_editor_property("tags", tags)
    return actor


def activate_actor_for_review(actor):
    try:
        actor.set_actor_hidden_in_game(False)
        actor.set_is_temporarily_hidden_in_editor(False)
    except Exception:
        pass
    try:
        for component in actor.get_components_by_class(unreal.PrimitiveComponent):
            component.set_visibility(True, True)
            component.set_hidden_in_game(False, True)
            component.set_collision_enabled(unreal.CollisionEnabled.NO_COLLISION)
            set_profile = getattr(component, "set_collision_profile_name", None)
            if callable(set_profile):
                set_profile("NoCollision")
    except Exception:
        pass
    return actor


def set_metadata(mesh):
    setter = getattr(unreal.EditorAssetLibrary, "set_metadata_tag", None)
    if not callable(setter):
        unreal.log_warning("EditorAssetLibrary.set_metadata_tag is unavailable; skipped placement metadata")
        return
    metadata = {
        "Aerathea.StaticMesh.StartupPlaced": "startup_review_actor",
        "Aerathea.StaticMesh.StartupActor": ACTOR_LABEL,
        "Aerathea.StaticMesh.VisualReview": "first_pass_approved_not_final_art",
        "Aerathea.StaticMesh.FinalArtAuthored": "false",
        "Aerathea.StaticMesh.CollisionPolicy": "disabled_no_correctness_claim",
        "Aerathea.StaticMesh.GameplayBehavior": "none_static_environmental_storytelling",
    }
    for tag, value in metadata.items():
        setter(mesh, tag, value)
    unreal.EditorAssetLibrary.save_loaded_asset(mesh)


def place_actor(mesh, material_instance):
    actor = find_actor_by_label(ACTOR_LABEL)
    if actor is None or actor.get_class().get_name() != "StaticMeshActor":
        if actor is not None:
            retire_actor(actor)
        actor = unreal.EditorLevelLibrary.spawn_actor_from_class(
            unreal.StaticMeshActor,
            ACTOR_LOCATION,
            review_rotator(0.0, ACTOR_YAW),
        )
    if actor is None:
        raise RuntimeError("Failed to spawn {}".format(ACTOR_LABEL))

    actor.set_actor_label(ACTOR_LABEL)
    actor.set_actor_location(ACTOR_LOCATION, False, True)
    actor.set_actor_rotation(review_rotator(0.0, ACTOR_YAW), False)
    actor.set_actor_scale3d(unreal.Vector(1.0, 1.0, 1.0))
    tag_actor(actor)
    activate_actor_for_review(actor)

    component = actor.get_component_by_class(unreal.StaticMeshComponent)
    if component is None:
        raise RuntimeError("Static mesh actor has no StaticMeshComponent: {}".format(ACTOR_LABEL))
    component.set_static_mesh(mesh)
    component.set_mobility(unreal.ComponentMobility.STATIC)
    component.set_collision_enabled(unreal.CollisionEnabled.NO_COLLISION)
    if material_instance is not None:
        component.set_material(0, material_instance)
    return actor


def main():
    mesh = unreal.load_asset(MESH_PATH)
    if mesh is None:
        raise RuntimeError("Missing Blood Axe low-cairn mesh: {}".format(MESH_PATH))
    material_instance = unreal.load_asset(MATERIAL_INSTANCE_PATH)
    if material_instance is None:
        raise RuntimeError("Missing Blood Axe low-cairn material instance: {}".format(MATERIAL_INSTANCE_PATH))

    if not unreal.EditorLevelLibrary.load_level(LEVEL_PATH):
        raise RuntimeError("Failed to load level: {}".format(LEVEL_PATH))

    place_actor(mesh, material_instance)
    set_metadata(mesh)

    if not unreal.EditorLevelLibrary.save_current_level():
        raise RuntimeError("Failed to save startup level after Blood Axe low-cairn placement")
    unreal.EditorAssetLibrary.save_directory("/Game/Aerathea/Maps", only_if_is_dirty=True, recursive=True)
    unreal.EditorAssetLibrary.save_directory("/Game/Aerathea/Props/Giants/BloodAxe/MovedCamp", only_if_is_dirty=True, recursive=True)
    unreal.log("Placed {} as a startup review actor at {} yaw {}.".format(ACTOR_LABEL, ACTOR_LOCATION, ACTOR_YAW))


main()
