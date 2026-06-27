import unreal


EXPECTED_NIAGARA_ASSETS = [
    "/Game/Aerathea/VFX/GnomeOgre/NS_GNM_AetherShieldWall_A01",
    "/Game/Aerathea/VFX/GnomeOgre/NE_GNM_ShieldEdgeBands_A01",
    "/Game/Aerathea/VFX/GnomeOgre/NE_GNM_ShieldSurfacePulse_A01",
    "/Game/Aerathea/VFX/GnomeOgre/NE_GNM_ShieldImpactRipple_A01",
    "/Game/Aerathea/VFX/GnomeOgre/NE_GNM_ShieldOverloadSparks_A01",
    "/Game/Aerathea/VFX/GnomeOgre/NE_GNM_ShieldFailingFragments_A01",
    "/Game/Aerathea/VFX/GnomeOgre/NE_GNM_ShieldShutdownCollapse_A01",
    "/Game/Aerathea/VFX/Ogres/NS_OGR_CrudeTekPylon_A01",
    "/Game/Aerathea/VFX/Ogres/NE_OGR_CrudeTekPylon_Overload_A01",
    "/Game/Aerathea/VFX/Creatures/NS_CRE_Manticore_Impact_A01",
    "/Game/Aerathea/VFX/Creatures/NE_CRE_Manticore_Impact_A01",
]


def asset_class_name(asset):
    return asset.get_class().get_name() if asset is not None and asset.get_class() is not None else "None"


def main():
    failures = []
    for asset_path in EXPECTED_NIAGARA_ASSETS:
        if not unreal.EditorAssetLibrary.does_asset_exist(asset_path):
            failures.append("missing {}".format(asset_path))
            continue
        asset = unreal.load_asset(asset_path)
        class_name = asset_class_name(asset)
        if "Niagara" not in class_name:
            failures.append("{} has class {}, expected Niagara asset".format(asset_path, class_name))

    if failures:
        raise RuntimeError("Gnome/Ogre VFX polish target validation failed: {}".format("; ".join(failures)))

    print("Gnome/Ogre VFX polish target validation passed: {} Niagara systems/emitters found.".format(len(EXPECTED_NIAGARA_ASSETS)))


if __name__ == "__main__":
    main()
