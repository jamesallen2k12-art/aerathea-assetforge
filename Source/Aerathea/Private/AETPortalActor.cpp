#include "AETPortalActor.h"

#include "Components/BoxComponent.h"
#include "Components/SceneComponent.h"
#include "Components/StaticMeshComponent.h"
#include "Engine/StaticMesh.h"
#include "Materials/MaterialInterface.h"

AAETPortalActor::AAETPortalActor()
{
	PrimaryActorTick.bCanEverTick = false;
	bReplicates = true;

	PortalState = EAETPortalState::Idle;
	DestinationId = TEXT("TODO_AET_PORTAL_DESTINATION");
	bServerAuthoritativeUse = true;

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
	InteractionVolume->SetRelativeLocation(FVector(0.0, -36.0, 150.0));
	InteractionVolume->SetBoxExtent(FVector(110.0, 80.0, 160.0));
	InteractionVolume->SetCollisionEnabled(ECollisionEnabled::QueryOnly);
	InteractionVolume->SetCollisionResponseToAllChannels(ECR_Ignore);
	InteractionVolume->SetCollisionResponseToChannel(ECC_Pawn, ECR_Overlap);
	InteractionVolume->SetGenerateOverlapEvents(true);
	InteractionVolume->OnComponentBeginOverlap.AddDynamic(this, &AAETPortalActor::HandleInteractionBeginOverlap);
	InteractionVolume->OnComponentEndOverlap.AddDynamic(this, &AAETPortalActor::HandleInteractionEndOverlap);
}

void AAETPortalActor::OnConstruction(const FTransform& Transform)
{
	Super::OnConstruction(Transform);

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

void AAETPortalActor::SetPortalState(EAETPortalState NewState)
{
	if (PortalState == NewState)
	{
		return;
	}

	PortalState = NewState;
	OnPortalStateChanged(NewState);
}

bool AAETPortalActor::CanInteract() const
{
	return PortalState == EAETPortalState::Idle || PortalState == EAETPortalState::Ready;
}

bool AAETPortalActor::RequestPortalUse(AActor* InteractingActor)
{
	if (InteractingActor == nullptr || !CanInteract())
	{
		return false;
	}

	if (bServerAuthoritativeUse && !HasAuthority())
	{
		return false;
	}

	LastOverlappingActor = InteractingActor;
	OnPortalUseRequested(InteractingActor);
	return true;
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
		LastOverlappingActor = nullptr;
	}
}
