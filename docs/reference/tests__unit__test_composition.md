# Reference for tests/unit/test_composition.py

Specify explicit startup and independent service wiring before extraction.

Source fingerprint: f5f788b0ee079db65533d9ac2c851e892e5ed4ed0605007b8f101082e8baddbe

This reference is generated from maintained source without imports or execution. Assigned values are intentionally omitted. Runtime-dependent types are explicit; the enclosing docstring defines the behavioral contract. See [architecture](../ARCHITECTURE_QUALITY.md) for manually reviewed responsibility and dependency decisions.

## Classes and callables

### test_settings_are_immutable_and_do_not_create_storage

Verify settings are immutable and do not create storage.

Kind: callable. Declared return: Not declared / class. Source line: 8.

### test_settings_keep_non_artifact_state_under_home_when_tools_are_external

IAC-010: an external artifact root does not relocate drafts into the checkout.

Kind: callable. Declared return: Not declared / class. Source line: 25.

### test_explicit_runtime_connects_llm_agents_and_services

Verify explicit runtime connects llm agents and services.

Kind: callable. Declared return: Not declared / class. Source line: 39.

### test_runtime_keeps_drafts_under_home_when_artifacts_use_the_checkout

IAC-010: runtime wiring must not derive draft storage from an external tool root.

Kind: callable. Declared return: Not declared / class. Source line: 81.

### test_view_binds_controller_and_preserves_launch_options

Verify view binds controller and preserves launch options.

Kind: callable. Declared return: Not declared / class. Source line: 117.

### test_view_binds_controller_and_preserves_launch_options.Component

Provide Component for the enclosing trusted test fixture.

Kind: class. Declared return: Not declared / class. Source line: 123.

### test_view_binds_controller_and_preserves_launch_options.Component.__init__

Provide init for the enclosing trusted test fixture.

Kind: callable. Declared return: Not declared / class. Source line: 126.

### test_view_binds_controller_and_preserves_launch_options.Component.__enter__

Provide enter for the enclosing trusted test fixture.

Kind: callable. Declared return: Not declared / class. Source line: 130.

### test_view_binds_controller_and_preserves_launch_options.Component.__exit__

Provide exit for the enclosing trusted test fixture.

Kind: callable. Declared return: Not declared / class. Source line: 134.

### test_view_binds_controller_and_preserves_launch_options.Component.__getattr__

Provide getattr for the enclosing trusted test fixture.

Kind: callable. Declared return: Not declared / class. Source line: 138.

### test_view_binds_controller_and_preserves_launch_options.Component.__getattr__.event

Provide event for the enclosing trusted test fixture.

Kind: callable. Declared return: Not declared / class. Source line: 141.

## Variables and parameters

| Scope | Name | Role and meaning | Type | Lifetime | Writes |
| --- | --- | --- | --- | --- | --- |
| module | logging | Imported dependency for logging in module; use the enclosing contract and type below. | Module or imported public symbol | Module/process lifetime | 3 |
| module | SimpleNamespace | Imported dependency for SimpleNamespace in module; use the enclosing contract and type below. | Module or imported public symbol | Module/process lifetime | 4 |
| module | Mock | Imported dependency for Mock in module; use the enclosing contract and type below. | Module or imported public symbol | Module/process lifetime | 5 |
| test_settings_are_immutable_and_do_not_create_storage | tmp_path | Parameter for tmp path in test_settings_are_immutable_and_do_not_create_storage; use the enclosing contract and type below. | Not explicitly annotated | Enclosing invocation or class/instance lifetime | 8 |
| test_settings_are_immutable_and_do_not_create_storage | Settings | Imported dependency for Settings in test_settings_are_immutable_and_do_not_create_storage; use the enclosing contract and type below. | Module or imported public symbol | Enclosing invocation or class/instance lifetime | 10 |
| test_settings_are_immutable_and_do_not_create_storage | settings | Immutable startup configuration; constructing it does not start external services. | Return type of from_environment; see its callable contract | Enclosing invocation or class/instance lifetime | 12 |
| test_settings_keep_non_artifact_state_under_home_when_tools_are_external | tmp_path | Parameter for tmp path in test_settings_keep_non_artifact_state_under_home_when_tools_are_external; use the enclosing contract and type below. | Not explicitly annotated | Enclosing invocation or class/instance lifetime | 25 |
| test_settings_keep_non_artifact_state_under_home_when_tools_are_external | Settings | Imported dependency for Settings in test_settings_keep_non_artifact_state_under_home_when_tools_are_external; use the enclosing contract and type below. | Module or imported public symbol | Enclosing invocation or class/instance lifetime | 27 |
| test_settings_keep_non_artifact_state_under_home_when_tools_are_external | home | Local binding for home in test_settings_keep_non_artifact_state_under_home_when_tools_are_external; use the enclosing contract and type below. | Runtime-dependent; see the enclosing callable contract | Enclosing invocation or class/instance lifetime | 29 |
| test_settings_keep_non_artifact_state_under_home_when_tools_are_external | tools | Local binding for tools in test_settings_keep_non_artifact_state_under_home_when_tools_are_external; use the enclosing contract and type below. | Runtime-dependent; see the enclosing callable contract | Enclosing invocation or class/instance lifetime | 30 |
| test_settings_keep_non_artifact_state_under_home_when_tools_are_external | settings | Immutable startup configuration; constructing it does not start external services. | Return type of from_environment; see its callable contract | Enclosing invocation or class/instance lifetime | 31 |
| test_explicit_runtime_connects_llm_agents_and_services | tmp_path | Parameter for tmp path in test_explicit_runtime_connects_llm_agents_and_services; use the enclosing contract and type below. | Not explicitly annotated | Enclosing invocation or class/instance lifetime | 39 |
| test_explicit_runtime_connects_llm_agents_and_services | caplog | Parameter for caplog in test_explicit_runtime_connects_llm_agents_and_services; use the enclosing contract and type below. | Not explicitly annotated | Enclosing invocation or class/instance lifetime | 39 |
| test_explicit_runtime_connects_llm_agents_and_services | create_runtime | Imported dependency for create runtime in test_explicit_runtime_connects_llm_agents_and_services; use the enclosing contract and type below. | Module or imported public symbol | Enclosing invocation or class/instance lifetime | 41 |
| test_explicit_runtime_connects_llm_agents_and_services | Settings | Imported dependency for Settings in test_explicit_runtime_connects_llm_agents_and_services; use the enclosing contract and type below. | Module or imported public symbol | Enclosing invocation or class/instance lifetime | 42 |
| test_explicit_runtime_connects_llm_agents_and_services | llm | Local binding for llm in test_explicit_runtime_connects_llm_agents_and_services; use the enclosing contract and type below. | Return type of object; see its callable contract | Enclosing invocation or class/instance lifetime | 44 |
| test_explicit_runtime_connects_llm_agents_and_services | factory | Local binding for factory in test_explicit_runtime_connects_llm_agents_and_services; use the enclosing contract and type below. | Return type of Mock; see its callable contract | Enclosing invocation or class/instance lifetime | 45 |
| test_explicit_runtime_connects_llm_agents_and_services | register | Local binding for register in test_explicit_runtime_connects_llm_agents_and_services; use the enclosing contract and type below. | Return type of Mock; see its callable contract | Enclosing invocation or class/instance lifetime | 46 |
| test_explicit_runtime_connects_llm_agents_and_services.lambda_46 | operations | Callback parameter for operations in test_explicit_runtime_connects_llm_agents_and_services.lambda_46; use the enclosing contract and type below. | Defined by the enclosing callback contract | Enclosing invocation or class/instance lifetime | 46 |
| test_explicit_runtime_connects_llm_agents_and_services | agents | Local binding for agents in test_explicit_runtime_connects_llm_agents_and_services; use the enclosing contract and type below. | Return type of SimpleNamespace; see its callable contract | Enclosing invocation or class/instance lifetime | 47 |
| test_explicit_runtime_connects_llm_agents_and_services | agent_factory | Local binding for agent factory in test_explicit_runtime_connects_llm_agents_and_services; use the enclosing contract and type below. | Return type of Mock; see its callable contract | Enclosing invocation or class/instance lifetime | 54 |
| test_explicit_runtime_connects_llm_agents_and_services | backend | Injected framework/execution provider; callers determine the required protocol. | Return type of SimpleNamespace; see its callable contract | Enclosing invocation or class/instance lifetime | 55 |
| test_explicit_runtime_connects_llm_agents_and_services | runtime | Explicitly composed application services for one owner or compatibility facade. | Return type of create_runtime; see its callable contract | Enclosing invocation or class/instance lifetime | 59 |
| test_runtime_keeps_drafts_under_home_when_artifacts_use_the_checkout | tmp_path | Parameter for tmp path in test_runtime_keeps_drafts_under_home_when_artifacts_use_the_checkout; use the enclosing contract and type below. | Not explicitly annotated | Enclosing invocation or class/instance lifetime | 81 |
| test_runtime_keeps_drafts_under_home_when_artifacts_use_the_checkout | create_runtime | Imported dependency for create runtime in test_runtime_keeps_drafts_under_home_when_artifacts_use_the_checkout; use the enclosing contract and type below. | Module or imported public symbol | Enclosing invocation or class/instance lifetime | 83 |
| test_runtime_keeps_drafts_under_home_when_artifacts_use_the_checkout | Settings | Imported dependency for Settings in test_runtime_keeps_drafts_under_home_when_artifacts_use_the_checkout; use the enclosing contract and type below. | Module or imported public symbol | Enclosing invocation or class/instance lifetime | 84 |
| test_runtime_keeps_drafts_under_home_when_artifacts_use_the_checkout | home | Local binding for home in test_runtime_keeps_drafts_under_home_when_artifacts_use_the_checkout; use the enclosing contract and type below. | Runtime-dependent; see the enclosing callable contract | Enclosing invocation or class/instance lifetime | 86 |
| test_runtime_keeps_drafts_under_home_when_artifacts_use_the_checkout | tools | Local binding for tools in test_runtime_keeps_drafts_under_home_when_artifacts_use_the_checkout; use the enclosing contract and type below. | Runtime-dependent; see the enclosing callable contract | Enclosing invocation or class/instance lifetime | 87 |
| test_runtime_keeps_drafts_under_home_when_artifacts_use_the_checkout | settings | Immutable startup configuration; constructing it does not start external services. | Return type of from_environment; see its callable contract | Enclosing invocation or class/instance lifetime | 88 |
| test_runtime_keeps_drafts_under_home_when_artifacts_use_the_checkout | security | Owner-scoped approval and path boundary injected into this service. | Return type of SimpleNamespace; see its callable contract | Enclosing invocation or class/instance lifetime | 91 |
| test_runtime_keeps_drafts_under_home_when_artifacts_use_the_checkout | security.configure_tool_storage | Attribute for security.configure tool storage in test_runtime_keeps_drafts_under_home_when_artifacts_use_the_checkout; use the enclosing contract and type below. | Return type of Mock; see its callable contract | Enclosing invocation or class/instance lifetime | 92 |
| test_runtime_keeps_drafts_under_home_when_artifacts_use_the_checkout | agents | Local binding for agents in test_runtime_keeps_drafts_under_home_when_artifacts_use_the_checkout; use the enclosing contract and type below. | Return type of SimpleNamespace; see its callable contract | Enclosing invocation or class/instance lifetime | 93 |
| test_runtime_keeps_drafts_under_home_when_artifacts_use_the_checkout | backend | Injected framework/execution provider; callers determine the required protocol. | Return type of SimpleNamespace; see its callable contract | Enclosing invocation or class/instance lifetime | 100 |
| test_view_binds_controller_and_preserves_launch_options | build_view | Imported dependency for build view in test_view_binds_controller_and_preserves_launch_options; use the enclosing contract and type below. | Module or imported public symbol | Enclosing invocation or class/instance lifetime | 119 |
| test_view_binds_controller_and_preserves_launch_options | launch | Imported dependency for launch in test_view_binds_controller_and_preserves_launch_options; use the enclosing contract and type below. | Module or imported public symbol | Enclosing invocation or class/instance lifetime | 119 |
| test_view_binds_controller_and_preserves_launch_options | events | Local binding for events in test_view_binds_controller_and_preserves_launch_options; use the enclosing contract and type below. | list | Enclosing invocation or class/instance lifetime | 121 |
| test_view_binds_controller_and_preserves_launch_options.Component.__init__ | self | Owning instance; its attributes retain state for the instance lifetime. | Not explicitly annotated | Enclosing invocation or class/instance lifetime | 126 |
| test_view_binds_controller_and_preserves_launch_options.Component.__init__ | args | Parameter for args in test_view_binds_controller_and_preserves_launch_options.Component.__init__; use the enclosing contract and type below. | Not explicitly annotated | Enclosing invocation or class/instance lifetime | 126 |
| test_view_binds_controller_and_preserves_launch_options.Component.__init__ | kwargs | Bounded JSON keyword arguments; no executable objects are accepted. | Not explicitly annotated | Enclosing invocation or class/instance lifetime | 126 |
| test_view_binds_controller_and_preserves_launch_options.Component.__init__ | self.kwargs | Bounded JSON keyword arguments; no executable objects are accepted. | Runtime-dependent; see the enclosing callable contract | Enclosing invocation or class/instance lifetime | 128 |
| test_view_binds_controller_and_preserves_launch_options.Component.__enter__ | self | Owning instance; its attributes retain state for the instance lifetime. | Not explicitly annotated | Enclosing invocation or class/instance lifetime | 130 |
| test_view_binds_controller_and_preserves_launch_options.Component.__exit__ | self | Owning instance; its attributes retain state for the instance lifetime. | Not explicitly annotated | Enclosing invocation or class/instance lifetime | 134 |
| test_view_binds_controller_and_preserves_launch_options.Component.__exit__ | args | Parameter for args in test_view_binds_controller_and_preserves_launch_options.Component.__exit__; use the enclosing contract and type below. | Not explicitly annotated | Enclosing invocation or class/instance lifetime | 134 |
| test_view_binds_controller_and_preserves_launch_options.Component.__getattr__ | self | Owning instance; its attributes retain state for the instance lifetime. | Not explicitly annotated | Enclosing invocation or class/instance lifetime | 138 |
| test_view_binds_controller_and_preserves_launch_options.Component.__getattr__ | name | Current identifier selected by parsing, lookup or dependency registration. | Not explicitly annotated | Enclosing invocation or class/instance lifetime | 138 |
| test_view_binds_controller_and_preserves_launch_options.Component.__getattr__.event | kwargs | Bounded JSON keyword arguments; no executable objects are accepted. | Not explicitly annotated | Enclosing invocation or class/instance lifetime | 141 |
| test_view_binds_controller_and_preserves_launch_options | gr | Local binding for gr in test_view_binds_controller_and_preserves_launch_options; use the enclosing contract and type below. | Return type of SimpleNamespace; see its callable contract | Enclosing invocation or class/instance lifetime | 148 |
| test_view_binds_controller_and_preserves_launch_options.comprehension_149 | name | Current identifier selected by parsing, lookup or dependency registration. | Element of the declared iterable | This comprehension only; does not leak into its enclosing scope | 151 |
| test_view_binds_controller_and_preserves_launch_options | controller | Local binding for controller in test_view_binds_controller_and_preserves_launch_options; use the enclosing contract and type below. | Return type of Mock; see its callable contract | Enclosing invocation or class/instance lifetime | 182 |
| test_view_binds_controller_and_preserves_launch_options | controller.get_installed_tools_catalog.return_value | Attribute for controller.get installed tools catalog.return value in test_view_binds_controller_and_preserves_launch_options; use the enclosing contract and type below. | str | Enclosing invocation or class/instance lifetime | 183 |
| test_view_binds_controller_and_preserves_launch_options | SessionRegistry | Imported dependency for SessionRegistry in test_view_binds_controller_and_preserves_launch_options; use the enclosing contract and type below. | Module or imported public symbol | Enclosing invocation or class/instance lifetime | 184 |
| test_view_binds_controller_and_preserves_launch_options | view | Local binding for view in test_view_binds_controller_and_preserves_launch_options; use the enclosing contract and type below. | Return type of build_view; see its callable contract | Enclosing invocation or class/instance lifetime | 186 |
| test_view_binds_controller_and_preserves_launch_options.lambda_186 | session_id | Browser or terminal session identifier for state and diagnostic ownership. | Defined by the enclosing callback contract | Enclosing invocation or class/instance lifetime | 186 |
| test_view_binds_controller_and_preserves_launch_options.comprehension_187 | _ | Comprehension item for  in test_view_binds_controller_and_preserves_launch_options.comprehension_187; use the enclosing contract and type below. | Element of the declared iterable | This comprehension only; does not leak into its enclosing scope | 187 |
| test_view_binds_controller_and_preserves_launch_options.comprehension_187 | data | Comprehension item for data in test_view_binds_controller_and_preserves_launch_options.comprehension_187; use the enclosing contract and type below. | Element of the declared iterable | This comprehension only; does not leak into its enclosing scope | 187 |
| test_view_binds_controller_and_preserves_launch_options.comprehension_188 | _ | Comprehension item for  in test_view_binds_controller_and_preserves_launch_options.comprehension_188; use the enclosing contract and type below. | Element of the declared iterable | This comprehension only; does not leak into its enclosing scope | 188 |
| test_view_binds_controller_and_preserves_launch_options.comprehension_188 | data | Comprehension item for data in test_view_binds_controller_and_preserves_launch_options.comprehension_188; use the enclosing contract and type below. | Element of the declared iterable | This comprehension only; does not leak into its enclosing scope | 188 |
| test_view_binds_controller_and_preserves_launch_options | options | Local binding for options in test_view_binds_controller_and_preserves_launch_options; use the enclosing contract and type below. | Runtime-dependent; see the enclosing callable contract | Enclosing invocation or class/instance lifetime | 190 |
| test_view_binds_controller_and_preserves_launch_options.comprehension_190 | name | Current identifier selected by parsing, lookup or dependency registration. | Element of the declared iterable | This comprehension only; does not leak into its enclosing scope | 190 |
| test_view_binds_controller_and_preserves_launch_options.comprehension_190 | data | Comprehension item for data in test_view_binds_controller_and_preserves_launch_options.comprehension_190; use the enclosing contract and type below. | Element of the declared iterable | This comprehension only; does not leak into its enclosing scope | 190 |
