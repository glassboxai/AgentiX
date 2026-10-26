# Reference for src/agentix/approval_store.py

Protected durable approvals, separate from untrusted tool artifacts.

Records contain hashes and reviewed declarative data, never executable trust
markers supplied by a tool. Each atomic record is bound to root/tool/policy.
Concurrent revocation is observed on the next check, not instant cancellation.

Source fingerprint: e4cab1181b2c1df3672c21fa9d8bf8736c685e99c879fe8149f2fd168dac8f23

This reference is generated from maintained source without imports or execution. Assigned values are intentionally omitted. Runtime-dependent types are explicit; the enclosing docstring defines the behavioral contract. See [architecture](../ARCHITECTURE_QUALITY.md) for manually reviewed responsibility and dependency decisions.

## Classes and callables

### DataProtector

Injected authenticated Windows protection; tests use explicit doubles.

Kind: class. Declared return: Not declared / class. Source line: 23.

### DataProtector.seal

Protect bounded serialized authorization bytes or raise.

Kind: callable. Declared return: bytes. Source line: 26.

### DataProtector.unseal

Recover authenticated bytes or raise on failure.

Kind: callable. Declared return: bytes. Source line: 30.

### policy_fingerprint

Hash named maintained security sources; never traverse generated storage.

Kind: callable. Declared return: str. Source line: 35.

### ApprovalStore

Own per-tool protected records under a user-local directory outside tools.

Kind: class. Declared return: Not declared / class. Source line: 56.

### ApprovalStore.__init__

Bind canonical location and policy; construction performs no writes.

Kind: callable. Declared return: None. Source line: 59.

### ApprovalStore._path

Return only an opaque owned filename after validating the public tool ID.

Kind: callable. Declared return: Path. Source line: 70.

### ApprovalStore.save

Atomically persist a trusted host's successful reviewed execution grant.

Caller must already enforce human acceptance and actual successful isolated
execution. This is not a model-facing API. Errors propagate to the ledger.

Kind: callable. Declared return: None. Source line: 84.

### ApprovalStore.load

Return valid protected metadata only for exact current artifacts/policy.

Missing records grant nothing. Other failures revoke the owned record and
return nothing; diagnostic events never include source, cases or secrets.

Kind: callable. Declared return: dict[str, Any] | None. Source line: 129.

### ApprovalStore.revoke

Remove only this tool's owned record; missing records are already revoked.

Kind: callable. Declared return: None. Source line: 197.

### user_approval_store

Compose user-local durable Windows protection lazily, without native calls.

Kind: callable. Declared return: ApprovalStore. Source line: 202.

## Variables and parameters

| Scope | Name | Role and meaning | Type | Lifetime | Writes |
| --- | --- | --- | --- | --- | --- |
| module | hashlib | Imported dependency for hashlib in module; use the enclosing contract and type below. | Module or imported public symbol | Module/process lifetime | 8 |
| module | json | Imported dependency for json in module; use the enclosing contract and type below. | Module or imported public symbol | Module/process lifetime | 9 |
| module | logging | Imported dependency for logging in module; use the enclosing contract and type below. | Module or imported public symbol | Module/process lifetime | 10 |
| module | os | Imported dependency for os in module; use the enclosing contract and type below. | Module or imported public symbol | Module/process lifetime | 11 |
| module | re | Imported dependency for re in module; use the enclosing contract and type below. | Module or imported public symbol | Module/process lifetime | 12 |
| module | tempfile | Imported dependency for tempfile in module; use the enclosing contract and type below. | Module or imported public symbol | Module/process lifetime | 13 |
| module | Path | Imported dependency for Path in module; use the enclosing contract and type below. | Module or imported public symbol | Module/process lifetime | 14 |
| module | Any | Imported dependency for Any in module; use the enclosing contract and type below. | Module or imported public symbol | Module/process lifetime | 15 |
| module | Protocol | Imported dependency for Protocol in module; use the enclosing contract and type below. | Module or imported public symbol | Module/process lifetime | 15 |
| module | WindowsDataProtection | Imported dependency for WindowsDataProtection in module; use the enclosing contract and type below. | Module or imported public symbol | Module/process lifetime | 17 |
| module | log_event | Imported dependency for log event in module; use the enclosing contract and type below. | Module or imported public symbol | Module/process lifetime | 18 |
| module | logger | Module logger emitting bounded operation diagnostics rather than artifact bodies. | Return type of getLogger; see its callable contract | Module/process lifetime | 20 |
| DataProtector.seal | self | Owning instance; its attributes retain state for the instance lifetime. | Not explicitly annotated | Enclosing invocation or class/instance lifetime | 26 |
| DataProtector.seal | data | Parameter for data in DataProtector.seal; use the enclosing contract and type below. | bytes | Enclosing invocation or class/instance lifetime | 26 |
| DataProtector.unseal | self | Owning instance; its attributes retain state for the instance lifetime. | Not explicitly annotated | Enclosing invocation or class/instance lifetime | 30 |
| DataProtector.unseal | data | Parameter for data in DataProtector.unseal; use the enclosing contract and type below. | bytes | Enclosing invocation or class/instance lifetime | 30 |
| policy_fingerprint | root | Explicit root directory against which named paths are resolved. | Runtime-dependent; see the enclosing callable contract | Enclosing invocation or class/instance lifetime | 37 |
| policy_fingerprint | digest | Content fingerprint for change detection; not a substitute for human approval. | Return type of sha256; see its callable contract | Enclosing invocation or class/instance lifetime | 38 |
| policy_fingerprint | name | Current identifier selected by parsing, lookup or dependency registration. | Element of the declared iterable | Enclosing invocation or class/instance lifetime | 39 |
| ApprovalStore.__init__ | self | Owning instance; its attributes retain state for the instance lifetime. | Not explicitly annotated | Enclosing invocation or class/instance lifetime | 60 |
| ApprovalStore.__init__ | directory | Parameter for directory in ApprovalStore.__init__; use the enclosing contract and type below. | Path | Enclosing invocation or class/instance lifetime | 60 |
| ApprovalStore.__init__ | tools_root | Parameter for tools root in ApprovalStore.__init__; use the enclosing contract and type below. | Path | Enclosing invocation or class/instance lifetime | 60 |
| ApprovalStore.__init__ | protector | Parameter for protector in ApprovalStore.__init__; use the enclosing contract and type below. | DataProtector | Enclosing invocation or class/instance lifetime | 60 |
| ApprovalStore.__init__ | policy | Parameter for policy in ApprovalStore.__init__; use the enclosing contract and type below. | str | Enclosing invocation or class/instance lifetime | 60 |
| ApprovalStore.__init__ | self.directory | Attribute for directory in ApprovalStore.__init__; use the enclosing contract and type below. | Return type of resolve; see its callable contract | Enclosing invocation or class/instance lifetime | 63 |
| ApprovalStore.__init__ | self.root | Explicit root directory against which named paths are resolved. | Return type of normcase; see its callable contract | Enclosing invocation or class/instance lifetime | 64 |
| ApprovalStore.__init__ | self.protector | Attribute for protector in ApprovalStore.__init__; use the enclosing contract and type below. | tuple | Enclosing invocation or class/instance lifetime | 67 |
| ApprovalStore.__init__ | self.policy | Attribute for policy in ApprovalStore.__init__; use the enclosing contract and type below. | tuple | Enclosing invocation or class/instance lifetime | 67 |
| ApprovalStore.__init__ | self.namespace | Attribute for namespace in ApprovalStore.__init__; use the enclosing contract and type below. | Return type of hexdigest; see its callable contract | Enclosing invocation or class/instance lifetime | 68 |
| ApprovalStore._path | self | Owning instance; its attributes retain state for the instance lifetime. | Not explicitly annotated | Enclosing invocation or class/instance lifetime | 70 |
| ApprovalStore._path | tool_name | Validated public tool identifier within the configured storage boundary. | str | Enclosing invocation or class/instance lifetime | 70 |
| ApprovalStore._path | parent | Local binding for parent in ApprovalStore._path; use the enclosing contract and type below. | Runtime-dependent; see the enclosing callable contract | Enclosing invocation or class/instance lifetime | 76 |
| ApprovalStore._path | path | Path under validation or an explicitly scoped maintained source path. | Runtime-dependent; see the enclosing callable contract | Enclosing invocation or class/instance lifetime | 79 |
| ApprovalStore.save | self | Owning instance; its attributes retain state for the instance lifetime. | Not explicitly annotated | Enclosing invocation or class/instance lifetime | 85 |
| ApprovalStore.save | tool_name | Validated public tool identifier within the configured storage boundary. | str | Enclosing invocation or class/instance lifetime | 86 |
| ApprovalStore.save | code | Source snapshot passed through approval, syntax checks and isolated staging. | bytes | Enclosing invocation or class/instance lifetime | 87 |
| ApprovalStore.save | tests | Optional unittest source snapshot; child-authored success remains provisional. | bytes | Enclosing invocation or class/instance lifetime | 88 |
| ApprovalStore.save | digest | Content fingerprint for change detection; not a substitute for human approval. | str | Enclosing invocation or class/instance lifetime | 89 |
| ApprovalStore.save | functions | Parameter for functions in ApprovalStore.save; use the enclosing contract and type below. | frozenset[str] | Enclosing invocation or class/instance lifetime | 90 |
| ApprovalStore.save | contract | Validated declarative acceptance data bound to current artifact identities. | dict[str, Any] | Enclosing invocation or class/instance lifetime | 91, 100 |
| ApprovalStore.save | parse_contract | Imported dependency for parse contract in ApprovalStore.save; use the enclosing contract and type below. | Module or imported public symbol | Enclosing invocation or class/instance lifetime | 98 |
| ApprovalStore.save | record | Local binding for record in ApprovalStore.save; use the enclosing contract and type below. | Return type of dict; see its callable contract | Enclosing invocation or class/instance lifetime | 101 |
| ApprovalStore.save | raw | Local binding for raw in ApprovalStore.save; use the enclosing contract and type below. | Return type of encode; see its callable contract | Enclosing invocation or class/instance lifetime | 112 |
| ApprovalStore.save | sealed | Local binding for sealed in ApprovalStore.save; use the enclosing contract and type below. | Return type of seal; see its callable contract | Enclosing invocation or class/instance lifetime | 115 |
| ApprovalStore.save | path | Path under validation or an explicitly scoped maintained source path. | Return type of _path; see its callable contract | Enclosing invocation or class/instance lifetime | 118 |
| ApprovalStore.save | descriptor | Local binding for descriptor in ApprovalStore.save; use the enclosing contract and type below. | Return type of mkstemp; see its callable contract | Enclosing invocation or class/instance lifetime | 120 |
| ApprovalStore.save | temporary | Local binding for temporary in ApprovalStore.save; use the enclosing contract and type below. | Return type of mkstemp; see its callable contract | Enclosing invocation or class/instance lifetime | 120 |
| ApprovalStore.save | stream | Managed resource for stream in ApprovalStore.save; use the enclosing contract and type below. | Return type of fdopen; see its callable contract | Context-manager block; exit invokes its cleanup protocol | 122 |
| ApprovalStore.load | self | Owning instance; its attributes retain state for the instance lifetime. | Not explicitly annotated | Enclosing invocation or class/instance lifetime | 129 |
| ApprovalStore.load | tool_name | Validated public tool identifier within the configured storage boundary. | str | Enclosing invocation or class/instance lifetime | 129 |
| ApprovalStore.load | code | Source snapshot passed through approval, syntax checks and isolated staging. | bytes | Enclosing invocation or class/instance lifetime | 129 |
| ApprovalStore.load | tests | Optional unittest source snapshot; child-authored success remains provisional. | bytes | Enclosing invocation or class/instance lifetime | 129 |
| ApprovalStore.load | path | Path under validation or an explicitly scoped maintained source path. | Return type of _path; see its callable contract | Enclosing invocation or class/instance lifetime | 136 |
| ApprovalStore.load | stream | Managed resource for stream in ApprovalStore.load; use the enclosing contract and type below. | Return type of open; see its callable contract | Context-manager block; exit invokes its cleanup protocol | 139 |
| ApprovalStore.load | sealed | Local binding for sealed in ApprovalStore.load; use the enclosing contract and type below. | Return type of read; see its callable contract | Enclosing invocation or class/instance lifetime | 140 |
| ApprovalStore.load | plain | Local binding for plain in ApprovalStore.load; use the enclosing contract and type below. | Return type of unseal; see its callable contract | Enclosing invocation or class/instance lifetime | 143 |
| ApprovalStore.load | record | Local binding for record in ApprovalStore.load; use the enclosing contract and type below. | Return type of loads; see its callable contract | Enclosing invocation or class/instance lifetime | 146 |
| ApprovalStore.load.comprehension_162 | key | Comprehension item for key in ApprovalStore.load.comprehension_162; use the enclosing contract and type below. | Element of the declared iterable | This comprehension only; does not leak into its enclosing scope | 164 |
| ApprovalStore.load.comprehension_162 | value | Value at the current validation/rendering boundary; apply the enclosing contract. | Element of the declared iterable | This comprehension only; does not leak into its enclosing scope | 164 |
| ApprovalStore.load | parse_contract | Imported dependency for parse contract in ApprovalStore.load; use the enclosing contract and type below. | Module or imported public symbol | Enclosing invocation or class/instance lifetime | 174 |
| ApprovalStore.load | contract | Validated declarative acceptance data bound to current artifact identities. | Return type of parse_contract; see its callable contract | Enclosing invocation or class/instance lifetime | 176 |
| ApprovalStore.load | functions | Local binding for functions in ApprovalStore.load; use the enclosing contract and type below. | Runtime-dependent; see the enclosing callable contract | Enclosing invocation or class/instance lifetime | 177 |
| ApprovalStore.load.comprehension_181 | name | Current identifier selected by parsing, lookup or dependency registration. | Element of the declared iterable | This comprehension only; does not leak into its enclosing scope | 184 |
| ApprovalStore.load.comprehension_186 | case | Comprehension item for case in ApprovalStore.load.comprehension_186; use the enclosing contract and type below. | Element of the declared iterable | This comprehension only; does not leak into its enclosing scope | 186 |
| ApprovalStore.load | exc | Caught exception for exc in ApprovalStore.load; use the enclosing contract and type below. | (OSError, ValueError, TypeError, KeyError, RecursionError) | Current exception handler; Python clears this binding afterward | 192 |
| ApprovalStore.revoke | self | Owning instance; its attributes retain state for the instance lifetime. | Not explicitly annotated | Enclosing invocation or class/instance lifetime | 197 |
| ApprovalStore.revoke | tool_name | Validated public tool identifier within the configured storage boundary. | str | Enclosing invocation or class/instance lifetime | 197 |
| user_approval_store | tools_root | Parameter for tools root in user_approval_store; use the enclosing contract and type below. | Path | Enclosing invocation or class/instance lifetime | 202 |
| user_approval_store | directory | Local binding for directory in user_approval_store; use the enclosing contract and type below. | Return type of Path; see its callable contract | Enclosing invocation or class/instance lifetime | 204 |
