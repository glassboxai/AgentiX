# V5-039: catalog-driven applications and clear tool contracts

Status: approved on 2026-10-29.

Replace the production words/vowels-only assembly with catalog-driven contracts.
Preserve the legacy pilot only for explicit compatibility fixtures, not as the
production fallback. Use qwen3-coder:30b for live creation and widget proposals.
Never supply reference widget source in the model prompt.

GEN-01: create four tools through real GUI operations: calculator, vowels, words,
and seeded bounded random numbers. Review all proposed specifications/source/tests
and declarative acceptance. Authoritative public function equals tool identity;
parameters and return use typing.Annotated with meaningful English metadata.
GEN-02: discover portable approved catalog contracts without executing source;
plan only listed approved tools, validate names, types, unknown connections and
cycles before execution. Generate each widget once, then reuse approved bytes.
GEN-03: build one reviewed native application using all four tools; host-observed
independent GUI expectations include exact arithmetic/counts, bounded random
samples and deterministic seeded repetition. Reload/reuse without regeneration.
GEN-04: dark slim scrollbars throughout maintained GUI; preserve readable focus.
Presentation removes only decorative leading/trailing pipe borders from verbose
activity, keeping internal operators/text and the unmodified captured diagnostic.
GEN-05: reject missing Annotated, missing descriptions, ambiguous public entries
and name mismatch for newly generated production tools, including human edits.
Existing approved legacy artifacts are not silently renamed or rewritten.

No host execution fallback, added external privileges, extra dependencies, downloads
or migration of existing generated artifacts. Tests use temporary authored fixtures;
real model/browser evidence is reported separately from doubles. v4 and the live v5
instance are not restarted by automated tests.

GEN-06 (live defect correction): separate semantic tool selection from callable verification/execution. The selector has no tools, returns a structured creation/reuse decision and exact named arguments, and is checked against catalog types before any selected operation. A mismatched calculator must not be reviewed as a way to count text. Rejection stops that operation; explicit new test operations are recorded separately.


## Verification record — 30 October 2026
GEN-01 through GEN-06 are implemented. Real GUI/model generation, reviewed corrections,
reuse checks and fresh native/browser acceptance are detailed in
../reports/V5_039_DELIVERY_REPORT.md. The final offline suite has 778 passing tests;
framework and Windows credential checks are recorded separately. This is finite
four-tool evidence, not autonomous correctness for every catalog or model output.
The approved polling race correction remains source-only in the live 7880 instance
because the user expressly requested no restart.
