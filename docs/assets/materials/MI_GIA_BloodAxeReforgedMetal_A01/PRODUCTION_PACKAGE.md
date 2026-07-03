# MI_GIA_BloodAxeReforgedMetal_A01 Production Package

## Art Direction Summary

- Asset name: `MI_GIA_BloodAxeReforgedMetal_A01`
- Asset type: Material Instance / shared Blood Axe Giant armory material
- Parent material target: future `M_AET_WeaponMetal_Handpainted` or equivalent stylized weapon-metal master
- Source kit: `KIT_GIA_BloodAxeArmory_A01`
- Source concept reference: `BloodAxeArmory.png#Material_ReforgedMetal`
- Faction/theme: Blood Axe Tribe, hostile Giant sub-faction
- Status: docs-only material production package ready
- Source-storage guardrail: keep `BloodAxeArmory.png` in the external source concept folder only. Do not copy, move, edit, embed, or commit the source image for this package.

`MI_GIA_BloodAxeReforgedMetal_A01` defines the shared blackened, hammered, stolen-and-reforged metal language for Blood Axe Giant raider weapons, armor plates, quivers, bow fittings, camp hardware, and future scrap-pile dressing. It should read as brutal field-forged war gear: dark iron, dull steel, soot, chipped red paint, broad hammer marks, grime, and rough leather contact wear. It must not replace neutral or civilized Giant material language, which remains blue-gray stonework, warm hearth light, restrained storm/rune accents, and practical highland craft.

## Gameplay Purpose

This material gives Blood Axe armory assets a consistent sub-faction identity across weapon silhouettes, gear modules, and camp props. It supports:

- `SM_GIA_BloodAxeDoubleAxe_A01`
- `SM_GIA_BloodAxeCrusherHammer_A01`
- `SM_GIA_BloodAxeLongbow_A01` metal caps and trophy bindings
- `KIT_GIA_BloodAxeQuivers_A01` buckles, arrowheads, rivet plates, and rack hardware
- Future Blood Axe cleaver, hook spear, knife, armor, banner pole, scrap pile, forge, and camp hardware packages

The material should help players identify hostile Blood Axe gear quickly at MMO camera distance without relying on tiny scratches, readable text, or dense trophy clutter.

## Silhouette Notes

The material does not create silhouette by itself, so the package must reinforce existing modeled forms rather than hide them. Use value separation and broad painted wear to support:

- Large axe blades and hammer faces.
- Thick haft bands, socket collars, and end caps.
- Armor plates, oversized buckles, quiver hardware, and arrowheads.
- Large reforged seams, weld scars, and hammered panels.
- Red war-paint slashes on broad planes only.

Avoid high-frequency pitting, tiny rivet fields, dense scratches, or repeated small highlights that make weapon heads and armor plates noisy. Small surface damage belongs in normal/roughness detail at restrained strength, not as a visual carpet.

## Scale Notes

Use the validated `SK_GIA_Base_A01` scale lock for all assets using this material:

- Female Giant baseline: 442 cm / 14'6".
- Male Giant baseline: 470 cm / 15'5".
- Approved Giant ranges: females 14-15 ft / 427-457 cm; males 14'10"-16'0" / 452-488 cm.
- Author texture density for Giant-scale props and armor, not normal humanoid weapon scale.

Texture detail must account for broad Giant weapon faces and armor plates. Hammer marks, red paint bands, ash streaks, and edge wear should remain readable on objects that may be 300-460 cm long. Micro scratches may exist in the normal and roughness maps, but they should not be the main read.

## Materials And Color Palette

Base material language:

- Blackened iron: charcoal gray, blue-black shadow, low-saturation cool undertones.
- Dark steel: muted gunmetal, worn edge highlights, broad plane variation.
- Reforged scrap plates: uneven but readable panels with hammered deformation.
- Red war paint: deep oxide red, chipped and rubbed away on high-contact edges.
- Soot and ash: matte gray-black deposits near grips, sockets, forge seams, and lower camp hardware.
- Dried grime: brown-black accumulation in recessed areas, used subtly.
- Leather contact wear: rough brown-black rub marks where metal meets straps or quiver rims.

Recommended color ranges:

- Base metal color: `#151719` to `#2A2C2E`
- Worn steel edge color: `#555A5C` to `#787B78`
- Oxide red paint: `#5F1513` to `#8B211B`
- Soot: `#0B0A09` to `#24201C`
- Ash dust: `#6A6458` to `#8A8275`
- Grime: `#2B2019` to `#403025`

No default emissive is approved for this material. A future forge-heat or shamanic variant may add a restrained `E` map, but that requires visual approval and a separate material state package.

## Concept Image Prompt

Create an original stylized fantasy MMORPG material sheet of `MI_GIA_BloodAxeReforgedMetal_A01` for the world of Aerathea. The design should emphasize blackened iron, dark steel, stolen scrap metal reforged into Giant raider weapons, broad hammer marks, chipped deep red war paint, soot, ash, rough grime, scorched leather contact wear, hostile Blood Axe sub-faction identity, and MMO-readable material zones for enormous axes, crusher hammers, giant bow fittings, quiver hardware, and armor plates. Use hand-painted texture detail, baked-AO-style depth, normal-map-style surface detail, restrained roughness variation, no default emissive glow, and production-friendly tiling or trim-sheet planning. Present it as a clean material board with swatches, flat sample plates, curved weapon-head samples, edge-wear callouts, ORM callouts, and scale notes for a 442 cm female Giant and a 470 cm male Giant. Avoid copying any existing franchise, avoid graphic gore, avoid making Blood Axe materials the default Giant culture, and avoid excessive micro-detail that would not translate to mid-poly Unreal assets.

## Modeling Notes

This is a material package only. It does not authorize mesh creation. Future mesh packages using this material should model:

- Primary weapon heads, sockets, bands, end caps, armor plates, and bow fittings.
- Large broken or reforged seams when they affect silhouette or panel layout.
- Major dents and large chipped blade shapes only where the mesh form benefits from them.
- Oversized rivets or studs only when they are few, silhouette-readable, and mechanically important.

Texture or normal-map:

- Fine scratches.
- Dense pitting.
- Tiny rivets.
- Small hammer marks.
- Hairline cracks.
- Minor weld texture.
- Small soot speckles.
- Thin red paint chips.

The material should be reusable across multiple Blood Axe assets by relying on masks, trim strips, and broad value blocks rather than custom one-off ornament for every prop.

## Texture And Material Notes

Texture set target:

- `T_GIA_BloodAxeReforgedMetal_A01_BC`
- `T_GIA_BloodAxeReforgedMetal_A01_N`
- `T_GIA_BloodAxeReforgedMetal_A01_ORM`
- Optional future approval-gated `T_GIA_BloodAxeReforgedMetal_ForgeHeat_A01_E`

Packed `ORM` channel plan:

- R: Ambient occlusion, with moderate darkening around plate overlaps, socket collars, and major dents.
- G: Roughness, generally high and matte, with edge-polished bands and worn grip-contact areas slightly lower.
- B: Metallic, high for iron/steel zones and zero for painted grime, soot, leather contamination, or ash overlays.

Parameter plan:

- `BaseTint`: broad metal tint, default dark gunmetal.
- `EdgeWearStrength`: controls worn steel exposure on convex edges.
- `HammerMarkNormalStrength`: restrained normal-map intensity for large and medium hammer marks.
- `SootAmount`: matte soot overlay, clamped to avoid hiding silhouette.
- `RedPaintAmount`: deep red paint mask intensity for Blood Axe identification.
- `RedPaintChipping`: breaks up red paint with broad chips, not dense noise.
- `GrimeInCavities`: cavity dirt strength, paired with AO.
- `RoughnessBias`: final roughness adjustment for weapon versus armor use.
- `ForgeHeatAmount`: default `0.0`; reserved for future approval-gated forge-heat variant.

Suggested scalar limits for future validator:

- `EdgeWearStrength`: `0.15` to `0.45`
- `HammerMarkNormalStrength`: `0.08` to `0.30`
- `SootAmount`: `0.05` to `0.35`
- `RedPaintAmount`: `0.10` to `0.55`
- `RedPaintChipping`: `0.20` to `0.60`
- `GrimeInCavities`: `0.10` to `0.45`
- `RoughnessBias`: `0.60` to `0.90`
- `ForgeHeatAmount`: locked to `0.0` until approved

## Triangle Budget

This material has no triangle budget by itself. Meshes using it should follow their own package budgets:

- Giant weapon heads and shafts: commonly 2k-10k tris depending on hero status.
- Quiver hardware and arrowheads: usually 3k-8k tris for the full quiver assembly.
- Wearable armor plates: 5k-12k tris per major module.
- Camp hardware and scrap piles: 8k-18k tris for composed dressing clusters.

Do not add geometry just to express small metal noise. Use material channels for fine detail and reserve geometry for large plates, blade silhouettes, sockets, and structural bands.

## LOD Plan

Material behavior must remain readable across LOD0-LOD3:

- LOD0: full normal-map detail, edge wear, red paint, soot, AO, and roughness variation.
- LOD1: preserve broad red paint masks, major edge wear, and plate-value separation; reduce fine normal intensity if shimmer appears.
- LOD2: keep big material zones and silhouette-supporting edge highlights; rely less on small scratches.
- LOD3: preserve blackened metal versus red-paint identification and broad weapon-head readability; small hammer marks may fade.

Future material validator should flag excessive tiling, noisy normal strength, emissive enabled without approval, or red paint masks that dominate more than half of the visible metal surface on neutral-use parts.

## Collision Notes

This material does not define collision. Meshes using it should rely on their package collision rules:

- Equipped weapons: collision disabled by default, with combat traces handled through sockets.
- Display weapons and camp props: simple boxes, capsules, or low-count convex hulls.
- Quiver hardware and arrowheads: collision on the quiver body or bundle, not per tiny fitting.
- Armor plates: skeletal attachment and physics asset rules from the Giant character package.

Material masks must not imply gameplay hit zones, weak points, damage types, or harvesting rules without a separate gameplay approval.

## Animation Notes

This material is static by default. No animated emissive, scrolling, pulsing, heat shimmer, or material-state timing is approved in this docs-only package.

Future optional states, each approval-gated:

- `ForgeHeat`: faint ember warmth at recent-forge seams or hot ingot props.
- `FreshImpactSpark`: event-only VFX/material response for a scripted strike.
- `ShamanicMarkedMetal`: separate Blood Axe shaman material variant, not a default armory material.

Any animated material state must keep bloom restrained and preserve MMO camera readability.

## Unreal Import Notes

Planned Unreal folder:

- `/Game/Aerathea/Materials/Giants/BloodAxe/`

Planned Unreal assets:

- `MI_GIA_BloodAxeReforgedMetal_A01`
- Future parent, if needed: `M_AET_WeaponMetal_Handpainted`
- Future material function, if needed: `MF_AET_EdgeWear_Handpainted`

Planned texture assets:

- `T_GIA_BloodAxeReforgedMetal_A01_BC`
- `T_GIA_BloodAxeReforgedMetal_A01_N`
- `T_GIA_BloodAxeReforgedMetal_A01_ORM`

Import rules:

- Use sRGB enabled for `BC`.
- Use sRGB disabled for `N`, `ORM`, and any future `E` mask.
- Use texture group appropriate for weapons/characters, not UI.
- Default resolution target: 1K for shared trim or small hardware, 2K for hero weapon material samples, 4K only for approved hero/boss close-up use.
- Keep material slot count low on consuming meshes: usually one shared metal slot plus optional handle/leather/cloth slot.
- No Unreal material graph, texture asset, or shader authoring is included in this package.

## Folder And Naming Recommendation

- Docs folder: `docs/assets/materials/MI_GIA_BloodAxeReforgedMetal_A01/`
- Package: `docs/assets/materials/MI_GIA_BloodAxeReforgedMetal_A01/PRODUCTION_PACKAGE.md`
- Planned Unreal folder: `/Game/Aerathea/Materials/Giants/BloodAxe/`
- Planned material instance: `MI_GIA_BloodAxeReforgedMetal_A01`
- Planned texture prefix: `T_GIA_BloodAxeReforgedMetal_A01`

Related consuming packages:

- `docs/assets/kits/KIT_GIA_BloodAxeArmory_A01/PRODUCTION_PACKAGE.md`
- `docs/assets/props/SM_GIA_BloodAxeDoubleAxe_A01/PRODUCTION_PACKAGE.md`
- `docs/assets/props/SM_GIA_BloodAxeCrusherHammer_A01/PRODUCTION_PACKAGE.md`
- `docs/assets/props/SM_GIA_BloodAxeLongbow_A01/PRODUCTION_PACKAGE.md`
- `docs/assets/kits/KIT_GIA_BloodAxeQuivers_A01/PRODUCTION_PACKAGE.md`

## Approval Gates

- DCC and texture authoring approval is required before creating source textures, trim sheets, baked maps, or material sample meshes.
- Unreal approval is required before creating parent material graphs, material instances, texture assets, or validators.
- Visual approval is required before enabling forge heat, shamanic glow, animated material states, or any emissive map.
- Culture approval is required if this red-black Blood Axe material language starts replacing neutral/civilized Giant stoneworker materials.
- Source-storage approval is required before copying or embedding `BloodAxeArmory.png` or any external concept into the repository.
- Gameplay approval is required before material masks imply damage types, loot rarity, interactable forging, weak points, or combat feedback.

## Quality Gate Checklist

- Blood Axe remains a hostile Giant sub-faction, separate from neutral/civilized Giant culture.
- Giant scale lock is explicit: female baseline 442 cm / 14'6", male baseline 470 cm / 15'5", with approved Giant ranges documented.
- Material supports huge Giant-scale weapon, armor, bow, quiver, and camp hardware surfaces.
- Base color, normal, ORM, and optional future emissive targets are named.
- Default material has no emissive, no animated state, and no bloom dependency.
- Red paint is a restrained sub-faction accent, not a full-surface palette replacement.
- Tiny scratches, pitting, rivets, and hammer noise are texture/normal detail, not geometry requirements.
- Parameter ranges are defined for future validator work.
- Unreal folder, asset names, texture names, sRGB rules, and material slot guidance are documented.
- Package makes no DCC, FBX, Unreal Content, runtime, source asset, texture authoring, global index, startup-scene, or source-concept-copying claim.
