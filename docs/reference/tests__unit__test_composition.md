# Reference for tests/unit/test_composition.py

Specify explicit startup and independent service wiring before extraction.

Source fingerprint: 995c9ca6c71b6bea55598d2c88b389aed2e4b68675fbc5f0a00328afde0f8c66

This reference is generated from maintained source without imports or execution. Assigned values are intentionally omitted. Runtime-dependent types are explicit; the enclosing docstring defines the behavioral contract. See [architecture](../ARCHITECTURE_QUALITY.md) for manually reviewed responsibility and dependency decisions.

## Classes and callables

### test_settings_are_immutable_and_do_not_create_storage

Verify settings are immutable and do not create storage.

Kind: callable. Declared return: Not declared / class. Source line: 7.

### test_explicit_runtime_connects_llm_agents_and_services

Verify explicit runtime connects llm agents and services.

Kind: callable. Declared return: Not declared / class. Source line: 18.

### test_view_binds_controller_and_preserves_launch_options

Verify view binds controller and preserves launch options.

Kind: callable. Declared return: Not declared / class. Source line: 51.

### test_view_binds_controller_and_preserves_launch_options.Component

Provide Component for the enclosing trusted test fixture.

Kind: class. Declared return: Not declared / class. Source line: 57.

### test_view_binds_controller_and_preserves_launch_options.Component.__init__

Provide init for the enclosing trusted test fixture.

Kind: callable. Declared return: Not declared / class. Source line: 60.

### test_view_binds_controller_and_preserves_launch_options.Component.__enter__

Provide enter for the enclosing trusted test fixture.

Kind: callable. Declared return: Not declared / class. Source line: 64.

### test_view_binds_controller_and_preserves_launch_options.Component.__exit__

Provide exit for the enclosing trusted test fixture.

Kind: callable. Declared return: Not declared / class. Source line: 68.

### test_view_binds_controller_and_preserves_launch_options.Component.__getattr__

Provide getattr for the enclosing trusted test fixture.

Kind: callable. Declared return: Not declared / class. Source line: 72.

### test_view_binds_controller_and_preserves_launch_options.Component.__getattr__.event

Provide event for the enclosing trusted test fixture.

Kind: callable. Declared return: Not declared / class. Source line: 75.

## Variables and parameters

| Scope | Name | Role and meaning | Type | Lifetime | Writes |
| --- | --- | --- | --- | --- | --- |
| module | SimpleNamespace | Imported dependency for SimpleNamespace in module; use the enclosing contract and type below. | Module or imported public symbol | Module/process lifetime | 3 |
| module | Mock | Imported dependency for Mock in module; use the enclosing contract and type below. | Module or imported public symbol | Module/process lifetime | 4 |
| test_settings_are_immutable_and_do_not_create_storage | tmp_path | Parameter for tmp path in test_settings_are_immutable_and_do_not_create_storage; use the enclosing contract and type below. | Not explicitly annotated | Enclosing invocation or class/instance lifetime | 7 |
| test_settings_are_immutable_and_do_not_create_storage | Settings | Imported dependency for Settings in test_settings_are_immutable_and_do_not_create_storage; use the enclosing contract and type below. | Module or imported public symbol | Enclosing invocation or class/instance lifetime | 9 |
| test_settings_are_immutable_and_do_not_create_storage | settings | Immutable startup configuration; constructing it does not start external services. | Return type of from_environment; see its callable contract | Enclosing invocation or class/instance lifetime | 11 |
| test_explicit_runtime_connects_llm_agents_and_services | tmp_path | Parameter for tmp path in test_explicit_runtime_connects_llm_agents_and_services; use the enclosing contract and type below. | Not explicitly annotated | Enclosing invocation or class/instance lifetime | 18 |
| test_explicit_runtime_connects_llm_agents_and_services | create_runtime | Imported dependency for create runtime in test_explicit_runtime_connects_llm_agents_and_services; use the enclosing contract and type below. | Module or imported public symbol | Enclosing invocation or class/instance lifetime | 20 |
| test_explicit_runtime_connects_llm_agents_and_services | Settings | Imported dependency for Settings in test_explicit_runtime_connects_llm_agents_and_services; use the enclosing contract and type below. | Module or imported public symbol | Enclosing invocation or class/instance lifetime | 21 |
| test_explicit_runtime_connects_llm_agents_and_services | llm | Local binding for llm in test_explicit_runtime_connects_llm_agents_and_services; use the enclosing contract and type below. | Return type of object; see its callable contract | Enclosing invocation or class/instance lifetime | 23 |
| test_explicit_runtime_connects_llm_agents_and_services | factory | Local binding for factory in test_explicit_runtime_connects_llm_agents_and_services; use the enclosing contract and type below. | Return type of Mock; see its callable contract | Enclosing invocation or class/instance lifetime | 24 |
| test_explicit_runtime_connects_llm_agents_and_services | register | Local binding for register in test_explicit_runtime_connects_llm_agents_and_services; use the enclosing contract and type below. | Return type of Mock; see its callable contract | Enclosing invocation or class/instance lifetime | 25 |
| test_explicit_runtime_connects_llm_agents_and_services.lambda_25 | operations | Callback parameter for operations in test_explicit_runtime_connects_llm_agents_and_services.lambda_25; use the enclosing contract and type below. | Defined by the enclosing callback contract | Enclosing invocation or class/instance lifetime | 25 |
| test_explicit_runtime_connects_llm_agents_and_services | agents | Local binding for agents in test_explicit_runtime_connects_llm_agents_and_services; use the enclosing contract and type below. | Return type of SimpleNamespace; see its callable contract | Enclosing invocation or class/instance lifetime | 26 |
| test_explicit_runtime_connects_llm_agents_and_services | agent_factory | Local binding for agent factory in test_explicit_runtime_connects_llm_agents_and_services; use the enclosing contract and type below. | Return type of Mock; see its callable contract | Enclosing invocation or class/instance lifetime | 33 |
| test_explicit_runtime_connects_llm_agents_and_services | backend | Injected framework/execution provider; callers determine the required protocol. | Return type of SimpleNamespace; see its callable contract | Enclosing invocation or class/instance lifetime | 34 |
| test_explicit_runtime_connects_llm_agents_and_services | runtime | Explicitly composed application services for one owner or compatibility facade. | Return type of create_runtime; see its callable contract | Enclosing invocation or class/instance lifetime | 37 |
| test_view_binds_controller_and_preserves_launch_options | build_view | Imported dependency for build view in test_view_binds_controller_and_preserves_launch_options; use the enclosing contract and type below. | Module or imported public symbol | Enclosing invocation or class/instance lifetime | 53 |
| test_view_binds_controller_and_preserves_launch_options | launch | Imported dependency for launch in test_view_binds_controller_and_preserves_launch_options; use the enclosing contract and type below. | Module or imported public symbol | Enclosing invocation or class/instance lifetime | 53 |
| test_view_binds_controller_and_preserves_launch_options | events | Local binding for events in test_view_binds_controller_and_preserves_launch_options; use the enclosing contract and type below. | list | Enclosing invocation or class/instance lifetime | 55 |
| test_view_binds_controller_and_preserves_launch_options.Component.__init__ | self | Owning instance; its attributes retain state for the instance lifetime. | Not explicitly annotated | Enclosing invocation or class/instance lifetime | 60 |
| test_view_binds_controller_and_preserves_launch_options.Component.__init__ | args | Parameter for args in test_view_binds_controller_and_preserves_launch_options.Component.__init__; use the enclosing contract and type below. | Not explicitly annotated | Enclosing invocation or class/instance lifetime | 60 |
| test_view_binds_controller_and_preserves_launch_options.Component.__init__ | kwargs | Bounded JSON keyword arguments; no executable objects are accepted. | Not explicitly annotated | Enclosing invocation or class/instance lifetime | 60 |
| test_view_binds_controller_and_preserves_launch_options.Component.__init__ | self.kwargs | Bounded JSON keyword arguments; no executable objects are accepted. | Runtime-dependent; see the enclosing callable contract | Enclosing invocation or class/instance lifetime | 62 |
| test_view_binds_controller_and_preserves_launch_options.Component.__enter__ | self | Owning instance; its attributes retain state for the instance lifetime. | Not explicitly annotated | Enclosing invocation or class/instance lifetime | 64 |
| test_view_binds_controller_and_preserves_launch_options.Component.__exit__ | self | Owning instance; its attributes retain state for the instance lifetime. | Not explicitly annotated | Enclosing invocation or class/instance lifetime | 68 |
| test_view_binds_controller_and_preserves_launch_options.Component.__exit__ | args | Parameter for args in test_view_binds_controller_and_preserves_launch_options.Component.__exit__; use the enclosing contract and type below. | Not explicitly annotated | Enclosing invocation or class/instance lifetime | 68 |
| test_view_binds_controller_and_preserves_launch_options.Component.__getattr__ | self | Owning instance; its attributes retain state for the instance lifetime. | Not explicitly annotated | Enclosing invocation or class/instance lifetime | 72 |
| test_view_binds_controller_and_preserves_launch_options.Component.__getattr__ | name | Current identifier selected by parsing, lookup or dependency registration. | Not explicitly annotated | Enclosing invocation or class/instance lifetime | 72 |
| test_view_binds_controller_and_preserves_launch_options.Component.__getattr__.event | kwargs | Bounded JSON keyword arguments; no executable objects are accepted. | Not explicitly annotated | Enclosing invocation or class/instance lifetime | 75 |
| test_view_binds_controller_and_preserves_launch_options | gr | Local binding for gr in test_view_binds_controller_and_preserves_launch_options; use the enclosing contract and type below. | Return type of SimpleNamespace; see its callable contract | Enclosing invocation or class/instance lifetime | 82 |
| test_view_binds_controller_and_preserves_launch_options.comprehension_83 | name | Current identifier selected by parsing, lookup or dependency registration. | Element of the declared iterable | This comprehension only; does not leak into its enclosing scope | 85 |
| test_view_binds_controller_and_preserves_launch_options | controller | Local binding for controller in test_view_binds_controller_and_preserves_launch_options; use the enclosing contract and type below. | Return type of Mock; see its callable contract | Enclosing invocation or class/instance lifetime | 108 |
| test_view_binds_controller_and_preserves_launch_options | controller.get_installed_tools_catalog.return_value | Attribute for controller.get installed tools catalog.return value in test_view_binds_controller_and_preserves_launch_options; use the enclosing contract and type below. | str | Enclosing invocation or class/instance lifetime | 109 |
| test_view_binds_controller_and_preserves_launch_options | SessionRegistry | Imported dependency for SessionRegistry in test_view_binds_controller_and_preserves_launch_options; use the enclosing contract and type below. | Module or imported public symbol | Enclosing invocation or class/instance lifetime | 110 |
| test_view_binds_controller_and_preserves_launch_options | view | Local binding for view in test_view_binds_controller_and_preserves_launch_options; use the enclosing contract and type below. | Return type of build_view; see its callable contract | Enclosing invocation or class/instance lifetime | 112 |
| test_view_binds_controller_and_preserves_launch_options.lambda_112 | session_id | Browser or terminal session identifier for state and diagnostic ownership. | Defined by the enclosing callback contract | Enclosing invocation or class/instance lifetime | 112 |
| test_view_binds_controller_and_preserves_launch_options.comprehension_113 | _ | Comprehension item for  in test_view_binds_controller_and_preserves_launch_options.comprehension_113; use the enclosing contract and type below. | Element of the declared iterable | This comprehension only; does not leak into its enclosing scope | 113 |
| test_view_binds_controller_and_preserves_launch_options.comprehension_113 | data | Comprehension item for data in test_view_binds_controller_and_preserves_launch_options.comprehension_113; use the enclosing contract and type below. | Element of the declared iterable | This comprehension only; does not leak into its enclosing scope | 113 |
| test_view_binds_controller_and_preserves_launch_options.comprehension_114 | _ | Comprehension item for  in test_view_binds_controller_and_preserves_launch_options.comprehension_114; use the enclosing contract and type below. | Element of the declared iterable | This comprehension only; does not leak into its enclosing scope | 114 |
| test_view_binds_controller_and_preserves_launch_options.comprehension_114 | data | Comprehension item for data in test_view_binds_controller_and_preserves_launch_options.comprehension_114; use the enclosing contract and type below. | Element of the declared iterable | This comprehension only; does not leak into its enclosing scope | 114 |
| test_view_binds_controller_and_preserves_launch_options | options | Local binding for options in test_view_binds_controller_and_preserves_launch_options; use the enclosing contract and type below. | Runtime-dependent; see the enclosing callable contract | Enclosing invocation or class/instance lifetime | 116 |
| test_view_binds_controller_and_preserves_launch_options.comprehension_116 | name | Current identifier selected by parsing, lookup or dependency registration. | Element of the declared iterable | This comprehension only; does not leak into its enclosing scope | 116 |
| test_view_binds_controller_and_preserves_launch_options.comprehension_116 | data | Comprehension item for data in test_view_binds_controller_and_preserves_launch_options.comprehension_116; use the enclosing contract and type below. | Element of the declared iterable | This comprehension only; does not leak into its enclosing scope | 116 |
