# BP_AET_Portal_A01 Implementation Handoff

## Purpose

Create the first production-ready Blueprint slice for the Aerathea portal landmark in `L_Aerathea_Startup`.

This handoff covers `BP_AET_Portal_A01` and its required arch dependency, `SM_AET_PortalArch_A01`. The slice should prove Blueprint composition, portal visual states, material/VFX state control, collision, interaction overlap, and startup-map replacement without implementing final traversal.

Do not make travel, teleport, quest, inventory, progression, or unlock behavior client-authoritative in this slice.

## Source References

- Blueprint package: `docs/assets/blueprints/BP_AET_Portal_A01/PRODUCTION_PACKAGE.md`
- Portal arch package: `docs/assets/props/SM_AET_PortalArch_A01/PRODUCTION_PACKAGE.md`
- Portal state sheet: `docs/assets/blueprints/BP_AET_Portal_A01/concepts/BP_AET_Portal_A01_state_sheet_A01.png`
- Portal arch concept sheet: `docs/assets/props/SM_AET_PortalArch_A01/concepts/SM_AET_PortalArch_A01_concept_sheet_A01.png`
- Startup map target: `/Game/Aerathea/Maps/L_Aerathea_Startup`

## Production Target

- Blueprint asset: `BP_AET_Portal_A01`
- Unreal path: `/Game/Aerathea/Blueprints/Props/BP_AET_Portal_A01`
- Required static mesh: `/Game/Aerathea/Props/Portal/SM_AET_PortalArch_A01`
- Required arch materials:
  - `/Game/Aerathea/Materials/Props/Portal/MI_AET_PortalArch_A01_Stone`
  - `/Game/Aerathea/Materials/Props/Portal/MI_AET_PortalArch_A01_Accent`
- Required portal core material: `/Game/Aerathea/Materials/Props/Portal/MI_AET_PortalCore_A01`
- Optional future Niagara system: `/Game/Aerathea/VFX/Portal/NS_AET_PortalIdle_A01`
- Optional future audio cue: `A_AET_PortalHum_A01` or equivalent approved portal hum cue

Initial slice behavior:

- Spawn as idle active by default.
- Show inactive, idle active, focused, and use-requested visual states.
- Overlap pawn interaction volume.
- Log or broadcast interaction intent only.
- Never perform final travel or teleport.

## Dependency Gate

`SM_AET_PortalArch_A01` is the hard dependency for a production Blueprint pass.

Before building the final Blueprint actor, confirm:

- Static mesh exists at `/Game/Aerathea/Props/Portal/SM_AET_PortalArch_A01`.
- Mesh scale matches the package target: 420 cm high, 360 cm wide, 90 cm deep.
- Pivot is bottom center at ground contact.
- Forward axis faces +X unless the level convention changes.
- Portal aperture is about 190 cm wide x 300 cm tall.
- LOD0-LOD3 are imported or generated and inspected.
- Runtime collision uses simple primitives, not complex-as-simple.
- Collision leaves the portal opening walkable unless a later gameplay spec requires blocking.
- Material slot count is 2 target, 3 maximum only if emissive inserts require it.
- Arch materials are assigned and preserve chunky stone, dark iron, brass, and restrained Aetherium language.

If the mesh is not imported, the Blueprint may be scaffolded with a temporary editor-only placeholder, but the slice is blocked from final validation, map replacement, collision approval, aperture alignment, and performance signoff.

## Blueprint Components

Use these components in `BP_AET_Portal_A01`:

| Component | Type | Parent | Required Setup |
| --- | --- | --- | --- |
| `DefaultSceneRoot` | Scene Component | None | Actor origin at arch bottom center. |
| `SM_PortalArch` | Static Mesh Component | `DefaultSceneRoot` | Assign `SM_AET_PortalArch_A01`; scale `1.0`; use imported collision. |
| `SM_PortalCore` | Static Mesh Component or plane mesh | `DefaultSceneRoot` or `SM_PortalArch` | Center in aperture; about 170 cm wide x 280 cm high; no collision; assign dynamic instance of `MI_AET_PortalCore_A01`. |
| `InteractionVolume` | Box Component or Sphere Component | `DefaultSceneRoot` | Overlap pawn only; radius target 175 cm or box equivalent; height target 260 cm. |
| `VFX_PortalIdle` | Niagara Component | `DefaultSceneRoot` | Optional; disabled if Niagara dependency is missing; attach at portal center. |
| `Audio_PortalHum` | Audio Component | `DefaultSceneRoot` | Optional; auto activate only when `bPortalActive` is true and audio cue exists. |
| `PointLight_Aetherium` | Point Light Component | `DefaultSceneRoot` | Optional; disabled by default on low settings; low intensity only. |
| `Billboard_EditorMarker` | Billboard Component | `DefaultSceneRoot` | Editor-only marker for portal ID/debug placement. |

Preferred socket targets, if the arch mesh includes sockets:

- `Socket_PortalCore`
- `Socket_VFX_Center`
- `Socket_Audio_Hum`

If sockets are not present on the imported arch, align child components by relative transforms and add a note for the mesh owner to add sockets in the next arch revision.

## Exposed Blueprint Variables

Group variables under clear editor categories.

### Portal

- `bPortalActive` bool, default `true`
- `PortalId` name or string, default `StartupPortal_A01`
- `DestinationId` name or string, default `None`
- `bAllowClientPreviewOnly` bool, default `true`
- `PortalState` name, default `IdleActive`

### Interaction

- `InteractionRadius` float, default `175.0`
- `InteractionHeight` float, default `260.0`
- `bPlayerInRange` bool, runtime only
- `FocusedActor` actor reference, runtime only

### Visuals

- `PortalCoreMaterial` material interface, default `MI_AET_PortalCore_A01`
- `IdleVfxSystem` Niagara system, optional
- `ActivationSound` sound base, optional
- `bUsePointLight` bool, default `false`
- `LowSettingsDisableVfx` bool, default `true`

### Debug

- `bDebugPortalLogs` bool, default `false`
- `bDrawInteractionDebug` bool, editor only, default `false`

Do not add a separate enum asset for this slice unless the project explicitly approves additional Unreal content assets. A name-based state variable is enough for the first Blueprint pass.

## Construction Script

The construction script should only do editor-safe setup:

1. Assign the arch mesh if the dependency is available.
2. Apply `InteractionRadius` and `InteractionHeight` to `InteractionVolume`.
3. Position `SM_PortalCore` inside the aperture.
4. Hide optional components when their asset references are unset.
5. Set preview state from `bPortalActive`.
6. Avoid spawning gameplay actors, changing level state, or running travel logic.

Keep gameplay authority out of the construction script.

## Runtime State Machine

Use simple state functions so the visual behavior is easy to inspect:

- `SetPortalState_Inactive`
- `SetPortalState_IdleActive`
- `SetPortalState_Focused`
- `SetPortalState_UseRequested`
- `SetPortalState_Cooldown`
- `SetPortalState_DisabledBlocked`

State definitions:

| State | Entry Condition | Visuals | Gameplay Behavior |
| --- | --- | --- | --- |
| `Inactive` | `bPortalActive == false` | Core opacity near 0; no idle VFX; no hum; no point light. | Interaction overlap can remain enabled for debug, but use requests are rejected. |
| `IdleActive` | BeginPlay default when active | Slow blue core pulse; restrained idle mist if available; low hum if available. | Pawn overlap updates `bPlayerInRange`; no travel. |
| `Focused` | Valid pawn enters interaction range or focus target is set | Slightly brighter rim and pulse speed; optional prompt event. | May broadcast `OnPortalFocusChanged(true)`. |
| `UseRequested` | Player presses interact while focused | Short brightness pulse and optional activation sound. | Log or broadcast request; do not teleport. |
| `Cooldown` | After use-request preview pulse | Return intensity toward idle. | Blocks repeated preview requests for a short local cooldown. |
| `DisabledBlocked` | Missing destination, inactive, or authority unavailable | Desaturated/dim core or red-free warning style; keep Aerathea blue language. | Reject request with debug reason only. |

Required transition flow:

1. `BeginPlay` -> `IdleActive` if `bPortalActive`, otherwise `Inactive`.
2. `InteractionVolume.BeginOverlap` with pawn -> `Focused` if active.
3. `InteractionVolume.EndOverlap` -> `IdleActive` if no valid focused pawn remains.
4. Interact request while `Focused` -> `UseRequested`.
5. `UseRequested` timer completes -> `Cooldown`.
6. `Cooldown` timer completes -> `Focused` if pawn remains in range, otherwise `IdleActive`.
7. Any state -> `Inactive` when `bPortalActive` becomes false.
8. Any invalid use request -> `DisabledBlocked`, then return to prior safe state.

Future server-authoritative behavior should replace the local use-request preview with a server request/validation path. The client may request portal use; the server must validate portal availability, player location, destination, cooldown, and game state before travel.

## VFX And Material Parameters

Create a dynamic material instance for `SM_PortalCore` at `BeginPlay` and store it as `MID_PortalCore`.

Recommended scalar parameters:

| Parameter | Inactive | Idle Active | Focused | Use Requested | Notes |
| --- | ---: | ---: | ---: | ---: | --- |
| `CoreOpacity` | `0.0` | `0.75` | `0.85` | `1.0` | Fade, do not pop. |
| `PulseIntensity` | `0.0` | `0.35` | `0.55` | `0.85` | Keep bloom restrained. |
| `NoisePanSpeed` | `0.0` | `0.08` | `0.12` | `0.18` | Slow magical motion. |
| `RimGlowIntensity` | `0.0` | `0.45` | `0.65` | `0.9` | Avoid screen-filling glow. |
| `DistortionStrength` | `0.0` | `0.08` | `0.12` | `0.16` | Disable at medium/far distance if expensive. |
| `ActivationAlpha` | `0.0` | `0.0` | `0.25` | `1.0` | Short pulse only. |

Recommended vector parameters:

- `CoreColorDeep`: `#06315E`
- `CoreColorAetherium`: `#1E86D9`
- `CoreColorHighlight`: `#9EDCFF`

Texture inputs:

- `T_AET_PortalCore_A01_Noise`
- `T_AET_PortalCore_A01_Mask`

Niagara user parameters, if `NS_AET_PortalIdle_A01` exists:

- `User.SpawnRateScale`
- `User.CoreColor`
- `User.PulseStrength`
- `User.PortalRadius`
- `User.DistanceCullStart`
- `User.DistanceCullEnd`

VFX budget rules:

- The material core must carry the portal read without dense particles.
- Niagara is optional for the first slice.
- Disable or reduce Niagara at distance.
- Keep point light disabled unless the startup scene needs a small local accent.
- Use emissive only for portal core, Aetherium channels, and interaction highlight.

## Collision And Interaction

Static mesh collision:

- `SM_PortalArch` blocks world/static and pawn according to the imported simple collision.
- Expected arch collision primitives:
  - `UCX_SM_AET_PortalArch_A01_00`: left column
  - `UCX_SM_AET_PortalArch_A01_01`: right column
  - `UCX_SM_AET_PortalArch_A01_02`: capstone
  - `UCX_SM_AET_PortalArch_A01_03`: base stones
- The portal opening should remain walkable unless gameplay later requires a blocking portal surface.

Portal core collision:

- `SM_PortalCore` has collision disabled.
- It should never block the pawn or camera.

Interaction volume:

- Overlap pawn only.
- Ignore world/static, visibility, camera, physics body, and projectiles unless a future interaction system requires otherwise.
- Box option: about 350 cm wide x 120 cm deep x 260 cm high, centered on the aperture.
- Sphere option: radius 175 cm, with vertical reach validated against player capsule height.
- Generate begin/end overlap events.

Interaction events:

- On valid pawn begin overlap: set `bPlayerInRange = true`, cache focused actor, enter `Focused`.
- On valid pawn end overlap: clear cached focused actor if matching, return to `IdleActive`.
- On local interact input or external interaction interface call: enter `UseRequested` only if active and focused.
- For the slice, output debug log or Blueprint event only:
  - `OnPortalUsePreviewRequested(PortalId, DestinationId, FocusedActor)`
- Do not perform map travel, streaming, teleport, save-state mutation, quest updates, or inventory changes.

## Level Placement

Target map:

- `/Game/Aerathea/Maps/L_Aerathea_Startup`

Placement notes:

- Replace or wrap the existing portal blockout content:
  - `AET_BOOT_PortalArch_*`
  - `AET_BOOT_PortalCore_Aetherium_A01`
- Use the current portal blockout location as the placement reference.
- Portal arch package notes a rough target of `X=350, Y=0`.
- Actor origin should sit at ground contact between the two columns.
- Portal should face +X unless the level convention has changed.
- Player should be able to stand inside the aperture without collision snagging.

## Implementation Sequence

1. Confirm `SM_AET_PortalArch_A01` is imported and passes the dependency gate.
2. Create `BP_AET_Portal_A01` at `/Game/Aerathea/Blueprints/Props/BP_AET_Portal_A01`.
3. Add components in the order listed in this handoff.
4. Assign arch mesh, portal core material, optional VFX, optional audio, and optional light.
5. Create exposed variables and categories.
6. Implement construction-script editor setup.
7. Implement `BeginPlay` dynamic material creation and default state entry.
8. Implement state functions and transition timers.
9. Implement overlap-driven focus behavior.
10. Implement interaction preview event with no travel side effects.
11. Place the Blueprint in `L_Aerathea_Startup`.
12. Disable or hide the old blockout pieces after replacement is visually confirmed.
13. Compile, save, run PIE, and perform validation.

## Validation Steps

Dependency validation:

- Confirm the arch mesh path resolves.
- Confirm arch scale, pivot, aperture, LODs, material slots, and collision.
- Confirm `MI_AET_PortalCore_A01` path resolves.
- Confirm missing optional VFX/audio assets do not break Blueprint compile.

Blueprint validation:

- Blueprint compiles with no warnings.
- Construction script does not spawn gameplay actors or mutate level state.
- `SM_PortalCore` is centered in the aperture and does not z-fight with the arch.
- Interaction volume dimensions match the package targets.
- Dynamic material instance updates all state parameters.
- Optional VFX and audio cleanly disable when unset.
- Point light is off by default or justified by scene review.

PIE validation:

- Player can approach without collision snagging.
- Player can stand inside the aperture.
- Begin overlap enters `Focused`.
- End overlap returns to `IdleActive`.
- Interact request enters `UseRequested`, then `Cooldown`, then the correct safe state.
- Inactive state blocks interaction preview and dims the core.
- No travel, teleport, save, quest, inventory, or progression effects occur.
- Portal remains readable without excessive bloom or dense particles.

Startup map validation:

- `BP_AET_Portal_A01` replaces or wraps the portal blockout cleanly.
- Existing startup scene composition remains readable from settlement distance.
- The portal reads as a landmark, not a raid-scale monument.
- GUI map check reports `0 Error(s), 0 Warning(s)`.

## Blockers And Open Items

Hard blockers for final Blueprint creation:

- `SM_AET_PortalArch_A01` is not imported at the required Unreal path.
- Arch collision is missing, complex-as-simple, or blocks the portal opening incorrectly.
- Arch pivot or scale does not match the package, preventing reliable placement.
- Portal core material `MI_AET_PortalCore_A01` is missing and no approved material fallback exists.

Soft blockers for full visual polish:

- `NS_AET_PortalIdle_A01` does not exist yet; use material-only core until VFX is approved.
- Portal hum audio cue does not exist yet; keep audio component disabled.
- Final Flamestrike approval is still pending for both first-pass concept references.
- Arch sockets may be absent; use relative transforms for the slice and request sockets in the next mesh pass.

Future gameplay blockers:

- No server-authoritative traversal service is defined yet.
- Destination registry, cooldown rules, unlock rules, and map-travel policy are not defined yet.
- Multiplayer prediction/feedback behavior is not defined yet.

Until those systems exist, `BP_AET_Portal_A01` must remain a visual and interaction-preview actor only.

## Acceptance Checklist

- Uses `SM_AET_PortalArch_A01` as the required static structure.
- Preserves the chunky Aerathea stone arch silhouette.
- Portal core fits inside the aperture and uses restrained blue Aetherium colors.
- Blueprint state machine supports inactive, idle active, focused, use-requested, cooldown, and blocked states.
- Interaction volume overlaps pawn only and does not block movement.
- Portal core has no collision.
- Optional VFX/audio/light dependencies are safe when missing.
- No client-authoritative final traversal exists in the slice.
- Startup map replacement is validated in PIE.
- GUI map check remains `0 Error(s), 0 Warning(s)`.
