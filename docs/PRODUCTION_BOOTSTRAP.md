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

- Grounded test area.
- Player, gnome, and minotaur scale markers.
- Portal-arch blockout with restrained Aetherium glow core.
- Target-dummy blockout.
- Directional light, sky light, overview camera, and scene label.
- Base materials:
  - `M_AET_Stone_Handpainted_A01`
  - `M_AET_Timber_Handpainted_A01`
  - `M_AET_DarkIron_A01`
  - `M_AET_Brass_A01`
  - `M_AET_AetheriumGlow_Blue_A01`

Validation:

- `Tools/Unreal/bootstrap_startup_scene.py` builds/saves the startup scene.
- `Tools/Unreal/validate_startup_scene.py` verifies 6 expected assets and 14 expected actors.
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

- Concept reference sheets generated for the first target dummy, portal arch, portal blueprint states, Mekgineer crate, and modular ground tile.
- `SM_AET_TargetDummy_A01` has a dedicated modeling handoff and is the first DCC production candidate.
- `SM_AET_TargetDummy_A01` build/import is blocked on an approved DCC mesh; do not substitute a procedural placeholder for the production asset.
- `SM_AET_PortalArch_A01`, `SM_AET_ModularGroundTile_A01`, and `SM_MKG_WorkshopPropCrate_A01` now have dedicated modeling handoffs.
- `BP_AET_Portal_A01` has an implementation handoff, but final Blueprint validation is blocked until `SM_AET_PortalArch_A01` is imported.
- `KIT_MKG_Armory_A01` has a kit package and child asset intake from `Gnome Armory.png`.
- Remaining first-slice concept references still need final visual approval before their DCC handoff files are treated as locked.
- The wider `ASSET CONCEPTS` folder contains 289 PNG source concept files. Some are collages/catalogs, so the final asset count is higher than 289 after child-asset expansion.

Next priority order:

1. Approve or revise the generated first-slice concept references:
   - `SM_AET_TargetDummy_A01`
   - `SM_AET_PortalArch_A01`
   - `BP_AET_Portal_A01`
   - `SM_MKG_WorkshopPropCrate_A01`
   - `SM_AET_ModularGroundTile_A01`
2. Build/import `SM_AET_TargetDummy_A01` as the first production mesh and replace the startup blockout.
3. Build/import `SM_AET_PortalArch_A01`, then create `BP_AET_Portal_A01` around it.
4. Build/import `SM_AET_ModularGroundTile_A01` and replace or supplement the startup ground plane.
5. Build/import `SM_MKG_WorkshopPropCrate_A01` for the first Mekgineer prop language test.
6. Validate each asset with collision, material slot count, LOD0-LOD3 plan, and map check.
7. Add a simple player-start/camera review flow once the first meshes exist.
8. Continue collage-aware intake on `ASSET CONCEPTS`, starting with the remaining armory sheets after `Gnome Armory.png`.

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
