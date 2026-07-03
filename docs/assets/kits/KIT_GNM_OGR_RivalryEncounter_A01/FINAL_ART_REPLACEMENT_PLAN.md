# KIT_GNM_OGR_RivalryEncounter_A01 Final-Art Replacement Plan

## Purpose

This plan converts the accepted first-pass Gnome/Ogre encounter review assets into final production assets without breaking the validated startup scene, encounter coordinator, VFX parameter contracts, or shared skeleton assumptions.

The current review slice is useful for scale, silhouette, sockets, LOD validation, phase review, and gameplay timing. It is not final sculpted or hand-painted production art.

## Current Execution Status

- 2026-06-28: Flamestrike approved the production order to finish the Gnome/Ogre final-art foundation first, then complete the Ogre shared rig/art-model fit before Iona, Infernal, Giant, Portal, and Abyss follow-up lanes.
- 2026-06-28: `Tools/Unreal/validate_ogre_shared_skeletons.py` passed through `UnrealEditor-Cmd`; the male Ogre base, Teknomancer, Warrior, Shaman, and Necromancer review meshes are bound to `/Game/Aerathea/Characters/Ogres/Base/SK_OGR_Base_Male_A01_Skeleton`.
- Shared Ogre final-art fit now follows `docs/assets/kits/KIT_GNM_OGR_RivalryEncounter_A01/OGRE_SHARED_RIG_FINAL_ART_FIT_PLAN.md`.

## Dependency Order

1. **Lock shared character foundations first.**
   - `SK_OGR_Base_A01` owns Ogre male/female proportion, skeleton, sockets, capsule expectations, and shared class rig fit.
   - `SK_GNM_HeavyMek_Rivalry_A01` must decide whether it remains a generic combat Mek rig or becomes part of a shared Iona-class Mek rig family.
   - `SK_CRE_Manticore_A01` remains the base Manticore skeleton for the interrupt variant.
2. **Replace class and vehicle blockouts over locked foundations.**
   - Ogre class outfits must not update the Ogre male base skeleton reference pose.
   - Heavy Mek final geometry must preserve pilot, weapon, stomp, shield, and reactor socket semantics.
   - Manticore interrupt geometry must stay compatible with the base Manticore skeleton.
3. **Replace static encounter props after character scale is stable.**
   - `SM_OGR_CairnBattleGate_A01` and `SM_OGR_CrudeTekPylon_A01` should match final Ogre and Mek scale before authored collision and UVs are locked.
   - `SM_GNM_AetherShieldProjector_A01` should preserve `BP_GNM_HeavyMekShieldwall_A01` attachment and facing assumptions.
4. **Author texture/material sets and final LODs.**
   - Use 2K texture sets for common encounter assets.
   - Reserve 4K only for a named hero Mek, named Ogre champion, or cinematic boss variant.
   - Keep micro-detail in normal/texture maps rather than geometry.
5. **Tune physics, collision, sockets, animation, and VFX after final topology exists.**
   - Generated first-pass physics assets are validation placeholders.
   - Final animation and gameplay traces should bind to sockets, not fragile mesh detail.
   - Niagara graph polish should consume the existing native `User.*` contracts rather than requiring Blueprint rewrites.

## Asset Replacement Matrix

| Asset | Final-Art Dependency | Replacement Work | Collision / Physics Work | Validation Gate |
| --- | --- | --- | --- | --- |
| `SK_OGR_Base_A01` | Highest: gates Ogre classes | Final male/female sculpt, retopo, UVs, skin textures, shared skeleton skin weighting | Tune base physics bodies and gameplay capsule after final proportions | `Tools/Unreal/validate_ogre_shared_skeletons.py`, `Tools/Unreal/validate_startup_scene.py` |
| `SK_OGR_Teknomancer_A01` | Depends on Ogre male base skeleton | Final class outfit, powered hammer, back tanks, belt/chest reactor, authored texture set | Add simplified auxiliary bodies for hammer/back reactor only if needed | Ogre shared-skeleton validator plus startup validation |
| `SK_OGR_Warrior_Rival_A01` | Depends on Ogre male base skeleton | Final armor, shield, hammer, brutal melee silhouette, authored texture set | Tune shield/hammer trace sockets and physics bodies | Ogre shared-skeleton validator plus startup validation |
| `SK_OGR_Shaman_A01` | Depends on Ogre male base skeleton | Final ritual outfit, staff, cairn/bone charms, shamanic glow masks | Tune staff and charm auxiliary physics only where readable | Ogre shared-skeleton validator plus startup validation |
| `SK_OGR_Necromancer_A01` | Depends on Ogre male base skeleton | Final necromancer outfit, staff/lantern, trophies, green-black emissive masks | Avoid per-chain collision; tune staff/trophy bodies only if needed | Ogre shared-skeleton validator plus startup validation |
| `SK_GNM_HeavyMek_Rivalry_A01` | Depends on Mek rig-family decision | Final mechanical frame, pilot hatch, shield/cannon arm, hammer/tool arm, authored texture set | Replace generated bodies with tuned limbs, feet, pilot hatch, and weapon bodies | Startup validation and close-up manual review |
| `BP_GNM_HeavyMekShieldwall_A01` / `SM_GNM_AetherShieldProjector_A01` | Depends on final Mek/projector scale | Final projector mesh, panel support geometry, material states, shield attachment fit | Keep collision simple; gameplay uses native shieldwall actor and helper volumes | Startup validation, VFX polish target validation |
| `VFX_GNM_AetherShieldWall_A01` | Depends on final projector sockets and native `User.*` contract | Bespoke Niagara graph for idle, braced, impact, overload, failing, shutdown states | Use Blueprint/gameplay volumes for mechanics, not particle collision | `Tools/Unreal/validate_gnome_ogre_vfx_polish_targets.py` plus visual capture |
| `SM_OGR_CairnBattleGate_A01` | Depends on final Ogre/Mek scale | Final cairn stones, gate hardware, modular wall variants, authored UV/texture set | Replace simple validation collision with tuned box/convex modules | Startup validation and modular snap review |
| `SM_OGR_CrudeTekPylon_A01` / `BP_OGR_CrudeTekPylon_A01` | Depends on final pylon silhouette and gameplay objective rules | Final reactor column, tanks, conductors, damage-state geometry, authored texture set | UCX base/column/tank/conductor blocks plus interaction overlap in Blueprint | Startup validation, timing trace validation |
| `SK_CRE_Manticore_A01` | Base creature skeleton | Final sculpt/retopo, skin/wing/tail UVs, authored textures, full skin weighting | Tune body, wing, tail, and stinger physics bodies | Startup validation and creature close-up review |
| `SK_CRE_Manticore_Interrupt_A01` / `BP_CRE_ManticoreInterrupt_A01` | Depends on base Manticore skeleton and encounter timing | Final interrupt variant polish, landing/impact pose support, authored texture/VFX masks | Preserve impact trace sockets and leap/hold timing volumes | Startup validation, timing trace validation |
| `BP_GNM_OGR_BattlefieldEncounter_A01` | Depends on all branch actors retaining contracts | No art replacement; keep coordinator stable while assets swap underneath | Recheck trigger volumes and actor assignments after final art placement | Phase sequence validation and gameplay timing trace validation |

## Parallel Work That Is Safe

- Static prop final sculpt/retopo for `SM_OGR_CairnBattleGate_A01` and `SM_OGR_CrudeTekPylon_A01` can proceed while character final art is underway, as long as authored scale stays aligned to the validated startup scene.
- Shieldwall Niagara graph polish can continue against existing `User.*` parameters while final projector art is built, as long as the final projector keeps the same attachment role.
- Texture style-sheet work can begin for Ogre skin, blackened iron, crude brass/copper, scorched leather, cairn stone, and Gnome blue Aetherium materials before final retopo is complete.

## Blocking Decisions

- Final Ogre base sculpt and skin weighting must be approved before Ogre class outfits are marked final.
- Heavy Mek rig-family choice must be made before committing final animation or physics for `SK_GNM_HeavyMek_Rivalry_A01`.
- Manticore final skeleton/skin must be stable before the interrupt variant receives final animation and impact timing.
- Final pylon gameplay rules determine whether damage-state geometry needs separate mesh sections, material parameters, or Blueprint-swapped components.

## Required Validation After Each Final Replacement

Run the smallest relevant gate first, then the broad startup gate:

- Ogre class replacement: `Tools/Unreal/validate_ogre_shared_skeletons.py`
- Gnome/Ogre phase coordinator: `Tools/Unreal/validate_gnome_ogre_encounter_phase_sequence.py`
- Pylon/Manticore timing: `Tools/Unreal/validate_gnome_ogre_gameplay_timing_traces.py`
- Shield/pylon/Manticore VFX targets: `Tools/Unreal/validate_gnome_ogre_vfx_polish_targets.py`
- Startup scene: `Tools/Unreal/validate_startup_scene.py`

## Quality Gate

- Final replacements preserve current scale, sockets, actor labels, Blueprint references, and validation paths.
- Final geometry improves silhouette and material readability without adding excessive micro-geometry.
- Collision remains simple and gameplay-driven.
- Texture sets use Base Color, Normal, AO, packed ORM, and focused emissive masks.
- LOD0-LOD3 plans remain intact and reduce detail without destroying the primary silhouette.
