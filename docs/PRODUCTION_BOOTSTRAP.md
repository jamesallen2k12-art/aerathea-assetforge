# Aerathea Production Bootstrap

## Current Editor Route

Use the X11 SM5 launcher for manual editor work:

`/home/Flamestrike/Projects/Aerathea/Tools/Unreal/launch_aerathea_editor_exact_sm5.sh`

This route is the current stable manual-edit baseline:

- Plasma X11 session.
- Vulkan SM5.
- Bindless disabled.
- RHI thread disabled during bootstrap.
- Lumen GI/reflections disabled in project settings during bootstrap.
- Startup map loaded from `Config/DefaultEngine.ini`: `/Game/Aerathea/Maps/L_Aerathea_Startup`.
- Verified clean close and relaunch on 2026-06-24.

Keep SM6 available for command-line validation and future rendering work, but do not make SM6 the daily Linux editor path until the presentation/device-loss issue is resolved.

## Existing Content Roots

The project content root is `Content/Aerathea`.

Initial production folders:

- `Blueprints`
- `Buildings`
- `Characters`
- `Creatures`
- `Developer`
- `Maps`
- `Materials`
- `Props`
- `UI`
- `VFX`

Use Unreal Editor for binary asset creation and saving. Use filesystem edits for scripts, docs, source, config, and launcher tooling.

## Startup Scene Status

The initial controlled Aerathea test scene exists in:

`/Game/Aerathea/Maps/L_Aerathea_Startup`

Current verified contents:

- 5x5 production ground-tile review area using `SM_AET_ModularGroundTile_A01`.
- Player, gnome, and minotaur scale markers.
- Production target dummy using `SM_AET_TargetDummy_A01`.
- Production portal review actor using `AAETPortalActor`, imported `SM_AET_PortalArch_A01`, and restrained Aetherium core material.
- Mekgineer workshop crate using `SM_MKG_WorkshopPropCrate_A01`.
- Gnome armory review props:
  - `SM_MKG_AetherKnife_A01`
  - `SM_MKG_AetherCoreUnit_A01`
  - `SM_MKG_SparkPistol_A01`
  - `SM_MKG_AetheriumGrenade_A01`
- Directional light, sky light, overview camera, and scene label.
- Base materials:
  - `M_AET_Stone_Handpainted_A01`
  - `M_AET_Timber_Handpainted_A01`
  - `M_AET_DarkIron_A01`
  - `M_AET_Brass_A01`
  - `M_AET_AetheriumGlow_Blue_A01`

Validation:

- `Tools/Unreal/bootstrap_startup_scene.py` builds/saves the startup scene.
- `Tools/Unreal/import_first_slice_assets.py` imports Blender-authored FBX exports and updates the startup scene.
- `Tools/Unreal/validate_startup_scene.py` verifies 19 expected assets, 15 expected actor labels, 25 production ground tiles, static mesh material slots, and the portal actor class.
- GUI map check result: `0 Error(s), 0 Warning(s)`.

Do not run `MAP CHECK` from the headless Python commandlet on UE 5.8; that path produced a native commandlet crash in `UEditorEngine::Map_Check`. Use the validator for headless checks and the GUI editor for map check.

## First Playable Visual Slice

Build a small, controlled Aerathea asset cluster before broad production. The goal is to prove the visual style, import rules, collision scale, material setup, LOD rules, and editor stability.

Asset index:

`docs/assets/ASSET_INDEX.md`

Production backlog:

- `docs/assets/PRODUCTION_BACKLOG.md`
- `docs/assets/ASSET_CONCEPTS_MANIFEST.md`
- Source concept folder: `/home/Flamestrike/Desktop/Aerathea/Aerathea Creative/ASSET CONCEPTS`
- Codex skill: `/home/Flamestrike/.codex/skills/aerathea-production-intake`

Current first-slice status:

- Blender 5.1.1 starts after downgrading Fedora `materialx` to `1.39.4-5.fc44`.
- Blender `.blend` sources and FBX exports exist for the first-slice target dummy, portal arch, modular ground tile, Mekgineer crate, and four Gnome armory child assets.
- `SM_AET_TargetDummy_A01`, `SM_AET_PortalArch_A01`, `SM_AET_ModularGroundTile_A01`, and `SM_MKG_WorkshopPropCrate_A01` are imported to Unreal and placed in the startup scene.
- `BP_AET_Portal_A01` is reparented to `AAETPortalActor`; the startup review actor uses the native C++ portal class to avoid a UE 5.8 Linux commandlet crash in Blueprint object placement.
- The startup scene includes a review camera, PlayerStart, fill light, and `AAETReviewCameraDirector` so X11/Vulkan game-mode captures use a stable production-asset view.
- `SM_MKG_AetherKnife_A01`, `SM_MKG_AetherCoreUnit_A01`, `SM_MKG_SparkPistol_A01`, and `SM_MKG_AetheriumGrenade_A01` have production packages, modeling handoffs, Blender sources, FBX exports, Unreal imports, startup placements, and passing validation.
- `KIT_MKG_Armory_A01`, `KIT_DWR_Armory_A01`, `KIT_ELV_Armory_A01`, `KIT_DEL_Armory_A01`, `KIT_ORC_Arsenal_A01`, `KIT_MIN_Arsenal_A01`, and `KIT_DKH_FieldGear_A01` have child intake and/or kit production packages ready.
- `SK_GNM_Base_A01` has the first race body production package ready.
- The wider `ASSET CONCEPTS` folder contains 289 PNG source concept files. Some are collages/catalogs, so the final asset count is higher than 289 after child-asset expansion.

Next priority order:

1. Create remaining Gnome armory child production packages from `KIT_MKG_Armory_A01`.
2. Create priority child packages from the Dwarven, Elven, Dark Elven, Orc, Minotaur, and Drakhar kit packages.
3. Create `SK_GNM_Base_A01` concept sheet/modeling handoff, then build the first gnome body source mesh and skeleton.
4. Implement final `BP_AET_Portal_A01` trigger/VFX/audio/destination behavior after portal gameplay rules are approved.
5. Add `BP_AET_TargetDummy_A01` behavior after combat/damage test rules are approved.
6. Create the first settlement modular package, either `SM_AET_Palisade_A01` or `SM_AET_House_A01`.
7. Create the first creature package, likely `SK_CRE_Gryphon_A01`.
8. Continue collage-aware intake on the remaining `ASSET CONCEPTS` categories.

## First Asset Production Rule

Do not jump straight to final art. For each production asset:

1. Approve the art direction summary.
2. Generate concept prompts or references.
3. Convert the chosen direction into a production sheet.
4. Build or import a mid-poly asset.
5. Apply texture/material plan.
6. Configure LODs and collision.
7. Validate in `L_Aerathea_Startup`.

## Source Control Status

- Local source control has been initialized on branch `main`.
- Baseline commit created: `5c018cb9f4ceb8d460482472f9716fe102ddbdd9`.
- First-slice production package commit created: `482f953`.
- No remote is configured yet.
- Preserve the current `.keep` placeholder files in empty content folders until real Unreal assets occupy those directories.
