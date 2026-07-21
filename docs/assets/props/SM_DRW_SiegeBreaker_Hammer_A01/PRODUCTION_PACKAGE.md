# SM_DRW_SiegeBreaker_Hammer_A01 Production Package

- Asset name: `SM_DRW_SiegeBreaker_Hammer_A01`
- Asset type: Static Mesh Weapon Prop (two-handed great hammer)
- Culture: Aerathea Dwarven
- Visual canon: `VC-DRW-SiegeBreaker-Hammer-A01`
- Status: concept approved, production package locked
- Approved by Flamestrike on 2026-07-07

## Art Direction Summary

`SM_DRW_SiegeBreaker_Hammer_A01` is a massive Aerathea Dwarven great hammer weapon prop. The design emphasizes a heavy faceted dark runestone head, aged bronze and dark steel dwarven bracing, blue emissive rune inlays, an engraved metal shaft, dark brown crisscross leather grip wrap, and a faceted ornate pommel with blue rune crystal inset.

This is a weapon/prop, not a Mek or vehicle. The previous `SK_GNM_IonaSiegebreakerMek_A01` direction was incorrect and has been superseded by this dwarven hammer concept.

## Gameplay Purpose

- Heavy two-handed dwarven warhammer weapon for NPCs and player use
- Iconic siege-breaking weapon with magical rune properties
- Scales as a signature dwarven legendary-tier weapon

## Silhouette Notes

- Dominant read: massive dark stone hammer head that dwarfs the shaft
- Clear weapon silhouette even at distance
- Stone head is the visual anchor; shaft and pommel support
- No silhouette confusion with staves, axes, or maces

## Scale Notes

- Overall length: 170 cm
- Head max width: 52 cm
- Head height: 38 cm
- Head depth: 32 cm
- Shaft length: 118 cm
- Grip wrap length: 42 cm
- Handle diameter: 5 cm
- Pommel length: 18 cm
- Pommel max width: 11 cm

## Materials And Color Palette

| Material | Palette | Use |
| --- | --- | --- |
| Dark runestone | charcoal, deep blue-black, cracked facets | Hammer head body |
| Aged bronze | warm oxidized bronze, green/copper patina edges | Dwarven bracing, collars, pommel |
| Dark steel | charcoal, soot-black | Rivets, frame, shaft |
| Blue rune emissive | bright blue-white arc | Rune inlays, pommel crystal |
| Dark leather | brown, worn/tanned texture | Grip wrap (crisscross/braided) |
| Carved runes | recessed into stone, subtle gold/copper inlay | Decorative rune grooves |

## Modeling Notes

- Build as a static mesh weapon prop
- Real geometry: main stone head facets, bronze bracing plates, shaft, pommel, grip wrap, rune channels
- Fake with textures: fine stone cracks, rivet heads, leather grain, surface wear, micro-scratches
- Stone head is the most detailed area visually but keep geometry clean
- Grip wrap should read as wrapped leather strips crossing over each other
- Pommel is faceted/ornate but readable as a counterweight

## Texture And Material Notes

Required texture maps:
- `T_DRW_SiegeBreaker_Hammer_A01_BC` (Base Color)
- `T_DRW_SiegeBreaker_Hammer_A01_N` (Normal)
- `T_DRW_SiegeBreaker_Hammer_A01_ORM` (Occlusion/Roughness/Metallic)
- `T_DRW_SiegeBreaker_Hammer_A01_E` (Emissive - blue runes only)

Material slot target: 2-3 max (stone + metal + emissive)

Use packed ORM: Occlusion, Roughness, Metallic. Use emissive only for rune inlays and pommel crystal.

## Triangle Budget

- LOD0 target: 3k-8k tris (large prop range for a detailed weapon)
- Material slot target: 2-3
- Texture target: 2K

## LOD Plan

- LOD0: Full detail, stone facets, bracing, runes, grip wrap, pommel
- LOD1: 60-70% tris, simplify minor bevels and secondary details
- LOD2: 35-45% tris, merge small plates, simplify grip texture geometry
- LOD3: 15-20% tris, preserve head/haft/pommel silhouette only

## Collision Notes

- Simple capsule or convex hull for the shaft
- Convex sphere/polygon for the head
- No collision needed on pommel unless it impacts gameplay
- Collision should be simplified for pick-up/drop physics

## Animation Notes

- Two-handed weapon pickup/placement
- Standard heavy weapon swing animation weight
- Rune glow VFX on active/hit states
- No procedural animation needed on the mesh itself

## Unreal Import Notes

- Asset type: Static Mesh
- Asset name: `SM_DRW_SiegeBreaker_Hammer_A01`
- Folder: `/Game/Aerathea/Weapons/Dwarven/Props/`
- Scale: centimeters (1 cm = 1 Unreal unit)
- Pivot: center of grip area (where hands would hold)
- Collision: convex hull
- Required sockets:
  - `socket_head_impact`
  - `socket_grip_start`
  - `socket_grip_end`
  - `socket_pommel`
  - `socket_rune_l`
  - `socket_rune_r`

## Folder And Naming Recommendation

- Docs: `docs/assets/props/SM_DRW_SiegeBreaker_Hammer_A01/`
- Source: `SourceAssets/Blender/Weapons/Dwarven/SM_DRW_SiegeBreaker_Hammer_A01/`
- Export: `SourceAssets/Exports/Weapons/Dwarven/SM_DRW_SiegeBreaker_Hammer_A01/`
- Unreal: `/Game/Aerathea/Weapons/Dwarven/Props/`
- Textures: `T_DRW_SiegeBreaker_Hammer_A01_*`
- Materials: `MI_DRW_SiegeBreaker_Hammer_A01_*`

## Quality Gate Checklist

- [ ] Stone head reads as faceted runestone, not generic rock
- [ ] Bronze bracing reads as dwarven craftsmanship
- [ ] Blue rune emissives are focal but not overwhelming
- [ ] Leather grip wrap is distinct and readable
- [ ] Scale supports 170 cm overall weapon length
- [ ] Materials match runestone, bronze, steel, leather, and emissive language
- [ ] LOD0-LOD3, collision, sockets, texture maps, and Unreal paths defined
- [ ] Tri count within 3k-8k target
- [ ] Major forms modeled; tiny details in textures/normal maps
