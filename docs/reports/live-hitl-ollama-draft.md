# Unverified local-model report draft

**Observations**  
The test run for requirement LIVE-001 was not passed. The real models were enabled, but the workflow doubles were not used. The native boundary was configured, but live runs never reached Python execution. File auto-approval was disabled. Reviewer interventions included correcting specifications through the GUI in the first and third attempts and rejecting proposed third-attempt tests for missing bool/integral-float/return-type checks and absence of an implementation file. The independent result showed an expected cost of 4250 cents for 250 kWh, but the observed tool result was null.  

Three attempts were made using different models: ollama/qwen3:8b, ollama/qwen2.5:7b, and ollama/qwen3:14b. The first attempt resulted in a pipeline not verified outcome after 362 seconds, with only specifications saved. The second attempt failed with an empty model response. The third attempt was rejected by the reviewer for incomplete tests, absence of implementation, and acceptance failure, with the own server stopping while the worker continued to run.  

The application source code remained unchanged, with the same SHA256 hashes for all files. The open deterministic defects include LIVE-FLOW-001, where the original user contract was lost at the creation boundary, and LIVE-UI-001, where a boolean was returned by a no-output approval callback.  

Regressions were noted in the offline, frameworks, and ruff categories, with some tests passing and others marked as strict xfail. The application source code was unchanged, and no code correctness, generated test execution, or final result was certified.  

**Unresolved Defects**  
- LIVE-FLOW-001: Original user contract lost at creation boundary.  
- LIVE-UI-001: Boolean returned by no-output approval callback.  

**Limitations**  
- Three sampled attempts are not a general model quality measurement.  
- No code correctness, generated test execution, or final result is certified.  
- The third attempt was stopped by the reviewer after rejection, not a natural completed workflow.
