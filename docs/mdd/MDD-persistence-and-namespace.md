# MDD — Persistence, Namespace Isolation & Catalog Migration

Criticality score **77.0 / 100** (centrality 4, security 4, business 3, complexity 4,
persistence 5, extensibility 3). Terminology: see [README](README.md#shared-terminology).

This component has three distinct responsibilities that share one storage root.
They are documented in separate subsections below and must not be read as one
mechanism.

- **4.1 Namespace isolation** — which paths are legal at all.
- **4.2 Catalog reads and publication** — how the Tools catalog is listed and how a
  reviewed draft becomes public.
- **4.3 Catalog migration** — how authenticated grants move between two v7 roots.

## 1. Purpose and Responsibilities

Responsibilities:

- Reject any path inside the retired v5 namespace and require explicit v7 roots
  (`require_v7_namespace`, `user_home`, `data_directory`,
  `Settings.from_environment`).
- Render the read-only Tools catalog and expose contracts (`ToolCatalog.contains`,
  `render`, `contracts`).
- Publish reviewed draft bytes into the public catalog
  (`publish_tool_draft`).
- Serialise cross-process catalog operations (`CatalogLock`, `reject_alias`).
- Plan and apply authenticated grant relocation between v7 roots with a review
  digest (`CatalogMigration.plan`, `apply`).
- Remove catalog entries with a prepared confirmation (`CatalogMaintenance`).

Explicit non-responsibilities:

- It does not approve or verify anything
  ([MDD-acceptance-and-verification.md](MDD-acceptance-and-verification.md)).
- It does not decide install eligibility
  ([MDD-installed-application-catalog.md](MDD-installed-application-catalog.md)).
- It does not migrate v5 data. See section 4.3.
- It does not create directories while resolving a path.

Layer: storage foundation. It depends on `security` for sealing and policy and on
no application or controller module.

## 2. Source Code Mapping

| File | Symbols |
| --- | --- |
| `src/agentix/storage/locations.py` | `_LEGACY_NAMESPACES`, `require_v7_namespace`, `user_home`, `data_directory` |
| `src/agentix/settings.py` | `Settings`, `Settings.from_environment`, `data_directory`, `tools_root` |
| `src/agentix/storage/catalog.py` | `ToolCatalog` (`contains`, `render`, `contracts`) |
| `src/agentix/storage/tool_publication.py` | `publish_tool_draft` |
| `src/agentix/storage/catalog_lock.py` | `reject_alias`, `CatalogLock` (`__enter__`, `__exit__`) |
| `src/agentix/storage/catalog_migration.py` | `fingerprint`, `CatalogMigration` (`plan`, `apply`, `_read`, `_path`, `_records`, `_decode`, `_grant`, `_tool`, `_widget`, `_application`, `_fresh`) |
| `src/agentix/storage/maintenance.py` | `Removal`, `package_digest`, `remove_tree`, `CatalogMaintenance` (`prepare_tool`, `prepare_app`, `confirm`) |

Entry points: `Settings.from_environment`, `ToolCatalog.render`,
`publish_tool_draft`, `CatalogMigration.plan`/`apply`,
`CatalogMaintenance.confirm`.

## 3. Architecture and Dependencies

Internal: `security/approval_store.py` (`ApprovalStore`, `policy_fingerprint`),
`security/data_protection.py`, `security/reuse_policy.py`,
`lab/application_artifacts.py` (`application_digest`), `storage/usage.py`.

External: standard library only; `msvcrt`-style locking is not used — the lock is
file-based with a timeout.

Dependency direction: everything depends on this component; it depends on
`security` and, for migration, on `lab`. That `storage` → `lab` edge is the one
layering inversion in the component.

Ports and adapters: `protector` is injected into `CatalogMigration` and
`CatalogMaintenance`; `verifier` and `widget_verifier` are injected callables, so
migration can require real native/browser gates without importing them.

## 4. Execution and Data Flow

### 4.1 Namespace isolation

`Settings.from_environment` requires `AGENTIX_HOME` and `AGENTIX_TOOLS_ROOT`,
resolves both, and passes each through `require_v7_namespace`. `user_home` rejects
relative roots, `..` segments, symlinks and reparse points on every ancestor.
`require_v7_namespace` compares whole case-folded path segments against
`("agentix", "v5")` and `("agentix-data", "v5")`, so a directory merely containing
`v5` in its name is accepted while the retired namespace is refused.

There is no default path. A missing variable raises rather than falling back.

### 4.2 Catalog reads and publication

```mermaid
flowchart LR
    D[Draft root owner/operation] --> P[publish_tool_draft]
    P --> L[CatalogLock]
    L --> C[Public catalog]
    C --> R[ToolCatalog.render]
    R --> M[Manager prompt]
```

`ToolCatalog.render` lists entries and their contracts read-only; `contains`
answers membership without loading bytes. `publish_tool_draft` copies the reviewed
draft members into the public root under the catalog lock. `CatalogLock` uses a
lock file with a 3-second default timeout and `reject_alias` refuses a lock path
that is a reparse point.

### 4.3 Catalog migration mechanism

`CatalogMigration` relocates **authenticated grants between two v7 roots** on the
same machine — for example from a staging root to the live root. It is not a
v5→v7 data migration.

`plan()` reads source records, decodes them, re-derives each grant against the
target root, and returns per-item status plus a `review_digest` over the item list,
input fingerprints and policies. `apply(reviewed_digest)` recomputes the plan,
refuses a stale digest, then for each item: re-reads inputs (`_fresh`), runs the
injected `widget_verifier` or `verifier` when the item requires fresh gates,
re-checks the application digest, writes a backup, seals the record, and creates
the destination with exclusive mode `xb` so an existing grant is never
overwritten. Per-item failures are recorded as `blocked` with a bounded reason and
do not abort the remaining items. A `receipt.json` records the operation.

Explicit statement: **v5 persisted Tools, Applications and approvals are not
migrated, adopted or read.** `require_v7_namespace` rejects those roots, and no
code path in this component accepts a v5 source. Historical v5 data remains
outside AgentiX v7 by design.

### 4.4 Removal

`CatalogMaintenance.prepare_tool`/`prepare_app` return a `Removal` describing exact
bytes and dependents; `confirm` performs the deletion with `remove_tree`, which
removes code last. `package_digest` binds the prepared removal to the bytes the
operator saw.

Inputs and outputs: paths and environment for 4.1; a draft root and tool name for
4.2; a reviewed digest for 4.3; a `Removal` for 4.4.

Error handling: 4.1 raises `ValueError`; 4.2 raises on alias or lock timeout; 4.3
records per-item `blocked` and returns the plan; 4.4 refuses a changed digest.

## 5. Contracts and Invariants

Public interfaces: `Settings.from_environment(environment=None) -> Settings`,
`require_v7_namespace(path, label) -> Path`,
`publish_tool_draft(staging_root, public_root, tool_name) -> None`,
`CatalogMigration.plan() -> dict`, `CatalogMigration.apply(reviewed_digest) -> dict`,
`CatalogMaintenance.confirm(removal) -> None`.

Preconditions: `AGENTIX_HOME` and `AGENTIX_TOOLS_ROOT` must be absolute and
outside the v5 namespace. `apply` requires a digest equal to a freshly computed
plan. `confirm` requires an unchanged package digest.

Postconditions: resolving a path creates nothing; `apply` never overwrites an
existing destination; `publish_tool_draft` leaves the draft in place.

Data contracts: migration records are sealed and limited to 262144 bytes; source
reads are limited to 1048576 bytes; the plan carries `items`, `inputs`,
`policies`, `review_digest`, and after `apply` also `operation_id` and `evidence`.

Security invariants:

- No v5 path is accepted anywhere in this component.
- Aliases and reparse points are rejected before any write.
- Destination creation uses exclusive mode, so a race cannot overwrite a grant.
- Migration never treats a native/browser failure as approval evidence.
- `remove_tree` deletes code last, so a partial removal cannot leave executable
  bytes without their record.

Persistence constraint: the on-disk layout is `AGENTIX_HOME/data/{tools,
applications,reviews,approvals,...}` plus `AGENTIX_HOME/migrations/<id>` for
operation evidence. `AGENTIX_TOOLS_ROOT` may differ from the data root; both are
validated independently.

## 6. Security and Reliability

Trust boundaries: environment → roots (validated); source root → target root
(authenticated relocation); operator → removal (digest bound).

Authorization and human review: `apply` requires an exact reviewed digest, and any
item needing fresh gates requires an injected verifier that must return `True`.

Sensitive data: records are sealed; log events carry operation ID, kind, outcome
and duration, never record bodies.

Failure modes and recovery:

| Failure | Behaviour |
| --- | --- |
| `AGENTIX_HOME` unset | `ValueError`, no fallback |
| Path inside v5 namespace | `ValueError` naming the resolved path |
| Symlink or reparse point | `ValueError("Data aliases are forbidden")` |
| Lock timeout | `CatalogLock` raises after 3 seconds |
| Stale migration digest | `ValueError("Exact migration review digest required; review is stale")` |
| Existing destination grant | exclusive create fails, item `blocked` |
| Verifier returns non-`True` | item `blocked`, no write |
| Changed package before removal | `confirm` refuses |

## 7. Testing and Verification

| Test file | Coverage |
| --- | --- |
| `tests/test_v5_locations.py` | Namespace rejection, alias rejection, mandatory roots |
| `tests/unit/test_config.py` | `Settings.from_environment` requirements |
| `tests/test_application_catalog.py` | `ToolCatalog` render and contracts |
| `tests/unit/test_tool_publication.py` | Draft publication, no overwrite |
| `tests/test_catalog_lock.py` | Lock timeout and alias rejection |
| `tests/test_catalog_migration.py` | Plan/apply, stale digest, per-item blocking, injected verifiers |
| `tests/test_catalog_maintenance.py` | Prepare/confirm removal |
| `tests/unit/test_security_storage_isolation.py` | v5 namespace refusal end to end |

Focused command: `python -m pytest tests/test_v5_locations.py tests/test_catalog_migration.py tests/unit/test_security_storage_isolation.py`

## 8. Architectural Findings

Strengths, evidenced:

- Namespace isolation is enforced at path resolution, so every consumer inherits
  it without repeating the check.
- Migration is review-digest bound and never overwrites, which makes a partial run
  inspectable rather than destructive.
- Removal deletes code last and is digest bound.

Technical debt, evidenced:

- `catalog_migration.py` is 398 lines and reaches into `ApprovalStore` internals
  (`_path`, `_decode`, `_records`) rather than a public reader interface.
- `CatalogMigration` and `ApplicationUpdates` share the same `_records`/`_decode`
  private helpers, so the update path depends on migration internals.
- `CatalogLock` has a fixed 3-second default with no caller override in most
  call sites.

Risks:

- `apply` is explicitly not crash-atomic across files; a crash mid-run leaves a
  partial set that only the receipt and backups can explain.
- `require_v7_namespace` compares segments only, so a v5 root reached through a
  junction that resolves outside those names is caught by the alias check, not by
  the namespace check.

Extension points: injected `protector`, `verifier` and `widget_verifier`;
`CatalogMaintenance` accepts revoke callbacks; `ToolCatalog.render` is the single
place to change catalog presentation.

## 9. Traceability

Source: as listed in section 2. Tests: section 7.

Related documentation: [`V7_STORAGE.md`](../V7_STORAGE.md), specs
[037](../specs/037-v5-structure-and-workspace.md),
[047](../specs/047-catalog-migration.md),
[055](../specs/055-iac-v7-storage-roots.md),
[`docs/reference/src__agentix__storage__locations.md`](../reference/src__agentix__storage__locations.md),
[`docs/reference/src__agentix__storage__catalog_migration.md`](../reference/src__agentix__storage__catalog_migration.md).

## 10. Open Questions

- Whether `AGENTIX_TOOLS_ROOT` is intended to ever differ from
  `AGENTIX_HOME/data/tools` in a supported deployment is not stated; the code
  allows it and validates both.
- The intended recovery procedure for a partially applied migration is described
  only by the receipt and backups, not by a documented operator runbook.
