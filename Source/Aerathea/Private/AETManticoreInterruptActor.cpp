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
	AssignDefaultAssets();
	UpdateInterruptLayout();
	ApplyInterruptState();
}

void AAETManticoreInterruptActor::SetInterruptState(EAETManticoreInterruptState NewState)
{
	InterruptState = NewState;
	ApplyInterruptState();
}

void AAETManticoreInterruptActor::SetSequenceProgress(float NewSequenceProgress)
{
	SequenceProgress = FMath::Clamp(NewSequenceProgress, 0.0f, 1.0f);
	UpdateInterruptLayout();
	ApplyInterruptState();
}

void AAETManticoreInterruptActor::TriggerInterrupt()
{
	InterruptState = EAETManticoreInterruptState::LeapImpact;
	SequenceProgress = 0.75f;
	UpdateInterruptLayout();
	ApplyInterruptState();
}

void AAETManticoreInterruptActor::ResetInterrupt()
{
	InterruptState = EAETManticoreInterruptState::Hidden;
	SequenceProgress = 0.0f;
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
		ImpactNiagara->SetVariableBool(TEXT("User.bImpact"), bImpactState);
		ImpactNiagara->SetVariableLinearColor(TEXT("User.ImpactColor"), FLinearColor(0.18f, 0.95f, 0.30f, 1.0f));
	}
}
