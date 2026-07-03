from pathlib import Path


ROOT = Path(__file__).resolve().parents[2]
KIT_ID = "KIT_GIA_BloodAxeCairnVariantBatch_A01"
PACKAGE_DOC = "docs/assets/kits/KIT_GIA_BloodAxeCairnVariantBatch_A01/DCC_GAME_READY_PREP_STATUS.md"
IMPORT_PACKET_DOC = "docs/assets/kits/KIT_GIA_BloodAxeCairnVariantBatch_A01/UNREAL_IMPORT_TASK_PACKET.md"
VISUAL_CANON_SOURCE = "VC-GIA-BloodAxe-CairnStones-A01"

FBX_IMPORT_UNIFORM_SCALE = 0.01

PARENT_MATERIAL_PATH = "/Game/Aerathea/Materials/Giants/BloodAxe/Cairns/M_GIA_BloodAxeCairnVariants_VertexBlend_A01"
MATERIAL_INSTANCE_PATH = "/Game/Aerathea/Materials/Instances/MI_GIA_BloodAxeCairnVariants_A01"
REVIEW_PROXY_MATERIAL_PATH = "/Game/Aerathea/Materials/Review/M_AET_CollisionProxy_Hidden_A01"

ASSETS = [
    {
        "name": "SM_GIA_BloodAxeApproachCairnMarker_A01",
        "source": "SourceAssets/Exports/Props/Giants/BloodAxe/StrongholdApproach/CairnMarkers/SM_GIA_BloodAxeApproachCairnMarker_A01/SM_GIA_BloodAxeApproachCairnMarker_A01.fbx",
        "unreal_path": "/Game/Aerathea/Props/Giants/BloodAxe/StrongholdApproach/CairnMarkers/SM_GIA_BloodAxeApproachCairnMarker_A01",
        "collision_proxies": 1,
    },
    {
        "name": "SM_GIA_BloodAxeRitualCairnGuidepost_A01",
        "source": "SourceAssets/Exports/Props/Giants/BloodAxe/RitualStones/Guideposts/SM_GIA_BloodAxeRitualCairnGuidepost_A01/SM_GIA_BloodAxeRitualCairnGuidepost_A01.fbx",
        "unreal_path": "/Game/Aerathea/Props/Giants/BloodAxe/RitualStones/Guideposts/SM_GIA_BloodAxeRitualCairnGuidepost_A01",
        "collision_proxies": 1,
    },
    {
        "name": "SM_GIA_BloodAxeLowThresholdCairn_A01",
        "source": "SourceAssets/Exports/Props/Giants/BloodAxe/CaveApproachMarkers/SM_GIA_BloodAxeLowThresholdCairn_A01/SM_GIA_BloodAxeLowThresholdCairn_A01.fbx",
        "unreal_path": "/Game/Aerathea/Props/Giants/BloodAxe/CaveApproachMarkers/SM_GIA_BloodAxeLowThresholdCairn_A01",
        "collision_proxies": 1,
    },
    {
        "name": "SM_GIA_BloodAxeCollapsedThresholdCairn_A01",
        "source": "SourceAssets/Exports/Props/Giants/BloodAxe/CaveApproachMarkers/SM_GIA_BloodAxeCollapsedThresholdCairn_A01/SM_GIA_BloodAxeCollapsedThresholdCairn_A01.fbx",
        "unreal_path": "/Game/Aerathea/Props/Giants/BloodAxe/CaveApproachMarkers/SM_GIA_BloodAxeCollapsedThresholdCairn_A01",
        "collision_proxies": 1,
    },
    {
        "name": "SM_GIA_BloodAxeCaveRemnantCairn_A01",
        "source": "SourceAssets/Exports/Props/Giants/BloodAxe/CaveApproachMarkers/SM_GIA_BloodAxeCaveRemnantCairn_A01/SM_GIA_BloodAxeCaveRemnantCairn_A01.fbx",
        "unreal_path": "/Game/Aerathea/Props/Giants/BloodAxe/CaveApproachMarkers/SM_GIA_BloodAxeCaveRemnantCairn_A01",
        "collision_proxies": 1,
    },
    {
        "name": "SM_GIA_BloodAxeCollapsedCaveRemnantCairn_A01",
        "source": "SourceAssets/Exports/Props/Giants/BloodAxe/CaveApproachMarkers/SM_GIA_BloodAxeCollapsedCaveRemnantCairn_A01/SM_GIA_BloodAxeCollapsedCaveRemnantCairn_A01.fbx",
        "unreal_path": "/Game/Aerathea/Props/Giants/BloodAxe/CaveApproachMarkers/SM_GIA_BloodAxeCollapsedCaveRemnantCairn_A01",
        "collision_proxies": 1,
    },
    {
        "name": "SM_GIA_BloodAxeCaveThresholdCairnPair_A01",
        "source": "SourceAssets/Exports/Props/Giants/BloodAxe/CaveApproachMarkers/SM_GIA_BloodAxeCaveThresholdCairnPair_A01/SM_GIA_BloodAxeCaveThresholdCairnPair_A01.fbx",
        "unreal_path": "/Game/Aerathea/Props/Giants/BloodAxe/CaveApproachMarkers/SM_GIA_BloodAxeCaveThresholdCairnPair_A01",
        "collision_proxies": 2,
    },
    {
        "name": "SM_GIA_BloodAxeMovedCampCairnPair_A01",
        "source": "SourceAssets/Exports/Props/Giants/BloodAxe/MovedCamp/SM_GIA_BloodAxeMovedCampCairnPair_A01/SM_GIA_BloodAxeMovedCampCairnPair_A01.fbx",
        "unreal_path": "/Game/Aerathea/Props/Giants/BloodAxe/MovedCamp/SM_GIA_BloodAxeMovedCampCairnPair_A01",
        "collision_proxies": 2,
    },
    {
        "name": "SM_GIA_BloodAxePairedCairnClosePair_A01",
        "source": "SourceAssets/Exports/Props/Giants/BloodAxe/CairnGuideposts/SM_GIA_BloodAxePairedCairnClosePair_A01/SM_GIA_BloodAxePairedCairnClosePair_A01.fbx",
        "unreal_path": "/Game/Aerathea/Props/Giants/BloodAxe/CairnGuideposts/SM_GIA_BloodAxePairedCairnClosePair_A01",
        "collision_proxies": 2,
    },
    {
        "name": "SM_GIA_BloodAxePairedCairnStaggeredPair_A01",
        "source": "SourceAssets/Exports/Props/Giants/BloodAxe/CairnGuideposts/SM_GIA_BloodAxePairedCairnStaggeredPair_A01/SM_GIA_BloodAxePairedCairnStaggeredPair_A01.fbx",
        "unreal_path": "/Game/Aerathea/Props/Giants/BloodAxe/CairnGuideposts/SM_GIA_BloodAxePairedCairnStaggeredPair_A01",
        "collision_proxies": 2,
    },
    {
        "name": "SM_GIA_BloodAxeCairnPathMarker_A01",
        "source": "SourceAssets/Exports/Props/Giants/BloodAxe/PathMarkers/SM_GIA_BloodAxeCairnPathMarker_A01/SM_GIA_BloodAxeCairnPathMarker_A01.fbx",
        "unreal_path": "/Game/Aerathea/Props/Giants/BloodAxe/PathMarkers/SM_GIA_BloodAxeCairnPathMarker_A01",
        "collision_proxies": 1,
    },
    {
        "name": "SM_GIA_BloodAxeCairnScrapCap_A01",
        "source": "SourceAssets/Exports/Props/Giants/BloodAxe/PathMarkers/SM_GIA_BloodAxeCairnScrapCap_A01/SM_GIA_BloodAxeCairnScrapCap_A01.fbx",
        "unreal_path": "/Game/Aerathea/Props/Giants/BloodAxe/PathMarkers/SM_GIA_BloodAxeCairnScrapCap_A01",
        "collision_proxies": 1,
    },
]


def source_path(asset):
    return ROOT / asset["source"]


def import_source_path(asset):
    path = source_path(asset)
    return path.with_name("{}_UnrealImport.fbx".format(asset["name"]))


def lod_path(asset, lod_index):
    path = source_path(asset)
    return path.with_name("{}_LOD{}.fbx".format(asset["name"], lod_index))


def destination_path(asset):
    return asset["unreal_path"].rsplit("/", 1)[0]
