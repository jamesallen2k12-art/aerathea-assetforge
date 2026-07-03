# KIT_INF_BalgorothCult_A01 Implementation Readiness Matrix

## Scope

- Original task: `AET-MA-20260628-022`
- Status refresh: `AET-MA-20260628-032`
- Scope type: DCC/Unreal readiness and implementation-status matrix.
- Build scope for this refresh: status/documentation only.
- New source, export, Unreal Content, runtime source, and tool implementation are explicitly out of scope for this refresh.

This matrix converts the Balgoroth cult child assets into implementation order and records completed first-pass dependency lanes. It does not approve or start additional DCC modeling, FBX export, Unreal import, Niagara graph authoring, startup placement, runtime gameplay, or final visual art.

## Package Set

| Asset | Package | Current status | Implementation status |
| --- | --- | --- | --- |
| `MI_INF_CultStone_Set_A01` | `docs/assets/materials/MI_INF_CultStone_Set_A01/PRODUCTION_PACKAGE.md` | Production package and build/import status ready | First-pass Unreal material set implemented and focused validation passed; final textures and final shader polish not authored |
| `SM_INF_BalgorothSigil_A01` | `docs/assets/props/SM_INF_BalgorothSigil_A01/PRODUCTION_PACKAGE.md` | Production package, modeling handoff, and build/import status ready | First-pass DCC source/export/proof and Unreal static mesh import validated; final sculpt/UVs/textures/tuned collision/startup placement not complete |
| `SM_INF_BrandingStone_A01` | `docs/assets/props/SM_INF_BrandingStone_A01/PRODUCTION_PACKAGE.md` | Production package and implementation packet ready | Docs-only implementation packet; DCC, FBX, Unreal Content, runtime behavior, VFX graph, and startup placement not started |
| `VFX_INF_RegenerationBrand_A01` | `docs/assets/vfx/VFX_INF_RegenerationBrand_A01/PRODUCTION_PACKAGE.md` | Production package ready | Not implemented |
| `SM_INF_AshBasin_A01` | `docs/assets/props/SM_INF_AshBasin_A01/PRODUCTION_PACKAGE.md` | Production package ready | Not implemented |
| `SM_INF_WitnessChains_A01` | `docs/assets/props/SM_INF_WitnessChains_A01/PRODUCTION_PACKAGE.md` | Production package ready | Not implemented |
| `SM_INF_TrialBanner_A01` | `docs/assets/props/SM_INF_TrialBanner_A01/PRODUCTION_PACKAGE.md` | Production package ready | Not implemented |

## Recommended Build Order

| Order | Asset | Why this order | Stop condition |
| ---: | --- | --- | --- |
| 1 | `MI_INF_CultStone_Set_A01` | Completed first-pass material dependency before mesh variants multiply. | Future work stops before final shader polish, texture production, or expanded emissive behavior unless a final-art material task is approved. |
| 2 | `SM_INF_BalgorothSigil_A01` | Completed first-pass reusable symbol relief source for branding stone, banner, floor, altar, and future gate/den props. | Future work stops before final sculpt/UV/texture/tuned collision, variant split, or startup placement unless assigned. |
| 3 | `SM_INF_BrandingStone_A01` | Next recommended build promotion; anchors regeneration/brand transfer sockets and interaction side for later VFX and ritual staging. | Stop before DCC source creation, Unreal import, startup placement, VFX graph authoring, or runtime interaction behavior until approved. |
| 4 | `SM_INF_AshBasin_A01` | Low-risk prop validates shared material use and restrained ash/ember socket conventions. | Stop before smoke/ember VFX authoring. |
| 5 | `SM_INF_WitnessChains_A01` | Adds modular dressing but must preserve sparse chunky chain geometry and non-complex collision. | Stop before physics, skeletal chains, or gameplay restraint behavior. |
| 6 | `SM_INF_TrialBanner_A01` | Uses locked sigil and ash-cloth language for faction-readable vertical dressing. | Stop before cloth simulation, skeletal variants, or symbol changes. |
| 7 | `VFX_INF_RegenerationBrand_A01` | Should consume built BrandingStone sockets and BrandGlow masks after prop/material targets are stable. | Stop before final Niagara graph art, gameplay healing rules, and animation timing. |

## Shared Scale Grid

| Reference | Scale |
| --- | --- |
| Humanoid review scale | 180 cm |
| Adult Infernal upper review scale | 274 cm |
| Lesser Spawn/Blooded staging | 70-90 cm |
| BrandingStone review target | 190h x 95w x 75d cm |
| AshBasin small target | 65w x 42h x 65d cm |
| AshBasin large target | 130w x 75h x 130d cm |
| WitnessChains wall pair | 180-320 cm hanging length |
| TrialBanner wall variant | 90-140w x 220-360h cm |

## Source And Export Plan

| Asset | Blender source path | FBX export path |
| --- | --- | --- |
| `SM_INF_BalgorothSigil_A01` | `SourceAssets/Blender/Props/Infernals/BalgorothCult/SM_INF_BalgorothSigil_A01/` | `SourceAssets/Exports/Props/Infernals/BalgorothCult/SM_INF_BalgorothSigil_A01/` |
| `SM_INF_BrandingStone_A01` | `SourceAssets/Blender/Props/Infernals/BalgorothCult/SM_INF_BrandingStone_A01/` | `SourceAssets/Exports/Props/Infernals/BalgorothCult/SM_INF_BrandingStone_A01/` |
| `SM_INF_AshBasin_A01` | `SourceAssets/Blender/Props/Infernals/BalgorothCult/SM_INF_AshBasin_A01/` | `SourceAssets/Exports/Props/Infernals/BalgorothCult/SM_INF_AshBasin_A01/` |
| `SM_INF_WitnessChains_A01` | `SourceAssets/Blender/Props/Infernals/BalgorothCult/SM_INF_WitnessChains_A01/` | `SourceAssets/Exports/Props/Infernals/BalgorothCult/SM_INF_WitnessChains_A01/` |
| `SM_INF_TrialBanner_A01` | `SourceAssets/Blender/Props/Infernals/BalgorothCult/SM_INF_TrialBanner_A01/` | `SourceAssets/Exports/Props/Infernals/BalgorothCult/SM_INF_TrialBanner_A01/` |

Material and VFX packages do not need Blender source unless helper meshes are approved later.

## Unreal Target Paths

| Asset | Unreal path |
| --- | --- |
| `MI_INF_CultStone_Set_A01` | `/Game/Aerathea/Materials/Infernals/`, `/Game/Aerathea/Materials/Instances/`, `/Game/Aerathea/Textures/Infernals/BalgorothCult/` |
| `SM_INF_BalgorothSigil_A01` | `/Game/Aerathea/Props/Infernals/BalgorothCult/Sigils/` |
| `SM_INF_BrandingStone_A01` | `/Game/Aerathea/Props/Infernals/BalgorothCult/BrandingStone/` |
| `SM_INF_AshBasin_A01` | `/Game/Aerathea/Props/Infernals/BalgorothCult/AshBasin/` |
| `SM_INF_WitnessChains_A01` | `/Game/Aerathea/Props/Infernals/BalgorothCult/WitnessChains/` |
| `SM_INF_TrialBanner_A01` | `/Game/Aerathea/Props/Infernals/BalgorothCult/TrialBanner/` |
| `VFX_INF_RegenerationBrand_A01` | `/Game/Aerathea/VFX/Infernals/RegenerationBrand/`, `/Game/Aerathea/Materials/Infernals/VFX/`, `/Game/Aerathea/Textures/Infernals/VFX/RegenerationBrand/` |

## Material Dependency Matrix

| Asset | Required material dependencies | Material-slot risk |
| --- | --- | --- |
| `SM_INF_BalgorothSigil_A01` | `MI_INF_CultStone_Basalt_A01`, `MI_INF_CultStone_ScorchedRed_A01`, `MI_INF_CultStone_ObsidianInset_A01`, emissive channel | Keep 1-3 slots; 4 only for approved hero floor insert. |
| `SM_INF_BrandingStone_A01` | Cult stone set, Balgoroth sigil, BrandGlow emissive state | Keep 3-5 slots; avoid duplicate custom stone materials. |
| `SM_INF_AshBasin_A01` | Cult stone basalt, scorched red, black iron, ash fill, emissive | Prefer 2-4 slots; 5 only for hero placement. |
| `SM_INF_WitnessChains_A01` | Black iron, basalt anchors, scorched grooves, bone/horn markers, optional emissive | Most variants should use 2-3 slots. |
| `SM_INF_TrialBanner_A01` | Ash cloth, black iron or bone/horn, sigil print, optional emissive | Keep 2-4 slots; no all-over emissive cloth. |
| `VFX_INF_RegenerationBrand_A01` | BrandGlow states, RegenerationBrand helper materials, BrandingStone sockets | Do not create a new brand material identity. |

## Socket And Locator Matrix

| Asset | Required sockets or locators |
| --- | --- |
| `SM_INF_BalgorothSigil_A01` | `vfx_sigil_core`, `vfx_eye_core`, `vfx_rejected_break`, `snap_floor_center` |
| `SM_INF_BrandingStone_A01` | `vfx_brand_core`, `vfx_brand_transfer`, `vfx_rejected_snap`, `interact_brand_side`, `snap_floor_center` |
| `SM_INF_AshBasin_A01` | `vfx_ash_lift`, `vfx_ember_core`, `vfx_rejected_puff`, `snap_floor_center` |
| `SM_INF_WitnessChains_A01` | `vfx_anchor_ember`, `vfx_chain_snap`, `snap_wall_anchor`, `snap_floor_anchor` |
| `SM_INF_TrialBanner_A01` | `snap_wall_hanger`, `snap_pole_base`, `vfx_sigil_ember`, `vfx_rejected_thread` |
| `VFX_INF_RegenerationBrand_A01` | consumes `vfx_brand_core`, `vfx_brand_transfer`, `User.BrandCoreWorldLocation`, `User.BrandTransferWorldLocation`, and body brand masks |

## Validator Plan

| Future lane | Required validator |
| --- | --- |
| Material authoring | `Tools/Unreal/validate_infernal_cult_stone_materials.py` |
| Sigil import | `Tools/Unreal/validate_infernal_balgoroth_sigil.py` |
| BrandingStone import | `Tools/Unreal/validate_infernal_branding_stone.py` |
| AshBasin import | `Tools/Unreal/validate_infernal_ash_basin.py` |
| WitnessChains import | `Tools/Unreal/validate_infernal_witness_chains.py` |
| TrialBanner import | `Tools/Unreal/validate_infernal_trial_banner.py` |
| RegenerationBrand VFX | `Tools/Unreal/validate_infernal_regeneration_brand_vfx.py` |
| Startup review placement | `Tools/Unreal/validate_startup_scene.py` after any startup map changes |

Validator checks should cover source import path, asset names, material slots, LOD0-LOD3, pivots, collision policy, required sockets, bounds, and stale reference prevention.

## Approval Gates

- DCC creation starts only after a build task selects the asset and confirms scope.
- Unreal import starts only after source asset or material/VFX authoring evidence exists.
- Startup placement starts only after focused import validation passes.
- Final VFX graph authoring for `VFX_INF_RegenerationBrand_A01` requires visual approval and must stay within the BrandGlow and Infernal readability contracts.
- Gameplay healing, regeneration values, backend authority, quest state, restraint behavior, cloth simulation, and final animation timing remain out of scope.

## Next Allowed Task

Run `AET-MA-20260629-033` only after user approval to promote `SM_INF_BrandingStone_A01` from implementation packet to DCC/Unreal build work. If approved, continue with BrandingStone DCC source/export/proof, Unreal import/validation, QA, and then RegenerationBrand readiness work that consumes the validated BrandingStone socket contract.
