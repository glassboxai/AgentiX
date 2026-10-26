# Unverified local-model report draft

**Observations**  
The report indicates that the test execution for CLI-001 and E2E-001 has completed with varying degrees of success. The offline test suite resulted in 263 passed tests, with 15 deselected. The frameworks test suite had 3 passed tests, with 271 deselected. The Windows isolation test suite had 9 passed tests, with 269 deselected. The browser test suite had 3 passed tests. The total number of distinct test cases is 278.  

The raw logs show that the CLI-browser-offline test run passed 263 tests in 12.15 seconds. The CLI-browser-frameworks test run passed 3 tests in 21.89 seconds. The CLI-browser-native test run passed 9 tests in 46.35 seconds. The CLI-browser-e2e test run passed 3 tests in 23.95 seconds. The CLI-browser-ruff test run formatted 65 files without errors.  

The application files have been hashed, with each file having a unique SHA256 checksum. The boundaries section outlines constraints such as the use of real Gradio with trusted workflow and OS doubles, the absence of Ollama model calls, and the deferred installer.  

The incidents section lists several issues, including terminal service failures, missing host verdict output, terminal control characters, and a missed file test in E2E-TEST-001.  

The report model selected is qwen3:8b to avoid local memory pressure from larger models, and the report is to be in prose only.  

**Unresolved Defects**  
- CLI-ERR-001: Terminal could not service pending review; coordinator-backed worker/main-input adapter added.  
- CLI-ERR-002: Host verdict output missing; independent validation status added.  
- CLI-ERR-003: Terminal control characters in review; escaped display preserving approved bytes.  
- E2E-TEST-001: File test missed directory approval; harness corrected, production rules unchanged.  

**Limitations**  
- The finite reviewed cases do not prove universal correctness.  
- The CLI interruption denies permissions but cannot forcibly cancel model I/O.  
- The installer remains deferred.  
- The test results do not provide coverage or fixes, nor do they guarantee security or successful installation.
