import math

import unreal


LEVEL_PATH = "/Game/Aerathea/Maps/L_Aerathea_Startup"
REVIEW_CAMERA_LOCATION = unreal.Vector(4710.0, -2880.0, 2575.0)
REVIEW_CAMERA_TARGET = unreal.Vector(-70, 160, 110)
EXPECTED_ASSETS = [
    "/Game/Aerathea/Materials/M_AET_Stone_Handpainted_A01",
    "/Game/Aerathea/Materials/M_AET_Timber_Handpainted_A01",
    "/Game/Aerathea/Materials/M_AET_DarkIron_A01",
    "/Game/Aerathea/Materials/M_AET_Brass_A01",
    "/Game/Aerathea/Materials/M_AET_AetheriumGlow_Blue_A01",
    "/Game/Aerathea/Materials/M_GNM_AetherShieldWall_Review_A01",
    "/Game/Aerathea/Materials/M_AET_Straw_A01",
    "/Game/Aerathea/Materials/M_AET_Leather_Dark_A01",
    "/Game/Aerathea/Materials/M_AET_PackedEarth_A01",
    "/Game/Aerathea/Materials/M_AET_Moss_A01",
    "/Game/Aerathea/Materials/M_GNM_Skin_Blockout_A01",
    "/Game/Aerathea/Materials/M_GNM_Workwear_Blockout_A01",
    "/Game/Aerathea/Materials/M_GNM_BootLeather_Blockout_A01",
    "/Game/Aerathea/Materials/M_GNM_Eye_Blockout_A01",
    "/Game/Aerathea/Materials/M_CRE_Gryphon_Feather_Blockout_A01",
    "/Game/Aerathea/Materials/M_CRE_Gryphon_Fur_Blockout_A01",
    "/Game/Aerathea/Materials/M_CRE_Gryphon_Keratin_Blockout_A01",
    "/Game/Aerathea/Materials/M_GIA_Skin_Blockout_A01",
    "/Game/Aerathea/Materials/M_GIA_Tattoo_Blockout_A01",
    "/Game/Aerathea/Materials/M_GIA_Leather_Blockout_A01",
    "/Game/Aerathea/Materials/M_GIA_Fur_Blockout_A01",
    "/Game/Aerathea/Materials/M_GIA_Hair_Blockout_A01",
    "/Game/Aerathea/Materials/M_GIA_Iron_Blockout_A01",
    "/Game/Aerathea/Materials/M_GIA_Stone_Blockout_A01",
    "/Game/Aerathea/Materials/M_GIA_RuneGlow_Blockout_A01",
    "/Game/Aerathea/Materials/M_INF_CultStone_Blockout_A01",
    "/Game/Aerathea/Materials/M_INF_ScorchedStone_Blockout_A01",
    "/Game/Aerathea/Materials/M_INF_ObsidianIron_Blockout_A01",
    "/Game/Aerathea/Materials/M_INF_RitualGlow_Blockout_A01",
    "/Game/Aerathea/Materials/M_OGR_CairnStone_Blockout_A01",
    "/Game/Aerathea/Materials/M_OGR_TekGlow_Blockout_A01",
    "/Game/Aerathea/Materials/M_OGR_SootedCopper_Blockout_A01",
    "/Game/Aerathea/Materials/M_OGR_RuneGlow_Blockout_A01",
    "/Game/Aerathea/Materials/M_OGR_StormRuneGlow_Blockout_A01",
    "/Game/Aerathea/Materials/M_OGR_ShamanStone_Blockout_A01",
    "/Game/Aerathea/Materials/M_OGR_FurMantle_Blockout_A01",
    "/Game/Aerathea/Materials/M_OGR_GraveCloth_Blockout_A01",
    "/Game/Aerathea/Materials/M_OGR_TombMetal_Blockout_A01",
    "/Game/Aerathea/Materials/M_CRE_Manticore_Body_Blockout_A01",
    "/Game/Aerathea/Materials/M_CRE_Manticore_Mane_Blockout_A01",
    "/Game/Aerathea/Materials/M_CRE_Manticore_Wing_Blockout_A01",
    "/Game/Aerathea/Materials/M_CRE_Manticore_TailClaw_Blockout_A01",
    "/Game/Aerathea/Materials/M_CRE_Manticore_Venom_Blockout_A01",
    "/Game/Aerathea/Materials/M_GNM_Mek_DarkIron_Blockout_A01",
    "/Game/Aerathea/Materials/M_GNM_Mek_Brass_Blockout_A01",
    "/Game/Aerathea/Materials/M_GNM_Mek_Copper_Blockout_A01",
    "/Game/Aerathea/Materials/M_GNM_Mek_BluePanel_Blockout_A01",
    "/Game/Aerathea/Materials/M_GNM_Mek_AetheriumGlow_Blockout_A01",
    "/Game/Aerathea/Materials/M_GNM_MekPilotSkin_Blockout_A01",
    "/Game/Aerathea/Materials/M_GNM_MekPilotWorkwear_Blockout_A01",
    "/Game/Aerathea/Materials/M_GNM_MekPilotHair_Blockout_A01",
    "/Game/Aerathea/Materials/M_GNM_Mek_Leather_Blockout_A01",
    "/Game/Aerathea/Materials/M_ABY_CharredFlesh_Blockout_A01",
    "/Game/Aerathea/Materials/M_ABY_ScorchedIron_Blockout_A01",
    "/Game/Aerathea/Materials/M_ABY_AshCloth_Blockout_A01",
    "/Game/Aerathea/Materials/M_ABY_BoneHorn_Blockout_A01",
    "/Game/Aerathea/Materials/M_ABY_PikeBlackIron_Blockout_A01",
    "/Game/Aerathea/Materials/M_ABY_VoidGlow_Blockout_A01",
    "/Game/Aerathea/Materials/M_ABY_EmberFissure_Blockout_A01",
    "/Game/Aerathea/Materials/Gnome/Iona/M_GNM_IonaMek_DarkIron_Blockout_A01",
    "/Game/Aerathea/Materials/Gnome/Iona/M_GNM_IonaMek_BrassCopper_Blockout_A01",
    "/Game/Aerathea/Materials/Gnome/Iona/M_GNM_IonaMek_LeatherCable_Blockout_A01",
    "/Game/Aerathea/Materials/Gnome/Iona/M_GNM_IonaMek_AetheriumGlow_Blockout_A01",
    "/Game/Aerathea/Materials/Gnome/Iona/M_GNM_IonaMek_CockpitGlass_Blockout_A01",
    "/Game/Aerathea/Materials/Gnome/Iona/M_GNM_IonaPilotSkin_Blockout_A01",
    "/Game/Aerathea/Materials/Gnome/Iona/M_GNM_IonaPilotHair_Blockout_A01",
    "/Game/Aerathea/Materials/Gnome/Iona/M_GNM_IonaPilotWorkwear_Blockout_A01",
    "/Game/Aerathea/Materials/Infernals/Mage/M_INF_Mage_Skin_Blockout_A01",
    "/Game/Aerathea/Materials/Infernals/Mage/M_INF_Mage_HornClaw_Blockout_A01",
    "/Game/Aerathea/Materials/Infernals/Mage/M_INF_Mage_Wing_Blockout_A01",
    "/Game/Aerathea/Materials/Infernals/Mage/M_INF_Mage_RitualCloth_Blockout_A01",
    "/Game/Aerathea/Materials/Infernals/Mage/M_INF_Mage_ObsidianArmor_Blockout_A01",
    "/Game/Aerathea/Materials/Infernals/Mage/M_INF_Mage_BoneOrnaments_Blockout_A01",
    "/Game/Aerathea/Materials/Infernals/Mage/M_INF_Mage_AbyssalGlow_Blockout_A01",
    "/Game/Aerathea/Materials/Infernals/Warrior/M_INF_Warrior_Skin_Blockout_A01",
    "/Game/Aerathea/Materials/Infernals/Warrior/M_INF_Warrior_HornClaw_Blockout_A01",
    "/Game/Aerathea/Materials/Infernals/Warrior/M_INF_Warrior_Wing_Blockout_A01",
    "/Game/Aerathea/Materials/Infernals/Warrior/M_INF_Warrior_RitualCloth_Blockout_A01",
    "/Game/Aerathea/Materials/Infernals/Warrior/M_INF_Warrior_ObsidianArmor_Blockout_A01",
    "/Game/Aerathea/Materials/Infernals/Warrior/M_INF_Warrior_BoneOrnaments_Blockout_A01",
    "/Game/Aerathea/Materials/Infernals/Warrior/M_INF_Warrior_AbyssalGlow_Blockout_A01",
    "/Game/Aerathea/Materials/Infernals/Rogue/M_INF_Rogue_Skin_Blockout_A01",
    "/Game/Aerathea/Materials/Infernals/Rogue/M_INF_Rogue_HornClaw_Blockout_A01",
    "/Game/Aerathea/Materials/Infernals/Rogue/M_INF_Rogue_Wing_Blockout_A01",
    "/Game/Aerathea/Materials/Infernals/Rogue/M_INF_Rogue_Wraps_Blockout_A01",
    "/Game/Aerathea/Materials/Infernals/Rogue/M_INF_Rogue_LightArmor_Blockout_A01",
    "/Game/Aerathea/Materials/Infernals/Rogue/M_INF_Rogue_BoneHorn_Blockout_A01",
    "/Game/Aerathea/Materials/Infernals/Rogue/M_INF_Rogue_SightGlow_Blockout_A01",
    "/Game/Aerathea/Materials/Infernals/Hunter/M_INF_Hunter_Skin_Blockout_A01",
    "/Game/Aerathea/Materials/Infernals/Hunter/M_INF_Hunter_HornClaw_Blockout_A01",
    "/Game/Aerathea/Materials/Infernals/Hunter/M_INF_Hunter_Wing_Blockout_A01",
    "/Game/Aerathea/Materials/Infernals/Hunter/M_INF_Hunter_HarnessLeather_Blockout_A01",
    "/Game/Aerathea/Materials/Infernals/Hunter/M_INF_Hunter_PursuitArmor_Blockout_A01",
    "/Game/Aerathea/Materials/Infernals/Hunter/M_INF_Hunter_BoneHorn_Blockout_A01",
    "/Game/Aerathea/Materials/Infernals/Hunter/M_INF_Hunter_SightMarkGlow_Blockout_A01",
    "/Game/Aerathea/Materials/Infernals/HornWingArch/M_INF_HornWingArch_CultStone_Blockout_A01",
    "/Game/Aerathea/Materials/Infernals/HornWingArch/M_INF_HornWingArch_ScorchedStone_Blockout_A01",
    "/Game/Aerathea/Materials/Infernals/HornWingArch/M_INF_HornWingArch_ObsidianIron_Blockout_A01",
    "/Game/Aerathea/Materials/Infernals/HornWingArch/M_INF_HornWingArch_BoneHorn_Blockout_A01",
    "/Game/Aerathea/Materials/Infernals/HornWingArch/M_INF_HornWingArch_BrandGlow_Blockout_A01",
    "/Game/Aerathea/Materials/Infernals/WorthinessAltar/M_INF_WorthinessAltar_CultStone_Blockout_A01",
    "/Game/Aerathea/Materials/Infernals/WorthinessAltar/M_INF_WorthinessAltar_ScorchedStone_Blockout_A01",
    "/Game/Aerathea/Materials/Infernals/WorthinessAltar/M_INF_WorthinessAltar_ObsidianIron_Blockout_A01",
    "/Game/Aerathea/Materials/Infernals/WorthinessAltar/M_INF_WorthinessAltar_BoneHorn_Blockout_A01",
    "/Game/Aerathea/Materials/Infernals/WorthinessAltar/M_INF_WorthinessAltar_BrandGlow_Blockout_A01",
    "/Game/Aerathea/Materials/Infernals/M_INF_BrandGlow_Master_A01",
    "/Game/Aerathea/Materials/Infernals/MF_INF_BrandGlowStates_A01",
    "/Game/Aerathea/Materials/Instances/MI_INF_BrandGlowStates_A01_Inactive",
    "/Game/Aerathea/Materials/Instances/MI_INF_BrandGlowStates_A01_Smolder",
    "/Game/Aerathea/Materials/Instances/MI_INF_BrandGlowStates_A01_TrialActive",
    "/Game/Aerathea/Materials/Instances/MI_INF_BrandGlowStates_A01_Accepted",
    "/Game/Aerathea/Materials/Instances/MI_INF_BrandGlowStates_A01_Rejected",
    "/Game/Aerathea/Materials/Instances/MI_INF_BrandGlowStates_A01_SorcererFocus",
    "/Game/Aerathea/Materials/Infernals/VFX/M_INF_WorthinessRing_A01",
    "/Game/Aerathea/Materials/Infernals/VFX/M_INF_WorthinessSigil_A01",
    "/Game/Aerathea/Materials/Infernals/VFX/M_INF_WorthinessAsh_A01",
    "/Game/Aerathea/Materials/Infernals/VFX/M_INF_WorthinessRejected_A01",
    "/Game/Aerathea/Materials/Infernals/VFX/M_INF_WorthinessJudgmentPulse_A01",
    "/Game/Aerathea/Materials/Instances/MI_INF_WorthinessRing_A01",
    "/Game/Aerathea/Materials/Instances/MI_INF_WorthinessSigil_A01",
    "/Game/Aerathea/Materials/Instances/MI_INF_WorthinessAsh_A01",
    "/Game/Aerathea/Materials/Instances/MI_INF_WorthinessRejected_A01",
    "/Game/Aerathea/Materials/Instances/MI_INF_WorthinessJudgmentPulse_A01",
    "/Game/Aerathea/VFX/Infernals/WorthinessJudgment/NS_INF_Worthiness_Inactive_A01",
    "/Game/Aerathea/VFX/Infernals/WorthinessJudgment/NS_INF_Worthiness_Smolder_A01",
    "/Game/Aerathea/VFX/Infernals/WorthinessJudgment/NS_INF_Worthiness_TrialActive_A01",
    "/Game/Aerathea/VFX/Infernals/WorthinessJudgment/NS_INF_Worthiness_Accepted_A01",
    "/Game/Aerathea/VFX/Infernals/WorthinessJudgment/NS_INF_Worthiness_Rejected_A01",
    "/Game/Aerathea/VFX/Infernals/WorthinessJudgment/NS_INF_Worthiness_JudgmentPulse_A01",
    "/Game/Aerathea/VFX/Infernals/WorthinessJudgment/NE_INF_WorthinessRingPulse_A01",
    "/Game/Aerathea/VFX/Infernals/WorthinessJudgment/NE_INF_WorthinessSigilPulse_A01",
    "/Game/Aerathea/VFX/Infernals/WorthinessJudgment/NE_INF_WorthinessAshMote_A01",
    "/Game/Aerathea/VFX/Infernals/WorthinessJudgment/NE_INF_WorthinessRejectedSnap_A01",
    "/Game/Aerathea/Props/Training/SM_AET_TargetDummy_A01",
    "/Game/Aerathea/Props/Portal/SM_AET_PortalArch_A01",
    "/Game/Aerathea/Props/Environment/SM_AET_ModularGroundTile_A01",
    "/Game/Aerathea/Props/Mekgineer/SM_MKG_WorkshopPropCrate_A01",
    "/Game/Aerathea/Weapons/Mekgineer/SM_MKG_AetherKnife_A01",
    "/Game/Aerathea/Props/Mekgineer/Armory/SM_MKG_AetherCoreUnit_A01",
    "/Game/Aerathea/Weapons/Mekgineer/SM_MKG_SparkPistol_A01",
    "/Game/Aerathea/Props/Mekgineer/Armory/SM_MKG_AetheriumGrenade_A01",
    "/Game/Aerathea/Props/Mekgineer/Armory/SM_MKG_MultiTool_A01",
    "/Game/Aerathea/Props/Mekgineer/Armory/SM_MKG_GrappleHook_A01",
    "/Game/Aerathea/Props/Gnomes/Mekgineer/SM_GNM_AetherShieldProjector_A01",
    "/Game/Aerathea/VFX/GnomeOgre/SM_GNM_AetherShieldWall_A01",
    "/Game/Aerathea/VFX/GnomeOgre/VFX_GNM_AetherShieldWall_A01",
    "/Game/Aerathea/VFX/GnomeOgre/NS_GNM_AetherShieldWall_A01",
    "/Game/Aerathea/VFX/Ogres/NS_OGR_CrudeTekPylon_A01",
    "/Game/Aerathea/VFX/Creatures/NS_CRE_Manticore_Impact_A01",
    "/Game/Aerathea/Weapons/Mekgineer/SM_MKG_SpikeDrill_A01",
    "/Game/Aerathea/Weapons/Mekgineer/SM_MKG_MonkeyWrench_A01",
    "/Game/Aerathea/Weapons/Mekgineer/SM_MKG_RatchetCleaver_A01",
    "/Game/Aerathea/Weapons/Mekgineer/SM_MKG_GearMace_A01",
    "/Game/Aerathea/Props/Mekgineer/Armory/SM_MKG_ToolPack_A01",
    "/Game/Aerathea/Buildings/Common/Palisade/SM_AET_Palisade_Wall_A01",
    "/Game/Aerathea/Buildings/Common/Palisade/SM_AET_Palisade_Post_A01",
    "/Game/Aerathea/Buildings/Common/Palisade/SM_AET_Palisade_Corner_A01",
    "/Game/Aerathea/Buildings/Common/Palisade/SM_AET_Palisade_Gate_A01",
    "/Game/Aerathea/Buildings/Common/Palisade/SM_AET_Palisade_EndCap_A01",
    "/Game/Aerathea/Props/Ogres/CairnFortifications/SM_OGR_CairnBattleGate_A01",
    "/Game/Aerathea/Characters/Gnomes/Base/SK_GNM_Base_A01",
    "/Game/Aerathea/Characters/Gnomes/Base/SK_GNM_Base_A01_Skeleton",
    "/Game/Aerathea/Characters/Gnomes/Base/PHYS_GNM_Base_A01",
    "/Game/Aerathea/Characters/Gnomes/Base/ABP_GNM_Base_A01",
    "/Game/Aerathea/Creatures/Gryphon/Base/SK_CRE_Gryphon_A01",
    "/Game/Aerathea/Creatures/Gryphon/Base/SK_CRE_Gryphon_A01_Skeleton",
    "/Game/Aerathea/Creatures/Gryphon/Base/PHYS_CRE_Gryphon_A01",
    "/Game/Aerathea/Creatures/Gryphon/Base/SK_CRE_Gryphon_A01_Anim",
    "/Game/Aerathea/Creatures/Gryphon/Base/ABP_CRE_Gryphon_A01",
    "/Game/Aerathea/Characters/Giants/Base/SK_GIA_Base_Male_A01",
    "/Game/Aerathea/Characters/Giants/Base/SK_GIA_Base_Male_A01_Skeleton",
    "/Game/Aerathea/Characters/Giants/Base/PHYS_GIA_Base_Male_A01",
    "/Game/Aerathea/Characters/Giants/Base/ABP_GIA_Base_Male_A01",
    "/Game/Aerathea/Characters/Giants/Base/SK_GIA_Base_Female_A01",
    "/Game/Aerathea/Characters/Giants/Base/SK_GIA_Base_Female_A01_Skeleton",
    "/Game/Aerathea/Characters/Giants/Base/PHYS_GIA_Base_Female_A01",
    "/Game/Aerathea/Characters/Giants/Base/ABP_GIA_Base_Female_A01",
    "/Game/Aerathea/Characters/Ogres/Teknomancer/SK_OGR_Teknomancer_A01",
    "/Game/Aerathea/Characters/Ogres/Teknomancer/PHYS_OGR_Teknomancer_A01",
    "/Game/Aerathea/Characters/Ogres/Teknomancer/ABP_OGR_Teknomancer_A01",
    "/Game/Aerathea/Characters/Ogres/Warrior/SK_OGR_Warrior_Rival_A01",
    "/Game/Aerathea/Characters/Ogres/Warrior/PHYS_OGR_Warrior_Rival_A01",
    "/Game/Aerathea/Characters/Ogres/Warrior/ABP_OGR_Warrior_Rival_A01",
    "/Game/Aerathea/Characters/Gnomes/Meks/SK_GNM_HeavyMek_Rivalry_A01",
    "/Game/Aerathea/Characters/Gnomes/Meks/SK_GNM_HeavyMek_Rivalry_A01_Skeleton",
    "/Game/Aerathea/Characters/Gnomes/Meks/PHYS_GNM_HeavyMek_Rivalry_A01",
    "/Game/Aerathea/Characters/Gnomes/Meks/ABP_GNM_HeavyMek_Rivalry_A01",
    "/Game/Aerathea/Props/Ogres/Teknomancy/SM_OGR_CrudeTekPylon_A01",
    "/Game/Aerathea/Creatures/Manticores/Base/SK_CRE_Manticore_A01",
    "/Game/Aerathea/Creatures/Manticores/Base/SK_CRE_Manticore_A01_Skeleton",
    "/Game/Aerathea/Creatures/Manticores/Base/PHYS_CRE_Manticore_A01",
    "/Game/Aerathea/Creatures/Manticores/Base/ABP_CRE_Manticore_A01",
    "/Game/Aerathea/Creatures/Manticores/SK_CRE_Manticore_Interrupt_A01",
    "/Game/Aerathea/Creatures/Manticores/PHYS_CRE_Manticore_Interrupt_A01",
    "/Game/Aerathea/Characters/Ogres/Shaman/SK_OGR_Shaman_A01",
    "/Game/Aerathea/Characters/Ogres/Shaman/PHYS_OGR_Shaman_A01",
    "/Game/Aerathea/Characters/Ogres/Shaman/ABP_OGR_Shaman_A01",
    "/Game/Aerathea/Characters/Ogres/Necromancer/SK_OGR_Necromancer_A01",
    "/Game/Aerathea/Characters/Ogres/Necromancer/PHYS_OGR_Necromancer_A01",
    "/Game/Aerathea/Characters/Ogres/Necromancer/ABP_OGR_Necromancer_A01",
    "/Game/Aerathea/Creatures/Abyss/Troops/BlackPikeTrooper/SK_ABY_BlackPikeTrooper_A01",
    "/Game/Aerathea/Creatures/Abyss/Troops/BlackPikeTrooper/SK_ABY_BlackPikeTrooper_A01_Skeleton",
    "/Game/Aerathea/Creatures/Abyss/Troops/BlackPikeTrooper/PHYS_ABY_BlackPikeTrooper_A01",
    "/Game/Aerathea/Creatures/Abyss/Troops/BlackPikeTrooper/ABP_ABY_Trooper_A01",
    "/Game/Aerathea/Characters/Gnomes/Iona/Mek/SK_GNM_IonaSiegebreakerMek_A01",
    "/Game/Aerathea/Characters/Gnomes/Iona/Mek/SK_GNM_IonaSiegebreakerMek_A01_Skeleton",
    "/Game/Aerathea/Characters/Gnomes/Iona/Mek/PHYS_GNM_IonaSiegebreakerMek_A01",
    "/Game/Aerathea/Characters/Gnomes/Iona/Mek/ABP_GNM_IonaSiegebreakerMek_A01",
    "/Game/Aerathea/Characters/Infernals/Base/SK_INF_Base_Compact_A01_Skeleton",
    "/Game/Aerathea/Characters/Infernals/Base/SK_INF_Base_Tall_A01_Skeleton",
    "/Game/Aerathea/Characters/Infernals/Mage/SK_INF_Mage_A01",
    "/Game/Aerathea/Characters/Infernals/Mage/PHYS_INF_Mage_A01",
    "/Game/Aerathea/Characters/Infernals/Mage/ABP_INF_Mage_A01",
    "/Game/Aerathea/Characters/Infernals/Warrior/SK_INF_Warrior_A01",
    "/Game/Aerathea/Characters/Infernals/Warrior/PHYS_INF_Warrior_A01",
    "/Game/Aerathea/Characters/Infernals/Warrior/ABP_INF_Warrior_A01",
    "/Game/Aerathea/Characters/Infernals/Rogue/SK_INF_Rogue_A01",
    "/Game/Aerathea/Characters/Infernals/Rogue/PHYS_INF_Rogue_A01",
    "/Game/Aerathea/Characters/Infernals/Rogue/ABP_INF_Rogue_A01",
    "/Game/Aerathea/Characters/Infernals/Hunter/SK_INF_Hunter_A01",
    "/Game/Aerathea/Characters/Infernals/Hunter/PHYS_INF_Hunter_A01",
    "/Game/Aerathea/Characters/Infernals/Hunter/ABP_INF_Hunter_A01",
    "/Game/Aerathea/Props/Infernals/BalgorothCult/SM_INF_CullingTrialFloor_A01",
    "/Game/Aerathea/Props/Infernals/BalgorothCult/SM_INF_HornWingArch_A01",
    "/Game/Aerathea/Props/Infernals/BalgorothCult/SM_INF_WorthinessAltar_A01",
    "/Game/Aerathea/Blueprints/Infernals/BP_INF_RitualAltar_A01",
    "/Game/Aerathea/Blueprints/Props/BP_AET_Portal_A01",
    "/Game/Aerathea/Blueprints/Props/BP_AET_TargetDummy_A01",
    "/Game/Aerathea/Blueprints/GnomeOgre/BP_GNM_HeavyMekShieldwall_A01",
    "/Game/Aerathea/Blueprints/GnomeOgre/BP_GNM_OGR_BattlefieldEncounter_A01",
    "/Game/Aerathea/Blueprints/Ogres/BP_OGR_CrudeTekPylon_A01",
    "/Game/Aerathea/Blueprints/Creatures/BP_CRE_ManticoreInterrupt_A01",
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
    "AET_PROD_MKG_MultiTool_A01",
    "AET_PROD_MKG_GrappleHook_A01",
    "AET_PROD_GNM_HeavyMekShieldwall_A01",
    "AET_PROD_MKG_SpikeDrill_A01",
    "AET_PROD_MKG_MonkeyWrench_A01",
    "AET_PROD_MKG_RatchetCleaver_A01",
    "AET_PROD_MKG_GearMace_A01",
    "AET_PROD_GnomeBase_A01",
    "AET_PROD_MKG_ToolPack_BackFit_A01",
    "AET_PROD_CRE_Gryphon_A01",
    "AET_PROD_GiantMaleBase_A01",
    "AET_PROD_GiantFemaleBase_A01",
    "AET_PROD_Palisade_Wall_A01",
    "AET_PROD_Palisade_Post_A01",
    "AET_PROD_Palisade_EndCap_A01",
    "AET_PROD_Palisade_Corner_A01",
    "AET_PROD_Palisade_Gate_A01",
    "AET_PROD_INF_CullingTrialFloor_A01",
    "AET_PROD_INF_HornWingArch_A01",
    "AET_PROD_INF_WorthinessAltar_A01",
    "AET_PROD_OgreTeknomancer_A01",
    "AET_PROD_OgreWarrior_Rival_A01",
    "AET_PROD_OGR_CairnBattleGate_A01",
    "AET_PROD_GNM_HeavyMek_Rivalry_A01",
    "AET_PROD_OGR_CrudeTekPylon_A01",
    "AET_PROD_CRE_Manticore_A01",
    "AET_PROD_CRE_Manticore_Interrupt_A01",
    "AET_PROD_OgreShaman_A01",
    "AET_PROD_OgreNecromancer_A01",
    "AET_PROD_ABY_BlackPikeTrooper_A01",
    "AET_PROD_GNM_IonaSiegebreakerMek_A01",
    "AET_PROD_INF_Mage_A01",
    "AET_PROD_INF_Warrior_A01",
    "AET_PROD_INF_Rogue_A01",
    "AET_PROD_INF_Hunter_A01",
    "AET_PROD_GNM_OGR_BattlefieldEncounter_A01",
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
    "/Game/Aerathea/Props/Mekgineer/Armory/SM_MKG_MultiTool_A01",
    "/Game/Aerathea/Props/Mekgineer/Armory/SM_MKG_GrappleHook_A01",
    "/Game/Aerathea/Props/Gnomes/Mekgineer/SM_GNM_AetherShieldProjector_A01",
    "/Game/Aerathea/VFX/GnomeOgre/SM_GNM_AetherShieldWall_A01",
    "/Game/Aerathea/Weapons/Mekgineer/SM_MKG_SpikeDrill_A01",
    "/Game/Aerathea/Weapons/Mekgineer/SM_MKG_MonkeyWrench_A01",
    "/Game/Aerathea/Weapons/Mekgineer/SM_MKG_RatchetCleaver_A01",
    "/Game/Aerathea/Weapons/Mekgineer/SM_MKG_GearMace_A01",
    "/Game/Aerathea/Props/Mekgineer/Armory/SM_MKG_ToolPack_A01",
    "/Game/Aerathea/Buildings/Common/Palisade/SM_AET_Palisade_Wall_A01",
    "/Game/Aerathea/Buildings/Common/Palisade/SM_AET_Palisade_Post_A01",
    "/Game/Aerathea/Buildings/Common/Palisade/SM_AET_Palisade_Corner_A01",
    "/Game/Aerathea/Buildings/Common/Palisade/SM_AET_Palisade_Gate_A01",
    "/Game/Aerathea/Buildings/Common/Palisade/SM_AET_Palisade_EndCap_A01",
    "/Game/Aerathea/Props/Ogres/CairnFortifications/SM_OGR_CairnBattleGate_A01",
    "/Game/Aerathea/Props/Ogres/Teknomancy/SM_OGR_CrudeTekPylon_A01",
    "/Game/Aerathea/Props/Infernals/BalgorothCult/SM_INF_CullingTrialFloor_A01",
    "/Game/Aerathea/Props/Infernals/BalgorothCult/SM_INF_HornWingArch_A01",
    "/Game/Aerathea/Props/Infernals/BalgorothCult/SM_INF_WorthinessAltar_A01",
]
EXPECTED_SKELETAL_MESHES = [
    (
        "/Game/Aerathea/Characters/Gnomes/Base/SK_GNM_Base_A01",
        "/Game/Aerathea/Characters/Gnomes/Base/PHYS_GNM_Base_A01",
        "/Game/Aerathea/Characters/Gnomes/Base/SK_GNM_Base_A01_Skeleton",
    ),
    (
        "/Game/Aerathea/Creatures/Gryphon/Base/SK_CRE_Gryphon_A01",
        "/Game/Aerathea/Creatures/Gryphon/Base/PHYS_CRE_Gryphon_A01",
        "/Game/Aerathea/Creatures/Gryphon/Base/SK_CRE_Gryphon_A01_Skeleton",
    ),
    (
        "/Game/Aerathea/Characters/Giants/Base/SK_GIA_Base_Male_A01",
        "/Game/Aerathea/Characters/Giants/Base/PHYS_GIA_Base_Male_A01",
        "/Game/Aerathea/Characters/Giants/Base/SK_GIA_Base_Male_A01_Skeleton",
    ),
    (
        "/Game/Aerathea/Characters/Giants/Base/SK_GIA_Base_Female_A01",
        "/Game/Aerathea/Characters/Giants/Base/PHYS_GIA_Base_Female_A01",
        "/Game/Aerathea/Characters/Giants/Base/SK_GIA_Base_Female_A01_Skeleton",
    ),
    (
        "/Game/Aerathea/Characters/Ogres/Teknomancer/SK_OGR_Teknomancer_A01",
        "/Game/Aerathea/Characters/Ogres/Teknomancer/PHYS_OGR_Teknomancer_A01",
        "/Game/Aerathea/Characters/Ogres/Base/SK_OGR_Base_Male_A01_Skeleton",
    ),
    (
        "/Game/Aerathea/Characters/Ogres/Warrior/SK_OGR_Warrior_Rival_A01",
        "/Game/Aerathea/Characters/Ogres/Warrior/PHYS_OGR_Warrior_Rival_A01",
        "/Game/Aerathea/Characters/Ogres/Base/SK_OGR_Base_Male_A01_Skeleton",
    ),
    (
        "/Game/Aerathea/Characters/Gnomes/Meks/SK_GNM_HeavyMek_Rivalry_A01",
        "/Game/Aerathea/Characters/Gnomes/Meks/PHYS_GNM_HeavyMek_Rivalry_A01",
        "/Game/Aerathea/Characters/Gnomes/Meks/SK_GNM_HeavyMek_Rivalry_A01_Skeleton",
    ),
    (
        "/Game/Aerathea/Creatures/Manticores/Base/SK_CRE_Manticore_A01",
        "/Game/Aerathea/Creatures/Manticores/Base/PHYS_CRE_Manticore_A01",
        "/Game/Aerathea/Creatures/Manticores/Base/SK_CRE_Manticore_A01_Skeleton",
    ),
    (
        "/Game/Aerathea/Creatures/Manticores/SK_CRE_Manticore_Interrupt_A01",
        "/Game/Aerathea/Creatures/Manticores/PHYS_CRE_Manticore_Interrupt_A01",
        "/Game/Aerathea/Creatures/Manticores/Base/SK_CRE_Manticore_A01_Skeleton",
    ),
    (
        "/Game/Aerathea/Characters/Ogres/Shaman/SK_OGR_Shaman_A01",
        "/Game/Aerathea/Characters/Ogres/Shaman/PHYS_OGR_Shaman_A01",
        "/Game/Aerathea/Characters/Ogres/Base/SK_OGR_Base_Male_A01_Skeleton",
    ),
    (
        "/Game/Aerathea/Characters/Ogres/Necromancer/SK_OGR_Necromancer_A01",
        "/Game/Aerathea/Characters/Ogres/Necromancer/PHYS_OGR_Necromancer_A01",
        "/Game/Aerathea/Characters/Ogres/Base/SK_OGR_Base_Male_A01_Skeleton",
    ),
    (
        "/Game/Aerathea/Creatures/Abyss/Troops/BlackPikeTrooper/SK_ABY_BlackPikeTrooper_A01",
        "/Game/Aerathea/Creatures/Abyss/Troops/BlackPikeTrooper/PHYS_ABY_BlackPikeTrooper_A01",
        "/Game/Aerathea/Creatures/Abyss/Troops/BlackPikeTrooper/SK_ABY_BlackPikeTrooper_A01_Skeleton",
    ),
    (
        "/Game/Aerathea/Characters/Gnomes/Iona/Mek/SK_GNM_IonaSiegebreakerMek_A01",
        "/Game/Aerathea/Characters/Gnomes/Iona/Mek/PHYS_GNM_IonaSiegebreakerMek_A01",
        "/Game/Aerathea/Characters/Gnomes/Iona/Mek/SK_GNM_IonaSiegebreakerMek_A01_Skeleton",
    ),
    (
        "/Game/Aerathea/Characters/Infernals/Mage/SK_INF_Mage_A01",
        "/Game/Aerathea/Characters/Infernals/Mage/PHYS_INF_Mage_A01",
        "/Game/Aerathea/Characters/Infernals/Base/SK_INF_Base_Tall_A01_Skeleton",
    ),
    (
        "/Game/Aerathea/Characters/Infernals/Warrior/SK_INF_Warrior_A01",
        "/Game/Aerathea/Characters/Infernals/Warrior/PHYS_INF_Warrior_A01",
        "/Game/Aerathea/Characters/Infernals/Base/SK_INF_Base_Tall_A01_Skeleton",
    ),
    (
        "/Game/Aerathea/Characters/Infernals/Rogue/SK_INF_Rogue_A01",
        "/Game/Aerathea/Characters/Infernals/Rogue/PHYS_INF_Rogue_A01",
        "/Game/Aerathea/Characters/Infernals/Base/SK_INF_Base_Compact_A01_Skeleton",
    ),
    (
        "/Game/Aerathea/Characters/Infernals/Hunter/SK_INF_Hunter_A01",
        "/Game/Aerathea/Characters/Infernals/Hunter/PHYS_INF_Hunter_A01",
        "/Game/Aerathea/Characters/Infernals/Base/SK_INF_Base_Tall_A01_Skeleton",
    ),
]
EXPECTED_LOD_STATIC_MESHES = [
    "/Game/Aerathea/Props/Portal/SM_AET_PortalArch_A01",
    "/Game/Aerathea/Props/Mekgineer/Armory/SM_MKG_MultiTool_A01",
    "/Game/Aerathea/Props/Mekgineer/Armory/SM_MKG_GrappleHook_A01",
    "/Game/Aerathea/Props/Gnomes/Mekgineer/SM_GNM_AetherShieldProjector_A01",
    "/Game/Aerathea/VFX/GnomeOgre/SM_GNM_AetherShieldWall_A01",
    "/Game/Aerathea/Weapons/Mekgineer/SM_MKG_SpikeDrill_A01",
    "/Game/Aerathea/Weapons/Mekgineer/SM_MKG_MonkeyWrench_A01",
    "/Game/Aerathea/Weapons/Mekgineer/SM_MKG_RatchetCleaver_A01",
    "/Game/Aerathea/Weapons/Mekgineer/SM_MKG_GearMace_A01",
    "/Game/Aerathea/Props/Mekgineer/Armory/SM_MKG_ToolPack_A01",
    "/Game/Aerathea/Buildings/Common/Palisade/SM_AET_Palisade_Wall_A01",
    "/Game/Aerathea/Buildings/Common/Palisade/SM_AET_Palisade_Post_A01",
    "/Game/Aerathea/Buildings/Common/Palisade/SM_AET_Palisade_Corner_A01",
    "/Game/Aerathea/Buildings/Common/Palisade/SM_AET_Palisade_Gate_A01",
    "/Game/Aerathea/Buildings/Common/Palisade/SM_AET_Palisade_EndCap_A01",
    "/Game/Aerathea/Props/Ogres/CairnFortifications/SM_OGR_CairnBattleGate_A01",
    "/Game/Aerathea/Props/Ogres/Teknomancy/SM_OGR_CrudeTekPylon_A01",
    "/Game/Aerathea/Props/Infernals/BalgorothCult/SM_INF_CullingTrialFloor_A01",
    "/Game/Aerathea/Props/Infernals/BalgorothCult/SM_INF_HornWingArch_A01",
    "/Game/Aerathea/Props/Infernals/BalgorothCult/SM_INF_WorthinessAltar_A01",
]
EXPECTED_STATIC_MESH_SOCKETS = [
    (
        "/Game/Aerathea/Props/Portal/SM_AET_PortalArch_A01",
        [
            "Socket_PortalCore",
            "Socket_VFX_Center",
            "Socket_Audio_Hum",
        ],
    ),
    (
        "/Game/Aerathea/Props/Mekgineer/Armory/SM_MKG_GrappleHook_A01",
        [
            "socket_muzzle",
            "socket_beam",
            "socket_cable",
        ],
    ),
    (
        "/Game/Aerathea/Props/Gnomes/Mekgineer/SM_GNM_AetherShieldProjector_A01",
        [
            "vfx_core",
            "vfx_shield_emit_l",
            "vfx_shield_emit_r",
            "attach_mek_l",
            "attach_mek_r",
            "damage_spark",
        ],
    ),
    (
        "/Game/Aerathea/Props/Infernals/BalgorothCult/SM_INF_CullingTrialFloor_A01",
        [
            "vfx_center",
            "vfx_ring_active",
            "vfx_rejected_gap",
            "snap_altar",
            "snap_arch_front",
            "stage_spawn",
            "stage_blooded",
            "stage_elder",
        ],
    ),
    (
        "/Game/Aerathea/Props/Infernals/BalgorothCult/SM_INF_HornWingArch_A01",
        [
            "snap_floor",
            "snap_altar",
            "guard_l",
            "guard_r",
            "banner_l",
            "banner_r",
            "vfx_crown",
            "vfx_eye",
            "vfx_inner_throat",
            "vfx_rejected_gap",
        ],
    ),
    (
        "/Game/Aerathea/Props/Infernals/BalgorothCult/SM_INF_WorthinessAltar_A01",
        [
            "snap_floor",
            "snap_arch_back",
            "interact_front",
            "stage_offering",
            "vfx_altar_core",
            "vfx_sacrifice_mark",
            "vfx_brand_transfer",
            "vfx_ring_link",
            "vfx_rejected_gap",
        ],
    ),
    (
        "/Game/Aerathea/Props/Ogres/CairnFortifications/SM_OGR_CairnBattleGate_A01",
        [
            "snap_wall_l",
            "snap_wall_r",
            "gate_center",
            "portcullis_top",
            "portcullis_bottom",
            "vfx_brazier_l",
            "vfx_brazier_r",
            "vfx_gate_forge",
            "vfx_skull_crest",
            "socket_banner_l",
            "socket_banner_r",
            "ai_gate_defender_l",
            "ai_gate_defender_r",
        ],
    ),
    (
        "/Game/Aerathea/Props/Ogres/Teknomancy/SM_OGR_CrudeTekPylon_A01",
        [
            "socket_core",
            "socket_top_arc",
            "socket_conductor_l",
            "socket_conductor_r",
            "socket_vent_l",
            "socket_vent_r",
            "socket_cable_in",
            "socket_cable_out",
            "socket_hit_core",
            "socket_repair_panel",
            "socket_ground_sparks",
            "socket_overload_burst",
        ],
    ),
]
EXPECTED_SKELETAL_MESH_SOCKETS = [
    (
        "/Game/Aerathea/Characters/Gnomes/Base/SK_GNM_Base_A01",
        [
            "hand_r_weapon",
            "hand_l_offhand",
            "back_pack",
            "head_goggles",
            "belt_tool_l",
            "belt_tool_r",
            "muzzle_preview",
            "vfx_aether_core",
        ],
    ),
    (
        "/Game/Aerathea/Creatures/Gryphon/Base/SK_CRE_Gryphon_A01",
        [
            "socket_head_vfx",
            "socket_beak",
            "socket_talon_l",
            "socket_talon_r",
            "socket_back_mount",
            "socket_saddle",
            "socket_wing_l_vfx",
            "socket_wing_r_vfx",
            "socket_tail",
        ],
    ),
    (
        "/Game/Aerathea/Characters/Giants/Base/SK_GIA_Base_Male_A01",
        [
            "hand_r_weapon",
            "hand_l_offhand",
            "hand_r_twohand_grip",
            "hand_l_twohand_grip",
            "back_large_weapon",
            "back_shield",
            "belt_tool_l",
            "belt_tool_r",
            "head_hair_ornament",
            "chest_talisman",
            "vfx_rune_hand_l",
            "vfx_rune_hand_r",
            "vfx_stomp_ground",
        ],
    ),
    (
        "/Game/Aerathea/Characters/Giants/Base/SK_GIA_Base_Female_A01",
        [
            "hand_r_weapon",
            "hand_l_offhand",
            "hand_r_twohand_grip",
            "hand_l_twohand_grip",
            "back_large_weapon",
            "back_shield",
            "belt_tool_l",
            "belt_tool_r",
            "head_hair_ornament",
            "chest_talisman",
            "vfx_rune_hand_l",
            "vfx_rune_hand_r",
            "vfx_stomp_ground",
        ],
    ),
    (
        "/Game/Aerathea/Characters/Ogres/Teknomancer/SK_OGR_Teknomancer_A01",
        [
            "hand_r_weapon",
            "hand_l_offhand",
            "hand_r_twohand_grip",
            "hand_l_twohand_grip",
            "spine_teknomancy_pack",
            "vfx_chest_core",
            "vfx_mouth",
            "vfx_stomp_ground",
            "vfx_hammer_core",
            "vfx_bracer_l",
            "vfx_bracer_r",
            "vfx_tek_core",
            "weapon_socket_r",
            "head_fx",
        ],
    ),
    (
        "/Game/Aerathea/Characters/Ogres/Warrior/SK_OGR_Warrior_Rival_A01",
        [
            "hand_r_weapon",
            "hand_l_offhand",
            "hand_r_twohand_grip",
            "hand_l_twohand_grip",
            "back_large_weapon",
            "back_shield",
            "belt_front",
            "vfx_belt_forge",
            "vfx_shield_core",
            "vfx_hammer_core",
            "vfx_stomp_ground",
            "head_fx",
        ],
    ),
    (
        "/Game/Aerathea/Characters/Gnomes/Meks/SK_GNM_HeavyMek_Rivalry_A01",
        [
            "vfx_reactor_core",
            "vfx_shield_l",
            "vfx_shield_r",
            "weapon_cannon_muzzle",
            "pilot_hatch",
            "foot_l",
            "foot_r",
            "vfx_stomp_l",
            "vfx_stomp_r",
            "weapon_hammer_socket",
            "vfx_chest_core",
        ],
    ),
    (
        "/Game/Aerathea/Creatures/Manticores/Base/SK_CRE_Manticore_A01",
        [
            "socket_head_fx",
            "socket_mouth_fx",
            "socket_bite_trace",
            "socket_claw_l",
            "socket_claw_r",
            "socket_foot_l",
            "socket_foot_r",
            "socket_wing_l_root",
            "socket_wing_r_root",
            "socket_wing_l_tip",
            "socket_wing_r_tip",
            "socket_tail_base",
            "socket_tail_mid",
            "socket_tail_stinger",
            "socket_vfx_venom_drip",
            "socket_vfx_landing_dust",
            "socket_back_variant",
        ],
    ),
    (
        "/Game/Aerathea/Creatures/Manticores/SK_CRE_Manticore_Interrupt_A01",
        [
            "socket_head_fx",
            "socket_mouth_fx",
            "socket_bite_trace",
            "socket_claw_l",
            "socket_claw_r",
            "socket_foot_l",
            "socket_foot_r",
            "socket_wing_l_root",
            "socket_wing_r_root",
            "socket_wing_l_tip",
            "socket_wing_r_tip",
            "socket_tail_base",
            "socket_tail_mid",
            "socket_tail_stinger",
            "socket_vfx_venom_drip",
            "socket_vfx_landing_dust",
            "socket_back_variant",
        ],
    ),
    (
        "/Game/Aerathea/Characters/Ogres/Shaman/SK_OGR_Shaman_A01",
        [
            "hand_r_weapon",
            "hand_l_offhand",
            "hand_r_twohand_grip",
            "hand_l_twohand_grip",
            "back_large_weapon",
            "back_shield",
            "vfx_mouth",
            "vfx_stomp_ground",
            "vfx_staff_head",
            "vfx_rune_wheel",
            "vfx_totem_chest",
            "weapon_staff_r",
            "head_fx",
        ],
    ),
    (
        "/Game/Aerathea/Characters/Ogres/Necromancer/SK_OGR_Necromancer_A01",
        [
            "hand_r_weapon",
            "hand_l_offhand",
            "hand_r_twohand_grip",
            "hand_l_twohand_grip",
            "back_large_weapon",
            "back_shield",
            "vfx_mouth",
            "vfx_stomp_ground",
            "vfx_lantern_core",
            "vfx_chest_necro",
            "vfx_bracer_l",
            "vfx_bracer_r",
            "weapon_staff_r",
            "head_fx",
        ],
    ),
    (
        "/Game/Aerathea/Creatures/Abyss/Troops/BlackPikeTrooper/SK_ABY_BlackPikeTrooper_A01",
        [
            "socket_weapon_r",
            "socket_weapon_l",
            "socket_pike_tip",
            "socket_head_vfx",
            "socket_eye_l",
            "socket_eye_r",
            "socket_chest_core",
            "socket_banner_back",
            "socket_ground_rift",
            "socket_hit_trace_pike",
        ],
    ),
    (
        "/Game/Aerathea/Characters/Gnomes/Iona/Mek/SK_GNM_IonaSiegebreakerMek_A01",
        [
            "socket_pilot_harness",
            "socket_cannon_l_mount",
            "socket_cannon_r_mount",
            "socket_cannon_l_muzzle",
            "socket_cannon_r_muzzle",
            "socket_core_chest",
            "socket_core_back",
            "socket_hand_l",
            "socket_hand_r",
            "socket_foot_l",
            "socket_foot_r",
            "socket_vent_l",
            "socket_vent_r",
            "socket_camera_focus",
            "vfx_arc_l",
            "vfx_arc_r",
        ],
    ),
    (
        "/Game/Aerathea/Characters/Infernals/Mage/SK_INF_Mage_A01",
        [
            "hand_l_claw",
            "hand_r_claw",
            "hand_l_cast",
            "hand_r_cast",
            "vfx_hand_l",
            "vfx_hand_r",
            "vfx_eye_l",
            "vfx_eye_r",
            "vfx_brand_chest",
            "vfx_brand_forearm_l",
            "vfx_brand_forearm_r",
            "vfx_wing_root_l",
            "vfx_wing_root_r",
            "wing_l_tip",
            "wing_r_tip",
            "tail_tip",
            "vfx_tail_tip",
            "vfx_regen_core",
            "vfx_sorcerer_focus",
            "vfx_worthiness_mark",
            "vfx_mouth",
        ],
    ),
    (
        "/Game/Aerathea/Characters/Infernals/Warrior/SK_INF_Warrior_A01",
        [
            "hand_l_claw",
            "hand_r_claw",
            "hand_l_cast",
            "hand_r_cast",
            "vfx_hand_l",
            "vfx_hand_r",
            "vfx_eye_l",
            "vfx_eye_r",
            "vfx_brand_chest",
            "vfx_brand_forearm_l",
            "vfx_brand_forearm_r",
            "vfx_wing_root_l",
            "vfx_wing_root_r",
            "wing_l_tip",
            "wing_r_tip",
            "tail_tip",
            "vfx_tail_tip",
            "vfx_regen_core",
            "vfx_mouth",
            "vfx_rage_core",
            "tail_sweep_trace",
            "wing_buffet_trace",
            "body_check_trace",
        ],
    ),
    (
        "/Game/Aerathea/Characters/Infernals/Rogue/SK_INF_Rogue_A01",
        [
            "hand_l_claw",
            "hand_r_claw",
            "hand_l_cast",
            "hand_r_cast",
            "vfx_hand_l",
            "vfx_hand_r",
            "vfx_eye_l",
            "vfx_eye_r",
            "vfx_brand_chest",
            "vfx_brand_forearm_l",
            "vfx_brand_forearm_r",
            "vfx_wing_root_l",
            "vfx_wing_root_r",
            "wing_l_tip",
            "wing_r_tip",
            "tail_tip",
            "vfx_tail_tip",
            "vfx_regen_core",
            "vfx_mouth",
            "vfx_ambush_mark",
            "vfx_invisible_sight_focus",
            "pounce_trace",
            "claw_rake_trace",
            "tail_balance_trace",
            "crouch_center",
        ],
    ),
    (
        "/Game/Aerathea/Characters/Infernals/Hunter/SK_INF_Hunter_A01",
        [
            "hand_l_claw",
            "hand_r_claw",
            "hand_l_cast",
            "hand_r_cast",
            "vfx_hand_l",
            "vfx_hand_r",
            "vfx_eye_l",
            "vfx_eye_r",
            "vfx_brand_chest",
            "vfx_brand_forearm_l",
            "vfx_brand_forearm_r",
            "vfx_wing_root_l",
            "vfx_wing_root_r",
            "wing_l_tip",
            "wing_r_tip",
            "tail_tip",
            "vfx_tail_tip",
            "vfx_regen_core",
            "vfx_mouth",
            "vfx_target_mark",
            "vfx_brow_sight",
            "vfx_pursuit_burst",
            "pounce_trace",
            "claw_takedown_trace",
            "tail_balance_trace",
            "tracking_center",
            "wing_burst_trace",
        ],
    ),
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
    "AET_PROD_MKG_MultiTool_A01",
    "AET_PROD_MKG_GrappleHook_A01",
    "AET_PROD_GNM_HeavyMekShieldwall_A01",
    "AET_PROD_MKG_SpikeDrill_A01",
    "AET_PROD_MKG_MonkeyWrench_A01",
    "AET_PROD_MKG_RatchetCleaver_A01",
    "AET_PROD_MKG_GearMace_A01",
    "AET_PROD_GnomeBase_A01",
    "AET_PROD_MKG_ToolPack_BackFit_A01",
    "AET_PROD_CRE_Gryphon_A01",
    "AET_PROD_GiantMaleBase_A01",
    "AET_PROD_GiantFemaleBase_A01",
    "AET_PROD_Palisade_Wall_A01",
    "AET_PROD_Palisade_Post_A01",
    "AET_PROD_Palisade_EndCap_A01",
    "AET_PROD_Palisade_Corner_A01",
    "AET_PROD_Palisade_Gate_A01",
    "AET_PROD_INF_CullingTrialFloor_A01",
    "AET_PROD_INF_HornWingArch_A01",
    "AET_PROD_INF_WorthinessAltar_A01",
    "AET_PROD_OgreTeknomancer_A01",
    "AET_PROD_OgreWarrior_Rival_A01",
    "AET_PROD_OGR_CairnBattleGate_A01",
    "AET_PROD_GNM_HeavyMek_Rivalry_A01",
    "AET_PROD_OGR_CrudeTekPylon_A01",
    "AET_PROD_CRE_Manticore_A01",
    "AET_PROD_CRE_Manticore_Interrupt_A01",
    "AET_PROD_OgreShaman_A01",
    "AET_PROD_OgreNecromancer_A01",
    "AET_PROD_ABY_BlackPikeTrooper_A01",
    "AET_PROD_GNM_IonaSiegebreakerMek_A01",
    "AET_PROD_INF_Mage_A01",
    "AET_PROD_INF_Warrior_A01",
    "AET_PROD_INF_Rogue_A01",
    "AET_PROD_INF_Hunter_A01",
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
EXPECTED_BOUNDS_LIMITS = {
    "AET_PROD_GroundTile_A01_R3_C3": {
        "extent_min": unreal.Vector(150.0, 150.0, 1.0),
        "extent_max": unreal.Vector(250.0, 250.0, 20.0),
        "radius_max": 360.0,
    },
    "AET_PROD_Portal_A01": {
        "extent_min": unreal.Vector(590.0, 120.0, 620.0),
        "radius_max": 1250.0,
    },
    "AET_PROD_TargetDummy_A01": {"radius_max": 350.0},
    "AET_PROD_WorkshopCrate_A01": {"radius_max": 250.0},
    "AET_PROD_MKG_GrappleHook_A01": {"radius_max": 180.0},
    "AET_PROD_GNM_HeavyMekShieldwall_A01": {
        "extent_min": unreal.Vector(40.0, 280.0, 120.0),
        "radius_max": 760.0,
    },
    "AET_PROD_GnomeBase_A01": {"radius_max": 250.0},
    "AET_PROD_CRE_Gryphon_A01": {"radius_max": 600.0},
    "AET_PROD_GiantMaleBase_A01": {
        "extent_min": unreal.Vector(45.0, 45.0, 180.0),
        "radius_max": 700.0,
    },
    "AET_PROD_GiantFemaleBase_A01": {
        "extent_min": unreal.Vector(40.0, 40.0, 155.0),
        "radius_max": 650.0,
    },
    "AET_PROD_Palisade_Gate_A01": {"radius_max": 800.0},
    "AET_PROD_INF_CullingTrialFloor_A01": {
        "extent_min": unreal.Vector(390.0, 390.0, 8.0),
        "radius_max": 720.0,
    },
    "AET_PROD_INF_HornWingArch_A01": {
        "extent_min": unreal.Vector(300.0, 90.0, 250.0),
        "radius_max": 760.0,
    },
    "AET_PROD_INF_WorthinessAltar_A01": {
        "extent_min": unreal.Vector(145.0, 80.0, 125.0),
        "radius_max": 550.0,
    },
    "AET_PROD_OgreTeknomancer_A01": {
        "extent_min": unreal.Vector(45.0, 45.0, 140.0),
        "radius_max": 700.0,
    },
    "AET_PROD_OgreWarrior_Rival_A01": {
        "extent_min": unreal.Vector(45.0, 45.0, 140.0),
        "radius_max": 760.0,
    },
    "AET_PROD_OGR_CairnBattleGate_A01": {
        "extent_min": unreal.Vector(430.0, 80.0, 260.0),
        "radius_max": 1450.0,
    },
    "AET_PROD_GNM_HeavyMek_Rivalry_A01": {
        "extent_min": unreal.Vector(45.0, 45.0, 140.0),
        "radius_max": 760.0,
    },
    "AET_PROD_OGR_CrudeTekPylon_A01": {
        "extent_min": unreal.Vector(60.0, 60.0, 190.0),
        "radius_max": 650.0,
    },
    "AET_PROD_CRE_Manticore_A01": {
        "extent_min": unreal.Vector(170.0, 170.0, 150.0),
        "radius_max": 920.0,
    },
    "AET_PROD_CRE_Manticore_Interrupt_A01": {
        "extent_min": unreal.Vector(170.0, 170.0, 150.0),
        "radius_max": 920.0,
    },
    "AET_PROD_OgreShaman_A01": {
        "extent_min": unreal.Vector(45.0, 45.0, 140.0),
        "radius_max": 780.0,
    },
    "AET_PROD_OgreNecromancer_A01": {
        "extent_min": unreal.Vector(45.0, 45.0, 140.0),
        "radius_max": 780.0,
    },
    "AET_PROD_ABY_BlackPikeTrooper_A01": {
        "extent_min": unreal.Vector(35.0, 35.0, 95.0),
        "radius_max": 520.0,
    },
    "AET_PROD_GNM_IonaSiegebreakerMek_A01": {
        "extent_min": unreal.Vector(80.0, 120.0, 185.0),
        "radius_max": 820.0,
    },
    "AET_PROD_INF_Mage_A01": {
        "extent_min": unreal.Vector(35.0, 35.0, 95.0),
        "radius_max": 560.0,
    },
    "AET_PROD_INF_Warrior_A01": {
        "extent_min": unreal.Vector(45.0, 45.0, 115.0),
        "radius_max": 720.0,
    },
    "AET_PROD_INF_Rogue_A01": {
        "extent_min": unreal.Vector(25.0, 25.0, 75.0),
        "radius_max": 500.0,
    },
    "AET_PROD_INF_Hunter_A01": {
        "extent_min": unreal.Vector(35.0, 35.0, 95.0),
        "radius_max": 650.0,
    },
}
REVIEW_CAMERA_ROTATION_TOLERANCE_DEGREES = 2.0
KEY_DIRECTIONAL_LIGHT_LABEL = "AET_BOOT_KeyLight_Directional"
EXPECTED_MOVABLE_LIGHT_LABELS = [
    "AET_BOOT_KeyLight_Directional",
    "AET_BOOT_SkyLight",
    "AET_PROD_ReviewFillLight_A01",
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


def asset_path_without_object(asset):
    return asset.get_path_name().split(".", 1)[0]


def skeletal_mesh_skeleton(mesh):
    skeleton = try_call(mesh, "get_skeleton")
    if skeleton is not None:
        return skeleton
    try:
        return mesh.get_editor_property("skeleton")
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


def component_hidden_or_invisible(component, actor_label=None):
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
    hidden_runtime_helpers = {
        "HitVolume",
        "InteractionVolume",
        "ShieldCollision",
    }
    hidden_runtime_helper_classes = {
        "BoxComponent",
        "CapsuleComponent",
        "SphereComponent",
    }
    if component_name in hidden_runtime_helpers and component_class_name in hidden_runtime_helper_classes:
        return False
    optional_shieldwall_components = {
        "Projector_04",
        "Projector_05",
        "ShieldPanel_03",
        "ShieldPanel_04",
        "ShieldNiagara",
    }
    if actor_label == "AET_PROD_GNM_HeavyMekShieldwall_A01" and component_name in optional_shieldwall_components:
        return False
    optional_pylon_components = {
        "PylonNiagara",
    }
    if actor_label == "AET_PROD_OGR_CrudeTekPylon_A01" and component_name in optional_pylon_components:
        return False
    optional_manticore_interrupt_components = {
        "ImpactNiagara",
    }
    if actor_label == "AET_PROD_CRE_Manticore_Interrupt_A01" and component_name in optional_manticore_interrupt_components:
        return False
    optional_ritual_altar_components = {
        "InteractionVolume",
        "WorthinessNiagara",
    }
    if actor_label == "AET_PROD_INF_WorthinessAltar_A01" and component_name in optional_ritual_altar_components:
        return False
    hidden = try_call(component, "is_hidden_in_game")
    visible = try_call(component, "is_visible")
    return bool(hidden) or visible is False


def vector_distance(a, b):
    return math.sqrt(((a.x - b.x) ** 2) + ((a.y - b.y) ** 2) + ((a.z - b.z) ** 2))


def vector_radius(vector):
    return math.sqrt((vector.x * vector.x) + (vector.y * vector.y) + (vector.z * vector.z))


def angle_delta_degrees(a, b):
    return abs((a - b + 180.0) % 360.0 - 180.0)


def log_camera_aim(camera_actor):
    location = camera_actor.get_actor_location()
    rotation = camera_actor.get_actor_rotation()
    target = REVIEW_CAMERA_TARGET
    location_error = vector_distance(location, REVIEW_CAMERA_LOCATION)
    if location_error > 1.0:
        raise RuntimeError("Review camera location mismatch: {:.2f} cm".format(location_error))
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
    pitch_error = angle_delta_degrees(rotation.pitch, expected_pitch)
    yaw_error = angle_delta_degrees(rotation.yaw, expected_yaw)
    if pitch_error > REVIEW_CAMERA_ROTATION_TOLERANCE_DEGREES or yaw_error > REVIEW_CAMERA_ROTATION_TOLERANCE_DEGREES:
        raise RuntimeError(
            "Review camera aim mismatch: pitch error {:.2f} deg, yaw error {:.2f} deg".format(
                pitch_error,
                yaw_error,
            )
        )


def validate_actor_bounds(actors_by_label):
    failures = []
    for label, limits in EXPECTED_BOUNDS_LIMITS.items():
        actor = actors_by_label.get(label)
        if actor is None:
            continue
        _origin, extent = actor.get_actor_bounds(False)
        radius = vector_radius(extent)
        extent_min = limits.get("extent_min")
        if extent_min is not None and (
            extent.x < extent_min.x or extent.y < extent_min.y or extent.z < extent_min.z
        ):
            failures.append("{} bounds extent {} is below expected {}".format(label, extent, extent_min))
        extent_max = limits.get("extent_max")
        if extent_max is not None and (
            extent.x > extent_max.x or extent.y > extent_max.y or extent.z > extent_max.z
        ):
            failures.append("{} bounds extent {} exceeds expected {}".format(label, extent, extent_max))
        radius_max = limits.get("radius_max")
        if radius_max is not None and radius > radius_max:
            failures.append("{} bounds radius {:.2f} cm exceeds {:.2f} cm".format(label, radius, radius_max))
    if failures:
        raise RuntimeError("Startup actor bounds validation failed: {}".format("; ".join(failures)))


def get_forward_shading_priority(component):
    for prop in ("forward_shading_priority", "ForwardShadingPriority"):
        try:
            return int(component.get_editor_property(prop))
        except Exception:
            pass
    return None


def validate_directional_light_priority(actors):
    failures = []
    winning_labels = []
    for actor in actors:
        component = actor.get_component_by_class(unreal.DirectionalLightComponent)
        if component is None:
            continue
        priority = get_forward_shading_priority(component)
        if actor.get_actor_label() == KEY_DIRECTIONAL_LIGHT_LABEL:
            if priority != 1:
                failures.append("{} ForwardShadingPriority is {}, expected 1".format(KEY_DIRECTIONAL_LIGHT_LABEL, priority))
            winning_labels.append(actor.get_actor_label())
        elif priority not in (None, 0):
            failures.append("{} ForwardShadingPriority is {}, expected 0".format(actor.get_actor_label(), priority))
    if KEY_DIRECTIONAL_LIGHT_LABEL not in winning_labels:
        failures.append("Missing key directional light {}".format(KEY_DIRECTIONAL_LIGHT_LABEL))
    if failures:
        raise RuntimeError("Directional light priority validation failed: {}".format("; ".join(failures)))


def get_light_component(actor):
    light_component_base = getattr(unreal, "LightComponentBase", None)
    if light_component_base is not None:
        component = actor.get_component_by_class(light_component_base)
        if component is not None:
            return component
    for class_name in (
        "DirectionalLightComponent",
        "SkyLightComponent",
        "PointLightComponent",
        "SpotLightComponent",
        "RectLightComponent",
    ):
        component_class = getattr(unreal, class_name, None)
        if component_class is None:
            continue
        component = actor.get_component_by_class(component_class)
        if component is not None:
            return component
    return None


def mobility_name(value):
    if value is None:
        return "None"
    text = str(value)
    return text.rsplit(".", 1)[-1]


def validate_review_light_mobility(actors_by_label):
    expected = unreal.ComponentMobility.MOVABLE
    failures = []
    for label in EXPECTED_MOVABLE_LIGHT_LABELS:
        actor = actors_by_label.get(label)
        if actor is None:
            failures.append("missing {}".format(label))
            continue
        component = get_light_component(actor)
        if component is None:
            failures.append("{} has no light component".format(label))
            continue
        try:
            mobility = component.get_editor_property("mobility")
        except Exception:
            mobility = None
        if mobility != expected:
            failures.append("{} mobility is {}, expected MOVABLE".format(label, mobility_name(mobility)))
    if failures:
        raise RuntimeError("Review light mobility validation failed: {}".format("; ".join(failures)))


def component_by_name(actor, component_class, expected_name):
    for component in actor.get_components_by_class(component_class):
        name = component.get_name()
        if name == expected_name or name.startswith("{}_".format(expected_name)):
            return component
    return None


def material_matches_expected(material, expected_path):
    if material is None:
        return False
    if asset_path_without_object(material) == expected_path:
        return True
    expected_name = expected_path.rsplit("/", 1)[-1]
    material_name = material.get_name()
    return expected_name in material_name


def validate_shieldwall_vfx_contract(shieldwall_actor):
    failures = []
    ranged_properties = {
        "ImpactIntensity": (0.0, 1.0),
        "OverloadPercent": (0.0, 1.0),
        "ImpactLocationNormalized": (-1.0, 1.0),
    }
    for prop_name, (min_value, max_value) in ranged_properties.items():
        try:
            value = float(shieldwall_actor.get_editor_property(prop_name))
        except Exception as exc:
            failures.append("missing property {} ({})".format(prop_name, exc))
            continue
        if value < min_value or value > max_value:
            failures.append("{} value {:.2f} is outside {:.2f}-{:.2f}".format(prop_name, value, min_value, max_value))

    expected_materials = {
        "ShieldIdleMaterial": "/Game/Aerathea/Materials/Instances/MI_GNM_AetherShieldWall_A01_Idle",
        "ShieldImpactMaterial": "/Game/Aerathea/Materials/Instances/MI_GNM_AetherShieldWall_A01_Impact",
        "ShieldFailingMaterial": "/Game/Aerathea/Materials/Instances/MI_GNM_AetherShieldWall_A01_Failing",
    }
    for prop_name, expected_path in expected_materials.items():
        try:
            material = shieldwall_actor.get_editor_property(prop_name)
        except Exception as exc:
            failures.append("missing property {} ({})".format(prop_name, exc))
            continue
        if material is None:
            failures.append("{} is not assigned".format(prop_name))
        elif not material_matches_expected(material, expected_path):
            failures.append("{} is {}, expected {}".format(prop_name, material.get_path_name(), expected_path))

    active_panel = component_by_name(shieldwall_actor, unreal.StaticMeshComponent, "ShieldPanel_01")
    if active_panel is None:
        failures.append("missing ShieldPanel_01 component")
    else:
        material = active_panel.get_material(0)
        expected_idle = expected_materials["ShieldIdleMaterial"]
        if material is None:
            failures.append("ShieldPanel_01 has no material")
        elif not material_matches_expected(material, expected_idle):
            failures.append("ShieldPanel_01 material is {}, expected {}".format(material.get_path_name(), expected_idle))

    try:
        shield_system = shieldwall_actor.get_editor_property("ShieldNiagaraSystem")
    except Exception as exc:
        failures.append("missing ShieldNiagaraSystem ({})".format(exc))
        shield_system = None
    expected_system = "/Game/Aerathea/VFX/GnomeOgre/NS_GNM_AetherShieldWall_A01"
    if shield_system is None:
        failures.append("ShieldNiagaraSystem is not assigned")
    elif asset_path_without_object(shield_system) != expected_system:
        failures.append("ShieldNiagaraSystem is {}, expected {}".format(shield_system.get_path_name(), expected_system))

    if failures:
        raise RuntimeError("Shieldwall VFX contract validation failed: {}".format("; ".join(failures)))


def static_mesh_component_mesh(component):
    mesh = try_call(component, "get_static_mesh")
    if mesh is not None:
        return mesh
    try:
        return component.get_editor_property("static_mesh")
    except Exception:
        return None


def skeletal_mesh_component_mesh(component):
    for method_name in ("get_skeletal_mesh_asset", "get_skeletal_mesh"):
        mesh = try_call(component, method_name)
        if mesh is not None:
            return mesh
    for prop_name in ("skeletal_mesh_asset", "skeletal_mesh"):
        try:
            mesh = component.get_editor_property(prop_name)
            if mesh is not None:
                return mesh
        except Exception:
            continue
    return None


def validate_pylon_contract(pylon_actor):
    failures = []
    class_name = pylon_actor.get_class().get_name()
    if "BP_OGR_CrudeTekPylon_A01" not in class_name and "AETCrudeTekPylonActor" not in class_name:
        failures.append("unexpected class {}".format(class_name))

    ranged_properties = {
        "OverloadPercent": (0.0, 1.0),
        "DamagePercent": (0.0, 1.0),
        "DamageWindowSeconds": (0.05, 60.0),
        "RepairWindowSeconds": (0.05, 60.0),
        "DamageTraceRadiusCm": (0.0, 1000.0),
        "RepairTraceRadiusCm": (0.0, 1000.0),
        "DamagePerTrace": (0.0, 1.0),
        "RepairPerTrace": (0.0, 1.0),
    }
    for prop_name, (min_value, max_value) in ranged_properties.items():
        try:
            value = float(pylon_actor.get_editor_property(prop_name))
        except Exception as exc:
            failures.append("missing property {} ({})".format(prop_name, exc))
            continue
        if value < min_value or value > max_value:
            failures.append("{} value {:.2f} is outside {:.2f}-{:.2f}".format(prop_name, value, min_value, max_value))

    mesh_component = component_by_name(pylon_actor, unreal.StaticMeshComponent, "PylonMesh")
    if mesh_component is None:
        failures.append("missing PylonMesh component")
    else:
        mesh = static_mesh_component_mesh(mesh_component)
        expected_path = "/Game/Aerathea/Props/Ogres/Teknomancy/SM_OGR_CrudeTekPylon_A01"
        if mesh is None:
            failures.append("PylonMesh has no static mesh")
        elif asset_path_without_object(mesh) != expected_path:
            failures.append("PylonMesh uses {}, expected {}".format(mesh.get_path_name(), expected_path))

    try:
        pylon_system = pylon_actor.get_editor_property("PylonNiagaraSystem")
    except Exception as exc:
        failures.append("missing PylonNiagaraSystem ({})".format(exc))
        pylon_system = None
    expected_system = "/Game/Aerathea/VFX/Ogres/NS_OGR_CrudeTekPylon_A01"
    if pylon_system is None:
        failures.append("PylonNiagaraSystem is not assigned")
    elif asset_path_without_object(pylon_system) != expected_system:
        failures.append("PylonNiagaraSystem is {}, expected {}".format(pylon_system.get_path_name(), expected_system))

    niagara_component = component_by_name(pylon_actor, unreal.NiagaraComponent, "PylonNiagara")
    if niagara_component is None:
        failures.append("missing PylonNiagara component")
    else:
        asset = try_call(niagara_component, "get_asset")
        if asset is not None and asset_path_without_object(asset) != expected_system:
            failures.append("PylonNiagara uses {}, expected {}".format(asset.get_path_name(), expected_system))

    if failures:
        raise RuntimeError("Crude Tek pylon contract validation failed: {}".format("; ".join(failures)))


def validate_ritual_altar_contract(altar_actor):
    failures = []
    class_name = altar_actor.get_class().get_name()
    if "BP_INF_RitualAltar_A01" not in class_name and "AETInfernalRitualAltarActor" not in class_name:
        failures.append("unexpected class {}".format(class_name))

    ranged_properties = {
        "TrialProgress": (0.0, 1.0),
        "JudgmentIntensity": (0.0, 1.0),
        "RejectedSeverity": (0.0, 1.0),
        "TrialDurationSeconds": (0.05, 60.0),
        "JudgmentPulseSeconds": (0.05, 10.0),
        "CooldownSeconds": (0.05, 30.0),
        "InteractionRadiusCm": (0.0, 1000.0),
        "InteractionDepthCm": (0.0, 1000.0),
    }
    for prop_name, (min_value, max_value) in ranged_properties.items():
        try:
            value = float(altar_actor.get_editor_property(prop_name))
        except Exception as exc:
            failures.append("missing property {} ({})".format(prop_name, exc))
            continue
        if value < min_value or value > max_value:
            failures.append("{} value {:.2f} is outside {:.2f}-{:.2f}".format(prop_name, value, min_value, max_value))

    try:
        slot_index = int(altar_actor.get_editor_property("BrandGlowMaterialSlotIndex"))
        if slot_index != 4:
            failures.append("BrandGlowMaterialSlotIndex is {}, expected 4".format(slot_index))
    except Exception as exc:
        failures.append("missing BrandGlowMaterialSlotIndex ({})".format(exc))

    expected_materials = {
        "BrandGlowInactiveMaterial": "/Game/Aerathea/Materials/Instances/MI_INF_BrandGlowStates_A01_Inactive",
        "BrandGlowSmolderMaterial": "/Game/Aerathea/Materials/Instances/MI_INF_BrandGlowStates_A01_Smolder",
        "BrandGlowTrialActiveMaterial": "/Game/Aerathea/Materials/Instances/MI_INF_BrandGlowStates_A01_TrialActive",
        "BrandGlowAcceptedMaterial": "/Game/Aerathea/Materials/Instances/MI_INF_BrandGlowStates_A01_Accepted",
        "BrandGlowRejectedMaterial": "/Game/Aerathea/Materials/Instances/MI_INF_BrandGlowStates_A01_Rejected",
        "BrandGlowJudgmentPulseMaterial": "/Game/Aerathea/Materials/Instances/MI_INF_BrandGlowStates_A01_SorcererFocus",
    }
    for prop_name, expected_path in expected_materials.items():
        try:
            material = altar_actor.get_editor_property(prop_name)
        except Exception as exc:
            failures.append("missing material property {} ({})".format(prop_name, exc))
            continue
        if material is None:
            failures.append("{} is not assigned".format(prop_name))
        elif not material_matches_expected(material, expected_path):
            failures.append("{} is {}, expected {}".format(prop_name, material.get_path_name(), expected_path))

    expected_niagara = {
        "InactiveNiagaraSystem": "/Game/Aerathea/VFX/Infernals/WorthinessJudgment/NS_INF_Worthiness_Inactive_A01",
        "SmolderNiagaraSystem": "/Game/Aerathea/VFX/Infernals/WorthinessJudgment/NS_INF_Worthiness_Smolder_A01",
        "TrialActiveNiagaraSystem": "/Game/Aerathea/VFX/Infernals/WorthinessJudgment/NS_INF_Worthiness_TrialActive_A01",
        "AcceptedNiagaraSystem": "/Game/Aerathea/VFX/Infernals/WorthinessJudgment/NS_INF_Worthiness_Accepted_A01",
        "RejectedNiagaraSystem": "/Game/Aerathea/VFX/Infernals/WorthinessJudgment/NS_INF_Worthiness_Rejected_A01",
        "JudgmentPulseNiagaraSystem": "/Game/Aerathea/VFX/Infernals/WorthinessJudgment/NS_INF_Worthiness_JudgmentPulse_A01",
    }
    for prop_name, expected_path in expected_niagara.items():
        try:
            system = altar_actor.get_editor_property(prop_name)
        except Exception as exc:
            failures.append("missing Niagara property {} ({})".format(prop_name, exc))
            continue
        if system is None:
            failures.append("{} is not assigned".format(prop_name))
        elif asset_path_without_object(system) != expected_path:
            failures.append("{} is {}, expected {}".format(prop_name, system.get_path_name(), expected_path))

    required_locators = [
        "InteractFrontLocator",
        "AltarCoreLocator",
        "SacrificeMarkLocator",
        "BrandTransferLocator",
        "RingLinkLocator",
        "RejectedGapLocator",
    ]
    for locator_name in required_locators:
        if component_by_name(altar_actor, unreal.SceneComponent, locator_name) is None:
            failures.append("missing {} component".format(locator_name))

    if component_by_name(altar_actor, unreal.BoxComponent, "InteractionVolume") is None:
        failures.append("missing InteractionVolume component")

    mesh_component = component_by_name(altar_actor, unreal.StaticMeshComponent, "AltarMesh")
    if mesh_component is None:
        failures.append("missing AltarMesh component")
    else:
        mesh = static_mesh_component_mesh(mesh_component)
        expected_path = "/Game/Aerathea/Props/Infernals/BalgorothCult/SM_INF_WorthinessAltar_A01"
        if mesh is None:
            failures.append("AltarMesh has no static mesh")
        elif asset_path_without_object(mesh) != expected_path:
            failures.append("AltarMesh uses {}, expected {}".format(mesh.get_path_name(), expected_path))
        state_material = mesh_component.get_material(4)
        if state_material is None:
            failures.append("AltarMesh slot 4 is unassigned")
        elif not any(material_matches_expected(state_material, expected_path) for expected_path in expected_materials.values()):
            failures.append("AltarMesh slot 4 uses {}, expected BrandGlow state material".format(state_material.get_path_name()))

    niagara_component = component_by_name(altar_actor, unreal.NiagaraComponent, "WorthinessNiagara")
    if niagara_component is None:
        failures.append("missing WorthinessNiagara component")
    else:
        asset = try_call(niagara_component, "get_asset")
        if asset is not None and asset_path_without_object(asset) not in set(expected_niagara.values()):
            failures.append("WorthinessNiagara uses {}, expected WorthinessJudgment system".format(asset.get_path_name()))

    if failures:
        raise RuntimeError("Infernal ritual altar contract validation failed: {}".format("; ".join(failures)))


def validate_manticore_interrupt_contract(manticore_actor):
    failures = []
    class_name = manticore_actor.get_class().get_name()
    if "BP_CRE_ManticoreInterrupt_A01" not in class_name and "AETManticoreInterruptActor" not in class_name:
        failures.append("unexpected class {}".format(class_name))

    try:
        progress = float(manticore_actor.get_editor_property("SequenceProgress"))
        if progress < 0.0 or progress > 1.0:
            failures.append("SequenceProgress value {:.2f} is outside 0.0-1.0".format(progress))
    except Exception as exc:
        failures.append("missing SequenceProgress ({})".format(exc))

    ranged_properties = {
        "StalkSeconds": (0.05, 20.0),
        "TelegraphSeconds": (0.05, 20.0),
        "ImpactSeconds": (0.05, 20.0),
        "ThreatHoldSeconds": (0.05, 20.0),
        "RetreatSeconds": (0.05, 20.0),
        "InterruptTraceRadiusCm": (0.0, 1200.0),
        "ImpactDamageRadiusCm": (0.0, 1200.0),
    }
    for prop_name, (min_value, max_value) in ranged_properties.items():
        try:
            value = float(manticore_actor.get_editor_property(prop_name))
        except Exception as exc:
            failures.append("missing property {} ({})".format(prop_name, exc))
            continue
        if value < min_value or value > max_value:
            failures.append("{} value {:.2f} is outside {:.2f}-{:.2f}".format(prop_name, value, min_value, max_value))

    mesh_component = component_by_name(manticore_actor, unreal.SkeletalMeshComponent, "ManticoreMesh")
    if mesh_component is None:
        failures.append("missing ManticoreMesh component")
    else:
        mesh = skeletal_mesh_component_mesh(mesh_component)
        expected_path = "/Game/Aerathea/Creatures/Manticores/SK_CRE_Manticore_Interrupt_A01"
        if mesh is None:
            failures.append("ManticoreMesh has no skeletal mesh")
        elif asset_path_without_object(mesh) != expected_path:
            failures.append("ManticoreMesh uses {}, expected {}".format(mesh.get_path_name(), expected_path))

    try:
        impact_system = manticore_actor.get_editor_property("ImpactNiagaraSystem")
    except Exception as exc:
        failures.append("missing ImpactNiagaraSystem ({})".format(exc))
        impact_system = None
    expected_system = "/Game/Aerathea/VFX/Creatures/NS_CRE_Manticore_Impact_A01"
    if impact_system is None:
        failures.append("ImpactNiagaraSystem is not assigned")
    elif asset_path_without_object(impact_system) != expected_system:
        failures.append("ImpactNiagaraSystem is {}, expected {}".format(impact_system.get_path_name(), expected_system))

    niagara_component = component_by_name(manticore_actor, unreal.NiagaraComponent, "ImpactNiagara")
    if niagara_component is None:
        failures.append("missing ImpactNiagara component")
    else:
        asset = try_call(niagara_component, "get_asset")
        if asset is not None and asset_path_without_object(asset) != expected_system:
            failures.append("ImpactNiagara uses {}, expected {}".format(asset.get_path_name(), expected_system))

    if failures:
        raise RuntimeError("Manticore interrupt contract validation failed: {}".format("; ".join(failures)))


def validate_encounter_contract(encounter_actor, actors_by_label):
    failures = []
    class_name = encounter_actor.get_class().get_name()
    if "BP_GNM_OGR_BattlefieldEncounter_A01" not in class_name and "AETGnomeOgreBattlefieldEncounterActor" not in class_name:
        failures.append("unexpected class {}".format(class_name))

    expected_bools = {
        "bUsePlacedActors": True,
        "bEnablePylonObjective": True,
        "bEnableCasterReinforcements": True,
        "bEnableManticoreInterrupt": True,
        "bAutoStart": True,
        "bAutoAdvanceReviewPhases": True,
    }
    for prop_name, expected in expected_bools.items():
        try:
            value = bool(encounter_actor.get_editor_property(prop_name))
        except Exception as exc:
            failures.append("missing property {} ({})".format(prop_name, exc))
            continue
        if value != expected:
            failures.append("{} is {}, expected {}".format(prop_name, value, expected))

    try:
        phase_duration = float(encounter_actor.get_editor_property("ReviewPhaseDurationSeconds"))
        if phase_duration < 0.25 or phase_duration > 30.0:
            failures.append("ReviewPhaseDurationSeconds {:.2f} is outside 0.25-30.0".format(phase_duration))
    except Exception as exc:
        failures.append("missing ReviewPhaseDurationSeconds ({})".format(exc))

    expected_refs = {
        "ShieldwallActor": "AET_PROD_GNM_HeavyMekShieldwall_A01",
        "GnomeHeavyMekActor": "AET_PROD_GNM_HeavyMek_Rivalry_A01",
        "OgreTeknomancerActor": "AET_PROD_OgreTeknomancer_A01",
        "OgreWarriorActor": "AET_PROD_OgreWarrior_Rival_A01",
        "CairnGateActor": "AET_PROD_OGR_CairnBattleGate_A01",
        "PylonObjectiveActor": "AET_PROD_OGR_CrudeTekPylon_A01",
        "OgreShamanActor": "AET_PROD_OgreShaman_A01",
        "OgreNecromancerActor": "AET_PROD_OgreNecromancer_A01",
        "ManticoreInterruptActor": "AET_PROD_CRE_Manticore_Interrupt_A01",
    }
    for prop_name, label in expected_refs.items():
        target_actor = actors_by_label.get(label)
        try:
            value = encounter_actor.get_editor_property(prop_name)
        except Exception as exc:
            failures.append("missing reference {} ({})".format(prop_name, exc))
            continue
        if value is None:
            failures.append("{} is unassigned".format(prop_name))
        elif target_actor is not None and value.get_actor_label() != label:
            failures.append("{} points to {}, expected {}".format(prop_name, value.get_actor_label(), label))

    validate = getattr(encounter_actor, "validate_dependencies", None)
    if callable(validate):
        try:
            if not validate():
                failures.append("ValidateDependencies returned false: {}".format(encounter_actor.get_editor_property("LastValidationReport")))
        except Exception as exc:
            failures.append("ValidateDependencies raised {}".format(exc))

    if failures:
        raise RuntimeError("Gnome/Ogre encounter contract validation failed: {}".format("; ".join(failures)))


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
    validate_actor_bounds(actors_by_label)
    validate_directional_light_priority(actors)
    validate_review_light_mobility(actors_by_label)

    portal_actor = next(
        actor
        for actor in actors
        if actor.get_actor_label() == "AET_PROD_Portal_A01"
    )
    portal_class_name = portal_actor.get_class().get_name()
    if "BP_AET_Portal_A01" not in portal_class_name and "AETPortalActor" not in portal_class_name:
        raise RuntimeError("Portal actor has unexpected class: {}".format(portal_class_name))

    target_dummy_actor = actors_by_label["AET_PROD_TargetDummy_A01"]
    target_dummy_class_name = target_dummy_actor.get_class().get_name()
    if "BP_AET_TargetDummy_A01" not in target_dummy_class_name and "AETTargetDummyActor" not in target_dummy_class_name:
        raise RuntimeError("Target dummy actor has unexpected class: {}".format(target_dummy_class_name))

    shieldwall_actor = actors_by_label["AET_PROD_GNM_HeavyMekShieldwall_A01"]
    shieldwall_class_name = shieldwall_actor.get_class().get_name()
    if "BP_GNM_HeavyMekShieldwall_A01" not in shieldwall_class_name and "AETHeavyMekShieldwallActor" not in shieldwall_class_name:
        raise RuntimeError("Shieldwall actor has unexpected class: {}".format(shieldwall_class_name))
    validate_shieldwall_vfx_contract(shieldwall_actor)

    validate_pylon_contract(actors_by_label["AET_PROD_OGR_CrudeTekPylon_A01"])
    validate_ritual_altar_contract(actors_by_label["AET_PROD_INF_WorthinessAltar_A01"])
    validate_manticore_interrupt_contract(actors_by_label["AET_PROD_CRE_Manticore_Interrupt_A01"])
    validate_encounter_contract(actors_by_label["AET_PROD_GNM_OGR_BattlefieldEncounter_A01"], actors_by_label)

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

    skeletal_slot_failures = []
    for mesh_path, physics_asset_path, skeleton_path in EXPECTED_SKELETAL_MESHES:
        mesh = unreal.load_asset(mesh_path)
        if mesh is None:
            skeletal_slot_failures.append("{} failed to load".format(mesh_path))
            continue
        if len(mesh.get_editor_property("materials")) == 0:
            skeletal_slot_failures.append("{} has no material slots".format(mesh_path))
        skeleton = skeletal_mesh_skeleton(mesh)
        if skeleton is None:
            skeletal_slot_failures.append("{} has no assigned skeleton".format(mesh_path))
        elif asset_path_without_object(skeleton) != skeleton_path:
            skeletal_slot_failures.append(
                "{} has unexpected skeleton {}".format(mesh_path, skeleton.get_path_name())
            )
        physics_asset = mesh.get_editor_property("physics_asset")
        if physics_asset is None:
            skeletal_slot_failures.append("{} has no assigned physics asset".format(mesh_path))
        elif physics_asset.get_path_name().split(".", 1)[0] != physics_asset_path:
            skeletal_slot_failures.append(
                "{} has unexpected physics asset {}".format(mesh_path, physics_asset.get_path_name())
            )
    if skeletal_slot_failures:
        raise RuntimeError("Skeletal mesh validation failed: {}".format("; ".join(skeletal_slot_failures)))

    lod_failures = []
    for mesh_path in EXPECTED_LOD_STATIC_MESHES:
        mesh = unreal.load_asset(mesh_path)
        if mesh is None:
            lod_failures.append("{} failed to load".format(mesh_path))
            continue
        lod_count = unreal.EditorStaticMeshLibrary.get_lod_count(mesh)
        if lod_count < 4:
            lod_failures.append("{} has {} LODs, expected at least 4".format(mesh_path, lod_count))

    skeletal_subsystem = unreal.get_editor_subsystem(unreal.SkeletalMeshEditorSubsystem)
    for mesh_path, _physics_asset_path, _skeleton_path in EXPECTED_SKELETAL_MESHES:
        mesh = unreal.load_asset(mesh_path)
        if mesh is None:
            continue
        if skeletal_subsystem is None:
            lod_failures.append("SkeletalMeshEditorSubsystem unavailable for {}".format(mesh_path))
            continue
        lod_count = skeletal_subsystem.get_lod_count(mesh)
        if lod_count < 4:
            lod_failures.append("{} has {} LODs, expected at least 4".format(mesh_path, lod_count))
    if lod_failures:
        raise RuntimeError("LOD validation failed: {}".format("; ".join(lod_failures)))

    socket_failures = []
    for mesh_path, expected_socket_names in EXPECTED_STATIC_MESH_SOCKETS:
        mesh = unreal.load_asset(mesh_path)
        if mesh is None:
            socket_failures.append("{} failed to load".format(mesh_path))
            continue
        missing_sockets = [
            socket_name
            for socket_name in expected_socket_names
            if mesh.find_socket(unreal.Name(socket_name)) is None
        ]
        if missing_sockets:
            socket_failures.append("{} missing sockets {}".format(mesh_path, ", ".join(missing_sockets)))

    for mesh_path, expected_socket_names in EXPECTED_SKELETAL_MESH_SOCKETS:
        mesh = unreal.load_asset(mesh_path)
        if mesh is None:
            socket_failures.append("{} failed to load".format(mesh_path))
            continue
        socket_names = {
            str(mesh.get_socket_by_index(index).get_editor_property("socket_name"))
            for index in range(mesh.num_sockets())
        }
        missing_sockets = [
            socket_name
            for socket_name in expected_socket_names
            if socket_name not in socket_names
        ]
        if missing_sockets:
            socket_failures.append("{} missing sockets {}".format(mesh_path, ", ".join(missing_sockets)))
    if socket_failures:
        raise RuntimeError("Socket validation failed: {}".format("; ".join(socket_failures)))

    gnome_actor = actors_by_label["AET_PROD_GnomeBase_A01"]
    toolpack_actor = actors_by_label["AET_PROD_MKG_ToolPack_BackFit_A01"]
    gnome_component = gnome_actor.get_component_by_class(unreal.SkeletalMeshComponent)
    if gnome_component is None:
        raise RuntimeError("AET_PROD_GnomeBase_A01 has no SkeletalMeshComponent")
    if not gnome_component.does_socket_exist(unreal.Name("back_pack")):
        raise RuntimeError("AET_PROD_GnomeBase_A01 component missing back_pack socket")
    if unreal.Name("AET_SOCKET_FIT_PREVIEW") not in toolpack_actor.get_editor_property("tags"):
        raise RuntimeError("ToolPack fit actor is missing AET_SOCKET_FIT_PREVIEW tag")
    socket_location = gnome_component.get_socket_location(unreal.Name("back_pack"))
    toolpack_location = toolpack_actor.get_actor_location()
    fit_distance = vector_distance(socket_location, toolpack_location)
    if fit_distance > 2.0:
        raise RuntimeError(
            "ToolPack fit actor is {:.2f} cm from gnome back_pack socket".format(fit_distance)
        )

    runtime_visibility_failures = []
    for label in EXPECTED_RUNTIME_VISIBLE_LABELS:
        actor = actors_by_label.get(label)
        if actor is None:
            continue
        if is_actor_hidden_in_game(actor):
            runtime_visibility_failures.append("{} is hidden in game".format(label))
        primitive_components = actor.get_components_by_class(unreal.PrimitiveComponent)
        for component in primitive_components:
            if component_hidden_or_invisible(component, label):
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
