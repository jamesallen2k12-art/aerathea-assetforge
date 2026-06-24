using UnrealBuildTool;

public class AeratheaEditorTarget : TargetRules
{
	public AeratheaEditorTarget(TargetInfo Target) : base(Target)
	{
		Type = TargetType.Editor;
		DefaultBuildSettings = BuildSettingsVersion.Latest;
		IncludeOrderVersion = EngineIncludeOrderVersion.Latest;
		ExtraModuleNames.Add("Aerathea");
	}
}
