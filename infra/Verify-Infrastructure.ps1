<#
.SYNOPSIS
Statically validate maintained PowerShell syntax and security-sensitive command usage.
.DESCRIPTION
AST parsing does not execute infrastructure. This gate complements provider tests;
it is not a complete security analyzer or a replacement for integration evidence.
#>
$ErrorActionPreference='Stop'
$count=0
foreach ($file in Get-ChildItem -LiteralPath $PSScriptRoot -File | Where-Object Extension -In '.ps1','.psm1') {
    $tokens=$null;$parseErrors=$null
    $ast=[Management.Automation.Language.Parser]::ParseFile($file.FullName,[ref]$tokens,[ref]$parseErrors)
    if (@($parseErrors).Count) { throw ($parseErrors|Out-String) }
    if (-not $ast.GetHelpContent()) { throw ('Missing module contract: '+$file.Name) }
    foreach ($node in $ast.FindAll({param($item) $item -is [Management.Automation.Language.CommandAst]},$true)) {
        $command=$node.GetCommandName()
        if ($command -in @('Invoke-Expression','iex','Stop-Process','Set-ExecutionPolicy','New-NetFirewallRule','Register-ScheduledTask','New-Service')) { throw ('Forbidden infrastructure command: '+$command) }
    }
    foreach ($node in $ast.FindAll({param($item) $item -is [Management.Automation.Language.FunctionDefinitionAst]},$true)) {
        if (-not $node.Body.GetHelpContent()) { throw ('Missing function contract: '+$node.Name) }
    }
    $count++
}
@{powershellFiles=$count;syntax='passed';commandPolicy='passed';limitations='Static policy, not a full security proof.'}|ConvertTo-Json
