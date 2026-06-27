# MI_INF_BrandGlowStates_A01 Production Package

## Art Direction Summary

`MI_INF_BrandGlowStates_A01` defines the final-art material-state direction for Infernal body brands, lit sigils, ritual scars, sorcerer glow accents, and Balgoroth cult markings. It is shared by `SK_INF_Base_A01`, `SK_INF_Lesser_A01`, and `KIT_INF_BalgorothCult_A01`.

The material must feel predatory and ritualized without turning the Infernals into constantly glowing demons. Glow is a state language: chosen, culling temper, regeneration, trial active, accepted, rejected, or sorcerer focus.

## Gameplay Purpose

- Provides consistent readable states for Infernal brands across adult, Lesser, sorcerer, and cult assets.
- Supports regeneration feedback, worthiness judgment, stealth detection, rage/culling temper, and magic-casting tells.
- Lets designers drive clear state changes without swapping meshes or adding heavy particle systems.

## Silhouette Notes

- Brand shapes should follow anatomy and major silhouette planes: chest, shoulders, horns, wing roots, forearms, claws, tail base, and spine ridges.
- Marks must be broad enough to read on 5' compact adults, 9' greater adults, and Lesser lifecycle stages.
- Avoid tiny rune text, dense tattoo webs, or all-over neon body glow.

## Scale Notes

- Use one shared material function/state set with masks authored per body variant.
- Adult masks need coverage for Compact, Standard, Greater, and Exalted height bands.
- Lesser masks need reduced intensity and simpler marks for Spawn and 1st Kill, then stronger marks for Blooded, Elder, and Ancient.

## Materials And Color Palette

- Inactive: red-brown scar tissue, low roughness variation, no active glow.
- Smolder: low ember orange at brand centerlines.
- Trial active: stronger red-orange channels limited to brand masks.
- Accepted: focused warm ember at chosen marks, stable and controlled.
- Rejected: brief violet-red pulse in broken-circle or claw-scar shapes.
- Sorcerer focus: ember orange plus a small violet core only at hands, eyes, or brand intersections.

## Concept Image Prompt

Create an original stylized fantasy MMORPG material-state sheet of `MI_INF_BrandGlowStates_A01` for the Infernals of Aerathea. The design should emphasize demonic mortal-descendant body brands, restrained ember glow, red-black scar tissue, Balgoroth horned crown and claw-scar motifs, inactive/smoldering/trial-active/accepted/rejected/sorcerer-focus states, readable masks on horns, wings, claws, tail, shoulders, chest, and forearms, and MMO-friendly material implementation. Use hand-painted texture detail, baked-AO-style depth, normal-map-style scar ridges, sparing emissive accents, and production-friendly shader states. Present it as a clean material board with body-region callouts, mask swatches, color values, intensity ranges, and runtime state notes. Avoid copied franchise symbols, gore, all-over neon glow, readable text, watermarks, and photoreal micro-detail.

## Modeling Notes

- No additional geometry is required for normal brand states.
- Final art may include subtle raised scar geometry only on hero models; common models should use normal maps and emissive masks.
- Horn, claw, tail, and wing root brands should align to existing sockets and animation deformation.

## Texture And Material Notes

Texture targets:

- `T_INF_BrandGlow_A01_E`
- `T_INF_BrandGlow_A01_Mask`
- `T_INF_BrandScar_A01_N`
- `T_INF_BrandScar_A01_ORM`

Material instances:

- `MI_INF_BrandGlowStates_A01_Inactive`
- `MI_INF_BrandGlowStates_A01_Smolder`
- `MI_INF_BrandGlowStates_A01_TrialActive`
- `MI_INF_BrandGlowStates_A01_Accepted`
- `MI_INF_BrandGlowStates_A01_Rejected`
- `MI_INF_BrandGlowStates_A01_SorcererFocus`

Suggested scalar parameters:

- `EmissiveIntensity`
- `PulseSpeed`
- `PulseWidth`
- `VioletMix`
- `ScarDarken`
- `HeatEdgeContrast`

## Triangle Budget

No triangle budget impact for common implementation. Hero raised-scar geometry, if approved later, should stay under 300-700 tris per character variant and should be removed by LOD1 or LOD2.

## LOD Plan

- LOD0: full emissive mask and normal scar detail.
- LOD1: same mask, reduced normal contrast and lower pulse frequency.
- LOD2: simplified mask or packed lower-resolution mask.
- LOD3: preserve only broad brand color blocks and eye/hand callouts where needed.

## Collision Notes

No collision.

## Animation Notes

- Material parameters should be driven by Animation Blueprint, Gameplay Ability, or ritual Blueprint state.
- Pulse must be low frequency by default.
- Rejected pulse should be short and event-based, not a constant idle state.

## Unreal Import Notes

- Asset type: Material Instance set or Material Function plus instances.
- Folder path: `/Game/Aerathea/Materials/Infernals/`
- Shared material function candidate: `MF_INF_BrandGlowStates_A01`
- Parent material candidate: `M_INF_BrandGlow_Master_A01`
- Use packed masks and expose scalar/vector parameters for Blueprint and Animation Blueprint control.

## Folder And Naming Recommendation

- Package folder: `docs/assets/materials/MI_INF_BrandGlowStates_A01/`
- Unreal folder: `/Game/Aerathea/Materials/Infernals/`
- Texture folder: `/Game/Aerathea/Textures/Infernals/BrandGlow/`
- Dependencies: `SK_INF_Base_A01`, `SK_INF_Lesser_A01`, `KIT_INF_BalgorothCult_A01`

## Quality Gate Checklist

- Glow is restrained and tied to lore/gameplay states.
- Material state names are reusable across adult, Lesser, and cult assets.
- Brand masks are readable from MMO camera distance.
- No readable text glyphs or copied symbols are required.
- Texture maps, state parameters, LOD behavior, Unreal paths, and runtime control notes are defined.
