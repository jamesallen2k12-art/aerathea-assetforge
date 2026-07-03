# VFX_INF_WorthinessJudgment_A01 Build Import Status

## Current State

First-pass Unreal VFX/material authoring is complete for the Infernal worthiness judgment ritual package. This pass creates loadable material parents, material instances, and template-derived Niagara systems/emitters so the culling trial floor, implemented altar Blueprint, validated altar timing/trace calls, and BrandGlow state handoff can bind against stable asset names.

This is not final VFX art. The Niagara assets are template-derived review targets and still need bespoke graph design, tuned fixed bounds, final gameplay `User.*` parameter polish, final texture inputs, and particle-density/bloom polish. A focused polish-readiness validator now locks the current restrained material scalar envelope so future graph work cannot drift into overbright or noisy states unnoticed.

`NIAGARA_ART_PASS_HANDOFF.md` now defines the manual graph-authoring recipe, native `User.*` parameter map, fixed-bounds requirements, LOD rules, and visual approval checklist for the next Unreal/Niagara pass. This is handoff readiness only; `GraphStatus` remains `template_derived_contract_ready` and `FinalGraphAuthored` remains `false`.

## Unreal Assets

- VFX folder: `/Game/Aerathea/VFX/Infernals/WorthinessJudgment/`
- Material parent folder: `/Game/Aerathea/Materials/Infernals/VFX/`
- Material instance folder: `/Game/Aerathea/Materials/Instances/`
- Primary socket source: `/Game/Aerathea/Props/Infernals/BalgorothCult/SM_INF_CullingTrialFloor_A01`
- Shared material-state dependency: `/Game/Aerathea/Materials/Instances/MI_INF_BrandGlowStates_A01_*`

## Material Parents And Instances

- `M_INF_WorthinessRing_A01` -> `MI_INF_WorthinessRing_A01`
- `M_INF_WorthinessSigil_A01` -> `MI_INF_WorthinessSigil_A01`
- `M_INF_WorthinessAsh_A01` -> `MI_INF_WorthinessAsh_A01`
- `M_INF_WorthinessRejected_A01` -> `MI_INF_WorthinessRejected_A01`
- `M_INF_WorthinessJudgmentPulse_A01` -> `MI_INF_WorthinessJudgmentPulse_A01`

## Niagara Systems

- `NS_INF_Worthiness_Inactive_A01`
- `NS_INF_Worthiness_Smolder_A01`
- `NS_INF_Worthiness_TrialActive_A01`
- `NS_INF_Worthiness_Accepted_A01`
- `NS_INF_Worthiness_Rejected_A01`
- `NS_INF_Worthiness_JudgmentPulse_A01`

## Niagara Emitters

- `NE_INF_WorthinessRingPulse_A01`
- `NE_INF_WorthinessSigilPulse_A01`
- `NE_INF_WorthinessAshMote_A01`
- `NE_INF_WorthinessRejectedSnap_A01`

## Automation

- Unreal authoring: `Tools/Unreal/import_infernal_worthiness_judgment_vfx.py`
- Focused validator: `Tools/Unreal/validate_infernal_worthiness_judgment_vfx.py`
- Polish contract validator: `Tools/Unreal/validate_infernal_worthiness_judgment_vfx_polish_contract.py`
- Blueprint timing/trace validator: `Tools/Unreal/validate_infernal_ritual_altar_timing_traces.py`
- Startup validator contract: `Tools/Unreal/validate_startup_scene.py`
- Manual Niagara art-pass handoff: `docs/assets/vfx/VFX_INF_WorthinessJudgment_A01/NIAGARA_ART_PASS_HANDOFF.md`

## Validation Results

Passed:

- `python -m py_compile Tools/Unreal/import_infernal_worthiness_judgment_vfx.py Tools/Unreal/validate_infernal_worthiness_judgment_vfx.py Tools/Unreal/validate_startup_scene.py`
- `UnrealEditor-Cmd ... -ExecutePythonScript=Tools/Unreal/import_infernal_worthiness_judgment_vfx.py`
- `UnrealEditor-Cmd ... -ExecutePythonScript=Tools/Unreal/validate_infernal_worthiness_judgment_vfx.py`
- `UnrealEditor-Cmd ... -ExecutePythonScript=Tools/Unreal/validate_infernal_worthiness_judgment_vfx_polish_contract.py`
- `UnrealEditor-Cmd ... -ExecutePythonScript=Tools/Unreal/validate_infernal_ritual_altar_timing_traces.py`
- `UnrealEditor-Cmd ... -ExecutePythonScript=Tools/Unreal/validate_startup_scene.py`

Focused validator result: `6` systems, `4` emitters, `5` material instances, `4` floor sockets, and `6` BrandGlow dependency instances passed.

Polish contract result: `5` material instances, `6` Niagara systems, `4` Niagara emitters, and restrained scalar ranges passed.

Niagara art-pass handoff result: required systems, emitters, native `User.*` parameters, fixed-bounds language, visual approval gate, and `FinalGraphAuthored=false` guard are validator-backed.

Blueprint timing/trace result: trial/cooldown flow, accepted/rejected verdicts, judgment pulse, and `6` locator getters passed.

Latest startup validator result: `233` expected assets, `55` expected actor labels, and `25` ground tiles passed.

## Non-Blocking Warnings

- Unreal platform validation still reports missing non-Linux SDKs; Linux and LinuxArm64 remain valid.
- Unreal emits normal editor startup and content-validation noise during headless command execution.

## Remaining Work

- Replace template-derived Niagara behavior with final hand-authored graph logic.
- Execute the manual Niagara art-pass handoff in Unreal without changing approved asset names or Blueprint assignments.
- Polish final Blueprint/Gameplay Ability graph use of the validated `User.*` parameters for state, radius, pulse intensity, rejection gap, accepted focus, and ash density.
- Tune fixed bounds and VFX LOD density for floor-only and altar Blueprint variants.
- Author final emissive/alpha texture sources for ring, sigil, ash, rejected snap, and judgment pulse material inputs.
- Polish the systems already assigned to `BP_INF_RitualAltar_A01` and future culling floor state previews.
