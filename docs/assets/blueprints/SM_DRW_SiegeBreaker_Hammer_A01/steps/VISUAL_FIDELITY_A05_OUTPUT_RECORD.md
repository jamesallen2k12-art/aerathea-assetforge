# Siege Breaker A05 Output Record

- Contract: `SB-VF-A05-ORTHOGRAPHIC-VOLUMETRIC`
- Asset: `SM_DRW_SiegeBreaker_Hammer_A01`
- Date: 2026-07-21
- Artifact status: `candidate`
- Pipeline status: `DCC game-ready candidate pending Flamestrike visual approval`
- Unreal authority: `false`
- Fully game-ready: `false`

## Decision Produced

The supplied numeric package, corrected canonical blockout, and freshly
extracted orthographic evidence produced one aligned, genuinely volumetric,
source-clean DCC package. A03/A04 construction input count is zero.

## Exact Outputs

- Blender source: `SourceAssets/Blender/Weapons/Dwarven/SM_DRW_SiegeBreaker_Hammer_A01/OrthographicVolumetric_A05/SM_DRW_SiegeBreaker_Hammer_A01_DCCGameReady_OrthographicVolumetric_A05.blend`
- Blender SHA-256: `ab0d284d82fb3b15c4d398d8a8f83a8eb991a76cb8c1d8f9f0dfb70507011144`
- Evaluated bounds: `51.999998 x 31.999999 x 170.000005 cm`
- LOD triangles: `7144 / 4856 / 3000 / 1428`
- Materials: stone, bronze, steel, leather, restrained rune emissive
- Textures: twenty `2048 x 2048` BC/N/ORM/E maps
- Collision: three custom proxies
- Exports: four FBXs and one GLB
- Independent audit: `pass`, `28/28`
- Final review board SHA-256: `befd52f5668abcbdadb0e8ce5c6798c9ad5a02c711037fe4ba851b59333b5aef`

## Core Controls Proven

- One shared `X=0,Y=0` assembly axis.
- Exact numeric bounds and `Z=0,14,18,60,132,170 cm` frame.
- Real closed volumes and unique multi-angle parallax.
- Zero image cards, facades, billboards, or backing blocks.
- Zero A03/A04 geometry, masks, textures, scales, or derived construction inputs.
- Clean semantic source intake with annotations and paper excluded.
- Closed/manifold source topology and UVs on every source mesh.
- Clean FBX/GLB reimports with exact global bounds.

## Internal Rejection History

Two A05 internal visual attempts were rejected before presentation: the first
for a rectangular head, pale stone hierarchy, missing side strike runes, and
weak leather/rune readability; the second for side-rune coplanar z-fighting.
One topology pass was rejected for open leather-wrap end rings. Those artifacts
were never eligible for Flamestrike approval.

## Pending Gate

Flamestrike must classify the final A05 board as `approved`, `rejected`, or
`blocked`. No Unreal import is authorized by this result.
