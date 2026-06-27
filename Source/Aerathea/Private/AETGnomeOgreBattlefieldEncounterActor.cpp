#include "AETGnomeOgreBattlefieldEncounterActor.h"

#include "AETCrudeTekPylonActor.h"
#include "AETHeavyMekShieldwallActor.h"
#include "AETManticoreInterruptActor.h"
#include "Components/BoxComponent.h"
#include "Components/SceneComponent.h"

AAETGnomeOgreBattlefieldEncounterActor::AAETGnomeOgreBattlefieldEncounterActor()
{
	PrimaryActorTick.bCanEverTick = true;
	bReplicates = true;

	EncounterState = EAETGnomeOgreEncounterState::Setup;
	bAutoStart = false;
	bUsePlacedActors = true;
	bEnablePylonObjective = false;
	bEnableCasterReinforcements = false;
	bEnableManticoreInterrupt = false;
	bLoopForReview = false;
	bAutoAdvanceReviewPhases = false;
	ReviewPhaseDurationSeconds = 3.0f;
	ReviewPhaseElapsedSeconds = 0.0f;
	ReviewPhaseIndex = 0;
	EncounterWidthCm = 2800.0f;
	EncounterDepthCm = 2200.0f;
	ShieldImpactLocationNormalized = 0.5f;
	PylonOverloadPercent = 0.0f;
	LastValidationReport = TEXT("Not validated.");

	SceneRoot = CreateDefaultSubobject<USceneComponent>(TEXT("SceneRoot"));
	SetRootComponent(SceneRoot);

	EncounterBounds = CreateDefaultSubobject<UBoxComponent>(TEXT("EncounterBounds"));
	EncounterBounds->SetupAttachment(SceneRoot);
	EncounterBounds->SetCollisionEnabled(ECollisionEnabled::NoCollision);
	EncounterBounds->SetGenerateOverlapEvents(false);
	EncounterBounds->SetVisibility(false, true);
	EncounterBounds->SetHiddenInGame(true, true);

	GnomeLineMarker = CreateDefaultSubobject<USceneComponent>(TEXT("GnomeLineMarker"));
	OgreLineMarker = CreateDefaultSubobject<USceneComponent>(TEXT("OgreLineMarker"));
	GateMarker = CreateDefaultSubobject<USceneComponent>(TEXT("GateMarker"));
	PylonMarker = CreateDefaultSubobject<USceneComponent>(TEXT("PylonMarker"));
	ManticoreEntryMarker = CreateDefaultSubobject<USceneComponent>(TEXT("ManticoreEntryMarker"));
	for (USceneComponent* Marker : {GnomeLineMarker, OgreLineMarker, GateMarker, PylonMarker, ManticoreEntryMarker})
	{
		Marker->SetupAttachment(SceneRoot);
	}

	ShieldwallTrigger = CreateDefaultSubobject<UBoxComponent>(TEXT("ShieldwallTrigger"));
	PylonTrigger = CreateDefaultSubobject<UBoxComponent>(TEXT("PylonTrigger"));
	ManticoreTrigger = CreateDefaultSubobject<UBoxComponent>(TEXT("ManticoreTrigger"));
	for (UBoxComponent* Trigger : {ShieldwallTrigger, PylonTrigger, ManticoreTrigger})
	{
		Trigger->SetupAttachment(SceneRoot);
		Trigger->SetCollisionEnabled(ECollisionEnabled::QueryOnly);
		Trigger->SetCollisionResponseToAllChannels(ECR_Ignore);
		Trigger->SetCollisionResponseToChannel(ECC_Pawn, ECR_Overlap);
		Trigger->SetGenerateOverlapEvents(true);
		Trigger->SetVisibility(false, true);
		Trigger->SetHiddenInGame(true, true);
	}
}

void AAETGnomeOgreBattlefieldEncounterActor::OnConstruction(const FTransform& Transform)
{
	Super::OnConstruction(Transform);

	EncounterWidthCm = FMath::Clamp(EncounterWidthCm, 1200.0f, 6000.0f);
	EncounterDepthCm = FMath::Clamp(EncounterDepthCm, 1200.0f, 6000.0f);
	ShieldImpactLocationNormalized = FMath::Clamp(ShieldImpactLocationNormalized, -1.0f, 1.0f);
	PylonOverloadPercent = FMath::Clamp(PylonOverloadPercent, 0.0f, 1.0f);
	ReviewPhaseDurationSeconds = FMath::Clamp(ReviewPhaseDurationSeconds, 0.25f, 30.0f);
	UpdateEncounterLayout();
	ApplyEncounterState();
}

void AAETGnomeOgreBattlefieldEncounterActor::BeginPlay()
{
	Super::BeginPlay();

	ValidateDependencies();
	if (bAutoAdvanceReviewPhases)
	{
		StartReviewPhaseSequence();
	}
	else if (bAutoStart)
	{
		SetEncounterState(EAETGnomeOgreEncounterState::GnomeHoldLine);
	}
}

void AAETGnomeOgreBattlefieldEncounterActor::Tick(float DeltaSeconds)
{
	Super::Tick(DeltaSeconds);

	if (!bAutoAdvanceReviewPhases || ReviewPhaseDurationSeconds <= KINDA_SMALL_NUMBER)
	{
		return;
	}

	ReviewPhaseElapsedSeconds += DeltaSeconds;
	if (ReviewPhaseElapsedSeconds >= ReviewPhaseDurationSeconds)
	{
		ReviewPhaseElapsedSeconds = 0.0f;
		AdvanceReviewPhase();
	}
}

bool AAETGnomeOgreBattlefieldEncounterActor::ValidateDependencies()
{
	TArray<FString> MissingRequired;
	TArray<FString> MissingOptional;

	if (ShieldwallActor == nullptr)
	{
		MissingRequired.Add(TEXT("ShieldwallActor"));
	}
	if (GnomeHeavyMekActor == nullptr)
	{
		MissingRequired.Add(TEXT("GnomeHeavyMekActor"));
	}
	if (OgreTeknomancerActor == nullptr)
	{
		MissingRequired.Add(TEXT("OgreTeknomancerActor"));
	}
	if (OgreWarriorActor == nullptr)
	{
		MissingRequired.Add(TEXT("OgreWarriorActor"));
	}
	if (CairnGateActor == nullptr)
	{
		MissingRequired.Add(TEXT("CairnGateActor"));
	}

	if (bEnablePylonObjective && PylonObjectiveActor == nullptr)
	{
		MissingOptional.Add(TEXT("PylonObjectiveActor"));
	}
	if (bEnableCasterReinforcements && OgreShamanActor == nullptr && OgreNecromancerActor == nullptr)
	{
		MissingOptional.Add(TEXT("OgreShamanActor or OgreNecromancerActor"));
	}
	if (bEnableManticoreInterrupt && ManticoreInterruptActor == nullptr)
	{
		MissingOptional.Add(TEXT("ManticoreInterruptActor"));
	}

	if (MissingRequired.Num() > 0)
	{
		LastValidationReport = FString::Printf(TEXT("Missing required dependencies: %s."), *FString::Join(MissingRequired, TEXT(", ")));
		if (MissingOptional.Num() > 0)
		{
			LastValidationReport += FString::Printf(TEXT(" Missing optional branches: %s."), *FString::Join(MissingOptional, TEXT(", ")));
		}
		OnEncounterValidationFailed.Broadcast(LastValidationReport);
		return false;
	}

	LastValidationReport = TEXT("Core dependencies valid.");
	if (MissingOptional.Num() > 0)
	{
		LastValidationReport += FString::Printf(TEXT(" Optional branches disabled or waiting on imports: %s."), *FString::Join(MissingOptional, TEXT(", ")));
	}
	return true;
}

void AAETGnomeOgreBattlefieldEncounterActor::ConfigureEncounter(
	float NewEncounterWidthCm,
	float NewEncounterDepthCm,
	bool bNewEnablePylonObjective,
	bool bNewEnableCasterReinforcements,
	bool bNewEnableManticoreInterrupt
)
{
	EncounterWidthCm = FMath::Clamp(NewEncounterWidthCm, 1200.0f, 6000.0f);
	EncounterDepthCm = FMath::Clamp(NewEncounterDepthCm, 1200.0f, 6000.0f);
	bEnablePylonObjective = bNewEnablePylonObjective;
	bEnableCasterReinforcements = bNewEnableCasterReinforcements;
	bEnableManticoreInterrupt = bNewEnableManticoreInterrupt;
	UpdateEncounterLayout();
	ValidateDependencies();
}

void AAETGnomeOgreBattlefieldEncounterActor::SetEncounterState(EAETGnomeOgreEncounterState NewState)
{
	if (EncounterState == NewState)
	{
		ApplyEncounterState();
		return;
	}

	EncounterState = NewState;
	ApplyEncounterState();
	OnEncounterPhaseChanged.Broadcast(NewState);
}

void AAETGnomeOgreBattlefieldEncounterActor::TriggerShieldImpact(float NewImpactLocationNormalized, float NewImpactIntensity)
{
	ShieldImpactLocationNormalized = FMath::Clamp(NewImpactLocationNormalized, -1.0f, 1.0f);
	if (ShieldwallActor != nullptr)
	{
		ShieldwallActor->TriggerImpact(ShieldImpactLocationNormalized, NewImpactIntensity);
	}
	SetEncounterState(EAETGnomeOgreEncounterState::ShieldImpact);
}

void AAETGnomeOgreBattlefieldEncounterActor::TriggerPylonOverload(float NewOverloadPercent)
{
	PylonOverloadPercent = FMath::Clamp(NewOverloadPercent, 0.0f, 1.0f);
	if (AAETCrudeTekPylonActor* PylonActor = Cast<AAETCrudeTekPylonActor>(PylonObjectiveActor.Get()))
	{
		PylonActor->TriggerOverload(PylonOverloadPercent);
	}
	if (ShieldwallActor != nullptr)
	{
		ShieldwallActor->SetOverloadPercent(PylonOverloadPercent);
	}
	OnPylonOverloadTriggered.Broadcast(PylonOverloadPercent);
	SetEncounterState(EAETGnomeOgreEncounterState::PylonOverload);
}

void AAETGnomeOgreBattlefieldEncounterActor::TriggerCasterReinforcement(AActor* CasterActor)
{
	if (CasterActor != nullptr)
	{
		SetOptionalActorEnabled(CasterActor, true);
		OnCasterReinforcementTriggered.Broadcast(CasterActor);
	}
	SetEncounterState(EAETGnomeOgreEncounterState::CasterReinforcement);
}

void AAETGnomeOgreBattlefieldEncounterActor::TriggerManticoreInterrupt(AActor* ManticoreActor)
{
	AActor* ActorToTrigger = ManticoreActor != nullptr ? ManticoreActor : ManticoreInterruptActor.Get();
	if (ActorToTrigger != nullptr)
	{
		SetOptionalActorEnabled(ActorToTrigger, true);
		if (AAETManticoreInterruptActor* InterruptActor = Cast<AAETManticoreInterruptActor>(ActorToTrigger))
		{
			InterruptActor->TriggerInterrupt();
		}
		OnManticoreInterruptTriggered.Broadcast(ActorToTrigger);
	}
	SetEncounterState(EAETGnomeOgreEncounterState::ManticoreInterrupt);
}

void AAETGnomeOgreBattlefieldEncounterActor::StartReviewPhaseSequence()
{
	ValidateDependencies();
	bAutoAdvanceReviewPhases = true;
	ReviewPhaseElapsedSeconds = 0.0f;
	ReviewPhaseIndex = 0;
	ApplyReviewPhase(ReviewPhaseIndex);
}

void AAETGnomeOgreBattlefieldEncounterActor::StopReviewPhaseSequence()
{
	bAutoAdvanceReviewPhases = false;
	ReviewPhaseElapsedSeconds = 0.0f;
}

void AAETGnomeOgreBattlefieldEncounterActor::AdvanceReviewPhase()
{
	++ReviewPhaseIndex;

	constexpr int32 ReviewPhaseCount = 7;
	if (ReviewPhaseIndex >= ReviewPhaseCount)
	{
		if (!bLoopForReview)
		{
			ReviewPhaseIndex = ReviewPhaseCount - 1;
			StopReviewPhaseSequence();
			ApplyReviewPhase(ReviewPhaseIndex);
			return;
		}

		ResetEncounter();
		ReviewPhaseIndex = 0;
		bAutoAdvanceReviewPhases = true;
	}

	ApplyReviewPhase(ReviewPhaseIndex);
}

void AAETGnomeOgreBattlefieldEncounterActor::ResetEncounter()
{
	PylonOverloadPercent = 0.0f;
	ShieldImpactLocationNormalized = 0.0f;
	if (ShieldwallActor != nullptr)
	{
		ShieldwallActor->SetOverloadPercent(0.0f);
		ShieldwallActor->SetImpactIntensity(0.0f);
		ShieldwallActor->SetImpactLocationNormalized(0.0f);
		ShieldwallActor->SetShieldState(EAETShieldwallState::Braced);
	}
	if (AAETCrudeTekPylonActor* PylonActor = Cast<AAETCrudeTekPylonActor>(PylonObjectiveActor.Get()))
	{
		PylonActor->ResetPylon();
	}
	if (AAETManticoreInterruptActor* InterruptActor = Cast<AAETManticoreInterruptActor>(ManticoreInterruptActor.Get()))
	{
		InterruptActor->ResetInterrupt();
	}
	SetOptionalActorEnabled(PylonObjectiveActor, bEnablePylonObjective);
	SetOptionalActorEnabled(OgreShamanActor, bEnableCasterReinforcements);
	SetOptionalActorEnabled(OgreNecromancerActor, bEnableCasterReinforcements);
	SetOptionalActorEnabled(ManticoreInterruptActor, bEnableManticoreInterrupt);
	SetEncounterState(EAETGnomeOgreEncounterState::Setup);
}

void AAETGnomeOgreBattlefieldEncounterActor::ApplyReviewPhase(int32 PhaseIndex)
{
	switch (PhaseIndex)
	{
	case 0:
		SetEncounterState(EAETGnomeOgreEncounterState::GnomeHoldLine);
		break;
	case 1:
		SetEncounterState(EAETGnomeOgreEncounterState::OgreAdvance);
		break;
	case 2:
		TriggerShieldImpact(0.15f, 0.75f);
		break;
	case 3:
		TriggerPylonOverload(0.78f);
		break;
	case 4:
		TriggerCasterReinforcement(OgreShamanActor != nullptr ? OgreShamanActor.Get() : OgreNecromancerActor.Get());
		break;
	case 5:
		TriggerManticoreInterrupt(ManticoreInterruptActor.Get());
		break;
	case 6:
	default:
		SetEncounterState(EAETGnomeOgreEncounterState::Resolution);
		break;
	}
}

void AAETGnomeOgreBattlefieldEncounterActor::ConfigureTrigger(UBoxComponent* TriggerComponent, const FVector& RelativeLocation, const FVector& Extent) const
{
	if (TriggerComponent == nullptr)
	{
		return;
	}
	TriggerComponent->SetRelativeLocation(RelativeLocation);
	TriggerComponent->SetBoxExtent(Extent);
	TriggerComponent->SetVisibility(false, true);
	TriggerComponent->SetHiddenInGame(true, true);
}

void AAETGnomeOgreBattlefieldEncounterActor::UpdateEncounterLayout()
{
	const float HalfDepth = EncounterDepthCm * 0.5f;
	const float HalfWidth = EncounterWidthCm * 0.5f;

	if (EncounterBounds != nullptr)
	{
		EncounterBounds->SetBoxExtent(FVector(HalfDepth, HalfWidth, 260.0f));
		EncounterBounds->SetRelativeLocation(FVector(0.0f, 0.0f, 130.0f));
	}

	if (GnomeLineMarker != nullptr)
	{
		GnomeLineMarker->SetRelativeLocation(FVector(-HalfDepth * 0.36f, 0.0f, 0.0f));
	}
	if (OgreLineMarker != nullptr)
	{
		OgreLineMarker->SetRelativeLocation(FVector(HalfDepth * 0.22f, 0.0f, 0.0f));
	}
	if (GateMarker != nullptr)
	{
		GateMarker->SetRelativeLocation(FVector(HalfDepth * 0.46f, 0.0f, 0.0f));
	}
	if (PylonMarker != nullptr)
	{
		PylonMarker->SetRelativeLocation(FVector(HalfDepth * 0.34f, -HalfWidth * 0.28f, 0.0f));
	}
	if (ManticoreEntryMarker != nullptr)
	{
		ManticoreEntryMarker->SetRelativeLocation(FVector(0.0f, HalfWidth * 0.56f, 0.0f));
	}

	ConfigureTrigger(ShieldwallTrigger, FVector(-HalfDepth * 0.25f, 0.0f, 120.0f), FVector(180.0f, HalfWidth * 0.42f, 140.0f));
	ConfigureTrigger(PylonTrigger, FVector(HalfDepth * 0.30f, -HalfWidth * 0.26f, 150.0f), FVector(220.0f, 220.0f, 180.0f));
	ConfigureTrigger(ManticoreTrigger, FVector(0.0f, HalfWidth * 0.50f, 180.0f), FVector(HalfDepth * 0.38f, 220.0f, 220.0f));
}

void AAETGnomeOgreBattlefieldEncounterActor::ApplyEncounterState()
{
	AAETCrudeTekPylonActor* PylonActor = Cast<AAETCrudeTekPylonActor>(PylonObjectiveActor.Get());
	AAETManticoreInterruptActor* InterruptActor = Cast<AAETManticoreInterruptActor>(ManticoreInterruptActor.Get());

	if (ShieldwallActor != nullptr)
	{
		switch (EncounterState)
		{
		case EAETGnomeOgreEncounterState::Setup:
			ShieldwallActor->SetShieldState(EAETShieldwallState::Braced);
			break;
		case EAETGnomeOgreEncounterState::GnomeHoldLine:
			ShieldwallActor->SetShieldState(EAETShieldwallState::Braced);
			break;
		case EAETGnomeOgreEncounterState::ShieldImpact:
			ShieldwallActor->TriggerImpact(ShieldImpactLocationNormalized, 0.65f);
			break;
		case EAETGnomeOgreEncounterState::PylonOverload:
			ShieldwallActor->SetOverloadPercent(PylonOverloadPercent);
			ShieldwallActor->SetShieldState(EAETShieldwallState::Overload);
			break;
		case EAETGnomeOgreEncounterState::Resolution:
			ShieldwallActor->SetShieldState(bLoopForReview ? EAETShieldwallState::Braced : EAETShieldwallState::Shutdown);
			break;
		case EAETGnomeOgreEncounterState::OgreAdvance:
		case EAETGnomeOgreEncounterState::CasterReinforcement:
		case EAETGnomeOgreEncounterState::ManticoreInterrupt:
		default:
			break;
		}
	}

	if (PylonActor != nullptr)
	{
		switch (EncounterState)
		{
		case EAETGnomeOgreEncounterState::Setup:
		case EAETGnomeOgreEncounterState::GnomeHoldLine:
			PylonActor->SetPylonState(EAETCrudeTekPylonState::Idle);
			PylonActor->SetOverloadPercent(0.0f);
			break;
		case EAETGnomeOgreEncounterState::OgreAdvance:
		case EAETGnomeOgreEncounterState::CasterReinforcement:
			PylonActor->SetPylonState(EAETCrudeTekPylonState::Charged);
			PylonActor->SetOverloadPercent(FMath::Max(PylonOverloadPercent, 0.35f));
			break;
		case EAETGnomeOgreEncounterState::PylonOverload:
			PylonActor->TriggerOverload(PylonOverloadPercent);
			break;
		case EAETGnomeOgreEncounterState::Resolution:
			PylonActor->SetPylonState(EAETCrudeTekPylonState::Damaged);
			PylonActor->SetDamagePercent(0.45f);
			break;
		case EAETGnomeOgreEncounterState::ShieldImpact:
		case EAETGnomeOgreEncounterState::ManticoreInterrupt:
		default:
			break;
		}
	}

	if (InterruptActor != nullptr)
	{
		switch (EncounterState)
		{
		case EAETGnomeOgreEncounterState::Setup:
		case EAETGnomeOgreEncounterState::GnomeHoldLine:
			InterruptActor->ResetInterrupt();
			break;
		case EAETGnomeOgreEncounterState::OgreAdvance:
		case EAETGnomeOgreEncounterState::CasterReinforcement:
			InterruptActor->SetInterruptState(EAETManticoreInterruptState::Stalking);
			InterruptActor->SetSequenceProgress(0.25f);
			break;
		case EAETGnomeOgreEncounterState::ManticoreInterrupt:
			InterruptActor->TriggerInterrupt();
			break;
		case EAETGnomeOgreEncounterState::Resolution:
			InterruptActor->SetInterruptState(EAETManticoreInterruptState::Retreat);
			InterruptActor->SetSequenceProgress(0.8f);
			break;
		case EAETGnomeOgreEncounterState::ShieldImpact:
		case EAETGnomeOgreEncounterState::PylonOverload:
		default:
			break;
		}
	}

	SetOptionalActorEnabled(PylonObjectiveActor, bEnablePylonObjective);
	SetOptionalActorEnabled(OgreShamanActor, bEnableCasterReinforcements);
	SetOptionalActorEnabled(OgreNecromancerActor, bEnableCasterReinforcements);
	SetOptionalActorEnabled(ManticoreInterruptActor, bEnableManticoreInterrupt);
}

void AAETGnomeOgreBattlefieldEncounterActor::SetOptionalActorEnabled(AActor* Actor, bool bEnabled) const
{
	if (Actor == nullptr)
	{
		return;
	}
	Actor->SetActorHiddenInGame(!bEnabled);
	Actor->SetActorEnableCollision(bEnabled);
	Actor->SetActorTickEnabled(bEnabled);
}
