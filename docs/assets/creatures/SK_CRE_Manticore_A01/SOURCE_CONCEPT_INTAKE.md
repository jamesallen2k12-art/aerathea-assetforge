# SK_CRE_Manticore_A01 Source Concept Intake

## Intake Summary

The base Manticore package consolidates the Aerathea Manticore source set into one reusable creature body, skeleton, material direction, and animation plan. The encounter-specific `SK_CRE_Manticore_Interrupt_A01` should inherit from this base package instead of defining a separate creature rig.

## Source References

| Source | Intake status | Use |
| --- | --- | --- |
| `Manticore.png` | Primary base reference | Dark mane, leathery bat/draconic wings, heavy lion body, curved scorpion tail |
| `Manticore1.png` | Primary base reference | Warm desert/ruin color language, strong wing membrane, upright threat pose |
| `Manticore2.png` | Variant/reference only | White/frost palette and feathered wing direction; do not use for the base wing language |
| `Manticore3.png` | Primary base reference | Storm-dark predator mood, black leathery wings, high hooked tail |
| `Manticore4.png` | Primary base reference | Red-rock desert variant, warm tawny body, red membrane underside |
| `Manticore5.png` | Secondary posture reference | Forest/overgrown stalking posture, mossy weathering; avoid feathered/bird cues |
| `Manticore6.png` | Secondary elite reference | Harness/ruin guardian mood can inform future tamed or named variant, not the base wild body |
| `Manticore7.png` | Variant/reference only | White coast/frost palette and soft wing language; not the base direction |
| `Manticore8.png` | Primary base reference | Ruin-stalker posture, readable tail arc, leathery wings, grounded predator stance |
| `Manticore9.png` | Variant/reference only | Lava/volcanic color variant; useful for future elemental skin |
| `Manticore10.png` | Variant/reference only | Moonlit white/feathered variant; rejected for base because the approved anchor requires bat/draconic wings |
| `GnomevsOgreandManticore8.png` | Encounter reference | Interrupt staging for `SK_CRE_Manticore_Interrupt_A01`, not base anatomy authority |

## Base Direction Decision

Use the dark/tawny ruin predator direction as the base. The base Manticore must read as lion body, leathery wings, and scorpion tail from gameplay distance. White, frost, moonlit, feathered, lava, and armored/tamed interpretations are future variants only.

## Child Routing

| Child ID | Type | Proposed package | Status | Notes |
| --- | --- | --- | --- | --- |
| `ManticoreSet#Base_RuinPredator` | Skeletal creature | `SK_CRE_Manticore_A01` | Package ready | Shared body, skeleton, materials, animation set |
| `GnomevsOgreandManticore8.png#Interrupt` | Encounter variant | `SK_CRE_Manticore_Interrupt_A01` | Package ready; DCC waits on base approval | Uses base rig and adds interrupt pose/VFX timing |
| `ManticoreSet#FrostWhite` | Creature variant | `SK_CRE_Manticore_Frost_A01` | Future package needed | Use only after base is approved |
| `ManticoreSet#Volcanic` | Creature variant | `SK_CRE_Manticore_Volcanic_A01` | Future package needed | Reuse base skeleton with lava material variant |
| `ManticoreSet#TamedGuardian` | Creature variant | `SK_CRE_Manticore_Guardian_A01` | Future package needed | Use harness/ruin guardian cues from `Manticore6.png` |
