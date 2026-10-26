# PROFILE-001 unified profile validation

Date: 2026-10-25. Project: D:/AI/AgentiX_v3. User approved unified local/remote profiles and safe diagnostics after the investigation.

## Investigation and delivered changes

The original local failure was reproducible from the code: SavedProfiles explicitly rejected Ollama, although Save profile was visible in local mode. The original external attempt was logged only as ValueError inside the old generic save wrapper, at its historical line 238. Its underlying cause cannot be reconstructed from those payload-free logs. A unique valid synthetic external profile saved, listed, read from the real Windows vault and deleted successfully in temporary storage. No original key or existing profile was read. Do not label that synthetic success as proof that the user's historical external failure is fixed.

Saved profiles now accepts Ollama metadata with an empty credential_ref, alongside unchanged legacy external records. Local profiles support save, refresh, select, apply, update and delete without constructing native credential storage. Readable Unicode names and model-style punctuation, such as Qwen3-coder:30b, are accepted within 64 printable characters; controls/markup are rejected. Local-to-remote conversion requires a new key, and remote-to-local conversion retires the old owned reference through the existing cleanup mechanism.

DeferredCredentialVault retains an explicit factory and initializes it only when a credential operation occurs. ProfileError carries closed fixed messages/codes and an optional numeric Windows status. Validation errors, credential writes and metadata writes are distinguishable without printing key values, raw vendor exception bodies or filesystem paths. The controller preserves the last safe failed-save reason through Refresh and preserves valid choices where possible. A failed precommit update leaves the old profile authoritative. A cleanup failure cannot replace the primary safe reason.

The native adapter preserves the legacy UTF-16 credential representation and explicitly checks Windows' 2560-byte blob limit before writing. Its generic ASCII format validator remains bounded; oversized UTF-16 blobs get key_storage_limit. This edge case is not established as the cause of the historical user failure. Source: https://learn.microsoft.com/en-us/windows/win32/api/wincred/ns-wincred-credentialw.

## Verification

| Check | Result | Evidence |
| --- | --- | --- |
| Initial feature regressions | Six failed before implementation | profiles-018-red.txt |
| Save then Refresh reason retention | Failed before UI correction | profiles-018-refresh-red.txt |
| Complete offline suite after all new negative tests | 421 passed, 27 deselected, 15 existing CrewAI warnings | profiles-018-offline-final.txt |
| Browser/framework/native-credential checks | 18 passed, 428 deselected; collected before two additional offline negative tests | profiles-018-integrations-first.txt |
| Ruff / formatting / references | Passed; 91 files formatted, no stale reference entries | profiles-018-ruff.txt, profiles-018-format.txt, profiles-018-reference.txt |

The explicit integration run comprises ten real Edge/Playwright scenarios on disposable Gradio, six installed CrewAI/Gradio checks and two native Windows credential integrations. Browser cases cover the exact local Save-then-Refresh flow, another session reloading/applying/deleting it, external create/update/delete, fixed-code credential denial, retention through refresh, password/consent clearing, and existing human acceptance/display regressions. Network/model/vault boundaries in browser fixtures are controlled doubles.

The added native integration joins an actual Gradio process_api callback, SessionState/owner routing, SessionModelConfiguration, temporary SavedProfiles metadata and real Windows Credential Manager. It stores a unique synthetic external key, reads only its own reference, refreshes the actual callback choices and deletes only its own temporary profiles/credentials in finally. No model inference, real supplier authentication, paid API call or existing user profile participates. Native AppContainer code was not changed and its prior evidence is not presented as a new run here.

Two extra offline checks after the integration collection cover an oversized blob before any native call and a simultaneous credential/cleanup failure retaining its primary reason. Product source was unchanged between that integration run and the final offline/quality checks. Existing external persistence, stale revisions, owner checks and secret-free metadata regressions remain passing. No historical hashes or reports were overwritten; profiles-018-source-hashes.json records the changed maintained files separately.

## Compatibility and operational limits

Existing external JSON and UTF-16 credentials remain compatible; no existing data is migrated or deleted. Older external-only application builds cannot read new Ollama profile records, so upgrade running instances before using the shared unified catalog. Each session still starts with local qwen3-coder:30b and saved remote profiles require fresh consent. Keys remain user/PC scoped in Windows Credential Manager, not protected against malware running as the same Windows user. Cross-service crash rollback, provider authentication and universal generated-code correctness are not claimed.

PROFILE-EXT-001 remains open for the cause of the historical external failure. In the updated application, retrying that operation should now return a bracketed safe code such as key_required, key_format, credential_unavailable, credential_write or metadata_write; a native numeric status may narrow the diagnosis. Share only that code, never the key. These changes resolve the local unsupported-profile behavior and hidden/lost error diagnostics; they do not justify inventing the original external root cause.

Existing live instances were not restarted as part of automated tests. Source/UI changes require an explicitly authorized application restart to become visible. No existing generated artifact, real key or user profile was inspected, modified or executed. English requirements, architecture, technical/user/install guides, incidents, authorization rules and source reference are synchronized. Local Ollama was requested for prose drafting only; its unverified draft/provenance are retained separately, and this final report is checked against raw evidence.
