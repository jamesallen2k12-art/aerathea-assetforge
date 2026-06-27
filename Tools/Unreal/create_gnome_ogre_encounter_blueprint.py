import unreal


BLUEPRINT_PATH = "/Game/Aerathea/Blueprints/GnomeOgre"


def ensure_directory(path):
    if not unreal.EditorAssetLibrary.does_directory_exist(path):
        unreal.EditorAssetLibrary.make_directory(path)


def parent_class_for(unreal_class_name, readable_name):
    parent_type = getattr(unreal, unreal_class_name, None)
    if parent_type is None:
        raise RuntimeError("Compiled {} class is not available to Unreal Python".format(readable_name))
    return parent_type.static_class() if hasattr(parent_type, "static_class") else parent_type


def ensure_blueprint(asset_name, unreal_class_name, readable_name, package_path=BLUEPRINT_PATH):
    ensure_directory(package_path)
    asset_path = "{}/{}".format(package_path, asset_name)
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


def main():
    ensure_blueprint(
        "BP_GNM_OGR_BattlefieldEncounter_A01",
        "AETGnomeOgreBattlefieldEncounterActor",
        "AAETGnomeOgreBattlefieldEncounterActor",
    )
    ensure_blueprint(
        "BP_GNM_HeavyMekShieldwall_A01",
        "AETHeavyMekShieldwallActor",
        "AAETHeavyMekShieldwallActor",
    )
    unreal.log("Aerathea Gnome/Ogre encounter Blueprint creation complete.")


main()
