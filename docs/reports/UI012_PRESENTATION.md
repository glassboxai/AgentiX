# UI-012: AgentiX presentation verification

Date: 2026-10-20. Status: implemented and verified within the approved UI block.

## Result

The GUI now uses the supplied AgentiX logo at the left of the header, AgentiX
immediately to its right and the approved three-line description alongside it.
The supplied stylesheet informed the near-black/cyan palette, subtle borders and
panel treatment. The application uses local Inter with Arial/sans-serif fallback;
it makes no external font request. The local PNG is also the favicon. Interface
emoji and chat toolbar icons are removed. The send button is a compact arrow
whose accessible name remains Send query. Native disclosure arrows remain.

The UI deterministically renders existing host-observed records as readable
fields and tables. It does not invoke a model to rewrite the answer, execute the
result text or invent a successful observation. Literal decoding is bounded by
text size/node count and display depth. Unsupported output falls back to escaped
text; the technical record remains in a disclosure and truncation is marked.
Euro context must be explicit in the original query. Finer-grained rates retain
their observed precision. Agent/CLI result records remain unchanged.

Validation displays stage and counts above a bounded scrolling list. Individual
expected/observed case data appears on expansion. Provisional output and complete
Python tests are available in review disclosures. The editable review box, IDs,
ownership and mandatory human approval behavior are unchanged. Catalog names
remain visible while signatures/descriptions are folded per tool; agents still
receive the original AST catalog text. Third-party verbose messages and technical
events remain in the owning session's activity disclosure.

## Verification and evidence

Characterization of the existing controller/review tests passed before editing.
The new presentation module tests first failed because the behavior did not yet
exist (`ui012-red.txt`). Evidence is retained separately from historical hashes.

| Check | Observed result | Raw evidence |
| --- | --- | --- |
| Offline suite | 316 passed, 19 opt-in cases deselected | ui012-offline-verified.txt |
| Real framework adapters | 5 passed, no model/server | ui012-frameworks-final.txt |
| Disposable browser suite | 5 passed | ui012-browser-verified.txt |
| Ruff lint / format | Passed, 78 active Python files | final tool output |
| Source snapshot | 78 Python files and 2 local assets | ui012-source-hashes.json |

Browser checks use independent trusted temporary fixtures. They verify edited
acceptance/owner separation/rejection, file review and desktop/mobile presentation
at widths 1440/390. The display fixture contains the independently authored
67.50 example and sixteen cases; it is not a fresh model execution. Tests verify
the result table, accessible send action, collapsed evidence, bounded case area,
disclosures remaining usable across timer ticks, folded catalog, computed Inter
font stack, no page overflow and result contrast of at least 4.5:1. Screenshots
were inspected after the automated checks; functional success alone did not
establish visual quality. Tables scroll horizontally on narrow screens.

The new actual application is open at `http://127.0.0.1:7871/`, with an empty
temporary catalog outside the excluded project directory. Its launcher retains
qwen3-coder:30b and native isolation. No new real-model query was submitted for
this presentation-only block. `ui012-live-manifest.json` and `ui012-live.png`
identify the instance. The existing port-7870 application was not restarted.

## Incidents and fixes

- UI012-ERR-001: the CSS send glyph became part of the accessible name. All five
  initial browser checks failed on the exact-name locator (`ui012-browser.txt`).
  Empty CSS alternative text makes the glyph decorative; the unchanged locator
  now passes. This fixes accessibility rather than weakening the action selector.
- UI012-ERR-002: inherited light chat bubbles gave approximately 1.07:1 contrast
  with the requested light text. Screenshot inspection found the issue after
  functional tests passed. `ui012-contrast-red-corrected.txt` captures the failing
  contrast assertion. Explicit dark bubble fills/theme variables correct it;
  final desktop/mobile checks pass. The colors JSON retains computed values.
- UI012-ERR-003: fixed two-place formatting hid an observed 0.12345 rate. The
  precision regression failed (`ui012-rate-red.txt`). Only already two-place
  values receive padded formatting; finer observations remain intact. The same
  regression now passes (`ui012-presentation-green.txt`, final offline suite).
- UI012-ERR-004: an intermediate engineering edit used a default Windows codepage
  and corrupted Unicode characters. The browser's currency assertion detected
  the issue (`ui012-contrast-red.txt`, before contrast measurement was reached).
  Restoring UTF-8 corrected it; currency tests now pass. Subsequent file edits
  explicitly used UTF-8. No project-generated tool was read or modified.

The first restricted framework run timed out during initialization (five failures
over about 451 seconds). The unrestricted same-source checks passed, and the
final rerun passed all five in about 29 seconds. This is environment-specific
verification evidence, not an application defect repair or a relaxed timeout.
The offline view double also needed the approved Base-theme/HTML widget API;
its existing launch assertions remain, with CSS/favicon assertions added.

## Limits

These checks do not establish model quality, new native isolation guarantees,
installer correctness or all-input semantic correctness. The prior real-model
result is documented separately in USER_PROMPT_LIVE30B.md. No execution policy,
approval shortcut, sandbox fallback, Docker or installer work was introduced.
Inter must be installed on the viewing computer; fallback typography is explicit.
Bounded views may truncate very large output with a visible marker.

Local qwen3:14b drafted report prose only. Its summary was checked against raw
evidence; viewport sizes were clarified as pixels, and the contrast claim remains
limited to measured result text. The draft and reviewed provenance JSON are
retained. Engineering code and tests were not generated with the local model.
