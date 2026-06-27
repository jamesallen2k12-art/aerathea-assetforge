# KIT_OGR_Teknomancy_A01 Child Asset Intake

## Intake Summary

The Ogre Teknomancy sources are collage-like kit references. They should be split into child assets before DCC production so workshop, siege-yard, and equipped-character pieces stay reusable.

## Child Assets

| Child Asset | Type | Primary Sources | Status | Notes |
| --- | --- | --- | --- | --- |
| `SM_OGR_TekCannon_A01` | Static Mesh / optional Blueprint Actor | `OgreTekShop.png`, `Ogres10.png`, `Ogres11.png` | Package needed | Massive siege cannon with orange rune barrel, reinforced wheels/base, recoil socket, and simple blocking collision. |
| `SM_OGR_ForgeReactor_A01` | Static Mesh / Blueprint Actor | `OgreTekShop.png`, `Ogres10.png` | Package needed | Vertical forge-reactor tower with furnace windows, vent pipes, hoist points, and glow pulse option. |
| `SM_OGR_PressureTank_A01` | Static Mesh | `OgreTekShop.png`, `Ogres10.png` | Package needed | Heavy cylindrical tank with brass bands, pressure gauge, chains, and vent socket. |
| `SM_OGR_TekWorkbench_A01` | Static Mesh | `OgreTekShop.png`, `Ogres10.png` | Package needed | Ogre-height workbench for tools, crates, hammering, and powered assemblies. |
| `SM_OGR_PoweredHammer_A01` | Static Mesh / weapon attachment | `OgreMaleTek.png`, `OgreTekvsGnomeMek.png`, `OgreSmiths.png` | Package needed | Oversized powered hammer for `SK_OGR_Teknomancer_A01`; grip sockets and hammer-core VFX required. |
| `SM_OGR_BracerEngine_L_A01` | Skeletal attachment / Static Mesh | `OgreMaleTek.png`, `OgreTekvsGnomeMek.png` | Package needed | Left/right bracer modules with vents, rune heat, and optional discharge sockets. |
| `SM_OGR_BeltReactor_A01` | Skeletal attachment | `OgreMaleTek.png`, `OgreTekvsGnomeMek.png` | Package needed | Waist or chest reactor module for Teknomancer class silhouette. |
| `SM_OGR_CoilBackRig_A01` | Skeletal attachment | `OgreMaleTek.png`, `OgreTekShop.png` | Package needed | Optional back-mounted pressure/coil rig using `spine_teknomancy_pack`. |
| `SM_OGR_ShieldBarricade_A01` | Static Mesh | `Ogres11.png` | Package needed | Heavy rune shield and field barricade for siege-yard cover. |
| `SM_OGR_HoistChain_A01` | Static Mesh / optional animated prop | `OgreTekShop.png`, `Ogres10.png` | Package needed | Large chain, hook, and hanging crate support; low-frequency sway only if animated. |
| `SM_OGR_TekToolCrate_A01` | Static Mesh | `OgreTekShop.png`, `Ogres10.png`, `OgreSmiths.png` | Package needed | Reusable tool/parts crate with blackened iron, chains, and glowing small core variant. |
| `BP_OGR_TekCannon_A01` | Blueprint Actor | `SM_OGR_TekCannon_A01` | Later implementation | Handles recoil, muzzle VFX socket, disabled/charged states, and simple interaction. |

## Shared Rules

- Keep child asset pivots production-friendly: bottom center for world props, grip point for weapons, socket contact point for character attachments.
- Use shared Ogre Teknomancy material instances wherever possible.
- Build major shape in geometry; bake scratches, tiny runes, small rivets, and wire tangles.
- Keep large powered props modular enough for both forge interiors and outdoor siege yards.
