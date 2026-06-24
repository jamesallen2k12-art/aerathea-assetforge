import unreal


LEVEL_PATH = "/Game/Aerathea/Maps/L_Aerathea_Startup"


def main():
    if unreal.EditorAssetLibrary.does_asset_exist(LEVEL_PATH):
        unreal.log("Aerathea startup level already exists: {}".format(LEVEL_PATH))
        if not unreal.EditorLevelLibrary.load_level(LEVEL_PATH):
            raise RuntimeError("Failed to load existing startup level: {}".format(LEVEL_PATH))
    else:
        unreal.log("Creating Aerathea startup level: {}".format(LEVEL_PATH))
        if not unreal.EditorLevelLibrary.new_level(LEVEL_PATH):
            raise RuntimeError("Failed to create startup level: {}".format(LEVEL_PATH))

    if not unreal.EditorLevelLibrary.save_current_level():
        raise RuntimeError("Failed to save startup level: {}".format(LEVEL_PATH))

    unreal.EditorAssetLibrary.save_directory("/Game/Aerathea/Maps", only_if_is_dirty=False, recursive=True)
    unreal.log("Aerathea startup level is ready: {}".format(LEVEL_PATH))


main()
