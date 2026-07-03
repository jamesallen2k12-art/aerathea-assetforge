import unreal


LEVEL_PATH = "/Game/Aerathea/Maps/L_Aerathea_Startup"
MESH_PATH = "/Game/Aerathea/Props/Giants/BloodAxe/Cairns/SM_GIA_BloodAxeCairnSlabCluster_A01_BacksideRepair"

MATERIAL_INSTANCE_PATHS = [
    "/Game/Aerathea/Materials/Instances/MI_GIA_BloodAxeCairnSlabCluster_A01_BacksideRepair_Stone",
    "/Game/Aerathea/Materials/Instances/MI_GIA_BloodAxeCairnSlabCluster_A01_BacksideRepair_EarthAsh",
    "/Game/Aerathea/Materials/Instances/MI_GIA_BloodAxeCairnSlabCluster_A01_BacksideRepair_Rawhide",
    "/Game/Aerathea/Materials/Instances/MI_GIA_BloodAxeCairnSlabCluster_A01_BacksideRepair_BloodAxeRedPaint",
]

ACTOR_LABEL = "AET_PROD_GIA_BloodAxeCairnSlabCluster_A01_BacksideRepair"
ACTOR_LOCATION = unreal.Vector(12000.0, 10000.0, 0.0)
ACTOR_YAW = -18.0
RELATED_REVIEW_PREFIX = "AET_PROD_GIA_BloodAxeCairnSlabCluster_A01_"
REVIEW_TAGS = [
    "AET_FIRST_SLICE",
    "AET_BLOODAXE_CAIRN_BACKSIDE_REPAIR_REVIEW",
    "AET_STATIC_REVIEW_TARGET",
]
RETIRED_REVIEW_TAGS = {
    "AET_BLOODAXE_CAIRN_COMPLETE_REVIEW",
    "AET_BLOODAXE_CAIRN_TEST2_MANUAL_REVIEW",
    "AET_BLOODAXE_CAIRN_BACKSIDE_REPAIR_REVIEW",
    "AET_STATIC_REVIEW_TARGET",
}


def review_rotator(pitch, yaw, roll=0.0):
    return unreal.Rotator(roll, pitch, yaw)


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


def retire_related_review_actors():
    for actor in all_level_actors():
        label = actor.get_actor_label()
        if label == ACTOR_LABEL or not label.startswith(RELATED_REVIEW_PREFIX):
            continue

        tags = [tag for tag in actor.get_editor_property("tags") if str(tag) not in RETIRED_REVIEW_TAGS]
        actor.set_editor_property("tags", tags)
        actor.set_actor_hidden_in_game(True)

        component = actor.get_component_by_class(unreal.StaticMeshComponent)
        if component is not None:
            component.set_visibility(False, True)
            component.set_hidden_in_game(True, True)


def material_key_for_slot(slot_name, index):
    lower_name = str(slot_name).lower()
    if "earth" in lower_name or "ash" in lower_name or "mud" in lower_name or "ground" in lower_name:
        return 1
    if "rawhide" in lower_name or "binding" in lower_name or "lashing" in lower_name:
        return 2
    if "redpaint" in lower_name or "red_paint" in lower_name or "paint" in lower_name or "red" in lower_name:
        return 3
    return 0


def asset_path_without_object(asset):
    return asset.get_path_name().split(".", 1)[0]


def set_metadata(mesh):
    setter = getattr(unreal.EditorAssetLibrary, "set_metadata_tag", None)
    if not callable(setter):
        unreal.log_warning("EditorAssetLibrary.set_metadata_tag is unavailable; skipped placement metadata")
        return
    metadata = {
        "Aerathea.StaticMesh.StartupPlaced": "startup_review_actor",
        "Aerathea.StaticMesh.StartupActor": ACTOR_LABEL,
        "Aerathea.StaticMesh.Status": "unreal_import_candidate_pending_backside_repair_review",
        "Aerathea.StaticMesh.VisualReview": "startup_review_capture_ready",
        "Aerathea.StaticMesh.FinalVisualApproval": "pending_flamestrike_review",
        "Aerathea.StaticMesh.FinalArtAuthored": "true",
        "Aerathea.StaticMesh.CollisionPolicy": "broad_simple_static_prop_collision_updated_for_rear_depth",
        "Aerathea.StaticMesh.GameplayBehavior": "none_static_environmental_storytelling",
    }
    for tag, value in metadata.items():
        setter(mesh, tag, value)
    unreal.EditorAssetLibrary.save_loaded_asset(mesh)


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
    collision_profile = getattr(component, "set_collision_profile_name", None)
    if callable(collision_profile):
        component.set_collision_profile_name("BlockAll")
    component.set_visibility(True, True)
    component.set_hidden_in_game(False, True)

    slots = list(mesh.get_editor_property("static_materials"))
    for index, slot in enumerate(slots):
        slot_name = slot.get_editor_property("material_slot_name")
        material_index = material_key_for_slot(slot_name, index)
        component.set_material(index, materials[material_index])
    return actor


def main():
    mesh = unreal.load_asset(MESH_PATH)
    if mesh is None:
        raise RuntimeError("Missing Blood Axe BacksideRepair cairn mesh: {}".format(MESH_PATH))

    materials = []
    for path in MATERIAL_INSTANCE_PATHS:
        material = unreal.load_asset(path)
        if material is None:
            raise RuntimeError("Missing BacksideRepair cairn material instance: {}".format(path))
        materials.append(material)

    if not unreal.EditorLevelLibrary.load_level(LEVEL_PATH):
        raise RuntimeError("Failed to load level: {}".format(LEVEL_PATH))

    retire_related_review_actors()
    place_actor(mesh, materials)
    set_metadata(mesh)

    if not unreal.EditorLevelLibrary.save_current_level():
        raise RuntimeError("Failed to save startup level after Blood Axe BacksideRepair cairn placement")
    unreal.EditorAssetLibrary.save_directory("/Game/Aerathea/Maps", only_if_is_dirty=True, recursive=True)
    unreal.EditorAssetLibrary.save_directory("/Game/Aerathea/Props/Giants/BloodAxe/Cairns", only_if_is_dirty=True, recursive=True)
    unreal.log("Placed {} at {} yaw {}.".format(ACTOR_LABEL, ACTOR_LOCATION, ACTOR_YAW))


if __name__ == "__main__":
    main()
