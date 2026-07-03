# SM_INF_BrandingStone_A01 Production Package

## Art Direction Summary

`SM_INF_BrandingStone_A01` is the Balgoroth cult body-brand source prop for Infernal trial rooms, Lesser lifecycle staging, regeneration rites, and worthiness ceremonies. It is a readable mid-poly ritual stone that presents a chosen Infernal hand, forearm, chest, or shoulder mark to a controlled ember channel without becoming a torture device or gore prop.

The asset should feel severe, old, judgmental, and predatory: black basalt mass, scorched red ritual channels, a large Balgoroth sigil face, claw-groove scoring, horn/wing silhouettes, and a restrained brand-core glow. The form must stay readable at MMO camera distance and reuse `MI_INF_CultStone_Set_A01`, `SM_INF_BalgorothSigil_A01`, and `MI_INF_BrandGlowStates_A01` language.

## Gameplay Purpose

- Provides a physical anchor for body-brand initiation, regeneration setup, and worthiness trial staging.
- Gives future `VFX_INF_RegenerationBrand_A01` a prop-side socket and material-mask contract.
- Supports Lesser Infernal Blooded/Elder progression scenes without creating a duplicate character package.
- Functions as a non-blocking ritual prop in den, altar, and proving-arena spaces unless a future Blueprint adds interaction.

## Silhouette Notes

- Primary shape: heavy upright or angled basalt monolith, 160-220 cm tall, with a broad hand/forearm presentation face.
- Top silhouette: horned crown ridge or split-wing cap, not a generic tombstone.
- Main read: large Balgoroth sigil inset, brand channel, hand/forearm presentation groove, and safe interaction side.
- Secondary forms: blackened iron brace, small bone/horn wedge markers, claw-score grooves, and ash-worn base stones.
- Avoid dense rivets, tiny runes, unreadable chain clutter, or full-surface glowing cracks.

## Scale Notes

- Recommended review scale: 190 cm high x 95 cm wide x 75 cm deep.
- Works beside 70-90 cm Lesser Spawn/Blooded stages and 152-274 cm adult Infernal body bands.
- Interaction side should be reachable by a 180 cm humanoid and readable beside a 274 cm Infernal.
- Base footprint should remain stable and simple enough for den/altar placement without blocking wing or tail movement.

## Materials and Color Palette

- Basalt mass: blue-black and ash-gray using `MI_INF_CultStone_Basalt_A01`.
- Scorched channel: dark red/burnt umber using `MI_INF_CultStone_ScorchedRed_A01`.
- Sigil inset: obsidian-black relief using `SM_INF_BalgorothSigil_A01` shape language.
- Brand core: restrained ember orange/deep red with short violet only for rejected/curse state.
- Braces: blackened iron with dark bronze edge wear.
- Minor markers: smoke-stained bone/horn, used sparingly.

## Concept Image Prompt

Create an original stylized fantasy MMORPG static mesh concept sheet of `SM_INF_BrandingStone_A01`, a Balgoroth cult branding stone for the Infernals of Aerathea. The design should emphasize a severe black basalt monolith, horned crown cap, split-wing silhouette, large Balgoroth sigil inset, hand and forearm presentation groove, claw-score channels, scorched red ritual lines, blackened iron brace, smoke-stained horn markers, restrained ember brand-core glow, and safe interaction side for body-brand rites, regeneration setup, and worthiness trial staging. Use hand-painted texture detail, readable broad shapes, baked-AO-style depth, normal-map-style surface detail, sparing emissive accents, and MMO-friendly mid-poly production geometry. Present it as a static mesh production sheet with front view, side depth view, top footprint, socket callouts, inactive/smolder/trial-active/accepted/rejected material states, and scale beside a 180 cm humanoid and 274 cm Infernal. Apply A03-style cleanup if using Infernal source references: preserve horns, wings, claws, brands, skull/bone menace, flame, lightning-like abyssal energy, anger, and villain threat while reducing tiny rivets, random speckle artifacts, malformed micro-spikes, broken micro-chains, dense glow fuzz, and photoreal noise. Avoid copied franchise symbols, gore, readable text, watermarks, full-screen fire, and universal portal styling.

## Modeling Notes

- Model the monolith body, horned cap, large sigil relief, presentation groove, major claw channels, base stones, and iron brace as real geometry.
- Use texture/normal maps for fine cracks, ash smears, heat stress, tiny scratches, subtle brand wear, and shallow chips.
- Keep the presentation groove large and simple: it should read as a place for hand/forearm/chest marking, not a complicated machine.
- Build as one static mesh with optional detachable sigil relief only if DCC needs reuse.
- Do not add mechanical needles, torture blades, excessive chains, or gore.

## Texture and Material Notes

Texture targets:

- `T_INF_BrandingStone_A01_BC`
- `T_INF_BrandingStone_A01_N`
- `T_INF_BrandingStone_A01_ORM`
- `T_INF_BrandingStone_A01_E`

Recommended material slots:

1. `MI_INF_CultStone_Basalt_A01`
2. `MI_INF_CultStone_ScorchedRed_A01`
3. `MI_INF_BalgorothSigil_A01_Obsidian`
4. `MI_INF_CultStone_BlackIron_A01`
5. `MI_INF_BrandingStone_A01_Emissive`

Material states:

- Inactive: no visible emissive except faint ash warmth in the core.
- Smolder: low ember in the brand groove and sigil core.
- Trial active: localized red-orange channel glow, no all-over bloom.
- Accepted: warm focused brand pulse from groove to sigil core.
- Rejected: brief violet-red snap at the broken-circle mark only.
- Cooldown: fading ember flecks and dark stone readability restored.

## Triangle Budget

- LOD0 target: 3k-6k tris.
- Upper bound: 8k tris only if the sigil relief, horned cap, and base stones need more silhouette support.
- Material slots: 3-5 maximum.
- Texture set: 1K for normal prop use, 2K only if used as a hero altar-room focal prop.

## LOD Plan

- LOD0: full monolith form, horned cap, sigil relief, presentation groove, claw channels, brace, base stones.
- LOD1: 55-60 percent; reduce small chips, secondary bevels, minor base-stone loops.
- LOD2: 25-35 percent; simplify brace and groove bevels, preserve horned cap, sigil silhouette, and brand-core color block.
- LOD3: 10-15 percent; preserve monolith outline, major sigil shape, and one emissive block only.

## Collision Notes

- Default collision: simple box or convex hull around the stone body and base.
- Interaction side should remain clear; avoid collision protrusions that trap tails, wings, or player capsules.
- Presentation groove does not need complex collision unless a future Blueprint requires precise hand placement.
- No gameplay damage, regeneration, or trial collision is implied by this static mesh package.

## Animation Notes

- Static mesh by default.
- Optional material-scalar animation for inactive, smolder, trial active, accepted, rejected, and cooldown states.
- No skeletal animation, moving parts, dynamic lights, or physics simulation in this package.
- Future VFX should bind through sockets and material masks, not by adding constant particles to the mesh.

## Unreal Import Notes

- Asset type: Static Mesh.
- Unreal folder: `/Game/Aerathea/Props/Infernals/BalgorothCult/BrandingStone/`
- Naming convention:
  - `SM_INF_BrandingStone_A01`
  - `MI_INF_BrandingStone_A01_Emissive`
  - `T_INF_BrandingStone_A01_BC`
  - `T_INF_BrandingStone_A01_N`
  - `T_INF_BrandingStone_A01_ORM`
  - `T_INF_BrandingStone_A01_E`
- Pivot: center bottom of the base footprint.
- Scale: centimeters, 1 Unreal unit = 1 cm.
- Collision: simple authored collision or generated convex collision.
- LODs: LOD0-LOD3 required.
- Socket plan:
  - `vfx_brand_core`
  - `vfx_brand_transfer`
  - `vfx_rejected_snap`
  - `interact_brand_side`
  - `snap_floor_center`

## Folder and Naming Recommendation

- Package folder: `docs/assets/props/SM_INF_BrandingStone_A01/`
- Related kit: `docs/assets/kits/KIT_INF_BalgorothCult_A01/`
- Related material package: `docs/assets/materials/MI_INF_CultStone_Set_A01/`
- Related symbol package: `docs/assets/props/SM_INF_BalgorothSigil_A01/`
- Future VFX dependency: `docs/assets/vfx/VFX_INF_RegenerationBrand_A01/`
- Source folder: `SourceAssets/Blender/Props/Infernals/BalgorothCult/SM_INF_BrandingStone_A01/`
- Export folder: `SourceAssets/Exports/Props/Infernals/BalgorothCult/SM_INF_BrandingStone_A01/`
- Unreal folder: `/Game/Aerathea/Props/Infernals/BalgorothCult/BrandingStone/`

## Quality Gate Checklist

- Branding stone reads as Balgoroth cult and not a generic tombstone, portal, forge, or torture device.
- Large horned cap, split-wing/sigil face, presentation groove, and brand core are readable at MMO camera distance.
- Materials follow `MI_INF_CultStone_Set_A01` and `SM_INF_BalgorothSigil_A01`.
- Glow is sparse, state-driven, and localized to brand/sigil channels.
- Major forms are real geometry; fine cracks, ash, scratches, and subtle brand wear stay in maps.
- Triangle budget, material slots, texture targets, LOD0-LOD3, collision, pivot, sockets, and Unreal path are defined.
- Future `VFX_INF_RegenerationBrand_A01` can consume the socket and material-mask contract without reinterpretation.
- No gore, readable text, copied symbols, excessive particles, or photoreal micro-detail.
