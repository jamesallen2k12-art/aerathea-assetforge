#pragma once

#include "CoreMinimal.h"
#include "GameFramework/Actor.h"
#include "AETCrudeTekPylonActor.generated.h"

class UNiagaraComponent;
class UNiagaraSystem;
class USceneComponent;
class UStaticMesh;
class UStaticMeshComponent;

UENUM(BlueprintType)
enum class EAETCrudeTekPylonState : uint8
{
	Idle UMETA(DisplayName = "Idle"),
	Charged UMETA(DisplayName = "Charged"),
	Overload UMETA(DisplayName = "Overload"),
	Damaged UMETA(DisplayName = "Damaged"),
	Destroyed UMETA(DisplayName = "Destroyed")
};

UCLASS(Blueprintable)
class AERATHEA_API AAETCrudeTekPylonActor : public AActor
{
	GENERATED_BODY()

public:
	AAETCrudeTekPylonActor();

	virtual void OnConstruction(const FTransform& Transform) override;

	UPROPERTY(VisibleAnywhere, BlueprintReadOnly, Category = "Aerathea|Ogre Tek Pylon")
	TObjectPtr<USceneComponent> SceneRoot;

	UPROPERTY(VisibleAnywhere, BlueprintReadOnly, Category = "Aerathea|Ogre Tek Pylon")
	TObjectPtr<UStaticMeshComponent> PylonMesh;

	UPROPERTY(VisibleAnywhere, BlueprintReadOnly, Category = "Aerathea|Ogre Tek Pylon|Markers")
	TObjectPtr<USceneComponent> CoreLocator;

	UPROPERTY(VisibleAnywhere, BlueprintReadOnly, Category = "Aerathea|Ogre Tek Pylon|Markers")
	TObjectPtr<USceneComponent> TopArcLocator;

	UPROPERTY(VisibleAnywhere, BlueprintReadOnly, Category = "Aerathea|Ogre Tek Pylon|Markers")
	TObjectPtr<USceneComponent> GroundSparksLocator;

	UPROPERTY(VisibleAnywhere, BlueprintReadOnly, Category = "Aerathea|Ogre Tek Pylon|VFX")
	TObjectPtr<UNiagaraComponent> PylonNiagara;

	UPROPERTY(EditAnywhere, BlueprintReadWrite, Category = "Aerathea|Ogre Tek Pylon")
	EAETCrudeTekPylonState PylonState;

	UPROPERTY(EditAnywhere, BlueprintReadWrite, Category = "Aerathea|Ogre Tek Pylon", meta = (ClampMin = "0.0", ClampMax = "1.0"))
	float OverloadPercent;

	UPROPERTY(EditAnywhere, BlueprintReadWrite, Category = "Aerathea|Ogre Tek Pylon", meta = (ClampMin = "0.0", ClampMax = "1.0"))
	float DamagePercent;

	UPROPERTY(EditAnywhere, BlueprintReadWrite, Category = "Aerathea|Ogre Tek Pylon")
	bool bPoweredVisible;

	UPROPERTY(EditAnywhere, BlueprintReadWrite, Category = "Aerathea|Ogre Tek Pylon|Assets")
	TObjectPtr<UStaticMesh> PylonStaticMesh;

	UPROPERTY(EditAnywhere, BlueprintReadWrite, Category = "Aerathea|Ogre Tek Pylon|VFX")
	TObjectPtr<UNiagaraSystem> PylonNiagaraSystem;

	UPROPERTY(EditAnywhere, BlueprintReadWrite, Category = "Aerathea|Ogre Tek Pylon|VFX")
	bool bUseNiagara;

	UFUNCTION(BlueprintCallable, Category = "Aerathea|Ogre Tek Pylon")
	void SetPylonState(EAETCrudeTekPylonState NewState);

	UFUNCTION(BlueprintCallable, Category = "Aerathea|Ogre Tek Pylon")
	void SetOverloadPercent(float NewOverloadPercent);

	UFUNCTION(BlueprintCallable, Category = "Aerathea|Ogre Tek Pylon")
	void SetDamagePercent(float NewDamagePercent);

	UFUNCTION(BlueprintCallable, Category = "Aerathea|Ogre Tek Pylon")
	void TriggerOverload(float NewOverloadPercent);

	UFUNCTION(BlueprintCallable, Category = "Aerathea|Ogre Tek Pylon")
	void ResetPylon();

protected:
	void AssignDefaultAssets();
	void UpdatePylonLayout();
	void ApplyPylonState();
};
