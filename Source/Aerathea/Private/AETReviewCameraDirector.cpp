#include "AETReviewCameraDirector.h"

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
	CaptureElapsedSeconds = 0.0f;
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
	PostScreenshotExitFrames = INDEX_NONE;

	ConfigureReviewMarkers();
	ApplyReviewCamera();

	if (UWorld* World = GetWorld())
	{
		World->GetTimerManager().SetTimerForNextTick(this, &AAETReviewCameraDirector::ApplyReviewCamera);
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

void AAETReviewCameraDirector::Tick(float DeltaSeconds)
{
	Super::Tick(DeltaSeconds);

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
