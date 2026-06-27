#pragma once

#include "CoreMinimal.h"
#include "GameFramework/Actor.h"
#include "AETManticoreInterruptActor.generated.h"

class UNiagaraComponent;
class UNiagaraSystem;
class USceneComponent;
class USkeletalMesh;
class USkeletalMeshComponent;

UENUM(BlueprintType)
enum class EAETManticoreInterruptState : uint8
{
	Hidden UMETA(DisplayName = "Hidden"),
	Stalking UMETA(DisplayName = "Stalking"),
	Telegraph UMETA(DisplayName = "Telegraph"),
	LeapImpact UMETA(DisplayName = "Leap Impact"),
	ThreatHold UMETA(DisplayName = "Threat Hold"),
	Retreat UMETA(DisplayName = "Retreat")
};

UCLASS(Blueprintable)
class AERATHEA_API AAETManticoreInterruptActor : public AActor
{
	GENERATED_BODY()

public:
	AAETManticoreInterruptActor();

	virtual void OnConstruction(const FTransform& Transform) override;

	UPROPERTY(VisibleAnywhere, BlueprintReadOnly, Category = "Aerathea|Manticore Interrupt")
	TObjectPtr<USceneComponent> SceneRoot;

	UPROPERTY(VisibleAnywhere, BlueprintReadOnly, Category = "Aerathea|Manticore Interrupt")
	TObjectPtr<USkeletalMeshComponent> ManticoreMesh;

	UPROPERTY(VisibleAnywhere, BlueprintReadOnly, Category = "Aerathea|Manticore Interrupt|Markers")
	TObjectPtr<USceneComponent> EntryMarker;

	UPROPERTY(VisibleAnywhere, BlueprintReadOnly, Category = "Aerathea|Manticore Interrupt|Markers")
	TObjectPtr<USceneComponent> ImpactMarker;

	UPROPERTY(VisibleAnywhere, BlueprintReadOnly, Category = "Aerathea|Manticore Interrupt|Markers")
	TObjectPtr<USceneComponent> RetreatMarker;

	UPROPERTY(VisibleAnywhere, BlueprintReadOnly, Category = "Aerathea|Manticore Interrupt|VFX")
	TObjectPtr<UNiagaraComponent> ImpactNiagara;

	UPROPERTY(EditAnywhere, BlueprintReadWrite, Category = "Aerathea|Manticore Interrupt")
	EAETManticoreInterruptState InterruptState;

	UPROPERTY(EditAnywhere, BlueprintReadWrite, Category = "Aerathea|Manticore Interrupt", meta = (ClampMin = "0.0", ClampMax = "1.0"))
	float SequenceProgress;

	UPROPERTY(EditAnywhere, BlueprintReadWrite, Category = "Aerathea|Manticore Interrupt")
	bool bVisibleDuringSetup;

	UPROPERTY(EditAnywhere, BlueprintReadWrite, Category = "Aerathea|Manticore Interrupt|Layout")
	FVector EntryOffset;

	UPROPERTY(EditAnywhere, BlueprintReadWrite, Category = "Aerathea|Manticore Interrupt|Layout")
	FVector ImpactOffset;

	UPROPERTY(EditAnywhere, BlueprintReadWrite, Category = "Aerathea|Manticore Interrupt|Layout")
	FVector RetreatOffset;

	UPROPERTY(EditAnywhere, BlueprintReadWrite, Category = "Aerathea|Manticore Interrupt|Assets")
	TObjectPtr<USkeletalMesh> ManticoreSkeletalMesh;

	UPROPERTY(EditAnywhere, BlueprintReadWrite, Category = "Aerathea|Manticore Interrupt|VFX")
	TObjectPtr<UNiagaraSystem> ImpactNiagaraSystem;

	UPROPERTY(EditAnywhere, BlueprintReadWrite, Category = "Aerathea|Manticore Interrupt|VFX")
	bool bUseNiagara;

	UFUNCTION(BlueprintCallable, Category = "Aerathea|Manticore Interrupt")
	void SetInterruptState(EAETManticoreInterruptState NewState);

	UFUNCTION(BlueprintCallable, Category = "Aerathea|Manticore Interrupt")
	void SetSequenceProgress(float NewSequenceProgress);

	UFUNCTION(BlueprintCallable, Category = "Aerathea|Manticore Interrupt")
	void TriggerInterrupt();

	UFUNCTION(BlueprintCallable, Category = "Aerathea|Manticore Interrupt")
	void ResetInterrupt();

	UFUNCTION(BlueprintCallable, Category = "Aerathea|Manticore Interrupt")
	void ConfigureInterruptOffsets(FVector NewEntryOffset, FVector NewImpactOffset, FVector NewRetreatOffset);

protected:
	void AssignDefaultAssets();
	void UpdateInterruptLayout();
	void ApplyInterruptState();
};
