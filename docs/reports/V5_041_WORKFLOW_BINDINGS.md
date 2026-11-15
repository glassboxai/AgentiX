# V5-041 workflow binding verification

Date: 30 October 2026. Incident: V5-ERR-041-01.
Scope: [approved general contract](../specs/041-general-workflow-bindings.md).

Implemented shared inputs, typed constants, explicit array selection and bounded
coherent independent-case selection without tool-specific production rules.
Exact legacy template SHA-256 baselines are preserved:

- app.py: `396e68258f69df9bc8500eabe6ebceb05c128aae25ad192cf69dc1bbb08431f8`
- operation.py: `a2605827259bc4184d0de8b2d25a7f6c760deb8b722f309e94574e6f5ab6f0ab`

These match the pre-change maintained reference fingerprints. New runtime source
fingerprints are recorded separately in the synchronized module reference pages;
no historical package or baseline digest is replaced. New package grants include
the binding-runtime version and resolver bytes.

Verification results:

| Check | Observed result |
| --- | --- |
| Complete default offline suite | 798 passed, 77 deselected; 18 existing CrewAI deprecation warnings |
| Focused offline binding/acceptance regressions | 20 passed, 3 opt-in tests deselected |
| Explicit frameworks suite | 9 passed; one Gradio row_count deprecation warning |
| Final focused Gradio callback | 1 passed; shared canonical input, derived values and failure clearing |
| Explicit headless native fixture | 1 passed; five independently expected node results |
| Native disposable Chrome browser | 1 passed; one standalone widget, four managed widgets, two complete runs and four fresh queue events |
| Ruff lint / format | passed; 310 maintained Python files formatted |
| Reference inventory/freshness | passed; no stale or missing entries |

The browser initially could not find Playwright-managed Chromium. It used the
already installed Chrome executable through AGENTIX_PLAYWRIGHT_EXECUTABLE; no
browser installation or download occurred. A subsequent real table comparison
exposed V5-ERR-041-02 (3.0 displayed as 3); the corrected comparator preserves
numeric expectations and rejects prefixes/suffixes and unequal values. Focused
red/green evidence and the final native-browser pass cover that correction.

An initial full offline run had 795 passes and only a stale-reference failure;
the final synchronized full run has 798 passes. During manual reference review,
explicit local type annotations clarified dictionary/control collection entries;
these documentation-only declarations were checked with 39 focused regression/reference
tests and a final two-test Gradio/native-browser run against the definitive bytes.
No unrelated expensive checks were repeated.

All evidence uses the v5 IaC-managed interpreter, independently authored temporary
fixtures and injected model proposals.
No existing generated artifacts are read. Native and browser checks are reported
separately from doubles and in-memory framework checks.

Limits: no qwen3-coder:30b inference or actual current-session creation was run.
No live application was restarted. The running 7880 process retains its earlier
code, including the previously deferred V5-ERR-039-21 reload. Finite cases and typed
bindings do not prove arbitrary request semantics; exact-byte human review and
host-held expected values remain required. Legacy packages retain their reviewed
behavior; the new binding contract is used by newly generated proposals.

Provenance: concise engineering record written and manually reviewed against raw
test output. No model drafting was used for this routine change record.


The final native/browser fixture package digest and separate legacy/new runtime
source hashes are retained in [the verification receipt](V5_041_VERIFICATION.json).
The digest was recomputed from the successful temporary package and validated
against the current maintained runtime bytes. Historical baseline hashes above
remain unchanged. Only final meaningful JSON evidence is retained in the project;
interim screenshots and diagnostic transcripts are not copied into documentation.
