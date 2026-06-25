#include "AETReviewCameraDirector.h"

#include "Camera/CameraActor.h"
#include "Camera/CameraComponent.h"
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
	ScreenshotDelaySeconds = 0.5f;
	ScreenshotWarmupFrames = 10;
	bReviewScreenshotRequested = false;
	bScreenshotDelayElapsed = false;
	bReviewExposureConfigured = false;
	RemainingWarmupFrames = INDEX_NONE;
}

void AAETReviewCameraDirector::BeginPlay()
{
	Super::BeginPlay();

	bCaptureReviewScreenshot = bCaptureReviewScreenshot || FParse::Param(FCommandLine::Get(), TEXT("AETReviewCapture"));

	ApplyReviewCamera();

	if (UWorld* World = GetWorld())
	{
		World->GetTimerManager().SetTimerForNextTick(this, &AAETReviewCameraDirector::ApplyReviewCamera);
		if (bCaptureReviewScreenshot)
		{
			World->GetTimerManager().SetTimer(
				ScreenshotTimerHandle,
				this,
				&AAETReviewCameraDirector::MarkScreenshotDelayElapsed,
				FMath::Max(0.2f, ScreenshotDelaySeconds),
				false
			);
		}
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
		return;
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
		PlayerController->ConsoleCommand(TEXT("r.EyeAdaptationQuality 0"), true);
		PlayerController->ConsoleCommand(TEXT("r.DefaultFeature.AutoExposure 0"), true);
		PlayerController->ConsoleCommand(TEXT("DisableAllScreenMessages"), true);
		PlayerController->ConsoleCommand(TEXT("viewmode unlit"), true);
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
	const FString Command = FString::Printf(TEXT("HighResShot %dx%d"), ClampedWidth, ClampedHeight);
	LogReviewViewState(TEXT("before HighResShot"), PlayerController);
	PlayerController->ConsoleCommand(Command, true);
	UE_LOG(LogTemp, Display, TEXT("AETReviewCameraDirector: requested runtime review screenshot with %s."), *Command);

	if (FParse::Param(FCommandLine::Get(), TEXT("AETReviewCaptureExit")))
	{
		if (UWorld* TimerWorld = GetWorld())
		{
			TimerWorld->GetTimerManager().SetTimer(
				ExitTimerHandle,
				this,
				&AAETReviewCameraDirector::RequestReviewExit,
				2.0f,
				false
			);
		}
	}
}

void AAETReviewCameraDirector::RequestReviewExit()
{
	UE_LOG(LogTemp, Display, TEXT("AETReviewCameraDirector: exiting after runtime review screenshot request."));
	FPlatformMisc::RequestExit(false);
}
