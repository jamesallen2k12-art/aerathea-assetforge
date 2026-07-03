# Visual Canon

## Style Target

Aerathea uses a stylized fantasy MMORPG art style with strong readable silhouettes, hand-painted texture detail, baked ambient occlusion, normal-map surface detail, production-friendly mid-poly forms, and restrained emissive accents.

The Aetherium Classic+ target means readable and timeless fantasy presentation with Unreal lighting, stronger atmosphere, cleaner models, and better materials than older classic-MMORPG assets, without photorealistic over-detail.

## Readability And Detail

Primary forms carry the design. Fine detail belongs in textures, normal maps, or baked detail unless it meaningfully affects silhouette or gameplay readability.

Real geometry is reserved for main body forms, large armor plates, major horns, claws, wings, tails, large gears, pipes, weapons, crystals, doors, windows, roofs, pillars, and mechanical joints.

Texture and normal detail carries tiny rivets, fine scratches, wood grain, stone cracks, cloth weave, small runes, micro gears, scale/feather/fur patterns, and stitching.

Glow language is sparse. Emissive maps belong to magic, Aetherium, runes, eyes, lamps, portals, cores, special effects, and state feedback.

## Texture Stack

Standard texture intent includes Base Color/Albedo, Normal, Ambient Occlusion, packed ORM, and optional Emissive for approved glow surfaces.

## Triangle Budget Targets

| Asset Type | LOD0 Target | Material Target | Texture Target |
| --- | ---: | ---: | --- |
| Small prop | 500-4k tris | 1 | 512-1K |
| Large prop | 4k-10k tris | 1-2 | 1K-2K |
| Small character or gnome | 15k-25k tris | 2-3 | 2K, 4K hero only |
| Normal humanoid | 20k-35k tris | 2-3 | 2K, 4K hero only |
| Large creature | 25k-50k tris | 2-4 | 2K-4K |
| Large Mek or boss creature | 35k-70k tris | 3-5 | 4K hero only when justified |
| Dragon or raid boss hero | 60k-100k tris | constrained | aggressive LODs |
| Small building | 12k-22k tris | 2-3 | modular preferred |
| Medium building | 18k-35k tris | 2-4 | modular preferred |
| Large building or fortress piece | 25k-45k tris | 3-5 | impostor or billboard at far distance |

## LOD Strategy

Important assets have LOD0, LOD1, LOD2, and LOD3. Detail reduction preserves the primary silhouette first. Typical reduction order removes tiny bolts/rivets/stitches, small straps and hanging pieces, small spikes, secondary decorative cuts, interior/backside detail, small pipes and ornaments, then minor animation parts.

## Building And Prop Language

Settlement assets use chunky readable silhouettes, timber, stone, brass, dark iron, blue roof shingles where faction-appropriate, warm lantern light, blue Aetherium glow, modular doors/windows/beams/roof pieces/lamps/banners, and hand-painted surface detail.

## Image-First Concept Policy

Approved visual production uses real concept references or image-generation outputs as concept art, followed by production package, DCC, Unreal import, and validation. Procedural Blender or Python output is treated as blockout/proof unless an approved concept sheet already exists.
