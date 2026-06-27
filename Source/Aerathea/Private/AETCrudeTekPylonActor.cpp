#include "AETCrudeTekPylonActor.h"

#include "Components/SceneComponent.h"
#include "Components/StaticMeshComponent.h"
#include "Engine/StaticMesh.h"
#include "NiagaraComponent.h"
#include "NiagaraSystem.h"

AAETCrudeTekPylonActor::AAETCrudeTekPylonActor()
{
	PrimaryActorTick.bCanEverTick = false;
	bReplicates = true;

	PylonState = EAETCrudeTekPylonState::Idle;
	OverloadPercent = 0.0f;
	DamagePercent = 0.0f;
	bPoweredVisible = true;
	bUseNiagara = true;
	DamageWindowSeconds = 8.0f;
	RepairWindowSeconds = 10.0f;
	DamageTraceRadiusCm = 220.0f;
	RepairTraceRadiusCm = 180.0f;
	DamagePerTrace = 0.18f;
	RepairPerTrace = 0.16f;
	DamageWindowElapsedSeconds = 0.0f;
	RepairWindowElapsedSeconds = 0.0f;
	bDamageWindowActive = false;
	bRepairWindowActive = false;

	SceneRoot = CreateDefaultSubobject<USceneComponent>(TEXT("SceneRoot"));
	SetRootComponent(SceneRoot);

	PylonMesh = CreateDefaultSubobject<UStaticMeshComponent>(TEXT("PylonMesh"));
	PylonMesh->SetupAttachment(SceneRoot);
	PylonMesh->SetCollisionProfileName(TEXT("BlockAll"));

	CoreLocator = CreateDefaultSubobject<USceneComponent>(TEXT("CoreLocator"));
	CoreLocator->SetupAttachment(SceneRoot);

	TopArcLocator = CreateDefaultSubobject<USceneComponent>(TEXT("TopArcLocator"));
	TopArcLocator->SetupAttachment(SceneRoot);

	GroundSparksLocator = CreateDefaultSubobject<USceneComponent>(TEXT("GroundSparksLocator"));
	GroundSparksLocator->SetupAttachment(SceneRoot);

	PylonNiagara = CreateDefaultSubobject<UNiagaraComponent>(TEXT("PylonNiagara"));
	PylonNiagara->SetupAttachment(SceneRoot);
	PylonNiagara->SetAutoActivate(false);
	PylonNiagara->SetVisibleFlag(false);
	PylonNiagara->SetHiddenInGame(true, true);
}

void AAETCrudeTekPylonActor::OnConstruction(const FTransform& Transform)
{
	Super::OnConstruction(Transform);

	OverloadPercent = FMath::Clamp(OverloadPercent, 0.0f, 1.0f);
	DamagePercent = FMath::Clamp(DamagePercent, 0.0f, 1.0f);
	DamageWindowSeconds = FMath::Clamp(DamageWindowSeconds, 0.05f, 60.0f);
	RepairWindowSeconds = FMath::Clamp(RepairWindowSeconds, 0.05f, 60.0f);
	DamageTraceRadiusCm = FMath::Clamp(DamageTraceRadiusCm, 0.0f, 1000.0f);
	RepairTraceRadiusCm = FMath::Clamp(RepairTraceRadiusCm, 0.0f, 1000.0f);
	DamagePerTrace = FMath::Clamp(DamagePerTrace, 0.0f, 1.0f);
	RepairPerTrace = FMath::Clamp(RepairPerTrace, 0.0f, 1.0f);
	AssignDefaultAssets();
	UpdatePylonLayout();
	ApplyPylonState();
}

void AAETCrudeTekPylonActor::SetPylonState(EAETCrudeTekPylonState NewState)
{
	PylonState = NewState;
	if (PylonState == EAETCrudeTekPylonState::Destroyed)
	{
		bDamageWindowActive = false;
		bRepairWindowActive = false;
	}
	ApplyPylonState();
}

void AAETCrudeTekPylonActor::SetOverloadPercent(float NewOverloadPercent)
{
	OverloadPercent = FMath::Clamp(NewOverloadPercent, 0.0f, 1.0f);
	if (OverloadPercent > 0.66f && PylonState == EAETCrudeTekPylonState::Idle)
	{
		PylonState = EAETCrudeTekPylonState::Charged;
	}
	ApplyPylonState();
}

void AAETCrudeTekPylonActor::SetDamagePercent(float NewDamagePercent)
{
	DamagePercent = FMath::Clamp(NewDamagePercent, 0.0f, 1.0f);
	if (DamagePercent > 0.75f)
	{
		PylonState = EAETCrudeTekPylonState::Destroyed;
		bDamageWindowActive = false;
		bRepairWindowActive = false;
	}
	else if (DamagePercent > 0.25f && PylonState != EAETCrudeTekPylonState::Overload)
	{
		PylonState = EAETCrudeTekPylonState::Damaged;
	}
	ApplyPylonState();
}

void AAETCrudeTekPylonActor::TriggerOverload(float NewOverloadPercent)
{
	OverloadPercent = FMath::Clamp(NewOverloadPercent, 0.0f, 1.0f);
	PylonState = EAETCrudeTekPylonState::Overload;
	ApplyPylonState();
}

void AAETCrudeTekPylonActor::BeginDamageWindow()
{
	DamageWindowElapsedSeconds = 0.0f;
	RepairWindowElapsedSeconds = 0.0f;
	bDamageWindowActive = true;
	bRepairWindowActive = false;
	if (PylonState != EAETCrudeTekPylonState::Destroyed)
	{
		PylonState = EAETCrudeTekPylonState::Overload;
	}
	ApplyPylonState();
}

void AAETCrudeTekPylonActor::BeginRepairWindow()
{
	DamageWindowElapsedSeconds = 0.0f;
	RepairWindowElapsedSeconds = 0.0f;
	bDamageWindowActive = false;
	bRepairWindowActive = PylonState != EAETCrudeTekPylonState::Destroyed;
	if (bRepairWindowActive)
	{
		PylonState = EAETCrudeTekPylonState::Damaged;
	}
	ApplyPylonState();
}

void AAETCrudeTekPylonActor::AdvanceObjectiveWindow(float DeltaSeconds)
{
	const float ClampedDeltaSeconds = FMath::Max(DeltaSeconds, 0.0f);
	if (bDamageWindowActive)
	{
		DamageWindowElapsedSeconds = FMath::Min(DamageWindowElapsedSeconds + ClampedDeltaSeconds, DamageWindowSeconds);
		if (DamageWindowElapsedSeconds >= DamageWindowSeconds)
		{
			bDamageWindowActive = false;
		}
	}
	if (bRepairWindowActive)
	{
		RepairWindowElapsedSeconds = FMath::Min(RepairWindowElapsedSeconds + ClampedDeltaSeconds, RepairWindowSeconds);
		if (RepairWindowElapsedSeconds >= RepairWindowSeconds)
		{
			bRepairWindowActive = false;
		}
	}
	ApplyPylonState();
}

void AAETCrudeTekPylonActor::ApplyDamageTrace(float DamageScale)
{
	if (!bDamageWindowActive || PylonState == EAETCrudeTekPylonState::Destroyed)
	{
		return;
	}

	SetDamagePercent(DamagePercent + DamagePerTrace * FMath::Max(DamageScale, 0.0f));
}

void AAETCrudeTekPylonActor::ApplyRepairTrace(float RepairScale)
{
	if (!bRepairWindowActive || PylonState == EAETCrudeTekPylonState::Destroyed)
	{
		return;
	}

	SetDamagePercent(DamagePercent - RepairPerTrace * FMath::Max(RepairScale, 0.0f));
	if (DamagePercent <= KINDA_SMALL_NUMBER)
	{
		DamagePercent = 0.0f;
		bRepairWindowActive = false;
		PylonState = OverloadPercent > 0.25f ? EAETCrudeTekPylonState::Charged : EAETCrudeTekPylonState::Idle;
		ApplyPylonState();
	}
}

bool AAETCrudeTekPylonActor::IsDamageWindowActive() const
{
	return bDamageWindowActive;
}

bool AAETCrudeTekPylonActor::IsRepairWindowActive() const
{
	return bRepairWindowActive;
}

float AAETCrudeTekPylonActor::GetDamageWindowAlpha() const
{
	return DamageWindowSeconds > KINDA_SMALL_NUMBER ? FMath::Clamp(DamageWindowElapsedSeconds / DamageWindowSeconds, 0.0f, 1.0f) : 0.0f;
}

float AAETCrudeTekPylonActor::GetRepairWindowAlpha() const
{
	return RepairWindowSeconds > KINDA_SMALL_NUMBER ? FMath::Clamp(RepairWindowElapsedSeconds / RepairWindowSeconds, 0.0f, 1.0f) : 0.0f;
}

FVector AAETCrudeTekPylonActor::GetCoreTraceLocation() const
{
	return CoreLocator != nullptr ? CoreLocator->GetComponentLocation() : GetActorLocation();
}

FVector AAETCrudeTekPylonActor::GetTopArcTraceLocation() const
{
	return TopArcLocator != nullptr ? TopArcLocator->GetComponentLocation() : GetActorLocation();
}

FVector AAETCrudeTekPylonActor::GetGroundSparksTraceLocation() const
{
	return GroundSparksLocator != nullptr ? GroundSparksLocator->GetComponentLocation() : GetActorLocation();
}

void AAETCrudeTekPylonActor::ResetPylon()
{
	OverloadPercent = 0.0f;
	DamagePercent = 0.0f;
	PylonState = EAETCrudeTekPylonState::Idle;
	bPoweredVisible = true;
	DamageWindowElapsedSeconds = 0.0f;
	RepairWindowElapsedSeconds = 0.0f;
	bDamageWindowActive = false;
	bRepairWindowActive = false;
	ApplyPylonState();
}

void AAETCrudeTekPylonActor::AssignDefaultAssets()
{
	if (PylonStaticMesh == nullptr)
	{
		PylonStaticMesh = LoadObject<UStaticMesh>(
			nullptr,
			TEXT("/Game/Aerathea/Props/Ogres/Teknomancy/SM_OGR_CrudeTekPylon_A01.SM_OGR_CrudeTekPylon_A01")
		);
	}
	if (PylonNiagaraSystem == nullptr)
	{
		PylonNiagaraSystem = LoadObject<UNiagaraSystem>(
			nullptr,
			TEXT("/Game/Aerathea/VFX/Ogres/NS_OGR_CrudeTekPylon_A01.NS_OGR_CrudeTekPylon_A01")
		);
	}
	if (PylonMesh != nullptr && PylonMesh->GetStaticMesh() == nullptr && PylonStaticMesh != nullptr)
	{
		PylonMesh->SetStaticMesh(PylonStaticMesh);
	}
}

void AAETCrudeTekPylonActor::UpdatePylonLayout()
{
	if (CoreLocator != nullptr)
	{
		CoreLocator->SetRelativeLocation(FVector(56.0f, 0.0f, 206.0f));
	}
	if (TopArcLocator != nullptr)
	{
		TopArcLocator->SetRelativeLocation(FVector(72.0f, 0.0f, 436.0f));
	}
	if (GroundSparksLocator != nullptr)
	{
		GroundSparksLocator->SetRelativeLocation(FVector(18.0f, 0.0f, 38.0f));
	}
	if (PylonNiagara != nullptr)
	{
		PylonNiagara->SetRelativeLocation(FVector(64.0f, 0.0f, 230.0f));
		PylonNiagara->SetRelativeScale3D(FVector(1.0f, 1.0f, 1.35f));
	}
}

void AAETCrudeTekPylonActor::ApplyPylonState()
{
	const bool bDestroyed = PylonState == EAETCrudeTekPylonState::Destroyed;
	const bool bVisible = bPoweredVisible || bDestroyed;
	const float StateValue = static_cast<float>(static_cast<uint8>(PylonState));

	FLinearColor StateColor(1.0f, 0.38f, 0.04f, 1.0f);
	if (PylonState == EAETCrudeTekPylonState::Idle)
	{
		StateColor = FLinearColor(0.25f, 0.62f, 1.0f, 1.0f);
	}
	else if (PylonState == EAETCrudeTekPylonState::Damaged)
	{
		StateColor = FLinearColor(0.95f, 0.12f, 0.02f, 1.0f);
	}
	else if (bDestroyed)
	{
		StateColor = FLinearColor(0.12f, 0.10f, 0.08f, 1.0f);
	}

	if (PylonMesh != nullptr)
	{
		PylonMesh->SetVisibility(bVisible, true);
		PylonMesh->SetHiddenInGame(!bVisible, true);
		PylonMesh->SetCollisionEnabled(bDestroyed ? ECollisionEnabled::QueryOnly : ECollisionEnabled::QueryAndPhysics);
		PylonMesh->SetScalarParameterValueOnMaterials(TEXT("PylonState"), StateValue);
		PylonMesh->SetScalarParameterValueOnMaterials(TEXT("OverloadPercent"), OverloadPercent);
		PylonMesh->SetScalarParameterValueOnMaterials(TEXT("DamagePercent"), DamagePercent);
		PylonMesh->SetScalarParameterValueOnMaterials(TEXT("DamageWindowAlpha"), GetDamageWindowAlpha());
		PylonMesh->SetScalarParameterValueOnMaterials(TEXT("RepairWindowAlpha"), GetRepairWindowAlpha());
		PylonMesh->SetVectorParameterValueOnMaterials(TEXT("StateColor"), FVector(StateColor.R, StateColor.G, StateColor.B));
	}

	if (PylonNiagara != nullptr)
	{
		if (PylonNiagaraSystem != nullptr && PylonNiagara->GetAsset() == nullptr)
		{
			PylonNiagara->SetAsset(PylonNiagaraSystem);
		}

		const bool bRunNiagara = bUseNiagara && bVisible && !bDestroyed && PylonNiagaraSystem != nullptr;
		PylonNiagara->SetVisibility(bRunNiagara, true);
		PylonNiagara->SetHiddenInGame(!bRunNiagara, true);
		if (bRunNiagara && !PylonNiagara->IsActive())
		{
			PylonNiagara->Activate(true);
		}
		else if (!bRunNiagara && PylonNiagara->IsActive())
		{
			PylonNiagara->Deactivate();
		}

		PylonNiagara->SetVariableFloat(TEXT("User.PylonState"), StateValue);
		PylonNiagara->SetVariableFloat(TEXT("User.OverloadPercent"), OverloadPercent);
		PylonNiagara->SetVariableFloat(TEXT("User.DamagePercent"), DamagePercent);
		PylonNiagara->SetVariableFloat(TEXT("User.DamageWindowAlpha"), GetDamageWindowAlpha());
		PylonNiagara->SetVariableFloat(TEXT("User.RepairWindowAlpha"), GetRepairWindowAlpha());
		PylonNiagara->SetVariableFloat(TEXT("User.DamageTraceRadius"), DamageTraceRadiusCm);
		PylonNiagara->SetVariableFloat(TEXT("User.RepairTraceRadius"), RepairTraceRadiusCm);
		PylonNiagara->SetVariableBool(TEXT("User.bOverloaded"), PylonState == EAETCrudeTekPylonState::Overload || OverloadPercent > 0.66f);
		PylonNiagara->SetVariableBool(TEXT("User.bDestroyed"), bDestroyed);
		PylonNiagara->SetVariableBool(TEXT("User.bDamageWindowActive"), bDamageWindowActive);
		PylonNiagara->SetVariableBool(TEXT("User.bRepairWindowActive"), bRepairWindowActive);
		PylonNiagara->SetVariableLinearColor(TEXT("User.StateColor"), StateColor);
		if (CoreLocator != nullptr)
		{
			PylonNiagara->SetVariableVec3(TEXT("User.CoreWorldLocation"), CoreLocator->GetComponentLocation());
		}
		if (TopArcLocator != nullptr)
		{
			PylonNiagara->SetVariableVec3(TEXT("User.TopArcWorldLocation"), TopArcLocator->GetComponentLocation());
		}
		if (GroundSparksLocator != nullptr)
		{
			PylonNiagara->SetVariableVec3(TEXT("User.GroundSparksWorldLocation"), GroundSparksLocator->GetComponentLocation());
		}
	}
}
