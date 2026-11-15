# Reproducible browser regression tests

E2E-001 drives the real Gradio view with Python Playwright. It starts a separate loopback server on a temporary port and stores independently authored fixtures under the operating system temporary directory. It never connects to the live application at port 7860, reads project generated artifacts, or calls Ollama.

Prerequisites: Python 3.11+, the project's runtime Gradio dependencies, and an installed Microsoft Edge browser. Install optional test dependencies into the project virtual environment:

```powershell
.\.autotool\Scripts\python.exe -m pip install -r requirements-browser.txt
.\.autotool\Scripts\python.exe -m pytest -m browser tests/e2e
```

Edge is used headlessly with a fresh browser profile. To use installed Chrome, set `$env:AGENTIX_BROWSER_CHANNEL = 'chrome'`. To use the Playwright-managed Chromium binary, install it with `.\.autotool\Scripts\python.exe -m playwright install chromium` and set `$env:AGENTIX_BROWSER_CHANNEL = ''`. Browser versions and available channels are described in the [official Playwright documentation](https://playwright.dev/python/docs/browsers). This workflow does not install or replace a system browser automatically.

Optionally set `$env:AGENTIX_E2E_ARTIFACTS = 'D:\AI\Agentix_v2\docs\reports'` to save a full-page screenshot of the approved case and host verdict. Leave it unset to avoid writing persistent screenshots. Server logs remain in pytest's temporary directory for diagnostics. The fixture stops its own process tree on Windows, including virtual-environment launcher children. It does not stop unrelated application processes.

The three scenarios cover separate directory/file permissions and persisted edits, mandatory acceptance despite file auto-approval, edited expected values compared by the host, visible expected/observed data, rejection, and independent browser sessions. The workflow uses real storage, approval coordination, verification ledger, evaluator and Gradio callbacks. Only the LLM workflow and OS execution boundary are replaced by trusted test fixtures. Consequently, passing these tests establishes neither model quality nor native isolation. Separate opt-in framework and Windows isolation suites remain relevant. Default offline pytest excludes browser tests and does not import Playwright.

Playwright does not need an LLM to run these tests. Agentix may use local Ollama during normal operation. Connecting an LLM to browser decisions would require another orchestration layer and would make these deterministic regressions less reproducible; it is not implemented here.

## Supervised real-model validation

The deterministic suite above is not a substitute for LIVE-001. The user requested an actual tool-creation attempt with the reviewer operating the GUI as the human in the loop. To launch a separate real instance with native Windows isolation and temporary storage:

```powershell
.\.autotool\Scripts\python.exe tools/live_gui_review.py --port 7861 --model ollama/qwen3-coder:30b --manifest docs/reports/live-coder30b-manifest.json
```

Use an available loopback port and a separate manifest/log name for each run. Open that URL, submit the problem and review every directory, specification, code, unittest and acceptance request. This harness supplies no fake agent output and automates no approvals. Never run proposed code on the host: the application's native boundary remains mandatory. Generated content is retained in the OS temporary directory identified by the manifest, outside the project's excluded generated directory. Stop only the process started for that run when finished. Existing application processes must not be restarted or stopped by this workflow.

The user requires qwen3-coder:30b for Agentix. The launcher's default matches that requirement. Do not replace it with another model to obtain a faster test. Earlier alternate-model samples are historical observations; they do not validate the required production model. Engineering report drafting is a separate use of Ollama and may use a smaller model.

Review output against an independently established requirement and expected results; inspect tests for meaningful assertions, actual function invocation, boundaries, invalid inputs and forbidden side effects. Record manual edits explicitly. A returned answer, a model's completion claim or generated PASS report alone cannot pass this test. If creation fails before code or tests exist, report those review stages as not reached. Actual sampled outcomes and open defects are in `reports/LIVE_HITL.md`.
