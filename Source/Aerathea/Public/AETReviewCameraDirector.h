#pragma once

#include "CoreMinimal.h"
#include "GameFramework/Actor.h"
#include "AETReviewCameraDirector.generated.h"

class ACameraActor;

UCLASS(Blueprintable)
class AERATHEA_API AAETReviewCameraDirector : public AActor
{
	GENERATED_BODY()

public:
	AAETReviewCameraDirector();

protected:
	virtual void Tick(float DeltaSeconds) override;
	virtual void BeginPlay() override;
	virtual void EndPlay(const EEndPlayReason::Type EndPlayReason) override;

	UPROPERTY(EditAnywhere, BlueprintReadWrite, Category = "Aerathea|Review")
	FName ReviewCameraTag;

	UPROPERTY(EditAnywhere, BlueprintReadWrite, Category = "Aerathea|Review")
	bool bCaptureReviewScreenshot;

	UPROPERTY(EditAnywhere, BlueprintReadWrite, Category = "Aerathea|Review", meta = (EditCondition = "bCaptureReviewScreenshot", ClampMin = "1"))
	int32 ScreenshotWidth;

	UPROPERTY(EditAnywhere, BlueprintReadWrite, Category = "Aerathea|Review", meta = (EditCondition = "bCaptureReviewScreenshot", ClampMin = "1"))
	int32 ScreenshotHeight;

	UPROPERTY(EditAnywhere, BlueprintReadWrite, Category = "Aerathea|Review", meta = (EditCondition = "bCaptureReviewScreenshot"))
	FString ScreenshotFilenameOverride;

	UPROPERTY(EditAnywhere, BlueprintReadWrite, Category = "Aerathea|Review", meta = (EditCondition = "bCaptureReviewScreenshot", ClampMin = "0.2"))
	float ScreenshotDelaySeconds;

	UPROPERTY(EditAnywhere, BlueprintReadWrite, Category = "Aerathea|Review", meta = (EditCondition = "bCaptureReviewScreenshot", ClampMin = "1"))
	int32 ScreenshotWarmupFrames;

	UFUNCTION(BlueprintCallable, Category = "Aerathea|Review")
	void ApplyReviewCamera();

	UFUNCTION(BlueprintCallable, Category = "Aerathea|Review")
	void RequestReviewScreenshot();

private:
	void ConfigureCommandLineOptions();
	void ConfigureEncounterReviewPhase();
	void ConfigureFocusedEncounterCamera(class ACameraActor* CameraActor);
	void ConfigureReviewMarkers();
	void UpdateOrbitCamera(float DeltaSeconds);
	void MarkScreenshotDelayElapsed();
	void TryRequestReviewScreenshot();
	void RequestReviewExit();

	bool bReviewScreenshotRequested;
	bool bScreenshotDelayElapsed;
	bool bReviewExposureConfigured;
	bool bOrbitReviewCamera;
	float CaptureElapsedSeconds;
	float OrbitElapsedSeconds;
	float OrbitStartAngleDegrees;
	float OrbitSpeedDegreesPerSecond;
	float OrbitRadius;
	float OrbitHeight;
	float OrbitFieldOfView;
	float OrbitLogElapsedSeconds;
	FVector OrbitTarget;
	bool bOrbitCameraMissingLogged;
	int32 RemainingWarmupFrames;
	int32 PostScreenshotExitFrames;

	FTimerHandle ScreenshotTimerHandle;
	FTimerHandle ExitTimerHandle;

};
