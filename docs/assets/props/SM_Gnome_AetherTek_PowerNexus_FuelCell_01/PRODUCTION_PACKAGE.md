# SM_Gnome_AetherTek_PowerNexus_FuelCell_01 Production Package

## Art Direction Summary

- Asset name: `SM_Gnome_AetherTek_PowerNexus_FuelCell_01`
- Asset type: Static Mesh / Mek chest power fuel cell
- Faction: Gnome / Mekgineer
- Status: Concept candidate / production package draft; approved visual source, Blender source, Unreal import, and visual approval pending

A compact AetherTek Generator fuel cell that slots into a gnome Light Mek chest Power Nexus. It uses dark iron cartridge massing, brass and copper routing hardware, protected blue Aetherium core glow, a front refractor shield lens, and three power-routing hardpoint sockets.

Process note: this package is based on lore and a generated proof pass. It is not visual canon and should not be treated as a DCC source candidate until an approved concept/source package and Blender source are present.

## Gameplay Purpose

Chest-mounted Light Mek power module, workshop display prop, loot/quest object, socket test mesh, and future VFX attachment source for Aetherium power-routing effects.

## Silhouette Notes

Use a compact vertical cartridge silhouette with side capacitors, front protected lens, triangular socket arrangement, and readable brass cage framing. The object should read as engineered Mekgineer hardware, not a loose magic crystal.

## Scale Notes

- Approximate generated dimensions: 62 cm wide, 47 cm deep, 81 cm tall.
- Pivot target: rear-bottom center for Mek chest socketing.
- Scale fit must be validated against the approved Light Mek chest Power Nexus.

## Materials And Color Palette

Dark iron structural body, worn brass collars and lens cage, copper routing traces and capacitors, dark leather rear straps, blue Aetherium core, and restrained cyan refractor glass.

## Concept Image Prompt

Create an original stylized fantasy MMORPG concept image of `SM_Gnome_AetherTek_PowerNexus_FuelCell_01` for the world of Aerathea. The design should emphasize a compact gnome Mekgineer AetherTek fuel-cell cartridge silhouette, brass and copper power routing, dark iron protective housing, a front refractor shield lens, three hardpoint power-routing sockets, blue Aetherium core glow, practical Light Mek chest integration, and production-friendly MMO readability. Use hand-painted texture detail, readable shapes, baked-AO-style depth, normal-map-style surface detail, sparing emissive accents, and mid-poly Unreal asset design. Present it as a front, side, back, top, and three-quarter production sheet on a clean background. Avoid copied franchise designs, excessive micro-detail, uncontrolled glow, and unreadable all-dark forms.

## Modeling Notes

Model the cartridge body, brass collars, front lens cage, side capacitors, socket cups, rear lugs, and main Aetherium core as real geometry. Texture tiny screws, scratches, grime, gauge marks, micro runes, and leather stitching.

## Texture And Material Notes

Generated guide textures:

- `T_SM_Gnome_AetherTek_PowerNexus_FuelCell_01_BC_Guide.png`
- `T_SM_Gnome_AetherTek_PowerNexus_FuelCell_01_N_Guide.png`
- `T_SM_Gnome_AetherTek_PowerNexus_FuelCell_01_ORM_Guide.png`
- `T_SM_Gnome_AetherTek_PowerNexus_FuelCell_01_E_Guide.png`

Final production should replace guide textures with authored hand-painted BaseColor, Normal, packed ORM, and restrained Emissive maps.

## Triangle Budget

Generated proof:

| LOD | Triangles | Named Parts |
| --- | ---: | ---: |
| LOD0 | 1384 | 61 |
| LOD1 | 572 | 22 |
| LOD2 | 344 | 15 |
| LOD3 | 112 | 7 |

Target remains small-prop safe.

## LOD Plan

- LOD0: full cartridge, lens cage, side capacitors, sockets, core, rear mount lugs.
- LOD1: simplified clamps, merged rails, reduced cylinders.
- LOD2: simplified body, core, lens, capacitors, and socket silhouettes.
- LOD3: boxed silhouette with core/lens inset and socket reads.

## Collision Notes

Generated simple convex UCX proxy: `32` tris, one named UCX part. Use simple collision for world placement and disable collision when attached inside a Light Mek chest socket unless gameplay requires interaction.

## Animation Notes

Static mesh baseline. Future material instance may pulse the core. Future Blueprint may expose active, depleted, overloaded, and damaged emissive states.

## Unreal Import Notes

- Suggested folder: `/Game/Aerathea/Props/Mekgineer/Power/`
- Mesh: `SM_Gnome_AetherTek_PowerNexus_FuelCell_01`
- Material instance: `MI_Gnome_AetherTek_PowerNexus_FuelCell_01`
- Pivot: rear-bottom center
- Collision: import UCX proxy
- Sockets: `Socket_PowerRoute_A`, `Socket_PowerRoute_B`, `Socket_PowerRoute_C`
- Validate scale against the Light Mek chest Power Nexus before approval.

## Folder And Naming Recommendation

- Docs: `docs/assets/props/SM_Gnome_AetherTek_PowerNexus_FuelCell_01/`
- Generated source: `SourceAssets/Generated/Props/Mekgineer/SM_Gnome_AetherTek_PowerNexus_FuelCell_01/`
- Unreal target: `/Game/Aerathea/Props/Mekgineer/Power/`

## Quality Gate Checklist

- Gnome/Mekgineer identity is clear.
- Fuel-cell cartridge role is readable.
- Front refractor shield lens is visible.
- Three routing sockets are present.
- Glow is restrained and purposeful.
- LOD0-LOD3 exist.
- Collision proxy exists.
- Guide textures and manifest exist.
- Unreal import validation remains pending.
- Flamestrike final visual approval remains pending.
