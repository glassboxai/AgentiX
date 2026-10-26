# SEC-LLM-001 and UI-MODEL-001

Status: implemented; final validation evidence is recorded in reports/MODEL_SECURITY_IMPLEMENTATION.md. Approved by the user on 2026-10-24.

Use the native Gradio Sidebar demonstrated in NexisNodes v0.4.0 shell.py. Move Authorization & Test Review into it, retaining ownership and approval checks. Model configuration is session-owned, and changes are denied while running or reviewing. Default remains ollama/qwen3-coder:30b. Support Ollama loopback and explicit opt-in OpenAI/OpenAI-compatible HTTPS endpoints. Reject credentials in URLs, redirects by policy where supported, and private/custom endpoints except loopback Ollama. Custom remote endpoints must resolve only to public addresses; DNS rebinding remains a documented residual risk without an egress proxy.

API keys must be stored with Windows Credential Manager, referenced by opaque profile-owned targets, excluded from repr/logs/prompts/child processes, cleared from the UI after submission, and retained until explicit profile deletion. No environment mutation for model selection. Credential storage failures deny remote configuration. Remote content disclosure requires explicit consent. Switching models invalidates previous runtime verification by constructing fresh application services with the existing owning security boundary.

Bound user query length, model iterations, request duration, response tokens, retry count and concurrency. Existing host approvals, native isolation and independent acceptance remain mandatory. Document all ten OWASP 2026 risks, existing and additional controls, test evidence and residual risks; do not claim certification or immunity. RAG/embedding and training risks are not applicable to currently absent features, but downloaded models remain a supply-chain trust assumption.

Acceptance: real framework builds one hideable Sidebar; review has exactly one location inside it; provider controls have stable elem_id; foreign browser tokens cannot change settings; running/pending sessions reject changes; invalid endpoints/types/models/keys fail closed without secret text; keys never enter public status. Offline tests use fake vault/network/model factories. Real vault and browser checks are separate, disposable and do not use paid APIs or existing artifacts. Ruff, reference freshness, offline/framework/native/browser checks and English documentation are required.

## Approved completion decisions

The user selected persistent Windows Credential Manager storage across application starts and a refreshed list of installed Ollama models. Saved profile consent is not persisted; every new session starts local. Profiles support create/select/update/delete with opaque UUID identity and stale revision rejection. Metadata lives in the Windows-user v3 data directory. Blank update keys retain the credential; failed precommit updates retain the prior profile. Keys clear after submissions and are never exposed by a read/show API. Deleting an active selected profile requires first switching this session to Ollama. Other sessions' already initialized clients are not secretly stopped.

Native Windows Credential Manager persistence is local to the current user and PC. Profile metadata replacement is atomic under an interprocess lock; cross-vault/filesystem crash rollback is not promised. Postcommit obsolete credential references remain recoverable for explicit cleanup retries.

The implementation preserves compatibility settings, adds bounded provider/agent/workflow settings, and must pass offline, real frameworks, disposable Windows credentials, native AppContainer and browser suites. New tests never use paid API inference or existing generated artifacts.
