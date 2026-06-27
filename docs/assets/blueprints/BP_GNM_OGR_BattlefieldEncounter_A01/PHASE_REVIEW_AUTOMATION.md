# BP_GNM_OGR_BattlefieldEncounter_A01 Phase Review Automation

## Purpose

This note tracks the deliberate review hooks for the Gnome/Ogre encounter coordinator. The startup map still supports the normal auto-advancing phase loop, but review captures can now force a single phase before the offscreen screenshot is taken.

## Command-Line Phase Hook

`AAETReviewCameraDirector` accepts either command-line key:

- `-AETEncounterPhase=ShieldImpact`
- `-AETReviewEncounterPhase=ShieldImpact`

Supported values:

- `Setup`
- `GnomeHoldLine`
- `OgreAdvance`
- `ShieldImpact`
- `PylonOverload`
- `CasterReinforcement`
- `ManticoreInterrupt`
- `Resolution`

Optional capture timing override:

- `-AETReviewCaptureDelay=0.45`

## Capture Tooling

Use this for the four branch review frames:

`Tools/Unreal/capture_gnome_ogre_phase_reviews.sh`

Default output:

`Saved/Automation/GnomeOgrePhaseReview/`

Generated files:

- `AeratheaStartupReview_ShieldImpact.png`
- `AeratheaStartupReview_PylonOverload.png`
- `AeratheaStartupReview_CasterReinforcement.png`
- `AeratheaStartupReview_ManticoreInterrupt.png`

For one-off captures, set `AET_REVIEW_ENCOUNTER_PHASE` before the standard startup capture script:

`AET_REVIEW_ENCOUNTER_PHASE=PylonOverload Tools/Unreal/capture_startup_review_offscreen.sh`

## Validation

Use the encounter-specific validator after C++ or Blueprint phase changes:

`/home/Flamestrike/UnrealEngine/UE_5.8.0/Engine/Binaries/Linux/UnrealEditor-Cmd /home/Flamestrike/Projects/Aerathea/Aerathea.uproject -NullRHI -NoRHIThread -NoSplash -Unattended -nop4 -ExecutePythonScript=/home/Flamestrike/Projects/Aerathea/Tools/Unreal/validate_gnome_ogre_encounter_phase_sequence.py`

The validator asserts:

- Dependencies validate.
- Auto phase sequence reaches all seven review states in order.
- Shield impact drives the shieldwall `Impact` state and intensity.
- Pylon overload drives the pylon `Overload` state and overload percent.
- Manticore interrupt drives the `LeapImpact` state and sequence progress.

## Review Rule

Before presenting a phase capture for approval, inspect the generated PNG for orientation, framing, actor visibility, and obvious clipping. If orientation is uncertain, use the existing A/B/C/D/E marker pass before generating clean phase captures.
