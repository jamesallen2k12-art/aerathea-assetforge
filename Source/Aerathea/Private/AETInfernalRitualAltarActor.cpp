#include "AETInfernalRitualAltarActor.h"

#include "Components/BoxComponent.h"
#include "Components/SceneComponent.h"
#include "Components/StaticMeshComponent.h"
#include "Engine/StaticMesh.h"
#include "Materials/MaterialInterface.h"
#include "NiagaraComponent.h"
#include "NiagaraSystem.h"

AAETInfernalRitualAltarActor::AAETInfernalRitualAltarActor()
{
	PrimaryActorTick.bCanEverTick = false;
	bReplicates = true;

	RitualState = EAETInfernalRitualAltarState::Smolder;
	TrialProgress = 0.0f;
	JudgmentIntensity = 0.22f;
	RejectedSeverity = 0.0f;
	BrandGlowMaterialSlotIndex = 4;
	bUseNiagara = true;
	bShowInteractionVolume = false;
	TrialDurationSeconds = 8.0f;
	JudgmentPulseSeconds = 1.25f;
	CooldownSeconds = 2.5f;
	InteractionRadiusCm = 170.0f;
	InteractionDepthCm = 90.0f;
	bBindingHooksEnabled = true;
	RitualBindingId = TEXT("Ritual_INF_CullingTrial_A01");
	ObjectiveBindingId = TEXT("OBJ_INF_ProveWorth_A01");
	UIStatePrefix = TEXT("UI.INF.RitualAltar");
	AudioEventPrefix = TEXT("Audio.INF.RitualAltar");
	RitualElapsedSeconds = 0.0f;
	CooldownElapsedSeconds = 0.0f;
	bRitualActive = false;
	CurrentUIStateTag = TEXT("UI.INF.RitualAltar.Smolder");
	CurrentAudioEventName = TEXT("Audio.INF.RitualAltar.Smolder");
	bLastVerdictAccepted = false;

	SceneRoot = CreateDefaultSubobject<USceneComponent>(TEXT("SceneRoot"));
	SetRootComponent(SceneRoot);

	AltarMesh = CreateDefaultSubobject<UStaticMeshComponent>(TEXT("AltarMesh"));
	AltarMesh->SetupAttachment(SceneRoot);
	AltarMesh->SetCollisionProfileName(TEXT("BlockAll"));

	InteractionVolume = CreateDefaultSubobject<UBoxComponent>(TEXT("InteractionVolume"));
	InteractionVolume->SetupAttachment(SceneRoot);
	InteractionVolume->SetCollisionProfileName(TEXT("OverlapAllDynamic"));
	InteractionVolume->SetGenerateOverlapEvents(true);
	InteractionVolume->SetVisibleFlag(false);
	InteractionVolume->SetHiddenInGame(true, true);

	InteractFrontLocator = CreateDefaultSubobject<USceneComponent>(TEXT("InteractFrontLocator"));
	InteractFrontLocator->SetupAttachment(SceneRoot);

	AltarCoreLocator = CreateDefaultSubobject<USceneComponent>(TEXT("AltarCoreLocator"));
	AltarCoreLocator->SetupAttachment(SceneRoot);

	SacrificeMarkLocator = CreateDefaultSubobject<USceneComponent>(TEXT("SacrificeMarkLocator"));
	SacrificeMarkLocator->SetupAttachment(SceneRoot);

	BrandTransferLocator = CreateDefaultSubobject<USceneComponent>(TEXT("BrandTransferLocator"));
	BrandTransferLocator->SetupAttachment(SceneRoot);

	RingLinkLocator = CreateDefaultSubobject<USceneComponent>(TEXT("RingLinkLocator"));
	RingLinkLocator->SetupAttachment(SceneRoot);

	RejectedGapLocator = CreateDefaultSubobject<USceneComponent>(TEXT("RejectedGapLocator"));
	RejectedGapLocator->SetupAttachment(SceneRoot);

	WorthinessNiagara = CreateDefaultSubobject<UNiagaraComponent>(TEXT("WorthinessNiagara"));
	WorthinessNiagara->SetupAttachment(SceneRoot);
	WorthinessNiagara->SetAutoActivate(false);
	WorthinessNiagara->SetVisibleFlag(false);
	WorthinessNiagara->SetHiddenInGame(true, true);
}

void AAETInfernalRitualAltarActor::OnConstruction(const FTransform& Transform)
{
	Super::OnConstruction(Transform);

	TrialProgress = FMath::Clamp(TrialProgress, 0.0f, 1.0f);
	JudgmentIntensity = FMath::Clamp(JudgmentIntensity, 0.0f, 1.0f);
	RejectedSeverity = FMath::Clamp(RejectedSeverity, 0.0f, 1.0f);
	BrandGlowMaterialSlotIndex = FMath::Max(BrandGlowMaterialSlotIndex, 0);
	TrialDurationSeconds = FMath::Clamp(TrialDurationSeconds, 0.05f, 60.0f);
	JudgmentPulseSeconds = FMath::Clamp(JudgmentPulseSeconds, 0.05f, 10.0f);
	CooldownSeconds = FMath::Clamp(CooldownSeconds, 0.05f, 30.0f);
	InteractionRadiusCm = FMath::Clamp(InteractionRadiusCm, 0.0f, 1000.0f);
	InteractionDepthCm = FMath::Clamp(InteractionDepthCm, 0.0f, 1000.0f);
	if (RitualBindingId.IsNone())
	{
		RitualBindingId = TEXT("Ritual_INF_CullingTrial_A01");
	}
	if (ObjectiveBindingId.IsNone())
	{
		ObjectiveBindingId = TEXT("OBJ_INF_ProveWorth_A01");
	}
	if (UIStatePrefix.IsNone())
	{
		UIStatePrefix = TEXT("UI.INF.RitualAltar");
	}
	if (AudioEventPrefix.IsNone())
	{
		AudioEventPrefix = TEXT("Audio.INF.RitualAltar");
	}
	RitualElapsedSeconds = FMath::Max(RitualElapsedSeconds, 0.0f);
	CooldownElapsedSeconds = FMath::Max(CooldownElapsedSeconds, 0.0f);
	AssignDefaultAssets();
	UpdateAltarLayout();
	ApplyRitualState();
}

void AAETInfernalRitualAltarActor::SetRitualState(EAETInfernalRitualAltarState NewState)
{
	RitualState = NewState;
	if (RitualState == EAETInfernalRitualAltarState::Inactive)
	{
		bRitualActive = false;
		TrialProgress = 0.0f;
		RitualElapsedSeconds = 0.0f;
		CooldownElapsedSeconds = 0.0f;
	}
	else if (RitualState == EAETInfernalRitualAltarState::TrialActive)
	{
		bRitualActive = true;
	}
	else if (RitualState == EAETInfernalRitualAltarState::Accepted || RitualState == EAETInfernalRitualAltarState::Rejected)
	{
		bRitualActive = false;
		TrialProgress = 1.0f;
	}
	ApplyRitualState();
}

void AAETInfernalRitualAltarActor::SetTrialProgress(float NewTrialProgress)
{
	TrialProgress = FMath::Clamp(NewTrialProgress, 0.0f, 1.0f);
	if (TrialProgress > 0.0f && RitualState == EAETInfernalRitualAltarState::Smolder)
	{
		RitualState = EAETInfernalRitualAltarState::TrialActive;
		bRitualActive = true;
	}
	ApplyRitualState();
}

void AAETInfernalRitualAltarActor::SetJudgmentIntensity(float NewJudgmentIntensity)
{
	JudgmentIntensity = FMath::Clamp(NewJudgmentIntensity, 0.0f, 1.0f);
	ApplyRitualState();
}

void AAETInfernalRitualAltarActor::StartTrial()
{
	RitualState = EAETInfernalRitualAltarState::TrialActive;
	TrialProgress = 0.0f;
	RitualElapsedSeconds = 0.0f;
	CooldownElapsedSeconds = 0.0f;
	bRitualActive = true;
	ApplyRitualState();
}

void AAETInfernalRitualAltarActor::AcceptSacrifice(float AcceptanceIntensity)
{
	RitualState = EAETInfernalRitualAltarState::Accepted;
	TrialProgress = 1.0f;
	JudgmentIntensity = FMath::Clamp(AcceptanceIntensity, 0.0f, 1.0f);
	RejectedSeverity = 0.0f;
	bRitualActive = false;
	ApplyRitualState();
	BroadcastVerdictResolved(true, JudgmentIntensity);
}

void AAETInfernalRitualAltarActor::RejectSacrifice(float RejectionSeverity)
{
	RitualState = EAETInfernalRitualAltarState::Rejected;
	TrialProgress = 1.0f;
	JudgmentIntensity = FMath::Clamp(RejectionSeverity, 0.0f, 1.0f);
	RejectedSeverity = FMath::Clamp(RejectionSeverity, 0.0f, 1.0f);
	bRitualActive = false;
	ApplyRitualState();
	BroadcastVerdictResolved(false, JudgmentIntensity);
}

void AAETInfernalRitualAltarActor::TriggerJudgmentPulse(float PulseIntensity)
{
	RitualState = EAETInfernalRitualAltarState::JudgmentPulse;
	JudgmentIntensity = FMath::Clamp(PulseIntensity, 0.0f, 1.0f);
	RitualElapsedSeconds = 0.0f;
	bRitualActive = false;
	ApplyRitualState();
}

void AAETInfernalRitualAltarActor::AdvanceRitual(float DeltaSeconds)
{
	const float ClampedDeltaSeconds = FMath::Max(DeltaSeconds, 0.0f);
	if (RitualState == EAETInfernalRitualAltarState::TrialActive)
	{
		RitualElapsedSeconds = FMath::Min(RitualElapsedSeconds + ClampedDeltaSeconds, TrialDurationSeconds);
		TrialProgress = GetTrialAlpha();
		if (TrialProgress >= 1.0f)
		{
			TriggerJudgmentPulse(1.0f);
			return;
		}
	}
	else if (RitualState == EAETInfernalRitualAltarState::JudgmentPulse)
	{
		RitualElapsedSeconds = FMath::Min(RitualElapsedSeconds + ClampedDeltaSeconds, JudgmentPulseSeconds);
		if (RitualElapsedSeconds >= JudgmentPulseSeconds)
		{
			RitualState = EAETInfernalRitualAltarState::Cooldown;
			RitualElapsedSeconds = 0.0f;
			CooldownElapsedSeconds = 0.0f;
		}
	}
	else if (RitualState == EAETInfernalRitualAltarState::Cooldown)
	{
		CooldownElapsedSeconds = FMath::Min(CooldownElapsedSeconds + ClampedDeltaSeconds, CooldownSeconds);
		if (CooldownElapsedSeconds >= CooldownSeconds)
		{
			ResetRitual();
			return;
		}
	}
	ApplyRitualState();
}

float AAETInfernalRitualAltarActor::GetTrialAlpha() const
{
	return TrialDurationSeconds > KINDA_SMALL_NUMBER ? FMath::Clamp(RitualElapsedSeconds / TrialDurationSeconds, 0.0f, 1.0f) : TrialProgress;
}

float AAETInfernalRitualAltarActor::GetCooldownAlpha() const
{
	return CooldownSeconds > KINDA_SMALL_NUMBER ? FMath::Clamp(CooldownElapsedSeconds / CooldownSeconds, 0.0f, 1.0f) : 0.0f;
}

FVector AAETInfernalRitualAltarActor::GetInteractFrontLocation() const
{
	return InteractFrontLocator != nullptr ? InteractFrontLocator->GetComponentLocation() : GetActorLocation();
}

FVector AAETInfernalRitualAltarActor::GetAltarCoreLocation() const
{
	return AltarCoreLocator != nullptr ? AltarCoreLocator->GetComponentLocation() : GetActorLocation();
}

FVector AAETInfernalRitualAltarActor::GetSacrificeMarkLocation() const
{
	return SacrificeMarkLocator != nullptr ? SacrificeMarkLocator->GetComponentLocation() : GetActorLocation();
}

FVector AAETInfernalRitualAltarActor::GetBrandTransferLocation() const
{
	return BrandTransferLocator != nullptr ? BrandTransferLocator->GetComponentLocation() : GetActorLocation();
}

FVector AAETInfernalRitualAltarActor::GetRingLinkLocation() const
{
	return RingLinkLocator != nullptr ? RingLinkLocator->GetComponentLocation() : GetActorLocation();
}

FVector AAETInfernalRitualAltarActor::GetRejectedGapLocation() const
{
	return RejectedGapLocator != nullptr ? RejectedGapLocator->GetComponentLocation() : GetActorLocation();
}

FName AAETInfernalRitualAltarActor::GetCurrentUIStateTag() const
{
	return CurrentUIStateTag;
}

FName AAETInfernalRitualAltarActor::GetCurrentAudioEventName() const
{
	return CurrentAudioEventName;
}

FName AAETInfernalRitualAltarActor::GetRitualBindingId() const
{
	return RitualBindingId;
}

FName AAETInfernalRitualAltarActor::GetObjectiveBindingId() const
{
	return ObjectiveBindingId;
}

void AAETInfernalRitualAltarActor::ResetRitual()
{
	RitualState = EAETInfernalRitualAltarState::Smolder;
	TrialProgress = 0.0f;
	JudgmentIntensity = 0.22f;
	RejectedSeverity = 0.0f;
	RitualElapsedSeconds = 0.0f;
	CooldownElapsedSeconds = 0.0f;
	bRitualActive = false;
	ApplyRitualState();
}

void AAETInfernalRitualAltarActor::AssignDefaultAssets()
{
	if (AltarStaticMesh == nullptr)
	{
		AltarStaticMesh = LoadObject<UStaticMesh>(
			nullptr,
			TEXT("/Game/Aerathea/Props/Infernals/BalgorothCult/SM_INF_WorthinessAltar_A01.SM_INF_WorthinessAltar_A01")
		);
	}
	if (BrandGlowInactiveMaterial == nullptr)
	{
		BrandGlowInactiveMaterial = LoadObject<UMaterialInterface>(
			nullptr,
			TEXT("/Game/Aerathea/Materials/Instances/MI_INF_BrandGlowStates_A01_Inactive.MI_INF_BrandGlowStates_A01_Inactive")
		);
	}
	if (BrandGlowSmolderMaterial == nullptr)
	{
		BrandGlowSmolderMaterial = LoadObject<UMaterialInterface>(
			nullptr,
			TEXT("/Game/Aerathea/Materials/Instances/MI_INF_BrandGlowStates_A01_Smolder.MI_INF_BrandGlowStates_A01_Smolder")
		);
	}
	if (BrandGlowTrialActiveMaterial == nullptr)
	{
		BrandGlowTrialActiveMaterial = LoadObject<UMaterialInterface>(
			nullptr,
			TEXT("/Game/Aerathea/Materials/Instances/MI_INF_BrandGlowStates_A01_TrialActive.MI_INF_BrandGlowStates_A01_TrialActive")
		);
	}
	if (BrandGlowAcceptedMaterial == nullptr)
	{
		BrandGlowAcceptedMaterial = LoadObject<UMaterialInterface>(
			nullptr,
			TEXT("/Game/Aerathea/Materials/Instances/MI_INF_BrandGlowStates_A01_Accepted.MI_INF_BrandGlowStates_A01_Accepted")
		);
	}
	if (BrandGlowRejectedMaterial == nullptr)
	{
		BrandGlowRejectedMaterial = LoadObject<UMaterialInterface>(
			nullptr,
			TEXT("/Game/Aerathea/Materials/Instances/MI_INF_BrandGlowStates_A01_Rejected.MI_INF_BrandGlowStates_A01_Rejected")
		);
	}
	if (BrandGlowJudgmentPulseMaterial == nullptr)
	{
		BrandGlowJudgmentPulseMaterial = LoadObject<UMaterialInterface>(
			nullptr,
			TEXT("/Game/Aerathea/Materials/Instances/MI_INF_BrandGlowStates_A01_SorcererFocus.MI_INF_BrandGlowStates_A01_SorcererFocus")
		);
	}
	if (InactiveNiagaraSystem == nullptr)
	{
		InactiveNiagaraSystem = LoadObject<UNiagaraSystem>(
			nullptr,
			TEXT("/Game/Aerathea/VFX/Infernals/WorthinessJudgment/NS_INF_Worthiness_Inactive_A01.NS_INF_Worthiness_Inactive_A01")
		);
	}
	if (SmolderNiagaraSystem == nullptr)
	{
		SmolderNiagaraSystem = LoadObject<UNiagaraSystem>(
			nullptr,
			TEXT("/Game/Aerathea/VFX/Infernals/WorthinessJudgment/NS_INF_Worthiness_Smolder_A01.NS_INF_Worthiness_Smolder_A01")
		);
	}
	if (TrialActiveNiagaraSystem == nullptr)
	{
		TrialActiveNiagaraSystem = LoadObject<UNiagaraSystem>(
			nullptr,
			TEXT("/Game/Aerathea/VFX/Infernals/WorthinessJudgment/NS_INF_Worthiness_TrialActive_A01.NS_INF_Worthiness_TrialActive_A01")
		);
	}
	if (AcceptedNiagaraSystem == nullptr)
	{
		AcceptedNiagaraSystem = LoadObject<UNiagaraSystem>(
			nullptr,
			TEXT("/Game/Aerathea/VFX/Infernals/WorthinessJudgment/NS_INF_Worthiness_Accepted_A01.NS_INF_Worthiness_Accepted_A01")
		);
	}
	if (RejectedNiagaraSystem == nullptr)
	{
		RejectedNiagaraSystem = LoadObject<UNiagaraSystem>(
			nullptr,
			TEXT("/Game/Aerathea/VFX/Infernals/WorthinessJudgment/NS_INF_Worthiness_Rejected_A01.NS_INF_Worthiness_Rejected_A01")
		);
	}
	if (JudgmentPulseNiagaraSystem == nullptr)
	{
		JudgmentPulseNiagaraSystem = LoadObject<UNiagaraSystem>(
			nullptr,
			TEXT("/Game/Aerathea/VFX/Infernals/WorthinessJudgment/NS_INF_Worthiness_JudgmentPulse_A01.NS_INF_Worthiness_JudgmentPulse_A01")
		);
	}
	if (AltarMesh != nullptr && AltarMesh->GetStaticMesh() == nullptr && AltarStaticMesh != nullptr)
	{
		AltarMesh->SetStaticMesh(AltarStaticMesh);
	}
}

void AAETInfernalRitualAltarActor::UpdateAltarLayout()
{
	if (InteractFrontLocator != nullptr)
	{
		InteractFrontLocator->SetRelativeLocation(FVector(0.0f, 132.0f, 102.0f));
	}
	if (AltarCoreLocator != nullptr)
	{
		AltarCoreLocator->SetRelativeLocation(FVector(0.0f, -6.0f, 132.0f));
	}
	if (SacrificeMarkLocator != nullptr)
	{
		SacrificeMarkLocator->SetRelativeLocation(FVector(0.0f, 74.0f, 108.0f));
	}
	if (BrandTransferLocator != nullptr)
	{
		BrandTransferLocator->SetRelativeLocation(FVector(0.0f, -146.0f, 266.0f));
	}
	if (RingLinkLocator != nullptr)
	{
		RingLinkLocator->SetRelativeLocation(FVector(0.0f, 82.0f, 106.0f));
	}
	if (RejectedGapLocator != nullptr)
	{
		RejectedGapLocator->SetRelativeLocation(FVector(88.0f, 72.0f, 111.0f));
		RejectedGapLocator->SetRelativeRotation(FRotator(0.0f, 0.0f, -32.0f));
	}
	if (InteractionVolume != nullptr)
	{
		InteractionVolume->SetRelativeLocation(FVector(0.0f, 132.0f, 102.0f));
		InteractionVolume->SetBoxExtent(FVector(InteractionRadiusCm, InteractionDepthCm, 95.0f));
		InteractionVolume->SetVisibility(bShowInteractionVolume, true);
		InteractionVolume->SetHiddenInGame(!bShowInteractionVolume, true);
	}
	if (WorthinessNiagara != nullptr)
	{
		WorthinessNiagara->SetRelativeLocation(FVector(0.0f, -6.0f, 132.0f));
		WorthinessNiagara->SetRelativeScale3D(FVector(1.0f, 1.0f, 1.0f));
	}
}

float AAETInfernalRitualAltarActor::CurrentStateValue() const
{
	return static_cast<float>(static_cast<uint8>(RitualState));
}

FLinearColor AAETInfernalRitualAltarActor::CurrentStateColor() const
{
	switch (RitualState)
	{
	case EAETInfernalRitualAltarState::Inactive:
		return FLinearColor(0.06f, 0.025f, 0.015f, 1.0f);
	case EAETInfernalRitualAltarState::TrialActive:
		return FLinearColor(1.0f, 0.28f, 0.035f, 1.0f);
	case EAETInfernalRitualAltarState::Accepted:
		return FLinearColor(1.0f, 0.62f, 0.22f, 1.0f);
	case EAETInfernalRitualAltarState::Rejected:
		return FLinearColor(0.95f, 0.02f, 0.12f, 1.0f);
	case EAETInfernalRitualAltarState::JudgmentPulse:
		return FLinearColor(1.0f, 0.16f, 0.02f, 1.0f);
	case EAETInfernalRitualAltarState::Cooldown:
		return FLinearColor(0.28f, 0.055f, 0.025f, 1.0f);
	case EAETInfernalRitualAltarState::Smolder:
	default:
		return FLinearColor(0.74f, 0.12f, 0.025f, 1.0f);
	}
}

UMaterialInterface* AAETInfernalRitualAltarActor::MaterialForState() const
{
	switch (RitualState)
	{
	case EAETInfernalRitualAltarState::Inactive:
		return BrandGlowInactiveMaterial;
	case EAETInfernalRitualAltarState::TrialActive:
		return BrandGlowTrialActiveMaterial;
	case EAETInfernalRitualAltarState::Accepted:
		return BrandGlowAcceptedMaterial;
	case EAETInfernalRitualAltarState::Rejected:
		return BrandGlowRejectedMaterial;
	case EAETInfernalRitualAltarState::JudgmentPulse:
		return BrandGlowJudgmentPulseMaterial != nullptr ? BrandGlowJudgmentPulseMaterial : BrandGlowTrialActiveMaterial;
	case EAETInfernalRitualAltarState::Cooldown:
		return BrandGlowSmolderMaterial;
	case EAETInfernalRitualAltarState::Smolder:
	default:
		return BrandGlowSmolderMaterial;
	}
}

UNiagaraSystem* AAETInfernalRitualAltarActor::NiagaraSystemForState() const
{
	switch (RitualState)
	{
	case EAETInfernalRitualAltarState::Inactive:
		return InactiveNiagaraSystem;
	case EAETInfernalRitualAltarState::TrialActive:
		return TrialActiveNiagaraSystem;
	case EAETInfernalRitualAltarState::Accepted:
		return AcceptedNiagaraSystem;
	case EAETInfernalRitualAltarState::Rejected:
		return RejectedNiagaraSystem;
	case EAETInfernalRitualAltarState::JudgmentPulse:
		return JudgmentPulseNiagaraSystem;
	case EAETInfernalRitualAltarState::Cooldown:
		return SmolderNiagaraSystem;
	case EAETInfernalRitualAltarState::Smolder:
	default:
		return SmolderNiagaraSystem;
	}
}

FName AAETInfernalRitualAltarActor::StateSuffixName() const
{
	switch (RitualState)
	{
	case EAETInfernalRitualAltarState::Inactive:
		return TEXT("Inactive");
	case EAETInfernalRitualAltarState::TrialActive:
		return TEXT("TrialActive");
	case EAETInfernalRitualAltarState::Accepted:
		return TEXT("Accepted");
	case EAETInfernalRitualAltarState::Rejected:
		return TEXT("Rejected");
	case EAETInfernalRitualAltarState::JudgmentPulse:
		return TEXT("JudgmentPulse");
	case EAETInfernalRitualAltarState::Cooldown:
		return TEXT("Cooldown");
	case EAETInfernalRitualAltarState::Smolder:
	default:
		return TEXT("Smolder");
	}
}

FName AAETInfernalRitualAltarActor::BuildBindingTag(FName Prefix) const
{
	const FString PrefixString = Prefix.IsNone() ? FString(TEXT("INF.RitualAltar")) : Prefix.ToString();
	const FString SuffixString = StateSuffixName().ToString();
	return FName(*FString::Printf(TEXT("%s.%s"), *PrefixString, *SuffixString));
}

void AAETInfernalRitualAltarActor::UpdateBindingState()
{
	CurrentUIStateTag = BuildBindingTag(UIStatePrefix);
	CurrentAudioEventName = BuildBindingTag(AudioEventPrefix);
}

void AAETInfernalRitualAltarActor::BroadcastBindingStateChanged()
{
	if (!bBindingHooksEnabled)
	{
		return;
	}
	OnRitualBindingStateChanged.Broadcast(RitualState, CurrentUIStateTag, CurrentAudioEventName, TrialProgress, JudgmentIntensity);
}

void AAETInfernalRitualAltarActor::BroadcastVerdictResolved(bool bAccepted, float VerdictIntensity)
{
	bLastVerdictAccepted = bAccepted;
	if (!bBindingHooksEnabled)
	{
		return;
	}
	OnRitualVerdictResolved.Broadcast(bAccepted, ObjectiveBindingId, FMath::Clamp(VerdictIntensity, 0.0f, 1.0f), RejectedSeverity);
}

void AAETInfernalRitualAltarActor::ApplyRitualState()
{
	const float StateValue = CurrentStateValue();
	const FLinearColor StateColor = CurrentStateColor();
	UpdateBindingState();

	if (AltarMesh != nullptr)
	{
		if (AltarMesh->GetStaticMesh() == nullptr && AltarStaticMesh != nullptr)
		{
			AltarMesh->SetStaticMesh(AltarStaticMesh);
		}
		if (UMaterialInterface* StateMaterial = MaterialForState())
		{
			AltarMesh->SetMaterial(BrandGlowMaterialSlotIndex, StateMaterial);
		}
		AltarMesh->SetVisibility(true, true);
		AltarMesh->SetHiddenInGame(false, true);
		AltarMesh->SetCollisionEnabled(ECollisionEnabled::QueryAndPhysics);
		AltarMesh->SetScalarParameterValueOnMaterials(TEXT("RitualState"), StateValue);
		AltarMesh->SetScalarParameterValueOnMaterials(TEXT("TrialProgress"), TrialProgress);
		AltarMesh->SetScalarParameterValueOnMaterials(TEXT("JudgmentIntensity"), JudgmentIntensity);
		AltarMesh->SetScalarParameterValueOnMaterials(TEXT("RejectedSeverity"), RejectedSeverity);
		AltarMesh->SetScalarParameterValueOnMaterials(TEXT("CooldownAlpha"), GetCooldownAlpha());
		AltarMesh->SetVectorParameterValueOnMaterials(TEXT("RitualStateColor"), FVector(StateColor.R, StateColor.G, StateColor.B));
	}

	if (WorthinessNiagara != nullptr)
	{
		UNiagaraSystem* ActiveSystem = NiagaraSystemForState();
		if (ActiveSystem != nullptr && WorthinessNiagara->GetAsset() != ActiveSystem)
		{
			WorthinessNiagara->SetAsset(ActiveSystem);
		}

		const bool bRunNiagara = bUseNiagara && ActiveSystem != nullptr && RitualState != EAETInfernalRitualAltarState::Inactive;
		WorthinessNiagara->SetVisibility(bRunNiagara, true);
		WorthinessNiagara->SetHiddenInGame(!bRunNiagara, true);
		if (bRunNiagara && !WorthinessNiagara->IsActive())
		{
			WorthinessNiagara->Activate(true);
		}
		else if (!bRunNiagara && WorthinessNiagara->IsActive())
		{
			WorthinessNiagara->Deactivate();
		}

		WorthinessNiagara->SetVariableFloat(TEXT("User.RitualState"), StateValue);
		WorthinessNiagara->SetVariableFloat(TEXT("User.TrialProgress"), TrialProgress);
		WorthinessNiagara->SetVariableFloat(TEXT("User.JudgmentIntensity"), JudgmentIntensity);
		WorthinessNiagara->SetVariableFloat(TEXT("User.RejectedSeverity"), RejectedSeverity);
		WorthinessNiagara->SetVariableFloat(TEXT("User.CooldownAlpha"), GetCooldownAlpha());
		WorthinessNiagara->SetVariableBool(TEXT("User.bTrialActive"), RitualState == EAETInfernalRitualAltarState::TrialActive);
		WorthinessNiagara->SetVariableBool(TEXT("User.bAccepted"), RitualState == EAETInfernalRitualAltarState::Accepted);
		WorthinessNiagara->SetVariableBool(TEXT("User.bRejected"), RitualState == EAETInfernalRitualAltarState::Rejected);
		WorthinessNiagara->SetVariableLinearColor(TEXT("User.RitualStateColor"), StateColor);
		if (AltarCoreLocator != nullptr)
		{
			WorthinessNiagara->SetVariableVec3(TEXT("User.AltarCoreWorldLocation"), AltarCoreLocator->GetComponentLocation());
		}
		if (SacrificeMarkLocator != nullptr)
		{
			WorthinessNiagara->SetVariableVec3(TEXT("User.SacrificeMarkWorldLocation"), SacrificeMarkLocator->GetComponentLocation());
		}
		if (BrandTransferLocator != nullptr)
		{
			WorthinessNiagara->SetVariableVec3(TEXT("User.BrandTransferWorldLocation"), BrandTransferLocator->GetComponentLocation());
		}
		if (RingLinkLocator != nullptr)
		{
			WorthinessNiagara->SetVariableVec3(TEXT("User.RingLinkWorldLocation"), RingLinkLocator->GetComponentLocation());
		}
		if (RejectedGapLocator != nullptr)
		{
			WorthinessNiagara->SetVariableVec3(TEXT("User.RejectedGapWorldLocation"), RejectedGapLocator->GetComponentLocation());
		}
	}
	BroadcastBindingStateChanged();
}
