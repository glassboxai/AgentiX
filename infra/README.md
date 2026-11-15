# AgentiX Windows Infrastructure as Code

## Supported profile and ownership

IAC-001 manages a Windows 11 x64 local engineering environment for one standard user.
It uses a native DSC 3.3.0 command resource, PowerShell and a WinGet-backed Python
provider. Python stays at 3.11.9 by explicit user choice; its age/security limitations
are not resolved by IaC. Ollama is an external local dependency: the user installs,
updates and starts it, and manages its models. IaC neither observes nor provisions its
binary, service, version or model catalog.

The profile declares exact prerequisites in windows.local.json. runtime.lock.txt pins
158 Python packages, including transitive dependencies, pip and verification tools,
with hashes of Windows x64/CPython 3.11-compatible wheels from PyPI. A changed lock
selects a new environment directory instead of overwriting an older environment.
This local engineering profile intentionally includes pytest, Ruff and Playwright.

Windows App Installer/WinGet >=1.6.2631 is an OS prerequisite when Python is absent.
If missing or blocked, Plan diagnoses that prerequisite; it does not silently install
or repair Windows components or ask for elevation. Python installation uses user scope,
x64, no PATH modification, file association, launcher or shortcuts. Ollama must be
installed and operated independently before a user selects a local model in the GUI.

## Review and apply

Run in a normal PowerShell session from the AgentiX v7 checkout:

```powershell
.\infra\Invoke-AgentiXIac.ps1 -Action Plan -OutFile .\deployment.plan.json
Get-Content .\deployment.plan.json
.\infra\Invoke-AgentiXIac.ps1 -Action Apply -PlanFile .\deployment.plan.json
.\infra\Invoke-AgentiXIac.ps1 -Action Test
```

Plan only observes state. OutFile explicitly writes the requested JSON report; no
requirements, configuration or tool storage are modified. Review changes, blockers,
warnings, prerequisite identities and the pinned source/configuration fingerprints.
Apply requires that exact plan. Changed source, configuration, observations or actions
require a fresh Plan. Plan digests are change-detection evidence, not signatures or
an authorization boundary against an attacker who already controls this user account.

Apply verifies prerequisites, bootstraps the pinned private DSC distribution if absent,
and delegates convergence to AgentiX.Local/Deployment. The resource supplies native
DSC get/test/set operations. It installs only planned resources in dependency order and
checks postconditions before proceeding. Failed prerequisites stop dependent work.
A successful installer exit alone does not establish convergence. Test is read-only;
its exit code is 0 for desired state and 2 for drift; failures use exit code 1.

All managed native binaries must have valid signatures from their expected publishers.
The DSC archive has a committed SHA-256 pin and member-path containment checks; WinGet
verifies the Python installer against its package manifest. Python installation
ignores ambient pip configuration and write targets, uses the hash lock and runs
pip check. Process configuration is restored after installation and manual startup.
Unknown configuration fields and unsupported managed versions are rejected. No automatic
upgrade or version fallback is performed for managed dependencies.

## Local model availability and trust

Install and start Ollama independently, then download any required models with its own
CLI or GUI. IaC Plan, Apply and Test do not contact Ollama and remain usable offline.
When a saved local profile first generates an application, AgentiX reads the selected
loopback `/api/tags` catalog and stores that model's digest as a TOFU baseline. This is
local change detection, not proof of publisher authenticity. Later generation requires
the same digest. A changed or unavailable digest blocks generation until the developer
uses the explicit **Reset trusted generation identity** control after reviewing it.
Neither IaC nor AgentiX downloads, starts, updates or replaces Ollama or its models.

## Managed locations and manual startup

The schema-2 `windows.local.json` profile declares separate reviewed local paths
for the runtime home and generated artifacts. The current approved values are
`D:\AI\Agentix-data\v7` and `D:\AI\AgentiX_v7\generated_tools` respectively.
IaC rejects relative/UNC/traversing/volume-root paths, existing reparse points
and root overlap before planning. An owner-scoped, untracked
`infra/.local-paths.<SID>.<home-hash>.json` receipt records the exact configured
home for launch diagnostics; it is an explicit desired-state resource, not a
source configuration or approval capability. Inspect the reviewed paths rather
than hardcoding another user's cache directory:

```powershell
Import-Module .\infra\Agentix.Iac.psm1 -Force
$deploymentPaths = Get-IacPaths (Read-IacConfiguration)
$deploymentPaths | ConvertTo-Json
& (Join-Path $deploymentPaths.launchers 'Start-Gui.ps1')
# Alternatively:
& (Join-Path $deploymentPaths.launchers 'Start-Cli.ps1')
```

The launchers use the new environment's exact Python executable and pass its physical
AGENTIX_HOME to every service. They do not recheck or start Ollama.
GUI uses 127.0.0.1:7878 and fails if occupied. It never terminates another listener or
chooses a random port. Provisioning starts neither GUI nor CLI. Startup is manual;
openBrowser controls whether that manual GUI launch opens the local browser.

Managed runtime/state goes below `home`; generated artifacts go only below
`toolsRoot`. Engineering never scans existing artifact contents. Normal application
behavior may generate and use tools there with native isolation and manual acceptance.
No V5 data or existing generated artifacts are copied. The reviewed settings are
`home`, `toolsRoot`, `AGENTIX_SERVER_PORT` and `AGENTIX_OPEN_BROWSER`; paths are
validated before planning and launch.

## Diagnostics, idempotence and recovery

Structured infrastructure logs contain operation/resource identities, outcome and
elapsed seconds, not prompts, artifact bodies, command credentials or environment values.
The infrastructure log rotates at 1 MiB with four retained rotations. Diagnostic output
from a failed prerequisite is truncated. Native prerequisite commands have a 20-minute
wrapper deadline. External package installations and detached installer children are not
transactional; inspect their state
after a timeout or interruption before retrying. There is no claim of automatic rollback.

An unchanged Plan has an empty changes array. Reapplying it must not reinstall packages,
recreate the environment, rewrite launchers or append resource-change events. Existing
managed paths and their ancestors cannot be reparse points. An existing environment
without the ownership marker is refused; it is never cleared or adopted. The marker is
ownership metadata, not an execution authorization capability. Convergence checks actual
interpreter identity and required package versions; it is not a full installed-file
integrity monitor. Runtime isolation/approval policies remain separate requirements.

On partial installation failure, retain logs, repair the diagnosed prerequisite and
create a fresh plan. An owned incomplete environment may be completed on retry. A bad
archive or invalid signature is not bypassed; retain evidence and obtain a verified
replacement through the reviewed definitions. Old environments and user data are not
automatically removed. No uninstaller, graphical application installer, firewall rule,
security exclusion, service, task or automatic application startup is supplied.

## Verification

Use the managed interpreter for the application suite:

```powershell
$managedPython = Join-Path $deploymentPaths.environment 'Scripts\python.exe'
& $managedPython -m pytest
& $managedPython -m pytest -m windows_credentials
& $managedPython -m pytest -m frameworks
& $managedPython -m pytest -m windows_isolation
& $managedPython -m pytest -m browser
& $managedPython -m ruff check src tests tools infra app.py main.py config.py custom_tools.py security_manager.py _agentix_path.py
& $managedPython -m ruff format --check src tests tools infra app.py main.py config.py custom_tools.py security_manager.py _agentix_path.py
& $managedPython tools/build_reference.py --check
.\infra\Verify-Infrastructure.ps1
```

Ordinary infrastructure tests use temporary paths and doubled installers/network providers;
explicit process/PowerShell compatibility tests use trusted snippets only. PowerShell
verification parses ASTs and enforces a narrow command policy; it is not PSScriptAnalyzer,
Pester or a complete security proof. Source references include all maintained PowerShell
functions and scoped variable names without executing those files or exporting values.
Native DSC/provisioning evidence is separate from offline checks. The current-machine
parallel application proves a fresh venv using existing prerequisites; it does not prove
installation of every missing requirement on a clean Windows machine. See
../docs/reports/IAC_IMPLEMENTATION.md for actual results and outstanding limitations.
