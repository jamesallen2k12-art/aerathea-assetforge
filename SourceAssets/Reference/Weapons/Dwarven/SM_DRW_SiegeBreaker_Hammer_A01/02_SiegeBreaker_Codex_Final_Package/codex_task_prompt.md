# Codex Task Prompt — Siege Breaker

Create a game-ready 3D model of **Siege Breaker**, a fictional non-functional Aerathean Dwarven Great Hammer Prop.

## First action
Read `asset_spec.json`, `dimensions_cm.csv`, and `AGENTS.md`. Report the authoritative coordinate system, bounds, measurement anchors, and the 4 cm shaft/pommel overlap before changing any file.

## Phase 1 — deterministic blockout
Run or adapt `blender/build_siege_breaker_blockout.py`. Confirm world-space bounds match:

- X: -26 cm to +26 cm at the head
- Y: -16 cm to +16 cm at the head
- Z: 0 cm to 170 cm overall

Render six true fixed-object views using `blender/render_six_orthographic_views.py`. Do not rotate or regenerate the asset between views. Confirm identical `ortho_scale`, resolution, and pixels-per-centimeter in the generated manifest.

## Phase 2 — detailed modeling
Preserve the canonical blockout envelope. Add:

- fractured dark stone striking blocks
- forged bronze and steel structural braces
- central faceted rune core
- engraved metal shaft
- cross-wrapped leather grip
- faceted pommel
- icy-blue rune inlays

Use the concept sheet only for style. Where visual art conflicts with the canonical geometry, follow the numeric specification.

## Phase 3 — game readiness
- clean topology
- UVs
- PBR material slots
- collision
- LODs
- Unreal-scale validation
- FBX and GLB export

## Deliverables
Write a validation report listing final dimensions, triangle counts, UV sets, material slots, collision method, LODs, export paths, and any deviations.
