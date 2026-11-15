# V5-038: permanent catalog deletion and rejected-tool repair

Status: approved on 2026-10-29, including permanent deletion (no recycle bin).
The user confirmed the intended filename is <tool_name>_tests.py, not _text.py.

## Observable acceptance

- DEL-01: Tools and Applications provide Delete selected tool/application below
  their catalogs. Two-step explicit confirmation defaults to cancellation; tokens
  are server-owned, session-bound, one-use and bound to exact current content.
- DEL-02: Installed application/composite dependencies block tool deletion even
  if the dependent package's source is currently invalid. Unreadable/corrupt
  dependency metadata fails closed. No cascade removal.
- DEL-03: Running/open application and headless operation leases prevent app
  deletion across sessions/processes. Closing releases ownership; dead-owner
  leases may be recovered conservatively. New leases and catalog mutations share
  a cross-process lock. No process is terminated by Delete.
- DEL-04: Validate exact owned package containment and every tree member; reject
  reparse points and stale changes. Revoke authorization before permanent removal.
  Failure is reported; no transactional rollback is promised. No arbitrary browser
  paths, wildcard deletion, v4 data or excluded project generated_tools inspection.
- REPAIR-01: Capture only an actually rejected owner/request proposal; allow
  inspection/editing of its available code and tests, including a rejected
  not-yet-written code/test proposal. Reject stale/foreign requests.
- REPAIR-02: Save and restart is a new explicit user operation. Validate both
  buffers before any write; block updates of tools referenced by installed apps;
  revoke old grants. Run native unittest verification again. Success is provisional.
- REPAIR-03: Generate declarative acceptance proposals through a bounded injected
  model boundary, preserve manual acceptance review and independent host comparison.
  No model-driven file rewrite, automatic retry after rejection or child execution
  on the host. Changed artifacts never inherit old approvals.

## Architecture and testing

Views in ui, owner/confirmation callbacks in controllers, repair workflow in
application and dependency/removal/usage services in storage. Tests use trusted
temporary packages and explicit model doubles. Add real GUI confirmation, blocking,
cancellation and rejection/edit/revalidation scenarios on disposable servers.

Dependency provisioning and semantic retrieval are research only in this block;
no new package/model installation, paid inference or expanded native privileges.
