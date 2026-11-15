# Reference for src/agentix/models/profile_errors.py

Closed, payload-free profile errors suitable for user-facing diagnostics.

Source fingerprint: 0b8fd27b948b007064cfcdebc9143ab07a4a51fd7059b96de27b6a2501064b0a

This reference is generated from maintained source without imports or execution. Assigned values are intentionally omitted. Runtime-dependent types are explicit; the enclosing docstring defines the behavioral contract. See [architecture](../ARCHITECTURE_QUALITY.md) for manually reviewed responsibility and dependency decisions.

## Classes and callables

### ProfileError

Carry only a closed reason code and optional numeric Windows status.

No caller-supplied message, key, URL, path or vendor exception body is stored.
The UI may display this exception's text; other exceptions remain private.

Kind: class. Declared return: Not declared / class. Source line: 27.

### ProfileError.__init__

Validate fixed diagnostic fields and construct a safe public message.

Kind: callable. Declared return: None. Source line: 34.

## Variables and parameters

| Scope | Name | Role and meaning | Type | Lifetime | Writes |
| --- | --- | --- | --- | --- | --- |
| module | MESSAGES | Module binding for MESSAGES in module; use the enclosing contract and type below. | dict | Module/process lifetime | 3 |
| module | MAX_WINDOWS_ERROR_CODE | Module binding for MAX WINDOWS ERROR CODE in module; use the enclosing contract and type below. | int | Module/process lifetime | 24 |
| ProfileError.__init__ | self | Owning instance; its attributes retain state for the instance lifetime. | Not explicitly annotated | Enclosing invocation or class/instance lifetime | 34 |
| ProfileError.__init__ | code | Source snapshot passed through approval, syntax checks and isolated staging. | str | Enclosing invocation or class/instance lifetime | 34 |
| ProfileError.__init__ | system_code | Parameter for system code in ProfileError.__init__; use the enclosing contract and type below. | int &#124; None | Enclosing invocation or class/instance lifetime | 34 |
| ProfileError.__init__ | self.code | Source snapshot passed through approval, syntax checks and isolated staging. | Runtime-dependent; see the enclosing callable contract | Enclosing invocation or class/instance lifetime | 38 |
| ProfileError.__init__ | self.system_code | Attribute for system code in ProfileError.__init__; use the enclosing contract and type below. | Runtime-dependent; see the enclosing callable contract | Enclosing invocation or class/instance lifetime | 39 |
| ProfileError.__init__ | message | Local binding for message in ProfileError.__init__; use the enclosing contract and type below. | Runtime-dependent; see the enclosing callable contract | Enclosing invocation or class/instance lifetime | 44, 46 |
