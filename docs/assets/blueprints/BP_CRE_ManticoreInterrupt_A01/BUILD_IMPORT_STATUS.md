# BP_CRE_ManticoreInterrupt_A01 Build And Import Status

## Current Status

- Build/import status: native-backed Manticore interrupt wrapper implemented; Blueprint asset created, compiled, placed in startup, and wired to the Gnome/Ogre encounter coordinator.
- Unreal state: `/Game/Aerathea/Blueprints/Creatures/BP_CRE_ManticoreInterrupt_A01`
- Startup actor: `AET_PROD_CRE_Manticore_Interrupt_A01`
- Native class: `AAETManticoreInterruptActor`
- Review scope: first-pass state control for Hidden, Stalking, Telegraph, LeapImpact, ThreatHold, and Retreat phases using the imported `SK_CRE_Manticore_Interrupt_A01` mesh and assigned `NS_CRE_Manticore_Impact_A01` Niagara target. Gameplay timing now exposes a deterministic Stalk/Telegraph/Impact/Hold/Retreat sequence and trace points for future ability binding.

## Runtime Contract

- Mesh component: `ManticoreMesh`
- Marker components: `EntryMarker`, `ImpactMarker`, `RetreatMarker`
- Niagara component: `ImpactNiagara`
- Niagara system: `/Game/Aerathea/VFX/Creatures/NS_CRE_Manticore_Impact_A01`
- Emitter target: `/Game/Aerathea/VFX/Creatures/NE_CRE_Manticore_Impact_A01`
- Layout properties: `EntryOffset`, `ImpactOffset`, `RetreatOffset`
- Gameplay parameters: `StalkSeconds`, `TelegraphSeconds`, `ImpactSeconds`, `ThreatHoldSeconds`, `RetreatSeconds`, `InterruptTraceRadiusCm`, `ImpactDamageRadiusCm`
- Gameplay functions: `BeginInterruptSequence`, `AdvanceInterruptSequence`, `TriggerInterrupt`, `IsInterruptSequenceActive`, `IsImpactWindowActive`, `GetEntryTraceLocation`, `GetImpactTraceLocation`, `GetRetreatTraceLocation`
- Material parameters: `InterruptState`, `SequenceProgress`, `ImpactIntensity`, `InterruptWindowAlpha`
- Niagara parameters: `User.InterruptState`, `User.SequenceProgress`, `User.InterruptWindowAlpha`, `User.InterruptTraceRadius`, `User.ImpactDamageRadius`, `User.bImpact`, `User.bImpactWindowActive`, `User.bInterruptSequenceActive`, `User.ImpactColor`

## Validation

- `Tools/Unreal/validate_startup_scene.py` validates the Blueprint asset, startup actor class, skeletal mesh binding, Niagara system assignment, runtime visibility, optional Niagara component visibility, and encounter coordinator reference.
- `Tools/Unreal/validate_gnome_ogre_gameplay_timing_traces.py` validates the Manticore timeline, impact window, trace locations, and trace/damage radii.
- Latest validation result: passing with `127` expected assets, `47` expected actor labels, and `25` ground tiles.

## Remaining To Finalize

1. Polish final `NS_CRE_Manticore_Impact_A01` impact, dust, venom, and wing-buffet Niagara graph from the template-derived review target, including the new timing and impact-window `User.*` parameters.
2. Replace first-pass Manticore variant geometry with final sculpt/skin/UVs/textures and tuned physics bodies.
3. Add final animation montage binding, tail/wing traces, encounter damage formulas, and interrupt rules after gameplay phase design is approved.
