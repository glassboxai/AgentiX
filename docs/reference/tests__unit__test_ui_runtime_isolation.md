# Reference for tests/unit/test_ui_runtime_isolation.py

Verify production session composition does not reuse mutable provider clients.

Source fingerprint: fd62fda95c85fd9c91700da155acf8effca05b5a468ef04db28b7e9eaf3559c4

This reference is generated from maintained source without imports or execution. Assigned values are intentionally omitted. Runtime-dependent types are explicit; the enclosing docstring defines the behavioral contract. See [architecture](../ARCHITECTURE_QUALITY.md) for manually reviewed responsibility and dependency decisions.

## Classes and callables

### test_default_view_creates_independent_runtime_clients

Verify default view creates independent runtime clients.

Kind: callable. Declared return: Not declared / class. Source line: 10.

### test_default_view_creates_independent_runtime_clients.runtime

Provide runtime for the enclosing trusted test fixture.

Kind: callable. Declared return: Not declared / class. Source line: 26.

### test_gui_sessions_start_local_despite_legacy_remote_environment

Legacy configuration cannot activate an external GUI model without consent.

Kind: callable. Declared return: Not declared / class. Source line: 50.

### test_gui_sessions_start_local_despite_legacy_remote_environment.create

Capture the provider settings handed to each actual session factory.

Kind: callable. Declared return: Not declared / class. Source line: 70.

## Variables and parameters

| Scope | Name | Role and meaning | Type | Lifetime | Writes |
| --- | --- | --- | --- | --- | --- |
| module | sys | Imported dependency for sys in module; use the enclosing contract and type below. | Module or imported public symbol | Module/process lifetime | 3 |
| module | ModuleType | Imported dependency for ModuleType in module; use the enclosing contract and type below. | Module or imported public symbol | Module/process lifetime | 4 |
| module | SimpleNamespace | Imported dependency for SimpleNamespace in module; use the enclosing contract and type below. | Module or imported public symbol | Module/process lifetime | 4 |
| module | uuid4 | Imported dependency for uuid4 in module; use the enclosing contract and type below. | Module or imported public symbol | Module/process lifetime | 5 |
| module | bootstrap | Imported dependency for bootstrap in module; use the enclosing contract and type below. | Module or imported public symbol | Module/process lifetime | 7 |
| test_default_view_creates_independent_runtime_clients | monkeypatch | Parameter for monkeypatch in test_default_view_creates_independent_runtime_clients; use the enclosing contract and type below. | Not explicitly annotated | Enclosing invocation or class/instance lifetime | 10 |
| test_default_view_creates_independent_runtime_clients | tmp_path | Parameter for tmp path in test_default_view_creates_independent_runtime_clients; use the enclosing contract and type below. | Not explicitly annotated | Enclosing invocation or class/instance lifetime | 10 |
| test_default_view_creates_independent_runtime_clients | Settings | Imported dependency for Settings in test_default_view_creates_independent_runtime_clients; use the enclosing contract and type below. | Module or imported public symbol | Enclosing invocation or class/instance lifetime | 13 |
| test_default_view_creates_independent_runtime_clients | shared | Local binding for shared in test_default_view_creates_independent_runtime_clients; use the enclosing contract and type below. | Return type of SimpleNamespace; see its callable contract | Enclosing invocation or class/instance lifetime | 15 |
| test_default_view_creates_independent_runtime_clients | legacy | Local binding for legacy in test_default_view_creates_independent_runtime_clients; use the enclosing contract and type below. | Return type of SimpleNamespace; see its callable contract | Enclosing invocation or class/instance lifetime | 16 |
| test_default_view_creates_independent_runtime_clients.lambda_19 | query | Original user request or a trusted test query; avoid payload logging by default. | Defined by the enclosing callback contract | Enclosing invocation or class/instance lifetime | 19 |
| test_default_view_creates_independent_runtime_clients.runtime | settings | Immutable startup configuration; constructing it does not start external services. | Not explicitly annotated | Enclosing invocation or class/instance lifetime | 26 |
| test_default_view_creates_independent_runtime_clients.runtime | kwargs | Bounded JSON keyword arguments; no executable objects are accepted. | Not explicitly annotated | Enclosing invocation or class/instance lifetime | 26 |
| test_default_view_creates_independent_runtime_clients.runtime | client | Local binding for client in test_default_view_creates_independent_runtime_clients.runtime; use the enclosing contract and type below. | Runtime-dependent; see the enclosing callable contract | Enclosing invocation or class/instance lifetime | 28 |
| test_default_view_creates_independent_runtime_clients.runtime.lambda_31 | query | Original user request or a trusted test query; avoid payload logging by default. | Defined by the enclosing callback contract | Enclosing invocation or class/instance lifetime | 31 |
| test_default_view_creates_independent_runtime_clients | gradio | Local binding for gradio in test_default_view_creates_independent_runtime_clients; use the enclosing contract and type below. | Return type of ModuleType; see its callable contract | Enclosing invocation or class/instance lifetime | 37 |
| test_default_view_creates_independent_runtime_clients | gradio.update | Attribute for gradio.update in test_default_view_creates_independent_runtime_clients; use the enclosing contract and type below. | Runtime-dependent; see the enclosing callable contract | Enclosing invocation or class/instance lifetime | 38 |
| test_default_view_creates_independent_runtime_clients.lambda_40 | registry | Callback parameter for registry in test_default_view_creates_independent_runtime_clients.lambda_40; use the enclosing contract and type below. | Defined by the enclosing callback contract | Enclosing invocation or class/instance lifetime | 40 |
| test_default_view_creates_independent_runtime_clients | _ | Local binding for  in test_default_view_creates_independent_runtime_clients; use the enclosing contract and type below. | Return type of get_default_ui; see its callable contract | Enclosing invocation or class/instance lifetime | 42 |
| test_default_view_creates_independent_runtime_clients | registry | Local binding for registry in test_default_view_creates_independent_runtime_clients; use the enclosing contract and type below. | Return type of get_default_ui; see its callable contract | Enclosing invocation or class/instance lifetime | 42 |
| test_default_view_creates_independent_runtime_clients | first | Local binding for first in test_default_view_creates_independent_runtime_clients; use the enclosing contract and type below. | tuple | Enclosing invocation or class/instance lifetime | 43 |
| test_default_view_creates_independent_runtime_clients | second | Local binding for second in test_default_view_creates_independent_runtime_clients; use the enclosing contract and type below. | tuple | Enclosing invocation or class/instance lifetime | 43 |
| test_gui_sessions_start_local_despite_legacy_remote_environment | monkeypatch | Parameter for monkeypatch in test_gui_sessions_start_local_despite_legacy_remote_environment; use the enclosing contract and type below. | Not explicitly annotated | Enclosing invocation or class/instance lifetime | 50 |
| test_gui_sessions_start_local_despite_legacy_remote_environment | tmp_path | Parameter for tmp path in test_gui_sessions_start_local_despite_legacy_remote_environment; use the enclosing contract and type below. | Not explicitly annotated | Enclosing invocation or class/instance lifetime | 50 |
| test_gui_sessions_start_local_despite_legacy_remote_environment | Settings | Imported dependency for Settings in test_gui_sessions_start_local_despite_legacy_remote_environment; use the enclosing contract and type below. | Module or imported public symbol | Enclosing invocation or class/instance lifetime | 52 |
| test_gui_sessions_start_local_despite_legacy_remote_environment | settings | Immutable startup configuration; constructing it does not start external services. | Return type of Settings; see its callable contract | Enclosing invocation or class/instance lifetime | 55 |
| test_gui_sessions_start_local_despite_legacy_remote_environment | legacy | Local binding for legacy in test_gui_sessions_start_local_despite_legacy_remote_environment; use the enclosing contract and type below. | Return type of SimpleNamespace; see its callable contract | Enclosing invocation or class/instance lifetime | 61 |
| test_gui_sessions_start_local_despite_legacy_remote_environment.lambda_64 | query | Original user request or a trusted test query; avoid payload logging by default. | Defined by the enclosing callback contract | Enclosing invocation or class/instance lifetime | 64 |
| test_gui_sessions_start_local_despite_legacy_remote_environment | calls | Local binding for calls in test_gui_sessions_start_local_despite_legacy_remote_environment; use the enclosing contract and type below. | list | Enclosing invocation or class/instance lifetime | 68 |
| test_gui_sessions_start_local_despite_legacy_remote_environment.create | settings | Immutable startup configuration; constructing it does not start external services. | Not explicitly annotated | Enclosing invocation or class/instance lifetime | 70 |
| test_gui_sessions_start_local_despite_legacy_remote_environment.create | kwargs | Bounded JSON keyword arguments; no executable objects are accepted. | Not explicitly annotated | Enclosing invocation or class/instance lifetime | 70 |
| test_gui_sessions_start_local_despite_legacy_remote_environment.create.lambda_75 | query | Original user request or a trusted test query; avoid payload logging by default. | Defined by the enclosing callback contract | Enclosing invocation or class/instance lifetime | 75 |
| test_gui_sessions_start_local_despite_legacy_remote_environment | gradio | Local binding for gradio in test_gui_sessions_start_local_despite_legacy_remote_environment; use the enclosing contract and type below. | Return type of ModuleType; see its callable contract | Enclosing invocation or class/instance lifetime | 82 |
| test_gui_sessions_start_local_despite_legacy_remote_environment | gradio.update | Attribute for gradio.update in test_gui_sessions_start_local_despite_legacy_remote_environment; use the enclosing contract and type below. | Runtime-dependent; see the enclosing callable contract | Enclosing invocation or class/instance lifetime | 83 |
| test_gui_sessions_start_local_despite_legacy_remote_environment.lambda_85 | registry | Callback parameter for registry in test_gui_sessions_start_local_despite_legacy_remote_environment.lambda_85; use the enclosing contract and type below. | Defined by the enclosing callback contract | Enclosing invocation or class/instance lifetime | 85 |
| test_gui_sessions_start_local_despite_legacy_remote_environment | _ | Local binding for  in test_gui_sessions_start_local_despite_legacy_remote_environment; use the enclosing contract and type below. | Return type of get_default_ui; see its callable contract | Enclosing invocation or class/instance lifetime | 87 |
| test_gui_sessions_start_local_despite_legacy_remote_environment | registry | Local binding for registry in test_gui_sessions_start_local_despite_legacy_remote_environment; use the enclosing contract and type below. | Return type of get_default_ui; see its callable contract | Enclosing invocation or class/instance lifetime | 87 |
