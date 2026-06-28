# VFX_INF_AbyssalSpellcasting_A01 Production Package

## 1. Art Direction Summary

- Asset name: `VFX_INF_AbyssalSpellcasting_A01`
- Asset type: Niagara/VFX production package plus material/VFX rules
- Primary users: `SK_INF_Mage_A01`, `SK_INF_Base_A01`, `SK_INF_Lesser_A01`, future Infernal class variants
- World: Aerathea
- Theme: Balgoroth-touched abyssal combat magic, brand-channel fire, lightning-like claw energy, invisible-sight reveal
- Current status: production package ready; Niagara/material authoring not started

This package defines the shared combat spellcasting language for adult Infernals and advanced Lesser Infernals. It is separate from `VFX_INF_WorthinessJudgment_A01`, which handles ritual floor and altar states. Abyssal spellcasting should feel angry, powerful, and predatory: flame, lightning-like red-orange arcs, glowing eyes, brand channels, claw bursts, wing-root flares, and short violent pulses. It must not become constant full-screen fire, unreadable bloom, or noisy artifact speckle.

Use `docs/assets/characters/INFERNAL_VISUAL_CLEANSE_STANDARD.md` as the visual gate. Preserve skulls, flame, lightning, glowing eyes, anger, and threat. Remove random speckles, excessive tiny sparks, malformed micro-runes, and clutter that hides hands, eyes, wings, tail, or silhouette.

## 2. Gameplay Purpose

- Supports Infernal mage combat spells, class telegraphs, and ability readability.
- Provides reusable effects for abyssal bolt, claw cast, brand-channel, regeneration flare, invisible-sight reveal, rage surge, wing-mantle intimidation, and tail-tip curse marks.
- Gives designers socket-driven effects that scale from Compact adult to Exalted adult without hand-authored one-offs.
- Keeps Infernal spellcasting visually distinct from blue Aetherium, Ogre green necromancy, Ogre shamanic storm/ember, and holy Valar magic.

## 3. Silhouette Notes

- Effects should frame the body, not replace it.
- Primary read points: eyes, open clawed hands, chest brand, forearm brands, wing roots, tail tip, and occasional mouth/roar flare.
- Flame and lightning arcs may connect hands to brands, but they should leave the face, hands, wings, and tail readable.
- Use short arc shapes, claw slashes, ember ribbons, and brand pulses rather than dense circular glyph fields.
- Avoid spell rings that crop through the character or hide the hand pose.

## 4. Scale Notes

- Must support adult Infernals from 152-274 cm.
- Default hand aura radius: 25-60 cm.
- Charged hand spell radius: 80-140 cm for major casts.
- Wing-root flare height: 60-180 cm, depending body band.
- Projectile start radius: 20-35 cm; projectile trail width should stay readable but not cover target silhouettes.
- Exalted/boss variants can scale intensity and radius by 1.25-1.5, but particle density should not scale linearly.

## 5. Materials And Color Palette

| Effect family | Palette | Use |
| --- | --- | --- |
| Ember fire | orange, deep red, hot red-orange core | hands, brands, regeneration flare, rage surge |
| Abyssal lightning | red-orange, orange-white center, occasional violet core | claw arcs, bolt charge, brand intersections |
| Violet abyss | focused violet-red | rejection/curse moments, sorcerer focus, invisible-sight edge |
| Smoke/ash | ash gray, smoke brown, dark ember flecks | short-lived cast aftermath only |
| Eye glow | ember orange, deep red, small violet core | invisible sight, rage, target lock |

Keep the palette hot and hostile. Do not introduce blue Aetherium, clean holy white, or Ogre green-black necromancy.

## 6. Concept Image Prompt

Create an original stylized fantasy MMORPG VFX state sheet of `VFX_INF_AbyssalSpellcasting_A01` for the Infernals of Aerathea. The design should emphasize Balgoroth-touched combat magic, red-orange flame, lightning-like abyssal claw arcs, glowing eyes, chest and forearm brand channels, open clawed hand casting, wing-root flares, tail-tip curse marks, regeneration pulses, invisible-sight reveal, rage surge, and powerful villain threat while preserving readable character silhouettes. Use hand-painted VFX shapes, focused emissive accents, clear MMO telegraphs, controlled particle density, and production-friendly Niagara design. Present it as a VFX board with idle smolder, hand charge, abyssal bolt, claw slash cast, brand-channel loop, regeneration flare, invisible-sight reveal, wing-mantle cast, rage surge, and cooldown frames with socket callouts. Avoid copied franchise symbols, gore, full-screen bloom, dense tiny sparks, unreadable magic circles, random speckle artifacts, readable text, and watermarks.

## 7. Modeling Notes

- No permanent mesh geometry is required.
- Optional reusable helper meshes may include low-poly arc ribbons, claw-slash planes, brand pulse planes, and projectile trail cards.
- Helper meshes should be simple, reusable, and material-driven.
- Spell effects attach to sockets and material masks rather than requiring custom mesh variants.
- Do not create dense modeled glyph rings or physical spell-circle props for ordinary combat casts.

## 8. Texture And Material Notes

Texture targets:

- `T_INF_AbyssalArc_A01_E`
- `T_INF_AbyssalFlame_A01_E`
- `T_INF_BrandPulse_A01_E`
- `T_INF_EyeReveal_A01_E`
- `T_INF_AshMote_A01_BC`

Material instances:

- `MI_INF_AbyssalArc_A01`
- `MI_INF_AbyssalFlame_A01`
- `MI_INF_BrandPulse_A01`
- `MI_INF_EyeReveal_A01`
- `MI_INF_AshMote_A01`

Niagara systems:

- `NS_INF_AbyssalHandCharge_A01`
- `NS_INF_AbyssalBolt_A01`
- `NS_INF_ClawSlashCast_A01`
- `NS_INF_BrandChannel_A01`
- `NS_INF_RegenerationFlare_A01`
- `NS_INF_InvisibleSightReveal_A01`
- `NS_INF_WingMantleCast_A01`
- `NS_INF_RageSurge_A01`

Suggested parameters:

- `User.State`
- `User.BodyBandScale`
- `User.EmissiveIntensity`
- `User.ArcDensity`
- `User.FlameHeight`
- `User.BrandPulseWidth`
- `User.VioletMix`
- `User.TargetLocation`
- `User.SourceSocketName`

## 9. Triangle Budget

No static triangle cost beyond optional reusable helper meshes.

- Arc ribbon helper: under 150 tris.
- Claw slash helper: under 120 tris.
- Projectile trail helper: under 200 tris.
- Brand pulse helper: under 100 tris.

Reuse helpers across systems and drive variation through material UVs, color, dissolve, and Niagara scale.

## 10. LOD Plan

- VFX LOD0: full hand aura, brand pulse, short arcs, ember flicker, limited ash, projectile/trail.
- VFX LOD1: reduce arc count, ash density, and secondary sparks.
- VFX LOD2: preserve hand/eye/brand color blocks and primary projectile only.
- VFX LOD3: disable particles; keep material glow pulses on eyes, hands, or brands where needed.

At every LOD, preserve the gameplay read before preserving decorative sparks.

## 11. Collision Notes

No collision. Gameplay traces, projectiles, cones, and area volumes belong to ability Blueprint/C++ logic. VFX systems should consume source/target transforms but not define gameplay impact.

## 12. Animation Notes

Required animation/VFX sync points:

- `CastWindup`: eyes and brands brighten.
- `HandCharge`: hand aura and arcs intensify.
- `Release`: projectile, claw arc, or burst fires.
- `ChannelLoop`: stable brand-to-hand pulse with low particle count.
- `Regeneration`: chest/core pulse then fading scar glow.
- `Reveal`: eye glow and short violet-red edge pulse.
- `RageSurge`: brief body-wide brand flash, then collapse to eyes/hands.
- `Cooldown`: ash motes and dim ember only.

The effect should respond to `SK_INF_Mage_A01` sockets first, then fall back to base Infernal sockets if class-specific sockets are missing.

## 13. Unreal Import Notes

- Asset type: Niagara systems, helper materials, optional helper meshes.
- Folder path: `/Game/Aerathea/VFX/Infernals/AbyssalSpellcasting/`
- Material path: `/Game/Aerathea/Materials/Infernals/VFX/`
- Texture path: `/Game/Aerathea/Textures/Infernals/VFX/`
- Primary consumers:
  - `/Game/Aerathea/Characters/Infernals/Mage/SK_INF_Mage_A01`
  - `/Game/Aerathea/Materials/Infernals/MI_INF_BrandGlowStates_A01`
  - future `ABP_INF_Mage_A01`
- Use fixed bounds per system and expose bounds scale for Exalted variants.
- Expose parameters to Gameplay Ability and Animation Blueprint.

## 14. Folder And Naming Recommendation

- Package folder: `docs/assets/vfx/VFX_INF_AbyssalSpellcasting_A01/`
- Unreal VFX folder: `/Game/Aerathea/VFX/Infernals/AbyssalSpellcasting/`
- Unreal material folder: `/Game/Aerathea/Materials/Infernals/VFX/`
- Related character package: `docs/assets/characters/SK_INF_Mage_A01/PRODUCTION_PACKAGE.md`
- Related material package: `docs/assets/materials/MI_INF_BrandGlowStates_A01/PRODUCTION_PACKAGE.md`

## 15. Quality Gate Checklist

- Reads as Infernal/Balgoroth magic, not Aetherium, holy magic, Ogre shamanism, or necromancy.
- Preserves flame, lightning-like arcs, glowing eyes, anger, and villain threat.
- Does not hide character hands, eyes, wings, tail, or silhouettes.
- Particle count, bloom, and spark density remain MMO-readable.
- Socket requirements and Niagara parameters are documented.
- Texture targets, material instances, LOD behavior, collision policy, animation sync points, and Unreal paths are included.
