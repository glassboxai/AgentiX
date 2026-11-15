<#
.SYNOPSIS
Plan, apply or test the reviewed Windows-user AgentiX deployment.
.DESCRIPTION
Plan/Test do not install or download anything. OutFile explicitly saves their JSON.
Apply requires a reviewed PlanFile. Ollama is externally managed.
LaunchGui/LaunchCli are manual actions, never invoked by provisioning.
#>
[CmdletBinding()]
param(
    [ValidateSet('Plan','Apply','Test','LaunchGui','LaunchCli')][string]$Action='Plan',
    [string]$PlanFile,
    [string]$OutFile
)
$ErrorActionPreference='Stop'
try {
    Import-Module (Join-Path $PSScriptRoot 'Agentix.Iac.psm1') -Force
    $config=Read-IacConfiguration
    switch ($Action) {
        'Plan' { $result=Get-IacPlan -Config $config -State (Get-IacState $config) }
        'Test' { $result=Test-IacDeployment $config }
        'Apply' {
            if (-not $PlanFile) { throw 'Apply requires PlanFile.' }
            $plan=ConvertTo-IacMap (Get-Content -LiteralPath $PlanFile -Raw | ConvertFrom-Json)
            Invoke-IacApply $plan $config
            $result=Test-IacDeployment $config
        }
        'LaunchGui' { Start-IacApplication $config 'Gui';exit 0 }
        'LaunchCli' { Start-IacApplication $config 'Cli';exit 0 }
    }
    $json=ConvertTo-Json -InputObject $result -Depth 60
    if ($OutFile) { [IO.File]::WriteAllText([IO.Path]::GetFullPath($OutFile),$json,[Text.UTF8Encoding]::new($false)) }
    Write-Output $json
    if ($Action -eq 'Test' -and -not $result.inDesiredState) { exit 2 }
    exit 0
} catch { Write-Error -Message $_.Exception.Message -ErrorAction Continue;exit 1 }
