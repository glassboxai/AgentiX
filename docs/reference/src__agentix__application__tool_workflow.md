# Reference for src/agentix/application/tool_workflow.py

Workflow orchestration with explicit factories, agents and catalog dependencies.

Creation decisions use a strict fail-closed contract. Task/context ordering is
preserved; only current test-service evidence permits the final execution stage.

Source fingerprint: eacb2ad54a4f7bdd1180a3fa474cf968694a7f883aba901b06b06c626e77738e

This reference is generated from maintained source without imports or execution. Assigned values are intentionally omitted. Runtime-dependent types are explicit; the enclosing docstring defines the behavioral contract. See [architecture](../ARCHITECTURE_QUALITY.md) for manually reviewed responsibility and dependency decisions.

## Classes and callables

### Orchestrator

Route queries and build tools without owning framework initialization.

Kind: class. Declared return: Not declared / class. Source line: 29.

### Orchestrator.__init__

Inject role objects, CrewAI factories and the read-only catalog callback.

Kind: callable. Declared return: None. Source line: 32.

### Orchestrator._saved_stage_text

Load fresh approved persisted bytes, never import or trust a model claim.

Receipts bind writes to the current owner/operation. Reads are bounded,
confined and hash checked; unchanged old receipts cannot advance a stage.

Kind: callable. Declared return: str. Source line: 57.

### Orchestrator._creation_stage

Run one model stage, then enforce its host-observed save postcondition.

No automatic model retry follows missing evidence or human denial. Model
errors propagate; artifact failures stop creation with payload-free logs.

Kind: callable. Declared return: tuple[str | None, str | None]. Source line: 84.

### Orchestrator.build_tool_pipeline

Create in gated stages using the original request and approved artifacts.

Each model task runs separately so a completion claim cannot launch the
next role before the host verifies a fresh approved save. Only maintained
ledger evidence and human acceptance can complete the final stage.

Kind: callable. Declared return: str. Source line: 115.

### Orchestrator.run_system

Run one bounded manager decision under correlated diagnostic context.

Kind: callable. Declared return: str. Source line: 228.

### Orchestrator._application_candidates

Read current approved suggestion metadata; failures yield no suggestion.

Kind: callable. Declared return: list[dict]. Source line: 255.

### Orchestrator._suggest_application

Recommend at most one approved application without executing it.

The decision carries no arguments and never reaches ``AppInvocation``, so a
Tools-tab query cannot run an installed application. Malformed, ambiguous
or unknown selections are logged and treated as no suggestion, which keeps
the normal creation route available without any execution fallback.

Kind: callable. Declared return: str | None. Source line: 271.

### Orchestrator._run_system

Main manager orchestrator: checks existing tools or builds a new one.

Kind: callable. Declared return: str. Source line: 322.

### Orchestrator._reuse_selected

Verify only the selected API, then execute through normal host permissions.

Kind: callable. Declared return: str. Source line: 440.

### Orchestrator._execution_answer

Render observed arguments/result, never certify unsupported model prose.

Kind: callable. Declared return: str. Source line: 469.

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
| module | DecisionValidationError | Imported dependency for DecisionValidationError in module; use the enclosing contract and type below. | Module or imported public symbol | Module/process lifetime | 14 |
| module | RunApplicationDecision | Imported dependency for RunApplicationDecision in module; use the enclosing contract and type below. | Module or imported public symbol | Module/process lifetime | 14 |
| module | parse_application_suggestion | Imported dependency for parse application suggestion in module; use the enclosing contract and type below. | Module or imported public symbol | Module/process lifetime | 14 |
| module | parse_manager_response | Imported dependency for parse manager response in module; use the enclosing contract and type below. | Module or imported public symbol | Module/process lifetime | 14 |
| module | log_event | Imported dependency for log event in module; use the enclosing contract and type below. | Module or imported public symbol | Module/process lifetime | 21 |
| module | operation_scope | Imported dependency for operation scope in module; use the enclosing contract and type below. | Module or imported public symbol | Module/process lifetime | 21 |
| module | VerificationLedger | Imported dependency for VerificationLedger in module; use the enclosing contract and type below. | Module or imported public symbol | Module/process lifetime | 22 |
| module | logger | Module logger emitting bounded operation diagnostics rather than artifact bodies. | Return type of getLogger; see its callable contract | Module/process lifetime | 24 |
| module | _WORK_CAPACITY | Module binding for WORK CAPACITY in module; use the enclosing contract and type below. | Return type of BoundedSemaphore; see its callable contract | Module/process lifetime | 26 |
| Orchestrator.__init__ | self | Owning instance; its attributes retain state for the instance lifetime. | Not explicitly annotated | Enclosing invocation or class/instance lifetime | 33 |
| Orchestrator.__init__ | agents | Parameter for agents in Orchestrator.__init__; use the enclosing contract and type below. | AgentSet | Enclosing invocation or class/instance lifetime | 34 |
| Orchestrator.__init__ | backend | Injected framework/execution provider; callers determine the required protocol. | Any | Enclosing invocation or class/instance lifetime | 35 |
| Orchestrator.__init__ | catalog | Parameter for catalog in Orchestrator.__init__; use the enclosing contract and type below. | Callable[[], str] | Enclosing invocation or class/instance lifetime | 36 |
| Orchestrator.__init__ | verification | Content-bound ledger used to authorize only the current approved operation. | VerificationLedger &#124; None | Enclosing invocation or class/instance lifetime | 37 |
| Orchestrator.__init__ | applications | Parameter for applications in Orchestrator.__init__; use the enclosing contract and type below. | Any | Enclosing invocation or class/instance lifetime | 38 |
| Orchestrator.__init__ | router | Parameter for router in Orchestrator.__init__; use the enclosing contract and type below. | Any | Enclosing invocation or class/instance lifetime | 39 |
| Orchestrator.__init__ | operations | Parameter for operations in Orchestrator.__init__; use the enclosing contract and type below. | Any | Enclosing invocation or class/instance lifetime | 40 |
| Orchestrator.__init__ | self.manager_agent | Attribute for manager agent in Orchestrator.__init__; use the enclosing contract and type below. | Runtime-dependent; see the enclosing callable contract | Enclosing invocation or class/instance lifetime | 43 |
| Orchestrator.__init__ | self.creation_manager_agent | Attribute for creation manager agent in Orchestrator.__init__; use the enclosing contract and type below. | Runtime-dependent; see the enclosing callable contract | Enclosing invocation or class/instance lifetime | 44 |
| Orchestrator.__init__ | self.application_selector_agent | Attribute for application selector agent in Orchestrator.__init__; use the enclosing contract and type below. | Runtime-dependent; see the enclosing callable contract | Enclosing invocation or class/instance lifetime | 45 |
| Orchestrator.__init__ | self.architect_agent | Attribute for architect agent in Orchestrator.__init__; use the enclosing contract and type below. | Runtime-dependent; see the enclosing callable contract | Enclosing invocation or class/instance lifetime | 48 |
| Orchestrator.__init__ | self.coder_agent | Attribute for coder agent in Orchestrator.__init__; use the enclosing contract and type below. | Runtime-dependent; see the enclosing callable contract | Enclosing invocation or class/instance lifetime | 49 |
| Orchestrator.__init__ | self.tester_agent | Attribute for tester agent in Orchestrator.__init__; use the enclosing contract and type below. | Runtime-dependent; see the enclosing callable contract | Enclosing invocation or class/instance lifetime | 50 |
| Orchestrator.__init__ | self.Task | Attribute for Task in Orchestrator.__init__; use the enclosing contract and type below. | tuple | Enclosing invocation or class/instance lifetime | 51 |
| Orchestrator.__init__ | self.Crew | Attribute for Crew in Orchestrator.__init__; use the enclosing contract and type below. | tuple | Enclosing invocation or class/instance lifetime | 51 |
| Orchestrator.__init__ | self.Process | Attribute for Process in Orchestrator.__init__; use the enclosing contract and type below. | tuple | Enclosing invocation or class/instance lifetime | 51 |
| Orchestrator.__init__ | self.get_installed_tools_catalog | Attribute for get installed tools catalog in Orchestrator.__init__; use the enclosing contract and type below. | Runtime-dependent; see the enclosing callable contract | Enclosing invocation or class/instance lifetime | 52 |
| Orchestrator.__init__ | self.verification | Content-bound ledger used to authorize only the current approved operation. | Runtime-dependent; see the enclosing callable contract | Enclosing invocation or class/instance lifetime | 53 |
| Orchestrator.__init__ | self.applications | Attribute for applications in Orchestrator.__init__; use the enclosing contract and type below. | Runtime-dependent; see the enclosing callable contract | Enclosing invocation or class/instance lifetime | 54 |
| Orchestrator.__init__ | self.router | Attribute for router in Orchestrator.__init__; use the enclosing contract and type below. | tuple | Enclosing invocation or class/instance lifetime | 55 |
| Orchestrator.__init__ | self.operations | Attribute for operations in Orchestrator.__init__; use the enclosing contract and type below. | tuple | Enclosing invocation or class/instance lifetime | 55 |
| Orchestrator._saved_stage_text | self | Owning instance; its attributes retain state for the instance lifetime. | Not explicitly annotated | Enclosing invocation or class/instance lifetime | 57 |
| Orchestrator._saved_stage_text | tool_name | Validated public tool identifier within the configured storage boundary. | str | Enclosing invocation or class/instance lifetime | 57 |
| Orchestrator._saved_stage_text | suffix | Parameter for suffix in Orchestrator._saved_stage_text; use the enclosing contract and type below. | str | Enclosing invocation or class/instance lifetime | 57 |
| Orchestrator._saved_stage_text | before | Parameter for before in Orchestrator._saved_stage_text; use the enclosing contract and type below. | Any | Enclosing invocation or class/instance lifetime | 57 |
| Orchestrator._saved_stage_text | hashlib | Imported dependency for hashlib in Orchestrator._saved_stage_text; use the enclosing contract and type below. | Module or imported public symbol | Enclosing invocation or class/instance lifetime | 63 |
| Orchestrator._saved_stage_text | Path | Imported dependency for Path in Orchestrator._saved_stage_text; use the enclosing contract and type below. | Module or imported public symbol | Enclosing invocation or class/instance lifetime | 64 |
| Orchestrator._saved_stage_text | security | Owner-scoped approval and path boundary injected into this service. | Runtime-dependent; see the enclosing callable contract | Enclosing invocation or class/instance lifetime | 66 |
| Orchestrator._saved_stage_text | path | Path under validation or an explicitly scoped maintained source path. | Return type of validate_and_resolve_path; see its callable contract | Enclosing invocation or class/instance lifetime | 67 |
| Orchestrator._saved_stage_text | receipt | Local binding for receipt in Orchestrator._saved_stage_text; use the enclosing contract and type below. | Return type of get_artifact_receipt; see its callable contract | Enclosing invocation or class/instance lifetime | 68 |
| Orchestrator._saved_stage_text | stream | Managed resource for stream in Orchestrator._saved_stage_text; use the enclosing contract and type below. | Return type of open; see its callable contract | Context-manager block; exit invokes its cleanup protocol | 71 |
| Orchestrator._saved_stage_text | data | Local binding for data in Orchestrator._saved_stage_text; use the enclosing contract and type below. | Return type of read; see its callable contract | Enclosing invocation or class/instance lifetime | 72 |
| Orchestrator._saved_stage_text | text | Local binding for text in Orchestrator._saved_stage_text; use the enclosing contract and type below. | Return type of decode; see its callable contract | Enclosing invocation or class/instance lifetime | 79 |
| Orchestrator._creation_stage | self | Owning instance; its attributes retain state for the instance lifetime. | Not explicitly annotated | Enclosing invocation or class/instance lifetime | 85 |
| Orchestrator._creation_stage | tool_name | Validated public tool identifier within the configured storage boundary. | str | Enclosing invocation or class/instance lifetime | 85 |
| Orchestrator._creation_stage | stage | Parameter for stage in Orchestrator._creation_stage; use the enclosing contract and type below. | str | Enclosing invocation or class/instance lifetime | 85 |
| Orchestrator._creation_stage | suffix | Parameter for suffix in Orchestrator._creation_stage; use the enclosing contract and type below. | str | Enclosing invocation or class/instance lifetime | 85 |
| Orchestrator._creation_stage | agent | Parameter for agent in Orchestrator._creation_stage; use the enclosing contract and type below. | Any | Enclosing invocation or class/instance lifetime | 85 |
| Orchestrator._creation_stage | description | Parameter for description in Orchestrator._creation_stage; use the enclosing contract and type below. | str | Enclosing invocation or class/instance lifetime | 85 |
| Orchestrator._creation_stage | security | Owner-scoped approval and path boundary injected into this service. | Runtime-dependent; see the enclosing callable contract | Enclosing invocation or class/instance lifetime | 92 |
| Orchestrator._creation_stage | path | Path under validation or an explicitly scoped maintained source path. | Return type of validate_and_resolve_path; see its callable contract | Enclosing invocation or class/instance lifetime | 93 |
| Orchestrator._creation_stage | before | Local binding for before in Orchestrator._creation_stage; use the enclosing contract and type below. | Return type of get_artifact_receipt; see its callable contract | Enclosing invocation or class/instance lifetime | 94 |
| Orchestrator._creation_stage | task | Local binding for task in Orchestrator._creation_stage; use the enclosing contract and type below. | Return type of Task; see its callable contract | Enclosing invocation or class/instance lifetime | 95 |
| Orchestrator._creation_stage | outcome | Local binding for outcome in Orchestrator._creation_stage; use the enclosing contract and type below. | Return type of kickoff; see its callable contract | Enclosing invocation or class/instance lifetime | 101 |
| Orchestrator._creation_stage | saved | Local binding for saved in Orchestrator._creation_stage; use the enclosing contract and type below. | Return type of _saved_stage_text; see its callable contract | Enclosing invocation or class/instance lifetime | 105 |
| Orchestrator._creation_stage | exc | Caught exception for exc in Orchestrator._creation_stage; use the enclosing contract and type below. | Exception | Current exception handler; Python clears this binding afterward | 106 |
| Orchestrator._creation_stage | detail | Local binding for detail in Orchestrator._creation_stage; use the enclosing contract and type below. | Runtime-dependent; see the enclosing callable contract | Enclosing invocation or class/instance lifetime | 108 |
| Orchestrator.build_tool_pipeline | self | Owning instance; its attributes retain state for the instance lifetime. | Not explicitly annotated | Enclosing invocation or class/instance lifetime | 115 |
| Orchestrator.build_tool_pipeline | tool_name | Validated public tool identifier within the configured storage boundary. | str | Enclosing invocation or class/instance lifetime | 115 |
| Orchestrator.build_tool_pipeline | user_requirement | Parameter for user requirement in Orchestrator.build_tool_pipeline; use the enclosing contract and type below. | str | Enclosing invocation or class/instance lifetime | 115 |
| Orchestrator.build_tool_pipeline | security | Owner-scoped approval and path boundary injected into this service. | Runtime-dependent; see the enclosing callable contract | Enclosing invocation or class/instance lifetime | 125 |
| Orchestrator.build_tool_pipeline | requirement | Local binding for requirement in Orchestrator.build_tool_pipeline; use the enclosing contract and type below. | Runtime-dependent; see the enclosing callable contract | Enclosing invocation or class/instance lifetime | 128 |
| Orchestrator.build_tool_pipeline | denial | Local binding for denial in Orchestrator.build_tool_pipeline; use the enclosing contract and type below. | str | Enclosing invocation or class/instance lifetime | 131 |
| Orchestrator.build_tool_pipeline | specification | Local binding for specification in Orchestrator.build_tool_pipeline; use the enclosing contract and type below. | Return type of _creation_stage; see its callable contract | Enclosing invocation or class/instance lifetime | 132 |
| Orchestrator.build_tool_pipeline | _ | Local binding for  in Orchestrator.build_tool_pipeline; use the enclosing contract and type below. | Return type of _creation_stage; see its callable contract | Enclosing invocation or class/instance lifetime | 132 |
| Orchestrator.build_tool_pipeline | code | Source snapshot passed through approval, syntax checks and isolated staging. | Return type of _creation_stage; see its callable contract | Enclosing invocation or class/instance lifetime | 151 |
| Orchestrator.build_tool_pipeline | code_rejection | Local binding for code rejection in Orchestrator.build_tool_pipeline; use the enclosing contract and type below. | Return type of _creation_stage; see its callable contract | Enclosing invocation or class/instance lifetime | 151 |
| Orchestrator.build_tool_pipeline | tests_path | Local binding for tests path in Orchestrator.build_tool_pipeline; use the enclosing contract and type below. | Return type of validate_and_resolve_path; see its callable contract | Enclosing invocation or class/instance lifetime | 177 |
| Orchestrator.build_tool_pipeline | before | Local binding for before in Orchestrator.build_tool_pipeline; use the enclosing contract and type below. | Return type of get_artifact_receipt; see its callable contract | Enclosing invocation or class/instance lifetime | 178 |
| Orchestrator.build_tool_pipeline | task | Local binding for task in Orchestrator.build_tool_pipeline; use the enclosing contract and type below. | Return type of Task; see its callable contract | Enclosing invocation or class/instance lifetime | 179 |
| Orchestrator.build_tool_pipeline | exc | Caught exception for exc in Orchestrator.build_tool_pipeline; use the enclosing contract and type below. | Exception | Current exception handler; Python clears this binding afterward | 210, 221 |
| Orchestrator.run_system | self | Owning instance; its attributes retain state for the instance lifetime. | Not explicitly annotated | Enclosing invocation or class/instance lifetime | 228 |
| Orchestrator.run_system | user_query | Original requirements retained across agent handoffs and final execution. | str | Enclosing invocation or class/instance lifetime | 228 |
| Orchestrator.run_system | operation_id | Identity of one user operation; new operations invalidate earlier evidence. | Return type of operation_scope; see its callable contract | Context-manager block; exit invokes its cleanup protocol | 238 |
| Orchestrator.run_system | self.verification.security.operation_id | Attribute for verification.security.operation id in Orchestrator.run_system; use the enclosing contract and type below. | Runtime-dependent; see the enclosing callable contract | Enclosing invocation or class/instance lifetime | 241 |
| Orchestrator.run_system | result | Intermediate or returned outcome; consult the callable contract for trust/validation. | Return type of _run_system; see its callable contract | Enclosing invocation or class/instance lifetime | 244 |
| Orchestrator.run_system | exc | Caught exception for exc in Orchestrator.run_system; use the enclosing contract and type below. | Exception | Current exception handler; Python clears this binding afterward | 245 |
| Orchestrator._application_candidates | self | Owning instance; its attributes retain state for the instance lifetime. | Not explicitly annotated | Enclosing invocation or class/instance lifetime | 255 |
| Orchestrator._application_candidates | reader | Local binding for reader in Orchestrator._application_candidates; use the enclosing contract and type below. | Return type of getattr; see its callable contract | Enclosing invocation or class/instance lifetime | 259 |
| Orchestrator._application_candidates | candidates | Local binding for candidates in Orchestrator._application_candidates; use the enclosing contract and type below. | Return type of reader; see its callable contract | Enclosing invocation or class/instance lifetime | 263 |
| Orchestrator._application_candidates | exc | Caught exception for exc in Orchestrator._application_candidates; use the enclosing contract and type below. | (OSError, ValueError) | Current exception handler; Python clears this binding afterward | 264 |
| Orchestrator._suggest_application | self | Owning instance; its attributes retain state for the instance lifetime. | Not explicitly annotated | Enclosing invocation or class/instance lifetime | 271 |
| Orchestrator._suggest_application | user_query | Original requirements retained across agent handoffs and final execution. | str | Enclosing invocation or class/instance lifetime | 271 |
| Orchestrator._suggest_application | candidates | Parameter for candidates in Orchestrator._suggest_application; use the enclosing contract and type below. | list[dict] | Enclosing invocation or class/instance lifetime | 271 |
| Orchestrator._suggest_application | task | Local binding for task in Orchestrator._suggest_application; use the enclosing contract and type below. | Return type of Task; see its callable contract | Enclosing invocation or class/instance lifetime | 281 |
| Orchestrator._suggest_application | response | Bounded response text to render or validate; it is not executable code. | Return type of kickoff; see its callable contract | Enclosing invocation or class/instance lifetime | 297 |
| Orchestrator._suggest_application | suggestion | Local binding for suggestion in Orchestrator._suggest_application; use the enclosing contract and type below. | Return type of parse_application_suggestion; see its callable contract | Enclosing invocation or class/instance lifetime | 304 |
| Orchestrator._suggest_application.comprehension_305 | candidate | Comprehension item for candidate in Orchestrator._suggest_application.comprehension_305; use the enclosing contract and type below. | Element of the declared iterable | This comprehension only; does not leak into its enclosing scope | 305 |
| Orchestrator._suggest_application | exc | Caught exception for exc in Orchestrator._suggest_application; use the enclosing contract and type below. | DecisionValidationError | Current exception handler; Python clears this binding afterward | 307 |
| Orchestrator._suggest_application | name | Current identifier selected by parsing, lookup or dependency registration. | Return type of next; see its callable contract | Enclosing invocation or class/instance lifetime | 313 |
| Orchestrator._suggest_application.comprehension_313 | candidate | Comprehension item for candidate in Orchestrator._suggest_application.comprehension_313; use the enclosing contract and type below. | Element of the declared iterable | This comprehension only; does not leak into its enclosing scope | 314 |
| Orchestrator._run_system | self | Owning instance; its attributes retain state for the instance lifetime. | Not explicitly annotated | Enclosing invocation or class/instance lifetime | 322 |
| Orchestrator._run_system | user_query | Original requirements retained across agent handoffs and final execution. | str | Enclosing invocation or class/instance lifetime | 322 |
| Orchestrator._run_system | existing_tools | Local binding for existing tools in Orchestrator._run_system; use the enclosing contract and type below. | Return type of get_installed_tools_catalog; see its callable contract | Enclosing invocation or class/instance lifetime | 327 |
| Orchestrator._run_system | selected | Local binding for selected in Orchestrator._run_system; use the enclosing contract and type below. | Return type of select; see its callable contract | Enclosing invocation or class/instance lifetime | 330 |
| Orchestrator._run_system | manager_decision | Local binding for manager decision in Orchestrator._run_system; use the enclosing contract and type below. | Return type of dumps; see its callable contract | Enclosing invocation or class/instance lifetime | 335, 382 |
| Orchestrator._run_system.comprehension_336 | key | Comprehension item for key in Orchestrator._run_system.comprehension_336; use the enclosing contract and type below. | Element of the declared iterable | This comprehension only; does not leak into its enclosing scope | 336 |
| Orchestrator._run_system | decision_agent | Local binding for decision agent in Orchestrator._run_system; use the enclosing contract and type below. | Runtime-dependent; see the enclosing callable contract | Enclosing invocation or class/instance lifetime | 339 |
| Orchestrator._run_system | manager_task | Local binding for manager task in Orchestrator._run_system; use the enclosing contract and type below. | Return type of Task; see its callable contract | Enclosing invocation or class/instance lifetime | 345 |
| Orchestrator._run_system | manager_crew | Local binding for manager crew in Orchestrator._run_system; use the enclosing contract and type below. | Return type of Crew; see its callable contract | Enclosing invocation or class/instance lifetime | 375 |
| Orchestrator._run_system | decision | Local binding for decision in Orchestrator._run_system; use the enclosing contract and type below. | Return type of parse_manager_response; see its callable contract | Enclosing invocation or class/instance lifetime | 384 |
| Orchestrator._run_system | suggestion | Local binding for suggestion in Orchestrator._run_system; use the enclosing contract and type below. | Return type of _suggest_application; see its callable contract | Enclosing invocation or class/instance lifetime | 389 |
| Orchestrator._run_system | tool_name | Validated public tool identifier within the configured storage boundary. | tuple | Enclosing invocation or class/instance lifetime | 392 |
| Orchestrator._run_system | purpose | Local binding for purpose in Orchestrator._run_system; use the enclosing contract and type below. | tuple | Enclosing invocation or class/instance lifetime | 392 |
| Orchestrator._run_system | pipeline | Local binding for pipeline in Orchestrator._run_system; use the enclosing contract and type below. | Return type of build_tool_pipeline; see its callable contract | Enclosing invocation or class/instance lifetime | 398 |
| Orchestrator._run_system | context | Local binding for context in Orchestrator._run_system; use the enclosing contract and type below. | Return type of acceptance_context; see its callable contract | Enclosing invocation or class/instance lifetime | 410 |
| Orchestrator._run_system | final_execution_task | Local binding for final execution task in Orchestrator._run_system; use the enclosing contract and type below. | Return type of Task; see its callable contract | Enclosing invocation or class/instance lifetime | 416 |
| Orchestrator._run_system | final_crew | Local binding for final crew in Orchestrator._run_system; use the enclosing contract and type below. | Return type of Crew; see its callable contract | Enclosing invocation or class/instance lifetime | 430 |
| Orchestrator._reuse_selected | self | Owning instance; its attributes retain state for the instance lifetime. | Not explicitly annotated | Enclosing invocation or class/instance lifetime | 440 |
| Orchestrator._reuse_selected | selected | Parameter for selected in Orchestrator._reuse_selected; use the enclosing contract and type below. | dict | Enclosing invocation or class/instance lifetime | 440 |
| Orchestrator._reuse_selected | Path | Imported dependency for Path in Orchestrator._reuse_selected; use the enclosing contract and type below. | Module or imported public symbol | Enclosing invocation or class/instance lifetime | 442 |
| Orchestrator._reuse_selected | name | Current identifier selected by parsing, lookup or dependency registration. | Runtime-dependent; see the enclosing callable contract | Enclosing invocation or class/instance lifetime | 444 |
| Orchestrator._reuse_selected | status | Local binding for status in Orchestrator._reuse_selected; use the enclosing contract and type below. | Return type of verify_existing_tool_tool; see its callable contract | Enclosing invocation or class/instance lifetime | 445, 458 |
| Orchestrator._reuse_selected | code | Source snapshot passed through approval, syntax checks and isolated staging. | Return type of snapshot; see its callable contract | Enclosing invocation or class/instance lifetime | 447 |
| Orchestrator._reuse_selected | _ | Local binding for  in Orchestrator._reuse_selected; use the enclosing contract and type below. | Return type of snapshot; see its callable contract | Enclosing invocation or class/instance lifetime | 447 |
| Orchestrator._reuse_selected | path | Path under validation or an explicitly scoped maintained source path. | Return type of Path; see its callable contract | Enclosing invocation or class/instance lifetime | 448 |
| Orchestrator._reuse_selected | stream | Managed resource for stream in Orchestrator._reuse_selected; use the enclosing contract and type below. | Return type of open; see its callable contract | Context-manager block; exit invokes its cleanup protocol | 453 |
| Orchestrator._reuse_selected | specification | Local binding for specification in Orchestrator._reuse_selected; use the enclosing contract and type below. | Return type of read; see its callable contract | Enclosing invocation or class/instance lifetime | 454 |
| Orchestrator._reuse_selected | proposal | Local binding for proposal in Orchestrator._reuse_selected; use the enclosing contract and type below. | Return type of acceptance; see its callable contract | Enclosing invocation or class/instance lifetime | 457 |
| Orchestrator._reuse_selected | outcome | Local binding for outcome in Orchestrator._reuse_selected; use the enclosing contract and type below. | Return type of execute_generated_tool_tool; see its callable contract | Enclosing invocation or class/instance lifetime | 462 |
| Orchestrator._execution_answer | self | Owning instance; its attributes retain state for the instance lifetime. | Not explicitly annotated | Enclosing invocation or class/instance lifetime | 469 |
| Orchestrator._execution_answer | result | Intermediate or returned outcome; consult the callable contract for trust/validation. | Return type of execution_result; see its callable contract | Enclosing invocation or class/instance lifetime | 471 |
