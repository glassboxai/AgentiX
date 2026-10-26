<#
.SYNOPSIS
DSC command-resource get/test/set bridge for the fixed Windows-user profile.
.DESCRIPTION
Set accepts only a complete reviewed plan supplied by the parent Apply operation.
It rechecks preconditions and runs the same dependency-injected convergence service.
#>
param([ValidateSet('get','test','set')][string]$Operation)
$ErrorActionPreference='Stop'
try {
    Import-Module (Join-Path $PSScriptRoot 'Agentix.Iac.psm1') -Force
    $inputText=[Console]::In.ReadToEnd()
    $desired=$inputText|ConvertFrom-Json
    if ($desired.profile -ne 'windows-user') { throw 'Unsupported DSC profile.' }
    $config=Read-IacConfiguration
    if ($Operation -eq 'set') {
        if (-not $env:AGENTIX_IAC_REVIEW) { throw 'DSC set requires a reviewed plan from Invoke-AgentiXIac.ps1.' }
        $review=ConvertTo-IacMap ($env:AGENTIX_IAC_REVIEW|ConvertFrom-Json)
        Invoke-IacConverge -Config $config -Plan $review -DscBootstrapped | Out-Null
    }
    $test=Test-IacDeployment $config
    if ($Operation -eq 'set' -and -not $test.inDesiredState) { throw 'Prerequisites incomplete; start Ollama manually if it is offline, then replan.' }
    $state=@{profile='windows-user';inDesiredState=[bool]$test.inDesiredState}
    if ($Operation -eq 'test') { $state['_inDesiredState']=[bool]$test.inDesiredState }
    ConvertTo-Json $state -Compress
    exit 0
} catch { [Console]::Error.WriteLine($_.Exception.Message);[Console]::Error.WriteLine($_.ScriptStackTrace);exit 1 }
