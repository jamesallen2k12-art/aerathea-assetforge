# SM_GIA_BloodAxeCairnTarget_A1_A01 Concept Geometry Brief

## Art Direction Summary

Build a Blood Axe Giant cairn target from the clearer `BloodAxe A1` source image. The asset should read as a low, broken ritual cairn made from heavy dark stone slabs, mud, ash, rawhide ties, and restrained oxide-red Blood Axe paint. It must not read as a generic pile of rocks or a clean round-base marker.

Source target:

- `docs/assets/visual_canon/BloodAxeCairnTargets_A01/VC_GIA_BloodAxe_CairnTarget_A1.png`

Status target for this pass:

- `DCC source candidate pending concept-geometry review`

## Gameplay Purpose

Small-to-medium Blood Axe environmental prop for camp edges, moved-camp residue, ritual paths, raid approach spaces, and highland hostile territory dressing. It should support repeated placement without looking like civilized Giant masonry.

## Silhouette Notes

Required A1 keeper shapes:

- Dominant large diagonal front slab with broken angular face.
- Oxide-red Blood Axe paint on the dominant front slab, not scattered randomly over every rock.
- Taller rear slab rising behind the front mass.
- Left-side bundled stack of flatter stones with rawhide binding.
- Right-side upright support stones, narrower and more vertical than the central slab.
- Small rear shards and broken stakes that prove the asset has actual 360-degree volume.
- Irregular mud, ash, and stone-contact base, not a clean circular pedestal.

Failure conditions:

- Reads as a smooth stone mound.
- Reads as separated pebble pile.
- Uses a round token base.
- Loses the dominant diagonal front slab.
- Lacks authored rear/side massing.

## Scale Notes

- Static prop footprint target: roughly 3.8 m wide x 3.1 m deep.
- Height target: roughly 1.75 m at the tallest rear slab.
- Designed for Giant camp spaces but low enough for player readability and line-of-sight safety.
- Pivot: ground center under the major front slab mass.

## Materials and Color Palette

- Dark blue-gray/charcoal highland stone.
- Cold ash, dark mud, and ochre earth at terrain contact.
- Oxide-red Blood Axe paint as broad marks only.
- Rawhide strips in muted tan-brown.
- No emissive accents for this A1 static prop.

## Concept Image Prompt

Source image already provided and tracked as visual target. If a future cleanup image is needed, use:

Create an original stylized fantasy MMORPG concept image of a Blood Axe Giant low broken cairn target for the world of Aerathea. The design should emphasize a dominant diagonal front stone slab, a taller rear slab, a lashed left stack of flatter stones, right-side support stones, dark highland cairn stone, cold mud and ash grounding, restrained oxide-red Blood Axe paint, brutal Giant raider culture, hostile moved-camp mood, and environmental landmark gameplay role. Use hand-painted texture detail, readable shapes, baked-AO-style depth, normal-map-style surface detail, sparing emissive accents, and MMO-friendly production design. Present it as a multi-angle static prop turnaround on a clean background. Avoid copying any existing franchise and avoid excessive micro-detail that would not translate to a mid-poly Unreal asset.

## Modeling Notes

- Author primary silhouette from slab volumes first.
- Use real geometry for the major stones, large chips, rawhide bands, and broad red paint strips.
- Use texture/normal detail later for hairline cracks, grain, and small chips.
- Build front, right, back, left, and hero proof renders against the A1 target image.
- Do not import to Unreal until the side-by-side DCC comparison passes concept-geometry review.

## Texture and Material Notes

Initial DCC pass may use generated review textures/materials, but final material plan should use:

- `T_GIA_BloodAxeCairnTarget_A1_A01_Stone_BC`
- `T_GIA_BloodAxeCairnTarget_A1_A01_Stone_N`
- `T_GIA_BloodAxeCairnTarget_A1_A01_Stone_ORM`
- `T_GIA_BloodAxeCairnTarget_A1_A01_Earth_BC`
- `T_GIA_BloodAxeCairnTarget_A1_A01_Earth_N`
- `T_GIA_BloodAxeCairnTarget_A1_A01_Earth_ORM`
- `T_GIA_BloodAxeCairnTarget_A1_A01_Rawhide_BC`
- `T_GIA_BloodAxeCairnTarget_A1_A01_Rawhide_N`
- `T_GIA_BloodAxeCairnTarget_A1_A01_Rawhide_ORM`
- `T_GIA_BloodAxeCairnTarget_A1_A01_RedPaint_BC`
- `T_GIA_BloodAxeCairnTarget_A1_A01_RedPaint_N`
- `T_GIA_BloodAxeCairnTarget_A1_A01_RedPaint_ORM`

## Triangle Budget

- Asset class: large static prop.
- LOD0 target: 4k-10k tris.
- LOD1 target: about 60% of LOD0.
- LOD2 target: about 35% of LOD0.
- LOD3 target: about 15-20% of LOD0.
- Material slots: 3-4 max for final; consolidate if the batch later needs tighter performance.

## LOD Plan

- LOD0: full slab cluster, paint strips, rawhide bindings, rubble, uneven ground contact.
- LOD1: remove smallest rubble and simplify secondary chips.
- LOD2: remove small rear shards and minor bindings; keep primary slab silhouette.
- LOD3: retain front slab, rear slab, left mass, right support mass, and terrain silhouette only.

Never remove the dominant front slab or tall rear slab before LOD3.

## Collision Notes

- Use broad UCX hulls for gameplay collision.
- Collision should block the main stone mass and not include every small pebble.
- Keep collision low and conservative so players do not snag on small decorative shards.

## Animation Notes

- None. Static Mesh.

## Unreal Import Notes

- Asset type: Static Mesh.
- Target path: `/Game/Aerathea/Props/Giants/BloodAxe/CairnTargets/A1/SM_GIA_BloodAxeCairnTarget_A1_A01`
- Import after DCC concept comparison approval only.
- Use centimeter scale from Blender export.
- Disable Nanite unless later performance review justifies it for static environment dressing.
- Validate scale, material slots, LOD switching, collision hull, and 360-degree read in an approved review map.

## Folder and Naming Recommendation

- Asset: `SM_GIA_BloodAxeCairnTarget_A1_A01`
- Blender source: `SourceAssets/Blender/Props/Giants/BloodAxe/CairnTargets/A1/SM_GIA_BloodAxeCairnTarget_A1_A01/`
- FBX exports: `SourceAssets/Exports/Props/Giants/BloodAxe/CairnTargets/A1/SM_GIA_BloodAxeCairnTarget_A1_A01/`
- Textures: `SourceAssets/Textures/Props/Giants/BloodAxe/CairnTargets/A1/SM_GIA_BloodAxeCairnTarget_A1_A01/`
- DCC reviews: `Saved/Automation/DCC/SM_GIA_BloodAxeCairnTarget_A1_A01/`
- Docs: `docs/assets/props/SM_GIA_BloodAxeCairnTarget_A1_A01/`

## Quality Gate Checklist

- [ ] Uses `VC_GIA_BloodAxe_CairnTarget_A1.png` as the direct visual target.
- [ ] Dominant diagonal front slab matches the A1 read.
- [ ] Taller rear slab is visible in side/back views.
- [ ] Left lashed stack reads as bundled slabs, not loose rocks.
- [ ] Right support stones read as upright supports.
- [ ] Red paint placement is broad and restrained.
- [ ] Ground contact is irregular mud/ash/debris, not a round pedestal.
- [ ] Front, right, back, left, and hero renders exist.
- [ ] Side-by-side concept comparison sheet exists.
- [ ] Status is not promoted beyond DCC candidate until Flamestrike approves the comparison.
- [ ] Unreal import is blocked until DCC concept-geometry review passes.
