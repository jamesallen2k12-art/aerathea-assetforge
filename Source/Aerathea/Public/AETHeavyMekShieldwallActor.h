#pragma once

#include "CoreMinimal.h"
#include "GameFramework/Actor.h"
#include "AETHeavyMekShieldwallActor.generated.h"

class UAudioComponent;
class UBoxComponent;
class USceneComponent;
class USplineComponent;
class UStaticMeshComponent;

UENUM(BlueprintType)
enum class EAETShieldwallState : uint8
{
	Inactive UMETA(DisplayName = "Inactive"),
	Booting UMETA(DisplayName = "Booting"),
	Braced UMETA(DisplayName = "Braced"),
	Impact UMETA(DisplayName = "Impact"),
	Overload UMETA(DisplayName = "Overload"),
	Failing UMETA(DisplayName = "Failing"),
	Shutdown UMETA(DisplayName = "Shutdown")
};

UCLASS(Blueprintable)
class AERATHEA_API AAETHeavyMekShieldwallActor : public AActor
{
	GENERATED_BODY()

public:
	AAETHeavyMekShieldwallActor();

	virtual void OnConstruction(const FTransform& Transform) override;

	UPROPERTY(VisibleAnywhere, BlueprintReadOnly, Category = "Aerathea|Shieldwall")
	TObjectPtr<USceneComponent> SceneRoot;

	UPROPERTY(VisibleAnywhere, BlueprintReadOnly, Category = "Aerathea|Shieldwall")
	TObjectPtr<UStaticMeshComponent> Projector01;

	UPROPERTY(VisibleAnywhere, BlueprintReadOnly, Category = "Aerathea|Shieldwall")
	TObjectPtr<UStaticMeshComponent> Projector02;

	UPROPERTY(VisibleAnywhere, BlueprintReadOnly, Category = "Aerathea|Shieldwall")
	TObjectPtr<UStaticMeshComponent> Projector03;

	UPROPERTY(VisibleAnywhere, BlueprintReadOnly, Category = "Aerathea|Shieldwall")
	TObjectPtr<UStaticMeshComponent> Projector04;

	UPROPERTY(VisibleAnywhere, BlueprintReadOnly, Category = "Aerathea|Shieldwall")
	TObjectPtr<UStaticMeshComponent> Projector05;

	UPROPERTY(VisibleAnywhere, BlueprintReadOnly, Category = "Aerathea|Shieldwall")
	TObjectPtr<USplineComponent> ShieldSpline;

	UPROPERTY(VisibleAnywhere, BlueprintReadOnly, Category = "Aerathea|Shieldwall")
	TObjectPtr<UStaticMeshComponent> ShieldPanel01;

	UPROPERTY(VisibleAnywhere, BlueprintReadOnly, Category = "Aerathea|Shieldwall")
	TObjectPtr<UStaticMeshComponent> ShieldPanel02;

	UPROPERTY(VisibleAnywhere, BlueprintReadOnly, Category = "Aerathea|Shieldwall")
	TObjectPtr<UStaticMeshComponent> ShieldPanel03;

	UPROPERTY(VisibleAnywhere, BlueprintReadOnly, Category = "Aerathea|Shieldwall")
	TObjectPtr<UStaticMeshComponent> ShieldPanel04;

	UPROPERTY(VisibleAnywhere, BlueprintReadOnly, Category = "Aerathea|Shieldwall")
	TObjectPtr<UBoxComponent> ShieldCollision;

	UPROPERTY(VisibleAnywhere, BlueprintReadOnly, Category = "Aerathea|Shieldwall")
	TObjectPtr<USceneComponent> ImpactLocator;

	UPROPERTY(VisibleAnywhere, BlueprintReadOnly, Category = "Aerathea|Shieldwall")
	TObjectPtr<UAudioComponent> AudioShieldLoop;

	UPROPERTY(EditAnywhere, BlueprintReadWrite, Category = "Aerathea|Shieldwall")
	EAETShieldwallState ShieldState;

	UPROPERTY(EditAnywhere, BlueprintReadWrite, Category = "Aerathea|Shieldwall", meta = (ClampMin = "300.0", ClampMax = "1200.0"))
	float ShieldWidthCm;

	UPROPERTY(EditAnywhere, BlueprintReadWrite, Category = "Aerathea|Shieldwall", meta = (ClampMin = "3", ClampMax = "5"))
	int32 ProjectorCount;

	UPROPERTY(EditAnywhere, BlueprintReadWrite, Category = "Aerathea|Shieldwall", meta = (ClampMin = "180.0", ClampMax = "520.0"))
	float ArcHeightCm;

	UPROPERTY(EditAnywhere, BlueprintReadWrite, Category = "Aerathea|Shieldwall")
	bool bBlocksProjectiles;

	UPROPERTY(EditAnywhere, BlueprintReadWrite, Category = "Aerathea|Shieldwall")
	bool bBlocksPawns;

	UPROPERTY(EditAnywhere, BlueprintReadWrite, Category = "Aerathea|Shieldwall", meta = (ClampMin = "0.0", ClampMax = "1.0"))
	float ImpactIntensity;

	UPROPERTY(EditAnywhere, BlueprintReadWrite, Category = "Aerathea|Shieldwall", meta = (ClampMin = "0.0", ClampMax = "1.0"))
	float OverloadPercent;

	UFUNCTION(BlueprintCallable, Category = "Aerathea|Shieldwall")
	void SetShieldState(EAETShieldwallState NewState);

	UFUNCTION(BlueprintCallable, Category = "Aerathea|Shieldwall")
	void SetImpactIntensity(float NewImpactIntensity);

	UFUNCTION(BlueprintCallable, Category = "Aerathea|Shieldwall")
	void SetOverloadPercent(float NewOverloadPercent);

	UFUNCTION(BlueprintCallable, Category = "Aerathea|Shieldwall")
	void ConfigureShieldwall(int32 NewProjectorCount, float NewShieldWidthCm, float NewArcHeightCm);

protected:
	void AssignDefaultAssets();
	void UpdateShieldwallLayout();
	void ApplyShieldState();
	TArray<UStaticMeshComponent*> ProjectorComponents() const;
	TArray<UStaticMeshComponent*> ShieldPanelComponents() const;
};
