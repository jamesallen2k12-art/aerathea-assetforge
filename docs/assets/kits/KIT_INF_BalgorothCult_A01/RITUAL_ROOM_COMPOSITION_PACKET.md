# KIT_INF_BalgorothCult_A01 Ritual Room Composition Packet

Task: `AET-MA-20260629-046`
Scope: docs-only composition planning for a future Balgoroth ritual-room placement pass.

This packet orders the current first-pass implemented Balgoroth cult assets and package-ready future props into a room composition contract. It does not authorize map edits, startup placement, DCC source creation, FBX export, Unreal Content changes, runtime source edits, tool creation, source-concept edits, or global index updates.

## Source Contracts

- Parent kit: `docs/assets/kits/KIT_INF_BalgorothCult_A01/PRODUCTION_PACKAGE.md`
- Visual breakdown: `docs/assets/kits/KIT_INF_BalgorothCult_A01/VISUAL_KIT_BREAKDOWN.md`
- Readiness matrix: `docs/assets/kits/KIT_INF_BalgorothCult_A01/IMPLEMENTATION_READINESS_MATRIX.md`
- Implemented floor: `docs/assets/props/SM_INF_CullingTrialFloor_A01/PRODUCTION_PACKAGE.md`, `docs/assets/props/SM_INF_CullingTrialFloor_A01/VISUAL_REVIEW_STATUS.md`
- Implemented arch: `docs/assets/props/SM_INF_HornWingArch_A01/BUILD_IMPORT_STATUS.md`
- Implemented altar and Blueprint: `docs/assets/props/SM_INF_WorthinessAltar_A01/BUILD_IMPORT_STATUS.md`, `docs/assets/blueprints/BP_INF_RitualAltar_A01/BUILD_IMPORT_STATUS.md`
- Implemented sigil source: `docs/assets/props/SM_INF_BalgorothSigil_A01/BUILD_IMPORT_STATUS.md`
- Package-ready future props: `docs/assets/props/SM_INF_BrandingStone_A01/`, `docs/assets/props/SM_INF_AshBasin_A01/`, `docs/assets/props/SM_INF_WitnessChains_A01/`, `docs/assets/props/SM_INF_TrialBanner_A01/`

## Composition Goal

Create a severe, readable Balgoroth worthiness chamber that presents the ritual in this order:

1. A guarded horn-wing threshold establishes cult territory.
2. The culling floor gives the room a clear circular proving zone.
3. The worthiness altar sits as the active judgment focus.
4. Balgoroth sigil language locks the back wall, floor, altar, and dressing identity.
5. Future BrandingStone, AshBasin, WitnessChains, and TrialBanner placements add secondary story beats without blocking movement or overcompeting with the altar.

The room must communicate culling temper, worthiness judgment, and Infernal hierarchy without gore, unreadable glyph text, excessive glow, or dense micro-detail.

## Current Implemented Core

These assets have first-pass implementation or validation evidence and may be referenced by a future map/startup placement task. They are not final art.

| Asset | Current evidence | Composition role | Placement caution |
| --- | --- | --- | --- |
| `SM_INF_CullingTrialFloor_A01` | First-pass DCC/Unreal visual review accepted; startup actor `AET_PROD_INF_CullingTrialFloor_A01`; sockets include `vfx_center`, `vfx_ring_active`, `vfx_rejected_gap`, `snap_altar`, `snap_arch_front`, `stage_spawn`, `stage_blooded`, `stage_elder`. | Central proving floor and room coordinate anchor. | Keep top collision flat. Do not cover the center sigil or active ring with dressing props. Final sculpt, UVs, textures, tuned collision, and expanded floor states remain pending. |
| `SM_INF_HornWingArch_A01` | First-pass DCC/Unreal review complete; startup actor `AET_PROD_INF_HornWingArch_A01`; validated at `650.00h x 660.00w x 220.87d cm` with 10 sockets. | Entry threshold, guarded gate read, first silhouette from approach. | Keep the opening passable and aligned to the floor `snap_arch_front` intent. Final art, tuned collision, VFX states, and optional gate Blueprint behavior remain pending. |
| `SM_INF_WorthinessAltar_A01` and `BP_INF_RitualAltar_A01` | First-pass mesh and native-backed Blueprint wrapper validated; startup actor `AET_PROD_INF_WorthinessAltar_A01`; validated at `356.00h x 404.00w x 346.00d cm`; 9 sockets/components, 6 BrandGlow state materials, and 6 WorthinessJudgment Niagara systems. | Active judgment focal point, interaction and VFX anchor, altar state machine. | Keep `GetInteractFrontLocation()` clear and visible from the proving floor. Final sculpt, UVs, final LODs, tuned collision, final VFX graph polish, and quest/audio/UI implementation remain pending. |
| `SM_INF_BalgorothSigil_A01` | First-pass DCC source/export and Unreal static mesh import validated; no startup placement; focused validation passed at `343.82h x 352.00w x 51.50d cm`, 4 material lanes, 4 sockets. | Shared symbol source for back wall relief, floor insert, altar inset, banner print, and package-ready props. | Treat as implemented source evidence, not an already placed room asset. Future wall/floor placement needs a placement task and collision/sightline validation. |

## Implemented Supporting Dependencies

| Dependency | Current evidence | Composition use | Limitation |
| --- | --- | --- | --- |
| `MI_INF_CultStone_Set_A01` | First-pass Unreal material set implemented and validated: 1 master, 7 material instances. | Shared basalt, scorched red stone, obsidian inset, black iron, bone/horn, ash cloth, and emissive channel language. | Final authored textures and final shader polish are not complete. |
| `MI_INF_BrandGlowStates_A01` | First-pass material-state authoring complete and validated: inactive, smolder, trial active, accepted, rejected, sorcerer focus. | Shared restrained glow states for altar, brand, sigil, and future props. | Final masks, scar normals, pulse logic, and live intensity tuning remain pending. |
| `VFX_INF_WorthinessJudgment_A01` | First-pass template-derived Niagara/material assets validated and assigned to the ritual altar Blueprint. | State read for inactive, smolder, trial active, accepted, rejected, and judgment pulse. | Not final VFX art. Bespoke graph design, fixed-bounds polish, final textures, and density/bloom tuning remain pending. |

## Package-Ready Future Assets

These assets are production-package ready but not implemented unless a later task promotes them. Do not claim DCC source, FBX export, Unreal Content, startup placement, runtime behavior, or final art for these lanes from this packet.

| Future asset | Package status | Intended room role | Placement caution |
| --- | --- | --- | --- |
| `SM_INF_BrandingStone_A01` | Production package and docs-only implementation packet ready. No DCC, export, Unreal import, runtime behavior, VFX graph, or startup placement started. | Side branding/regeneration alcove and future `VFX_INF_RegenerationBrand_A01` socket anchor. | Keep the `interact_brand_side` facing an open side lane. Do not make it a torture machine, portal, or duplicate altar. |
| `SM_INF_AshBasin_A01` | Production package ready. Not implemented. | Low ash/ember dressing near altar edges, witness positions, and branding alcove. | Non-blocking by default. No constant flame, dynamic lights, or heavy smoke. Place outside primary lanes. |
| `SM_INF_WitnessChains_A01` | Production package ready. Not implemented. | Wall/floor witness dressing, restraint implication, broken-chain storytelling. | Non-blocking by default. No physics, gameplay restraint, or per-link collision without approval. Keep tails and wings clear. |
| `SM_INF_TrialBanner_A01` | Production package ready. Not implemented. | Vertical cult read on entry, altar-side walls, witness zones, and den approach. | Static-first. No cloth simulation, readable script, dense fringe, or all-over glow. Keep banners out of the altar interaction cone. |

## Room Zones

Use this as a planning orientation, not a map coordinate claim:

- Front: player approach side through the horn-wing arch.
- Center: culling trial floor and readable ring.
- Rear: altar side, back wall, and optional large sigil relief.
- Left and right: witness, branding, ash, and banner dressing lanes.

| Zone | Primary assets | Purpose | Composition rules |
| --- | --- | --- | --- |
| Zone A: threshold | Implemented `SM_INF_HornWingArch_A01`; future `SM_INF_TrialBanner_A01` | Establish the chamber as Balgoroth territory before the player reaches the floor. | Align arch intent to floor `snap_arch_front`. Preserve the clear opening and keep banners on side planes or rear-side sockets, not in the passage. |
| Zone B: proving ring | Implemented `SM_INF_CullingTrialFloor_A01` | Central arena, trial progress read, Spawn/Blooded/Elder staging. | Keep center symbol and active ring visible from entry and standard gameplay camera. Leave floor grooves collision-flat. |
| Zone C: judgment focus | Implemented `SM_INF_WorthinessAltar_A01` and `BP_INF_RitualAltar_A01` | Runtime interaction, ritual state, accepted/rejected feedback. | Altar front faces the floor center. Interaction volume, UI prompt, and player approach must not be blocked by basins, chains, banners, or wall relief. |
| Zone D: back-wall authority | Implemented source `SM_INF_BalgorothSigil_A01`; future placement only | High hierarchy read behind the altar. | Use one large horned crown/split-wing symbol if approved. Avoid stacking multiple competing symbols behind the altar core. |
| Zone E: witness walls | Future `SM_INF_WitnessChains_A01`, future `SM_INF_TrialBanner_A01` | Oppressive side dressing and spectator punishment read. | Keep chains and banners on side walls or anchors. Default to no collision. Do not let hanging ends intrude into wing/tail lanes. |
| Zone F: branding alcove | Future `SM_INF_BrandingStone_A01`, optional future `SM_INF_AshBasin_A01` | Secondary ritual station for body-brand and regeneration setup. | Place off the main axis so it reads from the altar but does not split the focal hierarchy. Keep its interaction side clear. |
| Zone G: ash and cooldown dressing | Future `SM_INF_AshBasin_A01` | Low ember/ash story beats and ritual cooldown tone. | Use sparse basin placement at corners, altar sides, or witness edges. No constant smoke column or bright flame that competes with WorthinessJudgment. |

## Sightline And Readability Rules

- Entry sightline: from the arch, the player should read the floor ring first, the altar second, and the back-wall sigil third.
- Gameplay camera: the floor center, altar core, and rejected-gap area must remain visible from common three-quarter camera angles.
- Startup/review camera: any future visual review must not show underside, side-on plane, clipped arch, blank VFX, proxy geometry, or scale mismatch.
- Focal hierarchy: the altar and floor own active VFX. Future basins, banners, chains, and branding stone should remain lower brightness and lower motion.
- Symbol control: use one dominant Balgoroth mark per major sightline. Do not repeat many small sigils in a way that reads as noise.
- UI prompt clearance: prompts anchored at `GetInteractFrontLocation()` must not cover the altar core, floor center sigil, or active ring link.
- VFX path read: trial flow should read as ring to altar core to verdict point. Accepted feedback routes toward `GetBrandTransferLocation()`. Rejected feedback routes toward `GetRejectedGapLocation()`.
- Scale reference: preserve readability beside a 180 cm humanoid, 70-90 cm Lesser staging, and 274 cm adult Infernal with horns, folded wings, and tail.

## Interaction Flow Contract

This section references the existing `BP_INF_RitualAltar_A01` runtime contract only. It does not lock final quest text, rewards, failure penalties, backend authority, multiplayer behavior, combat interruption rules, UI art, or audio assets.

| Flow step | Room read | Existing or future contract |
| --- | --- | --- |
| Approach | Player passes or faces the horn-wing arch, seeing the floor ring and altar ahead. | Future map placement should preserve threshold to floor to altar alignment. |
| Discovery | Player enters altar focus/discovery range. | Future gameplay layer may emit `QEvent.INF.WorthinessAltar.Discovered` from the binding packet. |
| Prompt | Player focuses the altar while it is `Smolder` or approved `Inactive`. | UI must anchor to `GetInteractFrontLocation()` and show one prompt only. |
| Trial start | `StartTrial()` enters `TrialActive`. | Floor ring, altar core, and `GetRingLinkLocation()` should be the visible feedback chain. |
| Trial progress | `AdvanceRitual()` updates `TrialProgress`. | Do not add room dressing that blocks the floor ring or altar progress read. |
| Judgment pulse | Trial completion or `TriggerJudgmentPulse()` enters `JudgmentPulse`. | No reward, completion, or final verdict should be granted on pulse alone. |
| Verdict accepted | `AcceptSacrifice(Intensity)` enters `Accepted`. | Accepted feedback should read warm and focused at `GetBrandTransferLocation()`. Future BrandingStone can echo this only after implementation approval. |
| Verdict rejected | `RejectSacrifice(Intensity)` enters `Rejected`. | Rejected feedback should be a short violet-red snap at `GetRejectedGapLocation()`, not room-wide constant glow. |
| Cooldown/reset | `Cooldown` returns to `Smolder` or `ResetRitual()` clears transient state. | Retry, penalties, cancellation, out-of-range rules, and quest outcomes remain approval-gated. |

## Collision And Navigation Lanes

Future map placement should validate these lanes before visual approval:

- Primary lane: arch opening to floor center to altar interaction front stays clear for a player capsule and 274 cm Infernal review scale. Use the arch validated opening and avoid placing basins, chains, banner poles, or sigil relief inside this lane.
- Ring lane: keep an open circulation band around the culling floor so wing and tail characters can rotate without snagging on low props, raised rim collision, or side dressing.
- Interaction cone: keep the altar's front locator, interaction volume, and sacrifice/brand-transfer locators unobstructed. Dressing may frame this cone but must not cross it.
- Side lanes: witness chains, banners, ash basins, and branding stone belong along side walls or alcoves. Default collision should be none or simple low-profile collision.
- Vertical clearance: hanging banners and suspended chains must clear adult Infernal horns and folded wing silhouettes unless they are deliberately placed on walls outside travel paths.
- Floor collision: the culling floor top remains flat and simple. Ritual grooves, emissive channels, and sigil relief do not create holes or capsule traps.
- Arch collision: use simple left/right/top span blockers and keep the central passage open unless a future approved gate Blueprint intentionally blocks it.
- Sigil collision: wall relief should be no collision or simple non-complex collision only. Floor insert variants must be flat if walkable.
- No complex-as-simple collision should be introduced for final gameplay without a specific approved exception.

## Future Placement Order

1. Verify the implemented core in the target map task: floor, arch, altar Blueprint, material state dependencies, and WorthinessJudgment assignment.
2. Align the arch to the floor approach and the altar to the floor `snap_altar` intent before adding dressing.
3. Add a single large Balgoroth sigil wall/floor/altar placement only after a placement task owns map edits and collision review.
4. Promote and implement `SM_INF_BrandingStone_A01` before treating the branding alcove as usable in Unreal.
5. Add `SM_INF_AshBasin_A01`, `SM_INF_WitnessChains_A01`, and `SM_INF_TrialBanner_A01` last as non-blocking dressing after their DCC/Unreal lanes exist.
6. Run focused composition, collision, startup/map, VFX, and runtime validators before any final visual approval.

## Future Validator Needs

A later implementation task should add focused validators only when it owns the relevant files. Suggested future validator names are contracts, not created by this packet.

| Validator need | Suggested future check |
| --- | --- |
| Composition placement | `Tools/Unreal/validate_infernal_balgoroth_ritual_room_composition.py` verifies expected actor names, asset paths, snap intent, no duplicate focal assets, and implemented/package-ready status claims. |
| Map/startup guardrail | Confirms only the assigned map or startup scene changed, and only after a placement task explicitly owns that file. |
| Sightline review | Confirms floor ring, altar core, arch opening, and optional back-wall sigil are visible from approved review cameras with no clipping, side-on framing, underside view, or scale mismatch. |
| Collision lane scan | Confirms arch-to-altar lane, ring circulation, interaction cone, and side alcoves are clear; dressing props are non-blocking unless explicitly approved. |
| Runtime altar contract | Reuses `validate_infernal_ritual_altar_blueprint.py` and `validate_infernal_ritual_altar_timing_traces.py` for state, locator, and timing stability. |
| VFX restraint | Reuses WorthinessJudgment and BrandGlow polish validators to keep glow sparse, state-driven, bounded, and not overbright. |
| Future prop imports | Adds focused validators for BrandingStone, AshBasin, WitnessChains, and TrialBanner only after their DCC/Unreal lanes are assigned. |
| Stale docs prevention | Scans this packet and package docs so package-ready assets are not described as implemented before evidence exists. |

## Approval Gates

Stop for lead/user approval before:

- Editing any map or startup scene.
- Creating or modifying DCC source, FBX exports, Unreal Content, runtime source, or tool scripts.
- Placing `SM_INF_BalgorothSigil_A01` in a scene.
- Promoting BrandingStone, AshBasin, WitnessChains, TrialBanner, or RegenerationBrand from package-ready to DCC/Unreal implementation.
- Adding final quest text, reward rules, failure penalties, item costs, health sacrifice rules, persistence, party credit, multiplayer authority, or backend/analytics schema.
- Implementing final UI art, prompt copy, localization, controller prompts, audio middleware, final audio assets, or voice/subtitle work.
- Authoring final WorthinessJudgment Niagara graphs or increasing VFX intensity beyond the validated BrandGlow/Worthiness contracts.
- Claiming final visual approval for the room.

## Quality Gate Checklist

- Implemented assets are separated from package-ready future assets.
- No package-ready future asset is described as having DCC source, FBX export, Unreal import, runtime behavior, or startup placement.
- Room zones preserve the Balgoroth hierarchy: threshold, proving floor, altar, sigil authority, side dressing.
- Sightlines keep floor ring, altar core, and verdict feedback readable.
- Collision lanes protect arch passage, floor circulation, altar interaction, and wing/tail clearance.
- Glow remains sparse and state-driven.
- No gore, copied symbols, readable glyph text, dense micro-detail, constant smoke, or excessive particles are required.
- Future validators and approval gates are explicit.
- This packet remains documentation only.
