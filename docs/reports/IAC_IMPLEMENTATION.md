# IAC-001 implementation and current-machine evidence

Date: 2026-10-24. Checkout: D:/AI/AgentiX_v3. This report concerns v3, not the v2 working directory used by the desktop chat. The project infrastructure definition is infra/, with WinGet-backed user prerequisite installation, DSC 3.3.0 command resources and PowerShell Plan/Apply/Test entrypoints. No Docker, elevation, application autostart or graphical installer is provided.

## Implemented and observed

Python 3.11.9 and Ollama 0.40.6 were reused without adopting their installations. Private DSC 3.3.0 and a fresh independently owned venv were prepared. The 158-package Windows wheel lock has hash 7d6df7e204a38b636944818ef22ceaf8d78a3e91eb15a5e668fbd5768e1aa374. The environment is identified by its 7d6df7e204a38b63 prefix; manual launchers invoke its exact Python, with loopback GUI port 7873 and separate tool storage. No v2 environment is used as the deployed runtime.

Windows packaged-host virtualization resolved the logical LOCALAPPDATA/AgentiX/v3 location into this host's user package cache. iac-managed-paths-final.json records the actual physical paths. A user/home-scoped local location receipt lets later host contexts resolve that same owned deployment without traversing tool storage.

Actual initial provisioning succeeded: iac-apply-retry3.txt. The initial reapplication changed none of five tracked managed files: iac-apply-second.txt and iac-idempotence-result.json. The subsequent explicit location resource was applied successfully: iac-location-plan.json and iac-location-apply.txt. Later source changes require fresh plan fingerprints rather than accepting old plans.

Manual launch verification succeeded independently: GUI HTTP 200, duplicate port rejection and CLI clean exit. See iac-gui-smoke-result.json, iac-cli-smoke-result.json and iac-owned-gui-stop.txt. Only the disposable owned GUI listener was stopped. Provisioning did not start the application or restart existing instances. Existing generated artifacts were never inspected.

## Current readiness and limits

The final observation during SEC-LLM-001 shows zero planned infrastructure changes and zero blockers (iac-idempotence-final-plan.json), but its warning records Ollama offline. The loopback API check and prose-report attempt received connection refused. Do not reinterpret zero file changes as full runtime readiness: an operator must manually start Ollama before actual model use can be checked. No automatic server start, model download or substitute model was attempted.

Offline/provider doubles do not establish clean-Windows installation. This machine reused Python, Ollama and the already downloaded default model during the original successful application. Actual missing-Python/missing-Ollama installations and model pulls were not exercised here. No transactional rollback of external installers, full installed-file integrity monitor or resolution of Python 3.11.9 security age is claimed. PowerShell verification is parser/narrow-policy analysis, not Pester or PSScriptAnalyzer. Native AppContainer/browser/framework evidence is separate and retained in the associated reports.

The GUI model-profile feature added later does not change IaC's pinned default provisioning policy. Selecting other local/external models is explicit per-session application configuration and does not attest their model quality or availability.
