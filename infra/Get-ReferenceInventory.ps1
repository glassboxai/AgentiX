<#
.SYNOPSIS
Parse maintained infrastructure source into a JSON documentation inventory.
.DESCRIPTION
Uses the PowerShell AST without dot-sourcing or running the inspected files.
Only sibling ps1/psm1 files are considered. Values and secrets are never exported.
#>
$ErrorActionPreference='Stop'
$inventory=@()
foreach ($file in Get-ChildItem -LiteralPath $PSScriptRoot -File | Where-Object Extension -In '.ps1','.psm1') {
    if ($file.Attributes -band [IO.FileAttributes]::ReparsePoint) { throw 'Linked infrastructure source is not supported.' }
    $tokens=$null;$parseErrors=$null
    $ast=[Management.Automation.Language.Parser]::ParseFile($file.FullName,[ref]$tokens,[ref]$parseErrors)
    if (@($parseErrors).Count) { throw ('PowerShell parse errors in '+$file.Name) }
    $functions=@()
    foreach ($node in $ast.FindAll({param($item) $item -is [Management.Automation.Language.FunctionDefinitionAst]},$true)) {
        $help=$node.Body.GetHelpContent()
        $synopsis='See the module contract.';if ($help -and $help.Synopsis) {$synopsis=$help.Synopsis.Trim()}
        $functions+=@{name=$node.Name;line=$node.Extent.StartLineNumber;contract=$synopsis}
    }
    $variables=@{}
    foreach ($node in $ast.FindAll({param($item) $item -is [Management.Automation.Language.VariableExpressionAst]},$true)) {
        $scope='module';$parent=$node.Parent
        while ($parent) { if ($parent -is [Management.Automation.Language.FunctionDefinitionAst]) {$scope=$parent.Name;break};$parent=$parent.Parent }
        $name=$node.VariablePath.UserPath
        $variables[$scope+'::'+$name]=@{name=$name;scope=$scope;type=$node.StaticType.FullName;lifecycle='Enclosing invocation, unless explicitly process/environment or script scoped.'}
    }
    $inventory+=@{source=('infra/'+$file.Name);contract=($ast.GetHelpContent().Synopsis.Trim());functions=$functions;variables=@($variables.GetEnumerator()|Sort-Object Key|ForEach-Object Value)}
}
ConvertTo-Json -InputObject @($inventory|Sort-Object source) -Depth 12
