# AgentiX v7 installation and launch

## Scope and prerequisites

This guide applies to the AgentiX v7 source checkout. Run commands from that
checkout with a normal, non-elevated Windows user. IaC manages the AgentiX
Python runtime, pinned dependencies, DSC and launchers; it does not install,
start, update or download Ollama or its models.

Install, start and manage Ollama separately. Before application generation,
ensure that the selected local model is available from the configured loopback
endpoint. No Docker, service, automatic startup or global PATH modification is
performed by AgentiX IaC.

## Check an existing installation

Set the checkout path for the current machine, then run the read-only check:

```powershell
$repoRoot = 'D:\AI\AgentiX_v7'
Set-Location $repoRoot
.\infra\Invoke-AgentiXIac.ps1 -Action Test
```

`inDesiredState: true` means the managed AgentiX resources are ready. This
check deliberately does not contact Ollama.

## Prepare a missing or drifted installation

Only if `Test` reports drift or missing managed resources, create and review a
plan before applying it:

```powershell
$repoRoot = 'D:\AI\AgentiX_v7'
Set-Location $repoRoot
.\infra\Invoke-AgentiXIac.ps1 -Action Plan -OutFile .\agentix-v7.plan.json
Get-Content .\agentix-v7.plan.json
.\infra\Invoke-AgentiXIac.ps1 -Action Apply -PlanFile .\agentix-v7.plan.json
.\infra\Invoke-AgentiXIac.ps1 -Action Test
```

Apply accepts only the reviewed, current plan. Source, configuration, or
managed-state drift requires a new plan. Managed Python and DSC downloads use
pinned integrity checks. Ollama and its models are never downloaded, installed,
updated or selected by IaC.

### Resolve a stale or mismatched plan

If Apply reports `Reviewed plan is stale or modified`, do not reuse the plan
file. Confirm that the plan printed by `Plan` and the saved file have the same
`source`, `state` and `changes` values. A different file is an earlier plan and
cannot be applied safely. Generate, review and apply a newly named plan without
changing the checkout or managed state between these commands:

```powershell
$planFile = Join-Path $PWD 'agentix-v7-current.plan.json'
.\infra\Invoke-AgentiXIac.ps1 -Action Plan -OutFile $planFile
Get-Content $planFile
.\infra\Invoke-AgentiXIac.ps1 -Action Apply -PlanFile $planFile
.\infra\Invoke-AgentiXIac.ps1 -Action Test
```

Review the new plan before Apply: it must contain no `blockers`, and its
`changes` must be expected. If the final Test does not report
`inDesiredState: true`, do not launch the GUI; diagnose that result first.

Apply displays concise reviewed-stage messages in the invoking PowerShell
console. The infrastructure process can forward labeled native stdout and stderr
lines while a child runs, retaining bounded diagnostics and the existing exit
rules. Apply summarizes successful DSC completion and resource counts instead
of printing its machine JSON. The DSC resource still reserves stdout for its
JSON contract; detailed output from commands it starts is not bridged in this
phase.

During environment convergence, IaC uses that environment's locked Playwright
package to resolve the exact Chromium revision it requires. If the matching
binary is absent, it runs `python -m playwright install chromium` with the
managed virtual-environment Python. A compatible existing browser is reused;
Firefox and WebKit are not installed. A download failure, or a missing matching
binary after download, fails Apply with a Chromium-specific diagnostic. At
launch, `AGENTIX_PLAYWRIGHT_EXECUTABLE` is set to this resolved browser when it
is available; an existing caller value is otherwise preserved.

## Explicit in-app host dependency recovery

IaC `Apply` remains the normal way to prepare the environment. If a separately
launched GUI finds that its browser-acceptance Chromium is missing, the pending
application review explains the requirement and shows **Install required host
dependency**. The button is an explicit per-action confirmation: it invokes only
the active AgentiX Python with `-I -m playwright install chromium`, then verifies
the Playwright-selected executable. It does not install Python packages, other
browsers, Ollama, models, Tools or applications.

The control is shown only to the owner of the unchanged pending review. A failed
or declined installation leaves that review pending and reports no raw installer
output. After a successful installation, inspect the retained review and click
**Approve and verify** again; AgentiX never replays the previous approval click.
Future recovery entries require a separately reviewed host-owned registry change.

### Application-review flow

1. Select **Approve and verify** after completing the normal source and
   acceptance review.
2. If the browser requirement is missing, AgentiX opens an informational message.
   Select **Ok** only to dismiss that message: **Ok does not authorize or start
   an installation**.
3. In the Applications workspace, below the review action buttons, read the
   host-requirement explanation and select **Install required host dependency**.
   This button is the explicit consent to download the reviewed Chromium
   requirement.
4. Wait for the bounded installation result. A success message confirms that the
   executable was found; a failure leaves the same review pending and does not
   install a substitute.
5. Recheck the retained review and select **Approve and verify** once more to
   start native and browser acceptance. The initial approval is never replayed.

Operational logs intentionally bound long reason text. A truncated `reason=`
field can confirm that a dependency was detected, but it does not show that an
installation began. The `host_dependency_install_started` event marks the
explicit installation action; `host_dependency_install_verified` marks a
successfully rechecked result.

## Launch

Start Ollama independently if the local model workflow will be used, then launch
the GUI from the v7 checkout:

```powershell
$repoRoot = 'D:\AI\AgentiX_v7'
Set-Location $repoRoot
.\infra\Invoke-AgentiXIac.ps1 -Action LaunchGui
```

The GUI uses the configured loopback address and port 7878. Keep the launching
terminal open; Ctrl+C closes its owned host. A port conflict fails closed and
does not terminate another process. Use `LaunchCli` instead of `LaunchGui` for
terminal operation.

In the GUI, save and apply a local Ollama profile before generating an
application. The first generation records the selected model digest as a local
TOFU baseline. It detects later local changes but does not prove model
authenticity. A missing or changed digest blocks generation until the developer
explicitly resets the trusted generation identity.

### Resolving Gradio Port Conflicts

If AgentiX fails to start with `OSError: Cannot find empty port in range: 7878-7878`, a previous instance may still be running.

**1. Identify the process occupying the port:**

```powershell
Get-NetTCPConnection -LocalPort 7878 -State Listen |
    Select-Object LocalAddress, LocalPort, OwningProcess
```

**2. Verify the process identity:**

```powershell
Get-CimInstance Win32_Process -Filter "ProcessId = <PID>" |
    Select-Object Name, ExecutablePath, CommandLine
```

**Warning:** Never terminate a process based solely on its PID or port number. Verify that its executable path and command line correspond to an AgentiX instance. Terminating an unrelated process may interrupt other applications or cause data loss.

**3. Attempt a graceful shutdown first:**

If the previous AgentiX instance is still accessible, close it normally using its original PowerShell terminal (`Ctrl+C`) and wait for the process to exit. Allow any active operations to finish before shutting down.

Verify that the port has been released:

```powershell
Get-NetTCPConnection -LocalPort 7878 -State Listen -ErrorAction SilentlyContinue
```

No output indicates that no TCP listener is currently using port 7878.

**4. Force termination only if necessary:**

If the previous instance is unresponsive, cannot be closed normally, and its identity has been verified, confirm that the PID still belongs to that instance before executing:

```powershell
Stop-Process -Id <PID>
```

**5. Restart AgentiX:**

```powershell
.\infra\Invoke-AgentiXIac.ps1 -Action LaunchGui
```

**Note:** Replace `<PID>` with the actual process ID returned by PowerShell. PIDs may be reused, so always recheck the process identity immediately before termination. `Stop-Process` does not guarantee a graceful shutdown and may interrupt active operations or cause unsaved data to be lost.
## Managed V7 roots

The reviewed schema-2 profile in `infra/windows.local.json` selects two explicit
V7 locations: `home` is `D:\AI\Agentix-data\v7` for the managed Python runtime,
launchers, drafts, approvals, profiles, logs and cleanup receipts; `toolsRoot`
is `D:\AI\AgentiX_v7\generated_tools` for generated tool and application
artifacts. IaC does not read, migrate, remove or adopt the legacy V5 namespace.

Do not edit either path while a reviewed plan is pending or a managed process is
running. A changed configuration invalidates the plan and requires a new
`Plan`/review cycle. Paths must be absolute local directories, cannot overlap
each other or the source checkout runtime root, and cannot include existing
reparse points.

Launchers set `AGENTIX_HOME`, `AGENTIX_TOOLS_ROOT`, `AGENTIX_SERVER_PORT` and
`AGENTIX_OPEN_BROWSER` for their owned process. Do not set credentials or modify
global environment variables to configure model providers.

## How the Python environment is installed

There is no separate installer: IaC (`infra/Invoke-AgentiXIac.ps1`) owns every
step, and installation happens only during `Apply`. `Test` and `Plan` are
read-only and neither download nor write anything.

### When it runs

1. `-Action Test` observes the current state and compares actual package
   versions against `infra/runtime.lock.txt`. It installs nothing. When it
   reports `inDesiredState: true`, no work is pending.
2. `-Action Plan` computes the pending changes and writes the reviewed JSON
   plan.
3. `-Action Apply` performs the real installation in the fixed resource order
   (`$script:ResourceOrder`):
   - `python`: when the base interpreter is missing, WinGet installs
     `Python.Python.3.11` 3.11.9, x64, user scope, without a global PATH entry
     or the py launcher.
   - `dsc`: downloads the pinned DSC 3.3.0 and verifies its signature.
   - `environment`: creates the virtual environment, installs dependencies and
     installs Chromium.
   - `launchers`: generates the launchers.
   - `location`: writes the deployment configuration receipt.

Only the resources that the plan lists as changes are executed.

### What the `environment` resource does

- Creates the virtual environment under
  `D:\AI\Agentix-data\v7\environments\<hash16>\`, where the hash is the first
  16 characters of the SHA-256 digest of `runtime.lock.txt`. A changed lock
  therefore produces a new environment instead of updating the existing one.
- Writes the `.agentix-owned` marker; an existing directory without that marker
  is refused rather than adopted.
- Runs `pip install --require-hashes --only-binary=:all: -r runtime.lock.txt`
  with `PIP_CONFIG_FILE=NUL` and the index pinned to PyPI, neutralizing any
  caller `PIP_*` variables.
- Runs `pip check` to validate consistency.
- Installs Playwright **Chromium only**, and only when no compatible binary is
  already present.

### Current state of this machine

- Base interpreter:
  `C:\Users\xpiku\AppData\Local\Programs\Python\Python311\python.exe` (present).
- Managed environment:
  `D:\AI\Agentix-data\v7\environments\7d6df7e204a38b63\Scripts\python.exe`
  (present).

The environment is therefore already created and is not reinstalled on every
start.

### At launch

`LaunchGui` and `LaunchCli` install nothing: they validate prerequisites with
`Test-IacLaunch` and fail closed when something is missing. The only exception
is the explicit V7-055 recovery: when a pending application review detects that
Chromium is missing, **Install required host dependency** runs
`python -I -m playwright install chromium` with the managed Python after the
owner confirms. It installs no packages and no other browsers.

### Common points of confusion

- IaC never installs, starts, updates or selects Ollama or its models; those
  remain the operator's responsibility.
- When `Apply` reports `Reviewed plan is stale or modified`, the plan is no
  longer valid: generate a new, differently named plan.
- When the final `Test` does not report `inDesiredState: true`, do not launch
  the GUI; diagnose that result first.


