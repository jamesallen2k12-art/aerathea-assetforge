---
name: aerathea-gameplay-systems
description: Build Aerathea gameplay systems. Use for combat, interaction, timing, ability, enemy AI, loot, quest, encounter, objective, Blueprint/native runtime contracts, trace locations, gameplay validators, or ARPG/MMORPG system planning.
---

# Aerathea Gameplay Systems

## Quick Start

1. Read the task packet and gameplay-relevant production docs.
2. Define the runtime contract before implementation.
3. Keep visual, VFX, and art behavior as data-driven hooks when possible.
4. Add deterministic validators for timing, traces, states, and expected references.
5. Do not make final balance claims without playtest evidence.

## Runtime Contract Checklist

- states or phases
- callable functions/events
- replicated or local authority expectations
- timers and cooldowns
- interaction volumes or trace locations
- required sockets/locators
- VFX/material/audio hooks
- persistence expectations
- validation script path

## Approval Gates

Stop for approval before locking:

- class skill identity
- combat pace
- loot economy rules
- MMO backend/vendor assumptions
- multiplayer authority model
- boss or dungeon progression rules
