# Cross-Faction Armory DCC Readiness Matrix

## Scope

- Task: `AET-MA-20260629-047`
- Scope type: docs-only cross-faction DCC readiness matrix.
- Owned file: `docs/assets/kits/ARMORY_DCC_READINESS_MATRIX.md`
- Covered parent kits: `KIT_DWR_Armory_A01`, `KIT_ELV_Armory_A01`, `KIT_DEL_Armory_A01`, `KIT_ORC_Arsenal_A01`, `KIT_MIN_Arsenal_A01`, and `KIT_DKH_FieldGear_A01`.
- Excluded work: no DCC source creation, no FBX export, no Unreal import, no tool or validator authoring, no source concept copying, no per-package edits, no global index edits, and no final build-target selection.

This matrix converts already package-ready priority children into a shared readiness queue. It is a planning artifact only. A later implementation task must choose a build target and confirm scope before any source, export, Unreal, tool, or runtime work starts.

## Parent Kit Inputs

| Faction | Parent package | Priority children in scope | Readiness note |
| --- | --- | --- | --- |
| Dwarf | `docs/assets/kits/KIT_DWR_Armory_A01/PRODUCTION_PACKAGE.md` | `SM_DWR_OathkeeperHammer_A01`, `SM_DWR_StonewallShield_A01`, `SK_DWR_Helm_Stonebound_A01`, `MI_DWR_RunicGlowStates_A01` | Static weapon and shield are DCC-ready; helm fit waits on approved Dwarven base body/skeleton; material set is a dependency, not a mesh target. |
| Elf | `docs/assets/kits/KIT_ELV_Armory_A01/PRODUCTION_PACKAGE.md` | `SM_ELV_Moonblade_A01`, `SM_ELV_SilverleafRecurve_A01`, `SM_ELV_MoonwardBuckler_A01`, `SM_ELV_AetheriumLantern_A01` | Four static mesh props are DCC-ready; bow and lantern need socket/pivot confirmation during implementation. |
| Dark Elf | `docs/assets/kits/KIT_DEL_Armory_A01/PRODUCTION_PACKAGE.md` | `SM_DEL_DuskspiteBlade_A01`, `SM_DEL_VeilstriderBow_A01`, `SM_DEL_AegisOfEternalDusk_A01`, `MI_DEL_ShadowArmory_Set_A01` | Meshes are DCC-ready; shared material set should be authored or stubbed before final visual review. |
| Orc | `docs/assets/kits/KIT_ORC_Arsenal_A01/PRODUCTION_PACKAGE.md` | `SM_ORC_GreatAxe_A01`, `KIT_ORC_Shields_A01`, `KIT_ORC_ShamanicTalismans_A01`, `MI_ORC_RunicAffinities_A01` | Great axe is a single static mesh; shields and talismans are mini-kits requiring variant export manifests; material set is a dependency. |
| Minotaur | `docs/assets/kits/KIT_MIN_Arsenal_A01/PRODUCTION_PACKAGE.md` | `SM_MIN_GreatAxe_A01`, `SM_MIN_CrushingMaul_A01`, `KIT_MIN_HideShields_A01`, `KIT_MIN_Helmets_A01` | Weapons and hide shields are DCC-ready; helmets are fit-blocked on approved Minotaur body/skeleton. |
| Drakhar | `docs/assets/kits/KIT_DKH_FieldGear_A01/PRODUCTION_PACKAGE.md` | `SM_DKH_RiversindRecurve_A01`, `KIT_DKH_CurvedDaggers_A01`, `SM_DKH_ReedShellShield_A01`, `KIT_DKH_MagicTrackingCharms_A01` | DCC-ready only if approved A04 Drakhar scale is used; ignore the conflicting taller source-sheet scale. |

## Priority Queue

Priority does not select the final DCC build target. It ranks readiness and coordination cost for the lead to assign later.

| Queue | Asset or package | Type | Readiness | Why this position | Required gate before build |
| ---: | --- | --- | --- | --- | --- |
| 0 | `MI_DWR_RunicGlowStates_A01` | Material set | Dependency ready; no DCC mesh | Needed for Dwarf rune-bearing hammer, shield, and helm visual consistency. | Material task must be approved separately before Unreal authoring. |
| 0 | `MI_DEL_ShadowArmory_Set_A01` | Material set | Dependency ready; no DCC mesh | Prevents Dark Elf assets from drifting into unreadable black forms or inconsistent violet glow. | Material task must be approved separately before Unreal authoring. |
| 0 | `MI_ORC_RunicAffinities_A01` | Material set | Dependency ready; no DCC mesh | Defines blue-green spirit rune states for Orc axe, shields, and talismans. | Material task must be approved separately before Unreal authoring. |
| 1 | `SM_DWR_OathkeeperHammer_A01` | Static mesh weapon | Ready | Low-risk single prop; validates Dwarf dense steel/stone/brass/rune language. | Confirm one-handed grip pivot and rune-glow mask channel. |
| 2 | `SM_ELV_Moonblade_A01` | Static mesh weapon | Ready | Low-risk single prop; anchors Elven silver, moonstone, living whitewood, and restrained glow. | Confirm grip pivot and optional moonstone socket policy. |
| 3 | `SM_DEL_DuskspiteBlade_A01` | Static mesh weapon | Ready | Low-risk single prop after material language is locked; verifies crescent silhouette. | Confirm Dark Elf material dependency and violet glow socket policy. |
| 4 | `SM_ORC_GreatAxe_A01` | Static mesh weapon | Ready | Single heavy weapon; useful for Orc scale, grip, and disciplined clan material read. | Confirm two-handed grip pivot and spirit-rune mask policy. |
| 5 | `SM_MIN_GreatAxe_A01` | Static mesh weapon | Ready | Large simple weapon; validates Minotaur scale without emissive/material complexity. | Confirm approved Minotaur scale and two-handed grip pivot. |
| 6 | `SM_MIN_CrushingMaul_A01` | Static mesh weapon | Ready | Pairs with Minotaur axe to test blunt-head mass, LOD preservation, and no-magic material language. | Confirm impact socket is omitted unless VFX scope is approved. |
| 7 | `SM_DWR_StonewallShield_A01` | Static mesh shield | Ready | Adds Dwarf shield pivot, back strap, convex collision, and rune-channel constraints. | Confirm forearm strap pivot and simple collision bounds. |
| 8 | `SM_ELV_MoonwardBuckler_A01` | Static mesh shield | Ready | Small shield validates Elven light defensive silhouette with simple material cost. | Confirm back grip pivot and localized moonstone glow. |
| 9 | `SM_DEL_AegisOfEternalDusk_A01` | Static mesh shield | Ready | More complex crescent/cutout shield; depends on Dark Elf material readability. | Confirm cutout simplification and back grip pivot. |
| 10 | `SM_DKH_ReedShellShield_A01` | Static mesh shield | Ready with scale caution | Compact shield validates Drakhar A04 scale and reed/shell material language. | Confirm A04 scale markers and small forearm strap size. |
| 11 | `SM_ELV_AetheriumLantern_A01` | Static mesh prop | Ready | Tests lantern cage simplification, soft emissive core, and carry/hang pivot choice. | Choose bottom-center or handle-center pivot variant before DCC. |
| 12 | `SM_ELV_SilverleafRecurve_A01` | Static mesh bow | Ready with socket caution | Bow is ready but needs string and arrow-rest locator discipline. | Confirm `socket_arrow_rest`, `socket_string_top`, and `socket_string_bottom`. |
| 13 | `SM_DEL_VeilstriderBow_A01` | Static mesh bow | Ready with socket caution | Similar bow socket needs, plus Dark Elf crescent silhouette and material dependency. | Confirm bow sockets and optional violet-focus socket. |
| 14 | `SM_DKH_RiversindRecurve_A01` | Static mesh bow | Ready with scale and socket caution | Compact Drakhar bow combines A04 scale correction with bow-string locator needs. | Confirm A04 scale, clawed-hand grip size, and bow sockets. |
| 15 | `KIT_ORC_Shields_A01` | Shield mini-kit | Ready after variant split | Three variants require per-variant names, pivots, collisions, and export rows. | Approve variant export manifest before DCC. |
| 16 | `KIT_MIN_HideShields_A01` | Shield mini-kit | Ready after variant split | Three large variants validate Minotaur shield mass and simple raw-material language. | Approve variant export manifest and Minotaur forearm scale. |
| 17 | `KIT_DKH_CurvedDaggers_A01` | Weapon mini-kit | Ready after variant split | Small variants are efficient but need distinct hook/fang silhouettes and dual-wield pivots. | Approve per-dagger names, grip pivots, and A04 hand fit. |
| 18 | `KIT_ORC_ShamanicTalismans_A01` | Prop/accessory mini-kit | Ready after variant split | Charm clusters are lightweight but prone to noisy tiny geometry. | Approve cluster count, attachment pivots, and no-secondary-motion scope. |
| 19 | `KIT_DKH_MagicTrackingCharms_A01` | Prop/accessory mini-kit | Ready after variant split | Charm clusters need Volcreon-linked identity while avoiding dense trinket noise. | Approve cluster count, A04 attachment scale, and no-gameplay tracking behavior. |
| Hold | `SK_DWR_Helm_Stonebound_A01` | Armor module / skeletal or static helm | Package ready, fit-blocked | Package says DCC fit waits on approved Dwarven base body/skeleton. | Resume only after Dwarven base head/socket workflow is approved. |
| Hold | `KIT_MIN_Helmets_A01` | Armor mini-kit | Package ready, fit-blocked | Package says DCC fit waits on approved Minotaur base body/skeleton and horn shapes. | Resume only after Minotaur base body, horns, and head socket are approved. |

## Package Set

| Asset or package | Package path | Current package status |
| --- | --- | --- |
| `SM_DWR_OathkeeperHammer_A01` | `docs/assets/props/SM_DWR_OathkeeperHammer_A01/PRODUCTION_PACKAGE.md` | Production package ready; DCC build not started. |
| `SM_DWR_StonewallShield_A01` | `docs/assets/props/SM_DWR_StonewallShield_A01/PRODUCTION_PACKAGE.md` | Production package ready; DCC build not started. |
| `SK_DWR_Helm_Stonebound_A01` | `docs/assets/characters/SK_DWR_Helm_Stonebound_A01/PRODUCTION_PACKAGE.md` | Production package ready; DCC fit blocked on approved Dwarven base body/skeleton. |
| `MI_DWR_RunicGlowStates_A01` | `docs/assets/materials/MI_DWR_RunicGlowStates_A01/PRODUCTION_PACKAGE.md` | Production package ready; Unreal material authoring not started. |
| `SM_ELV_Moonblade_A01` | `docs/assets/props/SM_ELV_Moonblade_A01/PRODUCTION_PACKAGE.md` | Production package ready; DCC build not started. |
| `SM_ELV_SilverleafRecurve_A01` | `docs/assets/props/SM_ELV_SilverleafRecurve_A01/PRODUCTION_PACKAGE.md` | Production package ready; DCC build not started. |
| `SM_ELV_MoonwardBuckler_A01` | `docs/assets/props/SM_ELV_MoonwardBuckler_A01/PRODUCTION_PACKAGE.md` | Production package ready; DCC build not started. |
| `SM_ELV_AetheriumLantern_A01` | `docs/assets/props/SM_ELV_AetheriumLantern_A01/PRODUCTION_PACKAGE.md` | Production package ready; DCC build not started. |
| `SM_DEL_DuskspiteBlade_A01` | `docs/assets/props/SM_DEL_DuskspiteBlade_A01/PRODUCTION_PACKAGE.md` | Production package ready; DCC build not started. |
| `SM_DEL_VeilstriderBow_A01` | `docs/assets/props/SM_DEL_VeilstriderBow_A01/PRODUCTION_PACKAGE.md` | Production package ready; DCC build not started. |
| `SM_DEL_AegisOfEternalDusk_A01` | `docs/assets/props/SM_DEL_AegisOfEternalDusk_A01/PRODUCTION_PACKAGE.md` | Production package ready; DCC build not started. |
| `MI_DEL_ShadowArmory_Set_A01` | `docs/assets/materials/MI_DEL_ShadowArmory_Set_A01/PRODUCTION_PACKAGE.md` | Production package ready; Unreal material authoring not started. |
| `SM_ORC_GreatAxe_A01` | `docs/assets/props/SM_ORC_GreatAxe_A01/PRODUCTION_PACKAGE.md` | Production package ready; DCC build not started. |
| `KIT_ORC_Shields_A01` | `docs/assets/kits/KIT_ORC_Shields_A01/PRODUCTION_PACKAGE.md` | Production package ready; DCC build not started. |
| `KIT_ORC_ShamanicTalismans_A01` | `docs/assets/kits/KIT_ORC_ShamanicTalismans_A01/PRODUCTION_PACKAGE.md` | Production package ready; DCC build not started. |
| `MI_ORC_RunicAffinities_A01` | `docs/assets/materials/MI_ORC_RunicAffinities_A01/PRODUCTION_PACKAGE.md` | Production package ready; Unreal material authoring not started. |
| `SM_MIN_GreatAxe_A01` | `docs/assets/props/SM_MIN_GreatAxe_A01/PRODUCTION_PACKAGE.md` | Production package ready; DCC build not started. |
| `SM_MIN_CrushingMaul_A01` | `docs/assets/props/SM_MIN_CrushingMaul_A01/PRODUCTION_PACKAGE.md` | Production package ready; DCC build not started. |
| `KIT_MIN_HideShields_A01` | `docs/assets/kits/KIT_MIN_HideShields_A01/PRODUCTION_PACKAGE.md` | Production package ready; DCC build not started. |
| `KIT_MIN_Helmets_A01` | `docs/assets/kits/KIT_MIN_Helmets_A01/PRODUCTION_PACKAGE.md` | Production package ready; DCC fit blocked on approved Minotaur base body/skeleton. |
| `SM_DKH_RiversindRecurve_A01` | `docs/assets/props/SM_DKH_RiversindRecurve_A01/PRODUCTION_PACKAGE.md` | Production package ready; DCC build not started. |
| `KIT_DKH_CurvedDaggers_A01` | `docs/assets/kits/KIT_DKH_CurvedDaggers_A01/PRODUCTION_PACKAGE.md` | Production package ready; DCC build not started. |
| `SM_DKH_ReedShellShield_A01` | `docs/assets/props/SM_DKH_ReedShellShield_A01/PRODUCTION_PACKAGE.md` | Production package ready; DCC build not started. |
| `KIT_DKH_MagicTrackingCharms_A01` | `docs/assets/kits/KIT_DKH_MagicTrackingCharms_A01/PRODUCTION_PACKAGE.md` | Production package ready; DCC build not started. |

## Source And Export Path Plan

These paths are planned references only. This task does not create source folders, export folders, Blender files, FBX files, or Unreal assets.

| Asset or package | Planned Blender source path | Planned export path | Unreal target path from package |
| --- | --- | --- | --- |
| `SM_DWR_OathkeeperHammer_A01` | `SourceAssets/Blender/Kits/Dwarven/Armory/SM_DWR_OathkeeperHammer_A01/` | `SourceAssets/Exports/Kits/Dwarven/Armory/SM_DWR_OathkeeperHammer_A01/` | `/Game/Aerathea/Weapons/Dwarven/SM_DWR_OathkeeperHammer_A01` |
| `SM_DWR_StonewallShield_A01` | `SourceAssets/Blender/Kits/Dwarven/Armory/SM_DWR_StonewallShield_A01/` | `SourceAssets/Exports/Kits/Dwarven/Armory/SM_DWR_StonewallShield_A01/` | `/Game/Aerathea/Shields/Dwarven/SM_DWR_StonewallShield_A01` |
| `SK_DWR_Helm_Stonebound_A01` | `SourceAssets/Blender/Kits/Dwarven/Armory/SK_DWR_Helm_Stonebound_A01/` | `SourceAssets/Exports/Kits/Dwarven/Armory/SK_DWR_Helm_Stonebound_A01/` | `/Game/Aerathea/Characters/Dwarves/Armor/SK_DWR_Helm_Stonebound_A01` |
| `SM_ELV_Moonblade_A01` | `SourceAssets/Blender/Kits/Elven/Armory/SM_ELV_Moonblade_A01/` | `SourceAssets/Exports/Kits/Elven/Armory/SM_ELV_Moonblade_A01/` | `/Game/Aerathea/Weapons/Elven/SM_ELV_Moonblade_A01` |
| `SM_ELV_SilverleafRecurve_A01` | `SourceAssets/Blender/Kits/Elven/Armory/SM_ELV_SilverleafRecurve_A01/` | `SourceAssets/Exports/Kits/Elven/Armory/SM_ELV_SilverleafRecurve_A01/` | `/Game/Aerathea/Weapons/Elven/SM_ELV_SilverleafRecurve_A01` |
| `SM_ELV_MoonwardBuckler_A01` | `SourceAssets/Blender/Kits/Elven/Armory/SM_ELV_MoonwardBuckler_A01/` | `SourceAssets/Exports/Kits/Elven/Armory/SM_ELV_MoonwardBuckler_A01/` | `/Game/Aerathea/Shields/Elven/SM_ELV_MoonwardBuckler_A01` |
| `SM_ELV_AetheriumLantern_A01` | `SourceAssets/Blender/Kits/Elven/Armory/SM_ELV_AetheriumLantern_A01/` | `SourceAssets/Exports/Kits/Elven/Armory/SM_ELV_AetheriumLantern_A01/` | `/Game/Aerathea/Props/Elven/SM_ELV_AetheriumLantern_A01` |
| `SM_DEL_DuskspiteBlade_A01` | `SourceAssets/Blender/Kits/DarkElven/Armory/SM_DEL_DuskspiteBlade_A01/` | `SourceAssets/Exports/Kits/DarkElven/Armory/SM_DEL_DuskspiteBlade_A01/` | `/Game/Aerathea/Weapons/DarkElven/SM_DEL_DuskspiteBlade_A01` |
| `SM_DEL_VeilstriderBow_A01` | `SourceAssets/Blender/Kits/DarkElven/Armory/SM_DEL_VeilstriderBow_A01/` | `SourceAssets/Exports/Kits/DarkElven/Armory/SM_DEL_VeilstriderBow_A01/` | `/Game/Aerathea/Weapons/DarkElven/SM_DEL_VeilstriderBow_A01` |
| `SM_DEL_AegisOfEternalDusk_A01` | `SourceAssets/Blender/Kits/DarkElven/Armory/SM_DEL_AegisOfEternalDusk_A01/` | `SourceAssets/Exports/Kits/DarkElven/Armory/SM_DEL_AegisOfEternalDusk_A01/` | `/Game/Aerathea/Shields/DarkElven/SM_DEL_AegisOfEternalDusk_A01` |
| `SM_ORC_GreatAxe_A01` | `SourceAssets/Blender/Kits/Orc/Arsenal/SM_ORC_GreatAxe_A01/` | `SourceAssets/Exports/Kits/Orc/Arsenal/SM_ORC_GreatAxe_A01/` | `/Game/Aerathea/Weapons/Orc/SM_ORC_GreatAxe_A01` |
| `KIT_ORC_Shields_A01` | `SourceAssets/Blender/Kits/Orc/Arsenal/KIT_ORC_Shields_A01/` | `SourceAssets/Exports/Kits/Orc/Arsenal/KIT_ORC_Shields_A01/` | `/Game/Aerathea/Shields/Orc/` |
| `KIT_ORC_ShamanicTalismans_A01` | `SourceAssets/Blender/Kits/Orc/Arsenal/KIT_ORC_ShamanicTalismans_A01/` | `SourceAssets/Exports/Kits/Orc/Arsenal/KIT_ORC_ShamanicTalismans_A01/` | `/Game/Aerathea/Props/Orc/` |
| `SM_MIN_GreatAxe_A01` | `SourceAssets/Blender/Kits/Minotaur/Arsenal/SM_MIN_GreatAxe_A01/` | `SourceAssets/Exports/Kits/Minotaur/Arsenal/SM_MIN_GreatAxe_A01/` | `/Game/Aerathea/Weapons/Minotaur/SM_MIN_GreatAxe_A01` |
| `SM_MIN_CrushingMaul_A01` | `SourceAssets/Blender/Kits/Minotaur/Arsenal/SM_MIN_CrushingMaul_A01/` | `SourceAssets/Exports/Kits/Minotaur/Arsenal/SM_MIN_CrushingMaul_A01/` | `/Game/Aerathea/Weapons/Minotaur/SM_MIN_CrushingMaul_A01` |
| `KIT_MIN_HideShields_A01` | `SourceAssets/Blender/Kits/Minotaur/Arsenal/KIT_MIN_HideShields_A01/` | `SourceAssets/Exports/Kits/Minotaur/Arsenal/KIT_MIN_HideShields_A01/` | `/Game/Aerathea/Shields/Minotaur/` |
| `KIT_MIN_Helmets_A01` | `SourceAssets/Blender/Kits/Minotaur/Arsenal/KIT_MIN_Helmets_A01/` | `SourceAssets/Exports/Kits/Minotaur/Arsenal/KIT_MIN_Helmets_A01/` | `/Game/Aerathea/Characters/Minotaur/Armor/` |
| `SM_DKH_RiversindRecurve_A01` | `SourceAssets/Blender/Kits/Drakhar/FieldGear/SM_DKH_RiversindRecurve_A01/` | `SourceAssets/Exports/Kits/Drakhar/FieldGear/SM_DKH_RiversindRecurve_A01/` | `/Game/Aerathea/Weapons/Drakhar/SM_DKH_RiversindRecurve_A01` |
| `KIT_DKH_CurvedDaggers_A01` | `SourceAssets/Blender/Kits/Drakhar/FieldGear/KIT_DKH_CurvedDaggers_A01/` | `SourceAssets/Exports/Kits/Drakhar/FieldGear/KIT_DKH_CurvedDaggers_A01/` | `/Game/Aerathea/Weapons/Drakhar/` |
| `SM_DKH_ReedShellShield_A01` | `SourceAssets/Blender/Kits/Drakhar/FieldGear/SM_DKH_ReedShellShield_A01/` | `SourceAssets/Exports/Kits/Drakhar/FieldGear/SM_DKH_ReedShellShield_A01/` | `/Game/Aerathea/Shields/Drakhar/SM_DKH_ReedShellShield_A01` |
| `KIT_DKH_MagicTrackingCharms_A01` | `SourceAssets/Blender/Kits/Drakhar/FieldGear/KIT_DKH_MagicTrackingCharms_A01/` | `SourceAssets/Exports/Kits/Drakhar/FieldGear/KIT_DKH_MagicTrackingCharms_A01/` | `/Game/Aerathea/Props/Drakhar/` |

Material packages do not need Blender source or FBX exports unless a later approved task adds helper meshes or material preview props.

## Material Dependency Matrix

| Asset or package | Material dependency notes | Risk |
| --- | --- | --- |
| Dwarf weapon, shield, and helm | Use `MI_DWR_RunicGlowStates_A01` plus dark steel, slate stone, aged brass, leather, and restrained blue emissive masks. | Medium until material states exist in Unreal; low for DCC geometry. |
| Elf sword, bow, buckler, and lantern | No standalone priority material package exists. Use per-asset `BC`, `N`, `ORM`, and limited `E` maps for moonstone/Aetherium accents. | Medium; final material consistency needs a later Elven material-set task or shared parent assignment. |
| Dark Elf blade, bow, and shield | Use `MI_DEL_ShadowArmory_Set_A01` for obsidian, dark silver, black leather, veiled cloth, and violet lunar glow. | Medium until material set is authored; readability risk if dark forms lack edge contrast. |
| Orc axe, shields, and talismans | Use `MI_ORC_RunicAffinities_A01` plus dark iron, bronze, bone, leather, fur, spirit stone, and muted clan masks. | Medium until rune affinities are authored; mini-kit variants must not duplicate bespoke materials. |
| Minotaur weapons, shields, and helmets | Use raw iron, hide, bone, leather, fur, rope, dark wood, and no emissive baseline. | Low material complexity; high scale/fit risk for helmets only. |
| Drakhar bow, daggers, shield, and charms | No standalone priority material package exists. Use reed, shell, bone, leather, sun-baked wood/stone, and limited ember or relic emissive maps. | Medium; A04 scale correction and glow restraint must be validated asset by asset. |

## Risk Ranking

| Rank | Risk | Affected assets | Mitigation |
| ---: | --- | --- | --- |
| 1 | Character fit is blocked until base body/skeleton approval. | `SK_DWR_Helm_Stonebound_A01`, `KIT_MIN_Helmets_A01` | Keep on hold; do not author fit-critical DCC until body, head, horns, and head socket contracts are approved. |
| 2 | Drakhar source-sheet scale conflicts with approved A04 scale. | All `DKH` priority children | Use female 3'6"-4'2" and male 4'0"-4'6" scale; require scale marker validation in any DCC task. |
| 3 | Mini-kits need variant manifests before source work. | `KIT_ORC_Shields_A01`, `KIT_ORC_ShamanicTalismans_A01`, `KIT_MIN_HideShields_A01`, `KIT_DKH_CurvedDaggers_A01`, `KIT_DKH_MagicTrackingCharms_A01` | Approve variant names, per-variant pivots, export file names, material slots, and collision policy before modeling. |
| 4 | Bow sockets and future string behavior are not implementation-ready. | `SM_ELV_SilverleafRecurve_A01`, `SM_DEL_VeilstriderBow_A01`, `SM_DKH_RiversindRecurve_A01` | Confirm arrow rest and string locator names before DCC export; keep string animation out of scope. |
| 5 | Material dependency authoring is uneven across factions. | Dwarf, Dark Elf, Orc have material packages; Elf, Minotaur, Drakhar do not. | Treat material packages as dependencies, not mesh targets; use per-asset maps where no material package exists. |
| 6 | Excessive micro-detail could inflate geometry. | Talismans, charms, shields, rune/leaf/crescent details | Model primary forms only; push tiny scratches, stitches, glyphs, etching, weave, and pores into texture/normal maps. |
| 7 | Pivot and collision errors would break equipment use. | All weapons and shields | Validate grip/forearm/back strap pivots and simple collision in focused import validators. |
| 8 | Package-needed siblings can drift into scope. | All parent kits | Keep this matrix limited to priority children with existing production packages. |

## Validator Gaps And Future Checks

No focused armory DCC or Unreal validators were found under `Tools/DCC/` or `Tools/Unreal/` for these factions during this docs pass. Future implementation tasks should add focused validators only when those tasks own tools.

| Future lane | Validator requirement |
| --- | --- |
| DCC source/export validation | Confirm source path, export path, FBX name, centimeter scale, primary dimensions, pivot, LOD0-LOD3 presence, material slot count, and no micro-detail geometry misuse. |
| Weapon import validation | Confirm Unreal path, grip pivot, equipped collision disabled, simple pickup/display collision, LODs, material slots, texture references, and optional glow sockets. |
| Shield import validation | Confirm forearm/back grip pivot, simple convex/box collision, LODs, back strap read, material slots, and optional glow sockets. |
| Bow import validation | Confirm `socket_arrow_rest`, `socket_string_top`, `socket_string_bottom`, grip pivot, bow arc preservation across LODs, and no gameplay draw-string implementation unless assigned. |
| Mini-kit validation | Confirm per-variant mesh names, export rows, pivots, collision policy, material slots, LODs, and distinct silhouettes. |
| Character gear fit validation | Confirm approved base body/skeleton, head socket, horn/head clearance, clipping, LODs, material slots, and no gameplay collision while equipped. |
| Material validation | Confirm shared parent material, parameter naming, emissive strength clamps, mask texture references, distance fade or pulse limits, and no all-over glow. |
| Matrix maintenance validation | Run package-existence scan, implementation-scope guardrail scan, and `git diff --check` after docs edits. |

## Approval Gates

- Lead approval is required to select any final DCC build target from this queue.
- DCC work may start only from an assigned implementation task that owns the relevant source/export paths.
- Material authoring may start only from an assigned material/Unreal task; material packages in this matrix are dependencies, not DCC targets.
- Mini-kits require a variant export manifest before modeling starts.
- Drakhar work requires explicit A04 scale confirmation before any DCC source is authored.
- Dwarf and Minotaur helmet work remains blocked until the matching base body/skeleton and socket contracts are approved.
- Unreal import may start only after DCC source/export evidence exists and the task owns Unreal Content paths.
- Startup placement, gameplay behavior, VFX graph authoring, cloth/physics, secondary motion, final texture polish, and final visual approval are outside this matrix.

## Quality Gate Checklist

- The matrix references only package-ready priority children for the six assigned factions.
- DCC queue priority is recorded without choosing a final build target.
- Source/export paths are plans only; no folders, meshes, FBX files, tools, or Unreal assets are authored here.
- Material dependencies and missing material-package lanes are explicit.
- Fit-blocked gear is separated from ready static mesh work.
- Drakhar scale conflict is called out and resolved to approved A04 scale.
- Mini-kit variant manifests are approval-gated.
- Future validator gaps are documented without creating tools.
