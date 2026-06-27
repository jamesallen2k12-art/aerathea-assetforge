# NS_OGR_CrudeTekPylon_A01 Build And Import Status

## Current Status

- Unreal system: `/Game/Aerathea/VFX/Ogres/NS_OGR_CrudeTekPylon_A01`
- Emitter target: `/Game/Aerathea/VFX/Ogres/NE_OGR_CrudeTekPylon_Overload_A01`
- Build state: template-derived first-pass Niagara assets created and saved.
- Runtime binding: assigned to `BP_OGR_CrudeTekPylon_A01` through `PylonNiagaraSystem`.
- Validation: startup validation passes with the system assignment checked.

## Runtime Contract

- Component: `PylonNiagara`
- Native class: `AAETCrudeTekPylonActor`
- Parameters: `User.PylonState`, `User.OverloadPercent`, `User.DamagePercent`, `User.bOverloaded`, `User.bDestroyed`, `User.StateColor`, `User.CoreWorldLocation`, `User.TopArcWorldLocation`

## Remaining Work

1. Replace the template-derived graph with bespoke Ogre Teknomancy arcs, core pulses, and ground sparks.
2. Tune distance culling and scalability.
3. Re-capture the startup review image for visual approval.
