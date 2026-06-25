import math

import unreal


LEVEL_PATH = "/Game/Aerathea/Maps/L_Aerathea_Startup"
REVIEW_CAMERA_TARGET = unreal.Vector(-70, 160, 110)
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
    "/Game/Aerathea/Weapons/Mekgineer/SM_MKG_AetherKnife_A01",
    "/Game/Aerathea/Props/Mekgineer/Armory/SM_MKG_AetherCoreUnit_A01",
    "/Game/Aerathea/Weapons/Mekgineer/SM_MKG_SparkPistol_A01",
    "/Game/Aerathea/Props/Mekgineer/Armory/SM_MKG_AetheriumGrenade_A01",
    "/Game/Aerathea/Blueprints/Props/BP_AET_Portal_A01",
    LEVEL_PATH,
]
EXPECTED_ACTOR_LABELS = [
    "AET_BOOT_PlayerScale_180cm",
    "AET_BOOT_GnomeScale_110cm",
    "AET_BOOT_MinotaurScale_270cm",
    "AET_PROD_GroundTile_A01_R3_C3",
    "AET_PROD_TargetDummy_A01",
    "AET_PROD_Portal_A01",
    "AET_PROD_WorkshopCrate_A01",
    "AET_PROD_MKG_AetherKnife_A01",
    "AET_PROD_MKG_AetherCoreUnit_A01",
    "AET_PROD_MKG_SparkPistol_A01",
    "AET_PROD_MKG_AetheriumGrenade_A01",
    "AET_PROD_PlayerStart_Review_A01",
    "AET_PROD_Camera_Review_A01",
    "AET_PROD_ReviewCameraDirector_A01",
    "AET_PROD_ReviewFillLight_A01",
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
    "AET_PROD_PortalArch_A01",
    "AET_PROD_PortalCore_Aetherium_A01",
]
EXPECTED_STATIC_MESHES = [
    "/Game/Aerathea/Props/Training/SM_AET_TargetDummy_A01",
    "/Game/Aerathea/Props/Portal/SM_AET_PortalArch_A01",
    "/Game/Aerathea/Props/Environment/SM_AET_ModularGroundTile_A01",
    "/Game/Aerathea/Props/Mekgineer/SM_MKG_WorkshopPropCrate_A01",
    "/Game/Aerathea/Weapons/Mekgineer/SM_MKG_AetherKnife_A01",
    "/Game/Aerathea/Props/Mekgineer/Armory/SM_MKG_AetherCoreUnit_A01",
    "/Game/Aerathea/Weapons/Mekgineer/SM_MKG_SparkPistol_A01",
    "/Game/Aerathea/Props/Mekgineer/Armory/SM_MKG_AetheriumGrenade_A01",
]
EXPECTED_RUNTIME_VISIBLE_LABELS = [
    "AET_PROD_GroundTile_A01_R3_C3",
    "AET_PROD_TargetDummy_A01",
    "AET_PROD_Portal_A01",
    "AET_PROD_WorkshopCrate_A01",
    "AET_PROD_MKG_AetherKnife_A01",
    "AET_PROD_MKG_AetherCoreUnit_A01",
    "AET_PROD_MKG_SparkPistol_A01",
    "AET_PROD_MKG_AetheriumGrenade_A01",
    "AET_PROD_Camera_Review_A01",
    "AET_PROD_ReviewFillLight_A01",
    "AET_BOOT_KeyLight_Directional",
    "AET_BOOT_SkyLight",
]
EXPECTED_RUNTIME_HIDDEN_LABELS = [
    "AET_BOOT_PlayerScale_180cm",
    "AET_BOOT_GnomeScale_110cm",
    "AET_BOOT_MinotaurScale_270cm",
    "AET_BOOT_Camera_Overview",
    "AET_BOOT_Label_StyleTarget",
]


def all_level_actors():
    actor_subsystem = unreal.get_editor_subsystem(unreal.EditorActorSubsystem)
    return list(actor_subsystem.get_all_level_actors())


def try_call(obj, method_name):
    method = getattr(obj, method_name, None)
    if not callable(method):
        return None
    try:
        return method()
    except Exception:
        return None


def is_actor_hidden_in_game(actor):
    hidden = try_call(actor, "get_actor_hidden_in_game")
    if hidden is not None:
        return bool(hidden)
    try:
        return bool(actor.get_editor_property("hidden"))
    except Exception:
        return False


def component_hidden_or_invisible(component):
    component_name = component.get_name()
    component_class_name = component.get_class().get_name()
    editor_visual_classes = (
        "BillboardComponent",
        "DrawFrustumComponent",
        "CameraProxyMeshComponent",
        "ArrowComponent",
    )
    if component_class_name in editor_visual_classes or any(name in component_name for name in editor_visual_classes):
        return False
    hidden = try_call(component, "is_hidden_in_game")
    visible = try_call(component, "is_visible")
    return bool(hidden) or visible is False


def log_camera_aim(camera_actor):
    location = camera_actor.get_actor_location()
    rotation = camera_actor.get_actor_rotation()
    target = REVIEW_CAMERA_TARGET
    dx = target.x - location.x
    dy = target.y - location.y
    dz = target.z - location.z
    expected_yaw = math.degrees(math.atan2(dy, dx))
    expected_pitch = math.degrees(math.atan2(dz, math.sqrt((dx * dx) + (dy * dy))))
    unreal.log(
        "Aerathea review camera diagnostic: location={} rotation={} expected_pitch={:.2f} expected_yaw={:.2f}.".format(
            location,
            rotation,
            expected_pitch,
            expected_yaw,
        )
    )


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

    actors = all_level_actors()
    actors_by_label = {actor.get_actor_label(): actor for actor in actors}
    actor_labels = set(actors_by_label.keys())
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

    portal_actor = next(
        actor
        for actor in actors
        if actor.get_actor_label() == "AET_PROD_Portal_A01"
    )
    portal_class_name = portal_actor.get_class().get_name()
    if "BP_AET_Portal_A01" not in portal_class_name and "AETPortalActor" not in portal_class_name:
        raise RuntimeError("Portal actor has unexpected class: {}".format(portal_class_name))

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

    runtime_visibility_failures = []
    for label in EXPECTED_RUNTIME_VISIBLE_LABELS:
        actor = actors_by_label.get(label)
        if actor is None:
            continue
        if is_actor_hidden_in_game(actor):
            runtime_visibility_failures.append("{} is hidden in game".format(label))
        primitive_components = actor.get_components_by_class(unreal.PrimitiveComponent)
        for component in primitive_components:
            if component_hidden_or_invisible(component):
                runtime_visibility_failures.append(
                    "{} component {} is hidden or invisible".format(
                        label,
                        component.get_name(),
                    )
                )
    if runtime_visibility_failures:
        raise RuntimeError("Runtime visibility validation failed: {}".format("; ".join(runtime_visibility_failures)))

    hidden_guide_failures = []
    for label in EXPECTED_RUNTIME_HIDDEN_LABELS:
        actor = actors_by_label.get(label)
        if actor is None:
            continue
        if not is_actor_hidden_in_game(actor):
            hidden_guide_failures.append("{} is visible in game".format(label))
    if hidden_guide_failures:
        raise RuntimeError("Runtime hidden-guide validation failed: {}".format("; ".join(hidden_guide_failures)))

    review_camera = actors_by_label["AET_PROD_Camera_Review_A01"]
    if unreal.Name("AET_REVIEW_CAMERA") not in review_camera.get_editor_property("tags"):
        raise RuntimeError("Review camera is missing AET_REVIEW_CAMERA tag")
    log_camera_aim(review_camera)

    unreal.log(
        "Aerathea startup validation complete: {} assets, {} expected actors, {} ground tiles.".format(
            len(EXPECTED_ASSETS),
            len(EXPECTED_ACTOR_LABELS),
            len(ground_tiles),
        )
    )


main()
