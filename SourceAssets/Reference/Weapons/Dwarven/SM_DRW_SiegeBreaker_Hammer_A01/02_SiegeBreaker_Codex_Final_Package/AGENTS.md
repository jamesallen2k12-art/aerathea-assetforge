# AGENTS.md — Siege Breaker

## Mission
Create a game-ready 3D asset for the Aerathean Dwarven Great Hammer Prop named **Siege Breaker**.

## Authority order
1. `asset_spec.json`
2. `dimensions_cm.csv`
3. canonical Blender blockout
4. deterministic true orthographic renders and manifest
5. concept sheet for style only

## Mandatory geometry rules
- Overall bounds: 52 cm X × 32 cm Y × 170 cm Z.
- Head bounds: X ±26 cm, Y ±16 cm, Z 132–170 cm.
- Structural shaft: Z 14–132 cm; 5 cm outer diameter.
- Leather wrap: Z 18–60 cm; 42 cm visible length.
- Pommel: Z 0–18 cm; 11 cm maximum width.
- The shaft inserts 4 cm into the pommel, from Z 14–18 cm.
- Never change these measurements silently.

## Modeling priorities
1. exact envelope and silhouette
2. component assembly
3. large metal braces and stone masses
4. rune panels and medium ornament
5. micro-cracks, engraving, wear, and leather texture

## Required outputs
- `SiegeBreaker_Blockout.blend`
- detailed source `.blend`
- six true orthographic renders plus manifest
- 3/4 beauty render
- UVs and PBR material slots
- collision
- LODs
- FBX and GLB exports
- Unreal validation notes
