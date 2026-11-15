# Current limitations and incident routing

Updated 1 November 2026. [V7_INCIDENTS.md](V7_INCIDENTS.md) preserves historical V5 causes, solutions and regressions; [HISTORY.md](HISTORY.md) preserves inherited incident IDs. Old snapshots are not current test results.

- **PUB-001:** unapproved creation/repair bytes now remain under owner-bound
  drafts and are copied to the public tool catalog only after acceptance. The
  new policy fingerprint invalidates prior durable tool grants. Publication is
  not claimed crash-atomic.

- **V7-ERR-068:** re-running an unchanged test suite or polling status no longer
  deletes a durable tool approval; only explicit revocation (catalog deletion,
  repair, rejection, changed bytes or policy) removes it. The running 7878 process
  keeps the previous code until the owner relaunches it. See
  [incident record](V7_INCIDENTS.md).
- **V5-ERR-041-01:** the approved general binding extension is implemented and fixture-verified on disk; the existing 7880 process is not restarted. Existing live application semantics are not established by fixture tests. See [workflow binding specification](specs/041-general-workflow-bindings.md).
- **V7-ERR-005:** `app_policy()` no longer hashes `storage/maintenance.py`, so removal fixes stop invalidating installed approvals; the digest still covers every execution member and `get()` still refuses a stale policy. One final re-verification is required because the policy changed. The running process keeps the previous code until the owner relaunches it. See [specification](specs/061-catalog-services-outside-policy.md).
- **V7-ERR-004:** `Delete selected application` no longer reports `Application approval is stale`; removal verifies identity, exact bytes and the review, and keeps the usage and dependency checks. A stale application still cannot be launched and still requires `Re-verify selected app` before execution. The running process keeps the previous code until the owner relaunches it. See [specification](specs/060-stale-policy-removal.md).
- **V7-ERR-003:** a public input schema carrying `minimum`/`maximum` or any other JSON Schema keyword is rejected by name instead of the generic `(ValueError)`, and the plan prompt now forbids those keywords. The contract stays closed to `type`, `description`, `enum` and `items`. The running process keeps the previous code until the owner relaunches it. See [specification](specs/059-closed-input-schema-diagnostics.md).
- **V7-ERR-002:** a session with no saved profile selected now reports `profile_not_selected` instead of the changed-digest text, logs the rejection, and `demo.load` auto-selects the only saved profile for editing. Zero or several profiles stay an explicit choice. The running 7878 process keeps the previous code until the owner relaunches it. See [specification](specs/058-profile-selection-diagnostics.md).
- **V5-ERR-039-21:** Close/Play polling race fixed and regression-tested on disk. The user explicitly requested no restart of 7880; that running instance does not yet contain the last source fix.
- **LAB-002-TRANSPORT / native transport:** direct host access to an AppContainer HTTP listener and the experimental named-pipe alternative retain documented limitations/strict xfails. The maintained ASGI/IPC bridge is required. Never replace it with host execution or expand network rights to hide a failure.
- Generated code and generated tests remain untrusted. Human source/test review and independent host-compared acceptance are mandatory. Finite passing cases do not prove general correctness or honest tests. Incorrect model expectations and invented Gradio APIs required human corrections in V5-039.
- General applications use approved canonical catalog tools, a bounded typed DAG and a maintained compositor. Tested contracts have scalar inputs and scalar/list outputs. Arbitrary third-party dependency provisioning, dynamic model-planned call trees and semantic/vector tool retrieval are not delivered. V7-055 permits only the separately declared, user-confirmed host Playwright Chromium repair; it is not a general package installer.
- Model/request limits are bounded safeguards, not instant cancellation or immunity to prompt injection. External DNS validation does not close every DNS-rebinding window. Credentials exist briefly in browser/request/client memory; secure zeroization is not promised.
- AppContainer cleanup removes only proven-owned inactive resources. Unknown historical directories, nonempty contents and Windows locks can prevent immediate cleanup. No blanket deletion of Packages directories.
- Filesystem operations and external installs are not cross-service transactions. A failed permanent catalog removal may leave unauthorized partial files; credential/metadata interruption can leave cleanup work. No rollback guarantee.
- Same-user host malware, valid-record rollback and already-dispatched concurrent operations are residual trust limits. Browser session routing is not Windows account authentication.
- Python 3.11.9 remains intentionally pinned; its lifecycle risks were not resolved by IaC. This PC's provisioning is not a verified clean-Windows installation. No graphical installer is delivered.
- Current demonstration at 7880 uses an owned temporary validation profile. Do not assume its packages survive OS temporary-file cleanup. Geometry save passed; post-reopen geometry was not separately asserted in V5-039.

- **V7-ERR-075:** `tests/test_v5_review_browser.py::test_review_resize_and_context_help`
  carries a strict `xfail`. V7-068 moved `#application-candidates-accept` inside
  the closed `#applications-sidebar`, and the test never opens it, so the click
  waits for a hidden element. The flow passes with the sidebar toggle clicked;
  the repair changes the geometry asserted later in the same test and needs its
  own approved block. `xfail_strict = true` turns an unexpected pass into a
  failure. See [specification](specs/075-code-help-mermaid-rendering.md).

- **Pending UI consolidation:** only the Applications validation errors and "Save reviewed changes" confirmations use the shared `MessageDialog` modal (`src/agentix/ui/message_dialog.py`). Routing every Applications status message through that same modal remains an approved-but-deferred task; the streaming status Markdown is unchanged for now.

Verify current markers and test output before quoting counts. Do not reinterpret skips, xfails, simulated isolation or historical screenshots as current native/model verification.
