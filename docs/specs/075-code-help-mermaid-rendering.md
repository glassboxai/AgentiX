# V7-075: Mermaid rendering in the read-only Code Help transcript

Approved scope: the Applications `Code help` panel renders a fenced Mermaid
diagram produced by the model as an inline SVG, using a locally vendored,
digest-pinned bundle. Nothing else changes: no new route, no network fetch, no
execution or editing capability, no generated source, no live process.

## Requirement

Observable acceptance:

- The transcript is a Markdown component, so a ```` ```mermaid ```` fence is no
  longer displayed as literal text.
- A fenced Mermaid block inside `#chathelper-transcript` becomes an inline `<svg>`
  after the answer arrives, and again after a later answer replaces the content.
- Mermaid source outside the helper, including generated application output, is
  never rendered.
- The bundle is served from the packaged UI assets, with no CDN, `unpkg`,
  `jsdelivr`, `esm.sh` or `<script src=` reference.
- A diagram Mermaid cannot parse keeps its source visible and marked, instead of
  looping or blanking the transcript.

## Design

`src/agentix/ui/chathelper.py` builds the transcript as `gr.Markdown` with the
unchanged `chathelper-transcript` element id. `src/agentix/ui/assets/mermaid_render.js`
scopes a `MutationObserver` to that element and handles both shapes a fence can
take: Gradio's own `<div class="mermaid">` and a `pre > code.language-mermaid`
block, which it converts. Each diagram is drawn with `mermaid.render` under
`securityLevel: 'strict'`, with a bounded three-attempt retry because Mermaid's
internal render queue can strand the first task pushed while it drains at page
load. Failed blocks receive the `mermaid-failed` class and are excluded from the
selector, so the observer cannot retry them indefinitely.
`src/agentix/ui/branding.py` concatenates the renderer and the bundle into the
existing launch-time `js` option, after the maintained scripts, so the bundle's
`"use strict"` directive does not change the mode of the other assets.

Gradio executes that `js` string inside `eval`, where the bundle's top-level
`var __esbuild_esm_mermaid_nm` stays local and its own final assignment reads an
undefined `globalThis` property. `branding.mermaid_script()` therefore wraps the
unchanged bytes in an IIFE and republishes `globalThis.mermaid` from the local
binding; the vendored file itself is never edited.

## Vendored dependency

| Property | Value |
| --- | --- |
| Package | `mermaid` |
| Version | 11.12.2 |
| File | `src/agentix/ui/assets/mermaid.min.js` |
| SHA-256 | `d0830a6c05546e9edb8fe20a8f545f3e0dc7c4c3134d584bad9c13a99d7a71e0` |
| Origin | Local `@mermaid-js/mermaid-cli` installation; no download performed |
| Licence | MIT |

The digest is asserted by
`tests/test_v7_075_code_help_mermaid.py::test_vendored_bundle_matches_the_pinned_digest`,
so an unreviewed replacement fails the offline suite. Updating the bundle
requires a new digest, a renewed review and a new specification revision.

## Security

The model answer remains untrusted data. Markdown keeps Gradio's sanitisation,
`securityLevel: 'strict'` disables click handlers and raw HTML inside diagrams,
and the renderer never evaluates model text as JavaScript. Rendering stays inside
the read-only helper; the helper still has no execution, editing or approval
capability.

## Verification

- `tests/test_v7_075_code_help_mermaid.py` (offline, `frameworks` and `browser`),
  including a real Gradio launch that proves `window.mermaid` is published and a
  fence renders without page errors.
- `tests/test_v5_review_browser.py` asserts the transcript text through the
  Markdown component, and carries a strict `xfail` for the V7-068 sidebar layout
  regression described below (`1 xfailed` on 2026-11-13).
- `tests/test_ui_stylesheet.py` keeps the transcript styling in the maintained
  stylesheet.
- Full offline suite with the managed interpreter on 2026-11-13:
  `1072 passed, 97 deselected` in 354 s, exit 0; re-run after the strict `xfail`
  was added: `1072 passed, 97 deselected` in 358 s, exit 0.
- Ruff lint and format clean on 295 files; `tools/build_reference.py --check`
  reports no issues.

## Known pre-existing failure

`tests/test_v5_review_browser.py` stops before the Code Help step because
`#application-candidates-accept` now lives inside the closed
`#applications-sidebar` introduced by V7-068; the test never opens it. The same
flow passes when the sidebar toggle is clicked, verified on 2026-11-13 against a
disposable server.

Under the owner's decision D the test now carries a strict `xfail` with that
cause in its reason, so the suite reports `1 xfailed` instead of a red browser
run, and `xfail_strict = true` turns an unexpected pass into a failure that
demands removing the marker. The layout repair itself remains outside this
block.
