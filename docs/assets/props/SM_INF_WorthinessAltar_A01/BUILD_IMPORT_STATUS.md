# SM_INF_WorthinessAltar_A01 Build And Import Status

Last updated: 2026-06-28

## Status

First-pass DCC/Unreal review implementation and native Blueprint wrapper are complete and validated.

## Approved Direction

- User approval cleared the package handoff gate on 2026-06-28.
- Cleaned infernal gate reference used for readability direction: `Saved/ReferenceAdjustments/Infernals_Guarding_a_Gate2_Bright20_A04_RivetReduced_Stronger.png`.
- Production rule carried into the mesh: broad Balgoroth altar forms only; tiny rivets, micro-scratches, heat stress, ash, and fine cracks remain texture/normal-map work.

## Generated Source

- Blender source: `SourceAssets/Blender/Props/Infernals/BalgorothCult/SM_INF_WorthinessAltar_A01/SM_INF_WorthinessAltar_A01.blend`
- FBX export: `SourceAssets/Exports/Props/Infernals/BalgorothCult/SM_INF_WorthinessAltar_A01/SM_INF_WorthinessAltar_A01.fbx`
- DCC proof render: `Saved/Automation/InfernalWorthinessAltarReview/SM_INF_WorthinessAltar_A01_DCCReview.png`

## Unreal Assets

- Static mesh: `/Game/Aerathea/Props/Infernals/BalgorothCult/SM_INF_WorthinessAltar_A01`
- Blueprint wrapper: `/Game/Aerathea/Blueprints/Infernals/BP_INF_RitualAltar_A01`
- Native class: `AAETInfernalRitualAltarActor`
- Startup actor: `AET_PROD_INF_WorthinessAltar_A01`
- Material parents: `/Game/Aerathea/Materials/Infernals/WorthinessAltar/M_INF_WorthinessAltar_*_Blockout_A01`
- Material instances: `/Game/Aerathea/Materials/Instances/MI_INF_WorthinessAltar_A01_*`
- Startup level: `/Game/Aerathea/Maps/L_Aerathea_Startup`

## Validation

- Focused Blueprint validator: `Tools/Unreal/validate_infernal_ritual_altar_blueprint.py`
- Mesh-level validator: `Tools/Unreal/validate_infernal_worthiness_altar.py`
- Startup validator: `Tools/Unreal/validate_startup_scene.py`
- Focused Blueprint result: passed, `356.00h x 404.00w x 346.00d cm`, bounds radius `320.03 cm`, 9 components, 6 state materials, 6 Niagara systems.
- Mesh-level result: passed, `356.00h x 404.00w x 346.00d cm`, bounds radius `320.03 cm`, 9 sockets.
- Startup result: passed, `233 assets`, `55 expected actors`, `25 ground tiles`.

## Remaining Work

- Replace first-pass review geometry with final sculpt/retopo.
- Author UVs, final texture sets, and final authored LODs.
- Tune collision after final silhouette and wing/tail clearance review.
- Polish bespoke WorthinessJudgment Niagara graphs against the native `User.*` contract.
