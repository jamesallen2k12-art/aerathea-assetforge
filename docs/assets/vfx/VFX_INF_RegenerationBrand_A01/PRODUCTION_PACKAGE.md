# VFX_INF_RegenerationBrand_A01 Production Package

## Art Direction Summary

`VFX_INF_RegenerationBrand_A01` is the restrained Balgoroth brand-regeneration effect for Infernal body brands, branding stones, Lesser lifecycle rites, and future regeneration gameplay hooks. It connects the static `SM_INF_BrandingStone_A01` sockets to body-brand material states without becoming generic healing light, full-body fire, or constant bloom.

The effect should feel predatory and painful but controlled: ember-red scar lines waking up, short red-orange arcs from the branding stone to the chosen body mark, ash motes lifting, and a brief warm consolidation pulse. Violet is reserved for curse/rejection contamination only.

Current status: docs-only production package. No Niagara systems, emitters, materials, textures, Blueprint bindings, or Unreal assets are authored by this task.

## Gameplay Purpose

- Provides a future VFX contract for Infernal regeneration, brand initiation, Blooded/Elder advancement, and worthiness aftermath.
- Uses `SM_INF_BrandingStone_A01` sockets for prop-side origin and transfer points.
- Reuses `MI_INF_BrandGlowStates_A01` state language for body-brand masks.
- Keeps regeneration readable for MMO/ARPG camera distances without obscuring claws, wings, tails, or target silhouettes.

## Silhouette Notes

- Effects must frame the brand and body plane, not cover the whole character.
- Primary reads: brand core, forearm/chest/shoulder mask, brief transfer arc, and fading ember seam.
- Keep the face, hands, wings, tail, and weaponless natural-combat silhouette visible.
- Avoid smoke walls, dense sparks, huge rings, and full-body flame shells.

## Scale Notes

- Prop-side origin supports `SM_INF_BrandingStone_A01` at roughly 190 cm high.
- Character targets support Lesser stages from 70-90 cm and adult bands from 152-274 cm.
- Default brand pulse radius: 20-45 cm.
- Transfer arc length: 30-180 cm, depending hand/forearm/chest placement.
- Exalted or boss variants may scale radius by 1.25-1.5, but particle density should stay capped.

## Materials and Color Palette

| Effect family | Palette | Use |
| --- | --- | --- |
| Ember scar | deep red, ember orange | brand lines, healed scar seams |
| Hot core | red-orange with small orange-white center | short accepted/regrowth pulse |
| Ash motes | dark ash, smoke brown, faint ember points | low-density aftermath only |
| Curse contamination | violet-red, low opacity | rejection, failed brand, curse interference |
| Stone channel | scorched red, black basalt shadow | branding stone socket and groove response |

Do not introduce clean holy white, blue Aetherium, Ogre green-black necromancy, or constant violet aura.

## Concept Image Prompt

Create an original stylized fantasy MMORPG VFX state sheet of `VFX_INF_RegenerationBrand_A01` for the Infernals of Aerathea. The design should emphasize restrained Balgoroth brand regeneration, ember-red scar lines, body-brand masks, short red-orange transfer arcs from a black basalt branding stone, low ash motes, warm accepted pulse, brief violet-red curse contamination, and readable Infernal silhouettes with horns, wings, claws, and thick tails still visible. Use hand-painted VFX shapes, focused emissive accents, controlled particle density, fixed-bounds-friendly Niagara design, and MMO-friendly readability. Present it as a VFX board with inactive, smolder, brand transfer, regeneration pulse, accepted consolidation, rejected contamination, and cooldown frames, including `SM_INF_BrandingStone_A01` socket callouts and body-mask callouts. Avoid copied franchise symbols, gore, screen-filling fire, dense sparks, unreadable magic circles, readable text, watermarks, and photoreal noise.

## Modeling Notes

- No permanent mesh geometry is required.
- Optional helper meshes:
  - low-poly curved arc ribbon under 150 tris
  - brand pulse plane under 100 tris
  - tiny ash mote card under 20 tris
- Helper meshes should be reusable and material-driven.
- Do not add modeled needles, chains, glyph cages, or physical regeneration machinery.

## Texture and Material Notes

Texture targets:

- `T_INF_RegenerationBrand_Arc_A01_E`
- `T_INF_RegenerationBrand_Pulse_A01_E`
- `T_INF_RegenerationBrand_Ash_A01_BC`
- `T_INF_RegenerationBrand_Mask_A01_E`

Material targets:

- `M_INF_RegenerationBrand_Arc_A01`
- `M_INF_RegenerationBrand_Pulse_A01`
- `M_INF_RegenerationBrand_Ash_A01`
- `MI_INF_RegenerationBrand_Arc_A01`
- `MI_INF_RegenerationBrand_Pulse_A01`
- `MI_INF_RegenerationBrand_Ash_A01`

Niagara system targets:

- `NS_INF_RegenerationBrand_Inactive_A01`
- `NS_INF_RegenerationBrand_Smolder_A01`
- `NS_INF_RegenerationBrand_Transfer_A01`
- `NS_INF_RegenerationBrand_Pulse_A01`
- `NS_INF_RegenerationBrand_Accepted_A01`
- `NS_INF_RegenerationBrand_Rejected_A01`
- `NS_INF_RegenerationBrand_Cooldown_A01`

Emitter targets:

- `NE_INF_RegenerationBrand_Arc_A01`
- `NE_INF_RegenerationBrand_Pulse_A01`
- `NE_INF_RegenerationBrand_Ash_A01`
- `NE_INF_RegenerationBrand_Snap_A01`

## Triangle Budget

No static mesh triangle cost beyond optional helper cards.

- Arc ribbon helper: under 150 tris.
- Brand pulse helper: under 100 tris.
- Ash card helper: under 20 tris.
- Total helper mesh budget per system: under 500 tris.

## LOD Plan

- VFX LOD0: transfer arc, brand pulse, restrained ash, short edge sparks, material-mask pulse.
- VFX LOD1: reduce ash and sparks by at least 50 percent; keep transfer arc and brand pulse.
- VFX LOD2: remove sparks and most ash; preserve brand color block and one arc/pulse.
- VFX LOD3: disable particles; keep only material-mask glow if gameplay readability requires it.

Particle count should reduce before primary brand readability is removed.

## Collision Notes

No collision. Gameplay healing, regeneration, damage, cleanse, or curse logic belongs to future Blueprint/C++ or Gameplay Ability work. This package only defines visual response and parameter contracts.

## Animation Notes

Animation/VFX sync points:

- `BrandPrepare`: branding stone core smolders.
- `BrandContact`: target body mark brightens.
- `TransferStart`: short arc from stone to body mask.
- `RegenerationPulse`: scar/brand pulse expands once, then narrows.
- `AcceptedConsolidate`: warm ember settles into the brand.
- `RejectedSnap`: brief violet-red snap and ash kick.
- `Cooldown`: ash motes fade and emissive returns to low smolder.

The effect may be driven by animation notifies, ritual Blueprint states, or future gameplay abilities. It must not require final combat timing during this package stage.

## Unreal Import Notes

- Asset type: Niagara systems, emitters, helper materials, optional helper meshes.
- Unreal folder: `/Game/Aerathea/VFX/Infernals/RegenerationBrand/`
- Material path: `/Game/Aerathea/Materials/Infernals/VFX/`
- Texture path: `/Game/Aerathea/Textures/Infernals/VFX/RegenerationBrand/`
- Primary prop dependency: `/Game/Aerathea/Props/Infernals/BalgorothCult/BrandingStone/SM_INF_BrandingStone_A01`
- Primary material dependency: `/Game/Aerathea/Materials/Infernals/M_INF_BrandGlow_Master_A01`
- Future focused validator path: `Tools/Unreal/validate_infernal_regeneration_brand_vfx.py`
- Startup validation impact: not required until Niagara assets are authored, assigned, or placed in a review scene.

`User.*` parameter contract:

- `User.State`
- `User.SourceWorldLocation`
- `User.TargetWorldLocation`
- `User.BrandCoreWorldLocation`
- `User.BrandTransferWorldLocation`
- `User.BodyBandScale`
- `User.EmissiveIntensity`
- `User.PulseDuration`
- `User.ArcDensity`
- `User.AshDensity`
- `User.VioletMix`
- `User.AcceptedFocus`
- `User.RejectedSnap`

Fixed bounds:

- Prop-attached bounds should cover `vfx_brand_core`, `vfx_brand_transfer`, and the hand/forearm presentation groove without covering the full room.
- Character-attached bounds should scale from compact adult to 274 cm Greater/Exalted without clipping wing roots or tail base if those masks are active.

## Folder and Naming Recommendation

- Package folder: `docs/assets/vfx/VFX_INF_RegenerationBrand_A01/`
- Related prop: `docs/assets/props/SM_INF_BrandingStone_A01/`
- Related material state package: `docs/assets/materials/MI_INF_BrandGlowStates_A01/`
- Related combat VFX package: `docs/assets/vfx/VFX_INF_AbyssalSpellcasting_A01/`
- Unreal VFX folder: `/Game/Aerathea/VFX/Infernals/RegenerationBrand/`
- Unreal material folder: `/Game/Aerathea/Materials/Infernals/VFX/`
- Unreal texture folder: `/Game/Aerathea/Textures/Infernals/VFX/RegenerationBrand/`

## Quality Gate Checklist

- Reads as Infernal/Balgoroth regeneration, not holy healing, Aetherium, Ogre necromancy, or generic fire.
- Uses BrandingStone sockets and BrandGlow material states without redefining prop identity.
- Preserves body, hand, wing, tail, and brand silhouette readability.
- Particle density, bloom, and ash stay restrained.
- `User.*` parameters, Niagara system names, emitter names, fixed bounds, LOD behavior, animation sync points, and Unreal paths are defined.
- No final Niagara graph art, gameplay healing numbers, backend authority, or animation timing is claimed by this package.
