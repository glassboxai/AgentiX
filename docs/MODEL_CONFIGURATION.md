# Model settings and human review

The left Settings & Review sidebar follows the native Gradio Sidebar pattern used by NexisNodes v0.4.0. Its native toggle hides or opens it; the conversation, installed tool catalog and validation results remain in the main workspace. Authorization & Test Review exists only inside the sidebar. Use its independent scrollbar for long reviews.

## Local models

Every new session starts with Ollama and qwen3-coder:30b. Refresh models reads the selected loopback Ollama /api/tags endpoint. Select an installed model and click Apply model. No discovery action downloads a model or starts Ollama. An unavailable service or absent default is reported; there is no silent substitution. Selecting another model does not establish that it works as well as the historically validated qwen3-coder:30b.

## External profiles

1. Choose OpenAI or OpenAI-compatible, enter a plain profile name, External model and HTTPS endpoint, and enter the API key in the password field.
2. Save profile. This stores the key with Windows Credential Manager and only nonsecret metadata in the user-local v3 data directory. The key field clears after submission. Saving does not activate the provider.
3. Review the remote-data notice, explicitly check consent for this session, and click Apply model. Task descriptions and relevant artifacts will be transmitted to the selected provider. Provider retention and billing terms are external to AgentiX.
4. Later sessions can refresh and select a saved profile without re-entering its key. They still start locally and require new consent before external activation.
5. To update a profile, select it, edit its fields and optionally enter a replacement key, then save. An empty key retains the saved credential. Reload after concurrent changes; stale edits are rejected.
6. To create another profile, select New profile before entering its details. To delete, select an inactive profile and use Delete selected profile. First switch this session to Ollama if that profile is active. Deletion does not revoke the provider's key or terminate other sessions' clients.

Never include keys in the query. There is no show-key action. Profile operations are denied during active work or a pending review. A model change constructs fresh session services and never inherits a previous query's result. Under REUSE-002, a valid Windows-protected approval may authorize unchanged tool functions; a fresh isolated execution is still required and remote-provider consent remains session-specific.

Only public HTTPS APIs on port 443 are accepted. OpenAI uses https://api.openai.com/v1. Unsupported private endpoints, URL credentials, redirections or invalid configuration fail closed. No operation changes the global PATH or puts keys in environment variables. If credential storage is blocked, local Ollama remains available and external configuration fails.

## Scope and troubleshooting

The GUI is a local application for one Windows user, not a remotely authenticated service. Windows protects saved credentials against other users, not malware under the same account. Metadata uses the host's physical LOCALAPPDATA location; packaged Codex hosts can resolve it into their Windows package cache. Do not copy profile files as a way to migrate secrets to another user or PC.

Fixed failure messages avoid revealing secret exception bodies. Confirm the provider, endpoint, model, profile selection, key and consent. Check whether work/review is still pending, or reload a concurrently edited profile. Credential cleanup errors are logged by operation/type without key data. Read LLM_SECURITY_2026.md for threat assumptions and residual limitations.

## UI-MODEL-002 visibility and tested actions

With Ollama selected, API key and remote-transfer consent are hidden and are not required. Changing providers clears both values; choosing an external provider reveals a password field and unchecked consent. Loading a saved profile does not restore a key into the browser or remember consent. Secondary sidebar buttons use the reference Glass Box translucent dark palette with light text and subtle borders.

Refresh models explicitly reads the local catalog. Save profile and Delete selected profile operate on external profiles, not local Ollama credentials. Refresh saved profiles reloads the user-local catalog so another session's newly saved profile becomes selectable. Apply model changes only this session's client/runtime, and remains blocked during work/review. Current functional evidence is in reports/SIDEBAR_017_VALIDATION.md.

## Unified local and external profiles (PROFILE-001)

The selector is now Saved profiles. To create a local profile, choose New profile, keep Ollama, select the installed model and endpoint, enter a profile name and click Save profile. Refresh saved profiles or another session can load it. Select the saved entry and click Apply model to activate it for that session. Ollama stores metadata only: it requires no API key, consent or access to Windows Credential Manager. Editing a selected entry updates it; select New profile to create another. Names may contain readable Unicode and model-style punctuation, including colons, within 64 characters. Controls and markup are rejected.

External profiles still require a key on creation or conversion from local. An empty key retains an existing external credential. Converting external to local safely retires its old owned credential; converting local to external requires a new key. Saved keys and consent are never returned to the editor. Existing external JSON and credential encoding remain readable; no automatic migration or deletion of existing user data is performed. Older external-only application builds do not understand new local records and must not run as profile writers against the upgraded catalog.

Failed saves display a fixed reason code. Refresh preserves the last failed-save reason instead of replacing it with an unqualified success message. Report only the code in brackets; never share your key or full request logs. Common codes are key_format, key_required, credential_unavailable, credential_write, metadata_write and profile_changed. Numeric Windows error codes may supplement a native failure; vendor exception bodies, paths and credentials are not displayed. Local profiles remain usable if native credential storage is blocked.

The retained UTF-16 credential representation has a 2560-byte Windows blob limit (1280 printable ASCII characters), separately from the generic 8–2048-character format check. Oversized credentials receive key_storage_limit before a native write. Existing shorter credentials are unchanged. Official limit: https://learn.microsoft.com/en-us/windows/win32/api/wincred/ns-wincred-credentialw. Saving validates format/storage, not authentication with the provider.
