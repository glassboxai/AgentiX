# Current setup: Windows Infrastructure as Code

The approved IAC-001 Windows-user profile is implemented in ../infra. Follow
[the IaC installation and operations manual](../infra/README.md) for Plan/Apply/Test,
manual GUI/CLI startup, pinned prerequisites, model-download consent and recovery.
The profile prepares an independent hash-locked environment. Python 3.11.9 remains an
explicit compatibility choice; no Python upgrade or graphical installer is supplied.
Historical manual-setup instructions below remain reference for earlier checkouts.
Current evidence and limitations are in reports/IAC_IMPLEMENTATION.md.

# AgentiX v3 checkout setup

No application installer is supplied. Use Windows 11 and CPython 3.11 with a complete
standard library for native isolation. From D:\AI\AgentiX_v3:

```powershell
py -3.11 -m venv .venv
.\.venv\Scripts\Activate.ps1
python -m pip install -r requirements-runtime.txt -r requirements-dev.txt
# Optional browser checks:
python -m pip install -r requirements-browser.txt
$env:OLLAMA_MODEL = 'ollama/qwen3-coder:30b'
python app.py
# Or: python main.py
```

Ollama must already be running locally with qwen3-coder:30b available. Model download
and model memory requirements are separate from Python dependencies. Browser tests use
installed Edge by default. If the GUI port is occupied, do not terminate an existing
session automatically; use the documented disposable test server for verification.

requirements-runtime.txt pins observed direct dependencies. Transitive dependencies
are not locked and this fresh-environment procedure has not been verified on a clean
machine. The release tests used the existing v2 CPython environment against v3 source.
The v2 .autotool directory is deliberately not copied. No administrator installer,
update service or uninstall workflow is claimed. See README.md for verification commands.

The following retained notes describe current runtime requirements and historical
validation. Historical v2 evidence paths do not identify the new v3 checkout.

# Installation manual

The current GUI is branded AgentiX with local logo/CSS assets under
`src/agentix/ui/assets/`. Preserve that directory when copying this development
checkout. Inter should be installed locally for the requested typography; Arial
and the browser sans-serif are fallbacks. The GUI makes no external font request.
Normal startup applies the theme/favicon automatically. A process started before
the UI-012 changes keeps its loaded interface; a separate new instance can preview
the changes without restarting an active session. The installer remains deferred.

Status: development baseline only. No Windows installer has been implemented. The approved target is Windows 11, per user, without administrator rights; installer implementation is deferred at the user's request.

## Current checkout

Native execution now requires Windows and a complete local CPython installation whose executable, DLLs and standard library can be staged. The existing Windows 11/Python 3.11 environment was tested with AppContainer and Job Objects. No Docker or Python package for isolation is required. Native setup errors deny execution rather than falling back to the host. Only standard-library tool dependencies are supported; third-party tool packages are not copied. A fresh copied runtime per call adds startup/disk overhead.

Before each query's execution, the manager must invoke `Verify Existing Tool` for a provisional check and then `Submit Acceptance Cases for Human Review`. Explicit human approval plus host comparisons are required; unittest success and file auto-approval cannot authorize a tool. Evidence from previous queries or application runs is not reused. See `ACCEPTANCE_REVIEW.md` for the review flow, supported JSON outputs and comparisons. Both Gradio and the CLI support mandatory interactive acceptance. Run `main.py` for terminal review; see `ACCEPTANCE_REVIEW.md`. Start a new application process to load changed source; verification does not restart the live application.

The native checks use independently authored temporary fixtures and require no Ollama/model or application server:

```powershell
python -m pytest -m windows_isolation
```

These checks temporarily create and delete AppContainer profiles and staged runtimes. Host security policy may deny this. The isolated child has a 30-second default execution deadline; provisioning is additional. Current verification and security limitations are in `reports/HUMAN_ACCEPTANCE.md`.

SEC-005 adds server-side browser sessions and identified approvals without new runtime dependencies. Each browser session gets its own provider client/agent objects; model weights remain managed by Ollama. The view stores an access token in Gradio State and submits a nonsecret approval ID with its editor. Default capacity is 128 sessions; inactive registry entries expire after 1800 seconds on registry activity. Delivered unload events cancel unresolved approvals; active code is not forcibly interrupted. Shared artifact storage and the existing loopback launch remain unchanged.

Migration note for direct Python callers: `resolve_pending_request` now requires `request_id` and `owner_id` keyword arguments taken from the pending snapshot; omitted/stale/foreign identities return False. `on_approve`/`on_reject` likewise require the displayed request ID to authorize anything. Invalid manager creation JSON now fails explicitly instead of falling back to an unrelated tool. Restart an already running application to load these changes; automated verification does not restart it.

REF-003 implementation lives in `src/agentix/`. Keep that directory and `_agentix_path.py` alongside the root launch scripts when using a checkout. `app.py` and `main.py` still launch the UI and CLI respectively. Importing them no longer creates storage or initializes models/widgets; initialization occurs on explicit startup or legacy runtime-attribute access. No installed-package or Windows-installer workflow is claimed yet.

The copied `.autotool` environment is machine-dependent and is not a distributable installation. On this machine, from the project root:

```powershell
python -m pytest
```

For historical baseline reproduction only, the following command exposed the original known defects. Their expected-failure markers have since been removed after approved corrections; use the full suite above to run the current normal regression tests:

```powershell
python -m pytest -m known_issue --runxfail
```

On fresh Python 3.11+, installing `requirements-dev.txt` supports the offline suite and Ruff; it does not install application runtime dependencies. Pytest adds `src` and the checkout root through `pytest.ini`. Default tests need neither Ollama, Gradio/CrewAI installations nor a browser. They execute only trusted temporary fixtures.

The three opt-in framework tests require installed runtime dependencies. They construct real tool schemas/widgets and exercise Gradio process_api routing, approval IDs and unload in memory, without starting a model/HTTP server or reading existing project artifacts:

```powershell
python -m pytest -m frameworks
```

Check active application source with Ruff; do not scan the excluded artifact directory or inactive source copies:

```powershell
python -m ruff check src tests tools app.py main.py config.py security_manager.py custom_tools.py _agentix_path.py
python -m ruff format --check src tests tools app.py main.py config.py security_manager.py custom_tools.py _agentix_path.py
```

Runtime requires compatible Gradio, CrewAI and Ollama dependencies. A verified runtime lock and clean-install procedure remain pending. Default settings are `OLLAMA_BASE_URL=http://localhost:11434` and `OLLAMA_MODEL=ollama/qwen3-coder:30b`.

## Observed local runtime

Live check on 2026-10-19: the configured 30B model coincided with severe memory pressure on this approximately 16 GiB RAM machine. An earlier conversation-only smoke used a smaller-model override, but that did not validate tool creation. The user has confirmed that Agentix must use qwen3-coder:30b; current launches must use:

```powershell
$env:OLLAMA_MODEL = 'ollama/qwen3-coder:30b'
python app.py
```

This variable applies to that shell and its child process; a launch elsewhere still uses its own environment/default. Actual console startup and clean `q` exit were verified with `main.py`; CLI-001 subsequently added and tested its dedicated approval/review adapter. See `reports/LIVE_SMOKE.md` for measured results and limits. The live check did not validate full generated-tool E2E or change installation dependencies.

## Optional browser tests

Agents and crews run with `verbose=True`, preserving their messages in the GUI together with technical events. Both the normal launcher and supervised temporary launcher use owner-bound stdout routing. Shared role instructions now require specifications, implementation, tests, review and actual execution without repeating these duties in user queries. Empty-catalog decisions use a manager instance without tools; execution retains the regular manager's tools. Final tool answers use current host-observed call results. No new dependency is required. A running process must be restarted manually to load source changes; automated verification does not restart the user's live process. Real 30B review outcomes are recorded separately from deterministic checks.

Optional browser regression dependencies and commands are in `BROWSER_TESTING.md` and `requirements-browser.txt`. They are separate from the offline suite, use installed Edge by default, and require the runtime Gradio environment. They neither install an application installer nor require Ollama.

The subsequent supervised English 30B creation/review/execution run completed with
manual corrections, seven provisional tests and sixteen host-compared cases.
See `reports/COMMUNICATION_LIVE30B.md` for actual evidence and limits. This does
not establish clean-install or installer verification.

## Future installer requirements

Check supported Python, disk space, dependencies, Ollama and configured model. Create a fresh environment, install pinned dependencies, supply launcher/diagnostics and preserve generated artifacts on upgrades. Large model downloads must be explicit. The final manual must document actual paths, install/update/uninstall commands and troubleshooting backed by clean-environment tests. These are planned requirements, not existing capabilities.

Report commands and evidence limitations are documented in `reports/BASELINE.md`. Keep this manual synchronized with the eventual installer.

## Model profiles and Windows credentials

The v3 sidebar supports installed local Ollama models and explicit OpenAI/OpenAI-compatible profiles. No new Python dependency is needed. Windows Credential Manager must be available to the current non-elevated Windows user; if blocked, remote profile storage fails closed and local models remain usable. Profile metadata is stored in host-resolved LOCALAPPDATA/AgentiX/v3/data/model-profiles, independent of generated tools. Keys use non-roaming, current-user/current-PC persistence. No real API key is required to install or run the test suite. See MODEL_CONFIGURATION.md and LLM_SECURITY_2026.md before enabling remote providers. No graphical installer is introduced.

## PROFILE-001 compatibility

Local Ollama profiles now save without initializing Windows credential services. External profiles retain the existing user/PC vault boundary and UTF-16 representation. Existing external JSON files require no migration. Upgrade running instances before using the unified local/remote catalog: older external-only builds reject local entries. Do not delete existing metadata to work around an old instance. See MODEL_CONFIGURATION.md for safe diagnostic codes and the native blob-size limit.

## Reusing reviewed tools

A tool becomes reusable after review, host acceptance and a successful isolated call. A later question may supply different inputs without repeating tests or code review. With the protected store enabled, approval survives reloads, other sessions and restarts under the same user/machine/storage identity. Sensitive or unclassified calls still require explicit confirmation. Changed artifacts or security policy require renewed review, and historic tools without a protected record retain first-use verification.

## Durable reviewed-tool approvals

After initial human review, host-compared acceptance and a successful isolated call, approvals are remembered across reloads, sessions and restarts under the same Windows user and machine. Managed launchers preserve the configured tool-storage root. Protected records live under the host-resolved LOCALAPPDATA/AgentiX/v3/data/tool-approvals directory, outside the tools. A different storage root, changed implementation/tests/security policy or unreadable record requires renewed review. Historic tools without a protected record need one initial review; old unittest reports cannot establish trust. Sensitive/unclassified calls still ask for permission and approval cannot enable blocked network/filesystem access.

Review code, tests and acceptance in the right column below Tool validation, including when the model-settings sidebar is closed. The acceptance panel explains future-session authorization. If persistence fails, the current valid result may still be returned but fixed durable_approval diagnostics identify the failed storage operation; future-session reuse is not claimed for that failure. User-profile encryption is not a defense against software running as the same Windows user.
