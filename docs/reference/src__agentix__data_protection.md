# Reference for src/agentix/data_protection.py

Windows user-scoped DPAPI protection with explicit machine-bound entropy.

No LOCAL_MACHINE flag is used. Native buffers are freed with LocalFree. This
protects persistent authorization records, not against same-user host malware.

Source fingerprint: 8bab855b8afe127968d0f61a354e05a20bd150eb33abd9fcd43bc5c81b5b1064

This reference is generated from maintained source without imports or execution. Assigned values are intentionally omitted. Runtime-dependent types are explicit; the enclosing docstring defines the behavioral contract. See [architecture](../ARCHITECTURE_QUALITY.md) for manually reviewed responsibility and dependency decisions.

## Classes and callables

### _Blob

Native DATA_BLOB; Python owns input buffers and Windows owns output.

Kind: class. Declared return: Not declared / class. Source line: 13.

### WindowsDataProtection

Seal bounded data for the current Windows user and explicit machine ID.

Kind: class. Declared return: Not declared / class. Source line: 19.

### WindowsDataProtection._transform

Call noninteractive DPAPI and free the returned allocation on every exit.

Parameters: bounded input bytes and operation direction. Returns copied
output bytes. Raises OSError on unsupported/blocked/corrupt protection.
Native APIs and the read-only machine identifier are loaded only on use.

Kind: callable. Declared return: bytes. Source line: 22.

### WindowsDataProtection.seal

Encrypt data plus an internal version/digest envelope; return opaque bytes.

Kind: callable. Declared return: bytes. Source line: 73.

### WindowsDataProtection.unseal

Decrypt and verify the envelope; malformed or modified records fail closed.

Kind: callable. Declared return: bytes. Source line: 79.

## Variables and parameters

| Scope | Name | Role and meaning | Type | Lifetime | Writes |
| --- | --- | --- | --- | --- | --- |
| module | ctypes | Imported dependency for ctypes in module; use the enclosing contract and type below. | Module or imported public symbol | Module/process lifetime | 7 |
| module | hashlib | Imported dependency for hashlib in module; use the enclosing contract and type below. | Module or imported public symbol | Module/process lifetime | 8 |
| module | os | Imported dependency for os in module; use the enclosing contract and type below. | Module or imported public symbol | Module/process lifetime | 9 |
| module | wintypes | Imported dependency for wintypes in module; use the enclosing contract and type below. | Module or imported public symbol | Module/process lifetime | 10 |
| _Blob | _fields_ | Local binding for fields in _Blob; use the enclosing contract and type below. | list | Enclosing invocation or class/instance lifetime | 16 |
| WindowsDataProtection._transform | self | Owning instance; its attributes retain state for the instance lifetime. | Not explicitly annotated | Enclosing invocation or class/instance lifetime | 22 |
| WindowsDataProtection._transform | data | Parameter for data in WindowsDataProtection._transform; use the enclosing contract and type below. | bytes | Enclosing invocation or class/instance lifetime | 22 |
| WindowsDataProtection._transform | decrypt | Parameter for decrypt in WindowsDataProtection._transform; use the enclosing contract and type below. | bool | Enclosing invocation or class/instance lifetime | 22 |
| WindowsDataProtection._transform | winreg | Imported dependency for winreg in WindowsDataProtection._transform; use the enclosing contract and type below. | Module or imported public symbol | Enclosing invocation or class/instance lifetime | 31 |
| WindowsDataProtection._transform | key | Managed resource for key in WindowsDataProtection._transform; use the enclosing contract and type below. | Return type of OpenKey; see its callable contract | Context-manager block; exit invokes its cleanup protocol | 33 |
| WindowsDataProtection._transform | machine | Local binding for machine in WindowsDataProtection._transform; use the enclosing contract and type below. | Runtime-dependent; see the enclosing callable contract | Enclosing invocation or class/instance lifetime | 39 |
| WindowsDataProtection._transform | entropy | Local binding for entropy in WindowsDataProtection._transform; use the enclosing contract and type below. | Return type of digest; see its callable contract | Enclosing invocation or class/instance lifetime | 40 |
| WindowsDataProtection._transform | source_buffer | Local binding for source buffer in WindowsDataProtection._transform; use the enclosing contract and type below. | Return type of from_buffer_copy; see its callable contract | Enclosing invocation or class/instance lifetime | 41 |
| WindowsDataProtection._transform | entropy_buffer | Local binding for entropy buffer in WindowsDataProtection._transform; use the enclosing contract and type below. | Return type of from_buffer_copy; see its callable contract | Enclosing invocation or class/instance lifetime | 42 |
| WindowsDataProtection._transform | source | Explicit source document or source-code text; never imported for reference generation. | Return type of _Blob; see its callable contract | Enclosing invocation or class/instance lifetime | 43 |
| WindowsDataProtection._transform | extra | Local binding for extra in WindowsDataProtection._transform; use the enclosing contract and type below. | Return type of _Blob; see its callable contract | Enclosing invocation or class/instance lifetime | 44 |
| WindowsDataProtection._transform | output | Local binding for output in WindowsDataProtection._transform; use the enclosing contract and type below. | Return type of _Blob; see its callable contract | Enclosing invocation or class/instance lifetime | 45 |
| WindowsDataProtection._transform | api | Local binding for api in WindowsDataProtection._transform; use the enclosing contract and type below. | Return type of WinDLL; see its callable contract | Enclosing invocation or class/instance lifetime | 46 |
| WindowsDataProtection._transform | kernel | Local binding for kernel in WindowsDataProtection._transform; use the enclosing contract and type below. | Return type of WinDLL; see its callable contract | Enclosing invocation or class/instance lifetime | 47 |
| WindowsDataProtection._transform | function | Local binding for function in WindowsDataProtection._transform; use the enclosing contract and type below. | Runtime-dependent; see the enclosing callable contract | Enclosing invocation or class/instance lifetime | 48 |
| WindowsDataProtection._transform | function.argtypes | Attribute for function.argtypes in WindowsDataProtection._transform; use the enclosing contract and type below. | list | Enclosing invocation or class/instance lifetime | 49 |
| WindowsDataProtection._transform | function.restype | Attribute for function.restype in WindowsDataProtection._transform; use the enclosing contract and type below. | Runtime-dependent; see the enclosing callable contract | Enclosing invocation or class/instance lifetime | 58 |
| WindowsDataProtection._transform | kernel.LocalFree.argtypes | Attribute for kernel.LocalFree.argtypes in WindowsDataProtection._transform; use the enclosing contract and type below. | list | Enclosing invocation or class/instance lifetime | 59 |
| WindowsDataProtection._transform | kernel.LocalFree.restype | Attribute for kernel.LocalFree.restype in WindowsDataProtection._transform; use the enclosing contract and type below. | Runtime-dependent; see the enclosing callable contract | Enclosing invocation or class/instance lifetime | 60 |
| WindowsDataProtection.seal | self | Owning instance; its attributes retain state for the instance lifetime. | Not explicitly annotated | Enclosing invocation or class/instance lifetime | 73 |
| WindowsDataProtection.seal | data | Parameter for data in WindowsDataProtection.seal; use the enclosing contract and type below. | bytes | Enclosing invocation or class/instance lifetime | 73 |
| WindowsDataProtection.unseal | self | Owning instance; its attributes retain state for the instance lifetime. | Not explicitly annotated | Enclosing invocation or class/instance lifetime | 79 |
| WindowsDataProtection.unseal | data | Parameter for data in WindowsDataProtection.unseal; use the enclosing contract and type below. | bytes | Enclosing invocation or class/instance lifetime | 79 |
| WindowsDataProtection.unseal | hmac | Imported dependency for hmac in WindowsDataProtection.unseal; use the enclosing contract and type below. | Module or imported public symbol | Enclosing invocation or class/instance lifetime | 81 |
| WindowsDataProtection.unseal | plain | Local binding for plain in WindowsDataProtection.unseal; use the enclosing contract and type below. | Return type of _transform; see its callable contract | Enclosing invocation or class/instance lifetime | 83 |
| WindowsDataProtection.unseal | prefix | Local binding for prefix in WindowsDataProtection.unseal; use the enclosing contract and type below. | bytes | Enclosing invocation or class/instance lifetime | 84 |
| WindowsDataProtection.unseal | offset | Local binding for offset in WindowsDataProtection.unseal; use the enclosing contract and type below. | Return type of len; see its callable contract | Enclosing invocation or class/instance lifetime | 85 |
