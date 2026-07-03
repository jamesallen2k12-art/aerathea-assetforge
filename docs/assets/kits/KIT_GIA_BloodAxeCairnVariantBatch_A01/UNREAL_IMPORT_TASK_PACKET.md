# KIT_GIA_BloodAxeCairnVariantBatch_A01 Unreal Import Task Packet

## Scope

- Packet date: 2026-07-03
- Source status: `DCC game-ready candidate`
- Target status after this task: `Unreal import candidate`
- Out of scope: final visual approval, gameplay route logic, waypoint logic, quest markers, VFX/audio, pickup/loot/salvage behavior, destructible behavior, encounter setup, navmesh approval, and `Fully game-ready` status.

This packet defines the next Unreal import task for the twelve Blood Axe cairn variants. It does not perform the import by itself.

## Import Settings

- Asset type: Static Mesh.
- FBX import uniform scale: `0.01`.
- Combine mesh pieces: enabled.
- Auto-generate collision: disabled.
- Import vertex colors: enabled.
- Normal import: import or preserve source normals where available; do not recompute into a smoothed photoreal look.
- Material import: disabled or replaced with the approved Aerathea material instance after import.
- LOD setup: import the main FBX as the base mesh, then assign `_LOD1.fbx`, `_LOD2.fbx`, and `_LOD3.fbx`.
- `_LOD0.fbx` is an audit/export parity file and should not be required as a separate Unreal LOD import.
- Collision: validate imported simple collision. If UCX is not consumed by the combine-mesh import path, add equivalent broad simple box collision by script and record the fallback.

## Shared Unreal Targets

- Parent material: `/Game/Aerathea/Materials/Giants/BloodAxe/Cairns/M_GIA_BloodAxeCairnVariants_VertexBlend_A01`
- Material instance: `/Game/Aerathea/Materials/Instances/MI_GIA_BloodAxeCairnVariants_A01`
- Texture folder: `/Game/Aerathea/Textures/Giants/BloodAxe/Cairns/KIT_GIA_BloodAxeCairnVariantBatch_A01`
- Planned textures: `T_GIA_BloodAxeCairnVariants_A01_BC`, `T_GIA_BloodAxeCairnVariants_A01_N`, `T_GIA_BloodAxeCairnVariants_A01_ORM`

The first Unreal import test may use a vertex-color material with constant/detail inputs until the shared BC/N/ORM set is authored. Do not add emissive, active waypoint markers, readable symbols, glow strips, or gameplay-colored route marks.

## Asset Import Table

| Asset | Source FBX | Unreal Static Mesh Path | Collision |
| --- | --- | --- | --- |
| `SM_GIA_BloodAxeApproachCairnMarker_A01` | `SourceAssets/Exports/Props/Giants/BloodAxe/StrongholdApproach/CairnMarkers/SM_GIA_BloodAxeApproachCairnMarker_A01/SM_GIA_BloodAxeApproachCairnMarker_A01.fbx` | `/Game/Aerathea/Props/Giants/BloodAxe/StrongholdApproach/CairnMarkers/SM_GIA_BloodAxeApproachCairnMarker_A01` | 1 broad proxy |
| `SM_GIA_BloodAxeRitualCairnGuidepost_A01` | `SourceAssets/Exports/Props/Giants/BloodAxe/RitualStones/Guideposts/SM_GIA_BloodAxeRitualCairnGuidepost_A01/SM_GIA_BloodAxeRitualCairnGuidepost_A01.fbx` | `/Game/Aerathea/Props/Giants/BloodAxe/RitualStones/Guideposts/SM_GIA_BloodAxeRitualCairnGuidepost_A01` | 1 broad proxy |
| `SM_GIA_BloodAxeLowThresholdCairn_A01` | `SourceAssets/Exports/Props/Giants/BloodAxe/CaveApproachMarkers/SM_GIA_BloodAxeLowThresholdCairn_A01/SM_GIA_BloodAxeLowThresholdCairn_A01.fbx` | `/Game/Aerathea/Props/Giants/BloodAxe/CaveApproachMarkers/SM_GIA_BloodAxeLowThresholdCairn_A01` | 1 broad proxy |
| `SM_GIA_BloodAxeCollapsedThresholdCairn_A01` | `SourceAssets/Exports/Props/Giants/BloodAxe/CaveApproachMarkers/SM_GIA_BloodAxeCollapsedThresholdCairn_A01/SM_GIA_BloodAxeCollapsedThresholdCairn_A01.fbx` | `/Game/Aerathea/Props/Giants/BloodAxe/CaveApproachMarkers/SM_GIA_BloodAxeCollapsedThresholdCairn_A01` | 1 broad proxy |
| `SM_GIA_BloodAxeCaveRemnantCairn_A01` | `SourceAssets/Exports/Props/Giants/BloodAxe/CaveApproachMarkers/SM_GIA_BloodAxeCaveRemnantCairn_A01/SM_GIA_BloodAxeCaveRemnantCairn_A01.fbx` | `/Game/Aerathea/Props/Giants/BloodAxe/CaveApproachMarkers/SM_GIA_BloodAxeCaveRemnantCairn_A01` | 1 broad proxy |
| `SM_GIA_BloodAxeCollapsedCaveRemnantCairn_A01` | `SourceAssets/Exports/Props/Giants/BloodAxe/CaveApproachMarkers/SM_GIA_BloodAxeCollapsedCaveRemnantCairn_A01/SM_GIA_BloodAxeCollapsedCaveRemnantCairn_A01.fbx` | `/Game/Aerathea/Props/Giants/BloodAxe/CaveApproachMarkers/SM_GIA_BloodAxeCollapsedCaveRemnantCairn_A01` | 1 broad proxy |
| `SM_GIA_BloodAxeCaveThresholdCairnPair_A01` | `SourceAssets/Exports/Props/Giants/BloodAxe/CaveApproachMarkers/SM_GIA_BloodAxeCaveThresholdCairnPair_A01/SM_GIA_BloodAxeCaveThresholdCairnPair_A01.fbx` | `/Game/Aerathea/Props/Giants/BloodAxe/CaveApproachMarkers/SM_GIA_BloodAxeCaveThresholdCairnPair_A01` | 2 broad proxies |
| `SM_GIA_BloodAxeMovedCampCairnPair_A01` | `SourceAssets/Exports/Props/Giants/BloodAxe/MovedCamp/SM_GIA_BloodAxeMovedCampCairnPair_A01/SM_GIA_BloodAxeMovedCampCairnPair_A01.fbx` | `/Game/Aerathea/Props/Giants/BloodAxe/MovedCamp/SM_GIA_BloodAxeMovedCampCairnPair_A01` | 2 broad proxies |
| `SM_GIA_BloodAxePairedCairnClosePair_A01` | `SourceAssets/Exports/Props/Giants/BloodAxe/CairnGuideposts/SM_GIA_BloodAxePairedCairnClosePair_A01/SM_GIA_BloodAxePairedCairnClosePair_A01.fbx` | `/Game/Aerathea/Props/Giants/BloodAxe/CairnGuideposts/SM_GIA_BloodAxePairedCairnClosePair_A01` | 2 broad proxies |
| `SM_GIA_BloodAxePairedCairnStaggeredPair_A01` | `SourceAssets/Exports/Props/Giants/BloodAxe/CairnGuideposts/SM_GIA_BloodAxePairedCairnStaggeredPair_A01/SM_GIA_BloodAxePairedCairnStaggeredPair_A01.fbx` | `/Game/Aerathea/Props/Giants/BloodAxe/CairnGuideposts/SM_GIA_BloodAxePairedCairnStaggeredPair_A01` | 2 broad proxies |
| `SM_GIA_BloodAxeCairnPathMarker_A01` | `SourceAssets/Exports/Props/Giants/BloodAxe/PathMarkers/SM_GIA_BloodAxeCairnPathMarker_A01/SM_GIA_BloodAxeCairnPathMarker_A01.fbx` | `/Game/Aerathea/Props/Giants/BloodAxe/PathMarkers/SM_GIA_BloodAxeCairnPathMarker_A01` | 1 broad proxy |
| `SM_GIA_BloodAxeCairnScrapCap_A01` | `SourceAssets/Exports/Props/Giants/BloodAxe/PathMarkers/SM_GIA_BloodAxeCairnScrapCap_A01/SM_GIA_BloodAxeCairnScrapCap_A01.fbx` | `/Game/Aerathea/Props/Giants/BloodAxe/PathMarkers/SM_GIA_BloodAxeCairnScrapCap_A01` | 1 broad proxy |

## Metadata To Set

Set these static mesh metadata values during import:

- `Aerathea.StaticMesh.Status=unreal_import_candidate_pending_validation`
- `Aerathea.StaticMesh.SourceStatus=dcc_game_ready_candidate`
- `Aerathea.StaticMesh.Package=KIT_GIA_BloodAxeCairnVariantBatch_A01`
- `Aerathea.StaticMesh.PackageDoc=docs/assets/kits/KIT_GIA_BloodAxeCairnVariantBatch_A01/DCC_GAME_READY_PREP_STATUS.md`
- `Aerathea.StaticMesh.ImportPacket=docs/assets/kits/KIT_GIA_BloodAxeCairnVariantBatch_A01/UNREAL_IMPORT_TASK_PACKET.md`
- `Aerathea.StaticMesh.VisualCanonSource=VC-GIA-BloodAxe-CairnStones-A01`
- `Aerathea.StaticMesh.CollisionPolicy=broad_simple_static_prop_collision`
- `Aerathea.StaticMesh.GameplayBehavior=none_static_environmental_storytelling`
- `Aerathea.StaticMesh.FinalArtAuthored=false`
- `Aerathea.StaticMesh.FinalVisualApproval=pending_flamestrike_review`

## Required Unreal Validation

For each imported static mesh:

- Static mesh asset exists at the target path.
- Bounds remain plausible against the 442 cm / 470 cm Giant scale reference.
- Material slot count is 1.
- Vertex colors are present and visible through the material.
- LOD count is 4.
- LOD1, LOD2, and LOD3 switch without disappearing.
- Simple collision count is at least 1.
- Collision blocks broad traversal without snagging on tiny stone/ribbon detail.
- No emissive material is assigned.
- No Blueprint, route, quest, waypoint, pickup, loot, destructible, damage, VFX, or audio behavior is added.

## Review Placement

After import validation, place the batch in an approved Unreal review row or startup review section only if requested. The row should preserve the contact-sheet order and leave enough spacing to inspect paired assets separately.

## Decision Boundary

Completing this packet promotes the assets to `Unreal import candidate` only after import and validation pass. It still does not approve final aesthetics, gameplay use, Blood Axe route logic, cave entrance logic, objective use, or `Fully game-ready` status.
