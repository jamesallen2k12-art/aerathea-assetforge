# MI_MKG_AetheriumCore_Overcharged_A01 Production Package

## Art Direction Summary

- Asset name: `MI_MKG_AetheriumCore_Overcharged_A01`
- Asset type: Material Instance core variant
- Source: `Gnome Armory.png#Core_Overcharged`
- Parent kit: `KIT_MKG_Armory_A01`
- Source concept: `/home/Flamestrike/Desktop/Aerathea/Aerathea Creative/ASSET CONCEPTS/Gnome Armory.png`
- Faction/theme: Gnome / Mekgineer
- Status: Material production package ready; Unreal material instance not authored yet

Create an original Aerathea gnome/Mekgineer child asset from the armory catalog. This package keeps the compact, rugged, Aetherium-powered language established by `KIT_MKG_Armory_A01` and the first five completed child props.

## Gameplay Purpose

Supports higher-output blue core state for elite or dangerous powered devices. It can also serve future loot, crafting, vendor preview, armory display, equipment socket, and startup-scene review workflows where appropriate.

## Silhouette Notes

Primary read: material-only variant with brighter center and stronger but still restrained emissive pulse. Preserve the large readable forms first; any tiny screws, rivets, wire runs, gauge ticks, and surface scratches must be texture or normal-map detail.

## Scale Notes

shared material instance; avoid full-surface glow. Author in centimeters. Keep handles, grips, buttons, and attachment zones usable by compact 3-4 ft gnomes rather than human-scale proportions.

## Materials And Color Palette

Aetherium blue emissive material state with controlled opacity, pulse, and rim intensity; use dark blue base, saturated blue core, pale highlight, and packed mask/noise only if needed.

## Concept Image Prompt

Create an original stylized fantasy MMORPG concept image of `MI_MKG_AetheriumCore_Overcharged_A01`, a material instance core variant for the world of Aerathea. The design should emphasize material-only variant with brighter center and stronger but still restrained emissive pulse, compact gnome-scale ergonomics, brass and dark-iron engineering, dark leather utility details, restrained blue Aetherium accents, curious Mekgineer culture, and higher-output blue core state for elite or dangerous powered devices. Use hand-painted texture detail, readable shapes, baked-AO-style depth, normal-map-style surface detail, sparing emissive accents, and MMO-friendly production design. Present it as a production asset sheet with front, side, three-quarter view, scale callout, and material callouts on a clean background. Avoid copying any existing franchise and avoid excessive micro-detail that would not translate to a mid-poly Unreal asset.

## Modeling Notes

Create the material instance from the shared Aetherium glow master. Tune scalar/vector parameters for the variant role; do not create unique textures unless the parent master lacks a required mask/noise input.

## Texture And Material Notes

- Material instance: `MI_MKG_AetheriumCore_Overcharged_A01`
- Parent target: `M_AET_AetheriumGlow_Blue_A01` or future `M_MKG_AetheriumCore_Master`
- Parameters: `CoreColor`, `CoreOpacity`, `PulseIntensity`, `RimGlowIntensity`, `NoisePanSpeed`
- Optional textures: `T_MKG_AetheriumCore_A01_Noise`, `T_MKG_AetheriumCore_A01_Mask`
- Emissive must stay readable but restrained at MMO camera distance.

## Triangle Budget

material instance only; no triangle budget.

## LOD Plan

Use material quality switches or scalar reductions at distance. Disable expensive panning/noise on low settings if needed.

## Collision Notes

No collision; material-only child package.

## Animation Notes

Material parameter animation only: low-frequency pulse, opacity, and rim intensity. No spawned lights or particles required.

## Unreal Import Notes

- Unreal path: `/Game/Aerathea/Materials/Props/Mekgineer/Armory/MI_MKG_AetheriumCore_Overcharged_A01`
- Pivot: use the scale notes above; equipped items pivot at grip/attachment point, world props at bottom center unless otherwise stated.
- Scale: centimeters, 1 Unreal unit = 1 cm.
- Collision: simple pickup/display bounds only unless gameplay later requires a dedicated Blueprint.
- Material slot count: follow the texture/material notes above.
- Sockets: add `socket_muzzle`, `socket_beam`, `socket_flame`, `socket_cable`, `back_pack`, or module attachment sockets only when named in scale notes or gameplay purpose.

## Folder And Naming Recommendation

- Docs: `docs/assets/materials/MI_MKG_AetheriumCore_Overcharged_A01/`
- Source: `Content/Aerathea/Materials/Props/Mekgineer/Armory/`
- Export: `No FBX export; material instance authored in Unreal.`
- Unreal: `/Game/Aerathea/Materials/Props/Mekgineer/Armory/MI_MKG_AetheriumCore_Overcharged_A01`

## Quality Gate Checklist

- Original to Aerathea and aligned with the approved gnome/Mekgineer anchor.
- Compact gnome scale and ergonomics are preserved.
- Primary silhouette reads from MMO camera distance.
- Brass, copper, dark iron, leather, and blue Aetherium language is consistent.
- Glow is sparing and justified by a core, lens, muzzle, reactor, or Aetherium shard.
- Tiny rivets, scratches, stitching, and micro gears are texture/normal detail.
- Triangle budget, texture maps, LODs, collision, and Unreal path are defined.
- DCC source waits for approval when body fit, skeleton, or gameplay rules are unresolved.
