# SM_GIA_BloodAxeCairnSlabCluster_A01 Production Package

## Art Direction Summary

- Asset name: `SM_GIA_BloodAxeCairnSlabCluster_A01`
- Asset type: Static Mesh prop, Blender art-match proof-of-concept with ArmorPaint handoff
- Visual reference: `VC-GIA-BloodAxe-CairnStones-A01` candidate position `A1`
- Reference crop: `docs/assets/visual_canon/VC_GIA_BloodAxe_CairnStones_A01_A1_Crop.png`
- Faction/theme: Blood Axe Tribe, hostile Giant sub-faction only
- Status: approved A01 proof-of-concept game-ready static prop direction; placed and validated in Unreal as `SM_GIA_BloodAxeCairnSlabCluster_A01_Test2Manual`

This asset translates the `A1` cairn concept into a low Blood Axe slab cluster: collapsed dark stone slabs, ash/mud grounding, restrained oxide red paint, and rawhide lashings. It should read as a Blood Axe remnant immediately, not as an unpainted rock pile.

## Current Game-Ready Candidate

`SM_GIA_BloodAxeCairnSlabCluster_A01_Test2Manual` is the approved proof-of-concept game-ready candidate derived from the brightened A1/Test2 projection process.

- Status: approved by Flamestrike on 2026-07-01 and placed in Unreal.
- Approved pass: `A01-Test2-Bright-01`
- Blender source: `SourceAssets/Blender/Props/Giants/BloodAxe/Cairns/SM_GIA_BloodAxeCairnSlabCluster_A01_Test2Manual/SM_GIA_BloodAxeCairnSlabCluster_A01_Test2Manual.blend`
- FBX and LODs: `SourceAssets/Exports/Props/Giants/BloodAxe/Cairns/SM_GIA_BloodAxeCairnSlabCluster_A01_Test2Manual/`
- Textures: `SourceAssets/Textures/Props/Giants/BloodAxe/Cairns/SM_GIA_BloodAxeCairnSlabCluster_A01_Test2Manual/`
- Review board: `Saved/Automation/DCC/SM_GIA_BloodAxeCairnSlabCluster_A01_Test2Manual/SM_GIA_BloodAxeCairnSlabCluster_A01_Test2Manual_FinalGameReadyReviewBoard.png`
- Unreal mesh: `/Game/Aerathea/Props/Giants/BloodAxe/Cairns/SM_GIA_BloodAxeCairnSlabCluster_A01_Test2Manual`
- Startup actor: `AET_PROD_GIA_BloodAxeCairnSlabCluster_A01_Test2Manual`
- Metrics: LOD0 228 tris; bounds 323.00 cm wide x 156.00 cm deep x 209.00 cm high.
- Note: approved as a static environmental storytelling prop and proof-of-concept workflow target; gameplay interaction, quest marker behavior, destruction, VFX/audio, and combat use remain separate approval gates.

## Gameplay Purpose

Static environmental storytelling only. It suggests old Blood Axe presence, ritual territory, or a moved-camp remnant without creating a waypoint, loot marker, objective marker, route marker, or interaction prop.

## Silhouette Notes

- Low, broad, wider than tall.
- Primary silhouette uses a dominant fallen slab with smaller angled support slabs.
- Secondary upright fragments create a rough hostile profile without becoming a maintained guidepost.
- Red paint crosses the main slab and one side slab, matching the `A1` concept's readable Blood Axe beat.
- Rawhide lashings should sit over real geometry as broad straps, not tiny modeled threads.

## Scale Notes

- Target height: 120-155 cm.
- Target footprint: about 320 cm wide by 230 cm deep.
- Female Giant reference: 442 cm.
- Male Giant reference: 470 cm.
- The asset should feel low for Giants but oversized compared with normal humanoids.

## Materials and Color Palette

- Dark highland stone: charcoal, cold gray, weathered brown-gray.
- Ash/mud base: cold ash gray, soot black, dark mud.
- Blood Axe paint: restrained oxide red, chipped and faded.
- Rawhide: dark tan/brown lashing.
- No emissive, no blue rune language, no polished civic Giant stonework.

## Concept Image Prompt

Create an original stylized fantasy MMORPG static prop concept of a low Blood Axe Giant cairn slab cluster for Aerathea, based on a candidate A1 concept direction: collapsed dark highland stone slabs, broad ash and mud base, restrained faded oxide red paint, rawhide lashings, hostile Giant raider identity, and non-graphic environmental storytelling. Use hand-painted texture intent, readable mid-poly forms, baked-AO-style depth, and MMO-safe geometry. Avoid gore, waypoint symbols, UI markers, emissive glow, polished civilized Giant masonry, and excessive micro-detail.

## Modeling Notes

- Author as a single static prop composition with grouped mesh parts.
- Model real geometry for main slabs, broad support stones, rawhide straps, and ground base.
- Use simple painted geometry for red marks in the POC.
- Keep cracks, small chips, mud streaks, ash speckles, stone grain, and lashing fibers as future texture/normal work.
- Pivot at ground center under the broad footprint.
- Strongest readable side faces +X.

## Texture and Material Notes

Current source material strategy:

- Blender source keeps separate DCC review materials for stone, paint, rawhide, ash, and mud so the proof can stay close to the `A1` concept during the manual paint pass.
- Starter BC, N, and ORM texture map outputs exist at 1024 x 1024.
- Painted preview BC, N, and ORM texture map outputs exist at 2048 x 2048 for aesthetic review only.
- ArmorPaint handoff exists at `SourceAssets/ArmorPaint/Props/Giants/BloodAxe/Cairns/SM_GIA_BloodAxeCairnSlabCluster_A01/`.
- Paint-target FBX, concept reference, current review image, and starter maps are staged for a manual concept-match texture pass.
- Final Unreal material consolidation should happen after Flamestrike approves the painted result.

## Triangle Budget

- LOD0 target: 900-3.5k tris.
- LOD1 target: 500-1.8k tris.
- LOD2 target: 250-900 tris.
- LOD3 target: 100-350 tris.
- Collision proxy: 1-3 simple hulls.

## LOD Plan

- LOD0: full slab cluster, ground base, red paint geometry, broad rawhide straps.
- LOD1: remove small support stones and reduce bevel/detail.
- LOD2: keep primary slabs, simplified base, and one red paint beat.
- LOD3: preserve low mound silhouette and one broad red mark.

## Collision Notes

POC creates a simple UCX collision proxy source around the main footprint only. Collision correctness is not approved until Unreal import and gameplay placement are validated.

## Animation Notes

Static mesh only. No cloth simulation, physics, destruction, VFX, audio, or gameplay states.

## Unreal Import Notes

Future Unreal path:

`/Game/Aerathea/Props/Giants/BloodAxe/Cairns/SM_GIA_BloodAxeCairnSlabCluster_A01`

Import as Static Mesh with centimeter scale, ground-center pivot, no sockets, LOD0-LOD3 source available, simple collision proxy source, and no Blueprint behavior.

For the next Unreal pass, import the accepted painted BC/N/ORM maps if Flamestrike approves them. The generated starter maps are fallback only. Collapse the final import to the smallest practical material-slot count during Unreal validation.

## Folder and Naming Recommendation

- Blender source: `SourceAssets/Blender/Props/Giants/BloodAxe/Cairns/SM_GIA_BloodAxeCairnSlabCluster_A01/`
- FBX export: `SourceAssets/Exports/Props/Giants/BloodAxe/Cairns/SM_GIA_BloodAxeCairnSlabCluster_A01/`
- Texture source output: `SourceAssets/Textures/Props/Giants/BloodAxe/Cairns/SM_GIA_BloodAxeCairnSlabCluster_A01/`
- ArmorPaint handoff: `SourceAssets/ArmorPaint/Props/Giants/BloodAxe/Cairns/SM_GIA_BloodAxeCairnSlabCluster_A01/`
- DCC proof: `Saved/Automation/DCC/SM_GIA_BloodAxeCairnSlabCluster_A01/`
- Build script: `Tools/DCC/build_bloodaxe_cairn_slab_cluster_poc.py`
- Paint launcher: `Tools/DCC/launch_armorpaint_cairn_A01.sh`

## Quality Gate Checklist

- [x] Reads as Blood Axe, not plain rocks; approved by Flamestrike for the Test2Manual proof-of-concept lane.
- [x] Matches `A1` low slab-cluster direction; approved by Flamestrike for the Test2Manual proof-of-concept lane.
- [x] Separates Blood Axe from civilized Giant stonework.
- [x] Uses readable mid-poly shapes.
- [x] Includes LOD source collections.
- [x] Includes simple collision proxy source.
- [x] Includes DCC proof render.
- [x] Includes main FBX plus LOD0-LOD3 FBX handoffs.
- [x] Includes 1024 x 1024 BC/N/ORM texture map outputs.
- [x] Includes 2048 x 2048 BC/N/ORM painted preview maps.
- [x] Includes ArmorPaint handoff files for manual concept-match painting.
- [x] Brightened projected BC/N/ORM Test2Manual maps approved by Flamestrike for this proof-of-concept static prop.
- [x] Final Test2Manual Unreal material-slot count and material hookup validated.
- [x] Makes no gameplay, quest marker, VFX/audio, destruction, combat, or interaction claim.
