# V7-050: Existing Ollama API at launch

Status: approved and implemented on 2026-11-03.

## Requirement and acceptance

Manual GUI/CLI launch uses the existing http://127.0.0.1:11434 server without
requiring its exact provisioning version or a matching local CLI executable.
A differing server version emits a warning. A readable semantic version, available
API, installed qwen3-coder:30b with the reviewed digest and all other managed
prerequisites remain mandatory. An unavailable/invalid API or changed model blocks
execution. No installation, inference, process restart or automatic adoption occurs.
Plan, Apply and Test retain the exact approved prerequisite configuration and
integrity policy. windows.local.json records provisioning intent, not the currently
running server version; its Ollama pin is restored to 0.40.13.

## Design and incident V7-ERR-050

Launch previously reused Test-IacDeployment, coupling operation to provisioning
version equality. Updating Ollama caused drift; editing the JSON to 0.40.14 then
failed Assert-IacConfiguration, which only permits 0.40.13.
Test-IacLaunch copies an injected/read-only observation, normalizes only the Ollama
client/server version fields for the existing strict planner and adds explicit API
availability/version validation. It leaves caller state unchanged. Start-IacApplication
uses this result, reports blockers/changes and emits warnings before its injected
runner. Test-IacDeployment and provisioning remain unchanged.

The Config parameter is the validated provisioning map. State is an optional host
observation for dependency injection. observed is an invocation-local copy used to
reuse prerequisite rules; plan is the strict planner result. blockers and warnings
are invocation-local lists returned alongside changes and inDesiredState. No secret
or artifact content is added. Version drift tolerance is not certification of full
compatibility with every Ollama release.

## Evidence

Eight new readiness tests failed before implementation (missing launch validator).
Infrastructure regressions then passed, including differing versions, unchanged
strict planning, offline/invalid API, model mismatch and unrelated drift. Public
launcher tests use trusted state and an injected runner; they start no application.
A read-only host check observed Ollama 0.40.14 and launch readiness with no changes
or blockers, and one version warning. No GUI/model inference was performed.

Final verification (2026-11-03): managed environment 7d6df7e204a38b63;
`python -m pytest -q`: 899 passed, 88 deselected, 19 dependency/UI warnings.
Ruff check passed; Ruff format check: 329 files already formatted. Source reference
freshness passed. Verify-Infrastructure.ps1: six files, syntax/command policy passed.
Read-only host observation: server 0.40.14, approved model present, GUI port free,
launchReady true, no blockers. These checks do not establish live inference or GUI
operation. No framework/native/model/browser run or installation was needed.

Current changed-file SHA-256 values (separate from historical delivery hashes):
- infra\Agentix.Iac.psm1: c941bf41f18ba188e1b841e8dad4971d8307ee83d5634894587d0c593a140c0a
- infra\windows.local.json: a7dfef3d898beda6da588fadf50a5cf7ed2a9547f0d2bb9a1af8a949338b6994
- tests\unit\test_iac.py: 30a542c094eafb2ae5654b5ccd8d7f5dff2cb61fc57c6d3df27ff4676adb6ae8
