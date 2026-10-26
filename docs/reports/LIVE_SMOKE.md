# Live application, console and browser smoke checks

Date: 2026-10-19. Operational verification requested by the user. No application source changes, dependency installation or new standalone Playwright suite were made. All 34 application hashes still match `acceptance-evidence.json`.

## Application left running

The old application instance lacked the current validation panel. Only its confirmed Python processes were restarted. The current interface is available at `http://127.0.0.1:7860`, with a temporary process-level model override `OLLAMA_MODEL=ollama/qwen3:8b`. The source default remains `ollama/qwen3-coder:30b`.

The browser smoke check used the available browser automation's Playwright locators to fill the query, click Submit Query and verify the returned response. The test asked for a plain conversational acknowledgement and explicitly prohibited tool use, code execution and file creation/modification. The response `INTERFAZ OPERATIVA` was visibly returned. The validation panel was visible, Submit Query was enabled, and automatic file approval remained off. The catalogue was collapsed for the captured result. No generated-tool implementation was opened or executed by the test, and no file or acceptance approval was accepted. Normal application catalogue refresh remains runtime behavior.

The full Agentix workflow ran from 11:55:21 to 11:56:23, approximately 62 seconds. This is a successful bounded-scope smoke observation, not a satisfactory latency target. A separate direct Ollama health probe with `think=false` and `num_predict=16` returned `OK.` in 0.54 seconds; that number is not the Agentix round-trip duration or proof of the reason for its overhead.

Evidence: `live-smoke-evidence.json`, `agentix-live.png`, `app-live-8b.stdout.log` and `app-live-8b.stderr.log`. The browser tab containing the result was marked as a user deliverable.

## Resource incident and recovery

The first live query used the configured `qwen3-coder:30b`. The manager started, but no completion was observed before cancellation; both browser automation and one five-second HTTP health request timed out. The machine reported 16,697,356 KiB total visible RAM with only 866,120 KiB free. The resident model reported 10,685,975,100 bytes of VRAM allocation. A concurrent console startup also stalled. These observations support memory pressure as a contributor; they do not isolate every possible integration/performance cause.

Recovery cancelled only this test's Agentix and console processes, unloaded the 30B model loaded for the cancelled query, and started Agentix with the temporary 8B override. After unload, free RAM was 9,523,840 KiB; during the 8B query it was 6,743,416 KiB. HTTP health returned 200 and the live browser conversation completed. No other application processes were stopped, no model files removed, and no permanent model setting changed. The initial failed/cancelled attempts are not counted as passed.

The application still lacks model-memory admission checks, a user-visible model inference deadline and a cancellation control. No production fix for those issues is claimed. The current smaller-model workaround was verified with the completed browser query; implementing durable controls requires its own approved design and regression tests.

## Console status

`main.py` remains a lazy CLI/workflow entrypoint; `src/agentix/cli.py` retains the input loop and exit aliases. After recovery, the actual command-line entrypoint was launched and sent `q`; it displayed its banner/input prompt, exited cleanly and returned exit code 0. Evidence: `cli-live-smoke-retry.txt`. This proves startup/exit, not the complete tool-generation workflow.

The synchronous CLI has no dedicated human file/acceptance review client. Work requiring approval cannot bypass it and may wait until timeout. Keeping the console is practical because it already shares the same runtime, orchestration, isolation and acceptance services. A future terminal adapter should display pending context, accept approve/edit/reject decisions through the existing owner/request API, cancel on EOF/Ctrl+C and preserve mandatory manual acceptance. It should not duplicate business logic or auto-approve tests.

## Playwright and local models

The project virtual environment does not contain the standalone Python Playwright package. Browser smoke actions nevertheless used the browser tool's supported Playwright API, without modifying project dependencies. A committed reproducible browser suite is still pending.

Playwright controls the browser and does not require a language model. In the normal integration, Playwright submits a query to Agentix, Agentix calls local Ollama, and Playwright checks visible outcomes. A separate LLM browser agent could choose actions using DOM/screenshots and execute them through Playwright, but that extra adapter is neither required nor implemented here. Deterministic UI checks with controlled backend responses should remain separate from optional, slower live-Ollama checks. Future generation/acceptance E2E tests must use independent temporary storage, not existing project artifacts.

## Report provenance

A prose-only draft was requested from the already resident local `qwen3:8b` to avoid loading another large model. Raw evidence, original draft and provenance are retained. The reviewed report distinguishes startup/smoke success, cancelled attempts and unimplemented full E2E/CLI features.

Draft review rejected its unsupported claim that the 30B model was not fully unloaded: the unload API returned `done_reason=unload`. It also qualified the draft's causal claims: resource measurements support memory pressure as a contributor without proving every cause. The original draft is retained unmodified.
