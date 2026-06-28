# BP_AET_Portal_A01 Production Package

## Asset Brief

- Asset name: `BP_AET_Portal_A01`
- Asset type: Blueprint Actor
- World: Aerathea
- Category: Interactive portal / traversal actor
- Current status: Native preview behavior implemented in `AAETPortalActor`; Blueprint asset exists/reparented/compiled; startup validator passes; final traversal/VFX/audio still pending gameplay approval
- Required static mesh: `SM_AET_PortalArch_A01`

This blueprint wraps the portal arch mesh, visual portal core, interaction area, and future traversal behavior. The base portal is universal and race-neutral; race or faction portal variants should reuse this gameplay logic and change only mesh, materials, VFX, audio, or dressing as needed.

## Concept Reference

- State sheet: `docs/assets/blueprints/BP_AET_Portal_A01/concepts/BP_AET_Portal_A01_state_sheet_A01.png`
- Implementation handoff: `docs/assets/blueprints/BP_AET_Portal_A01/IMPLEMENTATION_HANDOFF.md`
- Generation mode: built-in image generation tool.
- Review status: usable first-pass reference for inactive, idle active, and highlighted interaction states; final Flamestrike approval still required before treating it as a locked final art target.

## Gameplay Purpose

The portal blueprint is the first interactive landmark actor for the startup scene. It should prove:

- Blueprint composition around a static mesh prop.
- Interaction volume setup.
- VFX/material state control.
- Future server-authoritative portal traversal boundary.
- Safe placeholder behavior until multiplayer architecture is ready.
- Epic-world traversal scale for players, Giants, major NPCs, enemies, dungeons, raids, and cities.

Initial implementation should be visual and non-destructive. Do not implement permanent travel, inventory, quest, or progression changes in a client-only blueprint.

## Silhouette Notes

The blueprint should preserve the silhouette of `SM_AET_PortalArch_A01`.

Additional visible parts:

- Portal core plane or mesh inside aperture.
- Subtle blue Aetherium mist or swirl.
- Optional low-intensity point light only if performance budget permits.
- Optional interaction marker component hidden outside editor builds.

Do not fill the arch with dense particles. The portal should read as active from the blue core shape and slow motion, not from screen-filling effects.

## Scale Notes

Final universal portal target:

- Uses the rebuilt `SM_AET_PortalArch_A01` at 1.0 scale.
- Minimum clear traversal height: 1000 cm / 10 m / about 33 ft.
- Portal should accommodate players, Giants, large NPCs, large enemies, and epic dungeon/raid/city traversal.
- Normal players should feel small when standing near the portal.
- Recommended interaction radius: 550 cm from portal center.
- Recommended trigger height: 1100 cm.
- Portal core should fit inside the rebuilt aperture, about 650-800 cm wide x 1000 cm high.
- Pivot inherits actor origin at arch bottom center.

Current startup review note:

- The current imported arch and portal core use the older smaller first-pass scale.
- Treat the current placement as a validation placeholder until the 10 m portal arch rebuild is complete.

## Materials And Color Palette

Required material instances:

- `MI_AET_PortalArch_A01_Stone`
- `MI_AET_PortalArch_A01_Accent`
- `MI_AET_PortalCore_A01`

Portal core palette:

- Deep blue: `#06315E`
- Aetherium blue: `#1E86D9`
- Pale core highlight: `#9EDCFF`

Portal core should be visibly magical, but still restrained. Avoid excessive bloom or full-screen glow.

## Concept Image Prompt

Create an original stylized fantasy MMORPG concept image of an active universal portal actor for the world of Aerathea. The design should emphasize a monumental stone arch with a 10 m / 33 ft clear traversal opening, restrained blue Aetherium portal core, old and mysterious world-scale magic, awe-inspiring scale, hand-painted stone and dark-iron materials, readable interaction space, and traversal gameplay for players, Giants, large NPCs, enemies, epic dungeons, raids, and cities. Normal player characters should feel small beside it. Use hand-painted texture detail, readable shapes, baked-AO-style depth, normal-map-style surface detail, sparing emissive accents, and MMO-friendly production design. Present it as a concept sheet showing inactive, idle active, and highlighted interaction states, with a 180 cm humanoid scale reference, a 470 cm Giant reference, and a 1000 cm clearance marker. Avoid copying any existing franchise and avoid excessive particles or micro-detail that would not translate to a performant Unreal asset.

## Blueprint Component Plan

Components:

- `DefaultSceneRoot`
- `SM_PortalArch`: StaticMeshComponent, uses `SM_AET_PortalArch_A01`
- `SM_PortalCore`: StaticMeshComponent or plane, uses `MI_AET_PortalCore_A01`
- `InteractionVolume`: BoxComponent or SphereComponent
- `VFX_PortalIdle`: NiagaraComponent, optional after VFX package exists
- `Audio_PortalHum`: AudioComponent, optional
- `PointLight_Aetherium`: optional, disabled by default on low settings

Sockets or attachment points:

- `Socket_PortalCore`
- `Socket_VFX_Center`
- `Socket_Audio_Hum`

Editor-exposed variables:

- `bPortalActive`
- `PortalId`
- `DestinationId`
- `InteractionRadius`
- `bAllowClientPreviewOnly`
- `PortalCoreMaterial`
- `IdleVfxSystem`
- `ActivationSound`

## Behavior Notes

Initial bootstrap behavior:

- Idle active visual state.
- Interaction overlap focus state.
- Use-requested preview state and cooldown.
- Debug logs and Blueprint events only, if needed.
- No map travel by default.
- No player teleport by default.

Future authoritative behavior:

- Client may request portal use.
- Server validates portal availability, player location, destination, cooldown, and required state.
- Server performs travel/teleport.
- Client receives visual/audio feedback.

Never make final traversal client-authoritative.

## Texture And Material Notes

Portal core material:

- Unlit or emissive material with low bloom.
- Panning noise texture for slow motion.
- Soft radial mask.
- Color parameter for state changes.
- Opacity parameter for activation/deactivation.

Texture names:

- `T_AET_PortalCore_A01_Noise`
- `T_AET_PortalCore_A01_Mask`

Material name:

- `MI_AET_PortalCore_A01`

## Triangle Budget

Blueprint mesh budget is mostly `SM_AET_PortalArch_A01`.

Additional geometry:

- Portal plane/core: 2 to 64 tris depending on mesh shape.
- VFX sprites: controlled by Niagara budget.

Keep total visible mesh overhead under 200 tris beyond the arch; portal size changes should come from the arch/core scale, not dense extra geometry.

## LOD Plan

Use arch LODs from `SM_AET_PortalArch_A01`.

Portal core:

- Full animated material at near distance.
- Reduced material animation at medium distance.
- Disable expensive VFX at far distance.
- Keep a simple blue core card visible for silhouette/readability.

## Collision Notes

Collision components:

- Arch collision from static mesh.
- Interaction volume set to overlap pawn.
- Portal core has no blocking collision.

Collision channel plan:

- `SM_PortalArch`: block world/static and pawn as needed by arch geometry.
- `InteractionVolume`: overlap pawn only.
- `SM_PortalCore`: no collision.

## Animation Notes

Animation should be material/VFX driven:

- Slow vertical or radial panning.
- Idle pulse at low intensity.
- Faster pulse on focus/interaction.
- Fade out when inactive.

Avoid skeletal animation for this actor.

## Unreal Import And Implementation Notes

- Blueprint path: `/Game/Aerathea/Blueprints/Props/BP_AET_Portal_A01`
- Static mesh dependency: `/Game/Aerathea/Props/Portal/SM_AET_PortalArch_A01`
- Material dependency: `/Game/Aerathea/Materials/Props/Portal/MI_AET_PortalCore_A01`
- VFX dependency: future `/Game/Aerathea/VFX/Portal/NS_AET_PortalIdle_A01`
- Place in `L_Aerathea_Startup` at current portal blockout location for the first pass; review and likely reposition after the 10 m arch rebuild.
- Use construction script only for editor-safe setup, not gameplay authority.
- Add clear editor category labels for exposed variables.

## Folder And Naming Recommendation

Unreal content:

- `/Game/Aerathea/Blueprints/Props/BP_AET_Portal_A01`
- `/Game/Aerathea/Materials/Props/Portal/MI_AET_PortalCore_A01`
- `/Game/Aerathea/Textures/Props/Portal/Core/T_AET_PortalCore_A01_Noise`
- `/Game/Aerathea/Textures/Props/Portal/Core/T_AET_PortalCore_A01_Mask`
- `/Game/Aerathea/VFX/Portal/NS_AET_PortalIdle_A01`

## Quality Gate Checklist

- Uses original Aerathea portal visuals.
- Preserves arch readability.
- Supports the approved 10 m / about 33 ft clear traversal scale.
- Normal players feel small beside the portal.
- Interaction volume is easy to inspect.
- No gameplay travel until server authority is implemented.
- Client-only behavior is visual/debug only.
- Portal core does not over-bloom.
- VFX can be disabled or reduced at distance.
- Collision does not block portal core.
- Blueprint variables are clearly named.
- GUI map check remains `0 Error(s), 0 Warning(s)`.
