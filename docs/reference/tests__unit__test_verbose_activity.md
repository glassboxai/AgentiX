# Reference for tests/unit/test_verbose_activity.py

LIVE-UX-001: preserve verbose agent messages alongside technical events.

Source fingerprint: ad147505db71d8302d6c4d1aab1393a4e3e4221f17f474e59efa41795fb9523e

This reference is generated from maintained source without imports or execution. Assigned values are intentionally omitted. Runtime-dependent types are explicit; the enclosing docstring defines the behavioral contract. See [architecture](../ARCHITECTURE_QUALITY.md) for manually reviewed responsibility and dependency decisions.

## Classes and callables

### test_every_application_agent_keeps_verbose_enabled

Verify every application agent keeps verbose enabled.

Kind: callable. Declared return: Not declared / class. Source line: 16.

### test_gated_creation_crews_keep_verbose_enabled

Verify gated creation crews keep verbose enabled.

Kind: callable. Declared return: Not declared / class. Source line: 22.

### test_gated_creation_crews_keep_verbose_enabled.crew

Provide crew for the enclosing trusted test fixture.

Kind: callable. Declared return: Not declared / class. Source line: 27.

### test_gated_creation_crews_keep_verbose_enabled.crew.kickoff

Provide kickoff for the enclosing trusted test fixture.

Kind: callable. Declared return: Not declared / class. Source line: 32.

### test_manager_and_final_execution_crews_keep_verbose_enabled

Check constructor policy only; this fixture does not validate execution.

Kind: callable. Declared return: Not declared / class. Source line: 47.

### test_manager_and_final_execution_crews_keep_verbose_enabled.crew

Provide crew for the enclosing trusted test fixture.

Kind: callable. Declared return: Not declared / class. Source line: 51.

### test_verbose_output_and_technical_events_remain_owner_bound

Verify verbose output and technical events remain owner bound.

Kind: callable. Declared return: Not declared / class. Source line: 69.

### test_verbose_output_and_technical_events_remain_owner_bound.worker

Provide worker for the enclosing trusted test fixture.

Kind: callable. Declared return: Not declared / class. Source line: 79.

### test_activity_output_restores_original_stream_after_failure

Verify activity output restores original stream after failure.

Kind: callable. Declared return: Not declared / class. Source line: 104.

### test_unicode_verbose_message_survives_legacy_windows_console

A narrow host encoding must not prevent the GUI from seeing SDK messages.

Kind: callable. Declared return: Not declared / class. Source line: 115.

### test_unicode_verbose_message_survives_legacy_windows_console.LegacyConsole

Provide LegacyConsole for the enclosing trusted test fixture.

Kind: class. Declared return: Not declared / class. Source line: 118.

### test_unicode_verbose_message_survives_legacy_windows_console.LegacyConsole.write

Provide write for the enclosing trusted test fixture.

Kind: callable. Declared return: Not declared / class. Source line: 121.

### test_fragmented_verbose_output_preserves_logical_lines_and_ansi

Verify fragmented verbose output preserves logical lines and ansi.

Kind: callable. Declared return: Not declared / class. Source line: 133.

## Variables and parameters

| Scope | Name | Role and meaning | Type | Lifetime | Writes |
| --- | --- | --- | --- | --- | --- |
| module | io | Imported dependency for io in module; use the enclosing contract and type below. | Module or imported public symbol | Module/process lifetime | 3 |
| module | logging | Imported dependency for logging in module; use the enclosing contract and type below. | Module or imported public symbol | Module/process lifetime | 4 |
| module | sys | Imported dependency for sys in module; use the enclosing contract and type below. | Module or imported public symbol | Module/process lifetime | 5 |
| module | threading | Imported dependency for threading in module; use the enclosing contract and type below. | Module or imported public symbol | Module/process lifetime | 6 |
| module | SimpleNamespace | Imported dependency for SimpleNamespace in module; use the enclosing contract and type below. | Module or imported public symbol | Module/process lifetime | 7 |
| module | pytest | Imported dependency for pytest in module; use the enclosing contract and type below. | Module or imported public symbol | Module/process lifetime | 9 |
| module | log_event | Imported dependency for log event in module; use the enclosing contract and type below. | Module or imported public symbol | Module/process lifetime | 11 |
| module | operation_scope | Imported dependency for operation scope in module; use the enclosing contract and type below. | Module or imported public symbol | Module/process lifetime | 11 |
| module | ConsoleThoughtsCapture | Imported dependency for ConsoleThoughtsCapture in module; use the enclosing contract and type below. | Module or imported public symbol | Module/process lifetime | 12 |
| test_every_application_agent_keeps_verbose_enabled | system | Parameter for system in test_every_application_agent_keeps_verbose_enabled; use the enclosing contract and type below. | Not explicitly annotated | Enclosing invocation or class/instance lifetime | 16 |
| test_every_application_agent_keeps_verbose_enabled | role | Parameter for role in test_every_application_agent_keeps_verbose_enabled; use the enclosing contract and type below. | Not explicitly annotated | Enclosing invocation or class/instance lifetime | 16 |
| test_every_application_agent_keeps_verbose_enabled | agent | Local binding for agent in test_every_application_agent_keeps_verbose_enabled; use the enclosing contract and type below. | Return type of getattr; see its callable contract | Enclosing invocation or class/instance lifetime | 18 |
| test_gated_creation_crews_keep_verbose_enabled | system | Parameter for system in test_gated_creation_crews_keep_verbose_enabled; use the enclosing contract and type below. | Not explicitly annotated | Enclosing invocation or class/instance lifetime | 22 |
| test_gated_creation_crews_keep_verbose_enabled | monkeypatch | Parameter for monkeypatch in test_gated_creation_crews_keep_verbose_enabled; use the enclosing contract and type below. | Not explicitly annotated | Enclosing invocation or class/instance lifetime | 22 |
| test_gated_creation_crews_keep_verbose_enabled | observed | Returned observation checked against the reviewed host-side expectation. | list | Enclosing invocation or class/instance lifetime | 24 |
| test_gated_creation_crews_keep_verbose_enabled | system.security.auto_approve | Attribute for system.security.auto approve in test_gated_creation_crews_keep_verbose_enabled; use the enclosing contract and type below. | bool | Enclosing invocation or class/instance lifetime | 25 |
| test_gated_creation_crews_keep_verbose_enabled.crew | kwargs | Bounded JSON keyword arguments; no executable objects are accepted. | Not explicitly annotated | Enclosing invocation or class/instance lifetime | 27 |
| test_gated_creation_crews_keep_verbose_enabled.crew | stage | Local binding for stage in test_gated_creation_crews_keep_verbose_enabled.crew; use the enclosing contract and type below. | Return type of len; see its callable contract | Enclosing invocation or class/instance lifetime | 30 |
| test_manager_and_final_execution_crews_keep_verbose_enabled | system | Parameter for system in test_manager_and_final_execution_crews_keep_verbose_enabled; use the enclosing contract and type below. | Not explicitly annotated | Enclosing invocation or class/instance lifetime | 47 |
| test_manager_and_final_execution_crews_keep_verbose_enabled | monkeypatch | Parameter for monkeypatch in test_manager_and_final_execution_crews_keep_verbose_enabled; use the enclosing contract and type below. | Not explicitly annotated | Enclosing invocation or class/instance lifetime | 47 |
| test_manager_and_final_execution_crews_keep_verbose_enabled | observed | Returned observation checked against the reviewed host-side expectation. | list | Enclosing invocation or class/instance lifetime | 49 |
| test_manager_and_final_execution_crews_keep_verbose_enabled.crew | kwargs | Bounded JSON keyword arguments; no executable objects are accepted. | Not explicitly annotated | Enclosing invocation or class/instance lifetime | 51 |
| test_manager_and_final_execution_crews_keep_verbose_enabled.crew | response | Bounded response text to render or validate; it is not executable code. | Runtime-dependent; see the enclosing callable contract | Enclosing invocation or class/instance lifetime | 54 |
| test_manager_and_final_execution_crews_keep_verbose_enabled.lambda_63 | name | Current identifier selected by parsing, lookup or dependency registration. | Defined by the enclosing callback contract | Enclosing invocation or class/instance lifetime | 63 |
| test_manager_and_final_execution_crews_keep_verbose_enabled.lambda_64 | name | Current identifier selected by parsing, lookup or dependency registration. | Defined by the enclosing callback contract | Enclosing invocation or class/instance lifetime | 64 |
| test_verbose_output_and_technical_events_remain_owner_bound | monkeypatch | Parameter for monkeypatch in test_verbose_output_and_technical_events_remain_owner_bound; use the enclosing contract and type below. | Not explicitly annotated | Enclosing invocation or class/instance lifetime | 69 |
| test_verbose_output_and_technical_events_remain_owner_bound | activity_output | Imported dependency for activity output in test_verbose_output_and_technical_events_remain_owner_bound; use the enclosing contract and type below. | Module or imported public symbol | Enclosing invocation or class/instance lifetime | 71 |
| test_verbose_output_and_technical_events_remain_owner_bound | host | Local binding for host in test_verbose_output_and_technical_events_remain_owner_bound; use the enclosing contract and type below. | Return type of StringIO; see its callable contract | Enclosing invocation or class/instance lifetime | 73 |
| test_verbose_output_and_technical_events_remain_owner_bound | captures | Local binding for captures in test_verbose_output_and_technical_events_remain_owner_bound; use the enclosing contract and type below. | dict | Enclosing invocation or class/instance lifetime | 75 |
| test_verbose_output_and_technical_events_remain_owner_bound.comprehension_75 | owner | Comprehension item for owner in test_verbose_output_and_technical_events_remain_owner_bound.comprehension_75; use the enclosing contract and type below. | Element of the declared iterable | This comprehension only; does not leak into its enclosing scope | 75 |
| test_verbose_output_and_technical_events_remain_owner_bound | barrier | Local binding for barrier in test_verbose_output_and_technical_events_remain_owner_bound; use the enclosing contract and type below. | Return type of Barrier; see its callable contract | Enclosing invocation or class/instance lifetime | 76 |
| test_verbose_output_and_technical_events_remain_owner_bound | errors | Local binding for errors in test_verbose_output_and_technical_events_remain_owner_bound; use the enclosing contract and type below. | list | Enclosing invocation or class/instance lifetime | 77 |
| test_verbose_output_and_technical_events_remain_owner_bound.worker | owner | Parameter for owner in test_verbose_output_and_technical_events_remain_owner_bound.worker; use the enclosing contract and type below. | Not explicitly annotated | Enclosing invocation or class/instance lifetime | 79 |
| test_verbose_output_and_technical_events_remain_owner_bound.worker | exc | Caught exception for exc in test_verbose_output_and_technical_events_remain_owner_bound.worker; use the enclosing contract and type below. | BaseException | Current exception handler; Python clears this binding afterward | 86 |
| test_verbose_output_and_technical_events_remain_owner_bound | threads | Local binding for threads in test_verbose_output_and_technical_events_remain_owner_bound; use the enclosing contract and type below. | list | Enclosing invocation or class/instance lifetime | 90 |
| test_verbose_output_and_technical_events_remain_owner_bound.comprehension_90 | owner | Comprehension item for owner in test_verbose_output_and_technical_events_remain_owner_bound.comprehension_90; use the enclosing contract and type below. | Element of the declared iterable | This comprehension only; does not leak into its enclosing scope | 90 |
| test_verbose_output_and_technical_events_remain_owner_bound | thread | Loop item for thread in test_verbose_output_and_technical_events_remain_owner_bound; use the enclosing contract and type below. | Element of the declared iterable | Enclosing invocation or class/instance lifetime | 91, 93 |
| test_verbose_output_and_technical_events_remain_owner_bound.comprehension_95 | thread | Comprehension item for thread in test_verbose_output_and_technical_events_remain_owner_bound.comprehension_95; use the enclosing contract and type below. | Element of the declared iterable | This comprehension only; does not leak into its enclosing scope | 95 |
| test_verbose_output_and_technical_events_remain_owner_bound | owner | Loop item for owner in test_verbose_output_and_technical_events_remain_owner_bound; use the enclosing contract and type below. | Element of the declared iterable | Enclosing invocation or class/instance lifetime | 98 |
| test_verbose_output_and_technical_events_remain_owner_bound | capture | Loop item for capture in test_verbose_output_and_technical_events_remain_owner_bound; use the enclosing contract and type below. | Element of the declared iterable | Enclosing invocation or class/instance lifetime | 98 |
| test_verbose_output_and_technical_events_remain_owner_bound | text | Local binding for text in test_verbose_output_and_technical_events_remain_owner_bound; use the enclosing contract and type below. | Return type of get_logs; see its callable contract | Enclosing invocation or class/instance lifetime | 99 |
| test_activity_output_restores_original_stream_after_failure | activity_output | Imported dependency for activity output in test_activity_output_restores_original_stream_after_failure; use the enclosing contract and type below. | Module or imported public symbol | Enclosing invocation or class/instance lifetime | 106 |
| test_activity_output_restores_original_stream_after_failure | original | Local binding for original in test_activity_output_restores_original_stream_after_failure; use the enclosing contract and type below. | Runtime-dependent; see the enclosing callable contract | Enclosing invocation or class/instance lifetime | 108 |
| test_unicode_verbose_message_survives_legacy_windows_console.LegacyConsole.write | self | Owning instance; its attributes retain state for the instance lifetime. | Not explicitly annotated | Enclosing invocation or class/instance lifetime | 121 |
| test_unicode_verbose_message_survives_legacy_windows_console.LegacyConsole.write | text | Parameter for text in test_unicode_verbose_message_survives_legacy_windows_console.LegacyConsole.write; use the enclosing contract and type below. | Not explicitly annotated | Enclosing invocation or class/instance lifetime | 121 |
| test_unicode_verbose_message_survives_legacy_windows_console | host | Local binding for host in test_unicode_verbose_message_survives_legacy_windows_console; use the enclosing contract and type below. | Return type of LegacyConsole; see its callable contract | Enclosing invocation or class/instance lifetime | 126 |
| test_unicode_verbose_message_survives_legacy_windows_console | capture | Local binding for capture in test_unicode_verbose_message_survives_legacy_windows_console; use the enclosing contract and type below. | Return type of ConsoleThoughtsCapture; see its callable contract | Enclosing invocation or class/instance lifetime | 127 |
| test_fragmented_verbose_output_preserves_logical_lines_and_ansi | capture | Local binding for capture in test_fragmented_verbose_output_preserves_logical_lines_and_ansi; use the enclosing contract and type below. | Return type of ConsoleThoughtsCapture; see its callable contract | Enclosing invocation or class/instance lifetime | 135 |
| test_fragmented_verbose_output_preserves_logical_lines_and_ansi | fragment | Loop item for fragment in test_fragmented_verbose_output_preserves_logical_lines_and_ansi; use the enclosing contract and type below. | Element of the declared iterable | Enclosing invocation or class/instance lifetime | 136 |
