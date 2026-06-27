#pragma once

#include "CoreMinimal.h"
#include "GameFramework/Actor.h"
#include "AETTargetDummyActor.generated.h"

class UBoxComponent;
class UStaticMeshComponent;

UCLASS(Blueprintable)
class AERATHEA_API AAETTargetDummyActor : public AActor
{
	GENERATED_BODY()

public:
	AAETTargetDummyActor();

	virtual void OnConstruction(const FTransform& Transform) override;
	virtual void BeginPlay() override;
	virtual float TakeDamage(
		float DamageAmount,
		struct FDamageEvent const& DamageEvent,
		class AController* EventInstigator,
		AActor* DamageCauser
	) override;

	UPROPERTY(VisibleAnywhere, BlueprintReadOnly, Category = "Aerathea|Target Dummy")
	TObjectPtr<USceneComponent> SceneRoot;

	UPROPERTY(VisibleAnywhere, BlueprintReadOnly, Category = "Aerathea|Target Dummy")
	TObjectPtr<UStaticMeshComponent> DummyMesh;

	UPROPERTY(VisibleAnywhere, BlueprintReadOnly, Category = "Aerathea|Target Dummy")
	TObjectPtr<UBoxComponent> HitVolume;

	UPROPERTY(EditAnywhere, BlueprintReadWrite, Category = "Aerathea|Target Dummy", meta = (ClampMin = "1.0"))
	float MaxTrainingHealth;

	UPROPERTY(VisibleInstanceOnly, BlueprintReadOnly, Category = "Aerathea|Target Dummy")
	float CurrentTrainingHealth;

	UPROPERTY(EditAnywhere, BlueprintReadWrite, Category = "Aerathea|Target Dummy", meta = (ClampMin = "0.0"))
	float HitReactionDurationSeconds;

	UPROPERTY(EditAnywhere, BlueprintReadWrite, Category = "Aerathea|Target Dummy", meta = (ClampMin = "0.0"))
	float ResetDelaySeconds;

	UPROPERTY(EditAnywhere, BlueprintReadWrite, Category = "Aerathea|Target Dummy")
	bool bAutoResetAfterBreak;

	UPROPERTY(EditAnywhere, BlueprintReadWrite, Category = "Aerathea|Target Dummy")
	bool bDebugHitLogs;

	UFUNCTION(BlueprintCallable, Category = "Aerathea|Target Dummy")
	float RegisterTrainingHit(float DamageAmount, AActor* DamageCauser, FName HitZone = NAME_None);

	UFUNCTION(BlueprintCallable, Category = "Aerathea|Target Dummy")
	void ResetTrainingHealth();

	UFUNCTION(BlueprintPure, Category = "Aerathea|Target Dummy")
	bool CanReceiveTrainingHit() const;

	UFUNCTION(BlueprintImplementableEvent, Category = "Aerathea|Target Dummy")
	void OnTrainingHit(float DamageAmount, float ScoreValue, AActor* DamageCauser, FName HitZone);

	UFUNCTION(BlueprintImplementableEvent, Category = "Aerathea|Target Dummy")
	void OnTrainingBroken(AActor* DamageCauser);

	UFUNCTION(BlueprintImplementableEvent, Category = "Aerathea|Target Dummy")
	void OnTrainingReset();

	UFUNCTION(BlueprintImplementableEvent, Category = "Aerathea|Target Dummy")
	void OnHitReactionStateChanged(bool bIsReacting);

protected:
	FTimerHandle HitReactionTimerHandle;
	FTimerHandle ResetTimerHandle;

	void EndHitReaction();
	void BreakTrainingDummy(AActor* DamageCauser);
};
