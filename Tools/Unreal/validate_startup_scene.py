import unreal


LEVEL_PATH = "/Game/Aerathea/Maps/L_Aerathea_Startup"
EXPECTED_ASSETS = [
    "/Game/Aerathea/Materials/M_AET_Stone_Handpainted_A01",
    "/Game/Aerathea/Materials/M_AET_Timber_Handpainted_A01",
    "/Game/Aerathea/Materials/M_AET_DarkIron_A01",
    "/Game/Aerathea/Materials/M_AET_Brass_A01",
    "/Game/Aerathea/Materials/M_AET_AetheriumGlow_Blue_A01",
    LEVEL_PATH,
]
EXPECTED_ACTOR_LABELS = [
    "AET_BOOT_GroundTile_20m_A01",
    "AET_BOOT_PlayerScale_180cm",
    "AET_BOOT_GnomeScale_110cm",
    "AET_BOOT_MinotaurScale_270cm",
    "AET_BOOT_PortalArch_LeftColumn_A01",
    "AET_BOOT_PortalArch_RightColumn_A01",
    "AET_BOOT_PortalArch_Capstone_A01",
    "AET_BOOT_PortalCore_Aetherium_A01",
    "AET_BOOT_TargetDummy_Blockout_A01",
    "AET_BOOT_TargetDummy_Crossbar_A01",
    "AET_BOOT_KeyLight_Directional",
    "AET_BOOT_SkyLight",
    "AET_BOOT_Camera_Overview",
    "AET_BOOT_Label_StyleTarget",
]


def main():
    missing_assets = [
        asset_path
        for asset_path in EXPECTED_ASSETS
        if not unreal.EditorAssetLibrary.does_asset_exist(asset_path)
    ]
    if missing_assets:
        raise RuntimeError("Missing expected assets: {}".format(", ".join(missing_assets)))

    if not unreal.EditorLevelLibrary.load_level(LEVEL_PATH):
        raise RuntimeError("Failed to load level: {}".format(LEVEL_PATH))

    actor_labels = {
        actor.get_actor_label()
        for actor in unreal.EditorLevelLibrary.get_all_level_actors()
    }
    missing_labels = [
        label
        for label in EXPECTED_ACTOR_LABELS
        if label not in actor_labels
    ]
    if missing_labels:
        raise RuntimeError("Missing startup actors: {}".format(", ".join(missing_labels)))

    unreal.log(
        "Aerathea startup validation complete: {} assets, {} expected actors.".format(
            len(EXPECTED_ASSETS),
            len(EXPECTED_ACTOR_LABELS),
        )
    )


main()
