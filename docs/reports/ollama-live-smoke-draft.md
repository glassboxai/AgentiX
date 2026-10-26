# Unverified local-model report draft

**Observations**  
- The application is accessible at `http://127.0.0.1:7860`.  
- The active process model override is set to `ollama/qwen3:8b`.  
- The persisted default model remains unchanged as `ollama/qwen3-coder:30b`.  
- Production source code has not been changed.  
- Production hashes have been checked for 34 files.  
- The browser smoke test indicates that Playwright controls are used, the response is visible, the validation panel is visible, and the submit button is enabled.  
- Automatic file approval is disabled.  
- The response from the browser is "INTERFAZ OPERATIVA".  
- Generation or tool execution was not requested.  
- Approvals were not accepted.  
- A screenshot named "agentix-live.png" was captured.  
- The scope of the browser test is limited to live input, Agentix manager, local Ollama, and visible response, excluding full tool creation/acceptance end-to-end testing.  
- The workflow started at 2026-10-19 11:55:21, finished at 2026-10-19 11:56:23.  
- The CLI entrypoint is `main.py`, and startup and Q exit were observed.  
- The CLI exit code is 0.  
- Evidence from the CLI is recorded in "cli-live-smoke-retry.txt".  
- The interactive approval client is not implemented; the core loop is retained, but approval-requiring work cannot bypass human review.  
- A resource incident occurred with the model `qwen3-coder:30b`.  
- System RAM is 16,697,356 KiB.  
- Observed free RAM is 866,120 KiB.  
- Resident model VRAM is 10,685,975,100 bytes.  
- Browser and HTTP timeouts were observed.  
- The first CLI attempt was cancelled during memory pressure and was not passed.  
- Mitigation steps included cancelling the own test, stopping only Agentix/test CLI processes, unloading the model loaded by the cancelled test, and restarting Agentix with a temporary `qwen3:8b` override.  
- Free RAM after unloading the model is 9,523,840 KiB.  
- Free RAM during the `qwen3:8b` query is 6,743,416 Ki.  
- A direct Ollama probe was performed with the model `qwen3:8b`.  
- The probe was completed successfully with a response of "OK".  
- The probe took 0.54 seconds.  
- The scope of the probe is limited to a direct bounded health check, not an Agentix round-trip duration.  
- Several features are not implemented, including dedicated terminal human-review dialogs, a committed standalone Playwright E2E suite, an LLM-driven browser agent, persistent model default changes, and model memory admission checks, model inference deadlines, and cancellation UI.  

**Unresolved Defects**  
- The interactive approval client is not implemented, and approval-requiring work cannot bypass human review.  
- The first CLI attempt was cancelled due to memory pressure and was not passed.  
- The model `qwen3-coder:30b` caused memory pressure, leading to the cancellation of the CLI attempt.  
- The browser and HTTP timeouts were observed during the resource incident.  
- The CLI evidence is recorded in "cli-live-smoke-retry.txt", but no further details are provided.  
- The model `qwen3-coder:30b` has a high resident VRAM usage, which may impact system performance.  
- The model `qwen3:8b` was used as a temporary override, but its performance and memory usage are not fully evaluated.  

**Limitations**  
- The browser smoke test scope is limited to live input, Agentix manager, local Ollama, and visible response, excluding full tool creation/acceptance end-to-end testing.  
- The CLI does not support interactive approval workflows, and approval-requiring work cannot bypass human review.  
- The model `qwen3-coder:30b` was not fully unloaded, and its impact on system resources is not fully understood.  
- The direct Ollama probe does not reflect the full Agentix round-trip duration.  
- Several features, including model memory admission checks, inference deadlines, and cancellation UI, are not implemented.  
- The CLI and browser smoke tests do not cover all aspects of the system, and further testing is required.
