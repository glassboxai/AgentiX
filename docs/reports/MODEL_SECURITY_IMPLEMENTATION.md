# SEC-LLM-001 / UI-MODEL-001 implementation report

Date: 2026-10-24. Project: D:/AI/AgentiX_v3. Status: implemented and verified within the scope below.

## Delivered behavior

The native Gradio Sidebar follows the pattern from NexisNodes v0.4.0 shell.py and contains the single Authorization & Test Review panel, with independent scrolling and an accessible native hide/open toggle. The main right column contains catalog and validation results. Hidden sidebar content is removed from interaction/visibility while the toggle remains available. Existing agent and crew verbose output is retained.

Ollama installed-model discovery reads only loopback /api/tags, without downloads or inference. The model dropdown supports installed names, including namespaces. An explicit External model textbox avoids ambiguity with local dropdown selection. Default GUI composition always starts with local ollama/qwen3-coder:30b independently of legacy CLI environment overrides. API profiles support OpenAI and public HTTPS OpenAI-compatible providers; no provider quality or authentication claim is inferred from configuration alone.

Saved profiles survive application restarts using Windows Credential Manager local-machine persistence for the current Windows user. JSON metadata contains names, endpoint/model/provider, revision and opaque credential references, never API keys or remembered consent. Select, create, update and delete are available from the sidebar. Remote activation requires fresh session consent and matching saved metadata/revision; empty update keys retain existing credentials. Credential inputs clear on authenticated submissions. Sessions retain independent clients, selected settings, approval state and verification. Applying another model builds fresh application services and does not inherit old execution authorization.

Profile writes use closed UUID filenames, bounded schemas, reparse checks, interprocess locking and atomic metadata replacement. New key targets do not overwrite the prior working credential before a successful commit. Stale revisions and stale displayed selection identities are rejected. Explicit deletion only touches references validated as owned by the selected profile. Old references are retained when cleanup needs retry. Closing the browser does not delete a saved key; deleting a profile does not revoke the vendor key or erase another session's already loaded client credential.

Remote transport validates public HTTPS destinations and base paths, denies URL credentials and redirects, rechecks resolution per request, and rejects private, reserved and multicast destinations. The installed CrewAI synchronous/asynchronous interceptor integration is exercised with synthetic credentials without sending a request. Model construction does not mutate environment variables. Host logging/activity and result/error paths redact registered keys and avoid raw provider exception messages at the settings boundary.

Queries are limited to 16,000 characters, active workflows to four per process, agents to twelve iterations/600 seconds/zero retries, and clients to configured 120-second requests/8,192 output tokens/zero retries. These are bounded settings, not hard instantaneous cancellation or billing guarantees. Existing compile-after-edit, approval, content-bound handoff, host acceptance, path-containment and AppContainer/Job Object gates remain in force.

## Final evidence

| Check | Result | Raw evidence |
| --- | --- | --- |
| Complete offline suite | 412 passed, 23 opt-in tests deselected; 15 existing CrewAI deprecation warnings | model-offline-final.txt |
| Complete explicit real-integration suite | 23 passed, 412 deselected, 118.41 seconds | model-integrations-final.txt |
| Browser subset | 7 passed; actual Edge/Playwright against disposable loopback server | model-browser-final.txt and model-browser/ |
| Native/framework subset before the final endpoint edge-case addition | 16 passed, including native credential cross-process persistence | model-native-final.txt |
| Ruff | Passed | model-ruff-check.txt |
| Formatting | 89 files already formatted | model-ruff-format.txt |
| Source-reference freshness | No missing/stale entries | model-reference-check.txt |
| PowerShell parser/narrow command policy | Five files passed; not Pester/PSScriptAnalyzer | model-powershell-check.txt |

The explicit integration suite comprises seven browser scenarios, six installed-framework/transport checks, nine native AppContainer checks and one native Windows Credential Manager check. The Windows vault test creates a unique synthetic target, reads it from a separate Python process using only a reference argument, compares a digest, deletes it in finally, and confirms it is absent. It does not enumerate or inspect existing credentials. Browser profile storage and model/network factories are doubled, while Gradio UI, callbacks, metadata persistence, review and host comparison are real. These distinctions prevent synthetic-key checks from being mistaken for actual provider authentication or model inference.

Initial failures and fixes are preserved in model-profiles-red.txt, model-sidebar-red.txt, model-request-policy-red.txt, model-capacity-red.txt, model-persistence-red.txt, model-saved-activation-red.txt, model-profile-identity-red.txt, model-local-start-red.txt, model-multicast-red.txt and model-namespace-red.txt. Browser findings and preparation errors are retained in the earlier model-browser/model-framework reports and explained in ../KNOWN_ISSUES.md. Assertions were not weakened to conceal failures. The earlier three compatibility failures were corrected by extending the Gradio double and explicitly asserting the new approved settings alongside all preserved legacy values.

## Security assessment and limits

The ten published OWASP GenAI LLM Top 10 2026 entries are mapped to concrete controls, tests and applicability in ../LLM_SECURITY_2026.md. This is not OWASP certification. No finite suite proves arbitrary generated programs correct, malicious tests honest, prompt injection impossible or all dependencies secure. Retained Python 3.11.9 age, same-user malware, browser extensions, provider-side retention, encoded/fragmented secret echoes, DNS resolution/connection races, aggregate lifetime resource use and cross-vault/filesystem crash orphan cleanup remain documented limits. No new training/RAG/vector pipeline is implemented.

No existing generated artifact, real API key or paid inference was used. Existing live instances and v2 runtime source were preserved; browser fixtures owned and stopped only their disposable processes. No model download, Ollama server start, Docker, Terraform migration or graphical installer was performed. A new application launch is needed to load changed Python/UI source; existing running applications were not restarted by these tests.

## Ollama report provenance and operational availability

Per engineering policy, tools/draft_report.py attempted local qwen3:14b prose-only drafting. The local service at http://127.0.0.1:11434 refused connection (WinError 10061), so no draft was produced and no remote fallback was used. This report was authored manually and checked against raw evidence. See model-report-draft-attempt.txt and model-report-provenance.json. Engineering code and tests were never generated by Ollama.

The same unavailable service prevents claiming current real-model readiness or fresh qwen3-coder:30b inference. It was not started automatically. The IaC profile still has zero proposed file/resource changes, but its warning explicitly records Ollama offline; zero changes must not be described as full runtime readiness. Historical v3 provisioning/GUI/CLI evidence and this current limitation are separated in IAC_IMPLEMENTATION.md.

## Updated maintained documentation

Specification 016, AGENTS.md, architecture, technical guide, installation guide, model-settings manual, OWASP matrix, change/incident registers and source reference were updated in English. The current maintained source/configuration hashes are recorded separately in model-security-source-hashes.json; historical baseline/fix manifests remain untouched.
