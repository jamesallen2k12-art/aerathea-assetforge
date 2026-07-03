#pragma once

#include "CoreMinimal.h"
#include "GameFramework/Actor.h"
#include "AETInfernalRitualAltarActor.generated.h"

class UBoxComponent;
class UMaterialInterface;
class UNiagaraComponent;
class UNiagaraSystem;
class USceneComponent;
class UStaticMesh;
class UStaticMeshComponent;

UENUM(BlueprintType)
enum class EAETInfernalRitualAltarState : uint8
{
	Inactive UMETA(DisplayName = "Inactive"),
	Smolder UMETA(DisplayName = "Smolder"),
	TrialActive UMETA(DisplayName = "Trial Active"),
	Accepted UMETA(DisplayName = "Accepted"),
	Rejected UMETA(DisplayName = "Rejected"),
	JudgmentPulse UMETA(DisplayName = "Judgment Pulse"),
	Cooldown UMETA(DisplayName = "Cooldown")
};

DECLARE_DYNAMIC_MULTICAST_DELEGATE_FiveParams(FAETInfernalRitualBindingStateChanged, EAETInfernalRitualAltarState, RitualState, FName, UIStateTag, FName, AudioEventName, float, TrialProgress, float, JudgmentIntensity);
DECLARE_DYNAMIC_MULTICAST_DELEGATE_FourParams(FAETInfernalRitualVerdictResolved, bool, bAccepted, FName, ObjectiveBindingId, float, VerdictIntensity, float, RejectionSeverity);

UCLASS(Blueprintable)
class AERATHEA_API AAETInfernalRitualAltarActor : public AActor
{
	GENERATED_BODY()

public:
	AAETInfernalRitualAltarActor();

	virtual void OnConstruction(const FTransform& Transform) override;

	UPROPERTY(VisibleAnywhere, BlueprintReadOnly, Category = "Aerathea|Infernal Ritual Altar")
	TObjectPtr<USceneComponent> SceneRoot;

	UPROPERTY(VisibleAnywhere, BlueprintReadOnly, Category = "Aerathea|Infernal Ritual Altar")
	TObjectPtr<UStaticMeshComponent> AltarMesh;

	UPROPERTY(VisibleAnywhere, BlueprintReadOnly, Category = "Aerathea|Infernal Ritual Altar|Interaction")
	TObjectPtr<UBoxComponent> InteractionVolume;

	UPROPERTY(VisibleAnywhere, BlueprintReadOnly, Category = "Aerathea|Infernal Ritual Altar|Markers")
	TObjectPtr<USceneComponent> InteractFrontLocator;

	UPROPERTY(VisibleAnywhere, BlueprintReadOnly, Category = "Aerathea|Infernal Ritual Altar|Markers")
	TObjectPtr<USceneComponent> AltarCoreLocator;

	UPROPERTY(VisibleAnywhere, BlueprintReadOnly, Category = "Aerathea|Infernal Ritual Altar|Markers")
	TObjectPtr<USceneComponent> SacrificeMarkLocator;

	UPROPERTY(VisibleAnywhere, BlueprintReadOnly, Category = "Aerathea|Infernal Ritual Altar|Markers")
	TObjectPtr<USceneComponent> BrandTransferLocator;

	UPROPERTY(VisibleAnywhere, BlueprintReadOnly, Category = "Aerathea|Infernal Ritual Altar|Markers")
	TObjectPtr<USceneComponent> RingLinkLocator;

	UPROPERTY(VisibleAnywhere, BlueprintReadOnly, Category = "Aerathea|Infernal Ritual Altar|Markers")
	TObjectPtr<USceneComponent> RejectedGapLocator;

	UPROPERTY(VisibleAnywhere, BlueprintReadOnly, Category = "Aerathea|Infernal Ritual Altar|VFX")
	TObjectPtr<UNiagaraComponent> WorthinessNiagara;

	UPROPERTY(EditAnywhere, BlueprintReadWrite, Category = "Aerathea|Infernal Ritual Altar")
	EAETInfernalRitualAltarState RitualState;

	UPROPERTY(EditAnywhere, BlueprintReadWrite, Category = "Aerathea|Infernal Ritual Altar", meta = (ClampMin = "0.0", ClampMax = "1.0"))
	float TrialProgress;

	UPROPERTY(EditAnywhere, BlueprintReadWrite, Category = "Aerathea|Infernal Ritual Altar", meta = (ClampMin = "0.0", ClampMax = "1.0"))
	float JudgmentIntensity;

	UPROPERTY(EditAnywhere, BlueprintReadWrite, Category = "Aerathea|Infernal Ritual Altar", meta = (ClampMin = "0.0", ClampMax = "1.0"))
	float RejectedSeverity;

	UPROPERTY(EditAnywhere, BlueprintReadWrite, Category = "Aerathea|Infernal Ritual Altar|Assets")
	TObjectPtr<UStaticMesh> AltarStaticMesh;

	UPROPERTY(EditAnywhere, BlueprintReadWrite, Category = "Aerathea|Infernal Ritual Altar|Materials", meta = (ClampMin = "0"))
	int32 BrandGlowMaterialSlotIndex;

	UPROPERTY(EditAnywhere, BlueprintReadWrite, Category = "Aerathea|Infernal Ritual Altar|Materials")
	TObjectPtr<UMaterialInterface> BrandGlowInactiveMaterial;

	UPROPERTY(EditAnywhere, BlueprintReadWrite, Category = "Aerathea|Infernal Ritual Altar|Materials")
	TObjectPtr<UMaterialInterface> BrandGlowSmolderMaterial;

	UPROPERTY(EditAnywhere, BlueprintReadWrite, Category = "Aerathea|Infernal Ritual Altar|Materials")
	TObjectPtr<UMaterialInterface> BrandGlowTrialActiveMaterial;

	UPROPERTY(EditAnywhere, BlueprintReadWrite, Category = "Aerathea|Infernal Ritual Altar|Materials")
	TObjectPtr<UMaterialInterface> BrandGlowAcceptedMaterial;

	UPROPERTY(EditAnywhere, BlueprintReadWrite, Category = "Aerathea|Infernal Ritual Altar|Materials")
	TObjectPtr<UMaterialInterface> BrandGlowRejectedMaterial;

	UPROPERTY(EditAnywhere, BlueprintReadWrite, Category = "Aerathea|Infernal Ritual Altar|Materials")
	TObjectPtr<UMaterialInterface> BrandGlowJudgmentPulseMaterial;

	UPROPERTY(EditAnywhere, BlueprintReadWrite, Category = "Aerathea|Infernal Ritual Altar|VFX")
	TObjectPtr<UNiagaraSystem> InactiveNiagaraSystem;

	UPROPERTY(EditAnywhere, BlueprintReadWrite, Category = "Aerathea|Infernal Ritual Altar|VFX")
	TObjectPtr<UNiagaraSystem> SmolderNiagaraSystem;

	UPROPERTY(EditAnywhere, BlueprintReadWrite, Category = "Aerathea|Infernal Ritual Altar|VFX")
	TObjectPtr<UNiagaraSystem> TrialActiveNiagaraSystem;

	UPROPERTY(EditAnywhere, BlueprintReadWrite, Category = "Aerathea|Infernal Ritual Altar|VFX")
	TObjectPtr<UNiagaraSystem> AcceptedNiagaraSystem;

	UPROPERTY(EditAnywhere, BlueprintReadWrite, Category = "Aerathea|Infernal Ritual Altar|VFX")
	TObjectPtr<UNiagaraSystem> RejectedNiagaraSystem;

	UPROPERTY(EditAnywhere, BlueprintReadWrite, Category = "Aerathea|Infernal Ritual Altar|VFX")
	TObjectPtr<UNiagaraSystem> JudgmentPulseNiagaraSystem;

	UPROPERTY(EditAnywhere, BlueprintReadWrite, Category = "Aerathea|Infernal Ritual Altar|VFX")
	bool bUseNiagara;

	UPROPERTY(EditAnywhere, BlueprintReadWrite, Category = "Aerathea|Infernal Ritual Altar|Interaction")
	bool bShowInteractionVolume;

	UPROPERTY(EditAnywhere, BlueprintReadWrite, Category = "Aerathea|Infernal Ritual Altar|Gameplay", meta = (ClampMin = "0.05", ClampMax = "60.0"))
	float TrialDurationSeconds;

	UPROPERTY(EditAnywhere, BlueprintReadWrite, Category = "Aerathea|Infernal Ritual Altar|Gameplay", meta = (ClampMin = "0.05", ClampMax = "10.0"))
	float JudgmentPulseSeconds;

	UPROPERTY(EditAnywhere, BlueprintReadWrite, Category = "Aerathea|Infernal Ritual Altar|Gameplay", meta = (ClampMin = "0.05", ClampMax = "30.0"))
	float CooldownSeconds;

	UPROPERTY(EditAnywhere, BlueprintReadWrite, Category = "Aerathea|Infernal Ritual Altar|Gameplay", meta = (ClampMin = "0.0", ClampMax = "1000.0"))
	float InteractionRadiusCm;

	UPROPERTY(EditAnywhere, BlueprintReadWrite, Category = "Aerathea|Infernal Ritual Altar|Gameplay", meta = (ClampMin = "0.0", ClampMax = "1000.0"))
	float InteractionDepthCm;

	UPROPERTY(EditAnywhere, BlueprintReadWrite, Category = "Aerathea|Infernal Ritual Altar|Binding")
	bool bBindingHooksEnabled;

	UPROPERTY(EditAnywhere, BlueprintReadWrite, Category = "Aerathea|Infernal Ritual Altar|Binding")
	FName RitualBindingId;

	UPROPERTY(EditAnywhere, BlueprintReadWrite, Category = "Aerathea|Infernal Ritual Altar|Binding")
	FName ObjectiveBindingId;

	UPROPERTY(EditAnywhere, BlueprintReadWrite, Category = "Aerathea|Infernal Ritual Altar|Binding")
	FName UIStatePrefix;

	UPROPERTY(EditAnywhere, BlueprintReadWrite, Category = "Aerathea|Infernal Ritual Altar|Binding")
	FName AudioEventPrefix;

	UPROPERTY(VisibleInstanceOnly, BlueprintReadOnly, Category = "Aerathea|Infernal Ritual Altar|Gameplay")
	float RitualElapsedSeconds;

	UPROPERTY(VisibleInstanceOnly, BlueprintReadOnly, Category = "Aerathea|Infernal Ritual Altar|Gameplay")
	float CooldownElapsedSeconds;

	UPROPERTY(VisibleInstanceOnly, BlueprintReadOnly, Category = "Aerathea|Infernal Ritual Altar|Gameplay")
	bool bRitualActive;

	UPROPERTY(VisibleInstanceOnly, BlueprintReadOnly, Category = "Aerathea|Infernal Ritual Altar|Binding")
	FName CurrentUIStateTag;

	UPROPERTY(VisibleInstanceOnly, BlueprintReadOnly, Category = "Aerathea|Infernal Ritual Altar|Binding")
	FName CurrentAudioEventName;

	UPROPERTY(VisibleInstanceOnly, BlueprintReadOnly, Category = "Aerathea|Infernal Ritual Altar|Binding")
	bool bLastVerdictAccepted;

	UPROPERTY(BlueprintAssignable, Category = "Aerathea|Infernal Ritual Altar|Binding")
	FAETInfernalRitualBindingStateChanged OnRitualBindingStateChanged;

	UPROPERTY(BlueprintAssignable, Category = "Aerathea|Infernal Ritual Altar|Binding")
	FAETInfernalRitualVerdictResolved OnRitualVerdictResolved;

	UFUNCTION(BlueprintCallable, Category = "Aerathea|Infernal Ritual Altar")
	void SetRitualState(EAETInfernalRitualAltarState NewState);

	UFUNCTION(BlueprintCallable, Category = "Aerathea|Infernal Ritual Altar")
	void SetTrialProgress(float NewTrialProgress);

	UFUNCTION(BlueprintCallable, Category = "Aerathea|Infernal Ritual Altar")
	void SetJudgmentIntensity(float NewJudgmentIntensity);

	UFUNCTION(BlueprintCallable, Category = "Aerathea|Infernal Ritual Altar")
	void StartTrial();

	UFUNCTION(BlueprintCallable, Category = "Aerathea|Infernal Ritual Altar")
	void AcceptSacrifice(float AcceptanceIntensity);

	UFUNCTION(BlueprintCallable, Category = "Aerathea|Infernal Ritual Altar")
	void RejectSacrifice(float RejectionSeverity);

	UFUNCTION(BlueprintCallable, Category = "Aerathea|Infernal Ritual Altar")
	void TriggerJudgmentPulse(float PulseIntensity);

	UFUNCTION(BlueprintCallable, Category = "Aerathea|Infernal Ritual Altar|Gameplay")
	void AdvanceRitual(float DeltaSeconds);

	UFUNCTION(BlueprintCallable, Category = "Aerathea|Infernal Ritual Altar|Gameplay")
	float GetTrialAlpha() const;

	UFUNCTION(BlueprintCallable, Category = "Aerathea|Infernal Ritual Altar|Gameplay")
	float GetCooldownAlpha() const;

	UFUNCTION(BlueprintCallable, Category = "Aerathea|Infernal Ritual Altar|Gameplay")
	FVector GetInteractFrontLocation() const;

	UFUNCTION(BlueprintCallable, Category = "Aerathea|Infernal Ritual Altar|Gameplay")
	FVector GetAltarCoreLocation() const;

	UFUNCTION(BlueprintCallable, Category = "Aerathea|Infernal Ritual Altar|Gameplay")
	FVector GetSacrificeMarkLocation() const;

	UFUNCTION(BlueprintCallable, Category = "Aerathea|Infernal Ritual Altar|Gameplay")
	FVector GetBrandTransferLocation() const;

	UFUNCTION(BlueprintCallable, Category = "Aerathea|Infernal Ritual Altar|Gameplay")
	FVector GetRingLinkLocation() const;

	UFUNCTION(BlueprintCallable, Category = "Aerathea|Infernal Ritual Altar|Gameplay")
	FVector GetRejectedGapLocation() const;

	UFUNCTION(BlueprintCallable, Category = "Aerathea|Infernal Ritual Altar|Binding")
	FName GetCurrentUIStateTag() const;

	UFUNCTION(BlueprintCallable, Category = "Aerathea|Infernal Ritual Altar|Binding")
	FName GetCurrentAudioEventName() const;

	UFUNCTION(BlueprintCallable, Category = "Aerathea|Infernal Ritual Altar|Binding")
	FName GetRitualBindingId() const;

	UFUNCTION(BlueprintCallable, Category = "Aerathea|Infernal Ritual Altar|Binding")
	FName GetObjectiveBindingId() const;

	UFUNCTION(BlueprintCallable, Category = "Aerathea|Infernal Ritual Altar")
	void ResetRitual();

protected:
	void AssignDefaultAssets();
	void UpdateAltarLayout();
	void ApplyRitualState();
	float CurrentStateValue() const;
	FLinearColor CurrentStateColor() const;
	UMaterialInterface* MaterialForState() const;
	UNiagaraSystem* NiagaraSystemForState() const;
	FName StateSuffixName() const;
	FName BuildBindingTag(FName Prefix) const;
	void UpdateBindingState();
	void BroadcastBindingStateChanged();
	void BroadcastVerdictResolved(bool bAccepted, float VerdictIntensity);
};
