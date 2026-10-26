# Reference for src/agentix/orchestration.py

Workflow orchestration with explicit factories, agents and catalog dependencies.

Creation decisions use a strict fail-closed contract. Task/context ordering is
preserved; only current test-service evidence permits the final execution stage.

Source fingerprint: bcb7493033d9703125780a87e82a683d170b9e39ea37ed1d215fb89137c8caec

This reference is generated from maintained source without imports or execution. Assigned values are intentionally omitted. Runtime-dependent types are explicit; the enclosing docstring defines the behavioral contract. See [architecture](../ARCHITECTURE_QUALITY.md) for manually reviewed responsibility and dependency decisions.

## Classes and callables

### Orchestrator

Route queries and build tools without owning framework initialization.

Kind: class. Declared return: Not declared / class. Source line: 23.

### Orchestrator.__init__

Inject role objects, CrewAI factories and the read-only catalog callback.

Kind: callable. Declared return: None. Source line: 26.

### Orchestrator._saved_stage_text

Load fresh approved persisted bytes, never import or trust a model claim.

Receipts bind writes to the current owner/operation. Reads are bounded,
confined and hash checked; unchanged old receipts cannot advance a stage.

Kind: callable. Declared return: str. Source line: 43.

### Orchestrator._creation_stage

Run one model stage, then enforce its host-observed save postcondition.

No automatic model retry follows missing evidence or human denial. Model
errors propagate; artifact failures stop creation with payload-free logs.

Kind: callable. Declared return: str | None. Source line: 70.

### Orchestrator.build_tool_pipeline

Create in gated stages using the original request and approved artifacts.

Each model task runs separately so a completion claim cannot launch the
next role before the host verifies a fresh approved save. Only maintained
ledger evidence and human acceptance can complete the final stage.

Kind: callable. Declared return: str. Source line: 98.

### Orchestrator.run_system

Run one bounded manager decision under correlated diagnostic context.

Kind: callable. Declared return: str. Source line: 182.

### Orchestrator._run_system

Main manager orchestrator: checks existing tools or builds a new one.

Kind: callable. Declared return: str. Source line: 205.

### Orchestrator._execution_answer

Render observed arguments/result, never certify unsupported model prose.

Kind: callable. Declared return: str. Source line: 306.

## Variables and parameters

| Scope | Name | Role and meaning | Type | Lifetime | Writes |
| --- | --- | --- | --- | --- | --- |
| module | json | Imported dependency for json in module; use the enclosing contract and type below. | Module or imported public symbol | Module/process lifetime | 7 |
| module | logging | Imported dependency for logging in module; use the enclosing contract and type below. | Module or imported public symbol | Module/process lifetime | 8 |
| module | threading | Imported dependency for threading in module; use the enclosing contract and type below. | Module or imported public symbol | Module/process lifetime | 9 |
| module | Callable | Imported dependency for Callable in module; use the enclosing contract and type below. | Module or imported public symbol | Module/process lifetime | 10 |
| module | Any | Imported dependency for Any in module; use the enclosing contract and type below. | Module or imported public symbol | Module/process lifetime | 11 |
| module | AgentSet | Imported dependency for AgentSet in module; use the enclosing contract and type below. | Module or imported public symbol | Module/process lifetime | 13 |
| module | CreateToolDecision | Imported dependency for CreateToolDecision in module; use the enclosing contract and type below. | Module or imported public symbol | Module/process lifetime | 14 |
| module | parse_manager_response | Imported dependency for parse manager response in module; use the enclosing contract and type below. | Module or imported public symbol | Module/process lifetime | 14 |
| module | log_event | Imported dependency for log event in module; use the enclosing contract and type below. | Module or imported public symbol | Module/process lifetime | 15 |
| module | operation_scope | Imported dependency for operation scope in module; use the enclosing contract and type below. | Module or imported public symbol | Module/process lifetime | 15 |
| module | VerificationLedger | Imported dependency for VerificationLedger in module; use the enclosing contract and type below. | Module or imported public symbol | Module/process lifetime | 16 |
| module | logger | Module logger emitting bounded operation diagnostics rather than artifact bodies. | Return type of getLogger; see its callable contract | Module/process lifetime | 18 |
| module | _WORK_CAPACITY | Module binding for WORK CAPACITY in module; use the enclosing contract and type below. | Return type of BoundedSemaphore; see its callable contract | Module/process lifetime | 20 |
| Orchestrator.__init__ | self | Owning instance; its attributes retain state for the instance lifetime. | Not explicitly annotated | Enclosing invocation or class/instance lifetime | 27 |
| Orchestrator.__init__ | agents | Parameter for agents in Orchestrator.__init__; use the enclosing contract and type below. | AgentSet | Enclosing invocation or class/instance lifetime | 28 |
| Orchestrator.__init__ | backend | Injected framework/execution provider; callers determine the required protocol. | Any | Enclosing invocation or class/instance lifetime | 29 |
| Orchestrator.__init__ | catalog | Parameter for catalog in Orchestrator.__init__; use the enclosing contract and type below. | Callable[[], str] | Enclosing invocation or class/instance lifetime | 30 |
| Orchestrator.__init__ | verification | Content-bound ledger used to authorize only the current approved operation. | VerificationLedger &#124; None | Enclosing invocation or class/instance lifetime | 31 |
| Orchestrator.__init__ | self.manager_agent | Attribute for manager agent in Orchestrator.__init__; use the enclosing contract and type below. | Runtime-dependent; see the enclosing callable contract | Enclosing invocation or class/instance lifetime | 34 |
| Orchestrator.__init__ | self.creation_manager_agent | Attribute for creation manager agent in Orchestrator.__init__; use the enclosing contract and type below. | Runtime-dependent; see the enclosing callable contract | Enclosing invocation or class/instance lifetime | 35 |
| Orchestrator.__init__ | self.architect_agent | Attribute for architect agent in Orchestrator.__init__; use the enclosing contract and type below. | Runtime-dependent; see the enclosing callable contract | Enclosing invocation or class/instance lifetime | 36 |
| Orchestrator.__init__ | self.coder_agent | Attribute for coder agent in Orchestrator.__init__; use the enclosing contract and type below. | Runtime-dependent; see the enclosing callable contract | Enclosing invocation or class/instance lifetime | 37 |
| Orchestrator.__init__ | self.tester_agent | Attribute for tester agent in Orchestrator.__init__; use the enclosing contract and type below. | Runtime-dependent; see the enclosing callable contract | Enclosing invocation or class/instance lifetime | 38 |
| Orchestrator.__init__ | self.Task | Attribute for Task in Orchestrator.__init__; use the enclosing contract and type below. | tuple | Enclosing invocation or class/instance lifetime | 39 |
| Orchestrator.__init__ | self.Crew | Attribute for Crew in Orchestrator.__init__; use the enclosing contract and type below. | tuple | Enclosing invocation or class/instance lifetime | 39 |
| Orchestrator.__init__ | self.Process | Attribute for Process in Orchestrator.__init__; use the enclosing contract and type below. | tuple | Enclosing invocation or class/instance lifetime | 39 |
| Orchestrator.__init__ | self.get_installed_tools_catalog | Attribute for get installed tools catalog in Orchestrator.__init__; use the enclosing contract and type below. | Runtime-dependent; see the enclosing callable contract | Enclosing invocation or class/instance lifetime | 40 |
| Orchestrator.__init__ | self.verification | Content-bound ledger used to authorize only the current approved operation. | Runtime-dependent; see the enclosing callable contract | Enclosing invocation or class/instance lifetime | 41 |
| Orchestrator._saved_stage_text | self | Owning instance; its attributes retain state for the instance lifetime. | Not explicitly annotated | Enclosing invocation or class/instance lifetime | 43 |
| Orchestrator._saved_stage_text | tool_name | Validated public tool identifier within the configured storage boundary. | str | Enclosing invocation or class/instance lifetime | 43 |
| Orchestrator._saved_stage_text | suffix | Parameter for suffix in Orchestrator._saved_stage_text; use the enclosing contract and type below. | str | Enclosing invocation or class/instance lifetime | 43 |
| Orchestrator._saved_stage_text | before | Parameter for before in Orchestrator._saved_stage_text; use the enclosing contract and type below. | Any | Enclosing invocation or class/instance lifetime | 43 |
| Orchestrator._saved_stage_text | hashlib | Imported dependency for hashlib in Orchestrator._saved_stage_text; use the enclosing contract and type below. | Module or imported public symbol | Enclosing invocation or class/instance lifetime | 49 |
| Orchestrator._saved_stage_text | Path | Imported dependency for Path in Orchestrator._saved_stage_text; use the enclosing contract and type below. | Module or imported public symbol | Enclosing invocation or class/instance lifetime | 50 |
| Orchestrator._saved_stage_text | security | Owner-scoped approval and path boundary injected into this service. | Runtime-dependent; see the enclosing callable contract | Enclosing invocation or class/instance lifetime | 52 |
| Orchestrator._saved_stage_text | path | Path under validation or an explicitly scoped maintained source path. | Return type of validate_and_resolve_path; see its callable contract | Enclosing invocation or class/instance lifetime | 53 |
| Orchestrator._saved_stage_text | receipt | Local binding for receipt in Orchestrator._saved_stage_text; use the enclosing contract and type below. | Return type of get_artifact_receipt; see its callable contract | Enclosing invocation or class/instance lifetime | 54 |
| Orchestrator._saved_stage_text | stream | Managed resource for stream in Orchestrator._saved_stage_text; use the enclosing contract and type below. | Return type of open; see its callable contract | Context-manager block; exit invokes its cleanup protocol | 57 |
| Orchestrator._saved_stage_text | data | Local binding for data in Orchestrator._saved_stage_text; use the enclosing contract and type below. | Return type of read; see its callable contract | Enclosing invocation or class/instance lifetime | 58 |
| Orchestrator._saved_stage_text | text | Local binding for text in Orchestrator._saved_stage_text; use the enclosing contract and type below. | Return type of decode; see its callable contract | Enclosing invocation or class/instance lifetime | 65 |
| Orchestrator._creation_stage | self | Owning instance; its attributes retain state for the instance lifetime. | Not explicitly annotated | Enclosing invocation or class/instance lifetime | 71 |
| Orchestrator._creation_stage | tool_name | Validated public tool identifier within the configured storage boundary. | str | Enclosing invocation or class/instance lifetime | 71 |
| Orchestrator._creation_stage | stage | Parameter for stage in Orchestrator._creation_stage; use the enclosing contract and type below. | str | Enclosing invocation or class/instance lifetime | 71 |
| Orchestrator._creation_stage | suffix | Parameter for suffix in Orchestrator._creation_stage; use the enclosing contract and type below. | str | Enclosing invocation or class/instance lifetime | 71 |
| Orchestrator._creation_stage | agent | Parameter for agent in Orchestrator._creation_stage; use the enclosing contract and type below. | Any | Enclosing invocation or class/instance lifetime | 71 |
| Orchestrator._creation_stage | description | Parameter for description in Orchestrator._creation_stage; use the enclosing contract and type below. | str | Enclosing invocation or class/instance lifetime | 71 |
| Orchestrator._creation_stage | security | Owner-scoped approval and path boundary injected into this service. | Runtime-dependent; see the enclosing callable contract | Enclosing invocation or class/instance lifetime | 78 |
| Orchestrator._creation_stage | path | Path under validation or an explicitly scoped maintained source path. | Return type of validate_and_resolve_path; see its callable contract | Enclosing invocation or class/instance lifetime | 79 |
| Orchestrator._creation_stage | before | Local binding for before in Orchestrator._creation_stage; use the enclosing contract and type below. | Return type of get_artifact_receipt; see its callable contract | Enclosing invocation or class/instance lifetime | 80 |
| Orchestrator._creation_stage | task | Local binding for task in Orchestrator._creation_stage; use the enclosing contract and type below. | Return type of Task; see its callable contract | Enclosing invocation or class/instance lifetime | 81 |
| Orchestrator._creation_stage | saved | Local binding for saved in Orchestrator._creation_stage; use the enclosing contract and type below. | Return type of _saved_stage_text; see its callable contract | Enclosing invocation or class/instance lifetime | 91 |
| Orchestrator._creation_stage | exc | Caught exception for exc in Orchestrator._creation_stage; use the enclosing contract and type below. | Exception | Current exception handler; Python clears this binding afterward | 92 |
| Orchestrator.build_tool_pipeline | self | Owning instance; its attributes retain state for the instance lifetime. | Not explicitly annotated | Enclosing invocation or class/instance lifetime | 98 |
| Orchestrator.build_tool_pipeline | tool_name | Validated public tool identifier within the configured storage boundary. | str | Enclosing invocation or class/instance lifetime | 98 |
| Orchestrator.build_tool_pipeline | user_requirement | Parameter for user requirement in Orchestrator.build_tool_pipeline; use the enclosing contract and type below. | str | Enclosing invocation or class/instance lifetime | 98 |
| Orchestrator.build_tool_pipeline | requirement | Local binding for requirement in Orchestrator.build_tool_pipeline; use the enclosing contract and type below. | Runtime-dependent; see the enclosing callable contract | Enclosing invocation or class/instance lifetime | 109 |
| Orchestrator.build_tool_pipeline | denial | Local binding for denial in Orchestrator.build_tool_pipeline; use the enclosing contract and type below. | str | Enclosing invocation or class/instance lifetime | 112 |
| Orchestrator.build_tool_pipeline | specification | Local binding for specification in Orchestrator.build_tool_pipeline; use the enclosing contract and type below. | Return type of _creation_stage; see its callable contract | Enclosing invocation or class/instance lifetime | 113 |
| Orchestrator.build_tool_pipeline | code | Source snapshot passed through approval, syntax checks and isolated staging. | Return type of _creation_stage; see its callable contract | Enclosing invocation or class/instance lifetime | 127 |
| Orchestrator.build_tool_pipeline | security | Owner-scoped approval and path boundary injected into this service. | Runtime-dependent; see the enclosing callable contract | Enclosing invocation or class/instance lifetime | 141 |
| Orchestrator.build_tool_pipeline | tests_path | Local binding for tests path in Orchestrator.build_tool_pipeline; use the enclosing contract and type below. | Return type of validate_and_resolve_path; see its callable contract | Enclosing invocation or class/instance lifetime | 142 |
| Orchestrator.build_tool_pipeline | before | Local binding for before in Orchestrator.build_tool_pipeline; use the enclosing contract and type below. | Return type of get_artifact_receipt; see its callable contract | Enclosing invocation or class/instance lifetime | 143 |
| Orchestrator.build_tool_pipeline | task | Local binding for task in Orchestrator.build_tool_pipeline; use the enclosing contract and type below. | Return type of Task; see its callable contract | Enclosing invocation or class/instance lifetime | 144 |
| Orchestrator.build_tool_pipeline | exc | Caught exception for exc in Orchestrator.build_tool_pipeline; use the enclosing contract and type below. | Exception | Current exception handler; Python clears this binding afterward | 172 |
| Orchestrator.run_system | self | Owning instance; its attributes retain state for the instance lifetime. | Not explicitly annotated | Enclosing invocation or class/instance lifetime | 182 |
| Orchestrator.run_system | user_query | Original requirements retained across agent handoffs and final execution. | str | Enclosing invocation or class/instance lifetime | 182 |
| Orchestrator.run_system | operation_id | Identity of one user operation; new operations invalidate earlier evidence. | Return type of operation_scope; see its callable contract | Context-manager block; exit invokes its cleanup protocol | 191 |
| Orchestrator.run_system | self.verification.security.operation_id | Attribute for verification.security.operation id in Orchestrator.run_system; use the enclosing contract and type below. | Runtime-dependent; see the enclosing callable contract | Enclosing invocation or class/instance lifetime | 193 |
| Orchestrator.run_system | result | Intermediate or returned outcome; consult the callable contract for trust/validation. | Return type of _run_system; see its callable contract | Enclosing invocation or class/instance lifetime | 196 |
| Orchestrator.run_system | exc | Caught exception for exc in Orchestrator.run_system; use the enclosing contract and type below. | Exception | Current exception handler; Python clears this binding afterward | 197 |
| Orchestrator._run_system | self | Owning instance; its attributes retain state for the instance lifetime. | Not explicitly annotated | Enclosing invocation or class/instance lifetime | 205 |
| Orchestrator._run_system | user_query | Original requirements retained across agent handoffs and final execution. | str | Enclosing invocation or class/instance lifetime | 205 |
| Orchestrator._run_system | existing_tools | Local binding for existing tools in Orchestrator._run_system; use the enclosing contract and type below. | Return type of get_installed_tools_catalog; see its callable contract | Enclosing invocation or class/instance lifetime | 210 |
| Orchestrator._run_system | decision_agent | Local binding for decision agent in Orchestrator._run_system; use the enclosing contract and type below. | Runtime-dependent; see the enclosing callable contract | Enclosing invocation or class/instance lifetime | 211 |
| Orchestrator._run_system | manager_task | Local binding for manager task in Orchestrator._run_system; use the enclosing contract and type below. | Return type of Task; see its callable contract | Enclosing invocation or class/instance lifetime | 217 |
| Orchestrator._run_system | manager_crew | Local binding for manager crew in Orchestrator._run_system; use the enclosing contract and type below. | Return type of Crew; see its callable contract | Enclosing invocation or class/instance lifetime | 247 |
| Orchestrator._run_system | manager_decision | Local binding for manager decision in Orchestrator._run_system; use the enclosing contract and type below. | Return type of str; see its callable contract | Enclosing invocation or class/instance lifetime | 254 |
| Orchestrator._run_system | decision | Local binding for decision in Orchestrator._run_system; use the enclosing contract and type below. | Return type of parse_manager_response; see its callable contract | Enclosing invocation or class/instance lifetime | 256 |
| Orchestrator._run_system | tool_name | Validated public tool identifier within the configured storage boundary. | tuple | Enclosing invocation or class/instance lifetime | 258 |
| Orchestrator._run_system | purpose | Local binding for purpose in Orchestrator._run_system; use the enclosing contract and type below. | tuple | Enclosing invocation or class/instance lifetime | 258 |
| Orchestrator._run_system | pipeline | Local binding for pipeline in Orchestrator._run_system; use the enclosing contract and type below. | Return type of build_tool_pipeline; see its callable contract | Enclosing invocation or class/instance lifetime | 264 |
| Orchestrator._run_system | context | Local binding for context in Orchestrator._run_system; use the enclosing contract and type below. | Return type of acceptance_context; see its callable contract | Enclosing invocation or class/instance lifetime | 276 |
| Orchestrator._run_system | final_execution_task | Local binding for final execution task in Orchestrator._run_system; use the enclosing contract and type below. | Return type of Task; see its callable contract | Enclosing invocation or class/instance lifetime | 282 |
| Orchestrator._run_system | final_crew | Local binding for final crew in Orchestrator._run_system; use the enclosing contract and type below. | Return type of Crew; see its callable contract | Enclosing invocation or class/instance lifetime | 296 |
| Orchestrator._execution_answer | self | Owning instance; its attributes retain state for the instance lifetime. | Not explicitly annotated | Enclosing invocation or class/instance lifetime | 306 |
| Orchestrator._execution_answer | result | Intermediate or returned outcome; consult the callable contract for trust/validation. | Return type of execution_result; see its callable contract | Enclosing invocation or class/instance lifetime | 308 |
