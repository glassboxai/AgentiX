# Reference for tests/test_application_crews.py

V5-042: CrewAI coordinates creation; native execution and review stay separate.

Source fingerprint: eb85dcd6329448901032f5f7455d9adf93fdfba8e90c3caace9fa69acdf8416f

This reference is generated from maintained source without imports or execution. Assigned values are intentionally omitted. Runtime-dependent types are explicit; the enclosing docstring defines the behavioral contract. See [architecture](../ARCHITECTURE_QUALITY.md) for manually reviewed responsibility and dependency decisions.

## Classes and callables

### approved_tool

Return independently authored tool metadata without importing its code.

Kind: callable. Declared return: ApprovedTool. Source line: 15.

### plan

Declare ordinary readable IDs and external ports without catalog prefixes.

Kind: callable. Declared return: dict. Source line: 35.

### steps_plan

Translate authored fixture labels into the new ordered-call task envelope.

Kind: callable. Declared return: dict. Source line: 54.

### code_plan

Return an authored code envelope; inventory has no input/output connections.

Kind: callable. Declared return: dict. Source line: 69.

### backend

Record actual coordination contracts with inert framework/model doubles.

Kind: callable. Declared return: SimpleNamespace. Source line: 82.

### backend.agent

Retain explicit role and verbose/resource options.

Kind: callable. Declared return: SimpleNamespace. Source line: 86.

### backend.task

Retain task dependencies and structured output schema.

Kind: callable. Declared return: SimpleNamespace. Source line: 92.

### backend.llm

Record pinned local model construction without inference.

Kind: callable. Declared return: object. Source line: 96.

### backend.Crew

Populate structured fixture outputs without executing model-produced Python.

Kind: class. Declared return: Not declared / class. Source line: 101.

### backend.Crew.__init__

Record the sequential crew definition.

Kind: callable. Declared return: None. Source line: 104.

### backend.Crew.kickoff

Complete the authored tasks in their declared order.

Kind: callable. Declared return: None. Source line: 109.

### test_crews_use_sequential_context_and_only_pending_widgets

Planning precedes integration; reused widgets require no additional crew.

Kind: callable. Declared return: None. Source line: 133.

### test_plan_prompt_closes_the_public_input_schema_keys

V7-059: the host prompt forbids numeric bounds instead of relying on the user.

Kind: callable. Declared return: None. Source line: 162.

### test_coordinator_uses_an_injected_session_llm_without_rebuilding_it

The application coordinator must preserve the active session model client.

Kind: callable. Declared return: None. Source line: 182.

### test_invalid_final_plan_stops_before_widgets_or_approval

Crew output remains data; unavailable tools fail host validation.

Kind: callable. Declared return: None. Source line: 193.

### test_pipeline_injects_coordinator_without_legacy_http_client

A real package can be assembled with CrewAI coordination and no host code import.

Kind: callable. Declared return: None. Source line: 208.

### test_real_crewai_task_context_and_pydantic_outputs_without_inference

Construct actual CrewAI agents/tasks/crews; only kickoff uses authored outputs.

Kind: callable. Declared return: None. Source line: 227.

### test_real_crewai_task_context_and_pydantic_outputs_without_inference.kickoff

Substitute inference only while keeping real framework schemas and context.

Kind: callable. Declared return: None. Source line: 238.

### test_failed_crew_releases_capacity_without_retry

One failed kickoff must not retry or prevent the next explicit operation.

Kind: callable. Declared return: None. Source line: 269.

### test_failed_crew_releases_capacity_without_retry.fail

Expose one controlled framework failure.

Kind: callable. Declared return: None. Source line: 277.

### test_missing_structured_output_cannot_reach_approval

A successful framework return alone cannot establish a valid application plan.

Kind: callable. Declared return: None. Source line: 294.

### test_application_verbose_and_events_belong_to_the_owning_session

Application crews must not send verbose output or events to another session.

Kind: callable. Declared return: None. Source line: 306.

### test_application_verbose_and_events_belong_to_the_owning_session.controller

Create only the controller contracts needed by generation.

Kind: callable. Declared return: SimpleNamespace. Source line: 317.

### test_application_verbose_and_events_belong_to_the_owning_session.Pipeline

Expose verbose and technical output without model/storage execution.

Kind: class. Declared return: Not declared / class. Source line: 337.

### test_application_verbose_and_events_belong_to_the_owning_session.Pipeline.__init__

Retain the injected root without touching it.

Kind: callable. Declared return: None. Source line: 340.

### test_application_verbose_and_events_belong_to_the_owning_session.Pipeline.generate

Emit both streams under the caller's ownership scope.

Kind: callable. Declared return: SimpleNamespace. Source line: 344.

## Variables and parameters

| Scope | Name | Role and meaning | Type | Lifetime | Writes |
| --- | --- | --- | --- | --- | --- |
| module | json | Imported dependency for json in module; use the enclosing contract and type below. | Module or imported public symbol | Module/process lifetime | 3 |
| module | Path | Imported dependency for Path in module; use the enclosing contract and type below. | Module or imported public symbol | Module/process lifetime | 4 |
| module | SimpleNamespace | Imported dependency for SimpleNamespace in module; use the enclosing contract and type below. | Module or imported public symbol | Module/process lifetime | 5 |
| module | pytest | Imported dependency for pytest in module; use the enclosing contract and type below. | Module or imported public symbol | Module/process lifetime | 7 |
| module | WIDGET | Imported dependency for WIDGET in module; use the enclosing contract and type below. | Module or imported public symbol | Module/process lifetime | 8 |
| module | CODE | Imported dependency for CODE in module; use the enclosing contract and type below. | Module or imported public symbol | Module/process lifetime | 9 |
| module | extract_tool_schema | Imported dependency for extract tool schema in module; use the enclosing contract and type below. | Module or imported public symbol | Module/process lifetime | 11 |
| module | ApprovedTool | Imported dependency for ApprovedTool in module; use the enclosing contract and type below. | Module or imported public symbol | Module/process lifetime | 12 |
| approved_tool | schema | Local binding for schema in approved_tool; use the enclosing contract and type below. | Return type of extract_tool_schema; see its callable contract | Enclosing invocation or class/instance lifetime | 17 |
| approved_tool | case | Local binding for case in approved_tool; use the enclosing contract and type below. | dict | Enclosing invocation or class/instance lifetime | 18 |
| steps_plan | proposal | Parameter for proposal in steps_plan; use the enclosing contract and type below. | dict &#124; None | Enclosing invocation or class/instance lifetime | 54 |
| steps_plan | value | Value at the current validation/rendering boundary; apply the enclosing contract. | Runtime-dependent; see the enclosing callable contract | Enclosing invocation or class/instance lifetime | 56 |
| steps_plan | steps | Local binding for steps in steps_plan; use the enclosing contract and type below. | list | Enclosing invocation or class/instance lifetime | 57 |
| steps_plan | node | Loop item for node in steps_plan; use the enclosing contract and type below. | Element of the declared iterable | Enclosing invocation or class/instance lifetime | 58 |
| steps_plan | arguments | Local binding for arguments in steps_plan; use the enclosing contract and type below. | dict | Enclosing invocation or class/instance lifetime | 59 |
| steps_plan | parameter | Loop item for parameter in steps_plan; use the enclosing contract and type below. | Element of the declared iterable | Enclosing invocation or class/instance lifetime | 60 |
| steps_plan | binding | Loop item for binding in steps_plan; use the enclosing contract and type below. | Element of the declared iterable | Enclosing invocation or class/instance lifetime | 60 |
| code_plan | proposal | Parameter for proposal in code_plan; use the enclosing contract and type below. | dict &#124; None | Enclosing invocation or class/instance lifetime | 69 |
| code_plan | value | Value at the current validation/rendering boundary; apply the enclosing contract. | Runtime-dependent; see the enclosing callable contract | Enclosing invocation or class/instance lifetime | 71 |
| code_plan.comprehension_74 | node | Comprehension item for node in code_plan.comprehension_74; use the enclosing contract and type below. | Element of the declared iterable | This comprehension only; does not leak into its enclosing scope | 75 |
| backend | proposal | Parameter for proposal in backend; use the enclosing contract and type below. | dict &#124; None | Enclosing invocation or class/instance lifetime | 82 |
| backend | crews | Local binding for crews in backend; use the enclosing contract and type below. | tuple | Enclosing invocation or class/instance lifetime | 84 |
| backend | agents | Local binding for agents in backend; use the enclosing contract and type below. | tuple | Enclosing invocation or class/instance lifetime | 84 |
| backend | models | Local binding for models in backend; use the enclosing contract and type below. | tuple | Enclosing invocation or class/instance lifetime | 84 |
| backend.agent | options | Parameter for options in backend.agent; use the enclosing contract and type below. | object | Enclosing invocation or class/instance lifetime | 86 |
| backend.agent | value | Value at the current validation/rendering boundary; apply the enclosing contract. | Return type of SimpleNamespace; see its callable contract | Enclosing invocation or class/instance lifetime | 88 |
| backend.task | options | Parameter for options in backend.task; use the enclosing contract and type below. | object | Enclosing invocation or class/instance lifetime | 92 |
| backend.llm | options | Parameter for options in backend.llm; use the enclosing contract and type below. | object | Enclosing invocation or class/instance lifetime | 96 |
| backend.Crew.__init__ | self | Owning instance; its attributes retain state for the instance lifetime. | Not explicitly annotated | Enclosing invocation or class/instance lifetime | 104 |
| backend.Crew.__init__ | options | Parameter for options in backend.Crew.__init__; use the enclosing contract and type below. | object | Enclosing invocation or class/instance lifetime | 104 |
| backend.Crew.kickoff | self | Owning instance; its attributes retain state for the instance lifetime. | Not explicitly annotated | Enclosing invocation or class/instance lifetime | 109 |
| backend.Crew.kickoff | item | Loop item for item in backend.Crew.kickoff; use the enclosing contract and type below. | Element of the declared iterable | Enclosing invocation or class/instance lifetime | 111 |
| backend.Crew.kickoff | value | Value at the current validation/rendering boundary; apply the enclosing contract. | Runtime-dependent; see the enclosing callable contract | Enclosing invocation or class/instance lifetime | 112 |
| backend.Crew.kickoff | item.output | Attribute for item.output in backend.Crew.kickoff; use the enclosing contract and type below. | Return type of SimpleNamespace; see its callable contract | Enclosing invocation or class/instance lifetime | 117 |
| test_crews_use_sequential_context_and_only_pending_widgets | tmp_path | Parameter for tmp path in test_crews_use_sequential_context_and_only_pending_widgets; use the enclosing contract and type below. | Path | Enclosing invocation or class/instance lifetime | 133 |
| test_crews_use_sequential_context_and_only_pending_widgets | make_application_coordinator | Imported dependency for make application coordinator in test_crews_use_sequential_context_and_only_pending_widgets; use the enclosing contract and type below. | Module or imported public symbol | Enclosing invocation or class/instance lifetime | 135 |
| test_crews_use_sequential_context_and_only_pending_widgets | framework | Local binding for framework in test_crews_use_sequential_context_and_only_pending_widgets; use the enclosing contract and type below. | Return type of backend; see its callable contract | Enclosing invocation or class/instance lifetime | 137 |
| test_crews_use_sequential_context_and_only_pending_widgets | coordinator | Local binding for coordinator in test_crews_use_sequential_context_and_only_pending_widgets; use the enclosing contract and type below. | Return type of make_application_coordinator; see its callable contract | Enclosing invocation or class/instance lifetime | 138 |
| test_crews_use_sequential_context_and_only_pending_widgets | tool | Local binding for tool in test_crews_use_sequential_context_and_only_pending_widgets; use the enclosing contract and type below. | Return type of approved_tool; see its callable contract | Enclosing invocation or class/instance lifetime | 139 |
| test_crews_use_sequential_context_and_only_pending_widgets | first | Local binding for first in test_crews_use_sequential_context_and_only_pending_widgets; use the enclosing contract and type below. | Runtime-dependent; see the enclosing callable contract | Enclosing invocation or class/instance lifetime | 148 |
| test_crews_use_sequential_context_and_only_pending_widgets | second | Local binding for second in test_crews_use_sequential_context_and_only_pending_widgets; use the enclosing contract and type below. | Runtime-dependent; see the enclosing callable contract | Enclosing invocation or class/instance lifetime | 148 |
| test_crews_use_sequential_context_and_only_pending_widgets.comprehension_153 | crew | Comprehension item for crew in test_crews_use_sequential_context_and_only_pending_widgets.comprehension_153; use the enclosing contract and type below. | Element of the declared iterable | This comprehension only; does not leak into its enclosing scope | 153 |
| test_crews_use_sequential_context_and_only_pending_widgets.comprehension_154 | agent | Comprehension item for agent in test_crews_use_sequential_context_and_only_pending_widgets.comprehension_154; use the enclosing contract and type below. | Element of the declared iterable | This comprehension only; does not leak into its enclosing scope | 155 |
| test_plan_prompt_closes_the_public_input_schema_keys | tmp_path | Parameter for tmp path in test_plan_prompt_closes_the_public_input_schema_keys; use the enclosing contract and type below. | Path | Enclosing invocation or class/instance lifetime | 162 |
| test_plan_prompt_closes_the_public_input_schema_keys | make_application_coordinator | Imported dependency for make application coordinator in test_plan_prompt_closes_the_public_input_schema_keys; use the enclosing contract and type below. | Module or imported public symbol | Enclosing invocation or class/instance lifetime | 164 |
| test_plan_prompt_closes_the_public_input_schema_keys | framework | Local binding for framework in test_plan_prompt_closes_the_public_input_schema_keys; use the enclosing contract and type below. | Return type of backend; see its callable contract | Enclosing invocation or class/instance lifetime | 166 |
| test_plan_prompt_closes_the_public_input_schema_keys | coordinator | Local binding for coordinator in test_plan_prompt_closes_the_public_input_schema_keys; use the enclosing contract and type below. | Return type of make_application_coordinator; see its callable contract | Enclosing invocation or class/instance lifetime | 167 |
| test_plan_prompt_closes_the_public_input_schema_keys | request | Local binding for request in test_plan_prompt_closes_the_public_input_schema_keys; use the enclosing contract and type below. | Return type of loads; see its callable contract | Enclosing invocation or class/instance lifetime | 171 |
| test_plan_prompt_closes_the_public_input_schema_keys | system | Local binding for system in test_plan_prompt_closes_the_public_input_schema_keys; use the enclosing contract and type below. | Runtime-dependent; see the enclosing callable contract | Enclosing invocation or class/instance lifetime | 172 |
| test_plan_prompt_closes_the_public_input_schema_keys | keyword | Loop item for keyword in test_plan_prompt_closes_the_public_input_schema_keys; use the enclosing contract and type below. | Element of the declared iterable | Enclosing invocation or class/instance lifetime | 174 |
| test_plan_prompt_closes_the_public_input_schema_keys | review | Local binding for review in test_plan_prompt_closes_the_public_input_schema_keys; use the enclosing contract and type below. | Return type of loads; see its callable contract | Enclosing invocation or class/instance lifetime | 177 |
| test_coordinator_uses_an_injected_session_llm_without_rebuilding_it | tmp_path | Parameter for tmp path in test_coordinator_uses_an_injected_session_llm_without_rebuilding_it; use the enclosing contract and type below. | Path | Enclosing invocation or class/instance lifetime | 182 |
| test_coordinator_uses_an_injected_session_llm_without_rebuilding_it | make_application_coordinator | Imported dependency for make application coordinator in test_coordinator_uses_an_injected_session_llm_without_rebuilding_it; use the enclosing contract and type below. | Module or imported public symbol | Enclosing invocation or class/instance lifetime | 184 |
| test_coordinator_uses_an_injected_session_llm_without_rebuilding_it | framework | Local binding for framework in test_coordinator_uses_an_injected_session_llm_without_rebuilding_it; use the enclosing contract and type below. | Return type of backend; see its callable contract | Enclosing invocation or class/instance lifetime | 186 |
| test_coordinator_uses_an_injected_session_llm_without_rebuilding_it | client | Local binding for client in test_coordinator_uses_an_injected_session_llm_without_rebuilding_it; use the enclosing contract and type below. | Return type of object; see its callable contract | Enclosing invocation or class/instance lifetime | 187 |
| test_coordinator_uses_an_injected_session_llm_without_rebuilding_it | coordinator | Local binding for coordinator in test_coordinator_uses_an_injected_session_llm_without_rebuilding_it; use the enclosing contract and type below. | Return type of make_application_coordinator; see its callable contract | Enclosing invocation or class/instance lifetime | 188 |
| test_invalid_final_plan_stops_before_widgets_or_approval | tmp_path | Parameter for tmp path in test_invalid_final_plan_stops_before_widgets_or_approval; use the enclosing contract and type below. | Path | Enclosing invocation or class/instance lifetime | 193 |
| test_invalid_final_plan_stops_before_widgets_or_approval | make_application_coordinator | Imported dependency for make application coordinator in test_invalid_final_plan_stops_before_widgets_or_approval; use the enclosing contract and type below. | Module or imported public symbol | Enclosing invocation or class/instance lifetime | 195 |
| test_invalid_final_plan_stops_before_widgets_or_approval | invalid | Local binding for invalid in test_invalid_final_plan_stops_before_widgets_or_approval; use the enclosing contract and type below. | Return type of plan; see its callable contract | Enclosing invocation or class/instance lifetime | 197 |
| test_invalid_final_plan_stops_before_widgets_or_approval | framework | Local binding for framework in test_invalid_final_plan_stops_before_widgets_or_approval; use the enclosing contract and type below. | Return type of backend; see its callable contract | Enclosing invocation or class/instance lifetime | 199 |
| test_invalid_final_plan_stops_before_widgets_or_approval | coordinator | Local binding for coordinator in test_invalid_final_plan_stops_before_widgets_or_approval; use the enclosing contract and type below. | Return type of make_application_coordinator; see its callable contract | Enclosing invocation or class/instance lifetime | 200 |
| test_pipeline_injects_coordinator_without_legacy_http_client | tmp_path | Parameter for tmp path in test_pipeline_injects_coordinator_without_legacy_http_client; use the enclosing contract and type below. | Path | Enclosing invocation or class/instance lifetime | 208 |
| test_pipeline_injects_coordinator_without_legacy_http_client | make_application_coordinator | Imported dependency for make application coordinator in test_pipeline_injects_coordinator_without_legacy_http_client; use the enclosing contract and type below. | Module or imported public symbol | Enclosing invocation or class/instance lifetime | 210 |
| test_pipeline_injects_coordinator_without_legacy_http_client | ApplicationPipeline | Imported dependency for ApplicationPipeline in test_pipeline_injects_coordinator_without_legacy_http_client; use the enclosing contract and type below. | Module or imported public symbol | Enclosing invocation or class/instance lifetime | 211 |
| test_pipeline_injects_coordinator_without_legacy_http_client | framework | Local binding for framework in test_pipeline_injects_coordinator_without_legacy_http_client; use the enclosing contract and type below. | Return type of backend; see its callable contract | Enclosing invocation or class/instance lifetime | 213 |
| test_pipeline_injects_coordinator_without_legacy_http_client | item | Local binding for item in test_pipeline_injects_coordinator_without_legacy_http_client; use the enclosing contract and type below. | Return type of generate; see its callable contract | Enclosing invocation or class/instance lifetime | 214 |
| test_pipeline_injects_coordinator_without_legacy_http_client.lambda_216 | evidence | Callback parameter for evidence in test_pipeline_injects_coordinator_without_legacy_http_client.lambda_216; use the enclosing contract and type below. | Defined by the enclosing callback contract | Enclosing invocation or class/instance lifetime | 216 |
| test_real_crewai_task_context_and_pydantic_outputs_without_inference | tmp_path | Parameter for tmp path in test_real_crewai_task_context_and_pydantic_outputs_without_inference; use the enclosing contract and type below. | Path | Enclosing invocation or class/instance lifetime | 228 |
| test_real_crewai_task_context_and_pydantic_outputs_without_inference | monkeypatch | Parameter for monkeypatch in test_real_crewai_task_context_and_pydantic_outputs_without_inference; use the enclosing contract and type below. | pytest.MonkeyPatch | Enclosing invocation or class/instance lifetime | 228 |
| test_real_crewai_task_context_and_pydantic_outputs_without_inference | Crew | Imported dependency for Crew in test_real_crewai_task_context_and_pydantic_outputs_without_inference; use the enclosing contract and type below. | Module or imported public symbol | Enclosing invocation or class/instance lifetime | 231 |
| test_real_crewai_task_context_and_pydantic_outputs_without_inference | TaskOutput | Imported dependency for TaskOutput in test_real_crewai_task_context_and_pydantic_outputs_without_inference; use the enclosing contract and type below. | Module or imported public symbol | Enclosing invocation or class/instance lifetime | 232 |
| test_real_crewai_task_context_and_pydantic_outputs_without_inference | make_application_coordinator | Imported dependency for make application coordinator in test_real_crewai_task_context_and_pydantic_outputs_without_inference; use the enclosing contract and type below. | Module or imported public symbol | Enclosing invocation or class/instance lifetime | 234 |
| test_real_crewai_task_context_and_pydantic_outputs_without_inference | calls | Local binding for calls in test_real_crewai_task_context_and_pydantic_outputs_without_inference; use the enclosing contract and type below. | list | Enclosing invocation or class/instance lifetime | 236 |
| test_real_crewai_task_context_and_pydantic_outputs_without_inference.kickoff | self | Owning instance; its attributes retain state for the instance lifetime. | Crew | Enclosing invocation or class/instance lifetime | 238 |
| test_real_crewai_task_context_and_pydantic_outputs_without_inference.kickoff | task | Loop item for task in test_real_crewai_task_context_and_pydantic_outputs_without_inference.kickoff; use the enclosing contract and type below. | Element of the declared iterable | Enclosing invocation or class/instance lifetime | 240 |
| test_real_crewai_task_context_and_pydantic_outputs_without_inference.kickoff | value | Value at the current validation/rendering boundary; apply the enclosing contract. | Runtime-dependent; see the enclosing callable contract | Enclosing invocation or class/instance lifetime | 243 |
| test_real_crewai_task_context_and_pydantic_outputs_without_inference.kickoff | task.output | Attribute for task.output in test_real_crewai_task_context_and_pydantic_outputs_without_inference.kickoff; use the enclosing contract and type below. | Return type of TaskOutput; see its callable contract | Enclosing invocation or class/instance lifetime | 248 |
| test_real_crewai_task_context_and_pydantic_outputs_without_inference | coordinator | Local binding for coordinator in test_real_crewai_task_context_and_pydantic_outputs_without_inference; use the enclosing contract and type below. | Return type of make_application_coordinator; see its callable contract | Enclosing invocation or class/instance lifetime | 257 |
| test_failed_crew_releases_capacity_without_retry | tmp_path | Parameter for tmp path in test_failed_crew_releases_capacity_without_retry; use the enclosing contract and type below. | Path | Enclosing invocation or class/instance lifetime | 269 |
| test_failed_crew_releases_capacity_without_retry | make_application_coordinator | Imported dependency for make application coordinator in test_failed_crew_releases_capacity_without_retry; use the enclosing contract and type below. | Module or imported public symbol | Enclosing invocation or class/instance lifetime | 271 |
| test_failed_crew_releases_capacity_without_retry | framework | Local binding for framework in test_failed_crew_releases_capacity_without_retry; use the enclosing contract and type below. | Return type of backend; see its callable contract | Enclosing invocation or class/instance lifetime | 273 |
| test_failed_crew_releases_capacity_without_retry | original | Local binding for original in test_failed_crew_releases_capacity_without_retry; use the enclosing contract and type below. | Runtime-dependent; see the enclosing callable contract | Enclosing invocation or class/instance lifetime | 274 |
| test_failed_crew_releases_capacity_without_retry | attempts | Local binding for attempts in test_failed_crew_releases_capacity_without_retry; use the enclosing contract and type below. | list | Enclosing invocation or class/instance lifetime | 275 |
| test_failed_crew_releases_capacity_without_retry.fail | self | Owning instance; its attributes retain state for the instance lifetime. | object | Enclosing invocation or class/instance lifetime | 277 |
| test_failed_crew_releases_capacity_without_retry | framework.Crew.kickoff | Attribute for framework.Crew.kickoff in test_failed_crew_releases_capacity_without_retry; use the enclosing contract and type below. | Runtime-dependent; see the enclosing callable contract | Enclosing invocation or class/instance lifetime | 282, 287 |
| test_failed_crew_releases_capacity_without_retry | coordinator | Local binding for coordinator in test_failed_crew_releases_capacity_without_retry; use the enclosing contract and type below. | Return type of make_application_coordinator; see its callable contract | Enclosing invocation or class/instance lifetime | 283 |
| test_missing_structured_output_cannot_reach_approval | tmp_path | Parameter for tmp path in test_missing_structured_output_cannot_reach_approval; use the enclosing contract and type below. | Path | Enclosing invocation or class/instance lifetime | 294 |
| test_missing_structured_output_cannot_reach_approval | make_application_coordinator | Imported dependency for make application coordinator in test_missing_structured_output_cannot_reach_approval; use the enclosing contract and type below. | Module or imported public symbol | Enclosing invocation or class/instance lifetime | 296 |
| test_missing_structured_output_cannot_reach_approval | framework | Local binding for framework in test_missing_structured_output_cannot_reach_approval; use the enclosing contract and type below. | Return type of backend; see its callable contract | Enclosing invocation or class/instance lifetime | 298 |
| test_missing_structured_output_cannot_reach_approval | framework.Crew.kickoff | Attribute for framework.Crew.kickoff in test_missing_structured_output_cannot_reach_approval; use the enclosing contract and type below. | Runtime-dependent; see the enclosing callable contract | Enclosing invocation or class/instance lifetime | 299 |
| test_missing_structured_output_cannot_reach_approval.lambda_299 | self | Owning instance; its attributes retain state for the instance lifetime. | Defined by the enclosing callback contract | Enclosing invocation or class/instance lifetime | 299 |
| test_missing_structured_output_cannot_reach_approval | coordinator | Local binding for coordinator in test_missing_structured_output_cannot_reach_approval; use the enclosing contract and type below. | Return type of make_application_coordinator; see its callable contract | Enclosing invocation or class/instance lifetime | 300 |
| test_application_verbose_and_events_belong_to_the_owning_session | tmp_path | Parameter for tmp path in test_application_verbose_and_events_belong_to_the_owning_session; use the enclosing contract and type below. | Path | Enclosing invocation or class/instance lifetime | 306 |
| test_application_verbose_and_events_belong_to_the_owning_session | io | Imported dependency for io in test_application_verbose_and_events_belong_to_the_owning_session; use the enclosing contract and type below. | Module or imported public symbol | Enclosing invocation or class/instance lifetime | 308 |
| test_application_verbose_and_events_belong_to_the_owning_session | logging | Imported dependency for logging in test_application_verbose_and_events_belong_to_the_owning_session; use the enclosing contract and type below. | Module or imported public symbol | Enclosing invocation or class/instance lifetime | 309 |
| test_application_verbose_and_events_belong_to_the_owning_session | RLock | Imported dependency for RLock in test_application_verbose_and_events_belong_to_the_owning_session; use the enclosing contract and type below. | Module or imported public symbol | Enclosing invocation or class/instance lifetime | 310 |
| test_application_verbose_and_events_belong_to_the_owning_session | ApplicationsBackend | Imported dependency for ApplicationsBackend in test_application_verbose_and_events_belong_to_the_owning_session; use the enclosing contract and type below. | Module or imported public symbol | Enclosing invocation or class/instance lifetime | 312 |
| test_application_verbose_and_events_belong_to_the_owning_session | SessionRegistry | Imported dependency for SessionRegistry in test_application_verbose_and_events_belong_to_the_owning_session; use the enclosing contract and type below. | Module or imported public symbol | Enclosing invocation or class/instance lifetime | 313 |
| test_application_verbose_and_events_belong_to_the_owning_session | ConsoleThoughtsCapture | Imported dependency for ConsoleThoughtsCapture in test_application_verbose_and_events_belong_to_the_owning_session; use the enclosing contract and type below. | Module or imported public symbol | Enclosing invocation or class/instance lifetime | 314 |
| test_application_verbose_and_events_belong_to_the_owning_session | activity_output | Imported dependency for activity output in test_application_verbose_and_events_belong_to_the_owning_session; use the enclosing contract and type below. | Module or imported public symbol | Enclosing invocation or class/instance lifetime | 315 |
| test_application_verbose_and_events_belong_to_the_owning_session | log_event | Imported dependency for log event in test_application_verbose_and_events_belong_to_the_owning_session; use the enclosing contract and type below. | Module or imported public symbol | Enclosing invocation or class/instance lifetime | 315 |
| test_application_verbose_and_events_belong_to_the_owning_session.controller | identity | Explicit owner identity used by a session factory or fixture. | str | Enclosing invocation or class/instance lifetime | 317 |
| test_application_verbose_and_events_belong_to_the_owning_session | sessions | Local binding for sessions in test_application_verbose_and_events_belong_to_the_owning_session; use the enclosing contract and type below. | Return type of SessionRegistry; see its callable contract | Enclosing invocation or class/instance lifetime | 333 |
| test_application_verbose_and_events_belong_to_the_owning_session | alice | Local binding for alice in test_application_verbose_and_events_belong_to_the_owning_session; use the enclosing contract and type below. | Return type of resolve; see its callable contract | Enclosing invocation or class/instance lifetime | 334 |
| test_application_verbose_and_events_belong_to_the_owning_session | bob | Local binding for bob in test_application_verbose_and_events_belong_to_the_owning_session; use the enclosing contract and type below. | Return type of resolve; see its callable contract | Enclosing invocation or class/instance lifetime | 335 |
| test_application_verbose_and_events_belong_to_the_owning_session.Pipeline.__init__ | self | Owning instance; its attributes retain state for the instance lifetime. | Not explicitly annotated | Enclosing invocation or class/instance lifetime | 340 |
| test_application_verbose_and_events_belong_to_the_owning_session.Pipeline.__init__ | root | Explicit root directory against which named paths are resolved. | Path | Enclosing invocation or class/instance lifetime | 340 |
| test_application_verbose_and_events_belong_to_the_owning_session.Pipeline.__init__ | self.root | Explicit root directory against which named paths are resolved. | Runtime-dependent; see the enclosing callable contract | Enclosing invocation or class/instance lifetime | 342 |
| test_application_verbose_and_events_belong_to_the_owning_session.Pipeline.generate | self | Owning instance; its attributes retain state for the instance lifetime. | Not explicitly annotated | Enclosing invocation or class/instance lifetime | 344 |
| test_application_verbose_and_events_belong_to_the_owning_session.Pipeline.generate | query | Original user request or a trusted test query; avoid payload logging by default. | str | Enclosing invocation or class/instance lifetime | 344 |
| test_application_verbose_and_events_belong_to_the_owning_session.Pipeline.generate | tools | Parameter for tools in test_application_verbose_and_events_belong_to_the_owning_session.Pipeline.generate; use the enclosing contract and type below. | dict | Enclosing invocation or class/instance lifetime | 344 |
| test_application_verbose_and_events_belong_to_the_owning_session | service | Local binding for service in test_application_verbose_and_events_belong_to_the_owning_session; use the enclosing contract and type below. | Return type of ApplicationsBackend; see its callable contract | Enclosing invocation or class/instance lifetime | 352 |
| test_application_verbose_and_events_belong_to_the_owning_session.lambda_355 | _ | Callback parameter for  in test_application_verbose_and_events_belong_to_the_owning_session.lambda_355; use the enclosing contract and type below. | Defined by the enclosing callback contract | Enclosing invocation or class/instance lifetime | 355 |
| test_application_verbose_and_events_belong_to_the_owning_session | rows | Local binding for rows in test_application_verbose_and_events_belong_to_the_owning_session; use the enclosing contract and type below. | Return type of list; see its callable contract | Enclosing invocation or class/instance lifetime | 358 |
| test_application_verbose_and_events_belong_to_the_owning_session | output | Local binding for output in test_application_verbose_and_events_belong_to_the_owning_session; use the enclosing contract and type below. | Return type of get_logs; see its callable contract | Enclosing invocation or class/instance lifetime | 362 |
