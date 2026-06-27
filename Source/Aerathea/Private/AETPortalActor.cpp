#include "AETPortalActor.h"

#include "Components/BoxComponent.h"
#include "Components/SceneComponent.h"
#include "Components/StaticMeshComponent.h"
#include "Engine/StaticMesh.h"
#include "Materials/MaterialInstanceDynamic.h"
#include "Materials/MaterialInterface.h"
#include "Net/UnrealNetwork.h"
#include "TimerManager.h"

AAETPortalActor::AAETPortalActor()
{
	PrimaryActorTick.bCanEverTick = false;
	bReplicates = true;

	bPortalActive = true;
	PortalId = TEXT("StartupPortal_A01");
	PortalState = EAETPortalState::Idle;
	DestinationId = NAME_None;
	bServerAuthoritativeUse = true;
	bAllowClientPreviewOnly = true;
	UsePreviewDurationSeconds = 0.35f;
	UseCooldownSeconds = 1.0f;
	InteractionBoxExtent = FVector(175.0f, 60.0f, 130.0f);
	bDebugPortalLogs = false;

	SceneRoot = CreateDefaultSubobject<USceneComponent>(TEXT("SceneRoot"));
	SetRootComponent(SceneRoot);

	PortalArchMesh = CreateDefaultSubobject<UStaticMeshComponent>(TEXT("PortalArchMesh"));
	PortalArchMesh->SetupAttachment(SceneRoot);
	PortalArchMesh->SetCollisionProfileName(TEXT("BlockAll"));

	PortalCoreMesh = CreateDefaultSubobject<UStaticMeshComponent>(TEXT("PortalCoreMesh"));
	PortalCoreMesh->SetupAttachment(SceneRoot);
	PortalCoreMesh->SetRelativeLocation(FVector(0.0, -18.0, 210.0));
	PortalCoreMesh->SetRelativeScale3D(FVector(1.05, 0.12, 1.55));
	PortalCoreMesh->SetCollisionEnabled(ECollisionEnabled::NoCollision);

	InteractionVolume = CreateDefaultSubobject<UBoxComponent>(TEXT("InteractionVolume"));
	InteractionVolume->SetupAttachment(SceneRoot);
	InteractionVolume->SetRelativeLocation(FVector(0.0, -36.0, 130.0));
	InteractionVolume->SetBoxExtent(InteractionBoxExtent);
	InteractionVolume->SetCollisionEnabled(ECollisionEnabled::QueryOnly);
	InteractionVolume->SetCollisionResponseToAllChannels(ECR_Ignore);
	InteractionVolume->SetCollisionResponseToChannel(ECC_Pawn, ECR_Overlap);
	InteractionVolume->SetGenerateOverlapEvents(true);
	InteractionVolume->SetVisibility(false, true);
	InteractionVolume->SetHiddenInGame(true, true);
	InteractionVolume->OnComponentBeginOverlap.AddDynamic(this, &AAETPortalActor::HandleInteractionBeginOverlap);
	InteractionVolume->OnComponentEndOverlap.AddDynamic(this, &AAETPortalActor::HandleInteractionEndOverlap);
}

void AAETPortalActor::OnConstruction(const FTransform& Transform)
{
	Super::OnConstruction(Transform);

	if (InteractionVolume != nullptr)
	{
		InteractionVolume->SetBoxExtent(InteractionBoxExtent);
		InteractionVolume->SetCollisionEnabled(ECollisionEnabled::QueryOnly);
		InteractionVolume->SetCollisionResponseToAllChannels(ECR_Ignore);
		InteractionVolume->SetCollisionResponseToChannel(ECC_Pawn, ECR_Overlap);
		InteractionVolume->SetVisibility(false, true);
		InteractionVolume->SetHiddenInGame(true, true);
	}

	if (PortalArchMesh != nullptr && PortalArchMesh->GetStaticMesh() == nullptr)
	{
		if (UStaticMesh* ArchMesh = LoadObject<UStaticMesh>(
				nullptr,
				TEXT("/Game/Aerathea/Props/Portal/SM_AET_PortalArch_A01.SM_AET_PortalArch_A01")
			))
		{
			PortalArchMesh->SetStaticMesh(ArchMesh);
		}
	}

	if (PortalCoreMesh != nullptr && PortalCoreMesh->GetStaticMesh() == nullptr)
	{
		if (UStaticMesh* CoreMesh = LoadObject<UStaticMesh>(nullptr, TEXT("/Engine/BasicShapes/Sphere.Sphere")))
		{
			PortalCoreMesh->SetStaticMesh(CoreMesh);
		}
	}

	if (PortalCoreMesh != nullptr)
	{
		if (UMaterialInterface* CoreMaterial = LoadObject<UMaterialInterface>(
				nullptr,
				TEXT("/Game/Aerathea/Materials/M_AET_AetheriumGlow_Blue_A01.M_AET_AetheriumGlow_Blue_A01")
			))
		{
			PortalCoreMesh->SetMaterial(0, CoreMaterial);
		}
	}
}

void AAETPortalActor::BeginPlay()
{
	Super::BeginPlay();

	if (PortalCoreMesh != nullptr)
	{
		PortalCoreMaterialInstance = PortalCoreMesh->CreateAndSetMaterialInstanceDynamic(0);
	}

	SetPortalState(bPortalActive ? EAETPortalState::Idle : EAETPortalState::Inactive);
}

void AAETPortalActor::GetLifetimeReplicatedProps(TArray<FLifetimeProperty>& OutLifetimeProps) const
{
	Super::GetLifetimeReplicatedProps(OutLifetimeProps);

	DOREPLIFETIME(AAETPortalActor, PortalState);
	DOREPLIFETIME(AAETPortalActor, DestinationId);
}

void AAETPortalActor::SetPortalState(EAETPortalState NewState)
{
	if (PortalState == NewState)
	{
		return;
	}

	PortalState = NewState;
	ApplyPortalVisualState();
	OnPortalStateChanged(NewState);

	if (bDebugPortalLogs)
	{
		UE_LOG(LogTemp, Display, TEXT("AETPortalActor %s state changed to %d."), *PortalId.ToString(), static_cast<uint8>(NewState));
	}
}

bool AAETPortalActor::CanInteract() const
{
	if (!bPortalActive || PortalState == EAETPortalState::Inactive || PortalState == EAETPortalState::Locked || PortalState == EAETPortalState::Blocked)
	{
		return false;
	}

	if (PortalState == EAETPortalState::UseRequested || PortalState == EAETPortalState::Cooldown)
	{
		return false;
	}

	return PortalState == EAETPortalState::Idle || PortalState == EAETPortalState::Focused || PortalState == EAETPortalState::Ready;
}

bool AAETPortalActor::RequestPortalUse(AActor* InteractingActor)
{
	if (InteractingActor == nullptr)
	{
		RejectPortalUse(InteractingActor, TEXT("NoInteractingActor"));
		return false;
	}

	if (!CanInteract())
	{
		RejectPortalUse(InteractingActor, TEXT("PortalNotInteractable"));
		return false;
	}

	if (!IsValidFocusedActor(InteractingActor))
	{
		RejectPortalUse(InteractingActor, TEXT("ActorNotInRange"));
		return false;
	}

	const bool bPreviewOnlyRequest = bAllowClientPreviewOnly && !HasValidDestination();
	if (bServerAuthoritativeUse && !HasAuthority() && !bPreviewOnlyRequest)
	{
		RejectPortalUse(InteractingActor, TEXT("RequiresServerAuthority"));
		return false;
	}

	if (!bPreviewOnlyRequest && !HasValidDestination())
	{
		RejectPortalUse(InteractingActor, TEXT("MissingDestination"));
		return false;
	}

	OnPortalUseRequested(InteractingActor);
	SetPortalState(EAETPortalState::UseRequested);

	GetWorldTimerManager().ClearTimer(UsePreviewTimerHandle);
	GetWorldTimerManager().SetTimer(UsePreviewTimerHandle, this, &AAETPortalActor::EnterUseCooldown, UsePreviewDurationSeconds, false);

	if (bDebugPortalLogs)
	{
		UE_LOG(
			LogTemp,
			Display,
			TEXT("AETPortalActor %s accepted preview use for %s toward destination %s."),
			*PortalId.ToString(),
			*GetNameSafe(InteractingActor),
			*DestinationId.ToString()
		);
	}

	return true;
}

void AAETPortalActor::SetPortalActive(bool bNewPortalActive)
{
	bPortalActive = bNewPortalActive;
	SetPortalState(bPortalActive ? EAETPortalState::Idle : EAETPortalState::Inactive);
}

bool AAETPortalActor::HasValidDestination() const
{
	return !DestinationId.IsNone() && DestinationId != TEXT("None") && DestinationId != TEXT("TODO_AET_PORTAL_DESTINATION");
}

void AAETPortalActor::HandleInteractionBeginOverlap(
	UPrimitiveComponent* OverlappedComponent,
	AActor* OtherActor,
	UPrimitiveComponent* OtherComp,
	int32 OtherBodyIndex,
	bool bFromSweep,
	const FHitResult& SweepResult
)
{
	if (OtherActor != nullptr && OtherActor != this)
	{
		LastOverlappingActor = OtherActor;
		OnPortalFocusChanged(OtherActor, true);

		if (CanInteract())
		{
			SetPortalState(EAETPortalState::Focused);
		}
	}
}

void AAETPortalActor::HandleInteractionEndOverlap(
	UPrimitiveComponent* OverlappedComponent,
	AActor* OtherActor,
	UPrimitiveComponent* OtherComp,
	int32 OtherBodyIndex
)
{
	if (OtherActor != nullptr && OtherActor == LastOverlappingActor)
	{
		OnPortalFocusChanged(OtherActor, false);
		LastOverlappingActor = nullptr;

		if (PortalState == EAETPortalState::Focused)
		{
			SetPortalState(bPortalActive ? EAETPortalState::Idle : EAETPortalState::Inactive);
		}
	}
}

void AAETPortalActor::EnterUseCooldown()
{
	SetPortalState(EAETPortalState::Cooldown);

	GetWorldTimerManager().ClearTimer(CooldownTimerHandle);
	GetWorldTimerManager().SetTimer(CooldownTimerHandle, this, &AAETPortalActor::ReturnToSafeState, UseCooldownSeconds, false);
}

void AAETPortalActor::ReturnToSafeState()
{
	if (!bPortalActive)
	{
		SetPortalState(EAETPortalState::Inactive);
		return;
	}

	SetPortalState(IsValidFocusedActor(LastOverlappingActor) ? EAETPortalState::Focused : EAETPortalState::Idle);
}

void AAETPortalActor::ApplyPortalVisualState()
{
	if (PortalCoreMaterialInstance == nullptr)
	{
		return;
	}

	float CoreOpacity = 0.75f;
	float PulseIntensity = 0.35f;
	float RimGlowIntensity = 0.45f;
	float ActivationAlpha = 0.0f;

	switch (PortalState)
	{
	case EAETPortalState::Inactive:
		CoreOpacity = 0.0f;
		PulseIntensity = 0.0f;
		RimGlowIntensity = 0.0f;
		break;
	case EAETPortalState::Focused:
		CoreOpacity = 0.85f;
		PulseIntensity = 0.55f;
		RimGlowIntensity = 0.65f;
		ActivationAlpha = 0.25f;
		break;
	case EAETPortalState::UseRequested:
		CoreOpacity = 1.0f;
		PulseIntensity = 0.85f;
		RimGlowIntensity = 0.9f;
		ActivationAlpha = 1.0f;
		break;
	case EAETPortalState::Cooldown:
		CoreOpacity = 0.8f;
		PulseIntensity = 0.45f;
		RimGlowIntensity = 0.55f;
		ActivationAlpha = 0.1f;
		break;
	case EAETPortalState::Locked:
	case EAETPortalState::Blocked:
		CoreOpacity = 0.3f;
		PulseIntensity = 0.1f;
		RimGlowIntensity = 0.2f;
		break;
	case EAETPortalState::Idle:
	case EAETPortalState::Charging:
	case EAETPortalState::Ready:
	default:
		break;
	}

	PortalCoreMaterialInstance->SetScalarParameterValue(TEXT("CoreOpacity"), CoreOpacity);
	PortalCoreMaterialInstance->SetScalarParameterValue(TEXT("PulseIntensity"), PulseIntensity);
	PortalCoreMaterialInstance->SetScalarParameterValue(TEXT("RimGlowIntensity"), RimGlowIntensity);
	PortalCoreMaterialInstance->SetScalarParameterValue(TEXT("ActivationAlpha"), ActivationAlpha);
}

bool AAETPortalActor::IsValidFocusedActor(AActor* Actor) const
{
	return Actor != nullptr && Actor != this && Actor == LastOverlappingActor;
}

void AAETPortalActor::RejectPortalUse(AActor* InteractingActor, FName Reason)
{
	OnPortalUseRejected(InteractingActor, Reason);

	if (bDebugPortalLogs)
	{
		UE_LOG(
			LogTemp,
			Display,
			TEXT("AETPortalActor %s rejected use for %s: %s."),
			*PortalId.ToString(),
			*GetNameSafe(InteractingActor),
			*Reason.ToString()
		);
	}
}
