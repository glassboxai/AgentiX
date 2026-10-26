# Verified baseline report

Historical pre-fix snapshot: the five defects described here have since been fixed by the explicitly approved REF-002 change. Current results are in `FIXES.md`; historical evidence and hashes are retained unchanged for comparison.

Date: 2026-10-19. Scope: approved phases 1–3 only. Production refactoring and installer implementation have not started.

## Results

The recorded pytest run collected **105 tests: 100 passed and 5 expected failures**. There were no unexpected failures or errors. Raw evidence is in `baseline-tests.xml` and `evidence.json`. A separate `--runxfail` execution produced five real failures (exit code 1), confirming that the defect reproducers fail against unchanged production; see `known-issues-red.txt`.

The five open defects are SEC-001/SEC-002 (sibling-prefix path escapes), SEC-003 (mutable pending-request exposure), SEC-004 (approved edited Python bypassing compilation) and UI-001 (shared execution history). They are not fixed. Strict xfails will make the suite fail on an unexpected pass, requiring explicit conversion to normal regression tests after approved fixes.

SHA-256 comparison confirms that `app.py`, `security_manager.py`, `custom_tools.py`, `main.py` and `config.py` match `production-baseline.json`. No application restart or generated-artifact migration was part of this work.

## Test scope

Unit tests exercise real storage, authorization, compilation, catalog, orchestration/controller and configuration functions with external initialization substituted. Filesystem fixtures are temporary. Component tests run real unittest subprocesses and dynamic execution of trusted fixture functions. Reporting-helper tests cover missing dependency metadata, local endpoint restrictions, redirect refusal, incomplete output and provenance.

No live Gradio browser, actual CrewAI decorator schemas, live agent/LLM answers, concurrent browser sessions, installer or OS-enforced sandbox is verified. No percentage coverage has been measured. Passing tests do not prove production stability or security. EXEC-001, AUTH-001, FLOW-001 and LOG-001 need subsequent design/investigation.

## Environment

Recorded interpreter: Python 3.11.9. Installed metadata: pytest 9.1.1, Gradio 6.30.0, CrewAI 1.15.28. `litellm` distribution metadata was unavailable; this does not alone establish a runtime failure. The Python platform string contains `Windows-10-10.0.26200-SP0`; that kernel-oriented string is not proof of the marketing edition of Windows. The agreed installer target remains Windows 11.

## Skills and governance

Six project-local skills are routed by `AGENTS.md`. Four are downloaded at pinned revisions with source licenses; two implement project-specific SDD/documentation rules. All six entrypoints pass the external skill validator using Python UTF-8 mode. `SKILLS/provenance.json` retains source revisions and file hashes. This is structural validation and content review, not a behavioral certification of third-party instructions. No global skill registration was performed.

## Local-model provenance and review

Ollama `qwen3:14b` drafted `ollama-baseline-draft.md` from `evidence.json` through the loopback-only report helper. The original model draft and `.provenance.json` are retained. No local model wrote code or tests.

Review corrections applied in this report: the model's description of a “stable production environment” was unsupported and is rejected; its Windows 10 edition inference from the platform string was removed; generic comments about test limitations were replaced with the exact boundaries above. The raw draft remains explicitly unverified and must not be used as the final assessment.

## Reproduction

From the project root:

```powershell
.\.autotool\Scripts\python.exe -m pytest --junitxml=docs/reports/baseline-tests.xml
.\.autotool\Scripts\python.exe tools\collect_evidence.py
.\.autotool\Scripts\python.exe -m pytest -m known_issue --runxfail
.\.autotool\Scripts\python.exe tools\draft_report.py --evidence docs/reports/evidence.json --output docs/reports/ollama-baseline-draft.md
```

The third command intentionally fails until production fixes are approved. The final command requires local Ollama and requests prose only; its output always needs review. The fresh-environment baseline suite requires only `requirements-dev.txt`, not the live runtime stack.

## Next approval boundary

Review `../specs/002-next-change-proposal.md` for the first proposed production block: path containment, defensive pending-request snapshots and validation of final approved Python content. Instance/session refactoring, execution isolation and installer implementation remain separate review blocks.
