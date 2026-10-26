# REUSE-001 implementation and verification

Date: 2026-10-25. Project: AgentiX v3. Live port 7873 was not restarted.

## Delivered behavior

Successful reviewed tools retain a bounded memory-only session grant. A new query prepares the unchanged tool without running unittest or requesting acceptance again, then must produce a fresh isolated execution receipt. Exact implementation/test bytes, owner, lifecycle and approved function coverage are checked. Sensitive or unclassified constructs require manual exact-call approval; existing sandbox permissions are unchanged. Another session, model runtime replacement or restart does not inherit grants. First-use tools without a grant retain the original tests/review flow.

## Engineering evidence

- `reuse-019-red.txt`: initial failing tests before production changes.
- `reuse-019-policy-red.txt`: typing introspection and direct second-call failures before correction.
- `reuse-019-browser-red.txt`: browser scenario initially failed before its dedicated fixture route was supplied.
- `reuse-019-offline-final.txt`: 448 passed, 28 deselected; 15 existing CrewAI deprecation warnings.
- `reuse-019-browser-focused.txt`: actual Playwright first review/12, then reuse/42; one review and one test run. Model choice and OS execution are trusted fixture doubles here.
- `reuse-019-native-lifecycle.txt`: updated native lifecycle passed, including reuse and subsequent drift/restoration rejection.
- The first combined opt-in run had 26 passes and one legacy lifecycle assertion expecting mandatory denial after changing operation_id. That assertion represented the intentionally replaced behavior, not a native isolation failure. The final run uses the approved reuse assertions and retains drift rejection.
- Final combined run: 27 passed and one native global-cleanup assertion failed while the separate live model workflow was actively creating AppContainer profiles. After closing only the owned disposable server, the complete native suite passed: 9 passed, 467 deselected in 49.70 seconds (`reuse-019-native-serial.txt`). Thus all 19 non-native opt-in scenarios and all 9 native scenarios have passing evidence, with the concurrency failure retained rather than hidden.

## Incidents and review interventions

REUSE-ERR-001: operation-bound authorization plus explicit manager instructions forced repeated testing/review. Separate successful session grants from query-bound result receipts and add REUSE_READY preparation.

REUSE-ERR-002: direct execution initially called is_verified before preparation, revoking an intact grant solely because operation_id changed. Prepare before checking and preserve unchanged grants during status polling. Direct second-call and polling regressions cover this.

REUSE-ERR-003: allowing arbitrary typing module calls admitted annotation evaluation to the unattended vocabulary. Exclude calls through typing; adversarial get_type_hints regression passes. Classification remains deliberately conservative, not a purity proof.

LIVE-REUSE-019: the initial model specification contradicted its own non-negative requirement. The engineer resolved negative/nonfinite/type behavior and rounding before approval. Generated implementation returned int for integer inputs below threshold despite promising float; the engineer made the return explicitly float. Generated tests used the wrong import and an incorrect rounding expectation; these were corrected and extended for exact return type, null/containers and the immediate upper boundary. Generated acceptance repeated a rounding error; the engineer corrected it and expanded five cases to twelve. These are supervised temporary artifacts, not modifications to project generated_tools. Initial creation is not claimed to be autonomous.

The first standalone browser navigation used networkidle, incompatible with ongoing Gradio polling; the disposable driver was retried using DOM content readiness. No application change or live-server restart was needed. The in-app browser execution tool was unavailable after discovery; standalone Playwright used a separate headless Edge instance.

## Residual limits

Finite reviewed cases do not prove all-input correctness or an honest arbitrary child implementation. Source review and native isolation remain necessary. Unknown harmless libraries may prompt. Permission does not enable blocked file/network operations. Trust is session-local and memory-only; observed drift is revoked, but an unobserved edit restored between checks is not a filesystem audit trail. No existing generated artifacts, real API keys, paid inference or v2 runtime were used.


## Completion record

The real GUI run used local ollama/qwen3-coder:30b, Playwright/headless Edge, native Windows isolation and fresh temporary storage outside the excluded project directory. The first English problem-only query described a shop's 10% discount at 100 euros and asked for 150 euros: host-observed final result **135.0**. The second asked for 80 euros under the same rules: the same calculate_discounted_price tool was selected and a fresh call returned **80.0**.

The initial creation had five explicit engineer approvals: directory, specification, implementation, Python tests and acceptance. Twelve host-compared acceptance cases passed. The second query had zero approval requests, zero unittest verification events, zero acceptance review events, zero artifact read/display operations and zero writes, with one reuse preparation and one successful execution/final observation. These counts are asserted in `reuse-019-live-evidence.json`; corresponding screenshots and raw stdout/stderr are preserved under `reuse-019-live-*`. The validation panel retained earlier accepted cases; they were not executed again for reuse.

No permission or file auto-approval switch was used for acceptance. The GUI's file auto-approval remained unchecked throughout the live run. Existing v2 and the user's v3 port 7873 were left running and unchanged; only the disposable 7874 process tree was stopped after evidence capture. The running 7873 process must be restarted separately to load this code.

NATIVE-TEST-019: the cleanup integration enumerates global Agentix profiles, so concurrent independently owned live evaluators can change its before/after set. The failure was preserved in the final combined log, not suppressed or weakened. Serial native execution after the owned live run stopped passed all nine checks, including the original cleanup assertion. Run global-resource cleanup checks separately from live agent evaluation.

The legacy live harness logs a safe model-profile-action error on its initial profile refresh because it intentionally composes the agent runtime without the optional model-configuration service. This did not prevent local inference, reviews or either execution; profile controls were outside this operational test and remain covered by dedicated browser/native credential integrations. It was not changed as part of reuse.

## Report provenance

Local qwen3:14b was called after the live qwen3-coder run, solely to draft prose from bounded verification facts. Its response stopped at an incomplete title (the generation budget was consumed without a usable report). The draft and provenance are retained; this final report was written and checked by the engineering agent against raw evidence. No model wrote engineering code or tests. The application's generated temporary tool is a separate, explicitly supervised runtime operation.
