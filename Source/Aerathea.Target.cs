using UnrealBuildTool;

public class AeratheaTarget : TargetRules
{
	public AeratheaTarget(TargetInfo Target) : base(Target)
	{
		Type = TargetType.Game;
		DefaultBuildSettings = BuildSettingsVersion.Latest;
		IncludeOrderVersion = EngineIncludeOrderVersion.Latest;
		ExtraModuleNames.Add("Aerathea");
	}
}
