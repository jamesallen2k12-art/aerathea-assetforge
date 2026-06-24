# Aerathea Asset Index

## Props

| Asset | Status | Package |
| --- | --- | --- |
| `SM_AET_TargetDummy_A01` | Source OBJ/FBX generated, imported to Unreal, startup blockout replaced, validation passing | `docs/assets/props/SM_AET_TargetDummy_A01/PRODUCTION_PACKAGE.md` |
| `SM_AET_PortalArch_A01` | Source OBJ/FBX generated, imported to Unreal, startup blockout replaced, validation passing | `docs/assets/props/SM_AET_PortalArch_A01/PRODUCTION_PACKAGE.md` |
| `SM_MKG_WorkshopPropCrate_A01` | Source OBJ/FBX generated, imported to Unreal, placed in startup scene, validation passing | `docs/assets/props/SM_MKG_WorkshopPropCrate_A01/PRODUCTION_PACKAGE.md` |
| `SM_AET_ModularGroundTile_A01` | Source OBJ/FBX generated, imported to Unreal, placed as 5x5 startup ground-tile layout, validation passing | `docs/assets/props/SM_AET_ModularGroundTile_A01/PRODUCTION_PACKAGE.md` |
| `SM_MKG_AetherKnife_A01` | Production package ready | `docs/assets/props/SM_MKG_AetherKnife_A01/PRODUCTION_PACKAGE.md` |
| `SM_MKG_AetherCoreUnit_A01` | Production package ready | `docs/assets/props/SM_MKG_AetherCoreUnit_A01/PRODUCTION_PACKAGE.md` |
| `SM_MKG_SparkPistol_A01` | Production package ready | `docs/assets/props/SM_MKG_SparkPistol_A01/PRODUCTION_PACKAGE.md` |
| `SM_MKG_AetheriumGrenade_A01` | Production package ready | `docs/assets/props/SM_MKG_AetheriumGrenade_A01/PRODUCTION_PACKAGE.md` |

## Kits

| Asset | Status | Package |
| --- | --- | --- |
| `KIT_MKG_Armory_A01` | Kit package ready, child asset intake complete, child packages needed | `docs/assets/kits/KIT_MKG_Armory_A01/PRODUCTION_PACKAGE.md` |
| `KIT_DWR_Armory_A01` | Child asset intake complete, kit production package needed | `docs/assets/kits/KIT_DWR_Armory_A01/CHILD_ASSET_INTAKE.md` |
| `KIT_ELV_Armory_A01` | Child asset intake complete, kit production package needed | `docs/assets/kits/KIT_ELV_Armory_A01/CHILD_ASSET_INTAKE.md` |
| `KIT_DEL_Armory_A01` | Child asset intake complete, kit production package needed | `docs/assets/kits/KIT_DEL_Armory_A01/CHILD_ASSET_INTAKE.md` |
| `KIT_ORC_Arsenal_A01` | Child asset intake complete, kit production package needed | `docs/assets/kits/KIT_ORC_Arsenal_A01/CHILD_ASSET_INTAKE.md` |
| `KIT_MIN_Arsenal_A01` | Child asset intake complete, kit production package needed | `docs/assets/kits/KIT_MIN_Arsenal_A01/CHILD_ASSET_INTAKE.md` |
| `KIT_DKH_FieldGear_A01` | Child asset intake complete, kit production package needed; source scale conflicts with approved Drakhar anchor | `docs/assets/kits/KIT_DKH_FieldGear_A01/CHILD_ASSET_INTAKE.md` |

## Blueprints

| Asset | Status | Package |
| --- | --- | --- |
| `BP_AET_Portal_A01` | Blueprint asset shell created in Unreal; visual startup portal uses imported arch and core, behavior scripting still pending | `docs/assets/blueprints/BP_AET_Portal_A01/PRODUCTION_PACKAGE.md` |

## Status Key

- `Production spec ready`: asset brief, concept prompts, modeling notes, texture plan, LOD plan, collision notes, Unreal import notes, and quality gate exist.
- `Concept direction proposed`: a recommended direction exists, but final visual approval is still pending.
- `Concept sheet generated`: a first-pass bitmap concept reference exists in the asset package.
- `Modeling handoff ready`: concept reference, production package, and DCC modeling checklist are available for a specific asset.
- `Build/import blocked on approved DCC mesh`: import cannot be completed without an approved modeled source asset; do not substitute a procedural placeholder.
- `Source OBJ/FBX generated`: deterministic DCC fallback source/export files exist under `SourceAssets/` while Blender is blocked by the local USD/MaterialX runtime issue.
- `Imported to Unreal`: the source export has been imported as a `.uasset`.
- `Kit package ready`: multi-asset kit direction exists and can be split into child production packages.
- `Child asset intake complete`: a collage/catalog has been visually split into buildable child items with proposed asset names.
- `Implementation handoff ready`: Blueprint construction plan exists, but the Unreal asset may still be blocked by missing imported dependencies.
- `Ready for modeling review`: concept and production spec can be reviewed for approval before DCC work starts.
- `Implementation pending`: blueprint behavior and dependencies are specified, but the Unreal Blueprint asset has not been built yet.
- `Ready for modeling`: concept direction has been approved and the asset can move to DCC production.
