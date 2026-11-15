# Reference for src/agentix/controllers/sidebar.py

Shared sidebar model/profile backend, independent of tab rendering and Gradio.

Source fingerprint: be1206eb5009c7648cd351e9f6c5483349f68fac96f70e578bc6df64caa22088

This reference is generated from maintained source without imports or execution. Assigned values are intentionally omitted. Runtime-dependent types are explicit; the enclosing docstring defines the behavioral contract. See [architecture](../ARCHITECTURE_QUALITY.md) for manually reviewed responsibility and dependency decisions.

## Classes and callables

### SidebarBackend

Delegate owner-checked provider/profile operations to protected services.

Kind: class. Declared return: Not declared / class. Source line: 8.

### SidebarBackend.configure_model

Verify browser ownership; clear the key input on both success and failure.

Kind: callable. Declared return: tuple[str, str, str]. Source line: 11.

### SidebarBackend.model_menu

Dispatch fixed profile actions after owner checks; never return secrets.

Kind: callable. Declared return: tuple[Any, ...]. Source line: 29.

### SidebarBackend.refresh_models

Read only the local Ollama catalog after checking the browser owner.

Kind: callable. Declared return: tuple[list[str], str, str]. Source line: 50.

### SidebarBackend.inspect_generation_identity

Read a nonsecret local model digest without changing its trusted baseline.

Kind: callable. Declared return: tuple[str, str, str]. Source line: 69.

### SidebarBackend.reset_generation_identity

Explicitly replace a saved local profile's trusted generation baseline.

Kind: callable. Declared return: tuple[str, str]. Source line: 91.

## Variables and parameters

| Scope | Name | Role and meaning | Type | Lifetime | Writes |
| --- | --- | --- | --- | --- | --- |
| module | Any | Imported dependency for Any in module; use the enclosing contract and type below. | Module or imported public symbol | Module/process lifetime | 3 |
| module | SessionOwnerAccess | Imported dependency for SessionOwnerAccess in module; use the enclosing contract and type below. | Module or imported public symbol | Module/process lifetime | 5 |
| SidebarBackend.configure_model | self | Owning instance; its attributes retain state for the instance lifetime. | Not explicitly annotated | Enclosing invocation or class/instance lifetime | 12 |
| SidebarBackend.configure_model | provider | Parameter for provider in SidebarBackend.configure_model; use the enclosing contract and type below. | str | Enclosing invocation or class/instance lifetime | 13 |
| SidebarBackend.configure_model | model | Parameter for model in SidebarBackend.configure_model; use the enclosing contract and type below. | str | Enclosing invocation or class/instance lifetime | 14 |
| SidebarBackend.configure_model | endpoint | Parameter for endpoint in SidebarBackend.configure_model; use the enclosing contract and type below. | str | Enclosing invocation or class/instance lifetime | 15 |
| SidebarBackend.configure_model | key | Parameter for key in SidebarBackend.configure_model; use the enclosing contract and type below. | str | Enclosing invocation or class/instance lifetime | 16 |
| SidebarBackend.configure_model | consent | Parameter for consent in SidebarBackend.configure_model; use the enclosing contract and type below. | bool | Enclosing invocation or class/instance lifetime | 17 |
| SidebarBackend.configure_model | token | Parameter for token in SidebarBackend.configure_model; use the enclosing contract and type below. | str &#124; None | Enclosing invocation or class/instance lifetime | 18 |
| SidebarBackend.configure_model | request | Parameter for request in SidebarBackend.configure_model; use the enclosing contract and type below. | Any | Enclosing invocation or class/instance lifetime | 19 |
| SidebarBackend.configure_model | session | Local binding for session in SidebarBackend.configure_model; use the enclosing contract and type below. | Return type of _session; see its callable contract | Enclosing invocation or class/instance lifetime | 22 |
| SidebarBackend.configure_model | status | Local binding for status in SidebarBackend.configure_model; use the enclosing contract and type below. | Return type of configure_model; see its callable contract | Enclosing invocation or class/instance lifetime | 24, 26 |
| SidebarBackend.model_menu | self | Owning instance; its attributes retain state for the instance lifetime. | Not explicitly annotated | Enclosing invocation or class/instance lifetime | 30 |
| SidebarBackend.model_menu | action | Parameter for action in SidebarBackend.model_menu; use the enclosing contract and type below. | str | Enclosing invocation or class/instance lifetime | 31 |
| SidebarBackend.model_menu | identity | Explicit owner identity used by a session factory or fixture. | str | Enclosing invocation or class/instance lifetime | 32 |
| SidebarBackend.model_menu | name | Current identifier selected by parsing, lookup or dependency registration. | str | Enclosing invocation or class/instance lifetime | 33 |
| SidebarBackend.model_menu | provider | Parameter for provider in SidebarBackend.model_menu; use the enclosing contract and type below. | str | Enclosing invocation or class/instance lifetime | 34 |
| SidebarBackend.model_menu | model | Parameter for model in SidebarBackend.model_menu; use the enclosing contract and type below. | str | Enclosing invocation or class/instance lifetime | 35 |
| SidebarBackend.model_menu | endpoint | Parameter for endpoint in SidebarBackend.model_menu; use the enclosing contract and type below. | str | Enclosing invocation or class/instance lifetime | 36 |
| SidebarBackend.model_menu | key | Parameter for key in SidebarBackend.model_menu; use the enclosing contract and type below. | str | Enclosing invocation or class/instance lifetime | 37 |
| SidebarBackend.model_menu | token | Parameter for token in SidebarBackend.model_menu; use the enclosing contract and type below. | str &#124; None | Enclosing invocation or class/instance lifetime | 38 |
| SidebarBackend.model_menu | request | Parameter for request in SidebarBackend.model_menu; use the enclosing contract and type below. | Any | Enclosing invocation or class/instance lifetime | 39 |
| SidebarBackend.model_menu | session | Local binding for session in SidebarBackend.model_menu; use the enclosing contract and type below. | Return type of _session; see its callable contract | Enclosing invocation or class/instance lifetime | 42 |
| SidebarBackend.refresh_models | self | Owning instance; its attributes retain state for the instance lifetime. | Not explicitly annotated | Enclosing invocation or class/instance lifetime | 51 |
| SidebarBackend.refresh_models | endpoint | Parameter for endpoint in SidebarBackend.refresh_models; use the enclosing contract and type below. | str | Enclosing invocation or class/instance lifetime | 51 |
| SidebarBackend.refresh_models | token | Parameter for token in SidebarBackend.refresh_models; use the enclosing contract and type below. | str &#124; None | Enclosing invocation or class/instance lifetime | 51 |
| SidebarBackend.refresh_models | request | Parameter for request in SidebarBackend.refresh_models; use the enclosing contract and type below. | Any | Enclosing invocation or class/instance lifetime | 51 |
| SidebarBackend.refresh_models | installed_models | Imported dependency for installed models in SidebarBackend.refresh_models; use the enclosing contract and type below. | Module or imported public symbol | Enclosing invocation or class/instance lifetime | 54 |
| SidebarBackend.refresh_models | session | Local binding for session in SidebarBackend.refresh_models; use the enclosing contract and type below. | Return type of _session; see its callable contract | Enclosing invocation or class/instance lifetime | 56 |
| SidebarBackend.refresh_models | configuration | Local binding for configuration in SidebarBackend.refresh_models; use the enclosing contract and type below. | Runtime-dependent; see the enclosing callable contract | Enclosing invocation or class/instance lifetime | 58 |
| SidebarBackend.refresh_models | reader | Local binding for reader in SidebarBackend.refresh_models; use the enclosing contract and type below. | Runtime-dependent; see the enclosing callable contract | Enclosing invocation or class/instance lifetime | 59 |
| SidebarBackend.refresh_models | names | Local binding for names in SidebarBackend.refresh_models; use the enclosing contract and type below. | Return type of installed_models; see its callable contract | Enclosing invocation or class/instance lifetime | 60, 65 |
| SidebarBackend.refresh_models | status | Local binding for status in SidebarBackend.refresh_models; use the enclosing contract and type below. | str | Enclosing invocation or class/instance lifetime | 61, 63, 66 |
| SidebarBackend.inspect_generation_identity | self | Owning instance; its attributes retain state for the instance lifetime. | Not explicitly annotated | Enclosing invocation or class/instance lifetime | 70 |
| SidebarBackend.inspect_generation_identity | model | Parameter for model in SidebarBackend.inspect_generation_identity; use the enclosing contract and type below. | str | Enclosing invocation or class/instance lifetime | 70 |
| SidebarBackend.inspect_generation_identity | endpoint | Parameter for endpoint in SidebarBackend.inspect_generation_identity; use the enclosing contract and type below. | str | Enclosing invocation or class/instance lifetime | 70 |
| SidebarBackend.inspect_generation_identity | token | Parameter for token in SidebarBackend.inspect_generation_identity; use the enclosing contract and type below. | str &#124; None | Enclosing invocation or class/instance lifetime | 70 |
| SidebarBackend.inspect_generation_identity | request | Parameter for request in SidebarBackend.inspect_generation_identity; use the enclosing contract and type below. | Any | Enclosing invocation or class/instance lifetime | 70 |
| SidebarBackend.inspect_generation_identity | read_generation_identity | Imported dependency for read generation identity in SidebarBackend.inspect_generation_identity; use the enclosing contract and type below. | Module or imported public symbol | Enclosing invocation or class/instance lifetime | 73 |
| SidebarBackend.inspect_generation_identity | ModelProfile | Imported dependency for ModelProfile in SidebarBackend.inspect_generation_identity; use the enclosing contract and type below. | Module or imported public symbol | Enclosing invocation or class/instance lifetime | 74 |
| SidebarBackend.inspect_generation_identity | session | Local binding for session in SidebarBackend.inspect_generation_identity; use the enclosing contract and type below. | Return type of _session; see its callable contract | Enclosing invocation or class/instance lifetime | 76 |
| SidebarBackend.inspect_generation_identity | digest | Content fingerprint for change detection; not a substitute for human approval. | Return type of read_generation_identity; see its callable contract | Enclosing invocation or class/instance lifetime | 78 |
| SidebarBackend.reset_generation_identity | self | Owning instance; its attributes retain state for the instance lifetime. | Not explicitly annotated | Enclosing invocation or class/instance lifetime | 91 |
| SidebarBackend.reset_generation_identity | token | Parameter for token in SidebarBackend.reset_generation_identity; use the enclosing contract and type below. | str &#124; None | Enclosing invocation or class/instance lifetime | 91 |
| SidebarBackend.reset_generation_identity | request | Parameter for request in SidebarBackend.reset_generation_identity; use the enclosing contract and type below. | Any | Enclosing invocation or class/instance lifetime | 91 |
| SidebarBackend.reset_generation_identity | session | Local binding for session in SidebarBackend.reset_generation_identity; use the enclosing contract and type below. | Return type of _session; see its callable contract | Enclosing invocation or class/instance lifetime | 93 |
| SidebarBackend.reset_generation_identity | digest | Content fingerprint for change detection; not a substitute for human approval. | Return type of reset_generation_identity; see its callable contract | Enclosing invocation or class/instance lifetime | 95 |
