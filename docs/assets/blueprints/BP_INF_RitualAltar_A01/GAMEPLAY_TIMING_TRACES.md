# BP_INF_RitualAltar_A01 Gameplay Timing And Trace Contract

Last updated: 2026-06-28

## Purpose

This document defines the runtime sequence that quest, combat, VFX, audio, and UI work can rely on for `BP_INF_RitualAltar_A01`.

The contract is validated by `Tools/Unreal/validate_infernal_ritual_altar_timing_traces.py` against the placed startup actor `AET_PROD_INF_WorthinessAltar_A01`.

## Timed State Flow

| Step | Call | Expected result |
| --- | --- | --- |
| Reset | `ResetRitual()` | `Smolder`, `TrialProgress = 0.0`, `bRitualActive = false` |
| Start | `StartTrial()` | `TrialActive`, `bRitualActive = true`, `TrialProgress = 0.0` |
| Half trial | `AdvanceRitual(TrialDurationSeconds * 0.5)` | `TrialActive`, `TrialProgress` and `GetTrialAlpha()` near `0.5` |
| End trial | `AdvanceRitual(TrialDurationSeconds + 0.1)` | `JudgmentPulse`, `TrialProgress = 1.0`, `bRitualActive = false` |
| Pulse end | `AdvanceRitual(JudgmentPulseSeconds + 0.1)` | `Cooldown`, `GetCooldownAlpha()` at cooldown start |
| Cooldown end | `AdvanceRitual(CooldownSeconds + 0.1)` | `Smolder`, `TrialProgress = 0.0`, `bRitualActive = false` |

Default timing values:

- `TrialDurationSeconds = 8.0`
- `JudgmentPulseSeconds = 1.25`
- `CooldownSeconds = 2.5`

## Verdict Calls

| Call | Expected result |
| --- | --- |
| `AcceptSacrifice(0.72)` | `Accepted`, `TrialProgress = 1.0`, `JudgmentIntensity = 0.72`, `RejectedSeverity = 0.0`, inactive trial |
| `RejectSacrifice(0.66)` | `Rejected`, `TrialProgress = 1.0`, `JudgmentIntensity = 0.66`, `RejectedSeverity = 0.66`, inactive trial |
| `TriggerJudgmentPulse(0.88)` | `JudgmentPulse`, `JudgmentIntensity = 0.88` |
| `SetTrialProgress(0.25)` | `TrialActive`, `TrialProgress` near `0.25` |

## Trace And VFX Locator Getters

The validator confirms the following getters return finite world-space vectors near the altar actor:

- `GetInteractFrontLocation()`
- `GetAltarCoreLocation()`
- `GetSacrificeMarkLocation()`
- `GetBrandTransferLocation()`
- `GetRingLinkLocation()`
- `GetRejectedGapLocation()`

These locations are the approved attachment points for interaction prompts, ritual core VFX, sacrifice-mark VFX, brand-transfer VFX, ring-link VFX, rejection snap VFX, audio one-shots, and gameplay traces.

## Validation Command

```bash
/home/Flamestrike/UnrealEngine/UE_5.8.0/Engine/Binaries/Linux/UnrealEditor-Cmd \
  /home/Flamestrike/Projects/Aerathea/Aerathea.uproject \
  -run=pythonscript \
  -ExecutePythonScript=/home/Flamestrike/Projects/Aerathea/Tools/Unreal/validate_infernal_ritual_altar_timing_traces.py \
  -unattended -nop4 -nosplash
```

Latest result: passed, including trial/cooldown flow, accepted/rejected verdicts, judgment pulse, and 6 locator getters.
