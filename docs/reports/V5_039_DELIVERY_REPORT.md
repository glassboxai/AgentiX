# V5-039 delivery report — 30 October 2026

## What now works

AgentiX generated four tools through its real GUI using qwen3-coder:30b: a calculator, an English vowel counter, a whitespace word counter and a seeded random-number generator. Each was reviewed and approved. Fresh user requests selected the correct installed tool without another approval or another run of its old unit tests. New tool contracts require meaningful Annotated input/output descriptions and matching tool/function names.

The model also proposed a workflow and four Gradio widgets. A maintained compositor built the application around them. The installed **Four-tool workshop** runs all four tools; it is not a hardcoded word-counter demonstration. Approved widget code, tests and CSS are retained alongside their tool packages.

## Problems and solutions

Model output still needed human review. Some specifications contradicted their examples; proposed tests contained wrong expected counts or random sequences. Widget proposals also invented Gradio test APIs and mishandled callback references, empty results or table shape. Review corrected these problems, and failing proposals were not installed. This does not establish reliable autonomous test generation.

Real browser testing exposed defects in the checker itself: radio controls needed proper selection, an unchanged zero could be mistaken for a fresh result, and table selectors read hidden measurement cells. Regressions now require completed queue events and inspect the actual accessible virtual grid, including 100-row and empty tables. A separate save regression preserves unchanged approved CRLF tool bytes during widget-only edits.

The retained GUI-reviewed proposal was explicitly reapproved in a fresh maintained supervisor process after checker corrections. Normal native and browser verification gates ran again, without replaying the model or executing generated Python in the host. Thus generation and editing used the GUI; the final recovery verification was explicitly invoked through the maintained host service, not solely through the GUI.

Rapid Close/Play revealed a lifecycle polling race. A deterministic failing regression justified serializing polling under the owner's controller lock. The source correction and backend regressions pass. At the user's request, **7880 was not restarted**, so that last correction takes effect at the next authorized launch.

## Evidence and limits

- Final offline suite: **778 passed, 74 deselected**, with 18 recorded warnings. Ruff passes; 299 files pass format checks; documentary reference checks report no issues.
- Separate real-framework checks: **8 passed**. Windows credential checks: **4 passed**, using synthetic credentials.
- Fresh application verification: **12 native widget test methods**, independent data comparisons and **21 completed browser executions**, including two combined runs.
- Installed-app GUI checks independently verified 83.5 minus 19.25 equals 64.25, four words and eleven vowels in a new sentence, seeded repetition, zero/empty output clearing and rejection of fractional draw counts without rounding.
- Layout testing verified move/resize grips on all 18 controls and saved a nonbutton textbox's geometry to config.json. Post-reopen geometry was not separately asserted in this delivery.

These are bounded observations, not coverage percentages, a clean-Windows installation test or proof against arbitrary malicious code. Existing native transport limitations remain documented. No existing generated_tools content was inspected. No Docker, model downloads, extra libraries, paid calls or real API keys were used.

## Where to try it

Latest running GUI: **http://127.0.0.1:7880/**. In Applications, refresh the installed apps, select **Four-tool workshop**, load it and use Play if it is not already open. Port 7879 was preserved.

This instance deliberately uses an owned temporary validation profile rather than the user's default data. Its packages are under the application path recorded in `v5-039-restored-app-verification.json`; they must not be assumed to survive operating-system temporary-file cleanup. No user-data migration was performed.

Raw evidence is retained in `v5-039-final-offline.txt`, `v5-039-final-frameworks.txt`, `v5-039-final-credentials.txt`, `v5-039-restored-app-verification.json`, `v5-039-unseen-installed-gui.json`, `v5-039-live-layout.json` and the poll red/green records in this directory.

## Report provenance

Local qwen3:14b drafted prose only from reviewed evidence. Its draft and response metadata are retained as `v5-039-local-report-draft.*`. This final report was manually reconciled with raw results, correcting draft generalizations and adding the final counts and limitations. That report model wrote no engineering code or tests; application generation used qwen3-coder:30b.
