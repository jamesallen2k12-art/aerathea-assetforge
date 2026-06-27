import unreal


GNOME_OGRE_VFX_PATH = "/Game/Aerathea/VFX/GnomeOgre"
OGRE_VFX_PATH = "/Game/Aerathea/VFX/Ogres"
CREATURE_VFX_PATH = "/Game/Aerathea/VFX/Creatures"

NIAGARA_TARGETS = [
    ("{}/NE_GNM_ShieldEdgeBands_A01".format(GNOME_OGRE_VFX_PATH), "/Niagara/DefaultAssets/Templates/Emitters/StaticBeam"),
    ("{}/NE_GNM_ShieldSurfacePulse_A01".format(GNOME_OGRE_VFX_PATH), "/Niagara/DefaultAssets/Templates/Emitters/SingleLoopingParticle"),
    ("{}/NE_GNM_ShieldImpactRipple_A01".format(GNOME_OGRE_VFX_PATH), "/Niagara/DefaultAssets/Templates/Emitters/SimpleSpriteBurst"),
    ("{}/NE_GNM_ShieldOverloadSparks_A01".format(GNOME_OGRE_VFX_PATH), "/Niagara/DefaultAssets/Templates/Emitters/DirectionalBurst"),
    ("{}/NE_GNM_ShieldFailingFragments_A01".format(GNOME_OGRE_VFX_PATH), "/Niagara/DefaultAssets/Templates/Emitters/ConfettiBurst"),
    ("{}/NE_GNM_ShieldShutdownCollapse_A01".format(GNOME_OGRE_VFX_PATH), "/Niagara/DefaultAssets/Templates/Emitters/SimpleSpriteBurst"),
    ("{}/NE_OGR_CrudeTekPylon_Overload_A01".format(OGRE_VFX_PATH), "/Niagara/DefaultAssets/Templates/Emitters/SimpleSpriteBurst"),
    ("{}/NE_CRE_Manticore_Impact_A01".format(CREATURE_VFX_PATH), "/Niagara/DefaultAssets/Templates/Emitters/DirectionalBurst"),
]


def ensure_directory(path):
    if not unreal.EditorAssetLibrary.does_directory_exist(path):
        unreal.EditorAssetLibrary.make_directory(path)


def duplicate_template_asset(target_asset_path, template_asset_path):
    package_path, asset_name = target_asset_path.rsplit("/", 1)
    ensure_directory(package_path)

    if unreal.EditorAssetLibrary.does_asset_exist(target_asset_path):
        return unreal.load_asset(target_asset_path)

    template_asset = unreal.load_asset(template_asset_path)
    if template_asset is None:
        raise RuntimeError("Niagara template {} is not available; could not create {}.".format(template_asset_path, target_asset_path))

    duplicated = unreal.EditorAssetLibrary.duplicate_asset(template_asset_path, target_asset_path)
    if duplicated is None:
        duplicated = unreal.AssetToolsHelpers.get_asset_tools().duplicate_asset(
            asset_name=asset_name,
            package_path=package_path,
            original_object=template_asset,
        )
    if duplicated is None:
        raise RuntimeError("Could not duplicate Niagara template {} to {}.".format(template_asset_path, target_asset_path))

    unreal.EditorAssetLibrary.save_loaded_asset(duplicated)
    unreal.log("Created template-derived Niagara asset {} from {}.".format(target_asset_path, template_asset_path))
    return duplicated


def main():
    for target_path, template_path in NIAGARA_TARGETS:
        asset = duplicate_template_asset(target_path, template_path)
        if asset is None or not unreal.EditorAssetLibrary.does_asset_exist(target_path):
            raise RuntimeError("Missing Niagara polish target after ensure: {}".format(target_path))

    for directory in {GNOME_OGRE_VFX_PATH, OGRE_VFX_PATH, CREATURE_VFX_PATH}:
        unreal.EditorAssetLibrary.save_directory(directory, only_if_is_dirty=True, recursive=True)

    unreal.log("Gnome/Ogre VFX polish target ensure complete: {} Niagara assets checked.".format(len(NIAGARA_TARGETS)))


if __name__ == "__main__":
    main()
