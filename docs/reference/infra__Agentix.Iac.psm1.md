# infra/Agentix.Iac.psm1

Source SHA-256: d925e7250b8155a0151da445e35e4396cc29a33af44c96f20f84b23810726dcd

Per-user desired-state planning and bounded convergence for AgentiX.

## Functions

### ConvertTo-IacMap

Recursively normalize JSON into ordered maps for stable fingerprints.

### Get-IacDigest

SHA-256 of canonical JSON; does not publish input values.

### Assert-IacContained

Enforce component containment and reject existing reparse-point ancestors.

### Assert-IacConfiguration

Reject unknown fields, unsupported versions and unsafe deployment inputs.

### Read-IacConfiguration

Load the fixed reviewed profile; never accepts executable configuration.

### Assert-IacSignature

Require a valid Authenticode signature from the reviewed prerequisite publisher.

### Resolve-IacRoot

Resolve Windows packaged-host folder aliases to a persistent physical managed path.

### Get-IacLocationFile

Return the current user's local, untracked deployment-location receipt path.

### Read-IacLocation

Validate owner-scoped physical-location metadata without traversing runtime data.

### Save-IacLocation

Persist the reviewed physical root for manual launches outside the provisioning host.

### Get-IacPaths

Derive owned paths without creating them or reading tool storage.

### Invoke-IacProcess

Run an explicit native argument vector, distinguishing stderr warnings from exit failures.

### Get-IacExecutableState

Read an installed binary identity, retaining hashes for reviewed-plan drift checks.

### Get-IacLaunchContent

Generate deterministic launchers with quoted literal paths and manual startup only.

### Get-IacEnvironmentState

Compare actual managed package versions and ownership; receipts alone cannot prove state.

### Get-IacPackageManager

Observe WinGet before planning a missing Python installation, freezing its exact identity.

### Get-IacState

Read prerequisites and owned state without downloads, writes or model execution.

### Get-IacSourceDigest

Fingerprint only named infrastructure and maintained application source, never artifact storage.

### Get-IacPlan

Produce a deterministic, reviewable plan from explicit observation and desired configuration.

### Test-IacPlan

Reject stale configuration, observations, source or modified planned actions.

### Write-IacEvent

Append bounded resource diagnostics without commands, prompts, artifacts or secrets.

### Get-IacArchive

Fetch a pinned official archive and verify SHA-256 before extraction.

### Set-IacResource

Converge one reviewed resource; no elevation, deletion, startup or host fallback.

### Invoke-IacConverge

Validate review then converge in dependency order; stop immediately on failure.

### Test-IacDeployment

Check desired state without requiring a free port for an already-running managed GUI.

### Invoke-IacApply

Bootstrap pinned DSC only after plan validation, then delegate mutation to its resource.

### Start-IacApplication

Manually launch GUI/CLI with managed Python after validating prerequisites.

## Scoped variables

Assigned values are excluded. Parameter/temporary meaning follows the owning function contract; process and script scopes are explicit.

| Name | Scope | Static type | Lifecycle |
| --- | --- | --- | --- |
| Config | Assert-IacConfiguration | System.Object | Enclosing invocation, unless explicitly process/environment or script scoped. |
| expected | Assert-IacConfiguration | System.Object | Enclosing invocation, unless explicitly process/environment or script scoped. |
| boundary | Assert-IacContained | System.Object | Enclosing invocation, unless explicitly process/environment or script scoped. |
| cursor | Assert-IacContained | System.Object | Enclosing invocation, unless explicitly process/environment or script scoped. |
| full | Assert-IacContained | System.Object | Enclosing invocation, unless explicitly process/environment or script scoped. |
| parent | Assert-IacContained | System.Object | Enclosing invocation, unless explicitly process/environment or script scoped. |
| Path | Assert-IacContained | System.Object | Enclosing invocation, unless explicitly process/environment or script scoped. |
| Root | Assert-IacContained | System.Object | Enclosing invocation, unless explicitly process/environment or script scoped. |
| Check | Assert-IacSignature | System.Object | Enclosing invocation, unless explicitly process/environment or script scoped. |
| File | Assert-IacSignature | System.Object | Enclosing invocation, unless explicitly process/environment or script scoped. |
| Kind | Assert-IacSignature | System.Object | Enclosing invocation, unless explicitly process/environment or script scoped. |
| Path | Assert-IacSignature | System.Object | Enclosing invocation, unless explicitly process/environment or script scoped. |
| pattern | Assert-IacSignature | System.Object | Enclosing invocation, unless explicitly process/environment or script scoped. |
| publishers | Assert-IacSignature | System.Object | Enclosing invocation, unless explicitly process/environment or script scoped. |
| signature | Assert-IacSignature | System.Object | Enclosing invocation, unless explicitly process/environment or script scoped. |
| _ | ConvertTo-IacMap | System.Object | Enclosing invocation, unless explicitly process/environment or script scoped. |
| key | ConvertTo-IacMap | System.Object | Enclosing invocation, unless explicitly process/environment or script scoped. |
| keys | ConvertTo-IacMap | System.Object | Enclosing invocation, unless explicitly process/environment or script scoped. |
| map | ConvertTo-IacMap | System.Object | Enclosing invocation, unless explicitly process/environment or script scoped. |
| null | ConvertTo-IacMap | System.Object | Enclosing invocation, unless explicitly process/environment or script scoped. |
| Value | ConvertTo-IacMap | System.Object | Enclosing invocation, unless explicitly process/environment or script scoped. |
| archive | Get-IacArchive | System.Object | Enclosing invocation, unless explicitly process/environment or script scoped. |
| archives | Get-IacArchive | System.Object | Enclosing invocation, unless explicitly process/environment or script scoped. |
| cache | Get-IacArchive | System.Object | Enclosing invocation, unless explicitly process/environment or script scoped. |
| Config | Get-IacArchive | System.Object | Enclosing invocation, unless explicitly process/environment or script scoped. |
| Kind | Get-IacArchive | System.Object | Enclosing invocation, unless explicitly process/environment or script scoped. |
| paths | Get-IacArchive | System.Object | Enclosing invocation, unless explicitly process/environment or script scoped. |
| pin | Get-IacArchive | System.Object | Enclosing invocation, unless explicitly process/environment or script scoped. |
| algorithm | Get-IacDigest | System.Object | Enclosing invocation, unless explicitly process/environment or script scoped. |
| text | Get-IacDigest | System.Object | Enclosing invocation, unless explicitly process/environment or script scoped. |
| Value | Get-IacDigest | System.Object | Enclosing invocation, unless explicitly process/environment or script scoped. |
| actual | Get-IacEnvironmentState | System.Object | Enclosing invocation, unless explicitly process/environment or script scoped. |
| Config | Get-IacEnvironmentState | System.Object | Enclosing invocation, unless explicitly process/environment or script scoped. |
| exe | Get-IacEnvironmentState | System.Object | Enclosing invocation, unless explicitly process/environment or script scoped. |
| false | Get-IacEnvironmentState | System.Object | Enclosing invocation, unless explicitly process/environment or script scoped. |
| identity | Get-IacEnvironmentState | System.Object | Enclosing invocation, unless explicitly process/environment or script scoped. |
| line | Get-IacEnvironmentState | System.Object | Enclosing invocation, unless explicitly process/environment or script scoped. |
| Matches | Get-IacEnvironmentState | System.Object | Enclosing invocation, unless explicitly process/environment or script scoped. |
| name | Get-IacEnvironmentState | System.Object | Enclosing invocation, unless explicitly process/environment or script scoped. |
| owned | Get-IacEnvironmentState | System.Object | Enclosing invocation, unless explicitly process/environment or script scoped. |
| owner | Get-IacEnvironmentState | System.Object | Enclosing invocation, unless explicitly process/environment or script scoped. |
| package | Get-IacEnvironmentState | System.Object | Enclosing invocation, unless explicitly process/environment or script scoped. |
| packages | Get-IacEnvironmentState | System.Object | Enclosing invocation, unless explicitly process/environment or script scoped. |
| Paths | Get-IacEnvironmentState | System.Object | Enclosing invocation, unless explicitly process/environment or script scoped. |
| present | Get-IacEnvironmentState | System.Object | Enclosing invocation, unless explicitly process/environment or script scoped. |
| required | Get-IacEnvironmentState | System.Object | Enclosing invocation, unless explicitly process/environment or script scoped. |
| script:InfraRoot | Get-IacEnvironmentState | System.Object | Enclosing invocation, unless explicitly process/environment or script scoped. |
| version | Get-IacEnvironmentState | System.Object | Enclosing invocation, unless explicitly process/environment or script scoped. |
| versions | Get-IacEnvironmentState | System.Object | Enclosing invocation, unless explicitly process/environment or script scoped. |
| Kind | Get-IacExecutableState | System.Object | Enclosing invocation, unless explicitly process/environment or script scoped. |
| Matches | Get-IacExecutableState | System.Object | Enclosing invocation, unless explicitly process/environment or script scoped. |
| Path | Get-IacExecutableState | System.Object | Enclosing invocation, unless explicitly process/environment or script scoped. |
| text | Get-IacExecutableState | System.Object | Enclosing invocation, unless explicitly process/environment or script scoped. |
| version | Get-IacExecutableState | System.Object | Enclosing invocation, unless explicitly process/environment or script scoped. |
| Config | Get-IacLaunchContent | System.Object | Enclosing invocation, unless explicitly process/environment or script scoped. |
| entry | Get-IacLaunchContent | System.Object | Enclosing invocation, unless explicitly process/environment or script scoped. |
| Paths | Get-IacLaunchContent | System.Object | Enclosing invocation, unless explicitly process/environment or script scoped. |
| script:InfraRoot | Get-IacLaunchContent | System.Object | Enclosing invocation, unless explicitly process/environment or script scoped. |
| env:LOCALAPPDATA | Get-IacLocationFile | System.Object | Enclosing invocation, unless explicitly process/environment or script scoped. |
| homeIdentity | Get-IacLocationFile | System.Object | Enclosing invocation, unless explicitly process/environment or script scoped. |
| owner | Get-IacLocationFile | System.Object | Enclosing invocation, unless explicitly process/environment or script scoped. |
| script:InfraRoot | Get-IacLocationFile | System.Object | Enclosing invocation, unless explicitly process/environment or script scoped. |
| command | Get-IacPackageManager | System.Object | Enclosing invocation, unless explicitly process/environment or script scoped. |
| false | Get-IacPackageManager | System.Object | Enclosing invocation, unless explicitly process/environment or script scoped. |
| supported | Get-IacPackageManager | System.Object | Enclosing invocation, unless explicitly process/environment or script scoped. |
| version | Get-IacPackageManager | System.Object | Enclosing invocation, unless explicitly process/environment or script scoped. |
| basePython | Get-IacPaths | System.Object | Enclosing invocation, unless explicitly process/environment or script scoped. |
| Config | Get-IacPaths | System.Object | Enclosing invocation, unless explicitly process/environment or script scoped. |
| env:LOCALAPPDATA | Get-IacPaths | System.Object | Enclosing invocation, unless explicitly process/environment or script scoped. |
| environment | Get-IacPaths | System.Object | Enclosing invocation, unless explicitly process/environment or script scoped. |
| lock | Get-IacPaths | System.Object | Enclosing invocation, unless explicitly process/environment or script scoped. |
| root | Get-IacPaths | System.Object | Enclosing invocation, unless explicitly process/environment or script scoped. |
| script:InfraRoot | Get-IacPaths | System.Object | Enclosing invocation, unless explicitly process/environment or script scoped. |
| blockers | Get-IacPlan | System.Object | Enclosing invocation, unless explicitly process/environment or script scoped. |
| changes | Get-IacPlan | System.Object | Enclosing invocation, unless explicitly process/environment or script scoped. |
| Config | Get-IacPlan | System.Object | Enclosing invocation, unless explicitly process/environment or script scoped. |
| DownloadModel | Get-IacPlan | System.Object | Enclosing invocation, unless explicitly process/environment or script scoped. |
| name | Get-IacPlan | System.Object | Enclosing invocation, unless explicitly process/environment or script scoped. |
| plan | Get-IacPlan | System.Object | Enclosing invocation, unless explicitly process/environment or script scoped. |
| script:ProjectRoot | Get-IacPlan | System.Object | Enclosing invocation, unless explicitly process/environment or script scoped. |
| State | Get-IacPlan | System.Object | Enclosing invocation, unless explicitly process/environment or script scoped. |
| warnings | Get-IacPlan | System.Object | Enclosing invocation, unless explicitly process/environment or script scoped. |
| file | Get-IacSourceDigest | System.Object | Enclosing invocation, unless explicitly process/environment or script scoped. |
| hashes | Get-IacSourceDigest | System.Object | Enclosing invocation, unless explicitly process/environment or script scoped. |
| name | Get-IacSourceDigest | System.Object | Enclosing invocation, unless explicitly process/environment or script scoped. |
| script:InfraRoot | Get-IacSourceDigest | System.Object | Enclosing invocation, unless explicitly process/environment or script scoped. |
| script:ProjectRoot | Get-IacSourceDigest | System.Object | Enclosing invocation, unless explicitly process/environment or script scoped. |
| _ | Get-IacState | System.Object | Enclosing invocation, unless explicitly process/environment or script scoped. |
| busy | Get-IacState | System.Object | Enclosing invocation, unless explicitly process/environment or script scoped. |
| Config | Get-IacState | System.Object | Enclosing invocation, unless explicitly process/environment or script scoped. |
| dsc | Get-IacState | System.Object | Enclosing invocation, unless explicitly process/environment or script scoped. |
| false | Get-IacState | System.Object | Enclosing invocation, unless explicitly process/environment or script scoped. |
| item | Get-IacState | System.Object | Enclosing invocation, unless explicitly process/environment or script scoped. |
| launchers | Get-IacState | System.Object | Enclosing invocation, unless explicitly process/environment or script scoped. |
| manager | Get-IacState | System.Object | Enclosing invocation, unless explicitly process/environment or script scoped. |
| model | Get-IacState | System.Object | Enclosing invocation, unless explicitly process/environment or script scoped. |
| ollama | Get-IacState | System.Object | Enclosing invocation, unless explicitly process/environment or script scoped. |
| ollamaPath | Get-IacState | System.Object | Enclosing invocation, unless explicitly process/environment or script scoped. |
| paths | Get-IacState | System.Object | Enclosing invocation, unless explicitly process/environment or script scoped. |
| python | Get-IacState | System.Object | Enclosing invocation, unless explicitly process/environment or script scoped. |
| tag | Get-IacState | System.Object | Enclosing invocation, unless explicitly process/environment or script scoped. |
| tags | Get-IacState | System.Object | Enclosing invocation, unless explicitly process/environment or script scoped. |
| target | Get-IacState | System.Object | Enclosing invocation, unless explicitly process/environment or script scoped. |
| true | Get-IacState | System.Object | Enclosing invocation, unless explicitly process/environment or script scoped. |
| version | Get-IacState | System.Object | Enclosing invocation, unless explicitly process/environment or script scoped. |
| Config | Invoke-IacApply | System.Object | Enclosing invocation, unless explicitly process/environment or script scoped. |
| env:AGENTIX_IAC_OPERATION | Invoke-IacApply | System.Object | Enclosing invocation, unless explicitly process/environment or script scoped. |
| env:AGENTIX_IAC_REVIEW | Invoke-IacApply | System.Object | Enclosing invocation, unless explicitly process/environment or script scoped. |
| env:PATH | Invoke-IacApply | System.Object | Enclosing invocation, unless explicitly process/environment or script scoped. |
| paths | Invoke-IacApply | System.Object | Enclosing invocation, unless explicitly process/environment or script scoped. |
| Plan | Invoke-IacApply | System.Object | Enclosing invocation, unless explicitly process/environment or script scoped. |
| principal | Invoke-IacApply | System.Object | Enclosing invocation, unless explicitly process/environment or script scoped. |
| result | Invoke-IacApply | System.Object | Enclosing invocation, unless explicitly process/environment or script scoped. |
| savedPath | Invoke-IacApply | System.Object | Enclosing invocation, unless explicitly process/environment or script scoped. |
| script:InfraRoot | Invoke-IacApply | System.Object | Enclosing invocation, unless explicitly process/environment or script scoped. |
| state | Invoke-IacApply | System.Object | Enclosing invocation, unless explicitly process/environment or script scoped. |
| after | Invoke-IacConverge | System.Object | Enclosing invocation, unless explicitly process/environment or script scoped. |
| cfg | Invoke-IacConverge | System.Object | Enclosing invocation, unless explicitly process/environment or script scoped. |
| changed | Invoke-IacConverge | System.Object | Enclosing invocation, unless explicitly process/environment or script scoped. |
| Config | Invoke-IacConverge | System.Object | Enclosing invocation, unless explicitly process/environment or script scoped. |
| converged | Invoke-IacConverge | System.Object | Enclosing invocation, unless explicitly process/environment or script scoped. |
| DscBootstrapped | Invoke-IacConverge | System.Object | Enclosing invocation, unless explicitly process/environment or script scoped. |
| false | Invoke-IacConverge | System.Object | Enclosing invocation, unless explicitly process/environment or script scoped. |
| id | Invoke-IacConverge | System.Object | Enclosing invocation, unless explicitly process/environment or script scoped. |
| Observe | Invoke-IacConverge | System.Object | Enclosing invocation, unless explicitly process/environment or script scoped. |
| Plan | Invoke-IacConverge | System.Object | Enclosing invocation, unless explicitly process/environment or script scoped. |
| review | Invoke-IacConverge | System.Object | Enclosing invocation, unless explicitly process/environment or script scoped. |
| script:ResourceOrder | Invoke-IacConverge | System.Object | Enclosing invocation, unless explicitly process/environment or script scoped. |
| Set | Invoke-IacConverge | System.Object | Enclosing invocation, unless explicitly process/environment or script scoped. |
| state | Invoke-IacConverge | System.Object | Enclosing invocation, unless explicitly process/environment or script scoped. |
| watch | Invoke-IacConverge | System.Object | Enclosing invocation, unless explicitly process/environment or script scoped. |
| argument | Invoke-IacProcess | System.Object | Enclosing invocation, unless explicitly process/environment or script scoped. |
| Arguments | Invoke-IacProcess | System.Object | Enclosing invocation, unless explicitly process/environment or script scoped. |
| errorText | Invoke-IacProcess | System.Object | Enclosing invocation, unless explicitly process/environment or script scoped. |
| escaped | Invoke-IacProcess | System.Object | Enclosing invocation, unless explicitly process/environment or script scoped. |
| Executable | Invoke-IacProcess | System.Object | Enclosing invocation, unless explicitly process/environment or script scoped. |
| false | Invoke-IacProcess | System.Object | Enclosing invocation, unless explicitly process/environment or script scoped. |
| info | Invoke-IacProcess | System.Object | Enclosing invocation, unless explicitly process/environment or script scoped. |
| output | Invoke-IacProcess | System.Object | Enclosing invocation, unless explicitly process/environment or script scoped. |
| process | Invoke-IacProcess | System.Object | Enclosing invocation, unless explicitly process/environment or script scoped. |
| quoted | Invoke-IacProcess | System.Object | Enclosing invocation, unless explicitly process/environment or script scoped. |
| stderr | Invoke-IacProcess | System.Object | Enclosing invocation, unless explicitly process/environment or script scoped. |
| stdout | Invoke-IacProcess | System.Object | Enclosing invocation, unless explicitly process/environment or script scoped. |
| tail | Invoke-IacProcess | System.Object | Enclosing invocation, unless explicitly process/environment or script scoped. |
| true | Invoke-IacProcess | System.Object | Enclosing invocation, unless explicitly process/environment or script scoped. |
| ErrorActionPreference | module | System.Object | Enclosing invocation, unless explicitly process/environment or script scoped. |
| PSHOME | module | System.Object | Enclosing invocation, unless explicitly process/environment or script scoped. |
| PSScriptRoot | module | System.Object | Enclosing invocation, unless explicitly process/environment or script scoped. |
| PSVersionTable | module | System.Object | Enclosing invocation, unless explicitly process/environment or script scoped. |
| script:InfraRoot | module | System.Object | Enclosing invocation, unless explicitly process/environment or script scoped. |
| script:ProjectRoot | module | System.Object | Enclosing invocation, unless explicitly process/environment or script scoped. |
| script:ResourceOrder | module | System.Object | Enclosing invocation, unless explicitly process/environment or script scoped. |
| config | Read-IacConfiguration | System.Object | Enclosing invocation, unless explicitly process/environment or script scoped. |
| script:InfraRoot | Read-IacConfiguration | System.Object | Enclosing invocation, unless explicitly process/environment or script scoped. |
| env:LOCALAPPDATA | Read-IacLocation | System.Object | Enclosing invocation, unless explicitly process/environment or script scoped. |
| file | Read-IacLocation | System.Object | Enclosing invocation, unless explicitly process/environment or script scoped. |
| null | Read-IacLocation | System.Object | Enclosing invocation, unless explicitly process/environment or script scoped. |
| owner | Read-IacLocation | System.Object | Enclosing invocation, unless explicitly process/environment or script scoped. |
| record | Read-IacLocation | System.Object | Enclosing invocation, unless explicitly process/environment or script scoped. |
| script:InfraRoot | Read-IacLocation | System.Object | Enclosing invocation, unless explicitly process/environment or script scoped. |
| Python | Resolve-IacRoot | System.Object | Enclosing invocation, unless explicitly process/environment or script scoped. |
| Root | Resolve-IacRoot | System.Object | Enclosing invocation, unless explicitly process/environment or script scoped. |
| content | Save-IacLocation | System.Object | Enclosing invocation, unless explicitly process/environment or script scoped. |
| env:LOCALAPPDATA | Save-IacLocation | System.Object | Enclosing invocation, unless explicitly process/environment or script scoped. |
| false | Save-IacLocation | System.Object | Enclosing invocation, unless explicitly process/environment or script scoped. |
| file | Save-IacLocation | System.Object | Enclosing invocation, unless explicitly process/environment or script scoped. |
| record | Save-IacLocation | System.Object | Enclosing invocation, unless explicitly process/environment or script scoped. |
| Root | Save-IacLocation | System.Object | Enclosing invocation, unless explicitly process/environment or script scoped. |
| script:InfraRoot | Save-IacLocation | System.Object | Enclosing invocation, unless explicitly process/environment or script scoped. |
| _ | Set-IacResource | System.Object | Enclosing invocation, unless explicitly process/environment or script scoped. |
| archive | Set-IacResource | System.Object | Enclosing invocation, unless explicitly process/environment or script scoped. |
| binary | Set-IacResource | System.Object | Enclosing invocation, unless explicitly process/environment or script scoped. |
| Config | Set-IacResource | System.Object | Enclosing invocation, unless explicitly process/environment or script scoped. |
| directory | Set-IacResource | System.Object | Enclosing invocation, unless explicitly process/environment or script scoped. |
| env:PIP_CONFIG_FILE | Set-IacResource | System.Object | Enclosing invocation, unless explicitly process/environment or script scoped. |
| env:PIP_INDEX_URL | Set-IacResource | System.Object | Enclosing invocation, unless explicitly process/environment or script scoped. |
| false | Set-IacResource | System.Object | Enclosing invocation, unless explicitly process/environment or script scoped. |
| item | Set-IacResource | System.Object | Enclosing invocation, unless explicitly process/environment or script scoped. |
| member | Set-IacResource | System.Object | Enclosing invocation, unless explicitly process/environment or script scoped. |
| name | Set-IacResource | System.Object | Enclosing invocation, unless explicitly process/environment or script scoped. |
| null | Set-IacResource | System.Object | Enclosing invocation, unless explicitly process/environment or script scoped. |
| owner | Set-IacResource | System.Object | Enclosing invocation, unless explicitly process/environment or script scoped. |
| paths | Set-IacResource | System.Object | Enclosing invocation, unless explicitly process/environment or script scoped. |
| Plan | Set-IacResource | System.Object | Enclosing invocation, unless explicitly process/environment or script scoped. |
| python | Set-IacResource | System.Object | Enclosing invocation, unless explicitly process/environment or script scoped. |
| Resource | Set-IacResource | System.Object | Enclosing invocation, unless explicitly process/environment or script scoped. |
| saved | Set-IacResource | System.Object | Enclosing invocation, unless explicitly process/environment or script scoped. |
| script:InfraRoot | Set-IacResource | System.Object | Enclosing invocation, unless explicitly process/environment or script scoped. |
| state | Set-IacResource | System.Object | Enclosing invocation, unless explicitly process/environment or script scoped. |
| target | Set-IacResource | System.Object | Enclosing invocation, unless explicitly process/environment or script scoped. |
| zip | Set-IacResource | System.Object | Enclosing invocation, unless explicitly process/environment or script scoped. |
| Config | Start-IacApplication | System.Object | Enclosing invocation, unless explicitly process/environment or script scoped. |
| entry | Start-IacApplication | System.Object | Enclosing invocation, unless explicitly process/environment or script scoped. |
| env:AGENTIX_OPEN_BROWSER | Start-IacApplication | System.Object | Enclosing invocation, unless explicitly process/environment or script scoped. |
| env:AGENTIX_SERVER_PORT | Start-IacApplication | System.Object | Enclosing invocation, unless explicitly process/environment or script scoped. |
| env:AGENTIX_TOOLS_ROOT | Start-IacApplication | System.Object | Enclosing invocation, unless explicitly process/environment or script scoped. |
| env:OLLAMA_BASE_URL | Start-IacApplication | System.Object | Enclosing invocation, unless explicitly process/environment or script scoped. |
| env:OLLAMA_MODEL | Start-IacApplication | System.Object | Enclosing invocation, unless explicitly process/environment or script scoped. |
| Executable | Start-IacApplication | System.Object | Enclosing invocation, unless explicitly process/environment or script scoped. |
| LASTEXITCODE | Start-IacApplication | System.Object | Enclosing invocation, unless explicitly process/environment or script scoped. |
| Mode | Start-IacApplication | System.Object | Enclosing invocation, unless explicitly process/environment or script scoped. |
| name | Start-IacApplication | System.Object | Enclosing invocation, unless explicitly process/environment or script scoped. |
| null | Start-IacApplication | System.Object | Enclosing invocation, unless explicitly process/environment or script scoped. |
| paths | Start-IacApplication | System.Object | Enclosing invocation, unless explicitly process/environment or script scoped. |
| Run | Start-IacApplication | System.Object | Enclosing invocation, unless explicitly process/environment or script scoped. |
| saved | Start-IacApplication | System.Object | Enclosing invocation, unless explicitly process/environment or script scoped. |
| script:ProjectRoot | Start-IacApplication | System.Object | Enclosing invocation, unless explicitly process/environment or script scoped. |
| state | Start-IacApplication | System.Object | Enclosing invocation, unless explicitly process/environment or script scoped. |
| test | Start-IacApplication | System.Object | Enclosing invocation, unless explicitly process/environment or script scoped. |
| variables | Start-IacApplication | System.Object | Enclosing invocation, unless explicitly process/environment or script scoped. |
| Config | Test-IacDeployment | System.Object | Enclosing invocation, unless explicitly process/environment or script scoped. |
| plan | Test-IacDeployment | System.Object | Enclosing invocation, unless explicitly process/environment or script scoped. |
| state | Test-IacDeployment | System.Object | Enclosing invocation, unless explicitly process/environment or script scoped. |
| true | Test-IacDeployment | System.Object | Enclosing invocation, unless explicitly process/environment or script scoped. |
| Config | Test-IacPlan | System.Object | Enclosing invocation, unless explicitly process/environment or script scoped. |
| fresh | Test-IacPlan | System.Object | Enclosing invocation, unless explicitly process/environment or script scoped. |
| Plan | Test-IacPlan | System.Object | Enclosing invocation, unless explicitly process/environment or script scoped. |
| State | Test-IacPlan | System.Object | Enclosing invocation, unless explicitly process/environment or script scoped. |
| Config | Write-IacEvent | System.Object | Enclosing invocation, unless explicitly process/environment or script scoped. |
| directory | Write-IacEvent | System.Object | Enclosing invocation, unless explicitly process/environment or script scoped. |
| Duration | Write-IacEvent | System.Object | Enclosing invocation, unless explicitly process/environment or script scoped. |
| env:AGENTIX_IAC_OPERATION | Write-IacEvent | System.Object | Enclosing invocation, unless explicitly process/environment or script scoped. |
| event | Write-IacEvent | System.Object | Enclosing invocation, unless explicitly process/environment or script scoped. |
| false | Write-IacEvent | System.Object | Enclosing invocation, unless explicitly process/environment or script scoped. |
| i | Write-IacEvent | System.Object | Enclosing invocation, unless explicitly process/environment or script scoped. |
| log | Write-IacEvent | System.Object | Enclosing invocation, unless explicitly process/environment or script scoped. |
| old | Write-IacEvent | System.Object | Enclosing invocation, unless explicitly process/environment or script scoped. |
| Outcome | Write-IacEvent | System.Object | Enclosing invocation, unless explicitly process/environment or script scoped. |
| paths | Write-IacEvent | System.Object | Enclosing invocation, unless explicitly process/environment or script scoped. |
| Resource | Write-IacEvent | System.Object | Enclosing invocation, unless explicitly process/environment or script scoped. |
| suffix | Write-IacEvent | System.Object | Enclosing invocation, unless explicitly process/environment or script scoped. |
