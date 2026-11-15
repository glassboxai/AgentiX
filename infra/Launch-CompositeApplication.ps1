<#
.SYNOPSIS
Manually launch the reviewed composite GUI using the exact managed Lab interpreter.
.DESCRIPTION
Does not require the Lab GUI or Ollama. No activation, PATH change or provisioning.
The Python supervisor enforces explicit-port failure, review and native isolation.
#>
[CmdletBinding()]
param(
    [ValidateRange(1024,65535)][int]$Port=7876,
    [ValidateRange(0,300)][int]$Duration=0
)
$ErrorActionPreference='Stop'
Import-Module (Join-Path $PSScriptRoot 'Agentix.Iac.psm1') -Force
$config=Read-IacConfiguration
$paths=Get-IacPaths $config
$state=Get-IacEnvironmentState $config $paths
if (-not $state.present) { throw 'Managed Lab environment is missing or has drifted. Review IaC Test/Plan before provisioning.' }
$interpreter=Join-Path $paths.environment 'Scripts\python.exe'
$entry=Join-Path (Split-Path $PSScriptRoot -Parent) 'application_launch.py'
& $interpreter $entry --port $Port --duration $Duration
exit $LASTEXITCODE
