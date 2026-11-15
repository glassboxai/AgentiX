# Verification routing

Use the exact managed v5 interpreter, not another version's environment. Start from the changed requirement and test module; never read all reports or references as context.

| Check | When / evidence boundary |
| --- | --- |
| `python -m pytest` | Offline regression suite; OS/model doubles do not establish real isolation/inference. |
| `python -m pytest -m frameworks` | Actual CrewAI/Gradio schemas and callbacks; no model/server. |
| `python -m pytest -m windows_credentials` | Native vault with synthetic credentials only. |
| `python -m pytest -m windows_isolation` | Native AppContainer with maintained temporary fixtures; report skips/xfails. |
| Browser / Playwright | Disposable loopback server, independent expectations, real controls and completed callbacks; never restart the live GUI. |
| Model acceptance | Only qwen3-coder:30b; English problem-only query, explicit human source/test review, independent expected results, exact-byte grants. |
| `python tools/build_reference.py --check` | Read-only inventory/freshness; not semantic correctness. |
| Ruff check and format check | Maintained source/test/tool/infra roots and named entrypoints only; never generated_tools. |
| Infrastructure verifier | Use documented PowerShell checks; no Apply/install as a test side effect. |

Every defect needs a failing regression before correction, normal passing regression after a fix, and an incident ID. Known defects may use strict xfail with an ID; an unexpected pass requires review. See current specifications 037–039 and the [delivery report](../reports/V5_039_DELIVERY_REPORT.md). Historical requirement IDs are indexed in [HISTORY.md](../HISTORY.md). This cleanup changed no tests or verification code.


For V5-042 use tests/test_application_crews.py plus the affected pipeline, reuse,
backend and binding tests during development. Explicit frameworks validates real
CrewAI schemas and context in memory with inference replaced. Reserve actual
AppContainer/browser checks for closing the block and supervised generated-code
execution. Default doubles cannot establish isolation; there is no host fallback.


V5-043 focuses on tests/test_code_application.py and tests/test_application_crews.py,
plus existing package/review/invocation regression coverage. Run the authored
connection-code fixtures explicitly with windows_isolation, and the code-package
browser fixture with both browser and windows_isolation. No real model is needed
to establish this architecture; supervised model acceptance is separate evidence.

V7-076 focuses on tests/test_widget_style_member.py (identity exclusion, manifest
rebinding, grammar rejection, hard link, revocation split), tests/test_widget_style_editor.py
(defaults, merge preservation, derived border style, bounds, backend load/save) and
tests/test_widget_style_window.py with the browser marker. Offline suites
test_v5_widget_css, test_code_application, test_general_application_pipeline,
test_composite_application, test_application_catalog, test_widget_reuse,
test_installed_apps, test_applications_backend and test_v4_shell cover composition
and the unchanged revocation path. No model run is required.
