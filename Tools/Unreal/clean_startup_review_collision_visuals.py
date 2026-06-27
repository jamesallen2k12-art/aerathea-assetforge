import unreal


LEVEL_PATH = "/Game/Aerathea/Maps/L_Aerathea_Startup"
SHAPE_COMPONENT_CLASSES = {
    "BoxComponent",
    "CapsuleComponent",
    "SphereComponent",
}


def all_level_actors():
    actor_subsystem = unreal.get_editor_subsystem(unreal.EditorActorSubsystem)
    return list(actor_subsystem.get_all_level_actors())


def is_shape_component(component):
    return component.get_class().get_name() in SHAPE_COMPONENT_CLASSES


def main():
    if not unreal.EditorLevelLibrary.load_level(LEVEL_PATH):
        raise RuntimeError("Failed to load level: {}".format(LEVEL_PATH))

    hidden_count = 0
    for actor in all_level_actors():
        for component in actor.get_components_by_class(unreal.PrimitiveComponent):
            if not is_shape_component(component):
                continue
            component.set_visibility(False, True)
            component.set_hidden_in_game(True, True)
            hidden_count += 1

    if not unreal.EditorLevelLibrary.save_current_level():
        raise RuntimeError("Failed to save {}".format(LEVEL_PATH))
    unreal.log("Hid {} startup review shape/collision components.".format(hidden_count))


main()
