# Reference for src/agentix/profile_errors.py

Closed, payload-free profile errors suitable for user-facing diagnostics.

Source fingerprint: 74dc0c01372b5dc8c56a71cb75bdc16fdeb08bd56a43926669c5c5309a80637c

This reference is generated from maintained source without imports or execution. Assigned values are intentionally omitted. Runtime-dependent types are explicit; the enclosing docstring defines the behavioral contract. See [architecture](../ARCHITECTURE_QUALITY.md) for manually reviewed responsibility and dependency decisions.

## Classes and callables

### ProfileError

Carry only a closed reason code and optional numeric Windows status.

No caller-supplied message, key, URL, path or vendor exception body is stored.
The UI may display this exception's text; other exceptions remain private.

Kind: class. Declared return: Not declared / class. Source line: 23.

### ProfileError.__init__

Validate fixed diagnostic fields and construct a safe public message.

Kind: callable. Declared return: None. Source line: 30.

## Variables and parameters

| Scope | Name | Role and meaning | Type | Lifetime | Writes |
| --- | --- | --- | --- | --- | --- |
| module | MESSAGES | Module binding for MESSAGES in module; use the enclosing contract and type below. | dict | Module/process lifetime | 3 |
| ProfileError.__init__ | self | Owning instance; its attributes retain state for the instance lifetime. | Not explicitly annotated | Enclosing invocation or class/instance lifetime | 30 |
| ProfileError.__init__ | code | Source snapshot passed through approval, syntax checks and isolated staging. | str | Enclosing invocation or class/instance lifetime | 30 |
| ProfileError.__init__ | system_code | Parameter for system code in ProfileError.__init__; use the enclosing contract and type below. | int &#124; None | Enclosing invocation or class/instance lifetime | 30 |
| ProfileError.__init__ | self.code | Source snapshot passed through approval, syntax checks and isolated staging. | Runtime-dependent; see the enclosing callable contract | Enclosing invocation or class/instance lifetime | 34 |
| ProfileError.__init__ | self.system_code | Attribute for system code in ProfileError.__init__; use the enclosing contract and type below. | Runtime-dependent; see the enclosing callable contract | Enclosing invocation or class/instance lifetime | 35 |
| ProfileError.__init__ | message | Local binding for message in ProfileError.__init__; use the enclosing contract and type below. | Runtime-dependent; see the enclosing callable contract | Enclosing invocation or class/instance lifetime | 38, 40 |
