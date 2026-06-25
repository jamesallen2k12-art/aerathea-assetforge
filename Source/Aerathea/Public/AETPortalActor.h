#pragma once

#include "CoreMinimal.h"
#include "GameFramework/Actor.h"
#include "AETPortalActor.generated.h"

class UBoxComponent;
class UStaticMeshComponent;

UENUM(BlueprintType)
enum class EAETPortalState : uint8
{
	Inactive UMETA(DisplayName = "Inactive"),
	Idle UMETA(DisplayName = "Idle"),
	Charging UMETA(DisplayName = "Charging"),
	Ready UMETA(DisplayName = "Ready"),
	Locked UMETA(DisplayName = "Locked")
};

UCLASS(Blueprintable)
class AERATHEA_API AAETPortalActor : public AActor
{
	GENERATED_BODY()

public:
	AAETPortalActor();

	virtual void OnConstruction(const FTransform& Transform) override;

	UPROPERTY(VisibleAnywhere, BlueprintReadOnly, Category = "Aerathea|Portal")
	TObjectPtr<USceneComponent> SceneRoot;

	UPROPERTY(VisibleAnywhere, BlueprintReadOnly, Category = "Aerathea|Portal")
	TObjectPtr<UStaticMeshComponent> PortalArchMesh;

	UPROPERTY(VisibleAnywhere, BlueprintReadOnly, Category = "Aerathea|Portal")
	TObjectPtr<UStaticMeshComponent> PortalCoreMesh;

	UPROPERTY(VisibleAnywhere, BlueprintReadOnly, Category = "Aerathea|Portal")
	TObjectPtr<UBoxComponent> InteractionVolume;

	UPROPERTY(EditAnywhere, BlueprintReadWrite, Category = "Aerathea|Portal")
	EAETPortalState PortalState;

	UPROPERTY(EditAnywhere, BlueprintReadWrite, Category = "Aerathea|Portal")
	FName DestinationId;

	UPROPERTY(EditAnywhere, BlueprintReadWrite, Category = "Aerathea|Portal")
	bool bServerAuthoritativeUse;

	UFUNCTION(BlueprintCallable, Category = "Aerathea|Portal")
	void SetPortalState(EAETPortalState NewState);

	UFUNCTION(BlueprintPure, Category = "Aerathea|Portal")
	bool CanInteract() const;

	UFUNCTION(BlueprintCallable, Category = "Aerathea|Portal")
	bool RequestPortalUse(AActor* InteractingActor);

	UFUNCTION(BlueprintImplementableEvent, Category = "Aerathea|Portal")
	void OnPortalStateChanged(EAETPortalState NewState);

	UFUNCTION(BlueprintImplementableEvent, Category = "Aerathea|Portal")
	void OnPortalUseRequested(AActor* InteractingActor);

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
};
