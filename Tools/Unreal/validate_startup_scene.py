import unreal


LEVEL_PATH = "/Game/Aerathea/Maps/L_Aerathea_Startup"
EXPECTED_ASSETS = [
    "/Game/Aerathea/Materials/M_AET_Stone_Handpainted_A01",
    "/Game/Aerathea/Materials/M_AET_Timber_Handpainted_A01",
    "/Game/Aerathea/Materials/M_AET_DarkIron_A01",
    "/Game/Aerathea/Materials/M_AET_Brass_A01",
    "/Game/Aerathea/Materials/M_AET_AetheriumGlow_Blue_A01",
    "/Game/Aerathea/Materials/M_AET_Straw_A01",
    "/Game/Aerathea/Materials/M_AET_Leather_Dark_A01",
    "/Game/Aerathea/Materials/M_AET_PackedEarth_A01",
    "/Game/Aerathea/Materials/M_AET_Moss_A01",
    "/Game/Aerathea/Props/Training/SM_AET_TargetDummy_A01",
    "/Game/Aerathea/Props/Portal/SM_AET_PortalArch_A01",
    "/Game/Aerathea/Props/Environment/SM_AET_ModularGroundTile_A01",
    "/Game/Aerathea/Props/Mekgineer/SM_MKG_WorkshopPropCrate_A01",
    "/Game/Aerathea/Blueprints/Props/BP_AET_Portal_A01",
    LEVEL_PATH,
]
EXPECTED_ACTOR_LABELS = [
    "AET_BOOT_PlayerScale_180cm",
    "AET_BOOT_GnomeScale_110cm",
    "AET_BOOT_MinotaurScale_270cm",
    "AET_PROD_GroundTile_A01_R3_C3",
    "AET_PROD_TargetDummy_A01",
    "AET_PROD_PortalArch_A01",
    "AET_PROD_PortalCore_Aetherium_A01",
    "AET_PROD_WorkshopCrate_A01",
    "AET_BOOT_KeyLight_Directional",
    "AET_BOOT_SkyLight",
    "AET_BOOT_Camera_Overview",
    "AET_BOOT_Label_StyleTarget",
]
RETIRED_BLOCKOUT_LABELS = [
    "AET_BOOT_GroundTile_20m_A01",
    "AET_BOOT_PortalArch_LeftColumn_A01",
    "AET_BOOT_PortalArch_RightColumn_A01",
    "AET_BOOT_PortalArch_Capstone_A01",
    "AET_BOOT_PortalCore_Aetherium_A01",
    "AET_BOOT_TargetDummy_Blockout_A01",
    "AET_BOOT_TargetDummy_Crossbar_A01",
]
EXPECTED_STATIC_MESHES = [
    "/Game/Aerathea/Props/Training/SM_AET_TargetDummy_A01",
    "/Game/Aerathea/Props/Portal/SM_AET_PortalArch_A01",
    "/Game/Aerathea/Props/Environment/SM_AET_ModularGroundTile_A01",
    "/Game/Aerathea/Props/Mekgineer/SM_MKG_WorkshopPropCrate_A01",
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

    retired_labels = [
        label
        for label in RETIRED_BLOCKOUT_LABELS
        if label in actor_labels
    ]
    if retired_labels:
        raise RuntimeError("Retired blockout actors still present: {}".format(", ".join(retired_labels)))

    ground_tiles = [
        label
        for label in actor_labels
        if label.startswith("AET_PROD_GroundTile_A01_")
    ]
    if len(ground_tiles) != 25:
        raise RuntimeError("Expected 25 production ground tiles, found {}".format(len(ground_tiles)))

    mesh_slot_failures = []
    for mesh_path in EXPECTED_STATIC_MESHES:
        mesh = unreal.load_asset(mesh_path)
        if mesh is None:
            mesh_slot_failures.append("{} failed to load".format(mesh_path))
            continue
        if len(mesh.get_editor_property("static_materials")) == 0:
            mesh_slot_failures.append("{} has no material slots".format(mesh_path))
    if mesh_slot_failures:
        raise RuntimeError("Static mesh validation failed: {}".format("; ".join(mesh_slot_failures)))

    unreal.log(
        "Aerathea startup validation complete: {} assets, {} expected actors, {} ground tiles.".format(
            len(EXPECTED_ASSETS),
            len(EXPECTED_ACTOR_LABELS),
            len(ground_tiles),
        )
    )


main()
