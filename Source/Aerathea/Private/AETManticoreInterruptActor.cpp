#include "AETManticoreInterruptActor.h"

#include "Components/SceneComponent.h"
#include "Components/SkeletalMeshComponent.h"
#include "Engine/SkeletalMesh.h"
#include "NiagaraComponent.h"
#include "NiagaraSystem.h"

AAETManticoreInterruptActor::AAETManticoreInterruptActor()
{
	PrimaryActorTick.bCanEverTick = false;
	bReplicates = true;

	InterruptState = EAETManticoreInterruptState::Hidden;
	SequenceProgress = 0.0f;
	bVisibleDuringSetup = true;
	EntryOffset = FVector(-220.0f, 160.0f, 0.0f);
	ImpactOffset = FVector(0.0f, 0.0f, 0.0f);
	RetreatOffset = FVector(260.0f, -130.0f, 0.0f);
	bUseNiagara = true;
	StalkSeconds = 1.2f;
	TelegraphSeconds = 0.8f;
	ImpactSeconds = 0.35f;
	ThreatHoldSeconds = 1.1f;
	RetreatSeconds = 1.0f;
	InterruptTraceRadiusCm = 260.0f;
	ImpactDamageRadiusCm = 320.0f;
	InterruptElapsedSeconds = 0.0f;
	bInterruptSequenceActive = false;

	SceneRoot = CreateDefaultSubobject<USceneComponent>(TEXT("SceneRoot"));
	SetRootComponent(SceneRoot);

	ManticoreMesh = CreateDefaultSubobject<USkeletalMeshComponent>(TEXT("ManticoreMesh"));
	ManticoreMesh->SetupAttachment(SceneRoot);
	ManticoreMesh->SetCollisionProfileName(TEXT("Pawn"));

	EntryMarker = CreateDefaultSubobject<USceneComponent>(TEXT("EntryMarker"));
	EntryMarker->SetupAttachment(SceneRoot);

	ImpactMarker = CreateDefaultSubobject<USceneComponent>(TEXT("ImpactMarker"));
	ImpactMarker->SetupAttachment(SceneRoot);

	RetreatMarker = CreateDefaultSubobject<USceneComponent>(TEXT("RetreatMarker"));
	RetreatMarker->SetupAttachment(SceneRoot);

	ImpactNiagara = CreateDefaultSubobject<UNiagaraComponent>(TEXT("ImpactNiagara"));
	ImpactNiagara->SetupAttachment(SceneRoot);
	ImpactNiagara->SetAutoActivate(false);
	ImpactNiagara->SetVisibleFlag(false);
	ImpactNiagara->SetHiddenInGame(true, true);
}

void AAETManticoreInterruptActor::OnConstruction(const FTransform& Transform)
{
	Super::OnConstruction(Transform);

	SequenceProgress = FMath::Clamp(SequenceProgress, 0.0f, 1.0f);
	StalkSeconds = FMath::Clamp(StalkSeconds, 0.05f, 20.0f);
	TelegraphSeconds = FMath::Clamp(TelegraphSeconds, 0.05f, 20.0f);
	ImpactSeconds = FMath::Clamp(ImpactSeconds, 0.05f, 20.0f);
	ThreatHoldSeconds = FMath::Clamp(ThreatHoldSeconds, 0.05f, 20.0f);
	RetreatSeconds = FMath::Clamp(RetreatSeconds, 0.05f, 20.0f);
	InterruptTraceRadiusCm = FMath::Clamp(InterruptTraceRadiusCm, 0.0f, 1200.0f);
	ImpactDamageRadiusCm = FMath::Clamp(ImpactDamageRadiusCm, 0.0f, 1200.0f);
	AssignDefaultAssets();
	UpdateInterruptLayout();
	ApplyInterruptState();
}

void AAETManticoreInterruptActor::SetInterruptState(EAETManticoreInterruptState NewState)
{
	InterruptState = NewState;
	if (InterruptState == EAETManticoreInterruptState::Hidden || InterruptState == EAETManticoreInterruptState::Retreat)
	{
		bInterruptSequenceActive = false;
	}
	ApplyInterruptState();
}

void AAETManticoreInterruptActor::SetSequenceProgress(float NewSequenceProgress)
{
	SequenceProgress = FMath::Clamp(NewSequenceProgress, 0.0f, 1.0f);
	UpdateInterruptLayout();
	ApplyInterruptState();
}

void AAETManticoreInterruptActor::BeginInterruptSequence()
{
	InterruptElapsedSeconds = 0.0f;
	SequenceProgress = 0.0f;
	bInterruptSequenceActive = true;
	InterruptState = EAETManticoreInterruptState::Stalking;
	UpdateInterruptLayout();
	ApplyInterruptState();
}

void AAETManticoreInterruptActor::AdvanceInterruptSequence(float DeltaSeconds)
{
	if (!bInterruptSequenceActive)
	{
		return;
	}

	const float TotalSeconds = StalkSeconds + TelegraphSeconds + ImpactSeconds + ThreatHoldSeconds + RetreatSeconds;
	InterruptElapsedSeconds = FMath::Clamp(InterruptElapsedSeconds + FMath::Max(DeltaSeconds, 0.0f), 0.0f, TotalSeconds);
	SequenceProgress = TotalSeconds > KINDA_SMALL_NUMBER ? FMath::Clamp(InterruptElapsedSeconds / TotalSeconds, 0.0f, 1.0f) : 1.0f;

	const float TelegraphStart = StalkSeconds;
	const float ImpactStart = TelegraphStart + TelegraphSeconds;
	const float HoldStart = ImpactStart + ImpactSeconds;
	const float RetreatStart = HoldStart + ThreatHoldSeconds;
	if (InterruptElapsedSeconds < TelegraphStart)
	{
		InterruptState = EAETManticoreInterruptState::Stalking;
	}
	else if (InterruptElapsedSeconds < ImpactStart)
	{
		InterruptState = EAETManticoreInterruptState::Telegraph;
	}
	else if (InterruptElapsedSeconds < HoldStart)
	{
		InterruptState = EAETManticoreInterruptState::LeapImpact;
	}
	else if (InterruptElapsedSeconds < RetreatStart)
	{
		InterruptState = EAETManticoreInterruptState::ThreatHold;
	}
	else
	{
		InterruptState = EAETManticoreInterruptState::Retreat;
		if (InterruptElapsedSeconds >= TotalSeconds)
		{
			bInterruptSequenceActive = false;
		}
	}

	UpdateInterruptLayout();
	ApplyInterruptState();
}

void AAETManticoreInterruptActor::TriggerInterrupt()
{
	InterruptState = EAETManticoreInterruptState::LeapImpact;
	SequenceProgress = 0.75f;
	InterruptElapsedSeconds = StalkSeconds + TelegraphSeconds;
	bInterruptSequenceActive = true;
	UpdateInterruptLayout();
	ApplyInterruptState();
}

bool AAETManticoreInterruptActor::IsInterruptSequenceActive() const
{
	return bInterruptSequenceActive;
}

bool AAETManticoreInterruptActor::IsImpactWindowActive() const
{
	return InterruptState == EAETManticoreInterruptState::LeapImpact || InterruptState == EAETManticoreInterruptState::ThreatHold;
}

float AAETManticoreInterruptActor::GetInterruptWindowAlpha() const
{
	const float TotalSeconds = StalkSeconds + TelegraphSeconds + ImpactSeconds + ThreatHoldSeconds + RetreatSeconds;
	return TotalSeconds > KINDA_SMALL_NUMBER ? FMath::Clamp(InterruptElapsedSeconds / TotalSeconds, 0.0f, 1.0f) : SequenceProgress;
}

FVector AAETManticoreInterruptActor::GetEntryTraceLocation() const
{
	return EntryMarker != nullptr ? EntryMarker->GetComponentLocation() : GetActorLocation() + EntryOffset;
}

FVector AAETManticoreInterruptActor::GetImpactTraceLocation() const
{
	return ImpactMarker != nullptr ? ImpactMarker->GetComponentLocation() : GetActorLocation() + ImpactOffset;
}

FVector AAETManticoreInterruptActor::GetRetreatTraceLocation() const
{
	return RetreatMarker != nullptr ? RetreatMarker->GetComponentLocation() : GetActorLocation() + RetreatOffset;
}

void AAETManticoreInterruptActor::ResetInterrupt()
{
	InterruptState = EAETManticoreInterruptState::Hidden;
	SequenceProgress = 0.0f;
	InterruptElapsedSeconds = 0.0f;
	bInterruptSequenceActive = false;
	UpdateInterruptLayout();
	ApplyInterruptState();
}

void AAETManticoreInterruptActor::ConfigureInterruptOffsets(FVector NewEntryOffset, FVector NewImpactOffset, FVector NewRetreatOffset)
{
	EntryOffset = NewEntryOffset;
	ImpactOffset = NewImpactOffset;
	RetreatOffset = NewRetreatOffset;
	UpdateInterruptLayout();
}

void AAETManticoreInterruptActor::AssignDefaultAssets()
{
	if (ManticoreSkeletalMesh == nullptr)
	{
		ManticoreSkeletalMesh = LoadObject<USkeletalMesh>(
			nullptr,
			TEXT("/Game/Aerathea/Creatures/Manticores/SK_CRE_Manticore_Interrupt_A01.SK_CRE_Manticore_Interrupt_A01")
		);
	}
	if (ImpactNiagaraSystem == nullptr)
	{
		ImpactNiagaraSystem = LoadObject<UNiagaraSystem>(
			nullptr,
			TEXT("/Game/Aerathea/VFX/Creatures/NS_CRE_Manticore_Impact_A01.NS_CRE_Manticore_Impact_A01")
		);
	}
	if (ManticoreMesh != nullptr && ManticoreMesh->GetSkeletalMeshAsset() == nullptr && ManticoreSkeletalMesh != nullptr)
	{
		ManticoreMesh->SetSkeletalMeshAsset(ManticoreSkeletalMesh);
	}
}

void AAETManticoreInterruptActor::UpdateInterruptLayout()
{
	if (EntryMarker != nullptr)
	{
		EntryMarker->SetRelativeLocation(EntryOffset);
	}
	if (ImpactMarker != nullptr)
	{
		ImpactMarker->SetRelativeLocation(ImpactOffset);
	}
	if (RetreatMarker != nullptr)
	{
		RetreatMarker->SetRelativeLocation(RetreatOffset);
	}

	FVector MeshLocation = EntryOffset;
	if (InterruptState == EAETManticoreInterruptState::Stalking)
	{
		MeshLocation = FMath::Lerp(EntryOffset, ImpactOffset, FMath::Clamp(SequenceProgress, 0.0f, 0.45f) / 0.45f);
	}
	else if (InterruptState == EAETManticoreInterruptState::Telegraph)
	{
		MeshLocation = FMath::Lerp(EntryOffset, ImpactOffset, 0.65f);
	}
	else if (InterruptState == EAETManticoreInterruptState::LeapImpact || InterruptState == EAETManticoreInterruptState::ThreatHold)
	{
		MeshLocation = ImpactOffset;
	}
	else if (InterruptState == EAETManticoreInterruptState::Retreat)
	{
		MeshLocation = FMath::Lerp(ImpactOffset, RetreatOffset, FMath::Clamp(SequenceProgress, 0.0f, 1.0f));
	}

	if (ManticoreMesh != nullptr)
	{
		ManticoreMesh->SetRelativeLocation(MeshLocation);
		ManticoreMesh->SetRelativeRotation(FRotator(0.0f, 0.0f, 0.0f));
	}
	if (ImpactNiagara != nullptr)
	{
		ImpactNiagara->SetRelativeLocation(ImpactOffset + FVector(0.0f, 0.0f, 32.0f));
	}
}

void AAETManticoreInterruptActor::ApplyInterruptState()
{
	const bool bHiddenState = InterruptState == EAETManticoreInterruptState::Hidden;
	const bool bVisible = !bHiddenState || bVisibleDuringSetup;
	const bool bImpactState =
		InterruptState == EAETManticoreInterruptState::LeapImpact ||
		InterruptState == EAETManticoreInterruptState::ThreatHold;

	if (ManticoreMesh != nullptr)
	{
		ManticoreMesh->SetVisibility(bVisible, true);
		ManticoreMesh->SetHiddenInGame(!bVisible, true);
		ManticoreMesh->SetCollisionEnabled(bVisible ? ECollisionEnabled::QueryAndPhysics : ECollisionEnabled::NoCollision);
		ManticoreMesh->SetScalarParameterValueOnMaterials(TEXT("InterruptState"), static_cast<float>(static_cast<uint8>(InterruptState)));
		ManticoreMesh->SetScalarParameterValueOnMaterials(TEXT("SequenceProgress"), SequenceProgress);
		ManticoreMesh->SetScalarParameterValueOnMaterials(TEXT("ImpactIntensity"), bImpactState ? 1.0f : 0.0f);
		ManticoreMesh->SetScalarParameterValueOnMaterials(TEXT("InterruptWindowAlpha"), GetInterruptWindowAlpha());
	}

	if (ImpactNiagara != nullptr)
	{
		if (ImpactNiagaraSystem != nullptr && ImpactNiagara->GetAsset() == nullptr)
		{
			ImpactNiagara->SetAsset(ImpactNiagaraSystem);
		}

		const bool bRunNiagara = bUseNiagara && bImpactState && ImpactNiagaraSystem != nullptr;
		ImpactNiagara->SetVisibility(bRunNiagara, true);
		ImpactNiagara->SetHiddenInGame(!bRunNiagara, true);
		if (bRunNiagara && !ImpactNiagara->IsActive())
		{
			ImpactNiagara->Activate(true);
		}
		else if (!bRunNiagara && ImpactNiagara->IsActive())
		{
			ImpactNiagara->Deactivate();
		}

		ImpactNiagara->SetVariableFloat(TEXT("User.InterruptState"), static_cast<float>(static_cast<uint8>(InterruptState)));
		ImpactNiagara->SetVariableFloat(TEXT("User.SequenceProgress"), SequenceProgress);
		ImpactNiagara->SetVariableFloat(TEXT("User.InterruptWindowAlpha"), GetInterruptWindowAlpha());
		ImpactNiagara->SetVariableFloat(TEXT("User.InterruptTraceRadius"), InterruptTraceRadiusCm);
		ImpactNiagara->SetVariableFloat(TEXT("User.ImpactDamageRadius"), ImpactDamageRadiusCm);
		ImpactNiagara->SetVariableBool(TEXT("User.bImpact"), bImpactState);
		ImpactNiagara->SetVariableBool(TEXT("User.bImpactWindowActive"), IsImpactWindowActive());
		ImpactNiagara->SetVariableBool(TEXT("User.bInterruptSequenceActive"), bInterruptSequenceActive);
		ImpactNiagara->SetVariableLinearColor(TEXT("User.ImpactColor"), FLinearColor(0.18f, 0.95f, 0.30f, 1.0f));
	}
}
