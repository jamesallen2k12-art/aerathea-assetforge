import unreal


LEVEL_PATH = "/Game/Aerathea/Maps/L_Aerathea_Startup"
FIRST_SLICE_TAG = "AET_FIRST_SLICE"
GRYPHON_LABEL = "AET_PROD_CRE_Gryphon_A01"
GRYPHON_MESH_PATH = "/Game/Aerathea/Creatures/Gryphon/Base/SK_CRE_Gryphon_A01"
GRYPHON_LOCATION = unreal.Vector(520.0, 520.0, 0.0)
GRYPHON_ROTATION = unreal.Rotator(0.0, 0.0, 42.0)
GRYPHON_SCALE = unreal.Vector(1.35, 1.35, 1.35)


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
    first_slice_name = unreal.Name(FIRST_SLICE_TAG)
    if first_slice_name not in tags:
        tags.append(first_slice_name)
    actor.set_editor_property("tags", tags)


def set_actor_transform(actor):
    try:
        actor.set_actor_location(GRYPHON_LOCATION, False, True)
    except Exception:
        actor.set_actor_location(GRYPHON_LOCATION, False, False)
    try:
        actor.set_actor_rotation(GRYPHON_ROTATION, False)
    except Exception:
        pass
    actor.set_actor_scale3d(GRYPHON_SCALE)


def activate_actor_for_review(actor):
    try:
        actor.set_actor_hidden_in_game(False)
    except Exception:
        pass
    try:
        actor.set_is_temporarily_hidden_in_editor(False)
    except Exception:
        pass
    try:
        for component in actor.get_components_by_class(unreal.PrimitiveComponent):
            try:
                component.set_visibility(True, True)
            except Exception:
                pass
            try:
                component.set_hidden_in_game(False, True)
            except Exception:
                pass
    except Exception:
        pass


def set_skeletal_mesh(component, mesh):
    for prop_name in ("skeletal_mesh_asset", "skeletal_mesh"):
        try:
            component.set_editor_property(prop_name, mesh)
            return
        except Exception:
            continue
    raise RuntimeError("Could not assign skeletal mesh {}".format(mesh.get_name()))


def main():
    if not unreal.EditorLevelLibrary.load_level(LEVEL_PATH):
        raise RuntimeError("Failed to load level: {}".format(LEVEL_PATH))

    mesh = unreal.load_asset(GRYPHON_MESH_PATH)
    if mesh is None:
        raise RuntimeError("Missing gryphon skeletal mesh: {}".format(GRYPHON_MESH_PATH))

    actor = find_actor_by_label(GRYPHON_LABEL)
    if actor is None:
        actor = unreal.EditorLevelLibrary.spawn_actor_from_class(
            unreal.SkeletalMeshActor,
            GRYPHON_LOCATION,
            GRYPHON_ROTATION,
        )
        if actor is None:
            raise RuntimeError("Failed to spawn {}".format(GRYPHON_LABEL))
        actor.set_actor_label(GRYPHON_LABEL)

    set_actor_transform(actor)
    tag_actor(actor)
    activate_actor_for_review(actor)

    component = actor.get_component_by_class(unreal.SkeletalMeshComponent)
    if component is None:
        raise RuntimeError("{} has no SkeletalMeshComponent".format(GRYPHON_LABEL))
    set_skeletal_mesh(component, mesh)

    if not unreal.EditorLevelLibrary.save_current_level():
        raise RuntimeError("Failed to save gryphon review placement")

    unreal.log(
        "Ensured {} review actor at {} scale {}.".format(
            GRYPHON_LABEL,
            GRYPHON_LOCATION,
            GRYPHON_SCALE,
        )
    )


main()
