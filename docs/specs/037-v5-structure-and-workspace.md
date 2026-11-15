# V5-037: independent architecture and review workspace

Status: approved and delivered as V5-037; current follow-up evidence and limitations are in ../reports/V5_039_DELIVERY_REPORT.md.

Preserve v4, its live processes and all excluded generated_tools. No existing user
data, credentials, grants or virtual environments are adopted.

## Requirements and observable acceptance

- ARCH-01: Gradio views live in ui; owner/session controllers in controllers;
  workflow coordination in application; adapters and security/storage/sandbox code
  have explicit topic packages. Canonical package paths are the only supported
  internal import paths: no `sys.modules[__name__]` compatibility alias remains in
  maintained source. Offline behavior must remain unchanged.
- DATA-01: v5 has one explicit per-user data root, independent of packaged-host
  LOCALAPPDATA virtualization. No production default writes into generated_tools.
- APP-01: require an English application display name, derive a safe Windows folder
  name, reject collisions and traversal, retain opaque identity only in metadata.
- CLEAN-01: track owned native profiles; close jobs before removing profiles and
  empty residual folders. Never enumerate/delete another version's profiles or
  follow links. Persist pending cleanup and retry with bounded diagnostics.
- CSS-01: co-locate widget Python, CSS and proposed widget tests. Bind CSS to review
  and package integrity; disallow external resource loading and global selectors.
- EDIT-01: all supported inputs/results/buttons have visible move/resize handles
  and hover halos in edit mode; relocating controls leaves no container lines.
- REVIEW-01: equal-height code panes, adjustable common height and column widths,
  internal editor scrolling and accessible resize controls.
- HELP-01: context chat has separate ui/chathelper.py and controllers/chathelper.py.
  Context contains current editor text, specification, filename/type, tool I/O
  contract and widget context contract where relevant. No other files or logs.
  Read-only assistance; per-session history, explicit remote consent, bounded
  context/output, no tool execution; floating movable/resizable/minimizable UI.

## Delivery order

1. Independent curated copy, characterization, package separation and runtime roots.
2. Named application persistence and owned sandbox cleanup.
3. Per-widget CSS and consistent visual editor/review sizing.
4. Code assistance, browser/native regression and synchronized English references.

## Evidence rules

Inherited v4 reports are antecedents. Tests use trusted temporary fixtures. Real
framework, browser, native and model evidence are distinguished. Provisioning and
launch require a v5-specific plan and exact interpreter; no v4 environment serves
as deployed v5 runtime. Use a new loopback port (7878), fail if occupied.
