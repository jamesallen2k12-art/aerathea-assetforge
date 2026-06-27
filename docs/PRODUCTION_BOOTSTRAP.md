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
- Production target dummy using `BP_AET_TargetDummy_A01`, backed by `SM_AET_TargetDummy_A01`.
- Production portal review actor using `AAETPortalActor`, imported `SM_AET_PortalArch_A01`, and restrained Aetherium core material.
- Mekgineer workshop crate using `SM_MKG_WorkshopPropCrate_A01`.
- Gnome armory review props:
  - `SM_MKG_AetherKnife_A01`
  - `SM_MKG_AetherCoreUnit_A01`
  - `SM_MKG_SparkPistol_A01`
  - `SM_MKG_AetheriumGrenade_A01`
  - `SM_MKG_RatchetCleaver_A01`
  - `SM_MKG_GearMace_A01`
  - `SM_MKG_MonkeyWrench_A01`
  - `SM_MKG_SpikeDrill_A01`
  - `SM_MKG_ToolPack_A01`, preview-fit to `SK_GNM_Base_A01` at `back_pack`
- Palisade modular review set:
  - `SM_AET_Palisade_Wall_A01`
  - `SM_AET_Palisade_Post_A01`
  - `SM_AET_Palisade_Corner_A01`
  - `SM_AET_Palisade_Gate_A01`
  - `SM_AET_Palisade_EndCap_A01`
- Ogre cairn fortification review module:
  - `SM_OGR_CairnBattleGate_A01`
- First-pass skeletal imports:
  - `SK_GNM_Base_A01`, `SK_GNM_Base_A01_Skeleton`, and `PHYS_GNM_Base_A01`
  - `SK_GNM_HeavyMek_Rivalry_A01`, `SK_GNM_HeavyMek_Rivalry_A01_Skeleton`, `PHYS_GNM_HeavyMek_Rivalry_A01`, and `ABP_GNM_HeavyMek_Rivalry_A01`
  - `SK_OGR_Warrior_Rival_A01`, `PHYS_OGR_Warrior_Rival_A01`, and `ABP_OGR_Warrior_Rival_A01`
  - `SK_CRE_Gryphon_A01`, `SK_CRE_Gryphon_A01_Skeleton`, `PHYS_CRE_Gryphon_A01`, and `SK_CRE_Gryphon_A01_Anim`
  - `SK_INF_Base_Compact_A01`, `SK_INF_Base_Tall_A01`, generated skeletons, physics assets, and ABP placeholders
  - `SK_INF_Lesser_Spawn_A01`, `SK_INF_Lesser_1stKill_A01`, `SK_INF_Lesser_Blooded_A01`, `SK_INF_Lesser_Elder_A01`, `SK_INF_Lesser_Ancient_A01`, generated skeletons, physics assets, and ABP placeholders
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
- `Tools/Unreal/validate_startup_scene.py` verifies 97 expected assets, 41 expected actor labels, 25 production ground tiles, static/skeletal material slots, generated LOD sets, skeletal and static mesh sockets, skeletal physics asset assignments, animation Blueprint placeholders, runtime-visible production components, intentionally hidden collision helper volumes, the ToolPack `back_pack` socket-fit preview, and the portal/target dummy actor classes.
- GUI map check result: `0 Error(s), 0 Warning(s)`.

Do not run `MAP CHECK` from the headless Python commandlet on UE 5.8; that path produced a native commandlet crash in `UEditorEngine::Map_Check`. Use the validator for headless checks and the GUI editor for map check.

## First Playable Visual Slice

Build a small, controlled Aerathea asset cluster before broad production. The goal is to prove the visual style, import rules, collision scale, material setup, LOD rules, and editor stability.

Visual review rule:

- Before presenting any Unreal visual approval, compare the live Unreal view against the source concept or DCC proof image.
- Match orientation, camera pitch/yaw, framing, and production scale before asking for approval.
- Use `Tools/Unreal/capture_startup_review_offscreen.sh` for automated startup captures; do not use a visible `-game` capture window unless explicitly needed, because it can capture the mouse.
- The canonical runtime review camera is `X=4710, Y=-2880, Z=2575`, aimed at `X=-70, Y=160, Z=110`, FOV 65. This is the Unreal-side orientation that visually matches the DCC proof after Blender-to-Unreal axis conversion.
- When orientation is uncertain, render the A/B/C/D/E marker gate before presenting:
  - DCC proof: `AET_REVIEW_MARKERS=1 blender --background --python Tools/DCC/render_startup_review.py`
  - Unreal proof: `AET_REVIEW_MARKERS=1 Tools/Unreal/capture_startup_review_offscreen.sh`
  - Marker validation: `/home/Flamestrike/UnrealEngine/UE_5.8.0/Engine/Binaries/Linux/UnrealEditor-Cmd /home/Flamestrike/Projects/Aerathea/Aerathea.uproject -NullRHI -NoRHIThread -NoSplash -Unattended -nop4 -ExecutePythonScript=/home/Flamestrike/Projects/Aerathea/Tools/Unreal/validate_review_alignment_markers.py`
- The accepted marker orientation is A on the right, B front/lower, C left, D back/upper, and E elevated above the plane for the current review camera. Rerun the normal Unreal capture without `AET_REVIEW_MARKERS` before presenting an approval image.
- If the view shows an underside, side-on plane, frustum/proxy geometry, clipped structure, or a scale mismatch, treat the review as failed and fix the camera/import path first.
- Use `Tools/Unreal/validate_startup_scene.py` and, when needed, `Tools/Unreal/diagnose_startup_review_view.py` before presenting the viewport.

Asset index:

`docs/assets/ASSET_INDEX.md`

Production backlog:

- `docs/assets/PRODUCTION_BACKLOG.md`
- `docs/assets/ASSET_CONCEPTS_MANIFEST.md`
- Source concept folder: `/home/Flamestrike/Desktop/Aerathea/Aerathea Creative/ASSET CONCEPTS`
- Codex skill: `/home/Flamestrike/.codex/skills/aerathea-production-intake`

Current first-slice status:

- Blender 5.1.1 starts after downgrading Fedora `materialx` to `1.39.4-5.fc44`.
- Blender `.blend` sources and FBX exports exist for the first-slice target dummy, portal arch, modular ground tile, Mekgineer crate, eleven Gnome armory child assets, the palisade module set, the first gnome base body, the first gryphon blockout, the first Infernal adult/Lesser lifecycle scale review set, and `SM_INF_CullingTrialFloor_A01`.
- `SM_AET_TargetDummy_A01`, `SM_AET_PortalArch_A01`, `SM_AET_ModularGroundTile_A01`, and `SM_MKG_WorkshopPropCrate_A01` are imported to Unreal and placed in the startup scene.
- `BP_AET_Portal_A01` is reparented to `AAETPortalActor`; native preview state, focus overlap, use-request cooldown, and destination validation are implemented while final traversal remains deferred.
- `BP_AET_TargetDummy_A01` exists, compiles from `AAETTargetDummyActor`, provides training hit/break/reset events, and now owns the startup target dummy actor.
- The startup scene includes a review camera, PlayerStart, fill light, and `AAETReviewCameraDirector` so X11/Vulkan offscreen game-mode captures use a stable production-asset view.
- Hidden `AET_REVIEW_MARKER` A/B/C/D/E debug actors are present for orientation checks and are only shown during marker captures.
- `SM_MKG_AetherKnife_A01`, `SM_MKG_AetherCoreUnit_A01`, `SM_MKG_SparkPistol_A01`, `SM_MKG_AetheriumGrenade_A01`, `SM_MKG_RatchetCleaver_A01`, `SM_MKG_GearMace_A01`, `SM_MKG_MonkeyWrench_A01`, `SM_MKG_SpikeDrill_A01`, `SM_MKG_ToolPack_A01`, and `SM_MKG_MultiTool_A01` have production packages, modeling handoffs, Blender sources, FBX exports, Unreal imports, startup placements or socket-fit previews, and passing validation.
- `KIT_MKG_Armory_A01` has all catalog child production packages and handoffs documented; first eleven child DCC meshes are imported and placed or fit-previewed, including `SM_MKG_GrappleHook_A01` with muzzle/beam/cable sockets.
- `KIT_GNM_OGR_RivalryEncounter_A01` first children include the approved first-pass `BP_GNM_HeavyMekShieldwall_A01`, `SM_GNM_AetherShieldProjector_A01`, strengthened segmented `SM_GNM_AetherShieldWall_A01`, `VFX_GNM_AetherShieldWall_A01`, `SK_OGR_Teknomancer_A01`, `SK_GNM_HeavyMek_Rivalry_A01`, `SK_OGR_Warrior_Rival_A01`, and `SM_OGR_CairnBattleGate_A01` review implementations with startup review placement. The kit also has package-ready `SK_OGR_Shaman_A01`, `SK_OGR_Necromancer_A01`, `SK_CRE_Manticore_A01`, `SK_CRE_Manticore_Interrupt_A01`, `SM_OGR_CrudeTekPylon_A01`, and `BP_GNM_OGR_BattlefieldEncounter_A01` planning slices. The shieldwall native Blueprint/VFX contract now supports state material switching, impact-location control, and validated scalar parameters.
- `SK_OGR_Teknomancer_A01` has a first-pass class-fit Blender source, FBX export, Unreal skeletal mesh import, material instances, LOD0-LOD3, sockets, physics asset, ABP placeholder, and startup review placement. Final sculpt, shared Ogre skeleton fit, authored textures, tuned physics, and animation remain pending.
- `SK_GNM_HeavyMek_Rivalry_A01` has a first-pass Blender source, FBX export, Unreal skeletal mesh import, material instances, LOD0-LOD3, Mek/VFX sockets, physics asset, ABP placeholder, and startup review placement. Final sculpt, retopo, UVs/textures, tuned physics, and animation remain pending.
- `SK_OGR_Warrior_Rival_A01` has a first-pass Blender source, FBX export, Unreal skeletal mesh import, material instances, LOD0-LOD3, shield/hammer/VFX sockets, physics asset, ABP placeholder, and startup review placement. Final sculpt, shared Ogre rig fit, UVs/textures, tuned physics, and animation remain pending.
- `SK_OGR_Shaman_A01` and `SK_OGR_Necromancer_A01` have production packages, modeling handoffs, build/import status files, source reference reviews, material plans, LOD plans, collision notes, sockets, and animation hooks ready. DCC builds are not started.
- `SM_OGR_CairnBattleGate_A01` has a first-pass Blender source, FBX export, Unreal static mesh import, cairn stone material base, material instances, LOD0-LOD3, static mesh sockets, simple collision, startup review placement, passing validation, and offscreen capture coverage. Final sculpt, UVs/textures, tuned collision, modular variants, and Blueprint gate behavior remain pending.
- `KIT_OGR_Teknomancy_A01` has a production package and child intake ready. `SM_OGR_CrudeTekPylon_A01` has a production package, modeling handoff, build/import status, material plan, socket plan, collision plan, LOD plan, and future Blueprint state notes ready. DCC build is not started.
- `BP_GNM_OGR_BattlefieldEncounter_A01` has a production package, implementation handoff, build/import status, dependency contract, phase-state plan, actor slots, collision volumes, variables, events, and optional-branch gates ready. Blueprint asset is not created.
- `SK_CRE_Manticore_A01` has a base production package, source concept intake, modeling handoff, build/import status, skeleton/proportion plan, material plan, LOD plan, collision plan, and sockets ready for approval. DCC build is not started.
- `SK_CRE_Manticore_Interrupt_A01` has an encounter-variant production package, modeling handoff, and build/import status ready for the Gnome/Ogre interrupt source. DCC build waits for base `SK_CRE_Manticore_A01` approval/import.
- `KIT_DWR_Armory_A01`, `KIT_ELV_Armory_A01`, `KIT_DEL_Armory_A01`, `KIT_ORC_Arsenal_A01`, `KIT_MIN_Arsenal_A01`, and `KIT_DKH_FieldGear_A01` have child intake and kit production packages ready, and their first priority child package docs are complete; DCC builds for those children are still pending.
- `SK_GNM_Base_A01` has a first-pass DCC review body, skeleton, Unreal skeletal mesh import, material instances, generated LOD0-LOD3, gear/VFX socket landmarks, assigned physics asset, animation Blueprint placeholder, and passing validation. Final sculpt, retopo, UVs, textures, tuned physics, and full animation set remain production work.
- `SM_AET_Palisade_A01` has wall/post/corner/gate/end-cap Blender sources, FBX exports, Unreal imports, startup placements, simple UCX collision, material instances, generated LOD0-LOD3, and passing validation.
- `SK_CRE_Gryphon_A01` has a first-pass DCC review mesh, skeleton, Unreal skeletal mesh import, material instances, generated LOD0-LOD3, creature socket landmarks, assigned physics asset, animation Blueprint placeholder, imported wing-spread animation blockout, and passing validation. Final sculpt, skinning, UVs, tuned physics bodies, and full animation set remain production work.
- `SK_INF_Base_A01` and `SK_INF_Lesser_A01` have approved first-pass DCC review meshes, FBX exports, Unreal skeletal mesh imports, material instances, generated LOD0-LOD3, claw/tail/wing/VFX sockets, assigned physics assets, animation Blueprint placeholders, startup scale placements, an offscreen Infernal scale review capture at `Saved/Automation/StartupReview/AeratheaStartupReview_InfernalScale_A01.png`, final adult body-band art direction, and a Lesser lifecycle stage sheet. `KIT_INF_BalgorothCult_A01` now has a visual kit breakdown; `SM_INF_CullingTrialFloor_A01` has Blender source, FBX export, Unreal static mesh import, material instances, LOD0-LOD3, static mesh sockets, local startup placement validation, and first-pass visual review accepted; `MI_INF_BrandGlowStates_A01` and `VFX_INF_WorthinessJudgment_A01` have production packages ready. Final sculpt, retopo, UVs, textures, tuned wing/tail physics, class or lifecycle animation sets, and authored cult material/VFX assets remain production work.
- The wider `ASSET CONCEPTS` folder contains 547 source concept files: 546 PNG files and 1 JPG file. Some are collages/catalogs, so the final asset count is higher than 547 after child-asset expansion. The latest 2026-06-27 addendum routes 63 Infernal/Balgoroth references, 21 Gnome-vs-Ogre encounter references, and 4 Gnome heavy Mek variants.

Next priority order:

1. Use `Tools/Unreal/launch_startup_review_editor.sh` when an interactive manual inspection is needed; focus on silhouette, scale, material readability, collision fit, sockets, and LOD transitions.
2. Review the updated startup scene with `SM_MKG_GrappleHook_A01`, `BP_GNM_HeavyMekShieldwall_A01`, `SK_OGR_Teknomancer_A01`, and `SK_GNM_HeavyMek_Rivalry_A01` visible together.
3. Continue the approved Gnome/Ogre rivalry follow-up sequence: final authored shieldwall Niagara art.
4. Resolve the first-pass `SK_OGR_Teknomancer_A01` shared Ogre skeleton warning during the final rig pass.
5. Replace first-pass review meshes with approved art-model geometry, final UVs, authored texture sets, and tuned collision after the relevant final art directions are approved.
6. Tune gnome and gryphon physics bodies, sockets, and animation Blueprint logic into real locomotion/attachment tests after approved final sculpt, skin, and animation direction is available.
7. Review and approve one proposed Abyss/Anathema child from `KIT_ABY_ShadowFlame_A01` before any DCC build.
8. Implement final `BP_AET_Portal_A01` traversal/VFX/audio/destination behavior after portal gameplay rules are approved.
9. Continue collage-aware intake on the remaining `ASSET CONCEPTS` categories.

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
