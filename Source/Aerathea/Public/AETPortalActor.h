#pragma once

#include "CoreMinimal.h"
#include "GameFramework/Actor.h"
#include "AETPortalActor.generated.h"

class UBoxComponent;
class UMaterialInstanceDynamic;
class UStaticMeshComponent;

UENUM(BlueprintType)
enum class EAETPortalState : uint8
{
	Inactive UMETA(DisplayName = "Inactive"),
	Idle UMETA(DisplayName = "Idle"),
	Focused UMETA(DisplayName = "Focused"),
	UseRequested UMETA(DisplayName = "Use Requested"),
	Cooldown UMETA(DisplayName = "Cooldown"),
	Charging UMETA(DisplayName = "Charging"),
	Ready UMETA(DisplayName = "Ready"),
	Locked UMETA(DisplayName = "Locked"),
	Blocked UMETA(DisplayName = "Blocked")
};

UCLASS(Blueprintable)
class AERATHEA_API AAETPortalActor : public AActor
{
	GENERATED_BODY()

public:
	AAETPortalActor();

	virtual void OnConstruction(const FTransform& Transform) override;
	virtual void BeginPlay() override;
	virtual void GetLifetimeReplicatedProps(TArray<FLifetimeProperty>& OutLifetimeProps) const override;

	UPROPERTY(VisibleAnywhere, BlueprintReadOnly, Category = "Aerathea|Portal")
	TObjectPtr<USceneComponent> SceneRoot;

	UPROPERTY(VisibleAnywhere, BlueprintReadOnly, Category = "Aerathea|Portal")
	TObjectPtr<UStaticMeshComponent> PortalArchMesh;

	UPROPERTY(VisibleAnywhere, BlueprintReadOnly, Category = "Aerathea|Portal")
	TObjectPtr<UStaticMeshComponent> PortalCoreMesh;

	UPROPERTY(VisibleAnywhere, BlueprintReadOnly, Category = "Aerathea|Portal")
	TObjectPtr<UBoxComponent> InteractionVolume;

	UPROPERTY(EditAnywhere, BlueprintReadWrite, Category = "Aerathea|Portal")
	bool bPortalActive;

	UPROPERTY(EditAnywhere, BlueprintReadWrite, Category = "Aerathea|Portal")
	FName PortalId;

	UPROPERTY(EditAnywhere, BlueprintReadWrite, Replicated, Category = "Aerathea|Portal")
	EAETPortalState PortalState;

	UPROPERTY(EditAnywhere, BlueprintReadWrite, Replicated, Category = "Aerathea|Portal")
	FName DestinationId;

	UPROPERTY(EditAnywhere, BlueprintReadWrite, Category = "Aerathea|Portal")
	bool bServerAuthoritativeUse;

	UPROPERTY(EditAnywhere, BlueprintReadWrite, Category = "Aerathea|Portal")
	bool bAllowClientPreviewOnly;

	UPROPERTY(EditAnywhere, BlueprintReadWrite, Category = "Aerathea|Portal|Interaction", meta = (ClampMin = "0.0"))
	float UsePreviewDurationSeconds;

	UPROPERTY(EditAnywhere, BlueprintReadWrite, Category = "Aerathea|Portal|Interaction", meta = (ClampMin = "0.0"))
	float UseCooldownSeconds;

	UPROPERTY(EditAnywhere, BlueprintReadWrite, Category = "Aerathea|Portal|Interaction")
	FVector InteractionBoxExtent;

	UPROPERTY(EditAnywhere, BlueprintReadWrite, Category = "Aerathea|Portal|Debug")
	bool bDebugPortalLogs;

	UFUNCTION(BlueprintCallable, Category = "Aerathea|Portal")
	void SetPortalState(EAETPortalState NewState);

	UFUNCTION(BlueprintPure, Category = "Aerathea|Portal")
	bool CanInteract() const;

	UFUNCTION(BlueprintCallable, Category = "Aerathea|Portal")
	bool RequestPortalUse(AActor* InteractingActor);

	UFUNCTION(BlueprintCallable, Category = "Aerathea|Portal")
	void SetPortalActive(bool bNewPortalActive);

	UFUNCTION(BlueprintPure, Category = "Aerathea|Portal")
	bool HasValidDestination() const;

	UFUNCTION(BlueprintImplementableEvent, Category = "Aerathea|Portal")
	void OnPortalStateChanged(EAETPortalState NewState);

	UFUNCTION(BlueprintImplementableEvent, Category = "Aerathea|Portal")
	void OnPortalUseRequested(AActor* InteractingActor);

	UFUNCTION(BlueprintImplementableEvent, Category = "Aerathea|Portal")
	void OnPortalFocusChanged(AActor* FocusedActor, bool bIsFocused);

	UFUNCTION(BlueprintImplementableEvent, Category = "Aerathea|Portal")
	void OnPortalUseRejected(AActor* InteractingActor, FName Reason);

protected:
	UFUNCTION()
	void HandleInteractionBeginOverlap(
		UPrimitiveComponent* OverlappedComponent,
		AActor* OtherActor,
		UPrimitiveComponent* OtherComp,
		int32 OtherBodyIndex,
		bool bFromSweep,
		const FHitResult& SweepResult
	);

	UFUNCTION()
	void HandleInteractionEndOverlap(
		UPrimitiveComponent* OverlappedComponent,
		AActor* OtherActor,
		UPrimitiveComponent* OtherComp,
		int32 OtherBodyIndex
	);

	UPROPERTY(VisibleInstanceOnly, BlueprintReadOnly, Category = "Aerathea|Portal")
	TObjectPtr<AActor> LastOverlappingActor;

	UPROPERTY(Transient, VisibleInstanceOnly, BlueprintReadOnly, Category = "Aerathea|Portal")
	TObjectPtr<UMaterialInstanceDynamic> PortalCoreMaterialInstance;

	FTimerHandle UsePreviewTimerHandle;
	FTimerHandle CooldownTimerHandle;

	void EnterUseCooldown();
	void ReturnToSafeState();
	void ApplyPortalVisualState();
	bool IsValidFocusedActor(AActor* Actor) const;
	void RejectPortalUse(AActor* InteractingActor, FName Reason);
};
