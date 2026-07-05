import unreal


LEVEL_PATH = "/Game/Aerathea/Maps/L_Aerathea_Startup"
MESH_PATH = "/Game/Aerathea/Props/Giants/BloodAxe/Cairns/SM_GIA_BloodAxeCairnstone_A002"
SOURCE_MATERIAL = "/Game/Aerathea/Materials/Instances/MI_GIA_BloodAxeCairnstone_A002_SourceTemplate"
INFERRED_MATERIAL = "/Game/Aerathea/Materials/Instances/MI_GIA_BloodAxeCairnstone_A002_InferredHidden"

ACTOR_LABEL = "AET_PROD_GIA_BloodAxeCairnstone_A002"
ACTOR_LOCATION = unreal.Vector(12480.0, 10360.0, 0.0)
ACTOR_YAW = -18.0
REVIEW_TAGS = [
    "AET_FIRST_SLICE",
    "AET_BLOODAXE_CAIRNSTONE_A002_REVIEW",
    "AET_STATIC_REVIEW_TARGET",
]


def review_rotator(pitch, yaw, roll=0.0):
    return unreal.Rotator(roll, pitch, yaw)


def asset_path_without_object(asset):
    return asset.get_path_name().split(".", 1)[0]


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
    for tag in REVIEW_TAGS:
        tag_name = unreal.Name(tag)
        if tag_name not in tags:
            tags.append(tag_name)
    actor.set_editor_property("tags", tags)


def set_metadata(mesh):
    setter = getattr(unreal.EditorAssetLibrary, "set_metadata_tag", None)
    if not callable(setter):
        unreal.log_warning("EditorAssetLibrary.set_metadata_tag unavailable; skipped placement metadata")
        return
    metadata = {
        "Aerathea.StaticMesh.StartupPlaced": "startup_review_actor",
        "Aerathea.StaticMesh.StartupActor": ACTOR_LABEL,
        "Aerathea.StaticMesh.VisualReview": "startup_review_capture_pending",
        "Aerathea.StaticMesh.FinalVisualApproval": "pending_flamestrike_review",
        "Aerathea.StaticMesh.FullyGameReady": "false",
    }
    for tag, value in metadata.items():
        setter(mesh, tag, value)
    unreal.EditorAssetLibrary.save_loaded_asset(mesh)


def material_slots(mesh):
    try:
        return list(mesh.get_editor_property("static_materials"))
    except Exception:
        return []


def place_actor(mesh, materials):
    actor = find_actor_by_label(ACTOR_LABEL)
    if actor is None or actor.get_class().get_name() != "StaticMeshActor":
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
    actor.set_actor_hidden_in_game(False)
    tag_actor(actor)

    component = actor.get_component_by_class(unreal.StaticMeshComponent)
    if component is None:
        raise RuntimeError("Static mesh actor has no StaticMeshComponent: {}".format(ACTOR_LABEL))
    component.set_static_mesh(mesh)
    component.set_mobility(unreal.ComponentMobility.STATIC)
    component.set_collision_enabled(unreal.CollisionEnabled.QUERY_AND_PHYSICS)
    set_profile = getattr(component, "set_collision_profile_name", None)
    if callable(set_profile):
        component.set_collision_profile_name("BlockAll")
    component.set_visibility(True, True)
    component.set_hidden_in_game(False, True)

    for index, slot in enumerate(material_slots(mesh)):
        slot_name = str(slot.get_editor_property("material_slot_name")).lower()
        material = materials["inferred"] if ("inferred" in slot_name or "hidden" in slot_name) else materials["source"]
        component.set_material(index, material)
    return actor


def main():
    mesh = unreal.load_asset(MESH_PATH)
    if mesh is None:
        raise RuntimeError("Missing A002 mesh: {}".format(MESH_PATH))
    materials = {
        "source": unreal.load_asset(SOURCE_MATERIAL),
        "inferred": unreal.load_asset(INFERRED_MATERIAL),
    }
    for key, material in materials.items():
        if material is None:
            raise RuntimeError("Missing A002 {} material instance".format(key))

    if not unreal.EditorLevelLibrary.load_level(LEVEL_PATH):
        raise RuntimeError("Failed to load level: {}".format(LEVEL_PATH))

    place_actor(mesh, materials)
    set_metadata(mesh)

    if not unreal.EditorLevelLibrary.save_current_level():
        raise RuntimeError("Failed to save startup level after A002 placement")
    unreal.EditorAssetLibrary.save_directory("/Game/Aerathea/Maps", only_if_is_dirty=True, recursive=True)
    unreal.EditorAssetLibrary.save_directory("/Game/Aerathea/Props/Giants/BloodAxe/Cairns", only_if_is_dirty=True, recursive=True)
    unreal.log("Placed {} at {} yaw {}.".format(ACTOR_LABEL, ACTOR_LOCATION, ACTOR_YAW))


if __name__ == "__main__":
    main()
