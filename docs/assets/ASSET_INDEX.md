# Aerathea Asset Index

## Props

| Asset | Status | Package |
| --- | --- | --- |
| `SM_AET_TargetDummy_A01` | Concept sheet generated, modeling handoff ready, build/import blocked on approved DCC mesh | `docs/assets/props/SM_AET_TargetDummy_A01/PRODUCTION_PACKAGE.md` |
| `SM_AET_PortalArch_A01` | Concept sheet generated, modeling handoff ready, build/import blocked on approved DCC mesh | `docs/assets/props/SM_AET_PortalArch_A01/PRODUCTION_PACKAGE.md` |
| `SM_MKG_WorkshopPropCrate_A01` | Concept sheet generated, modeling handoff ready | `docs/assets/props/SM_MKG_WorkshopPropCrate_A01/PRODUCTION_PACKAGE.md` |
| `SM_AET_ModularGroundTile_A01` | Concept sheet generated, modeling handoff ready | `docs/assets/props/SM_AET_ModularGroundTile_A01/PRODUCTION_PACKAGE.md` |

## Kits

| Asset | Status | Package |
| --- | --- | --- |
| `KIT_MKG_Armory_A01` | Kit package ready, child asset intake complete, child packages needed | `docs/assets/kits/KIT_MKG_Armory_A01/PRODUCTION_PACKAGE.md` |

## Blueprints

| Asset | Status | Package |
| --- | --- | --- |
| `BP_AET_Portal_A01` | Concept state sheet generated, implementation handoff ready, final Blueprint blocked on portal arch mesh import | `docs/assets/blueprints/BP_AET_Portal_A01/PRODUCTION_PACKAGE.md` |

## Status Key

- `Production spec ready`: asset brief, concept prompts, modeling notes, texture plan, LOD plan, collision notes, Unreal import notes, and quality gate exist.
- `Concept direction proposed`: a recommended direction exists, but final visual approval is still pending.
- `Concept sheet generated`: a first-pass bitmap concept reference exists in the asset package.
- `Modeling handoff ready`: concept reference, production package, and DCC modeling checklist are available for a specific asset.
- `Build/import blocked on approved DCC mesh`: import cannot be completed without an approved modeled source asset; do not substitute a procedural placeholder.
- `Kit package ready`: multi-asset kit direction exists and can be split into child production packages.
- `Child asset intake complete`: a collage/catalog has been visually split into buildable child items with proposed asset names.
- `Implementation handoff ready`: Blueprint construction plan exists, but the Unreal asset may still be blocked by missing imported dependencies.
- `Ready for modeling review`: concept and production spec can be reviewed for approval before DCC work starts.
- `Implementation pending`: blueprint behavior and dependencies are specified, but the Unreal Blueprint asset has not been built yet.
- `Ready for modeling`: concept direction has been approved and the asset can move to DCC production.
