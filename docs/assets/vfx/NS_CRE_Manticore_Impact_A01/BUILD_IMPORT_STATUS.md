# NS_CRE_Manticore_Impact_A01 Build And Import Status

## Current Status

- Unreal system: `/Game/Aerathea/VFX/Creatures/NS_CRE_Manticore_Impact_A01`
- Emitter target: `/Game/Aerathea/VFX/Creatures/NE_CRE_Manticore_Impact_A01`
- Build state: template-derived first-pass Niagara assets created and saved.
- Runtime binding: assigned to `BP_CRE_ManticoreInterrupt_A01` through `ImpactNiagaraSystem`.
- Validation: startup validation passes with the system assignment checked.

## Runtime Contract

- Component: `ImpactNiagara`
- Native class: `AAETManticoreInterruptActor`
- Parameters: `User.InterruptState`, `User.SequenceProgress`, `User.bImpact`, `User.ImpactColor`

## Remaining Work

1. Replace the template-derived graph with bespoke dust, claw, wing-buffet, and venom accent emitters.
2. Tune timing to the final Manticore leap/land animation.
3. Re-capture the startup review image for visual approval.
