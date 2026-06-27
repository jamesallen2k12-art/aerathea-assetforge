#include "AETTargetDummyActor.h"

#include "Components/BoxComponent.h"
#include "Components/SceneComponent.h"
#include "Components/StaticMeshComponent.h"
#include "Engine/DamageEvents.h"
#include "Engine/StaticMesh.h"
#include "TimerManager.h"

AAETTargetDummyActor::AAETTargetDummyActor()
{
	PrimaryActorTick.bCanEverTick = false;
	bReplicates = true;

	MaxTrainingHealth = 100.0f;
	CurrentTrainingHealth = MaxTrainingHealth;
	HitReactionDurationSeconds = 0.2f;
	ResetDelaySeconds = 2.0f;
	bAutoResetAfterBreak = true;
	bDebugHitLogs = false;

	SceneRoot = CreateDefaultSubobject<USceneComponent>(TEXT("SceneRoot"));
	SetRootComponent(SceneRoot);

	DummyMesh = CreateDefaultSubobject<UStaticMeshComponent>(TEXT("DummyMesh"));
	DummyMesh->SetupAttachment(SceneRoot);
	DummyMesh->SetCollisionProfileName(TEXT("BlockAll"));

	HitVolume = CreateDefaultSubobject<UBoxComponent>(TEXT("HitVolume"));
	HitVolume->SetupAttachment(SceneRoot);
	HitVolume->SetRelativeLocation(FVector(0.0f, 0.0f, 120.0f));
	HitVolume->SetBoxExtent(FVector(75.0f, 35.0f, 95.0f));
	HitVolume->SetCollisionEnabled(ECollisionEnabled::QueryOnly);
	HitVolume->SetCollisionResponseToAllChannels(ECR_Ignore);
	HitVolume->SetCollisionResponseToChannel(ECC_Visibility, ECR_Block);
	HitVolume->SetCollisionResponseToChannel(ECC_WorldDynamic, ECR_Overlap);
	HitVolume->SetGenerateOverlapEvents(false);
	HitVolume->SetVisibility(false, true);
	HitVolume->SetHiddenInGame(true, true);
}

void AAETTargetDummyActor::OnConstruction(const FTransform& Transform)
{
	Super::OnConstruction(Transform);

	if (DummyMesh != nullptr && DummyMesh->GetStaticMesh() == nullptr)
	{
		if (UStaticMesh* TargetDummyMesh = LoadObject<UStaticMesh>(
				nullptr,
				TEXT("/Game/Aerathea/Props/Training/SM_AET_TargetDummy_A01.SM_AET_TargetDummy_A01")
			))
		{
			DummyMesh->SetStaticMesh(TargetDummyMesh);
		}
	}

	if (HitVolume != nullptr)
	{
		HitVolume->SetVisibility(false, true);
		HitVolume->SetHiddenInGame(true, true);
	}
}

void AAETTargetDummyActor::BeginPlay()
{
	Super::BeginPlay();

	ResetTrainingHealth();
}

float AAETTargetDummyActor::TakeDamage(
	float DamageAmount,
	FDamageEvent const& DamageEvent,
	AController* EventInstigator,
	AActor* DamageCauser
)
{
	const float AppliedDamage = Super::TakeDamage(DamageAmount, DamageEvent, EventInstigator, DamageCauser);
	const float TrainingDamage = AppliedDamage > 0.0f ? AppliedDamage : DamageAmount;
	return RegisterTrainingHit(TrainingDamage, DamageCauser, NAME_None);
}

float AAETTargetDummyActor::RegisterTrainingHit(float DamageAmount, AActor* DamageCauser, FName HitZone)
{
	if (!CanReceiveTrainingHit() || DamageAmount <= 0.0f)
	{
		return 0.0f;
	}

	CurrentTrainingHealth = FMath::Clamp(CurrentTrainingHealth - DamageAmount, 0.0f, MaxTrainingHealth);
	const float ScoreValue = DamageAmount;

	OnTrainingHit(DamageAmount, ScoreValue, DamageCauser, HitZone);
	OnHitReactionStateChanged(true);

	GetWorldTimerManager().ClearTimer(HitReactionTimerHandle);
	GetWorldTimerManager().SetTimer(HitReactionTimerHandle, this, &AAETTargetDummyActor::EndHitReaction, HitReactionDurationSeconds, false);

	if (bDebugHitLogs)
	{
		UE_LOG(
			LogTemp,
			Display,
			TEXT("AETTargetDummyActor %s received %.1f damage from %s. Training health %.1f/%.1f."),
			*GetName(),
			DamageAmount,
			*GetNameSafe(DamageCauser),
			CurrentTrainingHealth,
			MaxTrainingHealth
		);
	}

	if (CurrentTrainingHealth <= 0.0f)
	{
		BreakTrainingDummy(DamageCauser);
	}

	return ScoreValue;
}

void AAETTargetDummyActor::ResetTrainingHealth()
{
	CurrentTrainingHealth = MaxTrainingHealth;
	GetWorldTimerManager().ClearTimer(ResetTimerHandle);
	OnTrainingReset();
}

bool AAETTargetDummyActor::CanReceiveTrainingHit() const
{
	return MaxTrainingHealth > 0.0f && CurrentTrainingHealth > 0.0f;
}

void AAETTargetDummyActor::EndHitReaction()
{
	OnHitReactionStateChanged(false);
}

void AAETTargetDummyActor::BreakTrainingDummy(AActor* DamageCauser)
{
	OnTrainingBroken(DamageCauser);

	if (bAutoResetAfterBreak)
	{
		GetWorldTimerManager().ClearTimer(ResetTimerHandle);
		GetWorldTimerManager().SetTimer(ResetTimerHandle, this, &AAETTargetDummyActor::ResetTrainingHealth, ResetDelaySeconds, false);
	}
}
