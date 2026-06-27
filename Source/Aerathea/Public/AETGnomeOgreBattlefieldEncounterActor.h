#pragma once

#include "CoreMinimal.h"
#include "GameFramework/Actor.h"
#include "AETGnomeOgreBattlefieldEncounterActor.generated.h"

class AAETHeavyMekShieldwallActor;
class UBoxComponent;
class USceneComponent;

UENUM(BlueprintType)
enum class EAETGnomeOgreEncounterState : uint8
{
	Setup UMETA(DisplayName = "Setup"),
	GnomeHoldLine UMETA(DisplayName = "Gnome Hold Line"),
	OgreAdvance UMETA(DisplayName = "Ogre Advance"),
	ShieldImpact UMETA(DisplayName = "Shield Impact"),
	PylonOverload UMETA(DisplayName = "Pylon Overload"),
	CasterReinforcement UMETA(DisplayName = "Caster Reinforcement"),
	ManticoreInterrupt UMETA(DisplayName = "Manticore Interrupt"),
	Resolution UMETA(DisplayName = "Resolution")
};

DECLARE_DYNAMIC_MULTICAST_DELEGATE_OneParam(FAETEncounterPhaseChangedSignature, EAETGnomeOgreEncounterState, NewState);
DECLARE_DYNAMIC_MULTICAST_DELEGATE_OneParam(FAETEncounterValidationSignature, const FString&, ValidationReport);
DECLARE_DYNAMIC_MULTICAST_DELEGATE_OneParam(FAETEncounterActorEventSignature, AActor*, EventActor);
DECLARE_DYNAMIC_MULTICAST_DELEGATE_OneParam(FAETEncounterFloatEventSignature, float, Value);

UCLASS(Blueprintable)
class AERATHEA_API AAETGnomeOgreBattlefieldEncounterActor : public AActor
{
	GENERATED_BODY()

public:
	AAETGnomeOgreBattlefieldEncounterActor();

	virtual void OnConstruction(const FTransform& Transform) override;
	virtual void BeginPlay() override;
	virtual void Tick(float DeltaSeconds) override;

	UPROPERTY(VisibleAnywhere, BlueprintReadOnly, Category = "Aerathea|Gnome Ogre Encounter")
	TObjectPtr<USceneComponent> SceneRoot;

	UPROPERTY(VisibleAnywhere, BlueprintReadOnly, Category = "Aerathea|Gnome Ogre Encounter")
	TObjectPtr<UBoxComponent> EncounterBounds;

	UPROPERTY(VisibleAnywhere, BlueprintReadOnly, Category = "Aerathea|Gnome Ogre Encounter|Markers")
	TObjectPtr<USceneComponent> GnomeLineMarker;

	UPROPERTY(VisibleAnywhere, BlueprintReadOnly, Category = "Aerathea|Gnome Ogre Encounter|Markers")
	TObjectPtr<USceneComponent> OgreLineMarker;

	UPROPERTY(VisibleAnywhere, BlueprintReadOnly, Category = "Aerathea|Gnome Ogre Encounter|Markers")
	TObjectPtr<USceneComponent> GateMarker;

	UPROPERTY(VisibleAnywhere, BlueprintReadOnly, Category = "Aerathea|Gnome Ogre Encounter|Markers")
	TObjectPtr<USceneComponent> PylonMarker;

	UPROPERTY(VisibleAnywhere, BlueprintReadOnly, Category = "Aerathea|Gnome Ogre Encounter|Markers")
	TObjectPtr<USceneComponent> ManticoreEntryMarker;

	UPROPERTY(VisibleAnywhere, BlueprintReadOnly, Category = "Aerathea|Gnome Ogre Encounter|Triggers")
	TObjectPtr<UBoxComponent> ShieldwallTrigger;

	UPROPERTY(VisibleAnywhere, BlueprintReadOnly, Category = "Aerathea|Gnome Ogre Encounter|Triggers")
	TObjectPtr<UBoxComponent> PylonTrigger;

	UPROPERTY(VisibleAnywhere, BlueprintReadOnly, Category = "Aerathea|Gnome Ogre Encounter|Triggers")
	TObjectPtr<UBoxComponent> ManticoreTrigger;

	UPROPERTY(EditAnywhere, BlueprintReadWrite, Category = "Aerathea|Gnome Ogre Encounter")
	EAETGnomeOgreEncounterState EncounterState;

	UPROPERTY(EditAnywhere, BlueprintReadWrite, Category = "Aerathea|Gnome Ogre Encounter")
	bool bAutoStart;

	UPROPERTY(EditAnywhere, BlueprintReadWrite, Category = "Aerathea|Gnome Ogre Encounter")
	bool bUsePlacedActors;

	UPROPERTY(EditAnywhere, BlueprintReadWrite, Category = "Aerathea|Gnome Ogre Encounter")
	bool bEnablePylonObjective;

	UPROPERTY(EditAnywhere, BlueprintReadWrite, Category = "Aerathea|Gnome Ogre Encounter")
	bool bEnableCasterReinforcements;

	UPROPERTY(EditAnywhere, BlueprintReadWrite, Category = "Aerathea|Gnome Ogre Encounter")
	bool bEnableManticoreInterrupt;

	UPROPERTY(EditAnywhere, BlueprintReadWrite, Category = "Aerathea|Gnome Ogre Encounter")
	bool bLoopForReview;

	UPROPERTY(EditAnywhere, BlueprintReadWrite, Category = "Aerathea|Gnome Ogre Encounter|Review")
	bool bAutoAdvanceReviewPhases;

	UPROPERTY(EditAnywhere, BlueprintReadWrite, Category = "Aerathea|Gnome Ogre Encounter|Review", meta = (ClampMin = "0.25", ClampMax = "30.0"))
	float ReviewPhaseDurationSeconds;

	UPROPERTY(VisibleInstanceOnly, BlueprintReadOnly, Category = "Aerathea|Gnome Ogre Encounter|Review")
	float ReviewPhaseElapsedSeconds;

	UPROPERTY(VisibleInstanceOnly, BlueprintReadOnly, Category = "Aerathea|Gnome Ogre Encounter|Review")
	int32 ReviewPhaseIndex;

	UPROPERTY(EditAnywhere, BlueprintReadWrite, Category = "Aerathea|Gnome Ogre Encounter", meta = (ClampMin = "1200.0", ClampMax = "6000.0"))
	float EncounterWidthCm;

	UPROPERTY(EditAnywhere, BlueprintReadWrite, Category = "Aerathea|Gnome Ogre Encounter", meta = (ClampMin = "1200.0", ClampMax = "6000.0"))
	float EncounterDepthCm;

	UPROPERTY(EditAnywhere, BlueprintReadWrite, Category = "Aerathea|Gnome Ogre Encounter|VFX", meta = (ClampMin = "-1.0", ClampMax = "1.0"))
	float ShieldImpactLocationNormalized;

	UPROPERTY(EditAnywhere, BlueprintReadWrite, Category = "Aerathea|Gnome Ogre Encounter|VFX", meta = (ClampMin = "0.0", ClampMax = "1.0"))
	float PylonOverloadPercent;

	UPROPERTY(EditAnywhere, BlueprintReadWrite, Category = "Aerathea|Gnome Ogre Encounter|Actors")
	TObjectPtr<AAETHeavyMekShieldwallActor> ShieldwallActor;

	UPROPERTY(EditAnywhere, BlueprintReadWrite, Category = "Aerathea|Gnome Ogre Encounter|Actors")
	TObjectPtr<AActor> GnomeHeavyMekActor;

	UPROPERTY(EditAnywhere, BlueprintReadWrite, Category = "Aerathea|Gnome Ogre Encounter|Actors")
	TObjectPtr<AActor> OgreTeknomancerActor;

	UPROPERTY(EditAnywhere, BlueprintReadWrite, Category = "Aerathea|Gnome Ogre Encounter|Actors")
	TObjectPtr<AActor> OgreWarriorActor;

	UPROPERTY(EditAnywhere, BlueprintReadWrite, Category = "Aerathea|Gnome Ogre Encounter|Actors")
	TObjectPtr<AActor> CairnGateActor;

	UPROPERTY(EditAnywhere, BlueprintReadWrite, Category = "Aerathea|Gnome Ogre Encounter|Actors")
	TObjectPtr<AActor> PylonObjectiveActor;

	UPROPERTY(EditAnywhere, BlueprintReadWrite, Category = "Aerathea|Gnome Ogre Encounter|Actors")
	TObjectPtr<AActor> OgreShamanActor;

	UPROPERTY(EditAnywhere, BlueprintReadWrite, Category = "Aerathea|Gnome Ogre Encounter|Actors")
	TObjectPtr<AActor> OgreNecromancerActor;

	UPROPERTY(EditAnywhere, BlueprintReadWrite, Category = "Aerathea|Gnome Ogre Encounter|Actors")
	TObjectPtr<AActor> ManticoreInterruptActor;

	UPROPERTY(VisibleInstanceOnly, BlueprintReadOnly, Category = "Aerathea|Gnome Ogre Encounter|Validation")
	FString LastValidationReport;

	UPROPERTY(BlueprintAssignable, Category = "Aerathea|Gnome Ogre Encounter|Events")
	FAETEncounterPhaseChangedSignature OnEncounterPhaseChanged;

	UPROPERTY(BlueprintAssignable, Category = "Aerathea|Gnome Ogre Encounter|Events")
	FAETEncounterValidationSignature OnEncounterValidationFailed;

	UPROPERTY(BlueprintAssignable, Category = "Aerathea|Gnome Ogre Encounter|Events")
	FAETEncounterFloatEventSignature OnPylonOverloadTriggered;

	UPROPERTY(BlueprintAssignable, Category = "Aerathea|Gnome Ogre Encounter|Events")
	FAETEncounterActorEventSignature OnCasterReinforcementTriggered;

	UPROPERTY(BlueprintAssignable, Category = "Aerathea|Gnome Ogre Encounter|Events")
	FAETEncounterActorEventSignature OnManticoreInterruptTriggered;

	UFUNCTION(BlueprintCallable, Category = "Aerathea|Gnome Ogre Encounter")
	bool ValidateDependencies();

	UFUNCTION(BlueprintCallable, Category = "Aerathea|Gnome Ogre Encounter")
	void ConfigureEncounter(float NewEncounterWidthCm, float NewEncounterDepthCm, bool bNewEnablePylonObjective, bool bNewEnableCasterReinforcements, bool bNewEnableManticoreInterrupt);

	UFUNCTION(BlueprintCallable, Category = "Aerathea|Gnome Ogre Encounter")
	void SetEncounterState(EAETGnomeOgreEncounterState NewState);

	UFUNCTION(BlueprintCallable, Category = "Aerathea|Gnome Ogre Encounter")
	void TriggerShieldImpact(float NewImpactLocationNormalized, float NewImpactIntensity);

	UFUNCTION(BlueprintCallable, Category = "Aerathea|Gnome Ogre Encounter")
	void TriggerPylonOverload(float NewOverloadPercent);

	UFUNCTION(BlueprintCallable, Category = "Aerathea|Gnome Ogre Encounter")
	void TriggerCasterReinforcement(AActor* CasterActor);

	UFUNCTION(BlueprintCallable, Category = "Aerathea|Gnome Ogre Encounter")
	void TriggerManticoreInterrupt(AActor* ManticoreActor);

	UFUNCTION(BlueprintCallable, Category = "Aerathea|Gnome Ogre Encounter|Review")
	void StartReviewPhaseSequence();

	UFUNCTION(BlueprintCallable, Category = "Aerathea|Gnome Ogre Encounter|Review")
	void StopReviewPhaseSequence();

	UFUNCTION(BlueprintCallable, Category = "Aerathea|Gnome Ogre Encounter|Review")
	void AdvanceReviewPhase();

	UFUNCTION(BlueprintCallable, Category = "Aerathea|Gnome Ogre Encounter")
	void ResetEncounter();

protected:
	void ConfigureTrigger(UBoxComponent* TriggerComponent, const FVector& RelativeLocation, const FVector& Extent) const;
	void UpdateEncounterLayout();
	void ApplyEncounterState();
	void ApplyReviewPhase(int32 PhaseIndex);
	void SetOptionalActorEnabled(AActor* Actor, bool bEnabled) const;
};
