# Reference for src/agentix/credentials.py

Windows Credential Manager adapter and host-output secret redaction.

Generic credentials are protected by the Windows user boundary, not against
malware running as that same user. No secret is written into project files or
process environment variables. Saved targets persist until explicit deletion; ephemeral targets are removed on cleanup.

Source fingerprint: 31e5d34f50a2eb83c7396cf7bb259a72912c1e17f6d17e920eeca59d5bf5405c

This reference is generated from maintained source without imports or execution. Assigned values are intentionally omitted. Runtime-dependent types are explicit; the enclosing docstring defines the behavioral contract. See [architecture](../ARCHITECTURE_QUALITY.md) for manually reviewed responsibility and dependency decisions.

## Classes and callables

### redact

Replace registered API key values before publishing host output.

Kind: callable. Declared return: str. Source line: 22.

### register_secret

Register a bounded key for process-lifetime redaction, or deny capacity.

Kind: callable. Declared return: None. Source line: 30.

### SecretFilter

Redact formatted vendor log messages and exception text at host handlers.

Kind: class. Declared return: Not declared / class. Source line: 44.

### SecretFilter.filter

Normalize messages without exposing original formatting arguments.

Kind: callable. Declared return: bool. Source line: 47.

### _Credential

Native CREDENTIALW layout; blob bytes are copied then freed by Windows.

Kind: class. Declared return: Not declared / class. Source line: 57.

### WindowsCredentialVault

Generic user-and-machine persistent credentials addressed by opaque owned targets.

Kind: class. Declared return: Not declared / class. Source line: 76.

### WindowsCredentialVault.__init__

Load user-level Windows APIs; fail closed on unsupported systems.

Kind: callable. Declared return: None. Source line: 79.

### WindowsCredentialVault._target

Constrain every access to the application namespace.

Kind: callable. Declared return: str. Source line: 98.

### WindowsCredentialVault.write

Store a key without filesystem or environment persistence.

Kind: callable. Declared return: None. Source line: 108.

### WindowsCredentialVault.read

Read an owned key; free the native allocation even on decoding failure.

Kind: callable. Declared return: str. Source line: 127.

### WindowsCredentialVault.delete

Remove one owned target; missing targets are already compliant.

Kind: callable. Declared return: None. Source line: 142.

### DeferredCredentialVault

Defer native credential construction until a credential operation is needed.

Local metadata operations never call the factory. SavedProfiles serializes its
writes; the lock also protects lazy construction for concurrent read callers.

Kind: class. Declared return: Not declared / class. Source line: 149.

### DeferredCredentialVault.__init__

Retain the injected factory without accessing the Windows API.

Kind: callable. Declared return: None. Source line: 156.

### DeferredCredentialVault._backend

Create the native boundary once, replacing unsafe initialization errors.

Kind: callable. Declared return: Any. Source line: 162.

### DeferredCredentialVault.write

Write only an explicitly requested credential through the lazy backend.

Kind: callable. Declared return: None. Source line: 172.

### DeferredCredentialVault.read

Read only the selected opaque reference through the lazy backend.

Kind: callable. Declared return: str. Source line: 176.

### DeferredCredentialVault.delete

Delete only an explicitly owned reference through the lazy backend.

Kind: callable. Declared return: None. Source line: 180.

## Variables and parameters

| Scope | Name | Role and meaning | Type | Lifetime | Writes |
| --- | --- | --- | --- | --- | --- |
| module | ctypes | Imported dependency for ctypes in module; use the enclosing contract and type below. | Module or imported public symbol | Module/process lifetime | 8 |
| module | logging | Imported dependency for logging in module; use the enclosing contract and type below. | Module or imported public symbol | Module/process lifetime | 9 |
| module | os | Imported dependency for os in module; use the enclosing contract and type below. | Module or imported public symbol | Module/process lifetime | 10 |
| module | threading | Imported dependency for threading in module; use the enclosing contract and type below. | Module or imported public symbol | Module/process lifetime | 11 |
| module | Callable | Imported dependency for Callable in module; use the enclosing contract and type below. | Module or imported public symbol | Module/process lifetime | 12 |
| module | wintypes | Imported dependency for wintypes in module; use the enclosing contract and type below. | Module or imported public symbol | Module/process lifetime | 13 |
| module | Any | Imported dependency for Any in module; use the enclosing contract and type below. | Module or imported public symbol | Module/process lifetime | 14 |
| module | ProfileError | Imported dependency for ProfileError in module; use the enclosing contract and type below. | Module or imported public symbol | Module/process lifetime | 16 |
| module | _values | Typed binding for values in module; use the enclosing contract and type below. | set[str] | Module/process lifetime | 18 |
| module | _lock | Module binding for lock in module; use the enclosing contract and type below. | Return type of RLock; see its callable contract | Module/process lifetime | 19 |
| redact | text | Parameter for text in redact; use the enclosing contract and type below. | str | Enclosing invocation or class/instance lifetime | 22, 26 |
| redact | value | Value at the current validation/rendering boundary; apply the enclosing contract. | Element of the declared iterable | Enclosing invocation or class/instance lifetime | 25 |
| register_secret | value | Value at the current validation/rendering boundary; apply the enclosing contract. | str | Enclosing invocation or class/instance lifetime | 30 |
| register_secret.comprehension_35 | c | Comprehension item for c in register_secret.comprehension_35; use the enclosing contract and type below. | Element of the declared iterable | This comprehension only; does not leak into its enclosing scope | 35 |
| SecretFilter.filter | self | Owning instance; its attributes retain state for the instance lifetime. | Not explicitly annotated | Enclosing invocation or class/instance lifetime | 47 |
| SecretFilter.filter | record | Parameter for record in SecretFilter.filter; use the enclosing contract and type below. | logging.LogRecord | Enclosing invocation or class/instance lifetime | 47 |
| SecretFilter.filter | record.msg | Attribute for record.msg in SecretFilter.filter; use the enclosing contract and type below. | Return type of redact; see its callable contract | Enclosing invocation or class/instance lifetime | 49 |
| SecretFilter.filter | record.args | Attribute for record.args in SecretFilter.filter; use the enclosing contract and type below. | tuple | Enclosing invocation or class/instance lifetime | 50 |
| SecretFilter.filter | record.exc_text | Attribute for record.exc text in SecretFilter.filter; use the enclosing contract and type below. | Return type of redact; see its callable contract | Enclosing invocation or class/instance lifetime | 52 |
| SecretFilter.filter | record.exc_info | Attribute for record.exc info in SecretFilter.filter; use the enclosing contract and type below. | NoneType | Enclosing invocation or class/instance lifetime | 53 |
| _Credential | _fields_ | Local binding for fields in _Credential; use the enclosing contract and type below. | list | Enclosing invocation or class/instance lifetime | 60 |
| WindowsCredentialVault.__init__ | self | Owning instance; its attributes retain state for the instance lifetime. | Not explicitly annotated | Enclosing invocation or class/instance lifetime | 79 |
| WindowsCredentialVault.__init__ | self.api | Attribute for api in WindowsCredentialVault.__init__; use the enclosing contract and type below. | Return type of WinDLL; see its callable contract | Enclosing invocation or class/instance lifetime | 83 |
| WindowsCredentialVault.__init__ | self.api.CredWriteW.argtypes | Attribute for api.CredWriteW.argtypes in WindowsCredentialVault.__init__; use the enclosing contract and type below. | list | Enclosing invocation or class/instance lifetime | 84 |
| WindowsCredentialVault.__init__ | self.api.CredWriteW.restype | Attribute for api.CredWriteW.restype in WindowsCredentialVault.__init__; use the enclosing contract and type below. | Runtime-dependent; see the enclosing callable contract | Enclosing invocation or class/instance lifetime | 85 |
| WindowsCredentialVault.__init__ | self.api.CredReadW.argtypes | Attribute for api.CredReadW.argtypes in WindowsCredentialVault.__init__; use the enclosing contract and type below. | list | Enclosing invocation or class/instance lifetime | 86 |
| WindowsCredentialVault.__init__ | self.api.CredReadW.restype | Attribute for api.CredReadW.restype in WindowsCredentialVault.__init__; use the enclosing contract and type below. | Runtime-dependent; see the enclosing callable contract | Enclosing invocation or class/instance lifetime | 92 |
| WindowsCredentialVault.__init__ | self.api.CredDeleteW.argtypes | Attribute for api.CredDeleteW.argtypes in WindowsCredentialVault.__init__; use the enclosing contract and type below. | list | Enclosing invocation or class/instance lifetime | 93 |
| WindowsCredentialVault.__init__ | self.api.CredDeleteW.restype | Attribute for api.CredDeleteW.restype in WindowsCredentialVault.__init__; use the enclosing contract and type below. | Runtime-dependent; see the enclosing callable contract | Enclosing invocation or class/instance lifetime | 94 |
| WindowsCredentialVault.__init__ | self.api.CredFree.argtypes | Attribute for api.CredFree.argtypes in WindowsCredentialVault.__init__; use the enclosing contract and type below. | list | Enclosing invocation or class/instance lifetime | 95 |
| WindowsCredentialVault._target | reference | Parameter for reference in WindowsCredentialVault._target; use the enclosing contract and type below. | str | Enclosing invocation or class/instance lifetime | 98 |
| WindowsCredentialVault._target | re | Imported dependency for re in WindowsCredentialVault._target; use the enclosing contract and type below. | Module or imported public symbol | Enclosing invocation or class/instance lifetime | 100 |
| WindowsCredentialVault.write | self | Owning instance; its attributes retain state for the instance lifetime. | Not explicitly annotated | Enclosing invocation or class/instance lifetime | 108 |
| WindowsCredentialVault.write | reference | Parameter for reference in WindowsCredentialVault.write; use the enclosing contract and type below. | str | Enclosing invocation or class/instance lifetime | 108, 110 |
| WindowsCredentialVault.write | key | Parameter for key in WindowsCredentialVault.write; use the enclosing contract and type below. | str | Enclosing invocation or class/instance lifetime | 108 |
| WindowsCredentialVault.write | blob | Local binding for blob in WindowsCredentialVault.write; use the enclosing contract and type below. | Return type of encode; see its callable contract | Enclosing invocation or class/instance lifetime | 112 |
| WindowsCredentialVault.write | buffer | Local binding for buffer in WindowsCredentialVault.write; use the enclosing contract and type below. | Return type of from_buffer_copy; see its callable contract | Enclosing invocation or class/instance lifetime | 115 |
| WindowsCredentialVault.write | credential | Local binding for credential in WindowsCredentialVault.write; use the enclosing contract and type below. | Return type of _Credential; see its callable contract | Enclosing invocation or class/instance lifetime | 116 |
| WindowsCredentialVault.read | self | Owning instance; its attributes retain state for the instance lifetime. | Not explicitly annotated | Enclosing invocation or class/instance lifetime | 127 |
| WindowsCredentialVault.read | reference | Parameter for reference in WindowsCredentialVault.read; use the enclosing contract and type below. | str | Enclosing invocation or class/instance lifetime | 127, 129 |
| WindowsCredentialVault.read | pointer | Local binding for pointer in WindowsCredentialVault.read; use the enclosing contract and type below. | Return type of callable; see its callable contract | Enclosing invocation or class/instance lifetime | 130 |
| WindowsCredentialVault.read | value | Value at the current validation/rendering boundary; apply the enclosing contract. | Return type of decode; see its callable contract | Enclosing invocation or class/instance lifetime | 134 |
| WindowsCredentialVault.delete | self | Owning instance; its attributes retain state for the instance lifetime. | Not explicitly annotated | Enclosing invocation or class/instance lifetime | 142 |
| WindowsCredentialVault.delete | reference | Parameter for reference in WindowsCredentialVault.delete; use the enclosing contract and type below. | str | Enclosing invocation or class/instance lifetime | 142, 144 |
| DeferredCredentialVault.__init__ | self | Owning instance; its attributes retain state for the instance lifetime. | Not explicitly annotated | Enclosing invocation or class/instance lifetime | 156 |
| DeferredCredentialVault.__init__ | factory | Parameter for factory in DeferredCredentialVault.__init__; use the enclosing contract and type below. | Callable[[], Any] | Enclosing invocation or class/instance lifetime | 156 |
| DeferredCredentialVault.__init__ | self.factory | Attribute for factory in DeferredCredentialVault.__init__; use the enclosing contract and type below. | Runtime-dependent; see the enclosing callable contract | Enclosing invocation or class/instance lifetime | 158 |
| DeferredCredentialVault.__init__ | self._instance | Attribute for instance in DeferredCredentialVault.__init__; use the enclosing contract and type below. | NoneType | Enclosing invocation or class/instance lifetime | 159 |
| DeferredCredentialVault.__init__ | self._instance_lock | Attribute for instance lock in DeferredCredentialVault.__init__; use the enclosing contract and type below. | Return type of RLock; see its callable contract | Enclosing invocation or class/instance lifetime | 160 |
| DeferredCredentialVault._backend | self | Owning instance; its attributes retain state for the instance lifetime. | Not explicitly annotated | Enclosing invocation or class/instance lifetime | 162 |
| DeferredCredentialVault._backend | self._instance | Attribute for instance in DeferredCredentialVault._backend; use the enclosing contract and type below. | Return type of factory; see its callable contract | Enclosing invocation or class/instance lifetime | 167 |
| DeferredCredentialVault.write | self | Owning instance; its attributes retain state for the instance lifetime. | Not explicitly annotated | Enclosing invocation or class/instance lifetime | 172 |
| DeferredCredentialVault.write | reference | Parameter for reference in DeferredCredentialVault.write; use the enclosing contract and type below. | str | Enclosing invocation or class/instance lifetime | 172 |
| DeferredCredentialVault.write | key | Parameter for key in DeferredCredentialVault.write; use the enclosing contract and type below. | str | Enclosing invocation or class/instance lifetime | 172 |
| DeferredCredentialVault.read | self | Owning instance; its attributes retain state for the instance lifetime. | Not explicitly annotated | Enclosing invocation or class/instance lifetime | 176 |
| DeferredCredentialVault.read | reference | Parameter for reference in DeferredCredentialVault.read; use the enclosing contract and type below. | str | Enclosing invocation or class/instance lifetime | 176 |
| DeferredCredentialVault.delete | self | Owning instance; its attributes retain state for the instance lifetime. | Not explicitly annotated | Enclosing invocation or class/instance lifetime | 180 |
| DeferredCredentialVault.delete | reference | Parameter for reference in DeferredCredentialVault.delete; use the enclosing contract and type below. | str | Enclosing invocation or class/instance lifetime | 180 |
