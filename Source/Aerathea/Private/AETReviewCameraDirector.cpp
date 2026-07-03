#include "AETReviewCameraDirector.h"

#include "AETGnomeOgreBattlefieldEncounterActor.h"
#include "AETHeavyMekShieldwallActor.h"
#include "Camera/CameraActor.h"
#include "Camera/CameraComponent.h"
#include "Components/PrimitiveComponent.h"
#include "EngineUtils.h"
#include "GameFramework/PlayerController.h"
#include "HAL/PlatformMisc.h"
#include "Misc/CommandLine.h"
#include "Misc/Parse.h"
#include "TimerManager.h"

namespace
{
FString NormalizedReviewPhaseName(FString PhaseName)
{
	PhaseName.TrimStartAndEndInline();
	PhaseName.ReplaceInline(TEXT("-"), TEXT(""));
	PhaseName.ReplaceInline(TEXT("_"), TEXT(""));
	PhaseName.ReplaceInline(TEXT(" "), TEXT(""));
	return PhaseName.ToLower();
}

bool TryReadEncounterPhaseCommandLine(EAETGnomeOgreEncounterState& OutState, FString& OutPhaseName)
{
	FString PhaseName;
	if (!FParse::Value(FCommandLine::Get(), TEXT("AETEncounterPhase="), PhaseName) &&
		!FParse::Value(FCommandLine::Get(), TEXT("AETReviewEncounterPhase="), PhaseName))
	{
		return false;
	}

	OutPhaseName = PhaseName;
	const FString NormalizedPhaseName = NormalizedReviewPhaseName(PhaseName);
	if (NormalizedPhaseName == TEXT("setup"))
	{
		OutState = EAETGnomeOgreEncounterState::Setup;
		return true;
	}
	if (NormalizedPhaseName == TEXT("gnomeholdline"))
	{
		OutState = EAETGnomeOgreEncounterState::GnomeHoldLine;
		return true;
	}
	if (NormalizedPhaseName == TEXT("ogreadvance"))
	{
		OutState = EAETGnomeOgreEncounterState::OgreAdvance;
		return true;
	}
	if (NormalizedPhaseName == TEXT("shieldimpact"))
	{
		OutState = EAETGnomeOgreEncounterState::ShieldImpact;
		return true;
	}
	if (NormalizedPhaseName == TEXT("pylonoverload"))
	{
		OutState = EAETGnomeOgreEncounterState::PylonOverload;
		return true;
	}
	if (NormalizedPhaseName == TEXT("casterreinforcement"))
	{
		OutState = EAETGnomeOgreEncounterState::CasterReinforcement;
		return true;
	}
	if (NormalizedPhaseName == TEXT("manticoreinterrupt"))
	{
		OutState = EAETGnomeOgreEncounterState::ManticoreInterrupt;
		return true;
	}
	if (NormalizedPhaseName == TEXT("resolution"))
	{
		OutState = EAETGnomeOgreEncounterState::Resolution;
		return true;
	}

	UE_LOG(LogTemp, Warning, TEXT("AETReviewCameraDirector: unrecognized AETEncounterPhase value '%s'."), *OutPhaseName);
	return false;
}

int32 ReviewPhaseIndexForState(EAETGnomeOgreEncounterState State)
{
	switch (State)
	{
	case EAETGnomeOgreEncounterState::GnomeHoldLine:
		return 0;
	case EAETGnomeOgreEncounterState::OgreAdvance:
		return 1;
	case EAETGnomeOgreEncounterState::ShieldImpact:
		return 2;
	case EAETGnomeOgreEncounterState::PylonOverload:
		return 3;
	case EAETGnomeOgreEncounterState::CasterReinforcement:
		return 4;
	case EAETGnomeOgreEncounterState::ManticoreInterrupt:
		return 5;
	case EAETGnomeOgreEncounterState::Resolution:
		return 6;
	case EAETGnomeOgreEncounterState::Setup:
	default:
		return 0;
	}
}

AAETGnomeOgreBattlefieldEncounterActor* FindGnomeOgreEncounterActor(UWorld* World)
{
	if (World == nullptr)
	{
		return nullptr;
	}

	for (TActorIterator<AAETGnomeOgreBattlefieldEncounterActor> It(World); It; ++It)
	{
		AAETGnomeOgreBattlefieldEncounterActor* EncounterActor = *It;
		if (EncounterActor != nullptr)
		{
			return EncounterActor;
		}
	}

	return nullptr;
}

const TCHAR* ReviewPhaseLogName(EAETGnomeOgreEncounterState State)
{
	switch (State)
	{
	case EAETGnomeOgreEncounterState::Setup:
		return TEXT("Setup");
	case EAETGnomeOgreEncounterState::GnomeHoldLine:
		return TEXT("GnomeHoldLine");
	case EAETGnomeOgreEncounterState::OgreAdvance:
		return TEXT("OgreAdvance");
	case EAETGnomeOgreEncounterState::ShieldImpact:
		return TEXT("ShieldImpact");
	case EAETGnomeOgreEncounterState::PylonOverload:
		return TEXT("PylonOverload");
	case EAETGnomeOgreEncounterState::CasterReinforcement:
		return TEXT("CasterReinforcement");
	case EAETGnomeOgreEncounterState::ManticoreInterrupt:
		return TEXT("ManticoreInterrupt");
	case EAETGnomeOgreEncounterState::Resolution:
		return TEXT("Resolution");
	default:
		return TEXT("Unknown");
	}
}

bool IsPhaseFocusRequested()
{
	return FParse::Param(FCommandLine::Get(), TEXT("AETReviewPhaseFocus")) ||
		FParse::Param(FCommandLine::Get(), TEXT("AETReviewFocusPhase"));
}

struct FFocusedEncounterCameraSettings
{
	AActor* FocusActor = nullptr;
	FVector AimOffset = FVector(0.0f, 0.0f, 160.0f);
	FVector CameraOffset = FVector(1450.0f, -920.0f, 720.0f);
	float FieldOfView = 42.0f;
	bool bUseBoundsOrigin = false;
};

void LogReviewViewState(const TCHAR* Context, APlayerController* PlayerController)
{
	if (PlayerController == nullptr)
	{
		return;
	}

	FVector ViewLocation = FVector::ZeroVector;
	FRotator ViewRotation = FRotator::ZeroRotator;
	PlayerController->GetPlayerViewPoint(ViewLocation, ViewRotation);

	AActor* ViewTarget = PlayerController->GetViewTarget();
	UE_LOG(
		LogTemp,
		Display,
		TEXT("AETReviewCameraDirector: %s view target=%s viewpoint=%s rot=%s."),
		Context,
		*GetNameSafe(ViewTarget),
		*ViewLocation.ToCompactString(),
		*ViewRotation.ToCompactString()
	);
}
}

AAETReviewCameraDirector::AAETReviewCameraDirector()
{
	PrimaryActorTick.bCanEverTick = true;
	PrimaryActorTick.bStartWithTickEnabled = true;
	ReviewCameraTag = TEXT("AET_REVIEW_CAMERA");
	bCaptureReviewScreenshot = false;
	ScreenshotWidth = 1280;
	ScreenshotHeight = 720;
	ScreenshotFilenameOverride = TEXT("");
	ScreenshotDelaySeconds = 0.5f;
	ScreenshotWarmupFrames = 10;
	bReviewScreenshotRequested = false;
	bScreenshotDelayElapsed = false;
	bReviewExposureConfigured = false;
	bOrbitReviewCamera = false;
	CaptureElapsedSeconds = 0.0f;
	OrbitElapsedSeconds = 0.0f;
	OrbitStartAngleDegrees = 235.0f;
	OrbitSpeedDegreesPerSecond = 20.0f;
	OrbitRadius = 700.0f;
	OrbitHeight = 250.0f;
	OrbitFieldOfView = 48.0f;
	OrbitLogElapsedSeconds = 0.0f;
	OrbitTarget = FVector(0.0f, 0.0f, 150.0f);
	bOrbitCameraMissingLogged = false;
	RemainingWarmupFrames = INDEX_NONE;
	PostScreenshotExitFrames = INDEX_NONE;
}

void AAETReviewCameraDirector::BeginPlay()
{
	Super::BeginPlay();

	SetActorTickEnabled(true);
	PrimaryActorTick.SetTickFunctionEnable(true);
	bCaptureReviewScreenshot = bCaptureReviewScreenshot || FParse::Param(FCommandLine::Get(), TEXT("AETReviewCapture"));
	CaptureElapsedSeconds = 0.0f;
	OrbitElapsedSeconds = 0.0f;
	OrbitLogElapsedSeconds = 0.0f;
	bOrbitCameraMissingLogged = false;
	PostScreenshotExitFrames = INDEX_NONE;

	ConfigureCommandLineOptions();
	ConfigureReviewMarkers();
	ApplyReviewCamera();
	ConfigureEncounterReviewPhase();

	if (UWorld* World = GetWorld())
	{
		World->GetTimerManager().SetTimerForNextTick(this, &AAETReviewCameraDirector::ApplyReviewCamera);
		World->GetTimerManager().SetTimerForNextTick(this, &AAETReviewCameraDirector::ConfigureEncounterReviewPhase);
	}

	if (bCaptureReviewScreenshot)
	{
		RemainingWarmupFrames = FMath::Max(1, ScreenshotWarmupFrames);
	}
	else
	{
		bScreenshotDelayElapsed = true;
	}

	UE_LOG(
		LogTemp,
		Display,
		TEXT("AETReviewCameraDirector: screenshot capture %s, delay %.2fs, warmup %d frames."),
		bCaptureReviewScreenshot ? TEXT("enabled") : TEXT("disabled"),
		ScreenshotDelaySeconds,
		ScreenshotWarmupFrames
	);
}

void AAETReviewCameraDirector::ConfigureCommandLineOptions()
{
	float RequestedDelay = ScreenshotDelaySeconds;
	if (FParse::Value(FCommandLine::Get(), TEXT("AETReviewCaptureDelay="), RequestedDelay))
	{
		ScreenshotDelaySeconds = FMath::Max(0.2f, RequestedDelay);
	}

	bOrbitReviewCamera =
		FParse::Param(FCommandLine::Get(), TEXT("AETReviewOrbit")) ||
		FParse::Param(FCommandLine::Get(), TEXT("AETReviewCameraOrbit"));

	float RequestedFloat = 0.0f;
	if (FParse::Value(FCommandLine::Get(), TEXT("AETReviewOrbitStartAngle="), RequestedFloat))
	{
		OrbitStartAngleDegrees = RequestedFloat;
	}
	if (FParse::Value(FCommandLine::Get(), TEXT("AETReviewOrbitSpeed="), RequestedFloat))
	{
		OrbitSpeedDegreesPerSecond = RequestedFloat;
	}
	if (FParse::Value(FCommandLine::Get(), TEXT("AETReviewOrbitRadius="), RequestedFloat))
	{
		OrbitRadius = FMath::Max(100.0f, RequestedFloat);
	}
	if (FParse::Value(FCommandLine::Get(), TEXT("AETReviewOrbitHeight="), RequestedFloat))
	{
		OrbitHeight = RequestedFloat;
	}
	if (FParse::Value(FCommandLine::Get(), TEXT("AETReviewOrbitFOV="), RequestedFloat))
	{
		OrbitFieldOfView = FMath::Clamp(RequestedFloat, 5.0f, 170.0f);
	}
	if (FParse::Value(FCommandLine::Get(), TEXT("AETReviewOrbitTargetX="), RequestedFloat))
	{
		OrbitTarget.X = RequestedFloat;
	}
	if (FParse::Value(FCommandLine::Get(), TEXT("AETReviewOrbitTargetY="), RequestedFloat))
	{
		OrbitTarget.Y = RequestedFloat;
	}
	if (FParse::Value(FCommandLine::Get(), TEXT("AETReviewOrbitTargetZ="), RequestedFloat))
	{
		OrbitTarget.Z = RequestedFloat;
	}

	if (bOrbitReviewCamera)
	{
		UE_LOG(
			LogTemp,
			Display,
			TEXT("AETReviewCameraDirector: orbit camera enabled target=%s radius=%.1f height=%.1f fov=%.1f speed=%.1f startAngle=%.1f."),
			*OrbitTarget.ToCompactString(),
			OrbitRadius,
			OrbitHeight,
			OrbitFieldOfView,
			OrbitSpeedDegreesPerSecond,
			OrbitStartAngleDegrees
		);
	}
}

void AAETReviewCameraDirector::ConfigureEncounterReviewPhase()
{
	EAETGnomeOgreEncounterState RequestedState = EAETGnomeOgreEncounterState::Setup;
	FString RequestedPhaseName;
	if (!TryReadEncounterPhaseCommandLine(RequestedState, RequestedPhaseName))
	{
		return;
	}

	UWorld* World = GetWorld();
	if (World == nullptr)
	{
		return;
	}

	AAETGnomeOgreBattlefieldEncounterActor* EncounterActor = FindGnomeOgreEncounterActor(World);
	if (EncounterActor == nullptr)
	{
		UE_LOG(LogTemp, Warning, TEXT("AETReviewCameraDirector: AETEncounterPhase requested, but no Gnome/Ogre encounter actor was found."));
		return;
	}

	EncounterActor->bAutoStart = false;
	EncounterActor->bAutoAdvanceReviewPhases = false;
	EncounterActor->StopReviewPhaseSequence();
	EncounterActor->ReviewPhaseIndex = ReviewPhaseIndexForState(RequestedState);
	EncounterActor->ResetEncounter();

	switch (RequestedState)
	{
	case EAETGnomeOgreEncounterState::Setup:
		break;
	case EAETGnomeOgreEncounterState::GnomeHoldLine:
	case EAETGnomeOgreEncounterState::OgreAdvance:
	case EAETGnomeOgreEncounterState::Resolution:
		EncounterActor->SetEncounterState(RequestedState);
		break;
	case EAETGnomeOgreEncounterState::ShieldImpact:
		EncounterActor->TriggerShieldImpact(0.15f, 0.75f);
		break;
	case EAETGnomeOgreEncounterState::PylonOverload:
		EncounterActor->TriggerPylonOverload(0.78f);
		break;
	case EAETGnomeOgreEncounterState::CasterReinforcement:
		EncounterActor->TriggerCasterReinforcement(
			EncounterActor->OgreShamanActor != nullptr ? EncounterActor->OgreShamanActor.Get() : EncounterActor->OgreNecromancerActor.Get()
		);
		break;
	case EAETGnomeOgreEncounterState::ManticoreInterrupt:
		EncounterActor->TriggerManticoreInterrupt(EncounterActor->ManticoreInterruptActor.Get());
		break;
	default:
		break;
	}

	UE_LOG(
		LogTemp,
		Display,
		TEXT("AETReviewCameraDirector: forced Gnome/Ogre review phase %s from command-line value '%s'."),
		ReviewPhaseLogName(RequestedState),
		*RequestedPhaseName
	);
}

void AAETReviewCameraDirector::Tick(float DeltaSeconds)
{
	Super::Tick(DeltaSeconds);

	UpdateOrbitCamera(DeltaSeconds);

	if (!bCaptureReviewScreenshot || bReviewScreenshotRequested)
	{
		if (bReviewScreenshotRequested && PostScreenshotExitFrames != INDEX_NONE)
		{
			--PostScreenshotExitFrames;
			if (PostScreenshotExitFrames <= 0)
			{
				PostScreenshotExitFrames = INDEX_NONE;
				RequestReviewExit();
			}
		}
		return;
	}

	CaptureElapsedSeconds += DeltaSeconds;
	if (!bScreenshotDelayElapsed && CaptureElapsedSeconds >= FMath::Max(0.2f, ScreenshotDelaySeconds))
	{
		bScreenshotDelayElapsed = true;
		UE_LOG(LogTemp, Display, TEXT("AETReviewCameraDirector: screenshot delay elapsed after %.2fs."), CaptureElapsedSeconds);
	}

	if (RemainingWarmupFrames == INDEX_NONE)
	{
		RemainingWarmupFrames = FMath::Max(1, ScreenshotWarmupFrames);
	}

	--RemainingWarmupFrames;
	TryRequestReviewScreenshot();
}

void AAETReviewCameraDirector::EndPlay(const EEndPlayReason::Type EndPlayReason)
{
	if (UWorld* World = GetWorld())
	{
		World->GetTimerManager().ClearTimer(ScreenshotTimerHandle);
		World->GetTimerManager().ClearTimer(ExitTimerHandle);
	}

	Super::EndPlay(EndPlayReason);
}

void AAETReviewCameraDirector::ConfigureReviewMarkers()
{
	UWorld* World = GetWorld();
	if (World == nullptr)
	{
		return;
	}

	const FName ReviewMarkerTag(TEXT("AET_REVIEW_MARKER"));
	const bool bShowReviewMarkers = FParse::Param(FCommandLine::Get(), TEXT("AETReviewMarkers"));
	int32 MarkerCount = 0;

	for (TActorIterator<AActor> It(World); It; ++It)
	{
		AActor* Actor = *It;
		if (Actor == nullptr || !Actor->ActorHasTag(ReviewMarkerTag))
		{
			continue;
		}

		++MarkerCount;
		Actor->SetActorHiddenInGame(!bShowReviewMarkers);
		TArray<UPrimitiveComponent*> Components;
		Actor->GetComponents<UPrimitiveComponent>(Components);
		for (UPrimitiveComponent* Component : Components)
		{
			if (Component == nullptr)
			{
				continue;
			}
			Component->SetHiddenInGame(!bShowReviewMarkers, true);
			Component->SetVisibility(bShowReviewMarkers, true);
		}
	}

	if (MarkerCount > 0)
	{
		UE_LOG(
			LogTemp,
			Display,
			TEXT("AETReviewCameraDirector: %s %d review alignment marker actors."),
			bShowReviewMarkers ? TEXT("showing") : TEXT("hiding"),
			MarkerCount
		);
	}
}

void AAETReviewCameraDirector::ApplyReviewCamera()
{
	UWorld* World = GetWorld();
	if (World == nullptr)
	{
		return;
	}

	APlayerController* PlayerController = World->GetFirstPlayerController();
	if (PlayerController == nullptr)
	{
		UE_LOG(LogTemp, Warning, TEXT("AETReviewCameraDirector: no PlayerController available."));
		return;
	}

	if (!bReviewExposureConfigured)
	{
		PlayerController->ConsoleCommand(TEXT("Slate.bAllowThrottling 0"), true);
		PlayerController->ConsoleCommand(TEXT("t.IdleWhenNotForeground 0"), true);
		PlayerController->ConsoleCommand(TEXT("t.MaxFPS 30"), true);
		PlayerController->ConsoleCommand(TEXT("r.VSync 0"), true);
		PlayerController->ConsoleCommand(TEXT("r.EyeAdaptationQuality 0"), true);
		PlayerController->ConsoleCommand(TEXT("r.DefaultFeature.AutoExposure 0"), true);
		PlayerController->ConsoleCommand(TEXT("r.DefaultFeature.AutoExposure.Bias 0.0"), true);
		PlayerController->ConsoleCommand(TEXT("DisableAllScreenMessages"), true);
		FString ReviewViewMode = TEXT("lit");
		FParse::Value(FCommandLine::Get(), TEXT("AETReviewViewMode="), ReviewViewMode);
		PlayerController->ConsoleCommand(
			FString::Printf(TEXT("viewmode %s"), *ReviewViewMode),
			true
		);
		bReviewExposureConfigured = true;
	}

	for (TActorIterator<ACameraActor> It(World); It; ++It)
	{
		ACameraActor* CameraActor = *It;
		if (CameraActor != nullptr && CameraActor->ActorHasTag(ReviewCameraTag))
		{
			CameraActor->SetActorHiddenInGame(false);
			if (UCameraComponent* CameraComponent = CameraActor->GetCameraComponent())
			{
				CameraComponent->SetVisibility(true, true);
			}
			ConfigureFocusedEncounterCamera(CameraActor);
			PlayerController->SetViewTargetWithBlend(CameraActor, 0.0f);
			UE_LOG(
				LogTemp,
				Display,
				TEXT("AETReviewCameraDirector: applied review camera %s at %s rot=%s."),
				*CameraActor->GetName(),
				*CameraActor->GetActorLocation().ToCompactString(),
				*CameraActor->GetActorRotation().ToCompactString()
			);
			LogReviewViewState(TEXT("after ApplyReviewCamera"), PlayerController);
			return;
		}
	}

	UE_LOG(LogTemp, Warning, TEXT("AETReviewCameraDirector: no camera tagged %s found."), *ReviewCameraTag.ToString());
}

void AAETReviewCameraDirector::UpdateOrbitCamera(float DeltaSeconds)
{
	if (!bOrbitReviewCamera)
	{
		return;
	}

	UWorld* World = GetWorld();
	if (World == nullptr)
	{
		return;
	}

	APlayerController* PlayerController = World->GetFirstPlayerController();
	if (PlayerController == nullptr)
	{
		return;
	}

	OrbitElapsedSeconds += DeltaSeconds;
	OrbitLogElapsedSeconds += DeltaSeconds;
	const float OrbitAngleRadians = FMath::DegreesToRadians(OrbitStartAngleDegrees + (OrbitElapsedSeconds * OrbitSpeedDegreesPerSecond));
	const FVector CameraLocation = OrbitTarget + FVector(
		FMath::Cos(OrbitAngleRadians) * OrbitRadius,
		FMath::Sin(OrbitAngleRadians) * OrbitRadius,
		OrbitHeight
	);
	const FRotator CameraRotation = (OrbitTarget - CameraLocation).Rotation();

	for (TActorIterator<ACameraActor> It(World); It; ++It)
	{
		ACameraActor* CameraActor = *It;
		if (CameraActor == nullptr || !CameraActor->ActorHasTag(ReviewCameraTag))
		{
			continue;
		}

		CameraActor->SetActorHiddenInGame(false);
		CameraActor->SetActorLocation(CameraLocation);
		CameraActor->SetActorRotation(CameraRotation);
		if (UCameraComponent* CameraComponent = CameraActor->GetCameraComponent())
		{
			CameraComponent->SetVisibility(true, true);
			CameraComponent->SetFieldOfView(OrbitFieldOfView);
		}

		PlayerController->SetViewTargetWithBlend(CameraActor, 0.0f);
		if (OrbitLogElapsedSeconds >= 2.0f)
		{
			OrbitLogElapsedSeconds = 0.0f;
			UE_LOG(
				LogTemp,
				Display,
				TEXT("AETReviewCameraDirector: orbit camera tick t=%.2f camera=%s loc=%s rot=%s target=%s."),
				OrbitElapsedSeconds,
				*CameraActor->GetName(),
				*CameraLocation.ToCompactString(),
				*CameraRotation.ToCompactString(),
				*OrbitTarget.ToCompactString()
			);
		}
		return;
	}

	if (!bOrbitCameraMissingLogged)
	{
		bOrbitCameraMissingLogged = true;
		UE_LOG(LogTemp, Warning, TEXT("AETReviewCameraDirector: orbit requested, but no camera tagged %s was found."), *ReviewCameraTag.ToString());
	}
}

void AAETReviewCameraDirector::ConfigureFocusedEncounterCamera(ACameraActor* CameraActor)
{
	if (CameraActor == nullptr || !IsPhaseFocusRequested())
	{
		return;
	}

	EAETGnomeOgreEncounterState RequestedState = EAETGnomeOgreEncounterState::Setup;
	FString RequestedPhaseName;
	if (!TryReadEncounterPhaseCommandLine(RequestedState, RequestedPhaseName))
	{
		return;
	}

	AAETGnomeOgreBattlefieldEncounterActor* EncounterActor = FindGnomeOgreEncounterActor(GetWorld());
	if (EncounterActor == nullptr)
	{
		return;
	}

	FFocusedEncounterCameraSettings CameraSettings;

	switch (RequestedState)
	{
	case EAETGnomeOgreEncounterState::ShieldImpact:
		CameraSettings.FocusActor = EncounterActor->ShieldwallActor.Get();
		CameraSettings.AimOffset = FVector(0.0f, 0.0f, 240.0f);
		CameraSettings.CameraOffset = FVector(1750.0f, -1350.0f, 920.0f);
		CameraSettings.FieldOfView = 48.0f;
		break;
	case EAETGnomeOgreEncounterState::PylonOverload:
		CameraSettings.FocusActor = EncounterActor->PylonObjectiveActor.Get();
		CameraSettings.AimOffset = FVector(0.0f, 0.0f, 50.0f);
		CameraSettings.CameraOffset = FVector(1300.0f, 1150.0f, 1000.0f);
		CameraSettings.FieldOfView = 52.0f;
		CameraSettings.bUseBoundsOrigin = true;
		break;
	case EAETGnomeOgreEncounterState::CasterReinforcement:
		CameraSettings.FocusActor = EncounterActor->OgreShamanActor != nullptr ? EncounterActor->OgreShamanActor.Get() : EncounterActor->OgreNecromancerActor.Get();
		CameraSettings.AimOffset = FVector(0.0f, 0.0f, 140.0f);
		CameraSettings.CameraOffset = FVector(-1500.0f, -1450.0f, 960.0f);
		CameraSettings.FieldOfView = 60.0f;
		break;
	case EAETGnomeOgreEncounterState::ManticoreInterrupt:
		CameraSettings.FocusActor = EncounterActor->ManticoreInterruptActor.Get();
		CameraSettings.AimOffset = FVector(0.0f, 0.0f, 280.0f);
		CameraSettings.CameraOffset = FVector(1550.0f, -1100.0f, 820.0f);
		CameraSettings.FieldOfView = 44.0f;
		break;
	default:
		return;
	}

	if (CameraSettings.FocusActor == nullptr)
	{
		UE_LOG(LogTemp, Warning, TEXT("AETReviewCameraDirector: phase focus requested for %s, but no focus actor is assigned."), ReviewPhaseLogName(RequestedState));
		return;
	}

	FVector FocusOrigin = CameraSettings.FocusActor->GetActorLocation();
	if (CameraSettings.bUseBoundsOrigin)
	{
		FVector BoundsOrigin = FocusOrigin;
		FVector BoundsExtent = FVector::ZeroVector;
		CameraSettings.FocusActor->GetActorBounds(false, BoundsOrigin, BoundsExtent);
		if (!BoundsExtent.IsNearlyZero())
		{
			FocusOrigin = BoundsOrigin;
		}
	}

	const FVector AimLocation = FocusOrigin + CameraSettings.AimOffset;
	const FVector CameraLocation = AimLocation + CameraSettings.CameraOffset;
	CameraActor->SetActorLocation(CameraLocation);
	CameraActor->SetActorRotation((AimLocation - CameraLocation).Rotation());
	if (UCameraComponent* CameraComponent = CameraActor->GetCameraComponent())
	{
		CameraComponent->SetFieldOfView(CameraSettings.FieldOfView);
	}

	UE_LOG(
		LogTemp,
		Display,
		TEXT("AETReviewCameraDirector: focused review camera on %s for phase %s at %s rot=%s aim=%s fov=%.1f."),
		*GetNameSafe(CameraSettings.FocusActor),
		ReviewPhaseLogName(RequestedState),
		*CameraActor->GetActorLocation().ToCompactString(),
		*CameraActor->GetActorRotation().ToCompactString(),
		*AimLocation.ToCompactString(),
		CameraSettings.FieldOfView
	);
}

void AAETReviewCameraDirector::MarkScreenshotDelayElapsed()
{
	bScreenshotDelayElapsed = true;
	TryRequestReviewScreenshot();
}

void AAETReviewCameraDirector::TryRequestReviewScreenshot()
{
	if (!bCaptureReviewScreenshot || bReviewScreenshotRequested || !bScreenshotDelayElapsed)
	{
		return;
	}

	if (RemainingWarmupFrames > 0)
	{
		return;
	}

	RequestReviewScreenshot();
}

void AAETReviewCameraDirector::RequestReviewScreenshot()
{
	if (bReviewScreenshotRequested)
	{
		return;
	}
	bReviewScreenshotRequested = true;

	ApplyReviewCamera();

	UWorld* World = GetWorld();
	if (World == nullptr)
	{
		return;
	}

	APlayerController* PlayerController = World->GetFirstPlayerController();
	if (PlayerController == nullptr)
	{
		UE_LOG(LogTemp, Warning, TEXT("AETReviewCameraDirector: cannot capture review screenshot without a PlayerController."));
		return;
	}

	const int32 ClampedWidth = FMath::Max(1, ScreenshotWidth);
	const int32 ClampedHeight = FMath::Max(1, ScreenshotHeight);
	FString FilenameOverride = ScreenshotFilenameOverride;
	FParse::Value(
		FCommandLine::Get(),
		TEXT("AETReviewCaptureFile="),
		FilenameOverride
	);
	const bool bHasFilenameOverride = !FilenameOverride.IsEmpty();
	const FString Command = bHasFilenameOverride
		? FString::Printf(TEXT("HighResShot %dx%d filename=\"%s\""), ClampedWidth, ClampedHeight, *FilenameOverride)
		: FString::Printf(TEXT("HighResShot %dx%d"), ClampedWidth, ClampedHeight);
	LogReviewViewState(TEXT("before HighResShot"), PlayerController);
	PlayerController->ConsoleCommand(Command, true);
	UE_LOG(LogTemp, Display, TEXT("AETReviewCameraDirector: requested runtime review screenshot with %s."), *Command);

	if (FParse::Param(FCommandLine::Get(), TEXT("AETReviewCaptureExit")))
	{
		PostScreenshotExitFrames = 90;
	}
}

void AAETReviewCameraDirector::RequestReviewExit()
{
	UE_LOG(LogTemp, Display, TEXT("AETReviewCameraDirector: exiting after runtime review screenshot request."));
	FPlatformMisc::RequestExit(false);
}
