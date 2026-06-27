#include "AETHeavyMekShieldwallActor.h"

#include "Components/AudioComponent.h"
#include "Components/BoxComponent.h"
#include "Components/SceneComponent.h"
#include "Components/SplineComponent.h"
#include "Components/StaticMeshComponent.h"
#include "Engine/StaticMesh.h"

AAETHeavyMekShieldwallActor::AAETHeavyMekShieldwallActor()
{
	PrimaryActorTick.bCanEverTick = false;
	bReplicates = true;

	ShieldState = EAETShieldwallState::Braced;
	ShieldWidthCm = 700.0f;
	ProjectorCount = 3;
	ArcHeightCm = 340.0f;
	bBlocksProjectiles = true;
	bBlocksPawns = false;
	ImpactIntensity = 0.0f;
	OverloadPercent = 0.0f;

	SceneRoot = CreateDefaultSubobject<USceneComponent>(TEXT("Root"));
	SetRootComponent(SceneRoot);

	Projector01 = CreateDefaultSubobject<UStaticMeshComponent>(TEXT("Projector_01"));
	Projector02 = CreateDefaultSubobject<UStaticMeshComponent>(TEXT("Projector_02"));
	Projector03 = CreateDefaultSubobject<UStaticMeshComponent>(TEXT("Projector_03"));
	Projector04 = CreateDefaultSubobject<UStaticMeshComponent>(TEXT("Projector_04"));
	Projector05 = CreateDefaultSubobject<UStaticMeshComponent>(TEXT("Projector_05"));

	for (UStaticMeshComponent* Projector : ProjectorComponents())
	{
		Projector->SetupAttachment(SceneRoot);
		Projector->SetCollisionProfileName(TEXT("BlockAll"));
	}

	ShieldSpline = CreateDefaultSubobject<USplineComponent>(TEXT("ShieldSpline"));
	ShieldSpline->SetupAttachment(SceneRoot);
	ShieldSpline->SetCollisionEnabled(ECollisionEnabled::NoCollision);

	ShieldPanel01 = CreateDefaultSubobject<UStaticMeshComponent>(TEXT("ShieldPanel_01"));
	ShieldPanel02 = CreateDefaultSubobject<UStaticMeshComponent>(TEXT("ShieldPanel_02"));
	ShieldPanel03 = CreateDefaultSubobject<UStaticMeshComponent>(TEXT("ShieldPanel_03"));
	ShieldPanel04 = CreateDefaultSubobject<UStaticMeshComponent>(TEXT("ShieldPanel_04"));

	for (UStaticMeshComponent* Panel : ShieldPanelComponents())
	{
		Panel->SetupAttachment(SceneRoot);
		Panel->SetCollisionEnabled(ECollisionEnabled::NoCollision);
		Panel->SetGenerateOverlapEvents(false);
	}

	ShieldCollision = CreateDefaultSubobject<UBoxComponent>(TEXT("ShieldCollision"));
	ShieldCollision->SetupAttachment(SceneRoot);
	ShieldCollision->SetCollisionEnabled(ECollisionEnabled::NoCollision);
	ShieldCollision->SetCollisionResponseToAllChannels(ECR_Ignore);
	ShieldCollision->SetGenerateOverlapEvents(false);
	ShieldCollision->SetVisibility(false, true);
	ShieldCollision->SetHiddenInGame(true, true);

	ImpactLocator = CreateDefaultSubobject<USceneComponent>(TEXT("ImpactLocator"));
	ImpactLocator->SetupAttachment(SceneRoot);

	AudioShieldLoop = CreateDefaultSubobject<UAudioComponent>(TEXT("AudioShieldLoop"));
	AudioShieldLoop->SetupAttachment(SceneRoot);
	AudioShieldLoop->bAutoActivate = false;
}

void AAETHeavyMekShieldwallActor::OnConstruction(const FTransform& Transform)
{
	Super::OnConstruction(Transform);

	ProjectorCount = FMath::Clamp(ProjectorCount, 3, 5);
	ShieldWidthCm = FMath::Clamp(ShieldWidthCm, 300.0f, 1200.0f);
	ArcHeightCm = FMath::Clamp(ArcHeightCm, 180.0f, 520.0f);
	ImpactIntensity = FMath::Clamp(ImpactIntensity, 0.0f, 1.0f);
	OverloadPercent = FMath::Clamp(OverloadPercent, 0.0f, 1.0f);

	AssignDefaultAssets();
	UpdateShieldwallLayout();
	ApplyShieldState();
}

void AAETHeavyMekShieldwallActor::SetShieldState(EAETShieldwallState NewState)
{
	ShieldState = NewState;
	ApplyShieldState();
}

void AAETHeavyMekShieldwallActor::SetImpactIntensity(float NewImpactIntensity)
{
	ImpactIntensity = FMath::Clamp(NewImpactIntensity, 0.0f, 1.0f);
	ApplyShieldState();
}

void AAETHeavyMekShieldwallActor::SetOverloadPercent(float NewOverloadPercent)
{
	OverloadPercent = FMath::Clamp(NewOverloadPercent, 0.0f, 1.0f);
	ApplyShieldState();
}

void AAETHeavyMekShieldwallActor::ConfigureShieldwall(int32 NewProjectorCount, float NewShieldWidthCm, float NewArcHeightCm)
{
	ProjectorCount = FMath::Clamp(NewProjectorCount, 3, 5);
	ShieldWidthCm = FMath::Clamp(NewShieldWidthCm, 300.0f, 1200.0f);
	ArcHeightCm = FMath::Clamp(NewArcHeightCm, 180.0f, 520.0f);
	UpdateShieldwallLayout();
	ApplyShieldState();
}

void AAETHeavyMekShieldwallActor::AssignDefaultAssets()
{
	UStaticMesh* ProjectorMesh = LoadObject<UStaticMesh>(
		nullptr,
		TEXT("/Game/Aerathea/Props/Gnomes/Mekgineer/SM_GNM_AetherShieldProjector_A01.SM_GNM_AetherShieldProjector_A01")
	);
	UStaticMesh* ShieldPanelMesh = LoadObject<UStaticMesh>(
		nullptr,
		TEXT("/Game/Aerathea/VFX/GnomeOgre/SM_GNM_AetherShieldWall_A01.SM_GNM_AetherShieldWall_A01")
	);

	if (ProjectorMesh != nullptr)
	{
		for (UStaticMeshComponent* Projector : ProjectorComponents())
		{
			if (Projector != nullptr && Projector->GetStaticMesh() == nullptr)
			{
				Projector->SetStaticMesh(ProjectorMesh);
			}
		}
	}

	if (ShieldPanelMesh != nullptr)
	{
		for (UStaticMeshComponent* Panel : ShieldPanelComponents())
		{
			if (Panel != nullptr && Panel->GetStaticMesh() == nullptr)
			{
				Panel->SetStaticMesh(ShieldPanelMesh);
			}
		}
	}
}

void AAETHeavyMekShieldwallActor::UpdateShieldwallLayout()
{
	const TArray<UStaticMeshComponent*> Projectors = ProjectorComponents();
	const TArray<UStaticMeshComponent*> Panels = ShieldPanelComponents();
	const int32 ActiveProjectors = FMath::Clamp(ProjectorCount, 3, 5);
	const float SegmentLength = ShieldWidthCm / static_cast<float>(ActiveProjectors - 1);
	const float ProjectorCenter = static_cast<float>(ActiveProjectors - 1) * 0.5f;

	if (ShieldSpline != nullptr)
	{
		ShieldSpline->ClearSplinePoints(false);
	}

	for (int32 Index = 0; Index < Projectors.Num(); ++Index)
	{
		UStaticMeshComponent* Projector = Projectors[Index];
		if (Projector == nullptr)
		{
			continue;
		}

		const bool bActive = Index < ActiveProjectors;
		Projector->SetVisibility(bActive, true);
		Projector->SetHiddenInGame(!bActive, true);
		if (!bActive)
		{
			continue;
		}

		const float Normalized = (static_cast<float>(Index) - ProjectorCenter) / ProjectorCenter;
		const float Y = (static_cast<float>(Index) - ProjectorCenter) * SegmentLength;
		const float X = -55.0f * FMath::Abs(Normalized);
		const FRotator Rotation(0.0f, -Normalized * 14.0f, 0.0f);
		Projector->SetRelativeLocation(FVector(X, Y, 0.0f));
		Projector->SetRelativeRotation(Rotation);

		if (ShieldSpline != nullptr)
		{
			ShieldSpline->AddSplinePoint(FVector(34.0f, Y, ArcHeightCm * 0.52f), ESplineCoordinateSpace::Local, false);
		}
	}

	if (ShieldSpline != nullptr)
	{
		ShieldSpline->UpdateSpline();
	}

	for (int32 Index = 0; Index < Panels.Num(); ++Index)
	{
		UStaticMeshComponent* Panel = Panels[Index];
		if (Panel == nullptr)
		{
			continue;
		}

		const bool bActive = Index < ActiveProjectors - 1;
		Panel->SetVisibility(bActive, true);
		Panel->SetHiddenInGame(!bActive, true);
		if (!bActive)
		{
			continue;
		}

		const float MidIndex = static_cast<float>(Index) + 0.5f;
		const float Normalized = (MidIndex - ProjectorCenter) / ProjectorCenter;
		const float Y = (MidIndex - ProjectorCenter) * SegmentLength;
		const float X = 32.0f - 24.0f * FMath::Abs(Normalized);
		Panel->SetRelativeLocation(FVector(X, Y, 0.0f));
		Panel->SetRelativeRotation(FRotator(0.0f, -Normalized * 8.0f, 0.0f));
		Panel->SetRelativeScale3D(FVector(1.0f, SegmentLength / 170.0f, ArcHeightCm / 340.0f));
	}

	if (ShieldCollision != nullptr)
	{
		ShieldCollision->SetRelativeLocation(FVector(34.0f, 0.0f, ArcHeightCm * 0.5f));
		ShieldCollision->SetBoxExtent(FVector(28.0f, ShieldWidthCm * 0.52f, ArcHeightCm * 0.5f));
	}

	if (ImpactLocator != nullptr)
	{
		ImpactLocator->SetRelativeLocation(FVector(46.0f, 0.0f, ArcHeightCm * 0.62f));
	}
}

void AAETHeavyMekShieldwallActor::ApplyShieldState()
{
	const bool bShieldVisible = ShieldState != EAETShieldwallState::Inactive && ShieldState != EAETShieldwallState::Shutdown;
	const bool bCollisionEnabled =
		bShieldVisible &&
		ShieldState != EAETShieldwallState::Failing &&
		(bBlocksProjectiles || bBlocksPawns);

	const TArray<UStaticMeshComponent*> Panels = ShieldPanelComponents();
	const int32 ActivePanelCount = FMath::Clamp(ProjectorCount, 3, 5) - 1;
	for (int32 Index = 0; Index < Panels.Num(); ++Index)
	{
		UStaticMeshComponent* Panel = Panels[Index];
		if (Panel == nullptr)
		{
			continue;
		}
		const bool bPanelSlotActive = Index < ActivePanelCount;
		Panel->SetVisibility(bShieldVisible && bPanelSlotActive, true);
		Panel->SetHiddenInGame(!(bShieldVisible && bPanelSlotActive), true);
	}

	if (ShieldCollision != nullptr)
	{
		ShieldCollision->SetCollisionEnabled(bCollisionEnabled ? ECollisionEnabled::QueryOnly : ECollisionEnabled::NoCollision);
		ShieldCollision->SetCollisionResponseToAllChannels(ECR_Ignore);
		ShieldCollision->SetCollisionResponseToChannel(ECC_Visibility, bBlocksProjectiles ? ECR_Block : ECR_Ignore);
		ShieldCollision->SetCollisionResponseToChannel(ECC_WorldDynamic, bBlocksProjectiles ? ECR_Block : ECR_Ignore);
		ShieldCollision->SetCollisionResponseToChannel(ECC_Pawn, bBlocksPawns ? ECR_Block : ECR_Ignore);
		ShieldCollision->SetVisibility(false, true);
		ShieldCollision->SetHiddenInGame(true, true);
	}
}

TArray<UStaticMeshComponent*> AAETHeavyMekShieldwallActor::ProjectorComponents() const
{
	return {
		Projector01,
		Projector02,
		Projector03,
		Projector04,
		Projector05,
	};
}

TArray<UStaticMeshComponent*> AAETHeavyMekShieldwallActor::ShieldPanelComponents() const
{
	return {
		ShieldPanel01,
		ShieldPanel02,
		ShieldPanel03,
		ShieldPanel04,
	};
}
