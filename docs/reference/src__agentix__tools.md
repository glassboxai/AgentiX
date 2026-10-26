# Reference for src/agentix/tools.py

Framework-free artifact operations composed with execution/test services.

CrewAI registration lives in adapters; imports never initialize frameworks/models.
Generated unittest results are provisional; human-reviewed host comparisons alone
authorize function execution for exact artifact snapshots. Successful calls may
establish session grants and optional protected durable approvals; each result remains operation-bound.

Source fingerprint: bd0faac9f0647808ebd076965feffa8ea17d54b3362e90e29b368bdee4095fae

This reference is generated from maintained source without imports or execution. Assigned values are intentionally omitted. Runtime-dependent types are explicit; the enclosing docstring defines the behavioral contract. See [architecture](../ARCHITECTURE_QUALITY.md) for manually reviewed responsibility and dependency decisions.

## Classes and callables

### ArtifactTools

Application operations for specifications, code, incidents and reads.

Kind: class. Declared return: Not declared / class. Source line: 26.

### ArtifactTools.__init__

Compose owner-bound services, native execution and a shared evidence ledger.

Kind: callable. Declared return: None. Source line: 29.

### ArtifactTools.run_and_save_tests_tool

Save/run generated unittest as provisional evidence, never final authorization.

Kind: callable. Declared return: str. Source line: 46.

### ArtifactTools.verify_existing_tool_tool

Prepare an unchanged successful tool, or use first-use tests and review.

Kind: callable. Declared return: str. Source line: 52.

### ArtifactTools.submit_acceptance_cases_tool

Request mandatory human review and host-evaluate declarative acceptance cases.

Kind: callable. Declared return: str. Source line: 63.

### ArtifactTools.execute_generated_tool_tool

Execute verified current bytes only inside the native OS boundary.

Kind: callable. Declared return: str. Source line: 67.

### ArtifactTools.append_structured_incidence

Standardizes timestamped incidence logging across all agents.
Writes formatted markdown to: <toolName>/<toolName>_<suffix>.

Kind: callable. Declared return: str. Source line: 73.

### ArtifactTools.save_specifications_tool

Saves software specifications to <toolName>/<toolName>_specifications.md.

Kind: callable. Declared return: str. Source line: 97.

### ArtifactTools.log_specifications_incidence_tool

Appends a timestamped incidence to <toolName>/<toolName>_specifications_incidences.md.

Kind: callable. Declared return: str. Source line: 102.

### ArtifactTools.compile_and_save_code_tool

Validates Python syntax by compiling it in memory before saving.
If valid, saves to <toolName>/<toolName>_code.py.
If invalid, AUTOMATICALLY records a timestamped entry in <toolName>_code_incidences.md.

Kind: callable. Declared return: str. Source line: 111.

### ArtifactTools.log_coder_incidence_tool

Appends a timestamped manual incidence to <toolName>/<toolName>_code_incidences.md.

Kind: callable. Declared return: str. Source line: 153.

### ArtifactTools.log_tester_incidence_tool

Appends a timestamped manual incidence to <toolName>/<toolName>_tests_incidences.md.

Kind: callable. Declared return: str. Source line: 162.

### ArtifactTools.read_artifact_tool

Safely reads an existing specification, code, or test file from the tool directory.

Kind: callable. Declared return: str. Source line: 171.

## Variables and parameters

| Scope | Name | Role and meaning | Type | Lifetime | Writes |
| --- | --- | --- | --- | --- | --- |
| module | json | Imported dependency for json in module; use the enclosing contract and type below. | Module or imported public symbol | Module/process lifetime | 9 |
| module | logging | Imported dependency for logging in module; use the enclosing contract and type below. | Module or imported public symbol | Module/process lifetime | 10 |
| module | os | Imported dependency for os in module; use the enclosing contract and type below. | Module or imported public symbol | Module/process lifetime | 11 |
| module | datetime | Imported dependency for datetime in module; use the enclosing contract and type below. | Module or imported public symbol | Module/process lifetime | 12 |
| module | AcceptanceEvaluator | Imported dependency for AcceptanceEvaluator in module; use the enclosing contract and type below. | Module or imported public symbol | Module/process lifetime | 14 |
| module | ApprovalStore | Imported dependency for ApprovalStore in module; use the enclosing contract and type below. | Module or imported public symbol | Module/process lifetime | 15 |
| module | ExecutionBackend | Imported dependency for ExecutionBackend in module; use the enclosing contract and type below. | Module or imported public symbol | Module/process lifetime | 16 |
| module | SecurityBoundary | Imported dependency for SecurityBoundary in module; use the enclosing contract and type below. | Module or imported public symbol | Module/process lifetime | 16 |
| module | log_event | Imported dependency for log event in module; use the enclosing contract and type below. | Module or imported public symbol | Module/process lifetime | 17 |
| module | ToolExecutor | Imported dependency for ToolExecutor in module; use the enclosing contract and type below. | Module or imported public symbol | Module/process lifetime | 18 |
| module | WindowsSandbox | Imported dependency for WindowsSandbox in module; use the enclosing contract and type below. | Module or imported public symbol | Module/process lifetime | 19 |
| module | TestRunner | Imported dependency for TestRunner in module; use the enclosing contract and type below. | Module or imported public symbol | Module/process lifetime | 20 |
| module | VerificationLedger | Imported dependency for VerificationLedger in module; use the enclosing contract and type below. | Module or imported public symbol | Module/process lifetime | 21 |
| module | logger | Module logger emitting bounded operation diagnostics rather than artifact bodies. | Return type of getLogger; see its callable contract | Module/process lifetime | 23 |
| ArtifactTools.__init__ | self | Owning instance; its attributes retain state for the instance lifetime. | Not explicitly annotated | Enclosing invocation or class/instance lifetime | 30 |
| ArtifactTools.__init__ | security | Owner-scoped approval and path boundary injected into this service. | SecurityBoundary | Enclosing invocation or class/instance lifetime | 31 |
| ArtifactTools.__init__ | sandbox | Injected execution boundary; structural type alone cannot prove OS isolation. | ExecutionBackend &#124; None | Enclosing invocation or class/instance lifetime | 33 |
| ArtifactTools.__init__ | approval_store | Parameter for approval store in ArtifactTools.__init__; use the enclosing contract and type below. | ApprovalStore &#124; None | Enclosing invocation or class/instance lifetime | 34 |
| ArtifactTools.__init__ | self.security | Owner-scoped approval and path boundary injected into this service. | Runtime-dependent; see the enclosing callable contract | Enclosing invocation or class/instance lifetime | 37 |
| ArtifactTools.__init__ | self.verification | Content-bound ledger used to authorize only the current approved operation. | Return type of VerificationLedger; see its callable contract | Enclosing invocation or class/instance lifetime | 38 |
| ArtifactTools.__init__ | backend | Injected framework/execution provider; callers determine the required protocol. | Runtime-dependent; see the enclosing callable contract | Enclosing invocation or class/instance lifetime | 39 |
| ArtifactTools.__init__ | self.executor | Attribute for executor in ArtifactTools.__init__; use the enclosing contract and type below. | Return type of ToolExecutor; see its callable contract | Enclosing invocation or class/instance lifetime | 40 |
| ArtifactTools.__init__ | self.runner | Attribute for runner in ArtifactTools.__init__; use the enclosing contract and type below. | Return type of TestRunner; see its callable contract | Enclosing invocation or class/instance lifetime | 41 |
| ArtifactTools.__init__ | self.acceptance | Attribute for acceptance in ArtifactTools.__init__; use the enclosing contract and type below. | Return type of AcceptanceEvaluator; see its callable contract | Enclosing invocation or class/instance lifetime | 44 |
| ArtifactTools.run_and_save_tests_tool | self | Owning instance; its attributes retain state for the instance lifetime. | Not explicitly annotated | Enclosing invocation or class/instance lifetime | 46 |
| ArtifactTools.run_and_save_tests_tool | tool_name | Validated public tool identifier within the configured storage boundary. | str | Enclosing invocation or class/instance lifetime | 46 |
| ArtifactTools.run_and_save_tests_tool | test_code | Proposed unittest source requiring approval and isolated execution. | str | Enclosing invocation or class/instance lifetime | 46 |
| ArtifactTools.run_and_save_tests_tool | result | Intermediate or returned outcome; consult the callable contract for trust/validation. | Return type of run_and_save_tests_tool; see its callable contract | Enclosing invocation or class/instance lifetime | 48 |
| ArtifactTools.verify_existing_tool_tool | self | Owning instance; its attributes retain state for the instance lifetime. | Not explicitly annotated | Enclosing invocation or class/instance lifetime | 52 |
| ArtifactTools.verify_existing_tool_tool | tool_name | Validated public tool identifier within the configured storage boundary. | str | Enclosing invocation or class/instance lifetime | 52 |
| ArtifactTools.verify_existing_tool_tool | result | Intermediate or returned outcome; consult the callable contract for trust/validation. | Return type of verify_existing_tool; see its callable contract | Enclosing invocation or class/instance lifetime | 59 |
| ArtifactTools.submit_acceptance_cases_tool | self | Owning instance; its attributes retain state for the instance lifetime. | Not explicitly annotated | Enclosing invocation or class/instance lifetime | 63 |
| ArtifactTools.submit_acceptance_cases_tool | tool_name | Validated public tool identifier within the configured storage boundary. | str | Enclosing invocation or class/instance lifetime | 63 |
| ArtifactTools.submit_acceptance_cases_tool | cases_json | Parameter for cases json in ArtifactTools.submit_acceptance_cases_tool; use the enclosing contract and type below. | str | Enclosing invocation or class/instance lifetime | 63 |
| ArtifactTools.execute_generated_tool_tool | self | Owning instance; its attributes retain state for the instance lifetime. | Not explicitly annotated | Enclosing invocation or class/instance lifetime | 68 |
| ArtifactTools.execute_generated_tool_tool | tool_name | Validated public tool identifier within the configured storage boundary. | str | Enclosing invocation or class/instance lifetime | 68 |
| ArtifactTools.execute_generated_tool_tool | function_name | Public callable selected for the current operation; empty selects test mode. | str | Enclosing invocation or class/instance lifetime | 68 |
| ArtifactTools.execute_generated_tool_tool | kwargs_json | Untrusted JSON argument text to validate before execution. | str | Enclosing invocation or class/instance lifetime | 68 |
| ArtifactTools.append_structured_incidence | self | Owning instance; its attributes retain state for the instance lifetime. | Not explicitly annotated | Enclosing invocation or class/instance lifetime | 74 |
| ArtifactTools.append_structured_incidence | tool_name | Validated public tool identifier within the configured storage boundary. | str | Enclosing invocation or class/instance lifetime | 74 |
| ArtifactTools.append_structured_incidence | suffix | Parameter for suffix in ArtifactTools.append_structured_incidence; use the enclosing contract and type below. | str | Enclosing invocation or class/instance lifetime | 74 |
| ArtifactTools.append_structured_incidence | title | Parameter for title in ArtifactTools.append_structured_incidence; use the enclosing contract and type below. | str | Enclosing invocation or class/instance lifetime | 74 |
| ArtifactTools.append_structured_incidence | details | Parameter for details in ArtifactTools.append_structured_incidence; use the enclosing contract and type below. | str | Enclosing invocation or class/instance lifetime | 74 |
| ArtifactTools.append_structured_incidence | timestamp | Local binding for timestamp in ArtifactTools.append_structured_incidence; use the enclosing contract and type below. | Return type of strftime; see its callable contract | Enclosing invocation or class/instance lifetime | 80 |
| ArtifactTools.append_structured_incidence | filename | Local binding for filename in ArtifactTools.append_structured_incidence; use the enclosing contract and type below. | Runtime-dependent; see the enclosing callable contract | Enclosing invocation or class/instance lifetime | 81 |
| ArtifactTools.append_structured_incidence | clean_details | Local binding for clean details in ArtifactTools.append_structured_incidence; use the enclosing contract and type below. | Return type of strip; see its callable contract | Enclosing invocation or class/instance lifetime | 84 |
| ArtifactTools.append_structured_incidence | entry | Local binding for entry in ArtifactTools.append_structured_incidence; use the enclosing contract and type below. | Runtime-dependent; see the enclosing callable contract | Enclosing invocation or class/instance lifetime | 86 |
| ArtifactTools.save_specifications_tool | self | Owning instance; its attributes retain state for the instance lifetime. | Not explicitly annotated | Enclosing invocation or class/instance lifetime | 97 |
| ArtifactTools.save_specifications_tool | tool_name | Validated public tool identifier within the configured storage boundary. | str | Enclosing invocation or class/instance lifetime | 97 |
| ArtifactTools.save_specifications_tool | content | Artifact or review text whose encoding, size and approval state must be checked. | str | Enclosing invocation or class/instance lifetime | 97 |
| ArtifactTools.save_specifications_tool | filename | Local binding for filename in ArtifactTools.save_specifications_tool; use the enclosing contract and type below. | Runtime-dependent; see the enclosing callable contract | Enclosing invocation or class/instance lifetime | 99 |
| ArtifactTools.log_specifications_incidence_tool | self | Owning instance; its attributes retain state for the instance lifetime. | Not explicitly annotated | Enclosing invocation or class/instance lifetime | 102 |
| ArtifactTools.log_specifications_incidence_tool | tool_name | Validated public tool identifier within the configured storage boundary. | str | Enclosing invocation or class/instance lifetime | 102 |
| ArtifactTools.log_specifications_incidence_tool | incidence | Parameter for incidence in ArtifactTools.log_specifications_incidence_tool; use the enclosing contract and type below. | str | Enclosing invocation or class/instance lifetime | 102 |
| ArtifactTools.compile_and_save_code_tool | self | Owning instance; its attributes retain state for the instance lifetime. | Not explicitly annotated | Enclosing invocation or class/instance lifetime | 111 |
| ArtifactTools.compile_and_save_code_tool | tool_name | Validated public tool identifier within the configured storage boundary. | str | Enclosing invocation or class/instance lifetime | 111 |
| ArtifactTools.compile_and_save_code_tool | code | Source snapshot passed through approval, syntax checks and isolated staging. | str | Enclosing invocation or class/instance lifetime | 111 |
| ArtifactTools.compile_and_save_code_tool | filename | Local binding for filename in ArtifactTools.compile_and_save_code_tool; use the enclosing contract and type below. | Runtime-dependent; see the enclosing callable contract | Enclosing invocation or class/instance lifetime | 117 |
| ArtifactTools.compile_and_save_code_tool | clean_code | Local binding for clean code in ArtifactTools.compile_and_save_code_tool; use the enclosing contract and type below. | Return type of strip; see its callable contract | Enclosing invocation or class/instance lifetime | 120, 122, 124, 126 |
| ArtifactTools.compile_and_save_code_tool | e | Caught exception for e in ArtifactTools.compile_and_save_code_tool; use the enclosing contract and type below. | SyntaxError | Current exception handler; Python clears this binding afterward | 131 |
| ArtifactTools.compile_and_save_code_tool | error_msg | Local binding for error msg in ArtifactTools.compile_and_save_code_tool; use the enclosing contract and type below. | Runtime-dependent; see the enclosing callable contract | Enclosing invocation or class/instance lifetime | 132 |
| ArtifactTools.log_coder_incidence_tool | self | Owning instance; its attributes retain state for the instance lifetime. | Not explicitly annotated | Enclosing invocation or class/instance lifetime | 153 |
| ArtifactTools.log_coder_incidence_tool | tool_name | Validated public tool identifier within the configured storage boundary. | str | Enclosing invocation or class/instance lifetime | 153 |
| ArtifactTools.log_coder_incidence_tool | incidence | Parameter for incidence in ArtifactTools.log_coder_incidence_tool; use the enclosing contract and type below. | str | Enclosing invocation or class/instance lifetime | 153 |
| ArtifactTools.log_tester_incidence_tool | self | Owning instance; its attributes retain state for the instance lifetime. | Not explicitly annotated | Enclosing invocation or class/instance lifetime | 162 |
| ArtifactTools.log_tester_incidence_tool | tool_name | Validated public tool identifier within the configured storage boundary. | str | Enclosing invocation or class/instance lifetime | 162 |
| ArtifactTools.log_tester_incidence_tool | incidence | Parameter for incidence in ArtifactTools.log_tester_incidence_tool; use the enclosing contract and type below. | str | Enclosing invocation or class/instance lifetime | 162 |
| ArtifactTools.read_artifact_tool | self | Owning instance; its attributes retain state for the instance lifetime. | Not explicitly annotated | Enclosing invocation or class/instance lifetime | 171 |
| ArtifactTools.read_artifact_tool | tool_name | Validated public tool identifier within the configured storage boundary. | str | Enclosing invocation or class/instance lifetime | 171 |
| ArtifactTools.read_artifact_tool | filename | Parameter for filename in ArtifactTools.read_artifact_tool; use the enclosing contract and type below. | str | Enclosing invocation or class/instance lifetime | 171 |
| ArtifactTools.read_artifact_tool | target_path | Local binding for target path in ArtifactTools.read_artifact_tool; use the enclosing contract and type below. | Return type of validate_and_resolve_path; see its callable contract | Enclosing invocation or class/instance lifetime | 174 |
| ArtifactTools.read_artifact_tool | f | Managed resource for f in ArtifactTools.read_artifact_tool; use the enclosing contract and type below. | Return type of open; see its callable contract | Context-manager block; exit invokes its cleanup protocol | 178 |
| ArtifactTools.read_artifact_tool | content | Artifact or review text whose encoding, size and approval state must be checked. | Return type of read; see its callable contract | Enclosing invocation or class/instance lifetime | 179 |
| ArtifactTools.read_artifact_tool | e | Caught exception for e in ArtifactTools.read_artifact_tool; use the enclosing contract and type below. | Exception | Current exception handler; Python clears this binding afterward | 182 |
