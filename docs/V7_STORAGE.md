# AgentiX v7 storage

The AgentiX v7 source checkout contains maintained code, tests, assets, infra
and documentation. User packages and runtime dependencies are stored separately.

The reviewed V7 schema-2 deployment profile declares `home` as
`D:\AI\Agentix-data\v7` and `toolsRoot` as
`D:\AI\AgentiX_v7\generated_tools`. The managed launcher passes both exact
values to GUI and CLI through `AGENTIX_HOME` and `AGENTIX_TOOLS_ROOT`; launch
through that launcher to avoid a second catalog. The legacy V5 namespace is not
read, moved or deleted by this deployment.

```text
<home>/
  environments/<runtime-lock-prefix>/
  launchers/
  tooling/
  cleanup/                         owned PID/profile cleanup receipts
  logs/
  data/
    drafts/<session>/<operation>/<tool_name>/  unapproved proposals and operation evidence
    reviews/<opaque-id>/review.json
    approvals/tools/
    approvals/widgets/
    approvals/applications/
    model-profiles/

<toolsRoot>/
  <tool_name>/                          accepted/public tools only
    <tool_name>_specifications.md
    <tool_name>_code.py
    <tool_name>_tests.py
    <tool_name>_widget.py
    <tool_name>_widget.css
    <tool_name>_widget_tests.py

<home>/data/applications/<human-name-slug>/
  app.py
  application.json
  config.json
  operation.py
  application_context.py
  application_contracts.py
  element_ids.py
  package_tests.py
  <dependency>_code.py
  <dependency>_widget.py
  <dependency>_widget.css
```

An application name is required in the GUI. Its normalized folder is reserved
without overwriting another package. Paths, Windows device names and ambiguous
trailing punctuation are rejected. A hidden opaque ID remains in authenticated
metadata and browser callbacks; names are not authorization capabilities.

Application packages contain exact dependency snapshots to prevent silent changes
when a shared tool is edited. operation.py is the same application's headless
composite operation; using it does not create another tool directory.

Tool approvals contain code/test/policy hashes, allowed functions and reviewed
acceptance cases. Widget approvals include the reviewed proposal and exact code,
CSS and proposed-test bindings. Application approvals bind ID, name/folder, review,
policy and dependencies. All are protected with user-scoped Windows DPAPI. Hashes
identify content; they do not prove correctness or replace human authorization.

Model profile JSON stores provider, endpoint, model, revision and an opaque vault
reference. API key values remain in Windows Credential Manager. No v4 grants or
credentials are adopted. Source changes in this release require new verification.

Native Windows profiles are named Agentix.v5.<uuid>. After job/profile deletion,
only owned empty residual directories are removed. Nonempty/linked/blocked trees
retain diagnostics and pending cleanup. Recovery skips living or ambiguous owner
processes. Old v4/Lab profiles without v5 ownership receipts are not deleted.


## Version-3 connection-code applications

New catalog applications store generated `application_logic.py` alongside maintained
`app.py`, `operation.py`, `application_values.py`, `application_context.py` and
`element_ids.py`, plus unchanged dependency/widget snapshots. Their manifest stores
public input schemas and a presentation-only widget inventory. It contains no
workflow, binding version or execution order; ordinary Python source preserves the
connections. Versions 1/2 keep their original runtime/file closures.

The review editor's virtual `application_acceptance.json` is host-held review data,
not an executable package member. Its independently supplied payload/expected values
are persisted in the owner draft review and covered by explicit application review.
Saving source or cases revokes approval. Unchanged tool bytes and grants are never
rewritten by connection-code generation.

A scoped `<tool>_widget.css` is the one exception (V7-076): the style window writes
it through `agentix.application.style_member`, which validates the closed grammar,
rewrites the declared member hash in `application.json` and keeps the approval
valid. The application identity excludes style members and their declared hashes,
so capture still rejects a stylesheet edited outside that writer.


## V7-047: reviewed catalog migration

Explicit catalog relocation authenticates prior grants, preserves current v7
approvals and requires fresh gates for changed case bindings and applications.
Stale packages remain blocked, without silent runtime edits or grant overwrites.
See [scope, design and evidence](specs/047-catalog-migration.md).


## V7-048: installed application update

The explicitly reviewed updater stages maintained-template and dependency-review
changes while preserving generated logic, independent application cases and layout.
Fresh native/browser gates precede backed-up installation; current grants and v6
remain untouched. See [scope and evidence](specs/048-installed-application-update.md).


