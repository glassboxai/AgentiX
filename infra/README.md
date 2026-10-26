# AgentiX Windows Infrastructure as Code

## Supported profile and ownership

IAC-001 manages a Windows 11 x64 local engineering environment for one standard user.
It uses a native DSC 3.3.0 command resource, PowerShell and a WinGet-backed Python
provider. Python stays at 3.11.9 by explicit user choice; its age/security limitations
are not resolved by IaC. Ollama is pinned to 0.40.6 and the default provisioned model is
ollama/qwen3-coder:30b with its reviewed SHA-256 content digest. The GUI may explicitly select other installed or external models under SEC-LLM-001; IaC provisions and verifies only the pinned local default.

The profile declares exact prerequisites in windows.local.json. runtime.lock.txt pins
158 Python packages, including transitive dependencies, pip and verification tools,
with hashes of Windows x64/CPython 3.11-compatible wheels from PyPI. A changed lock
selects a new environment directory instead of overwriting an older environment.
This local engineering profile intentionally includes pytest, Ruff and Playwright.

Windows App Installer/WinGet >=1.6.2631 is an OS prerequisite when Python is absent.
If missing or blocked, Plan diagnoses that prerequisite; it does not silently install
or repair Windows components or ask for elevation. Existing compatible Python/Ollama
installations are reused without being adopted, upgraded or uninstalled. Their observed
identities are bound to the reviewed plan. Python installation uses user scope, x64,
no PATH modification, file association, launcher or shortcuts. Missing Ollama uses
the official portable archive; it creates no service or automatic startup entry.

## Review and apply

Run in a normal PowerShell session from the AgentiX v3 checkout:

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

All native binaries must have valid signatures from their expected publishers. DSC
and Ollama archives have committed SHA-256 pins and member-path containment checks;
WinGet verifies the Python installer against its package manifest. Python installation
ignores ambient pip configuration and write targets, uses the hash lock and runs
pip check. Process configuration is restored after installation and manual startup.
Unknown configuration fields, unsupported versions and non-loopback model endpoints
are rejected. No automatic upgrade or version fallback is performed.

## Model availability

Plan never downloads a model. If the required model is missing from a running compatible
local server, explicitly authorize its download by creating a different reviewed plan:

```powershell
.\infra\Invoke-AgentiXIac.ps1 -Action Plan -DownloadModel -OutFile .\model.plan.json
Get-Content .\model.plan.json
.\infra\Invoke-AgentiXIac.ps1 -Action Apply -PlanFile .\model.plan.json
```

The download uses only the configured loopback API and the required model tag. The
resulting digest must match the pin. A changed installed digest blocks the plan rather
than silently replacing the model. Updating pins is a reviewed engineering change.

IaC never starts or restarts Ollama. If it is offline, file preparation may complete,
but deployment remains incomplete until an operator manually starts the pinned server.
For a newly prepared portable installation, inspect Get-IacPaths and explicitly run its
privateOllama executable with OLLAMA_HOST set to 127.0.0.1:11434 and the serve argument.
Then generate a fresh plan. Keep that server terminal open as appropriate; no persistent
service or login task is created. The same rule applies on a fresh Windows machine.

## Managed locations and manual startup

The logical root is LOCALAPPDATA/AgentiX/v3. Windows packaged hosts can virtualize this
folder. IaC resolves an existing root through the trusted CPython runtime and uses its
physical location, avoiding launchers that depend on a host-specific alias. An owner-scoped, untracked infra/.local-paths.<SID>.<home-hash>.json receipt preserves this location for normal terminals outside that host. It is an explicit desired-state resource, not a source configuration or approval capability. Inspect the
actual paths rather than hardcoding another user's application-cache directory:

```powershell
Import-Module .\infra\Agentix.Iac.psm1 -Force
$deploymentPaths = Get-IacPaths (Read-IacConfiguration)
$deploymentPaths | ConvertTo-Json
& (Join-Path $deploymentPaths.launchers 'Start-Gui.ps1')
# Alternatively:
& (Join-Path $deploymentPaths.launchers 'Start-Cli.ps1')
```

The launchers use the new environment's exact Python executable and recheck prerequisites.
GUI uses 127.0.0.1:7873 and fails if occupied. It never terminates another listener or
chooses a random port. Provisioning starts neither GUI nor CLI. Startup is manual;
openBrowser controls whether that manual GUI launch opens the local browser.

Managed runtime data goes to the new root's data/tools directory. Engineering never
scans its contents or the original generated_tools directory. Normal application
behavior may generate and use tools there with native isolation and manual acceptance.
No existing generated artifacts are copied. Legacy launchers retain port 7860, their
checkout-relative storage and browser behavior unless explicit settings are supplied.
The new settings are AGENTIX_SERVER_PORT, AGENTIX_OPEN_BROWSER and AGENTIX_TOOLS_ROOT;
ports and booleans are validated and the storage override must be absolute.

## Diagnostics, idempotence and recovery

Structured infrastructure logs contain operation/resource identities, outcome and
elapsed seconds, not prompts, artifact bodies, command credentials or environment values.
The infrastructure log rotates at 1 MiB with four retained rotations. Diagnostic output
from a failed prerequisite is truncated. Native prerequisite commands have a 20-minute
wrapper deadline; model download has a separate explicit API deadline. External package
installations and detached installer children are not transactional; inspect their state
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
