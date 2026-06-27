# Aerathea Asset Index

## Props

| Asset | Status | Package |
| --- | --- | --- |
| `SM_AET_TargetDummy_A01` | Blender source and FBX generated, imported to Unreal, startup blockout replaced, validation passing | `docs/assets/props/SM_AET_TargetDummy_A01/PRODUCTION_PACKAGE.md` |
| `SM_AET_PortalArch_A01` | Blender source and FBX generated, imported to Unreal, startup portal visual replaced, validation passing | `docs/assets/props/SM_AET_PortalArch_A01/PRODUCTION_PACKAGE.md` |
| `SM_MKG_WorkshopPropCrate_A01` | Blender source and FBX generated, imported to Unreal, placed in startup scene, validation passing | `docs/assets/props/SM_MKG_WorkshopPropCrate_A01/PRODUCTION_PACKAGE.md` |
| `SM_AET_ModularGroundTile_A01` | Blender source and FBX generated, imported to Unreal, placed as 5x5 startup ground-tile layout, validation passing | `docs/assets/props/SM_AET_ModularGroundTile_A01/PRODUCTION_PACKAGE.md` |
| `SM_MKG_AetherKnife_A01` | Blender source and FBX generated, imported to Unreal, modeling handoff ready, placed in startup scene, validation passing | `docs/assets/props/SM_MKG_AetherKnife_A01/PRODUCTION_PACKAGE.md` |
| `SM_MKG_AetherCoreUnit_A01` | Blender source and FBX generated, imported to Unreal, modeling handoff ready, placed in startup scene, validation passing | `docs/assets/props/SM_MKG_AetherCoreUnit_A01/PRODUCTION_PACKAGE.md` |
| `SM_MKG_SparkPistol_A01` | Blender source and FBX generated, imported to Unreal, modeling handoff ready, placed in startup scene, validation passing | `docs/assets/props/SM_MKG_SparkPistol_A01/PRODUCTION_PACKAGE.md` |
| `SM_MKG_AetheriumGrenade_A01` | Blender source and FBX generated, imported to Unreal, modeling handoff ready, placed in startup scene, validation passing | `docs/assets/props/SM_MKG_AetheriumGrenade_A01/PRODUCTION_PACKAGE.md` |

## Kits

| Asset | Status | Package |
| --- | --- | --- |
| `KIT_MKG_Armory_A01` | Kit package ready, child asset intake complete, first four child packages and handoffs ready | `docs/assets/kits/KIT_MKG_Armory_A01/PRODUCTION_PACKAGE.md` |
| `KIT_DWR_Armory_A01` | Child asset intake complete, kit production package ready | `docs/assets/kits/KIT_DWR_Armory_A01/PRODUCTION_PACKAGE.md` |
| `KIT_ELV_Armory_A01` | Child asset intake complete, kit production package ready | `docs/assets/kits/KIT_ELV_Armory_A01/PRODUCTION_PACKAGE.md` |
| `KIT_DEL_Armory_A01` | Child asset intake complete, kit production package ready | `docs/assets/kits/KIT_DEL_Armory_A01/PRODUCTION_PACKAGE.md` |
| `KIT_ORC_Arsenal_A01` | Child asset intake complete, kit production package ready | `docs/assets/kits/KIT_ORC_Arsenal_A01/PRODUCTION_PACKAGE.md` |
| `KIT_MIN_Arsenal_A01` | Child asset intake complete, kit production package ready | `docs/assets/kits/KIT_MIN_Arsenal_A01/PRODUCTION_PACKAGE.md` |
| `KIT_DKH_FieldGear_A01` | Child asset intake complete, kit production package ready; package uses approved 4-5 ft Drakhar scale over conflicting source-sheet scale | `docs/assets/kits/KIT_DKH_FieldGear_A01/PRODUCTION_PACKAGE.md` |

## Characters

| Asset | Status | Package |
| --- | --- | --- |
| `SK_GNM_Base_A01` | First race body production package ready | `docs/assets/characters/SK_GNM_Base_A01/PRODUCTION_PACKAGE.md` |
| `SK_OGR_Base_A01` | Ogre source concept intake and base body production package ready; DCC build not started | `docs/assets/characters/SK_OGR_Base_A01/PRODUCTION_PACKAGE.md` |

## Blueprints

| Asset | Status | Package |
| --- | --- | --- |
| `BP_AET_Portal_A01` | Blueprint asset reparented to `AAETPortalActor`; startup review actor uses the native portal class with imported arch/core visuals, validation passing | `docs/assets/blueprints/BP_AET_Portal_A01/PRODUCTION_PACKAGE.md` |

## Status Key

- `Production spec ready`: asset brief, concept prompts, modeling notes, texture plan, LOD plan, collision notes, Unreal import notes, and quality gate exist.
- `Concept direction proposed`: a recommended direction exists, but final visual approval is still pending.
- `Concept sheet generated`: a first-pass bitmap concept reference exists in the asset package.
- `Modeling handoff ready`: concept reference, production package, and DCC modeling checklist are available for a specific asset.
- `Build/import blocked on approved DCC mesh`: import cannot be completed without an approved modeled source asset; do not substitute a procedural placeholder.
- `Blender source and FBX generated`: Blender `.blend` source and FBX export files exist under `SourceAssets/`.
- `Imported to Unreal`: the source export has been imported as a `.uasset`.
- `Kit package ready`: multi-asset kit direction exists and can be split into child production packages.
- `Child asset intake complete`: a collage/catalog has been visually split into buildable child items with proposed asset names.
- `Implementation handoff ready`: Blueprint construction plan exists, but the Unreal asset may still be blocked by missing imported dependencies.
- `Ready for modeling review`: concept and production spec can be reviewed for approval before DCC work starts.
- `Implementation pending`: blueprint behavior and dependencies are specified, but the Unreal Blueprint asset has not been built yet.
- `Ready for modeling`: concept direction has been approved and the asset can move to DCC production.
