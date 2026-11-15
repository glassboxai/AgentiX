# AgentiX v7: tool and application storage and approval

## Purpose

This document explains where AgentiX v7 stores approved tools and installed applications, what an approval represents, and how maintained-code changes can make an existing approval stale.

An approval is not a permanent statement that an artifact is safe under every future version of AgentiX. It authorizes specific artifact content under a specific host policy and storage identity. Hashes detect whether those bound inputs have changed; they do not prove that the code is correct or replace human review and verification.

## Storage roots

The checked-in deployment profile is `infra/windows.local.json`. Its schema-2 configuration declares:

- `home`: `D:\AI\Agentix-data\v7`
- `toolsRoot`: `D:\AI\AgentiX_v7\generated_tools`

The managed launcher passes these as `AGENTIX_HOME` and `AGENTIX_TOOLS_ROOT`.

The current layout is therefore:

```text
D:\AI\Agentix-data\v7\
  data\
    drafts\                         unapproved proposals and operation evidence
    reviews\                         application review data
    approvals\
      tools\                        protected durable tool approvals
      widgets\                      protected widget approvals
      applications\                 protected installed-application approvals
    applications\                   installed application packages
    model-profiles\                 model profile metadata

D:\AI\AgentiX_v7\generated_tools\
  <tool_name>\                       accepted/public tool artifacts
```

Tools and applications have separate artifact locations and separate approval records. Application packages include snapshots of their reviewed dependencies; they do not create or replace entries in the public tools catalog. See [V7 storage layout](V7_STORAGE.md) and [the deployment profile](../infra/windows.local.json).

## What a tool approval binds

The durable tool approval is stored outside the public tool directory, under the configured data root. `src/agentix/security/approval_store.py` creates a protected record associated with the canonical tools-root path and tool name. The record binds, among other validated metadata:

- SHA-256 hashes of that tool's exact code and test bytes;
- the current host policy fingerprint;
- approved function identities and the reviewed acceptance contract.

Approval records are protected using user-scoped Windows Data Protection (DPAPI). Protection prevents a record from being treated as an ordinary, user-editable trust marker; it does not make stale content valid. Loading an approval checks its identity, policy and exact artifact hashes. Missing, changed or invalid bindings grant no durable approval.

The current tool policy fingerprint is computed by `policy_fingerprint()` in `src/agentix/security/approval_store.py`. It starts with the domain/version seed `AgentiX-reviewed-approval-v2`, then incorporates each listed relative path and the bytes of that maintained source file:

```text
src/agentix/security/approval_store.py
src/agentix/security/data_protection.py
src/agentix/security/reuse_policy.py
src/agentix/security/verification.py
src/agentix/execution.py
src/agentix/security/acceptance.py
src/agentix/sandbox/__init__.py
src/agentix/sandbox_worker.py
src/agentix/sandbox/windows_process.py
src/agentix/sandbox/profile_cleanup.py
src/agentix/storage/locations.py
src/agentix/application/tool_repair.py
src/agentix/agents/repair_acceptance.py
src/agentix/security/paths.py
src/agentix/security/__init__.py
src/agentix/storage/tool_publication.py
src/agentix/domain/tool_schema.py
```

These modules cover the host mechanisms around authorization and use of tools: approval storage/protection, reuse and verification policy, acceptance, execution and sandboxing, path checks, repair and publication, and the tool contract. The fingerprint is deliberately an explicit source list, not a hash of the whole repository.

## What an application approval binds

Installed applications are stored under:

```text
D:\AI\Agentix-data\v7\data\applications\<human-name-slug>\
```

Their protected approval records are separate, under `data\approvals\applications`; review data is stored under `data\reviews`. The application catalog implementation is `src/agentix/storage/installed_apps.py`.

An installed application approval binds the application identity and storage root, display name and folder, the application package digest, a digest of the review data, the current application policy fingerprint, and the approved catalog dependencies. Publication accepts only a reviewed and independently verified candidate. The installed catalog checks the policy, package digest and review digest when retrieving an application. Exact dependency snapshots in the package prevent a shared tool edit from silently changing the installed application's dependency bytes.

The package digest is calculated from validated package-member names and their exact bytes by `application_digest()` in `src/agentix/lab/application_artifacts.py`. The package manifest and runtime lock are also checked as part of package validation. The digest identifies those bytes; review and verification are still required for authorization.

The current application policy fingerprint is computed by `app_policy()` in `src/agentix/storage/installed_apps.py`. It starts with the domain/version seed `AgentiX-v5-installed-app-v1`, incorporates each listed relative path and the bytes of that maintained source file, and also incorporates `infra/runtime.lock.txt`:

```text
src/agentix/storage/installed_apps.py
src/agentix/widgets/styles.py
src/agentix/storage/locations.py
src/agentix/storage/catalog_lock.py
src/agentix/storage/usage.py
src/agentix/storage/maintenance.py
src/agentix/sandbox/profile_cleanup.py
src/agentix/application/app_controls.py
src/agentix/layout_contracts.py
src/agentix/lab/widget_bridge.py
src/agentix/lab/application_panel.py
src/agentix/ui/assets/application_editor.js
src/agentix/lab/application_artifacts.py
src/agentix/application/general_package.py
src/agentix/application/general_pipeline.py
src/agentix/application/general_acceptance.py
src/agentix/application/templates/code/app.py
src/agentix/application/templates/code/operation.py
src/agentix/application/templates/code/application_context.py
src/agentix/domain/application_code.py
src/agentix/domain/tool_schema.py
src/agentix/lab/application_session.py
src/agentix/lab/widget_worker.py
src/agentix/sandbox/windows_process.py
infra/runtime.lock.txt
```

This list covers the maintained application lifecycle: storage and catalog coordination, review and acceptance, package and dependency validation, application templates and connection-code contracts, widget/UI bridging, worker execution and sandbox controls, plus the locked runtime. It is broader than the tool list because an application is a composed package with installation, dependency and presentation/layout concerns in addition to execution.

## Why a code change can require revalidation

The policy fingerprint is checked as part of approval validity. If the bytes of any file in the applicable policy list change, its fingerprint changes. An approval made under the old fingerprint no longer matches the current one, even if the artifact's own code has not changed. An edit to a listed file can therefore require a fresh review/verification step even when the edit is behaviorally unrelated to the approved artifact. This is a conservative byte-identity rule, not a semantic analysis of the change.

A change to maintained code that is not included in the applicable list does not, by itself, alter that policy fingerprint. Artifact changes are checked separately: changed tool code/tests, changed application package bytes, changed review data, or changed dependencies can also make the corresponding approval stale.

Revalidation does not inherently mean regenerating an artifact. Existing tool or application files may remain installed, while the prior authorization is no longer accepted; the current review and verification workflow must establish a valid approval again before use.

The tool and application fingerprints are separate because their reviewed security boundaries differ. Tool approvals emphasize tool publication, callable contracts, acceptance, execution and reuse. Application approvals also cover composed-package validation, dependency snapshots, installation, layout/widget handling and application runtime behavior. Both lists are explicit so unrelated repository changes do not automatically invalidate every approval.

## Source of truth and limitations

The current configuration and behavior described here are reflected in:

- `infra/windows.local.json` and `infra/Agentix.Iac.psm1` for deployment roots and launcher environment;
- `src/agentix/settings.py` and `src/agentix/storage/locations.py` for explicit path resolution;
- `src/agentix/security/approval_store.py` for protected records and tool policy fingerprints;
- `src/agentix/storage/installed_apps.py` and `src/agentix/lab/application_artifacts.py` for application policy, package identity and installed-application checks;
- `docs/V7_STORAGE.md` for the documented storage layout.

The fingerprint lists are the operative source-level bindings: edits to those lists or their hashing behavior change how policy identity is determined. The hashes are authorization invalidation signals, not proof of correctness, and finite acceptance cases do not establish universal correctness of a tool or application.
