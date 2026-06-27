# BP_GNM_OGR_BattlefieldEncounter_A01 Gameplay Timing And Trace Contract

## Purpose

This handoff documents the first deterministic gameplay hooks for the approved Gnome/Ogre encounter branch objectives. It does not implement final combat AI, rewards, quest persistence, or balance. It gives Blueprint, ability, and quest code stable timing windows and trace points for the crude Tek pylon objective and Manticore interrupt branch.

## Pylon Objective Window

Native actor:

- `AAETCrudeTekPylonActor`
- Blueprint: `/Game/Aerathea/Blueprints/Ogres/BP_OGR_CrudeTekPylon_A01`
- Startup actor: `AET_PROD_OGR_CrudeTekPylon_A01`

Default gameplay settings:

- `DamageWindowSeconds`: `8.0`
- `RepairWindowSeconds`: `10.0`
- `DamageTraceRadiusCm`: `220.0`
- `RepairTraceRadiusCm`: `180.0`
- `DamagePerTrace`: `0.18`
- `RepairPerTrace`: `0.16`

Callable flow:

1. `TriggerPylonOverload(float NewOverloadPercent)` on the encounter starts the overload state and opens the damage window.
2. `ApplyPylonDamageTrace(float DamageScale)` applies one objective damage pulse while the damage window is active.
3. `AdvanceBranchTiming(float DeltaSeconds)` advances and closes the damage/repair windows.
4. `BeginPylonRepairWindow()` opens the repair window once the encounter reaches the recovery beat.
5. `ApplyPylonRepairTrace(float RepairScale)` applies one repair pulse while the repair window is active.

Trace points:

- Encounter-level pylon trace: `GetPylonTraceLocation()`
- Pylon core trace: `GetCoreTraceLocation()`
- Pylon top arc trace: `GetTopArcTraceLocation()`
- Pylon ground sparks trace: `GetGroundSparksTraceLocation()`

VFX/material additions:

- Material scalar parameters: `DamageWindowAlpha`, `RepairWindowAlpha`
- Niagara parameters: `User.DamageWindowAlpha`, `User.RepairWindowAlpha`, `User.DamageTraceRadius`, `User.RepairTraceRadius`, `User.bDamageWindowActive`, `User.bRepairWindowActive`, `User.GroundSparksWorldLocation`

## Manticore Interrupt Window

Native actor:

- `AAETManticoreInterruptActor`
- Blueprint: `/Game/Aerathea/Blueprints/Creatures/BP_CRE_ManticoreInterrupt_A01`
- Startup actor: `AET_PROD_CRE_Manticore_Interrupt_A01`

Default gameplay settings:

- `StalkSeconds`: `1.2`
- `TelegraphSeconds`: `0.8`
- `ImpactSeconds`: `0.35`
- `ThreatHoldSeconds`: `1.1`
- `RetreatSeconds`: `1.0`
- `InterruptTraceRadiusCm`: `260.0`
- `ImpactDamageRadiusCm`: `320.0`

Callable flow:

1. `BeginInterruptSequence()` starts the Stalking state from elapsed time zero.
2. `AdvanceInterruptSequence(float DeltaSeconds)` or encounter-level `AdvanceBranchTiming(float DeltaSeconds)` advances Stalking, Telegraph, LeapImpact, ThreatHold, and Retreat in order.
3. `TriggerInterrupt()` still supports the review/branch hook by jumping directly to `LeapImpact`.
4. `IsImpactWindowActive()` returns true for `LeapImpact` and `ThreatHold`.

Trace points:

- Encounter-level Manticore impact trace: `GetManticoreImpactTraceLocation()`
- Manticore entry trace: `GetEntryTraceLocation()`
- Manticore impact trace: `GetImpactTraceLocation()`
- Manticore retreat trace: `GetRetreatTraceLocation()`

VFX/material additions:

- Material scalar parameter: `InterruptWindowAlpha`
- Niagara parameters: `User.InterruptWindowAlpha`, `User.InterruptTraceRadius`, `User.ImpactDamageRadius`, `User.bImpactWindowActive`, `User.bInterruptSequenceActive`

## Validation

Use this dedicated validator after changing objective timing, trace locations, or branch state logic:

`/home/Flamestrike/UnrealEngine/UE_5.8.0/Engine/Binaries/Linux/UnrealEditor-Cmd /home/Flamestrike/Projects/Aerathea/Aerathea.uproject -NullRHI -NoRHIThread -NoSplash -Unattended -nop4 -ExecutePythonScript=/home/Flamestrike/Projects/Aerathea/Tools/Unreal/validate_gnome_ogre_gameplay_timing_traces.py`

The validator asserts:

- Pylon damage and repair window settings are positive and callable.
- Pylon damage traces raise `DamagePercent`.
- Pylon repair traces reduce `DamagePercent`.
- Pylon windows close after their configured durations.
- Pylon core, top arc, ground sparks, and encounter trace locations are valid.
- Manticore timing advances through `Stalking`, `Telegraph`, `LeapImpact`, and `Retreat`.
- Manticore impact window and trace locations are valid.

## Deferred Work

- Final player ability classes, damage formulas, resist rules, and repair tools.
- Quest objective text, reward tables, and persistence.
- Spawn balancing and multiplayer authority rules.
- Bespoke Niagara graph polish against the expanded `User.*` parameters.
